#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "canonical-status-audit-report.md"
EXCLUDED = {'.git', 'node_modules'}

REPLACEMENTS = {
    "| Λ structural meaning | Registered | Reflexive closure gives metric-proportional, positive w=-1 form. | Magnitude Open; w=-1 complete-closure argument is structural, not explicit dynamics. |":
    "| Λ structural meaning and scaling | Registered | Reflexive closure gives metric-proportional, positive `w=-1` form; horizon-scale self-holding gives `Λ ∼ R_H^-2`. | Native complete value `Λ_complete = 3 R_H^-2` is Conjectured-strong; present `Λ = 3 f_reflexive R_H^-2` uses empirical state input; dynamics `w(z)` remain Open. |",
    "- Λ magnitude as smallest/largest capstone ratio; interesting, but not the entry point for value work.":
    "- Λ dynamics and exact state-selection remain Open; structural meaning and `R_H^-2` scaling are Registered, while the native complete coefficient `3` is Conjectured-strong.",
    "| Full Einstein equation | Registered conditional; Conjectured for nonlinear sector | Weak-field Poisson/curvature line is strong; ledger later closes the old symmetric conserved rank-2 source premise structurally. | Adjudication (2026-06-21, Item 4): three open gates — tensor completeness beyond g00, strong-field/nonlinear regime, and **the second-order premise being imported from Lovelock rather than derived (the most promotable gate: derive it from a framework closure-order bound)**; plus exact `G`. See [gravity-and-curvature](gravity-and-curvature.md). |":
    "| Full Einstein equation | Registered conditional on manifold/order recovery; nonlinear sector not sealed | The second-order/locality premise has been promoted to Registered conditional status, and Lovelock is used as rule-given tensor rigidity rather than as an unmarked import. | Full spatial metric recovery, strong-field/nonlinear validity, and exact `G` remain Open. See [gravity-and-curvature](gravity-and-curvature.md) and [grqm-conflict-status](grqm-conflict-status.md). |",
    "| Mass as self-closure | Registered | Strong framework account of mass nature and m:p:E ratios. | Absolute mass values and generation mass tower Open. |":
    "| Mass as self-closure | Registered | Strong framework account of mass nature; the canonical proton/electron ratio is `m_p/m_e = 6π⁵[1 + c(3π⁴)⁻²]`, `3/2 ≤ c ≤ 9/4`. | The bracketed form and bounds are Registered; only the exact internal selection of `c`, absolute masses, and generation mass tower remain Open. |",
    "| Gauge group architecture `SU(3)_c x SU(2)_L x U(1)_Y` | `gauge-structure-result.md`; Φ §§8–12 | Yes, if described as lock | Registered and Sealed for structural group architecture, per current gauge result; Open for magnitudes/assignments |":
    "| Gauge group architecture `SU(3)_c x SU(2)_L x U(1)_Y` | `gauge-structure-result.md`; Φ §§8–12 | Yes, if described as lock | Registered, not Sealed; the alternating/closure-floor bridge remains the named gate; magnitudes and assignments are Open |",
    "1. Realizability-weighting seal: frequency=weight identity; exact |ψ|²-from-pairing; non-physics derivation.":
    "1. Realizability-weighting seal: the frequency=weight identity remains the genuine blocker; exact |ψ|²-from-pairing is substantially grounded, while the non-physics end-to-end derivation remains incomplete.",
    "the probabilistic spine is unconditional (frequency=weight dissolved, R5 grounded);":
    "the probabilistic spine remains conditional at the frequency=weight gate, while R5 is grounded;",
}

NEGATING_CONTEXT = (
    "do not claim", "do not state", "remove ", "strike:", "struck", "needs adversarial",
    "requires adversarial", "before registered-and-sealed", "possible outcomes", "if the ledger proof survives",
    "mathematical step", "sealed as mathematics", "not sealed", "registered-not-sealed", "open", "blocker",
    "remaining gate", "conditional", "rejected", "not proof", "does not prove", "denied", "retracted",
)

