# P-150 — bulk_extract.py vs. pipeline_vocabulary.yaml:30-39, comparación literal

Lectura previa a cualquier conclusión, por instrucción de la corrida.

## `bulk_extract.py` — `infer_actor_level` (líneas 157-181)

```python
def infer_actor_level(source_type, snippet):
    s = snippet.lower()
    has_buyer = bool(re.search(r'\b(?:buyer|customer|purchaser|patron|subscriber)\b', s))
    has_seller = bool(re.search(r'\b(?:seller|creator|shop\s*owner|vendor|author|instructor|artist)\b', s))
    if has_buyer and has_seller:
        return 'mixed'
    if has_buyer:
        return 'buyer'
    if has_seller:
        return 'seller'
    if source_type in ['help_center', 'policy_page', 'platform_doc']:
        return 'marketplace'
    if source_type == 'database_profile':
        return 'seller'
    if source_type == 'buyer_review':
        return 'buyer'
    if source_type == 'product_listing':
        return 'source'
    if source_type in ['reddit', 'seller_forum', 'blog']:
        return 'seller'
    if source_type == 'pricing_page':
        return 'marketplace'
    if source_type in ['article', 'report', 'news']:
        return 'marketplace'
    return 'unknown'
```

(`phases/01-source-intake/data-extraction/scripts/bulk_extract.py:157-181`)

## `pipeline_vocabulary.yaml:30-39` — `assignment_rule` de `actor`

```yaml
  assignment_rule: |
    Determined by source_type, not by topic. "Who speaks", not "who is affected."
    help_center, pricing_page, platform_doc, policy_page → platform
    blog / seller_forum / reddit (author = seller) → seller
    blog / reddit (author = buyer) → buyer
    search_results_page, category_page → marketplace
    product_listing, or promotional content from an external provider speaking in
    first person about their own product or service → third_party
    commentary or analysis without first-person actor → source
    See: signal_extraction_contract §7 Principle 3
```

(`pipeline_vocabulary.yaml:30-39`)

## Comparación

| `source_type` | `bulk_extract.py` (código) | `pipeline_vocabulary.yaml` (assignment_rule) | ¿Coincide? |
|---|---|---|---|
| `help_center` | `marketplace` (línea 168) | `platform` (línea 32) | **no** |
| `policy_page` | `marketplace` (línea 168) | `platform` (línea 32) | **no** |
| `platform_doc` | `marketplace` (línea 168) | `platform` (línea 32) | **no** |
| `pricing_page` | `marketplace` (línea 178) | `platform` (línea 32) | **no** |
| `search_results_page` / `category_page` | sin rama explícita en `infer_actor_level`, cae a `unknown` (no hay `if source_type == 'search_results_page'` en esta función) | `marketplace` (línea 35) | **no** (el código no implementa esta rama en absoluto) |
| `product_listing` | `source` (línea 174) | `third_party` (condicional, línea 36-37) | **no** (código fijo, vocab condicional) |

## Predicción — ¿se confirma?

La predicción (P-150) dice literalmente: "una fracción grande del 51% fuera de enum en `actor_level` no sería error de extracción sino `bulk_extract.py` implementando una heurística de keyword (`help_center` → `marketplace`) que el `assignment_rule` del vocabulario ... ya había superado."

Confirmado en el punto específico citado: `bulk_extract.py:167-168` mapea `help_center` (junto con `policy_page`, `platform_doc`) a `'marketplace'`; `pipeline_vocabulary.yaml:32` dice que esos mismos tres `source_type` (más `pricing_page`) deben ir a `platform`. El código no siguió al vocabulario vigente en este punto — implementa una regla más vieja o distinta.

Precisión sobre el mecanismo: `'marketplace'` es un valor válido del enum `actor` (`pipeline_vocabulary.yaml:24`), así que esta divergencia específica **no produce por sí sola un valor fuera de enum** — produce una clasificación en-enum pero incorrecta según la regla vigente. La relación entre esta divergencia código/vocab y la cifra "51% fuera de enum en `actor_level`" citada en la predicción no queda establecida por esta comparación; requiere el cruce contra los valores poblados en el corpus, que es la condición de verificación declarada en la fila P-150 ("cierre de la re-extracción").

No se modifica la fila P-150 del ledger. Esta rama queda sellada — sin PR, sin merge — hasta que Etapa 2 (re-extracción) cierre, por instrucción de la corrida.
