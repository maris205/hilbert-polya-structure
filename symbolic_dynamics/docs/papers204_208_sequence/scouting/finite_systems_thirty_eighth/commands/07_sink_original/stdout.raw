# Combinatorial / graph / order-dynamics scout for P107--P111

**Status:** scouting evidence only; external dissemination remains **HOLD**.  No
paper number is assigned by this document, and no statement below is an
absolute novelty claim.

**Evidence cutoff:** 2026-08-29.  The existing P1--P106 tree was treated as
read-only.  Exact programs created by this scout have the required
`combinatorial_` prefix and live only in `scouting/code/`.

## 1. Executive decision

There are two candidates worth advancing past scouting.

1. **GO, subject to a focused owner gate: cyclic partition shift--join.**
   On the partition lattice of `Z/nZ`, set
   \[
      J(\pi)=\pi\vee\rho\pi,
   \]
   where `rho` is one-step rotation.  The exact spike simultaneously found
   the iterate formula, divisor-indexed fixed set, finite zeta function,
   Möbius--Bell basin formula, sharp depth `n-2`, and the unexpectedly clean
   deepest-shell count `n phi(n)/2`.  The proof engines are partition-lattice
   propagation and subgroup/Möbius inversion, neither of which is the engine
   of P105 or P106.

2. **Conditional GO: cyclic nearest-neighbour gcd erosion.**  On cyclic words
   of divisors of `M`, set
   \[
      G(x)_i=\gcd(x_i,x_{i+1}).
   \]
   Prime valuations turn the system into independent one-sided minimum
   eroders.  This gives an exact window iterate, a longest-run pointwise depth
   law, a product basin formula, sharp depth `n-1`, and a prime-blind
   conjugacy signal.  It is theorem-dense, but its owner subtraction must be
   unusually explicit because monotone eroders and mathematical morphology
   are mature and P100 already uses valuations.

3. **RESERVE / owner-heavy negative control: degree-parity cut switching.**
   Its odd/even order dichotomy is exact and attractive, but the odd-order
   projection is precisely the classical Seidel switch by the odd-degree set.
   The even-order involution is a possible residual observation, not yet a
   paper-sized owner-subtracted contribution.

The other seven rules below are useful firewall entries.  Four are directly
owned classical constructions, two are theorem-thin, and one needs an
unpromising fill-in owner audit.  They should not occupy P107--P111 slots.

## 2. P1--P106 collision audit

The audit used the current collision firewalls, candidate/kill ledgers, and
the paper directory inventory through P106.  In particular, the search was
kept outside these occupied or explicitly excluded mechanisms:

- ordinary SFT/sofic/hom-shift variants, graph powers, full-map functional
  graphs, necklace decimation, ordinary rule-90/rule-184 reparametrizations,
  and already used torsion-window systems;
- rowmotion, promotion/0-Hecke and pop-stack actions, source candidates that
  merely rename Kreweras complement, and ordinary stack or push--pop
  encodings;
- P95 minimal-slack no-repeat, P96 window/finitary subset-circle mechanisms,
  P97 sumset squaring, P100 valuation digit erasure, and P101 clipped random
  synchronization;
- P105 cycle-minimum pruning and its cycle-deletion/standardization neighbours;
  and
- P106 synchronous MIS polarity and nearby Galois-polarity/maximal-independent
  closure maps.

Three tempting ideas were rejected before entering the candidate table:

- pairwise-union squaring of a set family is too close to P97's
  closure-by-binary-product engine;
- repeated leaf, core, or dominated-vertex stripping is too close in proof
  shape to the pruning lane and has a large direct literature; and
- blocker/Alexander-dual dynamics on clutters is both a standard involution
  and too close to the polarity language of P106.

The two GO candidates survive this firewall for different reasons.  The
partition rule coarsens an equivalence relation on a fixed cyclic ground set
by joining translates; it does not delete cycle entries.  The gcd rule is a
local meet on a product of divisor lattices; it neither erases the least
valuation digit as P100 does nor evolves a set by pairwise algebraic sum as
P97 does.

## 3. Candidate ledger

