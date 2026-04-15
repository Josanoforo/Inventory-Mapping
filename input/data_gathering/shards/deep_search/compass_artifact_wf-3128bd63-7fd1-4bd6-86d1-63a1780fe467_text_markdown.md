Search decomposition
- SD-01: What US royalty withholding tax rate does Envato apply to non-US authors from LatAm countries on sales to US buyers?
- SD-02: Does Envato require non-US (LatAm) authors to submit Form W-8BEN, and what are the consequences of non-submission?
- SD-03: Which LatAm countries have US income tax treaties that reduce Envato withholding below the 30% default?
- SD-04: Does Envato collect or remit VAT/IVA for purchases or subscriptions in Mexico, Chile, or other LatAm countries?
- SD-05: What is Envato's merchant-of-record or supplier-of-record status for transactions involving LatAm buyers or sellers?
- SD-06: In what currency does Envato pay author earnings, and who bears currency conversion costs?
- SD-07: Does Envato support local-currency (MXN, BRL, ARS, COP, CLP, PEN) bank transfers to LatAm authors via IACH?
- SD-08: What payout methods does Envato offer to non-US authors, including Payoneer, Wise, PayPal, SWIFT?
- SD-09: What fees does Payoneer charge for cross-border payouts from USD to local LatAm currencies via Envato?
- SD-10: Which LatAm countries are restricted from Envato author signup or payouts?
- SD-11: Does Envato issue Form 1042-S to non-US authors for US-source earnings reporting?
- SD-12: What do LatAm authors report about their cross-border tax/payout experience on Envato forums, Reddit, or blogs (April 2025–April 2026)?
- SD-13: Does Envato add VAT/IVA to Author Fees for authors based in Mexico or Chile?

---

Part 1 - Clean findings (direct_verified)

None. All Envato help center domains (help.author.envato.com, help.market.envato.com, help.elements.envato.com) and Envato forums (forums.envato.com) returned HTTP 403 (Forbidden) on every direct web_fetch attempt, preventing direct verification of any page content. All Envato-sourced findings are degraded to Part 2 (blocked_url_index_verified) with content recovered from Google search engine index snippets. No non-Envato source within the shard-allowed source_type subset could be direct_verified for an Envato-specific cross-border claim. See Research QA Notes for full accounting.

---

Part 2 - Provisional findings (blocked_url_index_verified)

### F-P01
What: Non-US Envato authors' sales to US buyers may be subject to US royalty withholding tax of up to 30%, with possible reduction if the author resides in a country with a US income tax treaty.
Verbatim snippet: "Accordingly, if you are a non-U.S. person, your sales to US buyers may be subject to royalty withholding tax of up to 30%. However, if you are a resident of a country that has an income tax treaty with the U.S., you may be eligible for a reduced withholding tax rate."
Source: https://help.author.envato.com/hc/en-us/articles/360000471243-Tax-Information-Form-W-8-Requirements-for-non-US-Authors
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated in available index recovery
Notes: Page returned 403 on direct fetch; verbatim recovered from Google search index snippet of same URL. Recovery method: search index. Cross-border cut: "non-U.S. person" + "US buyers" + "royalty withholding tax." Dimension: TAX. Flow: LatAm→US (LatAm seller earning from US buyer). Applies to all LatAm countries; most (Brazil, Argentina, Colombia, Chile, Peru, Ecuador, Bolivia, Paraguay, Uruguay, Costa Rica, Panama, Guatemala, Dominican Republic) lack US tax treaties and face the full 30%, per IRS Treaty Table 1 (Rev. May 2023) — that country-specific enumeration is external to this snippet.

### F-P02
What: If a non-US Envato author does not submit tax information, Market earnings from US buyers will be withheld at 30% and cannot benefit from a reduced treaty rate.
Verbatim snippet: "If you do not submit your tax information, your Market earnings from US buyers will be taxed at the highest rate of 30%, and will not benefit from a reduced withholding tax rate under a double tax agreement (if applicable)."
Source: https://help.author.envato.com/hc/en-us/articles/360000471243-Tax-Information-Form-W-8-Requirements-for-non-US-Authors
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated in available index recovery
Notes: Page returned 403; recovered from search index. Cross-border cut: "US buyers" + "withholding tax" + "double tax agreement." Dimension: TAX. Flow: LatAm→US.

