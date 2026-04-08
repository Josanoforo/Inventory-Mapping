# Signal Extraction Contract v0.1

## 1. Purpose

Transformar **Extraction Records validados** en **Signal Cards** que representen **observaciones discretas, trazables y mínimamente normalizadas**.

Signal Extraction existe para responder:

- ¿qué observaciones útiles pueden preservarse desde el material extraído?
- ¿cómo convertirlas en unidades comparables sin meter interpretación?
- ¿cómo mantener trazabilidad hacia la fuente original?

Signal Extraction **no** existe para:
- explicar el mercado
- sintetizar patrones cross-source
- construir tensiones
- priorizar
- decidir oportunidades
- producir preguntas de DT

---

## 2. Inputs

La fase recibe como input principal:

- `Data Extraction Records`
- `Data Extraction Validation Results`

### Condición de entrada
Solo deben entrar:
- records con `validation_status = pass`
- o `pass_with_flags`

Puede aceptar `rework` solo si hubo corrección explícita y revalidación.

### No debe aceptar
- records `reject`
- records sin trazabilidad suficiente
- records con síntesis cross-source
- records con `subject_exact` destruido
- records que ya traen interpretación downstream

---

## 3. Output

La salida canónica es un conjunto de **Signal Cards**.

### Unidad de salida
**Una Signal Card = una observación discreta, trazable y observacionalmente formulada, derivada de uno o más Extraction Records, pero sin producir meta-observación cross-source.**

Clave:

- puede consolidar un Extraction Record
- puede, en algunos casos, consolidar varios records de la **misma fuente** o del **mismo hecho local**
- no puede producir una síntesis cross-source disfrazada de “señal”

---

## 4. Qué sí hace

Permitido:

- leer Extraction Records validados
- convertir un record en una observación discreta
- reformular levemente para claridad observacional
- preservar trazabilidad a source + extraction
- mantener qualifiers importantes
- mantener actor level, time scope y metric type visibles
- crear Signal Cards mínimamente normalizadas
- marcar incertidumbres heredadas
- separar records que no deben fusionarse
- descartar records que no alcanzan umbral de señal

---

## 5. Qué no hace

Prohibido:

- comparar varias fuentes para concluir algo común
- decir “esto contradice otra fuente”
- decir “se repite varias veces, por lo tanto importa”
- agrupar por tema y llamar eso señal
- formular tensiones
- priorizar
- interpretar causas
- proponer oportunidades
- convertir una ausencia en gap formal de cobertura
- resumir “el mercado” o “las plataformas” desde varias cards
- producir meta-observaciones cross-source

---

## 6. Canonical Output Schema (conceptual)

Cada **Signal Card** debe contener, como mínimo:

- `signal_id`
- `source_record_ids[]`
- `source_ids[]`
- `round`
- `signal_text`
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
- `local_qualifiers[]`
- `uncertainties[]`
- `traceability_pointers[]`
- `normalization_notes[]`
- `extraction_notes[]`

---

## 7. Signal Card principles

### Principle 1
**Una Signal Card debe sonar observacional, no interpretativa.**

Bien:
- “Gumroad Discover requires at least one sale to activate.”
- “A seller reported zero organic views on Gumroad across 25 products.”
- “Creative Market’s terms state a 50% seller commission.”

Mal:
- “This shows Gumroad has a chicken-and-egg growth problem.”
- “This reveals a severe marketplace asymmetry.”
- “This confirms sellers cannot rely on discoverability.”

### Principle 2
**Una Signal Card debe preservar el hecho, no resolverlo.**

Si hay ambigüedad:
- se preserva
- no se corrige imaginariamente

### Principle 3
**Una Signal Card no debe mezclar niveles de análisis sin declararlo.**

Si la señal es:
- buyer-level
- seller-level
- marketplace-level
- product-level

eso debe quedar claro.

### Principle 4
**Una Signal Card no es una mini-síntesis.**

Si para redactarla necesitas hablar de:
- “varias fuentes”
- “el corpus”
- “en general”
- “la mayoría”

ya saliste de fase.

---

## 9. Decision boundary

Signal Extraction debe decidir solo esto:

### A. Convertir a Signal Card
Cuando el record preserva una observación suficientemente discreta y trazable.

### B. Preserve as isolated but weak
Cuando hay algo usable, pero todavía no sólido.

### C. Return to extraction rework
Cuando el record traía algo valioso pero mal preservado.

### D. Reject from signal layer
Cuando no llega al umbral observacional.

---

