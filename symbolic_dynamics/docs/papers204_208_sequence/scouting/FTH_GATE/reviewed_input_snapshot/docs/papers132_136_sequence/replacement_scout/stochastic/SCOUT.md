# Replacement stochastic/asynchronous scout: twenty owner-gated systems

**Audit date:** 2026-08-31 UTC  
**Scope:** replacement discovery only; no paper number and no Git action  
**Literal systems:** 20  
**Final disposition:** **zero paper-scale promotions**, two owner-heavy reserves,
and eighteen permanent kills

This is an intentionally negative result.  The cleanest finite signal, `BR1`,
is the least difunctional closure of a binary relation followed by a standard
connected-spanning-subgraph enumerator.  The second clean signal, `FG1`, is
ordinary affine-matroid closure followed by Möbius inversion on its flat
lattice.  Both are useful coordinates and neither survives the paper-value
gate.  No bounded search miss is used as novelty or priority evidence.

## 1. Breadth and exact executable contract

[`verify_replacement_stochastic.py`](verify_replacement_stochastic.py)
enumerates the complete finite ranges in the ledger below.  All probabilities
are `fractions.Fraction`; all other quantities are Python integers.  There is
no floating point, pseudorandom sampling, third-party package, network access,
seed, or timestamp.  A listed stochastic rule is uniform over the currently
active **labelled events** emitted by its successor function; two distinct
events leading to the same next state retain their multiplicity.

The frozen stdout is [`CANONICAL.txt`](CANONICAL.txt).  Reproduce it from this
directory with

```bash
cmp -s CANONICAL.txt <(PYTHONDONTWRITEBYTECODE=1 python3 verify_replacement_stochastic.py)
```

The run covers **142,937 parameter-labelled inputs** and makes **591,170 exact
assertions**: 591,167 belong to individual systems and three are global
system-count/handle/nonempty sentinels.  Finite enumeration is falsification
evidence, not a proof or owner certificate.

The 20 definitions were compared literally against all 117 systems in the
first four P132--P136 scout lanes and against the occupied P1--P131 maps.  No
row below is a parameter relabelling of one of those systems.  The pool avoids
exclusion/ASEP and k-mers, generic coalescents, tree pruning, ordinary random
walks, sorting/carrying, and waiting-time wrappers.  Several classical
processes are retained as negative controls because the earliest exact signal
is itself what triggers their kill.

## 2. Permanent twenty-system ledger

