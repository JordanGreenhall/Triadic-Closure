#!/usr/bin/env python3
"""Deterministic P23 normalization verifier.

Run from any directory inside the repository:
    python3 _compiler/verify_p23.py --base 76207d7a2891f68a1d825ac19864e6d88a0dba80

An optional overlay directory replaces repository-relative text files for
failure-capability tests without mutating the worktree.
"""

from __future__ import annotations

import argparse
import re
import subprocess
from pathlib import Path


LOCAL = "p23-stress-energy-as-three-office-source.md"
GLOBAL = "physics-domain-mature-status.md"
FRONTIERS = ("P23-F1", "P23-F2", "P23-F3")
P23_BASE = "76207d7a2891f68a1d825ac19864e6d88a0dba80"
ABSENT_REPORT_SCRIPTS = ("t_structure.py", "t_full.py", "t_converge.py")


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
    parser.add_argument("--base", default=P23_BASE, help="exact base ref for the PR diff")
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
    require(errors, base_sha == P23_BASE, f"base must resolve to exact P23 base {P23_BASE}; got {base_sha}")

    local = corpus_text(root, LOCAL, overlay)
    global_text = corpus_text(root, GLOBAL, overlay)
    required_local = (
        "# P23 — Stress-Energy as a Three-Office Source",
        "## Bounded verdict",
        "## Semantic boundary",
        "## Authority and lineage",
        "## 1. Conditional second-moment source",
        "## 2. Observer-relative three-sector decomposition",
        "## 3. Exact conditional population example",
        "## 4. Conservation is a separate dynamical condition",
        "## 5. Evidence and absent computations",
        "## 6. Claim and warrant ledger",
        "## 7. Local frontier",
        "## 8. Integration rules",
        "## 9. Source disposition",
        "Sum_a w_a V_a^mu V_a^nu != rho V^mu V^nu",
        "1 + 3 + 6 = 10",
        "T^{0n} = w_+ - w_-",
        "scalar continuity by itself does not imply tensor conservation",
        "documentary source claims only",
        "status: current",
    )
    for item in required_local:
        require(errors, item in local, f"missing canonical P23 element: {item}")

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

    source_guards = {
        "stress-energy-three-offices.md": (
            "concise result shadow for [P23", "exact This/From/With correspondence **Conjectured / Unregistered**",
            "scalar continuity alone does not prove",
        ),
        "mathematization-F11.md": (
            "[P23 Stress-Energy as a Three-Office Source]", "scripts are absent and were not rerun",
            "A general multi-stream sum is **not** equal", "Scalar continuity alone is insufficient",
        ),
        "mathematization-F8-F11.md": (
            "**P22/P23/P24 authority guard.**", "generic conservation language does not by itself prove",
        ),
    }
    for name, phrases in source_guards.items():
        text = corpus_text(root, name, overlay)
        for phrase in phrases:
            require(errors, phrase in text, f"{name} lacks P23 authority guard: {phrase}")

    for script in ABSENT_REPORT_SCRIPTS:
        require(errors, not any(path.is_file() for path in root.rglob(script)), f"reported script unexpectedly exists without P23 source adjudication: {script}")

    active_files = (
        LOCAL, GLOBAL, "stress-energy-three-offices.md", "mathematization-F11.md",
        "03-10-physics-concept-load-pass-ledger.md", "12-gravity-full-gr-imports.md",
        "physics-domain-work-plan.md", "physics-section-guide.md", "physics-source-map.md",
        "physics-registration-theorem.md", "sm-content-smuggle-audit-frontier.md",
        "p22-weak-field-gravity-as-participation-curvature.md", "gravity-and-curvature.md",
        "grqm-conflict-status.md", "grqm-problem-locator.md", "index.md",
        "overview/triadic-closure-reading-order.md",
    )
    combined = "\n".join(corpus_text(root, name, overlay) for name in active_files)
    required_guards = (
        "symmetric second-moment",
        "observer-relative",
        "real source weights",
        "scalar continuity alone",
        "general stress",
        "office map is Conjectured/Unregistered",
        "P24",
        "source normalization",
    )
    for phrase in required_guards:
        require(errors, phrase in combined, f"P23 consumer guard missing: {phrase}")

    banned_active = (
        "three independent covariant signature classes",
        "With-mode remains the unproven gate",
        "With-mode unproven",
        "premise (1) closed",
        "T^{μν}(x) = Σ_k a_k V_k^μ V_k^ν = ρ V^μ V^ν",
        "So the framework **produces** a symmetric, conserved, rank-2 source",
        "continuum conservation is exact",
        "Stress-energy claims await P23 normalization",
        "bounded This/From/With alignment is **Registered representationally**",
        "three-office correspondence is Registered",
    )
    for phrase in banned_active:
        require(errors, phrase not in combined, f"obsolete active P23 formulation remains: {phrase}")

    for upstream in (
        "p19-native-electron-ruler-and-proton-electron-ratio.md",
        "p20-baryon-closure-and-proton-neutron-relation.md",
        "with-to-this-closure.md",
    ):
        require(errors, not git(root, "diff", "--name-only", f"{args.base}...HEAD", "--", upstream).strip(), f"P23 reopened protected upstream owner {upstream}")

    for downstream in ("lambda-derived.md",):
        require(errors, not git(root, "diff", "--name-only", f"{args.base}...HEAD", "--", downstream).strip(), f"P23 opened excluded downstream owner {downstream}")

    tracked = set(git(root, "ls-files").splitlines())
    require(errors, not any(name.startswith("tools/") for name in tracked), "automated corpus mutator tools/ returned")
    require(errors, not any(name.startswith(".github/workflows/") for name in tracked), "write workflow returned")

    changed = changed_markdown(root, args.base)
    link_count = check_links(root, changed, errors)
    diff_check = subprocess.run(
        ["git", "diff", "--check", f"{args.base}...HEAD"], cwd=root,
        check=False, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    require(errors, diff_check.returncode == 0, "diff hygiene failed: " + (diff_check.stdout + diff_check.stderr).strip())

    print("P23 deterministic normalization verification")
    print(f"base: {args.base}")
    print(f"changed Markdown files checked: {len(changed)}")
    print(f"local Markdown links checked: {link_count}")
    print("frontier placement: canonical local + global summary only")
    print("P19/P20/P21 boundary: inherited, not reopened")
    print("P22 boundary: source normalization and G remain P22-owned")
    print("P24/P28 boundary: field equation and Lambda not normalized")
    print("retained computations: exact algebra separated from absent-script reports")

    if errors:
        for error in errors:
            print(f"FAIL {error}")
        return 1
    print("PASS P23 deterministic normalization verification")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
