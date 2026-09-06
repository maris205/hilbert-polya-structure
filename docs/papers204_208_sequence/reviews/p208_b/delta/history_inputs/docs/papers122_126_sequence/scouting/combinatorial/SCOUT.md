# P122--P126 combinatorial/geometric dynamics scout

**Status:** internal scouting only; **external HOLD**. No paper number is assigned.

**Snapshot:** 2026-08-30 UTC.

## 1. Scope and collision firewall

I read the P001--P121 directory names and the prior P107--P121 candidate pools,
collision maps, and kill ledgers before generating this pool. Exact repeats were
removed before testing. None of the candidates below re-proposes cycle pruning,
MIS polarity, partition shift--join, principal hooks, leaf/forest peeling,
ordinary closure, sorting/0-Hecke, odd-run erosion, synchronous multipartite
mex, maximal-bond contraction, odd-fringe mirror, local complementation,
CFL-factor rotation, chip firing, rowmotion, strong/GYO collapse, or the earlier
domino/crossing rotors.

The table contains exactly **16 literal self-maps**. Three received deterministic
standard-library pilots, the maximum allowed by the scouting protocol. Owner
searches used literal and structural formulations, included 2025--2026 queries,
and treated only primary papers, journal pages, DOI pages, official repositories,
or authors' paper pages as technical evidence. A search no-hit is bounded evidence
only, never a novelty claim.

Verdicts: PROMOTE_SPIKE means enough exact structure for a proof spike; CAUTION
marks unusually close owner subtraction; RESERVE leaves one cheap gate; KILL
means direct ownership, internal collision, or a theorem-thin selector.

## 2. Candidate table (exactly 16)

