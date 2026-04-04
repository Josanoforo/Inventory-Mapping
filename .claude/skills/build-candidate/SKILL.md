Build Candidate — Skill
Read `modules/05_candidate_builder.md` before executing.
Steps
1. Collect routed patterns
Read all `working/scans/*.json`. Collect patterns by routing:
`tension_candidate` → build as TC
`needs_audit` → apply pre-build filter from module, then build as TC if it passes
`rejected_grouping` → append to rejected_groupings.md
`coverage_gap` → append to coverage_gaps.md
`isolated_signal` → append to isolated_signals.md
2. Pre-build filter
Before building any TC from a needs_audit pattern:
If from lexical_overlap scan and <3 Signal IDs → rejected_grouping. Stop.
If from lexical_overlap scan and 3+ IDs but no explicit friction → rejected_grouping. Stop.
If from another scan and <3 IDs → proceed but add "minimal support" to classification_risk.
3. Deduplicate
Before building TCs, check for overlap:
If two patterns from different scans share >70% of their signal_ids, merge ONLY IF they share the same mechanism.
Before merging, verify: do both patterns describe the same blocker/blocked, same axis, or same contradiction?
If patterns come from different scan types (e.g., COO + FRI), verify they are the same phenomenon, not different phenomena sharing cards.
If merge would produce poles without coherent definitions, do NOT merge. Keep as separate TCs.
Note all source patterns in the merged TC.
4. Build each TC
For each tension_candidate or surviving needs_audit pattern:
a. Go to `input/signal_cards_round_*.md` and verify every Signal ID. Read the actual card.
b. If a Signal ID does not exist in the source file, exclude it. Note in classification_risk.
c. If after verification fewer than 2 Signal IDs remain, demote to rejected_grouping.
d. Card-polo relevance check: Before including a card in a pole, verify the card relates directly to the pole's definition. A card from the same round or platform is NOT sufficient reason. If the card describes a different mechanism (e.g., JavaScript scraping in a pole about VBA macros), exclude it.
e. Construct the TC markdown file matching the format of `reference/TC-001.md`:
ID: TC-NNN (starting at TC-002)
Status, Type, Mechanical relation, Analytical unit
Signal IDs list
Structured support with Poles
Additional context (if applicable)
What it supports (yes/no)
What is missing
Classification risk
Human fields (all empty)
f. structured_support MUST use a `poles` array for ALL TC types. Never use top-level keys like `blocker`, `blocked`, `polo_a`, or `polo_b`. The correct structure is always:
```json
"structured_support": {
  "poles": [
    { "label": "...", "definition": "...", "signal_ids": [...], "mechanical_summary": "...", "unit_used": "..." },
    { "label": "...", "definition": "...", "signal_ids": [...], "mechanical_summary": "...", "unit_used": "..." }
  ]
}
```
For friction TCs: use the pole `label` to indicate the role, e.g. "Blocker — restricción técnica de descarga en app móvil" and "Blocked — compradores sin acceso y vendedores absorbiendo soporte".
For co-occurrence TCs: use "Polo A — ..." and "Polo B — ...".
For contradictions, asymmetries, opposite directions: use "Polo A — ..." and "Polo B — ...".
g. Validate the constructed TC against `schemas/tension_candidate.schema.json`.
h. Write to `output/tension_candidates/TC-NNN.md`.
5. Build secondary outputs
`output/rejected_groupings.md`: all rejected grouping patterns.
`output/coverage_gaps.md`: all coverage gap patterns.
`output/isolated_signals.md`: all isolated signals.
6. Build review queue
Write `output/review_queue.md` listing every TC with:
ID, type, status, number of signal IDs, validation status (pending until validator runs).
Construction rules — field by field
These rules are mandatory. If a TC violates any of them, it is malformed.
Polo definition vs mechanical_summary — NOT the same
definition: what groups this pole in corpus terms. Example: "Sellers with high visible outcomes in the corpus."
mechanical_summary: where the cases come from (which rounds, which source types), what is not normalized, what they mix. Example: "Cases from rounds 4, 5, 10. Sources: Medium blogs, Substack newsletters, podcast interviews. Mix of self-reported monthly income and lifetime revenue. Not normalized by time period, audience size, or platform."
If definition and mechanical_summary contain identical text, the TC is malformed. Fix before outputting.
unit_used — declare specific units
NEVER write "mixed" or "mixed (ver classification_risk)."
ALWAYS list the specific units present. Example: "monthly income (USD), lifetime revenue (USD), visitor counts, fee percentages, listing counts."
If units are incompatible, declare which ones and note it.
analytical_unit — what you compare and what you separate
Analytical unit describes WHAT is being compared and WHAT is excluded from the analysis.
Example: "reported seller outcomes by platform, separated from marketplace distribution context."
NEVER include admission rules like "Both poles have 2+ cards support." That is a generation rule, not an analytical unit.
Signal ID descriptions — no truncation
Maximum 120 characters per description.
Cut at complete word boundary. If it doesn't fit, write a shorter summary.
NEVER produce descriptions ending mid-word ("becau", "produ", "transactio").
what_it_supports — specific to THIS candidate
yes: describe what SPECIFIC relationship the cards of THIS candidate show. Not "Coexistence of documented patterns."
Example yes: "Cards document that Etsy's mobile app does not support digital downloads AND that sellers report this as their #1 support request AND that buyers leave negative reviews citing inability to access files."
no: describe what SPECIFIC inference cannot be drawn from THIS candidate's cards.
Example no: "Does not establish what proportion of transactions are affected. Does not establish whether this has improved over time."
what_is_missing: list what is missing for THIS candidate specifically.
Example: "Buyer complaint rate relative to total transactions. Data from platforms other than Etsy. Temporal trend (is this improving?)."
CRITICAL: if what_it_supports.yes, what_it_supports.no, or what_is_missing text is identical between two different TCs, at least one is wrong. Every TC has a different mechanism — its fields must reflect that.
additional_context — separate context from direct evidence
If a TC has >10 Signal IDs, check whether some cards are marketplace context (traffic stats, platform user counts, general pricing data) vs direct evidence of the mechanism (the specific blocker, the specific blocked, the specific contradiction).
Cards that provide context but are not direct evidence of the poles go in `additional_context`, NOT in the poles.
This prevents pole inflation with loosely related cards.
Every Signal ID in additional_context MUST have a parenthetical description. Look up the card in `working/index/card_index.jsonl` and use the `observation` field. Maximum 120 characters, cut at complete word boundary. Never produce bare IDs without descriptions in additional_context.
In the JSON, additional_context.signal_ids must be an array of objects: `[{"id": "SC-R4-001", "description": "..."}, ...]`.
In the .md, each context ID must appear as: `- SC-R4-001 (description here)`.
The top-level signal_ids list in the .md "Signals that support it" section may list IDs without descriptions (they get descriptions inside the poles or additional_context sections), but every ID in the JSON signal_ids array MUST appear with a description somewhere in the .md file — either in a pole or in additional_context.
Format reference
Use `reference/TC-001.md` as the exact format template. Match its structure section by section.
