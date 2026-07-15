---
title: "Flat-Substrate F4–F7 Physics Construction"
type: worked-argument
status: supporting
updated: 2026-07-15
canonical-m2: mathematical-closure-composition-persistence.md
---

# Mathematizing the Flat Substrate: F4 (c as metric identity), F5 (sum-of-squares), F6 (Lorentzian signature), F7 (the Lorentz group)

> **Disposition.** This is a supporting physics construction, not the M2 mathematics lineage despite its historical F4–F7 labels. [M2 — Closure, Composition, and Persistence Machinery](mathematical-closure-composition-persistence.md) is canonical. The inherited identification of carrier depth with time, directed address-separation with symmetric space, and a carrier edge with a physical atomic step is not supplied by M1; the flat-metric bridges must be re-established in P4/P5.

### Second computation of the gravity-mathematization survey, building on the conditioning carrier `N`. Historical tags such as “proved” below are provenance until the M2 re-adjudication assigns live standings.

---

## 0. Inherited from F1–F2

- **(N)** The conditioning-network: nodes = standings (individuated by address/lineage), edges = single one-way turn-overs (conditionings). Background-free.
- **Depth** = finite address-length, an oriented integer carrier grading. Its physical-time reading is Open here.
- **Directed reachability** = minimal directed chain length where a path exists; it is generally asymmetric. A symmetric adjacency distance requires the declared selection of forgetting orientation, and its spatial reading is Open here.
- **M1-native quantities** must be definable from `N` plus living inherited structure. Primitive background rate/density is unavailable at this grade; later derived rates and densities are permitted after their measures are earned. A scalar coherence-participation functional is not inherited from M1 and must be constructed in M3.
- **Node-content:** offices (0.1), **J** = involutive polarity, orientation-reversal, J²=id (0.2, Treatise §7.2), the two sectors (0.3), the **pairing** = non-degenerate, J-compatible, bi-additive (0.4).

---

## F4 — c as the depth/separation identity (at metric level)

**(P7) [proved] The unit of depth and the unit of separation are the same unit — one conditioning — and their identity is c = 1.** A unit of depth is one turn-over along an address (one conditioning, counted as temporal advance). A unit of separation is one edge between addresses (one conditioning, counted as spatial step). By F1.3 these are the *same* intrinsic act (a conditioning) read under the two counts (From-count vs With-count). The conversion between them is therefore the identity: 1 edge of separation ↔ 1 increment of depth. Writing this conversion as c, **c = 1 by construction** — it is not a magnitude but the identity between the two namings of the unit act. ∎

**(C7.1) [proved] c is admissible and is not a free particular.** c is definable from N's edge/depth structure (P2-admissible) and equals 1 necessarily (P7). Contrast: in standard relativity c is an empirical constant carrying a large numerical value; here that value is an artifact of measuring depth and separation in unrelated units. On N there is one unit (the conditioning), so c = 1 is forced. **This is the first confirmed "different particular": c is the unit, not a parameter.** ∎

---

## F5 — The spatial metric is the sum of squares (from isotropy)

**Setup.** Address-separation gives, between two standings, a chain-length along each of the three flattened With-degrees (F3). Write the separation components (Δx¹, Δx², Δx³). The spatial interval is some combination σ(Δx¹, Δx², Δx³). The question: which combination?

**(P8) [proved] The three spatial degrees are isotropic — pairwise interchangeable by an admissible symmetry.** [forced-prior + here] The three degrees are the With-flattening of the marked triad: the flattening blinds the kind-marking (Treatise §7.4a), so the three are symmetric and interchangeable (the With-flattening is the *interchangeable* one, by the office-signature readout). "Interchangeable" means: there are admissible transformations of N permuting and, more strongly, continuously mixing the three degrees while preserving N's structure (the rotations among the flattened degrees). Admissible because they preserve addresses-up-to-relabeling of the flattened degrees, which carry no kind-marking to violate. ∎

**(P9) [proved] An isotropic, additive, sign-definite interval on three interchangeable degrees is the sum of squares (up to scale).** Proof: the spatial interval σ must be (i) **invariant** under the isotropy group (P8) — the continuous mixings of the three degrees; (ii) **additive over orthogonal independent separations** (the degrees are independent — separation along one is unconstrained by another; and accumulation of distinction composes additively, the metric-as-registered-distinction principle); (iii) **sign-definite** (a separation is a count of edges ≥ 0; the interval vanishes only at coincidence). The continuous group preserving a sign-definite additive quadratic form on three real degrees and acting transitively on directions is the rotation group SO(3), whose unique (up to scale) invariant sign-definite additive form is δᵢⱼΔxⁱΔxʲ = (Δx¹)² + (Δx²)² + (Δx³)². Any non-quadratic additive isotropic form (e.g. Σ|Δxⁱ|ᵖ, p≠2) is *not* invariant under continuous mixing of the degrees (only under the discrete permutations and sign-flips) — it fails (i). So the quadratic is forced by isotropy + additivity + sign-definiteness. ∎

