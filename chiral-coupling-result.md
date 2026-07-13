---
title: Chiral Coupling Result
type: result
created: 2026-06-21
updated: 2026-06-21
status: current
confidence: medium
sources:
  - chiral-coupling-result.md
  - gauge-structure-result.md
---

# Chiral Coupling Result

Result module for chiral coupling and weak SU(2), including maximal chirality / V−A form.

## Mature status

Status: **Registered** for maximal chirality/orientation-faithful coupling; **Open** for exact chiral fermion module and hypercharge embedding.

## Caution

The cover letter says the exact chiral module is not derived; do not overstate beyond the result module's scope.

## Grade adjudication (2026-06-21)

Worked as Item 6 of [physics-domain-work-plan](physics-domain-work-plan.md). Four sub-claims earn distinct grades.

**Chiral/vectorial criterion — Registered.** The framework fixes that a coupling is chiral iff orientation-faithful and vectorial iff orientation-independent, and that the weak coupling sits at maximal chirality (V−A). This is a structural result and is securely Registered.

**One-generation chiral module — Open.** The specific `SU(3)×SU(2)×U(1)` representation content of a single generation (the left-handed doublets, right-handed singlets, and their multiplicities) is *not* derived. The framework motivates a chiral, color-split, doublet-bearing pattern, but does not force the exact module. Treat as Open, not Conjectured-with-content, because no concrete representation assignment is pinned by framework primitives yet.

**Hypercharge / `1/6` charge-lattice — Conditional, not Registered.** The hypercharge assignments and the `1/6`-spaced charge lattice remain *conditional mystery-compression*: they follow only if a center-lock premise (the simultaneous diagonal identification of the `SU(3)`, `SU(2)`, and `U(1)` centers) is granted, and that premise is not derived. Any anomaly/hypercharge-ratio constraints that are supplied externally must be registered separately as imported empirical input, not as framework output.

**Generation count — Open and kept separate.** Multiplicity of generations is not addressed here and must not be folded into the module derivation (see Item 9).

**Verdict.** Criterion **Registered**; exact module and hypercharge **Open / conditional**, gated on (a) the center-lock premise and (b) the SU(3) alternating premise inherited from [gauge-structure-result](gauge-structure-result.md). Confidence >90% attaches to this split grade. The dependency on the Item 3 alternating gate means this item cannot seal ahead of the gauge bridge.

See also: [physics-domain-mature-status](physics-domain-mature-status.md), [physics-domain-work-plan](physics-domain-work-plan.md), [gauge-structure-result](gauge-structure-result.md), [claim-status-vocabulary](claim-status-vocabulary.md), [locked-actual-decrement-map](locked-actual-decrement-map.md).
