# Code

- `c131_odd_metaplectic_producer.py`: exact integer/modular family receipt.
- `c131_odd_metaplectic_checker.py`: independent checker; it does not import the producer.
- `c131_sympy_crosscheck.py`: separate symbolic reconstruction.
- `c131_replay.py`: byte-for-byte deterministic replay.
- `c131_mutation.py`: 29 repaired-hash semantic/schema mutations plus one
  stale-hash checksum mutation.
- `c131_release_manifest.py`: content-addressed 27-payload release ledger.
