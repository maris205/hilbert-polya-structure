# AS3-H: the full Heisenberg fixed-fibre answer

2026-09-08 UTC. Author proof; pending nonauthor review. One original
all-iterate question, not a list of auxiliary paper contracts.

## 1. Complete statement

Let `H`, `Gamma`, `A`, `q`, and `Phi` be exactly as in the
[frozen question](FROZEN_QUESTION.md). Define Fibonacci and Lucas numbers
by

```
F_0=0, F_1=1, F_(n+2)=F_(n+1)+F_n,
L_0=2, L_1=1, L_(n+2)=L_(n+1)+L_n.
```

For every `n>=1`, put

```
g_n = L_n if n is odd, and F_n if n is even,
Q(x,y)=x^2-xy-y^2,
S_n={(x/g_n,y/g_n) mod Z^2 : Q(x,y)=0 mod g_n}.
```

**Theorem.** The complete fixed set of `Phi^n` is precisely the union of
the central circle fibres above `S_n`. In particular there is one such
circle per element of `S_n`, and

```
C_n = R(g_n),
R(g) = product_(p^e || g) R_p(e),             (1)
R_2(e) = 2^(2 floor(e/2)),
R_5(e) = 5^e,
R_p(e) = (e+1)p^e-e p^(e-1)  if p is odd, p!=5, (5/p)=+1,
R_p(e) = p^(2 floor(e/2))     if p is odd, p!=5, (5/p)=-1.
```

The empty product is one. These formulas include all iterates and all
ramified, dyadic, inert, split, and repeated-prime cases. They contain no
unevaluated finite sum. More importantly, `S_n` itself gives all fixed
fibres rather than merely their cardinality.

For each divisor `d|n`, identify `S_d` and `S_n` as subsets of the same
horizontal torus. The fibres with pointwise least period exactly n are

```
S_n \ union_(d|n, d<n) S_d.                  (2)
```

Every point on one such fibre has that same least period. Their number is
`E_n=sum_(d|n) mu(n/d) C_d`. This is a number of circle fibres, not a number
of isolated periodic orbits; division by n is not asserted to give an
integer orbit count.

## 2. Exact central coordinate; the lattice is not discarded

Set

```
t=z-xy/2+(x+y)/2.
```

Substitution into the original one-step formula gives

```
t(Phi(x,y,z))=t(x,y,z).                      (3)
```

Indeed, if `t_0=z-xy/2`, its increment is `-x-y/2`, while the increment
of `(x+y)/2` is `x+y/2`. Thus the lifted map is `(v,t)->(Av,t)`.
This does not conjugate the compact quotient to a product torus.

Left multiplication by the lattice element `(m_1,m_2,k)` changes t by

```
k+(m_1 y-x m_2-m_1 m_2+m_1+m_2)/2.          (4)
```

For `B=A^n`, `M=B-I`, a base return satisfies `m=Mv in Z^2`. Equations
(3)-(4) prove that its whole central fibre is fixed exactly when

```
rho_n(m)=(det(v,m)+m_1 m_2-m_1-m_2)/2=0 mod 1.   (5)
```

This is the original C151 rotation, not a replacement observable: rewriting
(3) in the old coordinate gives
`q_n(v)=((Bv)_1(Bv)_2-v_1v_2-(Bv)_1-(Bv)_2+v_1+v_2)/2`, and subtracting
`m_1 v_2` gives exactly (5). No unknown affine drift remains.

## 3. The integral cofactor and its norm identity

The C156 matrix factorizations, reproduced here to fix coordinates, are

```
M=g U,
U=[[F_(n+1),F_n],[F_n,F_(n-1)]]   (n odd),
U=[[L_(n+1),L_n],[L_n,L_(n-1)]]   (n even).     (6)
```

They follow from `A=Q_0^2`, `Q_0=[[1,1],[1,0]]`, Fibonacci doubling and
Cassini. They were already proved in C156 and are not a new increment.
Write `U=[[r,s],[s,t]]`. The recurrence gives `r-t=s`, and

