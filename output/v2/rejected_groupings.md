# Rejected Groupings — v2 Run (2026-04-11)

## From scan: contradictions

### CONT-001
- **Pattern ID**: CONT-001
- **Scan type**: contradictions
- **Signal IDs**: SC-R1-005, SC-R1-032, SC-R1-035
- **Reason for rejection**: same_actor_discrepancy — all Signal IDs share actor value "marketplace"
- **Why it does not generate a DT question**: All cards are official Gumroad documentation (pricing page and help center). The difference between 10%+$0.50 and 10% flat may reflect article-level omission rather than a genuine product design contradiction. No cross-actor opposition present.

### CONT-002
- **Pattern ID**: CONT-002
- **Scan type**: contradictions
- **Signal IDs**: SC-R1-034, SC-R1-038
- **Reason for rejection**: same_actor_discrepancy — all Signal IDs share actor value "seller"
- **Why it does not generate a DT question**: Both cards are from seller-domain official Gumroad documentation; they describe different channel-specific refund policies (web vs mobile app), not a single-subject contradiction between independent actors.

### CONT-004
- **Pattern ID**: CONT-004
- **Scan type**: contradictions
- **Signal IDs**: SC-R1-027, SC-R1-024, SC-R1-028
- **Reason for rejection**: same_actor_discrepancy — all Signal IDs share actor value "seller"
- **Why it does not generate a DT question**: All three cards are from Gumroad help center articles in the seller domain; the geographic payment breadth claim and the no-payout-path documentation are from the same actor perspective (official platform documentation for sellers), removing cross-actor opposition.

---

## From scan: frictions

### FRIC-001
- **Pattern ID**: FRIC-001
- **Scan type**: frictions
- **Signal IDs**: SC-R1-055, SC-R1-062, SC-R1-073, SC-R1-069
- **Reason for rejection**: same_actor_discrepancy — all Signal IDs share actor value "seller"
- **Why it does not generate a DT question**: All four cards are in the seller domain; the blocking element (first-sale threshold) and blocked element (Discover traffic) are both documented from the seller or seller-tool perspective, with no marketplace-actor documentation of the mechanism.

### FRIC-002
- **Pattern ID**: FRIC-002
- **Scan type**: frictions
- **Signal IDs**: SC-R1-024, SC-R1-028, SC-R1-025, SC-R1-027
- **Reason for rejection**: same_actor_discrepancy — all Signal IDs share actor value "seller"
- **Why it does not generate a DT question**: All four cards are Gumroad help center documentation in the seller domain; the payout gap and the broad availability claim come from the same actor perspective, removing cross-actor friction.

### FRIC-003
- **Pattern ID**: FRIC-003
- **Scan type**: frictions
- **Signal IDs**: SC-R1-029, SC-R1-046
- **Reason for rejection**: same_actor_discrepancy — all Signal IDs share actor value "seller"
- **Why it does not generate a DT question**: Both cards document the seller side of the suspension-and-hold mechanism; no cross-actor documentation of the mechanism present.

### FRIC-004
- **Pattern ID**: FRIC-004
- **Scan type**: frictions
- **Signal IDs**: SC-R1-031, SC-R1-071
- **Reason for rejection**: same_actor_discrepancy — all Signal IDs share actor value "seller"
- **Why it does not generate a DT question**: Both cards are duplicate extractions from the same help center article, both in seller domain; no cross-actor documentation present.

---

## From scan: asymmetries

### ASYM-001
- **Pattern ID**: ASYM-001
- **Scan type**: asymmetries
- **Signal IDs**: SC-R1-050, SC-R1-060, SC-R1-054, SC-R1-039, SC-R1-056, SC-R1-051, SC-R1-049
- **Reason for rejection**: same_actor_discrepancy — all Signal IDs share actor value "seller"
- **Why it does not generate a DT question**: All cards are seller self-reports from blogs. The distributional asymmetry is already covered by TC-001 from the prior run. This cluster lacks cross-actor support.

### ASYM-003
- **Pattern ID**: ASYM-003
- **Scan type**: asymmetries
- **Signal IDs**: SC-R1-027, SC-R1-011, SC-R1-024, SC-R1-025, SC-R1-028
- **Reason for rejection**: same_actor_discrepancy — all Signal IDs share actor value "seller"
- **Why it does not generate a DT question**: All five cards are official Gumroad help center documentation in the seller domain. The payout asymmetry pattern is covered with cross-actor support in OPPO-004 (routed tension_candidate).

