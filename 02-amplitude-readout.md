---
title: "Amplitude / Readout Theorem"
type: result
status: current
created: 2026-06-21
updated: 2026-07-23
confidence: medium
sources:
  - realizability-weighting-law.md
claim_statuses: [Open, "Registered-candidate", Registered]
---

# Amplitude / Readout Theorem

## Scope

A squared amplitude is framework-native only when the unsquared quantity is an access or coherence-participation amplitude in a registered pairing geometry. A numerical readout label, angle, or ladder coefficient does not become a probability amplitude merely because it can be squared.

For a standing `sigma` and an admissible fork of alternatives `{e_i}`, write `w_sigma(e_i)` for the candidate's coherence-participation. The quantum instance is carried by the complex carrier and its Hermitian pairing.

## R5: noncontextuality from held and registered

The Gleason route requires the candidate weight to depend on the candidate ray rather than on which orthonormal basis contains it, and requires the total over every complete orthonormal basis to be constant. Both conditions follow from the held/registered discipline.

1. **Fork inventory.** In the registered carrier, orthogonality is registrable distinctness. An orthonormal family is therefore a family of mutually registrably distinct alternatives, and a complete orthonormal basis is a complete admissible fork.
2. **Alternative-alone dependence.** `w_sigma(e)` is the registered participation relation between the standing `sigma` and the candidate `e`. The other basis members are the held decomposition accompanying `e`. Allowing those co-alternatives to change `w_sigma(e)` would treat held bookkeeping as a registered distinction in the `sigma -> e` relation.
3. **Constant fork total.** A complete fork registers actuality-as-such: exactly one alternative actualizes. Its total coherence-participation is therefore fixed by the standing and is not altered by which held orthogonal decomposition presents the fork.

Thus `w_sigma` is a nonnegative frame function on rays satisfying

> `sum_i w_sigma(e_i) = W_sigma`

for every complete orthonormal basis `{e_i}`, with `W_sigma` independent of the basis.

**Grade:** **Registered-candidate** for the R5/noncontextuality grounding.

## The Born instance

In complex dimension at least three, Gleason's theorem then gives a positive operator `rho_sigma` such that

> `w_sigma(e) = <e, rho_sigma e>`.

For a pure standing, `rho_sigma = |sigma><sigma|`, so

> `w_sigma(e) = |h(sigma,e)|^2`.

After normalization over the fork,

> `P(e_i) = |h(sigma,e_i)|^2 / sum_j |h(sigma,e_j)|^2`.

The pairing, the R5 grounding, and the Gleason theorem therefore carry the exact quadratic Born form. The dimension-two caveat remains local to Gleason and must travel wherever this route is used.

## Access is not readout

A `cos^2(theta)` factor is admissible only when `theta` belongs to the carrier's access geometry. A normalized ladder coefficient, eigenvalue label, or other readout quantity belongs to the result space and cannot be imported as an access amplitude without a separate bridge.

## Boundary

This theorem supplies relative weighting among registered alternatives. It does not by itself supply an absolute decay or transition rate; that requires the local possibility-space and rate structure of the process. The separate demand that long-run frequency be derived from weight is Dissolved and is not a condition on this theorem.
