# P207 manuscript A — actual independent replay log

2026-09-06 UTC. Five actual independent reviewer executions completed:
one initial production and **two additional fresh pairs**, not two aliases
of one pair. Each passed 1,326,321 assertions and printed the same complete
37,971-byte canonical JSON. All ten actual raw `cmp` commands exited zero.
No author, gate or old verifier was imported or executed for these runs.

## Producer and dependence boundary

`verify.py` is a new standalone Python implementation by nonauthor reviewer
`batch197_lzk_gate`. It transparently reuses this same reviewer's earlier
gate algorithms (direct 13-height cones, the 81-height graph, the full
TCSD union); it is not presented as a new independent candidate assessor
or blind review. It contains no input-file read, repository import,
canonical read, random choice, native helper or network operation.
Only `collections`, `hashlib`, `itertools` and `json` are imported.
All arithmetic is arbitrary-precision integer arithmetic.

| Item | Exact value / SHA-256 |
|---|---|
| Independent source | `2b0e0d9c0bde25c7f9e5dc132b15d58f8ab20f6760c6898ba6abf12e330b5ee2` |
| Execution recorder | `f4f1d808f2248232a30d2cd2e75ff83444186693ed319c2523dcc13ae7720fb9` |
| Complete canonical stdout | `d4c1f4264d628f38c83d85e0532d036056fad89695ab399e25c9d19e6d09243e` |
| Ordered checked-record SHA-256 | `39f191682bb63507e7a5e423031d56e3c3642b696251778be44c111d8aa8f390` |
| Full freeze pin list | `272971bf814b500c3f70672eddf593cdfa4cc433a716662a0e4cf3f0b2305717` |
| Interpreter | `/root/miniconda3/bin/python3.12`, Python 3.12.3 |
| Interpreter executable SHA-256 | `9a3d9e94d2be60d9a2a91d08f62292a152e28175fb4ee1d871aa5850fbb7a101` |

The recorder separately reads and pins inputs, captures complete stdout
and stderr, and runs the raw comparisons. It removes inherited
PYTHONPATH/PYTHONHOME without displaying their contents, and sets
`LC_ALL=C`, `TZ=UTC`, `PYTHONHASHSEED=0`, `PYTHONDONTWRITEBYTECODE=1`,
`PYTHONSAFEPATH=1`. Each child runs with `-B` in its own new directory
containing a byte-pinned independent source copy. Interpreter version,
platform and actual `ldd` dependency output are retained per attempt;
there is no unpinned reviewer-created native math binary.

## Actual commands and runs

Working directory for these recorder commands was the workspace root.
The pair attempts were allowed to run concurrently, while the two children
within each pair were fresh sequential processes in distinct directories.

```sh
python3 -B docs/papers204_208_sequence/reviews/p207_a/record_review.py initial
python3 -B docs/papers204_208_sequence/reviews/p207_a/record_review.py pair_01
python3 -B docs/papers204_208_sequence/reviews/p207_a/record_review.py pair_02
```

| Execution | Actual UTC interval | Seconds | Assertions | Exit |
|---|---|---:|---:|---:|
| Initial run 0 | 07:27:18.739–07:27:42.710 | 23.971 | 1,326,321 | 0 |
| Pair 01 run 1 | 07:28:15.673–07:28:39.939 | 24.266 | 1,326,321 | 0 |
| Pair 01 run 2 | 07:28:39.943–07:29:03.969 | 24.026 | 1,326,321 | 0 |
| Pair 02 run 1 | 07:28:16.873–07:28:40.772 | 23.899 | 1,326,321 | 0 |
| Pair 02 run 2 | 07:28:40.777–07:29:04.709 | 23.932 | 1,326,321 | 0 |

The [initial receipt](execution/initial/RECEIPT.json),
[first pair receipt](execution/pair_01/RECEIPT.json) and
[second pair receipt](execution/pair_02/RECEIPT.json) retain every child
argument, cwd, start/end time, duration, exit and stream hash. Each child
stdout and all comparison streams are retained in full. Producer stderr
and every comparator stream are empty. The initial attempt has two `cmp`
commands; each pair has four: both children against its canonical snapshot,
the children against each other, and live canonical against its snapshot.
All are byte comparisons, not JSON normalization or matching summaries.

Before and after each attempt, the complete 106-entry freeze input set,
the producer, recorder and freeze-pin file were rehashed: all 109 inputs
were unchanged. The ten additional context/source pins are separate;
they are not file inputs to the mathematical producer. Each execution
attempt has its own complete nonself manifest. The overall review manifest
also covers all attempts, canonical, reports and auxiliary evidence.

## Scope and results

| Section | Passing assertions per execution | Actual finite scope |
|---|---:|---|
| Direct local certificate | 333,254 | All 3^13 height words, full cones and new-extremum witness domains |
| Independent core graph | 84 | All 81 vertices, 137 edges, powers 1–81 and full Newton determinant |
| Complete cyclic source/target/sign boxes | 989,612 | Every source, target and sign word for n=3,…,10 |
| Seed only | 3,371 | Exact stipulated wave/source profiles, n=4,…,64 |
| Total | 1,326,321 | No full cyclic box above n=10 |

The complete boxes have core counts `13,11,21,63,85,155,373,613`, observed
heights `1,5,5,5,5,5,5,6`, and maximum fibres `3,7,7,18,18,47,47,123`.
All attaining labelled targets, including seven at n=3 and both odd
families, are printed in the canonical. Every sign stratum is evaluated
from the original TCSD Fibonacci-gap theorem, then aggregated to every
whole rank-target fibre; actual source **sets**, not only cardinalities,
are compared. The canonical preserves full histograms, all graph data,
all 82 characteristic coefficients and the explicit two-stratum example.

The author's independent-in-form representation is different: inner-cone
factorization, eight temporal roles, kernel decoder and Kahn graph pruning.
The separate read-only [author artefact audit](AUTHOR_ARTIFACT_AUDIT.json)
passed 6,562 checks, validating all 106 physical frozen files (50 distinct
byte contents), nested 105/85/30/36/9 manifests, 17 preserved provenance
copies per author attempt, full recorded streams, all author inner cases
and all 1,836 explicit extension witnesses. Its code reads canonical data
to audit those artefacts; it is **not** one of the five independent producer
runs and is not counted in their assertions.

No independent mathematical producer, recorder or artefact audit failed
in these attempts. A read-only `sed` initially used the wrong batch path
for TCSD and exited two; the corrected original was then fully read.
`rg` returned one with empty output on the clean-PDF marker search, meaning
no marker hit, not a build failure. Historical author shorter-cone/test
failures and the earlier gate compile failure remain preserved elsewhere.
No failure or alias has been relabelled as a successful numerical run.

These computations check the finite premise and pressure the all-n proof;
they do not prove a sharp global clock or close a source-access issue.
They are manuscript A evidence, not accepted delta/B/terminal-gate evidence.
Root must use a new root-owned replay location if replaying this source;
do not append runs inside these closed attempts. `HOLD_EXTERNAL`.
