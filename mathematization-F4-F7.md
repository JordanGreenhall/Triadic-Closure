# Mathematizing the Flat Substrate: F4 (c as metric identity), F5 (sum-of-squares), F6 (Lorentzian signature), F7 (the Lorentz group)

### Second computation of the gravity-mathematization survey, building on F1–F2 (the conditioning-network N, the anti-smuggle admissibility rule, step atomicity). This tier gives a conditional derivation of the flat metric and Lorentz re-couplings while locating the still-open continuous-direction-carrier premise. Tags: **[proved]** (derived here), **[forced-prior]** (cited), **[argued]** (words, not full proof), **[open]** (gap), **[conditional]** (depends on a named construction). The discipline of F1.2 (P2) is in force: every quantity must be definable from N's intrinsic data; rate/density are banned.

---

## 0. Inherited from F1–F2

- **(N)** The conditioning-network: nodes = standings (individuated by address/lineage), edges = single one-way turn-overs (conditionings). Background-free.
- **Succession count** = address-length = the From-count (oriented, discrete, atomic — F2). The temporal substructure.
- **Address-separation** = minimal connecting-chain length = the With-count (symmetric). The spatial substructure; three-fold by the flattening (F3, taken as established: floor-and-ceiling three carried through the With-flattening).
- **(P2)** Admissibility rule: a quantity is admissible iff definable from N's intrinsic data (addresses, edges, node-content, ρ, conservation). Rate/density banned; coherence-participation and the two counts admitted.
- **Node-content:** offices (0.1), **J** = involutive polarity, orientation-reversal, J²=id (0.2, Treatise §7.2), the two sectors (0.3), and the pairing at its certified grade (0.4). Canonical M5 constructs a perfect rational bilinear form; canonical M6 supplies a complex Hermitian extension only at a selected closed rule-calculus grade. The Lorentz-signature form and continuum of directions used below are physics-specific constructions and may not be inferred from either unit alone.

---

## F4 — c as the succession-count/separation identity (at metric level)

**(P7) [proved] The unit of succession count and the unit of separation are the same unit — one conditioning — and their identity is c = 1.** A unit of succession count is one turn-over along an address (one conditioning, counted as temporal advance). A unit of separation is one edge between addresses (one conditioning, counted as spatial step). By F1.3 these are the *same* intrinsic act (a conditioning) read under the two counts (From-count vs With-count). The conversion between them is therefore the identity: 1 edge of separation ↔ 1 increment of succession count. Writing this conversion as c, **c = 1 by construction** — it is not a magnitude but the identity between the two namings of the unit act. ∎

**(C7.1) [proved] c is admissible and is not a free particular.** c is definable from N's edge/succession-count structure (P2-admissible) and equals 1 necessarily (P7). Contrast: in standard relativity c is an empirical constant carrying a large numerical value; here that value is an artifact of measuring succession count and separation in unrelated units. On N there is one unit (the conditioning), so c = 1 is forced. **This is the first confirmed "different particular": c is the unit, not a parameter.** ∎

---

## F5 — The spatial metric is the sum of squares (from isotropy)

**Setup.** Address-separation gives, between two standings, a chain-length along each of the three flattened With-degrees (F3). Write the separation components (Δx¹, Δx², Δx³). The spatial interval is some combination σ(Δx¹, Δx², Δx³). The question: which combination?

**(P8) [proved for permutation symmetry; continuous extension Open] The three spatial degrees are pairwise interchangeable by an admissible symmetry.** [forced-prior + here] The three degrees are the With-flattening of the marked triad: the flattening blinds the kind-marking, so permutations of the three preserve the displayed degree-structure. This establishes `S₃` interchangeability. It does not by itself construct intermediate directions, a topology, or continuous rotations; those are exactly the F5a dependency below.

**(P9) [proved conditional on continuous isotropy] An isotropic, additive, sign-definite interval on three continuously interchangeable degrees is the sum of squares (up to scale).** Given a separately constructed continuous rotation action, the standard invariant-form argument yields `δᵢⱼΔxⁱΔxʲ`. `S₃` permutation symmetry alone does not exclude other symmetric norms and therefore does not discharge this premise.

*Status of F5:* **[conditional]** on F5a. Permutation symmetry is established, but continuous interchangeability is not. Canonical M6 supplies neither a topology nor deployment of rule-presented scalars on the spatial degrees. Sub-gate F5a must construct the physical direction carrier and its continuous `SO(3)` action.

