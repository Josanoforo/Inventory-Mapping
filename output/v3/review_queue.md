# Review Queue — v3

Generated from: output/tension_candidates_v3/
Date: 2026-04-11
Validation status: pending (validator has not run)

---

| ID | Type | Status | Signal IDs count | Validation |
|----|------|--------|-----------------|------------|
| TC-002 | contradicción | pending_review | 6 | pending |
| TC-003 | asimetría distributiva | pending_review | 5 | pending |
| TC-004 | fricción | pending_review | 3 | pending |
| TC-005 | fricción | needs_audit_before_classification | 3 | pending |
| TC-006 | dirección opuesta | pending_review | 6 | pending |
| TC-007 | dirección opuesta | pending_review | 5 | pending |
| TC-008 | co-ocurrencia significativa | pending_review | 8 | pending |
| TC-009 | co-ocurrencia significativa | pending_review | 8 | pending |
| TC-010 | co-ocurrencia significativa | pending_review | 4 | pending |
| TC-011 | contradicción | needs_audit_before_classification | 4 | pending |

**Total TCs built: 10**

---

## Notes for reviewer

- TC-002: Merged from CON-001 (contradictions) + LEX-004 (lexical_overlap). >70% signal ID overlap, same mechanism. Verify whether Gumroad has undocumented $10 threshold for Discover eligibility.
- TC-003: Single card in Polo A (SC-R1-067, marketplace). Consider whether additional marketplace context cards (SC-R1-063, SC-R1-065, SC-R1-066, SC-R1-068) should be moved from additional_context to Polo A.
- TC-004: FRI-002 origin. SC-R1-046 reports 'many users' without specifying source — assess credibility before classification.
- TC-005: Minimal support in Polo B (1 card, actor=seller, undated forum post). Verify if SC-R1-041 is temporally related to SC-R1-014/SC-R1-016 policy changes.
- TC-006: Overlap in signal IDs with TC-002 (SC-R1-049, SC-R1-062, SC-R1-055). Different mechanism — TC-002 is about declared vs actual eligibility criteria; TC-006 is about forces (easy setup vs audience dependency).
- TC-007: Overlap in signal IDs with TC-004 (SC-R1-046, SC-R1-053). Different mechanism — TC-004 is about specific friction of suspension/payout retention; TC-007 is about opposite forces of MoR centralization vs seller operational control.
- TC-008: Co-occurrence framing of the Discover system. Overlaps in signal IDs with TC-002, TC-003, TC-006. Consider whether TC-008 is redundant given TC-002 and TC-006 coverage.
- TC-009: Co-occurrence framing of payout access. Overlaps in signal IDs with TC-004 and TC-007. Consider whether TC-009 is redundant.
- TC-010: Minimal support in Polo B (1 card). The trust/credibility angle is not covered by other TCs; preserving for human review.
- TC-011: Polo B has 1 card (actor=source). The mathematical explanation (10% + $0.50 varying by price) may resolve this before classification.
