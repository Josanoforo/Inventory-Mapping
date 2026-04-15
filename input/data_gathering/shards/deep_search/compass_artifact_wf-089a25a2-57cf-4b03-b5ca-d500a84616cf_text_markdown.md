# DG Run — Shard D6: Patreon × Cross-border LatAm↔US Mechanics and Experience

**DG Agent Output — April 14, 2026**
**Protocol note:** Protocol files 02_DG_CORE_PROTOCOL, 03_DG_OUTPUT_CONTRACT, 04_DG_SEARCH_DECOMPOSITION_RULES, and 05_OUTPUT_TEMPLATE were not located in Google Drive (multiple search strategies attempted across name, fullText, and folder queries). Execution proceeds on the embedded shard instructions, which contain comprehensive field definitions, verification statuses, source_type enums, QA criteria, and output structure. All protocol-defined rules from the shard are followed exactly.

---

## Search Decomposition

**SD-01** — CURRENCY × General LatAm × LatAm seller→US buyer — Patreon's currency conversion fee applied when patron payment currency differs from creator payout currency, affecting LatAm creators receiving cross-currency payments.

**SD-02** — CURRENCY × General LatAm × US seller→LatAm buyer — FX buffer and rate methodology used by Patreon to convert tier prices into LatAm buyers' local currencies (or default to USD for unsupported currencies).

**SD-03** — CURRENCY × General LatAm × Both — Complete list of Patreon's supported payout currencies; whether any LatAm currency (BRL, MXN, ARS, COP, CLP) is included.

**SD-04** — CURRENCY × General LatAm × US seller→LatAm buyer — Default currency handling when a LatAm patron's bank currency is not supported by Patreon; foreign transaction fee risk.

**SD-05** — TAX × Mexico × LatAm seller→any buyer — Mexican VAT (IVA) collection at 16% on payments from fans located in Mexico, effective October 2025.

**SD-06** — TAX × Mexico × LatAm seller→any buyer — Mexican income withholding tax (WHT) rates by RFC status (individual, business, no RFC), effective October 2025.

**SD-07** — TAX × Mexico × LatAm seller→any buyer — Mexican VAT withholding (WHT) sharing mechanism between Patreon and creator by RFC status.

**SD-08** — TAX × Brazil × LatAm seller→US buyer — Brazil-specific tax treatment, withholding, or VAT requirements on Patreon.

**SD-09** — TAX × Argentina × LatAm seller→US buyer — Argentina-specific tax treatment, withholding, or VAT requirements on Patreon.

**SD-10** — TAX × Colombia × LatAm seller→US buyer — Colombia-specific tax treatment on Patreon.

**SD-11** — TAX × Chile × LatAm seller→US buyer — Chile-specific tax treatment on Patreon.

**SD-12** — TAX × General LatAm × LatAm seller→US buyer — W-8BEN/W-8BEN-E requirement for all non-US creators; tax treaty benefits availability.

**SD-13** — TAX × General × Both — Patreon's merchant-of-record status; contracting entity; "Patreon = Merchant" declaration.

**SD-14** — TAX × General × Both — VAT/sales tax charged based on member (buyer) location, not creator location — cross-border VAT principle.

**SD-15** — AVAILABILITY × General LatAm × LatAm seller — PayPal payout country list for LatAm; which LatAm countries can receive payouts.

**SD-16** — AVAILABILITY × Cuba × Both — OFAC sanctions blocking Cuba from Patreon access.

**SD-17** — AVAILABILITY × General × Both — Geographic restrictions on payout methods (Stripe US-only; Payoneer non-US only).

**SD-18** — PAYOUT × General LatAm × LatAm seller — Payout methods and per-method fees available to international (LatAm) creators.

**SD-19** — PAYOUT × General LatAm × LatAm seller — USD-to-USD ACH transfer option via Wise or US bank account for international creators.

**SD-20** — PAYOUT × General LatAm × LatAm seller — PayPal and Payoneer Wallet payout limits for international creators.

**SD-21** — PAYOUT × General × LatAm seller — Legacy Payoneer global bank transfer fees for pre-December 2018 accounts.

**SD-22** — EXPERIENCE × General LatAm × Both — Reddit r/patreon and r/patreoncreators user experiences with LatAm↔US cross-border mechanics (April 2025–April 2026).

**SD-23** — EXPERIENCE × General LatAm × Both — English-language blog, article, and creator forum discussions about Patreon LatAm cross-border mechanics (April 2025–April 2026).

---

## Part 1 — Clean Findings (direct_verified)

No valid findings captured.

**Rationale:** All Patreon help center URLs (support.patreon.com) returned HTTP 403 on direct fetch. No source page could be directly accessed and verified. Content was confirmed exclusively through search engine indexing (Google search result snippets), which qualifies as blocked_url_index_verified per the conservative verification protocol. The verification bar was not lowered to inflate this section.

