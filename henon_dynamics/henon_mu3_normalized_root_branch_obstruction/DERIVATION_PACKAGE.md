# HCS-C46 derivation package

## Question

Does the normalized local root from C45 have integral divisor multiplicities,
as an ordinary determinant must?

## Exact reduction

At \(p=7\), the trace field has degree three.  The sector polynomials are
computed in \(\mathbf Q(\zeta_7)[z]\), paired with complex conjugates, reduced
to \(\mathbf Q(\theta)[z]\), and normed by resultants against
\(\theta^3+\theta^2-2\theta-1\).  This yields

\[
N_7=P_{18}^2/(49P_{12}^2).
\]

Modular gcds certify that both polynomials are squarefree and do not share a
root.  The norm divisor therefore has exact multiplicities \(\pm2\).

## Obstruction

C45 divides the norm logarithm by the field degree three.  This gives local
orders \(\pm2/3\), which are valid normalized-trace dimensions but invalid
orders for a scalar meromorphic function or ordinary finite-dimensional
determinant.  The obstruction is exact at the first split prime.

## Scientific interpretation

The negative result does not destroy the critical-boundary germ.  It identifies
its correct next category: a normalized-trace determinant, if one exists.
Thus C46 is not a retreat from C45; it separates an analytic survivor from an
incorrect ordinary-determinant interpretation.

