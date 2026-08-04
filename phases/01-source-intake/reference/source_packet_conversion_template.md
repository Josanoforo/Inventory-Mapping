# Source Packet conversion template

> Serie de reglas: SPT (D-257). Cita canónica: SPT-RN.

Conversión manual de findings de Data Gathering a Source Packets validables por el repo. Para usar mientras no exista un script automatizado.

## Qué es esto

Un Source Packet es la unidad que el repo de Inventory-Mapping espera como input para Source Intake. Cada packet representa **una fuente** (una URL o página) con todos sus snippets relevantes y metadata mínima. Downstream, Data Extraction toma el packet y produce records granulares por claim.

Las findings de DG no mapean 1-a-1 a packets. **Múltiples findings de la misma URL colapsan en un solo packet con múltiples snippets.** Eso significa que 50 findings de DG probablemente producen 30-40 packets, no 50.

## El workflow de conversión

Un loop por cada source único en tu output de DG:

1. **Agrupa findings por URL.** Todos los findings que vienen del mismo URL se procesan juntos. Ejemplo de DX-1: Devrim Ozcay tenía Finding 1 (enero $127) y Finding 2 (septiembre $180), ambas del mismo Medium article. Se vuelven UN packet con UN snippet (que contiene los dos meses), no dos packets.

2. **Crea el packet.** Llena los 11 campos packet-level (los mecánicos: ids, URL, tipo, fecha, autor, método, snippets array, intake_notes).

3. **Llena los 8 campos de clasificación.** Basado en lo que el source como un todo trata. Sección "Field-by-field guidance" abajo.

4. **Verifica traceability_status.** Sección "Fallback rules" abajo.

5. **Guarda como .json.** Un archivo por packet, en `working/source_intake/packets/` (o donde Claude Code te confirme que viven los packets — pendiente del mini-prompt de Gap 1).

## El template

Copia esto, llena los placeholders en angle brackets, borra los comentarios `//` antes de guardar como JSON válido.

```jsonc
{
  "packet_id": "SP-<batch>-<###>",        // ej: SP-001-001 (batch 001, packet 001)
  "source_id": "SRC-<batch>-<###>",       // ej: SRC-001-001. Si misma URL aparece en otro packet del mismo batch, mismo source_id
  "source_title": "<page title or article headline>",
  "source_type": "<one of the 18 enum values; same as DG finding source_type>",
  "source_ref": "<full URL>",
  "source_date_if_available": "<YYYY-MM-DD or null>",
  "author_or_actor_if_available": "<seller name / handle / null>",
  "retrieval_method": "<deep_search | gpt_custom | manual_search | unknown>",
  "retrieved_from": "<shard prompt name, or null>",   // ej: "gumroad_DX1_shard_v1"
  "raw_search_context": "<original search query that produced this, or null>",
  "snippets": [
    {
      "snippet_id": "SNP-001",
      "snippet_text": "<verbatim from DG finding>",
      "context_before": null,             // DG no captura contexto, default null
      "context_after": null,
      "location_pointer": {
        "pointer_type": "url",
        "pointer_value": "<URL, with #anchor if available>"
      }
    }
    // si la misma fuente tiene múltiples snippets relevantes, agrega más entradas aquí
  ],
  "possible_subjects": [],                // ver guidance
  "possible_actor_levels": [],            // ver guidance
  "possible_metric_types": [],            // ver guidance
  "possible_time_scopes": [],             // ver guidance
  "possible_geographies": null,           // ver guidance
  "uncertainties": [],                    // ver guidance
  "priority_for_source_first": "medium",  // ver guidance
  "intake_notes": [],                     // free-text array, contexto que no cabe en otros campos
  "traceability_status": "complete"       // ver fallback rules
}
```

## Field-by-field guidance — los 8 campos de juicio

### `possible_subjects`
Array de strings libres. Qué sujeto(s) trata el source. No es taxonomía cerrada, son etiquetas descriptivas en lenguaje natural. Pone los sujetos plausibles, no todos los imaginables.

- Income report de un seller específico → `["seller revenue reporting", "<plataforma> seller economics"]`
- Workflow de producción → `["AI-assisted production workflow", "digital product creation process"]`
- Policy primitive → `["<plataforma> seller policy", "<categoría específica de policy>"]`

Mínimo 1 sujeto. Máximo razonable: 3-4. Si tu lista crece, probablemente estás siendo demasiado granular.

