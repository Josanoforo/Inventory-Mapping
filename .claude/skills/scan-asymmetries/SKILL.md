# Scan Asymmetries — Skill

Read `modules/04_scanner.md` (section: Asymmetries) before executing.

## Input

`working/index/card_index.jsonl`

## Output

`working/scans/asymmetries.json` — validates against `schemas/scan_artifact.schema.json`

## Procedure

1. Load card index.
2. Identify axes where cards distribute unevenly. An axis is a measurable dimension: seller outcomes, platform fees, product pricing, category volume, geographic coverage.
3. For each axis:
   - Find cards at both ends of the distribution.
   - Verify both poles have card support (minimum 2 cards per pole).
   - Define poles in corpus terms, not absolute numbers.
   - Record: pattern_id, description, signal_ids per pole, components, signal_summaries.
   - Same-actor filter: look up the `actor` field for every Signal ID in both poles from `working/index/card_index.jsonl`. If all Signal IDs across both poles share the same actor value → route to `rejected_grouping` with reason `"same_actor_discrepancy"`. Skip remaining routing steps for this pattern.
4. Route each pattern (after same-actor filter):
   - Both poles documented, clear distributional skew → `tension_candidate`
   - One pole has only 1 card → `needs_audit`
   - Cards cluster around same range (no real asymmetry) → `rejected_grouping`
5. Write scan artifact. Validate against schema.

## Critical distinction

Asymmetry ≠ contradiction. Some sellers earning more than others is asymmetry. A card saying "most sellers earn X" and another saying "most sellers earn not-X" is contradiction.

## Unit awareness

Flag when cards at different poles use different units (monthly vs lifetime, gross vs net). Declare in the pattern description. Do not normalize — just declare.

## Note

TC-001 already covers seller income asymmetry. If this scan detects the same pattern, reference TC-001 in the routing_rationale and do not produce a duplicate.
