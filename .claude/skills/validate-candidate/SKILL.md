# Validate Candidate — Skill

Read `modules/06_validator.md` before executing.

## Steps

### 1. Load references

- Read `reference/protocol_canonical.md` (the 8 canonical checks).
- Read `schemas/tension_candidate.schema.json`.

### 2. For each TC in `output/tension_candidates/`

Run all 12 checks from the module:

1. **Signal IDs verified**: every ID has description in parentheses.
2. **Candidate Generation Rules**: not pure frequency — at least one rule from canon applies.
3. **Corpus-term polos**: definitions reference corpus, not absolute ranges.
4. **Units declared**: mixed units flagged, not hidden.
5. **Supports distinction**: "yes" and "no" sections distinguish evidence from inference.
6. **Rejected Groupings exist**: `output/rejected_groupings.md` is non-empty.
7. **Coverage Gaps reported**: `output/coverage_gaps.md` is non-empty.
8. **Mechanical language**: no valorative adjectives in mechanical_relation or mechanical_summary fields.
9. **Type matches relation**: the TC type corresponds to the actual pattern (not misclassified).
10. **Signal IDs verified against source**: spot-check 3 random IDs per TC against `input/` files.
11. **Human fields empty**: all human fields are empty strings.
12. **Schema valid**: TC parses and validates against tension_candidate.schema.json.

### 3. Write per-candidate report

For each TC, write `working/validation/candidate_reports/TC-NNN_validation.json`:
```json
{
  "candidate_id": "TC-002",
  "passed": true,
  "checks": [
    {"check": "signal_ids_verified", "passed": true, "detail": ""},
    {"check": "candidate_generation_rules", "passed": true, "detail": ""},
    ...
  ],
  "timestamp": "..."
}
```

Validate against `schemas/validation_report.schema.json`.

### 4. Write summary

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

### 5. Update review queue

Update `output/review_queue.md` with validation results for each TC.

## Important

Do not fix candidates. Do not discard candidates. Only report.
