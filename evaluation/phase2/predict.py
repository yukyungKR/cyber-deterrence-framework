"""Phase 2 predictions for the 85 graded evaluation incidents (unmasked condition).

    python evaluation/phase2/predict.py        (from the repository root, with src/ on PYTHONPATH)

Reads queries_85.csv and data/incidents.csv; writes predictions_85.csv. No label of an evaluation incident is read.
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "src"))

from cddf.data import OBJECTIVES, Data          # noqa: E402
from cddf import phase2 as P2                   # noqa: E402


def majority_shares(pool) -> dict:
    """Majority baseline: share of each objective type among the precedent pool."""
    n = len(pool) or 1
    return {o: sum(1 for c in pool if o in c.objectives) / n for o in OBJECTIVES}


def main() -> int:
    data = Data()
    train = data.training_incidents()
    train_docs = {d for c in train for d in c.reports}
    rows = list(csv.DictReader(open(HERE / "queries_85.csv", encoding="utf-8", newline="")))
    out = []
    for q in rows:
        docs = [d for d in q["linked_report_ids"].split(";") if d]
        assert not set(docs) & train_docs, f"{q['eurepoc_id']}: an evaluation report is in the precedent pool"
        tech = frozenset(t for t in q["techniques"].split(";") if t)
        pool = [c for c in train if c.actor != q["actor"]]            # same-actor rule (no match occurs)
        nb, counts, _ = P2.estimate(tech, q["sector"], pool)
        empty = not tech
        shares = majority_shares(pool) if empty else {o: counts[o] / P2.K for o in OBJECTIVES}
        cand = [o for o in OBJECTIVES if shares[o] >= P2.THETA]
        out.append([q["eurepoc_id"], q["linked_report_ids"], len(tech), *(c.eurepoc_id for _, c in nb),
                    *(counts[o] for o in OBJECTIVES), *(repr(shares[o]) for o in OBJECTIVES),
                    int(empty), ";".join(cand), len(train) - len(pool)])
    hdr = (["eurepoc_id", "linked_report_ids", "n_techniques"] + [f"neighbour_{i}" for i in range(1, P2.K + 1)]
           + [f"count_{o}" for o in OBJECTIVES] + [f"score_{o}" for o in OBJECTIVES]
           + ["empty_query_majority_substituted", "candidate_objectives", "same_actor_precedents_removed"])
    with open(HERE / "predictions_85.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(hdr)
        w.writerows(out)
    print(f"{len(out)} predictions written; {sum(r[-3] for r in out)} empty queries substituted")
    return 0


if __name__ == "__main__":
    sys.exit(main())
