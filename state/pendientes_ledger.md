# Pendientes — Ledger

**Generado:** S29, Run 1. Cosechado de `Decision_Log_consolidado.md` (tabla de cierre de S26),
`Decision_Log_update_session27.md`, `Handoff_session27.md`, `Decision_Log_update_session28.md`,
`Handoff_session28.md`.

**Qué es.** Puente entre el inventario de pendientes (vive en project files) y el estado real
(vive en el repo). Existe porque las dos cosas están en lados distintos y ninguna sesión puede
ver las dos a la vez.

**Regla de uso.** Ninguna decisión se discute hasta que su fila tenga `Estado` resuelto con cita.
Si se discute algo sin eso, el ledger falló y se mata; no se le agregan capas.

**Clases.**
- `hecho` — se cierra verificando el repo. No requiere juicio del operador.
- `decisión` — requiere juicio del operador. La verificación solo la enmarca.
- `parqueo` — no es decidible hoy. Necesita condición explícita de desparqueo, no discusión.

**Dónde se responde.** `CC` = Claude Code contra el repo · `DSC` = conversación DSC (project
files, diseño) · `OP` = solo el operador.

**Columna Estado.** Vacía en Run 1 por diseño. La llena Run 2 con cita literal.

---

## A. Nunca verificados contra el repo actual — objetivo de Run 2

| ID | Enunciado | Clase | Pregunta verificable | Dónde | Estado |
|---|---|---|---|---|---|
| P-094 | Métricas de flujo por fase diferidas. Los contadores de los manifests no discriminan | hecho | ¿Qué escribe métricas a disco hoy? Enumerar todo script que persista contadores, con ruta de salida | CC | sigue-abierto — 6 scripts `.py` escriben manifest por-corrida (`eje4_xlsx_to_json_batch.py`, `part4_to_recovery_packets.py`, `bulk_extract.py`, `extraction_prepare.py`, `converter_prepare.py`, `signal_prepare.py`); sin métrica cross-fase, confirma el diagnóstico original |
| P-092 | Auditoría de atomicidad de Phase 2 ejecutada solo sobre batch_001 | decisión | Enmarque: ¿cuántas cards existen hoy fuera de batch_001? | CC | sigue-abierto — `signal_converter_manifest.json`: `skeletons_processed: 25` = 100% de `batch_001`; `cards_written: 29`; 0 cards fuera de batch_001 |
| P-102 | Falta regla de verificación de ramas en `CLAUDE.md`. Tres casos: `fetch --prune`, trampa de columna Ahead, el relay no borra refs | decisión | Enmarque: ¿`CLAUDE.md` menciona hoy alguna de las tres? | CC | sigue-abierto — `CLAUDE.md` (93 líneas): 0 menciones de `fetch --prune`, "Ahead" o "relay" |
| P-109 | 186 queries del catálogo del eje 4 sin correr. Desbloqueado en S28 | decisión | Enmarque: ¿existe el catálogo de 186 queries en el repo? Ruta y conteo real | CC | sigue-abierto — el `.xlsx` no existe en `main`/`legacy/*`/`preserve/*`; `working/eje4/` no existe; solo script de pre-proceso + contrato del agente, sin correr. Conteo real no verificable desde el repo |
| P-141 | `product_type_unclear` falta en `source_packet.schema.json` y en la prosa de `source_packet_conversion_template.md`, y `vocab_check.py` no puede detectarlo porque con `match: subset` solo reporta valores de más | hecho | ¿En qué archivos aparece `product_type_unclear` hoy, y qué reporta `vocab_check.py` sobre ese campo? | CC | |

**Cerrados en esta corrección (ya hechos, verificados contra el repo — salen de la tabla):**

- **P-075** — cerrado-ya-hecho — `working/data_gathering/diagnostics/qa_notes/`, 59 archivos
- **P-077** — cerrado-ya-hecho — 79 diagnósticos ya clasificados en `working/data_gathering/diagnostics/part_4/` (43 `__F-X05.json` + 36 `__F-X07.json`, cada uno con `verification_status`); 0 refs a `scope_exploration`
- **P-082** — cerrado-ya-hecho — `working/source_intake/source_intake_gpt_recovery/` solo tiene `.gitkeep`, 0 archivos reales

---

## B. Ya verificados en S28 — no requieren Run 2, esperan decisión

