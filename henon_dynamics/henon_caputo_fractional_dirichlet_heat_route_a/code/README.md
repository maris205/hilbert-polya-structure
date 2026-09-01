# C277 executable certificate

Run the producer, producer-independent checker, symbolic audit, byte replay,
hostile mutations, and release closure in this order:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c277_caputo_producer.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c277_caputo_checker.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c277_caputo_sympy_crosscheck.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c277_caputo_replay.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c277_caputo_mutation.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c277_release_manifest.py
```

The producer evaluates the defining Mittag–Leffler series only on its stable
`0<=x<=1` audit range.  The checker independently recomputes those values in
double precision.  Large-time cells use the separate exact identity
`E_(1/2)(-x)=exp(x^2)erfc(x)` and SciPy's independent scaled-complementary-error
implementation.

The smoothing ledger samples only its declared `theta>=0` domain.  The
checker freezes the exact quantified iff contract and the separate statement
that `theta<0` is bounded because `A>=I` but is outside that domain.
