# C263 code contract

`c263_polya_producer.py` emits exact `Fraction` ledgers for ordered words,
recursive and closed count compositions, marginals, covariance matrices,
factorial moments, conditional martingale identities, and Dirichlet mixture
moments.  `c263_polya_checker.py` imports no producer code and reconstructs all
identities independently.  The SymPy script verifies generic algebra and a
deterministic spread of stored rows.  Replay requires byte equality; mutation
requires rejection of repaired-hash semantic changes and a stale-hash change.
The release script reruns all gates and writes the self-excluded manifest.
