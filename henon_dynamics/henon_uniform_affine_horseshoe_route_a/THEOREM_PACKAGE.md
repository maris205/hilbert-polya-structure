# Theorem package

Let `P=[3,4] x [1/5,1/3]`.  For `(lambda,mu) in P`, put

\[
R_0=[0,\lambda^{-1}]\times[0,1],\qquad
R_1=[1-\lambda^{-1},1]\times[0,1]
\]

and, on `R_e`, define

\[
F_{\lambda,\mu}(x,y)=
(\lambda x-(\lambda-1)e,\;\mu y+(1-\mu)e),\qquad e\in\{0,1\}.
\]

## Theorem 1 — uniform affine horseshoe

The two domain strips and the two image strips have gaps at least `1/3`.
The derivative on either branch is `diag(lambda,mu)`, so the unstable
expansion is at least `3` and the stable contraction is at most `1/3`.
The maximal two-sided invariant set is conjugate to the full two-shift.

For a based word `e_0...e_{n-1}`, the unique periodic point has

\[
x_0=\frac{\lambda-1}{\lambda^n-1}
\sum_{j=0}^{n-1}\lambda^{n-1-j}e_j,
\qquad
y_0=\frac{1-\mu}{1-\mu^n}
\sum_{j=0}^{n-1}\mu^{n-1-j}e_j.
\]

Consequently `#Fix(F^n)=2^n`, and the number of primitive cycles is

\[
p_n=\frac1n\sum_{d\mid n}\operatorname{mobius}(d)2^{n/d}.
\]

## Theorem 2 — exact trace-class owner

Let

\[
\mathcal H=\mathbb C^2\otimes
\ell^2(\mathbb N_{\ge1}\times\mathbb N_0),\quad
J=\begin{pmatrix}1&1\\1&1\end{pmatrix},
\]

and let `D_{lambda,mu}` be diagonal with entries
`lambda^{-r} mu^s`, `r>=1`, `s>=0`.  Define
`K_{lambda,mu}=J tensor D_{lambda,mu}`.  Then `K` is trace class and

\[
\|K_{\lambda,\mu}\|_1=
\frac{2}{(\lambda-1)(1-\mu)}\le\frac32.
\]

For every `n>=1`,

\[
\operatorname{Tr}K_{\lambda,\mu}^n
=\frac{2^n}{(\lambda^n-1)(1-\mu^n)}
=\sum_{q\in\operatorname{Fix}F^n}
\frac1{|\det(I-DF^n(q))|}.
\]

## Theorem 3 — determinant and uniformity

The Fredholm determinant is

\[
\det(I-zK_{\lambda,\mu})
=\prod_{r\ge1,s\ge0}(1-2z\lambda^{-r}\mu^s).
\]

It is zero-free for `|z|<lambda/2`, hence uniformly zero-free for
`|z|<3/2` on `P`.  Moreover

\[
\|K_{\lambda,\mu}-K_{\lambda',\mu'}\|_1
\le \frac34|\lambda-\lambda'|+
\frac94|\mu-\mu'|.
\]

## Strict evaluation

The structural uniform-parameter subgate passes.  The canonical evaluation is
still `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` because no frozen target divisor
or target-facing validation is present.  `route_b_invocation_allowed: false`.
