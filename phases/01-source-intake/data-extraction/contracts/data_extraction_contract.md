# Data Extraction Contract v0.1

> Serie de reglas: DEC (D-257). Cita canónica: DEC-RN.

## 1. Purpose

Transformar fuentes crudas en **Extraction Records** trazables y localmente coherentes, preservando suficiente estructura para que fases posteriores puedan trabajar sin adivinar:

- qué se dijo
- sobre qué sujeto exacto
- en qué contexto
- con qué métrica o unidad
- en qué temporalidad
- desde qué tipo de fuente
- y qué quedó incierto

Data Extraction **no interpreta el mercado**.
Data Extraction **no construye tensiones**.
Data Extraction **no compara fuentes entre sí**.

Su función es preservar evidencia utilizable sin destruir sus bordes.

---

## 2. Inputs

Tipos de input permitidos:

- páginas web
- artículos
- blogs
- help centers
- documentación de plataforma
- reviews
- foros
- listings
- entrevistas
- transcripciones
- páginas de pricing / policy
- imágenes o capturas, solo si contienen texto necesario
- PDFs, solo si el texto es accesible o puede segmentarse razonablemente

Cada input debe registrarse como **una fuente individual**.
No se permite mezclar múltiples fuentes en una sola extracción.

---

## 3. Output

La salida canónica de esta fase es un conjunto de **Extraction Records**.

### Unidad de salida
**Una extracción = una afirmación localmente coherente + el mínimo contexto necesario para no distorsionarla.**

No:
- un documento completo
- una síntesis del documento
- una comparación de múltiples documentos

Sí:
- un fragmento con claim principal preservado y contexto local suficiente

---

## 4. Qué sí hace

Permitido:

- segmentar una fuente en fragmentos
- detectar si un fragmento contiene una afirmación relevante
- registrar snippet principal
- registrar contexto local mínimo
- etiquetar tipo de fuente
- extraer sujeto exacto
- extraer actor level
- extraer métrica / unidad / timeframe si están explícitos
- preservar qualifiers
- marcar incertidumbres
- exportar records estructurados

---

## 5. Qué no hace

Prohibido:

- comparar múltiples fuentes
- decir que algo contradice otra fuente
- decir que algo es una fricción
- decir que algo sugiere oportunidad
- decir que algo es importante, central o clave
- agrupar por tema
- priorizar
- resumir un patrón cross-source
- convertir contexto en interpretación
- llenar campos con inferencia fuerte cuando la fuente no lo sostiene

Data Extraction no produce:
- Signal Cards
- Tension Candidates
- preguntas de DT
- recomendaciones
- oportunidades de negocio

---

## 6. Canonical Output Schema

Cada **Extraction Record** debe contener, como mínimo:

- `extraction_id`
- `source_id`
- `source_type`
- `source_title`
- `source_ref`
- `source_date_if_available`
- `author_or_actor_if_available`
- `snippet_primary`
- `snippet_context_before`
- `snippet_context_after`
- `claim_type`
- `subject_exact`
- `actor_level`
- `platforms`
- `product_type_if_explicit`
- `metric_type`
- `metric_value_raw`
- `metric_unit`
- `time_scope_raw`
- `time_scope_normalized_if_safe`
- `geography_if_explicit`
- `evidence_role`
- `local_qualifiers`
- `uncertainties`
- `parser_notes`
- `traceability_pointer`

---

## 7. Field Definitions

### `extraction_id`
ID único del record.

### `source_id`
ID único de la fuente de origen.

### `source_type`
Lista cerrada. Exactamente un valor por record. Espeja la taxonomía de `phases/00-data-gathering/reference/data_gathering_project_instructions_v4_5.md` §source_type taxonomy, que es donde se asigna.
- platform_doc
- help_center
- pricing_page
- policy_page
- blog
- article
- report
- news
- reddit
- seller_forum
- buyer_review
- product_listing
- interview
- video_transcript
- pdf
- database_profile
- search_results_page
- unknown

A blog post page that contains an active comment section is classified as `source_type: blog`. The container determines the type. Individual comments are split into separate records per speaker under the single-source rule, but all carry `source_type: blog`.

