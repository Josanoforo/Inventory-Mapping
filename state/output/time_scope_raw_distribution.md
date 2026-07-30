# time_scope_raw — distribución de forma, mecanismo de pérdida y cruce con el detector

Medición mecánica, solo lectura, fecha 2026-07-30. Ningún archivo existente fue
modificado; no se re-corrió ninguna fase; el detector se ejecutó tal como está.

## Bloque 0 — Inventario

| Objeto | Ruta | Conteo |
|---|---|---|
| Extraction Records | `working/data_extraction/records/*.json` | 1,178 |
| Skeletons (48 batches) | `working/signal_extraction/skeleton_batches/batch_001/ … batch_048/` | 1,178 |
| Schema Extraction Record | `phases/01-source-intake/data-extraction/schemas/data_extraction_record.schema.json` | 1 |
| Módulo converter | `phases/02-signal-extraction/modules/signal_converter.md` | 1 |
| Script markdown | `phases/02-signal-extraction/scripts/signal_to_markdown.py` | 1 |
| Detector | `signal_card_defect_check.py` (raíz del repo) | 1 |

`time_scope_raw` se declara en
`phases/01-source-intake/data-extraction/schemas/data_extraction_record.schema.json:285-288`:
tipo `["string", "null"]` (línea 286), descripción "Original temporal wording if present"
(línea 287). Aparece en la lista `required` en la línea 28.

## Bloque 1 — Distribución de forma sobre los 1,178 records

### Reglas mecánicas del clasificador

- Se cuenta como expresión temporal: fechas en cualquier formato (ISO, dd/mm/aaaa,
  dd.mm.aaaa, mes+día+año, día+mes+año, mes+año, mes solo, día de semana, años 19xx/20xx
  con o sin `~ © @`, rangos de años, trimestres `Q1-Q4`, estaciones/términos académicos);
  duraciones y frecuencias (número+unidad, unidades sin cuantificar como `weeks`/`años`,
  `daily/monthly/yearly/mensual/anual`, `per/each/every + unidad`, `calendar year`,
  `full year`, `year and a half`/`año y medio`, `multi-year`); deícticos (`currently`,
  `recently`, `earlier`, `now`, `last/next/this/previous/prior + unidad o mes`); y
  sustantivos/adjetivos temporales sin unidad (`period/período`, `tiempo/time`, `momento`,
  `lifetime`, `perpetual`, `permanently`, `evergreen`).
- Expresiones adyacentes separadas solo por espacios, paréntesis, `, ~ . – -` o palabras
  de rango (`to`, `through`, `a`, `al`, `hasta`, `until`, `y`, `and`, `de`) se fusionan en
  una sola expresión (rangos y apósitos: `January 2024 to August 2025`, `this year (2025)`,
  `full year 2024`, `mensual (monthly)` cuentan como una). Separadores `;` y `:` no fusionan.
- Marcadores de rol y conectores que NO cuentan como material: `as of, since, from, by,
  before, after, until, within, over, about, around, approximately, circa, starting,
  effective, more/less than, ago, later, back, end, beginning, early, late, per, each,
  every`, y equivalentes en español (`desde, hasta, hace, al, vigente, efectivo, pasado,
  después, antes, durante, casi`), artículos y preposiciones.
- Cualquier otro token restante (palabras de prosa, metadata como `accessed/updated/
  published/posted/reviewed/undated/date`, sustantivos de evento como `purchase/review/
  refund/launch`, cifras no temporales) cuenta como material no temporal.
- VACÍO = `null`, clave ausente o `""`. Con ≥1 expresión y material → MEZCLADO; 1
  expresión sin material → ANCLA-ÚNICA; ≥2 sin material → MÚLTIPLES-ANCLAS; contenido
  sin expresión → SIN-ANCLA.

### Tabla de distribución (n=1,178)

| Categoría | Conteo | % |
|---|---|---|
| VACÍO | 358 | 30.4% |
| ANCLA-ÚNICA | 290 | 24.6% |
| MÚLTIPLES-ANCLAS | 16 | 1.4% |
| MEZCLADO | 469 | 39.8% |
| SIN-ANCLA | 45 | 3.8% |
| NO-CLASIFICABLE | 0 | 0.0% |
| **Total** | **1178** | 100% |

