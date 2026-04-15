Search decomposition

- SD-01: Hotmart General Payment Policy (hotmart.com/en/legal/payments-policy) → entity routing by country/currency, MoR/commercial-agent model, Hotpay currency rules, FX conversion mechanics, license fees by currency, cash advance for non-Brazil, Payment Account restrictions
- SD-02: Hotmart General Terms of Use (hotmart.com/en/legal/terms-of-use) → bank account country-of-residence rule, OFAC sanctions/geographic restrictions, fund retention periods Brazil vs non-Brazil, co-production limitations
- SD-03: Hotmart General Purchase Terms (hotmart.com/en/legal/purchase-terms) → entity structure reiteration, Mexico reseller model, EU VAT handling, event tax by country
- SD-04: Hotmart Help Center: commission currency rules (help.hotmart.com/en/article/360015794612) → four commission currencies (BRL, USD, EUR, GBP), fallback to USD, Brazil auto-conversion note
- SD-05: Hotmart Help Center: withdrawal methods (help.hotmart.com/en/article/216440207) → minimums, fee tables, Colombia COP option, Wise account restrictions, Argentina BCRA regulation, Payoneer registration, auto monthly transfer since Feb 2024
- SD-06: Hotmart Help Center: international purchase process (help.hotmart.com/en/article/213026287) → buyer-side currency conversion, credit-card-only default, local payment options (OXXO, Baloto), supported display currencies (MXN, PEN)
- SD-07: Hotmart Help Center: tax rules by region (help.hotmart.com/en/article/28274925159437) → tax-inclusive vs tax-exclusive pricing, Hotmart-managed vs creator-managed tax collection
- SD-08: Hotmart Help Center: installment payments (help.hotmart.com/en/article/4404509205005) → installments for Chile, Peru, Mexico, Colombia, Brazil with currency-specific minimums
- SD-09: Hotmart Help Center: buyer payment methods by country (help.hotmart.com/en/article/25588460435085) → LatAm-specific methods (Mercado Pago, OXXO, SPEI, Efecty, PSE, Nequi, Pago Efectivo, Yape, Sencillito, Servipag); cross-border payment method limitations for non-Brazil creators selling to Brazil buyers
- SD-10: Hotmart Card Policies (hotmart.com/en/legal/hotmart-card-policies) → USD virtual card for non-Brazil users, Colombia-specific Pomelo payment institution
- SD-11: Reddit r/hotmart → English-language cross-border user experiences; RESULT: no qualifying English-language results found across 14 query variations; community is overwhelmingly Portuguese
- SD-12: Third-party English-language blogs, articles, reviews → Hotmart cross-border mechanics, seller experience reports, platform comparisons (restofworld.org, way2earning.com, payoneer.com, capterra.com, monetizedfuture.com, prnewswire.com)
- SD-13: Payoneer partner documentation → Hotmart as mass-payout partner for LatAm
- SD-14: English-language YouTube → Hotmart cross-border tutorials; RESULT: no relevant English-language content found
- SD-15: Hotmart pricing page (hotmart.com/en/pricing) → cross-border fee detail; RESULT: marketing page without specific cross-border fee tables

---

Part 1 - Clean findings (direct_verified)

### F-01
What: Hotpay processes transactions in three currencies: Brazilian Real (BRL) between users both domiciled in Brazil, Euro (EUR) between users both domiciled in the EU, and US Dollars (USD) as the purchase currency between all other users.
Verbatim snippet: "Hotmart makes payment transactions on Hotpay with the following currencies: (a) with purchase currency in Brazilian Real (BRL), between Users that declare that both are domiciled in Brazil; (b) with purchase currency in Euro (EUR), between Users that declare that both are domiciled in the European Union; or, (c) in American dollars (USD) as the purchase currency, between any other Users."
Source: https://hotmart.com/en/legal/payments-policy
source_type: policy_page
verification_status: direct_verified
Date: November 28, 2025 (policy version date)
Notes: Verified via direct fetch by two independent subagents. Section 4.6 of Payments Policy. All LatAm↔US transactions settle in USD under rule (c).

