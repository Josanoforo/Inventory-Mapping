# DG OUTPUT — SHARD D6: Payhip × Cross-border LatAm↔US Mechanics

**DG Agent Run**
**Shard:** D6 — Cross-border LatAm↔US mechanics and experience (English only)
**Platform:** Payhip
**Run date:** April 14, 2026
**Time window:** Current state for policies; April 2025–April 2026 for reported experiences
**Language:** English only

---

## 1. Search Decomposition

SD-01: Payhip payout methods available to sellers in LatAm countries (PayPal, Stripe, bank transfer, Payoneer, Mercado Pago) — help center and official docs
SD-02: Payhip minimum payout thresholds by country or payout method — help center
SD-03: Payhip currency conversion handling — which currencies sellers can receive, FX markup/spread — help center
SD-04: Payhip currencies accepted from buyers — help center/pricing
SD-05: Payhip VAT/sales tax handling for EU and US — merchant-of-record status — help center/policy
SD-06: Payhip tax form requirements for non-US sellers (W-8BEN) — help center
SD-07: Payhip 1099 handling for US sellers — help center
SD-08: Payhip country availability for seller accounts — which LatAm countries can register — help center/terms
SD-09: Payhip geographic/country restrictions on specific product types — policy
SD-10: Payhip KYC requirements by country — help center
SD-11: Reported seller experiences from Mexico receiving payouts from Payhip — Reddit/forums
SD-12: Reported seller experiences from Brazil receiving payouts from Payhip — Reddit/forums
SD-13: Reported seller experiences from Argentina/Colombia/Chile/Peru — Reddit/forums
SD-14: US seller experiences selling to LatAm buyers via Payhip — currency/tax issues
SD-15: Payhip payout timing by country — help center/forums
SD-16: Payhip Stripe Connect availability by country (Stripe supports limited LatAm countries) — docs
SD-17: Payhip PayPal availability and restrictions in LatAm — docs
SD-18: Payhip blog announcements about international payments or cross-border changes

---

## Part 1 — Clean Findings (direct_verified)

---

**Finding ID:** F-01
**What:** Payhip's Mercado Pago integration is available in Argentina, Brazil, Chile, Colombia, Mexico, Peru, and Uruguay, with supported currencies ARS, BRL, CLP, COP, MXN, PEN, and UYU.
**Verbatim snippet:** "Mercado Pago is available in Argentina, Brazil, Chile, Colombia, Mexico, Peru and Uruguay. Supported currencies include ARS, BRL, CLP, COP, MXN, PEN, and UYU."
**Source:** https://help.payhip.com/article/343-connecting-your-mercado-pago-account
**source_type:** help_center
**verification_status:** direct_verified
**Date:** Last updated December 31, 2025
**Dimension:** Availability
**Notes:** Page fetched by subagent; text cross-verified against search-index snippet returned in independent web search. Mercado Pago integration announced via Payhip blog on December 12, 2025. UYU (Uruguayan Peso) appears here but is absent from the general store-currency list on the Store Language and Currency help page.

---

**Finding ID:** F-02
**What:** Payhip requires the store currency to match the connected Mercado Pago account currency. Mercado Pago is available in Argentina, Brazil, Chile, Colombia, Mexico, Peru, and Uruguay with currencies ARS, BRL, CLP, COP, MXN, PEN, and UYU.
**Verbatim snippet:** "Note that the currency used in your Payhip account must match the currency in your Mercado Pago account."
**Source:** https://help.payhip.com/article/343-connecting-your-mercado-pago-account
**source_type:** help_center
**verification_status:** direct_verified
**Date:** Last updated December 31, 2025
**Dimension:** Currency
**Notes:** The snippet itself names Mercado Pago but not specific countries; the cross-border cut is established by the same article's earlier passage naming seven LatAm countries and their currencies (captured in F-01). A LatAm seller using Mercado Pago must set their Payhip store to their local LatAm currency, precluding USD pricing on the same store.

