Search decomposition
- SD-01: Base platform transaction fee — exact percentage and flat amount as stated on lemonsqueezy.com/pricing
- SD-02: Monthly or recurring platform-access fee (or absence thereof)
- SD-03: Additional processing surcharges by transaction type: international, PayPal, subscription
- SD-04: Payout fees by method (Stripe bank, PayPal) and region (US vs non-US)
- SD-05: Marketing and affiliate feature fees (abandoned cart recovery, affiliate referral, affiliate payout)
- SD-06: Payout schedule, hold period, minimum threshold, and settlement currency
- SD-07: Chargeback dispute fee and platform refund-right policy
- SD-08: Accepted payment methods and subscription-specific limitations
- SD-09: Merchant of record declaration and tax-handling policy
- SD-10: Custom or volume-based pricing availability and eligibility
- SD-11: Currency support count and conversion policy for payouts

---

Part 1 - Clean findings (direct_verified)

None. All pages on lemonsqueezy.com and docs.lemonsqueezy.com returned HTTP 403 on direct fetch (Cloudflare anti-bot protection). No findings could be direct_verified.

---

Part 2 - Provisional findings (blocked_url_index_verified)

### F-P01
What: Lemon Squeezy charges a consolidated platform transaction fee of 5% + 50¢ per transaction, with the possibility of small additional fees in edge cases.
Verbatim snippet: "We consolidate complex platform fees into one simple transaction fee of 5% + 50¢, but there are edge cases where small additional fees may need to be applied."
Source: https://www.lemonsqueezy.com/pricing
source_type: pricing_page
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated
Notes: Recovery method: Google search index snippet of the same URL; direct fetch returned 403. Snippet appears consistently across multiple independent search queries.

### F-P02
What: There is no monthly fee to use Lemon Squeezy for payment processing; fees are charged only when sales are generated.
Verbatim snippet: "There is no monthly fee to use Lemon Squeezy for payment processing. Our pricing is aligned with you, and you only pay when you generate sales."
Source: https://www.lemonsqueezy.com/pricing
source_type: pricing_page
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated
Notes: Recovery method: Google search index snippet of the same URL; direct fetch returned 403.

### F-P03
What: The platform fee covers credit card transaction fees, currency conversion fees, and taxes. It is calculated on the total order value and collected when the order is placed.
Verbatim snippet: "When you make a sale using Lemon Squeezy, we take a small fee, known as the "platform fee", to cover the costs of credit card transaction fees, currency conversion fees, taxes (yes, we cover taxes) etc. and the net sales will be paid out to your bank account or PayPal account."
Source: https://docs.lemonsqueezy.com/help/getting-started/fees
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated
Notes: Recovery method: Google search index snippet of the same URL; direct fetch returned 403. Identical text appeared in six independent search queries.

### F-P04
What: An additional +1.5% fee is added to the platform fee for international (outside of the US) transactions, an additional +1.5% fee is added for PayPal transactions, and an additional +0.5% fee is added for subscription payments.
Verbatim snippet: [Stated in layout: "There are certain times when an additional fee might be added to the platform fee to cover processing fees: +1.5% for international (outside of the US) transactions · +1.5% for PayPal transactions · +0.5% for subscription payments"]
Source: https://docs.lemonsqueezy.com/help/getting-started/fees
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated
Notes: Recovery method: Google search index snippet of the same URL; direct fetch returned 403. Items separated by "·" appear as a bulleted list on the source page. All three surcharges appeared together in search results and are presented as a single layout passage following the colon.

### F-P05
What: Payout fee via Stripe (bank transfer) is 1% per payout for bank accounts outside the US.
Verbatim snippet: [Stated in layout: "1% per payout for bank accounts outside the US"]
Source: https://docs.lemonsqueezy.com/help/getting-started/fees
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated
Notes: Recovery method: Google search index snippet of the same URL; direct fetch returned 403. This item appears under the "→ Payouts via Stripe" subsection based on the page's table of contents structure (Platform fee · Payout fees · → Payouts via Stripe · → Payouts via PayPal · Marketing fees).

