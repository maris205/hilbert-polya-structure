# P117–P121 combinatorial scout: twelve literal maps

**Status:** Phase-2 idea generation and cheap theorem pilots. No paper number
is assigned and no system is frozen. External status is HOLD_EXTERNAL.

**Scope:** exactly twelve literal self-maps are recorded below. They were
screened against P1–P116 and the Phase-1 owner landscape. A missing hit in a
bounded search is not a novelty claim. Classical local complementation,
Grundy colouring, Lyndon factorization, rotor routing, strong collapse,
chip-firing, source reversal, tree centroids, and solitaire results receive
zero credit.

## Ranked intake table

| ID | literal self-map | phase object | early signal | disposition |
|---|---|---|---|---|
| C01 | odd-degree synchronous local complement | labelled simple graphs | invariant parity sectors but periods 3, 4, 12, 36 occur | **PROMOTE** |
| C02 | synchronous open-neighbourhood mex | bounded vertex colourings of complete multipartite graphs | quotient depth at most two; classified fixed points and 2-cycles | **PROMOTE** |
| C03 | first-CFL-factor rotation | fixed-length words over an ordered alphabet | strict necklace descent; sharp depth \(n-1\) | **PROMOTE**, with owner gate |
| C04 | rotor-router on a bidirected lollipop | chip position and rotor configuration | possible articulation factorization of transient trees | **RESERVE** |
| C05 | rotor-guided local complementation | connected graph, chip, and cyclic rotor pointers | LC preserves the active neighbourhood, enabling a natural coupling | **RESERVE** |
| C06 | facet-nerve iteration | finite simplicial complexes up to isomorphism | direct strong-core owner is too close | **KILL** |
| C07 | delete all poset beat points simultaneously | finite \(T_0\) posets | the two-chain is sent to the empty poset | **KILL** |
| C08 | one-fire parallel chip-firing | fixed-mass configurations on a finite graph | period theory is directly occupied | **KILL** |
| C09 | simultaneous source-to-sink reversal | acyclic orientations of a fixed graph | the literal parallel iteration has a direct owner | **KILL** |
| C10 | heavy-component centroid walk | a fixed tree with a marked root | depth is only distance to the centroid set | **KILL** |
| C11 | Durfee-row solitaire | integer partitions of \(n\) | the clock collapses to \(n-\ell(\lambda)\) | **KILL** |
| C12 | Topswops prefix reversal | permutations of \([n]\) | famous direct temporal problem with no residual here | **KILL** |

The ranking is intentionally asymmetric: three maps have positive theorem
signals, two retain a credible but untested residual, and seven fail an owner,
safety, or theorem-thickness gate.

## C01. Odd-degree synchronous local complement

### Literal definition

- **Phase space:** all labelled simple graphs \(G\) on \([n]\).
- **Update:** write \(A=A(G)\) over \(\mathbb F_2\) and
  \(d_v=\deg_G(v)\bmod 2\). For each \(u\ne v\), set

  \[
  A'_{uv}=A_{uv}+\sum_{w=1}^n A_{uw}d_wA_{wv}\pmod 2,
  \qquad A'_{uu}=0.
  \]

  Thus \(\{u,v\}\) is toggled exactly when \(u,v\) have an odd number of
  common neighbours of odd current degree. This is simultaneous, not a
  sequential word of local complementations.
- **Parameter family:** \(n\ge0\), with invariant subfamilies indexed by the
  even-cardinality odd-degree set \(S(G)\).

### Early signal and falsified guesses

The degree-parity vector is invariant. For fixed \(u\), the parity of the
number of toggles incident with \(u\) is

\[
\sum_w A_{uw}d_w\sum_{v\ne u}A_{wv}
=\sum_w A_{uw}d_w(d_w+A_{uw})=0.
\]

Hence every Eulerian graph is fixed, the phase space splits into parity
sectors, and disjoint union factors the dynamics. A graph is fixed exactly
when every vertex pair has an even number of common odd-degree neighbours.

