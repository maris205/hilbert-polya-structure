# Code contract

- `c303_thermal_qubit_producer.py` emits the canonical 124-row evidence JSON.
- `c303_thermal_qubit_checker.py` independently reconstructs every exact cell,
  validates threshold brackets, rejects duplicate/nonfinite JSON, and checks an
  exact-type, duplicate/anchor/merge-safe Route-A YAML tree.  It does not import
  the producer.
- `c303_thermal_qubit_sympy_crosscheck.py` independently derives the generator,
  characteristic polynomial, flow, Choi minors, threshold closed form, and
  Bloch singular values.
- `c303_thermal_qubit_replay.py` requires byte-identical regeneration.
- `c303_thermal_qubit_mutation.py` repairs payload hashes after semantic attacks
  and requires all attacks to be rejected.
- `c303_release_manifest.py` reruns every gate, rebuilds each paper round twice
  in isolated directories, and closes the 27-payload ledger.

Run with Python bytecode disabled.  No network, random seed, or training data
is needed.
