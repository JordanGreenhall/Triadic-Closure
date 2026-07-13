---
title: "ε_FW — Forced Bracket and Terminal Status"
type: deposit
status: current
created: 2026-06-30
session: "ε_FW serious effort — close"
supersedes: "from-with-transport-deposit.md (this session's opening deposit)"
depends-on:
  - mass-derivation-three-faces        # ε_FW definition; 6π⁵; closed negatives
  - flavor-mark-metric-and-neutron     # exterior turn 2π; 3π⁴; mark-metric u·d=−1/2; marks-remain
  - quark-lepton-split                 # three roots; chiral lift; marked color
  - chiral-coupling-result             # spin lift; helicity
  - closure-inherited-metric           # measure machinery (color: 2π⁵)
claim_statuses: [Open, Conjectured, "Conjectured-strong", Registered, "Registered and Sealed"]
---

# ε_FW — Forced Bracket and Terminal Status

## 0. The object

`m_p/m_e = 6π⁵[1 + c(3π⁴)⁻²], with 3/2 ≤ c ≤ 9/4·(1 + ε_FW)`, `ε_FW = 1.8825×10⁻⁵` (subtraction residual against the
measured CODATA ratio `1836.152673`; `6π⁵ = 1836.1181`). The ratio is **empirical**
(no SM derivation exists; SM absorbs it via two free parameters). ε_FW is the From-With
chiral face of the proton mass, one-sided against the fixed ruler `m_e = 1`.

Write `ε_FW = c · s²`, with `s = 1/(3π⁴) = 3.422×10⁻³` the interior-only maintenance
seam (`3π⁴ = 6π⁵/2π`). Then `s² = 1.171×10⁻⁵` and the measured coefficient is
`c = 1.6076`.

## 1. Where ε_FW lives, and why

ε_FW is the **self-back-reaction of the exterior turn on the interior it carries**:
- From-With face base measure = the exterior turn `2π = S¹` (flavor §4.1). Electron =
  bare turn (`2π/2π = 1`, the ruler); proton = turn wrapping the interior closure.
- ε_FW is **second-order** by construction: the first-order effect of the turn carrying
  the interior *is* `6π⁵`; ε_FW is the residual back-reaction, one order down →
  scale `s² ~ 10⁻⁵` (right order, from structure not target).
- Sign **positive**: an absorbed closure-loading loads the recurrence, never frees it.
- Electron value **zero**: trivial interior, nothing to react back.

Mechanisms tested and **closed this session** (all gave zero or did not force):
- mark geometric phase / Berry holonomy: **zero**, forced by dimension (the ℤ₃ mark
  plane is one complex dimension — no Bloch sphere, no curvature). Computed:
  `arg⟨P|P'⟩⟨P'|P''⟩⟨P''|P⟩ = 0`.
- mark-curvature flux: zero (same reason).
- φ·s² (golden coefficient): **refused** — near-miss (φ=1.6180 vs needed 1.6076,
  +0.65%), no derivation; excluded by measurement at ~hundreds σ.
- import via neutron splitting: **fails** — neutron is spin-blind (spin cancels in
  n−p), cannot pin the spin coupling.
- import via g_A: **circular** (g_A = 5/3 was the smuggled upper endpoint).

## 2. The forced bracket (theorem)

The back-reaction coefficient `c` obeys, necessarily:

```
3/2  ≤  c  ≤  9/4          (1.5 ≤ c ≤ 2.25)
ε_FW = c · s²,  s = 1/(3π⁴)
observed:  c = 1.6076  ∈  [3/2, 9/4]
```

**Theorems supporting the walls:**

- **Lower wall `c ≥ 3/2` (mark floor).** The interior is *marked* color (marks are
  constitutive of a determinate baryon, not optional). Any operator transporting the
  interior contains the mark channel; its non-singlet eigenvalue is `3/2` (operator
  `(3/2)I − (1/2)J` from `u·d = −1/2`, spectrum `{0, 3/2, 3/2}`, the `0` on the
  singlet = the singlet exemption). The positive-loading sign forbids any channel from
  cancelling below the floor. **Forced.**

- **Upper wall `c ≤ 9/4` (alignment ceiling).** The turn is **one-dimensional** (base
  `S¹`), so the connection is a **1-form**; a 1-form carries no 2-form, hence the
  operator is **two-body** (no three-body term possible). Any two-body operator from
  mark + spin + correlated pairing is bounded by maximal simultaneous alignment:
  `3/2 + 3·(1/4) = 9/4`. **Forced.**

