# Experiment plan

| claim | exact theorem | independent evidence |
|---|---|---|
| unitarity and reversal | involution algebra for `S`, `C`, `Theta=CK` | rational matrix identities |
| signed orbit expansion | trace logarithm and primitive path regrouping | all rooted paths through clock 10 |
| order sensitivity | exact two determinant polynomials | SymPy determinant and factorized difference |
| averaging failure | exact `Cbar^T Cbar-I` | independent rational reconstruction |

## Frozen replays

- dimension: 10;
- trace moments: 12 for each arrangement;
- signed rooted and primitive path ledgers: clocks 1--10;
- repaired-hash semantic mutations plus one stale-hash sentinel.

## Commands

```bash
python3 code/c143_quantum_walk_producer.py
python3 code/c143_quantum_walk_checker.py
python3 code/c143_sympy_crosscheck.py
python3 code/c143_replay.py
python3 code/c143_mutation.py
```

The independent checker imports no producer module.  Finite walks test the
implementation; the matrix identities and trace-logarithm proof are
all-clock statements.
