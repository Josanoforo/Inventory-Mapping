# Phase 0 Eje 4 Discovery Agent — Guía operativa

## Qué hace este agente

Ejecuta queries del catálogo del eje 4 (canal de descubrimiento) contra surfaces web públicos (principalmente Reddit, con blog/medium/forum como secundarios) y produce findings anclados a fuente. Cada query del catálogo produce un shard markdown independiente que re-entra al pipeline de Phase 0.

A diferencia del recovery agent, este agente no recibe claims pre-existentes para verificar — recibe patterns de búsqueda (queries en lenguaje natural) y busca evidencia primaria que exista de facto en los surfaces accesibles.

El agente no corre el shard automáticamente. Un humano deposita los shards y ejecuta `parse_dg_shard.py` sobre cada uno (o sobre todos en bucle).

---

## Arquitectura del contrato

Este agente usa la arquitectura modular compartida introducida en D-167. El `CONTRACT.md` específico del eje4-discovery hereda los protocolos base desde `agents/codex/_shared/protocols/`:

- `_shared/protocols/core_protocol.md` — principios no negociables, single-source, multi-speaker, edge cases, `source_type`, `verification_status`, herramientas de acceso web, guardrails anti-drift.
- `_shared/protocols/output_contract.md` — estructura obligatoria, campos, QA.
- `_shared/protocols/search_decomposition_rules.md` — descomposición del input.
- `_shared/protocols/output_template.md` — template base con 4 Parts (este agente usa el template base sin extensiones).

**Lo que vive solo en `phase0-eje4-discovery/CONTRACT.md`:**
- Cómo tratar una query del xlsx como input de research.
- Camino A de surfaces (D-166): Reddit primario + blog/medium/forum secundarios.
- **Reddit-specific operating rules** — multi-speaker split de threads, comments anidados con blockquotes, one-continuous-passage trap (Pattern B), handling de posts removidos/eliminados, regional/subreddit scope.
- Paths de input y output.
- Convención de naming del shard (un shard por query).
- QA adicional específico (6 puntos Reddit-specific + anti-drift).

---

## Fuentes del catálogo

**Catálogo canónico:** `catalogos_eje4_canal_descubrimiento.xlsx` en project files del operador. 186 queries en 4 hojas:

| Catálogo | Queries | Foco |
|---|---|---|
| `catalogo_1` | 60 | Fricción declarada |
| `catalogo_2` | 47 | Fricción por migración |
| `catalogo_3a` | 40 | Presión acumulada sin resolución |
| `catalogo_3b` | 39 | Búsqueda de resolución operativa |

**Schema de 12 columnas por query:** `query_id`, `catalogo`, `tema_semilla`, `pattern_id`, `query_text`, `idioma`, `region`, `surface`, `metodo_pago_variable`, `canal_alternativo`, `ventana_temporal`, `notes_operador`.

**Distribución por surface:**

| Surface | Queries | % | Status |
|---|---|---|---|
| `reddit` | 155 | 83.3% | Ejecutable |
| `blog` | 11 | 5.9% | Ejecutable |
| `medium` | 3 | 1.6% | Ejecutable |
| `forum` | 3 | 1.6% | Ejecutable |
| `facebook_search` | 6 | 3.2% | Gap (D-166) |
| `instagram_search` | 4 | 2.2% | Gap (D-166) |
| `discord` | 2 | 1.1% | Gap (D-166) |
| `tiktok_search` | 2 | 1.1% | Gap (D-166) |

**Total ejecutable primer pase: 172 queries (92.5%). Total gap-declarado: 14 queries (7.5%).**

---

## Paso 1 — Pre-procesar el xlsx a JSON individuales por query

### Script

~~~bash
python phases/00-data-gathering/scripts/eje4_xlsx_to_json_batch.py
~~~

*(El script aún no existe en el repo. Su creación es parte del primer run del agente. Ver sección "Script de pre-procesamiento" más abajo para especificación.)*

### Output esperado

~~~
Total queries in xlsx: 186 | ejecutables: 172 | gap-declarado: 14
Done — batch: batch_YYYYMMDD_HHMMSS | queries: 172 | gap: 14 | dir: working/eje4/queries/batch_YYYYMMDD_HHMMSS
~~~

### Estructura del batch

~~~
working/eje4/queries/
└── batch_YYYYMMDD_HHMMSS/
    ├── batch_manifest.json        # metadatos + lista de las 14 gap queries
    ├── query_Q-C1-001.json
    ├── query_Q-C1-002.json
    │   ...
    └── query_Q-C3b-039.json        # 172 archivos de query ejecutables
