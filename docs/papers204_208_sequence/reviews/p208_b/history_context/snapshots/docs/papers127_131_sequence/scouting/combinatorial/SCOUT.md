# P127--P131 combinatorial/geometric scouting lane

**Status:** internal scouting only; **HOLD EXTERNAL**.  No paper number is
assigned and no candidate is frozen.

**Search and computation snapshot:** 2026-08-31 UTC.

## 1. Scope, exclusions, and decision rule

I first reduced the P001--P126 paper list and the P117--P126 scouting and kill
ledgers to a mechanism firewall.  This pool does not reuse cycle pruning, MIS
polarity, partition shift--join, ordinary peeling/closure, sorting or
0-Hecke, record/run reversal, synchronous mex, odd-component complementation,
Engel/unitriangular reduction, odd-fringe tree mirroring, parity root rotation,
balanced composition refinement, parallel Glaisher compression, finite-field
shears, monomial-ideal colon dynamics, or any symbolic/CA carrier.  A proof
indexing tree is not itself treated as a tree dynamical system.

The breadth pool has **25 literal maps**, spanning order ideals and posets,
set systems and partitions, tableaux and plane partitions, tilings,
hypergraphs and incidence structures, chord and bipartite matchings,
distributive lattices, lattice paths, polyominoes, and graphic-matroid bases.
Every displayed finite range was exhaustively enumerated.  `PROMOTE` below
means only “worth an independent proof/owner gate”; it never means novelty or
paper allocation.  `RESERVE` means a proved theorem spike whose residual is
too close to an occupied mechanism.  All other candidates are killed now.

Current result: **one conditional promotion (MT2), one reserve (PO2), and 23
kills**.  This deliberately stays below the cap of three promotions.

## 2. Exact breadth census: all 25 maps

The fingerprint columns report the union of periods and the largest transient
tail over the stated parameter range.  `I/F` is the last parameter's
image/fixed-point count.  Assertions include phase-space uniqueness, closure,
orbit closure, period positivity, and the complete functional-graph scan.

