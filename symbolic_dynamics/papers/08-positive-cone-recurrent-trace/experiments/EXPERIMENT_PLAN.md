# SD-C10 Frozen Experiment Plan

## Source lock

The only promoted family is Symbolic Dynamics.  On the entropy-ordered
tensor-atom prefix, use the recurrent bidirectional nearest-neighbor graph
with identity-labelled loops and a positive cocycle on every directed cross
edge.  Distinct positive free generators are the frozen universal
realization; `alpha=1/2` is fixed before computation.  The invariant is
`Tr_N tensor tau`, where `tau` extracts the group identity coefficient.

No Riemann-zero list, target-root comparison, fitted scale, fitted offset,
or post-hoc label choice is allowed.

## Exact tests

1. Enumerate the three-atom base trace through `r=10`, with opaque loop and
   cross-edge variables, and require every mixed closed path to be killed by
   `tau`.
2. Verify the formal/local trace-log product
   `D_tau(z)=product_i(1-z p_i^(-s))`.
3. Repeat the word ledger at `N=2,3,4` through `r=8`.
4. Form `B=[[0,L],[L*,0]]` and locate the first adjoint backtracking term
   through `r=6`.
5. Audit `alpha=0,1/8,1/4,1/2,3/4,7/8,1` on `0<=t<=40`; endpoints must be
   phase gauges and interior points may move.
6. Audit atom cutoffs `N=2,3,4,8,16,32` and report motion only as a finite
   numerical observation.

## Adversarial controls

- positive abelian `Z` labels (decisive specificity control);
- inverse-paired free labels;
- finite `S3` and `C5` labels;
- 32 frozen random positive-label assignments;
- shuffled atoms, composites, and matched-count random integers;
- finite regular `S3` representation;
- compressed free-group word balls.

The positive-abelian pass preregisters the conclusion that free-group
specificity is refuted.  Any base proof that uses only exclusion of the
identity from nonempty positive products must be reported as a general
conical/positive-monoid cocycle theorem and as `PROVES_TOO_MUCH` for RH
specificity.  Word-ball quantities are proxies only; no global FK or Brown
claim is permitted.
