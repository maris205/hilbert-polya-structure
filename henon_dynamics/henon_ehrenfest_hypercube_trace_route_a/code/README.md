# C171 exact code

- `c171_ehrenfest_producer.py`: deterministic exact JSON producer.
- `c171_ehrenfest_checker.py`: producer-independent formulas, Krawtchouk
  recurrence and small-cube closed-walk enumeration.
- `c171_sympy_crosscheck.py`: independent symbolic characteristic-polynomial
  and eigenvector reconstruction.
- `c171_replay.py`: byte-for-byte producer replay.
- `c171_mutation.py`: repaired-hash semantic and stale-hash attacks.
- `c171_release_manifest.py`: self-excluded content-addressed release ledger.

The scripts use no target or external dataset.  The finite ledgers are
regression sentinels and are not substituted for the all-parameter proof.
