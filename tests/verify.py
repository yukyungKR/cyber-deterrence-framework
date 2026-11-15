"""Verification: run the CLI on the three evidence records and compare every result value with the reference values.

    python tests/verify.py            (from the repository root)

The reference values in tests/reference/ were extracted from the outputs of the original implementation of the
method. Similarities and Jaccard values are compared after rounding to 4 decimal places (the precision of the
reference outputs); all other values are compared exactly. Exit status 0 means that every item passed.
"""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REF = ROOT / "tests" / "reference"

RUNS = {
    "viasat": ("cases/viasat/evidence_record.json", [], "cases/viasat/results"),
    "binance": ("cases/binance/evidence_record.json", ["--include-same-actor", "--defender-state", "US"],
                "cases/binance/results"),
    "binance_22docs": ("cases/binance/evidence_record_22docs.json", ["--include-same-actor", "--defender-state", "US"],
                       "cases/binance/results_22docs"),
}


def run_cli(record: str, opts: list[str], out: Path) -> dict:
    env_path = str(ROOT / "src")
    cmd = [sys.executable, "-m", "cddf.run", "--record", str(ROOT / record), "--out", str(out), *opts]
    import os
    env = {**os.environ, "PYTHONPATH": env_path + os.pathsep + os.environ.get("PYTHONPATH", ""), "PYTHONUTF8": "1"}
    subprocess.run(cmd, check=True, env=env, cwd=ROOT, stdout=subprocess.DEVNULL)
    return json.loads((out / "result.json").read_text(encoding="utf-8"))


def compare(ref: dict, res: dict) -> list[tuple[str, bool, str]]:
    p2, p3, p4, a = res["phase2"], res["phase3"], res["phase4"], res["assessment"]
    items = []

    def check(name, expected, got):
        items.append((name, expected == got, "" if expected == got else f"expected {expected!r}, got {got!r}"))

    nb = p2["neighbours"]
    check("neighbour ids in order", [n["eurepoc_id"] for n in ref["neighbours"]], [n["eurepoc_id"] for n in nb])
    check("neighbour similarities (4 dp)", [n["similarity"] for n in ref["neighbours"]],
          [round(n["similarity"], 4) for n in nb])
    check("neighbour Jaccard values (4 dp)", [n["jaccard"] for n in ref["neighbours"]], [round(n["jaccard"], 4) for n in nb])
    check("neighbour objective labels", [n["objectives"] for n in ref["neighbours"]], [sorted(n["objectives"]) for n in nb])
    check("label frequencies", ref["frequencies"], {o: v["count"] for o, v in p2["frequencies"].items()})
    check("candidate objective set", ref["candidate_objectives"], sorted(p2["candidate_objectives"]))
    check("pool after exclusion list", ref["pool"]["after_exclusion_list"], p2["pool"]["after_exclusion_list"])
    check("precedent pool size", ref["pool"]["after_cutoff"], p2["pool"]["after_cutoff"])
    check("query pool size", ref["pool"]["query_pool"], p2["pool"]["query_pool"])
    check("actors in the precedent pool", ref["pool"]["n_actors_after_cutoff"], p2["pool"]["n_actors_after_cutoff"])
    got_m = {str(m["measure_id"]): {"status": m["status"], "required_grade": m["required_grade"],
                                    "attribution_met": m["attribution_met"] if m["status"] in
                                    ("available at any time", "open for review") else None}
             for m in p3["measures"]}
    ref_m = {k: {"status": v["status"], "required_grade": v["required_grade"],
                 "attribution_met": v["attribution_met"] if v["status"] in ("available at any time", "open for review") else None}
             for k, v in ref["measures"].items()}
    check("status of the 19 measures", {k: v["status"] for k, v in ref_m.items()}, {k: v["status"] for k, v in got_m.items()})
    check("required attribution grades", {k: v["required_grade"] for k, v in ref_m.items()},
          {k: v["required_grade"] for k, v in got_m.items()})
    check("attribution requirement met (open measures)", {k: v["attribution_met"] for k, v in ref_m.items()},
          {k: v["attribution_met"] for k, v in got_m.items()})
    check("self-defence review", ref["self_defence_review"], p3["self_defence"]["review"])
    check("countermeasures purpose", ref["countermeasures_purpose"], p3["countermeasures"]["purpose"])
    d = p3["d3fend"]
    check("number of D3FEND defensive techniques", ref["d3fend"]["n_defensive_techniques"], d["n_defensive_techniques"])
    check("set of D3FEND defensive techniques", ref["d3fend"]["defensive_techniques"],
          sorted(x["defensive_technique"] for x in d["defensive_techniques"]))
    check("number of artefacts", ref["d3fend"]["n_artifacts"], d["n_artifacts"])
    check("artefacts with defences", ref["d3fend"]["n_artifacts_with_defences"], d["n_artifacts_with_defences"])
    check("techniques without artefacts", ref["d3fend"]["techniques_without_artifacts"], d["techniques_without_artifacts"])
    check("techniques not in D3FEND", ref["d3fend"]["techniques_not_in_d3fend"], d["techniques_not_in_d3fend"])
    check("precedent response counts", [(n["eurepoc_id"], n["number_political_responses"], n["number_legal_responses"])
                                        for n in ref["phase4"]["neighbours"]],
          [(n["eurepoc_id"], n["political"]["count"], n["legal"]["count"]) for n in p4["neighbours"]])
    check("neighbours with a political response", ref["phase4"]["with_political_response"], p4["proportions"]["political"]["n"])
    check("neighbours with a legal response", ref["phase4"]["with_legal_response"], p4["proportions"]["legal"]["n"])
    check("judgements by deterrence type", ref["judgements"], {r["type"]: r["judgement"] for r in a["judgements"]})
    return items


