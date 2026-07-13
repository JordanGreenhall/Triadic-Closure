#!/usr/bin/env python3
"""Final corpus reference pass after flattening the historical wiki.

This pass corrects two cases the first normalizer intentionally surfaced:
1. non-Markdown targets such as verify.py;
2. historical source paths whose basename is identical to the current document,
   which must not become circular self-citations.
It also adjudicates the small set of known renamed semantic targets.
"""

from __future__ import annotations

import os
import re
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_DIRS = {".git", "_site", "node_modules", ".venv", "venv"}
REPORT = ROOT / "reference-repair-report.md"


def allowed(path: Path) -> bool:
    rel = path.relative_to(ROOT)
    return not any(part in EXCLUDED_DIRS for part in rel.parts)


ALL_FILES = sorted(p for p in ROOT.rglob("*") if p.is_file() and allowed(p))
MD_FILES = sorted(p for p in ALL_FILES if p.suffix.lower() == ".md" and p != REPORT)
REL_SET = {p.relative_to(ROOT).as_posix() for p in ALL_FILES}
BY_NAME: dict[str, list[str]] = defaultdict(list)
BY_STEM: dict[str, list[str]] = defaultdict(list)
for rel in REL_SET:
    p = Path(rel)
    BY_NAME[p.name.casefold()].append(rel)
    BY_STEM[p.stem.casefold()].append(rel)

ALIASES = {
    "domain-entry-method": "entering-a-new-domain.md",
    "domain-entry-method.md": "entering-a-new-domain.md",
    "mass-derivation-three-faces": "epsilon-fw-bracket-result.md",
    "mass-derivation-three-faces.md": "epsilon-fw-bracket-result.md",
    "physics-source-map": "corpus-lineage.md",
    "physics-source-map.md": "corpus-lineage.md",
    "raw/package/verify.py": "verify.py",
}


def split_anchor(raw: str) -> tuple[str, str]:
    value = unquote(raw.strip()).replace("\\", "/")
    if "#" in value:
        target, anchor = value.split("#", 1)
        return target, anchor
    return value, ""


def resolve(raw: str, current: Path) -> str | None:
    target, _ = split_anchor(raw)
    target = target.removeprefix("./")
    if target in REL_SET:
        return target
    rel_current = current.relative_to(ROOT)
    candidate = (rel_current.parent / target).as_posix()
    if candidate in REL_SET:
        return candidate
    key = target.casefold()
    if key in ALIASES and ALIASES[key] in REL_SET:
        return ALIASES[key]
    name = Path(target).name.casefold()
    matches = BY_NAME.get(name, [])
    if len(matches) == 1:
        return matches[0]
    stem = Path(name).stem if "." in name else name
    matches = BY_STEM.get(stem, [])
    if len(matches) == 1:
        return matches[0]
    return None


def rel_link(target: str, current: Path) -> str:
    return Path(os.path.relpath(ROOT / target, current.parent)).as_posix()


def normalize_frontmatter(text: str, current: Path) -> str:
    if not text.startswith("---\n"):
        return text
    end = text.find("\n---\n", 4)
    if end < 0:
        return text
    lines = text[4:end].splitlines()
    body = text[end + 5 :]
    ordinary: list[str] = []
    source_values: list[str] = []
    historical_values: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        key = line.strip()
        if key in {"sources:", "historical_sources:"}:
            dest = source_values if key == "sources:" else historical_values
            i += 1
            while i < len(lines) and re.match(r"^\s+-\s+", lines[i]):
                dest.append(re.sub(r"^\s+-\s+", "", lines[i]).strip().strip('"\''))
                i += 1
            continue
        ordinary.append(line)
        i += 1

    current_rel = current.relative_to(ROOT).as_posix()
    live: list[str] = []
    historical: list[str] = []
    for value in source_values + historical_values:
        resolved = resolve(value, current)
        # A historical folder path collapsing onto the current file is
        # provenance, not a live source citation.
        if resolved and resolved != current_rel:
            live.append(rel_link(resolved, current))
        else:
            historical.append(value)

    # Remove exact duplicates while preserving order.
    live = list(dict.fromkeys(live))
    historical = list(dict.fromkeys(historical))
    out = ordinary
    if live:
        out.append("sources:")
        out.extend(f"  - {value}" for value in live)
    if historical:
        out.append("historical_sources:")
        out.extend(f"  - {value}" for value in historical)
    return "---\n" + "\n".join(out) + "\n---\n" + body


COMMENT = re.compile(r"(?P<label>[^\n]{0,120}?)<!-- unresolved historical reference: (?P<target>[^>]+) -->")
BACKTICK = re.compile(r"`(?P<target>(?:[^`\n]+/)+[^`\n]+\.(?:md|py|json|txt))`")


def normalize_body(text: str, current: Path) -> str:
    def comment_repl(match: re.Match[str]) -> str:
        target = match.group("target").strip()
        resolved = resolve(target, current)
        if not resolved:
            return match.group(0)
        label = match.group("label")
        # Capture only the final textual token used as the former wikilink label.
        token_match = re.search(r"([^,;:()\n]+)$", label)
        if not token_match:
            return match.group(0)
        token = token_match.group(1)
        prefix = label[: token_match.start(1)]
        return f"{prefix}[{token.strip()}]({rel_link(resolved, current)})"

    text = COMMENT.sub(comment_repl, text)

    def backtick_repl(match: re.Match[str]) -> str:
        target = match.group("target")
        resolved = resolve(target, current)
        if not resolved:
            return match.group(0)
        return f"`{rel_link(resolved, current)}`"

    return BACKTICK.sub(backtick_repl, text)


def unresolved_items() -> list[tuple[str, int, str]]:
    items: list[tuple[str, int, str]] = []
    for path in MD_FILES:
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for match in re.finditer(r"unresolved historical reference: ([^>]+)", line):
                items.append((path.relative_to(ROOT).as_posix(), number, match.group(1).strip()))
    return items


def main() -> None:
    changed: list[str] = []
    for path in MD_FILES:
        before = path.read_text(encoding="utf-8")
        after = normalize_frontmatter(before, path)
        after = normalize_body(after, path)
        if after != before:
            path.write_text(after, encoding="utf-8")
            changed.append(path.relative_to(ROOT).as_posix())

    unresolved = unresolved_items()
    report = [
        "# Reference Repair Report",
        "",
        "Final repository-tree reference audit.",
        "",
        f"- Markdown files scanned: **{len(MD_FILES)}**",
        f"- Files changed in final pass: **{len(changed)}**",
        f"- Remaining unresolved inline references: **{len(unresolved)}**",
        "",
        "## Files changed in final pass",
        "",
    ]
    report.extend(f"- [{name}]({name})" for name in changed)
    report.extend(["", "## Remaining unresolved inline references", ""])
    if unresolved:
        report.extend(["| File | Line | Reference |", "|---|---:|---|"])
        for name, line, target in unresolved:
            report.append(f"| [{name}]({name}) | {line} | `{target.replace('|', '\\|')}` |")
    else:
        report.append("None.")
    report.extend([
        "",
        "## Provenance rule",
        "",
        "Entries under `historical_sources:` identify source artifacts named by the former foldered wiki that are not independently present at a different path in this repository. They are retained as provenance labels, not live links. Live `sources:` entries resolve to actual repository files and never cite the containing document itself.",
        "",
    ])
    REPORT.write_text("\n".join(report), encoding="utf-8")
    print(f"Final pass changed {len(changed)} files; unresolved inline references: {len(unresolved)}")


if __name__ == "__main__":
    main()
