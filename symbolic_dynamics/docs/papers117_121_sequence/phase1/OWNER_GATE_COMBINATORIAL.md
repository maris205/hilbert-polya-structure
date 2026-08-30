# Phase 3 hostile owner gate: combinatorial lane

**Audit date:** 2026-08-30  
**Status:** `HOLD_EXTERNAL`  
**Scope:** R2, C02, C03, and C01 only. This is an independent owner/novelty
gate, not a proof audit and not a novelty certificate.

## Gate method and interpretation

I reconstructed each literal map and a small claim package before searching.
The search then used several formulations of the update: exact English,
algebraic or run-length form, the name of the carrier object, and the nearest
standard mechanism. Searches were repeated with `iteration`, `dynamics`,
`functional graph`, `period`, `transient`, `synchronous`, and 2025--2026
filters where meaningful. Direct-neighbour papers were read far enough to
compare the actual update and scheduler, not merely their titles.

The score is hostile residual value on a ten-point triage scale, after giving
zero credit to owned definitions and standard consequences. It is not a
probability of novelty. A bounded non-hit means only that the stated queries
and direct neighbours did not expose an exact owner by the audit date.

| candidate | closest occupied mechanism | residual score | gate | hard action |
|---|---|---:|---|---|
| R2 odd-run reversal | shrinking CA / static binary-run enumeration | **8.1/10** | **PROCEED** | promote, conditional on general proofs of both sharp depth formulas |
| C02 synchronous open-neighbourhood mex | exact Grundy mex correction under a serial daemon | **6.7/10** | **CAUTION** | promote only if the part-size-sensitive fibre/basin theorem is completed |
| C03 first-CFL-factor rotation | Duval least circular shift; a 2025 rotate-first-factor Nyldon procedure | **2.8/10** | **ABANDON** | kill the present claim package; reconsider only with a nontrivial full layer/fibre law |
| C01 odd-degree synchronous local complement | the level-1 generalized-local-complement edge kernel | **4.4/10** | **CAUTION** | keep as a spike only; kill unless an intrinsic infinite period family is proved |

The ranking is therefore **R2 > C02 > C01 > C03**. Only R2 presently clears
the owner gate without needing a new theorem of a different order of
difficulty.

## R2 — odd-run reversal on labelled binary cycles

### Literal map and extracted claims

The phase space is the set of labelled cyclic binary words of length $n$.
In one parallel round, flip every bit in every cyclic run of odd length.
The proposed package contains five claims.

1. Every orbit has eventual period at most two.
2. A word is recurrent if and only if all of its cyclic run lengths have the
   same parity.
3. For odd $n$, only the two constant words recur. For $n=2m$, the fixed
   count is $2^{m+1}-2$, and the 2-cycle count has an explicit
   odd-composition formula.
4. The maximum preperiod is $(n-1)/2$ for odd $n$, and
   $\lfloor(n-2)/4\rfloor$ for even $n$.
5. A run-boundary/coalescent representation proves the recurrence census and
   supplies sharp witnesses for both transient bounds.

Claims 1--4 are the proposed mathematical delta. Exhaustion through $n=16$
is evidence only; it cannot replace a general proof, especially for the even
maximum in Claim 4.

### Closest primary owners and subtraction

