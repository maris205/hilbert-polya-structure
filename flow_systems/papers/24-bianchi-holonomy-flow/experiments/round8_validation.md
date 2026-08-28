# P24 Round-8 validation report

## Material Passport

- Origin Skill: `ars-codex:academic-research-suite` plus exact experiment validation
- Origin Stage: Stage 1 research
- Verification Status: `VERIFIED / REPRODUCIBLE`
- Primary-output SHA-256: `cacf5b84d9faecdca1cdfc5e0082cbf21cf491fbfe75835d41919d4c9c5f54f3`
- Freeze SHA-256: `f60ef15527b254bef76dcf670c36c23018baf7ce7243792112795d2344240e0e`

## Universal principal-congruence theorem

Let `R` be a commutative ring with identity, let `m` be a non-zero-divisor,
and write `gamma=I+mA` in `SL_2(R)`.  Exact two-by-two determinant expansion
gives

```text
0 = m tr(A) + m^2 det(A),
tr(A) = -m det(A),
(tr(gamma)^2-4)/m^2 = m^2 det(A)^2 - 4 det(A) in R.
```

Thus Round-7 `D9` integrality is a universal level-normalized congruence
identity, not a special property of `Z[i]` or `Gamma((3))`.

The first jet `J_m(gamma)=A mod m` obeys

```text
J_m(h gamma h^-1)=J_m(gamma),
J_m(gamma^-1)=-J_m(gamma),
J_m(gamma^r)=r J_m(gamma).
```

The sign quotient is therefore a necessary invariant of unoriented
`Gamma((m))` conjugacy owners.  It is not a complete conjugacy classifier.

## Four executed A0 control families; canonical type gate remains open

All four pre-frozen control families were executed, with
5 executable subpanels over
6396 exact matrices/witnesses.  Strictly
mapping them to the evaluator list yields only
2 canonical types:
`neighboring dynamical parameters, simpler parent system`.  The mandatory Route-A
gate is therefore `INCOMPLETE_2_OF_3_CANONICAL_TYPES`, while the frozen-family execution status
is `COMPLETE_4_OF_4`.

1. Full `SL_2(Z[i])` parent: removing the level condition produces exact
   nonintegral `/9` witnesses, so the congruence hypothesis is essential.
2. Integer level 3: every frozen `Gamma_Z(3)` row satisfies the same formula.
3. Gaussian neighbor levels 2 and 4: every row satisfies its corresponding
   level-normalized formula.
4. Eisenstein level 3: every row satisfies the same `D9` formula in
   `Z[omega]`.

The exact control outcome is `REFUTED_D9_IS_NOT_GAUSSIAN_SPECIFIC` and
`STOP_SCOPED_D9_OWNER_MECHANISM`.  Passing these identities in controls is
a negative specificity result, not support for a Gaussian prime-owner map.

## First-jet collision audit

On all 11481 frozen Gaussian matrices, `D9` has
145 values.  The joint `(D9,J3 up to sign)` descriptor
has 517 values.  It separates
372 of the original
11336 collision rows
(372/11336; decimal
0.032815808045166).  The largest bucket falls from
505 to 84.

The Round-7 exact owner witness with common `D9=13` receives two different
first-jet IDs and is therefore separated.  Nevertheless,
10964 matrix-row collisions
remain and there are 0 singleton
joint buckets.  Those residual counts are not promoted to distinct-owner
claims because the word ball is not a complete conjugacy enumeration.

## Decision and Route firewall

Decision:

```text
STOP_D9_AS_GAUSSIAN_SPECIFIC_ARITHMETIC_OWNER;RETAIN_UNIVERSAL_CONGRUENCE_THEOREM_AND_FIRST_JET_REFINEMENT
```

The typed-proxy tuple remains

```text
(A0_WEAK_ARITHMETIC_RELATION, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)
overall = ROUTE_A_EXPLORATORY
FULL_BIANCHI_FLOW_ROUTE_A_TUPLE=UNASSIGNED
METRIC_BIANCHI_PREFIX_AUTHORIZED=false
ROUTE_B_INVOCATION_ALLOWED=false
```

No prime/zero target data, metric period, dynamical determinant, or operator is
used.  The universal theorem and specificity obstruction are paper-ready; an
orbit-to-Gaussian-prime-ideal map remains open.
