# Code lanes

- `c365_gelfand_tsetlin_producer.py`: canonical exact receipt producer.
- `c365_gelfand_tsetlin_checker.py`: independent reconstruction, including exact basepoint/coset-equality witnesses; it never imports the producer.
- `c365_gelfand_tsetlin_sympy_crosscheck.py`: symbolic arrow, dimension, KKS/moment-pairing, projector-period, and basepoint-witness checks.
- `c365_gelfand_tsetlin_replay.py`: two-isolated-directory byte replay.
- `c365_gelfand_tsetlin_mutation.py`: repaired-hash hostile suite and stale-hash control.
- `c365_release_manifest.py`: deterministic 27-payload release gate.

Every script refuses optimized Python (`-O` and `-OO`).
