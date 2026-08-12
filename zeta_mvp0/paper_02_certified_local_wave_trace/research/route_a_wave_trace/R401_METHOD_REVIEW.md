# R401 Numerical-Method Review

## Review mechanism

The external review MCP was unavailable.  An independent secondary-agent
audit was used before the production run.  No external-model score is
claimed.

## Rejected first design

The first proposed solver used product Hermite functions directly in the
original configuration coordinates.  That design was rejected before any
R401 result was archived.  Along the warped tail,

\[
 |\Psi_a(x,y)|^2\sim a^2x^4,
 \qquad
 V_a(x,y)\sim e^{\pi a^2x^4},
\]

whereas every finite Hermite combination has only Gaussian decay.  Hence

\[
 \langle\phi,V_a\phi\rangle=\infty
\]

for a generic nonzero Hermite function.  Finite Gauss--Hermite quadrature
would have produced a finite order-dependent surrogate for a divergent
matrix element.  Such values are not Ritz values and are inadmissible as
spectral evidence.  The initial module and tests were removed; no result
directory was produced with that method.

## Accepted exact-coordinate repair

The area-preserving polynomial map gives an exact unitary change

\[
 u=\Psi_a(q),\qquad dq=du.
\]

If \(J=D\Psi_a\), the kinetic quadratic form becomes

\[
 \frac{\hbar^2}{2}\int
 \nabla_u f^T G(u)\nabla_u f\,du,
 \qquad
 G(u)=J(\Psi_a^{-1}u)J(\Psi_a^{-1}u)^T.
\]

For the one-step centered map and \(u=(u,v)\),

\[
 G(u,v)=
 \begin{pmatrix}
 1+(c+2av)^2&-(c+2av)\\
 -(c+2av)&1
 \end{pmatrix}.
\]

Write \(G(0)=LL^T\), with \(\det L=1\), and let \(u=Lz\).  The reviewer
independently checked

\[
 B(z)=L^{-1}G(Lz)L^{-T},\qquad B(0)=I,
\]

and the residual form sign

\[
 +\frac{\hbar^2}{2}
 \int\nabla\phi_m^T(B-I)\nabla\phi_n\,dz.
\]

The transformed potential is

\[
 2\pi e^{\pi(s_-^2z_-^2+s_+^2z_+^2)}.
\]

Product Hermite functions are therefore in the potential form domain for
\(\hbar<2/s_+\), comfortably satisfied by R401.  The accepted implementation
uses the quadratic form directly, so it cannot omit the first-order terms
that would appear when expanding the divergence-form operator strongly.

## Implementation corrections required by review

Before production, the review required and the implementation adopted:

1. Gauss--Hermite order at least the maximum occupied degree plus three,
   with larger production margins;
2. preservation of the assembled matrix when computing Ritz residuals,
   rather than using `eigh(overwrite_a=True)` and then reading overwritten
   storage;
3. recording the pre-symmetrization defect before explicit symmetrization;
4. a separate \(\delta=0.01\) trace window with \(\chi(E)=1\);
5. the accepted \(T/(2\pi\sqrt D)\), not \(T/\sqrt D\), amplitude;
6. an independent angular-momentum Laguerre solver for the radial spectrum;
7. an exact harmonic finite-window oracle to expose pre-asymptotic
   oscillations.

## Audit result

At \(a=0\), transformed Cartesian and radial Laguerre spectra agree to
approximately \(10^{-14}\) in diagnostic and production comparisons.  All
R401 nested-basis phase budgets, quadrature checks, internal residuals, and
radial-oracle gates pass.  The no-production-import checker independently
recomputed the cutoffs, Fourier integral, harmonic spectra, theory
coefficient, normalized traces, scientific gates, and archive hashes; all 58
checks passed.

## Verdict

\[
 \boxed{
 \text{REJECT original-coordinate Hermites;}
 \quad
 \text{ACCEPT exact-coordinate transformed Galerkin for R401-SC.}}
\]

This is a numerical-method verdict, not a claim that the numerical
\(\delta=0.01\) lies inside the theorem's nonquantitative small-energy
threshold.
