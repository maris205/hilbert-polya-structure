# Owner-first search log — stochastic replacement 3

**Search date:** 2026-09-02 UTC  
**External status:** `HOLD_EXTERNAL`  
**Claim status:** no novelty, priority, or source-exhaustion claim.

## Search protocol

Search was performed before any system could be promoted.  Search snippets
were used only to locate primary records.  Decisions rely on publisher/DOI
pages, arXiv records, official institutional pages, or author-hosted papers.

Relationship labels:

- **direct kernel:** same carrier, active choice, and literal update;
- **direct object/program:** same move graph or algorithmic dynamical program,
  although the precise laziness/tie scheduler may differ;
- **same mechanism:** the update family is the same, while a cap, discretization,
  or noise convention differs;
- **nearest neighbour:** common carrier or vocabulary, different update;
- **generic owner:** the claimed formula is routine finite-state, first-passage,
  or reversible-chain machinery.

The kill test is asymmetric.  A positive direct match kills immediately.  A
bounded non-hit never clears novelty; a system can still be killed for theorem
thinness without a direct source.

## Databases and query families

Primary routing channels actually used:

- APS journal records;
- arXiv title/abstract/full-text records;
- SIAM, INFORMS, Taylor & Francis, Springer/Combinatorica, and DOI records;
- Stanford, Freie Universität Berlin, ETH, Monash, and author publication
  pages/PDFs.

Queries, with spelling and hyphen variants:

```text
DBM:
  Bak Sneppen global minimum nearest neighbors refresh
  discrete finite-state Bak-Sneppen ties
  punctuated equilibrium simple evolution model 71 4083

LIT:
  Latin square intercalate switch graph
  cycle switches Latin squares intercalate-only
  fixed rectangle intercalate trade Markov chain
  random Latin squares switchings Jacobson Matthews

PPT:
  plane partition add remove cube Glauber dynamics
  boxed plane partition local toggle Markov chain
  lozenge tiling single-flip Glauber dynamics
  Markov chain algorithms planar lattice structures

SMB:
  random blocking pair matching former partners single
  random paths stability two-sided matching
  blocking-pair Markov chain stable marriage absorption

AIM:
  stochastic capped additive increase multiplicative decrease Markov chain
  AIMD Bernoulli loss stationary distribution finite window
  increase decrease congestion avoidance Chiu Jain

RSP:
  Random-Edge acyclic unique sink orientation cube
  randomized simplex Klee-Minty cube expected path
  Gray code cube orientation random edge

R2O:
  random improving 2-opt dynamics TSP
  2-opt local search random move clock
  Croes method traveling salesman 2-opt

RDA:
  asynchronous deferred acceptance arbitrary proposal order
  random order Gale-Shapley proposals
  deferred acceptance proposal count order independent
```

Full-text phrase checks where searchable included `minimum`, `neighbor`,
`intercalate`, `cycle switch`, `single flip`, `blocking pair`, `randomly
chosen`, `additive increase`, `multiplicative decrease`, `Random-Edge`,
`acyclic unique sink`, `2-opt`, `proposal`, and `order`.

## DBM — direct mechanism

