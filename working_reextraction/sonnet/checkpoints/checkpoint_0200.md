# Checkpoint — batches 001–008 (~200 records)

## Independence note
This run did NOT read, open, list, or grep `working/data_extraction/records/` (the
official corpus) at any point. Only the permitted inputs were used: skeletons in
`working/data_extraction/skeleton_batches/batch_001` through `batch_008`, the Phase 1
data extraction contract, the schema, `pipeline_vocabulary.yaml`, and
`working_reextraction/sonnet/criteria.md`.

## Counts
- Skeletons in batch_001–batch_008: **200**
- Records written to `records/`: **200**
- Records written to `rejected_archive/`: **0**
- `out_of_enum` occurrences: **5** (all in `metric_type`)
- `schema_enum_conflict` occurrences: **0**

## out_of_enum distribution (by field)
- `metric_type`: 5
  - `paid_creator_count` — 2 (Patreon "creators with at least one paying member" stats; no schema enum value distinguishes creator-count from buyer-count, so `active_buyers` was not forced)
  - `content_category_distribution` — 2 (Patreon creator-profile counts by content category; no schema enum value for category-share distributions)
  - `complaint_count` — 1 (Domestika third-party complaints-platform aggregate complaint volume; no schema enum value for complaint counts)

No other field (`claim_type`, `actor_level`, `product_type_if_explicit`, `evidence_role`,
`uncertainties`) required an out-of-enum value in this batch range.

## schema_enum_conflict distribution
None. The three vocab phase_1_only uncertainty values not present in the schema enum
(`source_type_unclear`, `metric_type_unclear`, `snippet_needs_reopen`) were not needed
for any of the 200 records processed — the ambiguities encountered in this range were
adequately covered by the schema's own uncertainty values (`subject_ambiguity`,
`actor_level_unclear`, `time_scope_unclear`, `source_date_unclear`,
`current_vs_historical_ambiguity`, `context_insufficient`, `anecdotal_single_source`,
`methodology_unclear`, `author_conflict_of_interest_possible`, `net_vs_gross_ambiguity`,
`none`).

## Rejections
Zero records were rejected as `required_field_unfillable`. Even the sparsest snippets
in this range (truncated quotes, bare navigation/category labels, raw stat-block
layouts) had a determinable local subject once source context (title, source_type,
surrounding metadata) was taken into account, so `subject_exact` was fillable without
invention in every case. Several such thin snippets instead carry elevated
`uncertainties` (`context_insufficient`, `subject_ambiguity`) and explanatory
`parser_notes` rather than being rejected outright.

## New ambiguity patterns encountered (not explicitly covered by criteria.md)

1. **Aggregator/database metrics with no matching `metric_type` enum value.** Several
   sources (Graphtreon, earthweb, third-party complaint trackers) report counts that
   are real, determinable, single-figure metrics but do not map to any of the 20
   schema `metric_type` enum values — e.g., a count of *creators* with paying members
   (distinct from `active_buyers`, which is buyer-side), a distribution of *creator
   profiles* across content categories, and a platform's aggregate *complaint count*.
   Per the out-of-enum protocol these were written as descriptive literal strings
   (`paid_creator_count`, `content_category_distribution`, `complaint_count`) rather
   than forced into the nearest schema value, since e.g. `active_buyers` would
   silently collapse a creator-count into a buyer-count (a layer-collapse the contract
   explicitly forbids).

2. **Ambiguous multi-value stat blocks from ranking/database-profile layouts.**
   Several `database_profile` sources (e.g., Graphtreon rank tables) present two or
   three metrics in one visual block (e.g., paid-member count + monthly payout for one
   ranked entity) with no dominant single figure. These were recorded as
   `metric_type` arrays with a single combined `metric_value_raw` string, per the
   criteria.md guidance on mixed explicit metrics — this pattern recurred often
   enough in this range that it is worth naming explicitly.

3. **Un-attributable forum-reply authorship (platform staff vs. peer seller).**
   Several Domestika seller-forum replies address a named user by handle in a
   support-answer tone, making it genuinely ambiguous whether the speaker is
   Domestika community staff (→ `platform`) or a peer seller answering informally
   (→ `seller`). Resolved conservatively as `seller` (the forum's default per the
   contract's assignment_rule) with `actor_level_unclear` added to `uncertainties`
   and a `parser_notes` explanation, rather than guessing.

These three points have been appended to `working_reextraction/sonnet/criteria.md`
below the line `--- Agregado tras batch_008: ... ---`.