### F-P03
What: Authors in countries without a US tax treaty cannot reduce the 30% US royalty withholding tax rate on Envato.
Verbatim snippet: "If you're in a country that has no tax treaty with the US, unfortunately, we won't be able to reduce the royalty withholding tax rate of 30%."
Source: https://help.author.envato.com/hc/en-us/articles/360000471243-Tax-Information-Form-W-8-Requirements-for-non-US-Authors
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated in available index recovery
Notes: Page returned 403; recovered from search index. Cross-border cut: "country" + "tax treaty with the US" + "30%." Dimension: TAX. Flow: LatAm→US. Applies to the majority of LatAm countries that lack US tax treaties.

### F-P04
What: Even for non-treaty countries, submitting W-8 tax information on Envato is beneficial because it exempts earnings from non-US buyers from US taxes; only US-buyer royalty income attracts 30% withholding.
Verbatim snippet: "Even if your country does not have a treaty with the US, it is beneficial for you to submit your tax information. By submitting your tax information, your earnings from non-US buyers will not be subject to US taxes. Note, however, that your royalty income from US buyers will attract 30% royalty withholding tax."
Source: https://help.author.envato.com/hc/en-us/articles/360000471243-Tax-Information-Form-W-8-Requirements-for-non-US-Authors
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated in available index recovery
Notes: Page returned 403; recovered from search index. Cross-border cut: "non-US buyers" vs "US buyers" + withholding tax mechanism. Dimension: TAX. Flow: LatAm→US.

### F-P05
What: Envato annually sends non-US authors and the IRS a summary of US-customer earnings via Form 1042, enabling local tax reporting and claiming of credits for taxes withheld.
Verbatim snippet: "At the end of each calendar year we'll send to you and the IRS a summary of your earnings from US customers, Form 1042, so that you can accurately report your income to your local tax Authorities and claim any credits for the taxes withheld and remitted to the IRS."
Source: https://help.author.envato.com/hc/en-us/articles/360000471243-Tax-Information-Form-W-8-Requirements-for-non-US-Authors
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated in available index recovery
Notes: Page returned 403; recovered from search index. Cross-border cut: "US customers" + "IRS" + "local tax Authorities." Dimension: TAX. Flow: LatAm→US (reporting). Envato uses "Form 1042" in this passage; the individual author statement is technically Form 1042-S. Separate passage on same page states: "You will be provided a copy of your Form 1042 from 15th March in the year following the year you made your earnings."

### F-P06
What: On Envato Market, authors sell directly to customers; when a buyer is US-based, US royalty withholding tax applies to that sale.
Verbatim snippet: "With Envato Market, you are selling directly to the customer. When you sell to a buyer based in a country with royalty withholding taxes, they will apply. For example, when you sell to a US buyer, the US royalty withholding tax applies."
Source: https://help.author.envato.com/hc/en-us/articles/360000424886-Withholding-Taxes-with-Envato-Elements-and-Envato-Market
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated in available index recovery
Notes: Page returned 403; recovered from search index. Cross-border cut: "US buyer" + "US royalty withholding tax." Dimension: TAX. Flow: LatAm→US (LatAm seller, US buyer, Market platform). Same page also describes Envato Elements as selling to Envato (Australian company) with AU RWT — that is LatAm↔AU, not LatAm↔US, and is captured in F-X06.

### F-P07
What: Envato Elements subscribers in Mexico see their recurring billing adjusted to include Value Added Tax (VAT) of 16%.
Verbatim snippet: "Subscribers in Mexico will see a change in their recurring Envato Elements billing to include Value Added Tax (VAT) of 16%."
Source: https://help.elements.envato.com/hc/en-us/articles/30109659599257-Mexico-VAT-Information-for-Envato-Elements-Subscribers
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page states effective date February 20, 2024 in separate passage ("effective from the 20th of February, 2024") not continuous with this snippet
Notes: Page returned 403; recovered from search index. Cross-border cut: "Mexico" + "VAT" + "16%." Dimension: TAX. Flow: US→LatAm (platform → Mexican subscriber, buyer side). Same page provides pricing example: "$33 per month" → "$38.28 representing $5.28 of VAT that Envato Elements will pay to the Servicio de Administracion Tributaria."

### F-P08
What: Mexican business buyers on Envato Market with a valid RFC may recover Envato-charged VAT by claiming it as input tax on their Mexican VAT return.
Verbatim snippet: "If you are a business customer with a valid RFC, you may be able to recover the VAT charged by Envato by claiming it as input tax on your Mexican VAT return."
Source: https://help.market.envato.com/hc/en-us/articles/46566990286745-Mexico-VAT-Information-for-Buyers
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page states VAT visible on statements "for all purchases completed after 15 May 2025" (separate passage)
Notes: Page returned 403; recovered from search index. Cross-border cut: "Mexico" + "RFC" + "Mexican VAT return." Dimension: TAX. Flow: US→LatAm (platform → Mexican buyer). Same page states "Envato is registered for VAT in Mexico and charges VAT to buyers resident in Mexico from May 2025" and "Providing a valid RFC (Registro Federal de Contribuyentes) number will not exempt you from VAT charges" (separate passages). Page contains apparent typo "Meixan" for "Mexican."