*Status of F5:* **[proved]**, modulo (P8)'s claim that the isotropy is the *continuous* mixing group (not merely discrete permutations). That the flattening yields *continuous* interchangeability (rotations), not just permutation symmetry, rests on the degrees being a rule-given continuum (0.9) along each — **[argued]**, flagged: the continuum of directions needs the rule-given continuum deployed on the flattened degrees. Sub-gate F5a: confirm the isotropy is continuous (SO(3)), not discrete.

---

## F6 — The signature is Lorentzian (the minus sign), from the null bound

**Setup.** Depth (time, Δt) and the spatial interval combine into a single interval (F4: one unit). Write s = α(Δt) + β·σ(Δx) for some combination. The question: the relative sign/structure of the depth-part and the space-part.

**(P10) [proved] The null condition: a directly-conditioning pair has zero interval.** Two standings one edge apart in separation and one increment apart in depth (Δt = 1, |Δx| = 1, in unit terms) are in **direct conditioning contact** — one is the immediate conditioning of the other. Direct contact is the limiting case of "separation": the pair are as close as conditioning allows (neighbors). The interval between immediate-conditioning neighbors propagating at the bound (v = 1, F4) must be the **zero of the interval** — they are not separated *along the propagation*, since the propagation *is* their contact. (Admissible: this uses only depth, separation, and the v ≤ 1 bound, all intrinsic.) So the interval vanishes when |Δx| = Δt. ∎

**(P11) [proved] The interval is quadratic in depth with opposite sign: s² = −(Δt)² + σ(Δx) = −(Δt)² + (Δx¹)²+(Δx²)²+(Δx³)².** Proof: by F5 the spatial part is the sum of squares. The full interval must (i) reduce to the spatial sum-of-squares at equal depth (Δt = 0), and (ii) **vanish on the null condition** |Δx|² = (Δt)² (from P10: |Δx| = Δt ⇒ s = 0). A combination of (Δt)² and |Δx|² vanishing exactly when |Δx|² = (Δt)² is, up to scale, |Δx|² − (Δt)². Adding any non-quadratic dependence on Δt breaks (ii) at general separations (the null set would not be the cone |Δx| = Δt). So the interval is s² = −(Δt)² + |Δx|², with one timelike sign opposite to the three spacelike — **Lorentzian signature (1,3)**. The minus sign is forced by the null condition (P10), which is forced by the propagation bound (F4). ∎

*Status of F6:* **[proved]**, given F5 and the null condition (P10). The one substantive input is (P10) — that immediate-conditioning neighbors at the bound are zero-interval — which is **[argued]** cleanly (direct contact = not-separated-along-propagation) but deserves an explicit check that "zero interval" is the *forced* reading and not merely natural. Sub-gate F6a: pressure-test P10.

---

## F7 — The admissible re-couplings of N are exactly the Lorentz group

This is the owed proof. **Claim:** the group of admissible re-couplings of N — the transformations that re-split a separation into depth-vs-spatial parts while preserving N's structure — is exactly the Lorentz group O(1,3) (or its identity component SO⁺(1,3)).

### F7.1 What an admissible re-coupling is (defining the group)

**(D7) [definition, framework-bound] An admissible re-coupling is a transformation T of N's separations that:**
1. **preserves the conditioning structure** — maps conditioning-chains to conditioning-chains, respecting one-way orientation (it is a symmetry of the edge-structure, M2);
2. **preserves the unit** — one conditioning maps to one conditioning (c = 1 is preserved; F4);
3. **is J-compatible** — commutes with J (orientation-reversal), since J is constitutive node-content (0.2) and a symmetry of N must respect it;
4. **preserves the pairing** — the non-degenerate J-compatible pairing (0.4) is preserved (a symmetry preserves the inherited form).

These four conditions are not chosen for convenience; each is "a symmetry of N must preserve N's intrinsic structure," itemized over the structures N carries (edges/orientation, unit, J, pairing). Admissible by (P2).

### F7.2 The interval is preserved

**(P12) [proved] Every admissible re-coupling preserves the interval s² = −(Δt)² + |Δx|².** Proof: the interval is built (F5, F6) from (a) the spatial sum-of-squares, which is the pairing restricted to the spatial degrees, and (b) the null condition, which is the unit/orientation structure. Condition (D7.4) preserves the pairing (hence the spatial form and its extension), and (D7.1–D7.2) preserve the orientation and unit (hence the null condition). The interval is determined by these (F6), so it is preserved. ∎

