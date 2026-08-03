# Etapa 3 — casos para adjudicacion del operador

Muestra estratificada reproducible. Semilla `20260803`. 60 casos.

Cada bloque muestra solo los campos en desacuerdo, de tipo (A)
divergencia de valor o (B) presencia vs ausencia. Las diferencias de
solo orden (C) se listan aparte al final de cada bloque cuando existen,
y no motivan la inclusion del caso.

Elegibilidad del caso (paso 3 revisado): un record entra a la muestra
si tiene al menos un desacuerdo (A) o (B) en un **campo de enum**
(marcado 🔒 en la tabla de cada caso). Los campos de **texto libre**
(marcados 📝) no hacen elegible a un record por si solos, pero se
muestran igual si el record entro por un campo de enum.

El veredicto lo escribe el operador. El script no adjudica.

---

## Caso 1 — `ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-007-SNP-002`

- **Batch de origen:** batch_001
- **Estrato:** E1

**snippet_primary:**

> [Stated in layout: "$25,443,110 excludes hidden earnings Estimated Monthly Payouts"]

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(A · 📝 texto libre)_ | excludes hidden earnings | excludes hidden earnings · Estimated |
| `metric_unit` _(A · 📝 texto libre)_ | USD/month | USD per month |
| `parser_notes` _(A · 📝 texto libre)_ | Data recency stated only as 'Updated daily'; no snapshot date given beyond April 14, 2026 access. | snippet_primary is layout-derived (bracketed reconstruction), not prose verbatim. · Figure labeled 'Estimated' with no estimation method stated; unclear whether payouts are before or after platform fees. |
| `platforms` _(B · 📝 texto libre)_ | Patreon | _(lista vacia)_ |
| `subject_exact` _(A · 📝 texto libre)_ | Estimated aggregate monthly payouts to Patreon creators (excluding hidden/private earnings), per Graphtreon | Graphtreon estimated monthly payouts total for Patreon creators |
| `uncertainties` _(A · 🔒 enum)_ | current_vs_historical_ambiguity | time_scope_unclear · source_date_unclear · methodology_unclear · net_vs_gross_ambiguity |

**Criterios vigentes en este batch:**

- Sonnet — ninguna adicion formulada aun; solo criterios base.
- Fable — ninguna adicion formulada aun; solo criterios base.

**Veredicto:**


---

## Caso 2 — `ER-SP-compass_artifact_wf-0ffe7308-62e3-4530-ae68-93720df60f34_text_markdown-014-SNP-001`

- **Batch de origen:** batch_002
- **Estrato:** E1

**snippet_primary:**

> "No. Configurarlo es totalmente gratis, y solo pagarás 4.5% + 10.00 MXN por cada venta."

| Campo | Sonnet | Fable |
|---|---|---|
| `geography_if_explicit` _(B · 📝 texto libre)_ | Mexico | _(null)_ |
| `local_qualifiers` _(A · 📝 texto libre)_ | configurarlo es totalmente gratis (setup is free) | Configurarlo es totalmente gratis · solo pagarás 4.5% + 10.00 MXN por cada venta |
| `metric_unit` _(A · 📝 texto libre)_ | percent + fixed fee (MXN) | percent of sale plus fixed MXN amount (mixed units declared) |
| `parser_notes` _(A · 📝 texto libre)_ | Snippet is in Spanish; per-sale fee figure differs slightly from the 4.5% + 8 MXN figure in the investomatica calculator record for the same market — not reconciled here, as Data Extraction does not compare sources. | Snippet is an FAQ answer beginning with 'No.'; the question it answers was not captured — fee layer (processing vs other) not determinable from snippet alone. · No platform name in snippet text; 'Etsy' only in source_ref URL; platforms left empty per criteria F. · MXN currency does not by itself establish geography; geography left null. |
| `platforms` _(B · 📝 texto libre)_ | Etsy | _(lista vacia)_ |
| `subject_exact` _(A · 📝 texto libre)_ | Etsy Mexico seller transaction fee rate stated on the Etsy Mexico Payments page (Spanish) | per-sale charge (4.5% + 10.00 MXN) with free setup stated on Etsy MX payments page |
| `uncertainties` _(A · 🔒 enum)_ | none | source_date_unclear · context_insufficient |

**Criterios vigentes en este batch:**

- Sonnet — ninguna adicion formulada aun; solo criterios base.
- Fable — ninguna adicion formulada aun; solo criterios base.

**Veredicto:**


---

## Caso 3 — `ER-SP-compass_artifact_wf-1d3ea608-c044-4be6-97d1-5146f970457d_text_markdown-003-SNP-001`

- **Batch de origen:** batch_002
- **Estrato:** E1

**snippet_primary:**

> «Me han hecho un cargo a mi tarjeta de crédito por $273.535,43 cop (61,63us$) a favor de domestika sin mi autorización, casi un mes después de haber comprado ingenuamente tres cursos de crochet a bajo precio. Reclamé el mismo día que me hicieron el cargo (ayer) y me contestaron al siguiente día que yo había activado una suscripción lo cual es falso. Yo en ningún momento di mi autorización para un cobro de una suscripción anual. Exijo el reembolso!!»

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(B · 📝 texto libre)_ | _(lista vacia)_ | sin mi autorización · casi un mes después de haber comprado · suscripción anual |
| `metric_type` _(A · 🔒 enum)_ | unknown | price |
| `metric_unit` _(A · 📝 texto libre)_ | COP/USD | COP, with USD equivalent in parentheses (mixed units declared) |
| `parser_notes` _(A · 📝 texto libre)_ | Buyer complaint on a consumer-complaints aggregator site; source_type recorded as unknown per skeleton, actor determined by first-person buyer voice in the text. | source_type is 'unknown' (complaints site tuquejasuma.com); first-person buyer complaint, actor_level assigned buyer (who speaks). · Charged amount preserved verbatim including both currency figures; 'cop' is a currency marker, not geographic wording — geography left null. · Buyer disputes the platform's claim that a subscription was activated; both assertions preserved in snippet only. |
| `subject_exact` _(A · 📝 texto libre)_ | Buyer complaint of an unauthorized annual Domestika subscription charge on a credit card | buyer-reported unauthorized annual subscription charge to credit card by Domestika roughly one month after course purchase |
| `time_scope_raw` _(A · 📝 texto libre)_ | casi un mes después de haber comprado | casi un mes después de haber comprado; reclamo 'ayer' |
| `uncertainties` _(A · 🔒 enum)_ | anecdotal_single_source | anecdotal_single_source · source_date_unclear |

**Criterios vigentes en este batch:**

- Sonnet — ninguna adicion formulada aun; solo criterios base.
- Fable — ninguna adicion formulada aun; solo criterios base.

**Veredicto:**


---

## Caso 4 — `ER-SP-compass_artifact_wf-22c5fbd5-9e04-4d5a-9b0e-4cb97acec9cc_text_markdown_normalized-016-SNP-003`

- **Batch de origen:** batch_004
- **Estrato:** E1

**snippet_primary:**

> "Pasaron en muy poco tiempo de tener 200 empleados a alrededor de 800 en todo el mundo y, en año y medio, se van a quedar otra vez con 200. Ahí evidentemente hay algo raro."

| Campo | Sonnet | Fable |
|---|---|---|
| `actor_level` _(A · 🔒 enum)_ | seller | unknown |
| `local_qualifiers` _(B · 📝 texto libre)_ | _(lista vacia)_ | alrededor de 800 en todo el mundo · en año y medio |
| `metric_type` _(A · 🔒 enum)_ | unknown | employee count |
| `metric_value_raw` _(A · 📝 texto libre)_ | 200 to ~800 to 200 | de tener 200 empleados a alrededor de 800 … otra vez con 200 |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | metric_type out of enum: observed metric is an employee headcount; no enum value covers it. · Quoted speaker's role not determinable from snippet; actor_level set to unknown. · Platform named only in source_title/URL; platforms left empty per criteria F. · Speaker's closing assessment ('Ahí evidentemente hay algo raro') remains in snippet only. |
| `platforms` _(B · 📝 texto libre)_ | Domestika | _(lista vacia)_ |
| `subject_exact` _(A · 📝 texto libre)_ | Instructor account of Domestika's rapid headcount growth (200 to ~800 employees) followed by a return to ~200 within eighteen months | reported Domestika workforce fluctuation from 200 to around 800 employees and back toward 200 within a year and a half |
| `time_scope_raw` _(A · 📝 texto libre)_ | en año y medio | en muy poco tiempo … en año y medio |
| `uncertainties` _(A · 🔒 enum)_ | anecdotal_single_source · methodology_unclear | anecdotal_single_source · actor_level_unclear |

**Criterios vigentes en este batch:**

- Sonnet — ninguna adicion formulada aun; solo criterios base.
- Fable — ninguna adicion formulada aun; solo criterios base.

**Veredicto:**


---

## Caso 5 — `ER-SP-compass_artifact_wf-22c5fbd5-9e04-4d5a-9b0e-4cb97acec9cc_text_markdown_normalized-017-SNP-001`

- **Batch de origen:** batch_004
- **Estrato:** E1

**snippet_primary:**

> "I've heard many horror stories about Domestika from instructors over the years..."

| Campo | Sonnet | Fable |
|---|---|---|
| `actor_level` _(A · 🔒 enum)_ | seller | source |
| `local_qualifiers` _(B · 📝 texto libre)_ | _(lista vacia)_ | I've heard · over the years |
| `parser_notes` _(A · 📝 texto libre)_ | Snippet is truncated after the opening clause; the specific 'horror stories' content is not present in the extracted text. | Secondhand hearsay claim; snippet is truncated with ellipsis and the rest of the post was not captured. · source_date_if_available is approximate ('~2025'); not normalized. |
| `subject_exact` _(A · 📝 texto libre)_ | Instructor's general claim of having heard multiple negative accounts from Domestika instructors (specific content not present in truncated snippet) | commentator-reported accumulation of instructor 'horror stories' about Domestika over the years |
| `time_scope_raw` _(A · 📝 texto libre)_ | ~2025 | over the years |
| `uncertainties` _(A · 🔒 enum)_ | context_insufficient · anecdotal_single_source | anecdotal_single_source · source_date_unclear · context_insufficient |

**Criterios vigentes en este batch:**

- Sonnet — ninguna adicion formulada aun; solo criterios base.
- Fable — ninguna adicion formulada aun; solo criterios base.

**Veredicto:**


---

## Caso 6 — `ER-SP-compass_artifact_wf-28ef9d76-a020-462a-83e9-3321b6ece5b4_text_markdown_normalized-013-SNP-001`

- **Batch de origen:** batch_005
- **Estrato:** E1

**snippet_primary:**

> "I'm still fairly new to using Payhip and have two stores on their platform. What I most like about them is that you can set up your store with no upfront costs. You just pay 5% commission to Payhip on sales. So it's great for beginners. You can build blogs on their platform and custom pages. On one of my stores, I have set up my own Ebook products, where Payhip handles the UK and EU VAT. (As a comparison, on Amazon's KDP system you'd be paying them 30% on sales instead of 5%, and only if you price your Ebooks below $10.)"

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(A · 📝 texto libre)_ | no upfront costs · you just pay 5% commission to Payhip on sales · only if you price your Ebooks below $10 (Amazon KDP) | I'm still fairly new to using Payhip · with no upfront costs · So it's great for beginners |
| `metric_unit` _(A · 📝 texto libre)_ | percent | percent commission on sales |
| `metric_value_raw` _(A · 📝 texto libre)_ | 5% (Payhip) vs 30% (Amazon KDP, below $10 price) | 5% |
| `parser_notes` _(A · 📝 texto libre)_ | Reviewer distinguishes Payhip's VAT-handling role from its commission rate; both preserved as separate qualifiers rather than merged. | Comparator in snippet: Amazon KDP '30% on sales instead of 5%, and only if you price your Ebooks below $10'. · Reviewer is a seller with two Payhip stores; product explicitly 'Ebook products'. |
| `subject_exact` _(A · 📝 texto libre)_ | Seller review comparing Payhip's 5% commission and VAT handling to Amazon KDP's 30% ebook royalty cut below the $10 price threshold | seller review of Payhip: free store setup with 5% sales commission, blog and custom pages, and UK/EU VAT handling for own ebook products |
| `uncertainties` _(A · 🔒 enum)_ | anecdotal_single_source | anecdotal_single_source · source_date_unclear |

**Criterios vigentes en este batch:**

- Sonnet — ninguna adicion formulada aun; solo criterios base.
- Fable — ninguna adicion formulada aun; solo criterios base.

**Veredicto:**


---

## Caso 7 — `ER-SP-compass_artifact_wf-28ef9d76-a020-462a-83e9-3321b6ece5b4_text_markdown_normalized-022-SNP-001`

- **Batch de origen:** batch_006
- **Estrato:** E1

**snippet_primary:**

> "Every new entrepreneur selling digital products needs to use this product. I've seen online gurus recommending other platforms (probably because they have an ongoing partnerships), but Payhip is the BEST one for small entrepreneurs who can't afford the $XX per month fees that most platforms like Shopify charge. Their pricing starts at $0 per month with 5% transaction fee, I can't find any other platforms that have prices as low as this."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(A · 📝 texto libre)_ | speculates other reviewers recommend competitors due to undisclosed partnerships | Their pricing starts at $0 per month · for small entrepreneurs who can't afford the $XX per month fees that most platforms like Shopify charge · (probably because they have an ongoing partnerships) · I can't find any other platforms that have prices as low as this |
| `metric_unit` _(A · 📝 texto libre)_ | USD / percent | percent transaction fee |
| `metric_value_raw` _(A · 📝 texto libre)_ | $0/month; 5% | 5% |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | Additional figure in snippet: starting price '$0 per month'; Shopify fees given only as '$XX per month'. · Sitejabber review by a digital-products seller; promotional emphasis remains in snippet only. |
| `subject_exact` _(A · 📝 texto libre)_ | Seller review recommending Payhip over other platforms for small entrepreneurs based on its low starting price and transaction fee | seller review praising Payhip $0/month plus 5% transaction fee pricing versus monthly-fee platforms like Shopify |
| `uncertainties` _(A · 🔒 enum)_ | anecdotal_single_source · author_conflict_of_interest_possible | anecdotal_single_source · source_date_unclear |

