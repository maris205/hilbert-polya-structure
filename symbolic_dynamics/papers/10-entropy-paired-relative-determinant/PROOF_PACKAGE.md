# SD-C12 Proof Package

## Claim

Entropy-adjacent `1|1` pairing defines a relative trace-class symbolic
transfer on `Re(s)>0`, an exact relative Fredholm determinant, and a
reflection-symmetric zero-free completion on `0<Re(s)<1`. The completion
moves nontrivially on the critical line. Any fixed finite-block local
cancellation rule that extends the zero-order trace to all `Re(s)>0` must
have block coefficient sum zero, so it cannot orient every prime with `+1`.

## Status

PROVABLE AS STATED under the frozen hypotheses below.

The proved operator theorem does not pass the Route-A target ledger. Its
evaluation is `ROUTE_A_REJECTED`; exactness of the auxiliary determinant is
not promoted to arithmetic-candidate status.

## Assumptions

- `p_1<p_2<...` are the rational primes, obtained as tensor atoms and ordered
  by entropy.
- Adjacent pairing and its orientation are frozen modeling choices relative
  to that ordered list, not invariants forced by tensor factorization.
- `U` pairs the odd and even rank basis vectors.
- The primary determinant uses `z=1`; the two-variable statement is made on
  `|z|2^(-Re(s))<1`.
- The finite-block theorem uses one fixed coefficient pattern on consecutive
  blocks. Its necessity assumes asymptotic locality and divergence of the
  reciprocal block inventory; both hold for the primes.

## Notation

- `D_s^+=diag(p_(2n-1)^(-s))`.
- `B_s=U^*D_s^-U=diag(p_(2n)^(-s))`.
- `S_r(s)=Tr((D_s^+)^r-B_s^r)`.
- `R(s,z)=det_F[(I-zD_s^+)(I-zB_s)^(-1)]`.
- `H(s,z)=R(s,z)R(1-s,z)`.

## Proof Strategy

Pair adjacent entropy values and integrate the derivative of `x^(-s)` over
their disjoint intervals. This gives a summable trace-norm majorant without
estimating the two prime sectors separately. Fredholm determinant theory then
gives the product and all relative traces. Reflection is multiplication by
the same construction at `1-s`. Strict critical-line motion follows from the
positive second derivative of `log H(1/2+it,1)` at `t=0`. Discrete Abel
summation proves the finite-block theorem.

## Dependency Map

1. The trace-class theorem uses the entropy pairing and the integral identity.
2. The determinant theorem uses the trace-class theorem and invertibility of
   both diagonal factors.
3. Reflection uses the half-plane theorem twice.
4. The motion theorem uses reflection, termwise differentiation on compact
   subsets, and strict monotonicity of a scalar function `g(x)`.
5. The finite-block theorem uses discrete Abel summation for sufficiency and
   the frozen locality/divergence assumptions for necessity.

## Proof

### Step 1: trace norm

For `sigma=Re(s)>0`,

```text
p_(2n-1)^(-s)-p_(2n)^(-s)
 = s integral_[p_(2n-1),p_(2n)] x^(-s-1) dx.
```

The intervals are disjoint, hence

```text
||D_s^+-B_s||_1
 <= |s| integral_2^infinity x^(-sigma-1) dx
 = |s| 2^(-sigma)/sigma.
```

The same estimate, with `s` replaced by `rs`, gives

```text
||(D_s^+)^r-B_s^r||_1 <= (|s|/sigma)2^(-r sigma).
```

Local uniformity proves trace-norm holomorphy.

### Step 2: relative determinant

When `|z|2^(-sigma)<1`, both diagonal factors are invertible and

```text
(I-zD_s^+)(I-zB_s)^(-1)-I
 = -z(D_s^+-B_s)(I-zB_s)^(-1)
```

is trace class. Therefore its Fredholm determinant exists and equals

```text
R(s,z)=product_n (1-zp_(2n-1)^(-s))/(1-zp_(2n)^(-s)).
```

