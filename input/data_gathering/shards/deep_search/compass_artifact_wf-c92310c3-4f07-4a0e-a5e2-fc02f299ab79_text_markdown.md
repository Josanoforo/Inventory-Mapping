Search decomposition
- SD-01: Domestika help center articles on currency accepted for teacher/seller payouts (USD vs local currency)
- SD-02: Domestika help center articles on currency conversion for buyers in LatAm countries (MXN, BRL, COP, ARS) buying courses priced in USD
- SD-03: Domestika help center / terms on tax withholding for non-US sellers/teachers, including W-8BEN or equivalent forms
- SD-04: Domestika help center / terms on US 1099 or tax forms for US-based teachers
- SD-05: Domestika help center / terms on VAT/IVA handling for LatAm buyers or sellers, and merchant-of-record status in any LatAm country
- SD-06: Domestika country availability — which LatAm countries can open teacher/seller accounts, KYC by country
- SD-07: Domestika country availability — which LatAm countries can purchase courses; any geographic restrictions
- SD-08: Domestika payout methods available by country (PayPal, Payoneer, Wise, local bank, wire) with LatAm or US specificity
- SD-09: Domestika payout minimum thresholds by country with LatAm or US specificity
- SD-10: Domestika payout timing / processing schedule by country with LatAm or US specificity
- SD-11: Reddit r/Domestika threads from April 2025 – April 2026 with country-specific or currency-specific payout/tax experience
- SD-12: Trustpilot English-language reviews mentioning specific LatAm country, USD conversion, or payout issues (April 2025 – April 2026)
- SD-13: Video transcripts / blog posts / articles from Domestika teachers discussing cross-border payout mechanics (English, 2025–2026)
- SD-14: Seller forums (Indie Hackers, etc.) discussing Domestika teacher payouts with country-specific angle
- SD-15: Domestika terms of service and privacy policy for entity identification, merchant-of-record, and jurisdiction provisions
- SD-16: Domestika help center on local LatAm payment processors (dLocal or equivalent) handling cash/bank-transfer payments in Mexico, Colombia, Brazil
- SD-17: Domestika help center / terms on geographic restrictions and sanctioned countries affecting LatAm access
- SD-18: Class Central or other investigative journalism on Domestika teacher payout disparities with geographic angle

---

Part 1 - Clean findings (direct_verified)

### F-01

What: Domestika's Terms of Use state that displayed currency is based on user location at account creation, but all fees are always calculated in US dollars, with final charges varying depending on prevailing currency exchange rates offered by payment providers.
Verbatim snippet: "Fees may vary based on your location and other factors. If you are logged into your account, the currency you will see is based on your location when you created your account. However, the final fees charged to you will always be calculated in US dollars; therefore the final fees charged to you may vary depending on prevailing currency exchange rates offered by our payment providers."
Source: https://www.domestika.org/en/terms
source_type: policy_page
verification_status: direct_verified
Date: January 31, 2024 (last updated date stated on page)
Notes: Section 11 "FEES" of the Terms of Use. The explicit mention of currency exchange rates and location-based currency display establishes the cross-border billing mechanism that affects all non-US buyers, including LatAm.

### F-02

What: Domestika prohibits use of its services by users located in or residents of countries subject to US trade sanctions, explicitly naming Cuba among the blocked nations along with Iran, North Korea, Sudan, Syria, and the Crimea region of Ukraine.
Verbatim snippet: "You warrant that you (as an individual or as a representative of any entity on whose behalf you use the Services) are not located in, or a resident of, any country that is subject to applicable U.S. trade sanctions or embargoes (such as Cuba, Iran, North Korea, Sudan, Syria, or the Crimea region of Ukraine)."
Source: https://www.domestika.org/en/terms
source_type: policy_page
verification_status: direct_verified
Date: January 31, 2024 (last updated date stated on page)
Notes: Section 10 "GEOGRAPHIC RESTRICTIONS." Cuba is the only LatAm country explicitly named as blocked.

