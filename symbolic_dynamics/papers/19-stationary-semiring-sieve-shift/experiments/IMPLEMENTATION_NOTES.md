# SD-C21 Implementation Notes

## Scientific representation

- `F_m boxtimes F_n=F_mn` is implemented by integer multiplication.
- `F_m boxplus F_n=F_m+n` is an alphabet-sum operation on the full-shift
  skeleton, not a categorical coproduct of subshifts.
- Additive order is ordinary integer comparison transported with both
  semiring operations under relabeling controls.
- States `Q:n:d:q` explicitly materialize cofactor search.  The scientific
  source contains no `tensor_divides`, `exists_factor`, `factor_exists`, or
  `has_factor` identifier.
- Rejecting computations enter a one-way cemetery ray.  A reject self-loop is
  forbidden because it would create a false primitive orbit.

## Weighted adjacency

The vertex Hilbert space is `ell^2(V)`.  Every edge is a rank-one arrival
term.  Input and accept-terminal denominators are `2n` and `nd`; entry into
`Q:n:d:2` has denominator `2nd`; later quotient and cemetery denominators are
`ndq` and `n(k+1)`; accept loops have denominator `n`.
These transient roofs are intrinsic semiring expressions but remain a frozen
`MODELING_CHOICE`.  They make the absolute entry sum trace class for
`Re(s)>1` and do not affect any closed-walk trace.

## Exactness

- Scientific support checks use an independently implemented Eratosthenes
  sieve only in validation, never to build the graph.
- Matrix entries and traces use `fractions.Fraction`.
- The independent finite determinant uses fraction-free Bareiss elimination.
- SCCs use deterministic Tarjan traversal.
- Fixed random seeds are `19021`, `19022`, and `19100..19131`.
- The source audit uses Python AST plus actual Q-state graph counts.

## Performance boundary

The expanded quotient graph is much larger than an existential-factor macro.
Therefore the dense determinant prefix is frozen at `N=8`, while exact SCCs
and traces use `N=24`.  This is a preregistered computational boundary, not a
best-prefix selection.

## Provenance boundary

The Route-A YAML initially contains
`PENDING_FIRST_ARTIFACT_COMMIT` for both source and code commits.  The paper
lead will replace both with the first authority artifact commit and seal the
manifest in a later metadata-only commit.  This integration performs no Git
operation.