| ID | Literal phase space and simultaneous update | Exhaustive scope and exact signal | Assertions | Decision and reason |
|---|---|---:|---:|---|
| **PO1** | For an ideal $I$ of the $n$-fence, add all minimal elements of $P\setminus I$ when $|I|$ is even; otherwise delete all maximal elements of $I$. | $1\le n\le12$, 984 states; last $I/F=55/1$; tail 5, periods 1,2. | 9,086 | **KILL.** The hoped-for monotone clock is false, and this is an adaptive alternation of owned up/down boundary operators on an already used fence/rowmotion carrier. |
| **PO2** | For $I\in J([2]\times[m])$, delete all maxima when $|\max I|$ is odd; otherwise add all minimal elements of the complement. | $1\le m\le7$, 119 states; last $I/F=24/0$; tail 6, period 2. | 1,227 | **RESERVE**, with the all-size contract in Section 4.  Both branches are lattice Pop and dual-Pop, so the residual is only the parity scheduler and its triangular-coordinate census. |
| **PO3** | On a labelled poset, take the order dual iff the Hasse cover count is odd. | All labelled posets through $n=4$, 242 states; last $I/F=219/79$; tail 0, periods 1,2. | 1,268 | **KILL.** Cover parity is dual-invariant, so this collapses to a gated classical involution. |
| **SS1** | For an antichain $\mathcal A\subseteq B_n$, complement every member in $[n]$ iff the sum of member ranks is odd. | All Boolean antichains through $n=4$, 197 states; last $I/F=168/96$; tail 1, periods 1,2. | 952 | **KILL.** Only a one-step gate on Boolean complementation; no second theorem engine. |
| **SS2** | Canonically order blocks of a set partition by their minima; cyclically move the minima of all odd-sized blocks one block to the left, leaving other elements in their blocks. | All set partitions through $n=8$, 5,295 states; last $I/F=2839/1556$; tail 5, periods 1--6. | 39,002 | **KILL.** Rich small cycles but no invariant, all-size clock, or fibre recursion survived the cheap attack. |
| **SS3** | Canonically order blocks by minima; cyclically move the maxima of all even-sized blocks one selected block to the right. | All set partitions through $n=8$, 5,295 states; last $I/F=3188/1872$; tail 3, periods 1--4. | 32,056 | **KILL.** Same failure as SS2, with a weaker temporal signal. |
| **SS4** | On an ordered set partition $(B_1,\ldots,B_k)$, rotate the block list left by the number of odd blocks modulo $k$. | All ordered set partitions through $n=6$, 5,316 states; last $I/F=4683/1353$; tail 0, periods 1--5. | 41,646 | **KILL.** Block sizes are invariant; the dynamics is a transparent cyclic group action. |
| **TB1** | Transpose a standard Young tableau iff its descent number is odd; otherwise fix it. | All SYT through size 9, 3,735 states; last $I/F=2620/1320$; tail 1, periods 1,2. | 18,661 | **KILL.** A parity gate on classical conjugation, and close to the prior partition/tableau lane. |
| **TB2** | On a $2\times m$ rectangular SYT, apply rectangular evacuation iff the top-right entry is odd. | $1\le m\le5$, 64 states; last $I/F=32/24$; tail 1, periods 1,2. | 309 | **KILL.** Gated evacuation is theorem-thin and owner-dense. |
| **PP1** | For a plane partition in a $2\times b\times2$ box, apply boxed complement iff the main-diagonal sum is odd. | $1\le b\le4$, 181 states; last $I/F=81/61$; tail 1, periods 1,2. | 874 | **KILL.** Conditional use of an owned complementation involution. |
| **PP2** | Select checkerboard parity equal to the current volume parity and simultaneously toggle each selected entry to `upper + lower - entry`. | Plane partitions in $2\times b\times2$, $1\le b\le4$, 181 states; last $I/F=81/5$; tail 4, periods 1,2. | 1,170 | **KILL.** The nontrivial tail is real, but the update is directly in the plane-partition toggle/gyration neighborhood excluded at breadth stage. |
| **TL1** | Encode a $2\times n$ domino tiling by a composition in 1s and 2s.  Replace each maximal run `11` of length exactly two by `2`, and each maximal run of at least two 2s by the same number of copies of `11`, simultaneously. | $1\le n\le15$, 2,582 states; last $I/F=353/123$; tail 2, fixed eventual period. | 16,745 | **KILL.** A local word morphism/rewrite with direct P126 balanced-composition collision. |
| **TL2** | On domino tilings of a $4\times m$ rectangle, flip vertical/horizontal pairs in every occupied member of a fixed disjoint checkerboard of $2\times2$ cells. | $m=2,4,6$, 322 states; last $I/F=281/13$; tail 0, periods 1,2. | 1,899 | **KILL.** A product of commuting local involutions. |
| **HG1** | On a 3-uniform hypergraph on $[5]$, complement all triples iff an odd number of vertices have degree $1\pmod 3$. | All $2^{10}=1024$ states; $I/F=824/584$; tail 1, periods 1,2. | 4,977 | **KILL.** A statistic-gated global complement with no scalable second engine. |
| **HG2** | Cyclically relabel the currently odd-degree vertices in increasing order, fixing all other labels. | All 3-graphs on $[5]$; $I/F=1024/314$; tail 0, periods 1--5. | 6,777 | **KILL.** Odd-degree membership is transported by the relabelling, so all cycles are imposed label-rotation cycles. |
| **HG3** | Scan 4-sets lexicographically; for the first one spanning exactly 1 or 3 triples, toggle all four of its triples and stop. | All 3-graphs on $[5]$; $I/F=576/64$; tail 1, periods 1,2. | 6,913 | **KILL.** Lexicographic tie-breaking dominates the construction; the finite signal is only a gated involution. |
| **HG4** | On an $n\times n$ binary incidence matrix, transpose iff the number of odd row sums is odd. | $1\le n\le3$, 530 states; last $I/F=512/288$; tail 0, periods 1,2. | 2,579 | **KILL.** The gate is transpose-invariant; pure involution. |
| **MT1** | For every crossing-graph component that is exactly $K_2$, replace its four endpoints by the two consecutive pairs in their induced order; leave every other component unchanged. | Rooted chord matchings through 6 chords, 11,464 states; last $I/F=8696/8696$; tail 1, fixed eventual period. | 49,748 | **KILL behind MT2.** Idempotence and the adjacent-target fibres $1,2,4,9,21,51,127$ (Motzkin) are consequences of the same component decomposition, with less coverage than MT2. |
| **MT2** | In each crossing-graph component of a rooted chord matching, sort its endpoints and replace that component by consecutive pairs, simultaneously. | Rooted chord matchings through 6 chords, 11,464 states; last $I/F=132/132$; tail 1, fixed eventual period. | 68,398 | **PROMOTE TO OWNER/PROOF GATE**, conditionally.  Exact all-size fibre contract is in Section 3; all generic component and transform results receive zero credit. |
| **MT3** | Form the graph joining nested chords; in every component replace the induced endpoints by the rainbow matching. | Rooted chord matchings through 6 chords, 11,464 states; last $I/F=1707/1707$; tail 1, fixed eventual period. | 64,628 | **KILL.** Another one-step canonical reduction, without MT2's clean Catalan image and local fibre transform. |
| **MT4** | For an ordered pair of bipartite perfect matchings $(p,q)$, form $q^{-1}p$ and swap the two colours on every odd cycle. | All pairs through size 4, 617 states; last $I/F=576/384$; tail 0, periods 1,2. | 2,880 | **KILL.** Cycle decomposition makes this a product involution. |
| **LT1** | On a fence ideal lattice, send $I$ to its pseudocomplement $\{x:\downarrow x\cap I=\varnothing\}$. | Fences through $n=12$, 984 states; last $I/F=64/0$; tail 1, period 2. | 7,380 | **KILL DIRECT.** Pseudocomplement/double-negation behavior is standard Heyting-lattice structure, not a residual dynamical mechanism. |
| **LP1** | Reverse the E/N step word of an $(a,b)$ rectangle path iff its area is $1\pmod3$. | $1\le a,b\le5$, 912 states; last $I/F=168/168$; tail 1, periods 1,2. | 4,235 | **KILL.** Conditional reversal only; no intrinsic iterative clock. |
| **GE1** | Reflect a nonempty connected fixed-grid polyomino horizontally iff its edge perimeter is $1\pmod3$. | Grids $3\times2,3\times3,3\times4$, 1,384 states; last $I/F=1126/764$; tail 0, periods 1,2. | 6,415 | **KILL.** Perimeter is reflection-invariant, hence a gated symmetry. |
| **MA1** | For a spanning tree of $K_n$ with odd leaf count, add the lexicographically first nonedge and delete the lexicographically largest edge on the created cycle; fix even-leaf trees. | $2\le n\le5$, 145 states; last $I/F=77/65$; tail 3, fixed eventual period. | 760 | **KILL.** The descent signal depends on arbitrary labels/ties, and graphic-basis exchange is an occupied matroid mechanism. |

