# Review Queue — Tension Candidates

All tension candidates produced in Module 05 (Candidate Builder), Round 1.

| TC ID | Type | Status | Signal IDs count | Source patterns | Validation |
|-------|------|--------|-----------------|-----------------|------------|
| TC-002 | contradicción | needs_audit_before_classification | 3 | CONT-001 | pending |
| TC-003 | contradicción | pending_review | 2 | CONT-002 | pending |
| TC-004 | contradicción | pending_review | 3 | CONT-003 | pending |
| TC-005 | contradicción | pending_review | 3 | CONT-004 | pending |
| TC-006 | asimetría distributiva | pending_review | 7 | ASYM-001 | pending |
| TC-007 | asimetría distributiva | pending_review | 8 | ASYM-002 + COOC-002 (merge) | pending |
| TC-008 | asimetría distributiva | pending_review | 5 | ASYM-003 | pending |
| TC-009 | asimetría distributiva | needs_audit_before_classification | 2 | ASYM-004 | pending |
| TC-010 | asimetría distributiva | needs_audit_before_classification | 3 | ASYM-005 | pending |
| TC-011 | fricción | pending_review | 5 | FRIC-001 + COOC-001 (merge) | pending |
| TC-012 | fricción | pending_review | 4 | FRIC-002 | pending |
| TC-013 | fricción | needs_audit_before_classification | 2 | FRIC-003 | pending |
| TC-014 | fricción | needs_audit_before_classification | 2 | FRIC-004 | pending |
| TC-015 | fricción | pending_review | 3 | FRIC-005 | pending |
| TC-016 | fricción | pending_review | 4 | FRIC-006 | pending |
| TC-017 | co-ocurrencia significativa | pending_review | 6 | COOC-003 | pending |
| TC-018 | co-ocurrencia significativa | pending_review | 10 | COOC-005 | pending |
| TC-019 | dirección opuesta | pending_review | 6 | OPPO-001 | pending |
| TC-020 | dirección opuesta | pending_review | 7 | OPPO-002 | pending |
| TC-021 | dirección opuesta | pending_review | 7 | OPPO-003 | pending |
| TC-022 | dirección opuesta | pending_review | 6 | OPPO-004 | pending |
| TC-023 | dirección opuesta | pending_review | 6 | OPPO-005 | pending |
| TC-024 | fricción | needs_audit_before_classification | 3 | LEX-007 | pending |

**Total TCs: 23** (TC-002 through TC-024)

**Notes on merges:**
- TC-007 merges ASYM-002 and COOC-002: both patterns share 7 of 7 ASYM-002 signal IDs (100% overlap) and describe the same mechanism (fee structure asymmetry by sales channel). COOC-002 adds SC-R1-044 as additional context.
- TC-011 merges FRIC-001 and COOC-001: both patterns share 4 of 4 FRIC-001 signal IDs (100% overlap) and describe the same territory (Discover first-sale gate). COOC-001 adds SC-R1-049 to the merged TC.

**Status summary:**
- pending_review: 17 TCs
- needs_audit_before_classification: 6 TCs (TC-002, TC-009, TC-010, TC-013, TC-014, TC-024)

**Rejected groupings: 7** (COOC-004, LEX-001 through LEX-006) — see output/rejected_groupings.md

**Coverage gaps: 7** (GAP-001 through GAP-007) — see output/coverage_gaps.md

**Isolated signals: 0** — see output/isolated_signals.md
