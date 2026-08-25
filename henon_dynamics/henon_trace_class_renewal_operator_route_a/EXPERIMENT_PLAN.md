# Experiment plan

## Claim--evidence matrix

| claim | analytic evidence | replay evidence | hostile control |
|---|---|---|---|
| `T` is trace class | exact singular-value sums for `S` and rank-one norm for `R` | finite sections through size 14 | constant-weight advance is noncompact |
| determinant is the renewal series | rank-one Fredholm factorization | exact determinants of sizes 1--10 | determinant convention mutations |
| trace and primitive ledgers agree | logarithmic derivative and repetition regrouping | traces through 12; primitive clocks through 10 | coefficient, word, and count mutations |
| determinant is entire of order zero | coefficient-order formula | 16 exact coefficients | order-label mutation |

## Commands

```bash
python3 code/c142_renewal_producer.py
python3 code/c142_renewal_checker.py
python3 code/c142_sympy_crosscheck.py
python3 code/c142_replay.py
python3 code/c142_mutation.py
```

The checker imports no producer code.  SymPy reconstructs finite determinants
from fresh matrices.  Replay compares canonical bytes.  Mutation testing
repairs the payload hash for semantic attacks and retains one stale-hash
sentinel.
