# C110 verification code

`c110_nonautonomous_producer.py` writes the canonical exact ledger.
`c110_nonautonomous_checker.py` independently rebuilds it.
`c110_sympy_crosscheck.py` checks matrix powers, determinant prefixes, and
Newton identities in SymPy.  `c110_replay.py` checks canonical bytes and
scope.  `c110_mutation.py` runs ten hostile semantic mutations.

The release manifest script is intentionally run after the paper and round
PDFs are finalized.