| ID | Literal finite process and audited statistic | Complete finite range; exact assertions | Hostile disposition |
|---|---|---:|---|
| `BR1` | A state is a bipartite relation.  If a `2 x 2` submatrix has exactly three ones, add its missing one; choose any active corner.  Audit terminal, all schedule lengths, uniform-active mean, and every target depth fibre. | All relations in `K_(2,2)`, `K_(2,3)`, `K_(3,3)`, `K_(3,4)`; 4,688 inputs; 20,032 assertions. | All 640 target polynomials factor into connected-bipartite reliability polynomials; maximum depth 6 and fibre 1,795.  **`RESERVE_COORDINATE_LEMMA_OWNER_HEAVY`**, not a paper candidate. |
| `BR2` | In a three-one rectangle, delete the one opposite the missing corner; choose the labelled active rectangle uniformly.  Audit exact terminal law and possible clocks. | `K_(2,3)`, `K_(3,3)`; 576 inputs; 2,304 assertions. | 243 nonconfluent and 159 variable-clock sources, at most 13 terminals.  **Kill.** |
| `FG1` | For `S subset AG(d,2)`, whenever three points of an affine parallelogram are present, adjoin the fourth.  Audit terminal, clock, and every affine-flat fibre by depth. | Every subset for `d=1,2,3`; 276 inputs; 964 assertions. | Terminal is affine span; all 68 fibres equal the affine-flat Möbius formula, maximum fibre 149.  **`RESERVE_CLASSICAL_AFFINE_CLOSURE`** as a control only. |
| `FG2` | From a full affine two-plane in `AG(3,2)`, choose a plane-and-point event and delete that point uniformly. | All 256 subsets; 1,024 assertions. | 107 nonconfluent sources and as many as 56 cap-set terminals.  The clock happens to be fixed by matroid nullity, but the terminal law has no closed atlas.  **Kill.** |
| `FG3` | On the Fano plane, complete any line containing exactly two selected points. | All 128 point sets; 416 assertions. | Exactly projective-span closure; 16 flat fibres are subspace-Möbius polynomials.  **Kill direct matroid closure.** |
| `FG4` | In the Fano matroid, choose a contained circuit and one of its elements uniformly and delete it. | All 128 subsets; 1,508 assertions. | Rank/span and nullity clock are fixed, but 71 sources reach multiple bases and there are up to 28 terminals.  **Kill classical random basis reduction.** |
| `HG1` | In a 3-uniform hypergraph, add the fourth face when exactly three faces of a tetrahedron boundary are present. | Every 3-graph on 4 and 5 vertices plus one exact 6-vertex witness; 1,041 inputs; 5,202 assertions. | For `n=4,5` the closure mimics the binary simplicial-matroid closure (326 targets).  A seven-face absorbing state at `n=6` already omits the linearly forced face `(3,4,5)`.  This kills the attractive low-dimensional extrapolation, and no replacement atlas remains.  **Kill.** |
| `HG2` | From a complete tetrahedron boundary, choose one of its four faces uniformly and delete it. | Every 3-graph on 4 and 5 vertices; 1,040 inputs; 4,160 assertions. | 257 nonconfluent and 51 variable-clock sources, up to 155 terminals.  **Kill.** |
| `HG3` | A state is a family of nonempty subsets of `[3]`.  Choose a witness pair `A proper subset B` and delete `B`. | All 128 families; 384 assertions. | Unique inclusion-minimal Sperner kernel and fixed deletion clock; histories are only witness-labelled deletion orders.  **Kill theorem-thin.** |
| `HG4` | A family in `2^[3]`; choose two present sets whose union is absent and adjoin their union. | All 256 families; 1,024 assertions. | Generic semilattice closure, 122 terminals, maximum depth 4.  **Kill generic closure.** |
| `HG5` | Choose an incomparable present pair.  Delete the larger-cardinality member, or either member when tied, uniformly over events. | All 128 nonempty-set families; 512 assertions. | 96 nonconfluent and 68 variable-clock sources, up to nine chain terminals.  **Kill arbitrary thinning.** |
| `MT1` | A path-edge subset has distinct weights.  For an adjacent active conflict, delete its lower-weight edge; choose an active conflict uniformly. | All weight orders and active subsets for 3, 4, 5 edges; 4,272 inputs; 17,088 assertions. | 354 nonconfluent and 354 variable-clock instances, up to five matchings.  **Kill asynchronous heuristic.** |
| `MT2` | In a labelled graph, choose uniformly an edge whose deletion preserves every connected component; stop at a spanning forest. | Every graph on 4 and 5 vertices; 1,088 inputs; 22,248 assertions. | Graphic-matroid nullity is the clock, but 759 sources have multiple terminal forests and there are up to 125 terminals.  **Kill classical reverse deletion.** |
| `MT3` | A boxed plane partition is an order ideal.  Choose a removable maximal cube uniformly and delete it until empty. | All ideals in `2x2x2`, `2x2x3`, `2x2x4`; 175 inputs; 525 assertions. | Volume is the clock and histories are linear extensions (maximum 183,958).  **Kill distributive-lattice background.** |
| `W01` | On ternary words, contract any `aba` to `a`. | Every word of length 0--9; 29,524 inputs; 118,096 assertions. | Unique normal form and fixed clock in the full range, but this is immediate-backtrack/spur cancellation in an edge path.  **Kill direct reduction owner.** |
| `W02` | On binary words, contract a doubled length-two block `abab` to `ab`. | Every word of length 0--14; 32,767 inputs; 131,068 assertions. | Unique root and fixed clock in the full range, already inside fixed-length tandem-deduplication theory.  **Kill direct owner.** |
| `W03` | On ternary words, contract `abba` to `aa`. | Every word of length 0--9; 29,524 inputs; 118,096 assertions. | 978 nonconfluent and 348 variable-clock sources, up to three terminals.  **Kill.** |
| `W04` | On full binary bracketings, apply a right Tamari rotation `((AB)C) -> (A(BC))` at any subtree. | Every tree with 1--8 leaves; 626 inputs; 1,252 assertions. | Unique right comb, but 498 states have variable clocks; histories are paths in the classical Tamari lattice.  **Kill direct owner.** |
| `BF1` | Choose a pure literal of a signed CNF formula and delete every clause it satisfies. | All two-variable formulas and all three-variable formulas with at most four clauses; 18,158 inputs; 72,632 assertions. | Confluent residual core but 3,632 variable clocks.  This is the textbook pure-literal algorithm.  **Kill.** |
| `BF2` | Choose a unit clause, satisfy its literal, delete satisfied clauses and the opposite literal elsewhere; an empty clause absorbs. | Same 18,158 formulas; 72,632 assertions. | 1,812 sources can reach contradiction; 1,259 are nonconfluent and 448 have variable clocks, with up to four terminals.  **Kill textbook unit propagation.** |

The exact 6-vertex `HG1` separation witness is

```text
012, 013, 024, 034, 125, 135, 245.
```

It contains no three faces of a tetrahedron, so the local rule is already
absorbed.  Nevertheless the binary boundary vector of `345` lies in the span
of those seven triangle-boundary vectors.  This is a falsifier for the tempting
all-`n` simplicial-matroid identification, not evidence for a new theorem.

