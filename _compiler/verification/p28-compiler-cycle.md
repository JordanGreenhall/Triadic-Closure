# P28 Compiler Cycle

- Exact merged P27 base: `92b194970a7fa00f516e759eaeb3e4d3d38aad03`
- Exact clean P28 content head: `9489e0b7211bae8e0be68c35e96b943f1f0c5ba8`
- Branch: `agent/normalization-p28-persistent`

## Clean fixed-point run

Precondition: `git status --porcelain=v1` emitted no bytes at the named content head.

Command:

`python3 _compiler/verify_p28.py --base 92b194970a7fa00f516e759eaeb3e4d3d38aad03`

Exact stdout:

`P28 verification: PASS (base 92b194970a7fa00f516e759eaeb3e4d3d38aad03; 25 changed files; 16 changed Markdown files; 413 Markdown links scanned)`

The command was run twice from the same clean checkout. Outputs were byte-identical.

SHA-256 of exact stdout including its trailing newline:

`c534b386f15fa410f75b73ccde6caeee6fd21e55dd805d318a5ed12bd8248bf4`

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

Exact commands and rejection lines are committed in `_compiler/verification/p28-failure-*.txt`.

## Fixed-point conclusion

The clean content state is stable under repeated verification. The verifier and algebra reproducer modify no tracked file. Evidence documentation is added only after the named content state and does not alter canonical corpus semantics or verifier architecture.
