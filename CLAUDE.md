# Inventory Mapping — Project

## What this is

Automated inventory mapping over 1,560 Signal Cards. One subagent (`inventory-mapping`) runs the full pipeline using skills for each sub-operation.

## Authority hierarchy

1. `reference/protocol_canonical.md` — the canon. Overrides everything.
2. `modules/*.md` — normative specs per step. Override skills.
3. `.claude/skills/*/SKILL.md` — executable routines. Follow modules.

If a skill contradicts its module, the module wins.
If a module contradicts the canon, the canon wins.

## Pipeline sequence

1. Entry Gate → verify input integrity
2. Split Cards → raw rounds into discrete card batches
3. Index Cards → batches into card_index.jsonl
4. Scanner → 7 mechanical operations over index
5. Candidate Builder → scan patterns into tension candidates
6. Validator → each TC against protocol checks

Each step reads from `working/` and writes to `working/`. Final outputs go to `output/`.

## Global rules

- Every Signal ID must be verified against `input/signal_cards_round_*.md` before inclusion.
- Format: `SC-R[round]-[number]` with brief description in parentheses.
- No figures without a Signal ID backing them.
- No valorative adjectives in mechanical descriptions.
- Allowed verbs: aparece, co-ocurre, contradice, se distribuye, no se encontró, se concentra, se separa en polos, no converge.
- Forbidden language: importante, fuerte, central, revela que, demuestra que, necesidad, solución, recomendación, sugiere que.
- Polo definitions in corpus terms, not absolute ranges.
- Mixed units must be declared, not hidden.
- Human fields are never filled by the agent.

## Schemas

All intermediate and final outputs must validate against their schema in `schemas/`. If output does not validate, the step has failed.

## Resumability

Every step that processes batches maintains a manifest in `working/`. If interrupted, resume from the last recorded position in the manifest.
