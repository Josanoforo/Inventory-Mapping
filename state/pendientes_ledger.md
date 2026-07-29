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
| P-077 | Borderlines F-X05 y F-X07 de Part 4 legacy, sin decidir si entran a `scope_exploration` | hecho | ¿Existen F-X05 y F-X07 en el corpus vigente? En qué archivo y con qué clasificación, en todas las refs | CC | cerrado-ya-hecho — 79 diagnósticos ya clasificados en `working/data_gathering/diagnostics/part_4/` (43 `__F-X05.json` + 36 `__F-X07.json`, cada uno con `verification_status`); 0 refs a `scope_exploration` |
| P-082 | Acumulación en `source_intake_gpt_recovery/` sin flujo de recovery definido | hecho | ¿Cuántos archivos hay hoy en ese directorio en `main`? Si 0, cierra | CC | cerrado-ya-hecho — `working/source_intake/source_intake_gpt_recovery/` solo tiene `.gitkeep`, 0 archivos reales |
| P-097 | Phase 1b corrió sin validador (D-140). Diagnóstico corregido en S28: la ausencia de `validation_status` es conformidad con el schema | hecho | ¿Existe script de validación de Phase 1b en cualquier rama o en la historia? Nombre y ruta | CC | promover-a-decision — sin script en `main`/`legacy/*`/`preserve/*`/`git log --all`/objetos unreachable (`git fsck`); solo contrato+schema+`.gitkeep` vacío. No existir no es una decisión tomada, es ausencia sin resolver |
| P-075 | Sin lugar definido para QA notes densos tipo DX-2 | hecho | ¿Existen QA notes en el repo? Cuántos, en qué rutas | CC | cerrado-ya-hecho — `working/data_gathering/diagnostics/qa_notes/`, 59 archivos |
| P-094 | Métricas de flujo por fase diferidas. Los contadores de los manifests no discriminan | hecho | ¿Qué escribe métricas a disco hoy? Enumerar todo script que persista contadores, con ruta de salida | CC | sigue-abierto — 6 scripts `.py` escriben manifest por-corrida (`eje4_xlsx_to_json_batch.py`, `part4_to_recovery_packets.py`, `bulk_extract.py`, `extraction_prepare.py`, `converter_prepare.py`, `signal_prepare.py`); sin métrica cross-fase, confirma el diagnóstico original |
| U-4 | `working/data_gathering/part4_failure_mode_breakdown.json` sin dueño | hecho | ¿Qué archivo lo lee o lo escribe? Cero coincidencias = huérfano | CC | promover-a-decision — huérfano confirmado (0 refs en `main`, 0 refs en 105 objetos `unreachable` de `git fsck --full --unreachable`); qué hacer con él (borrar o conservar por valor diagnóstico) es juicio del operador |
| P-092 | Auditoría de atomicidad de Phase 2 ejecutada solo sobre batch_001 | decisión | Enmarque: ¿cuántas cards existen hoy fuera de batch_001? | CC | sigue-abierto — `signal_converter_manifest.json`: `skeletons_processed: 25` = 100% de `batch_001`; `cards_written: 29`; 0 cards fuera de batch_001 |
| P-102 | Falta regla de verificación de ramas en `CLAUDE.md`. Tres casos: `fetch --prune`, trampa de columna Ahead, el relay no borra refs | decisión | Enmarque: ¿`CLAUDE.md` menciona hoy alguna de las tres? | CC | sigue-abierto — `CLAUDE.md` (93 líneas): 0 menciones de `fetch --prune`, "Ahead" o "relay" |
| P-109 | 186 queries del catálogo del eje 4 sin correr. Desbloqueado en S28 | decisión | Enmarque: ¿existe el catálogo de 186 queries en el repo? Ruta y conteo real | CC | sigue-abierto — el `.xlsx` no existe en `main`/`legacy/*`/`preserve/*`; `working/eje4/` no existe; solo script de pre-proceso + contrato del agente, sin correr. Conteo real no verificable desde el repo |

---

## B. Ya verificados en S28 — no requieren Run 2, esperan decisión

