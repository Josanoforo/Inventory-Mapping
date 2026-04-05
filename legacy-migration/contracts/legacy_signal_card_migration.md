# Legacy Signal Card Migration Contract v0.1

## 1. Purpose

Auditar y traducir Signal Cards producidas antes del rediseño upstream al sistema nuevo, sin forzarlas directamente al schema canónico.

Este contrato existe para responder, por cada legacy Signal Card:

- si se puede mapear limpiamente al nuevo sistema
- si se puede mapear con flags y advertencias
- si el schema nuevo todavía no la representa bien (schema_gap)
- si necesita recuperación de fuente antes de poder migrar
- o si es irrecuperable

Migración legado **no es validación canónica final**.
Migración legado **no produce Signal Cards nuevas directamente**.
Migración legado **no interpreta el mercado**.
Migración legado **no construye tensiones**.

Su función es: diagnóstico, traducción, y clasificación de recoverability.

---

## 2. Qué es una legacy Signal Card

Una legacy Signal Card es cualquier Signal Card que fue producida:

- antes de que existiera el pipeline Source Intake → Data Extraction → Signal Extraction
- bajo enums o criterios que no corresponden al nuevo sistema ontológico
- sin pasar por el entry gate canónico nuevo
- o sin metadata de fuente estructurada según los nuevos schemas

Las legacy Signal Cards viven en `input/signal_cards_round_*.md` y están indexadas en `working/index/card_index.jsonl`.

---

## 3. Inputs

- Legacy Signal Cards desde `working/index/card_index.jsonl`
- Opcionalmente: `input/signal_cards_round_*.md` para contexto adicional

No requiere:
- Source Packets
- Extraction Records
- Signal Extraction Validation Results

---

## 4. Output

La salida canónica es un conjunto de **Migration Records** en formato JSONL.

### Unidad de salida
**Un Migration Record = una legacy Signal Card + diagnóstico de mappability + propuesta de traducción canónica + clasificación de recoverability.**

No es:
- una Signal Card canónica nueva
- un Extraction Record
- un Source Packet

Es un registro de auditoría y traducción.

---

## 5. Qué sí hace

Permitido:

- leer legacy Signal Cards desde card_index.jsonl
- extraer metadata legacy disponible: source, source_type, evidence_base, url, date
- proponer mapeo canónico de source_type con confianza declarada
- proponer mapeo canónico de evidence_role con confianza declarada
- asignar traceability_grade según disponibilidad de referencia
- asignar recoverability_status
- registrar failure_reasons cuando aplique
- producir Migration Records en JSONL
- actualizar el manifest de migración

---

## 6. Qué no hace

Prohibido:

- validar legacy cards directamente contra signal_card.schema.json
- convertir automáticamente legacy cards a Signal Cards canónicas nuevas
- interpretar importancia de señales
- comparar cards entre sí para detectar patrones
- construir Tension Candidates
- decidir qué pasa a Design Thinking
- hacer narrativa de mercado
- conectar automáticamente con upstream/ ni con input/

---

## 7. Reglas de migración

### Regla 1: No validación directa contra schema canónico
No comparar legacy cards contra `signal_card.schema.json`. El propósito es traducción, no validación.

### Regla 2: Preservar valores legacy crudos
Siempre registrar:
- `legacy_source_type_raw`
- `legacy_evidence_role_raw`
- `legacy_source_ref_raw`
- `legacy_source_label_raw`

Nunca sobrescribir el valor legacy.

### Regla 3: No forzar equivalencias destructivas
Si el mapeo canónico borra procedencia importante, registrar como `mappable_with_flags` o `schema_gap`, no como `clean_mappable`.

### Regla 4: Sin URL ni snippet → no clean_mappable
Si falta URL, snippet verificable o referencia estable, el resultado mínimo es `mappable_with_flags`. Si no hay referencia de ningún tipo, es `needs_source_recovery` o `unrecoverable`.

### Regla 5: Third-party sobre política de plataforma ≠ official_policy
Si una fuente third-party (blog, artículo, guía) describe fees, pricing o policy de una plataforma, nunca clasificar como `official_policy`. Clasificar como `comparative_commentary` o `reported_event`.

### Regla 6: benchmark no es source_type canónico
Si `legacy_source_type_raw = "benchmark"`, disparar `benchmark_is_not_source_type`. Intentar inferir el tipo real desde `legacy_source_ref_raw` o `legacy_source_label_raw`.

### Regla 7: listing → product_listing
Si `legacy_source_type_raw = "listing"`, mapear a `canonical_source_type = product_listing`. No usar `marketplace_listing` (no existe en el nuevo enum).

### Regla 8: Crunchbase y bases de datos de empresas
Mapear a:
- `canonical_source_type = database_profile`
- `canonical_evidence_role = database_fact`

