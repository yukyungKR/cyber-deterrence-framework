"""Short readable summary of a result (Markdown)."""
from __future__ import annotations

LABEL = {"exfiltration": "exfiltration", "manipulation_disclosure": "manipulation and disclosure",
         "disruption_destruction": "disruption and destruction"}
EFFECT = {"post": "observed", "pre": "not observed", "indeterminate": "indeterminate"}
INTRUSION = {"none": "not established", "persisting": "ongoing", "terminated": "terminated", "indeterminate": "indeterminate"}
DEPTH = {"external": "external systems", "office": "enterprise IT", "core": "mission-critical systems",
         "ot": "operational technology", "indeterminate": "indeterminate"}


def _objs(xs) -> str:
    return ", ".join(LABEL[x] for x in xs) if xs else "none"


def to_markdown(res: dict) -> str:
    i, p2, p3, p4, a = res["input"], res["phase2"], res["phase3"], res["phase4"], res["assessment"]
    opts = res["run_options"]
    L = [f"# {res['name']} ({res['case_id']})", ""]
    L += ["## Input", "",
          f"- Reference date of the technical state: {i['reference_date']}",
          f"- Techniques: {i['n_techniques']}",
          f"- Victim sector: {', '.join(i['victim_sector_sub'])}",
          f"- Intrusion: {INTRUSION[i['intrusion_state']]}; depth: {DEPTH[i['intrusion_depth']]}",
          "- Effects: " + "; ".join(f"{LABEL[k]} {EFFECT[v]}" for k, v in i["effects"].items()),
          f"- Armed-conflict nexus: {i['armed_conflict_nexus']}",
          f"- Actor-identification grade {i['actor_identification_grade']}; state-attribution grade "
          f"{i['state_attribution_grade']}",
          f"- Options: same-actor precedents {'kept' if opts['include_same_actor'] else 'excluded'}; defending state "
          f"{opts['defender_state'] or 'not set'}", ""]
    pool = p2["pool"]
    L += ["## Phase 2: objective estimation", "",
          f"Precedent pool: {pool['training_incidents']} training incidents; {len(pool['excluded_own_documents'])} built "
          f"from the incident's own documents removed ({pool['after_exclusion_list']}); {pool['after_cutoff']} eligible on "
          f"{pool['reference_date']}; query pool {pool['query_pool']}.", "",
          "| Rank | EuRepoC id | Actor | Similarity | Jaccard | Objectives |", "|--:|--|--|--:|--:|--|"]
    for n in p2["neighbours"]:
        L.append(f"| {n['rank']} | {n['eurepoc_id']} | {n['actor']} | {n['similarity']:.4f} | {n['jaccard']:.4f} | "
                 f"{_objs(n['objectives'])} |")
    L += ["", "Frequencies: " + "; ".join(f"{LABEL[o]} {v['count']}/{p2['settings']['k']}"
                                          for o, v in p2["frequencies"].items()),
          f"Candidate objective set: {_objs(p2['candidate_objectives'])}.", ""]
    L += ["## Phase 3: review of response measures", ""]
    if "measures" not in p3:
        L += [p3["note"], ""]
    else:
        L += ["| No. | Measure | Status | Attribution grade required | Met |", "|--:|--|--|--:|--|"]
        for m in p3["measures"]:
            met = "not required" if m["required_grade"] is None else ("yes" if m["attribution_met"] else "no")
            L.append(f"| {m['measure_id']} | {m['name']} | {m['status']} | {m['required_grade'] or '-'} | {met} |")
        cm, sd = p3["countermeasures"], p3["self_defence"]
        d = p3["d3fend"]
        L += ["", f"Countermeasures: {cm['status']}; purpose: {cm['purpose'] or 'not determined'}.",
              f"Self-defence: {sd['status']}" + (f" ({sd['review']})" if sd.get("review") else "") + ".",
              f"Plea of necessity: {p3['necessity']['status']}.",
              *([f"Defending state {p3['defender_state']}: sovereignty as {p3['defender_state_position']['sovereignty_position']}; "
                 f"forward cyber defence operations {p3['defender_state_position']['forward_cyber_defence']} "
                 "(the status of measure 16 is not changed)."] if p3.get("defender_state") else []),
              f"Defensive techniques (D3FEND {d['d3fend_version']}): {d['n_defensive_techniques']}, through "
              f"{d['n_artifacts_with_defences']} of {d['n_artifacts']} artefacts; {d['n_techniques_with_artifacts']} of "
              f"{d['n_techniques']} techniques are linked to artefacts.", ""]
    pr = p4["proportions"]
    L += ["## Phase 4: precedent responses", "",
          f"Neighbours with a political response: {pr['political']['n']}/{pr['political']['of']}; with a legal "
          f"response: {pr['legal']['n']}/{pr['legal']['of']}.", ""]
    for n in p4["neighbours"]:
        if n["no_record_found"]:
            L.append(f"- {n['eurepoc_id']}: no record found")
        else:
            parts = [f"{t} {n[t]['count_raw']}" for t in ("political", "legal") if n[t]["has_response"]]
            L.append(f"- {n['eurepoc_id']}: " + "; ".join(parts))
    L += ["", "## Deterrence strategy assessment", ""]
    if "judgements" not in a:
        L += [a["note"], ""]
    else:
        L += ["| Deterrence type | Judgement | Available measures |", "|--|--|--|"]
        for r in a["judgements"]:
            L.append(f"| {r['type']} | {r['judgement']} | {', '.join(map(str, r['available_measures'])) or '-'} |")
        L += ["", "Entanglement and the measures outside the four types receive no judgement.", "", a["note"], ""]
    return "\n".join(L)
