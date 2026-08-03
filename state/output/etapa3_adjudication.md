# Etapa 3 — casos para adjudicacion del operador

Muestra estratificada reproducible. Semilla `20260803`. 60 casos.

Cada bloque muestra solo los campos en desacuerdo, de tipo (A)
divergencia de valor o (B) presencia vs ausencia. Las diferencias de
solo orden (C) se listan aparte al final de cada bloque cuando existen,
y no motivan la inclusion del caso.

El veredicto lo escribe el operador. El script no adjudica.

---

## Caso 1 — `ER-SP-compass_artifact_wf-0ffe7308-62e3-4530-ae68-93720df60f34_text_markdown-012-SNP-003`

- **Batch de origen:** batch_002
- **Estrato:** E1

**snippet_primary:**

> "By default, the base currency of an etsy shop is set to be the same as that of the seller's native currency. However, sellers have an option to change the base currency used by their shops and thus their listings. If you change your shop's base currency to something other than your native currency, an extra 2.5% conversion fee will be charged on all deposits."

| Campo | Sonnet | Fable |
|---|---|---|
| `actor_level` _(A)_ | platform | source |
| `claim_type` _(A)_ | policy_statement | pricing_statement |
| `evidence_role` _(A)_ | official_policy | direct_claim |
| `local_qualifiers` _(A)_ | if you change your shop's base currency to something other than your native currency | By default · If you change your shop's base currency to something other than your native currency · on all deposits |
| `metric_unit` _(A)_ | percent | percent of deposits |
| `parser_notes` _(B)_ | _(lista vacia)_ | Third-party calculator page (Investomatica) describing Etsy fee policy; page attributes data to 'Source: etsy.com'. · time_scope_normalized_if_safe from source_date_if_available ('Last reviewed April 4, 2026') per criteria G. |
| `subject_exact` _(A)_ | Etsy shop base currency conversion fee when set to a non-native currency | Etsy 2.5% currency conversion fee on deposits when shop base currency differs from seller's native currency |
| `time_scope_normalized_if_safe` _(B)_ | _(null)_ | 2026-04-04 |
| `uncertainties` _(B)_ | none | _(lista vacia)_ |

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
| `geography_if_explicit` _(B)_ | Mexico | _(null)_ |
| `local_qualifiers` _(A)_ | configurarlo es totalmente gratis (setup is free) | Configurarlo es totalmente gratis · solo pagarás 4.5% + 10.00 MXN por cada venta |
| `metric_unit` _(A)_ | percent + fixed fee (MXN) | percent of sale plus fixed MXN amount (mixed units declared) |
| `parser_notes` _(A)_ | Snippet is in Spanish; per-sale fee figure differs slightly from the 4.5% + 8 MXN figure in the investomatica calculator record for the same market — not reconciled here, as Data Extraction does not compare sources. | Snippet is an FAQ answer beginning with 'No.'; the question it answers was not captured — fee layer (processing vs other) not determinable from snippet alone. · No platform name in snippet text; 'Etsy' only in source_ref URL; platforms left empty per criteria F. · MXN currency does not by itself establish geography; geography left null. |
| `platforms` _(B)_ | Etsy | _(lista vacia)_ |
| `subject_exact` _(A)_ | Etsy Mexico seller transaction fee rate stated on the Etsy Mexico Payments page (Spanish) | per-sale charge (4.5% + 10.00 MXN) with free setup stated on Etsy MX payments page |
| `uncertainties` _(A)_ | none | source_date_unclear · context_insufficient |

**Criterios vigentes en este batch:**

- Sonnet — ninguna adicion formulada aun; solo criterios base.
- Fable — ninguna adicion formulada aun; solo criterios base.

**Veredicto:**


---

## Caso 3 — `ER-SP-compass_artifact_wf-22c5fbd5-9e04-4d5a-9b0e-4cb97acec9cc_text_markdown_normalized-011-SNP-006`

- **Batch de origen:** batch_003
- **Estrato:** E1

**snippet_primary:**

> "Domestika hasn't stopped paying every inactive instructor. Liam Filler*, a Florida-based instructor, has been getting paid until now, despite not replying to students for a year and a half. He, too, like Diego, launched his course around 2019. The reason why Domestika has targeted some while paying others is unknown. The only difference I spotted is that Liam lives in the U.S. (where Domestika's office is), while the others are based outside."

| Campo | Sonnet | Fable |
|---|---|---|
| `actor_level` _(A)_ | seller | source |
| `claim_type` _(A)_ | anecdotal_report | comparative_commentary |
| `evidence_role` _(A)_ | reported_event | comparative_commentary |
| `geography_if_explicit` _(A)_ | U.S. / Florida | Florida · the U.S. |
| `local_qualifiers` _(A)_ | The reason why Domestika has targeted some while paying others is unknown | despite not replying to students for a year and a half · launched his course around 2019 · The reason why Domestika has targeted some while paying others is unknown · The only difference I spotted |
| `parser_notes` _(B)_ | _(lista vacia)_ | Asterisk after the instructor name marks a pseudonym per the source's convention. · Journalist's own comparison across two instructor cases; assigned 'source'. |
| `subject_exact` _(A)_ | Instructor-reported selective payment halt pattern correlated with instructor location (US vs. outside US), per investigative report | differential Domestika payment treatment of inactive instructors: US-based instructor still paid versus others halted |
| `time_scope_raw` _(A)_ | a year and a half of inactivity | until now |
| `uncertainties` _(A)_ | anecdotal_single_source · methodology_unclear | anecdotal_single_source |

**Criterios vigentes en este batch:**

- Sonnet — ninguna adicion formulada aun; solo criterios base.
- Fable — ninguna adicion formulada aun; solo criterios base.

**Veredicto:**


---

## Caso 4 — `ER-SP-compass_artifact_wf-22c5fbd5-9e04-4d5a-9b0e-4cb97acec9cc_text_markdown_normalized-011-SNP-007`

- **Batch de origen:** batch_003
- **Estrato:** E1

**snippet_primary:**

> "In August 2025, when Diego Gomez*, a Madrid-based Domestika instructor, checked his instructor dashboard, he found that the billion-dollar company had stopped paying him since July. The reason was his inactivity in the forum. He didn't understand why the online creative learning platform had halted his payments now. He had stopped replying to comments four years ago (his contract never stated it as a payment condition), and he was still getting paid until June 2025."

| Campo | Sonnet | Fable |
|---|---|---|
| `actor_level` _(A)_ | seller | source |
| `geography_if_explicit` _(A)_ | Madrid, España | Madrid |
| `local_qualifiers` _(A)_ | his contract never stated forum activity as a payment condition | The reason was his inactivity in the forum · He had stopped replying to comments four years ago (his contract never stated it as a payment condition) · he was still getting paid until June 2025 |
| `parser_notes` _(B)_ | _(lista vacia)_ | Asterisk after the instructor name marks a pseudonym per the source's convention. · Third-person journalistic narration of one instructor's account; assigned 'source'. |
| `subject_exact` _(A)_ | Instructor-reported payment halt tied to forum-comment inactivity despite years of prior payment continuity (Diego Gomez, per report) | reported Domestika payment halt since July 2025 for Madrid-based instructor Diego Gomez attributed to forum inactivity, discovered August 2025 |
| `time_scope_raw` _(A)_ | In August 2025... since July... four years ago... until June 2025 | In August 2025 |

**Criterios vigentes en este batch:**

- Sonnet — ninguna adicion formulada aun; solo criterios base.
- Fable — ninguna adicion formulada aun; solo criterios base.

**Veredicto:**


---

## Caso 5 — `ER-SP-compass_artifact_wf-28ef9d76-a020-462a-83e9-3321b6ece5b4_text_markdown_normalized-002-SNP-001`

- **Batch de origen:** batch_004
- **Estrato:** E1

**snippet_primary:**

> "Payhip is ideal for digital product creators, authors, or coaches who want a simple, free solution to start selling files, courses, and memberships with global tax handling."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(B)_ | _(lista vacia)_ | ideal for digital product creators, authors, or coaches · to start selling |
| `platforms` _(A)_ | Payhip · Gumroad | Payhip |
| `subject_exact` _(A)_ | Third-party blog recommendation of Payhip for digital product creators needing global tax handling, as a Gumroad alternative | characterization of Payhip as a simple free solution for selling files, courses and memberships with global tax handling |
| `uncertainties` _(A)_ | none | source_date_unclear |

**Criterios vigentes en este batch:**

- Sonnet — ninguna adicion formulada aun; solo criterios base.
- Fable — ninguna adicion formulada aun; solo criterios base.

**Veredicto:**


---

## Caso 6 — `ER-SP-compass_artifact_wf-28ef9d76-a020-462a-83e9-3321b6ece5b4_text_markdown_normalized-008-SNP-001`

- **Batch de origen:** batch_005
- **Estrato:** E1

**snippet_primary:**

> "More features. Much lower fees. Talk to real people who actually care. Payhip is the #1 eCommerce platform for selling digital products"

| Campo | Sonnet | Fable |
|---|---|---|
| `claim_type` _(A)_ | comparative_commentary | explicit_claim |
| `parser_notes` _(B)_ | _(lista vacia)_ | '#1' ranking self-claim with no basis stated in snippet. |
| `subject_exact` _(A)_ | Payhip's own marketing tagline claiming more features and lower fees than competitors, per Payhip Vs Gumroad page | Payhip self-claim as the #1 eCommerce platform for selling digital products, with lower fees and human support |
| `uncertainties` _(A)_ | none | source_date_unclear · author_conflict_of_interest_possible · methodology_unclear |

**Criterios vigentes en este batch:**

- Sonnet — ninguna adicion formulada aun; solo criterios base.
- Fable — ninguna adicion formulada aun; solo criterios base.

**Veredicto:**


---

## Caso 7 — `ER-SP-compass_artifact_wf-28ef9d76-a020-462a-83e9-3321b6ece5b4_text_markdown_normalized-021-SNP-001`

- **Batch de origen:** batch_005
- **Estrato:** E1

**snippet_primary:**

> "But if you're earning $500+ per month, the 5% cut can start to feel heavy. That's when platforms with 0% transaction fees (like Ko-fi Gold or Payhip's paid plan) may be better."

| Campo | Sonnet | Fable |
|---|---|---|
| `actor_level` _(A)_ | source | third_party |
| `local_qualifiers` _(B)_ | _(lista vacia)_ | if you're earning $500+ per month · may be better |
| `metric_unit` _(A)_ | USD / percent | percent |
| `metric_value_raw` _(A)_ | $500+/month threshold; 5% cut; 0% on paid plans | 5% |
| `parser_notes` _(B)_ | _(lista vacia)_ | The 5% cut refers to the platform in the page title (Buy Me a Coffee), which is not named in the snippet text; platforms list only names appearing in text per criteria F. · Blog hosted by Schoolmaker, a course-platform provider; assigned third_party. |
| `platforms` _(A)_ | Payhip · Ko-fi · Buy Me a Coffee | Ko-fi · Payhip |
| `subject_exact` _(A)_ | Third-party blog comparison noting Ko-fi Gold and Payhip's paid plan as 0%-transaction-fee alternatives once earnings exceed $500/month | commentary that a 5% platform cut weighs at $500+ monthly earnings, favoring 0%-transaction-fee options like Ko-fi Gold or Payhip's paid plan |
| `uncertainties` _(A)_ | none | source_date_unclear · author_conflict_of_interest_possible |

**Criterios vigentes en este batch:**

- Sonnet — ninguna adicion formulada aun; solo criterios base.
- Fable — ninguna adicion formulada aun; solo criterios base.

**Veredicto:**


---

## Caso 8 — `ER-SP-compass_artifact_wf-28f59dc7-8351-48a1-bcaa-ff9992b8fe70_text_markdown-008-SNP-002`

- **Batch de origen:** batch_006
- **Estrato:** E1

**snippet_primary:**