### F-02
What: For individual Creators residing in Mexico, Hotmart, acting as a reseller, will be responsible for issuing invoices to the Buyers, as well as issuing a self-invoice to the Creators; such Creators remain responsible for all other tax obligations in their country of residence.
Verbatim snippet: "For individual Creators residing in Mexico, Hotmart, acting as a reseller, will be responsible for issuing invoices to the Buyers, as well as issuing a self-invoice to the Creators. Notwithstanding the foregoing, such Creators remain responsible for all other tax obligations in their country of residence."
Source: https://hotmart.com/en/legal/payments-policy
source_type: policy_page
verification_status: direct_verified
Date: November 28, 2025 (policy version date)
Notes: Verified via direct fetch by two independent subagents. Section 1.7.2.1. Mexico is the only LatAm country where Hotmart acts as reseller rather than commercial agent.

### F-03
What: When a user contracts with Hotmart B.V., Hotmart acts as a commercial agent on behalf of the Creators, except for individual Creators residing in Mexico, in which case Hotmart acts as a reseller.
Verbatim snippet: "If the User contracts with Hotmart B.V., Hotmart will act as a commercial agent on behalf of the Creators, except for individual Creators residing in Mexico, in which case Hotmart will act as a reseller."
Source: https://hotmart.com/en/legal/payments-policy
source_type: policy_page
verification_status: direct_verified
Date: November 28, 2025 (policy version date)
Notes: Verified via direct fetch by two independent subagents. Section C. All non-Brazil, non-US-domestic transactions are processed by Hotmart BV (Netherlands entity). This determines MoR vs agent role for LatAm↔US flows.

### F-04
What: Brazil-domiciled users who make sales outside Brazilian territory and generate a balance in Dollars receive automatic daily transfers of that Dollar balance to their Payment Account, converted to Reais, via a third-party Payment Services Provider.
Verbatim snippet: "For Users who declare their domicile in Brazil, who make sales outside Brazilian territory and who generate a balance in Dollars, Hotmart together with its Third Party Partner (Payment Services Provider) will carry out automatic daily transfers of this available balance in Dollars to the Payment Account and issue electronic currency held by the User at SCD in Reais"
Source: https://hotmart.com/en/legal/payments-policy
source_type: policy_page
verification_status: direct_verified
Date: November 28, 2025 (policy version date)
Notes: Verified via direct fetch by two independent subagents. Section 4.7.1.1. Direction: Brazil seller → international buyer. Brazil sellers cannot hold USD balances; daily forced conversion USD→BRL.

### F-05
What: Commissions in Euros or US Dollars can be withdrawn via HotPay International by transfer directly to the registered bank account, with a minimum withdrawal amount of US$ 50.00 or € 50.00 plus fees.
Verbatim snippet: "You can withdraw commissions in Euros or US Dollars normally through HotPay International. This option allows you to receive the money by transfer directly to the registered bank account. The procedure for withdrawing these commissions is the same as indicated above, and the minimum withdrawal amount is US$ 50.00 or € 50.00 + fees."
Source: https://help.hotmart.com/en/article/216440207/how-to-withdraw-my-commission-
source_type: help_center
verification_status: direct_verified
Date: accessed April 14, 2026
Notes: Verified via direct fetch by two independent subagents. Applies to all non-BRL commission withdrawals for international sellers.

### F-06
What: Users with Colombia as registered account country can withdraw sales in US Dollars to Colombian Pesos (COP) by registering a Colombian bank account on the platform.
Verbatim snippet: "If the country registered in your account is Colombia, you can withdraw sales in US Dollars to Colombian Pesos (COP). To do this, you need to register a Colombian bank account on the platform."
Source: https://help.hotmart.com/en/article/216440207/how-to-withdraw-my-commission-
source_type: help_center
verification_status: direct_verified
Date: accessed April 14, 2026
Notes: Verified via direct fetch by two independent subagents. Colombia is the only non-Brazil LatAm country with an explicitly documented local-currency withdrawal option in this source.

### F-07
What: Wise personal accounts require the SWIFT code to match the country of registration, so producers located outside the U.S. and the EU cannot use Wise personal accounts for withdrawals; Wise business accounts outside Brazil can use SWIFT codes from other countries and can be used for payouts.
Verbatim snippet: "Wise account: Wise uses SWIFT codes tied to banks in the United States and the European Union. For personal accounts, the SWIFT must match the country of registration; therefore, producers located outside the U.S. and the EU cannot use Wise accounts for withdrawals. For business accounts outside Brazil, the SWIFT may belong to other countries; therefore, a Wise business account can be used for payouts."
Source: https://help.hotmart.com/en/article/216440207/how-to-withdraw-my-commission-
source_type: help_center
verification_status: direct_verified
Date: accessed April 14, 2026
Notes: Verified via direct fetch by two independent subagents. LatAm sellers (outside US/EU) cannot use personal Wise; must use Wise business account or alternative methods (Payoneer, local bank where supported).

