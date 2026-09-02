# Replacement geometry/mechanism breadth scout

## Freeze and outcome

- Scope: Stage-1 breadth only.  No manuscript and no paper number is assigned.
- Portfolio boundary: P1--P156.
- External state: **HOLD_EXTERNAL**.  This audit authorizes no posting,
  circulation, submission, author contact, or priority claim.
- Mechanism firewall: no finite-linear/stable-image engine, cyclic
  substitution, valuation/GCD system, selector/extraction process, tree or
  graph pruning, partition refinement, random intersection, rectangle-product
  process, generic closure, or generic power map was retained.
- Exact computation is bounded counterexample pressure, not an all-parameter
  proof and not ownership evidence.

Sixteen literal finite self-maps survived long enough to be enumerated.  Two
merit a focused theorem-and-owner gate:

1. **`BST`**, the binary-projective Steiner triangle collapse, has a four-way
   pointwise partition, a sharp rank boundary, a fixed-plus-three-cycle core,
   and a nonuniform every-target fibre theorem.
2. **`ORT`**, the orthocenter sliding window over `F_p^2` for `p=3 mod 4`, has
   a sharp depth-two singular boundary, a fixed-plus-four-cycle core, and an
   exact codomain-wide `0/1/(1+2R)` fibre law.

The initially attractive standard-Cremona totalization `CRE` is killed rather
than held as a reserve: its dominant involution/base-locus argument is
classical and its portfolio proof silhouette collides substantively with P103
and P150.  The other thirteen candidates are killed by direct ownership,
forbidden generic machinery, or a theorem package too thin to justify a
focused stage.

The companion verifier covers 40 parameter boxes and **575,833 exact
assertions**.  Its frozen transcript is `CANONICAL.txt`.

## Ranked ledger

| rank | handle | carrier / literal map | strongest early signal | decision |
|---:|---|---|---|---|
| 1 | `BST` | ordered triples of points of `PG(r-1,2)`; replace each vertex by the Steiner product of the other two | rank 2 is entirely periodic, while rank at least 3 has a one-step nonblock shell and block fibres of size `2^r-3` | **`SELECT_FOCUSED`** |
| 2 | `ORT` | ordered noncollinear affine triangles over `F_p^2`, plus a sink; slide the window through the orthocenter | `p=3` has no four-cycle core at all, whereas every `p>=7`, `p=3 mod 4`, has a large exact four-cycle core and three oriented right-angle shells | **`SELECT_FOCUSED_OWNER_AMBER`** |
| 3 | `CRE` | projective space plus a sink; totalized standard Cremona reciprocal | support strata give depths `0/1/2` and explicit exceptional fibres | **`KILL_DIRECT_OWNER_AND_P103`** |
| 4 | `REF` | ordered pairs on an anisotropic finite conic; specular recurrence | complete divisor-indexed cycle census | **`KILL_CIRCLE_BILLIARD_OWNER_THIN`** |
| 5 | `QIV` | affine vectors plus a sink; quadratic-form inversion | isotropic cone is exactly the Garden-of-Eden/sink stratum | **`KILL_CLASSICAL_INVERSION`** |
| 6 | `HUR` | ordered transposition pairs; one Hurwitz move | support union `2/3/4` gives exact periods `1/3/2` | **`KILL_LITERAL_HURWITZ_OWNER`** |
| 7 | `HAR` | anchored triples on `P^1`; replace the third point by its harmonic conjugate | fixed-point-free involution for every odd characteristic | **`KILL_CLASSICAL_INVOLUTION`** |
| 8 | `POL` | point--line pairs under a fixed polarity; exchange the two polar representatives | only fixed points and transpositions | **`KILL_COORDINATE_SWAP_THIN`** |
| 9 | `VIE` | `F_p^3`; one Vieta mutation | exactly `p^2` fixed points and all other points in 2-cycles | **`KILL_CLASSICAL_VIETA_INVOLUTION`** |
| 10 | `SFW` | directed facets of a simplex; shift and append the missing vertex | every orbit has exact length `d+1` | **`KILL_RELABELLED_ROTATION`** |
| 11 | `UAW` | unary automata with a retained transition table and moving pointer | full joint tail/period formula | **`KILL_GENERIC_FUNCTIONAL_GRAPH`** |
| 12 | `RCW` | rooted permutations; conjugate by the root--image transposition and move the root | a nonlinear-looking rule is globally an involution | **`KILL_SHALLOW_CONJUGATION`** |
| 13 | `SYT` | two-row standard Young tableaux; Schuetzenberger promotion | Catalan carrier with mixed orbit lengths and global order `2n` | **`KILL_PROMOTION_OWNER`** |
| 14 | `CUB` | boxed plane partitions; complement and rotate by 180 degrees | fixed locus is the self-complementary class | **`KILL_PLANE_PARTITION_OWNER`** |
| 15 | `PDU` | ordered projective triangles; take the three opposite-side polars | involution on every nondegenerate triangle | **`KILL_ADJUGATE_P103`** |
| 16 | `GFR` | group-labelled oriented faces with product one; cyclically rotate labels | fixed count is the number of cube roots of the identity | **`KILL_ROTATION_POWER_THIN`** |

