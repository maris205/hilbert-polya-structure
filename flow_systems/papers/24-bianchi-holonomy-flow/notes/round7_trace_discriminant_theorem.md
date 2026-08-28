# Round-7 exact trace-discriminant theorem

Date: **2026-08-28**

## Proposition

Let `gamma` belong to `SL_2(Z[i])` and satisfy `gamma = I (mod 3)`.  Define

```text
D9(gamma) = (tr(gamma)^2 - 4) / 9.
```

Then:

1. `D9(gamma)` is a Gaussian integer;
2. `D9(h gamma h^-1)=D9(gamma)` whenever the conjugate is defined;
3. `D9(gamma^-1)=D9(gamma)`; and
4. for every integer `r>=1`,

   ```text
   D9(gamma^r) = D9(gamma) S_(r-1)(tr(gamma))^2,
   S_0(t)=1, S_1(t)=t, S_n(t)=t S_(n-1)(t)-S_(n-2)(t).
   ```

All four statements are exact and use no prime or zero target data.

## Proof

Write `gamma=I+3A` with `A` in `M_2(Z[i])`.  The two-by-two determinant
identity gives

```text
1 = det(I+3A) = 1 + 3 tr(A) + 9 det(A).
```

Consequently `tr(A)=-3 det(A)` and

```text
tr(gamma)-2 = 3 tr(A) = -9 det(A).
```

Thus

```text
D9(gamma) = ((tr(gamma)-2)/9) (tr(gamma)+2)
```

lies in `Z[i]`.  Trace is invariant under conjugacy.  For a two-by-two
determinant-one matrix, Cayley--Hamilton implies
`tr(gamma^-1)=tr(gamma)`, proving the second and third statements.

For repetition, Cayley--Hamilton also yields the integer-polynomial recurrence
for `S_n`.  Equivalently, in a formal splitting extension with eigenvalues
`lambda` and `lambda^-1`,

```text
lambda^r-lambda^(-r)
  = S_(r-1)(lambda+lambda^-1) (lambda-lambda^-1).
```

Squaring and using
`tr(gamma^r)^2-4=(lambda^r-lambda^(-r))^2` proves the stated identity.
Because it is a polynomial identity over the coefficient ring, the argument
does not require diagonalizability of a particular matrix.  This completes
the proof.

## Frozen finite audit

The canonical Round-7 build applies the proposition to all **11,481** unique
exact matrices already frozen in the elementary-generated reduced-word ball
through length five.  It records 1 identity, 504 parabolic, and 10,976
loxodromic matrices.  Exact Gaussian-integer arithmetic verifies determinant,
level membership, integrality, conjugacy by the frozen `U1` witness, inversion,
and repetitions `r=1,...,5` for every row.

Only **145** distinct `D9` values occur, leaving **11,336** rows beyond first
occurrences.  These collisions are not a defect in the theorem: they are a
warning that matrix-level multiplicity is enormous.  More strongly, the
ledger contains the exact loxodromic pair

```text
gamma_1=[[1,3],[3,10]],       A_1 mod 3=[[0,1],[1,0]],
gamma_2=[[1,-3i],[3i,10]],    A_2 mod 3=[[0,-i],[i,0]],
D9(gamma_1)=D9(gamma_2)=13,
```

where `A_j=(gamma_j-I)/3`.  If `h=I+3B` belongs to `Gamma((3))`, expansion
modulo `9` gives

```text
(h gamma h^-1-I)/3 = A  (mod 3),
(gamma^-1-I)/3 = -A      (mod 3).
```

The two displayed residues are neither equal nor negatives in
`M_2(Z[i]/(3))`.  Thus the matrices lie in distinct unoriented
`Gamma((3))` conjugacy/inversion owners although their `D9` values agree.
This proves that `D9` itself is not a unique orbit owner, independently of
the much larger aggregate collision count.

## Scientific consequence and firewall

This is a paper-level positive result after the Round-6 phase statistic was
stopped: the arithmetic source supplies an intrinsic, exact, conjugacy- and
repetition-compatible Gaussian-integer invariant.  It is, however, only a
**necessary invariant**.  It does not provide:

- a bijection or canonical map from primitive geodesics to Gaussian-prime
  ideals;
- full `Gamma((3))` generation, conjugacy completeness, or group-certified
  primitivity;
- a metric length prefix, dynamical zeta function, Fredholm determinant, or
  zero comparison; or
- permission to promote the typed proxy beyond
  `(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`.

The complete Bianchi flow remains `UNASSIGNED`, and Route B remains closed.
