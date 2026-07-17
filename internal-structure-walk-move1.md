# The Internal-Structure Walk — Move 1: Locating the Gauge Source (and a Correction)

### Opening move of the internal-structure walk, the gate in front of the specific gauge forces, quarks, and atoms. Move 1 (dependency position) asks what the internal-structure stage should be looking for and from where. The result is partly a **correction** of a prior lead: of the two candidate non-interchangeable "threes" in the standing, only one (color, the This-flattened interior) is a genuine gauge source; the other (the mode-pairing bb/ff/bf) was mis-identified and is **not** a gauge factor. A force-fit toward the electroweak group SU(2)×U(1) from the mode-pairings was attempted, caught as a canary, and rejected. Computations inline. Tags: **[established-prior]**, **[derived-here]**, **[corrected]**, **[open]**, **[canary-rejected]**.

---

## 0. What stands coming in

- **[established-prior]** SU(3) for same-kind mediation, **conditional** on one isolated selection (A) (the antisymmetric-sector choice). The carrier M ≅ ℂ³ is recognized as color. (`d3-su3-conditional-theorem.md`.) The conditionality is hermetic and the selection located at one biconditional.
- **[established-prior]** Color = the **This-flattening**: the interior triadic distinction of a closure read across the recursion under the quality (non-interchangeable) basis. The three interior "colors" **share an invariant** (same kind, differ only in interior slot) — not a kind-distinction. (`physics-walk-D1-D5-consolidated.md`.)
- **[established-prior, but flagged provisional]** A D2/D4 lead: conditional on the sector-pure physical occupants not supplied by [P3](boson-fermion-and-holding-statistics.md), the two registered exchange modes (boson = symmetric, fermion = antisymmetric) give three proposed non-interchangeable pairings **bb, ff, bf**, floated as a candidate source of internal/charge degrees. Never sealed; explicitly "provisional, the live work to firm up."

So there are **two candidate non-interchangeable "threes"**: (C) the color interior-triad, and (M) the mode-pairing three. Move 1 must resolve their relationship before any gauge group is attempted.

## 1. (C) and (M) are different in kind (`internal_structure.py`)

- **(C) color** is a **1→3** structure: *one* closure, *three* interior moments (the office-triad read inside, flattened under quality). Non-interchangeable because quality is preserved.
- **(M) mode-pairing** is a **2→3** structure: *two* modes, *three* symmetric pairings (multiset coefficient C(2+1,2) = 3). Its natural structure under mode-swap b↔f is **2+1**: a doublet {bb, ff} (the like-mode pairs swap) + a singlet {bf} (the cross pair is fixed).

These are not the same three. (C) is a clean interior triple; (M) is a 2+1 combinatorial split. So the internal structure is not a single object seen twice.

## 2. The canary: force-fitting SU(2)×U(1) from (M) — attempted and rejected

The 2+1 structure of (M) under mode-swap (doublet + singlet) pattern-matches the electroweak group's representation content (SU(2) doublets + U(1) singlet). The attempt was written down: "(M) → doublet+singlet → weak/hypercharge?" **This is a canary** — reading the Standard Model's known structure back into a combinatorial coincidence. It was caught and is rejected by the gauge-symmetry test (§3). Recording it explicitly because the temptation is exactly the failure mode the discipline guards against: a suggestive numerical match (2+1 ↔ doublet+singlet) is not a derivation, and the rest of the walk must not lean on it.

## 3. The gauge-symmetry test: only (C) is a gauge source (`mode_pairing_test.py`)

A **gauge symmetry** requires a **direction of no distinction** — a continuous transformation among states registering no physical difference. Test each candidate:

- **(M) mode-pairing — NOT a gauge source.** Conditional on P3-admitted occupants, the mode distinction is **J-marked: distinct in exchange character** — symmetric holding permits complete-state co-occupation while antisymmetric holding excludes it. A transformation mixing sector-pure modes changes that exchange character, so it is **not** a no-distinction direction. The "doublet {bb, ff}" is not thereby a gauge doublet. **(M) is a classification by P3's scoped Registered–Sealed mode distinction, not an internal gauge charge.** [corrected]
- **(C) color — a genuine gauge source.** The three interior moments **share an invariant** (same kind, differ only in interior slot — established prior). That *is* a direction of no distinction: the three are indistinguishable in kind, so a continuous transformation among them registers no physical difference. This is exactly why (C) supports the continuous group SU(3) and (M) does not. [established-prior, re-grounded here]

**The correction.** The prior "mode-pairing → internal charge" lead confused a **kind-mark** (J-level, kind-distinct) with a **gauge direction** (no-distinction). They are opposite: a kind-mark is a registered distinction (it cannot be a no-distinction symmetry), while a gauge charge is a no-distinction direction. The mode-pairing, being built from the kind-mark, cannot be a gauge source. **Internal gauge structure, as established, is the This-flattened interior (color) alone.**

## 4. Move-1 result, stated honestly

- **[derived-here]** Of the two candidate internal "threes," only **(C) color** (the This-flattened interior, same-kind interior moments) is a genuine gauge source — because only it is a direction of no distinction. It gives the SU(3)-type structure (conditional on (A), per the prior theorem).
- **[corrected]** The **(M) mode-pairing** is **not** an internal gauge factor. Conditional on admitted sector-pure occupants, it spends P3's scoped Registered–Sealed boson/fermion exchange-mode distinction, not a no-distinction direction. The prior lead is corrected.
- **[canary-rejected]** The force-fit SU(2)×U(1) ← mode-pairing-2+1 is rejected as reading the Standard Model back into a combinatorial coincidence.
- **[open]** Where the **electroweak structure** (the SM's SU(2)×U(1)) would come from — *if the framework produces it at all* — is **genuinely open**. The natural second source (mode-pairings) is closed off. So either there is a *different*, not-yet-identified internal-structure source for it, or the framework does not force it. **This must not be fabricated.** Honest options to investigate next, none assumed:
  1. The **From-flattening** (ordering/oriented internal distinction) and the **marked-triad** images may carry internal structure not yet walked — only the This-flattening (color) has been worked. The four-images-at-D1 result gives From-flattened (asymmetric/ordering) and the marked triad as distinct images; whether either sources an internal symmetry is unexamined.
  2. The electroweak group may be a **deployment/selection** (like (A) for SU(3)), not forced — in which case the honest result is "selected, not forced," located precisely.
  3. The framework may genuinely **not** produce SU(2)×U(1) as fundamental — a possible negative result, which would be a real (if uncomfortable) finding, not a failure to be papered over.

## 5. The shape of the walk, revised

Coming in, the implicit expectation was that the framework's two non-interchangeable threes would deliver the Standard Model's SU(3) and electroweak factors. **Move 1 revises this:** the framework delivers **SU(3) from color** (conditional on (A)), and the second candidate three is **not** a gauge source. The internal gauge structure that is actually established is SU(3)-type color, and nothing more is forced by the mode structure. The other SM factors, if present, need a source not yet identified — and the walk's integrity depends on finding it (or its absence) honestly rather than fabricating it from a combinatorial near-match.

**Next (Move 2):** examine whether the **other D1 images** (From-flattened ordering, the marked triad) carry internal no-distinction directions — the only principled place a further internal gauge source could come from, since the This-flattening (color) and the mode-pairing (not-a-gauge-source) are now both accounted for. If they do not, the honest result is that the framework forces color (SU(3)) and leaves the electroweak sector as either selected or underived — located precisely, not hidden.

---

### Appendix: scripts (run, outputs recorded above)
- `internal_structure.py` — (C) vs (M): different in kind (1→3 interior triple vs 2→3 mode-pairing 2+1).
- `mode_pairing_test.py` — the gauge-symmetry test: (M) is kind-marked (not a no-distinction direction, not gauge); (C) is same-kind (a no-distinction direction, gauge). The mode-pairing lead corrected.
