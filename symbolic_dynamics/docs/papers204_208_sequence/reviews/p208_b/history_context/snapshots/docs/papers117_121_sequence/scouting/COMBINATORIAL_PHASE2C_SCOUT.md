# Phase-2c geometric/combinatorial rewrite replacement pool

**Date:** 2026-08-30  
**Status:** Q01 cleared the hard gate and is frozen internally as P120; the
remaining nine entries are scouting only  
**External status:** `HOLD_EXTERNAL`

## Scope and hard firewall

This report contains **exactly ten** literal finite dynamical systems.  They
were generated as a replacement pool after the R3 owner kill.  None is the
R2 odd-run reversal, C02 synchronous mex map, the regular Engel map, or a
literal map from P001--P116.

The intake firewall gives zero credit to ordinary peeling, closure,
rowmotion/promotion, sorting or 0-Hecke normalization, generic finite-linear
maps, standard tree rotations that change parenthood, and named canonical
reductions.  In particular:

- P105/P114 already occupy permutation pruning and rooted-tree leaf peeling;
- P110/P113 occupy partition-lattice shift--join and principal-hook
  regrouping;
- P78/P90 occupy sandpile and one-dimensional particle/CA mechanisms;
- P96/P97 occupy circle-expansion and sumset-closure dynamics;
- P111 owns binary-word area as a cocycle statistic; and
- P112 owns a parity/score-selected graph correction.

A bounded no-hit below is never treated as novelty.  Scores are hostile
paper-scale residual scores after the stated subtraction, not probabilities
of priority.

## Ranked table: exactly ten systems

| rank | ID | literal map | carrier | earliest useful signal | score | action |
|---:|---|---|---|---|---:|---|
| 1 | Q01 | mirror the child list at every odd-order fringe subtree | unlabelled plane rooted trees | involution, exact twisted-palindrome census, and an explicit algebraic fixed series | **8.1** | **PROMOTE INTERNALLY; HOLD EXTERNAL** |
| 2 | Q04 | left-greedy complementary domino flip | tilings of a `2 by n` strip | `(1,2) -> (1,1,1)` enters, rather than lies on, a 2-cycle | **7.1** | **RESERVE FOR SPIKE** |
| 3 | Q06 | translate every hyperedge by the odd-degree vertex set | simple `m`-edge hypergraphs on `[n]` | odd `m` gives an idempotent; even `m` gives an involution | **6.8** | **RESERVE** |
| 4 | Q08 | transpose an SYT exactly when its major index is odd | all standard Young tableaux of size `n` | the map alternates between involutive and idempotent regimes modulo four | **6.4** | **RESERVE** |
| 5 | Q09 | flip the diagonal opposite the least-labelled ear | triangulations of a labelled convex polygon | the quadrilateral is a 2-cycle, so there is no monotone ear clock | **6.0** | **RESERVE, UNSPIKED** |
| 6 | Q07 | reflect each primitive balanced-path excursion with odd turn count | balanced north/east words | intrinsic componentwise involution | **5.2** | **KILL: same-engine risk** |
| 7 | Q02 | cyclically shift every child list one place | vertex-labelled plane rooted trees | pointwise period is an outdegree LCM; global maximum is Landau `g(n-1)` | **4.8** | **KILL: mechanical product action** |
| 8 | Q05 | take the rotated complement in the current tight Ferrers box | partitions inside an `N by N` box | depth is exactly the number of distinct parts | **4.3** | **KILL: theorem-thin/P113** |
| 9 | Q10 | rotate labels once on every convex-hull layer | labelings of a fixed generic planar point set | period is just the LCM of layer sizes | **3.6** | **KILL: product action only** |
| 10 | Q03 | rotate a chord matching by its number of crossings | perfect matchings of cyclically labelled points | maximum period `2n`, but each crossing stratum is an owned rotation action | **2.9** | **KILL: owner reduction** |