### ASYM-004
- **Pattern ID**: ASYM-004
- **Scan type**: asymmetries
- **Signal IDs**: SC-R1-031, SC-R1-071
- **Reason for rejection**: same_actor_discrepancy — all Signal IDs share actor value "seller"
- **Why it does not generate a DT question**: Both cards are duplicate extractions from the same help center article in seller domain. Same-source, same-actor, no friction.

### ASYM-005
- **Pattern ID**: ASYM-005
- **Scan type**: asymmetries
- **Signal IDs**: SC-R1-029, SC-R1-046, SC-R1-053
- **Reason for rejection**: same_actor_discrepancy — all Signal IDs share actor value "seller"
- **Why it does not generate a DT question**: All three cards are in the seller domain; the official policy documentation and seller experience reports are from the same actor perspective, removing cross-actor opposition needed for asymmetry tension.

---

## From scan: co_occurrences

### COOC-004
- **Pattern ID**: COOC-004
- **Scan type**: co_occurrences
- **Signal IDs**: SC-R1-050, SC-R1-060, SC-R1-054, SC-R1-039, SC-R1-056, SC-R1-051, SC-R1-052
- **Reason for rejection**: DT question test fails — pure frequency clustering of seller income reports
- **Why it does not generate a DT question**: Seven cards report different seller outcomes but do not document a mechanism or friction between them. The distributional variation is captured in ASYM-001 (prior run, TC-001). This cluster is aggregation of outcomes without a design-relevant tension.

---

## From scan: lexical_overlap

### LEX-001
- **Pattern ID**: LEX-001
- **Scan type**: lexical_overlap
- **Signal IDs**: SC-R1-005, SC-R1-032, SC-R1-033, SC-R1-035, SC-R1-036
- **Reason for rejection**: shared vocabulary (10%) without explicit friction; deduplication signal for SC-R1-032 and SC-R1-035
- **Why it does not generate a DT question**: The 10% figure applies to distinct mechanisms across these cards; no friction exists between them.

### LEX-002
- **Pattern ID**: LEX-002
- **Scan type**: lexical_overlap
- **Signal IDs**: SC-R1-034, SC-R1-037
- **Reason for rejection**: complementary cards from adjacent articles on same topic; no explicit friction
- **Why it does not generate a DT question**: Both cards document different aspects of the same refund/chargeback policy domain; they are corroborative, not in opposition.

### LEX-003
- **Pattern ID**: LEX-003
- **Scan type**: lexical_overlap
- **Signal IDs**: SC-R1-031, SC-R1-071
- **Reason for rejection**: near-identical extractions from same help center article; deduplication signal
- **Why it does not generate a DT question**: Same article, same content, no friction between the cards.

### LEX-004
- **Pattern ID**: LEX-004
- **Scan type**: lexical_overlap
- **Signal IDs**: SC-R1-006, SC-R1-036
- **Reason for rejection**: same figure (30%) applied to distinct mechanisms and parties; no explicit friction
- **Why it does not generate a DT question**: SC-R1-006 is the Gumroad Discover fee; SC-R1-036's 30% is the Apple/Google store fee. Different parties, different channels.

### LEX-005
- **Pattern ID**: LEX-005
- **Scan type**: lexical_overlap
- **Signal IDs**: SC-R1-049, SC-R1-062
- **Reason for rejection**: corroborating observations from independent sellers; no explicit friction between the cards
- **Why it does not generate a DT question**: Both cards confirm the same experience (zero organic traffic); they are corroborating evidence, not opposing claims.

### LEX-006
- **Pattern ID**: LEX-006
- **Scan type**: lexical_overlap
- **Signal IDs**: SC-R1-043, SC-R1-047, SC-R1-050, SC-R1-052, SC-R1-054, SC-R1-060
- **Reason for rejection**: shared vocabulary (dashboard figures) without explicit friction between cards; different sellers, different outcomes, different time periods
- **Why it does not generate a DT question**: These are independent sellers reporting their own outcomes; no friction between the cards themselves.

### LEX-007 (pre-build filter discard)
- **Pattern ID**: LEX-007
- **Scan type**: lexical_overlap
- **Signal IDs**: SC-R1-040, SC-R1-050, SC-R1-043
- **Reason for rejection**: pre-build filter — lexical_overlap with 3+ IDs but no explicit friction between cards (epistemic friction about evidence quality is not explicit friction between card content)
- **Why it does not generate a DT question**: SC-R1-040 documents that screenshots can be fabricated; SC-R1-050 and SC-R1-043 report income figures. The manipulation capability is possible but not established as applying to any specific card. The evidentiary concern is a classification risk flag, not a content friction between cards.
