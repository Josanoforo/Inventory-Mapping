# vocab_check.py — blind spot measurement

Read-only measurement pass. No schemas, `pipeline_vocabulary.yaml`, `vocab_check.py`,
or the ledger were modified. No sync, no siding with schema or vocab, no match-mode
changes proposed.

Precondition verified: PR #73 (`Josanoforo/claude/ledger-uncertainties-schema-drift`)
is merged into `main` (merge commit `6235136`). Local `main` ref was stale before this
pass (`56364a6` vs `origin/main` `6235136`) — re-fetched and rebased the working branch
onto fresh `origin/main` before measuring.

Corpus measured: `working/data_extraction/records/*.json`, 1,178 files.

---

## BLOQUE 0 — El caso concreto: `uncertainties`

**Schema** — `phases/01-source-intake/data-extraction/schemas/data_extraction_record.schema.json:340-357`
(16 values):

```
subject_ambiguity, actor_level_unclear, time_scope_unclear, source_date_unclear,
metric_unit_unclear, context_insufficient, checkout_vs_payout_ambiguity,
net_vs_gross_ambiguity, current_vs_historical_ambiguity, platform_scope_unclear,
product_type_unclear, geography_unclear, methodology_unclear, anecdotal_single_source,
author_conflict_of_interest_possible, none
```

**Vocab** — `pipeline_vocabulary.yaml:138-166`, field `uncertainties`, `match: subset`:

- `core:` (`pipeline_vocabulary.yaml:141-155`, 14 values) — subject_ambiguity,
  actor_level_unclear, time_scope_unclear, source_date_unclear, context_insufficient,
  checkout_vs_payout_ambiguity, net_vs_gross_ambiguity, current_vs_historical_ambiguity,
  product_type_unclear, geography_unclear, none, methodology_unclear,
  anecdotal_single_source, author_conflict_of_interest_possible
- `phase_1_only:` (`pipeline_vocabulary.yaml:157-160`, 3 values) — source_type_unclear,
  metric_type_unclear, snippet_needs_reopen
- `phase_2_only:` (`pipeline_vocabulary.yaml:161-163`, 2 values) — metric_unit_unclear,
  platform_scope_unclear

Vocab total (core ∪ phase_1_only ∪ phase_2_only) = 19 values.

### Tres conjuntos

- **Solo en schema** (schema tiene, vocab no): **ninguno**. Los 16 valores del schema
  están todos dentro del conjunto vocab de 19.
- **Solo en vocab** (vocab tiene, schema no): **3 valores, los tres marcados
  `phase_1_only`** — es decir, la propia etiqueta de scope del vocab dice que
  pertenecen a este schema (Phase 1) y el schema no los declara:
  - `source_type_unclear`
  - `metric_type_unclear`
  - `snippet_needs_reopen`
- **En ambos**: los 16 valores del schema (14 `core` + 2 marcados `phase_2_only` que el
  schema de Phase 1 igual declara: `metric_unit_unclear`, `platform_scope_unclear`).

### Uso en los 1,178 records, valores "solo en vocab"

| valor | records que lo usan |
|---|---|
| `source_type_unclear` | 0 |
| `metric_type_unclear` | 0 |
| `snippet_needs_reopen` | 0 |

Ningún record usa hoy los tres valores que el schema no declara.

(Nota de contexto, no evaluativa: el schema también declara dos valores marcados
`phase_2_only` en el vocab — `metric_unit_unclear` (5 records) y
`platform_scope_unclear` (0 records) — que caen del lado "en ambos" del conjunto
porque el vocab los incluye en su unión total, aunque su etiqueta de scope diga
Phase 2.)

---

## BLOQUE 1 — La clase: campos `match: subset` en `vocab_check.py`

### Campos y modo de match

Todos los campos de nivel superior de `pipeline_vocabulary.yaml` que tienen entradas
tipo dict, con su modo de match. Default es `exact` cuando no se declara `match:`
(`vocab_check.py:9,173`).

