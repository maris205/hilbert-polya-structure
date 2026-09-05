# P205 Review A — actual independent producer and replay pair

2026-09-05 UTC. All commands below were executed, not merely proposed.
Working directory: `/root/autodl-tmp/symbolic_dynamics`.
Interpreter: **Python 3.12.3**. No randomness, environment-derived parameter,
network call, filesystem input or local research-module import is used by
the verifier. `-B` disables bytecode output. The complete dependency is the
new reviewer script plus this interpreter/standard-library behavior; the
source records are mathematical audit inputs, not execution inputs.

## Initial canonical production

```sh
python -B docs/papers204_208_sequence/reviews/p205_a/verify.py > docs/papers204_208_sequence/reviews/p205_a/CANONICAL.json
```

Actual process exit: **0**. The initial run was not seeded from author or
gate output. It produced the complete JSON retained as CANONICAL.json.
There were no failed checker versions or subsequently changed parameters.

## Two additional fresh producer/comparison executions

The following independent processes were launched concurrently. Within
each process, the producer was followed by `cmp` only on producer success.

```sh
python -B docs/papers204_208_sequence/reviews/p205_a/verify.py > docs/papers204_208_sequence/reviews/p205_a/run1.stdout 2> docs/papers204_208_sequence/reviews/p205_a/run1.stderr && cmp docs/papers204_208_sequence/reviews/p205_a/CANONICAL.json docs/papers204_208_sequence/reviews/p205_a/run1.stdout > docs/papers204_208_sequence/reviews/p205_a/run1.cmp.stdout 2> docs/papers204_208_sequence/reviews/p205_a/run1.cmp.stderr
python -B docs/papers204_208_sequence/reviews/p205_a/verify.py > docs/papers204_208_sequence/reviews/p205_a/run2.stdout 2> docs/papers204_208_sequence/reviews/p205_a/run2.stderr && cmp docs/papers204_208_sequence/reviews/p205_a/CANONICAL.json docs/papers204_208_sequence/reviews/p205_a/run2.stdout > docs/papers204_208_sequence/reviews/p205_a/run2.cmp.stdout 2> docs/papers204_208_sequence/reviews/p205_a/run2.cmp.stderr
```

| Execution | Python producer | Raw-byte comparator | Stderr / comparator output |
|---|---:|---:|---|
| Initial canonical | 0 | Not a replay | No error reported |
| Fresh replay 1 | 0 | 0 | All empty |
| Fresh replay 2 | 0 | 0 | All empty |

The two combined shell commands both actually completed with exit zero;
because each uses `&&`, this establishes both child-success and comparator
success. The comparisons consume the whole files without whitespace,
JSON-key or newline normalization. The entire [run 1 stdout](run1.stdout)
and [run 2 stdout](run2.stdout) remain in the package, including all boxes
and negative controls, not just an excerpt or final PASS line.

## Exact result and coverage

- Assertions per complete run: **11,265,033**, all PASS.
- Dynamical sources and full target sets: **315,093**.
- Literal orbit time points: **2,880,650**, each with coordinate,
  monotone-active-set and persistent-edge checks.
- All graphs: `n=0..5, q=3`; `n=0..4, q=4,5`; `n=0..3, q=7`.
- Static graphs: every labelled simple graph on `n=0..6`, **33,868** total.
- Sharp paths: every `n=2..30, q=3..13`, **319** cases.
- Complete recurrence uses whole-map leaf peeling, not trajectory cutoffs.
  Iterates are checked through each exact entrance plus two full periods.
- Every target's held-set reconstructed source set is compared with its
  complete literal incoming set. The maximum and all labelled graph/target
  equality cases are checked, including empty carriers and small orders.
- Six connected order-four counts are recomputed. Each inverse condition
  has an automatically found omission counterexample; the time-shift,
  orientation and same-active-mask controls are explicit in the canonical.

SHA256 values:

```text
verify.py       3a4cbce7210f93addc9a65bed2aef822b0cae3f859a9c93df66beb57f7bebeaa
CANONICAL.json  742ab7299ac4e44f15f42f56393abce02c41271164d1ae33a3b1cc80f093a626
record digest   da9196549676876a843e628f1ad921a872df262154bec9c9808406250e829e76
```

Each replay stdout has the canonical's SHA256, as well as passing raw
comparison. The `record digest` is a deterministic digest of every checked
state/static/path record, not the hash of the JSON file. All emitted output
is retained in CANONICAL.json; a digest is not represented as a missing
full producer transcript.

These are newly executed reviewer results, not a reuse of the candidate
7,530,194-check output or the paper author's 1,029,769-check record.
No finite box proves an all-parameter theorem or certifies novelty.
