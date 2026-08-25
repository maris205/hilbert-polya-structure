# C165 proof package

## Definition and full-tick convention

Let `X_m={0,1}^{Z/(2m)Z}`.  The first layer `A` swaps the disjoint pairs

```text
(0,1),(2,3),...,(2m-2,2m-1),
```

and the staggered layer `B` swaps

```text
(1,2),(3,4),...,(2m-1,0).
```

One clock tick is `T=B after A`.  Track a labelled cell rather than choosing
a pullback convention for configuration coordinates; the two conventions
have inverse site permutations and the same fixed and cycle data.

## Theorem 1: exact site motion and four-letter conjugacy

Let `tau` be the labelled-cell motion.  An even site first moves right under
`A` and again right under `B`; an odd site moves left twice.  Thus

```text
tau(i)=i+2 mod 2m  for even i,
tau(i)=i-2 mod 2m  for odd i.                         (1)
```

Define, for `j mod m`,

```text
e_j=2j,       o_j=1-2j mod 2m,
Phi(x)_j=(x_(e_j),x_(o_j)) in {0,1}^2.               (2)
```

Equation (1) gives `tau(e_j)=e_(j+1)` and
`tau(o_j)=o_(j+1)`.  Therefore `Phi` is a bijection from binary
configurations to length-`m` words over the four-letter alphabet `{0,1}^2`
and intertwines one full Margolus tick with one cyclic rotation.  This is an
exact conjugacy, not a fixed-count coincidence.

## Theorem 2: fixed points, exact periods, and zeta

The `n`-th power of a length-`m` rotation has `gcd(m,n)` coordinate cycles.
A four-letter word fixed by it is constant independently on each cycle, so

```text
#Fix(T^n)=4^gcd(m,n),                  m,n>=1.          (3)
```

Every least period divides `m`.  If `P_m(d)` counts labelled configurations
of exact period `d`, fixed-point partitioning and Moebius inversion give

```text
P_m(d)=sum_(e|d) mu(d/e) 4^e,          d|m,            (4)
C_m(d)=P_m(d)/d.                                         (5)
```

Here `C_m(d)` is an integer because exact-period points form disjoint
`d`-cycles.  Grouping the trace-log by those cycles yields the complete
finite Artin--Mazur zeta

```text
zeta_T(z)=product_(d|m) (1-z^d)^(-C_m(d)).             (6)
```

At `m=1`, both swap layers are the same transposition, so the full tick is
the identity on four configurations.  Equations (3)--(6) give
`P_1(1)=C_1(1)=4`; no exception or division by an empty clock is needed.
At `m=2`, `P_2(1)=4`, `P_2(2)=12`, and there are six two-cycles.

## Theorem 3: a uniform full-period concentration bound

Every proper divisor `d` of `m` satisfies `d<=m/2`.  Moreover
`0<=P_m(d)<=4^d`, and there are fewer than `m` proper divisors.  Hence

```text
# {x:per(x)<m}
 =sum_(d|m,d<m) P_m(d)
 <=m 4^(m/2).
```

Division by `|X_m|=4^m` proves, for every `m>=1`,

```text
Pr(per<m)<=m 4^(-m/2)=m/2^m,
Pr(per=m)>=1-m 4^(-m/2).                               (7)
```

For `m=1` the short-period set is empty and (7) remains true.  The factor
`m` deliberately trades sharp divisor information for a uniform elementary
bound; no optimality is claimed.

## Theorem 4: reversor and same-clock Koopman determinant

Let `r(i)=-i mod 2m`.  Parity is preserved, and direct substitution in (1)
gives

```text
r tau r=tau^(-1).                                      (8)
```

The induced configuration reflection `R` therefore satisfies
`R T R=T^(-1)`.  On the finite Hilbert space `H_m=l2(X_m)` with counting
measure, put

```text
(U_T f)(x)=f(T^(-1)x).
```

This is a unitary permutation.  Each dynamical `d`-cycle contributes one
cyclic permutation block whose determinant factor is `1-z^d`.  Consequently

```text
det(I-z U_T)=product_(d|m)(1-z^d)^(C_m(d))
            =zeta_T(z)^(-1).                           (9)
```

If `Theta f(x)=conjugate(f(Rx))`, then `Theta` is an involutive antiunitary
and

```text
Theta U_T Theta=U_T^(-1).                              (10)
```

This is a natural finite same-clock Koopman lift.  A permutation unitary is
self-adjoint exactly when its permutation is an involution.  Here `T=I` at
`m=1`, and `T^2=I` at `m=2`.  For every `m>=3`, the exact-period formula gives
`P_m(m)>0`, hence an `m`-cycle, so `T^2` is not the identity and `U_T` is not
self-adjoint.  No uniform self-adjoint realization, infinite-volume limit,
or Hilbert--Polya operator is asserted.

## Evidence and Route-A boundary

The released exact ledger covers `1<=m<=16`, 136 fixed-time cells and 50
period cells.  Direct configuration enumeration checks 87,380 states through
`m=8`.  These are sentinels for (1)--(10), whose proofs are all-parameter.

The strict tuple is

```text
(A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION),
overall ROUTE_A_EXPLORATORY.
```

There is no target divisor or global target-analytic comparison.  The model
is exactly solvable and reversible but is not described as chaotic or
interacting.  No arithmetic local data, Euler factors, root numbers,
automorphy, self-adjoint target operator, or Route-B authorization is claimed.