## System records

### `BST` -- binary-projective Steiner triangle collapse

- **Carrier.**  Let `V=F_2^r`, `r>=2`, `P=V\{0}`, and `N=|P|=2^r-1`.
  States are ordered triples in `P^3`.  These are points of
  `PG(r-1,2)` with repetition allowed.
- **Literal update.**  Put `x star x=x` and `x star y=x+y` for `x!=y`;
  this is the Steiner quasigroup operation of the binary projective triple
  system.  Define
  `S(a,b,c)=(b star c,c star a,a star b)`.
- **Small exact signature.**  At ranks `2,3,4`, respectively, the state counts
  are `27,343,3375`, fixed counts are `9,49,225`, and cycle histograms are
  `{1:9,3:6}`, `{1:49,3:42}`, `{1:225,3:210}`.  Rank 2 has maximum tail zero;
  ranks 3 and 4 have maximum tail one.  At rank 3 the indegree histogram is
  `{0:168,1:133,5:42}`.
- **Candidate sharp temporal theorem.**  Diagonal triples and ordered
  three-distinct projective-line blocks are fixed.  Exactly-two-equal triples
  lie in strict 3-cycles.  Every three-distinct nonblock triple maps in one
  step to a fixed block.  Thus the fixed count is `N^2`, there are
  `N(N-1)` strict 3-cycles, the periodic/image size is `4N^2-3N`, and the
  depth-one shell has size `N(N-1)(N-3)`.  The maximum tail is zero at `r=2`
  and one for every `r>=3`.
- **Independent second axis.**  Every diagonal or exactly-two-equal target
  has one preimage; every ordered block target has exactly `N-2=2^r-3`
  preimages; every nonblock target has none.  This is a genuine every-target
  fibre theorem, not a consequence of the temporal census alone.
- **Early anomaly.**  The Fano carrier (`r=3`) is the first rank with
  Garden-of-Eden states: 168 nonblocks disappear after one step and each of
  the 42 ordered-block fixed points has indegree five.  The smaller rank-2
  carrier hides the collapse because every three-distinct triple is a block.
- **Verdict.**  **`SELECT_FOCUSED`**.  The contribution candidate is the
  projective-block collapse plus its target-resolved fibres; the Steiner
  quasigroup and the projective Steiner system themselves receive zero credit.

### `ORT` -- orthocenter sliding window with a singular sink

- **Carrier.**  For a prime `p=3 mod 4`, use every ordered noncollinear
  triangle `(A,B,C)` in the affine plane `F_p^2`, together with a sink `dagger`.
  Orthogonality is defined by the anisotropic form
  `<(x,y),(u,v)>=xu+yv`.
- **Literal update.**  Let `H(A,B,C)` be the orthocenter.  Send
  `(A,B,C)` to `(B,C,H)` when that triple is noncollinear and to `dagger`
  otherwise; fix `dagger`.
