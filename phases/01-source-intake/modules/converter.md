# Module — Converter (Source Intake stage 2)

## Purpose

Transform Source Packet skeletons (produced by `upstream/source-intake/scripts/converter_prepare.py`) into complete, validated Source Packets by filling the 8 judgment fields following the conversion template. The 11 mechanical fields are already populated by stage 1 and must not be modified.

This module is executed by the `convert-findings` skill.

## Position in the pipeline

Converter stage 2 sits between Phase 0 Data Gathering and Phase 1 Source Intake proper. It completes the bridge that was previously assumed but never implemented. Its output — validated Source Packets — is the canonical input for Data Extraction (Phase 2) downstream.

This module does not belong to Inventory Mapping. It lives in `upstream/source-intake/` because it fulfills the Source Intake contract, not IM operations.

## Inputs

| Path | Purpose |
|---|---|
| `working/source_intake/skeleton_batches/batch_NNN/skeleton_*.json` | Skeletons produced by stage 1, one file per packet |
| `working/source_intake/converter_prepare_manifest.json` | Stage 1 manifest. Must have `status: complete` before stage 2 can run |
| `upstream/source-intake/reference/source_packet_conversion_template.md` | Conversion guide. Read in full before processing any skeleton |
| `upstream/source-intake/schemas/source_packet.schema.json` | Schema that completed packets must validate against |

## Outputs

| Path | Purpose |
|---|---|
| `working/source_intake/packets/<packet_id>.json` | Completed, validated Source Packets. Flat directory for downstream consumption |
| `working/source_intake/source_intake_gpt_recovery/<packet_id>.json` | Packets that could not satisfy the schema with the material available. Staged for GPT recovery flow (see section "GPT recovery staging") |
| `working/source_intake/converter_manifest.json` | Stage 2 manifest. Tracks progress, issues, and human review flags |

The directory `source_intake_gpt_recovery/` parallels the existing `working/data_gathering/phase0_part4_gpt_recovery/` defined in D-108. The naming convention is `<phase>_gpt_recovery/` — each phase that produces recovery candidates has its own directory, and the GPT recovery flow (when implemented) reads from the appropriate directory depending on which phase is feeding it.

Material in `source_intake_gpt_recovery/` is not rejected in the sense of "not useful." It is material that carries potential value but could not be completed through the automated flow because required schema fields were unfillable from the source alone. The GPT recovery flow will investigate the source further (or related sources) to recover the missing information and produce a valid packet.

## Closed vocabulary

### Manifest status values

| Value | Meaning |
|---|---|
| `pending` | Manifest exists but processing has not started |
| `in_progress` | Skeletons are being processed |
| `complete` | All skeletons processed, routed to either `packets/` or `source_intake_gpt_recovery/` |
| `failed` | Unrecoverable error stopped the run |
| `blocked_by_stage_1_incomplete` | Stage 1 manifest is not `complete`; stage 2 cannot proceed |

### Issue types

| Value | When it applies |
|---|---|
| `skeleton_invalid` | A skeleton file from stage 1 does not have the expected structure or is missing required mechanical fields |
| `template_case_uncovered` | The case falls outside anything the conversion template addresses, and no fallback applies |
| `needs_human_review` | Packet passed validation but has 4+ uncertainties or one high-severity uncertainty; flagged for operator review |
| `schema_validation_failed` | Completed packet does not validate against `source_packet.schema.json`; routed to `source_intake_gpt_recovery/` |
| `required_field_unfillable` | A required field of the schema cannot be filled from the material available; routed to `source_intake_gpt_recovery/` |
| `multiple_required_fields_unfillable` | Two or more required fields cannot be filled; routed to `source_intake_gpt_recovery/` (more severe than single-field case) |

This enum is closed. New issue types must be added here and to the manifest schema before the skill can register them.

### Destination values

A packet always lands in exactly one of these destinations:

| Value | Meaning |
|---|---|
| `packets` | Complete, schema-validated packet written to `working/source_intake/packets/` |
| `source_intake_gpt_recovery` | Packet could not be completed automatically, staged for GPT recovery in `working/source_intake/source_intake_gpt_recovery/` |

## Operations

Operations run sequentially. Each skeleton is a unit of work; checkpoints happen after each skeleton completes (success or routing to GPT recovery), not per batch. This is the checkpoint granularity that matches the cost of LLM work per skeleton.

### 1. Precondition checks