### F-03

What: Domestika's Terms of Use state that refunded amounts may differ from the original payment due to currency exchange rate fluctuations between the buyer's local currency and the US dollar.
Verbatim snippet: "Due to possible currency exchange rate fluctuations with your local currency and the US dollar, the refunded amount may be slightly higher or lower than your original paid amount."
Source: https://www.domestika.org/en/terms
source_type: policy_page
verification_status: direct_verified
Date: January 31, 2024 (last updated date stated on page)
Notes: Section 12 "REFUNDS." Explicit reference to local currency vs. US dollar establishes the cross-border FX risk borne by non-US buyers.

### F-04

What: Domestika's Privacy Policy identifies the platform operator and data controller as Domestika Inc., a US-incorporated entity with registered office at 2001 Addison St., Suite 300 Berkeley, CA, 94704, United States.
Verbatim snippet: "the Personal Data provided (the 'Personal Data') will be processed by Domestika Inc. ('Domestika') as the owner of the Platform and data controller of the Personal Data provided therein, whose contact details are as follows: Registered Office: 2001 Addison St., Suite 300 Berkeley, CA, 94704, United States."
Source: https://www.domestika.org/en/privacy
source_type: policy_page
verification_status: direct_verified
Date: July 10, 2024 (last updated date stated on page)
Notes: Establishes Domestika Inc. (US) as the operating entity and de facto merchant of record for all transactions, relevant to cross-border tax and jurisdiction determinations for LatAm users. No separate LatAm legal entity is referenced in any public Domestika legal documents.

---

Part 2 - Provisional findings (blocked_url_index_verified)

### F-P01

What: Domestika's help center lists nine LatAm currencies supported for price display on the website: Mexican peso (MXN), Argentine peso (ARG), Colombian peso (COP), Chilean peso (CLP), Peruvian sol (PEN), Panamanian balboa (PAB), Brazilian real (BRL), Uruguayan peso (UYU), and Costa Rica colón (CRC).
Verbatim snippet: [Stated in layout: "Mexican peso (MXN) Argentine peso (ARG) Colombian peso (COP) Chilean peso (CLP) Peruvian sol (PEN) Panamanian balboa (PAB) Brazilian real (BRL) Uruguayan peso (UYU) Costa Rica colón (CRC)"]
Source: https://support.domestika.org/hc/en-us/articles/360003316798-In-which-currency-are-the-prices-shown
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated
Notes: Page returned 403 on direct fetch; content captured from Google search index snippet tied to this exact URL. The page lists "ARG" rather than the ISO-standard "ARS" for the Argentine peso code. Additional non-LatAm currencies (EUR, GBP, CAD, AUD, JPY, INR, and others) are also listed on the same page but are outside D6 scope.

### F-P02

What: Domestika states it does not apply commissions or taxes relating to the exchange rate between currencies, but notes that the buyer's bank or payment processor may add an additional fee.
Verbatim snippet: "Domestika doesn't apply commissions or taxes relating to the exchange rate between currencies. However, your bank or payment processor may add an additional fee and so we suggest that you contact them directly to confirm their policy regarding this."
Source: https://support.domestika.org/hc/en-us/articles/360003316798-In-which-currency-are-the-prices-shown
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated
Notes: Page returned 403 on direct fetch; content captured from Google search index snippet tied to this exact URL. This means Domestika does not add an FX markup on top of the USD charge, but LatAm buyers may still face bank-imposed conversion fees.

### F-P03

What: Domestika's help center states that as a US-based company, all charges are processed in dollars and invoices are issued without taxes because Domestika does not charge them.
Verbatim snippet: "We remind you that as we are a company based in the United States, all charges are processed in dollars and invoices are issued without taxes because we do not charge them."
Source: https://support.domestika.org/hc/en-us/articles/360003164078-How-can-I-download-the-invoice-for-my-purchase
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated
Notes: Page returned 403 on direct fetch; content captured from Google search index snippet tied to this exact URL. Confirms Domestika does not collect VAT/IVA/sales tax on behalf of any jurisdiction. Any local tax obligations (e.g., Argentine impuesto PAIS, Mexican IVA on digital services) fall on the buyer or are applied by the buyer's bank/payment processor.

