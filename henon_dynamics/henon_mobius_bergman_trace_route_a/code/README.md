# Code

- `c132_mobius_bergman_producer.py`: exact geometry, word-matrix, and trace receipt.
- `c132_mobius_bergman_checker.py`: independent reconstruction; no producer import.
- `c132_sympy_crosscheck.py`: separate symbolic matrix and bound checks.
- `c132_replay.py`: byte-for-byte producer replay.
- `c132_mutation.py`: 36 repaired-hash semantic mutations plus one stale-hash
  mutation.
- `c132_release_manifest.py`: content-addressed 27-payload ledger.
