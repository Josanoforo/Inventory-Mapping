# Verificación verbatim de los MÚLTIPLES-ANCLAS de `time_scope_raw` — parada en Bloque 0

Medición solo lectura, fecha 2026-07-30. Ningún record, skeleton, card, schema,
script o el ledger fue modificado. No se re-corrió Phase 1 ni Phase 2.

## Bloque 0 — el universo, y por qué esta medición se detiene aquí

La tarea pide reconfirmar los 16 `extraction_id` MÚLTIPLES-ANCLAS citados en
`state/pendientes_ledger.md` (P-119, P-126, P-132) y en
`state/output/time_scope_raw_distribution.md` (rama
`claude/corpus-measurement-field-mapping-y4rrnl`, no mergeada a `main`), y
verificar que son "los mismos". Esa cifra de 16 no está listada en ningún
archivo del repo como una lista de 16 IDs — el archivo fuente documenta el
léxico mecánico usado y **5 ejemplos** de la categoría, no los 16:

> `time_scope_raw_distribution.md`, Bloque 1, categoría MÚLTIPLES-ANCLAS (16):
> - "2019; 3-4 years later; by June 2025"
> - "around 2019; for a year and a half"
> - "2016; in 2020"
> - "Summer term; Spring term; For weeks now"
> - "Two years ago; Two weeks ago; A few days ago"

Para "confirmar que son los mismos" hacía falta reconstruir los 16 aplicando
el léxico documentado (citado abajo, verbatim) sobre los 1,178 Extraction
Records de `working/data_extraction/records/*.json`. Se implementó ese
léxico como clasificador (script de trabajo, no commiteado — vive fuera del
repo, en el scratchpad de la sesión, para no tocar `state/scripts/`) y se
corrió sobre el corpus completo.

### Resultado: el conteo no da 16

Aplicando el léxico citado —tal como está escrito, sin ajustarlo a
posteriori para forzar 16— sobre los 1,178 records:

| Categoría | Documentado (rama `claude/corpus-measurement-field-mapping-y4rrnl`) | Reconstruido en esta sesión |
|---|---|---|
| VACÍO | 358 | 358 |
| ANCLA-ÚNICA | 290 | 275 |
| MÚLTIPLES-ANCLAS | 16 | **9** |
| MEZCLADO | 469 | 489 |
| SIN-ANCLA | 45 | 47 |
| **Total** | **1,178** | **1,178** |

VACÍO coincide exactamente (358/358) porque es la única categoría de límite
puramente mecánico (`null`/ausente/`""`). Las otras cuatro categorías
dependen de juicio sobre prosa natural, y no coinciden.

De los 9 reconstruidos, los 5 que sí aparecen como ejemplo en
`time_scope_raw_distribution.md` coinciden exactamente en valor literal y
`extraction_id` con los reconstruidos aquí (verificado uno a uno). Los 9
`extraction_id` y su valor literal de `time_scope_raw`:

1. `ER-SP-compass_artifact_wf-22c5fbd5-9e04-4d5a-9b0e-4cb97acec9cc_text_markdown_normalized-011-SNP-001` — "2019; 3-4 years later; by June 2025"
2. `ER-SP-compass_artifact_wf-22c5fbd5-9e04-4d5a-9b0e-4cb97acec9cc_text_markdown_normalized-011-SNP-006` — "around 2019; for a year and a half"
3. `ER-SP-compass_artifact_wf-22c5fbd5-9e04-4d5a-9b0e-4cb97acec9cc_text_markdown_normalized-011-SNP-011` — "2016; in 2020"
4. `ER-SP-compass_artifact_wf-22c5fbd5-9e04-4d5a-9b0e-4cb97acec9cc_text_markdown_normalized-014-SNP-001` — "Summer term; Spring term; For weeks now"
5. `ER-SP-compass_artifact_wf-22c5fbd5-9e04-4d5a-9b0e-4cb97acec9cc_text_markdown_normalized-015-SNP-001` — "Two years ago; Two weeks ago; A few days ago"
6. `ER-SP-compass_artifact_wf-22c5fbd5-9e04-4d5a-9b0e-4cb97acec9cc_text_markdown_normalized-020-SNP-001` — "7+ years; last term"
7. `ER-SP-compass_artifact_wf-28f59dc7-8351-48a1-bcaa-ff9992b8fe70_text_markdown-005-SNP-001` — "last 3 years; last 12 months"
8. `ER-SP-compass_artifact_wf-28f59dc7-8351-48a1-bcaa-ff9992b8fe70_text_markdown-015-SNP-001` — "January 2025; January 2026; 13 months"
9. `ER-SP-compass_artifact_wf-a69c4eb8-8715-4dec-b187-135b1b0fa31a_text_markdown-008-SNP-002` — "April 2025; over the last year"

Todos los 9 fueron confirmados existentes en
`working/data_extraction/records/*.json` (lectura directa, sin modificar).
Ninguno de los 9 tiene Signal Card (`working/signal_extraction/cards/*.json`
no contiene ningún `extraction_id` de la lista — grep directo, 0 matches);
ninguno pertenece a `batch_001` (el único batch corrido), confirmando el
patrón que P-119 ya señala para la mayoría del universo MÚLTIPLES-ANCLAS.

