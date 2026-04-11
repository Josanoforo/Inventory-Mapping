# Module 03 — Indexer

## Purpose

Transform discrete card batches into a structured JSONL index for mechanical scanning.

## Input

- `working/split/card_batches/batch_*.md`
- `working/split/split_manifest.json` (to know what to process)

## Output

- `working/index/card_index.jsonl` — one JSON line per card, validates against `schemas/card_record.schema.json`
- `working/index/index_manifest.json` — validates against `schemas/index_manifest.schema.json`

## Rules

- Process batches incrementally. Read one batch, extract fields, append to JSONL, update manifest.
- For each card, extract: id, round, observation, source, date, source_type, domain, actor, evidence_base, extraction_status.
- Parse `actor` from the "Actor:" field in the markdown block.
- Additionally extract: entities (platform names, seller names, product types mentioned) and figures (quantitative data present).
- Entities and figures are best-effort extraction to aid scanning. They do not need to be exhaustive.
- Validate each record against `schemas/card_record.schema.json` before appending.
- If a record fails validation, log it in manifest issues but continue processing.

## Fail states

- Batch file unreadable → log error, skip batch, continue.
- Card missing required field (id, observation, domain) → log in issues as error severity, skip card.
- Schema validation fails on a record → log in issues as warning, skip record.
- Final cards_indexed count does not match cards_total → manifest status = `failed`.

## Resumability

Read index_manifest.json. Resume from `last_batch_processed`. Do not reprocess already-indexed batches.

## Completion

When all batches are processed and cards_indexed matches cards_total (minus skipped), set status to `complete`.
