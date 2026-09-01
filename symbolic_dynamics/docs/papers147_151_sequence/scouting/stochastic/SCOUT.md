# Stochastic/graph Stage-1 scout — P147–P151 intake

**Lane:** random graph deletion, stochastic elimination, absorbing walks, and finite-chain controls.

**Date:** 2026-09-01.

**External status:** `HOLD_EXTERNAL`.
**Scope:** seventeen genuinely different literal updates; parameter sweeps are not counted as new systems.

## Outcome first

The expanded lane executed **1,269,363 exact assertions** over seventeen literal
systems.  The former two signals are now permanently removed.  `S09` is an
exact internal specialization of P136.  `S08` is exactly the classical
annihilation process on `L(K_{2,n})`; a new supermartingale argument gives
quantitative bounds, but not enough owner-subtracted mass to retain it.

The replacement signal is `R11`: simple random walk from the centre of a
finite unequal-legged spider, with all leaves absorbing.  It has a complete
leaf-marked Chebyshev rational transform, exact mean and variance, sharp
fixed-mass extremizers, and an inverse that recovers every arm length from the
endpoint law plus the mean.  Generic tree absorption and gambler's ruin are
zero-credit inputs, so the status is deliberately **owner-thin internal pass**,
not a novelty or release claim.

A second, deliberately non-graph pool tested four further mechanisms after
`R11`.  Fair integer halving has a sharp two-atom clock, but its whole package
is a one-scalar digit contraction too close to the occupied digit lane.
Totient--radical descent has infinite clock collisions, random squarefree
reduction sees only the maximum root multiplicity, and random two-braid
smoothing is a direct Kauffman-state specialization.  Therefore the second
pool has **no selection**; the value threshold was not lowered to manufacture
a second stochastic candidate.

The attractive path-vertex, banana-graph, induced-`P3`, DAG-source, and Young
corner profiles were not retained.  Exact computation exposed direct transfers
to graph peaks, random minimum spanning trees, the OK-Corral urn, linear
extensions, and the Frame–Robinson–Thrall hook formula respectively.

Enumeration below is falsification pressure only.  The bounded direct-owner
non-hit for the `R11` theorem conjunction is not a novelty, priority, or
release claim.

## Exact audit

| ID | literal update | tested carrier family | exact assertions | decision |
|---|---|---|---:|---|
| S01 | delete a uniform non-isolated vertex | paths | 409,128 | **KILL — graph peaks** |
| S02 | delete a uniform nonbridge edge | banana graphs | 46,141 | **KILL — reverse Kruskal/random MST** |
| S03 | choose an induced `P3`; delete its centre | complete bipartite graphs | 318 | **KILL — shifted OK-Corral urn** |
| S04 | delete a uniform source | finite DAGs | 125,568 | **KILL — linear extensions** |
| S05 | delete a uniform removable corner | Young diagrams | 890 | **KILL — standard tableaux/hook formula** |
| S06 | delete and shortcut a uniform active cycle element | permutations by cycle decomposition | 60 | **KILL — random-order wrapper** |
| S07 | choose a comparable pair; fair-delete one endpoint | complete height-two posets | 891 | **KILL — negative-binomial wrapper** |
| S08 | choose two conflicting edges; fair-delete one | `K_{2,n}` | 11,272 | **KILL — direct annihilation-process owner** |
| S09 | choose a triangle; delete one uniform edge | `r`-page triangle books | 3,335 | **KILL — exact P136 specialization** |
| S10 | delete a uniform simplicial vertex until complete | clique windmills | 70 | **KILL — PEO/random-order wrapper** |
| R11 | simple random walk; absorb at the first leaf | finite unequal-legged spiders | 65,528 | **PASS OWNER-THIN — replacement signal** |
| R12 | choose a uniform inversion and swap it | permutations | 76,741 | **KILL — random sorting/firewall** |
| R13 | swap a uniform occupied/unoccupied label | `k`-subsets / Johnson graphs | 450 | **KILL — Bernoulli–Laplace direct owner** |
| R14 | halve evenly; fair-round an odd integer before halving | positive integers, stopped at one | 327,675 | **KILL — occupied digit-contraction engine** |
| R15 | choose `phi(n)` or `n/rad(n)` fairly | positive integers, stopped at one | 15,667 | **KILL — infinite clock nonidentifiability** |
| R16 | choose derivative-GCD or squarefree kernel fairly | characteristic-zero factored polynomials | 54,390 | **KILL — law sees only maximum multiplicity** |
| R17 | fair-smooth a uniformly chosen unresolved crossing | closed positive two-braids | 131,239 | **KILL — direct Kauffman state sum** |
| **total** | **seventeen literal systems** |  | **1,269,363** |  |

