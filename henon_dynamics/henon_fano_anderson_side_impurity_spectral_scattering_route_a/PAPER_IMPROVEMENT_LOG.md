# Paper improvement log

## Round 0 — analytic core

- Froze the infinite-volume Hamiltonian and square-root normalization.
- Derived the Schur resolvent and proved exactly one simple pole on each
  physical band exterior.
- Added an explicit warning that the squared quartic is not the secular
  equation without branch constraints.

## Round 1 — substantive spectral/scattering extension

- Added the reflection-parity decomposition and cyclic eventually-free Jacobi
  argument proving pure absolute continuity in the band, multiplicity two,
  and absence of singular continuous spectrum.
- Fixed the resolvent convention: `G_dd=<d,(z-H)^(-1)d>` is anti-Herglotz,
  while `-G_dd` is Herglotz.  Added local-uniform Stone inversion, exterior
  pole-free measure exclusion, and both band-edge atom tests, so the absence
  of singular continuous spectrum no longer rests on an a.e. density alone.
- Derived the impurity density and residue weights and justified total mass by
  the Cauchy-transform asymptotic.
- Added exact amplitudes, probability conservation, and the if-and-only-if
  location of the Fano zero.

## Round 2 — boundary and integrity closure

- Added `g=0`, `J=0`, `epsilon=plus_or_minus 2J`, coupling-sign, and
  `g to 0` boundaries.
- Added evidence-role, hostile-test, source, and workspace-collision sections.
- Added the frozen Route-A tuple, scope firewall, Route-B lock, and AI-use
  disclosure.

The three rounds are intentionally content-distinct.  Final layout, reference,
font, text, raster, and deterministic-build status is recorded in
`paper/COMPILE_REPORT.md`.
