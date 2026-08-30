# C250 code contract

`c250_ep_producer.py` emits the deterministic JSON receipt.  The checker does
not import it and reconstructs all formulas independently.  The SymPy script
checks the linear pair, Wronskian, energy, radial, discriminant, and invariant
identities.  Replay and mutation scripts test byte determinism and tamper
rejection.  `c250_release_manifest.py` is the final content-addressed gate.
