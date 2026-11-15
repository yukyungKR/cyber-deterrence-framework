# Coding records of the evidence records

For each incident, the fields of the evidence (input) record other than the technique set were coded from a fixed bundle of public documents. Two coders coded the same bundle independently, the two records were compared field by field, and the author confirmed the final value of every field. This folder holds the final material of that procedure, five items per incident.

| Item | What it is |
|---|---|
| 1 Instructions | The coding instructions as given to the coders, the excerpt of the input form (section A, key definitions and allowed values) that came with them, the empty record template, and the list of bundle files with their hashes |
| 2 Coder records | Each coder's record (JSON) and evidence notes (Markdown). Each coded value cites a passage of a bundle document as `file:line` (keys pre-filled by the template excepted) |
| 3 Comparison sheet | Field-by-field comparison of the two records, with the author's choice in the last column (「저자 확정」) |
| 4 Author confirmation | The author's decision for each field in machine-readable form |
| 5 Confirmed record | The confirmed evidence record. Its `techniques` list is empty because the technique set is not coded by hand. It comes from the technique extractor |

The coders were two language models, Claude Opus (coder A) and Claude Fable (coder B). Each worked alone in an isolated directory that held only copies of the bundle, the instructions, the form excerpt and the template. Neither could see the other's output. The model versions are recorded in the comparison sheets: `claude-opus-5-5` and `claude-fable-5-1` for Viasat, and `claude-opus-5-5` and `claude-fable-5-2` for Binance. Where the two records differ, the author chose the value. Where they agree, the agreed value was kept with the author's confirmation.

All files are in Korean, as they were written. Quotations from the source documents are in their original language, mostly English. File names inside the documents are the working names used during coding, for example `coding_r2_claude_opus.json` for `coder_a_claude_opus.json`. The bundle documents themselves are not included. They are listed, with URLs and hashes, in `cases/<case>/documents.csv`.

## Edits made for publication

Local file paths, internal decision and record numbers, references to working files that are not published, and role labels of the working process were removed or replaced with neutral wording (for example `<local path>` or 「저자 결정」, "author decision"). Values of incidents outside the article that appeared as examples in the instructions and the form were replaced with `<example>`. Coded values, quotations from the documents, instructions, and the author's decisions were not changed. Because of these edits, hashes quoted inside the files describe the files as they were produced, not these copies.

## Viasat KA-SAT (2022)

Final coding round (round 2) on a bundle of 23 documents.

| Item | File |
|---|---|
| 1 Instructions | `viasat/01_instructions/coding_instructions.md`, `input_form_section_A_excerpt.md`, `record_template.jsonl`, `document_bundle_manifest.json` |
| 2 Coder A (Claude Opus) | `viasat/02_coder_a/coder_a_claude_opus.json`, `coder_a_claude_opus_evidence.md` |
| 2 Coder B (Claude Fable) | `viasat/02_coder_b/coder_b_claude_fable.json`, `coder_b_claude_fable_evidence.md` |
| 3 Comparison sheet | `viasat/03_comparison/comparison_sheet.md` |
| 4 Author confirmation | `viasat/04_author_confirmation/author_confirmation.json` |
| 5 Confirmed record | `viasat/05_confirmed_record/confirmed_record.jsonl` |

The comparison sheet also compares each coder with the confirmed record of the earlier round (column 「회차 1 확정값」). That earlier round is not published.

## Binance theft (2026)

Bundle of 25 documents: 22 technical documents (`tech_*`) and 3 government documents (`resp_*`) added as sources for the attribution fields.

| Item | File |
|---|---|
| 1 Instructions | `binance/01_instructions/coding_instructions.md`, `input_form_section_A_excerpt.md`, `record_template.jsonl`, `document_bundle_manifest.json` |
| 2 Coder A (Claude Opus) | `binance/02_coder_a/coder_a_claude_opus.json`, `coder_a_claude_opus_evidence.md` |
| 2 Coder B (Claude Fable) | `binance/02_coder_b/coder_b_claude_fable.json`, `coder_b_claude_fable_evidence.md` |
| 3 Comparison sheet | `binance/03_comparison/comparison_sheet.md` |
| 4 Author confirmation | `binance/04_author_confirmation/author_confirmation.json` |
| 5 Confirmed record | `binance/05_confirmed_record/confirmed_record.jsonl` |

## Document lists and hashes

In `cases/<case>/documents.csv`, `sha256` is the hash of the document text as given to the coders. For Viasat, the technique extractor read the same texts. For Binance, the coders received copies in which a few lines of collection notes were masked. The extractor received copies from which the collection header lines had been removed, so its input hashes differ from the listed ones.
