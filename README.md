# Cyber Deterrence Decision-Making Framework

This repository contains the code and data of the Cyber Deterrence Decision-Making Framework described in
Kim Y. *A cyber deterrence decision-making framework: from threat intelligence to deterrence strategy assessment.*
Journal of Cybersecurity (under review). The framework links the technical observation of a cyber incident, expressed
as MITRE ATT&CK techniques, with similar past incidents and with the requirements of international law. From an
evidence record of a new incident it estimates candidate objectives from the most similar precedents (Phase 2),
reviews 19 response measures as at the time of identification and derives the matching D3FEND defensive techniques
(Phase 3), retrieves the public responses of states to the precedents (Phase 4), and restates the review as a
judgement for each deterrence type (deterrence strategy assessment). The repository reproduces the results of the
article for the Viasat KA-SAT incident (2022) and the Binance theft (2026).

Archived version: Zenodo, release v1.0.0, DOI [10.5281/zenodo.24247702](https://doi.org/10.5281/zenodo.24247702).

## Scope of version 1.0

The code starts from evidence records whose technique sets have already been extracted. The technique extractor of
Phase 1 (a fine-tuned ATT&CK-BERT encoder with a logistic-regression decision step) is not part of this release; the
technique sets of the dataset and of the two incidents are provided as data, and the evaluation of the extractor is
provided as predictions (`evaluation/extractor/`). The other fields of the evidence records were coded under fixed
coding instructions by two coders working independently, and the author confirmed every value (see Coding records).

## Repository layout

```
data/                       derived data (see Data)
  incidents.csv             the processed incident dataset, one row per incident (806)
  precedent_eligibility.csv dates that decide whether a training incident is an eligible precedent
  eurepoc_responses.csv     EuRepoC political and legal response records of the training incidents
  measures.csv              the 19 response measures (Table 1 of the article)
  sectors.csv               the 18-sector scheme, its five groups and the 11 essential-interest sectors
  state_positions.csv       published positions of six states on sovereignty
  d3fend/                   ATT&CK -> artefact -> D3FEND defensive technique relations (D3FEND 1.6.0)
  THIRD_PARTY_NOTICES.md
src/cddf/                   the Python package
  record.py                 evidence record: loading and validation
  phase2.py                 objective estimation from similar precedents
  phase3.py                 review of the 19 response measures
  d3fend.py                 derivation of defensive techniques
  phase4.py                 precedent responses
  assessment.py             deterrence strategy assessment
  run.py                    command-line interface
  summary.py                summary.md writer
  labels.py                 objective labels of a EuRepoC incident (label rule)
cases/viasat/               evidence_record.json, documents.csv, results/
cases/binance/              evidence_record.json, evidence_record_22docs.json, documents.csv, results/, results_22docs/
tests/verify.py             verification against the reference values in tests/reference/
coding/                     coding instructions, the two coders' records, comparison and author confirmation
evaluation/phase2/          Phase 2 predictions for the 85 graded evaluation incidents, scorer
evaluation/extractor/       technique extractor: predictions on the AnnoCTR test set and summary
```

## Requirements and use

Python 3.10 or later. The package uses only the standard library.

```
pip install -e .            # or set PYTHONPATH=src
python -m cddf.run --record cases/viasat/evidence_record.json --out cases/viasat/results
python -m cddf.run --record cases/binance/evidence_record.json --out cases/binance/results --include-same-actor --defender-state US
python -m cddf.run --record cases/binance/evidence_record_22docs.json --out cases/binance/results_22docs --include-same-actor --defender-state US
python tests/verify.py
```

Options:

- `--include-same-actor` keeps precedents whose actor string equals the actor of the record. By default they are
  removed from the pool. The Binance runs use the option; the record's actor (TraderTraitor) matches no precedent,
  so the option does not change the Binance results.
- `--defender-state` (US, UK, FR, DE, NL, KR) adds the published position of that state to the review of
  forward cyber defence operations and, for an ongoing intrusion without effect, of countermeasures. It does not
  change the review statuses or the judgements. The Binance runs are from the perspective of the United States.

Each run writes `result.json` (all values) and `summary.md`. `tests/verify.py` runs the three records and compares
the neighbours and their similarities (rounded to 4 decimal places), the label frequencies and candidate objective set,
the precedent-pool sizes, the status, required grade and attribution check of the 19 measures, the countermeasures
purpose, the set and number of D3FEND defensive techniques, the precedent response records and proportions, and the
six judgements with reference values extracted from the outputs of the original implementation.

## Method as implemented

The article (Section 3) is the specification. The points below state how the code applies it, including details the
article does not spell out.

**Phase 2.** The pool is the 642 training incidents of `incidents.csv`, less every incident linked to a report listed
in the record's `excluded_report_ids` (the incident's own source documents), less incidents that are not eligible on
the record's `identified_date` (rule in `phase2.is_eligible`; data in `precedent_eligibility.csv`), and, unless
`--include-same-actor` is given, less incidents whose actor string equals the record's `actor`. Similarity is
0.9 × Jaccard similarity of the technique sets + 0.1 × sector match, where the sector match compares the first
recorded sector of the five-group level of the sector scheme (government and defence, critical infrastructure, finance
and commerce, information and communications, private and other) and a missing sector contributes 0. Victim assets
carry weight 0. The seven most similar incidents are the neighbours; ties are broken by the EuRepoC identifier in
string order. A type enters the candidate objective set when its share among the seven neighbours is at least 0.15,
that is, when two or more neighbours carry it. Two rule-based values are checked first: if the target is a specific
victim and neither an intrusion nor an effect is established, no objective can be examined and the estimate is
reported for reference only; the dormancy rule (intrusion ongoing, a persistence technique among T1053, T1078,
T1133, T1542 and T1543 observed, and none of a fixed list of collection, exfiltration and impact techniques) is
reported but held at the time of identification, because before any effect is observed its no-effect condition is met
by construction.

