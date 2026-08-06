# Proof Package: Analytic Spectral Activity of the Hénon Warp

## Claim 1: strict ground-state activation

Let \(a>-1\), \(a\ne0\), and \(h>0\).  Put

\[
r_a=\frac1{1+\sqrt{1+a}},
\qquad
\Psi_a(x,y)=(-2ar_ax-ax^2-y,x),
\]

\[
V_a(q)=2\pi e^{\pi|\Psi_a(q)|^2},
\qquad
V_0(q)=2\pi e^{\pi|q|^2},
\]

and let \(H_{a,h}=-h^2\Delta/2+V_a\) be the Friedrichs operator on
\(L^2(\mathbb R^2)\).  Then

\[
\boxed{\lambda_1(H_{a,h})>\lambda_1(H_{0,h}).}
\]

In particular, the Hénon-warped and radial operators are not isospectral.

## Status for Claim 1

`PROVABLE AS STATED`.  An independent review verified the inequality
direction, compactness and positivity assumptions, the Brothers--Ziemer
equality step, and the quartic non-radiality obstruction.  The primary
equality-case citation is recorded at the end of this package.

## Claim 2: full relative heat asymptotic with uniform remainder

For fixed \(h>0\), as \(t\downarrow0\), let

\[
L=\log\frac1{2\pi t}.
\]

The proposed asymptotic is

\[
\begin{aligned}
\operatorname{Tr}(e^{-tH_{a,h}})-\operatorname{Tr}(e^{-tH_{0,h}})
=-\frac{a^2}{24\pi}\Bigg[&L^2+
\bigl(2(1-\gamma)+4\pi r_a^2\bigr)L\\
&+\frac{\pi^2}{6}-2\gamma+\gamma^2
+4\pi r_a^2(1-\gamma)\Bigg]+O_{a,h}(tL^4).
\end{aligned}
\]

## Status for Claim 2

`PROVABLE AS STATED`.  R300-P1 closes the former uniform-remainder gap by a
direct Brownian-bridge amplitude expansion.  The proof is recorded in full in
`R300_P1_UNIFORM_REMAINDER_PROOF.md`; Lemma 6 below gives its dependency chain
and the exact bound used here.

## Assumptions and standard results used

- \(a>-1\), \(a\ne0\), and \(h>0\) are fixed.
- Symmetric decreasing rearrangement on \(\mathbb R^2\) is denoted by
  \(f^*\); symmetric increasing rearrangement is denoted by \(g_*\).
- Pólya--Szegő: \(\|\nabla f^*\|_2\le\|\nabla f\|_2\).
- The increasing/decreasing Hardy--Littlewood inequality:
  \(\int fg\ge\int f^*g_*\) for nonnegative equimeasurable data, understood
  by monotone truncation when \(g\) is unbounded.
- Brothers--Ziemer equality classification for Pólya--Szegő: if \(f\ge0\), equality holds, its
  superlevel sets have finite measure, and the intermediate critical set has
  measure zero, then \(f\) is a translate of \(f^*\).
- A smooth confining Schrödinger operator has a simple positive ground state;
  for an analytic potential the ground state is analytic by elliptic analytic
  regularity.

## Notation

- \(Q_{a,h}[f]=\frac{h^2}{2}\int|\nabla f|^2+\int V_a|f|^2\) is the closed
  quadratic form.
- \(\Theta_a(t)=\operatorname{Tr}(e^{-tH_{a,h}})\).
- \(I_a(t)=\int e^{-tV_a}|\nabla V_a|^2\).
- \(\lambda=2\pi t\) and
  \[
  A_k(\lambda)=\int_\lambda^\infty
  w e^{-w}\left(\log\frac w\lambda\right)^k\,dw.
  \]

## Proof strategy

Claim 1 uses symmetric rearrangement at the Rayleigh-quotient level.  Equality
would force the positive ground state to be radial up to translation; its
eigenvalue equation would then force \(V_a\) to be radial about the same
point.  The degree-four homogeneous part of \(|\Psi_a|^2\) excludes that for
\(a\ne0\).

