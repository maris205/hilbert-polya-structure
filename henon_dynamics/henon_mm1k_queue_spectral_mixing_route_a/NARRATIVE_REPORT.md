# Narrative report — HCS-C225

The decisive step is to carry one finite M/M/1/K model through its entire
reversible semigroup.  The queue capacity is not treated as a nuisance cutoff:
the endpoint rates produce Robin conditions, and those conditions close the
finite Jacobi spectrum at the explicit angles `j*pi/(K+1)`.  This simultaneously
delivers a normalized eigenbasis, an exact transient kernel, and a quantitative
mixing estimate.

The second step is a disciplined capacity boundary.  Subcritical finite laws
converge to the geometric stationary distribution and their gap converges to
the square-root rate difference.  At equal rates the gap collapses as `K^-2`
and the infinite chain is null recurrent.  Above criticality, finite stationary
mass moves to the reflecting wall and every fixed state loses mass; this is
recorded as mass escape, not mislabeled as a stationary distribution.

The artifact contains 20 exact stationary rows, 60 mode rows, 240 spectral
kernel rows and linked TV bounds, plus 16 limit rows and eight singular-face
rows.  The independent checker reports 3,655 assertions; SymPy reports 46
identities; replay is byte exact; 25 repaired-hash and two nested-schema
mutations plus one stale hash are rejected.

This is a substantial source-local advance, but it stops at the Route-A
boundary.  Queue states have no primitive arithmetic ownership, and the
finite Jacobi matrix is only a formal quantization hint.  The verdict is
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`,
`ROUTE_A_REJECTED`, with Route B false.
