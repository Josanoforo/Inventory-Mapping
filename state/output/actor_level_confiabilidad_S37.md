# E-AL-S37 — ¿Es confiable el actor_level de Phase 1?

> **Corrección — D-264 (S37).**
>
> El veredicto NO-CONFIABLE de este reporte midió `actor_level` de Phase 1 contra la tabla de
> `signal_converter.md` §4.4. Esa fue la lectura correcta del texto vigente al momento de la
> medición: líneas 140 y 142 decían que heredar sin modificar era "the default outcome for every
> card", pero que, cuando se cumplía una de dos condiciones (valor heredado `unknown`, o la
> formulación del signal_text revela imprecisión), había que "apply the table" — mandato, no
> sugerencia, para esos casos. La medición no tiene defecto metodológico: aplicó el criterio tal
> como el texto lo planteaba entonces.
>
> D-264 sustituye ese párrafo. Texto que instala en `signal_converter.md` §4.4, campo 3: la tabla
> es la regla de asignación, no un fallback; cuatro filas se resuelven por `source_type` y dos por
> la postura del hablante, con independencia del `source_type`; cuando ninguna fila aplica se
> hereda el valor de Phase 1 y ahí ese valor es la decisión, no un insumo. El veredicto se retira
> porque el criterio contra el que medía cambió, no porque la medición estuviera mal hecha.
>
> **Las siete mediciones (M1–M7) siguen vigentes** y son la base de evidencia de D-264. **El
> encuadre del veredicto (NO-CONFIABLE) no** — se retira como conclusión de este reporte.
>
> Dos afirmaciones adicionales del reporte original se descuentan:
> - (a) "La tabla aparece por primera vez río abajo" es afirmación histórica no sostenible sobre
>   un clon shallow. Lo sostenible: la tabla no está en el contrato de Phase 1
>   (`data_extraction_contract.md`), sí en el módulo de Phase 2.
> - (b) La identificación de la skill `extract-records` como productora real es una inferencia
>   sobre un archivo fuera del alcance declarado del encargo — marcada como tal en el reporte
>   original, nunca verificada.
>
> **Se conserva:** la distribución de M6 — la carga de corrección de Phase 2 se concentra en
> `product_listing` (6/6 cards overridden) y en el vecindario de `search_results_page`/
> `platform_doc`, y es baja en los cuatro `source_type` institucionales (`help_center`,
> `policy_page`, `platform_doc`, `pricing_page`). Es un hecho sobre dónde trabaja Phase 2,
> independiente del encuadre del veredicto.

**Resumen para decidir sin abrir archivos:** HEAD real coincide exactamente con el BASE declarado. Veredicto retirado por D-264 — ver el bloque de corrección arriba. La medición original dio 75.13% (420/559) en el subconjunto mecánicamente decidible contra un umbral de 90% declarado antes de aplicar la tabla; esa cifra sigue vigente como medición, no como juicio sobre Phase 1.

## Precondición [repo@BASE]

- BASE declarado por el redactor: `d5148acd763ead8915ccffdf9e17222f8c404b60`
- HEAD real verificado tras `git fetch origin --prune`: `d5148acd763ead8915ccffdf9e17222f8c404b60`
- `git log -1 origin/main`, `git merge-base HEAD origin/main` y `git rev-parse HEAD` devuelven los tres el mismo SHA. **No hay divergencia que anclar** — todas las cifras de este reporte son sobre ese commit exacto.
- La rama designada `claude/actor-level-phase-1-reliability-w5ygiy` no existe en `origin` (`git ls-remote origin refs/heads/...` vacío; el fetch reporta `[deleted]` para esa referencia). Se crea nueva desde `origin/main` en este mismo commit.
- **R-G — advertencia de clon shallow:** `git rev-parse --is-shallow-repository` → `true`; `.git/shallow` lista 5 commits frontera; solo 85 commits son alcanzables desde HEAD; `bulk_extract.py` solo tiene 4 commits visibles en su historia. Ninguna cifra de este reporte depende de historia no visible — toda medición es sobre el contenido de archivos en HEAD, no sobre cuándo cambiaron — pero cualquier pregunta de la forma "¿cuándo se corrigió X?" no se puede responder más allá de esos 4 commits, y se marca así donde aplica (M5).