### F-P09
What: Mexico-based Envato Elements subscribers who do not provide an RFC get the default "General Public" RFC code ('XAXX010101000') saved with their billing information.
Verbatim snippet: "If you do not provide a RFC, then the default 'General Public' RFC ('XAXX010101000') will be saved with your billing information."
Source: https://help.elements.envato.com/hc/en-us/articles/30109659599257-Mexico-VAT-Information-for-Envato-Elements-Subscribers
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated in this snippet
Notes: Page returned 403; recovered from search index. Cross-border cut: "Mexico" + "RFC" (Registro Federal de Contribuyentes, Mexico-specific tax ID). Dimension: TAX. Flow: US→LatAm (platform billing for Mexican subscriber). XAXX010101000 is Mexico's SAT generic public RFC.

### F-P10
What: Envato may add tax to Author Fees if the author's billing address is in Canada, Mexico, South Africa, Türkiye, or Chile.
Verbatim snippet: "You may see tax added to your Author Fees if your billing address is in: Canada, Mexico, South Africa, Türkiye, or Chile."
Source: https://help.author.envato.com/hc/en-us/articles/47853405391385-Global-Tax-Collection-VAT-GST-More-Information-for-Authors
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated in available index recovery
Notes: Page returned 403; recovered from search index. Cross-border cut: "Mexico" and "Chile" explicitly named as LatAm countries affected. Dimension: TAX. Flow: LatAm→US (tax on Author Fees charged to LatAm-based authors). Mexico and Chile are the only two LatAm countries in this list. Separate passage on same page states authors can add "tax registration number (e.g. VAT, GST, or RFC number) to your Envato billing details."

### F-P11
What: For purposes other than EU VAT, including selling to non-EU customers, the Envato Market Author is selling directly to the customer and receiving sale income; the Author subsequently pays an Author fee to Envato.
Verbatim snippet: "For all other purposes, including selling to non-EU customers, and including income tax purposes, the Author is selling directly to the customer and receiving a sale income. Subsequently, the Author pays an Author fee to Envato."
Source: https://help.author.envato.com/hc/en-us/articles/360000471323-VAT-for-Envato-Market
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated in available index recovery
Notes: Page returned 403; recovered from search index. Cross-border cut: "non-EU customers" (which includes all LatAm countries). Dimension: TAX. This establishes that Envato is NOT the merchant-of-record / supplier-of-record for LatAm transactions on Market — the author is the seller. Separate passage on same page states: "For EU VAT purposes only, Envato is shown as the supplier of record." No equivalent supplier-of-record statement for any LatAm country was found anywhere on this page or on any other Envato page. Cross-border cut is implicit (LatAm is definitionally non-EU) rather than naming a specific LatAm country.

### F-P12
What: Envato author earnings are paid in US dollars; the author is responsible for all costs of currency conversion, performed by the author's financial institution.
Verbatim snippet: "Currency: Your earnings will be paid to you in US dollars. You are responsible for all costs of currency conversion relating to your earnings."
Source: https://help.author.envato.com/hc/en-us/articles/41371538488473-Envato-Market-Author-Terms
source_type: policy_page
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated in available index recovery
Notes: Page returned 403; recovered from search index. Cross-border cut: "US dollars" + "currency conversion" (relevant when author is non-US, as all LatAm authors are). Dimension: CURRENCY. Flow: Applies to both LatAm→US and US→LatAm earnings flows. Full passage continues: "Your financial institution does the currency conversion and may charge you additional fees outside our control."

### F-P13
What: Envato offers bank transfers into 137 currencies, 83 of which use local IACH routes enabling same-currency transfers to authors' local bank accounts with faster payouts and fewer fees.
Verbatim snippet: "Envato now offers bank transfers into 137 currencies, 83 of which are transferred via local routes called International Automated Clearing Houses (IACHs). These are cross-border transfer services that enable electronic transfer payments using your local currency. This means faster payouts and fewer fees."
Source: https://help.author.envato.com/hc/en-us/articles/20535795834393-Getting-Started-with-the-Envato-Payout-System
source_type: help_center
verification_status: blocked_url_index_verified
Date: December 18, 2025 (page date "December 18, 2025 23:02 Updated" visible in search index snippet from a separate query)
Notes: Page returned 403; recovered from search index. Cross-border cut: "137 currencies" + "cross-border transfer services" + "local currency." Dimension: CURRENCY. LatAm currencies (MXN, BRL, COP, CLP, PEN, and potentially ARS) are likely among the 83 IACH-supported currencies, but the page does not enumerate specific currencies. Separate passage on same page: "Landing times for local currency payments are typically within 1-2 business days, as opposed to 5 business days with the SWIFT network."

