"""Derivation of defensive techniques from the observed techniques through MITRE D3FEND 1.6.0.

Path: ATT&CK technique -> digital artefact it acts on (offensive relations of the technique class, inherited from
its ancestor and descendant ATT&CK technique classes) -> defensive techniques attached to that artefact or to one of
its superclasses -> defensive tactic. The tables in ``data/d3fend/`` hold these relations, precomputed from the
ontology. No ranking or score is implied by the derivation.
"""
from __future__ import annotations

from .data import Data

NO_TACTIC = "(no tactic)"


def derive(techniques, data: Data) -> dict:
    techs = sorted({str(t).strip().upper() for t in techniques})
    per_tech: dict[str, dict] = {}
    artifacts: dict[str, dict] = {}
    defensive: dict[str, dict] = {}
    for t in techs:
        arts = data.d3fend_artifacts.get(t, [])
        defs_t: set[str] = set()
        for a in arts:
            ent = artifacts.setdefault(a["artifact"], {"artifact": a["artifact"], "label": a["artifact_label"],
                                                       "relations": {}})
            ent["relations"].setdefault(a["relation"], set()).add(t)
        for x in sorted({a["artifact"] for a in arts}):
            for d in data.d3fend_defences.get(x, []):
                defs_t.add(d["defensive_technique"])
                ent = defensive.setdefault(d["defensive_technique"], {
                    "defensive_technique": d["defensive_technique"], "label": d["defensive_technique_label"],
                    "d3fend_id": d["d3fend_id"], "tactics": set(), "attack_techniques": set(), "artifacts": set()})
                ent["tactics"].update(d["tactics"].split(";") if d["tactics"] else [NO_TACTIC])
                ent["attack_techniques"].add(t)
                ent["artifacts"].add(x)
                artifacts[x]["has_defence"] = True
        per_tech[t] = {"in_d3fend": t in data.d3fend_attack_ids,
                       "artifacts": sorted({(a["relation"], a["artifact"]) for a in arts}),
                       "n_defensive_techniques": len(defs_t)}
    defs = []
    for d in sorted(defensive.values(), key=lambda e: (e["label"] or e["defensive_technique"], e["defensive_technique"])):
        defs.append({"defensive_technique": d["defensive_technique"], "label": d["label"], "d3fend_id": d["d3fend_id"],
                     "tactics": sorted(d["tactics"]), "n_attack_techniques": len(d["attack_techniques"]),
                     "attack_techniques": sorted(d["attack_techniques"]), "via_artifacts": sorted(d["artifacts"])})
    tactic_counts: dict[str, int] = {}
    for d in defs:
        for tc in d["tactics"]:
            tactic_counts[tc] = tactic_counts.get(tc, 0) + 1
    arts_out = [{"artifact": a["artifact"], "label": a["label"], "has_defence": bool(a.get("has_defence")),
                 "relations": {r: sorted(ts) for r, ts in sorted(a["relations"].items())}}
                for a in sorted(artifacts.values(), key=lambda a: (a["label"] or a["artifact"], a["artifact"]))]
    return {
        "d3fend_version": "1.6.0",
        "n_techniques": len(techs),
        "techniques_not_in_d3fend": [t for t in techs if not per_tech[t]["in_d3fend"]],
        "techniques_without_artifacts": [t for t in techs if not per_tech[t]["artifacts"]],
        "n_techniques_with_artifacts": sum(1 for t in techs if per_tech[t]["artifacts"]),
        "n_artifacts": len(arts_out),
        "n_artifacts_with_defences": sum(1 for a in arts_out if a["has_defence"]),
        "n_defensive_techniques": len(defs),
        "defensive_tactic_counts": dict(sorted(tactic_counts.items())),
        "defensive_techniques": defs,
        "technique_artifacts": {t: [{"relation": r, "artifact": a} for r, a in v["artifacts"]] for t, v in per_tech.items()},
        "artifacts": arts_out,
        "note": "Candidate set derived from the D3FEND ontology relations; it does not rank defences or assess their "
                "effect. n_attack_techniques is the number of observed techniques whose artefacts the defensive "
                "technique protects.",
    }
