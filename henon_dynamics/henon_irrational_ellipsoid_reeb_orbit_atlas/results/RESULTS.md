# C242 results

The canonical receipt contains 48 irrational rows (two parameter orientations,
two axes, and twelve iterates) and six rational coordinate rows.  Every
irrational CZ value is backed by an integer-square certificate.  Rational
controls `2/1`, `3/2`, and `5/3` explicitly report the full-boundary
Morse--Bott family, common period, unit transverse multiplier, and null
pre-perturbation CZ value.

The independent checker, SymPy crosscheck, byte replay, and 29-case hostile
mutation suite are release gates.  Route A is
`A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_FORMAL_HINT`; overall verdict is
`ROUTE_A_REJECTED`, with Route B disabled.  No target arithmetic or determinant
claim is made.
