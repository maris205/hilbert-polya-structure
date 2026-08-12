# Theorem package

## T1. Adelic Hénon quantization

With the standard self-dual adelic Fourier transform,

\[
\mathcal U_H=\mathcal F_{\mathbb A}\mathcal M_{2q^3-q}
\]

is unitary on \(L^2(\mathbb A_{\mathbb Q})\), is a restricted tensor product,
and quantizes

\[
H_6(q,p)=(1-6q^2-p,q).
\]

For every finite prime \(p\),
\(\mathcal U_{H,p}1_{\mathbb Z_p}=1_{\mathbb Z_p}\).

## T2. Theta stabilizer

On the adelic Schwartz space,

\[
\Theta(\mathcal U_Hf)=\Theta(f).
\]

This follows from adelic Poisson summation and
\(\psi(2r^3-r)=1\) for \(r\in\mathbb Q\).

## T3. Mother-range equivalence

Let

\[
E(g)(x)=E_\times(g)(x)
=|x|^{1/2}\sum_{r\in\mathbb Q^\times}g(rx).
\]

This full adelic convention is essential: its positive-integer real
half-model applies only in an even sector, which the odd cubic chirp does not
preserve.

Let

\[
\mathcal S_0=\{g:g(0)=\widehat g(0)=0\}
\]

and

\[
\mathcal S_H=\{f:f(0)=\widehat{\mathcal M_{P_6}f}(0)=0\}.
\]

Then \(\mathcal M_{P_6}:\mathcal S_H\to\mathcal S_0\) is a bijection and

\[
E\mathcal U_H(\mathcal S_H)=E(\mathcal S_0).
\]

This is an exact Hénon presentation of the standard scaling spectral range.
It does not prove that the Hénon kick is essential.

## T4. Raw-unitary Euler-product obstruction

For every \(p\)-dimensional unitary \(U_p\), all \(p\) eigenphases give a
zero of

\[
\det(I-p^{1/2-s}U_p)
\]

within \(\pi/\log p\) of \(s=1/2\). Hence a product over unbounded primes
has an interior zero accumulation point unless an exact cancellation is
separately supplied. The raw finite-field critical-line product is not a
nonzero meromorphic candidate.

## T5. Exact cubic ball integral

For \(p>3\) and \(m\ge0\),

\[
\int_{p^{-m}\mathbb Z_p}\psi_p(2x^3-x)\,dx=1.
\]

Equivalently, the complete sum

\[
S_{p,m}=\sum_{u\bmod p^{3m}}
\exp\!\left(2\pi i\frac{2u^3-p^{2m}u}{p^{3m}}\right)
\]

satisfies \(S_{p,m}=p^2S_{p,m-1}\), \(S_{p,0}=1\).

## T6. Same-space noncompactness

For

\[
e_{p,m}=p^{-m/2}1_{p^{-m}\mathbb Z_p},
\]

one has \(e_{p,m}\rightharpoonup0\) and

\[
\|(\mathcal M_{P_6}-I)e_{p,m}\|^2=2-2p^{-m}.
\]

Therefore \(\mathcal M_{P_6}-I\) is not compact on
\(L^2(\mathbb Q_p)\). A naive same-space relative Fredholm determinant is
stopped.

## T7. Static range-pair theorem

Let

\[
V=\ker(ev_0),\quad
\mathcal S_0=V\cap\ker\Lambda_0,\quad
\mathcal M_P\mathcal S_0=V\cap\ker\Lambda_{-P}.
\]

Their common subspace
\[
W=V\cap\ker\Lambda_0\cap\ker\Lambda_{-P}
\]
has quotient dimension at most one in each hyperplane. After applying any
common linear map, the algebraic image quotients still have dimension at
most one. If both images extend to closed subspaces of one Hilbert
completion, the corresponding orthogonal projections satisfy

\[
\operatorname{rank}(P_H-P_0)\le2.
\]

This is a static fixed-phase rank bound. It does not imply two dynamical
scattering channels.

## T8. Infinite scaling-orbit obstruction

For \(D_af(x)=|a|^{1/2}f(ax)\),

\[
D_aM_{P_6}D_a^{-1}=M_{P_a},
\qquad P_a(x)=2a^3x^3-ax.
\]

The archimedean kernels

\[
\phi_a(z)=\exp[-2\pi i(2a^3z^3-az)],\qquad a>0,
\]

are linearly independent. A finite real-axis relation extends to an entire
identity, while on \(z=re^{i\pi/6}\) the largest \(a\) has the unique
dominant growth \(e^{4\pi a^3r^3+O(r)}\). Therefore

\[
\dim\operatorname{span}\{\Lambda_{-P_a}:a>0\}=\infty
\]

before applying the Poisson/scaling map. Consequently T7 cannot be promoted
to finite-channel dynamics without a new quotient or renormalization
theorem.

## T9. Exact Poisson boundary-defect identity

For the same full nonzero-rational scaling map

\[
E_\times(g)(x)=|x|^{1/2}\sum_{r\in\mathbb Q^\times}g(rx),
\]

Poisson summation gives

\[
E_\times(\widehat g)(x)
=E_\times(g)(x^{-1})
+|x|^{-1/2}g(0)-|x|^{1/2}\widehat g(0).
\]

Consequently, if \(g=M_{P_a}f\) and \(f(0)=0\), then

\[
E_\times(\mathcal F M_{P_a}f)(x)
=E_\times(M_{P_a}f)(x^{-1})
-|x|^{1/2}\Lambda_{P_a}(f).
\]

The output defect therefore lies in one common asymptotic mode at each
scale, although its coefficient functionals span an infinite-dimensional
family. This is an exact candidate compression mechanism, not a proof of a
finite-channel scattering theory or determinant class. The static family is
\(\Lambda_{-P_a}\), while this identity contains \(\Lambda_{+P_a}\); both
are separately infinite-dimensional and are not identified. Moreover,
\(|x|^{\pm1/2}\) are boundary modes whose membership in the scaling Hilbert
completion is not asserted, so T9 is not a bounded finite-rank operator
statement.

## Conditional promotion theorem

Assume a genuine scaling-site Hénon bundle/cocycle exists and a canonical
Poisson-renormalized or crossed-product anomaly determinant satisfies

\[
\Delta_H(s)\Delta_H(1-s)=1,\qquad
\Delta_H(s)=e^{g_H(s)}
\]

with \(g_H\) entire. Then

\[
D_H(s)=\xi(s)\Delta_H(s)
\]

has exactly the Riemann divisor and inherits the completed functional
equation up to the reciprocal Hénon factor.

The hypotheses of this conditional theorem are the next large gate; they
are not claimed here.
