---
title: Epistemic Warrant and Semantic Registration
type: concept
created: 2026-06-21
updated: 2026-07-15
status: current
confidence: high
sources:
  - architectonic-rigor-complete.md
  - triadic-structure-of-relating-rev-canonical.md
  - _compiler/03-architectonic-rigor-semantic-inventory.md
  - _compiler/07-claim-status-vocabulary-semantic-inventory.md
---

# Epistemic Warrant and Semantic Registration

The corpus uses a two-axis epistemology. Framework warrant and semantic registration answer different questions and may never be placed on one ladder.

## Axis 1 — framework standing and warrant

This axis asks: **what exact claim has the framework secured, by what route, and within what scope?**

### Epistemic state

- **Open** — the exact claim or joint is unresolved.
- **Conjectured** — the exact claim is a live proposal but has not been secured.
- **Secured** — the exact claim has been established within its stated scope by a named warrant route.

`Secured` is not generic provenness or maximal certainty. Its meaning is fixed by the route and the distance that route travels.

### Foundational premise category

- **Pure posit** — a premise adopted straightforwardly as a foundation, with no derivation or defense claimed. It is not an epistemic state, not Conjectured, not Secured, and not an incomplete defended posit. Record it as **Category: Pure posit; Warrant: none claimed**, then state it as a condition on every downstream result that depends on it.

Primitive relating — nothing stands beneath relating — is the canonical pure posit. It is **Native** on the registration axis.

### Warrant record

Every Secured claim must name its route, reach, conditions, and debts. Examples:

- **retorsion-secured** — ineliminability; not exhaustiveness;
- **dependency-secured** — priority, independence, or co-constitution;
- **constructed** — genesis from secured priors, as far as the construction is complete and smuggle-free;
- **selected** — licensed contingency under an explicit boundary;
- **theorem-secured** — consequence within named premises and rules;
- **defended posit** — maximal honest warrant at a completeness ceiling, with its defense profile;
- **empirically secured** — observational warrant, not framework derivation.

These routes are not interchangeable levels of one confidence scale. They secure different kinds of claims.

Exactly-three is the canonical defended-posit example. Its completed profile secures the claim within the completeness ceiling: retorsion blocks reduction below three, recorded candidate fourths fail to establish a peer office, and the defense is reflexively stable. The claim is therefore **Secured within that ceiling**, not “merely posited” or epistemically Open. It remains refutable by one genuine irreducible fourth office, and that refutability does not downgrade its present state. The concept and office names are **Native**; registration contributes nothing to this warrant.

A novel framework-native concept can therefore be fully secured without being Registered. Example record:

```text
Epistemic state: Secured
Warrant: retorsion
Reach: ineliminability of the stated claim
Limit: exhaustiveness not supplied by retorsion
Registration: Native
```

## Axis 2 — semantic registration

This axis applies only to the use of inherited or legacy conceptual language. It asks: **what familiar name, if any, may be used for the framework-secured content, and what semantic remainder remains quarantined?**

- **Native** — no inherited name is invoked or needed.
- **Unregistered** — a resemblance or candidate mapping may exist, but the inherited name is not licensed for forward use.
- **Registered** — a framework-secured core captures enough of an inherited concept's semantic content to license the familiar name. Only the explicitly mapped core may be spent. Every unmapped legacy implication remains quarantined.
- **Registered–Sealed** — within an explicit scope, the framework object and the properly stripped inherited concept are bidirectionally content-identical. There is no semantic remainder in either direction.

The historical spelling `Registered and Sealed` means `Registered–Sealed`.

### Compact definitions

> **Registered:** inherited name licensed over an explicitly mapped, framework-secured core; unmapped legacy surplus remains quarantined.

> **Registered–Sealed:** inherited name closed by bidirectional content-identity within scope; no remainder in either direction.

Registration is not an estimate of how well proved a claim is. A concept may be Registered when only a semantically sufficient portion of the inherited concept has been derived. The percentage of ordinary content derived is illustrative only; the governing object is the explicit semantic boundary.

### Registration invariants

1. Registration requires a Secured mapped core.
2. Registration contributes no epistemic warrant and cannot upgrade a claim's epistemic state.
3. Every downstream use of a Registered name must verify that it spends only the licensed core.
4. Registered–Sealed removes that surplus audit only within the sealed scope.
5. Contextual associations outside the properly stripped concept remain excluded even after a scoped registration seal.
6. A Native concept is not deficient or incomplete merely because registration is inapplicable.

### The two uses of “seal”

The source corpus uses `seal` in two distinct operations:

- **sealed recognition** — attach an inherited name while quarantining its unearned surplus; this yields **Registered** use;
- **sealed registration** — close the correspondence by bidirectional content-identity; this yields **Registered–Sealed**.

Operational prose should call the first **recognition with surplus quarantined** and reserve **Registered–Sealed** for correspondence closure.

## Administrative metadata

Record these separately from both axes:

- warrant strength;
- inherited conditions and parent debts;
- evidence or test state;
- confidence;
- workflow or deposit state;
- disposition: dissolved, retracted, superseded, quarantined, or historical.

## Required translations

- **Conjectured-strong** → epistemic state **Conjectured** plus warrant-strength metadata.
- **Registered-candidate** → decompose into an epistemic state, registration state, and candidate/deposit workflow state; never infer any one of them from the compound label.
- **Defended posit** → warrant profile; when its defense is complete, record the exact claim as **Secured** within that warrant's ceiling.
- **Registered, not Sealed** → registration state **Registered**, with licensed core and quarantined surplus stated.
- **Registered conditional on X** → state the epistemic state and warrant conditions separately from the registration state; X and every inherited debt remain explicit.
- **Registered structural / representational** → registration state **Registered** with the licensed scope made explicit.
- **Registered program / Open values** → split the program claim from the value claims and grade each on both axes.
- **Derived with empirical input** → state the epistemic result, framework route, empirical input, and registration separately.
- **Lead** → research/workflow metadata.
- **Dissolved**, **retracted**, **superseded**, **quarantined**, and **historical** → dispositions.
- **Current**, **control**, and **mature** → document lifecycle metadata.
- **Forced**, **checked**, **argued**, **verified**, and **theorem** → warrant or evidence vocabulary.
- **Locked actual** → deprecated package-era conflation; translate claim by claim through [locked-actual-decrement-map](locked-actual-decrement-map.md).

Ambiguous compounds such as `Open or Conjectured` must be resolved or split. They are not canonical final records.

## Minimal operating record

```text
Claim:
Epistemic state: Open | Conjectured | Secured
Warrant route and reach:
Scope / conditions / debts:
Registration: Native | Unregistered | Registered | Registered–Sealed
Licensed legacy content:        # required when Registered
Quarantined legacy surplus:     # required when Registered
Framework remainder:            # required when correspondence is incomplete
Evidence / confidence / workflow / disposition:  # only where relevant
```

For Registered–Sealed:

```text
Correspondence: bidirectional content-identity
Remainder: none within scope
```

## Execution rule

Never upgrade a claim by paraphrase, and never use registration as evidence of proof. For every inherited name, distinguish what the framework secured from what the name conventionally carries. If the surplus boundary is not stated, the Registered name may not bear downstream load.

See also: [agent-execution-rules](agent-execution-rules.md), [known-failure-modes](known-failure-modes.md), [locked-actual-decrement-map](locked-actual-decrement-map.md), [architectonic-rigor](architectonic-rigor.md), and [entering-a-new-domain](entering-a-new-domain.md).