---

## Part 2 — Provisional Findings (blocked_url_index_verified)

---

**Finding ID:** F-P01
**What:** Patreon charges a 2.5% currency conversion fee whenever a fan pays in a currency different from the creator's payout currency. This fee is calculated on the full processed amount including tax, and applies to every cross-currency transaction — directly affecting LatAm patrons paying US creators (or vice versa) when currencies differ. Dimension: CURRENCY.
**Verbatim snippet:** "A 2.5% currency conversion fee applies when a fan pays in a currency that's different from your payout currency. This fee is calculated on the full processed amount, including tax"
**Source:** https://support.patreon.com/hc/en-us/articles/11111747095181-Creator-fees-overview
**source_type:** help_center
**verification_status:** blocked_url_index_verified
**Date:** Current (references August 4, 2025 pricing change)
**Notes:** URL confirmed via Google index; direct fetch returned 403. Applies to all cross-currency transactions including LatAm↔US. Covers SD-01.

---

**Finding ID:** F-P02
**What:** Patreon adds a 2-7% FX buffer to tier prices when converting them into non-native currencies, with the buffer percentage varying by the historical volatility of each currency. Prices are then rounded up to the nearest 50 cents (or nearest whole number for certain currencies). This buffer affects how tier prices appear to LatAm patrons whose currencies are supported for display but not for payout. Dimension: CURRENCY.
**Verbatim snippet:** "After using that average rate to convert to a new currency we add a buffer of 2-7% (depending on the volatility of each currency's historical exchange rate) to protect creators against potential currency fluctuations. We then round up to the nearest 50 cents, except for CZK, DKK, HKD, HUF, NOK, PLN, and SEK, where we round up to the nearest whole number"
**Source:** https://support.patreon.com/hc/en-us/articles/360044469871-How-tiers-are-converted-into-other-currencies
**source_type:** help_center
**verification_status:** blocked_url_index_verified
**Date:** Current
**Notes:** URL confirmed via Google index; direct fetch returned 403. Covers SD-02. LatAm currencies with higher historical FX volatility (e.g., ARS, BRL) would likely fall toward the 7% end of this buffer range.

---

**Finding ID:** F-P03
**What:** Patreon's supported payout currencies do not include any LatAm currency. The platform supports 16 currencies (USD, EUR, GBP, AUD, CAD, CHF, CZK, DKK, HKD, HUF, JPY, NOK, NZD, PLN, SEK, SGD). BRL, MXN, ARS, COP, and CLP are absent, forcing all LatAm creators to operate in a non-local payout currency (typically USD). Dimension: CURRENCY.
**Verbatim snippet:** "Our mission is to get creators paid – and when we say creators, we mean the global community of creators, no matter where you are located. As a creator on Patreon, you can choose your payout to be in your preferred currency, and your patrons can also choose to pledge in their own local currency."
**Source:** https://support.patreon.com/hc/en-us/articles/360039589091-Patreon-s-supported-currencies
**source_type:** help_center
**verification_status:** blocked_url_index_verified
**Date:** Updated August 5, 2025 (per subagent report)
**Notes:** URL confirmed via Google index; direct fetch returned 403. The full currency list behind the 403 wall could not be exhaustively verified, but cross-referencing with the tier conversion article, creator currency FAQ, and payouts guide consistently references only AUD, GBP, EUR, USD (among others), with no LatAm currency appearing in any snippet. The "16+" currency figure is stated on the pricing page. Covers SD-03.

---

**Finding ID:** F-P04
**What:** When a patron's bank operates in a currency Patreon does not support, their processing currency defaults to USD, and their bank may charge a foreign transaction fee. This directly affects LatAm patrons (BRL, ARS, COP, CLP users) paying any creator — their payment is processed in USD regardless. Dimension: CURRENCY.
**Verbatim snippet:** "If a member's bank operates in a currency that we don't currently support, their processing currency will default to USD. As they are paying in a currency different from that of their local bank account, their bank may charge them an additional foreign transaction fee."
**Source:** https://support.patreon.com/hc/en-us/articles/360039539851-Setting-my-creator-currency-FAQ
**source_type:** help_center
**verification_status:** blocked_url_index_verified
**Date:** Current
**Notes:** URL confirmed via Google index; direct fetch returned 403. Covers SD-04. This means LatAm patrons in countries with unsupported currencies face: (1) forced USD processing, (2) potential bank foreign transaction fee, (3) the bank's own FX conversion spread.

---

