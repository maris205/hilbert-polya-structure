<!-- HENON_AUDIT_META_V1
{
  "artifact": "experiment_results",
  "candidate_audit_sha256": "07323e668ef4da5134fb74328bbb0b278fb2b98f789945725e00f963ddab238d",
  "candidate_executed": true,
  "candidate_id": "integral_area_henon_multiplier_support_v1",
  "must_run_failed": 0,
  "official_full_run_status": "PASS",
  "run_summary_sha256": "4ad647f700080cfc51a61663b2dbef422f9454a7db3ed604a7ec58dea1469348",
  "schema_version": 1
}
HENON_AUDIT_META_V1_END -->

# Exact Experiment Results

## Outcome

The frozen global polynomial symplectic Hénon candidate passes every exact
implementation and control check, but fails Route-A arithmetic relevance for
the proposed clock.  The all-period algebraic-unit theorem gives

```text
RAW_RATIONAL_PRIME_MODULUS: ABSENT_BY_THEOREM
A0: A0_FAIL_EXACT_RATIONAL_PRIME_MODULUS_ABSENT_BY_THEOREM
ROUTE: ROUTE_A_REJECTED_FOR_EXACT_RATIONAL_PRIME_MODULUS_CLOCK
```

The candidate remains a valid global polynomial symplectic automorphism.  Its
arithmetic failure is more specific: at the integral parameter, no periodic
return multiplier can have any exact rational modulus other than one.

## Raw exact candidate table

All coefficients below lie in
`Q[u]/(u^3-2u^2+2u-2)`.  Lower-period branches were removed exactly before a
formal solution was called exact-period.

| Exact period | Exact points | Exact cycles | Trace polynomial | Multiplier polynomial | Rational multiplier roots | Exact rational moduli in the real embedding |
|---:|---:|---:|---|---|---|---|
| 1 | 2 | 2 | `T^2-4T-4u` | `L^4-4L^3+(2-4u)L^2-4L+1` | none | `{1}` on the elliptic fixed cycle; the other cycle has irrational algebraic-unit moduli |
| 2 | 2 | 1 | `T+4u-14` | `L^2+(4u-14)L+1` | none | none; both moduli are irrational algebraic units |
| 3 | 6 | 2 | `T^2+(16u-20)T+96u^2-164u+8` | `L^4+(16u-20)L^3+(96u^2-164u+10)L^2+(16u-20)L+1` | none | none; all four moduli are irrational algebraic units |

Every displayed multiplier polynomial is monic, reciprocal, and has constant
term one.  Norming from the cubic parameter algebra to `Q` produced only
monic irreducible factors with constant term `+1` or `-1`, supplying the
finite algebraic-unit certificates.  Direct derivative products gave
determinant one, and cyclic starting-point shifts gave the same trace.

## Controls

| Control | Exact observation | Interpretation |
|---|---|---|
| `a=-15/16`, fixed point `(5/4,5/4)` | Characteristic polynomial `(L-2)(L-1/2)`; generic modulus classifier returned `1/2,2` | Prime 2 reappears exactly when coefficient denominators predeclare bad support `{2}`. |
| Integral `a=0`, periods 1--3 | Derived rational-modulus set `{1}`; no rational multiplier roots | Negative control agrees with the integral all-period theorem and exercises the same modulus pipeline. |
| `J_(a,delta)` with `delta=2` | Determinant `2`; unit conclusion refused for an empty declared support | Determinant one, or a tracked S-unit determinant, is essential. |
| Cat-map matrix | Irrational algebraic-unit spectral radius `(3+sqrt(5))/2>1` | The theorem does not prohibit unstable irrational moduli. |
| Floating and near-rational inputs | Rejected as inexact | Numerical proximity cannot create an exact rational-modulus label. |

## Key findings

1. **All-period theorem.** Projective homogenization first makes every finite
   complex periodic orbit algebraic.  The cyclic non-archimedean maximum
   argument then makes its coordinates integral; integral determinant-one
   monodromy makes both eigenvalues algebraic units.  In a
   conjugation-stable Galois closure,
   `|lambda|^2=lambda*conjugate(lambda)` is a unit.  Therefore exact
   `|lambda| in Q_{>0}` forces `|lambda|=1` for the frozen integral map.
2. **Finite implementation audit.** The complete exact cutoff through period
   three found five cycles and rational-modulus set `{1}`, with no rational
   multiplier root.  This checks recurrence signs, period separation,
   derivative order, resultants, conjugation classification, and reporting;
   it is not the source of the all-period claim.
3. **Sharp support boundary.** The denominator control realizes exact moduli
   `2` and `1/2`.  Hence area preservation alone does not exclude rational
   prime moduli; good reduction limits them to the predeclared finite bad
   support.
4. **Route decision.** Geometry passes, but A0 fails for this exact clock.
   A1 as a full primitive-orbit program is `STOP_SCOPED_AFTER_A0`; A2--A4 are
   likewise stopped, and Route B is not opened.

## Proof/experiment boundary

The following is proved for every period: periodic-coordinate integrality,
special-linear integral monodromy, algebraic-unit multipliers, and exclusion
of exact rational modulus other than one.  The finite audit proves only facts
about the explicitly eliminated periods 1--3 and validates the software.  It
does not classify irrational moduli, approximate moduli, singular values,
Lyapunov exponents, or whether rational eigenvalues `+1` or `-1` occur at
higher periods.

## Next step

No zeta, Fredholm, zero-target, or quantization stage is justified for this
candidate.  A separate source-locked candidate would have to explain, before
target access, how it escapes finite good-reduction support--for example via
an intrinsically infinite bad-place mechanism or a genuinely nonalgebraic
clock.  Changing this candidate's parameter or enlarging its bad set after
inspection is forbidden.