~~~

### Formato de `query_Q-XXX-NNN.json`

Serialización directa del xlsx row como JSON:

~~~json
{
  "query_id": "Q-C1-001",
  "catalogo": "1",
  "tema_semilla": "Cómo descubren productos digitales los buyers latinos que no usan Etsy ni Creative Market",
  "pattern_id": "C1-P1",
  "query_text": "no encuentro plantillas en español Etsy",
  "idioma": "es",
  "region": "latam_general",
  "surface": "reddit",
  "metodo_pago_variable": null,
  "canal_alternativo": null,
  "ventana_temporal": "last_12_months",
  "notes_operador": null
}
~~~

### Formato de `batch_manifest.json`

~~~json
{
  "batch_id": "batch_YYYYMMDD_HHMMSS",
  "generated_at": "YYYY-MM-DDTHH:MM:SSZ",
  "xlsx_source": "catalogos_eje4_canal_descubrimiento.xlsx",
  "total_queries_in_xlsx": 186,
  "ejecutables": 172,
  "gap_declarado": 14,
  "distribution_by_surface": {
    "reddit": 155,
    "blog": 11,
    "medium": 3,
    "forum": 3,
    "facebook_search": 6,
    "instagram_search": 4,
    "discord": 2,
    "tiktok_search": 2
  },
  "gap_queries": [
    {"query_id": "Q-CX-XXX", "surface": "facebook_search", "reason": "D-166 auth wall"}
  ]
}
~~~

### Verificación

~~~bash
# Debe retornar 172
ls working/eje4/queries/<batch_id>/query_*.json | wc -l

# Debe retornar 172 y 14
python3 -c "import json; m=json.load(open('working/eje4/queries/<batch_id>/batch_manifest.json')); print(m['ejecutables'], m['gap_declarado'])"

# Debe retornar 0 (ninguna gap query entró como archivo ejecutable)
ls working/eje4/queries/<batch_id>/query_*.json | xargs -I{} python3 -c "import json,sys; q=json.load(open(sys.argv[1])); print(q['query_id']) if q['surface'] in ['facebook_search','instagram_search','discord','tiktok_search'] else None" {} | wc -l
~~~

---

## Paso 2 — Validación técnica antes de escalar

**No correr las 172 queries en un solo run.** Esta validación viene directo de Tarea 2 del handoff de sesión 17.

### 2.1 — Smoke test con 3-5 queries diversas

Selecciona 3-5 queries del batch que cubran:
- Al menos 1 query de `catalogo_1` (fricción declarada) y 1 de `catalogo_3a` (presión acumulada) — son los extremos del catálogo.
- Al menos 1 query en español y 1 en inglés.
- Al menos 1 query con `region = mx` y 1 con `region = latam_general`.
- Al menos 1 query en `surface = reddit` y 1 en `surface = blog` si es posible.

### 2.2 — Ejecutar el agente sobre las queries seleccionadas

El agente procesa cada query y produce un shard por query. Ver `CONTRACT.md` para el template del shard.

### 2.3 — Auditar los shards producidos

Para cada shard, verificar:

- **Formato:** ¿Estructura de Parts 1/2/3/4 + Search decomposition + Research QA Notes? ¿Finding IDs siguen la convención?
- **Verbatim snippets:** ¿Son character-for-character, passage continuo, de reddit.com real (URLs verificables)?
- **Multi-speaker split:** Si un thread tiene OP + commenters, ¿quedaron separados en findings distintos?
- **Drift ratio:** ¿Cuántos "claims sintetizados shard-level" hay fuera de Part 3? Idealmente <10%, comparable al output del GPT custom.
- **Guardrails anti-drift:** ¿Part 4 contiene algo? En eje4-discovery Part 4 siempre debe ser `None`. Si contiene pattern naming, thesis statements, categorizaciones cross-finding, o absence findings "compensatorios", el contrato no está funcionando y hay que iterar sobre los protocolos compartidos antes de escalar.

### 2.4 — Decisión de escalar

Si la validación técnica pasa (formato OK + drift ratio bajo + guardrails respetados), escalar a batches más grandes (20 → 50 → 100 → 172).

Si el contrato tiene problemas, iterar sobre los protocolos compartidos (no sobre el CONTRACT específico del agente) para que la corrección beneficie también al recovery agent. Ver nota en handoff sesión 17 Tarea 2.

---

## Paso 3 — Ejecutar el agente en el batch completo (o subconjunto)

El agente recibe el directorio del batch y procesa cada archivo `query_*.json` produciendo un shard markdown por query.

### Output del agente

