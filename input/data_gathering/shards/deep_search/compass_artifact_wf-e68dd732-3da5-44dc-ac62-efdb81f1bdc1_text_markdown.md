# SHARD: Gumroad × D1 — Platform mechanics and fee structure

---

# 1. Search Decomposition

**SD-01:** Base per-transaction fee for direct/profile sales (percentage and flat-rate amount)

**SD-02:** Discover marketplace per-transaction fee

**SD-03:** Mobile app per-transaction fee (iOS/Android in-app purchases)

**SD-04:** Monthly, recurring, listing, or insertion fees (presence or absence)

**SD-05:** Credit card processing and PayPal fee treatment relative to Gumroad fee

**SD-06:** Affiliate fee structure (commission rates, Gumroad Affiliates vs. Your Affiliates, additional platform fees)

**SD-07:** Refund fee treatment (portion of Gumroad fee returned or retained upon refund)

**SD-08:** Payout schedule (frequency, day of week, minimum holding period)

**SD-09:** Minimum payout threshold (base amount and country-specific variations)

**SD-10:** Payout methods by country (direct deposit, PayPal, Stripe Connect eligibility and restrictions)

**SD-11:** Transaction currency and conversion mechanics (processing currency, exchange rate source, conversion timing)

**SD-12:** VAT, sales tax, and GST collection and remittance scope by region

**SD-13:** Merchant of Record status (effective date, scope of tax obligations, ToS formalization)

**SD-14:** Purchasing Power Parity discount mechanics (range, data source, refresh frequency)