| ID | Literal phase space and update | Parameter / early signal | Owner and internal subtraction | Score / verdict / hard kill condition |
|---|---|---|---|---|
| **C01** | Plane full binary trees with $n$ internal vertices. Write $T=(L,R)$. If $|L|$ is even and $R=(B,C)$, set $\Phi T=((L,B),C)$; if $R$ is a leaf, fix $T$. If $|L|$ is odd, write $L=(A,B)$ and set $\Phi T=(A,(B,R))$. | $n\ge0$. At $n=2$ the two trees form a 2-cycle. Through $n=12$, depth is exactly $\lfloor(n-1)/2\rfloor$ and one-step indegree is at most 2. | Ordinary rotations and Catalan enumeration are zero-credit. Firewall against P120 odd-fringe child-list mirroring and P114 peeling: this changes root association, not child order or vertex set. | **8.6, PROMOTE_SPIKE.** Kill if an exact subtree-parity root scheduler is owned, the spine proof fails, or the map is conjugate to an occupied one. |
| **C02** | Permutations $\pi\in S_n$. Cut the one-line word immediately before every left-to-right maximum; reverse every even-length record block simultaneously and leave odd blocks unchanged. | $n\ge0$. Every changed state drops lexicographically. Exact maximum depth is $n-1$; $(2,3,\ldots,n,1)$ is sharp. Fixed counts start $1,1,1,3,9,45,225,\ldots$. | Foata's first fundamental transformation and all-odd-cycle enumeration are zero-credit. Firewall against P105 bond-run contraction and P117 erosion: neither deletion nor run erosion occurs. | **8.3, PROMOTE_SPIKE.** Kill on a direct iterative record-block reversal owner, or if the residual never exceeds the fixed-point bijection plus elementary depth induction. |
| **C03** | Labelled simple graphs on $[n]$. Find current connected components and complement the induced graph on every odd-order component; leave even components unchanged, simultaneously. | $n\ge0$. First genuine 2-cycle at $n=5$; maximum depth $\lfloor(n-1)/2\rfloor$. A recursive split tree, fixed/recurrent EGFs, and zeta are available. | Corneil--Lerchs--Stewart Burlingham own recursive complementation/cotrees for cographs. All decomposition language is zero-credit; only the parity-scheduled map on **all** labelled graphs and its finite dynamics may remain. | **7.9, PROMOTE_SPIKE / CAUTION.** Kill if parity scheduling is already in cograph/modular-decomposition work, or if the result is only a cotree restatement. |
| **C04** | Edge-labelled ribbon graphs with $m$ edges. Compare the parities of the two incident boundary-component lengths of every edge, counting edge-side occurrences. Let $A(G)$ be the edges seeing opposite parities and set $\Phi(G)=G^{A(G)}$, the simultaneous partial dual. | $m\ge0$; the ribbon-group orbit is finite. The selector changes face cycles, so it is not a fixed group element. No canonical pilot yet. | Chmutov owns partial duality; Ellis-Monaghan--Moffatt own the ribbon-group action; Yan--Deng--Metsidik (2026) study vertex distributions over its orbits. Only the adaptive selector could remain. | **6.7, RESERVE_OWNER_FIRST.** Promote only if a permutation-encoding pilot gives a uniform non-product clock/fibre theorem and the 2026 neighborhood has no adaptive owner. |
| **C05** | Dyck paths of semilength $n$. In the unique first-return factorization $P=UADB$, swap $A,B$ when the elevation-area parity of $P$ is odd; otherwise fix $P$. | $n\ge1$. Even $n$ gives an idempotent half-census; odd $n$ gives an involution. | Deutsch (1999) directly owns the underlying swap $UADB\mapsto UBDA$; the area-parity gate is thin. | **2.0, KILL_DIRECT.** No residual beyond conditioning an owned involution. |
| **C06** | Labelled simple graphs. Form maximal biconnected blocks; for every odd-order block $B$ with $|B|\ge3$, toggle every pair inside $B$, simultaneously. Blocks share at most one vertex, so toggled pair sets are disjoint. | $n$ and block-cut profile. Complementation can destroy a block in one step and expose nested clocks; unpiloted. | Nearest mechanisms are block-cut decomposition and complementation. C03 is an internal neighbor but uses connected, not 2-connected, factors. | **6.3, RESERVE.** Kill if there is no size-decreasing block tree, periods are uncontrolled, or it is merely C03 with “block” substituted. |
| **C07** | Chord diagrams, i.e. perfect matchings of $[2n]$ in circular order. Build the chord-crossing graph. For every odd-order crossing component $C$, list its endpoints $s_1<\cdots<s_{2|C|}$ and replace every endpoint $s_i$ in its chords by $s_{2|C|+1-i}$, simultaneously. | $n\ge1$. The result is another perfect matching, while recomputation may merge or split crossing components; unpiloted. | Nearest mechanisms are chord-diagram reflection/mutation and circle-graph split decomposition. This is not the killed Q03 local crossing rotor. | **6.1, RESERVE.** Kill if reflection preserves every component, making a product involution, or if circle-graph mutation owns the literal rule. |
| **C08** | Finite posets on $[n]$. In every odd-order connected component of the undirected Hasse graph, reverse all order relations; leave even components unchanged. | $n\ge0$. Components and sizes are invariant, so this is an immediate componentwise involution. | Poset duality and connected factorization own all substance. | **3.0, KILL_THIN.** No transient layer or adaptive factorization. |
| **C09** | Noncrossing partitions $P\in NC_n$. Apply Kreweras complement $K(P)$ if the current block count is odd; otherwise fix $P$. | $n\ge1$. $K$ has finite order and sends $k$ blocks to $n+1-k$, so selector parity can switch. | Kreweras owns the complement, its order, and rank behavior. | **2.8, KILL_OWNER_THIN.** Final unless a fibre statistic exists that is not reducible to owned $K$-orbits. |
| **C10** | Labelled matroids on a fixed $n$-element ground set. If rank is odd, take the matroid dual; if rank is even, fix it. | $n\ge0$. For even $n$, odd ranks form dual 2-cycles; for odd $n$, they fall into the even-rank fixed set in one step. | Matroid duality owns the operation and $r\leftrightarrow n-r$. | **2.5, KILL_THIN.** Complete dynamics is a two-line parity calculation. |
| **C11** | Simple oriented matroids on a fixed labelled set $E$. Put $e$ in $S(M)$ when the number of positive cocircuits containing $e$ is odd; reorient $M$ on all of $S(M)$, then recompute. | Rank and $|E|$. Reorientation preserves the underlying matroid but changes the positive-cocircuit census; higher cycles are possible. | Reorientation and circuit/cocircuit signatures are heavily owned; a 2026 paper studies basis-to-reorientation bijections, though not this feedback. | **5.7, RESERVE_OWNER_FIRST.** Kill if sign symmetry makes $S=\varnothing$ or a fixed subset, or if this is a known signature action. |
| **C12** | Labelled trees on $[n]$. Let $O(T)$ be the increasing list of odd-degree labels, cycle these labels once, and transport every edge by that permutation. | $n\ge2$. Handshaking makes $|O|$ even; $O$ is invariant and every orbit period divides $|O|$. | Cayley/Prüfer enumeration and relabelling actions own the mechanism; P114 is only a carrier neighbor. | **3.2, KILL_NONINTRINSIC.** Cycles come solely from an imposed label rotation. |
| **C13** | Ordered set partitions $(B_1,\ldots,B_k)$ of $[n]$. Decompose the block list into maximal runs of odd-sized blocks; reverse each run of even run-length and leave all other blocks in place. | $n,k$. Run membership is invariant, hence the map is a product involution. | Ordered set-composition factorization owns the background. | **2.4, KILL_PRODUCT.** No adaptive recomputation or transient. |
| **C14** | Triangulations of a convex $n$-gon with cyclic labels. Scan internal diagonals by lexicographic endpoint pair; flip the first diagonal whose two opposite quadrilateral vertices have different label parity; fix if none exists. | $n\ge4$. Back-flips and lexicographic interference can create short cycles. | Associahedron/flip graph and Tamari/Cambrian orientations are nearest owners; the rule is label-dependent. | **5.0, RESERVE_LOW.** Kill if it is a relabelled standard Tamari walk, or if there is no infinite-family clock. |
| **C15** | Simplicial complexes $K$ on $[n]$, with void/full conventions fixed. If the number of facets is odd, apply Alexander dual $K^*=\{S:[n]\setminus S\notin K\}$; otherwise fix $K$. | $n\ge0$. Duality is involutive but may switch facet parity, giving only a selector transient plus possible 2-cycle. | Combinatorial Alexander duality owns the map and $K^{**}=K$. | **2.3, KILL_OWNER_THIN.** Only a parity gate on an owned involution remains. |
| **C16** | Clutters $\mathcal H$ on $[n]$. If $|\mathcal H|$ is odd, replace it by its blocker $b(\mathcal H)$, the clutter of inclusion-minimal hitting sets; otherwise fix it. | $n\ge0$, with empty-clutter conventions stated. Since $b^2(\mathcal H)=\mathcal H$, this is a gated involution. | Edmonds--Fulkerson directly own blocker duality and $b^2=\mathrm{id}$. | **2.2, KILL_DIRECT.** Selector gating supplies no paper-scale residual. |