**Phase 3.** An armed-conflict nexus coded `established` sets the incident aside for examination under international
humanitarian law; no peacetime review or assessment is produced. Otherwise: countermeasures are open for review when
any effect is observed; when no effect is observed they depend on the state's position (intrusion ongoing), are open
for the purpose of reparation only (intrusion terminated), or are excluded (intrusion not established or
indeterminate). The purpose recorded is cessation for an ongoing intrusion and reparation for a terminated one.
Self-defence is open for review of an armed attack when disruption and destruction is observed, open for review of
imminence when it is not observed but is a candidate objective, and otherwise has no basis for review. The plea of
necessity is open for review when any recorded sub-sector is one of the 11 essential-interest sectors and excluded
otherwise. Forward cyber defence operations depend on the state's position; the six positions are in
`state_positions.csv`. The other measures receive the treatment of Table 1. The attribution requirement of a measure
is met when the state-attribution grade is at least the grade its legal character requires (retorsion 2,
countermeasures 3, self-defence 4). Defensive techniques are derived through the D3FEND tables (`d3fend.py`).

**Phase 4.** For each neighbour the EuRepoC response columns are shown. A neighbour has a political (legal) response
when the EuRepoC count column `number_political_responses` (`number_legal_responses`) is greater than 0; a
neighbour with neither is marked 'no record found'. The proportions are counted over the seven neighbours.

**Deterrence strategy assessment.** As in the article (Section 3.4); see `assessment.py`.

## Data

| File | Rows | Content | Source |
|---|--:|---|---|
| `incidents.csv` | 806 | EuRepoC incident id; split (`train` 642, `evaluation` 158, `set_aside` 6); EuRepoC incident name; actor; linked ORKL report ids (1,783 reports in all); technique set (union over the linked reports); sector (five groups) and sub-sector (18 sectors) of the first recorded victim; victim assets (union over the linked reports, D3FEND class or ATT&CK for ICS asset ids); objective labels (exfiltration, manipulation and disclosure, disruption and destruction, dormancy) and `label_absent` (EuRepoC records no effect), given for the 642 training incidents only and left empty for the 164 evaluation and set-aside incidents; start date | EuRepoC Global Dataset v1.3; ORKL report ids; ATT&CK ids; D3FEND ids |
| `precedent_eligibility.csv` | 642 | for each training incident: number of linked reports, dated and undated, earliest publication date found for a linked report, EuRepoC start date | publication dates found in the reports and their reference URLs; EuRepoC |
| `eurepoc_responses.csv` | 642 | initiator, receiver countries, the two response counts and the ten political and legal response columns, as recorded | EuRepoC Global Dataset v1.3 |
| `measures.csv` | 19 | measure, deterrence type, punishment sub-item, legal character, treatment, required attribution grade | Table 1 of the article |
| `sectors.csv` | 18 | sub-sector, its group, essential interest (11) | sector scheme based on the CISA critical infrastructure sectors |
| `state_positions.csv` | 6 | sovereignty position (`principle`, `purist`: unauthorised access is a violation, `effects`: effects threshold, `silent`: not stated); due diligence | published national positions cited in the article |
| `d3fend/*.csv` | | `attack_ids`: ATT&CK ids known to D3FEND; `attack_artifacts`: technique, relation, artefact; `artifact_defences`: artefact, the (super)class carrying the defence, relation, defensive technique, D3FEND id, tactics | MITRE D3FEND 1.6.0 |

