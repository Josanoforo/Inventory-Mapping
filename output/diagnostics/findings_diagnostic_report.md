# Findings Diagnostic Report — Bloque 1

**Generado:** `findings_diagnostic.py`
**Repo root:** `/home/user/Inventory-Mapping`

## Cobertura de archivos cargados

| Directorio | Archivos JSON |
|---|---|
| `working/data_gathering/findings/` | 459 |
| `working/data_gathering/diagnostics/part_4/` | 126 |
| `working/data_gathering/recovery_packets/` (todos los batches) | 259 |
| **Total** | **844** |

> Nota: Las 6 tablas de distribución se calculan sobre el set `findings/` únicamente (los 459 parsados a JSON individual). Los conjuntos de diagnostics/part_4 y recovery_packets se listan en la tabla de cobertura para contexto del conteo total.

## T1. Distribución por plataforma (dominio de `source`)

| Dominio                      | Findings |
| ---------------------------- | -------- |
| help.payhip.com              | 52       |
| domestika.org                | 47       |
| payhip.com                   | 42       |
| etsy.com                     | 36       |
| kichink.com                  | 31       |
| help.etsy.com                | 21       |
| gumroad.com                  | 19       |
| es.trustpilot.com            | 18       |
| hotmart.com                  | 18       |
| trustpilot.com               | 15       |
| support.domestika.org        | 15       |
| classcentral.com             | 12       |
| help.gumroad.com             | 12       |
| help.hotmart.com             | 10       |
| community.etsy.com           | 8        |
| help.erank.com               | 5        |
| gumtrends.com                | 4        |
| insightraider.com            | 4        |
| elespanol.com                | 3        |
| comicsbeat.com               | 3        |
| medium.com                   | 3        |
| thecluttery.com              | 3        |
| storeleads.app               | 3        |
| sketchlikeanarchitect.com    | 2        |
| instructoresonline.es        | 2        |
| threads.com                  | 2        |
| loveeattravelrepeat.com      | 2        |
| sarahsewell.substack.com     | 2        |
| zapier.com                   | 2        |
| 6sense.com                   | 2        |
| press.hotmart.com            | 2        |
| similarweb.com               | 2        |
| koalanda.pro                 | 2        |
| muchainformacion.net         | 1        |
| domestika.pissedconsumer.com | 1        |
| julskitchen.substack.com     | 1        |
| moderngouache.com            | 1        |
| artdesignbytc.com            | 1        |
| yourvisualjournal.com        | 1        |
| facebook.com                 | 1        |
| schmoedraws.substack.com     | 1        |
| lucywernerpr.medium.com      | 1        |
| 80.lv                        | 1        |
| xeladu.medium.com            | 1        |
| lowcontentprofits.com        | 1        |
| natashatynes.substack.com    | 1        |
| jrheimbigner.substack.com    | 1        |
| tarikpierce.com              | 1        |
| bbb.org                      | 1        |
| bolomiller.medium.com        | 1        |
| najfywrites.substack.com     | 1        |
| timomason.substack.com       | 1        |
| edward-foster23.medium.com   | 1        |
| anhnguyenjohn.medium.com     | 1        |
| sandraeide.substack.com      | 1        |
| kiplinger.com                | 1        |
| srcreativestudio.com         | 1        |
| es.quora.com                 | 1        |
| play.google.com              | 1        |
| fullstats.io                 | 1        |
| marketsy.ai                  | 1        |
| putler.com                   | 1        |
| segmetrics.io                | 1        |
| gumforge.reavid.cc           | 1        |
| aveupuk.gumroad.com          | 1        |
| agentcrew.co                 | 1        |
| github.com                   | 1        |
| markethax.com                | 1        |
| tracxn.com                   | 1        |
| pabbly.com                   | 1        |
| pipedream.com                | 1        |
| apps.make.com                | 1        |
| authors.bookfunnel.com       | 1        |
| ordpress.com                 | 1        |
| ordpress.org                 | 1        |
| commoninja.com               | 1        |
| fiverr.com                   | 1        |
| techhubinsider.com           | 1        |
| semrush.com                  | 1        |
| crunchbase.com               | 1        |
| chrome-stats.com             | 1        |
| erank.com                    | 1        |
| marmalead.com                | 1        |
| everbee.io                   | 1        |
| alura.io                     | 1        |
| salesamurai.io               | 1        |
| linkmybooks.com              | 1        |
| blog.marmalead.com           | 1        |

## T2. Distribución por Part

| Part | Findings |
| ---- | -------- |
| 1    | 298      |
| 2    | 161      |

## T3. Distribución por `source_type`

| source_type                            | Findings |
| -------------------------------------- | -------- |
| policy_page                            | 70       |
| help_center                            | 53       |
| help_article                           | 44       |
| blog                                   | 41       |
| buyer_review                           | 34       |
| product_listing                        | 33       |
| pricing_page                           | 27       |
| database_profile                       | 25       |
| search_results_page                    | 24       |
| article                                | 22       |
| investigative_report                   | 18       |
| platform_doc                           | 13       |
| blog_post                              | 11       |
| seller_forum                           | 9        |
| report                                 | 9        |
| marketplace_tool                       | 8        |
| feature_page                           | 4        |
| review_platform                        | 2        |
| industry_news                          | 2        |
| social_media                           | 2        |
| platform_help                          | 2        |
| terms_page                             | 2        |
| platform_doc (official forum response) | 1        |
| developer_community                    | 1        |
| privacy_page                           | 1        |
| faq_page                               | 1        |

*Total valores distintos: 26*

## T4. Distribución por `verification_status`

| verification_status        | Findings |
| -------------------------- | -------- |
| direct_verified            | 301      |
| blocked_url_index_verified | 158      |

*9 finding(s) con campo `verification_status` multi-línea — normalizado a primera línea.*

## T5. Distribución por fecha (año extraído de `date`)

| Año       | Findings |
| --------- | -------- |
| 2011      | 1        |
| 2018      | 2        |
| 2021      | 6        |
| 2022      | 4        |
| 2023      | 8        |
| 2024      | 39       |
| 2025      | 95       |
| 2026      | 243      |
| (sin año) | 61       |

*Findings sin año extraíble: 61 de 459*

## T6. URLs únicas y ratio de colapso

| Métrica | Valor |
|---|---|
| Total findings en `findings/` | 459 |
| URLs únicas (`source`) | 253 |
| Ratio findings / URL | 1.81 |
| URLs con 1 solo finding | 179 |
| URLs con 2-5 findings | 64 |
| URLs con >5 findings | 10 |

### Top 10 URLs por frecuencia de findings

| URL (truncada a 80 chars)                                         | Findings |
| ----------------------------------------------------------------- | -------- |
| https://www.etsy.com/legal/fees/                                  | 18       |
| https://www.domestika.org/en/terms                                | 15       |
| https://www.kichink.com/legales/terminos                          | 15       |
| https://www.classcentral.com/report/domestika-unpaid-instructors/ | 11       |
| https://www.trustpilot.com/review/gumroad.com                     | 11       |
| https://www.domestika.org/es/courses                              | 7        |
| https://payhip.com/pricing                                        | 7        |
| https://gumroad.com/terms                                         | 7        |
| https://es.trustpilot.com/review/hotmart.com?page=5               | 6        |
| https://gumroad.com/pricing                                       | 6        |
