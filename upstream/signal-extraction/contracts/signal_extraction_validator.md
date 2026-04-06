# Signal Extraction Validator

## Purpose

Validate each Signal Card before it can pass to Inventory Mapping.

The validator does **not** decide whether a signal is important.
The validator does **not** build tensions.
The validator does **not** compare cards across the corpus.
The validator does **not** decide what passes to DT.

Its job is narrower:

- verify that the Signal Card remains observational
- verify that it preserves local traceability
- verify that it does not smuggle cross-source synthesis
- verify that it preserves subject, actor level, time scope, and qualifiers
- verify that it has not promoted context into signal
- verify that it has not fused multiple local claims unsafely

---

## Inputs

Read:
- one `Signal Card`

Optional references:
- `signal_card.schema.json`
- `Signal Extraction Contract v0.1`

---

## Output

Produce one validation result per Signal Card.

Allowed validation statuses:
- `pass`
- `pass_with_flags`
- `rework`
- `reject`

Allowed check statuses:
- `pass`
- `flag`
- `fail`
- `not_applicable`

---

## Validator stance

Be strict about observational discipline.

A Signal Card can be clean and still be uninteresting.
A Signal Card can be interesting and still fail.

Prefer:
- preserved uncertainty
- preserved qualifiers
- narrow subject
- explicit mixed level
- rework

Over:
- elegant phrasing
- compressed synthesis
- thematic grouping
- premature pattern language

---

## Core validation principle

A good Signal Card should let Inventory Mapping receive:

1. one discrete observation
2. with local traceability
3. with preserved subject exactness
4. with preserved actor level
5. with preserved metric/time qualifiers
6. without pattern-level interpretation

If Inventory Mapping can already read the Signal Card as a market thesis, the card is probably too cooked.

---

## Validation checks

### 1. Observational wording

#### Question
Does `signal_text` describe a local observation rather than a market reading or interpretation?

#### Pass if
- it describes what was said or observed locally
- it does not explain what the observation means
- it does not mention the corpus, pattern, or importance

#### Flag if
- wording is mostly observational but slightly compressed
- one phrase could be made more local without changing meaning

#### Fail if
- it uses interpretive verbs
- it sounds like a pattern summary
- it sounds like an early tension statement
- it sounds like a design or business implication

#### Red-flag wording
- reveals
- demonstrates
- suggests that
- confirms that
- implies that
- shows a tension
- indicates a market need
- many sellers report
- the corpus shows
- platforms split into

#### Typical failure codes
- `signal_not_observational`
- `downstream_interpretation_smuggled`

---

### 2. Subject exactness preserved

#### Question
Did the Signal Card preserve `subject_exact` without flattening important distinctions?

#### Pass if
- the subject remains narrow and local
- meaningful functional distinctions remain intact

#### Flag if
- the subject is usable but should be narrowed
- one ambiguity remains explicit

#### Fail if
- the subject became broader than the extraction record
- the card collapses meaningful distinctions
- the card turns a precise subject into a theme

#### Typical failure codes
- `subject_exact_lost`
- `checkout_vs_payout_collapsed`
- `net_vs_gross_collapsed`

---

### 3. Actor level preserved

#### Question
Does the Signal Card preserve the level of analysis correctly?

#### Pass if
- buyer, seller, product, marketplace, source remain explicit
- mixed level is marked only when genuinely mixed

#### Flag if
- mixed level is legitimate but not ideal
- one secondary level is present but clearly not central

#### Fail if
- seller-level and marketplace-level are flattened
- platform context is rewritten as seller outcome
- buyer behavior is rewritten as marketplace feature

#### Typical failure codes
- `actor_level_collapsed`
- `platform_vs_seller_level_collapsed`

---

### 4. Time scope preserved

#### Question
Did the Signal Card preserve temporal wording or explicit temporal uncertainty?

#### Pass if
- `time_scope_raw` remains faithful
- normalization is safe or absent
- current vs historical remains visible

#### Flag if
- time is present but only partially usable
- the signal is safe but still needs later time audit

#### Fail if
- time scope was dropped
- a historical statement became current
- a vague temporal phrase was normalized unsafely