- **Small exact signature.**  For `p=3` there are 433 states, only the sink is
  recurrent, the maximum tail is two, and indegrees are
  `{0:288,1:144,289:1}`.  For `p=7` there are 98,785 states, 56,449 recurrent
  states, cycle histogram `{1:1,4:14112}`, maximum tail two, and indegrees
  `{0:28224,1:70560,28225:1}`.
- **Candidate sharp temporal theorem.**  Put
  `T=p^2(p^2-1)(p^2-p)` and
  `R=p^2(p^2-1)(p-1)`.  There are `R` triangles right-angled at each specified
  vertex.  Nonright triangles, numbering
  `Q=T-3R=p^2(p^2-1)(p-1)(p-3)`, form strict 4-cycles.  Right-at-first states
  have depth two, right-at-second and right-at-third states have depth one,
  and the sink is fixed.  Hence `F^2(X)={dagger} union {nonright triangles}`
  is the sharp stable image and the zeta function is
  `(1-z)^(-1)(1-z^4)^(-Q/4)`.
- **Independent second axis.**  The sink has `1+2R` preimages.  A triangle
  right-angled at its first or second listed vertex has no preimage; a triangle
  right-angled at its third vertex or a nonright triangle has exactly one.
  Therefore the one-step image size is `1+T-2R`.  The depth CDF is
  `1+Q`, `1+Q+2R=1+T-R`, and `1+T` at thresholds zero, one, and two.
- **Early anomaly.**  The boundary prime `p=3` annihilates the generic
  four-cycle stratum (`Q=0`) without changing the sharp height two.  This is
  why a single generic-prime pilot would have been misleading.
- **Verdict.**  **`SELECT_FOCUSED_OWNER_AMBER`**.  Orthocentric four-point
  symmetry is classical and receives zero credit.  A focused gate must decide
  whether the finite-field singular boundary, exact oriented depth split, and
  codomain-wide fibre law leave a publishable residual.

### `CRE` -- totalized standard Cremona reciprocal

- **Carrier/update.**  On `P^d(F_p)` plus `dagger`, apply
  `[x_0:...:x_d] -> [prod_{j!=0}x_j:...:prod_{j!=d}x_j]` when the displayed
  vector is nonzero, and send its base locus to `dagger`; fix `dagger`.
- **Small exact signature.**  `(p,d)=(3,3)` has 41 states, nine recurrent,
  maximum tail two, cycles `{1:9}`, and indegrees
  `{0:28,1:8,4:4,17:1}`.
- **Candidate theorem.**  Full support is the torus involution; support `d`
  maps to a coordinate vertex and then the sink; support at most `d-1` maps
  directly to the sink.  The torus has `(p-1)^d` points and
  `gcd(2,p-1)^d` fixed points.
- **Second axis.**  A coordinate vertex has `(p-1)^(d-1)` preimages, a torus
  target one, every other boundary target zero, and the sink
  `1+sum_{s=1}^{d-1} binom(d+1,s)(p-1)^(s-1)`.
- **Anomaly/verdict.**  Dimension two already shows the support-`d` depth-two
  shell, but this is the standard Cremona involution with an artificial sink.
  **`KILL_DIRECT_OWNER_AND_P103`**.

### `REF` -- reflection recurrence on an anisotropic conic

- **Carrier/update.**  For `p=3 mod 4`, let
  `C={u in F_p^2:<u,u>=1}` and send
  `(u,v)` to `(v,2<u,v>v-u)` on `C^2`.
- **Small exact signature.**  `p=7` has 64 states and cycles
  `{1:8,2:4,4:4,8:4}`; every indegree is one.
- **Candidate theorem.**  Since `|C|=p+1`, for each `d|(p+1)` there are
  `phi(d)(p+1)/d` cycles of length `d`; every state is periodic.
- **Second axis/anomaly.**  All fibres are singleton.  The mixed divisor
  census first appears at `p=7`, but it is only circular billiard rotation in
  finite-conic coordinates.
