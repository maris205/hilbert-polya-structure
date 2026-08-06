# R106 — Independent Adaptive Magnetic-Dynamics Audit

## Purpose

Use a different integrator to replicate the R001 \(B=0\) signal and test the
classical \(B=1\) branch used by the quantum crossover.

## Frozen design

- Read the exact initial \((q,v)\) states and scale factors for seeds 0--3
  from R001 at \(E=1000\).
- Cells: \((a,B)=(0,0),(0,1),(1.02,0),(1.02,1)\), all with \(n=1\).
- Integrate 80 natural units with SciPy DOP853, `rtol=1e-10`, `atol=1e-12`,
  and analytic variational equations.
- Renormalize two tangent vectors every 0.5 natural units.
- Use physical velocity equations
  \[
    \dot q=v,\qquad
    \dot v=\begin{pmatrix}0&B\\-B&0\end{pmatrix}v-\nabla V(q).
  \]

The potential jet is independently reimplemented inside the audit script; it
does not call the Verlet stepper.

## Gates

- every trajectory completes with relative energy drift below \(10^{-8}\);
- radial \(B=0,1\) cells have zero joint FTLE/SALI flags at 80;
- nonlinear \(B=0,1\) cells have at least 3/4 joint flags;
- the nonlinear \(B=0\) DOP853/Verlet median FTLE ratio lies in \([0.7,1.3]\).

These are deterministic replication gates, not positive-measure claims.
