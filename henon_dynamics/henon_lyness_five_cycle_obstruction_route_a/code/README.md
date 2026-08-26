# C173 code contract

- `c173_lyness_producer.py` writes the canonical exact evidence ledger.
- `c173_lyness_checker.py` independently reconstructs rational orbits and
  validates every claim-bearing field without importing the producer.
- `c173_sympy_crosscheck.py` reconstructs the rational identities,
  invariant density, reversor, and cyclic projection algebra symbolically.
- `c173_replay.py` regenerates the JSON in a temporary directory and demands
  byte identity.
- `c173_mutation.py` repairs payload hashes after hostile semantic changes
  and confirms that the independent checker still rejects them.
- `c173_release_manifest.py` hashes the 27 payload files and excludes only
  itself and declared build caches.

All commands use exact rational or symbolic arithmetic.  The rational grid
and (n\le50) fixed-set ledger are regression sentinels, not proofs.
