# P28 Compiler Cycle

- Exact merged P27 base: `92b194970a7fa00f516e759eaeb3e4d3d38aad03`
- Exact clean P28 verifier-reconciliation head: `8c64e33ddd8e29093ccf09e405f3a041e6b2d2b0`
- Branch: `agent/normalization-p28-persistent`

## Clean fixed-point run

Precondition: `git status --porcelain=v1` emitted no bytes at the named content head.

Command:

`python3 _compiler/verify_p28.py --base 92b194970a7fa00f516e759eaeb3e4d3d38aad03`

Exact stdout:

`P28 verification: PASS (base 92b194970a7fa00f516e759eaeb3e4d3d38aad03; 32 changed files; 21 changed Markdown files; 433 Markdown links scanned)`

The command was run twice from the same clean checkout. Outputs were byte-identical.

SHA-256 of exact stdout including its trailing newline:

`4171fa72165a6f78589e63e72cd6b312db2acb5333f6b2caee25c28d11ee05ee`

Byte count of exact stdout including its trailing newline: `144`.

Postcondition: `git status --porcelain=v1` emitted no bytes after both runs.

## Exact algebra

`python3 _compiler/verify_p28_algebra.py` reproduced `_compiler/verification/p28-exact-finite-algebra.txt` byte-for-byte. It verifies `C(3,2)=3`, an exact rational witness for the `Omega_Lambda` identity, four same-scaling coefficient countermodels, and the two-premise conditional-flatness truth table.

## Failure capability

Executed verifier simulations rejected all six stale states with exit code 1:

- `--simulate confirmation`
- `--simulate coefficient`
- `--simulate dynamics`
- `--simulate flatness`
- `--simulate frontier`
- `--simulate boundary`

The bounded A1 consumer packet also executed and rejected four independent stale surfaces with exit code 1:

- `--simulate downstream-imports`
- `--simulate downstream-ledger`
- `--simulate downstream-smuggle`
- `--simulate downstream-deferred`

Three claim-specific partial-deletion surfaces also rejected with exit code 1 while retaining surrounding content and the P28 route:

- `--simulate downstream-coefficient-grade`
- `--simulate downstream-translation-grade`
- `--simulate downstream-structural-elements`

Exact commands and rejection lines are committed in `_compiler/verification/p28-failure-*.txt`.

## Fixed-point conclusion

The clean verifier-reconciliation state is stable under repeated verification in a detached case-sensitive checkout of the named commit. `git status --porcelain=v1` emitted no bytes before or after both runs; no untracked evidence or Python cache affected counts. The verifier and algebra reproducer modify no tracked file. Evidence documentation is added only after the named verifier-reconciliation state and does not alter canonical P28 theory, consumers, or frontier substance.
