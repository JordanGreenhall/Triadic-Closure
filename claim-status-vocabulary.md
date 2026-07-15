---
title: Claim Standing and Warrant
type: control
created: 2026-06-21
updated: 2026-07-15
status: control
confidence: high
sources:
  - architectonic-rigor-complete.md
  - triadic-structure-of-relating-rev-canonical.md
  - verification-companion.md
---

# Claim Standing and Warrant

This document governs two questions that must never be collapsed:

1. **Standing:** how strongly does the claim presently stand?
2. **Warrant route:** by what instrument, dependency, theorem, observation, selection, or check does it stand?

A source can authoritatively state a weak standing. A powerful warrant route can reach only a scoped or conditional claim. A high-confidence document can contain Open claims. Document status, source authority, confidence, and claim standing are separate metadata.

## 1. Live claim standings

Four standings form an ordered progression where their claims are comparable:

1. **Open** — the claim or required joint is not presently closed. It may be named as a dependency or frontier, but may not be spent as established.
2. **Conjectured** — a definite live proposal has stated support but has not been registered by the framework.
3. **Registered** — the framework reaches the claim in essence or within an explicitly stated scope. Uniqueness, full closure, an application premise, a numerical value, or some other identified debt may remain.
4. **Registered and Sealed** — within the stated scope, the native construction and the recognized content close bidirectionally: neither side carries additional load. Sealing does not import surplus theorems, conventional associations, values, or extensions belonging to an external name.

One further standing occupies a different ceiling:

- **Defended posit** — the maximal honest standing for an exact-totality claim on which the completeness diagnostic fires. It carries the complete defense profile: no counterexample exhibited, reflexive stability, and examination showing that proposed rivals are not genuine alternatives. It remains falsifiable by a genuine counterexample. It is not an embarrassed substitute for proof and it is not automatically equivalent to Registered or Registered and Sealed; it reports the strongest standing structurally available to that kind of claim.

`Defended posit` is both a standing and the name of its required defense profile. Ordinary statements that something is “defended” do not thereby receive this standing.

## 2. Warrant routes

The standing must be accompanied by the route that earns it. Current route vocabulary includes:

- **dependency** — one-way necessity or co-constitution established by the dependency test;
- **retorsion** — ineliminability established because denial necessarily deploys the denied condition;
- **construction** — genesis exhibited from already secured materials, with no unlicensed input;
- **selection** — one admissible structure chosen under an established boundary; alternatives remain legitimate;
- **mathematical theorem or formal proof** — conclusion secured within named premises, definitions, and inference rules;
- **sealed recognition** — an earned native structure is given an established name while all unearned surplus remains quarantined;
- **empirical input** — observation supplies an explicitly identified fact or number; it does not become an internal derivation;
- **finite check or computation** — a result tied to the exact inputs, range, algorithm, and artifact checked; it is not automatically a theorem;
- **defense profile** — the three-part warrant required for a Defended posit;
- **argument or comparison** — stated support that may warrant Conjectured standing but is not silently upgraded into construction or proof.

Terms such as `forced`, `native`, `derived`, `argued`, `checked`, `theorem`, `recognition`, and `selection` describe the route or force of a result. Except for the exact standing `Defended posit`, they are not substitutes for a live standing.

## 3. Required claim record

Every load-bearing claim must keep these fields distinguishable in prose or metadata:

- exact claim and scope;
- live standing;
- warrant route and named instrument;
- premises and their standings;
- conditions and whether each is discharged;
- empirical inputs or imported mathematical theorems;
- remaining sealing debt or open joint;
- falsifier or countermodel where applicable;
- downstream uses permitted at the present standing.

Confidence (`high`, `medium`, `low`), document roles (`current`, `canonical`, `control`, `frontier`), workflow states (`candidate`, `reviewed`, `pass`), and source authority do not replace any of these fields.

## 4. Conditional claims and premise floors

Grade the conditional result and its instantiated application separately.

- A theorem of the form “if X, then Y” may be Registered or Registered and Sealed as an implication even while X remains Open.
- The actual claim Y may not stand above the weakest undischarged premise or the instrument that connects the premises to Y.
- If a condition is already Registered at the scope being spent, it is a discharged dependency, not a reason to keep writing `conditional` indefinitely.
- If an empirical input supplies a value, distinguish the framework-native relation from the empirically populated instance.
- Conditions, scope, and unresolved debts travel with the claim through every summary and downstream use.

## 5. Normalization of compound and deprecated labels

The following expressions are not additional live standings:

- `Lead` → **Open**, with `research-state: lead` and the owed check stated.
- `Conjectured-strong` → **Conjectured**, with the stronger warrant or evidence stated separately.
- `Registered-candidate` → normally **Conjectured**, with `review-state: candidate-for-registration`; the owning semantic-unit adjudication must confirm the exact mapping and may not promote it merely from the label.
- `Registered-native` → **Registered**, with `route: native construction` or the exact native instrument.
- `Registered-not-Sealed` → **Registered**, with the sealing residuals named.
- `Registered conditional on X` → record the standing of the implication, the standing of X, and the resulting premise floor separately.
- `Dissolved` → a **disposition of a demand, distinction, or pseudo-problem**, not a modal standing. Any positive claim used to establish the dissolution receives its own standing.
- `derived with empirical state input` → record the internally derived relation, the empirical input, and the standing of the populated result separately.
- `pass`, `non-pass`, `quarantine`, `values-side`, `current`, `canonical`, `mature`, and confidence labels → workflow, boundary, document, or confidence metadata, not claim standing.
- `Sealed` used alone → normalize to **Registered and Sealed** only when the source actually establishes that standing and scope; otherwise recover the underlying grade.
- `Locked actual` → deprecated. Translate claim by claim through [Locked Actual Decrement Map](locked-actual-decrement-map.md); never infer a replacement grade mechanically.

These translations are loss-prevention rules, not a corpus-wide search-and-replace authorization. Each substantive semantic unit must adjudicate its own usages against its detailed lineage and surviving repairs.

## 6. No-upgrade rule

Never upgrade standing by compression, rhetorical confidence, a newer summary, a page-level label, or omission of a condition. In particular:

- argued is not proved;
- checked is not theorem;
- finite-range verification is not proof;
- selection is not forced;
- recognition contributes no standing beyond the native structure recognized;
- a relation result is not a first-principles derivation;
- a measure is not an observed frequency;
- an empirical fit is not an internal derivation;
- a candidate is not Registered merely because its parents are Registered.

When the lineage is insufficient, preserve the strongest warranted formulation, state the missing premise precisely, and keep the claim Open or Conjectured as the evidence permits.

## 7. C2 fixed-point test

Standing and warrant are normalized only when:

- every live claim uses one of the five standings above;
- compound labels have been decomposed without changing substantive force;
- route, conditions, inputs, and confidence are no longer encoded as grades;
- page-level metadata cannot silently grade every sentence;
- deprecated `locked actual` uses have been adjudicated individually;
- summaries preserve the weakest premise, scope, and open joint;
- a fresh reader or AI cannot promote a claim by confusing `forced`, `checked`, `candidate`, `current`, or `high confidence` with standing.
