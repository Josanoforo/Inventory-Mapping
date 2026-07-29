# Module — Signal Converter (Signal Extraction stage 2)

## Purpose

Transform Signal Card skeletons (produced by `phases/02-signal-extraction/scripts/signal_prepare.py`) into complete, validated Signal Cards by reading the extraction context, formulating an observational `signal_text`, and filling the 16 judgment fields following the Signal Extraction contract. The mechanical fields (`signal_id`, `source_record_ids`, `source_ids`, `round`, `traceability_pointers`) are already populated by stage 1 and must not be modified unless splitting produces additional cards.

This module is executed by the `extract-signals` skill.

## Position in the pipeline

Signal Converter stage 2 sits between Phase 2 Data Extraction and the Inventory Mapping entry gate. Its output — validated Signal Cards — feeds the Inventory Mapping pipeline (Entry Gate → Split Cards → Index Cards → Scanner → ...).

This module lives in `phases/02-signal-extraction/` because it fulfills the Signal Extraction contract, not Inventory Mapping operations.

## Inputs

| Path | Purpose |
|---|---|
| `working/signal_extraction/skeleton_batches/batch_NNN/skeleton_*.json` | Skeletons produced by stage 1, one file per Extraction Record |
| `working/signal_extraction/signal_prepare_manifest.json` | Stage 1 manifest. Must have `status: complete` before stage 2 can run. Also provides `signal_id_counter_at_stage1` for ID allocation during splitting |
| `phases/02-signal-extraction/contracts/signal_extraction_contract.md` | Signal Extraction contract. Read in full before processing any skeleton |
| `phases/02-signal-extraction/contracts/signal_extraction_validator.md` | Validator rules. Applied to every card before routing |
| `phases/02-signal-extraction/schemas/signal_card.schema.json` | Schema that completed cards must validate against |

## Outputs

| Path | Purpose |
|---|---|
| `working/signal_extraction/cards/<signal_id>.json` | Completed, validated Signal Cards. Flat directory for downstream consumption |
| `working/signal_extraction/signal_gpt_recovery/<signal_id>.json` | Cards that could not be completed automatically, staged for GPT recovery |
| `working/signal_extraction/signal_converter_manifest.json` | Stage 2 manifest. Tracks per-skeleton progress, splitting, routing decisions, and issues |

The directory `signal_gpt_recovery/` follows the pattern `<phase>_gpt_recovery/` established by prior phases. Material here is not rejected — it is material that the automated flow could not formulate observationally or could not validate against the schema, staged for GPT recovery.

## Closed vocabulary

### Manifest status values

| Value | Meaning |
|---|---|
| `pending` | Manifest exists but processing has not started |
| `in_progress` | Skeletons are being processed |
| `complete` | All skeletons processed, each routed to `cards/`, `signal_gpt_recovery/`, or logged as `skeleton_invalid` |
| `failed` | Unrecoverable error stopped the run |
| `blocked_by_stage_1_incomplete` | Stage 1 manifest is not `complete`; stage 2 cannot proceed |

### Issue types

| Value | When it applies |
|---|---|
| `skeleton_invalid` | A skeleton file from stage 1 does not have the expected structure or is missing required mechanical fields |
| `contract_case_uncovered` | The case falls outside anything the signal extraction contract addresses, and no fallback applies |
| `needs_human_review` | Card passed validation but has 4+ uncertainties; flagged for operator review |
| `schema_validation_failed` | Completed card does not validate against `signal_card.schema.json`; routed to `signal_gpt_recovery/` |
| `required_field_unfillable` | A required judgment field cannot be filled from the material available; routed to `signal_gpt_recovery/` |
| `multiple_required_fields_unfillable` | Two or more required judgment fields cannot be filled; routed to `signal_gpt_recovery/` |
| `split_performed` | The skeleton was split into 2 or more Signal Cards because it contained multiple discrete claims |
| `below_signal_threshold` | The extraction record does not reach the observational threshold for Signal Extraction; logged but not written to any destination |

This enum is closed. New issue types must be added here and to the manifest schema before the skill can register them.

### Destination values

A card always lands in exactly one destination:

| Value | Meaning |
|---|---|
| `cards` | Complete, schema-validated card written to `working/signal_extraction/cards/` |
| `signal_gpt_recovery` | Card could not be completed automatically, staged for GPT recovery |
| `skeleton_invalid` | Skeleton failed structural validation; no output file produced |
| `below_signal_threshold` | Record did not reach signal threshold; deliberately not written anywhere |