### F-P14
What: Non-US Envato authors who want to receive USD via bank transfer must use a Money Transfer Provider with a virtual US routing account, such as Payoneer or Wise.
Verbatim snippet: "If you would prefer a bank transfer, but are not in the USA and still want to receive USD, you will need to use a Money Transfer Provider that offers a virtual US routing account, such as Payoneer or Wise."
Source: https://help.author.envato.com/hc/en-us/articles/20535795834393-Getting-Started-with-the-Envato-Payout-System
source_type: help_center
verification_status: blocked_url_index_verified
Date: December 18, 2025 (page date visible in separate search index snippet)
Notes: Page returned 403; recovered from search index. Cross-border cut: "not in the USA" + "USD" + "virtual US routing account." Dimension: PAYOUT. Flow: LatAm→US (payout delivery mechanism for non-US authors). Separate passage on same page lists full method set: "Set your Payout method–either Bank Transfer or PayPal. If you want to select a virtual provider like Payoneer, Wise or Revolut, you need to select the Bank Transfer option." Also: "Please note that all PayPal payments are sent in USD."

### F-P15
What: Payoneer Global Bank Transfer from Envato converts from USD at a cost of $1.50 per transfer plus a 2% Foreign Exchange conversion fee on top of the daily mid-market rate.
Verbatim snippet: "Currency conversions take place from USD and costs $1.50 per transfer, plus 2% Foreign Exchange (FX) conversion fee on top of the daily mid-market rate."
Source: https://help.author.envato.com/hc/en-us/articles/360000471963-Payoneer-FAQs
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated in available index recovery
Notes: Page returned 403; recovered from search index. Cross-border cut: "from USD" + currency conversion mechanism. Dimension: PAYOUT. Applies to all LatAm authors using Payoneer Global Bank Transfer to receive in local currency (MXN, BRL, ARS, COP, CLP, PEN, etc.). Separate passage on same page: "Payments sent via USD SWIFT transfers to your bank account via Payoneer will incur a flat fee of $15.00." Also: "Payoneer offers payments in over 200 countries and more than 150 currencies."

### F-P16
What: Venezuelan citizens who currently work for the Venezuelan Government are prohibited by US sanctions from transacting on Envato platforms as authors or customers.
Verbatim snippet: "Additionally, current US sanctions against Venezuela also prohibit us from allowing authors and customers who are citizens of Venezuela and who currently work for the Venezuelan Government to transact on our platforms."
Source: https://help.author.envato.com/hc/en-us/articles/360000471303-What-Countries-Can-I-Not-Use-Envato-From
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated in available index recovery
Notes: Page returned 403; recovered from search index. Cross-border cut: "Venezuela" + "US sanctions" + geographic restriction. Dimension: AVAILABILITY. Flow: Applies to both directions (LatAm→US and US→LatAm). Same page states general payout-blocked countries: "if your residential address is located in Russia, Belarus, Afghanistan, Sudan, or Libya, we will not be able to pay you" — no LatAm country appears in the payout-blocked list. Also: "Due to payment restrictions, we are not accepting new author signups from Russia, Belarus, Afghanistan, Sudan, or Libya" — no LatAm country is blocked from signup.

---

Part 3 - Pattern candidates (sealed)

### PC-01
Pattern Candidate ID: PC-01
Candidate statement: Multiple Envato help center articles consistently reference a 30% default US royalty withholding rate for non-US authors without a tax treaty, and state this rate cannot be reduced for non-treaty countries; the majority of LatAm countries (Brazil, Argentina, Colombia, Chile, Peru, Ecuador, Bolivia, Paraguay, Uruguay, Costa Rica, Panama, Guatemala, Dominican Republic) lack US income tax treaties.
Related Finding IDs: F-P01, F-P02, F-P03, F-P04, F-P06
Status: sealed; not validated

