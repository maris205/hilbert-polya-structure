# Theorem and boundary package — C123

## Proposition 1 — strict random affine contraction

The common linear part

\[
A=\begin{pmatrix}1/2&-1/4\\1/4&0\end{pmatrix}
\]

has the repeated eigenvalue `1/4`, determinant `1/16`, and squared singular
values `3/16 ± sqrt(2)/8`, both below one.  Every finite branch composition
therefore has a unique fixed state.

## Proposition 2 — periodic noise-word prefix

All 126 rooted binary words of lengths one through six are checked.  Primitive
necklace counts are

```text
2, 1, 2, 3, 6, 9
```

for a total of 23.  Each canonical word owns an exact oriented periodic-state
row and composition determinant `16^{-n}`.  Its displayed `2^{-n}` value is
the probability of the chosen rooted length-`n` block under the iid law.  It
is neither the total probability mass of the necklace nor the probability of
an infinite periodic realization.

## Proposition 3 — degree-four Markov moments

On the 15 monomials of total degree at most four,

\[
(Pf)(x,y)=\tfrac12f(F_+(x,y))+\tfrac12f(F_-(x,y))
\]

is closed.  Its exact matrix has trace `453/256` and determinant `2^{-80}`.
The unique normalized stationary moment vector has covariance

\[
\Sigma=\frac1{3375}\begin{pmatrix}1088&128\\128&68\end{pmatrix},
\qquad \det\Sigma=\frac{256}{50625},
\]

and satisfies the exact Lyapunov equation.  Its `x` fourth cumulant is
`-47789203456/359401303125`, so Gaussian closure is not substituted.

## Boundary

The intrinsic word ledger supports only `A1_WEAK`: periods through six have no
prime-like target correspondence.  `A2_FAIL` because the degree-four Markov
determinant has no target-divisor match or analytic bridge; `A3_FAIL` because
no global analytic structure or continuation theorem is established;
`A4_FAIL`.  The canonical tuple is
`(A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`, overall `ROUTE_A_EXPLORATORY`.  No
complete random orbit atlas, global analytic owner, arithmetic promotion, or
Route B follows.
