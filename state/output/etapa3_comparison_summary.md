# Etapa 3 — resumen de comparacion determinista

Generado por `state/scripts/etapa3_compare.py`. El script compara; no adjudica.

## Procedencia

| | Sonnet | Fable |
|---|---|---|
| Rama | `claude/etapa-2-field-extraction-jyqwwj` | `claude/etapa-2-extraccion-juicio-gwnfk4` |
| Commit | `df28768bf9a2eb0e28ed529ef267aad934a9ba0e` | `7c94dd17a834d6b75e675b38d4a9825bd65b2758` |
| Records | 1173 | 1172 |
| Rechazos | 5 | 6 |

## Universo comparado

Universo = extraction_id presentes como record en AMBAS ramas.
Los rechazos quedan fuera del universo y se reportan aparte.

| Metrica | N |
|---|---|
| Universo comparado (records en ambas ramas) | 1172 |
| Solo en Sonnet | 1 |
| Solo en Fable | 0 |
| Records identicos campo a campo | 0 |
| Records con al menos una diferencia | 1172 |
| — con al menos un desacuerdo (A) o (B) | 1172 |
| — solo diferencias de orden (C) | 0 |

## Normalizacion aplicada

Unicamente `strip` de whitespace de bordes en strings, recursivo en
listas y objetos. Sin normalizacion de mayusculas, sinonimos ni
agrupacion de valores parecidos.

Categorias, contadas por separado y sin mezclarse:

- **(A) divergencia de valor** — ambos con valor, valores distintos.
- **(B) presencia vs ausencia** — uno con valor, el otro null / `[]` / ausente.
- **(C) orden en arrays** — mismos elementos (multiconjunto identico), distinto orden.

Para arrays: si los multiconjuntos coinciden y el orden difiere, es (C);
si los multiconjuntos difieren, es (A), o (B) si un lado esta vacio.

## Integridad — campos mecanicos

Campos que vienen del skeleton y deben ser identicos en ambos corpus.
Cualquier divergencia aqui es bug de integridad, no desacuerdo de juicio.

**Bugs de integridad: 0**

| Campo mecanico | (A) | (B) | (C) |
|---|---:|---:|---:|
| `extraction_id` | 0 | 0 | 0 |
| `source_packet_id` | 0 | 0 | 0 |
| `source_id` | 0 | 0 | 0 |
| `source_type` | 0 | 0 | 0 |
| `source_title` | 0 | 0 | 0 |
| `source_ref` | 0 | 0 | 0 |
| `source_date_if_available` | 0 | 0 | 0 |
| `snippet_primary` | 0 | 0 | 0 |
| `snippet_context_before` | 0 | 0 | 0 |
| `snippet_context_after` | 0 | 0 | 0 |
| `traceability_pointer` | 0 | 0 | 0 |

Campos mecanicos declarados pero ausentes en ambos corpus (no comparables):
- `_source_snippet_id`

## Campos de juicio — conteo por campo

Lista derivada de los propios records (todos los campos observados
menos los mecanicos), no hardcodeada.

| Campo | (A) valor | (B) presencia | (C) orden | total |
|---|---:|---:|---:|---:|
| `actor_level` | 100 | 0 | 0 | 100 |
| `author_or_actor_if_available` | 0 | 0 | 0 | 0 |
| `claim_type` | 332 | 0 | 0 | 332 |
| `evidence_role` | 239 | 0 | 0 | 239 |
| `geography_if_explicit` | 62 | 39 | 0 | 101 |
| `local_qualifiers` | 506 | 502 | 0 | 1008 |
| `metric_type` | 369 | 0 | 0 | 369 |
| `metric_unit` | 356 | 109 | 0 | 465 |
| `metric_value_raw` | 298 | 114 | 0 | 412 |
| `parser_notes` | 260 | 822 | 0 | 1082 |
| `platforms` | 176 | 424 | 35 | 635 |
| `product_type_if_explicit` | 62 | 0 | 0 | 62 |
| `subject_exact` | 1172 | 0 | 0 | 1172 |
| `time_scope_normalized_if_safe` | 11 | 233 | 0 | 244 |
| `time_scope_raw` | 127 | 464 | 0 | 591 |
| `uncertainties` | 470 | 505 | 1 | 976 |
| **TOTAL** | **4540** | **3212** | **36** | **7788** |

