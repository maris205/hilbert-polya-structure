# Theorem package

Let `alpha,beta>0` and let `P_t` be the canonical conservative/no-flux Jacobi
semigroup with generator

\[
Lf=x(1-x)f''+[\alpha-(\alpha+\beta)x]f'.
\]

The package proves simultaneously:

1. `0` is regular reflecting for `0<alpha<1` and entrance for `alpha>=1`;
   `1` is regular reflecting for `0<beta<1` and entrance for `beta>=1`.
2. The unique invariant probability is `Beta(alpha,beta)`, and the generator
   has the exact divergence form and Dirichlet form stated in the paper.
3. `P_n^(beta-1,alpha-1)(2x-1)` is a complete orthogonal eigenbasis with
   eigenvalues `-n(n+alpha+beta-1)` and sharp gap `alpha+beta`.
4. The heat kernel expansion holds relative to the Beta probability.  For
   every `t>0`, `P_t` is trace class and
   `det(I-zP_t)=product_n(1-z exp(-lambda_n t))`.
5. Every polynomial degree is invariant and
   `m_k'=k(k+alpha-1)m_(k-1)-k(k+alpha+beta-1)m_k`; the stationary moments are
   `(alpha)_k/(alpha+beta)_k`.
6. If `P_T f=f` in `L2(pi)` for `T>0`, then `f` is constant.  This is not a
   denial of sample-path recurrence: the canonical diffusion is irreducible
   and positive recurrent.

The finite certificate checks conventions and exact algebra at rational
sentinels.  The proof, not the finite grid, establishes the all-parameter
claims.
