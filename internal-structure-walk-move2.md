# Internal-Structure Walk — Move 2: The Gauge Group, and Quarks

### Walks the four D1 images for gauge no-distinction directions, reaches a verdict on the Standard Model gauge group, and derives quarks/confinement from the color floor. Computations in `move2.py`, `move2b.py`, `move2c.py`. Tags: [derived], [established-prior], [cross-check], [open], [not-derived].

## 1. The gauge directions among the four D1 images

A gauge symmetry = a continuous **no-distinction direction**. Test each of the four images:

| D1 image | same-kind multiplicity | gauge direction |
|---|---|---|
| This-flattened (color) | 3 (interior office triad, same-kind) | **SU(3)** [established, cond. on (A)] |
| From-flattened (ordering) | 1 (oriented line; phase preserving orientation) | **U(1)** [derived here] |
| With-flattened (extent) | — | spent on **space** (interchangeable degrees), not internal |
| marked triad (J) | — (offices distinct in kind) | **none** (mixing offices inadmissible) |

[derived] The From-flattened image carries a **U(1)**: the orientation is a 1-dim oriented structure, and the phase preserving its arrow (e^{iα}) is a continuous no-distinction direction. The marked triad carries **no** gauge direction — the three offices are kind-distinct (From/With/This do not interconvert), so a continuous mixing is inadmissible, the same fact that forbids rotating the offices.

## 2. The SU(2) verdict (`move2b.py`)

The same-kind multiplicities in the images are **3** (interior triad → SU(3)) and **1** (orientation → U(1)). **There is no same-kind 2** — the interior triad is rigidly three (floor and ceiling), the modes are kind-distinct (Move 1), so SU(2) has **no fundamental source** among the images.

[cross-check] This matches physics precisely. The **unbroken, exact** gauge groups in nature are exactly **SU(3)_color and U(1)_EM** — the two the framework produces. **SU(2)_weak is broken and chiral** — the profile of a non-fundamental (emergent/selected) symmetry, not a vacuum no-distinction direction. So the framework forces the unbroken sector and withholds the broken one: it gives precisely SU(3)×U(1) and predicts SU(2)_weak is *not* fundamental. This is a prediction with a right/wrong answer, not a fit — the framework's silence on SU(2) lands exactly where nature's symmetry-breaking is.

[open] The hypercharge/weak-mixing structure (U(1)_Y vs U(1)_EM, the broken sector) is not claimed; the framework's U(1) maps to the unbroken electromagnetic U(1). Whether the broken sector is a located selection (like (A)) or genuinely absent is open.

## 3. Quarks and confinement from the color floor (`move2c.py`)

The established color structure: three interior moments sharing an invariant (SU(3) triple); a closed neutral unit = the complete triad saturated; the floor = no single interior moment stands as a closure alone. Reading hadron structure off this, via triality (the 3 has triality +1, the 3̄ has −1; a color-neutral closure needs total triality 0 mod 3):

- single quark (3): triality 1 ≠ 0 → **cannot stand alone (confined)** [derived]
- three quarks (baryon): triality 3 ≡ 0 → **closes** (the complete triad) [derived]
- quark+antiquark (meson): triality 0 → **closes** (moment + antimoment) [derived]
- two quarks: triality 2 ≠ 0 → does not close [derived]

So the interior-triad floor forces: matter color-carriers come as a triple (**quarks**); single quarks are **confined** (triality-nonzero is not a closure); bound closures are exactly the color-neutral combinations (**baryons** = full triad, **mesons** = moment+antimoment). This is the observed hadron spectrum, from the SU(3) triple + closure-floor, no QCD dynamics imported.

[not-derived] The confinement **mechanism** (linear potential, flux tubes) — dynamics. Only the **kinematic** fact (non-neutral is not a standing closure) is forced here.

## 4. Result

The framework forces the internal gauge structure **SU(3) × U(1)** (color, conditional on (A); the orientation-phase U(1)), produces **quarks** as the color triple and **confinement** (kinematic) and the **baryon/meson** neutral closures from the color floor, and **withholds SU(2)_weak as fundamental** — matching that the exact unbroken groups are SU(3)_color and U(1)_EM while SU(2) is broken and chiral. Open: the broken electroweak sector (selected or absent — not fabricated); the confinement dynamics; the matter generations and mass spectrum.
