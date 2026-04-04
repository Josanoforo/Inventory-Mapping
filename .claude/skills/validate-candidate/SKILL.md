Validate Candidate — Skill
Read `modules/06_validator.md` before executing.
Steps
1. Load references
Read `reference/protocol_canonical.md` (the 8 canonical checks).
Read `schemas/tension_candidate.schema.json`.
2. For each TC in `output/tension_candidates/`
Run all 16 checks from the module:
Signal IDs verified: every ID has description in parentheses.
Candidate Generation Rules: not pure frequency — at least one rule from canon applies.
Corpus-term polos: definitions reference corpus, not absolute ranges.
Units declared: mixed units flagged, not hidden.
Supports distinction: "yes" and "no" sections distinguish evidence from inference.
Rejected Groupings exist: `output/rejected_groupings.md` is non-empty.
Coverage Gaps reported: `output/coverage_gaps.md` is non-empty.
Mechanical language: no valorative adjectives. Match forbidden words at word boundaries only. "solución" matches as standalone word, NOT inside "resolución." Whitelist: "resolución", "valor central."
Type matches relation: the TC type corresponds to the actual pattern (not misclassified).
Signal IDs verified against source: spot-check 3 random IDs per TC against `input/` files.
Human fields empty: all human fields are empty strings.
Schema valid: TC parses and validates against tension_candidate.schema.json.
mechanical_summary ≠ definition: no pole has identical text in both fields. If identical → flag "mechanical_summary_equals_definition."
unit_used specific: no pole says "mixed" without listing specific units. If evasive → flag "unit_used_evasive."
what_it_supports not template: what_it_supports.yes is NOT "Coexistencia de los patrones documentados en las cards referenciadas." If it is → flag "what_it_supports_is_template."
card-polo relevance spot check: for TCs with >15 Signal IDs, spot-check 2 random cards per pole — does each card relate to the pole's definition? If not → flag "card_polo_mismatch" with specific card ID.
3. Write per-candidate report
For each TC, write `working/validation/candidate_reports/TC-NNN_validation.json`:
```json
{
  "candidate_id": "TC-002",
  "passed": true,
  "checks": [
    {"check": "signal_ids_verified", "passed": true, "detail": ""},
    {"check": "candidate_generation_rules", "passed": true, "detail": ""},
    {"check": "mechanical_summary_not_definition", "passed": false, "detail": "Polo A has identical definition and mechanical_summary"},
    ...
  ],
  "timestamp": "..."
}
```
Validate against `schemas/validation_report.schema.json`.
4. Write summary
Write `working/validation/validation_summary.json`:
```json
{
  "total_candidates": N,
  "passed": N,
  "failed": N,
  "checks_most_failed": [],
  "candidates_needing_attention": []
}
```
5. Update review queue
Update `output/review_queue.md` with validation results for each TC.
Important
Do not fix candidates. Do not discard candidates. Only report.