```
det U=-1 (n odd), -5 (n even),
Q(Uw)=(det U) Q(w).                          (7)
```

For clarity, the coefficients of `x^2,xy,y^2` on the left of (7) are
`r^2-rs-s^2`, `2rs-rt-s^2-2st`, `s^2-st-t^2`. Using `r=t+s`, these are
respectively `det U`, `-det U`, `-det U`.

We will also use the following exact elementary divisibility facts:

```
g odd  => s odd and gcd(s,g)=1;
g even => 4|g, s=2u with u odd and gcd(u,g)=1.   (8)
```

Here s is `F_n` in the odd case and `L_n` in the even case. The identity
`L_n^2-5F_n^2=4(-1)^n` excludes every common odd prime. Both sequences
modulo two have period three. For the remaining assertions, use
`Q_0^12=[[233,144],[144,89]]=I mod 8` and the residue classes modulo 12:
if n is odd and divisible by 3, then `F_n=2 mod 4` and `L_n=4 mod 8`;
if n is even and divisible by 3, then `F_n=0 mod 8` and `L_n=2 mod 4`.
The latter uses n congruent to 0 or 6, the former 3 or 9. The displayed
matrix identity and those four initial residues prove the assertions for
all n, rather than extrapolating a finite computation.

## 4. The index-five selection is necessary and sufficient

Horizontal returns are indexed by `m in Z^2/MZ^2`, with `v=M^-1 m`.
If n is odd, U is unimodular, so every class uniquely has `m=Uw` with
`w in (Z/gZ)^2`; then `v=w/g`.

For even n it is essential not to assume this for all horizontal classes:
the total horizontal quotient has `5g^2` elements. We prove that every
zero-rotation class nevertheless lies in the index-five sublattice `UZ^2`.
The inverse matrix gives, with `d=det U`,

```
det(M^-1 m,m) = s Q(m)/(g d).                 (9)
```

In the even case `d=-5`. If (5) is zero, multiplication by `10g` shows
that `5|s Q(m)`. The identity in Section 3 gives `L_n^2=4 mod 5` for
even n, so `5` does not divide s. Therefore `Q(m)=0 mod 5`.

But `Q(X,Y)=(X+2Y)^2 mod 5`. Hence its zero locus modulo 5 is one
linear subspace of size five. By (7), `UZ^2` reduces into this subspace.
Since `det U=-5`, its reduction has rank one, and `UZ^2` is exactly the
preimage of that subspace: both sublattices have index five. Consequently

```
rho_n(m)=0 => m in UZ^2.                    (10)
```

On this sublattice `m=Uw` is unique modulo `gUZ^2` exactly when w is
unique modulo `gZ^2`. There is no factor-five multiplicity and no discarded
zero-rotation class. Again `v=w/g`.

## 5. Uniform removal of the affine parity term

For every n, after the forced coordinate step in Section 4, write
`m=Uw`, `v=w/g`. Direct expansion using `r-t=s` gives

```
rho_n(Uw) = s Q(w)/(2g) + P(Uw)/2,
P(a,b)=ab-a-b.                              (11)
```

Always `P(a,b)=Q(a,b) mod 2`. By (7), since det U is odd,

```
P(Uw)=Q(w) mod 2.                           (12)
```

If g is odd, (8) says s is odd and prime to g. The integer
`s Q(w)+g P(Uw)` is even by (12). It is divisible by `2g` if and only
if it is divisible by g, which is equivalent to `Q(w)=0 mod g`.

If g is even, write `s=2u` as in (8). Equation (11) is zero if and only if

```
u Q(w)+(g/2) P(Uw)=0 mod g.                 (13)
```

