# C272 executable certificate

Run the producer, independent checker, symbolic reconstruction, byte replay,
hostile mutations, and release manifest in that order:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c272_age_producer.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c272_age_checker.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c272_age_sympy_crosscheck.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c272_age_replay.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c272_age_mutation.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c272_release_manifest.py
```

The checker reconstructs every polynomial and root without importing producer
code.  It separately audits the `L1` eigenvalue gate, which prevents a formal
Euler–Lotka denominator root below the essential edge from being mislabeled as
an eigenvalue.