| ID | Enunciado | Clase | Qué falta | Dónde | Estado |
|---|---|---|---|---|---|
| P-125 | Regla 5 de `p2-extract-signals/SKILL.md` contradice campo 13 de `signal_converter.md` | hecho | **Decisión tomada en S28, edición pendiente.** Regla 5 → puntero; campo 13 → fuente única con exclusión de metadata y ruteo a `time_scope_raw` | CC | decidido, sin ejecutar |
| P-137 | `extraction_converter.md` rutea fallos a `extraction_gpt_recovery/`, que no existe. El árbol y `CLAUDE.md` dicen `rejected_archive/` | hecho | Edición trivial de una ruta | CC | verificado |
| P-131 | Dos versiones de `Blueprint_Phase_2_Signal_Extraction.md` con la misma pretensión de fuente única | hecho | Retirar una. Vive en project files, no en el repo | DSC | verificado |
| P-133 | El análisis de diferencias de S27 se llamó "health check", término reservado al componente E del Blueprint | hecho | Corrección de término en el registro | DSC | verificado |
| P-126 | `time_scope_raw` sin regla para material mezclado (bloque A, decisión 2a) | decisión | Extraer verbatim y resto a `normalization_notes`, o conservar string completo y marcar contaminación | DSC | verificado |
| P-119 | Múltiples anclajes temporales verbatim en `time_scope_raw` (bloque A, 2b). **Bloquea los 47 batches** | decisión | Concatenar con separador, un ancla y resto a notas, o splittear la card | DSC | verificado |
| P-127 | Condición de override de `actor_level` delega en juicio no acotado (bloque A, 3) | decisión | Eliminar la segunda condición, o acotarla a criterio verificable. No hay criterio propuesto y los casos no existen | DSC | verificado |
| P-128 | Hueco en la tabla de `source_type` para reporte en tercera persona (bloque A, 4). Obligatoria en los 305 records con `actor_level: unknown` | decisión | `source` es el polo seguro; `seller` crea polos falsamente cross-actor | DSC | verificado |
| P-129 | `pipeline_vocabulary.yaml` es autoridad declarada sobre enums y ningún ejecutor lo lee | decisión | Agregarlo a lectura obligatoria, o retirar la declaración de autoridad | DSC | verificado |
| P-132 | El detector se mergeó sin satisfacer la precondición de calibración de D-212 Carga A. Los tres casos no existen | decisión | Recalibrar contra casos nuevos, o aceptar el detector con limitaciones declaradas | DSC | verificado |
| P-134 | `evidence_role` no cruza a Phase 3: `card_record` tiene `evidence_base`, string libre sin enum | decisión | Extender el puente (precedente D-126) o aceptar la pérdida | DSC | verificado |
| P-135 | No existe CI. `.github/workflows/` ausente. D-203 declaró el health check automatizado; el script existe y nada lo dispara | decisión | Construir CI, o retirar la declaración de D-203 | DSC | verificado |
| P-136 | Tres campos requeridos vacíos en 1,178 de 1,178: `author_or_actor_if_available`, `snippet_context_before`, `snippet_context_after` | decisión | Quitar el requisito, hacerlo exigible, o re-correr Phase 1 | DSC | verificado |
| U-1 | `geography_if_explicit` no cruza el puente. `card_record` no tiene campo geográfico; el país solo existe como texto libre. Cuatro TCs lo piden | decisión | Extender el puente | DSC | verificado |
| U-2 | `metric_type`, `metric_value_raw`, `metric_unit` sí están en `required` de `phases/02-signal-extraction/schemas/signal_card.schema.json:18-20` (definiciones en líneas 160-186, 221-224, 225-228). No faltan del schema | decisión | Extender la Signal Card | DSC | verificado |
| U-3 | No existe campo de fecha de fuente en la Signal Card. `source_date_if_available` existe en Phase 1 y no cruza. `date` de Phase 3 está contaminado con alcance temporal | decisión | Agregar el campo, o aceptar que 4 TCs no se pueden satisfacer | DSC | verificado |
| P-078 | Documentación de Signal Extraction fragmentada. Dos protocolos obsoletos contra el código en project files | decisión | Reencuadrado por el diseño de S29: blueprints viven en project files. Lo que queda es jubilar los dos obsoletos | DSC | verificado |
| P-116 | Sin mecanismo para jubilar documentos obsoletos. Debilitado como causa del 28%, reforzado por P-129 y P-131 | decisión | Mecanismo, o aceptar el costo caso por caso | DSC | verificado |
| P-121 | El archivado del manifest es prosa, no mecanismo | decisión | Construir el mecanismo, o aceptar la mitigación | CC | verificado |

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
| A — pendientes de verificar (Run 2) | 9 |
| B — verificados, esperando decisión | 19 |
| C — decisiones de DSC | 4 |
| D — candidatos a parqueo | 5 |
| **Total abiertos** | **37** |

**Cerrados en S28, no re-abrir:** P-076, P-107, P-108, P-110, P-112, P-114, P-120, P-122, P-123,
P-124, P-130.
**Cerrados antes:** P-058, P-060, P-063, P-064, P-065, P-066, P-079, P-080, P-101, P-104, P-105,
P-106, P-111, P-113, P-115.
**Huecos de numeración, no son pendientes:** P-024, P-027, P-028, P-051 a P-057, P-081 a P-093
parcialmente, P-098, P-103.

---

## Nota sobre la forma de la cola

19 de 37 ya están verificados y esperan juicio del operador. 9 esperan que alguien mire el repo.
5 no son decidibles hoy. **El cuello es la cola de decisiones, no la de verificación.**

De los 19 del grupo B, siete son huecos de puente o de campo (P-134, P-136, U-1, U-2, U-3, más
`local_qualifiers` y `time_scope_raw`) y todos comparten la misma pregunta previa: qué campos
consume Phase 3 realmente. Esa pregunta es el entregable A de Run 3. **Decidir cualquiera de los
siete antes de Run 3 repite el error que interrumpió S28 cuatro veces.**

Los cuatro del bloque A (P-119, P-126, P-127, P-128) bloquean los 47 batches y tres de ellos
están explícitamente diferidos al assessment por el handoff de S28.