Reducing modulo two uses `4|g` and odd u; it forces `Q(w)=0 mod 2`.
The binary form `X^2+XY+Y^2` is zero over F_2 only at `(0,0)`.
Thus both coordinates of w are even, so the same is true of Uw and
`P(Uw)` is even. The second summand in (13) is therefore zero modulo g.
Since `gcd(u,g)=1`, (13) is equivalent to `Q(w)=0 mod g`.
Conversely, the latter congruence first forces w even, and the same
calculation proves (13). This proves the equivalence in both directions
at every dyadic exponent; it does not complete the square by dividing by
two modulo an even modulus.

Sections 4 and 5 prove the claimed bijection and the full fixed-set
statement. In particular, all relevant base coordinates have denominator
dividing g, even though the entire even-n horizontal return module has
exponent `5g`.

## 6. Evaluation of the norm-congruence count

CRT identifies `Q=0 mod g` with the product of `Q=0 mod p^e` conditions.
These elementary local counts are standard norm-congruence arithmetic;
the proof below is included so the dynamical result has no unchecked
finite-quadratic-module hypothesis.

For `p=2`, or for an odd prime p with `(5/p)=-1`, the reduction of Q
vanishes only at `(0,0)`. If `a=min(v_p(x),v_p(y))`, then
`v_p(Q(x,y))=2a`: after division by `p^a`, the vector is nonzero modulo p
and the reduced form is nonzero. Thus `Q=0 mod p^e` is equivalent to both
coordinates being divisible by `p^ceil(e/2)`. There are exactly
`p^(2 floor(e/2))` such pairs.

For odd `p!=5` with `(5/p)=+1`, the two distinct roots of
`T^2-T-1` modulo p lift uniquely to roots `a,b mod p^e`. This follows
successively by solving one linear congruence for each next digit, since
the derivative is a unit. The map
`(x,y)->(x-a y,x-b y)` is invertible modulo `p^e`; Q becomes the product
of those two coordinates. For a first coordinate of valuation `j<e`,
there are `p^(e-j)-p^(e-j-1)` choices and `p^j` choices of the second
coordinate annihilating it. A zero first coordinate allows all `p^e`
second coordinates. Summing gives
`p^e+e(p^e-p^(e-1))`, as in (1).

For p=5, the invertible coordinate change `a=2x-y`, `b=y` gives
`4Q=a^2-5b^2`. The two terms, if nonzero, have valuations of different
parity, so no lowest-valuation cancellation is possible. Divisibility by
`5^e` is therefore equivalent to
`5^ceil(e/2)|a` and `5^floor(e/2)|b`. These give exactly `5^e` residue
pairs. This completes the proof of (1).

## 7. Least periods, inherited sentinels, and limits

The fixed fibres for divisors of n are literal subsets of the same compact
manifold. Membership is independent of the central coordinate by (5).
Therefore every point of any one fibre has the same set of return times.
The elementary divisor decomposition of fixed points proves (2) and its
Möbius count. No isolated-orbit interpretation is used.

The cheap handwritten checks frozen in advance are:

| n | g_n | Evaluated R(g_n) | Inherited C151/C156 value |
| --- | --- | --- | --- |
| 2 | 1 | 1 | 1 |
| 3 | 4 | 4 | 4 |
| 10 | 55 | `R_5(1) R_11(1)=5*21=105` | 105 |
| 12 | 144 | `R_2(4) R_3(2)=16*9=144` | 144 |

These are consequences of the proof checked against already existing
sentinels, not fresh executions or evidence for an infinite extrapolation.
The index-five and dyadic steps are separately proved in Sections 4-5.

The theorem closes the exact original all-n fixed-fibre count and
classification. It does not furnish an ordinary trace formula, a zeta
continuation theorem, a new general Gauss-sum theory, or isolated periodic
orbits. The existing clean-family/stability obstruction survives unchanged.
The new discriminant-five norm interpretation is source-internal integral
arithmetic; its CRT product is not relabelled an Euler product or target
arithmetic datum. No independent-paper admission is asserted by this proof.
