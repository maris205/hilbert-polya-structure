# Experiment plan

1. Recompute `a_5`, `a_7`, and `a_11` from the curve.
2. Build the first-logarithmic-coefficient matrix with columns `(1,a_p,p)`.
3. Solve over exact rational arithmetic and require determinant -24
   (absolute value 24).
4. Exhaust all integral classes in `[-12,12]^3`.
5. Check the unique solution on holdout primes 13 through 31.
6. Mutate the sign of `a_7` and ensure the frozen determinant/solution lock
   detects the change.

The linear theorem, not the finite box, proves uniqueness over all rational
and integral exponents.
