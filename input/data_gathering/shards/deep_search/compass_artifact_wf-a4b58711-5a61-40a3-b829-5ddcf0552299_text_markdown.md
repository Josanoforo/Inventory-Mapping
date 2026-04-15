# Data Gathering: Patreon × D1 — Platform mechanics and fee structure

---

## Search decomposition

- SD-01: Current standard platform fee for creators publishing after August 4, 2025
- SD-02: Legacy platform plan names and fee percentages (Founders, Pro/Lite, Premium)
- SD-03: Payment processing fees by currency (standard and micropayment rates)
- SD-04: Currency conversion fee rate and conditions
- SD-05: iOS App Store fee (Apple in-app purchases) and Patreon's treatment
- SD-06: US iOS users and Epic v. Apple exemption from IAP
- SD-07: Payout methods available by country
- SD-08: Payout fees by method and currency (local bank, USD bank, PayPal, Payoneer)
- SD-09: Payout minimums by method
- SD-10: Payout delivery timelines and pending periods (Web/Android vs. iOS)
- SD-11: Automatic payout schedule and payout frequency limits
- SD-12: Payout hold policies (new creator, method changes)
- SD-13: Refund policy — fan refund window and creator refund window
- SD-14: Refund fee policy
- SD-15: Tax handling on creator fees (VAT/GST/sales tax)
- SD-16: One-time purchase (Commerce) fee structure
- SD-17: Platform fee calculation basis (inclusion/exclusion of sales tax)
- SD-18: Subscription billing migration deadline

---

## Part 1 — Clean findings (direct_verified)

None. All Patreon Help Center pages (support.patreon.com) returned HTTP 403 Forbidden on direct fetch. All patreon.com seed URLs also blocked direct automated access. No direct_verified findings could be produced for this shard.

---

## Part 2 — Provisional findings (blocked_url_index_verified)

### F-P01
What: Patreon's standard plan platform fee is 10% of successfully processed payments; legacy plan creators may pay 5%, 8%, or 11%.
Verbatim snippet: "Platform fee – A percentage of successfully processed payments. This depends on your plan: creators on the standard plan pay 10%, while legacy plan creators may pay 5%, 8% or 11%. You can check which plan you're on in your Account Settings"
Source: https://support.patreon.com/hc/en-us/articles/22581195376909-Creator-fees-FAQ
source_type: help_center
verification_status: blocked_url_index_verified
Date: Updated August 05, 2025 16:00 (visible in search index)
Notes: Retrieval method: Google search index snippet for this exact URL. Direct fetch returned 403. The three legacy percentages (5%, 8%, 11%) are listed without plan-name mapping in this source.

### F-P02
What: The standard 10% platform fee policy is effective for creators who publish their creator page after August 4, 2025; creators who published on or before that date keep their existing platform pricing.
Verbatim snippet: "This policy is effective for creators who publish their creator page after August 4, 2025. If you are a creator who publishes your page on or before August 4, 2025, you will keep your existing platform pricing — this new plan will not apply to you, and you will not see a change in price as a result of this change."
Source: https://support.patreon.com/hc/en-us/articles/36426991446797-A-standard-platform-fee-for-new-creators-effective-after-August-4-2025
source_type: help_center
verification_status: blocked_url_index_verified
Date: Updated January 28, 2026 15:05 (visible in search index)
Notes: Retrieval method: Google search index snippet for this exact URL. Direct fetch returned 403.

### F-P03
What: Creators who joined Patreon before May 2019 were placed on a discounted founders-only plan at 5% platform fee.
Verbatim snippet: "In May 2019, we first introduced new creator plans and fees. Creators who joined before this date were placed on a discounted founders-only plan, 5%, that gave them the same features as when they first joined without any additional costs."
Source: https://support.patreon.com/hc/en-us/articles/9943809610253-What-is-the-Founders-plan
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated in search index
Notes: Retrieval method: Google search index snippet for this exact URL. Direct fetch returned 403.

