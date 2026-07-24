#!/usr/bin/env python3
"""Verify exact-result strings and local Markdown links.

This script has no semantic function. It checks only that selected high-risk
strings occur in both EXACT-RESULTS.md and their canonical owner, and that local
Markdown links in the compact reader surface resolve to files.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "EXACT-RESULTS.md"

CHECKS: tuple[tuple[str, str, tuple[str, ...]], ...] = (
    ("involution", "02-architectonic-rigor-and-the-mathematics-walk.md", (r"J^2=\mathrm{id}", r"\lambda^2=1")),
    ("flat interval", "04-physics-i-the-walk.md", ("ds² = −dt² + dx² + dy² + dz²", "c = 1")),
    ("native SU(3)", "05-physics-ii-internal-structure-and-matter.md", (r"SL(3,\mathbb C)\cap U(3)=SU(3)",)),
    ("chiral projectors", "05-physics-ii-internal-structure-and-matter.md", (r"P_L=\frac{I-h}{2},\qquad P_R=\frac{I+h}{2}",)),
    ("mark geometry", "05-physics-ii-internal-structure-and-matter.md", (r"e_u\cdot e_d=e_d\cdot e_s=e_s\cdot e_u=-\frac12", r"|P|^2=|N|^2=3,\qquad P\cdot N=\frac32")),
    ("closure measure", "06-physics-iii-actualization-measure-and-mass.md", (r"\operatorname{Vol}_{\rm closure}=\operatorname{Vol}(S^5)\operatorname{Vol}(S^3)=\pi^3\cdot2\pi^2=2\pi^5",)),
    ("seating factor", "06-physics-iii-actualization-measure-and-mass.md", (r"3\cdot2\pi^5=6\pi^5",)),
    ("mass relation", "06-physics-iii-actualization-measure-and-mass.md", (r"\frac{m_p}{m_e}", r"6\pi^5\left[1+c(3\pi^4)^{-2}\right]", r"\frac32\le c\le\frac94")),
    ("atomic occupancy", "08-chemistry-the-walk.md", ("2(2l+1)",)),
    ("atomic spectrum", "08-chemistry-the-walk.md", (r"E_n\propto-\frac{1}{n^2}",)),
    ("Lambda identity", "07-physics-iv-gravity-lambda-grqm.md", (r"w=-1", r"\Lambda=3\Omega_\Lambda R_H^{-2}")),
    ("background flatness", "07-physics-iv-gravity-lambda-grqm.md", (r"\Omega_k=0",)),
    ("aromatic closure", "08-chemistry-the-walk.md", ("2+4k", "4n+2")),
)

LINK_SURFACES = ("README.md", "index.md", "EXACT-RESULTS.md")
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError as exc:
        raise RuntimeError(f"cannot read {path.relative_to(ROOT)}: {exc}") from exc


def check_strings() -> list[str]:
    failures: list[str] = []
    registry = read(REGISTRY)
    for name, owner_name, needles in CHECKS:
        owner_path = ROOT / owner_name
        owner = read(owner_path)
        for needle in needles:
            if needle not in registry:
                failures.append(f"{name}: missing from EXACT-RESULTS.md: {needle}")
            if needle not in owner:
                failures.append(f"{name}: missing from {owner_name}: {needle}")
    return failures


def check_links() -> list[str]:
    failures: list[str] = []
    for surface_name in LINK_SURFACES:
        surface = ROOT / surface_name
        text = read(surface)
        for target in LINK_RE.findall(text):
            if "://" in target or target.startswith("#") or target.startswith("mailto:"):
                continue
            file_part = target.split("#", 1)[0]
            if not file_part:
                continue
            resolved = (surface.parent / file_part).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                failures.append(f"{surface_name}: link escapes repository: {target}")
                continue
            if not resolved.is_file():
                failures.append(f"{surface_name}: missing local link target: {target}")
    return failures


def main() -> int:
    failures = check_strings() + check_links()
    if failures:
        print("Exact-result check failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1
    print(f"Exact-result check passed: {len(CHECKS)} string groups; {len(LINK_SURFACES)} link surfaces.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
