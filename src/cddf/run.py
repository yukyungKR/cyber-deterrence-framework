"""Command-line entry point.

    python -m cddf.run --record <evidence_record.json> --out <dir> [--include-same-actor] [--defender-state US]

Writes ``result.json`` (all values) and ``summary.md`` (a short readable summary) into ``--out``.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from . import __version__, assessment, phase2, phase3, phase4
from . import record as R
from .data import Data
from .summary import to_markdown


def analyse(rec: dict, data: Data, include_same_actor: bool = False, defender_state: str | None = None) -> dict:
    p2 = phase2.run(rec, data, include_same_actor)
    p3 = phase3.run(rec, data, p2["candidate_objectives"], defender_state)
    p4 = phase4.run(p2["neighbours"], data)
    sector, sub = R.sectors(rec)
    return {
        "framework_version": __version__,
        "case_id": rec["case_id"], "name": rec.get("name_en") or rec["name"],
        "run_options": {"include_same_actor": include_same_actor, "defender_state": defender_state},
        "input": {"reference_date": rec["identified_date"], "actor": rec.get("actor"),
                  "n_techniques": len(R.techniques(rec)), "techniques": sorted(R.techniques(rec)),
                  "victim_sector": list(R.split_values(rec["victim_sector"])),
                  "victim_sector_sub": list(R.split_values(rec["victim_sector_sub"])),
                  "main_sector": sector, "main_sector_sub": sub,
                  "victim_assets": [a["value"] for a in rec.get("victim_assets") or []],
                  "intrusion_state": rec["intrusion_state"]["value"], "intrusion_depth": rec["access_depth"]["draft"],
                  "effects": {o: R.effect(rec, o) for o in R.EFFECT_TYPES.values()},
                  "armed_conflict_nexus": rec["conflict_nexus"],
                  "actor_identification_grade": rec["c_id"]["grade"], "state_attribution_grade": rec["c_st"]["grade"],
                  "state_attribution_reference_date": rec["c_st"].get("reference_date"),
                  "excluded_report_ids": sorted(rec.get("excluded_report_ids") or [])},
        "phase2": p2, "phase3": p3, "phase4": p4,
        "assessment": assessment.run(p3),
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="python -m cddf.run", description=__doc__.splitlines()[0])
    ap.add_argument("--record", required=True, type=Path, help="evidence record (JSON)")
    ap.add_argument("--out", required=True, type=Path, help="output directory")
    ap.add_argument("--include-same-actor", action="store_true",
                    help="keep precedents of the same actor in the pool (default: excluded)")
    ap.add_argument("--defender-state", default=None, help="state whose published positions are applied (US, UK, FR, DE, NL, KR)")
    ap.add_argument("--data", type=Path, default=None, help="data directory (default: the repository's data/)")
    a = ap.parse_args(argv)
    data = Data(a.data)
    try:
        rec = R.load(a.record, data)
    except R.RecordError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    res = analyse(rec, data, a.include_same_actor, a.defender_state)
    a.out.mkdir(parents=True, exist_ok=True)
    (a.out / "result.json").write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
    (a.out / "summary.md").write_text(to_markdown(res), encoding="utf-8", newline="\n")
    print(f"{res['case_id']}: results written to {a.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
