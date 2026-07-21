---
title: "P23 — Stress-Energy as a Three-Office Source"
type: result
status: current
created: 2026-07-21
updated: 2026-07-21
confidence: medium
unit: P23
sources:
  - stress-energy-three-offices.md
  - mathematization-F11.md
  - mathematization-F8-F11.md
  - claim-status-vocabulary.md
  - propagation-and-invariant-velocity.md
  - p7-manifold-recovery-and-local-continuum.md
---

# P23 — Stress-Energy as a Three-Office Source

## Bounded verdict

P23 Secures two pieces of conditional mathematics and adjudicates a bounded candidate use of **stress-energy**. Given a licensed spacetime tangent carrier, an observer split, real source weights, and oriented source vectors, the second moment

```text
T^{mu nu} = Sum_a w_a V_a^mu V_a^nu
```

is symmetric. Relative to the selected unit timelike observer, any symmetric rank-two source has three tensor sectors: observer-scalar energy, mixed spatial flux, and pure spatial stress. For a source already licensed as physical stress-energy, that decomposition and its sector vocabulary are Registered at kinematic scope. The further This/From/With alignment is a selected **Conjectured** representational proposal, not a one-to-one theorem: P4 supplies From-time and With-space index kinds, while P17 reads energy through a This–From relation rather than equating energy with This alone.

P23 does **not** establish that every conditioning network supplies the required real weights and tangent vectors, that scalar continuity alone implies tensor conservation, that one effective velocity represents a general multi-stream source, that the network dynamically realizes every spatial-stress component, or that P23's source is already the normalized scalar source of P22. It supplies no Einstein equation, `G`, full metric, nonlinear dynamics, or Lambda result.

## Semantic boundary

The licensed inherited content is:

- a symmetric rank-two source built as a real weighted second moment of oriented vectors;
- its observer-relative energy, flux, and spatial-stress sectors when the input is independently licensed as a physical source;
- a selected candidate office correspondence based on closure, orientation, and co-standing relation;
- conditional local conservation when the complete tensor balance equations are exhibited.

Quarantined surplus includes:

- an unrestricted material stress-energy tensor for arbitrary matter;
- energy conditions, equations of state, pressure laws, viscosity, elasticity, spin currents, or quantum expectation values;
- a framework derivation of all source coefficients or of their dimensions/units;
- identification of This alone with energy or a unique one-to-one office/tensor-sector theorem;
- automatic covariant conservation from the phrase “conservation of registered distinctions”;
- gravitational coupling, Einstein's equation, exact `8 pi G`, full GR, or cosmological dynamics.

## Authority and lineage

This page is the canonical P23 owner. `stress-energy-three-offices.md` is its concise result shadow. `mathematization-F11.md` retains the detailed source proposal and absent-script reports; its full-Einstein/Lovelock continuation is P24 material. `mathematization-F8-F11.md` is earlier supersession-sensitive development evidence. P22 continues to own the weak-field participation-curvature model, its scalar source-normalization gap, and `G`. P24 owns field-equation and full-GR completion.

The named `t_structure.py`, `t_full.py`, and `t_converge.py` scripts are absent. Their alleged executions and convergence values are documentary reports only. The exact algebra below is reproduced independently and does not depend on those reports.

## 1. Conditional second-moment source

Let a selected local continuum realization provide:

- a Lorentzian tangent carrier and a chosen unit timelike observer `u^mu`;
- oriented source vectors `V_a^mu` associated with admitted conditioning flows;
- real weights `w_a` whose source meaning and normalization are stated.

Then define

```text
T^{mu nu} = Sum_a w_a V_a^mu V_a^nu.
```

Each outer product is symmetric, so

```text
T^{mu nu} = T^{nu mu}
```

is theorem-Secured mathematics given the displayed inputs. This does not require an absent script.

The weights must not be called quantum amplitudes without an additional real-weight map. Complex amplitudes cannot be inserted directly into a real stress tensor. Nonnegativity may be selected for kinetic-flow examples, but P23 does not derive it universally.

For a general multi-stream source,

```text
Sum_a w_a V_a^mu V_a^nu != rho V^mu V^nu
```

for any single effective `V` unless the second moment is rank one or extra closure conditions are satisfied. The former F11 equality between these expressions is therefore retained only for a one-stream/rank-one specialization.

## 2. Observer-relative three-sector decomposition

Use signature `(-,+,+,+)` and define the spatial projector

```text
h^mu_nu = delta^mu_nu + u^mu u_nu.
```

For a symmetric `T^{mu nu}`, define

