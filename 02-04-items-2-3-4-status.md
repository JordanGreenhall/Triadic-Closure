---
title: "SM Frontier Items 2–4: Arguments and Status"
type: process
status: current
created: 2026-06-25
updated: 2026-06-25
scope: frontier-items-2-3-4
statuses_used: [Open, Conjectured, Registered, "Registered and Sealed", PASS, CONDITIONAL]
sources:
  - amplitude-readout-theorem.md
  - realizability-weighting-law.md
  - epsilon-su3-bridge-construction.md
  - same-kind-carrier-representation-theorem.md
  - gauge-structure-result.md
  - 03-04-five-cycle-expansion-contraction.md
  - sm-content-smuggle-audit-frontier.md
  - p26-matter-sourced-geometry-holonomy-and-bmv.md
---

# SM Frontier Items 2–4: Arguments and Status

This file records the worked state of the first three load-bearing items on the
SM-content smuggle frontier. Grades use the live claim-status vocabulary
(Open / Conjectured / Registered / Registered and Sealed) plus the loop pass-states
(PASS / CONDITIONAL). Nothing here is stamped **Registered and Sealed**; the
residuals that hold each result below seal are named explicitly.

## Governing discipline

A loop works backwards from the established physics concept: name what the concept
actually does in physics, identify what the wiki asks it to do, then derive the
framework-native equivalent of exactly that capacity. Two standing rules:

- Do not ask an item to bear more than the load it actually carries downstream.
- A claim's grade is the floor of its own instrument and its premises. A premise
  that is itself **Registered** is *discharged*, and a claim resting on it inherits
  Registered — it is **not** thereby marked "conditional." "Conditional on X" is
  reserved for premises that are themselves Open or Conjectured.

## Dependency order (acyclic)

```
foundation (office-count posit, no-privileged-frame, This-flattening) + Item 2
        │
        ▼
   Item 4  — same-kind complex carrier C³, Hermitian pairing, fixed form
        │
        ▼
   Item 3  — alternating ternary invariant + connectedness/irreducibility
        │       + SL(3,C) ∩ U(3) = SU(3)
        ▼
   native SU(3)
```

Item 4 is upstream of Item 3: Item 3 reads its carrier off Item 4. The earlier
back-edge — "Item 4's dimension-3 is conditional on Item 3's alternating form" — is
**cut**, because dimension-3 has an independent and more fundamental ground (the
office count flattened; see Item 4, Gate F). `no-privileged-frame` is a *shared
upstream primitive* used by both items, not a back-edge.

---

## Item 2 — Amplitude / Readout: **PASS**

### Concept and capacity
The Born rule: assign normalized weights to outcomes/channels from a state-or-fork
context by squaring an amplitude in an inner-product space.

### The scoping insight
The previous process stalled trying to seal the identity
`observed long-run frequency = framework weighting measure`. Current correction:
that identity was misposed. Actuality needs no second bridge from weights to events;
the shape of the possibility space gives the actualization rate/measure,
and frequency is the many-event view of that actuality. The downstream load is
Born-rule-level **weighting/selection among registered alternatives**, and the
Registered weighting measure carries all of it. No current downstream page needs a
separate native *frequency=weight* theorem.

### Native object
A normalized `|amplitude|²` / coherence-participation measure on a licensed
pairing/frame. Registered via pairing-origin + conservation/normalization + the
Gleason frame-function theorem (dimension ≥ 3, as mathematics-as-mathematics).

### Dependency map (completed)

| Downstream page | Use of Item 2 | Item 2 load? | Carried? |
|---|---|---|---|
| `with-to-this-closure` | weighted actuality-selection among closure forks | yes — weighting only | ✓ measure; attractor uniqueness carried by local arity/stability |
| `gravity-and-curvature` | the F8 coherence-participation functional + its gradient | yes — supply the measure | ✓ math-as-math; integration to curvature is local F9/F11 |
| `gravity-asymmetry` | participation-weight comparison of next-configurations ("no rate, no density, no driver") | yes — weighting/comparison | ✓ measure |
| `mass-as-self-closure` | coupling strength ≡ `|h(σ,k)|²` overlap | yes — definition = squared amplitude | ✓ Registered as program |
| `mass-derivation-three-faces` | "equal weighting" = spatial isotropy; "cyclotron frequency" = measurement | **no** — symmetry + empirical metrology | n/a |
| `propagation-…` (both) | explicitly marks the Born measure / frequency as Open | **no** — defers, places no load | ✓ consistent |
| `d6-persistence` | escape participation-weight as decay "rate-in-essence" | yes — relative propensity | ✓ at measure level (see flag) |
| `p26-matter-sourced-geometry-holonomy-and-bmv` | candidate amplitudes/phases on a causal-growth square and BMV branch alternatives | yes — beyond weight alone | ✗ connection, edge phase, branch state, and entanglement witness remain Conjectured/Open under P26 |