- **Verdict.**  **`KILL_CIRCLE_BILLIARD_OWNER_THIN`**.

### `QIV` -- quadratic inversion with an isotropic sink

- **Carrier/update.**  For `p=1 mod 4`, on `F_p^2 union {dagger}` send
  `v` to `v/<v,v>` when the norm is nonzero and otherwise to `dagger`.
- **Small exact signature.**  `p=5` has 26 states, 17 recurrent, maximum tail
  one, cycles `{1:5,2:6}`, and indegrees `{0:9,1:16,10:1}`.
- **Candidate theorem.**  The `2p-1` norm-zero vectors enter the sink in one
  step; the `(p-1)^2` anisotropic vectors form an involution with `p-1` fixed
  unit vectors.
- **Second axis/anomaly.**  Anisotropic targets have one preimage, isotropic
  targets none, and the sink has `2p` preimages.  Changing from
  `p=3 mod 4` to `p=1 mod 4` creates the two-line singular cone.
- **Verdict.**  **`KILL_CLASSICAL_INVERSION`**.

### `HUR` -- Hurwitz move on transposition pairs

- **Carrier/update.**  On ordered pairs of transpositions of `S_n`, set
  `(a,b)->(b,bab)`.
- **Small exact signature.**  For `n=5`, the 100 states have cycles
  `{1:10,2:15,3:20}` and singleton fibres.
- **Candidate theorem.**  Equal transpositions are fixed, disjoint pairs form
  `3 binom(n,4)` two-cycles, and intersecting pairs form
  `2 binom(n,3)` three-cycles.
- **Second axis/anomaly.**  The map is bijective, so every fibre is singleton;
  the first 2-cycles occur only when four support points are available.
- **Verdict.**  **`KILL_LITERAL_HURWITZ_OWNER`**.

### `HAR` -- harmonic-conjugation involution

- **Carrier/update.**  For odd `p`, use triples `(A,B;X)` of points of
  `P^1(F_p)` with `A!=B` and `X` not an anchor; replace `X` by its harmonic
  conjugate with respect to `(A,B)`.
- **Small exact signature.**  At `p=5`, all 120 states lie in 60 two-cycles.
- **Candidate theorem.**  All `p(p^2-1)` states form a fixed-point-free
  involution.
- **Second axis/anomaly.**  Every target has one preimage; characteristic two
  is a genuine excluded boundary because harmonic conjugation degenerates.
- **Verdict.**  **`KILL_CLASSICAL_INVOLUTION`**.

### `POL` -- projective-polarity exchange

- **Carrier/update.**  Fix a nondegenerate polarity of `PG(2,p)`.  Represent
  a point and a line by their polar coefficient vectors and exchange them.
- **Small exact signature.**  At `p=3`, 169 states split into 13 fixed points
  and 78 two-cycles.
- **Candidate theorem.**  With `M=p^2+p+1`, there are `M` fixed states and
  `(M^2-M)/2` two-cycles.
- **Second axis/anomaly.**  Every fibre is singleton.  The entire mechanism is
  a coordinate swap under an involutive identification.
- **Verdict.**  **`KILL_COORDINATE_SWAP_THIN`**.

### `VIE` -- one-coordinate Vieta mutation

- **Carrier/update.**  For odd `p`, send
  `(x,y,z)` in `F_p^3` to `(x,y,xy-z)`.
- **Small exact signature.**  At `p=5`, 125 states split into 25 fixed points
  and 50 two-cycles.
- **Candidate theorem.**  There are `p^2` fixed points (`2z=xy`) and all
  remaining points form two-cycles.
- **Second axis/anomaly.**  Every fibre is singleton; characteristic two
  collapses the fixed-locus equation and is the only boundary event.
- **Verdict.**  **`KILL_CLASSICAL_VIETA_INVOLUTION`**.

### `SFW` -- directed simplex-facet walk

- **Carrier/update.**  A state is an ordered list of `d` distinct vertices of
  a labelled `d`-simplex.  Delete the first and append the unique missing
  vertex.