## 10. Qué sí puede fusionar y qué no

### Puede fusionar
Solo si se trata de:
- el mismo hecho local
- la misma fuente
- el mismo sujeto exacto
- y la fusión no agrega interpretación

Ejemplo permitido:
Dos snippets contiguos de una misma policy page que juntos forman un solo requisito.

### No puede fusionar
- varias fuentes
- varios sellers distintos
- varias plataformas
- varios momentos históricos
- varios claims que ya requieren comparación

Si lo haces, ya estás fabricando señal compuesta.

---

## 11. Validation Checklist

Una Signal Card pasa si:

- [ ] tiene `signal_id`
- [ ] tiene `source_record_ids`
- [ ] tiene trazabilidad suficiente hacia extracción y fuente
- [ ] `signal_text` sigue siendo observacional
- [ ] no contiene interpretación estratégica
- [ ] no mezcla múltiples fuentes de forma sintética
- [ ] preserva `subject_exact`
- [ ] preserva `actor_level`
- [ ] preserva o marca `time_scope`
- [ ] no borra qualifiers relevantes
- [ ] no convierte contexto en claim
- [ ] no convierte una comparación local en conclusión de mercado

---

## 12. Failure reasons

- `signal_not_observational`
- `cross_source_meta_observation`
- `multiple_records_fused_unsafely`
- `subject_exact_lost`
- `actor_level_collapsed`
- `time_scope_dropped`
- `qualifier_dropped`
- `context_promoted_to_signal`
- `downstream_interpretation_smuggled`
- `traceability_weakened`
- `insufficient_discreteness`
- `local_claim_boundary_broken`

---

## 13. Quality rules

### Rule 1
**No usar lenguaje de inferencia.**

Evitar:
- revela
- demuestra
- sugiere que
- confirma que
- implica que
- evidencia una oportunidad
- muestra una tensión

### Rule 2
**No promover contexto a observación principal.**

Ejemplo:
“Etsy has 95.6M active buyers” puede ser señal válida como `traffic_signal`, pero no debe redactarse como “Etsy provides seller discoverability automatically”.

### Rule 3
**No usar el corpus como sujeto.**

Signal Extraction no dice:
- “the corpus shows”
- “sources converge”
- “there is a split between”
- “many sellers report”

Eso es después.

### Rule 4
**Si una señal solo existe porque resumiste demasiado, no es buena señal.**

### Rule 5
**Si una observación depende de una comparación entre fuentes, no pertenece aquí.**

---

## 14. Handoff to Inventory Mapping

Signal Extraction le entrega a Inventory Mapping:

- Signal Cards discretas
- trazables
- observacionales
- con qualifiers y incertidumbres preservadas
- sin agrupación cross-source

Inventory Mapping se encargará luego de:
- detectar patrones
- agrupar
- probar contradicción / fricción / asimetría / hueco
- construir candidatos

Signal Extraction no debe anticiparse a eso.

---

## 15. Success criterion

Signal Extraction está funcionando bien si, en Inventory Mapping, disminuyen estos problemas:

- cards compuestas
- meta-observaciones cross-source coladas
- pérdida de sujeto exacto
- pérdida de actor level
- pérdida de qualifiers
- TCs que fallan porque la “signal” ya venía interpretada
- agrupaciones formadas sobre resúmenes en vez de observaciones discretas

---

## 16. Human audit questions

Para auditar una muestra de Signal Cards, pregúntate:

1. ¿Esta card describe una observación o ya una lectura?
2. ¿Podría existir sin hablar del corpus completo?
3. ¿Preserva el sujeto exacto?
4. ¿Preserva actor level y time scope?
5. ¿Borró qualifiers?
6. ¿Fusionó más de un hecho?
7. ¿Está comparando fuentes sin decirlo?
8. ¿Está haciendo trabajo que le corresponde a Inventory Mapping?

---

## 17. Minimal examples

### Mal ejemplo
“Multiple sellers report that Gumroad lacks discoverability unless creators already have an audience.”

Problemas:
- múltiples sellers
- cross-source synthesis
- ya habla como patrón de mercado

### Mejor ejemplo
“A seller reported that after one year on Gumroad selling Notion templates, most early sales came from their own audience rather than from platform discoverability.”

Eso sí es una observación localizada.

---

## 18. Global rule

Si una Signal Card ya te suena como algo que podría ir directo a Design Thinking, probablemente ya está demasiado cocinada.

La buena Signal Card todavía molesta un poco, porque **preserva borde** en vez de venderte una narrativa.