Una página servida desde un subdominio o ruta de ayuda o soporte de la plataforma bajo estudio se clasifica `help_center`, aunque su contenido tenga forma de artículo o de entrada de blog. El contenedor determina el tipo.

### `source_ref`
Referencia estable a la fuente:
- URL
- ruta de archivo
- identificador interno
- cita documental

### `snippet_primary`
El fragmento principal que contiene la afirmación.

Debe ser lo bastante preciso para recuperar el sentido local.
No debe ser un resumen libre si puede preservarse el wording.

### `snippet_context_before` / `snippet_context_after`
Contexto mínimo necesario para no malinterpretar la afirmación.

### `claim_type`
Enum cerrado. La lista completa y autoritativa vive en `pipeline_vocabulary.yaml`, campo `claim_type` — no se reproduce aquí.

### `subject_exact`
Campo crítico.

Debe nombrar el sujeto de la afirmación con precisión local.

Ejemplos buenos:
- `Gumroad Discover activation requirement`
- `PayPal as checkout payment method in Gumroad`
- `PayPal as seller payout rail in Gumroad`
- `Creative Market seller commission base rate`
- `seller-reported net retained after taxes on Creative Market`

Ejemplos malos:
- `fees`
- `PayPal`
- `traffic`
- `sales`
- `discoverability`

### `actor_level`
Valores permitidos:
- buyer
- seller
- product
- marketplace
- source
- mixed
- unknown

### `platforms`
Lista explícita de plataformas mencionadas.
No inferir si no aparece claramente.

### `product_type_if_explicit`
Solo si la fuente lo dice o lo deja inequívoco.

Ejemplos:
- notion_template
- ebook
- digital_planner
- prompt
- spreadsheet
- unknown

### `metric_type`
Valores sugeridos:
- revenue
- profit
- payout
- fee_rate
- traffic_volume
- active_buyers
- monthly_visitors
- sales_count
- first_sale
- review_requirement
- activation_requirement
- discoverability_claim
- payment_method_availability

No lo dejaría libre completamente.
Necesitas enums o al menos catálogo controlado.

### `evidence_role`
Esto te puede salvar muchísimo downstream.

Valores:
- direct_claim
- local_context
- downstream_consequence
- anecdotal_example
- official_policy
- comparative_commentary
- derived_calculation
- seller_self_claim
- reported_event
- database_fact
- observed_platform_state
- unknown

Esto ayuda a no tratar todo como soporte directo.

---

## 8. Allowed Operations

Data Extraction puede:

1. Registrar metadata de la fuente
2. Segmentar la fuente en fragmentos
3. Identificar si un fragmento contiene una afirmación relevante
4. Construir un Extraction Record
5. Validar completitud y trazabilidad
6. Exportar records estructurados

---

## 9. Forbidden Operations

Data Extraction no puede:

1. Resolver contradicciones
2. Agrupar varias fuentes en un solo record
3. Crear claims sintéticos cross-source
4. Asignar importancia
5. Decir que algo implica oportunidad
6. Traducir evidencia a estrategia
7. Convertir tema en tensión
8. Borrar qualifiers por “limpieza”
9. Inventar normalización si el dato no lo permite

---

## 10. Extraction Quality Rules

### DEC-R1 (Rule 1)
**No colapsar capas funcionales.**
Ejemplos:
- checkout ≠ payout
- fee base ≠ net retained
- active buyers ≠ seller discoverability
- platform traffic ≠ seller sales outcome

### DEC-R2 (Rule 2)
**No convertir contexto en claim.**
Ejemplo:
“95.6M active buyers” puede ser contexto, no prueba directa de discoverability integrada seller-side.

### DEC-R3 (Rule 3)
**No borrar qualifiers.**
Si el fragmento dice:
- “at the time of writing”
- “in the US”
- “for shops under $10k”
- “within first 6 months”

deben preservarse.

### DEC-R4 (Rule 4)
**No resolver ambigüedad: marcarla.**
Unknown > inferencia bonita.

