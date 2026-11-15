# Technique extractor: evaluation on the AnnoCTR test set

This folder lets a reader check the extractor figure reported in the article
(precision 0.731, recall 0.581, F1 0.648, 95% interval 0.589–0.693). The
extractor itself is not part of this release; the technique sets of the
dataset and of the two incidents are provided as data.

## Files

- `predictions_annoctr_test.csv` — for each of the 34 test reports of AnnoCTR
  (the `linking_mitre_only` test split), the ATT&CK techniques predicted by the
  final extractor configuration, folded to the parent technique
  (264 predictions in total). Report names are AnnoCTR document identifiers.
  No AnnoCTR text or annotation is included.
- `summary.json` — threshold, precision, recall, F1, the 95% bootstrap interval,
  the counts of true positives (193), false positives (71) and false negatives
  (139), and the number of gold (report, technique) pairs (332).

## How to rescore

1. Download AnnoCTR (Lange et al., LREC-COLING 2024;
   https://github.com/boschresearch/anno-ctr-lrec-coling-2024, CC BY-SA 4.0).
2. Gold set of a report: every annotation in `linking_mitre_only/test.jsonl`
   with `entity_type == "TECHNIQUE"` whose `label_link` points to an ATT&CK
   technique page; take the technique ID (and sub-technique if present),
   map revoked IDs to their current ID through the `revoked-by` relationships
   of the ATT&CK Enterprise, ICS and Mobile bundles, and fold sub-techniques
   to the parent (`T1059.003` → `T1059`). Every document that appears in the
   file is in the population (34 documents; one has an empty gold set).
3. Score micro-averaged over (report, technique) pairs: TP = predicted and in
   gold, FP = predicted and not in gold, FN = in gold and not predicted;
   precision = TP/(TP+FP), recall = TP/(TP+FN), F1 = harmonic mean.
4. The interval resamples the 34 reports with replacement
   (1,000 resamples drawn with `numpy.random.default_rng(20260826)`),
   recomputes micro F1 on each resample and takes the 2.5th and 97.5th
   percentiles.

The extractor configuration: sentence-level candidates from rules and a
sentence model, scored with a fine-tuned ATT&CK-BERT encoder (Abdeen et al.,
2023), and a logistic regression over five features
(`cos_desc`, `cos_proc`, `tech_freq_log`, `term_idf`, `is_lit`) with
acceptance threshold 0.26.
