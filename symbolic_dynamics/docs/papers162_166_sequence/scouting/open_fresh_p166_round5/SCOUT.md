# P166 Round-5 sparse-carrier scout

Decision: **KILL_ALL**  
Lifecycle: **HOLD_EXTERNAL**  
Exact evidence: `verify_scout.py` and byte-frozen `CANONICAL.txt`.

## Gate and scope

Seven systems were implemented before judgment.  They cover Boolean
functions, finite topological spaces, pointed quiver representations,
combinatorial designs, finite impartial-game states, signed set systems, and
Latin squares.  None is a Round-1--4 variant or one of CTC/POC/GDI.  Ordinary
linear CA, Jordan/image/radical powers, generic closure/peeling, dual-only
actions and standard selectors were not eligible for promotion.

## 1. XCT: XOR-centroid translation of a Boolean support

Let `V=F_2^n`, `q=2^n`, and identify a Boolean function with its support
`S subset V`.  Define

```text
h(S)=sum_{x in S} x,            T(S)=S+h(S).
```

The literal system has an unusually clean raw package.  For any `a in V`,

```text
h(S+a)=h(S)+(|S| mod 2)a.
```

Taking `a=h(S)` proves:

- on even-cardinality supports, `h` is invariant and `T^2(S)=S`;
- an odd support maps in one step to an odd support with centroid zero, which
  is fixed;
- an even support is fixed precisely when `h(S)=0` or when
  `S+h(S)=S`.

For `n>=1` put `M=2^{q-n-1}`.  The linear statistic
`S -> (|S| mod 2,h(S))` has rank `n+1`, so each parity-centroid class has
size `M`.  For a fixed nonzero `a`, an `a`-invariant set is a union of the
`q/2` translation pairs.  Its centroid is `a` precisely when an odd number
of pairs is chosen.  Therefore the full functional-graph census is

```text
fixed points = 2^{q-n} + (q-1)2^{q/2-1},
tail-one points = (q-1)2^{q-n-1},
period-two points = (q-1)(2^{q-n-1}-2^{q/2-1}).
```

The last expression vanishes at `n=1,2`.  At `n=0`, both Boolean functions
are fixed.

Every target fibre is explicit.  If `B` is even, its unique source is
`B+h(B)`.  If `B` is odd with `h(B)=0`, its sources are all `q` distinct
translates `B+v`; an odd set has trivial translation stabilizer.  An odd
target with nonzero centroid has no source.  The same cardinalities hold at
every time `t>=1`.  Hence

```text
|im T| = 2^{q-1}+2^{q-n-1}.
```

There is also a weight-resolved phase census.  Let

```text
beta_k = 0                                      if k is odd,
         (-1)^{k/2} binom(q/2,k/2)             if k is even.
```

Then the number of `k`-subsets with centroid zero is

```text
[binom(q,k)+(q-1)beta_k]/q,
```

while the number with any specified nonzero centroid is

```text
[binom(q,k)-beta_k]/q.
```

This follows from the additive-character product: a nontrivial character
contributes `(1-z^2)^{q/2}`.

The verifier exhausts the entire Boolean-function phase through `n=4`, or
65,536 states at the largest rank, including every target and times one to
three.

### Why XCT is still killed

The weight-centroid formula is an instance of the already-owned enumeration
of fixed-cardinality subset sums in finite abelian groups.  After subtracting
it, the inverse proof and exceptional fixed census both use translation
orbits and target stabilizers.  P162's central second axis is exactly an
arbitrary-target translation-stabilizer fibre polynomial plus recovery.  XCT
has different forward dynamics—deterministic action rather than stochastic
intersection—but its purported independent inverse/census engine is not
independent inside this portfolio.  Keeping only the short order-two/order-one
temporal identity is below threshold.  **KILL_INTERNAL_P162.**

## 2. BND: finite-topology boundary iteration

For a finite topological space `(X,tau)` and `A subset X`, set

```text
D(A)=cl(A) intersect cl(X\A).
```

Write `F=D(A)`.  It is closed.  Then

```text
D(F)=F\int(F).
```

This set is closed and has empty interior: any open subset contained in it
would also be an open subset of `F`, contradicting its disjointness from
`int(F)`.  Thus

```text
D^3=D^2
```

on every topological space.  All recurrent states are fixed and the maximum
possible transient depth is two.

The verifier independently constructs every labelled topology on `n<=4`
points (`1,1,4,29,355`) and all marked subsets.  At `n=4` the 5,680 marked
states split into 1,175 fixed, 3,831 depth-one and 674 depth-two states.  The
largest one-step target fibre is 16, but positive fibre sizes vary across all
even values from 2 to 16.

The universal temporal statement is a standard identity for the topological
boundary operator, already sitting inside the boundary-extended Kuratowski
operator monoid.  No topology-uniform image criterion or target-fibre count
emerged; enumerating labelled finite topologies is static background.
**KILL_DIRECT_OPERATOR_NO_ATLAS.**

## 3. ZAT: zero-triggered arrow transport

Fix a one-arrow quiver representation `A:U->V` over `F_q`.  A state is a
marked pair `(u,v)`, and

```text
T_A(u,v) = (u,Au)  if v=0 and Au!=0,
           (u,v)   otherwise.
```