**Criterios vigentes en este batch:**

- Sonnet — ninguna adicion formulada aun; solo criterios base.
- Fable — ninguna adicion formulada aun; solo criterios base.

**Veredicto:**


---

## Caso 8 — `ER-SP-compass_artifact_wf-291008ae-711f-4c29-83eb-6a5c8ef0eef8_text_markdown_normalized-002-SNP-003`

- **Batch de origen:** batch_007
- **Estrato:** E1

**snippet_primary:**

> "This is the payment processor for revid.ai. They are both scams. One star because I can't give 0. Impossible to speak with a live person, impossible to cancel your revid.ai account with an active Lemonsqueezy account, and impossible to cancel. Fraud."

| Campo | Sonnet | Fable |
|---|---|---|
| `claim_type` _(A · 🔒 enum)_ | review_statement | anecdotal_report |
| `local_qualifiers` _(A · 📝 texto libre)_ | impossible to cancel your revid.ai account with an active Lemonsqueezy account | Impossible to speak with a live person · impossible to cancel your revid.ai account with an active Lemonsqueezy account |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | Valorative wording ('scams', 'Fraud') remains in snippet only. |
| `platforms` _(A · 📝 texto libre)_ | Lemon Squeezy · revid.ai | Revid · Lemon Squeezy |
| `subject_exact` _(A · 📝 texto libre)_ | Buyer review describing Lemon Squeezy and revid.ai together as impossible to cancel or reach a live person for | buyer-reported inability to reach a live person or cancel a revid.ai account tied to an active Lemonsqueezy subscription |

**Criterios vigentes en este batch:**

- Sonnet — ninguna adicion formulada aun; solo criterios base.
- Fable — ninguna adicion formulada aun; solo criterios base.

**Veredicto:**


---

## Caso 9 — `ER-SP-compass_artifact_wf-295a3f4a-2ebb-4c3b-9b1d-9b7d3840172c_text_markdown-007-SNP-001`

- **Batch de origen:** batch_008
- **Estrato:** E1

**snippet_primary:**

> "Kichink puede ofrecer servicios a usuarios en todo el mundo. Si usa nuestros servicios dentro o fuera de México, Kichink Servicios, S.A. de C.V. es el responsable de la administración de sus datos personales."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(B · 📝 texto libre)_ | _(lista vacia)_ | puede ofrecer servicios a usuarios en todo el mundo · dentro o fuera de México |
| `subject_exact` _(A · 📝 texto libre)_ | Kichink privacy policy statement on data-controller responsibility for users inside or outside Mexico | Kichink Servicios S.A. de C.V. as data controller for users inside or outside Mexico, with services offered worldwide |
| `uncertainties` _(A · 🔒 enum)_ | none | source_date_unclear |

**Criterios vigentes en este batch:**

- Sonnet — ninguna adicion formulada aun; solo criterios base.
- Fable — ninguna adicion formulada aun; solo criterios base.

**Veredicto:**


---

## Caso 10 — `ER-SP-compass_artifact_wf-3128bd63-7fd1-4bd6-86d1-63a1780fe467_text_markdown-003-SNP-004`

- **Batch de origen:** batch_008
- **Estrato:** E1

**snippet_primary:**

> "Even if your country does not have a treaty with the US, it is beneficial for you to submit your tax information. By submitting your tax information, your earnings from non-US buyers will not be subject to US taxes. Note, however, that your royalty income from US buyers will attract 30% royalty withholding tax."

| Campo | Sonnet | Fable |
|---|---|---|
| `geography_if_explicit` _(A · 📝 texto libre)_ | US | the US |
| `local_qualifiers` _(B · 📝 texto libre)_ | _(lista vacia)_ | Even if your country does not have a treaty with the US · Note, however |
| `metric_type` _(A · 🔒 enum)_ | fee_rate | tax_withholding_rate |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | metric_type out of enum: observed metric is a tax withholding rate; no enum value covers it. · Platform name appears only in source_title/URL; platforms left empty per criteria F. |
| `platforms` _(B · 📝 texto libre)_ | Envato | _(lista vacia)_ |
| `subject_exact` _(A · 📝 texto libre)_ | Envato guidance that submitting tax information benefits authors in non-treaty countries by exempting non-US-buyer earnings from US tax, while US-buyer earnings still face 30% withholding | benefit of submitting tax information without a US treaty: non-US-buyer earnings not subject to US taxes, while US-buyer royalties attract 30% withholding |
| `uncertainties` _(A · 🔒 enum)_ | none | source_date_unclear |

**Criterios vigentes en este batch:**

- Sonnet — ninguna adicion formulada aun; solo criterios base.
- Fable — ninguna adicion formulada aun; solo criterios base.

**Veredicto:**


---

## Caso 11 — `ER-SP-compass_artifact_wf-345ae7ea-8655-485d-821e-f35693f6a78f_text_markdown-007-SNP-001`

- **Batch de origen:** batch_009
- **Estrato:** E1

**snippet_primary:**

> "Created a 'reading log template' in half an hour. Designed a small set of motivational quote posters (A4 JPGs). Wrote a short guide: '5 Tricks to Build a Micro‑business in a Weekend.' Within 24 hours I had three live products. Tested $1 prices, $5, and the pay‑what‑you‑want model. I shared links in Facebook groups for writers, on LinkedIn, even in a Slack community. One sale here, two there. By day end, $20 in revenue — not earth‑shattering, but a proof of concept."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(A · 📝 texto libre)_ | not earth-shattering, but a proof of concept | Tested $1 prices, $5, and the pay‑what‑you‑want model · not earth‑shattering, but a proof of concept |
| `metric_unit` _(A · 📝 texto libre)_ | USD | USD (first day) |
| `parser_notes` _(A · 📝 texto libre)_ | three distinct product types were created (reading log template, motivational quote posters, short guide); none maps unambiguously to a single schema product_type_if_explicit enum value, so left unknown rather than forced | Products explicitly named (reading log template; motivational quote posters A4 JPGs; short guide) but they span types not covered by the product-type enum with no dominant type; set to unknown. · Selling platform (Payhip) named only in source_title/URL, not in snippet text; platforms left empty of it per criteria F. |
| `platforms` _(A · 📝 texto libre)_ | Payhip · Facebook · LinkedIn · Slack | Facebook · LinkedIn · Slack |
| `subject_exact` _(A · 📝 texto libre)_ | seller-reported first-day revenue from newly launched digital products on Payhip | seller-reported one-day launch of three products (reading log template, quote posters, short guide) with price testing and $20 first-day revenue |
| `time_scope_raw` _(A · 📝 texto libre)_ | within 24 hours | Within 24 hours … By day end |
| `uncertainties` _(A · 🔒 enum)_ | anecdotal_single_source · product_type_unclear | anecdotal_single_source · source_date_unclear |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008)

**Veredicto:**


---

## Caso 12 — `ER-SP-compass_artifact_wf-394dae4a-6a0d-4d19-af44-9adf808718dc_text_markdown-002-SNP-005`

- **Batch de origen:** batch_009
- **Estrato:** E1

**snippet_primary:**

> "Since February 2024, we have been automatically transferring all sales commissions available for withdrawal in currencies other than Brazilian Real (BRL) on a monthly basis."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(A · 📝 texto libre)_ | currencies other than Brazilian Real (BRL) · on a monthly basis | on a monthly basis · in currencies other than Brazilian Real (BRL) |
| `metric_type` _(A · 🔒 enum)_ | payout | unknown |
| `parser_notes` _(A · 📝 texto libre)_ | Brazilian Real is a currency reference implying Brazil geography but not an explicit place-name statement; geography_if_explicit left null for consistency with other currency-only mentions in this batch | Platform name appears only in source_ref URL; platforms left empty per criteria F. |
| `platforms` _(B · 📝 texto libre)_ | Hotmart | _(lista vacia)_ |
| `subject_exact` _(A · 📝 texto libre)_ | automatic monthly transfer policy for Hotmart commissions held in non-BRL currencies | automatic monthly transfer of all withdrawable non-BRL sales commissions since February 2024 |
| `uncertainties` _(B · 🔒 enum)_ | _(lista vacia)_ | source_date_unclear |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008)

**Veredicto:**


---

## Caso 13 — `ER-SP-compass_artifact_wf-394dae4a-6a0d-4d19-af44-9adf808718dc_text_markdown-008-SNP-001`

- **Batch de origen:** batch_010
- **Estrato:** E1

**snippet_primary:**

> "Before joining Hotmart, Martínez, the car repair creator, hadn't been able to charge clients outside of his native market of Costa Rica. Although many were willing to pay his $20 monthly subscription fee, they couldn't find a way around PayPal's geographic payment restrictions."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(A · 📝 texto libre)_ | couldn't find a way around PayPal's geographic payment restrictions | Before joining Hotmart · Although many were willing to pay |
| `metric_type` _(A · 🔒 enum)_ | payment_method_availability | price |
| `metric_unit` _(A · 📝 texto libre)_ | USD | USD per month (subscription fee) |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | Third-person journalistic narration of one creator's case; assigned 'source'. |
| `subject_exact` _(A · 📝 texto libre)_ | reported inability of a Costa Rica-based creator to charge international clients via PayPal prior to joining Hotmart | reported inability of a Costa Rica-based creator to charge clients abroad before Hotmart, due to PayPal geographic payment restrictions, despite willingness to pay the $20 monthly subscription |
| `time_scope_raw` _(A · 📝 texto libre)_ | monthly | Before joining Hotmart |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008)

**Veredicto:**


---

## Caso 14 — `ER-SP-compass_artifact_wf-394dae4a-6a0d-4d19-af44-9adf808718dc_text_markdown-008-SNP-002`

- **Batch de origen:** batch_010
- **Estrato:** E1

**snippet_primary:**

> "'Hotmart has a really good advantage: They accept all payment processors, credit cards, even cash payments in cornershops like Oxxo,' Sofía Macías, a personal finance creator, told Rest of World."

| Campo | Sonnet | Fable |
|---|---|---|
| `claim_type` _(A · 🔒 enum)_ | review_statement | explicit_claim |
| `evidence_role` _(A · 🔒 enum)_ | reported_event | direct_claim |
| `local_qualifiers` _(B · 📝 texto libre)_ | _(lista vacia)_ | even cash payments in cornershops like Oxxo |
| `parser_notes` _(A · 📝 texto libre)_ | quote is mediated through journalist reporting (Rest of World) rather than a first-person seller post; actor_level set to seller reflecting the quoted speaker, actor_level_unclear flagged for the mediated framing | Direct quote from a creator (seller voice) in a journalistic article; 'really good advantage' is the speaker's wording, preserved in snippet only. · time_scope_normalized_if_safe from source_date_if_available ('June 19, 2023') per criteria G/K1 (state claim at publication). |
| `subject_exact` _(A · 📝 texto libre)_ | creator-reported payment method breadth of Hotmart (processors, credit cards, cash payments via Oxxo) | creator-quoted claim that Hotmart accepts all payment processors, credit cards and cash payments at cornershops like Oxxo |
| `time_scope_normalized_if_safe` _(B · 📝 texto libre)_ | _(null)_ | 2023-06-19 |
| `uncertainties` _(A · 🔒 enum)_ | anecdotal_single_source · actor_level_unclear | anecdotal_single_source |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008)

**Veredicto:**


---

## Caso 15 — `ER-SP-compass_artifact_wf-4ff72059-9383-471e-a419-d446777044ad_text_markdown-004-SNP-008`

- **Batch de origen:** batch_014
- **Estrato:** E1

**snippet_primary:**

> "El apartado Forma de pago pide seleccionar como medio de pago cualquiera de las opciones que se ofrecen: cuenta Kash®; Tarjeta de crédito o débito; Depósito Bancario; Depósito en Tiendas con convenio; Pago en Puerta (sujeto a la disponibilidad de acuerdo con la opción de entrega BIP®)."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(A · 📝 texto libre)_ | Pago en Puerta sujeto a la disponibilidad de acuerdo con la opción de entrega BIP | (sujeto a la disponibilidad de acuerdo con la opción de entrega BIP®) |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | 'Kash®' is the platform's own prepaid account, named in text; 'BIP®' is the platform's delivery option, not listed as platform. · Platform name appears only in source_ref URL for this snippet. |
| `platforms` _(A · 📝 texto libre)_ | Kichink | Kash |
| `subject_exact` _(A · 📝 texto libre)_ | Kichink checkout payment method options (Kash account, credit/debit card, bank deposit, affiliated-store deposit, cash-on-delivery subject to BIP delivery availability) | checkout payment options: Kash account, credit/debit card, bank deposit, deposit at partner stores, and pago en puerta subject to BIP delivery availability |
| `uncertainties` _(B · 🔒 enum)_ | _(lista vacia)_ | source_date_unclear |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008)

**Veredicto:**


---

## Caso 16 — `ER-SP-compass_artifact_wf-5c07963d-6c4c-4536-a602-03c04203e92c_text_markdown-013-SNP-001`

- **Batch de origen:** batch_015
- **Estrato:** E1

**snippet_primary:**

> "Unlike Etsy, which charges $0.20 per listing every four months, Amazon lets you list as many products as you want for free. You only pay when something sells. Amazon charges a flat 15% referral fee on every sale. This is much higher than Etsy's 6.5% transaction fee. While Amazon's fee includes payment processing, the total cost per sale is still significantly higher."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(A · 📝 texto libre)_ | Amazon's fee includes payment processing | You only pay when something sells · While Amazon's fee includes payment processing |
| `metric_unit` _(A · 📝 texto libre)_ | USD/percent | percent per sale (Amazon) |
| `metric_value_raw` _(A · 📝 texto libre)_ | $0.20 (Etsy listing) / 6.5% (Etsy transaction) / 15% (Amazon referral) | a flat 15% referral fee |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | Comparator figures in snippet: Etsy '$0.20 per listing every four months' and '6.5% transaction fee'. · source_date_if_available is year-only ('2026'); not normalized. |
| `subject_exact` _(A · 📝 texto libre)_ | comparative fee-structure claim between Etsy ($0.20 listing, 6.5% transaction) and Amazon (free listing, flat 15% referral fee) | fee comparison: Amazon free unlimited listings with flat 15% referral fee (processing included) versus Etsy $0.20 per listing every four months and 6.5% transaction fee |
| `uncertainties` _(B · 🔒 enum)_ | _(lista vacia)_ | source_date_unclear |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008)

