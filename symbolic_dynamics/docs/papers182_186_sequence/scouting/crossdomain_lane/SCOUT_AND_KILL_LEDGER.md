# Cross-domain scout and kill ledger

The list below contains sixteen literal finite systems.  Distinctness is by
carrier plus local operation and proof mechanism, not by a parameter change.
`KEEP` means only “worth the next internal stage”; it never means novel.

## 1. Random incoming-copy symmetrization (RICS) — KEEP-1

**Carrier and rule.**  A state is a loopless labelled directed graph with
adjacency bits `A_ij` for `i != j`.  Choose `v` uniformly from `[n]` and set

`A'_{vu}=A_{uv}` for every `u != v`, leaving every other arc unchanged.

**Small-case signal.**  Exhaustion through `n=4` shows recurrent counts
`1,2,8,64`; maximum distinct one-step fibre sizes `1,3,10,29`; and, from the
completely conflicting representative at time `n`, absorption-word counts
`1,4,24,168`.  The endpoint-support counts are `1,2,9,40`.  The exact verifier
proves the structural identities behind all of these numbers on the tested
range.

**Theorem axes.**  Conflict-graph deletion; independent-set absorption
polynomial; first-occurrence-order endpoint kernel; exact labelled and distinct
one-step fibres; recurrent classification; graph-polynomial consequences.

**Verdict.**  KEEP.  The local maps do not commute and endpoints retain first
occurrence order, separating the mechanism from P179's support-only commuting
idempotents.

## 2. Co-gcd translation (CGT) — KEEP-2

**Carrier and rule.**  On `Z/p^a Z`, with representatives `0 <= x < p^a`, set

`T(x) = x + p^a/gcd(x,p^a) (mod p^a)`, including `gcd(0,p^a)=p^a`.

**Small-case signal.**  Across 25 prime-power carriers up to `5^5=3125` and
`7^4=2401`, every fibre has size `0,1`, or `2`, with equal numbers of empty and
double fibres.  For `p=3,a=4`, the 81 states split into fibre counts
`3/75/3`; 72 are recurrent and exactly 3 states occur at each positive tail
depth `1,2,3`.  The full tested census is in `CANONICAL.txt`.

**Theorem axes.**  Complete valuation-stratum functional graph; odd/even
exponent tail laws; middle-valuation conveyor for even `a`; exact cycle census;
explicit double-fibre atlas; image defect `p^floor((a-1)/2)`.

**Verdict.**  KEEP, conditional on stronger external ownership search.  The
literal nonlinear translation and the middle-stratum conveyor differ from
P142's divisor-valued valuation map and P166's Hamming-weight phase shift.

## 3. Random suffix-set compression (SSC) — KILL after pilot

**Carrier and rule.**  A state is a nonempty subset `A` of binary words of
length `d`.  Choose `b` uniformly from `{0,1}` and map the whole set by
`x_1...x_d -> x_2...x_d b`, merging duplicates.

**Small-case signal.**  Exact depth-shell counts for `d=1,2,3,4` are
`(2,1)`, `(4,2,9)`, `(8,4,18,225)`, and
`(16,8,36,450,65025)`.  At `d=4` the one-step image has 510 states and the
largest one-step fibre is 6561.  Time-`t` images and fibres were checked
exhaustively through `d=3,t=d+2`.

**Theorem axes.**  Closed image formula; common-suffix exact tail; shell CDF;
time-`t` fibres; de Bruijn recurrent chain.

**Verdict.**  KILL as a paper candidate.  This is visibly the power-set action
of the binary shift-register automaton; synchronization is immediate after any
`d` letters.  It is owner-obvious and lies directly under the P55 probabilistic
finite-automata theme.  Retain only as a reusable exact-control example.

## 4. Odd-degree clique projection (OCP) — KILL

**Carrier and rule.**  For a labelled simple graph `G`, let `O(G)` be its
odd-degree vertices and set `T(G)=G triangle K_{O(G)}`.