---

## F6 — The signature is Lorentzian (the minus sign), from the null bound

**Setup.** Succession count (time, Δt) and the spatial interval combine into a single interval (F4: one unit). Write s = α(Δt) + β·σ(Δx) for some combination. The question: the relative sign/structure of the succession-count part and the space-part.

**(P10) [proved] The null condition: a directly-conditioning pair has zero interval.** Two standings one edge apart in separation and one succession-count increment apart (Δt = 1, |Δx| = 1, in unit terms) are in **direct conditioning contact** — one is the immediate conditioning of the other. Direct contact is the limiting case of "separation": the pair are as close as conditioning allows (neighbors). The interval between immediate-conditioning neighbors propagating at the bound (v = 1, F4) must be the **zero of the interval** — they are not separated *along the propagation*, since the propagation *is* their contact. (Admissible: this uses only succession count, separation, and the v ≤ 1 bound, all intrinsic.) So the interval vanishes when |Δx| = Δt. ∎

**(P11) [proved] The interval is quadratic in succession count with opposite sign: s² = −(Δt)² + σ(Δx) = −(Δt)² + (Δx¹)²+(Δx²)²+(Δx³)².** Proof: by F5 the spatial part is the sum of squares. The full interval must (i) reduce to the spatial sum-of-squares at equal succession count (Δt = 0), and (ii) **vanish on the null condition** |Δx|² = (Δt)² (from P10: |Δx| = Δt ⇒ s = 0). A combination of (Δt)² and |Δx|² vanishing exactly when |Δx|² = (Δt)² is, up to scale, |Δx|² − (Δt)². Adding any non-quadratic dependence on Δt breaks (ii) at general separations (the null set would not be the cone |Δx| = Δt). So the interval is s² = −(Δt)² + |Δx|², with one timelike sign opposite to the three spacelike — **Lorentzian signature (1,3)**. The minus sign is forced by the null condition (P10), which is forced by the propagation bound (F4). ∎

*Status of F6:* **[proved]**, given F5 and the null condition (P10). The one substantive input is (P10) — that immediate-conditioning neighbors at the bound are zero-interval — which is **[argued]** cleanly (direct contact = not-separated-along-propagation) but deserves an explicit check that "zero interval" is the *forced* reading and not merely natural. Sub-gate F6a: pressure-test P10.

---

## F7 — The admissible re-couplings of N are exactly the Lorentz group

This is the owed proof. **Claim:** the group of admissible re-couplings of N — the transformations that re-split a separation into succession-count-versus-spatial parts while preserving N's structure — is exactly the Lorentz group O(1,3) (or its identity component SO⁺(1,3)).

### F7.1 What an admissible re-coupling is (defining the group)

**(D7) [definition, framework-bound] An admissible re-coupling is a transformation T of N's separations that:**
1. **preserves the conditioning structure** — maps conditioning-chains to conditioning-chains, respecting one-way orientation (it is a symmetry of the edge-structure, M2);
2. **preserves the unit** — one conditioning maps to one conditioning (c = 1 is preserved; F4);
3. **is J-compatible** — commutes with J (orientation-reversal), since J is constitutive node-content (0.2) and a symmetry of N must respect it;
4. **preserves the physics form** — the re-coupling preserves the separately constructed Lorentz-signature form. This is not merely inheritance of M5's rational bilinear witness; compatibility with J and the M5/M6 scalar structure must be checked after the physics form is built.

These four conditions are not chosen for convenience; each is “a symmetry of N must preserve the certified structure actually used” — edges/orientation, unit, J, and the constructed physics form. Admissible by (P2), conditional on the form's own construction.

### F7.2 The interval is preserved

**(P12) [proved, conditional on the F5/F6 physics form] Every admissible re-coupling preserves the interval s² = −(Δt)² + |Δx|².** Proof: the interval is built in F5/F6 from the separately constructed spatial and null structures. Condition (D7.4) preserves that physics form, and (D7.1–D7.2) preserve orientation and unit. This conclusion does not follow merely from M5's rational pairing witness. ∎

So Aut(N, re-coupling) ⊆ O(s²) = O(1,3): every admissible re-coupling is an interval-preserving transformation, i.e. a Lorentz transformation.

### F7.3 The converse — every Lorentz transformation is an admissible re-coupling

This is the harder direction (showing the group is *exactly* Lorentz, not a subgroup).

