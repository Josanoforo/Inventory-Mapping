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

## Caso 1 — `ER-SP-compass_artifact_wf-0ffe7308-62e3-4530-ae68-93720df60f34_text_markdown-012-SNP-003`

- **Batch de origen:** batch_002
- **Estrato:** E1

**snippet_primary:**

> "By default, the base currency of an etsy shop is set to be the same as that of the seller's native currency. However, sellers have an option to change the base currency used by their shops and thus their listings. If you change your shop's base currency to something other than your native currency, an extra 2.5% conversion fee will be charged on all deposits."

| Campo | Sonnet | Fable |
|---|---|---|
| `actor_level` _(A · 🔒 enum)_ | platform | source |
| `claim_type` _(A · 🔒 enum)_ | policy_statement | pricing_statement |
| `evidence_role` _(A · 🔒 enum)_ | official_policy | direct_claim |
| `local_qualifiers` _(A · 📝 texto libre)_ | if you change your shop's base currency to something other than your native currency | By default · If you change your shop's base currency to something other than your native currency · on all deposits |
| `metric_unit` _(A · 📝 texto libre)_ | percent | percent of deposits |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | Third-party calculator page (Investomatica) describing Etsy fee policy; page attributes data to 'Source: etsy.com'. · time_scope_normalized_if_safe from source_date_if_available ('Last reviewed April 4, 2026') per criteria G. |
| `subject_exact` _(A · 📝 texto libre)_ | Etsy shop base currency conversion fee when set to a non-native currency | Etsy 2.5% currency conversion fee on deposits when shop base currency differs from seller's native currency |
| `time_scope_normalized_if_safe` _(B · 📝 texto libre)_ | _(null)_ | 2026-04-04 |
| `uncertainties` _(B · 🔒 enum)_ | none | _(lista vacia)_ |

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

## Caso 3 — `ER-SP-compass_artifact_wf-22c5fbd5-9e04-4d5a-9b0e-4cb97acec9cc_text_markdown_normalized-011-SNP-007`

- **Batch de origen:** batch_003
- **Estrato:** E1

**snippet_primary:**

> "In August 2025, when Diego Gomez*, a Madrid-based Domestika instructor, checked his instructor dashboard, he found that the billion-dollar company had stopped paying him since July. The reason was his inactivity in the forum. He didn't understand why the online creative learning platform had halted his payments now. He had stopped replying to comments four years ago (his contract never stated it as a payment condition), and he was still getting paid until June 2025."

| Campo | Sonnet | Fable |
|---|---|---|
| `actor_level` _(A · 🔒 enum)_ | seller | source |
| `geography_if_explicit` _(A · 📝 texto libre)_ | Madrid, España | Madrid |
| `local_qualifiers` _(A · 📝 texto libre)_ | his contract never stated forum activity as a payment condition | The reason was his inactivity in the forum · He had stopped replying to comments four years ago (his contract never stated it as a payment condition) · he was still getting paid until June 2025 |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | Asterisk after the instructor name marks a pseudonym per the source's convention. · Third-person journalistic narration of one instructor's account; assigned 'source'. |
| `subject_exact` _(A · 📝 texto libre)_ | Instructor-reported payment halt tied to forum-comment inactivity despite years of prior payment continuity (Diego Gomez, per report) | reported Domestika payment halt since July 2025 for Madrid-based instructor Diego Gomez attributed to forum inactivity, discovered August 2025 |
| `time_scope_raw` _(A · 📝 texto libre)_ | In August 2025... since July... four years ago... until June 2025 | In August 2025 |

**Criterios vigentes en este batch:**

- Sonnet — ninguna adicion formulada aun; solo criterios base.
- Fable — ninguna adicion formulada aun; solo criterios base.

**Veredicto:**


---

## Caso 4 — `ER-SP-compass_artifact_wf-22c5fbd5-9e04-4d5a-9b0e-4cb97acec9cc_text_markdown_normalized-011-SNP-008`

- **Batch de origen:** batch_004
- **Estrato:** E1

**snippet_primary:**

> "They answered that we can have a video call, I said no as I just wanted a written answer saying if they are going to pay or not. Since then, no more replies."

| Campo | Sonnet | Fable |
|---|---|---|
| `evidence_role` _(A · 🔒 enum)_ | reported_event | seller_self_claim |
| `local_qualifiers` _(B · 📝 texto libre)_ | _(lista vacia)_ | I just wanted a written answer saying if they are going to pay or not · Since then, no more replies |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | First-person instructor quote inside a journalistic report; counterpart ('They') unnamed in snippet; platforms left empty per criteria F. |
| `platforms` _(B · 📝 texto libre)_ | Domestika | _(lista vacia)_ |
| `subject_exact` _(A · 📝 texto libre)_ | Instructor-reported unresponsiveness from Domestika when requesting a written answer on payment status, per investigative report | instructor-reported offer of a video call instead of a written answer on payment, followed by no further replies |
| `time_scope_raw` _(B · 📝 texto libre)_ | _(null)_ | Since then |

**Criterios vigentes en este batch:**

- Sonnet — ninguna adicion formulada aun; solo criterios base.
- Fable — ninguna adicion formulada aun; solo criterios base.

**Veredicto:**


---

## Caso 5 — `ER-SP-compass_artifact_wf-28ef9d76-a020-462a-83e9-3321b6ece5b4_text_markdown_normalized-003-SNP-002`

- **Batch de origen:** batch_004
- **Estrato:** E1

**snippet_primary:**

> "Payhip doesn't come with extra features such as communities, live chat, and a full-fledged email marketing system built-in (that Podia comes with). Payhip does integrate with MailChimp out of the box though."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(B · 📝 texto libre)_ | _(lista vacia)_ | built-in · out of the box |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | time_scope_normalized_if_safe from source_date_if_available ('Sep 19, 2022') per criteria G. |
| `platforms` _(A · 📝 texto libre)_ | Podia · Payhip | Payhip · Podia · MailChimp |
| `subject_exact` _(A · 📝 texto libre)_ | Third-party blog comparison of Podia and Payhip built-in feature sets (community, live chat, email marketing, MailChimp integration) | feature comparison: Payhip lacking built-in communities, live chat and full email marketing versus Podia, while integrating with MailChimp |
| `time_scope_raw` _(B · 📝 texto libre)_ | Sep 19, 2022 | _(null)_ |
| `uncertainties` _(B · 🔒 enum)_ | none | _(lista vacia)_ |

**Criterios vigentes en este batch:**

- Sonnet — ninguna adicion formulada aun; solo criterios base.
- Fable — ninguna adicion formulada aun; solo criterios base.

**Veredicto:**


---

## Caso 6 — `ER-SP-compass_artifact_wf-28ef9d76-a020-462a-83e9-3321b6ece5b4_text_markdown_normalized-009-SNP-001`

- **Batch de origen:** batch_005
- **Estrato:** E1

**snippet_primary:**

> "At Payhip, our goal is to make pricing as simple and transparent as possible. So, no feature-gating here! You'll get access to all of our amazing features to help you grow your business, even on our free plan."

| Campo | Sonnet | Fable |
|---|---|---|
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | Own pricing page statement; no fee figures in this snippet. |
| `subject_exact` _(A · 📝 texto libre)_ | Payhip's own claim of full feature access on its free plan with no feature-gating, per its Pricing page | Payhip pricing-page claim of no feature-gating with access to all features including on the free plan |
| `uncertainties` _(A · 🔒 enum)_ | none | source_date_unclear |

**Criterios vigentes en este batch:**

- Sonnet — ninguna adicion formulada aun; solo criterios base.
- Fable — ninguna adicion formulada aun; solo criterios base.

**Veredicto:**


---

## Caso 7 — `ER-SP-compass_artifact_wf-28f59dc7-8351-48a1-bcaa-ff9992b8fe70_text_markdown-003-SNP-002`

- **Batch de origen:** batch_006
- **Estrato:** E1

**snippet_primary:**

> "El día 2 de julio de 2025 compré un curso individual en la plataforma Domestika por 0,99 €. En el mes de agosto de 2025 se cargó en mi cuenta bancaria un importe de 313,41 €, correspondiente"

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(B · 📝 texto libre)_ | _(lista vacia)_ | un curso individual · por 0,99 € |
| `metric_value_raw` _(A · 📝 texto libre)_ | 0,99€ course; 313,41€ charge | 313,41 € |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | Snippet truncated mid-sentence ('correspondiente'); what the charge corresponded to was not captured. · Additional figure in snippet: course price '0,99 €'. |
| `subject_exact` _(A · 📝 texto libre)_ | Buyer complaint of a 0.99€ individual course purchase followed by a 313.41€ bank charge the next month | buyer-reported 313.41€ bank charge in August 2025 following a 0.99€ single course purchase on Domestika on July 2, 2025 |
| `time_scope_normalized_if_safe` _(A · 📝 texto libre)_ | 2025-07-02 | 2025-07-02/2025-08 |
| `time_scope_raw` _(A · 📝 texto libre)_ | El día 2 de julio de 2025... En el mes de agosto de 2025 | El día 2 de julio de 2025 … En el mes de agosto de 2025 |
| `uncertainties` _(A · 🔒 enum)_ | anecdotal_single_source | anecdotal_single_source · snippet_needs_reopen |

**Criterios vigentes en este batch:**

- Sonnet — ninguna adicion formulada aun; solo criterios base.
- Fable — ninguna adicion formulada aun; solo criterios base.

**Veredicto:**


---

## Caso 8 — `ER-SP-compass_artifact_wf-291008ae-711f-4c29-83eb-6a5c8ef0eef8_text_markdown_normalized-003-SNP-002`

- **Batch de origen:** batch_007
- **Estrato:** E1

**snippet_primary:**

> "I have paid money to this address for a shutter count on my camera and i didn't receive any information on it. Very annoyed !"

| Campo | Sonnet | Fable |
|---|---|---|
| `claim_type` _(A · 🔒 enum)_ | review_statement | anecdotal_report |
| `parser_notes` _(A · 📝 texto libre)_ | Specific merchant/product behind the 'shutter count' service is not identified in the snippet beyond the review platform context (Lemon Squeezy). | Company name appears only in source_ref URL; platforms left empty per criteria F. |
| `platforms` _(B · 📝 texto libre)_ | Lemon Squeezy | _(lista vacia)_ |
| `subject_exact` _(A · 📝 texto libre)_ | Buyer review reporting payment for a shutter-count service with no information received in return | buyer-reported payment for a camera shutter-count service without receiving the information |
| `uncertainties` _(A · 🔒 enum)_ | anecdotal_single_source · subject_ambiguity | anecdotal_single_source |

**Criterios vigentes en este batch:**

- Sonnet — ninguna adicion formulada aun; solo criterios base.
- Fable — ninguna adicion formulada aun; solo criterios base.

**Veredicto:**


---

## Caso 9 — `ER-SP-compass_artifact_wf-295a3f4a-2ebb-4c3b-9b1d-9b7d3840172c_text_markdown-004-SNP-001`

- **Batch de origen:** batch_008
- **Estrato:** E1

**snippet_primary:**

> "Otra cosa interesante, es que podemos tener nuestra versión en ingles, ya que hacen envíos a Estados Unidos, eso si, tienes que traducir tu mismo por cada articulo que hagas."

| Campo | Sonnet | Fable |
|---|---|---|
| `evidence_role` _(A · 🔒 enum)_ | anecdotal_example | seller_self_claim |
| `local_qualifiers` _(A · 📝 texto libre)_ | tienes que traducir tu mismo por cada articulo | eso si, tienes que traducir tu mismo por cada articulo que hagas |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | Platform name appears only in source_title/URL ('hacen envíos' in text); platforms left empty per criteria F. · source_date_if_available is approximate ('circa 2015–2017'); not normalized. |
| `platforms` _(B · 📝 texto libre)_ | Kichink | _(lista vacia)_ |
| `subject_exact` _(A · 📝 texto libre)_ | Blogger's account of testing the Kichink store, noting English-language storefront capability requiring manual per-item translation for US shipments | seller-reported English store version option with US shipping on Kichink, requiring manual per-item translation by the seller |
| `time_scope_raw` _(B · 📝 texto libre)_ | circa 2015-2017 (por contexto) | _(null)_ |

**Criterios vigentes en este batch:**

- Sonnet — ninguna adicion formulada aun; solo criterios base.
- Fable — ninguna adicion formulada aun; solo criterios base.

**Veredicto:**


---

