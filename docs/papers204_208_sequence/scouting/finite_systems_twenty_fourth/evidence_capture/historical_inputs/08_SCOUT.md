# Stochastic / local-rewrite scouting lane

**Audit date:** 2026-08-31  
**Scope:** exploratory only; no paper number assigned and no system frozen  
**Internal decision:** `GO_INTERNAL` for `S02` alone  
**External decision:** `HOLD_EXTERNAL` pending independent owner review  
**Hostile disposition:** `S01`, `S03`--`S26` are stopped or killed

This lane tested literal stochastic kernels rather than names or informal
analogies. It spans shrinking words, occupied subsets, endofunctions, spin
systems, independent sets, matchings, exclusion particles, random walks,
integer rewrites, chip configurations, permutations, Boolean lattices, Dyck
words, orientations, and trees. A finite non-hit is not a novelty result. In
particular, the lane does not recycle P121's product-plus-one coalescence,
P126's balanced refinement, or P117's prohibited pointer-doubling mechanism.

## 1. Exact executable contract

The executable is `code/pilot_exact.py`; its frozen stdout is
`code/PILOT_CANONICAL.txt`. It uses only the Python standard library. Every
probability is a `fractions.Fraction`; all other quantities are integers.
There is no floating point, pseudorandom sampling, third-party package,
network access, or timestamp in the computation.

Fresh execution and byte comparison:

```bash
cd docs/papers127_131_sequence/scouting/stochastic
PYTHONDONTWRITEBYTECODE=1 python3 code/pilot_exact.py > /tmp/stochastic_pilot.out
cmp -s /tmp/stochastic_pilot.out code/PILOT_CANONICAL.txt
```

The stable run executes **9,225,587 exact assertions**: 9,225,583 attributed
to the 26 systems below and four global ledger assertions. The word “state”
means a literal enumerated source, reachable state, or dynamic-programming
state specified in the corresponding row; it never means a sample.

## 2. Literal system ledger

“Uniform active” means uniform among currently effective events. A
uniform-site or uniform-bond rule retains its stated lazy moves. A
nondeterministic rewrite enumerates every legal successor.