**Veredicto:**


---

## Caso 17 — `ER-SP-compass_artifact_wf-5c07963d-6c4c-4536-a602-03c04203e92c_text_markdown-018-SNP-001`

- **Batch de origen:** batch_015
- **Estrato:** E1

**snippet_primary:**

> "Amazon Handmade integrates into the larger Amazon marketplace of mass-produced products, so some customers might not be intentionally looking for handmade goods. Etsy is an online marketplace for vintage and handmade goods from around the globe. Founded as a small Brooklyn shop in 2005, Etsy has grown into an ecommerce hub with a global customer base of nearly 90 million active buyers in 2024. Those buyers are often intentionally seeking handmade goods, and some are looking for products with personalization options."

| Campo | Sonnet | Fable |
|---|---|---|
| `claim_type` _(A · 🔒 enum)_ | statistical_data | comparative_commentary |
| `local_qualifiers` _(A · 📝 texto libre)_ | Founded as a small Brooklyn shop in 2005 | Founded as a small Brooklyn shop in 2005 · some customers might not be intentionally looking for handmade goods · some are looking for products with personalization options |
| `metric_type` _(A · 🔒 enum)_ | unknown | active_buyers |
| `parser_notes` _(A · 📝 texto libre)_ | source is Shopify's own blog; Shopify is a competing platform to Etsy | Blog hosted by Shopify, a competing platform. · 'Brooklyn' appears as founding-location narrative, not claim geography; geography left null. |
| `platforms` _(A · 📝 texto libre)_ | Amazon Handmade · Etsy | Amazon Handmade · Amazon · Etsy |
| `subject_exact` _(A · 📝 texto libre)_ | Etsy founding year and active buyer count claim (nearly 90 million active buyers in 2024) | Etsy characterization as global vintage/handmade marketplace with nearly 90 million active buyers in 2024 intentionally seeking handmade goods, versus Amazon Handmade embedded among mass-produced products |
| `uncertainties` _(A · 🔒 enum)_ | author_conflict_of_interest_possible | source_date_unclear · author_conflict_of_interest_possible |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008)

**Veredicto:**


---

## Caso 18 — `ER-SP-compass_artifact_wf-5c07963d-6c4c-4536-a602-03c04203e92c_text_markdown-021-SNP-001`

- **Batch de origen:** batch_015
- **Estrato:** E1

**snippet_primary:**

> "The constant debate of Redbubble vs Etsy often stems from a misunderstanding of their core business models. One is a hands-off marketplace for artists, while the other is a bustling hub for hands-on creators."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(B · 📝 texto libre)_ | _(lista vacia)_ | often stems from a misunderstanding of their core business models |
| `subject_exact` _(A · 📝 texto libre)_ | characterization of Redbubble as a hands-off print-on-demand marketplace versus Etsy as a hands-on creator marketplace | business-model contrast: Redbubble as hands-off marketplace for artists versus Etsy as hub for hands-on creators |
| `uncertainties` _(B · 🔒 enum)_ | _(lista vacia)_ | source_date_unclear |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008)

**Veredicto:**


---

## Caso 19 — `ER-SP-compass_artifact_wf-63c228bc-9037-4ba4-9569-3f62e8735192_text_markdown-011-SNP-007`

- **Batch de origen:** batch_016
- **Estrato:** E1

**snippet_primary:**

> "I am a digital product seller and I sell items with full resale rights (PLR/MRR). Gumroad suddenly suspended my account without sending me any email or warning. I had over $250 in my balance..."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(A · 📝 texto libre)_ | sells items with full resale rights (PLR/MRR) · no email or warning given before suspension | without sending me any email or warning · I sell items with full resale rights (PLR/MRR) |
| `metric_unit` _(A · 📝 texto libre)_ | USD | USD balance |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | Snippet truncated with ellipsis; outcome not captured. |
| `subject_exact` _(A · 📝 texto libre)_ | seller-reported sudden Gumroad account suspension without warning while holding over $250 in balance, selling resale-rights (PLR/MRR) digital products | seller of full-resale-rights (PLR/MRR) products reporting sudden Gumroad suspension without email or warning, with an over-$250 balance |
| `uncertainties` _(A · 🔒 enum)_ | anecdotal_single_source | anecdotal_single_source · snippet_needs_reopen |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008)

**Veredicto:**


---

## Caso 20 — `ER-SP-compass_artifact_wf-6b226a5c-1235-4d40-a521-ad9932514aff_text_markdown-004-SNP-003`

- **Batch de origen:** batch_016
- **Estrato:** E1

**snippet_primary:**

> [Stated in layout: "1% per payout for bank accounts outside the US"]

| Campo | Sonnet | Fable |
|---|---|---|
| `geography_if_explicit` _(B · 📝 texto libre)_ | outside the US | _(null)_ |
| `metric_unit` _(A · 📝 texto libre)_ | percent | percent per payout |
| `metric_value_raw` _(A · 📝 texto libre)_ | 1% | 1% per payout for bank accounts outside the US |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | snippet_primary is layout-derived (bracketed reconstruction), not prose verbatim. · 'outside the US' is a negated geographic scope; geography left null. · Platform name appears only in source_ref URL; platforms left empty per criteria F. |
| `platforms` _(B · 📝 texto libre)_ | Lemon Squeezy | _(lista vacia)_ |
| `subject_exact` _(A · 📝 texto libre)_ | Lemon Squeezy payout fee for bank accounts outside the US (1% per payout) | 1% per-payout fee for bank accounts outside the US |
| `uncertainties` _(B · 🔒 enum)_ | _(lista vacia)_ | source_date_unclear |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008)

**Veredicto:**


---

## Caso 21 — `ER-SP-compass_artifact_wf-7a40dcc5-be9a-4273-a3e8-0d53cab18fb3_text_markdown_normalized-012-SNP-002`

- **Batch de origen:** batch_017
- **Estrato:** E2

**snippet_primary:**

> "I did the hard work and I take all of my own photos, make all of my own mockups, and all of my other designs. I also make all of my own products that I put my designs on, and I do it myself within my own business. Everyone should have to do the same on Etsy. It's about time that Etsy changed the rules to protect real artists."

| Campo | Sonnet | Fable |
|---|---|---|
| `claim_type` _(A · 🔒 enum)_ | explicit_claim | anecdotal_report |
| `local_qualifiers` _(B · 📝 texto libre)_ | _(lista vacia)_ | I did the hard work · and I do it myself within my own business · Everyone should have to do the same on Etsy |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | 'protect real artists' is the seller's advocacy framing, preserved in qualifiers/snippet as source wording. |
| `subject_exact` _(A · 📝 texto libre)_ | seller self-description of independently producing designs and products in support of Etsy Creativity Standards enforcement | seller-reported full self-production workflow (own photos, mockups, designs, products) and endorsement of Etsy rule changes protecting self-producing artists |
| `uncertainties` _(A · 🔒 enum)_ | none | anecdotal_single_source |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016)

**Veredicto:**


---

## Caso 22 — `ER-SP-compass_artifact_wf-7b6a9899-eda3-4893-93ba-3553f79cab42_text_markdown-002-SNP-001`

- **Batch de origen:** batch_018
- **Estrato:** E2

**snippet_primary:**

> "NO es claro lo del dinero pues debe ser mas sencillo que lo envien a la cuenta que ya autorizaron sin problema , pues son 7 dias de garantia para el cliente y luego porque no puedo usar mi dinero , en fin es eso muy revuelto. De lo bueno son una plataforma muy accesible y segura para vender asi que unas por otras , ojala mejoren para dar mas difusión a los clientes y pagos prontos pero estan en la media , por eso solo 3 estrellas merecen en mi opinion."

| Campo | Sonnet | Fable |
|---|---|---|
| `actor_level` _(A · 🔒 enum)_ | buyer | seller |
| `evidence_role` _(A · 🔒 enum)_ | reported_event | seller_self_claim |
| `local_qualifiers` _(B · 📝 texto libre)_ | _(lista vacia)_ | pues son 7 dias de garantia para el cliente y luego porque no puedo usar mi dinero · De lo bueno son una plataforma muy accesible y segura para vender · estan en la media |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | Platform named only in source_ref URL; platforms left empty per criteria F. |
| `platforms` _(B · 📝 texto libre)_ | Hotmart | _(lista vacia)_ |
| `subject_exact` _(A · 📝 texto libre)_ | buyer-reported dissatisfaction with Hotmart fund release timing and account withdrawal restrictions | seller review criticizing unclear fund release tied to the 7-day buyer guarantee while rating the platform accessible and secure (3 stars) |
| `time_scope_raw` _(A · 📝 texto libre)_ | 7 dias de garantia (7-day guarantee period) | 7 dias de garantia |
| `uncertainties` _(A · 🔒 enum)_ | none | anecdotal_single_source |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016)

**Veredicto:**


---

## Caso 23 — `ER-SP-compass_artifact_wf-7b6a9899-eda3-4893-93ba-3553f79cab42_text_markdown-005-SNP-001`

- **Batch de origen:** batch_018
- **Estrato:** E2

**snippet_primary:**

> "Como productor esta plataforma es una estafa. Además de ser de mala calidad, lenta y para nada cómoda para interactuar con estudiantes. El servicio al cliente es pésimo y responden siempre con resp..."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(B · 📝 texto libre)_ | _(lista vacia)_ | Como productor · El servicio al cliente es pésimo |
| `parser_notes` _(A · 📝 texto libre)_ | Snippet truncated with trailing ellipsis mid-sentence. | Snippet truncated mid-word ('resp...'); valorative wording ('estafa') remains in snippet only. · Platform named only in source_ref URL; platforms left empty per criteria F. |
| `platforms` _(B · 📝 texto libre)_ | Hotmart | _(lista vacia)_ |
| `subject_exact` _(A · 📝 texto libre)_ | seller-reported dissatisfaction with Hotmart platform quality and customer service | producer review describing the platform as low quality, slow, uncomfortable for student interaction, with poor scripted customer service |
| `uncertainties` _(A · 🔒 enum)_ | context_insufficient | anecdotal_single_source · snippet_needs_reopen |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016)

**Veredicto:**


---

## Caso 24 — `ER-SP-compass_artifact_wf-7df7092c-4929-4bbe-b35f-a7efa126b514_text_markdown_normalized-006-SNP-001`

- **Batch de origen:** batch_019
- **Estrato:** E2

**snippet_primary:**

> "Hi, I see Individual plan From $16.50/month but when I go to purchase this plan, it shows $33/m with vat it is $39. Why is the different showing?"

| Campo | Sonnet | Fable |
|---|---|---|
| `claim_type` _(A · 🔒 enum)_ | explicit_claim | anecdotal_report |
| `evidence_role` _(A · 🔒 enum)_ | unknown | anecdotal_example |
| `local_qualifiers` _(B · 📝 texto libre)_ | _(lista vacia)_ | when I go to purchase this plan |
| `metric_unit` _(A · 📝 texto libre)_ | USD | USD per month |
| `metric_value_raw` _(A · 📝 texto libre)_ | $16.50/month advertised vs $33/m with VAT ($39) | From $16.50/month … $33/m with vat it is $39 |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | Three price figures preserved verbatim: advertised $16.50/month; checkout $33/month; $39 with VAT. |
| `platforms` _(A · 📝 texto libre)_ | Envato Elements | Envato |
| `subject_exact` _(A · 📝 texto libre)_ | buyer-reported discrepancy between advertised and checkout price for Envato Elements Individual plan | buyer-reported discrepancy between advertised 'From $16.50/month' Individual plan and $33/month at checkout ($39 with VAT) |
| `uncertainties` _(A · 🔒 enum)_ | none | source_date_unclear · anecdotal_single_source |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016)

**Veredicto:**


---

## Caso 25 — `ER-SP-compass_artifact_wf-7df7092c-4929-4bbe-b35f-a7efa126b514_text_markdown_normalized-012-SNP-001`

- **Batch de origen:** batch_019
- **Estrato:** E2

**snippet_primary:**

> "Most reviewers were unhappy with their experience overall. Many customers expressed dissatisfaction with the products, citing issues such as outdated content, faulty files, and items not matching descriptions."

| Campo | Sonnet | Fable |
|---|---|---|
| `evidence_role` _(A · 🔒 enum)_ | comparative_commentary | local_context |
| `local_qualifiers` _(B · 📝 texto libre)_ | _(lista vacia)_ | Most reviewers · Many customers |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | Aggregated summary text (likely platform-generated review synthesis), not an individual reviewer's voice; assigned 'source'. · Platform named only in source_ref URL; platforms left empty per criteria F. |
| `platforms` _(B · 📝 texto libre)_ | Envato Market | _(lista vacia)_ |
| `subject_exact` _(A · 📝 texto libre)_ | third-party aggregate sentiment summary of Envato Market buyer reviews | aggregate review summary: most reviewers unhappy, citing outdated content, faulty files and items not matching descriptions |
| `uncertainties` _(A · 🔒 enum)_ | methodology_unclear | source_date_unclear · methodology_unclear |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016)

**Veredicto:**


---

## Caso 26 — `ER-SP-compass_artifact_wf-80dc1a5e-cdb7-4f06-a0fb-62209a2ddd08_text_markdown-006-SNP-002`

- **Batch de origen:** batch_020
- **Estrato:** E2

**snippet_primary:**

> "I've been trying to transfer my money from the store for 3 months now. Customer support is slow and just deflects the questions. Stay away."

| Campo | Sonnet | Fable |
|---|---|---|
| `claim_type` _(A · 🔒 enum)_ | review_statement | anecdotal_report |
| `local_qualifiers` _(B · 📝 texto libre)_ | _(lista vacia)_ | Customer support is slow and just deflects the questions |
| `metric_type` _(A · 🔒 enum)_ | payout | unknown |
| `metric_unit` _(B · 📝 texto libre)_ | months | _(null)_ |
| `metric_value_raw` _(B · 📝 texto libre)_ | 3 months | _(null)_ |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | Platform named only in source_ref URL; platforms left empty per criteria F. |
| `platforms` _(B · 📝 texto libre)_ | Lemon Squeezy | _(lista vacia)_ |
| `subject_exact` _(A · 📝 texto libre)_ | seller-reported Lemon Squeezy delay transferring seller store funds | seller-reported 3 months attempting to transfer money out of the store with slow, deflecting customer support |
| `time_scope_raw` _(B · 📝 texto libre)_ | _(null)_ | for 3 months now |
| `uncertainties` _(A · 🔒 enum)_ | none | anecdotal_single_source |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016)

