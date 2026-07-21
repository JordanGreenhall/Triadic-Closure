> **Historical F3 terminology note:** this superseded status page uses `depth` for horizontal temporal/address progression. Read those occurrences as **succession count**. Current canon reserves depth for vertical coinductive office-decomposition.

> **P22 historical/adversarial source.** Status: **Superseded as current status; retained as adversarial evidence.** [P22 Weak-Field Gravity as Participation Curvature](p22-weak-field-gravity-as-participation-curvature.md) governs every current weak-field claim and grade. The drift and reciprocal-clock sign ambiguity below remain live failure tests. The named scripts are absent and their recorded outputs are not rerun evidence.

# F10, Honest Status: Not Derived — the Obstacle Located

### F10 asked whether F9's tilt law (P selects neighbor i with probability d_i/Σd_j, linear in conditioning-degree) accumulates in the continuum limit to *exactly metric curvature* (geodesic motion in a curved metric), as opposed to a drift/force on a flat background. After explicit computation, **F10 is not established.** This document records what was found — including a genuine obstacle and a sign-ambiguity that controls the entire result — rather than a fitted derivation. Scripts and outputs inline. The honest headline: the gravitational sign hinges on a definition of "proper time on the network" that the framework has not yet supplied, and the two natural definitions give *opposite* signs (attraction vs repulsion). Choosing the one that matches known gravity would be fitting, not deriving, so it is not done here.

---

## 1. What was computed (real, holds)

**[checked] (`f10_step1.py`) The naive continuum limit of the F9 hopping is a spatial drift ∝ ∇log d, with constant diffusion.** On a chain with degree field d(x), hopping to neighbor i with probability ∝ d_i gives mean displacement per step = a²·d'(x)/d(x) and mean-square displacement = a². So the leading effect is a drift velocity v ∝ ∇log d.

**[checked] (`f10_step2.py`) This is a velocity drift — a medium effect — not geodesic motion.** A biased random walk yields a drift *velocity* (v ∝ ∇log d); geodesic motion in a static metric yields an *acceleration* (a ∝ −∇Φ). These are physically different: a velocity-drift stops when the bias stops (like a particle in a viscous medium); geodesic motion is inertial (continues). **The naive F9 hopping, as a walk in background time, gives the medium-drift, which is the *wrong* structure for gravity.** This is the first genuine obstacle.

## 2. The attempted resolution, and where it breaks

**The right framework move** is to refuse background time: the step *is* the depth *is* (proper) time (the c = 1 identity, F4). A content is not hopping spatially as an external clock ticks; its depth-advance and spatial-move are one conditioning. So the degree field must modulate the *depth-advance itself* (proper time vs coordinate time = the metric's g₀₀), not just the spatial choice. If the degree field produces a position-dependent g₀₀, that *is* curvature, and the spatial drift becomes the geodesic (Newtonian-limit) motion in that metric — genuine curvature, not a separate force.

**Where it breaks: the sign-determining ambiguity.** Producing g₀₀ requires identifying a content's *proper time* with a specific quantity on the conditioning-network. Two natural candidates exist, and **they give opposite signs:**

- **[checked] (`f10_step4.py`) Ambient-flow clock.** The conserved coherence-flow's visit-rate at a node scales *with* degree (corr(visit-rate, degree) = 0.994; visit-rate/π = 1.0 ± 0.03, matching the stationary measure π_i ∝ d_i). If proper time = ambient conditioning-rate at the content's location, then the clock runs *faster* at high degree, g₀₀ is more negative there with the sign giving Φ = +c·d, and the geodesic acceleration is −c·∇d — **repulsion from high degree. Wrong (anti-gravity).**

- **[checked] (`f10_step5.py`) Own-outward-share clock.** If proper time = the share of local conditioning that advances the content's *own* worldline outward (the F9 partition: at a busy/high-degree node, more conditioning is ambient re-cohering, so a resident content's own outward fraction is smaller, ∝ 1/d), then the clock runs *slower* at high degree (dτ/dt ≈ 1 − (d−d₀)/d₀), Φ = −(d−d₀)/d₀, and the geodesic acceleration is +（1/d₀)∇d — **attraction toward high degree. Correct (gravity).**