| ID | Literal state space and kernel | Exact range; states | Assertions | Decision and earliest signal |
|---|---|---:|---:|---|
| `S01` | Nonempty words over `Z/3Z`; choose an unequal adjacent pair uniformly, retain its cyclic winner, and delete its loser. | All words of length 1--9; periodic-prefix terminal-size law through length 19; 150,459 states. | 3,076,752 | `STOP_UNPROVED_OWNER_COLLISION`: the full periodic law matches the PD(1/3,0) block-count recurrence, but no literal reduction was proved and that target law is owned. |
| `S02` | Occupied subsets of a rooted path; choose a nonroot occupied vertex uniformly, move it one step rootward, and coalesce on occupied arrival. | All 8,178 nonempty subsets for `n=1..12`; every one of the 4,095 root-containing subsets receives the general mean check; full-start law through `n=10`. | 102,531 | `PROMOTE`: the mean from every rooted initial state is an exact sum of adjacent-interface meeting means; the full-start PGF also has exact support, endpoint masses, and mean. |
| `S03` | Endofunctions started at a directed cycle; choose active `v` uniformly and set `f(v):=f(f(v))`. | Complete reachable set for `n=1..7`; closed-SCC audit through `n=6`; 280,392 states. | 3,202,042 | `KILL_INTERNAL`: the census `(n+1)^(n-1)` is correct negative evidence, but the rule is P117-excluded pointer doubling. |
| `S04` | Binary line; choose a bond uniformly, rewrite `11` to `00`, otherwise hold. | All words `n=1..12`; 8,190 states. | 131,086 | `KILL_OWNER_CLASSICAL`: Fibonacci absorbing sets and parity are standard annihilation/RSA structure. |
| `S05` | Binary line with fixed endpoints; choose an internal site uniformly and apply strict three-site majority. | All words `n=1..10`; 2,046 states. | 17,940 | `KILL_OWNER_CLASSICAL`: each flip removes two domain walls; zero-temperature one-dimensional Glauber core. |
| `S06` | Binary words; choose a length-three window uniformly and interchange `010` and `111`, otherwise hold. | All words `n=1..9`; 1,022 states. | 10,767 | `KILL_TRIVIAL_REVERSIBILITY`: parity sectors and involutive edges give immediate uniform component stationarity. |
| `S07` | Independent sets of a path; single-site activity-one hard-core heat bath. | All independent sets `n=1..12`; 984 states. | 7,936 | `KILL_OWNER_CLASSICAL`: exact detailed balance is the standard hard-core Glauber chain. |
| `S08` | Matchings of a path; choose an edge uniformly and toggle it when legal. | All matchings on paths with 2--13 vertices; 984 states. | 17,204 | `KILL_OWNER_CLASSICAL`: symmetric monomer-dimer Glauber dynamics. |
| `S09` | Cyclic binary words; choose an active cyclic `110` uniformly and rewrite it to `101`. | All words `n=4..9`, complete SCC audit; 1,008 states. | 1,026 | `KILL_OWNER_CLASSICAL`: facilitated exclusion/TASEP specialization. |
| `S10` | Binary opinions on a path; choose an oriented edge uniformly and copy donor to receiver. | All words `n=2..9`; 1,020 states. | 30,728 | `KILL_OWNER_CLASSICAL`: the standard voter martingale. |
| `S11` | Unlabelled occupancies on a star; choose a particle then a neighboring destination uniformly, with coalescence. | All nonempty occupancies on stars with 1--8 leaves, complete SCC audit; 1,012 states. | 8,200 | `KILL_OWNER_CLASSICAL`: ordinary coalescing random walks. |
| `S12` | Binary particles on a cycle; choose a particle and fair direction, move into a vacancy or annihilate on collision. | All occupancies `n=3..9`, complete SCC audit; 1,016 states. | 9,214 | `KILL_OWNER_CLASSICAL`: parity gives the classical annihilating-walk sectors. |
| `S13` | Positive integer pairs; subtract the smaller from the larger, fixing equality. | Every pair `1<=a,b<=20`; 400 sources. | 5,153 | `KILL_OWNER_CLASSICAL`: subtractive Euclidean algorithm. |
| `S14` | Finite nonnegative digit-count vectors; fire `c_i>=2` by two-to-one binary carrying. | Every descendant of `N=0..31` in six positions; 1,626 states. | 6,208 | `KILL_OWNER_CLASSICAL`: abelian carries and `N-popcount(N)` firings. |
| `S15` | Chip configurations on a finite path with endpoint sinks; asynchronously fire height at least two. | Initial heights in `{0,1,2,3}^ell`, `ell=1..5`, and all descendants; 5,495 states. | 17,200 | `KILL_OWNER_CLASSICAL`: abelian sandpile stabilization. |
| `S16` | Permutations; choose a position uniformly and move its item to the front. | All permutations `n=1..8`; 46,233 states. | 46,249 | `KILL_OWNER_CLASSICAL`: uniform Tsetlin/random-to-front chain. |
| `S17` | Permutations; choose a bond uniformly and swap exactly when it is a descent. | All permutations `n=1..8`; 46,233 states. | 474,985 | `KILL_OWNER_CLASSICAL`: inversion descent is bubble-sort/0-Hecke structure. |
| `S18` | Permutations; choose an unordered pair uniformly and transpose its images. | All permutations `n=2..7`; 5,912 states. | 236,008 | `KILL_OWNER_CLASSICAL`: random-transposition split/merge chain. |
| `S19` | Tuples of Boolean-lattice elements; replace active adjacent `(A,B)` by `(A intersect B,A union B)`. | All `m`-tuples for `m=2..5`, ground size `q=1..3`; 38,860 states. | 172,570 | `KILL_DECOMPOSES_TO_CLASSICAL`: the basin product decomposes elementwise into binary 0-Hecke sorts. |
| `S20` | Dyck words; choose a peak `()` uniformly and delete it. | Every Dyck word of semilength 0--10; 23,714 states. | 274,677 | `KILL_SCHEDULE_ONLY`: lifetime is deterministically the semilength; only classical deletion histories remain. |
| `S21` | Variable-length binary words; choose an equal adjacent pair uniformly and delete it. | Every source of length 0--16; 131,071 sources. | 1,048,577 | `KILL_STANDARD_NORMAL_FORM`: stack/free-product reduction owns the alternating normal form. |
| `S22` | Orientations of a cycle; choose a sink uniformly and reverse both incident edges. | Every orientation `n=3..10`, complete SCC audit; 2,040 states. | 4,614 | `KILL_OWNER_CLASSICAL`: standard sink-firing/chip-firing action. |
| `S23` | Permutations; choose a strict local minimum uniformly and rotate `(a,b,c)` to `(b,c,a)`. | All permutations `n=3..8`, complete SCC audit; 46,230 states. | 90,144 | `KILL_WEAK_STRUCTURE`: no nontrivial closed SCC, but no compact clock, basin law, or invariant. |
| `S24` | Fixed-length binary words; choose `101` uniformly and rewrite it to `010`. | All words `n=1..15`; terminal sets through `n=12`; 65,534 sources. | 196,612 | `KILL_NONCONFLUENT_COMPLEXITY`: 3,106 sources have multiple normal forms, with multiplicity at least nine. |
| `S25` | Variable-length binary words; choose an unequal boundary uniformly, then delete either endpoint with probability `1/2`. | All words of length 1--10; alternating full law through length 17; 6,763 states. | 34,922 | `KILL_OWNER_INTERNAL`: paired lengths reproduce PD(1/2,0), behind another adjacent-coalescence wrapper. |
| `S26` | Complete rooted binary trees; repeatedly choose a currently available edge uniformly and greedily match/delete both endpoints. | Heights 0--3 with complete remaining-vertex recursion; 514 states. | 2,238 | `KILL_OWNER_NO_ALL_PARAMETER_RESIDUAL`: at height three the size law is `{4:9/49,5:40/49}`, but no all-height closure survived generic random-greedy/RSA ownership. |

