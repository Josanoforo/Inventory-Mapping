# Data Extraction Validator

## Purpose

Validate each Data Extraction Record before it can pass downstream to Signal Extraction.

The validator does **not** evaluate strategic importance.
The validator does **not** compare records across sources.
The validator does **not** decide whether a record is a signal, a tension, or an opportunity.

Its job is narrower:

- verify traceability
- verify local claim integrity
- verify preservation of subject, actor level, metric, and time scope
- verify that ambiguity was preserved instead of flattened
- detect when context was upgraded into claim
- detect when the record is already doing downstream interpretation

---

## Inputs

Read:
- one `Data Extraction Record`

Optional references:
- `data_extraction_record.schema.json`
- `Data Extraction Contract v0.1`

---

## Output

Produce one `Data Extraction Validation Result` per record.

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

Be conservative.

If a record looks clean but required hidden interpretation to become clean, it is **not** clean.

Prefer:
- explicit uncertainty
- narrow subject
- preserved qualifiers
- rework

Over:
- elegant normalization
- silent repair
- semantic smoothing

---

## Core validation principle

A good Extraction Record should allow a later phase to understand:

1. what the source says locally
2. about what exact subject
3. at what level of analysis
4. with what metric or condition
5. in what time scope
6. under what qualifiers
7. with what unresolved ambiguity

If the record cannot preserve those, it is not ready.

---

## Validation checks

### 1. Traceability

#### Question
Can I go back to the exact source location without guessing?

#### Pass if
- `traceability_pointer` is present
- it points to a real retrievable source location
- `snippet_primary` matches the pointed location

#### Flag if
- traceability exists but is coarse
- pointer gets you to the document but not to a precise section
- snippet is locally correct but surrounding context is hard to recover

#### Fail if
- there is no usable pointer
- pointer is broken, missing, or too vague
- snippet cannot be verified from the source

#### Typical failure codes
- `source_not_traceable`

---

### 2. Subject Exactness

#### Question
Does `subject_exact` name the local subject precisely enough, without flattening important distinctions?

#### Pass if
- the subject is narrow and local
- it distinguishes meaningful functional layers
- it matches what the snippet actually says

#### Flag if
- the subject is usable but could be narrower
- one ambiguity remains visible but preserved

#### Fail if
- the subject is generic or theme-like
- it collapses distinctions that matter downstream
- it says less than the source, not just more cleanly

#### Good examples
- `Gumroad Discover activation requirement`
- `PayPal as checkout payment method in Gumroad`
- `Creative Market seller commission base rate`

#### Bad examples
- `traffic`
- `fees`
- `PayPal in Gumroad`
- `seller outcomes`

#### Typical failure codes
- `subject_exact_lost`
- `checkout_vs_payout_collapsed`
- `net_vs_gross_collapsed`

---

### 3. Actor Level

#### Question
Is the record clear about who or what level the claim is about?

#### Pass if
- `actor_level` is clearly set
- buyer, seller, product, marketplace, source are not flattened

#### Flag if
- mixed level is real and explicitly marked as `mixed`
- one secondary level is present but not central

#### Fail if
- levels are collapsed
- actor level is implied but not marked
- platform-level context is treated as seller-level claim

#### Typical failure codes
- `actor_level_collapsed`
- `platform_vs_seller_level_collapsed`

---

### 4. Claim Type

#### Question
Does `claim_type` describe the local statement, not a downstream interpretation?

#### Pass if
- it names what kind of local statement the record contains
- it does not interpret the statement

#### Flag if
- more than one claim type could fit, but one safe type was chosen conservatively

#### Fail if
- the claim type already implies contradiction, friction, importance, or opportunity
- the record is describing what the validator thinks the claim means, not what kind of claim it is

#### Good examples
- `policy_statement`
- `anecdotal_report`
- `derived_calculation`
- `availability_statement`

#### Bad examples
- `contradiction`
- `friction`
- `evidence of need`
- `market opportunity`

#### Typical failure codes
- `claim_type_interpretive`

---

### 5. Metric and Unit

#### Question
Did the record preserve metric type and unit without collapsing incompatible quantities?

#### Pass if
- metric is explicit and faithful
- unit is explicit or safely marked as unclear
- gross vs net, payout vs price, revenue vs profit remain distinct

#### Flag if
- metric is present but one part remains ambiguous and is marked in uncertainties

#### Fail if
- metric type was guessed
- unit was invented
- incompatible metrics were merged
- event conditions were turned into quantities or vice versa

#### Typical failure codes
- `metric_type_mixed`
- `metric_unit_invented`
- `net_vs_gross_collapsed`

---

### 6. Time Scope

#### Question
Did the record preserve temporal scope and avoid unsafe normalization?

#### Pass if
- `time_scope_raw` preserves the original temporal wording
- normalization is applied only when safe
- historical vs current remains visible

#### Flag if
- source date exists but present relevance is uncertain
- timeframe is partial but uncertainty is preserved

#### Fail if
- time scope was dropped
- historical claim was rewritten as current
- normalized time was invented from vague wording

