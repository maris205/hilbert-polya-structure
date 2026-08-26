# C180 executable contract

- `c180_lattes_producer.py` writes canonical exact evidence.
- `c180_lattes_checker.py` independently reconstructs every formula, torsion quotient, and Wold row.
- `c180_sympy_crosscheck.py` checks the algebra, formal zeta, Möbius ledger, and Fourier-chain identities with SymPy.
- `c180_replay.py` demands byte-identical producer replay.
- `c180_mutation.py` applies repaired-hash semantic corruptions plus a stale-hash corruption.
- `c180_release_manifest.py` validates the Route-A v0.2 source lock and axis artifact paths, then closes the 27-file payload ledger while excluding itself and transient TeX files.

All commands use exact arithmetic. The checker deliberately imports no producer module. Finite cutoffs are regression sentinels, not theorem hypotheses.
