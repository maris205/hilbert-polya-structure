# Stochastic/graph breadth scout: ten literal finite or absorbing systems

**Audit date:** 2026-09-01 UTC
**Scope:** anonymous Route-A discovery only; no paper slot is assigned
**External status:** `HOLD_EXTERNAL`
**Literal systems tested:** **10**
**Current recommendation:** retain `VS1` and `PE1` as internal finalists;
permanently kill `RT1`, `CS1`, `IF1`, `CB1`, `PS1`, `MR1`, and `ID1`; retain
`DQ1` only as a theorem-thin reserve

This lane began from the preceding
[`problem anchor`](../../../papers137_141_sequence/PROBLEM_ANCHOR.md),
[`candidate kill ledger`](../../../papers137_141_sequence/phase1/CANDIDATE_POOL_AND_KILL_LEDGER.md),
and
[`collision firewall`](../../../papers137_141_sequence/phase1/SYSTEM_COLLISION_FIREWALL.md),
then applied the consolidated historical occupancy file
[`../../phase1/HISTORICAL_OCCUPANCY.md`](../../phase1/HISTORICAL_OCCUPANCY.md).
In particular, no candidate below is a majority triple contraction, threshold
random-greedy independent-set process, random Euclidean chunk, adjacent
representative contraction/coalescence, quota/birthday/Pólya stopping rule,
hyperedge exposure/cover process, or standard random-greedy support
corollary.  A changed scheduler or carrier name was not counted as a new
system.

The two finalists remain anonymous and internal.  The searches reported here
are owner-risk checks, not novelty certificates.  No source non-hit authorizes
priority, authorship, posting, specialist contact, submission, publicity, or
any other external action.

## 1. Exact executable contract

[`verify_stochastic_scout.py`](verify_stochastic_scout.py) uses Python integers
and `fractions.Fraction` only.  It uses no floating point, pseudorandom
sampling, third-party package, seed, timestamp, or network access.  Distinct
labelled events keep their exact multiplicities even when they reach the same
state.

The frozen stdout is [`CANONICAL.txt`](CANONICAL.txt).  Reproduce it from this
directory with

```bash
cmp -s CANONICAL.txt <(PYTHONDONTWRITEBYTECODE=1 python3 verify_stochastic_scout.py)
```

The run covers **176,865 parameter-labelled inputs, histories, or exact
states** and makes **1,248,967 exact assertions**.  Of these, 1,248,964 are
charged to individual systems and three are global system-count, unique-handle,
and nonempty-row sentinels.  Finite enumeration is counterexample pressure,
never a proof, owner clearance, or novelty evidence.

## 2. Permanent ten-system ledger