## Alcance efectivamente leído

- `working/data_extraction/records/*.json` (1,178 archivos, completos, vía script)
- `working/data_extraction/extraction_converter_manifest.json`
- `working/data_extraction/rejected_archive_phase1b/` (vacío salvo `.gitkeep`)
- `working/signal_extraction/cards/*.json` (29 archivos, completos)
- `phases/01-source-intake/data-extraction/scripts/bulk_extract.py` (completo)
- `phases/01-source-intake/data-extraction/scripts/extraction_prepare.py` (docstring + encabezado)
- `phases/01-source-intake/data-extraction/scripts/test_e5_fixtures.py` (docstring + fixtures de `actor_level`)
- `phases/01-source-intake/data-extraction/contracts/data_extraction_contract.md` (sección `actor_level` + ejemplo mínimo)
- `phases/01-source-intake/data-extraction/modules/extraction_converter.md` (completo)
- `phases/01-source-intake/data-extraction/schemas/data_extraction_record.schema.json` (completo)
- `phases/02-signal-extraction/modules/signal_converter.md` (completo)
- `phases/02-signal-extraction/schemas/signal_card.schema.json` (enum `actor_level`)
- `.claude/skills/p2-extract-signals/SKILL.md` (completo)
- Otros `*.schema.json` que mencionan `actor_level` (grep de confirmación, no declaran enums propios distintos): `signal_inventory_gate.schema.json`, `signal_validation.schema.json`, `source_packet.schema.json` (`possible_actor_levels`), `data_extraction_validator.schema.json`

**Fuera de alcance, no leídos:** `pipeline_vocabulary.yaml` (citado por comentarios dentro de `bulk_extract.py`, pero no está en la lista cerrada de este encargo), `.claude/skills/extract-records/SKILL.md` (no está en la lista cerrada; su módulo normativo `extraction_converter.md` sí se leyó completo), cualquier archivo preexistente en `state/output/` distinto del que este encargo escribe.

---

## M1 — Universo y distribución

Total extraction records: **1,178** (conteo de archivos `*.json` en `working/data_extraction/records/` y conteo de `extraction_id` únicos tras parsear — ambos coinciden; 0 archivos malformados).

Schema que gobierna `actor_level` para extraction records: **`phases/01-source-intake/data-extraction/schemas/data_extraction_record.schema.json`**, propiedad `actor_level` (`oneOf`: string de un enum de 9 valores, o array de ese mismo enum). Enum: `buyer, seller, product, marketplace, platform, source, third_party, mixed, unknown`.

1,150 records llevan `actor_level` como string escalar; **28 lo llevan como array** (asignación multi-actor).

**Distribución escalar (n=1,150):**

| actor_level | count | ¿en enum? |
|---|---:|---|
| platform | 600 | sí |
| unknown | 305 | sí |
| seller | 141 | sí |
| buyer | 50 | sí |
| marketplace | 27 | sí |
| source | 10 | sí |
| third_party_observer | 10 | **NO** |
| creator | 5 | **NO** |
| mixed | 1 | sí |
| third_party | 1 | sí |
| **subtotal** | **1,150** | |

**Distribución en arrays (n=28):**

| actor_level (array) | count |
|---|---:|
| [marketplace, seller] | 12 |
| [seller, marketplace] | 11 |
| [marketplace, buyer] | 4 |
| [buyer, seller] | 1 |
| **subtotal** | **28** |

**Valores fuera del enum del schema:** 15 records (`third_party_observer`: 10, `creator`: 5). Ninguno de los 28 arrays contiene un valor fuera de enum. Estos dos valores son, textualmente, los mismos dos ejemplos que `signal_converter.md:159` cita como valores que "Phase 1 ha producido" fuera del vocabulario cerrado — la mención en el módulo de Phase 2 coincide con lo que efectivamente existe en el corpus.

---

## M2 — Cruce source_type × actor_level (los 1,178 records)