- **Small exact signature.**  Dimensions `2,3,4` give respectively
  `2,6,24` cycles, all of lengths `3,4,5`.
- **Candidate theorem.**  Every state has exact period `d+1`, with `d!`
  cycles.
- **Second axis/anomaly.**  Every fibre is singleton; no nontrivial anomaly
  survives the identification with rotation of a cyclic vertex ordering.
- **Verdict.**  **`KILL_RELABELLED_ROTATION`**.

### `UAW` -- unary-automaton execution

- **Carrier/update.**  States are `(f,i)` with `f:[n]->[n]`; retain `f` and
  send the pointer to `f(i)`.
- **Small exact signature.**  At `n=4`, 1,024 states have maximum tail three,
  cycles `{1:256,2:96,3:32,4:6}`, and indegrees
  `{0:324,1:432,2:216,3:48,4:4}`.
- **Candidate theorem.**  The number with tail `t` and eventual period `ell`
  is
  `n (n-1)_(t+ell-1) n^(n-t-ell)` for `0<=t<n` and
  `1<=ell<=n-t`.
- **Second axis/anomaly.**  The fibre of `(f,j)` has size `|f^{-1}(j)|`; over
  the whole carrier the number of targets of indegree `k` is
  `n binom(n,k)(n-1)^(n-k)`.  The maximum tail grows sharply as `n-1`.
- **Verdict.**  **`KILL_GENERIC_FUNCTIONAL_GRAPH`**; the transition table is
  merely carried as a static parameter.

### `RCW` -- rooted-permutation conjugation walker

- **Carrier/update.**  On `S_n x [n]`, let `j=sigma(i)`, let `tau=(i j)`, and
  send `(sigma,i)` to `(tau sigma tau,j)`.
- **Small exact signature.**  At `n=5`, 600 states split into 120 fixed points
  and 240 two-cycles.
- **Candidate theorem.**  The map is an involution; exactly `n!` states are
  fixed.
- **Second axis/anomaly.**  Every fibre is singleton.  The apparently
  nonlinear permutation update disappears after the second iterate.
- **Verdict.**  **`KILL_SHALLOW_CONJUGATION`**.

### `SYT` -- promotion on two-row rectangles

- **Carrier/update.**  Standard Young tableaux of shape `2 x n` under
  Schuetzenberger promotion.
- **Small exact signature.**  For widths `2,3,4,5`, the Catalan carrier sizes
  are `2,5,14,42`, with cycle histograms `{2:1}`, `{2:1,3:1}`,
  `{2:1,4:1,8:1}`, and `{2:1,5:2,10:3}`.
- **Candidate theorem.**  Promotion has global order `2n` for `n>=3`
  (the small widths have orders one and two); fixed powers are controlled by
  the rectangular-tableau cyclic-sieving polynomial.
- **Second axis/anomaly.**  Every fibre is singleton.  Width three is the
  first mixed-orbit carrier.
- **Verdict.**  **`KILL_PROMOTION_OWNER`**; this is a named classical action,
  and the Catalan/hook/cyclic-sieving engine is explicitly occupied.

### `CUB` -- complement-rotate on boxed plane partitions

- **Carrier/update.**  On plane partitions `pi` in an `a x b x c` box, set
  `pi'_(i,j)=c-pi_(a+1-i,b+1-j)`.
- **Small exact signature.**  The `2 x 3 x 2` box has 50 states, six fixed
  points, and 22 two-cycles.
- **Candidate theorem.**  The update is an involution and its fixed set is the
  self-complementary plane partitions, with the classical product counts.
- **Second axis/anomaly.**  Every fibre is singleton; fixed states exist only
  under the familiar box-parity constraint.
- **Verdict.**  **`KILL_PLANE_PARTITION_OWNER`**.

### `PDU` -- polar duality on projective triangles

- **Carrier/update.**  On ordered noncollinear triples `(A,B,C)` of
  `PG(2,p)`, identify each opposite-side covector with its pole under the
  standard polarity and send the triangle to `(B cross C,C cross A,A cross B)`.