The incident dataset was built by joining EuRepoC incidents and ORKL reports at incident level. Objective labels are
assigned by rule (`src/cddf/labels.py`) from the EuRepoC fields `incident_type` and `mitre_impact`: Data theft, Data Exfiltration and
Resource Hijacking give exfiltration; Data theft & Doxing gives exfiltration and manipulation and disclosure;
Defacement and Data Manipulation give manipulation and disclosure; Disruption, Ransomware and the ATT&CK Impact
values of denial of service, encryption, destruction, wiping, service stop, shutdown, account access removal and
firmware corruption give disruption and destruction; Hijacking without Misuse gives dormancy; Hijacking with Misuse
gives no label. Sectors are mapped from EuRepoC `receiver_category` and `receiver_subcategory`. Actor strings are
those of the incident-to-report join; `(unknown or unattributed)` marks incidents without a named actor. The files
contain no text of the CTI reports. The labels of the evaluation and set-aside incidents are not published; they can
be derived from EuRepoC with `cddf.labels` (see `evaluation/phase2/`).

Licences of the sources: EuRepoC is CC BY-NC 4.0; see `data/THIRD_PARTY_NOTICES.md` for EuRepoC, ORKL, MITRE
ATT&CK and MITRE D3FEND.

## Evidence records

`cases/<case>/evidence_record.json` is the confirmed evidence record of each incident
(`coding/<case>/05_confirmed_record/confirmed_record.jsonl`) with three changes: the technique set is the set
extracted by the technique extractor from the incident's documents, and two keys are added, `excluded_report_ids`
and `name_en` (an English name used in the results). `tests/verify.py` checks that all other keys and values equal
the confirmed record. The fields read by the code:

| Key | Meaning (article term) | Values |
|---|---|---|
| `identified_date` | reference date of the technical state | YYYY-MM-DD |
| `techniques` | technique set | ATT&CK ids |
| `victim_sector`, `victim_sector_sub` | victim sector (group, 18-sector scheme); the first value is the main target | `sectors.csv` |
| `victim_assets` | victim assets | D3FEND or ATT&CK for ICS asset names |
| `intrusion_state.value` | intrusion state | `none` (not established), `persisting` (ongoing), `terminated`, `indeterminate` |
| `access_depth.draft` | intrusion depth | `external`, `office` (enterprise IT), `core` (mission-critical), `ot`, `indeterminate` |
| `effect_realized.by_type` | effects: `1` exfiltration, `2` manipulation and disclosure, `3` disruption and destruction | `post` (observed), `pre` (not observed), `indeterminate` |
| `conflict_nexus` | armed-conflict nexus | `established`, `ambiguous`, `none` |
| `c_id.grade`, `c_st.grade` | actor-identification and state-attribution confidence | 1 to 5 |
| `actor` | actor, for the same-actor exclusion | string |
| `target_specificity` | specific victim or capability captured before deployment | `specific_victim`, `capability_only` |
| `excluded_report_ids` | ORKL reports among the incident's own source documents | ORKL ids |

The reasoning fields (`basis`, `note` and similar) and some descriptive values are the coders' record and are in
Korean, with quotations from the source documents. The source documents are listed in `cases/<case>/documents.csv` (title, publisher, URL, publication and access
dates, SHA-256 of the text, role); the documents themselves are not included.
`evidence_record_22docs.json` differs from the Binance record only in its technique set (29 techniques extracted
from 22 documents instead of 23 from 20).

## Coding records

`coding/<case>/` holds, for each incident, the five final items of the coding procedure: the instructions as given to
the coders, the two coders' records with the cited source passages, the field-by-field comparison sheet, the author's
confirmation and the confirmed record. The two coders were the language models Claude Opus and Claude Fable
(Anthropic), each working on its own copy of the same document bundle; where they differed the author chose the
value. The files are in Korean. Details and the edits made for publication are in `coding/README.md`.

## Evaluation

Phase 2: `evaluation/phase2/` holds the 85 queries, the per-incident predictions (unmasked condition, θ 0.15, K 7,
weights 0.9/0.1/0), the prediction script and a scorer that derives the gold labels from EuRepoC; see its README.
Reported: Macro-F1 0.619 on 85 incidents (39 actors), majority baseline 0.480.

Technique extractor: `evaluation/extractor/` holds the techniques predicted for the 34 test reports of AnnoCTR and the
summary (precision 0.731, recall 0.581, F1 0.648, 95% interval 0.589–0.693), with instructions for rescoring
against AnnoCTR; see its README.

## Licences

Code: MIT (`LICENSE`). Data and case records: CC BY-NC 4.0 (`LICENSE-DATA.md`), in line with the EuRepoC licence.
Third-party notices: `data/THIRD_PARTY_NOTICES.md`.

## Citation

Kim Y. A cyber deterrence decision-making framework: from threat intelligence to deterrence strategy assessment.
Journal of Cybersecurity (under review).

Code and data: Kim Y. cyber-deterrence-framework, release v1.0.0. Zenodo, 2026. https://doi.org/10.5281/zenodo.24247702
