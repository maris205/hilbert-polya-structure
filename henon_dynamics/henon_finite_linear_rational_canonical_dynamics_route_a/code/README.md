# Code map

- `c204_finite_linear_producer.py`: deterministic exact ledger.
- `c204_finite_linear_checker.py`: independent matrix-rank/graph checker; it
  does not import producer code.
- `c204_finite_linear_sympy_crosscheck.py`: polynomial-gcd and Koopman checks.
- `c204_finite_linear_replay.py`: temporary byte-for-byte regeneration.
- `c204_finite_linear_mutation.py`: 17 repaired-hash and one stale-hash attack.
- `c204_release_manifest.py`: self-excluded 27-payload release closure.
