# C147 proof package

## Claim and status

**Status: PROVABLE AS STATED WITH SCOPED MEASURE.**  Positive coprime square-
billiard directions own the asserted primitive lengths and clean transverse
families; the exact finite ledger, first symmetry-inequivalent length
collision, irrational-aspect control, stability obstruction, and natural
Dirichlet quantization follow.  Positive length refers to the transverse
slice, not Liouville measure in the full energy shell.

## Frozen notation

Let `Q=[0,1]^2` and fix unit speed.  Reflecting `Q` across its sides unfolds a
regular billiard trajectory to a straight line.  A positive `(m,n)` is an
absolute-direction representative: it owns four signed unfolded sectors and
two sectors after pairing by time reversal.  Coordinate swap remains a tagged
square symmetry, and the two time-reversal-quotiented axis families are
separate.  For `m,n>0`, put

```text
v_(m,n)=(2m,2n),       L_(m,n)=2 sqrt(m^2+n^2).
```

## Dependency map

1. Primitive classification uses the translation lattice `(2Z)^2`.
2. Clean families use transverse offsets in the doubled torus.
3. Stability singularity uses the fixed-family tangent eigenvector in the full
   reduced Poincare linearization.
4. Counting uses gcd enumeration and Möbius inversion.
5. Collision minimality uses symmetry-reduced exact enumeration.
6. Aspect control uses rational independence of `1,sqrt(2)`.
7. A4 uses the intrinsic Dirichlet half-wave, without a clean-family trace or
   target matching.

## Theorem 1: primitive unfolding and length

For every `m,n>0`, a regular trajectory in direction `(m,n)` returns with its
position and velocity after unfolded displacement `(2m,2n)` and has length
`L_(m,n)`.  The family is primitive exactly when `gcd(m,n)=1`.

**Proof.**  In each coordinate, folding a straight line back into `[0,1]`
identifies positions modulo two and records velocity by the parity of the
unit-cell reflection.  Thus return of both position and oriented velocity
requires an even-integer displacement in both coordinates.  At unit speed,
the translation `(2m,2n)` has Euclidean length
`2 sqrt(m^2+n^2)`.  If `d=gcd(m,n)>1`, translation `(2m/d,2n/d)` gives a
shorter oriented return.  Conversely, a shorter oriented return would be
`(2a,2b)` with `(m,n)=k(a,b)` for an integer `k>1`, contradicting coprimality.
Vertex-hitting offsets are excluded, so every reflection is regular. ∎

During this period the line crosses `2m` vertical and `2n` horizontal sides.
The total number of reflections is `2(m+n)`.  Hence the product of Dirichlet
reflection signs is `(-1)^(2(m+n))=+1`.

## Theorem 2: clean transverse cylinders and singular stability

For each primitive direction, regular periodic trajectories form a clean
one-dimensional family.  A transverse circle parametrizes parallel orbits;
removing the finitely many offsets whose lines meet unfolded lattice vertices
decomposes it into open cylinders.  Each cylinder has positive transverse
length.  The direction is fixed, so this subset has zero Liouville measure in
the full energy shell.

Let `P_gamma` denote the full reduced Poincare return on a smooth local section
inside the fixed unit-energy shell.  Put `e=w/L` along the primitive unfolded
vector and let `e_perp` be its quarter turn.  In local section coordinates,
`s` is displacement along `e_perp` and `theta` is angular deviation from `e`.
The time to advance one primitive longitudinal length is `L/cos(theta)`, so

```text
P_gamma(s,theta)=(s+L tan(theta),theta),
DP_gamma(s,0)=[[1,L],[0,1]].
```

Because `L>0`, `ker(I-DP_gamma)=span(partial_s)`, exactly the tangent to the
fixed-family curve.  Therefore

```text
det(I-DP_gamma)=0.                               (1)
```

**Proof.**  On the doubled torus, parallel rational lines of a fixed slope are
closed and their quotient by translation along the flow is a circle.
Only finitely many quotient offsets pass through a torus image of a square
vertex.  On each complementary interval, unfolding and folding vary smoothly
and preserve the offset after the primitive translation.  The displayed local
calculation then proves both the fixed-curve identity and the clean kernel
equality, hence (1), without replacing the full Poincare linearization by a
scalar.  Since a single direction has angular measure zero, the ambient
measure statement follows. ∎

## Proposition 3: exact direction count

For `1<=m,n<=M`, the number of ordered positive primitive directions is

```text
C(M)=sum_(d=1)^M mu(d) floor(M/d)^2.             (2)
```

At `M=40`, `C(40)=979`.  These representatives own 3,916 signed oriented
sectors, or 1,958 after pairing by time reversal; the two unoriented axis
boundary classes remain separate.

**Proof.**  The indicator of coprimality is
`1_(gcd(m,n)=1)=sum_(d|m,d|n) mu(d)`.  Summing over the square and exchanging
the finite sums gives (2).  Exact integer evaluation gives 979. ∎

## Proposition 4: first inequivalent square collision

After quotienting coordinate swap, the smallest positive integer represented
by two distinct primitive direction classes is

```text
65=1^2+8^2=4^2+7^2.                              (3)
```

Thus `(1,8)` and `(4,7)` have common length `2 sqrt(65)` but are not related
by time reversal or coordinate swap.

**Proof.**  Both pairs are coprime and satisfy (3).  The producer enumerates
every positive pair in increasing `m^2+n^2` and canonicalizes by sorting the
two coordinates.  The independent checker reconstructs all representation
sets for squares `1,...,64` and verifies that each has at most one primitive
canonical representative.  If `m^2+n^2<65`, then each positive coordinate is
at most eight, so the cutoff 40 contains every unrestricted positive-integer
candidate in that range.  This is therefore an exact global proof of
minimality, not a cutoff-relative assertion. ∎

## Proposition 5: irrational-aspect collision control

For the rectangle of width one and height `alpha=2^(1/4)`, distinct positive
ordered directions never have the same length.

**Proof.**  Squared lengths divided by four are
`m^2+sqrt(2)n^2`.  Equality for `(m,n)` and `(m',n')` gives

```text
(m^2-m'^2)+sqrt(2)(n^2-n'^2)=0.
```

The two coefficients are rational and `sqrt(2)` is irrational, so both vanish.
Positivity gives `m=m'` and `n=n'`. ∎

## Natural quantization and boundary

Let `-Delta_D` be the Dirichlet Laplacian with domain
`H^2(Q) intersect H_0^1(Q)`, and put `H_D=sqrt(-Delta_D)` on the form domain
`H_0^1(Q)`.  The half-wave group `exp(-itH_D)` is unitary on `L^2(Q)` and has
principal symbol `|p|`, hence the same unit-speed length clock on `|p|=1`.
Complex conjugation `K` is antiunitary, `K^2=I`, and
`K exp(-itH_D) K=exp(itH_D)`.  Dirichlet reflection contributes phase `-1`
per regular bounce, agreeing with the `+1` total phase over `2(m+n)` bounces.
This intrinsic integrable construction supports `A4_NATURAL_QUANTIZATION`.
C147 does not claim that it repairs (1), supplies a clean-family trace formula,
or matches any target data or analytic structure.

The strict tuple is
`(A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`.  No target divisor,
functional equation, counting law, prime-like map, arithmetic/local datum,
Euler factor, root number, automorphy claim, Hilbert--Polya construction, or
Route-B authorization is present.