RULES = [
    ("LAMBDA_COMPLETE_OVERCLAIM", re.compile(r"Λ\s*(?:=|complete\s*=)\s*3\s*R_H\^-?2", re.I),
     lambda l: not any(x in l.lower() for x in ("conject", "native complete", "conditional"))),
    ("LAMBDA_OMEGA_DERIVATION", re.compile(r"deriv(?:e|es|ed|ation).*Ω_DE|Ω_DE.*deriv", re.I),
     lambda l: "not" not in l.lower() and "does not" not in l.lower()),
    ("LAMBDA_RETRACTED_2PI", re.compile(r"Λ.*2π|2π.*Λ", re.I),
     lambda l: not any(x in l.lower() for x in ("retract", "category error", "not"))),
    ("A4_OVERCLAIM", re.compile(r"A/4|area.*1/4|1/4.*area", re.I),
     lambda l: any(x in l.lower() for x in ("sealed", "exactly derived", "forced")) and not any(x in l.lower() for x in NEGATING_CONTEXT)),
    ("THERMAL_2PI_OVERCLAIM", re.compile(r"2π.*(?:thermal|temperature|period)|(?:thermal|temperature|period).*2π", re.I),
     lambda l: any(x in l.lower() for x in ("sealed", "forced", "exact")) and not any(x in l.lower() for x in NEGATING_CONTEXT + ("remaining", "hinge"))),
    ("BMV_SUPERPOSITION_SMUGGLE", re.compile(r"BMV.*spacetime superposition|spacetime superposition.*BMV", re.I),
     lambda l: any(x in l.lower() for x in ("prove", "proves", "confirm", "requires", "demonstrates")) and not any(x in l.lower() for x in NEGATING_CONTEXT)),
    ("MANIFOLD_OVERCLAIM", re.compile(r"manifold recovery", re.I),
     lambda l: any(x in l.lower() for x in ("sealed", "complete", "proven", "derived")) and not any(x in l.lower() for x in NEGATING_CONTEXT + ("remains",))),
    ("SU3_OVERCLAIM", re.compile(r"SU\(3\)", re.I),
     lambda l: any(x in l.lower() for x in ("sealed", "fully forced", "uniquely forced", "exactly derived")) and not any(x in l.lower() for x in NEGATING_CONTEXT)),
    ("FREQUENCY_WEIGHT_OVERCLAIM", re.compile(r"frequency\s*=\s*weight|frequency-is-weight", re.I),
     lambda l: not any(x in l.lower() for x in NEGATING_CONTEXT + ("caveat", "gate"))),
    ("NEUTRON_MAGNITUDE_OVERCLAIM", re.compile(r"neutron.*(?:mass|splitting)|(?:mass|splitting).*neutron", re.I),
     lambda l: any(x in l.lower() for x in ("sealed", "exactly derived", "registered")) and "magnitude" in l.lower() and not any(x in l.lower() for x in NEGATING_CONTEXT + ("conject", "sign", "mechanism"))),
    ("HYPERCHARGE_OVERCLAIM", re.compile(r"hypercharge", re.I),
     lambda l: any(x in l.lower() for x in ("sealed", "exact assignments", "assignments derived", "fully derived")) and not any(x in l.lower() for x in NEGATING_CONTEXT)),
    ("GENERATION_THREE_OVERCLAIM", re.compile(r"(?:three|3) generations|generation count", re.I),
     lambda l: any(x in l.lower() for x in ("forced", "derived", "registered", "sealed")) and not any(x in l.lower() for x in NEGATING_CONTEXT)),
]


def process(path: Path):
    original = path.read_text(encoding='utf-8')
    text = original
    changes = []
    for old, new in REPLACEMENTS.items():
        if old in text:
            text = text.replace(old, new)
            changes.append(old[:70])
    if text != original:
        path.write_text(text, encoding='utf-8')
    return changes, text


def main():
    files, modified, flags = [], [], []
    for path in sorted(ROOT.rglob('*.md')):
        if any(part in EXCLUDED for part in path.parts):
            continue
        files.append(path)
        changes, text = process(path)
        if changes:
            modified.append((path.relative_to(ROOT), changes))
        for n, line in enumerate(text.splitlines(), 1):
            for name, pattern, predicate in RULES:
                if pattern.search(line) and predicate(line):
                    flags.append((path.relative_to(ROOT), n, name, line.strip()))

    out = [
        '# Canonical-Status Corpus Audit', '',
        f'- Markdown files scanned: **{len(files)}**',
        f'- Files mechanically normalized: **{len(modified)}**',
        f'- Lines requiring semantic adjudication: **{len(flags)}**', '',
        '## Governing distinctions', '',
        '- Λ: meaning/sign/`w=-1` and `R_H^-2` scaling Registered; native complete coefficient `3` Conjectured-strong; present value uses empirical state input; dynamics Open.',
        '- `A/4`: area-law shape and cancellation strong; coefficient not Sealed because the `2π` thermal/modular-flow identification and strong-field Einstein use remain gated.',
        '- BMV-positive is forced for the matter-sourced branch but does not prove actual spacetime superposition.',
        '- Manifold recovery and exact smooth/local-Lorentz continuum recovery remain unsealed even where dimension, criticality, and frame-freedom are Registered.',
        '- `SU(3)` architecture is Registered, not Sealed; the alternating/closure-floor premise remains the named gate.',
        '- Frequency=weight remains the blocker in the realizability-weighting law.',
        '- Neutron sign/mechanism and decay structure may be Registered while the full magnitude remains Conjectured/Open.',
        '- Exact hypercharge assignments and generation count remain Open.', '',
        '## Mechanically normalized files', ''
    ]
    if modified:
        for p, changes in modified:
            out.append(f'- `{p}` — {len(changes)} stale governing formulation(s) updated')
    else:
        out.append('- None.')
    out += ['', '## Semantic-adjudication queue', '']
    if flags:
        for p, n, name, line in flags:
            out.append(f'- `{p}:{n}` — **{name}** — {line}')
    else:
        out.append('- None.')
    REPORT.write_text('\n'.join(out) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
