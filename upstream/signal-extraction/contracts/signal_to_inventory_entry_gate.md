# Signal to Inventory Entry Gate

## Purpose

Controlar qué Signal Cards pueden pasar de Signal Extraction a Inventory Mapping.

Este gate existe para evitar que Inventory Mapping reciba material que ya viene:

- interpretado
- compuesto
- mal trazado
- sin sujeto exacto
- con niveles colapsados
- o demasiado débil para servir como unidad observacional

Inventory Mapping debe recibir **observaciones discretas**, no mini-síntesis ni proto-tensiones.

---

## Inputs

Read:
- `Signal Cards`
- `Signal Extraction Validation Results`

Optional references:
- `signal_card.schema.json`
- `Signal Extraction Contract v0.1`
- `Signal Extraction Validator`

---

## Outputs

Allowed routing outputs:

- `pass_to_inventory_mapping`
- `preserve_as_isolated_signal`
- `return_to_signal_rework`
- `reject_from_inventory_input`

Optional artifacts:
- `entry_gate_report.json`
- `isolated_signals.json`
- `rework_queue.json`
- `rejected_signals.json`

---

## Core decision principle

A Signal Card should pass to Inventory Mapping only if it is:

1. **observational**
2. **discrete**
3. **traceable**
4. **locally bounded**
5. **not already doing Inventory Mapping’s job**

If a Signal Card already sounds like a pattern, tension, contradiction, asymmetry, or market reading, it should not pass cleanly.

---

## Required checks

### 1. Validation status check

#### Pass if
The Signal Card validation result is:
- `pass`
- or `pass_with_flags`

#### Return to rework if
The Signal Card validation result is:
- `rework`

#### Reject if
The Signal Card validation result is:
- `reject`

#### Rule
No Signal Card may pass if validator already marked it as interpretive, cross-source synthetic, or untraceable.

---

### 2. Discreteness check

#### Question
Is this one observational unit, or a fused bundle?

#### Pass if
- one clear local observation is centered
- subordinate context does not create a second main claim

#### Preserve as isolated if
- the card is discrete but too weak, too isolated, or too niche to route into pattern detection immediately

#### Return to rework if
- multiple local claims were fused
- it should be split into 2+ Signal Cards

#### Reject if
- the card is so broad or fused that local recovery is no longer realistic

---

### 3. Observational boundary check

#### Question
Does the card remain observational, or has it drifted into interpretation?

#### Pass if
- signal text describes what was observed locally
- no pattern-level language is present

#### Return to rework if
- wording is slightly interpretive but recoverable

#### Reject if
- the card already asserts contradiction, friction, asymmetry, gap, pattern, or importance

#### Red-flag language
- reveals
- demonstrates
- suggests that
- confirms that
- implies that
- the corpus shows
- many sellers report
- platforms split into
- there is a tension between

---

### 4. Subject exactness check

#### Question
Can Inventory Mapping safely work with this subject without having to reconstruct it?

#### Pass if
- `subject_exact` is narrow and usable
- meaningful distinctions remain intact

#### Preserve as isolated if
- subject is narrow, but the card is too weak or sparse for pattern routing

#### Return to rework if
- subject is recoverable but too broad
- critical functional distinctions were flattened

#### Reject if
- subject is effectively theme-level only

---

### 5. Actor level and analysis level check

#### Question
Can Inventory Mapping trust the level of analysis on this card?

#### Pass if
- buyer / seller / product / marketplace level is explicit
- mixed level is real and marked

#### Return to rework if
- actor level is flattened but recoverable

#### Reject if
- level collapse destroys the meaning of the card

#### Important note
Inventory Mapping can compare across cards later.
This gate only ensures that each card arrives with its own level intact.

---

### 6. Time and qualifier preservation check

#### Question
Did the card preserve temporal and conditional boundaries enough to remain safe?

#### Pass if
- `time_scope_raw` is present or uncertainty is explicit
- important qualifiers are preserved

#### Preserve as isolated if
- the card is valid but time/qualifier weakness makes broader grouping risky

#### Return to rework if
- qualifiers were dropped but recoverable from extraction
- time scope got blurred but can be restored

#### Reject if
- loss of time or qualifier changes the meaning too much

---

### 7. Cross-source contamination check

#### Question
Is this still source-local enough to be treated as a signal?

#### Pass if
- it does not summarize multiple unrelated sources
- it does not talk about “many sellers,” “multiple sources,” or “overall”

