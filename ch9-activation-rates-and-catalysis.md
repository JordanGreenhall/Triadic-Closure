---
title: CH9 Activation, Rates, and Catalysis
type: chemistry-result
created: 2026-07-23
updated: 2026-07-23
status: current
confidence: medium
sources:
  - ch3-maintenance-relief-and-energetic-ordering.md
  - ch8-reaction-site-taxonomy-and-acid-base-readings.md
  - p17-mass-as-closure-maintenance.md
  - _compiler/04-chemistry-walk-semantic-inventory.md
  - _compiler/verification/ch9-authority-adjudication.md
---

# CH9 — Activation, Rates, and Catalysis

## Standing summary

CH9 owns the first normalized chemistry dynamics package after CH8's reaction-site taxonomy. Its exact scope is activation, rate propensity, the conditional exponential rate form, and catalyst cycles.

The structural package is **Conjectured-strong and Unregistered as a completed physical kinetics theory**. CH9 identifies what must be supplied for a reaction-site passage to become dynamically available, how comparative passage propensity may depend on an activation burden, and how a catalyst may alter the route while being restored through a cycle. It does not derive calibrated rate constants, empirical activation energies, molecular mechanisms, or thermodynamic direction.

## Unit boundary

CH9 owns:

1. activation as the additional closure-maintenance burden along a passage route;
2. comparative rate propensity as accessibility of an activation ridge under available variation;
3. the conditional exponential dependence of passage frequency on a dimensionless activation burden;
4. catalysis as a restored alternate passage cycle with a lower maximal activation burden.

CH9 does not own:

- CH8 reaction-site taxonomy or acid/base readings;
- CH10 thermodynamic direction, free-energy ordering, equilibrium, or equilibrium constants;
- empirical Arrhenius parameters, transition-state geometries, detailed mechanisms, solvent models, diffusion limits, tunneling corrections, or measured rate constants;
- catalyst discovery tables, enzyme specificity, turnover numbers, poisoning, selectivity, or industrial process data.

## Activation ridge

A CH8 passage specifies the kind of site re-apportionment at issue. CH9 adds the dynamics question: whether there exists a realizable route connecting the admitted initial and final standings, and what additional maintenance burden is encountered along that route.

For a route `gamma` through a passage configuration class, write the maintenance profile schematically as `M_gamma(s)`. The activation burden relative to the initial standing is

`Delta M^ddagger(gamma) = max_s M_gamma(s) - M_initial`.

This is a structural definition only. CH9 does not yet supply a native chemistry maintenance functional, a complete path space, units, or calibrated values. Those remain dependent on CH3 and on an explicit passage construction.

The effective activation burden for the passage is the infimum over admitted routes:

`Delta M^ddagger = inf_gamma Delta M^ddagger(gamma)`.

No claim is made that the infimum is attained, unique, or represented by an empirical transition state without further construction.

## Rate propensity

At fixed environmental provision, a passage with a smaller admitted activation burden is proposed to have greater rate propensity than an otherwise comparable passage with a larger burden. This is a comparative ordering claim, not a numerical rate law.

Rate propensity is distinct from thermodynamic direction. A passage may be dynamically accessible without being thermodynamically favored, and a thermodynamically favored passage may remain slow because its activation burden is high. CH10 owns direction and equilibrium.

## Conditional exponential form

If the available variation relevant to crossing the activation ridge has an exponential tail in the dimensionless burden `Delta M^ddagger / Theta`, then the passage frequency has the conditional form

`k = A exp(-Delta M^ddagger / Theta)`.

Here:

- `Theta` is the available variation scale in the same maintenance units;
- `A` is an attempt or encounter factor determined by the admitted local dynamics;
- `Delta M^ddagger` is the effective activation burden.

The exponential form is **Secured only conditionally on the stated tail assumption and a defined passage dynamics**. CH9 does not identify `Theta` with `k_B T`, does not derive the gas constant, does not derive the Arrhenius prefactor, and does not supply numerical activation energies or rate constants.

## Catalyst cycle

A catalyst is reconstructed as an additional standing `C` that participates in an alternate sequence of admitted passages,

`R + C -> I_1 -> ... -> P + C`,

such that:

1. the catalyst is restored at cycle completion;
2. the net reactant-to-product site change is the same as in the uncatalyzed passage;
3. the alternate cycle has a lower maximal activation burden than the best admitted uncatalyzed route.

Catalysis therefore changes route accessibility and rate propensity. It does not change the net CH8 passage identity, and CH9 does not infer that it changes CH10 thermodynamic direction or equilibrium position.

Catalyst restoration is a cycle condition, not a claim that the catalyst is unchanged at every intermediate stage. Catalyst consumption, degradation, poisoning, and side passages remain outside the ideal cycle definition.

## Claim ledger

| Claim | Standing | Registration | Use rule |
|---|---|---|---|
| activation is maximal excess maintenance along an admitted route | Conjectured-strong structural definition | Unregistered physically | requires native functional and path class |
| smaller activation burden gives greater comparative rate propensity | Conjectured | Unregistered | fixed provision and comparable attempt structure required |
| exponential rate form | Secured conditionally | Unregistered physically | requires exponential variation tail and defined dynamics |
| catalyst is a restored alternate passage cycle | Conjectured-strong structural definition | Unregistered physically | explicit cycle occupant required |
| lower cycle maximum increases rate propensity | Conjectured conditionally | Unregistered | does not imply thermodynamic change |

## Smuggle-watches

1. **Activation vocabulary is not a transition-state construction.** Familiar energy diagrams do not supply the native route, path space, or maintenance functional.
2. **The exponential form is conditional.** Arrhenius notation does not import `k_B`, temperature calibration, empirical prefactors, or measured activation energies.
3. **Rate is not direction.** Kinetic accessibility does not establish spontaneity, free-energy ordering, equilibrium, or yield.
4. **Catalysis is not thermodynamic leverage.** A restored lower-burden route does not alter the net initial/final ordering merely by lowering activation.
5. **A catalyst cycle requires restoration.** A reagent consumed stoichiometrically is not a catalyst under this definition.

## Local research frontiers

### CH9-F1 — native activation functional and explicit route

**Standing:** Open and Unregistered.

**Missing:** one admitted CH8 passage, a common configuration class, a native maintenance functional, an explicit route, and a finite activation burden.

**False-completion warning:** a textbook reaction coordinate is not a framework route construction.

### CH9-F2 — physical rate law and scale

**Standing:** exponential form Secured conditionally; physical law Open and Unregistered.

**Missing:** variation distribution, provision scale, attempt factor, units, normalization, and one calibrated rate comparison.

**False-completion warning:** fitting an Arrhenius plot does not derive the framework law.

### CH9-F3 — explicit catalyst cycle

**Standing:** structural cycle definition Conjectured-strong; realization Open.

**Missing:** one admitted uncatalyzed route, one catalyst-participating route, catalyst restoration, common net passage, and proof of a lower maximal activation burden.

**False-completion warning:** empirical catalytic acceleration does not itself exhibit the framework cycle.

## Downstream use rule

Later chemistry may use CH9 only for the graded activation, comparative-rate, conditional-exponential, and catalyst-cycle claims stated here. No later unit may cite CH9 as deriving thermodynamic direction, free energy, equilibrium constants, product ratios, numerical rate constants, empirical activation energies, or catalyst performance data.

## Bottom line

CH9 normalizes activation as route burden, rate propensity as dynamic accessibility, the exponential rate form under an explicit tail assumption, and catalysis as a restored lower-burden passage cycle. It does not normalize thermodynamic direction or equilibrium; those remain CH10.