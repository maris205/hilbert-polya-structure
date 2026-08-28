# C213 source and ownership audit

## Source lock

- Owner: the Markov velocity-jump semigroup on
  \(L^2(\mathbb T_{2\pi}\times\{\pm1\})\), with uniform invariant measure.
- Parameters: real \(c,\lambda\geq0\); clock: physical elapsed time.
- Generator: \(Lf=c v\partial_xf+\lambda(f(x,-v)-f(x,v))\).
- Fourier convention: integer modes \(k\in\mathbb Z\), normalized circle
  measure; the finite determinant is only the two-by-two characteristic
  polynomial of \(G_k\).
- Route evaluator: `flow_systems/skills/route-a-evaluator.md` v0.2.0,
  SHA-256 `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.

## Prior-work collision boundary

The repository has several unrelated finite-state, delay and PDE controls.
None owns this circle telegraph process together with its all-mode Jordan,
gap and essential-norm theorem.  This is a repository-relative ownership
check, not a literature-priority claim.

## Evidence boundary

The producer emits 700 exact/high-precision block rows and 25 gap rows.  The
checker reconstructs every matrix entry and eigenvalue without importing the
producer; SymPy independently verifies the block polynomial, telegraph
elimination, critical condition and gap identity.  The finite grid is not a
proof of an infinite quantifier.  No target tables, fitted values or external
observations enter the receipt.

The strict evaluator tuple is
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`.  Scope literal is
`NO_BAD_EULER_OR_ROOT_NUMBER`; Route B is not authorized.