| ID | Literal stochastic system | Complete exact pilot | Exact signal and permanent disposition |
|---|---|---:|---|
| `VS1` | Fix an orientation of a finite simple graph.  At each time choose a vertex uniformly and reverse every incident arc. | All 1,099 labelled graphs through five vertices; every state in one push orbit; exact return counts through time five; every component-size partition of total order at most 24.  8,436 inputs, 26,787 assertions. | Complete orbit, spectrum, period, return law, and a component-order spectral inverse. **`FINALIST_INTERNAL/HOLD_EXTERNAL`.** |
| `PE1` | In a labelled convex polygon choose any current vertex uniformly, delete that ear, and record the new neighbour diagonal; stop at a triangle. | Every one of the 68,185 complete deletion sequences for orders 3 through 9; 625 terminal triangulations; every final-face refinement. 5,984 assertions. | Fixed clock, complete endpoint/history law by the weak dual tree, and a sharp least endpoint mass. **`FINALIST_INTERNAL/HOLD_EXTERNAL`.** |
| `RT1` | In a rooted tree choose an edge of the current root component uniformly, cut it, discard the component away from the root, and continue until the root is isolated. | All 1,441 root-labelled trees through six vertices and all 158,623 edge-priority orders. 4,333 assertions. | Exact all-tree PGF recursion and sharp mean extrema are correct, but the literal cutting/record equivalence is directly owned. **`KILL_DIRECT_OWNER`, permanent.** |
| `DQ1` | Expand an ordered positive workload vector into contiguous job-labelled service quanta; repeatedly delete the leftmost or rightmost quantum with probability one half and stop at one quantum. | Every ordered positive workload vector of total at most 12: 4,095 inputs and 45,057 marked endpoint cells. 61,437 assertions. | Complete marked binomial endpoint law and an inverse for the ordered workloads given total load. **`RESERVE_THEOREM_THIN`; no finalist slot.** |
| `CS1` | A chip at height `h>=2` moves one or two levels rootward with equal probability; height one has the forced move to zero. | Every height 0 through 50 and every clock coefficient. 1,427 assertions. | Closed clock polynomial and mean, but only a bounded-renewal/composition recurrence. **`KILL_OWNER_THIN`, permanent.** |
| `IF1` | Start with an interval, choose one of all uncut bonds uniformly, crack it, and continue through all resulting components; retain the binary cut genealogy. | All 46,233 bond orders through nine sites; all 2,055 endpoint shapes. 4,126 assertions. | Exact tree-hook endpoint law, but it is the classical Cartesian-tree/random-BST law. **`KILL_DIRECT_OWNER`, permanent.** |
| `CB1` | In a cactus choose a currently intact cycle uniformly, then delete a uniform edge of that cycle; stop at a forest. | Every ordered tuple of one to three cycle lengths in 3 through 6; 6,174 endpoints and 35,658 histories. 12,432 assertions. | Product-uniform deleted-edge law and fixed cycle-count clock. This is a one-line cactus factorisation inside reverse deletion. **`KILL_THEOREM_THIN`, permanent.** |
| `PS1` | On a permutation choose an adjacent length-three window and rotate it left or right uniformly. | Every permutation of orders 3 through 8: 46,230 states. 1,127,922 assertions. | Exactly two irreducible aperiodic parity classes, each uniform at stationarity. This is an immediate finite-group walk. **`KILL_GROUP_WALK_OWNER`, permanent.** |
| `MR1` | In a binary word choose a current occurrence of `11` uniformly and independently resample its two bits fairly; stop when `11` is absent. | Exact rational linear systems for lengths 2 through 6: 74 transient states, 50 absorbing states, every endpoint and mean Bellman equation. 444 assertions. | Rich terminal support and large means, but this is literal violated-event resampling without an all-length residual. **`KILL_RESAMPLING_OWNER`, permanent.** |
| `ID1` | In the current union of path intervals choose uniformly one of all nonempty contiguous subintervals and erase it; repeat to the empty set. | Every state through ten sites: 2,036 states. 4,072 assertions. | 1,672 variable-clock states, but the full-interval law has only exponential state-DP and no stable all-parameter spine. **`KILL_NO_CLOSED_ATLAS`, permanent.** |

These are ten genuinely different literal kernels: an orientation switch walk,
polygon ear deletion, root-retaining tree fragmentation, two-ended workload
service, monotone chip descent, bond-crack genealogy, cactus cycle breaking,
an adjacent three-cycle group walk, local bad-event resampling, and arbitrary
interval erasure.  Parameter sweeps within a row are validation points for one
system and are not counted as extra systems.

## 3. Finalist `VS1`: random vertex pushes on graph orientations

### 3.1 Literal chain and orbit classification

Let `G=(V,E)` be a fixed simple graph, `|V|=n`, and orient every edge.  A push
at `v` reverses every arc incident with `v`.  At each discrete time choose
`v` uniformly from all `n` vertices.  Pushes are commuting involutions.  If
the connected components have vertex sets `C_1,...,C_c`, their only relations
are

```text
product_(v in C_i) push(v) = identity.                         (VS1.1)
```

Thus every push orbit is a torsor for

```text
A_G = F_2^V / span{1_(C_1),...,1_(C_c)},
|A_G| = 2^(n-c).                                               (VS1.2)
```

The chain is irreducible on each orbit and symmetric, hence its unique
stationary law on that orbit is uniform.  There are
`2^(|E|-n+c)` such orbits.  This classifies every recurrent class, not merely
the support from one chosen orientation.

### 3.2 Complete spectrum, returns, and period

Write `s_i=|C_i|` and first use the uncompressed sign-count factors

```text
B_s(x) = sum_(0<=j<=s, j even) binom(s,j) x^j,
M_G(x) = product_i B_(s_i)(x).                                 (VS1.3)
```

A character of `A_G` assigns signs `epsilon_v in {+1,-1}` with
`product_(v in C_i) epsilon_v=1` in every component.  If exactly `k` signs
are negative, the transition eigenvalue is

```text
lambda_k = (1/n) sum_v epsilon_v = (n-2k)/n.                   (VS1.4)
```

