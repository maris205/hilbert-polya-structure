# Replacement-2 owner-first search log

**Search date:** 2026-09-02 UTC  
**External status:** `HOLD_EXTERNAL`  
**Claim status:** no novelty, priority, or nonexistence claim.

## Method and classification

The search was run before any candidate could be promoted.  Search-engine
results were used only to route to primary records.  The sources credited in
the decisions below are arXiv records, publisher/DOI pages, official society or
institutional records, or author-hosted copies/pages.

Relationship labels mean:

- **direct kernel:** the same state and literal random update;
- **direct object:** the same carrier and legal move graph, even if the exact
  laziness scheduler differs;
- **same observable/model family:** the same principal random object or
  statistic, but a different kernel;
- **nearest neighbour:** shared language or framework only;
- **generic owner:** a general theorem reduces the candidate's claimed axis to
  a routine specialization.

A bounded non-hit is recorded only as a limitation.  It never supports a
novelty claim.  Subscription-only MathSciNet, Zentralblatt, and exhaustive
citation-graph coverage were not completed.

## Databases and query ledger

The following query families were used, with spelling, hyphenation, and symbol
variants:

```text
ATF:
  convex polygon triangulation random diagonal flip Markov chain
  associahedron flip walk mixing
  Molloy Reed Steiger triangulation walk

RBF:
  reduced word random walk commutation braid moves
  graph of reduced words commutation braid
  longest permutation reduced-word braid Markov chain

RAN:
  random Apollonian network choose triangular face add vertex
  random active face subdivision ternary tree
  uniform leaf expansion ordered ternary increasing tree hook formula

GRS:
  inverse a-shuffle stable sort iid labels rising sequences
  Bayer Diaconis probability every arrangement riffle shuffle
  dovetail shuffle semigroup a-shuffle

SBS:
  random Bulgarian solitaire one card each pile independently probability
  stochastic Bulgarian solitaire stationary measure
  pile-wise Bernoulli Bulgarian solitaire

RSK:
  iid random word RSK shape Markov chain Schur transition
  conditioned random walks RSK correspondence shape process
  hook content RSK random word endpoint distribution

MCA:
  random adding machine choose digit position increment carry process
  cyclic group walk powers of base increments inverse weights
  carries shuffling symmetric functions

RGE:
  finite field random pivot Schur complement process
  uniformly random nonzero pivot Gaussian elimination
  binary matrix pivot history distribution
  matrix factorizations uniformly random pivoting

RNC:
  random compatible diagonal insertion convex polygon
  sequential random noncrossing chord insertion triangulation distribution
  random noncrossing plane configurations uniform dissections

RMI:
  random mapping orbit tail cycle joint distribution
  random functional graph rho length generating function
  Flajolet Odlyzko random mapping statistics
```

Full-text phrase checks, where a primary PDF was available, included
`transition`, `uniform`, `stationary`, `rising sequence`, `commutation`,
`braid`, `active face`, `top card`, `shape process`, `Schur complement`,
`compatible diagonal`, `tail`, and `cycle`.  Phrase non-hits are routing facts,
not theorem-level evidence.

## Candidate-by-candidate audit

### ATF — direct kernel