### F-P04

What: Domestika's help center acknowledges that in some countries, local or national taxes are applied to international purchases or to currencies different from the buyer's local currency, which can result in additional charges or declined payments.
Verbatim snippet: "In some countries, there are local/national taxes that are applied to international purchases or to currencies that are different from that of your local currency which can result in an additional charge."
Source: https://support.domestika.org/hc/en-us/articles/360003447297-What-should-I-do-if-I-can-t-complete-the-payment
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated
Notes: Page returned 403 on direct fetch; content captured from Google search index snippet tied to this exact URL. This passage immediately precedes the Argentina-specific passage captured in F-P05. No specific LatAm countries are named in this passage itself, but the "international purchases" and "currencies that are different" language confirms the cross-border cut.

### F-P05

What: Domestika's help center specifically identifies Argentina as a country where there is a monthly limit for transactions in dollars, and states that reaching this limit will cause payment rejections on the platform.
Verbatim snippet: "Likewise in places like Argentina, there's a monthly limit for transactions in dollars. If you reach this limit and attempt to complete a new purchase, the payment will be rejected."
Source: https://support.domestika.org/hc/en-us/articles/360003447297-What-should-I-do-if-I-can-t-complete-the-payment
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated
Notes: Page returned 403 on direct fetch; content captured from Google search index snippet tied to this exact URL. This passage follows the one captured in F-P04 on the same page. Argentina is the only LatAm country explicitly named in this context. The dollar transaction limit references Argentine Central Bank (BCRA) restrictions on foreign-currency purchases.

### F-P06

What: Domestika's Payment methods help page states that buyers located in Mexico, Colombia, or Brazil can use local payment methods such as paying in cash or via bank transfer, and that the buyer's profile location must be updated for this option to appear.
Verbatim snippet: "If you are in Mexico, Colombia, or Brazil, you can use local payment methods such as paying in cash or via bank transfer.* In order for this payment option to appear for you, you should have your location updated in your profile."
Source: https://support.domestika.org/hc/en-us/articles/360018788378-Payment-methods
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated
Notes: Page returned 403 on direct fetch; content captured from Google search index snippet tied to this exact URL. Only Mexico, Colombia, and Brazil are named as having local payment methods. No other LatAm countries (e.g., Argentina, Chile, Peru) have this option documented.

### F-P07

What: Domestika requires country-specific identity numbers for LatAm local payment methods: CURP for Mexico, CC (cédula de ciudadanía) number for Colombia, and CPF/CNPJ number for Brazil, each entered during the checkout process.
Verbatim snippet: "Mexico: After following the necessary steps to make the purchase, please choose the option \"Pay in cash and other payment methods\" and insert your CURP number (if you don't know it, you can always find out what it is in this link. Take into account that we only request this information for security reasons). Select the bank or commercial entity of your choice in order to generate a proof of purchase and once you have it, please go to the bank or commercial entity to make the payment. Colombia: After following the necessary steps to make the purchase, please choose the option \"Pay in cash and other payment methods\" and insert the CC number. Select the bank or commercial entity of your choice in order to generate a proof of purchase and once you have it, please go to the bank or commercial entity to make the payment. Brazil: After following the necessary steps to make the purchase, please choose the option \"Pay in Cash and other payment methods\" and introduce the CPF/CNPJ number."
Source: https://support.domestika.org/hc/en-us/articles/360018788378-Payment-methods
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated
Notes: Page returned 403 on direct fetch; content captured from Google search index snippet tied to this exact URL. Same page as F-P06 but covers the distinct data point of country-specific KYC/identity requirements for local payments. These identity document requirements serve as de facto KYC for LatAm local payment flows.

