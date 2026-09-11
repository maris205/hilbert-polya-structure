# Stochastic/graph/spatial Stage-1 scout — P152–P156 intake

**Date:** 2026-09-02  
**External status:** `HOLD_EXTERNAL`  
**Scope:** twelve genuinely different literal stochastic systems. Parameter
sweeps are not counted as new systems.  This is an internal falsification and
owner-subtraction record, not a novelty, priority, or release claim.

## Outcome first

Two systems survive the first value gate.

1. **HTM — hierarchical tree meet.**  Repeatedly meet the current vertex with
   an independent uniform leaf of a fixed level-homogeneous rooted tree.  The
   special tree map gives an exact all-time depth transform, a geometric root
   clock, recovery of the entire branching profile from one depth layer, and
   sharp fixed-multiset extremizers for expected depth-area.  A finite
   meet-semilattice is a left-regular band, so Brown's general semigroup-walk
   framework is assigned **zero credit**.  The only retained conjunction is
   the map-specific nested-cylinder law plus inverse and area exchange theorem.
   Status: **`SURVIVE_OWNER_THIN / HOLD_EXTERNAL`**.

2. **BTB — signed-book triad balance.**  Choose a uniformly random imbalanced
   page of a signed `r`-page triangle book and flip a uniformly random edge of
   that page.  The full sign process lumps to
   `k -> k-1` with probability `2/3` and `k -> r-k` with probability `1/3`.
   Its absorption-time/spine-flip transform is Chebyshev-rational; the mean,
   parity law, sharp clock extrema, and a two-statistic inverse are explicit.
   This is **exactly**, not merely analogous to, Istrate's probabilistic triadic
   dynamics at `p=1/3`; it is also the update-epoch chain of Antal–Krapivsky–
   Redner local triad dynamics at `p=1/3`.  Therefore the kernel, balance
   semantics, XOR/hyperedge-switching encoding, and generic absorption are all
   zero-credit.  Only the exact book-carrier theorem package survives.  Status:
   **`SURVIVE_DIRECT-KERNEL_SPECIALIZATION / HOLD_EXTERNAL`**, with high owner
   risk and a mandatory Stage-2 full-text/citation-chain audit.

The remaining ten mechanisms are killed.  Four are definition-level owners
(sink popping, voter, Young growth, Tsetlin library); three collapse into an
occupied internal engine or generic random-scan wrapper; and three have only a
single routine axis after exact reduction.  The threshold was not lowered to
manufacture more survivors.

The deterministic verifier executed **86,217 exact assertions** using only
integers and `fractions.Fraction`: 19,730 for HTM, 46,422 for BTB, and 20,065
across the ten breadth controls.

## Collision firewall

- No vertex/edge deletion, forest peeling, greedy MIS, matching, polygon-ear
  deletion, component complement, coalescence, quota/exposure process, urn/
  Johnson walk, or Cayley/random-scan wrapper is retained.
- HTM keeps the carrier tree fixed.  Its state is an ancestor obtained by a
  meet with fresh leaves; it neither contracts the tree (P148) nor performs a
  nearest-neighbour first-passage walk (P151).
- BTB keeps every edge and flips signs.  Its reflection jump can increase the
  number of imbalanced pages.  It is not the old book-edge deletion scout,
  which was an exact P136 sunflower specialization.  Its principal risk is
  external and explicit: the update kernel is already owned.
- The ten kills below remain kills even if a bounded source search missed a
  paper.  A bounded non-hit is never treated as novelty evidence.

## Exact audit table

