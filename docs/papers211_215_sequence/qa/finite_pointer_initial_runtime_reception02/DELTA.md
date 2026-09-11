# Pointer initial receiver 02: minimal source-only correction

2026-09-08 UTC. This new directory alone is owned by this bounded revision.
**SOURCE_ONLY / NOT_EXECUTED.** Root must receive this delta before separately
running the revised checker. No producer or canonical run is authorized here.

[inspect_initial.py](inspect_initial.py): **591 lines / 39,410 bytes**,
SHA-256 `ee52f54c6197cb6137397437d7bbd2883e53275e531fd9a6ebaccc1835b91154`.
[DELTA.diff](DELTA.diff) is the complete four-hunk native forward difference
from [receiver 01](../finite_pointer_initial_runtime_reception01/inspect_initial.py),
SHA-256 `daf7b06a20252979c96cca9f13793ae0d3230cd65e30f5124ffff1a379c44bdc`.
The ordinary native diff exit 1 and full output are in [NATIVE.json](NATIVE.json).

## Cause and exact change

The [first actual root audit result](../pointer_saved_output_root/runtime_execution01/RESULT.json)
and its complete 4,288-byte child audit stdout record exit 1 at check 5,189:
receiver 01 incorrectly required all 129 runtime-lock rows to be host files.
This is a receiver classification defect, not a producer failure. The original
failed audit and its closed controller evidence remain unchanged.

The historical lock has exactly **129 rows = 127 host + 2 project sources**.
The two project paths are the old `p211_runtime.py` and `runtime_core.py`.
The pointer wrapper remains the separately bound third adapter source.
Revision 02 changes only:

1. `HERE` to this new source directory.
2. The 129-row classification: the complete set of project paths must equal
   those two literal old sources; each full rich row must equal the already
   validated binding adapter row, and its SHA/size must equal `SOURCE_PINS`.
3. The host allowlist and its annotation: `aliases(host_files)` receives only
   the remaining 127 entries, and every resolved alias must also lie outside
   the project. This narrower set feeds unchanged child open and raw maps
   checks. The three project module registrations remain explicit and unchanged.
4. The output fields: `frozen_runtime_lock_rows`, `frozen_project_source_rows`,
   and `frozen_host_file_rows` distinguish 129, 2 and 127. The historical
   binding result's `runtime_files:129` stays unchanged.

The provenance-containing `expected` key remains documentary only; it is
not substituted into child or mapped-host scope. All other infrastructure,
scientific-output opacity, closure, time, command and strict-input checks
are unchanged.

## Actual source-only checks and preservation

Native f76571 reads only archived lock/binding metadata and confirms the exact
129/127/2 partition, both full rich project rows and 127 declared host aliases
outside the project. Native 7e2a68 parses AST only: the four old-line change
ranges are 23, 307, 435–437 and 563; only `audit` changes function AST.
The other 20 functions and all other top-level AST except `HERE` are identical.
The ten stdlib imports and absence of execution/write calls remain checked.
No checker function is imported or called.

Native 65e6d7 verifies all 9 original preparation payloads; aa6736 verifies all
10 failed-audit payloads. Their original seals remain
`44ea091871b62f2e5889f6ec644ddc1acb56163b8791d077309080870e343ddd` and
`019a2cbab0c81dc0ac4c77432f64bdb5ce331f7a3001069961f4ab1194d4b56b`.
[INPUTS.sha256](INPUTS.sha256) pins eight exact original source/lock/binding/
failure inputs, workspace-root-relative. This package's [SHA256SUMS](SHA256SUMS)
is directory-relative and nonself.

No scientific stdout body was read, no scientific gate was changed, and no
receiver or producer was executed in this preparation. The project skill's
source-before-execution gate is retained. Preserve this package and place any
later separately authorized root execution in a new capture directory.
