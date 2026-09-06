# Combinatorial breadth scout: bounded owner and priority search

**Search date:** 2026-09-02 UTC  
**Scope:** the four strongest pre-search candidates from the 18-system breadth
screen  
**External state:** `HOLD_EXTERNAL`

This is a bounded priority screen, not a novelty certificate.  A search nonhit
is recorded only as a nonhit.  It is never treated as evidence that a statement
is new.  Conversely, a source owning the literal update or its decisive proof
engine is enough to kill a candidate even when the scout found an unrecorded
minor corollary.

The query frontier was deliberately small: exact rule phrases first, then the
closest established vocabulary, with arXiv, journal DOI pages, and official
proceedings preferred.  No candidate text was sent to an outside model and no
external repository state was changed.

## 1. `LCP`: delete the whole leftmost-child subtree at every plane-tree vertex

### Queries

```text
plane tree delete leftmost child subtree iteration pruning ordered tree leftmost child
ordered rooted tree pruning first child subtree generating function preimages
site:arxiv.org plane trees pruning leftmost child old path subtree
"delete the leftmost" "plane tree" subtree
"leftmost child subtree" pruning tree
```

### Primary and authoritative hits

1. Benjamin Hackl, Clemens Heuberger, Sara Kropf, and Helmut Prodinger,
   [*Fringe Analysis of Plane Trees Related to Cutting and
   Pruning*](https://arxiv.org/abs/1704.01095), Aequationes Mathematicae 92
   (2018), 311--353, journal DOI
   [10.1007/s00010-017-0529-0](https://doi.org/10.1007/s00010-017-0529-0).
   The paper directly studies repeated deterministic reductions of plane trees:
   cutting all leaves, maximal leaf-ended paths, leftmost (old) leaves, and
   leftmost-child maximal paths.  It also develops inverse expansion operators
   and exact/asymptotic survivor statistics.  This owns the broad vocabulary
   "leftmost pruning", fixed-time iteration, and generating-function expansion.

   It does **not** define the literal scout rule
   `L(T_1,...,T_k)=(L(T_2),...,L(T_k))`.  Its old-leaf rule deletes a leftmost
   child only when that child is a leaf; its old-path rule deletes maximal
   leaf-ended paths all of whose vertices are leftmost children.  Neither rule
   deletes the *entire current first-child subtree at every vertex*.  The source
   also does not state the sibling-bottleneck pointwise clock or the
   target-resolved product `z T(z)^t product_i P_{t,U_i}(z)` found here.

2. William Y. C. Chen, Emeric Deutsch, and Sergi Elizalde,
   [*Old and young leaves on plane trees*](https://arxiv.org/abs/math/0410127).
   This is a direct static owner for the term "old leaf" and for enumerating
   leftmost-child leaves.  It supplies no whole-subtree iteration, clock, or
   target preimage series.

3. Sen-Peng Eu, Seunghyun Seo, and Heesung Shin,
   [*Enumerations of vertices among all rooted ordered trees with levels and
   degrees*](https://arxiv.org/abs/1605.00715), Discrete Mathematics 340 (2017),
   2123--2129, DOI
   [10.1016/j.disc.2017.04.007](https://doi.org/10.1016/j.disc.2017.04.007).
   This statically enumerates first children/non-first children with level and
   degree refinements.  It owns those static statistics, not the scout update.

### Subtraction and priority decision

All generic Catalan enumeration, symbolic plane-tree equations, leftmost-leaf
terminology, pruning language, and the idea of an inverse expansion operator
receive zero credit.  The residual is unusually crisp: whole-first-subtree
deletion, the exact `t`-iterate formula, the minimum-child-index path clock, and
every-target all-time inverse products.  No direct owner for that conjunction
was retrieved inside the bounded frontier.

**Decision:** `PASS_OWNER_THIN__SELECT_FOCUSED`.  This is the highest-priority
candidate, but a focused search must inspect citations around old-path pruning
before any freeze.

## 2. `PAE`: retain position/value parity agreements and standardize

### Queries

```text
permutation retain positions values same parity standardization parity agreement
permutations parity succession position value parity preserving extraction
"same parity" position value permutation standardize subsequence
"parity agreement" permutation extraction
site:arxiv.org parity alternating permutations position value same parity
"parity-alternating permutations" odd positions odd entries
```

### Primary hits

1. Frether Getachew Kebede and Fanja Rakotondrajao,
   [*Parity alternating permutations starting with an odd
   integer*](https://arxiv.org/abs/2101.09125), Enumerative Combinatorics and
   Applications 1:2 (2021), DOI
   [10.54550/ECA2021V1S2R16](https://doi.org/10.54550/ECA2021V1S2R16).
   Their PAPs start odd and alternate parity, hence are exactly the same-rank
   fixed states `pi_i congruent i (mod 2)` of the scout map.  The source owns
   the class name and static enumeration/statistics.  It does not define an
   extraction-and-standardization map, iterate it, characterize target image
   ranks, or give target fibres.

2. Shinji Tanimoto,
   [*Combinatorial study on the group of parity alternating
   permutations*](https://arxiv.org/abs/0812.1839).  This is an earlier static
   owner for the full parity-alternating group and ascent/inversion statistics.
   It again supplies no rank-changing extraction dynamics.

The exact-rule queries did not retrieve a source defining
`std(pi_i : i congruent pi_i mod 2)`.  That is a bounded nonhit only.

### Internal owner/collision subtraction

The external nonhit does not resolve the more serious portfolio collision.
P156 also retains a subword according to an absolute position/value predicate
and standardizes it; P149 is another selected-subword standardization map.  The
generic carrier, standardization, rank monotonicity, selected-position/value
matching, and factorial completion language therefore receive zero credit.
The earlier binary parity sieve in the P152--P156 root scout also removes
parity-mismatched coordinates, although it has a word rather than permutation
carrier.

The candidate survives only provisionally because its residual proof objects
are different: every nonfixed loss is even; the fixed locus is a large Young
subgroup rather than identities; target feasibility is a simultaneous embedding
of two balanced binary parity words; and rank eight is the first obstruction to
the naive `m+2` image rule (732 targets need rank `m+4`).

**Decision:** `SELECT_PROOF_AND_COLLISION_GATE`, below `LCP`.  It must be killed
if the exact target-threshold/fibre theorem reduces to P156 after a routine
two-colour substitution, or if the permanent "selector changed only by parity"
firewall is judged controlling.  No paper freeze is authorized here.

## 3. `CCQ`: quotient by connected components of the crossing graph

### Queries

```text
site:arxiv.org set partition crossing graph connected components noncrossing partition
"crossing graph" "set partition" connected
set partitions connected components crossing relation noncrossing decomposition
"components of the crossing graph" set partition noncrossing
"crossing-connected components" set partitions
"noncrossing closure" "crossing graph" partition
```

### Direct owner hit

Germain Kreweras,
[*On the noncrossing partitions of a cycle*](https://www.math.utah.edu/~earnshaw/research/kreweras.pdf)
(English translation of the foundational 1972 paper), defines the noncrossing
closure of a partition by making the original blocks vertices of a graph,
joining crossing blocks, and merging each connected component.  The source also
proves the closure is the finest/noncrossing coarsening in the appropriate
order.  This is the decisive mechanism of `CCQ`; writing component membership
as an RGF on block indices changes the output carrier but not the owned closure
operation.

Matthieu Josuat-Verges,
[*Cumulants of the q-semicircular law, Tutte polynomials, and
heaps*](https://arxiv.org/abs/1203.3157), Canadian Journal of Mathematics 65
(2013), 863--878, DOI
[10.4153/CJM-2012-042-9](https://doi.org/10.4153/CJM-2012-042-9), explicitly
defines the crossing graph of a set partition and calls a partition connected
when that graph is connected.  This owns the connected-crossing vocabulary and
Tutte-polynomial apparatus.

The bounded search did not retrieve the scout's auxiliary minimum-ground-set
formula `2m-s_1(rho)` for realizing a target component RGF `rho`.  That residual
does not rescue a paper whose literal central operation is the classical
noncrossing closure.

**Decision:** `KILL_DIRECT_OWNER`.  Keep the exact finite check only as a
negative-control record.

## 4. `ILP`: degree-at-most-one peeling of permutation inversion graphs

### Queries

```text
site:arxiv.org permutation graph k-core leaf pruning
"permutation graph" "2-core"
inversion graph iterative delete degree one vertices permutation
permutation graphs core decomposition
site:arxiv.org k-core decomposition repeatedly remove vertices degree less than k permutation graph
```

### Direct mechanism hits

1. Stephen B. Seidman, *Network structure and minimum degree*, Social Networks
   5 (1983), 269--287, DOI
   [10.1016/0378-8733(83)90028-X](https://doi.org/10.1016/0378-8733(83)90028-X),
   is the foundational owner of graph `k`-cores.

2. Vladimir Batagelj and Matjaz Zaversnik,
   [*An O(m) Algorithm for Cores Decomposition of
   Networks*](https://arxiv.org/abs/cs/0310049), explicitly attributes the
   core notion to Seidman and gives the standard core-decomposition algorithm.

3. Jose Ignacio Alvarez-Hamelin, Luca Dall'Asta, Alain Barrat, and Alessandro
   Vespignani,
   [*k-core decomposition: a tool for the visualization of large scale
   networks*](https://arxiv.org/abs/cs/0504107), describes the decomposition as
   recursive pruning of the least-connected vertices.

For `k=2`, repeatedly deleting vertices of current degree below two is exactly
the scout update on the inversion graph.  Restricting the input to permutation
graphs and translating surviving vertices back to a standardized permutation
does not alter that core algorithm.

**Decision:** `KILL_DIRECT_OWNER`.  Fixed-state or shell-depth enumeration for
permutation graphs could be a separate static problem, but it cannot be sold as
a new finite dynamics system in this portfolio.

## Priority summary

| candidate | direct external owner? | decisive internal collision | bounded decision |
|---|---:|---|---|
| `LCP` | no exact-rule hit; close plane-tree pruning owners | P114 leaf peeling; P148 level contraction | `PASS_OWNER_THIN__SELECT_FOCUSED` |
| `PAE` | no exact-rule hit; fixed class directly owned | P149/P156 subword standardization; earlier parity sieve | `SELECT_PROOF_AND_COLLISION_GATE` |
| `CCQ` | yes, Kreweras noncrossing closure | partition closure/pruning exclusion | `KILL_DIRECT_OWNER` |
| `ILP` | yes, generic 2-core pruning | generic graph pruning exclusion | `KILL_DIRECT_OWNER` |

The search leaves exactly two items worth additional internal work.  This log
does not assign either item a paper number and does not authorize external
release.