| ID | literal update | exact small-instance signal | owner/collision result | decision |
|---|---|---|---|---|
| HTM | current vertex `meet` fresh uniform leaf | 363 branching profiles, 121 extremal families | Brown LRB/semigroup framework zero-credit; no direct special conjunction hit in bounded search | **SURVIVE owner-thin** |
| BTB | choose imbalanced book page; flip one of its three edges uniformly | all 1,013 nonzero bit states through `r=9`; 80 rational transform cases | exact Istrate `p=1/3` kernel; residual is special-carrier law only | **SURVIVE direct-kernel specialization** |
| SPP | choose a sink of an oriented cycle; resample its two incident arrows | uniform-start means `3,6,10,15` for `n=3..6` | exact Cohn–Pemantle–Propp sink popping | **KILL** |
| PCF | choose two elements in one nontrivial permutation cycle; transpose them | split multiplicities through `n=10`; history counts `3,16,125,1296,16807` | random-transposition fragmentation/Cayley history; internal cycle/random-order collision | **KILL** |
| VOS | on a star choose a discordant edge and copy one endpoint to the other fairly | from `(hub=A,0 A-leaves)`, `E T=m`, `P(A)=1/(m+1)` through `m=12` | update-epoch chain of link-update voter dynamics; close to first-passage lane | **KILL** |
| RGE | sample a fresh uniform residue modulo `x`; set `x <- gcd(x,U)` | all-time laws through `t=6` for `12,18,30,60,210` | only prime support visible; occupied valuation/GCD engine | **KILL** |
| BCS | sample a uniform lower sub-box by replacing every upper coordinate independently | exact means for `(2)^d`, `d<=8`, and `(2,3),(3,3),(2,3,4)` | product of one-coordinate contractions; no second independent axis | **KILL** |
| RRO | over `F_2`, add a uniformly sampled rank-one matrix `uv^T` | every rank kernel for `1<=m,n<=4`, plus detailed balance | bilinear-forms association scheme owns rank geometry; generic birth–death quotient | **KILL** |
| TCE | in a fixed graph choose an eligible nonedge with a common neighbour and add it | path history counts `1,1,4,204,280848,18163801920` for `n=2..7` | triadic-closure mechanism; endpoint and clock deterministic | **KILL** |
| DMF | choose an addable Young cell uniformly and grow to a rectangle | history counts `2,5,462` for `2x2,2x3,3x4`; all partitions through size 10 | exact standard-tableau/hook-length object | **KILL** |
| CME | continuous-time reversible dimerization `2A <-> B` at mass action rates | weights `1,6,3` at mass 4 and `1,15,45,15` at mass 6 | product-form CRN/detailed-balance owner; one routine stationary axis | **KILL** |
| HFW | choose a label with fixed weight and move it to the front | weighted stationary law through `n=6`; exact equal-weight two-step law | exact Tsetlin library / semigroup walk | **KILL** |

## HTM — hierarchical tree meet

### Literal system

Fix height `h>=1` and branching profile

`b=(b_1,...,b_h)`, with every `b_i>=2`.

Vertices at depth `d` are words of length `d`, and a leaf is a word of length
`h`.  Fix the distinguished leaf `v=00...0`.  Put `X_0=v`.  At each integer
time sample an independent uniform leaf `U_t` and set

`X_t = LCA(X_{t-1},U_t)`.

Let `D_t` be the depth of `X_t`, let `B_0=1` and
`B_k=product_{j=1}^k b_j`, and let `T=inf{t>=1:D_t=0}`.

This update is literal and closed: every state lies on the root-to-`v` path,
and `D_t=min(D_{t-1},L_t)`, where `L_t` is the longest common-prefix length of
`v` and `U_t`.

### Exact pilot

The verifier enumerates every sampled leaf for every depth state of all 363
profiles of heights `1..5` with factors in `{2,3,4}`.  It then iterates the
literal rational kernel for seven time layers.  It also checks two all-time
transform points per profile, the Bellman depth-area, inverse recovery, and all
121 multisets of length `2..5` over `{2,3,4,5}`.

For example, for `b=(2,3,4)`,

`E sum_{t>=0} D_t = 3 + 1/(2-1) + 1/(6-1) + 1/(24-1) = 488/115`.

### Full-parameter theorem package

