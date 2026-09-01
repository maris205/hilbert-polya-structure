# Exact-computation plan

## Claims under test

1. The central-binomial coefficients satisfy the survival convolution and
   first-descent identities through a broad exact window.
2. The discrete-arcsine rows are normalized, symmetric, and shared by the
   positive-count and maximum-time statistics in no-ties controls.
3. Atomic increments break the frozen continuous formulas and can create
   maximum ties.
4. The bulk discrete mass approaches the arcsine density under `1/n` scaling.

## Evidence design

- Generate `q_n` exactly for `0<=n<=40` and all `q_k q_{n-k}` cells for
  `0<=n<=32`.
- Enumerate every sign and permutation of `(1,3,...,3^(n-1))` for
  `1<=n<=7`.  Superincreasing magnitudes eliminate all subset-sum ties.
- Enumerate all simple-symmetric paths through `n=8` as the atomic boundary.
- Record bulk scaling receipts at `n=64,128,256,512` and
  `x=1/4,1/2,3/4`.

## Independence and hostility

The checker reimplements central-binomial arithmetic and the history
enumerator without importing the producer.  SymPy independently extracts the
univariate and bivariate generating-function coefficients.  Replay runs a
fresh producer and requires byte identity.  Every mutation repairs the payload
hash before invoking the checker, so rejection cannot rely on a stale digest.

## Evidence boundary

No finite table proves a distribution-free statement.  The proof uses maximum
factorization and the permutation-cycle lemma; computation audits algebra,
normalization, indexing, and tie conventions.