## 3. `BR1`: exact theorem-shaped lemma and why it does not pass

Let `R subseteq A x B`, regarded as a bipartite graph.  The rule adds one
missing corner whenever three corners of a rectangle are present.  Write
`R^square` for the endpoint.

### 3.1 Zero-credit endpoint and clock

Every nontrivial connected component of `R` is completed to the biclique on
the same two vertex classes.  Equivalently,

```text
R^square = (R R^T)^* R = R (R^T R)^*.
```

This is exactly the least difunctional relation containing `R`, not a new
normal form.  Since each firing adds one edge, every schedule has the
tautological depth

```text
D(R) = |R^square| - |R|.
```

Termination and scheduler independence follow either from monotonicity plus
minimality of the difunctional closure, or directly by completing connected
components.  All of this receives zero contribution credit.

### 3.2 Every-target fibre identity

Fix an absorbing target whose nontrivial components are bicliques
`K_(a_i,b_i)`.  Let

```text
C_(a,b)(x) = sum_H x^|E(H)|,
```

where the sum is over connected spanning subgraphs `H` of `K_(a,b)`.  A
source closes to the target exactly when, independently in every target
rectangle, it is a connected spanning bipartite subgraph.  Hence the complete
target depth polynomial is

```text
B_T(q) = sum_(R^square=T) q^D(R)
       = product_i q^(a_i b_i) C_(a_i,b_i)(q^(-1)).        (BR1.1)
```

The verifier checks (BR1.1) independently for all 640 targets in the stated
boxes.  Its second route computes `C_(a,b)` by distinguishing a left vertex
and solving the component recurrence

```text
(1+x)^(ab)
 = sum_(1<=i<=a, 0<=j<=b)
   binom(a-1,i-1) binom(b,j)
   C_(i,j)(x) (1+x)^((a-i)(b-j)),                       (BR1.2)
```

with `C_(1,0)=1` and `C_(i,0)=0` for `i>1`.  Equations (BR1.1)--(BR1.2) are
correct and all-parameter, but the proof is a one-paragraph identification of
two classical objects.

### 3.3 Fresh primary-owner subtraction