For Claim 2, the area-preserving change of variables cancels the classical
heat term pointwise in a common coordinate.  A second-order Taylor expansion
in the Brownian amplitude reduces the first correction to \(I_a-I_0\), whose
angular integral is exact.  Bridge symmetry removes the odd orders; a
good/bad path split and an integrated fourth-amplitude derivative bound give
the uniform \(O_{a,h}(tL^4)\) remainder.

## Dependency map

1. Claim 1 depends on Lemmas 1--4.
2. Lemma 2 uses Pólya--Szegő and increasing/decreasing Hardy--Littlewood.
3. Strictness in Lemma 4 uses the equality classification in Lemma 3 and the
   non-radial polynomial check.
4. The exact carrier in Claim 2 depends on Lemma 5.
5. The full asymptotic additionally depends on the proved uniform estimate in
   Lemma 6.

## Proof of Claim 1

### Lemma 1: equimeasurability

The potentials \(V_a\) and \(V_0\) are equimeasurable, and \(V_0\) is the
symmetric increasing rearrangement of \(V_a\).

#### Proof

The Jacobian matrix is

\[
D\Psi_a(x,y)=
\begin{pmatrix}
-2a(r_a+x)&-1\\
1&0
\end{pmatrix},
\]

so \(\det D\Psi_a=1\).  The inverse is polynomial, hence \(\Psi_a\) is a
global volume-preserving diffeomorphism.  For every \(E>2\pi\),

\[
\begin{aligned}
|\{q:V_a(q)<E\}|
&=|\{q:|\Psi_a(q)|^2<\pi^{-1}\log(E/2\pi)\}|\\
&=|\{u:|u|^2<\pi^{-1}\log(E/2\pi)\}|\\
&=|\{q:V_0(q)<E\}|.
\end{aligned}
\]

The same equality is trivial for \(E\le2\pi\).  Since \(V_0\) is radial and
strictly increasing in \(|q|\), it is precisely the symmetric increasing
rearrangement of \(V_a\). ∎

### Lemma 2: rearranged Rayleigh inequality

For every \(f\) in the form domain of \(H_{a,h}\),

\[
Q_{0,h}[|f|^*]\le Q_{a,h}[f],
\qquad
\||f|^*\|_2=\|f\|_2.
\]

#### Proof

The diamagnetic inequality for the ordinary gradient gives
\(|\nabla|f||\le|\nabla f|\) almost everywhere.  Pólya--Szegő therefore gives

\[
\int|\nabla |f|^*|^2
\le\int|\nabla |f||^2
\le\int|\nabla f|^2.
\]

For a direct proof of the potential direction, set

\[
A_s=\{V_a\le s\},\qquad A_s^*=\{V_0\le s\},\qquad s\ge2\pi.
\]

Lemma 1 gives \(|A_s|=|A_s^*|\), and the set form of the
Hardy--Littlewood inequality gives

\[
\int_{A_s}|f|^2\le\int_{A_s^*}(|f|^*)^2.
\]

Use the nonnegative layer-cake identity

\[
V_a=2\pi+\int_{2\pi}^{\infty}\mathbf 1_{\{V_a>s\}}\,ds
\]

and Tonelli's theorem.  Since rearrangement preserves the \(L^2\) norm,

\[
\begin{aligned}
\int V_a|f|^2
&=2\pi\|f\|_2^2+
\int_{2\pi}^{\infty}
\left(\|f\|_2^2-\int_{A_s}|f|^2\right)ds\\
&\ge2\pi\||f|^*\|_2^2+
\int_{2\pi}^{\infty}
\left(\||f|^*\|_2^2-\int_{A_s^*}(|f|^*)^2\right)ds\\
&=\int V_0(|f|^*)^2.
\end{aligned}
\]

Adding the kinetic and potential inequalities proves the claim. ∎

### Lemma 3: equality forces a radial ground state

If \(\lambda_1(H_{a,h})=\lambda_1(H_{0,h})\), then the positive normalized
ground state \(\phi_a\) of \(H_{a,h}\) is radial about some point
\(q_0\in\mathbb R^2\).

#### Proof

The potential \(V_a\) is smooth, bounded below, and proper.  Thus
\(H_{a,h}\) has compact resolvent.  Positivity improvement of its heat
semigroup gives a simple ground-state eigenvalue with a strictly positive
normalized eigenfunction \(\phi_a\).  Elliptic regularity and analyticity of
\(V_a\) imply that \(\phi_a\) is real analytic.

