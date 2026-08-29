# Exact control results — P110

Status: **FINAL MECHANICAL QA REPLAY PASS / EXTERNAL HOLD**.

Command:

```text
python3 code/verify.py
```

Fresh output: **CONTROL_OUTPUT.txt**.

Result freshly replayed again during final QA on 2026-08-29 UTC:

- status: **PASS**;
- exact assertions: **1,916,206**;
- literal partitions: **142,417**, namely every state in `Pi_1` through
  `Pi_10`;
- closed basin and divisor-convolution lanes: **PASS** through `n=50`;
- exhaustive binary-cut defect lanes: **PASS** through `n=12`;
- temporal Möbius and formal-zeta reconstruction: **PASS** through period
  `60`.
- stored-output comparison: **byte-identical** to `CONTROL_OUTPUT.txt`.
- canonical fresh/stored stdout SHA-256:
  `8b88fb8202b063ee843eb5941ed57a373b8941f1759c5d334447105913d01ab3`.

Selected exhaustive lanes are:

| `n` | `Bell(n)` | fixed | depths from `0` upward | deepest | basins by subgroup order |
|---:|---:|---:|---|---:|---|
| 4 | 15 | 3 | `3,8,4` | 4 | `{1:1,2:3,4:11}` |
| 5 | 52 | 2 | `2,30,10,10` | 10 | `{1:1,5:51}` |
| 6 | 203 | 4 | `4,115,66,12,6` | 6 | `{1:1,2:7,3:24,6:171}` |
| 7 | 877 | 2 | `2,476,280,77,21,21` | 21 | `{1:1,7:876}` |
| 8 | 4,140 | 4 | `4,2224,1440,368,64,24,16` | 16 | `{1:1,2:15,4:209,8:3915}` |
| 9 | 21,147 | 3 | `3,11439,7482,1710,360,99,27,27` | 27 | `{1:1,3:124,9:21022}` |
| 10 | 115,975 | 4 | `4,62911,42570,8175,1785,380,90,40,20` | 20 | `{1:1,2:31,5:2703,10:113240}` |

The program uses three convention-separated realizations:

1. union–find for the literal partition join and update;
2. a separately accumulated join of original translates; and
3. direct graph construction followed by depth-first connected components.

It also constructs subgroup endpoints from residue classes, evaluates the
Möbius–Bell formula independently of literal indegrees, and classifies every
deepest state by its block structure and primitive difference.  A separate
lane exhausts every nonconstant binary cut through `n=12`, checking the exact
two-defect set for primitive chords, the absence of defects for admissible
nonprimitive chords, trivial cut stabilizers, and uniqueness of an admissible
primitive chord.  All arithmetic is exact.  The control uses no random seed,
floating point, computer algebra, symbolic simplifier, or optimization solver.
It is finite evidence; the manuscript proofs establish the infinite family.
