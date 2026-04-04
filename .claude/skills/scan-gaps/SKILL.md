# Scan Gaps — Skill

Read `modules/04_scanner.md` (section: Gaps) before executing.

## Input

`working/index/card_index.jsonl`

## Output

`working/scans/gaps.json` — validates against `schemas/scan_artifact.schema.json`

## Procedure

1. Load card index.
2. Analyze what the corpus covers by domain, platform, product type, and perspective (seller/buyer/platform).
3. Identify areas where you would expect cards based on what IS present, but cards are absent.
4. For each gap:
   - Describe what is missing.
   - Reference cards that create the expectation (if any).
   - Explain how this gap limits reading the inventory.
   - Record: pattern_id, description, signal_ids (cards that create the expectation), routing.
5. Route all gaps as `coverage_gap`.
6. Write scan artifact. Validate against schema.

## Expected coverage to check against

Based on the corpus structure (10 rounds covering different product types and perspectives):
- Buyer perspective: is it proportional to seller perspective?
- Geographic: Spanish-language market vs English-language market coverage.
- Product types: are all types represented (ebooks, templates, planners, spreadsheets, prompts)?
- Platforms: are all major platforms represented?
- Income range: are intermediate outcomes represented, or only high and low?
- Temporal: are cards current or dated?
- Post-purchase: is there data on what happens after the sale?

## What counts as a gap

A gap must limit the reading of the inventory. "We don't have cards about X" is only a gap if X's absence makes the existing cards harder to interpret or creates a blind spot for DT.
