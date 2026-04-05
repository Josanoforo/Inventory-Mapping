# Legacy Migration Summary

---

## Run metadata

| Field | Value |
|---|---|
| Migration version | 0.1 |
| Total legacy cards in corpus | 1,561 |
| Cards processed in this run | 20 (stratified pilot) |
| Run date | 2026-04-05 |
| Run by | legacy-signal-card-migration-skill/pilot-20 |

---

## Distribución por recoverability_status

| Status | Count | % |
|---|---|---|
| `clean_mappable` | 6 | 30% |
| `mappable_with_flags` | 8 | 40% |
| `schema_gap` | 3 | 15% |
| `needs_source_recovery` | 2 | 10% |
| `unrecoverable` | 1 | 5% |
| **Total** | **20** | **100%** |

**Usable (clean + flags):** 14 / 20 = **70%**

Projected to full corpus (1,561 cards):
- clean_mappable: ~468
- mappable_with_flags: ~624
- schema_gap: ~234
- needs_source_recovery: ~156
- unrecoverable: ~78

---

## Distribución por traceability_grade

| Grade | Count | % |
|---|---|---|
| `complete` | 7 | 35% |
| `partial` | 7 | 35% |
| `weak` | 5 | 25% |
| `none` | 1 | 5% |
| **Total** | **20** | **100%** |

Cards with at least partial traceability: 14 / 20 = 70%.

---

## Principales failure_reasons detectados

| Failure reason | Count |
|---|---|
| `source_ref_partial_only` | 8 |
| `snippet_not_verifiable` | 7 |
| `benchmark_is_not_source_type` | 2 |
| `source_type_not_in_new_enum` | 2 |
| `role_too_ambiguous` | 2 |
| `third_party_policy_contamination` | 1 |
| `source_ref_missing` | 1 |
| `snippet_missing` | 1 |
| `traceability_broken` | 1 |

*Note: one card can have multiple failure_reasons. The unrecoverable card (SC-R1-031) accounts for 3 of the bottom reasons.*

---

## Schema gaps detectados

| Legacy value | Count | Proposed resolution |
|---|---|---|
| `benchmark` (Marketsy.ai) | 1 | Infer `database_profile`; human reclassification required |
| `benchmark` (Etsy market pages) | 1 | Infer `search_results_page`; human reclassification required |
| `other_specified (TikTok self-report)` | 1 | Ontology decision required: social media video post has no canonical source_type |

**Pattern:** `benchmark` is the primary recurring gap — 2 of 3 schema_gap cards. Both require human reclassification because type inference without URL is low confidence. The TikTok case requires an ontology decision (new enum value or mapping policy for social media video posts).

---

## Principales grupos de needs_source_recovery

| Pattern | Count | Suggested followup |
|---|---|---|
| Publication name only, no URL (news/blog) | 2 | `reopen_source_for_url` — search by publication name + topic |

Cards: SC-R1-004 (anonymous blog), SC-R1-018 (LaRepublica.es).

---

## Recomendaciones de follow-up

1. **URL prepend pass**: 3 cards have domain URLs without `https://` (SC-R2-001, SC-R2-111, SC-R10-023). A mechanical pass prepending `https://` and verifying returns upgrades them from `partial` traceability.

2. **Benchmark reclassification**: 2 schema_gap cards use `benchmark` as source_type. Human decision on the inferred type (`database_profile` vs `search_results_page`) is required before these can advance.

3. **TikTok ontology decision**: 1 card (SC-R1-030) uses a TikTok self-report with no canonical source_type. Decision required: add `video_social` or `social_media_post` to the enum, or map to `video_transcript`, or hold indefinitely.

4. **Source recovery for LaRepublica.es**: SC-R1-018 has publication name and date (March 2026). Search is feasible.

5. **Evidence role review**: 2 cards flagged `role_too_ambiguous` (SC-R4-001, SC-R6-019). Both have `comparative_commentary` assigned conservatively. Human review can upgrade if warranted.

---

## Pilot status

Pilot passed structurally. All 20 records produced and validated against `legacy_signal_card_migration.schema.json` with 0 schema errors. Failure reasons are mechanical and fully documented.

**Scale remains pending decisions on:**
- Social-media source_type: `SC-R1-030` (TikTok self-report) has no canonical `source_type`; ontology decision required before migrating that class of card
- Benchmark handling visibility: policy for `benchmark`-typed cards (keep `schema_gap` as terminal state, or add URL-pattern reclassification pass) not yet decided
- Non-destructive URL normalization design: ~460 corpus cards carry domain URLs without `https://`; the approach (pre-processing pass vs. post-processing pass vs. no pass) must be agreed before a full run locks in traceability grades

No scale run has been initiated.

---

## Notas de auditoría

- Pilot ran via Python script in main session (sub-agent timed out at preflight stage).
- All 20 records written to `legacy-migration/working/migrations/legacy_signal_card_migrations.jsonl`.
- Schema validation: `jsonschema` library, Python 3. All 20 VALID.
- `unresolved_cases.md` created during preflight hardening (was missing from rail).
- Stratified sample: 10 rounds × 2 cards each (20 total), covering 9 distinct legacy source_type values.
- No modifications made to `working/index/card_index.jsonl`, `input/signal_cards_round_*.md`, or any canonical schema outside the patched upstream files.
