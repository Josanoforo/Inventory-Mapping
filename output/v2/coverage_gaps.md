# Coverage Gaps — v2 Run (2026-04-11)

## GAP-001 — Buyer perspective absent
- **Gap name**: Buyer-side documentation absent from corpus
- **Signal IDs creating expectation**: SC-R1-034, SC-R1-038
- **Description**: No card in the corpus documents buyer motivations, buyer conversion behavior, buyer satisfaction, or the buyer decision-making process when purchasing on Gumroad. The corpus is entirely seller-perspective and platform-perspective.
- **Why it limits reading of the inventory**: Buyer behavior can only be inferred from seller and platform accounts. Patterns about refunds, chargebacks, and Discover discoverability cannot be evaluated from the buyer side. Any design decision affecting buyer experience lacks direct evidence.

---

## GAP-002 — Alternative platform coverage absent
- **Gap name**: Comparative platform data absent
- **Signal IDs creating expectation**: SC-R1-061, SC-R1-041
- **Description**: No cards document the terms, fees, policies, or seller experiences of Lemon Squeezy, Payhip, or other platforms mentioned as migration destinations. Platform mentions appear only as named entities in seller migration accounts.
- **Why it limits reading of the inventory**: Patterns about platform switching and competitive positioning (e.g., OPPO-003, OPPO-005) cannot be contextualized against alternatives. The Gumroad-specific patterns may be platform-specific or industry-wide — no basis to distinguish.

---

## GAP-003 — Post-purchase data absent
- **Gap name**: Post-purchase outcome data absent
- **Signal IDs creating expectation**: SC-R1-022, SC-R1-003
- **Description**: No card documents post-delivery outcomes: whether buyers complete or consume purchased content, repeat purchase rates, membership retention, or product return behavior. Documentation ends at point of delivery.
- **Why it limits reading of the inventory**: Patterns about refunds (FRIC-006), chargeback rates (OPPO-002), and membership economics (COOC-005) cannot be evaluated in the context of product consumption or repeat engagement. The refund and chargeback rates are documented as policies without documentation of what drives them.

---

## GAP-004 — Non-English-language market seller coverage absent
- **Gap name**: Non-English-language seller experience absent
- **Signal IDs creating expectation**: SC-R1-027, SC-R1-019
- **Description**: No card documents seller experiences in Spanish-speaking, Asia-Pacific, or other non-English-language markets despite the platform claiming 160+ country availability and USD-only settlement creating specific effects for non-USD sellers.
- **Why it limits reading of the inventory**: Geographic payout gap patterns (filtered as same_actor_discrepancy in this run) and the USD settlement mechanism (SC-R1-019, present in OPPO-004) cannot be evaluated against the population most affected by payout constraints. The English-language bias in the seller corpus likely over-represents markets where direct deposit is available.

---

## GAP-005 — Intermediate seller income range absent
- **Gap name**: Intermediate outcome range under-documented
- **Signal IDs creating expectation**: SC-R1-056, SC-R1-050, SC-R1-039
- **Description**: The corpus documents outcomes at the extremes (under $200 and over $15,000) but the $500-$15,000 range has only SC-R1-039 ($3,271 over 6 months) as a single card. Two or more independent cards with outcomes in this range are absent.
- **Why it limits reading of the inventory**: The shape of the seller income distribution cannot be determined from the corpus. The bimodal appearance of the distribution may be an artifact of which seller stories get published (high outcomes are publishable as success stories; very low outcomes are publishable as cautionary tales). The absence prevents evaluation of whether a typical seller outcome exists.

---

## GAP-006 — Template and AI prompt product type seller experience absent
- **Gap name**: Template, spreadsheet, AI prompt seller experience absent
- **Signal IDs creating expectation**: SC-R1-065, SC-R1-072
- **Description**: No seller-side card specifically documents experience selling templates, Notion products, AI prompts, spreadsheets, or planners on Gumroad — despite Discover category tags including these types (SC-R1-065) and these being frequently-cited product categories in the 2024-2026 period.
- **Why it limits reading of the inventory**: Product-type-specific patterns around discoverability and fee impact cannot be evaluated for these categories. Seller outcome patterns (TC-001, ASYM-001) may be skewed toward specific product types (PDFs, courses, art) that are over-represented in the seller blog corpus.

---

## GAP-007 — Membership and subscription dynamics data absent
- **Gap name**: Membership retention and recurring revenue data absent
- **Signal IDs creating expectation**: SC-R1-003, SC-R1-075
- **Description**: No card documents membership retention rates, failed recurring billing, subscription churn, or the economics of recurring revenue on Gumroad. The corpus documents membership feature availability but no seller-side outcomes from operating a membership product.
- **Why it limits reading of the inventory**: The fee structure for membership sales is not documented in the corpus (SC-R1-005 through SC-R1-036 document one-time sale fees but not recurring billing fee treatment). Any pattern involving recurring revenue relies on features documentation only.