Q01 alone clears the requested score-at-least-7.5 gate.  Its explicit
algebraic equation and objectwise owner firewall justify internal promotion,
subject throughout to `HOLD_EXTERNAL`.  Q02 was downgraded after proof:
all of its temporal statements are consequences of a product of static local
cycles, so the exact calculation is a negative spike rather than a paper.

## Q01. Odd-fringe mirror on plane rooted trees

### Literal map

Let `P_n` be the Catalan set of unlabelled plane rooted trees with `n>=1`
vertices.  For every vertex `v`, let `T_v` be its fringe subtree.  In one
simultaneous update `M`:

1. retain the rooted parent--child relation;
2. if `|T_v|` is odd, reverse the left-to-right child list at `v`;
3. if `|T_v|` is even, retain that child order.

All trigger bits are read from the old tree.  Child reversal does not change
any fringe order, so the same trigger set is used forever.

### Infinite-family theorem spike

**Status: PROVABLE AS STATED.**

Fringe orders are invariant and every local reversal has order two.  The
local reversals commute because they act on distinct child lists.  Hence

\[
M^2=\mathrm{id}
\]

on every `P_n`.  The nontrivial part is the fixed set, not the period bound.

Let

\[
A(x)=\sum_{n\ge1}C_{n-1}x^n=\frac{x}{1-A(x)}
\]

be the plane-tree series.  Let `E(x)` and `O(x)` enumerate `M`-fixed trees of
even and odd order.  Root decomposition gives the coupled formal system

\[
\boxed{
 E=\frac{xO}{(1-E)^2-O^2},
 \qquad
 O=\frac{x(1+E)}{1-A(x^2)}.
}
\]

For an even-order fixed tree the root does not reverse, so its child sequence
consists entirely of fixed trees and has odd total order.  The odd part of
`SEQ(E+O)` is

\[
\frac12\left(\frac1{1-E-O}-\frac1{1-E+O}\right)
=\frac{O}{(1-E)^2-O^2}.
\]

For an odd-order fixed tree, write its child list as
`(T_1,...,T_r[,U],T'_r,...,T'_1)`.  The root condition is the literal
twisted-palindrome relation `T'_i=M(T_i)`.  Each off-centre pair has series
`A(x^2)` because `T_i` is arbitrary and the pair has order `2|T_i|`.
The optional central child `U` must be `M`-fixed and even: the root has odd
order, so its children have even total order.  Hence the odd-root child-list
series is `(1+E)/(1-A(x^2))`.  This proves the boxed system, including its
parity offsets.

The algebraicity can be made explicit.  Put `F=E+O`, `G=E-O`,
`B=A(x^2)`, and `c=1-B`.  The coupled equations imply

\[
(F+G)(1-F)(1-G)=x(F-G),\qquad
G=\frac{(c-x)F-2x}{c+x},\qquad B^2-B+x^2=0.
\]

Eliminating `G` and `B` gives `P(x,F(x))=0`, where

\[
\begin{aligned}
P(x,y)={}&(2x^2-x)y^6+(1-2x)y^5
 +(4x^3+6x^2+4x)y^4\\
&+(4x^3-12x^2-11x-6)y^3\\
&+(2x^4-11x^3+10x^2+26x+8)y^2\\
&+(4x^4-2x^3-20x^2-19x-3)y\\
&+2x^4+9x^3+14x^2+3x.
\end{aligned}
\]

Since `P_y(0,0)=-3`, the condition `F(0)=0` selects a unique formal branch;
the displayed equation is not merely a declaration that some elimination
exists.  The exact pilot evaluates this polynomial on the independently
enumerated series through degree twelve.

If `f_n=[x^n]F(x)`, the complete finite cycle data is

\[
\#\mathrm{Fix}(M|P_n)=f_n,\qquad
\#\{\text{2-cycles}\}=\frac{C_{n-1}-f_n}{2},
\]

and

\[
\zeta_{M,n}(z)
=(1-z)^{-f_n}(1-z^2)^{-(C_{n-1}-f_n)/2}.
\]

The first fixed counts are

`1,1,2,5,8,36,48,303,368,2792,3248,27310`.

