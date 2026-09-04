# Reproducibility

From the package root, run:

```bash
python -B code/c372_kirchhoff_love_producer.py
python -B code/c372_kirchhoff_love_checker.py
python -B code/c372_kirchhoff_love_sympy_crosscheck.py
python -B code/c372_kirchhoff_love_replay.py
python -B code/c372_kirchhoff_love_mutation.py
python -m unittest tests/test_c372_smoke.py
python -B code/c372_release_manifest.py --write --build-pdfs
python -B code/c372_release_manifest.py
```

The producer uses exact `Fraction` arithmetic.  The checker never imports
it: it rebuilds the reduced rational grid, computes modal squares from the
unfactorized Love formula, locates threshold dyadics by integer binary
search, and reconstructs all invariants.  The SymPy lane checks the interior
velocity, normal boundary motion, modal factorization, symmetry modes,
derivatives, threshold ordering, singular faces, exact brackets, and period
conventions.  Replay builds the evidence twice in isolated directories; the
mutation suite repairs the payload hash after semantic attacks.

The release gate strictly parses JSON/YAML, refuses optimized Python, locks
the evaluator, builds each conditional manuscript round twice under epoch
`1788480000`, rejects warnings, checks fonts/text/rasterization, and closes
the exact self-excluding manifest.