### 5 ejemplos por categoría (valor literal | extraction_id)

**VACÍO** (358):
- `null` | `ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-001-SNP-001`
- `null` | `ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-003-SNP-001`
- `null` | `ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-004-SNP-001`
- `null` | `ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-005-SNP-001`
- `null` | `ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-010-SNP-001`

**ANCLA-ÚNICA** (290):
- "as of February 2026" | `ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-002-SNP-001`
- "as of January 2025" | `ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-006-SNP-001`
- "Starting Jan 1, 2023" | `ER-SP-compass_artifact_wf-0ffe7308-62e3-4530-ae68-93720df60f34_text_markdown-001-SNP-001`
- "March 2026" | `ER-SP-compass_artifact_wf-0ffe7308-62e3-4530-ae68-93720df60f34_text_markdown-002-SNP-001`
- "As of August 29, 2025" | `ER-SP-compass_artifact_wf-0ffe7308-62e3-4530-ae68-93720df60f34_text_markdown-004-SNP-001`

**MÚLTIPLES-ANCLAS** (16):
- "2019; 3-4 years later; by June 2025" | `ER-SP-compass_artifact_wf-22c5fbd5-9e04-4d5a-9b0e-4cb97acec9cc_text_markdown_normalized-011-SNP-001`
- "around 2019; for a year and a half" | `ER-SP-compass_artifact_wf-22c5fbd5-9e04-4d5a-9b0e-4cb97acec9cc_text_markdown_normalized-011-SNP-006`
- "2016; in 2020" | `ER-SP-compass_artifact_wf-22c5fbd5-9e04-4d5a-9b0e-4cb97acec9cc_text_markdown_normalized-011-SNP-011`
- "Summer term; Spring term; For weeks now" | `ER-SP-compass_artifact_wf-22c5fbd5-9e04-4d5a-9b0e-4cb97acec9cc_text_markdown_normalized-014-SNP-001`
- "Two years ago; Two weeks ago; A few days ago" | `ER-SP-compass_artifact_wf-22c5fbd5-9e04-4d5a-9b0e-4cb97acec9cc_text_markdown_normalized-015-SNP-001`

**MEZCLADO** (469):
- "Currently (article last updated Feb. 25, 2026)" | `ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-002-SNP-002`
- "as of January 2025 (from article context)" | `ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-006-SNP-002`
- "Accessed April 14, 2026; Updated daily" | `ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-007-SNP-001`
- "Accessed April 14, 2026" | `ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-007-SNP-003`
- "Accessed April 2026; Updated daily" | `ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-009-SNP-001`

**SIN-ANCLA** (45):
- "After the acquisition" | `ER-SP-compass_artifact_wf-22c5fbd5-9e04-4d5a-9b0e-4cb97acec9cc_text_markdown_normalized-011-SNP-009`
- "next recurring purchase following the date of such changes" | `ER-SP-compass_artifact_wf-4ef0d94a-344f-48de-a6a0-29bd09258ed5_text_markdown_normalized-015-SNP-008`
- "No visible date" | `ER-SP-compass_artifact_wf-c82ebd53-b62c-4f66-b8e2-ae9f5673d0ac_text_markdown_normalized-001-SNP-001`
- "Undated (from search results)" | `ER-SP-compass_artifact_wf-e33b0dbb-828e-4221-b8c5-7bf05bddcdba_text_markdown_normalized-006-SNP-001`
- "Undated" | `ER-SP-compass_artifact_wf-e33b0dbb-828e-4221-b8c5-7bf05bddcdba_text_markdown_normalized-007-SNP-001`

**NO-CLASIFICABLE** (0):
- (sin casos; ver nota sobre casos límite más abajo)

Casos límite resueltos por decisión de léxico (documentada arriba), no forzados en
silencio: `"perpetual, irrevocable"` → MEZCLADO (`perpetual` cuenta como expresión de
duración; `irrevocable` es material); `"free trial period"` y `"at the commencement of
your participation period"` → MEZCLADO (`period` cuenta como sustantivo temporal;
`free trial`/`commencement/participation` son material); `"durante cierto período de
tiempo (for a certain period of time)"` → MEZCLADO; `"Fecha no visible; página activa
al momento de consulta"` → MEZCLADO (`momento` cuenta como sustantivo temporal), mientras
`"Fecha no visible; página promocional activa"` → SIN-ANCLA. Bajo un léxico que excluya
los sustantivos temporales sin unidad, esos casos caerían en SIN-ANCLA o NO-CLASIFICABLE;
con el léxico declarado, NO-CLASIFICABLE queda en 0.