| ID | System and update-rule class | Earliest exact signal | Owner / collision risk | Decision |
|---|---|---|---|---|
| C1 | cyclic partition shift--join; automorphism plus lattice join | Möbius--Bell basins, depth `n-2`, deepest shell `n phi(n)/2` | medium owner risk; low P105/P106 collision | **GO owner-gated** |
| C2 | cyclic divisor-word gcd erosion; local meet CA | window gcd, product basins, threshold-run depth, prime-blind conjugacy | medium-high owner risk; medium P100/CA collision | **GO conditional** |
| C3 | degree-parity cut switching; adaptive graph switch | odd `n` projection versus even `n` involution | direct Seidel owner on odd branch | **RESERVE / do not freeze** |
| C4 | crossing-component coarsening of set partitions; closure | fixed Catalan states and no depth beyond one | exact noncrossing-closure owner | **KILL_DIRECT** |
| C5 | ordered parallel chordal fill; monotone edge addition | fill dependencies propagate by Boolean derivation height | standard elimination/fill literature | **KILL_OWNER_RISK** |
| C6 | parallel source-to-sink reversal; orientation toggle | click invariants and Coxeter/circulation structure | exact source-to-sink literature | **KILL_DIRECT** |
| C7 | lower-shadow descent of uniform hypergraphs; rank lowering | all iterates are higher shadows; colex extremizers persist | Kruskal--Katona directly owns core | **KILL_DIRECT** |
| C8 | clocked odd--even comparator dynamics on permutations | unique sorted 2-cycle; reverse order needs `n` phases | classical parallel sorting | **KILL_DIRECT** |
| C9 | synchronous run halving on bounded words; local contraction | independent ceiling-halving of run lengths and binomial basins | low direct-map hit, but theorem-thin | **RESERVE_THIN** |
| C10 | iterated line graph; edge-to-vertex graph operator | four-way path/cycle/claw/prolific dichotomy | exact classical iteration owner | **KILL_DIRECT** |

## 4. C1 -- cyclic partition shift--join

### Exact system

Let `Pi_n` be the set of set partitions of the cyclic group
`C_n = Z/nZ`, ordered by refinement.  Let `rho(i)=i+1`, acting on
partitions by relabelling, and define
\[
        J_n(\pi)=\pi\vee\rho\pi .
\]
The join is the least common coarsening, equivalently the transitive closure
of the union of the two equivalence relations.  This is a self-map of the
Bell-sized finite phase space `Pi_n`.

### Earliest closed signals

The semilattice identity and the fact that `rho` is a lattice automorphism
give, without simulation,
\[
        J_n^t(\pi)=\bigvee_{j=0}^{t}\rho^j\pi .                 \tag{C1.1}
\]
If `H(pi)` is the subgroup generated by all differences `x-y` with `x,y`
in a common block of `pi`, then the eventual state is exactly the partition
of `C_n` into cosets of `H(pi)`.  Consequently:

- every recurrent point is fixed;
- fixed partitions are the coset partitions of the unique subgroup of each
  order `h|n`, hence there are `tau(n)` of them; and
- the finite dynamical zeta function is
  \[
       \zeta_{J_n}(z)=(1-z)^{-\tau(n)}.                       \tag{C1.2}
  \]

The basin enumeration is already closed.  Let `B_d` be the `d`-th Bell
number and let `N_n(h)` count initial partitions whose stable subgroup has
order exactly `h`.  Partitions refining the coset partition of a subgroup of
order `h` can be chosen independently on its `n/h` cosets, so there are
`B_h^(n/h)`.  Divisor-lattice inversion gives
\[
 N_n(h)=\sum_{d\mid h}\mu(h/d) B_d^{,n/d},\qquad h\mid n.    \tag{C1.3}
\]

The exact global absorption depth is
\[
              D_n=\max(0,n-2).                               \tag{C1.4}
\]
For `n>=3`, the deepest shell seen in every exhaustive lane is
\[
       \#\{\pi:\tau(\pi)=n-2\}=\frac{n\varphi(n)}2.           \tag{C1.5}
\]
Its predicted members are precisely the atoms having one two-element block
`{a,a+d}` with `gcd(d,n)=1`, all other blocks being singletons.  The count is
then the number of unoriented primitive chords of the labelled `n`-cycle.
Equation (C1.5) is the highest-value proof spike: it is exact through `n=9`,
but should be treated as a theorem obligation, not inferred from data alone.

