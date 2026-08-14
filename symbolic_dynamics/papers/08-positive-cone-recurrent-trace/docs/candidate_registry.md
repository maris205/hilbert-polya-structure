# Candidate Registry

## SD-C10 — positive-cone recurrent trace

- Family: **Symbolic Dynamics**, exclusively.
- Source: tensor-indecomposable finite full shifts, generated internally and
  ordered by topological entropy `log(p)`.
- Grammar: identity loop at each atom and both directed nearest-neighbor
  cross edges, hence a recurrent/strongly connected finite base graph.
- Cocycle: distinct positive free generators on directed cross edges in the
  frozen realization; reverse graph edges are not assigned inverse labels.
- Weight:

  \[
  d_i(s)=p_i^{-s},\qquad
  c_{ij}^{(\alpha)}(s)=\alpha d_i(s)+(1-\alpha)d_j(s),
  \quad \alpha=\tfrac12.
  \]

- Invariant: `Tr_N tensor tau`, with `tau` the identity-coefficient group
  trace.
- Data firewall: no Riemann-zero data, target roots, fitting, or rescaling.

### Exact accomplishments

1. Every mixed base closed path carries a nonempty positive word, so
   `(Tr_N tensor tau)(L_s^r)=sum_i p_i^(-rs)` for every `r>=1`.
2. Consequently `D_tau(z)=product_i(1-z p_i^(-s))` formally; the scalar
   trace series is absolutely convergent at `z=1` on `Re(s)>1`.  Any
   operator-analytic determinant reading is restricted to a selected
   small-norm/invertible logarithm branch.
3. The chiral adjoint introduces inverse labels and breaks the clean ledger
   at `r=2` by the exact positive term `2 sum_e |c_e(t)|^2`.
4. Endpoint `alpha=0,1` objects are phase gauges; every tested interior
   alpha moves in the quadratic/chiral moments.

### Specificity verdict

**Free-group specificity is refuted.**  The positive abelian `Z` control
passes at all orders, because the proof needs neither freeness nor
noncommutativity.  The true theorem is for a cocycle into any conical or
positive monoid whose nonempty positive products exclude the identity.
Accordingly, the base ledger is powerful but nonselective and is marked
`PROVES_TOO_MUCH` without an additional source-internal label principle.

Finite relation controls fail at the first graph-admissible relation:
inverse pairs at `r=2`, the frozen `S3` assignment at `r=4`, and `C5` at
`r=10=lcm(2,5)` because the chain requires an even number of cross steps.

### Route status

```text
(A0_ANALYTIC_ARITHMETIC_ORIGIN,
 A1_PASS_ANALYTIC,
 A2_ANALYTIC_DETERMINANT,
 A3_PARTIAL_ANALYTIC_STRUCTURE,
 A4_FORMAL_HINT)

ROUTE_A_ANALYTIC_CANDIDATE
GO_BASE_TAU_LEDGER / STOP_CHIRAL_UNIFICATION
route_b_invocation_allowed: false
```

Canonical frozen evaluation:
`evaluations/route_a/SD-C10/20260813T131330Z.yaml`.  Its source and code
provenance is commit `4e094ae14a34bc98fc8b7cf4424d2edee8d5580e`; the
following metadata commit freezes the evaluation and paper manifest.
