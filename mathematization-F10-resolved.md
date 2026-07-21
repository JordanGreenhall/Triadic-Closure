> **P22 supporting source.** [P22 Weak-Field Gravity as Participation Curvature](p22-weak-field-gravity-as-participation-curvature.md) governs current claims and grades. The checks below are retained reports: their named scripts are absent and were not rerun. The selected static `2+1` inverse-clock model supports bounded curvature Registration; source/clock uniqueness, a common `3+1` implementation, the spatial metric sector, source normalization, and `G` remain open.

# F10, Bounded Model Report: Gravity as Curvature

### Supersedes the earlier conclusion that no bounded F10 model exists. In the selected inverse-clock model, the reported independent walk and metric specifications agree at static weak-field scope and exhibit the expected geodesic/tidal signatures. This does not prove that atomicity uniquely forces the inverse clock, and the absent scripts prevent fresh reproduction from this repository.

---

## 1. The two prior obstacles, resolved

**Obstacle 1 — the sign (which way bodies fall): selected-model resolution, uniqueness still open.** The gravity sign reduces to whether proper-time rate `d tau/dt` increases or decreases with local conditioning degree `d`. The displayed model reads F2 atomicity as licensing a content's fixed own-step against `d`-scaled ambient activity and therefore selects the reciprocal `d tau/dt proportional to 1/d`. That gives a slower clock at high degree, `g00=-(d0/d)^2`, `Phi=-(d-d0)/d0`, and attraction toward increasing degree. P22 retains the ambient-flow clock as an admissible countermodel not yet excluded by a native uniqueness proof; atomicity distinguishes own advance from ambient activity but does not yet force this exact inverse relation over all clock maps.

**Obstacle 2 — velocity-drift vs. geodesic (is the motion inertial?): resolved conceptually and quantitatively.** *Conceptually* (gerund-native): there are no nouns being pushed. A content is re-selected each step unconditionally; there is no rest state for a "drift" to damp toward. So motion is inertial by default (re-selection persists — "inertia" is the persistence of the re-selection shape, needing no cause because not-relating is impossible for an actual), and a non-uniform realizability field *steers* that inertial motion ("acceleration" = the field-weighting bending the persistent re-selection). The "medium-drift that decays to rest" worry presupposed a background rest-frame the network does not have. *Quantitatively*: see §2.

## 2. Geodesic motion matches (the walk = the metric's geodesic)

**[reported check; scripts absent] (`f10_geodesic_check.py`, `f10_factor2.py`)** Two independent specifications:
1. **The walk** — a content with position and re-selection-direction; each proper step, inertia advances it by its direction, the F9 degree-tilt steers the direction, and the atomicity clock sets coordinate-time-per-proper-step ∝ d. No geometry input.
2. **The geodesic** — of the metric g₀₀ = −(d₀/d)², acceleration −½ ∂ₓ(d₀/d)² = d₀²·d′/d³. No walk input.

They agree: near-static acceleration ratio walk/geodesic = **1.01** (after fixing a redundant ½ in the discrete bias normalization), **constant across all parameters** (mass position, amplitude, width, baseline degree — verified 0.500 ± noise before the convention fix, i.e. a pure convention factor, not a varying disagreement). The F9-steered inertial re-selection *is* geodesic motion in the degree-determined metric.

## 3. Genuine curvature — tidal geodesic deviation (the decisive test)

A potential is not curvature; **curvature is geodesic deviation** (tidal forces between nearby free worldlines), trivial in 1+1, so tested in 2+1.

**[reported check; script absent] (`f10_deviation.py`)** Two free walkers released near a degree bump (a modeled source), falling in:
- **radial separation** (along infall): **grows** 6.0 → 16.1 — tidal **stretch**;
- **transverse separation** (perpendicular): **shrinks** 6.0 → 4.8 — tidal **squeeze**.

Opposite signs. A uniform force moves both walkers identically (separation constant); only genuine **tidal curvature** stretches radially while squeezing transversely. This is the unmistakable fingerprint of curvature (the same effect as tidal stretching and ocean tides).

**[reported check; script absent] (`f10_tidal_quant.py`)** The source reports matching tidal-component magnitudes and a suppressed vacuum trace:
- measured vs. predicted tidal components T_xx (ratio 0.90), T_yy (ratio 0.95) — agreement to ~10%, the residual consistent with discretization of second derivatives of a Gaussian on a grid (both components off similarly — a discretization scale, not a structural gap);
- **tracelessness:** far from the source the tidal trace is ~10⁻⁷ versus in-field components ~10⁻⁵ — two orders smaller. The vacuum tidal tensor is traceless (∇²Φ → 0 off-source): radial stretch exactly balances transverse squeeze. This is the genuine curvature/vacuum condition.

## 4. What F10 now establishes

In the reported weak-field, static, `2+1` model:
- a localized conditioning profile is represented through the selected clock metric `g00`;
- the selected F9 degree-tilt + gerund-native inertia agrees with geodesic motion in the reported finite check, after its stated convention correction;
- nearby free contents experience **genuine tidal curvature** — correct stretch/squeeze signature, matching magnitudes, traceless in vacuum.

Within the selected model, gravity-as-geometry is supported for this regime: a localized conditioning-profile source changes the clock metric, and the reported free paths and relative deviations agree with the independently specified metric behavior. P22 does not treat the mass-to-source map or inverse clock as uniquely forced.

## 5. Honest scope — what is and isn't shown

**Reported within the selected model:** weak-field, static, `2+1`, `g00`-sector geodesics, tidal deviation, and vacuum-trace suppression. The attractive sign follows from the selected inverse clock; P22 retains as open the proof that this exact map is uniquely forced.

**Not yet shown (the remaining F10/F11 frontier):**
- **The spatial metric sector (g_ij) and the full 3+1 tensor.** Only the g₀₀ (clock) sector was needed for the weak-field tests, but full GR has spatial curvature too; the strong-field and dynamical regimes are untested.
- **The full Einstein equation (F11/P24).** The reported vacuum-trace suppression is consistent with the weak-field statement `nabla^2 Phi=0` away from a source. It does not construct a physical scalar source or `T_{mu nu}`. P23 owns source construction; P24 owns the Lovelock/full-Einstein route, spatial metric, and nonlinear completion.
- **The conserved-flow standing-state choice** (flagged in F9) still rides underneath.

**Status:** the selected degree-tilt/clock model is **Registered at bounded static weak-field scope** as a curvature rather than uniform-drift construction. The reported simulation is supporting evidence, not a rerun proof. P22's three local frontiers and P23/P24 retain the remaining bridges.

---

### Appendix: named scripts absent from the repository; retained output claims above
- `f10_geodesic_check.py` — walk vs. g₀₀-geodesic acceleration (ratio → 1 after convention fix).
- `f10_factor2.py` — the factor of 2 is a constant convention, not a varying disagreement; located and removed.
- `f10_deviation.py` — geodesic deviation: radial stretch + transverse squeeze (the curvature signature).
- `f10_tidal_quant.py` — tidal-tensor magnitudes match (~90%); traceless in vacuum (far-field trace 100× smaller).
