# Scan Frictions — Skill

Read `modules/04_scanner.md` (section: Frictions) before executing.

## Input

`working/index/card_index.jsonl`

## Output

`working/scans/frictions.json` — validates against `schemas/scan_artifact.schema.json`

## Procedure

1. Load card index.
2. Find patterns where something documented in cards blocks, hinders, or creates cost for something else also documented in cards.
3. For each friction pattern:
   - Identify the blocking element (what creates the friction) with card support.
   - Identify what is being blocked or hindered with card support.
   - Verify both sides have card support (minimum 2 cards total).
   - Record: pattern_id, description, signal_ids, components (blocker + blocked), signal_summaries.
   - Every pattern with `routing: rejected_grouping` carries a `reason_code`. Mechanical values (`same_actor`, `insufficient_ids`) are not emitted by this skill — the router computes them.
   - Mechanical routing rules (same-actor, insufficient IDs) are applied by `scan_router.py`, not here. See `phases/03-inventory-mapping/modules/04_scanner.md`, "Routing authority". Do not restate them.
4. Route each pattern:
   - Both sides documented, mechanism clear → `tension_candidate`
   - Mechanism unclear or single-card support → `needs_audit`
   - Complaints without documented mechanism → `rejected_grouping`, `reason_code: relation_not_present`
5. Write scan artifact. Validate against schema.

## What counts as friction

- Platform limitation that creates seller/buyer cost (e.g., can't download from app → support burden).
- Licensing complexity that blocks or complicates a documented activity.
- Fee structure that erodes documented seller margins.
- Technical incompatibility that blocks documented use case.

## What does NOT count

- A single complaint without mechanism.
- A card saying something is hard without documenting what it blocks.
- Seller frustration expressed in a card without a documented structural cause in other cards.
