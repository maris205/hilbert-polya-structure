# Paper plan — P114

## Problem anchor

Treat parallel leaf peeling as one finite self-map on the union of all rooted
forests carried by subsets of `[n]`, rather than only as an algorithm on one
tree.  Close global basins, temporal shells, local fibres, and periodic data.

## Claim matrix

| Claim | Route in manuscript | Independent control |
|---|---|---|
| endpoint is the original root set; entry time is height, with empty height zero | subtree-height induction plus empty case | literal parent-map orbits |
| specified `r`-root basin is the Cayley sum | all-minors matrix-tree determinant | exhaustive endpoint ledger |
| all depth CDFs use `A_0=1`, `A_h=exp(xA_(h-1))` | labelled species | exact rational truncated series |
| local fibre depends only on `(m,s)` | inclusion–exclusion on newly attached leaves | every literal target fibre through `n=6` |
| fixed count `2^n`, zeta; for `n>=2`, max depth `n-1` and deepest `n!` | strict vertex loss and Hamilton-path classification, with `n=0,1` split | complete functional graphs |

## Two proof routes

1. Parent pointers, subtree heights, strict vertex loss, and direct preimage
   surgery.
2. Matrix-tree determinants, labelled exponential generating functions, and
   exact inclusion–exclusion.

## Scope gate

The main internal collision is P105's cycle-minimum permutation pruning.
P114 uses rooted forests, simultaneous exposed leaves, height, Cayley
determinants, and target-leaf fibres; no permutation-cycle recurrence is
reused.  Parallel `RAKE`, classical tree/all-minors counts, labelled-height
recurrences, height-driven pruning/leaf stripping, inclusion–exclusion,
absorption/zeta conversion, and the elementary Hamilton-path extremal step
are not claimed.  The bounded owner audit cannot establish priority for the
endpoint-indexed assembly or `(m,s)` fibre calculation.