## 3. Strongest exact theorem signals

### C01: parity-guided root rotation

Let $C(z)=\sum_{n\ge0}C_nz^n$ be the Catalan OGF and
$E(z)=(C(z)+C(-z))/2$. The following has a direct proof skeleton, not
just an enumerative fit.

1. Every trajectory walks in one direction along a root spine until the first
   even-sized middle subtree, where it traverses the same rotation edge back.
   Hence every eventual period is 1 or 2.
2. Every transient rotation passes a distinct odd-sized middle subtree and
   its incident internal vertex. Thus
   $\tau(T)\le\lfloor(n-1)/2\rfloor$; alternating combs attain equality.
3. Fixed trees are exactly a root with a right leaf and an even-sized left
   subtree. Including the zero-vertex leaf, their OGF is $1+zE(z)$.
4. A recurrent rotation edge is
   \[
   (A,(B,C))\longleftrightarrow((A,B),C),
   \qquad |A|,|B|\ \text{even}.
   \]
   Hence the recurrent-point OGF is
   \[
   1+zE(z)+2z^2E(z)^2C(z).
   \]
5. There is at most one left-rotation preimage and one right-rotation
   preimage, so every one-step fibre has size at most 2. Exhaustion through
   all 208,012 trees of size 12 confirms every clause.

This is the strongest candidate: a spine normal form, sharp clock, recurrent
census, fibre bound, and fixed-$n$ zeta fit a compact theorem package without
claiming generic rotation-graph background.

### C02: simultaneous even record-block reversal

Four statements already have direct proofs; the transient layer table remains
computational evidence.

