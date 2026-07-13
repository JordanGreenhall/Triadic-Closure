#!/usr/bin/env python3
"""Normalize internal Markdown references against the repository's actual tree.

The repository was uploaded from a foldered wiki into a largely flat GitHub tree.
This tool repairs:
  * YAML frontmatter `sources:` entries;
  * Obsidian wikilinks;
  * relative Markdown links;
  * backticked historical file paths when their basename exists in the repo.

Missing source-provenance entries are moved from `sources:` to
`historical_sources:` so live source lists contain only resolvable repository
files. Unresolved wikilinks are retained as readable text plus an HTML comment,
and are recorded in a generated report for human adjudication.
"""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "reference-repair-report.md"
EXCLUDED_DIRS = {".git", "_site", "node_modules", ".venv", "venv"}
EXCLUDED_FILES = {REPORT.name}


def markdown_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*.md"):
        rel = path.relative_to(ROOT)
        if any(part in EXCLUDED_DIRS for part in rel.parts):
            continue
        if rel.name in EXCLUDED_FILES:
            continue
        files.append(path)
    return sorted(files)


FILES = markdown_files()
REL_SET = {p.relative_to(ROOT).as_posix() for p in FILES}
BY_BASENAME: dict[str, list[str]] = defaultdict(list)
BY_STEM: dict[str, list[str]] = defaultdict(list)
for rel in REL_SET:
    p = Path(rel)
    BY_BASENAME[p.name.casefold()].append(rel)
    BY_STEM[p.stem.casefold()].append(rel)

# Explicit historical aliases observed in the uploaded corpus.
ALIASES = {
    "physics-walk-d1-d5-consolidated.md": "physics-walk-d1-d5-consolidated.md",
    "physics-walk-d1-d5-consolidated": "physics-walk-d1-d5-consolidated.md",
    "physics-walk-d1-d6.md": "physics-walk-D1-D6.md",
    "physics-walk-d1-d6": "physics-walk-D1-D6.md",
    "physics-walk-d2.md": "physics-walk-D2.md",
    "physics-walk-d2": "physics-walk-D2.md",
    "triadic-structure-of-relating-rev-canonical": "triadic-structure-of-relating-rev-canonical.md",
    "triadic-structure-of-relating": "triadic-structure-of-relating.md",
}


def clean_target(raw: str) -> tuple[str, str]:
    target = unquote(raw.strip())
    anchor = ""
    if "#" in target:
        target, anchor = target.split("#", 1)
    return target.strip(), anchor.strip()


def resolve_target(raw: str, current: Path) -> str | None:
    target, _anchor = clean_target(raw)
    if not target:
        return None
    target = target.replace("\\", "/")
    if target.startswith("./"):
        target = target[2:]

    # Exact repository-relative path.
    if target in REL_SET:
        return target

    # Exact path relative to the current document.
    rel_current = current.relative_to(ROOT)
    relative_candidate = (rel_current.parent / target).as_posix()
    if relative_candidate in REL_SET:
        return relative_candidate

    key = target.casefold()
    if key in ALIASES and ALIASES[key] in REL_SET:
        return ALIASES[key]

    basename = Path(target).name
    candidates = BY_BASENAME.get(basename.casefold(), [])
    if len(candidates) == 1:
        return candidates[0]

    stem = Path(basename).stem if basename.lower().endswith(".md") else basename
    candidates = BY_STEM.get(stem.casefold(), [])
    if len(candidates) == 1:
        return candidates[0]

    return None


def github_anchor(anchor: str) -> str:
    if not anchor:
        return ""
    slug = anchor.strip().casefold()
    slug = re.sub(r"[^\w\- ]", "", slug, flags=re.UNICODE)
    slug = re.sub(r"\s+", "-", slug)
    return f"#{slug}"


def relative_link(target: str, current: Path) -> str:
    # The corpus is predominantly flat; explicit repository-root paths are
    # valid GitHub links from root documents. For nested documents, compute a
    # relative path without relying on platform-specific separators.
    current_rel = current.relative_to(ROOT)
    if current_rel.parent == Path("."):
        return target
    import os
    return Path(os.path.relpath(ROOT / target, current.parent)).as_posix()