## Caso 10 — `ER-SP-compass_artifact_wf-3128bd63-7fd1-4bd6-86d1-63a1780fe467_text_markdown-003-SNP-003`

- **Batch de origen:** batch_008
- **Estrato:** E1

**snippet_primary:**

> "If you're in a country that has no tax treaty with the US, unfortunately, we won't be able to reduce the royalty withholding tax rate of 30%."

| Campo | Sonnet | Fable |
|---|---|---|
| `geography_if_explicit` _(A · 📝 texto libre)_ | US | the US |
| `local_qualifiers` _(B · 📝 texto libre)_ | _(lista vacia)_ | If you're in a country that has no tax treaty with the US |
| `metric_type` _(A · 🔒 enum)_ | fee_rate | tax_withholding_rate |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | metric_type out of enum: observed metric is a tax withholding rate; no enum value covers it. · Platform name appears only in source_title/URL; platforms left empty per criteria F. |
| `platforms` _(B · 📝 texto libre)_ | Envato | _(lista vacia)_ |
| `subject_exact` _(A · 📝 texto libre)_ | Envato inability to reduce the 30% royalty withholding tax rate for authors in countries without a US tax treaty | no reduction of the 30% royalty withholding rate for authors in countries without a US tax treaty |
| `uncertainties` _(A · 🔒 enum)_ | none | source_date_unclear |

**Criterios vigentes en este batch:**

- Sonnet — ninguna adicion formulada aun; solo criterios base.
- Fable — ninguna adicion formulada aun; solo criterios base.

**Veredicto:**


---

## Caso 11 — `ER-SP-compass_artifact_wf-345ae7ea-8655-485d-821e-f35693f6a78f_text_markdown-005-SNP-001`

- **Batch de origen:** batch_009
- **Estrato:** E1

**snippet_primary:**

> "I mentioned that I have a Payhip store too where I sell my software-related products. I promote the store only my on Faceless-Voiceless YouTube Channel. And so far, I have made 7 sales. Currently, I have only 68 subscribers on this channel."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(A · 📝 texto libre)_ | promoted only via a single Faceless-Voiceless YouTube channel with 68 subscribers | I promote the store only my on Faceless-Voiceless YouTube Channel · Currently, I have only 68 subscribers on this channel |
| `parser_notes` _(A · 📝 texto libre)_ | YouTube subscriber count (68) preserved as qualifier/context rather than a separate metric, to avoid collapsing a traffic-source count with the Payhip sales_count claim (Rule 1) | 'software-related products' is ambiguous between software itself and products about software; product_type_if_explicit set to unknown with product_type_unclear. |
| `product_type_if_explicit` _(A · 🔒 enum)_ | software | unknown |
| `subject_exact` _(A · 📝 texto libre)_ | seller-reported sales count for a software products store on Payhip promoted via a single small YouTube channel | seller-reported 7 sales of software-related products on a Payhip store promoted only via a 68-subscriber faceless YouTube channel |
| `time_scope_raw` _(A · 📝 texto libre)_ | so far | so far … Currently |
| `uncertainties` _(A · 🔒 enum)_ | anecdotal_single_source | anecdotal_single_source · product_type_unclear · source_date_unclear |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008)

**Veredicto:**


---

## Caso 12 — `ER-SP-compass_artifact_wf-345ae7ea-8655-485d-821e-f35693f6a78f_text_markdown-010-SNP-002`

- **Batch de origen:** batch_009
- **Estrato:** E1

**snippet_primary:**

> "I tried shopify and felt like I needed a PhD. I couldn't figure it out. I like the ease of Payhip, plus I don't need 67 plugins to do simple things."

| Campo | Sonnet | Fable |
|---|---|---|
| `claim_type` _(A · 🔒 enum)_ | review_statement | comparative_commentary |
| `local_qualifiers` _(A · 📝 texto libre)_ | don't need 67 plugins to do simple things | I couldn't figure it out · plus I don't need 67 plugins to do simple things |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | 'felt like I needed a PhD' is the seller's hyperbole, preserved in snippet only. |
| `subject_exact` _(A · 📝 texto libre)_ | seller-reported ease of use of Payhip compared to Shopify setup complexity | author-seller comparison: Shopify perceived as too complex versus Payhip's ease without plugin dependence |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008)

**Veredicto:**


---

## Caso 13 — `ER-SP-compass_artifact_wf-345ae7ea-8655-485d-821e-f35693f6a78f_text_markdown-012-SNP-001`

- **Batch de origen:** batch_009
- **Estrato:** E1

**snippet_primary:**

> "This is the thing most Payhip reviews gloss over. The platform is excellent at processing a transaction once someone has decided to buy. What it cannot do is bring that person to you in the first place. This is the central challenge of Test 02 for us. We have created three digital products — a ChatGPT prompt workbook, an AI tools directory and a Whiteout Survival strategy guide — listed them on Payhip and priced them reasonably. The products are live. The checkout works. But without traffic, nothing sells."

| Campo | Sonnet | Fable |
|---|---|---|
| `claim_type` _(A · 🔒 enum)_ | comparative_commentary | explicit_claim |
| `local_qualifiers` _(A · 📝 texto libre)_ | products are live, checkout works · without traffic, nothing sells | This is the thing most Payhip reviews gloss over · priced them reasonably · But without traffic, nothing sells |
| `parser_notes` _(A · 📝 texto libre)_ | three product types named (ChatGPT prompt workbook, AI tools directory, Whiteout Survival strategy guide) do not map cleanly/uniformly to a single schema product_type_if_explicit enum value; set to unknown rather than forced to a less-bad value | Products explicitly named (ChatGPT prompt workbook; AI tools directory; Whiteout Survival strategy guide) but they span types without a dominant enum match; product_type set to unknown. · source_date_if_available derives only from title year ('2026'); not normalized. |
| `subject_exact` _(A · 📝 texto libre)_ | seller-reported distinction between Payhip checkout capability and traffic/discovery generation for three listed digital products | seller-tested claim that Payhip processes transactions well but brings no traffic, with three live priced products unsold without traffic |
| `uncertainties` _(A · 🔒 enum)_ | anecdotal_single_source · product_type_unclear | anecdotal_single_source · source_date_unclear |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008)

**Veredicto:**


---

## Caso 14 — `ER-SP-compass_artifact_wf-4ef0d94a-344f-48de-a6a0-29bd09258ed5_text_markdown_normalized-015-SNP-010`

- **Batch de origen:** batch_013
- **Estrato:** E1

**snippet_primary:**

> "Unfortunately, at this time, we are unable to offer partial refunds for your purchases."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(B · 📝 texto libre)_ | _(lista vacia)_ | at this time |
| `parser_notes` _(A · 📝 texto libre)_ | wording ("at this time") signals a possibly temporary state rather than a permanent policy | Platform name appears only in source_ref URL for this snippet; platforms left empty per criteria F. · time_scope_raw 'at this time' is relative; normalized left null per criteria G. |
| `platforms` _(B · 📝 texto libre)_ | Domestika | _(lista vacia)_ |
| `subject_exact` _(A · 📝 texto libre)_ | Domestika's current inability to offer partial refunds | no partial refunds offered for purchases at this time |
| `uncertainties` _(B · 🔒 enum)_ | current_vs_historical_ambiguity | _(lista vacia)_ |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008)

**Veredicto:**


---

## Caso 15 — `ER-SP-compass_artifact_wf-4ff72059-9383-471e-a419-d446777044ad_text_markdown-004-SNP-014`

- **Batch de origen:** batch_014
- **Estrato:** E1

**snippet_primary:**

> "Abono a su Cuenta Kash®: El COMPRADOR, podrá solicitar el abono del importe del producto devuelto a su Cuenta Kash®; sin embargo, el costo del envió no podrá ser reembolsado y en ningún caso será absorbido por KICHINK. Transferencia bancaria: El Comprador podrá solicitar la devolución mediante transferencia bancaria por el total de la compra. Cupón: Si así lo desea, El Comprador podrá solicitar un cupón por el monto total de su compra, mismo que podrá ser utilizado por El Comprador para realizar cualquier otra compra en Las Tiendas afiliadas con Kichink, en un plazo no mayor a 90 días."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(A · 📝 texto libre)_ | el costo del envío no podrá ser reembolsado y en ningún caso será absorbido por KICHINK | el costo del envió no podrá ser reembolsado y en ningún caso será absorbido por KICHINK · en un plazo no mayor a 90 días |
| `metric_unit` _(B · 📝 texto libre)_ | days | _(null)_ |
| `metric_value_raw` _(B · 📝 texto libre)_ | 90 | _(null)_ |
| `subject_exact` _(A · 📝 texto libre)_ | Kichink buyer refund method options (Kash account credit, bank transfer, or store coupon valid 90 days), with shipping cost non-refundable | buyer refund options for returned products: Kash account credit (shipping non-refundable), bank transfer for the full purchase, or a coupon valid 90 days at Kichink-affiliated stores |
| `time_scope_raw` _(B · 📝 texto libre)_ | en un plazo no mayor a 90 días | _(null)_ |
| `uncertainties` _(B · 🔒 enum)_ | _(lista vacia)_ | source_date_unclear |

Diferencias de solo orden (C) en este record, no motivan inclusion:
- `platforms`

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008)

**Veredicto:**


---

## Caso 16 — `ER-SP-compass_artifact_wf-5c07963d-6c4c-4536-a602-03c04203e92c_text_markdown-004-SNP-001`

- **Batch de origen:** batch_014
- **Estrato:** E1

**snippet_primary:**

> "Gumroad's user-friendly interface makes it easy for anyone to build a hosted storefront with minimal effort. Still, Etsy has one key advantage over Gumroad: an established customer base. With Etsy, you don't need to have an existing social media following to make sales."

| Campo | Sonnet | Fable |
|---|---|---|
| `actor_level` _(A · 🔒 enum)_ | source | third_party |
| `local_qualifiers` _(B · 📝 texto libre)_ | _(lista vacia)_ | with minimal effort · Still, Etsy has one key advantage over Gumroad |
| `parser_notes` _(A · 📝 texto libre)_ | source (Sellfy) is a competing platform to both Gumroad and Etsy; this specific snippet does not promote Sellfy directly but carries a possible competitive framing | Blog hosted by Sellfy, a competing platform. |
| `subject_exact` _(A · 📝 texto libre)_ | comparison of Gumroad's ease of storefront setup versus Etsy's established customer base advantage (no existing following required to sell) | comparison: Gumroad easy hosted storefront versus Etsy's established customer base enabling sales without an existing social following |
| `uncertainties` _(A · 🔒 enum)_ | author_conflict_of_interest_possible | source_date_unclear · author_conflict_of_interest_possible |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008)

**Veredicto:**


---

## Caso 17 — `ER-SP-compass_artifact_wf-5c07963d-6c4c-4536-a602-03c04203e92c_text_markdown-006-SNP-002`

- **Batch de origen:** batch_014
- **Estrato:** E1

**snippet_primary:**

> "In 2013 Etsy changed its policy allowing sellers to hire people to run their businesses and to partner with manufacturers to produce their goods … my business slowed … [cheaper] designs that were once unique to my shop flooded the platform. … to sell on Amazon Handmade you need to qualify by submitting an artisan application. [This process, in my opinion] encourages a more authentic artisanal space by auditing each shop prior to accepting them to ensure the items are genuinely handmade."

| Campo | Sonnet | Fable |
|---|---|---|
| `actor_level` _(A · 🔒 enum)_ | mixed | seller |
| `evidence_role` _(A · 🔒 enum)_ | anecdotal_example | seller_self_claim |
| `local_qualifiers` _(A · 📝 texto libre)_ | designs that were once unique to my shop flooded the platform · Amazon Handmade requires an artisan application audited prior to acceptance | my business slowed · designs that were once unique to my shop flooded the platform · [This process, in my opinion] encourages a more authentic artisanal space |
| `parser_notes` _(A · 📝 texto libre)_ | snippet blends a first-person seller anecdote ("my business slowed") with what appears to be an editorially bracketed opinion insertion ("[This process, in my opinion]"); speaker attribution is ambiguous, hence actor_level mixed | First-person seller quote embedded in the blog (bracketed editorial insertions preserved as they appear). |
| `subject_exact` _(A · 📝 texto libre)_ | 2013 Etsy policy change permitting outsourced production/manufacturing partners, and a reported market-saturation effect, contrasted with Amazon Handmade's artisan application vetting | seller-reported impact of Etsy's 2013 policy allowing hired help and manufacturing partners (slowed business, flood of cheaper designs) versus Amazon Handmade's artisan application vetting |
| `uncertainties` _(A · 🔒 enum)_ | actor_level_unclear · anecdotal_single_source | anecdotal_single_source · source_date_unclear |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008)

