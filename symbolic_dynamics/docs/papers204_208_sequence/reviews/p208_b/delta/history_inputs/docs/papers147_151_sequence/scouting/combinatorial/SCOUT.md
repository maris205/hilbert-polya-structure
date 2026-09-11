# P147--P151 combinatorial / word / relation scouting

**Route:** A.  **Stage:** Stage 1 breadth and falsification only.  **External
status:** `HOLD_EXTERNAL`.  **Paper allocation:** none.

This lane tested twelve genuinely different literal finite systems.  It does
not revive record, border, palindrome, Lyndon, prefix-majority, relation
cubing, leftmost Dyck reassociation, partition split/join/shift, or a
parity/complement/scheduler recoding of P1--P146.  Exact enumeration is used
only as counterexample pressure.  It is neither an all-parameter proof nor an
owner certificate.

The most important conclusion is negative.  The initially strongest raw
signal, lexicographic chord uncrossing (`M01`), loses its static fibre theorem
to the matching-crossing literature and its geometric interface to P130.  A
bounded search did not locate the exact repeated scheduler, but the remaining
clock is adjacent-inversion resolution in the opener/closer encoding.  That is
too close to the batch's classical-sorting firewall to freeze as a paper.
This sublane therefore returns **no gate-clean select**.  That is preferable
to spending one of five slots on a renamed owned mechanism.

The exact replay is
[`verify_combinatorial_scout.py`](verify_combinatorial_scout.py); canonical
stdout is [`CANONICAL.txt`](CANONICAL.txt).  The final run made
**20,638,365 assertions and passed**.

## 1. Decision ledger

| ID | literal carrier and update | strongest exact signal | nearest collision / owner subtraction | decision |
|---|---|---|---|---|
| `L01` | inversion sequence; replace each entry by its strict rank in its current prefix | Catalan fixed set, sharp tail `n-2`, unique deepest source | the exact map, Catalan fixed set, stabilization, and maximal-time family are in Allagan--Gao--Testart (2026) | **KILL_DIRECT** |
| `M01` | perfect chord matching; resolve the lexicographically least crossing into a nesting | crossing number is the exact pointwise clock; Catalan endpoints; target basin polynomial `prod [h]_u` | Lam owns the uncrossing poset; Hermite histories own the `q`-product; P130 owns chord/noncrossing target-fibre geometry; the residual is constrained bubble sorting | **KILL_OWNER_THIN** |
| `B01` | partial permutation; match the least unmatched left vertex to the least unmatched right vertex | tail is number of holes; every permutation target has an increasing-subsequence basin polynomial | explicit batch ban on another greedy matching process; increasing-subsequence distribution is mature | **KILL_PORTFOLIO** |
| `C01` | bounded word; delete the leftmost equal adjacent pair | free-product normal form, exact cancellation clock, every-target regular-tree walk fibre | free-product/cogrowth theory plus the explicit free-monoid transport kill | **KILL_TRANSFER** |
| `T01` | labelled tree with a root marker; move the marker into its unique component larger than half | exact distance-to-centroid clock; one/two centroid endpoints and exact basin split | classical centroid walk; P114 rooted-forest metric interface | **KILL_CLASSICAL** |
| `G01` | labelled graph with a fixed order; fill the higher-neighbour clique of the least active vertex | sharp tail `n-2`; fixed graphs are exactly those for which the order is a PEO | Rose--Tarjan--Lueker vertex elimination owns the literal fill process | **KILL_DIRECT** |
| `S01` | `k`-uniform set family; apply the first changing `ij`-compression | strict weight potential and shifted fixed families | classical compression/shifting, plus no clean target fibre after subtraction | **KILL_CLASSICAL** |
| `F01` | endofunction; conjugate by the order of `(indegree,label)` | idempotent, image equals fixed set, exact one-step group-action inverse description | canonical relabelling/encoding is expressly inadmissible | **KILL_ENCODING** |
| `O01` | order ideal of a fence; ordinary rowmotion | bijective, Fibonacci carrier, rich exact periods | Striker--Williams rowmotion and the generic rowmotion/linear-extension firewall | **KILL_DIRECT** |
| `U01` | set family; adjoin the union from the least offending pair | endpoint is union closure; exact closure-deficit clock; target Möbius fibre polynomial | generic closure is a permanent intake kill | **KILL_FIREWALL** |
| `Q01` | tournament; reverse the first cyclic triangle | fixed tournaments are transitive; all nonfixed orbits eventually enter a 2-cycle | tournament interchange graphs own cyclic-triangle reversal; P112 owns tournament-reversal territory; scheduler theorem is a generic minimum-labelled-edge lemma | **KILL_OWNER_THIN** |
| `D01` | chips on a path with two sinks; fire the least unstable site | exact potential-gap clock, abelian endpoint, odometer interpretation | classical chip firing/sandpiles and occupied P62--P81 sandpile territory | **KILL_DIRECT** |

