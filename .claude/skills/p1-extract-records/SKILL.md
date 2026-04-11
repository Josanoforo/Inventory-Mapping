# Extract Records — Skill

Executes Module — Extraction Converter (Data Extraction stage 2). Reads skeleton files produced by stage 1 and fills the 15 judgment fields to produce complete, validated Extraction Records. Routes failures to GPT recovery staging without discarding them.

## Module this skill executes

Read `upstream/data-extraction/modules/extraction_converter.md` in full before processing anything. The module is the contract. This skill is the execution instruction layered on top.

## Mandatory reading before any skeleton is processed

Before touching any skeleton file, load these into context and keep them available throughout the run:

1. `upstream/data-extraction/modules/extraction_converter.md` — the module contract
2. `upstream/data-extraction/contracts/data_extraction_contract.md` — the extraction guide, including field definitions, quality rules, and failure taxonomy
3. `upstream/data-extraction/schemas/data_extraction_record.schema.json` — the target schema with closed enums
4. `upstream/data-extraction/schemas/extraction_converter_manifest.schema.json` — the manifest schema this skill writes to

If any of these files cannot be read, stop immediately and report which file is missing. Do not attempt to proceed from memory.

## Core loop

Process skeletons one at a time, in deterministic order, with checkpoint after each one.

For each skeleton:

1. **Read the skeleton file** from `working/data_extraction/skeleton_batches/batch_NNN/`.
2. **Validate structure**: verify all 10 mechanical fields are present. The required mechanical fields are: `extraction_id`, `source_packet_id`, `source_id`, `source_type`, `source_title`, `source_ref`, `snippet_primary`, `snippet_context_before`, `snippet_context_after`, `traceability_pointer`. Note that `source_date_if_available`, `author_or_actor_if_available`, `snippet_context_before`, and `snippet_context_after` may be null — null is valid for those fields. If any required mechanical field is absent entirely, register `skeleton_invalid` in the manifest and move to the next skeleton. Do not produce any output for this one.
3. **Fill the 15 judgment fields** following the extraction contract, in this order:
   - `claim_type`
   - `subject_exact`
   - `actor_level`
   - `platforms`
   - `product_type_if_explicit`
   - `metric_type`
   - `metric_value_raw`
   - `metric_unit`
   - `time_scope_raw`
   - `time_scope_normalized_if_safe`
   - `geography_if_explicit`
   - `evidence_role`
   - `local_qualifiers`
   - `uncertainties`
   - `parser_notes`
4. **Apply uncertainty counting**: after all 15 fields are filled, count the entries in `uncertainties`. If the count is 4 or more, add `needs_human_review` to the issues for this record.
5. **Validate against schema**: check the complete record against `data_extraction_record.schema.json`.
6. **Route to destination**:
   - If validation passes and no `required_field_unfillable` occurred: write to `working/data_extraction/records/<extraction_id>.json`, destination `records`
   - If validation fails or a required field was unfillable: write to `working/data_extraction/extraction_gpt_recovery/<extraction_id>.json` using the recovery format (see below), destination `extraction_gpt_recovery`
7. **Update manifest**: append an entry to `processed_skeletons` with `extraction_id`, `destination`, `issues_for_this_record`, and `processed_at` timestamp. Save the manifest to disk immediately. Do not batch manifest writes.
8. **Move to the next skeleton.**

## Filling judgment fields — strict rules

**Rule 1: The contract is the only authority.** For each of the 15 judgment fields, consult the corresponding section of `upstream/data-extraction/contracts/data_extraction_contract.md` before deciding. If the contract gives clear instruction that applies, follow it. Do not substitute your own reasoning for what the contract says.

**Rule 2: Closed enums are closed.** Fields with enum values (`claim_type`, `actor_level`, `product_type_if_explicit`, `metric_type`, `evidence_role`, `uncertainties`) may only contain values from the enums in `data_extraction_record.schema.json`. If no value fits, use `unknown` if the enum allows it, or mark the field as unfillable and route to recovery. Never invent enum values.

**Rule 3: Ambiguity goes to uncertainties, not to invention.** If two contract-valid values are equally plausible for a field, pick the more conservative one and add the corresponding uncertainty code from the enum. Do not pick one and hide the ambiguity. Do not invent a third option to avoid choosing.

**Rule 4: Missing material is not filled in.** If the material in the skeleton does not support a required judgment field, do not guess. Mark `required_field_unfillable` and route the record to recovery. The recovery flow exists specifically for this case.

**Rule 5: Cases the contract does not cover.** Look for a fallback in the contract's "Failure Reasons" section (§12) and "Quality Rules" section (§10) before giving up. If no fallback applies, register `contract_case_uncovered` with specific detail about which field and which case, fill the field with the most conservative possible value (or `unknown` if the enum allows it), and continue. Do not stop the run.

