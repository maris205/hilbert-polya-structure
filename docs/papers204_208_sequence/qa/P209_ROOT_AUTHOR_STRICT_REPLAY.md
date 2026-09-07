# P209: actual root author-code pair

2026-09-07 UTC. **PASS_ROOT_AUTHOR_PAIR / HOLD_EXTERNAL**. Root actually
launched two new source-only executions of the unchanged paper-local
author verifier. This is not merely inspecting the author's earlier pair,
and is not an independent mathematical implementation or manuscript review.

Each run passed **98,278 assertions on all 3,414 original-box states**,
exactly n=0,...,5. The complete per-state stdout is byte-identical to the
already existing 1,810,065-byte canonical, SHA-256
`5fb68816b57897fb5c68f661dbdc8b75c7066e0adf967bdd3b49067d23167720`.
Both producer exits and the three actual raw comparisons are zero. Root
then independently checked the complete closed pair and executed the three
raw comparisons again; those are comparisons, not two extra producer runs.

The [full actual launch/precheck/closure record](P209_ROOT_AUTHOR_STRICT_REPLAY.actual.json)
binds the command, actual outer exit zero, complete stdout and the later
read-only closure output. The actual inner package is
[root_author_pair_01](root_replays/p209_author_strict/root_author_pair_01/RECEIPT.json)
and the [outer launcher](root_replays/p209_author_strict/launcher_root_author_pair_01/RECEIPT.json)
retains the recorder's complete stdout/stderr. No standard output was
constructed or adopted by the root pair.

## Inputs and original-source adaptation

Root read every line of the 688-line recorder and 154-line launcher, their
complete adaptation diff and the earlier author sources. The
[six-payload preparation](p209_author_root_preparation/README.md) preserves
exact physical copies of both originals. Root's actual two `cmp` commands
confirmed byte identity with those originals. Two `diff` exits of 1 are
expected and their full concatenated output equals the declared diff.
Python 3.10 AST parsing of all four infrastructure files passed without
executing them. This documentary precheck preceded the real launch.

The adaptation changes only root output/role paths, pair-only entry,
initial pins for both wrappers, and the read-only existing-canonical rule.
No old recorder is dynamically imported, and no mathematical code or
cutoff is changed. Every producer capsule initially contains exactly the
unchanged `bootstrap.py` and `verify.py`. Both new wrappers are included
in the initial input set. Existing-canonical equality is checked against
the original baseline; no adoption branch remains.

The minimal C.UTF-8/UTC environment and `/usr/bin/python3.10 -I -S -B`
use optimization zero, no site and separate absent exclusive cache paths
for outer launcher, parent and both children. All 3,211 known input paths
including capsules/comparison inputs and all 3,133 runtime-file records
match before/after/current bytes. All 85 commands completed with actual
exit zero: 80 recursive linkage commands, two producers and three raw
comparisons. All outer ten initial pins passed too. Parent/child module,
open-file and sampled direct-PID map closure has no uncovered dependency
or consumed bytecode; configuration presence/path sets were recaptured.

These are the recorded conservative inventories and bounded observations,
not continuous syscall or grandchild tracing, a fully traced outer startup,
or OS-hermetic reconstruction. Failed/unknown child outcomes would not
become successful results through cleanup. The outer unclosed policy has
not been invoked in this actual successful pair.

## Complete seals and remaining gates

Root checked all 462 inner payloads and all ten outer payloads, with exact
nonself directory coverage, then checked every payload again. Inner seal:
`107a068ca6bbbea6cddf1c6ea9f9cb4604e3143c4d19d0232adcd4eb0bf16601`.
Outer seal:
`502b6d315f87bb6efdba41e4cd99862c270af4005dd8e631d5d373176d653756`.

The separate [author archive inspection](P209_AUTHOR_PAIR_ROOT_INSPECTION.actual.json)
preserves the earlier author pair's 463+10 payload closure. The
[two author builds and four actual root page views](P209_AUTHOR_ROOT_VIEWS.md)
are a different evidence obligation. None of these runs proves an
all-parameter theorem by enumeration, creates Round0, closes A/B or
completes P209. Root remains a proof contributor and cannot serve as an
independent P209 reviewer. The fifth batch seat remains unfilled.
