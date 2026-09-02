# P166 Round-4 exact scout

Verdict: **KILL_ALL**  
Lifecycle: **HOLD_EXTERNAL**  
Verifier: `verify_scout.py`; the checked-in transcript is `CANONICAL.txt`.

The threshold was two closed theorem axes after complete owner and internal
proof-silhouette subtraction.  A pretty identity or a bounded experimental
pattern was not enough.

## 1. GDI: residue gcd-increment

For `m>=1`, let

```text
C_m(x) = x + gcd(x,m) (mod m),   x in Z/mZ,
```

with `gcd(0,m)=m`.  Put

```text
a(m) = sum_{p^e || m} e(p-1),   a(1)=0.
```

The exact probe verifies all residues through `m=180` and the following
all-parameter spine.

- `gcd(C_m(x),m)` is a multiple of `gcd(x,m)`.  If `d=gcd(x,m)`, division by
  `d` semiconjugates the remaining orbit to the same map modulo `m/d`.
- Zero is the unique recurrent point and every orbit reaches it.
- The global height is exactly `a(m)`, attained by `x=1`.  If `p` is the
  least prime factor, the orbit of `1` makes `p-1` steps before division by
  `p`, giving `a(m)=p-1+a(m/p)`.  An arbitrary unit hits a nonunit in at most
  `p-1` steps; a nonunit starts in a proper divisor quotient.  Induction gives
  the matching upper bound.
- For a target represented by `0<=y<m`, its complete one-step fibre is

  ```text
  C_m^{-1}(y) = { y-d mod m : d|m, d|y,
                  gcd(y/d-1,m/d)=1 }.
  ```

  For `y=0`, every divisor `d|m` is allowed.

Thus the mathematics clears the two-axis gate.  It fails the owner gate:
the literal map and the orbit question were posted publicly in June 2026,
and OEIS A059975 now explicitly records both the iteration interpretation and
the same height formula.  This is a decisive direct-owner kill, not merely a
crowded-neighborhood warning.

## 2. CSP: centralizer-size power on permutations

For `pi in S_n`, set

```text
P(pi) = pi^{z(lambda(pi))},
z(lambda)=product_i i^{m_i} m_i!,
```

where `m_i` is the number of `i`-cycles.  The state dependence is illusory:
every cycle length occurring in `pi` divides `z(lambda)`, hence `P(pi)=id`.
The exhaustive check through `S_8` confirms a single image point, one fixed
state, and depth one for every other state.

There is no second axis: the identity fibre has size `n!` and every other
fibre is empty.  General finite-group power maps are already a mature direct
literature, and P102/P154 consume the internal group/power-map neighborhood.
This is killed before any attempt to decorate it.

## 3. POC: parity outer-product correction

Let `A in F_2^{m x n}`, let `r=A 1_n` and `c=A^T 1_m`, and define

```text
Phi(A)=A+r c^T.
```

This was the strongest un-subtracted signal.  If `s=1^T A 1`, direct margin
calculation gives

```text
r(Phi(A))=(1+s)r,   c(Phi(A))=(1+s)c.
```

Consequently:

- the image and recurrent set are the even-total matrices, of size
  `2^{mn-1}`;
- an odd-total source has exact depth one and lands in the balanced subspace
  `r=c=0`;
- on the even-total hyperplane the margins are invariant and `Phi^2=id`;
- the fixed-point count is

  ```text
  2^{m(n-1)} + 2^{(m-1)n} - 2^{(m-1)(n-1)};
  ```

- for every `t>=1` and target `B`, the time-`t` fibre size is zero if `B` has
  odd total, is `1+2^{m+n-2}` if `B` is balanced, and is one otherwise;
  for a nonbalanced recurrent target, the unique source alternates with the
  parity of `t`;
- there are `2^{(m-1)(n-1)}` balanced targets;
- the carrier size recovers `mn`, while the largest positive fibre recovers
  `m+n`; together they recover the unordered pair `{m,n}`.

The verifier exhausts boxes through `4 x 4` and checks fibres for times
`1,2,3,4`.  This is not retained.  P127 already uses binary matrix margins,
a parity-defined image hyperplane, rank-one feedback, tail-one collapse,
small recurrent periods, and a `0/1/large` target-fibre law.  Rectangularizing
and removing the transpose simplifies that engine; it does not create an
independent proof silhouette.

## 4. CTC: a transpose self-commutator

For `A=[[a,b],[c,d]] in M_2(F_q)`, define

```text
K(A)=AA^T-A^T A.
```

Every output is symmetric, so `K^2=0`.  In odd characteristic, write
`u=c-b`, `v=c+b`, `w=a-d`.  Then

```text
K(A) = [[-uv, uw], [uw, uv]].
```

Therefore the image is every traceless symmetric matrix.  Each nonzero
target has `q(q-1)` sources and zero has
`q^3+q(q-1)` sources.  The depth census is

```text
depth 0: 1;
depth 1: q^3+q(q-1)-1;
depth 2: q(q-1)(q^2-1).
```

In characteristic two, putting `r=b+c` gives diagonal `r^2` and off-diagonal
`(a+d)r`.  The image is zero together with

```text
[[x,y],[y,x]],  x != 0.
```

Every nonzero image target has `q^2` sources, zero has `q^3`, and the depth
layers are `1`, `q^3-1`, `q^3(q-1)`.  The verifier treats genuine `F_4`, not
integers modulo four, as well as `F_2,F_3,F_5,F_7`.