| source_type | total | platform | marketplace | seller | buyer | source | third_party | mixed | unknown | creator | third_party_observer | [mkt,sell] | [sell,mkt] | [mkt,buy] | [buy,sell] |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| help_center | 236 | 222 | 1 | 3 | 3 | 0 | 0 | 1 | 0 | 0 | 0 | 5 | 0 | 0 | 1 |
| blog | 198 | 60 | 10 | 43 | 1 | 4 | 0 | 0 | 70 | 0 | 7 | 1 | 2 | 0 | 0 |
| buyer_review | 118 | 0 | 0 | 38 | 18 | 0 | 0 | 0 | 62 | 0 | 0 | 0 | 0 | 0 | 0 |
| article | 105 | 37 | 0 | 11 | 6 | 0 | 0 | 0 | 51 | 0 | 0 | 0 | 0 | 0 | 0 |
| policy_page | 103 | 93 | 3 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 1 | 2 | 0 |
| platform_doc | 78 | 58 | 5 | 1 | 0 | 0 | 0 | 0 | 14 | 0 | 0 | 0 | 0 | 0 | 0 |
| unknown (source_type) | 65 | 0 | 0 | 8 | 19 | 0 | 0 | 0 | 36 | 0 | 2 | 0 | 0 | 0 | 0 |
| pricing_page | 52 | 46 | 2 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 |
| report | 51 | 7 | 2 | 9 | 0 | 4 | 0 | 0 | 21 | 0 | 1 | 1 | 6 | 0 | 0 |
| search_results_page | 46 | 44 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| product_listing | 44 | 24 | 0 | 3 | 1 | 2 | 0 | 0 | 14 | 0 | 0 | 0 | 0 | 0 | 0 |
| seller_forum | 41 | 2 | 2 | 18 | 1 | 0 | 0 | 0 | 11 | 5 | 0 | 1 | 0 | 1 | 0 |
| database_profile | 33 | 2 | 1 | 5 | 0 | 0 | 0 | 0 | 25 | 0 | 0 | 0 | 0 | 0 | 0 |
| news | 7 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 1 | 0 |
| interview | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **1,178** | 600 | 27 | 141 | 50 | 10 | 1 | 1 | 305 | 5 | 10 | 12 | 11 | 4 | 1 |

15 de los 18 valores de `source_type` del enum están presentes en el corpus. **`reddit`, `video_transcript` y `pdf` no aparecen ni una sola vez** en los 1,178 records.

---

## M3 — Subconjunto mecánicamente decidible

Nota de ubicación: el encargo cita la tabla de asignación como "`signal_converter.md` §4.3". En el archivo vigente, §4.3 es "Assess splitting need"; la tabla de seis filas (incluyendo el texto citado verbatim en el encargo) vive en §4.4, campo 3 (`actor_level`), líneas 144–155. El contenido coincide exactamente con lo citado — solo el número de sección está desplazado. No invalida la medición.

Filas mecánicas usadas (source_type solo, sin necesitar autor): `help_center/pricing_page/platform_doc/policy_page → platform`; `search_results_page/category_page → marketplace`; `product_listing → third_party`. Las filas de `blog/seller_forum/reddit` (autor-dependientes) quedan fuera de este subconjunto por instrucción explícita del encargo.

| source_type | actor_level predicho | total | coincide | no-coincide | tasa |
|---|---|---:|---:|---:|---:|
| help_center | platform | 236 | 222 | 14 | 94.1% |
| policy_page | platform | 103 | 93 | 10 | 90.3% |
| platform_doc | platform | 78 | 58 | 20 | 74.4% |
| pricing_page | platform | 52 | 46 | 6 | 88.5% |
| search_results_page | marketplace | 46 | 1 | 45 | 2.2% |
| product_listing | third_party | 44 | 0 | 44 | 0.0% |
| category_page | marketplace | 0 | — | — | no presente en el corpus ni en el enum de `source_type` |
| **TOTAL mecánico** | | **559** | **420** | **139** | **75.13%** |

**El agregado esconde una fractura fuerte por categoría predicha:**
- Grupo "platform" (help_center+policy_page+platform_doc+pricing_page): 419/469 = **89.3%**
- Grupo "marketplace" (search_results_page): 1/46 = **2.2%**
- Grupo "third_party" (product_listing): 0/44 = **0.0%**

`category_page` no existe en el enum `source_type` de `data_extraction_record.schema.json` ni en ningún record del corpus — la mitad de la fila 4 de la tabla no tiene territorio aquí.

