# E-A5REC-S37 — La excepción declarada del filtro same-actor

Solo lectura + este reporte. No repara nada, no cierra A5. Mide.

## Precondición [repo@BASE]

- **BASE** = `HEAD` de `origin/main` al correr: `02efc8081b60c7a1b4339b413ceda5e8bf80e84c` (2026-08-05 01:57:16 +0000).
- Rama designada `claude/same-actor-filter-exception-tbqw17`: no existe en `origin` (`git fetch --prune` reporta `[deleted]` para esa referencia). Creada nueva desde `origin/main` en ese mismo commit.
- `pipeline_vocabulary.yaml`, campo `actor`, `notes`, línea 44: contiene literalmente:
  > `- "'source' and 'mixed' trigger needs_audit in Phase 3 scanner (not eligible for cross-actor filter)."`
- Siete skills `scan-*` existen. Cuatro contienen el bloque "Same-actor filter": `scan-asymmetries`, `scan-contradictions`, `scan-frictions`, `scan-opposite-directions`. Tres no lo contienen: `scan-co-occurrences`, `scan-gaps`, `scan-lexical-overlap`. Confirmado por conteo directo antes de escribir nada.
- Verificado antes de escribir: `state/output/excepcion_same_actor_S37.md` no existe en `origin/main` — este encargo no se había corrido.
- **R-G**: `git rev-parse --is-shallow-repository` → `true` al iniciar. Se corrió `git fetch --unshallow origin`; tras eso → `false`. 639 commits alcanzables desde HEAD. Todas las afirmaciones de CUÁNDO en este reporte (M4) están respaldadas por este historial completo, no por un clon parcial.

**Nota de alcance.** El encargo declara una lista cerrada de LECTURA. Dos de las preguntas explícitas (M3.1 pide "confirma y añade los que falten, con archivo:línea"; M5 pide re-medir `unknown` sobre "el corpus de 1,178") no son respondibles dentro de esa lista cerrada sin leer, respectivamente, `phases/02-signal-extraction/scripts/signal_to_markdown.py` (sí está en la lista) y `working/data_extraction/records/*.json` (NO está en la lista cerrada — el corpus de 1,178 vive ahí, no en `working/signal_extraction/cards/`). Para responder lo que el encargo pide explícitamente, se leyó `working/data_extraction/records/*.json` (1,178 archivos, solo lectura, sin escritura). Se declara aquí para que el operador lo juzgue: es una lectura fuera de la lista cerrada, hecha porque la alternativa era dejar M5 sin responder en su segunda mitad. También se leyeron, para contexto y re-verificación cruzada (no como fuente primaria de ninguna cifra): `state/output/actor_level_confiabilidad_S37.md`, `state/output/etapa3_veredictos.md`, `state/output/verificacion_decisiones_S36.md`, y (vía `git show`, no vía lectura del árbol de trabajo) el diff de `phases/01-source-intake/data-extraction/contracts/data_extraction_contract.md` en el commit `5f1e03d4`. Ninguna cifra reportada abajo depende de esos archivos sin haber sido re-medida directamente sobre los datos primarios declarados en el encargo.

---

## M1 — Los cuatro filtros, ¿son el mismo texto?

Extracción del bloque completo "Same-actor filter" (desde la línea que empieza `Same-actor filter:` hasta la línea que termina en `regardless of any other consideration.`) de las cuatro skills, comparación byte a byte (`md5sum` + `diff`):

**`scan-asymmetries/SKILL.md:22-26`:**
```
   - Same-actor filter: look up the `actor` field for every Signal ID in both poles from `working/index/card_index.jsonl`. If ALL Signal IDs across BOTH poles have the SAME actor value → route to rejected_grouping with reason "same_actor_discrepancy".

     This check is purely mechanical: compare actor values only. Do NOT evaluate whether the cards in each pole refer to the same mechanism, sub-topic, or channel. Grounding evaluation is the human's job during review, not the scanner's.

     If the poles contain different actor values, the pattern passes this filter regardless of any other consideration.
```

