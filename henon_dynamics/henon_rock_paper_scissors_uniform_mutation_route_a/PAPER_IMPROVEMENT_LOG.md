# Paper improvement log

## Round 0 → Round 1

Added the explicit cubic turning equation and the endpoint-cancelled integral
(5), including the third-root factorization.  The finite ledger protocol was
made explicit so RK4 diagnostics cannot be mistaken for the LaSalle proof.

## Round 1 → Round 2

Added the complete degenerate-face statement (`a=0` contraction and identity),
the ambient-versus-tangent Jacobian distinction, the algebraic AM–HM remainder,
and the strict Route-A tuple/scope declaration.  Corrected the May–Leonard
bibliographic title and stated that it is context only, not the frozen
additive-uniform-mutation model.

Both changes are substantive content revisions; the three resulting PDFs are
kept as distinct release artifacts.

## Release-integrity correction

The final audit made the conservative-period quantifier explicit: periodic
levels and the heteroclinic network require \(a>0\), whereas
\(a=\mu=0\) is the identity flow.  A repaired-hash hostile mutation now locks
this boundary so that the evidence contract cannot silently regress.