def repair_frontmatter(text: str, current: Path, unresolved: list[tuple[str, str, int]]) -> str:
    if not text.startswith("---\n"):
        return text
    end = text.find("\n---\n", 4)
    if end == -1:
        return text
    front = text[4:end].splitlines()
    body = text[end + 5 :]

    out: list[str] = []
    historical: list[str] = []
    i = 0
    while i < len(front):
        line = front[i]
        if line.strip() == "sources:":
            out.append(line)
            i += 1
            while i < len(front) and re.match(r"^\s+-\s+", front[i]):
                source_line = front[i]
                prefix, source = re.match(r"^(\s+-\s+)(.*)$", source_line).groups()  # type: ignore[union-attr]
                source = source.strip().strip('"\'')
                resolved = resolve_target(source, current)
                if resolved:
                    out.append(f"{prefix}{relative_link(resolved, current)}")
                else:
                    historical.append(source)
                    unresolved.append((current.relative_to(ROOT).as_posix(), source, i + 2))
                i += 1
            continue
        # Remove an existing generated historical_sources block so reruns are idempotent.
        if line.strip() == "historical_sources:":
            i += 1
            while i < len(front) and re.match(r"^\s+-\s+", front[i]):
                historical.append(re.sub(r"^\s+-\s+", "", front[i]).strip())
                i += 1
            continue
        out.append(line)
        i += 1

    if historical:
        out.append("historical_sources:")
        for source in dict.fromkeys(historical):
            out.append(f"  - {source}")

    return "---\n" + "\n".join(out) + "\n---\n" + body


WIKILINK = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")
MD_LINK = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)")
BACKTICK_PATH = re.compile(r"`((?:[A-Za-z0-9_. -]+/)+[A-Za-z0-9_. -]+\.(?:md|py|json|txt))`")


def repair_body(text: str, current: Path, unresolved: list[tuple[str, str, int]]) -> str:
    lines = text.splitlines(keepends=True)
    in_fence = False
    repaired: list[str] = []

    for line_no, line in enumerate(lines, 1):
        if re.match(r"^\s*(```|~~~)", line):
            in_fence = not in_fence
            repaired.append(line)
            continue
        if in_fence:
            repaired.append(line)
            continue

        def wiki_repl(match: re.Match[str]) -> str:
            raw_target = match.group(1).strip()
            label = (match.group(2) or raw_target.split("#", 1)[0]).strip()
            target, anchor = clean_target(raw_target)
            resolved = resolve_target(target, current)
            if resolved:
                return f"[{label}]({relative_link(resolved, current)}{github_anchor(anchor)})"
            unresolved.append((current.relative_to(ROOT).as_posix(), raw_target, line_no))
            return f"{label}<!-- unresolved historical reference: {raw_target} -->"

        line = WIKILINK.sub(wiki_repl, line)

        def md_repl(match: re.Match[str]) -> str:
            label, raw = match.group(1), match.group(2).strip()
            if re.match(r"^(?:https?://|mailto:|#)", raw):
                return match.group(0)
            # Preserve optional title after the URL.
            url = raw.split(maxsplit=1)[0].strip("<>")
            target, anchor = clean_target(url)
            resolved = resolve_target(target, current)
            if resolved:
                return f"[{label}]({relative_link(resolved, current)}{github_anchor(anchor)})"
            # Only flag references that look like repository documents.
            if target.lower().endswith((".md", ".py", ".json", ".txt")) or "/" in target:
                unresolved.append((current.relative_to(ROOT).as_posix(), raw, line_no))
            return match.group(0)

        line = MD_LINK.sub(md_repl, line)

        def backtick_repl(match: re.Match[str]) -> str:
            raw = match.group(1)
            resolved = resolve_target(raw, current)
            if resolved:
                return f"`{relative_link(resolved, current)}`"
            unresolved.append((current.relative_to(ROOT).as_posix(), raw, line_no))
            return match.group(0)

        line = BACKTICK_PATH.sub(backtick_repl, line)
        repaired.append(line)

    return "".join(repaired)


def main() -> int:
    changed: list[str] = []
    unresolved: list[tuple[str, str, int]] = []

    for path in FILES:
        original = path.read_text(encoding="utf-8")
        updated = repair_frontmatter(original, path, unresolved)
        updated = repair_body(updated, path, unresolved)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            changed.append(path.relative_to(ROOT).as_posix())

    # Deduplicate unresolved entries while preserving order.
    unresolved = list(dict.fromkeys(unresolved))
    report_lines = [
        "# Reference Repair Report",
        "",
        "Generated by `tools/normalize_references.py` against the repository tree.",
        "",
        f"- Markdown files scanned: **{len(FILES)}**",
        f"- Files changed: **{len(changed)}**",
        f"- Unresolved historical references: **{len(unresolved)}**",
        "",
        "## Files changed",
        "",
    ]
    report_lines.extend(f"- [{name}]({name})" for name in changed)
    report_lines.extend(["", "## Unresolved historical references", ""])
    if unresolved:
        report_lines.append("These references have no unique target in the present repository. They were removed from live `sources:` blocks or marked inline for human adjudication.")
        report_lines.append("")
        report_lines.append("| File | Line | Historical reference |")
        report_lines.append("|---|---:|---|")
        for filename, ref, line in unresolved:
            escaped = ref.replace("|", "\\|")
            report_lines.append(f"| [{filename}]({filename}) | {line} | `{escaped}` |")
    else:
        report_lines.append("None.")
    report_lines.append("")
    REPORT.write_text("\n".join(report_lines), encoding="utf-8")

    print(f"Scanned {len(FILES)} Markdown files; changed {len(changed)}; unresolved {len(unresolved)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