> "Intentar contactar con Domestika no fue sencillo. Hay un chat en la esquina inferior, pero es para hablar con una IA... y esta te remite a una página donde se indica que no es posible cancelar la suscripción una vez activada."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(B)_ | _(lista vacia)_ | pero es para hablar con una IA · donde se indica que no es posible cancelar la suscripción una vez activada |
| `parser_notes` _(B)_ | _(lista vacia)_ | The no-cancellation statement is the buyer's report of a platform page, not a directly captured policy text. |
| `subject_exact` _(A)_ | Buyer account of difficulty contacting Domestika support, describing an AI-only chat that redirects to a no-cancellation page | buyer-reported contact difficulty with Domestika: AI-only chat redirecting to a page stating the subscription cannot be cancelled once activated |
| `time_scope_normalized_if_safe` _(B)_ | 2025-12-17 | _(null)_ |
| `time_scope_raw` _(B)_ | 17 diciembre 2025 | _(null)_ |

**Criterios vigentes en este batch:**

- Sonnet — ninguna adicion formulada aun; solo criterios base.
- Fable — ninguna adicion formulada aun; solo criterios base.

**Veredicto:**


---

## Caso 9 — `ER-SP-compass_artifact_wf-28f59dc7-8351-48a1-bcaa-ff9992b8fe70_text_markdown-014-SNP-004`

- **Batch de origen:** batch_007
- **Estrato:** E1

**snippet_primary:**

> "I am writing this to warn others about Domestika's deceptive billing practices. What started as a small, one-off purchase has turned into a nightmare of unauthorized, high-value charges. In March 2025, I was charged $175 without any prior notification, renewal reminder, or receipt. Most recently, they hit my account for a staggering $361.70—a massive \"price hike\" that was also taken without consent or notice."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(A)_ | without any prior notification, renewal reminder, or receipt | What started as a small, one-off purchase · without any prior notification, renewal reminder, or receipt · that was also taken without consent or notice |
| `metric_value_raw` _(A)_ | $175 (March 2025); $361.70 (most recent) | $361.70 |
| `parser_notes` _(B)_ | _(lista vacia)_ | Earlier figure in snippet: '$175' charged in March 2025; latest charge undated, so no normalization. |
| `subject_exact` _(A)_ | Buyer report of two undisclosed Domestika charges in 2025 (a $175 charge and a later $361.70 'price hike') with no prior notification | buyer-reported escalating unauthorized Domestika charges after a one-off purchase: $175 in March 2025 and most recently $361.70, without notification or consent |
| `time_scope_normalized_if_safe` _(B)_ | 2025-03 | _(null)_ |
| `time_scope_raw` _(A)_ | In March 2025 | In March 2025 … Most recently |
| `uncertainties` _(A)_ | anecdotal_single_source | anecdotal_single_source · source_date_unclear |

**Criterios vigentes en este batch:**

- Sonnet — ninguna adicion formulada aun; solo criterios base.
- Fable — ninguna adicion formulada aun; solo criterios base.

**Veredicto:**


---

## Caso 10 — `ER-SP-compass_artifact_wf-291008ae-711f-4c29-83eb-6a5c8ef0eef8_text_markdown_normalized-003-SNP-007`

- **Batch de origen:** batch_007
- **Estrato:** E1

**snippet_primary:**

> "I have bought a face yoga program which they launched as the original program from Valeriia Veksler. Which it is not!! They have misused her content, her own set-up, her face and her brand."

| Campo | Sonnet | Fable |
|---|---|---|
| `claim_type` _(A)_ | review_statement | anecdotal_report |
| `local_qualifiers` _(B)_ | _(lista vacia)_ | which they launched as the original program from Valeriia Veksler |
| `parser_notes` _(B)_ | _(lista vacia)_ | Misuse assertion is the reviewer's claim; company name appears only in source_ref URL. |
| `platforms` _(B)_ | Lemon Squeezy | _(lista vacia)_ |
| `subject_exact` _(A)_ | Buyer review alleging a face-yoga program sold via Lemon Squeezy misappropriated another creator's (Valeriia Veksler) content, likeness, and brand | buyer-reported face yoga program sold as Valeriia Veksler's original which the buyer asserts misused her content, set-up, face and brand |

**Criterios vigentes en este batch:**

- Sonnet — ninguna adicion formulada aun; solo criterios base.
- Fable — ninguna adicion formulada aun; solo criterios base.

**Veredicto:**


---

## Caso 11 — `ER-SP-compass_artifact_wf-295a3f4a-2ebb-4c3b-9b1d-9b7d3840172c_text_markdown-009-SNP-001`

- **Batch de origen:** batch_008
- **Estrato:** E1

**snippet_primary:**

> "Aparte de las compras nacionales, un segmento importante de las transacciones provienen de Estados Unidos y Latinoamérica: \"La idea es seguir creciendo, consolidarnos en todo México y explorar la expansión a otros países. Tenemos compradores interesantes en Estados Unidos, centro y Suramérica que se parecen a México en términos de mercado y confianza. Hacia allá vamos\", finalizó De Heredia."

| Campo | Sonnet | Fable |
|---|---|---|
| `actor_level` _(A)_ | marketplace | platform |
| `geography_if_explicit` _(A)_ | Estados Unidos · centro y Suramérica | Estados Unidos · Latinoamérica · México · centro y Suramérica |
| `local_qualifiers` _(A)_ | un segmento importante | La idea es seguir creciendo · que se parecen a México en términos de mercado y confianza · Hacia allá vamos |
| `parser_notes` _(B)_ | _(lista vacia)_ | Article lead ('un segmento importante de las transacciones') is the source's wording; 'importante' not reproduced in fields. · Platform name appears only in source_title/URL, not in snippet text; platforms left empty per criteria F. · time_scope_normalized_if_safe from source_date_if_available ('21 de junio de 2016') per criteria G. |
| `platforms` _(B)_ | Kichink | _(lista vacia)_ |
| `subject_exact` _(A)_ | Kichink founder's statement identifying the US and Latin America as a significant share of transactions, alongside expansion aspirations | Kichink founder statement on transaction origins from the United States and Latin America and intent to consolidate in Mexico and expand to similar markets |
| `time_scope_raw` _(B)_ | 21 de junio de 2016 | _(null)_ |
| `uncertainties` _(B)_ | methodology_unclear | _(lista vacia)_ |

**Criterios vigentes en este batch:**

- Sonnet — ninguna adicion formulada aun; solo criterios base.
- Fable — ninguna adicion formulada aun; solo criterios base.

**Veredicto:**


---

## Caso 12 — `ER-SP-compass_artifact_wf-3128bd63-7fd1-4bd6-86d1-63a1780fe467_text_markdown-003-SNP-003`

- **Batch de origen:** batch_008
- **Estrato:** E1

**snippet_primary:**

> "If you're in a country that has no tax treaty with the US, unfortunately, we won't be able to reduce the royalty withholding tax rate of 30%."

| Campo | Sonnet | Fable |
|---|---|---|
| `geography_if_explicit` _(A)_ | US | the US |
| `local_qualifiers` _(B)_ | _(lista vacia)_ | If you're in a country that has no tax treaty with the US |
| `metric_type` _(A)_ | fee_rate | tax_withholding_rate |
| `parser_notes` _(B)_ | _(lista vacia)_ | metric_type out of enum: observed metric is a tax withholding rate; no enum value covers it. · Platform name appears only in source_title/URL; platforms left empty per criteria F. |
| `platforms` _(B)_ | Envato | _(lista vacia)_ |
| `subject_exact` _(A)_ | Envato inability to reduce the 30% royalty withholding tax rate for authors in countries without a US tax treaty | no reduction of the 30% royalty withholding rate for authors in countries without a US tax treaty |
| `uncertainties` _(A)_ | none | source_date_unclear |

**Criterios vigentes en este batch:**

- Sonnet — ninguna adicion formulada aun; solo criterios base.
- Fable — ninguna adicion formulada aun; solo criterios base.

**Veredicto:**


---

## Caso 13 — `ER-SP-compass_artifact_wf-4ef0d94a-344f-48de-a6a0-29bd09258ed5_text_markdown_normalized-005-SNP-001`

- **Batch de origen:** batch_011
- **Estrato:** E1

**snippet_primary:**

> "Domestika doesn't apply commissions or taxes relating to the exchange rate between currencies. However, your bank or payment processor may add an additional fee and so we suggest that you contact them directly to confirm their policy regarding this."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(A)_ | your bank or payment processor may add an additional fee | However, your bank or payment processor may add an additional fee · we suggest that you contact them directly to confirm their policy |
| `metric_type` _(A)_ | unknown | fee_rate |
| `parser_notes` _(B)_ | _(lista vacia)_ | Claim asserts absence of platform FX fees; no numeric value present. |
| `subject_exact` _(A)_ | Domestika's non-application of currency exchange commissions/taxes, with possible bank/processor fees disclaimed | Domestika claim of applying no exchange-rate commissions or taxes, with possible additional fees from the buyer's bank or payment processor |
| `uncertainties` _(B)_ | _(lista vacia)_ | source_date_unclear |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008)

**Veredicto:**


---

## Caso 14 — `ER-SP-compass_artifact_wf-4ef0d94a-344f-48de-a6a0-29bd09258ed5_text_markdown_normalized-014-SNP-004`

- **Batch de origen:** batch_012
- **Estrato:** E1

**snippet_primary:**

> "A Domestika course usually has between two and four hours of content, and we recommend for at least 60% of that to be in video format, but we'll advise you in detail on all these topics in due time."

| Campo | Sonnet | Fable |
|---|---|---|
| `claim_type` _(A)_ | policy_statement | explicit_claim |
| `evidence_role` _(A)_ | official_policy | direct_claim |
| `local_qualifiers` _(A)_ | we'll advise you in detail on all these topics in due time | usually · we recommend for at least 60% of that to be in video format · but we'll advise you in detail on all these topics in due time |
| `metric_type` _(A)_ | unknown | course content duration |
| `metric_unit` _(A)_ | hours/percent | hours of content |
| `metric_value_raw` _(A)_ | between two and four hours; at least 60% | between two and four hours |
| `parser_notes` _(B)_ | _(lista vacia)_ | metric_type out of enum: observed metric is course content duration; no enum value covers it. · Additional figure in snippet: recommended 'at least 60%' video share. |
| `subject_exact` _(A)_ | Domestika course length and video-format-share recommendation for teacher-submitted courses (2-4 hours, at least 60% video) | typical Domestika course length of two to four hours of content with recommended minimum 60% in video format |
| `uncertainties` _(B)_ | _(lista vacia)_ | source_date_unclear |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008)

**Veredicto:**


---

## Caso 15 — `ER-SP-compass_artifact_wf-4ef0d94a-344f-48de-a6a0-29bd09258ed5_text_markdown_normalized-015-SNP-007`

- **Batch de origen:** batch_013
- **Estrato:** E1

**snippet_primary:**

> "If you initiate your subscription with a free trial, you will receive one Plus credit at the start of the trial period. If you do not cancel before the free trial period ends, the subscription will automatically continue under the applicable billing cycle, and the remaining credits will be granted accordingly (11 credits for an annual subscription or 1 credit for a monthly subscription). Conversely, if you cancel your subscription before the trial period concludes and have not redeemed the Plus credit granted, that credit will be automatically canceled and will no longer be available for use."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(A)_ | credit is automatically cancelled and forfeited if subscription cancelled before trial ends and credit unredeemed | If you initiate your subscription with a free trial · If you do not cancel before the free trial period ends, the subscription will automatically continue under the applicable billing cycle · if you cancel your subscription before the trial period concludes and have not redeemed the Plus credit granted |
| `metric_type` _(A)_ | unknown | subscription credits granted |
| `metric_value_raw` _(A)_ | 1 credit at trial start; 11 additional credits (annual) or 1 additional credit (monthly) if not cancelled | one Plus credit … 11 credits for an annual subscription or 1 credit for a monthly subscription |
| `parser_notes` _(B)_ | _(lista vacia)_ | metric_type out of enum: observed metric is a credits-granted quantity; no enum value covers it. · Platform name appears only in source_ref URL for this snippet; platforms left empty per criteria F. · time_scope_normalized_if_safe from source_date_if_available (terms updated January 31, 2024) per criteria G/K1. |
| `platforms` _(B)_ | Domestika | _(lista vacia)_ |
| `subject_exact` _(A)_ | Domestika Plus free-trial credit allocation and cancellation-forfeiture rule | free-trial credit mechanics: 1 Plus credit at trial start, automatic billing continuation with remaining credits (11 annual / 1 monthly) unless cancelled, and cancellation of unredeemed trial credit |
| `time_scope_normalized_if_safe` _(B)_ | _(null)_ | 2024-01-31 |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008)

**Veredicto:**


---