These are 26 actually enumerated systems. `S25` and `S26` were genuine
replacement kernels after `S01` and `S03` failed; neither was counted as a
survivor merely to fill a quota.

## 3. Kill discipline and replacement audit

- `S03` is the decisive hostile reversal. Its finite census is strong and
  correct, but the literal mechanism is pointer doubling, explicitly fenced
  by the P117 history. It receives no promotion credit.
- `S04`--`S22` were stopped as soon as exact output exposed a standard
  annihilation, Glauber, exclusion, voter, random-walk, Euclidean, abelian,
  sorting, split/merge, Catalan, reduction, or chip-firing engine.
- `S23` and `S24` failed structural gates: weak output and uncontrolled
  nonconfluence, respectively.
- The first replacement `S25` produced a clean all-parameter recurrence,
  but it is exactly a PD(1/2,0) block-count law and is too close to the
  adjacent-coalescence firewall. It is a kill, not a promotion.
- The second replacement `S26` changes both state space and scheduler, but
  only a height-three fraction survived. Generic random-greedy
  matching/random sequential adsorption already owns the proof engine, and
  no exact all-height second output emerged. It is killed. A separate reserve
  lane is required if the global batch needs another candidate.

## 4. Stopped candidate `S01`: useful exact negative evidence

Let `W_n=(0,1,2,0,1,2,...)` be the prefix of length `n`, and let `M_n` be
its terminal monochromatic length under `S01`. Exact computation shows that
the laws for lengths `3k+1`, `3k+2`, and `3k+3` coincide for every complete
triple tested through length 18; length 19 supplies the next `3k+1` law.
Writing that common law as `p_k(m)` and its PGF as `F_k(z)`, the verified
recurrence is

$$
p_{k+1}(m)=p_k(m)\left(1-\frac{m}{3(k+1)}\right)
 +p_k(m-1)\frac{m-1}{3(k+1)},\qquad p_0(1)=1,
$$

or equivalently

$$
F_{k+1}(z)=F_k(z)+\frac{z(z-1)}{3(k+1)}F'_k(z).
$$

The script checks this law through `k=6` and the rising moments

$$
\mathbb E[M_k^{\overline r}]
=r!\prod_{j=1}^k\frac{3j+r}{3j},\qquad 1\le r\le5.
$$

The mean product is only the case `r=1`. The entire recurrence is exactly
the block-count chain of the two-parameter Poisson--Dirichlet/Chinese
restaurant process with `alpha=1/3, theta=0`. That observation is negative
evidence: no literal coupling from the cyclic-deletion word to that process
was obtained, while the target distribution and all consequences of its
recurrence are directly owned. Therefore `S01` is not promoted. The gamma
ratio, `k^(1/3)` asymptotic, and generic cyclic-coalescence language receive
zero residual credit.