### Campos presentes en un corpus y no en el otro

Ninguno: ambos corpus usan el mismo conjunto de claves.

## Elegibilidad de muestreo — campos de enum

Criterio revisado (paso 3): un record es elegible para la muestra si
tiene al menos un desacuerdo (A) o (B) en un CAMPO DE ENUM, no en
cualquier campo. Los campos de enum se derivan del schema
`phases/01-source-intake/data-extraction/schemas/data_extraction_record.schema.json`,
recorriendo cada propiedad top-level en busca de `enum` directo, dentro
de `oneOf`, o en `items` de un array.

**Campos de enum declarados por el schema:**

- `source_type` _(excluido: mecanico)_
- `claim_type`
- `actor_level`
- `product_type_if_explicit`
- `metric_type`
- `evidence_role`
- `uncertainties`
- `traceability_pointer` _(excluido: mecanico)_

**Campos de elegibilidad (enum, menos mecanicos):**

- `claim_type`
- `actor_level`
- `product_type_if_explicit`
- `metric_type`
- `evidence_role`
- `uncertainties`

Los desacuerdos en campos de texto libre (`subject_exact`,
`local_qualifiers`, `metric_value_raw`, `metric_unit`, `time_scope_raw`,
`time_scope_normalized_if_safe`, `geography_if_explicit`,
`parser_notes`, `platforms`, `author_or_actor_if_available`) no hacen
elegible a un record por si solos, pero se siguen mostrando en su
bloque de adjudicacion si el record entro por otra via.

**Contraste: elegibles bajo el criterio anterior (cualquier campo) vs
el criterio de enum, por estrato:**

| Estrato | Elegibles — criterio anterior | Elegibles — criterio enum |
|---|---:|---:|
| E1 | 399 | 344 |
| E2 | 595 | 590 |
| E3 | 178 | 173 |
| **TOTAL** | **1172** | **1107** |

## Muestreo estratificado

**Semilla: `20260803`** (fija y declarada; la muestra es reproducible).

Muestra objetivo: ~60 casos. Solo entran extraction_id con al menos un
desacuerdo (A) o (B) en un CAMPO DE ENUM (elegibilidad). Los de tipo (C)
y los desacuerdos exclusivamente en campos de texto libre no entran a
la muestra. Reparto proporcional por mayor-resto sobre los elegibles de
cada estrato.

| Estrato | Batches | Elegibles (enum A/B) | Cuota | Tomados | Deficit |
|---|---|---:|---:|---:|---:|
| E1 | batch_001–batch_016 | 344 | 19 | 19 | 0 |
| E2 | batch_017–batch_040 | 590 | 32 | 32 | 0 |
| E3 | batch_041–batch_048 | 173 | 9 | 9 | 0 |
| **TOTAL** | | **1107** | **60** | **60** | **0** |

## Rechazos (fuera del universo comparado)

Solo IDs y de que lado. Sin analisis.

| Categoria | N |
|---|---:|
| Rechazados por ambos | 5 |
| Rechazados solo por Sonnet | 0 |
| Rechazados solo por Fable | 1 |

| extraction_id | Sonnet | Fable |
|---|:---:|:---:|
| `ER-SP-compass_artifact_wf-de144e73-98a7-403c-a882-9327b9dbadd2_text_markdown-008-SNP-001` | rechazado | rechazado |
| `ER-SP-compass_artifact_wf-de144e73-98a7-403c-a882-9327b9dbadd2_text_markdown-011-SNP-001` | rechazado | rechazado |
| `ER-SP-compass_artifact_wf-de144e73-98a7-403c-a882-9327b9dbadd2_text_markdown-012-SNP-001` | rechazado | rechazado |
| `ER-SP-compass_artifact_wf-de144e73-98a7-403c-a882-9327b9dbadd2_text_markdown-015-SNP-001` | rechazado | rechazado |
| `ER-SP-compass_artifact_wf-de144e73-98a7-403c-a882-9327b9dbadd2_text_markdown-016-SNP-001` | rechazado | rechazado |
| `ER-SP-compass_artifact_wf-0ffe7308-62e3-4530-ae68-93720df60f34_text_markdown-012-SNP-002` | record | rechazado |

