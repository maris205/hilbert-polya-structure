# Research question

For every `n >= 1`, can the parallel fair-bit refinement chain on labelled set
partitions be solved exactly from an arbitrary initial partition, including its
full time-dependent law, spectral structure, absorption distribution, and
large-`n` threshold, while keeping the Route-A arithmetic boundary explicit?

The question has five coupled parts:

1. Determine `K_n^t(pi,sigma)` without iterating the Bell-number matrix.
2. Recover the complete law and expectation of the block count from one block.
3. Determine the last-collision time `T_n` exactly and at its critical scale.
4. Prove, rather than infer, the spectral multiplicities and diagonalizability.
5. Decide whether the resulting determinant supplies any Route-A bridge.

The contract begins at `n=1`.  The unique empty partition at `n=0` could be
added by convention with `T_0=0`, but doing so requires a separate `0^0`
normalization and is deliberately outside this package.

Success means one global theorem plus independently reproducible finite
certificates.  A numerical pattern or a claim based only on triangular
diagonal entries is not sufficient.
