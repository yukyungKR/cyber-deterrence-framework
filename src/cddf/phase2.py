"""Phase 2: objective estimation from similar precedents."""
from __future__ import annotations

from .data import OBJECTIVES, Data, Incident
from . import record as R

#: Settings chosen on the training incidents by five-fold cross-validation partitioned by actor.
K = 7
W_TECHNIQUE = 0.9
W_SECTOR = 0.1
THETA = 0.15

MISSING_SECTOR = ("", R.INDETERMINATE)

#: Techniques of the ATT&CK Persistence tactic and later stages used by the dormancy rule
#: (sub-techniques are folded into their parent technique).
PERSISTENCE_TECHNIQUES = frozenset({"T1053", "T1078", "T1133", "T1542", "T1543"})
BEYOND_PERSISTENCE_TECHNIQUES = frozenset({
    "T1005", "T1056", "T1113", "T1114", "T1123", "T1560",                                  # collection
    "T1041", "T1567",                                                                      # exfiltration
    "T1485", "T1486", "T1489", "T1490", "T1491", "T1495", "T1498", "T1565", "T1657",       # impact
})


def jaccard(a: frozenset, b: frozenset) -> float:
    if not a and not b:
        return 0.0
    return len(a & b) / len(a | b)


def sector_match(a: str, b: str) -> float:
    """1 if the two main sectors are equal; a missing sector contributes nothing."""
    if a in MISSING_SECTOR or b in MISSING_SECTOR:
        return 0.0
    return 1.0 if a == b else 0.0


def similarity(q_tech: frozenset, q_sector: str, c: Incident) -> float:
    return W_TECHNIQUE * jaccard(q_tech, c.techniques) + W_SECTOR * sector_match(q_sector, c.sector)


def is_eligible(e, reference_date: str) -> bool:
    """A precedent is eligible at the reference date of the technical state.

    - If a linked report was published on or before the reference date, the precedent is eligible unless its
      recorded start date is later than the reference date.
    - If no linked report has a known date, or all dated reports are later and at least one report is undated,
      the start date decides: eligible if it is on or before the reference date, not eligible if it is unknown.
    - If all linked reports are dated and all are later than the reference date, the precedent is not eligible.
    """
    d, start = e.earliest_report_date, e.start_date
    if d is not None and d <= reference_date:
        return not (start is not None and start > reference_date)
    if d is None or e.n_reports_undated > 0:
        return start is not None and start <= reference_date
    return False


def precedent_pool(rec: dict, data: Data, include_same_actor: bool = False) -> tuple[list[Incident], dict]:
    """Training incidents, less those built from the incident's own documents, less precedents not yet eligible
    at the reference date, less (by default) precedents of the same actor (exact string match)."""
    train = data.training_incidents()
    own = set(rec.get("excluded_report_ids") or [])
    excluded = sorted((i.eurepoc_id for i in train if own & set(i.reports)), key=int)
    after_list = [i for i in train if i.eurepoc_id not in set(excluded)]
    ref = rec["identified_date"]
    after_cutoff = [i for i in after_list if is_eligible(data.eligibility[i.eurepoc_id], ref)]
    actor = (rec.get("actor") or "").strip()
    same = [i for i in after_cutoff if i.actor == actor]
    query = after_cutoff if include_same_actor else [i for i in after_cutoff if i.actor != actor]
    if not query:
        raise RuntimeError("the precedent pool is empty")
    info = {"training_incidents": len(train), "excluded_own_documents": excluded,
            "after_exclusion_list": len(after_list), "reference_date": ref, "after_cutoff": len(after_cutoff),
            "n_actors_after_cutoff": len({i.actor for i in after_cutoff}),
            "same_actor_precedents": len(same), "same_actor_excluded": not include_same_actor,
            "query_pool": len(query)}
    return query, info


