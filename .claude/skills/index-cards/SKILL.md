# Index Cards — Skill

Read `modules/03_indexer.md` before executing.

## Steps

1. Read `working/index/index_manifest.json` if it exists (for resumption). If not, initialize it.
2. Read `working/split/split_manifest.json` to get list of batches and totals.
3. For each batch file in `working/split/card_batches/`:
   a. If batch already processed per manifest, skip.
   b. Parse each card in the batch.
   c. Extract fields into a JSON record:
      ```json
      {
        "id": "SC-R1-001",
        "round": 1,
        "observation": "...",
        "source": "...",
        "date": "...",
        "source_type": "blog",
        "domain": "market",
        "evidence_base": "...",
        "extraction_status": "extracted",
        "entities": ["Etsy", "Gumroad"],
        "figures": ["$200/month", "10%"]
      }
      ```
   d. Validate record against `schemas/card_record.schema.json`.
   e. If valid, append as one line to `working/index/card_index.jsonl`.
   f. If invalid, log in manifest issues, skip record.
   g. Update manifest: batches_processed, cards_indexed, last_batch_processed.
4. After all batches: verify cards_indexed matches expected total (minus skipped).
5. Set manifest status to `complete` or `failed`.

## Entity extraction guidance

- **entities**: Platform names (Etsy, Gumroad, Notion, Canva, Amazon KDP, Shopify, etc.), seller names when named, product types (template, ebook, planner, spreadsheet, prompt).
- **figures**: Any number with unit or currency. "$200/month", "10%", "1,560 cards", "30,000+ templates".
- Best-effort. Missing an entity is acceptable. Inventing one is not.

## Validation

Each JSONL line must be independently parseable JSON and validate against schema.
