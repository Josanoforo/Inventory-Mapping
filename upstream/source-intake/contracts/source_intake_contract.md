# Source Intake Contract v0.1

## 1. Purpose

Transformar outputs de **deep search** y hallazgos exploratorios en **Source Packets** separados por fuente, con suficiente estructura para que Data Extraction pueda trabajar sobre ellos sin depender de síntesis prematura.

Source Intake **no extrae records finales**.
Source Intake **no compara fuentes**.
Source Intake **no decide tensiones**.
Source Intake **no formula hallazgos de mercado**.

Su función es:

- separar por fuente
- conservar trazabilidad
- bajar compresión
- preservar snippets y contexto local
- registrar incertidumbres
- preparar material para Data Extraction

---

## 2. Inputs

Puede recibir:

- output de deep search
- listas de fuentes
- snippets encontrados por búsqueda
- notas de hallazgos exploratorios
- metadatos de fuente
- enlaces / refs a artículos, blogs, docs, páginas de pricing, foros, reviews, etc.

### Restricción crítica
Si el input ya viene como:
- “varias fuentes dicen…”
- “hay una contradicción entre…”
- “el patrón general es…”

Source Intake **no debe aceptar eso como Source Packet directo**.

Debe:
- o romperlo de vuelta por fuente,
- o marcarlo como no usable / parking lot,
- o pedir re-apertura de fuentes.

---

## 3. Output

La salida canónica es un conjunto de **Source Packets**.

### Unidad de salida
**Un Source Packet = una sola fuente + sus snippets locales relevantes + metadata + incertidumbres.**

No:
- un resumen de varias fuentes
- una comparación entre plataformas
- una mini tesis

Sí:
- una fuente concreta
- con evidencia local preservada

---

## 4. Qué sí hace

Permitido:

- identificar fuentes individuales
- deduplicar refs obvias
- registrar metadata básica
- extraer snippets relevantes del output de deep search
- agrupar snippets solo si pertenecen a la misma fuente
- adjuntar contexto local suficiente
- registrar posibles subjects / actors / metrics como **tentativos**
- marcar incertidumbres
- priorizar para source-first si hace falta
- exportar Source Packets estructurados

---

## 5. Qué no hace

Prohibido:

- fusionar múltiples fuentes en un solo packet
- producir claims cross-source
- decidir que algo contradice otra fuente
- decir que algo es una tensión
- decir que algo es una oportunidad
- interpretar importancia
- convertir snippets en una narrativa sintética
- normalizar agresivamente
- resolver ambigüedad funcional

---

## 6. Canonical Output Schema (conceptual)

Cada Source Packet debe contener, como mínimo:

- `packet_id`
- `source_id`
- `source_title`
- `source_type`
- `source_ref`
- `source_date_if_available`
- `author_or_actor_if_available`
- `retrieval_method`
- `retrieved_from`
- `raw_search_context`
- `snippets[]`
- `possible_subjects[]`
- `possible_actor_levels[]`
- `possible_metric_types[]`
- `possible_time_scopes[]`
- `possible_geographies[]`
- `uncertainties[]`
- `priority_for_source_first`
- `intake_notes`
- `traceability_status`

---

## 7. Field Definitions

### `packet_id`
ID único del Source Packet.

### `source_id`
ID único de la fuente.
Si la fuente no tiene ID estable, crear uno local y consistente.

### `source_title`
Título visible o label útil de la fuente.

### `source_type`
Valores sugeridos:
- platform_doc
- help_center
- pricing_page
- policy_page
- blog
- article
- reddit
- seller_forum
- buyer_review
- marketplace_listing
- interview
- video_transcript
- pdf
- unknown

### `source_ref`
URL, path, document ref o identificador local.

### `source_date_if_available`
Fecha visible o recuperable.
Si no está clara, dejar `null` y marcar incertidumbre.

### `author_or_actor_if_available`
Ejemplo:
- platform
- seller handle
- reviewer
- blog author
- interviewer
- unknown

### `retrieval_method`
Cómo llegó esta fuente.
Valores sugeridos:
- deep_search
- manual_search
- follow_up_query
- reopened_source
- imported_reference

### `retrieved_from`
Referencia al batch o corrida de deep search de donde vino.

### `raw_search_context`
Texto mínimo que preserve cómo apareció el hallazgo en deep search.
No es para análisis. Es para auditoría.

### `snippets[]`
Lista de snippets locales relevantes de esa misma fuente.

Cada snippet debería incluir:
- `snippet_id`
- `snippet_text`
- `context_before`
- `context_after`
- `location_pointer`

### `possible_subjects[]`
Subjects tentativos, no finales.
Sirven como ayuda para Data Extraction.
Ejemplo:
- `Gumroad Discover activation requirement`
- `PayPal as checkout method in Gumroad`
- `Creative Market seller commission base rate`

### `possible_actor_levels[]`
Valores sugeridos:
- buyer
- seller
- product
- marketplace
- source
- mixed
- unknown

### `possible_metric_types[]`
Tentativos, no finales.
Ejemplo:
- fee_rate
- revenue
- payout
- search_discovery
- active_buyers
- payment_method_availability