### F-P04
What: Founders plan eligibility requires joining Patreon before May 7, 2019, and not having upgraded plans, changed currency, or had the creator page unpublished.
Verbatim snippet: "You're on the Founders plan if you joined Patreon before May 7, 2019, and haven't upgraded your plan in the past, changed your currency, or had your creator page unpublished by you or by Patreon for any reason."
Source: https://support.patreon.com/hc/en-us/articles/11111747095181-Creator-fees-overview
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated in search index
Notes: Retrieval method: Google search index snippet for this exact URL. Direct fetch returned 403.

### F-P05
What: Patreon's standard payment processing fee varies by currency; the USD standard rate is given as an example of 2.9% + $0.30.
Verbatim snippet: [Stated in layout: "Payment processing fee Varies by currency (e.g., 2.9% + $0.30 USD) standard payment process rate"]
Source: https://support.patreon.com/hc/en-us/articles/11111747095181-Creator-fees-overview
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated in search index
Notes: Retrieval method: Google search index snippet for this exact URL. Direct fetch returned 403. The full "Processing rates by currency" table referenced on this page could not be retrieved via search snippets. The 2.9% + $0.30 is explicitly labeled "e.g." — it is an example, not the only rate.

### F-P06
What: A 2.5% currency conversion fee applies when a fan pays in a currency different from the creator's payout currency, calculated on the full processed amount including tax.
Verbatim snippet: "A 2.5% currency conversion fee applies when a fan pays in a currency that's different from your payout currency. This fee is calculated on the full processed amount, including tax"
Source: https://support.patreon.com/hc/en-us/articles/11111747095181-Creator-fees-overview
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated in search index
Notes: Retrieval method: Google search index snippet for this exact URL. Direct fetch returned 403.

### F-P07
What: No currency conversion fee is applied if a paid member pays in the creator's payout currency.
Verbatim snippet: "If a paid member pays you in your payout currency, then there is no currency conversion fee applied."
Source: https://support.patreon.com/hc/en-us/articles/11111747095181-Creator-fees-overview
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated in search index
Notes: Retrieval method: Google search index snippet for this exact URL. Direct fetch returned 403.

### F-P08
What: Apple takes a 30% service fee for purchases through Apple's in-app purchase system within the Patreon iOS app; this fee replaces Patreon's standard payment processing fee for that transaction.
Verbatim snippet: "App Store fee (iOS purchases) – If a member makes a purchase through Apple's in-app purchase system within the Patreon iOS app, Apple takes a 30% service fee. This fee replaces Patreon's standard payment processing fee for that transaction"
Source: https://support.patreon.com/hc/en-us/articles/22581195376909-Creator-fees-FAQ
source_type: help_center
verification_status: blocked_url_index_verified
Date: Updated August 05, 2025 16:00 (visible in search index)
Notes: Retrieval method: Google search index snippet for this exact URL. Direct fetch returned 403.

### F-P09
What: iOS in-app purchases are subject to Patreon's 10% standard platform fee and currency conversion fees (if applicable), applied to the sale amount before sales tax; Patreon does not charge a payment processing fee on iOS in-app purchase transactions.
Verbatim snippet: "As with all one-time purchases, successfully processed sales on iOS in-app purchases are also subject to Patreon's 10% standard platform fee and currency conversion fees (if applicable), applied to the sale amount before sales tax. Patreon does not charge a payment processing fee on iOS in-app purchase transactions."
Source: https://support.patreon.com/hc/en-us/articles/20009513905933-How-iOS-in-app-payment-works-for-one-time-purchases
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated in search index
Notes: Retrieval method: Google search index snippet for this exact URL. Direct fetch returned 403. Snippet references "10% standard platform fee" — this applies to creators on the standard plan; legacy plan creators may have different platform fees.

