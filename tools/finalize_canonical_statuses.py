#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / '_compiler/02-audit-repairs-semantic-inventory.md'
text = path.read_text(encoding='utf-8')
old = '3. AUD-007 removes `frequency=weight` from the live probability dependency graph but does not eliminate the need to verify the F8/F9 construction itself.'
new = '3. AUD-007 proposes a route that may eventually remove `frequency=weight` from the live probability dependency graph; until that route is integrated into and accepted by `realizability-weighting-law.md`, frequency=weight remains the current blocker, alongside verification of the F8/F9 construction.'
if old in text:
    path.write_text(text.replace(old, new), encoding='utf-8')