#: keys of the evidence record that are not in the confirmed coding record: the filled technique set (it replaces the
#: coders' technique field) and two keys added for the run
RECORD_EXTRA_KEYS = {"techniques", "excluded_report_ids", "name_en"}


def check_record_against_confirmed(record: str) -> tuple[str, bool, str]:
    name = "evidence record equals the confirmed coding record (except technique set and added keys)"
    case = Path(record).parts[1]
    conf_path = ROOT / "coding" / case / "05_confirmed_record" / "confirmed_record.jsonl"
    if not conf_path.exists():
        return (name, False, f"coding/{case}/05_confirmed_record/confirmed_record.jsonl not found")
    conf = json.loads(conf_path.read_text(encoding="utf-8"))
    rec = json.loads((ROOT / record).read_text(encoding="utf-8"))
    diff = sorted(k for k in set(conf) | set(rec)
                  if k not in RECORD_EXTRA_KEYS and conf.get(k, "<absent>") != rec.get(k, "<absent>"))
    missing = sorted(k for k in RECORD_EXTRA_KEYS if k not in rec)
    ok = not diff and not missing
    return (name, ok, "" if ok else f"differing keys {diff}, missing keys {missing}")


def main() -> int:
    failed = 0
    with tempfile.TemporaryDirectory() as tmp:
        for run, (record, opts, committed) in RUNS.items():
            ref = json.loads((REF / f"{run}.json").read_text(encoding="utf-8"))
            res = run_cli(record, opts, Path(tmp) / run)
            items = [check_record_against_confirmed(record)] + compare(ref, res)
            cpath = ROOT / committed / "result.json"
            if cpath.exists():
                same = json.loads(cpath.read_text(encoding="utf-8")) == res
                items.append(("committed result.json equals a fresh run", same, "" if same else "differs"))
            bad = [x for x in items if not x[1]]
            failed += len(bad)
            print(f"{run}: {'PASS' if not bad else 'FAIL'} ({len(items) - len(bad)}/{len(items)} items)")
            for name, ok, why in items:
                print(f"  [{'ok' if ok else 'FAIL'}] {name}{'' if ok else ' - ' + why}")
    print("ALL PASSED" if not failed else f"{failed} item(s) failed")
    return 0 if not failed else 1


if __name__ == "__main__":
    sys.exit(main())