Assume the two ground-state eigenvalues are equal.  The Rayleigh principle and
Lemma 2 give

\[
\lambda_1(H_{0,h})
\le Q_{0,h}[\phi_a^*]
\le Q_{a,h}[\phi_a]
=\lambda_1(H_{a,h})
=\lambda_1(H_{0,h}).
\]

Both inequalities are equalities.  In particular, \(\phi_a^*\) attains the
Rayleigh infimum for \(H_{0,h}\), so it is the positive radial ground state of
that operator.  The kinetic and potential rearrangement deficits in Lemma 2
are separately nonnegative, so the Pólya--Szegő kinetic deficit is zero.

The nonconstant analytic function \(\phi_a^*\) cannot have its intermediate
critical set of positive measure: otherwise each analytic partial derivative
would vanish identically, forcing \(\phi_a^*\) to be constant, which is
incompatible with nonzero \(L^2(\mathbb R^2)\) normalization.  Its positive
superlevel sets have finite measure because \(\phi_a^*\in L^2\).  The
Brothers--Ziemer equality classification for Pólya--Szegő therefore applies
and yields

\[
\phi_a(q)=\phi_a^*(q-q_0)
\]

for some \(q_0\), first almost everywhere and then everywhere by continuity.
Thus \(\phi_a\) is radial about \(q_0\). ∎

### Lemma 4: the Hénon potential is not radial up to translation

For \(a\ne0\), \(V_a\) is not radial about any point of \(\mathbb R^2\).

#### Proof

If \(V_a\) were radial about a point, then so would be

\[
P_a(x,y)=\frac1\pi\log\frac{V_a(x,y)}{2\pi}
=x^2+(2ar_ax+ax^2+y)^2.
\]

Translation does not change the highest homogeneous part of a polynomial.
The degree-four homogeneous part of \(P_a\) is

\[
a^2x^4.
\]

The highest degree-four part of a polynomial radial about any point must be a
rotation-invariant homogeneous polynomial, hence a constant multiple of
\((x^2+y^2)^2\).  Matching the \(y^4\) coefficient would force that constant
to vanish, while the \(x^4\) coefficient is \(a^2>0\).  This is impossible.
∎

### Completion of Claim 1

Lemma 2 and the Rayleigh principle first give

\[
\lambda_1(H_{0,h})\le\lambda_1(H_{a,h}).
\]

If equality held, Lemma 3 would give
\(\phi_a(q)=\phi_a^*(q-q_0)\).  Translate the ground-state equation for
\(H_{0,h}\) and subtract it from the equation for \(H_{a,h}\).  Since the
eigenvalues are equal,

\[
\bigl(V_a(q)-V_0(q-q_0)\bigr)\phi_a(q)=0.
\]

The ground state is strictly positive and both potentials are continuous, so
\(V_a(q)=V_0(q-q_0)\) for all \(q\).  This contradicts Lemma 4.  Equality is
therefore impossible, and

\[
\lambda_1(H_{a,h})>\lambda_1(H_{0,h}).
\]

This proves Claim 1. ∎

## Supporting heat-trace ordering

For each fixed \(t>0\), Trotter product kernels and the
Brascamp--Lieb--Luttinger multiple-integral inequality give

\[
\Theta_a(t)\le\Theta_0(t).
\]

At finite Trotter number, every Gaussian transition kernel is already
symmetric decreasing and
\((e^{-tV_a/n})^*=e^{-tV_0/n}\).  Applying the multiple-integral inequality
and passing to the trace-norm Trotter limit yields the result.  This package
does not assert strict inequality for every \(t\), because that requires an
equality classification stable under the Trotter limit.  Claim 1 already
proves non-isospectrality without that stronger statement.

## Exact part of Claim 2

### Lemma 5: exact first-gradient carrier

For every \(t>0\),

\[
\boxed{
I_a(t)-I_0(t)
=\frac{2a^2}{t^2}
\left[A_2(2\pi t)+4\pi r_a^2A_1(2\pi t)\right]>0.}
\]

#### Proof

Set \(z=(u,v)=\Psi_a(q)\) and
\(W(z)=2\pi e^{\pi|z|^2}\).  Since \(dq=dz\),