**Finding ID:** F-P05
**What:** Patreon acknowledges that even when a patron pays in the same currency as their payment instrument, their bank may charge a foreign transaction fee if payment is processed in a different country — and that Patreon's "choices about payment processing may impact or otherwise give rise to this fee." This is a cross-border disclosure affecting LatAm patrons whose transactions may be processed through US infrastructure. Dimension: CURRENCY.
**Verbatim snippet:** "Even if a paid member pays in the same currency as the currency associated with their payment instrument, when a paid member's payment is processed in a country different from the one associated with their payment instrument, then the financial institution associated with that payment instrument may charge them a foreign transaction fee for that payment. We are not applying this fee, have no knowledge of whether the fee is applied, and do not receive any of the funds from that fee, but our choices about payment processing may impact or otherwise give rise to this fee."
**Source:** https://support.patreon.com/hc/en-us/articles/22581195376909-Creator-fees-FAQ
**source_type:** help_center
**verification_status:** blocked_url_index_verified
**Date:** Current
**Notes:** URL confirmed via Google index; direct fetch returned 403. Also confirmed in Patreon's Terms of Use (patreon.com/policy/legal, effective December 14, 2023) with identical language. Cross-border disclosure relevant to SD-04.

---

**Finding ID:** F-P06
**What:** Patreon collects VAT at 16% on payments from fans located in Mexico, effective from October 2025. This tax is added to the tier price at checkout (e.g., a $10 tier appears as $11.60 to Mexican fans). This applies to all creators regardless of their location — a US creator with Mexican fans will have 16% VAT added to those fans' payments. Dimension: TAX.
**Verbatim snippet:** "Patreon will collect VAT (16%) on payments from your fans located in Mexico. We have notified your existing members about this change. You don't need to change your tier pricing, because this will be added to the price fans pay at checkout."
**Source:** https://support.patreon.com/hc/en-us/articles/39169435612429-Mexican-VAT-Income-Taxes
**source_type:** help_center
**verification_status:** blocked_url_index_verified
**Date:** Effective October 1, 2025
**Notes:** URL confirmed via Google index; direct fetch returned 403. Covers SD-05. Flow direction: applies to Mexican fans paying ANY creator (both US seller→LatAm buyer and LatAm seller→LatAm buyer). Verbatim confirmed in my own web_search results.

---

**Finding ID:** F-P07
**What:** Patreon withholds income tax from the earnings of creators based in Mexico, effective October 2025. The withholding rate depends on RFC (Registro Federal de Contribuyentes) status: 20% without an RFC, 2.5% with an individual RFC. Income WHT applies to all earnings before deduction of Patreon's fees, regardless of where the creator's fans are located. Patreon pays the withheld amount to SAT (Mexican tax authority). Dimension: TAX.
**Verbatim snippet:** "Income WHT is calculated on your earnings. The rate of income WHT depends on your RFC status: Without an RFC: 20% of your earnings will be withheld as income tax. With an RFC (individual): 2.5% of your earnings will be withheld."
**Source:** https://support.patreon.com/hc/en-us/articles/39169435612429-Mexican-VAT-Income-Taxes
**source_type:** help_center
**verification_status:** blocked_url_index_verified
**Date:** Effective October 1, 2025; current as of April 2026
**Notes:** URL confirmed via Google index; direct fetch returned 403. Covers SD-06. Flow direction: LatAm seller (Mexico)→any buyer. One subagent reported the individual RFC rate as 1% (the original October 2025 rate); the current page as indexed by Google shows 2.5%, consistent with the January 2026 Mexican regulatory reform that increased the rate from 1% to 2.5% for individual digital platform sellers. Verbatim confirmed in my own web_search results showing the 2.5% figure.

---

**Finding ID:** F-P08
**What:** Patreon applies a VAT withholding mechanism for Mexican creators that depends on RFC status. Without an RFC, Patreon withholds 100% of VAT collected and pays it to SAT. With an individual RFC, Patreon withholds 50% and remits the remaining 50% to the creator, who must then file and pay it to SAT directly. Dimension: TAX.
**Verbatim snippet:** "Depending on whether you have a local tax registration, known locally as an RFC (Registro Federal de Contribuyentes), Patreon is required to withhold the VAT collected and pay it directly to the Mexican tax authorities (SAT). If you have an RFC, Patreon will remit some or all of the Mexican VAT collected to you, and you are required to report and pay this VAT to the Mexican tax authorities through your own tax filings."
**Source:** https://support.patreon.com/hc/en-us/articles/39169435612429-Mexican-VAT-Income-Taxes
**source_type:** help_center
**verification_status:** blocked_url_index_verified
**Date:** Effective October 1, 2025
**Notes:** URL confirmed via Google index; direct fetch returned 403. Covers SD-07. The specific VAT WHT rates (100%/50%) appear in search snippets from this same page. Flow direction: LatAm seller (Mexico)→any buyer. The page also states RFC deadline for initial setup was September 28, 2025.

---

