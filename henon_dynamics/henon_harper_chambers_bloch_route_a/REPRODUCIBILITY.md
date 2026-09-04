# Reproducibility

Run from this directory with ordinary, nonoptimized Python:

```bash
python -B code/c371_harper_producer.py
python -B code/c371_harper_checker.py
python -B code/c371_harper_sympy_crosscheck.py
python -B code/c371_harper_replay.py
python -B code/c371_harper_mutation.py
python -m unittest tests/test_c371_smoke.py
python -B code/c371_release_manifest.py --write --build-pdfs
python -B code/c371_release_manifest.py
```

The producer obtains the Chambers polynomial by multiplying transfer
matrices with polynomial entries.  The checker never imports the producer;
it reconstructs the polynomial from a reference Hermitian fiber
characteristic polynomial and rebuilds every dense fiber.  The SymPy lane
uses an exact implementation of `Q[zeta_q]/Phi_q` and verifies the permitted
phase support, extreme coefficients, parity, duality, reversal, and central
edge for all reduced `q<=10` with symbolic anisotropy degree.  These are
finite exact checks; the all-denominator central value is sourced from
Lamoureux--Mingo, Theorem 2.5 and Corollary 2.6.

The replay performs two isolated byte-identical evidence builds.  The
hostile suite repairs the inner payload hash after semantic mutations.  The
release gate refuses `python -O` and `python -OO`, strictly parses JSON and
YAML, runs the smoke suite, builds every conditional manuscript twice at
epoch `1788480000`, rejects warnings, checks embedded subset fonts, extracts
text, rasterizes all pages, and closes a self-excluding 35-payload manifest.
