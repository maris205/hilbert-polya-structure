# C213 exact theorem package

## Frozen owner

Let \(\mathbb T_{2\pi}=\mathbb R/(2\pi\mathbb Z)\), let
\(v\in\{+1,-1\}\), and let \(c,\lambda\geq0\).  On the normalized space
\(L^2(\mathbb T_{2\pi}\times\{\pm1\})\),

\[
Lf(x,v)=cv\,\partial_xf(x,v)+\lambda[f(x,-v)-f(x,v)].
\]

This is the backward (observable) generator on
$D(L)=H^1_{\rm per}(\mathbb T_{2\pi})\otimes\mathbb C^2$.  Densities evolve
under $L^*$; its Fourier blocks are $G_{-k}$, which have the same spectra and
norms as the blocks displayed below.

The clock is physical elapsed time.  For mode \(k\in\mathbb Z\), in the
ordered velocity basis \((+1,-1)\),
\[
G_k=\begin{pmatrix}-\lambda+ick&\lambda\\\lambda&-\lambda-ick\end{pmatrix},
\qquad N_k=G_k+\lambda I,
\qquad N_k^2=(\lambda^2-c^2k^2)I.
\]

## Theorem 1 — exact block and all-mode exponential

Writing \(\delta_k^2=\lambda^2-c^2k^2\),
\[
e^{tG_k}=e^{-\lambda t}\left(\cosh(\delta_kt)I+
\frac{\sinh(\delta_kt)}{\delta_k}N_k\right).
\]
The quotient is defined by continuity as \(t\) when \(\delta_k=0\).  Thus
the same expression is real-hyperbolic, oscillatory, or a single Jordan
exponential according to the sign of \(\delta_k^2\).  The eigenvalues are
\[
\rho_{k,\pm}=-\lambda\pm\sqrt{\lambda^2-c^2k^2}.
\]

## Theorem 2 — telegraph equation and spectral atlas

For \(c>0\) and total density \(\rho=f_++f_-\), eliminating the flux in the
adjoint equations gives
\[
\rho_{tt}+2\lambda\rho_t=c^2\rho_{xx}.
\]
For \(c>0,\lambda>0\), the sharp spectral-abscissa gap from the invariant
constant mode is
\[
g(c,\lambda)=
\begin{cases}
\lambda,&\lambda\leq c,\\
\lambda-\sqrt{\lambda^2-c^2},&\lambda>c.
\end{cases}
\]
It is zero on \(c=0\) or \(\lambda=0\).  This is not a claim of
constant-free \(L^2\) operator-norm decay: non-normal and critical blocks can
have polynomial transients.

At \(\lambda=c|k|>0\), mode \(k\) has one Jordan block at \(-\lambda\).
Mode zero has eigenvalues \(0,-2\lambda\).  If \(c>0,\lambda>0\), only
constant densities are stationary.  If \(c=0\), every common spatial profile
of the two velocities is stationary (infinite dimension); if \(\lambda=0\)
and \(c>0\), the stationary space consists of the two velocity-wise spatial
constants.

## Theorem 3 — essential and degenerate boundaries

For \(c>0,\lambda>0\), the high-frequency block limit gives essential norm
\(\|P_t\|_{\rm ess}=e^{-\lambda t}\) on the complement of constants; it is
nonzero, so the semigroup is not compact and belongs to no finite Schatten
class.  For \(c=0\) or \(\lambda=0\), the
essential norm is one.  The face \(\lambda=0\) is the same-clock unitary pair
of translations, while \(c=0\) is velocity-only mixing without spatial
decay.

The finite rows in the receipt are regression sentinels.  The displayed
identities, not the finite grid, carry the all-mode quantifiers.  The Fourier
characteristic polynomial is source-local and is not a Fredholm determinant,
target divisor, arithmetic zero, or Hilbert–Polya operator.
