# C232 executable chain

`c232_duffing_producer.py` writes the canonical high-precision JSON ledger.
`c232_duffing_checker.py` reconstructs all roots and quadratures independently.
`c232_duffing_sympy_crosscheck.py` checks the algebraic identities;
`c232_duffing_replay.py` checks clean byte replay;
`c232_duffing_mutation.py` runs hostile semantic/schema/stale-hash tests;
`c232_release_manifest.py` seals the payload ledger.