**Veredicto:**


---

## Caso 27 — `ER-SP-compass_artifact_wf-83a235d5-86a0-4c10-9097-e29688c3b834_text_markdown_normalized-016-SNP-017`

- **Batch de origen:** batch_022
- **Estrato:** E2

**snippet_primary:**

> "Sellers may be required to pay the following types of fees. Please note that all fees are listed exclusive of any value-added tax (VAT) or similar taxes that may apply. See the Taxes section below for further details. It's important to note that all service fees, including prepaid fees, are non-refundable."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(A · 📝 texto libre)_ | all service fees, including prepaid fees, are non-refundable | exclusive of any value-added tax (VAT) or similar taxes that may apply · all service fees, including prepaid fees, are non-refundable |
| `metric_type` _(A · 🔒 enum)_ | fee_rate | unknown |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | Platform named only in source_ref URL; platforms left empty per criteria F. |
| `platforms` _(B · 📝 texto libre)_ | Etsy | _(lista vacia)_ |
| `subject_exact` _(A · 📝 texto libre)_ | Etsy seller fees stated exclusive of VAT and non-refundable status of service fees | seller fees listed exclusive of VAT or similar taxes, with all service fees including prepaid fees being non-refundable |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016)

**Veredicto:**


---

## Caso 28 — `ER-SP-compass_artifact_wf-a714e31c-2e2c-4735-a50c-9e9535323a2c_text_markdown-003-SNP-001`

- **Batch de origen:** batch_026
- **Estrato:** E2

**snippet_primary:**

> "Hotmart es en realidad una plataforma de cursos independiente, aunque es tan completa que merece su propia categoría dentro del mercado de la afiliación. Podríamos decir que es algo así como una combinación de Udemy con Teachable y la archiconocida ClickBank. Una mezcla explosiva… ¿eh?"

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(B · 📝 texto libre)_ | _(lista vacia)_ | Podríamos decir que es algo así como |
| `subject_exact` _(A · 📝 texto libre)_ | blog author's categorization of Hotmart as a hybrid course/affiliate marketplace distinct from Udemy or Teachable | characterization of Hotmart as an independent course platform combining traits of Udemy, Teachable and ClickBank within affiliate marketing |
| `uncertainties` _(A · 🔒 enum)_ | none | source_date_unclear |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016)

**Veredicto:**


---

## Caso 29 — `ER-SP-compass_artifact_wf-a714e31c-2e2c-4735-a50c-9e9535323a2c_text_markdown-012-SNP-001`

- **Batch de origen:** batch_026
- **Estrato:** E2

**snippet_primary:**

> "Hotmart actualmente está en el número de las plataformas para vender cursos en forma de infoproductos digitales por su fácil uso, formación gratuita, y registro gratis. Desbancando así a ClickBank. [...] Realmente Clickbank prácticamente no se utilizar en el mundo hispano, pues el mercado hispano se ha trasladado a Hotmart, muchísimo mejor con diferencia."

| Campo | Sonnet | Fable |
|---|---|---|
| `geography_if_explicit` _(B · 📝 texto libre)_ | mundo hispano | _(null)_ |
| `local_qualifiers` _(A · 📝 texto libre)_ | por su fácil uso, formación gratuita, y registro gratis | Realmente Clickbank prácticamente no se utilizar en el mundo hispano · el mercado hispano se ha trasladado a Hotmart |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | 'muchísimo mejor con diferencia' is the author's valorative wording; market-shift claim unquantified. · 'el mundo hispano' is a market descriptor, not claim geography wording; geography left null. |
| `subject_exact` _(A · 📝 texto libre)_ | blog author's claim that Hotmart displaced ClickBank in the Hispanic market for digital-course sales | claim that Hotmart displaced ClickBank in the Hispanic infoproduct market thanks to ease of use, free training and free registration |
| `uncertainties` _(A · 🔒 enum)_ | none | source_date_unclear · methodology_unclear |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016)

**Veredicto:**


---

## Caso 30 — `ER-SP-compass_artifact_wf-a714e31c-2e2c-4735-a50c-9e9535323a2c_text_markdown-015-SNP-001`

- **Batch de origen:** batch_026
- **Estrato:** E2

**snippet_primary:**

> "La principal diferencia de Hotmart respecto a otros marketplaces como Udemy, es que Hotmart cuenta con una estructura un poco más compleja y tiene 'el afiliado' para revender tus productos que Udemy, por ejemplo, no tiene."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(B · 📝 texto libre)_ | _(lista vacia)_ | una estructura un poco más compleja · que Udemy, por ejemplo, no tiene |
| `subject_exact` _(A · 📝 texto libre)_ | blog author's comparison of Hotmart's affiliate-reseller structure against Udemy's lack of one | differentiation of Hotmart from marketplaces like Udemy via its affiliate reseller system and somewhat more complex structure |
| `uncertainties` _(A · 🔒 enum)_ | none | source_date_unclear |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016)

**Veredicto:**


---

## Caso 31 — `ER-SP-compass_artifact_wf-a943ee9d-6e80-4080-a978-da2156eaae41_text_markdown-003-SNP-002`

- **Batch de origen:** batch_027
- **Estrato:** E2

**snippet_primary:**

> "GMS transacted on the Etsy app grew 6.6% year-over-year, and represented approximately 46% of GMS."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(A · 📝 texto libre)_ | GMS transacted on the Etsy app | approximately |
| `metric_type` _(A · 🔒 enum)_ | revenue | GMS |
| `metric_unit` _(A · 📝 texto libre)_ | percent | percent (GMS growth and share) |
| `metric_value_raw` _(A · 📝 texto libre)_ | grew 6.6% year-over-year; approximately 46% of GMS | grew 6.6% year-over-year … approximately 46% of GMS |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | metric_type out of enum: observed label 'GMS' (gross merchandise sales) copied verbatim; GMS is transaction volume, not platform revenue, so the revenue enum value would collapse layers (Rule 1). · Company's own earnings press release. · time_scope_normalized_if_safe from source_date_if_available ('February 19, 2026') per criteria G/K1. |
| `subject_exact` _(A · 📝 texto libre)_ | Etsy's own disclosed app-transacted GMS growth and share of total GMS | Etsy app GMS growth of 6.6% YoY, representing approximately 46% of GMS (Q4 2025) |
| `time_scope_normalized_if_safe` _(B · 📝 texto libre)_ | _(null)_ | 2026-02-19 |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016)

**Veredicto:**


---

## Caso 32 — `ER-SP-compass_artifact_wf-a943ee9d-6e80-4080-a978-da2156eaae41_text_markdown-014-SNP-003`

- **Batch de origen:** batch_028
- **Estrato:** E2

**snippet_primary:**

> "etsy.com's audience is 41.74% male and 58.26% female. The largest age group of visitors are 25 - 34 year olds."

| Campo | Sonnet | Fable |
|---|---|---|
| `metric_type` _(A · 🔒 enum)_ | unknown | audience demographics |
| `metric_unit` _(A · 📝 texto libre)_ | percent | percent of audience |
| `metric_value_raw` _(A · 📝 texto libre)_ | 41.74% male; 58.26% female | 41.74% male and 58.26% female |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | metric_type out of enum: observed metric is audience demographic shares; no enum value covers it. · time_scope_normalized_if_safe from data label ('March 2026') per criteria G/K1. |
| `subject_exact` _(A · 📝 texto libre)_ | etsy.com visitor gender and age demographic breakdown per third-party analytics report | etsy.com audience demographics per SimilarWeb: 41.74% male, 58.26% female, largest group 25-34 |
| `time_scope_raw` _(B · 📝 texto libre)_ | data labeled March 2026 | _(null)_ |
| `uncertainties` _(A · 🔒 enum)_ | none | methodology_unclear |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016)

**Veredicto:**


---

## Caso 33 — `ER-SP-compass_artifact_wf-a9f3dcd5-c78e-4ae8-b4d1-09fed2f8d84d_text_markdown-002-SNP-001`

- **Batch de origen:** batch_029
- **Estrato:** E2

**snippet_primary:**

> "I bought a yearly subscription (finishing January 31st 2026) for $227.05 to a content provider called Chasing Bourbon. Patreon decided to take this content provider off their platform for their own decision/policy and now they refuse to reimburse me for the unused portion or $75.63. I happened to know the content provider and they are not paying him either so Patreon is just keeping my money. I want my money back since they are not providing the service that they terminated at their own decision"

| Campo | Sonnet | Fable |
|---|---|---|
| `claim_type` _(A · 🔒 enum)_ | review_statement | anecdotal_report |
| `local_qualifiers` _(A · 📝 texto libre)_ | for their own decision/policy · not paying him either so Patreon is just keeping my money | I bought a yearly subscription (finishing January 31st 2026) for $227.05 · Patreon decided to take this content provider off their platform for their own decision/policy · now they refuse to reimburse me for the unused portion or $75.63 · they are not paying him either |
| `metric_type` _(A · 🔒 enum)_ | refund_policy | unknown |
| `metric_unit` _(B · 📝 texto libre)_ | USD | _(null)_ |
| `metric_value_raw` _(B · 📝 texto libre)_ | $227.05; $75.63 | _(null)_ |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | Amounts $227.05 (yearly subscription) and $75.63 (unused portion) present; main claim is the refund refusal event, not a metric — amounts kept in local_qualifiers (criterion H). |
| `subject_exact` _(A · 📝 texto libre)_ | buyer's BBB complaint about Patreon withholding a refund after removing a creator from the platform | buyer refused reimbursement of the unused portion of a yearly subscription after Patreon removed the creator from the platform |
| `time_scope_normalized_if_safe` _(B · 📝 texto libre)_ | 2026-01-31 | _(null)_ |
| `time_scope_raw` _(B · 📝 texto libre)_ | finishing January 31st 2026 | _(null)_ |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016)

**Veredicto:**


---

## Caso 34 — `ER-SP-compass_artifact_wf-a9f3dcd5-c78e-4ae8-b4d1-09fed2f8d84d_text_markdown-005-SNP-001`

- **Batch de origen:** batch_029
- **Estrato:** E2

**snippet_primary:**

> "Terrible experience, they do not care about people using their platforms at all. I used to be subscribed to a creator charging a staggering amount of 39$ a month and patreon just wiped their account and refused to refund me my money. The creator also kept deleting, hiding, reposting same exact posts over and over again. It's truly hilarious how people just blindly trust patreon"

| Campo | Sonnet | Fable |
|---|---|---|
| `claim_type` _(A · 🔒 enum)_ | review_statement | anecdotal_report |
| `local_qualifiers` _(B · 📝 texto libre)_ | _(lista vacia)_ | a creator charging a staggering amount of 39$ a month · patreon just wiped their account and refused to refund me my money · The creator also kept deleting, hiding, reposting same exact posts over and over again |
| `metric_unit` _(B · 📝 texto libre)_ | USD per month | _(null)_ |
| `metric_value_raw` _(B · 📝 texto libre)_ | $39 | _(null)_ |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | Subscription price '39$ a month' present; main claim is the account wipe and refund refusal — amount kept in local_qualifiers (criterion H). |
| `subject_exact` _(A · 📝 texto libre)_ | buyer's complaint about Patreon wiping a creator's account and refusing a refund | buyer subscribed to a creator whose account Patreon wiped, with a refund refused |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016)

**Veredicto:**


---

## Caso 35 — `ER-SP-compass_artifact_wf-a9f3dcd5-c78e-4ae8-b4d1-09fed2f8d84d_text_markdown-005-SNP-004`

- **Batch de origen:** batch_029
- **Estrato:** E2

**snippet_primary:**

> "website does not use the standard conversion rates the rest of the world does, if im advertised a patreon subscription for $3 i want to pay $3 not £3 currently £3 is more then $3 this is a scam"

| Campo | Sonnet | Fable |
|---|---|---|
| `claim_type` _(A · 🔒 enum)_ | review_statement | anecdotal_report |
| `local_qualifiers` _(A · 📝 texto libre)_ | does not use the standard conversion rates the rest of the world does | if im advertised a patreon subscription for $3 i want to pay $3 not £3 · currently £3 is more then $3 |
| `metric_unit` _(B · 📝 texto libre)_ | USD and GBP (mixed, declared) | _(null)_ |
| `metric_value_raw` _(B · 📝 texto libre)_ | $3; £3 | _(null)_ |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | Main claim is the currency-conversion billing practice, not a price level — amounts $3/£3 kept in local_qualifiers (criterion H). Mixed currencies USD and GBP declared here. · time_scope_raw 'currently' is relative — normalized left null (criterion G). |
| `subject_exact` _(A · 📝 texto libre)_ | buyer's complaint about Patreon's currency conversion rate diverging from standard USD/GBP rates | buyer charged in GBP at parity for a Patreon subscription advertised in USD, described as not using standard conversion rates |
| `time_scope_raw` _(B · 📝 texto libre)_ | _(null)_ | currently |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016)

**Veredicto:**


---

## Caso 36 — `ER-SP-compass_artifact_wf-b66489b8-52e0-4cd3-9bfd-9810fa4ba897_text_markdown_normalized-008-SNP-001`

- **Batch de origen:** batch_029
- **Estrato:** E2

**snippet_primary:**

> "You can upload multiple files, including ebooks, PDFs, audio, video, or other file types. Each file can be up to 5GB in size." … "We support most file types, including PDFs, audio, video, ZIP files, and more. However, certain file types such as EXE, ISO, DMG, VBS, SCR, and JAR are not supported."