### F-P10
What: iOS users in the United States do not have to use Apple's in-app purchase flow; they can complete purchases through Patreon's mobile web checkout and are not subject to the 30% IAP fee, reflecting the Epic v. Apple ruling.
Verbatim snippet: "U.S. customers Due to ongoing legal developments, iOS users in the United States do not have to use Apple's in-app purchase (IAP) flow. Instead, they have the option to complete purchases directly through Patreon's mobile web checkout and are not subject to the 30% IAP fee. This experience reflects the outcome of the Epic v. Apple ruling, which prohibits Apple from blocking alternative payment methods"
Source: https://support.patreon.com/hc/en-us/articles/36426991446797-A-standard-platform-fee-for-new-creators-effective-after-August-4-2025
source_type: help_center
verification_status: blocked_url_index_verified
Date: Updated January 28, 2026 15:05 (visible in search index)
Notes: Retrieval method: Google search index snippet for this exact URL. Direct fetch returned 403. "U.S. customers" appears to be a section heading followed by body text in the original page layout.

### F-P11
What: The platform fee is calculated based on the payment amount, excluding sales tax.
Verbatim snippet: "The platform fee covers the use of Patreon's platform and is a percentage of successfully processed membership and one-time purchases. We calculate your platform fee based on the payment amount, excluding sales tax."
Source: https://support.patreon.com/hc/en-us/articles/11111747095181-Creator-fees-overview
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated in search index
Notes: Retrieval method: Google search index snippet for this exact URL. Direct fetch returned 403.

### F-P12
What: One-time purchases are subject to the same fees as membership payments: platform fee between 5% and 12% of successfully processed sales + applicable taxes depending on platform plan, and payment processing fee varies by currency.
Verbatim snippet: [Stated in layout: "It's free to list your work for sale on Patreon (e.g., digital products, posts, and collections). One-time purchases are subject to the same fees as membership payments: Platform fee Between 5% and 12% of successfully processed sales + applicable taxes, depending on your platform plan · Payment processing fee Varies by currency (e.g., 2.9% + $0.30 USD) standard payment process rate"]
Source: https://support.patreon.com/hc/en-us/articles/36426991446797-A-standard-platform-fee-for-new-creators-effective-after-August-4-2025
source_type: help_center
verification_status: blocked_url_index_verified
Date: Updated January 28, 2026 15:05 (visible in search index)
Notes: Retrieval method: Google search index snippet for this exact URL. Direct fetch returned 403. Layout uses bullet/card formatting on original page. "Between 5% and 12%" reflects the range across all current plans (Founders 5%, Pro 8%, Standard 10%, Premium 11% or 12%).

### F-P13
What: US-based creators can use bank transfer processed by Stripe; creators outside the US use bank transfer processed by Payoneer.
Verbatim snippet: "Depending on your payout country, you can choose from one of the following options: Bank transfer (processed by Stripe) – available for creators based in the U.S · Bank transfer (processed by Payoneer) – available to creators who reside outside of the U.S — please see full country eligibility list here"
Source: https://support.patreon.com/hc/en-us/articles/208656246-How-payouts-work
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated in search index
Notes: Retrieval method: Google search index snippet for this exact URL. Direct fetch returned 403. PayPal and Payoneer Wallet are also available as payout options per other parts of this page.

### F-P14
What: For non-US creators using local bank transfer, the payout fee is a small flat fee (e.g., about $0.50 local equivalent per payout, varies by currency), with a minimum payout of $10 or local equivalent.
Verbatim snippet: [Stated in layout: "Fees: A small flat fee (e.g., about $0.50 local equivalent per payout, varies by currency). Minimum payout of $10 or local equivalent."]
Source: https://support.patreon.com/hc/en-us/articles/39694936541965-Payouts-guide-for-creators-outside-of-the-US
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated in search index
Notes: Retrieval method: Google search index snippet for this exact URL. Direct fetch returned 403. The ~$0.50 is stated as an example ("e.g., about") — exact fee varies by currency. The full payout fee table by currency could not be retrieved.