| ID | Enunciado | Clase | Qué falta | Dónde | Estado |
|---|---|---|---|---|---|
| P-125 | Regla 5 de `p2-extract-signals/SKILL.md` contradice campo 13 de `signal_converter.md` | hecho | **Decisión tomada en S28, edición pendiente.** Regla 5 → puntero; campo 13 → fuente única con exclusión de metadata y ruteo a `time_scope_raw` | CC | decidido, sin ejecutar |
| P-137 | `extraction_converter.md` rutea fallos a `extraction_gpt_recovery/`, que no existe. El árbol y `CLAUDE.md` dicen `rejected_archive/` | hecho | Edición trivial de una ruta | CC | cerrado — ruta corregida en `extraction_converter.md` a `rejected_archive/`, commit `e0928ed` |
| P-131 | Dos versiones de `Blueprint_Phase_2_Signal_Extraction.md` con la misma pretensión de fuente única | hecho | Retirar una. Vive en project files, no en el repo | DSC | verificado |
| P-133 | El análisis de diferencias de S27 se llamó "health check", término reservado al componente E del Blueprint | hecho | Corrección de término en el registro | DSC | verificado |
| P-126 | `time_scope_raw` sin regla para material mezclado (bloque A, decisión 2a) | decisión | Extraer verbatim y resto a `normalization_notes`, o conservar string completo y marcar contaminación | DSC | verificado |
| P-119 | Múltiples anclajes temporales verbatim en `time_scope_raw` (bloque A, 2b). **Bloquea los 47 batches** | decisión | Concatenar con separador, un ancla y resto a notas, o splittear la card | DSC | verificado |
| P-127 | Condición de override de `actor_level` delega en juicio no acotado (bloque A, 3) | decisión | Eliminar la segunda condición, o acotarla a criterio verificable. No hay criterio propuesto y los casos no existen | DSC | verificado |
| P-128 | Hueco en la tabla de `source_type` para reporte en tercera persona (bloque A, 4). Obligatoria en los 305 records con `actor_level: unknown` | decisión | `source` es el polo seguro; `seller` crea polos falsamente cross-actor | DSC | verificado |
| P-129b | Valores poblados en el corpus vigente caen fuera del enum del schema Y del enum de `pipeline_vocabulary.yaml` simultáneamente — no es divergencia schema-vocab, en estos tres campos ambos enums coinciden exactamente: `actor_level` 15/1178 (`third_party_observer`×10, `creator`×5 — ya señalado como drift de Phase 1 en `phases/02-signal-extraction/modules/signal_converter.md:159`), `product_type_if_explicit` 207/1178 (texto libre, ej. "online courses", "digital_download"), `metric_type` 186/1178. Contraste: `product_type_if_explicit`, `metric_type` y `uncertainties` están 0/29 en Signal Card (`state/output/field_population_signal_cards.md:17,18,26`) contra 207/1178 y 186/1178 fuera de ambos enums, y 155/1178 fuera del enum del vocab (0/1178 fuera del schema), respectivamente, en Extraction Record (`state/output/field_population_extraction_records.md:24,25,33`) | decisión | Re-normalizar los valores fuera de enum en los tres campos (mapear a un valor válido, o agregar los valores recurrentes al enum si son legítimos), o aceptar la pérdida de estructura | DSC | verificado — `state/output/field_population_extraction_records.md:22,24,25` y `state/output/field_population_raw.json` (rama `claude/field-lifecycle-population-audit-a060e7`, Run 3) |
| P-132 | El detector se mergeó sin satisfacer la precondición de calibración de D-212 Carga A. Los tres casos no existen | decisión | Recalibrar contra casos nuevos, o aceptar el detector con limitaciones declaradas | DSC | verificado |
| P-134 | Segunda corrección: no es problema de enum. `evidence_role` aparece en CLEAN FIELDS de `vocab_check.py` (0 divergencia) y la sección OPEN-STRING FIELDS del mismo check reporta `(none)` — no existe en el repo ningún campo donde el vocab declare enum cerrado y el schema lo declare string libre. El hueco es de puente, no de enum: el renombrado a `evidence_base` ocurre en el paso de renderizado a markdown (`signal_to_markdown.py:274`, línea literal `f"Evidence base: {evidence_role}"`), y `card_record.schema.json:47` declara su propio campo `evidence_base` (string libre, sin enum) — con un nombre distinto a `evidence_role`, por lo que `vocab_check.py` nunca lo compara contra el enum de origen (el check empareja por nombre exacto). El valor cruza vía el texto del label; la restricción de enum no cruza porque el puente no lo intenta, no porque el checker lo deje pasar | decisión | Extender el puente para que el enum sobreviva al renderizado (precedente D-126), o aceptar que `evidence_base` quede como texto libre | DSC | verificado — corrida local de `vocab_check.py` (CLEAN FIELDS incluye `evidence_role`; OPEN-STRING FIELDS: `(none)`), confirmado también en runs de CI `30504740061`/`30504959916`; `card_record.schema.json:47`; `signal_to_markdown.py:274`; `state/output/field_lifecycle_card_record_bridge.md:18` (rama `claude/field-lifecycle-population-audit-a060e7`, Run 3) |
| P-139 | Tres campos declarados en `pipeline_vocabulary.yaml` sin ningún campo de schema que los declare: `verification_status`, `allowed_verbs`, `forbidden_language` — reportados por `vocab_check.py` bajo `VOCAB FIELDS WITH NO MATCHING SCHEMA FIELD FOUND` (sección informativa: no gatea el exit code, a diferencia de DIVERGENCIAS y OPEN-STRING FIELDS). `verification_status` es campo obligatorio y central de Phase 0 (`phases/00-data-gathering/reference/data_gathering_project_instructions_v4_5.md`: "Every finding must include... verification_status"; "verification_status must be exactly one of: direct_verified, blocked_url_index_verified, could_not_verify"), pero Phase 0 no tiene ningún `*.schema.json` en el repo. Misma clase que P-129 (divergencia schema↔vocab), dirección opuesta: ahí el check encontró coincidencia de nombre y comparó valores; aquí no hay schema con el que comparar, así que el gap no cae en DIVERGENCIAS ni en OPEN-STRING FIELDS — el check no lo reporta como divergencia porque solo compara donde hay match | decisión | Escribir el schema que falta (Phase 0), o aceptar que estos tres campos vivan solo en el vocab sin validación estructural | DSC | verificado — corrida local de `vocab_check.py` y runs de CI `30504740061`/`30504959916` (sección `VOCAB FIELDS WITH NO MATCHING SCHEMA FIELD FOUND`); `pipeline_vocabulary.yaml:172-182,346-362` |
| P-136 | Tres campos requeridos vacíos en 1,178 de 1,178: `author_or_actor_if_available`, `snippet_context_before`, `snippet_context_after`. Los tres son `required` en `data_extraction_record.schema.json:16,18,19` y null en el 100% del corpus (`state/output/field_population_extraction_records.md:16,18,19`, rama `claude/field-lifecycle-population-audit-a060e7`, Run 3). Misma falla que P-097 por el otro lado: sin validador de Phase 1b, nada detecta que un campo `required` esté null en todo el corpus — el tipo nullable (`["string","null"]`) hace que la validación de JSON Schema pase igual | decisión | Quitar el requisito, hacerlo exigible, o re-correr Phase 1 | DSC | verificado |
| P-138 | `uncertainties` muere en el puente JSON→Markdown: 27/29 Signal Cards lo tienen poblado (2 vacíos, `empty_array`; `state/output/field_population_signal_cards.md`, fila `uncertainties`) y `signal_to_markdown.py` no lo referencia en ninguna línea — 0 ocurrencias del nombre en el script (confirmado por grep directo), `field_lifecycle_signal_card.md:24` lo marca `SIN-CONSUMIDOR-ENCONTRADO`. Se suma a los 12 campos de Signal Card que no cruzan el puente (`field_lifecycle_signal_card.md:29-40`). Dentro de ese grupo es el de poblado real más alto entre los campos con variabilidad real — excluye `source_ids`, `subject_exact`, `platforms`, `product_type_if_explicit`, `metric_type`, `normalization_notes`, que están 29/29 sin un solo vacío por diseño, no por medición — por delante de `local_qualifiers` (25/29) | decisión | Extender el puente (precedente D-126), o aceptar que `uncertainties` no llegue a markdown | DSC | verificado — `state/output/field_population_signal_cards.md` (fila `uncertainties`), `state/output/field_lifecycle_signal_card.md:24,29-40` (rama `claude/field-lifecycle-population-audit-a060e7`, Run 3); 0 ocurrencias confirmadas por grep sobre `phases/02-signal-extraction/scripts/signal_to_markdown.py` |
| P-140 | `signal_card_defect_check.py` en modo por defecto siempre sale con exit 0, sin importar cuántos defectos encuentre — `sys.exit(0)` incondicional en la línea 504 (fin de `main()`, fuera del bloque `if args.fixtures`). Confirmado corriendo el script sin flags sobre el corpus real: reporta 2 defectos (`time_scope_loss`×2) y sale 0 igual. Solo `--fixtures` es pass/fail real: gatea contra `EXPECTED_GATE` y sale 1 si no calibra — así corre en CI (P-135). El gate custodia la suite de fixtures del propio script, no el corpus de producción; documentado como límite conocido en el comentario de `.github/workflows/ci.yml`, no corregido ahí. Además, el conteo real de fixtures es 21 archivos (11 en `signal_card_defect_check_fixtures/cards/`, 10 en `.../records/`), no 22 — el 22 viene del handoff de S28 (project files, no el repo) y está mal | decisión | Dar a modo por defecto un exit code real (umbral de defectos a decidir), o aceptar que el script mida y no gatee fuera de `--fixtures` | DSC | verificado — `signal_card_defect_check.py:504`; corrida local sin flags (2 defectos, exit 0) y con `--fixtures` (exit 0, calibración vigente); conteo directo de archivos en `signal_card_defect_check_fixtures/{cards,records}/` (11+10=21) |
| U-1 | `geography_if_explicit` no cruza el puente. `card_record` no tiene campo geográfico; el país solo existe como texto libre. Cuatro TCs lo piden | decisión | Extender el puente | DSC | verificado |
| U-2 | `metric_type`, `metric_value_raw`, `metric_unit` sí están en `required` de `phases/02-signal-extraction/schemas/signal_card.schema.json:18-20` (definiciones en líneas 160-186, 221-224, 225-228). No faltan del schema | decisión | Extender la Signal Card | DSC | verificado |
| U-3 | No existe campo de fecha de fuente en la Signal Card. `source_date_if_available` existe en Phase 1 y no cruza. `date` de Phase 3 está contaminado con alcance temporal | decisión | Agregar el campo, o aceptar que 4 TCs no se pueden satisfacer | DSC | verificado |
| P-078 | Documentación de Signal Extraction fragmentada. Dos protocolos obsoletos contra el código en project files | decisión | Reencuadrado por el diseño de S29: blueprints viven en project files. Lo que queda es jubilar los dos obsoletos | DSC | verificado |
| P-116 | Sin mecanismo para jubilar documentos obsoletos. Debilitado como causa del 28%, reforzado por P-129 y P-131 | decisión | Mecanismo, o aceptar el costo caso por caso | DSC | verificado |
| P-121 | El archivado del manifest es prosa, no mecanismo | decisión | Construir el mecanismo, o aceptar la mitigación | CC | verificado |
| P-097 | Phase 1b corrió sin validador (D-140). Diagnóstico corregido en S28: la ausencia de `validation_status` es conformidad con el schema | hecho | No existir no es una decisión tomada, es ausencia sin resolver | CC | promover-a-decision — sin script en `main`/`legacy/*`/`preserve/*`/`git log --all`/objetos unreachable (`git fsck`); solo contrato+schema+`.gitkeep` vacío. No existir no es una decisión tomada, es ausencia sin resolver |
| U-4 | `working/data_gathering/part4_failure_mode_breakdown.json` sin dueño | hecho | Qué hacer con él (borrar o conservar por valor diagnóstico) es juicio del operador | CC | promover-a-decision — huérfano confirmado (0 refs en `main`, 0 refs en 105 objetos `unreachable` de `git fsck --full --unreachable`); qué hacer con él (borrar o conservar por valor diagnóstico) es juicio del operador |