### Longitud en caracteres (sobre los 820 valores no vacíos)

mínimo = 4; máximo = 109; mediana = 30.0

Los 10 valores más largos:

| Chars | extraction_id | Valor literal |
|---|---|---|
| 109 | `ER-SP-compass_artifact_wf-a9f3dcd5-c78e-4ae8-b4d1-09fed2f8d84d_text_markdown-005-SNP-008` | "Cancellation February 2025; charges continued 5 months; experience December 2, 2025; review December 11, 2025" |
| 108 | `ER-SP-compass_artifact_wf-a69c4eb8-8715-4dec-b187-135b1b0fa31a_text_markdown-010-SNP-001` | "Accessed April 2026; page undated; references November 2025 billing deadline (April–November 2025 estimated)" |
| 103 | `ER-SP-compass_artifact_wf-4ef0d94a-344f-48de-a6a0-29bd09258ed5_text_markdown_normalized-015-SNP-006` | "12 months from commencement of subscription period; or Plus subscription expiration (whichever earlier)" |
| 101 | `ER-SP-compass_artifact_wf-f65accb1-75e2-4cb1-be7d-0d01a8fabf93_text_markdown-011-SNP-001` | "Approximately November 29, 2024 (estimated from tweet ID; exact date not displayed in search snippet)" |
| 93 | `ER-SP-compass_artifact_wf-22c5fbd5-9e04-4d5a-9b0e-4cb97acec9cc_text_markdown_normalized-011-SNP-007` | "August 2025; stopped paying since July; paid until June 2025; stopped replying four years ago" |
| 89 | `ER-SP-compass_artifact_wf-22c5fbd5-9e04-4d5a-9b0e-4cb97acec9cc_text_markdown_normalized-018-SNP-001` | "as of the beginning of 2022; Usually, within a month from the production phase being over" |
| 88 | `ER-SP-compass_artifact_wf-83a235d5-86a0-4c10-9097-e29688c3b834_text_markdown_normalized-016-SNP-007` | "prior 365 days (rolling window for $10,000 USD threshold, calculated first day of month)" |
| 86 | `ER-SP-compass_artifact_wf-f678b42a-32e6-4c77-b539-89b40c493fbb_text_markdown-009-SNP-004` | "Efectivo desde 1 de enero de 2024 (algunos países) / 1 de abril de 2025 (demás países)" |
| 86 | `ER-SP-compass_artifact_wf-f678b42a-32e6-4c77-b539-89b40c493fbb_text_markdown-009-SNP-003` | "Efectivo desde 1 de enero de 2024 (algunos países) / 1 de abril de 2025 (demás países)" |
| 86 | `ER-SP-compass_artifact_wf-f678b42a-32e6-4c77-b539-89b40c493fbb_text_markdown-009-SNP-002` | "Efectivo desde 1 de enero de 2024 (algunos países) / 1 de abril de 2025 (demás países)" |

## Bloque 2 — El mecanismo de la pérdida (los 11 PERDIDO de batch_001)

Referencia previa: `state/output/phase1_to_card_field_fate.md` — sobre 29 pares
card→skeleton, `time_scope_raw`: 11 ORIGEN-VACÍO, 4 LIMPIO, 3 NORMALIZADO, 11 PERDIDO
(18 con valor en origen, 11 llegan vacíos).

### La regla que gobierna el campo

`phases/02-signal-extraction/modules/signal_converter.md:171`, cita literal:

> 9. **`time_scope_raw`** — Inherit from `_extraction_context.time_scope_raw`. Preserve
> original temporal wording. Null if absent. `time_scope_raw` is verbatim from the
> snippet — do not append record metadata or access dates to it; those go in
> `normalization_notes`.

La regla contiene dos instrucciones en el mismo enunciado: heredar el valor del contexto,
y la restricción de que el campo es verbatim del snippet (la metadata del record y las
fechas de acceso no van en él sino en `normalization_notes`).