### F-P15
What: For non-US creators using USD bank transfer (cross-currency to local bank), the payout fee is 1.55% of payout amount + $0.25 per payout, with no additional currency conversion fee, and a minimum payout of $10; Patreon handles the conversion from USD to local currency.
Verbatim snippet: [Stated in layout: "Fees: 1.55% of payout amount + $0.25 per payout. No additional currency conversion fee is applied. Minimum payout of $10. Conversion: Patreon handles the conversion from USD → local currency before sending to your bank."]
Source: https://support.patreon.com/hc/en-us/articles/39694936541965-Payouts-guide-for-creators-outside-of-the-US
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated in search index
Notes: Retrieval method: Google search index snippet for this exact URL. Direct fetch returned 403.

### F-P16
What: For non-US creators paying out USD to a USD bank account, the payout fee is $0.50 per payout with no currency conversion at payout time.
Verbatim snippet: [Stated in layout: "Fees: $0.50 per payout. Conversion: No additional currency conversion happens at payout time, since the transfer is from USD to a USD bank account."]
Source: https://support.patreon.com/hc/en-us/articles/39694936541965-Payouts-guide-for-creators-outside-of-the-US
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated in search index
Notes: Retrieval method: Google search index snippet for this exact URL. Direct fetch returned 403.

### F-P17
What: When enabled, automatic payouts are initiated on the 5th of each month as long as the creator has a positive balance.
Verbatim snippet: "When enabled, automatic payouts are initiated on the 5th of each month as long as you have a positive balance. You can enable or disable automatic payouts from your Payouts page."
Source: https://support.patreon.com/hc/en-us/articles/208656246-How-payouts-work
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated in search index
Notes: Retrieval method: Google search index snippet for this exact URL. Direct fetch returned 403.

### F-P18
What: Once a payout is initiated, it typically takes 1–5 days for funds to appear in the creator's personal account.
Verbatim snippet: "Once a payout is initiated, it typically takes 1-5 days for the funds to appear in your personal account."
Source: https://support.patreon.com/hc/en-us/articles/208656246-How-payouts-work
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated in search index
Notes: Retrieval method: Google search index snippet for this exact URL. Direct fetch returned 403.

### F-P19
What: New creators on Patreon have a 5-day payout hold from the date of adding their first payout method or from the date of receiving their first payment.
Verbatim snippet: "If you are a brand new creator on Patreon, please note that there will be a 5-day hold in place from the date of adding your first payout method or from the date of receiving your first payment."
Source: https://support.patreon.com/hc/en-us/articles/208656246-How-payouts-work
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated in search index
Notes: Retrieval method: Google search index snippet for this exact URL. Direct fetch returned 403.

### F-P20
What: Funds from Commerce on Web and Android are pending for up to 7 days; funds from iOS in-app purchases remain pending for up to 75 days, accounting for Apple's processing time.
Verbatim snippet: "Funds from products purchased through Commerce on Web and Android will appear as pending for up to 7 days before they can be withdrawn from your balance. Funds from product sales made via iOS in-app purchases will remain pending for up to 75 days before they will be available for payout, accounting for the time Apple requires to process and confirm the funds."
Source: https://support.patreon.com/hc/en-us/articles/208656246-How-payouts-work
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated in search index
Notes: Retrieval method: Google search index snippet for this exact URL. Direct fetch returned 403.

### F-P21
What: Creators can payout once every 24 hours; automatic payouts count as one payout; Patreon may cap monthly payouts if costs and patterns change.
Verbatim snippet: "You can payout once every 24 hours. If you have automatic payouts turned on, this counts as one payout. However, we may cap the number of payouts available per month if payout costs and patterns change dramatically in the future."
Source: https://support.patreon.com/hc/en-us/articles/203913499-Paying-out-your-earnings
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated in search index
Notes: Retrieval method: Google search index snippet for this exact URL. Direct fetch returned 403.

