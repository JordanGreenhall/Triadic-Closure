#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OWNER = ROOT / 'ch2-two-center-capacity-ownership-and-mode-fork.md'
STATUS = ROOT / 'chemistry-domain-mature-status.md'
INDEX = ROOT / 'index.md'
INVENTORY = ROOT / 'repository-inventory.md'
CONTROL = ROOT / 'ch2-supersession-control.md'

required = {
    OWNER: [
        'capacity two',
        'Capacity is not occupancy',
        'Symmetric/antisymmetric is not automatically bonding/antibonding',
        'CH2-F1', 'CH2-F2', 'CH2-F3',
        'CH3 energetic ordering remain unestablished',
    ],
    STATUS: ['| CH2 |', 'CH2-F1', 'CH2-F2', 'CH2-F3', 'No CH3'],
    INDEX: ['CH2 Two-Center Capacity, Ownership, and Mode Fork', 'CH3 has not begun'],
    INVENTORY: ['ch2-two-center-capacity-ownership-and-mode-fork.md', 'ch2-supersession-control.md'],
    CONTROL: ['Do not use capacity two as occupancy two', 'Do not infer CH1 nonemptiness'],
}

for path, needles in required.items():
    text = path.read_text()
    for needle in needles:
        if needle not in text:
            raise SystemExit(f'CH2 verification FAIL: {path.name} lacks {needle!r}')

for frontier in ('CH2-F1', 'CH2-F2', 'CH2-F3'):
    count = OWNER.read_text().count(frontier) + STATUS.read_text().count(frontier)
    if count != 2:
        raise SystemExit(f'CH2 verification FAIL: {frontier} placement count {count}, expected 2')

print('CH2 verification: PASS')
