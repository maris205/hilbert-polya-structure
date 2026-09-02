# Symmetric matrix Riccati Möbius theorem

Let `X0` be a real symmetric `n` by `n` matrix and put

\[
F_t(X_0)=(X_0\cosh t+I\sinh t)
          (I\cosh t+X_0\sinh t)^{-1}.
\]

## Theorem

1. Wherever the denominator is invertible, `F_t(X0)` is the unique symmetric
   solution of `Xdot=I-X^2`; `F_t o F_s=F_(t+s)` whenever both sides lie in
   the same classical chart.
2. If `lambda_1,...,lambda_n` are the eigenvalues of `X0`, a chart pole occurs
   exactly at `t=atanh(-1/lambda_j)` for `|lambda_j|>1`.  The maximal interval
   through zero is bounded by the nearest such negative and positive poles.
3. The solution is forward global exactly when `lambda_min(X0)>=-1`.  In that
   case
   `F_t(X0) -> I-2 P_{ker(X0+I)}`.  Every eigenvalue strictly greater than
   `-1` converges to `+1` with `O(exp(-2t))` remainder; that scale is exact
   unless the eigenvalue is already the fixed value `+1`.
4. With `Phi(X)=tr(X^3/3-X)`,

   \[
   \frac{d}{dt}\Phi(X(t))=-\|I-X(t)^2\|_F^2.
   \]

   Consequently every recurrent classical trajectory is an equilibrium.
5. The equilibria are the symmetric involutions.  The component with plus
   multiplicity `p` and minus multiplicity `q=n-p` is the Grassmann orbit
   `O(n)/(O(p) x O(q))`.  Its stable, unstable, and center dimensions are

   \[
   \frac{p(p+1)}2,\qquad \frac{q(q+1)}2,\qquad pq,
   \]

   and the center is precisely tangent to the equilibrium component.
6. In an eigenbasis of `X0`, the Fréchet derivative is the Schur multiplier

   \[
   (DF_t(X_0)H)_{ij}=
   \frac{H_{ij}}
   {(\cosh t+\lambda_i\sinh t)(\cosh t+\lambda_j\sinh t)}.
   \]
7. The block system `Udot=V`, `Vdot=U`, `U(0)=I`, `V(0)=X0` satisfies
   `X=VU^{-1}` until `det U=0`; the chart singularities in item 2 are exactly
   the loss of invertibility of `U`.

## Proof skeleton

The block exponential gives `U=I cosh t+X0 sinh t` and
`V=X0 cosh t+I sinh t`; differentiating `VU^{-1}` gives the Riccati equation.
The spectral theorem reduces maximality and limits to the scalar Möbius map.
The trace derivative is the Frobenius pairing of `X^2-I` with `I-X^2`.
At an involution `S=diag(I_p,-I_q)`, the linearization
`H -> -(SH+HS)` is `-2`, `+2`, and `0` on the plus block, minus block, and
off-diagonal block.  Finally, the divided difference of the scalar Möbius map
is the reciprocal product displayed in item 6.

## Route-A decision

`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`, hence
`ROUTE_A_REJECTED`.  The linear lift is exact but finite-dimensional and
source-local; it is not a target spectral realization.