### Qué hace el código con el campo

Ningún script escribe `time_scope_raw` en la card; no existe rama de código que lo
descarte. Lo que el código hace:

- `phases/02-signal-extraction/scripts/signal_prepare.py:73` declara
  `EXTRACTION_CONTEXT_FIELDS = (` con `"time_scope_raw"` en la línea 93; el loop de la
  línea 201 (`for field in EXTRACTION_CONTEXT_FIELDS`) copia el valor del Extraction
  Record al `_extraction_context` del skeleton (asignado en la línea 233). La línea 221
  deja el campo top-level del skeleton en null: `"time_scope_raw": None,` bajo el
  comentario de la línea 212, `# Campos de juicio — vacíos; stage 2 los llena`. El
  llenado es del stage 2 (conversión por agente bajo el módulo), no de un script.
- `phases/02-signal-extraction/scripts/signal_to_markdown.py:150-164` (`extract_date`)
  solo lee: `Prioridad: time_scope_normalized_if_safe → time_scope_raw → ""` (línea 155);
  líneas 161-163: `raw = card.get("time_scope_raw")` / `if raw:` / `return str(raw)`.
- `signal_card_defect_check.py:262` y `:276` lo leen para los checks 2 y 4 (ver Bloque 3).

El descarte, cuando ocurre, ocurre en la conversión stage 2 gobernada por la regla del
módulo, y las cards lo registran en `normalization_notes`.

### Card por card: ¿el descarte es consistente con la regla?

Verificación mecánica por caso: ¿el valor de origen aparece verbatim (normalizando solo
espacios, sin distinguir mayúsculas) en el snippet del record
(`snippet_context_before + snippet_primary + snippet_context_after`)?

| Card | Valor de origen (skeleton, ruta:línea) | ¿Verbatim en snippet? | Nota de la card |
|---|---|---|---|
| SC-R1-008 | "as of January 2025 (from article context)" (`working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-008.json:62`) | no | "time_scope_raw set to null: 'as of January 2025' does not appear verbatim in this snippet; it was inferred from the source article's title and a sibling snippet, which is not permitted for time_scope_raw (verbatim-only). The inference is preserved here as context rather than in time_scope_raw." (`working/signal_extraction/cards/SC-R1-008.json:42`) |
| SC-R1-009 | "Accessed April 14, 2026; Updated daily" (`working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-009.json:62`) | no | "time_scope_raw set to null: neither 'Accessed April 14, 2026' nor 'Updated daily' appear verbatim in this snippet (the snippet is only the layout-stated figure); both are extraction-record metadata about the page, not snippet text." (`working/signal_extraction/cards/SC-R1-009.json:42`) |
| SC-R1-010 | "Accessed April 14, 2026; Updated daily" (`working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-010.json:62`) | no | "time_scope_raw set to null: neither the access date nor 'Updated daily' appear verbatim in this snippet." (`working/signal_extraction/cards/SC-R1-010.json:44`) |
| SC-R1-011 | "Accessed April 14, 2026" (`working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-011.json:62`) | no | "time_scope_raw set to null: the access date does not appear verbatim in this snippet (a navigation category list)." (`working/signal_extraction/cards/SC-R1-011.json:42`) |
| SC-R1-012 | "Accessed April 14, 2026; Updated daily" (`working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-012.json:62`) | no | "time_scope_raw set to null: the access date does not appear verbatim in this snippet (a layout-derived ranking statistic)." (`working/signal_extraction/cards/SC-R1-012.json:43`) |
| SC-R1-013 | "Accessed April 14, 2026; Updated daily" (`working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-013.json:62`) | no | "time_scope_raw set to null: the access date does not appear verbatim in this snippet." (`working/signal_extraction/cards/SC-R1-013.json:46`) |
| SC-R1-014 | "Accessed April 2026; Updated daily" (`working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-014.json:62`) | no | "time_scope_raw set to null: not verbatim in snippet." (`working/signal_extraction/cards/SC-R1-014.json:42`) |
| SC-R1-017 | "Accessed April 2026" (`working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-017.json:62`) | no | "time_scope_raw set to null: the access date does not appear verbatim in this snippet (a category filter list)." (`working/signal_extraction/cards/SC-R1-017.json:41`) |
| SC-R1-020 | "March 2026" (`working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-020.json:63`) | no | "time_scope_raw set to null: 'March 2026' is the changelog entry's own date (record metadata) and does not appear as literal text within snippet_primary itself. This is a borderline case worth flagging: unlike an incidental page-access timestamp, a changelog's own dateline arguably describes when the reported event occurred, not just when the page was viewed — but it is still not verbatim-present in the snippet text, so per the verbatim-only rule for time_scope_raw it is not preserved here. Flagged for operator judgment." (`working/signal_extraction/cards/SC-R1-020.json:55`) |
| SC-R1-1181 | "Accessed April 2026; Updated daily" (`working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-014.json:62`) | no | "time_scope_raw set to null: not verbatim in snippet." (`working/signal_extraction/cards/SC-R1-1181.json:44`) |
| SC-R1-1182 | "Accessed April 2026; Updated daily" (`working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-014.json:62`) | no | "time_scope_raw set to null: not verbatim in snippet." (`working/signal_extraction/cards/SC-R1-1182.json:44`) |

