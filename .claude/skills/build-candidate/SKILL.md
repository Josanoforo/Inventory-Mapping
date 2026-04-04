# Build Candidate — Skill

Read `modules/05_candidate_builder.md` before executing.

## Steps

### 1. Collect routed patterns

Read all `working/scans/*.json`. Collect patterns by routing:
- `tension_candidate` → build as TC
- `needs_audit` → build as TC with status `needs_audit_before_classification`
- `rejected_grouping` → append to rejected_groupings.md
- `coverage_gap` → append to coverage_gaps.md
- `isolated_signal` → append to isolated_signals.md

### 2. Deduplicate

Before building TCs, check for overlap:
- If two patterns from different scans share >70% of their signal_ids, merge into one TC.
- Note both source patterns in the merged TC.

### 3. Build each TC

For each tension_candidate or needs_audit pattern:

a. Go to `input/signal_cards_round_*.md` and verify every Signal ID. Read the actual card.
b. If a Signal ID does not exist in the source file, exclude it. Note in classification_risk.
c. If after verification fewer than 2 Signal IDs remain, demote to rejected_grouping.
d. Construct the TC markdown file matching the format of `reference/TC-001.md`:
   - ID: TC-NNN (starting at TC-002)
   - Status, Type, Mechanical relation, Analytical unit
   - Signal IDs list
   - Structured support with Poles (definition in corpus terms, signal_ids with descriptions, mechanical summary, unit used, notes)
   - Additional context if applicable
   - What it supports (yes/no)
   - What is missing
   - Classification risk
   - Human fields (all empty)
e. Validate the constructed TC against `schemas/tension_candidate.schema.json`.
f. Write to `output/tension_candidates/TC-NNN.md`.

### 4. Build secondary outputs

- `output/rejected_groupings.md`: all rejected grouping patterns.
- `output/coverage_gaps.md`: all coverage gap patterns.
- `output/isolated_signals.md`: all isolated signals.

### 5. Build review queue

Write `output/review_queue.md` listing every TC with:
- ID, type, status, number of signal IDs, validation status (pending until validator runs).

## Format reference

Use `reference/TC-001.md` as the exact format template. Match its structure section by section.
