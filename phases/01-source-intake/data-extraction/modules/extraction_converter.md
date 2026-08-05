# Module — Extraction Converter (Data Extraction stage 2)

> Serie de reglas: EXC (D-257). Cita canónica: EXC-RN.

## Purpose

Transform Extraction Record skeletons (produced by `phases/01-source-intake/data-extraction/scripts/extraction_prepare.py`) into complete, validated Extraction Records by filling the 15 judgment fields following the Data Extraction contract. The 10 mechanical fields are already populated by stage 1 and must not be modified.

This module is executed by the `extract-records` skill.

## Position in the pipeline

Extraction Converter stage 2 sits between Phase 1 Source Intake and Phase 2 Data Extraction proper. Its output — validated Extraction Records — is the canonical input for Signal Extraction downstream.

This module lives in `phases/01-source-intake/data-extraction/` because it fulfills the Data Extraction contract, not Inventory Mapping operations.

## Inputs

| Path | Purpose |
|---|---|
| `working/data_extraction/skeleton_batches/batch_NNN/skeleton_*.json` | Skeletons produced by stage 1, one file per Extraction Record |
| `working/data_extraction/extraction_prepare_manifest.json` | Stage 1 manifest. Must have `status: complete` before stage 2 can run |
| `phases/01-source-intake/data-extraction/contracts/data_extraction_contract.md` | Extraction contract. Read in full before processing any skeleton |
| `phases/01-source-intake/data-extraction/schemas/data_extraction_record.schema.json` | Schema that completed records must validate against |

## Outputs

| Path | Purpose |
|---|---|
| `working/data_extraction/records/<extraction_id>.json` | Completed, validated Extraction Records. Flat directory for downstream consumption |
| `working/data_extraction/rejected_archive_phase1b/<extraction_id>.json` | Records that could not satisfy the schema with the material available. Staged for GPT recovery |
| `working/data_extraction/extraction_converter_manifest.json` | Stage 2 manifest. Tracks per-skeleton progress, routing decisions, and issues |

The directory is `rejected_archive_phase1b/`, not the `<phase>_gpt_recovery/` pattern used elsewhere — e.g. `working/source_intake/source_intake_gpt_recovery/` from Phase 1 — because this is the name the repo tree and `CLAUDE.md` record for Phase 1b. Material in `rejected_archive_phase1b/` is not rejected material — it is material that carries potential value but could not be completed through the automated flow because required judgment fields were unfillable from the snippet alone.

## Closed vocabulary

### Manifest status values

| Value | Meaning |
|---|---|
| `pending` | Manifest exists but processing has not started |
| `in_progress` | Skeletons are being processed |
| `complete` | All skeletons processed, routed to either `records/` or `rejected_archive_phase1b/` |
| `failed` | Unrecoverable error stopped the run |
| `blocked_by_stage_1_incomplete` | Stage 1 manifest is not `complete`; stage 2 cannot proceed |

### Issue types

| Value | When it applies |
|---|---|
| `skeleton_invalid` | A skeleton file from stage 1 does not have the expected structure or is missing required mechanical fields |
| `contract_case_uncovered` | The case falls outside anything the extraction contract addresses, and no fallback applies |
| `needs_human_review` | Record passed validation but has 4+ uncertainties or one high-severity uncertainty; flagged for operator review |
| `schema_validation_failed` | Completed record does not validate against `data_extraction_record.schema.json`; routed to `rejected_archive_phase1b/` |
| `required_field_unfillable` | A required judgment field cannot be filled from the material available; routed to `rejected_archive_phase1b/` |
| `multiple_required_fields_unfillable` | Two or more required judgment fields cannot be filled; routed to `rejected_archive_phase1b/` (more severe than single-field case) |

This enum is closed. New issue types must be added here and to the manifest schema before the skill can register them.

### Destination values

A record always lands in exactly one of these destinations:

| Value | Meaning |
|---|---|
| `records` | Complete, schema-validated record written to `working/data_extraction/records/` |
| `rejected_archive_phase1b` | Record could not be completed automatically, staged for GPT recovery in `working/data_extraction/rejected_archive_phase1b/` |
| `skeleton_invalid` | Skeleton failed structural validation; no output file produced |

## Operations

Operations run sequentially. Each skeleton is a unit of work; checkpoints happen after each skeleton completes (success or routing to GPT recovery), not per batch. This checkpoint granularity matches the cost of LLM work per skeleton.

### 1. Precondition checks

- Read `working/data_extraction/extraction_prepare_manifest.json`. If it does not exist or `status != complete`, set stage 2 manifest status to `blocked_by_stage_1_incomplete` and exit with a clear message. Do not process anything.
- Read `phases/01-source-intake/data-extraction/contracts/data_extraction_contract.md` in full. If missing, fail with clear message.
- Read `phases/01-source-intake/data-extraction/schemas/data_extraction_record.schema.json`. If missing, fail with clear message.
- Create output directories if they do not exist: `working/data_extraction/records/`, `working/data_extraction/rejected_archive_phase1b/`.

### 2. Load or initialize stage 2 manifest

- If `working/data_extraction/extraction_converter_manifest.json` exists and `status == complete`, exit cleanly with a "nothing to do" message.
- If it exists and `status == in_progress`, read it to determine which skeletons have already been processed. Processing will resume from the next unprocessed skeleton.
- If it does not exist, initialize with `status: pending`, empty counters, and empty arrays.

### 3. Enumerate skeletons to process

- Walk `working/data_extraction/skeleton_batches/batch_NNN/` in batch numeric order.
- Within each batch, process skeletons in alphabetical order by filename (deterministic ordering).
- Skip any skeleton whose `extraction_id` is already in the manifest's `processed_skeletons` list.

### 4. Process each skeleton

For each unprocessed skeleton:

**4.1 Read and validate skeleton structure.** Verify that all 10 mechanical fields are present and populated:
- `extraction_id`, `source_packet_id`, `source_id`, `source_type`, `source_title`
- `source_ref`, `snippet_primary`, `snippet_context_before`, `snippet_context_after`, `traceability_pointer`

If any mechanical field is missing or the JSON cannot be parsed, register a `skeleton_invalid` issue and continue to the next skeleton. Do not produce any output for this skeleton.

Note: `source_date_if_available`, `author_or_actor_if_available`, `snippet_context_before`, and `snippet_context_after` may legitimately be null in the skeleton — null is valid for those fields and is not a structural failure.

**4.2 Apply extraction contract to judgment fields.** Fill the 15 judgment fields following the instructions in `phases/01-source-intake/data-extraction/contracts/data_extraction_contract.md`. For each field:

Fill the judgment fields in this order:
1. `claim_type` — classify using the closed enum from the schema
2. `subject_exact` — name the precise local subject of the claim (critical field; see contract §7)
3. `actor_level` — buyer, seller, product, marketplace, platform, source, third_party, mixed, or unknown
4. `platforms` — explicit platforms mentioned; never infer what is not stated
5. `product_type_if_explicit` — only if the source states it or leaves it unambiguous
6. `metric_type` — from the closed enum; use `unknown` if none applies clearly
7. `metric_value_raw` — original value string/number if present, else null
8. `metric_unit` — unit of the metric value if present, else null
9. `time_scope_raw` — original temporal wording if present, else null
10. `time_scope_normalized_if_safe` — normalized form only if safely derivable without interpretation
11. `geography_if_explicit` — only if the source states a geographic scope
12. `evidence_role` — classify using the closed enum from the schema
13. `local_qualifiers` — list of limiting or conditioning qualifiers to preserve verbatim
14. `uncertainties` — list from the closed enum; mark ambiguity rather than resolving it
15. `parser_notes` — operational notes about parsing decisions; no strategic interpretation

For each judgment field:

