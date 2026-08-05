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
   - Every pattern with `routing: rejected_grouping` carries a `reason_code`. Mechanical values (`same_actor`, `insufficient_ids`) are not emitted by this skill — the router computes them.
   - Mechanical routing rules (same-actor, insufficient IDs) are applied by `scan_router.py`, not here. See `phases/03-inventory-mapping/modules/04_scanner.md`, "Routing authority". Do not restate them.
4. Route each pattern:
   - Both forces documented, acting on same system → `tension_candidate`
   - One force has single-card support → `needs_audit`
   - Forces act on different systems → `rejected_grouping`, `reason_code: relation_not_present`
5. Write scan artifact. Validate against schema.

## Distinction from contradiction

- Contradiction: Card A says "X is true", Card B says "X is false." Same claim, opposite assertions.
- Opposite direction: Card A documents a force pushing toward Y, Card B documents a force pushing away from Y. Different forces, same system.

## Examples of what to look for

- AI making content creation easier (more supply) vs buyers becoming more discerning (demand for quality).
- Platform fees increasing vs seller margins decreasing.
- Market growing (more buyers) vs market saturating (more sellers).
