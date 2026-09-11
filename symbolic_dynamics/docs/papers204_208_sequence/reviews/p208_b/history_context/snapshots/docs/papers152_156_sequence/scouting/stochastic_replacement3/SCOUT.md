# Stochastic replacement-3 breadth scout — P152–P156

**Audit date:** 2026-09-02 UTC  
**External status:** `HOLD_EXTERNAL`  
**Scope:** eight literal stochastic dynamics not used in the first two
P152--P156 stochastic pools.  This is an internal owner and theorem-value gate,
not a novelty, priority, or release claim.

## Outcome first

The third replacement round also closes with an empty pool:

```text
systems tested = 8
paper-sized survivors = 0
kills = 8
exact assertions = 41,355
status = PASS_EMPTY_POOL
```

No threshold was lowered to fill a fifth seat.  The two clearest early signals
were hostilely subtracted:

- **LIT, Latin intercalate trades:** all 12 order-3 squares are frozen, whereas
  the fixed-rectangle chain is connected on all 576 order-4 squares and the
  number of active trades varies from 4 to 12.  Wanless directly owns the
  intercalate/cycle-switch graph program.  After that subtraction there is no
  closed all-order temporal transform, inverse, or clock extremizer.
- **SMB, blocking-pair matching:** two explicit `3 x 3` preference profiles
  each have two stable endpoints and nontrivial rational mean clocks, including
  `637/82`.  Roth--Vande Vate study the same random blocking-pair kernel and
  prove almost-sure convergence plus accessibility of every stable endpoint.
  The remaining profile-by-profile linear solve is generic.

The next controls were also below threshold.  AIMD has exact finite stationary
laws but only a trivial one-row rate inverse; Gray-cube Random-Edge has an exact
clock recurrence but is ordinary AUSO first passage; strict 2-opt has a
deterministic endpoint in both pilots; asynchronous deferred acceptance has a
deterministic endpoint *and* deterministic proposal count.  DBM and PPT are
directly owned dynamical models.

## Intake and collision firewall

- None of the eight literal systems is HTM, BTB, a tree meet, signed-book
  process, graph deletion, forest/ear peeling, urn/Johnson walk, random mapping,
  riffle shuffle, Bulgarian solitaire, RSK growth, modular carry addition,
  finite-field Schur pivoting, or compatible polygon insertion.
- They are also not cosmetic variants of P147--P151: there is no run
  consolidation, tree-level contraction, peak extraction, Lyness map, or
  spider walk.
- A fixed-slot or active-choice Markov scheduler receives no credit by itself.
  In particular, uniform stationarity of LIT/PPT and the recurrences for
  RSP/R2O are treated as generic controls.
- Ordinary first-passage recurrences, static MacMahon/Latin/TSP counts, finite
  rational linear solves, and generic matrix resolvents are assigned zero.
- SMB and RDA use preference matchings, not the greedy graph matching/MIS lane.
  Their direct external owners kill them before that distinction can carry a
  claim.
- A bounded owner non-hit is never used as evidence of novelty.

## Exact audit table

