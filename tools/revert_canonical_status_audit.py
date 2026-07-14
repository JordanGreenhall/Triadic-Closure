#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REPLACEMENTS = {
    "archivist-instructions-foundation-audit.md": [
        (
            "the probabilistic spine remains conditional at the frequency=weight gate, while R5 is grounded;",
            "the probabilistic spine is unconditional (frequency=weight dissolved, R5 grounded);",
        ),
    ],
    "_compiler/02-audit-repairs-semantic-inventory.md": [
        (
            "**Adjudication:** retained. Together with the detailed F8 construction, this supplies the native non-contextuality premise. This proposes a route that could remove the old `frequency=weight` demand, but until it is integrated into and accepted by `realizability-weighting-law.md`, frequency=weight remains the live blocker in the current result page.",
            "**Adjudication:** retained. Together with the detailed F8 construction, this supplies the native non-contextuality premise. The old `frequency=weight` demand is not a live dependency.",
        ),
        (
            "3. AUD-007 proposes a route that may eventually remove `frequency=weight` from the live probability dependency graph; until that route is integrated into and accepted by `realizability-weighting-law.md`, frequency=weight remains the current blocker, alongside verification of the F8/F9 construction.",
            "3. AUD-007 removes `frequency=weight` from the live probability dependency graph but does not eliminate the need to verify the F8/F9 construction itself.",
        ),
    ],
    "locked-actual-decrement-map.md": [
        (
            "| Gauge group architecture `SU(3)_c x SU(2)_L x U(1)_Y` | `gauge-structure-result.md`; Φ §§8–12 | Yes, if described as lock | Registered, not Sealed; the alternating/closure-floor bridge remains the named gate; magnitudes and assignments are Open |",
            "| Gauge group architecture `SU(3)_c x SU(2)_L x U(1)_Y` | `gauge-structure-result.md`; Φ §§8–12 | Yes, if described as lock | Registered and Sealed for structural group architecture, per current gauge result; Open for magnitudes/assignments |",
        ),
    ],
    "physics-domain-mature-status.md": [
        (
            "| Full Einstein equation | Registered conditional on manifold/order recovery; nonlinear sector not sealed | The second-order/locality premise has been promoted to Registered conditional status, and Lovelock is used as rule-given tensor rigidity rather than as an unmarked import. | Full spatial metric recovery, strong-field/nonlinear validity, and exact `G` remain Open. See [gravity-and-curvature](gravity-and-curvature.md) and [grqm-conflict-status](grqm-conflict-status.md). |",
            "| Full Einstein equation | Registered conditional; Conjectured for nonlinear sector | Weak-field Poisson/curvature line is strong; ledger later closes the old symmetric conserved rank-2 source premise structurally. | Adjudication (2026-06-21, Item 4): three open gates — tensor completeness beyond g00, strong-field/nonlinear regime, and **the second-order premise being imported from Lovelock rather than derived (the most promotable gate: derive it from a framework closure-order bound)**; plus exact `G`. See [gravity-and-curvature](gravity-and-curvature.md). |",
        ),
        (
            "| Λ structural meaning and scaling | Registered | Reflexive closure gives metric-proportional, positive `w=-1` form; horizon-scale self-holding gives `Λ ∼ R_H^-2`. | Native complete value `Λ_complete = 3 R_H^-2` is Conjectured-strong; present `Λ = 3 f_reflexive R_H^-2` uses empirical state input; dynamics `w(z)` remain Open. |",
            "| Λ structural meaning | Registered | Reflexive closure gives metric-proportional, positive w=-1 form. | Magnitude Open; w=-1 complete-closure argument is structural, not explicit dynamics. |",
        ),
        (
            "| Mass as self-closure | Registered | Strong framework account of mass nature; the canonical proton/electron ratio is `m_p/m_e = 6π⁵[1 + c(3π⁴)⁻²]`, `3/2 ≤ c ≤ 9/4`. | The bracketed form and bounds are Registered; only the exact internal selection of `c`, absolute masses, and generation mass tower remain Open. |",
            "| Mass as self-closure | Registered | Strong framework account of mass nature and m:p:E ratios. | Absolute mass values and generation mass tower Open. |",
        ),
        (
            "1. Realizability-weighting seal: the frequency=weight identity remains the genuine blocker; exact |ψ|²-from-pairing is substantially grounded, while the non-physics end-to-end derivation remains incomplete.",
            "1. Realizability-weighting seal: frequency=weight identity; exact |ψ|²-from-pairing; non-physics derivation.",
        ),
        (
            "- Λ dynamics and exact state-selection remain Open; structural meaning and `R_H^-2` scaling are Registered, while the native complete coefficient `3` is Conjectured-strong.",
            "- Λ magnitude as smallest/largest capstone ratio; interesting, but not the entry point for value work.",
        ),
    ],
}

for rel, pairs in REPLACEMENTS.items():
    path = ROOT / rel
    text = path.read_text(encoding="utf-8")
    for old, new in pairs:
        if old in text:
            text = text.replace(old, new)
    path.write_text(text, encoding="utf-8")

workflow = ROOT / ".github/workflows/normalize-references.yml"
text = workflow.read_text(encoding="utf-8")
for fragment in (
    "      - 'tools/audit_canonical_statuses.py'\n",
    "      - 'tools/finalize_canonical_statuses.py'\n",
    "      - 'tools/revert_canonical_status_audit.py'\n",
    "      - name: Finalize canonical-status adjudications\n        run: python3 tools/finalize_canonical_statuses.py\n\n",
    "      - name: Audit and normalize other canonical statuses\n        run: python3 tools/audit_canonical_statuses.py\n\n",
    "      - name: Revert canonical-status audit changes\n        run: python3 tools/revert_canonical_status_audit.py\n\n",
):
    text = text.replace(fragment, "")
text = text.replace("git commit -m 'Audit and normalize canonical statuses across corpus'", "git commit -m 'Normalize canonical proton-electron mass ratio across corpus'")
workflow.write_text(text, encoding="utf-8")

for rel in (
    "canonical-status-audit-report.md",
    "tools/audit_canonical_statuses.py",
    "tools/finalize_canonical_statuses.py",
    "tools/revert_canonical_status_audit.py",
):
    path = ROOT / rel
    if path.exists():
        path.unlink()