## Caso 16 — `ER-SP-compass_artifact_wf-4ff72059-9383-471e-a419-d446777044ad_text_markdown-004-SNP-002`

- **Batch de origen:** batch_013
- **Estrato:** E1

**snippet_primary:**

> "Si el monto mínimo no es alcanzado, El Agregador podrá procesar el pago a petición de La Tienda con un cargo adicional por concepto administrativo del 10% (diez por ciento) con un mínimo a cobrar de $10.00 (diez pesos 00/100 moneda nacional) más IVA sobre el valor de la transacción."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(A)_ | a petición de la tienda | Si el monto mínimo no es alcanzado · a petición de La Tienda · por concepto administrativo · sobre el valor de la transacción |
| `metric_unit` _(A)_ | percent/MXN | percent with MXN minimum plus IVA (mixed units declared) |
| `metric_value_raw` _(A)_ | 10% (mínimo $10.00 + IVA) | 10% (diez por ciento) con un mínimo a cobrar de $10.00 (diez pesos 00/100 moneda nacional) más IVA |
| `parser_notes` _(B)_ | _(lista vacia)_ | Platform name appears only in source_ref URL ('El Agregador'/'La Tienda' in text); platforms left empty per criteria F. |
| `platforms` _(B)_ | Kichink | _(lista vacia)_ |
| `subject_exact` _(A)_ | Kichink/Aggregator below-minimum settlement administrative fee (10%, with $10 MXN + IVA minimum) processed on store request | 10% administrative surcharge (minimum $10.00 MXN plus IVA) for store-requested payouts below the minimum settlement amount |
| `uncertainties` _(B)_ | _(lista vacia)_ | source_date_unclear |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008)

**Veredicto:**


---

## Caso 17 — `ER-SP-compass_artifact_wf-4ff72059-9383-471e-a419-d446777044ad_text_markdown-004-SNP-015`

- **Batch de origen:** batch_014
- **Estrato:** E1

**snippet_primary:**

> "La TIENDA debe confirmar la orden de compra y programar la recolección del producto o los productos comprados en un plazo máximo de 72 horas hábiles posteriores a la compra por parte del COMPRADOR."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(B)_ | _(lista vacia)_ | posteriores a la compra por parte del COMPRADOR |
| `metric_type` _(A)_ | unknown | order confirmation deadline |
| `metric_unit` _(A)_ | business hours | horas hábiles |
| `metric_value_raw` _(A)_ | 72 | un plazo máximo de 72 horas hábiles |
| `parser_notes` _(B)_ | _(lista vacia)_ | metric_type out of enum: observed metric is an order-confirmation deadline; no enum value covers it. · Platform name appears only in source_ref URL for this snippet; platforms left empty per criteria F. |
| `platforms` _(B)_ | Kichink | _(lista vacia)_ |
| `subject_exact` _(A)_ | Kichink seller obligation to confirm the order and schedule product pickup within 72 business hours of purchase | store obligation to confirm purchase orders and schedule product pickup within 72 business hours of the buyer's purchase |
| `uncertainties` _(B)_ | _(lista vacia)_ | source_date_unclear |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008)

**Veredicto:**


---

## Caso 18 — `ER-SP-compass_artifact_wf-5c07963d-6c4c-4536-a602-03c04203e92c_text_markdown-007-SNP-001`

- **Batch de origen:** batch_014
- **Estrato:** E1

**snippet_primary:**

> "Etsy? That's more like renting a shelf in a crowded marketplace. Sure, you tap into a built-in audience, but you're competing with a million other makers. You can pretty it up a bit—but you're still boxed into Etsy's layout. And when someone buys from you there, what do they say? 'I got it on Etsy.' Ouch."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(A)_ | you're competing with a million other makers · you're still boxed into Etsy's layout | Sure, you tap into a built-in audience · but you're competing with a million other makers · you're still boxed into Etsy's layout |
| `parser_notes` _(A)_ | source is Big Cartel, a competing storefront platform; commentary critiques Etsy in a context promoting Big Cartel as the alternative | Blog hosted by Big Cartel, a competing platform; 'a million other makers' is rhetorical wording. · time_scope_normalized_if_safe from source_date_if_available ('2025-06-24') per criteria G/K1. |
| `subject_exact` _(A)_ | metaphorical comparison contrasting Etsy's built-in traffic/competition tradeoff against loss of brand attribution at point of sale | Big Cartel characterization of Etsy as renting a shelf in a crowded marketplace: built-in audience, heavy maker competition, layout constraints, and purchases attributed to Etsy |
| `time_scope_normalized_if_safe` _(B)_ | _(null)_ | 2025-06-24 |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008)

**Veredicto:**


---

## Caso 19 — `ER-SP-compass_artifact_wf-5c07963d-6c4c-4536-a602-03c04203e92c_text_markdown-020-SNP-001`

- **Batch de origen:** batch_015
- **Estrato:** E1

**snippet_primary:**

> "On the buyer side, approximately 83% say Etsy has items they can't find anywhere else, making it a powerful marketplace for sellers of creative goods. eBay is a digital shopping marketplace that operates at a larger scale than Etsy, with 133 million active buyers worldwide and approximately two billion live listings across more than 190 global markets."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(B)_ | _(lista vacia)_ | approximately 83% say · approximately two billion live listings across more than 190 global markets |
| `metric_type` _(A)_ | unknown | active_buyers |
| `metric_unit` _(A)_ | percent/buyers/listings/markets | active buyers worldwide (eBay) |
| `metric_value_raw` _(A)_ | 83%; 133 million; approximately two billion; more than 190 | 133 million |
| `parser_notes` _(A)_ | source is Shopify's own blog, a party unaffiliated with but commercially adjacent to both Etsy and eBay as a storefront alternative | Blog hosted by Shopify, a competing platform. · Additional metric in snippet: 'approximately 83%' of buyers say Etsy has items they can't find anywhere else (survey basis not stated). · time_scope_normalized_if_safe from source_date_if_available ('2025-03-06') per criteria G/K1. |
| `subject_exact` _(A)_ | comparative marketplace-scale statistics for Etsy (83% of buyers say items are unique) and eBay (133 million active buyers, approximately two billion live listings, 190+ markets) | buyer-side uniqueness perception (~83% say Etsy has items findable nowhere else) versus eBay scale (133 million active buyers, ~2 billion live listings, 190+ markets) |
| `time_scope_normalized_if_safe` _(B)_ | _(null)_ | 2025-03-06 |

Diferencias de solo orden (C) en este record, no motivan inclusion:
- `uncertainties`

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008)

**Veredicto:**


---

## Caso 20 — `ER-SP-compass_artifact_wf-63c228bc-9037-4ba4-9569-3f62e8735192_text_markdown-012-SNP-001`

- **Batch de origen:** batch_016
- **Estrato:** E1

**snippet_primary:**

> "So far, I have made 734 sales from 28 products with a net profit of $515.10 (yes, all fees are already deducted here)."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(A)_ | 734 sales from 28 products · all fees already deducted | (yes, all fees are already deducted here) |
| `metric_unit` _(A)_ | USD | USD net (fees deducted) |
| `parser_notes` _(B)_ | _(lista vacia)_ | Additional figures in snippet: '734 sales', '28 products'; the 1000-day span appears in source_title. · Platform named only in source_title/URL, not in snippet text; platforms left empty per criteria F. |
| `platforms` _(B)_ | Gumroad | _(lista vacia)_ |
| `subject_exact` _(A)_ | seller-reported cumulative Gumroad net profit ($515.10 from 734 sales across 28 products) after fees, over roughly 1000 days | seller-reported 734 sales across 28 products with $515.10 net profit after roughly 1000 days selling on Gumroad |
| `time_scope_raw` _(A)_ | 1000 days | So far |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008)

**Veredicto:**


---

## Caso 21 — `ER-SP-compass_artifact_wf-7a40dcc5-be9a-4273-a3e8-0d53cab18fb3_text_markdown_normalized-011-SNP-001`

- **Batch de origen:** batch_017
- **Estrato:** E2

**snippet_primary:**

> "Over a year ago, I traveled to the Bologna Children's Book Fair with my freshly printed portfolio, looking for clarity and a new spark. That trip led to a big shift in my art journey. I decided to pause children's book illustration and started focusing on creating art for products and licensing. Now, one year (and 300 Etsy sales!) later, I'm celebrating the joy and balance I've found in making and selling my own artwork."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(B)_ | _(lista vacia)_ | I decided to pause children's book illustration and started focusing on creating art for products and licensing |
| `metric_unit` _(A)_ | sales | sales (first year) |
| `parser_notes` _(B)_ | _(lista vacia)_ | 'Bologna Children's Book Fair' is an event in the narrative, not claim geography. |
| `subject_exact` _(A)_ | seller-reported cumulative Etsy sales count after one year selling art products | artist-seller celebrating 300 Etsy sales one year after shifting from children's book illustration to product art and licensing |
| `time_scope_raw` _(A)_ | one year | Over a year ago … Now, one year later |
| `uncertainties` _(A)_ | none | anecdotal_single_source |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016)

**Veredicto:**


---

## Caso 22 — `ER-SP-compass_artifact_wf-7b6a9899-eda3-4893-93ba-3553f79cab42_text_markdown-005-SNP-005`

- **Batch de origen:** batch_018
- **Estrato:** E2

**snippet_primary:**

> "Hotmart es una experiencia desagradable para creadores. Aca estoy usando su paygate para mi plataforma de Kajabi, para aceptar pagos en monedas locales en Latinoamérica y se han tardado más de un mes en aprobar mis documentos y darme entrada para poder registrar cuenta bancaria y aceptar pagos en dólares aunque ya estaba vendiendo mi producto digital. Estoy poniendo quejas en el BBB de los EEUU. Es falta de ética el tomarse 5 días cada vez para \"analizar\" documentos legales que ni me piden acá en EEUU. Al poner mis quejas finalmente aprobaron los documentos pero no puedo retirar todo el dinero que he hecho a pesar de que ellos se quedan con un porcentaje. Piénsalo bien antes de usar su plataforma."

| Campo | Sonnet | Fable |
|---|---|---|
| `claim_type` _(A)_ | review_statement | anecdotal_report |
| `geography_if_explicit` _(A)_ | Latin America · United States | Latinoamérica · EEUU |
| `local_qualifiers` _(A)_ | already selling my digital product · 5 days each time to analyze documents | para aceptar pagos en monedas locales en Latinoamérica · aunque ya estaba vendiendo mi producto digital · Es falta de ética el tomarse 5 días cada vez para "analizar" documentos legales · Al poner mis quejas finalmente aprobaron los documentos pero no puedo retirar todo el dinero |
| `parser_notes` _(B)_ | _(lista vacia)_ | 'BBB de los EEUU' named in text as the complaint venue. |
| `platforms` _(A)_ | Hotmart · Kajabi | Hotmart · Kajabi · BBB |
| `subject_exact` _(A)_ | seller-reported delay in Hotmart document approval for accepting payments via Kajabi paygate integration | US-based creator using Hotmart as paygate for a Kajabi platform reporting over a month of document approval delays for local-currency payments in Latin America, BBB complaints, and remaining withdrawal limits |
| `time_scope_raw` _(A)_ | more than a month | se han tardado más de un mes |
| `uncertainties` _(A)_ | none | anecdotal_single_source |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016)

**Veredicto:**


---

## Caso 23 — `ER-SP-compass_artifact_wf-7df7092c-4929-4bbe-b35f-a7efa126b514_text_markdown_normalized-011-SNP-002`

- **Batch de origen:** batch_019
- **Estrato:** E2

**snippet_primary:**

> "envato.com's audience is 56.75% male and 43.25% female. The largest age group of visitors are 25 - 34 year olds."

| Campo | Sonnet | Fable |
|---|---|---|
| `metric_type` _(A)_ | unknown | audience demographics |
| `metric_unit` _(A)_ | percent | percent of audience |
| `metric_value_raw` _(A)_ | 56.75% male, 43.25% female; largest age group 25-34 | 56.75% male and 43.25% female |
| `parser_notes` _(B)_ | _(lista vacia)_ | metric_type out of enum: observed metric is audience demographic shares; no enum value covers it. · time_scope_normalized_if_safe from page data period '[March 2026]' per criteria G/K1. |
| `subject_exact` _(A)_ | third-party demographic analytics on envato.com visitor audience | envato.com audience demographics: 56.75% male, 43.25% female, largest age group 25-34 (SimilarWeb) |
| `time_scope_normalized_if_safe` _(B)_ | _(null)_ | 2026-03 |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016)

