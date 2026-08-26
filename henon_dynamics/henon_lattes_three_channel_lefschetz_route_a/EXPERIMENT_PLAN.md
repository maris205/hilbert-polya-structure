# Experiment plan

## Claim-driven tests

1. **Symbolic channel test.** For \(m=2,\ldots,10\) and \(n=1,\ldots,12\), compute all three channel counts, multipliers, totals, Lefschetz sums, exact-period points, and primitive cycles using exact integers and fractions.
2. **Direct torsion test.** For all frozen pairs with \(2\le m\le6\) and \(m^n\le80\), materialize both rational two-tori \(E[a-1]\) and \(E[a+1]\), form their actual set intersection, quotient every point by sign, and compare all three class counts and a canonical class digest with the theorem.
3. **Wold-chain test.** For \(m=2,\ldots,8\), enumerate all 840 sign classes in the nonzero lattice box \([-20,20]^2\), extract the unique maximal \(m\)-power depth, and verify the primitive root, shift, and adjoint boundary.
4. **Independent checker.** Recompute every row without importing producer code; use a different determinant-free implementation path for the formulas and direct set arithmetic for torsion.
5. **CAS test.** Ask SymPy to prove the channel total and Lefschetz rational identity, compare log-zeta coefficients, verify Möbius inversion, and recheck every Wold factorization.
6. **Integrity tests.** Require byte-identical replay, 23 repaired-hash semantic mutation rejections, one stale-hash rejection, deterministic double PDF compilation, embedded fonts, layout checks, and a self-excluded 27-payload-file release manifest.

## Interpretation rule

The proof is the all-parameter argument in `THEOREM_PACKAGE.md`. Finite enumeration is a regression sentinel and cannot promote any Route-A gate. Any mismatch blocks release; a clean ledger supports implementation correctness only.

## Frozen limits

All arithmetic is exact. No target data, prime tables, fitted constants, floating tolerances, local factors, Euler factors, root numbers, or Route-B information enter any test.
