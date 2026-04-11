# Module 02 — Splitter

## Purpose

Split raw round files into discrete card batches suitable for incremental indexing.

## Input

- `input/signal_cards_round_*.md` (10 files)

## Output

- `working/split/card_batches/` — batch files, each containing a set of discrete cards
- `working/split/split_manifest.json` — validates against `schemas/split_manifest.schema.json`

## Rules

- Split each round file by card delimiter (`---` blocks containing `**SC-R*`).
- Each batch file contains a manageable number of cards (target: 20-30 cards per batch).
- Batch files are named `batch_RNN_BBB.md` where NN is round number, BBB is batch number.
- Preserve full card text exactly as-is. No modification, no field extraction yet.
- Update split_manifest.json after each round is processed.

## Fail states

- Card count after split does not match expected count for that round → stop, report discrepancy.
- Card delimiter not found → malformed input, stop.
- Schema validation of manifest fails → stop.

## Resumability

If interrupted, read split_manifest.json. Resume from first round with status `pending`.
