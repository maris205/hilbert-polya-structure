# P209 root author-pair preparation

Status: `PREPARED_NOT_EXECUTED`. No root producer, build or scientific
comparison has been run by this preparation. Root must read the complete
wrappers and the exact diff, wait for the author package to stabilize, then
decide to execute. This is infrastructure only, not manuscript A, a new
proof contribution, a freeze or a terminal acceptance.

## Exact originals and disclosed changes

`original_snapshot/record_author.py` is the exact 692-line author source:
SHA256 `8519ce540b160a0934902c6ef1f9dc337ab566cd55e8f0efd89d1502d47ac0b0`.
`original_snapshot/launch_author.py` is the exact 145-line author source:
SHA256 `7fc9a8e066c29e1dd85ba37a4e0aa09ebd78182436a22c5b3ea36d4ad4c191e7`.
These are physical documentary copies, never dynamically imported or run.

The two root sources are:

- `root_record_pair.py`, 688 lines:
  `17005c3091c91dfb6a23e249a56ccbcb2b6311b8fe2e0f596454c497bfeecc5f`.
- `root_launch_pair.py`, 154 lines:
  `fa776f69d12e5e106bc8e8bb4e4aaa9534043005d5de8c2f39348b1b896d1caa`.

`ADAPTATION.diff` contains the complete ordinary unified diff from each
original to its root counterpart. Changes are limited to fixed path/role
settings, pair-only entry guards, inclusion of both new wrapper sources in
initial pins, and the existing-canonical/no-adoption restriction. Original
runtime/config discovery, command attempts and full streams, failure cleanup,
incremental input/observation closure, exact generated-manifest accounting
and raw comparisons are preserved. Build helpers remain byte-for-byte as
functions but are unreachable through the pair-only entry point.

`PAPER` is exactly
`/root/autodl-tmp/symbolic_dynamics/papers/209-ordered-fibre-threading`;
`ROOT` is exactly `/root/autodl-tmp/symbolic_dynamics`. Both wrappers write
only new invocation directories below
`docs/papers204_208_sequence/qa/root_replays/p209_author_strict/`.
That base may be created at actual invocation time; no execution directory
or output base was created by preparation. Existing invocation directories,
symlink aliases and previously existing cache prefixes are refused.

The author `bootstrap.py` and mathematical `verify.py` are copied unchanged
into each fresh two-code-file capsule by the actual root run. The preparer
did not inspect the mathematical verifier in this task. No author recorder,
old verifier or external scientific implementation is imported. The original
n=0..5 / 3,414-state guards remain unchanged.

An existing paper `CANONICAL.json` is mandatory before execution and stays
read-only. Its original pin is checked after comparison and in global closure;
all canonical-writing/adoption branches were removed. Three actual raw
comparisons are still required: run1/run2, run1/canonical and run2/canonical.
The legacy diagnostic label `ADOPTED_CANONICAL_BYTES` and the false-valued
`canonical_adopted` field are retained only to minimize the disclosed diff;
neither permits adoption.

## Root launch after stabilization and full reading

First verify this preparation's nonself `SHA256SUMS`. From the workspace
root, choose a new label. Example command (not executed):

```sh
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 LC_ALL=C.UTF-8 TZ=UTC /usr/bin/python3.10 -I -S -B -X pycache_prefix=/root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/qa/root_replays/p209_author_strict/launcher_root_author_pair_01/never_created_launcher_cache /root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/qa/p209_author_root_preparation/root_launch_pair.py pair root_author_pair_01
```

This creates the separate `launcher_root_author_pair_01/` full-stream
package and `root_author_pair_01/` actual pair package. The latter contains
two actual original-box executions, complete stdout/stderr and comparison
records. No output is placed in the author-owned paper. An eventual
`PASS_ROOT_AUTHOR_PAIR` is root execution of the author verifier, not an
independent verifier or manuscript-review decision.

Keep every failure directory. The unchanged outer policy returns
`UNCLOSED_NO_SEAL` if the recorder does not finish with a verifiable complete
receipt/seal; possibly still-changing raw streams get no settled-stream
hashes, outer seal or PASS. Inner caught exceptions retain their original
outcomes and separate owned-process cleanup records. These are bounded
module/open-file/PID-map observations and conservative inventories, not
continuous syscall/grandchild tracing or an OS-hermetic claim. An unclosed
outer result does not assert that all descendants have exited.

## Preparation-only checks

Both original physical copies were actually compared with their paper
originals using `cmp --`: both exit 0, empty stdout/stderr. Both unified
diff commands returned expected exit 1 because the wrappers intentionally
differ. Python 3.10 AST parsing succeeded on all four infrastructure files,
without importing or executing any of them. AST comparison additionally
confirmed that only recorder `science/pair/main` and launcher
`check_closed_recorder/main` function bodies changed; all other function
bodies are identical to their originals. These are documentary/static checks,
not producer runs, builds, mathematical validation or canonical comparisons.

The project research skill controls this separation of actual evidence from
prepared code and the retention of original sources. No paper, historical
gate, central index or Git state was modified; external actions remain
`HOLD_EXTERNAL`.