So Aut(N, re-coupling) ⊆ O(s²) = O(1,3): every admissible re-coupling is an interval-preserving transformation, i.e. a Lorentz transformation.

### F7.3 The converse — every Lorentz transformation is an admissible re-coupling

This is the harder direction (showing the group is *exactly* Lorentz, not a subgroup).

**(P13) [argued → partially proved] Every interval-preserving transformation is realized by an admissible re-coupling of N.** The Lorentz group O(1,3) is generated by (a) **spatial rotations** SO(3), and (b) **boosts** (the depth↔spatial mixings). Take each:

- **Rotations** are admissible re-couplings: they are the continuous isotropy of the spatial degrees (P8), which preserve edges, unit, J, and pairing (they act within the spatial degrees, which carry no orientation to violate). So SO(3) ⊆ Aut(N). **[proved, given F5a].**
- **Boosts** are the re-splittings of a separation into depth-vs-spatial parts — exactly the "re-coupling" of F1/propagation: a different admissible accounting of the same conditioning-separation as more-depth-less-spatial or vice versa, preserving the interval and the unit. That a boost preserves edges/orientation: a boost re-coordinatizes the same conditioning-chains (it does not add or cut edges), so it preserves the conditioning structure (D7.1). That it preserves J and the pairing: a boost is an interval-preserving map (by definition), and the interval is the pairing-extension (F6); J-compatibility holds because the boost is built from the same depth/spatial structure J acts on. So boosts ⊆ Aut(N). **[argued]** — the load-bearing sub-claim is that *every* interval-preserving boost corresponds to an *admissible* re-splitting (and not some boosts are inadmissible). Sub-gate F7a.

**(P14) [proved, given P13] Aut(N, re-coupling) = O(1,3) (or SO⁺(1,3) for the orientation-and-time-direction-preserving part).** From P12, Aut(N) ⊆ O(1,3). From P13, the generators of O(1,3) (rotations + boosts) are in Aut(N), so O(1,3) ⊆ Aut(N). Hence equality. Restricting to (D7.1)'s one-way orientation-preservation (conditioning runs one way) selects the **orthochronous** part (time-direction-preserving), and to the proper part if reflection is excluded: SO⁺(1,3), the connected Lorentz group. ∎

### F7.4 Status of F7

**[proved]** that Aut(N) ⊆ O(1,3) (P12) and that the interval is preserved; **[proved]** that rotations are admissible (given F5a); **[argued]** that all boosts are admissible re-couplings (P13, the converse for boosts) — this is the one remaining substantive gap, **sub-gate F7a**: show every interval-preserving boost is an admissible re-splitting of N's separations (no interval-preserving boost is excluded by D7.1–D7.4). If F7a holds, F7 is sealed: the re-coupling symmetry of N is exactly the connected Lorentz group, which is the flat-metric seal owed since the metric-maturation walk.

The orthochronous restriction is itself a **result, not an input**: because conditioning is one-way (M2), the admissible group is the *time-direction-preserving* part — N does not admit the time-reversing Lorentz transformations as re-couplings. This matches the physical fact that the orthochronous proper Lorentz group is the physical symmetry, and it falls out of From's one-wayness.

---

## Status after F4–F7

**Proved:**
- **F4:** c = 1 is the depth/separation unit-identity, forced, not a particular (P7, C7.1).
- **F5:** the spatial metric is the sum of squares, forced by isotropy + additivity + sign-definiteness (P9), modulo F5a (isotropy is continuous SO(3)).
- **F6:** the signature is Lorentzian (1,3), the minus sign forced by the null condition from the propagation bound (P11), modulo F6a (P10 pressure-test).
- **F7:** Aut(N, re-coupling) ⊆ O(1,3) proved (P12); rotations admissible; the full equality Aut(N) = SO⁺(1,3) proved modulo F7a (boost-admissibility converse). The **orthochronous restriction is derived** from From's one-wayness, not imposed.

**Remaining sub-gates to seal the flat tier:**
- **F5a:** the spatial isotropy is the continuous rotation group (rule-given continuum on the flattened degrees), not merely discrete permutations.
- **F6a:** pressure-test the null condition (P10) — that immediate-conditioning neighbors at the bound are forced to zero-interval.
- **F7a:** the converse for boosts — every interval-preserving boost is an admissible re-coupling of N (no admissibility condition excludes any boost).

These three are concrete and finite; clearing them seals the flat Lorentzian metric and the Lorentz-group symmetry as forced from N. Then the tier is complete and the curved/Einstein gates (F8–F11) follow, with the F1.2 admissibility rule (no rate, no density) carried into the gravity-tilt computation.

**Confirmed structural particulars (our model vs. standard):** c is the unit (= 1, forced), not an empirical parameter; the orthochronous restriction is derived from one-way conditioning, not postulated. Both are points where our grounding differs from the standard presentation while recovering the same flat structure.

