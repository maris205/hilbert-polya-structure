# Stochastic and local-rewrite breadth scout

**Audit date:** 2026-08-31  
**Scope:** Stage-1 scouting only; no paper number is assigned here  
**Literal systems:** 27  
**Internal recommendation:** one theorem-ready residual (`R02`) and one repair reserve (`Q03`)  
**External recommendation:** `R02` remains `HOLD_EXTERNAL`; the literal model and its standard sector theory have a direct owner

## 1. Exact executable contract

[`verify_stochastic_scout.py`](verify_stochastic_scout.py) exhaustively runs 27
different kernels spanning finite-word rewrites, permutation deletion and
sorting, tree/DAG erosion, random greedy graph processes, directed queues and
piles, coalescence, and classical finite Markov controls. It uses Python
integers and `fractions.Fraction` only. There is no floating point, sampling,
third-party package, network access, or timestamp in the computation.

The frozen output is [`CANONICAL.txt`](CANONICAL.txt). Reproduce it with

```bash
cd docs/papers132_136_sequence/scouting/stochastic
PYTHONDONTWRITEBYTECODE=1 python3 verify_stochastic_scout.py > /tmp/stochastic-scout.txt
cmp -s /tmp/stochastic-scout.txt CANONICAL.txt
```

The canonical run covers **1,804,440 enumerated or dynamic-programming states**
and executes **6,142,681 exact assertions**, of which 6,142,677 are attributed
to individual systems and four audit the global ledger. A finite check is
falsification evidence, not a proof and not a novelty claim.

For acyclic nondeterministic rewrites, the executable enumerates every legal
successor and checks terminal sets, possible path lengths, history counts, or
the exact law under uniform choice among active events, as appropriate. A
row's “states” may therefore count literal inputs or memoized states; it never
means a random sample.

## 2. Permanent 27-system ledger

