# Exact Experiment Results

**Candidate:** `pcf_quadratic_prime_multiplier_obstruction_v1`  
**Date:** 2026-08-13  
**Execution:** source-locked SymPy exact arithmetic, periods `1<=n<=4`  
**Overall required-run status:** `PASS`

## Result in one sentence

The all-period proof excludes every raw rational-prime multiplier of the
frozen PCF quadratic, and the independent exact audits through period four
validate the algebra without producing any rational multiplier candidate;
the rational `p=2` exponent-prime question for `n>=2` remains `OPEN`.

## Raw candidate table

Let `K=Q[u]/(u^3-2u^2+2u-2)` and let `L` denote the cycle multiplier.  The
per-point resultant was verified to be the exact `n`th power of the displayed
per-cycle polynomial.

| Exact period `n` | Formal degree | Exact degree | Cycles | Resultant degree | Per-cycle multiplier polynomial | Rational roots |
|---:|---:|---:|---:|---:|---|---|
| 1 | 2 | 2 | 2 | 2 | `L^2-2L-4u` | none |
| 2 | 2 | 2 | 1 | 2 | `L-4+4u` | none |
| 3 | 6 | 6 | 2 | 6 | `L^2+(-16+8u)L-64+64u` | none |
| 4 | 12 | 12 | 3 | 12 | `L^3+(-48+16u^2)L^2+(256+256u^2)L+4096` | none |

For every period, the derivative-of-iterate and direct chain-product
multipliers agree, lower-period gcd checks find no candidate contamination,
the point resultant groups into the expected cycle multiplicity, and the
cycle polynomial annihilates the multiplier in the exact orbit quotient.
Rational-root certification was simultaneous in the basis `1,u,u^2`; no
floating approximation or near-integer threshold was used.

## Frozen controls

| Control | Assumption status | Exact rational multipliers by period `n=1,2,3,4` | Required behavior |
|---|---|---|---|
| `z^2` | Algebraic-integer coefficients | `{0,2}`, `{4}`, `{8}`, `{16}` | Recovers the nonzero `2^n` exponent clock. |
| `z^2-2` | Algebraic-integer coefficients | `{-2,4}`, `{-4}`, `{-8,8}`, `{-16,16}` | Recovers the period-one raw-prime residue and Chebyshev boundary behavior. |
| `z^2-3/4` | Algebraic-integer coefficient assumption violated | `{-1,3}`, none, none, none | Detects the odd raw prime `3`; records and completely removes the formal-period-two collision at the fixed multiplier `-1`. |

The nonintegral control is decisive against an always-negative code path:
the same exact rational-root and primality machinery that reports no candidate
for the frozen map correctly finds the internally derived raw prime `3` when
the theorem's integrality assumption is removed.

## Key findings

1. **Observation:** all four candidate cycle polynomials have empty exact
   rational-root sets.  **Interpretation:** the finite audit is consistent
   with the derivative-content theorem and contains no low-period exceptional
   rational value.  **Implication:** the implementation supplies a concrete
   certificate, but the all-period conclusion continues to rest on the proof,
   not on a cutoff.  **Next step:** no higher-period sampling is needed for
   the raw-prime question.

2. **Observation:** every control prediction is recovered, including `3` for
   `z^2-3/4` and `2^n` for `z^2`.  **Interpretation:** rational-root detection,
   internal deterministic primality classification, and formal/exact-period
   separation are sensitive to both positive and negative outcomes.
   **Implication:** the candidate's null rational-root list is not generated
   by a pipeline that always says “none.”  **Next step:** retain these controls
   in every manuscript-level reproducibility package.

3. **Observation:** the independently computed `f_u(x)=1-ux^2` and
   `g(z)=z^2-u` pipelines agree at every period after exact monic
   normalization.  **Interpretation:** multiplier invariance under
   `z=-ux` is implemented correctly rather than assumed numerically.
   **Implication:** the obstruction transfers exactly to the inherited map.
   **Next step:** none for this coordinate check.

4. **Observation:** the cotangent formula has zero one-form pullback and
   determinant residuals and returns `(lambda,lambda^{-1})`, while the
   denominator vanishes at `q=0`, the branch images overlap, and the regular
   domain is unbounded.  **Interpretation:** this is an exact branchwise
   symplectic bridge only.  **Implication:** no global, compact, or invertible
   symplectic-lift claim is available.  **Next step:** any global carrier must
   be a separately designed candidate.

5. **Observation:** divisibility rules out odd exponent-prime bases but is
   compatible with `|lambda|=2^n`.  **Interpretation:** empty low-period
   rational-root lists do not settle an all-period existence question.
   **Implication:** the status for rational `p=2`, `n>=2`, is and remains
   `OPEN`.  **Next step:** pursue it only through a separate all-period
   argument, never by extending the finite cutoff post hoc.

## Statistical scope

There are no random seeds, fitted parameters, repeated-sample estimates,
confidence intervals, or hypothesis tests.  All reported outcomes are exact
polynomial identities or categorical proof-boundary checks.  Wall time and
peak memory are engineering diagnostics, not scientific evidence.

## Execution diagnostics

- Python 3.12.3; SymPy 1.14.0; pytest 9.0.3.
- Required exact workflow: approximately 16.06 seconds of measured block time.
- Process peak resident memory: 771,460 KiB (about 753 MiB), below the frozen
  4 GiB ceiling.
- Test suite: 37 passed, 0 failed, 0 errors, 0 skipped.
- GPU: not used.
- External data: none.
- External prime tables and Riemann-zero data: not accessed.
- Conditional high-period real-orbit ledger: disabled and not executed.

## Scientific classification

```text
RAW_RATIONAL_PRIME: ABSENT_BY_THEOREM
ODD_RATIONAL_EXPONENT_PRIME: ABSENT_BY_THEOREM
P2_EXPONENT_PRIME_PERIOD_1: ABSENT
P2_EXPONENT_PRIME_PERIOD_N_GE_2: OPEN
COMPLEX_MODULUS_ONLY: OUTSIDE_THEOREM
COTANGENT_BRIDGE: BRANCHWISE_EXACT_SYMPLECTIC_ONLY
```
