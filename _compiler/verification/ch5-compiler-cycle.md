# CH5 Compiler Cycle

## First cycle

The initial PR 57 branch incorrectly treated D2(b) mass-separation/Born–Oppenheimer material as CH5. Comparison against the named chemistry specification and X1 ownership failed.

## Repair

The branch was force-reset to the merged CH4 base. The mislabeled owner and all associated propagation were discarded. CH5 was rebuilt from D2(d–e): covalent limit, ionic limit, charge site, site-apportionment continuum, screening texture, and electronegativity.

## Second cycle

No further semantic ownership change was required. Scale separation remains X1-owned; CH3 remains maintenance/energy; CH6 remains unopened.

**Result:** PASS, no-change after repair.