# C161 verification plan

1. Derive `(A_n,B_n,C_n)` independently by symbolic summation.
2. Apply the gcd obstruction, reduced odd Gauss formula, and constant branch.
3. Exhaust all odd `q<=31`, all `a,b mod q`, and `1<=n<=2q`.
4. Exhaust the prime discriminant zero law on the same range.
5. Run an independent implementation, SymPy checks, deterministic replay, and
   repaired-hash plus stale-hash mutations.
6. Compile three manuscript rounds twice under a fixed epoch and close a
   self-excluded content-addressed manifest.

The finite sweeps are regression sentinels.  The theorem rests on the finite
Gauss proof in `THEOREM_PACKAGE.md`.
