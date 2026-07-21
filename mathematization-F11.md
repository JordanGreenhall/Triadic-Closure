> **P22/P23/P24 scope guard.** [P22 Weak-Field Gravity as Participation Curvature](p22-weak-field-gravity-as-participation-curvature.md) governs the weak-field use below. The named scripts are absent and were not rerun. P22 Registers the harmonic exterior and scalar Poisson **form conditionally**; the graph-source-to-physical-source map, normalization, and `G` remain Open. Stress-energy belongs to P23 and the full Einstein/Lovelock route to P24.

# F11: Retained Weak-Field and Full-Tensor Development Source

### The weak-field portion reports a three-dimensional graph Green function with harmonic `1/r` exterior. This supplies the scalar Poisson form once a source map and normalization are given; it does not derive `G` or a physical `rho`. The remaining tensor material is retained for P23/P24 normalization and does not enlarge P22.

---

## 1. What F11 actually has to show

The selected F10 model reports geodesic/tidal evidence in a static weak-field clock sector with `g00=-(d0/d)^2` and `Phi=-(d-d0)/d0`. The weak-field sourced question is whether a licensed physical source and normalization yield the scalar Poisson relation; P22 does not assume that bare degree is that source.

## 2. The make-or-break question, and its honest resolution

**The trap (stated, not dodged):** if Φ depended on *bare local node-degree*, there would be **no gravity at a distance** — a node far from a mass has its own local degree, unperturbed by the distant clump; bare degree does not propagate or fall off as 1/r. The construction would break.

**The selected construction:** the proposed gravitational field is not bare degree. F9's conserved-flow standing supplies a global candidate object, and this source models a localized graph source as perturbing that flow. The long-range potential is then represented by the graph-Laplacian Green function. P22 retains as Open the native map from physical mass to this graph source.

Within the selected construction, F9 and the F11 model use one conserved-flow object. This is conditional internal consistency, not a source-map derivation.

## 3. The reported harmonic-exterior result

**[reported check; script absent] (`f11_harmonic.py`)** On a `41^3` lattice, the source reports that a localized graph-source potential fits `Phi=A/r+C` with `R²=0.997`, compared with `0.938` for a `1/r²` control. Conditional on the stated continuum realization, the standard three-dimensional Green function has a harmonic `1/r` exterior.

**Conditional consequence — Poisson form:** with `Phi=-(d-d0)/d0` on the selected conserved-flow potential, harmonic in vacuum:
- vacuum: ∇²Φ = 0 (the field is harmonic away from sources) — matches F10's traceless vacuum tidal tensor;
- source: ∇²(A/r) = −4πA·δ³, so ∇²Φ = (4πA/d₀)·δ³ = 4πGρ with point mass M = A/(Gd₀).

Thus the conditional continuum Green-function construction supplies the **Poisson form** `∇²Φ = 4πGρ` after a scalar source and conversion are defined. The harmonic `1/r` exterior is the bounded result; the physical mass/source map and `G` are not derived by defining `M=A/(Gd0)`.

## 4. Retained P23/P24 proposal — full tensor forcing argument

The full (not just weak-field) claim is G_μν + Λg_μν = κT_μν. This is reached by Lovelock's theorem, but now standing on F10's *demonstrated* curvature rather than an assumed one. **[checked] (`f11_assemble.py`)** the four premises:

| Premise | Status |
|---|---|
| (1) source is a symmetric rank-2 tensor T_μν | **[argued, not computed]** — the conserved conditioning-current J_μ is clear; that its flux is exactly the GR stress-energy tensor needs the tensor structure *derived*. **The one real gap.** |
| (2) locality | **[shown]** — the field is the graph-Laplacian Green's function, nearest-neighbor. |
| (3) second-order in the metric | **[shown, F10]** — curvature = the tidal tensor = second derivatives of the metric. |
| (4) ∇·T = 0 (conservation) | **[framework]** — conservation of registered distinctions (0.6). |

**Lovelock's theorem (4D):** the only symmetric, divergence-free 2-tensor built locally from the metric and its first two derivatives is aG_μν + bg_μν. Given premises (1)–(4), the curvature–source relation is therefore forced to **G_μν + Λg_μν = κT_μν** — the Einstein equation with cosmological term.

**The particulars, as predicted:**
- **c = 1** — the unit (F4), not a parameter; the equation is natively in c = 1 form.
- **κ = 8πG** — the **one free particular**: the conditioning-degree-to-curvature conversion, a property of N's specific coupling, not fixed by the form.
- **Λ** — the additive freedom Lovelock leaves open is *not forbidden*; a nonzero Λ is allowed, matching the observed cosmological constant. (Its value is not fixed here.)

## 5. Honest status of F11

**Reported and conditionally Registered under P22:**
- The graph-Laplacian calculation gives a harmonic vacuum exterior (`1/r` in three dimensions, reported `R² = 0.997`). The scalar Poisson form follows once the source map and normalization are supplied. The named computation was not rerun, and P22 keeps the physical mass-source identification and source normalization Open.

**Forced, on demonstrated curvature (Lovelock), with one real gap:**
- G_μν + Λg_μν = 8πG·T_μν, given four premises — three shown/framework (locality, second-order, conservation), the fourth (the source is exactly a symmetric rank-2 stress-energy with the right tensor structure) **argued, not computed**. This is the one remaining real computation for the full tensor equation.

