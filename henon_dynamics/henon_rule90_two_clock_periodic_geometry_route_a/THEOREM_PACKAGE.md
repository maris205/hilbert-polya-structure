# C145 proof package

## Claim

For every `L,n>=1`, let `F_L` be Rule 90 on the cyclic binary lattice of
length `L`.  Then

```text
#Fix(F_L^n)=2^deg gcd(x^L+1,(x^2+1)^n+x^n)          (over F_2).   (1)
```

This includes even `L` when `x^L+1` is not squarefree.  Möbius inversion gives
the exact-period points and division by `n` gives primitive temporal cycles.
The resulting periodic geometry depends essentially on the ordered two-clock
pair `(L,n)`.

## Status

**PROVABLE AS STATED.**

## Assumptions and notation

- `R_L=F_2[x,x^{-1}]/(x^L-1)`.  In characteristic two, `x^L-1=x^L+1`.
- `a=x+x^{-1}` and `F_L` is multiplication by `a`.
- `Fix(L,n)=#ker(F_L^n-I)`.
- `P_L(n)` counts points of least positive temporal period `n`.
- `C_L(n)` counts temporal cycles of least period `n`.

## Dependency map

1. Clear the Laurent denominator by the invertible monomial `x^n`.
2. Prove the multiplication-kernel lemma by ideal divisibility, without a
   distinct-root assumption.
3. Count the binary kernel to obtain (1).
4. Apply finite-set Möbius inversion and orbit partitioning.
5. Identify fixed configurations with labeled spatiotemporal tori.
6. Search the frozen finite ledger for exact information-loss witnesses.

## Lemma 1: multiplication kernels with multiplicity

Let `f,h` be polynomials over a field, with `f` monic, and let `m_h` be
multiplication by `h` on `k[x]/(f)`.  Put `g=gcd(f,h)`, `f=g f_1`, and
`h=g h_1`.  Since `gcd(f_1,h_1)=1`,

```text
f | hq  iff  g f_1 | g h_1 q  iff  f_1 | q.
```

Thus the kernel consists of the residue classes `f_1 r mod f` with
`deg r<deg g`.  They are linearly independent and span, so

```text
dim ker(m_h)=deg g.                                (2)
```

This proof uses divisibility, not roots; repeated factors of `f` cause no gap.

## Theorem 2: all-size fixed-point formula

The Laurent quotient is identified with `F_2[x]/(x^L+1)` because `x` is
invertible modulo a polynomial with constant term one.  In characteristic two,

```text
x^n(a^n-1)=(x^2+1)^n+x^n=:b_n.                    (3)
```

Multiplication by `x^n` is invertible, so `F_L^n-I` and multiplication by
`b_n` have the same kernel.  Applying (2) to `f=x^L+1`, `h=b_n` gives kernel
dimension `deg gcd(f,b_n)`.  A binary vector space of dimension `d` has `2^d`
elements, proving (1) for every `L,n>=1`.  For example,
`x^6+1=(x^3+1)^2`; the proof and ledger include this non-squarefree case.

## Theorem 3: exact temporal periods and tori

Every point fixed by `F_L^n` has least temporal period dividing `n`.  Therefore

```text
Fix(L,n)=sum_(d|n) P_L(d),
P_L(n)=sum_(d|n) mu(n/d) Fix(L,d),
C_L(n)=P_L(n)/n.                                  (4)
```

The last quotient is an integer because exact-period-`n` points partition into
cycles of size `n`.

A labeled `L x n` spatiotemporal torus is an array satisfying

```text
u_(i,j+1)=u_(i-1,j)+u_(i+1,j),   i mod L, j mod n.
```

Its row at time zero determines every row, and temporal closure is precisely
`F_L^n u=u`.  Hence the number of labeled tori is `Fix(L,n)`.

## Proposition 4: two-clock information loss

The complete `24 x 24` ledger gives three separately quantified area controls.

- In the full positive domain, the first area with unequal fixed counts is
  `3`: `(L,n)=(1,3)` has `1`, while `(3,1)` has `4`.
- Restricting to `L,n>=2`, the first such area is `6`: `(2,3)` has `1`, while
  `(3,2)` has `4`.
- Requiring at least one cell with nonzero exact-period content, the first such
  nondegenerate area is `12`; `(6,2)` has `Fix=16`, `P=12`, and `C=6`, while
  the other eligible aspect ratios have different fixed counts and zero
  exact-period content.

The qualifiers are part of the claims; no unbounded minimality is inferred
from the cutoff.  A second control fixes `L=5`: both `Fix(5,3)` and `Fix(5,6)`
equal `16`, but `P_5(3)=15` gives five primitive cycles, whereas `P_5(6)=0`.
Thus area loses aspect ratio and one fixed count loses divisor history.

## Route-A conclusion

The strict verdict is `(A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`, overall
`ROUTE_A_EXPLORATORY`.  The finite-volume primitive cycles are intrinsic and
exact, but circumference and time remain two essential clocks and no single
frozen target determinant exists.  No target global analytic structure,
arithmetic/local factor, natural operator lift, or Route-B authorization is
claimed.
