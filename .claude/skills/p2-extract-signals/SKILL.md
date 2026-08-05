# Extract Signals — Skill

> Serie de reglas: PES (D-257). Cita canónica: PES-RN.

Executes Module — Signal Converter (Signal Extraction stage 2). Reads skeleton files produced by stage 1, formulates observational signal_text, and fills the 16 judgment fields to produce complete, validated Signal Cards. Handles splitting when a skeleton contains multiple discrete claims. Routes failures to GPT recovery staging without discarding them.

## Module this skill executes

Read `phases/02-signal-extraction/modules/signal_converter.md` in full before processing anything. The module is the contract. This skill is the execution instruction layered on top.

## Mandatory reading before any skeleton is processed

Before touching any skeleton file, load these into context and keep them available throughout the run:

1. `phases/02-signal-extraction/modules/signal_converter.md` — the module contract
2. `phases/02-signal-extraction/contracts/signal_extraction_contract.md` — the extraction guide: Signal Card principles, what can/cannot be fused, decision boundary, quality rules
3. `phases/02-signal-extraction/contracts/signal_extraction_validator.md` — all 11 validator checks, decision rules, failure severity guide, and the mandatory notes scrubbing step
4. `phases/02-signal-extraction/schemas/signal_card.schema.json` — the target schema with closed enums and signal_id pattern
5. `phases/02-signal-extraction/schemas/signal_converter_manifest.schema.json` — the manifest schema this skill writes to

If any of these files cannot be read, stop immediately and report which file is missing. Do not attempt to proceed from memory.

## Core loop

Process skeletons one at a time, in deterministic order, with checkpoint after each skeleton (including all cards produced from it, if splitting).

For each skeleton:

1. **Read the skeleton file** from `working/signal_extraction/skeleton_batches/batch_NNN/`.
2. **Validate structure**: verify that all required mechanical fields are present and structurally valid:
   - `signal_id` — string matching `^SC-R\d+-\d+$`
   - `source_record_ids` — non-empty array of strings
   - `source_ids` — non-empty array of strings
   - `round` — positive integer
   - `traceability_pointers` — non-empty array
   - `_extraction_context` — object with `snippet_primary` as a non-null, non-empty string
   If any required field is absent or invalid, register `skeleton_invalid` and move to the next skeleton. Do not produce any output for this one.
3. **Assess signal threshold**: decide whether the content of `_extraction_context.snippet_primary` reaches the observational threshold (contract §9). If it falls into §9D (no discrete claim), register `below_signal_threshold` with a specific note about why, and continue without writing any file.
4. **Assess splitting need**: before formulating any card, determine whether the extraction context contains multiple discrete claims that the contract (§10) permits splitting into separate Signal Cards. Apply the splitting rules strictly — split only when clearly warranted; otherwise express as one card.
5. **Allocate additional signal_ids if splitting**: for each additional card beyond the first, increment `next_signal_id_counter` in the manifest immediately and use the resulting ID for that card. Save the manifest after each counter increment (before formulating that card) so IDs are never re-used on resumption.
6. **Formulate signal_text and fill judgment fields** for each card following the module's field-filling order (§4.4). Read the corresponding `_extraction_context` field first, then decide whether to inherit or adjust. When inheriting, pass the value through unchanged. When adjusting, record the reason in `normalization_notes`.
7. **Apply validator checks** (all 11 from signal_extraction_validator.md). If check 11 (Notes Locality) triggers, apply the mandatory scrubbing step before routing. Record all flag codes and failure codes in issues.
8. **Check uncertainty count**: if 4 or more entries in `uncertainties`, add `needs_human_review`.
9. **Validate against schema**: check the completed card against `signal_card.schema.json`.
10. **Route to destination**:
    - `pass` or `pass_with_flags` from validator AND schema passes → write to `working/signal_extraction/cards/<signal_id>.json`, destination `cards`
    - `rework` or `reject` from validator → write to `working/signal_extraction/signal_gpt_recovery/<signal_id>.json`, destination `signal_gpt_recovery`
    - Schema validation fails → write to `working/signal_extraction/signal_gpt_recovery/<signal_id>.json`, destination `signal_gpt_recovery`
11. **Update manifest**: append one entry to `processed_skeletons` with `skeleton_signal_id`, `cards_produced` (one entry per card produced), `issues_for_this_skeleton`, and `processed_at`. Update all counters. Save the manifest to disk immediately. Do not batch manifest writes.
12. **Move to the next skeleton.**

