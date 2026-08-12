# Derivation Package

## Target

Derive a broad family of explicit Hénon-based Schrödinger operators that pass
the Hilbert--Pólya quantum-object gate Q and the two-growing-term mean-clock
gate W without using zeta-zero data.

The primary object is

\[
  \mathcal H_\Psi=-\frac12\Delta+2\pi e^{\Phi_\Psi(q)},
  \qquad
  \Phi_\Psi(q)=\pi|\Psi(q)|^2,
\]

where \(\Psi:\mathbb R^2\to\mathbb R^2\) is a proper area-preserving
diffeomorphism.  The final manuscript's concrete family takes
\(\Psi=\widetilde H_a^n\); the uncentered \(H_a^n\) is an affine-conjugate
Q/W variant and is not used to infer the manuscript's reflection symmetry.

## Status

**COHERENT AS STATED** for Q, the exact classical clock, and the quantum two
growing terms for every fixed Hénon iterate.  Chaos, random-matrix class,
prime-power trace, and zeta-zero identification remain experimental or open.

## Invariant Object

The invariant object is the configuration sublevel-volume function

\[
  A_\Phi(t)=\bigl|\{q\in\mathbb R^2:\Phi(q)<t\}\bigr|.
\]

The Riemann mean clock depends on this pushforward volume, not on the visual
shape of individual level sets.  Area-preserving warps can therefore change
the geometry and dynamics while leaving \(A_\Phi\), and hence the classical
clock, exactly unchanged.

## Assumptions

- \(\Psi\) is a proper orientation-preserving \(C^\infty\) diffeomorphism of
  \(\mathbb R^2\) with \(\det D\Psi=1\).
- For the quantitative quantum remainder, the length of
  \(\Psi^{-1}(\partial B_R)\) and the derivatives of \(\Phi_\Psi\) on
  \(\Psi^{-1}(B_R)\) grow at most polynomially in \(R\).
- The uncentered Hénon family is
  \(H_a(x,y)=(1-ax^2-y,x)\), with fixed real \(a\) and fixed iterate
  \(n\ge1\).
- The manuscript and numerical dynamics use the affine conjugate centered at
  the positive fixed point
  \(r_a=1/(1+\sqrt{1+a})\) for \(a>-1\).  When \(a\ne0\), this also equals
  \((\sqrt{1+a}-1)/a\):
  \[
    \widetilde H_a(\xi,\eta)
    =(-2ar_a\xi-a\xi^2-\eta,\xi).
  \]
  The theorem applies unchanged because this is again a proper
  determinant-one polynomial automorphism of the same degree.
- Counts include eigenvalues \(\le E\); strict counts are used inside the
  Dirichlet--Neumann proof to handle the Neumann zero mode correctly.

## Notation

- \(L(E)=\log(E/2\pi)\).
- \(\mathcal N_{\rm cl,\Psi}(E)\) is the four-dimensional semiclassical phase
  volume divided by \((2\pi)^2\).
- \(N_\Psi(E)\) is the quantum eigenvalue count.
- \(D=2^n\) is the polynomial degree of \(H_a^n\) for \(a\ne0\).

## Derivation Strategy

First express the mean clock only through the pushforward of configuration
area.  Then exploit the exact preservation of area under \(\Psi\).  Finally,
use energy-dependent square bracketing in physical coordinates; polynomial
distortion of a fixed Hénon iterate costs only powers of \(\log E\), which are
still dominated by the power saving \(E^{-1/4}\).

## Derivation Map

1. Two-dimensional momentum integration reduces the classical count to
   \((2\pi)^{-1}\int(E-V)_+dq\).
2. The change of variables \(u=\Psi(q)\) is exact because
   \(\det D\Psi=1\).
3. The remaining radial integral is the Paper 6 exponential integral and
   gives both growing Riemann--von Mangoldt coefficients exactly.
4. Properness gives confinement and compact resolvent.
5. Hénon polynomial distortion changes boundary length and potential
   derivatives by powers of \(\log E\), not powers of \(E\).
6. Dirichlet--Neumann bracketing with square size \(E^{-1/4}\) therefore gives
   an \(o(E)\) quantum remainder.
7. A unitary configuration change moves the Hénon warp from the potential into
   a determinant-one variable kinetic metric; it does not remove the geometry.

## Main Derivation

### Step 1 — exact phase-volume reduction (identity)

For \(E>2\pi\), the momentum disk at fixed \(q\) has area
\(2\pi(E-V_\Psi(q))_+\).  Hence

\[
\begin{aligned}
\mathcal N_{\rm cl,\Psi}(E)
 &=\frac1{(2\pi)^2}\int_{\mathbb R^2}\!dq
   \int_{|p|^2/2<E-V_\Psi(q)}\!dp\\
 &=\frac1{2\pi}\int_{\mathbb R^2}
   \bigl(E-2\pi e^{\pi|\Psi(q)|^2}\bigr)_+\,dq.
\end{aligned}
\]

### Step 2 — area-preserving clock invariance (identity)

Set \(u=\Psi(q)\).  Since \(dq=du\),