#### Typical failure codes
- `time_scope_dropped`
- `normalized_time_unsafe`
- `current_vs_historical_ambiguity`

---

### 5. Qualifiers preserved

#### Question
Were important local qualifiers preserved in the Signal Card?

#### Pass if
- limiting conditions remain visible
- phrases such as `at the time of writing`, `in the US`, `for shops under $10k`, `first 6 months` survive

#### Flag if
- qualifier survives indirectly but should be made more explicit

#### Fail if
- a dropped qualifier materially changes the reading
- the signal becomes broader than the source claim

#### Typical failure codes
- `qualifier_dropped`

---

### 6. Evidence role preserved

#### Question
Does `evidence_role` still match the role the observation plays?

#### Pass if
- direct claim stays direct
- local context stays context
- official policy stays policy
- anecdotal example stays anecdotal

#### Flag if
- the role is plausible but borderline

#### Fail if
- context becomes signal
- commentary becomes direct support
- downstream consequence becomes primary observation

#### Typical failure codes
- `context_promoted_to_signal`
- `evidence_role_unclear`

---

### 7. Single-claim discreteness

#### Question
Is the Signal Card still one discrete observation rather than a fused bundle?

#### Pass if
- one coherent local observation is centered
- supporting context is subordinate

#### Flag if
- a secondary local detail is attached but does not create a second main claim

#### Fail if
- multiple claims are fused
- the card summarizes a whole section or source
- it should have been split into separate Signal Cards

#### Typical failure codes
- `multiple_records_fused_unsafely`
- `local_claim_boundary_broken`
- `insufficient_discreteness`

---

### 8. No cross-source meta-observation

#### Question
Does the card remain local rather than cross-source?

#### Pass if
- the card is grounded in source-local observation
- it does not compare or summarize across sources

#### Fail if
- it says “multiple sellers report”
- it says “the corpus shows”
- it says “sources converge”
- it combines evidence from multiple unrelated sources into one observation

#### Important note
A Signal Card may cite multiple `source_record_ids` only when they belong to the same local fact boundary. It may not become a cross-source synthesis card.

#### Typical failure codes
- `cross_source_meta_observation`
- `multiple_records_fused_unsafely`

---

### 9. Traceability preserved

#### Question
Can I still get back from the Signal Card to the exact extraction/source basis?

#### Pass if
- `source_record_ids` are present
- `traceability_pointers` are usable
- source chain is not weakened

#### Flag if
- traceability is present but coarse

#### Fail if
- signal lost its extraction chain
- traceability became too vague to audit

#### Typical failure codes
- `traceability_weakened`

---

### 10. No tension-smuggling

#### Question
Is the Signal Card doing work that belongs to Inventory Mapping?

#### Pass if
- it stays as an observation
- it does not imply contradiction, friction, asymmetry, or gap

#### Fail if
- the card is already grouping things into a candidate pattern
- it reads like a prebuilt tension
- it anticipates Inventory Mapping language

#### Typical failure codes
- `downstream_interpretation_smuggled`

---

### 11. Notes Locality

#### Question
Do the notes fields contain only local, non-interpretive content?

#### What it verifies
`normalization_notes` and `extraction_notes` must not contain:
- references to other records or findings by ID pattern (`F\d+`, `Finding \d+`, `SC-R\d+-\d+`, `record \d+`)
- cross-source comparison language (`confirmed by`, `consistent with`, `contradicted by`, `corroborated by`, `same as`, `similar to`)
- version comparison language (`earlier version`, `updated from`, `previously stated`)
- interpretive math or reconciliation (digit + operator + digit in a context phrase, or phrases like `this implies`, `this means`, `this works out to`)

#### Failure handling
Route to `pass_with_flags` and emit `notes_interpretive_content` in the failures list. The card continues downstream. The mandatory scrubbing step (below) runs immediately after this validator emits the flag, before the card advances to the Inventory Mapping entry gate.

#### Mandatory scrubbing step
When `notes_interpretive_content` is emitted, the scrubber runs between Signal Extraction validation and the Inventory Mapping entry gate:

1. Read `normalization_notes` and `extraction_notes`.
2. Apply regex-replace to remove matched patterns from the four categories above. For each match, remove the matched substring plus any surrounding conjunction or punctuation that becomes dangling (leading "and", trailing semicolon, orphaned parenthesis).
3. If scrubbing leaves a field empty or reduced to whitespace, set it to an empty array.
4. Write the scrubbed notes back to the card.
5. Append one entry to `working/notes_scrubbing/scrubbing_log.jsonl`: `{record_id, original_notes_hash, scrubbed_notes_hash, patterns_matched}`.

The scrubber does not re-run the validator after scrubbing. It does not modify any field other than `normalization_notes` and `extraction_notes`. If the only content was forbidden content, the field is left as an empty array.

#### Typical failure codes
- `notes_interpretive_content`

---

## Decision rules

### Use `pass` when
- all critical checks pass
- no structural failure codes are triggered
- remaining uncertainty is explicit and minor

### Use `pass_with_flags` when
- the Signal Card is usable
- but one or more non-fatal issues remain visible
- later phases can still work safely if they respect the flags

Typical examples:
- time scope preserved but still unclear
- actor level is mixed and explicitly marked
- one subject ambiguity remains preserved

### Use `rework` when
- the card contains real value
- but it needs structural repair before Inventory Mapping

Typical rework-worthy problems:
- wording drifts slightly interpretive
- subject widened too much
- context promoted too far
- discreteness not clean
- qualifiers missing but recoverable from extraction

### Use `reject` when
- the card is already a cross-source synthesis
- traceability is broken
- the card is mostly interpretation
- the card fuses several claims beyond safe repair
- it is no longer meaningfully observational

---

## Failure severity guide

### Usually `reject`
- `cross_source_meta_observation`
- `downstream_interpretation_smuggled`
- `traceability_weakened` when severe
- `signal_not_observational`

### Usually `rework`
- `subject_exact_lost`
- `actor_level_collapsed`
- `time_scope_dropped`
- `qualifier_dropped`
- `context_promoted_to_signal`
- `insufficient_discreteness`

### Depends on recoverability
- `multiple_records_fused_unsafely`
- `platform_vs_seller_level_collapsed`
- `checkout_vs_payout_collapsed`
- `net_vs_gross_collapsed`

---

## Notes discipline

Notes may explain:
- what failed
- why it failed
- what should be repaired

Notes must not:
- interpret the market
- say the signal is important
- propose a tension
- recommend a business opportunity
- compare it to other signals

---

## Rework instruction discipline

Good rework instructions are local and mechanical.

Good:
- `Narrow signal_text back to one local observation`
- `Restore qualifier 'in the US' from extraction`
- `Split policy statement from seller anecdote into separate Signal Cards`
- `Keep traffic metric as traffic_signal; do not rewrite as seller discoverability claim`

Bad:
- `Make it better`
- `Clarify`
- `Needs more rigor`
- `Too broad`

---

## Example evaluation patterns

### Example 1
Signal text:
`Multiple sellers report that Gumroad lacks discoverability unless creators already have an audience.`

Likely result:
- observational wording: fail
- no cross-source meta-observation: fail
- no tension-smuggling: fail
- status: `reject`

Reason:
This is already corpus-level synthesis, not a signal.

### Example 2
Signal text:
`A seller reported that after one year on Gumroad selling Notion templates, most early sales came from their own audience rather than from platform discoverability.`

Likely result:
- observational wording: pass
- subject exactness: pass
- actor level: pass
- time scope: pass_with_flags if date unclear
- status: `pass` or `pass_with_flags`

Reason:
It stays local, seller-level, and observational.

### Example 3
Signal text:
`Etsy has 95.6M active buyers, so sellers benefit from integrated discoverability.`

Likely result:
- observational wording: fail
- evidence role: fail
- actor level: fail
- status: `rework` or `reject`

Reason:
Platform context got promoted into seller-side interpretation.

---

## Global rule

If the validator has to mentally “undo” a summary in order to recover a local observation, the Signal Card is not clean.

Signal Extraction exists to preserve discrete observations.
Inventory Mapping exists to discover patterns.
Do not let Signal Cards do both jobs.