- Backhouse and Oliveira, [*On difunctions*](https://www.sciencedirect.com/science/article/pii/S2352220823000329),
  *Journal of Logical and Algebraic Methods in Programming* 134 (2023),
  100878, review Riguet's 1948 notion and explicitly identify a difunction as
  a set of completely disjoint rectangles.  The relation class and terminal
  geometry are zero credit.
- Kahl, [*A Relation-Algebraic Approach to Graph Structure
  Transformation*](https://www.cas.mcmaster.ca/~kahl/Publications/RelRew/RelRew_TR2002-03.pdf),
  Definition 5.2.1, explicitly defines the least difunctional closure as the
  displayed transitive-composition formula.  Thus even the closure operator,
  not merely the word “difunctional,” is directly owned.
- Connected spanning subgraphs are precisely the pathsets counted by the
  all-terminal reliability polynomial.  Pérez-Rosés,
  [*Sixty Years of Network Reliability*](https://doi.org/10.1007/s11786-018-0345-5),
  reviews this definition and records recursive formulas for complete
  bipartite graphs; Frank and Gaul's primary paper
  [*On reliability in stochastic graphs*](https://doi.org/10.1002/net.3230120204)
  is part of that classical line.  Therefore `C_(a,b)` and its component
  recurrence are zero credit.

Fresh queries for `"three-corner completion"`, `"rectangle completion"
binary relation dynamics`, `difunctional closure asynchronous`, and the exact
fibre/reliability conjunction did not locate a paper printing (BR1.1) in this
notation.  That bounded non-hit does not rescue the contract: after owner
subtraction, (BR1.1) is a useful coordinate lemma, not a theorem-scale paper.

**Decision:** `RESERVE_COORDINATE_LEMMA_OWNER_HEAVY`.  It may be cited inside
a future relation-dynamics paper whose main theorem is elsewhere.  It must not
be allocated a paper slot on its own.

## 4. `FG1`: second reserve, also below paper scale

For a nonempty `S subset AG(r,2)`, the rule's endpoint is `aff(S)` and every
schedule has depth `|aff(S)|-|S|`.  For a target affine `r`-flat, Möbius
inversion gives

```text
F_r(q)
 = sum_(s=0)^r 2^(r-s) [r choose s]_2
   (-1)^(r-s) 2^binom(r-s,2)
   sum_(m=1)^(2^s) binom(2^s,m) q^(2^r-m).              (FG1.1)
```

The empty source is the sole source of the empty target.  The executable
checks (FG1.1) for every affine flat through `AG(3,2)`.

This is standard closure in the affine binary matroid followed by standard
Möbius inversion on its lattice of flats.  A current primary reference,
[Ferroni, Matherne and Vecchi, *Chain Tutte
Polynomials*](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v33i2p21)
(2026), explicitly recalls the flat-closure/Möbius spanning-subset identity.
Internally, P67 already occupies a matroid carrier, P109 occupies finite-field
subspace fibres, and P125 occupies binary quadratic geometry.  The literal
parallelogram rule differs from all three, but a different presentation does
not create residual theorem value.

**Decision:** `RESERVE_CLASSICAL_AFFINE_CLOSURE` as a regression/control
formula only; no paper-scale promotion.

## 5. Owner-killed false positives

- `W01` is an edge-path spur reduction.  Geoghegan's
  [*Topological Methods in Group Theory*](https://www.maths.ed.ac.uk/~v1ranick/papers/geoghe.pdf),
  Section 3.1, states the unique reduction obtained by deleting degenerate
  edges and adjacent inverse pairs.  Encoding a vertex word as a path turns
  `aba -> a` into exactly that operation.  The finite confluence signal is not
  residual progress.
- `W02` is fixed-length tandem deduplication.  Jain, Farnoud, Schwartz and
  Bruck, [*Duplication-Correcting Codes for Data Storage in the DNA of Living
  Organisms*](https://arxiv.org/abs/1606.00397), give the unique-root
  classification for fixed and bounded duplication lengths.  The observed
  binary length-two root is directly inside that theory.
- `HG1` initially looked stronger than a generic Horn closure because every
  `n<=5` endpoint agreed with linear closure in the triangle-boundary
  matroid.  Simplicial boundary matrices and their spanning-tree matroids are
  classical; see Duval, Klivans and Martin,
  [*Simplicial matrix-tree theorems*](https://arxiv.org/abs/0802.2576).
  The explicit `n=6` witness above then kills even the tempting all-size
  identification.

The remaining kills fail earlier: nonconfluence/variable clocks without an
exact law (`BR2`, `FG2`, `HG2`, `HG5`, `MT1`, `W03`, `BF2`), or a literal
classical algorithm/lattice (`FG3`, `FG4`, `HG3`, `HG4`, `MT2`, `MT3`,
`W04`, `BF1`).

## 6. P1--P131 and current-batch collision firewall

| This lane | Closest occupied material | Nonidentity and why it still does not promote |
|---|---|---|
| `BR1/BR2` | P68 complete-bipartite hom shifts; P106 graph polarity; P123 component complementation; P127 looped-digraph parity | The carrier is a bipartite relation and the atomic move is one missing rectangle corner, so there is no literal collision.  The external difunctional-closure owner is nevertheless decisive. |
| `FG1--FG4` | P67 plaquette matroid; P109 nilpotent subspace images; P125 quadratic-space pairs | The affine/Fano updates are literal new maps, but their strongest outputs are generic flat closure, rank, bases, and Möbius inversion. |
| `HG1--HG5` | P110 partition shift--join; P123 graph components; P124 monomial upper sets | Hypergraphs and set families are new carriers.  Horn/semilattice closure or arbitrary thinning provides no independent temporal theorem. |
| `MT1--MT3` | P114 forest peeling; P129 rootward coalescence; P130 chord-matching fibres | Weighted conflict deletion, graph reverse deletion, and ideal-cube deletion are distinct, but their outputs reduce to heuristic matchings, matroid bases, or linear extensions. |
| `W01--W04` | P117 run reversal; P122 record-block reversal; P126 composition refinement; P131 Euclidean block rotation | These are shrinking nontransport rewrites/rotations, not the occupied maps.  Direct word/path/Tamari owners consume them instead. |
| `BF1--BF2` | no formula carrier among P1--P131 | Literal novelty of carrier is insufficient: both updates are textbook SAT preprocessing algorithms and the exact pilot exposes no new distribution. |

Searches over the other three current replacement scouts also found no
duplicate literal.  Shared nouns such as “matching,” “flat,” “fibre,” or
“closure” are not counted as collisions; a classical theorem transfer is
still enough to kill value.

## 7. Final gate

| Rank | Handle | Mathematical status | Paper gate |
|---:|---|---|---|
| 1 | `BR1` | Correct all-parameter fibre identity with two elementary derivations | **RESERVE lemma only; direct closure and reliability owners** |
| 2 | `FG1` | Correct all-target affine-flat Möbius polynomial | **RESERVE control only; generic matroid inversion** |
| 3--20 | all others | Exact negative evidence or classical reductions | **KILL** |

There is therefore **no stochastic/asynchronous replacement finalist in this
batch**.  The correct action is to change mechanism class, especially toward
genuinely state-dependent random kernels with a nontrivial exact law, rather
than polishing either closure reserve.
