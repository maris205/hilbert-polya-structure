# Proof package — orientation subtraction and a known SER control

Author/proof contributor: /root/round211_finite_matching_scout.

## Claim and status

**PROVABLE AS STATED:** the bounded subtraction certificates below, including the explicit one-step inverse for the source-owned SER control on connected simple graphs.
**NOT CURRENTLY JUSTIFIED:** a new paper-level two-axis residual after source and old-mechanism subtraction.

No new literal is nominated. No all-parameter claim is inferred from a pilot: there was no scientific execution.

## Assumptions and notation

All graphs are finite, simple and labelled. A tree is connected and acyclic. An orientation gives each undirected edge exactly one direction. A source has indegree zero; a sink has outdegree zero. The SER control in Section 3 acts on all acyclic orientations of a fixed connected graph with $n\ge2$. Its literal step simultaneously reverses all edges incident with the old sinks. There is no moving marker, local list, rotor or extra scheduler. The singleton graph is handled separately.

For a set $U$, $\delta U$ denotes the edges having exactly one endpoint in $U$. Reversal of a specified edge set means symmetric difference of its indicator with the orientation bits. Write $N_G(B)=\bigcup_{b\in B}N_G(b)$.

## Strategy and dependency map

1. Mod-two incidence gives the complete fixed-schedule push subtraction.
2. The already-proved LAR central-branch lemma gives literal fixed-tree root-kernel collision.
3. Direct old-sink/new-source reconstruction gives the SER inverse.
4. Independent-set size and connectedness give its sharp star maximum.
5. A direct triangle orbit prevents an unsupported universal two-period extrapolation.
6. These certificates do not establish new temporal or source-priority contribution.

## 1. Fixed-schedule vertex pushes are cut translations

Fix any orientation reference on $G=(V,E)$. Encode the current orientation by $x\in\mathbb F_2^E$. Pushing vertex $v$ adds $\delta\{v\}$. For a fixed finite word $w$ of vertex pushes, let $a\in\mathbb F_2^V$ record the parity of each vertex's occurrences. The word map is exactly
$$T_w(x)=x+\delta a.$$
This follows edge by edge: the edge $uv$ is reversed once for each occurrence of either endpoint, hence its reversal parity is $a_u+a_v$. Therefore
$$T_w^2(x)=x,\qquad T_w^{-1}=T_w.$$
All fibres have size one. If $\delta a=0$, the map is the identity; otherwise every orbit has exact period two. A sweep containing every vertex once is the identity since $\delta\mathbf1=0$.

The original P145 proof identifies the cut kernel as componentwise constant vectors and the push orbit as the corresponding quotient. Thus deterministic fixed-word scheduling adds no new temporal or inverse mechanism to that read primitive. This statement is deliberately restricted to a fixed word: it does **not** identify arbitrary orientation-dependent vertex selection with one fixed translation. No such new selector was proposed.

## 2. Fixed-tree least-farthest root relocation is literally old

For a fixed labelled tree $S$ with at least two vertices, set
$$f_S(x)=\min\operatorname{argmax}_{y\in V(S)}d_S(x,y).$$
The actual old LAR proof, lines 15–18 and Lemma 1 (lines 49–95), already defines this exact marker map and proves
$$\operatorname{im} f_S=\{p,q\},\qquad f_S(p)=q,\qquad f_S(q)=p.$$

The proof mechanism is explicit. At an even-diameter center $c$, let $B$ be the branch containing the least peripheral vertex $p$; $q$ is the least maximal-depth vertex outside $B$. For $x$ of depth $r$ inside $B$, outside maximal-depth vertices have distance $r+h$, while inside-branch distances are at most $r+h-2$. Hence $f_S(x)=q$. For $x$ outside $B$, the least farthest choice is $p$, including $x=c$. Thus
$$f_S^{-1}(q)=B,\qquad f_S^{-1}(p)=V(S)\setminus B.$$
At an odd-diameter central edge, deleting that edge gives two sides; every vertex maps to the least deepest vertex on the opposite side, giving the analogous two fibres. The original proof includes the single-edge boundary and the sharp $|V(S)|-1$ fibre/star equality classification.

Calling this root relocation would only reuse the same carrier/update and complete two-image theorem. It is not new merely because the enclosing LAR system moves a leaf rather than a marker. Conversely, this exact kernel collision does not identify the entire leaf-surgery map with the marker map.

P195 is a separate already-read fixed-tree root system: it selects the least adjacent vertex whose edge-side has odd size. Its actual proof uses parity-oriented edges or the odd-cut forest, branch witnesses for the sharp tail, and a local eligible-neighbour inverse. No replacement congruence, new score selector or other parameter wrapper was introduced here.

## 3. Exact inverse for the source-owned SER control

The known literal is identified in the direct primary SER body listed in SOURCES_AND_SUBTRACTION.md. The following proof is independently written here as a subtraction/feasibility control and claims no novelty.