### F-P06
What: Payout fee via PayPal is a flat fee of $0.50 per payout for accounts in the US and 3% capped at $30 per payout for accounts outside the US.
Verbatim snippet: [Stated in layout: "A flat fee of $0.50 per payout for accounts in the US · 3% capped at $30 per payout for accounts outside the US"]
Source: https://docs.lemonsqueezy.com/help/getting-started/fees
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated
Notes: Recovery method: Google search index snippet of the same URL; direct fetch returned 403. These items appear under the "→ Payouts via PayPal" subsection based on the page's table of contents structure. Both items appeared consecutively in a single search snippet.

### F-P07
What: Lemon Squeezy charges additional marketing feature fees: +5% for payments recovered through abandoned cart emails, +3% for affiliate referrals charged to merchants, and +2% for affiliate payouts charged to affiliates.
Verbatim snippet: [Stated in layout: "Some of Lemon Squeezy's marketing features have additional fees. These include: +5% for payments recovered through abandoned cart emails · +3% for affiliate referrals (merchants) +2% for affiliate payouts (affiliates)"]
Source: https://docs.lemonsqueezy.com/help/getting-started/fees
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated
Notes: Recovery method: Google search index snippet of the same URL; direct fetch returned 403. Items appear under the "Marketing fees" section per the page's table of contents.

### F-P08
What: Custom pricing is available for fast-growing or large-scale businesses, those selling products lower than $10, or those processing high volumes of transactions, by contacting the sales team.
Verbatim snippet: "If you're a fast-growing or established large-scale business, sell products lower than $10, or have a business model that processes a high volume of transactions, contact our sales team for custom pricing."
Source: https://docs.lemonsqueezy.com/help/getting-started/fees
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated
Notes: Recovery method: Google search index snippet of the same URL; direct fetch returned 403.

### F-P09
What: Payouts are created twice monthly on the 1st and 15th of the month and include all sales since the last payout. Net sales are held for 13 days before becoming available for payout on the 14th and 28th of the month. Payouts can take 1-5 days to appear in a bank account.
Verbatim snippet: "Payouts are created twice monthly on the 1st and 15th of the month and include all sales since the last payout. Net sales are held for 13 days before becoming available for payout on the 14th and 28th of the month. Payouts can take 1-5 days to appear in your bank account. For example, if you make a sale on the 4th of the month, it will be included in the payout created on the 15th, and paid out on the 28th."
Source: https://docs.lemonsqueezy.com/help/getting-started/getting-paid
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated
Notes: Recovery method: Google search index snippet of the same URL; direct fetch returned 403. Identical text appeared across four independent search queries.

### F-P10
What: There is a minimum payout threshold of $50. If the upcoming payout does not meet this threshold it will remain "Pending" and be rolled over to the next payout cycle.
Verbatim snippet: "There is a minimum payout threshold of $50. If your upcoming payout doesn't meet this threshold it will remain "Pending" and be rolled over to the next payout cycle."
Source: https://docs.lemonsqueezy.com/help/getting-started/getting-paid
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated
Notes: Recovery method: Google search index snippet of the same URL; direct fetch returned 403.

### F-P11
What: Bank payouts are made in USD and converted to local currency using the mid-market exchange rate at the time of payout. PayPal payouts are always in USD.
Verbatim snippet: "Payouts made using bank transfers will be converted to your local currency using the mid-market exchange rate at the time of payout."
Source: https://docs.lemonsqueezy.com/help/getting-started/getting-paid
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated
Notes: Recovery method: Google search index snippet of the same URL; direct fetch returned 403. The "What" field statement about PayPal payouts in USD is supported by a separate passage from the same page appearing in the same search result: "Payouts made using PayPal are always in USD." These are two separate passages; only the bank transfer snippet is cited as the verbatim passage.

### F-P12
What: Lemon Squeezy is responsible for handling chargebacks. In most cases a full refund is issued on the seller's behalf and the refunded amount (minus the platform fee) plus a $15 dispute fee is deducted from the seller's next payout.
Verbatim snippet: "Generally, Lemon Squeezy is responsible for handling any chargebacks made against your sales. In most cases, we will offer a full refund on your behalf and deduct the refunded amount (minus our platform fee) plus a $15 dispute fee from your next payout."
Source: https://docs.lemonsqueezy.com/help/payments/refunds-chargebacks
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated
Notes: Recovery method: Google search index snippet of the same URL; direct fetch returned 403. Identical text appeared in two independent search queries.