### F-P08

What: Domestika's help center states that the Plus subscription cannot be purchased in cash or via bank transfer (the local payment methods available in Mexico, Colombia, and Brazil), because it requires a payment method that enables automatic renewal.
Verbatim snippet: "**The Plus subscription cannot be purchased in cash or via bank transfer (available in Mexico, Colombia and Brazil), as it must have a means of payment that enables automatic renewal."
Source: https://support.domestika.org/hc/en-us/articles/4417429219345-How-do-I-pay-for-the-Domestika-Plus
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated
Notes: Page returned 403 on direct fetch; content captured from Google search index snippet tied to this exact URL. The leading "**" appears in the search snippet and may be formatting from the original page. This means buyers in Mexico, Colombia, and Brazil who rely on cash/bank-transfer payments cannot subscribe to Domestika Plus, effectively restricting the subscription product for those using local-only payment methods.

### F-P09

What: Domestika identifies dLocal as the processor for local payment methods (cash, bank transfer) on the website, requiring buyers to provide proof of payment or receipt from the store where the deposit was made.
Verbatim snippet: "Payment on the website through local methods (cash, bank transfer) processed by dLocal: proof of payment or receipt from the store where the deposit was made."
Source: https://support.domestika.org/hc/en-us/articles/360003052038-I-can-t-find-my-course-in-my-profile
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated
Notes: Page returned 403 on direct fetch; content captured from Google search index snippet tied to this exact URL. dLocal is a publicly traded LatAm-focused cross-border payment processor (NASDAQ: DLO), confirming Domestika uses specialized LatAm payment infrastructure for local cash/bank-transfer flows in Mexico, Colombia, and Brazil. The same passage also appears on https://support.domestika.org/hc/en-us/articles/4406236005137.

### F-P10

What: Domestika's help center states that payments processed from App Stores (not by Domestika) are generally considered local transactions, and suggests buyers with problems completing international purchases consider using the Domestika app as an alternative.
Verbatim snippet: "Payments processed from the App Stores (not by Domestika) are generally considered local transactions. If you have problems with international purchases, please consider trying to complete your order using the Domestika app."
Source: https://support.domestika.org/hc/en-us/articles/360003447297-What-should-I-do-if-I-can-t-complete-the-payment
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated
Notes: Page returned 403 on direct fetch; content captured from Google search index snippet tied to this exact URL. Same page as F-P04 and F-P05. This establishes that LatAm buyers whose cards are blocked for international/USD purchases can use the Apple App Store or Google Play as an alternative payment path, where the transaction is processed as local by the respective app store rather than as an international USD charge by Domestika.

---

Part 3 - Pattern candidates (sealed)

### PC-01

Pattern Candidate ID: PC-01
Candidate statement: Multiple Domestika policy and help center pages consistently describe a billing architecture in which all web charges are settled in USD from a US entity (Domestika Inc., Berkeley CA), with LatAm buyers seeing local-currency display prices but absorbing all currency conversion costs from their own banks or payment processors, as Domestika states it does not apply commissions on exchange rates.
Related Finding IDs: F-01, F-03, F-04, F-P01, F-P02, F-P03
Status: sealed; not validated

### PC-02

Pattern Candidate ID: PC-02
Candidate statement: Three LatAm countries — Mexico, Colombia, and Brazil — receive differentiated treatment in Domestika's buyer payment infrastructure, with dedicated local payment methods (cash and bank transfer processed by dLocal) and country-specific identity verification requirements (CURP, CC, CPF/CNPJ), while other LatAm countries must use international card or PayPal payments to transact on the platform.
Related Finding IDs: F-P06, F-P07, F-P08, F-P09
Status: sealed; not validated

### PC-03

