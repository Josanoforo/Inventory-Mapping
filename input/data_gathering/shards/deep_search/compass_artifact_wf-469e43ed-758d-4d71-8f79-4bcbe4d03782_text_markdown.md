# DG OUTPUT — Lemon Squeezy × D6: Cross-border LatAm↔US mechanics (English)

---

## 1. SEARCH DECOMPOSITION

**SD-01** [Currency]: What LatAm currencies (MXN, BRL, ARS, COP, CLP, PEN, BOB, UYU, PYG, GTQ, HNL, NIO, CRC, DOP, VES) does Lemon Squeezy support for store/checkout display?
**SD-02** [Currency]: How does Lemon Squeezy convert non-USD currencies at checkout (mechanism, rate type, markup)?
**SD-03** [Currency]: Does Lemon Squeezy charge an FX markup or spread on currency conversion at checkout or payout?
**SD-04** [Currency]: How does Lemon Squeezy handle payout currency conversion for non-US bank accounts?
**SD-05** [Currency]: What is the +1.5% international transaction fee and is it triggered by buyer location, seller location, or both?
**SD-06** [Tax]: What is Lemon Squeezy's merchant-of-record status and what tax obligations does it handle for cross-border sales?
**SD-07** [Tax]: Does Lemon Squeezy collect and remit VAT/IVA for purchases made by LatAm buyers?
**SD-08** [Tax]: What tax forms (W-8BEN, W-8BEN-E, W-9) does Lemon Squeezy require for non-US (LatAm) sellers?
**SD-09** [Tax]: Under what conditions does Lemon Squeezy issue 1099-K forms?
**SD-10** [Tax]: Is US withholding tax applied to payouts to non-US (LatAm) merchants? At what rate?
**SD-11** [Tax]: Does Lemon Squeezy reference tax treaty effects for any LatAm countries?
**SD-12** [Availability]: Which LatAm countries appear in the Lemon Squeezy bank payout supported countries list?
**SD-13** [Availability]: Which LatAm countries are supported for PayPal payouts?
**SD-14** [Availability]: Are any LatAm countries on the Lemon Squeezy unsupported customer countries list?
**SD-15** [Availability]: Are LatAm-specific payment methods (PIX, Boleto, OXXO, Mercado Pago) supported for LatAm buyers?
**SD-16** [Availability]: What KYC/identity verification requirements exist for LatAm sellers?
**SD-17** [Payout]: What payout methods are available to non-US (LatAm) sellers (bank, PayPal, Payoneer, Wise)?
**SD-18** [Payout]: What are the bank payout fees for international (non-US) sellers vs US sellers?
**SD-19** [Payout]: What are the PayPal payout fees for international sellers vs US sellers?
**SD-20** [Payout]: What is the payout timing and minimum threshold for LatAm sellers?
**SD-21** [Payout]: Can non-US sellers use Wise or Payoneer accounts for Lemon Squeezy payouts?
**SD-22** [Availability]: Is VES (Venezuelan Bolívar) supported as a store display currency?
**SD-23** [Currency]: Does Lemon Squeezy support multi-currency wallets for sellers?
**SD-24** [Availability]: What seller experiences are reported by LatAm-based sellers using Lemon Squeezy (April 2025–April 2026)?

---

## Part 1 — Clean Findings (direct_verified)

---

**F-01**
- **Dimension:** Payout
- **What:** Lemon Squeezy bank payout fees for international (non-US) users are 1%; US bank payouts are free (0%).
- **Verbatim snippet:** "Lemon Squeezy has slashed its fees for stores that get payouts via Stripe. Payouts to U.S. bank accounts will now be free, while international users will pay 1%."
- **Source:** https://www.indiehackers.com/post/tech/lemon-squeezy-is-slashing-its-payout-fees-so-long-as-you-use-stripe-s5aeYKsIj9dWWq7TlaBb
- **source_type:** article
- **verification_status:** direct_verified
- **Date:** October 24, 2024
- **Notes:** Article by Katie Hignett (Indie Hackers). Edge 1 applied: journalism article = single-source (article). "International" means non-US in this context. Effective October 28, 2024 per same article. Applies to all LatAm sellers using bank payouts.

---

**F-02**
- **Dimension:** Payout
- **What:** Lemon Squeezy charges a flat fee of $0.50 for US PayPal payouts and 3% (up to $30) for international PayPal payouts.
- **Verbatim snippet:** "Lemon Squeezy will still charge a flat fee of $0.50 for U.S. payouts sent through Paypal, and 3% (up to $30) for international accounts."
- **Source:** https://www.indiehackers.com/post/tech/lemon-squeezy-is-slashing-its-payout-fees-so-long-as-you-use-stripe-s5aeYKsIj9dWWq7TlaBb
- **source_type:** article
- **verification_status:** direct_verified
- **Date:** October 24, 2024
- **Notes:** Same article as F-01 (Katie Hignett). Separate continuous passage covering PayPal-specific payout fees. The 3% cap at $30 applies to LatAm sellers choosing PayPal.

