# Pilot 20 — Stratified Sample Selection

**Pilot date:** 2026-04-05
**Total cards in corpus:** 1,561
**Cards selected:** 20

---

## Selection table

| ID | Round | legacy_source_type | Razón de inclusión | Tipo de diversidad representada |
|---|---|---|---|---|
| SC-R1-004 | 1 | blog | Blog sin nombre ni URL — fuente completamente anónima | Trazabilidad débil; blog sin URL; extraction_status=ambiguous |
| SC-R1-010 | 1 | benchmark | "benchmark" como source_type — disparar benchmark_is_not_source_type; solo nombre "Marketsy.ai" sin URL | Schema_gap candidate; benchmark no es tipo canónico; sin URL |
| SC-R1-018 | 1 | news | Publicación nombrada (LaRepublica.es) sin URL completa | News source; nombre de fuente sin URL; needs_source_recovery candidate |
| SC-R1-030 | 1 | other_specified (TikTok self-report) | Tipo legacy completamente fuera de cualquier enum conocido | Enum extension required; anecdotal seller experience; TikTok content |
| SC-R1-031 | 1 | other_specified (absence finding) | "Observed absence" — sin referencia identificable de ningún tipo | Sin referencia; traceability=none; unrecoverable candidate |
| SC-R2-001 | 2 | listing | URL de listing sin https (etsy.com/listing/...) — referencia parcial | Listing → product_listing mapping; partial URL (domain only, no https) |
| SC-R2-019 | 2 | benchmark | Etsy market pages — benchmark con referencia parcial de dominio sin https | Benchmark schema_gap; partial URL; SERP/market page ambiguity |
| SC-R2-111 | 2 | review | Trustpilot sin https (trustpilot.com/...) — partial URL | Buyer review; partial URL without https; anecdotal buyer experience |
| SC-R3-003 | 3 | blog | Analyzify con URL completa https:// — blog con trazabilidad fuerte | Blog con URL completa; clean_mappable candidate; pricing claim |
| SC-R3-014 | 3 | report | InsightFactory con URL completa https:// — report con trazabilidad fuerte | Report tipo canónico; URL completa; clean_mappable candidate |
| SC-R3-102 | 3 | review | Trustpilot con URL completa https:// — buyer review trazable | Review con URL completa; buyer review; complete traceability candidate |
| SC-R3-108 | 3 | forum_post | Etsy Community Forum con URL completa https:// | Forum post tipo legacy; seller experience anecdotal; URL completa |
| SC-R4-001 | 4 | blog | Whop.com citando Reddit — tercero describiendo experiencia de vendedor | Blog citando Reddit; anecdotal seller income; URL completa |
| SC-R4-030 | 4 | report | Customcy.com estudio grande con URL completa | Report con datos cuantitativos; URL completa; clean_mappable candidate |
| SC-R5-034 | 5 | blog | fueler.io con URL completa pero extraction_status=ambiguous | Blog con URL completa pero claim ambiguo; trazabilidad parcialmente rota |
| SC-R6-019 | 6 | blog | Whop.com citando listing de Etsy — tercero describiendo datos de plataforma | Blog citando listing (not direct); third-party; URL completa; round 6 |
| SC-R7-056 | 7 | listing | Gumroad listing con URL https completa | Listing con URL completa; pricing data; round 7; observed_platform_state candidate |
| SC-R8-008 | 8 | blog | Craftybase describiendo fees de Etsy — third_party_policy_contamination | Third-party blog describiendo política de plataforma; contamination case; round 8 |
| SC-R9-016 | 9 | news | Craft Industry Alliance con URL https completa — anécdota documentada | News tipo canónico; URL completa; round 9; anecdotal documented event |
| SC-R10-023 | 10 | report | WordsRated con dominio sin https — partial URL en report | Report round 10; partial URL; needs_source_recovery candidate |

---

## Cobertura de diversidad

**Rounds cubiertos:** 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 (todos los 10 rounds representados)

**Source types legacy cubiertos:**
- blog: 6 cards (SC-R1-004, SC-R3-003, SC-R4-001, SC-R5-034, SC-R6-019, SC-R8-008)
- benchmark: 2 cards (SC-R1-010, SC-R2-019)
- listing: 2 cards (SC-R2-001, SC-R7-056)
- report: 3 cards (SC-R3-014, SC-R4-030, SC-R10-023)
- news: 2 cards (SC-R1-018, SC-R9-016)
- review: 2 cards (SC-R2-111, SC-R3-102)
- forum_post: 1 card (SC-R3-108)
- other_specified (TikTok self-report): 1 card (SC-R1-030)
- other_specified (absence finding): 1 card (SC-R1-031)

**Trazabilidad esperada:**
- URL completa (https://): SC-R3-003, SC-R3-014, SC-R3-102, SC-R3-108, SC-R4-001, SC-R4-030, SC-R5-034, SC-R6-019, SC-R7-056, SC-R8-008, SC-R9-016
- Solo nombre de fuente (sin URL): SC-R1-004, SC-R1-010, SC-R1-018, SC-R1-030, SC-R1-031, SC-R2-019
- URL parcial (dominio sin https): SC-R2-001, SC-R2-111, SC-R10-023

**Casos especiales:**
- benchmark (schema_gap candidate): SC-R1-010, SC-R2-019
- third_party_policy_contamination: SC-R8-008
- absence finding / sin referencia: SC-R1-031
- TikTok / enum extension: SC-R1-030
- anecdotal seller experience: SC-R1-030, SC-R4-001
- buyer review: SC-R2-111, SC-R3-102
- pricing/fees/policy: SC-R8-008, SC-R2-001