### F-08
What: Due to new regulations from the Central Bank of Argentina (BCRA), there has been a standardization of a fee for payments with conversions of purchases in Argentine Pesos (ARS) to offers in US Dollars (USD) or conversions of commissions in US Dollars (USD) to products offered in Argentine Pesos (ARS).
Verbatim snippet: "Due to new regulations from the Central Bank of Argentina (BCRA), there has been a standardization of a fee for payments with conversions of purchases in Argentine Pesos (ARS) to offers in US Dollars (USD) or conversions of commissions in US Dollars (USD) to products offered in Argentine Pesos (ARS)."
Source: https://help.hotmart.com/en/article/216440207/how-to-withdraw-my-commission-
source_type: help_center
verification_status: direct_verified
Date: accessed April 14, 2026
Notes: Verified via direct fetch by two independent subagents. Fee amount not specified in source. Argentina-specific regulatory burden on ARS↔USD cross-border flows.

### F-09
What: Users who do not live or pay taxes in Brazil can withdraw their balance directly to their local bank account in the currency of their country, as long as it is US Dollars, Euros, or Pounds.
Verbatim snippet: "If you don't live or pay taxes in Brazil, you can withdraw your balance directly to your local bank account in the currency of your country (as long as it is US Dollars, Euros, or Pounds)."
Source: https://help.hotmart.com/en/article/360015794612/in-which-currency-will-my-commission-be-paid-
source_type: help_center
verification_status: direct_verified
Date: accessed April 14, 2026
Notes: Verified via direct fetch by two independent subagents. LatAm sellers whose local currency is not USD, EUR, or GBP must use other withdrawal methods (e.g., Payoneer or local bank where supported such as Colombia COP).

### F-10
What: Since February 2024, Hotmart has been automatically transferring all sales commissions available for withdrawal in currencies other than Brazilian Real (BRL) on a monthly basis.
Verbatim snippet: "Since February 2024, we have been automatically transferring all sales commissions available for withdrawal in currencies other than Brazilian Real (BRL) on a monthly basis."
Source: https://help.hotmart.com/en/article/216440207/how-to-withdraw-my-commission-
source_type: help_center
verification_status: direct_verified
Date: accessed April 14, 2026
Notes: Verified via direct fetch by two independent subagents. Applies to all international (non-BRL) commissions from cross-border sales. On-demand withdrawal via Payoneer also available in addition to the automatic monthly transfer.

### F-11
What: Creators who live in other countries have limited payment methods available to Brazilian Buyers — only credit card and PIX — because the commission will be paid in dollars and payment via bank slip and bank transfer does not convert on the platform.
Verbatim snippet: "Creators who live in other countries have limited payment methods available to Brazilian Buyers. This is because the commission will be paid in dollars. In addition, payment via bank slip and bank transfer, for example, does not convert on the platform. Therefore, the payment option available on the payment page will be by credit card and PIX."
Source: https://help.hotmart.com/en/article/25588460435085/what-payment-methods-are-available-and-how-can-i-enable-them-for-my-product-
source_type: help_center
verification_status: direct_verified
Date: accessed April 14, 2026
Notes: Verified via direct fetch by two independent subagents. Direction: non-Brazil seller → Brazil buyer. Restricts buyer payment options when seller is cross-border.

### F-12
What: Registering or transferring amounts to a bank account of the same ownership but located outside the Creator, Co-producer or Affiliate's country of residence is prohibited.
Verbatim snippet: "Registering or transferring amounts to a bank account of the same ownership but located outside the Creator, Co-producer or Affiliate's country of residence is also prohibited."
Source: https://hotmart.com/en/legal/terms-of-use
source_type: policy_page
verification_status: direct_verified
Date: October 6, 2025 (document version date)
Notes: Verified via direct fetch by two independent subagents. Section 2.8. Forces payout to same-country bank accounts only; no cross-border bank routing allowed regardless of account ownership.

