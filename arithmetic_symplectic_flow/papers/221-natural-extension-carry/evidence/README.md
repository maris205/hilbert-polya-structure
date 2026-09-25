# Evidence record — ANG-20260918-HIC01

**Candidate:** history completion of the exact 219 escape-carry rule.  
**Status:** T0/T2 ESTABLISHED; T1 PARTIAL; STOP — SQRT CLOCK AND k MULTIPLICITY.  
**Evidence class:** direct symbolic proof and finite branch case analysis.  
**Computation:** none; no external data, prime table, GPU run, or numerical
search was used.

## Reproducible checks

1. Read the frozen 219 rule and the frozen 221 card.
2. Verify that every branch leaves n fixed or increases it.
3. For a history, use monotonicity and the lower bound n≥2 to obtain an
   eventually constant negative-time n-tail.
4. Exclude composite constant tails by the divisor branch.
5. Classify the prime tail as the d=2 through floor(√p)+1 cycle.
6. Apply determinism to extend that cycle to all later coordinates.
7. Count one cycle for each pair (p,k), retaining every phase.
8. Unpack the fixed unit roof by endpoint gluing; check integer-crossing
   translation, completeness, and the exact primitive/repeated flow times.

The projection counterexample (2,3,0,0) is exact. It demonstrates that the
history carrier is not a surjective relabelling of the original state space.
All claims are scoped to the frozen object; no Route coordinate or peer-review
status is claimed.
