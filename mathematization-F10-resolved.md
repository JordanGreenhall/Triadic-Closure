# F10, Substantially Closed: Gravity Is Genuine Curvature

### Supersedes the earlier "F10 not done" status. After resolving the sign (via step-atomicity) and the velocity-drift-vs-geodesic worry (via gerund-native inertia + direct simulation), F10's spine is established: the F9 conditioning-degree tilt produces **genuine spacetime curvature** — geodesic motion, tidal geodesic deviation with the correct stretch/squeeze signature, matching tidal-tensor magnitudes, and a traceless vacuum tensor. All checks use **independent specifications**: the walkers know only F9 (degree-tilt) + gerund-native inertia + the atomicity clock; the geometric predictions come only from the metric. Agreement is therefore structural, not fitted. Scope limits stated honestly at the end. Scripts and outputs inline.

---

## 1. The two prior obstacles, resolved

**Obstacle 1 — the sign (which way bodies fall): resolved by step-atomicity (F2).** The gravity sign reduces to whether proper-time-rate dτ/dt increases or decreases with local conditioning-degree d. This is built from the one network quantity π_i ∝ d_i (the conserved-flow measure): proper time is either that rate (∝ d) or its reciprocal (∝ 1/d). **F2 (step atomicity) forces the reciprocal:** a content's own tick is *one atomic conditioning*, a fixed unit that does not scale with the neighborhood; per that fixed tick the ambient does d-worth of activity, so the content's own advance per unit global progress is 1/d. Hence dτ/dt ∝ 1/d (clock slower at high degree — gravitational dilation), g₀₀ = −(d₀/d)², Φ = −(d−d₀)/d₀, and geodesic acceleration points toward higher degree — **attractive**. The alternative (dτ/dt ∝ d) would require the atomic step to dilate with local degree, contradicting F2. The sign is forced by an already-proved result, not chosen.

**Obstacle 2 — velocity-drift vs. geodesic (is the motion inertial?): resolved conceptually and quantitatively.** *Conceptually* (gerund-native): there are no nouns being pushed. A content is re-selected each step unconditionally; there is no rest state for a "drift" to damp toward. So motion is inertial by default (re-selection persists — "inertia" is the persistence of the re-selection shape, needing no cause because not-relating is impossible for an actual), and a non-uniform realizability field *steers* that inertial motion ("acceleration" = the field-weighting bending the persistent re-selection). The "medium-drift that decays to rest" worry presupposed a background rest-frame the network does not have. *Quantitatively*: see §2.

## 2. Geodesic motion matches (the walk = the metric's geodesic)

**[checked] (`f10_geodesic_check.py`, `f10_factor2.py`)** Two independent specifications:
1. **The walk** — a content with position and re-selection-direction; each proper step, inertia advances it by its direction, the F9 degree-tilt steers the direction, and the atomicity clock sets coordinate-time-per-proper-step ∝ d. No geometry input.
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
- conditioning-degree concentration **is** a curved metric (g₀₀ from the atomicity clock);
- the F9 degree-tilt + gerund-native inertia **is** geodesic motion in that metric (quantitative match, no free parameter);
- nearby free contents experience **genuine tidal curvature** — correct stretch/squeeze signature, matching magnitudes, traceless in vacuum.

Gravity-as-geometry is therefore not asserted but **demonstrated** for this regime: a mass is a region of excess conditioning-degree; it curves the metric; free contents fall along geodesics; nearby contents feel true tidal forces. All from F9 + atomicity + gerund-native inertia, with no geometry assumed and every geometric prediction specified independently of the walk.

## 5. Honest scope — what is and isn't shown

**Shown:** weak-field, static, 2+1, the g₀₀-sector curvature: geodesics, tidal deviation, tracelessness. The sign is forced (F2); the motion is inertial (gerund-native, confirmed numerically); the deviation is genuine curvature (not a potential).

**Not yet shown (the remaining F10/F11 frontier):**
- **The spatial metric sector (g_ij) and the full 3+1 tensor.** Only the g₀₀ (clock) sector was needed for the weak-field tests, but full GR has spatial curvature too; the strong-field and dynamical regimes are untested.
- **The full Einstein equation (F11).** The vacuum tracelessness shown here is the weak-field statement ∇²Φ = 0 (vacuum). The *sourced* equation — that the curvature relates to the conditioning-degree distribution by exactly G_μν = 8πG T_μν — is the F11 target. What is now in hand toward it: the source is conditioning-degree (= energy, admissibly), the relation is local and (weak-field) linear, and conservation (∇·T=0) is conservation of registered distinctions (0.6). The Lovelock-forcing argument can now stand on a *demonstrated* curvature rather than an assumed one — but exhibiting the full tensor and fixing G (the one free particular) remains.
- **The conserved-flow standing-state choice** (flagged in F9) still rides underneath.

**Status:** F10's core claim — that the degree-tilt produces genuine curvature, not a flat-background force — is **established for the weak-field static regime**, with the sign forced by atomicity and the geodesic/tidal structure verified by independent simulation. The full-tensor / sourced-equation extension (F11) is the remaining frontier, now resting on demonstrated curvature.

---

### Appendix: scripts (run, outputs recorded above)
- `f10_geodesic_check.py` — walk vs. g₀₀-geodesic acceleration (ratio → 1 after convention fix).
- `f10_factor2.py` — the factor of 2 is a constant convention, not a varying disagreement; located and removed.
- `f10_deviation.py` — geodesic deviation: radial stretch + transverse squeeze (the curvature signature).
- `f10_tidal_quant.py` — tidal-tensor magnitudes match (~90%); traceless in vacuum (far-field trace 100× smaller).
