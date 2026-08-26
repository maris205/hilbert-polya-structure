# Paper 21 methodology blueprint

Date: **2026-08-24**
Design: **quantitative algebraic number theory with exact finite-field controls**

## Frozen inputs

- fixed `p,r,m` with primes `p != r` and `m>=1`;
- Paper 15's odd-`r` compositum and separate quadratic branch;
- one selected Frobenius conjugacy class for least-witness bounds and the
  full disjoint union of classes giving both exact valuations;
- a declared unconditional or GRH-conditional effective Chebotarev theorem.

## Method

1. Reconstruct the two finite extensions and prove their intersection and
   Galois properties on the frozen parameters.
2. Import the Phase-2 verified degree, the selected-class density, the total
   exact-condition density, and the generic discriminant bound; compute the
   relative different and every local Artin conductor for `E/Q(zeta_r)` at
   `p` and `r`.
3. Verify that every selected Frobenius element gives exactly, not merely at
   least, the two requested `r`-adic valuations.
4. Apply Thorner--Zaman's relative-conductor theorem and compare it explicitly
   against the verified Kadiri--Wong unconditional and Bach--Sorenson
   ERH/GRH black-box bounds.
5. State the GRH-dependent improvement separately, with its hypothesis in the
   theorem title and conclusion.
6. Compare observed first witnesses with the proved bound without fitting the
   bound to the data.

## Controls

- odd `r` and `r=2` handled separately;
- intersection and ramification checks for small exact fields;
- excluded cases `ell in {p,r}` and ramified primes;
- brute-force verification of both valuations for pre-registered small
  triples `(p,r,m)`;
- conjugacy-class versus single-element check over `Q`;
- a deliberately weakened Frobenius condition showing why exactness can fail.

## Failure modes

- a theorem for a single automorphism is used where only a conjugacy class is
  available;
- discriminant growth omits dependence on `p,r,m`;
- a density theorem is mislabeled as a least-prime bound;
- conditional and unconditional bounds are blended;
- exact order is replaced by divisibility of order;
- generic effective Chebotarev is cited without closing the simultaneous
  valuation translation.

## Validation

- independent field/discriminant derivation;
- exact CAS checks on small fields, retained as controls rather than proof;
- primary-source verification of every hypothesis and constant convention;
- independent proof and citation review;
- numerical witness manifest with exact integer arithmetic.

## Expected output and effort

Phase-2 source/field audit is complete.  After a separate user checkpoint,
the next bounded effort is the Phase-3 local-conductor kill test; absent a
nonvacuous improvement, downgrade the project to a short quantitative note.