| ID | State, literal update, and audited statistic | Exact range; states | Signal and disposition |
|---|---|---:|---|
| `R01` | Binary line; rewrite any `100 -> 011`. Audit Fibonacci value, terminal, depth, image size, and terminal fibres. | lengths 1--14; 32,766 | Confluent with a sharp clock and extremal fibres, but Fibonacci-normalization and maximal-representation owners eat the core. **`KILL_OWNER_FIBONACCI_REPRESENTATIONS`.** |
| `R02` | Binary open line; for fixed `k>=2`, rewrite any `1^k 0 -> 0 1^k`. Audit the terminal projection, per-zero odometer, inversion clock, every terminal fibre, and its depth polynomial. | all words: `k=2`, lengths 1--16; `k=3,4`, lengths 1--13; 163,834 | Every target fibre has an exact Gaussian-binomial depth enumerator. Literal dimer/k-mer physics and sector theory are zero credit; only the open-boundary residual is retained. **`PROMOTE_INTERNAL_OWNER_HOLD`.** |
| `R03` | Binary words; contract `010 -> 0`. Audit normal form and all path lengths. | lengths 0--16; 131,071 | Unique irreducible and fixed clock, maximum 7; standard terminating string reduction. **Kill.** |
| `R04` | Ternary words; contract any equal pair `aa -> a`. Audit terminal, clock, histories. | lengths 0--9; 29,524 | Exact run compression and clock `n-number_of_runs`; free-idempotent normal form. **Kill.** |
| `R05` | Binary words; delete both letters of any unequal pair. Audit signed-count terminal and clock. | lengths 0--18; 524,287 | Unique all-zero/all-one normal form and `min(#0,#1)` clock; free-group cancellation. **Kill.** |
| `R06` | Binary cycle; flip an isolated bit whose two neighbours agree. Audit all absorbing states and the exact uniform-active law. | lengths 3--12; 8,184 | 4,894 sources are nonconfluent, with at most 29 terminals; zero-temperature one-dimensional Glauber mechanism. **Kill.** |
| `R07` | Ternary line; rewrite `012 -> 210`. Audit confluence and inversion change. | lengths 0--9; 29,524 | Orthogonal rewrite; inversion rises by three per event, maximum depth 6. The proof is immediate. **Kill.** |
| `R08` | Binary line; rewrite `010 -> 101`. Audit terminal and path-length sets. | lengths 1--12; 8,190 | 3,106 sources have multiple normal forms and 2,242 have variable clocks; at most nine terminals. **Kill nonconfluent.** |
| `R09` | Binary cycle; in any cyclic `111`, replace the middle bit by zero. Audit absorbing laws and clocks. | lengths 3--12; 8,184 | Absorbing distance-two hard-core sets, as many as 29 outcomes; random-sequential-adsorption core. **Kill.** |
| `P01` | Permutation line; delete any strict local maximum (an endpoint is compared with its sole neighbour). Audit terminal, histories, and uniform-active history law. | sizes 1--8; 46,233 | Min-Cartesian-tree leaf pruning and the forest hook formula, maximum 210 histories. Classical and collides with P114/P121 machinery. **Kill.** |
| `P02` | Permutation; swap any adjacent descent. Audit sorted terminal, inversion clock, and history recursion. | sizes 1--9; 409,113 | Bubble-sort/0-Hecke/Coxeter reduced-word engine; maximum history count 29,258,366,996,258,488,320. **Kill.** |
| `P03` | Permutation; delete the left, larger entry of any adjacent descent. | sizes 1--8; 46,233 | Terminal is exactly the right-to-left-minimum subsequence; maximum 5,040 histories. **Kill monotone-stack normal form.** |
| `P04` | Permutation; choose any adjacent pair and delete its smaller entry. | sizes 1--8; 46,233 | Global maximum is the unique survivor and every clock is `n-1`. **Kill theorem-thin tournament erosion.** |
| `P05` | Permutation; delete any entry that is not a left record. | sizes 1--8; 46,233 | Terminal is the left-record subsequence; if `d` entries disappear there are `d!` schedules. **Kill classical record theory.** |
| `P06` | Permutation; transpose a uniformly chosen unordered pair of positions. Audit connectivity, reversibility, and parity. | `S_n`, `n=2..7`; 5,912 | Irreducible symmetric graph, uniform stationary measure, period two. **Kill classical random-transposition chain.** |
| `G01` | Labelled tree rooted at zero; repeatedly delete any nonroot leaf. Audit deletion histories. | all Prüfer trees `n=2..6`; 16,028 | `(n-1)!/product_{v != root}|T_v|`; classical tree hook formula and literal `P01` conjugate. **Kill.** |
| `G02` | Naturally ordered DAG; repeatedly delete a current source. Audit all histories against brute-force orders. | all such DAGs `n=1..5`; 11,537 | Histories are exactly topological orders/linear extensions for 1,099 DAGs. **Kill classical.** |
| `G03` | Full path; choose a remaining vertex uniformly, accept it, and delete its closed neighbourhood. Audit the complete selected-set law. | `P_n`, `n=1..15`; 2,329 | Exact maximal-independent-set laws; final mean `618626159/91216125`. Random greedy/RSA owner. **Kill.** |
| `G04` | Full cycle edge set; choose an available edge uniformly, accept it, and delete it and its two adjacent edges. | `C_n`, `n=3..14`; 1,417 | Exact greedy-matching laws; final mean `188752/31185`. **Kill random-greedy matching.** |
| `G05` | One infected site on a cycle; choose an infected/uninfected boundary edge uniformly and infect its other endpoint. Audit cover clock and last-site law. | `C_n`, `n=3..17`; 1,645 | Deterministic `n-1` clock and reflection-symmetric last-site law. One-dimensional Eden/Richardson specialization. **Kill.** |
| `Q01` | Nonnegative composition; move one token from any positive nonlast coordinate one step right. | totals at most 10, lengths 2--6; 12,364 | Unique all-at-sink terminal and weighted-distance clock, maximum 50. **Kill independent directed transport.** |
| `Q02` | Digits; if `x_i >= 3`, replace `(x_i,x_{i+1})` by `(x_i-3,x_{i+1}+1)`. | digits 0--6, lengths 2--6; 137,249 | Unique base-three stabilization and scheduler-independent odometer. **Kill abelian carrying.** |
| `Q03` | Nonnegative composition; whenever `x_i >= x_{i+1}+2`, move one unit from `i` to `i+1`. | totals at most 15, lengths 2--6; 74,596 | Confluent terminal, fixed odometer, maximum depth 20, 6,356 observed terminals. Generic abelianness is owned; retain only as a repair reserve. **`RESERVE_ABELLANESS_GATE`.** |
| `Q04` | Nonnegative piles; when adjacent piles are both positive, subtract one from each. Audit exact absorbing law. | heights 0--2, lengths 2--7; 3,276 | 1,940 sources are nonconfluent, with at most 13 terminals; stochastic matching erosion. **Kill.** |
| `M01` | Set partition from singletons; choose an unordered block pair uniformly and merge. | starts `n=1..8`; 6,838 | Kingman pair-merge clock and product of merger choices. **Kill classical coalescent.** |
| `M02` | Ehrenfest urn; choose a ball uniformly and switch its urn. | `n=1..40`; 860 | Exact binomial reversible law and parity-two period. **Kill classical control.** |
| `M03` | Neutral Moran count chain; choose reproducer and death individual uniformly. | populations `n=2..40`; 780 | Fixation probability `i/n` and exact rational Bellman absorption means. **Kill classical control.** |