1. M. Molloy, B. Reed, and W. Steiger,
   [*On the mixing rate of the triangulation walk*](https://doi.org/10.1090/DIMACS/043/11),
   DIMACS Series 43 (1999), 179--190.  The official DIMACS/AMS record and the
   [author publication page](https://www.cs.toronto.edu/~molloy/webpapers/papers.html)
   describe the chain on triangulations of a convex polygon that chooses one of
   the `n-3` internal diagonals at random and flips it.  This is the **direct
   kernel**.
2. D. Eppstein and D. Frishberg,
   [*Improved mixing for the convex polygon triangulation flip walk*](https://arxiv.org/abs/2207.09972),
   is a later primary source on the same chain.

**Zero credit:** literal chain, associahedron move graph, reversibility/uniform
stationarity, and generic mixing questions.  **Decision:** `KILL_DIRECT`.

### RBF — direct object

1. J. Elder,
   [*On Graphs of Sets of Reduced Words*](https://arxiv.org/abs/2201.12887),
   defines `G(sigma)` with reduced words as vertices and commutation or long
   braid moves as edges.  This is the **direct move object**.
2. A. Schilling, N. M. Thiéry, G. White, and N. Williams,
   [*Braid moves in commutation classes of the symmetric group*](https://arxiv.org/abs/1507.00656),
   treats braid-move statistics and promotion orbits on the same structures.

The scout's fixed pair/triple-slot scheduler adds self-loops to a symmetric
walk on this owned graph; it does not create a carrier-specific second axis.
**Zero credit:** move graph, connectivity via Coxeter relations, commutation and
braid statistics.  **Decision:** `KILL_DIRECT_OBJECT`.

### RAN — direct kernel/model

T. Zhou, G. Yan, P.-L. Zhou, Z.-Q. Fu, and B.-H. Wang,
[*Random Apollonian Networks*](https://arxiv.org/abs/cond-mat/0409414),
introduce the rule that repeatedly chooses a triangular face and inserts a new
vertex joined to its three corners.  This is the **direct model**.  The dual
ordered ternary leaf-growth representation and increasing-tree history count
are standard encodings of that update.

**Zero credit:** literal face-subdivision process, Random Apollonian Network
name/model, scale-free-network consequences, and generic increasing-tree hook
enumeration.  **Decision:** `KILL_DIRECT`.

### GRS — direct kernel and exact law

D. Bayer and P. Diaconis,
[*Trailing the Dovetail Shuffle to Its Lair*](https://doi.org/10.1214/aoap/1177005705),
*Annals of Applied Probability* 2 (1992), 294--313; an institutional primary
record is also hosted by the
[Stanford Department of Statistics](https://statistics.stanford.edu/technical-reports/trailing-dovetail-shuffle-its-lair).
The paper gives a simple expression for the probability of every arrangement
after any number of shuffles.  Stable sorting by iid labels is the standard
inverse `a`-shuffle construction, and the rising-sequence formula and
multiplicative shuffle semigroup are direct material.

**Zero credit:** update, arrangement law, all-time convolution, rising-sequence
statistic, and mixing consequences.  **Decision:** `KILL_DIRECT`.

### SBS — direct kernel

1. S. Popov,
   [*Random Bulgarian solitaire*](https://arxiv.org/abs/math/0401385),
   *Random Structures & Algorithms* 27 (2005),
   [DOI 10.1002/rsa.20076](https://doi.org/10.1002/rsa.20076), studies the
   variant in which a single candidate card in each pile is selected
   independently with fixed probability.  At `p=1/2`, this is the scout's
   **direct kernel**.
2. K. Eriksson, M. Jonsson, and J. Sjöstrand,
   [*The Limit Shape of a Stochastic Bulgarian Solitaire*](https://arxiv.org/abs/1309.2846),
   studies the related card-wise Bernoulli variant.  It is a **same-family,
   different-kernel** source, not the direct-owner basis.
3. The same authors'
   [random `q`-proportion extension](https://arxiv.org/abs/1703.07102) explicitly
   describes Popov's one-candidate-per-pile rule as its base case.

**Zero credit:** literal pile-wise process, finite ergodicity program, and
limit-shape framing.  **Decision:** `KILL_DIRECT`.

### RSK — direct shape-process owner

N. O'Connell,
[*A path-transformation for random walks and the Robinson--Schensted correspondence*](https://arxiv.org/abs/math/0203177),
relates the RSK path transformation to a random walk conditioned to remain in a
type-A Weyl chamber and supplies the shape-process framework.  Together with
the classical RSK/Schur correspondence, this determines the Markov shape law
used by the scout.

**Zero credit:** RSK shape Markov property, conditioned-walk interpretation,
Schur transition, hook-length endpoint multiplicity, and hook-content
specialization.  **Decision:** `KILL_DIRECT`.

### MCA — generic owner; nearest carries source is not the same kernel

P. Diaconis and J. Fulman,
[*Carries, shuffling, and symmetric functions*](https://arxiv.org/abs/0902.0179),
study the Markov chain formed by carries when several random base-`b` numbers
are added and relate it to riffle-shuffle descents.  This is a **nearest
same-theme source, not the same kernel**: MCA is a single counter modulo `b^h`
that chooses one increment from `{1,b,...,b^(h-1)}`.

No bounded primary search hit was classified as the exact MCA kernel.  The kill
does not rely on that non-hit.  The all-time transform is the standard
character transform of a random walk on the finite cyclic group, the
weight-inverse is literal one-step support reading, and stationary carry tails
are uniform-digit counting.  Those generic reductions leave no independent
paper-sized conjunction.

**Zero credit:** cyclic-group Fourier convolution, uniform stationarity, and
classical carries language.  **Decision:** `KILL_GENERIC`.

### RGE — nearest randomized-pivot sources; no direct-owner claim

1. I. Detherage and R. Shah,
   [*Matrix Factorizations with Uniformly Random Pivoting*](https://arxiv.org/abs/2505.02023),
   develops a randomized pivoting rule for numerical matrix-factorization
   algorithms.  It is a **nearest programme**, not the same kernel: the scout
   chooses a nonzero entry of a finite-field matrix and deletes its pivot row
   and column via a Schur complement.
2. J. Peca-Medlin,
   [*Distribution of the number of pivots needed using Gaussian elimination
   with partial pivoting on random matrices*](https://arxiv.org/abs/2301.13452),
   studies pivot movements under GEPP for random numerical ensembles.  It is a
   **different random object and different statistic**.

The bounded search did not locate a primary source for the exact binary
nonzero-Schur-pivot chain.  That is not novelty evidence.  The system is killed
because its clock is the elementary rank descent and no closed history
transform/inverse/extremal second axis emerged.

**Zero credit:** Gaussian-elimination and Schur-complement basics, rank descent,
and broad randomized-pivoting motivation.  **Decision:** `KILL_THIN`.

### RNC — static same-object neighbours; no direct-kernel hit

1. N. Curien and I. Kortchemski,
   [*Random non-crossing plane configurations: A conditioned Galton--Watson
   tree approach*](https://arxiv.org/abs/1201.3354), studies uniform dissections
   and noncrossing trees.  It is a **same-carrier/static-law neighbour**, not
   the sequential compatible-diagonal kernel.
2. The ATF sources above own the convex-polygon triangulation carrier with a
   different flip update.
3. Internally, P146 already occupies a convex-polygon triangulation endpoint
   lane.  This is an internal collision, not external ownership.

No bounded primary search hit was classified as the exact naïve insertion
kernel.  The non-hit is not credited.  The endpoint is currently only a finite
path sum, with no all-parameter transform or second axis.

**Zero credit:** Catalan triangulation enumeration, static uniform dissection
laws, noncrossing/tree encodings, and the occupied internal polygon carrier.
**Decision:** `KILL_THIN_INTERNAL`.

### RMI — direct classical model

P. Flajolet and A. M. Odlyzko,
[*Random Mapping Statistics*](https://doi.org/10.1007/3-540-46885-4_34),
LNCS 434 (1990), 329--354.  The publisher abstract states that the paper gives
a general generating-function/singularity framework for about twenty
parameters of uniformly random mappings.  An
[author-hosted publication index](https://www-users.cse.umn.edu/~odlyzko/doc/probability.html)
links the paper as well.  The functional graph of a uniform map and its orbit
tail/cycle statistics are the **direct classical object**.

**Zero credit:** random-map functional graph, rho/tail/cycle decomposition,
generating-function framework, and classical parameter asymptotics.
**Decision:** `KILL_DIRECT`.

## Surviving claim conjunction

There is none in this round.  The only correct owner-gate result is

```text
SURVIVORS = 0
STATUS = PASS_EMPTY_POOL
EXTERNAL = HOLD_EXTERNAL
```

RNC's hexagon boundary, MCA's elementary exact formulas, and RGE's
same-rank-history split may be useful seeds, but none survives as a claim
conjunction.  Re-entry requires both an all-parameter theorem breakthrough and
a new primary-source audit.

## Bounded-search limitation

The audit is deliberately conservative but not exhaustive.  It did not finish
subscription citation indexes, all non-English literature, books without
searchable full text, theses, or every descendant citation.  Therefore even an
unmatched exact kernel above cannot be described as new.  Conversely, the
decisions do not depend on asserting absence: candidates are killed either by
a positive owner match or by failure of the two-axis theorem gate.
