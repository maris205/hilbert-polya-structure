# HCS-C270: standard Heisenberg sub-Riemannian cut locus

This package gives a convention-complete theorem for the standard real
Heisenberg group `H^1`: its unit-speed Hamiltonian geodesics, exponential-map
Jacobian, first conjugate and cut times, identity cut locus, and exact distance
formula including the horizontal and vertical faces.

The theorem is `PROVABLE AS STATED`.  The evidence contains 800 trajectory
rows, 64 nonvertical distance rows, 12 vertical-boundary rows, and 10,972
numeric cells independently recounted from an explicit field schema.  An
independent checker, symbolic derivation, byte replay, and repaired-hash hostile
mutation suite guard the result.

Complete geodesics have no nontrivial closed orbits, so the Route-A tuple uses
`A1_FAIL` and the verdict is `ROUTE_A_REJECTED`; the scope literal is
`NO_BAD_EULER_OR_ROOT_NUMBER`.  No general Carnot-group theorem, arithmetic
local data, or target operator is claimed.

See `THEOREM_PACKAGE.md`, `results/TEST_REPORT.md`, and `paper/main.pdf`.