### PC-02
Pattern Candidate ID: PC-02
Candidate statement: Envato's LatAm-specific tax documentation is concentrated on Mexico, with dedicated VAT pages for Market buyers, Elements subscribers, and Authors; Chile appears only in the Global Tax Collection author fee list alongside Mexico; no other LatAm country has dedicated Envato tax documentation.
Related Finding IDs: F-P07, F-P08, F-P09, F-P10
Status: sealed; not validated

### PC-03
Pattern Candidate ID: PC-03
Candidate statement: Envato's payout system documentation describes USD as the default earnings currency with multiple cross-border delivery mechanisms (IACH local currency in 137 currencies, Payoneer, Wise, PayPal in USD, SWIFT), but no LatAm-country-specific payout method, threshold, or timing difference is documented.
Related Finding IDs: F-P12, F-P13, F-P14, F-P15
Status: sealed; not validated

---

Part 4 - Could not verify / Out-of-scope

### F-X01: Specific US tax treaty royalty withholding rates for individual LatAm countries on Envato
What: Envato's "US Tax Treaties" article references IRS treaty rate tables for copyright royalty withholding but the page could not be fetched; specific treaty rates for LatAm countries (Mexico 10%, Venezuela 10%, Jamaica 10%, Barbados 5%, Trinidad & Tobago 0%) are sourced from IRS Treaty Table 1 (Rev. May 2023), which is not an Envato source.
Verbatim snippet: "n/a — absence finding"
Source: Searches attempted: (1) web_fetch of https://help.author.envato.com/hc/en-us/articles/360000470606-US-Tax-Treaties returned 403; (2) web_search for site:help.author.envato.com "US Tax Treaties" returned page title and generic description "This article lists all the current US Tax Treaties across the countries Envato operates" but no rate table content; (3) IRS Treaty Table 1 at irs.gov/pub/irs-lbi/tax-treaty-table-1.pdf was fetched successfully but is not an Envato source and falls outside the allowed source_type subset for this shard.
source_type: help_center
verification_status: could_not_verify
Date: Accessed April 2026
Notes: The Envato page exists and is indexed but its treaty rate table content could not be recovered from search index snippets. Country-specific treaty rates (e.g., Mexico 10% copyright royalties under Article 12(2)) are confirmed by the IRS table but cannot be attributed to Envato documentation without direct page verification.

### F-X02: Australian Royalty Withholding Tax rates for LatAm Envato Elements authors (LatAm↔AU, out of D6 scope)
What: Envato Elements authors sell to Envato (an Australian company), triggering Australian Royalty Withholding Tax (AU RWT) at 0–30% depending on Australia–country tax treaties. Mexico and Argentina have AU treaties (reduced rates); Brazil, Colombia, Peru, Venezuela do not (30% default).
Verbatim snippet: "With Envato Elements, you are selling your items to Envato, an Australian company. Therefore the Australian royalty withholding tax applies. If your country does not have a tax treaty with Australia, the royalty withholding tax is 30%."
Source: https://help.author.envato.com/hc/en-us/articles/360000424886-Withholding-Taxes-with-Envato-Elements-and-Envato-Market
source_type: help_center
verification_status: could_not_verify
Date: Accessed April 2026; page returned 403
Notes: Content recovered from search index. Degraded to Part 4 because this describes LatAm↔AU flow direction, not LatAm↔US as required by the D6 shard scope. However, this directly affects the total tax burden of LatAm Envato authors. AU treaty rates for specific LatAm countries (Mexico 10%, Argentina 10–15%, Chile 5–10%) sourced from PwC Australia WHT table (external, not Envato).

### F-X03: Absence — No LatAm author experience reports from April 2025–April 2026 on Envato forums
What: No Envato forum threads from April 2025–April 2026 were found containing experience reports from LatAm-based authors about tax withholding, payouts, currency conversion, or country-specific issues.
Verbatim snippet: "n/a — absence finding"
Source: Searches attempted: (1) web_fetch of https://forums.envato.com/search?q=withholding%20tax returned 403; (2) web_fetch of https://forums.envato.com/search?q=payout%20country returned 403; (3) web_search for site:forums.envato.com "Mexico" AND ("tax" OR "withholding" OR "payout") — results all pre-date April 2025; (4) web_search for site:forums.envato.com "Brazil" AND "tax" — zero LatAm-specific results from target window; (5) web_search for site:forums.envato.com "Argentina" AND ("tax" OR "payout") — zero results; (6) web_search for site:forums.envato.com "Colombia" AND ("tax" OR "payout") — zero results; (7) web_search for site:forums.envato.com "Latin America" AND ("tax" OR "payout") — zero results.
source_type: seller_forum
verification_status: could_not_verify
Date: Accessed April 2026
Notes: forums.envato.com returned 403 on all direct fetch attempts. Search index returned only pre-2025 threads with LatAm country mentions (Venezuela ~2016, Bolivia ~2015, Brazil ~2015). LatAm-specific forum discussion appears extremely sparse; forum is dominated by South Asian, Middle Eastern, and Eastern European author discussions.