| source | what it owns | what it does not own here |
|---|---|---|
| Rosenfeld, Wu, and Dubitzki, [*Fast language acceptance by shrinking cellular automata*](<https://doi.org/10.1016/0020-0255(83)90045-2>) (1983) | the shrinking-cell model: cells disappear and the surviving neighbours become adjacent | this particular cyclic parity rule, its recurrent set, its census, or its sharp finite transient |
| Modanese and Worsch, [*Shrinking and Expanding Cellular Automata*](https://doi.org/10.1007/978-3-319-39300-1_13) (2016), and Kutrib, Malcher, and Wendlandt, [*Shrinking one-way cellular automata*](https://doi.org/10.1007/s11047-016-9588-8) (2017) | later formal models and complexity theory for shrinking automata | the exact odd-run temporal classification |
| Balado and Silvestre, [*Systematic Enumeration of Fundamental Quantities Involving Runs in Binary Strings*](https://arxiv.org/abs/2602.10005) (2026) | static run/composition enumeration, including joint zero/one-run statistics | iteration of odd-run reversal |

The nearest-mechanism comparison becomes transparent on run boundaries. If
successive boundaries are $b_i,b_{i+1}\in\mathbb Z/n\mathbb Z$, then their
gap parity is the parity of $b_{i+1}-b_i$. After one update, a boundary
survives exactly when its two incident run lengths have the same parity. Thus
the proof engine is a deterministic deletion/coalescence process on boundary
data. This is an inference from the literal rule, and it places the work next
to shrinking automata; it does not identify the map with any cited SCA rule.

All general facts about binary runs, compositions, shrinking automata, and
fixed-radius cellular automata receive zero credit. Internally, P80's Boolean
majority dynamics, P90's cellular-automaton material, and P100's word erosion
also receive zero credit. The residual delta is the **exact conjunction** of
the parity-boundary rule, period-$\le2$ classification, recurrent census, and
parity-dependent sharp transient.

### Search boundary

Representative formulations included `flip every bit in an odd-length run`,
`odd run reversal binary cyclic word`, `run parity cellular automaton`,
`run-length encoded block automaton odd`, `equal-parity boundary deletion`,
`coalescing run boundaries`, and the same queries with `period`, `transient`,
`functional graph`, `2025`, and `2026`. I also followed the SCA references
above and recent static run-enumeration references. No exact temporal owner
was located in this bounded search.

### Residual delta, objection, and verdict

**Residual delta.** Almost the whole proposed temporal package survives owner
subtraction. It is unusually coherent: one boundary process could support
classification, enumeration, and two genuinely sharp clocks.

**Strongest hostile objection.** Once written in run-boundary coordinates,
the map may look like a short exercise in parity deletion rather than a new
dynamical mechanism. More seriously, the attractive even-depth formula is
currently vulnerable to being an $n\le16$ pattern. A paper that treats the
enumeration as proof fails immediately.

**Verdict: PROCEED (8.1/10).** Promote R2 to a proof gate. Require a complete
infinite-family proof of both transient maxima, a derivation of the 2-cycle
composition sum, and an explicit statement that shrinking-CA and static-run
theory are zero-credit background. Kill if the even bound cannot be proved
from the coalescent invariant or if an exact named block rule with the same
temporal census is subsequently found.

## C02 — synchronous open-neighbourhood mex

### Literal map and extracted claims

For a graph $G$ of maximum degree $\Delta$, the phase space is
$\{0,\ldots,\Delta\}^{V(G)}$, and

\[
F_G(c)(v)=\operatorname{mex}\{c(u):uv\in E(G)\}.
\]

On $K_{a_1,\ldots,a_k}$, one round makes each part monochromatic and induces

\[
T_k(x)_i=\operatorname{mex}\{x_j:j\ne i\}.
\]

The proposed package contains five claims.

1. The graph map collapses to the $k$-coordinate quotient in one round,
   and one quotient round puts all coordinates in $\{0,\ldots,k-1\}$.
2. The fixed points of $T_k$ are exactly the $k!$ permutations of
   $0,\ldots,k-1$.
3. Every other recurrent orbit is a classified 2-cycle: for
   $0\le m\le k-2$, place $0,\ldots,m-1$ injectively and fill the remaining
   coordinates by $m$, alternating with $m+1$. Hence
   $b_k=k!\sum_{j=2}^k1/j!$.
4. Quotient preperiod is at most two, original-colouring preperiod at most
   three, and the quotient zeta function is
   $(1-z)^{-k!}(1-z^2)^{-b_k}$.
5. The original graph map has explicit one-step fibres and basin sizes that
   depend on the full vector $(a_1,\ldots,a_k)$.

Claims 1--4 have a direct support/multiplicity proof in prospect. Claim 5 is
still a required inclusion--exclusion theorem, not an established part of
the package.

### Closest primary owners and subtraction

The decisive source is Hedetniemi, Jacobs, and Srimani,
[*Linear time self-stabilizing colorings*](<https://doi.org/10.1016/S0020-0190(03)00299-0>)
(2003). Their Algorithm 2.1 uses the same local value, shifted from colours
$\{0,1,\ldots\}$ to $\{1,2,\ldots\}$: a privileged vertex replaces its colour
by the least positive integer absent from its open neighbourhood. The paper
explicitly assumes a serial model in which a central daemon chooses one
privileged vertex at a time, and proves convergence in at most $n+2m$
moves to a Grundy colouring. It therefore directly owns the local mex
correction, its fixed-point interpretation, and asynchronous stabilization.
It does **not** study the unconditional Jacobi update of every vertex, its
2-cycles, or the complete-multipartite quotient functional graph.

[Firoz, Zalewski, and Lumsdaine](https://doi.org/10.1109/PACT.2019.00040)
(2019) own further parallel/asynchronous Grundy-colouring algorithms, and
[Bossek et al.](https://doi.org/10.1007/s00453-021-00838-3) (2021) use Grundy
local search in dynamic graph colouring. Recent distributed
$(\Delta+1)$-colouring work, including the OPODIS 2025 proceedings paper by
[Fuchs and Kuhn](https://doi.org/10.4230/LIPIcs.OPODIS.2025.23), confirms
that synchronous neighbourhood-colour updates are a heavily occupied model
class. None of these sources located in this audit gives the displayed
$T_k$ census.

Consequently, mex/Grundy definitions, the characterization of fixed points
as Grundy colourings, and generic distributed convergence or colouring
complexity receive zero credit. Internally, P80's synchronous majority and
P106's graph polarity receive zero credit. The defensible residual is the
**unconditional synchronous scheduler**, the multipartite collapse, exact
2-cycle/depth law, and a genuinely $(a_i)$-sensitive fibre theorem.

### Search boundary

Queries included `synchronous mex graph colouring dynamics`, `parallel
Grundy recolouring cycles`, `simultaneous smallest available colour update`,
`complete multipartite Grundy colouring`, `mex operator complete
multipartite functional graph`, `Jacobi Grundy update period`, and 2025--2026
variants. I read the 2003 rule and scheduler, not just its abstract, and
checked recent locally iterative and Grundy-local-search neighbours. No
primary source for the exact synchronous complete-multipartite census was
located in this bounded search.

### Residual delta, objection, and verdict

**Residual delta.** The scheduler change is mathematically consequential:
the asynchronous owner converges, while the proposed simultaneous map has a
fully classifiable family of 2-cycles. The quotient census is clean and the
part sizes offer a possible second theorem through fibres.

**Strongest hostile objection.** A referee can accurately say that the paper
takes the exact 2003 Grundy correction rule, changes the daemon to a global
clock, and then solves a symmetry quotient. The fixed-point theorem is fully
owned, the zeta function is automatic after the cycle count, and the
$a_i$'s disappear after one round. Without a closed, parameter-sensitive
fibre/basin formula, the residual may be only an elegant exercise.

**Verdict: CAUTION (6.7/10).** Conditional promote. The paper-sized gate is
Claim 5 plus a proof that the depth-two quotient classification is exhaustive;
the abstract and title must lead with synchronous 2-cycles/fibres, not with a
new colouring algorithm. Kill if the fibre law collapses to an unilluminating
product or if a direct synchronous-mex census owner appears.

## C03 — first-CFL-factor rotation

### Literal map and extracted claims

For a nonempty word of length $n$ over an ordered $q$-letter alphabet,
write its nonincreasing Chen--Fox--Lyndon factorization as
$w=\ell_1\cdots\ell_r$, and set

\[
F(w)=\ell_2\cdots\ell_r\ell_1.
\]

The proposed package contains five claims.

1. The update stays in a necklace and strictly decreases lexicographically
   unless all CFL factors are equal.
2. Every word reaches the least conjugate; all periodic points are fixed and
   are precisely powers of Lyndon words.
3. The number of fixed words is the necklace number
   $N_q(n)=n^{-1}\sum_{d\mid n}\varphi(d)q^{n/d}$.
4. Every transient has length at most $n-1$, and the bound is sharp.
5. The words $a_1\ge\cdots\ge a_{n-1}>a_n$ form a deepest family of size
   $\binom{q+n-2}{n}$.

No full depth-layer recurrence or one-step-fibre law is currently proved.

### Closest primary owners and subtraction

Duval's [*Factorizing words over an ordered alphabet*](<https://doi.org/10.1016/0196-6774(83)90017-2>)
(1983) is not merely background to factorization: its stated applications
include least suffix and least circular shift. Thus CFL computation and the
canonical necklace endpoint are directly occupied. The modern scope remains
active: [Hendrian, Köppl, Yoshinaka, and Shinohara](https://doi.org/10.4230/LIPIcs.CPM.2024.18)
(CPM 2024) treat factorization and canonical rotation for Galois words while
explicitly recalling linear-time classical Lyndon detection, factorization,
and rotation.

A still closer mechanism neighbour is Fleischmann, Huch, and Nowotka,
[*Generalised Nyldon Words*](https://doi.org/10.1016/j.tcs.2025.115320)
(2025). Its factor-list algorithm includes a rotate-first-factor-to-the-end
step when producing the required generalized Nyldon ordering. It is not the
literal C03 self-map: the maintained factorization and order are different,
and it does not recompute the classical CFL factorization after each rotation.
It nevertheless makes a claim of conceptual novelty for “move the first
canonical factor to the end” untenable. Finally, Badkobeh, Bannai, I, and
Köppl, [*Bijective BWT Based Compression Schemes*](https://doi.org/10.1007/s00224-025-10235-w)
(version of record 2026), compute Lyndon factorizations across all cyclic
rotations. This does not own the iteration, but it occupies the exact local
landscape in which a functional-forest analysis would sit.

CFL uniqueness, least conjugates, necklace counts, powers of Lyndon words,
and efficient rotation algorithms receive zero credit. Internally, P100's
word erosion, P105's cyclic pruning, and P111's word cocycle receive zero
credit. After subtraction, only the chosen slow iteration, its round statistic,
and any nonstandard fibre/layer enumeration remain.

### Search boundary

Queries included `first Lyndon factor rotation`, `move first CFL factor to
end`, `iterated Duval rotation`, `Lyndon factorization dynamics`, `functional
graph least conjugate`, `round complexity minimum rotation`, `rotate first
Nyldon factor`, and 2025--2026 variants. Direct neighbours on Galois words,
generalized Nyldon words, BBWT, and all-rotation Lyndon factorization were
read. No exact paper on the displayed recompute-and-rotate functional forest
was located in this bounded search.

### Residual delta, objection, and verdict

**Residual delta.** The sharp $n-1$ clock and its deepest weakly decreasing
family appear not to be stated in the sources checked. That is a real but
narrow residual. A complete depth-layer or fibre recurrence could change the
assessment.

**Strongest hostile objection.** The current paper would look like an
artificial unit-cost unrolling of Duval's 1983 least-circular-shift machinery.
Its endpoint, roots, and root count are classical; strict descent is a short
Lyndon comparison; and the zeta function would be immediate from “all cycles
are fixed.” The 2025 Nyldon rotate-first-factor procedure makes the
mechanism-level adjacency visible even though it is not the same map.

**Verdict: ABANDON (2.8/10).** Kill the current five-claim package. Do not
promote merely because no exact functional-forest phrase was found. Re-entry
would require a genuinely nontrivial full depth distribution or fibre
recurrence, independently interesting beyond minimum-rotation correctness,
followed by a fresh owner gate.

## C01 — odd-degree synchronous local complement

### Literal map and extracted claims

For a labelled simple graph with adjacency matrix $A$ over $\mathbb F_2$,
let $d=A\mathbf 1$ and $D=\operatorname{diag}(d)$. Define, for $u\ne v$,

\[
A'_{uv}=A_{uv}+(ADA)_{uv},\qquad A'_{uu}=0.
\]

Equivalently, toggle $uv$ when $u,v$ have an odd number of common
neighbours of odd current degree. The proposed package contains five claims.

1. The degree-parity vector $d$, hence the odd-degree support $S(G)$, is
   invariant.
2. Eulerian graphs are fixed; more generally, $G$ is fixed exactly when
   every pair has an even number of common neighbours in $S(G)$.
3. Disjoint union factors the dynamics, so certified component periods yield
   least-common-multiple periods.
4. Exact small-order data give only fixed points through $n=4$, periods two
   by $n=5$, a specified period-four orbit at $n=7$, and sampled periods
   $3,12,36$ at larger orders.
5. The hoped-for paper theorem is a structural parity-sector decomposition
   and an intrinsic infinite family of nontrivial periods.

Claims 1--3 are elementary identities. Claim 4 is bounded evidence. Claim 5
is not yet a theorem.

### Closest primary owners and subtraction

Ordinary local complementation and LC equivalence are classical; for example,
Bouchet's [*Graphic presentations of isotropic systems*](<https://doi.org/10.1016/0095-8956(88)90055-X>)
(1988) and subsequent recognition theory own that foundation. More damaging
is the recent generalized operation in Claudet and Perdrix,
[*Local Equivalence of Stabilizer States: A Graphical Characterisation*](https://doi.org/10.4230/LIPIcs.STACS.2025.27)
and [*Deciding Local Unitary Equivalence of Graph States in Quasi-Polynomial
Time*](https://doi.org/10.4230/LIPIcs.ICALP.2025.59) (both 2025).

Their level-$r$ operation toggles an edge when the number of common
neighbours of its endpoints in a parameter multiset $S$ is
$2^{r-1}\bmod 2^r$. At level one, the **edge-toggle kernel** is therefore
exactly parity of common neighbours in $S$, which is the kernel in C01 after
putting $S=S(G)$. This is a formal formula-level collision that must be
credited directly.

There is also a precise difference. Generalized local complementation is
defined for a valid independent parameter multiset $S$; the odd-degree set
$S(G)$ need not be independent. C01 also selects $S$ intrinsically from
the current graph and recomputes it after every round. Hence the literal C01
map is not, in general, a valid generalized local complementation from those
papers. The residual is the adaptive policy $S=\operatorname{Odd}(G)$, the
proof that this policy freezes its own support, and the resulting temporal
structure—not the toggle formula.

All ordinary or generalized LC definitions, equivalence results, and common-
neighbour parity algebra receive zero credit. Internally, P80's Boolean graph
network, P103's matrix transformation, and P112's degree-driven tournament
update receive zero credit. Componentwise least-common-multiple amplification
alone is also too generic to count as the missing structural family.

### Search boundary

Queries included `simultaneous local complementation`, `parallel local
complementation graph`, `odd-degree vertices local complementation`, `odd
common neighbours toggle`, `A diag(A1) A graph transform`, `adaptive local
complementation dynamics`, `generalized local complementation iteration`, and
2025--2026 variants. I read the 2025 generalized-LC definition and its
validity hypotheses. No source for iteration with the intrinsic selector
$S(G)=\operatorname{Odd}(G)$ was located in this bounded search.

### Residual delta, objection, and verdict

**Residual delta.** The adaptive odd-degree selector is not cosmetic: it is
not generally an admissible independent generalized-LC support, yet its
parity is invariant under the update. This can create dynamics far beyond the
involutive valid operation. Periods $3,4,12,36$ are promising signals, but
all are finite witnesses; only the stated order-seven first-occurrence claim
comes with exhaustive lower-order coverage. None constitutes a general
classification.

**Strongest hostile objection.** After the 2025 generalized-LC formula gets
direct credit, the proposed “new operation” is only a state-dependent choice
of its support. The currently proved residual consists of one invariant, a
fixed-point test, product factorization, and finite examples. That is not yet
a paper. Manufacturing unbounded periods solely by disjoint unions of a few
base cycles would not repair the conceptual thinness.

**Verdict: CAUTION (4.4/10).** Do not freeze a paper slot. Retain C01 only as
a theorem spike with a hard gate: construct and prove an intrinsic connected
infinite family of nontrivial cycles or obtain a structural normal form for a
nontrivial parity sector. Kill if the only general period growth is disjoint-
union LCM, or if the adaptive update is found in LC/graph-state literature
under another name.

## Claim-credit and promote/kill ledger

| candidate | zero-credit core | defensible residual | present action |
|---|---|---|---|
| R2 | binary-run enumeration; shrinking-CA model; ordinary CA background | complete parity-boundary temporal census and sharp odd/even depth | **PROMOTE to proof gate** |
| C02 | mex/Grundy rule; Grundy fixed points; serial/asynchronous convergence; generic parallel colouring | simultaneous multipartite quotient cycles/depth plus full $(a_i)$-dependent fibres | **CONDITIONAL PROMOTE** |
| C03 | CFL factorization; least circular shift; necklace roots/counts; canonical rotation algorithms | only the artificial iteration's sharp clock and any future full layer/fibre law | **KILL current package** |
| C01 | ordinary/generalized LC; parity common-neighbour toggle kernel; product-LCM boilerplate | adaptive odd-degree selector and its genuinely structural temporal consequences | **RESERVE SPIKE; no slot** |

## Final owner-gate recommendation

1. Advance **R2** first. Its closest owners occupy the representation and
   static enumeration, not the exact temporal conjunction.
2. Advance **C02** only if the original-colouring fibre theorem is completed
   before drafting. The 2003 serial-daemon owner must be named prominently
   and receive exact rule-level credit.
3. Keep **C01** off the paper slate until it passes its connected-infinite-
   family or parity-normal-form gate. The 2025 generalized-LC collision is
   material, not a footnote.
4. **Abandon C03 in its current form.** A bounded phrase-level non-hit cannot
   overcome Duval ownership plus the 2025 rotate-first-factor neighbour and
   the present lack of a nontrivial forest theorem.

All four decisions remain `HOLD_EXTERNAL`. No bounded non-hit above is a
claim of novelty, priority, or freedom to publish.
