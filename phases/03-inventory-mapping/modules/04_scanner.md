Module 04 — Scanner
Purpose
Run 7 mechanical operations over the card index. Each produces a scan artifact. These artifacts feed the candidate builder.
Input
`working/index/card_index.jsonl`
Output
`working/scans/contradictions.json`
`working/scans/asymmetries.json`
`working/scans/frictions.json`
`working/scans/co_occurrences.json`
`working/scans/gaps.json`
`working/scans/opposite_directions.json`
`working/scans/lexical_overlap.json`
All validate against `schemas/scan_artifact.schema.json`.
Operations
1. Contradictions
Find pairs of cards that affirm opposite things about the same subject.
Both cards must reference the same entity, platform, or topic.
The opposition must be explicit, not inferred.
Minimum 2 cards per pattern.
2. Asymmetries
Find axes where distribution is unequal with support on both ends.
Identify the axis (e.g., seller outcomes, platform adoption, pricing).
Both poles must have card support.
Unequal distribution is not contradiction.
3. Frictions
Find cards where something blocks or hinders without being a contradiction.
The blocking element must be documented in cards.
The thing being blocked must also be documented.
Pure complaints without documented mechanism are not friction.
4. Co-occurrences
Find cards that appear together consistently around the same topic.
Minimum 3 cards co-occurring.
Co-occurrence must span at least 2 different rounds or sources.
Must generate a plausible DT question to route as tension_candidate.
If no DT question → route as rejected_grouping.
5. Gaps
Find areas where you would expect cards and there are none.
Base expectation on what the corpus covers vs what is absent.
A gap must limit the reading of the inventory to count.
Report what is missing, not what is present.
6. Opposite directions
Find forces pushing in contrary directions documented across cards.
Both directions must have card support.
Different from contradiction: these are not about the same fact, but about different forces acting on the same system.
7. Lexical overlap
Find cards that share vocabulary or territory and might be the same phenomenon described differently.
Flag for deduplication awareness, not as tension.
Default routing is `rejected_grouping`. Only route as `tension_candidate` if explicit friction exists between the overlapping cards.
Cap rule (applies to ALL operations)
If a pattern accumulates >30 Signal IDs, it is too broad to be a workable tension. Before routing:
Split by sub-mechanism (e.g., "Etsy mobile app download limitation" separate from "buyer confusion about digital vs physical").
Or split by platform (e.g., separate Etsy friction from Gumroad friction).
Each sub-pattern must have its own coherent mechanism with its own Signal IDs.
Do not produce monolithic cross-platform patterns. A pattern with 100+ IDs is an unscoped aggregation, not a tension.
Routing rules per pattern
Each pattern gets a routing decision:
`tension_candidate`: meets at least one Candidate Generation Rule from the canon.
`rejected_grouping`: frequency without friction.
`coverage_gap`: relevant absence.
`isolated_signal`: single card, rare, preserved.
`needs_audit`: partial support, unclear classification.
Routing authority

Routing has two layers, and they do not live in the same place.

Mechanical rules are computed by `phases/03-inventory-mapping/scripts/scan_router.py`, which is the single writer of all routing outputs. A scan skill does not apply them and must not restate them. Two rules are mechanical today:

- Same-actor: a pattern whose `signal_ids` all resolve to a single `actor` value in `card_index.jsonl` is routed to `rejected_grouping` with `reason_code: same_actor`. This applies ONLY to the four scans whose patterns have two poles — asymmetries, contradictions, frictions, opposite_directions. Co-occurrences, gaps and lexical overlap are excluded by design (declared in commit `bbda31a9`, the commit that introduced the filter); applying it there would discard legitimate coverage gaps.
- Insufficient IDs: lexical overlap patterns with fewer than 3 Signal IDs, and any pattern left with fewer than 2 after verification, are routed to `rejected_grouping` with `reason_code: insufficient_ids`.

Judgment rules stay with the scan skill, which emits its routing plus a closed `reason_code` from `pipeline_vocabulary.yaml`: `no_dt_question`, `no_explicit_friction`, `dedup_same_source`, `overlap_existing_tc`, `coverage_signal`. The router transports these unchanged. `coverage_signal` re-routes the pattern to the coverage gaps output — a pattern that documents an absence is not a rejection.

Why the split. A rule copied into each skill drifts silently and cannot be verified. Measured on the v4 run: two frictions patterns whose Signal IDs all shared one actor were emitted as `tension_candidate` and `needs_audit` while duplicate `-REJECTED` twins of the same patterns existed alongside them. The copied filter was not only duplicated, it was failing inside its own scan with nothing to detect it. A single writer makes silent discards structurally impossible rather than detectable, and makes the mechanical outcome recomputable when the index changes.

Operator overrides live in `routing_overrides.json` next to the scan artifacts and are applied after the mechanical rules; each entry cites the decision that authorizes it.
Fail states
Index file empty or unreadable → fail scan, report.
Scan produces zero patterns → valid result (no patterns found), not a failure.
Pattern has fewer than 2 signal_ids → invalid, do not include.
Notes
Each scan runs independently. They can run in any order.
A card can appear in multiple scan outputs. No forced exclusivity.
Do not merge scans. Each produces its own artifact file.
