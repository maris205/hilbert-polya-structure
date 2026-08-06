# R107 — Independent Fourth-Order Quantum-Stencil Protocol

## Purpose

R100--R105 use one second-order gauge-covariant finite-difference family.
R107 asks whether the core finite-window conclusion survives a different
kinetic stencil.  The experiment is frozen before any fourth-order spectrum
is computed.

This is a discretization audit, not a search for a magnetic field and not a
test against zeta ordinates.

## Independent stencil

For each coordinate, approximate the covariant kinetic term by

\[
 -\frac12D_h^2\psi_i
 =
 \frac{5}{4h^2}\psi_i
 -\frac{2}{3h^2}
   \left(U_{i,i+1}\psi_{i+1}+U_{i,i-1}\psi_{i-1}\right)
 +\frac{1}{24h^2}
   \left(U_{i,i+2}\psi_{i+2}+U_{i,i-2}\psi_{i-2}\right).
\]

Here \(U_{ij}=\exp(-i\int_i^jA\cdot dq)\) is evaluated exactly along a
straight lattice link for either supported linear gauge.  Missing stencil
points are set to zero, giving a Dirichlet zero-extension closure.  The
potential wall lies far outside the target energy region, so boundary closure
error should be exponentially suppressed for the retained modes.

## Frozen cells and grids

- model: centered \(a=1.02,n=1\);
- fields: \(B=0\) and \(B=1\);
- target energy: 450;
- wall factor: 100;
- eigenvalues: 180;
- fourth-order nominal spacings: \(h=0.03\) and \(h=0.0225\);
- common analysis window: sorted modes 25--164 inclusive.

The independent reference is the already archived second-order \(h^2\)
extrapolation from R102, which was computed before R107 was designed.

## Frozen gates

For each field:

1. the fourth-order coarse-to-fine median relative level change is below
   0.5%;
2. the fourth-order fine spectrum and archived second-order extrapolation
   differ by less than 0.75% in median relative level position;
3. their mean adjacent-spacing ratios differ by less than 0.02;
4. their pointwise adjacent-ratio arrays have Pearson correlation above 0.90;
5. eigen-residual and Hermiticity unit tests pass.

Gauge covariance, \(B\leftrightarrow-B\), and zero-field reality are tested
at the matrix level.  All decisions are reported even if a gate fails.

## Interpretation

Passing would support stencil robustness of the finite-window scalar and
magnetic crossover signals.  It would not constitute a finite-element or
spectral-method replication, a high-energy universality theorem, an
arithmetic choice of \(B\), or evidence for individual Riemann zeros.

Failing kills the current cross-discretization claim and requires diagnosing
boundary closure, resolution, or second-order extrapolation before the RMT
language is retained.