---

**F-03**
- **Dimension:** Payout
- **What:** Previous Lemon Squeezy bank payout fees were 0.5% + $2.50 for US users and 3% + $2.50 for international users.
- **Verbatim snippet:** "It's a major drop for both U.S. and international users, who previously sacrificed 0.5% + $2.50 or 3% + $2.50 of to access their income, respectively."
- **Source:** https://www.indiehackers.com/post/tech/lemon-squeezy-is-slashing-its-payout-fees-so-long-as-you-use-stripe-s5aeYKsIj9dWWq7TlaBb
- **source_type:** article
- **verification_status:** direct_verified
- **Date:** October 24, 2024
- **Notes:** Same article as F-01/F-02. "Respectively" maps 0.5% + $2.50 to US, 3% + $2.50 to international. These were the fees prior to the October 28, 2024 reduction.

---

**F-04**
- **Dimension:** Tax
- **What:** As a merchant of record, Lemon Squeezy calculates and pays global sales tax for digital products, handling legal processing and fees in every country.
- **Verbatim snippet:** "As a merchant of record, Lemon Squeezy calculates and pays global sales tax for digital products, handling legal processing and fees in every country. It primarily serves SaaS and software businesses."
- **Source:** https://techcrunch.com/2024/07/26/stripe-acquires-payment-processing-startup-lemon-squeezy/
- **source_type:** article
- **verification_status:** direct_verified
- **Date:** July 26, 2024
- **Notes:** TechCrunch article on Stripe's acquisition of Lemon Squeezy. Edge 1 applied: journalism article = single-source (article). "In every country" encompasses LatAm countries. Does not name specific LatAm jurisdictions or IVA.

---

**F-05**
- **Dimension:** Currency
- **What:** Lemon Squeezy charges an additional +1.5% for international transactions on top of its standard platform fee.
- **Verbatim snippet:** [Stated in layout: "Additional Fees: +1.5% for international transactions, +1.5% for PayPal transactions, +0.5% for subscription payments"]
- **Source:** https://sourcefees.com/detail/lemonsqueezy
- **source_type:** article
- **verification_status:** direct_verified
- **Date:** Accessed April 2026; page undated
- **Notes:** Third-party fee aggregation site. The +1.5% international fee applies when the buyer is outside the US per Lemon Squeezy's official documentation (see F-P15). The +1.5% PayPal and +0.5% subscription fees in the same layout element are not cross-border-specific.

---

**F-06**
- **Dimension:** Currency
- **What:** Lemon Squeezy's real cost can push into the 10–18% range when including extra charges for subscriptions, PayPal, international payments, affiliates, and cart recovery.
- **Verbatim snippet:** "Lemon Squeezy markets 5% + 50¢, but the real cost often runs higher. Extra charges for subscriptions, PayPal, international payments, affiliates, and cart recovery can push fees into the 10-18% range."
- **Source:** https://freemius.com/lemon-squeezy-alternative/
- **source_type:** article
- **verification_status:** direct_verified
- **Date:** Accessed April 2026; page undated
- **Notes:** Freemius is a direct competitor to Lemon Squeezy. The 10–18% range is their calculation, not Lemon Squeezy's stated figure. "International payments" references the cross-border surcharge. Treat with caution as a competitor source.

---

## Part 2 — Provisional Findings (blocked_url_index_verified)

All docs.lemonsqueezy.com and lemonsqueezy.com pages returned HTTP 403 on direct fetch attempts. Content below was verified via Google search engine index snippets of the same URLs. All lemonsqueezy.nolt.io pages also returned 403; content verified via search index snippets.

---

**F-P01**
- **Dimension:** Currency
- **What:** Lemon Squeezy processes all transactions in USD using real-time, mid-market exchange rates. No additional fees are charged for this conversion.
- **Verbatim snippet:** "Although we display your products in one of the many currencies we offer, ultimately we charge your customers the equivalent cost in USD. We do this using real-time, mid-market exchange rates to convert purchases to USD for processing. We do not charge any additional fees for this conversion."
- **Source:** https://docs.lemonsqueezy.com/help/payments/currencies
- **source_type:** help_center
- **verification_status:** blocked_url_index_verified
- **Date:** Accessed April 2026; page undated
- **Notes:** Page returned 403. Content verified via search engine index. USD-centric processing is the core cross-border FX mechanism. LatAm buyers see local-currency prices but are charged the USD equivalent.