Representative exact rows are:

| `n` | `B_n` | fixed | depth histogram | basin sizes by subgroup order | deepest |
|---:|---:|---:|---|---|---:|
| 4 | 15 | 3 | `{0:3,1:8,2:4}` | `{1:1,2:3,4:11}` | 4 |
| 6 | 203 | 4 | `{0:4,1:115,2:66,3:12,4:6}` | `{1:1,2:7,3:24,6:171}` | 6 |
| 8 | 4140 | 4 | `{0:4,1:2224,2:1440,3:368,4:64,5:24,6:16}` | `{1:1,2:15,4:209,8:3915}` | 16 |
| 9 | 21147 | 3 | `{0:3,1:11439,2:7482,3:1710,4:360,5:99,6:27,7:27}` | `{1:1,3:124,9:21022}` | 27 |

### Proposed short-paper theorem contract

1. Prove the exact iterate (C1.1) and identify the endpoint as the coset
   partition of `H(pi)`.
2. Classify all recurrent/fixed states and prove (C1.2).
3. Prove the exact basin formula (C1.3), including `h=1`, `h=n`, prime `n`,
   and `n=1,2` endpoints.
4. Prove the sharp depth (C1.4).
5. Prove the primitive-chord classification and deepest-shell formula
   (C1.5).  A safe route is to inspect the two omitted translates at time
   `n-3`: one primitive chord leaves two components, while a nonprimitive
   chord distributes the missing edges among distinct subgroup cycles; any
   second independent initial relation must bridge the remaining cut.
6. State recovery carefully: for `n>=3`, the sharp depth recovers `n`; the
   small endpoints must be separated by phase size.  Do not claim that the
   fixed count `tau(n)` alone recovers `n`.

### Two independent proof/control routes

**Route A -- translated equivalence graphs.**  Replace every block by a
connected graph, translate those edges through consecutive positions, and
use connectivity.  The full orbit of a difference `d` is a union of
`gcd(d,n)` cycles.  Removing one translate leaves every such cycle connected,
which proves the `n-2` upper bound; the two-missing-edge analysis attacks the
deepest shell.

**Route B -- subgroup and incidence inversion.**  Translation-invariant
equivalence relations for the regular cyclic action are subgroup coset
partitions.  Refinement below a coset partition factors into independent Bell
choices, after which ordinary divisor Möbius inversion proves the basin
formula.  This route does not use the time-step connectivity proof.

**Independent exact control.**  Restricted-growth strings enumerate every
partition, union--find computes joins, a separately constructed orbit join
checks (C1.1), and a literal functional orbit is compared against the subgroup
endpoint and Möbius formula.  Every state is also checked against the
primitive-chord deepest-shell classification, not merely against its total
count.  The stored script makes 164,113 assertions over all partitions through
`n=9`.

### Direct-owner and collision gate