---

## M4 — Subconjunto no cubierto

`source_type` sin fila alguna en la tabla de seis filas (ni mecánica ni autor-dependiente):

| source_type | records |
|---|---:|
| buyer_review | 118 |
| article | 105 |
| unknown (source_type) | 65 |
| report | 51 |
| database_profile | 33 |
| news | 7 |
| interview | 1 |
| **TOTAL** | **380** |

`source_type` con fila en la tabla pero no mecánica (autor-dependiente — necesita saber si el autor es comprador o vendedor):

| source_type | records |
|---|---:|
| blog | 198 |
| seller_forum | 41 |
| reddit | 0 (no presente en el corpus) |
| **TOTAL** | **239** |

**Territorio combinado que cualquier criterio nuevo tendría que cubrir por otra vía** (sin fila + fila no mecánica): 380 + 239 = **619 records** (52.5% del universo de 1,178).

Verificación cruzada: 559 (mecánico, M3) + 619 (no mecánico, M4) = 1,178 = universo total. Cuadra exacto.

---

## M5 — El productor

**Ruta y líneas vigentes:** `phases/01-source-intake/data-extraction/scripts/bulk_extract.py`, función `infer_actor_level(source_type, snippet)`, **líneas 185–212**.

**Orden real de evaluación:**
1. *(líneas 191–192)* Si `source_type` ∈ {`help_center`, `policy_page`, `platform_doc`, `pricing_page`} → retorna `'platform'` de inmediato. Rama incondicional: no hay ningún otro valor alcanzable para estos cuatro `source_type`, sin importar el contenido del snippet.
2. *(líneas 193–201)* Si no cayó en (1): pasa el snippet a minúsculas y aplica regex de vocabulario comprador (`buyer|customer|purchaser|patron|subscriber`) y vendedor (`seller|creator|shop\s*owner|vendor|author|instructor|artist`). Ambos → `mixed`. Solo comprador → `buyer`. Solo vendedor → `seller`.
3. *(líneas 202–211)* Si ningún regex golpeó: fallback por `source_type` — `database_profile`→`seller`, `buyer_review`→`buyer`, `product_listing`→`source`, {`reddit`,`seller_forum`,`blog`}→`seller`, {`article`,`report`,`news`}→`marketplace`.
4. *(línea 212)* Si nada aplicó → `'unknown'`.

El comentario en líneas 186–190 declara el orden como deliberado: las cuatro fuentes institucionales se resuelven antes del regex "para que una mención de 'buyer'/'seller' en el snippet no pueda sobreescribir quién habla realmente." Para el resto de `source_type`, el regex de vocabulario tiene prioridad sobre el fallback por tipo — el orden se invierte según el grupo.

**Mapeo completo vigente:**

| source_type | sin match de regex buyer/seller | con match de regex |
|---|---|---|
| help_center, policy_page, platform_doc, pricing_page | `platform` (incondicional) | `platform` (igual, el regex ni se evalúa) |
| database_profile | `seller` | `buyer`/`seller`/`mixed` según regex |
| buyer_review | `buyer` | `buyer`/`seller`/`mixed` según regex |
| product_listing | `source` | `buyer`/`seller`/`mixed` según regex |
| reddit, seller_forum, blog | `seller` | `buyer`/`seller`/`mixed` según regex |
| article, report, news | `marketplace` | `buyer`/`seller`/`mixed` según regex |
| search_results_page, category_page, interview, cualquier otro no listado | `unknown` | `buyer`/`seller`/`mixed` según regex |

**¿`pricing_page` tiene rama?** **Sí.** Línea 191, dentro de la lista incondicional junto con `help_center`, `policy_page`, `platform_doc`. No está fuera por omisión en el código vigente; el comentario de líneas 186–190 documenta la decisión explícitamente. No puedo verificar si estuvo ausente en una versión anterior — el clon es shallow y solo expone 4 commits para este archivo (ver R-G arriba) — pero el estado vigente en HEAD es inequívoco: la rama existe hoy.

**Records con `source_type: pricing_page` y su `actor_level` cargado:** 52 records — `platform`: 46, `[marketplace, seller]`: 2, `creator`: 2 (fuera de enum), `seller`: 1, `source`: 1.