Moreover,

```text
log R(s,z)=-sum_(r>=1) z^r S_r(s)/r,
```

and the estimate from Step 1 proves absolute local convergence. At `z=1`
the condition holds for every `sigma>0`.

### Step 3: reflection and zero-freeness

Both factors in `H(s,1)=R(s,1)R(1-s,1)` exist exactly when
`0<Re(s)<1`, and swapping `s` with `1-s` swaps them. Every diagonal local
factor has modulus strictly below one before subtraction from one. Thus both
relative quotient operators are invertible. Their Fredholm determinants, and
hence `H`, are nonzero throughout the strip.

### Step 4: strict critical-line motion

On `s=1/2+it`, reflection and conjugation give
`H(s,1)=|R(s,1)|^2`. Set

```text
g(x)=x^(-1/2)(log x)^2/(1-x^(-1/2))^2.
```

Termwise differentiation yields

```text
d^2/dt^2 log H(1/2+it,1)|_(t=0)
 =2 sum_n [g(p_(2n-1))-g(p_(2n))].
```

Writing `y=sqrt(x)` gives

```text
g(x)=4y(log y)^2/(y-1)^2.
```

Its logarithmic derivative is negative because
`log y>2(y-1)/(y+1)` for `y>1`; the latter difference has derivative
`(y-1)^2/[y(y+1)^2]>0` and vanishes at `y=1`. Hence every summand is positive.
The series converges by the alternating-series criterion applied to the
decreasing sequence `g(p_n)`. The second derivative is strictly positive, so
the reflected determinant is not vertically constant.

### Step 5: finite-block rigidity

For a fixed block pattern `c_1,...,c_m`, let
`A_n(s)=sum_j c_j x_(mn+j)^(-s)`. If `sum_j c_j=0`, discrete Abel summation
writes each `A_n` as a fixed linear combination of adjacent differences.
The disjoint-interval estimate from Step 1 then gives absolute local
convergence on `Re(s)>0`. Conversely, if the block sum is nonzero and the
inventory is asymptotically local, then at `s=1`,
`A_n(1)` is asymptotic to the nonzero block sum divided by the first block
entry. Divergence of the reciprocal block inventory prevents trace-class
summation. Thus zero block sum is necessary and sufficient in the frozen
class. All-positive coefficients have block sum `m`, so they fail.

Therefore the claim follows. ∎

## Corrections or Missing Assumptions

- The finite-block necessity theorem is not asserted for block patterns that
  change with rank, sparse defects, unbounded block size, or arbitrary decaying
  coefficients.
- The determinant is a relative Fredholm determinant. Neither individual
  Fredholm determinant exists throughout the half-plane; on `Re(s)<=1`, the
  product notation must not be read as a quotient of standalone determinants.

## Open Risks

- Entropy-rank parity is canonical only after fixing the least atom and the
  orientation `odd=plus`; reversing it inverts `R`.
- Reflection plus zero-freeness does not supply a completed divisor.
- No operator-domain or self-adjoint spectral realization is present.

## Conservative Route evaluation

```text
(A0_ANALYTIC_ARITHMETIC_ORIGIN,
 A1_FAIL,
 A2_ANALYTIC_DETERMINANT,
 A3_FAIL,
 A4_FAIL)

ROUTE_A_REJECTED
GO_COMMON_STRIP_RELATIVE_DETERMINANT
STOP_POSITIVE_EULER_ORIENTATION
STOP_DIVISOR
STOP_SCOPED / PROVES_TOO_MUCH
ROUTE_B_LOCKED
```

Here `A1_FAIL` is specifically a target-ledger failure, while
`A2_ANALYTIC_DETERMINANT` applies only to the exact auxiliary relative
determinant; those qualifiers are not additional evaluator enum values.

The A3 reflection is tautological: `H(s,z)` was defined by multiplying the
copy at `1-s`. It is a correct symmetry of the auxiliary object, not a derived
arithmetic functional equation.