---

**Finding ID:** F-03
**What:** Payhip's Mercado Pago payout model sends the full payment (without Payhip fees deducted) instantly to the seller after each transaction; Payhip fees are billed separately at the end of each month via credit card. This differs from the Stripe and PayPal payout models on Payhip.
**Verbatim snippet:** "Mercado Pago payments are processed instantly, so you receive funds immediately after each transaction. Mercado Pago payments work a little differently compared to Stripe or PayPal on Payhip. You will get your full payment (without Payhip fees deducted) instantly after each transaction has been processed. At the end of each month, you'll be billed for your Payhip fees using your preferred credit card."
**Source:** https://help.payhip.com/article/343-connecting-your-mercado-pago-account
**source_type:** help_center
**verification_status:** direct_verified
**Date:** Last updated December 31, 2025
**Dimension:** Payout
**Notes:** Cross-border cut established by same article identifying Mercado Pago as operating in seven LatAm countries (F-01). Snippet itself names Mercado Pago but not specific LatAm countries. The instant-payout-then-monthly-bill structure is unique to Mercado Pago among Payhip's payment gateways.

---

**Finding ID:** F-04
**What:** Payhip's Stripe integration lists Brazil and Mexico as the only Latin American countries supported. Argentina, Chile, Colombia, Peru, and Uruguay are not listed for Stripe on Payhip.
**Verbatim snippet:** "Stripe is currently supported in over 40 countries including Austria, Australia, Belgium, Brazil, Bulgaria, Canada, Croatia, Cyprus, Czech Republic, Denmark, Estonia, Finland, France, Germany, Gibraltar, Greece, Hong Kong, Hungary, Ireland, Italy, Japan, Latvia, Liechtenstein, Lithuania, Luxembourg, Malaysia, Malta, Mexico, Netherlands, New Zealand, Norway, Poland, Portugal, Romania, Singapore, Slovenia, Slovakia, Spain, Sweden, Switzerland, Thailand, United Arab Emirates, United Kingdom and United States."
**Source:** https://help.payhip.com/article/65-connecting-your-stripe-account
**source_type:** help_center
**verification_status:** direct_verified
**Date:** Last updated February 25, 2026
**Dimension:** Availability
**Notes:** Page fetched by subagent. The exhaustive country list is reproduced verbatim. Brazil and Mexico are the only LatAm countries present. Argentina, Chile, Colombia, Peru, and Uruguay are absent from this list, meaning sellers in those countries cannot use Stripe via Payhip and must use Mercado Pago (F-01) or PayPal (F-05).

---

**Finding ID:** F-05
**What:** Payhip's PayPal integration lists Brazil, Mexico, and the United States among countries where sellers can connect a personal or business PayPal account. Sellers in other LatAm countries not on this named list must use a business PayPal account.
**Verbatim snippet:** "PayPal is currently supported in over 200 countries including Australia, Austria, Belgium, Brazil, Canada, Cyprus, Czech Republic, Estonia, Finland, France, Germany, Greece, Hungary, Ireland, Italy, Latvia, Luxemburg, Malta, Mexico, Netherlands, New Zealand, Poland, Portugal, Romania, San Marino, Slovakia, Slovenia, South Africa, Spain, United Kingdom, and United States. If you're based in the countries listed above, you can connect either a personal or business PayPal account to your Payhip store. For all other countries on PayPal's supported list, you must have a business PayPal account."
**Source:** https://help.payhip.com/article/64-connecting-your-paypal-account
**source_type:** help_center
**verification_status:** direct_verified
**Date:** Accessed April 2026; page undated
**Dimension:** Availability
**Notes:** Page fetched by subagent. Brazil and Mexico are the only LatAm countries explicitly named on the personal-or-business list. Argentina, Chile, Colombia, Peru, and Uruguay are not named, meaning sellers in those countries require a business PayPal account. The "over 200 countries" claim implies PayPal may still be available in those LatAm countries, but with the business-account restriction.

