# P211 A actual initial/canonical/strict-pair replay record

2026-09-08 UTC. All scientific invocations below actually occurred under
root's distinct A bindings. This log receives and explicitly reuses those
records; it does not claim an additional invocation by the final reporter.
The complete original runtime evidence is read-only and unchanged.

## Exact source, parameters and runtime

Scientific source is the independent 403-line `verify.py`, 17,324 bytes,
SHA-256 `35140051d98c1adcc14ca0041407f1a07a0488bb40a9962fa586ac517c0a389a`.
The single `parameters.json` is 426 bytes, SHA-256
`a12bcbda054a0a6a8cfc6ebd774e70ff8df4318dd7d902e0724a6d84212e78cc`.
The capsule is exactly those two physical files; only
`verify.py --parameters ABS_PARAMETERS` is supported. Their literal
scientific argv, source pin and successful compile/exec outcome are in
each child RESULT. The runtime does not use direct `python verify.py`
startup; that difference is deliberately recorded.

All ordinary imports are exactly itertools, json, math, sys. The accepted
runtime lock is `qa/p211_runtime_preparation/discovery02/RUNTIME_LOCK.json`,
SHA-256 `1499a93909e39b49c16408985053936b7eb7efcf664e91fd75fa77de607be2ab`.
All 122 ordinary runtime keys, bounded configuration and loader states,
adapter source pins and actual observed inputs are included, not only the
interpreter. Scientific/native/envelope deadlines are 300/60/900 seconds.

The exact environment is PATH=/usr/bin:/bin, LANG=C.UTF-8,
LC_ALL=C.UTF-8, TZ=UTC, with no inherited extra environment. Each stage uses
system `/usr/bin/python3.10 -I -S -B`, optimize zero and its distinct
never-created pycache prefix. The actual search path is
`/usr/lib/python310.zip`, `/usr/lib/python3.10`,
`/usr/lib/python3.10/lib-dynload`. Complete before/after runtime, configuration,
open-event, input and process-settlement records remain in every stage.

## Actual outer invocations

All paths below are absolute in the real records. Workspace cwd is
`/root/autodl-tmp/symbolic_dynamics`. These are recorded past commands,
not instructions to launch another run.

```text
/usr/bin/env -i PATH=/usr/bin:/bin LANG=C.UTF-8 LC_ALL=C.UTF-8 TZ=UTC /usr/bin/python3.10 -I -S -B -X pycache_prefix=/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/root_replays/p211_a_initial_01/never_created_outer_cache /root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/p211_runtime_preparation/p211_runtime.py outer /root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/p211_a_initial_binding/BINDING.json 8f019e9cc35ba0c0d3ed02d9b419f844acc09f0df83ae8aeff590811463b5f0f /root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/root_replays/p211_a_initial_01

/usr/bin/env -i PATH=/usr/bin:/bin LANG=C.UTF-8 LC_ALL=C.UTF-8 TZ=UTC /usr/bin/python3.10 -I -S -B -X pycache_prefix=/root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/root_replays/p211_a_pair_01/never_created_outer_cache /root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/p211_runtime_preparation/p211_runtime.py outer /root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/p211_a_pair_binding/BINDING.json ac746054ca390447aea13089ca3de3ea4832e0d1eb2a54140640fbc23b8d4325 /root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/root_replays/p211_a_pair_01
```

The actual product sessions are **23759** and **48113**, both settled with
exit zero. Initial actual chunks are 9f77fe then 099f4f; pair chunks are
3a662d then acce52. Exact requests, actual returned records and final
controls are preserved in each binding package's
`PRODUCTION_TOOL_INVOCATION.json`. Each child actual argv uses the same
binding/digest and stage-specific child01/child02 cache prefix, with its
cwd the two-file `recorder/capsule` directory. The complete child commands,
pids, process-group settlement, exit codes and raw stream pins are in
`recorder/commands/03_verify_01/RECEIPT.json` and, for the pair,
`03_verify_02/RECEIPT.json`.

## Initial reception and exclusive canonical adoption

Under `qa/p211_a_initial_binding/`, BINDING.json is 52,365 bytes with the
initial digest in the command above. The execution tree is
`qa/root_replays/p211_a_initial_01/`: 77 payloads, seven actual native
commands and one actual scientific invocation. Its complete manifest is
`91570ff70f06a60f1190ab64c4593505580880b572266941494a61eaf7bc3375`.
The complete initial stdout is
`recorder/commands/03_verify_01/stdout.raw`; scientific stderr is empty.

