# R001 — FTLE/SALI Time-Length Convergence

## Purpose

R000 separates the nonlinear centered Hénon warps from the exact radial
control after 80 natural time units.  R001 tests whether that separation has
the correct time dependence: finite-time shear in the integrable radial
control should decay, whereas nonlinear FTLE should remain order one and SALI
should remain aligned.

## Frozen design

- Energy: \(E=1000\).
- Cells: \((a,n)=(0,1),(1.02,1),(1.02,2),(6,1)\).
- Seeds: Sobol indices 0, 1, 2, 3.
- One 160-natural-unit trajectory per cell/seed, with checkpoints at 20, 40,
  80, and 160.
- Steps per natural unit: 4096, 8192, 16384, and 16384 respectively.  These
  equal or exceed the R000 refinement resolutions.
- Same analytic tangent-Verlet implementation and \(10^{-4}\) energy-drift
  validity gate as R000.

## Retention checks

1. Every record must be finite and energy-valid.
2. The radial median SALI at \(t=160\) must exceed \(10^{-3}\), and its median
   FTLE magnitude must be materially below the nonlinear medians.
3. For each nonlinear family, at least three of four seeds must have
   \(\lambda_{160}>0.05\) and \(\mathrm{SALI}_{160}<10^{-8}\).
4. The nonlinear median plateau ratio
   \(\lambda_{160}/\lambda_{80}\) must lie in \([0.6,1.4]\).

These are deterministic screening rules, not statistical confidence claims.