### Carried premises (must travel with downstream uses)
1. **Dimension ≥ 3** for the exact `|·|²` form (the standard Gleason gap at
   dim 2 is not closed and must not be hidden).
2. **`d6-persistence` "rate-in-essence"** is licit only as a *relative escape
   propensity* (a weighting/comparison). Observed decay rates remain empirical or
   comparison unless the local escape possibility-space/rate structure is derived;
   do not route this back into a generic frequency=weight work item.

### Verdict
**PASS** — the Registered weighting measure carries every measured downstream load.
The `cos²(θ)` smuggle the audit warns about is *guarded-against, not active*: every
`cos²(θ)` occurrence in the corpus is in the control/audit pages that set the rule,
not in a live derivation.

### Integration rule
Downstream pages may use `|amplitude|²` / coherence-participation as a native
weighting measure; must not silently promote a measure to an observed frequency;
must keep the dim-2 flag; observed decay/transition *rates* as numbers remain
empirical or comparison unless the local possibility-space/rate structure is derived.
P26 may use this item for normalized weighting only; it may not infer a complex edge phase, non-exact holonomy, measured BMV entanglement, or a decoherence prediction from the measure.
**No grade change** to the realizability-weighting law — it stays Registered, not
Sealed — but frequency=weight must not be presented as a work frontier.

---

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

---

## Item 4 — Same-Kind Complex Carrier: **CONDITIONAL-PASS / Registered carrier theorem**

The load reduces to six gates. All reach **Registered**; the role-sorted, discrete,
vector/operator, projective, lower-dimensional, symmetric-cubic, and fibered
alternatives are all excluded.

### Gate A — one carrier (vs. fibered/isomorphic fibers) — **Registered**
A fibered model posits three isomorphic fibers plus a gluing datum. By the
registrability dichotomy: a registrable gluing datum is an additional internal
distinction — a frame-selector forbidden by `no-fourth-determinant` and contrary to
pure same-kindness; an unregistrable one makes the fibers framework-identical, so
they collapse to one carrier under the single shared closure-kind basis. Since
"same-kind" *is* "registered under one shared character" (With's basis, §2.5),
there is no room for an independent registrable gluing datum. One With-field forces
one carrier.
**Falsification surface:** a gluing datum that is registrable yet not a forbidden
frame-selector.

### Gate B — complex linearity (vs. real) — **Registered** (the load-bearing gate)
The real alternative (ℝ³, real determinant, `SO(3)`) is fully coherent, so
complexness is not forced by the alternating form, one carrier, scalar verdict, or
dimension alone. The native source is **non-interchangeability**: the This-flattened
triad is registered as "symmetric but non-interchangeable," so the three moments
carry a *registered orientation*. A linear/total order would privilege a first
element — a frame-selector, forbidden by `no-privileged-frame`. The only orientation
on three elements with no privileged element is the **cyclic order ℤ₃**. ℤ₃ has no
faithful real one-dimensional representation; its minimal faithful representation is
two real dimensions — rotation by 120°, i.e. multiplication by a primitive cube root
of unity. To register the orientation faithfully, each moment-line carries that
complex structure. Hence the carrier is complex.

Chain: non-interchangeable (This-flattening) + no-privileged-element
(`no-privileged-frame`) + three (office count) ⇒ cyclic ℤ₃ ⇒ faithful real rep is
complex ⇒ complex carrier.

**Falsification surface / seal residual:** the step "non-interchangeable +
no-privileged-element + three ⇒ cyclic ℤ₃" — formally excluding an exotic
non-cyclic registered structure on three elements is the seal debt.
**Recognition only (not load-bearing):** the center of `SU(3)` is ℤ₃; the same
cyclic structure that forces complexness reappears as the center of the group it
builds toward — a consistency, not a derivation.

### Gate C — scalar closure-verdict is primitive (vs. vector/operator) — **Registered**
A dependency argument. The closure-verdict asks whether the triad closes as one,
with what standing — a This/actuality question. Any vector- or operator-valued
output is *produced content*: a successor This conditioned by the closure
(From→This lineage). Producing the content of a closure presupposes the closure
occurred, so closure-status is prior to produced content, not a readout of it. The
verdict is single-valued because With's basis registers one respect (the
closure-kind). Vector/operator-with-scalar-readout models are dependent downstream
representations.