1. A record block begins with its largest entry. The earliest reversed block
   therefore makes the word lexicographically smaller. There are no nontrivial
   cycles.
2. The last record block begins at the maximum $n$. If its length is even, one
   step puts $n$ in a terminal singleton and leaves a size-$(n-1)$ prefix
   problem. If it is odd, that block stays inert and only the earlier prefix
   evolves. Induction gives $\tau(\pi)\le n-1$.
3. The permutation $(2,3,\ldots,n,1)$ has depth exactly $n-1$.
4. Fixed points are precisely the permutations whose record blocks all have
   odd length. Foata's transformation identifies them with permutations
   having all cycles odd. Therefore
   \[
   \sum_{n\ge0}f_n\frac{x^n}{n!}
   =\exp\left(\sum_{j\ge0}\frac{x^{2j+1}}{2j+1}\right)
   =\sqrt{\frac{1+x}{1-x}},
   \]
   with $f_{2m}=((2m-1)!!)^2$ and
   $f_{2m+1}=(2m+1)!!(2m-1)!!$.
5. Exact depth layers are canonical through $n=9$, but **no layer recurrence
   is claimed**. Deriving one, or an exact pointwise fibre recursion, is the
   paper-scale gate.

Foata's bijection and the all-odd-cycle EGF receive zero contribution credit.
The possible residual is the literal synchronous map, its sharp clock, and a
still-needed transient/fibre theorem.

### C03: odd-component complementation

For an odd connected component $H$, either $\overline H$ is connected and
$H\leftrightarrow\overline H$ is a 2-cycle, or $\overline H$ splits into
smaller components that can never merge again. This gives a recursive odd
co-component split tree.

1. Every eventual period is 1 or 2; pointwise depth is the maximum active
   split-tree height.
2. Along an active branch, odd component order drops by a positive even
   amount, hence at least 2. Thus
   $\tau(G)\le\lfloor(n-1)/2\rfloor$.
3. Sharp odd witnesses satisfy
   $G_{2k+1}=\overline{G_{2k-1}\sqcup K_2}$; adding an isolated vertex gives
   even-order witnesses.
4. Fixed graphs are exactly those whose nonsingleton components all have even
   order. If $c_n$ counts connected labelled graphs and $C_{\mathrm{even}}(x)$
   is the even part of their EGF, then
   \[
   F(x)=\exp\bigl(x+C_{\mathrm{even}}(x)\bigr).
   \]
5. For odd $n\ge3$, the connected and co-connected count is
   $b_n=2c_n-2^{\binom n2}$. Put
   $B_{\mathrm{odd}}(x)=\sum_{n\ge3,\ n\text{ odd}}b_nx^n/n!$. Recurrent
   points have EGF
   \[
   R(x)=\exp\bigl(x+C_{\mathrm{even}}(x)+B_{\mathrm{odd}}(x)\bigr).
   \]
   If $f_n,r_n$ are fixed and recurrent counts, the fixed-$n$ zeta is
   $(1-t)^{-f_n}(1-t^2)^{-(r_n-f_n)/2}$.

The cograph/cotree owner is very close, so C03 ranks below C01 and C02 despite
its thicker theorem package.

### C04: strongest unpiloted reserve

The face-parity selector is state-dependent inside a finite ribbon-group orbit,
but almost all ambient structure is owned. It is not promoted. The only useful
next action is an owner-first permutation encoding through $m=5$, looking for
a period beyond 2, a uniform parity clock, or a nontrivial exact fibre formula.
Absence of all three is an immediate kill.

## 4. Canonical pilot evidence

All code uses only the Python standard library and is confined to this directory.

| Pilot | Exhaustive scope | Main checks | Assertions | Canonical output |
|---|---:|---|---:|---|
| pilot_parity_root_rotation.py | all plane full binary trees, $0\le n\le12$ | closure, size, period, sharp depth, fixed/recurrent criteria and OGF, fibre at most 2 | **1,743,138** | pilot_parity_root_rotation.out |
| pilot_even_record_reversal.py | all permutations, $0\le n\le9$ | closure, strict lex drop, fixed formula, exact depth layers, maximum indegree, sharp witness | **1,821,399** | pilot_even_record_reversal.out |
| pilot_odd_component_complement.py | all labelled simple graphs, $0\le n\le6$ | component refinement, period/depth, fixed/recurrent criteria, assembly EGFs, zeta integrality | **214,396** | pilot_odd_component_complement.out |
| **Total** |  |  | **3,778,933** |  |