| Campo | Sonnet | Fable |
|---|---|---|
| `claim_type` _(A · 🔒 enum)_ | policy_statement | availability_statement |
| `local_qualifiers` _(A · 📝 texto libre)_ | EXE, ISO, DMG, VBS, SCR, and JAR are not supported | certain file types such as EXE, ISO, DMG, VBS, SCR, and JAR are not supported |
| `metric_type` _(A · 🔒 enum)_ | unknown | file_size_limit |
| `metric_unit` _(A · 📝 texto libre)_ | GB | GB per file |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | metric_type fuera de enum: per-file upload size limit ('Each file can be up to 5GB in size') — no enum value covers file/upload limits; minimal descriptor 'file_size_limit' (K5). · Source date 'Accessed April 2026; page undated' — access dates never normalize time_scope (K1). |
| `subject_exact` _(A · 📝 texto libre)_ | Payhip digital product file size and supported/unsupported file type policy | Payhip digital product uploads accept multiple files up to 5GB each across most file types, excluding EXE, ISO, DMG, VBS, SCR, and JAR |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016)

**Veredicto:**


---

## Caso 37 — `ER-SP-compass_artifact_wf-b66489b8-52e0-4cd3-9bfd-9810fa4ba897_text_markdown_normalized-033-SNP-001`

- **Batch de origen:** batch_031
- **Estrato:** E2

**snippet_primary:**

> "Free beautifully designed store themes that are fully customizable. Every theme is just a starting point. No coding or HTML required."

| Campo | Sonnet | Fable |
|---|---|---|
| `evidence_role` _(A · 🔒 enum)_ | official_policy | direct_claim |
| `local_qualifiers` _(A · 📝 texto libre)_ | no coding or HTML required | Every theme is just a starting point · No coding or HTML required |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | Platform named only in source_ref, not in snippet text — platforms left empty (criterion F). Marketing feature page assigned direct_claim (K6). Source date 'Accessed April 2026; page undated' — never normalizes (K1). |
| `platforms` _(B · 📝 texto libre)_ | Payhip | _(lista vacia)_ |
| `subject_exact` _(A · 📝 texto libre)_ | Payhip's own description of free customizable store themes requiring no coding | free fully customizable store themes offered on the Payhip themes page with no coding required |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016)

**Veredicto:**


---

## Caso 38 — `ER-SP-compass_artifact_wf-b66489b8-52e0-4cd3-9bfd-9810fa4ba897_text_markdown_normalized-040-SNP-001`

- **Batch de origen:** batch_031
- **Estrato:** E2

**snippet_primary:**

> "Check out our payhip template selection for the very best in unique or custom, handmade pieces from our templates shops."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(A · 📝 texto libre)_ | unique or custom, handmade pieces from our templates shops | the very best in unique or custom, handmade pieces from our templates shops |
| `metric_type` _(A · 🔒 enum)_ | search_discovery | unknown |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | product_type fuera de enum: market category is explicitly 'payhip template' — no enum value covers generic templates; observed label recorded (K5). · 'payhip' appears as part of the product-category compound 'payhip template selection', not as a service-as-such mention — excluded from platforms (K3). Etsy named only in source_ref — platforms left empty (criterion F). |
| `platforms` _(B · 📝 texto libre)_ | Etsy · Payhip | _(lista vacia)_ |
| `product_type_if_explicit` _(A · 🔒 enum)_ | unknown | payhip template |
| `subject_exact` _(A · 📝 texto libre)_ | Etsy marketplace search-results page for third-party-made Payhip templates | Etsy market page offering a selection of payhip templates from template shops |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016)

**Veredicto:**


---

## Caso 39 — `ER-SP-compass_artifact_wf-b8196d6f-3c52-444d-99ca-a873af688da7_text_markdown-001-SNP-001`

- **Batch de origen:** batch_031
- **Estrato:** E2

**snippet_primary:**

> "Anime Tracker | Notion Template · TZS15,000 · Apple Slides | Figma Slides Template · TZS0+ · Bookworm Library | Notion Template · TZS25,000 · Min-folio | Notion Template · My Skin | Notion Template"

| Campo | Sonnet | Fable |
|---|---|---|
| `actor_level` _(A · 🔒 enum)_ | seller | third_party |
| `claim_type` _(A · 🔒 enum)_ | availability_statement | pricing_statement |
| `local_qualifiers` _(B · 📝 texto libre)_ | _(lista vacia)_ | Apple Slides \| Figma Slides Template · TZS0+ |
| `metric_value_raw` _(A · 📝 texto libre)_ | TZS15,000; TZS0+; TZS25,000 | TZS15,000 \| TZS0+ \| TZS25,000 |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | Four of five products explicitly labeled 'Notion Template' (dominant); one 'Figma Slides Template' — dominant value assigned per the array rule. · Two products (Min-folio, My Skin) show no price in the capture. 'Notion' and 'Figma' appear inside product-type labels, not as service mentions — excluded from platforms (K3). Platform named only in source_ref/title — platforms left empty (criterion F). |
| `platforms` _(B · 📝 texto libre)_ | Lemon Squeezy | _(lista vacia)_ |
| `subject_exact` _(A · 📝 texto libre)_ | seller's Lemon Squeezy storefront (amdesigns) product listings and prices in Tanzanian shillings | five template products on the amdesigns Lemon Squeezy store, three with TZS prices shown |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016)

**Veredicto:**


---

## Caso 40 — `ER-SP-compass_artifact_wf-bae0f41e-e3a0-414a-900e-24a67d70982c_text_markdown-001-SNP-002`

- **Batch de origen:** batch_031
- **Estrato:** E2

**snippet_primary:**

> "Around the world in 2026, over 95752 companies have started using Gumroad as Social Commerce tool."

| Campo | Sonnet | Fable |
|---|---|---|
| `geography_if_explicit` _(A · 📝 texto libre)_ | around the world | Around the world |
| `metric_type` _(A · 🔒 enum)_ | unknown | customer_count |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | metric_type fuera de enum: count of companies using the platform — descriptor 'customer_count' (K5). · Explicit year 'in 2026' in snippet — normalized to year granularity '2026' (criterion G). geography verbatim 'Around the world'. Estimate without stated methodology — methodology_unclear. |
| `subject_exact` _(A · 📝 texto libre)_ | third-party market-intelligence database's count of companies using Gumroad as a social-commerce tool | count of companies worldwide that have started using Gumroad as a social-commerce tool in 2026 per 6sense |
| `uncertainties` _(A · 🔒 enum)_ | none | methodology_unclear |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016)

**Veredicto:**


---

## Caso 41 — `ER-SP-compass_artifact_wf-bae0f41e-e3a0-414a-900e-24a67d70982c_text_markdown-003-SNP-003`

- **Batch de origen:** batch_032
- **Estrato:** E2

**snippet_primary:**

> [Stated in layout: "Name | Category | Average rating | Reviews | Mixed reviews | Price | Sales | Est. Revenue: Old Book Cover & Spread Mockup Design Syndrome | design / graphics | 5.0 ⭐ | 118 | 2% | $13.00 | 20,221 | $262,873.00"]

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(B · 📝 texto libre)_ | _(lista vacia)_ | Est. Revenue |
| `metric_type` _(A · 🔒 enum)_ | review_count · sales_count · revenue · price | revenue |
| `metric_unit` _(A · 📝 texto libre)_ | stars, count, percent, and USD (mixed, declared) | USD (Est. Revenue) |
| `metric_value_raw` _(A · 📝 texto libre)_ | 5.0 stars; 118 reviews; 2% mixed reviews; $13.00; 20,221 sales; $262,873.00 est. revenue | $262,873.00 |
| `parser_notes` _(A · 📝 texto libre)_ | Single product row combines four distinct metric dimensions with no dominant one; recorded as array. | Additional metrics (criterion H): Sales 20,221; Price $13.00; Reviews 118; Average rating 5.0; Mixed reviews 2%. · Source's explicit category label 'design / graphics' for a mockup design product — product_type 'design_asset'. Estimated figure without stated methodology — methodology_unclear. · Snippet delivered as a layout capture ('[Stated in layout: ...]' is a capture annotation). Platform named only in source_ref — platforms left empty (criterion F). |
| `platforms` _(B · 📝 texto libre)_ | Gumroad | _(lista vacia)_ |
| `subject_exact` _(A · 📝 texto libre)_ | third-party dataset provider's per-product listing example showing rating, reviews, price, sales, and estimated revenue for a single Gumroad product | Gumtrends table row for the product 'Old Book Cover & Spread Mockup Design Syndrome' with rating, reviews, price, sales, and estimated revenue |
| `uncertainties` _(A · 🔒 enum)_ | none | methodology_unclear |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016)

**Veredicto:**


---

## Caso 42 — `ER-SP-compass_artifact_wf-bae0f41e-e3a0-414a-900e-24a67d70982c_text_markdown-004-SNP-001`

- **Batch de origen:** batch_032
- **Estrato:** E2

**snippet_primary:**

> [Stated in layout: "Price Range | # Products | % of Revenue | Avg Sales | Total Revenue: $0.01–$4.99 | 2,084 | 0.8% | 313 | $1.7M; $5–$9.99 | 2,896 | 3% | 328 | $6.2M; $10–$19.99 | 3,365 | 5.5% | 241 | $11.4M; $20–$29.99 | 1,760 | 4.7% | 235 | $9.7M; $30–$49.99 | 1,409 | 7.3% | 268 | $15M; $50–$99.99 | 857 | 7% | 239 | $14.5M; $100–$199.99 | 265 | 6% | 318 | $12.4M; $200+ | 316 | 65.7% | 154 | $135.3M"]

| Campo | Sonnet | Fable |
|---|---|---|
| `metric_type` _(A · 🔒 enum)_ | price · revenue · sales_count | revenue share by price range |
| `metric_unit` _(A · 📝 texto libre)_ | count, percent, and USD (mixed, declared) | mixed: product count, % of revenue, average sales, USD total revenue per price range |
| `metric_value_raw` _(A · 📝 texto libre)_ | $0.01–$4.99: 2,084 products, 0.8% revenue, 313 avg sales, $1.7M total; $200+: 316 products, 65.7% revenue, 154 avg sales, $135.3M total (full 8-tier table in snippet) | $0.01–$4.99 \| 2,084 \| 0.8% \| 313 \| $1.7M; $5–$9.99 \| 2,896 \| 3% \| 328 \| $6.2M; $10–$19.99 \| 3,365 \| 5.5% \| 241 \| $11.4M; $20–$29.99 \| 1,760 \| 4.7% \| 235 \| $9.7M; $30–$49.99 \| 1,409 \| 7.3% \| 268 \| $15M; $50–$99.99 \| 857 \| 7% \| 239 \| $14.5M; $100–$199.99 \| 265 \| 6% \| 318 \| $12.4M; $200+ \| 316 \| 65.7% \| 154 \| $135.3M |
| `parser_notes` _(A · 📝 texto libre)_ | Full price-band table (8 rows) condensed to endpoints in metric_value_raw for brevity; complete data preserved verbatim in snippet_primary. | metric_type fuera de enum: table of revenue distribution across price ranges — descriptor 'revenue share by price range' (K5); full table preserved verbatim, mixed units declared. · Snippet delivered as a layout capture. No data source or methodology stated — methodology_unclear. Platform named only in source title/ref — platforms left empty (criterion F). |
| `platforms` _(B · 📝 texto libre)_ | Gumroad | _(lista vacia)_ |
| `subject_exact` _(A · 📝 texto libre)_ | third-party report's breakdown of Gumroad product counts, revenue share, average sales, and total revenue by price band | distribution of Gumroad products, revenue share, average sales, and total revenue across eight price ranges |
| `time_scope_normalized_if_safe` _(B · 📝 texto libre)_ | 2026-03-21 | _(null)_ |
| `time_scope_raw` _(B · 📝 texto libre)_ | Updated March 21, 2026 | _(null)_ |
| `uncertainties` _(A · 🔒 enum)_ | none | methodology_unclear |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016)

**Veredicto:**


---

## Caso 43 — `ER-SP-compass_artifact_wf-bbbe6c81-ce19-4446-ada5-416354340fc4_text_markdown-001-SNP-003`

- **Batch de origen:** batch_032
- **Estrato:** E2

**snippet_primary:**

> "el 78 por ciento se realiza a través de dispositivos móviles, el 20 por ciento en computadoras y el 2 por ciento restante en tabletas"

| Campo | Sonnet | Fable |
|---|---|---|
| `evidence_role` _(A · 🔒 enum)_ | database_fact | reported_event |
| `metric_type` _(A · 🔒 enum)_ | unknown | purchase device share |
| `metric_unit` _(A · 📝 texto libre)_ | percent | % de compras por dispositivo |
| `metric_value_raw` _(A · 📝 texto libre)_ | 78% dispositivos móviles; 20% computadoras; 2% tabletas | el 78 por ciento se realiza a través de dispositivos móviles, el 20 por ciento en computadoras y el 2 por ciento restante en tabletas |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | metric_type fuera de enum: distribution of purchases by device — descriptor 'purchase device share' (K5); values preserved verbatim. · Platform named only in source title/ref, not in this snippet — platforms left empty (criterion F). Figures reported without attribution or methodology — methodology_unclear. |
| `platforms` _(B · 📝 texto libre)_ | Hotmart | _(lista vacia)_ |
| `subject_exact` _(A · 📝 texto libre)_ | news article's reported device-type split for digital-product purchases | share of purchases made via mobile devices, computers, and tablets |
| `uncertainties` _(A · 🔒 enum)_ | none | methodology_unclear |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016)

**Veredicto:**


---

## Caso 44 — `ER-SP-compass_artifact_wf-bbbe6c81-ce19-4446-ada5-416354340fc4_text_markdown-004-SNP-001`

- **Batch de origen:** batch_032
- **Estrato:** E2

**snippet_primary:**

> "No pude bajar un e book que compre en la plataforma y no me respondieron aún. Compre en otras ocasiones y fue todo bien pero en esta compra al contrario."

| Campo | Sonnet | Fable |
|---|---|---|
| `claim_type` _(A · 🔒 enum)_ | review_statement | anecdotal_report |
| `local_qualifiers` _(A · 📝 texto libre)_ | compre en otras ocasiones y fue todo bien pero en esta compra al contrario | Compre en otras ocasiones y fue todo bien pero en esta compra al contrario |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | 'e book' named explicitly — product_type 'ebook'. Platform named only in source_ref, not in snippet text ('la plataforma') — platforms left empty (criterion F). |
| `platforms` _(B · 📝 texto libre)_ | Hotmart | _(lista vacia)_ |
| `subject_exact` _(A · 📝 texto libre)_ | buyer's complaint about being unable to download a purchased ebook on Hotmart with no support response | buyer unable to download a purchased ebook from the platform with no response yet, after previous purchases went well |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016)

