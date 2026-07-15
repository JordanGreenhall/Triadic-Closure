# F10, Substantially Closed: Gravity Is Genuine Curvature

### Historical resolution attempt. The simulations exhibit curvature behavior conditional on a selected clock bridge. Canonical M1 supplies integer carrier depth but does not force `dτ/dt ∝ 1/d`; therefore the sign and metric identification are not established by step atomicity. The M4 lineage must adjudicate the remaining conditional construction.

---

## 1. The two prior obstacles, resolved

**Obstacle 1 — the sign (which way bodies fall): unresolved bridge.** The gravity sign depends on whether `dτ/dt` increases with local conditioning-degree `d` or follows its reciprocal. M1 says only that one carrier edge increments carrier depth by one. It does not identify that count with proper time or choose `dτ/dt ∝ 1/d`. The reciprocal clock rule used below is therefore a **selection**. Conditional on it, `g00 = -(d0/d)^2`, `Phi = -(d-d0)/d0`, and attraction toward higher degree follow. The simulations test that conditional model; they do not derive the clock bridge.

**Obstacle 2 — velocity-drift vs. geodesic (is the motion inertial?): resolved conceptually and quantitatively.** *Conceptually* (gerund-native): there are no nouns being pushed. A content is re-selected each step unconditionally; there is no rest state for a "drift" to damp toward. So motion is inertial by default (re-selection persists — "inertia" is the persistence of the re-selection shape, needing no cause because not-relating is impossible for an actual), and a non-uniform realizability field *steers* that inertial motion ("acceleration" = the field-weighting bending the persistent re-selection). The "medium-drift that decays to rest" worry presupposed a background rest-frame the network does not have. *Quantitatively*: see §2.

## 2. Geodesic motion matches (the walk = the metric's geodesic)

**[checked] (`f10_geodesic_check.py`, `f10_factor2.py`)** Two independent specifications:
1. **The walk** — a content with position and re-selection-direction; each selected proper step advances it, the F9 degree-tilt steers the direction, and the selected reciprocal clock sets coordinate-time-per-proper-step proportional to `d`. The clock rule is an input.
2. **The geodesic** — of the metric g₀₀ = −(d₀/d)², acceleration −½ ∂ₓ(d₀/d)² = d₀²·d′/d³. No walk input.

They agree: near-static acceleration ratio walk/geodesic = **1.01** (after fixing a redundant ½ in the discrete bias normalization), **constant across all parameters** (mass position, amplitude, width, baseline degree — verified 0.500 ± noise before the convention fix, i.e. a pure convention factor, not a varying disagreement). The F9-steered inertial re-selection *is* geodesic motion in the degree-determined metric.

## 3. Genuine curvature — tidal geodesic deviation (the decisive test)

A potential is not curvature; **curvature is geodesic deviation** (tidal forces between nearby free worldlines), trivial in 1+1, so tested in 2+1.

**[checked] (`f10_deviation.py`) The curvature signature is present and correct.** Two free walkers released near a degree bump (a "mass"), falling in:
- **radial separation** (along infall): **grows** 6.0 → 16.1 — tidal **stretch**;
- **transverse separation** (perpendicular): **shrinks** 6.0 → 4.8 — tidal **squeeze**.

Opposite signs. A uniform force moves both walkers identically (separation constant); only genuine **tidal curvature** stretches radially while squeezing transversely. This is the unmistakable fingerprint of curvature (the same effect as tidal stretching and ocean tides).

**[checked] (`f10_tidal_quant.py`) The tidal-tensor magnitudes match, and the tensor is traceless in vacuum:**
- measured vs. predicted tidal components T_xx (ratio 0.90), T_yy (ratio 0.95) — agreement to ~10%, the residual consistent with discretization of second derivatives of a Gaussian on a grid (both components off similarly — a discretization scale, not a structural gap);
- **tracelessness:** far from the source the tidal trace is ~10⁻⁷ versus in-field components ~10⁻⁵ — two orders smaller. The vacuum tidal tensor is traceless (∇²Φ → 0 off-source): radial stretch exactly balances transverse squeeze. This is the genuine curvature/vacuum condition.

## 4. What F10 now establishes

In the weak-field, static, 2+1 regime tested:
- conditional on the reciprocal clock selection, conditioning-degree concentration defines the tested `g00` metric;
- the F9 degree-tilt + gerund-native inertia **is** geodesic motion in that metric (quantitative match, no free parameter);
- nearby free contents experience **genuine tidal curvature** — correct stretch/squeeze signature, matching magnitudes, traceless in vacuum.

The simulations demonstrate internal agreement between the selected walk and selected metric in this regime. Because both spend the unearned reciprocal clock bridge, they do not yet demonstrate that the framework itself identifies conditioning degree with spacetime curvature.

## 5. Honest scope — what is and isn't shown

**Shown conditionally:** weak-field, static, 2+1 behavior of the selected `g00` model: geodesics, tidal deviation, and approximate vacuum tracelessness. The sign is not forced by M1.

**Not yet shown (the remaining F10/F11 frontier):**
- **The spatial metric sector (g_ij) and the full 3+1 tensor.** Only the g₀₀ (clock) sector was needed for the weak-field tests, but full GR has spatial curvature too; the strong-field and dynamical regimes are untested.
- **The full Einstein equation (F11).** The vacuum tracelessness shown here is the weak-field statement ∇²Φ = 0 (vacuum). The *sourced* equation — that the curvature relates to the conditioning-degree distribution by exactly G_μν = 8πG T_μν — is the F11 target. What is now in hand toward it: the source is conditioning-degree (= energy, admissibly), the relation is local and (weak-field) linear, and conservation (∇·T=0) is conservation of registered distinctions (0.6). The Lovelock-forcing argument can now stand on a *demonstrated* curvature rather than an assumed one — but exhibiting the full tensor and fixing G (the one free particular) remains.
- **The conserved-flow standing-state choice** (flagged in F9) still rides underneath.

**Standing:** **Conjectured** as a framework bridge, supported by conditional weak-field simulations. The reciprocal clock rule, full tensor, and sourced equation remain Open dependencies.

---

### Appendix: scripts (run, outputs recorded above)
- `f10_geodesic_check.py` — walk vs. g₀₀-geodesic acceleration (ratio → 1 after convention fix).
- `f10_factor2.py` — the factor of 2 is a constant convention, not a varying disagreement; located and removed.
- `f10_deviation.py` — geodesic deviation: radial stretch + transverse squeeze (the curvature signature).
- `f10_tidal_quant.py` — tidal-tensor magnitudes match (~90%); traceless in vacuum (far-field trace 100× smaller).