### Diagnóstico — la presuposición de M5 no se sostiene

El encargo llama a `bulk_extract.py` "el productor" de los 1,178 records medidos en M1–M4, M6 y M7. Leyendo el código y el corpus vigentes en HEAD (ninguna de las siguientes cuatro observaciones requiere historia git), la evidencia muestra que **no lo es**:

1. **Huella textual ausente.** `process_skeleton()` (línea 560) escribe siempre el mismo `parser_notes` fijo y literal: `"bulk_extract_script: heuristic rules applied; verify subject_exact and claim_type for quality"`. Búsqueda exacta sobre los 1,178 records: **0 coincidencias**. Los 1,178 tienen `parser_notes` únicos y específicos de contenido (fechas, cifras, nombres de fuente) — incompatibles con la salida fija de esta función.

2. **Salidas matemáticamente imposibles.** Para los cuatro `source_type` con rama incondicional (`help_center`, `policy_page`, `platform_doc`, `pricing_page`), la función solo puede devolver `'platform'` — no existe otro camino en el código, para ningún snippet. Extendiendo el mismo análisis a `search_results_page` y `product_listing` (que sí tienen ramas alcanzables vía regex): de los 139 desajustes del subconjunto mecánico de M3, **132 (95.0%) son valores que el código vigente no puede producir bajo ninguna entrada**, dado su `source_type`. Solo 7 de los 139 son teóricamente alcanzables (requerirían vocabulario específico de comprador/vendedor en el snippet).

3. **El propio script se declara aparte del flujo de producción.** `test_e5_fixtures.py`, mismo directorio, docstring: *"Regression fixtures for FICHA E5a ... and FICHA E5b (infer_actor_level vs pipeline_vocabulary.yaml assignment_rule) ... Not wired into CI — that is a separate, un-taken decision."* Es un script de ficha (E5a/E5b), validado con fixtures aisladas, nunca conectado a CI.

4. **El módulo normativo de esta etapa nombra otro ejecutor.** `extraction_converter.md` línea 9: *"This module is executed by the `extract-records` skill"* — skill declarada en línea 252 como `.claude/skills/extract-records/SKILL.md`, no `bulk_extract.py`. `CLAUDE.md` nombra la misma etapa "p1-extract-records" en su tabla de navegación de Phase 1. Por la jerarquía de autoridad del propio repo (el módulo es la especificación normativa de la etapa), el productor documentado es la skill, no este script.

**Quién parece haber producido los 1,178 records:** la skill `extract-records`, aplicando `data_extraction_contract.md` por juicio, no `bulk_extract.py` por heurística determinística. Esto es una inferencia sostenida por los cuatro puntos anteriores, no una remedición directa — no hay log de ejecución de skill dentro del alcance leído para confirmarlo de forma mecánica, y se marca como tal.

**Consecuencia para el resto de este reporte:** M1–M4, M6 y M7 miden el corpus real y no cambian — no dependen de qué proceso lo produjo. Lo que cambia es el ancla causal para el veredicto: el contrato que gobierna a la skill real es `data_extraction_contract.md`, no `bulk_extract.py`. Su sección `actor_level` (líneas 209–217) enumera **7 valores permitidos** (`buyer, seller, product, marketplace, source, mixed, unknown`) y **no menciona `platform` ni `third_party`**, pese a que el schema exige 9 valores y pese a que `platform` es el valor más frecuente del corpus (600 de 1,178). El contrato tampoco define ninguna tabla `source_type → actor_level`: esa tabla aparece por primera vez, río abajo, en `signal_converter.md` §4.4 (Phase 2), como mecanismo de normalización condicional — no como regla que Phase 1 tuviera disponible al momento de decidir.

---

## M6 — Las 29 cards

Join: `source_record_ids` de la card contra `extraction_id` del record. **Las 29 cards joinean 1:1 con exactamente un record cada una — 0 cards sin join, 0 cards con más de un `source_record_id`.**

**Re-medición de las seis cifras de procedencia:**