```text
rho       = T_{mu nu} u^mu u^nu,
q^mu      = -h^mu_alpha T^{alpha beta} u_beta,
S^{mu nu} = h^mu_alpha h^nu_beta T^{alpha beta}.
```

Then

```text
T^{mu nu} = rho u^mu u^nu
          + u^mu q^nu + q^mu u^nu
          + S^{mu nu},
```

with `q^mu u_mu=0` and `S^{mu nu}u_nu=0`. This is theorem-Secured decomposition mathematics on the stated carrier and observer split. It is observer-relative, not three observer-free scalar invariants. Component counting remains `1 + 3 + 6 = 10`; “three sectors” must not be misread as three tensor components.

The selected candidate office reading is:

| Office | Tensor sector | Licensed content |
|---|---|---|
| This | `rho` | candidate closure reading of the observer-local energy scalar; P17 requires the change-relative This–From energy relation |
| From | `q^mu` | oriented transport, momentum density, or energy flux |
| With | `S^{mu nu}` | pure spatial relational stress, including isotropic and anisotropic parts |

With is not identical to shear. If desired, `S^{mu nu}=p h^{mu nu}+pi^{mu nu}` separates isotropic pressure from trace-free anisotropic stress; both remain within the spatial relational sector. The tensor split itself is exact, but it does not derive the office table. P4's direct index reading is temporal From versus spatial With: `T^{00}`, `T^{0i}`, and `T^{ij}` are From–From, From–With, and With–With blocks on that carrier. P17 separately says energy is a standing read with respect to admissible change, entering through a This–From relation. Therefore the displayed This/From/With table is selected and **Conjectured**, with registration **Unregistered** as an exact office correspondence. It remains a useful proposal, but is not a theorem that every physical source is generated by exactly one office term.

## 3. Exact conditional population example

Let `n^mu` be a selected unit spatial direction orthogonal to `u^mu`, and admit two oppositely directed source vectors

```text
V_+ = u + n,
V_- = u - n
```

with real positive weights `w_+` and `w_-`. In the local `(u,n)` basis,

```text
T^{00} = w_+ + w_-,
T^{0n} = w_+ - w_-,
T^{nn} = w_+ + w_-.
```

If `w_+ != w_-`, the energy, flux, and spatial-stress sectors are all nonzero. If `w_+=w_-`, net flux cancels while energy and a nonzero relational stress remain. This exact two-stream calculation closes the claim that a nonzero **spatial-stress tensor sector** is merely algebraically available: within the selected multi-stream construction, it is concretely populated. It does not by itself close a With-office derivation, because the office correspondence and native source dynamics remain unconstructed.

The result is conditional. P23 does not thereby prove that the corpus's actual conditioning dynamics admits these vectors and weights, selects them generically, supplies transverse stresses, or realizes every symmetric spatial tensor. The population of an arbitrary `S^{mu nu}` and the framework meaning of its coefficients remain open.

## 4. Conservation is a separate dynamical condition

For the second-moment source,

```text
partial_mu T^{mu nu}
  = Sum_a [partial_mu(w_a V_a^mu)] V_a^nu
  + Sum_a w_a V_a^mu partial_mu V_a^nu.
```

Consequently, scalar continuity by itself does not imply tensor conservation when the source vectors vary. A sufficient conditional route is that each stream satisfies both a continuity equation and force-free/geodesic transport, or that the summed exchange terms cancel under an explicitly stated interaction law. For constant `V_a`, independent continuity `partial_mu(w_a V_a^mu)=0` is sufficient.

The framework principle that registered distinctions are conserved can motivate a local balance law, but it does not by itself construct the continuum divergence, momentum equation, connection terms, or inter-stream exchange cancellation. Covariant conservation `nabla_mu T^{mu nu}=0` remains conditional on the recovered carrier/calculus and an exhibited source evolution.

## 5. Evidence and absent computations

The retained F11 source reports that absent scripts checked symmetry, component structure, an advected flow, and second-order convergence with values `9.6 x 10^-3` at `L=30` and `5.9 x 10^-4` at `L=120`. P23 records those as documentary source claims only. They are not rerun evidence and cannot Secure conservation or a continuum limit.

The symmetry, decomposition, two-stream population, and conservation identity on this page are exact algebra independently reproducible from their displayed premises. Their physical expenditure remains limited by the source-vector, weight, carrier, and dynamics conditions.

## 6. Claim and warrant ledger

