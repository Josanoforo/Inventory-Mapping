# Phase 1 Inventory Report — Bloque 2

Lo que existe realmente en el repo para Phase 1. No lo que los blueprints dicen que debería existir.

---

## 1. Estructura de directorios

```
phases/01-source-intake/
├── contracts/
│   ├── source_intake_contract.md
│   └── source_intake_validator.md
├── modules/
│   └── converter.md
├── reference/
│   └── source_packet_conversion_template.md
├── schemas/
│   ├── converter_manifest.schema.json
│   ├── converter_prepare_manifest.schema.json
│   ├── rejected_archive_record.schema.json
│   ├── source_intake_validation.schema.json
│   └── source_packet.schema.json
├── scripts/
│   ├── converter_prepare.py         (542 líneas)
│   └── route_unrecoverable.py       (159 líneas)
└── data-extraction/
    ├── contracts/
    │   ├── data_extraction_contract.md
    │   └── data_extraction_validator.md
    ├── modules/
    │   └── extraction_converter.md
    ├── schemas/
    │   ├── data_extraction_record.schema.json
    │   ├── data_extraction_validator.schema.json
    │   ├── extraction_converter_manifest.schema.json
    │   └── extraction_prepare_manifest.schema.json
    └── scripts/
        └── extraction_prepare.py    (418 líneas)
```

**Total: 19 archivos — 3 scripts Python (1,119 líneas), 7 Markdown, 9 JSON schemas.**

---

## 2. Scripts Python

| Script | Líneas | Input | Output |
|---|---|---|---|
| `scripts/converter_prepare.py` | 542 | `working/data_gathering/findings/*.json` | `working/source_intake/skeleton_batches/` |
| `scripts/route_unrecoverable.py` | 159 | `working/data_gathering/diagnostics/part_4/*.json` | `working/source_intake/rejected_archive/` |
| `data-extraction/scripts/extraction_prepare.py` | 418 | `working/source_intake/packets/*.json` | `working/data_extraction/skeleton_batches/` |

### converter_prepare.py — primera línea de docstring

```
converter_prepare.py — Converter stage 1 (preparación mecánica).

Lee findings producidos por parse_dg_shard.py desde
working/data_gathering/findings/*.json, los agrupa por URL de fuente, y
escribe esqueletos de Source Packet en working/source_intake/skeleton_batches/
para que el stage 2 (skill LLM) llene los campos de juicio.
```

Llena 11 campos mecánicos. Deja 8 campos de juicio vacíos/null para stage 2 (skill `p1-convert-findings`).
Idempotente. Retomable desde manifest.

### route_unrecoverable.py — primera línea de docstring

```
Routes unrecoverable findings from working/data_gathering/diagnostics/part_4/
to working/source_intake/rejected_archive/, creating RejectedArchiveRecord JSON
files validated against rejected_archive_record.schema.json.

Run this BEFORE converter_prepare.py.
```

Filtra por whitelist `RECOVERY_AGENT_SOURCE_TOOLS = ["gpt_custom"]`.
Los archivos en `part_4/` cuyo `source_tool` no esté en la whitelist se saltan silenciosamente.

### extraction_prepare.py — primera línea de docstring

```
extraction_prepare.py — Extraction stage 1 (preparación mecánica).

Lee Source Packets validados de working/source_intake/packets/*.json,
y para cada snippet en cada packet genera un skeleton de Extraction Record
en working/data_extraction/skeleton_batches/ para que el stage 2 (skill LLM)
llene los campos de juicio.
```

Llena 10 campos mecánicos. Deja 15 campos de juicio vacíos/null para stage 2 (skill `p1-extract-records`).
Idempotente. Retomable desde manifest.

---

## 3. Archivos Markdown

| Archivo | Primera línea |
|---|---|
| `contracts/source_intake_contract.md` | `# Source Intake Contract v0.1` |
| `contracts/source_intake_validator.md` | `# Source Intake Validator` |
| `modules/converter.md` | `# Module — Converter (Source Intake stage 2)` |
| `reference/source_packet_conversion_template.md` | `# Source Packet conversion template` |
| `data-extraction/contracts/data_extraction_contract.md` | `# Data Extraction Contract v0.1` |
| `data-extraction/contracts/data_extraction_validator.md` | `# Data Extraction Validator` |
| `data-extraction/modules/extraction_converter.md` | `# Module — Extraction Converter (Data Extraction stage 2)` |

**Extracto de `reference/source_packet_conversion_template.md` (líneas 1–9):**
```
# Source Packet conversion template

Conversión manual de findings de Data Gathering a Source Packets validables
por el repo. Para usar mientras no exista un script automatizado.

Un Source Packet es la unidad que el repo de Inventory-Mapping espera como
input para Source Intake. Cada packet representa una fuente (una URL o página)
con todos sus snippets relevantes y metadata mínima.

Las findings de DG no mapean 1-a-1 a packets. Múltiples findings de la misma
URL colapsan en un solo packet con múltiples snippets.
```

---

## 4. JSON Schemas

### Source Intake (5 schemas)