Root's original complete record reception passed 114,707 checks / 306
paths, followed by 352,469 saved-output semantic checks. Only then did
root exclusively write the previously absent A canonical from these raw
bytes. The full ADOPTION packet preserves the false preexistence flag,
accepted source/production/semantic pins, event order and actual comparison:

```text
/usr/bin/cmp -- /root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/qa/root_replays/p211_a_initial_01/recorder/commands/03_verify_01/stdout.raw /root/autodl-tmp/symbolic_dynamics/docs/papers211_215_sequence/reviews/p211_a/CANONICAL.json
```

That comparison exited zero with empty stdout/stderr. This is one distinct
adoption comparison, not one of the later pair's three. No normalization,
old-pilot conversion or prior canonical overwrite occurred. Present-day
canonical existence is not represented as a new absence observation.

## Separate strict pair and actual raw comparisons

Under `qa/p211_a_pair_binding/`, BINDING.json is 69,389 bytes with the
pair digest above. The exact initial-to-pair delta changes only mode,
attempt, accepted canonical pin, additional actual count equalities,
provenance and canonical-preservation policy. Source, parameters, imports,
runtime, carriers and deadlines are unchanged. The complete delta object
has been checked against both whole binding objects.

The pair execution tree is `qa/root_replays/p211_a_pair_01/`: 104 payloads,
11 actual native commands and two actual scientific invocations. Manifest:
`87585f6973baa78ce13af9686cc8b5ab66c70372b62ca658f6fec4fda84dce10`.
Each child exited zero with complete stdout and empty stderr. The actual
native comparisons under `recorder/commands/` are:

| Command record | Exact operands | Actual result |
| --- | --- | --- |
| `04_canonical_1` | `03_verify_01/stdout.raw` versus accepted A canonical | exit 0; empty raw stdout/stderr |
| `04_canonical_2` | `03_verify_02/stdout.raw` versus accepted A canonical | exit 0; empty raw stdout/stderr |
| `05_pair` | `03_verify_01/stdout.raw` versus `03_verify_02/stdout.raw` | exit 0; empty raw stdout/stderr |

Every record carries the full absolute `/usr/bin/cmp --` argv, cwd, ENV4,
deadline, successful process settlement and stream pins. The reviewer's
artifact receiver checked every whole raw operand in addition to the real
native receipts. This is byte equality, not normalized JSON equality.

All three actual stdout files and the canonical are **1,313,394 bytes**,
SHA-256 `e637aa186b5d11c3bba1ad5318d42c7dc93ea736fee9ed3013ebcc1beaa9cd43`.
Root's pair record reception passed 190,018 checks / 350 paths; both
complete saved outputs separately passed 352,811 semantic checks.

## Actual finite census, same in all three outputs

| n | Whole states/targets | Image targets | Zero-fibre targets | Observed height | Named A checks |
| --- | --- | --- | --- | --- | --- |
| 1 | 1 | 1 | 0 | 0 | 29 |
| 2 | 3 | 2 | 1 | 1 | 61 |
| 3 | 10 | 5 | 5 | 2 | 166 |
| 4 | 35 | 13 | 22 | 2 | 522 |
| 5 | 126 | 34 | 92 | 3 | 1,761 |
| 6 | 462 | 89 | 373 | 3 | 6,178 |
| 7 | 1,716 | 233 | 1,483 | 4 | 22,234 |

Each invocation therefore has 2,353 states/targets/edges and 30,951 named
checks. The full output preserves every row, incoming list, complete orbit,
cycle, traversal, labelled gap description and coefficient table, not
only this census. Named counts exclude some helper assertions and are
not claimed to count every low-level comparison. These finite facts do
not establish an all-n theorem or extend the manuscript's claim scope.

## Reviewer reception, reuse and limits

`RUNTIME_EVIDENCE_ACCEPTANCE.md` records my new actual artifact receptions:
176,456 checks / 323 paths for initial, 312,961 / 360 for pair, and
9,575 / 454 for full-key closure. The complete original 226/244 binding
input keys, 17/10 binding packages, 77/104 execution trees, actual native
records, all original root semantic pins and the existing canonical were
checked. The original 20 preparation payloads remain unchanged.

The final reporter performed zero new scientific producers, zero builds,
zero page views and no semantic-output recomputation. Root's actual three
scientific invocations and complete saved-output semantic inspections are
explicitly reused under the full unchanged dependency key. Process audit
events and sampled maps/configuration do not imply continuous OS tracing
or host hermeticity. The old pilot failure and all old records are preserved.
This log does not preaccept the root response or same-A delta.

All `qa/` paths in this log are relative to `docs/papers211_215_sequence/`.
