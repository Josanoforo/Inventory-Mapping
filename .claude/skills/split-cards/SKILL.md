# Split Cards — Skill

Read `modules/02_splitter.md` before executing.

## Steps

1. Read `working/split/split_manifest.json` if it exists (for resumption). If not, initialize it.
2. For each round file in `input/signal_cards_round_*.md`:
   a. If round already `complete` in manifest, skip.
   b. Split file content by card delimiter: `---` blocks containing `**SC-R`.
   c. Group cards into batches of ~25 cards each.
   d. Write each batch to `working/split/card_batches/batch_R{round}_{batch_num}.md`.
   e. Preserve card text exactly. No modification.
   f. Update manifest: cards_found, batches_written, status for this round.
3. After all rounds: compute totals, set status to `complete`.
4. Validate manifest against `schemas/split_manifest.schema.json`.

## Batch naming

`batch_R01_001.md`, `batch_R01_002.md`, ..., `batch_R10_007.md`

## Verification

After splitting, confirm: sum of cards_found across all rounds = 1,560 (or actual input count from entry gate report).