def dormancy_rule(rec: dict) -> tuple[bool, str]:
    """Dormancy (persistent access without a visible effect) by rule."""
    ts = rec.get("target_specificity")
    observed = [R.EFFECT_TYPES[y] for y, v in rec["effect_realized"]["by_type"].items() if v == "post"]
    if observed:
        return False, f"an effect is observed ({', '.join(observed)})"
    if ts == "capability_only":
        return True, "capability captured before deployment"
    if rec["intrusion_state"]["value"] != "persisting":
        return False, f"the intrusion is not ongoing ({rec['intrusion_state']['value']})"
    tech = {t.split(".")[0] for t in R.techniques(rec)}
    if not tech & PERSISTENCE_TECHNIQUES:
        return False, "no persistence technique is observed"
    beyond = sorted(tech & BEYOND_PERSISTENCE_TECHNIQUES)
    if beyond:
        return False, f"collection, exfiltration or impact techniques are observed ({', '.join(beyond)})"
    return True, f"persistence ({', '.join(sorted(tech & PERSISTENCE_TECHNIQUES))}) without later-stage techniques"


def objective_unestablished_rule(rec: dict) -> tuple[bool, str]:
    """No objective can be examined: a specific victim, no intrusion and no effect."""
    if rec.get("target_specificity") != "specific_victim":
        return False, "the target is not a specific victim"
    observed = [R.EFFECT_TYPES[y] for y, v in rec["effect_realized"]["by_type"].items() if v == "post"]
    if observed:
        return False, f"an effect is observed ({', '.join(observed)})"
    if rec["intrusion_state"]["value"] != "none":
        return False, f"an intrusion is established ({rec['intrusion_state']['value']})"
    return True, "specific victim, no intrusion and no effect observed"


def rule_layer(rec: dict) -> dict:
    """Rule-based values checked before the precedent estimate.

    If no objective can be examined, the precedent estimate is reported for reference only. The dormancy rule is
    held at the time of identification when no effect has been observed yet (the condition 'no visible effect'
    is then met by construction); the precedent estimate stays the main output and the hold is reported."""
    ou, ou_why = objective_unestablished_rule(rec)
    dm, dm_why = dormancy_rule(rec)
    before_effect = rec["effect_realized"]["value"] != "post"
    if ou:
        state = "objective_unestablished"
    elif dm and not before_effect:
        state = "dormancy"
    else:
        state = None
    return {"state": state, "estimate_role": "reference" if state else "main",
            "objective_unestablished": {"applies": ou, "reason": ou_why},
            "dormancy": {"rule_true": dm, "held": bool(dm and before_effect), "reason": dm_why}}


def estimate(q_tech: frozenset, q_sector: str, pool: list[Incident]) -> tuple[list, dict, list[str]]:
    """The K nearest precedents, the count of each objective type among them, and the candidate objective set."""
    scored = sorted(((similarity(q_tech, q_sector, c), c) for c in pool), key=lambda t: (-t[0], t[1].eurepoc_id))
    nb = scored[:K]
    if len(nb) != K:
        raise RuntimeError(f"only {len(nb)} precedents in the pool; {K} are needed")
    counts = {o: sum(1 for _, c in nb if o in c.objectives) for o in OBJECTIVES}
    candidates = [o for o in OBJECTIVES if counts[o] / K >= THETA and counts[o] > 0]
    return nb, counts, candidates


def run(rec: dict, data: Data, include_same_actor: bool = False) -> dict:
    pool, info = precedent_pool(rec, data, include_same_actor)
    q_tech = R.techniques(rec)
    q_sector, _ = R.sectors(rec)
    nb, counts, candidates = estimate(q_tech, q_sector, pool)
    shares = {o: counts[o] / K for o in OBJECTIVES}
    neighbours = []
    for rank, (s, c) in enumerate(nb, start=1):
        neighbours.append({
            "rank": rank, "eurepoc_id": c.eurepoc_id, "incident_name": c.name, "actor": c.actor,
            "similarity": s, "jaccard": jaccard(q_tech, c.techniques),
            "sector_match": sector_match(q_sector, c.sector) == 1.0, "sector": c.sector,
            "objectives": [o for o in OBJECTIVES if o in c.objectives],
            "common_techniques": sorted(q_tech & c.techniques),
        })
    return {
        "settings": {"k": K, "weight_technique": W_TECHNIQUE, "weight_sector": W_SECTOR, "weight_asset": 0.0,
                     "threshold": THETA, "tie_break": "eurepoc_id (string order)"},
        "pool": info,
        "neighbours": neighbours,
        "frequencies": {o: {"count": counts[o], "share": shares[o]} for o in OBJECTIVES},
        "candidate_objectives": candidates,
        "rule_layer": rule_layer(rec),
    }
