# C145 code

- `c145_rule90_producer.py`: bit-polynomial `F_2` gcd evidence producer.
- `c145_rule90_checker.py`: independent binary-matrix/rank and direct-state
  checker; imports no producer code.
- `c145_sympy_crosscheck.py`: full `Poly(...,modulus=2)` gcd path.
- `c145_replay.py`: isolated byte-identity replay.
- `c145_mutation.py`: semantic repaired-hash and stale-hash audit.
- `c145_release_manifest.py`: self-excluded 27-file release ledger.

All counts are exact integers.  The `24 x 24` cutoff is a replay ledger, not a
theorem cutoff.