### F-P22
What: Fans must request a refund within 60 days of the original payment via their Billing History; outside this window they are directed to Patreon Product Support.
Verbatim snippet: "Fans can go to their Billing History and select the payment they'd like refunded. They must request a refund within 60 days of the original payment. If they are outside this window, they will be directed to contact Patreon Product Support for further assistance."
Source: https://support.patreon.com/hc/en-us/articles/205032045-Patreon-s-refund-policy
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated in search index
Notes: Retrieval method: Google search index snippet for this exact URL. Direct fetch returned 403.

### F-P23
What: There are no additional fees for refunding; the creator gives back the amount originally received and Patreon returns its share and any sales tax/VAT to the member/customer.
Verbatim snippet: "There are no additional fees for refunding. When you initiate a refund, you only give back the amount you originally received, and we return any remaining amount retained by Patreon to the paid member/customer, including Patreon's share and any sales tax/VAT."
Source: https://support.patreon.com/hc/en-us/articles/22581195376909-Creator-fees-FAQ
source_type: help_center
verification_status: blocked_url_index_verified
Date: Updated August 05, 2025 16:00 (visible in search index)
Notes: Retrieval method: Google search index snippet for this exact URL. Direct fetch returned 403.

### F-P24
What: Creators can refund a member's three most recent payments from Relationship Manager, only within 90 days of the original processing date, as long as the creator has an account balance to cover the refund.
Verbatim snippet: "You can refund a member's three most recent payments from Relationship Manager, as long as you have an account balance to cover the refunded amount. You can only refund a charge within 90 days of the original processing date."
Source: https://support.patreon.com/hc/en-us/articles/8779192853261-Subscription-Billing-FAQ
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated in search index
Notes: Retrieval method: Google search index snippet for this exact URL. Direct fetch returned 403.

### F-P25
What: Patreon may be required to apply sales tax/VAT to the service fees it charges creators, based on location, business status, local laws, intermediary platform treatment, type of service, and applicable exemptions.
Verbatim snippet: "Depending on your location and business status, Patreon may be required to apply sales tax/VAT to the service fees it charges creators. These tax obligations are based on local laws, including how intermediary platforms are treated, the type of service, and whether any exemptions apply in your jurisdiction."
Source: https://support.patreon.com/hc/en-us/articles/16477355698957-Taxes-on-creator-fees
source_type: help_center
verification_status: blocked_url_index_verified
Date: Updated March 03, 2026 20:41 (visible in search index)
Notes: Retrieval method: Google search index snippet for this exact URL. Direct fetch returned 403.

### F-P26
What: In certain countries (South Africa, Switzerland, Indonesia, Malaysia) Patreon will generally charge VAT irrespective of the creator's VAT ID registration status.
Verbatim snippet: "Also, note that in certain countries (e.g., South Africa, Switzerland, Indonesia, Malaysia) Patreon will generally charge VAT irrespective of your VAT ID registration status."
Source: https://support.patreon.com/hc/en-us/articles/16477355698957-Taxes-on-creator-fees
source_type: help_center
verification_status: blocked_url_index_verified
Date: Updated March 03, 2026 20:41 (visible in search index)
Notes: Retrieval method: Google search index snippet for this exact URL. Direct fetch returned 403. Country list uses "e.g." qualifier — may not be exhaustive.

### F-P27
What: All creators still using legacy billing must switch to subscription billing by November 1, 2026.
Verbatim snippet: "All creators still using legacy billing will need to switch to subscription billing by November 1, 2026."
Source: https://support.patreon.com/hc/en-us/articles/8779192853261-Subscription-Billing-FAQ
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated in search index
Notes: Retrieval method: Google search index snippet for this exact URL. Direct fetch returned 403.