**Veredicto:**


---

## Caso 18 — `ER-SP-compass_artifact_wf-63c228bc-9037-4ba4-9569-3f62e8735192_text_markdown-007-SNP-001`

- **Batch de origen:** batch_015
- **Estrato:** E1

**snippet_primary:**

> "I confessed that in three years on Gumroad, I've made a grand total of $139.96. I have a free ebook on ghostwriting that seven people downloaded. A paid guide on pitching that maybe ten people bought, and a free short story set at a Catholic school in Amman, Jordan, that some downloaded."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(A · 📝 texto libre)_ | free ebook on ghostwriting downloaded by seven people · paid guide on pitching bought by maybe ten people · free short story set at a Catholic school in Amman, Jordan | a grand total · that maybe ten people bought |
| `metric_unit` _(A · 📝 texto libre)_ | USD | USD over three years |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | Products explicitly include a free 'ebook' and a paid 'guide'; ebook taken as explicit type; 'Amman, Jordan' is the story's setting, not claim geography. · Additional figures in snippet: 7 downloads of the free ebook; ~10 buyers of the paid guide. |
| `product_type_if_explicit` _(A · 🔒 enum)_ | unknown | ebook |
| `subject_exact` _(A · 📝 texto libre)_ | seller-reported cumulative 3-year Gumroad earnings ($139.96) across a free ebook, a paid guide, and a free short story | seller-reported three-year Gumroad total of $139.96 across a free ebook (7 downloads), a paid pitching guide (~10 buyers) and a free short story |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008)

**Veredicto:**


---

## Caso 19 — `ER-SP-compass_artifact_wf-6b226a5c-1235-4d40-a521-ad9932514aff_text_markdown-003-SNP-001`

- **Batch de origen:** batch_016
- **Estrato:** E1

**snippet_primary:**

> "For subscription products we only support cards, Apple Pay, Google Pay and PayPal at this time."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(B · 📝 texto libre)_ | _(lista vacia)_ | For subscription products · at this time |
| `parser_notes` _(A · 📝 texto libre)_ | wording ("at this time") signals a possibly temporary limitation rather than a permanent restriction | Platform name appears only in source_ref URL; only the payment methods named in text. |
| `platforms` _(A · 📝 texto libre)_ | Lemon Squeezy · Apple Pay · Google Pay · PayPal | Apple Pay · Google Pay · PayPal |
| `subject_exact` _(A · 📝 texto libre)_ | Lemon Squeezy subscription-product checkout payment method limitation (cards, Apple Pay, Google Pay, PayPal only, at this time) | payment methods for subscription products limited to cards, Apple Pay, Google Pay and PayPal at this time |
| `uncertainties` _(A · 🔒 enum)_ | current_vs_historical_ambiguity | source_date_unclear |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008)

**Veredicto:**


---

## Caso 20 — `ER-SP-compass_artifact_wf-7a40dcc5-be9a-4273-a3e8-0d53cab18fb3_text_markdown_normalized-011-SNP-001`

- **Batch de origen:** batch_017
- **Estrato:** E2

**snippet_primary:**

> "Over a year ago, I traveled to the Bologna Children's Book Fair with my freshly printed portfolio, looking for clarity and a new spark. That trip led to a big shift in my art journey. I decided to pause children's book illustration and started focusing on creating art for products and licensing. Now, one year (and 300 Etsy sales!) later, I'm celebrating the joy and balance I've found in making and selling my own artwork."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(B · 📝 texto libre)_ | _(lista vacia)_ | I decided to pause children's book illustration and started focusing on creating art for products and licensing |
| `metric_unit` _(A · 📝 texto libre)_ | sales | sales (first year) |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | 'Bologna Children's Book Fair' is an event in the narrative, not claim geography. |
| `subject_exact` _(A · 📝 texto libre)_ | seller-reported cumulative Etsy sales count after one year selling art products | artist-seller celebrating 300 Etsy sales one year after shifting from children's book illustration to product art and licensing |
| `time_scope_raw` _(A · 📝 texto libre)_ | one year | Over a year ago … Now, one year later |
| `uncertainties` _(A · 🔒 enum)_ | none | anecdotal_single_source |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016)

**Veredicto:**


---

## Caso 21 — `ER-SP-compass_artifact_wf-7b6a9899-eda3-4893-93ba-3553f79cab42_text_markdown-005-SNP-005`

- **Batch de origen:** batch_018
- **Estrato:** E2

**snippet_primary:**

> "Hotmart es una experiencia desagradable para creadores. Aca estoy usando su paygate para mi plataforma de Kajabi, para aceptar pagos en monedas locales en Latinoamérica y se han tardado más de un mes en aprobar mis documentos y darme entrada para poder registrar cuenta bancaria y aceptar pagos en dólares aunque ya estaba vendiendo mi producto digital. Estoy poniendo quejas en el BBB de los EEUU. Es falta de ética el tomarse 5 días cada vez para \"analizar\" documentos legales que ni me piden acá en EEUU. Al poner mis quejas finalmente aprobaron los documentos pero no puedo retirar todo el dinero que he hecho a pesar de que ellos se quedan con un porcentaje. Piénsalo bien antes de usar su plataforma."

| Campo | Sonnet | Fable |
|---|---|---|
| `claim_type` _(A · 🔒 enum)_ | review_statement | anecdotal_report |
| `geography_if_explicit` _(A · 📝 texto libre)_ | Latin America · United States | Latinoamérica · EEUU |
| `local_qualifiers` _(A · 📝 texto libre)_ | already selling my digital product · 5 days each time to analyze documents | para aceptar pagos en monedas locales en Latinoamérica · aunque ya estaba vendiendo mi producto digital · Es falta de ética el tomarse 5 días cada vez para "analizar" documentos legales · Al poner mis quejas finalmente aprobaron los documentos pero no puedo retirar todo el dinero |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | 'BBB de los EEUU' named in text as the complaint venue. |
| `platforms` _(A · 📝 texto libre)_ | Hotmart · Kajabi | Hotmart · Kajabi · BBB |
| `subject_exact` _(A · 📝 texto libre)_ | seller-reported delay in Hotmart document approval for accepting payments via Kajabi paygate integration | US-based creator using Hotmart as paygate for a Kajabi platform reporting over a month of document approval delays for local-currency payments in Latin America, BBB complaints, and remaining withdrawal limits |
| `time_scope_raw` _(A · 📝 texto libre)_ | more than a month | se han tardado más de un mes |
| `uncertainties` _(A · 🔒 enum)_ | none | anecdotal_single_source |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016)

**Veredicto:**


---

## Caso 22 — `ER-SP-compass_artifact_wf-7df7092c-4929-4bbe-b35f-a7efa126b514_text_markdown_normalized-011-SNP-002`

- **Batch de origen:** batch_019
- **Estrato:** E2

**snippet_primary:**

> "envato.com's audience is 56.75% male and 43.25% female. The largest age group of visitors are 25 - 34 year olds."

| Campo | Sonnet | Fable |
|---|---|---|
| `metric_type` _(A · 🔒 enum)_ | unknown | audience demographics |
| `metric_unit` _(A · 📝 texto libre)_ | percent | percent of audience |
| `metric_value_raw` _(A · 📝 texto libre)_ | 56.75% male, 43.25% female; largest age group 25-34 | 56.75% male and 43.25% female |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | metric_type out of enum: observed metric is audience demographic shares; no enum value covers it. · time_scope_normalized_if_safe from page data period '[March 2026]' per criteria G/K1. |
| `subject_exact` _(A · 📝 texto libre)_ | third-party demographic analytics on envato.com visitor audience | envato.com audience demographics: 56.75% male, 43.25% female, largest age group 25-34 (SimilarWeb) |
| `time_scope_normalized_if_safe` _(B · 📝 texto libre)_ | _(null)_ | 2026-03 |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016)

**Veredicto:**


---

## Caso 23 — `ER-SP-compass_artifact_wf-7df7092c-4929-4bbe-b35f-a7efa126b514_text_markdown_normalized-012-SNP-001`

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

## Caso 24 — `ER-SP-compass_artifact_wf-7df7092c-4929-4bbe-b35f-a7efa126b514_text_markdown_normalized-013-SNP-001`

- **Batch de origen:** batch_019
- **Estrato:** E2

**snippet_primary:**

> "We've been using ThemeForest for years and all the products we've purchased have always worked well. However, our last product didn't work and was completely broken. We opened a dispute on PayPal for a refund and were blocked from our account. ThemeForest support requested a pause in the PayPal dispute. And now they claim they won't issue a refund even after reviewing our case and hundreds of negative reviews from the seller? This is an illegal practice since the product arrived completely broken. We no longer trust any Envato service."

| Campo | Sonnet | Fable |
|---|---|---|
| `claim_type` _(A · 🔒 enum)_ | review_statement | anecdotal_report |
| `evidence_role` _(A · 🔒 enum)_ | reported_event | anecdotal_example |
| `local_qualifiers` _(A · 📝 texto libre)_ | completely broken · opened a dispute on PayPal for a refund and were blocked from our account | all the products we've purchased have always worked well · ThemeForest support requested a pause in the PayPal dispute · even after reviewing our case and hundreds of negative reviews from the seller |
| `metric_type` _(A · 🔒 enum)_ | refund_policy | unknown |
| `metric_unit` _(B · 📝 texto libre)_ | reviews | _(null)_ |
| `metric_value_raw` _(B · 📝 texto libre)_ | hundreds of negative reviews from the seller | _(null)_ |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | 'illegal practice' is the reviewer's characterization, preserved in snippet only. |
| `platforms` _(A · 📝 texto libre)_ | ThemeForest | ThemeForest · PayPal · Envato |
| `product_type_if_explicit` _(A · 🔒 enum)_ | design_asset | unknown |
| `subject_exact` _(A · 📝 texto libre)_ | buyer-reported ThemeForest refund denial for a broken product despite a PayPal dispute | long-time ThemeForest buyer reporting a broken product, account blocked after opening a PayPal dispute, support requesting a dispute pause, and refund denied |
| `time_scope_raw` _(B · 📝 texto libre)_ | _(null)_ | We've been using ThemeForest for years |
| `uncertainties` _(A · 🔒 enum)_ | none | anecdotal_single_source |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016)

**Veredicto:**


---

## Caso 25 — `ER-SP-compass_artifact_wf-80dc1a5e-cdb7-4f06-a0fb-62209a2ddd08_text_markdown-001-SNP-002`

- **Batch de origen:** batch_019
- **Estrato:** E2

**snippet_primary:**

> "Some features I want so that this platform can become better — Source — Doesn't tell where the traffic is coming from. Analytics is very basic. No categories. I sell in two niches, and categorizing them becomes difficult. No cross-selling or upselling. Email marketing is a little costly."

| Campo | Sonnet | Fable |
|---|---|---|
| `claim_type` _(A · 🔒 enum)_ | comparative_commentary | anecdotal_report |
| `local_qualifiers` _(A · 📝 texto libre)_ | I sell in two niches, and categorizing them becomes difficult | Some features I want so that this platform can become better · I sell in two niches, and categorizing them becomes difficult · Email marketing is a little costly |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | Which platform the feature list refers to is not determinable from the snippet alone (comparison article covers three). |
| `platforms` _(B · 📝 texto libre)_ | Lemon Squeezy | _(lista vacia)_ |
| `subject_exact` _(A · 📝 texto libre)_ | seller-reported feature gaps in Lemon Squeezy analytics, categorization, and marketing tools | seller-listed platform shortcomings: no traffic-source data, basic analytics, no categories (hindering two-niche selling), no cross/upselling, costly email marketing |
| `uncertainties` _(A · 🔒 enum)_ | none | anecdotal_single_source · source_date_unclear · context_insufficient |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016)

**Veredicto:**


---

## Caso 26 — `ER-SP-compass_artifact_wf-80dc1a5e-cdb7-4f06-a0fb-62209a2ddd08_text_markdown-002-SNP-001`

- **Batch de origen:** batch_020
- **Estrato:** E2

**snippet_primary:**