### `possible_time_scopes[]`
Wording temporal tentativo si aparece:
- monthly
- lifetime
- April 2026
- since October 2024
- first 6 months
- unknown

### `possible_geographies[]`
Solo si aparece o se infiere con mucha seguridad desde la fuente local.

### `uncertainties[]`
Ejemplos:
- source_date_unclear
- checkout_vs_payout_ambiguity
- current_vs_historical_ambiguity
- source_type_unclear
- context_insufficient
- snippet_needs_reopen

### `priority_for_source_first`
Valores sugeridos:
- high
- medium
- low

Regla:
- `high` para claims sensibles, contradictorios, cuantitativos o policy-critical
- `medium` para hallazgos prometedores pero no críticos
- `low` para contexto periférico

### `intake_notes`
Notas operativas, no interpretativas.
Ejemplo:
- “Source packet likely useful for contradiction audit”
- “Date visible but scope unclear”
- “May need reopening for exact payout vs checkout distinction”

### `traceability_status`
Valores:
- complete
- partial
- weak

---

## 8. Quality Rules

### Rule 1
**Un Source Packet nunca mezcla fuentes.**

### Rule 2
**Los snippets mandan.**
Si un packet no tiene snippets locales útiles, no es packet bueno.

### Rule 3
**Posibles subjects y metrics son ayudas, no verdad final.**
Source Intake puede sugerir, no fijar.

### Rule 4
**No convertir deep search summary en packet canónico.**
Si el output viene ya mezclado, romperlo o rechazarlo.

### Rule 5
**Preservar incertidumbre.**
Si no sabes si PayPal se refiere a checkout o payout, márcalo.

### Rule 6
**Contexto local mínimo, no ensayo.**
No copies medio artículo. Solo lo suficiente para no distorsionar.

---

## 9. Validation Checklist

Un Source Packet pasa si:

- [ ] representa una sola fuente
- [ ] tiene `source_ref`
- [ ] tiene al menos un snippet local usable
- [ ] cada snippet tiene `location_pointer`
- [ ] no contiene síntesis cross-source
- [ ] no hace claims interpretativos
- [ ] conserva incertidumbres reales
- [ ] su trazabilidad es al menos `partial`

---

## 10. Failure Reasons

- `multiple_sources_fused`
- `no_local_snippets`
- `traceability_weak`
- `cross_source_summary_carried_over`
- `source_metadata_missing`
- `snippet_context_missing`
- `possible_subject_overinterpreted`
- `possible_metric_overinterpreted`
- `uncertainty_hidden`

---

## 11. Parking Lot Boundary

Source Intake puede mandar a parking lot solo cuando:

- la fuente parece útil
- pero falta una pieza recuperable
- y esa pieza puede obtenerse con follow-up acotado

Ejemplos:
- falta fecha
- snippet necesita reopening
- source ref parcial
- ambigüedad funcional crítica

No manda a parking lot:
- síntesis cross-source irrecuperable
- fuentes sin trazabilidad real
- outputs demasiado cocinados sin fuente local recuperable

---

## 12. Priority Rules for Source-First

Mandar a `priority_for_source_first = high` si el packet toca:

- fees
- payouts
- pricing
- payment/payout availability
- requirements / thresholds / activation conditions
- policy changes
- contradictory-looking claims
- métricas cuantitativas que sostendrán una TC
- claims que probablemente sobrevivan a Inventory Mapping

Mandar a `medium` si:
- parece prometedor pero no decisivo
- necesita limpieza antes de ser usado fuerte

Mandar a `low` si:
- es contexto útil
- no parece claim crítico
- sirve más como paisaje que como soporte

---

## 13. Success Criterion

Source Intake está funcionando bien si, cuando pasa a Data Extraction:

- hay menos pérdida de trazabilidad
- llegan menos outputs cross-source cocinados
- los claims sensibles ya traen snippets y contexto local
- el extractor tiene que adivinar menos
- baja la tasa de `subject_exact_lost` y `cross_source_synthesis_smuggled`

---

## 14. Human Audit Questions

Para una muestra de Source Packets, pregúntate:

1. ¿Este packet representa una sola fuente o varias?
2. ¿Los snippets sí alcanzan para trabajar localmente?
3. ¿Qué parte del packet es evidencia y qué parte es ayuda tentativa?
4. ¿Hay algo aquí ya demasiado interpretado?
5. ¿Data Extraction podría trabajar sobre esto sin reimaginar la fuente?
6. ¿Vale la pena source-first o basta con este packet?
7. ¿Lo que falta es recuperable o ya está perdido?

---

## 15. Minimal Example

### Bad packet
- packet mezcla dos blogs y un foro
- trae solo una frase tipo “varias fuentes dicen que Gumroad no tiene discoverability”
- no trae snippets locales ni refs precisas

Eso no pasa.

### Better packet
- una sola fuente
- snippets con contexto
- source_ref claro
- possible_subject = `Gumroad Discover activation requirement`
- uncertainty = `time_scope_unclear`
- priority_for_source_first = `high`

Eso sí pasa a Data Extraction.
