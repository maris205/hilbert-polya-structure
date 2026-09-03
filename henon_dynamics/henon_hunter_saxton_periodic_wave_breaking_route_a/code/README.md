# C324 executable lanes

- `c324_hunter_saxton_producer.py` emits the canonical finite evidence.
- `c324_hunter_saxton_checker.py` independently reconstructs every owned field
  and strictly parses both JSON and evaluation YAML.
- `c324_hunter_saxton_sympy_crosscheck.py` checks the Riccati, Jacobian, and
  transformed-energy identities without importing producer code.
- `c324_hunter_saxton_replay.py` performs two isolated byte reproductions.
- `c324_hunter_saxton_mutation.py` attacks mathematical values, nested schemas,
  repaired hashes, nonfinite JSON, and hostile YAML.
- `c324_release_manifest.py` rebuilds the complete package and writes or checks
  the self-excluding 27-payload release manifest.

All Python lanes explicitly refuse optimized (`python -O`) execution.
