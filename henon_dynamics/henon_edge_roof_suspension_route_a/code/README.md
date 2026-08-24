# C135 code

- `c135_edge_roof_producer.py`: formal determinant, exact trace dictionaries,
  primitive ledger, separation and collision receipts.
- `c135_edge_roof_checker.py`: independent standard-library reconstruction;
  imports no producer code.
- `c135_sympy_crosscheck.py`: independent symbolic determinant, Laplace
  specialization, radical, and trace-coefficient checks.
- `c135_replay.py`: byte-for-byte producer replay.
- `c135_mutation.py`: 42 repaired-payload-hash semantic mutations plus one
  stale-hash mutation.
- `c135_release_manifest.py`: self-excluded 27-payload release ledger.

No network or external dataset is required.