| ID | literal update | exact pilot and earliest signal | owner/theorem subtraction | decision |
|---|---|---|---|---|
| DBM | refresh a uniformly tie-broken global minimum and its two cycle neighbours with fresh discrete fitnesses | every state for `3<=n<=5`, alphabets 2 and 3; at `n=5,q=3,t=3`, full support and `E min=67907/354294` | discrete specialization of Bak--Sneppen; only generic finite layers remain | **KILL_DIRECT** |
| LIT | choose a row-pair/column-pair slot; trade it iff it is an intercalate | `n=3`: 12 isolated states; `n=4`: one 576-state component, 4--12 active slots | Wanless directly owns cycle/intercalate switch graphs; no closed temporal/inverse axis | **KILL_DIRECT_OBJECT** |
| PPT | choose a box cell and add/remove direction uniformly; toggle one cube iff the plane partition remains legal | MacMahon counts `10,20,50`, exact uniform stationary and volume complement symmetry | exact lozenge-tiling single-flip Glauber dynamics is owned; MacMahon is static | **KILL_DIRECT** |
| SMB | choose a blocking pair uniformly; match it and free former partners | two size-3 profiles, each with 2 stable endpoints; means `637/82` and `36186760832205392/4520768244784785` | exact Roth--Vande Vate random path to stability | **KILL_DIRECT** |
| AIM | with loss probability `p`, halve the capped window; otherwise increase it by one | caps 4--12, `p=1/3,2/5`; exact stationary and six time layers | AIMD mechanism is classical; finite stationary solve, trivial transition inverse, no second axis | **KILL_OWNER_THIN** |
| RSP | on a Gray-ranked cube, choose a uniformly random outgoing edge of the rank orientation | complete clocks through dimension 7; top means from `2` to a large rational, support doubles | Random-Edge on AUSOs/Klee--Minty cubes is direct algorithmic owner; recurrence is ordinary first passage | **KILL_DIRECT_PROGRAM** |
| R2O | from a Euclidean tour, choose uniformly among strict length-decreasing 2-opt moves | all 60 and 360 undirected anchored tours at `n=6,7`; exactly one local optimum in each pilot | Croes owns 2-opt; random active scheduler adds only instance-specific descent | **KILL_THIN** |
| RDA | choose a free proposer uniformly and execute its next deferred-acceptance proposal | exact state DAGs for sizes 3 and 4; one endpoint and one proposal count per profile | Gale--Shapley owns DA; scheduler randomness is a zero-credit order wrapper | **KILL_DEGENERATE** |

## 1. DBM — discrete Bak--Sneppen minimum refresh

### Literal system

Fix a cycle of `n>=3` sites and an alphabet `{0,...,q-1}`, `q>=2`.  A state is
`x=(x_0,...,x_{n-1})`.  Find the minimum fitness and choose uniformly among
sites attaining it.  Replace the selected site's value and the values of its
two cycle neighbours by independent uniform alphabet values.  All other sites
hold.

This is a discrete tie-resolved finite version of the extremal-neighbour
refresh rule.  It is neither a random scan of all sites nor an edge/vertex
deletion.

### Exact pilot and theorem ceiling

The verifier constructs every transition from every state for
`3<=n<=5`, `q in {2,3}`.  It checks stochastic rows, closure, and rotation
equivariance, then iterates three rational layers from the all-zero state.  For
`n=5,q=3`, all `3^5=243` states already have positive mass at time three and

```text
E[min_i X_i(3)] = 67907/354294.
```

The literal first-step operator gives finite layer recurrences, but no
all-parameter transform, inverse of `(n,q)` from a nontrivial observation, or
sharp configuration extremizer emerged.  Full support at time three is a
mixing diagnostic, not a theorem axis.

### Owner subtraction and decision

Bak and Sneppen introduce the global-minimum plus neighbour-refresh mechanism.
Discretizing fitness values and uniformly resolving ties does not create a new
mechanism.  The model, extremal selection, neighbour refresh, avalanche and
criticality framing all receive zero credit.

**Decision:** `KILL_DIRECT`.

## 2. LIT — fixed-rectangle Latin intercalate trades

### Literal system

Fix a labelled Latin square `L` of order `n`.  A scheduler slot consists of an
unordered pair of rows and an unordered pair of columns, so there are

```text
R = binom(n,2)^2
```

slots.  Choose one uniformly.  If its `2 x 2` subarray is

```text
a b
b a       with a != b,
```

replace it by `b a / a b`; otherwise hold.  The move is an involution.

### Exact pilot and attempted theorem package

Every labelled Latin square of orders 3 and 4 is independently generated from
row permutations.  The exact boundary is

```text
n=3: 12 squares, zero active intercalates, 12 singleton components;
n=4: 576 squares, 4..12 active intercalates, one connected component.
```

Let `A_n` be the intercalate-switch adjacency matrix and `D_n` the diagonal
matrix of active-trade counts.  The fixed scheduler gives the exact identity

```text
P_n = I - D_n/R + A_n/R.                          (LIT.1)
```