**Veredicto:**


---

## Caso 45 — `ER-SP-compass_artifact_wf-bbbe6c81-ce19-4446-ada5-416354340fc4_text_markdown-013-SNP-001`

- **Batch de origen:** batch_033
- **Estrato:** E2

**snippet_primary:**

> "Estou há alguns meses sem conseguir comprar nenhum curso da hotmart, consigo acessar os que estão ativos, mas não consigo comprar novos. Ele diz que há uma falha no pagamento, mas não há, pois tento trocar para outras opções de pagamento e continua dando o mesmo erro. Nesse meio tempo já tentei comprar cursos de vários valores e todos dão esse mesmo erro. Mesmo tendo limite/dinheiro, não consigo efetuar a compra no pix, no boleto, no cartão e nenhuma outra forma. Quando tento pedir ajuda no site, sou respondida por inteligência artificial."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(A · 📝 texto libre)_ | already able to access previously purchased/active courses | Ele diz que há uma falha no pagamento, mas não há · Mesmo tendo limite/dinheiro, não consigo efetuar a compra no pix, no boleto, no cartão e nenhuma outra forma · sou respondida por inteligência artificial |
| `parser_notes` _(A · 📝 texto libre)_ | Buyer reports an AI support agent responded instead of a human; root cause of payment failure not established. | product_type fuera de enum: 'cursos' named explicitly — observed value 'curso' recorded (K5). 'pix', 'boleto', 'cartão' are payment methods, not platforms — excluded (K3). · time_scope_raw 'há alguns meses' is relative — normalized left null (criterion G). |
| `product_type_if_explicit` _(A · 🔒 enum)_ | unknown | curso |
| `subject_exact` _(A · 📝 texto libre)_ | buyer-reported inability to complete any Hotmart purchase across all payment methods over several months | buyer unable to purchase any new Hotmart courses for months due to a persistent payment error across pix, boleto, card and other methods, with AI-only support |
| `time_scope_raw` _(B · 📝 texto libre)_ | _(null)_ | há alguns meses |
| `uncertainties` _(A · 🔒 enum)_ | subject_ambiguity | anecdotal_single_source |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032)

**Veredicto:**


---

## Caso 46 — `ER-SP-compass_artifact_wf-bc6f268c-aeb6-4040-a1a6-8670888bb92f_text_markdown-014-SNP-001`

- **Batch de origen:** batch_034
- **Estrato:** E2

**snippet_primary:**

> "Choose from over 64,100 website templates and themes. Explore items created by our global community of independent designers and developers, confident they're hand-reviewed by us."

| Campo | Sonnet | Fable |
|---|---|---|
| `claim_type` _(A · 🔒 enum)_ | availability_statement | statistical_data |
| `evidence_role` _(A · 🔒 enum)_ | observed_platform_state | direct_claim |
| `local_qualifiers` _(B · 📝 texto libre)_ | _(lista vacia)_ | created by our global community of independent designers and developers · confident they're hand-reviewed by us |
| `metric_type` _(A · 🔒 enum)_ | unknown | catalog size |
| `metric_unit` _(A · 📝 texto libre)_ | items | website templates and themes |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | metric_type fuera de enum: marketplace catalog count — descriptor 'catalog size' reused (K5). Platform named only in source_ref — platforms left empty (criterion F). |
| `platforms` _(B · 📝 texto libre)_ | ThemeForest | _(lista vacia)_ |
| `subject_exact` _(A · 📝 texto libre)_ | ThemeForest marketplace catalogue scale claim for website templates and themes | count of website templates and themes available on the ThemeForest all-category page, described as hand-reviewed items from a global community |
| `time_scope_raw` _(B · 📝 texto libre)_ | Accessed April 2026; page undated | _(null)_ |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032)

**Veredicto:**


---

## Caso 47 — `ER-SP-compass_artifact_wf-de144e73-98a7-403c-a882-9327b9dbadd2_text_markdown-004-SNP-001`

- **Batch de origen:** batch_038
- **Estrato:** E2

**snippet_primary:**

> "1. tshirt 2. shirt 3. stickers 4. pokemon 5. wall art 6. gift 7. jewelry 8. phone case 9. resident evil 10. keychain 11. home decor 12. womens clothing 13. necklace 14. ayn thor 15. png 16. easter 17. personalized gift 18. ita bag 19. press on nails 20. t shirt"

| Campo | Sonnet | Fable |
|---|---|---|
| `metric_type` _(A · 🔒 enum)_ | etsy_keyword_search_ranking | keyword ranking |
| `metric_unit` _(B · 📝 texto libre)_ | _(null)_ | rank position |
| `metric_value_raw` _(B · 📝 texto libre)_ | _(null)_ | 1. tshirt 2. shirt 3. stickers 4. pokemon 5. wall art 6. gift 7. jewelry 8. phone case 9. resident evil 10. keychain 11. home decor 12. womens clothing 13. necklace 14. ayn thor 15. png 16. easter 17. personalized gift 18. ita bag 19. press on nails 20. t shirt |
| `parser_notes` _(A · 📝 texto libre)_ | metric_type 'etsy_keyword_search_ranking' has no enum match for a ranked keyword list; recorded as out_of_enum literal. | metric_type fuera de enum: ranked keyword list — descriptor 'keyword ranking' (K5); full list preserved verbatim (K10). · List items are search keywords, not platform mentions (K3). Tracker ranking without stated methodology — methodology_unclear (K12). Platform named only in source title/ref — platforms left empty (criterion F). |
| `platforms` _(B · 📝 texto libre)_ | Etsy | _(lista vacia)_ |
| `subject_exact` _(A · 📝 texto libre)_ | third-party keyword-research blog's ranked list of top Etsy search keywords | top 20 Etsy search keywords ranked by eRank, from 'tshirt' at #1 to 't shirt' at #20 |
| `time_scope_normalized_if_safe` _(B · 📝 texto libre)_ | 2026-04-06 | _(null)_ |
| `time_scope_raw` _(B · 📝 texto libre)_ | 6 April 2026 | _(null)_ |
| `uncertainties` _(A · 🔒 enum)_ | none | methodology_unclear |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032)

**Veredicto:**


---

## Caso 48 — `ER-SP-compass_artifact_wf-de144e73-98a7-403c-a882-9327b9dbadd2_text_markdown-006-SNP-001`

- **Batch de origen:** batch_038
- **Estrato:** E2

**snippet_primary:**

> "Koalanda tracks all Etsy listings: currently more than 125 million. Out of all listings, there are about 8 million that have sales in the last 30 days."

| Campo | Sonnet | Fable |
|---|---|---|
| `actor_level` _(A · 🔒 enum)_ | third_party | source |
| `local_qualifiers` _(B · 📝 texto libre)_ | _(lista vacia)_ | Out of all listings, there are about 8 million that have sales in the last 30 days |
| `metric_type` _(A · 🔒 enum)_ | third_party_tracked_listing_count | catalog size |
| `metric_unit` _(A · 📝 texto libre)_ | listings | Etsy listings |
| `metric_value_raw` _(A · 📝 texto libre)_ | more than 125 million listings tracked; about 8 million with sales in the last 30 days | currently more than 125 million |
| `parser_notes` _(A · 📝 texto libre)_ | metric_type 'third_party_tracked_listing_count' out_of_enum; same pattern as prior third-party listing-scale claims. | metric_type fuera de enum: platform catalog count — descriptor 'catalog size' reused (K5). Additional metric kept as qualifier (criterion H). · time_scope_raw 'currently' is relative — normalized left null (criterion G). Tracker estimate — methodology_unclear (K12). |
| `subject_exact` _(A · 📝 texto libre)_ | third-party Etsy analytics tool vendor's reported scale of tracked Etsy listings and recently-selling listings | Koalanda tracking more than 125 million Etsy listings, of which about 8 million have sales in the last 30 days |
| `time_scope_raw` _(A · 📝 texto libre)_ | last 30 days (as of access, April 2026) | currently |
| `uncertainties` _(A · 🔒 enum)_ | none | methodology_unclear |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032)

**Veredicto:**


---

## Caso 49 — `ER-SP-compass_artifact_wf-e33b0dbb-828e-4221-b8c5-7bf05bddcdba_text_markdown_normalized-008-SNP-001`

- **Batch de origen:** batch_039
- **Estrato:** E2

**snippet_primary:**

> > "EU and UK VAT - These are digital UK & EU VAT collected for that period"
> 
> > "Stripe/PayPal Fees - These are payment processor fees charged by PayPal and Stripe"
> 
> > "Payhip Fees - These are platform fees charged by Payhip depending on your plan"
> 
> > "Custom Taxes - These are taxes that were manually set up, collected, and sent to you"
> 
> > "Products Sold - This lists the products and the number of items sold for that period"
> 
> > "Affiliates Commission - This shows the amount earned by your affiliates"
> 
> > "Affiliate Sales - This shows the number of sales generated by your affiliates"

| Campo | Sonnet | Fable |
|---|---|---|
| `claim_type` _(A · 🔒 enum)_ | explicit_claim | availability_statement |
| `local_qualifiers` _(B · 📝 texto libre)_ | _(lista vacia)_ | Payhip Fees - These are platform fees charged by Payhip depending on your plan |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | Availability state claim with explicit last-updated September 27, 2022 and null raw — normalized (K1). Payment processors excluded from platforms (K3). |
| `subject_exact` _(A · 📝 texto libre)_ | Payhip monthly sales-report field definitions (VAT, processor fees, platform fees, custom taxes, products sold, affiliate commission/sales) | sales report components: EU and UK VAT, Stripe/PayPal fees, Payhip plan fees, custom taxes, products sold, affiliates commission, and affiliate sales |
| `time_scope_raw` _(B · 📝 texto libre)_ | Last updated September 27, 2022 | _(null)_ |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032)

**Veredicto:**


---

## Caso 50 — `ER-SP-compass_artifact_wf-e33b0dbb-828e-4221-b8c5-7bf05bddcdba_text_markdown_normalized-009-SNP-001`

- **Batch de origen:** batch_039
- **Estrato:** E2

**snippet_primary:**

> > "you can earn a 50% recurring commission on Payhip's transaction fees and any monthly paid plans from the sellers you refer. That means if someone signs up through your link and has upgraded to a paid plan, you get a cut every month as long as the seller is active. You will also earn 50% of the amount we collect from their sales for transaction fees."
> 
> > "You get paid out on a monthly basis on the 13th of every month via Paypal. There is a minimum commission amount of $50 for payouts, and if you do not meet this threshold, your commission will be combined with the following months until you reach the minimum balance of $50."

| Campo | Sonnet | Fable |
|---|---|---|
| `claim_type` _(A · 🔒 enum)_ | pricing_statement | policy_statement |
| `local_qualifiers` _(B · 📝 texto libre)_ | _(lista vacia)_ | you get a cut every month as long as the seller is active · You get paid out on a monthly basis on the 13th of every month via Paypal · There is a minimum commission amount of $50 for payouts, and if you do not meet this threshold, your commission will be combined with the following months |
| `metric_type` _(A · 🔒 enum)_ | payout | affiliate commission rate |
| `metric_unit` _(A · 📝 texto libre)_ | percent; USD | % of transaction fees and paid-plan revenue |
| `metric_value_raw` _(A · 📝 texto libre)_ | 50% recurring commission on Payhip transaction fees and paid-plan revenue from referred sellers; $50 minimum monthly payout via PayPal on the 13th | a 50% recurring commission on Payhip's transaction fees and any monthly paid plans from the sellers you refer |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | metric_type fuera de enum: partner commission — descriptor 'affiliate commission rate' reused (K5). Additional metrics kept as qualifiers (criterion H): monthly payout on the 13th, $50 minimum payout threshold. 'Paypal' is a payment processor — excluded (K3). Page undated — not normalized (K1). |
| `subject_exact` _(A · 📝 texto libre)_ | Payhip affiliate-partner recurring commission rate and monthly payout threshold | partner program paying 50% recurring commission on Payhip transaction fees and referred sellers' paid plans, paid monthly on the 13th via PayPal with a $50 minimum that rolls over |
| `time_scope_raw` _(B · 📝 texto libre)_ | Undated | _(null)_ |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032)

**Veredicto:**


---

## Caso 51 — `ER-SP-compass_artifact_wf-e33b0dbb-828e-4221-b8c5-7bf05bddcdba_text_markdown_normalized-011-SNP-001`

- **Batch de origen:** batch_039
- **Estrato:** E2

**snippet_primary:**

> > "On occasion, a customer may file a chargeback for their purchase. This means that they are claiming that you did not provide them with the promised product or service and want their money back."
> 
> > "If customers have agreed to your refund policy and terms of service before they make their purchase and they then put through a chargeback, you should be protected. You can let the company who is handling the chargeback know that the customer was made aware of your terms."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(B · 📝 texto libre)_ | _(lista vacia)_ | you should be protected · You can let the company who is handling the chargeback know that the customer was made aware of your terms |
| `metric_type` _(A · 🔒 enum)_ | refund_policy | unknown |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | Policy state claim with explicit last-updated April 10, 2024 and null raw — normalized (K1). Platform named only in source_ref — platforms left empty (criterion F). |
| `platforms` _(B · 📝 texto libre)_ | Payhip | _(lista vacia)_ |
| `subject_exact` _(A · 📝 texto libre)_ | Payhip seller guidance on chargeback protection via pre-purchase agreement to refund policy and terms | chargeback protection for sellers when customers agreed to the refund policy and terms of service before purchase |
| `time_scope_raw` _(B · 📝 texto libre)_ | Last updated April 10, 2024 | _(null)_ |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032)

**Veredicto:**


---

## Caso 52 — `ER-SP-compass_artifact_wf-e68dd732-3da5-44dc-ac62-efdb81f1bdc1_text_markdown-003-SNP-002`

- **Batch de origen:** batch_042
- **Estrato:** E3

**snippet_primary:**