> "I sell templates for a living and have used several of these providers. The main options are Gumroad - high fees and ugly design, solid system never had issues does most what I need. Lemon Squeezy - it was very popular until being acquired by stripe. Full of serious bugs, bad support. Lovely design, slightly better fees than Gumroad, but many hidden. Would still use over Gumroad just cause the Gumroad checkout design is so bad it loses sales imo. Paddle - haven't used it but I think it's probably as good as Gumroad or Lemon. Polar.sh - the trendy new option, most creators abandoning Lemon Squeezy are moving there. Has lots of innovation in features beyond payments such as selling private GitHub access. All of these platforms are MOR as far as I know, all provide the checkout UI etc. all handle digital asset file delivery. They are perfect for creators selling digital products that want a turn key solution and don't want to do any development work."

| Campo | Sonnet | Fable |
|---|---|---|
| `evidence_role` _(A · 🔒 enum)_ | comparative_commentary | seller_self_claim |
| `local_qualifiers` _(A · 📝 texto libre)_ | all provide checkout UI · all handle digital asset file delivery · haven't used Paddle · most creators abandoning Lemon Squeezy are moving to Polar.sh | I sell templates for a living and have used several of these providers · slightly better fees than Gumroad, but many hidden · haven't used it but I think · most creators abandoning Lemon Squeezy are moving there · as far as I know |
| `metric_type` _(A · 🔒 enum)_ | fee_rate | unknown |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | 'templates' as sold product is generic; not covered by the product enum. · Design judgments ('ugly', 'lovely') are the seller's wording, in snippet only. · source_date approximate ('11 months ago' ≈ May 2025); not normalized. |
| `platforms` _(A · 📝 texto libre)_ | Gumroad · Lemon Squeezy · Paddle · Polar.sh | Gumroad · Lemon Squeezy · Stripe · Paddle · Polar.sh · GitHub |
| `subject_exact` _(A · 📝 texto libre)_ | seller comparison of digital-product Merchant-of-Record checkout providers (Gumroad, Lemon Squeezy, Paddle, Polar.sh) | template seller's survey of MOR checkout providers: Gumroad (high fees, solid), Lemon Squeezy (post-Stripe bugs, hidden fees), Paddle (untried), Polar.sh (trendy destination for Lemon Squeezy leavers) |
| `uncertainties` _(A · 🔒 enum)_ | none | anecdotal_single_source · source_date_unclear |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016)

**Veredicto:**


---

## Caso 27 — `ER-SP-compass_artifact_wf-80dc1a5e-cdb7-4f06-a0fb-62209a2ddd08_text_markdown-004-SNP-004`

- **Batch de origen:** batch_020
- **Estrato:** E2

**snippet_primary:**

> "The downside: you can't start selling immediately. Lemon Squeezy requires account approval, which can take several days to over a week, and their support is very slow. There have also been a lot of recent bugs, like people being unable to check out and customers getting double-charged."

| Campo | Sonnet | Fable |
|---|---|---|
| `claim_type` _(A · 🔒 enum)_ | comparative_commentary | anecdotal_report |
| `local_qualifiers` _(A · 📝 texto libre)_ | support is very slow · people being unable to check out and customers getting double-charged | you can't start selling immediately · which can take several days to over a week · There have also been a lot of recent bugs, like people being unable to check out and customers getting double-charged |
| `metric_type` _(A · 🔒 enum)_ | activation_requirement | unknown |
| `metric_unit` _(B · 📝 texto libre)_ | days | _(null)_ |
| `metric_value_raw` _(B · 📝 texto libre)_ | several days to over a week | _(null)_ |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | Bug reports about other users are secondhand within the seller's account. |
| `subject_exact` _(A · 📝 texto libre)_ | seller-reported Lemon Squeezy account approval delay and recent checkout/double-charge bugs | seller-reported Lemon Squeezy downsides: account approval taking days to over a week, very slow support, and recent bugs including checkout failures and double charges |
| `time_scope_raw` _(B · 📝 texto libre)_ | _(null)_ | recent |
| `uncertainties` _(A · 🔒 enum)_ | none | anecdotal_single_source |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016)

**Veredicto:**


---

## Caso 28 — `ER-SP-compass_artifact_wf-83a235d5-86a0-4c10-9097-e29688c3b834_text_markdown_normalized-016-SNP-001`

- **Batch de origen:** batch_021
- **Estrato:** E2

**snippet_primary:**

> "You will only be charged a listing fee for creating or renewing a listing on Etsy; there is no fee for editing a listing. You will be charged a listing fee whether or not the listed item sells, unless you create a private listing, in which case you will only be charged the listing fee when the private listing is sold. Etsy.com listings expire after four months. Pattern-only listings do not expire. If you list multiple quantities of the same item, the initial listing fee will be $0.20, and the listing will be automatically renewed at $0.20 after each of the items sells."

| Campo | Sonnet | Fable |
|---|---|---|
| `claim_type` _(A · 🔒 enum)_ | policy_statement | pricing_statement |
| `local_qualifiers` _(A · 📝 texto libre)_ | no fee for editing a listing · Pattern-only listings do not expire | there is no fee for editing a listing · whether or not the listed item sells · unless you create a private listing · Etsy.com listings expire after four months. Pattern-only listings do not expire. · the listing will be automatically renewed at $0.20 after each of the items sells |
| `metric_unit` _(A · 📝 texto libre)_ | USD | USD per listing creation/auto-renewal |
| `subject_exact` _(A · 📝 texto libre)_ | Etsy listing fee amount and multi-quantity renewal mechanics | listing fee charged on creation/renewal regardless of sale (private listings charged only on sale), four-month expiry (Pattern listings exempt), $0.20 initial and $0.20 auto-renewal per multi-quantity item sold |
| `time_scope_raw` _(B · 📝 texto libre)_ | Etsy.com listings expire after four months | _(null)_ |
| `uncertainties` _(B · 🔒 enum)_ | none | _(lista vacia)_ |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016)

**Veredicto:**


---

## Caso 29 — `ER-SP-compass_artifact_wf-83a235d5-86a0-4c10-9097-e29688c3b834_text_markdown_normalized-016-SNP-015`

- **Batch de origen:** batch_022
- **Estrato:** E2

**snippet_primary:**

> "Etsy offers sellers in certain locations the ability to purchase shipping labels to fulfill their orders. The cost of the shipping label will depend on the shipping carrier, and the origin, destination, weight, and dimensions of the package."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(B · 📝 texto libre)_ | _(lista vacia)_ | sellers in certain locations · will depend on the shipping carrier, and the origin, destination, weight, and dimensions of the package |
| `subject_exact` _(A · 📝 texto libre)_ | Etsy shipping label cost basis for sellers in eligible locations | shipping label purchase availability for sellers in certain locations, with cost varying by carrier, origin, destination, weight and dimensions |
| `uncertainties` _(B · 🔒 enum)_ | geography_unclear | _(lista vacia)_ |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016)

**Veredicto:**


---

## Caso 30 — `ER-SP-compass_artifact_wf-853a5ee8-c8c0-498f-a255-2c1745e85afc_text_markdown-005-SNP-001`

- **Batch de origen:** batch_022
- **Estrato:** E2

**snippet_primary:**

> "This Envato Elements vs Adobe Stock helped me see that the latter comes with a variety of licensing options. Adobe Stock enables me to choose between Standard, Enhanced, and Extended licenses, which allows me to select the most suitable license for my project. Each license covers different usage rights. For instance, the Standard license has up to $10,000 in legal coverage. At the same time, Envato Elements includes only one license type."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(B · 📝 texto libre)_ | _(lista vacia)_ | the Standard license has up to $10,000 in legal coverage · Envato Elements includes only one license type |
| `metric_unit` _(B · 📝 texto libre)_ | USD legal coverage | _(null)_ |
| `metric_value_raw` _(B · 📝 texto libre)_ | $10,000 | _(null)_ |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | First-person reviewer voice on a review site; treated as commentary source. · source_date approximate ('approximately April 3, 2026'); not normalized. |
| `platforms` _(A · 📝 texto libre)_ | Adobe Stock · Envato Elements | Adobe Stock · Envato |
| `subject_exact` _(A · 📝 texto libre)_ | author comparison of Adobe Stock tiered licensing options versus Envato Elements single license type | licensing comparison: Adobe Stock's Standard/Enhanced/Extended options (Standard with up to $10,000 legal coverage) versus Envato Elements' single license type |
| `uncertainties` _(A · 🔒 enum)_ | none | source_date_unclear |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016)

**Veredicto:**


---

## Caso 31 — `ER-SP-compass_artifact_wf-a06fe5fe-c286-4184-a6a6-fb33112437d3_text_markdown-001-SNP-001`

- **Batch de origen:** batch_023
- **Estrato:** E2

**snippet_primary:**

> "To get started, visit the seller's store. In some cases, you may be taken directly to a product page or checkout if the seller has shared a direct purchase link.\n\nOnce you're on the seller's store, click on the product you're interested in to view more details. You can either add it to your cart and continue browsing or click Buy Now to proceed directly to checkout.\n\nAt checkout, you'll be asked to enter your email address and select a payment method. You can typically pay using PayPal or a debit or credit card, depending on the seller's setup.\n\nOnce your payment is successful, your purchase is complete. [...] Digital products are delivered instantly after purchase via a download page. [...] Yes. After your purchase, you will receive an email receipt that includes your order details, a download or login link, and the seller's contact email. [...] Sellers will receive basic information needed to fulfill your order, such as your email address and, for physical products, your shipping details. They do not have access to your full payment details."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(A · 📝 texto libre)_ | sellers do not have access to full payment details | depending on the seller's setup · Digital products are delivered instantly after purchase via a download page · They do not have access to your full payment details |
| `metric_type` _(A · 🔒 enum)_ | payment_method_availability | payment_method_availability |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | time_scope_normalized_if_safe from source_date_if_available ('Updated March 17, 2026') per criteria G/K1. |
| `platforms` _(A · 📝 texto libre)_ | Payhip | Payhip · PayPal |
| `subject_exact` _(A · 📝 texto libre)_ | Payhip help center description of the buyer checkout and product delivery flow | Payhip buying flow: store/product/checkout navigation, email plus PayPal or card payment per seller setup, instant digital delivery, email receipt, and limited seller access to buyer data |
| `time_scope_normalized_if_safe` _(B · 📝 texto libre)_ | _(null)_ | 2026-03-17 |
| `uncertainties` _(B · 🔒 enum)_ | none | _(lista vacia)_ |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016)

**Veredicto:**


---

## Caso 32 — `ER-SP-compass_artifact_wf-a69c4eb8-8715-4dec-b187-135b1b0fa31a_text_markdown-001-SNP-001`

- **Batch de origen:** batch_025
- **Estrato:** E2

**snippet_primary:**

> "Many reasons, first of all, it's a platform that is well known and used by many other Skyrim modders like me, so it's easier to get a following since many of the players already have an account and are following other creators. My Skyrim mods are and will always be free for everyone, but I needed a place where I have full control of my content, were the rules are clear and I don't have to change my way of making and sharing mods to adapt to a 'mysterious algorithm', and it has the best integration with other platforms."

| Campo | Sonnet | Fable |
|---|---|---|
| `claim_type` _(A · 🔒 enum)_ | explicit_claim | anecdotal_report |
| `local_qualifiers` _(A · 📝 texto libre)_ | already used by many other Skyrim modders · rules are clear · best integration with other platforms | My Skyrim mods are and will always be free for everyone · I don't have to change my way of making and sharing mods to adapt to a 'mysterious algorithm' · it has the best integration with other platforms |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | 'Skyrim' names the game the mods target, not a marketplace; not listed in platforms. · time_scope_normalized_if_safe from source_date_if_available ('May 13, 2025') per criteria G/K1. |
| `subject_exact` _(A · 📝 texto libre)_ | creator's stated reasons for choosing Patreon over other platforms (community familiarity, control, algorithm avoidance) | Skyrim modder's reasons for choosing Patreon: existing modder audience with accounts, content control, clear rules without algorithm adaptation, and integrations |
| `time_scope_normalized_if_safe` _(B · 📝 texto libre)_ | _(null)_ | 2025-05-13 |
| `uncertainties` _(A · 🔒 enum)_ | none | anecdotal_single_source |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016)

**Veredicto:**


---

## Caso 33 — `ER-SP-compass_artifact_wf-a714e31c-2e2c-4735-a50c-9e9535323a2c_text_markdown-010-SNP-004`

- **Batch de origen:** batch_026
- **Estrato:** E2

**snippet_primary:**