Breadth enumeration covered **66,549 parameter-labelled states** and made
**390,585 assertions**.

## 3. MT2 conditional promotion: rooted crossing-component planarisation

### 3.1 Literal map and claim ceiling

Use a linearly ordered endpoint set $[2n]=\{1,\ldots,2n\}$; equivalently,
use a labelled circular chord diagram with a fixed cut before endpoint 1.  Two
chords are adjacent in the crossing graph when their endpoints alternate.  If
$K$ is a crossing-graph component with ordered endpoint set
$s_1<\cdots<s_{2k}$, replace all chords of $K$ by
$(s_1,s_2),(s_3,s_4),\ldots,(s_{2k-1},s_{2k})$.  Do this for all components.
This rooted convention is essential: the map is **not** equivariant under
moving the cut.

The admissible theorem contract is the following, and no asymptotic or
priority claim is included.

1. **Image and dynamics.**  The map $\Phi_n$ is idempotent.  Its image and
   fixed set are exactly the noncrossing matchings, hence both have size
   $\operatorname{Cat}_n$.  Every nonfixed point has depth one, there are
   $(2n-1)!!-\operatorname{Cat}_n$ Garden states, and the fixed-$n$ zeta is
   $(1-z)^{-\operatorname{Cat}_n}$.
2. **Local inverse specification.**  Give a noncrossing target $T$ its
   nesting forest, with a virtual root.  For every vertex $v$ (including the
   root), independently take a noncrossing partition of the ordered list of
   the $d_T(v)$ immediate children, and decorate each block of size $k$ by a
   crossing-connected $k$-chord diagram.  Re-pairing the endpoints according
   to the decorations is a bijection onto $\Phi_n^{-1}(T)$.