### F-X04: Absence — No Reddit discussions of Envato LatAm↔US cross-border mechanics found
What: No Reddit posts or threads were found discussing Envato's cross-border tax withholding, payout mechanics, currency conversion, or country-specific issues for LatAm authors or buyers.
Verbatim snippet: "n/a — absence finding"
Source: Searches attempted: (1) web_search for site:reddit.com "envato" "tax" ("Mexico" OR "Brazil" OR "Argentina" OR "Colombia" OR "Latin America") — zero relevant results; (2) web_search for site:reddit.com "envato" "withholding" OR "W-8BEN" — zero results; (3) web_search for site:reddit.com "envato" "payout" ("Latin America" OR "LatAm" OR "Mexico" OR "Brazil") — zero results; (4) web_search for site:reddit.com envato tax withholding 2025 2026 — zero results.
source_type: reddit
verification_status: could_not_verify
Date: Accessed April 2026
Notes: Complete absence of Reddit discussion on this topic. LatAm Envato authors may discuss these issues in Spanish-language forums or social media not covered by English-language search.

### F-X05: Absence — No YouTube transcripts found for Envato tax setup tutorials specific to LatAm
What: No YouTube videos or transcripts were found covering Envato tax setup (W-8BEN, withholding, payout methods) specifically for LatAm-based authors.
Verbatim snippet: "n/a — absence finding"
Source: Searches attempted: (1) web_search for site:youtube.com "envato" "withholding tax" OR "W-8BEN" OR "tax information" — zero relevant results; (2) web_search for "envato" tax setup non-US author tutorial — no YouTube results with LatAm focus.
source_type: video_transcript
verification_status: could_not_verify
Date: Accessed April 2026
Notes: Any tutorials that exist may be in Spanish or Portuguese, outside the English-only scope of this shard.

### F-X06: Coverage gap — Spanish-language Envato forum thread on Chilean invoicing
What: A Spanish-language thread on Envato forums discusses a Chilean buyer's inability to obtain legal invoices (facturas) from Envato for tax purposes. Thread title: "Facturación/Billing."
Verbatim snippet: "n/a — Spanish-language content, out of English-only scope"
Source: https://forums.envato.com/t/facturacion-billing/490365 (returned 403 on fetch; content identified via search index)
source_type: seller_forum
verification_status: could_not_verify
Date: Approximately 2024 based on thread numbering
Notes: Thread is entirely in Spanish. Per shard rule (English only), content cannot be included in Part 1 or Part 2. This represents a coverage gap: Chilean buyer-side invoicing issues (inability to get "factura legal" from Envato for Chilean tax purposes) are discussed in Spanish but no equivalent English-language thread was found. The invoicing issue (Envato not providing Chilean-compliant tax invoices) may be material for D6 TAX dimension.

### F-X07: Out-of-scope — $50 USD minimum payout threshold (uniform, no cross-border cut)
What: Envato applies a $50 USD minimum payout threshold for all payout methods, applicable uniformly to all authors regardless of country.
Verbatim snippet: "There is a $50 minimum payout amount (for each of the payout methods). If you don't reach the $50 minimum within the month, we will withhold your monies until you reach the minimum."
Source: https://help.author.envato.com/hc/en-us/articles/20535795834393-Getting-Started-with-the-Envato-Payout-System
source_type: help_center
verification_status: could_not_verify
Date: December 18, 2025 (page date visible in search index)
Notes: Degraded to Part 4 because the $50 minimum applies uniformly regardless of country — this is D1 territory (generic fee/policy), not D6 (cross-border-specific). No country-specific payout threshold differences were found for any LatAm country.

### F-X08: Out-of-scope — Payout schedule (15th of each month, uniform)
What: Envato processes author payouts on the 15th of each month; authors must set up payout details by the 8th of the month.
Verbatim snippet: "You'll still be paid on the 15th of each month if you have earned more than the minimum payment threshold of $50."
Source: https://help.author.envato.com/hc/en-us/articles/20535795834393-Getting-Started-with-the-Envato-Payout-System
source_type: help_center
verification_status: could_not_verify
Date: December 18, 2025
Notes: Degraded to Part 4 because the payout schedule applies uniformly to all countries — D1, not D6. No country-specific timing differences for LatAm were documented.

