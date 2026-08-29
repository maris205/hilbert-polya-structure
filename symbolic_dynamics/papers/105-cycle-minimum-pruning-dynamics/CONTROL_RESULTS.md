# Exact control results — P105

Command:

```text
python3 code/verify_cycle_minimum_pruning.py
```

Stored output: **CONTROL_OUTPUT.txt**.

Result on 2026-08-29 UTC:

- status: **PASS**;
- exact assertions: **17,219,241**;
- literal permutations: **409,113**, namely every state in `S_1` through
  `S_9`;
- nontrivial literal trajectory-step evaluations: **1,981,326**, counted
  with repetitions when different starting states traverse the same
  functional-graph edge;
- states whose literal indegree was compared with the closed fiber formula:
  **409,113**;
- restricted-cycle recurrence and all endpoint layers: **PASS** through
  `n=50`;
- temporal Möbius and formal-zeta reconstruction: **PASS** through period
  `60`.

The first registered depth histograms are:

| `n` | depth counts from `0` through `n-1` |
|---:|---|
| 4 | `1, 9, 8, 6` |
| 5 | `1, 25, 40, 30, 24` |
| 6 | `1, 75, 200, 180, 144, 120` |
| 7 | `1, 231, 980, 1260, 1008, 840, 720` |
| 8 | `1, 763, 5152, 8820, 8064, 6720, 5760, 5040` |
| 9 | `1, 2619, 28448, 61236, 72576, 60480, 51840, 45360, 40320` |

The program uses only finite permutations, integers, and exact rational
numbers.  It uses no random seed, floating-point theorem check, computer
algebra system, symbolic simplifier, or optimization solver.  Computation is
a convention-sensitive finite control; the manuscript proofs establish the
infinite family.