**`scan-contradictions/SKILL.md:22-26`:** — texto idéntico al anterior, carácter por carácter.

**`scan-frictions/SKILL.md:22-26`:** — texto idéntico al anterior, carácter por carácter.

**`scan-opposite-directions/SKILL.md:23-27`:** — texto idéntico al anterior, carácter por carácter (el bloque empieza una línea más abajo en este archivo porque el procedimiento tiene un paso extra antes: "Verify both forces act on the same system or domain.").

**Resultado:** `md5sum` de los cuatro bloques extraídos = `fce3dfa53936c5bc189ebc4a049ebb55`, 614 bytes cada uno. **Idénticos, sin divergencia.** `diff` entre cualquier par de los cuatro: vacío.

No divergen — la condición de la plantilla ("Si divergen, eso ya es hallazgo... la clase P-153 aplica") no se activa por esta vía. Pero la duplicación en sí es un hecho aparte de la identidad textual: son cuatro copias del mismo texto en cuatro archivos, no una referencia compartida. Eso importa para el veredicto de abajo, independientemente de que hoy coincidan carácter por carácter — coincidir hoy no es lo mismo que estar definidas en un solo lugar.

---

## M2 — Las tres skills sin filtro: ¿diseño o hueco?

**Evidencia de mayor peso — el commit que introdujo el filtro declara la exclusión explícitamente.** `git log -S"Same-actor filter"` sobre los cuatro archivos que sí tienen el bloque apunta a un único commit: `bbda31a9b2919554683636f00e0fe3ed9e32aafd` (2026-04-11 02:44:14 +0000), mensaje:
> "Add same-actor filter to scanners and actor composition block to builder [...] Filter does not apply to co-occurrences, gaps, or lexical-overlap"

Las tres exclusiones fueron declaradas en el mismo commit que introdujo el filtro, no omitidas después. Esto ya responde M2 para las tres. La lectura de cada skill (abajo) corrobora **por qué** con la estructura de cada una:

**`scan-co-occurrences/SKILL.md:16-24`** — agrupa un solo clúster de 3+ cards ("Find sets of 3+ cards that consistently appear around the same topic"), no dos polos. `04_scanner.md:31-36` confirma: "Find cards that appear together consistently around the same topic [...] Must generate a plausible DT question to route as tension_candidate." No hay "Polo A / Polo B" que comparar — el filtro, tal como está escrito en las otras cuatro skills, opera sobre "both poles"; aquí no hay segundo polo. Diseño, no hueco: la estructura del scan no produce el objeto (dos polos) sobre el que el filtro mecánico compara.

**`scan-gaps/SKILL.md:15-24`** — no agrupa cards existentes entre sí; documenta ausencia ("Identify areas where you would expect cards [...] but cards are absent"). `04_scanner.md:37-41`: "Report what is missing, not what is present." Todos los patrones rutean a `coverage_gap` (`04_scanner.md:60`), no a `rejected_grouping`/`tension_candidate`/`needs_audit`. No hay polos de cards en oposición — el `signal_ids` que se registra son "cards that create the expectation", un solo conjunto de apoyo, no dos lados. Diseño, no hueco, por la misma razón estructural que co-occurrences.

**`scan-lexical-overlap/SKILL.md:9-20`** — es el caso menos limpio de los tres. Agrupa un "overlap group" (no polos nombrados), pero su regla de ruteo sí permite una salida de dos lados: "Overlap reveals explicit friction or tension between the overlapping cards → `tension_candidate`" (`SKILL.md:15`; `04_scanner.md:46-49`: "Only route as `tension_candidate` if explicit friction exists between the overlapping cards"). Esa salida se parece estructuralmente a lo que contradictions/frictions detectan (fricción explícita entre dos lados) — y ninguna de las dos tiene el filtro de actor. Sin la cita del commit `bbda31a9` esto sería ambiguo y defendible como hueco. Con la cita, es diseño declarado: el autor del filtro consideró las tres explícitamente y las excluyó a las tres por nombre, incluida esta. La ambigüedad estructural queda, pero la decisión no fue silenciosa.