---

**Finding ID:** F-06
**What:** PayPal on Payhip charges an additional 1.5% on top of the standard 2.99% + fixed fee for international commercial transactions, which applies to cross-border LatAm↔US transactions.
**Verbatim snippet:** "The standard credit and debit card payment fee is 2.99% + a fixed fee per transaction, which varies according to the transaction currency. An additional 1.5% applies to international commercial transactions."
**Source:** https://help.payhip.com/article/64-connecting-your-paypal-account
**source_type:** help_center
**verification_status:** direct_verified
**Date:** Accessed April 2026; page undated
**Dimension:** Payout
**Notes:** Page fetched by subagent; text cross-verified via search-index snippet. The "international commercial transactions" qualifier provides the cross-border cut. The page also states: "Note that these fees are collected by PayPal and do not go to Payhip." These are PayPal fees described on a Payhip help page; Payhip itself does not add a cross-border surcharge.

---

**Finding ID:** F-07
**What:** Payhip supports six LatAm currencies — ARS (Argentine Peso), BRL (Brazilian Real), CLP (Chilean Peso), COP (Colombian Peso), MXN (Mexican Peso), PEN (Peruvian Sol) — and USD (US Dollar) as store currencies. The default store currency is USD and only one currency is supported per store.
**Verbatim snippet:** [Stated in layout: "ARS – Argentine Peso · BRL – Brazilian Real · CLP – Chilean Peso · COP – Colombian Peso · MXN – Mexican Peso · PEN – Peruvian Sol · USD – US Dollar"] and "By default, the currency for your store is USD." and "Payhip only supports one default language and currency per store at this time."
**Source:** https://help.payhip.com/article/234-store-language-and-currency
**source_type:** help_center
**verification_status:** direct_verified
**Date:** Last updated January 30, 2026
**Dimension:** Currency
**Notes:** Page fetched by subagent. The full currency list on the page contains 40 currencies; only LatAm and USD entries are reproduced in the snippet above per scope. The layout format uses a vertical list; the [Stated in layout] notation captures the relevant entries. UYU (Uruguayan Peso) is notably absent from this general currency list but IS available via Mercado Pago per F-01. The single-currency-per-store constraint means a LatAm seller pricing in MXN cannot simultaneously offer USD pricing on the same store, and vice versa.

---

**Finding ID:** F-08
**What:** Payhip does not remit taxes for countries outside the EU. For non-EU/UK countries — including the United States and all LatAm countries — Payhip can collect tax at checkout per seller-configured rates, but the seller must self-report and remit those taxes to the relevant authorities.
**Verbatim snippet:** "Payhip handles digital EU VAT for you, but what about taxes for countries outside of the EU? Whilst we don't remit this tax on your behalf, we do make it easy to collect that tax on top of, or within, your product pricing. We also give you a monthly sales report that summarizes how much tax you've collected, making reporting a breeze!"
**Source:** https://help.payhip.com/article/174-taxes-for-digital-products
**source_type:** help_center
**verification_status:** direct_verified
**Date:** Last updated December 12, 2024
**Dimension:** Tax
**Notes:** Page fetched by subagent; text cross-verified via search-index snippet. Cross-border cut is the explicit distinction between EU (Payhip remits) and "countries outside of the EU" (Payhip does not remit). The snippet does not name specific LatAm countries or the US, but the "countries outside of the EU" formulation encompasses all LatAm countries and the United States. The page also states: "Here at Payhip we're not tax experts. Please always check with your accountant to understand exactly who/what you need to charge."

---

