# C146 exact code

- `c146_heisenberg_producer.py` builds the canonical iterate-20 evidence.
- `c146_heisenberg_checker.py` independently reconstructs group, lattice,
  matrix, Lucas, stability, Lefschetz, and counterexample receipts.
- `c146_sympy_crosscheck.py` supplies an independent symbolic reconstruction.
- `c146_replay.py` demands byte-identical producer replay.
- `c146_mutation.py` repairs semantic hashes before hostile rejection and also
  tests a stale hash.
- `c146_release_manifest.py` closes exactly 27 payload files and excludes
  itself and transient build artifacts.

All mathematical calculations use exact integers, rational arithmetic, or
symbolic algebra.  No network or target data is used.
