---
title: Closure-Inherited Metric
type: physics-closure-mass
created: 2026-06-23
updated: 2026-07-23
status: current
confidence: high
section: Closure, confinement, and mass/value machinery
sources:
  - mass-derivation-three-faces.md
  - gauge-structure-result.md
  - mathematization-F8-done.md
---

# Closure-Inherited Metric

The measure of one color closure is the measure of its normalized moment-standings, not the volume of an abstract operator group:

> `Vol(closure) = Vol(S^5) · Vol(S^3) · 1 = pi^3 · 2 pi^2 = 2 pi^5`.

This page fixes the metric and its scale before the measure is used in the proton/electron relation.

## Closure-space construction

A determinant-one orthonormal color frame is constructed moment by moment from the primitive Hermitian pairing on standings.

1. **First moment.** Choose a unit standing `e_1` in `C^3`. The self-pairing condition `h(e_1,e_1)=1` gives the unit standing-space `S^5`, with radius fixed at one by the standing's own normalization.
2. **Second moment.** Choose a unit standing `e_2` in the orthogonal complement `e_1^perp ≅ C^2`. Restricting the same pairing to that complement gives the unit standing-space `S^3`, again at radius one. The second factor is therefore derived by pairing-on-standings within the remaining closure-space.
3. **Third moment.** Orthonormality leaves a one-dimensional complex complement. The determinant-one condition selects the unique phase of `e_3`. The third moment is forced and contributes no continuous freedom and therefore the multiplicative factor `1`.

Thus

> `Vol(S^5) · Vol(S^3) · 1 = pi^3 · 2 pi^2 = 2 pi^5`.

The construction is order-independent: no moment is privileged, and choosing a different first moment merely applies the `SU(3)` action to the same normalized standing-space.

## Why this is the invariant measure

The pairing supplies the metric locally at each moment, and the `SU(3)` action preserves both the pairing and the determinant-one completion. The product measure is therefore invariant under the closure's no-distinction freedom. Its scale is not conventional: both sphere radii are fixed by self-pairing equal to one.

No operator direction is measured anywhere in the construction. The abstract trace metric, which gives `sqrt(3) pi^5`, is therefore inapplicable to the physical closure.

## Algebraic cross-check

The geometric construction and the frame-side `lambda_8` result are the same fact read two ways. After `e_1` and `e_2` are chosen, the determinant-balancing direction is not independent: `det=1` forces the third phase. In the algebraic description this is the dependence of

> `lambda_8 = diag(1,1,-2)/sqrt(3)`.

Counting that direction as free produces the abstract trace-metric result. Treating it as the forced completion of the standing-space produces `2 pi^5`.

## Why confinement matters

There is no physical free color standing whose detached operator-group metric could be measured. Color stands only in determinant-preserving closure. The measure therefore belongs to the closed standing-space itself.

## Grade and boundary

**Registered:**

- the primitive pairing, not a trace form, is the metric source;
- the first unit moment contributes `S^5`;
- the second unit moment contributes `S^3` by restriction of the same pairing to `e_1^perp ≅ C^2`;
- orthonormal completion plus `det=1` forces the third moment with zero remaining freedom;
- the resulting invariant, normalized closure measure is `2 pi^5`;
- the geometric forced-completion result agrees with the registered `lambda_8` dependence argument.

This page supplies the single-closure measure. Spatial seating produces the separate factor `3`, giving the exact With-This factor `6 pi^5`, in [mass-derivation-three-faces](mass-derivation-three-faces.md). The complete proton/electron relation remains

> `m_p / m_e = 6 pi^5 [1 + c(3 pi^4)^-2]`, with `3/2 <= c <= 9/4`.

Only the exact internal selection of `c` remains Open. See [epsilon-fw-bracket-result](epsilon-fw-bracket-result.md).