---

## M3 — ¿Dónde viviría la excepción?

### 1. ¿Qué otros lugares de Phase 3 leen `actor`?

Ya conocidos, confirmados con línea exacta:
- `phases/03-inventory-mapping/schemas/card_record.schema.json:6` — `actor` en la lista `required`.
- `phases/03-inventory-mapping/schemas/card_record.schema.json:43-46` — define el enum: `["buyer", "seller", "product", "marketplace", "platform", "source", "third_party", "mixed"]`. **No incluye `unknown`** (consistente con `pipeline_vocabulary.yaml:19,29`: "Phase 3 does not use unknown").
- `phases/03-inventory-mapping/modules/03_indexer.md:20` — "For each card, extract: id, round, observation, source, date, source_type, domain, actor, evidence_base, extraction_status."
- `phases/03-inventory-mapping/modules/03_indexer.md:21` — "Parse `actor` from the 'Actor:' field in the markdown block."
- `phases/03-inventory-mapping/modules/05_candidate_builder.md:27-32` — bloque "Actor composition" obligatorio en cada TC: Polo A/Polo B/Cross-actor YES-NO, poblado desde `card_index.jsonl`.

Faltaban por confirmar, encontrados en esta corrida:

- **`phases/02-signal-extraction/scripts/signal_to_markdown.py:79-88`** — mapa `ACTOR_LEVEL_TO_DOMAIN` (de `actor_level` a `domain`, un campo distinto del schema de Phase 3).
- **`phases/02-signal-extraction/scripts/signal_to_markdown.py:124-149`** — función `derive_domain(actor_level)`, que consume `actor_level` para producir `domain`.
- **`phases/02-signal-extraction/scripts/signal_to_markdown.py:253,257,272`** — lee `actor_level = card.get("actor_level")` (línea 253), lo pasa a `derive_domain` (línea 257), y lo escribe literal en la línea `f"Actor: {actor_level}"` (línea 272) del bloque markdown — el mismo bloque que `03_indexer.md:21` luego parsea. Este es el punto donde el valor cruza de Phase 2 (JSON) a Phase 3 (markdown → índice).
- **Los cuatro `scan-*/SKILL.md` mismos** (`scan-asymmetries:22`, `scan-contradictions:22`, `scan-frictions:22`, `scan-opposite-directions:23`) — ya citados completos en M1, pero son en sí mismos un lugar que lee `actor` (vía `card_index.jsonl`), separado de los tres ya conocidos.
- **Ausencia notable:** `phases/03-inventory-mapping/schemas/tension_candidate.schema.json` y `phases/03-inventory-mapping/schemas/scan_artifact.schema.json` **no mencionan `actor` en absoluto** (grep completo, cero coincidencias). El bloque "Actor composition" que `05_candidate_builder.md:27-32` exige por escrito en cada TC no está validado por ningún schema — existe como instrucción de skill, no como campo verificable.
- **Ausencia notable:** `phases/03-inventory-mapping/modules/04_scanner.md` (el módulo que gobierna el paso Scanner, normativamente superior a las skills por la jerarquía de autoridad del repo) **no menciona `actor` en absoluto** (grep completo, cero coincidencias). El filtro same-actor vive únicamente en las cuatro skills; el módulo que las gobierna no lo define, no lo exige y no lo respalda.
- **Ausencia notable:** `phases/03-inventory-mapping/reference/protocol_canonical.md` (el canon, autoridad máxima dentro de Phase 3 según `CLAUDE.md`) **tampoco menciona `actor`** en absoluto.

### 2. `needs_audit` del scanner vs. `needs_audit` de la nota: ¿la misma cosa?

**No. Son dos condiciones de disparo distintas que comparten un nombre.**

