# Module 04 — Scanner

## Purpose

Run 7 mechanical operations over the card index. Each produces a scan artifact. These artifacts feed the candidate builder.

## Input

- `working/index/card_index.jsonl`

## Output

- `working/scans/contradictions.json`
- `working/scans/asymmetries.json`
- `working/scans/frictions.json`
- `working/scans/co_occurrences.json`
- `working/scans/gaps.json`
- `working/scans/opposite_directions.json`
- `working/scans/lexical_overlap.json`

All validate against `schemas/scan_artifact.schema.json`.

## Operations

### 1. Contradictions
Find pairs of cards that affirm opposite things about the same subject.
- Both cards must reference the same entity, platform, or topic.
- The opposition must be explicit, not inferred.
- Minimum 2 cards per pattern.

### 2. Asymmetries
Find axes where distribution is unequal with support on both ends.
- Identify the axis (e.g., seller outcomes, platform adoption, pricing).
- Both poles must have card support.
- Unequal distribution is not contradiction.

### 3. Frictions
Find cards where something blocks or hinders without being a contradiction.
- The blocking element must be documented in cards.
- The thing being blocked must also be documented.
- Pure complaints without documented mechanism are not friction.

### 4. Co-occurrences
Find cards that appear together consistently around the same topic.
- Minimum 3 cards co-occurring.
- Co-occurrence must span at least 2 different rounds or sources.
- Must generate a plausible DT question to route as tension_candidate.
- If no DT question → route as rejected_grouping.

### 5. Gaps
Find areas where you would expect cards and there are none.
- Base expectation on what the corpus covers vs what is absent.
- A gap must limit the reading of the inventory to count.
- Report what is missing, not what is present.

### 6. Opposite directions
Find forces pushing in contrary directions documented across cards.
- Both directions must have card support.
- Different from contradiction: these are not about the same fact, but about different forces acting on the same system.

### 7. Lexical overlap
Find cards that share vocabulary or territory and might be the same phenomenon described differently.
- Flag for deduplication awareness, not as tension.
- Route as needs_audit unless clear friction exists.

## Routing rules per pattern

Each pattern gets a routing decision:
- `tension_candidate`: meets at least one Candidate Generation Rule from the canon.
- `rejected_grouping`: frequency without friction.
- `coverage_gap`: relevant absence.
- `isolated_signal`: single card, rare, preserved.
- `needs_audit`: partial support, unclear classification.

## Fail states

- Index file empty or unreadable → fail scan, report.
- Scan produces zero patterns → valid result (no patterns found), not a failure.
- Pattern has fewer than 2 signal_ids → invalid, do not include.

## Notes

- Each scan runs independently. They can run in any order.
- A card can appear in multiple scan outputs. No forced exclusivity.
- Do not merge scans. Each produces its own artifact file.
