# C196 narrative report

## Material progress

C196 moves one whole classical dynamical model from arbitrary initial data to
its complete scattering geometry.  The Hermitian pencil is not merely a
trajectory formula: its rank-one commutator proves all-time simplicity,
converts eigenvalue perturbation into the exact Newton force, yields global
completeness and all trace invariants, and constructs both directions of a
global spectral atlas.

The negative-time end is treated separately.  Multiplication by negative
time reverses eigenvalue order, so spectral line `m` enters with rank
`N+1-m` and exits with rank `m`, while its intercept remains attached to that
line.  Distinct asymptotic velocities then rule out bounded nonconstant
periodic motion.

## Evidence separation

The infinite statement is proved by rank, commutator, perturbation, and ODE
arguments under the classical Moser source lock.  The 18 finite systems only
catch sign, pair-factor, atlas-denominator, or implementation defects.  The
checker is algorithmically distinct: realified Jacobi eigenvalues, polynomial
projectors, and centered differences replace the producer's LAPACK
eigenvector path.  SymPy is a third exact route.

## Deliberate stopping boundary

`g=0`, coincident initial data, `N=1`, and other Calogero families are not
blurred into the theorem.  No periodic-orbit zeta is attached to an unbounded
flow without bounded periodic motion.  The inverse-square quantum Hamiltonian
is acknowledged only at the natural Friedrichs-realization level, never as a
target spectrum.

The verdict is
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`, overall
rejected, Route B false.