This is idempotent.  If `rank(A)=r`, its fixed/image count is

```text
q^dim(U)(q^dim(V)-1)+q^{dim(U)-r},
```

and it has `q^dim(U)-q^{dim(U)-r}` depth-one states.  For a target `(u,v)`,
the fibre size is

```text
0,  if v=0 and Au!=0;
1,  if v=0 and Au=0, or v!=0 and v!=Au;
2,  if v=Au!=0.
```

The verifier includes zero-dimensional endpoints and all maps in several
`F_2/F_3` boxes.  Nothing here uses quiver representation theory beyond the
presence of one linear arrow: it is a guarded assignment and one-step
projection.  Decorating the census by rank does not create a second temporal
axis.  **KILL_GUARDED_PROJECTION.**

## 4. EOD: exact-one feedback on a complement design

On `[v]`, take the symmetric design whose block at `x` is
`B_x=[v]\{x}`.  For a current point set `S`, activate `x` exactly when
`|B_x intersect S|=1`.  The definition reduces literally to

```text
T(S) = [v]\S,  if |S|=1;
       S,       if |S|=2;
       empty,   otherwise.
```

For `v>=4`, empty and all 2-subsets are fixed, every singleton has exact
depth two, and all sets of size at least three have depth one.  The image is
empty, the `v` co-singletons, and the `binom(v,2)` two-subsets.  The empty
fibre has size

```text
2^v-v-binom(v,2),
```

and every other image target has a unique source.  At `v=3`, every 2-subset
has its singleton complement as a second source; at `v=2`, the two singletons
form a 2-cycle.

The design contributes no nontrivial incidence geometry: all results are
cardinality thresholding on the complement of a singleton.  This is a thin
exact-one Boolean network adjacent to P80/P106/P118.  **KILL_THRESHOLD_REDUCTION.**

## 5. NIM: canonical capped two-pile move

On positions `(a,b)` with `0<=a,b<=N`, fix equal piles and otherwise reduce
the larger pile to the smaller:

```text
T(a,b)=(min(a,b),min(a,b)).
```

The fixed/image set is the `N+1` diagonal positions.  Every off-diagonal
position has depth one, and

```text
|T^{-1}(k,k)|=2(N-k)+1.
```

This is the literal winning move for two-pile normal-play Nim and a one-step
optimal-policy projection.  The fibre census is not an independent game
theorem.  **KILL_DIRECT_BOUTON.**

## 6. GSR: global-sign reorientation

On signed subsets `s in {-1,0,1}^n`, let `p(s)` be the product of the nonzero
signs, with empty product `+1`, and set `R(s)=p(s)s`.

- `p=+1` gives a fixed state.
- If `p=-1` and the support has odd size, one global reversal makes the
  product positive, so the state has depth one.
- If `p=-1` and the support has even size, global reversal preserves the
  negative product and gives a 2-cycle.

Consequently

```text
fixed = (3^n+1)/2,
tail one = (3^n-(-1)^n)/4,
period-two points = (3^n+(-1)^n-2)/4.
```

For every `t>=1`, an even-support target has fibre one; an odd-support target
has fibre two when its sign product is positive and zero otherwise.  Exact
enumeration runs through `n=9`.

Global sign reversal and reorientation are native oriented-matroid/signed-set
symmetries.  The feedback only chooses whether to apply one central
involution, so temporal and inverse statements are the same two-orbit
calculation.  The full signed cube was also used by the earlier OZP scout,
though its update was different.  **KILL_CENTRAL_ACTION_THIN.**

## 7. DLR: diagonal row feedback on Latin squares

For a labelled Latin square `L`, let `d_i=L(i,i)`.  If `d` is a permutation,
set

```text
T(L)(i,j)=L(d_i,j);
```

otherwise hold.  Row permutation preserves Latinness.  Complete enumeration
of orders one through four gives:

| order | squares | permutation diagonals | image | functional shapes |
|---:|---:|---:|---:|---|
| 1 | 1 | 1 | 1 | one fixed |
| 2 | 2 | 0 | 2 | two fixed |
| 3 | 12 | 6 | 7 | 7 fixed, 5 depth-one |
| 4 | 576 | 48 | 536 | 530 fixed, 40 depth-one, 6 period-three |

The order-four 3-cycle is a real early anomaly, but it does not stabilize into
an all-order temporal theorem; target fibres already take sizes 1, 3 and 5.
The update is a state-dependent row isotopism, in a literature with mature
isotopism and autotopism cycle theory.  Without a scalable spine, a bounded
3-cycle is not promotable.  **KILL_NO_SPINE.**

## Aggregate gate

| requirement | outcome |
|---|---|
| at least six literal systems | 7 |
| six distinct carrier classes | 7 |
| small-box functional graph and target fibres | completed for every row |
| all-parameter temporal plus independent inverse/image/census | XCT only before subtraction |
| direct/static owner subtraction | XCT weight census, BND boundary, NIM strategy, GSR reorientation subtracted |
| P1--P165 collision subtraction | XCT fails P162; EOD and GSR also enter occupied Boolean/action silhouettes |

Final decision: **ROUND5 = KILL_ALL**.  No paper or theorem contract should be
created from this lane.