#### Return to rework if
- a local observation was phrased too broadly but can be localized again

#### Reject if
- the card is already a cross-source meta-observation

---

### 8. Pattern-readiness check

#### Question
Is this card usable as input for pattern detection, not just archival preservation?

#### Pass if
- it is discrete
- traceable
- semantically bounded
- not too weak to be noise
- not so narrow that it cannot participate in later grouping

#### Preserve as isolated if
- it is valid and worth keeping
- but likely too singular, sparse, or fragile for pattern-building

#### Return to rework if
- readiness is blocked by formatting, discreteness, or clarity issues

#### Reject if
- it adds no usable observational value

---

## Routing logic

### `pass_to_inventory_mapping`
Use when the Signal Card is:
- validated (`pass` or `pass_with_flags`)
- discrete
- observational
- traceable
- locally bounded
- not cross-source synthetic
- usable for pattern detection

### `preserve_as_isolated_signal`
Use when the Signal Card is:
- valid and worth keeping
- but too isolated, thin, or non-pattern-ready for Inventory Mapping

Examples:
- rare but potentially useful observation
- one-off seller case with clean traceability
- weak but valid edge-case evidence

### `return_to_signal_rework`
Use when the Signal Card has:
- recoverable interpretation drift
- recoverable subject broadening
- recoverable qualifier/time loss
- fused but splittable local claims

### `reject_from_inventory_input`
Use when the Signal Card is:
- cross-source synthetic
- untraceable
- irrecoverably interpretive
- too fused to salvage
- too degraded to preserve as isolated signal

---

## Failure reasons

Use one or more of:

- `validation_not_passed`
- `signal_not_observational`
- `subject_exact_too_broad`
- `actor_level_not_safe`
- `time_scope_not_safe`
- `qualifier_loss_material`
- `cross_source_meta_observation`
- `multiple_claims_fused`
- `pattern_language_smuggled`
- `too_weak_for_inventory`
- `traceability_not_safe`

---

## Preservation rules for isolated signals

A Signal Card preserved as isolated signal must:
- remain traceable
- remain observational
- retain subject exactness
- keep uncertainties visible
- not be silently promoted later without explicit routing

It may be useful later for:
- gap interpretation
- later corroboration
- edge-case review
- human-selected carryover

But it is not active Inventory Mapping input by default.

---

## Gate report structure (recommended)

For each Signal Card, record:

- `signal_id`
- `validation_status`
- `entry_gate_decision`
- `failure_reasons[]`
- `notes[]`

Example:

```json
{
  "signal_id": "SC-R4-049",
  "validation_status": "pass_with_flags",
  "entry_gate_decision": "pass_to_inventory_mapping",
  "failure_reasons": [],
  "notes": [
    "Time scope remains unclear but uncertainty is preserved."
  ]
}
```

---

## Decision examples

### Example A
Signal Card:
`Gumroad Discover requires at least one sale to activate.`

Decision:
- `pass_to_inventory_mapping`

Reason:
- discrete
- observational
- requirement-local
- good candidate for later contradiction/friction/asymmetry checks

### Example B
Signal Card:
`Multiple sellers report that Gumroad lacks discoverability unless creators already have an audience.`

Decision:
- `reject_from_inventory_input`

Reason:
- cross-source meta-observation
- already pattern language
- not source-local

### Example C
Signal Card:
`A seller reported zero organic views on Gumroad across 25 products.`

Decision:
- `pass_to_inventory_mapping`
or
- `preserve_as_isolated_signal`

Reason:
- observational and traceable, but whether it is pattern-ready depends on corpus density

### Example D
Signal Card:
`Etsy has 95.6M active buyers, therefore sellers benefit from integrated discoverability.`

Decision:
- `return_to_signal_rework`

Reason:
- platform context promoted into seller-side interpretation
- claim can likely be recovered into a cleaner traffic/buyer signal

### Example E
Signal Card:
`Creative Market takes 50% commission, but sellers only keep 20%.`

Decision:
- `reject_from_inventory_input`
or `return_to_signal_rework` depending on recoverability

Reason:
- fused multiple sources/levels
- already pattern-compressed
- needs separation before safe routing

---

## Global rule

Inventory Mapping should receive **clean observational atoms**, not semi-assembled molecules.

If the Signal Card already contains the seeds of a tension in its wording, the gate should be suspicious.

The point is not to maximize throughput.
The point is to protect the next phase from inherited collapse.