> "In consideration of Gumroad's MOR Services, in respect of each resale of your Products through the Services, you agree to pay Gumroad a per-transaction fee (the, "Gumroad Fee") for each resale made by Gumroad through the Services. The Gumroad Fee owed for each resale through the Services is automatically deducted from the purchase price paid by the Buyer, with the remainder (less any amounts in respect of taxes and any other charges payable by you pursuant to this Agreement) owed and paid to you by Gumroad (such remainder amount, the "Supplier Fee")."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(A · 📝 texto libre)_ | less any amounts in respect of taxes and any other charges payable by you | (less any amounts in respect of taxes and any other charges payable by you pursuant to this Agreement) |
| `metric_type` _(A · 🔒 enum)_ | fee_rate | unknown |
| `parser_notes` _(A · 📝 texto libre)_ | Gumroad Fee (deducted from buyer price) is distinct from remainder Supplier Fee paid to seller; net vs gross not fully disambiguated in this snippet | No fee rate stated in this clause — metric_type left 'unknown'. Policy state claim with explicit Effective Date January 1, 2025 and null raw — normalized (K1). |
| `subject_exact` _(A · 📝 texto libre)_ | Gumroad Fee vs Supplier Fee split mechanics under merchant-of-record terms | per-transaction Gumroad Fee for merchant-of-record resales, automatically deducted from the buyer's purchase price, with the remainder paid to the supplier as the Supplier Fee |
| `time_scope_raw` _(B · 📝 texto libre)_ | Effective Date: January 1, 2025; Last Updated Date: December 10, 2024 | _(null)_ |
| `uncertainties` _(B · 🔒 enum)_ | net_vs_gross_ambiguity | _(lista vacia)_ |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016), S6 (desde batch_040), S7 (desde batch_040), S8 (desde batch_040)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032), K13 (desde batch_040), K14 (desde batch_040)

**Veredicto:**


---

## Caso 53 — `ER-SP-compass_artifact_wf-e68dd732-3da5-44dc-ac62-efdb81f1bdc1_text_markdown-003-SNP-006`

- **Batch de origen:** batch_042
- **Estrato:** E3

**snippet_primary:**

> "Supplier Fees owed to you by Gumroad will be paid to you after a completed resale transaction based on an agreed upon settlement schedule, which is subject to change at the discretion of Gumroad."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(A · 📝 texto libre)_ | subject to change at the discretion of Gumroad | based on an agreed upon settlement schedule, which is subject to change at the discretion of Gumroad |
| `metric_type` _(A · 🔒 enum)_ | payout | unknown |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | No concrete schedule stated — metric_type left 'unknown'. Policy state claim with explicit Effective Date January 1, 2025 and null raw — normalized (K1). |
| `subject_exact` _(A · 📝 texto libre)_ | Gumroad Supplier Fee payout timing tied to a Gumroad-set settlement schedule | supplier fees paid after completed resale transactions on an agreed settlement schedule, changeable at Gumroad's discretion |
| `time_scope_raw` _(B · 📝 texto libre)_ | Effective Date: January 1, 2025; Last Updated Date: December 10, 2024 | _(null)_ |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016), S6 (desde batch_040), S7 (desde batch_040), S8 (desde batch_040)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032), K13 (desde batch_040), K14 (desde batch_040)

**Veredicto:**


---

## Caso 54 — `ER-SP-compass_artifact_wf-e68dd732-3da5-44dc-ac62-efdb81f1bdc1_text_markdown-005-SNP-001`

- **Batch de origen:** batch_042
- **Estrato:** E3

**snippet_primary:**

> "To receive a payout, you must have a minimum balance of US $10. Certain countries have higher minimum payout balances - Thailand (600 THB) and Korea (40,000 KRW)."

| Campo | Sonnet | Fable |
|---|---|---|
| `geography_if_explicit` _(B · 📝 texto libre)_ | Thailand · Korea | _(null)_ |
| `local_qualifiers` _(B · 📝 texto libre)_ | _(lista vacia)_ | Certain countries have higher minimum payout balances |
| `metric_type` _(A · 🔒 enum)_ | payout | minimum payout |
| `metric_unit` _(A · 📝 texto libre)_ | mixed (USD/THB/KRW) | mixed: USD, THB, KRW |
| `metric_value_raw` _(A · 📝 texto libre)_ | US $10 (Thailand 600 THB; Korea 40,000 KRW) | US $10; Thailand (600 THB); Korea (40,000 KRW) |
| `parser_notes` _(A · 📝 texto libre)_ | Mixed currency units declared: base threshold in USD, Thailand in THB, Korea in KRW | metric_type fuera de enum: payout threshold — descriptor 'minimum payout' reused (K5); mixed currencies declared. Country exceptions kept in the value; the general claim has no single geography — geography left null. · Policy state claim with explicit last-updated July 23, 2024 and null raw — normalized (K1). Platform named only in source_ref — platforms left empty (criterion F). |
| `platforms` _(B · 📝 texto libre)_ | Gumroad | _(lista vacia)_ |
| `subject_exact` _(A · 📝 texto libre)_ | Gumroad minimum payout balance threshold, with country-specific exceptions | minimum payout balance of US $10, with higher minimums for Thailand (600 THB) and Korea (40,000 KRW) |
| `time_scope_raw` _(B · 📝 texto libre)_ | Page last updated July 23, 2024 | _(null)_ |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016), S6 (desde batch_040), S7 (desde batch_040), S8 (desde batch_040)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032), K13 (desde batch_040), K14 (desde batch_040)

**Veredicto:**


---

## Caso 55 — `ER-SP-compass_artifact_wf-f51aad3f-6ad1-4ebb-9cb3-cdab05234caa_text_markdown-007-SNP-001`

- **Batch de origen:** batch_043
- **Estrato:** E3

**snippet_primary:**

> "The main options are Gumroad - high fees and ugly design, solid system never had issues does most what I need · Lemon Squeezy - it was very popular until being acquired by stripe. Full of serious bugs, bad support. Lovely design, slightly better fees than Gumroad, but many hidden. Would still use over Gumroad just cause the Gumroad checkout design is so bad it loses sales imo"

| Campo | Sonnet | Fable |
|---|---|---|
| `evidence_role` _(A · 🔒 enum)_ | comparative_commentary | direct_claim |
| `local_qualifiers` _(A · 📝 texto libre)_ | slightly better fees than Gumroad, but many hidden | solid system never had issues does most what I need · it was very popular until being acquired by stripe. Full of serious bugs, bad support · slightly better fees than Gumroad, but many hidden · the Gumroad checkout design is so bad it loses sales imo |
| `parser_notes` _(A · 📝 texto libre)_ | Hacker News commenter's platform-user status (buyer vs seller) not explicitly stated; defaulted to seller given comparative fee/checkout framing | Actor 'seller' per assignment_rule (seller_forum, author choosing a platform to sell). Fee claims carry no figures — metric_type left 'unknown'. Source date '~2025-05' is approximate — source_date_unclear (K2). |
| `subject_exact` _(A · 📝 texto libre)_ | forum commenter's comparison of Gumroad fees/design vs Lemon Squeezy fees/bugs/support | forum author's comparison: Gumroad with high fees and ugly but solid checkout, Lemon Squeezy with lovely design and slightly better but partly hidden fees plus serious bugs and bad support since the Stripe acquisition |
| `time_scope_raw` _(B · 📝 texto libre)_ | ~2025-05 (approximately 11 months before April 2026) | _(null)_ |
| `uncertainties` _(A · 🔒 enum)_ | actor_level_unclear · time_scope_unclear | source_date_unclear |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016), S6 (desde batch_040), S7 (desde batch_040), S8 (desde batch_040)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032), K13 (desde batch_040), K14 (desde batch_040)

**Veredicto:**


---

## Caso 56 — `ER-SP-compass_artifact_wf-f51aad3f-6ad1-4ebb-9cb3-cdab05234caa_text_markdown-019-SNP-001`

- **Batch de origen:** batch_043
- **Estrato:** E3

**snippet_primary:**

> "We provide all-inclusive pricing of 5% + 50¢ per transaction. You might be used to similar fees over at Paddle, but that's just the beginning. Explore some of the benefits of Lemon Squeezy over Paddle below."

| Campo | Sonnet | Fable |
|---|---|---|
| `evidence_role` _(A · 🔒 enum)_ | official_policy | direct_claim |
| `local_qualifiers` _(B · 📝 texto libre)_ | _(lista vacia)_ | You might be used to similar fees over at Paddle, but that's just the beginning |
| `metric_unit` _(A · 📝 texto libre)_ | percent + USD flat | mixed: % + ¢ per transaction |
| `metric_value_raw` _(A · 📝 texto libre)_ | 5% + 50¢ | all-inclusive pricing of 5% + 50¢ per transaction |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | Platform's own competitor-comparison page — author_conflict_of_interest_possible (K4). Mixed units declared. Page not dated — not normalized (K1). |
| `subject_exact` _(A · 📝 texto libre)_ | Lemon Squeezy all-inclusive per-transaction fee positioned against Paddle | all-inclusive pricing of 5% + 50¢ per transaction, framed as similar to Paddle's fees with additional claimed benefits |
| `time_scope_raw` _(B · 📝 texto libre)_ | not dated | _(null)_ |
| `uncertainties` _(A · 🔒 enum)_ | none | author_conflict_of_interest_possible |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016), S6 (desde batch_040), S7 (desde batch_040), S8 (desde batch_040)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032), K13 (desde batch_040), K14 (desde batch_040)

**Veredicto:**


---

## Caso 57 — `ER-SP-compass_artifact_wf-f65accb1-75e2-4cb1-be7d-0d01a8fabf93_text_markdown-009-SNP-001`

- **Batch de origen:** batch_044
- **Estrato:** E3

**snippet_primary:**

> "We wanted to inform you that PayPal has suspended Gumroad's use of their service. As a result, we can no longer process payouts to PayPal accounts. We've invested heavily in direct bank transfers for nearly every country. We encourage you to connect a bank account directly to your Gumroad account to ensure uninterrupted payouts."

| Campo | Sonnet | Fable |
|---|---|---|
| `claim_type` _(A · 🔒 enum)_ | explicit_claim | policy_statement |
| `local_qualifiers` _(A · 📝 texto libre)_ | We've invested heavily in direct bank transfers for nearly every country | We've invested heavily in direct bank transfers for nearly every country · We encourage you to connect a bank account directly to your Gumroad account to ensure uninterrupted payouts |
| `metric_value_raw` _(B · 📝 texto libre)_ | _(null)_ | we can no longer process payouts to PayPal accounts |
| `parser_notes` _(A · 📝 texto libre)_ | Quoted Gumroad-to-seller notice reposted in a seller forum thread | PayPal named as the company taking the suspension action, not as an incidental payment method — included in platforms (K3). Quoted platform email relayed in a forum thread — actor 'platform' by who speaks (K7), evidence reported_event. · Narrated event — the October 16, 2024 email date does not normalize the claim's time scope (K1). |
| `subject_exact` _(A · 📝 texto libre)_ | PayPal's suspension of Gumroad's use of its payout service | platform email announcing PayPal suspended Gumroad's use of its service, ending PayPal payouts, with direct bank transfers offered for nearly every country instead |
| `time_scope_normalized_if_safe` _(B · 📝 texto libre)_ | 2024-10-16 | _(null)_ |
| `time_scope_raw` _(B · 📝 texto libre)_ | October 16, 2024 (email timestamp: Wed, 16 Oct 2024 22:11:34 UTC) | _(null)_ |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016), S6 (desde batch_040), S7 (desde batch_040), S8 (desde batch_040)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032), K13 (desde batch_040), K14 (desde batch_040)

**Veredicto:**


---

## Caso 58 — `ER-SP-compass_artifact_wf-fbf25436-287d-411c-be97-ee28c335a4a4_text_markdown-005-SNP-002`

- **Batch de origen:** batch_046
- **Estrato:** E3

**snippet_primary:**

> "DONT GO NEAR THIS COMPANY. SMOKESCREENS AND MIRRORS EXPERIENCE . ZERO CUSTOMER SUPPORT , NOT EVEN A BOT GENERATED COURTESY MAILMTOMSAY WE HAVE RECEIVED YOUR QUERY/COMPLAINT AND RE LOOKING INTO IT. I HAVE REPORTED THEM TO MASTERCARD WITH A REFUND REQUEST AND A RECOMMENDATION TO BLACK LIST THEM . WETHER IT IS INCOMPETENCE OR DELIBERATE FRAUDULENCE IS DIFFICULT TO TELL, BUT THE RESULT IS THE SAME. YOU WASTE TIME AND MONEY ON A PRODUCT THAT YOU PAY FOR BUT NEVER RECEIVE."

| Campo | Sonnet | Fable |
|---|---|---|
| `claim_type` _(A · 🔒 enum)_ | review_statement | anecdotal_report |
| `local_qualifiers` _(B · 📝 texto libre)_ | _(lista vacia)_ | ZERO CUSTOMER SUPPORT , NOT EVEN A BOT GENERATED COURTESY MAIL · WETHER IT IS INCOMPETENCE OR DELIBERATE FRAUDULENCE IS DIFFICULT TO TELL · YOU WASTE TIME AND MONEY ON A PRODUCT THAT YOU PAY FOR BUT NEVER RECEIVE |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | 'MASTERCARD' is a card network — excluded from platforms (K3). 'THIS COMPANY' is unnamed in text — platforms left empty (criterion F). |
| `platforms` _(B · 📝 texto libre)_ | Gumroad | _(lista vacia)_ |
| `subject_exact` _(A · 📝 texto libre)_ | Trustpilot buyer complaint of zero human customer-support response after escalating a Gumroad dispute to Mastercard | buyer reporting zero customer support with no acknowledgment of their complaint, a paid product never received, and a Mastercard refund request with a blacklist recommendation |
| `time_scope_normalized_if_safe` _(B · 📝 texto libre)_ | 2025-11-19 | _(null)_ |
| `time_scope_raw` _(B · 📝 texto libre)_ | November 19, 2025 | _(null)_ |
| `uncertainties` _(A · 🔒 enum)_ | none | anecdotal_single_source |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016), S6 (desde batch_040), S7 (desde batch_040), S8 (desde batch_040)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032), K13 (desde batch_040), K14 (desde batch_040)

**Veredicto:**


---

## Caso 59 — `ER-SP-compass_artifact_wf-fbf25436-287d-411c-be97-ee28c335a4a4_text_markdown-006-SNP-001`

- **Batch de origen:** batch_046
- **Estrato:** E3

**snippet_primary:**