Boundary firewall: equal adjacent letters are inactive; the word is a line,
not a cycle; the scheduler is uniform among active unequal boundaries; and
changing any of these produces a different process. These distinctions do
not cure the missing reduction or owner collision.

## 5. Sole survivor `S02`: rootward active-pile coalescence

### 5.1 Literal model and exact PGF

Fix the path `{0,1,...,n-1}` with absorbing root zero. A state is a finite
occupied set `S` containing zero. If `S != {0}`, choose `v in S\{0}`
uniformly and set

$$
C_v(S)=(S\setminus\{v\})\cup\{v-1\}.
$$

Set occupancy removes multiplicity at a collision. Let `T_S` be the number
of updates to `{0}` and `G_S(z)=E[z^{T_S}]`. The literal first-step law is

$$
G_{\{0\}}(z)=1,\qquad
G_S(z)=\frac{z}{|S|-1}\sum_{v\in S\setminus\{0\}}G_{C_v(S)}(z).
$$

The potential `Phi(S)=sum_{x in S}x` decreases strictly, so this is a finite
acyclic recurrence and absorption is certain.

### 5.2 General-initial-state interface theorem

Write `S={s_0,s_1,...,s_r}` with
`0=s_0<s_1<...<s_r`. Define `h(a,b)` for `0<=a<=b` by

$$
h(a,a)=0,\qquad h(0,b)=b,
$$

and, for `0<a<b`,

$$
h(a,b)=\frac12+
\frac{h(a-1,b)+h(a,b-1)}2.
$$

Then the paper-level theorem contract is

$$
\boxed{\mathbb E[T_S]=\sum_{i=1}^{r}h(s_{i-1},s_i).}
$$

This is not a fitted full-start mean. It covers every rooted initial subset.
The exact program independently computes the discrete Bellman expectation
and the interface sum for all **4,095** root-containing subsets across
`n=1..12`; every equality passes.

Proof route, now closed at theorem level:

1. Poissonize by giving each occupied nonroot pile a rate-one clock. The
   embedded jump chain is exactly the uniform-active discrete process.
2. Label the initially occupied positions in order and use the standard
   graphical construction for ordered coalescing pure-death walks. At time
   `t`, the number `N_t` of nonroot piles equals the number of still-open
   interfaces between consecutive initial labels.
3. The jump-counting process has predictable intensity `N_t`. Since the
   state space is finite and `Phi` strictly decreases, compensator identity
   and Tonelli give

   $$
   \mathbb E[T_S]=\mathbb E\!\int_0^\infty N_t\,dt
   =\sum_{i=1}^{r}\mathbb E[\tau_i],
   $$

   where `tau_i` is the lifetime of interface `(s_{i-1},s_i)`.
4. Until two ordered graphical paths meet, they occupy distinct sites and
   read independent rate-one clocks. First-event conditioning gives exactly
   the displayed recurrence for `h`; if the lower path is at zero, the upper
   path needs `b` mean-one jumps. Hence `E[tau_i]=h(s_{i-1},s_i)`.

No independence among the different interface lifetimes is asserted or
needed; linearity and Tonelli are sufficient.

### 5.3 Full-start corollary and second exact outputs

For adjacent starts, a ballot/reflection evaluation of the triangular
recurrence gives

$$
h(m-1,m)=\frac{(2m-1)!!}{(2m-2)!!}
=\frac{2m}{4^m}{2m\choose m}
=\mathbb E|S_{2m}|,
$$

where `S_{2m}` is a length-`2m` simple symmetric walk. One rigorous route is
to stop the fair event-type walk when its gap first reaches zero or its lower
particle has made `m-1` moves. Catalan paths count the former exits and the
ballot difference

$$
{p+q-1\choose q}-{p+q-1\choose q-1},\qquad p=m-1,
$$

counts the latter exits. Pascal telescoping yields
`2m*binom(2m,m)/4^m`; equivalently these values satisfy
`2m h(m,m+1)=(2m+1)h(m-1,m)` with base value `h(0,1)=1`.
Thus for full occupancy `S_n={0,...,n-1}`,

$$
\boxed{\mathbb E[T_{S_n}]
=\sum_{m=1}^{n-1}\frac{(2m-1)!!}{(2m-2)!!}.}
$$

