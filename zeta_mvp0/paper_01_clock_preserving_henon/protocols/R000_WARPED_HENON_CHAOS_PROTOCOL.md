# R000 — Warped-Hénon Classical Chaos Protocol

> **Historical terminology note.**  This frozen protocol predates the current
> gate ledger.  Its positive-measure language was an aspiration, not an
> achieved claim.  The run supplies only zero-input, sampled S diagnostics;
> the inherited \(a=1.02\) parameter itself comes from an earlier
> RH-motivated, zero-exposed lineage and is not statistically blinded.

## Frozen question

Does the currently evaluated zero-input operator

\[
 \mathcal H_{a,n}=-\frac12\Delta
 +2\pi\exp\!\left(\pi|\widetilde H_a^n(q)|^2\right)
\]

retain a numerically stable positive-measure chaotic component, in contrast
with its exact radial control \(a=0\)?  Here \(\widetilde H_a\) is the Hénon
map centered at its positive fixed point.  Centering is an affine
area-preserving conjugacy and does not change the exact mean clock.

No Riemann zero ordinate, prime table, or fitted spectral target is loaded.

## Design

- Smoke calibration: \(a\in\{0,1.02,6\}\), \(n\in\{1,2,3\}\),
  \(E\in\{10^2,10^3\}\), two seeds, eight natural units, and 128 steps
  per natural unit.  It is retained as a stiffness/failure record only.
- Production cells:
  \((a,n,s)=(0,1,2048),(1.02,1,4096),(6,1,8192),(1.02,2,8192)\),
  where \(s\) is the primary steps per natural unit, at
  \(E\in\{10^2,10^3\}\).
- Primary deterministic microcanonical sample: eight nonzero Sobol points per
  cell, uniform in configuration area in \(u=\widetilde H_a^n(q)\) and uniform
  in momentum angle, truncated at 0.88 of the allowed radius.
- Integrator: velocity Verlet with its exact analytic tangent map.
- Primary duration: 80 natural units, where
  \(t_{\rm nat}=\sqrt{\log(E/2\pi)/E}\).
- Refinement controls double \(s\) on the first two frozen seeds per cell.
- Renormalization: eight times per natural unit.

The smoke run showed that the original common step size was invalid for most
nonlinear cells.  It also showed enormous allowed-domain anisotropy for
\((a,n)=(6,2),(6,3)\), with nonfinite trajectories at the smoke resolution.
Those branches are not silently dropped: they remain explicit failed
high-distortion candidates, while production focuses on comparable, converged
cells.  The \((1.02,2)\) branch is retained because its calibrated resolution
remained computationally tractable.

## Recorded diagnostics

- dimensionless and physical-time maximal variational FTLE;
- SALI from two analytic tangent vectors;
- maximum relative energy drift;
- scaled angular-momentum range;
- upward Poincaré crossings and coarse occupancy;
- initial state, Sobol coordinates, step size, completion status, software and
  platform metadata.

## Numerical validity gates

1. A record is valid only if it completes, remains finite, and has maximum
   relative energy drift at most \(10^{-4}\).
2. A primary/refined pair is resolution-stable when the dimensionless FTLE
   changes by at most \(\max(0.02,0.25|\lambda|)\).
3. Any claimed chaotic fraction must be reported both with and without
   invalid trajectories; invalid high-distortion cases are not dropped.
4. The radial \(a=0\) control must show the expected decay toward zero before
   a positive threshold is interpreted dynamically.

## Exploratory retention gate

Retain the S branch only if, after duration and resolution checks, at least
10% of the sampled microcanonical states in one fixed \((a,n)\) family have

\[
 \lambda_{\rm nat}>0.05,
 \qquad \mathrm{SALI}<10^{-4},
\]

with a materially smaller fraction in the radial control.  This is a
pre-specified numerical screening rule, not a theorem about positive measure.

## Hard stops

- If high-energy/refined FTLEs decay like the radial control, demote B1 to a
  pure Q/W backbone.
- If \(n=3\) is numerically stiff, record the failure and do not infer chaos
  from unstable integration.
- Do not compute zero-fit error, nearest-zero matches, or RMT statistics until
  this classical gate is resolved.
