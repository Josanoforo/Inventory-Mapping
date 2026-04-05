# Legacy Migration — Usage Guide

---

## Principio clave

**Migración legado = diagnóstico y traducción.**
**No = validación canónica final.**

La migración legado no produce Signal Cards canónicas nuevas.
Produce Migration Records: registros de auditoría que documentan si una legacy card puede mapearse al nuevo sistema, con qué confianza, y qué follow-up requiere.

---

## Cuándo usar migración legado

Usar este carril cuando:

1. La Signal Card fue producida **antes del rediseño upstream** (antes de que existieran Source Intake → Data Extraction → Signal Extraction).
2. La card fue creada **bajo enums o criterios viejos** (e.g. `source_type = benchmark`, `listing`, `report` antes del parche de ontología).
3. El material **no nació desde el pipeline upstream** — no hay Source Packet, no hay Extraction Record, no pasó por el entry gate canónico.
4. Quieres auditar **cuántas de las 1,561 legacy Signal Cards son recuperables** antes de decidir si re-correr el corpus.

---

## Cuándo NO usar migración legado

No usar este carril cuando:

1. El material es **nuevo** y fue producido por el pipeline upstream (Source Intake → Data Extraction → Signal Extraction).
2. La card **ya pasó** por `signal_to_inventory_entry_gate`.
3. Estás trabajando con **Extraction Records o Source Packets** — esos usan sus propios validators.

---

## Significado de cada recoverability_status

### `clean_mappable`

La legacy card puede traducirse al nuevo sistema sin pérdida relevante.

Condiciones:
- Tiene URL completa y estable
- `source_type` legacy mapea a un valor canónico con confianza alta o media
- `evidence_role` es inferible con confianza alta o media
- Sin failure_reasons críticos

Acción: puede avanzar a clasificación canónica si se decide hacer eso.

---

### `mappable_with_flags`

La legacy card tiene valor y se puede traducir, pero con advertencias explícitas.

Condiciones típicas:
- Tiene referencia pero no URL completa
- El mapeo de source_type o evidence_role es de confianza media o baja
- Hay un failure_reason no crítico (e.g. `source_ref_partial_only`, `third_party_policy_contamination`)

Acción: puede avanzar pero el receptor debe respetar los flags. No tratar como clean.

---

### `schema_gap`

La legacy card usa un valor que no existe en el nuevo enum y no puede mapearse sin una decisión de diseño.

Condiciones típicas:
- `legacy_source_type_raw = benchmark` sin tipo inferable
- Fuente es una herramienta analítica no cubierta por el enum
- El tipo real requeriría un nuevo valor en el enum canónico

Acción: documentar el gap. No forzar mapeo. Escalar a decisión de diseño ontológico.

---

### `needs_source_recovery`

La legacy card tiene valor potencial pero falta material de trazabilidad para migrar limpiamente.

Condiciones típicas:
- Hay nombre de fuente pero no URL
- El snippet no es verificable sin abrir la fuente
- El `suggested_followup` apunta a `reopen_source_for_url` o `reopen_source_for_snippet`

Acción: follow-up acotado para recuperar la referencia. No migrar todavía.

---

### `unrecoverable`

La legacy card no puede migrarse porque no hay trazabilidad posible.

Condiciones típicas:
- Sin referencia de ningún tipo
- El snippet no puede verificarse bajo ningún método
- Múltiples failure_reasons críticos simultáneos (e.g. `source_ref_missing` + `snippet_missing`)

Acción: documentar y excluir. No intentar recuperar. Registrar en el manifest.

---

## Flujo de uso típico

### Para correr una muestra

1. Invocar el skill `legacy-signal-card-migration` con `--sample N`
2. El skill lee N cards desde `working/index/card_index.jsonl` (desde el punto de resume del manifest)
3. Produce N Migration Records en `legacy-migration/working/migrations/legacy_signal_card_migrations.jsonl`
4. Actualiza `legacy-migration/working/manifests/legacy_migration_manifest.json`

### Para correr el corpus completo

1. Invocar el skill sin `--sample`
2. El skill procesa todas las cards no procesadas desde el manifest
3. Al terminar, actualizar `legacy-migration/output/legacy_migration_summary.md` con los totales del manifest

### Para revisar resultados

1. Leer `legacy_migration_manifest.json` para el resumen por status
2. Filtrar `legacy_signal_card_migrations.jsonl` por `recoverability_status` o `failure_reasons` para análisis detallado
3. Revisar `legacy_migration_summary.md` para la distribución general

---

## Qué NO hacer durante la migración

- No modificar `working/index/card_index.jsonl` ni `input/signal_cards_round_*.md`
- No validar migration records contra `signal_card.schema.json`
- No producir Tension Candidates ni conectar con Inventory Mapping
- No forzar `clean_mappable` en cards sin URL
- No asignar `official_policy` a fuentes de terceros
- No colapsar `report` o `news` a `article`
- No usar `marketplace_listing` (no existe en el nuevo enum)

---

## Archivos del carril

```
legacy-migration/
├── contracts/
│   └── legacy_signal_card_migration.md      ← reglas autoritativas
├── schemas/
│   └── legacy_signal_card_migration.schema.json
├── modules/
│   └── 01_legacy_signal_card_migration.md   ← secuencia de procesamiento
├── .claude/skills/legacy-signal-card-migration/
│   └── SKILL.md                              ← rutina ejecutable
├── working/
│   ├── migrations/
│   │   └── legacy_signal_card_migrations.jsonl
│   └── manifests/
│       └── legacy_migration_manifest.json
├── output/
│   └── legacy_migration_summary.md
├── legacy_mapping_notes.md                   ← tabla de mapeo por tipo legacy
└── legacy_migration_usage.md                 ← este archivo
```