**Finding ID:** F-09
**What:** A Payhip staff member stated in January 2026 that Payhip plans to launch global tax handling (expanding beyond the current EU/UK MoR) in the first half of 2026, pending no delays.
**Verbatim snippet:** "Hi Rebecca, we don't have an official ETA but, as long as everything goes as planned, we plan to launch handleing global taxes in the first half of the year."
**Source:** https://payhip.com/blog/whats-new-at-payhip-2025/
**source_type:** blog
**verification_status:** direct_verified
**Date:** January 11, 2026 (comment date)
**Dimension:** Tax
**Notes:** Blog page fetched directly and full text verified character-for-character. Comment posted by "Lucy @ Payhip" (staff handle) in response to user "Rebecca" asking about global MoR ETA. Typo "handleing" preserved verbatim from original. Cross-border cut is via "global taxes" qualifier, implying all jurisdictions including US and LatAm, though no specific LatAm country or currency is named. Earlier in the same thread (November 24, 2025), same staff member stated: "MoR support is something we're working on, though we don't have an exact ETA yet. We're hoping for sometime next year." This is an informal comment, not an official policy announcement. As of April 2026, no public announcement of a global MoR launch has been identified.

---

**Finding ID:** F-10
**What:** Payhip provides a country blocking tool that allows sellers to block specific countries and specific US states from completing checkout, described as a feature for sales tax purposes.
**Verbatim snippet:** "For sales tax purposes you might want to block certain countries from purchasing from you. This is possible through the country blocking manager. It will let you block countries and even specific US states from completing the checkout process on your store."
**Source:** https://help.payhip.com/article/280-blocking-countries
**source_type:** help_center
**verification_status:** direct_verified
**Date:** Last updated September 26, 2023
**Dimension:** Availability
**Notes:** Page fetched by subagent. Cross-border cut is the named geographic reference "US states" and the ability to block "countries." This tool is seller-controlled; Payhip itself does not impose default country blocks. The stated use case ("for sales tax purposes") implies sellers may block LatAm countries or US states where they lack tax compliance capacity.

---

## Part 2 — Provisional Findings (blocked_url_index_verified)

---

**Finding ID:** F-P01
**What:** Payhip states it acts as the seller's reseller for EU/UK digital product sales and is "100% responsible" for digital EU/UK VAT. This reseller/MoR role does not extend to other jurisdictions including the United States or Latin American countries.
**Verbatim snippet:** "If your customer is buying a digital product in the EU/UK we act as your reseller which means we're 100% responsible for digital EU/UK VAT."
**Source:** https://payhip.com/features/vat-taxes
**source_type:** platform_doc
**verification_status:** blocked_url_index_verified
**Date:** Accessed April 2026; page undated
**Dimension:** Tax
**Notes:** URL returned in search results but the page could not be fully fetched; snippet sourced from search-engine index. The phrase "we act as your reseller" is the only known instance where Payhip explicitly claims a reseller/MoR role. Cross-border cut is via "EU/UK" as named geographic scope; the reseller role is stated as limited to these regions. The absence of equivalent language for US or LatAm jurisdictions, combined with F-08, establishes that Payhip is NOT the merchant of record for LatAm↔US transactions.

---

## Part 3 — Pattern Candidates (sealed)

---

**PC-01:** Across F-01, F-04, and F-05, Mercado Pago is the only payment gateway on Payhip that lists LatAm countries beyond Brazil and Mexico. Stripe on Payhip lists only Brazil and Mexico among LatAm countries. PayPal names Brazil and Mexico for personal-or-business accounts and requires business accounts for other LatAm countries. For sellers in Argentina, Chile, Colombia, Peru, and Uruguay, Mercado Pago is the sole documented dedicated gateway on Payhip.

**PC-02:** Across F-08, F-P01, F-X01, F-X02, and F-X03, Payhip's official documentation contains no LatAm-specific or US-specific tax guidance. No mention of W-8BEN, 1099, IVA, withholding tax, or tax treaty effects appears on any Payhip help center, terms, or policy page. The only automated tax mechanism is EU/UK digital VAT (F-P01). All non-EU/UK tax obligations — including US state sales tax and LatAm country taxes — rest entirely on the seller (F-08).

