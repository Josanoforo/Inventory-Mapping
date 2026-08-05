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
   - Every pattern with `routing: rejected_grouping` carries a `reason_code`. Mechanical values (`same_actor`, `insufficient_ids`) are not emitted by this skill — the router computes them.
   - Mechanical routing rules (same-actor, insufficient IDs) are applied by `scan_router.py`, not here. See `phases/03-inventory-mapping/modules/04_scanner.md`, "Routing authority". Do not restate them.
5. Route each pattern:
   - Clear explicit contradiction with 2+ cards per side → `tension_candidate`
   - Apparent contradiction but one side has only 1 card → `needs_audit`
   - Thematic overlap without actual opposition → `rejected_grouping`, `reason_code: relation_not_present`
6. Write scan artifact. Validate against schema.

## What counts as contradiction

- Card A says "X is Y" and Card B says "X is not Y" (or opposite of Y).
- Both about the same subject, same scope.

## What does NOT count

- Different subjects that seem related.
- One card about Etsy, another about Gumroad — different platforms are not contradiction.
- A card saying "market is saturated" and another saying "I succeeded" — that's asymmetry, not contradiction.