The two candidate proper-times are reciprocal (ambient ∝ d, own-share ∝ 1/d) and give opposite gravitational signs. The correct, attractive result follows *only* from the own-outward-share definition.

## 3. Why this is not a derivation (the honest verdict)

I can tell a plausible framework story for *either* clock. The own-outward-share story (proper time = a content's own worldline progress, not the ambient busyness of its location) is arguably the more correct reading of "proper time" — proper time *should* be the content's own advance, not the activity passing through its position. But "arguably more correct" is not "derived," and I reached the attractive sign by selecting the definition that yields it. **Selecting the definition that matches known gravity is fitting, not deriving.** Presenting clean attractive GR on that basis would be the canary — a fluent, satisfying result that smuggles the sign-determining choice. So F10 is recorded as not done.

## 4. What F10 actually leaves — the sharp owed result

The obstacle is now precisely located, which is the genuine product of this attempt:

**Owed (F10-core): derive, from the framework, what a content's proper time is as a quantity on the conditioning-network.** Specifically: is proper time (i) the ambient conditioning-rate at the content's location (∝ degree), or (ii) the content's own outward-worldline-progress share (∝ 1/degree)? This single question determines the sign of gravity:
- (i) ⇒ repulsion (wrong);
- (ii) ⇒ attraction, and — with the proper-depth framing — genuine geodesic motion in a curved g₀₀, i.e. curvature not drift (right).

If (ii) is *forced* by the framework (not merely available), then F10 likely goes through: the degree field gives g₀₀ ≈ −(1 + 2Φ) with Φ ∝ −(d−d₀), geodesics accelerate toward degree-concentration, the motion is inertial/universal (metric, not force), and the velocity-drift obstacle of §1 is dissolved (it was an artifact of background-time framing). But establishing (ii)-as-forced is the real content and is not done.

## 5. Status of the gravity program after the honest F10 attempt

- **F8** (the coherence-participation functional, forced via Gleason for dim ≥ 3): **done, holds.**
- **F9** (the standing vector σ_i = √(d_i)/Z; the tilt C(e_i) = d_i/Σd_j, exactly linear in conditioning-degree): **done, holds** (with the one flagged modeling choice — the conserved-flow standing-state).
- **F10** (the tilt accumulates to exactly metric curvature): **not done.** Two obstacles found: (a) the naive hopping gives a velocity-drift (medium), not geodesic motion — resolvable in principle by the proper-depth framing; (b) the gravitational sign depends on an underived definition of proper time, with the two natural definitions giving opposite signs. F10 reduces to deriving proper time on the network (F10-core), which is owed.
- **F11** (the Einstein form via Lovelock): **conditional on F10**, as before, and additionally on the sign being resolved attractive.

**Net:** the gravity program is real and computed through F9, and F10 is honestly open with the obstacle sharply identified (proper time on the network, sign-determining). This is a better place to be than a fitted F10 — the owed thing is now a single precise question — but it is not the completed curvature derivation, and is not claimed as one.

---

### Appendix: scripts (run, outputs recorded above)
- `f10_step1.py` — continuum limit of F9 hopping: drift ∝ ∇log d, constant diffusion.
- `f10_step2.py` — velocity-drift (medium) vs acceleration (geodesic): the first obstacle.
- `f10_step3.py` — proper-depth framing (posited g₀₀); flagged as possibly arranging the answer.
- `f10_step4.py` — ambient-flow clock ∝ degree ⇒ repulsion (wrong sign), computed.
- `f10_step5.py` — own-outward-share clock ∝ 1/degree ⇒ attraction (right sign); the sign-ambiguity made explicit.
