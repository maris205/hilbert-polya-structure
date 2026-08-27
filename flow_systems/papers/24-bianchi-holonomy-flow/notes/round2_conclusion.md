# P24 Round-2 conclusion — finite level-(3) word ball

Date: **2026-08-27**

## Landed result

`[NUMERICALLY_CERTIFIED]` for the explicitly frozen elementary-generator word
ball: 22,409 freely reduced words through length 5 collapse to 11,481 exact
matrices in `SL_2(Z[i])`; all have determinant one and are congruent to `I`
modulo `(3)`.  The ledger contains 10,976 loxodromic, 504 parabolic, and one
identity row.  It detects 32 exact power repetitions inside the enumerated set
and leaves 10,944 rows primitive only relative to that finite search boundary.

Complex length is reconstructed from the projective trace with maximum residual
`1.1375e-13`.  Orientation pairs, symbolic cyclic classes, word-to-matrix
collisions, trace collisions, parabolic/cusp risk, and completeness limits are
retained row by row.

## Executed control

A deterministic target-free permutation shuffled holonomy angles over 10,944
primitive-within-ball candidates while retaining every length and repetition
field.  The frozen phase/length score was `0.0031738184` before and
`0.0224706482` after shuffling.  `[NUMERICAL_OBSERVATION]`: the chosen statistic
does not distinguish the observed angles from this generic compiler control.
The control verdict remains `[OPEN]`, because the sample is not a full orbit
ledger and the matched non-arithmetic Kleinian comparison is not yet executed.

## Route boundary

```text
PROPOSAL_STAGE=1
ROUTE_A_SCOPE=A0-A1
A0_ORBIT_IDEAL_MAP=OPEN
A1_FINITE_WORDBALL_EVIDENCE=NUMERICALLY_CERTIFIED
A1_FULL_PRIMITIVE_CONJUGACY_LEDGER=OPEN
HOLONOMY_CONTROL_EVIDENCE=NUMERICAL_OBSERVATION
HOLONOMY_CONTROL_VERDICT=OPEN
FORMAL_A0_A4_TUPLE=UNASSIGNED
ROUTE_B_EVALUATION=NOT_RUN
ROUTE_B_INVOCATION_ALLOWED=false
GATES_A_E=NOT_REACHED
```

The elementary matrices are not claimed to generate all of `Gamma((3))`; the
word ball is not a conjugacy fundamental domain; cusp/scattering terms are not
computed; and no row is assigned a Gaussian or rational prime.  The smallest
next gate is a generator/conjugacy completeness theorem or an independently
certified full primitive-class enumerator, followed by the matched
non-arithmetic Kleinian control.