---

**F-P02**
- **Dimension:** Currency
- **What:** Payouts are always made in USD. Sellers can select a non-USD payout currency for bank payouts, which is converted at the mid-market exchange rate at the time of payout.
- **Verbatim snippet:** "Payouts are always made in USD. If you set up bank payouts, you can select a payout currency (we recommend this matches your bank account). If you select a currency other than USD, our payout processor will convert the payout amount to your selected currency using the mid-market exchange rate at the time of payout."
- **Source:** https://docs.lemonsqueezy.com/help/payments/currencies
- **source_type:** help_center
- **verification_status:** blocked_url_index_verified
- **Date:** Accessed April 2026; page undated
- **Notes:** Page returned 403. Content verified via search engine index. "Mid-market exchange rate" implies no additional FX markup at payout. LatAm sellers selecting MXN, BRL, ARS, COP, etc. as payout currency would receive conversion at this rate.

---

**F-P03**
- **Dimension:** Currency
- **What:** Lemon Squeezy supports 14 LatAm currencies for store display: ARS (Argentine Peso), BOB (Boliviano), BRL (Brazilian Real), CLP (Chilean Peso), COP (Colombian Peso), CRC (Costa Rican Colon), DOP (Dominican Peso), GTQ (Guatemalan Quetzal), HNL (Honduran Lempira), MXN (Mexican Peso), NIO (Nicaraguan Córdoba), PEN (Peruvian Nuevo Sol), PYG (Paraguayan Guarani), and UYU (Uruguayan Peso). VES (Venezuelan Bolívar) is absent.
- **Verbatim snippet:** [Stated in layout: currency list of 130+ items including "ARS - Argentine Peso", "BOB - Boliviano", "BRL - Brazilian Real", "CLP - Chilean Peso", "COP - Colombian Peso", "CRC - Costa Rican Colon", "DOP - Dominican Peso", "GTQ - Guatemalan Quetzal", "HNL - Honduran Lempira", "MXN - Mexican Peso", "NIO - Nicaraguan Córdoba", "PEN - Peruvian Nuevo Sol", "PYG - Paraguayan Guarani", "UYU - Uruguayan Peso"; list ends at "ZMW - Zambian Kwacha" with no VES entry between UZS and VND]
- **Source:** https://docs.lemonsqueezy.com/help/payments/currencies
- **source_type:** help_center
- **verification_status:** blocked_url_index_verified
- **Date:** Accessed April 2026; page undated
- **Notes:** Page returned 403. Individual currencies confirmed via multiple search engine index queries targeting the same URL's content. VES absence confirmed by observing the alphabetical list jumps from "UZS - Uzbekistan Som" to "VND - Vietnamese Dong."

---

**F-P04**
- **Dimension:** Tax
- **What:** Lemon Squeezy is the merchant of record for all sales, handling collection and remittance of sales tax including international tax like VAT so sellers do not need to manage it.
- **Verbatim snippet:** "Lemon Squeezy is known as the merchant of record for all sales through our platform. That means we take care of a lot of the headaches that are normally associated with selling goods online. For example, you don't have to worry about collecting and remitting sales tax (including international tax like VAT) as Lemon Squeezy simply takes care of it for you. This is possible because Lemon Squeezy is technically selling products on your behalf and therefore we are liable for all of the complicated bits."
- **Source:** https://docs.lemonsqueezy.com/help/payments/sales-tax-vat
- **source_type:** help_center
- **verification_status:** blocked_url_index_verified
- **Date:** Accessed April 2026; page undated
- **Notes:** Page returned 403. Content from search engine index. "International tax like VAT" is the cross-border mechanism. The page does not use the term "IVA" (standard LatAm term for VAT).

---

**F-P05**
- **Dimension:** Tax
- **What:** When sales tax has been applied to an order, Lemon Squeezy deducts it from the seller's next payout and then reports and remits it.
- **Verbatim snippet:** "Sales tax will appear in your orders and invoices in Lemon Squeezy so you can see when we've charged sales tax. If sales tax has been applied to an order, we will deduct it from your next payout so that we can report and remit it."
- **Source:** https://docs.lemonsqueezy.com/help/payments/sales-tax-vat
- **source_type:** help_center
- **verification_status:** blocked_url_index_verified
- **Date:** Accessed April 2026; page undated
- **Notes:** Page returned 403. Content from search engine index. This mechanism applies to all cross-border sales. For a US buyer purchasing from a LatAm seller, US sales tax collected by LS would be deducted and remitted by LS.

---