| campo (vocab key) | schema_field | match | ruta:línea de declaración |
|---|---|---|---|
| actor | actor, actor_level | exact (default) | — (sin `match:` en `pipeline_vocabulary.yaml:13-45`) |
| metric_type | metric_type | exact (default) | — (`pipeline_vocabulary.yaml:47-69`) |
| evidence_role | evidence_role | exact (default) | — (`pipeline_vocabulary.yaml:71-84`) |
| source_type | source_type | exact (default) | — (`pipeline_vocabulary.yaml:86-105`) |
| product_type_if_explicit | product_type_if_explicit | exact (default) | — (`pipeline_vocabulary.yaml:107-120`) |
| pointer_type | pointer_type | **subset** | `pipeline_vocabulary.yaml:123` |
| uncertainties | uncertainties | **subset** | `pipeline_vocabulary.yaml:139` |
| verification_status | verification_status | exact (default) | — (`pipeline_vocabulary.yaml:172-187`) |
| claim_type | claim_type | exact (default) | — (`pipeline_vocabulary.yaml:193-206`) |
| retrieval_method | retrieval_method | exact (default) | — (`pipeline_vocabulary.yaml:208-217`) |
| priority_for_source_first | priority_for_source_first | exact (default) | — (`pipeline_vocabulary.yaml:219-221`) |
| traceability_status | traceability_status | exact (default) | — (`pipeline_vocabulary.yaml:223-225`) |
| tension_type | type | exact (default) | — (`pipeline_vocabulary.yaml:231-243`) |
| tension_status | status | exact (default) | — (`pipeline_vocabulary.yaml:245-253`) |
| classification_risk | classification_risk | exact (default) | — (`pipeline_vocabulary.yaml:255-266`) |
| scan_routing | routing | exact (default) | — (`pipeline_vocabulary.yaml:268-279`) |
| scan_type | scan_type | exact (default) | — (`pipeline_vocabulary.yaml:281-290`) |
| domain | domain | exact (default) | — (`pipeline_vocabulary.yaml:292-303`) |
| extraction_status | extraction_status | exact (default) | — (`pipeline_vocabulary.yaml:305-307`) |
| check_status | status | exact (default) | — (`pipeline_vocabulary.yaml:315-326`) |
| manifest_status | status | **subset** | `pipeline_vocabulary.yaml:330` |
| allowed_verbs | allowed_verbs | exact (default) | — (`pipeline_vocabulary.yaml`, sin ocurrencia en schemas) |
| forbidden_language | forbidden_language | exact (default) | — (`pipeline_vocabulary.yaml`, sin ocurrencia en schemas) |

Tres campos declaran `match: subset`: **pointer_type**, **uncertainties**, **manifest_status**.

### Cita literal — lógica que implementa `subset` y apaga la dirección "missing"

`vocab_check.py:200-212`:

```python
    divergences = []
    for declared_set, files in enum_occurrences.items():
        missing = (vocab_values - optional) - declared_set
        extra = declared_set - vocab_values
        if match_mode == "subset":
            missing = set()
        if missing or extra:
            divergences.append({
                "files": sorted(files),
                "declared": sorted(declared_set),
                "missing": sorted(missing),
                "extra": sorted(extra),
            })
```

`missing` (valores que el vocab declara y el schema no) se calcula igual que en modo
`exact`, pero en `match_mode == "subset"` se pisa con `set()` antes de decidir si hay
divergencia. Esa dirección nunca dispara para un campo `subset`, sin importar cuántos
valores falten en el schema — solo `extra` (schema tiene, vocab no) puede producir un
reporte.

### Los otros dos campos `subset`: ¿tienen la misma ceguera?

**`pointer_type`** — schema declarado en tres archivos:

- `phases/02-signal-extraction/schemas/signal_card.schema.json:336-344`: 8 valores
  (incluye `source_record_ref`)
- `phases/01-source-intake/schemas/source_packet.schema.json:276-283`: 7 valores (sin
  `source_record_ref`)
- `phases/01-source-intake/data-extraction/schemas/data_extraction_record.schema.json:378-385`:
  7 valores (sin `source_record_ref`)

