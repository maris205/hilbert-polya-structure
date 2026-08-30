# C239 test report

The independent checker locks every top-level and nested field, source
baseline, evaluator hash, citation record, route tuple, and all-false scope
flags.  It independently implements the literal reverse-pile packet
interleave and compares it with modular multiplication at all 1,100 positions
of the 50-parameter grid.  It then recomputes fixed counts, local orders,
Möbius inversion, direct cycle decompositions, and small zeta-denominator/
Koopman polynomials.

Results: checker `PASS (2,303 assertions)`; SymPy `PASS (50 symbolic
identities)`; byte replay `PASS`; hostile mutation `PASS 44/44`.  The source
zeta and finite permutation spectrum are exact, but A2 remains `FAIL` under
the target-match criterion and all forbidden arithmetic/Route-B claims remain
absent.