P. Bak and K. Sneppen,
[*Punctuated equilibrium and criticality in a simple model of evolution*](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.71.4083),
*Physical Review Letters* 71 (1993), 4083--4086,
[DOI 10.1103/PhysRevLett.71.4083](https://doi.org/10.1103/PhysRevLett.71.4083).
The primary APS record introduces the model in which the least-fit species and
its neighbours are refreshed by new random fitnesses.  This is the **direct
mechanism**.  The scout only replaces continuous fitnesses by a finite alphabet
and resolves ties uniformly.

A later primary APS paper,
[*Bak-Sneppen model: Local equilibrium and critical value*](https://journals.aps.org/pre/abstract/10.1103/PhysRevE.97.042123),
confirms that the model and neighbour-number variants remain an active direct
literature.

**Zero credit:** global-minimum selection, neighbour refresh, avalanche and
self-organized-criticality framing, and model naming.  **Decision:**
`KILL_DIRECT`.

## LIT — direct move graph

1. I. M. Wanless,
   [*Cycle Switches in Latin Squares*](https://doi.org/10.1007/s00373-004-0567-7),
   *Graphs and Combinatorics* 20 (2004), 545--570; the
   [author-hosted paper](https://users.monash.edu.au/~iwanless/papers/cycleswapgr.GC.pdf)
   constructs graphs whose vertices are classes of Latin squares and whose
   edges arise from cycle switches.  It explicitly includes the variant in
   which only intercalates may be switched.  This is the **direct move graph**.
2. M. Kwan and B. Sudakov,
   [*Intercalates and Discrepancy in Random Latin Squares*](https://arxiv.org/abs/1607.04981),
   and Kwan--Sah--Sawhney,
   [*Large deviations in random Latin squares*](https://arxiv.org/abs/2106.11932),
   own modern static distributional questions for the intercalate count.
3. Kwan--Petrova--Sawhney,
   [*Parities in random Latin squares*](https://arxiv.org/abs/2509.13125),
   uses stable intercalate switchings for rerandomization.  It is not the same
   fixed-slot Markov chain but narrows the available switching claims.

Jacobson--Matthews random Latin-square generation is a **same sampling
programme, different enlarged move space**; it is not used as the direct-kernel
basis.

**Zero credit:** intercalate switch, switch graph/component language, static
intercalate count, and generic reversible walk on that graph.  The exact lazy
scheduler was not separately matched in the bounded search, but no temporal
theorem survives.  **Decision:** `KILL_DIRECT_OBJECT`.

## PPT — direct local Glauber model

1. M. Luby, D. Randall, and A. Sinclair,
   [*Markov Chain Algorithms for Planar Lattice Structures*](https://epubs.siam.org/doi/abs/10.1137/S0097539799360355),
   *SIAM Journal on Computing* 31 (2001), 167--192,
   [DOI 10.1137/S0097539799360355](https://doi.org/10.1137/S0097539799360355),
   studies local flip chains for planar tiling structures and uniform
   generation.
2. B. Laslier and F. L. Toninelli,
   [*Lozenge tilings, Glauber dynamics and macroscopic shape*](https://arxiv.org/abs/1310.5844),
   explicitly studies Glauber dynamics on lozenge tilings with uniform
   invariant measure.
3. The same authors,
   [*The mixing time of the lozenge tiling Glauber dynamics*](https://arxiv.org/abs/2207.01444),
   calls the update the single-flip Glauber dynamics on lozenge tilings viewed
   as `(2+1)`-dimensional surfaces.

A boxed plane partition is the stepped-surface/lozenge-tiling encoding of the
scout state, and a legal cube toggle is the local lozenge flip.  This is a
**direct model under a standard bijection**, not a loose analogy.

**Zero credit:** local flip, uniform stationary law, connectivity/mixing
programme, height/volume observable, and static boxed-plane-partition count.
**Decision:** `KILL_DIRECT`.

## SMB — exact direct kernel

A. E. Roth and J. H. Vande Vate,
[*Random Paths to Stability in Two-Sided Matching*](https://web.stanford.edu/~alroth/papers/1990_E_Random_Paths.pdf),
*Econometrica* 58 (1990), 1475--1480,
[DOI 10.2307/2938326](https://doi.org/10.2307/2938326).
The author-hosted primary paper states that, starting from an arbitrary
matching, randomly chosen blocking pairs are allowed to match; it proves
convergence to a stable matching with probability one and that every stable
matching has positive probability from the all-unmatched state.  Its literal
definition makes the former partners single.  This is the scout's **exact
direct kernel**.

**Zero credit:** random blocking-pair process, convergence, stable endpoint
support, and decentralized random-path interpretation.  Profile-specific
clock fractions obtained by generic linear systems do not form a residual.
**Decision:** `KILL_DIRECT`.

## AIM — same mechanism; stochastic finite specialization remains thin

D.-M. Chiu and R. Jain,
[*Analysis of the increase and decrease algorithms for congestion avoidance in
computer networks*](https://doi.org/10.1016/0169-7552(89)90019-6),
*Computer Networks and ISDN Systems* 17 (1989), 1--14.  The
[author publication page](https://home.ie.cuhk.edu.hk/~dmchiu/old_pub.html)
lists the paper and associated congestion-avoidance work.  The primary result
characterizes increase/decrease controls and identifies additive increase plus
multiplicative decrease as the convergent efficient/fair mechanism.

This is a **same mechanism owner**, not a claim that the paper prints the exact
finite-cap Bernoulli stationary fractions.  The bounded search for
`stochastic AIMD stationary distribution` found a broad queueing/network
literature; it was not treated as exhaustively audited.

**Zero credit:** AIMD name/mechanism, congestion feedback interpretation,
convergence/fairness framing.  The residual is only finite stationary linear
algebra and a trivial one-row recovery of `p`.  **Decision:**
`KILL_OWNER_THIN`.

## RSP — direct Random-Edge/AUSO programme

1. B. Gärtner, M. Henk, and G. M. Ziegler,
   [*Randomized simplex algorithms on Klee--Minty cubes*](https://www.mi.fu-berlin.de/math/groups/discgeom/ziegler/Publikationen_old/randomized_simplex_algorithms_on_klee-minty_cubes1/index.html),
   *Combinatorica* 18 (1998), 349--372,
   [DOI 10.1007/PL00009827](https://doi.org/10.1007/PL00009827).  The official
   author page links the primary preprint and describes expected pivot paths on
   oriented cubes.
2. T. D. Hansen, M. Paterson, and U. Zwick,
   [*Improved upper bounds for Random-Edge and Random-Jump on abstract cubes*](https://epubs.siam.org/doi/abs/10.1137/1.9781611973402.65),
   explicitly studies finding the sink of an acyclic unique-sink orientation of
   the cube with Random-Edge.
3. R. Gillmann,
   [*The Random Edge Simplex Algorithm on Dual Cyclic 4-Polytopes*](https://arxiv.org/abs/math/0605117),
   treats Random-Edge even for abstract objective functions/AUSOs.

The scout's inverse-Gray total ranking supplies one specific AUSO.  It does not
escape this **direct algorithmic programme**.

**Zero credit:** Random-Edge, AUSO sink search, pivot-path clock recurrence,
and generic expected path length.  **Decision:** `KILL_DIRECT_PROGRAM`.

## R2O — direct deterministic move; random scheduler unmatched but thin

G. A. Croes,
[*A Method for Solving Traveling-Salesman Problems*](https://pubsonline.informs.org/doi/10.1287/opre.6.6.791),
*Operations Research* 6 (1958), 791--812,
[DOI 10.1287/opre.6.6.791](https://doi.org/10.1287/opre.6.6.791),
introduces the mechanizable local tour-improvement method now called 2-opt.
Modern primary approximation work includes
[*The Approximation Ratio of the 2-Opt Heuristic for the Euclidean Traveling
Salesman Problem*](https://arxiv.org/abs/2010.02583).

The bounded search did not identify a primary source for precisely “uniformly
choose among all current strict improvements” on the scout's two point
families.  This is not a positive result.  The move and potential descent are
owned, while the random scheduler yields only instance-specific finite DAG
recurrences and deterministic endpoints in the pilot.

**Zero credit:** 2-opt move, local-optimum endpoint, strict length potential,
and generic active-choice recurrence.  **Decision:** `KILL_THIN`.

## RDA — direct base algorithm; scheduler is zero-credit wrapper

D. Gale and L. S. Shapley,
[*College Admissions and the Stability of Marriage*](https://www.tandfonline.com/doi/abs/10.1080/00029890.1962.11989827),
*American Mathematical Monthly* 69 (1962), 9--15,
[DOI 10.2307/2312726](https://doi.org/10.2307/2312726), introduces deferred
acceptance and proves stability.  The proposal order does not change the
proposer-optimal outcome under the standard strict complete-list assumptions.

The scout only chooses the next currently free proposer uniformly.  Each
proposer still advances monotonically down the owned preference list.  Since
the final matching is fixed, the total number of proposals is the sum of final
partner ranks plus one and is also fixed.  Thus the stochastic scheduler does
not create a random endpoint or clock.

**Zero credit:** DA mechanism, stable/proposer-optimal endpoint, proposal-list
monotonicity, and order wrapper.  **Decision:** `KILL_DEGENERATE`.

## Surviving conjunction and bounded-search limitation

There is no surviving claim conjunction:

```text
SURVIVORS = 0
STATUS = PASS_EMPTY_POOL
EXTERNAL = HOLD_EXTERNAL
```

This owner audit is bounded.  It did not exhaust MathSciNet, Zentralblatt,
non-English literature, every book/thesis, or all citation descendants.  In
particular, absence of a matched exact scheduler for AIM, R2O, or LIT is not an
absence claim.  Those candidates are killed independently because their
residual formulas fail the non-generic two-axis theorem threshold.