## Operations

Operations run sequentially. Each skeleton is a unit of work; checkpoints happen after all cards produced from a skeleton are written, not per batch. This is the checkpoint granularity that matches the cost of LLM work per skeleton (including potential splitting work).

### 1. Precondition checks

- Read `working/signal_extraction/signal_prepare_manifest.json`. If it does not exist or `status != complete`, set stage 2 manifest status to `blocked_by_stage_1_incomplete` and exit with a clear message. Do not process anything.
- Read `signal_id_counter_at_stage1` from the stage 1 manifest. Use this to initialize `next_signal_id_counter` in the stage 2 manifest if the stage 2 manifest does not already exist.
- Read `phases/02-signal-extraction/contracts/signal_extraction_contract.md` in full. If missing, fail with clear message.
- Read `phases/02-signal-extraction/contracts/signal_extraction_validator.md` in full. If missing, fail with clear message.
- Read `phases/02-signal-extraction/schemas/signal_card.schema.json`. If missing, fail with clear message.
- Create output directories if they do not exist: `working/signal_extraction/cards/`, `working/signal_extraction/signal_gpt_recovery/`.

### 2. Load or initialize stage 2 manifest

- If `working/signal_extraction/signal_converter_manifest.json` exists and `status == complete`, exit cleanly with a "nothing to do" message.
- If it exists and `status == in_progress`, read it. The `processed_skeletons` list and `next_signal_id_counter` are the resume state.
- If it does not exist, initialize with `status: pending`, `next_signal_id_counter` from stage 1 manifest, empty counters, and empty arrays.

### 3. Enumerate skeletons to process

- Walk `working/signal_extraction/skeleton_batches/batch_NNN/` in batch numeric order.
- Within each batch, process skeletons in alphabetical order by filename (deterministic ordering).
- Skip any skeleton whose `skeleton_signal_id` (the stage 1 signal_id) is already in the manifest's `processed_skeletons` list.

### 4. Process each skeleton

For each unprocessed skeleton:

**4.1 Read and validate skeleton structure.** Verify the following mechanical fields are present and structurally valid:
- `signal_id` — string matching `^SC-R\d+-\d+$`
- `source_record_ids` — non-empty array
- `source_ids` — non-empty array
- `round` — positive integer
- `traceability_pointers` — non-empty array
- `_extraction_context` — object containing at minimum `snippet_primary` (non-null string)

If any mechanical field is missing or invalid, register `skeleton_invalid` and continue to the next skeleton. Do not produce any output for this skeleton.

**4.2 Assess signal threshold.** Before formulating any signal, assess whether the extraction record's `snippet_primary` (read from `_extraction_context.snippet_primary`) reaches the observational threshold defined in the contract (§9, Decision boundary A vs D):

- If the content is entirely context with no discrete observable claim (contract §9D), register `below_signal_threshold` with specific detail and continue. Do not write to any destination.
- If the content is weak but usable (contract §9B), continue with processing but plan to add `context_insufficient` to `uncertainties`.
- Otherwise proceed to formulation.

**4.3 Assess splitting need.** Before writing the first card, read `_extraction_context` to assess whether the extraction record contains multiple discrete claims that the contract (§10) permits splitting. Apply these rules:

- Split only if: multiple distinct local claims are present within the same source and subject boundary, the claims do not need comparison between sources, and each split card would individually satisfy the schema.
- Do NOT split if: the claims share the same subject_exact and actor_level and can be expressed as one coherent observation, or if splitting would require introducing cross-source material.
  - Exception: observation + causal attribution by the speaker are always two distinct claims, even when they share subject_exact and actor_level. "What happened" and "why the speaker thinks it happened" are never one coherent observation.
- If splitting, allocate additional `signal_id` values by incrementing `next_signal_id_counter` in the manifest before formulating each additional card. The first card retains the stage 1 `signal_id`. Register `split_performed` in issues for this skeleton. Update manifest counter immediately.
- **No unexpressed factual claim.** If the snippet contains a second discrete factual affirmation — an additional data point, a comparative figure, a named case — that is not expressed in the card being produced, it must either be split into its own card or its omission explicitly recorded (in `normalization_notes` or `extraction_notes`, with the reason). No affirmation present in the snippet may be left both unexpressed and unregistered.