\[
I_a-I_0
=\int e^{-tW(z)}(2\pi W(z))^2
\left(|D\Psi_a(q)^Tz|^2-|z|^2\right)dz.
\]

The inverse coordinates satisfy

\[
q=(v,-2ar_av-av^2-u),
\]

and hence

\[
D\Psi_a(q)=
\begin{pmatrix}
-2a(r_a+v)&-1\\
1&0
\end{pmatrix}.
\]

Direct multiplication gives

\[
|D\Psi_a(q)^Tz|^2-|z|^2
=-4a(r_a+v)uv+4a^2(r_a+v)^2u^2.
\]

The remaining weight is radial.  All terms odd in \(u\) or \(v\) integrate
to zero, leaving

\[
I_a-I_0
=4a^2\int e^{-tW}(2\pi W)^2
\left(r_a^2u^2+u^2v^2\right)dudv>0.
\]

Use polar coordinates \(u=\rho\cos\theta\),
\(v=\rho\sin\theta\), then put \(s=\pi\rho^2\) and
\(w=2\pi t e^s\).  The angular moments are

\[
\int_0^{2\pi}\cos^2\theta\,d\theta=\pi,
\qquad
\int_0^{2\pi}\cos^2\theta\sin^2\theta\,d\theta=\frac\pi4.
\]

Substitution yields exactly

\[
I_a-I_0
=\frac{2a^2}{t^2}
\left[A_2(2\pi t)+4\pi r_a^2A_1(2\pi t)\right].
\]

The bracket is positive because its defining integrands are nonnegative and
not almost everywhere zero. ∎

The Gamma moments

\[
\int_0^\infty we^{-w}\log w\,dw=1-\gamma,
\]

\[
\int_0^\infty we^{-w}(\log w)^2dw
=\frac{\pi^2}{6}-2\gamma+\gamma^2
\]

then give the displayed \(L^2\), \(L\), and constant coefficients, with an
\(O((2\pi t)^2\operatorname{poly}(L))\) lower-limit correction.

### Lemma 6: uniform Brownian-amplitude remainder

For fixed \(a>-1\) and \(h>0\),

\[
\boxed{
\Theta_a(t)-\Theta_0(t)
=-\frac{t^2}{48\pi}(I_a(t)-I_0(t))
+O_{a,h}(tL^4).}
\]

#### Proof

Let \(Q_a=\Psi_a^{-1}\), \(W(z)=2\pi e^{\pi|z|^2}\),
\(\varepsilon=h\sqrt t\), and let \(B\) be a standard two-dimensional
Brownian bridge.  Feynman--Kac and \(dq=dz\) give

\[
\Theta_a(t)=\frac1{2\pi h^2t}\int F_a(\varepsilon,z)dz,
\]

\[
F_a(\theta,z)=\mathbb E\exp\left[-t\int_0^1
V_a(Q_a(z)+\theta B_s)ds\right].
\]

At \(\theta=0\), \(F_a(0,z)=e^{-tW(z)}\), independently of \(a\).  Thus the
complete classical terms cancel pointwise before absolute values are taken.

The exact displacement formula

\[
\Psi_a(Q_a(u,v)+(\xi,\eta))
=\bigl(u-2a(r_a+v)\xi-a\xi^2-\eta,v+\xi\bigr)
\]

and Faà di Bruno imply, with \(\sigma=\pi|z|^2\),

\[
|\Phi_a(Q_a(z)+w)-\sigma|
\le C_a(1+\sigma)(|w|+|w|^2),
\]

\[
\|D^kV_a(Q_a(z)+w)\|
\le C_{a,k}V_a(Q_a(z)+w)(1+\sigma)^k,
\qquad1\le k\le4,
\]

for the displacements used below.  Freeze a small \(\delta>0\), write
\(M=\sup_s|B_s|\), and use the symmetric event

\[
G_t=\left\{M\le\frac{\delta}{h\sqrt tL}\right\}.
\]

The Gaussian bridge maximum bound gives

\[
\mathbb P(G_t^c)\le C_he^{-c_h/(tL^2)}.
\]

On \(G_t\), Taylor's theorem in \(\theta\), together with invariance under
\(B\mapsto-B\), removes the odd orders.  If

\[
A(\theta)=t\int_0^1V_a(Q_a(z)+\theta B_s)ds,
\]