Vocab (`pipeline_vocabulary.yaml:124-132`): mismos 8 valores, con `source_record_ref`
marcado `optional` (`pipeline_vocabulary.yaml:134`). Los tres conjuntos de schema son
subconjuntos exactos del vocab — **no hay valores del vocab ausentes de ningún schema
más allá de lo ya declarado `optional`**. `pointer_type` no tiene la ceguera de
`uncertainties`.

**`manifest_status`** — schema declarado en ocho archivos `*manifest.schema.json`, con
tres conjuntos distintos de valores:

| conjunto declarado | archivos | valores del vocab ausentes (ceguera) |
|---|---|---|
| `{in_progress, complete}` | `phases/02-signal-extraction/schemas/signal_prepare_manifest.schema.json:26-29`, `phases/01-source-intake/data-extraction/schemas/extraction_prepare_manifest.schema.json:25-28` | `pending`, `failed`, `blocked_by_stage_1_incomplete` |
| `{in_progress, complete, failed}` | `phases/03-inventory-mapping/schemas/split_manifest.schema.json:8-10`, `phases/03-inventory-mapping/schemas/index_manifest.schema.json:8-10` | `pending`, `blocked_by_stage_1_incomplete` |
| `{pending, in_progress, complete, failed, blocked_by_stage_1_incomplete}` | `phases/02-signal-extraction/schemas/signal_converter_manifest.schema.json:26-31`, `phases/01-source-intake/schemas/converter_manifest.schema.json:26-31`, `phases/01-source-intake/data-extraction/schemas/extraction_converter_manifest.schema.json:24-29` | ninguno — igual al vocab |

Vocab completo (`pipeline_vocabulary.yaml:334-338`): `pending, in_progress, complete,
failed, blocked_by_stage_1_incomplete`.

**`manifest_status` tiene la misma ceguera que `uncertainties`**: cinco de los ocho
schemas declaran menos valores que el vocab, y `vocab_check.py` no lo reporta porque
`missing` se descarta en modo `subset`.

### Uso en el corpus, dirección ciega de `manifest_status`

Instancias de manifest encontradas en `working/` (no hay instancias de
`split_manifest.json` ni `index_manifest.json` todavía — esos pasos de Phase 3 no se
han corrido):

| archivo instancia | status actual | ¿en la dirección ciega de su schema? |
|---|---|---|
| `working/signal_extraction/signal_prepare_manifest.json` | `complete` | no |
| `working/signal_extraction/signal_converter_manifest.json` | `in_progress` | no |
| `working/data_extraction/extraction_prepare_manifest.json` | `complete` | no |
| `working/data_extraction/extraction_converter_manifest.json` | `complete` | no |
| `working/source_intake/converter_prepare_manifest.json` | `complete` | no |
| `working/source_intake/converter_manifest.json` | `complete` | no |

0 de 6 instancias de manifest usan hoy un valor que caiga en la dirección ciega de su
propio schema.

---

## BLOQUE 2 — Qué más está ciego

### Schemas con enums que NO están en la configuración de `vocab_check.py`

Propiedades con `"enum"` en algún `*.schema.json` (fuera de `working/`) cuyo nombre de
propiedad no coincide con ningún `schema_field` / key configurado en
`pipeline_vocabulary.yaml`:

| archivo | propiedad |
|---|---|
| `phases/01-source-intake/data-extraction/schemas/data_extraction_validator.schema.json` | `validation_status` |
| `phases/01-source-intake/data-extraction/schemas/data_extraction_validator.schema.json` | `failures` |
| `phases/01-source-intake/data-extraction/schemas/extraction_converter_manifest.schema.json` | `destination` |
| `phases/01-source-intake/data-extraction/schemas/extraction_converter_manifest.schema.json` | `issues_for_this_record` |
| `phases/01-source-intake/data-extraction/schemas/extraction_prepare_manifest.schema.json` | `issue_type` |
| `phases/01-source-intake/schemas/converter_manifest.schema.json` | `destination` |
| `phases/01-source-intake/schemas/converter_manifest.schema.json` | `issues_for_this_packet` |
| `phases/01-source-intake/schemas/converter_manifest.schema.json` | `issue_type` |
| `phases/01-source-intake/schemas/converter_prepare_manifest.schema.json` | `issue_type` |
| `phases/01-source-intake/schemas/rejected_archive_record.schema.json` | `reason_code` |
| `phases/01-source-intake/schemas/source_intake_validation.schema.json` | `validation_status` |
| `phases/01-source-intake/schemas/source_intake_validation.schema.json` | `failures` |
| `phases/01-source-intake/schemas/source_packet.schema.json` | `possible_actor_levels` |
| `phases/01-source-intake/schemas/source_packet.schema.json` | `possible_metric_types` |
| `phases/02-signal-extraction/schemas/signal_converter_manifest.schema.json` | `issues_for_this_skeleton` |
| `phases/02-signal-extraction/schemas/signal_converter_manifest.schema.json` | `destination` |
| `phases/02-signal-extraction/schemas/signal_inventory_gate.schema.json` | `validation_status` |
| `phases/02-signal-extraction/schemas/signal_inventory_gate.schema.json` | `entry_gate_decision` |
| `phases/02-signal-extraction/schemas/signal_inventory_gate.schema.json` | `failure_reasons` |
| `phases/02-signal-extraction/schemas/signal_inventory_gate.schema.json` | `isolated_signal_reason` |
| `phases/02-signal-extraction/schemas/signal_prepare_manifest.schema.json` | `issue_type` |
| `phases/02-signal-extraction/schemas/signal_validation.schema.json` | `validation_status` |
| `phases/02-signal-extraction/schemas/signal_validation.schema.json` | `failures` |
| `phases/03-inventory-mapping/schemas/index_manifest.schema.json` | `severity` |

Nota: `validation_status` aparece en cuatro archivos distintos
(`data_extraction_validator.schema.json`, `source_intake_validation.schema.json`,
`signal_inventory_gate.schema.json`, `signal_validation.schema.json`) con conjuntos de
valores que no son idénticos entre sí (p. ej. `source_intake_validation.schema.json`
incluye `parking_lot`, los otros tres no) — observación mecánica, sin evaluar cuál lado
tiene razón.

### Direcciones verificadas por campo comparado

| campo | match | ¿verifica "missing" (vocab→schema)? | ¿verifica "extra" (schema→vocab)? |
|---|---|---|---|
| actor | exact | sí | sí |
| metric_type | exact | sí | sí |
| evidence_role | exact | sí | sí |
| source_type | exact | sí | sí |
| product_type_if_explicit | exact | sí | sí |
| pointer_type | subset | **no** | sí |
| uncertainties | subset | **no** | sí |
| verification_status | exact | sin ocurrencia en schemas — no aplica | sin ocurrencia en schemas — no aplica |
| claim_type | exact | sí | sí |
| retrieval_method | exact | sí | sí |
| priority_for_source_first | exact | sí | sí |
| traceability_status | exact | sí | sí |
| tension_type | exact | sí | sí |
| tension_status | exact | sí | sí |
| classification_risk | exact | sí | sí |
| scan_routing | exact | sí | sí |
| scan_type | exact | sí | sí |
| domain | exact | sí | sí |
| extraction_status | exact | sí | sí |
| check_status | exact | sí | sí |
| manifest_status | subset | **no** | sí |
| allowed_verbs | exact | sin ocurrencia en schemas — no aplica | sin ocurrencia en schemas — no aplica |
| forbidden_language | exact | sin ocurrencia en schemas — no aplica | sin ocurrencia en schemas — no aplica |

Ningún campo configurado tiene cobertura "ninguna" en ambas direcciones cuando sí
ocurre en algún schema — los tres campos `subset` cubren solo `extra`.

Los 24 campos de enum listados arriba (schemas fuera de configuración) tienen
cobertura "ninguna" en ambas direcciones, porque `vocab_check.py` nunca los toca: no
existen como key en `pipeline_vocabulary.yaml`, así que el loop en
`vocab_check.py:244` (`for field_name, entry in vocab.items()`) jamás los visita.

---

## BLOQUE 4 — Parada

Sin veredicto sobre qué lado (schema o vocab) es correcto. Sin propuesta de cambiar
`match: subset` a otro modo. Sin estimación de esfuerzo de reparación.