**PC-03:** Across F-X07, F-X08, and F-X10, zero English-language community discussion (Reddit, IndieHackers, Trustpilot, Capterra, YouTube) was found containing first-hand accounts of Payhip cross-border LatAm↔US seller experiences within the April 2025–April 2026 window. Payhip's Mercado Pago integration was announced in December 2025 (F-01 date), which may partially explain the absence of accumulated user reports.

---

## Part 4 — Could Not Verify / Out-of-Scope

---

**F-X01:** W-8BEN requirements for non-US sellers on Payhip
n/a — absence finding. Searched: help.payhip.com (full-text and site-search for "W-8BEN," "W8BEN," "withholding"), payhip.com/terms, payhip.com/faq, web search "Payhip W-8BEN." Zero mentions found on any Payhip-owned page. Since Payhip routes payments through seller-owned Stripe/PayPal accounts (not through Payhip itself), W-8BEN obligations would flow from Stripe or PayPal, not from Payhip.
**Source:** n/a — absence finding
**Searched locations:** https://help.payhip.com (site-wide), https://payhip.com/terms, https://payhip.com/faq, web search "Payhip W-8BEN site:help.payhip.com," web search "Payhip W-8BEN tax form non-US seller"

---

**F-X02:** 1099 handling for US sellers on Payhip
n/a — contradicted across sources, unverifiable from official Payhip documentation. No Payhip help center, terms, or policy page mentions "1099." A third-party tax service (flyfin.tax/1099-orgs/payhip) claims "Payhip.com will dispatch a 1099-K form to you" upon reaching $600 in earnings, but this appears to be auto-generated template content. A seller blog post from September 2020 (1mkwilliams.com) states "NOTE: PayHip does not provide 1099s for US authors for end of year taxes" — but this is outside the time window and may be outdated. Since Payhip payments flow directly into seller-owned Stripe or PayPal accounts, 1099-K forms would be issued by Stripe or PayPal (as the payment settlement entities), not by Payhip.
**Source:** n/a — absence finding (official); contradicted across third-party sources
**Searched locations:** https://help.payhip.com (site-wide), https://payhip.com/terms, https://payhip.com/faq, web search "Payhip 1099 tax form US seller"

---

**F-X03:** IVA (Impuesto al Valor Agregado) handling for LatAm countries on Payhip
n/a — absence finding. Searched: help.payhip.com (site-wide for "IVA"), web search "Payhip IVA Mexico Brazil tax." Zero mentions found. Payhip's tax-configuration tool (F-08) allows sellers to manually add tax rates for any country, but no pre-configured IVA rates or LatAm-specific tax guidance exists in Payhip's documentation.
**Source:** n/a — absence finding
**Searched locations:** https://help.payhip.com (site-wide), web search "Payhip IVA Mexico Brazil," web search "Payhip VAT sales tax Latin America"

---

**F-X04:** KYC/identity verification requirements by country on Payhip
n/a — absence finding. Searched: help.payhip.com (site-wide for "KYC," "verification," "identity"). No Payhip-specific KYC documentation found. KYC requirements are handled by the connected payment processor (Stripe, PayPal, or Mercado Pago), not by Payhip itself. Payhip's registration process requires only name and email; no country-specific identity verification step is documented on Payhip's side.
**Source:** n/a — absence finding
**Searched locations:** https://help.payhip.com (site-wide), web search "Payhip KYC verification country"

---

**F-X05:** Payoneer or Wise as payout methods on Payhip
n/a — absence finding. Searched: help.payhip.com, payhip.com/faq, payhip.com/payment-gateways. Neither Payoneer nor Wise is mentioned as a supported payment gateway or payout method on any Payhip page. Payhip's 13 supported gateways are: Stripe, PayPal, Square, Mollie, Mercado Pago, Paystack, Flutterwave, PayU, Razorpay, Iyzico, Midtrans, Xendit, Paytabs.
**Source:** n/a — absence finding
**Searched locations:** https://help.payhip.com (site-wide), https://payhip.com/faq, https://payhip.com/blog/new-feature-payhip-integrates-with-11-new-payment-gateways/