Let $Y$ be any acyclic orientation of a connected simple graph on $n\ge2$ vertices. Let
$$A=\operatorname{Sources}(Y),\qquad B=\operatorname{Sinks}(Y).$$
For $S\subseteq A$, let $Y^S$ be the orientation obtained by reversing all edges incident with $S$. Then the complete inverse is
$$F^{-1}(Y)=
\left\{Y^S:S\subseteq A,\ 
\text{every }b\in B\text{ has a neighbour in }S\right\}. \tag{1}$$
Different qualifying $S$ give different predecessor orientations.

### Necessity

Suppose $F(X)=Y$ and let $S$ be all sinks of $X$. There are no adjacent sinks in a graph without isolated vertices, so the simultaneous reversal is unambiguous. Each $s\in S$ becomes a source of $Y$, hence $S\subseteq A$, and reversing the same edges recovers $X=Y^S$.

Take $b\in B$. It cannot belong to $S$, since $Y$ has no isolated vertices and a vertex cannot be both a source and a sink. If $b$ had no neighbour in $S$, none of its incident edges would have changed. It would then also be a sink of $X$ outside $S$, a contradiction. Thus $S$ meets every neighbourhood of a vertex in $B$.

### Sufficiency

Now let $S\subseteq A$ satisfy the neighbourhood condition and put $X=Y^S$. The set $A$ is independent, because an edge between two sources would have an incoming endpoint. Every $s\in S$ is therefore a sink of $X$.

For $u\notin S$ that is not a sink of $Y$, choose an outgoing edge of $u$ in $Y$. Its other endpoint cannot be in $S$, since vertices in $S$ are sources of $Y$. That outgoing edge survives in $X$, so $u$ is not a sink of $X$. If $u\in B$, the assumed neighbour in $S$ supplies an outgoing edge of $u$ in $X$. Consequently the sinks of $X$ are exactly $S$.

The orientation $X$ is acyclic: a directed cycle cannot use a vertex of $S$, all of which are sinks in $X$, and all edges between the other vertices are unchanged from acyclic $Y$. Applying SER to $X$ reverses exactly the edges incident with $S$ and returns $Y$. This proves sufficiency.

### Distinctness and evaluated count

If $Y^S=Y^{S'}$, then $\delta(S\triangle S')$ is empty. Connectedness implies $S\triangle S'$ is either empty or all of $V$. The latter is impossible because both sets lie in the proper subset $A$; a connected graph with an edge cannot have every vertex a source. Thus $S=S'$.

Equation (1) is a source-neighbourhood hitting-set enumeration, not a search through unknown source orientations. Ordinary inclusion–exclusion now gives
$$|F^{-1}(Y)|=
\sum_{C\subseteq B}(-1)^{|C|}
2^{\,|A|-|A\cap N_G(C)|}. \tag{2}$$
Indeed, a subset of $A$ missing all required neighbours for each $b\in C$ must lie in $A\setminus N_G(C)$, whose subset count is the displayed power of two. No new contribution credit is assigned to inclusion–exclusion.

Since $B$ is nonempty, the empty $S$ never qualifies. Since $|A|\le n-1$,
$$|F^{-1}(Y)|\le 2^{|A|}-1\le 2^{n-1}-1. \tag{3}$$
Across connected labelled simple graphs on $n\ge2$ vertices, equality holds exactly for a star oriented toward its center. For necessity, equality forces $|A|=n-1$. Those $n-1$ vertices are independent, so connectedness forces every edge to join them to the remaining vertex, with every such edge present and directed to that vertex. Conversely, in this inward star every nonempty subset of the leaf sources hits the sole sink's neighbourhood, so (1) gives $2^{n-1}-1$ predecessors. For $n=2$, either orientation is such an inward star and the maximum is one.

For $n=1$, the unique empty-edge orientation is fixed and has one predecessor. Formula (1) was not asserted in this isolated-vertex case.

## 4. What the control does not prove

An acyclic triangle ordered $a\to b\to c$ with $a\to c$ has successive total orders
$$[a,b,c]\longmapsto[c,a,b]\longmapsto[b,c,a]\longmapsto[a,b,c].$$
The last element is the unique sink at each step and becomes the first. The three labelled orientations are distinct, so this is an exact period-three orbit. On a single edge, SER simply reverses that edge and has exact period two. These are hand deductions, not enumerated test output.

Thus tree/edge intuition cannot be promoted into an all-graph period-two theorem. The primary report's scalar ratio $m/p$ also cannot alone recover the individual integers $m,p$ or an entrance time. Formula (1) supplies only an inverse axis for a known literal; it does not establish a residual full-parameter temporal contribution or source clearance. The inaccessible original atlas/body cannot be treated as a negative result in a novelty search.

## Corrections and open risks

No claim is made that every possible graph-orientation system has been excluded. No exact tree-specific temporal formula, basin census or new global period classification is submitted. No generic potential-only, rotor/list/pointer or globally ordered matching wrapper was instantiated. The source-owned control proof above is unreviewed author deduction and is not a paper admission or manuscript-review PASS.

The bounded conclusion is therefore zero new literal proposals and no promotion; this is not an impossibility theorem about future research.