### F-13
What: For international purchases, the price of the product can only be converted into dollar, euro, mexican peso, and peruvian soles at the time of purchase, depending on the country the buyer is in.
Verbatim snippet: "Besides, the price of the product can only be converted into dollar, euro, mexican peso, and peruvian soles at the time of the purchase, depending on the country the buyer is."
Source: https://help.hotmart.com/en/article/213026287/how-does-the-international-purchase-process-work-
source_type: help_center
verification_status: direct_verified
Date: accessed April 14, 2026
Notes: Verified via direct fetch by two independent subagents. MXN and PEN are explicitly supported as buyer checkout display currencies. Other LatAm currencies (COP, ARS, CLP) are not listed as checkout conversion options in this source.

### F-14
What: The Hotmart Card Policies regulate the request and use of the Hotmart Card for transactions carried out in U.S. dollars (USD) by approved Users who declare domicile outside Brazil in their Platform account.
Verbatim snippet: "These Hotmart Card Policies regulate the request and use of the Hotmart Card for transactions carried out in U.S. dollars (USD) by approved Users who declare domicile outside Brazil in their Platform account."
Source: https://hotmart.com/en/legal/hotmart-card-policies
source_type: policy_page
verification_status: direct_verified
Date: July 2, 2025 (policy version date)
Notes: Verified via direct fetch by two independent subagents. Overview Section A. Provides non-Brazil users (including LatAm sellers) a USD-denominated virtual Mastercard to spend earnings without withdrawing to bank.

---

Part 2 - Provisional findings (blocked_url_index_verified)

### F-P01
What: A Costa Rica-based creator (Martínez) had not been able to charge clients outside of his native market of Costa Rica before joining Hotmart, because clients could not find a way around PayPal's geographic payment restrictions.
Verbatim snippet: "Before joining Hotmart, Martínez, the car repair creator, hadn't been able to charge clients outside of his native market of Costa Rica. Although many were willing to pay his $20 monthly subscription fee, they couldn't find a way around PayPal's geographic payment restrictions."
Source: https://restofworld.org/2023/hotmart-get-rich-without-going-viral/
source_type: article
verification_status: blocked_url_index_verified
Date: June 19, 2023
Notes: Recovery method: research subagent reported successful direct page access; conservatively classified as blocked_url_index_verified because verbatim was not independently double-verified by a separate verification subagent. Article predates April 2025–April 2026 experience window. Journalism interview, single-source OK per protocol. Direction: Costa Rica seller → US buyer (Latino community in US mentioned in article context).

### F-P02
What: A Mexico-based personal finance creator (Sofía Macías) stated that Hotmart accepts all payment processors, credit cards, and even cash payments in cornershops like OXXO.
Verbatim snippet: "'Hotmart has a really good advantage: They accept all payment processors, credit cards, even cash payments in cornershops like Oxxo,' Sofía Macías, a personal finance creator, told Rest of World."
Source: https://restofworld.org/2023/hotmart-get-rich-without-going-viral/
source_type: article
verification_status: blocked_url_index_verified
Date: June 19, 2023
Notes: Recovery method: same article as F-P01, different speaker (multi-speaker page split). Research subagent reported direct page access; conservatively classified as provisional. Journalism interview, single-source OK. OXXO is a Mexico-specific local cash payment method.

### F-P03
What: Payoneer states that companies including Hotmart, Workana, MercadoLibre, and Airbnb choose Payoneer to deliver their mass payouts across Latin America, via Payoneer's network extending to 190+ countries and territories in over 70 currencies.
Verbatim snippet: "Companies like Hotmart, Workana, MercadoLibre, and Airbnb choose Payoneer to deliver their mass payouts across Latin America. Our robust network, which extends to 190+ countries and territories in over 70 currencies, allows enterprises to reach payees anywhere in the world with peace of mind."
Source: https://www.payoneer.com/resources/risk-compliance/latin-america-growth/
source_type: article
verification_status: blocked_url_index_verified
Date: not specified
Notes: Recovery method: Google search snippet. URL not directly fetched by verification subagent. Payoneer is the confirmed payout partner for Hotmart non-BRL currencies.