`04_scanner.md:62` (Routing rules per pattern): `` `needs_audit`: partial support, unclear classification. `` — genérico para las 7 operaciones.

Instanciado en cada una de las cuatro skills con filtro, el disparador real de `needs_audit` es **soporte de cards, nunca valor de actor**:
- `scan-asymmetries/SKILL.md:29` — "One pole has only 1 card → `needs_audit`"
- `scan-contradictions/SKILL.md:29` — "Apparent contradiction but one side has only 1 card → `needs_audit`"
- `scan-frictions/SKILL.md:29` — "Mechanism unclear or single-card support → `needs_audit`"
- `scan-opposite-directions/SKILL.md:30` — "One force has single-card support → `needs_audit`"

Ninguna de las cuatro reglas de ruteo menciona el valor de `actor` como condición de `needs_audit`. El disparador es "single-card support" / "mechanism unclear" — sobre el número y claridad de las cards, no sobre quién habla.

`pipeline_vocabulary.yaml:44`: "'source' and 'mixed' trigger `needs_audit` in Phase 3 scanner" — este `needs_audit` se dispara por el **valor del campo `actor`** (`source` o `mixed`, sin importar cuántas cards haya de soporte).

Son dos conceptos con el mismo nombre de destino (`needs_audit`) y condiciones de entrada mutuamente independientes: una cuenta cards, la otra lee un valor de enum. Un patrón con `actor=source` en ambos polos y 5 cards de soporte por lado dispararía el `needs_audit` de la nota (si existiera) pero no el del scanner (soporte no es el problema). No hay ningún punto del código o la especificación donde ambas condiciones se unifiquen.

### 3. ¿Existe algún artefacto donde la excepción se haya aplicado?

**Cero ocurrencias — y no solo por ausencia de intento.** `output/tension_candidates/` contiene únicamente `.gitkeep`. `working/scans/` contiene únicamente `.gitkeep`. `working/index/` contiene únicamente `.gitkeep` — **no existe `card_index.jsonl` en el árbol actual**, lo que significa que ni siquiera el Indexer (paso previo al Scanner) se ha corrido sobre el corpus vigente. No hay ningún artefacto vivo donde ninguna de las dos versiones del filtro (la base, mecánica, o la excepción de la nota) se haya podido aplicar, porque el pipeline no ha producido salidas de Phase 3 en el estado actual del repo.

Ver M4 para la historia de por qué (hubo corridas reales, después borradas, antes de que la nota existiera).

---

## M4 — ¿La regla se implementó alguna vez? [unshallow hecho, R-G satisfecho]

Cronología completa, 639 commits alcanzables desde HEAD:

| Hora (UTC, 2026-04-11) | Commit | Qué pasó |
|---|---|---|
| 02:44:14 | `bbda31a9` | Filtro mecánico base (comparar `actor` de todos los Signal IDs en ambos polos) agregado a las 4 skills + bloque "Actor composition" al builder. Mensaje declara explícitamente: "Filter does not apply to co-occurrences, gaps, or lexical-overlap." |
| 02:47:50 – 04:19:42 | `78d28271`, `7f71db78`, `753047c6`, `09fd8635`, `90b23b3f`, `7fec4eff`, `90fd6d8e`, `a1e3d84b` | Corridas reales del pipeline (v2, v3, v4): scans + builder sobre un índice de 75 cards, con el filtro base aplicado. `7fec4eff` (03:42:28) es el último commit que toca el texto del filtro en cualquiera de las 4 skills — "Clarify same-actor filter: purely mechanical actor value comparison, no grounding eval". Produjo `output/tension_candidates/TC-002.md` … `TC-0NN.md`, `output/rejected_groupings.md`, `output/coverage_gaps.md`, `output/review_queue.md`, artefactos de scan v1/v3/v4 — todos existieron en el árbol en algún punto de esta ventana. |
| 04:19:42 | `3dfd73ca` | "Clean up test run data; preserve design files and diagnostics" — borra scans v1/v3/v4, tension candidates v1-v4, y manifiestos de esa corrida. |
| 04:24:05 | `ac8fae63` | "Remove remaining test run artifacts and intermediate outputs" — borra `output/v2/`, `output/v3/`, `working/scans_v2/` y remanentes. |
| 06:03:43 | `acfafdd0a` | **`pipeline_vocabulary.yaml` se crea por primera vez** (289 líneas, archivo nuevo completo). Contiene, ya en esta primera versión, la línea 44 citada: "'source' and 'mixed' trigger needs_audit in Phase 3 scanner (not eligible for cross-actor filter)." `git blame` confirma: esta línea no ha cambiado desde este commit — es la misma hoy. |

