#!/usr/bin/env python3
"""Deterministic verifier for normalization unit P28.

An optional overlay directory replaces repository-relative text files for
failure-capability tests without changing the worktree.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path
from typing import NoReturn

ROOT = Path(__file__).resolve().parents[1]
OWNER = "p28-lambda-cosmological-closure-magnitude-and-dynamics.md"
GLOBAL = "physics-domain-mature-status.md"
BASE = "92b194970a7fa00f516e759eaeb3e4d3d38aad03"
SIMULATE: str | None = None


def fail(message: str) -> NoReturn:
    print(f"P28 verification: FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def git(*args: str) -> str:
    try:
        return subprocess.check_output(
            ["git", *args], cwd=ROOT, text=True, stderr=subprocess.STDOUT
        ).strip()
    except subprocess.CalledProcessError as exc:
        fail(f"git {' '.join(args)} failed: {exc.output.strip()}")


def corpus_text(relative: str, overlay: Path | None) -> str:
    path = Path(relative)
    if overlay is not None and (overlay / path).is_file():
        text = (overlay / path).read_text(encoding="utf-8")
        return simulated_text(relative, text)
    full = ROOT / path
    if not full.is_file():
        fail(f"required file absent: {relative}")
    return simulated_text(relative, full.read_text(encoding="utf-8"))


def simulated_text(relative: str, text: str) -> str:
    if SIMULATE is not None and SIMULATE.startswith("downstream-"):
        stale = {
            "downstream-imports": ("12-gravity-full-gr-imports.md", "| `Λ` structural meaning: stress-energy of self-closure, `w = -1` | **Registered** | Magnitude advanced by grqm-conflict-status: scaling Registered; native complete `3 R_H^-2` Conjectured-strong; present value `Λ_present = 3 f_reflexive R_H^-2` with empirical note `f_reflexive ≈ Ω_DE ≈ 0.685`; dynamics Open. |"),
            "downstream-ledger": ("03-10-physics-concept-load-pass-ledger.md", "- **`Λ` structural meaning:** stress-energy of self-closure, `w=-1` — **Registered**; scaling `Λ ∼ R_H^-2` **Registered**; native complete `3 R_H^-2` **Conjectured-strong**; present value `Λ_present = 3 f_reflexive R_H^-2` with empirical note `f_reflexive ≈ Ω_DE ≈ 0.685`; dynamics Open."),
            "downstream-smuggle": ("sm-content-smuggle-audit-frontier.md", "Lambda structural meaning and scaling are Registered; native complete `3 R_H^-2` is Conjectured-strong; present `Λ_present = 3 f_reflexive R_H^-2` with empirical note `f_reflexive ≈ Ω_DE ≈ 0.685`; Lambda dynamics remain Open."),
            "downstream-deferred": ("deferred-articulations-map.md", "Every quantitative claim that has had to be retracted (the Λ magnitude, Σ|h|² for the holding, the coupling constants) came from deferred articulation."),
        }
        stale_path, stale_text = stale[SIMULATE]
        return stale_text if relative == stale_path else text
    if relative != OWNER or SIMULATE is None:
        return text
    if SIMULATE == "frontier":
        return text.replace("P28-F3", "P28-FX")
    injections = {
        "confirmation": "\npresent value is predicted\n",
        "coefficient": "\ncoefficient `3` is Registered\n",
        "dynamics": "\nnative expansion dynamics are Registered\n",
        "flatness": "\nbackground flatness is Registered\n",
        "boundary": "\nP29 Standard Model completion has begun\n",
    }
    return text + injections[SIMULATE]


def require(text: str, needle: str, where: str) -> None:
    if needle not in text:
        fail(f"{where} lacks required text: {needle}")


def forbid(text: str, needle: str, where: str) -> None:
    if needle in text:
        fail(f"{where} retains forbidden text: {needle}")


def main() -> None:
    global SIMULATE
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", required=True)
    parser.add_argument("--overlay", type=Path, help="temporary semantic-check overlay")
    parser.add_argument(
        "--simulate",
        choices=(
            "confirmation", "coefficient", "dynamics", "flatness", "frontier", "boundary",
            "downstream-imports", "downstream-ledger", "downstream-smuggle", "downstream-deferred",
        ),
        help="in-memory stale-state mutation for rejection-capability tests",
    )
    args = parser.parse_args()
    if args.base != BASE:
        fail(f"base must be exact merged P27 head {BASE}, got {args.base}")
    git("cat-file", "-e", f"{args.base}^{{commit}}")
    overlay = args.overlay.resolve() if args.overlay else None
    SIMULATE = args.simulate

    changed = set(git("diff", "--name-only", f"{args.base}...HEAD").splitlines())
    working_changed = set(git("diff", "--name-only").splitlines())
    working_changed.update(git("diff", "--cached", "--name-only").splitlines())
    working_changed.update(git("ls-files", "--others", "--exclude-standard").splitlines())
    all_changed = changed | working_changed
    required_paths = {
        OWNER,
        GLOBAL,
        "lambda-derived.md",
        "lambda-scaling-validation-task.md",
        "grqm-conflict-status.md",
        "grqm-problem-locator.md",
        "_compiler/verify_p28.py",
        "_compiler/verify_p28_algebra.py",
        "_compiler/verification/p28-unit-opening.md",
        "_compiler/verification/p28-exact-finite-algebra.txt",
    }
    missing = required_paths - all_changed
    if missing:
        fail(f"required changed paths absent: {sorted(missing)}")
    forbidden = {
        "p17-mass-as-closure-maintenance.md",
        "p22-weak-field-gravity-as-participation-curvature.md",
        "p23-stress-energy-as-three-office-source.md",
        "p24-full-einstein-form-as-conditional-rigidity.md",
        "p25-grqm-background-conflict-and-nonrenormalizability.md",
        "p26-matter-sourced-geometry-holonomy-and-bmv.md",
        "p27-horizon-area-entropy-temperature-and-information.md",
    }
    for path in all_changed:
        if path in forbidden or path.startswith("p29-"):
            fail(f"neighbor or later-unit owner changed in P28: {path}")

    owner = corpus_text(OWNER, overlay)
    for needle in (
        "framework meaning, tensor form, positive sign, and `w=-1` structure are **Registered**",
        "`Lambda ~ R_H^-2` remains **Registered**",
        "**Conjectured-strong and Unregistered as a completed coefficient derivation**",
        "is an **exact definitional identity**",
        "not an independent prediction, fit, or empirical confirmation",
        "**Conjectured-strong translation with empirical state input**",
        "**Conjectured-strong and Unregistered as a completed dissolution**",
        "**Open and Unregistered**",
        "**Conjectured conditional framework claim and Unregistered**",
        "P28-F1",
        "P28-F2",
        "P28-F3",
        "Dimensional scaling leaves",
        "masquerading as confirmation",
        "P29 Standard Model completion",
    ):
        require(owner, needle, OWNER)
    for stale in (
        "three independent measurements satisfy",
        "present value is predicted",
        "coefficient `3` is Registered",
        "native expansion dynamics are Registered",
        "background flatness is Registered",
        "problem is dissolved as a completed Registered result",
        "P29 Standard Model completion has begun",
    ):
        forbid(owner, stale, OWNER)

    for shadow in ("lambda-derived.md", "grqm-conflict-status.md", "grqm-problem-locator.md"):
        text = corpus_text(shadow, overlay)
        require(text, OWNER, shadow)
        require(text, "Registered", shadow)
        require(text, "Conjectured-strong", shadow)
        require(text, "definitional", shadow)
        require(text, "Open", shadow)
        require(text, "Unregistered", shadow)
    status = corpus_text("grqm-conflict-status.md", overlay)
    locator = corpus_text("grqm-problem-locator.md", overlay)
    for stale in (
        "three independent measurements satisfy it",
        "present value `Λ = 3 Ω_Λ R_H⁻²` is Conjectured-strong",
    ):
        forbid(status, stale, "grqm-conflict-status.md")
        forbid(locator, stale, "grqm-problem-locator.md")

    global_text = corpus_text(GLOBAL, overlay)
    for field in ("P28-F1", "P28-F2", "P28-F3"):
        require(global_text, field, GLOBAL)
        require(owner, field, OWNER)
        living = []
        for path in ROOT.rglob("*.md"):
            rel = path.relative_to(ROOT).as_posix()
            if rel.startswith((".git/", "_compiler/verification/")):
                continue
            text = corpus_text(rel, overlay)
            if field in text:
                living.append(rel)
        if sorted(living) != sorted([OWNER, GLOBAL]):
            fail(f"{field} living placement is {sorted(living)}")

    for route in (
        "index.md",
        "physics-section-guide.md",
        "physics-source-map.md",
        "repository-inventory.md",
        "overview/triadic-closure-reading-order.md",
        "physics-domain-work-plan.md",
        "physics-registration-theorem.md",
        "supersession-map.md",
        "sm-content-smuggle-audit-frontier.md",
    ):
        require(corpus_text(route, overlay), OWNER, route)

    downstream_consumers = (
        "12-gravity-full-gr-imports.md",
        "03-10-physics-concept-load-pass-ledger.md",
        "sm-content-smuggle-audit-frontier.md",
    )
    downstream_requirements = (
        OWNER,
        "Registered at structural scope",
        "Registered at macro-scaling scope",
        "Conjectured-strong and Unregistered",
        "definitional identity",
        "not empirical confirmation",
        "empirical input",
        "Open and Unregistered",
    )
    for consumer in downstream_consumers:
        text = corpus_text(consumer, overlay)
        for needle in downstream_requirements:
            require(text, needle, consumer)
        forbid(text, "`Λ_present = 3 f_reflexive R_H^-2` with empirical note", consumer)

    deferred = corpus_text("deferred-articulations-map.md", overlay)
    for needle in (
        OWNER,
        "unsupported exact/numerical Lambda coefficient",
        "confirmatory present-magnitude language",
        "stronger dynamical claims",
        "Registered macro `Lambda ~ R_H^-2` scaling",
        "separately grades the coefficient, empirical translation, and dynamics",
    ):
        require(deferred, needle, "deferred-articulations-map.md")
    forbid(deferred, "(the Λ magnitude,", "deferred-articulations-map.md")

    # Every declared canonical source must resolve to a tracked file.
    in_frontmatter = False
    for line in owner.splitlines():
        if line == "---":
            in_frontmatter = not in_frontmatter
            continue
        if in_frontmatter and line.startswith("  - "):
            source = line[4:]
            if not (ROOT / source).is_file() or source not in git("ls-files", source).splitlines():
                fail(f"owner source is not a tracked file: {source}")

    task = corpus_text("lambda-scaling-validation-task.md", overlay)
    require(task, "Open / Unexecuted", "lambda-scaling-validation-task.md")
    require(task, "not a result report", "lambda-scaling-validation-task.md")

    algebra_evidence = corpus_text("_compiler/verification/p28-exact-finite-algebra.txt", overlay)
    for result in (
        "spatial_dimension=3 unordered_two_planes=3",
        "reconstructed_Lambda=7",
        "scaling_countermodel_alpha=7/2",
        "unsourced_background_excluded=true",
        "P28 exact finite algebra: PASS",
    ):
        require(algebra_evidence, result, "p28-exact-finite-algebra.txt")
    algebra_run = subprocess.run(
        [sys.executable, str(ROOT / "_compiler/verify_p28_algebra.py")],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    if algebra_run.returncode != 0:
        fail(f"P28 algebra reproducer failed: {algebra_run.stderr.strip()}")
    if algebra_run.stdout != algebra_evidence:
        fail("P28 algebra output is not byte-identical to committed evidence")

    for path in (
        "_compiler/verification/p28-failure-confirmation.txt",
        "_compiler/verification/p28-failure-coefficient.txt",
        "_compiler/verification/p28-failure-dynamics.txt",
        "_compiler/verification/p28-failure-flatness.txt",
        "_compiler/verification/p28-failure-frontier.txt",
        "_compiler/verification/p28-failure-boundary.txt",
        "_compiler/verification/p28-failure-downstream.txt",
    ):
        require(corpus_text(path, overlay), "Result: REJECTED", path)

    markdown_changed = [p for p in all_changed if p.endswith(".md")]
    links = sum(corpus_text(path, overlay).count("](") for path in markdown_changed)
    print(
        "P28 verification: PASS "
        f"(base {BASE}; {len(all_changed)} changed files; "
        f"{len(markdown_changed)} changed Markdown files; {links} Markdown links scanned)"
    )


if __name__ == "__main__":
    main()