- **Small exact signature.**  At `p=3`, 1,404 states split into 24 fixed
  triangles and 690 two-cycles.
- **Candidate theorem.**  The map is an involution on every nondegenerate
  ordered triangle; fixed triangles are precisely the self-polar ordered
  frames.
- **Second axis/anomaly.**  Every fibre is singleton; characteristic two
  changes the self-polar count but not involutivity.
- **Verdict.**  **`KILL_ADJUGATE_P103`**; the cross-product proof is the
  3-by-3 adjugate identity in geometric notation.

### `GFR` -- rotation of a group-labelled oriented face

- **Carrier/update.**  For a finite group `G`, use triples `(a,b,c)` with
  `abc=e` and cyclically rotate them.
- **Small exact signature.**  For `S_3`, 36 states have cycles
  `{1:3,3:11}`.
- **Candidate theorem.**  Fixed states are `(g,g,g)` with `g^3=e`; all other
  states have period three.
- **Second axis/anomaly.**  Every fibre is singleton.  The nonabelian carrier
  changes only the cube-root count, not the dynamics.
- **Verdict.**  **`KILL_ROTATION_POWER_THIN`**.

## Five-interface P1--P156 collision audit

The five interfaces are `(C)` carrier, `(U)` literal update, `(T)` temporal
silhouette, `(F)` target/fibre object, and `(E)` dominant proof engine.  A
carrier resemblance alone is not fatal; an update identity or transferable
`T+F+E` conjunction is.

| handle | C | U | T | F | E / decisive comparison |
|---|---|---|---|---|---|
| `BST` | finite geometry overlaps P67/P81/P153 | no prior pairwise Steiner-triangle update | P153 is shallow but has a `p`-cycle with depth `p`, unlike fixed/3-cycle plus depth one | block incidence fibres are not P153's triangular-polynomial fibres | projective-line equation `a+b+c=0`, not polynomial-triangular conjugacy; survives |
| `ORT` | finite-field plane overlaps P81/P150/P153 | no prior sliding orthocenter window | P150 also has a totalized periodic core and singular trees, but periods/depth strata are `1/4` and `0/1/2` here | orientation-specific right-angle `0/1/sink` fibres differ from P150's denominator fibres | orthocentric quartet plus anisotropic counting, not Lyness/QRT algebra; survives owner-amber |
| `CRE` | projective finite field near P103/P150 | standard Cremona coordinate products are adjugate cofactors | involution plus depth-two base-locus tree matches the occupied adjugate/totalization silhouette | exceptional-coordinate fibres come from support strata | P103 adjugate identity and P150 sink totalization transfer directly; fatal |
| `REF` | orthogonality/conic near P81 | no identical prior rule | pure permutation/rotation, a permanently weak silhouette | all fibres singleton | cyclic parametrization reduces it to circular billiard rotation; fatal owner/thinness |
| `QIV` | finite-field quadratic space near P81/P150 | totalized norm inversion is not P150's Lyness map | involution plus one singular shell is thinner than P150 | `0/1/2p` fibres are a quadratic-cone count | classical inversion supplies the whole engine; fatal |
| `HUR` | symmetric-group carrier near P105/P135/P154/P155 | literal Hurwitz generator is externally named | support types yield only periods 1--3 | all fibres singleton | braid/Hurwitz action owns the update; fatal |
| `HAR` | projective-line carrier has no close occupied paper | literal harmonic conjugation is classical | fixed-point-free involution | all fibres singleton | cross-ratio `-1` gives everything; fatal |
| `POL` | projective incidence near P67/P81/P106 | under polarity it is exactly coordinate exchange | only fixed points/2-cycles | all fibres singleton | involutive identification, no residual engine; fatal |
| `VIE` | finite-field triples near P125/P150 | Vieta mutation is a named classical involution | fixed hypergraph plus 2-cycles | all fibres singleton | `z -> xy-z` twice; fatal thinness/owner |
| `SFW` | simplex flags are new | update is rotation after adding the missing label | one uniform period | all fibres singleton | cyclic ordering erases the geometry; fatal |
| `UAW` | automata/finite-state carrier overlaps P23/P34/P57--P61 | pointer execution is literal but generic | arbitrary functional-graph tails/cycles | indegree is the static transition indegree | generic endofunction decomposition, explicitly excluded; fatal |
| `RCW` | permutations overlap P105/P122/P135/P154--P156 | conjugation walker is distinct | global involution is too shallow | all fibres singleton | cancellation of the same transposition on the second step; fatal |
| `SYT` | tableau/partition carrier near P74/P83/P113/P144 | literal Schuetzenberger promotion | cyclic-sieving orbit theorem is directly owned | all fibres singleton | hook/Catalan/promotion machinery is permanently excluded; fatal |
| `CUB` | partitions/tilings near P110/P113/P126 | complement-rotate is classical | involution | all fibres singleton; fixed locus is classical self-complementarity | plane-partition symmetry/product machinery is directly owned; fatal |
| `PDU` | projective frames near P67/P81/P103 | opposite-side polar map is adjugation | involution | all fibres singleton | double-adjugate proof from P103 transfers verbatim; fatal |
| `GFR` | group carrier near P84/P91/P102/P135/P137/P154 | update is coordinate rotation | periods only 1/3 | all fibres singleton | cube-root count plus rotation, a generic power/closure-adjacent package; fatal |

