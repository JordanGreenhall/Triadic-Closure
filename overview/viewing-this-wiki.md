---
title: Viewing This Wiki
type: overview
created: 2026-06-21
updated: 2026-06-21
status: control
confidence: high
---

# Viewing This Wiki

This folder is a real Markdown wiki, not only a machine index. It is a Triadic Closure wiki; physics is a major deep-dive subcorpus, not the whole frame. It uses Obsidian-style wikilinks of the form: double-bracket page names.

## Best option: Obsidian

Open the folder as an Obsidian vault:

`/Users/roberthall/Library/CloudStorage/GoogleDrive-jordan.greenhall@gmail.com/My Drive/Triadic Closure Wiki/Triadic Closure Wiki`

Steps:

1. Open Obsidian.
2. Choose **Open folder as vault**.
3. Select `/Users/roberthall/Library/CloudStorage/GoogleDrive-jordan.greenhall@gmail.com/My Drive/Triadic Closure Wiki/Triadic Closure Wiki`.
4. Open `index.md` first, then [[triadic-closure-reading-order]].

Obsidian will make the wiki links clickable and gives backlinks / graph view.

## Good option: VS Code

Open the folder in VS Code. Markdown links and file search work well, especially with extensions such as:

- Markdown All in One;
- Foam;
- markdown-link-updater.

This is less native than Obsidian but good for editing.

## Static HTML option

A dependency-free static builder is included:

```bash
cd "/Users/roberthall/Library/CloudStorage/GoogleDrive-jordan.greenhall@gmail.com/My Drive/Triadic Closure Wiki/Triadic Closure Wiki"
python3 _meta/build_html_wiki.py
open _site/index.html
```

This produces a clickable HTML copy under `_site/`. It is intentionally simple and not a replacement for Obsidian. Re-run it after edits.

## Terminal/manual option

The wiki is still usable manually:

- Start at `index.md`.
- Read `overview/triadic-closure-reading-order.md` before entering physics pages.
- For control/status work, read:
  - `overview/corpus-lineage.md`
  - `overview/supersession-map.md`
  - `overview/locked-actual-decrement-map.md`
  - `overview/physics-domain-mature-status.md` (for physics work)
  - `overview/physics-domain-work-plan.md` (for physics work)
  - `process/agent-execution-rules.md`

## Rule

If browsing by hand, never treat raw package files as current just because they contain polished prose. Always route through `index.md`, [[triadic-closure-reading-order]], and the control pages first.
