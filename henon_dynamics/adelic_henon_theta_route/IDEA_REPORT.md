# C35 big-door idea report

## Executive decision

Four all-period directions were compared.  The selected direction is the
adelic Hénon--theta construction because it is the only one that immediately
produces one global Hilbert space, a genuine nonlinear Hénon quantization,
an exact prime clock, and an exact Riemann spectral-range bridge.

The selection is not based on a finite zero fit.  No Riemann zeros were used.

## Candidate landscape

| Rank | Candidate | Decisive result | Decision |
|---:|---|---|---|
| 1 | Scaling-covariant adelic Hénon--Tate anomaly | Same-space perturbation is noncompact; fixed-phase rank is at most two, but the scaling orbit is infinite and forces a Poisson/crossed-product theorem | `GO_BIG_DOOR` |
| 2 | Maxwell--Hill Kummer all-period tower | Strong fixed-period Galois data, but no compatible finite-rank cross-period object; a global tower would be infinite rank | `CONDITIONAL_LONG_ROUTE` |
| 3 | Hénon--Mayer modular deformation | A full determinant route exists at the modular parent, but a Hénon rewriting is a coordinate/grafting control and generic deformation destroys arithmetic scattering | `CONTROL_ONLY` |
| 4 | Adapted-domain adelic Hénon--theta presentation | Exact mother-route compatibility, but Hénon can be removed by transport | `CONTROL_ONLY` |
| 5 | Raw prime product of finite-field Hénon unitaries | Critical-line normalization creates a zero accumulation point; standard normalization has local degree growing like \(p\) | `STOP_THEOREM` |

## Candidate 5 hard kill

For a \(p\)-dimensional unitary \(U_p\), consider

\[
D_{p}(s)=\det(I-p^{1/2-s}U_p).
\]

If \(e^{i\theta_{p,j}}\) is an eigenvalue, its zero set is

\[
s=\frac12+
i\frac{\theta_{p,j}+2\pi k}{\log p},
\qquad k\in\mathbb Z.
\]

For every \(j\), choose \(k\) so the numerator lies in \([-\pi,\pi]\).
Every prime therefore contributes \(p\) zeros within distance
\(\pi/\log p\) of \(1/2\).  The point \(1/2\) is a zero accumulation point,
so the unordered product cannot define a nonzero meromorphic function unless
an independently justified cross-prime cancellation is supplied.

This is a stronger obstruction than lack of numerical evidence: local
unitarity alone manufactures a false critical line.

## Why the selected route is a large step

The adelic mother model repairs two old structural failures at once.

1. The finite-field family \(\{U_p\}\) becomes the local shadow of one
   restricted adelic unitary \(\mathcal U_H\).
2. The real generating-function constant gauge becomes invisible under the
   canonical global character, rather than rotating the determinant.

The exact prime orbit structure comes from the scaling site, where
\(C_p=\mathbb R_+^*/p^{\mathbb Z}\) has length \(\log p\).  The Hénon
quantization lives on the same adelic arithmetic space and fixes every
unramified local vacuum. No scaling-site cocycle identifying this fact with
orbit holonomy is yet constructed. Strict Route A requires that coupling;
the mother route alone is a transport control.

## Exact D+ pilot: static boundary versus the scaling orbit

Put

\[
I_{p,m}=\int_{p^{-m}\mathbb Z_p}\psi_p(2x^3-x)\,dx.
\]

For every \(p>3\) and \(m\ge0\), one has \(I_{p,m}=1\).  After clearing the
denominator, the complete cubic sum \(S_m\) satisfies

\[
S_m=p^2S_{m-1},\qquad S_0=1,
\]

because summing the last base-\(p\) digit forces the previous residue to be
divisible by \(p\).  This proves the claimed integral exactly.

The normalized ball vectors are weakly null, but

\[
\|(M_P-I)e_{p,m}\|^2\to2.
\]

Thus the direct same-space perturbation is not compact.

The fixed test-space geometry has a static low-rank behavior. Both \(S_0\) and
\(M_PS_0\) are hyperplanes in \(\ker(f\mapsto f(0))\).  Their common kernel
has codimension at most two.  Fourier transform and the common scaling map
therefore give algebraic image quotients of dimension at most one on each
side. If a common closed Hilbert realization exists, its projection
difference has rank at most two.

This does not persist as a finite-dimensional dynamic channel. Dilation
sends \(P\) to \(P_a(x)=2a^3x^3-ax\), and the associated archimedean phase
kernels are linearly independent for distinct positive \(a\). The
pre-Poisson boundary orbit is infinite-dimensional. The valid escape, if it
exists, is a scaling-covariant Poisson anomaly or crossed-product trace.

Poisson summation makes that escape concrete. With the full adelic
nonzero-rational normalization,

\[
E_\times(\widehat g)(x)=E_\times(g)(x^{-1})
+|x|^{-1/2}g(0)-|x|^{1/2}\widehat g(0).
\]

For \(g=M_{P_a}f\) with \(f(0)=0\), every scale therefore contributes its
boundary defect along the same output mode \(|x|^{1/2}\), even though the
coefficient functionals remain infinite-dimensional. This is the precise
candidate anomaly; the output mode is distributional/asymptotic and is not
yet known to lie in the scaling Hilbert completion, so it is not a
finite-channel or determinant theorem.

## Simpler-parent and random-phase controls

- Replacing the cubic phase by zero leaves the inherited scaling zeta
  unchanged. This proves the current Riemann divisor is inherited, not
  Hénon-generated.
- Replacing the phase by any integral polynomial also fixes all finite
  spherical vacua and the rational theta distribution.  Hence theta
  invariance is a broad rational-polynomial mechanism, not unique to H6.
- Replacing the local unitary phases by random phases retains the false local
  critical-line zero accumulation.  Hence that signal has no arithmetic
  specificity.

## Selected research question

Can a genuine scaling-site Hénon cocycle and canonical Poisson/crossed-product
renormalization turn the infinite dilation orbit into a nonconstant zero-free
factor satisfying \(\Delta_H(s)\Delta_H(1-s)=1\)?

## Full conditional success route

The shortest serious route is:

1. retain the scaling-site primitive orbits \(C_p\) and exact clock
   \(\log p\);
2. use \(\mathcal U_H\) to define a genuine scaling-site bundle/cocycle and
   its chronological holonomy;
3. prove a Poisson-renormalized or crossed-product trace formula for the
   infinite boundary orbit;
4. show the non-vacuum relative determinant equals \(e^{g_H(s)}\) with
   \(g_H\) entire;
5. transfer the known completion, functional equation, and zero counting to
   the Hénon determinant;
6. test whether the induced Hénon symmetry supplies a positive Weil form.

Step 1 is inherited and the separate local vacuum compatibility is exact.
Steps 2--4 are now the single scaling-covariance gate rather than a set of
small local experiments.