**4.4 Formulate signal_text and fill judgment fields.** For each card to be produced from this skeleton (one unless splitting), formulate the observational signal_text and fill the 16 judgment fields in this order:

1. **`signal_text`** — Write the observational signal text following contract §7 (Signal Card principles). The text must:
   - Describe a local observation, not a market reading
   - Avoid interpretive verbs (reveals, demonstrates, suggests that, confirms that, implies that)
   - Not mention the corpus, pattern, or cross-source material
   - Preserve the fact, not resolve it
   - Be derivable from `_extraction_context.snippet_primary` alone or with `snippet_context_before`/`snippet_context_after`

2. **`subject_exact`** — Preserve from `_extraction_context.subject_exact` unless the extraction record's subject must be narrowed further for this specific card. Never broaden. Never flatten meaningful distinctions (checkout ≠ payout, fee base ≠ net retained, active buyers ≠ discoverability).

3. **`actor_level`** — Identifies **who speaks or acts** in the observation — the entity that is the **source of the claim**, not who is affected by it. A help_center article about seller fees has `actor_level = platform` (Gumroad is speaking), not `seller` (even though sellers are affected). A seller blog post about their own earnings has `actor_level = seller` (the seller is speaking).

   Assignment rules by source type:
   - `help_center`, `pricing_page`, `platform_doc`, `policy_page` → always `platform`
   - `blog`, `seller_forum`, `reddit` where the author is a seller → `seller`
   - `blog`, `reddit` where the author is a buyer → `buyer`
   - `search_results_page`, `category_page` (platform-generated content) → `marketplace`
   - `product_listing`, or promotional content from an external provider speaking in
     first person about its own product or service → `third_party`. `third_party` is a
     third party selling or promoting its own product or service — never a seller of the
     marketplace under study.
   - Commentary or analysis with no first-person actor → `source`. `source` is reserved
     for commentary or analysis with no first-person actor — not for a third party
     speaking in first person to sell its own product (that is `third_party`).

   Inherit from `_extraction_context.actor_level` as a starting point, but override whenever the source type rule above applies. Never set `actor_level` based on who is *affected* by the observation.

4. **`platforms`** — Inherit from `_extraction_context.platforms`. Only platforms explicitly named in the local snippet; never infer.

5. **`product_type_if_explicit`** — Inherit from `_extraction_context.product_type_if_explicit`. Only if the source states it unambiguously.

6. **`metric_type`** — Inherit from `_extraction_context.metric_type`. From the closed enum. Use `unknown` if none applies clearly.

7. **`metric_value_raw`** — Inherit from `_extraction_context.metric_value_raw`. Original value as extracted. Null if not present.

8. **`metric_unit`** — Inherit from `_extraction_context.metric_unit`. Null if not present.

9. **`time_scope_raw`** — Inherit from `_extraction_context.time_scope_raw`. Preserve original temporal wording. Null if absent. `time_scope_raw` is verbatim from the snippet — do not append record metadata or access dates to it; those go in `normalization_notes`.

10. **`time_scope_normalized_if_safe`** — Inherit from `_extraction_context.time_scope_normalized_if_safe`. Only if safely derivable without interpretation.

11. **`geography_if_explicit`** — Inherit from `_extraction_context.geography_if_explicit`. Only if the source states a geographic scope.

12. **`evidence_role`** — Inherit from `_extraction_context.evidence_role`. If the signal formulation reveals a different role, adjust. Context must not become direct claim (contract §13, Rule 2).

13. **`local_qualifiers`** — Inherit from `_extraction_context.local_qualifiers`. Never drop qualifiers that condition the claim. Preserve verbatim.

    A qualifier is a condition that limits the scope of the claim — geographic scope, a threshold, a time window, a caveat. It is not source content. Full policy clauses, definitions, and entire sentences do not belong here: if they are part of the claim they belong in `signal_text`; if they are a separate claim they belong in another card.

14. **`uncertainties`** — Inherit from `_extraction_context.uncertainties`. Add any new uncertainty codes revealed by the signal formulation. Values from the closed enum only.

15. **`normalization_notes`** — Notes on any minimal normalization applied during signal formulation. Must not reference other records, cross-source comparisons, or interpretive content (see validator §11, Notes Locality check).

