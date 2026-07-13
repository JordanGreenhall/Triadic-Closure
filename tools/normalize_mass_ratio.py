#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
CANON_ASCII = "m_p / m_e = 6 pi^5 [1 + c(3 pi^4)^-2], with 3/2 <= c <= 9/4"
CANON_UNICODE = "m_p/m_e = 6π⁵[1 + c(3π⁴)⁻²], with 3/2 ≤ c ≤ 9/4"
REPORT = ROOT / "mass-ratio-audit-report.md"
EXCLUDED_PARTS = {'.git', 'node_modules'}

EXACT_REPLACEMENTS = {
    "m_p / m_e = 6 pi^5 x (1 + epsilon_FW)": CANON_ASCII,
    "m_p / m_e = 6 pi^5 (1 + epsilon_FW)": CANON_ASCII,
    "m_p/m_e = 6π⁵(1+ε_FW)": CANON_UNICODE,
    "m_p/m_e = 6π⁵ × (1 + ε_FW)": CANON_UNICODE,
    "m_p/m_e = 6π⁵ x (1 + ε_FW)": CANON_UNICODE,
    "m_p/m_e = 6π⁵ · (1 + ε_FW)": CANON_UNICODE,
    "m_p/m_e = 6π⁵[1 + c(3π⁴)⁻²], with 3/2 ≤ c ≤ 9/4·(1 + ε_FW)": CANON_UNICODE,
    "m_p / m_e ≈ 6 pi^5": "for calculations explicitly insensitive to 10^-5-level effects, the canonical ratio may be computationally truncated to its exact With-This factor 6 pi^5",
    "m_p/m_e ≈ 6π⁵": "for calculations explicitly insensitive to 10⁻⁵-level effects, the canonical ratio may be computationally truncated to its exact With–This factor 6π⁵",
    "D6/D7 need only `m_p/m_e may be computationally approximated by the exact With-This factor 6π⁵ only when 10⁻⁵-level effects are explicitly being neglected; the canonical ratio is m_p/m_e = 6π⁵[1 + c(3π⁴)⁻²], with 3/2 ≤ c ≤ 9/4` to leading order": "D6/D7 may computationally truncate the canonical ratio to its exact With–This factor `6π⁵` because they are insensitive to 10⁻⁵-level effects",
    "D6/D7 may proceed now on `6π⁵`-to-leading-order with ε_FW quarantined as:": "D6/D7 may use the computational truncation `6π⁵` while retaining the canonical bracketed theorem as:",
    "6 pi^5 color-seating ratio": "6 pi^5 exact With-This color-seating factor",
    "6π⁵ color-seating ratio": "6π⁵ exact With-This color-seating factor",
    "6 pi^5 proton mass-as-such": "6 pi^5 exact With-This factor within the proton/electron ratio",
    "6π⁵ proton mass-as-such": "6π⁵ exact With-This factor within the proton/electron ratio",
    "6 pi^5 exact / epsilon_FW bracketed": "the exact With-This factor 6 pi^5 / the theorem-bounded From-With bracket",
    "6π⁵ exact / ε_FW bracketed": "the exact With-This factor 6π⁵ / the theorem-bounded From-With bracket",
    "the same split the mass ratio exhibited (6π⁵ exact; ε_FW bracketed)": "the same split the mass-ratio theorem exhibited: the With–This factor `6π⁵` exact, and the multiplicative From–With coefficient theorem-bounded",
    "a nucleus closure (closed color, 6π⁵,\nRegistered)": "a nucleus closure (closed color, carrying the exact With–This factor `6π⁵` within the canonical bracketed mass ratio, Registered)",
    "optional precision polish": "a non-gating but canonical theorem-bounded factor",
    "The differential between the proven leading term\n> `6π⁵` (plus the forced bracket structure) and the empirical mass ratio": "The measured position of the coefficient within the proven bracketed theorem\n> `m_p/m_e = 6π⁵[1 + c(3π⁴)⁻²]`, relative to the exact With–This factor `6π⁵`,",
    "the first-order effect of the turn carrying\n  the interior *is* `6π⁵`; ε_FW is the residual back-reaction, one order down": "the direct With–This seating of the carried interior is the exact factor `6π⁵`; ε_FW is the second-order From–With back-reaction",
    "measured CODATA ratio `1836.152673`; `6π⁵ = 1836.1181`). The ratio is **empirical**": "measured CODATA ratio `1836.152673`; the exact With–This factor is `6π⁵ = 1836.1181`). The measured numerical ratio is **empirical**",
    "Because `3π⁴ = 6π⁵/2π` is the proton-interior-per-electron-circle ratio, expressing the": "Because `3π⁴ = 6π⁵/2π` is the proton-interior-per-electron-circle normalization, expressing the",
}

BAD_DIRECT_ASCII = re.compile(r"(?<![A-Za-z0-9_])m_p\s*/\s*m_e\s*=\s*6\s*pi\^5(?!\s*\[)")
BAD_DIRECT_UNICODE = re.compile(r"(?<![A-Za-z0-9_])m_p\s*/\s*m_e\s*=\s*6π⁵(?!\s*\[)")