#### Typical failure codes
- `time_scope_missing`
- `normalized_time_unsafe`
- `current_vs_historical_ambiguity`

---

### 7. Evidence Role

#### Question
Did the record correctly distinguish direct claim, context, consequence, policy, anecdote, or commentary?

#### Pass if
- `evidence_role` matches the role the snippet is playing locally

#### Flag if
- the role is plausible but borderline between two safe categories

#### Fail if
- context is treated as direct claim
- downstream consequence is treated as primary support
- commentary is treated as policy
- platform scale metric is treated as direct discoverability claim

#### Typical failure codes
- `context_as_claim`
- `evidence_role_unclear`

---

### 8. Qualifiers

#### Question
Were important qualifiers preserved?

#### Pass if
- limiting conditions remain visible
- phrases like `at the time of writing`, `in the US`, `for shops under $10k`, `first 6 months` survive

#### Flag if
- qualifier is preserved indirectly but could be made clearer

#### Fail if
- qualifier disappeared
- loss of qualifier changes the reading materially

#### Typical failure codes
- `qualifier_dropped`

---

### 9. Uncertainties

#### Question
Were genuine ambiguities preserved rather than silently resolved?

#### Pass if
- uncertainties are explicit when needed
- `unknown` or the correct ambiguity tag is used

#### Flag if
- uncertainty exists but is too coarsely described

#### Fail if
- ambiguity is visible in the snippet but absent in the record
- the record chose one interpretation without basis

#### Typical failure codes
- `uncertainty_hidden`

---

### 10. No Cross-Source Synthesis

#### Question
Does the record remain local to one source?

#### Pass if
- the record only represents one source
- no cross-source statements appear

#### Fail if
- it references contradiction with another source
- it says “most sources,” “overall,” “across platforms,” or similar cross-source framing
- it merges content from multiple sources

#### Typical failure codes
- `cross_source_synthesis_smuggled`

---

### 11. Single-Claim Boundary

#### Question
Does the record preserve one coherent local claim, rather than fusing several?

#### Pass if
- one local claim is clearly centered
- surrounding context supports that claim without introducing a second major claim

#### Flag if
- one secondary claim exists but is clearly subordinate

#### Fail if
- multiple primary claims are fused
- a long summary blob replaced several distinct source claims
- the record should have been split into 2+ records

#### Typical failure codes
- `multiple_claims_fused`

---

## Decision rules

### Use `pass` when
- all critical checks pass
- no failure code is triggered
- remaining uncertainty is minor and already explicit

### Use `pass_with_flags` when
- the record is usable downstream
- but one or more non-fatal ambiguities remain
- uncertainty was preserved honestly

Typical examples:
- subject is precise but one functional ambiguity remains
- source date exists but current relevance is unclear
- actor level is mixed and explicitly marked

### Use `rework` when
- the record contains real value
- but a recoverable structural problem remains

Typical rework-worthy problems:
- subject too broad
- actor level flattened
- evidence role wrong but recoverable
- time scope missing from normalized field but present in source
- qualifier preserved in snippet but not surfaced in record

### Use `reject` when
- source is not traceable
- record already performs downstream interpretation
- multiple claims are fused beyond safe recovery
- cross-source synthesis was smuggled in
- dropped qualifiers change the meaning materially

---

## Failure severity guide

### Usually `reject`
- `source_not_traceable`
- `cross_source_synthesis_smuggled`
- `claim_type_interpretive`

### Usually `rework`
- `subject_exact_lost`
- `actor_level_collapsed`
- `time_scope_missing`
- `evidence_role_unclear`
- `qualifier_dropped`
- `metric_type_mixed`
- `uncertainty_hidden`

### Depends on local recoverability
- `multiple_claims_fused`
- `checkout_vs_payout_collapsed`
- `net_vs_gross_collapsed`
- `platform_vs_seller_level_collapsed`

---

## Validator notes discipline

Notes are allowed only for:
- what failed
- why it failed
- how to repair it

Notes must NOT:
- speculate about market meaning
- call something important
- suggest downstream opportunity
- compare across sources
- recommend DT treatment

---

## Rework instruction discipline

A good rework instruction tells the upstream system exactly what to fix.

Good:
- `Narrow subject_exact to checkout payment method rather than PayPal in Gumroad`
- `Split this into two records: commission base rate and seller-reported net retained after taxes`
- `Preserve source timeframe wording in time_scope_raw`

Bad:
- `Make clearer`
- `Improve quality`
- `Fix wording`
- `Needs more detail`

---

## Example evaluation pattern

### Example
Record says:
- subject: `PayPal in Gumroad`
- claim_type: `contradiction`
- snippet: blog mentions PayPal or Stripe processing fees
- no uncertainty marked

### Validator outcome
- `subject_exact`: fail
- `claim_type`: fail
- `uncertainties`: fail
- overall status: `reject` or `rework` depending on source traceability and recoverability

Reason:
The record already collapsed function and introduced downstream interpretation.

---

## Global rule

If the validator has to “understand what the record probably meant” in order to pass it, the record should not pass cleanly.

The validator is not there to be generous.
It is there to preserve epistemic discipline.
