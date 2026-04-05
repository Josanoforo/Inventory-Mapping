---
name: legacy-signal-card-migration
description: Migrate legacy Signal Cards to the new upstream ontology by auditing source metadata, proposing canonical mappings, and classifying recoverability. Reads from card_index.jsonl, writes Migration Records to legacy_signal_card_migrations.jsonl.
---

# Skill: Legacy Signal Card Migration

## Authority chain

1. `legacy-migration/contracts/legacy_signal_card_migration.md` — contract (overrides this skill)
2. `legacy-migration/modules/01_legacy_signal_card_migration.md` — module (overrides this skill)
3. `legacy-migration/legacy_mapping_notes.md` — mapping rules
4. This SKILL.md — executable routine

---

## What this skill does

Reads legacy Signal Cards from `working/index/card_index.jsonl` and produces Migration Records in `legacy-migration/working/migrations/legacy_signal_card_migrations.jsonl`.

For each card it:
1. Extracts legacy metadata (source, source_type, evidence_base)
2. Runs 6 structured checks
3. Proposes canonical source_type and evidence_role with declared confidence
4. Assigns traceability_grade and recoverability_status
5. Records failure_reasons and suggested_followup
6. Writes one Migration Record to the JSONL output
7. Updates the manifest

---

## What this skill does NOT do

- Does not validate against signal_card.schema.json
- Does not convert legacy cards to canonical Signal Cards
- Does not build tensions or patterns
- Does not interpret the market
- Does not connect to upstream/ or modify input/

---

## Inputs

- `working/index/card_index.jsonl` — legacy Signal Cards
- `legacy-migration/legacy_mapping_notes.md` — mapping rules
- `legacy-migration/contracts/legacy_signal_card_migration.md` — rules
- `legacy-migration/schemas/legacy_signal_card_migration.schema.json` — output schema

---

## Outputs

- `legacy-migration/working/migrations/legacy_signal_card_migrations.jsonl` — Migration Records (append mode)
- `legacy-migration/working/manifests/legacy_migration_manifest.json` — updated manifest

---

## Execution steps

### 0. Read manifest to determine resume point

Read `legacy-migration/working/manifests/legacy_migration_manifest.json`.
Check `last_processed_id`. If set, skip all cards with `id <= last_processed_id` in the JSONL.

### 1. Open card_index.jsonl

Process cards sequentially or in a batch.
For a sample run, process only the requested N cards.

### 2. For each card — extract legacy fields

```
legacy_signal_id        = card.id
legacy_source_type_raw  = card.source_type  (null if absent)
legacy_evidence_role_raw = null  (legacy cards do not have this field)
legacy_source_ref_raw   = card.source       (raw value, may contain URL or label)
legacy_source_label_raw = card.source       (same field, dual-used as label)
```

Note: the legacy `source` field serves as both ref and label. Preserve verbatim.

### 3. Run checks — in this order

Apply rules from Module 01:

1. `reference_available` — is `legacy_source_ref_raw` non-null and non-empty?
2. `reference_stable` — does it contain `https://`? (pass=yes, flag=domain-only, fail=label-only)
3. `source_type_mappable` — apply mapping table from `legacy_mapping_notes.md`
4. `evidence_role_mappable` — infer from source_type + source_ref + observation
5. `snippet_verifiability` — is `evidence_base` present AND reference_stable = pass or flag?
6. `legacy_value_requires_enum_extension` — is the legacy value unknown to both old and new enum?

### 4. Propose canonical mappings

Using `legacy_mapping_notes.md` as the primary reference:

- Assign `canonical_source_type` from the mapping table
- Assign confidence: high/medium/low/none
- Infer `canonical_evidence_role` from source_type + source context
- Assign confidence: high/medium/low/none

If no mapping is possible, assign null with confidence = none.