**F-P06**
- **Dimension:** Tax
- **What:** Non-US merchants and affiliates on Lemon Squeezy are required to complete a Form W-8, which includes name, tax classification, and country of residence to establish identity and non-US person status.
- **Verbatim snippet:** "Non-US merchants and affiliates are required to complete a Form W-8, which includes some basic information about you, such as your name, tax classification, and country of residence. The purpose of the Form W-8 is to establish your identity and status as a non-U.S. person."
- **Source:** https://docs.lemonsqueezy.com/help/tax-forms
- **source_type:** help_center
- **verification_status:** blocked_url_index_verified
- **Date:** Accessed April 2026; page undated
- **Notes:** Page returned 403. Content from search engine index. W-8 encompasses W-8BEN (individuals) and W-8BEN-E (entities). This applies to all LatAm-based sellers.

---

**F-P07**
- **Dimension:** Tax
- **What:** Lemon Squeezy payouts may be blocked or paused if required tax information is missing. Funds cannot be transferred externally, but payments continue to be received.
- **Verbatim snippet:** "Payouts may be blocked or paused if we are missing required tax information. Funds cannot be transferred externally, but payments will continue to be received."
- **Source:** https://docs.lemonsqueezy.com/help/tax-forms
- **source_type:** help_center
- **verification_status:** blocked_url_index_verified
- **Date:** Accessed April 2026; page undated
- **Notes:** Page returned 403. Content from search engine index. Directly impacts LatAm sellers who have not yet submitted W-8BEN or W-8BEN-E forms. Sales accumulate but cannot be paid out until tax documentation is complete.

---

**F-P08**
- **Dimension:** Tax
- **What:** US-based Lemon Squeezy sellers (or those who completed a W-9) receive a 1099-K if they exceeded $20,000 USD in gross volume and 200 transactions in the previous calendar year.
- **Verbatim snippet:** "If you meet all the criteria below for the previous calendar year, you will receive a 1099-K from Lemon Squeezy: The account is based in the US (or has completed a Form W-9) More than $20,000 USD in gross volume from sales of goods or services in the previous calendar year"
- **Source:** https://docs.lemonsqueezy.com/help/tax-forms
- **source_type:** help_center
- **verification_status:** blocked_url_index_verified
- **Date:** Accessed April 2026; page undated
- **Notes:** Page returned 403. Content from search engine index. The 1099-K applies only to US-based accounts or W-9 filers. Non-US (LatAm) sellers completing W-8 forms do not receive 1099-K. Snippet truncated; the >200 transaction criterion is stated separately on the same page.

---

**F-P09**
- **Dimension:** Tax
- **What:** The Form W-8 is used by foreign individuals and entities to certify their foreign status for U.S. tax purposes, declaring they are not U.S. persons.
- **Verbatim snippet:** "The Form W-8 is used by foreign individuals and entities to certify their foreign status for U.S. tax purposes, allowing them to declare that they are not U.S. persons and are not subject to U.S. taxation."
- **Source:** https://docs.lemonsqueezy.com/help/tax-forms/w8-w9-forms
- **source_type:** help_center
- **verification_status:** blocked_url_index_verified
- **Date:** Accessed April 2026; page undated
- **Notes:** Page returned 403. Content from search engine index. This is the form required for all LatAm sellers. The phrase "not subject to U.S. taxation" appears in the form's purpose description; actual tax treatment may differ based on income characterization and treaty.

---

**F-P10**
- **Dimension:** Payout
- **What:** PayPal payouts from Lemon Squeezy are made in USD. PayPal may charge the recipient a fee to convert or withdraw.
- **Verbatim snippet:** "Bank payouts will be made in USD. For bank payouts to a currency other than USD, the total will be converted to your chosen currency. PayPal payouts will be made in USD. Note that PayPal may charge you a fee to convert or withdraw your money once it's in your PayPal account."
- **Source:** https://docs.lemonsqueezy.com/help/getting-started/getting-paid
- **source_type:** help_center
- **verification_status:** blocked_url_index_verified
- **Date:** Accessed April 2026; page undated
- **Notes:** Page returned 403. Content from search engine index. LatAm sellers receiving PayPal payouts get USD; subsequent conversion to MXN, BRL, ARS, COP, etc. would occur within PayPal at PayPal's own rates, which are not controlled by Lemon Squeezy.

---

**F-P11**
- **Dimension:** Availability
- **What:** PayPal payouts on Lemon Squeezy are supported in 200+ countries and regions.
- **Verbatim snippet:** "PayPal payouts are supported in 200+ countries and regions."
- **Source:** https://docs.lemonsqueezy.com/help/getting-started/supported-countries
- **source_type:** help_center
- **verification_status:** blocked_url_index_verified
- **Date:** Accessed April 2026; page undated
- **Notes:** Page returned 403. Content from search engine index. 200+ countries encompasses all major LatAm countries. This is the broadest payout availability mechanism for LatAm sellers who may not have bank payout support.