16. **`extraction_notes`** — Carryover notes from `_extraction_context.parser_notes` that remain useful for audit. Apply the same locality discipline as normalization_notes.

For each judgment field, inheritance from `_extraction_context` is the default. Override only when the signal formulation requires it, and record the reason in `normalization_notes` or `extraction_notes`.

**4.5 Apply validator checks.** Run the completed card through all 11 checks in `phases/02-signal-extraction/contracts/signal_extraction_validator.md`:

1. Observational wording — `signal_text` is local, not a market reading
2. Subject exactness preserved — `subject_exact` not widened
3. Actor level preserved — not flattened across buyer/seller/marketplace
4. Time scope preserved — not dropped or unsafely normalized
5. Qualifiers preserved — no limiting condition dropped
6. Evidence role preserved — context not promoted to direct claim
7. Single-claim discreteness — one coherent observation, not a fused bundle
8. No cross-source meta-observation — grounded in one local source
9. Traceability preserved — `source_record_ids` and `traceability_pointers` intact
10. No tension-smuggling — not doing Inventory Mapping's job
11. Notes locality — `normalization_notes` and `extraction_notes` contain no forbidden patterns

For checks 1–10, apply the validator's pass/flag/fail/not_applicable logic. For check 11 (Notes Locality), if the flag is triggered, apply the mandatory scrubbing step described in the validator before routing.

After all checks:
- `pass` — proceed to schema validation
- `pass_with_flags` — proceed to schema validation; record all flag codes in issues
- `rework` — do not write to `cards/`. Route to `signal_gpt_recovery/` with the rework-reason detail. Register `schema_validation_failed` (sub-type: rework).
- `reject` — do not write to `cards/`. Route to `signal_gpt_recovery/` with rejection detail. Register `schema_validation_failed` (sub-type: reject).

**4.6 Check uncertainty count.** After validator checks, count the entries in `uncertainties`. If the count is 4 or more, add `needs_human_review` to the issues for this card. The card still proceeds.

**4.7 Validate completed card against schema.** Run the card through `phases/02-signal-extraction/schemas/signal_card.schema.json`.

- If validation passes: write to `working/signal_extraction/cards/<signal_id>.json`. Destination is `cards`.
- If validation fails because a required judgment field is null: determine which field(s). If one, register `required_field_unfillable`; if two or more, register `multiple_required_fields_unfillable`. Route to `signal_gpt_recovery/`.
- If validation fails for any other schema reason: register `schema_validation_failed` with the specific error. Route to `signal_gpt_recovery/`.

**4.8 Write to destination.**

- For `cards` destination: write the complete card JSON to `working/signal_extraction/cards/<signal_id>.json`.
- For `signal_gpt_recovery` destination: write a recovery-ready JSON to `working/signal_extraction/signal_gpt_recovery/<signal_id>.json` using the structure defined in "GPT recovery staging" below.

**4.9 Update manifest.** After all cards from this skeleton are written, append one entry to `processed_skeletons` with `skeleton_signal_id`, `cards_produced` (array of card entries with signal_id and destination), `issues_for_this_skeleton`, and `processed_at`. Update counters. Save the manifest to disk.

This update happens after every skeleton (all cards from it), not every batch. If interrupted, resumption starts from the next unprocessed skeleton.

### 5. Completion

When all skeletons across all batches have been processed, set manifest status to `complete`, record `completed_at` timestamp, and exit.

## GPT recovery staging

Cards routed to `signal_gpt_recovery/` are staged with the structure the GPT recovery flow needs:

```json
{
  "signal_id": "SC-R{round}-{NNN}",
  "recovery_type": "signal_extraction_incomplete",
  "origin_stage": "signal_extraction_stage_2",
  "original_skeleton": { "...the stage 1 skeleton as read..." },
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
  "staged_at": "<iso timestamp>"
}
```

The `recovery_guidance.suggested_direction` must be concrete. For a rework case: "Narrow signal_text back to one local observation about [specific subject]; remove the phrase 'this demonstrates' and replace with the verbatim claim from the snippet." For a missing field: "Re-open source at [source_ref] to recover the actor_level for the claim about [subject_exact]." Generic guidance like "fix the card" is not acceptable.

## Signal threshold guidance

The contract (§9) defines four decision outcomes. Apply them as follows:

**Convert to Signal Card (§9A):** The snippet contains a discrete, locally observable claim with traceable source. Clear subject, or at most one preserved ambiguity.

**Preserve as isolated but weak (§9B):** There is something observable but the material is fragmented or partially unfillable. Produce the card with `context_insufficient` in uncertainties, route to `cards/` if schema validates.

**Return to extraction rework (§9C):** The record contained value but the signal is not formulable observationally from this skeleton alone. Route to `signal_gpt_recovery/` with rework guidance.

**Reject from signal layer (§9D):** No discrete claim exists. The snippet is purely contextual with no local observation. Register `below_signal_threshold`, do not write to any destination.

## Splitting rules (contract §10)

A skeleton may be split into multiple Signal Cards only if:

1. The extraction record's `_extraction_context` contains two or more clearly distinct local claims
2. The claims share the same source (`source_ids`) so cross-source synthesis is not occurring
3. Each resulting card would independently satisfy the schema
4. Splitting does not require comparing the claims to each other
5. If a passage contains both a factual observation AND a causal attribution by the speaker
   (e.g., "I got zero views [observation] because Discover requires a first sale [attribution]"),
   split into two cards even if they share subject_exact and actor_level. The observation card
   describes what happened. The attribution card describes what the speaker claims caused it.
   Both are extractable — but they are distinct claims that downstream phases must be able
   to process independently.

When splitting is performed:
- The first card retains the skeleton's original `signal_id`
- Additional cards receive new IDs allocated from `next_signal_id_counter`
- `next_signal_id_counter` is incremented and saved to the manifest before each additional ID is used
- All cards from one skeleton carry the same `source_record_ids` and `source_ids` (they all derive from the same Extraction Record)
- `split_performed` is registered in `issues_for_this_skeleton`

Do not split if the two claims would be better expressed as one card with two qualifiers. Do not split to create two half-signals when one discrete signal is what the evidence supports.

## Fail states

| Situation | Behavior |
|---|---|
| Stage 1 manifest missing or not complete | Set status `blocked_by_stage_1_incomplete`, exit |
| Signal Extraction contract missing | Fatal error, exit with clear message |
| Signal Extraction validator missing | Fatal error, exit with clear message |
| Signal Card schema missing | Fatal error, exit with clear message |
| Skeleton directory empty | Fatal error, exit with clear message |
| Individual skeleton unreadable or malformed | Register `skeleton_invalid`, continue with next |
| I/O error writing a card or recovery file | Register issue with detail, continue with next skeleton |

## Resumability

Checkpoint granularity is per skeleton (all cards produced from it), not per batch.

On startup:

1. Read `working/signal_extraction/signal_converter_manifest.json`.
2. If `status == complete`: exit cleanly.
3. If `status == in_progress`: read `processed_skeletons` (use `skeleton_signal_id` field) and `next_signal_id_counter`. Skip any skeleton already processed. Resume from the next unprocessed skeleton using the saved `next_signal_id_counter`.
4. If `status == blocked_by_stage_1_incomplete`: re-check `working/signal_extraction/signal_prepare_manifest.json`. If stage 1 is now `complete`, reset status to `in_progress` and proceed. Otherwise exit with message.
5. If `status == failed`: do not auto-resume. Operator must inspect manifest, resolve failure, and reset status before re-running.
6. If manifest does not exist: read `signal_id_counter_at_stage1` from stage 1 manifest; initialize stage 2 manifest with `status: in_progress`, `next_signal_id_counter` set to that value, empty arrays, and proceed.

## Skill that executes this module

`.claude/skills/extract-signals/SKILL.md`

---

## Notes on naming

The directory `signal_gpt_recovery/` follows the pattern `<phase>_gpt_recovery/` established by `working/data_gathering/phase0_part4_gpt_recovery/`, `working/source_intake/source_intake_gpt_recovery/`, and `working/data_extraction/extraction_gpt_recovery/`. Each phase that produces recovery candidates has its own directory, so the GPT recovery flow knows which phase a given candidate originates from and can apply the appropriate recovery logic.

Material in `signal_gpt_recovery/` includes: cards that were reworked (wording drifted interpretive), cards that were rejected (cross-source synthesis detected), and cards that could not be completed because required fields were unfillable from the snippet. The `issue_type` in `failure_detail` distinguishes these cases for the recovery operator.
