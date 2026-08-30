# C240 results

The exact receipt contains 747 primitive canonical binary words for each of
\(\lambda=1/2,2/3,3/4\), hence 2241 word rows.  The affine solver finds 138
nonempty word-certified \(\delta\)-components through length 12.  Every row
stores the return point, all intermediate affine states, derivative
\(\lambda^n\), carry rotation, and both endpoint equality decisions.

The direct ledger has 295 probes (base grid plus every distinct endpoint).
Independent 90-digit iteration recovers settled suffix words for the interior
controls and exposes the branch change at equality endpoints.  SymPy confirms
119 generic/rational identities; byte replay is identical; the hostile suite
rejects 33/33 repaired-hash mutations.

This is a finite, source-local piecewise-contraction theorem.  The grouped
components are not asserted maximal, and the factor \(1-z^n\lambda^n\) is not
a target determinant.  Route-A is `ROUTE_A_REJECTED` with A0/A2/A3 failures;
Route B is disabled.
