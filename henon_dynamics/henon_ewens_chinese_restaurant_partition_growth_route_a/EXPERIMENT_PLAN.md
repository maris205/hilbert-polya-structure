# Claim-driven verification plan

## Claims

1. The insertion process is exchangeable with the exact Ewens EPPF.
2. Every occupancy vector has the stated exact probability.
3. The total block count is a sum of independent Bernoulli innovations with an exact rising-factorial PGF.
4. `K_n/log n -> theta` almost surely and the variance-normalized block count satisfies a CLT.
5. For fixed `m`, `(C_1,...,C_m)` converges jointly to independent Poisson variables with means `theta/j`.

## Proof lanes

- labelled-partition induction for the EPPF;
- exact combinatorial multiplicity for occupancy vectors;
- conditional-probability factorization for independent innovations;
- Kolmogorov convergence plus Kronecker's lemma for the strong law;
- bounded Lindeberg array for the CLT;
- mixed falling-factorial moments for the Poisson limit.

## Computational receipts

- 914 occupancy vectors through `n=16`;
- 528 unsigned-Stirling rows and 2,640 exact block-count probabilities through `n=32`;
- 320 Bernoulli rows through customer 64;
- 740 exact mixed-factorial moments;
- 80 normalization and 16 boundary rows;
- independent checker, symbolic lane, byte replay, hostile mutations, and deterministic PDF release gate.

Finite tables do not prove the asymptotic claims.