Pattern Candidate ID: PC-03
Candidate statement: Domestika's publicly documented cross-border tax posture places all tax responsibility on the buyer or seller — the platform does not collect or remit VAT, IVA, or sales tax and issues tax-free invoices from its US entity, while no public documentation exists regarding teacher-side tax withholding, W-8BEN/1099 forms, or withholding rates by country, with teacher contracts reportedly covered by NDA.
Related Finding IDs: F-04, F-P03, F-P04, F-X01, F-X02, F-X03
Status: sealed; not validated

---

Part 4 - Could not verify / Out-of-scope

### F-X01: W-8BEN / tax form requirements for non-US Domestika teachers

What: No data found on whether Domestika requires W-8BEN forms from non-US (including LatAm) teachers, or what tax withholding procedures apply to cross-border teacher royalty payments.
Verbatim snippet: "n/a — absence finding"
Source: Searched support.domestika.org (help center, terms, privacy policy, teachers page), web searches for "Domestika W-8BEN," "Domestika teacher tax withholding," "Domestika non-US teacher tax form," Reddit, Indie Hackers, Medium, and YouTube. No results.
source_type: unknown
verification_status: could_not_verify
Date: Searched April 2026
Notes: Domestika's Privacy Policy confirms collection of "tax identification data" from teachers/affiliates/creatives, implying some tax form process exists, but no public documentation specifies the forms or rates. Teacher contracts are reportedly covered by NDA (per EdWize and Sketch Like an Architect blog references). Comparable US-based platform Udemy publicly documents W-8BEN requirements; Domestika does not.

### F-X02: Specific tax withholding rates by country for Domestika teacher payouts

What: No data found on specific tax withholding rates applied by Domestika to teacher royalty or advance payments, by country or tax treaty status.
Verbatim snippet: "n/a — absence finding"
Source: Searched support.domestika.org, domestika.org/en/terms, domestika.org/en/privacy, web searches for "Domestika withholding rate teacher," "Domestika royalty tax country," Reddit, forums. No results.
source_type: unknown
verification_status: could_not_verify
Date: Searched April 2026
Notes: As Domestika Inc. is a US entity paying royalties to non-US individuals, US tax law (IRC §1441) would generally require 30% withholding on US-source income to non-US payees absent a W-8BEN claiming treaty benefits. No public Domestika source confirms or denies this. Searched locations only.

### F-X03: VAT/IVA collection or handling by Domestika for LatAm countries

What: No data found on Domestika collecting, remitting, or handling VAT or IVA for any specific LatAm country (e.g., Mexican IVA on digital services, Colombian IVA, Argentine IVA).
Verbatim snippet: "n/a — absence finding"
Source: Searched support.domestika.org for "IVA," "VAT," "value added tax," domestika.org/en/terms, domestika.org/en/privacy. No LatAm-specific VAT/IVA results found.
source_type: unknown
verification_status: could_not_verify
Date: Searched April 2026
Notes: F-P03 confirms Domestika states "invoices are issued without taxes because we do not charge them." Several LatAm countries (Mexico since June 2020, Colombia, Argentina, Chile) require foreign digital service providers to collect local VAT/IVA on B2C digital sales. Domestika's public position appears to be non-collection, but no specific country-level compliance documentation was found. Coverage gap for this shard.

### F-X04: Teacher payout methods beyond PayPal

What: No data found on Domestika offering teacher/instructor payout methods other than PayPal (such as Payoneer, Wise, wire transfer, or local bank transfer for LatAm-based teachers).
Verbatim snippet: "n/a — absence finding"
Source: Searched support.domestika.org, domestika.org/en/teachers (which states "All you need is a PayPal account"), domestika.org/en/affiliates, web searches for "Domestika teacher payout Payoneer," "Domestika teacher wire transfer," "Domestika teacher bank transfer payout," Reddit, forums. No alternative methods found.
source_type: unknown
verification_status: could_not_verify
Date: Searched April 2026
Notes: The Domestika teachers page (directly accessed) states only PayPal. The affiliates page states payouts are "in dollars (USD) via PayPal." No Payoneer, Wise, wire, or local-bank teacher payout options are documented anywhere. This may limit LatAm teachers in countries with restricted PayPal functionality. Searched locations only.

