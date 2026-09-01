# Executable certificate

- `c283_padic_producer.py`: deterministic 438-cell receipt; high-precision
  analytic sums and finite character FFT/filtration comparisons.
- `c283_padic_checker.py`: standalone semantic reconstruction and strict schema
  checker; it imports no producer function.
- `c283_padic_sympy_crosscheck.py`: exact rational finite-quotient projections,
  spectra, zeta derivatives, residues, and finite geometric sums.
- `c283_padic_replay.py`: fresh-path byte replay.
- `c283_padic_mutation.py`: repaired-hash hostile semantic attacks plus stale
  hash and unknown-schema attacks.
- `c283_release_manifest.py`: exact file-set, script, evaluation, PDF, font,
  text, deterministic-build, and Example 5.1/arXiv:1511.02146 direct-owner
  closure gate.

All scripts are run with `python3 -B` and `PYTHONDONTWRITEBYTECODE=1` so the
release directory remains free of sidecars.