**Veredicto:**


---

## Caso 24 — `ER-SP-compass_artifact_wf-7df7092c-4929-4bbe-b35f-a7efa126b514_text_markdown_normalized-012-SNP-001`

- **Batch de origen:** batch_019
- **Estrato:** E2

**snippet_primary:**

> "Most reviewers were unhappy with their experience overall. Many customers expressed dissatisfaction with the products, citing issues such as outdated content, faulty files, and items not matching descriptions."

| Campo | Sonnet | Fable |
|---|---|---|
| `evidence_role` _(A)_ | comparative_commentary | local_context |
| `local_qualifiers` _(B)_ | _(lista vacia)_ | Most reviewers · Many customers |
| `parser_notes` _(B)_ | _(lista vacia)_ | Aggregated summary text (likely platform-generated review synthesis), not an individual reviewer's voice; assigned 'source'. · Platform named only in source_ref URL; platforms left empty per criteria F. |
| `platforms` _(B)_ | Envato Market | _(lista vacia)_ |
| `subject_exact` _(A)_ | third-party aggregate sentiment summary of Envato Market buyer reviews | aggregate review summary: most reviewers unhappy, citing outdated content, faulty files and items not matching descriptions |
| `uncertainties` _(A)_ | methodology_unclear | source_date_unclear · methodology_unclear |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016)

**Veredicto:**


---

## Caso 25 — `ER-SP-compass_artifact_wf-7df7092c-4929-4bbe-b35f-a7efa126b514_text_markdown_normalized-013-SNP-001`

- **Batch de origen:** batch_019
- **Estrato:** E2

**snippet_primary:**

> "We've been using ThemeForest for years and all the products we've purchased have always worked well. However, our last product didn't work and was completely broken. We opened a dispute on PayPal for a refund and were blocked from our account. ThemeForest support requested a pause in the PayPal dispute. And now they claim they won't issue a refund even after reviewing our case and hundreds of negative reviews from the seller? This is an illegal practice since the product arrived completely broken. We no longer trust any Envato service."

| Campo | Sonnet | Fable |
|---|---|---|
| `claim_type` _(A)_ | review_statement | anecdotal_report |
| `evidence_role` _(A)_ | reported_event | anecdotal_example |
| `local_qualifiers` _(A)_ | completely broken · opened a dispute on PayPal for a refund and were blocked from our account | all the products we've purchased have always worked well · ThemeForest support requested a pause in the PayPal dispute · even after reviewing our case and hundreds of negative reviews from the seller |
| `metric_type` _(A)_ | refund_policy | unknown |
| `metric_unit` _(B)_ | reviews | _(null)_ |
| `metric_value_raw` _(B)_ | hundreds of negative reviews from the seller | _(null)_ |
| `parser_notes` _(B)_ | _(lista vacia)_ | 'illegal practice' is the reviewer's characterization, preserved in snippet only. |
| `platforms` _(A)_ | ThemeForest | ThemeForest · PayPal · Envato |
| `product_type_if_explicit` _(A)_ | design_asset | unknown |
| `subject_exact` _(A)_ | buyer-reported ThemeForest refund denial for a broken product despite a PayPal dispute | long-time ThemeForest buyer reporting a broken product, account blocked after opening a PayPal dispute, support requesting a dispute pause, and refund denied |
| `time_scope_raw` _(B)_ | _(null)_ | We've been using ThemeForest for years |
| `uncertainties` _(A)_ | none | anecdotal_single_source |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016)

**Veredicto:**


---

## Caso 26 — `ER-SP-compass_artifact_wf-80dc1a5e-cdb7-4f06-a0fb-62209a2ddd08_text_markdown-001-SNP-002`

- **Batch de origen:** batch_019
- **Estrato:** E2

**snippet_primary:**

> "Some features I want so that this platform can become better — Source — Doesn't tell where the traffic is coming from. Analytics is very basic. No categories. I sell in two niches, and categorizing them becomes difficult. No cross-selling or upselling. Email marketing is a little costly."

| Campo | Sonnet | Fable |
|---|---|---|
| `claim_type` _(A)_ | comparative_commentary | anecdotal_report |
| `local_qualifiers` _(A)_ | I sell in two niches, and categorizing them becomes difficult | Some features I want so that this platform can become better · I sell in two niches, and categorizing them becomes difficult · Email marketing is a little costly |
| `parser_notes` _(B)_ | _(lista vacia)_ | Which platform the feature list refers to is not determinable from the snippet alone (comparison article covers three). |
| `platforms` _(B)_ | Lemon Squeezy | _(lista vacia)_ |
| `subject_exact` _(A)_ | seller-reported feature gaps in Lemon Squeezy analytics, categorization, and marketing tools | seller-listed platform shortcomings: no traffic-source data, basic analytics, no categories (hindering two-niche selling), no cross/upselling, costly email marketing |
| `uncertainties` _(A)_ | none | anecdotal_single_source · source_date_unclear · context_insufficient |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016)

**Veredicto:**


---

## Caso 27 — `ER-SP-compass_artifact_wf-80dc1a5e-cdb7-4f06-a0fb-62209a2ddd08_text_markdown-002-SNP-001`

- **Batch de origen:** batch_020
- **Estrato:** E2

**snippet_primary:**

> "I sell templates for a living and have used several of these providers. The main options are Gumroad - high fees and ugly design, solid system never had issues does most what I need. Lemon Squeezy - it was very popular until being acquired by stripe. Full of serious bugs, bad support. Lovely design, slightly better fees than Gumroad, but many hidden. Would still use over Gumroad just cause the Gumroad checkout design is so bad it loses sales imo. Paddle - haven't used it but I think it's probably as good as Gumroad or Lemon. Polar.sh - the trendy new option, most creators abandoning Lemon Squeezy are moving there. Has lots of innovation in features beyond payments such as selling private GitHub access. All of these platforms are MOR as far as I know, all provide the checkout UI etc. all handle digital asset file delivery. They are perfect for creators selling digital products that want a turn key solution and don't want to do any development work."

| Campo | Sonnet | Fable |
|---|---|---|
| `evidence_role` _(A)_ | comparative_commentary | seller_self_claim |
| `local_qualifiers` _(A)_ | all provide checkout UI · all handle digital asset file delivery · haven't used Paddle · most creators abandoning Lemon Squeezy are moving to Polar.sh | I sell templates for a living and have used several of these providers · slightly better fees than Gumroad, but many hidden · haven't used it but I think · most creators abandoning Lemon Squeezy are moving there · as far as I know |
| `metric_type` _(A)_ | fee_rate | unknown |
| `parser_notes` _(B)_ | _(lista vacia)_ | 'templates' as sold product is generic; not covered by the product enum. · Design judgments ('ugly', 'lovely') are the seller's wording, in snippet only. · source_date approximate ('11 months ago' ≈ May 2025); not normalized. |
| `platforms` _(A)_ | Gumroad · Lemon Squeezy · Paddle · Polar.sh | Gumroad · Lemon Squeezy · Stripe · Paddle · Polar.sh · GitHub |
| `subject_exact` _(A)_ | seller comparison of digital-product Merchant-of-Record checkout providers (Gumroad, Lemon Squeezy, Paddle, Polar.sh) | template seller's survey of MOR checkout providers: Gumroad (high fees, solid), Lemon Squeezy (post-Stripe bugs, hidden fees), Paddle (untried), Polar.sh (trendy destination for Lemon Squeezy leavers) |
| `uncertainties` _(A)_ | none | anecdotal_single_source · source_date_unclear |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016)

**Veredicto:**


---

## Caso 28 — `ER-SP-compass_artifact_wf-80dc1a5e-cdb7-4f06-a0fb-62209a2ddd08_text_markdown-004-SNP-004`

- **Batch de origen:** batch_020
- **Estrato:** E2

**snippet_primary:**

> "The downside: you can't start selling immediately. Lemon Squeezy requires account approval, which can take several days to over a week, and their support is very slow. There have also been a lot of recent bugs, like people being unable to check out and customers getting double-charged."

| Campo | Sonnet | Fable |
|---|---|---|
| `claim_type` _(A)_ | comparative_commentary | anecdotal_report |
| `local_qualifiers` _(A)_ | support is very slow · people being unable to check out and customers getting double-charged | you can't start selling immediately · which can take several days to over a week · There have also been a lot of recent bugs, like people being unable to check out and customers getting double-charged |
| `metric_type` _(A)_ | activation_requirement | unknown |
| `metric_unit` _(B)_ | days | _(null)_ |
| `metric_value_raw` _(B)_ | several days to over a week | _(null)_ |
| `parser_notes` _(B)_ | _(lista vacia)_ | Bug reports about other users are secondhand within the seller's account. |
| `subject_exact` _(A)_ | seller-reported Lemon Squeezy account approval delay and recent checkout/double-charge bugs | seller-reported Lemon Squeezy downsides: account approval taking days to over a week, very slow support, and recent bugs including checkout failures and double charges |
| `time_scope_raw` _(B)_ | _(null)_ | recent |
| `uncertainties` _(A)_ | none | anecdotal_single_source |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016)

**Veredicto:**


---

## Caso 29 — `ER-SP-compass_artifact_wf-83a235d5-86a0-4c10-9097-e29688c3b834_text_markdown_normalized-016-SNP-001`

- **Batch de origen:** batch_021
- **Estrato:** E2

**snippet_primary:**

> "You will only be charged a listing fee for creating or renewing a listing on Etsy; there is no fee for editing a listing. You will be charged a listing fee whether or not the listed item sells, unless you create a private listing, in which case you will only be charged the listing fee when the private listing is sold. Etsy.com listings expire after four months. Pattern-only listings do not expire. If you list multiple quantities of the same item, the initial listing fee will be $0.20, and the listing will be automatically renewed at $0.20 after each of the items sells."

| Campo | Sonnet | Fable |
|---|---|---|
| `claim_type` _(A)_ | policy_statement | pricing_statement |
| `local_qualifiers` _(A)_ | no fee for editing a listing · Pattern-only listings do not expire | there is no fee for editing a listing · whether or not the listed item sells · unless you create a private listing · Etsy.com listings expire after four months. Pattern-only listings do not expire. · the listing will be automatically renewed at $0.20 after each of the items sells |
| `metric_unit` _(A)_ | USD | USD per listing creation/auto-renewal |
| `subject_exact` _(A)_ | Etsy listing fee amount and multi-quantity renewal mechanics | listing fee charged on creation/renewal regardless of sale (private listings charged only on sale), four-month expiry (Pattern listings exempt), $0.20 initial and $0.20 auto-renewal per multi-quantity item sold |
| `time_scope_raw` _(B)_ | Etsy.com listings expire after four months | _(null)_ |
| `uncertainties` _(B)_ | none | _(lista vacia)_ |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016)

**Veredicto:**


---

## Caso 30 — `ER-SP-compass_artifact_wf-83a235d5-86a0-4c10-9097-e29688c3b834_text_markdown_normalized-016-SNP-015`

- **Batch de origen:** batch_022
- **Estrato:** E2

**snippet_primary:**

> "Etsy offers sellers in certain locations the ability to purchase shipping labels to fulfill their orders. The cost of the shipping label will depend on the shipping carrier, and the origin, destination, weight, and dimensions of the package."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(B)_ | _(lista vacia)_ | sellers in certain locations · will depend on the shipping carrier, and the origin, destination, weight, and dimensions of the package |
| `subject_exact` _(A)_ | Etsy shipping label cost basis for sellers in eligible locations | shipping label purchase availability for sellers in certain locations, with cost varying by carrier, origin, destination, weight and dimensions |
| `uncertainties` _(B)_ | geography_unclear | _(lista vacia)_ |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016)

**Veredicto:**


---

## Caso 31 — `ER-SP-compass_artifact_wf-853a5ee8-c8c0-498f-a255-2c1745e85afc_text_markdown-005-SNP-001`

- **Batch de origen:** batch_022
- **Estrato:** E2

**snippet_primary:**