### `possible_actor_levels`
Array. Enum cerrado: `buyer`, `seller`, `product`, `marketplace`, `source`, `mixed`, `unknown`.

- Seller hablando de su propia experiencia → `["seller"]`
- Plataforma documentando policy → `["marketplace"]`
- Article describiendo a un seller → `["seller", "source"]` (porque el source mismo está actuando como capturador)
- Buyer review de un producto → `["buyer", "product"]`
- Cuando hay duda real → `["unknown"]` solo (no mezcles `unknown` con otros valores)

### `possible_metric_types`
Array. Enum cerrado de 20 valores. **Este es el campo donde más vas a usar `unknown`.**

Los valores que sí encajan limpio:
- `revenue` — para income reports
- `fee_rate` — para fee policies
- `price` — para pricing observations
- `sales_count` — para conteo de ventas
- `traffic_volume`, `monthly_visitors`, `active_buyers` — métricas de plataforma
- `payout`, `profit`, `time_to_first_sale`, `first_sale` — métricas seller
- `refund_policy`, `review_requirement`, `activation_requirement` — policy/operational
- `payment_method_availability`, `payout_method_availability` — disponibilidad
- `discoverability_claim`, `search_discovery`, `conversion_rate`, `review_count` — discoverability/conversion

Los workflow findings (DX-2) no encajan en ningún valor del enum. Para ellos: `["unknown"]` y nota en `intake_notes` algo como "Workflow/process finding; metric_type enum does not currently cover production workflow descriptions."

### `possible_time_scopes`
Array de strings libres. Cuándo aplica el dato.

- Mes específico → `["2024-01"]` o `["January 2024"]`
- Rango → `["Jan-Sep 2024"]`
- Annual → `["2024 calendar year"]`
- Snapshot actual → `["current as of <fecha de captura>"]`
- Sin fecha visible → `["undated"]`
- Históricamente estable → `["ongoing"]`

### `possible_geographies`
Array de strings o `null`. Geografía mencionada en el source.

- Si la fuente menciona país/región específica → `["United States"]`, `["Mexico"]`, etc.
- Si menciona múltiples → `["United States", "Canada", "United Kingdom"]`
- Si es global o no menciona geografía → `null` (no array vacío, literal null)
- Si menciona "global" o "worldwide" explícitamente → `["global"]`

### `uncertainties`
Array. Enum cerrado de 13 valores. Qué cosas no están claras sobre este source.

- `source_date_unclear` — si la fecha no es visible o es ambigua
- `source_type_unclear` — si dudaste cómo clasificarlo
- `context_insufficient` — si el snippet por sí solo no se entiende sin más contexto
- `snippet_needs_reopen` — si el snippet podría necesitar verificación adicional
- `checkout_vs_payout_ambiguity` — específico de fees/revenue, si no queda claro qué se mide
- `net_vs_gross_ambiguity` — específico de revenue
- `current_vs_historical_ambiguity` — si no queda claro si el dato es vigente
- `subject_ambiguity` — si dudaste qué clasificar en `possible_subjects`
- `actor_level_unclear` — si dudaste en `possible_actor_levels`
- `metric_type_unclear` — si dudaste en `possible_metric_types` (úsalo siempre que pongas `unknown`)
- `time_scope_unclear` — si dudaste en `possible_time_scopes`
- `geography_unclear` — si dudaste en `possible_geographies`
- `none` — si NO hay incertidumbres. Usa este solo, no lo mezcles con otros.

### `priority_for_source_first`
Un valor: `high`, `medium`, `low`.

Heurística simple:
- `high` — claim claro, snippet limpio, source verificable directo, encaja con alguna direction de DT que ya identificaste
- `medium` — default. Source válido pero no urgente.
- `low` — flagged en DG (notes contamination, paywall partial), o tangencial al pilot

No es ranking de calidad — es ranking de orden en que Data Extraction debería procesarlo si hay budget limit.

### `traceability_status`
Un valor: `complete`, `partial`, `weak`.

Heurística:
- `complete` — URL accesible directo, snippet visible en la página, autor identificable, fecha visible
- `partial` — falta uno de esos cuatro elementos. Ejemplo: snippet visible pero página sin fecha → partial
- `weak` — faltan dos o más, o el snippet vino vía mirror/cache, o el author es pseudónimo no verificable

Equivalencia con DG verification states:
- `direct_verified` en DG → `complete` o `partial` (depende de si la fecha está)
- `indirect_verified` en DG → `complete` (misma confianza epistemológica que direct_verified;
  la limitación es de la herramienta, no de la información; la distinción de método queda
  en el campo verification_status del finding original)
