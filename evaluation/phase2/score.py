"""Score the Phase 2 predictions of the 85 graded evaluation incidents against EuRepoC labels.

    python evaluation/phase2/score.py --eurepoc <path to eurepoc_global_dataset_1_3.csv>

The gold labels are derived from the EuRepoC fields `incident_type` and `mitre_impact` with
`cddf.labels.labels_of` (the label rule used for the training incidents). For each objective type the prediction is
positive when its score in predictions_85.csv is at least θ (0.15), so an incident with an empty candidate set is
graded with three negative predictions. Per-type precision, recall and F1 are computed over the 85 incidents
(0 when undefined); Macro-F1 is the mean of the three F1 values. The majority baseline gives every incident the
share of each type among the 642 training incidents, scored at θ = 0.05 (its training cross-validation threshold on
the grid without 0.0).
The 95 % interval of the difference (Phase 2 minus majority) is a paired bootstrap over incidents: 10,000
resamples with `random.Random(20260820)`, incidents in the order of predictions_85.csv.
"""
from __future__ import annotations

import argparse
import csv
import random
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "src"))

from cddf.data import OBJECTIVES, Data          # noqa: E402
from cddf.labels import eurepoc_labels          # noqa: E402

THETA, THETA_MAJORITY, B, SEED = 0.15, 0.05, 10_000, 20260820


def f1(pairs) -> float:
    tp = sum(1 for p, g in pairs if p and g)
    fp = sum(1 for p, g in pairs if p and not g)
    fn = sum(1 for p, g in pairs if not p and g)
    prec = tp / (tp + fp) if tp + fp else 0.0
    rec = tp / (tp + fn) if tp + fn else 0.0
    return 2 * prec * rec / (prec + rec) if prec + rec else 0.0


def macro_f1(scores: list[dict], gold: list[set], theta: float) -> float:
    return sum(f1([(s[o] >= theta, o in g) for s, g in zip(scores, gold)]) for o in OBJECTIVES) / len(OBJECTIVES)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--eurepoc", required=True, type=Path)
    a = ap.parse_args()
    rows = list(csv.DictReader(open(HERE / "predictions_85.csv", encoding="utf-8", newline="")))
    gold_all = eurepoc_labels(a.eurepoc, [r["eurepoc_id"] for r in rows])
    gold = [{o for o in gold_all[r["eurepoc_id"]] if o in OBJECTIVES} for r in rows]
    absent = [r["eurepoc_id"] for r, g in zip(rows, gold) if not g]
    if absent:
        print(f"warning: {len(absent)} incidents have no label in this EuRepoC file: {absent}", file=sys.stderr)
    model = [{o: float(r[f"score_{o}"]) for o in OBJECTIVES} for r in rows]
    train = Data().training_incidents()
    maj_share = {o: sum(1 for c in train if o in c.objectives) / len(train) for o in OBJECTIVES}
    majority = [dict(maj_share) for _ in rows]
    m, b = macro_f1(model, gold, THETA), macro_f1(majority, gold, THETA_MAJORITY)
    rng, n, diffs = random.Random(SEED), len(rows), []
    for _ in range(B):
        ix = [rng.randrange(n) for _ in range(n)]
        diffs.append(macro_f1([model[i] for i in ix], [gold[i] for i in ix], THETA)
                     - macro_f1([majority[i] for i in ix], [gold[i] for i in ix], THETA_MAJORITY))
    diffs.sort()
    for o in OBJECTIVES:
        print(f"F1 {o}: {f1([(s[o] >= THETA, o in g) for s, g in zip(model, gold)]):.3f}")
    print(f"Macro-F1 (Phase 2, θ {THETA}): {m:.3f}  n = {n}")
    print(f"Macro-F1 (majority, θ {THETA_MAJORITY}): {b:.3f}")
    print(f"difference {m - b:+.3f}, 95% paired bootstrap interval [{diffs[int(0.025 * B)]:+.3f}, {diffs[int(0.975 * B)]:+.3f}]")
    return 0


if __name__ == "__main__":
    sys.exit(main())