**Cerrados en esta corrección (decisión ya ejecutada, verificada — salen de la tabla):**

- **P-135** — CI existe: `.github/workflows/ci.yml`, dos jobs (`vocab-check`, `signal-card-defect-check --fixtures`), sin `continue-on-error`. Mergeado en PR #66 (`claude/ci-vocab-and-defect-checks`, merge `214dfe6`). Probado en las dos direcciones sobre el mismo PR: run `30504740061` (commit `d3f5954`) falló con exit 1 — `vocab_check.py` reportó divergencia real de `uncertainties` (`extra in schema: anecdotal_single_source, author_conflict_of_interest_possible, methodology_unclear`); run `30504959916` (commit `17ed6b3`), tras mergear el fix de PR #65 a la rama, pasó con exit 0 en los dos jobs.
- **P-129a** — Eran dos campos, no uno. `claim_type`: `statistical_data` agregado al vocab (PR #63, commit `7124833`; 90/1178 registros lo usan). `uncertainties`: `methodology_unclear` (107 apariciones), `anecdotal_single_source` (28), `author_conflict_of_interest_possible` (23) agregados al core del vocab (PR #65, commit `4b016db`) — 158 apariciones sumadas, 150/1178 registros con al menos uno de los tres (unión con solapamiento; no son 158 registros distintos). `vocab_check.py` en exit 0 en `main` hoy — 0 divergencias, `uncertainties` en CLEAN FIELDS.

---

## C. Decisiones de DSC — no tocan el repo

| ID | Enunciado | Clase | Dónde | Estado |
|---|---|---|---|---|
| P-117 | Asignación por fase duplicada entre `Blueprint_DSC.md` y `DSC_Consolidado.md`. Cerrado para Phase 2 por D-213 (puntero); abierto para las otras ocho | decisión | DSC | |
| P-118 | Sexta pregunta del DFPI sobre rendimiento observado de la asignación. D-206 la declara revisable sin decir contra qué | decisión | DSC | |
| P-061 | La pregunta del proyecto no está escrita limpia. Bloquea el DFPI *del proyecto* | decisión | OP | |
| P-062 | Criterio de parada del reconocimiento. Vinculado a P-061 | decisión | OP | |

---

## D. Candidatos a parqueo — necesitan condición de desparqueo, no discusión

| ID | Enunciado | Condición de desparqueo propuesta | Estado |
|---|---|---|---|
| P-002 | Fase post-Expression Research sin definir | Cuando Phase 7 produzca expresiones | |
| P-004 | Blueprint de Expression Research reconstruido sin uso real | Cuando Phase 8 corra por primera vez | |
| P-059 | Direction creator-driven, estructuralmente distinta | Cuando se decida ampliar el subject | |
| P-095 | Convención de nombrado de shards | Cuando Phase 0 vuelva a correr en volumen | |
| P-096 | Iterar `shard_template_v3`. Sin movimiento desde S15 | Idem P-095 | |

---

## Conteo

| Grupo | Filas |
|---|---|
| A — pendientes de verificar (Run 2) | 5 |
| B — verificados, esperando decisión | 23 |
| C — decisiones de DSC | 4 |
| D — candidatos a parqueo | 5 |
| **Total abiertos** | **37** |

**Cerrados en esta corrección:** P-135, P-129a (ver citas en la tabla B, justo después de P-121); P-075, P-077, P-082 (ver citas bajo la tabla A, justo después de la tabla).
**Cerrados en S28, no re-abrir:** P-076, P-107, P-108, P-110, P-112, P-114, P-120, P-122, P-123,
P-124, P-130.
**Cerrados antes:** P-058, P-060, P-063, P-064, P-065, P-066, P-079, P-080, P-101, P-104, P-105,
P-106, P-111, P-113, P-115.
**Huecos de numeración, no son pendientes:** P-024, P-027, P-028, P-051 a P-057, P-081 a P-093
parcialmente, P-098, P-103.

---

## Nota sobre la forma de la cola

23 de 37 ya están verificados y esperan juicio del operador. 9 esperan que alguien mire el repo.
5 no son decidibles hoy. **El cuello es la cola de decisiones, no la de verificación.**

De los 23 del grupo B, ocho son huecos de puente o de campo (P-134, P-136, P-138, U-1, U-2, U-3,
más `local_qualifiers` y `time_scope_raw`) y todos comparten la misma pregunta previa: qué campos
consume Phase 3 realmente. Esa pregunta es el entregable A de Run 3. **Decidir cualquiera de los
ocho antes de Run 3 repite el error que interrumpió S28 cuatro veces.**

Los cuatro del bloque A (P-119, P-126, P-127, P-128) bloquean los 47 batches y tres de ellos
están explícitamente diferidos al assessment por el handoff de S28.
