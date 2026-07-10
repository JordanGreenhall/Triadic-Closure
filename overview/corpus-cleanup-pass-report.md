---
title: Corpus Cleanup Pass Report
type: control
created: 2026-06-28
updated: 2026-06-28
status: control
confidence: medium
---

# Corpus Cleanup Pass Report

This page records the current cleanup pass over the synced Triadic Closure Wiki. It is a working control note, not doctrine.

Primary path now used for corpus work:

`/Users/roberthall/Library/CloudStorage/GoogleDrive-jordan.greenhall@gmail.com/My Drive/Triadic Closure Wiki/Triadic Closure Wiki`

## Pass scope

Mechanical inventory found:

- 266 total files
- 125 Markdown files
- 73 active Markdown files outside `raw/` and `archive/`
- 36 raw Markdown provenance files
- 16 archive Markdown files
- 123 generated HTML files under `_site/`

## Corrections made in this pass

1. **Primary path corrected.** `overview/viewing-this-wiki.md` now points to the Google Drive-synced vault, not the stale Desktop path.
2. **Verification language corrected.** `SCHEMA.md`, `results/verification-companion.md`, `overview/corpus-lineage.md`, and `process/agent-execution-rules.md` now treat package-era `verify.py` output as historical provenance, not the current wiki verifier.
3. **Λ status propagated.** `results/gravity-and-curvature.md`, `Frontier Close Loop Execution/12-gravity-full-gr-imports/12-gravity-full-gr-imports Readme.md`, `process/sm-frontier-loop-state/03-10-physics-concept-load-pass-ledger.md`, and `overview/physics-domain-mature-status.md` now agree with [[lambda-derived]] / [[grqm-conflict-status]]: structure Registered; scaling Registered; native complete `3 R_H^-2` Conjectured-strong; present `Λ_present = 3 f_reflexive R_H^-2` with empirical note `f_reflexive ≈ Ω_DE ≈ 0.685`; dynamics / `w(z)` Open.
4. **Second-order full-Einstein route corrected.** Old Lovelock-only / still-conjectural second-order language was replaced with the current split: G1-conditioned one-step-conditioning second-order route Registered conditional; Lovelock-style tensor rigidity rule-given once premises are admitted; not Sealed.
5. **Neutron A₂ stale keystone corrected.** `results/neutron-consideration.md` no longer leaves the one-line summary or §5.2 resting on imported A₂ / flavor-SU(3). It now routes the `1/4` term through [[flavor-mark-metric-and-neutron]] and marks the receipt-complement partition / proton residual as the remaining gates.
6. **Flavor source mapping cleaned.** `overview/physics-source-map.md` no longer points future agents to the original Downloads path as the current source; it identifies the integrated result page and supersession relation.
7. **Flavor result navigation added.** `results/flavor-mark-metric-and-neutron.md` now has Place/Source-link sections for wiki navigation.
8. **Async audit findings folded in.** Corrected gauge architecture over-seal in `overview/locked-actual-decrement-map.md`; updated SU(3) work-plan residuals; corrected Item 1 PASS contradiction; corrected Item 5/6/8/13 electroweak residual routing; corrected electron charge-sign status; moved generation membership from Item 9 to Item 13; corrected neutron interim-status drift in result/process pages; and added `physics-source-map` to the Start Here list.

## Mechanical verification run

After patches:

- Static build succeeded: `python3 _meta/build_html_wiki.py`
- Built 125 pages under `_site/`
- Missing wikilinks: 0
- Stale scan hits for the following live-bad patterns: 0
  - Desktop wiki path
  - stale Λ-open/mere-values-side language
  - live `verify.py` verifier instructions
  - stale Lovelock-only / still-conjectural full-Einstein route wording
  - old neutron A₂ keystone as live grounding

Remaining false-positive scan hit:

- `results/grqm-conflict-status.md` contains “non-exactness only generic / value decoration-dependent” only inside a correction/retraction sentence; this is expected and should not be removed.

## Remaining cleanup frontier

1. Continue subcorpus audit of `results/*.md`, `overview/*.md`, and `Frontier Close Loop Execution/**/*.md` for stale status drift that is not caught by mechanical phrase scans.
2. Normalize missing `Place in the physics section` / `Source links` sections where useful, especially older foundational/result pages that predate the current wiki-organization standard.
3. Decide whether `index.md` should remain intentionally frontmatter-free or receive frontmatter for schema consistency.
4. Sweep generated `_site/` only via rebuild; do not hand-edit generated HTML.

See also: [[physics-domain-mature-status]], [[physics-domain-work-plan]], [[supersession-map]], [[known-failure-modes]], [[agent-execution-rules]].
