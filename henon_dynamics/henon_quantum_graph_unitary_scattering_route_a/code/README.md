# C133 code map

- `c133_quantum_graph_producer.py`: deterministic exact evidence producer.
- `c133_quantum_graph_checker.py`: independent reconstruction; it imports no
  producer code.
- `c133_sympy_crosscheck.py`: block-determinant and Newton-series cross-check.
- `c133_replay.py`: byte-for-byte producer replay.
- `c133_mutation.py`: 48 repaired-hash semantic mutations plus one stale-hash
  mutation.
- `c133_release_manifest.py`: content-addressed closed release ledger.

Run all commands from the package root.  No random input, external data,
floating acceptance tolerance, prime table, or zero table is used.