Canonical comparison command, with STEM replaced by each file stem:

    python3 docs/papers122_126_sequence/scouting/combinatorial/pilot_STEM.py \
      | cmp - docs/papers122_126_sequence/scouting/combinatorial/pilot_STEM.out

Falsified guesses retained to prevent theorem inflation:

- C01 is not idempotent: the two size-2 trees form a 2-cycle. It is not
  globally an involution either: size 3 already has a transient. Singleton
  fibres also fail at size 3.
- C02 is not idempotent: depth 2 occurs at $n=3$. Absence of cycles is instead
  certified by strict lexicographic descent.
- C03 does not always settle at a fixed graph: $n=5$ has 432 points on
  2-cycles, and 80 graphs have depth 2.

## 5. Primary owner audit and zero-credit ledger

### C01: binary-tree rotations

- Lucas, Roelants van Baronaigien, and Ruskey,
  [“On Rotations and the Generation of Binary Trees”](https://www.sciencedirect.com/science/article/pii/S019667748371045X),
  *Journal of Algorithms* 15 (1993), 343--366,
  DOI 10.1006/jagm.1993.1045, own rotation graphs and rotation-based
  generation.
- Busjatskaja and Kochetkov,
  [“Even and odd trees”](https://arxiv.org/abs/1811.10357), study parity and
  rotation groups for plane/bipartite trees, but their bracket-code/root
  parity is not the current left-subtree-size scheduler.
- Searches for “subtree parity root rotation,” “even left subtree rotate,”
  “parity guided associahedron walk,” and 2025--2026 variants found no direct
  map. This is a bounded no-hit. Catalan counts, ordinary rotations,
  associahedra, and rotation-graph facts are zero-credit.

### C02: record blocks

- Foata and Han,
  [“Signed words and permutations, I: A fundamental transformation”](https://doi.org/10.1090/S0002-9939-06-08436-X),
  *Proceedings of the AMS* 135 (2007), 31--40, and the classical first
  fundamental transformation own the record-block/cycle correspondence.
- Lugo,
  [“Profiles of Permutations”](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v16i1r99),
  *Electronic Journal of Combinatorics* 16 (2009), R99,
  DOI 10.37236/188, owns the weighted-cycle framework and all-odd-cycle
  enumeration used by the fixed EGF.
- Searches for simultaneous/even record-block reversal, iterated reversal at
  left-to-right maxima, Foata-block dynamics, and 2025--2026 record dynamics
  returned distributional and pattern papers but no direct iteration. This
  no-hit is bounded. The fixed-point bijection and EGF are zero-credit.

### C03: component complementation

- Corneil, Lerchs, and Stewart Burlingham,
  [“Complement reducible graphs”](https://www.sciencedirect.com/science/article/pii/0166218X81900135),
  *Discrete Applied Mathematics* 3 (1981), 163--174,
  DOI 10.1016/0166-218X(81)90013-5, explicitly study graphs reducible by
  recursively complementing connected subgraphs and their unique tree
  representation.
- Searches for odd-order component complementation, parity-scheduled component
  complement, iterative co-component splitting, and 2025--2026 cograph
  dynamics found no literal schedule. All decomposition and cotree statements
  are nevertheless zero-credit. Any residual must be phrased narrowly as exact
  finite dynamics of this parity scheduler on all labelled graphs.

### C04: ribbon partial duality

- Chmutov,
  [“Generalized duality for graphs on surfaces and the signed Bollobás--Riordan polynomial”](https://www.sciencedirect.com/science/article/pii/S0095895608001421),
  *Journal of Combinatorial Theory B* 99 (2009), 617--638,
  DOI 10.1016/j.jctb.2008.09.007, owns partial duality.
- Ellis-Monaghan and Moffatt,
  [“Twisted duality for embedded graphs”](https://arxiv.org/abs/0906.5557),
  own the $S_3^{|E|}$ ribbon-group action and orbit framework.
- Yan, Deng, and Metsidik,
  [“Introducing a vertex polynomial invariant for embedded graphs”](https://www.sciencedirect.com/science/article/abs/pii/S0012365X26001354),
  *Discrete Mathematics* 349 (2026), 115111, study vertex distributions
  across ribbon-group orbits. This recent neighborhood makes C04 high-risk.

### Direct-owner kills

- Deutsch,
  [“An involution on Dyck paths and its consequences”](https://www.sciencedirect.com/science/article/pii/S0012365X98003707),
  *Discrete Mathematics* 204 (1999), 163--166,
  DOI 10.1016/S0012-365X(98)00370-7, owns C05's first-return swap.
- Kreweras,
  [“Sur les partitions non croisées d'un cycle”](https://www.sciencedirect.com/science/article/pii/0012365X72900416),
  *Discrete Mathematics* 1 (1972), 333--350,
  DOI 10.1016/0012-365X(72)90041-6, owns C09's complement.
- Björner and Tancer,
  [“Combinatorial Alexander Duality -- a Short and Elementary Proof”](https://arxiv.org/abs/0710.1172),
  later DOI 10.1007/s00454-008-9102-x, own C15's dual and involution.
- Edmonds and Fulkerson,
  [“Bottleneck extrema” (primary scan)](https://web.vu.lt/mif/s.jukna/EC_Book_2nd/Edmonds-Fulkerson.pdf),
  *Journal of Combinatorial Theory* 8 (1970), 299--306, define the blocker and
  prove $b(b(\mathcal H))=\mathcal H$. C16 has no residual.

The search covered literal rules and close structural translations, not every
unpublished note, thesis, or non-indexed book. No no-hit may be written as
“first,” “novel,” or priority. Before any freeze, repeat the gate in
MathSciNet/zbMATH/Google Scholar citation neighborhoods.

## 6. Promote/reserve/kill ledger

### Promote to proof spike

1. **C01 parity-guided root rotation:** highest score and cleanest firewall.
2. **C02 even record-block reversal:** promote, with an exact layer recurrence
   or fibre law as the paper-scale gate, not the owned fixed EGF.
3. **C03 odd-component complement:** promote under CAUTION; owner subtraction
   must precede contribution language.

### Reserve only

- **C04:** owner-first ribbon encoding; no theorem prose yet.
- **C06:** one block-tree experiment; kill unless size loss is uniform.
- **C07:** one crossing-component experiment; kill if it is a product involution.
- **C11:** parity-identity calculation before enumeration.
- **C14:** literal Tamari/Cambrian comparison before computation.

### Killed now

- Direct/near-direct owner and selector-thin: **C05, C09, C10, C15, C16**.
- Mechanical product or label artifact: **C08, C12, C13**.

## 7. Recommended proof spikes and graph/record ordering

1. **C01 -- formal spine encoding.** Prove period dichotomy, sharp
   $\lfloor(n-1)/2\rfloor$ clock, indegree at most 2, recurrent OGF, and
   fixed-$n$ zeta by two routes: a rotation-spine word and recursive root
   decomposition. Repeat the owner gate against associahedron orientations.
2. **C02 -- record-block recursion.** Formalize the maximum-$n$ induction and
   Foata subtraction, then derive either an exact depth-layer recurrence or a
   pointwise fibre recursion. Without one, demote to reserve. The proof-completion
   risk is therefore **medium**: fixed points and sharp depth are done, but the
   paper-scale transient enumerator is not.
3. **C03 -- odd co-component split tree.** Formalize well-foundedness, sharp
   witnesses, assembly EGFs, and zeta. Its mathematical completion risk is
   **low**, because the recursion is already explicit; its owner risk is
   **high**, because the 1981 cograph paper owns recursive connected-subgraph
   complementation and cotrees.
4. **C04 -- not yet a proof spike.** Build a ribbon-permutation encoder only
   after the direct 2026 owner neighborhood is exhausted.

For the requested graph-versus-record comparison: **rank C02 record reversal
above C03 graph complementation for freezing**, despite C03's more complete
theorem package. C02 has medium proof-completion risk but a cleaner residual;
C03 is nearly proved but has a direct mechanism owner and thus high novelty/
scope risk. The overall ordering remains **C01 > C02 > C03 > C04**.

Everything remains external HOLD.