### Ranking after subtraction

1. **`M01` is the strongest raw package but not a select.**  Before
   subtraction it has three clean axes: a sharp pointwise clock, complete
   recurrent/endpoint classification, and every-target graded basins.  After
   subtraction, only the exact scheduler-oriented functional graph remains,
   and its proof is adjacent-inversion sorting.
2. **`B01` is the mathematical second.**  Its permutation-by-permutation
   basin polynomial is unusually explicit, including unique extremal basins.
   It is nevertheless unusable without waiving the hard prohibition on
   another greedy matching process.
3. **`U01` is the cleanest nonmatching control.**  Its Möbius fibre identity
   is exact for every target, but it is precisely a generic finite closure
   system.  It is a useful standard for what the value gate must reject.

There is consequently no honest same-lane replacement for `M01`.  A final
five-paper freeze should draw the replacement from another scouting lane,
not relax either the P130 or the generic-sorting/matching firewall.

## 2. `M01`: exact subtraction of the strongest raw signal

### 2.1 Literal map and finite profile

Let a matching on `[2n]={0,...,2n-1}` be written with each chord `(a,b)` in
increasing order.  Among all crossings

```text
(a,c), (b,d),       a < b < c < d,
```

choose the lexicographically least quadruple `(a,b,c,d)` and replace those
two chords by the nesting `(a,d),(b,c)`.  Fix a matching with no crossing.

For `n=1,...,7`, the exact triples `(states,image,fixed)` are

```text
(1,1,1), (3,2,2), (15,8,5), (105,53,14),
(945,473,42), (10395,5198,132), (135135,67568,429).
```

The exact maximal tails are

```text
0, 1, 3, 6, 10, 15, 21 = binom(n,2).
```

The last box exhausts all `135,135` matchings.  It checks all `429` terminal
basins and every coefficient of every target polynomial.

### 2.2 Raw theorem package and proof route

The following conjunction is valid all parameters.

1. Resolving the selected crossing decreases the total crossing number by
   exactly one.  A direct interval case split shows that any third chord that
   would change the net external crossing count would itself form an earlier
   crossing, contrary to the scheduler choice.  Thus
   `tau(M)=cr(M)` pointwise.
2. The set of opener positions is invariant.  For each admissible opener set
   there is one noncrossing matching: scan left to right and match every
   closer to the last still-open opener.  This is the endpoint of every state
   in that opener fibre.  Recurrent states are exactly the Catalan
   noncrossing matchings.
3. If a target has closer heights `h_1,...,h_n` immediately before its down
   steps, then its complete depth-basin polynomial is

   ```text
   B_T(u) = product_(j=1)^n (1+u+...+u^(h_j-1)).
   ```

   The basin size is `product h_j`.  The adjacent matching has basin one;
   the rainbow target has basin `n!`.
4. The unique global deepest state is
   `(0,n),(1,n+1),...,(n-1,2n-1)`, in which every pair of chords crosses.

The verifier's exact falsifier is stronger than a tail census: at every
nonfixed state it checks the one-unit decrement and opener invariance; it
iterates to the stack target; and it compares the observed depth counter of
every target with the full product polynomial.  `M01` contributes more than
the displayed `146,599` state visits because every orbit edge and every
coefficient is asserted independently.

### 2.3 Owner search and claim subtraction

The exact-scheduler search on 2026-09-01 used primary/official records only,
including the phrases

```text
matching "leftmost crossing" uncrossing
chord matching "lexicographically first" crossing uncrossing
perfect matching leftmost uncrossing crossings
matching crossing nesting adjacent transposition
chord diagram uncrossing bubble sort
```