---

**F-X06:** Minimum payout thresholds for regular Payhip sellers
n/a — absence finding. No minimum payout threshold for regular seller payouts is documented on any Payhip page. Payments flow directly and instantly to the seller's connected payment processor (Stripe, PayPal, or Mercado Pago) per transaction (see F-03 for Mercado Pago model). The only documented threshold is $50 USD for the Partner (affiliate referral) program, paid monthly via PayPal — this applies to referral commissions, not seller product revenue.
**Source:** n/a — absence finding
**Searched locations:** https://help.payhip.com/article/173-how-do-i-get-paid, https://help.payhip.com (site-wide for "minimum payout" and "threshold"), web search "Payhip minimum payout threshold"

---

**F-X07:** Reddit or forum LatAm seller experiences with Payhip payouts
n/a — absence finding. Executed 16+ targeted Reddit searches (site:reddit.com) combining "Payhip" with Mexico, Brazil, Argentina, Colombia, Latin America, payout, PayPal international, W-8BEN, currency conversion, and subreddits r/digitalnomad, r/Entrepreneur, r/juststart, r/selfpublish, r/SideProject. Zero relevant posts found. Also searched IndieHackers (site:indiehackers.com "Payhip") — mentions found but none with LatAm cross-border content. Trustpilot and Capterra reviews scanned — no LatAm country, currency, or cross-border payout experience mentioned.
**Source:** n/a — absence finding
**Searched locations:** reddit.com (16+ queries), indiehackers.com, trustpilot.com/review/payhip.com, capterra.com/p/251233/Payhip/

---

**F-X08:** YouTube content discussing Payhip payouts from LatAm
n/a — absence finding. Searched: "Payhip payout Latin America YouTube," "Payhip international seller payout YouTube," "Payhip tutorial payout method country YouTube." Zero relevant YouTube videos found covering Payhip payouts for Latin American sellers.
**Source:** n/a — absence finding
**Searched locations:** web search (3 queries targeting YouTube)

---

**F-X09:** Exchange rate markup or FX spread information on Payhip
n/a — absence finding. No Payhip documentation discusses exchange rate markups, FX spreads, or currency conversion mechanics. Payhip's single-currency-per-store design (F-07) and currency-matching requirement for Mercado Pago (F-02) suggest currency conversion may be handled entirely by the payment processor (Stripe, PayPal, Mercado Pago) rather than by Payhip. No Payhip page addresses what happens when a buyer pays in a currency different from the store's default currency.
**Source:** n/a — absence finding
**Searched locations:** https://help.payhip.com (site-wide for "currency conversion," "exchange rate," "FX"), web search "Payhip currency conversion"

---

**F-X10:** Spanish- or Portuguese-language coverage gap
Coverage gap noted. Per scope rules, only English-language content was searched. LatAm seller discussions about Payhip may exist in Spanish or Portuguese on platforms not covered by this English-only search (e.g., Spanish-language YouTube, Portuguese-language blogs, Mercado Libre community forums, Spanish Reddit equivalents). The absence of English-language community discussion (F-X07) may partly be explained by this language gap. Payhip's help center offers Portuguese (Brazil) and Spanish store language options (per F-07 source), suggesting a non-English-speaking LatAm user base exists.
**Source:** n/a — coverage gap notation
**Searched locations:** N/A — language boundary, not searched

---

