# C138 code map

- `c138_magnetic_graph_producer.py` emits the exact magnetic theta-graph certificate and oriented orbit-ledger digests.
- `c138_magnetic_graph_checker.py` independently reconstructs the Laurent determinant, all controls, 14,760 rooted walks, and 1,905 primitive cycles.
- `c138_sympy_crosscheck.py` supplies a separate block-determinant and antiunitary calculation.
- `c138_replay.py` demands byte-identical evidence regeneration.
- `c138_mutation.py` applies repaired-hash semantic attacks plus one stale-hash control.
- `c138_release_manifest.py` builds the self-excluded 27-payload release ledger.

The checker never imports the producer.  Individual oriented phases remain Laurent monomials in the ledger; only the complete determinant is tested for flux-reversal evenness.
