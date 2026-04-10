# Rejected Groupings

Patterns discarded during the pre-build filter or routing, not advanced to tension candidate status.

---

## COOC-004 — co_occurrences

- Signal IDs: SC-R1-050, SC-R1-060, SC-R1-054, SC-R1-039, SC-R1-056, SC-R1-051, SC-R1-052
- Reason for rejection: Seven cards co-occur around seller income reporting from Gumroad, but the routing_rationale in the scan identifies this as frequency clustering without a DT question test that passes. The distributional asymmetry in outcomes is already captured in ASYM-001 (TC-006). These cards document individual seller outcome reports that vary widely; they do not document a mechanism or friction between them.
- Why it does not generate a DT question: The cards describe seven distinct sellers reporting their own distinct outcomes. Resolving the relationship between these cards does not change a design decision about the platform itself — they are instances of outcomes, not mechanisms in tension.

---

## LEX-001 — lexical_overlap

- Signal IDs: SC-R1-005, SC-R1-032, SC-R1-033, SC-R1-035, SC-R1-036
- Reason for rejection: Five cards share the figure "10%" but apply it to distinct mechanisms: platform fee (SC-R1-005, SC-R1-032, SC-R1-035), affiliate commission rate (SC-R1-033), and Gumroad's component of the mobile app fee (SC-R1-036). The shared vocabulary reflects that Gumroad uses the same percentage rate for multiple distinct purposes. SC-R1-032 and SC-R1-035 are a deduplication signal (same help center policy stated in two articles). No explicit friction exists between these cards.
- Why it does not generate a DT question: The overlap is vocabulary coincidence, not a mechanism in tension. The fee-tier asymmetry across channels is already captured in ASYM-002 (TC-007); the affiliate rate is a distinct mechanism. Knowing that "10%" appears in five cards does not change a design decision.

---

## LEX-002 — lexical_overlap

- Signal IDs: SC-R1-034, SC-R1-076
- Reason for rejection: Both cards originate from the same source URL (help.gumroad.com/article/51, dated May 10, 2023). They document complementary provisions of the same policy page (Gumroad's proactive refund authority and the buyer's chargeback authority). Has only 2 Signal IDs from the same source, and no explicit friction exists between the cards themselves — they are complementary, not in friction.
- Why it does not generate a DT question: The two cards are from the same article and document the same policy from two angles. The friction pattern they participate in is already documented in FRIC-006 (TC-016). This is a deduplication awareness signal, not a tension.

---

## LEX-003 — lexical_overlap

- Signal IDs: SC-R1-031, SC-R1-071
- Reason for rejection: Both cards originate from the same source URL (help.gumroad.com/article/289, dated November 20, 2023) and report substantially the same figures (250 MB free limit, 16 GB paid limit). SC-R1-031 adds one detail not in SC-R1-071 (the 500 MB Download all threshold). These are near-identical extractions from the same article, not two independent sources. No friction exists between them.
- Why it does not generate a DT question: The two cards document the same policy from the same article. The file size asymmetry they both document is already captured in ASYM-004 (TC-009) and FRIC-004 (TC-014). This is a deduplication signal only.

---

## LEX-004 — lexical_overlap

- Signal IDs: SC-R1-006, SC-R1-036
- Reason for rejection: Both cards share the figure "30%" but apply it to distinct parties and channels. SC-R1-006 documents Gumroad's 30% Discover web fee (charged by Gumroad). SC-R1-036 documents the App Store/Google Play 30% component of the 40% mobile app total (charged by Apple/Google, not Gumroad). Only 2 Signal IDs, and no explicit friction exists — the surface vocabulary overlap masks a fundamental distinction in who charges the 30% and in what channel.
- Why it does not generate a DT question: Resolving the relationship between these two cards does not change a design decision because they already describe distinct line items in the fee structure. The fee-tier asymmetry is captured in ASYM-002 (TC-007).

---

## LEX-005 — lexical_overlap

- Signal IDs: SC-R1-049, SC-R1-062
- Reason for rejection: Both cards document sellers with 26-35 products receiving zero organic traffic. They are corroborating evidence for the same underlying mechanism (the first-sale Discover threshold), not two sources describing the phenomenon from different angles that create friction between them. Only 2 Signal IDs. No explicit friction between these two cards themselves.
- Why it does not generate a DT question: The two cards confirm the same observation from independent sellers. They are already included as support in CONT-003 (TC-004) and FRIC-001 / COOC-001 (TC-011) where they serve as corroborating evidence.

---

## LEX-006 — lexical_overlap

- Signal IDs: SC-R1-043, SC-R1-047, SC-R1-050, SC-R1-052, SC-R1-054, SC-R1-060
- Reason for rejection: Six cards from independent sellers share the territory of seller-reported income and dashboard figures from Gumroad. The vocabulary overlap reflects that they all draw on the same platform's data interface. These are six distinct sellers reporting their own distinct outcomes — there is no friction between the cards. The distributional asymmetry in outcomes is already captured in ASYM-001 (TC-006).
- Why it does not generate a DT question: The shared vocabulary (Gumroad dashboard, revenue figures) reflects a common data source, not a tension. Resolving the relationship between these six cards does not change a design decision about the platform.

---

**Verification count:** 7 needs_audit patterns received total. Filter dispositions:
- CONT-001 → passed filter → TC-002 (already existed)
- ASYM-004 → passed filter → TC-009
- ASYM-005 → passed filter → TC-010
- FRIC-003 → passed filter → TC-013
- FRIC-004 → passed filter → TC-014
- LEX-007 → from lexical_overlap scan, 3 Signal IDs, explicit friction documented → passed filter → TC-024

Total needs_audit received: 6. Total needs_audit passed to TC build: 6. Total needs_audit written to rejected: 0 (all 6 passed).

Total patterns routed to rejected_grouping from scan routing: 7 (COOC-004, LEX-001 through LEX-006).

Total written above: 7. This matches the 7 patterns with rejected_grouping routing.