---

## F5a, F6a, F7a — the three sub-gates cleared (flat tier sealed)

**(P15) [proved] F6a — the null condition is forced; it is the unit-identity.** At the bound v = 1, one increment of depth is spent entirely traversing one link of separation — and by F4 the depth-increment and the spatial-link are the *same single conditioning* counted two ways. So Δt = 1 and |Δx| = 1 at the bound are not two separations but one act counted both ways; the *net* separation (the interval) is that one act minus itself, = 0. The interval's vanishing on the null cone is therefore not an independent assumption but c = 1 (F4) read as "one act, counted as both depth and link, nets to zero": s² = −Δt² + |Δx|² = −1 + 1 = 0. The minus sign (F6) and the null cone are the same fact as the unit-identity (F4). ∎

**(P16) [proved] F5a — the spatial isotropy is continuous SO(3), not merely discrete S₃.** The With-flattening blinds *all* directional kind-marking (Treatise §7.4a), not only the marking distinguishing the three named degrees from one another. If only the three original axes were real and directions *between* them were not, that would be a retained marking (axes privileged over intermediate directions) — precisely the marking the flattening removes. So intermediate directions are as unprivileged as the axes; with the rule-given continuum (0.9) on each degree, a separation may point in any rule-given direction the three degrees span, and the no-privileged-direction symmetry preserving the degree-structure is the continuous rotation group SO(3). Discrete-permutation-only (S₃) would retain the forbidden axis-privileging marking. Hence the isotropy is continuous, and F5's sum-of-squares is forced (only the quadratic is SO(3)-invariant). ∎

**(P17) [proved] F7a — every orthochronous interval-preserving transformation is an admissible re-coupling; only the time-reversing ones are excluded.** Check D7.1–D7.4 against an arbitrary orthochronous interval-preserver:
- *D7.2 (unit):* c = 1 is the null structure of the interval (F4/F6); an interval-preserver preserves it. ✓
- *D7.4 (pairing):* the interval is the pairing extended by the J-signature (F6); an interval-preserver is a pairing-preserver by construction. ✓
- *D7.3 (J-compatible):* the (1,3) signature is exactly the J-eigenstructure (time = J-odd/orientation-carrying, space = J-even); preserving the interval preserves the signature-split, hence commutes with J. Automatic, not an extra constraint. ✓
- *D7.1 (edges + orientation):* a conditioning-chain is a sequence of future-directed within-cone links (each |Δx| ≤ Δt). An orthochronous transformation preserves the null cone and maps future-directed timelike/null vectors to future-directed timelike/null vectors, hence within-cone links to within-cone links — conditioning-chains to conditioning-chains, orientation respected. ✓ The *non*-orthochronous (time-reversing) transformations fail D7.1 (they reverse one-way conditioning) and are correctly excluded.

So every orthochronous interval-preserver satisfies all four conditions and is admissible; the only exclusions are the time-reversing transformations, by D7.1's one-wayness. ∎

### The flat tier, sealed

**(THEOREM, flat tier) [proved, modulo the cited prior materials] The admissible re-coupling symmetry of the conditioning-network N is exactly the proper orthochronous Lorentz group SO⁺(1,3), with invariant interval s² = −Δt² + (Δx¹)² + (Δx²)² + (Δx³)², and this is forced from N's intrinsic structure.**

Every component forced, with its source:
- **c = 1** — the depth/link unit-identity (F4); not a parameter.
- **spatial sum-of-squares** — continuous isotropy (SO(3)) from the total flattening of directional marking + rule-given continuum (F5, P16).
- **Lorentzian minus sign / null cone** — the unit-identity read as net-zero separation at the bound (F6, P15); the same fact as c = 1.
- **exactly the Lorentz group** — interval-preservation both inclusions (P12, P14), with admissibility = interval-preservation for orthochronous transformations (P17).
- **proper orthochronous specifically** — *derived* from From's one-way conditioning (P17, D7.1), not imposed: N does not admit time-reversing re-couplings.

The flat Lorentzian structure of physics is thereby recovered as forced from the conditioning-network, which is itself the horizontal build of the terminal mathematical object. Two particulars differ from the standard presentation and are themselves results: **c is the unit (= 1), not an empirical constant**, and **the orthochronous restriction is derived from one-way conditioning**, not postulated.

**Remaining for the whole gravity program (curved tier, not flat):** F8 (coherence-participation functional over next-configurations), F9 (the de-smuggled gravity tilt: the Hamiltonian-distribution raises toward-it coherence-participation, all quantities (P2)-admissible), F10 (coherence-weighting accumulates to curvature in the rule-given continuum limit), F11 (the relation is exactly the Einstein equation; G the one free particular, c the unit). The flat tier is now a sealed foundation for these.