### Gate D — fixed form (vs. projective line) — **Registered**, and it locates U(1)
The closure-verdict has a magnitude (Gate C). A magnitude is a registered
distinction, and conservation of registered distinctions (§9.7) forces it to be
preserved exactly — the form's **modulus is fixed**, `det = 1` on the nose, not up
to scale. The residual phase freedom (`ε ↦ e^{iθ}ε`) is not a defect: it is the
**From-phase, the separately-registered U(1) oriented line**. So the projective
ambiguity is exactly the U(1) factor, and the fixed-modulus internal stabilizer is
`SU(3)` — consistent with the gauge-structure result locating U(1) at the From-phase.

### Gate E — Hermitian pairing (vs. symmetric-bilinear) — **Registered**
*(Depends on Gate B, which is Registered, so E inherits Registered — it is not
"conditional on B." The earlier "conditional on B" was a status error: it
double-counted B as both a Registered result and a live open premise.)*
Given a complex carrier, the pairing is forced Hermitian: the coherence-overlap is a
real nonnegative magnitude (Item 2's `|h|²`), and a real-valued conjugation-symmetric
form on a complex space is Hermitian; a symmetric C-bilinear form would instead
distinguish a preferred real structure — a registered real frame, forbidden (this is
what excludes `SO(3,C)` in Item 3). Positive-definiteness comes from Item 2: the
participation weight is ≥ 0, zero only for the zero standing, and a genuine standing
is maximally self-participating. So the pairing is positive-definite Hermitian —
which cuts `SL(3,C)` to `SU(3)`.

### Gate F — dimension exactly 3 — **Registered** (independent of Item 3)
The three This-flattened interior moments come from the **three offices** (the
exactly-three posit) via This-flattening — one marked triad, three flattened images.
Each occupies one complex line (Gate B); three complex lines = C³. This grounds
dimension-3 in the office-count posit plus This-flattening, **upstream of any gauge
work and with no reference to the alternating form.** The "nonzero alternating
3-form ⇒ dim ≥ 3" route is corroboration, not the load-bearing ground. This is the
cut that makes the 3↔4 dependency acyclic.

### Verdict
**CONDITIONAL-PASS: the same-kind complex carrier C³ with Hermitian pairing and
fixed volume form is a Registered carrier theorem** — an upgrade from "no carrier
theorem exists." Conditional only in that it sits, as the whole corpus does, on the
foundational posits; its own seal residuals are Gate B's ℤ₃-cyclic formalization
(the largest) and minor formal residuals on A, C, D.

---

## Combined status

| Object | Grade | Held below seal by |
|---|---|---|
| Item 2 — amplitude/readout weighting measure | **PASS** (Registered, not Sealed) | old frequency=weight gate is misposed; local rate/spectrum derivations remain case-specific |
| Item 4 — same-kind complex carrier C³ + Hermitian + fixed form | **CONDITIONAL-PASS / Registered** | Gate B ℤ₃-formalization; minor A/C/D residuals |
| Item 3 — connectedness lemma | **Registered** | relate-through criterion |
| Item 3 — irreducibility lemma | **Registered** | polystability; no-privileged-frame subspace-scope |
| Item 3 — `Stab(ε)=SL(3,C)`, `∩U(3)=SU(3)`, dim 3 | **Sealed as mathematics** | (inputs licensed by Item 4) |
| **native SU(3)** | **Registered** (not Sealed) | the residuals above |

### The single load-bearing joint
The acyclicity of 3 ↔ 4 rests on **dimension-3 being grounded in the office count
(Gate F) rather than in the alternating form.** If that independent ground failed,
3 and 4 would be mutually conditional and both would drop below Registered. The
office-count route holds (it is the exactly-three posit flattened), but this is the
joint to press.

### Highest-value seal target
**Gate B's ℤ₃-cyclic formalization** — it is the load-bearing residual under Item 4
and, through it, under native SU(3).

### What is *not* claimed
Native SU(3) is **not** Registered and Sealed; the SM color-group *name* still
carries no surplus beyond the Registered structure. Exact hypercharge assignments,
the electroweak mixing angle, generation count, masses/Yukawas, and completeness of
`SU(3) × SU(2) × U(1)` remain Open. Decay/transition *rates* as observed numbers
remain empirical or comparison unless their local possibility-space/rate structure is derived.