### F-X05: Payout minimum thresholds or timing by country/region for teachers

What: No data found on Domestika teacher payout minimum thresholds, payout frequency, or payout scheduling by country or region (LatAm or US).
Verbatim snippet: "n/a — absence finding"
Source: Searched support.domestika.org, domestika.org/en/teachers, web searches for "Domestika payout minimum," "Domestika teacher payment schedule country," "Domestika royalty payment frequency," Reddit, forums. No results.
source_type: unknown
verification_status: could_not_verify
Date: Searched April 2026
Notes: The affiliates page states payments are calculated "every month." A third-party blog (sketchlikeanarchitect.com, David Drazil, Czech Republic–based teacher) mentions advance fees are paid "usually within a month of completing production" but provides no country-specific details and is under NDA. No public schedule, threshold, or country-specific payout timing documentation exists.

### F-X06: English-language LatAm-specific cross-border experience reports (April 2025 – April 2026)

What: No English-language Reddit posts, forum threads, Trustpilot reviews, or blog posts were found from LatAm-based Domestika teachers or buyers specifically reporting cross-border payment, currency, tax, or payout experiences within the April 2025 – April 2026 window.
Verbatim snippet: "n/a — absence finding"
Source: Searched site:reddit.com/r/Domestika (subreddit appears inactive or nonexistent), site:reddit.com Domestika payout country, site:reddit.com Domestika currency Latin America, site:reddit.com Domestika Mexico/Brazil/Colombia/Argentina, Trustpilot domestika.org English reviews, site:indiehackers.com Domestika, Medium Domestika teacher, YouTube Domestika teacher payout. No LatAm-specific English-language experience reports found.
source_type: unknown
verification_status: could_not_verify
Date: Searched April 2026
Notes: The r/Domestika subreddit appears to have minimal or no active community. Domestika discussions on Reddit are scattered across other subreddits (r/craftsnark, r/graphic_design, r/argentina, r/embroidery) and overwhelmingly focus on subscription billing issues rather than cross-border payment mechanics. LatAm user experiences may exist primarily in Spanish-language sources (coverage gap noted below). Teacher contracts reportedly include NDAs which likely suppress public discussion of payout specifics.

### F-X07: Teacher PayPal-only payout (verified content, no explicit cross-border cut in text)

What: Domestika's teachers page states that all a teacher needs to receive payments is a PayPal account, but the passage contains no explicit mention of country, currency, or cross-border mechanism.
Verbatim snippet: "All you need is a PayPal account. As soon as we verify it, we'll send you the instructions so that you can easily receive the payments."
Source: https://www.domestika.org/en/teachers
source_type: platform_doc
verification_status: could_not_verify
Date: Accessed April 2026; page undated
Notes: Page was directly accessed and content is verified, but the finding is degraded to could_not_verify and placed in Part 4 because the verbatim snippet contains no explicit cross-border cut (no country, no currency code, no international tax mechanism, no geographic restriction). The cross-border relevance is contextual (US company paying international teachers via PayPal) rather than explicit in the text. Degraded per D6 QA checklist.

### F-X08: US vs non-US instructor payment disparity (Class Central, not LatAm-specific)

What: A Class Central investigative article reports that a US-based (Florida) Domestika instructor continued receiving payments while non-US instructors had payments stopped, but the non-US instructors referenced are based in Spain (Madrid), not in Latin America.
Verbatim snippet: "Domestika hasn't stopped paying every inactive instructor. Liam Filler*, a Florida-based instructor, has been getting paid until now, despite not replying to students for a year and a half."
Source: https://www.classcentral.com/report/domestika-unpaid-instructors/
source_type: article
verification_status: could_not_verify
Date: November 4, 2025 (article date per search snippet)
Notes: Page returned 403 on direct fetch; snippet captured from Google search index. Degraded to could_not_verify because: (1) the 403 access issue, (2) snippet may be truncated, and (3) the geographic comparison is US vs. Spain, not US vs. LatAm, placing it outside strict D6 scope. The article uses pseudonyms (asterisked names). The finding is included as contextual evidence of possible geographic differential in Domestika's payout enforcement, but no LatAm instructor is specifically named or discussed.

