# C320 executable lanes

- `c320_darboux_halphen_producer.py`: independent rational-series arithmetic,
  high-precision theta tests, modular-generator tests, and collision receipts.
- `c320_darboux_halphen_checker.py`: strict parser plus independent SymPy and
  100-digit theta reconstruction; it imports no producer code.
- `c320_darboux_halphen_sympy_crosscheck.py`: Chazy, discriminant,
  covariance, and collision identities.
- `c320_darboux_halphen_replay.py`: isolated byte replay.
- `c320_darboux_halphen_mutation.py`: repaired-digest and YAML attacks.
- `c320_release_manifest.py`: executable/PDF/file-ledger release gate.

All executable lanes explicitly refuse optimized Python.