The parity oscillation is real rather than a small-size artefact of ordinary
global mirror symmetry.  The first `M`-fixed tree that is not globally
mirror-symmetric is `((),((),))` at order four; the first globally
mirror-symmetric tree that is not `M`-fixed is
`(((),((),)),(((),),()))` at order nine.  Here `()` denotes a leaf and a
tuple lists the children of its root.

### Two genuinely different proof routes

1. **Ordered-species/palindrome route (complete spike).**  Split fixed trees
   by total parity at the root.  Ordinary fixed child sequences give the
   odd part of `1/(1-F)`.  Twisted palindromes give
   `(1+E)/(1-A(x^2))`.  Separating even and odd orders produces the boxed
   system; elementary elimination gives `P`, and the involution gives the
   cycle census and zeta formula.
2. **Underlying-tree/local-dihedral route.**  Forget the plane order and fix
   an underlying nonplane rooted tree.  Its plane embeddings are products of
   arrangements of child-branch isomorphism classes.  At each odd fringe
   vertex, `M` acts by reversal on that local arrangement.  Burnside/Pólya
   counting of palindromic multiset words gives fixed embeddings fibrewise;
   summing over underlying trees gives an independent refinement by
   automorphism type.  This route does not use the global `SEQ` equation and
   can refine by the unordered skeleton.

### Hostile owner search through 2026