~~~
working/eje4_discovery/
└── batch_YYYYMMDD_HHMMSS/
    ├── compass_artifact_eje4_Q-C1-001_text_markdown.md
    ├── compass_artifact_eje4_Q-C1-002_text_markdown.md
    │   ...
    └── compass_artifact_eje4_Q-C3b-039_text_markdown.md
~~~

Un shard por query ejecutable. Las queries gap-declarado del `batch_manifest.json` no producen shards.

### Resultado esperado

**172 shards** (uno por query ejecutable) por un run del catálogo completo. Un shard con las 4 Parts marcadas como `None` y Research QA Notes completas es un output válido — significa que la query no rindió evidencia accesible en los surfaces buscados. Cero findings NO es un fracaso del agente, y **no** se registra como absence finding en Part 4 (Part 4 del eje4 siempre es `None` — ver CONTRACT.md sección "Comportamiento si la query no rinde").

---

## Paso 4 — Depositar los shards y ejecutar parse_dg_shard.py

### Directorio de destino

~~~
input/data_gathering/shards/eje4_discovery/
~~~

*(Nuevo directorio. Crear antes del primer run. `parse_dg_shard.py` deriva `source_tool` del nombre del directorio padre, así que los shards depositados en `eje4_discovery/` reciben `source_tool = "eje4_discovery"`.)*

**Pre-flight antes del primer run:** verificar que `parse_dg_shard.py` acepta `eje4_discovery` como valor válido de `source_tool`. Esta verificación ya se hizo en la ejecución de D-167: el `VALID_SOURCE_TOOLS` set en línea 439 del parser fue actualizado para incluir `"eje4_discovery"`. Si en futuras sesiones se crea otro agente Codex, habrá que repetir este pre-flight.

### Ejecutar el parser en bucle sobre todos los shards del batch

~~~bash
for shard in input/data_gathering/shards/eje4_discovery/compass_artifact_eje4_*_text_markdown.md; do
    python phases/00-data-gathering/scripts/parse_dg_shard.py "$shard"
done
~~~

### Output del parser

~~~
working/data_gathering/findings/<shard_id>__<finding_id>.json     ← Part 1 + Part 2
working/data_gathering/diagnostics/qa_notes/<shard_id>_qa.json    ← Research QA Notes
~~~

Donde `shard_id = "compass_artifact_eje4_Q-C1-001_text_markdown"` (uno por query).

**Nota:** los shards del eje4-discovery no generan archivos en `working/data_gathering/diagnostics/part_4/` porque Part 4 siempre es `None` en este agente. Las queries que no rindieron se ven en los `_qa.json` con `Query outcome: query empty`, no en `diagnostics/part_4/`. Esto es distinto del recovery agent, que sí genera items en `diagnostics/part_4/` para sus absence findings con `unrecoverable`.

---

## Flujo completo de re-entrada al pipeline

~~~
1. Script pre-procesa xlsx a JSON por query + manifest
   working/eje4/queries/<batch_id>/query_Q-XXX-NNN.json  (172 archivos)
   working/eje4/queries/<batch_id>/batch_manifest.json   (1 archivo con las 14 gap)

2. Smoke test con 3-5 queries → auditoría → decisión de escalar

3. Agente Codex procesa queries → produce shards markdown
   working/eje4_discovery/<batch_id>/compass_artifact_eje4_Q-XXX-NNN_text_markdown.md

4. Humano deposita shards
   input/data_gathering/shards/eje4_discovery/compass_artifact_eje4_Q-XXX-NNN_text_markdown.md

5. parse_dg_shard.py procesa cada shard (en bucle sobre el directorio)
   ├── direct_verified    → working/data_gathering/findings/  (Part 1)
   ├── indirect_verified  → working/data_gathering/findings/  (Part 2)
   └── Research QA Notes  → working/data_gathering/diagnostics/qa_notes/

   (Part 4 siempre es None en eje4-discovery — no genera items en diagnostics/part_4/.
    Las queries vacías viven en qa_notes con Query outcome: query empty.)

6. Phase 1 (converter_prepare.py) recoge los findings de working/data_gathering/findings/
   junto con todos los demás findings — sin routing especial para eje4-discovery.
~~~

---

## Trazabilidad por query

Una ventaja operativa del modelo shard-por-query: todo lo que downstream necesita saber sobre una query específica vive en un archivo con nombre predecible.

**Mapping directo:**

