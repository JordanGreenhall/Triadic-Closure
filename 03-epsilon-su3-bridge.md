---
title: "SM Frontier Item 3: Epsilon / SU(3) Bridge"
type: process
status: native-su3-registered-not-sealed
frontier_item: 3
updated: 2026-07-15
sources:
  - process/sm-frontier-loop-state/02-04-items-2-3-4-status.md
  - Frontier Close Loop Execution/epsilon-su3-bridge-construction.md
  - Frontier Close Loop Execution/same-kind-carrier-representation-theorem.md
  - results/gauge-structure-result.md
---

# Item 3 — Epsilon / SU(3) Bridge

## Item 3 — ε / SU(3) Bridge: native SU(3) **Registered** (not Sealed)

### Concept and capacity
A fixed nonzero alternating complex 3-form (ε / determinant) whose stabilizer, with
a Hermitian pairing, is compact `SU(3)`; supplies the color/representation
structure.

### The reduction
Given a scalar-valued, complex-multilinear, nonzero, primitive, fixed ternary
closure-verdict on a same-kind 3-carrier (all supplied by Item 4), the live rivals
are exactly: the **alternating** form (stabilizer `SL(3,C)`, irreducible,
connected) versus the **symmetric** cubics, which split into the `xyz`-type
(stabilizer with reducible diagonal-torus identity component, disconnected) and the
generic type (finite stabilizer, e.g. the Hesse group of order 216, which acts
*irreducibly*). The two lemmas are not redundant — each kills a different rival:
**connectedness** kills the finite/Hesse symmetric cubics; **irreducibility** kills
the `xyz`-torus. Only the alternating form survives both.

### Lemma 1 — Connectedness — **Registered**
Item 4 supplies a complex same-kind carrier, so the interior multiplicity is a
*continuum* of superpositions, not a finite label set. With is relation-through: it
must hold that multiplicity as one related whole. A finite or discrete admissible
re-framing family (Hesse, S₃, any finite stabilizer) relates only finitely many
configurations and leaves a positive-dimensional family unrelated-through —
With would then hold isolated labelled points, not one related whole, contradicting
its office. Hence the admissible family (the algebraic stabilizer) has
positive-dimensional orbits: it is connected. This excludes every finite-stabilizer
symmetric cubic, including the irreducible Hesse case.
**Seal residual:** the precise "relate-through" criterion (ruling out a discrete
group with dense orbits — excluded here because admissible transformations form the
algebraic stabilizer, whose finite case has finite orbits).

### Lemma 2 — Irreducibility — **Registered** (new route)
Anchored to an already-Registered property, **no privileged internal frame**, not
to the retired "vanishing-on-coincidence" premise. Suppose the stabilizer fixes a
proper subspace. The closure-verdict is nonzero/nondegenerate, so its stabilizer is
reductive (polystable form ⇒ closed orbit ⇒ reductive). A reductive group fixing a
proper subspace fixes a complement too (complete reducibility), so it fixes a proper
subspace of dimension ≤ 1 — a **fixed line**. But a globally fixed interior line is
a frame-independent, separately-addressable interior direction: a privileged
internal frame-element, which `no-privileged-frame` forbids. Contradiction.
Therefore the stabilizer acts **irreducibly**, killing the `xyz`-torus by function,
not by "QCD doesn't use it."
This route closes the 2-plane loophole (a fixed plane forces a fixed line via
reductivity) and avoids the §9.6 sector-assignment worry — antisymmetry is
*derived* from no-privileged-frame, not assigned by recognition.
**Seal residuals:** (a) polystability of the closure-verdict form; (b) the exact
subspace-scope of `no-privileged-frame` (it forbids a fixed line cleanly; sealing
wants that scope formalized).

### Rival excluded: SO(3,C)
`SO(3,C)` also acts irreducibly on C³ and preserves the alternating form, so
irreducibility + alternating alone would admit it — and `SO(3,C) ∩ U(3) = SO(3)`,
the wrong group. It is excluded because `SO(3,C)` additionally preserves a
symmetric **C-bilinear** internal form, whereas the only licensed pairing (Item 4,
Gate E) is **Hermitian** (sesquilinear), distinguishing no symmetric C-bilinear
invariant. So the holomorphic stabilizer is the full `SL(3,C)`, and
`SL(3,C) ∩ U(3) = SU(3)`.

### Mathematical step — **Sealed as mathematics**
Given fixed nonzero `ε ∈ Λ³(C³)*` and a compatible Hermitian pairing,
`Stab(ε) = SL(3,C)` and `SL(3,C) ∩ U(3) = SU(3)`; minimality forces dim = 3.

### Verdict
**Native SU(3) is Registered** (not Sealed): both lemmas at Registered, the carrier
at Registered (Item 4), the stabilizer step Sealed as mathematics. This clears the
former "conditional-mathematics-only" ceiling.

## Integration note

This supersedes the earlier “conditional mathematics only” ceiling. The SU(3) derivation is now carried as native Registered, not Sealed. Remaining residuals are seal residuals, chiefly formalizing the connectedness/irreducibility premises and their dependence on the Registered Item 4 carrier theorem.


## 2026-07-15 execution

Full-load and adversarial verification: [Lineage 3 execution](lineage-execution/03-epsilon-su3-bridge.md). Verdict remains **PASS-for-load / Registered, not Sealed**; named seal residuals are preserved.
