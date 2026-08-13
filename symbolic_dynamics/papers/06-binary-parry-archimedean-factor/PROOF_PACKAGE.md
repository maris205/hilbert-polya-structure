# Paper 06 Proof Package

## Claim boundary

**Status: coherent A3 mechanism, incomplete global completion.**

SD-C08 canonically produces the finite-prime Fredholm factor and the
Archimedean Gamma factor from the two irreducible sectors of the unique
minimal full-shift atom. This is a same-source Mellin–Fredholm factorization,
not one dynamical determinant. No meromorphic continuation, functional
equation, pole removal, or Riemann-zero divisor is proved.

## 1. Minimal binary source and its two sectors

For the full shifts \(F_n\), tensor product and entropy obey

\[
F_m\boxtimes F_n\cong F_{mn},\qquad h(F_n)=\log n.
\]

The nonunit tensor atoms are \(F_p\), and \(F_2\) is their unique
least-entropy member. Let

\[
\Omega_q=q^{-1/2}(1,\ldots,1),\qquad
K_q=|\Omega_q\rangle\langle\Omega_q|=J_q/q.
\]

This is the unique positive \(S_q\)-invariant rank-one projection onto the
trivial line. For \(q=2\),

\[
\mathbb C^2=\mathbb C\Omega_2\oplus E_2,
\qquad E_2=\mathbb C(1,-1),
\]

so the centered standard representation is also one-dimensional and occurs
with multiplicity one. For \(q>2\), it has dimension \(q-1\) and contains no
nonzero \(S_q\)-invariant scalar direction.

## 2. Stationary sector: exact Euler determinant

Before separating the sectors, put

\[
Q=\operatorname{diag}(1,-1),\qquad
H(z)=e^{zQ/2}K_2e^{zQ/2}
=\frac12\begin{pmatrix}e^z&1\\1&e^{-z}\end{pmatrix}.
\]

This rank-one matrix has nonzero eigenvalue \(\cosh z\), hence
\[
\operatorname{tr}H(z)^r=(\cosh z)^r.
\]
At \(z=0\) this is the Euler power trace. At
\(z=iu/\sqrt r\), it is the exact binary characteristic function and tends
to \(e^{-u^2/2}\). Thus one source-internal trace deformation generates the
two channels below.

On
\(\mathcal H=\ell^2(\operatorname{At})\otimes\mathbb C^2\), define

\[
\mathcal A_s=\bigoplus_{F_p}p^{-s}K_2.
\]

Since \(K_2^r=K_2\) and \(\operatorname{tr}K_2=1\),

\[
\operatorname{Tr}\mathcal A_s^r=\sum_p p^{-rs}.
\]

For \(\Re s>1\), \(\mathcal A_s\) is trace class and

\[
\det(I-\mathcal A_s)
=\exp\left(-\sum_{r\ge1}\frac1r\sum_pp^{-rs}\right)
=\prod_p(1-p^{-s})=\zeta(s)^{-1}.
\]

Equivalently, its odd one-particle Berezinian is \(\zeta(s)\). This preserves
the full prime-power ledger of SD-C07.

The ledger does not by itself select the binary kernel: any finite rank-one
projection with trace one has the same power traces. If a reversible
stochastic kernel has eigenvalues \(1,\lambda_2,\ldots,\lambda_q\) and
\(\operatorname{tr}K^r=1\) for every \(r\ge1\), Newton identities force
all \(\lambda_j=0\); reversibility then makes it a rank-one orthogonal
projection. Thus exactness selects rank one, while minimality and the scalar
fluctuation sector select \(F_2\).

## 3. Sign sector: the Archimedean Mellin limit

Under the Parry measure of \(F_2\), let \(X_j\in\{-1,+1\}\) be the sign
observable and \(S_N=\sum_{j=0}^{N-1}X_j\). For odd \(N\), put

\[
Y_N=\frac{S_N}{\sqrt{2\pi N}},\qquad
M_N(s)=\mathbb E|Y_N|^{s-1}.
\]