> "This Envato Elements vs Adobe Stock helped me see that the latter comes with a variety of licensing options. Adobe Stock enables me to choose between Standard, Enhanced, and Extended licenses, which allows me to select the most suitable license for my project. Each license covers different usage rights. For instance, the Standard license has up to $10,000 in legal coverage. At the same time, Envato Elements includes only one license type."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(B)_ | _(lista vacia)_ | the Standard license has up to $10,000 in legal coverage · Envato Elements includes only one license type |
| `metric_unit` _(B)_ | USD legal coverage | _(null)_ |
| `metric_value_raw` _(B)_ | $10,000 | _(null)_ |
| `parser_notes` _(B)_ | _(lista vacia)_ | First-person reviewer voice on a review site; treated as commentary source. · source_date approximate ('approximately April 3, 2026'); not normalized. |
| `platforms` _(A)_ | Adobe Stock · Envato Elements | Adobe Stock · Envato |
| `subject_exact` _(A)_ | author comparison of Adobe Stock tiered licensing options versus Envato Elements single license type | licensing comparison: Adobe Stock's Standard/Enhanced/Extended options (Standard with up to $10,000 legal coverage) versus Envato Elements' single license type |
| `uncertainties` _(A)_ | none | source_date_unclear |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016)

**Veredicto:**


---

## Caso 32 — `ER-SP-compass_artifact_wf-a06fe5fe-c286-4184-a6a6-fb33112437d3_text_markdown-001-SNP-001`

- **Batch de origen:** batch_023
- **Estrato:** E2

**snippet_primary:**

> "To get started, visit the seller's store. In some cases, you may be taken directly to a product page or checkout if the seller has shared a direct purchase link.\n\nOnce you're on the seller's store, click on the product you're interested in to view more details. You can either add it to your cart and continue browsing or click Buy Now to proceed directly to checkout.\n\nAt checkout, you'll be asked to enter your email address and select a payment method. You can typically pay using PayPal or a debit or credit card, depending on the seller's setup.\n\nOnce your payment is successful, your purchase is complete. [...] Digital products are delivered instantly after purchase via a download page. [...] Yes. After your purchase, you will receive an email receipt that includes your order details, a download or login link, and the seller's contact email. [...] Sellers will receive basic information needed to fulfill your order, such as your email address and, for physical products, your shipping details. They do not have access to your full payment details."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(A)_ | sellers do not have access to full payment details | depending on the seller's setup · Digital products are delivered instantly after purchase via a download page · They do not have access to your full payment details |
| `metric_type` _(A)_ | payment_method_availability | payment_method_availability |
| `parser_notes` _(B)_ | _(lista vacia)_ | time_scope_normalized_if_safe from source_date_if_available ('Updated March 17, 2026') per criteria G/K1. |
| `platforms` _(A)_ | Payhip | Payhip · PayPal |
| `subject_exact` _(A)_ | Payhip help center description of the buyer checkout and product delivery flow | Payhip buying flow: store/product/checkout navigation, email plus PayPal or card payment per seller setup, instant digital delivery, email receipt, and limited seller access to buyer data |
| `time_scope_normalized_if_safe` _(B)_ | _(null)_ | 2026-03-17 |
| `uncertainties` _(B)_ | none | _(lista vacia)_ |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016)

**Veredicto:**


---

## Caso 33 — `ER-SP-compass_artifact_wf-a4b58711-5a61-40a3-b829-5ddcf0552299_text_markdown-010-SNP-002`

- **Batch de origen:** batch_025
- **Estrato:** E2

**snippet_primary:**

> "All creators still using legacy billing will need to switch to subscription billing by November 1, 2026."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(A)_ | still using legacy billing | All creators still using legacy billing |
| `parser_notes` _(B)_ | _(lista vacia)_ | Platform named only in source_ref URL; platforms left empty per criteria F. |
| `platforms` _(B)_ | Patreon | _(lista vacia)_ |
| `subject_exact` _(A)_ | Patreon deadline for creators to migrate off legacy billing to subscription billing | mandatory migration of all legacy-billing creators to subscription billing by November 1, 2026 |
| `uncertainties` _(A)_ | none | source_date_unclear |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016)

**Veredicto:**


---

## Caso 34 — `ER-SP-compass_artifact_wf-a714e31c-2e2c-4735-a50c-9e9535323a2c_text_markdown-010-SNP-001`

- **Batch de origen:** batch_026
- **Estrato:** E2

**snippet_primary:**

> "Hotmart aplica una comisión por cada venta (típicamente 9,9% + €0,05) y además cobra al retirar tu saldo. Por ejemplo, si retiras entre €50 y €100, pueden quedarse con unos €7,5 adicionales. Traducción: cuanto más vendes, más pagas en comisiones. Thinkific trabaja con tarifa fija. Las pasarelas de pago (Stripe, PayPal, Thinkific Payments) tienen sus propias comisiones por transacción, pero no hay una estructura de comisiones de plataforma que limite tus ingresos al escalar."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(A)_ | cuanto más vendes, más pagas en comisiones | y además cobra al retirar tu saldo · Por ejemplo, si retiras entre €50 y €100, pueden quedarse con unos €7,5 adicionales · cuanto más vendes, más pagas en comisiones · pero no hay una estructura de comisiones de plataforma que limite tus ingresos al escalar |
| `metric_type` _(A)_ | fee_rate · payout | fee_rate |
| `metric_unit` _(A)_ | percent and EUR (mixed, declared) | percent plus EUR flat per sale (mixed units declared) |
| `metric_value_raw` _(A)_ | 9,9% + €0,05 por venta; unos €7,5 adicionales al retirar entre €50 y €100 | típicamente 9,9% + €0,05 |
| `parser_notes` _(A)_ | Per-sale commission and separate withdrawal fee are distinct functional layers (checkout vs payout) combined in the same comparative snippet without full separation by the source. | Additional figure in snippet: withdrawal charge 'unos €7,5' on €50-€100 withdrawals. |
| `subject_exact` _(A)_ | blog author's comparison of Hotmart per-sale and withdrawal fees versus Thinkific's flat-fee model | fee comparison: Hotmart ~9.9% + €0.05 per sale plus withdrawal charges (~€7.5 on €50-€100 withdrawals) versus Thinkific flat fee with only gateway commissions |
| `uncertainties` _(A)_ | checkout_vs_payout_ambiguity | source_date_unclear |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016)

**Veredicto:**


---

## Caso 35 — `ER-SP-compass_artifact_wf-a75564bf-b82a-4c6f-b147-9be329dc5e6f_text_markdown_normalized-004-SNP-001`

- **Batch de origen:** batch_027
- **Estrato:** E2

**snippet_primary:**

> [Stated in layout: "Categorías · Todos · Tamaño · Color · Cantidad · Comprar · Disponibilidad · Compra segura con Garantía Kichink · FORMAS DE PAGO · Tarjetas de Crédito, Débito, efectivo y Kash. Compartir en"]

| Campo | Sonnet | Fable |
|---|---|---|
| `parser_notes` _(B)_ | _(lista vacia)_ | snippet_primary is layout-derived (bracketed reconstruction), not prose verbatim. · Product page is for a digital image ('imagen digital' in URL), but product typing not explicit in the captured layout text. |
| `platforms` _(A)_ | Kichink | Kichink · Kash |
| `subject_exact` _(A)_ | Kichink individual product page layout including accepted payment methods and purchase-guarantee messaging | payment methods shown on a Kichink product page: credit cards, debit, cash and Kash, with 'Garantía Kichink' secure-purchase badge |
| `uncertainties` _(A)_ | none | source_date_unclear |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016)

**Veredicto:**


---

## Caso 36 — `ER-SP-compass_artifact_wf-bae0f41e-e3a0-414a-900e-24a67d70982c_text_markdown-003-SNP-003`

- **Batch de origen:** batch_032
- **Estrato:** E2

**snippet_primary:**

> [Stated in layout: "Name | Category | Average rating | Reviews | Mixed reviews | Price | Sales | Est. Revenue: Old Book Cover & Spread Mockup Design Syndrome | design / graphics | 5.0 ⭐ | 118 | 2% | $13.00 | 20,221 | $262,873.00"]

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(B)_ | _(lista vacia)_ | Est. Revenue |
| `metric_type` _(A)_ | review_count · sales_count · revenue · price | revenue |
| `metric_unit` _(A)_ | stars, count, percent, and USD (mixed, declared) | USD (Est. Revenue) |
| `metric_value_raw` _(A)_ | 5.0 stars; 118 reviews; 2% mixed reviews; $13.00; 20,221 sales; $262,873.00 est. revenue | $262,873.00 |
| `parser_notes` _(A)_ | Single product row combines four distinct metric dimensions with no dominant one; recorded as array. | Additional metrics (criterion H): Sales 20,221; Price $13.00; Reviews 118; Average rating 5.0; Mixed reviews 2%. · Source's explicit category label 'design / graphics' for a mockup design product — product_type 'design_asset'. Estimated figure without stated methodology — methodology_unclear. · Snippet delivered as a layout capture ('[Stated in layout: ...]' is a capture annotation). Platform named only in source_ref — platforms left empty (criterion F). |
| `platforms` _(B)_ | Gumroad | _(lista vacia)_ |
| `subject_exact` _(A)_ | third-party dataset provider's per-product listing example showing rating, reviews, price, sales, and estimated revenue for a single Gumroad product | Gumtrends table row for the product 'Old Book Cover & Spread Mockup Design Syndrome' with rating, reviews, price, sales, and estimated revenue |
| `uncertainties` _(A)_ | none | methodology_unclear |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016)

**Veredicto:**


---

## Caso 37 — `ER-SP-compass_artifact_wf-bbbe6c81-ce19-4446-ada5-416354340fc4_text_markdown-004-SNP-001`

- **Batch de origen:** batch_032
- **Estrato:** E2

**snippet_primary:**

> "No pude bajar un e book que compre en la plataforma y no me respondieron aún. Compre en otras ocasiones y fue todo bien pero en esta compra al contrario."

| Campo | Sonnet | Fable |
|---|---|---|
| `claim_type` _(A)_ | review_statement | anecdotal_report |
| `local_qualifiers` _(A)_ | compre en otras ocasiones y fue todo bien pero en esta compra al contrario | Compre en otras ocasiones y fue todo bien pero en esta compra al contrario |
| `parser_notes` _(B)_ | _(lista vacia)_ | 'e book' named explicitly — product_type 'ebook'. Platform named only in source_ref, not in snippet text ('la plataforma') — platforms left empty (criterion F). |
| `platforms` _(B)_ | Hotmart | _(lista vacia)_ |
| `subject_exact` _(A)_ | buyer's complaint about being unable to download a purchased ebook on Hotmart with no support response | buyer unable to download a purchased ebook from the platform with no response yet, after previous purchases went well |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016)

**Veredicto:**


---

## Caso 38 — `ER-SP-compass_artifact_wf-bbbe6c81-ce19-4446-ada5-416354340fc4_text_markdown-010-SNP-001`

- **Batch de origen:** batch_033
- **Estrato:** E2

**snippet_primary:**

> "No dia 25/04 comprei o curso, Ruptura Viral IA, do produtor *****, esse curso veio incompleto, está faltando a aula \"Vídeo Dark Horizontal - Animando e Gerando Narração (Parte 04)\", na descrição das aulas tem vários comentários de outros alunos relatando a falta da aula, eu mandei mensagem e email para o ***** e suporte, sem resposta, tentei contato com a Hotmart que também não dá suporte a esse tipo de problema, a Hotmart apenas passa o email do produtor, que não responde ninguém, vi reclamação de outras pessoas com o mesmo relato, o curso está incompleto."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(A)_ | other students reported the same missing lesson in comments, per buyer | está faltando a aula "Vídeo Dark Horizontal - Animando e Gerando Narração (Parte 04)" · na descrição das aulas tem vários comentários de outros alunos relatando a falta da aula · a Hotmart apenas passa o email do produtor, que não responde ninguém |
| `parser_notes` _(A)_ | Buyer states Hotmart support redirected them to the seller's email, which went unanswered. | product_type fuera de enum: 'curso' named explicitly — observed value recorded verbatim (K5). · 'No dia 25/04' has no year in the snippet — not normalized (K2); the year in source_date would be an inference. |
| `product_type_if_explicit` _(A)_ | unknown | curso |
| `subject_exact` _(A)_ | buyer-reported incomplete course content (missing lesson) on Hotmart-hosted product with no seller response | buyer received the course 'Ruptura Viral IA' missing a lesson, with producer and support unresponsive and Hotmart only forwarding the producer's email |
| `time_scope_raw` _(B)_ | _(null)_ | No dia 25/04 |
| `uncertainties` _(A)_ | subject_ambiguity | anecdotal_single_source |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032)

