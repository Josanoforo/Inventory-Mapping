# Module 01 — Entry Gate

## Purpose

Verify that the signal card inventory is fit for mapping. If it fails, nothing else runs.

## Input

- `input/signal_cards_round_*.md` (10 files, 1,560 cards expected)

## Output

- `working/entry_gate/entry_gate_report.json`

## Checks

1. **Discrete cards**: No compound cards (one observation per card).
2. **No strategic interpretation**: Cards contain observations, not strategy.
3. **No cross-source meta-observations**: No "multiple sources agree" language leaked from Data Gathering.
4. **Evidence base preserved**: Every card has an Evidence base field.
5. **IDs present and traceable**: Every card has a valid `SC-R[round]-[number]` ID.

## Pass criteria

All 5 checks pass across all 1,560 cards.

## Fail behavior

If any check fails, report fails with specific card IDs and violation descriptions. Do not proceed to split.

## Notes

- Words like "should", "must" appearing inside quoted source content are not violations. Only card-level strategic interpretation counts.
- The check is over Observation and Evidence base fields, not over quoted material within them.