## Focused theorem contracts

### Gate 1: `BST`

A focused audit should prove, for every `r>=2` and without relying on bounded
enumeration:

1. the exhaustive four-stratum partition (diagonal, exactly two equal,
   ordered block, ordered nonblock) and the exact action on every stratum;
2. the sharp rank-2/rank-at-least-3 stabilization boundary, complete fixed and
   strict-three-cycle counts, depth polynomial, image size, and zeta function;
3. independently, the every-target fibre law `1`, `N-2`, or `0`, including a
   direct parametrization of all `N-2` sources of a specified block;
4. the degenerate ranks `r=1,2` as explicit boundary checks if the final
   statement elects to start at `r=1`;
5. an owner search for this exact ternary state map, not merely for Steiner
   quasigroups or binary projective Steiner systems, followed by explicit
   zero-credit subtraction of those standard inputs and of quasigroup cellular
   automata.

The proof spine is short but not a generic linear-map engine: equality branches
in `star` separate the four strata, while the equation
`(b+c)+(c+a)+(a+b)=0` forces only the all-distinct nonblock shell onto the
projective blocks.  The proposed residual is the complete functional graph
coupled to the nonuniform target fibres.

### Gate 2: `ORT`

A focused audit should prove, for every prime `p=3 mod 4`:

1. existence/uniqueness of the algebraic orthocenter and the four-point
   orthocentric identity over `F_p`, with all characteristic assumptions
   explicit;
2. disjointness and exact size `R` of the three oriented right-angle strata;
3. the exact depth `2/1/1` behavior of those strata, strict period four of all
   nonright triangles, the `p=3` empty-core boundary, sharp stabilization at
   time two, cycle counts, and zeta function;
4. independently, reconstruct the unique candidate source of an arbitrary
   triangle and prove the target-resolved fibre law, sink fibre, image size,
   and depth CDF;
5. compare directly with P150's zero-totalized finite-field rational dynamics
   and with finite-field orthocentric-system owners.  If the singular/fibre
   package is already explicit in that literature, kill immediately.

The standard fact that four orthocentric points may be cyclically re-windowed
is zero-credit input.  Only the finite-field anisotropic boundary and the full
temporal/fibre enumeration can survive the focused gate.

## Reproducibility boundary

Run

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_replacement.py
```

and byte-compare stdout with `CANONICAL.txt`.  The script independently builds
each finite carrier, checks literal closure, computes the functional graph,
and then compares pointwise depths and indegrees with the stated formulas for
`BST`, `ORT`, and `CRE`.  The remaining systems receive exact cycle/fibre
checks appropriate to their theorem ceilings.  Neither the script nor this
scout licenses a novelty statement.