The verifier uses only integers and `fractions.Fraction`.  For `R11` it compares
a literal vertex-state first-passage recursion with an independently assembled
Chebyshev rational transform coefficient by coefficient.

## S01 — active-vertex deletion on paths

### Literal update

For a finite graph `G`, if an edge remains, choose uniformly among vertices of
positive current degree and delete the chosen vertex and its incident edges.
Isolated vertices freeze.  On `P_n`, stop at the surviving independent set.

### Exact pilot

All `n!` choice orders were checked for every `2 <= n <= 9`.  If the deletion
order gives distinct ranks to the vertices, the survivors are exactly the
vertices whose rank is larger than every neighbouring rank, including the two
one-sided boundary comparisons.  Let

`F_n(z) = E[z^{number of survivors on P_n}]`.

The first deletion splits the path, giving

`F_0=1`, `F_1=z`, and

`F_n(z) = (1/n) sum_{a=0}^{n-1} F_a(z) F_{n-1-a}(z)` for `n>=2`.

Consequently the ordinary generating function `F(x,z)=sum F_n(z)x^n`
satisfies the Riccati equation

`dF/dx = F^2 + z - 1`, `F(0,z)=1`,

and `E|endpoint(P_n)|=(n+1)/3` for `n>=2`.

### All-parameter theorem and proof engine

The theorem is the equality between the absorbing set and the local-maxima set
of a uniform vertex labelling, followed by the first-deletion factorization and
the Riccati solution.  This is fully proved by the rank coupling and was
verified in 409,128 exact assertions.

### Collision and owner search