Consequently

$$
\mathbb E[T_{S_n}]
=\frac{4}{3\sqrt\pi}n^{3/2}+O(n^{1/2}).
$$

The PGF computation additionally verifies through `n=10` that

$$
\operatorname{supp}(T_{S_n})=
\{n-1,n,\ldots,{n\choose2}\},
$$

$$
\Pr(T_{S_n}=n-1)=\frac1{(n-1)!},\qquad
\Pr\!\left(T_{S_n}={n\choose2}\right)
=2^{-{n-1\choose2}}.
$$

The support interval itself admits an induction for every rooted `S`:
`supp(T_S)={max(S),...,Phi(S)}`. If the predecessor of `max(S)` is empty,
moving the maximum exposes the entire interval by induction. If it is
occupied, combine the top collision with the move at the bottom of that
occupied run; their successor intervals overlap because `Phi(S)>=2max(S)-1`.
For the full state, the minimum path is the unique descending collision order,
giving `1/(n-1)!`. The maximum-mass formula has exact evidence and a
noncollision/ballot proof route, but it is not needed for the promotion and
must not be elevated to a paper claim until that separate derivation is fully
written.

### 5.4 Edge cases and variant firewall

- `S={0}` gives `T_S=0`; the interface sum is empty.
- A singleton `{0,b}` has deterministic lifetime `b`, matching `h(0,b)`.
- The state is a set; mass-labelled piles or retained multiplicity are
  different systems.
- Only occupied nonroot sites ring at equal rate. Uniform geometric-site
  clocks with lazy moves, clocks attached permanently to original particles,
  or edge clocks change the embedded chain.
- Motion is deterministic and rootward. Unbiased, reversible, or
  non-backtracking coalescing walks are not this kernel.
- The proved contract is for a path. A rooted-tree extension is outside this
  lane and requires a new theorem and owner gate.

## 6. Owner-direct primary-source screen

Search date: **2026-08-31**. Only primary technical papers are used as owner
evidence. Bounded non-hit is explicitly not treated as novelty.

### 6.1 `S01` owner hit

Verbatim queries included:

```text
"number of tables" "K_n" Chinese restaurant process alpha
Pitman Chinese restaurant process generalized Stirling numbers DOI
Jim Pitman exchangeable random partitions alpha theta Chinese restaurant 1995 DOI
"Exchangeable and partially exchangeable random partitions" DOI
"rock-paper-scissors" one-dimensional stochastic particle system exact solution coarsening
"Coalescence Model of Rock-Paper-Scissors Particles"
```

