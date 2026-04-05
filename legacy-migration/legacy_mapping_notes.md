# Legacy Mapping Notes

Reglas explícitas para mapear valores legacy de `source_type` al sistema canónico nuevo.
Este documento es normativo para el SKILL y es consultado durante la ejecución de migración.

---

## Tabla de mapeo principal

| Legacy value | Canonical source_type | Confidence | Notes |
|---|---|---|---|
| `blog` | `blog` | high | Mapeo directo |
| `article` | `article` | high | Mapeo directo |
| `listing` | `product_listing` | high | Ver regla: listing → product_listing |
| `report` | `report` | high | Ver regla: report es tipo canónico válido |
| `news` | `news` | high | Ver regla: news es tipo canónico válido |
| `benchmark` | *(ver abajo)* | — | Ver regla: benchmark no es source_type |
| `platform_doc` | `platform_doc` | high | Mapeo directo |
| `help_center` | `help_center` | high | Mapeo directo |
| `pricing_page` | `pricing_page` | high | Mapeo directo |
| `policy_page` | `policy_page` | high | Mapeo directo |
| `reddit` | `reddit` | high | Mapeo directo |
| `seller_forum` | `seller_forum` | high | Mapeo directo |
| `buyer_review` | `buyer_review` | high | Mapeo directo |
| `interview` | `interview` | high | Mapeo directo |
| `video_transcript` | `video_transcript` | high | Mapeo directo |
| `pdf` | `pdf` | high | Mapeo directo |
| `unknown` | `unknown` | high | Mapeo directo |
| null / ausente | `unknown` | low | Campo no presente en la legacy card |

---

## Casos especiales

---

### report

**Mapeo recomendado:** `canonical_source_type = report`
**Confidence:** high

`report` es un tipo canónico válido desde el parche de ontología v0.1.
No colapsar a `article`.

**evidence_role sugerido:**
- Si es un informe de análisis de mercado o industria: `comparative_commentary`
- Si es un informe con datos factuales cuantitativos: `direct_claim` o `reported_event`

**Cuándo usar schema_gap:**
Nunca para `report` — ya está en el enum canónico.

**Cuándo usar needs_source_recovery:**
Si `legacy_source_ref_raw` no contiene URL y el informe no es verificable por nombre solo.

---

### news

**Mapeo recomendado:** `canonical_source_type = news`
**Confidence:** high

`news` es un tipo canónico válido desde el parche de ontología v0.1.
No colapsar a `article`.

**evidence_role sugerido:**
- Si el artículo reporta un evento datado: `reported_event`
- Si es noticia de producto o plataforma con cita directa: `direct_claim`

**Cuándo usar schema_gap:**
Nunca para `news` — ya está en el enum canónico.

**Cuándo usar needs_source_recovery:**
Si no hay URL ni publicación identificable con fecha.

---

### listing

**Mapeo recomendado:** `canonical_source_type = product_listing`
**Confidence:** high

La legacy label `listing` se refiere a una página de producto o listado de un vendedor.
`marketplace_listing` no existe en el nuevo enum. Usar `product_listing`.

**evidence_role sugerido:**
- Si el snippet viene de la descripción del vendedor en su propio listing: `seller_self_claim`
- Si es texto de condiciones o políticas del listing: `official_policy` (con cautela — solo si es el vendedor mismo)
- Si es un precio o feature visible en la página: `observed_platform_state`

**Cuándo usar schema_gap:**
Si el listing es de una plataforma y no de un vendedor individual, y la distinción importa pero no es recuperable.

**Cuándo usar needs_source_recovery:**
Si la URL del listing no está disponible y el claim depende de texto de producto específico.

---

### benchmark

**Mapeo recomendado:** inferir desde `legacy_source_ref_raw`
**Confidence:** baja por defecto hasta que se infiera el tipo real

`benchmark` no es un source_type canónico. Es una categoría funcional, no un tipo de fuente.
Siempre disparar: `failure_reasons: ["benchmark_is_not_source_type"]`

**Regla de inferencia:**
Analizar `legacy_source_ref_raw` para determinar el tipo real:

| Referencia legacy contiene | Tipo canónico inferido | Evidence role inferido |
|---|---|---|
| URL de Crunchbase | `database_profile` | `database_fact` |
| URL de SimilarWeb, Semrush, Ahrefs, etc. | `database_profile` | `observed_platform_state` |
| URL de Etsy/marketplace search results | `search_results_page` | `observed_platform_state` |
| URL de blog o artículo de análisis | `article` o `report` | `comparative_commentary` |
| Solo nombre sin URL | confidence = low, type = `unknown` | `unknown` |

**Cuándo usar schema_gap:**
Si la referencia es una herramienta analítica propietaria sin tipo claro en el enum nuevo.

**Cuándo usar needs_source_recovery:**
Si la referencia es solo un nombre (e.g. "SimilarWeb") sin URL, y el dato cuantitativo es relevante para la card.

