# Theorem package

## Main theorem

For fixed `theta>0`, let `Pi_n` be the Chinese-restaurant partition of `[n]`, let `K_n` be its number of blocks, and let `C_j(n)` be its number of size-`j` blocks.  Then:

- each labelled partition with block sizes `n_1,...,n_k` has probability
  `theta^k/(theta rising n) * product_i (n_i-1)!`;
- every count vector `c` with `sum j*c_j=n` has probability
  `n!/(theta rising n) * product_j (theta/j)^c_j/c_j!`;
- `K_n` is a sum of independent Bernoulli variables with success probabilities `theta/(theta+i-1)` and PGF `(theta*z rising n)/(theta rising n)`;
- `K_n/log n -> theta` almost surely and `(K_n-EK_n)/sqrt(Var K_n)` converges to standard normal;
- for each fixed `m`, `(C_1(n),...,C_m(n))` converges jointly to independent `Poisson(theta/j)` variables.

## Proof dependencies

1. Unique-predecessor induction on labelled partitions.
2. Exact labelled-partition multiplicity for a count vector.
3. History-independent conditional innovation probabilities.
4. Summable normalized variances and Kronecker's lemma.
5. Lindeberg--Feller for bounded independent summands.
6. Exact mixed falling-factorial moments and their correction limit.

## Status

Every item is proved in `paper/main.pdf`.  The JSON panels and symbolic identities are implementation receipts, not asymptotic proofs.