| Claim | Epistemic standing | Registration | Reach / debt |
|---|---|---|---|
| Symmetry of `Sum_a w_a V_a^mu V_a^nu` | Secured as theorem mathematics given real weights and vectors | Registered within source-tensor scope | Does not derive inputs or conservation. |
| Observer-relative `rho/q/S` decomposition | Secured as theorem mathematics on a selected Lorentzian carrier and observer split | Registered representationally for an independently licensed physical source | Three sectors, not three components or observer-free invariants. |
| This/From/With correspondence | Conjectured as a selected representational alignment | Unregistered as an exact office correspondence | P4 gives From/With index blocks; P17 gives a This–From energy relation; uniqueness and one-to-one alignment are absent. |
| Two-stream population of energy, flux, and spatial stress | Secured conditionally by displayed algebra | Registered only as source-sector mathematics | Does not establish generic physical population or a With-office derivation. |
| General conditioning-network source law and coefficient meaning | Conjectured | Unregistered beyond the bounded construction | Native vector/weight map and normalization absent. |
| General covariant conservation | Open as a framework construction; Secured conditionally when full balance equations hold | Registered only conditionally | Scalar continuity alone is insufficient. |
| Arbitrary spatial-stress population | Open | Unregistered | No construction of every `S^{mu nu}`, pressure law, or material response. |
| P22 scalar-source identification and `G` | Open under P22 | Unregistered here | P23 does not close P22-F3. |
| Full Einstein/Lovelock field equation | P24-owned | Unregistered here | No P24 promotion follows from source kinematics. |
| Lambda source and cosmological dynamics | P28-owned | Unregistered here | Excluded from P23. |

## 7. Local frontier

### P23-F1 — Native source vectors, weights, and coefficient semantics

**Current strongest result:** a symmetric rank-two second moment is exact once oriented vectors and real weights are supplied; the observer sectors and one selected population example are explicit.

**Missing:** a framework-native map from admitted conditioning events to the tangent vectors and real weights, proof of any positivity/normalization rule, units/ruler meaning, and exclusion or grading of alternative source constructions.

**False-completion risk:** calling `a_k` an amplitude or calling edge count energy can make a real physical source tensor appear automatic.

**Next legitimate research action:** construct the source-vector and real-weight map before coupling it to P22 or P24.

### P23-F2 — Local balance law and covariant conservation

**Current strongest result:** the exact divergence identity states sufficient conditions; independently conserved constant-vector streams furnish a conditional example.

**Missing:** a native local evolution law, momentum/transport equation, inter-stream exchange accounting, covariantization on the recovered carrier, and proof that the resulting total source is divergence-free.

**False-completion risk:** scalar continuity or generic conservation language can be mistaken for `nabla_mu T^{mu nu}=0`.

**Next legitimate research action:** exhibit the local source evolution and prove all terms in the tensor divergence cancel.

### P23-F3 — General spatial-stress population and office correspondence

**Current strongest result:** the two-stream construction populates nonzero spatial stress, including a zero-net-flux case, and the full spatial sector is mathematically available. P4 and P17 supply constraints on any office interpretation.

**Missing:** an admissible network construction for general isotropic and anisotropic `S^{mu nu}`, framework-meaningful coefficients, and a derivation or rejection of the proposed office correspondence consistent with P4's From/With index blocks and P17's This–From energy relation.

**False-completion risk:** one nonzero `T^{nn}` or a rank-one kinetic source can be mistaken for arbitrary material stress-energy.

**Next legitimate research action:** enumerate admissible multi-direction source configurations and determine the realized span of the spatial second moment.

## 8. Integration rules

A downstream page may say:

- P23 conditionally constructs a symmetric rank-two second-moment source;
- every such source admits the stated observer-relative energy/flux/spatial-stress split;
- the This/From/With correspondence is a selected Conjectured proposal, not Registered as an exact office theorem;
- a selected two-stream example populates a nonzero spatial-stress sector, not by itself a derived With-office mode;
- conservation is conditional on complete local balance equations.

A downstream page may not say:

- arbitrary conditioning amplitudes are automatically real stress-energy weights;
- a general multi-stream source equals one rank-one `rho V V` tensor;
- scalar continuity alone proves tensor or covariant conservation;
- all material stresses, coefficients, equations of state, or energy conditions are derived;
- P23 supplies the P22 scalar source normalization, `G`, Einstein's equation, full GR, or Lambda dynamics.

## 9. Source disposition

- **Canonical:** this page.
- **Concise shadow:** `stress-energy-three-offices.md`.
- **Supporting retained source:** the P23 construction and absent-script reports in `mathematization-F11.md`.
- **Earlier development / supersession-sensitive:** `mathematization-F8-F11.md`.
- **P24+ downstream consumers:** `12-gravity-full-gr-imports.md`, `grqm-problem-locator.md`, and `grqm-conflict-status.md`; they cannot upgrade P23.
