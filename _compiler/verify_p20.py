#!/usr/bin/env python3
"""Deterministic, repository-relative verification for normalization unit P20."""

from __future__ import annotations

import re
import subprocess
import sys
from fractions import Fraction
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
CANONICAL = ROOT / "p20-baryon-closure-and-proton-neutron-relation.md"
GLOBAL = ROOT / "physics-domain-mature-status.md"
ACTIVE_EXPENDITURES = (
    "p20-baryon-closure-and-proton-neutron-relation.md",
    "flavor-mark-metric-and-neutron.md",
    "d6-persistence.md",
    "physics-domain-mature-status.md",
    "index.md",
    "07-particle-identity-ledger.md",
    "03-10-physics-concept-load-pass-ledger.md",
    "11-decay-product-registration.md",
    "p13-particle-identity-and-native-role-taxonomy.md",
    "sm-content-smuggle-audit-frontier.md",
    "physics-chemistry-gate-crossing.md",
    "physics-section-guide.md",
    "physics-source-map.md",
)
FRONTIERS = ("P20-F1", "P20-F2", "P20-F3")

checks: list[str] = []
failures: list[str] = []


def check(label: str, condition: bool, detail: str = "") -> None:
    if condition:
        checks.append(label)
    else:
        failures.append(f"{label}: {detail or 'condition not met'}")


def git(*args: str, check_result: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=check_result,
    )


def slugify(heading: str) -> str:
    value = heading.strip().lower()
    value = re.sub(r"[^\w\- ]", "", value, flags=re.UNICODE)
    return re.sub(r"[ -]+", "-", value).strip("-")


def anchors_for(path: Path) -> set[str]:
    anchors: set[str] = set()
    counts: dict[str, int] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        match = re.match(r"^#{1,6}\s+(.+?)\s*$", line)
        if not match:
            continue
        base = slugify(match.group(1))
        count = counts.get(base, 0)
        counts[base] = count + 1
        anchors.add(base if count == 0 else f"{base}-{count}")
    return anchors


try:
    root_from_git = Path(git("rev-parse", "--show-toplevel").stdout.strip()).resolve()
except subprocess.CalledProcessError as exc:
    print(f"FAIL repository discovery: {exc.stderr.strip()}")
    sys.exit(1)
check("repository-relative execution", root_from_git == ROOT, f"git root {root_from_git} != {ROOT}")

canonical = CANONICAL.read_text(encoding="utf-8")
global_text = GLOBAL.read_text(encoding="utf-8")
active = {name: (ROOT / name).read_text(encoding="utf-8") for name in ACTIVE_EXPENDITURES}

catalog_elements = (
    "P20",
    "Baryon closure and proton–neutron relation",
    "singlet",
    "marks",
    "sign",
    "magnitude",
)
check(
    "catalog elements",
    all(element.lower() in canonical.lower() for element in catalog_elements),
    "canonical P20 catalog wording incomplete",
)

for frontier in FRONTIERS:
    local_heading_count = len(re.findall(rf"^###\s+{re.escape(frontier)}\b", canonical, re.MULTILINE))
    global_entry_count = len(re.findall(rf"^\d+\.\s+\*\*{re.escape(frontier)}\b", global_text, re.MULTILINE))
    check(f"{frontier} substantive local placement", local_heading_count == 1, f"found {local_heading_count}")
    check(f"{frontier} substantive global placement", global_entry_count == 1, f"found {global_entry_count}")

local_sections = re.split(r"(?=^###\s+P20-F[123]\b)", canonical, flags=re.MULTILINE)
for frontier in FRONTIERS:
    section = next((part for part in local_sections if re.match(rf"^###\s+{frontier}\b", part)), "")
    check(f"{frontier} finite local discharge", "Finite discharge condition:" in section, "missing finite condition")
    global_line = next((line for line in global_text.splitlines() if re.match(rf"^\d+\.\s+\*\*{frontier}\b", line)), "")
    check(f"{frontier} finite global discharge", "Finite discharge condition:" in global_line, "missing finite condition")

merge_base = git("merge-base", "origin/main", "HEAD").stdout.strip()
added_markdown = [
    line for line in git("diff", "--diff-filter=A", "--name-only", f"{merge_base}..HEAD", "--", "*.md").stdout.splitlines()
    if line
]
link_errors: list[str] = []
link_pattern = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
for relative in sorted(added_markdown):
    source = ROOT / relative
    for line_no, line in enumerate(source.read_text(encoding="utf-8").splitlines(), 1):
        for raw_target in link_pattern.findall(line):
            target = raw_target.strip().split(maxsplit=1)[0].strip("<>")
            if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.IGNORECASE) or target.startswith("mailto:"):
                continue
            path_part, separator, fragment = target.partition("#")
            destination = source if not path_part else (source.parent / unquote(path_part)).resolve()
            if not destination.exists():
                link_errors.append(f"{relative}:{line_no}: missing {target}")
                continue
            if separator and fragment and destination.suffix.lower() == ".md":
                if unquote(fragment).lower() not in anchors_for(destination):
                    link_errors.append(f"{relative}:{line_no}: missing anchor {target}")
