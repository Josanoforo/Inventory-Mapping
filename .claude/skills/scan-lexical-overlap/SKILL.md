# Scan Lexical Overlap — Skill

Read `modules/04_scanner.md` (section: Lexical overlap) before executing.

## Input

`working/index/card_index.jsonl`

## Output

`working/scans/lexical_overlap.json` — validates against `schemas/scan_artifact.schema.json`

## Procedure

1. Load card index.
2. Find groups of cards that share significant vocabulary, entities, or territory and might describe the same phenomenon from different angles.
3. For each overlap group:
   - List shared vocabulary/entities.
   - Assess: are these cards about the same thing or different things that sound similar?
   - Record: pattern_id, description, signal_ids, signal_summaries.
4. Route each pattern:
   - Overlap reveals friction or tension between the overlapping cards → `tension_candidate`
   - Overlap is deduplication signal (same phenomenon, different sources) → `needs_audit` with note "possible dedup"
   - Overlap is coincidental vocabulary → `rejected_grouping`
5. Write scan artifact. Validate against schema.

## Purpose

This scan exists primarily for deduplication awareness. If two different scans (e.g., contradictions and frictions) might pick up the same underlying pattern because the cards share vocabulary, lexical overlap flags it early.

## What to flag

- Cards across rounds that describe the same platform behavior in different words.
- Cards that use the same figures from the same original source but appear in different rounds.
- Cards where the observation is nearly identical but sourced differently.