### F-P04
What: A third-party affiliate review states that for Brazilians, the minimum Hotmart payout is 20 Reals; for non-Brazilians, the minimum payout is $50 or €50; and that payment options are bank transfer and Payoneer.
Verbatim snippet: "The payment options are bank transfer and Payoneer. If you are a Brazilian, then you need to reach at least 20 Reals. For others, the minimum payout is $50 or €50."
Source: https://www.way2earning.com/2021/06/hotmart-affiliate-program/
source_type: blog
verification_status: blocked_url_index_verified
Date: 2021 (periodically updated; site title references 2026)
Notes: Recovery method: Google search snippet. URL not directly fetched by verification subagent. The 20 BRL Brazilian minimum threshold appears only in third-party sources within this shard; not confirmed in the official help center articles accessed.

### F-P05
What: Hotmart announced strong performance results following the adoption of Pix Automático, Brazil's new recurring feature within the real-time payment system Pix, integrated through EBANX, a fintech specializing in payments for emerging markets.
Verbatim snippet: "Hotmart, a global technology company and leader in digital business in the Creator Economy, announced strong performance results following the adoption of Pix Automático, Brazil's new recurring feature within the real-time payment system Pix."
Source: https://www.prnewswire.com/news-releases/ebanx-enables-pix-recurring-payments-for-hotmart-leading-to-a-32-point-retention-increase-302565939.html
source_type: article
verification_status: blocked_url_index_verified
Date: September 24, 2025
Notes: Recovery method: Google search snippet; page partially loaded on direct fetch attempt. Brazil-specific payment infrastructure (Pix) affecting buyer payment options for sellers serving Brazilian market.

### F-P06
What: Hotmart has sales in more than 188 countries, and offices in Brazil, Spain, Mexico, Colombia, the Netherlands, France, the United Kingdom and the United States.
Verbatim snippet: "The company has millions of users around the world, sales in more than 188 countries, and offices in: Brazil, Spain, Mexico, Colombia, the Netherlands, France, the United Kingdom and the United States."
Source: https://www.affiliateprogramdb.com/brands/hotmart-affiliate-program/
source_type: article
verification_status: blocked_url_index_verified
Date: not specified
Notes: Recovery method: Google search snippet. URL not directly fetched by verification subagent. Lists physical office presence in three LatAm countries (Brazil, Mexico, Colombia) and in the US.

---

Part 3 - Pattern candidates (sealed)

### PC-01
Pattern Candidate ID: PC-01
Candidate statement: All LatAm↔US transactions on Hotmart are denominated in USD and processed by the Netherlands entity Hotmart BV, creating a Netherlands-intermediated settlement structure for cross-border flows rather than direct LatAm-entity or US-entity processing.
Related Finding IDs: F-01, F-03, F-05, F-09, F-14
Status: sealed; not validated

### PC-02
Pattern Candidate ID: PC-02
Candidate statement: LatAm sellers outside Brazil face a more constrained payout infrastructure than Brazilian sellers, with higher minimum thresholds, fewer withdrawal method options, mandatory same-country bank account registration, and no local-currency conversion option except for Colombia (USD→COP).
Related Finding IDs: F-05, F-06, F-07, F-09, F-12, F-P04
Status: sealed; not validated

### PC-03
Pattern Candidate ID: PC-03
Candidate statement: Mexico receives distinct regulatory and operational treatment among LatAm countries on Hotmart: it is the only country where Hotmart operates as reseller rather than commercial agent, it has country-specific buyer payment methods (OXXO, SPEI, Mercado Pago), and the Mexican peso is one of only four currencies supported for buyer checkout price conversion.
Related Finding IDs: F-02, F-03, F-13, F-P02
Status: sealed; not validated

---

Part 4 - Could not verify / Out-of-scope

### F-X01: W-8BEN / 1099 / US tax forms for non-US Hotmart sellers
What: No English-language documentation found confirming whether Hotmart issues, requires, or processes W-8BEN, 1099, or other US tax forms for non-US sellers.
Verbatim snippet: "n/a — absence finding"
Source: specific searches and locations attempted: "hotmart W-8BEN", "hotmart 1099 tax form", site:help.hotmart.com/en W-8BEN, site:hotmart.com W-8BEN, web search "hotmart" "W-8BEN" OR "1099" OR "tax form"
source_type: unknown
verification_status: could_not_verify
Date: April 14, 2026
Notes: Searched official Hotmart help center (en-us), terms of use, payments policy, purchase terms, and English-language third-party sources. No references to W-8BEN, 1099, or US tax forms found in any source.

