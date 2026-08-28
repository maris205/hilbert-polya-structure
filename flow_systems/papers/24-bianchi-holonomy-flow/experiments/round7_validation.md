# P24 Round-7 validation report

## Material Passport

- Origin Skill: `ars-codex:academic-research-suite` plus exact experiment validation
- Origin Stage: Stage 1 research
- Verification Status: `VERIFIED / REPRODUCIBLE`
- Primary-output SHA-256: `62aff0238f86ed9d582724a58b24d5cab31959742a2101fde026a043ab8d8024`
- Freeze SHA-256: `16bddd930a90af0fe673a698b912b9d302cfd126c5a1cb5bef48cfc496846b93`

## Exact theorem and finite audit

Write `gamma=I+3A`.  Over `Z[i]`,

```text
1 = det(gamma) = 1 + 3 tr(A) + 9 det(A),
```

so `tr(gamma)-2=3 tr(A)=-9 det(A)`.  Therefore
`D9(gamma)=(tr(gamma)^2-4)/9` is a Gaussian integer.  Trace proves
conjugacy invariance, and `tr(gamma^-1)=tr(gamma)` in `SL_2` proves inversion
invariance.  Cayley--Hamilton gives
`D9(gamma^r)=D9(gamma) S_(r-1)(tr(gamma))^2`, where
`S_0=1`, `S_1=t`, and `S_n=t S_(n-1)-S_(n-2)`.

The deterministic audit contains `11481`
unique exact matrices: `1` identity,
`504` parabolic, and
`10976` loxodromic.  It records
`145` distinct `D9` values and
`11336` rows beyond first occurrences.
For every row, determinant, level membership, integrality, conjugacy by `U1`,
inversion, and repetitions `r=1,...,5` pass by exact Gaussian-integer
arithmetic.

Non-injectivity already occurs after quotienting by conjugacy and inversion.
The ledger contains
`gamma_1=[[1,3],[3,10]]` and
`gamma_2=[[1,-3i],[3i,10]]`, both with `D9=13`.  For
`A_j=(gamma_j-I)/3`, their residues modulo 3 are
`[[0,1],[1,0]]` and `[[0,-i],[i,0]]`, which are neither equal nor negatives.
For `h` in `Gamma((3))`, reduction modulo 9 proves that `A mod 3` is unchanged
under `h gamma h^-1`, while inversion negates it.  The two matrices therefore
belong to distinct unoriented `Gamma((3))` owners despite their equal `D9`.

Decision: `RETAIN_AS_SOURCE_DERIVED_NECESSARY_INVARIANT_WITHOUT_OWNER_OR_METRIC_PREFIX`.

## Claim and Route boundary

`D9` is a source-derived necessary invariant.  The exact residue witness above
proves that it is non-injective even on unoriented `Gamma((3))` conjugacy
owners, and no Gaussian-prime ideal is assigned.  The sample is the elementary-generated
reduced-word ball through length five, not all of `Gamma((3))` and not a full
conjugacy enumeration.  It supplies neither a metric prefix nor a determinant.

The conservative typed-proxy tuple remains

```text
(A0_WEAK_ARITHMETIC_RELATION, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)
overall = ROUTE_A_EXPLORATORY
FULL_BIANCHI_FLOW_ROUTE_A_TUPLE=UNASSIGNED
ROUTE_B_INVOCATION_ALLOWED=false
```
