# P24 Round-5 conclusion — common marked-word rule, residual marking confound

## Paper-level result

Round 5 executes the comparison that Round 4 could not: both the level-`(3)`
Bianchi candidate and the finite-volume non-arithmetic `5_2=m015` control are
enumerated by the same freely reduced, cyclically reduced, dihedrally
canonicalized marked-word rule through length 5.  The phase-sensitive complex
moment and its 64-permutation null were frozen before result execution under
SHA-256
`210cff78b8af54847baae1c7ef21572dd697d70004f50723f6b1bac4e19a85b7`.

The exact symbolic census produces 2,074 candidate owners from 19,624 linear
words and 51 control owners from 372 linear words.  After exact symbolic
primitivity and loxodromic filtering, the phase comparison uses 1,932 and 39
rows respectively.  Its observed standardized values are `-1.74684253916` and
`-0.811352306226`, for absolute contrast `0.935490232934`.

## Scientific interpretation

The result is a concrete methods advance, not an arithmetic verdict.  The same
enumeration **algorithm** now applies to both systems, so the former word-ball
versus metric-cutoff error is removed.  However, the candidate has four
positive generators and the control presentation has two.  Alphabet size,
presentation, sample cardinality, and marking dependence therefore remain
confounded.  Neither ledger is called a complete metric length spectrum or a
full group-conjugacy/primitive census.

Exact and numerical evidence are kept separate:

- marked-word canonicalization/primitivity and candidate `Z[i]` matrix checks
  are exact;
- the control geometry/non-arithmeticity is inherited from the Round-4 source
  theorem chain;
- control holonomies and the cross-system phase values are non-interval
  numerical observations;
- no prime, prime-ideal, or zero target data are consumed.

## Route boundary and next result

```text
ARS_STAGE=1_RESEARCH_IN_PROGRESS
PROPOSAL_STAGE=1
ROUTE_A_SCOPE=A0-A1_ONLY
FORMAL_ROUTE_A_TUPLE=UNASSIGNED
A2_A4_EVALUATION=NOT_EVALUATED
ARITHMETIC_KILL_VERDICT=BLOCKED_BY_MARKING_AND_PRESENTATION_CONFOUND
ROUTE_B_EVALUATION=NOT_RUN
ROUTE_B_INVOCATION_ALLOWED=false
GATES_A_E=NOT_REACHED
```

The next smallest paper-producing artifact is a preregistered same-marked-
generator-count Nielsen sensitivity panel.  It should ask whether the descriptive
phase contrast is stable across target-free changes of marking before any
metric-spectrum computation or arithmetic interpretation is attempted.