**SD-15:** Chargeback and dispute handling (who bears cost, Gumroad's discretion, supplier reimbursement)

---

# 2. Part 1 — Clean findings (direct_verified)

---

## F-01

**What:** Gumroad charges 10% + $0.50 per transaction for all sales through a creator's profile or direct links to customers.

**Verbatim snippet:** [Stated in layout: "10% + $0.50 Per transaction for all sales through your profile or direct links to your customers."]

**Source:** https://gumroad.com/pricing

**source_type:** pricing_page

**verification_status:** direct_verified

**Date:** Accessed April 2026; page undated

**Notes:** Stated in a pricing card element on the page. The heading "10% + $0.50" and the description text are separated by a line break in the card layout.

---

## F-02

**What:** Gumroad charges 30% per transaction when new customers find and buy from a creator through the Discover marketplace.

**Verbatim snippet:** [Stated in layout: "30% Per transaction when new customers find and buy from you through our discover marketplace."]

**Source:** https://gumroad.com/pricing

**source_type:** pricing_page

**verification_status:** direct_verified

**Date:** Accessed April 2026; page undated

**Notes:** Stated in a pricing card element directly below the 10% + $0.50 card. The heading "30%" and the description text are separated by a line break in the card layout.

---

## F-03

**What:** Gumroad has no hidden fees and no monthly charges.

**Verbatim snippet:** "We believe in transparent pricing that helps you grow. No hidden fees, no monthly charges."

**Source:** https://gumroad.com/pricing

**source_type:** pricing_page

**verification_status:** direct_verified

**Date:** Accessed April 2026; page undated

**Notes:** Subheading text appearing directly below the main "Simple, transparent pricing" header on the pricing page.

---

## F-04

**What:** Since January 1, 2025, Gumroad handles all tax obligations as a Merchant of Record, managing sales tax collection and remittance worldwide.

**Verbatim snippet:** "Since January 1, 2025, Gumroad handles ALL your tax obligations. Yes, you read that right – we manage sales tax collection and remittance worldwide."

**Source:** https://gumroad.com/pricing

**source_type:** pricing_page

**verification_status:** direct_verified

**Date:** Accessed April 2026; page undated

**Notes:** From the "We're a Merchant of Record" section of the pricing page, under the "Tax management" label.

---

## F-05

**What:** Gumroad handles all tax obligations for global sales automatically, including VAT, GST, and other international tax requirements.

**Verbatim snippet:** "We'll handle all tax obligations for your global sales automatically. You don't need to worry about VAT, GST, or any other international tax requirements."

**Source:** https://gumroad.com/pricing

**source_type:** pricing_page

**verification_status:** direct_verified

**Date:** Accessed April 2026; page undated

**Notes:** [Stated in layout: FAQ block, answer to the question "What about international sales?"]

---

## F-06

**What:** Gumroad collects taxes in regions where it has tax obligations as a merchant of record; coverage varies by location.

**Verbatim snippet:** "We'll collect taxes in regions where we have tax obligations as a merchant of record. This varies by location, and we'll automatically handle the appropriate tax collection for each sale."

**Source:** https://gumroad.com/pricing

**source_type:** pricing_page

**verification_status:** direct_verified

**Date:** Accessed April 2026; page undated

**Notes:** [Stated in layout: FAQ block, answer to the question "Will Gumroad collect taxes everywhere?"]

---

## F-07

**What:** Gumroad collects VAT as required and sends it to the EU.

**Verbatim snippet:** [Stated in layout: "Don't sweat VAT We collect VAT as required and send it to the EU. You don't need to do a thing."]

**Source:** https://gumroad.com/features

**source_type:** platform_doc

**verification_status:** direct_verified

**Date:** Accessed April 2026; page undated

**Notes:** Stated in a feature card under the "Money, incoming" / "Payment Integrations" section. Heading "Don't sweat VAT" and body text are separated by a line break in the card layout.

---

## F-08

**What:** Gumroad is the merchant of record for the resale of Products to Buyers per the Terms of Service. Suppliers shall not issue invoices or make demands for payment to Buyers.

**Verbatim snippet:** "You acknowledge and agree that Gumroad is the merchant of record for the resale of your Products to the Buyers, and that you shall not issue any invoice or make any demand for payment to any Buyer in relation to any completed resale of your Products through the Services."

**Source:** https://gumroad.com/terms

**source_type:** policy_page

**verification_status:** direct_verified

**Date:** Effective Date: January 1, 2025; Last Updated Date: December 10, 2024

**Notes:** From Section 6.1 (Appointment) of the Terms of Service.

---

## F-09

**What:** Suppliers pay Gumroad a per-transaction fee (the "Gumroad Fee") for each resale, automatically deducted from the purchase price paid by the Buyer. The remainder, less taxes and other charges, is the "Supplier Fee" paid to the supplier.

**Verbatim snippet:** "In consideration of Gumroad's MOR Services, in respect of each resale of your Products through the Services, you agree to pay Gumroad a per-transaction fee (the, "Gumroad Fee") for each resale made by Gumroad through the Services. The Gumroad Fee owed for each resale through the Services is automatically deducted from the purchase price paid by the Buyer, with the remainder (less any amounts in respect of taxes and any other charges payable by you pursuant to this Agreement) owed and paid to you by Gumroad (such remainder amount, the "Supplier Fee")."

**Source:** https://gumroad.com/terms

**source_type:** policy_page

**verification_status:** direct_verified

**Date:** Effective Date: January 1, 2025; Last Updated Date: December 10, 2024

**Notes:** From Section 6.4 (Gumroad Fee and Supplier Fee). The original text contains a comma after "the," before "Gumroad Fee" which appears to be a typographical error in the Terms of Service as published.

---

## F-10

**What:** Gumroad does not assess or collect listing or insertion fees. Current Gumroad Fees can be viewed on the Pricing page and may change from time to time.

**Verbatim snippet:** "Gumroad does not assess or collect "listing" or "insertion" fees, but will collect the Gumroad Fee from buyer proceeds as described in section 6.4. The Gumroad Fees vary depending on whether a Product is resold on the Website or on the applicable Supplier Property that leverages the Services. The current Gumroad Fees can be viewed on the page "Pricing". We may change the Gumroad Fees from time to time by posting the changes on the Website."

**Source:** https://gumroad.com/terms

**source_type:** policy_page

**verification_status:** direct_verified

**Date:** Effective Date: January 1, 2025; Last Updated Date: December 10, 2024

**Notes:** From Section 11.1 (Supplier's Payment of Gumroad Fees).

---

## F-11

**What:** Regardless of the listed display currency, all transactions through Gumroad settle in USD.

**Verbatim snippet:** "Regardless of listed currency, all transactions through the Services will settle in USD."

**Source:** https://gumroad.com/terms

**source_type:** policy_page

**verification_status:** direct_verified

**Date:** Effective Date: January 1, 2025; Last Updated Date: December 10, 2024

**Notes:** From Section 9 (Currency Conversion).

---

## F-12

**What:** Gumroad handles Buyers' refund requests, chargebacks, and disputes in Gumroad's sole discretion. Suppliers are responsible for reimbursing Gumroad for amounts paid in connection with refunds, chargebacks, or disputes, plus any other reasonable costs.

**Verbatim snippet:** "Gumroad will handle Buyers' requests for refunds, chargebacks and other disputes with Buyers in Gumroad's sole discretion. The Supplier shall, at Gumroad's request, provide all information as may be requested by Gumroad to resolve Buyers' requests or disputes. Supplier is responsible for reimbursing Gumroad for the amount of any monies paid by Gumroad to Buyers or Third-Party Service Providers, or any other parties, in connection with refunds, chargebacks or disputes, as well as for any other reasonable costs incurred by Gumroad in resolving these requests."

**Source:** https://gumroad.com/terms

**source_type:** policy_page

**verification_status:** direct_verified

**Date:** Effective Date: January 1, 2025; Last Updated Date: December 10, 2024

**Notes:** From Section 7.1(a) (Refunds, Chargebacks, Disputes).

---

## F-13

**What:** Supplier Fees are paid after a completed resale transaction based on an agreed-upon settlement schedule, which is subject to change at Gumroad's discretion.

**Verbatim snippet:** "Supplier Fees owed to you by Gumroad will be paid to you after a completed resale transaction based on an agreed upon settlement schedule, which is subject to change at the discretion of Gumroad."

**Source:** https://gumroad.com/terms

**source_type:** policy_page

**verification_status:** direct_verified

**Date:** Effective Date: January 1, 2025; Last Updated Date: December 10, 2024

**Notes:** From Section 6.4 (Gumroad Fee and Supplier Fee).

---

## F-14

**What:** Gumroad may offset funds owed but not yet paid to suppliers against sums due, or reasonably likely to become due, to Gumroad.

**Verbatim snippet:** "Notwithstanding the forgoing, Gumroad may also offset against funds owed but not yet paid to Supplier via the Services any sums due, or reasonably likely to become due, to Gumroad pursuant to these Terms of Service."

**Source:** https://gumroad.com/terms

**source_type:** policy_page

**verification_status:** direct_verified

**Date:** Effective Date: January 1, 2025; Last Updated Date: December 10, 2024

**Notes:** From Section 6.4 (Gumroad Fee and Supplier Fee). The published text contains "forgoing" which appears to be a typo in the original Terms of Service (likely intended: "foregoing").

---

# 3. Part 2 — Provisional findings (blocked_url_index_verified)

---

## F-P01

**What:** For sales made on Gumroad's website, Gumroad charges a 10% flat fee. This does not include credit card processing or PayPal fees.

**Verbatim snippet:** "For sales made on Gumroad's website, we charge a 10% flat fee. This does not include: Credit card processing PayPal fees"

**Source:** https://help.gumroad.com/article/66-gumroads-fees

**source_type:** help_center

**verification_status:** blocked_url_index_verified

**Date:** Page last updated July 18, 2024 (per search index metadata)

**Notes:** Direct fetch of this URL returned an authentication wall ("Please sign in to continue"). Snippet recovered via Google search index, attributed to this exact URL in multiple independent search results. The items after "This does not include:" may be formatted as a list on the original page; search index flattened the formatting.

---

## F-P02

**What:** For sales made on the Gumroad mobile app, Gumroad charges 40% total (10% goes to Gumroad, and 30% goes to the App Store/Google Play Store).

**Verbatim snippet:** "For sales made on the Gumroad mobile app, we charge 40% (10% goes to Gumroad, and 30% goes to the App Store/Google Play Store)."

**Source:** https://help.gumroad.com/article/66-gumroads-fees

**source_type:** help_center

**verification_status:** blocked_url_index_verified

**Date:** Page last updated July 18, 2024 (per search index metadata)

**Notes:** Direct fetch returned authentication wall. Snippet recovered via Google search index attributed to this exact URL.

---

## F-P03

**What:** There are no additional fees for affiliates; only the affiliate's sales commission is deducted from the sale.

**Verbatim snippet:** "There are no additional fees for affiliates – only the affiliate's sales commission gets deducted from the sale."

**Source:** https://help.gumroad.com/article/66-gumroads-fees

**source_type:** help_center

**verification_status:** blocked_url_index_verified

**Date:** Page last updated July 18, 2024 (per search index metadata)

**Notes:** Direct fetch returned authentication wall. Snippet recovered via Google search index attributed to this exact URL.

---

## F-P04

**What:** In the case of refunds, Gumroad returns the Gumroad fee minus the fee charged by their payments processor, which is not returned to Gumroad.

**Verbatim snippet:** "In the case of refunds, we return the Gumroad fee minus the fee charged by our payments processor (which is not returned to us)."

**Source:** https://help.gumroad.com/article/66-gumroads-fees

**source_type:** help_center

**verification_status:** blocked_url_index_verified

**Date:** Page last updated July 18, 2024 (per search index metadata)

**Notes:** Direct fetch returned authentication wall. Snippet recovered via Google search index attributed to this exact URL.

---

## F-P05

**What:** To receive a payout, creators must have a minimum balance of US $10. Certain countries have higher minimum payout balances: Thailand (600 THB) and Korea (40,000 KRW).

**Verbatim snippet:** "To receive a payout, you must have a minimum balance of US $10. Certain countries have higher minimum payout balances - Thailand (600 THB) and Korea (40,000 KRW)."

**Source:** https://help.gumroad.com/article/13-getting-paid

**source_type:** help_center

**verification_status:** blocked_url_index_verified

**Date:** Page last updated July 23, 2024 (per search index metadata)

**Notes:** Direct fetch returned authentication wall. Snippet recovered via Google search index attributed to this exact URL. One search index variant includes a ⚠️ emoji prefix before "To receive a payout"; this may be present on the original page.

---

## F-P06

**What:** Each payout is for sales made up to the previous Friday UTC. The sale amount sits in the Gumroad balance for at least 7 days before being paid out.

**Verbatim snippet:** "Each payout is for sales made up to the previous Friday UTC. This means that the sale amount sits in your Gumroad balance for at least 7 days before being paid out."

**Source:** https://help.gumroad.com/article/13-getting-paid

**source_type:** help_center

**verification_status:** blocked_url_index_verified

**Date:** Page last updated July 23, 2024 (per search index metadata)

**Notes:** Direct fetch returned authentication wall. Snippet recovered via Google search index attributed to this exact URL. Equivalent language corroborated via search index of articles 269 and 281 attributed to those respective URLs.

---

## F-P07

**What:** PayPal payouts are always processed in USD and usually take 1–3 business days.

**Verbatim snippet:** "PayPal payouts are always processed in USD, and usually in 1-3 business days."

**Source:** https://help.gumroad.com/article/13-getting-paid

**source_type:** help_center

**verification_status:** blocked_url_index_verified

**Date:** Page last updated July 23, 2024 (per search index metadata)

**Notes:** Direct fetch returned authentication wall. Snippet recovered via Google search index attributed to this exact URL.

---

## F-P08

**What:** All currency conversions happen based on the exchange rates at the time of sale, not at the time of the payout. These are typically mid-market rates.

**Verbatim snippet:** "All currency conversions happen based on the exchange rates at the time of sale, not at the time of the payout. These are typically mid-market rates that you can estimate here."

**Source:** https://help.gumroad.com/article/13-getting-paid

**source_type:** help_center

**verification_status:** blocked_url_index_verified

**Date:** Page last updated July 23, 2024 (per search index metadata)

**Notes:** Direct fetch returned authentication wall. Snippet recovered via Google search index attributed to this exact URL. The word "here" is a hyperlink in the original page; destination URL not captured in the search index snippet.

---

## F-P09

**What:** Purchasing power parity (PPP) lets creators set dynamic discounts based on customer location. Discounts range from 20% to 60%, are sourced from the World Bank, and refresh weekly.

**Verbatim snippet:** "Purchasing power parity (PPP) lets Gumroad creators set up dynamic discounts based on where the customer lives, ensuring that the price is proportional to their local currency and cost of living."

**Source:** https://help.gumroad.com/article/327-purchasing-power-parity

**source_type:** help_center

**verification_status:** blocked_url_index_verified

**Date:** Accessed April 2026; page date not visible in search index

**Notes:** Direct fetch returned authentication wall. Snippet recovered via Google search index attributed to this exact URL. A second continuous passage from the same article, confirmed via separate search query, states: "The discounts range from 20% to 60%, are sourced from the World Bank, and refresh weekly." That passage is not concatenated here per contract rules but supports the What field's claim about discount range.

---

## F-P10

**What:** Gumroad handles VAT on behalf of creators for all digital product sales in the EU and the UK, acting as merchant of record for collecting and remitting VAT.

**Verbatim snippet:** "Gumroad handles VAT on behalf of creators for all digital product sales in the EU and the UK. We collect, remit, and even allow buyers to refund VAT without sellers having to lift a finger."

**Source:** https://help.gumroad.com/article/10-dealing-with-vat

**source_type:** help_center

**verification_status:** blocked_url_index_verified

**Date:** Accessed April 2026; page date not visible in search index

**Notes:** Direct fetch returned authentication wall. Snippet recovered via Google search index attributed to this exact URL.

---

# 4. Part 3 — Pattern candidates (sealed)

---

## PC-01

**Candidate:** Gumroad applies different flat fee rates by sales channel — direct sales, Discover web marketplace, and mobile app — without volume-based tiers or graduated thresholds.

**Related Finding IDs:** F-01, F-02, F-P01, F-P02

**Status:** sealed; not validated

---

## PC-02

**Candidate:** Gumroad's Merchant of Record transition shifted indirect tax administration, collection, reporting, and remittance responsibilities from sellers to the platform across all supported jurisdictions.

**Related Finding IDs:** F-04, F-05, F-06, F-08, F-P10

**Status:** sealed; not validated

---

## PC-03

**Candidate:** Gumroad payout mechanics combine a fixed weekly cycle with country-dependent payout methods, minimum thresholds, and currency denominations.

**Related Finding IDs:** F-13, F-P05, F-P06, F-P07, F-P08

**Status:** sealed; not validated

---

# 5. Part 4 — Could not verify / Out-of-scope

---

## F-X01: Complete list of direct deposit countries

**What:** "No data found on the complete list of countries eligible for direct deposit payouts."

**Verbatim snippet:** "n/a — absence finding"

**Source:** Searched help.gumroad.com via Google with queries: `site:help.gumroad.com supported countries`, `site:help.gumroad.com direct deposit countries`; articles 13 and 152 reference a list of direct deposit countries but the full enumeration was not captured in available search index snippets. Direct fetch of both article URLs returned authentication walls.

**source_type:** unknown

**verification_status:** could_not_verify

**Date:** Accessed April 2026

**Notes:** Multiple help center articles reference a list of countries eligible for direct deposit, but the full list was not surfaced in any search index snippet or directly fetchable page.

---

## F-X02: Discover promotional fee specific percentages or tiers

**What:** "No data found on specific percentages or tier levels for the increased Discover promotional fee option beyond the base Discover rate."

**Verbatim snippet:** "n/a — absence finding"

**Source:** Searched help.gumroad.com/article/79-gumroad-discover via Google with query: `site:help.gumroad.com Gumroad Discover fee`; the article mentions creators can agree to "an increased Discover fee" for better product placement, but no specific percentage options or tier levels were captured.

**source_type:** unknown

**verification_status:** could_not_verify

**Date:** Accessed April 2026

**Notes:** The pricing page (F-02) states a flat 30% for Discover sales. The help center article/79 references an "increased Discover fee" option but does not enumerate specific rate tiers in the captured snippets.

---

## F-X03: Fee caps or maximum fee amounts

**What:** "No data found on fee caps or maximum fee amounts for any fee type."

**Verbatim snippet:** "n/a — absence finding"

**Source:** Searched gumroad.com/pricing (directly fetched, full content reviewed), gumroad.com/terms (directly fetched, full content reviewed), and help.gumroad.com/article/66-gumroads-fees (via Google search index). None mentions fee caps or maximum fee amounts.

**source_type:** unknown

**verification_status:** could_not_verify

**Date:** Accessed April 2026

**Notes:** All three primary fee-related sources were reviewed. No cap, ceiling, or maximum amount is stated for any fee type.

---

# 6. Research QA Notes

## Findings forced to Provisional (IDs + reason)

F-P01 through F-P10 — All help.gumroad.com article URLs returned an authentication wall ("Please sign in to continue") on direct fetch. The help center (help.gumroad.com) has been migrated to an AI-powered assistant interface requiring login. All snippets for provisional findings were recovered via Google search index, where each snippet was directly attributed to a specific help.gumroad.com article URL in the search results. Recovery method: targeted `site:help.gumroad.com` queries returning indexed page content tied to exact article URLs.

## Findings degraded to could_not_verify (IDs + reason)

F-X01 — Direct deposit country list referenced in multiple articles but full enumeration not surfaced in search snippets.
F-X02 — Discover promotional fee tier details not available in captured snippets; only the "increased Discover fee" concept was described.
F-X03 — Absence finding; no fee cap information found in any source reviewed.

## Findings degraded due to URL not fixable

None.

## Multi-speaker pages split

N/A — All sources are exclusively Gumroad's platform voice (first-party documentation, pricing pages, Terms of Service, and help center articles).

## Truncated or partial sources

All help.gumroad.com articles (F-P01 through F-P10) were available only as Google search index snippets, not full page text. Full article content may contain additional fee-related information not captured in the indexed snippets. Wayback Machine (web.archive.org) fetches of these URLs were blocked by the fetch tool's permissions restrictions.

## source_type ambiguities

- **gumroad.com/features** classified as `platform_doc` — first-party feature listing page describing platform capabilities.
- **gumroad.com/terms** classified as `policy_page` — Terms of Service Agreement with effective date and legal provisions.
- **gumroad.com/pricing** classified as `pricing_page` — primary pricing page including fee cards and FAQ section.
- **gumroad.com/taxes** was fetched and found to serve identical content to gumroad.com/pricing (same page title "Simple, transparent pricing" and identical body text). No separate findings were created from gumroad.com/taxes to avoid duplication.

## Coverage gaps by expected category

- **SD-03 (Mobile app fee):** Covered only via provisional finding F-P02 from help center article/66. No direct_verified finding from a directly fetched page states the 40% mobile app fee.
- **SD-05 (CC/PayPal fee exclusion):** Covered only via provisional finding F-P01 ("This does not include: Credit card processing PayPal fees"). No direct_verified finding explicitly states whether the $0.50 flat fee on the pricing page (F-01) includes or excludes processing fees.
- **SD-06 (Affiliate fee structure):** Covered only via provisional finding F-P03. No direct_verified finding from directly fetched pages addresses affiliate fee mechanics.
- **SD-09 (Minimum payout threshold):** Covered only via provisional finding F-P05. No direct_verified finding addresses the $10 minimum or country-specific variations.
- **SD-10 (Payout methods by country):** Partial coverage. The pricing page FAQ mentions direct deposit and PayPal vary by country (addressed generally in pricing page content). Full list of direct deposit-eligible countries not captured (F-X01). Stripe Connect availability and country exclusions (Brazil, India, Indonesia, Malaysia, Mexico, Philippines, Thailand) were found in search index snippets from article/13 but not promoted to a formal finding due to snippet boundary uncertainty in the continuous passage.
- **SD-14 (PPP):** Covered via provisional finding F-P09. The discount range (20%–60%) and data source (World Bank) were confirmed in a separate search verification query but appear in a passage separated by a UI element (toggle screenshot) on the original page, requiring the What field claim about the range to be supported by a secondary snippet noted in the Notes field rather than the primary Verbatim.

## Fee discrepancy between pricing page and help center

The pricing page (F-01) states the base direct-sales fee as **"10% + $0.50"** per transaction. The help center fees article (F-P01) states **"a 10% flat fee"** with no mention of a $0.50 per-transaction flat component. Both are reported as found in their respective findings. This discrepancy is noted here for transparency; no reconciliation or interpretation was applied per contract rules.

## Cases where input could not be decomposed without interpretation

None.