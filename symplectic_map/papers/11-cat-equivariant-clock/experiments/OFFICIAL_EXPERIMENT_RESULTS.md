# Official Experiment Results

**Candidate:** `cat_equivariant_retention_tradeoff_v1`  
**Registered run:** `REGISTERED_RUN_0001`  
**Date:** 2026-08-15 UTC  
**Execution status:** `COMPLETED_CERTIFIED`  
**Registered audit count:** 1  
**Candidate numerical-run count:** 0

## Bound execution evidence

| Artifact | SHA-256 |
|---|---|
| source lock v2 | `331a1f9004f83c7979daf8eacddd6844072c6b5b7068293c1276985cf6aaa87b` |
| source-lock review R2 | `2f75d6934e3d61bdc941ee6689102a1cb08a959270a7cd87965579f1ec5cc622` |
| reviewed execution tree | `5ee1918a57fee56a2ca5a117c5749f614efbfd6baed96ae45480d6091a4741eb` |
| deployment review, full R1+R2 file | `3cfe1a34677ef5af06d1a8448de74f5d5dc202dc0136ccf51bfd88f3915110c5` |
| pre-execution JUnit | `4cf187fbd29f8a2b89dae2035a0971086b70108e395629ef198fcfc4869307ff` |
| authorized pre-execution audit | `429c43d1002b5e51ad60ee7614f3156081f32651972500624d05185694996479` |
| durable registered claim | `c58c9bc93d0e6af2440c163323d7dcc3c098a0c470f0f11bfb31fa98fb82c79f` |
| raw exact result | `bef8aa5d632ed11b1ca58a123bbfe967a5426e2049d862118a373e4c1dc005fe` |
| registered terminal | `e6ec2c40094a933a3b6f18a46afb36df538e84fb8afee9b63ba6ab166acbe983` |
| post-run JUnit | `a4bd081c0ac9bd8ab9efca301d01c858e5e90a43e9c2796acc0431d79df0287f` |

The registered command was invoked exactly once. It processed only the
ordered arithmetic tuple `(2,3,5,7,11,4,6,9,10)` and one separately typed
structural unit control. The structural control never entered the arithmetic
modulus namespace.

## Raw nine-row comparison table

All exponents below are exact rational values. Every factor uses the locked
Artin--Mazur inverse sign.

| q | n_q | r_q | m_q | point support | orbit support | cardinality(point) exponent | orbifold(point) exponent | cardinality(orbit) exponent | orbifold(orbit) exponent | nonidentity sectors | stack period | labelled a recovered |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| 2 | 3 | 3 | 1 | 3 | 1 | 1 | 1/3 | 3 | 1 | 0 | 1 | yes |
| 3 | 8 | 4 | 2 | 4 | 1 | 2 | 1/4 | 8 | 1 | 0 | 1 | yes |
| 5 | 20 | 10 | 2 | 10 | 1 | 2 | 1/10 | 20 | 1 | 0 | 1 | yes |
| 7 | 48 | 8 | 6 | 8 | 1 | 6 | 1/8 | 48 | 1 | 0 | 1 | yes |
| 11 | 100 | 5 | 20 | 5 | 1 | 20 | 1/5 | 100 | 1 | 0 | 1 | yes |
| 4 | 12 | 3 | 4 | 3 | 1 | 4 | 1/3 | 12 | 1 | 0 | 1 | yes |
| 6 | 24 | 12 | 2 | 12 | 1 | 2 | 1/12 | 24 | 1 | 0 | 1 | yes |
| 9 | 72 | 12 | 6 | 12 | 1 | 6 | 1/12 | 72 | 1 | 0 | 1 | yes |
| 10 | 60 | 30 | 2 | 30 | 1 | 2 | 1/30 | 60 | 1 | 0 | 1 | yes |

## Structural unit control

For the abstract effective action
`C6/C2 disjoint-union C6/C3`, the formula and explicit-coset engines agree:

- the action kernel has order 1;
- the source factors have supports 2 and 3, each with exponent 1;
- no support-6 factor exists despite the effective `C6` action;
- the coarse quotient has support 1 and exponent 2;
- the point-orbifold weights are `3/2` at support 2 and `2/3` at support 3;
- the orbit-orbifold reduction and static inertia count are both 5; and
- the labelled twist is recovered because the action is effective.

This theorem/control is not an arithmetic modulus row and is not a candidate.

## Key findings

1. **Observation:** explicit fixed-set/groupoid enumeration and the separate
   regular-torsor theorem engine agree exactly in all nine rows.  **Interpretation:**
   the point-order, orbit-order, twisted, enhanced, orbifold, and groupoid
   records implement the locked definitions rather than a single crosswired
   calculation.  **Implication:** the definition-sensitive retention hierarchy
   is certified within the frozen finite scope.

2. **Observation:** point-order Burnside support is `r_q`, whereas orbit-order
   support and every Morita quotient period are 1.  **Interpretation:** source
   order survives before quotient/orbifold compression, but quotient dynamics
   are static.  **Implication:** retaining a period and compressing to a unit
   factor are different operations.

3. **Observation:** the complete twisted table uniquely selects
   `g=a_q^(-k)`, while the enhanced carrier records `a_q`; the regular action
   kernel is trivial.  **Interpretation:** the strongest audited carriers
   recover the labelled local twist.  **Implication:** this is a positive
   retention boundary, not a blanket failure of equivariant data.

4. **Observation:** `r_2=r_4=3` and `r_6=r_9=12`, and all four composite rows
   satisfy the same hierarchy.  **Interpretation:** retained order neither
   identifies the modulus nor selects primes.  **Implication:** substituting
   `t=q^(-s)` still requires the external family label `q`.

5. **Observation:** all exact external-operation counters are zero, the
   coefficient environment varies with `q`, and no cross-`q` ring
   identification is supplied.  **Interpretation:** the calculation remains
   local and labelled.  **Implication:** it does not create a common return
   clock, an intrinsic prime selector, or Route-B authorization.

## Disposition and next step

All registered controls `K001` through `K012` are exactly true. The machine
classification is:

`EQUIVARIANT_RETENTION_COMPRESSION_TRADEOFF_CERTIFIED / A0_FAIL_MODULUS_GLOBAL_NON_SPECIFIC / ROUTE_B_NOT_OPENED`.

No new scientific experiment is suggested inside the frozen Paper-11 scope.
The required next step is read-only independent result-integrity review; only
after `RESULT_PASS` may the one-shot strict result manifest and manuscript
handoff be authorized.