Four searches aimed at the exact phrases “partition lattice join cyclic
shift”, “join rotates set partition”, “shift-invariant closure equivalence
relation”, and “iterating partition join automorphism” found no exact update
or the Möbius--Bell/deepest-shell package.  The closest owners are
[Britnell--Wildon, *Orbit coherence in permutation groups*](https://arxiv.org/abs/1205.4960),
which studies joins among orbit partitions, and
[*Permutation groups, partition lattices and block structures*](https://arxiv.org/abs/2409.10461),
which studies invariant partitions as a sublattice.  Both are mandatory
background; neither search result states the self-map `pi -> pi join rho pi`
or its transient/basin formulas.  Search absence is only a bounded owner
check, so the status remains **GO owner-gated**, not “novel”.

Internal collision is low.  P105 deletes a distinguished element from every
permutation cycle and standardizes a smaller permutation.  C1 preserves the
ground set, monotonically coarsens an equivalence relation, and its main
enumerator is Bell/Möbius rather than cycle fibres.

### Fast KILL test

Kill or merge the candidate if any of the following occurs:

- a direct source contains this exact self-map and either (C1.3) or (C1.5);
- the primitive-chord classification fails at the first independently coded
  lane beyond `n=9`; or
- the purported second proof collapses to a restatement of the union--find
  iteration rather than a genuine subgroup/Möbius argument.

## 5. C2 -- cyclic nearest-neighbour gcd erosion

### Exact system

Fix positive integers `M,n`, let `D(M)` be the divisor lattice of `M`, and
take the cyclic phase space `D(M)^n`.  Define
\[
        G_{M,n}(x)_i=\gcd(x_i,x_{i+1}),\qquad i\pmod n.        \tag{C2.1}
\]
This is a local meet update on a generally non-chain alphabet.

### Earliest closed signals

Associativity and idempotence of gcd give the exact light cone
\[
       G_{M,n}^t(x)_i=\gcd(x_i,x_{i+1},\ldots,x_{i+t}).        \tag{C2.2}
\]
Thus every orbit reaches the constant word with value `d=gcd_i x_i`.
Constants are all the recurrent points, so
\[
       \#\operatorname{Fix}G_{M,n}=\tau(M),\qquad
       \zeta_{G_{M,n}}(z)=(1-z)^{-\tau(M)}.                  \tag{C2.3}
\]

The basin of the constant `d|M` factors prime by prime:
\[
 \#\mathcal B_d
   =\prod_{p^a\parallel M/d}\big((a+1)^n-a^n\big)
   =\sum_{e\mid M/d}\mu(e)\tau(M/(de))^n.                  \tag{C2.4}
\]
The first form says that, for every prime exponent, at least one coordinate
attains zero after division by `d`; the second is ordinary gcd Möbius
inversion.

There is also a pointwise depth formula.  For every prime `p|M` and threshold
`r>min_i v_p(x_i)`, form the cyclic binary word
\[
       b_i(p,r)=1_{\{v_p(x_i)\ge r\}}.
\]
If `L(p,r)` is its longest cyclic run of ones, then
\[
       \tau(x)=\max_{p,r}L(p,r).                              \tag{C2.5}
\]
In particular the exact worst depth is `n-1` for `M>1,n>1`, with the
degenerate cases having depth zero.

The early anomaly is **prime blindness**.  The depth histograms for
`(M,n)=(12,5)` and `(18,5)` are identical,
`{0:6,1:510,2:1970,3:1780,4:3510}`, and their basin lists differ only by
relabelling the primes.  More generally, permuting the prime-exponent factors
of `M` gives an explicit conjugacy of the meet alphabets and hence of the
entire cyclic-word dynamics.  This is structural, not a numerical accident.

Other exact lanes include:

| `(M,n)` | phase size | fixed | max depth | selected basin data |
|---|---:|---:|---:|---|
| `(4,5)` | 243 | 3 | 4 | `{1:211,2:31,4:1}` |
| `(6,6)` | 4096 | 4 | 5 | `{1:3969,2:63,3:63,6:1}` |
| `(12,5)` | 7776 | 6 | 4 | `{1:6541,2:961,3:211,4:31,6:31,12:1}` |
| `(36,4)` | 6561 | 9 | 3 | `{1:4225,2:975,3:975,4:65,6:225,9:65,12:15,18:15,36:1}` |
| `(30,6)` | 262144 | 8 | 5 | basin at `1` is 250047; each one-prime quotient has 3969 |

### Proposed short-paper theorem contract

1. Prove (C2.2), endpoint classification, recurrent/fixed classification,
   and zeta (C2.3), with `M=1`, `n=1`, and constant-word endpoints explicit.
2. Prove both equal forms in the basin formula (C2.4).
3. Prove the threshold-run pointwise depth formula (C2.5) and sharp depth,
   rather than reporting only an upper bound.
4. Prove the prime-exponent permutation conjugacy.  A converse classification
   should be claimed only if the functional graph is shown to recover the
   exponent multiset; the current evidence proves the forward conjugacy, not
   that converse.
5. Include an owner-subtraction theorem stating exactly what remains after
   generic monotone-eroder and morphological-erosion facts are removed: the
   divisor-lattice arithmetic basin factorization and the prime-blind finite
   functional-graph package.

### Two independent proof/control routes

**Route A -- valuation thresholds.**  Under `v_p`, gcd becomes minimum.
Thresholding a minimum produces Boolean AND, whose `t`-th iterate is an AND
over a length-`t+1` window.  Longest cyclic runs then prove the exact depth.

**Route B -- arithmetic incidence.**  Count divisor tuples with specified gcd
by Möbius inversion, or independently factor the minimum-zero condition over
prime-exponent coordinates.  This proves (C2.4) without using the run proof.

**Independent exact control.**  The script enumerates literal divisor tuples,
iterates literal gcds, compares them with a separately evaluated window gcd,
checks descent in the divisor order, computes threshold-run depth, and compares
literal basins with the product formula.  Seven lanes make 4,661,822
assertions.

### Direct-owner and collision gate

Eight targeted searches for “gcd cellular automaton”, neighbouring gcd,
one-sided min CA, cyclic erosion, and divisor-lattice local meet found no
source stating (C2.1)--(C2.5) as this finite arithmetic functional graph.
However, [Gács--Törmä, *Stable Multi-Level Monotonic Eroders*](https://link.springer.com/article/10.1007/s00224-021-10061-w)
shows that monotone multi-level eroders are an established subject, and
ordinary flat erosion is standard mathematical morphology.  Therefore a
paper may not present the threshold erosion itself as the contribution.

Internal collision is medium.  P100 also decomposes an arithmetic map by
prime valuation, and P90/P57 occupy cellular-automaton language.  C2 survives
only if the object/action/result boundary stays explicit: fixed cyclic words
over a divisor lattice, local gcd, basin factorization by the attractor, and
longest threshold runs.  Status: **conditional GO**.

### Fast KILL test

Kill C2 if a direct owner contains the exact cyclic gcd map plus basin or
depth formulas, or if owner subtraction leaves only the generic sentence
“minimum erodes runs”.  Also kill it for this round if the final manuscript
cannot state a contribution materially distinct from P100's valuation-layer
proof engine.

## 6. C3 -- degree-parity cut switching

### Exact system and anomaly

For a labelled simple graph `G` on `[n]`, let `O(G)` be its odd-degree vertex
set and let `delta(S)` be the complete cut between `S` and its complement.
Define
\[
            \Phi_n(G)=G\triangle\delta(O(G)).                 \tag{C3.1}
\]
Over `F_2`, the degree boundary of `delta(S)` is `n 1_S` when `|S|` is even.
The handshaking lemma makes `|O(G)|` even, producing a clean parity bifurcation:

- if `n` is odd, `Phi_n` is an idempotent projection onto the Eulerian
  graphs;
- if `n` is even, the odd-degree set is preserved and `Phi_n^2=id`;
  fixed graphs are exactly those whose degree parities are all zero or all
  one.

Writing `m=binom(n,2)`, the fixed count is
\[
 F_n=\begin{cases}
  2^{m-n+1},&n\text{ odd},\\
  2^{m-n+2},&n\text{ even},
 \end{cases}
\]
and
\[
 \zeta_{\Phi_n}(z)=
 \begin{cases}
   (1-z)^{-F_n},&n\text{ odd},\\
   (1-z)^{-F_n}(1-z^2)^{-(2^m-F_n)/2},&n\text{ even}.
 \end{cases}                                                   \tag{C3.2}
\]
For odd `n`, every Eulerian target has `2^(n-1)` preimages.

Exact enumeration through `n=7` made 6,393,093 assertions.  At `n=6` it
found 2,048 fixed graphs and 15,360 two-cycles among 32,768 labelled graphs;
at `n=7` it found 32,768 fixed Eulerian graphs among 2,097,152 graphs.

### Potential contract and routes

The maximal possible contract is the parity dichotomy, fixed/periodic census,
zeta (C3.2), odd-order uniform fibres, and a careful even-order switching-class
decomposition.  Route A is boundary/coboundary linear algebra over `F_2`.
Route B is literal edge-mask enumeration with an independent degree-fibre
counter.

### Direct owner and verdict

The owner gate fires on the core odd-order result.  Seidel's switching theorem
says that every odd-order switching class contains a unique even graph, and
the constructive proof switches precisely by the odd-degree set.  See
[Mallows--Sloane, *Two-Graphs, Switching Classes and Euler Graphs Are Equal in Number*](https://doi.org/10.1137/0128070)
and the later switching literature.  Thus the odd-order projection and its
uniform-fibre interpretation must be treated as classical.  The even-order
involution is a neat residual calculation but not yet sufficient for a full
paper.  **RESERVE_OWNER_HEAVY**; do not freeze it into P107--P111.

Fast kill: if a focused Seidel search also states the even-order parity
involution or its cycle census, mark the whole candidate `KILL_DIRECT`.

## 7. C4 -- crossing-component noncrossing closure

### System and early signal

Given a set partition drawn on a cyclically ordered ground set, form the graph
whose vertices are its blocks and whose edges join crossing blocks.  Merge all
blocks in each connected component.  The result is already noncrossing.

A temporary exhaustive lane through `n=8` found no genuine transient depth:
every state is either fixed or enters the fixed set in one step.  At `n=8`,
1,430 of the 4,140 partitions are fixed and the other 2,710 have depth one;
the fixed count is the Catalan number, as expected.

### Contract, routes, and owner gate

An unowned contract would contain idempotence, Catalan fixed count, zeta, and
fibres over noncrossing partitions.  Route A is the crossing-component lemma;
Route B is restricted-growth-string enumeration plus a crossing-graph
component computation.

This exact construction is already the classical **noncrossing closure**:
Kreweras defines it by merging connected components of the crossing graph and
proves its universal property; see the translated
[*On the Noncrossing Partitions of a Cycle*](https://www.math.utah.edu/~earnshaw/research/kreweras.pdf).
The one-step data therefore confirm the owner rather than open a paper.
**KILL_DIRECT**.

## 8. C5 -- ordered parallel chordal fill

### System and early signal

Fix a vertex order `sigma`.  In one parallel step, for every vertex `v`, add
all missing edges among the later neighbours of `v`, using the graph at the
start of the step.  Repeat.  The edge set is monotone, and the endpoint is the
least supergraph for which `sigma` is a perfect elimination order.

The first nontrivial signal is that an edge can appear because of an edge
created at an earlier round, so the transient is the height of a Boolean
fill-derivation tree rather than merely one-step clique completion.  A cycle
with the natural order triangulates immediately, whereas nested fill
dependencies can force several rounds.

### Possible contract and two routes

A viable contract would need an exact first-appearance-time formula for every
fill edge, a sharp maximum derivation height, a fixed-graph census for a fixed
order, and endpoint recovery.  Route A writes the update as a monotone Boolean
recurrence for adjacency and interprets time as derivation height.  Route B
compares a literal parallel iterator with a standard sequential elimination
fill and enumerates all labelled graphs for small `n`.

The construction sits directly inside sparse elimination, fill-in, and
chordal-completion theory; even parallel elimination orders are an established
topic (for example, [Bornstein--Maggs--Miller--Ravi](https://scholars.duke.edu/publication/785994)).
No simple fixed-order census or sharp depth appeared in the first gate, and
the owner burden is high.  **KILL_OWNER_RISK** for this round.

Fast kill: a source identifying parallel fill rounds with elimination-tree
height, or failure to find a closed maximum-depth family by `n<=8`, closes the
candidate.

## 9. C6 -- parallel source-to-sink reversal

### System and early signal

On the acyclic orientations of a fixed graph, simultaneously reverse every
edge incident from a current source.  Sources form an independent set, so the
parallel step is a commuting product of ordinary source-to-sink conversions.
Cycle circulations are invariant, and on a tree the operation remains in the
single click-equivalence class.

### Possible contract and two routes

The hoped-for contract would classify periodic orbits by circulation, give
exact periods on paths/cycles/trees, and express the zeta function in terms of
click classes.  Route A uses Coxeter elements and commuting source clicks.
Route B enumerates acyclic orientations and checks circulation vectors and
functional graphs independently.

The update is directly in the mature “click” literature.
[Macauley--Mortveit, *Posets from Admissible Coxeter Sequences*](https://arxiv.org/abs/0910.4376)
studies the equivalence relation generated by source-to-sink conversions and
its Coxeter/asynchronous-dynamics interpretations.  Parallelizing commuting
sources does not create enough owner distance.  **KILL_DIRECT**.

Fast kill: already fired--the update decomposes into commuting standard
clicks and the proposed invariants are the direct owners' invariants.

## 10. C7 -- lower-shadow descent of uniform hypergraphs

### System and early signal

For a family `F subset binom([n],k)`, define its lower shadow
\[
    \partial F=\{A\in\tbinom{[n]}{k-1}:A\subset B
                  \text{ for some }B\in F\}.
\]
Use the disjoint union of ranks `0,...,n` plus a cemetery convention as the
phase space.  The exact iterate is the `t`-fold shadow, and colex initial
segments remain extremal at every rank.  Absorption time is rank-controlled,
not chaotic.

### Contract, routes, and owner gate

The maximal contract would package all iterated shadow sizes, sharp extremal
profiles, endpoint cases, and perhaps preimage fibres.  Route A is compression
and binomial representation; Route B is literal subset-family enumeration and
shadow formation.

The core is the Kruskal--Katona theorem and its iterated form.  A modern owner
with explicit lower-shadow and extremal-family scope is
[Serra--Vena, *Extremal families for the Kruskal--Katona theorem*](https://arxiv.org/abs/2304.05145).
Recasting rank descent as time does not leave an adequate residual theorem.
**KILL_DIRECT**.

Fast kill: already fired--colex extremality for every iterate is standard, and
no independent fibre law emerged.

## 11. C8 -- clocked odd--even comparator dynamics

### System and early signal

On `S_n x Z/2Z`, compare-exchange the disjoint adjacent pairs of the parity
specified by the clock, then flip the clock.  Every actual swap decreases the
inversion count.  Hence every orbit reaches the two clock copies of the sorted
permutation, which form the unique recurrent 2-cycle.  The reverse
permutation attains the standard worst case of `n` parallel phases.

### Contract and two routes

The possible finite-dynamics package would give the unique recurrent orbit,
zeta `(1-z^2)^(-1)`, a particle/displacement expression for pointwise depth,
the sharp `n` bound, and transient-layer counts.  Route A is the zero--one
principle plus particle trajectories; Route B is literal permutation/clock
functional-graph enumeration.

Odd--even transposition sorting is classical and is explicitly described as
an `n`-phase parallel sort in the standard literature; see, for example,
[*Odd-even, compare-exchange parallel sorting*](https://doi.org/10.1016/0165-6074(94)90012-4).
The clocked zeta reformulation is not enough owner-subtracted content.
**KILL_DIRECT**.

Fast kill: already fired--the complete transient mechanism is the sorting
algorithm itself.

## 12. C9 -- synchronous run halving on bounded words

### System and early signal

Let the finite phase contain all binary words of length at most `n`, including
the empty word.  Write a nonempty word in maximal-run coordinates
`(epsilon;r_1,...,r_k)`, where adjacent run symbols alternate.  Define
\[
 T(\epsilon;r_1,\ldots,r_k)
   =(\epsilon;\lceil r_1/2\rceil,\ldots,\lceil r_k/2\rceil).
                                                                    \tag{C9.1}
\]
No runs merge, and therefore
\[
 T^t(\epsilon;r_1,\ldots,r_k)
   =(\epsilon;\lceil r_1/2^t\rceil,\ldots,
                    \lceil r_k/2^t\rceil).                         \tag{C9.2}
\]
The pointwise depth is `ceil(log_2 max_i r_i)`.  Fixed states are the empty
word and the two alternating words of every positive length, so there are
`1+2n` recurrent/fixed states and zeta `(1-z)^(-(1+2n))`.

For either fixed alternating word with `k` runs, its full basin within the
bounded phase has size
\[
       \sum_{N=k}^{n}\binom{N-1}{k-1}=\binom nk.                \tag{C9.3}
\]
The basin identity
`1+2 sum_{k=1}^n binom(n,k)=2^(n+1)-1` recovers the whole phase.  Cumulative
depth shells reduce to bounded-composition coefficients with each part at
most `2^t`.

### Routes, risk, and verdict

Route A is the run-coordinate conjugacy and ceiling identity.  Route B is
composition generating functions plus literal word enumeration.  Targeted
search did not locate this exact bounded functional graph, but the proof is
essentially run-length encoding followed by independent scalar halving.  The
theorem is clean yet too elementary, and it has a generic erasure/pruning
motif.  **RESERVE_THIN**, not a P107--P111 freeze.

Fast kill: unless a cyclic or larger-alphabet extension creates a new
factorization, parity effect, or recovery theorem without breaking the run
conjugacy, stop here.

## 13. C10 -- iterated line graph

### System and signal

Map a finite simple graph `G` to its line graph `L(G)`, whose vertices are
edges of `G` and whose adjacencies record incident edge pairs.  This is a
genuinely different graph operator, but its dynamical classification is
already known: connected paths shrink to the empty graph, cycles are fixed up
to isomorphism, the claw enters the triangle, and all other connected graphs
are prolific with eventually unbounded order.

### Contract, routes, and owner gate

A putative contract would simply restate this four-way classification and
then track graph parameters.  Route A uses degree/order recurrences and
Whitney-style line-graph structure; Route B constructs iterated line graphs
literally and canonicalizes isomorphism types.

The direct owner is van Rooij--Wilf's 1965 iteration theorem, and current work
continues to study parameter growth; see
[Caro--Lauri--Zarb, *Index of Parameters of Iterated Line Graphs*](https://arxiv.org/abs/2105.02496)
and the original DOI `10.1007/BF01904834`.  **KILL_DIRECT**.

Fast kill: already fired--even the global orbit dichotomy is directly owned.

## 14. Exact-spike reproducibility

The three strongest structural signals were checked by independent literal
enumeration.  Run from the repository root:

```bash
python3 docs/papers107_111_sequence/scouting/code/combinatorial_partition_shift_join.py
python3 docs/papers107_111_sequence/scouting/code/combinatorial_cyclic_gcd_erosion.py
python3 docs/papers107_111_sequence/scouting/code/combinatorial_degree_parity_cut.py
```

Current stored-code outcomes:

| spike | lanes | assertions | verdict |
|---|---|---:|---|
| partition shift--join | every partition for `1<=n<=9` | 164,113 | PASS |
| cyclic gcd erosion | `(1,5),(4,5),(6,6),(12,5),(18,5),(36,4),(30,6)` | 4,661,822 | PASS |
| degree-parity cut switch | every labelled graph for `1<=n<=7` | 6,393,093 | PASS |
| **total** |  | **11,219,028** | **PASS** |

The controls are deliberately not proof clones:

- the partition program compares literal one-step joins with a separately
  accumulated orbit join, then compares the endpoint with an independently
  built coset partition and the basins with a numerical Möbius--Bell formula;
- the gcd program compares literal orbits with both a direct window gcd and a
  valuation-threshold run computation, then checks a separately evaluated
  prime-product basin formula; and
- the graph program compares edge-mask iteration with independent `F_2`
  degree-parity fibres, idempotence/involution identities, and closed cycle
  counts.

## 15. Final ranking and freeze advice

### Rank 1 -- cyclic partition shift--join: GO

This has the best combination of theorem density, early anomaly, proof-route
separation, and internal collision safety.  Freeze it only after one more
targeted owner pass using the exact formula strings and after a proof of the
deepest-shell classification.  If those pass, it is the natural first
combinatorial slot in P107--P111.

### Rank 2 -- cyclic gcd erosion: conditional GO

The exact dynamics are as strong as C1, and the product basin formula plus
prime-blind conjugacy are useful arithmetic structure.  Its weakness is not
the theorem but owner subtraction: the manuscript must foreground what is
specific to divisor lattices and finite cyclic functional graphs, and must
firewall P100 explicitly.  Freeze only if that subtraction remains a full
theorem rather than a change of vocabulary.

### Rank 3 -- degree-parity cut switching: RESERVE, not a freeze

Keep the exact spike because it is an excellent parity benchmark and the
even-order involution may inspire a different graph rule.  Do not allocate a
paper to (C3.1) itself unless a second owner pass establishes a genuinely
unowned even-order theorem family beyond the immediate cycle census.

### Slot discipline

This scout recommends freezing **at most two** systems from its branch.  It is
better to leave the remaining P107--P111 positions to stronger candidates
from other branches than to promote C4--C10 after their kill gates have fired.
All external-facing status remains **HOLD**.