**Small-case signal.**  The handshaking lemma makes `|O(G)|` even, so toggling
the clique reverses precisely the degree parities in `O(G)`.  Every graph lands
in the Eulerian subspace in one step; each Eulerian target has `2^(n-1)`
preimages indexed by even vertex sets.

**Theorem axes.**  Image, fibres, rank over `F_2`, and quotient projection.

**Verdict.**  KILL.  One-step parity projection is a proof transfer from the
parity/graph-linear cluster around P127/P145/P159, with no dynamical runway.

## 5. Random local complementation (RLC) — KILL

**Carrier and rule.**  On simple graphs, choose `v` uniformly and complement
the subgraph induced by the current open neighbourhood `N(v)`; all incident
edges at `v` remain fixed.

**Small-case signal.**  Each local move is an involution, so the chain is a
random walk on a local-complementation orbit and its transition matrix is
symmetric.

**Theorem axes.**  Orbit classification, stabilizers, periods, mixing.

**Verdict.**  KILL.  Local complementation and its graph-state orbits have an
obvious mature owner literature; rediscovering the orbit walk is not a Route-A
system contribution.

## 6. Random wedge-to-triangle closure (WTC) — KILL

**Carrier and rule.**  In a simple graph, choose uniformly an ordered open
wedge `(u,v,w)` with `uv,vw` edges and `uw` absent, and add `uw`; if none exists,
self-loop.

**Small-case signal.**  Edge count increases at every active move.  The
absorbing graphs are disjoint unions of cliques, and the endpoint is simply the
clique completion of every initial connected component, independent of order.

**Theorem axes.**  Absorption time and coupon bounds for missing intra-component
edges.

**Verdict.**  KILL.  The endpoint is ordinary transitive/cluster closure and
the remaining probability question is a generic monotone random process.

## 7. Bilinear orthogonal trim (BOT) — KILL

**Carrier and rule.**  Fix a finite vector space with a nondegenerate symmetric
bilinear form.  On ordered subspace pairs set
`T(U,W)=(U intersect W^perp, W intersect U^perp)`.

**Small-case signal.**  The two output subspaces are mutually orthogonal, and a
second application changes nothing; the image is exactly the mutually
orthogonal pairs.

**Theorem axes.**  Fibre enumeration by radicals and formed-space dimensions.

**Verdict.**  KILL.  This is a canonical idempotent formed-space retraction;
the dynamics is exhausted in one line and collides with the static
subspace/bilinear cluster.

## 8. Subspace meet-join comparator (SMJ) — KILL

**Carrier and rule.**  On ordered subspace pairs of `F_q^n`, set
`T(U,W)=(U intersect W,U+W)`.

**Small-case signal.**  It is idempotent and its image is the flag locus
`U subseteq W`; dimensions are sorted while total dimension is conserved.

**Theorem axes.**  Gaussian-binomial fibre counts and flag strata.

**Verdict.**  KILL.  This is the textbook lattice comparator/normal form, a
static one-step map rather than a new dynamical mechanism.

## 9. Random span growth (RSG) — KILL

**Carrier and rule.**  From a subspace `U <= F_q^n`, sample `v` uniformly in
the ambient vector space and set `U'=U+<v>`.

**Small-case signal.**  Dimension is a pure-birth chain with hold probability
`q^(dim U-n)` and reaches the full space almost surely.

**Theorem axes.**  Exact hitting-time generating function and `q`-coupon
decomposition.

**Verdict.**  KILL.  This is the generic random-span process and is already
conceptually occupied by the finite-subspace/quotient systems around P109 and
P173.

## 10. Hypergraph blocker normalization (HBN) — KILL

**Carrier and rule.**  For a hypergraph `H` on `[n]`, let `b(H)` be the family
of inclusion-minimal hitting sets, and set `T(H)=b(H)`.

**Small-case signal.**  The first image is a clutter and classical blocker
duality gives `b(b(H))=min(H)`, so every orbit immediately enters a fixed point
or a 2-cycle on clutters.