Therefore the multiplicity of `lambda_k` is exactly `[x^k]M_G(x)`.  In
particular, for every `t>=0`, the return probability from any orientation in
the orbit is

```text
Pr(X_t=X_0) = 2^(-(n-c)) sum_k [x^k]M_G(x) ((n-2k)/n)^t.       (VS1.5)
```

The chain has period two exactly when every component has even order.  In
that case the all-negative character is legal and supplies eigenvalue `-1`.
If a component has odd order, its component relation gives an odd closed walk;
an isolated vertex gives a self-loop, while every nontrivial orbit also has a
two-step return.  Hence the remaining cases are aperiodic.

The verifier constructs every push orbit for every graph through five
vertices, checks the incidence-image rank, performs an independent integer
closed-walk recurrence through time five, and compares it with (VS1.5).

### 3.3 Spectral inverse for component orders

The proposed supporting inverse theorem is precise and has a sharp
nonidentifiability boundary:

> Given the ambient order `n`, the transition spectrum of one push orbit
> uniquely determines the multiset of connected-component orders.  It does
> not determine any internal component adjacency, nor the starting
> orientation inside the orbit.

The root-separation proof is elementary but real.  Compress the even spectral
indices by putting

```text
E_s(y) = sum_(r>=0) binom(s,2r)y^r,
Q_G(y) = product_i E_(s_i)(y),
M_G(x) = Q_G(x^2).                                             (VS1.6)
```

Now substitute `y=-t^2` in one compressed factor:

```text
E_s(-t^2)
 = ((1+i t)^s + (1-i t)^s)/2
 = (1+t^2)^(s/2) cos(s arctan t).                              (VS1.7)
```

For `s>=2`, the zero of `E_s(y)` nearest the origin is the simple negative
root

```text
rho_s = -tan^2(pi/(2s)).                                      (VS1.8)
```

Its modulus decreases strictly with `s`.  No smaller-order factor can vanish
at `rho_s`: equality would require `(2j+1)/r=1/s` with `r<s`.  Consequently,
the closest root of `Q_G` identifies the largest component order, and its
multiplicity identifies the number of largest components.  Divide their
`E_s` factors and repeat.  The root in (VS1.8) is simple, so its multiplicity
is exactly the number of components of that maximum order.  Since `E_1=1`,
isolated vertices are invisible to
the factor product itself and are recovered last from the known total `n`.

The executable performs this inverse with exact integer polynomial division,
not numerical roots.  It reconstructs all 7,337 component-size partitions of
every fixed total through 24.  This explicitly checks root multiplicities and
the isolated-vertex boundary.

### 3.4 Owner subtraction and historical collision gate

