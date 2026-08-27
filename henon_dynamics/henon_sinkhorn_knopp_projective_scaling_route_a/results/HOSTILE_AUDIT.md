# C191 hostile audit

This is an internal artifact-bound audit, not external peer review and not a
novelty certificate.

The mutation suite recomputes the canonical payload hash after each semantic
attack.  It rejects 242 repaired-hash mutations covering candidate identity,
date, source commit, evaluator provenance, scope, every source-lock,
attribution, theorem, Route-A, scope-flag, progress/boundary and nonclaim field,
all four primary-source records, all aggregate finite counts, selected rows
across the zero-pattern census, every positive and boundary case, population
changes and ordering changes.  One additional stale-hash mutation is rejected.

High-risk rejected attacks include:

- collapsing support, total support and full indecomposability into one
  condition;
- claiming finite positive scaling factors from support alone;
- confusing uniqueness of the doubly stochastic representative with gauge
  uniqueness of its diagonal factors;
- replacing the full-cycle log Jacobian `S^T S` by `S^2` on the asymmetric
  sentinel;
- promoting the local rate `sigma_2(S)^2` to a global or dimension-only bound;
- treating a convergent fixed point as a nonconstant primitive-orbit owner;
- treating the finite zero-pattern census as the all-matrix proof;
- identifying an ordinary local characteristic determinant with a target
  divisor;
- enabling any target table, arithmetic local data, Euler-factor, root-number,
  automorphy, Hilbert--Polya or Route-B flag;
- promoting any member of the frozen all-fail Route-A tuple.

The independent checker and separate SymPy path strengthen implementation
confidence without claiming priority for the Sinkhorn--Knopp,
Brualdi--Parter--Schneider, Franklin--Lorenz or Knight results.  The package
makes no external-review or acceptance claim.
