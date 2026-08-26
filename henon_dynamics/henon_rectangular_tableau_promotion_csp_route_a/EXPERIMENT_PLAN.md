# C187 exact-validation plan

## Claim matrix

| Claim | Infinite justification | Executable regression | Failure trigger |
|---|---|---|---|
| `j^N=id` and not necessarily order `N` | Rhoades/Haiman attribution | direct cycle orders on selected rectangles | any cycle length not dividing `N`, or `2x2` reported as order four |
| CSP fixed counts | Rhoades Theorem 1.3, unshifted q-hook | exact cyclotomic remainder and direct promotion enumeration | nonconstant primitive-root remainder or fixed-count mismatch |
| exact periods/cycles | divisor Möbius inversion | population, integrality and direct-cycle checks | negative/nonintegral cycle count or missing population |
| zeta/determinant | finite cycle-block proof | exact factor ledgers and degree totals | reciprocal/sign or exponent mismatch |
| Koopman spectrum | roots of cyclic permutation blocks | all 441 multiplicity rows | multiplicities fail to sum to tableau count |
| evacuation reversal | classical `e j e=j^-1` | direct test on 37,401 tableaux | involution or conjugacy failure |
| Route-A stop | source and scope audit | exact-map checker and semantic mutations | arithmetic/target/Route-B flag changes |

## Regression domain

- Formula ledger: all 36 ordered pairs `1<=a,b<=6`.
- Every iterate: 441 rows, one for each `0<=d<ab`.
- Exact periods: 162 divisor rows.
- Spectral multiplicities: 441 root-exponent rows.
- Direct enumeration: every declared rectangle with `ab<=16` and at most
  50,000 tableaux, totaling 26 rectangles and 37,401 tableaux.

The finite domain is a deterministic regression design, not a sampling proof
of the all-rectangle theorem.

## Independent paths

1. The producer uses a standard-library cyclotomic-factor construction.
2. The checker reconstructs q-hook polynomials by direct polynomial division,
   independently enumerates small tableaux, and implements promotion,
   demotion and rectangular evacuation.
3. The SymPy path reconstructs the cyclotomic factorization and every root
   remainder without importing producer functions.
4. Replay requires byte equality.
5. Repaired-hash mutations attack semantic fields; a stale-hash mutation tests
   the canonical payload digest.

## Release gates

- all exact programs pass;
- three content-distinct PDFs exist and round 2 equals the final PDF;
- two fresh fixed-epoch builds are byte identical;
- fonts are embedded; log and rendered-page inspections are clean;
- the self-excluded manifest contains exactly 27 payload files, giving a
  28-file package after the manifest is included.