### F-P13
What: Lemon Squeezy reserves the right to issue refunds within 60 days of purchase, at its own discretion, in order to prevent chargebacks.
Verbatim snippet: "That being said, Lemon Squeezy reserves the right to issue refunds within 60 days of purchase, at its own discretion, in order to prevent chargebacks."
Source: https://docs.lemonsqueezy.com/help/payments/refunds-chargebacks
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated
Notes: Recovery method: Google search index snippet of the same URL; direct fetch returned 403.

### F-P14
What: When a seller issues a refund, the refunded amount minus the platform fee is deducted from the seller's next payout. Refunds can take up to 10 days to appear on the customer's statement.
Verbatim snippet: "The refunded amount (minus our platform fee) will be deducted from your next payout."
Source: https://docs.lemonsqueezy.com/help/payments/refunds-chargebacks
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated
Notes: Recovery method: Google search index snippet of the same URL; direct fetch returned 403. The 10-day processing time for customer-facing refunds is stated in a separate passage from the same page ("Refunds can take up to 10 days to appear on your customer's statement") but is not included in this verbatim snippet to avoid concatenation.

### F-P15
What: For subscription products, only cards, Apple Pay, Google Pay and PayPal are supported as payment methods.
Verbatim snippet: "For subscription products we only support cards, Apple Pay, Google Pay and PayPal at this time."
Source: https://docs.lemonsqueezy.com/help/checkout/payment-methods
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated
Notes: Recovery method: Google search index snippet of the same URL; direct fetch returned 403.

### F-P16
What: Lemon Squeezy charges merchants a 3% fee for each order referred by an affiliate, added to the normal platform fee.
Verbatim snippet: "Lemon Squeezy will charge small 3% fee for each order referred by an affiliate, which will be added to the normal platform fee."
Source: https://docs.lemonsqueezy.com/help/affiliates-for-merchants/fees
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated
Notes: Recovery method: Google search index snippet of the same URL; direct fetch returned 403. Note the apparent grammatical omission ("charge small" rather than "charge a small") appears to reflect the source text as indexed.

### F-P17
What: Affiliates are charged a 2% fee of their commission for each referral, deducted from payouts.
Verbatim snippet: "A small 2% fee will be taken from each referral, which will be deducted from your payouts."
Source: https://docs.lemonsqueezy.com/help/affiliates/fees
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated
Notes: Recovery method: Google search index snippet of the same URL; direct fetch returned 403. A second sentence on the same page clarifies "We charge affiliates 2% fee of ther commission for each referral" (apparent typo "ther" in source).

---

Part 3 - Pattern candidates (sealed)

### PC-01
Pattern Candidate ID: PC-01
Candidate statement: Lemon Squeezy's fee structure uses a single base platform fee with additive percentage surcharges applied conditionally by transaction type (international, PayPal, subscription), marketing feature (abandoned cart), and affiliate channel.
Related Finding IDs: F-P01, F-P04, F-P07, F-P16, F-P17
Status: sealed; not validated

### PC-02
Pattern Candidate ID: PC-02
Candidate statement: Payout fees are differentiated by both payout method (Stripe bank vs PayPal) and region (US vs non-US), with US accounts receiving lower or zero fees on both methods.
Related Finding IDs: F-P05, F-P06
Status: sealed; not validated

### PC-03
Pattern Candidate ID: PC-03
Candidate statement: Lemon Squeezy retains its platform fee on refunded and chargebacked orders while passing the refunded amount and any dispute fee through to the seller's next payout.
Related Finding IDs: F-P12, F-P13, F-P14
Status: sealed; not validated

---

Part 4 - Could not verify / Out-of-scope

### F-X01: Stripe payout fee for US bank accounts
What: The Stripe (bank transfer) payout fee for US-based bank accounts is reported as 0% per payout, but this could not be verified from the fees help center page via search index snippets. The claim appears only in a blog post (excluded source type for this shard).
Verbatim snippet: "n/a — search index snippet of the fees page did not capture the US Stripe payout rate line item"
Source: https://docs.lemonsqueezy.com/help/getting-started/fees
source_type: help_center
verification_status: could_not_verify
Date: Accessed April 2026
Notes: The fees page's table of contents includes "→ Payouts via Stripe" as a subsection, and the non-US rate (1%) was captured. The US rate likely appears on the same page but was truncated in all search index snippets retrieved. A blog post at https://www.lemonsqueezy.com/blog/payout-fees-sliced states "0% per payout for bank accounts in the US" but blogs are an excluded source type.

