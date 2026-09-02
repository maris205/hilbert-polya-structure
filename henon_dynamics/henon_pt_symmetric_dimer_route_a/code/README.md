# C297 exact programs

- `c297_pt_dimer_producer.py` writes the canonical exact receipt.
- `c297_pt_dimer_checker.py` independently reconstructs every cell and uses
  duplicate-rejecting JSON and YAML loaders.
- `c297_pt_dimer_sympy_crosscheck.py` derives the matrix, metric, Riccati, and
  propagator identities separately.
- `c297_pt_dimer_replay.py` demands two fresh byte-identical receipts.
- `c297_pt_dimer_mutation.py` runs repaired-hash and raw parser attacks.
- `c297_release_manifest.py` reruns all gates, validates all PDF rounds, and
  closes the exact file ledger.

The checker does not import the producer.  All commands use source-local
parameters and require no network access.
