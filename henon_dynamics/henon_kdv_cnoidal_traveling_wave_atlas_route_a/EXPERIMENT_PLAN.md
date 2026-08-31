# Experiment and proof plan

## Analytic contract

1. Reduce the PDE with `xi=x-c*t`, integrate twice, and factor the resulting
   cubic by its roots.
2. Prove that a compact allowed interval exists only for three simple roots
   or for the lower-double-root homoclinic face.
3. Substitute the Jacobi `cn^2` profile and derive speed, modulus, wave
   number, fundamental period, mean, and mean square.
4. Take the soliton and harmonic limits without assigning a speed to a
   constant profile.
5. prove Galilean covariance and separate the stationary `c=0` circle face.

## Executable contract

- Produce twelve ordered rational-root rows at 90 decimal digits.
- Independently reconstruct period and two moments by endpoint-regularized
  quadrature rather than by the displayed elliptic formulas.
- Verify the profile ODE and first integral at independent elliptic-function
  nodes.
- Use SymPy to prove the cubic coefficient, `cn^2`, soliton, and Galilean
  identities over exact rational grids.
- Require clean-process byte replay and at least twenty repaired-hash semantic
  mutation rejections.
- Compile three substantively different paper rounds twice in fresh trees at
  `SOURCE_DATE_EPOCH=1788048000`, with embedded fonts and no final warning,
  reference, or layout defect.

Finite rows certify conventions and implementations.  The continuum theorem
is carried by the proof, not by sampling.
