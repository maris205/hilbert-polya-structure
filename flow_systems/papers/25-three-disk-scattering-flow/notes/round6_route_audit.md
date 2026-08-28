# P25 Round-6 typed Route-A audit

Date: **2026-08-28**

The exact Route record is
[`../../../evaluations/route_a/THREE-DISK-NO-REPEAT-MASLOV-SYMBOLIC/2026-08-28-stage1.yaml`](../../../evaluations/route_a/THREE-DISK-NO-REPEAT-MASLOV-SYMBOLIC/2026-08-28-stage1.yaml).

## Tuple

```text
candidate = THREE-DISK-NO-REPEAT-MASLOV-SYMBOLIC

(A0_FAIL,
 A1_PASS_ANALYTIC,
 A2_ANALYTIC_DETERMINANT,
 A3_FAIL,
 A4_FAIL)

overall = ROUTE_A_REJECTED
route_b_invocation_allowed = false
```

`A0_FAIL` is not inferred from the determinant: the control has no arithmetic
source by construction.  `A1_PASS_ANALYTIC` belongs to the exact primitive and
repetition ledger of the unit-roof symbolic suspension.  `A2_ANALYTIC_DETERMINANT`
belongs to its `3 x 3` transfer matrix and exact Euler product.  These credits
cannot move to the physical Euclidean-flight-length flow, whose formal tuple
remains `UNASSIGNED`.

The A2 result is nevertheless useful infrastructure.  It tests, without
floating-point or target data, that orientation, primitivity, repetition,
phase, trace exponential, Euler product, and determinant convention are wired
consistently.  Its rejection demonstrates the Route-A rule that exact A1--A2
algebra cannot compensate for failed A0 arithmetic provenance.

No Route-B evaluation is run or authorized, and manuscript drafting remains
unauthorized.