Since every edge is reversible, `P_n` is symmetric and the uniform law is
stationary.  This is the complete analytic signal obtained.  The candidate
would need a carrier-specific all-order diagonalization or clock together with
an inverse/extremal theorem.  `(I-zP_n)^{-1}` is a forbidden generic resolvent,
and the intercalate count alone neither reconstructs `L` nor controls future
degrees.

### Owner subtraction and decision

Wanless constructs graphs of Latin-square classes with edges given by cycle
switches and explicitly treats the intercalate-only variant.  Jacobson--Matthews
and later work also use Latin-square switching for random generation, while
modern primary papers study intercalate statistics.  Thus the carrier, trade,
switch graph, and static intercalate extremals receive zero credit.

The order-3/order-4 jump is crisp but not paper-sized after subtraction.

**Decision:** `KILL_DIRECT_OBJECT`.

## 3. PPT — boxed plane-partition cube toggles

### Literal system

A state is a plane partition in an `a x b x c` box, represented by an
`a x b` weakly decreasing height array with entries in `{0,...,c}`.  Choose a
cell and a sign `+/-` uniformly from the `2ab` fixed slots.  Add or remove one
cube at that cell if the resulting array is still a plane partition; otherwise
hold.

### Exact pilot and theorem ceiling

Complete state and transition censuses give

```text
box       states   largest coefficient of volume census
1x2x3       10                    2
2x2x2       20                    4
2x3x2       50                    8.
```

The counts agree exactly with MacMahon's product.  The fixed signed-site
scheduler is symmetric, its graph is connected, and uniform measure is
stationary.  Complementing every height by `c-x` after rotating the array gives
the checked volume symmetry `N_v=N_{abc-v}`.

Those are static enumeration and generic reversible-walk facts.  No closed
time transform, dynamic inverse, or new extremal clock was found.

### Owner subtraction and decision

Plane partitions in a box are lozenge tilings of a hexagon, and adding/removing
a legal cube is the single-flip Glauber dynamics.  Luby--Randall--Sinclair and
Laslier--Toninelli directly study local tiling Glauber dynamics, uniform
stationarity, and mixing/macroscopic evolution.  MacMahon enumeration is also
classical static input.

**Decision:** `KILL_DIRECT`.

## 4. SMB — random blocking-pair paths to stable matching

### Literal system

Fix two equally sized sets of agents with strict complete preferences and rank
remaining single below every partner.  A state is a partial one-to-one
matching.  A pair is blocking when both agents prefer one another to their
current partners.  At every nonstable state choose a blocking pair uniformly,
match them, and make their former partners single.  Stop at stability.

### Exact pilot and full recurrence

There are 34 partial matchings at size three.  The verifier constructs every
row for two explicit preference profiles, proves that every state has a route
to stability, and independently solves the rational absorption equations.  In
both profiles the empty matching reaches two stable endpoints with positive
probability.  The exact mean clocks are

```text
637/82,
36186760832205392/4520768244784785.
```

For stable `sigma`, the complete marked transform satisfies

```text
F_mu(z,sigma)=1{mu=sigma}                            if mu is stable,

F_mu(z,sigma)=z/|B(mu)| sum_{b in B(mu)} F_{mu.b}(z,sigma)
                                                       otherwise.    (SMB.1)
```

This is exact first-step decomposition, but on arbitrary preference profiles it
is only finite linear elimination.  The large denominators are evidence that a
small universal sufficient statistic did not appear.

### Direct owner and decision

Roth and Vande Vate study the same process: randomly chosen blocking pairs
match, the abandoned partners become single, convergence to a stable matching
occurs almost surely, and every stable matching is accessible with positive
probability from the empty state.  Therefore the update, convergence, and
endpoint-support theorem are direct-owner material.

No residual restricted preference family with a closed transform plus inverse
or sharp extremizer was found in this round.

**Decision:** `KILL_DIRECT`.

## 5. AIM — capped additive-increase/multiplicative-decrease

### Literal system

