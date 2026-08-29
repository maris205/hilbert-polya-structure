# C235 results

The deterministic producer records 15 conservative quadrature rows, 3
center-limit rows, 6 uniform-mutation rows (including all three coordinate
boundaries), 3 exact `a=0` contractions, and 4 tangent-linearization rows.
All rational inputs satisfy the simplex constraint.  The independent checker
recomputes the endpoint-cancelled integral and the fixed-step diagnostic
without importing producer code; SymPy verifies the mass, product, AM–HM,
turning, center-spectrum, and contraction identities.  Canonical replay is
byte-identical in two fresh temporary trees, and 25/25 hostile mutations are
rejected.

The finite receipt is evidence of implementation closure only.  It does not
turn a continuum of ODE periods into a discrete primitive-orbit product.
Route-A remains `ROUTE_A_REJECTED`; Route B is disabled.
