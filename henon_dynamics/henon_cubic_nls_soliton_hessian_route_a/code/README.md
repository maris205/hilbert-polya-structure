# Code map

- `c221_nls_producer.py` — emits the canonical exact/decimal receipt.
- `c221_nls_checker.py` — producer-independent recursive schema and value audit.
- `c221_nls_sympy_crosscheck.py` — symbolic profile, integral, kernel and factorization checks.
- `c221_nls_replay.py` — clean-process byte replay.
- `c221_nls_mutation.py` — repaired-hash semantic, unknown-key and stale-hash hostile tests.
- `c221_release_manifest.py` — validates the 28-file contract and writes the self-excluded manifest.

The numerical scripts use exact `fractions.Fraction` labels and high-precision
`mpmath` only for displayed values and derivative residuals.  The checker does
not import producer functions, and no finite-box diagonalization is used as a
continuum proof.