### F-X02: Complete enumerated list of all accepted payment methods
What: The full list of all payment methods accepted at checkout (beyond cards and subscription-specific methods) could not be fully verified from the payment methods help center page. Partial list includes cards (Visa, Mastercard, American Express, Discover, Diners Club, JCB, China UnionPay), PayPal, Apple Pay, Google Pay, and bank debits, but the complete list and regional availability was not fully captured.
Verbatim snippet: "n/a — search index snippets captured partial content only"
Source: https://docs.lemonsqueezy.com/help/checkout/payment-methods
source_type: help_center
verification_status: could_not_verify
Date: Accessed April 2026
Notes: Multiple search queries returned fragments from this page but no single snippet contained the complete payment method list. The pricing page references "16 different payment methods" and "up to 21 payment methods" in different passages, creating ambiguity about the current count.

### F-X03: Terms of service fee-related provisions
What: The full terms of service could not be verified. The URL https://www.lemonsqueezy.com/legal/terms does not appear to exist; the actual URL is https://www.lemonsqueezy.com/terms. Search snippets captured partial terms content including liability caps and governing law, but no specific fee schedule or fee-change provisions were found in the terms.
Verbatim snippet: "n/a — page blocked; partial content from search index"
Source: https://www.lemonsqueezy.com/terms
source_type: policy_page
verification_status: could_not_verify
Date: Accessed April 2026
Notes: Direct fetch returned 403. Multiple search queries retrieved excerpts from the SaaS Service Agreement and End User Terms but did not surface any specific clauses governing fee changes, fee caps, or billing dispute resolution beyond the liability limitation clause. The provided URL (https://www.lemonsqueezy.com/legal/terms) does not resolve; the correct path appears to be /terms.

---

Research QA Notes
- Findings forced to Provisional: F-P01 through F-P17 (all 17 findings). Reason: all pages on lemonsqueezy.com and docs.lemonsqueezy.com returned HTTP 403 on direct fetch due to Cloudflare anti-bot protection. No page content could be directly fetched. All content was recovered from Google's search engine index (cached snippets of the same URLs).
- Findings degraded to could_not_verify: F-X01 (US Stripe payout fee — truncated in search snippets, only verifiable via excluded blog source type), F-X02 (full payment method list — incomplete capture in snippets), F-X03 (terms of service fee provisions — URL mismatch and incomplete capture).
- Findings degraded due to URL not fixable: F-X03 (provided URL /legal/terms does not exist; actual URL is /terms).
- Multi-speaker pages split: None applicable. All pages represent Lemon Squeezy's own voice.
- Truncated or partial sources: All sources are partial — recovered from search engine index snippets rather than full page fetches. The fees page (F-P03 through F-P08) appeared most complete across snippets. The terms page (F-X03) was most severely truncated.
- source_type ambiguities: The fees page at docs.lemonsqueezy.com/help/getting-started/fees could arguably be classified as either help_center or platform_doc; classified as help_center based on its location within the /help/ documentation path. The affiliate fees pages (F-P16, F-P17) are similarly within /help/ and classified as help_center.
- Coverage gaps where findings expected but not found: (1) Stripe payout fee for US bank accounts (0%) — expected on the fees page but not captured in snippets. (2) Specific supported countries list for bank payouts — the page at /help/getting-started/supported-countries exists but its full country list was not captured. (3) KYC/identity verification requirements — page exists at /help/getting-started/verify-your-identity but not within scope of fee/payment findings. (4) Tax-inclusive pricing toggle details — referenced on the sales-tax-vat page but not a fee finding. (5) Email marketing pricing tiers — referenced on the pricing page ("Monthly or annual charges for email marketing features are based on the total number of subscribers you have and are free for up to 500 subscribers") but specific tier pricing was not captured. (6) The provided URL https://docs.lemonsqueezy.com/help/getting-started/fees-and-taxes does not exist; the correct URL is https://docs.lemonsqueezy.com/help/getting-started/fees.
- Cases where input could not be decomposed without interpretation: None.