**HTM-1, pathwise product identity and layer law.**  For every `t>=0`,

`X_t=LCA(v,U_1,...,U_t)`

and, for `1<=k<=h`,

`P(D_t>=k)=B_k^{-t}`.

For `t>=1`, this gives

`P(D_t=0)=1-b_1^{-t}`,

`P(D_t=d)=B_d^{-t}-B_{d+1}^{-t}` for `1<=d<h`, and

`P(D_t=h)=B_h^{-t}`.

**HTM-2, all-time depth transform.**  For `|z|<1`,

`sum_{t>=0} z^t E[y^{D_t}]`

`= 1/(1-z) + sum_{k=1}^h (y^k-y^{k-1})/(1-z/B_k)`.

Thus the complete depth process has a finite rational transform whose poles
are the reciprocal cylinder masses.

**HTM-3, root clock.**  `T` is geometric on `{1,2,...}` with

`P(T>t)=b_1^{-t}`,

`E[z^T]=(b_1-1)z/(b_1-z)`,

`E T=b_1/(b_1-1)`, and

`Var(T)=b_1/(b_1-1)^2`.

The clock sees only `b_1`; this nonidentifiability is part of the theorem, not
hidden.

**HTM-4, inverse boundary.**  One known positive-time depth layer recovers all
prefix products from

`B_k=P(D_t>=k)^{-1/t}`,

and then `b_k=B_k/B_{k-1}`.  In particular, the time-one layer gives a purely
rational/integer reconstruction.  Clock-only data cannot recover `b_2,...,b_h`.

**HTM-5, depth-area and sharp fixed-multiset extremizers.**  With

`A=sum_{t>=0} D_t`,

`E A = sum_{k=1}^h B_k/(B_k-1)`

`= h + sum_{k=1}^h 1/(B_k-1)`.

Among all orderings of a fixed multiset of branching factors, the nonincreasing
ordering uniquely minimizes `E A` and the nondecreasing ordering uniquely
maximizes it, modulo swapping equal factors.

### Proof engine and boundaries

Associativity of LCA/meet yields the pathwise identity.  The event `D_t>=k`
is the intersection of `t` independent depth-`k` cylinders, each of mass
`1/B_k`.  Tail summation gives HTM-2 and HTM-5.  HTM-3 is the first sample
whose first symbol differs from that of `v`.  For the extremizer, swap adjacent
factors `a,b` after prefix product `P`: all later prefix products agree, and
the sole changed term is `1/(Pa-1)` versus `1/(Pb-1)`.  This strict adjacent
exchange proves both sharp orders.

The assumptions `h>=1`, `b_i>=2`, a fixed level-homogeneous tree, a fixed
starting leaf, and independent uniform leaf samples are essential.  Allowing
nonuniform leaves replaces cylinder masses by arbitrary nested masses; allowing
irregular trees destroys recovery of a single branching profile.

### Owner subtraction