### El léxico citado, verbatim (fuente: `time_scope_raw_distribution.md`, rama `claude/corpus-measurement-field-mapping-y4rrnl`)

> Se cuenta como expresión temporal: fechas en cualquier formato (ISO,
> dd/mm/aaaa, dd.mm.aaaa, mes+día+año, día+mes+año, mes+año, mes solo, día de
> semana, años 19xx/20xx con o sin `~ © @`, rangos de años, trimestres
> `Q1-Q4`, estaciones/términos académicos); duraciones y frecuencias
> (número+unidad, unidades sin cuantificar como `weeks`/`años`,
> `daily/monthly/yearly/mensual/anual`, `per/each/every + unidad`,
> `calendar year`, `full year`, `year and a half`/`año y medio`,
> `multi-year`); deícticos (`currently`, `recently`, `earlier`, `now`,
> `last/next/this/previous/prior + unidad o mes`); y sustantivos/adjetivos
> temporales sin unidad (`period/período`, `tiempo/time`, `momento`,
> `lifetime`, `perpetual`, `permanently`, `evergreen`).
>
> Expresiones adyacentes separadas solo por espacios, paréntesis, `, ~ . – -`
> o palabras de rango (`to, through, a, al, hasta, until, y, and, de`) se
> fusionan en una sola expresión [...]. Separadores `;` y `:` no fusionan.
>
> Marcadores de rol y conectores que NO cuentan como material: `as of, since,
> from, by, before, after, until, within, over, about, around, approximately,
> circa, starting, effective, more/less than, ago, later, back, end,
> beginning, early, late, per, each, every`, y equivalentes en español
> (`desde, hasta, hace, al, vigente, efectivo, pasado, después, antes,
> durante, casi`), artículos y preposiciones.
>
> Cualquier otro token restante (palabras de prosa, metadata como
> `accessed/updated/published/posted/reviewed/undated/date`, sustantivos de
> evento como `purchase/review/refund/launch`, cifras no temporales) cuenta
> como material no temporal.
>
> VACÍO = `null`, clave ausente o `""`. Con ≥1 expresión y material →
> MEZCLADO; 1 expresión sin material → ANCLA-ÚNICA; ≥2 sin material →
> MÚLTIPLES-ANCLAS; contenido sin expresión → SIN-ANCLA.

Este léxico es prosa descriptiva con listas de ejemplos ("como", "tales
como"), no una gramática cerrada y enumerable — no fija, por ejemplo, si
`annual` (inglés) cuenta igual que `anual` (español, sí listado), si `half`
cuenta igual que `año y medio` (frase completa, sí listado), si `7+` cuenta
como número+unidad igual que `more than 7`, o qué hacer con adjetivos
intensificadores sobre un deíctico ya listado (`most recently` vs.
`recently`). Cada una de esas cuatro decisiones, tomadas en un sentido u
otro, cambia qué records caen en MÚLTIPLES-ANCLAS vs. MEZCLADO vs.
ANCLA-ÚNICA. La reconstrucción de esta sesión resolvió esas ambigüedades de
la manera más permisiva razonable (incluyendo `annual`, `half`, `7+`) y aun
así llegó a 9, no a 16.

## Bloques 1–3 — no ejecutados

Por instrucción explícita de la tarea ("Si el conteo no da 16, DETENTE y
repórtalo"), esta medición se detiene en el Bloque 0. Ejecutar los Bloques
1–3 (clasificación verbatim, cruce con Phase 2, población de
`time_scope_normalized_if_safe`) sobre un universo de 16 no confirmado
produciría cifras que aparentan solidez sin tenerla — el problema no es
recontar mal 3 casos, es que 7 de los 16 originales no son identificables a
partir del léxico tal como está escrito. Decidir cuáles son esos 7 requiere
releer los 1,178 `time_scope_raw` (o consultar directamente el registro de
la sesión que produjo la cifra de 16) — trabajo que excede lectura mecánica
del léxico documentado y que esta tarea no autoriza a resolver por
interpretación propia.

## No resuelto aquí (anotado, no tocado)

- La cifra de 16 en `state/pendientes_ledger.md` (P-119, P-126, P-132) y en
  `time_scope_raw_distribution.md` no tiene, en ningún archivo del repo, un
  listado de los 16 `extraction_id` que la componen — solo el conteo y 5
  ejemplos. Sin ese listado, o sin el registro de sesión original, "son los
  mismos" no es verificable con certeza; solo es verificable que 9 de ellos
  son inequívocamente correctos bajo el léxico citado.
- No se decide aquí si el léxico debería precisarse (agregar `annual`,
  `half`, `7+`, intensificadores de deícticos como reglas explícitas) — eso
  es un cambio a un archivo de medición previo en otra rama, fuera del
  alcance de "solo lectura" de esta tarea.
