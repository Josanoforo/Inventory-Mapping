# Module 01 — Legacy Signal Card Migration

## Authority

This module is normative for the legacy-migration rail.
It overrides the SKILL if there is a conflict.
It does not override `legacy_signal_card_migration.md` (contract).

---

## Scope

This module governs one operation only:

> Read legacy Signal Cards from `working/index/card_index.jsonl`, extract available metadata, propose canonical mappings, classify recoverability, and produce Migration Records in `legacy-migration/working/migrations/legacy_signal_card_migrations.jsonl`.

---

## Inputs

| Source | Field(s) used |
|---|---|
| `working/index/card_index.jsonl` | `id`, `source`, `source_type`, `evidence_base`, `date`, `round`, `observation`, `extraction_status` |
| `legacy-migration/legacy_mapping_notes.md` | mapping rules per legacy source_type value |
| `legacy-migration/contracts/legacy_signal_card_migration.md` | migration rules |
| `legacy-migration/schemas/legacy_signal_card_migration.schema.json` | output schema |

---

## Outputs

| File | Description |
|---|---|
| `legacy-migration/working/migrations/legacy_signal_card_migrations.jsonl` | One Migration Record per processed legacy card |
| `legacy-migration/working/manifests/legacy_migration_manifest.json` | Running counters updated after each batch |

---

## Processing sequence

For each legacy Signal Card:

### Step 1 — Extract legacy metadata

Read from `card_index.jsonl`:
- `id` → `legacy_signal_id`
- `source` → `legacy_source_ref_raw` and `legacy_source_label_raw`
- `source_type` → `legacy_source_type_raw`
- `evidence_base` → used for `snippet_verifiability` check
- `extraction_status` → informational

If a field is absent in the legacy card, record `null` in the corresponding `legacy_*_raw` field.

### Step 2 — Run checks

#### `reference_available`
- pass: any non-null, non-empty value in `legacy_source_ref_raw` or `legacy_source_label_raw`
- fail: both are null or empty

#### `reference_stable`
- pass: `legacy_source_ref_raw` contains a full URL (`https://`)
- flag: contains a partial URL, domain only, or a named source without URL
- fail: only a label with no URL or path
- not_applicable: if `reference_available` failed

#### `source_type_mappable`
Apply mapping table from `legacy_mapping_notes.md`:
- pass: legacy value maps to a canonical value with high or medium confidence
- flag: maps with low confidence or via indirect inference
- fail: no mapping exists (triggers `source_type_not_in_new_enum` or `benchmark_is_not_source_type`)

#### `evidence_role_mappable`
Infer from combination of `legacy_source_type_raw`, `legacy_source_ref_raw`, and `observation`:
- pass: role can be assigned with high or medium confidence
- flag: role is plausible but borderline
- fail: no role can be inferred reliably

#### `snippet_verifiability`
- pass: `evidence_base` is non-null and `reference_stable` passed
- flag: `evidence_base` present but reference is only partial
- fail: `evidence_base` is null or missing, or reference is none
- not_applicable: not used

#### `legacy_value_requires_enum_extension`
- fail: legacy value is not in the old enum AND not in the new enum
- pass: legacy value maps to a new enum value (even if imperfectly)
- not_applicable: if source_type field is null

### Step 3 — Assign canonical proposals

Apply mapping rules from `legacy_mapping_notes.md` to assign:
- `canonical_source_type` (or null if not mappable)
- `canonical_source_type_confidence`
- `canonical_evidence_role` (or null if not mappable)
- `canonical_evidence_role_confidence`

Never invent a canonical value without declaring confidence.

### Step 4 — Assign traceability_grade

| Condition | Grade |
|---|---|
| Full URL + verifiable snippet | `complete` |
| Full URL, no precise snippet anchor | `partial` |
| Named source without URL, or URL without snippet | `weak` if URL present but incomplete; `partial` if URL present |
| No reference of any kind | `none` |

Simplified rule:
- `complete`: URL + evidence_base + reference_stable = pass
- `partial`: URL present but reference_stable = flag, or evidence_base present but snippet_verifiability = flag
- `weak`: reference_available = pass but reference_stable = fail
- `none`: reference_available = fail

### Step 5 — Assign recoverability_status

Apply these rules in order:

1. If `reference_available = fail` AND `snippet_verifiability = fail`: → `unrecoverable`
2. If `benchmark_is_not_source_type` in failure_reasons AND no URL present: → `schema_gap` or `needs_source_recovery`
3. If `source_type_not_in_new_enum` in failure_reasons AND `legacy_value_requires_enum_extension = fail`: → `schema_gap`
4. If `reference_available = pass` AND `reference_stable = fail`: → `needs_source_recovery`
5. If all checks pass with no critical failures: → `clean_mappable`
6. If checks pass but flags present: → `mappable_with_flags`

### Step 6 — Assign failure_reasons

Collect failure codes from the check results and apply the rules from the contract. A card may have multiple failure reasons.

### Step 7 — Assign suggested_followup

| Condition | Suggested followup |
|---|---|
| `needs_source_recovery` | `reopen_source_for_url` or `reopen_source_for_snippet` |
| `schema_gap` with recoverable type inference | `reclassify_source_type_manually` |
| `mappable_with_flags` with ambiguous role | `reclassify_evidence_role_manually` |
| Multiple fused sources in observation | `split_into_multiple_records` |
| `schema_gap` without clear path | `mark_as_schema_gap_and_hold` |
| `unrecoverable` | `discard_and_document` |
| `clean_mappable` | `none` |

### Step 8 — Write Migration Record

Produce one JSON object per card conforming to `legacy_signal_card_migration.schema.json`.
Append to `legacy-migration/working/migrations/legacy_signal_card_migrations.jsonl`.

### Step 9 — Update manifest

After each batch, update `legacy-migration/working/manifests/legacy_migration_manifest.json` with current counts.

---

## Resumability

The manifest tracks `last_processed_id`. If interrupted, resume from the card after the last recorded `legacy_signal_id` in the JSONL output.

---

## What this module does NOT do

- Does not validate migration records against `signal_card.schema.json`
- Does not produce Extraction Records or Source Packets
- Does not build tensions or patterns
- Does not connect output to the upstream pipeline automatically
- Does not interpret the market
- Does not decide what passes to Inventory Mapping

---

## Quality criterion

The migration is running correctly if:
- every `clean_mappable` record has a full URL and an assignable canonical source_type with at least medium confidence
- every `schema_gap` record documents exactly which value requires enum extension
- no `official_policy` is assigned to a third-party source describing platform policy
- `benchmark` never appears as a canonical source_type
- `marketplace_listing` never appears as a canonical source_type (replaced by `product_listing`)