### F-X09: Degraded — Venezuela author forum experience (2016, outside time window)
What: A Venezuela-based author on Envato forums reported receiving only $4.42 from a $13.60 sale, attributing the reduction to fees and taxes, circa January 2016.
Verbatim snippet: "Hi there. I from Venezuela, i don´t know all of this issues of fees and taxes But for my first sale of the year its a very disapointment. Its a bad joke my sale for $13.60 only I get 4,42$"
Source: https://forums.envato.com/t/please-tell-me-this-is-not-a-bad-joke-fees-and-taxes/24931
source_type: seller_forum
verification_status: could_not_verify
Date: Approximately January 2016
Notes: Degraded to Part 4 because the post dates to approximately January 2016, outside the April 2025–April 2026 experience window. Forum returned 403 on direct fetch; snippet recovered from search index. Venezuela has a US tax treaty (10% royalty rate), so this author may not have submitted a W-8BEN with tax ID, resulting in 30% withholding. Post is a genuine LatAm author experience but cannot be time-window verified.

### F-X10: Degraded — Mexico buyer invoice request on Envato forum (~2024)
What: A Mexico-based buyer on Envato forums requested a purchase invoice for a product, stating "I am in Mexico," circa 2024.
Verbatim snippet: "I need you to send me the purchase invoice for the LineOne dashboard that I just purchased, what would be the procedure to follow to get it to me and what documents would you need? I am in Mexico."
Source: https://forums.envato.com/t/need-the-invoice-for-my-purchase/476971
source_type: seller_forum
verification_status: could_not_verify
Date: Approximately 2024 based on thread numbering
Notes: Degraded to Part 4 because post predates the April 2025–April 2026 experience window. Forum returned 403; snippet recovered from search index. This is buyer-side (US→LatAm flow) and relates to Mexico-specific invoicing requirements (RFC/CFDI). Post username and exact date could not be verified.

### F-X11: Absence — No Envato merchant-of-record statement for any specific LatAm country
What: No Envato documentation was found stating that Envato acts as merchant-of-record or supplier-of-record for transactions involving any specific LatAm country. Envato is supplier of record for EU VAT only.
Verbatim snippet: "n/a — absence finding"
Source: Searches attempted: (1) web_search for site:help.author.envato.com "merchant of record" OR "supplier of record" — results reference EU VAT only; (2) web_search for envato "merchant of record" Mexico OR Brazil OR Chile OR Colombia OR Argentina — no relevant results; (3) F-P11 confirms "For non-EU Customers, the Author is shown as the supplier"; (4) Mexico VAT pages (F-P07, F-P08) show Envato collects/remits Mexico VAT but do not use supplier-of-record or merchant-of-record language.
source_type: help_center
verification_status: could_not_verify
Date: Accessed April 2026
Notes: While Envato collects and remits Mexico VAT (IVA) on Elements subscriptions and Market purchases (per F-P07, F-P08), and is "registered for VAT in Mexico," no page uses the specific phrase "merchant of record" or "supplier of record" for Mexico or any LatAm country. The MoR language is reserved for EU VAT per F-P11.

### F-X12: Absence — No blog posts by LatAm Envato authors describing tax/payout experience found
What: No English-language blog posts by LatAm-based Envato authors describing their cross-border tax withholding, payout, or currency conversion experience were found.
Verbatim snippet: "n/a — absence finding"
Source: Searches attempted: (1) web_search for "envato" "payout" "Latin America" OR "Mexico" OR "Brazil" experience — zero blog results; (2) web_search for envato themeforest author Mexico Brazil experience 2025 — no LatAm author experience blogs; (3) web_search for "envato" "W-8BEN" guide tutorial non-US seller — no LatAm-specific results.
source_type: blog
verification_status: could_not_verify
Date: Accessed April 2026
Notes: Any such blog posts may exist in Spanish or Portuguese, outside this shard's English-only scope.

### F-X13: Out-of-scope — "North America Sales Tax" page excludes Mexico
What: Envato's "North America Sales Tax for Envato Market" article covers US state sales taxes and Canadian Quebec Sales Tax but does not mention Mexico, despite Mexico being geographically part of North America.
Verbatim snippet: "n/a — content not fully recoverable from search index"
Source: https://help.author.envato.com/hc/en-us/articles/360001112903-North-America-Sales-Tax-for-Envato-Market (returned 403; search snippets reference US states and Quebec only)
source_type: help_center
verification_status: could_not_verify
Date: January 16, 2025 (page date visible in search index)
Notes: Mexico's sales tax treatment is handled via separate "Mexico VAT" pages (F-P07, F-P08, F-P10) rather than the North America Sales Tax page. This structural observation may be relevant to understanding how Envato categorizes Mexico for tax purposes.