---

**F-P12**
- **Dimension:** Availability
- **What:** LatAm countries confirmed in the Lemon Squeezy bank payout supported countries list include Argentina, Bolivia, Chile, Colombia, Costa Rica, Dominican Republic, Ecuador, El Salvador, Guatemala, Guyana, Jamaica, and Mexico.
- **Verbatim snippet:** [Stated in layout: bank payout country list including "Argentina · ... · Bolivia · Bosnia and Herzegovina · Botswana · Brunei Darussalam · ... · Chile · Colombia · Costa Rica · ... · Dominican Republic · Ecuador · ... · El Salvador · ... · Guatemala · Guyana · ... · Jamaica · ... · Mexico"]
- **Source:** https://docs.lemonsqueezy.com/help/getting-started/supported-countries
- **source_type:** help_center
- **verification_status:** blocked_url_index_verified
- **Date:** Accessed April 2026; page undated
- **Notes:** Page returned 403. Country list partially recovered from cached/translated version. Full list contains 79 bank payout countries. Brazil is notably absent from the visible alphabetical sequence (list reads "Bolivia · Bosnia and Herzegovina · Botswana · Brunei Darussalam" with no Brazil between Bolivia and Botswana). Peru, Uruguay, Paraguay, Venezuela, Honduras, Nicaragua, and Panama were not confirmed in the visible portion of the list.

---

**F-P13**
- **Dimension:** Availability
- **What:** Lemon Squeezy accepts purchases from all countries except 18 listed as unsupported. No Latin American country appears on the unsupported list.
- **Verbatim snippet:** "We cannot accept payments from customers in the following countries: Central African Republic · Cuba · Democratic People's Republic of Korea · Democratic Republic of the Congo · Eritrea · Guinea-Bissau · Iran · Iraq · Lebanon · Libya · Mali · North Korea · Russian Federation · Somalia · South Sudan · Sudan · Syrian Arab Republic · Yemen"
- **Source:** https://docs.lemonsqueezy.com/help/getting-started/supported-countries
- **source_type:** help_center
- **verification_status:** blocked_url_index_verified
- **Date:** Accessed April 2026; page undated
- **Notes:** Page returned 403. Content from search engine index. The complete unsupported list is 18 countries. No LatAm country is listed, confirming LatAm buyers can purchase on Lemon Squeezy.

---

**F-P14**
- **Dimension:** Payout
- **What:** Lemon Squeezy bank payouts are converted to the seller's local currency using the mid-market exchange rate at the time of payout.
- **Verbatim snippet:** "Payouts made using bank transfers will be converted to your local currency using the mid-market exchange rate at the time of payout."
- **Source:** https://docs.lemonsqueezy.com/help/getting-started/getting-paid
- **source_type:** help_center
- **verification_status:** blocked_url_index_verified
- **Date:** Accessed April 2026; page undated
- **Notes:** Page returned 403. Content from search engine index. "Your local currency" applies to LatAm sellers receiving payouts in MXN, BRL, ARS, COP, CLP, PEN, etc. Corroborates F-P02 from a different LS docs page.

---

**F-P15**
- **Dimension:** Currency
- **What:** Lemon Squeezy adds +1.5% for international (outside of the US) transactions to the platform fee.
- **Verbatim snippet:** "There are certain times when an additional fee might be added to the platform fee to cover processing fees: +1.5% for international (outside of the US) transactions"
- **Source:** https://docs.lemonsqueezy.com/help/getting-started/fees
- **source_type:** help_center
- **verification_status:** blocked_url_index_verified
- **Date:** Accessed April 2026; page undated
- **Notes:** Page returned 403. Content from search engine index. The same page provides an example using "someone in France (20% VAT)" as the buyer, confirming the fee is triggered by the buyer's location outside the US, not the seller's location. This means: US seller → LatAm buyer = +1.5% applies; LatAm seller → US buyer = +1.5% does NOT apply.

---

**F-P16**
- **Dimension:** Payout
- **What:** Lemon Squeezy set payout fees at 0% per payout for US bank accounts and 1% per payout for bank accounts outside the US.
- **Verbatim snippet:** "New payout fees are now 0% per payout for bank accounts in the US and 1% per payout for bank accounts outside the US."
- **Source:** https://www.lemonsqueezy.com/blog/payout-fees-sliced
- **source_type:** blog
- **verification_status:** blocked_url_index_verified
- **Date:** October 22, 2024
- **Notes:** Blog post by JR Farr (CEO). Page returned 403. Content from search engine index. Corroborates F-01 from the official Lemon Squeezy source. The same blog states effective date as "Starting October 28th (next payout cycle)."

