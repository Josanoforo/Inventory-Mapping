# Module 06 — Validator

## Purpose

Run the 8-point self-check from the canonical protocol against every produced TC. Flag failures without discarding.

## Input

- `output/tension_candidates/TC-*.md`
- `reference/protocol_canonical.md` (the 8 checks)

## Output

- `working/validation/candidate_reports/TC-NNN_validation.json` — per candidate, validates against `schemas/validation_report.schema.json`
- `working/validation/validation_summary.json` — aggregate results

## Checks (from canon)

1. Does every candidate have verified Signal IDs with descriptions in parentheses?
2. Does every candidate pass Candidate Generation Rules (not pure frequency)?
3. Are polos defined in corpus terms, not absolute ranges?
4. Are mixed units declared, not hidden?
5. Does "What this candidate actually supports" distinguish what the cards show from what someone might infer?
6. Is there at least one Rejected Grouping in the output?
7. Are Coverage Gaps reported in the output?
8. Is all language mechanical (no valorative adjectives)?

## Additional checks

9. Does the TC type match the actual mechanical relation?
10. Are all Signal IDs verified against source files?
11. Are human fields empty?
12. Does the TC validate against `schemas/tension_candidate.schema.json`?

## Behavior

- Run all checks on each TC.
- If a check fails, mark it in the report with detail explaining the failure.
- Do NOT discard the TC. Flag it.
- A TC that fails checks gets added to review_queue.md with validation issues noted.
- The validator does not fix candidates. It reports.

## Validation summary

```json
{
  "total_candidates": N,
  "passed": N,
  "failed": N,
  "checks_most_failed": ["check_name", ...],
  "candidates_needing_attention": ["TC-NNN", ...]
}
```

## Fail states

- TC file unreadable → log, skip, continue.
- Canon file missing → cannot validate, abort.
