# C152 proof package

## Status and definitions

**Status: PROVABLE AS STATED.**  Ordered positive pairs retain coordinate
swap; axes are excluded.  For `t>0`, define

```text
H_prim(t)=sum_(m,n>=1,gcd(m,n)=1) exp(-4t(m^2+n^2)).       (1)
```

Each ordered primitive direction contributes once.  If distinct directions
have equal length, their contributions add; no collision is deduplicated.
The factor four is `L_(m,n)^2` for unit-square billiard length
`L_(m,n)=2 sqrt(m^2+n^2)`.

## Theorem 1: absolute convergence and exact factorization

Let `theta_+(u)=sum_(k>=1) exp(-u k^2)`.  Then

```text
H_prim(t)=sum_(d>=1) mu(d) theta_+(4td^2)^2.                (2)
```

Both (1) and the absolutely valued version of the right side converge for
every `t>0`.

**Proof.**  The coprimality indicator is
`sum_(d|m,d|n)mu(d)`.  Substituting `m=da,n=db` gives (2) formally.  For a
positive decreasing Gaussian,

```text
theta_+(4td^2) <= integral_0^infinity exp(-4td^2x^2)dx
                 =sqrt(pi)/(4d sqrt(t)).
```

Therefore the sum of absolute values after the substitution is at most
`pi/(16t) sum d^(-2)`, which is finite.  This justifies every interchange and
also proves (1) convergent. ∎

Equivalently, if `b_s` counts all ordered positive representations
`s=a^2+b^2` and `c_s` counts the primitive ones, then

```text
c_s=sum_(d^2|s) mu(d)b_(s/d^2).                            (3)
```

The evidence and independent checker verify (3) for every `s<=20000`.

## Theorem 2: primitive quarter-disk count

For real `R>=0`, define

```text
Q(R)=#{(m,n) in Z_{>=1}^2: m^2+n^2<=R^2},
N(R)=#{the same pairs with gcd(m,n)=1}.
```

Then

```text
Q(R)=pi R^2/4+O(R+1),                              (4)
N(R)=3R^2/(2pi)+O(R log R).                         (5)
```

**Proof.**  Comparing the union of unit squares anchored at positive lattice
points with quarter disks of radii differing by `sqrt(2)` proves (4); excluding
the axes changes only `O(R+1)` points.  Möbius inversion, with the real
argument retained, gives

```text
N(R)=sum_(d<=R/sqrt(2)) mu(d)Q(R/d).                (6)
```

The main term in (6) contains
`sum_(d<=R/sqrt(2))mu(d)/d^2`.  Absolute convergence and the Dirichlet
convolution identity for the Möbius function give
`sum_(d>=1)mu(d)/d^2=1/zeta(2)=6/pi^2`; here the final equality is the Basel
sum.  The omitted tail is `O(1/R)`.  The error from (4) is
`O(R sum_(d<=R)1/d)+O(R)=O(R log R)`.  Substitution proves (5). ∎

## Theorem 3: small-time law

As `t` decreases to zero,

```text
H_prim(t)=3/(8pi t)+O(t^(-1/2)log(1/t)).            (7)
```

**Proof.**  Stieltjes integration by parts (the boundary terms vanish) gives

```text
H_prim(t)=8t integral_0^infinity r exp(-4tr^2)N(r)dr.       (8)
```

Put `c=3/(2pi)` in (5).  The main term in (8) is

```text
8tc integral_0^infinity r^3 exp(-4tr^2)dr=c/(4t)=3/(8pi t).
```

Using `N(r)-cr^2=O(r log(2+r))`, the remaining integral is bounded by
`O(t integral r^2 log(2+r) exp(-4tr^2)dr)`.  The change
`u=sqrt(t)r` makes this
`O(t^(-1/2)log(1/t))`; the bounded small-`r` part is smaller. ∎

## Boundary

Equation (1) is a positive heat transform of source direction labels.  It is
not a clean wave trace, not a Gutzwiller or isolated-orbit determinant, and
not `Tr exp(t Delta_D)` or any other Dirichlet eigenvalue trace.  The positive
Dirichlet half-wave on the same unit-square classical geometry remains a
natural self-adjoint quantization, but no identity between its spectrum and
(1) is claimed.

The strict tuple is
`(A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`.  No target divisor,
functional equation, counting law, arithmetic/local datum, Euler factor, root
number, automorphy statement, Hilbert--Polya construction, or Route-B
authorization is present.