> "En el uso diario, Thinkific resulta más intuitivo y ordenado. Todo está donde esperas encontrarlo. Hotmart cubre muchas funciones, pero su navegación puede resultar confusa. En ocasiones incluso mezcla idiomas en la interfaz, lo que no ayuda."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(A · 📝 texto libre)_ | en ocasiones incluso mezcla idiomas en la interfaz | En el uso diario · En ocasiones incluso mezcla idiomas en la interfaz |
| `subject_exact` _(A · 📝 texto libre)_ | blog author's comparison of Hotmart interface usability versus Thinkific | usability comparison: Thinkific more intuitive and ordered versus Hotmart's broader but confusing navigation with occasional mixed-language interface |
| `uncertainties` _(A · 🔒 enum)_ | none | source_date_unclear |

Diferencias de solo orden (C) en este record, no motivan inclusion:
- `platforms`

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016)

**Veredicto:**


---

## Caso 34 — `ER-SP-compass_artifact_wf-a75564bf-b82a-4c6f-b147-9be329dc5e6f_text_markdown_normalized-007-SNP-001`

- **Batch de origen:** batch_027
- **Estrato:** E2

**snippet_primary:**

> [Stated in layout: "Categorias · Sub categorias · Precio · Pais · Otros · Filtros · PRODUCTOS · TIENDAS · COLECCIONES · Done"]

| Campo | Sonnet | Fable |
|---|---|---|
| `metric_type` _(A · 🔒 enum)_ | search_discovery | unknown |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | snippet_primary is layout-derived (bracketed reconstruction), not prose verbatim. · A country ('Pais') facet exists in search; no countries enumerated in the capture. · Platform named only in source_ref URL; platforms left empty per criteria F. |
| `platforms` _(B · 📝 texto libre)_ | Kichink | _(lista vacia)_ |
| `subject_exact` _(A · 📝 texto libre)_ | Kichink category search-results page filter layout elements | Kichink search interface facets for 'ropa': categories, subcategories, price, country and other filters across products, stores and collections |
| `uncertainties` _(A · 🔒 enum)_ | none | source_date_unclear |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016)

**Veredicto:**


---

## Caso 35 — `ER-SP-compass_artifact_wf-bbbe6c81-ce19-4446-ada5-416354340fc4_text_markdown-006-SNP-001`

- **Batch de origen:** batch_033
- **Estrato:** E2

**snippet_primary:**

> "yo debía unas cuotas a black sheet, me contactó un abogado español el cual llegamos a un acuerdo de pagar 7 cuotas y resulta que pagué las 7 cuotas y aún me siguen cobrando a través de la plataforma hotmart, por favor paren de cobrar o me tocará ir a las vías legales, porque ya esto no es un cobro, es un robo cobrar cuotas de más, mi nombre es juan carlos martinez anillo"

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(B · 📝 texto libre)_ | _(lista vacia)_ | pagué las 7 cuotas y aún me siguen cobrando a través de la plataforma hotmart · ya esto no es un cobro, es un robo cobrar cuotas de más |
| `parser_notes` _(A · 📝 texto libre)_ | Speaker describes a third-party debt-collection agreement ('black sheet') plus continued Hotmart billing; exact billing mechanism (subscription vs installment) not specified in snippet. | 'black sheet' is the creditor/vendor named in the anecdote, not a platform/service mention — excluded from platforms (K3). |
| `subject_exact` _(A · 📝 texto libre)_ | buyer-reported continued installment billing on Hotmart after completing a separate collections payment agreement | buyer who settled 7 agreed installments still being charged through the Hotmart platform and threatening legal action |
| `uncertainties` _(A · 🔒 enum)_ | subject_ambiguity | anecdotal_single_source |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032)

**Veredicto:**


---

## Caso 36 — `ER-SP-compass_artifact_wf-bbbe6c81-ce19-4446-ada5-416354340fc4_text_markdown-015-SNP-001`

- **Batch de origen:** batch_033
- **Estrato:** E2

**snippet_primary:**

> "O @cleitonquerobin oferta uma ferramenta de ia e aí você compra e quando chega dentro da compra que seria a ferramenta ele te ensina como comprar outra ferramenta com a mensalidade 1000% do valor que ele te vendeu. É isso tudo dentro do Hotmart. Quero meu dinheiro de volta"

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(A · 📝 texto libre)_ | described markup as '1000% do valor' of the original purchase, per buyer | ele te ensina como comprar outra ferramenta com a mensalidade 1000% do valor que ele te vendeu · É isso tudo dentro do Hotmart |
| `parser_notes` _(A · 📝 texto libre)_ | Buyer names a specific seller handle; complaint concerns seller conduct rather than a platform-level claim. | 'ferramenta de ia' (AI tool) mapped to product_type 'software' — noted as the closest explicit match. |
| `product_type_if_explicit` _(A · 🔒 enum)_ | unknown | software |
| `subject_exact` _(A · 📝 texto libre)_ | buyer-reported misleading advertising by a Hotmart seller upselling a second, far costlier tool subscription | buyer of an AI tool sold inside Hotmart that turned out to teach buying another tool with a monthly fee 1000% of the sold price, requesting money back |
| `time_scope_raw` _(B · 📝 texto libre)_ | January 2026 (refund processed 07/01/2026) | _(null)_ |
| `uncertainties` _(A · 🔒 enum)_ | subject_ambiguity | anecdotal_single_source |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032)

**Veredicto:**


---

## Caso 37 — `ER-SP-compass_artifact_wf-bbbe6c81-ce19-4446-ada5-416354340fc4_text_markdown-019-SNP-007`

- **Batch de origen:** batch_033
- **Estrato:** E2

**snippet_primary:**

> "I didn't know that this site was for some eCourses instead of making money on TikTok. I'm still Waiting on my refund. This isn't what I was signing up for. Now I have to wait to be able to buy groceri..."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(B · 📝 texto libre)_ | _(lista vacia)_ | This isn't what I was signing up for · I'm still Waiting on my refund |
| `parser_notes` _(A · 📝 texto libre)_ | Snippet truncated with '...' mid-word; outcome not available in captured text. | product_type fuera de enum: 'eCourses' named explicitly — observed value recorded verbatim (K5). · Snippet cuts mid-word ('buy groceri...') — flagged snippet_needs_reopen (K8). TikTok named as a service in the text; Hotmart only in source_ref — not listed (criterion F). |
| `platforms` _(A · 📝 texto libre)_ | Hotmart | TikTok |
| `product_type_if_explicit` _(A · 🔒 enum)_ | unknown | eCourses |
| `subject_exact` _(A · 📝 texto libre)_ | buyer-reported confusion over Hotmart course subject matter (expected TikTok monetization, received eCourse) while awaiting refund | buyer who expected a way to make money on TikTok found the site sells eCourses instead and is still waiting on a refund |
| `uncertainties` _(A · 🔒 enum)_ | context_insufficient | anecdotal_single_source · snippet_needs_reopen |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032)

**Veredicto:**


---

## Caso 38 — `ER-SP-compass_artifact_wf-bc6f268c-aeb6-4040-a1a6-8670888bb92f_text_markdown-015-SNP-001`

- **Batch de origen:** batch_034
- **Estrato:** E2

**snippet_primary:**

> "2026's Best Selling Themes on ThemeForest - updated weekly."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(B · 📝 texto libre)_ | _(lista vacia)_ | updated weekly |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | Explicit year in '2026's Best Selling Themes' scoping the list — normalized to year granularity '2026' (criterion G). ThemeForest named in text — listed in platforms. |
| `subject_exact` _(A · 📝 texto libre)_ | ThemeForest Top Sellers page framing statement (updated weekly) | ThemeForest top-sellers page header describing 2026's best selling themes, updated weekly |
| `time_scope_normalized_if_safe` _(B · 📝 texto libre)_ | _(null)_ | 2026 |
| `time_scope_raw` _(A · 📝 texto libre)_ | Accessed April 2026; page undated | 2026's |
| `uncertainties` _(B · 🔒 enum)_ | none | _(lista vacia)_ |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032)

**Veredicto:**


---

## Caso 39 — `ER-SP-compass_artifact_wf-bc6f268c-aeb6-4040-a1a6-8670888bb92f_text_markdown-015-SNP-003`

- **Batch de origen:** batch_034
- **Estrato:** E2

**snippet_primary:**

> [Stated in layout: "Kalles - Clean, Versatile, Responsive Shopify Theme - RTL support by The4 in Fashion $89 (2.2K) 58 Sales Live Preview"]

| Campo | Sonnet | Fable |
|---|---|---|
| `claim_type` _(A · 🔒 enum)_ | statistical_data | pricing_statement |
| `evidence_role` _(A · 🔒 enum)_ | database_fact | observed_platform_state |
| `local_qualifiers` _(A · 📝 texto libre)_ | (2.2K) review count shown alongside | Kalles - Clean, Versatile, Responsive Shopify Theme - RTL support |
| `metric_type` _(A · 🔒 enum)_ | price · sales_count | price |
| `metric_unit` _(A · 📝 texto libre)_ | USD; sales | USD |
| `metric_value_raw` _(A · 📝 texto libre)_ | $89 price; 58 Sales | $89 |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | product_type fuera de enum: item explicitly labeled 'Shopify Theme' — observed label recorded (K5). · Additional metrics (criterion H): (2.2K) rating count and 58 Sales. 'Shopify' appears inside the product-type label — excluded from platforms (K3). Snippet delivered as a layout capture (K10). |
| `platforms` _(B · 📝 texto libre)_ | ThemeForest | _(lista vacia)_ |
| `product_type_if_explicit` _(A · 🔒 enum)_ | software | Shopify theme |
| `subject_exact` _(A · 📝 texto libre)_ | ThemeForest single top-seller listing: Kalles Shopify theme price and recent sales count | Kalles Shopify theme listing on the ThemeForest top-sellers page priced at $89 with rating and sales counts |
| `time_scope_raw` _(B · 📝 texto libre)_ | Accessed April 2026; page undated | _(null)_ |
| `uncertainties` _(B · 🔒 enum)_ | none | _(lista vacia)_ |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032)

**Veredicto:**


---

## Caso 40 — `ER-SP-compass_artifact_wf-c82ebd53-b62c-4f66-b8e2-ae9f5673d0ac_text_markdown_normalized-002-SNP-001`

- **Batch de origen:** batch_034
- **Estrato:** E2

**snippet_primary:**

> "Starting in February 2024, all sales commissions available for withdrawal in any currency, except BRL (real), are automatically transferred without a withdrawal fee once a month to the bank account you registered on our platform."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(A · 📝 texto libre)_ | except BRL (real) | in any currency, except BRL (real) · to the bank account you registered on our platform |
| `metric_type` _(A · 🔒 enum)_ | payout | payout schedule |
| `metric_unit` _(B · 📝 texto libre)_ | _(null)_ | frequency of automatic transfer |
| `metric_value_raw` _(A · 📝 texto libre)_ | once a month, no withdrawal fee | automatically transferred without a withdrawal fee once a month |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | metric_type fuera de enum: transfer cadence — descriptor 'payout schedule' reused (K5). · Explicit date 'February 2024' in snippet — normalized to month granularity '2024-02' (criterion G). Platform named only in source_ref — platforms left empty (criterion F). |
| `platforms` _(B · 📝 texto libre)_ | Hotmart | _(lista vacia)_ |
| `subject_exact` _(A · 📝 texto libre)_ | Hotmart automatic monthly withdrawal transfer without fee for non-BRL commission balances | automatic monthly transfer, without withdrawal fee, of sales commissions available for withdrawal in any currency except BRL, starting February 2024 |
| `uncertainties` _(B · 🔒 enum)_ | none | _(lista vacia)_ |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032)

**Veredicto:**


---

## Caso 41 — `ER-SP-compass_artifact_wf-d45e9141-896e-4a7c-8acd-75d53f883e24_text_markdown-006-SNP-001`

- **Batch de origen:** batch_036
- **Estrato:** E2

**snippet_primary:**

> "The math: on $10,000 monthly subscription revenue, YouTube Memberships pays out $7,000 to the creator while Patreon Pro pays out $8,700 to $9,200. Over a year, the fee difference equals $20,400 in favor of Patreon on $10,000 monthly revenue."

