> **P22/P23/P24 scope guard.** [P22 Weak-Field Gravity as Participation Curvature](p22-weak-field-gravity-as-participation-curvature.md) governs the weak-field use below. [P23 Stress-Energy as a Three-Office Source](p23-stress-energy-as-three-office-source.md) governs source construction and conservation. [P24 Full Einstein Form as Conditional Tensor Rigidity](p24-full-einstein-form-as-conditional-rigidity.md) governs the retained forcing proposal. The named scripts are absent and were not rerun. Neither locality, source kinematics, nor the theorem's form supplies the missing P24 premise map.

# F11: Retained Weak-Field and Full-Tensor Development Source

### The weak-field portion reports a three-dimensional graph Green function with harmonic `1/r` exterior. This supplies the scalar Poisson form once a source map and normalization are given; it does not derive `G` or a physical `rho`. The remaining tensor material is retained for P23/P24 normalization and does not enlarge P22.

---

## 1. What F11 actually has to show

The selected F10 model reports geodesic/tidal evidence in a static weak-field clock sector with `g00=-(d0/d)^2` and `Phi=-(d-d0)/d0`. The weak-field sourced question is whether a licensed physical source and normalization yield the scalar Poisson relation; P22 does not assume that bare degree is that source.

## 2. The make-or-break question, and its honest resolution

**The trap (stated, not dodged):** if Φ depended on *bare local node-degree*, there would be **no gravity at a distance** — a node far from a mass has its own local degree, unperturbed by the distant clump; bare degree does not propagate or fall off as 1/r. The construction would break.

**The selected construction:** the proposed gravitational field is not bare degree. F9's conserved-flow standing supplies a global candidate object, and this source models a localized graph source as perturbing that flow. The long-range potential is then represented by the graph-Laplacian Green function. P22 retains as Open the native map from physical mass to this graph source.

Within the selected construction, F9 and the F11 model use one conserved-flow object. This is conditional internal consistency, not a source-map derivation.

## 3. The separately reported harmonic-exterior result

**[reported check; script absent] (`f11_harmonic.py`)** On a `41^3` lattice, this source reports that a localized graph/profile perturbation fits `delta d=A/r+C_d` with `R²=0.997`, compared with `0.938` for a `1/r²` control. This is a distinct documentary report of unknown relationship to `gravity-asymmetry.md`'s underspecified `R²=0.9993` report. Conditional on the stated continuum realization, the standard three-dimensional Green function has a harmonic `1/r` exterior.

**Conditional consequence — Poisson form:** distinguish the positive graph/profile perturbation from the selected inverse-clock potential:

```text
delta d(r) = A/r + C_d,
Phi(r) = -delta d(r)/d_0 = -A/(d_0 r) + C_Phi,
nabla^2 Phi = +(4 pi A/d_0) delta^3(r).
```

Thus `Phi` is harmonic away from the source. If `rho=M delta^3(r)` and `G M:=A/d_0` are conditionally defined, the same sign-consistent equation is `nabla^2 Phi=4 pi G rho`.

Thus the conditional continuum Green-function construction supplies the **Poisson form** `nabla^2 Phi=4 pi G rho` after a scalar source and conversion are defined. The harmonic `1/r` exterior is conditional analytic mathematics; the absent-script value is documentary evidence only. The physical mass/source map and `G` are not derived by defining `G M:=A/d_0`.

## 4. Retained P24 proposal — full tensor forcing argument

The full (not just weak-field) claim is `G_mu nu + Lambda g_mu nu = kappa T_mu nu`. That P24 proposal invokes Lovelock-style rigidity under additional premises. It is not a P23 result, and the absent `f11_assemble.py` script was not rerun.

| Premise | Status |
|---|---|
| (1) source is a symmetric rank-2 tensor `T_mu nu` | **P23-bounded.** The weighted second moment is symmetric and admits the observer-relative three-sector split under P23's stated inputs; native weights/vectors and general dynamics remain open. |
| (2) locality | **Shown only for the displayed nearest-neighbor graph rule.** This does not prove exact continuum derivative order, naturality, or a full tensor equation. |
| (3) second-order in the metric | **Conjectured/Unregistered under P24.** One-step locality admits higher-derivative finite-spacing corrections; a scaling/order theorem is absent. |
| (4) `nabla_mu T^{mu nu}=0` | **P23-conditional.** Scalar continuity or generic conservation language alone is insufficient; complete local balance equations and carrier calculus are required. |

**P24 boundary:** the corpus accepts a general Lovelock-style theorem family as external mathematics and retains `H=aG+bg` as the selected target route. It has not adopted one exact claim-specific schema or complete closed hypothesis list, so applicability to a framework tensor remains Conjectured/Open and Unregistered. `H=cT`, `a!=0`, P23 source conservation, and coupling calibration are separate model/source premises, not hypotheses supplied by the import.

Claims about `c`, `kappa=8 pi G`, Lambda, and the full field equation remain with their numbered later owners. They are not consequences of P23 source kinematics.

## 5. Honest status of F11