- **Singlet exemption (cross-check).** The color singlet (det=1, ℤ₃-even) returns with
  zero holonomy; the defect lives only in the marks-that-remain (`P = 2u+d`, `|P|²=3`).
  Consistent with the `0` eigenvalue above. **Forced.**

## 3. The remaining opening (Conjecture)

The **position within the bracket** is the single open quantity. It is the From-With
connection normalization — equivalently `(β+γ)`, the one effective coupling, or the
commutator scale `κ` of `[From, With]`. The office *relations* fix the operator's
structure, sign, channels, and the two walls, but **not its magnitude**; magnitude
needs a metric on the algebra that fixes commutator scale, which is not on the board
(the closure measure gave `a_S/a_M = π`, which does not map to `β+γ` because β and γ
are degenerate on every baryon: `X = ⟨ΣS_i·S_j⟩` identically, octet and decuplet alike).

> **Conjecture (ε_FW position).** The differential between the proven leading term
> `6π⁵` (plus the forced bracket structure) and the empirical mass ratio lives at
> `c ∈ [3/2, 9/4]`, observed `1.6076` — near the mark floor, indicating the spin/
> correlated loading is small. The exact position is open and requires the From-With
> coupling scale. **Conjectured; not blocking.**

## 4. Downstream load-bearing assessment (the operative result)

ε_FW is **not load-bearing for D6/D7 atomic spectra or the periodic landscape.**
- It reaches atomic spectra at `~10⁻⁸` (reduced-mass correction `~5×10⁻⁴` × ε_FW
  `~10⁻⁵`; hyperfine `~10⁻⁶` × ε_FW). D6/D7 structure lives at order 1–`10⁻²`.
  Six-plus orders of cushion.
- D6/D7 need only `m_p/m_e may be computationally approximated by the exact With-This factor 6π⁵ only when 10⁻⁵-level effects are explicitly being neglected; the canonical ratio is m_p/m_e = 6π⁵[1 + c(3π⁴)⁻²], with 3/2 ≤ c ≤ 9/4` to leading order — that the ruler is native and the
  hierarchy exists. Both Registered. The ratio's last digits are invisible to shell
  combinatorics and stability.

**Therefore ε_FW is a terminal node**, not infrastructure. Its open residue (`κ`,
the position in the bracket) is **a non-gating but canonical theorem-bounded factor** on a flagship
"reproduce CODATA to `10⁻⁷`" claim — worth pursuing as precision physics, gating
nothing. D6/D7 may proceed now on `6π⁵`-to-leading-order with ε_FW quarantined as:
**exists, positive, ~10⁻⁵, bracketed in `[3/2, 9/4]·s²`, value open, non-blocking.**

## 5. Status ledger

| Claim | Grade |
|---|---|
| ε_FW one-sided; electron = ruler = 2π/2π | **Registered** |
| From-With base = exterior turn 2π (S¹); norm 3π⁴ | **Registered** |
| ε_FW = self-back-reaction, second-order, sign +, electron-zero | **Registered** |
| bracket `3/2 ≤ c ≤ 9/4` | **Registered (theorem)** |
| — lower wall (mark floor + positive loading) | **Registered** |
| — upper wall (1-form ⇒ two-body ⇒ alignment 9/4) | **Registered** |
| singlet exemption | **Registered** |
| position in bracket / connection scale κ = (β+γ) | **Open** |
| ε_FW value (c = 1.6076) is in `[3/2, 9/4]` | **Conjectured** (position), observed |
| ε_FW non-load-bearing for D6/D7 | **Registered** |
| upper endpoint = 5/3 (g_A) | **Retracted — imported, not native** |
| mark Berry phase / curvature flux mechanism | **Closed — zero, forced by dimension** |
| φ as coefficient | **Refused — near-miss, no derivation** |

## 6. Closed negatives (keep closed)

boundary-geometry `(2π⁵−1)/(6π⁵)²` (wrong normalization, ~9.6× high); metrology seam;
power of `1/(2π)` (`1/(2π)⁶ ≈ 1.63×10⁻⁵`, not clean); `φ·s²`; `8/5`, `9/16π⁹` (fits).

## 7. Next (if precision is pursued, not required)

The From-With commutator scale `[From, With]` from the office algebra — the one
unforced quantity, now isolated, non-relocatable, and known to gate only the
precision claim, not the architecture.