Internally this is nearest to P141 only at the independent-set output; unlike
random greedy MIS, the endpoint need not be maximal.  Externally, however, the
entire output is a peak/local-maximum set of a graph labelling.  Paths are the
classical permutation case, with the endpoint convention contributing only
one-sided boundary peaks.  The direct owner neighbourhood includes
[Peaks on Graphs](https://arxiv.org/abs/1708.08493) and the established
permutation peak literature, including
[The pinnacle set of a permutation](https://doi.org/10.1016/j.disc.2018.08.011).

**Decision:** permanent kill.  The dynamical wording does not create a residual
beyond the owned peak statistic.

## S02 — nonbridge deletion on banana graphs

### Literal update

From a connected graph, choose uniformly among current nonbridge edges and
delete the chosen edge.  Stop at a spanning tree.  The pilot carrier is a
banana graph with `r` internally disjoint `u-v` paths of lengths
`ell_1,...,ell_r`.

### Exact pilot

Every edge ordering was checked for length vectors `(2,2,2)`, `(2,2,3)`, and
`(2,3,3)`.  At each deletion one whole path becomes broken.  The path-breaking
order is the Plackett–Luce size-biased order with weights `ell_i`; the last
unbroken path is the survivor.  Its exact probability is

`P(i last) = sum_{A subseteq [r] minus {i}} (-1)^|A| ell_i /(ell_i+sum_{j in A}ell_j)`.

Conditional on survivor `i`, the missing edge in every other path is uniform,
so a particular terminal tree has mass

`P(i last) / product_{j != i} ell_j`.

### All-parameter theorem and proof engine

Assign a uniform random total order to the edges.  Processing that order and
deleting an edge exactly when connectivity is preserved is reverse Kruskal.
On the banana carrier, the first inspected edge of each unresolved path breaks
that path; independent exponential clocks of rates `ell_i` give the formula.

### Collision and owner search

The random ordering plus reverse-delete rule is exactly the random-MST model,
not a new deletion mechanism.  The current primary overview
[Models of random spanning trees](https://arxiv.org/abs/2407.20226) explicitly
treats spanning trees obtained by i.i.d. random edge weights and a greedy MST
algorithm.  This also violates the intake ban on generic random-scan wrappers.

**Decision:** permanent kill.  The banana formula is a soluble example inside
the directly owned random-MST process.

## S03 — induced-`P3` centre deletion on `K_{a,b}`

### Literal update

Choose an induced three-vertex path uniformly from the current graph and delete
its centre vertex.  Starting from `K_{a,b}`, the state remains complete
bipartite, possibly with an empty side.

### Exact pilot

At state `(a,b)` the numbers of paths centred on the two sides are
`a*C(b,2)` and `b*C(a,2)`.  Therefore, for `a+b>2`,

`P((a,b)->(a-1,b))=(b-1)/(a+b-2)`,

`P((a,b)->(a,b-1))=(a-1)/(a+b-2)`.

All states `1<=a,b<=8` were checked, including the forced final boundary step.

### All-parameter theorem and proof engine

The path count above proves the projection.  With shifted interior coordinates
`x=a-1`, `y=b-1`, one side loses a unit with probability proportional to the
other side.  This is the OK-Corral cross-death recurrence; once a shifted count
hits zero, this graph convention performs one deterministic boundary
completion.

### Collision and owner search

The OK-Corral urn and its survivor law are directly owned by
[Kingman–Volkov](https://doi.org/10.1023/A:1022294908268); the published exact
law also has a
[formal correction](https://doi.org/10.1007/s10959-019-00921-0).  General
weighted versions are already treated in
[On sampling without replacement and OK-Corral urn models](https://arxiv.org/abs/1003.1603).

**Decision:** permanent kill.  The induced-subgraph presentation is an exact
state shift of an owned diminishing urn.

## S04 — uniform source deletion in a DAG

### Literal update

Choose a current indegree-zero vertex uniformly, delete it and its incident
arcs, and repeat to the empty DAG.

### Exact pilot

For every forward-edge DAG on at most five labelled vertices, every permutation
was tested.  The possible deletion histories are exactly the topological orders,
and their recursive count is the sum over currently minimal elements.  This
gave 125,568 exact checks.

### All-parameter theorem and proof engine

Induct on the first source.  A valid history begins with and only with a minimal
element of the reachability poset, so histories are precisely linear extensions.
Uniform source choice merely assigns the familiar product of reciprocal
minimal-set sizes to each extension.

### Collision and owner search

This is definition-level linear-extension/topological-sort theory.  The direct
equivalence is recorded in the current primary survey
[Linear extensions of finite posets](https://arxiv.org/abs/2311.02743) and the
algorithmic literature, for example
[Generating linear extensions of posets by transpositions](https://doi.org/10.1016/0095-8956(92)90067-8).

**Decision:** permanent kill.  There is no owner-subtracted temporal result.

## S05 — random Young-corner deletion

### Literal update

From a Young diagram, choose a removable southeast corner uniformly and delete
that cell.  Continue to the empty diagram.

### Exact pilot

All partitions through size 12 were checked.  The number of possible full
deletion histories equals

`f^lambda = |lambda|! / product_{cells c} h(c)`.

The corner recursion and the hook product agreed in every case.

### All-parameter theorem and proof engine

Reverse a deletion history and label cells by insertion time.  The result is a
standard Young tableau, bijectively.  The history count is therefore the
classical hook-length formula.

### Collision and owner search

The exact product is owned by Frame, Robinson, and Thrall,
[The Hook Graphs of the Symmetric Group](https://doi.org/10.4153/CJM-1954-030-1).
It is also too close to the portfolio's principal-hook and Catalan/hook
interfaces to retain as a stochastic relabelling.

**Decision:** permanent kill.

## S06 — cycle erosion of a permutation

### Literal update

Choose uniformly among elements lying in current cycles of length at least two.
Delete the selected element from its cycle by shortcutting predecessor to
successor.  A singleton cycle freezes.  Stop with one survivor from each
original cycle.

### Exact pilot

For initial cycle lengths `ell_1,...,ell_c`, the clock is fixed at
`sum_i(ell_i-1)`, and a particular vector of cycle survivors has mass
`1/product_i ell_i`.  Six mixed cycle profiles, through total size nine, were
checked by exact state recursion.

### All-parameter theorem and proof engine

Within every original cycle, exchangeability makes the last remaining label
uniform.  Independent relative orders on disjoint cycles make the survivors
independent; the global deletion interleaving contributes no endpoint bias.

### Collision and owner search

The full theorem is a random-permutation/exponential-race identity.  The cycle
carrier does not create an inverse, clock, or endpoint residual after this
wrapper is assigned zero credit.  It also lies too near earlier partition
shift/join interfaces.

**Decision:** permanent internal kill under the generic random-scan rule.

## S07 — fair comparable-pair elimination

### Literal update

In the complete height-two poset with `a` lower and `b` upper elements, choose a
comparable lower–upper pair uniformly and fair-delete one of its endpoints.
Stop when the surviving set is an antichain, equivalently when one level is
empty.

### Exact pilot

The side deleted at every step is a fair coin.  The identity within that side
is uniform.  The probability that exactly `s` lower elements survive is

`C(b+a-s-1,b-1) / 2^(b+a-s)`, `1<=s<=a`,

and symmetrically for upper survivors.  A specific surviving `s`-subset has an
additional factor `1/C(a,s)`.  All `1<=a,b<=9` were checked.

### All-parameter theorem and proof engine

Project the pair choice to the selected endpoint's level.  The projection is an
i.i.d. fair coin stopped when one quota is exhausted, so the endpoint and clock
laws are negative-binomial.

### Collision and owner search

The literal relation update is distinct, but its entire probability theorem is
a two-quota stopping rule.  It collides with the `DQ1` reserve and violates the
hard ban on quota/exposure wrappers whose only result is a classical waiting
law.

**Decision:** permanent internal kill.

## S08 — fair conflict deletion on `K_{2,n}`

### Literal update

Regard the edges of a bipartite graph as active jobs.  Choose uniformly an
unordered pair of active edges sharing an endpoint and then delete one of the
two edges by a fair coin.  Stop when no conflict remains, so the endpoint is a
matching.  Start from `K_{2,n}`.

### Exact pilot and strong lumping

Every reachable column is of one of four types: double, row-`A` only, row-`B`
only, or empty.  Let `(x,y,z)` count the first three types and set

`C(x,y,z)=C(x+y,2)+C(x+z,2)+x`.

For `C>0`, the exact transition probabilities are

`(x,y,z)->(x-1,y,z+1)` with `x(x+y)/(2C)`,

`(x,y,z)->(x-1,y+1,z)` with `x(x+z)/(2C)`,

`(x,y,z)->(x,y-1,z)` with `y(x+y-1)/(2C)`,

`(x,y,z)->(x,y,z-1)` with `z(x+z-1)/(2C)`.

These probabilities sum to one and prove strong lumpability.  Let `p(x,y,z)`
be the probability of an absorbing matching of size two, with boundary value
`p(0,y,z)=1` exactly when `y=z=1`.  The four transitions give an exact
all-parameter rational recurrence.

From the full start, `p_n=p(n,0,0)` begins

`0, 1/2, 17/24, 931/1152, 9180653/10644480, 1455263749/1625702400`

for `1<=n<=6`.  Conditional on size two, every one of the `n(n-1)` labelled
two-edge matchings has mass `p_n/[n(n-1)]`.  Conditional on size one, every one
of the `2n` edges has mass `(1-p_n)/(2n)`.  Hence the absorption clock is exactly

`2n-2` with probability `p_n`, and `2n-1` with probability `1-p_n`.

The verifier compared labelled graph recursion with the independent
three-coordinate recurrence for every representative `(x,y,z)` through six
columns.

### Analytic upgrade obtained before killing the system

Put `a=x+y`, `b=x+z`, and let `q_n=1-p_n`.  Before either row reaches a
singleton, the overlap density

`M(a,b,x)=x/(ab)`

is a supermartingale.  Direct substitution in the four transitions gives

`E(Delta M | a,b,x)`

`=x[-2ab+(a+b)x+a+b-2x] / [ab(a-1)(b-1)D] <= 0`,

where `D=a(a-1)+b(b-1)+2x`.  If one row is an overlapping singleton and the
other has size `b`, write `Q_b` for the eventual size-one probability.  Then

`Q_1=1`,

`Q_b=[1+(b-1)^2 Q_(b-1)]/[b(b-1)+2]`,

and the transformed sequence `R_b=bQ_b` satisfies

`R_b=R_(b-1)+[b-2R_(b-1)]/[b(b-1)+2] <= H_b`.

Optional stopping at the first singleton row therefore yields the explicit
all-parameter upper bound

`q_n <= H_n/n`.

There is also a genuine lower bound.  Run only the two independent within-row
clique death processes and condition their uniform final labels to agree, an
event of probability `1/n`.  If no vertical clock rings before both rows have
reached their common singleton, S08 must end at size one.  If `I` is the
integrated row overlap, the conditional no-ring probability is `E exp(-I)`.
The clique block-count process `K(t)` has rates `C(k,2)` and, for
`m(t)=E[K(t)-1]`,

`m'(t) <= -m(t)(m(t)+1)/2`.

Consequently `integral m(t)^2 dt <= 2(n-1-log n)`, while the expected maximum
of the two row absorption times is below four.  Jensen's inequality gives

`q_n >= e^(-6)/n > 1/(729n)`.

Thus the finite recurrence has been upgraded to a nontrivial convergence
theorem

`1-H_n/n <= p_n <= 1-e^(-6)/n`.

The gap of a logarithm remains, and the computation `nq_n=0.3440,0.3216,
0.3092,0.3023` at `n=50,100,200,400` indicates a finite asymptotic constant
which this round did not prove.  Those decimals are scouting evidence only.

### Collision and direct-owner search

The owner collision is exact.  Make the edges of `K_{2,n}` the vertices of its
line graph.  A conflicting pair is then an edge of `L(K_{2,n})`; choosing an
occupied conflict and fair-deleting one endpoint is the embedded jump chain of
the classical annihilation process.  O'Hely and Sudbury introduced that
process as particles killing neighbouring particles; Penrose and Sudbury give
the finite-graph construction by independent edge-event times and fair attack
directions, and explicitly note that the jammed state is an independent set:
[O'Hely--Sudbury](https://doi.org/10.1239/jap/996986655),
[Penrose--Sudbury](https://arxiv.org/abs/math/0503519).

This is equality of transition kernels, not merely an MIS-output analogy.
P141 remains the closest internal endpoint object, but the external process
owner is already decisive.  The new bounds are honest special-carrier
lemmas; with a logarithmic gap and no asymptotic constant, they do not leave a
paper-sized residual.

**Decision:** permanent kill — direct process owner plus insufficient
owner-subtracted theorem value.  Preserve the recurrence, supermartingale, and
bounds as negative controls; do not revive by changing clocks or using the
line-graph name.

## S09 — one-edge triangle deletion on a book graph

### Literal update

Given a graph containing a triangle, choose a current triangle uniformly and
then choose one of its three edges uniformly and delete that edge.  Stop when
the graph is triangle-free.  The carrier `B_r` consists of `r` triangles sharing
one common spine edge; page `i` has its two private side edges.

### Exact pilot

As long as the spine survives, the current triangles are exactly the unresolved
pages.  A step deletes the common spine with probability `1/3`, simultaneously
destroying every remaining triangle, or resolves the chosen page by deleting a
private side edge with probability `2/3`.

Let `T_r` be the clock.  Then

`P(T_r=t)=(2/3)^(t-1)/3` for `1<=t<r`,

`P(T_r=r)=(2/3)^(r-1)`.

For a subset `S` of `s<=r-1` pages and a choice of one deleted side on each page
in `S`, the terminal graph in which precisely those sides and the common spine
are deleted has mass

`1 / (3^(s+1) C(r,s))`.

For a side-choice word on all `r` pages, the terminal graph retaining the spine
and deleting those `r` private sides has mass `3^(-r)`.  Thus there are exactly

`sum_{s=0}^{r-1} C(r,s)2^s + 2^r = 3^r`

absorbing graphs, all with an explicit mass.  For `r>=2`, immediate spine
deletion is the unique maximum-mass endpoint, of mass `1/3`.

The labelled recursion and the formula were compared for every `1<=r<=7`,
including all 2,187 endpoints when `r=7`.

### All-parameter theorem contract and proof engine

The proposed theorem package is already deductive:

1. complete absorber classification and the exact `3^r` census;
2. the truncated-geometric sharp clock law;
3. every-target endpoint masses and unique maximum-mass endpoint;
4. exact history factorization: a fixed order of `s` resolved pages followed
   by spine deletion has mass `1/[3^(s+1)(r)_s]`, while a fixed all-page order
   with retained spine has mass `1/[3^r r!]`.

The proof uses a two-state spine decomposition, followed by exchangeability of
the unresolved page set.  No asymptotic or numerical step is needed.

### Collision and final decision

The independent audit found an exact internal conjugacy.  Form the triangle
hypergraph whose vertices are graph edges and whose hyperedges are graph
triangles.  Deleting a selected graph edge is exactly recording a selected
hypergraph vertex and removing every hit hyperedge.  For an `r`-page book this
hypergraph is the P136 sunflower with

`c=1`, `m=r`, `p_i=2`, and `lambda_i=1`.

Every S09 clock, endpoint, absorber-count, mode, and history formula is a
literal specialization of P136's stronger heterogeneous weighted theorem.
The same encoding also places the general update inside Bar-Yehuda's
hypergraph Pitt process.  Full evidence and the projected/full-history
convention are recorded in
[`OWNER_AUDIT_S09.md`](../../phase1/OWNER_AUDIT_S09.md).

**Decision:** permanent kill — exact occupied P136 specialization and direct
general process owner.  The random-triangle-removal process remains only a
different nearest neighbour and is not the reason for the kill.

## S10 — simplicial deletion on clique windmills

### Literal update

Choose a current simplicial vertex uniformly and delete it.  Stop as soon as
the remaining graph is complete.  The carrier has clique blocks of private
sizes `m_1,...,m_r` sharing one articulation vertex.

### Exact pilot

Until only one nonempty block remains, all and only private vertices are
simplicial.  Their deletion order is a uniform permutation of `M=sum m_i`
labels, and the endpoint is the articulation together with the terminal
monochromatic run.  For a specified `s`-subset of block `i`, the exact endpoint
mass is

`s! (M-s-1)! (M-m_i) / M!`.

In particular, block `i` is the winning block with probability `m_i/M`, so if
`M` is known the winner law identifies the entire block-size vector.  Six mixed
block profiles were checked exactly.

### All-parameter theorem and proof engine

The proof is the uniform-permutation terminal-run calculation.  The inverse
statement follows immediately from `P(winner=i)=m_i/M`.

### Collision and owner search

Simplicial deletion is a perfect elimination ordering of a chordal graph; the
direct structural owner is Dirac's characterization, discussed in
[Dirac's theorem on chordal graphs and Alexander duality](https://doi.org/10.1016/j.ejc.2003.12.008).
On this windmill family the stochastic refinement collapses completely to a
terminal run under sampling without replacement.  It is also mechanistically
too close to forest leaf peeling and the `DQ1` deletion reserve.

**Decision:** permanent kill under both the PEO owner and random-scan rule.

## R11 — absorbing simple random walk on a finite spider

### Literal update and exact pilot

Let `S(ell_1,...,ell_r)` consist of a centre joined to `r` internally disjoint
paths of positive edge lengths `ell_i`.  Start simple random walk at the centre,
move uniformly to a neighbour at every step, and make every leaf absorbing.
Record both the first leaf and the absorption time `T`.

The verifier tested all `340` ordered profiles with `1<=r<=4` and
`1<=ell_i<=4`.  For each profile it compared the literal vertex-state recursion
with the rational transform below coefficient by coefficient through time
`2 sum ell_i+12`.  It also checked every endpoint mass, the first possible
atom, parity, both moments, both sharp equality classes, and the inverse.

### Complete leaf-marked clock transform

Define even continuant polynomials

`P_0(z)=0`, `P_1(z)=1`, `P_2(z)=2`,

`P_l(z)=2P_(l-1)(z)-z^2 P_(l-2)(z)`.

Equivalently `P_l(z)=z^(l-1) U_(l-1)(1/z)`, where `U_j` is the Chebyshev
polynomial of the second kind.  Put

`P(z)=product_j P_(ell_j)(z)`,

`D(z)=rP(z)-z^2 sum_i P_(ell_i-1)(z) product_(j!=i) P_(ell_j)(z)`.

Then the leaf-marked first-passage PGF is

`F_i(z)=E[z^T 1{leaf i}]
       =z^(ell_i) product_(j!=i)P_(ell_j)(z) / D(z)`.

The proof is an excursion renewal at the centre.  On arm `ell`, gambler's ruin
from its first vertex has successful transform
`1/U_(ell-1)(1/z)` and return-to-centre transform
`U_(ell-2)(1/z)/U_(ell-1)(1/z)`; the initial centre step gives the two terms in
`D`.  In particular, `F_i` has only powers congruent to `ell_i mod 2`, and its
first atom is

`P(T=ell_i, leaf i)=1/[r 2^(ell_i-1)]`.

### Moments, sharp mass extremizers, and inverse

Write

`H=sum_i 1/ell_i`, `L=sum_i ell_i`, and `C=sum_i ell_i^3`.

Evaluation and two differentiations at `z=1` give

`P(leaf i)=ell_i^(-1)/H`,

`E T=L/H`,

`Var(T)=(C-2L)/(3H)+L^2/(3H^2)`.

The endpoint law is therefore inverse length, not uniform.  For fixed arm
count `r` and total length `L`, write `L=qr+s`, `0<=s<r`.  Convexity of
`x -> 1/x` and integer smoothing give the sharp bounds

`L/[r-1+1/(L-r+1)] <= E T`

`<= L/[(r-s)/q+s/(q+1)]`.

The lower equality class is exactly a permutation of
`(L-r+1,1,...,1)`; the upper equality class consists exactly of balanced arms
whose lengths differ by at most one.

There is also a precise identifiability boundary.  The labelled endpoint
probabilities determine the primitive positive integer vector
`d=(d_i)` proportional to `(ell_i)`, but are invariant under common dilation
`ell_i -> c ell_i`.  Once `E T` is also known,

`c^2=(E T) (sum_i 1/d_i)/(sum_i d_i)`,

so the ordered arm lengths are recovered uniquely.  Thus endpoint-only scale
blindness and endpoint-plus-mean identifiability are both exact.

### Owner subtraction and decision

Simple random walk, gambler's ruin, Chebyshev continuants, electrical harmonic
measure, and generic absorbing-chain resolvents receive zero credit.  Pearce's
primary paper [*Random walks on trees*](https://doi.org/10.1016/0012-365X(80)90234-4)
already treats leaf absorption probabilities and expected walk length on a
general finite tree.  De la Iglesia and Juarez's
[*Birth-death chains on a spider*](https://arxiv.org/abs/2111.10450) is the
nearest same-carrier framework: it studies discrete half-line spiders through
matrix-valued spectral methods and includes constant-probability random walks.
Its “reflecting-absorbing factorization” is a stochastic matrix factorization,
not the present unequal finite-arm leaf boundary.

De la Peña, Gzyl, and McDonald's primary
[*Inverse problems for random walks on trees: network tomography*](https://arxiv.org/abs/math/0610821)
is the nearest inverse result located.  It assumes a known finite-tree
topology, treats internal transition probabilities as unknown, and observes
the complete joint first-hitting time/place laws at two augmented boundary
layers.  It therefore owns the broad inverse-first-passage genre, but does not
state R11's coarse-data result: a fixed simple-walk kernel, unknown integer arm
lengths, and recovery from the endpoint vector plus one mean.

Searches over arXiv, Project Euclid, ScienceDirect/Elsevier, Springer, and
exact DOI/title indexes for finite spiders, generalized stars, absorbing
leaves, first-passage transforms, Chebyshev PGFs, and inverse arm recovery did
not locate a primary source stating the conjunction above.  This is a bounded
non-hit only.  After subtracting Pearce's general endpoint/mean inputs, the
leaf-marked rational law, exact variance, sharp fixed-mass equality classes,
and endpoint-plus-mean inverse remain.

**Decision:** `PASS_OWNER_THIN / HOLD_EXTERNAL`.  This is the stochastic
replacement signal after a bounded owner audit, subject to independent
replication before any theorem contract is frozen.

## R12 — uniform-inversion swap sorting

From a permutation, choose uniformly among its current inversions and swap the
two entries; stop at the identity.  Exact recursion over every permutation
through order seven shows that the clock support has sharp endpoints

`min T=n-number_of_cycles(pi)`, `max T=inv(pi)`.

The lower endpoint is the unrestricted transposition distance.  Every
nontrivial permutation cycle contains two positions inverted by the restricted
value order (otherwise its restriction would be the identity); swapping that
pair splits the cycle, so the lower endpoint is attainable.  The upper endpoint
is attained by adjacent inversion swaps.  Every allowed swap lowers inversion
number by a positive odd integer, proving absorption and the upper bound.

This is not a replacement.  Fleischer's primary
[*Fun-Sort—or the chaos of unordered binary search*](https://doi.org/10.1016/j.dam.2004.01.003)
already studies the rule that samples two cells and swaps them exactly when
out of order; R12 is its embedded effective-swap chain.  It also falls under
the explicit generic comparator/random-sorting firewall.

**Decision:** permanent direct-owner/firewall kill.

## R13 — Bernoulli–Laplace exchange on `k`-subsets

From a `k`-subset of `[n]`, choose uniformly one occupied and one unoccupied
label and exchange them.  The state graph is the Johnson graph.  The verifier
recomputed exact returns through time six for every `2<=n<=11` and
`1<=k<=floor(n/2)`, checking the classical spectrum

`lambda_j=1-j(n-j+1)/[k(n-k)]`,

with multiplicity `C(n,j)-C(n,j-1)`.

This is exactly the Bernoulli–Laplace diffusion model, not a new subset
dynamics.  The primary literature treats the known eigenstructure explicitly;
see, for example,
[*Cutoff for the Bernoulli--Laplace urn model with o(n) swaps*](https://doi.org/10.1214/20-AIHP1052).
It also collides with the generic matroid-basis/association-scheme spectral
firewall.

**Decision:** permanent direct-owner kill.

## R14 — fair randomized halving

For `n>1`, replace an even `n` by `n/2`; for odd `n`, choose
`(n-1)/2` or `(n+1)/2` with equal probability.  Stop at one.  If
`2^k <= n <= 2^(k+1)`, the exact clock is

`Pr(T=k)=(2^(k+1)-n)/2^k`,

`Pr(T=k+1)=(n-2^k)/2^k`.

Consequently `E T=k+(n-2^k)/2^k`, the variance is `alpha(1-alpha)`
with `alpha=(n-2^k)/2^k`, and the clock law identifies `n` exactly.
The verifier proves the recursion and these formulae independently for every
`1<=n<2^16`.

This is a real exact anomaly, but not an independent paper mechanism in this
portfolio.  The proof is binary digit contraction plus one scalar affine
interpolation, the same digital normal-form spine already occupied by P100
and adjacent to P101's random contraction/synchronization lane.  There is no
separate endpoint, geometry, or history axis after that subtraction.

**Decision:** `KILL_INTERNAL_DIGIT_CONTRACTION`; do not promote the pretty
two-atom identity by itself.

## R15 — random totient--radical descent

For `n>1`, choose fairly between

`n -> phi(n)` and `n -> n/rad(n)`,

and stop at one.  Both branches strictly descend.  Exact rational recursion
was run for every `n<=5000`.  It immediately exposes an infinite inverse
failure: for every odd prime `p`, the two successors of `p` and `2p` are the
same multiset `{p-1,1}`, hence their complete absorption-clock laws agree.
The finite pilot already contains more than 2,500 repeated clock laws.

The process has termination but no endpoint axis and no clock
identifiability; the remaining arithmetic irregularity would merely outsource
the hard part to iterated-totient structure.

**Decision:** `KILL_NO_INVERSE_NO_SECOND_AXIS`.

## R16 — random derivative-GCD / squarefree reduction

Let `f=prod_i g_i^(e_i)` over characteristic zero with distinct irreducible
`g_i`.  Fairly replace `f` by `gcd(f,f')` or by its squarefree kernel, and stop
at one.  On multiplicities the two branches are

`e_i -> max(e_i-1,0)` and `e_i -> 1_{e_i>0}`.

Writing `m=max_i e_i`, the projected chain is exactly
`m -> m-1` or `m -> 1` fairly.  Thus the **entire** clock law depends only on
`m`, not on the number, degrees, labels, or remaining multiplicities of the
irreducible factors.  In particular,

`E T = 4-4/2^m`.

All exponent profiles of length at most four with entries at most six were
checked against the scalar chain through sixteen steps, together with the
exact Bellman mean.  The compression is too severe to support an inverse or
a second theorem axis.

**Decision:** `KILL_MAX_MULTIPLICITY_ONLY`.

## R17 — sequential random Kauffman smoothing

Take the closure of the positive two-braid with `n` crossings.  Repeatedly
choose an unresolved crossing uniformly and choose either smoothing fairly.
If `K` crossings receive the cup--cap smoothing, the terminal number of loops
is `L=2` for `K=0` and `L=K` otherwise.  Hence

`E[y^L]=2^(-n)((1+y)^n-1+y^2)`,

and `E L=n/2+2/2^n`.  Every smoothing word through `n=16` was checked in the
literal two-strand Temperley--Lieb multiplication.

This is not a stochastic-dynamics advance.  The order of resolving crossings
is irrelevant, and the terminal sum is exactly a specialization of Kauffman's
primary state model; see L. H. Kauffman,
[*State models and the Jones polynomial*](https://doi.org/10.1016/0040-9383(87)90009-7),
*Topology* 26 (1987), 395--407.

**Decision:** permanent direct-owner/state-sum kill.

## Kill ledger and handoff

| class | IDs | reason that survives renaming |
|---|---|---|
| direct external same-object transfer | S01, S02, S03, S04, S05 | peaks, random MST, OK-Corral, linear extensions, hook formula |
| generic random-order/quota/sorting transfer | S06, S07, S10, R12 | independent last survivors, negative-binomial quota, terminal run, random inversion sorting |
| direct process or internal transfer | S08, S09, R13 | annihilation process, exact P136 sunflower specialization, Bernoulli--Laplace diffusion |
| replacement signal | R11 | finite-spider leaf-marked PGF, variance, sharp mean extrema, and inverse; general tree endpoint/mean inputs are zero credit |
| second-pool value/internal kills | R14, R15, R16 | occupied digit contraction; infinite clock collision; maximum-multiplicity collapse |
| second-pool direct state-sum kill | R17 | random smoothing is the Kauffman bracket state model |

Recommended root actions are:

1. keep `S08` and `S09` permanently killed; neither may re-enter through a line
   graph, triangle-hypergraph, clock-rate, or endpoint relabelling;
2. send `R11` through a second independent owner/claim-subtraction replication focused on
   finite-tree leaf first passage, generalized stars, phase-type/Chebyshev
   transforms, and inverse Markov-chain identification;
3. if `R11` survives, freeze only the finite unequal-arm theorem conjunction,
   explicitly crediting general tree absorption probabilities and means to
   Pearce;
4. do not revive R12 or R13 by conditioning away null moves or renaming the
   Johnson graph.
5. record the second stochastic pool as **no selection**; none of R14--R17
   meets R11's independent multi-axis value.

## Reproduction

Run:

```bash
python docs/papers147_151_sequence/scouting/stochastic/verify_stochastic_scout.py
```

The expected byte-visible transcript is `CANONICAL.txt`.  All work remains
anonymous and internal under `HOLD_EXTERNAL`.