**(P13) [argued → partially proved] Every interval-preserving transformation is realized by an admissible re-coupling of N.** The Lorentz group O(1,3) is generated by (a) **spatial rotations** SO(3), and (b) **boosts** (the succession-count↔spatial mixings). Take each:

- **Rotations** are admissible re-couplings only after F5a supplies the continuous isotropy of the spatial carrier. Given that construction, they preserve edges, unit, J, and the F5/F6 physics form, so SO(3) ⊆ Aut(N). **[proved, given F5a and the form].**
- **Boosts** are the re-splittings of a separation into succession-count-versus-spatial parts — exactly the “re-coupling” of F1/propagation: a different admissible accounting of the same conditioning-separation as more-succession-count/less-spatial or vice versa, preserving the interval and the unit. A boost re-coordinatizes the same conditioning-chains and preserves the separately constructed interval form; J-compatibility must be checked against the succession-count/spatial structure. So boosts ⊆ Aut(N). **[argued]** — the load-bearing sub-claim is that *every* interval-preserving boost corresponds to an admissible re-splitting. Sub-gate F7a.

**(P14) [proved, given P13] Aut(N, re-coupling) = O(1,3) (or SO⁺(1,3) for the orientation-and-time-direction-preserving part).** From P12, Aut(N) ⊆ O(1,3). From P13, the generators of O(1,3) (rotations + boosts) are in Aut(N), so O(1,3) ⊆ Aut(N). Hence equality. Restricting to (D7.1)'s one-way orientation-preservation (conditioning runs one way) selects the **orthochronous** part (time-direction-preserving), and to the proper part if reflection is excluded: SO⁺(1,3), the connected Lorentz group. ∎

### F7.4 Status of F7

**[proved]** that Aut(N) ⊆ O(1,3) (P12) and that the interval is preserved; **[proved]** that rotations are admissible (given F5a); **[argued]** that all boosts are admissible re-couplings (P13, the converse for boosts) — this is the one remaining substantive gap, **sub-gate F7a**: show every interval-preserving boost is an admissible re-splitting of N's separations (no interval-preserving boost is excluded by D7.1–D7.4). If F7a holds, F7 is sealed: the re-coupling symmetry of N is exactly the connected Lorentz group, which is the flat-metric seal owed since the metric-maturation walk.

The orthochronous restriction is itself a **result, not an input**: because conditioning is one-way (M2), the admissible group is the *time-direction-preserving* part — N does not admit the time-reversing Lorentz transformations as re-couplings. This matches the physical fact that the orthochronous proper Lorentz group is the physical symmetry, and it falls out of From's one-wayness.

---

## Status after F4–F7

**Proved:**
- **F4:** c = 1 is the succession-count/separation unit-identity, forced, not a particular (P7, C7.1).
- **F5:** the spatial metric is the sum of squares, forced by isotropy + additivity + sign-definiteness (P9), modulo F5a (isotropy is continuous SO(3)).
- **F6:** the signature is Lorentzian (1,3), the minus sign forced by the null condition from the propagation bound (P11), modulo F6a (P10 pressure-test).
- **F7:** Aut(N, re-coupling) ⊆ O(1,3) proved (P12); rotations admissible; the full equality Aut(N) = SO⁺(1,3) proved modulo F7a (boost-admissibility converse). The **orthochronous restriction is derived** from From's one-wayness, not imposed.

**Remaining sub-gates to seal the flat tier:**
- **F5a:** construct a physical rule-presented direction carrier, select and audit its M6 rule calculus, and prove that its admissible symmetry is the continuous rotation group rather than merely discrete permutations.
- **F6a:** pressure-test the null condition (P10) — that immediate-conditioning neighbors at the bound are forced to zero-interval.
- **F7a:** the converse for boosts — every interval-preserving boost is an admissible re-coupling of N (no admissibility condition excludes any boost).

These three are concrete and finite; clearing them seals the flat Lorentzian metric and the Lorentz-group symmetry as forced from N. Then the tier is complete and the curved/Einstein gates (F8–F11) follow, with the F1.2 admissibility rule (no rate, no density) carried into the gravity-tilt computation.

**Confirmed structural particulars (our model vs. standard):** c is the unit (= 1, forced), not an empirical parameter; the orthochronous restriction is derived from one-way conditioning, not postulated. Both are points where our grounding differs from the standard presentation while recovering the same flat structure.

---

## F5a, F6a, F7a — reassessment of the three sub-gates