**Hallazgo central:** el filtro base (mecánico, sin distinción de valor) se implementó, se corrió contra datos reales tres veces (v2/v3/v4), y sus artefactos se borraron — **todo esto ocurrió antes de que `pipeline_vocabulary.yaml` existiera**. La nota que describe la excepción por valor (`source`/`mixed` → `needs_audit`) entró **1h39min después** de que se borraran las últimas corridas, y **2h21min después** del último commit que tocó el texto de cualquiera de las cuatro skills. Ningún commit posterior a `acfafdd0a` (ni ese día, ni en los 639 commits del historial completo hasta hoy) vuelve a tocar el bloque "Same-actor filter" de ninguna de las cuatro skills — `git log` sobre los cuatro archivos lo confirma: el último cambio de contenido de filtro en cada uno es `7fec4eff`, tres commits (y ~2h20min) antes de que la nota naciera.

**Búsqueda exhaustiva de una implementación perdida:** `git log --all -p -G` sobre las tres variantes de la frase ("not eligible for cross-actor", "source...needs_audit", "needs_audit...source") en todo el historial (`--all`, no solo la rama de HEAD) sobre `*.md` y `*.yaml` devuelve exactamente dos apariciones de esta nota: el commit original `acfafdd0a` (2026-04-11) y un commit de **hoy**, `5f1e03d46a01201fb952328c8ce67d93a96a4ea2` (2026-08-05 01:53:58 +0000, "D-267 (S37): completa D-197/D-198 en las tres superficies de Phase 1", ya en `origin/main`, ancestro confirmado de BASE) — que **copia la nota textualmente** hacia `phases/01-source-intake/data-extraction/contracts/data_extraction_contract.md:227`, como parte de propagar las notas del vocabulario a Phase 1. Ninguna de las dos apariciones toca código de skill. No hay una tercera versión perdida en ningún refactor.

**Veredicto de M4: entró como descripción de algo que no existía.** No es "se diseñó y nunca se implementó" (eso implicaría una intención de implementación pendiente, y no hay ningún rastro de tal intención en 639 commits ni en las corridas v2-v4, que usaron el filtro base, no el de valor). No es "se implementó y se perdió en un refactor" (no hay ningún commit, en ningún punto del historial completo con `--all`, que implemente lógica condicionada al valor `source`/`mixed` en ninguna skill). La nota se escribió en tiempo presente, como si describiera una conducta ya existente del scanner ("trigger needs_audit"), en el mismo commit que creó el archivo de vocabulario entero — y esa conducta nunca existió en el código, ni antes ni después. El commit de hoy la trató como documentación asentada y citable, no como pendiente de diseño, lo que refuerza esta lectura.

---

## M5 — Escala sobre el corpus vigente [solo lectura]

### Distribución de `actor_level` en las 29 cards

Re-medido directamente sobre `working/signal_extraction/cards/*.json` (29 archivos, campo `actor_level`, valor escalar en los 29 — ninguno es array en este corpus):

| actor_level | count |
|---|---:|
| source | 14 |
| third_party | 8 |
| platform | 6 |
| marketplace | 1 |
| **total** | **29** |

Coincide exactamente con la cifra de procedencia (source 14, third_party 8, platform 6, marketplace 1 sobre `d5148acd`) — re-medido sobre BASE `02efc808`, sin cambio.