**Rule 6: Do not rewrite the snippet.** `snippet_primary` is a mechanical field. Its value comes from the skeleton unchanged. Do not alter it while filling judgment fields.

**Rule 7: Do not collapse functional layers.** The extraction contract (§10, Rule 1) prohibits collapsing: checkout ≠ payout, fee base ≠ net retained, active buyers ≠ seller discoverability. When a snippet touches multiple layers, name the layer precisely in `subject_exact` and mark `subject_ambiguity` in uncertainties if the snippet conflates them.

**Rule 8: Preserve qualifiers.** Any temporal, geographic, or conditional qualifier from the snippet must appear in `local_qualifiers` verbatim. Do not drop them for brevity.

## Recovery file format

When a record is routed to `extraction_gpt_recovery/`, the file is not a raw partial record. It is staged with the structure the GPT recovery flow will consume:

```json
{
  "extraction_id": "ER-<packet_id>-<snippet_id>",
  "recovery_type": "data_extraction_schema_incomplete",
  "origin_stage": "data_extraction_stage_2",
  "original_skeleton": { "...exact contents of the skeleton file as read..." },
  "partial_record": { "...the record as far as it could be completed..." },
  "failure_detail": {
    "issue_type": "schema_validation_failed | required_field_unfillable | multiple_required_fields_unfillable",
    "missing_required_fields": ["field_name_1", "field_name_2"],
    "validation_error": "specific schema validation error message if applicable, otherwise null",
    "contract_notes": "what the contract could not resolve, in plain language"
  },
  "recovery_guidance": {
    "suggested_direction": "what GPT should investigate to recover the missing information",
    "source_ref": "the source_ref from the original skeleton",
    "source_type": "the source_type from the original skeleton",
    "source_packet_id": "the source_packet_id to trace back to the originating packet"
  },
  "staged_at": "<ISO 8601 timestamp>"
}
```

The `recovery_guidance.suggested_direction` is your best effort to describe what GPT should look for. Be concrete: "Re-open the pricing page at source_ref to determine whether the fee rate applies to checkout or payout in the Gumroad context" is good. "Find more information" is not acceptable.

## Resumability

At startup, read `working/data_extraction/extraction_converter_manifest.json`:

- If `status == complete`: exit cleanly, do nothing.
- If `status == in_progress`: read `processed_skeletons`. Skip any skeleton whose `extraction_id` is already in that list. Resume from the next unprocessed skeleton.
- If `status == blocked_by_stage_1_incomplete`: re-check `working/data_extraction/extraction_prepare_manifest.json`. If stage 1 is now `complete`, set stage 2 status to `in_progress` and proceed. Otherwise exit with message.
- If `status == failed`: do not auto-resume. Exit with message asking operator to inspect.
- If manifest does not exist: initialize with `status: in_progress`, empty arrays, and proceed.

## Prohibitions

- Do not modify the 10 mechanical fields of any skeleton. They were filled by stage 1 and must pass through unchanged.
- Do not process skeletons in parallel. The manifest checkpoint assumes sequential processing.
- Do not batch manifest writes. Save the manifest after every skeleton completes, before moving to the next.
- Do not skip validation. Every record routed to `records/` must have been validated against `data_extraction_record.schema.json`. Every record routed to `extraction_gpt_recovery/` must have failed validation with a specific recorded reason.
- Do not invent field values. If the contract does not tell you what to put, the material does not support a value, and no fallback applies, route to recovery.
- Do not silently swallow contract gaps. Every case the contract does not cover must be registered as `contract_case_uncovered` in the manifest so the operator can improve the contract later.
- Do not remove `needs_human_review` entries from the manifest after the fact. Once flagged, it stays flagged even if the record was written successfully. The flag is for operator priority, not for the skill to resolve.
- Do not modify the stage 1 manifest or stage 1 skeleton files under any circumstance. They are upstream and immutable from this skill's perspective.
- Do not merge snippets. Each skeleton represents exactly one snippet. The `subject_exact` field must describe the claim of that specific snippet, not a synthesis across snippets.

## Completion

When all skeletons across all batches have been processed (no unprocessed skeletons remain), set `status` to `complete`, record `completed_at` with the current ISO 8601 timestamp, save the manifest one final time, and exit.

Report at the end:
- Total skeletons processed
- Records written to `records/`
- Records staged to `extraction_gpt_recovery/`
- Records flagged `needs_human_review`
- Skeleton failures (structural)
- Any `contract_case_uncovered` issues registered

This is the telemetry the operator needs to decide whether the Extraction Converter is working well or whether the contract, the stage 1 output, or the schema need adjustment.