then

\[
\partial_\theta^4e^{-A}
=e^{-A}\left[(A')^4-6(A')^2A''+3(A'')^2
+4A'A'''-A^{(4)}\right].
\]

Split at \(\sigma_*=L+8\log L\).  On \(\sigma\le\sigma_*\), put
\(Y=e^{\sigma-L}\).  The preceding geometric estimates give

\[
|\partial_\theta^4e^{-A}|
\le C_aM^4(1+\sigma)^4
\sum_{m=1}^4Y^me^{-c_aY}.
\]

Since \(d\sigma=dY/Y\) after radial integration, its main-region spatial
integral is \(O_a(L^4)\).  On the tail, the lower path potential is at least

\[
\exp\bigl((1-\alpha_L)\sigma-L-\alpha_L\bigr),
\qquad
\alpha_L=C_a(\delta/L+\delta^2/L^2),
\]

whose value at \(\sigma_*\) is at least \(L^7\) for small \(t\).  The upper
potential differs only by a power \(1+O_{a,\delta}(L^{-1})\).  The tail is
therefore an incomplete-Gamma integral and is \(O_{a,N}(L^{-N})\) for every
fixed \(N\).  Consequently,

\[
\int\sup_{|\theta|\le\varepsilon}
\mathbb E[\mathbf1_{G_t}|\partial_\theta^4e^{-A}|]dz
=O_a(L^4).
\]

The bad event is controlled without an infinite-volume loss.  Pathwise
Jensen and translation invariance give

\[
\int e^{-t\int_0^1V_a(q+w_s)ds}dq
\le\int e^{-tV_a(q)}dq=E_1(2\pi t)=O(L).
\]

Thus all bad-event terms, including the restricted second derivative, are
super-exponentially smaller than \(t^2L^4\).  To justify differentiating the
bad-event expectation, the exact polynomial displacement gives, for fixed
\(z,t\) and \(|\theta|\le\theta_0\),

\[
|\partial_\theta^2e^{-A(\theta)}|
\le C_{a,z,\theta_0}(1+M)^{10};
\]

this is integrable because the bridge maximum has Gaussian tails.  It follows
that

\[
\int\left|F_a(\varepsilon,z)-F_a(0,z)
-\frac{\varepsilon^2}{2}F_a''(0,z)\right|dz
=O_{a,h}(t^2L^4).
\]

Finally, the bridge covariance identities \(1/12\) and \(1/6\) give

\[
F_a''(0,z)=e^{-tV_a}
\left[\frac{t^2}{12}|\nabla V_a|^2-\frac t6\Delta V_a\right].
\]

The integration by parts below is obtained with expanding cutoffs; its cross
term vanishes because \(e^{-tV_a}|\nabla V_a|\in L^1\).  Using

\[
\int e^{-tV_a}\Delta V_a=tI_a(t)
\]

and the free-kernel prefactor yields \(-t^2I_a/(48\pi)\).  Subtract the
\(a=0\) expansion and use the pointwise classical cancellation.  This proves
the lemma.  The differentiability, domination, tail substitution, and bad
second-derivative estimates are written out in full in
`R300_P1_UNIFORM_REMAINDER_PROOF.md`. ∎

## Corrections or missing assumptions

- No extra assumption is needed for strict ground-state non-isospectrality
  beyond the standard rearrangement equality theorem.
- The full heat asymptotic is now proved by Lemma 6.  A local
  Wigner--Kirkwood series alone would still be insufficient; the proof uses a
  global Brownian good/bad decomposition and exact classical cancellation.

## Open risks

- The trace-norm form of the Trotter convergence used for the separate
  supporting all-\(t\) heat inequality should be cited precisely before
  publication; Claim 2 does not depend on that inequality.
- The equality theorem for Pólya--Szegő should be cited with hypotheses that
  match an analytic positive ground state on \(\mathbb R^2\).
- None of these results produces rational-prime times or amplitudes.  P and Z
  remain open.

## Primary equality-case citation

J. E. Brothers and W. P. Ziemer, “Minimal rearrangements of Sobolev
functions,” *Journal für die reine und angewandte Mathematik* **384** (1988),
153--179, https://doi.org/10.1515/crll.1988.384.153.