### Fracción de pares que caerían en `rejected_grouping` por mismo actor

**Método declarado:** el filtro real compara "todos los Signal IDs en ambos polos" — con polos de un solo card cada uno (el caso mínimo, sin simular ninguna lógica real de agrupación de ningún scan), la regla se reduce a: ¿el `actor_level` de la card A es igual al de la card B? Se enumeran todos los pares no ordenados posibles entre las 29 cards — `C(29,2) = 406` pares — y se cuentan los pares donde ambas cards comparten el mismo valor de `actor_level`, sumando combinaciones dentro de cada grupo:

- `source`: C(14,2) = 91
- `third_party`: C(8,2) = 28
- `platform`: C(6,2) = 15
- `marketplace`: C(1,2) = 0

Pares con mismo actor: 91 + 28 + 15 + 0 = **134**. Total de pares posibles: **406**.

**Fracción: 134/406 = 67/203 ≈ 0.3300 (33.00%).**

Esto es un límite superior conceptual, no una predicción de cuántas tensiones reales caerían así: los polos reales de un scan casi siempre agrupan más de una card por lado, y la probabilidad de que **todas** las cards de ambos polos combinados compartan actor cae cuantas más cards entren. La cifra de pares (33.00%) mide la fracción del universo de comparaciones posibles a nivel de card individual, no la fracción de tensiones que el pipeline produciría.

### `unknown` en el corpus de 1,178

Re-medido directamente sobre `working/data_extraction/records/*.json` (1,178 archivos, 0 malformados, 0 sin campo `actor_level`; ver Nota de alcance arriba sobre por qué se leyó esta ruta):

- 1,150 records con `actor_level` como string escalar; 28 como array.
- `actor_level: "unknown"` (escalar): **305**.
- `"unknown"` dentro de alguno de los 28 arrays: **0**.
- **Total con `unknown`: 305.**

Coincide exactamente con la cifra de procedencia (305) — re-medido sobre BASE `02efc808`, sin cambio.

---

## Veredicto obligatorio

**La excepción no tiene lugar coherente** — el `needs_audit` que las cuatro skills disparan (soporte insuficiente de cards, `04_scanner.md:62` + reglas de ruteo por skill) y el `needs_audit` que la nota del vocabulario describe (valor de `actor` igual a `source` o `mixed`) son condiciones de entrada distintas que comparten un nombre de salida; implementar la nota tal como está escrita exigiría definir una tercera vía hacia `needs_audit` que hoy no existe en ningún módulo ni skill, no extender una que ya está ahí.

Independientemente de esa incoherencia conceptual: incluso el filtro base (sin la excepción) vive hoy en cuatro copias textuales idénticas (M1) sin ancla en el módulo (`04_scanner.md`) ni en el canon (`protocol_canonical.md`) que lo gobiernan — la superficie de cambio para cualquier ajuste al filtro, exista o no la excepción, ya es N=4 por diseño actual del repo, no una condición única.

## R-E — Barrera

**Ausente.** `vocab_check.py` (raíz del repo) es la única verificación automática que existe sobre `pipeline_vocabulary.yaml`, y su propio docstring + código declaran el alcance: compara los **valores de enum** declarados contra los enums de cada `*.schema.json` del repo. La constante `META_KEYS` del script incluye literalmente `"notes"` en la lista de claves excluidas de la comparación — el campo exacto donde vive la frase sobre `source`/`mixed` y `needs_audit` está explícitamente fuera del alcance de la única barrera que existe. No hay ningún mecanismo, en este repo, que verifique que una afirmación en prosa dentro de `notes:` corresponda a conducta real en las skills o módulos que describe. El commit de hoy (`5f1e03d4`) propagó la misma nota, sin verificación, a una segunda superficie (`data_extraction_contract.md`) — evidencia directa de que la barrera no se activó ni en la escritura original ni en su propagación reciente.

No se propone construir esta barrera — se declara su ausencia, por instrucción del encargo.