**Key rules (enforced, never skip):**
- `benchmark` → never a canonical source_type; trigger `benchmark_is_not_source_type`
- `listing` → `product_listing` (not marketplace_listing)
- `report` → `report` (not article)
- `news` → `news` (not article)
- Third-party blog describing platform policy → `comparative_commentary` or `reported_event`, never `official_policy`
- Crunchbase or company database → `database_profile` / `database_fact`
- SERP or search results → `search_results_page` / `observed_platform_state`

### 5. Assign traceability_grade

```
complete   → reference_stable=pass AND snippet_verifiability=pass
partial    → reference_stable=pass AND snippet_verifiability=flag
             OR reference_stable=flag AND snippet_verifiability=pass
weak       → reference_available=pass AND reference_stable=fail
none       → reference_available=fail
```

### 6. Assign recoverability_status

Apply in order (first match wins):
1. `reference_available=fail` AND `snippet_verifiability=fail` → `unrecoverable`
2. `legacy_value_requires_enum_extension=fail` → `schema_gap`
3. `benchmark_is_not_source_type` in failure_reasons → `schema_gap` (if no URL) or `mappable_with_flags` (if URL present and type inferable)
4. `reference_available=pass` AND `reference_stable=fail` → `needs_source_recovery`
5. Any check = flag (no fails) → `mappable_with_flags`
6. All checks = pass → `clean_mappable`

### 7. Collect failure_reasons

Apply codes from the contract based on check results. Multiple codes allowed.

### 8. Assign suggested_followup

Apply the table from Module 01.

### 9. Build Migration Record

Produce one JSON object:

```json
{
  "migration_id": "MIG-<legacy_signal_id>",
  "legacy_signal_id": "<id>",
  "legacy_source_type_raw": "<value or null>",
  "legacy_evidence_role_raw": null,
  "legacy_source_ref_raw": "<value or null>",
  "legacy_source_label_raw": "<value or null>",
  "canonical_source_type": "<value or null>",
  "canonical_source_type_confidence": "<high|medium|low|none>",
  "canonical_evidence_role": "<value or null>",
  "canonical_evidence_role_confidence": "<high|medium|low|none>",
  "traceability_grade": "<complete|partial|weak|none>",
  "recoverability_status": "<status>",
  "checks": {
    "reference_available": { "status": "...", "rationale": "..." },
    "reference_stable": { "status": "...", "rationale": "..." },
    "source_type_mappable": { "status": "...", "rationale": "..." },
    "evidence_role_mappable": { "status": "...", "rationale": "..." },
    "snippet_verifiability": { "status": "...", "rationale": "..." },
    "legacy_value_requires_enum_extension": { "status": "...", "rationale": "..." }
  },
  "failure_reasons": [],
  "migration_notes": [],
  "suggested_followup": "<value or null>",
  "migrated_at": "<ISO 8601 date>",
  "migrated_by": "legacy-signal-card-migration-skill"
}
```

Append to `legacy-migration/working/migrations/legacy_signal_card_migrations.jsonl`.

### 10. Update manifest

After each card (or end of batch), update:

```json
{
  "total_cards_seen": <n>,
  "migrated_count": <n>,
  "clean_mappable_count": <n>,
  "mappable_with_flags_count": <n>,
  "schema_gap_count": <n>,
  "needs_source_recovery_count": <n>,
  "unrecoverable_count": <n>,
  "last_processed_id": "<last id>",
  "last_updated": "<ISO 8601>",
  "migration_version": "0.1"
}
```

---

## Batch behavior

- Default: process all unprocessed cards from the manifest resume point
- Sample mode: if invoked with `--sample N`, process only the next N unprocessed cards
- Never reprocess already-migrated cards unless explicitly asked

---

## Notes discipline

`migration_notes` entries must be operational only:
- "Source field contains URL and label combined; split applied."
- "legacy_source_type_raw = benchmark; inferred database_profile from Crunchbase URL."
- "No evidence_base field in legacy card; snippet_verifiability marked fail."

Never in migration_notes:
- market interpretation
- tension language
- importance assessment
- comparison between cards
