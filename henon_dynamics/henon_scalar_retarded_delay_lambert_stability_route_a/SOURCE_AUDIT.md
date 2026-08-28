# C210 source and ownership audit

## Source lock

- Owner: the scalar retarded history semigroup on
  \(C([-\tau,0];\mathbb C)\), with the boundary generator stated in
  `THEOREM_PACKAGE.md`.
- Parameters: real \(a,b,\tau\geq0\); clock: physical time \(t\).
- Normalization: sup norm on histories and the fundamental solution
  \(r(0)=1\), \(r(t<0)=0\).
- Determinant convention: \(\Delta(\lambda)=\lambda+a+b e^{-\lambda\tau}\)
  is a characteristic function, never a target or Fredholm determinant.
- Route evaluator: `flow_systems/skills/route-a-evaluator.md` v0.2.0,
  SHA-256 `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.

## Prior-work collision boundary

The repository contains several discrete memory, renewal, transport and
stochastic controls.  None owns a continuous retarded functional-differential semigroup with the
Lambert-branch, eventual-compactness and all-delay Hopf atlas frozen here.
This statement is repository-relative and is not a literature-priority claim.

## Evidence boundary

The producer emits exact rational method-of-steps strings for twelve parameter
sentinels and three symbolic Hopf controls.  The checker re-derives every row
without importing producer code; SymPy independently verifies the Lambert
substitution, derivative/multiplicity criterion, Laplace term and Hopf modulus.
No target tables, fitted values or external observations enter the receipt.

The strict evaluator tuple is `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`.
Scope literal is `NO_BAD_EULER_OR_ROOT_NUMBER`; Route B is not authorized.
