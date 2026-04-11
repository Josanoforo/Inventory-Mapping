# Scan Frictions — Skill

Read `modules/04_scanner.md` (section: Frictions) before executing.

## Input

`working/index/card_index.jsonl`

## Output

`working/scans/frictions.json` — validates against `schemas/scan_artifact.schema.json`

## Procedure

1. Load card index.
2. Find patterns where something documented in cards blocks, hinders, or creates cost for something else also documented in cards.
3. For each friction pattern:
   - Identify the blocking element (what creates the friction) with card support.
   - Identify what is being blocked or hindered with card support.
   - Verify both sides have card support (minimum 2 cards total).
   - Record: pattern_id, description, signal_ids, components (blocker + blocked), signal_summaries.
   - Same-actor filter: look up the `actor` field for every Signal ID in both poles from `working/index/card_index.jsonl`. If ALL Signal IDs across BOTH poles have the SAME actor value → route to rejected_grouping with reason "same_actor_discrepancy".

     This check is purely mechanical: compare actor values only. Do NOT evaluate whether the cards in each pole refer to the same mechanism, sub-topic, or channel. Grounding evaluation is the human's job during review, not the scanner's.

     If the poles contain different actor values, the pattern passes this filter regardless of any other consideration.
4. Route each pattern (after same-actor filter):
   - Both sides documented, mechanism clear → `tension_candidate`
   - Mechanism unclear or single-card support → `needs_audit`
   - Complaints without documented mechanism → `rejected_grouping`
5. Write scan artifact. Validate against schema.

## What counts as friction

- Platform limitation that creates seller/buyer cost (e.g., can't download from app → support burden).
- Licensing complexity that blocks or complicates a documented activity.
- Fee structure that erodes documented seller margins.
- Technical incompatibility that blocks documented use case.

## What does NOT count

- A single complaint without mechanism.
- A card saying something is hard without documenting what it blocks.
- Seller frustration expressed in a card without a documented structural cause in other cards.