**Theorem axes.**  Fibre counts over clutter cores and self-dual blockers.

**Verdict.**  KILL.  The entire functional graph is a restatement of classical
blocker duality; ownership is obvious.

## 11. Endofunction squaring (EPS) — KILL

**Carrier and rule.**  On all endofunctions `f:[n]->[n]`, set `T(f)=f o f`.

**Small-case signal.**  Tree heights halve and each directed cycle is acted on
by doubling positions; cycle periods are multiplicative-order calculations.

**Theorem axes.**  Tail from maximum in-tree height and cycle-length 2-parts.

**Verdict.**  KILL.  It is literal functional-graph powering, forbidden by the
powering firewall and adjacent to P167/P171/P172.

## 12. Asynchronous path compression (APC) — KILL

**Carrier and rule.**  On an endofunction `f`, choose a nonperiodic vertex `v`
uniformly and replace only `f(v)` by `f(f(v))`; periodic vertices are inert.

**Small-case signal.**  The sum of distances to directed cycles strictly
decreases; absorbing endofunctions have all trees of height at most one.

**Theorem axes.**  Absorption histories, order dependence, and forest hook
counts.

**Verdict.**  KILL.  This is standard path compression presented as a Markov
chain and directly collides with P167's endofunction-surgery lane.

## 13. Random row-clone voter kernel (RCV) — KILL

**Carrier and rule.**  A state is an `n by m` binary table.  Choose an ordered
pair of distinct rows `(i,j)` uniformly and replace row `i` by row `j`.

**Small-case signal.**  Only the partition of row labels by row type matters;
it evolves as the complete-graph voter model and absorbs at a constant-row
table.

**Theorem axes.**  Coalescent duality, consensus time, endpoint law.

**Verdict.**  KILL.  This is the classical voter model with decorative binary
row labels; the partition/occupancy proof transfers directly.

## 14. Random adjacent gcd--lcm comparator (DGC) — KILL

**Carrier and rule.**  On tuples of divisors of a fixed integer `N`, choose an
adjacent index and replace `(x_i,x_{i+1})` by
`(gcd(x_i,x_{i+1}),lcm(x_i,x_{i+1}))`.

**Small-case signal.**  Prime valuations undergo independent adjacent
min--max comparators; fair schedules sort the tuple into a divisibility chain.

**Theorem axes.**  Absorption histories and products of sorting-network
statistics.

**Verdict.**  KILL.  It is distributive-lattice bubble sort and too close to
the valuation/gcd cluster around P142.

## 15. Random maximal-chain toggle (MCT) — KILL

**Carrier and rule.**  A state is a family `F subseteq 2^[n]`.  Choose a
permutation `pi` uniformly and toggle membership of every prefix set
`empty,{pi_1},...,{pi_1,...,pi_n}`.

**Small-case signal.**  This is addition by a maximal-chain incidence vector
in `F_2^(2^n)`; the state graph is a Cayley graph of the span of those vectors.

**Theorem axes.**  Code rank, Fourier spectrum, communication classes.

**Verdict.**  KILL.  It transfers P177's additive-code/Cayley/Fourier proof
package almost verbatim, despite changing the incidence geometry.

## 16. Boolean split normalization (BSN) — KILL

**Carrier and rule.**  On ordered pairs of subsets of `[n]`, set
`T(A,B)=(A intersect B,A triangle B)`.

**Small-case signal.**  A second step is `(empty,A union B)`, which is fixed;
the map is a coordinatewise four-state product of depth at most two.

**Theorem axes.**  Exact depth and product fibres.

**Verdict.**  KILL.  It is a shallow coordinatewise semilattice normalizer and
offers no theorem beyond elementary product bookkeeping; it also sits near the
intersection systems P158/P162.

## Triage count

- Literal systems specified: **16**.
- Exact pilots: **3**.
- Internal survivors: **2**.
- Killed or quarantined: **14**.
- Novelty claims: **0**.