## Formulating signal_text — strict rules

**PES-R1 (Rule 1): Signal text must be observational, not interpretive.** Write what was observed or stated locally. Do not write what it means, implies, reveals, or confirms. Re-read contract §7 (Principles) and §13 (Quality Rules) before drafting signal_text for each card.

**PES-R2 (Rule 2): Derive from the snippet, not from inference.** `signal_text` must be directly supportable from `_extraction_context.snippet_primary` (with `snippet_context_before`/`snippet_context_after` as supporting context). If the signal requires bridging to other sources or inferring unstated facts, it is not a valid signal — route to recovery with rework guidance.

**PES-R3 (Rule 3): Avoid red-flag wording.** The validator will reject any signal_text containing: reveals, demonstrates, suggests that, confirms that, implies that, shows a tension, indicates a market need, many sellers report, the corpus shows, platforms split into, sources converge. Check for these before committing the text.

**PES-R4 (Rule 4): Preserve the fact, not resolve it.** If the source is ambiguous about what it means, signal_text preserves the ambiguity. "The policy states X as a requirement but does not specify what happens if not met" is better than "The platform requires X" when the consequence is unclear.

**PES-R5 (Rule 5): One signal = one local observation.** If two claims are present, decide to split (per §10) or express the primary claim and mark the secondary as `local_context`. Do not average or blend two claims into one signal.

## Filling judgment fields — strict rules

**PES-R6 (Rule 6): Inheritance is the default.** For fields 2–16 (everything except `signal_text`), inheritance from `_extraction_context` is the default. The extraction record already completed a judgment pass; Signal Extraction should not casually override it.

Exception: `actor_level` (field 3). Per D-264, `signal_converter.md` §4.4 field 3 is the assignment rule for `actor_level`, not a fallback — see that table for the authoritative rule. Inheritance only applies there when no row of the table applies, and in that case the inherited value is itself the decision the table produces, not a default this rule is supplying.

**PES-R7 (Rule 7): Override only when signal formulation requires it.** The only valid reason to change an inherited value is if the signal_text formulation reveals that the extraction record's value was imprecise for the specific claim now being expressed. Record the override reason in `normalization_notes`.

Exception: `actor_level` (field 3). Applying the assignment table in `signal_converter.md` §4.4 field 3 is not an override under this rule, even when it changes the inherited value — under D-264 the table is the rule being applied, not a deviation from one. This rule's "override only when..." condition governs fields 2 and 4–16.

**PES-R8 (Rule 8): Closed enums are closed.** `actor_level`, `product_type_if_explicit`, `metric_type`, `evidence_role`, `uncertainties` may only contain values from the enums in `signal_card.schema.json`. If no value fits, use `unknown` if the enum allows it. Never invent enum values.

**PES-R9 (Rule 9): Ambiguity goes to uncertainties, not to invention.** Two equally plausible enum values → pick the more conservative + add the corresponding uncertainty code. Do not hide ambiguity.

**PES-R10 (Rule 10): Never drop qualifiers.** See `phases/02-signal-extraction/modules/signal_converter.md` §4.4, field `local_qualifiers`, for the authoritative rule. If a qualifier is dropped, the validator (check 5) will catch it.

**PES-R11 (Rule 11): Notes locality is mandatory.** `normalization_notes` and `extraction_notes` must not contain: references to other records by ID pattern, cross-source comparison language (confirmed by, consistent with, contradicted by, corroborated by), version comparison language, or interpretive math. If you notice you've written any of these, remove them before the validator runs. The validator's check 11 will apply mandatory scrubbing if they slip through, but clean notes at write-time are preferable.

## Recovery file format

When a card is routed to `signal_gpt_recovery/`, write the recovery file in this structure:

```json
{
  "signal_id": "SC-R{round}-{NNN}",
  "recovery_type": "signal_extraction_incomplete",
  "origin_stage": "signal_extraction_stage_2",
  "original_skeleton": { "...exact contents of the skeleton file as read..." },
  "partial_card": { "...the card as far as stage 2 could complete it..." },
  "failure_detail": {
    "issue_type": "schema_validation_failed | required_field_unfillable | multiple_required_fields_unfillable | rework | reject",
    "missing_required_fields": ["field_name_1"],
    "validation_error": "specific schema validation error message if applicable, otherwise null",
    "validator_failures": ["failure_code_1", "failure_code_2"],
    "contract_notes": "what the contract or validator could not resolve, in plain language"
  },
  "recovery_guidance": {
    "suggested_direction": "what GPT should do to recover or repair this card",
    "source_ref": "the source_ref from _extraction_context",
    "source_type": "the source_type from _extraction_context",
    "source_record_id": "the extraction_id from _extraction_context"
  },
  "staged_at": "<ISO 8601 timestamp>"
}
```