| Campo | Sonnet | Fable |
|---|---|---|
| `claim_type` _(A · 🔒 enum)_ | comparative_commentary | derived_calculation |
| `evidence_role` _(A · 🔒 enum)_ | comparative_commentary | derived_calculation |
| `local_qualifiers` _(B · 📝 texto libre)_ | _(lista vacia)_ | The math: |
| `metric_unit` _(A · 📝 texto libre)_ | USD | USD per month |
| `metric_value_raw` _(A · 📝 texto libre)_ | YouTube Memberships pays $7,000 vs Patreon Pro pays $8,700-$9,200 on $10,000/mo subscription revenue; $20,400/yr difference | YouTube Memberships pays out $7,000 to the creator while Patreon Pro pays out $8,700 to $9,200 (on $10,000 monthly subscription revenue) |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | Additional derived figure (criterion H): 'Over a year, the fee difference equals $20,400 in favor of Patreon on $10,000 monthly revenue'. |
| `platforms` _(A · 📝 texto libre)_ | YouTube Memberships · Patreon | YouTube · Patreon |
| `subject_exact` _(A · 📝 texto libre)_ | third-party guide fee-payout comparison between YouTube Memberships and Patreon with worked annual difference | creator payout comparison on $10,000 monthly subscription revenue: $7,000 via YouTube Memberships versus $8,700 to $9,200 via Patreon Pro, a $20,400 annual difference favoring Patreon |
| `time_scope_normalized_if_safe` _(B · 📝 texto libre)_ | 2026-03-04 | _(null)_ |
| `time_scope_raw` _(B · 📝 texto libre)_ | Accessed April 2026; last updated March 4, 2026 | _(null)_ |
| `uncertainties` _(B · 🔒 enum)_ | none | _(lista vacia)_ |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032)

**Veredicto:**


---

## Caso 42 — `ER-SP-compass_artifact_wf-d45e9141-896e-4a7c-8acd-75d53f883e24_text_markdown-023-SNP-003`

- **Batch de origen:** batch_037
- **Estrato:** E2

**snippet_primary:**

> "No need to set up Stripe or deal with tax paperwork. We manage all of it behind the scenes so you don't have to."

| Campo | Sonnet | Fable |
|---|---|---|
| `claim_type` _(A · 🔒 enum)_ | policy_statement | availability_statement |
| `evidence_role` _(A · 🔒 enum)_ | official_policy | direct_claim |
| `local_qualifiers` _(B · 📝 texto libre)_ | _(lista vacia)_ | We manage all of it behind the scenes so you don't have to |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | 'Stripe' is a payment processor — excluded from platforms per the payment-method convention (K3). Promotional pricing-page copy — author_conflict_of_interest_possible (K4). Platform named only in source_ref — platforms left empty (criterion F). |
| `platforms` _(B · 📝 texto libre)_ | Patreon | _(lista vacia)_ |
| `subject_exact` _(A · 📝 texto libre)_ | Patreon handling of payment-gateway setup and tax paperwork on behalf of creators | no need for creators to set up Stripe or handle tax paperwork, managed by the platform behind the scenes |
| `time_scope_raw` _(B · 📝 texto libre)_ | Accessed April 2026; page undated | _(null)_ |
| `uncertainties` _(A · 🔒 enum)_ | none | author_conflict_of_interest_possible |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032)

**Veredicto:**


---

## Caso 43 — `ER-SP-compass_artifact_wf-d5fe5a2c-6077-4bcd-ad62-c4fe3960e23a_text_markdown-002-SNP-001`

- **Batch de origen:** batch_037
- **Estrato:** E2

**snippet_primary:**

> "Hotmart Developers is the website where you check out Hotmart's APIs. This data is ideal for Creators who have their own team of developers and want to create an even more personalized analysis with their own systems."

| Campo | Sonnet | Fable |
|---|---|---|
| `claim_type` _(A · 🔒 enum)_ | explicit_claim | availability_statement |
| `local_qualifiers` _(B · 📝 texto libre)_ | _(lista vacia)_ | ideal for Creators who have their own team of developers |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | Help-center doc assigned official_policy (K6). |
| `subject_exact` _(A · 📝 texto libre)_ | Hotmart Developers API availability for creators with their own development teams | Hotmart Developers website exposing Hotmart's APIs for creators with developer teams to build personalized analyses |
| `time_scope_raw` _(B · 📝 texto libre)_ | Accessed April 2026; page undated | _(null)_ |
| `uncertainties` _(B · 🔒 enum)_ | none | _(lista vacia)_ |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032)

**Veredicto:**


---

## Caso 44 — `ER-SP-compass_artifact_wf-de144e73-98a7-403c-a882-9327b9dbadd2_text_markdown-009-SNP-001`

- **Batch de origen:** batch_038
- **Estrato:** E2

**snippet_primary:**

> "Sale Samurai gives you the insights and analytics needed to skyrocket your Etsy SEO. Keyword research with real search volume data from Etsy."

| Campo | Sonnet | Fable |
|---|---|---|
| `claim_type` _(A · 🔒 enum)_ | explicit_claim | availability_statement |
| `evidence_role` _(A · 🔒 enum)_ | comparative_commentary | direct_claim |
| `local_qualifiers` _(B · 📝 texto libre)_ | _(lista vacia)_ | needed to skyrocket your Etsy SEO · real search volume data from Etsy |
| `metric_type` _(A · 🔒 enum)_ | search_discovery | unknown |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | First-person promotional vendor voice — author_conflict_of_interest_possible (K4). |
| `subject_exact` _(A · 📝 texto libre)_ | third-party Etsy-SEO tool vendor's self-promotional description of keyword-research analytics using real Etsy search-volume data | Sale Samurai offering insights, analytics, and keyword research with real search volume data from Etsy |
| `time_scope_raw` _(B · 📝 texto libre)_ | Accessed April 2026; page undated | _(null)_ |
| `uncertainties` _(A · 🔒 enum)_ | none | author_conflict_of_interest_possible |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032)

**Veredicto:**


---

## Caso 45 — `ER-SP-compass_artifact_wf-de144e73-98a7-403c-a882-9327b9dbadd2_text_markdown-011-SNP-002`

- **Batch de origen:** batch_038
- **Estrato:** E2

**snippet_primary:**

> "Custom Name Necklace, 18K Gold Plated Name Necklace, Personalized Name Necklace, Birthday Gift for Her, Mother's Day Gift, Gift for Mom — (55,428 reviews), Star Seller — Sale Price $14.05, Original Price $28.11 (50% off), Shop: AnyaShopStudio, Ad, FREE shipping"

| Campo | Sonnet | Fable |
|---|---|---|
| `claim_type` _(A · 🔒 enum)_ | statistical_data | pricing_statement |
| `evidence_role` _(A · 🔒 enum)_ | database_fact | observed_platform_state |
| `local_qualifiers` _(A · 📝 texto libre)_ | Star Seller badge · Ad · FREE shipping · Shop: AnyaShopStudio | Star Seller · Ad · FREE shipping |
| `metric_type` _(A · 🔒 enum)_ | price · review_count | price |
| `metric_unit` _(A · 📝 texto libre)_ | USD; reviews | USD |
| `metric_value_raw` _(A · 📝 texto libre)_ | Sale Price $14.05, Original Price $28.11 (50% off); 55,428 reviews | Sale Price $14.05, Original Price $28.11 (50% off) |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | product_type fuera de enum: physical product 'Necklace' named explicitly — observed value recorded (K5). · Additional metric (criterion H): '(55,428 reviews)'. Platform named only in source_ref — platforms left empty (criterion F). |
| `platforms` _(B · 📝 texto libre)_ | Etsy | _(lista vacia)_ |
| `product_type_if_explicit` _(A · 🔒 enum)_ | unknown | necklace |
| `subject_exact` _(A · 📝 texto libre)_ | Etsy jewelry-category search-results single listing: custom name necklace price, discount, and review count | custom name necklace listing at sale price $14.05 from original $28.11 (50% off), with 55,428 reviews, Star Seller status, ad placement, and free shipping |
| `time_scope_raw` _(B · 📝 texto libre)_ | Accessed April 2026; listing undated | _(null)_ |
| `uncertainties` _(B · 🔒 enum)_ | none | _(lista vacia)_ |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032)

**Veredicto:**


---

## Caso 46 — `ER-SP-compass_artifact_wf-e33b0dbb-828e-4221-b8c5-7bf05bddcdba_text_markdown_normalized-002-SNP-001`

- **Batch de origen:** batch_038
- **Estrato:** E2

**snippet_primary:**

> > "On the 1st Jan 2015, the European Union introduced the digital EU VAT law. This law requires all sales of digital items (such as ebooks) in the EU to pay VAT based on the location of the customer."
> 
> > "In order to remove all of the administrative burden from our sellers we will take care of all EU VAT issues for your customers based in the European Union."
> 
> > "The UK has left the EU but they have a similar law that also requires VAT be charged on digital products if your customer is based in the UK - regardless of where the seller is from."
> 
> > "By default, we automatically handle digital UK & EU VAT for you. If you'd rather handle the process yourself you can uncheck the first two checkboxes."
> 
> > "Choosing to include taxes within the product price means your customers won't see a difference in the price they need to pay. However it means your profits will be impacted to account for sales tax - instead of being passed on to customers."
> 
> > "If your customer is not based in the EU or UK, then this digital tax will not be applied to their transaction. They will be charged at the regular price you set for the product."

| Campo | Sonnet | Fable |
|---|---|---|
| `geography_if_explicit` _(A · 📝 texto libre)_ | European Union; United Kingdom | EU and UK |
| `local_qualifiers` _(B · 📝 texto libre)_ | _(lista vacia)_ | pay VAT based on the location of the customer · The UK has left the EU but they have a similar law - regardless of where the seller is from · Choosing to include taxes within the product price means your customers won't see a difference in the price they need to pay. However it means your profits will be impacted · If your customer is not based in the EU or UK, then this digital tax will not be applied to their transaction |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | Policy state claim with explicit last-updated date February 21, 2026 and null raw — normalized 2026-02-21 (K1). '1st Jan 2015' dates the law's introduction, not the claim's scope. geography verbatim from 'in the EU' / 'based in the UK'. Platform named only in source_ref — platforms left empty (criterion F). |
| `platforms` _(B · 📝 texto libre)_ | Payhip | _(lista vacia)_ |
| `subject_exact` _(A · 📝 texto libre)_ | Payhip EU/UK digital VAT compliance handling on behalf of sellers | automatic handling of digital UK and EU VAT by default, charged by customer location under the 2015 EU digital VAT law and the similar UK law, with seller options to self-handle or include tax in price |
| `time_scope_raw` _(B · 📝 texto libre)_ | Last updated February 21, 2026 | _(null)_ |
| `uncertainties` _(B · 🔒 enum)_ | none | _(lista vacia)_ |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032)

**Veredicto:**


---

## Caso 47 — `ER-SP-compass_artifact_wf-e33b0dbb-828e-4221-b8c5-7bf05bddcdba_text_markdown_normalized-005-SNP-003`

- **Batch de origen:** batch_039
- **Estrato:** E2

**snippet_primary:**

> > "If I refund a payment, do the fees get refunded? Both Payhip fees and PayPal/Stripe fees will not be returned when you refund a transaction."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(B · 📝 texto libre)_ | _(lista vacia)_ | Both Payhip fees and PayPal/Stripe fees will not be returned when you refund a transaction |
| `metric_type` _(A · 🔒 enum)_ | fee_rate | unknown |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | Policy state claim with explicit last-updated April 19, 2024 and null raw — normalized (K1). |
| `platforms` _(A · 📝 texto libre)_ | Payhip · PayPal · Stripe | Payhip |
| `subject_exact` _(A · 📝 texto libre)_ | Payhip non-refundability of platform and processor fees on refunded transactions | neither Payhip fees nor PayPal/Stripe fees returned when a transaction is refunded |
| `time_scope_raw` _(B · 📝 texto libre)_ | Last updated April 19, 2024 | _(null)_ |
| `uncertainties` _(B · 🔒 enum)_ | none | _(lista vacia)_ |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032)

**Veredicto:**


---

## Caso 48 — `ER-SP-compass_artifact_wf-e33b0dbb-828e-4221-b8c5-7bf05bddcdba_text_markdown_normalized-012-SNP-001`

- **Batch de origen:** batch_039
- **Estrato:** E2

**snippet_primary:**

> > "The standard Mollie fee for online credit card transactions ranges from 1.80% + €0.25 to 2.90% + €0.25 per transaction for European Economic Area consumer credit cards from Mastercard and Visa. Rates vary by payment methods, please check Mollie's pricing page for the latest updates. Note that these fees are collected by Mollie and do not go to Payhip."

