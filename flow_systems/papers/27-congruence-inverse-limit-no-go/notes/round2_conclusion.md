# P27 Round-2 conclusion — finite levels do not repair the limit owner

Date: **2026-08-27**

## Landed result

Three hyperbolic elements of `Gamma(3)` were frozen before computation and
reduced at the eight prescribed levels `q=3,6,18,72,360,2160,15120,120960`.
For each of the 24 pairs, the order in the projective quotient was computed by
sequential multiplication and by independent group-bound factor reduction.
All 24 pairs agree exactly.  The resulting order sequences are

```text
G3-A: 1,3,3,6,6,36,72,288
G3-B: 1,1,3,12,60,360,360,2880
G3-C: 1,2,6,12,12,72,72,576.
```

The matrix entries, determinant, trace, `Gamma(3)` membership, PSL sign at the
closing exponent, bonding compatibility, divisibility from one level to the
next, geodesic length, and period scaling are explicit in the CSV.  This is
`[NUMERICALLY_CERTIFIED]` exact-integer finite computation; floating values are
deterministic displays of the analytically defined geodesic lengths.
There are 21 nontrivial adjacent-level transitions across the three elements,
all passing bonding and previous-order divisibility checks; the three level-1
rows are reported separately as base initializations.

## Owner firewall

At a finite level, the reduction order `o_q(gamma)` gives the closed-lift period
`o_q(gamma) ell(gamma)`.  It does not give one positive time shared by all
levels.  A periodic point of the inverse limit would require precisely such a
single common time, and the Stage-1 theorem proves it cannot exist.  Therefore:

```text
FINITE_LEVEL_STATISTIC_OWNER=CONGRUENCE_TOWER_PLUS_FROZEN_MATRIX
INVERSE_LIMIT_FLOW_PERIODIC_SET=EMPTY [PROVED]
FINITE_LEVEL_TO_LIMIT_ORBIT_CREDIT=FORBIDDEN
```

The observed growth is compatible with the no-go theorem and cannot
“compensate” for its A1 obstruction.  A future normalized distribution would
be owned by the tower and its chosen normalization, not by primitive orbits of
`M_infinity`.

## Route boundary

- A0 arithmetic provenance remains present, but the intrinsic rational-prime
  correspondence remains `[OPEN]`.
- The `[PROVED] PROVED_A1_OBSTRUCTION` for `M_infinity` is unchanged.
- The finite-level table adds a diagnostic, not an A1 pass and not an A2 zeta.
- The formal Route-A tuple remains `UNASSIGNED`; the required full evaluator
  input, especially a same-owner determinant convention for A2, is not frozen.
- A2--A4 are `NOT_EVALUATED`; Route B is not run; invocation is false; Gates
  A--E are not reached.

No rational-prime table, Riemann-zero table, fitted clock, or target-derived
weight was used.
