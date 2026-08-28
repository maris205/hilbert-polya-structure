# Round-8 universal congruence theorem and specificity obstruction

Date: **2026-08-28**

## Theorem A — universal normalized trace discriminant

Let `R` be a commutative ring with identity, let `m` be a non-zero-divisor in
`R`, and let

```text
gamma = I + m A in SL_2(R).
```

Then

```text
(tr(gamma)^2-4)/m^2 = m^2 det(A)^2 - 4 det(A) in R.
```

Here the quotient notation means the displayed numerator is exactly `m^2`
times the right-hand side; no fraction field is needed.  In particular, the
Round-7 Gaussian invariant

```text
D9(gamma)=(tr(gamma)^2-4)/9
```

is integral for every principal level-`(3)` determinant-one matrix over every
coefficient ring satisfying these hypotheses.  Its integrality is not special
to the Gaussian integers.

### Proof

The two-by-two determinant identity gives

```text
1 = det(I+mA) = 1 + m tr(A) + m^2 det(A).
```

Since `m` is a non-zero-divisor,

```text
tr(A) = -m det(A),
tr(gamma)-2 = m tr(A) = -m^2 det(A).
```

Therefore

```text
tr(gamma)^2-4
 = (tr(gamma)-2)(tr(gamma)+2)
 = (-m^2 det(A))(4-m^2 det(A))
 = m^2(m^2 det(A)^2-4 det(A)).
```

This proves the claim.

## Theorem B — first congruence jet laws

Under the same assumptions, define the oriented first jet

```text
J_m(gamma) = A mod m in M_2(R/mR).
```

The non-zero-divisor hypothesis makes `A=(gamma-I)/m` unique.  Then:

1. for `h in Gamma((m))`,
   `J_m(h gamma h^-1)=J_m(gamma)`;
2. `J_m(gamma^-1)=-J_m(gamma)`; and
3. for every integer `r>=1`, `J_m(gamma^r)=r J_m(gamma)`.

Consequently, the sign class `[J_m(gamma)]_{+/-}` is a necessary invariant of
unoriented conjugacy/inversion owners **inside `Gamma((m))`**.

### Proof

Because `h` and `h^-1` reduce to `I` modulo `m`,

```text
h gamma h^-1 = I + m(h A h^-1),
h A h^-1 = A mod m.
```

Also

```text
gamma^-1-I = -m A gamma^-1,
```

and `gamma^-1=I mod m`, proving the inversion law.  Finally, the binomial
identity in the matrix ring gives

```text
(I+mA)^r = I + r m A + m^2(...),
```

which proves the repetition law after division by `m` and reduction modulo
`m`.

The theorem does not claim invariance under conjugation by the full ambient
`SL_2(R)`, nor does it claim that the jet class is a complete conjugacy
classifier.

## Four exact A0 controls

The pre-result contract froze four controls before the canonical build.

| Control | Exact finite panel | Result | Consequence |
|---|---:|---|---|
| full Gaussian ambient parent | 4 witnesses | 3/4 have nonintegral `/9` discriminant | the level hypothesis is essential |
| rational-integer level 3 | 485 matrices | 485/485 pass | Gaussian coefficients are unnecessary |
| Gaussian neighbor levels 2 and 4 | 1,969 + 1,969 matrices | all pass their level-normalized formula | level 3 is not unique |
| Eisenstein-integer level 3 | 1,969 matrices | 1,969/1,969 pass | the identity persists in another imaginary-quadratic ring |

The executable panel therefore contains **6,396** exact matrices/witnesses,
and all four pre-frozen control families were executed.  The
principal-congruence theorem has zero finite-replay failures.  Under the
Route-A evaluator taxonomy, however, these families instantiate only two
canonical types—`simpler parent system` and `neighboring dynamical
parameters`—rather than the required three.  The canonical mandatory gate is
therefore `INCOMPLETE_2_OF_3_CANONICAL_TYPES`; the result below is a negative
specificity theorem, not a claim that the mandatory gate is complete:

```text
REFUTED_D9_IS_NOT_GAUSSIAN_SPECIFIC
STOP_SCOPED_D9_OWNER_MECHANISM
```

Passing the controls cannot be counted as positive evidence for a Gaussian
prime-ideal owner.  It proves that `D9` alone would certify the same algebraic
property for much broader systems.

## Frozen first-jet collision census

The Round-8 build reuses all **11,481** exact Round-7 Gaussian matrices.

```text
distinct D9 values                         = 145
distinct first jets up to sign              = 41
distinct joint (D9, signed jet) descriptors = 517
D9 collision rows beyond first           = 11,336
joint-descriptor collision rows           = 10,964
collision rows separated by first jet        = 372
exact reduction                         = 372/11,336
decimal reduction                        = 0.032815808045166
largest D9 bucket                           = 505
largest joint-descriptor bucket              = 84
singleton joint-descriptor buckets             = 0
```

The exact Round-7 pair

```text
gamma_1=[[1,3],[3,10]],
gamma_2=[[1,-3i],[3i,10]],
D9(gamma_1)=D9(gamma_2)=13
```

has distinct signed first jets and is therefore separated.  This is a genuine
owner-refinement result.  Its aggregate effect is nevertheless limited: it
removes only 372 of 11,336 matrix-row collisions.  The remaining 10,964 rows
are described only as **matrix descriptor collisions**.  They are not asserted
to be distinct conjugacy owners because the finite word ball is not a complete
conjugacy census.

## Paper consequence and Route boundary

Round 8 converts the Round-7 observation into a stronger, paper-ready result:
an exact universality theorem, a four-family specificity obstruction, and a
quantified first-jet refinement theorem.  The scientific conclusion is
negative for the proposed `D9` owner mechanism but positive as a structural
classification result.  The separate canonical Route-A control-type gate
remains incomplete at `2/3`.

The allowed claim is:

> Level-normalized trace-discriminant integrality is a universal
> principal-congruence identity.  The signed first congruence jet is a sharper
> necessary owner invariant, but neither object supplies a Gaussian-prime-ideal
> correspondence.

The typed proxy remains

```text
(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)
overall = ROUTE_A_EXPLORATORY
```

The complete Bianchi flow stays `UNASSIGNED`; no metric primitive prefix,
dynamical determinant, zero comparison, or Route-B invocation is authorized.