| Schema | Descripción |
|---|---|
| `source_packet.schema.json` | Canonical schema para un Source Packet producido por Source Intake |
| `source_intake_validation.schema.json` | Resultado de validación de un Source Packet |
| `converter_prepare_manifest.schema.json` | Manifest de stage 1 (converter_prepare.py). Tracks skeleton batch production con checkpoint para resumption |
| `converter_manifest.schema.json` | Manifest de stage 2 (skill convert-findings). Tracks per-skeleton processing con checkpoint |
| `rejected_archive_record.schema.json` | Registro de finding interceptado antes de Phase 1 por ser unrecoverable |

### Data Extraction (4 schemas)

| Schema | Descripción |
|---|---|
| `data_extraction_record.schema.json` | Canonical schema para un Extraction Record producido por Data Extraction |
| `data_extraction_validator.schema.json` | Resultado de validación de un Extraction Record |
| `extraction_prepare_manifest.schema.json` | Manifest de stage 1 (extraction_prepare.py). Tracks progress con checkpoint |
| `extraction_converter_manifest.schema.json` | Manifest de stage 2 (skill extract-records). Tracks per-skeleton progress |

---

## 5. Gates y validators

No existen módulos "gate" separados en Phase 1. La validación está implementada como:

- **Schemas JSON** (`source_intake_validation.schema.json`, `data_extraction_validator.schema.json`): definen el contrato de validación.
- **Contracts Markdown** (`source_intake_contract.md`, `data_extraction_contract.md`): especifican qué valida y qué no valida cada stage.
- **Manifests**: cada script escribe un manifest con estado (`pending`, `done`, `error`) por item procesado, lo que permite resumption.

Hay validators definidos como documentos (`.md`) pero no como scripts ejecutables independientes. La validación de schemas se asume implementada en los skills de stage 2 (`p1-convert-findings`, `p1-extract-records`).

---

## 6. Conexión Phase 0 → Phase 1

### Flujo documentado explícitamente en docstrings

```
Phase 0 output
├── working/data_gathering/findings/*.json          ──► converter_prepare.py (Stage 1 SI)
└── working/data_gathering/diagnostics/part_4/*.json ──► route_unrecoverable.py

Phase 1 Source Intake
├── working/source_intake/skeleton_batches/         ──► skill p1-convert-findings (Stage 2 SI)
└── working/source_intake/rejected_archive/         (dead end — archivados)

Phase 1 Source Intake output
└── working/source_intake/packets/*.json            ──► extraction_prepare.py (Stage 1 DE)

Phase 1 Data Extraction
└── working/data_extraction/skeleton_batches/       ──► skill p1-extract-records (Stage 2 DE)

Phase 1 Data Extraction output
└── working/data_extraction/records/*.json          ──► Phase 2 Signal Extraction (input)
```

**Nota de orden de ejecución:** `route_unrecoverable.py` debe correr ANTES de `converter_prepare.py`. El docstring lo declara explícitamente.

---

## 7. Estado de implementación — lo que existe vs. lo que falta

### Existe en el repo

| Componente | Estado |
|---|---|
| `converter_prepare.py` (Source Intake Stage 1) | Completo — listo para ejecutar |
| `route_unrecoverable.py` (pre-proceso Part 4) | Completo — listo para ejecutar |
| `extraction_prepare.py` (Data Extraction Stage 1) | Completo — listo para ejecutar |
| Contracts (SI y DE) | Completos |
| Validators (SI y DE) — como documentos Markdown | Completos |
| Schemas (9 archivos) | Completos |
| Modules (SI stage 2, DE stage 2) | Especificados como Markdown |
| Reference — conversion template | Completo |

### No existe en el repo (referenciado pero ausente)

| Componente | Referenciado en | Estado |
|---|---|---|
| Skill `p1-convert-findings` (Source Intake Stage 2) | `modules/converter.md` | Skill disponible en `.claude/skills/` — no es un script del repo |
| Skill `p1-extract-records` (Data Extraction Stage 2) | `data-extraction/modules/extraction_converter.md` | Skill disponible en `.claude/skills/` — no es un script del repo |
| Validator script ejecutable (SI) | `contracts/source_intake_validator.md` | Solo documentado, no implementado como script |
| Validator script ejecutable (DE) | `data-extraction/contracts/data_extraction_validator.md` | Solo documentado, no implementado como script |

### Estado de los directorios working/ de Phase 1

| Directorio | Estado |
|---|---|
| `working/source_intake/skeleton_batches/` | Existe, vacío (0 archivos) |
| `working/source_intake/packets/` | Existe, vacío (0 archivos) |
| `working/source_intake/rejected_archive/` | Existe, vacío (0 archivos) |
| `working/source_intake/enrichment/` | Existe, vacío (0 archivos) |
| `working/source_intake/source_intake_gpt_recovery/` | Existe, vacío (0 archivos) |
| `working/data_extraction/skeleton_batches/` | Existe, vacío (0 archivos) |
| `working/data_extraction/records/` | Existe, vacío (0 archivos) |
| `working/data_extraction/rejected_archive/` | Existe, vacío (0 archivos) |

**Phase 1 no ha sido ejecutada.** Los directorios de output están creados pero ningún script ha producido output todavía.