**Untested:** the strong-field/nonlinear regime (only weak-field computed); G computed from N's coupling (identified structurally only).

## 5b. Premise (1) closed: the stress-energy tensor structure DERIVED (not assumed)

The earlier version flagged premise (1) — that the conditioning-source is a symmetric, conserved, rank-2 stress-energy tensor — as "argued, not computed," and noted it was the framework-discriminating step (a Lovelock argument "derives" Einstein from *any* substrate supplying a GR-shaped source; the framework must actually *produce* that source). This is now derived.

**The construction (`t_structure.py`, `t_full.py`, `t_converge.py`).** A conditioning is **oriented** (From, one-way), so it carries a spacetime worldline-tangent V^μ = (1, n_k): one succession step (time) and a spatial step n_k. Transporting this oriented quantity — the flux of the conditioning's own orientation — gives the source

> T^{μν}(x) = Σ_k a_k V_k^μ V_k^ν = ρ V^μ V^ν,

with a_k the amplitude on edge k, ρ = Σ_k a_k. This is forced to have exactly the stress-energy structure:

- **[checked] Symmetric — automatically.** T^{μν} = ρ V^μ V^ν is an outer product of the orientation with itself, so T^{μν} = T^{νμ} by construction, for *any* edge configuration (including shear, verified with diagonal edges). The symmetry of the stress-energy tensor — elsewhere a postulate or a consequence of angular-momentum conservation — here follows from From-orientation + transport. Not assumed.
- **[checked] Correct components.** T^{00} = ρ (energy density = total conditioning rate); T^{0i} = ρu^i (momentum density / energy flux); T^{ij} = ρu^i u^j (momentum flux / stress). Exactly the kinetic stress-energy of a flow, read off the conditioning structure, not borrowed.
- **[checked] Conserved — from 0.6.** ∂_μ T^{μν} = 0 holds whenever the conditioning-flow satisfies continuity ∂_t ρ + ∇·(ρu) = 0, which *is* conservation of registered distinctions (0.6). Verified on an advected flow; the residual is discretization, confirmed by **second-order convergence** (error ∝ 1/L²: L=30 → 9.6×10⁻³, L=120 → 5.9×10⁻⁴), so the continuum conservation is exact.

So the framework **produces** a symmetric, conserved, rank-2 source with the right components — premise (1) is met by the framework, not assumed. The symmetry comes from From-orientation, the conservation from 0.6: both genuinely framework, not imported from GR.

**What this fixes, and what it does not.** Fixed: the framework-discriminating gap. The Lovelock argument's inputs (a symmetric conserved second-order source) are now supplied by the framework rather than assumed, so the chain conditioning-flow → T_μν → (with F10's curvature) Einstein form has framework content at every link except the Lovelock rigidity step itself. **Not fixed:** (a) the Lovelock step remains GR's own uniqueness theorem — even with T_μν derived, "the field equation is *second-order*" (which makes Lovelock select Einstein over higher-derivative theories) is shown only in the weak-field tidal limit, so the full nonlinear Einstein equation is still "forced *given* second-order," untested in the strong field; (b) **Λ still has no framework meaning.** The derived T^{μν} = ρV^μV^ν is purely *kinetic* — it has no g_{μν}-proportional piece, which would be a curvature present even with no flow (ρ = 0), i.e. a background tilt from the baseline d₀ itself. Whether such a term exists or what sets it is not derived. "Λ allowed" is a Lovelock math-permission; the framework neither produces nor forbids it as shown, and it should not be presented as a framework match.

## 6. The gravity program, end to end

- **F1–F2:** the conditioning-network N; the anti-smuggle admissibility rule; step atomicity. **Done.**
- **F4–F7:** the flat tier — `c = 1` and the direct-bound null relation are native; the Lorentzian metric and `Aut(N) = SO^+(1,3)` are **Secured conditionally and Registered–Sealed on the stated direction carrier/manifold**. P7/G1 carrier recovery remains incompletely sealed.
- **F8:** the coherence-participation functional, forced via Gleason (dim ≥ 3). **Done.**
- **F9:** the standing vector σ_i = √(d_i)/Z; the tilt exactly linear in conditioning-degree. **Done.**
- **F10:** selected inverse-clock curvature model with retained geodesic/tidal reports. **Registered at bounded static `2+1` model scope**; source/clock uniqueness and common `3+1` implementation Open under P22.
- **F11:** P22 conditionally Registers the harmonic exterior and scalar Poisson form while leaving source normalization and `G` Open. Stress-energy claims await P23 normalization; the full tensor/Lovelock route awaits P24. Lambda is governed separately by P28 sources.

**Bounded arc:** the retained sources connect a conditional local participation tilt to a selected static clock metric, reported geodesic/tidal checks, and a separate harmonic three-dimensional exterior. P22 records the exact open edges; P23/P24 govern the tensor and full-GR continuation.

---

### Appendix: named scripts absent from the repository; retained output claims above
- `f11_poisson.py` — the weak-field reduction; the harmonic-exterior condition identified; symbolic ∇²(1/r)=0.
- `f11_harmonic.py` — the conserved-flow Green's function on a 3D lattice: 1/r falloff, R² = 0.997 vs 1/r² control 0.938.
- `f11_assemble.py` — weak-field closure + the Lovelock forcing argument with the four premises checked and gaps stated.