### DEC-R5 (Rule 5)
**Un Extraction Record no mezcla fuentes.**
Nunca.

### DEC-R6 (Rule 6)
**No resumir demasiado pronto.**
Preservar wording cuando sea posible.

---

## 11. Validation Checklist

Un Extraction Record pasa si:

- [ ] tiene `source_id`
- [ ] tiene `snippet_primary`
- [ ] tiene `traceability_pointer`
- [ ] tiene `subject_exact`
- [ ] tiene `actor_level` o `unknown`
- [ ] no mezcla múltiples fuentes
- [ ] no contiene interpretación estratégica
- [ ] preserva qualifiers relevantes
- [ ] no inventa métrica, unidad o temporalidad
- [ ] deja incertidumbres explícitas cuando aplica

---

## 12. Failure Reasons

Usa razones claras, por ejemplo:

- `source_not_traceable`
- `subject_exact_lost`
- `actor_level_collapsed`
- `metric_type_mixed`
- `time_scope_missing`
- `qualifier_dropped`
- `context_as_claim`
- `cross_source_synthesis_smuggled`
- `multiple_claims_fused`
- `evidence_role_unclear`
- `source_type_unclear`

---

## 13. Failure Taxonomy to Track

Esta taxonomía no es solo para fallar records. También te sirve para auditar el sistema después.

- `subject_exact_lost`
- `actor_level_collapsed`
- `metric_type_mixed`
- `time_scope_missing`
- `official_vs_anecdotal_flattened`
- `direct_claim_vs_context_mixed`
- `cross_source_synthesis_smuggled`
- `qualifier_dropped`
- `derived_summary_without_traceable_snippet`

---

## 14. Upstream / Downstream Boundaries

### Upstream of Data Extraction
- Source Intake
- Source registration
- metadata básica

### Downstream of Data Extraction
- Signal Extraction
- Inventory Mapping
- candidate building
- human review

Data Extraction entrega material estructurado.
No decide qué sobrevive como señal o tensión.

---

## 15. Minimal Example

### Bad Record
- subject_exact: `PayPal in Gumroad`
- claim_type: `contradiction`
- snippet_primary: `PayPal fees apply`
- evidence_role: `direct_claim`

Problemas:
- sujeto demasiado ancho
- claim_type ya interpreta
- no distingue checkout vs payout
- no preserva ambigüedad

### Better Record
- `subject_exact`: `PayPal included in effective fee calculation for Gumroad sale`
- `claim_type`: `derived_calculation`
- `snippet_primary`: `including PayPal or Stripe processing fees...`
- `source_type`: `blog`
- `source_date_if_available`: `April 2026`
- `actor_level`: `marketplace`
- `metric_type`: `fee_calculation_component`
- `evidence_role`: `comparative_commentary`
- `uncertainties`: [
  `whether PayPal refers to checkout or payout`,
  `source may be outdated`
  ]
- `traceability_pointer`: `...`

---

## 16. Decision Boundary

Si una extracción requiere demasiada interpretación para completarse, no se “embellece”.

Se debe:
- marcar como incierta,
- o fallarla con razón explícita.

---

## 17. Success Criterion

Data Extraction está funcionando bien si, en fases posteriores, disminuyen estos problemas:

- comparaciones entre sujetos ambiguos
- mezcla de niveles de análisis
- pérdida de temporalidad
- policy vs anecdote flattening
- contexto tratado como soporte directo
- TCs con `rework` por unidad analítica sucia

---

## 18. Human Audit Questions

Para auditar una muestra de Extraction Records, pregúntate:

1. ¿Qué dice exactamente este record?
2. ¿Sobre qué sujeto exacto?
3. ¿Desde qué tipo de fuente?
4. ¿En qué nivel de análisis?
5. ¿Qué métrica usa y en qué unidad?
6. ¿Qué temporalidad tiene?
7. ¿Qué qualifiers preservó?
8. ¿Qué incertidumbres dejó visibles?
9. ¿Convirtió contexto en claim?
10. ¿Estoy leyendo una fuente preservada o una reinterpretación elegante?
