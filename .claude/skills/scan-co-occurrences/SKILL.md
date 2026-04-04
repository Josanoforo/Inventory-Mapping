# Scan Co-occurrences — Skill

Read `modules/04_scanner.md` (section: Co-occurrences) before executing.

## Input

`working/index/card_index.jsonl`

## Output

`working/scans/co_occurrences.json` — validates against `schemas/scan_artifact.schema.json`

## Procedure

1. Load card index.
2. Find sets of 3+ cards that consistently appear around the same topic, entity, or phenomenon across at least 2 different rounds or sources.
3. For each co-occurrence cluster:
   - Verify minimum 3 cards.
   - Verify cross-round or cross-source presence.
   - Ask: does this cluster generate a question that Design Thinking would need to answer?
   - Record: pattern_id, description, signal_ids, signal_summaries.
4. Route each pattern:
   - Generates a plausible DT question → `tension_candidate`
   - Consistent co-occurrence but no DT question → `rejected_grouping`
5. Write scan artifact. Validate against schema.

## The DT question test

A co-occurrence generates a DT question if resolving or understanding the relationship between the co-occurring cards would change a design decision. If the co-occurrence is just "many cards about Etsy fees" — that's frequency, not a DT question.

## What does NOT count

- Pure frequency (many cards about the same topic).
- Cards from the same source that naturally cover the same ground.
- Thematic similarity without consistent co-appearance.