3. **Pointwise fibre product.**  Let $c_k$ count crossing-connected
   $k$-chord diagrams and define
   
   \[
     C(u)=\sum_{k\ge1}c_k u^k,\qquad
     A(u)=\sum_{k\ge0}a_k u^k=1+C\bigl(uA(u)\bigr).
   \]
   
   Then
   
   \[
     |\Phi_n^{-1}(T)|=
     \prod_{v\in V(T)\cup\{\widehat0\}}a_{d_T(v)}.
   \]
   
   Equivalently,
   $a_d=\sum_{\pi\in NC(d)}\prod_{B\in\pi}c_{|B|}$.
4. **Sharp largest fibre.**  Concatenation injects
   $\mathcal A_i\times\mathcal A_j$ into $\mathcal A_{i+j}$, and a
   one-block connected decoration lies outside its image; hence
   $a_i a_j<a_{i+j}$ for $i,j>0$.  Since the child degrees in a nesting
   forest sum to $n$, the unique largest fibre is over the consecutive-pair
   matching $(1,2)(3,4)\cdots(2n-1,2n)$ and has size $a_n$.
5. **Exact initial census.**  The connected counts and largest fibres begin
   
   \[
   (c_1,\ldots,c_7)=(1,1,4,27,248,2830,38232),
   \]
   
   \[
   (a_0,\ldots,a_7)=(1,1,2,8,52,464,5184,68928).
   \]

There are two proof routes.  The direct route takes the noncrossing endpoint
partition formed by crossing components, applies the consecutive-pair section,
and proves the sibling-list inverse lemma.  The second route recursively cuts
at the outermost target chords; the ordered child lists independently carry
the noncrossing-partition transform, and induction yields the same product.

### 3.2 Counterexample pressure and exact control

The focused pilot exhausts every rooted chord matching through $n=7$:
146,599 sources and 625 noncrossing targets.  It checked image membership,
idempotence, the Catalan image count, the fibre formula for **every** target,
the consecutive and rainbow extremes, the unique pilot maximizer, and total
fibre mass.  It made **293,872 assertions**.

Small counterexamples prevent overstatement:

- fibre size is not a function of $n$: at $n=2$ the consecutive target has
  fibre 2 while the rainbow target has fibre 1;
- the map is not rotation-equivariant: the 2-chord crossing is rotation
  invariant, while its chosen consecutive-pair image is not;
- the relevant transform is $A=1+C(uA)$, not the owned full-diagram equation
  $D=1+C(uD^2)$;
- there is no nontrivial transient hierarchy or cycle theorem: the map is
  genuinely one-step idempotent.

### 3.3 Owner subtraction and internal collision firewall

Owner risk is **high**, but the bounded search did not locate the literal
consecutive-pair section together with its target-wise fibre product.
Everything in the following list is zero-credit:

- Kreweras's [noncrossing closure of a partition](https://doi.org/10.1016/0012-365X(72)90041-6)
  owns the closure operation and the noncrossing-partition lattice.