**Finding ID:** F-P09
**What:** All non-US creators on Patreon must submit a W-8BEN (individuals) or W-8BEN-E (entities) form to receive payouts. This form certifies non-US status for IRS purposes. The form includes an option to claim tax treaty benefits for reduced withholding under Chapter 3. This requirement applies to all LatAm creators. Dimension: TAX.
**Verbatim snippet:** "All creators who are not US citizens must submit a W-8BEN or W-8BEN-E in order to pay out their funds. This form ensures that the IRS knows that earnings you make on Patreon are not subject to US income tax."
**Source:** https://support.patreon.com/hc/en-us/articles/360057086011-Submitting-a-W-8BEN
**source_type:** help_center
**verification_status:** blocked_url_index_verified
**Date:** Current
**Notes:** URL confirmed via Google index; direct fetch returned 403. Covers SD-12. Applies to all LatAm creators. Mexico has a US income tax treaty; Brazil, Argentina, Colombia, and Chile do not have comprehensive US income tax treaties, which may affect treaty benefit claims on the W-8BEN. Verbatim confirmed in my own web_search results.

---

**Finding ID:** F-P10
**What:** All creators contract with Patreon, Inc., a U.S. entity. All payments are structured as coming from this US entity. This establishes Patreon's role as the contracting counterparty for all international creators, including LatAm. Dimension: TAX (merchant-of-record structural finding).
**Verbatim snippet:** "As per our terms, all Creators contract with Patreon, Inc., a U.S. entity. As such, all payments are coming from the U.S. entity."
**Source:** https://support.patreon.com/hc/en-us/articles/360047578411-EU-Creator-Frequently-Asked-Tax-Questions
**source_type:** help_center
**verification_status:** blocked_url_index_verified
**Date:** Current
**Notes:** URL confirmed via Google index; direct fetch returned 403. Covers SD-13. While sourced from the EU Creator FAQ, this statement is structural and applies universally to all creators including LatAm. This is a first-class merchant-of-record finding per shard rules.

---

**Finding ID:** F-P11
**What:** Patreon explicitly declares itself as the "Merchant" in the payment processing chain. Creators create the goods, but Patreon manages the exchange. The payment gateway selects the acquiring bank based on the patron's country of residence. Dimension: TAX (merchant-of-record structural finding).
**Verbatim snippet:** "Patreon = Merchant Creators create the goods, but Patreon manages the actual exchange, thus making us the merchant."
**Source:** https://support.patreon.com/hc/en-us/articles/360024774831-How-payment-processing-works-on-Patreon
**source_type:** help_center
**verification_status:** blocked_url_index_verified
**Date:** Current
**Notes:** URL confirmed via Google index; direct fetch returned 403. Covers SD-13. Verbatim confirmed in my own web_search results. The same article states: "The Payment Gateway talks to the Acquiring Bank, picking the right one based on the country in which the patron lives" — confirming country-based payment routing for cross-border transactions.

---

**Finding ID:** F-P12
**What:** Patreon charges sales tax/VAT based on the location of the member (buyer), not the creator (seller). Cross-border sales of digital services are subject to VAT in the customer's location. Patreon calculates, collects, files, and remits VAT in jurisdictions where it has obligation. Each country handles VAT differently, with Mexico referenced as having specific collection and payment obligations. Dimension: TAX.
**Verbatim snippet:** "Where applicable, sales tax is charged on supplies to members and customers based on the location of the member and not of the creator. Since you may have members and customers anywhere in the world and the tax rules differ among locations, all of this information is relevant to you."
**Source:** https://support.patreon.com/hc/en-us/articles/360043054911-Patreon-s-Sales-Tax-Requirements
**source_type:** help_center
**verification_status:** blocked_url_index_verified
**Date:** Current
**Notes:** URL confirmed via Google index; direct fetch returned 403. Covers SD-14. Cross-border principle: a US creator with Mexican fans sees VAT applied based on Mexico's rules; a Mexican creator with US fans sees US state sales tax applied based on each patron's US state.

---

**Finding ID:** F-P13
**What:** Patreon's location-based income withholding policy is jurisdiction-specific. Patreon may withhold income tax from creator earnings depending on their location, with Mexico explicitly referenced as an example. In specific jurisdictions, Patreon also shares VAT payment obligations with the creator through a "withhold VAT mechanism." Dimension: TAX.
**Verbatim snippet:** "Depending on location, Patreon may need to withhold income tax from your earnings earned on Patreon. See, for example, our Mexican VAT & Income Taxes page. You can see your gross earnings and any income tax withheld amounts by visiting the Documents page of your Payouts section. In addition, for any tax withholdings, Patreon usually issues withholding certificates which should provide information and support for your relevant tax compliance."
**Source:** https://support.patreon.com/hc/en-us/articles/207477063-US-Creator-Frequently-Asked-Tax-Questions
**source_type:** help_center
**verification_status:** blocked_url_index_verified
**Date:** Current
**Notes:** URL confirmed via Google index; direct fetch returned 403. Covers SD-06 (general framework). This establishes that Patreon's income withholding is a location-dependent policy applied selectively, not universally. Mexico is the only LatAm country explicitly referenced. Verbatim confirmed in my own web_search results.

