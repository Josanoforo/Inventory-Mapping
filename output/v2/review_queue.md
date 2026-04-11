# Review Queue — v2 Run (2026-04-11)

Generated from working/scans_v2/ artifacts. TC numbering continues from TC-001 (existing).

| ID | Type | Status | Signal IDs | Validation | Source Patterns |
|----|------|--------|------------|------------|-----------------|
| TC-002 | contradicción | pending_review | 3 (SC-R1-067, SC-R1-049, SC-R1-062) | pending | CONT-003 |
| TC-003 | fricción | pending_review | 3 (SC-R1-014, SC-R1-016, SC-R1-012) | pending | FRIC-005 |
| TC-004 | fricción | pending_review | 3 (SC-R1-034, SC-R1-018, SC-R1-037) | pending | FRIC-006 |
| TC-005 | asimetría distributiva | pending_review | 8 (SC-R1-005, SC-R1-007, SC-R1-032, SC-R1-035, SC-R1-006, SC-R1-036, SC-R1-038, SC-R1-044) | pending | ASYM-002, COOC-002 (merged) |
| TC-006 | dirección opuesta | pending_review | 6 (SC-R1-067, SC-R1-066, SC-R1-069, SC-R1-055, SC-R1-062, SC-R1-073) | pending | OPPO-001, COOC-001 (merged) |
| TC-007 | dirección opuesta | pending_review | 6 (SC-R1-042, SC-R1-070, SC-R1-033, SC-R1-018, SC-R1-034, SC-R1-006) | pending | OPPO-002 |
| TC-008 | dirección opuesta | pending_review | 7 (SC-R1-002, SC-R1-042, SC-R1-069, SC-R1-074, SC-R1-016, SC-R1-014, SC-R1-017) | pending | OPPO-003 |
| TC-009 | dirección opuesta | pending_review | 6 (SC-R1-027, SC-R1-011, SC-R1-001, SC-R1-024, SC-R1-028, SC-R1-019) | pending | OPPO-004 |
| TC-010 | dirección opuesta | pending_review | 6 (SC-R1-067, SC-R1-070, SC-R1-010, SC-R1-016, SC-R1-014, SC-R1-029) | pending | OPPO-005 |
| TC-011 | co-ocurrencia significativa | pending_review | 6 (SC-R1-014, SC-R1-015, SC-R1-016, SC-R1-017, SC-R1-018, SC-R1-023) | pending | COOC-003 |
| TC-012 | co-ocurrencia significativa | pending_review | 10 (SC-R1-011, SC-R1-017, SC-R1-019, SC-R1-021, SC-R1-024, SC-R1-025, SC-R1-026, SC-R1-027, SC-R1-028, SC-R1-030) | pending | COOC-005 |

**Total TCs built in this run: 11**
**Previous run TC count: 23**

## Notes

- TC-001 carries over from previous run (not rebuilt in v2).
- TC-002 through TC-012 are new v2 TCs built from working/scans_v2/ artifacts.
- LEX-007 (needs_audit, lexical_overlap) was discarded by pre-build filter: 3+ IDs but no explicit friction between cards. Written to rejected_groupings.md.
- ASYM-002 and COOC-002 merged into TC-005 (>70% shared Signal IDs, same mechanism).
- OPPO-001 and COOC-001 merged into TC-006 (>70% shared Signal IDs, same mechanism).
- SC-R1-076 referenced in prior scan artifacts does not exist in the card index (corpus has 75 cards, SC-R1-001 to SC-R1-075); excluded from all patterns in this run.
- The v2 run produced fewer TCs (11 vs 23 previous) primarily due to the same-actor filter, which routed 11 patterns to rejected_grouping that were previously routed as tension_candidate or needs_audit.
