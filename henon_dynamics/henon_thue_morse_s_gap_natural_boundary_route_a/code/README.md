# C159 code

- `c159_s_gap_producer.py` writes the canonical exact evidence.
- `c159_s_gap_checker.py` independently enumerates cyclic words and rebuilds
  every finite renewal coefficient with standard-library arithmetic.
- `c159_sympy_crosscheck.py` reconstructs the formal product and logarithmic
  derivative identities through degree 24.
- `c159_replay.py` requires byte-identical regeneration.
- `c159_mutation.py` repairs hashes after semantic changes and requires the
  checker to reject every changed claim, plus one stale-hash control.
- `c159_release_manifest.py` builds the final self-excluded release ledger.

Run all commands from the repository root.  No script reads target zero or
prime tables, arithmetic/local factors, or Route-B inputs.