---

**F-P17**
- **Dimension:** Payout
- **What:** A Lemon Squeezy user reports that adding a Wise USD account was not accepted by Stripe, but a Wise IBAN account works for receiving payouts.
- **Verbatim snippet:** "Tried to add Wise USD account but seems like Stripe is not accepting it but on the other hand Wise IBAN account is working fine"
- **Source:** https://lemonsqueezy.nolt.io/519
- **source_type:** seller_forum
- **verification_status:** blocked_url_index_verified
- **Date:** Accessed April 2026; page undated
- **Notes:** Page returned 403. Content from search engine snippet. Anonymous user on Nolt feedback board. Single speaker (multi-speaker split applied). Relevant to LatAm sellers who commonly use Wise for international USD receipts. User-reported experience, not confirmed by Lemon Squeezy.

---

**F-P18**
- **Dimension:** Payout
- **What:** A user states it is not possible to avoid payout fees by receiving payouts to USD accounts (Wise or Revolut) if the business is based outside the US.
- **Verbatim snippet:** "As I understand it it's also not possible to avoid the fees by receiving payouts to USD accounts (Wise or Revolut for example) if your business is based outside of the US."
- **Source:** https://lemonsqueezy.nolt.io/519
- **source_type:** seller_forum
- **verification_status:** blocked_url_index_verified
- **Date:** Accessed April 2026; page undated
- **Notes:** Page returned 403. Content from search engine snippet. Anonymous user, separate speaker from F-P17 (multi-speaker split applied). Prefixed with "As I understand it" indicating user interpretation, not confirmed policy.

---

**F-P19**
- **Dimension:** Availability
- **What:** A Lemon Squeezy user requests support for PIX, multiple installments, and boleto to open the Brazilian market for creators.
- **Verbatim snippet:** "Allow other payment methods that fits the Brazilian market like Pix, multiple installments, and boleto. This would open a huge market for Brazilian creators."
- **Source:** https://lemonsqueezy.nolt.io/583
- **source_type:** seller_forum
- **verification_status:** blocked_url_index_verified
- **Date:** Accessed April 2026; page undated
- **Notes:** Page returned 403. Content from search engine snippet. Anonymous feature request. The request implies PIX, boleto, and installment payments are not currently supported on Lemon Squeezy for Brazilian buyers.

---

**F-P20**
- **Dimension:** Availability
- **What:** A user states the lack of PIX is a reason they have not migrated to Lemon Squeezy, as PIX is the payment method they receive most from Brazilian customers.
- **Verbatim snippet:** "PIX would be great for me too. One of the reasons that still makes me think about migrating to this platform is the lack of PIX, because it is the payment method I receive most from Brazilian customers on my current system."
- **Source:** https://lemonsqueezy.nolt.io/583
- **source_type:** seller_forum
- **verification_status:** blocked_url_index_verified
- **Date:** Accessed April 2026; page undated
- **Notes:** Page returned 403. Content from search engine snippet. Anonymous user, separate speaker from F-P19 (multi-speaker split applied). Mentions "Brazilian customers" explicitly.

---

**F-P21**
- **Dimension:** Payout
- **What:** Lemon Squeezy users request Payoneer as a payout option, which is not currently available.
- **Verbatim snippet:** "Add support for Payoneer payouts."
- **Source:** https://lemonsqueezy.nolt.io/5
- **source_type:** seller_forum
- **verification_status:** blocked_url_index_verified
- **Date:** Accessed April 2026; page undated
- **Notes:** Page returned 403. Content from search engine snippet. Feature request. The existence of this request implies Payoneer is not currently a supported payout method. Payoneer is widely used in LatAm for receiving international payments.

---

## Part 3 — Pattern Candidates (sealed)

---

**PC-01**
Findings F-P01, F-P02, F-P10, F-P14 describe a USD-centric payment architecture where all transactions are processed in USD regardless of store display currency, all payouts are denominated in USD, and conversion to local currency occurs at the payout stage using mid-market exchange rates.

**PC-02**
Findings F-P06, F-P07, F-P08, F-P09 describe a tax documentation gate where non-US sellers must complete W-8 forms before payouts are enabled, with payout blocking as the enforcement mechanism for tax compliance.

**PC-03**
Findings F-P19, F-P20 describe an absence of LatAm-specific buyer payment methods (PIX, boleto, installments) on Lemon Squeezy, referenced by users targeting the Brazilian market.

**PC-04**
Findings F-01, F-02, F-05, F-P15, F-P16 describe a layered cross-border fee structure where international transactions incur a +1.5% buyer-location-based surcharge at checkout and a separate percentage-based payout fee differential (1% bank / 3% PayPal for non-US vs 0% / $0.50 for US).

