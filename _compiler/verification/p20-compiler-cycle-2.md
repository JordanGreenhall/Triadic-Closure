# P20 Complete Compiler Review — Cycle 2

Cycle type: second full semantic-unit compiler review, not deterministic-verifier repetition.

Reviewed commit at cycle start: `bcc45e09798bf2381c74efc3b43107d973e13e44`

Reviewed commit at cycle end: `bcc45e09798bf2381c74efc3b43107d973e13e44`

Corpus changes produced by this cycle: none.

A pre-cycle search had exposed stale neutron-witness language in `physics-walk-checklist.md`; that defect was corrected and committed before this cycle began. Cycle 2 therefore started only after all known semantic and verification corrections were committed.

## Reviewed set

Authority and dependency controls:

- `p10-color-singlet-and-representation-consequences.md`
- `with-to-this-closure.md`
- `p12-spin-helicity-handedness-and-chiral-coupling.md`
- `p13-particle-identity-and-native-role-taxonomy.md`
- `p14-flavor-and-mark-geometry.md`
- `p15-charge-hypercharge-valence-and-center-locking.md`
- `p16-quantitative-qcd-dynamics-and-quarantine.md`
- `p17-mass-as-closure-maintenance.md`
- `p18-closure-inherited-metric-and-2pi5-measure.md`
- `p19-native-electron-ruler-and-proton-electron-ratio.md`
- `amplitude-readout-theorem.md`

Canonical, supporting, and historical P20 sources:

- `p20-baryon-closure-and-proton-neutron-relation.md`
- `flavor-mark-metric-and-neutron.md`
- `neutron-consideration.md`

Living consumers and controls:

- `03-10-physics-concept-load-pass-ledger.md`
- `07-particle-identity-ledger.md`
- `11-decay-product-registration.md`
- `d6-persistence.md`
- `epsilon-fw-bracket-result.md`
- `physics-chemistry-gate-crossing.md`
- `physics-domain-mature-status.md`
- `physics-domain-work-plan.md`
- `physics-walk-checklist.md`
- `sm-content-smuggle-audit-frontier.md`

Authority, disposition, and reading path:

- `index.md`
- `overview/triadic-closure-reading-order.md`
- `physics-section-guide.md`
- `physics-source-map.md`
- `supersession-map.md`

Verification and reader controls:

- `_compiler/verify_p20.py`
- `_compiler/verification/p20-fresh-reader.md`
- `_compiler/verification/p20-compiler-cycle-1.md`
- both current failure-capability outputs

## Pass results

| Pass | Second-review result |
|---|---|
| 0 — Authority | Claim-specific lineage remained stable. P20 is canonical; the integrated neutron page is supporting; the neutron draft is historical/adversarial. P12 and P16 do not warrant a native equal-spin nucleon theorem. No authority change was found. |
| 1 — Semantics | Shared color closure and positive `uud`/`udd` differentiation remain distinct from the selected equal-spin premise. Sign, physical access weight, and complete magnitude remain Conjectured. P20 supplies no decay result. No semantic change was found. |
| 2 — Propagation | Canonical, supporting, status, identity, persistence, work-plan, checklist, smuggle-control, source-map, guide, and supersession consumers agree on selected equal spin, Conjectured ordering/access/magnitude, and P21-owned decay. No propagation change was found. |
| 3 — Structure | The canonical/supporting/historical split remains natural and no file performs an incompatible new job. No structural change was found. |
| 4 — Information architecture | Index, reading order, section guide, source map, and supersession map route the reader to P20 first and visibly bound the retained sources. No navigation change was found. |
| 5 — Frontier audit | The resolved P13 positive-differentiation frontier is absent; P13-F2 and P13-F3 remain unchanged. P20-F1, P20-F2, and P20-F3 each occur in exactly the canonical local page and global physics status. No frontier change was found. |
| 6 — Claim status | Equal spin is selected/model-conditional only. Positive mark differentiation keeps its inherited P14 grade. Sign, physical `1/4`, and magnitude remain Conjectured; observations remain empirical checks. No grade change was found. |
| 7 — Vocabulary | `selected/model-conditional`, `native nucleon assignment`, `mark differentiation`, `physical access weight`, and P21 ownership are used consistently. Historical uses are behind an explicit supersession guard. No vocabulary change was found. |
| 8 — Notation | Mark vectors, inner products, normalized overlap, square, ledger symbols, and inherited P19 expression remain consistent. Independent rational arithmetic again returned norms `3`, inner product `3/2`, overlap `1/2`, and square `1/4`. No notation change was found. |
| 9 — Compression/disposition | The supporting page still retains unique derivation; the historical page still retains unique failed-route evidence. Both have explicit authority guards. No merge, archive, or deletion was warranted. |
| 10 — Readability | A fresh-reader/adversarial reading recovered the canonical owner, selected spin premise, positive mark differentiation, three exact frontiers, P19 inheritance, and P21 exclusion without conversational context. No readability change was found. |
| 11 — Verification | Exact-base verifier passed at the reviewed commit: 21 changed Markdown files, 293 local links, frontier placement, mark arithmetic, resolved-frontier absence, equal-spin grade, P19 boundary, P21 boundary, and diff hygiene all passed. Targeted Git searches and authority-path searches also passed. |

## Targeted second-review evidence

- `git grep -n 'P13-F1' HEAD -- '*.md'`: no occurrences.
- Exact searches for `spin-equivalent`, `spin contributes equally`, `equal spin contribution`, and `spin gate (cancels` returned four occurrences: the canonical and supporting occurrences explicitly say selected/model-conditional, while the two historical-body occurrences are governed by the explicit supersession notice at the top of `neutron-consideration.md`.
- P13 still states that P14 supplies `uud`/`udd`, P15 supplies outward/neutral valence, P20 owns the mass relation, and P21 owns decay; P13-F2 and P13-F3 remain unchanged.
- Each P20 frontier ID resolves to only `p20-baryon-closure-and-proton-neutron-relation.md` and `physics-domain-mature-status.md`.
- Cycle start and end commit are identical, and the working tree remained unchanged throughout the corpus review.

## Deterministic verification

Command:

`python3 _compiler/verify_p20.py --base 6d88509b900add3340f7a688ab58e66a0ee30134`

Result: PASS.

The deterministic output is stored separately as verifier output. It is corroborating evidence, not a substitute for this compiler cycle.

## Cycle result

PASS — FIXED POINT. The second complete passes 0–11 compiler review produced no corpus changes.