- J. Pitman, “Exchangeable and partially exchangeable random partitions,”
  *Probability Theory and Related Fields* 102 (1995), 145--158,
  [DOI 10.1007/BF01213386](https://doi.org/10.1007/BF01213386), directly
  owns the two-parameter partition/block-count mechanism. All consequences
  of the PD(1/3,0) recurrence receive zero credit.
- J. Pitman and M. Yor, “The two-parameter Poisson--Dirichlet distribution
  derived from a stable subordinator,” *Annals of Probability* 25 (1997),
  855--900, [DOI 10.1214/aop/1024404422](https://doi.org/10.1214/aop/1024404422),
  owns the named distributional family.
- Y. Itoh, “Coalescence Model of Rock-Paper-Scissors Particles,” *Physica A*
  648 (2024), 129950,
  [DOI 10.1016/j.physa.2024.129950](https://doi.org/10.1016/j.physa.2024.129950),
  owns generic RPS coalescence/survivor framing. Its kernel difference does
  not rescue the unproved word-to-PD reduction.

Result: direct law ownership plus missing literal proof. `S01` is stopped.

### 6.2 `S02` owner subtraction

Verbatim queries included:

```text
"rootward" coalescing particles path stochastic
coalescing particles directed path move toward root occupied sites
"coalescing random walk" rooted tree absorption time path
"pure death" coalescing random walks interface meeting time
"ordered coalescing" pure-death processes meeting time
coalescing pure death process adjacent interface lifetime
directed coalescing random walks path rate one absorption exact
"(2n-3)!!" "(2n-4)!!" absorption time
```

Primary technical neighbors and zero-credit subtraction:

| Source | Zero-credit owner scope | Literal residual after subtraction |
|---|---|---|
| V. Kanade, F. Mallmann-Trenn, and T. Sauerwald, “On Coalescence Time in Graphs: When Is Coalescing as Fast as Meeting?”, *ACM Transactions on Algorithms* 19(2) (2023), [DOI 10.1145/3576900](https://doi.org/10.1145/3576900); [arXiv:1611.02460](https://arxiv.org/abs/1611.02460) | General coalescing-walk time, full occupancy, and meeting/hitting comparisons. | Their particles make random walks on undirected graphs; they do not state the deterministic rootward active-pile interface sum found here. |
| C. Cooper, R. Elsässer, H. Ono, and T. Radzik, “Coalescing Random Walks and Voting on Connected Graphs,” *SIAM J. Discrete Math.* 27 (2013), [DOI 10.1137/120900368](https://doi.org/10.1137/120900368); [arXiv:1204.4106](https://arxiv.org/abs/1204.4106) | One-particle-per-vertex coalescing walks, voting duality, and bounds. | Independent graph walks differ from uniform-active deterministic rootward motion. |
| I. Benjamini, E. Foxall, O. Gurel-Gurevich, M. Junge, and H. Kesten, “Site recurrence for coalescing random walk,” *Electronic Communications in Probability* 21 (2016), [DOI 10.1214/16-ECP5](https://doi.org/10.1214/16-ECP5); [arXiv:1510.04721](https://arxiv.org/abs/1510.04721) | Coalescing systems, rooted-tree settings, and graphical recurrence tools. | Infinite-time recurrence and non-backtracking walks do not supply this finite pure-death law. |
| A. Ermakov, “Exact probabilities and asymptotics for the one-dimensional coalescing ideal gas,” *Stochastic Processes and their Applications* 71 (1997), 275--284, [DOI 10.1016/S0304-4149(97)00077-X](https://doi.org/10.1016/S0304-4149(97)00077-X) | Exact one-dimensional coalescing laws and reductions to simple-walk hitting receive zero credit. | Unit-speed particles choose directions at collisions; this is not the one-way finite rooted-path kernel or its general interface-additive jump count. |

No primary source in this bounded screen states the same deterministic
rootward active-clock chain together with
`E[T_S]=sum_i h(s_{i-1},s_i)`. That is a bounded non-hit, not a novelty
certificate. The survivor remains `HOLD_EXTERNAL` until an independent
domain expert searches at the kernel and theorem levels.

## 7. P1--P126 collision ceiling

| Internal owner / firewall | Required subtraction |
|---|---|
| P90 Rule-184 particle dynamics | Fixed-length parallel traffic dynamics receive no credit. |
| P101 random cap/floor synchronization | Generic random scheduling and reset statistics receive no credit. |
| P114 rooted-forest leaf peeling | Rooted geometry, monotonicity, and peeling clocks receive no credit; `S02` must earn its asynchronous path law. |
| P117 and its historical exclusions | Word eroders and pointer doubling are fenced; `S03` is killed outright. |
| P121 adjacent `(x,y)->xy+1` coalescence | Adjacent deletion histories, random-BST/Yule splits, generic coalescence, and all owned downstream statistics receive zero credit. `S01` and `S25` do not survive this ceiling. |
| P126 balanced composition refinement | Part splitting, refinement clocks, restricted-composition counts, and fibre products receive no credit. |

For `S02`, the residual is narrow: a deterministic rootward path, active-pile
embedded clock, general-initial-state interface-additive mean, and its
adjacent pure-death evaluation. Shared coalescence terminology is not part of
the claim.

## 8. Final recommendation

- `S02`: **GO_INTERNAL** to the next proof/owner phase on the general
  interface theorem and exact PGF. The theorem proof route is complete enough
  to justify promotion, and all rooted subsets through `n=12` pass an
  independent exact equality check.
- `S01`, `S25`, `S26`: **KILL/STOP**. The first two hit owned PD laws; the
  third has no all-parameter residual. `S03` is killed by the pointer-doubling
  firewall; `S04`--`S24` remain killed for the recorded reasons.
- Overall: **one survivor, zero frozen systems, no paper number assigned**.
  External dissemination remains **`HOLD_EXTERNAL`** pending independent
  owner review. If the global sequence requires another candidate, activate
  a different reserve lane rather than weakening this gate.
