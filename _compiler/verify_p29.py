#!/usr/bin/env python3
"""Deterministic verifier for normalization unit P29."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
BASE = "e017d0876126a3f44d9e16dfe28bca4994b8dd6f"
OWNER = "p29-standard-model-completion-electroweak-breaking-generations-and-spectrum.md"
STATUS = "physics-domain-mature-status.md"
LEDGER = "03-10-physics-concept-load-pass-ledger.md"
SHADOW = "13-higgs-yukawa-electroweak-generations-spectrum-quarantine/13-higgs-yukawa-electroweak-generations-spectrum-quarantine Readme.md"
SIMULATE: str | None = None


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True)


def fail(message: str) -> None:
    raise AssertionError(message)


def original(path: str) -> str:
    return (ROOT / path).read_text()


def substitute_once(text: str, old: str, new: str, label: str) -> str:
    if text.count(old) != 1:
        fail(f"simulation {label}: expected one exact mutation target, got {text.count(old)}")
    return text.replace(old, new, 1)


def text(path: str) -> str:
    value = original(path)
    if path == OWNER:
        mutations = {
            "owner-module": ("the exact chiral matter module and one-generation content are **Open and Unregistered**", "the exact chiral matter module and one-generation content are **Registered**"),
            "owner-higgs": ("a framework Higgs object, representation, potential, vacuum/ground selection, breaking scale, Yukawa map, Yukawa couplings, and resulting mass mechanism are **Open and Unregistered**", "a framework Higgs object, representation, potential, vacuum/ground selection, breaking scale, Yukawa map, Yukawa couplings, and resulting mass mechanism are **Registered**"),
            "owner-generations": ("generation count is **Open and Unregistered**", "generation count is **Registered**"),
            "owner-spectrum": ("a framework numerical particle spectrum is **Open and Unregistered**", "a framework numerical particle spectrum is **Registered**"),
            "owner-triad": ("the primitive triad does not entail three generations", "the primitive triad entails three generations"),
            "frontier-f1": ("### P29-F1 — exact electroweak module, breaking, and residual sectors", "### removed frontier one"),
            "frontier-f2": ("### P29-F2 — Higgs/Yukawa construction and mass-mechanism bridge", "### removed frontier two"),
            "frontier-f3": ("### P29-F3 — generation multiplicity and numerical particle spectrum", "### removed frontier three"),
        }
        if SIMULATE in mutations:
            old, new = mutations[SIMULATE]
            value = substitute_once(value, old, new, SIMULATE)
    elif path == STATUS and SIMULATE == "status-overgrade":
        value = substitute_once(
            value,
            "| P29 generations and numerical particle spectrum | Open; mass-Casimir route candidate/Unexecuted | Unregistered |",
            "| P29 generations and numerical particle spectrum | Registered | Registered |",
            SIMULATE,
        )
    elif path == LEDGER and SIMULATE == "ledger-overgrade":
        value = substitute_once(
            value,
            "generation count and complete/numerical spectrum are **Open and Unregistered**; the candidate route is **Unexecuted and Unregistered**",
            "generation count and complete/numerical spectrum are **Registered**; the candidate route is **Executed and Registered**",
            SIMULATE,
        )
    elif path == SHADOW and SIMULATE == "shadow-route":
        value = substitute_once(
            value,
            "[P29](../p29-standard-model-completion-electroweak-breaking-generations-and-spectrum.md)",
            "P29",
            SIMULATE,
        )
    return value


def require(haystack: str, needle: str, label: str) -> None:
    if needle not in haystack:
        fail(f"{label}: missing {needle!r}")


def section(value: str, start: str, end: str | None = None) -> str:
    if start not in value:
        fail(f"missing section start {start!r}")
    out = value.split(start, 1)[1]
    if end is not None:
        if end not in out:
            fail(f"missing section end {end!r}")
        out = out.split(end, 1)[0]
    return out


def check_owner() -> None:
    owner = text(OWNER)
    summary = section(owner, "## Standing summary", "## Semantic and unit boundary")
    for claim in (
        "the exact chiral matter module and one-generation content are **Open and Unregistered**",
        "exact hypercharge assignments, anomaly cancellation, center quotient, electric-charge lattice, electroweak breaking, photon/W/Z identities, and mixing are **Open and Unregistered**",
        "a framework Higgs object, representation, potential, vacuum/ground selection, breaking scale, Yukawa map, Yukawa couplings, and resulting mass mechanism are **Open and Unregistered**",
        "generation count is **Open and Unregistered**",
        "the primitive triad does not entail three generations",
        "D5 mass-Casimir-over-D4-charge-profile route is **candidate, Unexecuted, and Unregistered**",
        "a framework numerical particle spectrum is **Open and Unregistered**",
        "measured values remain empirical inputs or comparison targets",
    ):
        require(summary, claim, "canonical standing summary")

    gen = section(owner, "## Generations adjudication", "## Numerical spectrum adjudication")
    for claim in (
        "one, two, three, four, or another finite number of repeated modules",
        "mass-Casimir operator",
        "multiplicity means generation rather than another degeneracy",
        "executable reproducer",
    ):
        require(gen, claim, "generation adjudication")

    for frontier, next_frontier in (
        ("P29-F1", "### P29-F2"),
        ("P29-F2", "### P29-F3"),
        ("P29-F3", "## Integration rule"),
    ):
        starts = [line for line in owner.splitlines() if line.startswith(f"### {frontier}")]
        if len(starts) != 1:
            fail(f"{frontier}: expected one canonical local frontier, got {len(starts)}")
        start = starts[0]
        block = section(owner, start, next_frontier)
        for field in (
            "**Standing:**",
            "**Current strongest achieved result:**",
            "**Missing:**",
            "**Dependencies and downstream claims affected:**",
            "**False-completion warning:**",
            "**Local owner:** this P29 page.",
            "**Next legitimate research action:**",
        ):
            require(block, field, frontier)


def check_consumers() -> None:
    status = text(STATUS)
    for row in (
        "| P29 exact electroweak module, breaking, and residual sectors | Open | Unregistered |",
        "| P29 Higgs/Yukawa construction and mass mechanism | Open | Unregistered |",
        "| P29 generations and numerical particle spectrum | Open; mass-Casimir route candidate/Unexecuted | Unregistered |",
    ):
        require(status, row, "mature status")
    for frontier in ("P29-F1", "P29-F2", "P29-F3"):
        require(status, frontier, "mature frontier")
        lines = [line for line in status.splitlines() if re.match(rf"\d+\. \*\*{frontier} —", line)]
        if len(lines) != 1:
            fail(f"mature {frontier}: expected one frontier line, got {len(lines)}")
        for field in (
            "**Standing:**", "**Current strongest achieved result:**", "**Missing:**",
            "**Dependencies and downstream claims affected:**", "**False-completion warning:**",
            "**Local owner:**", "**Next legitimate research action:**",
        ):
            require(lines[0], field, f"mature {frontier}")

    ledger = text(LEDGER)
    item = section(ledger, "## Item 13 — Standard Model completion quarantine", "## Loop-agent output contract")
    for phrase in (
        "PASSES only as an authority-bounded quarantine adjudication",
        "Open and Unregistered",
        "Unexecuted and Unregistered",
        "No consumer may infer electroweak completion, Higgs/Yukawa mass generation, three generations, or numerical spectrum",
    ):
        require(item, phrase, "Item 13 ledger")

    shadow = text(SHADOW)
    route = "[P29](../p29-standard-model-completion-electroweak-breaking-generations-and-spectrum.md)"
    require(shadow, route, "Item 13 shadow route")
    require(shadow, "PASS is achieved as an authority-bounded quarantine under P29", "Item 13 shadow grade")
    if shadow.index("p29-standard-model-completion") > shadow.index("gauge-structure-result"):
        fail("Item 13 shadow does not route canonical P29 before legacy sources")

    requirements = {
        "sm-content-smuggle-audit-frontier.md": (
            "Registers the quarantine adjudication only",
            "Exact electroweak module/breaking, Higgs/Yukawa construction, generation count, and complete/numerical spectrum are Open and Unregistered",
        ),
        "physics-domain-work-plan.md": (
            "mass-Casimir spectral-multiplicity-over-D4-charge-profile route is candidate, Unexecuted, and Unregistered",
            "exact P29 content Open and Unregistered",
        ),
        "supersession-map.md": (
            "### P29 Standard Model-completion standing",
            "Registers only the authority-bounded quarantine",
        ),
        "Frontier Close Loop Execution Readme.md": (
            "PASS only as a P29 authority-bounded quarantine",
        ),
        "physics-chemistry-gate-crossing.md": (
            "that route is Unexecuted and Unregistered and does not presently determine generation count",
        ),
        "deferred-articulations-map.md": (
            "P29 keeps the complete/numerical particle spectrum Open and Unregistered",
        ),
        "physics-registration-theorem.md": (
            "[P29 / Item 13](p29-standard-model-completion-electroweak-breaking-generations-and-spectrum.md)",
        ),
        "index.md": (
            "[P29 Standard Model Completion, Electroweak Breaking, Generations, and Spectrum](p29-standard-model-completion-electroweak-breaking-generations-and-spectrum.md)",
        ),
    }
    for path, phrases in requirements.items():
        value = text(path)
        for phrase in phrases:
            require(value, phrase, f"P29 consumer {path}")


def check_frontier_placement() -> None:
    files = [
        str(path.relative_to(ROOT))
        for path in ROOT.rglob("*.md")
        if ".git" not in path.parts and path.relative_to(ROOT).parts[0] != "_compiler"
    ]
    expected = {OWNER, STATUS}
    for frontier in ("P29-F1", "P29-F2", "P29-F3"):
        living = {path for path in files if frontier in original(path)}
        if living != expected:
            fail(f"{frontier} placement {sorted(living)} != {sorted(expected)}")


def check_protected_owners(base: str) -> None:
    protected = (
        "same-kind-carrier-representation-theorem.md",
        "gauge-structure-result.md",
        "p10-color-singlet-and-representation-consequences.md",
        "p11-gauge-sources-beyond-color.md",
        "p12-spin-helicity-handedness-and-chiral-coupling.md",
        "p13-particle-identity-and-native-role-taxonomy.md",
        "p14-flavor-and-mark-geometry.md",
        "p15-charge-hypercharge-valence-and-center-locking.md",
        "p16-quantitative-qcd-dynamics-and-quarantine.md",
        "p17-mass-as-closure-maintenance.md",
        "p18-closure-inherited-metric-and-2pi5-measure.md",
        "p19-native-electron-ruler-and-proton-electron-ratio.md",
        "p20-baryon-closure-and-proton-neutron-relation.md",
        "with-to-this-closure.md",
        "p22-weak-field-gravity-as-participation-curvature.md",
        "p23-stress-energy-as-three-office-source.md",
        "p24-full-einstein-form-as-conditional-rigidity.md",
        "p25-grqm-background-conflict-and-nonrenormalizability.md",
        "p26-matter-sourced-geometry-holonomy-and-bmv.md",
        "p27-horizon-area-entropy-temperature-and-information.md",
        "p28-lambda-cosmological-closure-magnitude-and-dynamics.md",
    )
    changed = set(git("diff", "--name-only", base, "--", *protected).splitlines())
    if changed:
        fail(f"prior canonical owners changed: {sorted(changed)}")


def check_mutators() -> None:
    code_paths = git("ls-files", "*.py", "*.sh", "*.yml", "*.yaml", "*.json").splitlines()
    refs = []
    for path in code_paths:
        if path == "_compiler/verify_p29.py":
            continue
        try:
            value = original(path)
        except UnicodeDecodeError:
            continue
        if OWNER in value:
            refs.append(path)
    if refs:
        fail(f"unadjudicated non-Markdown P29 mutator/source references: {refs}")


def count_changed_markdown_links(base: str) -> tuple[int, int, int]:
    changed = git("diff", "--name-only", base).splitlines()
    markdown = [path for path in changed if path.endswith(".md") and (ROOT / path).exists()]
    pattern = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
    links = 0
    for path in markdown:
        for raw in pattern.findall(original(path)):
            target = raw.strip().strip("<>")
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            links += 1
            dest = unquote(target.split("#", 1)[0])
            if dest and not ((ROOT / path).parent / dest).resolve().exists():
                fail(f"broken changed-file link: {path} -> {target}")
    return len(changed), len(markdown), links


def verify(base: str) -> None:
    try:
        subprocess.run(["git", "cat-file", "-e", f"{base}^{{commit}}"], cwd=ROOT, check=True, capture_output=True)
    except subprocess.CalledProcessError:
        fail(f"base commit unavailable: {base}")
    if base != BASE:
        fail(f"wrong P29 base {base}; expected {BASE}")

    check_owner()
    check_consumers()
    check_frontier_placement()
    check_protected_owners(base)
    check_mutators()
    changed, markdown, links = count_changed_markdown_links(base)
    print(f"P29 verification: PASS (base {base}; {changed} changed files; {markdown} changed Markdown files; {links} Markdown links scanned)")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", default=BASE)
    parser.add_argument("--simulate", choices=(
        "owner-module", "owner-higgs", "owner-generations", "owner-spectrum", "owner-triad",
        "frontier-f1", "frontier-f2", "frontier-f3", "status-overgrade", "ledger-overgrade", "shadow-route",
    ))
    args = parser.parse_args()
    global SIMULATE
    SIMULATE = args.simulate
    try:
        verify(args.base)
    except (AssertionError, OSError, subprocess.CalledProcessError, StopIteration) as exc:
        print(f"P29 verification: FAIL: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