- `blocked_url_index_verified` en DG → `partial` o `weak`
  [DEPRECATED — producido por shards pre-recovery; no aparece en output del recovery agent]
- `could_not_verify` en DG → no debería llegar a esta conversión, queda en Part 4 de DG
  [DEPRECATED — reemplazado por unrecoverable en el recovery agent]
- `unrecoverable` en DG → NO entra al inventario activo de Phase 1. Interceptado en
  working/data_gathering/diagnostics/part_4/ antes de que converter_prepare.py corra.
  El paso route_unrecoverable escribe a working/source_intake/rejected_archive/ con
  reason_code: unrecoverable_after_recovery, preservando los campos attempted y why_failed
  del finding original.

## Fallback rules

Cuando dudes:

1. **SPT-R1 (Regla 1) — Si dudas entre dos valores en un enum cerrado**, pone los dos. Los campos `possible_*` están diseñados para eso.

2. **SPT-R2 (Regla 2) — Si ningún valor del enum encaja**, usa `unknown` (o `null` si el campo lo permite). Nunca inventes valores fuera del enum.

3. **SPT-R3 (Regla 3) — Si una incertidumbre te bloquea**, agrégala a `uncertainties` y continúa con tu mejor estimado en el campo afectado. No bloquees el packet completo por una duda en un campo.

4. **SPT-R4 (Regla 4) — Si el snippet del DG finding no se sostiene sin más contexto** (ej: requiere haber leído el párrafo anterior), marca `context_insufficient` en uncertainties y considera bajar `traceability_status` a `partial`.

5. **SPT-R5 (Regla 5) — Si dudas entre `complete` y `partial`**, default a `partial`. Si dudas entre `partial` y `weak`, default a `weak`. Default conservador, igual que en DG.

6. **SPT-R6 (Regla 6) — Si una finding de DG estaba en Part 2 (provisional) y su `verification_status` es
   `blocked_url_index_verified`**: el packet hereda la incertidumbre: `traceability_status: weak`
   y `snippet_needs_reopen` en uncertainties.
   **EXCEPCIÓN**: si `verification_status` es `indirect_verified` (output del recovery agent),
   aplicar la regla de equivalencia de la sección `traceability_status` (→ `complete`),
   no esta fallback rule. La distinción de método queda en el finding original.

## Worked example — DX-1 Finding 1 (Devrim Ozcay)

Finding original de DG (resumido):

```
Seller: Devrim Ozcay (@devrimozcay on Medium)
Product: Developer PDF guides
Revenue: $127 in January 2024
Source: https://medium.com/write-a-catalyst/my-gumroad-income-breakdown-2-539-...
Source type: blog
Verbatim snippet: "Income Is Extremely Volatile January: $127 March: $45 
  June: $400 September: $180 December: $2,539 It's not a smooth curve. 
  It's chaos. Some months, one person buys a $79 bundle and makes your month."
Verification: direct_verified
Date: Published March 2026, reporting on 2024 calendar year
```

Importante: este finding y DX-1 Finding 2 (mismo seller, septiembre $180) **comparten URL**, así que se convierten en UN solo packet con UN snippet (el snippet ya contiene los datos de los dos meses).

Source Packet resultante:

```json
{
  "packet_id": "SP-001-001",
  "source_id": "SRC-001-001",
  "source_title": "My Gumroad Income Breakdown: $2,539 in Revenue — Here's What Worked",
  "source_type": "blog",
  "source_ref": "https://medium.com/write-a-catalyst/my-gumroad-income-breakdown-2-539-in-revenue-heres-what-worked-c0797855df76",
  "source_date_if_available": "2026-03-15",
  "author_or_actor_if_available": "Devrim Ozcay (@devrimozcay)",
  "retrieval_method": "deep_search",
  "retrieved_from": "gumroad_DX1_shard_v1",
  "raw_search_context": null,
  "snippets": [
    {
      "snippet_id": "SNP-001",
      "snippet_text": "Income Is Extremely Volatile January: $127 March: $45 June: $400 September: $180 December: $2,539 It's not a smooth curve. It's chaos. Some months, one person buys a $79 bundle and makes your month.",
      "context_before": null,
      "context_after": null,
      "location_pointer": {
        "pointer_type": "url",
        "pointer_value": "https://medium.com/write-a-catalyst/my-gumroad-income-breakdown-2-539-in-revenue-heres-what-worked-c0797855df76"
      }
    }
  ],
  "possible_subjects": [
    "Gumroad seller revenue reporting",
    "developer digital product economics"
  ],
  "possible_actor_levels": ["seller"],
  "possible_metric_types": ["revenue"],
  "possible_time_scopes": [
    "January 2024",
    "March 2024",
    "June 2024",
    "September 2024",
    "December 2024",
    "2024 calendar year"
  ],
  "possible_geographies": null,
  "uncertainties": [
    "current_vs_historical_ambiguity",
    "net_vs_gross_ambiguity"
  ],
  "priority_for_source_first": "high",
  "intake_notes": [
    "Article published March 2026 reporting on 2024 data — seller is reporting historical, not current, performance",
    "December $2,539 figure ambiguous: appears in monthly breakdown but matches stated annual total — could be cumulative annual, not December monthly",
    "Snippet covers multiple monthly figures; downstream Data Extraction should split per month per unit-of-observation rule"
  ],
  "traceability_status": "complete"
}
```

