"""Phase 3: review of the 19 response measures at the time of identification."""
from __future__ import annotations

from .data import Data
from . import record as R
from . import d3fend

# Review statuses and treatments (wording of the article)
AVAILABLE = "available at any time"
OPEN = "open for review"
EXCLUDED = "excluded"
NO_BASIS = "no basis for review"
STATE_POSITION = "depends on the state's position"
CONSENT = "subject to authorisation or consent"
TIMING_INDEPENDENT = "independent of timing"

#: Requirements the legal adviser and the policymaker confirm once a review is open.
FURTHER_CONFIRMATION = {
    12: "prior internationally wrongful act; conditions of exercise and termination",
    13: "scale and effects of the attack; necessity; proportionality",
    14: "requirements of ARSIWA Article 25",
}

#: Sovereignty positions: verdict on forward cyber defence operations and on countermeasures against an ongoing
#: intrusion without effect.
FORWARD_VIEW = {"principle": "may be claimed to be available", "purist": "may be unlawful",
                "effects": "room remains for operations whose effects fall below the threshold",
                "silent": "position not stated"}
ONGOING_CM_VIEW = {"purist": OPEN, "principle": EXCLUDED, "effects": EXCLUDED, "silent": "position to be confirmed"}

IMMINENCE_DEPTH = ("core", "ot")
WINDOW = {"none": "window of opportunity not formed", "persisting": "window of opportunity formed and continuing",
          "terminated": "window of opportunity closed", "indeterminate": "window of opportunity indeterminate"}
INTERDICTION = {"post": "no opportunity to prevent the disruption remains (effect observed)",
                "pre": "an opportunity to prevent the disruption remains (effect not observed)",
                "indeterminate": "opportunity to prevent the disruption indeterminate"}


def timing_state(effect: str, intrusion: str) -> str:
    """State of the incident for the prior-wrongful-act question: an effect first, then the intrusion state.
    An indeterminate intrusion state is treated as not established."""
    if effect == "post":
        return "effect_observed"
    return {"persisting": "intrusion_ongoing", "terminated": "intrusion_terminated"}.get(intrusion,
                                                                                          "intrusion_not_established")


def countermeasures(timing: str, intrusion: str, data: Data, defender: str | None) -> dict:
    by_state = {s: ONGOING_CM_VIEW[p["sovereignty_position"]] for s, p in data.state_positions.items()}
    if timing == "effect_observed":
        status, reason = OPEN, "an effect is observed: breach of an obligation and attribution to the state are examined in turn"
    elif timing == "intrusion_ongoing":
        status, reason = STATE_POSITION, ("no effect observed and the intrusion is ongoing: open where unauthorised "
                                          "access is itself a violation of sovereignty, excluded where sovereignty is a "
                                          "principle or an effects threshold applies, to be confirmed where no position "
                                          "is stated")
    elif timing == "intrusion_terminated":
        status, reason = OPEN, "no effect observed and the intrusion has terminated: open for the purpose of reparation only"
    else:
        status, reason = EXCLUDED, "no effect observed and no intrusion established: no prior wrongful act (countermeasures are not preventive)"
    purpose = None
    if status != EXCLUDED:
        purpose = {"persisting": "cessation", "terminated": "reparation"}.get(intrusion)
    out = {"status": status, "reason": reason, "purpose": purpose}
    if timing == "intrusion_ongoing":
        out["by_state"] = by_state
        if defender:
            out["defender_state_view"] = by_state[defender]
    return out


def self_defence(rec: dict, candidates: list[str]) -> dict:
    e3 = R.effect(rec, "disruption_destruction")
    depth = rec["access_depth"]["draft"]
    if e3 == "post":
        return {"status": OPEN, "review": "armed attack",
                "reason": "disruption and destruction is observed: review of whether the incident amounts to an armed attack"}
    if "disruption_destruction" in candidates:
        factor = "present" if depth in IMMINENCE_DEPTH else "weak"
        return {"status": OPEN, "review": "imminence", "imminence_factor": f"{factor} (intrusion depth {depth})",
                "reason": "disruption and destruction is not observed but is in the candidate objective set: review "
                          "of imminence (the candidate starts the review and does not itself satisfy imminence)"}
    return {"status": NO_BASIS, "review": None,
            "reason": "disruption and destruction is neither observed nor in the candidate objective set"}


