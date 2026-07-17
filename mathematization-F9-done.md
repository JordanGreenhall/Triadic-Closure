# F9, Done Properly: The Standing Vector σ, and the Gravity Tilt Derived as Exactly Linear in Conditioning-Degree

### Builds on F8 (the next-configuration space (V, h) and the conditional functional C(k) = |h(σ,k)|²/h(k,k)). M5 does not supply the positive-definite physics pairing assumed by F8; every F9 result therefore inherits that unresolved condition. Within it, this document constructs the standing vector σ and computes the tilt. The result is stronger than the prose F9 (P20) claimed: the coherence-participation of P coupling to neighbor i is not merely *monotone* in i's conditioning-degree but **exactly linear** in it. Every non-trivial step is checked by computation; scripts and outputs are recorded. Tags: **[def]**, **[derived]** (within stated conditions), **[checked]** (computed), **[choice]** (a modeling selection, flagged honestly).

---

## 1. What σ must be

From F8: σ ∈ V is the accumulated standing projected onto P's coupling-options, with σ_i = h(σ, e_i) the standing's coherence-amplitude for the elementary coupling "P conditions neighbor i next." The owed task: construct σ_i explicitly from the standing, and find its dependence on the neighbors' structure — without assuming the dependence.

## 2. The construction of σ — derived, not assumed

The standing is the already-built conditioning-network. The coherence-amplitude σ_i for the link P→i is determined by how strongly node i is already coherently woven into the standing — coupling P to a well-woven node extends the existing coherence; coupling to an isolated node does not. The construction proceeds in two derived links.

**[derived, link 1] The conserved coherence-measure on the standing is the conditioning-degree.** ρ-coherence (0.5) is coherence that *composes and conserves* (0.6: registered distinctions are conserved). The object that carries conserved coherence across the network is the **conserved coherence-flow** — the stationary state of the coherence-flow on the conditioning-network. For a flow (random-walk) operator on a network, the stationary measure is exactly

> π_i ∝ d_i, where d_i = the conditioning-degree of node i (the count of conditionings incident at i).

**[checked]** (`sigma_check2.py`): the random-walk stationary distribution π_i = d_i/Σ_j d_j is exactly stationary (πP = π to machine precision, max error ~10⁻¹⁸). This is the framework's conserved-coherence object; its measure is the conditioning-degree. (Note: conditioning-degree is the F9/P19 admissible cash-value of "energy/Hamiltonian at a node" — an edge-count, not a density.)

**[derived, link 2] The amplitude is the square root of the conserved measure.** The pairing (0.4) and the Born structure established in F8 give the relation amplitude² = measure (coherence-participation, the C-functional, is the squared modulus of the amplitude). So the coherence-*amplitude* is the square root of the conserved coherence-*measure*:

> σ_i = √(π_i) = √(d_i) / Z, with Z = √(Σ_j d_j).

**[checked]** (`sigma_check2.py`): with σ_i = √(π_i), the log-log slope of σ_i versus d_i is exactly 0.5 and corr(σ_i, √d_i) = 1.0.

(Contrast — why this is the right object, recorded for honesty: the *bare adjacency* leading eigenvector gives σ_i ∝ d_i^≈0.5 only noisily — correlation ~0.4, with large structural scatter (`sigma_construct.py`), because it is a global eigenvector sensitive to more than local degree. The **conserved-flow** stationary amplitude gives the clean exact √d_i. The selection of the conserved-flow object over the bare-adjacency object is a **[choice]**, but a motivated one: ρ is conservation (0.5/0.6), so the conserved-flow stationary state is the framework-correct coherent object, and it is the one that makes the measure conserved. This choice is flagged, not buried; discharging it fully means showing the conserved-flow object is *forced* by ρ/conservation, not merely consistent with it.)

## 3. The tilt (F9), computed — exactly linear in conditioning-degree

With σ_i = √(d_i)/Z and the elementary couplings h-orthonormal (h = I in this basis), compute C for the elementary coupling k = e_i (P couples purely to neighbor i):

