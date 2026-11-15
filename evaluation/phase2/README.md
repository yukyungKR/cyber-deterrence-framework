# Phase 2 evaluation: predictions for the 85 graded evaluation incidents

The evaluation is published as per-incident predictions so that it can be rescored. The gold labels are not in this
repository; they are derived from the EuRepoC Global Dataset v1.3 (DOI 10.5281/zenodo.14965395) by `score.py`.

## Files

| File | Content |
|---|---|
| `queries_85.csv` | the 85 queries: EuRepoC incident id, actor, linked ORKL report ids, sector and sub-sector, technique set |
| `predict.py` | runs Phase 2 (`cddf.phase2.estimate`) on each query and writes `predictions_85.csv` |
| `predictions_85.csv` | one row per incident (see below) |
| `score.py` | derives the labels from a EuRepoC CSV and computes the per-type F1, Macro-F1 and the bootstrap interval |

Columns of `predictions_85.csv`: `eurepoc_id`; `linked_report_ids` (`;`-separated); `n_techniques`;
`neighbour_1` … `neighbour_7` (EuRepoC ids of the precedents, most similar first); `count_<type>` (number of the seven
neighbours carrying the type); `score_<type>` (the score that is compared with θ: count / 7, or the majority share for
an empty query, see below); `empty_query_majority_substituted`; `candidate_objectives` (types with score ≥ 0.15);
`same_actor_precedents_removed` (0 for every incident). The three types are exfiltration, manipulation and
disclosure, and disruption and destruction.

## Condition

- **Unmasked**: the query is the full technique set of the incident, the union of the techniques extracted from its
  graded linked reports (no removal of effect-stage techniques).
- Settings as in the case runs: K = 7, weights technique 0.9, sector 0.1, assets 0; θ = 0.15 (training
  cross-validation threshold of the weighted k-nearest-neighbour engine in the unmasked condition, rule 1).
- Precedent pool: the 642 training incidents, unchanged for every query. No precedent date filter is applied in the
  evaluation. The same-actor rule is applied but removes nothing, because the evaluation incidents were split from
  the training incidents by actor (85 incidents, 39 actors, none shared with the pool; no linked report shared with
  the pool).
- Sector: the first recorded victim sector, mapped from EuRepoC as for the training incidents.
- Empty queries: two incidents have an empty technique set. As in the original evaluation, their scores are replaced
  by the majority baseline (the share of each type among the training incidents), and the neighbour columns show
  the neighbours the engine returned before the replacement.
- The 85 incidents are those of the evaluation set with linked reports and at least one objective label; incidents
  whose EuRepoC record gives no label were excluded before grading.

## Gold labels and scoring

Gold labels: `cddf.labels.labels_of` (`src/cddf/labels.py`) applied to the EuRepoC fields `incident_type` and
`mitre_impact`; dormancy is not one of the three graded types. The same function gives the labels of the 642
training incidents in `data/incidents.csv`.

Scoring: for each type, a prediction is positive when the score is at least θ. Precision, recall and F1 are computed
over the 85 incidents (a ratio with a zero denominator is 0). An incident with an empty candidate set is graded with
three negative predictions; it is not dropped. Macro-F1 is the mean of the three per-type F1 values. The majority
baseline predicts the training shares for every incident and is scored at its own training cross-validation
threshold θ = 0.05 (threshold grid without 0.0). The interval is a paired bootstrap of the difference Phase 2 minus
majority over incidents: 10,000 resamples, seed 20260820, incidents in file order.

Reported in the article: Macro-F1 0.619 on n = 85 incidents (39 actors); majority baseline 0.480. In the original
evaluation output these are 0.61932 (Phase 2, θ 0.15, 85 graded incidents) and 0.479504 (majority, θ 0.05); the
difference is 0.139816 with a 95 % bootstrap interval of [0.045963, 0.225986] (resampling incidents).

## Note on this release

`predict.py` reproduces the predictions of the original evaluation code exactly (scores, neighbours and candidate
sets of all 85 incidents were checked against the original engine). `score.py` has not been run for this release;
the figures above are those reported in the article and were not recomputed here.