---

**Finding ID:** F-P14
**What:** PayPal payouts from Patreon are available in at least 29 LatAm countries/territories, processed through PayPal/HyperWallet. The confirmed LatAm countries include: Argentina, Bahamas, Barbados, Belize, Bermuda, Brazil, Cayman Islands, Chile, Colombia, Costa Rica, Dominica, Dominican Republic, Ecuador, El Salvador, French Guiana, Guadeloupe, Guatemala, Honduras, Jamaica, Mexico, Nicaragua, Panama, Peru, St. Kitts & Nevis, St. Lucia, Trinidad & Tobago, Turks & Caicos Islands, Uruguay, Venezuela. Dimension: AVAILABILITY.
**Verbatim snippet:** "Patreon uses PayPal as an option to process payouts. In some cases, your payout may be processed through a service called HyperWallet, which is a global platform provided by PayPal, to handle payouts for users around the world. This may mean our list of supported countries and regions could differ from PayPal's official list."
**Source:** https://support.patreon.com/hc/en-us/articles/29467737603981-Paypal-supported-countries
**source_type:** help_center
**verification_status:** blocked_url_index_verified
**Date:** Current
**Notes:** URL confirmed via Google index; direct fetch returned 403. Covers SD-15. The full LatAm country list was confirmed in my own web_search results. Verbatim confirmed. This represents the broadest LatAm country availability for any Patreon payout method.

---

**Finding ID:** F-P15
**What:** Cuba is explicitly blocked from Patreon under OFAC sanctions. Patreon restricts transactions involving Cuba (along with Iran, North Korea, Syria, Crimea, DNR, and Luhansk). Enforcement measures include prohibiting access from sanctioned locations, restricting creator benefits from sanctioned areas, and requesting additional compliance information. Dimension: AVAILABILITY.
**Verbatim snippet:** "Certain countries, including Cuba, Iran, North Korea, Syria, and specific regions such as Crimea, the Donetsk People's Republic (DNR), and Luhansk People's Republic (LNR), along with any individuals or entities operating or residing therein"
**Source:** https://support.patreon.com/hc/en-us/articles/360038061371-Sanctions-Policy
**source_type:** help_center
**verification_status:** blocked_url_index_verified
**Date:** Current
**Notes:** URL confirmed via Google index; direct fetch returned 403. Covers SD-16. Cuba is the only LatAm country explicitly blocked. All other major LatAm countries appear on payout-supported lists.

---

**Finding ID:** F-P16
**What:** Stripe direct deposit payout is restricted to US-based creators only. Payoneer bank transfer is exclusively for creators outside the US. This creates a structural split where LatAm creators cannot use Stripe and must use Payoneer-processed bank transfers, PayPal, or Payoneer Wallet for payouts. Dimension: AVAILABILITY.
**Verbatim snippet:** "Depending on your payout country, you can choose from one of the following options: Bank transfer (processed by Stripe) – available for creators based in the U.S. Bank transfer (processed by Payoneer) – available to creators who reside outside of the U.S — please see full country eligibility list here."
**Source:** https://support.patreon.com/hc/en-us/articles/208656246-How-payouts-work
**source_type:** help_center
**verification_status:** blocked_url_index_verified
**Date:** Current
**Notes:** URL confirmed via Google index; direct fetch returned 403. Covers SD-17. Confirmed by separate snippet from Adding your payout details article: "Stripe direct deposit payout is only available for US creators." and "Payoneer is only available as a payout option for creators outside of the US."

---

