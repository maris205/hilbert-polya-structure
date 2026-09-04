# Theorem package

## Model and regularity convention

Let

\[
f(\zeta,t)=a(t)\zeta+b(t)\zeta^2,
\quad a(t)>0,\quad b(t)\in\mathbb C,
\]

and impose

\[
\operatorname{Re}\!\left(f_t\overline{\zeta f_\zeta}\right)=q
\quad\text{on }|\zeta|=1,
\]

for fixed real `q`.  A smooth univalent solution satisfies `a>2|b|`; this is
exactly the condition that the quadratic map be injective and have no
critical point on the closed disk.

## Main theorem

For any smooth univalent initial coefficients, there is a unique maximal
smooth coefficient solution and

\[
\dot a=\frac{aq}{a^2-4|b|^2},\qquad
\dot b=-\frac{2qb}{a^2-4|b|^2}.
\]

The quantities

\[
\kappa=a^2b,
\qquad
M_0=a^2+2|b|^2=\operatorname{Area}(f(\mathbb D))/\pi
\]

satisfy `kappa_dot=0` and `M0_dot=2q`.  With `u=a^2`,

\[
M_0=F(u)=u+\frac{2|\kappa|^2}{u^2},\qquad
F'(u)=1-\frac{4|\kappa|^2}{u^3}.
\]

If `u_c=(4|kappa|^2)^(1/3)`, then smooth univalence is exactly `u>u_c`,
and `F` is strictly increasing there.

- For `q>0`, the upper branch exists globally, `u` increases to infinity,
  and `2|b|/a` tends to zero.
- For `q=0`, the coefficients are stationary.
- For `q<0` and `kappa` nonzero, the first singular time is

  \[
  T=\frac{M_0(0)-3u_c/2}{-2q}.
  \]

  At that time `a_c=2|b_c|`, the only critical point reaches the unit circle,
  and no critical point in the closed disk or self-intersection on the closed
  disk occurs earlier.

Writing `b_c=B exp(i phi)` and parametrizing near the critical preimage by
`zeta=-exp(-i phi) exp(i s)` gives

\[
e^{i\phi}(f(\zeta,T)-z_c)
=-Bs^2-iBs^3+\frac7{12}Bs^4+O(s^5),
\qquad z_c=-\overline{b_c}.
\]

Thus, in rotated coordinates, `Y^2/X^3` tends to `1/B`: the endpoint is one
ordinary semicubical cusp.

## Boundary proposition

If `kappa=0`, then `b=0` and `a(t)^2=a(0)^2+2qt`.  Under suction the circle
collapses at `a(0)^2/(-2q)` and no cusp precedes collapse.  Initial equality
`a=2|b|` with nonzero `b` is already cusped and has zero smooth lifespan.
Initial `0<a<2|b|` has an interior critical point and is not asserted to
represent a conformal Laplacian-growth domain.

## Proof boundary

The proof is analytic and covers all complex `b`, not merely the rational
panels.  Evidence rows test algebra, branch labels, rational cusp clocks, and
the local coefficient ratio.  They do not prove the continuous theorem.

No post-cusp weak solution, surface-tension model, higher-degree theorem,
priority claim, or target arithmetic statement is made.
