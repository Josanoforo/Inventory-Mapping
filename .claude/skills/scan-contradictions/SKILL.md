# Scan Contradictions — Skill

Read `modules/04_scanner.md` (section: Contradictions) before executing.

## Input

`working/index/card_index.jsonl`

## Output

`working/scans/contradictions.json` — validates against `schemas/scan_artifact.schema.json`

## Procedure

1. Load card index.
2. Group cards by shared entities and topics.
3. Within each group, find pairs where observations affirm opposite things about the same subject.
4. For each pair:
   - Verify both cards reference the same entity/topic.
   - Verify the opposition is explicit in the observation text, not inferred.
   - Record: pattern_id, description (mechanical verbs only), signal_ids, signal_summaries, components (the two opposing sides).
   - Same-actor filter: look up the `actor` field for every Signal ID in both poles from `working/index/card_index.jsonl`. If ALL Signal IDs across BOTH poles have the SAME actor value → route to rejected_grouping with reason "same_actor_discrepancy".

     This check is purely mechanical: compare actor values only. Do NOT evaluate whether the cards in each pole refer to the same mechanism, sub-topic, or channel. Grounding evaluation is the human's job during review, not the scanner's.

     If the poles contain different actor values, the pattern passes this filter regardless of any other consideration.
5. Route each pattern (after same-actor filter):
   - Clear explicit contradiction with 2+ cards per side → `tension_candidate`
   - Apparent contradiction but one side has only 1 card → `needs_audit`
   - Thematic overlap without actual opposition → `rejected_grouping`
6. Write scan artifact. Validate against schema.

## What counts as contradiction

- Card A says "X is Y" and Card B says "X is not Y" (or opposite of Y).
- Both about the same subject, same scope.

## What does NOT count

- Different subjects that seem related.
- One card about Etsy, another about Gumroad — different platforms are not contradiction.
- A card saying "market is saturated" and another saying "I succeeded" — that's asymmetry, not contradiction.
