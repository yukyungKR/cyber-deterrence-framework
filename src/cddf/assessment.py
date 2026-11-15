"""Deterrence strategy assessment: the Phase 3 statuses restated as one judgement per deterrence type.

- available: the type contains at least one measure that is available at any time or open for review, and the
  attribution grade that measure requires is met (or none is required);
- conditionally available: such a measure exists but the state-attribution grade falls short, or the only measures
  left depend on a condition (the state's position on sovereignty, the authorisation or consent of the other state);
- unavailable: every measure of the type is excluded or has no basis for review.

Punishment is judged in four sub-items. Entanglement and the measures outside the four types receive no judgement.
The assessment takes no input beyond the review results and the state-attribution grade.
"""
from __future__ import annotations

from . import phase3 as P3

AVAILABLE, CONDITIONAL, UNAVAILABLE = "available", "conditionally available", "unavailable"

TYPE_ROWS = [
    ("denial", (15, 16), "the defending state's position on sovereignty; where the action takes effect"),
    ("punishment: diplomatic and economic", (2, 3, 4, 5, 6, 7, 8, 9, 19),
     "grounds of state attribution; whether another international obligation is breached"),
    ("punishment: law enforcement", (10, 11), "authorisation or consent of the other state"),
    ("punishment: countermeasures", (12,), "prior wrongful act; conditions of exercise and termination"),
    ("punishment: self-defence", (13,), "necessity, proportionality, temporal relation"),
    ("norms", (1,), "grounds of state attribution; whether another international obligation is breached"),
]
NO_JUDGEMENT_ROWS = [
    ("entanglement", (18,), "whether treaties and cooperation exist at the time"),
    ("outside the four types", (14, 17), "whether the victim sector is an essential interest (plea of necessity)"),
]
OPEN = (P3.AVAILABLE, P3.OPEN)
CLOSED = (P3.EXCLUDED, P3.NO_BASIS)
CONDITION = (P3.STATE_POSITION, P3.CONSENT)


def classify(m: dict, c_st: int) -> str:
    st, req = m["status"], m["required_grade"]
    if st in OPEN:
        return "available" if req is None or c_st >= req else "attribution_short"
    if st in CONDITION:
        return "condition"
    if st in CLOSED:
        return "closed"
    if st == P3.TIMING_INDEPENDENT:
        return "off_axis"
    raise ValueError(f"measure {m['measure_id']}: status {st!r} has no rule")


def judge(kinds: set[str]) -> str:
    if "available" in kinds:
        return AVAILABLE
    if kinds & {"attribution_short", "condition"}:
        return CONDITIONAL
    assert kinds <= {"closed"}, kinds
    return UNAVAILABLE


def run(phase3: dict) -> dict:
    if "measures" not in phase3:
        return {"note": "no assessment: the incident is set aside for examination under international humanitarian law"}
    c_st = phase3["state_attribution_grade"]
    by_id = {m["measure_id"]: m for m in phase3["measures"]}
    rows = []
    for typ, ids, extra in TYPE_ROWS:
        items = [{"measure_id": i, "name": by_id[i]["name"], "status": by_id[i]["status"],
                  "required_grade": by_id[i]["required_grade"], "kind": classify(by_id[i], c_st)} for i in ids]
        rows.append({"type": typ, "judgement": judge({x["kind"] for x in items}),
                     "available_measures": [x["measure_id"] for x in items if x["kind"] == "available"],
                     "conditional_or_closed": [{"measure_id": x["measure_id"], "status": x["status"],
                                                "reason": "attribution grade below the required grade"
                                                if x["kind"] == "attribution_short" else x["status"]}
                                               for x in items if x["kind"] != "available"],
                     "further_confirmation": extra, "measures": items})
    no_judgement = []
    for typ, ids, extra in NO_JUDGEMENT_ROWS:
        items = [{"measure_id": i, "name": by_id[i]["name"], "status": by_id[i]["status"],
                  "kind": classify(by_id[i], c_st)} for i in ids]
        no_judgement.append({"type": typ, "judgement": None,
                             "available_measures": [x["measure_id"] for x in items if x["kind"] == "available"],
                             "further_confirmation": extra, "measures": items})
    return {"state_attribution_grade": c_st,
            "summary": {v: [r["type"] for r in rows if r["judgement"] == v] for v in (AVAILABLE, CONDITIONAL, UNAVAILABLE)},
            "judgements": rows, "no_judgement": no_judgement,
            "note": "A judgement of available means that the conditions are in place for examining the measures of "
                    "that type in law and policy; it is not a recommendation."}
