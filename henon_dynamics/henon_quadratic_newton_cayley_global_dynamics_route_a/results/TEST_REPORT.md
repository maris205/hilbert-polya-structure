# HCS-C257 test report

All commands were run from the package root with Python bytecode disabled.

```text
python3 -B code/c257_newton_producer.py
  C257_PRODUCER_PASS; 16 period rows; 128 root-order rows

python3 -B code/c257_newton_checker.py
  C257 independent checker: PASS (1317 assertions)

python3 -B code/c257_newton_sympy_crosscheck.py
  C257_SYMPY_PASS (88 symbolic identities)

python3 -B code/c257_newton_replay.py
  C257 byte replay: PASS

python3 -B code/c257_newton_mutation.py
  C257 hostile mutations: PASS 41/41
```

The checker is producer-independent and recomputes Möbius inversion,
multiplicative orders, exact rational iterates, schema closure, provenance,
evaluator tuple, and every scope flag.  The SymPy program independently
reconstructs the Möbius conjugacy, inverse, critical points, both error
identities, Julia-line map, cycle multipliers, and zeta logarithmic
coefficients.

PDF gates: three distinct revisions, two fresh two-pass builds per revision,
byte determinism within each revision, final equals round 2, 2 A4 pages, 24
embedded/subset font records, clean logs, extractable text, and visual pass.