The vertex operation is not new.  Klostermeyer's primary paper
[*Pushing Vertices and Orienting Edges*](https://combinatorialpress.com/ars-articles/volume-051-ars-articles/pushing-vertices-and-orienting-edges/)
defines exactly the reversal of all arcs incident with a pushed vertex and
credits still earlier push-operation work.  The push operation, its commuting
relations, and push-equivalence terminology receive zero contribution credit.
Likewise, Fourier diagonalisation of an abelian Cayley walk and uniform
stationarity of a symmetric finite walk are generic owned tools and receive
zero credit.

The bounded primary search used the literal conjunctions `random vertex push
orientation Markov chain`, `push-equivalence random walk spectrum`, and
`vertex switching component sizes spectrum`.  It located the push-operation
literature but no source printing (VS1.3)--(VS1.8) as a stochastic inverse
package.  That non-hit leaves owner risk unresolved; it does not establish
novelty.

The closest internal mechanisms are parity dynamics on looped digraphs,
odd-component graph complementation, synchronous polarity/MIS dynamics, and
the earlier majority graph network.  `VS1` is not a schedule variant of any of
them: the carrier is an orientation torsor, the literal move is one cut-vector
translation, the temporal object is a recurrent abelian Cayley chain, and the
main output is a transition-spectrum inverse.  The shared use of binary
incidence algebra is nevertheless a serious proof-engine proximity and must
remain in the final collision review.

**Frozen internal contract:** orbit classification (VS1.2), complete spectrum
and return law (VS1.3)--(VS1.5), exact period criterion, and the component-order
inverse with its adjacency/orientation nonidentifiability boundary.  Status:
`FINALIST_INTERNAL/HOLD_EXTERNAL`.

## 4. Finalist `PE1`: uniform ear deletion of a convex polygon

### 4.1 Literal process and clock

Start with a labelled convex `n`-gon.  Every current vertex is an ear.  While
more than three vertices remain, choose **uniformly from all current
vertices**, delete that vertex, and record the diagonal joining its two
current neighbours.  The remaining polygon is again convex.  The process
stops at its final triangle; the recorded diagonals form a terminal
triangulation `T`.

The clock is pathwise

```text
tau_n = n-3.                                                   (PE1.1)
```

Every complete deletion sequence has probability

```text
1/[n(n-1)...4] = 6/n!.                                       (PE1.2)
```

The temporal content is therefore not the clock alone but the complete
many-to-one history law onto triangulations.

### 4.2 Root-face hook sum and complete endpoint law

Let `D_T` be the weak dual tree of `T`: its `N=n-2` vertices are the triangular
faces, with dual adjacency across an internal diagonal.  Fix a possible final
face `r` and root `D_T` there.  For each nonroot dual vertex `v`, let
`s_v^(r)` be the size of its descendant subtree.

Deletion sequences ending at face `r` are exactly the orders that remove
children before parents in this rooted dual tree.  The rooted-tree hook
formula gives

```text
h_r(T) = (n-3)! / product_(v != r) s_v^(r).                   (PE1.3)
```

The final-face marked history count, total history count, and exact endpoint
law are consequently

```text
H(T,r) = h_r(T),
H(T)   = sum_(r in Faces(T)) h_r(T),
Pr(T)  = 6 H(T)/n!.                                          (PE1.4)
```

This is every-target and root-resolved.  The verifier does not infer it from
normalisation: it independently enumerates all deletion sequences through
order nine, constructs each weak dual, and checks every one of the 625
triangulations and every possible final face against (PE1.3).

The exact profiles `n : number of triangulations / min H / max H` are

```text
3: 1/1/1       4: 2/2/2       5: 5/4/4       6: 14/8/12
7: 42/16/28    8: 132/32/112  9: 429/64/316.
```

### 4.3 Sharp least history and endpoint mass

For any finite tree `D`, let `L(D)` count orders that delete leaves until one
vertex remains.  Then

```text
L(singleton)=1,
L(D)=sum_(ell a leaf of D) L(D-ell).                          (PE1.5)
```

Induction gives

```text
L(D) >= 2^(|D|-1),                                           (PE1.6)
```

with equality exactly for a path.  A path has two leaf choices at every
nontrivial stage and attains equality.  A nonpath tree has at least three
leaves, so applying the induction bound to every first deletion makes the
inequality strict.  Since `H(T)=L(D_T)`, this proves the sharp theorem

```text
H(T) >= 2^(n-3),
Pr(T) >= 6*2^(n-3)/n!,                                      (PE1.7)
```

with equality exactly when the weak dual of `T` is a path.  Fans are examples,
but the equality class is the full path-dual class, not just fans.

### 4.4 Owner subtraction and historical collision gate

Ear clipping is classical and receives zero credit.  Eder, Held, and
Palfrader's primary computational-geometry article
[*Parallelized ear clipping for the triangulation and constrained Delaunay
triangulation of polygons*](https://doi.org/10.1016/j.comgeo.2018.01.004)
uses the standard ear operation, and Regev's
[*A bijection between triangulations and 312-avoiding
permutations*](https://arxiv.org/abs/1311.1955) explicitly uses ear clipping in
the convex-polygon/triangulation setting.  Convex-polygon triangulations,
weak-dual trees, Catalan enumeration, and the generic rooted-tree hook formula
are all zero-credit background.

The bounded primary search used `random ear clipping triangulation
distribution`, `ear removal sequences dual tree`, and `triangulation shelling
orders hook formula`.  It found deterministic/randomised algorithmic uses and
ear-clipping bijections, but no primary source stating the uniform-current-ear
endpoint law (PE1.3)--(PE1.4) together with the sharp path-dual minimum
(PE1.7).  This non-hit does not clear the conjunction.

The closest internal systems are rooted-forest leaf peeling and chord-based
matching/retraction geometry.  The dual-tree proof engine is genuinely close
to forest peeling and must be charged at full strength.  Literal separation is
still clear: the evolving carrier is a shrinking convex polygon, any current
vertex is selected uniformly, the endpoint is a random triangulation rather
than a forest core, and the exact output is a root-face-refined endpoint mass.
The chord system uses a matching/retraction carrier and crossing-component
fibres, not triangulation shellings.  There is no majority, greedy MIS,
coalescence, or cover/exposure mechanism.

**Frozen internal contract:** the literal uniform-current-vertex process,
fixed clock (PE1.1), root-face hook sum and complete endpoint law
(PE1.3)--(PE1.4), and sharp minimum/equality classification (PE1.7).  Status:
`FINALIST_INTERNAL/HOLD_EXTERNAL`.

## 5. Strong exact signal killed by a direct owner: `RT1`

Let every edge of a rooted tree carry an independent continuous priority.
Cutting the least-priority edge of the current root component and discarding
the other component is distributionally the literal uniform-edge process.
An edge is actually cut exactly when its priority is a lower record on its
root path.

There is a compact all-tree PGF.  For a vertex `v`, let `R_v(t,z)` be the PGF
for record cuts below `v` when the ancestral cutoff priority is `t`; leaves
have `R_v=1`.  If `w` ranges over the children of `v`, then

```text
R_v(t,z) = product_w [
    (1-t) R_w(t,z) + z integral_0^t R_w(u,z) du
],
G_T(z) = R_root(1,z).                                        (RT1.1)
```

The two terms distinguish a child edge arriving after the ancestral cutoff
from a child edge that is itself a record.  The mean follows immediately:

```text
E X_T = sum_(v != root) 1/depth(v).                           (RT1.2)
```

Ordering the nonroot vertices by nondecreasing depth gives `depth(v_i)<=i`,
so among rooted trees on `n` vertices

```text
H_(n-1) <= E X_T <= n-1,                                    (RT1.3)
```

with equality at the rooted path and rooted star, respectively.  Exact
priority enumeration verifies the full PGF for every labelled rooted tree
through six vertices.

None of this can be promoted.  Meir and Moon's primary paper
[*Cutting down random trees*](https://doi.org/10.1017/S1446788700006698)
defines the same uniform edge cut, retention of the root component, and root
isolation objective.  Janson's
[*Random cutting and records in deterministic and random
trees*](https://doi.org/10.1002/rsa.20086) explicitly proves the cutting/record
distributional equivalence while conditioning on deterministic trees.  That
consumes the literal process and its decisive proof engine.  `RT1` is therefore
`KILL_DIRECT_OWNER` permanently, even though (RT1.1)--(RT1.3) are useful exact
regression identities.

## 6. The theorem-thin reserve and remaining permanent kills

### 6.1 `DQ1`: exact but below the value floor

For ordered workloads `a_1,...,a_m`, put `S=sum a_i` and
`A_j=sum_(i<=j)a_i`, with `A_0=0`.  In the first `S-1` fair end choices, let
`K` be the number of left deletions.  The sole surviving quantum has original
position `K+1`, hence

```text
Pr(last job=j, K=k) = binom(S-1,k)/2^(S-1)
                       if A_(j-1) <= k < A_j,
Pr(last job=j) = 2^(-(S-1))
                 sum_(k=A_(j-1))^(A_j-1) binom(S-1,k).        (DQ1.1)
```

Given `S`, cumulative endpoint masses are strictly increasing binomial CDF
values and recover all `A_j`, hence the ordered workload vector.  This is a
correct endpoint inverse, but its proof is only the fair two-ended deletion
coupling.  It repeats the endpoint-peeling/binomial silhouette and lacks a
second temporal spine.  It remains `RESERVE_THEOREM_THIN`, not a finalist.

### 6.2 Compact kill certificates

- `CS1` has
  `F_0=1`, `F_1=z`, `F_h=z(F_(h-1)+F_(h-2))/2`, and
  `E T_h=2h/3+2/9-(2/9)(-1/2)^h`.  Its coefficient law is only weighted
  compositions with parts one and two, too close to occupied capped-Fibonacci
  and composition machinery.  **Permanent kill.**
- `IF1` maps a uniform bond order to its Cartesian tree.  For a binary shape
  with `m` internal nodes, its history count is
  `m!/product_v |subtree(v)|`.  This is exactly the classical
  random-BST/Cartesian-tree hook law.  **Permanent direct-owner kill.**
- `CB1` deletes exactly one edge independently and uniformly from every cactus
  cycle; every endpoint has mass `product_i 1/ell_i`, the clock is the cycle
  count, and every endpoint has `c!` cycle-order histories.  This is a
  factorised reverse-delete control, not a paper theorem.  **Permanent kill.**
- `PS1` is the symmetric Cayley walk generated by adjacent three-cycles and
  their inverses.  Adjacent three-cycles generate the alternating group, so
  the two permutation parities are the only recurrent classes; inverse pairs
  and a generator cubed give return lengths two and three.  Uniform
  stationarity and aperiodicity are immediate.  **Permanent group-walk kill.**
- `MR1` is literal violated-event resampling for the bad events `w_iw_(i+1)=11`.
  The exact terminal laws are nontrivial but the finite linear system has no
  all-length factorisation, and the process lies inside owned resampling
  algorithms.  **Permanent kill.**
- `ID1` is genuinely state dependent and has variable clocks, but even its
  full-interval means through order ten show no stable closed form; only the
  subset-state Bellman DP survives.  **Permanent no-atlas kill.**

No killed row may be revived by biasing its scheduler, adding independent
waiting times, changing labels, or retaining a static support statistic.

## 7. Full historical collision firewall

| This lane | Closest occupied interface | Literal/temporal separation and final gate |
|---|---|---|
| `VS1` | parity dynamics on looped digraphs; odd-component complementation; synchronous graph polarity and majority networks | Orientation torsors and uniform vertex cut translations are literal new moves; complete recurrent spectrum and component-order inverse are new temporal objects internally. Binary-incidence proof overlap remains a mandatory review gate. **Finalist/HOLD.** |
| `PE1` | rooted-forest leaf peeling; chord-matching retraction/fibres | Polygon vertices, recorded triangulation diagonals, and endpoint probabilities differ literally. Dual-tree hook machinery is a serious shared proof engine and receives zero generic credit. **Finalist/HOLD.** |
| `RT1` | rooted-forest peeling and rootward pile dynamics | Edge cutting and root-component retention differ internally, but the exact external cutting process and record reduction are directly owned. **Kill.** |
| `DQ1` | push–pop queues and continued-fraction queues | Two-ended quantum deletion is not either occupied queue update, but its sole spine is a binomial survivor law. **Reserve only.** |
| `CS1` | capped Fibonacci absorption and balanced compositions | Literal monotone chip jumps are distinct; the entire theorem transfers from one/two-step renewal compositions. **Kill.** |
| `IF1` | tree pruning and chord geometry | Cutting every bond and retaining the genealogy is distinct, but the endpoint is exactly a Cartesian tree with the standard hook law. **Kill.** |
| `CB1` | graph reverse deletion and component processes | Cycle-first cactus scheduling is literal new bookkeeping; the product endpoint law is too thin and owner-saturated. **Kill.** |
| `PS1` | permutation pruning, record-block transforms, and finite group walks | No literal transform collision, but recurrent classification is generic Cayley generation. **Kill.** |
| `MR1` | reset/random finite-memory systems | Local violated-pair resampling is distinct from the occupied reset maps; the direct resampling owner and missing all-length theorem kill it. **Kill.** |
| `ID1` | shrinking-word and fragmentation lanes | Arbitrary interval erasure is literal new and avoids contraction/coalescence, but no exact atlas survives beyond Bellman recursion. **Kill.** |

The finalist pair is internally separated as well.  `VS1` is a length-preserving
recurrent walk on an orientation torsor, diagonalised by characters and
supporting a spectral inverse.  `PE1` is a finite shrinking geometric process
with deterministic clock, random triangulation endpoints, and dual-tree
history hooks.  They share neither carrier, literal update, temporal
silhouette, endpoint object, nor primary proof engine.

## 8. Final recommendation

| Rank | Handle | Exact contract | Gate |
|---:|---|---|---|
| 1 | `VS1` | orbit atlas, complete spectrum/returns/period, component-order spectral inverse | **`FINALIST_INTERNAL/HOLD_EXTERNAL`; push operation and Cayley machinery zero-credit** |
| 2 | `PE1` | fixed clock, every-triangulation and final-face hook law, sharp path-dual minimum | **`FINALIST_INTERNAL/HOLD_EXTERNAL`; ear clipping and generic tree hooks zero-credit** |
| 3 | `DQ1` | complete marked binomial endpoint law and workload inverse | **reserve only; theorem-thin** |
| 4 | `RT1` | all-tree record PGF and sharp mean extrema | **permanent direct-owner kill** |
| 5--10 | remaining six | exact negative controls | **permanent kills** |

Only `VS1` and `PE1` should enter the cross-lane selection gate.  This is an
internal recommendation, not a novelty, priority, authorship, or publication
claim.  External status remains `HOLD_EXTERNAL`.