**(P15) [proved] F6a — the null condition is forced; it is the unit-identity.** At the bound v = 1, one succession-count increment is spent entirely traversing one link of separation — and by F4 the succession-count increment and the spatial-link are the *same single conditioning* counted two ways. So Δt = 1 and |Δx| = 1 at the bound are not two separations but one act counted both ways; the *net* separation (the interval) is that one act minus itself, = 0. The interval's vanishing on the null cone is therefore not an independent assumption but c = 1 (F4) read as "one act, counted as both succession count and link, nets to zero": s² = −Δt² + |Δx|² = −1 + 1 = 0. The minus sign (F6) and the null cone are the same fact as the unit-identity (F4). ∎

**(P16) [Open / conditional] F5a — continuous `SO(3)` isotropy is not supplied by M6 or flattening alone.** Flattening removes registered kind-marking among directions that have been constructed. It does not construct intermediate directions, a topology on the direction space, or a continuous group action. M6 supplies rule-presented scalar schemas only relative to a selected closed rule calculus, and it does not deploy those scalars on this physical carrier. A model with only three permuted axes remains compatible with the displayed premises. To discharge F5a, a physics construction must exhibit the rule-presented direction carrier and prove that its admissible automorphisms contain the required rotation action.

**(P17) [proved conditional on the F5/F6 carrier and form] F7a — every orthochronous interval-preserving transformation is an admissible re-coupling; only the time-reversing ones are excluded.** Once the rule-presented direction carrier, continuous action, and Lorentz form are separately supplied, check D7.1–D7.4 against an arbitrary orthochronous interval-preserver:
- *D7.2 (unit):* c = 1 is the null structure of the interval (F4/F6); an interval-preserver preserves it. ✓
- *D7.4 (physics form):* the interval is the F5/F6 Lorentz-signature form; an interval-preserver preserves it by construction. This is not an inference from M5's rational pairing. ✓
- *D7.3 (J-compatible):* the (1,3) signature is exactly the J-eigenstructure (time = J-odd/orientation-carrying, space = J-even); preserving the interval preserves the signature-split, hence commutes with J. Automatic, not an extra constraint. ✓
- *D7.1 (edges + orientation):* a conditioning-chain is a sequence of future-directed within-cone links (each |Δx| ≤ Δt). An orthochronous transformation preserves the null cone and maps future-directed timelike/null vectors to future-directed timelike/null vectors, hence within-cone links to within-cone links — conditioning-chains to conditioning-chains, orientation respected. ✓ The *non*-orthochronous (time-reversing) transformations fail D7.1 (they reverse one-way conditioning) and are correctly excluded.

So every orthochronous interval-preserver satisfies all four conditions and is admissible; the only exclusions are the time-reversing transformations, by D7.1's one-wayness. ∎

### The flat tier, conditional

**(THEOREM, flat tier) [conditional] Given a physics-side rule-presented direction carrier with continuous `SO(3)` action, the Lorentz-signature form, and the stated re-coupling premises, the admissible re-coupling symmetry is the proper orthochronous Lorentz group `SO⁺(1,3)`. M6 does not discharge those physics premises.**

Every component forced, with its source:
- **c = 1** — the succession-count/link unit-identity (F4); not a parameter.
- **spatial sum-of-squares** — conditional on the still-open physics construction of a rule-presented direction carrier and continuous `SO(3)` action (F5, P16).
- **Lorentzian minus sign / null cone** — the unit-identity read as net-zero separation at the bound (F6, P15); the same fact as c = 1.
- **exactly the Lorentz group** — interval-preservation both inclusions (P12, P14), with admissibility = interval-preservation for orthochronous transformations (P17).
- **proper orthochronous specifically** — *derived* from From's one-way conditioning (P17, D7.1), not imposed: N does not admit time-reversing re-couplings.

The conditional derivation identifies exactly what would recover the flat Lorentzian structure from the conditioning-network. It does not yet construct the continuous direction carrier. Two particulars within the conditional line differ from the standard presentation: **c is the unit (= 1), not an empirical constant**, and **the orthochronous restriction follows from one-way conditioning**, rather than being separately postulated.

**Remaining for the gravity program:** F5a now explicitly requires selection and closure of the M6 rule calculus, construction of a physical direction carrier, and proof of its continuous rotation action. F8–F11 retain their stated additional conditions, including the continuum-limit and curvature debts. The flat tier is not sealed until the F5a carrier/deployment gap is discharged.