| Campo | Sonnet | Fable |
|---|---|---|
| `geography_if_explicit` _(B · 📝 texto libre)_ | _(null)_ | European Economic Area |
| `local_qualifiers` _(A · 📝 texto libre)_ | fees collected by Mollie, not Payhip | Rates vary by payment methods, please check Mollie's pricing page for the latest updates · these fees are collected by Mollie and do not go to Payhip |
| `metric_unit` _(A · 📝 texto libre)_ | percent + EUR flat | mixed: % + EUR per transaction |
| `metric_value_raw` _(A · 📝 texto libre)_ | 1.80% + EUR0.25 to 2.90% + EUR0.25 | ranges from 1.80% + €0.25 to 2.90% + €0.25 per transaction |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | Pricing state claim with explicit last-updated February 22, 2026 and null raw — normalized (K1). geography verbatim 'for European Economic Area consumer credit cards'. 'Mollie', 'Mastercard', 'Visa' are payment services — excluded from platforms (K3). Mixed units declared. |
| `platforms` _(A · 📝 texto libre)_ | Payhip · Mollie | Payhip |
| `subject_exact` _(A · 📝 texto libre)_ | Payhip-documented Mollie payment-gateway transaction fee range | standard Mollie fee for online credit card transactions ranging from 1.80% + €0.25 to 2.90% + €0.25 per transaction for EEA Mastercard and Visa consumer cards, collected by Mollie not Payhip |
| `time_scope_raw` _(B · 📝 texto libre)_ | Last updated February 22, 2026 | _(null)_ |
| `uncertainties` _(B · 🔒 enum)_ | none | _(lista vacia)_ |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032)

**Veredicto:**


---

## Caso 49 — `ER-SP-compass_artifact_wf-e33b0dbb-828e-4221-b8c5-7bf05bddcdba_text_markdown_normalized-015-SNP-002`

- **Batch de origen:** batch_039
- **Estrato:** E2

**snippet_primary:**

> > "Paystack is supported in Côte d'Ivoire (Ivory Coast), Ghana, Kenya, Nigeria, and South Africa."

| Campo | Sonnet | Fable |
|---|---|---|
| `geography_if_explicit` _(A · 📝 texto libre)_ | Cote d'Ivoire (Ivory Coast) · Ghana · Kenya · Nigeria · South Africa | Côte d'Ivoire (Ivory Coast), Ghana, Kenya, Nigeria, and South Africa |
| `metric_unit` _(B · 📝 texto libre)_ | _(null)_ | countries |
| `metric_value_raw` _(B · 📝 texto libre)_ | _(null)_ | supported in Côte d'Ivoire (Ivory Coast), Ghana, Kenya, Nigeria, and South Africa |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | geography verbatim country list. Page undated — not normalized (K1). 'Paystack' is a payment service — excluded from platforms (K3). Platform named only in source_ref — platforms left empty (criterion F). |
| `platforms` _(B · 📝 texto libre)_ | Payhip · Paystack | _(lista vacia)_ |
| `subject_exact` _(A · 📝 texto libre)_ | Payhip-documented Paystack gateway country coverage | Paystack support in five listed African countries |
| `time_scope_raw` _(B · 📝 texto libre)_ | Undated | _(null)_ |
| `uncertainties` _(B · 🔒 enum)_ | none | _(lista vacia)_ |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032)

**Veredicto:**


---

## Caso 50 — `ER-SP-compass_artifact_wf-e33b0dbb-828e-4221-b8c5-7bf05bddcdba_text_markdown_normalized-022-SNP-002`

- **Batch de origen:** batch_040
- **Estrato:** E2

**snippet_primary:**

> > "PayTabs supports countries in the Middle East and North Africa (MENA) region, including Egypt, Iraq, Jordan, Kuwait, Oman, Saudi Arabia, and United Arab Emirates."

| Campo | Sonnet | Fable |
|---|---|---|
| `geography_if_explicit` _(A · 📝 texto libre)_ | Egypt · Iraq · Jordan · Kuwait · Oman · Saudi Arabia · United Arab Emirates | Middle East and North Africa (MENA) region, including Egypt, Iraq, Jordan, Kuwait, Oman, Saudi Arabia, and United Arab Emirates |
| `metric_unit` _(B · 📝 texto libre)_ | _(null)_ | countries |
| `metric_value_raw` _(B · 📝 texto libre)_ | _(null)_ | supports countries in the Middle East and North Africa (MENA) region |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | Availability state claim with explicit last-updated February 21, 2026 and null raw — normalized (K1). geography verbatim. 'PayTabs' is a payment service — excluded (K3). Platform named only in source_ref — platforms left empty (criterion F). |
| `platforms` _(B · 📝 texto libre)_ | Payhip · PayTabs | _(lista vacia)_ |
| `subject_exact` _(A · 📝 texto libre)_ | Payhip-documented PayTabs gateway MENA-region country coverage | PayTabs support in MENA-region countries including Egypt, Iraq, Jordan, Kuwait, Oman, Saudi Arabia, and United Arab Emirates |
| `time_scope_raw` _(B · 📝 texto libre)_ | Last updated February 21, 2026 | _(null)_ |
| `uncertainties` _(B · 🔒 enum)_ | none | _(lista vacia)_ |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032)

**Veredicto:**


---

## Caso 51 — `ER-SP-compass_artifact_wf-e33b0dbb-828e-4221-b8c5-7bf05bddcdba_text_markdown_normalized-029-SNP-001`

- **Batch de origen:** batch_040
- **Estrato:** E2

**snippet_primary:**

> > **Free Forever** — $0 /mo — +5% transaction fee — All features — Unlimited products — Unlimited revenue
> 
> > **Plus** — $29 /mo — +2% transaction fee — All features — Unlimited products — Unlimited revenue
> 
> > **Pro** — $99 /mo — No transaction fee — All features — Unlimited products — Unlimited revenue

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(B · 📝 texto libre)_ | _(lista vacia)_ | All features — Unlimited products — Unlimited revenue (each tier) |
| `metric_unit` _(A · 📝 texto libre)_ | USD/mo + percent | mixed: USD per month + % transaction fee |
| `metric_value_raw` _(A · 📝 texto libre)_ | Free Forever ($0/mo): +5% transaction fee; Plus ($29/mo): +2% transaction fee; Pro ($99/mo): no transaction fee | Free Forever — $0 /mo — +5% transaction fee \| Plus — $29 /mo — +2% transaction fee \| Pro — $99 /mo — No transaction fee |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | Tier structure preserved verbatim in listing order; mixed units declared. Page undated — not normalized (K1). Platform named only in source_ref — platforms left empty (criterion F). |
| `platforms` _(B · 📝 texto libre)_ | Payhip | _(lista vacia)_ |
| `subject_exact` _(A · 📝 texto libre)_ | Payhip pricing-page subscription-tier transaction fee schedule (Free/Plus/Pro) | three plan tiers with identical features and limits: Free Forever at $0/mo + 5% transaction fee, Plus at $29/mo + 2%, Pro at $99/mo with no transaction fee |
| `time_scope_raw` _(B · 📝 texto libre)_ | Undated | _(null)_ |
| `uncertainties` _(B · 🔒 enum)_ | none | _(lista vacia)_ |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032)

**Veredicto:**


---

## Caso 52 — `ER-SP-compass_artifact_wf-e33b0dbb-828e-4221-b8c5-7bf05bddcdba_text_markdown_normalized-030-SNP-001`

- **Batch de origen:** batch_041
- **Estrato:** E3

**snippet_primary:**

> > "Payment is handled separately, and securely, through the payment processor you have selected during checkout ('Payment Processor'). Your payment card details are never collected by Us."
> 
> > "We will hold details relating to any transaction you make, such as your name, e-mail address, IP address, billing address, location data for 10 years from the date of the transaction for EU VAT purposes in respect of digital products."
> 
> > "All information We hold about you is stored on secure servers in the EU."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(A · 📝 texto libre)_ | for EU VAT purposes in respect of digital products · payment card details never collected by Payhip | Your payment card details are never collected by Us · for EU VAT purposes in respect of digital products · All information We hold about you is stored on secure servers in the EU |
| `metric_type` _(A · 🔒 enum)_ | data_retention_duration | data retention period |
| `metric_value_raw` _(A · 📝 texto libre)_ | 10 years | for 10 years from the date of the transaction |
| `parser_notes` _(A · 📝 texto libre)_ | metric_type out_of_enum: data retention duration has no matching controlled-vocabulary value | metric_type fuera de enum: personal-data retention window — descriptor 'data retention period' (K5). · geography verbatim 'in the EU'. Page undated — not normalized (K1). Platform named only in source_ref — platforms left empty (criterion F). |
| `platforms` _(B · 📝 texto libre)_ | Payhip | _(lista vacia)_ |
| `subject_exact` _(A · 📝 texto libre)_ | Payhip transaction data retention period for EU VAT purposes | payments handled by the selected processor with no card details collected, transaction data retained 10 years for EU VAT purposes, and all data stored on secure servers in the EU |
| `time_scope_raw` _(B · 📝 texto libre)_ | from the date of the transaction | _(null)_ |
| `uncertainties` _(B · 🔒 enum)_ | none | _(lista vacia)_ |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016), S6 (desde batch_040), S7 (desde batch_040), S8 (desde batch_040)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032), K13 (desde batch_040), K14 (desde batch_040)

**Veredicto:**


---

## Caso 53 — `ER-SP-compass_artifact_wf-e68dd732-3da5-44dc-ac62-efdb81f1bdc1_text_markdown-002-SNP-001`

- **Batch de origen:** batch_041
- **Estrato:** E3

**snippet_primary:**

> [Stated in layout: "10% + $0.50 Per transaction for all sales through your profile or direct links to your customers."]

| Campo | Sonnet | Fable |
|---|---|---|
| `metric_unit` _(A · 📝 texto libre)_ | percent + USD flat | mixed: % + USD per transaction |
| `metric_value_raw` _(A · 📝 texto libre)_ | 10% + $0.50 | 10% + $0.50 Per transaction |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | Snippet delivered as a layout capture (K10). Page undated ('Accessed April 2026') — not normalized (K1). Mixed units declared. Platform named only in source_ref — platforms left empty (criterion F). |
| `platforms` _(B · 📝 texto libre)_ | Gumroad | _(lista vacia)_ |
| `subject_exact` _(A · 📝 texto libre)_ | Gumroad direct-sale (profile/direct link) per-transaction fee rate | fee of 10% + $0.50 per transaction for sales through the seller's profile or direct links |
| `time_scope_raw` _(B · 📝 texto libre)_ | Accessed April 2026; page undated | _(null)_ |
| `uncertainties` _(B · 🔒 enum)_ | source_date_unclear | _(lista vacia)_ |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016), S6 (desde batch_040), S7 (desde batch_040), S8 (desde batch_040)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032), K13 (desde batch_040), K14 (desde batch_040)

**Veredicto:**


---

## Caso 54 — `ER-SP-compass_artifact_wf-e68dd732-3da5-44dc-ac62-efdb81f1bdc1_text_markdown-002-SNP-002`

- **Batch de origen:** batch_041
- **Estrato:** E3

**snippet_primary:**

> [Stated in layout: "30% Per transaction when new customers find and buy from you through our discover marketplace."]

| Campo | Sonnet | Fable |
|---|---|---|
| `metric_unit` _(A · 📝 texto libre)_ | percent | % per transaction |
| `metric_value_raw` _(A · 📝 texto libre)_ | 30% | 30% Per transaction |
| `parser_notes` _(A · 📝 texto libre)_ | Discover fee (30%) is distinct from direct/profile fee (10%+$0.50); not collapsed into one figure | Snippet delivered as a layout capture (K10). Page undated — not normalized (K1). Platform named only in source_ref — platforms left empty (criterion F). |
| `platforms` _(B · 📝 texto libre)_ | Gumroad | _(lista vacia)_ |
| `subject_exact` _(A · 📝 texto libre)_ | Gumroad Discover marketplace per-transaction fee rate | fee of 30% per transaction when new customers find and buy through the discover marketplace |
| `time_scope_raw` _(B · 📝 texto libre)_ | Accessed April 2026; page undated | _(null)_ |
| `uncertainties` _(B · 🔒 enum)_ | source_date_unclear | _(lista vacia)_ |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016), S6 (desde batch_040), S7 (desde batch_040), S8 (desde batch_040)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032), K13 (desde batch_040), K14 (desde batch_040)

**Veredicto:**


---

## Caso 55 — `ER-SP-compass_artifact_wf-f51aad3f-6ad1-4ebb-9cb3-cdab05234caa_text_markdown-009-SNP-001`

