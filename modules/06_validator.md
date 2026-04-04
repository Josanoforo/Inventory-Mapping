Module 06 — Validator
Purpose
Run checks from the canonical protocol against every produced TC. Flag failures without discarding.
Input
`output/tension_candidates/TC-*.md`
`reference/protocol_canonical.md` (the 8 checks)
Output
`working/validation/candidate_reports/TC-NNN_validation.json` — per candidate, validates against `schemas/validation_report.schema.json`
`working/validation/validation_summary.json` — aggregate results
Checks (from canon)
Does every candidate have verified Signal IDs with descriptions in parentheses?
Does every candidate pass Candidate Generation Rules (not pure frequency)?
Are polos defined in corpus terms, not absolute ranges?
Are mixed units declared, not hidden?
Does "What this candidate actually supports" distinguish what the cards show from what someone might infer?
Is there at least one Rejected Grouping in the output?
Are Coverage Gaps reported in the output?
Is all language mechanical (no valorative adjectives)? Use word-boundary matching, not substring. "solución" as a standalone word is forbidden; "resolución" containing "solución" as substring is NOT a match. Whitelist for known false positives: "resolución", "valor central."
Additional checks
Does the TC type match the actual mechanical relation?
Are all Signal IDs verified against source files?
Are human fields empty?
Does the TC validate against `schemas/tension_candidate.schema.json`?
Builder quality checks (new)
mechanical_summary ≠ definition: verify that no pole has identical text in definition and mechanical_summary fields. If identical, flag as "mechanical_summary_equals_definition."
unit_used specific: verify no pole says "mixed" or "mixed (ver classification_risk)" without listing specific units. If evasive, flag as "unit_used_evasive."
what_it_supports not template: verify that what_it_supports.yes is NOT the generic text "Coexistencia de los patrones documentados en las cards referenciadas." If it is, flag as "what_it_supports_is_template."
card-polo relevance spot check: for TCs with >15 Signal IDs, spot-check 2 random cards per pole — does each card relate to the pole's definition? If not, flag as "card_polo_mismatch" with the specific card ID.
Behavior
Run all checks on each TC.
If a check fails, mark it in the report with detail explaining the failure.
Do NOT discard the TC. Flag it.
A TC that fails checks gets added to review_queue.md with validation issues noted.
The validator does not fix candidates. It reports.
Validation summary
```json
{
  "total_candidates": N,
  "passed": N,
  "failed": N,
  "checks_most_failed": ["check_name", ...],
  "candidates_needing_attention": ["TC-NNN", ...]
}
```
Fail states
TC file unreadable → log, skip, continue.
Canon file missing → cannot validate, abort.