- Query row en xlsx → `working/eje4/queries/<batch_id>/query_Q-C1-001.json`
- Shard del agente → `working/eje4_discovery/<batch_id>/compass_artifact_eje4_Q-C1-001_text_markdown.md`
- Findings parseados → `working/data_gathering/findings/compass_artifact_eje4_Q-C1-001_text_markdown__F-01.json`, `...__F-02.json`, etc.
- Research QA Notes parseadas → `working/data_gathering/diagnostics/qa_notes/compass_artifact_eje4_Q-C1-001_text_markdown_qa.json`

(Sin items en `diagnostics/part_4/` — Part 4 del eje4 siempre es `None`.)

Esto habilita auditorías por query (¿qué rindió Q-C1-001?), por pattern_id (todas las queries que derivan de C1-P1), por catálogo (catalogo_1 completo), o por surface (todos los findings de reddit).

---

## Señales a medir después del primer batch significativo

Cuando hayas corrido al menos 20-30 queries del catálogo, los siguientes cortes son diagnósticos:

**1. Drift ratio por query y por catálogo.**

Calcular el ratio de claims sintetizados shard-level / findings totales, por query y agregado por catálogo. Si `catalogo_3a` tiene drift sistemáticamente más alto que `catalogo_1`, la hipótesis débil del handoff ("a menos findings, más síntesis compensatoria") se fortalece y hay que intervenir antes de escalar al batch completo.

**2. Query outcome por surface.**

¿Qué porcentaje de queries en `reddit` terminaron con `Query outcome: query empty` vs `blog`/`medium`/`forum`? Si Reddit está produciendo queries vacías sistemáticamente a pesar de las rutas declaradas en el CONTRACT, los guardrails de herramientas web (`core_protocol.md`) no están siendo respetados por el runtime de Codex, o Reddit se endureció y las rutas declaradas ya no funcionan. Esta señal se lee de los archivos `_qa.json` en `diagnostics/qa_notes/`, no de `diagnostics/part_4/` (que no tendrá nada del eje4).

**3. Multi-speaker split rate.**

Para shards de queries con `surface = reddit`, ¿cuántos findings tiene un shard promedio? Si la mayoría de shards tiene 1-2 findings y los threads visitados tenían claramente más comentarios relevantes, el split multi-speaker no está ocurriendo. Eso es violación de regla del contrato.

**4. Pattern B (profile metadata + body text concatenation).**

Auditar manualmente 10 shards al azar buscando Verbatim snippets que hayan concatenado profile metadata con body text. Si aparecen, el contrato está siendo violado en el punto específico que el handoff marcó como trampa aprendida de los shards archivados.

---

## Script de pre-procesamiento — especificación pendiente

El script `eje4_xlsx_to_json_batch.py` no existe en el repo al cierre de D-167. Su creación es parte del primer run del agente. Especificación:

**Input:** `catalogos_eje4_canal_descubrimiento.xlsx` (project files del operador, copiado al working dir del repo).

**Operaciones:**

1. Leer las 4 hojas del xlsx (`catalogo_1`, `catalogo_2`, `catalogo_3a`, `catalogo_3b`).
2. Validar schema de 12 columnas por hoja.
3. Para cada row: generar un dict con las 12 columnas como pares clave-valor.
4. Filtrar rows con `surface in ['facebook_search', 'instagram_search', 'discord', 'tiktok_search']` hacia el manifest (gap-declarado), no hacia archivos de query.
5. Escribir cada row ejecutable a `working/eje4/queries/batch_YYYYMMDD_HHMMSS/query_<query_id>.json`.
6. Escribir el `batch_manifest.json` con metadatos agregados + lista de las 14 queries gap.

**Dependencias:** `openpyxl` (lectura de xlsx), `json` (stdlib), `pathlib` (stdlib), `datetime` (stdlib para timestamp del batch).

**Longitud esperada:** ~50-80 líneas. No requiere co-diseño extenso — es transformación directa.

---

## Auditoría del output

Ver guardrails anti-drift en `_shared/protocols/core_protocol.md`. Los tres patrones prohibidos (pattern naming inventado en Part 4, thesis statements en Part 4, categorizaciones cross-finding fuera de Part 3) aplican con especial fuerza a los shards del eje4-discovery. Razón: las queries del catálogo son exploratorias y la tentación de "interpretar" los hallazgos es alta — es exactamente el failure mode que se observó en los 4 shards archivados de D-164 (drift ratio de 15% hasta infinito).

Pregunta primaria de auditoría: **"¿esto trajo información que podemos usar?"**, no "¿esto cumple el contrato?". El contrato es infraestructura que soporta el discovery. Un shard con dos findings clean y ningún párrafo de interpretación es mejor que un shard con dos findings clean y cuatro párrafos de teoría compensatoria sobre el territorio.