\[
  \mathcal N_{\rm cl,\Psi}(E)
  =\frac1{2\pi}\int_{|u|^2<L(E)/\pi}
    \bigl(E-2\pi e^{\pi|u|^2}\bigr)\,du.
\]

Polar integration gives

\[
  \boxed{
  \mathcal N_{\rm cl,\Psi}(E)
  =\frac{E}{2\pi}\log\frac{E}{2\pi}
   -\frac{E}{2\pi}+1.}
\]

Equivalently,

\[
  A_{\Phi_\Psi}(t)
  =|\Psi^{-1}(B_{\sqrt{t/\pi}})|=t.
\]
This identity is for \(t\geq0\); for \(t<0\) the sublevel area is zero.

### Step 3 — explicit Hénon warp (identity)

The map

\[
  H_a(x,y)=(1-ax^2-y,x)
\]

has Jacobian determinant one and inverse

\[
  H_a^{-1}(u,v)=(v,1-av^2-u).
\]

It is therefore a proper area-preserving polynomial automorphism.  For one
iterate,

\[
  \boxed{
  V_a(x,y)=2\pi\exp\!\left(
  \pi\left[(1-ax^2-y)^2+x^2\right]\right).}
\]

The parameter \(a=1.02\) now occurs in a static, real, confining operator
whose classical mean count is exact for every \(a\).  The value \(a=6\) is a
same-clock hyperbolic control.

For dynamics it is preferable to use

\[
 \widetilde V_{a,n}(q)
 =2\pi\exp\!\left(\pi|\widetilde H_a^n(q)|^2\right).
\]

Centering preserves the exact clock and all polynomial estimates, fixes the
origin, and makes \(a=0\) an exact radial control for every iterate.  It also
prevents iterates from being dominated by an irrelevant affine translation.

### Step 4 — the warp becomes kinetic geometry (identity)

Define the unitary map

\[
  (U_\Psi f)(u)=f(\Psi^{-1}(u)).
\]

If \(g=U_\Psi f\), then

\[
 \int|\nabla_q f|^2dq
 =\int \nabla_u g(u)^T G_\Psi(u)\nabla_u g(u)\,du,
\]

where

\[
 G_\Psi(u)=D\Psi(\Psi^{-1}u)D\Psi(\Psi^{-1}u)^T,
 \qquad \det G_\Psi=1.
\]

Thus \(\mathcal H_\Psi\) is unitarily equivalent to

\[
 -\frac12\nabla_u\!\cdot G_\Psi(u)\nabla_u
 +2\pi e^{\pi|u|^2}.
\]

The potential becomes radial, but the nonlinear Hénon geometry survives in a
variable determinant-one kinetic metric.  Only an affine orthogonal warp
would restore the original Euclidean operator.

### Step 5 — quantum scale separation (proposition)

For \(\Psi=H_a^n\), let \(D=2^n\).  On the allowed set
\(|H_a^n(q)|\le R\), polynomial inverse estimates give

\[
 \operatorname{length}\bigl((H_a^n)^{-1}(\partial B_R)\bigr)
 =O_{a,n}(R^D),
 \qquad
 \sup|\nabla\Phi_{a,n}|=O_{a,n}(R^D).
\]

At energy \(E\), \(R\asymp\sqrt{\log E}\).  Hence all geometric losses are
polylogarithmic.  With square side \(\ell=E^{-1/4}\), the accumulated
potential oscillation is

\[
 O_{a,n}\!\left(E\ell(\log E)^{1+D/2}\right)
 =O_{a,n}\!\left(E^{3/4}(\log E)^{1+D/2}\right)=o(E).
\]

The summed square lattice errors are smaller than the same envelope.  The
proof package supplies the strict-count bracketing details.

## Remarks and Interpretation

- This family decouples the mean clock from level-set geometry.  The clock is
  fixed by configuration area, while Hénon warping changes forces, orbit
  structure, and the quantum kinetic metric.
- Iterating \(H_a\) increases geometric complexity without changing the exact
  classical count.  Every fixed iterate remains compatible with a quantum
  \(o(E)\) remainder, although its logarithmic exponent worsens rapidly.
- The construction is not an inverse spectral fit.  No zero ordinate appears
  in \(V_{a,n}\).
- Passing Q/W plus displaying chaos would still not supply the Euler product.
  Prime-power periods and amplitudes remain a separate P gate.

## Boundaries and Non-Claims

- No claim is made that \(a=1.02\) is uniquely selected by the mean law; the
  mean law is intentionally independent of \(a\).
- Area preservation does not prove classical chaos, GUE statistics, or the
  absence of every antiunitary symmetry.
- The exact phase-volume identity does not identify individual zeta zeros.
- Fixed \(n\) is essential in the current quantum proof.  Letting the iterate
  grow with energy can turn polylogarithmic distortion into a power of \(E\)
  and requires a new analysis.

## Open Risks

- The one-iterate warped system may remain too regular; this is an empirical
  question, not answered by visual contour complexity.
- Strong anisotropy can cause finite-box and mesh bias in spectral pilots.
- Hénon iterates may produce chaos but also numerical stiffness.
- The P gate may remain absent even if Q/W/S and GUE-like diagnostics pass.