def canonical_note(style: str) -> str:
    if style == 'unicode':
        return ("\n\n**Canonical mass-ratio rule.** The complete proton/electron ratio is "
                f"`{CANON_UNICODE}`. The standalone `6π⁵` is only the exact With–This "
                "color-seating factor within that ratio. The bracketed form, positive sign, "
                "second-order scale, multiplicative placement, and coefficient bounds are "
                "Registered. Only the exact internal selection of `c` remains Open; observation "
                "places `c ≈ 1.6076`.\n")
    return ("\n\n**Canonical mass-ratio rule.** The complete proton/electron ratio is "
            f"`{CANON_ASCII}`. The standalone `6 pi^5` is only the exact With-This "
            "color-seating factor within that ratio. The bracketed form, positive sign, "
            "second-order scale, multiplicative placement, and coefficient bounds are "
            "Registered. Only the exact internal selection of `c` remains Open; observation "
            "places `c approximately 1.6076`.\n")


def insert_note(text: str, note: str) -> str:
    if "Canonical mass-ratio rule." in text:
        return text
    if text.startswith('---\n'):
        end = text.find('\n---\n', 4)
        if end != -1:
            pos = end + 5
            return text[:pos] + note + text[pos:]
    m = re.search(r'^# .+\n', text, flags=re.M)
    if m:
        return text[:m.end()] + note + text[m.end():]
    return note.lstrip() + '\n' + text


def process(path: Path):
    original = path.read_text(encoding='utf-8')
    text = original
    changes = []
    for old, new in EXACT_REPLACEMENTS.items():
        if old in text:
            text = text.replace(old, new)
            changes.append(f"replaced `{old}`")
    if BAD_DIRECT_ASCII.search(text):
        text = BAD_DIRECT_ASCII.sub(CANON_ASCII, text)
        changes.append("repaired direct ASCII equation")
    if BAD_DIRECT_UNICODE.search(text):
        text = BAD_DIRECT_UNICODE.sub(CANON_UNICODE, text)
        changes.append("repaired direct Unicode equation")
    lowered = text.lower()
    has_mass_context = any(k in lowered for k in ('proton/electron', 'proton-to-electron', 'mass ratio', 'mass-ratio', 'm_p/m_e', 'm_p / m_e'))
    has_sixpi = ('6π⁵' in text) or ('6 pi^5' in lowered)
    has_canonical = ('c(3π⁴)⁻²' in text) or ('c(3 pi^4)^-2' in lowered)
    historical = any(part.lower() in {'archive', '_archive'} for part in path.parts) or 'historical' in path.name.lower()
    if has_mass_context and has_sixpi and not has_canonical and not historical:
        style = 'unicode' if '6π⁵' in text else 'ascii'
        text = insert_note(text, canonical_note(style))
        changes.append("inserted canonical reporting rule")
    if text != original:
        path.write_text(text, encoding='utf-8')
    return changes, text


def suspicious_lines(path: Path, text: str):
    out = []
    for i, line in enumerate(text.splitlines(), 1):
        low = line.lower()
        if ('6π⁵' in line or '6 pi^5' in low or 'm_p/m_e' in low or 'm_p / m_e' in low or 'epsilon_fw' in low or 'ε_fw' in line or '1836' in line):
            if BAD_DIRECT_ASCII.search(line) or BAD_DIRECT_UNICODE.search(line):
                out.append((i, 'DIRECT ERROR', line.strip()))
                continue
            if ('6π⁵' in line or '6 pi^5' in low) and any(k in low for k in ('ratio', 'proton mass', 'nucleus mass', 'closure mass')):
                if not any(k in low for k in ('factor', 'not the complete', 'within the ratio', 'canonical', 'bracketed theorem', 'normalization')):
                    out.append((i, 'REVIEW', line.strip()))
    return out


def main():
    files = []
    modified = []
    exceptions = []
    for path in sorted(ROOT.rglob('*.md')):
        if path == REPORT or any(part in EXCLUDED_PARTS for part in path.parts):
            continue
        files.append(path)
        changes, text = process(path)
        if changes:
            modified.append((path.relative_to(ROOT), changes))
        for line_no, kind, line in suspicious_lines(path, text):
            exceptions.append((path.relative_to(ROOT), line_no, kind, line))
    lines = [
        '# Mass-Ratio Corpus Audit', '',
        f'- Markdown files scanned: **{len(files)}**',
        f'- Files modified: **{len(modified)}**',
        f'- Remaining flagged lines: **{len(exceptions)}**', '',
        '## Canonical expression', '',
        f'`{CANON_UNICODE}`', '',
        'The standalone `6π⁵` or `6 pi^5` is the exact With–This factor, never the complete ratio.', '',
        '## Modified files', ''
    ]
    if modified:
        for path, changes in modified:
            lines.append(f'- `{path}` — ' + '; '.join(changes))
    else:
        lines.append('- None.')
    lines += ['', '## Remaining flagged lines', '']
    if exceptions:
        for path, line_no, kind, line in exceptions:
            lines.append(f'- `{path}:{line_no}` — **{kind}** — {line}')
    else:
        lines.append('- None.')
    REPORT.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    direct_errors = [x for x in exceptions if x[2] == 'DIRECT ERROR']
    if direct_errors:
        raise SystemExit(f'{len(direct_errors)} direct mass-ratio errors remain')


if __name__ == '__main__':
    main()