No source located in that bounded search stated this exact repeated
lexicographic self-map.  This is only a non-hit, not novelty evidence.

The subtraction is nevertheless decisive.

- Lam's [*The uncrossing partial order on matchings is
  Eulerian*](https://arxiv.org/abs/1406.5671) directly owns the matching
  crossing-resolution order and its noncrossing extremal layer.
- Josuat-Vergès's [*Crossings, Motzkin paths and
  moments*](https://doi.org/10.1016/j.disc.2011.05.019) gives the
  opener/closer Hermite-history encoding in which a closer at height `h`
  carries a `q`-choice.  Consequently `prod [h_j]_q` and all its coefficient
  consequences receive zero credit.
- Chen--Deng--Du--Stanley--Yan's [*Crossings and Nestings of Matchings and
  Partitions*](https://arxiv.org/abs/math/0501230) owns the fixed-endpoint
  crossing/nesting distributional setting.
- Internally, P130 already uses chord matchings, noncrossing endpoints,
  uncrossing literature, and target-local nesting-fibre geometry.  A
  different deterministic scheduler proves nonidentity, not paper-scale
  separation.

Finally, with opener positions fixed, a matching is a constrained close-order
word.  A crossing is an inversion, and the selected cover exchanges an
adjacent inverted pair.  The exact clock is therefore the inversion clock of
a constrained bubble sort.  This consumes the putative temporal residual
under the batch's explicit classical-sorting rule.  `M01` is
**`KILL_OWNER_THIN`**, not a paper assignment.

## 3. `B01`: strongest mathematical second, portfolio-ineligible

### 3.1 Literal map and profile

A state is an injective partial map from left vertices `[n]` to right
vertices `[n]`, written as a tuple with `-1` for a hole.  If holes remain,
match the least unmatched left vertex to the least unused right vertex.

For `n=1,...,7`, the exact state counts are

```text
2, 7, 34, 209, 1546, 13327, 130922
  = sum_k binom(n,k)^2 k!.
```

The image counts are

```text
1, 3, 14, 85, 626, 5387, 52882,
```

the fixed counts are `1,2,6,24,120,720,5040`, and the maximal tails are
`1,2,3,4,5,6,7`.

### 3.2 Candidate theorem package

The tail of a state is exactly its number of holes.  The unique deepest
state is the empty partial matching.  At depth `d` the exact all-parameter
state census is

```text
binom(n,d)^2 (n-d)!.
```

For a terminal permutation `pi`, let

```text
I_pi(u) = sum_{A subset [n], pi restricted to A increasing} u^|A|.
```

Then the depth-basin polynomial of `pi` is exactly `I_pi(u)`: the deleted
left positions are `A`, and greedy completion reproduces `pi` precisely when
the values `pi(A)` occur in increasing order.  The identity is the unique
largest target, with basin `2^n`; the decreasing permutation is the unique
smallest target, with basin `n+1`.  The proof route is a direct restriction /
completion bijection, independent of enumeration.

The verifier checks the temporal layer formula and the entire polynomial for
all `sum_{n<=7} n! = 5,913` targets.  A falsifier can reject the theorem by a
single target/subset mismatch, not merely a total count mismatch.

### 3.3 Collision and decision

Lifschitz--Pittel's primary increasing-subsequence work is
[*The number of increasing subsequences of the random
permutation*](https://doi.org/10.1016/0097-3165(81)90049-2); all static
increasing-subsequence distribution claims receive zero credit.  More
decisively, the current historical firewall explicitly prohibits another
greedy matching process.  This is exactly one.  The package is retained as a
high-value negative control, **`KILL_PORTFOLIO`**.

## 4. Ten further genuinely distinct systems

### 4.1 `L01`: strict prefix rank on inversion sequences

**Map.**  For an inversion sequence `e=(e_1,...,e_n)`, set

```text
Theta(e)_i = #{j<i : e_j < e_i}.
```

**Exact profile.**  For `n=1,...,9`, image sizes are

```text
1,2,5,15,53,217,1014,5335,31240;
```

fixed sizes are

```text
1,2,5,14,42,132,429,1430,4862 = Cat_n;
```

and maximum tails are `0,0,1,2,3,4,5,6,7`.  For every `n>=3`, the unique
deepest state is

```text
(0,1,...,n-3,0,1).
```

**Raw theorem / proof.**  Iterated prefix ranks stabilize; the fixed states
are Catalan; the sharp clock is `n-2` with the displayed equality family.
The natural proof tracks the first coordinate at which rank information is
not yet self-consistent and inducts on the stabilized prefix.

**Owner and decision.**  Allagan--Gao--Testart, [*Iterating the Lehmer code on
inversion sequences: Catalan fixed points and finite
stabilization*](https://arxiv.org/abs/2608.24476), state this literal map,
Catalan fixed points, finite stabilization, and the maximal-time family.
This is an immediate **`KILL_DIRECT`**.  The exact falsifier still checks all
`409,113` inversion sequences through `n=9` and all iterate identities.

### 4.2 `C01`: adjacent-equal cancellation

**Map.**  On all words over `q` letters of length at most `N`, delete the
leftmost adjacent pair `aa`; fix a reduced word.

**Exact profile.**  The two exhaustive boxes are

```text
q=2,N=12: states=8191, image=2051, fixed=25,  max_tail=6;
q=3,N= 8: states=9841, image=1669, fixed=766, max_tail=4.
```

**Candidate all-parameter theorem.**  The endpoint is the reduced normal form
in the free product of `q` copies of `C_2`; the clock is
`(|w|-|red(w)|)/2`; the sharp carrier clock is `floor(N/2)`; and the fixed
count is

```text
1 + sum_(ell=1)^N q(q-1)^(ell-1).
```

For any fixed target at reduced distance `d`, its length-`m` source count is
the regular-tree walk number `A_m(d)`, determined by

```text
A_0(0)=1,
A_(m+1)(0)=q A_m(1),
A_(m+1)(d)=A_m(d-1)+(q-1)A_m(d+1),  d>=1.
```

The verifier checks every target and length coefficient.  Confluence of the
free-product rewriting system and the Cayley-tree recurrence are the proof
routes.

**Collision / owner.**  Mairesse--Mathéus [*Random walks on free products of
cyclic groups*](https://arxiv.org/abs/math/0509211) and Bell--Liu--Mishna
[*Cogrowth Series for Free Products of Finite
Groups*](https://arxiv.org/abs/2110.00089) own the normal-form/walk engine.
The problem anchor separately says to kill free-monoid transport.  Hence
**`KILL_TRANSFER`**.

### 4.3 `T01`: heavy-component walk to a tree centroid

**Map.**  A state is an unrooted labelled tree with a distinguished marker
`r`.  Delete `r`; if one component has more than `n/2` vertices, move the
marker one edge into that unique component; otherwise fix.

**Exact profile.**  For `n=1,...,8`, the aggregate
`(rooted states,image states,fixed states,max tail)` is

```text
(1,1,1,0),
(2,2,2,0),
(9,3,3,1),
(64,28,28,1),
(625,305,125,2),
(7776,4026,2106,2),
(117649,63217,16807,3),
(2097152,1155960,405504,3).
```

This exhausts all `262,144` labelled trees at `n=8` and every one of their
`2,097,152` marker positions.

**Candidate theorem.**  Every orbit stops at a centroid; its pointwise clock
is distance to the centroid set; the global sharp clock is
`floor((n-1)/2)`, witnessed by a path.  A tree has one centroid, whose basin
contains all `n` marker positions, or two adjacent centroids, whose two basins
have size `n/2` each.  The proof uses component-side sizes along an edge and
the standard centroid lemma.

**Collision / owner.**  This is the classical centroid-walk algorithm, with
nearby primary centroid literature including [*Centroids to centers in
trees*](https://doi.org/10.1002/net.3230210103).  Internally, P114 already
occupies rooted-forest metric absorption.  Recasting the classical algorithm
as a finite map leaves no inverse theorem beyond choosing a root marker:
**`KILL_CLASSICAL`**.

### 4.4 `G01`: fixed-order elimination fill

**Map.**  On a graph on ordered vertices `[n]`, choose the least vertex whose
higher-numbered neighbours are not a clique and add every missing edge among
those neighbours.  Fix if no such vertex exists.

**Exact profile.**  For `n=1,...,7`, `(states,image,fixed,max tail)` is

```text
(1,1,1,0), (2,2,2,0), (8,7,7,1),
(64,41,39,2), (1024,430,324,3),
(32768,9061,3839,4).
```

**Candidate theorem.**  Once a vertex is processed, later edge additions
cannot destroy its completed higher-neighbour clique.  Hence the tail is at
most `n-2`; an inductively nested missing-edge construction is sharp.  The
fixed states are exactly the graphs for which `0<1<...<n-1` is a perfect
elimination ordering.  Recurrent states are fixed.  A prospective fibre
description is by assigning each added fill edge to its least forcing
elimination vertex; the small data show that this does not factor cleanly.

**Owner / falsifier / decision.**  Rose--Tarjan--Lueker's [*Algorithmic
Aspects of Vertex Elimination on
Graphs*](https://doi.org/10.1137/0205021) owns fixed-order fill and perfect
elimination.  Every nonfixed verifier step asserts edge monotonicity, and all
`32,768` six-vertex graphs are iterated, but this cannot create residual
priority: **`KILL_DIRECT`**.

### 4.5 `S01`: scheduled uniform-family compression

**Map.**  For a `k`-uniform family and `i<j`, perform the usual full
`ij`-compression: replace a set containing `j` but not `i` by its shifted set
when the latter is absent.  Apply the lexicographically first pair that
changes the family.

**Exact profile.**  All families for `n<=5` were tested.  The informative
`n=5` rows `(k: states,image,fixed,max tail)` are

```text
0: (2,2,2,0), 1: (32,17,6,4), 2: (1024,323,16,8),
3: (1024,323,16,8), 4: (32,17,6,4), 5: (2,2,2,0).
```

At `n=4,k=2` the row is `(64,26,8,4)`.  The complete table for every
`(n,k)` is in the canonical output.

**Candidate theorem.**  The sum of element labels over all member sets
strictly decreases at every step; recurrent states are precisely shifted
families.  This supplies termination and a crude all-parameter potential
bound.  A paper-scale package would additionally need a sharp clock and an
every-target inverse theorem.  The exact profiles show no such factorization.

**Owner / decision.**  This is classical compression, beginning with the
Erdős--Ko--Rado shifting tradition; see the primary [*Intersection theorems
for systems of finite sets*](https://doi.org/10.1093/qmath/12.1.313).
Changing the scheduler adds no admissible contribution: **`KILL_CLASSICAL`**.

### 4.6 `F01`: indegree-ranked endofunction conjugation

**Map.**  For `f:[n]->[n]`, rank vertices by `(indegree_f(v),v)`.  If `r` is
that ranking permutation, set `T(f)=r f r^{-1}`.

**Exact profile.**  For `n=1,...,6`, image/fixed counts are

```text
1,3,10,47,246,1602
```

inside `1,4,27,256,3125,46656` endofunctions.  The maximum tail is zero at
`n=1` and one thereafter.

**Candidate theorem.**  The indegrees of `T(f)` are nondecreasing in the new
labels, so `T^2=T`; image and fixed set coincide.  For a fixed target `g`,
the one-step fibre is the quotient of the permutations `sigma` satisfying
that `sigma^{-1}` is increasing within every equal-indegree block of `g`,
under the stabilizer of `g`, via `f=sigma^{-1}g sigma`.  This is an exact
group-action inverse route, not an enumerative conjecture.

**Collision / decision.**  The whole update is canonical relabelling.  The
anchor explicitly rejects carrier encoding/relabeling, and canonical graph
labelling is mature (for example McKay's university-hosted primary paper
[*Practical Graph
Isomorphism*](https://users.cecs.anu.edu.au/~bdm/nauty/PGI.pdf)).  A one-step
retraction is also below the progress threshold: **`KILL_ENCODING`**.

### 4.7 `O01`: rowmotion on fence ideals

**Map.**  For the fence `0<1>2<3>...`, send an order ideal `I` to the ideal
generated by the minimal elements of its complement.

**Exact profile.**  The carrier sizes for `n=1,...,15` are

```text
2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597.
```

The first eight exact period-by-state profiles are

```text
n=1  {2:2}
n=2  {3:3}
n=3  {2:2,3:3}
n=4  {3:3,5:5}
n=5  {2:2,3:3,8:8}
n=6  {3:3,7:7,11:11}
n=7  {2:2,3:3,5:5,10:10,14:14}
n=8  {3:3,9:9,13:26,17:17}.
```

There are no fixed ideals in the tested nonempty fences; rowmotion is a
bijection.  The exact profiles through `n=15` are recorded canonically.

**Candidate theorem.**  Carrier size is `F_(n+2)`; all states are recurrent;
every one-step fibre has size one; periods may be derived by the known fence
orbit decomposition.  This is an excellent falsifier of any false
uniform-period guess, but not a new dynamics package.

**Owner / decision.**  Striker--Williams, [*Promotion and
Rowmotion*](https://arxiv.org/abs/1108.1172), directly own rowmotion as a
toggle-group action.  Generic rowmotion/linear-extension results are also
explicitly zero-credit in the anchor: **`KILL_DIRECT`**.

### 4.8 `U01`: scheduled union closure

**Map.**  For a family `F` of subsets of `[n]`, choose the lexicographically
least pair `A<B` in `F` with `A union B` absent and adjoin that union.

**Exact profile.**  For `n=1,...,4`, `(states,image,fixed,max tail)` is

```text
(4,4,4,0), (16,14,14,1),
(256,154,122,4), (65536,32918,4960,11).
```

**Candidate theorem.**  The endpoint is the union closure `Cl(F)`, independent
of scheduler; the exact clock is `|Cl(F)|-|F|`; recurrent states are exactly
union-closed families.  For a fixed union-closed target `U`, write

```text
G_U(z)=sum_{F: Cl(F)=U} z^|F|.
```

If `L(U)` is the inclusion poset of union-closed subfamilies of `U`, then

```text
G_U(z)=sum_{V<=U} mu(V,U)(1+z)^|V|,
B_U(u)=u^|U| G_U(u^(-1)).
```

This follows by Möbius inversion from
`(1+z)^|U|=sum_{V<=U}G_V(z)`.  The verifier checks the full zeta identity for
every target through `n=4`, not only the endpoint clock.

**Owner / decision.**  Finite union-closure algorithms and Moore co-families
are established, for example in Colomb et al., [*Recursive decomposition tree
of a Moore co-family and closure
algorithm*](https://doi.org/10.1007/s10472-013-9362-x).  More importantly,
generic closure operators are a literal permanent kill in this batch.
**`KILL_FIREWALL`**.

### 4.9 `Q01`: lexicographic cyclic-triangle reversal

**Map.**  In a labelled tournament, choose the lexicographically first cyclic
triple and reverse all three of its arcs.  Fix a tournament with no cyclic
triple.

**Exact profile.**  For `n=1,...,6`, `(states,image,fixed,max tail)` is

```text
(1,1,1,0), (2,2,2,0), (8,8,6,0),
(64,58,24,2), (1024,802,120,3),
(32768,22704,720,4),
(2097152,1335336,5040,5).
```

At `n=3`, the two nontransitive states form a 2-cycle.  At `n=6`, exactly
`720` states have period one and `32,048` states (including transients) have
eventual period two.  At `n=7` these numbers are `5,040` and `2,092,112`.
The exact `n=7` tail census is

```text
tau=0: 1,190,944; 1: 751,568; 2: 131,832; 3: 21,960;
tau=4: 832; 5: 16.
```

Here `tau=0` includes both fixed points and the `1,185,904` nonfixed cycle
vertices, i.e. `592,952` terminal 2-cycles.

**All-parameter recurrent theorem.**  Fixed tournaments are transitive, so
there are `n!`.  Reversing the selected triple leaves that same triple cyclic.
At the next state either it is selected again, producing a 2-cycle, or a
strictly earlier triple is selected.  Selected triple labels therefore
strictly descend until a mutual-minimum interchange edge is reached: an edge
`T--T'` of the cyclic-triangle interchange graph for which the reversed
triple is the lexicographically least cyclic triple at both endpoints.
Terminal 2-cycles are exactly these mutual-minimum edges.  Every nonfixed
orbit enters one, with the general bound `tau<=binom(n,3)-1`.

The observed stronger `tau<=n-2` now survives exhaustive testing at `n=7`,
but it remains an anomaly rather than a theorem.  Attempting to extend every
deepest seven-vertex source by all `2^7` orientations of a new vertex produced
no depth-six witness.  No monotone statistic giving the linear bound, no
all-`n` normal form for mutual-minimum edges, and no independent
target-resolved inverse were found.  The generic descent lemma therefore does
not revive the candidate.

**Exact falsifier.**  With tournament bits ordered by pairs and bit one
meaning lower label beats higher label, the three-vertex state `010` is sent
to `101`, which is sent back to `010`.  This kills any convergence-to-
transitive claim at the smallest possible size.  The verifier also computes
the complete functional graph through all `2,097,152` seven-vertex
tournaments and asserts period in `{1,2}` state by state.

**Owner / collision / decision.**  Kolesnik--Mitchell--Przybyłowski's
[*Coxeter Interchange Graphs*](https://doi.org/10.1007/s00026-025-00768-9)
explicitly defines tournament interchange edges by cyclic-triangle reversal
and records score preservation and score-fibre connectivity.  P112 already
occupies tournament reversal dynamics.  The new recurrent observation is the
generic minimum-labelled-edge lemma above.  A bounded exact-scheduler audit
searched combinations of “lexicographically first/minimum”, “cyclic
triangle”, “triangle interchange”, “switch”, and “tournament score sequence”
in arXiv, Crossref/DOI, and publisher records; it found the direct interchange
owner but no primary source naming this repeated lex scheduler.  That non-hit
is not a novelty certificate: after subtraction the only proved residual is
the label-descent lemma, with neither the sharp linear clock nor the target
inverse required by this batch.  Decision: **`KILL_OWNER_THIN`**.

### 4.10 `D01`: least-unstable path chip firing

**Map.**  On `m` nonsink vertices in a path bracketed by two sinks, choose the
least `i` with at least two chips, remove two, and send one to each path
neighbour; an endpoint loses one chip to its adjacent sink.  The finite
carrier consists of all configurations with total mass at most `N`.

**Exact profile.**  At `N=8`, for `m=1,...,6`,
`(states,image,fixed,max tail)` is

```text
(9,7,2,4), (45,31,4,7), (165,111,8,13),
(495,327,16,17), (1287,835,32,23),
(3003,1916,64,26).
```

**Candidate theorem.**  Put

```text
W(x)=sum_(i=1)^m i(m+1-i)x_i.
```

Every legal firing decreases `W` by exactly two.  Stabilization is independent
of whether one always fires the least or the greatest unstable site; the two
schedulers also have the same odometer and firing count.  Hence

```text
tau(x)=(W(x)-W(stab(x)))/2.
```

Recurrent states are precisely the stable binary configurations, and for
`N>=m` there are `2^m`.  Target fibres are the nonnegative integer odometers
solving the corresponding discrete-Laplacian equation with the legality
obstacle.  The verifier compares least/greatest endpoints, odometers, and the
potential gap for every tested input.

**Owner / decision.**  Björner--Lovász--Shor's [*Chip-firing games on
graphs*](https://doi.org/10.1016/S0195-6698(13)80111-4) owns termination and
abelian/odometer infrastructure; Björner--Lovász's [directed extension](https://doi.org/10.1023/A:1022467132614)
develops the wider theory.  The internal portfolio already contains
sandpiles.  The literal priority scheduler adds no paper-scale residual:
**`KILL_DIRECT`**.

## 5. Aborted intakes not counted as distinct systems

Two attractive formulas were deliberately not used to inflate the breadth
count.

- For an endofunction `f`, the map
  `i -> |f^{-1}(f(i))|-1` merges domain fibres solely by equal cardinality.
  After quotienting its labels it is the root scout's equal-cardinality
  coarsening (`EQC`), so it is an intake collision, not a thirteenth system.
- On a path orientation, repeatedly pushing the least source has a sharp
  quadratic tail and product basins, but it is the same vertex-push literal
  operation as P145 with a new scheduler.  The P147--P151 anchor explicitly
  forbids scheduler changes of P142--P146, so it was aborted before promotion.

## 6. Exact-evidence boundary

The verifier checks the literal maps, carrier closure, clocks, fixed/recurrent
sets, extremal witnesses, and the advertised target polynomials.  Its final
line is

```text
ASSERTIONS=20638365
STATUS=PASS
```

This proves only that no counterexample exists in the enumerated boxes and
that the exact finite identities were implemented consistently.  It does not
prove the all-parameter statements, priority, novelty, or external-release
rights.  All sources above are primary papers, official DOI records, arXiv
records, or an author's university-hosted primary manuscript.  No external
submission, message, or repository action was taken.