**Finding ID:** F-P17
**What:** Patreon offers international creators (including LatAm) four payout pathways with distinct fee structures: (1) Local currency bank transfer — ~$0.50 flat fee, minimum $10 payout; (2) USD cross-currency bank transfer — $0.25 + 1.55% conversion fee, minimum $10; (3) USD-to-USD ACH bank transfer — $0.50 flat fee; (4) PayPal and Payoneer Wallet — fees set by those providers, not by Patreon. Dimension: PAYOUT.
**Verbatim snippet:** "If you're an international creator receiving payouts in USD, you have two direct payout options available to you alongside PayPal and Payoneer: Cross currency bank transfer – $0.25 flat fee + 1.55% currency conversion fee (this is inclusive of any currency conversion fees). Eligible countries can payout from USD in Patreon directly to their local currency · USD to USD bank transfer – $0.50 flat fee. As an international creator, you can set up and pay out to a US bank account at any time via a USD to USD local ACH transfer. Just be sure to select the United States as your bank country."
**Source:** https://support.patreon.com/hc/en-us/articles/360039539851-Setting-my-creator-currency-FAQ
**source_type:** help_center
**verification_status:** blocked_url_index_verified
**Date:** Current
**Notes:** URL confirmed via Google index; direct fetch returned 403. Covers SD-18. Verbatim confirmed in my own web_search results. Corroborated by the Payouts guide for creators outside the US article (https://support.patreon.com/hc/en-us/articles/39694936541965). For LatAm creators using USD payout, the $0.25 + 1.55% cross-currency transfer or the $0.50 USD-to-USD ACH are the primary options beyond PayPal/Payoneer Wallet.

---

**Finding ID:** F-P18
**What:** International creators can select the United States as their bank country to enable USD-to-USD ACH transfers, even if they reside outside the US. This is explicitly described as usable with services like Wise. This allows LatAm creators to receive USD payouts at a $0.50 flat fee by maintaining a US-denominated bank account (e.g., via Wise). Dimension: PAYOUT.
**Verbatim snippet:** "Note: In all countries listed, Payoneer Wallet and PayPal are also available payout options. Please note that your bank country is separate from your country of residence. You may select the United States as your bank country, even if you reside outside the U.S., to enable local USD bank transfers."
**Source:** https://support.patreon.com/hc/en-us/articles/39694936541965-Payouts-guide-for-creators-outside-of-the-US
**source_type:** help_center
**verification_status:** blocked_url_index_verified
**Date:** Updated December 12, 2025
**Notes:** URL confirmed via Google index; direct fetch returned 403. Covers SD-19. The same article provides an explicit example: "An Australian creator sets USD as their payout currency and also sets the US as their payout country. They've set up a USD bank account (via a company like Wise) to accept USD payouts directly." This pathway is available to LatAm creators who set up a USD account through Wise or similar fintech services.

---

**Finding ID:** F-P19
**What:** PayPal and Payoneer Wallet payouts from Patreon may be subject to a $20,000 USD payout limit, as set by PayPal/Payoneer. Direct bank transfer has no such limit from Patreon's side. Third-party providers (PayPal, Payoneer) may charge additional fees for currency conversion or withdrawal that vary by region. Dimension: PAYOUT.
**Verbatim snippet:** "For most creators on Patreon for direct payouts, there's no payout limit. If you're using the Payoneer Wallet or PayPal, there may be a payout limit of $20,000 USD. These are set by Payoneer or PayPal, and you can find the details on their website."
**Source:** https://support.patreon.com/hc/en-us/articles/39694936541965-Payouts-guide-for-creators-outside-of-the-US
**source_type:** help_center
**verification_status:** blocked_url_index_verified
**Date:** Updated December 12, 2025
**Notes:** URL confirmed via Google index; direct fetch returned 403. Covers SD-20. The same article includes a separate disclaimer: "The payout fees listed above do not include any additional costs that may be charged by third-party payment processors. While direct bank transfer does not include any additional fees, PayPal and Payoneer may charge extra fees for currency conversion or withdrawal, which vary by region and are subject to change at any time without notice." Relevant to LatAm creators who may face additional regional fees from these providers.

---

**Finding ID:** F-P20
**What:** Creators who connected a Payoneer account prior to December 19, 2018 may use Payoneer's legacy Global Bank Transfer method, which costs $3 USD per payout plus a 2% currency conversion fee. Dimension: PAYOUT.
**Verbatim snippet:** "Creators that connected a Payoneer account prior to December 19, 2018 may be using Payoneer's older Global Bank Transfer payout method. Global Bank Transfers are $3 USD per payout plus the 2% currency conversion fee."
**Source:** https://support.patreon.com/hc/en-us/articles/360058870591-Payoneer-FAQs
**source_type:** help_center
**verification_status:** blocked_url_index_verified
**Date:** Current
**Notes:** URL confirmed via Google index; direct fetch returned 403. Covers SD-21. Legacy method; affects only pre-December 2018 Payoneer-connected accounts. For LatAm creators who connected early, this $3 + 2% fee structure may still apply unless they update their payout method.

---

## Part 3 — Pattern Candidates (sealed)

**PC-01:** Mexico is the only LatAm country with a dedicated Patreon help center article addressing country-specific tax mechanics. No equivalent articles exist for Brazil, Argentina, Colombia, Chile, or any other LatAm country. The Patreon help center tax section (Non-US creator tax info) lists articles for Mexico, EU/DAC7, Germany, Australia, Canada, and UK (Brexit) — no other LatAm jurisdiction appears. The section navigation sidebar visible in search results confirms this: "Mexican VAT & Income Taxes · EU Creator: Introduction to income reporting requirements (DAC7) · Submitting a W-8BEN · Providing your VAT ID number · About Tax Identification Numbers (TINs) · EU Creator: Frequently Asked Tax Questions · EU IOSS VAT on Goods · Australia Creator... · Canada Creator... · German VAT · Brexit..."

**PC-02:** Across all Patreon help center, policy, and pricing pages, LatAm-specific language appears only in two contexts: (1) the Mexico tax article and (2) the PayPal supported countries list. No other LatAm country is individually named in any help center article related to taxes, payouts, or currency. All other non-US LatAm creator guidance defaults to the general international/non-US framework (W-8BEN, Payoneer bank transfer, PayPal payout, USD payout currency).

**PC-03:** No user-reported experiences discussing Patreon cross-border mechanics for LatAm countries were found on Reddit (r/patreon, r/patreoncreators), Patreon's community forum (community.patreon.com), Indie Hackers, or English-language creator blogs within the April 2025–April 2026 window. Sixteen distinct Reddit search queries and twelve distinct web search queries for creator experiences returned zero qualifying results. Reddit's restricted search engine indexing (post-2024 API policy changes) may partially explain this absence, but low volume of English-language LatAm-specific Patreon discussion is also likely.

---

## Part 4 — Could Not Verify / Out-of-Scope

**F-X01:** Brazil-specific tax treatment on Patreon — SD-08 returned no Patreon help center page, policy page, or official documentation addressing Brazil-specific tax, VAT, or withholding mechanics. Brazilian creators are governed by the general non-US framework (W-8BEN, no country-specific withholding on Patreon's side). Brazil does not have a comprehensive income tax treaty with the US. Absence finding.

**F-X02:** Argentina-specific tax treatment on Patreon — SD-09 returned no Patreon help center page or official documentation addressing Argentina-specific tax mechanics. Argentina does not have a comprehensive US income tax treaty. Absence finding.

**F-X03:** Colombia-specific tax treatment on Patreon — SD-10 returned no Patreon documentation addressing Colombia-specific tax mechanics. Colombia does not have a comprehensive US income tax treaty. Absence finding.

**F-X04:** Chile-specific tax treatment on Patreon — SD-11 returned no Patreon documentation addressing Chile-specific tax mechanics. Chile does not have a comprehensive US income tax treaty. Absence finding.

**F-X05:** Reddit user experiences (April 2025–April 2026) — SD-22 returned zero qualifying Reddit posts or comments from r/patreon or r/patreoncreators about LatAm↔US cross-border mechanics within the time window. Sixteen search queries were executed. Reddit's restricted indexing may be a contributing factor. Absence finding.

**F-X06:** English-language blog/article creator experiences (April 2025–April 2026) — SD-23 returned no qualifying first-person creator accounts of LatAm↔US Patreon cross-border experiences within the time window. A Utoppia blog post (December 2025, https://blog.utoppia.com/how-to-receive-payments/patreon/) mentions "digital artists in Brazil" using Patreon but is promotional marketing for Utoppia's own services and does not constitute a verifiable creator experience. Absence finding.

**F-X07:** 30% default US withholding rate for non-US creators — A third-party tax advisory blog (1800accountant.com) states: "The standard withholding rate is typically 30% for payments to foreign persons. This rate may be reduced based on tax treaties between your country and the U.S." This is accurate as a statement of IRS statutory default under Chapter 3, but Patreon's own help center does NOT state this rate. The EU Creator FAQ states "Patreon doesn't withhold any taxes from your funds earned on Patreon" (for EU context), and Mexico has its own specific rates (20%/2.5%). Whether the 30% statutory rate is actually applied by Patreon to LatAm creators in countries without a specific tax article is unconfirmed from Patreon's own sources. Secondary source; could not verify against Patreon-primary documentation.

**F-X08:** Trustpilot review — country not supported for PayPal payout — A Trustpilot review states a creator "couldn't withdraw the money via PayPal because they said my country is not supported." The reviewer does not name their country, payout method attempted (beyond PayPal), or specific outcome details. Per shard rules: "Experience findings must be specific: must name payout method attempted, country, outcome. Vague complaints → Part 4." No country or currency named; out of scope.

**F-X09:** LatAm creator census statistic — Secondary source (Blogging Wizard / Influencer Marketing Hub citing Patreon's 2022 Creator Census) states "5.08% were from Latin America" (659 out of ~13,000 surveyed creators). This is a 2022 statistic from a third-party aggregator, not directly from a Patreon page currently verifiable. Not a cross-border mechanic. Out of scope per "Marketing claims about 'global reach' without concrete mechanics."

**F-X10:** Mexico 2026 income tax rate increase from 1% to 2.5% for individual RFC holders — Third-party regulatory sources (Fonoa, KPMG) report that Mexico's 2026 digital platform tax reform increased the income tax withholding rate for individual sellers from 1% to 2.5%. This aligns with the current Patreon help center page showing 2.5% (rather than the 1% initially reported for October 2025). The regulatory context explains the rate change but is not from a Patreon-primary source. Noted as context for F-P07 discrepancy. Source: https://www.fonoa.com/resources/blog/mexico-digital-platform-tax-b2b-2026 (source_type: blog). Could not verify as Patreon-primary.

---

## Research QA Notes

### Coverage Gaps

1. **All Patreon help center URLs returned 403 on direct fetch.** Every support.patreon.com article was confirmed to exist via Google search engine index (URL, title, and substantive content visible in search snippets), but no page could be directly rendered. This is a systematic access restriction (likely bot-detection or Cloudflare protection on support.patreon.com). As a result, **all 20 findings are classified as blocked_url_index_verified rather than direct_verified**, producing 0 clean findings against an expected shape of 10-18. The verification bar was not lowered per shard instructions.

2. **No Reddit user experiences found for any LatAm country.** Sixteen distinct Reddit search queries targeting r/patreon and r/patreoncreators yielded zero results for LatAm cross-border topics within the April 2025–April 2026 window. Contributing factors: (a) Reddit restricted search engine crawling post-2024 API changes, reducing discoverability; (b) r/patreon is a relatively small subreddit; (c) LatAm creators may discuss Patreon issues in Spanish/Portuguese forums rather than English-language Reddit. Direct Reddit fetches (both www.reddit.com and old.reddit.com) were also blocked.

3. **No Patreon community forum (community.patreon.com) results found.** Searches returned no indexed content from this domain.

4. **Spanish/Portuguese content gap.** Per shard language restriction (English only), no Spanish-language subreddits (r/Mexico, r/argentina, r/brasil), Spanish-language blogs, or Portuguese-language forums were searched. LatAm creator experiences are likely more extensively documented in Spanish and Portuguese. This is flagged as a coverage gap per shard instructions.

5. **Complete absence of country-specific Patreon documentation for Brazil, Argentina, Colombia, and Chile.** Mexico is the only LatAm country with a dedicated Patreon help center article. The remaining four major LatAm countries have no country-specific tax, VAT, or payout guidance from Patreon.

6. **Payoneer country eligibility list not directly verified.** The Patreon help center article "How payouts work" links to a "full country eligibility list" for Payoneer bank transfers, but the linked page was not accessible. PayPal's country list was verified; Payoneer's specific country list for Patreon payouts was not independently confirmed for LatAm coverage.

7. **Supported currencies full list not fully rendered.** The Patreon "Supported currencies" article (360039589091) lists all 16 supported currencies, but the full list was truncated in search snippets. The 16 currencies were reconstructed from cross-references across multiple articles (tier conversion, creator currency FAQ, payouts guide). The absence of LatAm currencies is inferred from consistent non-appearance across all sources, not from an explicit "not supported" statement.

### Degradation Log

| Finding | Degradation | Reason |
|---------|-------------|--------|
| All F-P findings | direct_verified → blocked_url_index_verified | Systematic 403 on all support.patreon.com direct fetches |
| F-P03 | Content partially inferred | Full currency list not visible in search snippets; reconstructed from cross-references |
| F-P07 | Rate discrepancy noted | One subagent reported 1% individual RFC rate (October 2025 original); search index shows 2.5% (current, post-January 2026 reform). 2.5% used as current state. |
| F-X07 | Demoted to Part 4 | 30% default withholding: IRS statutory rate stated by third-party blog, not confirmed as Patreon-applied |
| F-X08 | Demoted to Part 4 | Trustpilot review too vague — no country, no currency, no specific outcome |

### Source_type Assignments

All Patreon support.patreon.com articles → help_center.
Patreon sanctions policy (360038061371) → help_center (content is within the help center domain; no separate "policy_page" domain identified). Note: could also be classified as policy_page since it describes policy rather than how-to guidance. Classified as help_center based on URL domain.
Patreon Terms of Use (patreon.com/policy/legal) → policy_page (referenced in F-P05 Notes but not used as primary source).
Third-party blogs (1800accountant, Fonoa, Utoppia) → blog (all in Part 4).
Trustpilot → buyer_review (in Part 4).

### Multi-Speaker Splits

No multi-speaker situations arose. Zero Reddit threads were found, so no multi-commenter splitting was required.

### Decomposition Limitations

SD-08 through SD-11 (Brazil, Argentina, Colombia, Chile specific tax treatment) produced only absence findings. These SDs were correctly decomposed per the shard instruction to separate by country, but Patreon's help center simply has no country-specific content for these jurisdictions. The decomposition was appropriate but the source material is absent.

SD-22 and SD-23 (user experiences) both produced absence findings. The April 2025–April 2026 time window combined with the English-only language restriction and Reddit's indexing limitations resulted in zero qualifying experience findings.