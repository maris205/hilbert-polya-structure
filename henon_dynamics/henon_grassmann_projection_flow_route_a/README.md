# HCS-C298 — exact Grassmann projection flow

For a fixed real symmetric matrix `A`, this package closes the rank-`k`
orthogonal-projection flow

`dot(P)=[P,[P,A]]`.

The main theorem gives the global solution
`Ran(P(t))=exp(tA)Ran(P0)` and its projector formula, exact exterior-power
scaling, every simple-spectrum Schubert-cell limit and actual-support rate,
all invariant-projection equilibria and linear modes, the full repeated-
spectrum product-Grassmann Morse--Bott atlas, associated-graded limits, and a
strict Lyapunov exclusion of nonconstant recurrence.

Subset sums are not assumed distinct.  For simple spectrum, uniqueness of the
leading supported Plücker coordinate follows from representable-matroid
greedy exchange.  For repeated spectrum, the entire tied top-weight component
is retained and identified basis-independently through the eigenflag.

This differs from C185: C185 moves a full matrix on an isospectral orbit
toward a separate diagonal target, whereas C298 fixes `A` and moves a
projection/subspace by the linear action induced by `exp(tA)`.

Route-A tuple:
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`; overall verdict
`ROUTE_A_REJECTED`, with Route B locked.  Run
`python -B code/c298_release_manifest.py` for the complete release audit.
