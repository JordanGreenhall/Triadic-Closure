# Mathematizing the Substrate: F1 (the conditioning-network as a formal object) and F2 (step atomicity)

### First computation of the gravity-mathematization survey. The conditioning-network is built as the horizontal build (lineage of takings) of the terminal mathematical object, deploying the Treatise's §6.10 lineage structure carrying the From-survey content (0.1–0.10). Every claim is tagged: **[proved]** (derived here from stated materials), **[forced-prior]** (established in a prior canonical document, cited not re-derived), **[argued]** (words, not yet a proof), **[open]** (named gap). Nothing locked before D7.

---

## 0. Materials (cited, not re-derived)

From the Treatise (Triadic Structure of Relating Rev Canonical) and the From-survey (physics checklist Part 0):

- **(M1) Lineage / turn-over / address.** [forced-prior, §6.10] A closure surveyed presents three aspects (conditioning / holding / arrived). Taking one aspect as a unit for the next determination is a **turn-over**. Iterating turn-overs generates an **address**: a record of which aspect of which prior closure was taken at each step. The address has character because it has lineage.
- **(M2) One-way takings; non-commutativity.** [forced-prior, §6.10] Each aspect-edge is a one-way From. Order of turn-overs matters (FT ≠ TF); identifying them would require an inverse to From, which does not exist. Non-commutativity is the lineage effect of one-way conditioning, not imported from algebra.
- **(M3) Unary reachability.** [forced-prior, §6.10] For a recursion taking one aspect at a time, every finite address can be walked, and distinct addresses remain distinct under non-commutativity. (Compound-nesting injectivity is open — does not bear on the unary substrate used here.)
- **(M4) Orientation-sourced discrete grading.** [forced-prior, 0.7] The integers at admissibility grade: ordinal counting by oriented succession (role-distinct positions in oriented chains). Counting is sourced from orientation, **not** from symmetric multiplicity — which carries no arity (the collapse theorem, 0.3/0.7).
- **(M5) ρ-coherence; monotone conservation.** [forced-prior, 0.5, 0.6] Recursive-coherence ρ holds finite-depth pieces into the whole and composes passages up to coherence. Registered distinctions are conserved monotonically — once registered, permanent; identifications provisional.
- **(M6) What the From does not supply.** [forced-prior, 0.10] Spacetime, dimension, metric, dynamics, and the completed continuum are **not** inherited. They must be shown realizable from the inherited content, never assumed.

---

## F1 — The conditioning-network as a formal object

### F1.1 The object, defined

The conditioning-network is **not** a graph embedded in a background space. It is the **horizontal build of the terminal object**: the structure of takings (M1) under one-way conditioning (M2). Define it directly from the materials.

**Definition (conditioning-network N).**
- **Nodes** of N are **standings** — actuals that have been taken. By (M1) each standing is reached by a finite address: a walk-history of turn-overs. Two standings are the **same node** iff they have the same address (M3: addresses individuate; unary reachability keeps distinct addresses distinct).
- **Edges** of N are **conditionings**: a directed relation A ◁ B ("A directly conditions B") holding iff B is reached from A by exactly **one** turn-over (one aspect of A taken as the unit yielding B). Edges are one-way (M2).
- N carries the inherited content at each node: the office-survey (0.1), J (0.2), the two sectors (0.3), the pairing (0.4). These ride on the standings; they are not extra structure added to the graph.

**(P1) [proved] N is a directed structure with no background.** The nodes are addresses (walk-histories), the edges are single turn-overs. Nothing in the definition references a position-in-space or an instant-in-time; "where" and "when" are *internal* — a node's location is its address, a node's time is its depth in the build (below, F2). So N is background-free by construction: it is the build, and the build is not *in* anything. This is exactly what (M6) requires — N must not presuppose spacetime/metric, and it does not.

### F1.2 The admissibility criterion for quantities (the anti-smuggle rule)

