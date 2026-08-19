# C67 experiment plan

1. Rebind C64 evidence and C66 evidence/manifest by exact bytes.
2. Reconstruct the fixed 16-by-16 mark matrix and verify its determinant.
3. Compute M^-1 and M^(-T) over the rationals without floating point.
4. Convert each column and row denominator set to its minimal coordinate order.
5. Check both identity products, global denominator 144, and 43 nonzero entries.
6. Recompute the profiles with SymPy, replay in a clean process, and reject
   hostile mutations.
7. Compile and audit the scoped manuscript.

Kill gates: any source drift, failed identity, profile mismatch, denominator
change, unsupported canonical-Smith claim, or scope-firewall violation.
