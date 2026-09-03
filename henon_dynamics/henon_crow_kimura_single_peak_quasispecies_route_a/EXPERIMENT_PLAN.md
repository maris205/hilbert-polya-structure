# HCS-C336 exact-evidence plan

## Claim under test

Audit the normalization and finite-dimensional consequences of the analytic
theorem without using finite computation as proof for arbitrary genome length.

## Exact fixtures

- Genome lengths `1<=L<=10`.
- Three positive rational `(U,s)` pairs.
- Walsh/Hamming poles `d_k=-2Uk/L` and weights
  `w_k=binom(L,k)/2^L`.
- Full hypercube matrices for the small direct-comparison range.
- Separate exact receipts for `s=0`, `U=0` and `L=1`.

## Required checks

1. Binomial retained multiplicities sum with `L+1` to `2^L`.
2. The rational secular polynomial equals the matrix-determinant-lemma
   expression and has the expected trace coefficient.
3. Direct small hypercube characteristic polynomials equal the full predicted
   factorization.
4. Exact root counts give one root above zero and one per mutation gap.
5. Walsh difference vectors realize every retained eigenvalue.
6. The quotient derivative equals the nonlinear vector field.
7. Boundary formulas and every Route-A scope flag remain literal.

The producer and checker are separate implementations.  The checker imports
no producer module.  A third SymPy lane checks characteristic polynomials,
Sturm counts and boundary identities.  Replay uses isolated output files and
demands byte identity.  Mutation tests repair semantic hashes after hostile
changes, so passing cannot be achieved by stale-hash rejection alone.
