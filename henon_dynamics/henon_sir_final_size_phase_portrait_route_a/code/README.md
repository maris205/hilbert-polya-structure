# C198 executable certificate

```bash
python c198_sir_producer.py
python c198_sir_checker.py
python c198_sir_sympy_crosscheck.py
python c198_sir_replay.py
python c198_sir_mutation.py
```

The producer evaluates both real Lambert branches at high precision.  The
checker is deliberately Lambert-free: Python `Decimal` logarithms and monotone
bisection independently recover the lower and upper intersections of every
phase curve.  SymPy separately proves the invariant, scaling, peak,
linearization and sensitivity identities.  The evidence contains no clinical
or fitted outbreak data and is not medical advice.
