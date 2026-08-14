# SD-C21 Obstruction Registry

## O21.1 — transient verifier invisibility

**Status:** proved for SD-C21.

Every input, divisor, quotient-search, and cemetery edge lies on no directed
cycle.  Hence it contributes zero to every power trace.  The full trace-class
operator is block triangular with diagonal recurrent block
`diag(p^(-s))`; deleting all transient edges preserves its Fredholm
determinant.

## O21.2 — exact-ledger pruning obstruction

**Status:** proved under positive nonzero formal edge weights and an orbitwise
exact Euler ledger.

If a recurrent strongly connected component contains two declared cycles or
one declared cycle plus another recurrent edge, connector paths produce an
additional primitive class.  Therefore an exact no-mixed ledger forces the
recurrent core to be a disjoint union of simple cycles.  Pruning transient
states and first-return contraction reduce it to a diagonal loop system.  Raw
graph-step fugacity must retain `z^length` under contraction.

Signed, complex, supertrace, or cancellation-based universalizations remain
open and are not claimed.

## O21.3 — universal total-decider compiler

**Status:** proved.

For any decidable support `S` with arbitrary finite runtime `T(n)`, give the
`t`-th computation edge denominator `n(t+2)`, send accepted inputs to an
`n^(-s)` self-loop, and send rejected inputs to a one-way cemetery ray.  For
`Re(s)>1`, the trace norm is bounded independently of runtime growth by a
product of two convergent Dirichlet series.  The determinant is

```text
product_(n in S) (1-z n^(-s)).
```

Thus the same symbolic compiler selects squares, powers of two, Fibonacci
numbers, hash predicates, polynomial irreducibles, or arbitrary effective
factorial-monoid atoms.  Exact Euler compilation alone has no RH-selective
force.

## Next smallest obligation

The next candidate must forbid verifier-generated accept self-loops and place
both semiring operations inside recurrent transitions on all nonunit objects.
It must establish primitive-cycle separation before any Fredholm continuation
or holonomy decoration is attempted.
