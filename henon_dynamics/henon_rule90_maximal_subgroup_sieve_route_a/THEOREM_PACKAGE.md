# C160 proof package

## Source lemma

Let `L=2^r-1`, `r>=2`, and identify cyclic states with
`R_L=F_2[x,x^(-1)]/(x^L-1)`.  Rule 90 is multiplication by
`a=x+x^(-1)`.  Frobenius gives `a^(L+1)=a`.  Since the kernel has dimension
one, the complete periodic set is `V=im(a)`, with dimension `L-1`; its
restriction `g` satisfies `g^L=I`.  Indeed, `a^d v=v` implies
`v=a(a^(d-1)v)` and hence every periodic or fixed state lies in `V`, whereas
`a^L(au)=a^(L+1)u=au` makes every image state periodic.

For every `d>=1`, clearing the Laurent monomial gives

```text
D_L(d)=deg gcd(x^L+1,(x^2+1)^d+x^d),
|Fix_V(g^d)|=2^(D_L(d)).                                      (1)
```

Every realized period divides `L`.

## Theorem 1: exact maximal-subgroup sieve

Let `P(L)` be the set of distinct ordinary integer prime divisors of the
source circumference.  A point with period `m<L` has `m|L`; choose a prime
`p` dividing `L/m`.  Then `m|L/p` and the point lies in `Fix(g^(L/p))`.
The converse is immediate, so

```text
{v in V:per(v)<L}=union_(p in P(L)) Fix(g^(L/p)).              (2)
```

For a nonempty subset `Q` of distinct factors, polynomial Bézout identities
for `g^L=I` imply that the intersection of the fixed kernels is fixed by the
greatest common divisor of their clocks.  Since

```text
gcd_{p in Q}(L/p)=L/product_{p in Q}p,
```

inclusion--exclusion and (1) give the all-length exact formula

```text
N_<L = sum_(empty!=Q subset P(L)) (-1)^(|Q|+1)
       2^(D_L(L/product(Q))).                                  (3)
```

Its first two Bonferroni truncations rigorously bracket `N_<L`.  Formula (3)
uses at most `2^omega(L)-1` maximal-subgroup intersections instead of all
`L-1` proper clock times.  It equals the independent Möbius exact-period
formula, but supplies the stronger set-theoretic geometry and sharp overlap
corrections missing from C155.

## Theorem 2: every Mersenne-prime source size

Assume additionally that `L>3` is prime.  Since every period divides `L`, its
support is contained in `{1,L}`.  A fixed state has multiplier eigenvalue one,
so after clearing `x` it is controlled by

```text
x^2+x+1=0.                                                     (4)
```

The nontrivial roots of (4) have order three.  They occur among the `L`-th
roots only if `3|L`, impossible for prime `L>3`.  Thus `D_L(1)=0` and zero is
the unique fixed state.  Consequently

```text
P_L(1)=1,
P_L(L)=2^(L-1)-1,
C_L(L)=(2^(L-1)-1)/L,
Pr_V(period<L)=2^(-(L-1)).                                    (5)
```

The complete finite dynamical zeta is therefore

```text
zeta_g(z)=1/((1-z)(1-z^L)^((2^(L-1)-1)/L)).                   (6)
```

At the excluded `L=3`, equation (4) divides `x^3+1`; `g` is the identity on
the four-state image.  This exact exception is retained.  Theorem 2 applies
to every source length meeting its premise and makes no claim that infinitely
many such lengths exist.

## Boundary

The ordinary factors of `L` describe maximal subgroups of a finite source
clock; they are not arithmetic local factors.  The strict tuple is

```text
(A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL), overall ROUTE_A_EXPLORATORY.
```

There is no target divisor, target analytic comparison, natural operator
lift, or Route-B authorization.
