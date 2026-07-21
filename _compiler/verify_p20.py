#!/usr/bin/env python3
"""Deterministic P20 normalization verifier.

Run from any directory inside the repository:
    python3 _compiler/verify_p20.py --base 6d88509b900add3340f7a688ab58e66a0ee30134

An optional overlay directory supports failure-capability tests. A file in the overlay
replaces the same repository-relative file for semantic checks without mutating the tree.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from fractions import Fraction
from pathlib import Path


LOCAL = "p20-baryon-closure-and-proton-neutron-relation.md"
GLOBAL = "physics-domain-mature-status.md"
FRONTIERS = ("P20-F1", "P20-F2", "P20-F3")
P20_BASE = "6d88509b900add3340f7a688ab58e66a0ee30134"


def git(root: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=root,
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if result.returncode:
        detail = result.stderr.strip() or result.stdout.strip()
        raise RuntimeError(f"git {' '.join(args)} failed: {detail}")
    return result.stdout


def require(errors: list[str], condition: bool, message: str) -> None:
    if not condition:
        errors.append(message)


def corpus_text(root: Path, relative: str | Path, overlay: Path | None) -> str:
    relative_path = Path(relative)
    if overlay is not None and (overlay / relative_path).is_file():
        return (overlay / relative_path).read_text(encoding="utf-8")
    return (root / relative_path).read_text(encoding="utf-8")


def changed_markdown(root: Path, base: str) -> list[Path]:
    names = git(root, "diff", "--name-only", "--diff-filter=ACMR", f"{base}...HEAD")
    return sorted(
        (root / name for name in names.splitlines() if name.endswith(".md")),
        key=lambda path: path.relative_to(root).as_posix(),
    )


def check_links(root: Path, paths: list[Path], errors: list[str]) -> int:
    pattern = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
    checked = 0
    for path in paths:
        text = path.read_text(encoding="utf-8")
        for raw_target in pattern.findall(text):
            target = raw_target.strip().split("#", 1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            target = target.replace("%20", " ")
            checked += 1
            resolved = (path.parent / target).resolve()
            require(
                errors,
                resolved.exists(),
                f"broken local link in {path.relative_to(root)}: {raw_target}",
            )
    return checked


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", default=P20_BASE, help="exact base ref for the PR diff")
    parser.add_argument(
        "--overlay",
        type=Path,
        help="temporary content overlay for failure-capability tests",
    )
    args = parser.parse_args()

    root_text = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if root_text.returncode:
        print("FAIL repository discovery")
        return 1
    root = Path(root_text.stdout.strip()).resolve()
    overlay = args.overlay.resolve() if args.overlay else None
    errors: list[str] = []

    try:
        base_sha = git(root, "rev-parse", f"{args.base}^{{commit}}").strip()
    except RuntimeError as error:
        print(f"FAIL base resolution: {error}")
        return 1
    require(
        errors,
        base_sha == P20_BASE,
        f"base must resolve to exact P20 base {P20_BASE}; got {base_sha}",
    )

    local = corpus_text(root, LOCAL, overlay)
    global_text = corpus_text(root, GLOBAL, overlay)

    required_local = (
        "## Unit opening note",
        "## Authority adjudication",
        "## Current understanding",
        "### 1. Baryon closure",
        "### 2. What proton and neutron share, and what differs",
        "### 3. Sign: a candidate relief route, not a completed derivation",
        "### 4. Mark algebra and the candidate `1/4`",
        "### 5. Magnitude: selected ledger under explicit conditions",
        "### 6. P21 boundary",
        "## Claim record",
        "## Local frontier",
        "## Verdict",
        "**Direct Jordan rulings:** none carries unique P20 work.",
        "P20 does not derive beta decay",
    )
    for item in required_local:
        require(errors, item in local, f"missing canonical catalog element: {item}")

    for frontier in FRONTIERS:
        files = []
        for path in root.rglob("*.md"):
            rel = path.relative_to(root)
            if ".git" in rel.parts or "_compiler/verification" in rel.as_posix():
                continue
            if frontier in corpus_text(root, rel, overlay):
                files.append(rel.as_posix())
        require(
            errors,
            sorted(files) == sorted([GLOBAL, LOCAL]),
            f"{frontier} must occur only in local/global files; got {sorted(files)}",
        )
        require(
            errors,
            local.count(f"### {frontier} —") == 1,
            f"{frontier} must have one local heading",
        )
        require(
            errors,
            global_text.count(f"**{frontier} —") == 1,
            f"{frontier} must have one global entry",
        )

    # Formula verification uses exact rational arithmetic.
    uu = dd = Fraction(1)
    ud = Fraction(-1, 2)
    p_norm = 4 * uu + dd + 4 * ud
    n_norm = uu + 4 * dd + 4 * ud
    p_dot_n = 2 * uu + 2 * dd + 5 * ud
    normalized_overlap = p_dot_n / p_norm
    squared_overlap = normalized_overlap**2
    require(errors, p_norm == 3 and n_norm == 3, "mark norms are not both 3")
    require(errors, p_dot_n == Fraction(3, 2), "mark inner product is not 3/2")
    require(errors, normalized_overlap == Fraction(1, 2), "normalized overlap is not 1/2")
    require(errors, squared_overlap == Fraction(1, 4), "squared overlap is not 1/4")

    active_files = (
        LOCAL,
        GLOBAL,
        "flavor-mark-metric-and-neutron.md",
        "d6-persistence.md",
        "p13-particle-identity-and-native-role-taxonomy.md",
        "03-10-physics-concept-load-pass-ledger.md",
        "07-particle-identity-ledger.md",
        "11-decay-product-registration.md",
        "sm-content-smuggle-audit-frontier.md",
        "physics-domain-mature-status.md",
        "physics-domain-work-plan.md",
        "physics-chemistry-gate-crossing.md",
        "physics-section-guide.md",
        "physics-source-map.md",
        "physics-walk-checklist.md",
        "supersession-map.md",
        "index.md",
        "epsilon-fw-bracket-result.md",
    )
    combined = "\n".join(corpus_text(root, name, overlay) for name in active_files)
    banned = (
        "heavier sign via relief-valve mechanism Registered",
        "[Registered: mechanism and sign.]",
        "`1/4` = squared mark-access overlap** | **Registered",
        "leading splitting structure `1/(2π) + 1/4` (~1.6%) | **Registered",
        "neutron escape/transition structure and conditional overlap weight established",
        "spin-equivalent mixed mark configuration",
    )
    for phrase in banned:
        require(errors, phrase not in combined, f"obsolete active formulation remains: {phrase}")

    stale_spin_patterns = (
        re.compile(r"equal spin contribution[^|\n]*\|\s*(?:\*\*)?(?:Secured|Registered)"),
        re.compile(r"spin gate \(cancels[^\n]*\|\s*\*\*Registered"),
        re.compile(r"spin contributes (?:\*\*)?equally[^\n]{0,160}\[Registered", re.IGNORECASE),
    )
    for pattern in stale_spin_patterns:
        require(
            errors,
            pattern.search(combined) is None,
            f"active P20 consumer overgrades equal nucleon spin: {pattern.pattern}",
        )

    spin_guards = (
        "selected/model-conditional premise; native nucleon assignment unconstructed",
        "It is not Secured or Registered as native nucleon content",
        "Selected/model-conditional comparison premise; not Secured or Registered",
    )
    for phrase in spin_guards:
        require(errors, phrase in combined, f"equal-spin boundary guard missing: {phrase}")

    p13 = corpus_text(root, "p13-particle-identity-and-native-role-taxonomy.md", overlay)
    markdown_with_resolved_frontier = []
    for path in root.rglob("*.md"):
        rel = path.relative_to(root)
        if ".git" in rel.parts or "_compiler/verification" in rel.as_posix():
            continue
        if "P13-F1" in corpus_text(root, rel, overlay):
            markdown_with_resolved_frontier.append(rel.as_posix())
    require(
        errors,
        not markdown_with_resolved_frontier,
        "resolved P13 positive-differentiation frontier remains in "
        + str(sorted(markdown_with_resolved_frontier)),
    )
    p13_routes = (
        "P14 now supplies their `uud`/`udd` mark differentiation",
        "P15 supplies their outward/neutral valence differentiation",
        "P20 owns the mass relation",
        "P21 owns decay",
        "### P13-F2 — Neutrino office trace",
        "### P13-F3 — Taxonomy completeness",
    )
    for phrase in p13_routes:
        require(errors, phrase in p13, f"P13 routing/frontier guard missing: {phrase}")

    required_status = (
        "framework-derived positive sign are therefore **Conjectured**",
        "`1/4` is **Conjectured as a physical access weight**",
        "complete magnitude expression is therefore **Conjectured**",
        "observed positive sign is empirical corroboration, not framework warrant",
        "P20 supplies no decay result",
    )
    for phrase in required_status:
        require(errors, phrase in local, f"canonical status guard missing: {phrase}")

    p19_boundary_ok = (
        "P19's electron ruler and proton/electron ratio are inherited rather than reopened"
        in local
        and "P20 does not reopen it" in local
    )
    p21_boundary_ok = (
        "P20 does not derive beta decay" in local and "Those belong to P21" in local
    )
    require(errors, p19_boundary_ok, "P19 inherited/not-reopened boundary assertion failed")
    require(errors, p21_boundary_ok, "P21 decay-exclusion boundary assertion failed")

    changed = changed_markdown(root, args.base)
    link_count = check_links(root, changed, errors)

    diff_check = subprocess.run(
        ["git", "diff", "--check", f"{args.base}...HEAD"],
        cwd=root,
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    require(
        errors,
        diff_check.returncode == 0,
        "diff hygiene failed: " + (diff_check.stdout + diff_check.stderr).strip(),
    )

    print("P20 deterministic normalization verification")
    print(f"base: {args.base}")
    print(f"changed Markdown files checked: {len(changed)}")
    print(f"local Markdown links checked: {link_count}")
    print("frontier file placement: local canonical + global summary")
    print(f"mark norms: {p_norm}, {n_norm}")
    print(f"mark inner product: {p_dot_n}")
    print(f"normalized overlap: {normalized_overlap}")
    print(f"squared overlap: {squared_overlap}")

    if errors:
        print(f"FAIL ({len(errors)} errors)")
        for error in errors:
            print(f"- {error}")
        return 1
    print("resolved P13 differentiation frontier: absent")
    print("equal-spin nucleon standing: selected/model-conditional only")
    print("P19 boundary: inherited, not reopened")
    print("P21 boundary: decay excluded")
    print("diff hygiene: checked")
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