def necessity(rec: dict, data: Data, candidates: list[str]) -> dict:
    if not R.is_essential(rec, data):
        return {"status": EXCLUDED, "reason": "the victim sector is not an essential-interest sector"}
    e3 = R.effect(rec, "disruption_destruction")
    return {"status": OPEN, "reason": "the victim sector is an essential-interest sector",
            "elements": {  # listed for the review, not judged
                "intrusion_state": WINDOW[rec["intrusion_state"]["value"]],
                "intrusion_depth": rec["access_depth"]["draft"],
                "opportunity_to_prevent": INTERDICTION[e3],
                "disruption_destruction_observed": e3,
                "disruption_destruction_in_candidates": "disruption_destruction" in candidates}}


def forward_defence(data: Data, defender: str | None) -> dict:
    by_state = {s: FORWARD_VIEW[p["sovereignty_position"]] for s, p in data.state_positions.items()}
    out = {"status": STATE_POSITION, "reason": "depends on the state's position on sovereignty", "by_state": by_state}
    if defender:
        out["defender_state_view"] = by_state[defender]
    return out


def run(rec: dict, data: Data, candidates: list[str], defender: str | None = None) -> dict:
    if defender is not None and defender not in data.state_positions:
        raise ValueError(f"defender state {defender!r} not in {tuple(data.state_positions)}")
    nexus = rec["conflict_nexus"]
    if nexus == "established":
        return {"armed_conflict_nexus": nexus, "path": "international humanitarian law",
                "note": "an armed-conflict nexus is established: the incident is set aside for separate examination "
                        "under international humanitarian law and the peacetime review is not made"}
    effect = rec["effect_realized"]["value"]
    intrusion = rec["intrusion_state"]["value"]
    timing = timing_state(effect, intrusion)
    cm = countermeasures(timing, intrusion, data, defender)
    sd = self_defence(rec, candidates)
    ne = necessity(rec, data, candidates)
    fw = forward_defence(data, defender)
    c_st = rec["c_st"]["grade"]
    detail = {12: cm, 13: sd, 14: ne, 16: fw}
    measures = []
    for m in data.measures:
        mid, tr = m["measure_id"], m["treatment"]
        if mid in detail:
            status, reason = detail[mid]["status"], detail[mid]["reason"]
        elif tr == "always":
            status = AVAILABLE
            reason = ("available at any time, provided that the measure breaches no other international obligation"
                      if m["legal_character"] == "retorsion" else "available at any time")
        elif tr == "consent":
            status, reason = CONSENT, "requires the authorisation or consent of the other state; otherwise treated as countermeasures"
        elif tr == "timing_independent":
            status, reason = TIMING_INDEPENDENT, "only the existence of treaties and cooperation is recorded"
        else:  # pragma: no cover - table error
            raise ValueError(f"measure {mid}: treatment {tr!r} has no rule")
        req = m["required_grade"]
        measures.append({"measure_id": mid, "name": m["name"], "deterrence_type": m["deterrence_type"],
                         "punishment_subitem": m["punishment_subitem"] or None, "legal_character": m["legal_character"] or None,
                         "treatment": tr, "status": status, "reason": reason, "required_grade": req,
                         # met when the state-attribution grade reaches the required grade, or no grade is required
                         "attribution_met": True if req is None else c_st >= req,
                         **({"further_confirmation": FURTHER_CONFIRMATION[mid]} if mid in FURTHER_CONFIRMATION and status == OPEN else {})})
    out = {"armed_conflict_nexus": nexus, "path": "peacetime", "timing_state": timing,
           "state_attribution_grade": c_st, "measures": measures,
           "countermeasures": cm, "self_defence": sd, "necessity": ne, "forward_cyber_defence": fw,
           "defender_state": defender,
           "d3fend": d3fend.derive(rec["techniques"], data)}
    if defender:
        p = data.state_positions[defender]
        out["defender_state_position"] = {"state": defender, "sovereignty_position": p["sovereignty_position"],
                                          "forward_cyber_defence": FORWARD_VIEW[p["sovereignty_position"]],
                                          "due_diligence": p["due_diligence"]}
    return out