Resultado: en los 11 casos el valor de origen NO aparece verbatim en el snippet — los 11
valores son metadata de acceso o datación del record (`Accessed …`, `Updated daily`,
dateline de changelog, inferencia desde el título del artículo), no redacción temporal
del snippet. La cláusula verbatim de la regla predice exactamente este descarte, y la
regla ordena registrar esa metadata en `normalization_notes`: las 11 cards contienen una
nota `time_scope_raw set to null: …` que lo hace. El descarte es consistente con la regla
en 11 de 11 casos; no se encontró ningún caso donde un valor verbatim del snippet se haya
descartado.

Caso anotado: en SC-R1-020 la propia card marca el descarte como límite — la nota dice
que `'March 2026'` es el dateline de la entrada de changelog (metadata del record) pero
señala que un dateline de changelog "arguably describes when the change happened". El
descarte sigue la cláusula verbatim; la card lo declara borderline. Se reporta, no se
resuelve aquí.

## Bloque 3 — Cruce contra el detector

### Salida literal de `python3 signal_card_defect_check.py` (sin flags)

```
==============================================================================
SIGNAL CARD DEFECT CHECK
==============================================================================
Cards dir:   working/signal_extraction/cards
Records dir: working/data_extraction/records

------------------------------------------------------------------------------
PER-CARD FLAGS
------------------------------------------------------------------------------

[SC-R1-010]
  defect: time_scope_loss
  evidence: des hidden earnings Estimated Monthly Payouts"]
  measured: time_scope_raw=null, matched temporal pattern: 'Monthly'

[SC-R1-016]
  defect: time_scope_loss
  evidence: [Stated in layout: "Monthly Investment: $1,600/month (ful
  measured: time_scope_raw=null, matched temporal pattern: 'Monthly'

------------------------------------------------------------------------------
SUMMARY — counts by defect type
------------------------------------------------------------------------------
  Cards processed: 29
  Cards with >=1 flag: 2
  qualifier_overfill: 0
  time_scope_contamination: 0
  partial_discreteness: 0
  time_scope_loss: 2

------------------------------------------------------------------------------
QUALIFIER LENGTH / SENTENCE-COUNT DISTRIBUTION (this run)
------------------------------------------------------------------------------
  char length: n=53 min=9 max=90 mean=30.8 median=24
  sentence count: n=53 min=1 max=1 mean=1.0 median=1

  Threshold sensitivity (QUALIFIER_MAX_CHARS=90, +/-50%):
        -50% (>45 chars): 10/53 qualifiers flagged
     current (>90 chars): 0/53 qualifiers flagged
        +50% (>135 chars): 0/53 qualifiers flagged

  Threshold sensitivity (QUALIFIER_MAX_SENTENCES=1, +/-50%, rounded):
        -50% (>1 sentences): 0/53 qualifiers flagged
     current (>1 sentences): 0/53 qualifiers flagged
        +50% (>2 sentences): 0/53 qualifiers flagged
```

### Qué detecta y qué no

El detector reporta 2 `time_scope_loss`: **SC-R1-010** y **SC-R1-016**.

Cruce contra los 11 PERDIDO de la traza previa:

