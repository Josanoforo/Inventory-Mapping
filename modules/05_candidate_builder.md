Module 05 — Candidate Builder
Purpose
Transform scan patterns routed as `tension_candidate` or `needs_audit` into fully formed Tension Candidate files. Also produce rejected_groupings.md, coverage_gaps.md, and isolated_signals.md from their respective routings.
Input
`working/scans/*.json` (all 7 scan artifacts)
`input/signal_cards_round_*.md` (for Signal ID verification)
`reference/TC-001.md` (format reference)
`reference/protocol_canonical.md` (rules)
Output
`output/tension_candidates/TC-NNN.md` — one file per candidate
`output/rejected_groupings.md`
`output/coverage_gaps.md`
`output/isolated_signals.md`
`output/review_queue.md` — index of all TCs with status
Pre-build filter
Before building a TC from any pattern, apply these filters:
If the pattern comes from `lexical_overlap` scan and has <3 Signal IDs → route to `rejected_groupings.md`. Do not build TC.
If the pattern comes from `lexical_overlap` scan and has 3+ Signal IDs but no explicit friction → route to `rejected_groupings.md`. Do not build TC.
If the pattern comes from another scan and has <3 Signal IDs → build as TC but add "minimal support — only 2 cards" to classification_risk.
Rules
For each pattern routed as tension_candidate:
Go back to the original signal cards in `input/`. Do not rely solely on the index.
Verify every Signal ID against the source file. If the card does not exist, do not include it.
Build the TC in the format of `reference/TC-001.md`.
Validate against `schemas/tension_candidate.schema.json`.
Write to `output/tension_candidates/TC-NNN.md` as markdown matching TC-001 format.
TC numbering starts at TC-002 (TC-001 already exists).
For each pattern routed as needs_audit:
Apply pre-build filter first.
If it passes, build as TC with status `needs_audit_before_classification`.
Include in review_queue.md with audit flag.
For patterns routed as rejected_grouping:
Append to `output/rejected_groupings.md` with: grouping_label, signal_ids, reason_for_rejection, why_it_does_not_generate_a_DT_question.
For patterns routed as coverage_gap:
Append to `output/coverage_gaps.md` with: gap_name, signal_ids_if_any, description, why_it_limits_reading_of_the_inventory.
For patterns routed as isolated_signal:
Append to `output/isolated_signals.md` with: signal_id, why_preserved.
Candidate Construction Rules
Type: Must match the actual mechanical relation. Contradiction ≠ asymmetry.
Polos: Defined in corpus terms, not absolute ranges.
Units: Declared with specific unit names. "mixed" alone is not acceptable.
What it supports: Distinguish what cards show from what someone might infer. Must be specific to THIS candidate.
What is missing: What would clarify, dissolve, or normalize THIS candidate specifically.
Classification risk: Select all that apply from the canon's list.
Human fields: All empty. Never fill them.
Deduplication
If two scan artifacts produce patterns that reference >70% of the same Signal IDs, merge ONLY IF the patterns share the same mechanism:
Verify both patterns describe the same blocker/blocked relationship, the same distributional axis, or the same contradiction.
If the patterns come from different scan types (e.g., COO + FRI), verify they describe the same phenomenon from different angles — not different phenomena that happen to share cards.
If merging would produce poles without coherent definitions, do NOT merge. Keep as separate TCs.
If merged, list all source_patterns.
Fail states
Signal ID not found in source file → exclude from candidate, note in classification_risk.
Pattern has <2 verified Signal IDs after verification → demote to rejected_grouping.
TC fails schema validation → do not output, log error.
