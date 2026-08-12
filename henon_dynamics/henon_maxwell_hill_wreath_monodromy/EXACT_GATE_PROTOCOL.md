# Exact gate protocol

## Frozen input

The C33 certificate and four supporting source artifacts are locked by
SHA-256. The imported object is exactly \(P_9\), the symmetric two-branch
Hill product \(\beta=N_H\), its rational norm, and the theorem
\(\operatorname{Gal}(P_9)=S_9\).

## Nine checker gates

1. `G0_SCHEMA_HASH_PASSPORT`: exact top-level schema, canonical payload hash,
   strict passport, and no unknown payload keys.
2. `G1_SOURCE_AND_C33_OBJECT`: all source hashes and imported formulas.
3. `G2_NORM_POLYNOMIAL_AND_IRREDUCIBILITY`: exact resultant polynomial and
   independent Rabin test modulo \(7\).
4. `G3_RATIONAL_SQUARECLASSES`: discriminant, norm, factorizations, and the
   sign-field comparison.
5. `G4_LOCAL_NEWTON_ODD_VALUATION`: translated coefficient valuations, unit
   residues, residual polynomial, factor degrees, gcd, and parity support.
6. `G5_PERMUTATION_RELATION_MODULE`: complete \(512\)-vector orbit-span rank
   census and the four invariant-submodule possibilities.
7. `G6_RELATION_ELIMINATION`: pair-orbit annihilator and exclusion of the
   all-ones relation.
8. `G7_FULL_WREATH_GROUP`: rank, kernel, quotient, embedding, group order, and
   equality with \(C_2\wr S_9\).
9. `G8_ROUTE_A_DECISIONS_SCOPE`: conservative Route-A tuple and all
   non-claims.

All schema comparisons are recursive and type-strict. Expected integers do
not accept booleans or floats. A semantic rejection is `FAIL`; an unexpected
checker exception is `ERROR` and also exits nonzero.

## Chronology and scope

The chronological Hénon and Hill formulas are inherited from C33 without
change. Each \(\beta_i\) is a product of two branch Hill determinants; the
certificate does not replace this nine-object ledger with eighteen
independent branch classes. No determinant or all-period claim is present.
