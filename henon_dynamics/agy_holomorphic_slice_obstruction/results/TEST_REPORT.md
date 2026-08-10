# HCS-C26 regression and mutation report

**Date:** 2026-08-10
**Command:** `./code/run_c26.sh`
**Outcome:** `PASS`

Producer summary:

```json
{"states":7,"edges":14,"base_state":4,"gamma_length":128,"S_x0":"15076979616018/8999921","complex_cone_delta":"14783/1642663","birkhoff_theta":"12206150825/12121793906","birkhoff_q_bound":"0.00173375049763643206391704653769","periodic_trace_examples":3,"two_return_elementary_length":391,"three_return_elementary_length":650,"sentinel_first_returns":13528,"sentinel_collisions":0}
```

The independent checker passes fourteen of fourteen registered checks.

Regression and mutation suite:

```text
Ran 21 tests
OK
```

The suite rejects or exposes:

- right multiplication in place of later-on-the-left chronology;
- confusing the homological matrix `B` with the length matrix `R=B^T`;
- Jacobian exponents three or five in place of four;
- using `B` instead of the positive prefix `P=B^T`, or allowing a zero
  prefix entry;
- complex dimension four in place of projective dimension three;
- a branchwise fitted logarithm or numerical samples as a common-domain
  proof;
- reversing the genuine two-return matrix product;
- confusing the cyclically invariant two-return characteristic polynomial
  with a spectral chronology test;
- erasing the characteristic-polynomial difference under the three-return
  noncyclic reversal;
- leaving `lambda^(-(s+4))` uncancelled instead of the trace atom
  `lambda^(-(s+1))/chi'(lambda)`;
- a mutated section word or the wrong base state;
- replacement of the exact `x0` by the barycenter;
- row-sum/column-sum confusion in `S(x0)`;
- omission or downgrading of the bounded constant-embedding assumption;
- omission or silent certification of bounded point evaluation;
- promotion of the length-20 replay to an all-length proof or branch
  completeness statement;
- use of separate atom squares when equal projected matrices with opposite
  central signs would cancel;
- ignoring projected-matrix collisions;
- averaging central signs or chronological branch matrices;
- importing the producer from the independent checker.

The collision mutation is explicit: two equal projected atoms with
coefficients `+a` and `-a` have signed aggregate zero even though the naive
sum of their separate squared magnitudes is positive.  This test is why the
certificate retains the external C25 injectivity hypothesis instead of
inferring it from a finite cutoff.
