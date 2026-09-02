# Code contract

- `c295_isochrone_producer.py` writes deterministic exact evidence using quadratic-field coefficients and 60-digit decimal controls.
- `c295_isochrone_checker.py` is producer-independent.  It enforces exact JSON/YAML schemas and types, rejects duplicate/nonfinite JSON and duplicate/non-string/anchor/alias/merge YAML, reconstructs all cells, and performs direct high-precision quadratures.
- `c295_isochrone_sympy_crosscheck.py` independently verifies the circular, Vieta, action-frequency, apsidal, closure-grid, escape, and Kepler identities.
- `c295_isochrone_replay.py` reproduces evidence in two isolated paths and requires byte identity.
- `c295_isochrone_mutation.py` launches repaired-hash semantic attacks and raw parser attacks against both evidence and evaluation.
- `c295_release_manifest.py` repeats all gates, performs two clean builds of each of three substantive paper rounds, checks exact package membership, and writes the self-excluded manifest.

Run with Python 3 from the package root.  The checker deliberately does not import the producer.  Build intermediates and Python bytecode are forbidden from the release tree.