> C(e_i) = |h(σ, e_i)|² / h(e_i,e_i) = |σ_i|² = d_i / Σ_j d_j.

**[checked]** (`sigma_F9.py`, N = 120 random standing): C(e_i)/d_i is constant across all neighbors (std/mean = 0.0); C(e_i) = d_i/Σ_j d_j exactly; C(e_i) is monotone increasing in d_i.

So the gravity tilt is **exactly linear** in the neighbor's conditioning-degree:

> **C(e_i) = d_i / Σ_j d_j**, and P couples to neighbor i with probability **P(i) = d_i / Σ_j d_j**.

The √ in the amplitude (link 2) and the squaring in C (Born, F8) cancel: amplitude = √(degree), participation = amplitude² = degree. Born's squaring exactly undoes the amplitude's square-root, leaving coherence-participation linear in the conserved measure (degree).

## 4. What this establishes, and what it strengthens

- **F8's owed piece (σ) is constructed** [derived + checked]: σ_i = √(d_i)/Z, from two framework links — conserved coherence-measure = degree (0.6), amplitude = √measure (0.4/Born).
- **F9 (the tilt) is computed and strengthened.** The prose F9 (P20) argued only monotonicity. The construction gives the exact law C(e_i) = d_i/Σ_j d_j — **coherence-participation linear in conditioning-degree**. The gravity tilt toward high-conditioning-degree (= high-Hamiltonian = high-energy) nodes is now an explicit, exactly-linear law, fully F1.2-admissible (degree is an edge-count; C is the pairing functional; no rate, no density anywhere).
- **The coupling-to-energy is exact, not just qualitative.** P's selection weights neighbors *linearly by their conditioning-degree* — gravity couples to energy because coherence-participation of a coupling is exactly the (normalized) conditioning-degree of its target.

## 5. Honest status

**Established (derived + computed):**
- σ_i = √(d_i)/Z (the standing vector, explicit). [derived, checked]
- C(e_i) = d_i/Σ_j d_j (the tilt, exactly linear in degree). [checked]
- P(i) = d_i/Σ_j d_j (the selection probability over next-couplings). [checked]

**Flagged choices / owed:**
- **[condition]** The positive-definite physics pairing assumed by F8 remains separately owned; M5's perfect rational form and conditional M6 Hermitian extension do not discharge it.
- **[choice]** The standing-state is the conserved coherence-flow stationary amplitude (not the bare adjacency eigenvector). Motivated by ρ = conservation, and it is what makes the measure conserved — but "forced by ρ" is owed; currently "the framework-consistent choice," not "the unique choice."
- **The continuum step is still ahead (F10).** This gives the *per-step, discrete* tilt law (linear in degree). Whether this discrete linear-in-degree weighting accumulates, in the rule-given continuum limit, to exactly the metric curvature (the cone-tilt tensor) is **F10** — still the open frontier. F9 supplies F10's input (an explicit, exactly-linear local tilt law) in clean admissible form, which is exactly what a curvature computation needs.

**The chain, end to end:** conserved coherence-flow ⇒ measure = conditioning-degree (0.6) ⇒ amplitude = √degree (0.4/Born) ⇒ C(e_i) = degree/Σdegree (the tilt, linear). Each arrow a framework fact; the one selection (conserved-flow object) flagged. This is the de-smuggled gravity tilt as an explicit law, ready for the F10 continuum/curvature computation.

---

### Appendix: scripts (run, outputs recorded above)
- `sigma_construct.py` — bare-adjacency eigenvector: σ_i ∝ d_i^≈0.5 but noisy (corr ~0.4); shows degree alone underdetermines the adjacency eigenvector.
- `sigma_check2.py` — conserved coherence-flow: stationary measure π_i ∝ d_i exactly (error ~10⁻¹⁸); amplitude √π_i gives slope exactly 0.5, corr 1.0.
- `sigma_F9.py` — the tilt: C(e_i) = d_i/Σ_j d_j exactly; monotone; linear in degree.