| Cifra | DSC (procedencia) | Re-medida aquí | ¿Coincide? |
|---|---|---:|---|
| Extraction records indexados | 1,178 | 1,178 | Sí |
| Signal cards | 29 | 29 | Sí |
| Cards con override explícito de `actor_level` en `normalization_notes` | 28 de 29 | 28 de 29 | Sí |
| Cards cuyo `actor_level` heredado era `unknown` | 0 | 0 | Sí |
| Cards donde la tabla de source-type predice el valor final | 12 | 12 | Sí |
| Cards cuyo `source_type` no tiene fila mecánica en la tabla | 16 | 16 | Sí |

Único card sin mención de `actor_level` en `normalization_notes`: `SC-R1-017` — su valor heredado (`marketplace`, de un record `search_results_page`) ya coincidía con el valor final; no hubo nada que anotar como cambio.

**Detalle completo por card** (source_type y actor_level heredado del record joineado, predicción de la tabla mecánica si aplica, valor final de la card):

| signal_id | source_type | actor_level heredado (record) | predicción tabla mecánica | actor_level final (card) | ¿tabla predice el final? |
|---|---|---|---|---|---|
| SC-R1-001 | product_listing | source | third_party | third_party | Sí |
| SC-R1-002 | article | seller | — (sin fila) | source | — |
| SC-R1-003 | article | seller | — (sin fila) | source | — |
| SC-R1-004 | product_listing | buyer | third_party | third_party | Sí |
| SC-R1-005 | product_listing | source | third_party | third_party | Sí |
| SC-R1-006 | product_listing | seller | third_party | third_party | Sí |
| SC-R1-007 | article | seller | — (sin fila) | source | — |
| SC-R1-008 | article | seller | — (sin fila) | source | — |
| SC-R1-009 | database_profile | seller | — (sin fila) | source | — |
| SC-R1-010 | database_profile | seller | — (sin fila) | source | — |
| SC-R1-011 | database_profile | marketplace | — (sin fila) | third_party | — |
| SC-R1-012 | database_profile | seller | — (sin fila) | source | — |
| SC-R1-013 | database_profile | seller | — (sin fila) | source | — |
| SC-R1-014 | database_profile | seller | — (sin fila) | source | — |
| SC-R1-015 | product_listing | seller | third_party | third_party | Sí |
| SC-R1-016 | product_listing | seller | third_party | third_party | Sí |
| SC-R1-017 | search_results_page | marketplace | marketplace | marketplace | Sí |
| SC-R1-018 | blog | seller | — (fila autor-dependiente, no mecánica) | third_party | — |
| SC-R1-019 | seller_forum | [marketplace, seller] | — (fila autor-dependiente, no mecánica) | platform | — |
| SC-R1-020 | pricing_page | marketplace | platform | source | **No** |
| SC-R1-021 | help_center | mixed | platform | platform | Sí |
| SC-R1-022 | help_center | [buyer, seller] | platform | platform | Sí |
| SC-R1-023 | help_center | seller | platform | platform | Sí |
| SC-R1-024 | help_center | seller | platform | platform | Sí |
| SC-R1-025 | help_center | seller | platform | platform | Sí |
| SC-R1-1179 | article | seller | — (sin fila) | source | — |
| SC-R1-1180 | article | seller | — (sin fila) | source | — |
| SC-R1-1181 | database_profile | seller | — (sin fila) | source | — |
| SC-R1-1182 | database_profile | seller | — (sin fila) | source | — |

De las 13 cards cuyo `source_type` sí tiene fila mecánica, 12 coinciden con la predicción y 1 (`SC-R1-020`, `pricing_page`) no. Nótese que la tasa a nivel de card (12/13 = 92.3%) es sustancialmente más alta que la tasa a nivel de record (M3: 75.13%) — es lo esperable, no una segunda medición independiente de lo mismo: Phase 2 (`signal_converter.md`) aplica esta misma tabla como su mecanismo de corrección, así que las cards reflejan la tabla casi por construcción. M6 mide qué tan bien quedó la corrección de Phase 2, no la confiabilidad de Phase 1 — para eso está M3.

---

## M7 — unknown

Records con `actor_level: unknown` (escalar): **305**. Ningún valor `"unknown"` aparece dentro de ninguno de los 28 arrays. El pendiente del proyecto que cita 305 **coincide exactamente** — confirmado, no corregido.