---

### Crunchbase y bases de datos de empresa

**Mapeo recomendado:**
- `canonical_source_type = database_profile`
- `canonical_evidence_role = database_fact`
- **Confidence:** high si URL de Crunchbase presente; medium si solo nombre

Aplica a: Crunchbase, LinkedIn company pages, Companies House, PitchBook, AngelList, y equivalentes.

**Cuándo usar schema_gap:**
Nunca — `database_profile` ya está en el enum.

**Cuándo usar needs_source_recovery:**
Si el dato (e.g. fecha de fundación, empleados) no tiene URL verificable.

---

### SERP y páginas de resultados de búsqueda

**Mapeo recomendado:**
- `canonical_source_type = search_results_page`
- `canonical_evidence_role = observed_platform_state`
- **Confidence:** high si URL de SERP o marketplace search presente; medium si inferido

Aplica a: Etsy search results, Google Shopping SERP, Amazon search, plataforma search results.

Nota: una SERP no es un product listing. Es una página de resultados.
Si la URL incluye `/market/`, `/search?`, `?q=`, o equivalente, es una SERP.

**evidence_role siempre `observed_platform_state`:**
Un estado visible en la plataforma (cuántos reviews tiene un shop, qué aparece en búsqueda) es un estado observado, no un claim del vendedor ni una política oficial.

**Cuándo usar schema_gap:**
Nunca — `search_results_page` ya está en el enum.

**Cuándo usar needs_source_recovery:**
Si la URL de búsqueda no está disponible y el dato (e.g. número de reviews de un shop) no puede verificarse.

---

### Third-party blog que describe política de plataforma

**Mapeo recomendado:**
- `canonical_source_type = blog`
- `canonical_evidence_role = comparative_commentary` o `reported_event`
- **Confidence:** high para source_type; medium para evidence_role

**Regla crítica:**
Un blog de tercero describiendo fees, pricing o política de una plataforma **nunca** recibe `official_policy`.
`official_policy` es exclusivo de documentos emitidos directamente por la plataforma (help_center, policy_page, platform_doc).

Disparar: `failure_reasons: ["third_party_policy_contamination"]` si la legacy card tenía esta mezcla implícita.

**Cuándo usar needs_source_recovery:**
Si el blog cita una política específica y queremos verificar si esa política todavía está vigente.

---

### Página propia del vendedor / product listing

**Mapeo recomendado:**
- `canonical_source_type = product_listing`
- `canonical_evidence_role = seller_self_claim`
- **Confidence:** high si URL de listing presente

Aplica a: páginas de producto en el sitio propio del vendedor, descripción de template en Gumroad/Etsy/etc.

**Distinción importante:**
- Si el texto es descripción del producto por el vendedor → `seller_self_claim`
- Si el texto es condición de soporte o política del vendedor → `seller_self_claim` también (no `official_policy`)
- `official_policy` aplica solo a documentos de plataforma, no del vendedor individual

**Cuándo usar schema_gap:**
Si el listing mezcla texto del vendedor con texto de la plataforma y no es separable.

---

## Regla general de evidence_role

Cuando el evidence_role no se puede inferir con confianza media o alta:

1. Si hay URL y snippet: asignar el más conservador (e.g. `comparative_commentary` antes que `official_policy`)
2. Si no hay snippet: `unknown` con confidence = low
3. Nunca asignar `official_policy` a fuentes que no sean `platform_doc`, `help_center`, `policy_page` de la propia plataforma

---

## Tabla rápida: evidence_role por source_type canónico

| canonical_source_type | evidence_role más probable | Notas |
|---|---|---|
| `platform_doc` | `official_policy` | Si es doc oficial de la plataforma |
| `help_center` | `official_policy` | Si es help center oficial |
| `pricing_page` | `official_policy` | Si es pricing page oficial |
| `policy_page` | `official_policy` | Si es policy page oficial |
| `blog` | `comparative_commentary` o `anecdotal_example` | Depende de si es análisis o experiencia personal |
| `article` | `comparative_commentary` o `reported_event` | |
| `report` | `comparative_commentary` o `direct_claim` | Depende del tipo de dato |
| `news` | `reported_event` | |
| `reddit` | `anecdotal_example` o `seller_self_claim` | |
| `seller_forum` | `anecdotal_example` o `seller_self_claim` | |
| `buyer_review` | `anecdotal_example` | |
| `product_listing` | `seller_self_claim` o `observed_platform_state` | |
| `database_profile` | `database_fact` | |
| `search_results_page` | `observed_platform_state` | |
| `interview` | `anecdotal_example` o `direct_claim` | Depende del entrevistado |
| `video_transcript` | `anecdotal_example` o `comparative_commentary` | |
| `pdf` | Depende del contenido | Inferir desde contexto |
| `unknown` | `unknown` | |
