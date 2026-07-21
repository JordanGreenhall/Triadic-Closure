#!/usr/bin/env python3
"""Deterministic P22 normalization verifier.

Run from any directory inside the repository:
    python3 _compiler/verify_p22.py --base 9085a7443b9cb71808f8c3afc43161929db1263f

An optional overlay directory replaces repository-relative text files for
failure-capability tests without mutating the worktree.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path


LOCAL = "p22-weak-field-gravity-as-participation-curvature.md"
GLOBAL = "physics-domain-mature-status.md"
FRONTIERS = ("P22-F1", "P22-F2", "P22-F3")
P22_BASE = "9085a7443b9cb71808f8c3afc43161929db1263f"
ABSENT_REPORT_SCRIPTS = (
    "f10_geodesic_check.py",
    "f10_factor2.py",
    "f10_deviation.py",
    "f10_tidal_quant.py",
    "f11_poisson.py",
    "f11_harmonic.py",
    "f11_assemble.py",
)


def git(root: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", *args], cwd=root, check=False, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
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
            target = target.strip("<>").replace("%20", " ")
            checked += 1
            resolved = (path.parent / target).resolve()
            require(errors, resolved.exists(), f"broken local link in {path.relative_to(root)}: {raw_target}")
    return checked


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", default=P22_BASE, help="exact base ref for the PR diff")
    parser.add_argument("--overlay", type=Path, help="temporary semantic-check overlay")
    args = parser.parse_args()

    root_result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"], check=False, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    if root_result.returncode:
        print("FAIL repository discovery")
        return 1
    root = Path(root_result.stdout.strip()).resolve()
    overlay = args.overlay.resolve() if args.overlay else None
    errors: list[str] = []

    try:
        base_sha = git(root, "rev-parse", f"{args.base}^{{commit}}").strip()
    except RuntimeError as error:
        print(f"FAIL base resolution: {error}")
        return 1
    require(errors, base_sha == P22_BASE, f"base must resolve to exact P22 base {P22_BASE}; got {base_sha}")

    local = corpus_text(root, LOCAL, overlay)
    global_text = corpus_text(root, GLOBAL, overlay)
    required_local = (
        "# P22 — Weak-Field Gravity as Participation Curvature",
        "## Bounded verdict",
        "## Semantic boundary",
        "## Authority and lineage",
        "## 1. Conditional discrete input",
        "## 4. Documentary reports and conditional analytic tidal mathematics",
        "## 5. Distinct three-dimensional reports, harmonic exterior, and Poisson form",
        "## 6. Claim and warrant ledger",
        "## 7. Local frontier",
        "## 8. Integration rules",
        "## 9. Source disposition",
        "Registered at static weak-field model scope",
        "does not infer a physical scalar density",
        "status: current",
        "G M := A/d_0",
        "documentary report only",
    )
    for item in required_local:
        require(errors, item in local, f"missing canonical P22 element: {item}")

    for frontier in FRONTIERS:
        files: list[str] = []
        for path in root.rglob("*.md"):
            rel = path.relative_to(root)
            if ".git" in rel.parts or "_compiler/verification" in rel.as_posix():
                continue
            if frontier in corpus_text(root, rel, overlay):
                files.append(rel.as_posix())
        require(errors, sorted(files) == sorted([GLOBAL, LOCAL]), f"{frontier} must occur only in local/global files; got {sorted(files)}")
        require(errors, local.count(f"### {frontier} —") == 1, f"{frontier} must have one local heading")
        require(errors, global_text.count(f"**{frontier} —") == 1, f"{frontier} must have one global entry")

    fixed_support = "flat fixed-support anisotropic-walk countermodel"
    require(errors, local.count(fixed_support) == 1, "P22-F1 local entry must contain the fixed-support anisotropic-walk countermodel once")
    require(errors, global_text.count(fixed_support) == 1, "P22-F1 global entry must contain the fixed-support anisotropic-walk countermodel once")
    for path in root.rglob("*.md"):
        rel = path.relative_to(root)
        if ".git" in rel.parts or "_compiler/verification" in rel.as_posix() or rel.as_posix() in (LOCAL, GLOBAL):
            continue
        require(errors, fixed_support not in corpus_text(root, rel, overlay), f"P22-F1 fixed-support countermodel escaped local/global records: {rel}")

    source_guards = {
        "gravity-and-curvature.md": ("type: supporting", "status: shadow", "P22 governs every weak-field claim"),
        "gravity-asymmetry.md": ("**P22 supporting source.**", "scripts are absent"),
        "mathematization-F10-resolved.md": ("**P22 supporting source.**", "scripts are absent and were not rerun", "[reported check; scripts absent]"),
        "mathematization-F11.md": ("**P22/P23/P24 scope guard.**", "scripts are absent and were not rerun", "[reported check; script absent]"),
        "mathematization-F10-status.md": ("Status: **Superseded as current status; retained as adversarial evidence.**",),
    }
    for name, phrases in source_guards.items():
        text = corpus_text(root, name, overlay)
        for phrase in phrases:
            require(errors, phrase in text, f"{name} lacks authority guard: {phrase}")

    for script in ABSENT_REPORT_SCRIPTS:
        require(errors, not any(path.is_file() for path in root.rglob(script)), f"reported script unexpectedly exists without P22 source adjudication: {script}")

    active_files = (
        LOCAL, GLOBAL, "gravity-and-curvature.md", "gravity-asymmetry.md",
        "mathematization-F10-resolved.md", "mathematization-F11.md",
        "03-10-physics-concept-load-pass-ledger.md", "12-gravity-full-gr-imports.md",
        "12-gravity-full-gr-imports/12-gravity-full-gr-imports Readme.md",
        "physics-domain-work-plan.md", "physics-section-guide.md", "physics-source-map.md",
        "physics-registration-theorem.md", "physics-chemistry-gate-crossing.md",
        "supersession-map.md", "grqm-conflict-status.md", "grqm-problem-locator.md",
        "index.md", "overview/triadic-closure-reading-order.md",
    )
    combined = "\n".join(corpus_text(root, name, overlay) for name in active_files)
    required_guards = (
        "Registered at bounded static-model scope",
        "source/clock uniqueness",
        "common `3+1` implementation",
        "source normalization",
        "retained reports",
        "scripts are absent",
        "physical `rho` and `G` remain Open",
        "P23 owns stress-energy",
        "P24 owns",
    )
    for phrase in required_guards:
        require(errors, phrase in combined, f"P22 consumer guard missing: {phrase}")

    banned_active = (
        "F10 substantially closed for weak-field static regime",
        "Poisson's equation, the weak-field Einstein equation — holds, derived",
        "sign forced by atomicity, geodesic motion and tidal deviation verified",
        "scripts (run, outputs recorded above)",
        "weak-field gravity stands without the prior caveat",
        "Secured as reported finite-model evidence",
        "same modeled field as the F11 potential",
        "Phi=A/r+C",
        "Phi(r) = A / r + C",
        "The continuum step is still ahead (F10)",
        "F10 — still the open frontier",
        "gravity asymmetry** (dilation vs curvature",
    )
    for phrase in banned_active:
        require(errors, phrase not in combined, f"obsolete active P22 formulation remains: {phrase}")

    correction_requirements = {
        LOCAL: (
            "unequal weights alone do not alter reachable directions, null support, or metric structure",
            "Profile/weight-to-support or metric bridge",
            "Retained documentary report only",
            "delta d(r) = A / r + C_d",
            "Phi(r) = -delta d(r) / d_0 = -A / (d_0 r) + C_Phi",
            "nabla^2 Phi = +(4 pi A/d_0) delta^3(r)",
            "No repository evidence identifies them as one run",
        ),
        "mathematization-F11.md": (
            "delta d=A/r+C_d",
            "Phi(r) = -delta d(r)/d_0",
            "G M:=A/d_0",
            "distinct documentary report of unknown relationship",
        ),
        "gravity-asymmetry.md": (
            "does not logically alter their support",
            "R²=0.9993",
            "relationship to F11's separately described",
            "documentary evidence only",
        ),
        "mathematization-F9-done.md": ("P22 owns the later gravity status", "local weight law, not a metric/support theorem"),
        "physics-walk-D1-D5-consolidated.md": ("The gravity walk (P22 normalized)", "P22 gravity frontiers"),
    }
    for name, phrases in correction_requirements.items():
        text = corpus_text(root, name, overlay)
        for phrase in phrases:
            require(errors, phrase in text, f"{name} lacks frozen-correction element: {phrase}")

    for upstream in (
        "p19-native-electron-ruler-and-proton-electron-ratio.md",
        "p20-baryon-closure-and-proton-neutron-relation.md",
        "with-to-this-closure.md",
    ):
        require(errors, not git(root, "diff", "--name-only", f"{args.base}...HEAD", "--", upstream).strip(), f"P22 reopened protected upstream owner {upstream}")

    for downstream in ("stress-energy-three-offices.md", "lambda-derived.md"):
        require(errors, not git(root, "diff", "--name-only", f"{args.base}...HEAD", "--", downstream).strip(), f"P22 opened excluded downstream owner {downstream}")

    changed = changed_markdown(root, args.base)
    link_count = check_links(root, changed, errors)
    diff_check = subprocess.run(
        ["git", "diff", "--check", f"{args.base}...HEAD"], cwd=root,
        check=False, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    require(errors, diff_check.returncode == 0, "diff hygiene failed: " + (diff_check.stdout + diff_check.stderr).strip())

    print("P22 deterministic normalization verification")
    print(f"base: {args.base}")
    print(f"changed Markdown files checked: {len(changed)}")
    print(f"local Markdown links checked: {link_count}")
    print("frontier placement: canonical local + global summary only")
    print("P19/P20/P21 boundary: inherited, not reopened")
    print("P23/P24/P28 boundary: source owners not opened")
    print("retained computations: explicitly reported; named scripts absent")

    if errors:
        print(f"FAIL ({len(errors)} errors)")
        for error in errors:
            print(f"- {error}")
        return 1
    print("weak-field model: Registered at bounded selected static scope")
    print("source/clock uniqueness, common 3+1 implementation, source normalization, G: Open")
    print("diff hygiene: checked")
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
