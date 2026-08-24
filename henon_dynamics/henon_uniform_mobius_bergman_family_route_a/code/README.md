# C137 code map

- `c137_uniform_mobius_producer.py` emits the canonical exact evidence object.
- `c137_uniform_mobius_checker.py` independently reconstructs all 18,414 grid-word receipts and closes every evidence schema layer.
- `c137_sympy_crosscheck.py` separately verifies the symbolic matrix, trace, nuclear, Lipschitz, and fixed-point identities.
- `c137_replay.py` demands byte-identical regeneration.
- `c137_mutation.py` repairs hashes for semantic attacks and includes one stale-hash control.
- `c137_release_manifest.py` creates the self-excluded 27-payload release ledger.

The checker does not import the producer.  All theorem quantities are exact integers or rationals; the nine-point grid is a deterministic replay sentinel, not the basis of the uniform theorem.