---

## Veredicto

**Umbral declarado para CONFIABLE: ≥90% de acierto en el subconjunto mecánicamente decidible de M3.**

Razón del umbral: `actor_level` es un campo de juicio fundacional — identifica quién habla en cada observación y alimenta directamente los scanners de Phase 3 (asimetrías, contradicciones, direcciones opuestas) que comparan señales entre polos. El subconjunto de M3 es, por diseño del propio encargo, la parte del problema *sin* ambigüedad genuina: `source_type` solo, sin necesitar leer quién es el autor. Es la parte fácil. Si la parte fácil falla más de aproximadamente 1 de cada 10 veces, el defecto no es "casos límite que podían caer para cualquier lado" — es que la regla mecánica, disponible o no, no se está aplicando consistentemente. 90% refleja ese estándar: no more than 1-in-10 en la porción del problema que no debería requerir juicio alguno.

### **NO-CONFIABLE**

75.13% (420/559) < 90%. Con n=559, el intervalo de confianza normal al 95% es 75.13% ± 3.6% — el resultado no roza el umbral por azar de muestra pequeña.

**R-D — forma de la causa raíz, anclada en M5 (con su corrección):** **rama faltante, pero en el contrato de Phase 1, no en un script.** El proceso real que llenó `actor_level` (la skill `extract-records`, per M5) operó bajo `data_extraction_contract.md`, que nunca definió una tabla `source_type → actor_level`. Su única instrucción es identificar "quién habla" contra un enum de 7 valores que ni siquiera incluye `platform` o `third_party`. La tabla de seis filas que sí mecaniza este mapeo aparece recién en Phase 2 (`signal_converter.md` §4.4) como parche condicional aplicado después del hecho — nunca estuvo disponible para Phase 1 al momento de decidir. Esto explica la fractura vista en M3: los `source_type` "institucionales" (`help_center`, `policy_page`, `platform_doc`) alcanzaron una tasa razonable (74–94%) probablemente porque "quién habla" es intuitivamente obvio en ese contenido incluso sin tabla explícita — mientras que los casos que sí exigen distinguir entre categorías vecinas (`search_results_page`: ¿marketplace hablando o contenido genérico?; `product_listing`, sobre todo: ¿third-party promocionando su propio producto, o marketplace, o "source" genérico?) no tenían guía mecánica alguna y colapsaron a 2.2% y 0.0% respectivamente.

**Por qué no INDETERMINADA:** el subconjunto decidible de M3 (559 records) es el 47.5% del universo de 1,178 — ni una porción marginal ni una muestra pequeña (n=559 sostiene el intervalo de ±3.6% citado arriba, muy lejos de poder rozar 90% por ruido). Frente a M4 (619 records, 52.5%) es de tamaño comparable, prácticamente mitad y mitad — no "demasiado chico frente a M4" en ningún sentido razonable. INDETERMINADA no aplica.

---

## R-E — Barrera

**Ausente.** Ni `data_extraction_contract.md` ni `extraction_converter.md` (el módulo que gobierna la promoción de un record a `records/`) contienen un chequeo que cruce `source_type` contra `actor_level` antes de escribir el record. Los "Promotion criteria" de `extraction_converter.md` verifican solo: validación de schema, ausencia de campos requeridos nulos, y validez estructural del skeleton — ninguno de los tres es una verificación de consistencia interna entre `source_type` y `actor_level`.

La única verificación de esta clase que existe en el material leído vive en Phase 2 (`signal_converter.md` §4.4, campo 3), y es: (a) posterior — corre después de que el record ya fue promovido y consumido por Signal Extraction, no antes de escribirlo; (b) condicional — solo se activa si el valor heredado es `unknown` o si la formulación del signal_text "revela" imprecisión, no como auditoría sistemática de los 1,178 records; (c) no produce una métrica de tasa de coincidencia — el hallazgo de esta corrida (75.13% agregado, 0.0% en `product_listing`) no estaba capturado en ningún manifest ni artefacto anterior a esta corrida.

No se propone construir esta barrera — solo se declara su ausencia, por instrucción del encargo.

---

Sin recomendaciones más allá de lo pedido. No se propone qué hacer con P-127, con el corpus, ni con el código.