- Read `working/source_intake/converter_prepare_manifest.json`. If it does not exist or `status != complete`, set stage 2 manifest status to `blocked_by_stage_1_incomplete` and exit with a clear message. Do not process anything.
- Read `upstream/source-intake/reference/source_packet_conversion_template.md` in full. If missing, fail with clear message.
- Read `upstream/source-intake/schemas/source_packet.schema.json`. If missing, fail with clear message.
- Create output directories if they do not exist: `working/source_intake/packets/`, `working/source_intake/source_intake_gpt_recovery/`.

### 2. Load or initialize stage 2 manifest

- If `working/source_intake/converter_manifest.json` exists and `status == complete`, exit cleanly with a "nothing to do" message.
- If it exists and `status == in_progress`, read it to determine which skeletons have already been processed. Processing will resume from the next unprocessed skeleton.
- If it does not exist, initialize with `status: pending`, empty counters, and empty issues array.

### 3. Enumerate skeletons to process

- Walk `working/source_intake/skeleton_batches/batch_NNN/` in batch numeric order.
- Within each batch, process skeletons in alphabetical order by filename (deterministic ordering).
- Skip any skeleton whose `packet_id` is already in the manifest's `processed_skeletons` list.

### 4. Process each skeleton

For each unprocessed skeleton:

**4.1 Read and validate skeleton structure.** If the skeleton is missing any of the 11 mechanical fields, or the JSON cannot be parsed, register a `skeleton_invalid` issue and continue to the next skeleton. Do not produce any output for this skeleton.

**4.2 Detect stage 1 inherited marks.** If `intake_notes` contains the Part 2 inheritance marker (written by stage 1 when a skeleton derives from Part 2 provisional findings with verification_status blocked_url_index_verified; findings with indirect_verified from the recovery agent do not carry this marker), apply the three consequences:
- Set `traceability_status` to `weak` (overriding the template heuristic for this case)
- Add `snippet_needs_reopen` to the `uncertainties` array as a starting entry
- Record internally that `priority_for_source_first` has a ceiling of `medium` and cannot be `high` regardless of other factors

**4.3 Apply conversion template to judgment fields.** Fill the 8 judgment fields in the order they appear in the conversion template. For each field:

- If the template gives clear instruction and the material supports the decision, fill the field as instructed.
- If there is genuine ambiguity between two or more plausible values, pick the most conservative and add the corresponding code to `uncertainties` from the closed enum in the schema.
- If the case is not covered by the template at all, look for a fallback rule in the template's "Fallback rules" section. Apply the fallback if one exists.
- If no fallback applies either, register a `template_case_uncovered` issue with specific detail about which field and which case, fill the field with the most conservative possible value or `unknown` if the enum allows it, and continue.

**4.4 Check uncertainty severity.** After all 8 judgment fields are filled, count the uncertainties in the packet. If the count is 4 or more, or if any single uncertainty is high-severity (definition of "high-severity" lives in the conversion template), add `needs_human_review` to the issues for this packet. The packet still proceeds to validation.

**4.5 Validate completed packet against schema.** Run the packet through `upstream/source-intake/schemas/source_packet.schema.json`.

- If validation passes: write the packet to `working/source_intake/packets/<packet_id>.json`. Destination is `packets`.
- If validation fails because a required field is null or missing: determine which field(s). If exactly one required field is unfillable, register `required_field_unfillable` and route to GPT recovery. If two or more required fields are unfillable, register `multiple_required_fields_unfillable` and route to GPT recovery.
- If validation fails for any other schema reason (type mismatch, enum violation, pattern mismatch), register `schema_validation_failed` with the specific validation error and route to GPT recovery.

**4.6 Write to destination.** 

- For `packets` destination: write the complete packet JSON to `working/source_intake/packets/<packet_id>.json`.
- For `source_intake_gpt_recovery` destination: write a recovery-ready JSON to `working/source_intake/source_intake_gpt_recovery/<packet_id>.json` using the structure defined in "GPT recovery staging" below.

**4.7 Update manifest.** After the packet is written, append the packet_id to the manifest's `processed_skeletons` list with its destination and any issue types registered. Update counters. Save the manifest to disk.

This update happens after every skeleton, not every batch. If the process is interrupted, resumption starts from the next unprocessed skeleton with zero work lost.

### 5. Completion

When all skeletons across all batches have been processed, set manifest status to `complete`, record `completed_at` timestamp, and exit.

## GPT recovery staging

Packets routed to `source_intake_gpt_recovery/` are not raw packets. They are staged with the structure the GPT recovery flow needs as input when it is eventually implemented. This avoids having to reprocess the original skeleton later.

