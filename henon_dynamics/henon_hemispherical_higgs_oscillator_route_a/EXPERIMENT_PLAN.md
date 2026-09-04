# Exact verification plan

## Classical lane

Use 4 exact (R^2) values, 4 positive (omega) values, 8 positive radial
actions, 8 positive angular-momentum magnitudes, and both signs. The resulting
2,048 cells independently check (J,E), the turning polynomial, discriminant,
root certificates, action recovery, threshold, frequencies, and both periods.

## Quantum lane

Enumerate every ((N,n_r,m)) through (N=128). There are
(sum_{N=0}^{128}(N+1)=8,385) labels. Check energy coefficients,
multiplicities, Jacobi parameters, flat-limit coefficients, and the
(omega=0) Dirichlet label (l=N+1).

SymPy checks the general Jacobi differential equation and 27 direct radial
Schrödinger substitutions with several degrees, angular labels, and half-odd
integer values of nu.

## Revival lane

- 256 reduced rational (2\nu) controls, with exact (M_{min}), consecutive
  gaps, (k=1) global phase, and all phases through (k=129);
- 256 irrational controls (2\nu=\sqrt d) for nonsquare (d).

## Release lanes

Canonical producer, code-independent checker, SymPy verifier, two-directory
byte replay, repaired-hash hostile mutation, unittest smoke, three conditional
manuscripts built twice each in fresh directories, PDF audits, and an exact
35-payload self-excluded manifest.

Finite computation is a regression receipt, not proof by sampling.