- If the contract gives clear instruction and the material supports the decision, fill the field as instructed.
- If there is genuine ambiguity between two or more plausible values, pick the most conservative and add the corresponding code to `uncertainties` from the closed enum in the schema.
- If the case is not covered by the contract at all, look for a fallback rule in the contract's "Failure Reasons" and "Quality Rules" sections. Apply any applicable fallback.
- If no fallback applies either, register a `contract_case_uncovered` issue with specific detail about which field and which case, fill the field with the most conservative possible value or `unknown` if the enum allows it, and continue.

**4.3 Check uncertainty severity.** After all 15 judgment fields are filled, count the uncertainties in the record. If the count is 4 or more, add `needs_human_review` to the issues for this record. The record still proceeds to validation.

**4.4 Validate completed record against schema.** Run the record through `phases/01-source-intake/data-extraction/schemas/data_extraction_record.schema.json`.

- If validation passes: write the record to `working/data_extraction/records/<extraction_id>.json`. Destination is `records`.
- If validation fails because a required judgment field is null or missing: determine which field(s). If exactly one required field is unfillable, register `required_field_unfillable` and route to GPT recovery. If two or more required fields are unfillable, register `multiple_required_fields_unfillable` and route to GPT recovery.
- If validation fails for any other schema reason (type mismatch, enum violation, pattern mismatch), register `schema_validation_failed` with the specific validation error and route to GPT recovery.

**4.5 Write to destination.**

- For `records` destination: write the complete record JSON to `working/data_extraction/records/<extraction_id>.json`.
- For `rejected_archive_phase1b` destination: write a recovery-ready JSON to `working/data_extraction/rejected_archive_phase1b/<extraction_id>.json` using the structure defined in "GPT recovery staging" below.

**4.6 Update manifest.** After the record is written, append the extraction_id to the manifest's `processed_skeletons` list with its destination and any issue types registered. Update counters. Save the manifest to disk.

This update happens after every skeleton, not every batch. If the process is interrupted, resumption starts from the next unprocessed skeleton with zero work lost.

### 5. Completion

When all skeletons across all batches have been processed, set manifest status to `complete`, record `completed_at` timestamp, and exit.

## GPT recovery staging

Records routed to `rejected_archive_phase1b/` are not raw partial records. They are staged with the structure the GPT recovery flow needs as input when it is eventually implemented.

Each file in `rejected_archive_phase1b/` contains:

```json
{
  "extraction_id": "ER-<packet_id>-<snippet_id>",
  "recovery_type": "data_extraction_schema_incomplete",
  "origin_stage": "data_extraction_stage_2",
  "original_skeleton": { "...the stage 1 skeleton as read..." },
  "partial_record": { "...the record as far as stage 2 could complete it..." },
  "failure_detail": {
    "issue_type": "schema_validation_failed | required_field_unfillable | multiple_required_fields_unfillable",
    "missing_required_fields": ["field_name_1", "field_name_2"],
    "validation_error": "specific error message from schema validation, if applicable",
    "contract_notes": "any notes the skill recorded about what the contract could not resolve"
  },
  "recovery_guidance": {
    "suggested_direction": "what the GPT should investigate to recover the missing information",
    "source_ref": "the source_ref from the original skeleton",
    "source_type": "the source_type from the original skeleton",
    "source_packet_id": "the source_packet_id to trace back to the originating packet"
  },
  "staged_at": "<iso timestamp>"
}
```

The `recovery_guidance.suggested_direction` must be concrete. "Investigate the source to determine the subject_exact for the snippet about fee calculations" is good. "Find more information" is not acceptable.

## Promotion criteria

A record is promoted to `working/data_extraction/records/` if and only if:

1. It validates against `phases/01-source-intake/data-extraction/schemas/data_extraction_record.schema.json`
2. No required judgment field is null or missing
3. The skeleton structure was valid (it did not fail at step 4.1)

A record is routed to `working/data_extraction/rejected_archive_phase1b/` if:

1. It failed schema validation for any reason AND
2. The skeleton structure was valid (otherwise it does not produce any output; it only produces a `skeleton_invalid` issue)

A record can be in `records/` and simultaneously flagged `needs_human_review` in the manifest. These are valid records that need operator attention, not failed records. They are consumed downstream normally; the flag exists so the operator can prioritize review.

## Extraction quality rules (from contract)

These rules apply during step 4.2 when filling judgment fields. Violations must be marked in `uncertainties` or `parser_notes`, not silently fixed.

**EXC-R1 (Rule 1): Do not collapse functional layers.**
- checkout ≠ payout
- fee base ≠ net retained
- active buyers ≠ seller discoverability
- platform traffic ≠ seller sales outcome

**EXC-R2 (Rule 2): Do not convert context into claim.**
A snippet may provide context for a claim without being the claim itself. Mark `evidence_role` as `local_context` when appropriate rather than `direct_claim`.

**EXC-R3 (Rule 3): Do not drop qualifiers.**
If the snippet says "at the time of writing", "in the US", "for shops under $10k", or similar — preserve verbatim in `local_qualifiers`.

**EXC-R4 (Rule 4): Do not resolve ambiguity; mark it.**
`unknown` > invented inference. When two values are equally plausible for an enum field, pick the more conservative and add the corresponding uncertainty code.

**EXC-R5 (Rule 5): One Extraction Record, one source.**
Each skeleton already represents one snippet from one source. Never synthesize across snippets or packets.

**EXC-R6 (Rule 6): Do not summarize the snippet.**
Preserve wording. `snippet_primary` comes from the skeleton unchanged; do not rewrite it when filling judgment fields.

## Fail states

| Situation | Behavior |
|---|---|
| Stage 1 manifest missing or not complete | Set status `blocked_by_stage_1_incomplete`, exit |
| Extraction contract missing | Fatal error, exit with clear message |
| Extraction record schema missing | Fatal error, exit with clear message |
| Skeleton directory empty | Fatal error, exit with clear message |
| Individual skeleton unreadable or malformed | Register `skeleton_invalid`, continue with next |
| I/O error writing a record or recovery file | Register issue with detail, continue with next skeleton |

Only three situations are fatal: missing stage 1 completion, missing contract or schema files, and empty skeleton directory. Everything else is a per-skeleton issue that does not stop the run.

## Resumability

Checkpoint granularity is per skeleton, not per batch.

On startup:

1. Read `working/data_extraction/extraction_converter_manifest.json`.
2. If `status == complete`: exit cleanly.
3. If `status == in_progress`: read the `processed_skeletons` list. Skip any skeleton whose `extraction_id` is already in that list. Resume from the first unprocessed skeleton.
4. If `status == blocked_by_stage_1_incomplete`: re-verify stage 1. If stage 1 is now `complete`, reset stage 2 status to `in_progress` and proceed. If stage 1 is still not complete, exit with message.
5. If `status == failed`: do not auto-resume. Operator must inspect the manifest, resolve the failure cause, and manually reset the status before re-running.
6. If manifest does not exist: create with `status: in_progress`, empty processed list, and proceed.

## Skill that executes this module

`.claude/skills/extract-records/SKILL.md`

---

## Notes on naming

The directory is `rejected_archive_phase1b/`, per the repo tree and `CLAUDE.md` — not `extraction_gpt_recovery/`, which does not exist. Despite the name, placement here is not a quality judgment. The material it contains is not rejected in the sense of being worthless. It is material that the automated flow could not complete because required judgment fields were unfillable from the snippet as parsed. The GPT recovery flow exists specifically to investigate such material further and recover what is needed for it to fulfill the schema.

This phase does not follow the `<phase>_gpt_recovery/` pattern used by `working/data_gathering/phase0_part4_gpt_recovery/` and `working/source_intake/source_intake_gpt_recovery/` — its directory has a different name. Each phase that produces recovery candidates has its own directory, allowing the GPT recovery flow to apply the appropriate recovery logic per phase.