**Retained report and separately Registered conditional mathematics under P22:**
- This source separately reports a `41^3` graph-source fit (`R²=0.997`, control `0.938`); its relation to the underspecified `0.9993` report is unknown. The report is documentary evidence only. Conditional analytic `1/r` mathematics supplies the harmonic exterior and scalar Poisson form once the source map and normalization are supplied. P22 keeps the physical mass-source identification and source normalization Open.

**P23 source standing:** symmetric second-moment algebra and the observer-relative energy/flux/spatial-stress split are Secured conditionally; sector vocabulary is Registered for an independently licensed physical source; the further three-office correspondence is selected/Conjectured and Unregistered as an exact theorem. One selected two-stream example populates all three tensor sectors. Native source weights/vectors, general stress population, coefficient meaning, and covariant conservation remain live P23 frontiers.

**P24 standing:** the named rigidity family is accepted externally at general conditional scope; the exact P24 schema and claim-specific applicability remain Conjectured/Open and Unregistered. The normalized Einstein-plus-metric form is a selected/Conjectured conditional model and Unregistered as a native field equation. P22 retains graph/scalar normalization and physical `G`; P23 retains tensor-source semantics/evolution/conservation; P24 retains `kappa:=c/a` inside the selected model, the nonzero source coupling, `kappa=8 pi G`, calibration, and nonlinear expenditure.

## 5b. Retained P23 source proposal, corrected through canonical authority

The retained source proposed a weighted second moment of oriented conditioning vectors. P23 preserves the exact algebra while correcting its scope and evidence standing.

**The proposed construction.** Given a licensed tangent carrier, admitted oriented vectors `V_a^mu`, and real source weights `w_a`, define

> `T^{mu nu}(x) = Sum_a w_a V_a^mu V_a^nu`.

This tensor is symmetric by exact outer-product algebra. A general multi-stream sum is **not** equal to one rank-one `rho V^mu V^nu` tensor unless the second moment is rank one or additional closure conditions hold. The retained word `amplitude` does not supply a real stress-energy weight; that map remains open.

- **Symmetry:** theorem-Secured given the displayed inputs.
- **Components:** relative to a selected observer, every symmetric source decomposes into energy scalar, spatial flux, and spatial stress. P23 Registers those sector names for an independently licensed physical source, but keeps the further This/From/With correspondence selected/Conjectured and Unregistered as an exact office theorem.
- **Population:** an exact selected two-stream example gives nonzero observer-scalar, mixed-vector, and spatial-tensor sectors; physical source naming and generic network dynamics remain unproved.
- **Conservation:** `partial_mu T^{mu nu}` contains both continuity and vector-transport terms. Scalar continuity alone is insufficient when `V_a` varies. Complete local balance equations are required.

The absent `t_structure.py`, `t_full.py`, and `t_converge.py` scripts and their convergence figures are documentary source claims only. They were not rerun and do not Secure a continuum conservation law.

**What this fixes, and what it does not.** P23 supplies a bounded source-tensor construction and conditional decomposition registration, not a native physical stress-energy identification or full source dynamics. It does not close P22's scalar source normalization, derive `G`, provide every P24 premise, or adjudicate P28 Lambda claims.

## 6. The gravity program, end to end

- **F1–F2:** the conditioning-network N; the anti-smuggle admissibility rule; step atomicity. **Done.**
- **F4–F7:** the flat tier — `c = 1` and the direct-bound null relation are native; the Lorentzian metric and `Aut(N) = SO^+(1,3)` are **Secured conditionally and Registered–Sealed on the stated direction carrier/manifold**. P7/G1 carrier recovery remains incompletely sealed.
- **F8:** the coherence-participation functional, forced via Gleason (dim ≥ 3). **Done.**
- **F9:** the standing vector σ_i = √(d_i)/Z; the tilt exactly linear in conditioning-degree. **Done.**
- **F10:** selected inverse-clock curvature model with retained geodesic/tidal reports. **Registered at bounded static `2+1` model scope**; source/clock uniqueness and common `3+1` implementation Open under P22.
- **F11:** P22 conditionally Registers the harmonic exterior and scalar Poisson form while retaining graph/scalar normalization and `G`. P23 governs bounded source/decomposition mathematics and open tensor-source dynamics. P24 accepts the general theorem-family import but leaves exact schema/applicability and the selected full equation Conjectured/Open and Unregistered. Lambda is governed separately by P28.

**Bounded arc:** the retained sources connect a conditional local participation tilt to a selected static clock metric, reported geodesic/tidal checks, and a separate harmonic three-dimensional exterior. P22 records the exact open edges; P23/P24 govern the tensor and full-GR continuation.

---

### Appendix: named scripts absent from the repository; retained output claims above
- `f11_poisson.py` — the weak-field reduction; the harmonic-exterior condition identified; symbolic ∇²(1/r)=0.
- `f11_harmonic.py` — absent script named for the separately described `41^3` graph-source report: `1/r` fit `R²=0.997` versus `1/r²` control `0.938`; unknown relation to the `0.9993` report.
- `f11_assemble.py` — weak-field closure + the Lovelock forcing argument with the four premises checked and gaps stated.
- `t_structure.py`, `t_full.py`, `t_converge.py` — absent scripts named for the retained P23 symmetry/component/conservation reports; outputs and convergence values are documentary only.