- Flajolet and Noy,
  [*Analytic Combinatorics of Chord Diagrams*](https://algo.inria.fr/flajolet/Publications/FlNo00.pdf),
  DOI [10.1007/978-3-662-04166-6_17](https://doi.org/10.1007/978-3-662-04166-6_17),
  own crossing components, their enumeration, and
  $D=1+C(uD^2)$.
- Nabergall's primary Waterloo dissertation,
  [*Enumerative perspectives on chord diagrams*](https://uwspace.uwaterloo.ca/items/51239c85-b044-4e6b-97c6-710332c37c93),
  explicitly owns the bijection between a chord diagram and a noncrossing
  partition of its endpoints into even blocks decorated by connected chord
  diagrams.  This is the closest structural owner and must be cited as such.
- Acan,
  [*On a uniformly random chord diagram and its intersection graph*](https://arxiv.org/abs/1501.01489),
  DOI [10.1016/j.disc.2016.11.004](https://doi.org/10.1016/j.disc.2016.11.004),
  owns the intersection-graph language and component statistics.
- Callan,
  [*Sets, Lists and Noncrossing Partitions*](https://cs.uwaterloo.ca/journals/JIS/VOL11/Callan/callan412.html),
  owns the generic noncrossing-partition transform, including the functional
  equation form used for $A$.
- Alman, Lian, and Tran,
  [*The uncrossing partial order on matchings is Eulerian*](https://arxiv.org/abs/1406.5671),
  DOI [10.1016/j.jcta.2015.04.004](https://doi.org/10.1016/j.jcta.2015.04.004),
  own the matching uncrossing poset and its Catalan minimal elements.  Their
  local resolutions are not this componentwise deterministic section.
- Young,
  [*Linear k-Chord Diagrams*](https://cs.uwaterloo.ca/journals/JIS/VOL23/Young/young5.html),
  owns short-chord and short-component enumeration.  The 2026 primary
  neighbor
  [*Methods for Analyzing RNA Pseudoknots via Chord Diagrams and Intersection Graphs*](https://doi.org/10.1007/s11538-026-01646-y)
  owns no matching-to-matching temporal map located in this audit.

The only residual proposed for a later gate is the conjunction: the literal
rooted map, the sibling-list inverse bijection, the target-wise product, and
its exact extremal fibre.  Generic connected counts, Catalan image counts,
noncrossing closure, the transform itself, and uncrossing theory are not
contributions.

Internally, this is not P105/P117/P122 word or run dynamics, P106 MIS
polarity, P114/P120 tree dynamics, P118 mex, P123 graph complementation, or
P126 composition refinement.  The nesting forest is only a proof coordinate.
It does share the chord carrier with the killed local crossing rotor and with
the earlier P122--P126 odd-component reflection reserve; this is a real
scope-risk, recorded rather than hidden.

**Verdict:** score **7.8/10, PROMOTE_TO_INDEPENDENT_PROOF_AND_OWNER_GATE**.
Kill immediately if a source owns the consecutive-pair section or the
pointwise nesting-forest fibre theorem, or if the next gate regards a
one-step canonicalisation as insufficient paper value.

## 4. PO2 reserve: frontier-parity wave on $J([2]\times[m])$

Write an ideal as row lengths $(a,b)$ with $0\le b\le a\le m$.  Directly from
the literal boundary rule,

\[
\Phi_m(a,b)=
\begin{cases}
(1,0),&(a,b)=(0,0),\\
(a-1,0),&b=0<a,\\
(a,a-1),&a=b>0,\\
(a+1,b+1),&0<b<a<m,\\
(m,b+1),&0<b<a=m.
\end{cases}
\]

This gives a genuine all-size theorem spike, not an extrapolation from the
enumeration:

1. For $m\ge2$ the recurrent set consists of exactly the two 2-cycles
   $\{(0,0),(1,0)\}$ and $\{(m,m-1),(m,m)\}$; for $m=1$ only the first remains.
2. For $m\ge3$, the pointwise depth is
   
   \[
   \tau(a,b)=
   \begin{cases}
   0,&(a,b)\text{ recurrent},\\
   a-1,&b=0,\\
   1,&(a,b)=(1,1),\\
   m-a+1,&a=b\ge2,\\
   m-b-1,&0<b<a.
   \end{cases}
   \]
   
   Thus $\max\tau=m-1$, with exactly the witnesses $(m,0)$ and $(2,2)$.
3. The depth layers for $m\ge3$ have sizes $4$ at depth 0, $4$ at depth 1,
   $d+3$ at $2\le d\le m-2$, and $2$ at depth $m-1$.
4. For $m\ge3$, the numbers of targets of indegree $0,1,2,3$ are
   
   \[
   2m-2,\quad \frac{m^2-5m+14}{2},\quad 2m-6,\quad 2,
   \]
   
   so $|\operatorname{Im}\Phi_m|=(m^2-m+6)/2$ and the maximum one-step
   indegree is 3.
5. The fixed-$m$ zeta is $(1-z^2)^{-2}$ for $m\ge2$ (and
   $(1-z^2)^{-1}$ for $m=1$).

The first proof route is case-by-case arithmetic on the five coordinate
branches.  The second draws the triangular coordinate grid: the functional
graph is two directed 2-cycles with explicit incoming diagonal and boundary
chains, from which layers and indegrees follow by counting lattice points.

The focused control first compared the coordinate rule with the literal ideal
map for every ideal through $m=8$, then checked all formulas through $m=250$:
2,667,125 triangular states and **8,003,445 assertions**.  Boundary pressure is
explicit: $m=1$ has only one 2-cycle, $m=2$ does not have the two claimed sharp
witnesses, and the theorem is not asserted for $[r]\times[m]$ with $r>2$.
Idempotence and a unique attractor are already false in the smallest cases.

The owner subtraction is unfavorable:

- Cameron and Fon-Der-Flaass,
  [*Orbits of antichains revisited*](https://doi.org/10.1016/0195-6698(95)90036-5),
  own the foundational order-ideal/antichain dynamics.
- Striker and Williams,
  [*Promotion and Rowmotion*](https://arxiv.org/abs/1108.1172), and Striker,
  [*Rowmotion and generalized toggle groups*](https://arxiv.org/abs/1601.03710),
  own the toggle framework and rowmotion neighborhood.
- Propp and Roby,
  [*Homomesy in products of two chains*](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v22i3p4/pdf/),
  DOI [10.37236/3579](https://doi.org/10.37236/3579), own the detailed
  $J([a]\times[b])$ rowmotion setting.
- Defant and Williams,
  [*Semidistrim Lattices*](https://arxiv.org/abs/2111.08122), DOI
  [10.1017/fms.2023.46](https://doi.org/10.1017/fms.2023.46), own lattice Pop,
  dual Pop, and their relation to rowmotion.  On $J(P)$ the two branches here
  are exactly “remove all maxima” Pop and “add all complement minima” dual Pop.
- Lafrenière, Lewis, McNicholas, Striker, and Welch,
  [*Interval-closed set rowmotion and homomesy on products of two chains*](https://arxiv.org/abs/2505.04000),
  completely describe a different rowmotion on $[2]\times[n]$ and are the
  closest 2025 carrier-specific neighbor.  The 2026 primary presentation
  [*Rowmotion and Echelonmotion*](https://personal.utdallas.edu/~nxw170830/docs/FPSAC2026/)
  further confirms how saturated the down/up-data neighborhood is.

All general order-ideal, toggle, Pop/dual-Pop, product-of-chains, and
rowmotion facts are zero-credit.  Only the state-dependent parity scheduler
and the five formulas above remain.  That residual is exact but too narrow and
too close to the explicit poset/toggle exclusion to promote now.

**Verdict:** score **6.2/10, RESERVE_ONLY / near-kill**.  A direct adaptive
Pop/dual-Pop owner, or a policy ruling that a solved triangular coordinate
wave is not a distinct mechanism, kills it.  It must not displace MT2.

## 5. Owner-search log (bounded, primary-source only)

Searches were run on 2026-08-31 with literal and structural variants, including
2025--2026 filters.  Representative strings were:

- `"crossing component" chord diagram adjacent pairs normalization`;
- `chord diagram component planarization map fibres`;
- `"noncrossing closure" perfect matching dynamics`;
- `uncrossing map chord diagrams noncrossing matchings`;
- `"A(z)=1+C(zA(z))" chord diagrams`;
- `2025 2026 chord diagram connected component intersection graph`;
- `order ideal remove all maximal add all minimal complement dynamics`;
- `number of maximal elements parity order ideal dynamics`;
- `pop-stack operator distributive lattice order ideals remove maximal`;
- `2025 2026 rowmotion product of two chains parity`.

The audit read the direct technical sources linked in Sections 3.3 and 4,
including the explicit structural lemma in Nabergall rather than relying on a
search snippet.  No bounded query found MT2's exact deterministic section plus
target-wise fibres, or PO2's exact adaptive parity scheduler.  These are
**bounded non-hits only**.  They are not novelty or priority statements.

## 6. Falsified guesses and permanent local kills

- “Adaptive involution gates stay involutions” failed for SS1, TB1, TB2,
  PP1, and LP1: each can have a one-step transient.
- “The plane-partition parity toggle is periodic from time zero” failed:
  PP2 has tail 4 in the small box family.
- “The set-partition extrema rotors are products of fixed cycles” failed:
  SS2 has tail 5 and periods 1--6; nevertheless no proof-scale invariant
  appeared.
- “The first crossing normalization has a nontrivial clock” failed twice:
  MT1 and MT2 are idempotent.
- “Pseudocomplementation converges to a fixed ideal” failed on fences: LT1
  reaches 2-cycles.
- “Greedy basis exchange is one-step” failed: MA1 reaches tail 3, but its
  label dependence makes that signal nonintrinsic.
- For MT2, the guesses “rotation-equivariant” and “uniform fibre” fail at two
  chords.  For PO2, “one recurrent class” and “idempotent” fail immediately.

The 23 `KILL` rows above are not to be recycled in this sequence without a new
carrier or a theorem engine not present here.  In particular, MT1/MT3 must not
be used as weaker chord-diagram substitutes for MT2, and PO1 must not be used
as a fence version of PO2.

## 7. Reproducibility and exact totals

Only Python's standard library is used.  Canonical byte comparisons pass:

```sh
python3 docs/papers127_131_sequence/scouting/combinatorial/pilot_breadth.py \
  | cmp - docs/papers127_131_sequence/scouting/combinatorial/pilot_breadth_output.txt
python3 docs/papers127_131_sequence/scouting/combinatorial/pilot_contracts.py \
  | cmp - docs/papers127_131_sequence/scouting/combinatorial/pilot_contracts_output.txt
```

| File | Purpose | Assertions | SHA-256 |
|---|---|---:|---|
| `pilot_breadth.py` | all 25 functional-graph scans | 390,585 | `c7b479f02f8298ad14ed3c96217aa8acdf2864ad40c33856fe9613b07410be1e` |
| `pilot_breadth_output.txt` | canonical breadth stdout | -- | `f61c888150e328f81045312bd1eb79bc4cd0fe525aa60e94e1aca240a646a2d9` |
| `pilot_contracts.py` | PO2 all-size-formula stress and MT2 target-fibre exhaustion | 8,297,317 | `9cdbd94b96e341909e4a0abcf886e3702b39c9bcc281c28251236ed49d9bb477` |
| `pilot_contracts_output.txt` | canonical focused stdout | -- | `d95baeaaeb674827c6b116a2d4a788d77574b4761acb1bfee7635b40a7e3e542` |
| **Total** | breadth plus focused controls | **8,687,902** | -- |

The scripts are verification evidence, not proofs of the all-size statements.
The all-size arguments are the component/sibling-list bijection for MT2 and
the explicit five-branch coordinate analysis for PO2.

## 8. Ranked handoff

1. **MT2 rooted crossing-component planarisation — conditional PROMOTE,
   7.8/10.**  Exact signal: idempotent Catalan image, pointwise
   nesting-forest fibre product, and unique largest fibre $a_n$ with
   $A=1+C(uA)$.  Owner risk is high because the component decomposition and
   transform are directly owned; the residual conjunction must survive an
   independent hostile gate.
2. **PO2 frontier-parity wave — RESERVE_ONLY, 6.2/10.**  Exact signal: two
   2-cycles, sharp depth $m-1$, complete layer and indegree censuses, and
   zeta.  Owner/internal-policy risk is very high: its two branches are owned
   Pop/dual-Pop on the explicitly saturated $J([2]\times[m])$ carrier.

No third candidate clears both the theorem and collision gates.  External
status remains **HOLD**.
