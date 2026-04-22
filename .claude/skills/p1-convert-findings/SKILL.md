# Convert Findings — Skill

Executes Module — Converter (Source Intake stage 2). Reads skeleton files produced by stage 1 and fills the 8 judgment fields to produce complete, validated Source Packets. Routes failures to GPT recovery staging without discarding them.

## Module this skill executes

Read `phases/01-source-intake/modules/converter.md` in full before processing anything. The module is the contract. This skill is the execution instruction layered on top.

## Mandatory reading before any skeleton is processed

Before touching any skeleton file, load these into context and keep them available throughout the run:

1. `phases/01-source-intake/modules/converter.md` — the module contract
2. `phases/01-source-intake/reference/source_packet_conversion_template.md` — the conversion guide, including the field-by-field guidance, fallback rules, and the DX-2 workflow sidebar
3. `phases/01-source-intake/schemas/source_packet.schema.json` — the target schema with closed enums
4. `phases/01-source-intake/schemas/converter_manifest.schema.json` — the manifest schema this skill writes to

If any of these files cannot be read, stop immediately and report which file is missing. Do not attempt to proceed from memory.

## Core loop

Process skeletons one at a time, in deterministic order, with checkpoint after each one.

For each skeleton:

1. **Read the skeleton file** from `working/source_intake/skeleton_batches/batch_NNN/`.
2. **Validate structure**: verify all 11 mechanical fields are present and populated. If any is missing, register `skeleton_invalid` in `skeleton_failures` of the manifest and move to the next skeleton. Do not produce any output for this one.
3. **Check for Part 2 inheritance**: scan `intake_notes` for the Part 2 marker left by stage 1. If present, apply the three consequences immediately and record them internally:
   - `traceability_status` will be set to `weak` (overriding the template heuristic for this case; stage 1 only emits this marker for findings with verification_status blocked_url_index_verified, so findings with indirect_verified from the recovery agent follow the template's normal mapping)
   - `snippet_needs_reopen` will be added to the `uncertainties` array as a starting entry
   - `priority_for_source_first` has a ceiling of `medium` and cannot be `high`
4. **Fill the 8 judgment fields** following the conversion template, in the order the template lists them: possible_subjects, possible_actor_levels, possible_metric_types, possible_time_scopes, possible_geographies, uncertainties, priority_for_source_first, traceability_status.
5. **Apply uncertainty counting**: after all 8 fields are filled, count the entries in `uncertainties`. If the count is 4 or more, add `needs_human_review` to the issues for this packet.
6. **Validate against schema**: check the complete packet against `source_packet.schema.json`.
7. **Route to destination**:
   - If validation passes and no `required_field_unfillable` occurred: write to `working/source_intake/packets/<packet_id>.json`, destination `packets`
   - If validation fails or a required field was unfillable: write to `working/source_intake/source_intake_gpt_recovery/<packet_id>.json` using the recovery format (see below), destination `source_intake_gpt_recovery`
8. **Update manifest**: append an entry to `processed_skeletons` with `packet_id`, `destination`, `issues_for_this_packet`, and `processed_at` timestamp. Save the manifest to disk immediately. Do not batch manifest writes.
9. **Move to the next skeleton.**

## Filling judgment fields — strict rules

**Rule 1: The template is the only authority.** For each of the 8 judgment fields, consult the corresponding section of `phases/01-source-intake/reference/source_packet_conversion_template.md` before deciding. If the template gives a clear instruction that applies, follow it. Do not substitute your own reasoning for what the template says.

**Rule 2: Closed enums are closed.** Fields with enum values (`possible_actor_levels`, `possible_metric_types`, `uncertainties`, `priority_for_source_first`, `traceability_status`) may only contain values from the enum in `source_packet.schema.json`. If no value fits, use `unknown` if the enum allows it, or mark the field as unfillable and route to recovery. Never invent enum values.

**Rule 3: Ambiguity goes to uncertainties, not to invention.** If two template-valid values are equally plausible for a field, pick the more conservative one and add the corresponding uncertainty code from the enum. Do not pick one and hide the ambiguity. Do not invent a third option to avoid choosing.

**Rule 4: Missing material is not filled in.** If the material in the skeleton does not support a required field, do not guess. Mark `required_field_unfillable` and route the packet to recovery. The recovery flow exists specifically for this case.

**Rule 5: Cases the template does not cover.** Look for a fallback rule in the template's "Fallback rules" section before giving up. If no fallback applies either, register `template_case_uncovered` with specific detail about which field and which case, fill the field with the most conservative possible value (or `unknown` if the enum allows it), and continue. Do not stop the run.

## Recovery file format

When a packet is routed to `source_intake_gpt_recovery/`, the file is not a raw partial packet. It is staged with the structure the GPT recovery flow will consume:

```json
{
  "packet_id": "SP-<shard_id>-<NNN>",
  "recovery_type": "source_intake_schema_incomplete",
  "origin_stage": "source_intake_stage_2",
  "original_skeleton": { ... exact contents of the skeleton file as read ... },
  "partial_packet": { ... the packet as far as it could be completed ... },
  "failure_detail": {
    "issue_type": "schema_validation_failed | required_field_unfillable | multiple_required_fields_unfillable",
    "missing_required_fields": [ "field_name_1", "field_name_2" ],
    "validation_error": "specific schema validation error message if applicable, otherwise null",
    "template_notes": "what the template could not resolve, in plain language"
  },
  "recovery_guidance": {
    "suggested_direction": "what GPT should investigate to recover the missing information",
    "source_ref": "the URL from the original skeleton",
    "source_type": "the source_type from the original skeleton"
  },
  "staged_at": "<ISO 8601 timestamp>"
}
```

The `recovery_guidance.suggested_direction` is your best effort to describe what GPT should look for. Be concrete: "Investigate the pricing page to recover fee_rate values for the subscription tier" is good. "Find more information" is not acceptable.

## Resumability

At startup, read `working/source_intake/converter_manifest.json`:

- If `status == complete`: exit cleanly, do nothing.
- If `status == in_progress`: read `processed_skeletons`. Skip any skeleton whose `packet_id` is already in that list. Resume from the next unprocessed skeleton.
- If `status == blocked_by_stage_1_incomplete`: re-check `working/source_intake/converter_prepare_manifest.json`. If stage 1 is now `complete`, set stage 2 status to `in_progress` and proceed. Otherwise exit with message.
- If `status == failed`: do not auto-resume. Exit with message asking operator to inspect.
- If manifest does not exist: initialize with `status: in_progress`, empty arrays, and proceed.

## Prohibitions

- Do not modify the 11 mechanical fields of any skeleton. They were filled by stage 1 and must pass through unchanged.
- Do not process skeletons in parallel. The manifest checkpoint assumes sequential processing.
- Do not batch manifest writes. Save the manifest after every skeleton completes, before moving to the next.
- Do not skip validation. Every packet routed to `packets/` must have been validated against `source_packet.schema.json`. Every packet routed to `source_intake_gpt_recovery/` must have failed validation with a specific recorded reason.
- Do not invent field values. If the template does not tell you what to put, the material does not support a value, and no fallback applies, route to recovery.
- Do not silently swallow template gaps. Every case the template does not cover must be registered as `template_case_uncovered` in the manifest so the operator can improve the template later.
- Do not remove `needs_human_review` entries from the manifest after the fact. Once flagged, it stays flagged even if the packet was written successfully. The flag is for operator priority, not for the skill to resolve.
- Do not modify the stage 1 manifest or stage 1 output files under any circumstance. They are upstream and immutable from this skill's perspective.

## Completion

When all skeletons across all batches have been processed (no unprocessed skeletons remain), set `status` to `complete`, record `completed_at` with the current ISO 8601 timestamp, save the manifest one final time, and exit.

Report at the end:
- Total skeletons processed
- Packets written to `packets/`
- Packets staged to `source_intake_gpt_recovery/`
- Packets flagged `needs_human_review`
- Skeleton failures (structural)
- Any `template_case_uncovered` issues registered

This is the telemetry the operator needs to decide whether the Converter is working well or whether the template, the stage 1 output, or the schema need adjustment.