Kenneth Brown's primary paper
[Semigroups, rings, and Markov chains](https://arxiv.org/abs/math/0006145)
analyzes random walks on left-regular bands.  A finite meet-semilattice is a
commutative idempotent semigroup and hence lies in that framework.  Therefore
the semigroup encoding, generic random-product viewpoint, spectral
diagonalization, and idempotent structure receive **zero credit** here.

The retained conjunction is narrower and map-specific: uniform tree-cylinder
tails `B_k^{-t}`, the single-layer reconstruction of every branching factor,
and the strict prefix-product exchange theorem for depth-area.  Bounded searches
of arXiv and journal indexes for `random LCA`, `random lowest common ancestor`,
`longest common prefix Markov chain`, and `semilattice meet Markov chain` found
LCA data structures, random-tree questions, and generic semigroup walks, but no
direct owner of that conjunction.  This is a **bounded non-hit only**.

**Decision:** survive owner-thin.  Stage 2 must search MathSciNet/Zentralblatt
and citation chains before any paper assignment.

## BTB — signed-book triad balance

### Literal system

Let `B_r` be the graph of `r>=1` triangles sharing one spine edge; every page
has two private edges.  Give every edge a sign in `{+1,-1}`.  Page `i` is
imbalanced when the product of its three signs is `-1`; write its bit as
`x_i=1`.  If at least one page is imbalanced:

1. choose an imbalanced page uniformly;
2. choose one of its three edges uniformly;
3. flip the chosen sign.

Stop when all pages are balanced.  Let `K_t=sum_i x_i`, let `T` be the number
of updates to absorption, and let `J` be the number of spine flips before
absorption.

A private-edge flip changes only the selected bit from one to zero.  A spine
flip complements every bit.  Hence the full `2^r` imbalance process is strongly
lumpable by `K_t`, with

`k -> k-1` with probability `2/3`,

`k -> r-k` with probability `1/3`.

If the two targets agree, their probabilities add.  At `r=1`, every update
absorbs in one step.

### Exact pilot

All 1,013 nonzero imbalance vectors through `r=9` were enumerated from the
literal choice of active page and physical edge.  Four rational `(z,u)` points
were tested for every `r<=20` by independently solving the full first-step
linear system and comparing it with the Chebyshev expression.  Direct rational
systems for means and spine parity were solved through `r=25`; extremizers and
the inverse were tested through `r=200`.

For `r=7`, the exact expected times from `k=1,...,7` are

`4,7,9,10,10,9,7`.

### Full-parameter theorem package

Define

`F_k(z,u)=E_k[z^T u^J]`, with `F_0=1`.

**BTB-1, exact Bellman system.**  For `1<=k<=r`,

`F_k=z[(2/3)F_{k-1}+(u/3)F_{r-k}]`.

**BTB-2, Chebyshev rational transform.**  Let `U_j` be the Chebyshev
polynomial of the second kind, put `U_{-1}=0`, and set

`xi=[9+z^2(4-u^2)]/(12z)`.

For `r>=2`,

`F_k=U_{k-1}(xi)F_1-U_{k-2}(xi)`,

where

`F_1=[3U_{r-2}(xi)-2zU_{r-3}(xi)+zu]`

`    /[3U_{r-1}(xi)-2zU_{r-2}(xi)]`.

For `r=1`, `F_1=z(2+u)/3`.  The formula is an identity of rational functions;
as a probability transform it is used for `|z|<1, |u|<=1`, with boundary
values obtained by continuity where appropriate.

**BTB-3, mean and sharp clock extrema.**

`E_k T = k(r+2-k)/2`.

For `r>1`, the unique minimum is at `k=1`, with value `(r+1)/2`.  The maximum
is attained at `k=(r+2)/2` when `r` is even, and at the two nearest integers
`(r+1)/2,(r+3)/2` when `r` is odd.  Its value is

`floor((r+2)^2/4)/2`.

For `r=1`, the only state is both minimum and maximum.

**BTB-4, spine parity.**

`E_k[(-1)^J]=(r+2-2k)/(r+2)`, hence

`P_k(J odd)=k/(r+2)`.

**BTB-5, coarse-data inverse.**  For a nonabsorbing start, let

`q=P(J odd)` and `m=E T`.

Then

`r+2=sqrt[2m/{q(1-q)}]` and `k=q(r+2)`.

Thus `(m,q)` recovers both integer parameters, subject to the evident
integrality/feasibility check `r>=1`, `1<=k<=r`.

### Proof engine and boundaries

The physical edge enumeration proves lumpability.  Eliminating the reflected
term `F_{r-k}` from adjacent Bellman equations gives

`F_{k+1}=2xi F_k-F_{k-1}`,

and the `k=r` Bellman equation supplies the displayed boundary ratio.  First
derivatives at `(z,u)=(1,1)`, or direct elimination, yield the quadratic mean;
evaluation at `(z,u)=(1,-1)` yields the affine parity law.  Concavity of the
mean gives the exact extrema, and algebra gives the inverse.  Almost-sure
absorption follows because any block of `r` consecutive private choices has
positive probability and forces the count to zero.

The theorem uses update epochs: there are no balanced-page no-op selections.
If one instead samples uniformly from all `r` pages, BTB is the embedded jump
chain and physical time acquires state-dependent geometric holding times.
Nonuniform edge choices replace the coefficient `2/3`; nonuniform page choices
destroy the one-dimensional count lumping.

### Direct owner subtraction

Antal, Krapivsky, and Redner define local triad dynamics in
[Dynamics of Social Balance on Networks](https://arxiv.org/abs/cond-mat/0506476).
Their paper states that at `p=1/3` each edge of an imbalanced triad is flipped
equiprobably.  Their base clock samples all triads and permits balanced no-ops;
conditioning on an update gives the present page selection.

Istrate's
[On the dynamics of Social Balance on general networks](https://arxiv.org/abs/0811.0381)
is even closer: Definition 2 selects a uniformly random imbalanced triangle,
and at `p=1/3` selects each of its three edges with probability `1/3`.
Consequently BTB is **the same kernel on the book carrier**, not a neighbouring
model.  Istrate also supplies the general XOR/hyperedge-switching duality.  The
book's triadic dual is one `r`-vertex hyperedge (the shared spine) plus two
self-loops at every page (the private edges).

Accordingly, zero credit is assigned to the update, the balance interpretation,
the full-graph state space, generic absorption/reachability, and the hypergraph/
XOR reformulation.  The residual is precisely the special-carrier quotient and
the conjunction of its bivariate Chebyshev transform, quadratic sharp clock,
spine parity, and inverse.  Bounded searches for `signed book graph social
balance`, `book graph triadic dynamics`, `shared-edge triangles edge flip`, and
`star XOR RandomWalkSAT exact absorption` found the general owners above but
no book-specific exact law.  Again, that is only a bounded non-hit.

**Decision:** provisional survive as a direct-kernel special-carrier theorem
package.  This is the riskier of the two survivors; any direct book-law owner
kills it immediately.

## SPP — cycle sink popping

### Definition and exact pilot

Orient the edges of `C_n`.  While a sink exists, choose a sink uniformly and
resample its two incident orientations independently and fairly.  For uniform
initial orientations, exact absorbing-system solves give

`E T = 3,6,10,15 = C(n,2)` for `n=3,4,5,6`,

and probability `1/2` for either of the two directed-cycle endpoints.

### Theorem profile, owner, decision

There is no surviving theorem conjecture: the all-`n` identity
`E T=C(n,2)` is already Proposition 4.10 of Cohn, Pemantle, and Propp, which
also gives the conditional mean `2j(n-j)` from `j` clockwise arrows.  Their
algorithm allows any legal sink scheduler, so the uniform scheduler here is an
explicit specialization of exactly the same sink-resampling kernel:
[Generating a random sink-free orientation in quadratic time](https://arxiv.org/abs/math/0103189),
with later sharp runtime analysis by Guo and He,
[Tight bounds for popping algorithms](https://arxiv.org/abs/1807.01680).

**KILL — direct same-object/same-kernel owner.**

## PCF — permutation-cycle fragmentation

### Definition and exact pilot

From a permutation, choose uniformly a pair lying in the same nontrivial
cycle and compose with that transposition.  The chosen cycle splits; stop at
the identity.  For a single `n`-cycle the clock is deterministically `n-1`.
An `a+(n-a)` split has `n` transpositions when `a != n-a` and `n/2` when
`a=n/2`.  The numbers of complete minimal histories for `n=3..7` are

`3,16,125,1296,16807 = n^{n-2}`.

### Theorem profile, owner, decision

The proposed theorem would combine the split kernel with the Cayley/Dénes
minimal-factorization count.  Random transposition cycles are already treated
as coagulation-fragmentation, for example by Berestycki and Durrett in
[A phase transition in the random transposition random walk](https://arxiv.org/abs/math/0403259),
and explicit permutation fragmentation is treated by Goldschmidt, Martin, and
Spanò in [Fragmenting random permutations](https://arxiv.org/abs/0712.0556).
Internally, the history count is another Cayley/random-order wrapper and the
cycle primitive neighbours the occupied cycle-pruning lane.

**KILL — direct classical fragmentation plus internal firewall.**

## VOS — voter model on a star

### Definition and exact pilot

On a star with `m` leaves, choose a discordant hub–leaf edge uniformly and
then choose one endpoint fairly to copy the other's colour.  Start with an
`A` hub and all-`B` leaves.  The effective state is hub colour plus the number
of `A` leaves.  Exact systems through `m=12` give

`E T=m`, and `P(A consensus)=1/(m+1)`.

### Theorem profile, owner, decision

First-step elimination proves both identities for all `m`, and the two-line
state graph also gives a rational transform.  More precisely, this scheduler
is the embedded update-epoch chain of **link-update** voter dynamics (choose an
edge and a copying direction, then suppress concordant no-ops), not the
site-update Holley–Liggett kernel on an irregular graph.  Link-update consensus
times on networks are already treated directly by Castellano in
[Effect of network topology on the ordering dynamics of voter models](https://arxiv.org/abs/cond-mat/0504522).
The primary classical voter reference is Holley–Liggett,
[Ergodic Theorems for Weakly Interacting Infinite Systems and the Voter Model](https://doi.org/10.1214/aop/1176996306).
The star quotient is a persistent one-dimensional walk and is too close in
shape to the just-completed first-passage lane.

**KILL — direct kernel and insufficient owner-subtracted mass.**

## RGE — fresh-residue GCD erosion

### Definition and exact pilot

From integer `x>1`, draw `U` uniformly from `{0,...,x-1}` and set
`x <- gcd(x,U)`; stop at one.  If `P(n)` is the set of prime divisors of `n`,
exact iteration confirms

`P(T<=t)=product_{p|n}(1-p^{-t})`.

Thus

`E T=sum_{nonempty S subseteq P(n)} (-1)^{|S|+1} d_S/(d_S-1)`,

where `d_S=product_{p in S}p`.  Examples are `23/10` for both `12` and `18`,
`87767/36540` for both `30` and `60`, and
`1563526089677/636617813832` for `210`.

### Theorem profile, owner, decision

CRT independence proves the all-time law; the law recovers only the radical,
never prime exponents.  A bounded exact-literal search found no direct paper,
but the entire engine is independent prime-valuation death and duplicates the
portfolio's occupied valuation/GCD/digit-contraction silhouette.

**KILL — internal engine collision despite a clean formula.**

## BCS — coordinatewise bounding-box contraction

### Definition and exact pilot

At upper corner `u=(u_1,...,u_d)`, independently sample
`V_i` uniformly from `{1,...,u_i}` and replace `u` by `V`; stop at all ones.
For `u=(2,...,2)`, the coordinate clocks are independent geometric variables,
so

`E T=sum_{j=1}^d (-1)^{j+1} C(d,j)/(1-2^{-j})`.

Literal recursions verify this through `d=8`.  Other exact means are `91/30`
for `(2,3)`, `401/120` for `(3,3)`, and `4647667/1204280` for `(2,3,4)`.

### Theorem profile, owner, decision

The general law is the maximum of independent one-coordinate contraction
clocks.  Inclusion–exclusion supplies a transform, but there is no interacting
second axis, sharp structural extremizer, or useful inverse beyond factor
recovery from independent poles.  The bounded search found only generic
contraction/max-geometric neighbours, not a direct literal owner.

**KILL — exact but theorem-thin and close to occupied coordinate synchronization.**

## RRO — random rank-one addition over a finite field

### Definition and exact pilot

For `A in F_2^{m x n}`, sample uniform `u in F_2^m` and `v in F_2^n`, including
zero, and set `A <- A+uv^T`.  Rank is a Markov quotient.  From rank `k`,

`p_up=(2^m-2^k)(2^n-2^k)/2^{m+n}`,

`p_down=(2^k-1)2^{k-1}/2^{m+n}`,

and the residual mass stays at `k`.  Every literal matrix update for
`1<=m,n<=4` agrees, and detailed balance agrees with the exact number of
rank-`k` matrices.  The full `3x3` kernels appear in the frozen transcript.

### Theorem profile, owner, decision

Row/column reduction and the rank-one update criterion prove the formulas for
general `q`; generalized Krawtchouk polynomials would diagonalize the quotient.
That is precisely the rank geometry of Delsarte's bilinear-forms association
scheme,
[Bilinear forms over a finite field, with applications to coding theory](https://doi.org/10.1016/0097-3165%2878%2990015-8).

**KILL — classical association-scheme quotient; generic spectrum only.**

## TCE — fixed-vertex triadic-closure growth

### Definition and exact pilot

Start from `P_n`.  At each step choose uniformly among distinct missing edges
whose endpoints have a common neighbour and add that edge.  A connected graph
with no eligible nonedge is complete, so the endpoint is `K_n` and the clock is
deterministically `C(n,2)-(n-1)`.  Exact legal-edge history counts for
`n=2..7` are

`1,1,4,204,280848,18163801920`.

### Theorem profile, owner, decision

A subset recurrence computes the history sequence, but no product, inverse, or
second stochastic statistic appeared in the first round.  Triadic closure is a
standard network-growth mechanism; a primary source is Holme and Kim,
[Growing scale-free networks with tunable clustering](https://doi.org/10.1103/PhysRevE.65.026107).
That carrier is not the present fixed path, so the collision is mechanism-level
rather than same object; the decisive issue is theorem thinness.

**KILL — deterministic endpoint/clock and no second axis.**

## DMF — uniform addable-cell Young growth

### Definition and exact pilot

Inside a fixed rectangle, choose an addable Young cell uniformly and add it;
stop at the rectangle.  Reversing a complete history gives a standard Young
tableau.  Exact corner recursions agree with the hook formula for every
partition through size ten.  Counts for `2x2`, `2x3`, and `3x4` are
`2,5,462`.

### Theorem profile, owner, decision

The all-shape history count is `|lambda|!/product_c h(c)`.  This is the exact
standard-tableau object, with the probabilistic hook treatment of Greene,
Nijenhuis, and Wilf in
[A probabilistic proof of a formula for the number of Young tableaux of a given shape](https://doi.org/10.1016/0001-8708%2879%2990023-9).
It also violates the internal hook/linear-extension firewall.

**KILL — definition-level owned object.**

## CME — reversible dimerization CTMC

### Definition and exact pilot

Fix total monomer mass `N=a+2b`.  Use the continuous-time mass-action reactions

`2A -> B` at rate `C(a,2)`, and `B -> 2A` at rate `b`.

The birth–death stationary weights satisfy

`w_0=1`, `w_{b+1}=w_b C(N-2b,2)/(b+1)`.

Exact detailed balance was checked for every `2<=N<=30`.  The unnormalized
weights are `(1,6,3)` for `N=4` and `(1,15,45,15)` for `N=6`.

### Theorem profile, owner, decision

The recurrence gives the stationary law immediately, but this is a routine
weakly reversible mass-action network.  Gillespie's primary formulation is
[Exact stochastic simulation of coupled chemical reactions](https://pubs.acs.org/doi/10.1021/j100540a008),
and product-form stationary laws for complex-balanced systems are established
by Anderson, Craciun, and Kurtz in
[Product-form stationary distributions for deficiency zero chemical reaction networks](https://arxiv.org/abs/0803.3042).

**KILL — direct general theory and only a routine stationary axis.**

## HFW — weighted random-to-front library

### Definition and exact pilot

At each step choose label `i` with fixed probability proportional to `w_i`
and move it to the front of the current permutation.  For front-to-back order
`sigma`, the stationary law is

`pi(sigma)=product_j w_{sigma_j}/sum_{ell>=j}w_{sigma_ell}`.

Exact invariance was checked for weights `(1,2,...,n)` through `n=6`.  The
identity masses are `1/3,1/15,1/105,1/945,1/10395`.  Starting from `123` with
equal weights, the exact two-step masses are `2/9` on `123,213,312` and `1/9`
on the other three permutations.

### Theorem profile, owner, decision

This is the Tsetlin library itself, already included in the semigroup-walk
framework of Brown and described directly in current primary work such as
[q-deformations of the Tsetlin library](https://arxiv.org/abs/2601.21195).
It is also a generic random-scan wrapper forbidden by the internal firewall.

**KILL — exact same kernel/direct owner.**

## Owner-first search ledger

Only primary/author-hosted arXiv records and official journal/DOI landing pages
were used.  Search-engine snippets, surveys, and tertiary pages were not used
as claim evidence.

| query family | databases/endpoints | classification and subtraction |
|---|---|---|
| `semigroup meet Markov chain`, `random LCA`, `longest common prefix Markov chain` | arXiv, Brown primary record, journal indexes | Brown is a **generic-framework owner**; all LRB/semigroup credit removed. No direct HTM conjunction hit in bounded search. |
| `social balance signed book graph`, `book graph triadic dynamics`, `shared-edge triangles flip` | arXiv full text for Antal–Krapivsky–Redner and Istrate | Istrate is **same kernel**, not nearest neighbour; generic triad/XOR/hypergraph claims removed. No book-law hit in bounded search. |
| `cycle sink popping` | arXiv primary records | Cohn–Pemantle–Propp is **same object/same kernel**; permanent kill. |
| `random transposition fragmentation permutation cycles` | arXiv primary records | direct coagulation-fragmentation neighbourhood plus Cayley history; kill. |
| `voter model star absorption`, `link-update voter dynamics` | arXiv, APS, Project Euclid/DOI | same link-update event kernel after suppressing no-ops; special star quotient not enough. |
| `random gcd uniform residue Markov chain` | arXiv, journal indexes | no direct literal hit; internal valuation/GCD collision independently kills. |
| `uniform sub-box contraction Markov chain` | arXiv, journal indexes | no direct literal hit; one-axis value kill. |
| `rank-one addition finite-field matrix rank chain` | ScienceDirect/DOI, arXiv | bilinear-forms association scheme is direct rank-geometry owner; kill. |
| `triadic closure random edge addition` | APS/DOI, arXiv | generic mechanism owner; fixed-path enumeration remains thin. |
| `Young addable corner random growth hook` | ScienceDirect/DOI | exact tableau/hook object; kill. |
| `reversible dimerization stochastic stationary`, `product form CRN` | ACS/DOI, arXiv | general stochastic chemistry and product-form owners; kill. |
| `Tsetlin library random to front` | arXiv, Brown primary record | exact same kernel; kill. |

The two survivor searches must be repeated with MathSciNet, Zentralblatt,
Crossref citation chains, and full-text reference chasing before Stage 2.  The
present database access is not sufficient for a novelty conclusion.

## Reproducibility contract

- Run `PYTHONDONTWRITEBYTECODE=1 python3 verify_stochastic_scout.py` from this
  directory or the repository root.
- The output must compare byte-for-byte with `CANONICAL.txt`.
- The verifier has no randomness, timestamps, network access, third-party
  packages, or floating-point arithmetic.
- The frozen transcript is evidence for the formulas tested, not evidence of
  originality.

**Final Stage-1 disposition:** HTM and BTB remain internal candidates under
`HOLD_EXTERNAL`; all ten other systems are killed.
