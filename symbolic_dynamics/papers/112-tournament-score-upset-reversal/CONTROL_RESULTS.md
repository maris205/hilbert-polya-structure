# Exact control results — P112

Status: **PASS / finite falsification evidence / external HOLD**.

Command:

```text
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py
```

Result:

- status: **PASS**;
- exact assertions: **1,677,508**;
- labelled tournament states: **33,868**, namely every state for
  `0 <= n <= 6`;
- implementations: bit-coded update and a separate literal set-of-arcs
  update;
- arithmetic: exact integers only, with no random seed, floating point,
  symbolic simplifier, or external package.

Complete lane summary:

| `n` | phase | fixed | maximum observed depth | depth histogram |
|---:|---:|---:|---:|---|
| 0 | 1 | 1 | 0 | `{0:1}` |
| 1 | 1 | 1 | 0 | `{0:1}` |
| 2 | 2 | 2 | 0 | `{0:2}` |
| 3 | 8 | 8 | 0 | `{0:8}` |
| 4 | 64 | 40 | 1 | `{0:40,1:24}` |
| 5 | 1,024 | 264 | 1 | `{0:264,1:760}` |
| 6 | 32,768 | 2,048 | 2 | `{0:2048,1:26400,2:4320}` |

The independently counted regular-tournament sequence through order six is
`[0,1,0,2,0,24,0]`, using `r_0=0`.  Substitution in the fixed recurrence
gives `[1,1,2,8,40,264,2048]`, exactly matching direct fixed-state counts.

The active counterexample search loops over increasing orders and then
increasing numerical masks.  In that specified finite scan, the least
nonidempotent state is `n=6`, mask `148`, with edges listed lexicographically
and bit one meaning that the smaller endpoint wins:

```text
148, scores (2,2,2,2,3,4)
  -> 4, scores (1,1,2,2,4,5)
  -> 0, scores (0,1,2,3,4,5)
  -> 0.
```

The stored stdout is `code/verification_output.txt`.  These lanes test and
falsify finite instances; the manuscript proofs establish the stated
infinite-family results.  The word “least” above is scan-dependent; these data
do not establish a sharp global depth function.

Repair-stage regression: a fresh standard-library process was compared with
the stored **781-byte** transcript using bytewise `cmp`; the comparison was
identical.  The output label is
`least_nonidempotent_in_specified_scan`, matching the qualified claim.