> "BUYERS BEWARE: I purchased a chrome extension for $17 that didn't work. I never received a receipt and the extension didn't work with no contact info for the developer. I contacted support after multiple AI email responses, was forced to open a chargeback. TERRIBLE customer service. I wish I'd checked into this website before purchasing this extension."

| Campo | Sonnet | Fable |
|---|---|---|
| `claim_type` _(A · 🔒 enum)_ | review_statement | anecdotal_report |
| `local_qualifiers` _(B · 📝 texto libre)_ | _(lista vacia)_ | I purchased a chrome extension for $17 that didn't work · I never received a receipt · was forced to open a chargeback |
| `metric_unit` _(B · 📝 texto libre)_ | USD | _(null)_ |
| `metric_value_raw` _(B · 📝 texto libre)_ | $17 | _(null)_ |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | 'chrome extension' is a software product — product_type 'software' (closest explicit match). 'chrome' appears inside the product label — excluded from platforms (K3). Gumroad named only in source_ref ('this website') — platforms left empty (criterion F). |
| `platforms` _(B · 📝 texto libre)_ | Gumroad | _(lista vacia)_ |
| `subject_exact` _(A · 📝 texto libre)_ | Trustpilot buyer complaint of a non-functional Chrome extension purchase with no developer contact on Gumroad | buyer of a $17 Chrome extension that did not work, with no receipt, no developer contact info, multiple AI support replies, and a forced chargeback |
| `time_scope_normalized_if_safe` _(B · 📝 texto libre)_ | 2025-08-12 | _(null)_ |
| `time_scope_raw` _(B · 📝 texto libre)_ | August 12, 2025 | _(null)_ |
| `uncertainties` _(A · 🔒 enum)_ | none | anecdotal_single_source |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016), S6 (desde batch_040), S7 (desde batch_040), S8 (desde batch_040)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032), K13 (desde batch_040), K14 (desde batch_040)

**Veredicto:**


---

## Caso 60 — `ER-SP-compass_artifact_wf-ff9eedd9-5f17-49fb-9226-4a8afea39903_text_markdown_normalized-017-SNP-001`

- **Batch de origen:** batch_047
- **Estrato:** E3

**snippet_primary:**

> "All your marketing was linked to the gumroad page. That means you need to update all those links. But do you honestly know and control where those links are? I don't think you will. There will be people mentioning it in Reddit comments, reddit posts, IH comments, Hacker News comments, slack messages... Changing to a competitor is probably going to result in lost sales if you've got any decent traction in social media."

| Campo | Sonnet | Fable |
|---|---|---|
| `claim_type` _(A · 🔒 enum)_ | comparative_commentary | instructional_statement |
| `evidence_role` _(A · 🔒 enum)_ | anecdotal_example | direct_claim |
| `local_qualifiers` _(B · 📝 texto libre)_ | _(lista vacia)_ | But do you honestly know and control where those links are? I don't think you will · Changing to a competitor is probably going to result in lost sales if you've got any decent traction in social media |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | Actor 'seller' per assignment_rule (seller_forum, seller-audience advice). Post date 'undated (context suggests early-to-mid 2023)' is approximate — source_date_unclear (K2). |
| `platforms` _(A · 📝 texto libre)_ | Gumroad | Gumroad · Reddit · Hacker News · Slack |
| `subject_exact` _(A · 📝 texto libre)_ | peer-warned risk of lost sales when migrating away from Gumroad due to uncontrolled external link references | warning that migrating off a Gumroad page breaks uncontrolled inbound links across Reddit, Hacker News, Slack and elsewhere, likely costing sales for sellers with social traction |
| `time_scope_raw` _(B · 📝 texto libre)_ | Accessed April 2026; post undated (context suggests early-to-mid 2023) | _(null)_ |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016), S6 (desde batch_040), S7 (desde batch_040), S8 (desde batch_040)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032), K13 (desde batch_040), K14 (desde batch_040)

**Veredicto:**


---

## Apendice — texto de las adiciones de criterio referenciadas

Derivado de `criteria.md` de cada rama. Una adicion registrada 'tras
batch_N' rige desde batch_N+1: ambos criteria.md declaran las adiciones
como no retroactivas.

### Sonnet

- **S1** (formulada tras batch_008, vigente desde batch_009): Métricas de agregadores/bases de datos que no mapean a ningún valor del enum metric_type (p.ej. conteo de creadores con al menos un pagador, distribución de perfiles por categoría de contenido, conteo agregado de quejas en una plataforma de terceros) se escriben como string descriptivo literal (out_of_enum), nunca forzadas al valor "menos malo" del enum (p.ej. active_buyers colapsaría conteo de creadores con conteo de compradores).
- **S2** (formulada tras batch_008, vigente desde batch_009): Bloques de estadísticas de ranking/database_profile que combinan 2-3 métricas explícitas en un solo bloque visual sin que ninguna domine (p.ej. paid-member count + monthly payout de una misma entidad rankeada) se registran como metric_type en array con un solo metric_value_raw combinado en string, no se separan en registros distintos si llegaron como una sola unidad de snippet.
- **S3** (formulada tras batch_008, vigente desde batch_009): Respuestas en foros de vendedores donde no es determinable si quien responde es staff de la plataforma o un vendedor par (p.ej. respuestas de soporte dirigidas por nombre de usuario en foros de Domestika) se resuelven por defecto como actor_level "seller" (regla por defecto del contrato para seller_forum), agregando actor_level_unclear a uncertainties y una nota en parser_notes explicando la ambigüedad — nunca se asume "platform" sin evidencia explícita de que quien habla es la plataforma misma.
- **S4** (formulada tras batch_016, vigente desde batch_017): source_type "buyer_review" no determina por sí solo actor_level "buyer". Reseñas en sitios de terceros (Trustpilot, BBB) que mecánicamente llevan source_type=buyer_review pueden estar escritas por sellers/creators quejándose de payouts, suspensiones de cuenta o fees — el texto mismo revela quién habla ("I am a seller on Gumroad...", "sells items with full resale rights"). Se aplica la regla general del contrato ("quién habla, no source_type") y se asigna actor_level "seller" cuando el hablante se identifica explícitamente como vendedor/creador, independientemente de la etiqueta mecánica de source_type.
- **S5** (formulada tras batch_016, vigente desde batch_017): Snippets truncados con elipsis final ("...") en reviews de terceros (Trustpilot) o en listados/tablas parcialmente capturados (listas de países, monedas) no se rechazan por esta razón sola. Se preservan como aparecen, se registra uncertainties: context_insufficient, y se agrega una nota en parser_notes indicando que el fragmento está incompleto y que el valor final (p.ej. cifra exacta, país completo de la lista) no está disponible en el snippet capturado. Solo se rechaza (subject_exact unfillable) si el truncamiento deja el sujeto mismo indeterminable, no solo un detalle secundario.
- **S6** (formulada tras batch_040, vigente desde batch_041): Skeletons cuyo snippet_primary es enteramente un placeholder de recuperación fallida (p.ej. "n/a — content recovered via research subagent's direct fetch of X; verbatim character-for-character accuracy cannot be independently confirmed") sin ningún texto real de la página capturado, se rechazan por subject_exact_unfillable — no hay afirmación real que sostenga un sujeto. No confundir con snippets truncados con "..." (batch_016), que sí preservan texto real parcial y no se rechazan por esa razón sola.
- **S7** (formulada tras batch_040, vigente desde batch_041): Cifras de CTR o de variación porcentual que exceden el rango normal 0-100% (p.ej. "12-mo average CTR is 127%", "monthly CTR up 892%") se preservan verbatim tal como las reporta la fuente de terceros, sin corregir ni reinterpretar. No se usa metric_unit_unclear (phase_2_only, prohibido en Fase 1); se usa methodology_unclear si se necesita marcar la anomalía.
- **S8** (formulada tras batch_040, vigente desde batch_041): Nombres de moneda (p.ej. "mexican peso", "Brazilian Real", "Colombian Pesos", "Argentine Pesos") implican geografía pero no son, por sí mismos, un nombre de lugar explícito en el snippet. geography_if_explicit se deja null cuando la única señal geográfica es el nombre de una moneda, con nota en parser_notes explicando la inferencia implícita descartada; se prioriza esta regla sobre inferir el país a partir del gentilicio de la moneda, salvo que el mismo snippet nombre el país o gentilicio de forma independiente (p.ej. "Argentine Pesos" Y "Argentina" both appearing, or an adjective form like "mexicano/mexican" modifying a noun directly, en cuyo caso el adjetivo sí cuenta como explícito).

### Fable

- **K1** (formulada tras batch_008, vigente desde batch_009): Normalización temporal desde metadata de página (extiende G): una fecha de contenido explícita en source_date_if_available (publicado / last updated / reviewed / effective / changelog / fecha de post) normaliza el time_scope de claims que describen ESTADO vigente (política, pricing, disponibilidad, comparativa) cuando time_scope_raw es null. Fechas solo de acceso ("Accessed ...") NUNCA normalizan. Eventos o anécdotas narradas NO toman la fecha de publicación; solo normalizan si el propio claim trae fecha explícita. Si raw es relativo ("currently", "now") → normalized null (G literal).
- **K2** (formulada tras batch_008, vigente desde batch_009): Fechas aproximadas ("~2025", "circa") no normalizan y añaden source_date_unclear. Mes sin año en snippet no se normaliza aunque la fecha de página permita inferir el año.
- **K3** (formulada tras batch_008, vigente desde batch_009): platforms (afina F): una mención textual solo cuenta si nombra la plataforma/servicio como tal; etiquetas de categoría, temas de curso o nombres de creadores que coinciden con nombres de plataforma se excluyen con parser_note.
- **K4** (formulada tras batch_008, vigente desde batch_009): author_conflict_of_interest_possible se asigna a voz promocional en primera persona sobre producto/servicio propio (vendor listings, blogs de plataforma sobre sí misma o competidores, posts con link de afiliado).
- **K5** (formulada tras batch_008, vigente desde batch_009): metric_type out-of-enum: si la fuente da una etiqueta ("Paid Members", "Number of Paid Creators", "plazo máximo de activación") se copia verbatim; si no hay etiqueta, descriptor mínimo en snake/espacios + cita del wording en parser_notes.
- **K6** (formulada tras batch_008, vigente desde batch_009): evidence_role para voz de plataforma: official_policy solo para documentos de política/help/legal/pricing formales y anuncios de política; respuestas de soporte en foros y copy de marketing → direct_claim.
- **K7** (formulada tras batch_008, vigente desde batch_009): actor_level para source_types no mapeados por la assignment_rule (report, news, unknown, buyer_review, interview, database_profile) y para autores atípicos (blog de plataforma, blog de competidor, staff en foro): se asigna por "quién habla" (regla D) y se registra issue contract_case_uncovered por record. Rol del hablante indeterminable → unknown + actor_level_unclear.
- **K8** (formulada tras batch_016, vigente desde batch_017): Snippets truncados (elipsis final, corte a media palabra, listas de layout con "...") → uncertainties += snippet_needs_reopen y parser_note; el contenido faltante no se reconstruye ni se infiere.
- **K9** (formulada tras batch_016, vigente desde batch_017): buyer_review con voz de vendedor (quejas de cuenta/payout de creadores en sitios de reseñas) → actor_level seller por "quién habla" (extiende K7), con issue contract_case_uncovered; el source_type prefijado se preserva.
- **K10** (formulada tras batch_032, vigente desde batch_033): Capturas de tablas/layout de sitios analíticos ("[Stated in layout: ...]"): la tabla completa se preserva verbatim en metric_value_raw en orden de listado, las unidades mixtas se declaran en metric_unit ("mixed: ..."), y metric_type recibe descriptor mínimo K5 (p. ej. "revenue by category", "store count by category"). La anotación de captura ("[Stated in layout:", "[From Google search index snippet") se registra en parser_notes y no se trata como truncación K8.
- **K11** (formulada tras batch_032, vigente desde batch_033): Páginas con voz de plataforma prefijadas con source_type de vendedor (product_listing de páginas de features/pricing/partner/navegación, blog corporativo, article de help-center): actor_level por "quién habla" (platform) + issue contract_case_uncovered (extiende K7). Los listados genuinos de productos de vendedores mantienen third_party según la assignment_rule sin issue.
- **K12** (formulada tras batch_032, vigente desde batch_033): Proveedores de datos/analítica reportando estimaciones sobre una plataforma (Semrush, SimilarWeb, 6sense, Storeleads, Gumtrends, Wappalyzer, ful.io) → actor "source" + methodology_unclear si la cifra es estimación sin metodología declarada. Proveedores de integraciones/herramientas promocionando su propia integración con la plataforma (Zapier, Pipedream, Pabbly, Make, widgets, apps) → actor "third_party" + author_conflict_of_interest_possible (K4).
- **K13** (formulada tras batch_040, vigente desde batch_041): Skeletons sin contenido de fuente (snippet_primary consiste solo en una nota de recuperación tipo "n/a — content recovered via research subagent..."): subject_exact es irrellenable sin inferencia → destino rejected_archive con required_field_unfillable, citando la nota en el detalle. El contenido nunca se reconstruye desde source_title ni la URL.
- **K14** (formulada tras batch_040, vigente desde batch_041): Fees de pasarelas de pago de terceros relatadas por la plataforma en help-center ("Connect your X account"): claim pricing_statement con metric_type fee_rate (unidades mixtas declaradas), la pasarela y demás métodos de pago se excluyen de platforms (extiende K3), y el descargo "collected by X and do not go to [platform]" se copia como qualifier. Las listas de países soportados van como payment_method_availability con geography verbatim y el listado completo preservado.
- **K15** (formulada tras batch_048, vigente desde batch_049): Testimonios de vendedores curados en páginas de marketing de la plataforma: actor "seller" por quién habla + issue K7, evidence seller_self_claim, y uncertainties anecdotal_single_source + author_conflict_of_interest_possible por el contexto promocional curado.
- **K16** (formulada tras batch_048, vigente desde batch_049): Páginas de comparación/"alternative" alojadas por una plataforma competidora que se compara a sí misma: actor "platform" por quién habla (K11) + issue + author_conflict_of_interest_possible (K4). Vendedores que comparan a terceros sin ser sujeto de la comparación → "third_party" + K4. Emails o anuncios de plataforma citados dentro de foros → actor "platform" + evidence reported_event.

