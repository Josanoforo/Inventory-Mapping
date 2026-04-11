# Scan Opposite Directions — Skill

Read `modules/04_scanner.md` (section: Opposite directions) before executing.

## Input

`working/index/card_index.jsonl`

## Output

`working/scans/opposite_directions.json` — validates against `schemas/scan_artifact.schema.json`

## Procedure

1. Load card index.
2. Find pairs of forces or trends documented in cards that push in contrary directions on the same system.
3. For each pattern:
   - Identify Force A with card support.
   - Identify Force B with card support.
   - Verify both forces act on the same system or domain.
   - Verify both have minimum 2 cards support.
   - Record: pattern_id, description, signal_ids, components (Force A, Force B), signal_summaries.
   - Same-actor filter: look up the `actor` field for every Signal ID in both poles from `working/index/card_index.jsonl`. If ALL Signal IDs across BOTH poles have the SAME actor value → route to rejected_grouping with reason "same_actor_discrepancy".

     This check is purely mechanical: compare actor values only. Do NOT evaluate whether the cards in each pole refer to the same mechanism, sub-topic, or channel. Grounding evaluation is the human's job during review, not the scanner's.

     If the poles contain different actor values, the pattern passes this filter regardless of any other consideration.
4. Route each pattern (after same-actor filter):
   - Both forces documented, acting on same system → `tension_candidate`
   - One force has single-card support → `needs_audit`
   - Forces act on different systems → `rejected_grouping`
5. Write scan artifact. Validate against schema.

## Distinction from contradiction

- Contradiction: Card A says "X is true", Card B says "X is false." Same claim, opposite assertions.
- Opposite direction: Card A documents a force pushing toward Y, Card B documents a force pushing away from Y. Different forces, same system.

## Examples of what to look for

- AI making content creation easier (more supply) vs buyers becoming more discerning (demand for quality).
- Platform fees increasing vs seller margins decreasing.
- Market growing (more buyers) vs market saturating (more sellers).