`recovery_guidance.suggested_direction` must be concrete and local:
- For rework: "Narrow signal_text to one local observation; remove the interpretive conclusion and restore the verbatim claim from the snippet."
- For missing `subject_exact`: "Re-open source at [source_ref] to determine the precise subject of the fee calculation claim."
- For `below_signal_threshold` (note: these are not written to recovery, but if rework is needed): explain specifically what makes the snippet insufficient.

## Resumability

At startup, read `working/signal_extraction/signal_converter_manifest.json`:

- If `status == complete`: exit cleanly, do nothing. If a new run is intended (e.g. stage 1 produced additional skeletons), archive this manifest first — copy it, unmodified, to `working/signal_extraction/signal_converter_manifest.<archived_at>.json` (`<archived_at>` = ISO 8601 UTC timestamp of the archive action, `:` replaced by `-`) — then initialize a fresh manifest as in the "manifest does not exist" case below. Never delete or overwrite a `complete` manifest without archiving it first.
- If `status == in_progress`: read `processed_skeletons` (use `skeleton_signal_id` to identify processed entries) and restore `next_signal_id_counter`. Skip skeletons already in `processed_skeletons`. Resume from the next unprocessed skeleton with the saved counter.
- If `status == blocked_by_stage_1_incomplete`: re-check `working/signal_extraction/signal_prepare_manifest.json`. If stage 1 is now `complete`, reset status to `in_progress` and proceed. Otherwise exit with message.
- If `status == failed`: do not auto-resume. Exit with message asking operator to inspect.
- If manifest does not exist: read `signal_id_counter_at_stage1` from stage 1 manifest; initialize with `status: in_progress`, `next_signal_id_counter` set to that value, empty arrays, and proceed.

## Prohibitions

- Do not modify the mechanical fields of any skeleton (`signal_id`, `source_record_ids`, `source_ids`, `round`, `traceability_pointers`). Exception: splitting allocates new `signal_id` values for additional cards, but does not modify the original skeleton file.
- Do not modify the stage 1 skeleton files or stage 1 manifest under any circumstance. They are upstream and immutable.
- Do not process skeletons in parallel. The manifest checkpoint (including `next_signal_id_counter`) assumes sequential processing.
- Do not batch manifest writes. Save the manifest after every skeleton completes (all its cards), before moving to the next.
- Do not skip validation. Every card written to `cards/` must have passed validator checks and schema validation. Every card written to `signal_gpt_recovery/` must have failed with a specific recorded reason.
- Do not invent field values. If the contract does not tell you what to put, the material does not support a value, and no fallback applies, route to recovery.
- Do not silently swallow contract gaps. Every case the contract does not cover must be registered as `contract_case_uncovered` in the manifest with specific field and case detail.
- Do not remove `needs_human_review` once set. It is for operator priority, not for the skill to resolve.
- Do not merge extraction records. Each skeleton is one Extraction Record. `source_record_ids` may contain multiple IDs only if stage 1 produced a skeleton with multiple records — which it does not in the current design (1:1 mapping). Do not manually add additional `source_record_ids` from other skeletons.
- Do not write signal_text that sounds like it belongs in Design Thinking. If you have to ask "does this sound like it's doing Inventory Mapping's job?", the answer is probably yes. Keep it observational.

## Completion

When all skeletons across all batches have been processed, set `status` to `complete`, record `completed_at` with the current ISO 8601 timestamp, save the manifest one final time, and exit.

Report at the end:
- Total skeletons processed
- Signal Cards written to `cards/`
- Signal Cards staged to `signal_gpt_recovery/`
- Signal Cards flagged `needs_human_review`
- Skeletons below signal threshold (no output)
- Skeleton failures (structural)
- Splits performed
- Any `contract_case_uncovered` issues registered

This telemetry tells the operator whether Signal Extraction is producing clean, discrete observations or whether the upstream Extraction Records, the contract, or the validator rules need adjustment before the cards enter Inventory Mapping.
