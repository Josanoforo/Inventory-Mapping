Scan Lexical Overlap — Skill
Read `modules/04_scanner.md` (section: Lexical overlap) before executing.
Input
`working/index/card_index.jsonl`
Output
`working/scans/lexical_overlap.json` — validates against `schemas/scan_artifact.schema.json`
Procedure
Load card index.
Find groups of cards that share significant vocabulary, entities, or territory and might describe the same phenomenon from different angles.
For each overlap group:
List shared vocabulary/entities.
Assess: are these cards about the same thing or different things that sound similar?
Record: pattern_id, description, signal_ids, signal_summaries.
Route each pattern:
Overlap reveals explicit friction or tension between the overlapping cards → `tension_candidate`
ALL other overlap → `rejected_grouping` with note "possible dedup"
This includes: shared figures, shared entity names, same fact from different sources, coincidental vocabulary.
Write scan artifact. Validate against schema.
Critical rule
Do NOT route as `needs_audit` by default. The default for lexical overlap is `rejected_grouping`. Only `tension_candidate` if there is explicit friction between the cards — not just shared vocabulary.
Cards that repeat the same figure (e.g., "$0.20", "6.5%") about the same platform from different rounds are deduplication signals, not tensions.
Purpose
This scan exists primarily for deduplication awareness. If two different scans (e.g., contradictions and frictions) might pick up the same underlying pattern because the cards share vocabulary, lexical overlap flags it early.
What to flag
Cards across rounds that describe the same platform behavior in different words.
Cards that use the same figures from the same original source but appear in different rounds.
Cards where the observation is nearly identical but sourced differently.
