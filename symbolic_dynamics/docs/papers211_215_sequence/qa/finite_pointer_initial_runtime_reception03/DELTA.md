# Pointer initial receiver 03: separate path and target identities

2026-09-09 UTC. **SOURCE_ONLY / NOT_EXECUTED.** This bounded revision owns
only this new directory. Root will receive the complete delta before any
separately authorized receiver run; no producer or canonical run occurs here.

[inspect_initial.py](inspect_initial.py): **595 lines / 39,649 bytes**,
SHA-256 `6eb51dbad9a0b647020c03abd65823cf2b820f32b6452a69d5d9c8003b6e0450`.
[DELTA.diff](DELTA.diff) contains exactly two native hunks against
[receiver 02](../finite_pointer_initial_runtime_reception02/inspect_initial.py),
whose SHA-256 remains
`ee52f54c6197cb6137397437d7bbd2883e53275e531fd9a6ebaccc1835b91154`.

## Exact defect and correction

The second actual receiver failed at check 59,248, old line 344. Its archived
`/lib64/ld-linux-x86-64.so.2` identity and resolved target
`/usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2` identity have equal
240,936-byte content and SHA
`8c7e2990d2847ca210d6f716d4b9aa62997c2fd2acfcda587c1ec398ed364618`,
but different `symlink` metadata. Comparing the first path against the
second path's full rich row was incorrect. This is a receiver defect,
not a producer failure. Both the 102,532-byte failed audit stdout and the
actual [root native record](../pointer_saved_output_root/RUNTIME_EXECUTION_NATIVE02.json)
are preserved as original inputs.

Only `HERE` and the old line 344 change. The revised branch pins the original
path with `allowed[name]` and its resolved target with `allowed[resolved]`
separately; it then requires the original's actual resolved path to equal
`resolved` and both basic content identities to agree. Only the resolved
target's basic content row enters `ordinary[resolved]`. All allowed-path,
child-capsule and narrow 127-host restrictions remain unchanged. General
`pin` semantics are not relaxed.

The complete 591-line baseline was read and every remaining pin/comparison
site checked for the same mistake. No second instance was found: raw maps
resolve p before `host[p]`; saved module paths are explicitly resolved and
use content-only expected rows; ldd uses the same literal p for the file and
`host[p]`; other calls use the same path's row or explicitly content-only
pins. This is a bounded source audit, not proof of a successful runtime run.

## Actual minimal evidence

[NATIVE.json](NATIVE.json) retains the archived-failure metadata extraction,
actual root-native read, full native diff (8015ba, ordinary exit 1), source pin,
and AST check 43b831. The AST check finds only `check_opens` changed: the
other 20 functions, including `pin`, `aliases` and `audit`, are identical;
other top-level AST is identical except `HERE`. Its complete census lists
all 19 new pin call sites. It does not import or call any receiver function.

The first metadata-display request failed because `jq` is unavailable
(exit 127); that native failure and the successful read-only JSON fallback
are both preserved. No live host probe or scientific stdout body read was
needed. Original preparation and failed-attempt packages were not rewritten
or re-audited; root's already accepted 80-key scope is reused by exact source
derivation, not relabelled as a fresh check.

[INPUTS.sha256](INPUTS.sha256) pins five exact original source/seal/failure
inputs, workspace-root-relative. [SHA256SUMS](SHA256SUMS) is the new
directory-relative nonself seal. Preserve all old versions and failures.
The project skill's source-before-execution gate remains in effect; this
preparation asserts no runtime reception, scientific acceptance or B PASS.
