# Executable audit

- `c223_jaynes_cummings_producer.py` serializes the canonical exact/numerical
  excitation ledger.
- `c223_jaynes_cummings_checker.py` imports no producer, recursively closes
  the schema, reconstructs every block/propagator and directly checks a finite
  Fock commutator.
- `c223_jaynes_cummings_sympy_crosscheck.py` independently proves the Pauli
  square, characteristic, unitary, gauge and revival-parity identities.
- `c223_jaynes_cummings_replay.py` requires canonical byte reproduction in a
  clean subprocess.
- `c223_jaynes_cummings_mutation.py` repairs hashes after semantic/schema
  corruptions and separately attacks a stale hash.
- `c223_release_manifest.py` reruns all gates and freezes exactly 27 payload
  files plus its self-excluded manifest.

No network, target table or external dataset is used.