**Veredicto:**


---

## Caso 39 — `ER-SP-compass_artifact_wf-bbbe6c81-ce19-4446-ada5-416354340fc4_text_markdown-019-SNP-002`

- **Batch de origen:** batch_033
- **Estrato:** E2

**snippet_primary:**

> "Ordered digital course from creator via Hotmart platform. When accessing the course it was empty. Asked for a refund same day. Which the bot processed straight away. Refund showed pending on my accoun..."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(A)_ | refund shown as pending per buyer | When accessing the course it was empty · Asked for a refund same day. Which the bot processed straight away |
| `parser_notes` _(A)_ | Snippet truncated with '...'; final refund outcome not available in captured text. | product_type fuera de enum: 'digital course' named explicitly — observed value recorded verbatim (K5). · Snippet cuts mid-word ('pending on my accoun...') — flagged snippet_needs_reopen (K8). |
| `product_type_if_explicit` _(A)_ | unknown | digital course |
| `subject_exact` _(A)_ | buyer-reported empty digital course content on Hotmart, refund request auto-processed by support bot | buyer of a digital course via Hotmart found it empty and requested a same-day refund, processed immediately by the bot and showing pending |
| `uncertainties` _(A)_ | context_insufficient | anecdotal_single_source · snippet_needs_reopen |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032)

**Veredicto:**


---

## Caso 40 — `ER-SP-compass_artifact_wf-bc6f268c-aeb6-4040-a1a6-8670888bb92f_text_markdown-011-SNP-001`

- **Batch de origen:** batch_034
- **Estrato:** E2

**snippet_primary:**

> [Stated in layout: "All categories · Vectors Print Templates Presentation Templates Logo Templates Graphics Add-ons Web Elements Fonts Icons Game Assets Infographics Textures T-Shirts ePublishing Isolated Objects · Browse New Browse Bestsellers Show more"]

| Campo | Sonnet | Fable |
|---|---|---|
| `parser_notes` _(B)_ | _(lista vacia)_ | All items are category labels — excluded from platforms (K3). Snippet delivered as a layout capture (K10). Platform named only in source_ref — platforms left empty (criterion F). |
| `platforms` _(B)_ | GraphicRiver | _(lista vacia)_ |
| `subject_exact` _(A)_ | GraphicRiver category navigation listing | category list shown on the GraphicRiver all-categories page |
| `time_scope_raw` _(B)_ | Accessed April 2026; page undated | _(null)_ |
| `uncertainties` _(B)_ | none | _(lista vacia)_ |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032)

**Veredicto:**


---

## Caso 41 — `ER-SP-compass_artifact_wf-bc6f268c-aeb6-4040-a1a6-8670888bb92f_text_markdown-013-SNP-001`

- **Batch de origen:** batch_034
- **Estrato:** E2

**snippet_primary:**

> [Stated in layout: "Site Templates (23980)"]

| Campo | Sonnet | Fable |
|---|---|---|
| `metric_type` _(A)_ | themeforest_category_item_count | product count by category |
| `metric_unit` _(A)_ | items | items in category |
| `metric_value_raw` _(A)_ | 23980 | Site Templates (23980) |
| `parser_notes` _(A)_ | metric_type 'themeforest_category_item_count' out_of_enum; same pattern as AudioJungle category counts. | metric_type fuera de enum: per-category item count — descriptor 'product count by category' reused (K5, K10). Snippet delivered as a layout capture. Platform named only in source_ref — platforms left empty (criterion F). |
| `platforms` _(B)_ | ThemeForest | _(lista vacia)_ |
| `subject_exact` _(A)_ | ThemeForest Site Templates category listing count | item count for the Site Templates category on the ThemeForest category page |
| `time_scope_raw` _(B)_ | Accessed April 2026; page undated | _(null)_ |
| `uncertainties` _(B)_ | none | _(lista vacia)_ |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032)

**Veredicto:**


---

## Caso 42 — `ER-SP-compass_artifact_wf-bc6f268c-aeb6-4040-a1a6-8670888bb92f_text_markdown-015-SNP-005`

- **Batch de origen:** batch_034
- **Estrato:** E2

**snippet_primary:**

> [Stated in layout: "All Items Popular Files Featured Files Top New Files Follow Feed Top Authors Top New Authors Public Collections View All Categories"]

| Campo | Sonnet | Fable |
|---|---|---|
| `parser_notes` _(B)_ | _(lista vacia)_ | Snippet delivered as a layout capture (K10). Platform named only in source_ref — platforms left empty (criterion F). |
| `platforms` _(B)_ | ThemeForest | _(lista vacia)_ |
| `subject_exact` _(A)_ | ThemeForest top-sellers page secondary navigation options | navigation options shown on the ThemeForest top-sellers page |
| `time_scope_raw` _(B)_ | Accessed April 2026; page undated | _(null)_ |
| `uncertainties` _(B)_ | none | _(lista vacia)_ |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032)

**Veredicto:**


---

## Caso 43 — `ER-SP-compass_artifact_wf-d45e9141-896e-4a7c-8acd-75d53f883e24_text_markdown-002-SNP-001`

- **Batch de origen:** batch_036
- **Estrato:** E2

**snippet_primary:**

> "For most independent musicians in 2026, Ko-fi is the better starting point. It charges 0% on one-time donations and only 5% on memberships, compared to Patreon's 5-12% plus processing fees. On $500 in monthly fan support, a Ko-fi Gold creator keeps roughly $475 while a Patreon Pro creator nets around $400. However, Patreon wins on community-building tools and structured membership tiers."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(B)_ | _(lista vacia)_ | For most independent musicians in 2026, Ko-fi is the better starting point · However, Patreon wins on community-building tools and structured membership tiers |
| `metric_unit` _(A)_ | percent | % of fan support |
| `metric_value_raw` _(A)_ | Ko-fi: 0% one-time donations, 5% memberships; Patreon: 5-12% plus processing; on $500/mo, Ko-fi Gold nets ~$475 vs Patreon Pro ~$400 | Ko-fi: 0% on one-time donations and only 5% on memberships; Patreon: 5-12% plus processing fees |
| `parser_notes` _(B)_ | _(lista vacia)_ | Additional derived figures (criterion H): 'On $500 in monthly fan support, a Ko-fi Gold creator keeps roughly $475 while a Patreon Pro creator nets around $400'. · Explicit year 'in 2026' scoping the comparison — normalized '2026' (criterion G). |
| `subject_exact` _(A)_ | third-party article fee comparison between Ko-fi and Patreon with worked take-home examples | Ko-fi's 0% fee on one-time donations and 5% on memberships versus Patreon's 5-12% plus processing fees, with a $500/month keep-rate example, and Patreon's advantage in community tools |
| `time_scope_raw` _(A)_ | 2026 | in 2026 |
| `uncertainties` _(B)_ | none | _(lista vacia)_ |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032)

**Veredicto:**


---

## Caso 44 — `ER-SP-compass_artifact_wf-d45e9141-896e-4a7c-8acd-75d53f883e24_text_markdown-021-SNP-001`

- **Batch de origen:** batch_037
- **Estrato:** E2

**snippet_primary:**

> "Patreon gives you a direct line of access to your fan community, with no ads or gatekeepers in the way. Through real-time group chats, comments, DMs, and even directly over email, you can connect more deeply and directly with your community here than anywhere else."

| Campo | Sonnet | Fable |
|---|---|---|
| `claim_type` _(A)_ | explicit_claim | comparative_commentary |
| `local_qualifiers` _(B)_ | _(lista vacia)_ | with no ads or gatekeepers in the way · you can connect more deeply and directly with your community here than anywhere else |
| `metric_type` _(A)_ | discoverability_claim | unknown |
| `parser_notes` _(B)_ | _(lista vacia)_ | Platform homepage in promotional comparative voice — author_conflict_of_interest_possible (K4); marketing copy assigned direct_claim (K6). |
| `subject_exact` _(A)_ | Patreon homepage marketing claim on direct fan access without ads or gatekeepers | Patreon homepage claim of a direct line to the fan community with no ads or gatekeepers, connecting more deeply than anywhere else via chats, comments, DMs, and email |
| `time_scope_raw` _(B)_ | Accessed April 2026; page undated (homepage) | _(null)_ |
| `uncertainties` _(A)_ | none | author_conflict_of_interest_possible |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032)

**Veredicto:**


---

## Caso 45 — `ER-SP-compass_artifact_wf-d45e9141-896e-4a7c-8acd-75d53f883e24_text_markdown-022-SNP-001`

- **Batch de origen:** batch_037
- **Estrato:** E2

**snippet_primary:**

> "In a nutshell, Patreon is a platform for paying content creators of all types, but it's not really a blogging platform. Substack is designed as a blogging platform, and it's much more intuitive for readers to use as well."

| Campo | Sonnet | Fable |
|---|---|---|
| `actor_level` _(A)_ | platform | seller |
| `evidence_role` _(A)_ | comparative_commentary | direct_claim |
| `local_qualifiers` _(B)_ | _(lista vacia)_ | In a nutshell · it's much more intuitive for readers to use as well |
| `parser_notes` _(B)_ | _(lista vacia)_ | Post is a creator's own announcement on their Patreon page ('Moving to...'), not platform voice — actor 'seller' by who speaks (K7). |
| `subject_exact` _(A)_ | Patreon's own blog post distinguishing Patreon from Substack as not a blogging platform | creator's assessment that Patreon is a platform for paying creators but not really a blogging platform, while Substack is designed for blogging and more intuitive for readers |
| `time_scope_normalized_if_safe` _(B)_ | 2025-07-30 | _(null)_ |
| `time_scope_raw` _(B)_ | July 30, 2025 | _(null)_ |
| `uncertainties` _(B)_ | none | _(lista vacia)_ |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032)

**Veredicto:**


---

## Caso 46 — `ER-SP-compass_artifact_wf-de144e73-98a7-403c-a882-9327b9dbadd2_text_markdown-011-SNP-002`

- **Batch de origen:** batch_038
- **Estrato:** E2

**snippet_primary:**

> "Custom Name Necklace, 18K Gold Plated Name Necklace, Personalized Name Necklace, Birthday Gift for Her, Mother's Day Gift, Gift for Mom — (55,428 reviews), Star Seller — Sale Price $14.05, Original Price $28.11 (50% off), Shop: AnyaShopStudio, Ad, FREE shipping"

| Campo | Sonnet | Fable |
|---|---|---|
| `claim_type` _(A)_ | statistical_data | pricing_statement |
| `evidence_role` _(A)_ | database_fact | observed_platform_state |
| `local_qualifiers` _(A)_ | Star Seller badge · Ad · FREE shipping · Shop: AnyaShopStudio | Star Seller · Ad · FREE shipping |
| `metric_type` _(A)_ | price · review_count | price |
| `metric_unit` _(A)_ | USD; reviews | USD |
| `metric_value_raw` _(A)_ | Sale Price $14.05, Original Price $28.11 (50% off); 55,428 reviews | Sale Price $14.05, Original Price $28.11 (50% off) |
| `parser_notes` _(B)_ | _(lista vacia)_ | product_type fuera de enum: physical product 'Necklace' named explicitly — observed value recorded (K5). · Additional metric (criterion H): '(55,428 reviews)'. Platform named only in source_ref — platforms left empty (criterion F). |
| `platforms` _(B)_ | Etsy | _(lista vacia)_ |
| `product_type_if_explicit` _(A)_ | unknown | necklace |
| `subject_exact` _(A)_ | Etsy jewelry-category search-results single listing: custom name necklace price, discount, and review count | custom name necklace listing at sale price $14.05 from original $28.11 (50% off), with 55,428 reviews, Star Seller status, ad placement, and free shipping |
| `time_scope_raw` _(B)_ | Accessed April 2026; listing undated | _(null)_ |
| `uncertainties` _(B)_ | none | _(lista vacia)_ |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032)

**Veredicto:**


---

## Caso 47 — `ER-SP-compass_artifact_wf-e33b0dbb-828e-4221-b8c5-7bf05bddcdba_text_markdown_normalized-002-SNP-002`

- **Batch de origen:** batch_038
- **Estrato:** E2

