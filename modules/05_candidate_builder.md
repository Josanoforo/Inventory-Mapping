# Module 05 — Candidate Builder

## Purpose

Transform scan patterns routed as `tension_candidate` or `needs_audit` into fully formed Tension Candidate files. Also produce rejected_groupings.md, coverage_gaps.md, and isolated_signals.md from their respective routings.

## Input

- `working/scans/*.json` (all 7 scan artifacts)
- `input/signal_cards_round_*.md` (for Signal ID verification)
- `reference/TC-001.md` (format reference)
- `reference/protocol_canonical.md` (rules)

## Output

- `output/tension_candidates/TC-NNN.md` — one file per candidate
- `output/rejected_groupings.md`
- `output/coverage_gaps.md`
- `output/isolated_signals.md`
- `output/review_queue.md` — index of all TCs with status

## Rules

### For each pattern routed as tension_candidate:

1. Go back to the original signal cards in `input/`. Do not rely solely on the index.
2. Verify every Signal ID against the source file. If the card does not exist, do not include it.
3. Build the TC in the format of `reference/TC-001.md`.
4. Validate against `schemas/tension_candidate.schema.json`.
5. Write to `output/tension_candidates/TC-NNN.md` as markdown matching TC-001 format.
6. TC numbering starts at TC-002 (TC-001 already exists).

### For each pattern routed as needs_audit:

- Build as TC with status `needs_audit_before_classification`.
- Include in review_queue.md with audit flag.

### For patterns routed as rejected_grouping:

- Append to `output/rejected_groupings.md` with: grouping_label, signal_ids, reason_for_rejection, why_it_does_not_generate_a_DT_question.

### For patterns routed as coverage_gap:

- Append to `output/coverage_gaps.md` with: gap_name, signal_ids_if_any, description, why_it_limits_reading_of_the_inventory.

### For patterns routed as isolated_signal:

- Append to `output/isolated_signals.md` with: signal_id, why_preserved.

## Candidate Construction Rules

- **Type**: Must match the actual mechanical relation. Contradiction ≠ asymmetry.
- **Polos**: Defined in corpus terms, not absolute ranges.
- **Units**: Declared. Mixed units flagged.
- **What it supports**: Distinguish what cards show from what someone might infer.
- **What is missing**: What would clarify, dissolve, or normalize.
- **Classification risk**: Select all that apply from the canon's list.
- **Human fields**: All empty. Never fill them.

## Deduplication

If two scan artifacts produce patterns that reference largely the same cards (>70% overlap), merge into one TC and note both source patterns. Do not produce near-duplicate candidates.

## Fail states

- Signal ID not found in source file → exclude from candidate, note in classification_risk.
- Pattern has <2 verified Signal IDs after verification → demote to rejected_grouping.
- TC fails schema validation → do not output, log error.
