# Rejected Groupings — v4 (Round 1, 75 cards)

---

## FRI-003-REJECTED
**Scan type:** frictions
**Signal IDs:** SC-R1-024, SC-R1-025, SC-R1-027, SC-R1-028
**Reason:** same_actor_discrepancy — all 4 signal IDs have actor=platform. The payout restriction (no payout for sellers in countries without direct deposit or PayPal) is documented entirely in platform cards. No seller-actor card documents the experience of being unpaid.
**Why it does not generate a DT question:** Both sides of the potential friction are platform documents. The affected population (sellers in unpaid countries) is not documented in the corpus. The pattern is a policy cluster, not a friction with two documented actors.

---

## FRI-005-REJECTED
**Scan type:** frictions
**Signal IDs:** SC-R1-038, SC-R1-070
**Reason:** same_actor_discrepancy — both signal IDs have actor=platform. SC-R1-038 documents the $100 price cap for Discover mobile eligibility; SC-R1-070 documents the $5,000 maximum price for Gumroad products. No seller card documents the experience of being excluded from Discover mobile due to price.
**Why it does not generate a DT question:** Both sides are platform policy documents. No seller-side experience of the exclusion is documented in this corpus.

---

## CON-001
**Scan type:** contradictions
**Signal IDs:** SC-R1-005, SC-R1-032, SC-R1-035
**Reason:** same_actor_discrepancy — all 3 signal IDs have actor=platform. The apparent inconsistency between '10% + $0.50' (SC-R1-005) and '10% flat fee' (SC-R1-032, SC-R1-035) exists within platform documents. Possible versioning difference (SC-R1-032 dated July 2023; others undated).
**Why it does not generate a DT question:** The inconsistency is between official platform documents, not between platform and seller experience. Without a seller card documenting confusion or harm from this inconsistency, it does not generate a DT question.

---

## ASY-001
**Scan type:** asymmetries
**Signal IDs:** SC-R1-050, SC-R1-054, SC-R1-060, SC-R1-056, SC-R1-051, SC-R1-049, SC-R1-062
**Reason:** Duplicate of TC-001 (seller income asymmetry already covered) plus same_actor_discrepancy (all 7 signal IDs have actor=seller).
**Why it does not generate a DT question:** TC-001 already covers the seller income asymmetry pattern with cards from other rounds. Additionally, all cards are seller-actor — no cross-actor contrast is present in this Round 1 subset alone.

---

## COO-001
**Scan type:** co_occurrences
**Signal IDs:** SC-R1-011, SC-R1-024, SC-R1-025, SC-R1-027, SC-R1-028
**Reason:** No DT question — consistent co-occurrence of payout restriction policy cards from a single actor (platform). No seller-side experience documented.
**Why it does not generate a DT question:** The co-occurrence documents a single-actor policy cluster. All cards describe the same policy from different official sources. Understanding the relationship between these cards would not change a design decision without the missing buyer/seller perspective.

---

## OPD-002
**Scan type:** opposite_directions
**Signal IDs:** SC-R1-001, SC-R1-002, SC-R1-064, SC-R1-016, SC-R1-017, SC-R1-014
**Reason:** same_actor_discrepancy — all 6 signal IDs have actor=platform. The contrast is between the platform's marketing/features language (presenting seller autonomy) and its ToS/policy language (retaining unilateral control). Both forces are documented in platform documents.
**Why it does not generate a DT question:** As a pattern, this contrast exists entirely within platform-authored documents. Without a seller-side card documenting the experience of the tension between these two platform framings, it does not generate a DT question independently.

---

## LEX-001
**Scan type:** lexical_overlap
**Signal IDs:** SC-R1-005, SC-R1-032, SC-R1-035, SC-R1-033
**Reason:** Possible dedup (SC-R1-005, SC-R1-032, SC-R1-035 all document the 10% platform fee from different official sources) plus vocabulary coincidence (SC-R1-033 uses '10%' for affiliate commission, a different mechanism). No explicit friction between cards.
**Why it does not generate a DT question:** The overlap is a deduplication signal. The cards document the same or similar policies from different official documents. SC-R1-033's 10% figure refers to a different mechanism (affiliate commission) — vocabulary coincidence, not the same phenomenon.

---

## LEX-002
**Scan type:** lexical_overlap
**Signal IDs:** SC-R1-049, SC-R1-062, SC-R1-048
**Reason:** Possible dedup — three seller cards describing the same phenomenon (zero or ineffective organic traffic from Gumroad Discover) from different sources and dates. No explicit friction between the cards.
**Why it does not generate a DT question:** The cards are consistent with each other. Their co-occurrence provides evidence for the blocked pole in TC-003 and TC-005 but does not generate a distinct DT question on its own. These cards are already included as evidence in TC-003, TC-005.

---

## LEX-003
**Scan type:** lexical_overlap
**Signal IDs:** SC-R1-034, SC-R1-037
**Reason:** Vocabulary coincidence — both cards cite '90 days' but for different mechanisms (platform-initiated refund window vs buyer-initiated chargeback window). No explicit friction between the cards.
**Why it does not generate a DT question:** The shared timeframe is coincidental. The two mechanisms (platform refund right, bank chargeback right) are different but both documented consistently. These cards are included in TC-004's blocker pole.
