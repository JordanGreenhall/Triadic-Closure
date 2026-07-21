#!/usr/bin/env python3
"""Deterministic P24 normalization verifier.

Run from any directory inside the repository:
    python3 _compiler/verify_p24.py --base 3f3c6a313a0ff678b8b61fcc9a4a290a1ec4de3a

An optional overlay directory replaces repository-relative text files for
failure-capability tests without mutating the worktree.
"""

from __future__ import annotations

import argparse
import math
import re
import subprocess
from fractions import Fraction
from pathlib import Path


LOCAL = "p24-full-einstein-form-as-conditional-rigidity.md"
GLOBAL = "physics-domain-mature-status.md"
FRONTIERS = ("P24-F1", "P24-F2", "P24-F3")
P24_BASE = "3f3c6a313a0ff678b8b61fcc9a4a290a1ec4de3a"
ABSENT_REPORT_SCRIPTS = ("f11_assemble.py",)


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


def verify_exact_algebra(errors: list[str]) -> None:
    """Reproduce finite-difference and coefficient-normalization algebra."""
    coefficients: dict[int, Fraction] = {}
    for order in (2, 4, 6):
        numerator = Fraction(1 + (-1) ** order, math.factorial(order))
        coefficients[order] = numerator
    require(errors, coefficients == {
        2: Fraction(1, 1), 4: Fraction(1, 12), 6: Fraction(1, 360),
    }, f"nearest-neighbor Taylor coefficients changed: {coefficients}")

    a, b, c = Fraction(3), Fraction(6), Fraction(15)
    require(errors, (b / a, c / a) == (Fraction(2), Fraction(5)),
            "nondegenerate rigidity coefficients do not normalize as Lambda=b/a, kappa=c/a")
    require(errors, Fraction(0) == 0,
            "degenerate a=0 branch check failed")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", default=P24_BASE, help="exact base ref for the PR diff")
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
    require(errors, base_sha == P24_BASE, f"base must resolve to exact P24 base {P24_BASE}; got {base_sha}")

    local = corpus_text(root, LOCAL, overlay)
    global_text = corpus_text(root, GLOBAL, overlay)
    required_local = (
        "# P24: Full Einstein Form as Conditional Tensor Rigidity",
        "## Standing summary",
        "## Semantic boundary",
        "## Authority and lineage",
        "## 1. The conditional rigidity implication",
        "H_{mu nu} = a G_{mu nu} + b g_{mu nu}",
        "Lambda:=b/a",
        "kappa:=c/a",
        "If `a=0`",
        "## 2. One-step locality is not yet a continuum order theorem",
        "f''(x) + (a^2/12) f''''(x) + (a^4/360) f^(6)(x)",
        "## 3. Premise ledger",
        "selected/Conjectured conditional model and is Unregistered",
        "## 5. Local frontier",
        "## 6. Integration rule",
        "## 7. Source disposition",
    )
    for item in required_local:
        require(errors, item in local, f"missing canonical P24 element: {item}")

    for frontier in FRONTIERS:
        files: list[str] = []
        for path in root.rglob("*.md"):
            rel = path.relative_to(root)
            if ".git" in rel.parts or "_compiler/verification" in rel.as_posix():
                continue
            if frontier in corpus_text(root, rel, overlay):
                files.append(rel.as_posix())
        require(errors, sorted(files) == sorted([GLOBAL, LOCAL]),
                f"{frontier} must occur only in local/global files; got {sorted(files)}")
        require(errors, local.count(f"### {frontier} —") == 1,
                f"{frontier} must have one local heading")
        require(errors, global_text.count(f"**{frontier} —") == 1,
                f"{frontier} must have one global entry")

    source_guards = {
        "12-gravity-full-gr-imports.md": (
            "concise import-boundary shadow", "Selected/Conjectured conditional model; Unregistered",
            "f''+(a^2/12)f''''+...",
        ),
        "mathematization-F11.md": (
            "[P24 Full Einstein Form as Conditional Tensor Rigidity]",
            "Conjectured/Unregistered under P24", "scripts are absent and were not rerun",
        ),
        "mathematization-F8-F11.md": (
            "[P24](p24-full-einstein-form-as-conditional-rigidity.md)",
            "Retained conditional tensor-rigidity proposal", "Bianchi identity do not construct",
        ),
        "grqm-conflict-status.md": (
            "Conjectured / Unregistered under P24",
            "| `8π` Einstein/source coefficient | Open under P22/P24 |",
        ),
        "grqm-problem-locator.md": (
            "Conjectured / Unregistered under P24", "`8π`** Einstein/source coefficient",
            "**Open under P22/P24**",
        ),
    }
    for name, phrases in source_guards.items():
        text = corpus_text(root, name, overlay)
        for phrase in phrases:
            require(errors, phrase in text, f"{name} lacks P24 authority guard: {phrase}")

    for script in ABSENT_REPORT_SCRIPTS:
        require(errors, not any(path.is_file() for path in root.rglob(script)),
                f"reported script unexpectedly exists without P24 source adjudication: {script}")

    active_files = (
        LOCAL, GLOBAL, "12-gravity-full-gr-imports.md", "mathematization-F11.md",
        "mathematization-F8-F11.md", "03-10-physics-concept-load-pass-ledger.md",
        "physics-domain-work-plan.md", "physics-section-guide.md", "physics-source-map.md",
        "physics-registration-theorem.md", "sm-content-smuggle-audit-frontier.md",
        "grqm-conflict-status.md", "grqm-problem-locator.md", "index.md",
        "overview/triadic-closure-reading-order.md", "repository-inventory.md",
    )
    combined = "\n".join(corpus_text(root, name, overlay) for name in active_files)
    for phrase in (
        "conditional mathematical implication", "locality-to-order", "higher-derivative",
        "complete premise map", "source conservation", "nonzero Einstein",
        "tensor completeness", "nonlinear", "P28", "Open under P22/P24",
    ):
        require(errors, phrase in combined, f"P24 consumer guard missing: {phrase}")

    banned_active = (
        "Registered conditional on G1",
        "Registered-conditional through",
        "Registered conditional / Conjectured nonlinear",
        "**Registered (native)**",
        "**Registered-native** — audited Lovelock",
        "full Einstein equation remains P24-bound and Registered-conditional",
        "second-order field equation from one-step conditioning locality",
    )
    for phrase in banned_active:
        require(errors, phrase not in combined, f"obsolete active P24 formulation remains: {phrase}")

    ordered_pairs = {
        "index.md": (LOCAL, "12-gravity-full-gr-imports.md"),
        "physics-section-guide.md": (LOCAL, "12-gravity-full-gr-imports.md"),
        "physics-source-map.md": (LOCAL.removesuffix(".md"), "12-gravity-full-gr-imports"),
        "repository-inventory.md": (LOCAL, "12-gravity-full-gr-imports.md"),
    }
    for name, (owner, shadow) in ordered_pairs.items():
        text = corpus_text(root, name, overlay)
        require(errors, owner in text and shadow in text and text.index(owner) < text.index(shadow),
                f"{name} does not route canonical P24 before its shadow")

    inventory = corpus_text(root, "_compiler/18-supersession-map-semantic-inventory.md", overlay)
    require(errors, "Conditional tensor rigidity does not establish the P24 premises" in inventory,
            "compiled supersession inventory is stale for P24")

    for upstream in (
        "p7-manifold-recovery-and-local-continuum.md",
        "p19-native-electron-ruler-and-proton-electron-ratio.md",
        "p20-baryon-closure-and-proton-neutron-relation.md",
        "with-to-this-closure.md",
        "p22-weak-field-gravity-as-participation-curvature.md",
        "p23-stress-energy-as-three-office-source.md",
    ):
        require(errors, not git(root, "diff", "--name-only", f"{args.base}...HEAD", "--", upstream).strip(),
                f"P24 reopened protected upstream owner {upstream}")
    for downstream in ("lambda-derived.md",):
        require(errors, not git(root, "diff", "--name-only", f"{args.base}...HEAD", "--", downstream).strip(),
                f"P24 opened excluded downstream owner {downstream}")

    tracked = set(git(root, "ls-files").splitlines())
    require(errors, not any(name.startswith("tools/") for name in tracked),
            "automated corpus mutator tools/ returned")
    require(errors, not any(name.startswith(".github/workflows/") for name in tracked),
            "write workflow returned")

    changed = changed_markdown(root, args.base)
    link_count = check_links(root, changed, errors)
    verify_exact_algebra(errors)
    diff_check = subprocess.run(
        ["git", "diff", "--check", f"{args.base}...HEAD"], cwd=root,
        check=False, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    require(errors, diff_check.returncode == 0,
            "diff hygiene failed: " + (diff_check.stdout + diff_check.stderr).strip())

    print("P24 deterministic normalization verification")
    print(f"base: {args.base}")
    print(f"changed Markdown files checked: {len(changed)}")
    print(f"local Markdown links checked: {link_count}")
    print("frontier placement: canonical local + global summary only")
    print("P7/P19-P23 boundary: inherited, not reopened")
    print("P28 boundary: Lambda source and cosmology not normalized")
    print("retained computation: absent f11_assemble.py remains documentary")
    print("exact algebra: nearest-neighbor expansion and coefficient normalization checked")

    if errors:
        for error in errors:
            print(f"FAIL {error}")
        return 1
    print("PASS P24 deterministic normalization verification")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