The target-rank decoration is also elementary.  For odd `q`, nonzero
rank-one image points exist precisely on the two isotropic lines of
`x^2+y^2` when `-1` is a square, giving `2(q-1)` of them; otherwise there are
none.  In characteristic two the image contains `q-1` rank-one and
`(q-1)^2` rank-two targets.

No exact finite-field dynamical owner was located in the bounded search, but
the input operation is the classical transpose self-commutator measuring
failure of normality.  After subtracting that identity, the whole paper is a
two-variable quadratic parametrization followed by the generic fact that a
symmetric output has zero self-commutator.  Its depth-two/quadratic-fibre
profile is crowded internally by P103, P125, P127 and P161.  The rank spectrum
is not a logically independent dynamical axis.  **KILL_THEOREM_THIN_COLLISION.**

## 5. DPS: odd-degree Seidel feedback

For a simple graph `G` on `[n]`, let `S(G)` be its even-cardinality set of
odd-degree vertices, and Seidel-switch every edge of the cut
`S(G) | ([n]\S(G))`.

- If `n` is odd, vertices of `S(G)` change degree parity and all other
  vertices do not.  Hence one step lands in the Eulerian graphs and then
  fixes.  There are `2^{binom(n,2)-n+1}` fixed targets, and each has exactly
  `2^{n-1}` preimages, indexed by even subsets `S`.
- If `n` is even, the odd set is invariant and the map is an involution.  Its
  fixed graphs have all degrees even or all degrees odd, a total of
  `2^{binom(n,2)-n+2}`.  Every target fibre is a singleton.

The formulas include `n=1,2` and are exhausted through `n=6`.  Seidel
switching is classical, and the equality between switching-class counts and
Eulerian-graph counts is explicitly classical.  More importantly for this
sequence, parity margin elimination and a parity-dependent projection or
involution are again the P127 engine.  **KILL_CLASSICAL_PLUS_P127.**

## 6. HOP: boundary-to-triangle hypergraph operator

For a 3-graph `H`, take its mod-two pair boundary `partial H`, then let
`Theta(H)` contain exactly the triples whose three pairs all occur in
`partial H`.  The first step factors as

```text
C_3 --partial--> Eulerian graphs --Tri--> C_3.
```

The boundary image has dimension `binom(n-1,2)` and every boundary graph has
`2^{binom(n-1,3)}` lifts.  Thus for every target 3-graph `K`,

```text
|Theta^{-1}(K)| = 2^{binom(n-1,3)}
                  * #{Eulerian g : Tri(g)=K}.
```

On the quotient, the graph update is

```text
F(g)=partial Tri(g),
F(A)_{ij}=A_{ij}(A^2)_{ij} over F_2.
```

Exact quotient enumeration through `n=7` found only fixed recurrent points
and maximum tail two, but the image/fixed sequences already branch sharply:

| `n` | Eulerian graphs | distinct `Tri(g)` | `|im F|` | fixed `g` | max tail |
|---:|---:|---:|---:|---:|---:|
| 3 | 2 | 2 | 2 | 2 | 0 |
| 4 | 8 | 5 | 5 | 5 | 1 |
| 5 | 64 | 37 | 37 | 37 | 1 |
| 6 | 1,024 | 562 | 292 | 187 | 2 |
| 7 | 32,768 | 18,296 | 4,856 | 3,719 | 2 |

The displayed fibre identity merely transfers the hard work to the
target-specific triangle-realization multiplicity.  No all-parameter clock,
image characterization, or evaluated every-target atlas emerged.  Small
tail two is not extrapolated.  **KILL_NO_CLOSED_SPINE.**

## 7. CTR: center-directed marked-root transport

A state is a labelled unrooted tree `T` with a marked vertex `r`; the tree is
held fixed.  Move `r` one edge toward the center.  At a unique center it is
fixed; at a bicenter the two central vertices swap.

For the fixed carrier tree, the transient depth is exactly
`dist(r,C(T))`.  The recurrent period is one for a unique center and two for
a bicenter.  Across all `n`-vertex trees the sharp height is
`floor((n-1)/2)`, attained by a path.  Every time-target root fibre can be
written exactly:

- for noncentral `y`, it consists of descendants `x` on the same center ray
  with `dist(x,C)=dist(y,C)+t`;
- for a unique center `c`, it consists of all `x` with `dist(x,c)<=t`;
- for a bicenter target, take all roots reaching the central edge by time
  `t` and retain the parity class determined by the residual swaps.

All labelled trees through `n=7` are generated independently by Prüfer words.
The result is nevertheless marker navigation on a static metric tree: the
clock and fibres are two readings of the same unique-path fact.  Jordan's
one-or-two-center theorem is classical, while P151 already uses a moving
marker/first-passage interface on finite trees.  It is not P148 contraction,
but it has no independent deformation axis.  **KILL_STATIC_MARKER_NAVIGATION.**

## Final gate

| requirement | outcome |
|---|---|
| at least five systems | 7 tested literally |
| at least four carrier classes | 7: residues, permutations/groups, matrices (two different maps), graphs, hypergraphs, marked trees |
| early exact signal | present in GDI, POC, CTC, DPS, CTR; HOP bounded signal; CSP immediate collapse |
| two axes after source subtraction | none |
| direct-owner gate | GDI fails decisively; DPS/CTR classical; CTC classical input identity |
| P1--P165 silhouette gate | POC/DPS fail P127; CTC and CTR remain too internally crowded/thin |

**ROUND4 = KILL_ALL.**  No paper was created and no candidate should be
promoted from this directory.