Each file in `source_intake_gpt_recovery/` contains:

```json
{
  "packet_id": "SP-<shard_id>-<NNN>",
  "recovery_type": "source_intake_schema_incomplete",
  "origin_stage": "source_intake_stage_2",
  "original_skeleton": { ... the stage 1 skeleton as read ... },
  "partial_packet": { ... the packet as far as stage 2 could complete it ... },
  "failure_detail": {
    "issue_type": "schema_validation_failed | required_field_unfillable | multiple_required_fields_unfillable",
    "missing_required_fields": [ "field_name_1", "field_name_2" ],
    "validation_error": "specific error message from schema validation, if applicable",
    "template_notes": "any notes the skill recorded about what the template could not resolve"
  },
  "recovery_guidance": {
    "suggested_direction": "what the GPT should investigate to recover the missing information",
    "source_ref": "the URL or source identifier from the original packet",
    "source_type": "so GPT knows what kind of source to approach"
  },
  "staged_at": "<iso timestamp>"
}
```

The `recovery_type: source_intake_schema_incomplete` is a new value that extends the types defined in D-108 (`access_retry` and `scope_exploration`). This extension should be registered as a decision in the decision log when the session closes.

The `recovery_guidance` section is the skill's best effort to tell GPT what to look for. The skill produces it based on what the template and the skeleton indicate is missing. The GPT recovery flow (when implemented) consumes this guidance; if the guidance is insufficient, the operator can enrich it manually before handing the packet to the GPT.

## Promotion criteria

A packet is promoted to `working/source_intake/packets/` if and only if:

1. It validates against `upstream/source-intake/schemas/source_packet.schema.json`
2. No required field is null or missing
3. The skeleton structure was valid (it did not fail at step 4.1)

A packet is routed to `working/source_intake/source_intake_gpt_recovery/` if:

1. It failed schema validation for any reason AND
2. The skeleton structure was valid (otherwise it does not produce any output at all; it only produces a `skeleton_invalid` issue)

A packet can be in `packets/` and simultaneously flagged `needs_human_review` in the manifest. These are valid packets that need operator attention, not failed packets. They are consumed downstream normally; the flag exists so the operator can prioritize review.

## Fail states

| Situation | Behavior |
|---|---|
| Stage 1 manifest missing or not complete | Set status `blocked_by_stage_1_incomplete`, exit |
| Conversion template missing | Fatal error, exit with clear message |
| Source Packet schema missing | Fatal error, exit with clear message |
| Skeleton directory empty | Fatal error, exit with clear message |
| Individual skeleton unreadable or malformed | Register `skeleton_invalid`, continue with next |
| I/O error writing a packet or recovery file | Register issue with detail, continue with next skeleton |
| Schema file unreadable | Fatal error, exit |

Only three situations are fatal: missing stage 1 completion, missing template or schema files, and empty skeleton directory. Everything else is a per-skeleton issue that does not stop the run.

## Resumability

Checkpoint granularity is per skeleton, not per batch.

On startup:

1. Read the stage 2 manifest.
2. If `status == complete`: exit cleanly.
3. If `status == in_progress`: read the `processed_skeletons` list. Skip any skeleton in that list during enumeration. Resume from the first unprocessed skeleton.
4. If `status == blocked_by_stage_1_incomplete`: re-verify stage 1. If stage 1 is now `complete`, reset stage 2 status to `in_progress` and proceed. If stage 1 is still not complete, exit with message.
5. If `status == failed`: do not auto-resume. Operator must inspect the manifest, resolve the failure cause, and manually reset the status before re-running.
6. If manifest does not exist: create with `status: in_progress`, empty processed list, and proceed.

## Skill that executes this module

`.claude/skills/convert-findings/SKILL.md` (to be designed after this module).

---

## Notes on naming

The directory `source_intake_gpt_recovery/` is an operational name, not a quality judgment. The material it contains is not rejected in the sense of being worthless. It is material that the automated flow could not complete because required schema fields were unfillable from the source as parsed. The GPT recovery flow exists specifically to investigate such material further and recover what is needed for it to fulfill the schema.

The naming parallels the existing `working/data_gathering/phase0_part4_gpt_recovery/` (from D-108). Each phase that produces recovery candidates has its own recovery directory, using the pattern `<phase>_gpt_recovery/`. This allows the GPT recovery flow (when implemented) to know which phase a given recovery candidate originated from, and apply the appropriate recovery logic for that phase.
