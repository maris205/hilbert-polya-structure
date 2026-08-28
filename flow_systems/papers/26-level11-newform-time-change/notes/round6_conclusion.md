# P26 Round-6 conclusion

## Paper-level advance

Round 6 removes the orientation-choice defect at first order.  The canonical
inverse-closed product is even in the time-change parameter: its first
variation is exactly zero, while its second variation is

```text
2s^2 I(gamma)^2 sum_(r>=1) r exp(-sr ell(gamma))
```

for the reciprocal Ruelle convention, with the frozen stability denominator
inserted for the Selberg-type convention.  The observable is intrinsic to the
inverse pair, nonnegative for real `s>0`, and requires no positive-word
half-ledger.

The corresponding Hecke question has a sharp answer.  For
`Q_d=sum_(O:d_O=d) I(delta_O)^2`, any predeclared `p`-only scalar recurrence
for all `s` requires and is implied by

```text
Q_1=lambda_p I(M)^2,
Q_d=0 for d>1.
```

The Round-4 linear period sum does not imply these quadratic conditions.

## Finite result

- 552 inverse-pair/repetition rows validate the `r^2/r=r` second-derivative
  law.
- 110 quadratic degree-moment rows and 165 finite weighted rows audit
  `lambda_p=a_p` and `lambda_p=a_p^2`.
- Both primary scalars fail 51/55 group moment checks and 153/165 rows for
  each frozen kernel.
- Four `p=5` groups pass only as finite numerical observations.
- The secondary control `lambda_p=a_p^2-p` fails 55/55 groups and 165/165
  rows for each kernel.
- Twelve tests and two byte-identical builds pass; artifact-tree SHA-256 is
  `fc553aa18bc4fb54d70ea8f4c0bdbc41efc3c0905b3f2942c49e1f6f8c62f864`.

## Verdict

```text
CANONICAL_INVERSE_PAIR_FIRST_VARIATION=PROVED_EXACT_ZERO
CANONICAL_INVERSE_PAIR_SECOND_VARIATION=PROVED_ORIENTATION_EVEN
QUADRATIC_HECKE_DEGREE_MOMENT_CRITERION=PROVED
LINEAR_HECKE_PERIOD_RELATION_IMPLIES_QUADRATIC_RECURRENCE=false
A_P_SQUARED_MINUS_P_ROLE=SECONDARY_NEGATIVE_CONTROL_ONLY
FINITE_NUMERICAL_SURVIVORS=4/55
```

This is a local finite-product theorem/audit at ARS Stage 1 and Proposal Route
A A0--A1.  It is not formal A2: the primitive class list is incomplete, the
global product and continuation are open, and no root count, target-zero
comparison, validation/test split, or cutoff/precision A2 campaign was run.
The conservative formal evaluation is
`(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)` with overall
status `ROUTE_A_EXPLORATORY`; it records the obstruction without promoting the
candidate.