This is the payoff of building N from the object rather than as a free graph, and it is the structural fix for the recurring rate/density smuggle.

**(P2) [proved] A quantity on N is admissible iff it is definable from N's intrinsic data: addresses (lineage), edge-structure (one-way conditionings), node-content (offices, J, sectors, pairing), ρ-coherence, and conservation — and nothing else.** Proof: N's total content is exhausted by (M1)–(M5); (M6) states explicitly that no background measure (metric, dimension, spacetime) is inherited. A quantity referencing a background not in this list references content N does not have, hence is not a quantity *on N* but an import. ∎

**(C2.1) [proved] "Rate" and "density," as used in the prior gravity arguments, are inadmissible.** "Rate" = amount per unit *background time*; "density" = amount per unit *background space-region*. Both presuppose a background metric/measure, which by (M6) is not inherited and by (P2) is not definable on N. Therefore neither is an admissible quantity on N. This is *why* they smuggled: they are well-formed only against a background N does not supply. ∎

**(C2.2) [proved] "Coherence-participation" is admissible.** Coherence-participation of a configuration is its degree of ρ-coherence with the accumulated standing (the monotone-conserved lineage). Both ρ (M5) and the accumulated lineage (M1, M5) are intrinsic to N. Hence coherence-participation is definable on N and is admissible. ∎

This gives the standing discipline for all downstream gravity work: **every quantity must pass (P2); rate and density are banned by (C2.1); coherence-participation, address-distance, depth, and sector-content are the admissible primitives.**

### F1.3 Distance and the two intrinsic measures

N supplies exactly two intrinsic count-structures, and they are different in kind (this is the From/With seam, read on N):

- **Depth (the From-count).** The length of the address — how many turn-overs deep a standing is. Oriented (one-way, M2), hence ordered. [This will be time; F2 establishes its atomicity.]
- **Address-separation (the With-count).** Between two standings, the minimal number of conditioning-edges connecting them (shortest one-way-respecting chain). [This will be spatial distance; its three-fold flattened structure is F3, not treated here.]

**(P3) [proved] Depth and address-separation are distinct intrinsic measures, both definable on N, neither presupposing the other or any background.** Depth is a property of a single address (its length); address-separation is a relation between two addresses (connecting-chain-length). Both are counts of edges/turn-overs (M1, M4) — admissible by (P2). They are distinct because depth is monadic-ordered (one address, oriented) and separation is dyadic (two addresses); §F2 shows depth is atomic, and the From/With distinction (Treatise §7.4a) makes depth the oriented From-count and separation the symmetric With-count. ∎

---

## F2 — Step atomicity

**Claim to prove:** the step (one conditioning = one depth-increment) is **atomic** — there is no fractional conditioning, no continuum of sub-steps between a standing and the standing it conditions. The temporal substructure is genuinely discrete, and this is *forced*, not chosen.

### F2.1 The proof

**(P4) [proved] One conditioning is atomic.** A conditioning is one turn-over (M1): the taking of one aspect of one standing as the unit for the next. A turn-over is a single office-act — by the Treatise's stride discipline (no fourth operation; a determination is one act over standing materials), it does not decompose into sub-takings that are themselves turn-overs of the same build, because a "half-turn-over" would be a taking that has neither completed (no new standing yet) nor not-begun (no standing to be unit of) — it would be a standing that both is and is not at unit-altitude, which the closure discipline forbids (a standing either stands, at a definite address/depth, or it is not a standing). Hence a conditioning is indivisible: it either has occurred (a new address of depth n+1 stands) or it has not (only the depth-n standing stands). There is no intermediate. ∎