### F-X02: Specific withholding tax rates by LatAm country on Hotmart
What: No English-language documentation found listing specific tax withholding percentage rates by country for Hotmart sellers in LatAm↔US flows.
Verbatim snippet: "n/a — absence finding"
Source: specific searches and locations attempted: "hotmart tax withholding rate country", "hotmart withholding percentage", site:help.hotmart.com/en tax withholding rate, site:hotmart.com/en/legal tax rate
source_type: unknown
verification_status: could_not_verify
Date: April 14, 2026
Notes: Payments Policy Section 1.6 discusses tax obligations generally but does not specify percentage rates. Help center tax article discusses tax-inclusive vs tax-exclusive regions without enumerating specific rates or listing which countries fall into each category.

### F-X03: KYC verification requirements by country for Hotmart seller accounts
What: No English-language documentation found detailing country-specific KYC document requirements or verification procedures for Hotmart seller account creation.
Verbatim snippet: "n/a — absence finding"
Source: specific searches and locations attempted: "hotmart KYC country requirements", "hotmart verification documents country", site:help.hotmart.com/en KYC, "hotmart seller account verification country"
source_type: unknown
verification_status: could_not_verify
Date: April 14, 2026
Notes: Terms of Use mention registration and banking information requirements generally (Section 2.8) but no country-specific KYC documentation requirements found in English.

### F-X04: English-language Reddit experiences on Hotmart cross-border LatAm↔US
What: No English-language Reddit posts or comments found discussing specific cross-border LatAm↔US payout, tax, currency, or availability experiences on Hotmart with named countries and concrete outcomes.
Verbatim snippet: "n/a — absence finding"
Source: specific searches and locations attempted: site:reddit.com/r/hotmart payout country, site:reddit.com hotmart Brazil US tax, site:reddit.com hotmart currency withdrawal, reddit hotmart payout method country experience, site:reddit.com "hotmart" Brazil OR Mexico OR Colombia OR Argentina payment, site:reddit.com hotmart international payout, site:reddit.com hotmart cross-border, site:reddit.com hotmart W-8BEN tax (14 query variations total)
source_type: reddit
verification_status: could_not_verify
Date: April 14, 2026
Notes: Hotmart Reddit community is overwhelmingly Portuguese-language (top subreddits: r/desabafos, r/brasil, r/investimentos, r/farialimabets — all Brazilian Portuguese). No English-language subreddit activity found indexed by search engines. Direct Reddit URL access was blocked by permissions.

### F-X05: Capterra review — payout failure in unspecified Latin American country
What: A verified Capterra user (Prof. Dr. Werner K., CEO) reported inability to transfer money to a bank account "here in Latin America" without naming the specific country or payout method attempted.
Verbatim snippet: "I never received my money. It was not possible to transfer the money to my bank account here in Latin America, the money was sent back and customer support sent me a weird message."
Source: https://www.capterra.com/p/219169/Hotmart/reviews/
source_type: buyer_review
verification_status: could_not_verify
Date: January 31, 2024
Notes: Reviewer did not name a specific LatAm country or payout method attempted. Per shard rules, experience findings must name the country, payout method, and outcome. Degraded to Part 4 due to insufficient geographic specificity.

### F-X06: Portuguese/Spanish-language coverage gap
What: Significant Hotmart cross-border seller discussion exists in Portuguese and Spanish but is excluded from this English-only shard scope.
Verbatim snippet: "n/a — absence finding"
Source: specific searches and observations: SocialGrep Hotmart subreddit distribution shows top communities are r/desabafos (11.1%), r/brasil (11%), r/investimentos (9%), r/farialimabets (8.7%) — all Portuguese. Web search results for Hotmart payout/tax queries frequently returned Portuguese/Spanish results ahead of English results.
source_type: unknown
verification_status: could_not_verify
Date: April 14, 2026
Notes: English-only shard scope excludes the vast majority of Hotmart community discussion, which occurs in Portuguese (Brazilian) and Spanish. This language restriction severely limits the quantity of experiential findings available for this shard.