---

Research QA Notes
- Findings forced to Provisional: F-P01 through F-P10 — all from support.domestika.org help center pages that returned HTTP 403 on direct fetch. Content for each was captured from Google search index snippets tied to exact URLs. Verification conservatively assigned as blocked_url_index_verified per protocol (search index of the same URL = valid indirect access).
- Findings degraded to could_not_verify: F-X07 (verified content from directly accessed page but lacks explicit cross-border cut in text per D6 QA checklist); F-X08 (403 access + not LatAm-specific).
- Findings degraded due to URL not fixable: None.
- Multi-speaker pages split into separate findings: None applicable. No multi-speaker pages were encountered with D6-relevant content. MoneySavingExpert forum (forums.moneysavingexpert.com/discussion/6557604/domestika-warning) had multiple speakers but content was UK↔US, not LatAm↔US — excluded from D6 scope entirely.
- Truncated or partial sources: All support.domestika.org pages (F-P01 through F-P10) were accessed only via Google search index snippets, which may truncate or reformat page content. Full page content could not be verified due to 403 errors. Snippets used are continuous passages as displayed in search index.
- source_type ambiguities: The shard scope lists "tax_page" as an allowed source_type, but "tax_page" is NOT in the 18-value enum. No findings in this shard required this classification. F-P03 (invoice/tax-related help center article) and F-P04 (payment issues article with tax content) were classified as help_center, which is the most specific valid enum value for support.domestika.org articles. Domestika does not appear to have a dedicated tax policy page.
- Coverage gaps where findings expected but not found:
  - **Teacher-side tax mechanics (SD-03, SD-04):** No public documentation exists for W-8BEN, 1099, or any tax withholding rates for Domestika teachers. This is a critical gap — as a US entity paying royalties internationally, Domestika almost certainly has tax withholding processes, but they are not publicly documented and are likely covered by teacher contract NDAs.
  - **VAT/IVA compliance for LatAm (SD-05):** Domestika states it does not charge taxes on invoices, but multiple LatAm countries now require foreign digital service providers to collect local VAT/IVA. No Domestika documentation addresses compliance with these requirements.
  - **Teacher payout details (SD-08, SD-09, SD-10):** No country-specific payout methods, thresholds, or timing are publicly documented. PayPal is the only confirmed method. This is a significant gap for understanding LatAm teacher experience.
  - **LatAm user experience in English (SD-11, SD-12, SD-13, SD-14):** No English-language LatAm-specific cross-border experience reports were found from April 2025–April 2026. LatAm user experiences likely exist primarily in Spanish-language sources (e.g., Domestika's own Spanish-language forums have Argentina-specific payment threads). This is a language-boundary coverage gap inherent to the English-only constraint of this shard.
  - **Argentine peso (ARS) buyer experience:** Argentina is specifically named in Domestika's help center as having dollar transaction limits, but no English-language buyer experience reports were found describing the impact.
  - **Accepted card networks with LatAm relevance:** The Payment methods page lists Elo, Hipercard (Brazilian card networks), BBVA Bancomer, and Santander (Mexican banks) among accepted cards, confirming LatAm-specific payment infrastructure. This was not elevated to a standalone finding but is noted here as supporting context for PC-02.
  - **Domestika affiliate payouts:** The affiliates page (domestika.org/en/affiliates) states payouts are "in dollars (USD) via PayPal" monthly. This was not elevated to a standalone finding because the page was only partially accessed (search snippet), and the cross-border cut is general (USD for all affiliates) rather than LatAm-specific.
- Cases where input could not be decomposed without interpretation: None.