**(P5) [proved] Depth is discrete, sourced from orientation.** By (M4), counting is the orientation-sourced ℤ-grading: depth is the count of one-way takings along an address. Discreteness is *forced* by the source: the only arity-bearing structure is the oriented count (M4); symmetric multiplicity carries no arity (the collapse theorem). A *continuum* of sub-steps would require arity finer than the oriented count provides — i.e., a count of "how much of a turn-over" has occurred — but (P4) shows a turn-over has no proper parts, so there is no finer arity. Depth therefore takes values in the oriented discrete grade (ℤ⁺ along any address), with no values between successive depths. ∎

**(P6) [proved] The discreteness is forced, not a modeling choice.** Two independent routes converge:
1. *From atomicity (P4):* the turn-over has no proper parts, so there is nothing to count between depths.
2. *From the arity-source (M4, P5):* the only source of countable structure is oriented succession; it is intrinsically discrete (ordinal); and (M6) confirms no background continuum is inherited that could supply intermediate values. A continuum *along the step-direction* would have to be the *completed* classical continuum, which is **inadmissible — a theorem of the gate** (0.9). So a continuous time-substructure at the step level is not merely unchosen; it is *positively excluded* by the gate theorem. ∎

### F2.2 What F2 does and does not establish

- **Established:** the step is atomic (P4); depth (the From-count, = time in essence) is discrete, orientation-sourced, with no intermediate values (P5); and this discreteness is forced by atomicity, by the arity-source, and positively by the gate's exclusion of the completed continuum at the step level (P6).
- **Not established here (correctly deferred):**
  - That the *large-scale* temporal structure is a rule-given continuum (the smooth time of the metric) — this is a coarse-graining of the discrete depth, using the *rule-given* (not completed) continuum (0.9), and belongs to the continuum-limit gates (F10/F11), not here. F2's discreteness is the *substructure*; the rule-given continuum is its large-scale deployment. No conflict: discrete substructure, rule-given-continuous coarse-graining.
  - The atomicity of *spatial* separation (the link) — parallel but distinct; address-separation is a count of edges (M1), discrete by the same (M4) source, but its three-fold flattened structure (F3) is separate.

---

## Status after F1–F2

**Proved here:**
- **F1:** N is the background-free horizontal build of the terminal object (P1); the admissibility criterion for quantities (P2), with rate/density banned (C2.1) and coherence-participation admitted (C2.2); depth and address-separation as the two distinct intrinsic measures (P3).
- **F2:** the step is atomic (P4); depth is discrete and orientation-sourced (P5); discreteness is forced, including by the gate's exclusion of the completed continuum at step level (P6).

**The main result of the day — the anti-smuggle rule (P2, C2.1, C2.2):** every quantity in the physics reconstruction must be definable from N's intrinsic data (lineage/addresses, one-way edges, node-content, ρ-coherence, conservation). Rate and density fail this (they presuppose an un-inherited background); coherence-participation passes. This is the structural reason the smuggle recurred and the permanent discipline that prevents it.

**Re-homed / answered gates:**
- **F1** — answered: N is the §6.10 lineage build, not a free graph; formal definition given.
- **F2** — answered: step atomicity proved three ways.

**Next gates (in dependency order):**
- **F3** — exactly three spatial degrees: verify the floor-and-ceiling three is carried through the With-flattening of address-separation (cite Treatise floor/ceiling; confirm "exactly three," not "≥ three").
- **F4** — c as the depth/separation identity at metric level (mostly notational, given F1.3's two measures).
- **F5/F6** — the flat metric form (sum-of-squares from isotropy) and signature (minus sign from the null bound), read off the J-compatible pairing (0.4) + J (0.2).
- **F7** — the owed proof: the admissible re-couplings of N (J-compatible, pairing-preserving) are exactly the Lorentz group.
- **F8/F9** — coherence-participation functional over next-configurations; Hamiltonian-distribution raising toward-it coherence-participation (the de-smuggled gravity tilt), now constrained to be (P2)-admissible.
- **F10/F11** — the rule-given (not completed) continuum limit; curvature; the Einstein equation with G as the one free particular and c as the unit (not a particular).
