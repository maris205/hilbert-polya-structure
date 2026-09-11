# P209 actual author evidence

2026-09-07 UTC. **AUTHOR_PAIR_PASSED / NOT_MANUSCRIPT_REVIEW /
OWNER_AMBER / HOLD_EXTERNAL.** This is an author execution report. The
all-size results are proved in [the proof package](PROOF_PACKAGE.md), not
inferred from these finite checks. Existing framing and execution inputs
were not rewritten after they were pinned.

## Actual pair and complete output

The fresh [standalone verifier](verify.py) was executed twice in separate
physical code-only capsules. Each contains exactly `verify.py` and
`bootstrap.py`, copied and pinned before its producer starts. No pilot,
candidate-gate, old-paper or reviewer mathematical implementation is
imported. This tuple-product author representation is disclosed; it is not
an independent P209 review.

Both producers actually exited zero and passed **98,278 assertions over
3,414 states**, with complete per-state transition, orbit, graph,
vertex-image, decoder and literal predecessor data. The original cutoff
is exactly $n=0,\ldots,5$. Three actual `cmp` commands compared the two
raw outputs and each with the adopted canonical; all exited zero.
`CANONICAL.json` was copied from the first actual stdout only after the
producer-pair comparison passed. Its size is 1,810,065 bytes and SHA256 is
`5fb68816b57897fb5c68f661dbdc8b75c7066e0adf967bdd3b49067d23167720`.

| n | All functions | Recurrent functions | Largest fibre | Box assertions |
|---|---:|---:|---:|---:|
| 0 | 1 | 1 | 1 | 16 |
| 1 | 1 | 1 | 1 | 20 |
| 2 | 4 | 3 | 2 | 85 |
| 3 | 27 | 14 | 4 | 637 |
| 4 | 256 | 87 | 8 | 6,726 |
| 5 | 3,125 | 671 | 16 | 90,790 |

The six box counts sum to 98,274; four separate literal adapter-witness
assertions give the recorded total 98,278. Every maximizing target is the
unique cyclic successor, with the stated empty/singleton conventions.
The table is extracted from actual output, not a replacement for the
[full canonical](CANONICAL.json). Observed entrance indices are only
finite orbit data, not an all-size sharp clock.

## Commands and execution key

The actual outer command, from the workspace root, was:

```sh
/usr/bin/env -i PATH=/usr/bin:/bin LANG=C.UTF-8 LC_ALL=C.UTF-8 TZ=UTC /usr/bin/python3.10 -I -S -B -X pycache_prefix=/root/autodl-tmp/symbolic_dynamics/papers/209-ordered-fibre-threading/launcher_author_pair_01/never_created_launcher_cache /root/autodl-tmp/symbolic_dynamics/papers/209-ordered-fibre-threading/launch_author.py pair author_pair_01
```

The [outer receipt](launcher_author_pair_01/RECEIPT.json) records actual
recorder exit zero and retains full recorder stdout/stderr and the exact
pre-spawn sources. The [inner receipt](author_pair_01/RECEIPT.json),
[all command index](author_pair_01/ALL_COMMAND_RECORDS.json), and each
producer's pre-spawn attempt, complete streams, observations and receipt
are the originals. Both producer commands use the same isolated flags,
optimization zero, explicit minimal environment and their own absent,
exclusive bytecode-cache prefixes. Neither `site` nor old bytecode is used.

The full known-input key contains 3,209 paths including source capsules
and generated data subsequently consumed by comparisons. There are 69
initial scientific/documentary inputs, 3,133 runtime files, and 80 actual
successful linkage commands; with two producers and three comparisons,
the complete command index has 85 entries. Before/after bytes, path
resolutions, optional configuration presence, and inventory file-name sets
are checked. Stdlib/dynload, recursive dependency closure, actual loader
paths, locale/gconv and configuration inputs are covered. The
[observation closure](author_pair_01/OBSERVED_CLOSURE.json) has no uncovered
file or consumed bytecode.

Early/late parent and producer modules/maps, sampled direct-child maps,
and conservative inventories are the actual observation scope. This is
not continuous tracing, a complete grandchild trace, or OS-hermetic
reconstruction. Generated manifests are recognized only by exact paths
that this invocation generated and successfully validated.

## Preserved seals and preflight scope

The [463-payload pair seal](author_pair_01/SHA256SUMS) has SHA256
`25e6fc27591c42e72d7b940de38a312d61b93587e119244cf8ed84fc5c587c85`.
The [10-payload outer seal](launcher_author_pair_01/SHA256SUMS) has SHA256
`e342887d8b1c4cda6c2e9f2e3f8cd55fee602abfbe6dcd198196ff1006237e09`.

Root and a separate infrastructure reader checked the recorder before
the first execution. Their pre-execution corrections covered exact
generated-manifest handling; cleanup/reaping before sealing; preservation
of partial command observations and known-input baselines; configured
local/user font roots; conservative unclosed outer outcomes; and the
original existing-canonical baseline. These were infrastructure fixes,
not mathematics or manuscript findings. No mathematical or build attempt
was run with the earlier recorder versions. The executed recorder is
`8519ce540b160a0934902c6ef1f9dc337ab566cd55e8f0efd89d1502d47ac0b0`;
launcher `7fc9a8e066c29e1dd85ba37a4e0aa09ebd78182436a22c5b3ea36d4ad4c191e7`;
bootstrap `dc2f0ef968f2b451ceaf390ac7a8189005881246624a0f94ab64879efa18a80b`.

The actual pair passed on its first attempt. No failed numerical attempt
is hidden. Source-retrieval limitations remain separately disclosed in
[SOURCE_AUDIT.md](SOURCE_AUDIT.md). Root's author-level reads and
infrastructure inspection do not constitute manuscript A or B.

The [build report](BUILD_REPORT.md), [actual all-page views](PAGE_VIEWS.md)
and [current lifecycle](PAPER_STATUS.md) complete the author handoff.
No frozen Round0, manuscript-review acceptance or batch completion is
claimed here.