- De los 11 PERDIDO, el detector detecta **1**: SC-R1-010 (su snippet contiene
  "Estimated Monthly Payouts"; el token `Monthly` matchea el patrón de frecuencia).
- Los otros **10** PERDIDO no son detectados: SC-R1-008, SC-R1-009, SC-R1-011, SC-R1-012,
  SC-R1-013, SC-R1-014, SC-R1-017, SC-R1-020, SC-R1-1181, SC-R1-1182.
- El segundo flag del detector, SC-R1-016, **no pertenece a los 11 PERDIDO**: su origen
  (`_extraction_context.time_scope_raw`) es null — en la traza previa es ORIGEN-VACÍO,
  no PERDIDO. Su snippet contiene "Monthly Investment: $1,600/month" y por eso matchea.

El encargo planteaba "qué 2 casos detecta y qué 9 no" sobre los 11; la cifra medida es:
1 de los 11 detectado, 10 no detectados, y 1 flag del detector fuera del conjunto de 11.
No se ajustó ninguna de las dos mediciones.

### La condición del detector y por qué los 10 no la satisfacen

`signal_card_defect_check.py:275-285`, cita literal:

```python
def check_time_scope_loss(card, snippet_text):
    if card.get("time_scope_raw"):
        return []
    match = TEMPORAL_RE.search(snippet_text) or MONTH_RE.search(snippet_text)
    if not match:
        return []
    return [{
        "defect": "time_scope_loss",
        "evidence": snippet_text[max(0, match.start() - 30):match.end() + 30],
        "measured": f"time_scope_raw=null, matched temporal pattern: '{match.group(0)}'",
    }]
```

`snippet_text` se construye en `signal_card_defect_check.py:217-223`
(`snippet_text_for_record`) solo con `snippet_context_before`, `snippet_primary` y
`snippet_context_after` del record. Los patrones son `signal_card_defect_check.py:139-150`:

```python
MONTH_RE = re.compile(
    r"\b(January|February|March|April|May|June|July|August|September|October|November|December)\b"
)
TEMPORAL_PATTERNS = [
    r"\b(19|20)\d{2}\b",
    r"\bas of\b",
    r"\bcurrent as of\b",
    r"\blast updated\b",
    r"\bsince\s+\w+\s+\d{4}\b",
    r"\b(daily|weekly|monthly|quarterly|annually)\b",
]
TEMPORAL_RE = re.compile("|".join(TEMPORAL_PATTERNS), re.IGNORECASE)
```

La condición del detector mide **snippet → card**: dispara solo si la card tiene
`time_scope_raw` vacío Y el texto del snippet contiene alguno de esos patrones. La traza
previa mide **campo del ER (vía skeleton) → campo de la card**. Son dos definiciones de
pérdida distintas. Los 10 PERDIDO no detectados no satisfacen la condición porque sus
snippets no contienen ningún match de `TEMPORAL_RE` ni `MONTH_RE` (verificado ejecutando
ambos regex sobre `snippet_text_for_record` de cada record): en esos 10 records la
redacción temporal vive en campos de metadata del record (`time_scope_raw` del ER,
`source_date_if_available`), que el detector no consulta — exactamente el mismo motivo
por el que la regla verbatim del módulo excluyó esos valores de la card. La columna
"detector matchea snippet" por caso:

| Card | Match de TEMPORAL_RE/MONTH_RE en su snippet |
|---|---|
| SC-R1-008 | (ninguno) |
| SC-R1-009 | (ninguno) |
| SC-R1-010 | `Monthly` |
| SC-R1-011 | (ninguno) |
| SC-R1-012 | (ninguno) |
| SC-R1-013 | (ninguno) |
| SC-R1-014 | (ninguno) |
| SC-R1-017 | (ninguno) |
| SC-R1-020 | (ninguno) |
| SC-R1-1181 | (ninguno) |
| SC-R1-1182 | (ninguno) |

La discrepancia 2 vs 11 queda así: 11 pérdidas ER→card (todas consistentes con la regla
verbatim del módulo); 2 flags del detector bajo su definición snippet→card; intersección
= 1 (SC-R1-010). La discrepancia es el hallazgo; no se ajustó ni el detector ni la traza.