The exact census for \(n=0,\ldots,6\) gives maximum
\((\text{depth},\text{period})\)

\[
(0,1),(0,1),(0,1),(0,1),(2,1),(2,2),(3,2).
\]

The verified seven-vertex mask 1394850, with edges

\[
02,06,13,23,26,35,45,56,
\]

lies on a 4-cycle. Thus order seven is the first order at which a period
greater than two occurs. A deterministic order-eight sample gives a period-3
orbit, so the power-of-two guess also fails. Samples at orders eight through
ten reach periods \(12,12,36\). The map first fails to be an involution and
first changes the degree multiset at the four-vertex star.

### Owner subtraction and internal collision

Bouchet's local-complement/isotropic-system theory and all LC-equivalence or
principal-pivot results are background
([Bouchet 1988](https://doi.org/10.1016/0095-8956(88)90055-X),
[Bouchet 1993](https://doi.org/10.1016/0012-365X(93)90357-Y),
[Brijder--Hoogeboom](https://doi.org/10.1016/j.tcs.2012.02.031)).
A bounded search did not locate this state-dependent simultaneous polynomial
update; that is only permission for a deeper owner search. Internally, P80
owns a Boolean majority network, P103 a matrix transform, and P112 a
degree-driven tournament update. The residual must be the parity-sector
factorization and nontrivial period semigroup.

### Two proof routes

1. **Block-matrix route:** freeze \(S\), write
   \(A=\begin{psmallmatrix}B&C\\C^T&E\end{psmallmatrix}\), and analyze
   \(A\mapsto A+\operatorname{off}(ADA)\). Direct products then turn certified
   base cycles into least-common-multiple period constructions.
2. **Parity-walk route:** view a toggle as an odd count of marked length-two
   walks. Double counting proves the invariant; switching on the marked
   common-neighbour hypergraph can attack fixed points and cycle families.

### Kill condition

Kill if the exact update already has a direct owner, or if no infinite
structural period construction beyond disjoint unions survives. No global
period bound is promoted: the spike already destroyed two naive versions.

## C02. Synchronous open-neighbourhood mex

### Literal definition

- **Phase space:** for a graph \(G\) of maximum degree \(\Delta\), all
  colourings \(c:V(G)\to\{0,\ldots,\Delta\}\).
- **Update:**

  \[
  F_G(c)(v)=\operatorname{mex}\{c(u):uv\in E(G)\}.
  \]

  The empty neighbourhood has mex zero.
- **Parameter family:** complete multipartite graphs
  \(K_{a_1,\ldots,a_k}\), with \(k\ge1\) and all \(a_i\ge1\).

### Early exact signal

All vertices in one part have identical open neighbourhoods, so one round
makes every part monochromatic. On part colours the map is

\[
T_k(x)_i=\operatorname{mex}\{x_j:j\ne i\}.
\]

After one quotient step all coordinates lie in \(\{0,\ldots,k-1\}\). On this
quotient:

- fixed points are precisely the \(k!\) permutations of \(0,\ldots,k-1\);
- every nontrivial cycle has length two;
- for \(0\le m\le k-2\), choose \(m\) positions and bijectively place
  \(0,\ldots,m-1\) there; filling all remaining positions by \(m\),
  respectively \(m+1\), gives one 2-cycle, and these are all of them;
- every quotient state reaches the recurrent set in at most two rounds.

Thus

\[
b_k=\sum_{m=0}^{k-2}\frac{k!}{(k-m)!}
=k!\sum_{j=2}^{k}\frac1{j!},
\qquad
\zeta_{T_k}(z)=(1-z)^{-k!}(1-z^2)^{-b_k}.
\]

The original colouring becomes part-monochromatic after one round and has
total transient depth at most three. The smallest nonuniform 2-cycle is
\((0,1,1)\leftrightarrow(0,2,2)\), disproving the guess that every
nonpermutation flows to the uniform \(0/1\) cycle. The state \((0,0,1)\)
needs two quotient rounds, disproving an idempotent-after-one guess.

### Owner subtraction and internal collision

Mex/Grundy colouring and parallel colouring algorithms receive zero credit;
the nearest located primary algorithmic owner is
[Firoz--Zalewski--Lumsdaine](https://doi.org/10.1109/PACT.2019.00040).
The bounded search did not locate the exact synchronous census on complete
multipartite graphs. Internally P80 owns synchronous majority and P106 a
power-set graph polarity. The residual is the mex-specific part quotient,
recurrent classification, and fibre law.

### Two proof routes

1. **Support/multiplicity route:** let \(r\) be the least missing part colour.
   A coordinate below \(r\) survives exactly when unique; every other
   coordinate becomes \(r\). A second support reduction gives the canonical
   2-cycle and proves the depth bound.
2. **Species/fibre route:** treat singleton low colours as labelled atoms and
   the repeated colour as one marked block. Falling factorials enumerate
   cycles; inclusion--exclusion over colour sets in each original part counts
   one-step fibres and basin sizes as functions of \(a_1,\ldots,a_k\).

### Kill condition

Kill if a direct synchronous-mex owner is found, or if original-colouring
fibres do not yield a second parameter-sensitive theorem beyond the quotient.
Generic Grundy-colouring facts cannot be claimed.

## C03. First-CFL-factor rotation

### Literal definition

- **Phase space:** all nonempty words \(w\in\{0,\ldots,q-1\}^n\).
- **Update:** take the nonincreasing Chen--Fox--Lyndon factorization
  \(w=\ell_1\cdots\ell_r\) and set

  \[
  F(w)=\ell_2\cdots\ell_r\ell_1.
  \]

- **Parameter family:** alphabet size \(q\ge2\), length \(n\ge1\).

### Early exact signal

The update stays in the cyclic-conjugacy class. Unless all CFL factors are
equal, \(u>v\Rightarrow uv>vu\) gives \(F(w)<w\). Every word therefore reaches
the lexicographically least word in its necklace. Periodic points are exactly
the fixed words \(\ell^r\) with \(\ell\) Lyndon, counted by

\[
N_q(n)=\frac1n\sum_{d\mid n}\varphi(d)q^{n/d}.
\]

There are at most \(n\) distinct rotations, so depth is at most \(n-1\).
This is sharp: for \(n\ge2\), every word

\[
a_1\ge a_2\ge\cdots\ge a_{n-1}>a_n
\]

needs \(n-1\) rounds. There are \(\binom{q+n-2}{n}\) such deepest words.

Exhaustion for \(q=2,n\le12\) and \(q=3,n\le9\) found the sharp maximum at
every length. The path \(110\to101\to011\) shows that one factor rotation need
not reach the minimum. The word \(100\) reaches \(001\) in one round despite
three initial one-letter factors, so depth is not initial factor count minus
one. The word \(010\) reaches its minimum in one round although the minimum
begins two positions later, so depth is not the rotation index.

### Owner subtraction and internal collision

CFL factorization, Duval's algorithm, and least circular shift are zero-credit
background
([Duval 1983](https://doi.org/10.1016/0196-6774(83)90017-2)).
The bounded search did not find the iterated functional forest, sharp round
statistic, or fibre enumerator as a direct subject; algorithmic analyses
remain a high owner risk. Internally P100 erases digits, P105 prunes
permutation cycles, and P111 studies a word-area cocycle.

### Two proof routes

1. **Lyndon-comparison route:** group the initial run of equal largest
   factors and use \(uv>vu\) at the first smaller factor. This proves strict
   descent, fixed points, and the sharp weakly decreasing family.
2. **Necklace/suffix-array route:** work on each cyclic orbit. Every necklace
   is one rooted functional component; Burnside counts roots, while cyclic
   suffix ranks or a Duval-state automaton can attack depth layers and fibres.

### Kill condition

Kill if this repeated rotation is already a named least-conjugate algorithm
with round/fibre laws, or if no depth-layer or fibre recurrence is obtained.
Factorization and minimum-rotation correctness alone are owner material.

## C04. Rotor-router on a bidirected lollipop

### Literal definition

- **Phase space:** a chip position and one outgoing rotor at every vertex of
  \(L_{a,b}\), formed from \(C_a\) with a path of length \(b\) attached at one
  cycle vertex; replace each edge by both arcs and use the planar cyclic
  orders.
- **Update:** advance the rotor at the chip and move the chip along the new
  arc.
- **Parameter family:** \(a\ge3,b\ge1\).

### Early anomaly

The recurrent unicycle period is known. The only plausible residual is off
that locus: the articulation may split tail excursions from cycle rotations
and factor transient depth and predecessor trees. No independent finite
spike was run, so this is reserve only.

### Owner subtraction and internal collision

Unicycles, Euler tours, recurrent states, and Picard-group orbits are zero
credit
([Holroyd et al.](https://arxiv.org/abs/0801.3306),
[Chan--Church--Grochow](https://arxiv.org/abs/1502.05811)).
P78 occupies sandpile translations and P104 a finite cocycle. Only a complete
transient basin/fibre law specific to \(L_{a,b}\) can survive.

### Two proof routes

1. Cycle-rooted spanning forests plus Matrix--Tree determinants.
2. A cut at the articulation, one-dimensional tail odometers, and an
   excursion recursion at the cycle vertex.

### Kill condition

Kill if reachability literature already gives the transient trees, or if the
calculation is only the known unicycle period plus a standard hitting time.

## C05. Rotor-guided local complementation

### Literal definition

- **Phase space:** a connected graph \(G\) on \([n]\), a chip \(x\), and at
  each vertex a pointer into a fixed cyclic order of the other vertices.
- **Update:** locally complement at \(x\); advance the pointer at \(x\) to the
  next current neighbour \(y\), skipping nonneighbours; move the chip to
  \(y\). Other pointers stay fixed. LC at \(x\) leaves \(N_G(x)\) unchanged,
  so the move is unambiguous, and it preserves connectedness.
- **Parameter family:** \(n\ge2\) and an ambient rotation system.

### Early anomaly

The active neighbourhood is unchanged in the current round, but its internal
complement changes future neighbourhoods seen by other rotors. Thus the
selector is neither an external LC word nor an ordinary rotor walk. A
triangle already moves to a two-edge path while the chip move stays legal.

### Owner subtraction and internal collision

Separate LC and rotor results are zero credit. No direct coupled owner was
located in the bounded search, which is not a novelty certificate. The map
faces P78/P112 collision pressure; a generic skew-product description earns
nothing.

### Two proof routes

1. An isotropic-system groupoid cocycle over rotor states, tracking cut-rank
   or parity invariants.
2. Rotor excursion decomposition with a finite substitution rule for the
   graph neighbourhoods changed between returns.

### Kill condition

Kill unless an \(n\le5\) census exposes a stable invariant or infinite period
family. Also kill if the itinerary becomes graph-independent and hides a
clock.

## C06. Facet-nerve iteration

- **Phase space:** isomorphism classes of complexes with at most \(N\)
  vertices and \(N\) facets.
- **Update:** facets become vertices; a set of new vertices is a face iff the
  corresponding old facets have nonempty total intersection.
- **Parameter family:** \(N\ge1\).
- **Early anomaly:** nerve iteration approaches the strong core, which is the
  direct-owner mechanism rather than a residual.
- **Owner subtraction:** Barmak--Minian connect nerves, strong collapses, and
  unique cores ([primary paper](https://arxiv.org/abs/0907.2954)); P114 owns
  exact parallel reduction clocks.
- **Proof routes:** incidence Galois/Dowker duality; dominated-vertex strong
  collapses.
- **Kill condition:** triggered by the direct iteration-to-core owner and
  P114 shadow. **KILL.**

## C07. Delete all poset beat points simultaneously

- **Phase space:** finite \(T_0\) posets, including the empty poset.
- **Update:** delete every current up or down beat point and retain the
  induced order.
- **Parameter family:** posets of order at most \(n\).
- **Early anomaly:** in a two-chain, the lower point is up beat and the upper
  point down beat; both disappear, whereas sequential deletion leaves the
  one-point core.
- **Owner subtraction:** Stong owns beat-point/core theory
  ([primary source](https://www.ams.org/tran/1966-123-02/S0002-9947-1966-0195042-2/));
  P114/P105 add internal collision.
- **Proof routes:** sequential deformation retractions; Hasse domination
  layers.
- **Kill condition:** core safety fails at order two, while any tie repair is
  nonintrinsic. **KILL.**

## C08. One-fire parallel chip-firing

- **Phase space:** nonnegative configurations of fixed mass \(M\) on a
  connected graph \(G\).
- **Update:** every vertex with at least its degree in chips simultaneously
  sends one chip along every incident edge.
- **Parameter family:** connected cactus graphs and \(M\ge0\).
- **Early anomaly:** none survived the owner gate; eventual periods and
  stabilization are already direct subjects.
- **Owner subtraction:** period/stabilization results are zero credit
  ([Bitar--Goles](https://doi.org/10.1016/0304-3975(92)90316-8),
  [2026 result](https://doi.org/10.1016/j.dam.2026.08.021)); P78 is a direct
  paper-level collision.
- **Proof routes:** Laplacian/firing-vector invariants; recurrent firing words
  decomposed across cactus blocks.
- **Kill condition:** no prior cactus transient anomaly remains after two
  direct owners. **KILL.**

## C09. Simultaneous source-to-sink reversal

- **Phase space:** acyclic orientations of a fixed graph \(G\).
- **Update:** reverse every edge incident with a source. Sources are
  independent, so the reversals commute.
- **Parameter family:** finite connected graphs \(G\).
- **Early anomaly:** on \(K_n\), the source is moved to the sink in the total
  order, giving period \(n\).
- **Owner subtraction:** Goles--Prisner study exactly repeated parallel source
  reversal
  ([primary paper](https://doi.org/10.1016/S0304-3975(99)00122-X));
  P78/P112 add internal collision.
- **Proof routes:** Laplacian divisor classes; Coxeter heaps and cyclic shifts
  of linear extensions.
- **Kill condition:** direct literal owner. **KILL.**

## C10. Heavy-component centroid walk

- **Phase space:** pairs \((T,r)\) with fixed unrooted tree \(T\) and marked
  root \(r\).
- **Update:** move \(r\) to the neighbour in the unique component of \(T-r\)
  with more than \(|V(T)|/2\) vertices, if it exists; otherwise fix it.
- **Parameter family:** finite trees \(T\).
- **Early anomaly:** none; depth is exactly distance to the centroid set. A
  bicentroidal tree has two fixed roots and the central edge separates basins.
- **Owner subtraction:** standard centroid theory owns the mechanism; P114
  owns rooted-tree depth/basin enumeration.
- **Proof routes:** strict decrease of largest component size; convexity of a
  tree distance potential.
- **Kill condition:** renamed distance clock with no second output. **KILL.**

## C11. Durfee-row solitaire

- **Phase space:** partitions
  \(\lambda=(\lambda_1\ge\cdots\ge\lambda_\ell>0)\) of \(n\).
- **Update:** let \(d=\max\{i:\lambda_i\ge i\}\); subtract one from the first
  \(d\) parts, discard zeros, append \(d\), and sort.
- **Parameter family:** \(n\ge1\).
- **Early anomaly:** unless \(\lambda=(1^n)\), none of the decremented parts
  vanishes and one new part appears. Hence

  \[
  \tau(\lambda)=n-\ell(\lambda),
  \]

  and every orbit ends at \((1^n)\). Durfee geometry collapses to length.
- **Owner subtraction:** Bulgarian-solitaire variants are extensive
  ([generalized version](https://arxiv.org/abs/1703.07099),
  [2026 survey](https://arxiv.org/abs/2607.17194)); P113/P110 occupy the
  partition lane.
- **Proof routes:** partition-length Lyapunov; Ferrers row-creation count.
- **Kill condition:** theorem-thin and internally colliding. **KILL.**

## C12. Topswops prefix reversal

- **Phase space:** permutations \(\pi\in S_n\).
- **Update:** fix \(\pi\) if \(\pi_1=1\); otherwise reverse the first
  \(\pi_1\) entries.
- **Parameter family:** \(n\ge1\).
- **Early anomaly:** termination is classical, while the hard extremal
  stopping function is already computed through at least \(n=19\)
  ([Kimura et al.](https://arxiv.org/abs/2103.08346)).
- **Owner subtraction:** Conway's problem, Knuth's reverse search, bounds, and
  records are all zero credit; P105/P93 and the sorting firewall collide.
- **Proof routes:** Wilf-type monotone binary potentials; reverse enumeration
  of prefix-reversal predecessor trees.
- **Kill condition:** no family-specific residual and no cheap theorem pilot.
  **KILL.**

## Cheap-pilot ledger

Only the three highest-signal maps were piloted. All scripts use only the
Python standard library and deterministic enumeration or a fixed LCG.

| script | exact/sample range | assertions | falsified guesses |
|---|---|---:|---|
| proof_spikes/comb_odd_local_complement.py | exact all graphs \(n\le6\); 20,000 deterministic masks for each \(7\le n\le10\) | 372,463 | involution; degree-sequence invariance; period \(\le2\); power-of-two periods |
| proof_spikes/comb_neighbor_mex.py | quotient states \(0\le k\le6\), plus listed multipartite colourings of total order at most five | 164,185 | all nonfixed states go to the uniform cycle; quotient preperiod at most one |
| proof_spikes/comb_lyndon_rotation.py | \(q=2,n\le12\) and \(q=3,n\le9\) | 301,725 | one-step minimum rotation; depth = initial factor count minus one; depth = rotation index |

Total assertions: **838,373**. All three fresh runs exited zero. Enumeration
supports only the displayed bounded statements. The general C02 and C03
spikes also have the direct arguments stated above; no global period claim is
made for C01.

Commands:

    python3 docs/papers117_121_sequence/proof_spikes/comb_odd_local_complement.py
    python3 docs/papers117_121_sequence/proof_spikes/comb_neighbor_mex.py
    python3 docs/papers117_121_sequence/proof_spikes/comb_lyndon_rotation.py

## Proof-status gate

| ID | claim package | status |
|---|---|---|
| C01 | parity invariance, Eulerian fixed locus, component factorization, fixed criterion | PROVABLE AS STATED |
| C01 | any global restriction on recurrent periods | NOT CURRENTLY JUSTIFIED; periods 3 and 4 occur |
| C02 | multipartite collapse, quotient depth, recurrent classification, zeta | PROVABLE AS STATED |
| C02 | arbitrary-part-size original-colouring fibre formula | PROVABLE AFTER AN INCLUSION--EXCLUSION LEMMA |
| C03 | strict descent, necklace endpoint/count, depth bound, sharp family/count | PROVABLE AS STATED |
| C03 | full depth-layer or one-step-fibre generating function | NOT CURRENTLY JUSTIFIED |

## Recommendation

Advance C02 first: it already supports collapse, exact recurrent
classification, a sharp transient bound, cycle count/zeta, and
parameter-sensitive fibres with two proof engines. Advance C03 only after a
targeted owner check for iterative Duval/least-conjugate algorithms. Advance
C01 as a deeper anomaly spike rather than a polished theorem: its invariant
is exact, but high-period witnesses demand a real parity-sector
decomposition. Keep C04 and C05 on reserve. Do not reintroduce the seven kills
under renamed core, orientation, tree-height, partition, or sorting language.

**External posting, priority, novelty, authorship, and venue decisions remain
HOLD_EXTERNAL.**