**snippet_primary:**

> > "Your customer will be charged: $10 + (0.20 × $10) = $12"
> 
> > "We will charge 5% and will collect the EU VAT amount: (0.05 × $10) + (0.20 × $10) = $2.50"
> 
> > "You will receive the remaining amount: $12 – $2.50 = $9.50 (Note: PayPal will deduct it's fees as well)"
> 
> **Verbatim text (VAT included in price, same scenario):**
> 
> > "Your customer will be charged: $10"
> 
> > "Price before VAT applied: $10 ÷ 1.20 = $8.33"
> 
> > "We will charge 5% and will collect the EU VAT amount: (0.05 × $8.33) + ($10 – $8.33) = $2.09"
> 
> > "You will receive the remaining amount: $10 – $2.09 = $7.91 (Note: PayPal will deduct its fees as well)"

| Campo | Sonnet | Fable |
|---|---|---|
| `evidence_role` _(A)_ | derived_calculation | official_policy |
| `local_qualifiers` _(A)_ | PayPal will deduct its fees as well | Your customer will be charged: $10 + (0.20 × $10) = $12 · We will charge 5% and will collect the EU VAT amount: (0.05 × $10) + (0.20 × $10) = $2.50 · Price before VAT applied: $10 ÷ 1.20 = $8.33 · You will receive the remaining amount: $10 – $2.09 = $7.91 (Note: PayPal will deduct its fees as well) |
| `metric_type` _(A)_ | vat_calculation_example | unknown |
| `metric_unit` _(B)_ | USD | _(null)_ |
| `metric_value_raw` _(B)_ | VAT on top: charged $12, Payhip+VAT collected $2.50, seller receives $9.50; VAT included: charged $10, Payhip+VAT collected $2.09, seller receives $7.91 | _(null)_ |
| `parser_notes` _(A)_ | metric_type 'vat_calculation_example' has no enum match for a worked tax-calculation illustration; recorded as out_of_enum literal. | Illustrative worked example with mixed components (price, 5% fee, 20% VAT) — formulas preserved verbatim in qualifiers; metric_type left 'unknown' (no single claimed metric). · The heading '**Verbatim text (VAT included in price, same scenario):**' is a capture annotation, not page prose. Policy help doc with last-updated February 21, 2026 — normalized 2026-02-21 (K1). 'PayPal' is a payment processor — excluded (K3). |
| `platforms` _(B)_ | Payhip · PayPal | _(lista vacia)_ |
| `subject_exact` _(A)_ | Payhip worked VAT-calculation examples comparing VAT-added-on-top versus VAT-included-in-price scenarios | worked examples of a $10 sale with 20% VAT and 5% platform fee: VAT-added ($12 charged, $9.50 to seller) versus VAT-included ($10 charged, $7.91 to seller), before PayPal fees |
| `time_scope_raw` _(B)_ | Last updated February 21, 2026 | _(null)_ |
| `uncertainties` _(B)_ | none | _(lista vacia)_ |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032)

**Veredicto:**


---

## Caso 48 — `ER-SP-compass_artifact_wf-e33b0dbb-828e-4221-b8c5-7bf05bddcdba_text_markdown_normalized-007-SNP-001`

- **Batch de origen:** batch_039
- **Estrato:** E2

**snippet_primary:**

> > "At this point in time, Payhip does not automatically process payouts for affiliates. The sellers handle the payments to affiliates themselves. We make this process easier for them though. We provide monthly affiliate sales reports that include the PayPal email of the affiliate and the commission they earned for each month."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(B)_ | _(lista vacia)_ | The sellers handle the payments to affiliates themselves · We make this process easier for them though |
| `metric_type` _(A)_ | payout_method_availability | unknown |
| `parser_notes` _(B)_ | _(lista vacia)_ | time_scope_raw 'At this point in time' is relative — normalized left null (criterion G). 'PayPal' is a payment processor — excluded (K3). |
| `subject_exact` _(A)_ | Payhip affiliate payout handled manually by sellers, with Payhip providing monthly commission reports | no automatic affiliate payouts by the platform, with sellers paying affiliates themselves aided by monthly affiliate sales reports including PayPal emails and commissions |
| `time_scope_raw` _(A)_ | Undated | At this point in time |
| `uncertainties` _(B)_ | none | _(lista vacia)_ |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032)

**Veredicto:**


---

## Caso 49 — `ER-SP-compass_artifact_wf-e33b0dbb-828e-4221-b8c5-7bf05bddcdba_text_markdown_normalized-013-SNP-003`

- **Batch de origen:** batch_039
- **Estrato:** E2

**snippet_primary:**

> > "Square is available in Australia, Canada, France, Ireland, Japan, Spain, United Kingdom, and the United States."

| Campo | Sonnet | Fable |
|---|---|---|
| `geography_if_explicit` _(A)_ | Australia · Canada · France · Ireland · Japan · Spain · United Kingdom · United States | Australia, Canada, France, Ireland, Japan, Spain, United Kingdom, and the United States |
| `metric_unit` _(B)_ | _(null)_ | countries |
| `metric_value_raw` _(B)_ | _(null)_ | available in Australia, Canada, France, Ireland, Japan, Spain, United Kingdom, and the United States |
| `parser_notes` _(B)_ | _(lista vacia)_ | geography verbatim country list. Page undated — not normalized (K1). 'Square' is a payment service — excluded from platforms (K3). Platform named only in source_ref — platforms left empty (criterion F). |
| `platforms` _(B)_ | Payhip · Square | _(lista vacia)_ |
| `subject_exact` _(A)_ | Payhip-documented Square gateway country coverage | Square availability in eight listed countries |
| `time_scope_raw` _(B)_ | Undated | _(null)_ |
| `uncertainties` _(B)_ | none | _(lista vacia)_ |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032)

**Veredicto:**


---

## Caso 50 — `ER-SP-compass_artifact_wf-e33b0dbb-828e-4221-b8c5-7bf05bddcdba_text_markdown_normalized-020-SNP-001`

- **Batch de origen:** batch_040
- **Estrato:** E2

**snippet_primary:**

> > "The standard PayU fee for online transactions ranges from 2% per transaction depending on your country/region and where your customer is paying from. Note that these fees are collected by PayU and do not go to Payhip."

| Campo | Sonnet | Fable |
|---|---|---|
| `local_qualifiers` _(A)_ | fees collected by PayU, not Payhip · varies by country/region and customer location | depending on your country/region and where your customer is paying from · these fees are collected by PayU and do not go to Payhip |
| `metric_unit` _(A)_ | percent | % per transaction |
| `metric_value_raw` _(A)_ | 2% | ranges from 2% per transaction |
| `parser_notes` _(B)_ | _(lista vacia)_ | Pricing state claim with explicit last-updated December 17, 2025 and null raw — normalized (K1). 'PayU' is a payment service — excluded (K3). |
| `platforms` _(A)_ | Payhip · PayU | Payhip |
| `subject_exact` _(A)_ | Payhip-documented PayU gateway transaction fee rate | PayU standard online transaction fee ranging from 2% per transaction depending on country/region, collected by PayU not Payhip |
| `time_scope_raw` _(B)_ | Last updated December 17, 2025 | _(null)_ |
| `uncertainties` _(B)_ | none | _(lista vacia)_ |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032)

**Veredicto:**


---

## Caso 51 — `ER-SP-compass_artifact_wf-e33b0dbb-828e-4221-b8c5-7bf05bddcdba_text_markdown_normalized-026-SNP-001`

- **Batch de origen:** batch_040
- **Estrato:** E2

**snippet_primary:**

> > "Payhip is secure. We don't store card details - all payments are handled by Paypal and Stripe."

| Campo | Sonnet | Fable |
|---|---|---|
| `claim_type` _(A)_ | explicit_claim | policy_statement |
| `local_qualifiers` _(B)_ | _(lista vacia)_ | Payhip is secure |
| `parser_notes` _(B)_ | _(lista vacia)_ | Page undated (footer copyright is not a content date) — not normalized (K1). 'Paypal'/'Stripe' are payment services — excluded (K3). |
| `platforms` _(A)_ | Payhip · PayPal · Stripe | Payhip |
| `subject_exact` _(A)_ | Payhip security claim on not storing card details, delegating handling to PayPal/Stripe | no card details stored by the platform, with all payments handled by PayPal and Stripe |
| `time_scope_raw` _(B)_ | Undated (footer copyright 2026) | _(null)_ |
| `uncertainties` _(B)_ | none | _(lista vacia)_ |

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
| `local_qualifiers` _(A)_ | for EU VAT purposes in respect of digital products · payment card details never collected by Payhip | Your payment card details are never collected by Us · for EU VAT purposes in respect of digital products · All information We hold about you is stored on secure servers in the EU |
| `metric_type` _(A)_ | data_retention_duration | data retention period |
| `metric_value_raw` _(A)_ | 10 years | for 10 years from the date of the transaction |
| `parser_notes` _(A)_ | metric_type out_of_enum: data retention duration has no matching controlled-vocabulary value | metric_type fuera de enum: personal-data retention window — descriptor 'data retention period' (K5). · geography verbatim 'in the EU'. Page undated — not normalized (K1). Platform named only in source_ref — platforms left empty (criterion F). |
| `platforms` _(B)_ | Payhip | _(lista vacia)_ |
| `subject_exact` _(A)_ | Payhip transaction data retention period for EU VAT purposes | payments handled by the selected processor with no card details collected, transaction data retained 10 years for EU VAT purposes, and all data stored on secure servers in the EU |
| `time_scope_raw` _(B)_ | from the date of the transaction | _(null)_ |
| `uncertainties` _(B)_ | none | _(lista vacia)_ |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016), S6 (desde batch_040), S7 (desde batch_040), S8 (desde batch_040)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032), K13 (desde batch_040), K14 (desde batch_040)

**Veredicto:**


---

## Caso 53 — `ER-SP-compass_artifact_wf-e68dd732-3da5-44dc-ac62-efdb81f1bdc1_text_markdown-002-SNP-002`

- **Batch de origen:** batch_041
- **Estrato:** E3

**snippet_primary:**

> [Stated in layout: "30% Per transaction when new customers find and buy from you through our discover marketplace."]

| Campo | Sonnet | Fable |
|---|---|---|
| `metric_unit` _(A)_ | percent | % per transaction |
| `metric_value_raw` _(A)_ | 30% | 30% Per transaction |
| `parser_notes` _(A)_ | Discover fee (30%) is distinct from direct/profile fee (10%+$0.50); not collapsed into one figure | Snippet delivered as a layout capture (K10). Page undated — not normalized (K1). Platform named only in source_ref — platforms left empty (criterion F). |
| `platforms` _(B)_ | Gumroad | _(lista vacia)_ |
| `subject_exact` _(A)_ | Gumroad Discover marketplace per-transaction fee rate | fee of 30% per transaction when new customers find and buy through the discover marketplace |
| `time_scope_raw` _(B)_ | Accessed April 2026; page undated | _(null)_ |
| `uncertainties` _(B)_ | source_date_unclear | _(lista vacia)_ |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016), S6 (desde batch_040), S7 (desde batch_040), S8 (desde batch_040)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032), K13 (desde batch_040), K14 (desde batch_040)

**Veredicto:**


---

## Caso 54 — `ER-SP-compass_artifact_wf-f65accb1-75e2-4cb1-be7d-0d01a8fabf93_text_markdown-002-SNP-001`

- **Batch de origen:** batch_044
- **Estrato:** E3

**snippet_primary:**

> "1. Be a seller in a country with a cross-border minimum > $10 (e.g. Argentina, Colombia, South Korea, Paraguay) 2. Visit Settings → Payments 3. Change any field (e.g. update bank account) and save 4. The country's exchange-rate-dependent minimum is now persisted as your payout_threshold_cents 5. If the exchange rate drops, your threshold stays at the old higher value"

