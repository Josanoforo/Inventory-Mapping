# P-150 — bulk_extract.py vs. pipeline_vocabulary.yaml:30-39 (@ `main@a1a4084a`), comparación literal

Lectura previa a cualquier conclusión, por instrucción de la corrida.

## Nota de sellado [2026-07-30] — anclaje de citas a SHA

Toda cita de línea a `bulk_extract.py` y a `pipeline_vocabulary.yaml` en este archivo queda
anclada además al commit `main@a1a4084a` (verificado: contenido y numeración de línea en ese SHA
coinciden exactamente con lo transcrito abajo). Razón: P-142 y P-143, abiertos en el ledger, van a
editar `bulk_extract.py`, y las líneas citadas aquí se van a correr cuando eso pase — el número de
línea solo, sin SHA, dejaría de apuntar al código que este archivo describe. Nada existente se
borra ni se reescribe; esto es una adición.

## `bulk_extract.py` — `infer_actor_level` (líneas 157-181 @ `main@a1a4084a`)

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

(`phases/01-source-intake/data-extraction/scripts/bulk_extract.py:157-181` @ `main@a1a4084a`)

## `pipeline_vocabulary.yaml:30-39` (@ `main@a1a4084a`) — `assignment_rule` de `actor`

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

(`pipeline_vocabulary.yaml:30-39` @ `main@a1a4084a`)

## Comparación

| `source_type` | `bulk_extract.py` (código) | `pipeline_vocabulary.yaml` (assignment_rule) | ¿Coincide? |
|---|---|---|---|
| `help_center` | `marketplace` (línea 168 @ `main@a1a4084a`) | `platform` (línea 32 @ `main@a1a4084a`) | **no** |
| `policy_page` | `marketplace` (línea 168 @ `main@a1a4084a`) | `platform` (línea 32 @ `main@a1a4084a`) | **no** |
| `platform_doc` | `marketplace` (línea 168 @ `main@a1a4084a`) | `platform` (línea 32 @ `main@a1a4084a`) | **no** |
| `pricing_page` | `marketplace` (línea 178 @ `main@a1a4084a`) | `platform` (línea 32 @ `main@a1a4084a`) | **no** |
| `search_results_page` / `category_page` | sin rama explícita en `infer_actor_level`, cae a `unknown` (no hay `if source_type == 'search_results_page'` en esta función) | `marketplace` (línea 35 @ `main@a1a4084a`) | **no** (el código no implementa esta rama en absoluto) |
| `product_listing` | `source` (línea 174 @ `main@a1a4084a`) | `third_party` (condicional, línea 36-37 @ `main@a1a4084a`) | **no** (código fijo, vocab condicional) |

## Predicción — ¿se confirma?

La predicción (P-150) dice literalmente: "una fracción grande del 51% fuera de enum en `actor_level` no sería error de extracción sino `bulk_extract.py` implementando una heurística de keyword (`help_center` → `marketplace`) que el `assignment_rule` del vocabulario ... ya había superado."

Confirmado en el punto específico citado: `bulk_extract.py:167-168` (@ `main@a1a4084a`) mapea `help_center` (junto con `policy_page`, `platform_doc`) a `'marketplace'`; `pipeline_vocabulary.yaml:32` (@ `main@a1a4084a`) dice que esos mismos tres `source_type` (más `pricing_page`) deben ir a `platform`. El código no siguió al vocabulario vigente en este punto — implementa una regla más vieja o distinta.

Precisión sobre el mecanismo: `'marketplace'` es un valor válido del enum `actor` (`pipeline_vocabulary.yaml:24` @ `main@a1a4084a`), así que esta divergencia específica **no produce por sí sola un valor fuera de enum** — produce una clasificación en-enum pero incorrecta según la regla vigente. La relación entre esta divergencia código/vocab y la cifra "51% fuera de enum en `actor_level`" citada en la predicción no queda establecida por esta comparación; requiere el cruce contra los valores poblados en el corpus, que es la condición de verificación declarada en la fila P-150 ("cierre de la re-extracción").

No se modifica la fila P-150 del ledger. Esta rama queda sellada — sin PR, sin merge — hasta que Etapa 2 (re-extracción) cierre, por instrucción de la corrida.

---

## Corrección [2026-07-30T05:34:26Z] — a) HALLAZGO NUEVO: override por keyword, mayor que el desalineamiento medido

El análisis de arriba compara `source_type` contra `assignment_rule` rama por rama, pero eso presupone que `source_type` se consulta. No siempre ocurre.

`bulk_extract.py:157-163` (`infer_actor_level`, @ `main@a1a4084a`):
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
```

`pipeline_vocabulary.yaml:30-31` (@ `main@a1a4084a`):
```yaml
  assignment_rule: |
    Determined by source_type, not by topic. "Who speaks", not "who is affected."
```

Las primeras cuatro líneas ejecutables de la función (159-166) buscan las palabras `buyer|customer|purchaser|patron|subscriber` y `seller|creator|shop owner|vendor|author|instructor|artist` en el texto del `snippet` — es decir, en el tópico — y retornan sobre ese match sin haber consultado `source_type` todavía. Si el `snippet` menciona cualquiera de esas palabras, la rama de `source_type` (línea 167 en adelante) nunca se alcanza, sin importar cuál sea el `source_type` real del record. Esto es exactamente lo que `assignment_rule` dice no hacer: "Determined by source_type, not by topic." La función abre determinando por tópico.

Esto es un mecanismo distinto y anterior al de la comparación `source_type → valor` de más arriba, y de mayor alcance: no está acotado a `help_center`/`policy_page`/`platform_doc`/`pricing_page` — aplica a cualquier `source_type`, incluyendo los que sí coinciden con el vocab en la tabla de comparación (por ejemplo `buyer_review` o `seller_forum`), porque el override por palabra clave ocurre antes de que el código llegue a esas ramas.

## Corrección [2026-07-30T05:34:26Z] — b) REFUTACIÓN de la mitad explicativa de la predicción

La predicción P-150 dice: "una fracción grande del 51% fuera de enum en `actor_level` no sería error de extracción sino `bulk_extract.py` implementando [la heurística]."

`'marketplace'` es un valor legal del enum `actor` (`pipeline_vocabulary.yaml:24` @ `main@a1a4084a`, ya citado arriba). La divergencia `marketplace`/`platform` documentada en este archivo produce una clasificación **en-enum pero incorrecta**, no un valor fuera de enum. Un mecanismo que sustituye un valor válido del enum por otro valor igualmente válido del mismo enum no puede, por construcción, producir una entrada que esté fuera de ese enum.

Esto refuta la mitad explicativa de la predicción ahora, con la lectura de código sola — no queda pendiente del cierre de Etapa 3. Lo que sigue pendiente de Etapa 3 es la otra mitad, distinta: si la re-extracción, al cerrar, muestra que el corpus diverge en los puntos exactos donde el override por keyword (arriba, punto a) predice — es decir, si records cuyo `snippet` contiene esas palabras terminan con `actor_level` distinto al que `assignment_rule` asignaría por `source_type` solo. Eso sí es una pregunta empírica abierta; la explicación del 51% fuera de enum vía `marketplace`/`platform` no lo es — está cerrada, y cerrada en contra de la predicción tal como estaba escrita.