The local central limit theorem, together with a uniform small-ball bound,
gives locally uniform convergence on \(\Re s>0\) to the Mellin transform of
the self-dual Gaussian:

\[
M_N(s)\longrightarrow
\int_{\mathbb R}|x|^{s-1}e^{-\pi x^2}\,dx
=\pi^{-s/2}\Gamma(s/2).
\]

Odd \(N\) avoids a zero atom at finite cutoff. The exponent \(1/2\) in the
normalization is the fluctuation exponent; the factor \(\pi\) fixes the
self-dual Fourier convention.

For \(F_q\), put its symbols at the vertices of the centered regular simplex
in dimension \(d=q-1\), and take the radial statistic with the same
\(\sqrt{2\pi N}\) scale. Its limiting Mellin transform is

\[
M_d(s)=(\pi d)^{-(s-1)/2}
\frac{\Gamma((d+s-1)/2)}{\Gamma(d/2)}.
\]

Only \(d=1\), hence \(q=2\), equals
\(\pi^{-s/2}\Gamma(s/2)\). This is a representation-dimensional
specificity test, not a denial of ordinary one-dimensional CLT universality.

## 4. Same-source factorization

The trivial and sign channels occur canonically in one multiplicity-free
\(S_2\)-permutation representation. Therefore, on \(\Re s>1\), define

\[
\mathfrak Z_{\rm SD}(s)
:=\left(\lim_{N\to\infty}M_N(s)\right)
\operatorname{Ber}(I-\mathcal A_s)
=\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]

The identity is an internally sourced product of two different transforms.
It must not be upgraded to a single Fredholm determinant without a coupling
theorem.

## 5. Hellinger chiral centering

Let

\[
G=\bigoplus_p p^{-1}I_{E_p}
\]

and let \(K=\bigoplus_pK_p\) be bounded and block preserving, so
\([G,K]=0\). Put

\[
A_t=G^{1/2+it}K,\qquad
B_t=\begin{pmatrix}0&A_t\\A_t^*&0\end{pmatrix}.
\]

Then

\[
U_t=\operatorname{diag}(G^{it/2},G^{-it/2})
\]

is unitary and direct multiplication gives

\[
B_t=U_tB_0U_t^*.
\]

Hence every block-preserving completion of this form is isospectral on the
critical axis. Spectral motion requires \([G,K]\ne0\), which means cross-atom
mixing. Such mixing creates mixed temporal cycles unless a new intrinsic
cancellation theorem preserves the prime-power ledger.

For the frozen rank-one block, define off the axis

\[
\mathcal B_s=
\begin{pmatrix}0&G^sK\\G^{1-s}K&0\end{pmatrix}.
\]

Its active eigenvalues on each atom are \(\pm p^{-1/2}\). In the common
Schatten strip \(1/3<\Re s<2/3\),

\[
\det_3(I-z\mathcal B_s)
=\prod_p(1-z^2/p)e^{z^2/p},
\]

independent of \(s\). Moreover
\(\operatorname{Tr}\mathcal B_s^{2r}=2\sum_pp^{-r}\) only converges for
\(r\ge2\); the divergent \(r=1\) quadratic trace is precisely what
\(\det_3\) removes. The regularization reaches the critical line but cannot
carry a vertical zero divisor.

## 6. Route outcome

The Route-A tuple is

\[
(\texttt{A0\_ANALYTIC\_ARITHMETIC\_ORIGIN},
\texttt{A1\_PASS\_ANALYTIC},
\texttt{A2\_ANALYTIC\_DETERMINANT},
\texttt{A3\_PARTIAL\_ANALYTIC\_STRUCTURE},
\texttt{A4\_FORMAL\_HINT}).
\]

Overall: `ROUTE_A_ANALYTIC_CANDIDATE`, with the stage result
`GO_A3_ARCHIMEDEAN_FACTOR / STOP_GLOBAL_COMPLETION`. Every Route-B coordinate
is false and Route B remains locked.
