# C229 results

The producer emits a 64-significant-digit, deterministic certificate.  The
ledger has 8 boundary controls (strict, equality, regular and all zero-rate
faces), 7 affine-transform controls, 3 Gamma stationary controls, 9 Laguerre
modes plus 3 kernel rows, 5 gap rows and 3 zero-atom rows.  The independent
checker passes 235 assertions; SymPy passes 18 identities; replay is byte
identical; hostile mutation rejection is 20/20.

The theorem-level result is the exact affine/Gamma/Laguerre closure on the
positive face together with an explicit all-parameter boundary atlas.  The
Route-A tuple is `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`.