### F-P28
What: Founders who have changed their payout currency retain their 5% platform fee but are subject to the standard processing rates rather than the Founders processing rates.
Verbatim snippet: "Founders who have changed their payout currency remain on the Founders plan and retain their 5% platform fee, but are subject to the standard processing rates below rather than the Founders processing rates."
Source: https://support.patreon.com/hc/en-us/articles/11111747095181-Creator-fees-overview
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated in search index
Notes: Retrieval method: Google search index snippet for this exact URL. Direct fetch returned 403.

---

## Part 3 — Pattern candidates (sealed)

### PC-01
Pattern Candidate ID: PC-01
Candidate statement: Patreon's fee structure consists of multiple layered components — platform fee, payment processing fee, currency conversion fee, payout fee, and applicable taxes — each applied at a different stage of the payment-to-payout pipeline, with rates varying by plan type, payment method, currency, and geographic location.
Related Finding IDs: F-P01, F-P05, F-P06, F-P08, F-P11, F-P14, F-P15, F-P25
Status: sealed; not validated

### PC-02
Pattern Candidate ID: PC-02
Candidate statement: Patreon operates a two-tier pricing regime in which creators who published before August 4, 2025 retain legacy plan rates (5%, 8%, or 11%) and Founders-specific processing rates, while all creators publishing after that date are placed on the standardized 10% plan with standardized processing rates.
Related Finding IDs: F-P01, F-P02, F-P03, F-P04, F-P28
Status: sealed; not validated

### PC-03
Pattern Candidate ID: PC-03
Candidate statement: Apple iOS in-app purchases introduce a distinct fee and fund-availability regime — 30% Apple fee replacing Patreon processing fees, up to 75-day pending period, separate refund flow through Apple — with US iOS users exempted from the IAP requirement due to the Epic v. Apple ruling.
Related Finding IDs: F-P08, F-P09, F-P10, F-P20
Status: sealed; not validated

---

## Part 4 — Could not verify / Out-of-scope

### F-X01: Complete payment processing rates by currency table
What: The Creator fees overview page references a "Processing rates by currency" table with specific percentage + flat-fee rates for each supported currency (standard and micropayment rates). The full table could not be retrieved.
Verbatim snippet: n/a — table content inaccessible
Source: https://support.patreon.com/hc/en-us/articles/11111747095181-Creator-fees-overview
source_type: help_center
verification_status: could_not_verify
Date: Accessed April 2026
Notes: Direct fetch returned 403. Search engine index snippets did not reproduce the full rates table. Only the USD example (2.9% + $0.30) was recoverable from running text. Rates for EUR, GBP, CAD, AUD, and other currencies remain unverified. Micropayment rate thresholds ($3 USD / €3 / £3 referenced in a separate legacy article) could not be confirmed as current.

### F-X02: US Stripe bank transfer payout fee
What: No specific payout fee amount for US-based creators using Stripe bank transfer was found in recoverable search snippets.
Verbatim snippet: n/a — absence finding
Source: https://support.patreon.com/hc/en-us/articles/11111747095181-Creator-fees-overview (references payout fee tables) and https://support.patreon.com/hc/en-us/articles/208656246-How-payouts-work (references Stripe for US but no fee amount)
source_type: help_center
verification_status: could_not_verify
Date: Accessed April 2026
Notes: Both pages reference payout fee tables that were embedded in the original page content but could not be retrieved from search index snippets. The How payouts work page states Stripe bank transfer is available for US creators but does not state the fee in recoverable text.

### F-X03: PayPal and Payoneer Wallet payout fees by currency
What: The Creator fees overview and Payouts guide reference payout fee tables for PayPal and Payoneer Wallet options. Specific fee amounts per currency could not be retrieved.
Verbatim snippet: n/a — table content inaccessible
Source: https://support.patreon.com/hc/en-us/articles/11111747095181-Creator-fees-overview and https://support.patreon.com/hc/en-us/articles/39694936541965-Payouts-guide-for-creators-outside-of-the-US
source_type: help_center
verification_status: could_not_verify
Date: Accessed April 2026
Notes: Both pages state payout fee tables exist for PayPal and Payoneer but the tables could not be retrieved from search index snippets. Recoverable text states "PayPal and Payoneer may charge extra fees for currency conversion or withdrawal, which vary by region and are subject to change at any time without notice."