Notas sobre las decisiones de juicio en este ejemplo:

- **possible_subjects**: dos etiquetas, una sobre el sujeto general (seller revenue) y una más específica al nicho (developer products). No fui más granular porque el source no lo justifica.
- **possible_metric_types**: `revenue` encaja limpio, no necesité `unknown`.
- **possible_time_scopes**: enumeré cada mes mencionado más el calendar year general. Downstream Data Extraction va a producir un record por mes; el packet debe declarar todos los time scopes posibles.
- **uncertainties**: las dos incertidumbres reflejan ambigüedades reales del source (no sabemos si los figures son net o gross, no sabemos si el seller sigue activo en 2026). Estas son las incertidumbres que el DG finding mismo flaggeó.
- **priority_for_source_first**: high porque es exactamente el tipo de source que importa para tu pregunta y el snippet es limpio.
- **intake_notes**: aquí va el contexto que no cabe en campos cerrados — el detalle del December ambiguity, la nota sobre publicación tardía, la pista para downstream sobre cómo splittear.
- **traceability_status**: complete porque tenemos URL directa, autor identificable, fecha de publicación, y snippet visible.

## Sidebar — workflow findings (caso DX-2)

Para findings de DX-2 (workflows AI-asistidos), el schema tiene un mismatch estructural: `possible_metric_types` no tiene valores para describir workflows de producción.

Tratamiento:

```json
{
  "possible_metric_types": ["unknown"],
  "uncertainties": [
    "metric_type_unclear",
    // resto de uncertainties que apliquen
  ],
  "intake_notes": [
    "Workflow/process finding; metric_type enum in current schema does not cover production workflow descriptions. Captured as unknown.",
    // otras notas
  ]
}
```

Esto es deuda del schema, no del packet. Si el proyecto eventualmente se enfoca en workflows como direction principal, el schema necesita un valor como `production_workflow` o `tool_usage_claim` en el enum. Por ahora, `unknown` + nota explícita en intake_notes preserva la información sin romper validation.

## Convenciones de IDs sugeridas

No están en el schema (ambos packet_id y source_id son strings libres), pero te conviene una convención consistente para no perderte:

- `packet_id`: `SP-<batch>-<###>` donde batch es un código de tu corrida (puede ser fecha, número de sesión, lo que sea). Ejemplo: `SP-2026-04-A-001` para el primer packet de la corrida A del 6 de abril 2026.
- `source_id`: `SRC-<batch>-<###>`. Cuando un source aparece en múltiples packets (no debería pasar dentro de un mismo batch, pero puede pasar entre batches), el source_id se mantiene el mismo. Eso te permite tracking cross-batch.
- `snippet_id`: `SNP-<###>` dentro de cada packet, secuencial empezando en 001. No globalmente único, solo único dentro de su packet.

## Tiempo estimado

Por packet, después de los primeros 5 (cuando ya agarraste ritmo):

- Mecánicos (10 campos): ~1 minuto
- 8 campos de juicio: 2-4 minutos
- Lectura del finding original + decisiones: 1-2 minutos
- **Total por packet:** 4-7 minutos

Para 30-40 packets: **2-4 horas de trabajo manual concentrado**.

Si después del primer batch te das cuenta de que estás repitiendo las mismas decisiones, ese es el momento de escribir un script — vas a tener data real sobre dónde el script puede ahorrar tiempo y dónde sigue requiriendo juicio humano.
