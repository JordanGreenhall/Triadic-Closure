---
title: Claim Status Vocabulary
type: concept
created: 2026-06-21
updated: 2026-07-15
status: current
confidence: high
sources:
  - architectonic-rigor-complete.md
  - triadic-structure-of-relating-rev-canonical.md
  - verification-companion.md
  - _compiler/03-architectonic-rigor-semantic-inventory.md
  - _compiler/07-claim-status-vocabulary-semantic-inventory.md
---

# Claim Status Vocabulary

Claim standing, warrant route, warrant strength, conditions, confidence, evidence state, workflow state, and disposition are separate fields. No label may migrate from one field into another by compression.

## Live claim standings

The corpus has exactly four claim standings:

- **Open** — explicitly not closed; a live claim, dependency, or joint on the work frontier. It may be named but not spent downstream as closed.
- **Conjectured** — a plausible live proposal not yet registered by the framework.
- **Registered** — the framework reaches the claim in essence or under explicit conditions, while sealing, uniqueness, bidirectional identity, or full closure remains incomplete.
- **Registered and Sealed** — within an explicit scope, the framework object and the properly stripped recognized content carry no unearned surplus relative to one another.

Sealing is scope-sensitive. It does not automatically seal associated theorems, numerical values, extensions, or conventional meanings.

## Orthogonal metadata

Record these separately from standing:

- **Warrant route** — how the claim was reached: retorsion, dependency, construction, selection, sealed recognition, formal theorem, calculation, empirical input, or another explicitly named instrument.
- **Warrant profile** — for example, **defended posit**: the maximal honest warrant for an exact-totality claim at the completeness ceiling, with its defense stated. A defended posit still requires one of the four live standings.
- **Warrant strength** — qualifiers such as strong; they do not create new standings.
- **Conditions and inheritance** — premises, scope restrictions, imported theorems, empirical inputs, and unresolved parent debts that must travel with the claim.
- **Evidence or test state** — checked, machine-verified, argued, adversarially tested, finite-range, or similar. A test result is not a standing.
- **Confidence** — confidence in the grading or argument; never a substitute for standing or warrant.
- **Workflow state** — candidate, deposit, awaiting adversarial pass, awaiting sign-off, or implementation state. **Registered-candidate** is a workflow/admission label, not a fifth standing.
- **Disposition** — dissolved, retracted, superseded, quarantined, or historical. **Dissolved** means a demand or problem was removed as a category error; no surviving proposition is thereby assigned a fifth standing.

## Required translations

- **Conjectured-strong** → **Conjectured** plus `warrant-strength: strong`.
- **Registered-candidate** → state one of the four standings separately and record candidate/deposit/sign-off state as workflow metadata.
- **Defended posit** → state one of the four standings separately and record the defended-posit warrant profile.
- **Registered, not Sealed** → **Registered**, with the named sealing debt.
- **Registered conditional on X** → **Registered** within the stated condition; X's own standing and every inherited debt remain explicit. The result may not be spent unconditionally.
- **Derived with empirical state input** → state the justified standing plus the empirical input and conditionality.
- **Lead** → research/workflow metadata, not standing.
- **Dissolved**, **retracted**, **superseded**, **quarantined**, and **historical** → dispositions, not standings.
- **Current**, **control**, and **mature** → document or lifecycle metadata, not claim standing.
- **Forced**, **retorsion-secured**, **construction**, **selection**, **recognition**, **checked**, **argued**, and **theorem** → warrant or evidence vocabulary, not standings.
- **Locked actual** → deprecated package-era shorthand; translate claim by claim through [locked-actual-decrement-map](locked-actual-decrement-map.md).

Compound or ambiguous expressions such as “Open or Conjectured,” “Registered structural / representational,” or “Registered program / Open values” must be split into distinct claims or reduced to one standing with explicit scope. They are not additional grades.

## Execution rule

Never upgrade standing, warrant, or evidence by paraphrase. Argued is not proved; checked is not theorem; finite-range verification is not proof; selection is not forced; a relation result is not a first-principles derivation; a measure is not an observed frequency.

Every load-bearing claim report must state, separately:

1. semantic claim and scope;
2. one live standing;
3. warrant route or profile;
4. conditions and inherited debts;
5. evidence/test state where relevant;
6. confidence only if useful;
7. workflow state or disposition where relevant.

See also: [agent-execution-rules](agent-execution-rules.md), [known-failure-modes](known-failure-modes.md), [locked-actual-decrement-map](locked-actual-decrement-map.md), [architectonic-rigor](architectonic-rigor.md).