- **Batch de origen:** batch_043
- **Estrato:** E3

**snippet_primary:**

> "While Lemon Squeezy caters to solo creators and indie hackers, Polar is built for developers who need robust APIs, advanced features, and the ability to scale to enterprise-level requirements." and "At $50,000 monthly revenue, Polar saves you $500/month. At $100,000, you save $1,000/month compared to Lemon Squeezy."

| Campo | Sonnet | Fable |
|---|---|---|
| `actor_level` _(A · 🔒 enum)_ | third_party | platform |
| `local_qualifiers` _(B · 📝 texto libre)_ | _(lista vacia)_ | Polar is built for developers who need robust APIs, advanced features, and the ability to scale to enterprise-level requirements |
| `metric_type` _(A · 🔒 enum)_ | fee_rate | fee savings comparison |
| `metric_unit` _(A · 📝 texto libre)_ | USD | USD per month saved |
| `metric_value_raw` _(A · 📝 texto libre)_ | $500/month saved at $50,000; $1,000/month saved at $100,000 | At $50,000 monthly revenue, Polar saves you $500/month. At $100,000, you save $1,000/month compared to Lemon Squeezy |
| `parser_notes` _(A · 📝 texto libre)_ | Comparison page is published by Polar itself about a competitor (Lemon Squeezy); potential vendor bias | metric_type fuera de enum: claimed monthly savings versus competitor — descriptor 'fee savings comparison' (K5). · Comparison page on the competitor's own site (polar.sh) — actor 'platform' by who speaks (K7/K11) and author_conflict_of_interest_possible (K4). Page not dated — not normalized (K1). |
| `subject_exact` _(A · 📝 texto libre)_ | Polar vs Lemon Squeezy monthly savings at $50,000 and $100,000 revenue tiers (Polar-authored comparison) | Polar positioned for developers needing robust APIs and enterprise scale versus Lemon Squeezy for solo creators, with claimed savings of $500/month at $50,000 and $1,000/month at $100,000 revenue |
| `time_scope_raw` _(B · 📝 texto libre)_ | not dated (current as of April 2026) | _(null)_ |

Diferencias de solo orden (C) en este record, no motivan inclusion:
- `platforms`

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016), S6 (desde batch_040), S7 (desde batch_040), S8 (desde batch_040)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032), K13 (desde batch_040), K14 (desde batch_040)

**Veredicto:**


---

## Caso 56 — `ER-SP-compass_artifact_wf-f51aad3f-6ad1-4ebb-9cb3-cdab05234caa_text_markdown-014-SNP-001`

- **Batch de origen:** batch_043
- **Estrato:** E3

**snippet_primary:**

> "Right now, to be honest, our MVP is on par with Gumroad in terms of functionality. Our user experience diversifies us, but the true value in what Lemon Squeezy can do for you beyond what already exists is yet to come."

| Campo | Sonnet | Fable |
|---|---|---|
| `claim_type` _(A · 🔒 enum)_ | explicit_claim | comparative_commentary |
| `evidence_role` _(A · 🔒 enum)_ | seller_self_claim | direct_claim |
| `local_qualifiers` _(A · 📝 texto libre)_ | our MVP is on par with Gumroad in terms of functionality | Our user experience diversifies us · the true value in what Lemon Squeezy can do for you beyond what already exists is yet to come |
| `parser_notes` _(A · 📝 texto libre)_ | Forum post is from Lemon Squeezy's own founder, an early-stage self-assessment likely outdated relative to 2026 | First-person platform-founder voice in the forum post ('our MVP') — actor 'platform' by who speaks (K7) and author_conflict_of_interest_possible (K4). · time_scope_raw 'Right now' is relative — normalized left null (criterion G). Source date '~2021' is approximate — source_date_unclear (K2). |
| `subject_exact` _(A · 📝 texto libre)_ | Lemon Squeezy founder's self-assessment of MVP parity with Gumroad functionality | founder's statement that the Lemon Squeezy MVP is on par with Gumroad in functionality, differentiated by user experience, with further value yet to come |
| `time_scope_raw` _(A · 📝 texto libre)_ | ~2021 | Right now |
| `uncertainties` _(A · 🔒 enum)_ | source_date_unclear · current_vs_historical_ambiguity | author_conflict_of_interest_possible · source_date_unclear |

Diferencias de solo orden (C) en este record, no motivan inclusion:
- `platforms`

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016), S6 (desde batch_040), S7 (desde batch_040), S8 (desde batch_040)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032), K13 (desde batch_040), K14 (desde batch_040)

**Veredicto:**


---

## Caso 57 — `ER-SP-compass_artifact_wf-f65accb1-75e2-4cb1-be7d-0d01a8fabf93_text_markdown-005-SNP-001`

- **Batch de origen:** batch_044
- **Estrato:** E3

**snippet_primary:**

> "If the retail price of a Product is listed in a currency other than United States Dollars (USD), Gumroad will calculate a USD price based upon an exchange rate determined by Gumroad. Gumroad uses exchange rates obtained from http://openexchangerates.org/api. Gumroad cannot and does not guarantee that the exchange rate displayed reflects the most up to date rate due to the fluctuating nature of exchange rates. Accordingly, Gumroad recommends that you confirm current rates before engaging in any transactions on the Platform. Regardless of listed currency, all transactions through the Services will settle in USD."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(A · 📝 texto libre)_ | Gumroad cannot and does not guarantee that the exchange rate displayed reflects the most up to date rate | Gumroad cannot and does not guarantee that the exchange rate displayed reflects the most up to date rate · Gumroad recommends that you confirm current rates before engaging in any transactions · Regardless of listed currency, all transactions through the Services will settle in USD |
| `metric_unit` _(B · 📝 texto libre)_ | USD | _(null)_ |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | Policy state claim with explicit Effective Date January 1, 2025 and null raw — normalized (K1). 'openexchangerates.org' is a data source named in the policy, not a marketplace platform — excluded (K3). |
| `subject_exact` _(A · 📝 texto libre)_ | Gumroad exchange-rate determination method and USD settlement guarantee | USD price calculation for non-USD listings using exchange rates from openexchangerates.org without guarantee of currency, with all transactions settling in USD |
| `time_scope_raw` _(B · 📝 texto libre)_ | Effective January 1, 2025; last updated December 10, 2024 | _(null)_ |
| `uncertainties` _(B · 🔒 enum)_ | none | _(lista vacia)_ |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016), S6 (desde batch_040), S7 (desde batch_040), S8 (desde batch_040)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032), K13 (desde batch_040), K14 (desde batch_040)

**Veredicto:**


---

## Caso 58 — `ER-SP-compass_artifact_wf-f678b42a-32e6-4c77-b539-89b40c493fbb_text_markdown-010-SNP-003`

- **Batch de origen:** batch_045
- **Estrato:** E3

**snippet_primary:**

> "Debido a la nueva normativa del Banco Central de la República Argentina (BCRA), que amplió el plazo para las remesas al exterior y afectó la liquidación de operaciones, se estandarizó la aplicación de una tarifa en los pagos con conversión de compra con pesos argentinos (ARS) para ofertas en dólares estadounidenses (USD), o conversiones de comisiones en dólares estadounidenses (USD) para productos ofertados en pesos argentinos (ARS)."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(B · 📝 texto libre)_ | _(lista vacia)_ | Debido a la nueva normativa del Banco Central de la República Argentina (BCRA), que amplió el plazo para las remesas al exterior · pagos con conversión de compra con pesos argentinos (ARS) para ofertas en dólares estadounidenses (USD), o conversiones de comisiones en dólares estadounidenses (USD) para productos ofertados en pesos argentinos (ARS) |
| `metric_type` _(A · 🔒 enum)_ | fee_rate | unknown |
| `parser_notes` _(B · 📝 texto libre)_ | _(lista vacia)_ | Fee mentioned without a rate — metric_type left 'unknown'. geography from the BCRA/ARS references naming Argentina. Platform named only in source_ref — platforms left empty (criterion F). |
| `platforms` _(B · 📝 texto libre)_ | Hotmart | _(lista vacia)_ |
| `subject_exact` _(A · 📝 texto libre)_ | Hotmart currency-conversion fee for ARS-USD commission conversions tied to Argentina BCRA regulation | standardized fee applied to ARS/USD conversion payments and commissions due to a BCRA regulation extending remittance timelines and affecting settlement |
| `time_scope_normalized_if_safe` _(B · 📝 texto libre)_ | 2026-04 | _(null)_ |
| `time_scope_raw` _(B · 📝 texto libre)_ | as of April 2026 | _(null)_ |
| `uncertainties` _(B · 🔒 enum)_ | none | _(lista vacia)_ |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016), S6 (desde batch_040), S7 (desde batch_040), S8 (desde batch_040)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032), K13 (desde batch_040), K14 (desde batch_040)

**Veredicto:**


---

## Caso 59 — `ER-SP-compass_artifact_wf-fbf25436-287d-411c-be97-ee28c335a4a4_text_markdown-004-SNP-003`

- **Batch de origen:** batch_046
- **Estrato:** E3

**snippet_primary:**

> "This is the worst online purchasing experience I have ever had. I paid for my purchase, post payment I was given the option to send the book to kindle - this didn't work. I set up an account and to..."

| Campo | Sonnet | Fable |
|---|---|---|
| `claim_type` _(A · 🔒 enum)_ | review_statement | anecdotal_report |
| `local_qualifiers` _(B · 📝 texto libre)_ | _(lista vacia)_ | This is the worst online purchasing experience I have ever had · I was given the option to send the book to kindle - this didn't work |
| `parser_notes` _(A · 📝 texto libre)_ | Snippet truncated with '...' | Snippet cuts mid-sentence ('I set up an account and to...') — flagged snippet_needs_reopen (K8). 'kindle' named as the delivery service — included (K3). Gumroad named only in source_ref — not listed (criterion F). Digital book purchase — product_type 'ebook'. |
| `platforms` _(A · 📝 texto libre)_ | Gumroad | Kindle |
| `subject_exact` _(A · 📝 texto libre)_ | Trustpilot buyer complaint about broken Kindle-send feature for a Gumroad ebook purchase | buyer whose post-payment send-to-Kindle option did not work, describing it as their worst online purchasing experience |
| `time_scope_normalized_if_safe` _(B · 📝 texto libre)_ | 2026-04-01 | _(null)_ |
| `time_scope_raw` _(B · 📝 texto libre)_ | April 1, 2026 | _(null)_ |
| `uncertainties` _(A · 🔒 enum)_ | context_insufficient | anecdotal_single_source · snippet_needs_reopen |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016), S6 (desde batch_040), S7 (desde batch_040), S8 (desde batch_040)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032), K13 (desde batch_040), K14 (desde batch_040)

**Veredicto:**


---

## Caso 60 — `ER-SP-compass_artifact_wf-fbf25436-287d-411c-be97-ee28c335a4a4_text_markdown-005-SNP-005`

- **Batch de origen:** batch_046
- **Estrato:** E3

**snippet_primary:**

> "I provided full proof that I was blocked by the seller within the refund period, yet Gumroad kept sending automated AI replies saying \"contact the seller.\" Now, they simply ignore my emails — not even a single human response. This platform protects scammers, not creators or customers. I've already reported this to FTC and my local bank."

| Campo | Sonnet | Fable |
|---|---|---|
| `claim_type` _(A · 🔒 enum)_ | review_statement | anecdotal_report |
| `local_qualifiers` _(A · 📝 texto libre)_ | within the refund period | I provided full proof that I was blocked by the seller within the refund period · kept sending automated AI replies saying "contact the seller" · This platform protects scammers, not creators or customers |
| `metric_type` _(A · 🔒 enum)_ | refund_policy | unknown |
| `parser_notes` _(A · 📝 texto libre)_ | Buyer states having reported the matter to FTC and their bank | 'FTC' is a regulator, not a platform — excluded (K3). |
| `subject_exact` _(A · 📝 texto libre)_ | Trustpilot buyer complaint of automated-only Gumroad support response after being blocked by a seller within the refund window | buyer blocked by a seller within the refund period who received only automated AI replies from Gumroad, then silence, and reported the case to the FTC and their bank |
| `time_scope_normalized_if_safe` _(B · 📝 texto libre)_ | 2025-11-19 | _(null)_ |
| `time_scope_raw` _(B · 📝 texto libre)_ | November 19, 2025 | _(null)_ |
| `uncertainties` _(A · 🔒 enum)_ | none | anecdotal_single_source |

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

