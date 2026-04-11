# Review Queue — v4 (Round 1, 75 cards)

Generated: 2026-04-11

---

| ID | Type | Status | Signal IDs | Source Pattern(s) | Validation |
|----|------|--------|------------|-------------------|------------|
| TC-002 | fricción | pending_review | 4 (SC-R1-036, SC-R1-038, SC-R1-047, SC-R1-061) | FRI-001 | pending |
| TC-003 | fricción | pending_review | 7 (SC-R1-073, SC-R1-055, SC-R1-067, SC-R1-069, SC-R1-065, SC-R1-062, SC-R1-049) | FRI-002, OPD-001 | pending |
| TC-004 | fricción | pending_review | 7 (SC-R1-015, SC-R1-016, SC-R1-017, SC-R1-018, SC-R1-034, SC-R1-029, SC-R1-046) | COO-003, FRI-004 | pending |
| TC-005 | asimetría distributiva | pending_review | 7 (SC-R1-067, SC-R1-065, SC-R1-066, SC-R1-063, SC-R1-062, SC-R1-049, SC-R1-048) | ASY-002 | pending |
| TC-006 | co-ocurrencia significativa | pending_review | 6 (SC-R1-005, SC-R1-006, SC-R1-036, SC-R1-044, SC-R1-047, SC-R1-061) | COO-002 | pending |
| TC-007 | contradicción | needs_audit_before_classification | 3 (SC-R1-055, SC-R1-062, SC-R1-073) | CON-002 | pending |

---

**Total TCs: 6**
- pending_review: 5 (TC-002, TC-003, TC-004, TC-005, TC-006)
- needs_audit_before_classification: 1 (TC-007)

**Rejected groupings:** 9 (see output/v4/rejected_groupings.md)
**Coverage gaps:** 4 (see output/v4/coverage_gaps.md)
**Isolated signals:** 0

---

## Audit flag — TC-007
TC-007 requires audit before classification. The contradiction between seller-reported Discover threshold ($10 / first sale) and platform documentation (unspecified eligibility criteria) is partial: the platform card does not explicitly contradict the threshold, it simply does not specify it. Audit should verify whether Gumroad has published the specific threshold criteria elsewhere, and whether the seller-reported $10 / first-sale conditions are consistent with each other.
