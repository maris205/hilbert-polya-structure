# Source and claim audit — C120

## Source ownership

The source object is fully specified inside this package:

- `V(q)=q^4/4-q^2`;
- `F(q,p)=(q^3-2q-p,q)`;
- `S(q,Q)=qQ-V(q)` with convention `p=-S_q`, `P=S_Q`;
- `R(q,p)=(p,q)`;
- the named coordinate word `(0,1,-1)` and phase-space cycle.

No external dataset, orbit table, literature value, stochastic seed, or
floating-point fit enters the evidence. Novelty is deliberately unverified;
there are no external citations or reviewer scores.

## Independent evidence paths

1. The producer derives a canonical JSON receipt using exact SymPy algebra.
2. The checker reimplements the map, inverse, Jacobian, action, controls, and
   route boundary without importing the producer.
3. The symbolic cross-check derives the identities from fresh symbols.
4. Replay requires byte-identical regeneration.
5. Twenty-one hostile mutations probe model, orbit, monodromy, action,
   controls, target-prime/divisor nonclaims, all four route labels, and the
   firewall.

## Claim boundary

Certified: determinant one; two-sided polynomial inverse; `RFR=F^{-1}`;
three fixed points; one primitive period-three cycle; its exact monodromy and
action Hessian; three negative controls.

Not certified: a complete primitive-orbit atlas; a target prime
correspondence or log-prime clock; a source-owned dynamical zeta/Fredholm
object; a target divisor or global analytic structure; arithmetic or local
factors; Euler products; root numbers; automorphy; Hilbert–Pólya; or Route B.

The route labels follow `skills/route-a-evaluator.md` exactly:
`(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)`. Exact orbit/action data are
`PROVED` structural evidence, but they do not satisfy the missing Route-A
targets.

## Integrity controls

The package avoids implementation-as-evidence by requiring independent
recomputation. It avoids bug-as-insight by recording exact residuals for every
negative control. It avoids methodology fabrication by describing only
checks present in the executable scripts. The scope literal is
`NO_BAD_EULER_OR_ROOT_NUMBER`.
