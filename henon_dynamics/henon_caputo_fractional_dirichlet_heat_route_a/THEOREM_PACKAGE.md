# Theorem package: Caputo memory versus Dirichlet heat smoothing

## Frozen owner and conventions

Let `A=-d^2/dx^2` on `X=L2((0,pi))`, with

`D(A)=H^2(0,pi) cap H_0^1(0,pi)`.

For `0<beta<=1`, solve

\[
 {}^C D_t^\beta u(t)+Au(t)=0,\qquad u(0)=u_0.
\]

The normalized eigenbasis is `e_n=sqrt(2/pi) sin(nx)`, `Ae_n=n^2e_n`.
For `0<beta<1`, the Caputo derivative is

\[
 {}^C D_t^\beta f(t)=\frac1{\Gamma(1-\beta)}
 \int_0^t(t-s)^{-\beta}f'(s)\,ds.
\]

The Sobolev gain `s` means the spectral space `D(A^(s/2))`; at `s=2`
this is exactly `H^2 cap H_0^1`.  This endpoint convention is frozen.

## Main theorem

For every `u_0 in X` there is a unique strong-for-positive-time mild solution

\[
 S_\beta(t)u_0=\sum_{n\ge1}
 E_\beta(-n^2t^\beta)\langle u_0,e_n\rangle e_n,
 \qquad
 E_\beta(z)=\sum_{k\ge0}\frac{z^k}{\Gamma(\beta k+1)}.
\]

It has the following complete phase atlas.

1. For `0<beta<1`, `S_beta(t)` is the inverse-stable subordination of the
   Dirichlet heat semigroup.  It is self-adjoint, a positive operator,
   positivity preserving, and contractive on `L2`.  It is strongly continuous
   at zero, but it is not a semigroup.
2. For every fixed `t>0`, `0<beta<1`, and `theta>=0`,

   \[
   A^\theta S_\beta(t)\in\mathcal B(X)
   \quad\Longleftrightarrow\quad \theta\le1.
   \]

   Equivalently the family gains every `s<=2` spatial derivatives, including
   the endpoint `s=2`, and fails for every `s>2`, within the declared
   smoothing domain `s>=0`.  Negative `theta` is outside this declared domain:
   since `A>=I`, `A^theta` is bounded for `theta<0`, and hence so is
   `A^theta S_beta(t)`.
3. For every `t>0`, `0<beta<1`, and `p>0`,

   \[
   S_\beta(t)\in\mathcal S_p\quad\Longleftrightarrow\quad p>\frac12.
   \]

   The endpoint `p=1/2` diverges.
4. In operator norm,

   \[
   t^\beta S_\beta(t)\longrightarrow
   \frac{A^{-1}}{\Gamma(1-\beta)}\qquad(t\to\infty),
   \]

   and `t^beta ||S_beta(t)|| -> 1/Gamma(1-beta)`.
5. At `beta=1`, `S_1(t)=exp(-tA)`.  For every `t>0` it maps into every
   `D(A^theta)`, lies in every `S_p`, and has norm exactly `exp(-t)`.

## Proof

Taking sine coefficients reduces the equation to
`Caputo_D^beta a_n+n^2 a_n=0`.  The coefficient shift

\[
 {}^C D_t^\beta\frac{t^{\beta k}}{\Gamma(\beta k+1)}
 =\frac{t^{\beta(k-1)}}{\Gamma(\beta(k-1)+1)},\qquad k\ge1,
\]

proves the scalar Mittag–Leffler solution.  Pollard's theorem makes
`E_beta(-x)` completely monotone on the positive axis.  Equivalently there is
an inverse-stable probability density `eta_beta(t,s)` characterized by

\[
 \int_0^\infty e^{-zt}\eta_\beta(t,s)\,dt
 =z^{\beta-1}e^{-s z^\beta},
\]

and

\[
 S_\beta(t)=\int_0^\infty e^{-sA}\eta_\beta(t,s)\,ds.
\]

This gives positivity preservation and contraction; scalar dominated
convergence gives strong continuity.  If `S_beta` were a semigroup, its first
mode multiplier would be a continuous multiplicative function and hence an
exponential.  The expansion
`E_beta(-t^beta)=1-t^beta/Gamma(1+beta)+O(t^(2beta))` is not exponential for
`beta<1`, proving the category boundary.

On the positive ray, the Mittag–Leffler asymptotic is

\[
 E_\beta(-x)=\frac1{x\Gamma(1-\beta)}+O(x^{-2}),
 \qquad x\to\infty,
\]

with a harmless vanishing coefficient when a reciprocal Gamma factor hits a
pole.  Therefore, for fixed `t>0`, the singular values satisfy

\[
 E_\beta(-n^2t^\beta)\sim
 \frac{t^{-\beta}}{\Gamma(1-\beta)}n^{-2}.
\]

The multiplier of `A^theta S_beta(t)` is thus asymptotic to a positive
constant times `n^(2theta-2)`.  Within the declared `theta>=0` smoothing
domain it is bounded if and only if `theta<=1`.  For `theta<0`, the spectral
inequality `A>=I` makes `A^theta` bounded, so `A^theta S_beta(t)` is bounded as
well; these negative powers are not part of the declared smoothing domain.
The `S_p` sum is comparable to `sum n^(-2p)`, proving the sharp threshold and
its divergent endpoint.

Finally, the same scalar asymptotic is uniform for `x>=t^beta`.  Hence the
diagonal multipliers of
`t^beta S_beta(t)-A^{-1}/Gamma(1-beta)` converge uniformly in `n`, which proves
operator-norm convergence.  Complete monotonicity makes the first mode the
operator norm.  At `beta=1`, the multipliers are `exp(-n^2t)`, yielding the
separate heat conclusions.

## Evidence boundary

The receipt stores 24 scalar Mittag–Leffler values, 192 spectral cells, six
composition witnesses, 96 independent `beta=1/2` long-time cells, 35
smoothing classifications, and 25 Schatten classifications.  The arbitrary
parameter theorem is proved by the multiplier arguments above; finite cells
are regression and convention evidence only.

## Route A

The strict tuple is
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`, overall
`ROUTE_A_REJECTED`, with Route B disabled.  The Caputo solution family is not
a target arithmetic determinant or Hilbert–Pólya operator.  Scope is
`NO_BAD_EULER_OR_ROOT_NUMBER`.