### F-X07: English-language YouTube content on Hotmart cross-border mechanics
What: No relevant English-language YouTube videos found discussing specific Hotmart cross-border LatAm↔US payout, tax, or currency mechanics with concrete details.
Verbatim snippet: "n/a — absence finding"
Source: specific searches and locations attempted: "site:youtube.com hotmart international payout english", "hotmart cross border selling youtube english", "hotmart tax withholding explained youtube"
source_type: video_transcript
verification_status: could_not_verify
Date: April 14, 2026
Notes: YouTube search results for Hotmart are predominantly Portuguese and Spanish language. No English transcripts with cross-border LatAm↔US specifics located.

### F-X08: Club Asesor Fiscal — Hotmart listed as Merchant of Record platform (URL 404)
What: A Spanish tax advisory blog reportedly listed Hotmart among Merchant of Record platforms alongside Paddle, Lemon Squeezy, Gumroad, and Payhip.
Verbatim snippet: "Some well-known ones include Paddle, Lemon Squeezy, Gumroad (partially), Payhip, and Hotmart. But there are key differences between them."
Source: https://clubasesorfiscal.com/en/merchant-of-record-para-creadores/
source_type: blog
verification_status: could_not_verify
Date: not specified
Notes: URL returned 404 on direct fetch. Text recovered from Google search snippet only. Insufficient context in snippet to determine whether the MoR classification refers specifically to LatAm↔US flows or to EU/global tax handling.

---

Research QA Notes

- **Findings forced to Provisional:** F-P01 and F-P02 (Rest of World article at restofworld.org/2023/hotmart-get-rich-without-going-viral/ was accessed by research subagent but verbatim was not independently double-verified by a separate verification subagent; conservatively classified as blocked_url_index_verified). F-P03, F-P04, F-P05, F-P06 were sourced from Google search snippets and could not be directly fetched for verification.
- **Findings degraded to could_not_verify:** F-X05 (Capterra review degraded from potential buyer_review finding due to no specific country named per shard rules on experience finding specificity). F-X08 (Club Asesor Fiscal blog degraded from article finding due to 404 error on direct URL fetch; only Google search snippet available with insufficient context).
- **Findings degraded due to URL not fixable:** F-X08 (clubasesorfiscal.com/en/merchant-of-record-para-creadores/ returned 404; no archived version attempted).
- **Multi-speaker pages split into separate findings:** F-P01 (Martínez, Costa Rica creator) and F-P02 (Sofía Macías, Mexico creator) are from the same Rest of World article URL but quote distinct interviewees with different country-specific experiences.
- **Truncated or partial sources:** F-P05 (PRNewswire EBANX press release page partially loaded; verbatim extracted from accessible portion and confirmed against search snippet).
- **source_type ambiguities:** F-P05 classified as "article" (press release via PRNewswire; "news" exists in the 18-value enum but is not in the shard's allowed source_type list; "article" used as closest permitted match). Shard instructions mention "tax_page" which is not in the 18-value enum; help_center and policy_page used as appropriate per shard guidance.
- **Coverage gaps where findings expected but not found:** (1) W-8BEN/1099/US tax forms — no English-language documentation found for Hotmart; (2) Specific withholding tax rates by LatAm country — no rates enumerated in any source; (3) KYC requirements by country — no country-specific KYC details found; (4) English-language Reddit experiences — zero qualifying results across 14 query variations; (5) English YouTube content — no relevant results; (6) Tax treaty effects on Hotmart withholding — no documentation found; (7) FX markup/spread percentages — no specific percentages or spread data found in any source; (8) Payout timing by country (days to receive funds) — no country-specific timing data found beyond the general "monthly auto-transfer" and "2 business days" cash advance references; (9) Complete list of countries eligible for seller accounts — no enumerated list found, only general statements about 188+ countries.
- **Clean finding count exceeds expected range (14 vs 5–12 expected):** Hotmart's English-language policy documentation (payments-policy, terms-of-use, purchase-terms, card-policies) and help center articles were all directly accessible and contained extensive cross-border LatAm↔US specifics across all four dimensions. The bar was not lowered; all 14 clean findings have character-for-character verified verbatim, explicit named-country or currency-code cross-border elements, and were confirmed by two independent verification subagents.
- **Cases where input could not be decomposed without interpretation:** None. All four dimensions (Currency, Tax, Availability, Payout) had clear, decomposable search targets in the specified source locations.