---

Research QA Notes
- Findings forced to Provisional: F-P01 through F-P16 — all 16 findings forced to blocked_url_index_verified because every Envato help center domain (help.author.envato.com, help.market.envato.com, help.elements.envato.com) returned HTTP 403 on all direct web_fetch attempts. Content was recovered exclusively from Google search engine index snippets of the same URLs. Verbatim snippets may contain minor formatting differences from the original pages (e.g., missing bold, list markers, or table formatting). Part 1 (Clean) is empty as a result; this was not a verification bar decision but a systemic access limitation.
- Findings degraded to could_not_verify: F-X01 (treaty rate table not recoverable from search index); F-X02 (LatAm↔AU flow, out of D6 scope); F-X07 ($50 minimum, uniform/D1); F-X08 (payout schedule, uniform/D1); F-X09 (Venezuela experience, outside time window); F-X10 (Mexico invoice, outside time window); F-X13 (North America Sales Tax excludes Mexico, structural observation).
- Findings degraded due to URL not fixable: None — all URLs are valid and indexed; the 403 is a server-side access block, not a broken URL.
- Multi-speaker pages split: None applicable — all forum threads returned 403, preventing multi-speaker identification from full thread content. Forum content in F-X09 and F-X10 represents single speakers extracted from search index snippets; multi-speaker split could not be performed because full thread content was inaccessible.
- Truncated/partial sources: All 16 Part 2 findings rely on search index snippets, which may be truncated relative to full page content. Key truncation risks: (1) the US Tax Treaties rate table (F-X01) was not recoverable; (2) the Global Tax Collection page's full country list and rate table may contain additional detail not captured; (3) the Mexico VAT for Authors page content was almost entirely unrecoverable (only generic meta-description indexed).
- source_type ambiguities: (1) F-P12 uses policy_page for the Author Terms article (https://help.author.envato.com/hc/en-us/articles/41371538488473-Envato-Market-Author-Terms) — this could also be classified as help_center since it is hosted on the help center domain, but the content is contractual terms making policy_page more accurate. (2) Forum threads F-X09 and F-X10 classified as seller_forum; the Mexico buyer in F-X10 is technically a buyer, but the forum (forums.envato.com) is primarily an author/seller community and the buyer_review source_type is reserved for dedicated review platforms.
- Coverage gaps by category:
  - CURRENCY: No documentation found about specific LatAm currency exchange rates, markups, or spreads applied by Envato or its payment providers for MXN, BRL, ARS, COP, CLP, PEN conversions. The 137-currency/83-IACH claim does not enumerate which LatAm currencies are supported via local routes.
  - TAX: (a) Specific US treaty withholding rates for LatAm countries not recoverable from Envato sources (F-X01). (b) Mexico VAT for Authors page content almost entirely unrecoverable. (c) Chile VAT rate not stated by Envato (no dedicated Chile page; Chile only appears in Global Tax Collection list). (d) No Envato documentation for Brazil, Argentina, Colombia, Peru, Ecuador, Bolivia, or any other LatAm country beyond Mexico and Chile.
  - AVAILABILITY: No documentation found listing which specific LatAm countries can or cannot open Envato author accounts; only sanctioned/blocked countries (Russia, Belarus, Afghanistan, Sudan, Libya) are named, plus the Venezuela Government-employee restriction. Envato states author applications are "currently closed" and will "reopen from mid April 2026 for some content types" (found in search index of Becoming an Envato Author FAQs).
  - PAYOUT: No LatAm-country-specific payout method restrictions, timing differences, or fee schedules found. Payoneer fees ($1.50 + 2% FX) and SWIFT fees ($15) are global, not LatAm-specific.
  - EXPERIENCE: Complete absence of LatAm author or buyer experience reports from April 2025–April 2026 in English on any platform searched (forums, Reddit, YouTube, blogs). Spanish-language content exists (F-X06 Chilean invoicing thread) but is out of scope.
  - SPANISH-LANGUAGE GAP: Multiple searches suggest LatAm Envato users discuss these topics primarily in Spanish. At least one Spanish-only forum thread (F-X06) and one Spanish-language Envato Elements review site (impulsaecommerce.com) were identified but excluded per the English-only scope rule.
- Cases where input could not be decomposed without interpretation: None. All 13 sub-searches map directly to the four shard dimensions and the specified LatAm countries.