check("PR-added Markdown links", not link_errors, "; ".join(link_errors))

u_dot_u = d_dot_d = Fraction(1, 1)
u_dot_d = Fraction(-1, 2)
p_norm = 4 * u_dot_u + d_dot_d + 4 * u_dot_d
n_norm = u_dot_u + 4 * d_dot_d + 4 * u_dot_d
p_dot_n = 2 * u_dot_u + 2 * d_dot_d + 5 * u_dot_d
overlap = p_dot_n / p_norm
squared_overlap = overlap * overlap
check(
    "mark algebra",
    (p_norm, n_norm, p_dot_n, overlap, squared_overlap)
    == (Fraction(3), Fraction(3), Fraction(3, 2), Fraction(1, 2), Fraction(1, 4)),
    f"got {p_norm}, {n_norm}, {p_dot_n}, {overlap}, {squared_overlap}",
)
for literal in ("|P|^2 = |N|^2 = 3", "P·N = 3/2", "= 1/2", "squared overlap = 1/4"):
    check(f"documented algebra {literal}", literal in canonical, "literal absent from canonical page")

check(
    "sign and relief status demoted",
    "**Framework standing:** Conjectured." in canonical
    and "mass-ordering sign" in canonical
    and "Unregistered as framework results" in canonical,
    "canonical sign/mechanism downgrade incomplete",
)
check(
    "physical access status demoted",
    "Conjectured candidate access weight" in canonical
    and "not a Secured or Registered physical weighting measure" in canonical,
    "canonical physical access downgrade incomplete",
)
check(
    "conditional algebra preserved",
    "Given the selected P14 geometry, this algebra is Sealed" in canonical,
    "algebraic result was not preserved at its conditional grade",
)

for name, text in active.items():
    lowered = text.lower()
    check(f"{name} has no actuality warrant", not any(
        phrase in lowered for phrase in (
            "actual exterior electron relation",
            "exists in reality",
            "occupied counterpart",
            "actual electron relation",
            "real external relationship",
        )
    ), "physical actuality/occupancy phrase remains")

stale_patterns = (
    r"(?:m_n-m_p|neutron heavier|relief(?:-valve)? mechanism).{0,120}\b(?:Secured|Registered)\b",
    r"(?:1/4.{0,100}(?:physical|mark-access|access-weight)|(?:physical|mark-access|access-weight).{0,100}1/4).{0,100}\b(?:Secured|Registered)\b",
    r"1/4.{0,100}Registered weighting measure",
    r"1/4.{0,100}Secured conditionally",
)
for name, text in active.items():
    hits = []
    for line_no, line in enumerate(text.splitlines(), 1):
        lowered_line = line.lower()
        explicitly_demoted = (
            "conjectured" in lowered_line
            or "unregistered" in lowered_line
            or "not registered" in lowered_line
            or "not a secured" in lowered_line
            or "superseded" in lowered_line
        )
        if not explicitly_demoted and any(re.search(pattern, line, re.IGNORECASE) for pattern in stale_patterns):
            hits.append(str(line_no))
    check(f"{name} has no stale former grade", not hits, f"lines {','.join(hits)}")

check(
    "P19 boundary explicit",
    "P19's electron ruler and proton/electron mass ratio are inherited rather than reopened" in canonical
    and "P19's residual" in canonical,
    "P19 inheritance/residual boundary missing",
)
check(
    "P21 boundary explicit",
    "P21 With-to-This closure, decay, beta-decay particulars, lifetimes, and decay-product registration are excluded" in canonical
    and "P21 decay particulars remain outside P20" in canonical,
    "P21 exclusion missing",
)

diff_check = git("diff", "--check", f"{merge_base}..HEAD", check_result=False)
check(
    "git diff --check against merge-base with origin/main",
    diff_check.returncode == 0,
    (diff_check.stdout + diff_check.stderr).strip(),
)

print("P20 deterministic verifier")
for index, label in enumerate(checks, 1):
    print(f"PASS {index:02d}: {label}")
if failures:
    for index, failure in enumerate(failures, 1):
        print(f"FAIL {index:02d}: {failure}")
    print(f"RESULT: FAIL ({len(failures)} failed, {len(checks)} passed)")
    sys.exit(1)
print(f"RESULT: PASS ({len(checks)} checks)")