Fix cap `C>=2` and rational loss probability `0<p<1`.  The state is a window
`X_t in {1,...,C}`.  Independently each epoch,

```text
X_{t+1}=max(1,floor(X_t/2))   with probability p,
X_{t+1}=min(C,X_t+1)          with probability 1-p.
```

This is a global feedback step, not coordinate random scan.

### Exact pilot and analytic ceiling

For every `4<=C<=12` and `p in {1/3,2/5}`, the verifier constructs the exact
kernel, solves the stationary law over rationals, verifies every balance
equation, and matches six time layers against direct Bernoulli-word expansion.
For `C=12`, stationary means are

```text
p=1/3: 417013/110703,
p=2/5: 98006234/32966795.
```

For `1<j<C`, the stationary equations have the binary-preimage form

```text
pi_j=(1-p)pi_{j-1}+p(pi_{2j}+pi_{2j+1}),          (AIM.1)
```

with out-of-range terms omitted and separate cap/bottom boundaries.  A single
interior transition row recovers `p`, but this is merely reading the two branch
weights.  The finite stationary solve and (AIM.1) do not give the requested
all-time transform plus independent inverse/extremal axis.

### Owner subtraction and decision

Chiu--Jain establish the additive-increase/multiplicative-decrease congestion
control mechanism and its convergence/fairness role.  There is also an
extensive stochastic AIMD literature; a bounded primary search was not treated
as exhaustive.  The cap and Bernoulli-loss discretization are a specialization,
not a new mechanism.

**Decision:** `KILL_OWNER_THIN`.

## 6. RSP — Random-Edge on a Gray-ranked cube orientation

### Literal system

Label the vertices of the `d`-cube by binary reflected Gray words
`g(r)=r xor floor(r/2)`, `0<=r<2^d`.  Orient every cube edge from the endpoint
with larger inverse-Gray rank to the endpoint with smaller rank.  From a
nonsink vertex choose one outgoing edge uniformly; the rank-zero vertex
absorbs.

This inverse-Gray orientation is an acyclic unique-sink orientation.  To see
the non-generic part, scan the free coordinates of any face from most to least
significant.  At a free coordinate, its Gray bit can be chosen uniquely to
make the corresponding inverse-Gray rank bit zero.  Any other vertex has a
first free coordinate with inverse-rank bit one; toggling that coordinate
strictly lowers the rank.  Hence the recursively chosen vertex is the face's
unique local sink.  The verifier also checks every face through `d=7`.  This is
a specific full family, not an arbitrary transition matrix.

### Exact pilot and theorem ceiling

For every vertex through `d=7`, the verifier checks strict rank descent and
recursively computes the full absorption-time law.  From the top-ranked vertex:

```text
d=2: E T=2,       clock support size 2;
d=3: E T=37/12,   support size 4;
d=4: E T=1387/324, support size 8;
...
d=7: support size 64.
```

The recurrence

```text
F_v(z)=z/|O(v)| sum_{u in O(v)} F_u(z),   F_sink(z)=1
```

is ordinary first passage on an acyclic digraph and receives zero credit.  The
means do not exhibit a simple closed form, and no orientation inverse or sharp
family extremizer appeared.

### Owner subtraction and decision

Random-Edge is a classical randomized simplex pivot rule.  Gärtner--Henk--
Ziegler analyze randomized pivoting on Klee--Minty cube orientations, and the
AUSO literature directly treats Random-Edge path complexity.  The Gray ranking
is only a selected orientation inside that program.

**Decision:** `KILL_DIRECT_PROGRAM`.

## 7. R2O — random strict 2-opt descent

### Literal system

Fix labelled Euclidean points and an undirected Hamiltonian tour.  List all
2-opt segment reversals that strictly reduce squared Euclidean tour length.
Choose one improving tour uniformly and repeat; if none exists, stop.

### Exact pilot and theorem ceiling

The verifier enumerates all anchored undirected tours for two fixed integer
point sets:

```text
n=6: 60 tours, one local optimum;
n=7: 360 tours, one local optimum.
```

