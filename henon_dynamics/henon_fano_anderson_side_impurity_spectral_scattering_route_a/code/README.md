# C345 executable lanes

- `c345_fano_anderson_producer.py`: canonical exact JSON producer.
- `c345_fano_anderson_checker.py`: strict independent checker; it does not
  import or name the producer.
- `c345_fano_anderson_sympy_crosscheck.py`: independent symbolic lane,
  including anti-Herglotz sign and band-edge limit checks.
- `c345_fano_anderson_replay.py`: two-isolated-directory byte replay.
- `c345_fano_anderson_mutation.py`: repaired-hash hostile suite, strict parser
  attacks, spectral-measure-proof attacks, and exhaustive evaluator-leaf
  attacks.
- `c345_release_manifest.py`: PDF, scope, lane, ledger, and release gate.

Run with `PYTHONDONTWRITEBYTECODE=1`.  Every script intentionally refuses
optimized Python so that assertions cannot disappear under `-O` or `-OO`.