| Campo | Sonnet | Fable |
|---|---|---|
| `evidence_role` _(A)_ | reported_event | observed_platform_state |
| `geography_if_explicit` _(A)_ | Argentina · Colombia · South Korea · Paraguay | Argentina, Colombia, South Korea, Paraguay |
| `local_qualifiers` _(B)_ | _(lista vacia)_ | Be a seller in a country with a cross-border minimum > $10 · If the exchange rate drops, your threshold stays at the old higher value |
| `metric_type` _(A)_ | payout | unknown |
| `metric_unit` _(B)_ | USD | _(null)_ |
| `metric_value_raw` _(B)_ | minimum > $10 | _(null)_ |
| `parser_notes` _(A)_ | GitHub issue reproduction steps for a payout_threshold_cents bug affecting cross-border minimum countries | geography from the snippet's example list of affected countries ('e.g. Argentina, Colombia, South Korea, Paraguay'). Actor 'seller' per assignment_rule (seller_forum-typed GitHub issue, seller-side reporter). Gumroad named only in source_ref — platforms left empty (criterion F). |
| `platforms` _(B)_ | Gumroad | _(lista vacia)_ |
| `subject_exact` _(A)_ | reported Gumroad bug: cross-border payout threshold not updating when exchange rate drops | bug report: saving any payments-settings field persists the country's exchange-rate-dependent cross-border minimum as payout_threshold_cents, which stays at the old higher value if the exchange rate drops |
| `time_scope_normalized_if_safe` _(B)_ | 2026-02-27 | _(null)_ |
| `time_scope_raw` _(B)_ | February 27, 2026 | _(null)_ |
| `uncertainties` _(A)_ | none | anecdotal_single_source |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016), S6 (desde batch_040), S7 (desde batch_040), S8 (desde batch_040)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032), K13 (desde batch_040), K14 (desde batch_040)

**Veredicto:**


---

## Caso 55 — `ER-SP-compass_artifact_wf-f678b42a-32e6-4c77-b539-89b40c493fbb_text_markdown-009-SNP-004`

- **Batch de origen:** batch_045
- **Estrato:** E3

**snippet_primary:**

> [Contenido de tabla; múltiples subagentes confirman la fila: Escenario 2 — Productor: cualquier país excepto México — Comprador: México — Responsable: Hotmart gestiona impuestos y emite facturas]

| Campo | Sonnet | Fable |
|---|---|---|
| `evidence_role` _(A)_ | database_fact | official_policy |
| `local_qualifiers` _(B)_ | _(lista vacia)_ | Productor: cualquier país excepto México |
| `parser_notes` _(A)_ | Snippet is a table row reconstructed from multiple subagent passes per skeleton metadata | Snippet delivered as a table-row capture with provenance note ('múltiples subagentes confirman la fila') — capture annotation, not page prose (K10). Two conditional effective dates on the page — not normalized (K2 spirit). |
| `subject_exact` _(A)_ | Hotmart tax-management responsibility scenario: Mexico buyer, any-other-country seller (Hotmart responsible) | scenario 2 table row: for buyers in Mexico with producers in any other country, Hotmart manages taxes and issues invoices |
| `time_scope_raw` _(B)_ | Efectivo desde 1 de enero de 2024 (algunos países) / 1 de abril de 2025 (demás países) | _(null)_ |
| `uncertainties` _(B)_ | time_scope_unclear | _(lista vacia)_ |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016), S6 (desde batch_040), S7 (desde batch_040), S8 (desde batch_040)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032), K13 (desde batch_040), K14 (desde batch_040)

**Veredicto:**


---

## Caso 56 — `ER-SP-compass_artifact_wf-fbf25436-287d-411c-be97-ee28c335a4a4_text_markdown-003-SNP-002`

- **Batch de origen:** batch_045
- **Estrato:** E3

**snippet_primary:**

> "I purchased a digital product on Gumroad for approximately $200. The seller failed to deliver the product properly, and I could not access the content from the day of purchase. The link/pages were unavailable and did not function. I contacted the seller many times, but they stopped responding and provided no solution at all. I then contacted Gumroad support and provided full evidence, including screenshots, purchase receipts, and the entire message history. Gumroad repeatedly told me to contact the seller directly and refused to intervene, even though their own policy states that Gumroad may step in when a seller does not respond for 30 days."

| Campo | Sonnet | Fable |
|---|---|---|
| `evidence_role` _(A)_ | reported_event | anecdotal_example |
| `local_qualifiers` _(A)_ | their own policy states that Gumroad may step in when a seller does not respond for 30 days | I could not access the content from the day of purchase · Gumroad repeatedly told me to contact the seller directly and refused to intervene · their own policy states that Gumroad may step in when a seller does not respond for 30 days |
| `metric_type` _(A)_ | refund_policy | unknown |
| `metric_unit` _(B)_ | USD | _(null)_ |
| `metric_value_raw` _(B)_ | $200 | _(null)_ |
| `parser_notes` _(B)_ | _(lista vacia)_ | Purchase amount 'approximately $200' kept implicit in subject; main claim is the non-delivery and support refusal (criterion H). |
| `subject_exact` _(A)_ | buyer complaint that Gumroad declined to intervene on undelivered digital product despite 30-day non-response policy (BBB filing) | buyer of a ~$200 digital product with non-functioning access links, an unresponsive seller, and Gumroad support refusing to intervene despite its stated 30-day non-response policy |
| `time_scope_normalized_if_safe` _(B)_ | 2025-07-10 | _(null)_ |
| `time_scope_raw` _(B)_ | July 10, 2025 (complaint filed); charges on May 8 and June 5, 2025 | _(null)_ |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016), S6 (desde batch_040), S7 (desde batch_040), S8 (desde batch_040)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032), K13 (desde batch_040), K14 (desde batch_040)

**Veredicto:**


---

## Caso 57 — `ER-SP-compass_artifact_wf-fbf25436-287d-411c-be97-ee28c335a4a4_text_markdown-005-SNP-001`

- **Batch de origen:** batch_046
- **Estrato:** E3

**snippet_primary:**

> "The worst shopping experience I've ever had. I tried 4 different cards from different banks – either the bank declines the transaction because it considers Gumroad suspicious, or the website itself says the card isn't supported. What exactly isn't supported? It's a regular international VISA card from a major European bank. How do you even operate like this?"

| Campo | Sonnet | Fable |
|---|---|---|
| `claim_type` _(A)_ | review_statement | anecdotal_report |
| `geography_if_explicit` _(B)_ | European | _(null)_ |
| `local_qualifiers` _(B)_ | _(lista vacia)_ | either the bank declines the transaction because it considers Gumroad suspicious, or the website itself says the card isn't supported · It's a regular international VISA card from a major European bank |
| `metric_type` _(A)_ | payment_method_availability | unknown |
| `metric_value_raw` _(B)_ | 4 different cards from different banks | _(null)_ |
| `parser_notes` _(B)_ | _(lista vacia)_ | 'VISA' is a card network — excluded from platforms (K3). 'major European bank' describes the card issuer, not the claim's geography — geography left null. |
| `subject_exact` _(A)_ | Trustpilot buyer complaint that international VISA cards are declined or unsupported at Gumroad checkout | buyer whose 4 cards from different banks all failed — banks declining Gumroad as suspicious or the site rejecting a regular international VISA card as unsupported |
| `time_scope_normalized_if_safe` _(B)_ | 2025-11-19 | _(null)_ |
| `time_scope_raw` _(B)_ | November 19, 2025 | _(null)_ |
| `uncertainties` _(A)_ | none | anecdotal_single_source |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016), S6 (desde batch_040), S7 (desde batch_040), S8 (desde batch_040)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032), K13 (desde batch_040), K14 (desde batch_040)

**Veredicto:**


---

## Caso 58 — `ER-SP-compass_artifact_wf-fbf25436-287d-411c-be97-ee28c335a4a4_text_markdown-005-SNP-003`

- **Batch de origen:** batch_046
- **Estrato:** E3

**snippet_primary:**

> "Trying to download bought fiels ... Download speed of gumroad <10kB/s ... you have to sit for hours trying to download 100MB that take verywhere els just a second ... and it cancels the download every few minutes... unable to get my purchase ... and i checked ... if i go somewhere else like steam i download at 100MB/s"

| Campo | Sonnet | Fable |
|---|---|---|
| `claim_type` _(A)_ | review_statement | anecdotal_report |
| `local_qualifiers` _(B)_ | _(lista vacia)_ | you have to sit for hours trying to download 100MB · it cancels the download every few minutes |
| `metric_type` _(A)_ | unknown | download speed |
| `metric_unit` _(A)_ | mixed (kB/s / MB/s) | kB/s vs MB/s |
| `metric_value_raw` _(A)_ | <10kB/s vs ~100MB/s on Steam | Download speed of gumroad <10kB/s ... if i go somewhere else like steam i download at 100MB/s |
| `parser_notes` _(B)_ | _(lista vacia)_ | metric_type fuera de enum: observed download throughput — descriptor 'download speed' (K5); mixed units declared. · The inline '...' are the reviewer's own writing style, not capture truncation — not flagged under K8. Steam named as the comparison service — included (K3). |
| `platforms` _(A)_ | Gumroad | Gumroad · Steam |
| `subject_exact` _(A)_ | Trustpilot buyer complaint of very slow, repeatedly-interrupted file download speed on Gumroad | buyer unable to retrieve a purchase due to Gumroad download speeds under 10kB/s with repeated cancellations, versus 100MB/s downloads elsewhere like Steam |
| `time_scope_normalized_if_safe` _(B)_ | 2025-11-19 | _(null)_ |
| `time_scope_raw` _(B)_ | November 19, 2025 | _(null)_ |
| `uncertainties` _(A)_ | none | anecdotal_single_source |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016), S6 (desde batch_040), S7 (desde batch_040), S8 (desde batch_040)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032), K13 (desde batch_040), K14 (desde batch_040)

**Veredicto:**


---

## Caso 59 — `ER-SP-compass_artifact_wf-fbf25436-287d-411c-be97-ee28c335a4a4_text_markdown-005-SNP-004`

- **Batch de origen:** batch_046
- **Estrato:** E3

**snippet_primary:**

> "I purchased a book, but seller did not even upload it so I could download. Gumroad never gave me a refund. THis is how Scam works."

| Campo | Sonnet | Fable |
|---|---|---|
| `claim_type` _(A)_ | review_statement | anecdotal_report |
| `local_qualifiers` _(B)_ | _(lista vacia)_ | seller did not even upload it so I could download · THis is how Scam works |
| `metric_type` _(A)_ | refund_policy | unknown |
| `parser_notes` _(B)_ | _(lista vacia)_ | Downloadable book purchase — product_type 'ebook'. |
| `subject_exact` _(A)_ | Trustpilot buyer complaint of no refund after seller failed to upload purchased file | buyer of a book the seller never uploaded for download, with no refund given by Gumroad |
| `time_scope_normalized_if_safe` _(B)_ | 2025-11-19 | _(null)_ |
| `time_scope_raw` _(B)_ | November 19, 2025 | _(null)_ |
| `uncertainties` _(A)_ | none | anecdotal_single_source |

**Criterios vigentes en este batch:**

- Sonnet — S1 (desde batch_008), S2 (desde batch_008), S3 (desde batch_008), S4 (desde batch_016), S5 (desde batch_016), S6 (desde batch_040), S7 (desde batch_040), S8 (desde batch_040)
- Fable — K1 (desde batch_008), K2 (desde batch_008), K3 (desde batch_008), K4 (desde batch_008), K5 (desde batch_008), K6 (desde batch_008), K7 (desde batch_008), K8 (desde batch_016), K9 (desde batch_016), K10 (desde batch_032), K11 (desde batch_032), K12 (desde batch_032), K13 (desde batch_040), K14 (desde batch_040)

**Veredicto:**


---

## Caso 60 — `ER-SP-domestika_d3_output-004-SNP-001`

- **Batch de origen:** batch_048
- **Estrato:** E3

**snippet_primary:**

> [Stated in layout: "Cursos en promoción"]

| Campo | Sonnet | Fable |
|---|---|---|
| `claim_type` _(A)_ | explicit_claim | availability_statement |
| `parser_notes` _(A)_ | Bare page-header label, no further content captured | Snippet delivered as a layout capture (K10). Actor 'marketplace' per assignment_rule (search_results_page). Platform named only in source_ref — platforms left empty (criterion F). |
| `platforms` _(B)_ | Domestika | _(lista vacia)_ |
| `subject_exact` _(A)_ | Domestika "on sale" course-catalog page header | on-sale courses section header ('Cursos en promoción') on the Domestika courses site |
| `time_scope_raw` _(B)_ | Accessed April 2026; page undated | _(null)_ |
| `uncertainties` _(B)_ | context_insufficient | _(lista vacia)_ |

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