Every move strictly decreases an integer potential.  Complete endpoint and
clock laws are computed by dynamic programming in increasing length order.  A
maximum-length starting tour has one endpoint in both pilots and clock-support
sizes 11 and 22.

Strict potential descent proves termination, but the output is instance
specific.  There is no all-point-set transform, inverse geometry theorem, or
sharp temporal extremizer.  A generic recurrence over improving neighbours is
not a contribution.

### Owner subtraction and decision

Croes introduces the mechanizable 2-opt improvement method for the travelling
salesman problem.  Later primary work studies its approximation properties.
The uniform selection among current improvements is only a stochastic local
search scheduler.

**Decision:** `KILL_THIN`.

## 8. RDA — randomly scheduled deferred acceptance

### Literal system

Run proposer-side deferred acceptance with strict complete preference lists,
but at each step choose uniformly among currently free proposers who have an
untried receiver.  The selected proposer makes the next proposal on its list;
the receiver retains the preferred of its incumbent and the new proposer.

### Exact pilot and general negative theorem

Exact state DAGs were constructed for one size-3 and one size-4 profile.  They
contain 15 and 16 reachable states, respectively.  The final matchings and
proposal clocks are

```text
n=3: matching (2,1,0), clock 6;
n=4: matching (0,1,2,3), clock 4.
```

The lack of clock randomness is general.  Deferred acceptance produces the
same proposer-optimal matching under every legal proposal order.  Each proposer
proposes down its list without repetition until reaching its final partner.
Consequently

```text
T=sum_m (rank_m(final partner)+1),                 (RDA.1)
```

which is order independent.  Random scheduling changes only transient
interleavings.

### Owner subtraction and decision

Gale--Shapley owns deferred acceptance, stability, and the proposer-optimal
endpoint.  The random scheduler is a generic order wrapper, while (RDA.1) is a
routine invariant of the owned algorithm.  There is no stochastic clock or
endpoint axis to develop.

**Decision:** `KILL_DEGENERATE`.

## Theorem-value comparison

| system | all-parameter temporal object | inverse/extremal axis | fatal issue |
|---|---|---|---|
| DBM | only literal finite layers | none | direct model owner |
| LIT | affine kernel identity; generic resolvent only | intercalate degree is nonidentifying | direct switch-graph owner |
| PPT | generic reversible local-flip chain | static volume symmetry only | direct Glauber owner |
| SMB | generic marked first-step system | no profile inverse/extremizer | exact same-kernel owner |
| AIM | stationary binary-preimage recurrence | one-row `p` reading only | owner-heavy and second-axis thin |
| RSP | ordinary acyclic first-passage recurrence | none | direct Random-Edge/AUSO program |
| R2O | instance-specific potential DAG | none | one stochastic wrapper over 2-opt |
| RDA | deterministic proposal clock | endpoint/clock already owned | randomness degenerates |

No row clears both required columns.

## Exact evidence

The standalone verifier
[`verify_stochastic_replacement3.py`](verify_stochastic_replacement3.py)
uses only the Python standard library, integers, and `fractions.Fraction`.  It
imports no earlier scout.  A cold run is

```bash
python3 docs/papers152_156_sequence/scouting/stochastic_replacement3/verify_stochastic_replacement3.py
```

The frozen transcript is [`VERIFICATION.txt`](VERIFICATION.txt).  The run
executes **41,355 exact assertions**:

```text
DBM   1,239
LIT  22,022
PPT     998
SMB     335
AIM     810
RSP   5,310
R2O  10,466
RDA     175
```

These checks are falsifiers, not proofs of originality.  The formula-coherence
failure for LIT/SMB is recorded separately in
[`DERIVATION_PACKAGE.md`](DERIVATION_PACKAGE.md).

## Final gate

```text
SELECTED = NONE
STATUS = PASS_EMPTY_POOL
EXTERNAL = HOLD_EXTERNAL
```

The only defensible action is to leave the stochastic fifth seat empty.  A
future re-entry must bring a new literal mechanism with a non-generic temporal
formula and an independent inverse or sharp extremal theorem before owner
positioning begins.
