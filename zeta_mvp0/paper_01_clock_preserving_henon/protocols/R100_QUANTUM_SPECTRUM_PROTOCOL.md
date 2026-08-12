# R100 — Zero-Input Quantum Spectrum Pilot

## Question

Does the \(a=1.02\) warped operator, which has sampled chaotic diagnostics,
have quantum level
repulsion distinct from the radial control, and does a magnetic extension
move the available antiunitary symmetry from the orthogonal toward the unitary
class without changing the classical mean clock?

No prime or zero array is loaded by this protocol.  The frozen
\(a=1.02\) value nevertheless comes from an earlier RH-motivated,
zero-exposed lineage and is not described as statistically blinded.

## Operators

\[
 \mathcal H_{a,B}
 =\frac12(-i\nabla-A_B)^2
 +2\pi\exp\!\left(\pi|\widetilde H_a(q)|^2\right),
\qquad
 A_B=\frac B2(-y,x).
\]

The momentum translation \(p\mapsto p-A_B(q)\) preserves classical phase
volume, so the exact classical Q/W clock is independent of \(B\).  At
\(B=0\), complex conjugation is an antiunitary symmetry with \(T^2=+1\), so
GUE is not expected.  At fixed nonzero \(B\), ordinary time reversal maps the
operator to the \(-B\) member and is not an internal symmetry.

## Discretization

- Gauge-covariant Peierls finite differences in symmetric gauge.
- Dirichlet rectangle enclosing the preimage of the potential contour
  \(V=100E_{\rm target}\), plus three nominal grid steps.
- Shift-invert Hermitian Lanczos.
- Smoke: 60 eigenvalues on a coarse grid for \((a,B)=(0,0),(1.02,0),(1.02,1)\).
- Production target after smoke: at least 180 eigenvalues on two or more grids
  for the radial, scalar \(a=1.02\), magnetic \(a=1.02\), and feasible
  \(a=6\) controls.

## Frozen diagnostics

- ordered eigenvalues and grid metadata;
- exact-clock unfolded mean spacing;
- adjacent spacing ratio, which needs no fitted unfolding;
- near-degeneracy fraction;
- per-level coarse/refined convergence over an interior mode window.

Reference means are Poisson 0.3863, GOE 0.5359, and GUE 0.6027.  Distances to
these constants are descriptive only; no i.i.d. p-values are assigned.

## Validity gates

1. Matrix Hermiticity defect below \(10^{-12}\) in tests.
2. Highest used level lies well below the boundary wall energy.
3. The interior median coarse/refined relative level change is below 1%; if it
   is larger, no RMT-class interpretation is permitted.
4. Statistics discard at least 25 low levels and 15 upper edge levels.
5. No zeta ordinate or prime list is loaded.

## Claim boundary

Finding GOE- or GUE-like ratios would supply only a finite-window R
diagnostic.  It would not pass P; Z remains untested and unauthorized before
P.  It would not produce the explicit formula, a prime trace, individual zeta
zeros, or RH.