The closest primary owner is Chen--Shapiro--Yang,
[*Parity reversing involutions on plane trees and 2-Motzkin
paths*](https://doi.org/10.1016/j.ejc.2004.07.013), `European Journal of
Combinatorics` 27 (2006), 283--289.  Their unlabelled-tree involution locates
one illegal vertex and transfers a prefix of its siblings; it changes the
parity of the number of leaves.  It is not simultaneous child reversal, does
not preserve the same local data, and does not give the boxed fixed series.
Deutsch's [ordered-tree
bijection](https://doi.org/10.1006/jcta.1999.3027) (2000) is another direct
involution neighbour, but it redistributes degree and level statistics rather
than applying the literal fringe-parity rule.

Recent searches also checked the 2025--2026 plane-tree action literature.
Bousquet-Mélou--Krattenthaler's
[*Cyclic sieving phenomena for trees and tree-rooted
maps*](https://arxiv.org/abs/2512.18656) moves a distinguished root corner,
leaf, or nonleaf corner around a fixed plane tree.  Its action changes the
rooting and has cyclic-sieving fixed sets; it does not reverse selected child
lists.  Claesson--Kitaev--Steingrímsson--Wang's 2026 preprint
[*Involution h on Catalan
structures*](https://arxiv.org/abs/2607.06247) is a closer current owner of
abstract Catalan involutions, global child-list reversal, fixed-point
enumeration, and Donaghey's automorphism.  It receives zero credit here:
their plane-tree `h` sends the three-leaf star to a depth-three path and has
no positive even-size fixed points, whereas Q01 preserves every parent--child
edge and has fixed trees of both parities.  Thus neither `h`, their global
`rev`, nor the stated composition is the literal odd-fringe map.

Searches for `odd subtree size reverse children`, `fringe parity
mirror plane tree`, `recursive ordered-tree involution`, and their
2025--2026 variants did not locate the literal map.  This is a bounded
no-hit only.

### Objectwise firewalls

| feature | Q01 odd-fringe mirror | classical global mirror | P114 leaf peeling |
|---|---|---|---|
| carrier | fixed-order plane rooted trees | fixed-order plane rooted trees | rooted forests with a rank-lowering sink |
| local action | reverse only at odd fringe order | reverse at every vertex | delete all eligible nonroot leaves |
| edges/order | every edge and vertex retained | every edge and vertex retained | vertices and incident edges deleted |
| temporal law | all states recurrent, period one or two | all states recurrent, period one or two | absorption depth equals a height clock |
| fixed test | even root: children pointwise fixed; odd root: `M`-twisted palindrome | mirror-twisted palindrome at every root | no local-palindrome criterion |
| enumeration | Catalan carrier with the coupled `E/O` series above | classical self-mirror census | Cayley forest basins |

The two explicit tuples above make the fixed sets of Q01 and global mirror
incomparable, rather than merely differently described.  P114's deletion,
height clock, basins, and Cayley enumeration therefore receive zero credit.
P83/P88 tree-shift enumerations and generic Catalan/algebraic-series methods
also receive zero credit.

**Strongest objection.**  The involution is deliberately local, and once the
twisted-palindrome grammar is seen, algebraicity belongs to standard
context-free enumeration.  The residual is therefore the exact conjunction
of the intrinsic trigger, the parity-sensitive fixed characterization, the
explicit coupled system and degree-six branch, and the complete cycle census;
none of those standard tools receives novelty credit by itself.

**Hard verdict: PROMOTE INTERNALLY, 8.1/10; `HOLD_EXTERNAL`.**  The explicit
polynomial clears the required algebraic/refinement gate, and the 2026 Catalan
owner is nonliteral object by object.  The claim ceiling is the involution,
fixed characterization, coupled `E/O` equations, displayed polynomial, and
exact fixed/two-cycle/zeta census.  No asymptotic, priority, or general
Catalan-involution claim is authorized.  Kill only if a future source states
the same odd-fringe trigger after a proved conjugacy.

## Q02. Simultaneous child-cycle rotation

### Literal map

Let `L_n` be the plane rooted trees on vertex labels `{0,...,n-1}` with root
fixed at zero.  In one update `R`, every nonleaf vertex simultaneously moves
the first child in its ordered child list to the last position.  Parenthood,
labels, and every outdegree are unchanged.

Labels are essential in this formulation: child subtrees at one vertex have
disjoint label sets, so a nontrivial cyclic shift cannot accidentally fix a
repeated child word.

### Infinite-family theorem spike

**Status: PROVABLE AS STATED.**

For `T in L_n`,

\[
\boxed{\operatorname{per}_R(T)
=\operatorname{lcm}\{\deg^+(v):\deg^+(v)>0\}.}
\]

Indeed, after `t` rounds the child list at `v` has moved by `t` modulo its
outdegree, independently of every other vertex.  Since the positive
outdegrees sum to `n-1`, the global maximum is

\[
\boxed{\max_{T\in L_n}\operatorname{per}_R(T)=g(n-1),}
\]

where `g` is Landau's function, the maximum LCM of a partition.  Conversely,
every partition `d_1+...+d_k=n-1` is realized by a spine whose `i`th spine
vertex has `d_i` children, so the upper bound is attained.  Degrees four and
three already give an eight-vertex period-12 tree, falsifying the tempting
`period <= n` guess.

For each `t>=1`, let `T_t(x)` be the EGF-normalized plane-tree series fixed by
`R^t`.  A vertex can have zero children or a positive number dividing `t`,
and therefore

\[
\boxed{
T_t(x)=x\left(1+\sum_{d\mid t}T_t(x)^d\right).
}
\]

The number with root label fixed is
`(n-1)![x^n]T_t(x)`.  Möbius inversion of these fixed-iterate counts gives
the number of cycles of every exact period and hence the finite zeta
function.  This is a full period-layer theorem, not only a maximum.

### Two genuinely different proof routes

1. **Local commuting-action route.**  Freeze the underlying labelled rooted
   tree.  Its plane orders form a product of cyclic torsors, one at each
   nonleaf vertex; `R` is the diagonal generator.  This proves the pointwise
   LCM formula.  A spine construction and Landau's partition
   characterization prove sharpness.
2. **Lukasiewicz/cycle-lemma route.**  Encode a plane tree by its preorder
   outdegree word.  Fixed points of `R^t` are exactly the Lukasiewicz words
   whose positive letters divide `t`.  The cycle lemma or Lagrange inversion
   gives the boxed functional equation directly.  The same encoding realizes
   every degree partition and independently recovers the Landau maximum.

### Hostile owner search through 2026

A newly indexed programming problem,
[*Anya Loves Trees!*](https://codeforces.com/problemset/problem/2244/F),
uses the literal local move “choose a vertex and cyclically shift its children
to the left” as an allowed operation.  It is not a scholarly temporal owner
and does not apply the move at every vertex on every clock tick, but it means
the primitive operation itself receives zero originality credit.

The closest recent scholarly neighbour is again
Bousquet-Mélou--Krattenthaler (2025), whose four cyclic actions move a root
corner around a plane tree and include degree-refined cyclic sieving.  That
root-moving action is not `R`.  Nichols--Pilz--Tóth--Zehmakan,
[*Transition operations over plane
trees*](https://doi.org/10.1016/j.disc.2020.111929), study edge rotations,
edge slides, and compatible simultaneous rotations of geometric spanning
trees; those operations change parenthood/topology and are not child-list
cycles.  Searches for `cyclic shift children at every vertex`, `simultaneous
child-list rotation`, `LCM outdegrees tree action`, and 2025--2026 variants
found no paper stating the displayed finite dynamics.

**Internal subtraction.**  P114 is separated literally: it deletes leaves
and lowers rank, whereas `R` is a bijection on embeddings of a fixed labelled
rooted tree.  Classical simply-generated-tree equations, Lagrange inversion,
and Landau's function are zero-credit tools.

**Strongest objection and terminal gate.**  Once the local operations are
recognized as commuting rotations, every orbit is a diagonal orbit in a
static product of cyclic groups.  The pointwise LCM is immediate, Landau's
function only optimizes a degree partition, and the fixed EGF is the standard
degree-restricted tree equation.  No state-dependent interaction remains.

**Verdict: KILL, 4.8/10.**  The exact spike is retained as a negative control,
but closed period layers would only refine the same mechanical product action.
Do not revive Q02 as a paper candidate.

## Q03. Crossing-count rotor on circular matchings

### Literal map and exact spike

Let `C_n` be perfect matchings of `2n` cyclically labelled points.  Let
`c(M)` be the number of crossing chord pairs and let `rho` rotate all endpoint
labels clockwise once.  Define

\[
K(M)=\rho^{c(M)}M.
\]

Crossing number is rotation-invariant.  If `d(M)` is the size of the ordinary
rotation orbit of `M`, then

\[
\operatorname{per}_K(M)=\frac{d(M)}{\gcd(d(M),c(M))}.
\]

The map is bijective.  For every `n>=3`, the matching
`{(0,2),(1,3),(4,5),(6,7),...}` has one crossing, trivial rotational
stabilizer, and period `2n`, which is maximal.

The pilot also killed two plausible overstatements.  The two diameters of a
quadrilateral cross but form a fixed state, so a crossing need not cause
motion.  Matchings with the same crossing number can have different periods
because their rotational stabilizers differ.

### Two proof routes

1. **Invariant-statistic route.**  Since `c(rho M)=c(M)`, induction gives
   `K^t(M)=rho^{t c(M)}M`.  The period formula and maximal family follow.
2. **Stratum/stabilizer route.**  Decompose `C_n` into the sets `P_{n,k}` of
   matchings with `k` crossings, then into ordinary rotation orbits.  On an
   orbit of size `d`, `K` is addition by `k` in `Z/dZ`.  Burnside and Möbius
   inversion give all cycle counts.

### Fatal owner reduction

Liang--Bowling, [*Cyclic Sieving of
Matchings*](https://arxiv.org/abs/1712.07812), explicitly study the cyclic
group `C_{2n}` acting by rotation on `P_{n,k}`, the matchings with exactly
`k` crossings, and prove cyclic-sieving results for the first crossing
strata.  On every one of their invariant strata,

\[
K|_{P_{n,k}}=\rho^k.
\]

Thus Q03 is not an independent geometric dynamics: it is the disjoint union
of fixed powers of the already studied rotation actions.  The period formula
is the generic orbit--stabilizer formula for those powers.  Recent
2025--2026 searches found further rotation/CSP work on matchings, plane trees,
and unicellular maps, but no fact capable of restoring a residual after this
literal stratum reduction.

**Verdict: KILL, 2.9/10.**  The exact computations are correct, but the whole
claim package is owner-level cyclic-action bookkeeping.

## Q04. Left-greedy complementary flips on a domino strip

- **Phase space:** domino tilings of a `2 by n` rectangle, encoded as
  compositions of `n` with parts `1` (one vertical domino) and `2` (a pair
  of horizontal dominoes).
- **Update:** scan the old composition from left to right.  Replace a part
  `2` by `11`.  Replace the next two parts by `2` when they are `11`.
  Leave an unmatched `1` in place.  Every decision consumes its source
  parts, so the rule is a deterministic maximal set of disjoint `2 by 2`
  face flips.
- **Parameter family:** `n>=0`, with the empty tiling fixed.
- **Early anomaly:** `11 <-> 2`, but
  `12 -> 111 -> 21 -> 111`.  Hence a source can have a genuine transient
  before a two-cycle even though each individual face flip is involutive.
- **Nearest subtraction:** local domino flips, hard-dimer Glauber dynamics,
  greedy maximal matchings on paths, and Fibonacci-cube encodings are all
  zero credit.  Internally P90 and the current rewrite lane S01 are serious
  risks.
- **Two prospective routes:** a finite transducer on the `{1,2}`
  composition; alternatively, alternating-path defects between the current
  path matching and the fixed odd-edge matching.
- **Kill gate:** promote only if a future exact pilot proves a sharp
  unbounded transient and a full recurrent/fibre census not already known
  for greedy complementary matchings.  No such theorem is claimed here.

**Disposition: RESERVE FOR SPIKE, 7.1/10.**

## Q05. Tight-box Ferrers complement

- **Phase space:** partitions fitting an `N by N` square, including the empty
  partition.
- **Update:** fix the empty partition.  For
  `lambda=(lambda_1>=...>=lambda_h>0)`, take the 180-degree rotated complement
  inside its *current tight* `h by lambda_1` rectangle:

  \[
  B(\lambda)=(\lambda_1-\lambda_h,\ldots,
               \lambda_1-\lambda_1),
  \]

  then discard zero parts.
- **Early exact signal:** the number of distinct positive part sizes drops by
  exactly one.  Therefore the absorption depth at the empty partition is
  exactly that number.  For example
  `(4,3,1)->(3,1)->(2)->empty`.
- **Owner/internal subtraction:** complement in a fixed Ferrers rectangle is
  classical; only the repeated tight reboxing is residual.  P113 already
  occupies a sharper partition-depth theorem and P110 occupies partition
  reassembly.
- **Two prospective routes:** track successive distinct part gaps under
  reverse complement; alternatively, trace southeast boundary words and
  delete their two terminal runs after each tight reboxing.
- **Kill:** the clock is a renamed distinct-part count and the fibres are a
  direct reverse-complement reconstruction.

**Disposition: KILL, 4.3/10.**

## Q06. Odd-incidence translation of a simple hypergraph

- **Phase space:** simple `m`-edge hypergraphs `H subseteq 2^[n]`, with the
  empty edge allowed.
- **Update:** let `D(H)` be the vertices having odd hypergraph degree and set
  `J(H)={E triangle D(H):E in H}`.
- **Parameter family:** `n,m>=0` with `m<=2^n`.
- **Early exact signal:** for `v in D(H)` its new degree is
  `m-deg_H(v)`; every other degree is unchanged.  Hence

  \[
  D(J(H))=
  \begin{cases}
    D(H),&m\text{ even},\\
    \varnothing,&m\text{ odd}.
  \end{cases}
  \]

  Thus even `m` gives an involution and odd `m` gives an idempotent.  If
  `m` is odd and `K` is Eulerian, its one-step fibre is its translation
  orbit, of size `2^n/|\operatorname{Stab}(K)|`.
- **Owner/internal subtraction:** generic hypergraph switching, incidence
  column complementation, and Fourier analysis of subset translations are
  zero credit.  The parity-selected switching engine is uncomfortably close
  to C01 and P112.
- **Two prospective routes:** incidence-matrix column complementation;
  translation action of `(Z/2Z)^n` with stabilizer enumeration.
- **Kill gate:** no promotion without a closed stabilizer distribution for
  simple hypergraphs.  The parity dichotomy alone is too short.

**Disposition: RESERVE, 6.8/10.**

## Q07. Turn-parity reflection of primitive lattice excursions

- **Phase space:** balanced words with `n` up-steps and `n` down-steps,
  allowed on both sides of height zero.
- **Update:** split at returns to zero into signed primitive excursions.  In
  every component having an odd number of direction changes, exchange up and
  down throughout that component; retain every even-turn component.
- **Early exact signal:** the return decomposition and turn counts survive
  reflection, so the map is an involution.  Fixed paths are precisely those
  whose primitive excursions all have even turn count.
- **Owner/internal subtraction:** Narayana/turn enumeration and reflection of
  Dyck excursions are standard.  More importantly, this is another
  parity-triggered independent-component involution, too close in proof
  engine to Q01 and in narrative to R2.
- **Two prospective routes:** use unique return-factorization and multiply
  primitive fixed-series; alternatively, pair signed excursions orbitwise
  under reflection and apply Burnside's lemma.
- **Kill:** even if its fixed series is easy, it cannot occupy the same batch
  lane as the stronger tree system.

**Disposition: KILL, 5.2/10.**

## Q08. Major-parity tableau conjugation

- **Phase space:** the disjoint union of standard Young tableaux of all
  shapes of size `n`.
- **Update:** transpose `T` if `maj(T)` is odd; otherwise fix it.
- **Parameter family:** `n>=0`.
- **Early exact signal:** tableau transposition complements the descent set,
  so
  `maj(T^top)=n(n-1)/2-maj(T)`.  If `n(n-1)/2` is even, the odd-major states
  form transpose 2-cycles and the even-major states are fixed.  If it is odd,
  every odd-major state maps in one step to an even-major fixed state.  Thus
  the map alternates between an involution and an idempotent according to
  `n mod 4`.
- **Nearest subtraction:** conjugation, descent complementation, the
  `q`-hook formula at `q=-1`, domino tableaux, and sign-imbalance theory are
  zero credit.  P113 owns partition-shape dynamics but not tableaux.
- **Two prospective routes:** descent-set complementation gives the temporal
  law; root-of-unity hook evaluation can count fixed and absorbed states
  shape by shape.
- **Kill gate:** the statistic-triggered transpose may be judged engineered,
  and the entire census may be an immediate `q=-1` specialization.

**Disposition: RESERVE, 6.4/10.**

## Q09. Least-ear flip on convex triangulations

- **Phase space:** triangulations of a convex polygon with cyclic vertex
  labels `1,...,n`.
- **Update:** for `n=3` fix the unique triangulation.  Otherwise choose the
  ear whose tip has the least label and flip its opposite internal diagonal
  in the adjacent quadrilateral.
- **Early anomaly:** the two quadrilateral triangulations form a 2-cycle.
  The selected ear disappears after its flip, so the scheduler is not an ear
  deletion or a monotone Tamari normalization.
- **Nearest subtraction:** flip graphs, rotation distance, simultaneous
  compatible flips, and deterministic triangulation walks are a dense owner
  field; [Nichols et
  al.](https://doi.org/10.1016/j.disc.2020.111929) are a direct mechanism
  neighbour.  P114 is an internal ear/leaf warning.
- **Two prospective routes:** dual-tree tracking of the least ear; symbolic
  dynamics on the cyclic gap word of ear tips.
- **Kill gate:** kill unless a future census exposes an infinite exact period
  family and a nontrivial basin law.  No temporal conjecture is promoted.

**Disposition: RESERVE, UNSPIKED, 6.0/10.**

## Q10. Convex-layer label rotor

- **Phase space:** bijective labelings of a fixed generic finite planar point
  set `P`.
- **Update:** compute the fixed onion decomposition of `P` and move every
  label one point clockwise on its own convex layer, simultaneously.
- **Parameter family:** point configurations with layer sizes
  `s_1,...,s_r`.
- **Early exact signal:** every state has period
  `lcm(s_1,...,s_r)`.  All fixed-iterate counts are either zero or `|P|!`.
- **Owner/internal subtraction:** this is merely a product of cyclic
  permutation actions on static layers.  Circle actions and finite-subset
  geometry already face P84/P96 pressure.
- **Two prospective routes:** decompose the labeling set into cyclic layer
  torsors; alternatively, view the update as one fixed permutation and read
  its orbit lengths from its disjoint-cycle decomposition.
- **Kill:** there is no state-dependent geometry, fibre theorem, or
  transient.  The geometric language does not make the product action a new
  mechanism.

**Disposition: KILL, 3.6/10.**

## Exact pilot ledger

Exactly the three candidates selected before the hostile search were
piloted.  All scripts are deterministic and use only the Python standard
library.

| candidate | script | exhaustive range | assertions | falsified guesses |
|---|---|---:|---:|---|
| Q01 | `proof_spikes/comb_phase2c_odd_fringe_mirror.py` | all plane rooted trees, orders 1--12; degree-six residual through `x^12` | 247,553 | fixed iff globally mirror-symmetric, in both directions |
| Q02 | `proof_spikes/comb_phase2c_child_rotation.py` | all root-fixed labelled plane trees, orders 1--7; explicit order-8 witness | 1,660,358 | period at most the vertex count |
| Q03 | `proof_spikes/comb_phase2c_crossing_rotor.py` | all circular matchings with 1--7 chords | 1,416,581 | crossing implies motion; crossing number alone determines period |
| **total** |  |  | **3,324,492** |  |

Fresh commands:

```text
python3 docs/papers117_121_sequence/proof_spikes/comb_phase2c_odd_fringe_mirror.py
python3 docs/papers117_121_sequence/proof_spikes/comb_phase2c_child_rotation.py
python3 docs/papers117_121_sequence/proof_spikes/comb_phase2c_crossing_rotor.py
```

All three exited zero.  Enumeration is falsification evidence only; the
infinite statements promoted for Q01--Q03 have the separate arguments given
above.

## Hostile-search boundary for the top three

The owner search used multiple literal and structural formulations:

- `odd subtree size reverse children`, `fringe parity mirror`, `recursive
  ordered-tree involution`, plane-tree/Dyck involutions, and 2025--2026
  variants;
- `cyclic shift every child list`, `simultaneous child rotation`, `local
  rotation group plane tree`, `LCM outdegrees`, and 2025--2026 tree CSP and
  transition-operation literature;
- `rotate chord matching by crossing number`, `matching rotation crossing
  statistic`, `cyclic sieving matchings with k crossings`, chord-diagram
  dynamics, and 2025--2026 variants.

Primary full texts or official pages were read far enough to compare the
literal actions, not only titles.  The search found a fatal stratum-by-stratum
owner for Q03, close but nonliteral involution owners for Q01, and close but
nonliteral root/edge rotation owners for Q02.  Search absence for Q01/Q02 is
bounded as of the audit date.

## Recommended next gate

1. **Promote Q01 internally under `HOLD_EXTERNAL`.**  The required elimination
   and second owner gate are complete.  Keep the claim ceiling at the exact
   theorem package stated above; singular asymptotics remain outside scope.
2. **Permanently kill Q02 and Q03.**  Both are unions/products of static cyclic
   actions, despite their correct exact formulae.
3. **Spike Q04 only if another slot remains.**  The sharp question is whether
   complementary greedy matchings on a path have an unbounded exact transient
   and whether that temporal law is already known.
4. **Permanently kill Q05, Q07, and Q10 in their present forms.**  Do not
   reintroduce them as crossing dynamics, tight Ferrers duality, excursion
   parity, or convex-layer geometry.

This scout authorizes only the internal P120 handoff for Q01.  It does not
authorize a shared-ledger edit, priority claim, external release, or any paper
assignment for Q02--Q10.