Per-system assertion ledger (in the same order as the table):

```text
R01 286766   R02 976143   R03 393213   R04 88572    R05 1572861
R06 55262    R07 88572    R08 8191     R09 24552    P01 277398
P02 818226   P03 92466    P04 138699   P05 138699   P06 236014
G01 16028    G02 11537    G03 537      G04 214      G05 60
Q01 24728    Q02 548996   Q03 328536   Q04 13104    M01 24
M02 900      M03 2379
```

The breadth requirement is met literally, not by relabelling one parameter
family. The `k=2,3,4` instances are validation points for the single `R02`
all-`k` theorem contract and are not counted as extra systems. The ledger
deliberately keeps negative results so later rounds do not rediscover a
standard scheduler behind a new carrier.

## 3. `R02`: frozen open-boundary `k`-mer residual

### 3.1 Zero-credit owner boundary

Barma, Grynberg, and Stinchcombe study the same binary dimer update
`110 -> 011` in “Directed diffusion of reconstituting dimers,” *Journal of
Physics: Condensed Matter* 19 (2007), 065112,
[arXiv:cond-mat/0609041](https://arxiv.org/abs/cond-mat/0609041),
[DOI 10.1088/0953-8984/19/6/065112](https://doi.org/10.1088/0953-8984/19/6/065112).
Their periodic binary model, deletion-defined irreducible string,
`A=11,B=10,C=0` sector encoding, and ASEP interpretation are direct ownership,
not merely nearby work. The broader driven `k`-mer physical family is also
treated as owned background unless a specialist gate proves otherwise.
Accordingly this scout assigns **zero contribution** to

- the literal dimer rule or its all-`k` extension `1^k 0 -> 0 1^k`;
- the name “reconstituting dimers/`k`-mers”;
- irreducible-string sector conservation;
- periodic-ring stochastic physics and ASEP reductions; and
- generic scheduler independence, carrying, or abelian-network language.

The possible residual is narrower: orient the rule on a finite **open line**,
run it to absorption, and determine for every `k>=2` the complete terminal
projection, scheduler-independent odometer, and every target fibre refined by
depth. The bounded primary-source audit did not locate this conjunction in the
literal owner paper. A non-hit is not novelty or priority evidence, so the
external status remains `HOLD_EXTERNAL`.

### 3.2 State, carry recursion, and exact projection

Fix `k>=2`. Let a binary word with `z` zeros have its unique gap encoding

$$
w=1^{g_0}0\,1^{g_1}0\cdots 0\,1^{g_z},\qquad g_i\geq0.
$$

A firing immediately before zero `i` transfers `k` ones from gap `i` to gap
`i+1`. For `0<=i<z`, put

$$
b_i=\left\lfloor\frac{g_i}{k}\right\rfloor,
\qquad r_i=g_i\bmod k,
\qquad c_{-1}=0,
\qquad c_i=c_{i-1}+b_i=\sum_{j=0}^{i}b_j.                              \tag{R02.1}
$$

Incoming traffic adds exactly `k c_{i-1}` ones to gap `i`; hence `c_i` is the
number of times the `i`-th zero fires. The frozen terminal projection is

$$
\operatorname{gaps}(Q_k(w))=
\left(r_0,\ldots,r_{z-1},
g_z+k\sum_{i=0}^{z-1}b_i\right).                                      \tag{R02.2}
$$

Thus the internal terminal gaps are precisely the residues in
`{0,...,k-1}`, while the last gap absorbs every complete `k`-block. Every
legal schedule has depth

$$
D_k(w)=\sum_{i=0}^{z-1}c_i
=\sum_{i=0}^{z-1}(z-i)b_i.                                             \tag{R02.3}
$$

If `Inv(w)` counts pairs consisting of a one to the left of a zero, each
rewrite lowers it by exactly `k`, independently certifying

$$
D_k(w)=\frac{\operatorname{Inv}(w)-
\operatorname{Inv}(Q_k(w))}{k}.                                       \tag{R02.4}
$$

### 3.3 Every-target fibre and Gaussian depth law

Fix an absorbing target with gaps

$$
t=(r_0,\ldots,r_{z-1},\beta),
\qquad 0\leq r_i<k,
\qquad \beta\geq0,
$$

and let `B=floor(beta/k)`. Its preimages are in bijection with

$$
(b_0,\ldots,b_{z-1})\in\mathbb Z_{\geq0}^{z},
\qquad \sum_i b_i\leq B,                                               \tag{R02.5}
$$

through the explicit inverse gaps

$$
g_i=r_i+kb_i\quad(i<z),
\qquad
g_z=\beta-k\sum_i b_i.                                                 \tag{R02.6}
$$

Consequently every target, not merely a maximal or generic target, obeys

$$
|Q_k^{-1}(t)|=\binom{B+z}{z},                                          \tag{R02.7}
$$

and its full depth enumerator is

$$
\sum_{Q_k(w)=t}q^{D_k(w)}
=\sum_{\substack{b_i\geq0\\\sum b_i\leq B}}
q^{\sum_{i=0}^{z-1}(z-i)b_i}
=\begin{bmatrix}B+z\\z\end{bmatrix}_q.                              \tag{R02.8}
$$

At `q=1`, (R02.8) recovers (R02.7). The executable checks
(R02.1)--(R02.4) for every binary word through length 16 at `k=2` and through
length 13 at `k=3,4`. It checks (R02.7)--(R02.8) separately for every
absorbing target in those ranges. This is 163,834 literal inputs and 976,143
exact assertions. The largest observed depths are 32, 14, and 10 for
`k=2,3,4`, respectively, and the largest observed fibre has size 495. No
counterexample occurs in the stated ranges.

### 3.4 Proof routes

Two independent short routes are available.

1. **Directed-gap odometer.** The `i`-th zero receives `k` ones for every
   upstream firing, so it fires `c_i=b_i+c_{i-1}` times regardless of order.
   Induction over the labelled zeros proves (R02.2)--(R02.3). The explicit
   inverse parametrization proves (R02.5)--(R02.7), and the last sum in
   (R02.8) is the partition generating function for a `z` by `B` rectangle.
2. **Potential plus commutation.** `Inv` decreases by `k` at every step and
   bounds all trajectories. Firings at distinct labelled zeros commute in gap
   coordinates, and the upstream-to-downstream recurrence fixes their counts.
   This proves termination and schedule independence separately from the
   fibre bijection.

Bond and Levine's “Abelian Networks I. Foundations and Examples,” *SIAM
Journal on Discrete Mathematics* 30 (2016),
[DOI 10.1137/15M1030984](https://doi.org/10.1137/15M1030984), owns the general
abelian-network and least-action framework. That framework is background; the
residual value, if priority survives, must be the explicit all-`k` open-line
projection together with the every-target Gaussian fibre law.

### 3.5 Internal noncollision firewall

| Occupied internal material | Zero-credit overlap | Residual distinction required for `R02` |
|---|---|---|
| P63 rank-one XOR inverse windows | Fixed-length binary words and local symbolic encodings. | P63 is a linear `GF(2)` factor/inverse-radius problem on a rank-one subshift. `R02` is a terminating nonlinear open-line rewrite preserving zero count and each internal gap modulo `k`; no XOR factor, inverse window, or subshift claim is used. |
| P82 shifted Fredkin and P90 Rule 184 | Conservative binary local dynamics and traffic vocabulary. | Rule 184 synchronously moves singleton traffic patterns (`10 -> 01` in its particle reading) on a ring. `R02` asynchronously moves an assisted `k`-block to an open absorbing projection. Fredkin reversibility/frozen-SFT machinery is absent. |
| P114 rooted-forest peeling | Termination, rank, and endpoint language. | `R02` neither changes a tree nor deletes letters; its invariant is the labelled-zero gap odometer and every-target word fibre. |
| P117 odd-run cyclic reversal | Binary runs, parity, and transient/recurrent questions. | P117 is a synchronous cyclic run map with recurrent one/two-cycles. `R02` is an acyclic open-line rewrite; run residues alone receive no credit. |
| P121 adjacent product-plus-one coalescence | Uniform-active histories, adjacent interaction, and Yule/BST carriers. | P121 decreases block count and coalesces values. `R02` preserves word length and particle/zero counts and has a deterministic terminal/odometer for every scheduler. |
| P126 balanced composition refinement | Integer-composition carriers, pointwise fibres, and all-target formulas. | Encoding by gaps is only a coordinate change. P126 synchronously expands each part and changes composition length; `R02` transports `k`-blocks between a fixed number of gaps asynchronously. The noncollision invariant is fixed zero count plus the terminal residue vector modulo `k`. |
| P129 rootward active-pile coalescence | Directed transport, absorption, and stochastic scheduling. | P129 shrinks occupied support by coalescence and studies a genuinely random absorption time. `R02` preserves word length and its complete odometer is deterministic; its residual statistic is a projection fibre polynomial. |
| Earlier one-defect abelian queues | Scheduler independence and directed carrying. | No defect is present. Generic abelianness is zero credit; the retained output is the full all-`k` projection and every-target `q`-fibre. |

This firewall is a nonconjugacy audit, not evidence that the residual is
externally new.

## 4. Owner-killed strong signals

### 4.1 `R01`: Fibonacci rewrite `100 -> 011`

With Fibonacci weights read from right to left, `R01` preserves value, raises
the number of ones by one, terminates, and is locally confluent because the
left-hand side has no self-overlap. Exact enumeration through length 14 also
finds

$$
|\operatorname{im}Q_n|=F_{n+3}-1,
\qquad
\max_w D(w)=\left\lfloor\frac{n-1}{2}\right\rfloor,
$$

and the conjectural sharp maximum fibre

$$
\max_t|Q_n^{-1}(t)|=
\begin{cases}
1,&n\leq2,\\
F_{(n+3)/2},&n\geq3\text{ odd},\\
2F_{n/2},&n\geq4\text{ even}.
\end{cases}
$$

These are good exact signals but not an available paper core. Frougny's
primary normalization work—“Representation of numbers in nonclassical
numeration systems,” *Proceedings of ARITH-10* (1991),
[DOI 10.1109/ARITH.1991.145528](https://doi.org/10.1109/ARITH.1991.145528),
and “Representations of numbers and finite automata,” *Mathematical Systems
Theory* 25 (1992),
[DOI 10.1007/BF01368783](https://doi.org/10.1007/BF01368783)—owns finite-state
Fibonacci normalization. Kocábová, Masáková, and Pelantová directly study
integers with maximal numbers of Fibonacci representations in *RAIRO —
Theoretical Informatics and Applications* 39 (2005),
[DOI 10.1051/ita:2005022](https://doi.org/10.1051/ita:2005022).

The finite orientation supplies an elementary confluence proof, but after
subtracting normalization and maximal-representation enumeration it is not
theorem-dense enough. Final disposition:
`KILL_OWNER_FIBONACCI_REPRESENTATIONS`. It must not receive a paper number.

### 4.2 `P01`: local-maximum deletion

The min-Cartesian tree of a permutation turns current local maxima into
deletable nonroot leaves. If `T_v` is the subtree at `v`, the exact number of
deletion histories is

$$
\frac{(n-1)!}{\prod_{v\ne\mathrm{root}}|T_v|}.
$$

Vuillemin's “A Unifying Look at Data Structures,” *Communications of the ACM*
23 (1980), [DOI 10.1145/358841.358852](https://doi.org/10.1145/358841.358852),
is the direct Cartesian-tree source. Björner and Wachs' “q-Hook length
formulas for forests,” *Journal of Combinatorial Theory, Series A* 52 (1989),
[DOI 10.1016/0097-3165(89)90028-9](https://doi.org/10.1016/0097-3165(89)90028-9),
owns the stronger forest-hook framework. Internally the same proof silhouette
also hits P114 leaf peeling and P121's Cartesian-tree/Yule machinery. Final
disposition: `KILL_CLASSICAL_AND_INTERNAL_CARTESIAN_TREE`.

The three strongest literal signals therefore received direct primary-owner
gates: `R02` survives only after severe subtraction, while `R01` and `P01` are
killed. Clean formulas were not allowed to substitute for novelty.

## 5. `Q03`: theorem-shaped repair reserve

For `x=(x_0,...,x_{n-1})`, fire bond `i` when
`x_i >= x_{i+1}+2`, sending one unit right. Termination follows because
`sum (i+1)x_i` rises by one and is bounded. Disjoint moves commute; if both
adjacent bonds are legal, either order remains legal and gives the same state.
Newman's lemma therefore yields a unique terminal, characterized by

$$
x_i\leq x_{i+1}+1\qquad(0\leq i<n-1),
$$

and the terminal fixes the total number of firings through the weighted
moment. The executable confirms this for every composition of total at most
15 and length at most six.

There is a plausible stronger normal form. Put `z_i=x_i+i` and
`S_j=sum_{i<j}z_i`. A firing lowers only `S_{i+1}` by one, and stability is
discrete convexity of `S`. The expected closed statement is that the terminal
prefix path is the greatest integer convex minorant of the initial prefix
path with fixed endpoints. A least-action comparison gives a short proof
route: any stable minorant below the current path remains below it after a
legal lowering. This statement is **not frozen by the current verifier** and
must be added as an independent exact assertion before use.

Generic confluence, abelianness, stabilization, and least action are already
covered by the Bond--Levine framework cited above. `Q03` may advance only if a
second output is proved, preferably an explicit all-target fibre criterion or
generating function derived from the convex-minorant description. Thus its
honest status is `RESERVE_ABELLANESS_GATE`, not a paper-ready promotion.

## 6. Devil's-advocate audit

- `R02` is not a new system. The exact dimer rule and its standard periodic
  sector theory are directly owned by Barma--Grynberg--Stinchcombe; broader
  physical `k`-mer language also receives zero credit.
- A gap vector is an encoding, not a contribution. Directed transport and
  abelian stabilization are standard; without (R02.7)--(R02.8), the residual
  collapses.
- The `q`-binomial itself is classical. Any contribution must be phrased as
  its occurrence as the complete depth enumerator of **every open-boundary
  terminal fibre for all `k>=2`**, not as invention of a Gaussian polynomial.
- Exact checks at `k=2,3,4` and bounded lengths cannot establish priority or
  all-size truth. The two proof routes above are mandatory before manuscript
  use.
- `Q03` currently has only an elementary confluence theorem. It is reserve
  material until the convex-minorant and fibre layers are proved and owner
  audited.
- `R01` and `P01` are killed despite clean formulas. They are not fallback
  fillers if another lane fails.

## 7. Handoff ranking

Only two systems survive the theorem-shape screen; only one is ready for a
paper-selection gate.

1. **`R02` — proceed internally, hold externally.** Freeze the all-`k`
   open-boundary projection (R02.1)--(R02.2), odometer
   (R02.3)--(R02.4), explicit inverse fibre (R02.5)--(R02.7), and every-target
   Gaussian depth polynomial (R02.8). Subtract the literal dimer/`k`-mer
   model, irreducible string, periodic physics, ASEP, generic abelianness, and
   the classical `q`-binomial identity.
2. **`Q03` — reserve after repair.** First freeze and independently verify the
   greatest-integer-convex-minorant normal form; then require a nontrivial
   all-target fibre or depth formula. Kill if this reduces to generic abelian
   stabilization.

`R01` is the strongest discarded signal, but its direct Fibonacci owners make
the correct decision an owner-kill. No third finalist is manufactured to fill
a quota.