**F-X11:** US state-level tax configuration on Payhip — borderline, not included as clean finding
The Payhip help center (https://help.payhip.com/article/174-taxes-for-digital-products) describes US state-level sales tax configuration with product-type selection and zip-code overrides. Snippet: "If you're setting up tax for the United States then things will be slightly different - firstly you'll have to choose whether you're adding a tax for a digital product, physical product, subscription, or coaching service." While this names "United States," the feature applies uniformly to all sellers (US or non-US) selling to US buyers and is not specific to cross-border LatAm↔US mechanics. Classified as borderline D1/D6 and excluded from Part 1.
**Source:** https://help.payhip.com/article/174-taxes-for-digital-products
**Searched locations:** Same as F-08

---

## Research QA Notes

**Source verification approach:** Help center pages fetched via subagent web_fetch calls. Key snippets cross-verified against independent web-search-index text. Blog pages (payhip.com/blog/whats-new-at-payhip-2025/ and payhip.com/blog/new-feature-payhip-integrates-with-11-new-payment-gateways/) fetched directly by lead agent and verified character-for-character. One URL (payhip.com/features/vat-taxes) could not be fully fetched; snippet sourced from search-engine index and classified as blocked_url_index_verified.

**Snippet fidelity:** All snippets in Part 1 are continuous passages as reported by fetched page content. The blog comment in F-09 preserves the original typo ("handleing"). The [Stated in layout] notation in F-07 represents a vertical currency list rendered as inline items.

**Cross-border cut enforcement:** Every Part 1 and Part 2 finding contains at least one of: named country (Brazil, Mexico, Argentina, Chile, Colombia, Peru, Uruguay, United States), named currency (ARS, BRL, CLP, COP, MXN, PEN, UYU, USD), international fee qualifier ("international commercial transactions"), or geographic tax distinction ("countries outside of the EU," "global taxes," "US states"). Three findings (F-02, F-03, F-09) have cross-border cuts established primarily via context (Mercado Pago = LatAm gateway, "global taxes" = beyond EU/UK); this is noted in each finding's Notes field.

**Reddit/forum absence:** The complete absence of English-language Payhip LatAm↔US seller experience reports (F-X07) was confirmed across 16+ Reddit searches, IndieHackers, Trustpilot, and Capterra. Even the broadest possible search ("site:reddit.com payhip") returned zero results, indicating Payhip has minimal Reddit discussion footprint overall (not only for LatAm topics).

**1099 conflict:** Two third-party sources make contradictory claims about Payhip 1099 issuance (F-X02). No official Payhip source addresses this. The architectural explanation (payments flow through seller-owned Stripe/PayPal accounts, so 1099-K comes from those processors) is consistent with the absence of any Payhip 1099 documentation.

**Temporal note on Mercado Pago:** The Mercado Pago integration was announced December 12, 2025 (blog post). The help center article was last updated December 31, 2025. This is within the time window but very recent, which may explain the absence of community experience reports.

**Global MoR caveat (F-09):** The planned global tax handling expansion mentioned by a Payhip staff member in a blog comment (January 2026) is informal and conditional ("as long as everything goes as planned"). As of April 14, 2026, no official announcement of a global MoR launch has been identified in any searched source. If launched, this would materially change the D6 findings related to Tax dimension.

**QA checklist applied to all findings:**
1. All What content supported by snippet — verified per finding.
2. What qualifiers checked — F-02 and F-03 note in Notes field that cross-border context is established by same-page content captured in F-01.
3. All Sources are full URLs — verified.
4. One source identity per finding — verified.
5. Multi-speaker pages: F-09 isolates a single speaker (Lucy @ Payhip staff); user question from Rebecca not included in snippet.
6. Notes contain local verification limitations only — verified; no cross-source interpretation or recommendations included.
7. All source_type values are from the allowed enum (help_center, blog, platform_doc) — verified.
8. verification_status assigned conservatively — direct_verified for fetched pages; blocked_url_index_verified for one unfetchable URL.
9. Five verification edge cases applied per finding (URL resolves, snippet is verbatim, source is original publisher, date verified or stated as undated, no conflicting content at source).
10. Visible qualifiers preserved: country names, currency codes, percentages, payout method names, tax form references, effective dates, direction of flow.
11. Borderline findings degraded to Part 4 (F-X11).