**PC-05**
Findings F-P17, F-P18, F-P21 describe limitations in payout method flexibility for non-US sellers: Wise USD accounts are reported as not accepted by Stripe, international payout fees cannot be avoided by using USD-denominated third-party accounts, and Payoneer is not a supported payout method.

---

## Part 4 — Could Not Verify / Out-of-Scope

---

**F-X01:** US withholding tax rates for LatAm W-8BEN filers
No Lemon Squeezy documentation was found specifying withholding tax rates applied to payouts to non-US sellers. The W-8 form guidance describes establishing foreign status but does not state a withholding percentage. Standard IRS rules (30% default, reducible by treaty) may apply but are not confirmed in LS-specific sources.
Verbatim: n/a — absence finding
Source: Searches attempted on docs.lemonsqueezy.com/help/tax-forms, docs.lemonsqueezy.com/help/tax-forms/w8-w9-forms, web searches for "lemon squeezy" withholding tax, "lemon squeezy" "30%" withholding.

**F-X02:** Tax treaty effects for LatAm countries
No Lemon Squeezy documentation references tax treaties with any specific country, including LatAm countries (Mexico, Brazil, Colombia, Argentina, Chile, etc.). No mention of reduced withholding rates under bilateral tax treaties.
Verbatim: n/a — absence finding
Source: Searches attempted on docs.lemonsqueezy.com tax pages, web searches for "lemon squeezy" "tax treaty", "lemon squeezy" W-8BEN treaty benefits.

**F-X03:** IVA (Latin American VAT) terminology in Lemon Squeezy documentation
No Lemon Squeezy page uses the term "IVA." All references are to "VAT" or "sales tax" generically. It cannot be confirmed whether Lemon Squeezy charges IVA specifically in LatAm jurisdictions or what rates apply.
Verbatim: n/a — absence finding
Source: Searches attempted on docs.lemonsqueezy.com/help/payments/sales-tax-vat, web searches for "lemonsqueezy" IVA, site:docs.lemonsqueezy.com IVA.

**F-X04:** Brazil bank payout support status
Brazil was not visible in the partially recovered bank payout country list from the supported-countries page. The alphabetical list reads "Bolivia · Bosnia and Herzegovina · Botswana · Brunei Darussalam" with no Brazil entry between Bolivia and Botswana/Brunei. Brazil's bank payout support status could not be confirmed or denied due to partial list recovery.
Verbatim: n/a — absence finding (partial data)
Source: https://docs.lemonsqueezy.com/help/getting-started/supported-countries (403; partial list from search index).

**F-X05:** Peru, Uruguay, Paraguay, Venezuela, Honduras, Nicaragua, Panama bank payout support
These countries were not confirmed in the visible portion of the bank payout country list. The full 79-country list could not be retrieved due to the 403 block and search snippet truncation.
Verbatim: n/a — absence finding (partial data)
Source: https://docs.lemonsqueezy.com/help/getting-started/supported-countries (403; partial list from search index).

**F-X06:** Country-specific payout timing differences for LatAm
No evidence found that payout timing varies by country. The standard schedule (created 1st/15th, paid 14th/28th, 13-day hold, 1–5 day bank transit) appears to apply uniformly. No LatAm-specific timing data found.
Verbatim: n/a — absence finding
Source: https://docs.lemonsqueezy.com/help/getting-started/getting-paid (403; search index content reviewed).

**F-X07:** KYC/verification requirements specific to LatAm countries
No LatAm-specific KYC or verification requirements found in Lemon Squeezy documentation. General verification ("you may be asked to verify your identity for fraud prevention") is mentioned. A Thai seller's account verification difficulty was documented on devmystify.com (October 2025) but is not LatAm-specific and was therefore excluded from D6 scope.
Verbatim: n/a — absence finding
Source: Searches attempted on docs.lemonsqueezy.com help pages, web searches for "lemon squeezy" KYC verification Latin America.

**F-X08:** LatAm-based seller experiences with Lemon Squeezy (April 2025–April 2026)
No Reddit posts, Indie Hackers posts, blog posts, or forum discussions from LatAm-based sellers describing their cross-border experience with Lemon Squeezy were found within the April 2025–April 2026 time window. All Reddit searches (site:reddit.com with LatAm country names, currency codes, "lemon squeezy") returned zero results. One Threads post in Spanish by an Argentine user (@devcarreras) was found but excluded per English-language-only scope.
Verbatim: n/a — absence finding
Source: 12 Reddit search queries, 2 Indie Hackers search queries, 3 general web searches for LatAm seller experiences. All returned zero LatAm-specific results.

---

## Research QA Notes