### Regla 9: SERP y páginas de resultados
Mapear a:
- `canonical_source_type = search_results_page`
- `canonical_evidence_role = observed_platform_state`

### Regla 10: report y news son tipos canónicos válidos
No colapsar `report` ni `news` a `article` por defecto. Mapear directamente a sus tipos canónicos correspondientes.

---

## 8. Clasificación de recoverability_status

### `clean_mappable`
La card tiene:
- referencia estable (URL completa o identificador verificable)
- source_type legacy que mapea a un valor canónico con confianza alta o media
- evidence_role inferible con confianza alta o media
- sin failure_reasons críticos

### `mappable_with_flags`
La card es usable pero tiene al menos una de estas condiciones:
- referencia parcial (nombre de fuente sin URL)
- mapeo de source_type con confianza media o baja
- mapeo de evidence_role con confianza media o baja
- un failure_reason no crítico (e.g. `source_ref_partial_only`, `third_party_policy_contamination`)

### `schema_gap`
La card contiene un valor legacy que:
- no existe en el nuevo enum
- no puede mapearse sin crear un tipo nuevo
- o requiere decisión de diseño ontológico antes de migrar

Ejemplos: `benchmark`, tipos muy específicos de plataforma no cubiertos.

### `needs_source_recovery`
La card tiene evidencia de valor potencial pero:
- falta URL o referencia estable
- el snippet no es verificable sin abrir la fuente original
- se requiere follow-up acotado para recuperar la referencia

### `unrecoverable`
La card no puede migrarse porque:
- no tiene referencia de ningún tipo
- la fuente no es trazable ni recuperable
- el snippet o claim no puede verificarse bajo ningún método razonable
- múltiples failure_reasons críticos simultáneos

---

## 9. Checks obligatorios

### `reference_available`
¿Hay alguna referencia de fuente en la legacy card (URL, nombre, label)?

### `reference_stable`
¿Es esa referencia suficientemente estable para ser recuperada o verificada?

### `source_type_mappable`
¿Puede el valor legacy de source_type mapearse a un valor canónico del nuevo enum?

### `evidence_role_mappable`
¿Puede inferirse un evidence_role canónico desde la metadata legacy disponible?

### `snippet_verifiability`
¿El evidence_base o snippet de la legacy card es verificable contra una fuente trazable?

### `legacy_value_requires_enum_extension`
¿El valor legacy requiere un tipo que no existe ni en el enum viejo ni en el nuevo? Si sí, marca `schema_gap`.

---

## 10. Failure reasons de referencia

| Código | Cuándo usarlo |
|---|---|
| `source_ref_missing` | No hay ningún campo de referencia en la legacy card |
| `source_ref_partial_only` | Solo hay nombre de fuente, sin URL ni ref estable |
| `source_not_verifiable` | La referencia existe pero no puede verificarse |
| `source_type_not_in_new_enum` | El valor legacy no tiene equivalente en el nuevo enum |
| `evidence_role_not_in_new_enum` | El evidence_role legacy no tiene equivalente nuevo |
| `benchmark_is_not_source_type` | Legacy usa "benchmark" como source_type |
| `listing_too_broad_for_new_enum` | Legacy "listing" es ambiguo entre tipos canónicos |
| `report_not_in_new_enum` | Aplica solo a versiones viejas anteriores al parche de ontología |
| `news_not_in_new_enum` | Aplica solo a versiones viejas anteriores al parche de ontología |
| `database_source_not_represented` | Fuente es base de datos pero no se puede clasificar limpiamente |
| `serp_source_not_represented` | Fuente es SERP/results page sin representación clara |
| `third_party_policy_contamination` | Blog/artículo de tercero describe política oficial de plataforma |
| `snippet_missing` | No hay evidence_base ni snippet en la legacy card |
| `snippet_not_verifiable` | El snippet existe pero no puede verificarse con la referencia disponible |
| `role_too_ambiguous` | No se puede inferir evidence_role con confianza suficiente |
| `traceability_broken` | La cadena de trazabilidad está rota de forma no recuperable |

---

## 11. Traceability grading

| Grade | Criterio |
|---|---|
| `complete` | URL completa y verificable + snippet identificable |
| `partial` | URL presente pero sin anchor/sección, o nombre de fuente con fecha |
| `weak` | Solo nombre de fuente sin URL ni fecha |
| `none` | Sin referencia de ningún tipo |

---

## 12. Éxito de la migración

La migración está funcionando bien si:
- cada Migration Record preserva el valor legacy crudo sin pérdida
- los mapeos canónicos están justificados y tienen confianza declarada
- los schema_gaps están documentados, no silenciados
- los needs_source_recovery tienen suggested_followup accionable
- no se producen clean_mappable fraudulentos para cards sin URL