### F-X04: Premium plan current platform fee rate (11% vs. 12% discrepancy)
What: The Creator fees FAQ (updated August 2025) states legacy plan rates as "5%, 8% or 11%" while the Patreon Creator Plans article and Lite deprecation FAQ state Premium plan fee as 12%. The current Premium plan rate could not be definitively determined from a single current-state source.
Verbatim snippet: n/a — conflicting information across sources
Source: https://support.patreon.com/hc/en-us/articles/22581195376909-Creator-fees-FAQ (states "11%") and https://support.patreon.com/hc/en-us/articles/360024952552-Patreon-Creator-Plans (states "12%")
source_type: help_center
verification_status: could_not_verify
Date: Accessed April 2026
Notes: The Creator fees FAQ (updated August 2025) is the more recently updated source and lists 11%. The Creator Plans article (date unknown, may be from 2019) lists 12% for Premium. Unable to determine which is current without direct page access. Per protocol, cannot synthesize across sources.

### F-X05: patreon.com/pricing page content
What: No data could be gathered from the main patreon.com/pricing page.
Verbatim snippet: n/a — absence finding
Source: https://www.patreon.com/pricing
source_type: pricing_page
verification_status: could_not_verify
Date: Accessed April 2026
Notes: Direct fetch returned a permissions error. Web search did not return indexed content specifically from this URL. The page may use client-side rendering that prevents indexing of fee details.

---

## Research QA Notes

- **Findings forced to Provisional:** F-P01 through F-P28 — all 28 findings. Reason: all Patreon Help Center pages (support.patreon.com) returned HTTP 403 Forbidden on direct automated fetch. Content was recovered exclusively via Google search engine index snippets attributed to the exact source URLs. This satisfies the blocked_url_index_verified criteria (exact URL fixed, direct fetch failed, snippet retrieved via search index of the same URL).
- **Findings degraded to could_not_verify:** F-X01 (processing rate table inaccessible), F-X02 (US payout fee amount not found in snippets), F-X03 (PayPal/Payoneer payout fee tables inaccessible), F-X04 (conflicting rates across sources), F-X05 (pricing page content inaccessible).
- **Findings degraded due to URL not fixable:** None. All URLs are fixed and verified as Patreon Help Center articles.
- **Multi-speaker pages split:** None applicable. All sources are Patreon's own help center articles in Patreon's editorial voice.
- **Truncated or partial sources:** All sources are partial — search engine index snippets only capture portions of each page. Embedded tables (processing rates by currency, payout fees by currency/method) were not captured in any search snippet. This is the primary data gap for this shard.
- **source_type ambiguities:** None. All support.patreon.com articles are clearly help_center. The patreon.com/pricing page (F-X05) would be pricing_page if accessible.
- **Coverage gaps where findings expected but not found:**
  - Complete payment processing rates by currency (standard rates for EUR, GBP, CAD, AUD, etc.)
  - Micropayment processing rate thresholds and amounts (current state)
  - US Stripe payout fee amount
  - PayPal payout fee amounts per currency
  - Payoneer Wallet payout fee amounts per currency
  - Payoneer global bank transfer and wire transfer fee amounts
  - Full list of supported payout currencies
  - Full list of supported payout countries
  - Legacy Pro plan and Premium plan fee rates with plan-name-to-percentage mapping from a single current-state source
  - patreon.com/pricing page content
- **Cases where input could not be decomposed without interpretation:** None.
- **0 direct_verified findings:** This is an unusual shape for the shard. The entire Patreon Help Center (support.patreon.com) blocks automated HTTP requests with 403 responses. All 28 findings were recovered from Google search index snippets for the exact source URLs. The search snippets are generally reliable representations of page content but may have minor formatting differences from the original pages. No findings were elevated to direct_verified to avoid inflating the clean count.