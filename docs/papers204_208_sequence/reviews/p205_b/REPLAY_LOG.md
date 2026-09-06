# P205 manuscript Review B — actual independent executions

Scientific executions and comparisons: 2026-09-05 UTC. Receipt assembled
2026-09-06 UTC after a parent-reported service interruption; the successful
pair below predates the interruption and was not rerun merely to change
the receipt date. See [EXECUTION_CONTINUITY.md](EXECUTION_CONTINUITY.md).

Working directory: `/root/autodl-tmp/symbolic_dynamics`.
Interpreter actually queried: **Python 3.12.3**. Both fresh child processes
used `PYTHONHASHSEED=0 LC_ALL=C TZ=UTC`, ordinary standard-library Python,
and the same unchanged local standalone producer:

```sh
PYTHONHASHSEED=0 LC_ALL=C TZ=UTC python3 docs/papers204_208_sequence/reviews/p205_b/verify.py
```

| Execution | Child exit | Complete captured stdout | Bytes | Assertions |
|---|---:|---|---:|---:|
| Fresh process 1 | 0 | [run1.stdout](run1.stdout) | 14,444 | 12,023,630 |
| Fresh process 2 | 0 | [run2.stdout](run2.stdout) | 14,444 | 12,023,630 |

The full first stdout became [CANONICAL.json](CANONICAL.json); it was not
a expected-result template. Each actual child stdout was retained verbatim
with its final newline. The independent producer prints only computed JSON,
has no file I/O, and never reads a canonical, manuscript, author/A/gate
implementation, old verifier or dataset. No random seed, network service,
imported scientific code, subprocess or hidden helper affects its output.
It imports only `collections`, `hashlib`, `itertools` and `json`.

The following **raw byte comparisons actually ran**, each with no output
and exit zero. These are not normalized JSON comparisons:

```sh
cmp docs/papers204_208_sequence/reviews/p205_b/run1.stdout docs/papers204_208_sequence/reviews/p205_b/run2.stdout
cmp docs/papers204_208_sequence/reviews/p205_b/run1.stdout docs/papers204_208_sequence/reviews/p205_b/CANONICAL.json
cmp docs/papers204_208_sequence/reviews/p205_b/run2.stdout docs/papers204_208_sequence/reviews/p205_b/CANONICAL.json
```

Exact pins:

| Artifact | SHA256 |
|---|---|
| `verify.py` | `98c74ab0e43171e673c232a9e6e2cf3f517825f9133eca9974a384fb4e846e97` |
| `CANONICAL.json`, `run1.stdout`, `run2.stdout` (each) | `9125dc56e504cafb295cb29b5469a4b941d5a0d63ccedcf3a32076272d5aedb9` |
| `INPUT_PINS.sha256` | `0bd844df7fda5fd3f3581bcc5234fcd15e40cdc146dd5e0e1d2c3d32a088b8a3` |

## Exact execution coverage

Every labelled simple graph and every state **and target** is covered for
`0<=n<=4`, `q in {3,5,6}`, plus `n=5,q=3`: 16 boxes, 1,252
graph/palette instances and 380,061 state/target instances. The canonical
contains each full box's height, eventual-period and fibre histograms,
literal cycle count, number of examined edge subsets, and a rolling SHA256
of its ordered per-state records (graph, source, literal successor,
distances, SCC depth/period and full decoded source set).

The records are deterministically recomputed, not all expanded in stdout;
the canonical is the **complete actual stdout**, not a claim that a digest
is an expanded archive of every orbit. No cutoffs are omitted or inferred.

- Boolean walk-weight coefficients compute first reachable weight, with
  zero-weight same-layer closure and the generic simple-route horizon
  `(q-1)(n-1)`. This is not Floyd or event-queue activation.
- Kosaraju SCCs identify cycles directly; reverse BFS supplies exact
  entrance and eventual period. This is not indegree leaf peeling.
- Every literal trajectory is checked through `h+2q+1`, with actual
  conflict bits and first conflicts. The coordinate and threshold tests
  each execute 4,265,682 assertions.
- Every target is decoded by enumerating old conflict **edge subsets**,
  then checking equality on every old edge. It is compared with the
  complete actual source set, not just a count, in 380,061 assertions.
- Global bounds and all graph/target equality pairs are tested, including
  disconnected graphs, isolates, proper targets, empty fibres and `n=0`.
- Static total-cover support exhausts all labelled graphs `0<=n<=5`
  (1,100 graphs, not all order-six graphs). It includes all six connected
  four-vertex boundary counts and the P4 containment counts `3,2,2,3`.
- The sharp path family has 351 cases, `2<=n<=40`, `3<=q<=11`, with
  literal threshold checks; the largest tested entrance is 380. Constant
  star fibres are checked at `3<=n<=14`, `q=3`.
- Controls detect reversed waiting orientation, a first-conflict/first-
  increment offset, omission of each inverse condition, seed-mask loss of
  clock information, total-cover-only loss of target information, and the
  literal CCA constant-edge separator.

All 12,023,630 assertions are enumerated by category in the canonical.
These finite executions pressure the independent all-parameter deductions
in [SOURCE_AND_PROOF.md](SOURCE_AND_PROOF.md); they do not prove general
`n,q` by extrapolation. Author and A executions are not relabelled as B
executions. Root's required independent replay pair is a later separate
obligation.