### Forced-provisional
All 21 Part 2 findings are blocked_url_index_verified because every docs.lemonsqueezy.com, lemonsqueezy.com, and lemonsqueezy.nolt.io page returned HTTP 403 on direct fetch. Content was verified solely through Google search engine index snippets. Archive.org versions were also inaccessible. This significantly reduced the Clean finding count (6) below the expected 15–25. The verification bar was not lowered; findings were classified conservatively.

### Degraded
F-P03 (LatAm currency list): The full 130-currency list could not be viewed as a single continuous passage due to search snippet truncation. Individual LatAm currencies were confirmed via multiple targeted search queries against the same URL. The VES absence was confirmed by observing the alphabetical sequence gap (UZS → VND). Degraded from a single-list finding to a composite confirmation.

F-P12 (LatAm bank payout countries): The full 79-country list was not recoverable. Only a partial alphabetical sequence was visible. Several LatAm countries (Brazil, Peru, Uruguay, Paraguay, Venezuela, Honduras, Nicaragua, Panama) could not be confirmed present or absent. Finding reflects only the confirmed portion.

### URL-not-fixable
All 10 primary Lemon Squeezy URLs and 2 Archive.org fallback URLs are unfetchable. The 403 block appears domain-wide for both docs.lemonsqueezy.com and lemonsqueezy.com. This is a systemic access limitation, not a per-page issue.

### Multi-speaker splits
F-P17 and F-P18: Split from lemonsqueezy.nolt.io/519 (two distinct anonymous speakers).
F-P19 and F-P20: Split from lemonsqueezy.nolt.io/583 (two distinct anonymous speakers). A third speaker on the same page ("I need to use pix too. Without it i can't use your service.") was omitted as it added minimal incremental information beyond F-P19 and F-P20.

### Truncations
F-P08 (1099-K criteria): The search snippet truncated before the ">200 transactions" criterion. This criterion was confirmed from a separate search query on the same page and noted in the finding.
F-P03 (currency list): Search snippet displayed partial alphabetical ranges. Full list not recovered.
F-P12 (bank payout countries): List truncated at approximately the letter M in the alphabetical sequence.

### source_type ambiguities
F-P17/F-P18/F-P19/F-P20/F-P21: Nolt.io feedback boards mapped to seller_forum. Nolt is a product feedback/feature-request platform, not a traditional seller forum. seller_forum is the closest match in the 18-value taxonomy.
F-05: sourcefees.com mapped to article. It is a third-party fee comparison site, not journalism. article is the closest match.
F-06: freemius.com competitor comparison page mapped to article.

### Coverage gaps
1. **Brazil bank payout status** (F-X04): Could not confirm whether Brazil is in the 79-country bank payout list. This is a critical gap for the LatAm↔US corridor given Brazil's market size.
2. **Withholding tax rates** (F-X01/F-X02): No LS-specific data on US withholding rates or tax treaty effects for any LatAm country. This is a material gap for LatAm sellers evaluating net payout amounts.
3. **IVA handling** (F-X03): No confirmation that LS charges IVA specifically in LatAm jurisdictions or at correct country-specific rates.
4. **LatAm seller experiences** (F-X08): Zero English-language LatAm-specific seller testimonials found in any source within the time window. This limits the experiential evidence for this shard to platform documentation and community feature requests only.
5. **Multi-currency wallet support** (SD-23): No evidence found. Lemon Squeezy appears to operate on a single-store-currency model with USD settlement. No multi-currency wallet feature was mentioned in any source.

### Decomposition limitations
SD-10 (withholding tax rates), SD-11 (tax treaty effects), and SD-16 (LatAm-specific KYC) yielded no findings. These sub-searches were valid decompositions of the shard scope but the underlying data does not exist in publicly accessible Lemon Squeezy documentation. These are genuine documentation gaps, not decomposition errors.

### Edge cases applied
Edge 1: F-01, F-02, F-03 (IndieHackers article by Katie Hignett), F-04 (TechCrunch article) — journalism articles citing Lemon Squeezy as source = single-source (article).
Edge 3: All docs.lemonsqueezy.com pages — URLs could not be accessed directly; content verified via search index → classified as blocked_url_index_verified, not direct_verified.
Edge 5: No ambiguous URLs (subreddit-level or domain-only) were used as sources.

### Reddit access
All 7 specific Reddit thread URLs (r/SaaS, r/developersIndia) referenced in third-party comparison sites were blocked (PERMISSIONS_ERROR). Old.reddit.com fallbacks were also blocked. 12 site:reddit.com search queries returned zero results for LatAm-specific Lemon Squeezy discussions. Reddit quotes cited by competitor comparison sites (Fungies.io, Freemius) were excluded per Edge 2 (secondary retelling = not single-source → not valid for Part 1 or 2).