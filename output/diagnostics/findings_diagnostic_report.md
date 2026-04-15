# Findings Diagnostic Report — Dataset Completo

**Total findings en `working/data_gathering/findings/`:** 1178

## T1. Distribución por plataforma (dominio de `source`)

| Dominio               | Findings |
| --------------------- | -------- |
| trustpilot.com        | 104      |
| domestika.org         | 61       |
| help.payhip.com       | 55       |
| payhip.com            | 50       |
| etsy.com              | 47       |
| help.hotmart.com      | 41       |
| kichink.com           | 39       |
| gumroad.com           | 36       |
| help.etsy.com         | 32       |
| hotmart.com           | 30       |
| docs.lemonsqueezy.com | 30       |
| support.patreon.com   | 30       |
| support.domestika.org | 28       |
| es.trustpilot.com     | 28       |
| help.gumroad.com      | 21       |
| (otros)               | 546      |
| **TOTAL**             | 1178     |

*Dominios únicos totales: 259*

## T2. Distribución por Part

| Part      | Findings | % del total |
| --------- | -------- | ----------- |
| 1         | 668      | 56.7%       |
| 2         | 510      | 43.3%       |
| **TOTAL** | 1178     | 100.0%      |

## T3. Distribución por `source_type`

| source_type                            | Findings |
| -------------------------------------- | -------- |
| help_center                            | 189      |
| blog                                   | 187      |
| buyer_review                           | 116      |
| article                                | 105      |
| policy_page                            | 100      |
| platform_doc                           | 65       |
| unknown                                | 63       |
| pricing_page                           | 52       |
| product_listing                        | 46       |
| search_results_page                    | 44       |
| help_article                           | 44       |
| seller_forum                           | 40       |
| database_profile                       | 33       |
| report                                 | 33       |
| investigative_report                   | 18       |
| blog_post                              | 11       |
| marketplace_tool                       | 8        |
| news                                   | 5        |
| feature_page                           | 4        |
| review_platform                        | 2        |
| industry_news                          | 2        |
| social_media                           | 2        |
| platform_help                          | 2        |
| terms_page                             | 2        |
| interview                              | 1        |
| platform_doc (official forum response) | 1        |
| developer_community                    | 1        |
| privacy_page                           | 1        |
| faq_page                               | 1        |
| **TOTAL**                              | 1178     |

*Valores distintos: 29*

## T4. Distribución por `verification_status`

| verification_status        | Findings |
| -------------------------- | -------- |
| direct_verified            | 671      |
| blocked_url_index_verified | 507      |
| **TOTAL**                  | 1178     |

*9 finding(s) con campo multi-línea — normalizado a primera línea.*

## T5. Distribución por fecha (año extraído de `date`)

| Año       | Findings |
| --------- | -------- |
| 2011      | 1        |
| 2016      | 4        |
| 2017      | 7        |
| 2018      | 5        |
| 2019      | 3        |
| 2020      | 12       |
| 2021      | 13       |
| 2022      | 14       |
| 2023      | 17       |
| 2024      | 88       |
| 2025      | 263      |
| 2026      | 663      |
| (sin año) | 88       |
| **TOTAL** | 1178     |

*Findings sin año extraíble: 88 de 1178 (7.5%)*

## T6. Concentración de fuentes (URLs únicas)

| Métrica                        | Valor |
| ------------------------------ | ----- |
| Total findings                 | 1178  |
| URLs únicas (`source`)         | 642   |
| Ratio findings / URL           | 1.83  |
| URLs con exactamente 1 finding | 427   |
| URLs con 2–5 findings          | 191   |
| URLs con 6–10 findings         | 16    |
| URLs con >10 findings          | 8     |

### Top 20 URLs por frecuencia de findings

| URL (≤85 chars)                                                   | Findings |
| ----------------------------------------------------------------- | -------- |
| https://www.kichink.com/legales/terminos                          | 18       |
| https://www.domestika.org/en/terms                                | 18       |
| https://www.etsy.com/legal/fees/                                  | 18       |
| https://www.trustpilot.com/review/gumroad.com                     | 17       |
| https://gumroad.com/pricing                                       | 12       |
| https://www.classcentral.com/report/domestika-unpaid-instructors/ | 11       |
| https://www.trustpilot.com/review/www.patreon.com                 | 11       |
| https://gumroad.com/terms                                         | 11       |
| https://www.trustpilot.com/review/www.envato.com                  | 10       |
| https://www.trustpilot.com/review/lemonsqueezy.com?page=5         | 9        |
| https://www.trustpilot.com/review/www.etsy.com                    | 9        |
| https://veloxthemes.com/blog/polar-vs-lemonsqueezy-vs-gumroad     | 9        |
| https://payhip.com/pricing                                        | 8        |
| https://hotmart.com/en/legal/payments-policy                      | 8        |
| https://help.gumroad.com/article/13-getting-paid                  | 8        |
| https://www.kichink.com/crea-tu-tienda                            | 7        |
| https://docs.lemonsqueezy.com/help/getting-started/fees           | 7        |
| https://www.domestika.org/es/courses                              | 7        |
| https://www.trustpilot.com/review/hotmart.com                     | 7        |
| https://www.domestika.org/es/terms                                | 6        |

## T7. Cobertura por plataforma × direction

| Plataforma    | D1 — Platform mechanics & fee structure | D2 — Seller experience & workarounds | D3 — Catalog, discovery & market signals | D4 — Buyer behavior | D5 — Competitive positioning | D6 — Cross-border LatAm↔US | Total |
| ------------- | --------------------------------------- | ------------------------------------ | ---------------------------------------- | ------------------- | ---------------------------- | -------------------------- | ----- |
| Domestika     | —                                       | 35                                   | 62                                       | 26                  | —                            | 30                         | 153   |
| Envato        | —                                       | —                                    | 25                                       | 24                  | 22                           | 16                         | 87    |
| Etsy          | —                                       | 23                                   | 71                                       | 38                  | 28                           | 20                         | 180   |
| Gumroad       | 24                                      | 23                                   | 28                                       | 21                  | 26                           | 17                         | 139   |
| Hotmart       | 18                                      | 20                                   | 16                                       | 31                  | 28                           | 48                         | 161   |
| Kichink       | 22                                      | —                                    | 11                                       | 4                   | 12                           | 14                         | 63    |
| Lemon Squeezy | 17                                      | 12                                   | 10                                       | 16                  | 33                           | 27                         | 115   |
| Patreon       | 28                                      | 17                                   | 33                                       | —                   | 32                           | —                          | 110   |
| Payhip        | 58                                      | 16                                   | 48                                       | 10                  | 38                           | —                          | 170   |
| **TOTAL**     | 167                                     | 146                                  | 304                                      | 170                 | 219                          | 172                        | 1178  |

*Todos los shard_ids resueltos a plataforma y direction.*
