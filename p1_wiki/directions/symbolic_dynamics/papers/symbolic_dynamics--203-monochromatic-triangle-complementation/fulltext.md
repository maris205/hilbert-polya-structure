---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--203-monochromatic-triangle-complementation"
canonical_tex: "symbolic_dynamics/papers/203-monochromatic-triangle-complementation/main.tex"
canonical_pdf: "symbolic_dynamics/papers/203-monochromatic-triangle-complementation/main.pdf"
source_sha256: "70c22a62adc3b6218278a6fd91b08dfa8d02efddf03ba7cc115bd35a3ab6de54"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Least Monochromatic-Triangle Complementation: A Sharp Entrance Time and Complete Inverse Fibres

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/203-monochromatic-triangle-complementation>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/203-monochromatic-triangle-complementation/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/203-monochromatic-triangle-complementation/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/203-monochromatic-triangle-complementation/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/203-monochromatic-triangle-complementation/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  On all simple graphs with $n$ labelled vertices, complement the three edges of the lexicographically first monochromatic triple, interpreting absent edges as colour zero, and hold if no such triple exists. We prove that every strict change of the selected triple introduces a previously unused vertex. After the first change its least vertex is constant; alternating edge colours then exclude returns, including the vertex retired before this anchor stabilizes. The maximum entrance time is exactly $\max\{0,n-3\}$. For every target, local colour and order tests reconstruct all predecessors, including empty fibres. The maximum fibre is one for $n\le3$ and $\max\{4,n-2\}$ otherwise, and explicit certificates characterize all maximizing targets. Induced complementation, generic involution scheduling and the static Johnson clique bound are classical inputs; the results concern their realization by the specified schedule.
author:
- Anonymous
bibliography:
- references.bib
title: |
  Least Monochromatic-Triangle Complementation:\
  A Sharp Entrance Time and Complete Inverse Fibres
```

## Markdown 正文

# The map and its background

Let $[n]=\{0,\ldots,n-1\}$, where $n\ge0$, and let $\mathcal X_n=\{0,1\}^{\binom{[n]}2}$. Thus the carrier consists of all simple loopless undirected labelled graphs, not only forests. Write $x_{uv}$ for the colour of the unordered pair $\{u,v\}$. Compare triples lexicographically after sorting their labels. A triple is monochromatic when its three pair colours agree. Let $\mathcal M(X)$ be the monochromatic triples, let $T(X)=\min\mathcal M(X)$ when this set is nonempty, and write $X^Q$ for complementation of the three pairs in a triple $Q$. Define $$\label{eq:map}
F(X)=\begin{cases}X^{T(X)},&\mathcal M(X)\ne\varnothing,\\
X,&\mathcal M(X)=\varnothing.\end{cases}$$ All labels remain fixed. This specifies a finite autonomous deterministic map on $2^{\binom n2}$ states.

The operation is induced subgraph complementation, as defined by Fomin et al. [@fomin2020subgraph Section 1]; their algorithmic question asks whether some chosen set reaches a graph class. No new complementation primitive is claimed here. Selecting the least available involution also gives a generic descent argument, recalled below. The additional temporal question is whether a strict change can reuse an old vertex. The inverse question is which undos satisfy all earlier-triple constraints simultaneously. The static star/top classification of Johnson cliques [@shuldiner2022clique Section 3] supplies a capacity bound, not the colour/order feasibility of actual inverse fibres.

Let $\tau(X)$ be the first time the orbit of $X$ enters a directed cycle, and put $H(n)=\max_X\tau(X)$. We prove the exact value of $H(n)$, then give complete one-step inverse sets and every maximum-fibre target. No closed basin census or all-time inverse formula is asserted.

# No-return geometry and the sharp entrance time

Along a moving orbit write $G_t=F^t(G_0)$, $T_t=T(G_t)$, and let $c_t$ be the colour of $T_t$ before its flip. Since $T_t$ remains monochromatic, $T_{t+1}\le T_t$. Equality makes the next flip undo the preceding one. Every moving orbit therefore enters a two-cycle, and cannot enter a fixed point. Its entrance time is the number of strict selector changes before the first equality. On a strict change, the new triple was previously mixed, shares exactly one edge with the flipped triple, and replaces a vertex by a smaller one. Its colour is $1-c_t$. These facts alone are generic scheduling consequences.

[\[lem:obstructions\]]{#lem:obstructions label="lem:obstructions"} Two consecutive strict changes cannot use the same shared edge. The least vertex of the selected triple cannot decrease after the first strict change.

For the first assertion, suppose three successive selectors are $abc$, $abd$, $abe$, with colours $q,1-q,q$. The edges $ae,be$ are untouched by the first two flips, and $ab$ returns to colour $q$. Hence $abe$ was initially monochromatic and earlier than $abc$, a contradiction.

For the second, write $T_0=abc$, $T_1=dab$, where $d<c$, and suppose the minimum decreases in $T_2$. The first assertion excludes the shared edge $ab$ a second time, so, interchanging $a,b$ if necessary, $T_2=eda$ with $e<\min T_1$. Then $e$ is smaller than every vertex of $T_0$. If $T_0$ has colour $q$, the untouched edge $ea$ must have colour $q$ for $T_2$. Initially $eab$ and $eac$ precede $T_0$, forcing $eb=ec=1-q$. After flipping $T_0$, the triple $ebc$ is monochromatic of colour $1-q$ and earlier than $T_1$, a contradiction. Apply this argument at each pair of consecutive strict changes.

[\[lem:no-return\]]{#lem:no-return label="lem:no-return"} Each strict selector change introduces a vertex that has not appeared in any earlier selected triple of that orbit.

First consider a strict trace with a common least vertex $a$. Orient its initial non-anchor pair according to which vertex is removed first. Lemma [\[lem:obstructions\]](#lem:obstructions){reference-type="ref" reference="lem:obstructions"} then gives the sliding representation $$T_t=\{a,v_t,v_{t+1}\},\qquad v_{t+2}<v_t.$$ Indeed, retaining the same non-anchor vertex at two successive changes would reuse the same shared edge. Both the even and odd subsequences strictly decrease. Suppose the first repeated vertex has indices $i<j$. They have opposite parity. For $i\ge1$, its anchor edge is flipped in $T_{i-1}$ and $T_i$ and retains its entry colour $c_{i-1}$ while absent. Re-entry in $T_{j-1}$ requires the opposite colour $c_{j-1}$, impossible. For $i=0$, its single flip leaves colour $1-c_0$, whereas the odd index $j$ requires colour $c_{j-1}=c_0$. Thus this trace has no return.

The only uncovered case is an initial decrease of the least vertex: $T_0=\{r,u,v\}$ of colour $q$ and $T_1=\{a,u,v\}$ with $a<\min T_0$. Put $\gamma=1-q$. In $G_1$, the five edges $au,av,uv,ru,rv$ have colour $\gamma$; $ar$ is unchanged. Initially no monochromatic triple contains $a$, since every such triple precedes $T_0$. Consequently each initial $a$-colour class $k$ induces only edges of colour $1-k$.

If $ar=\gamma$, the triples $aru,arv$ in $G_1$ force $r>\max(u,v)$ by minimality of $T_1$. Neither decreasing subsequence can introduce $r$. Otherwise $ar=q$. Orient the fixed-anchor trace from $G_1$ as $v_0=u,v_1=v$ and suppose $r$ first re-enters at relative time $k$. Its unchanged anchor edge forces $k$ odd. Thus $r=v_{k+1}$ is a new even-position vertex and its partner $w=v_k$ is odd-position, with $w\le v$. If $w\in\{u,v\}$, the edge $rw=\gamma$ in $G_1$ blocks the required $q$ triangle. Otherwise $w<v$ and the initial anchor colour of $w$ is $\gamma$: its first entry was at relative time $k-1$, which is even, and its anchor edge was untouched before entry. Hence initially $wu=wv=q$. If $rw=q$, then $ruw$ was an initial monochromatic triple earlier than $ruv$, replacing $v$ by $w<v$. Therefore $rw=\gamma$; this edge stays unchanged while $r$ is absent and again blocks re-entry. Lemma [\[lem:obstructions\]](#lem:obstructions){reference-type="ref" reference="lem:obstructions"} and the fixed-anchor argument exclude all other returns.

[\[thm:time\]]{#thm:time label="thm:time"} For every $n\ge0$, $H(n)=\max\{0,n-3\}$.

The initial selected triple uses three vertices, and every strict change uses a new one by Lemma [\[lem:no-return\]](#lem:no-return){reference-type="ref" reference="lem:no-return"}. This gives $H(n)\le n-3$ for $n\ge3$. For sharpness fix $n\ge3$, set $N=n-1$, $v_i=n-1-i$ for $0\le i<N$, and use anchor $0$. Prescribe initial anchor-edge colours $s_0=s_1=0$ and $s_i=(i-1)\bmod2$ for $i\ge2$. For $i<j$ set $$\label{eq:witness}
x_{v_iv_j}=\begin{cases}
i\bmod2,&j=i+1,\\
1-s_i,&j>i+1,\ s_i=s_j,\\
s_i,&j>i+1,\ s_i\ne s_j.
\end{cases}$$ The selected trace is $T_t=\{0,v_t,v_{t+1}\}$ of colour $t\bmod2$, for $0\le t\le n-3$. Initially the only monochromatic triple containing $0$ is $0v_0v_1$: every other pair with equal anchor colours has the opposite pair colour.

For the induction, at time $t\ge1$ the carry vertex $v_t$ has its anchor edge flipped once. Retired $v_i$, $1\le i<t$, have that edge flipped twice, restoring $s_i$; the exceptional $v_0$ has colour one. Future vertices keep their initial colours. No two future vertices form a monochromatic triple with $0$. Nor does a retired/future pair: their mutual edge is unchanged, equal initial classes have opposite pair colour, and $v_0$ has colour-zero edges to all future vertices whose anchor colour is one. Retired/retired eligible pairs are later than the proposed pair. Future vertices matching the carry's current colour have indices $j=t+1,t+3,\ldots$. The consecutive edge is eligible by [\[eq:witness\]](#eq:witness){reference-type="eqref" reference="eq:witness"}; for $j\ge t+3$ the initial classes differ and its colour $s_t=1-(t\bmod2)$ is wrong. Every carry/retired eligible pair is later because retired labels exceed the next future label. Non-anchor triples are also later. This proves the stated trace. Its last triple is $012$, the first possible triple, and its flip is immediately reversed. There are exactly $n-3$ strict changes. For $n<3$ the map is the identity; at $n=3$ its moving states already lie in their two-cycle.

# Every target and its complete inverse

For $Q\in\mathcal M(Y)$ of colour $c$, impose these target-local conditions:

D

:   Every $P\in\mathcal M(Y)$ with $P<Q$ satisfies $|P\cap Q|=2$.

C

:   For $u\notin Q$ and $\{x,y\}\subset Q$ with $\{u,x,y\}<Q$, the colours $y_{ux},y_{uy}$ are not both $1-c$.

Let $\mathcal A(Y)$ be the monochromatic triples satisfying D and C.

[\[thm:inverse\]]{#thm:inverse label="thm:inverse"} Every target has the exact predecessor set $$F^{-1}(Y)=\begin{cases}
\{Y\},&\mathcal M(Y)=\varnothing,\\
\{Y^Q:Q\in\mathcal A(Y)\},&\mathcal M(Y)\ne\varnothing.
\end{cases}$$ The displayed sources are distinct. A moving target is in the image if and only if $\mathcal A(Y)\ne\varnothing$. If $Q=T(Y)$ has colour $c$, then $Y$ is recurrent if and only if C holds for $Q$.

A nonholding predecessor leaves its selected triple monochromatic, so it must be $Y^Q$ for $Q\in\mathcal M(Y)$. Distinct triples flip different edge sets. For $Q$ to be selected in $Y^Q$, all earlier triples must be mixed. An earlier monochromatic target triple is destroyed exactly when it shares an edge with $Q$, giving D. A mixed triple becomes monochromatic only by sharing one flipped edge $xy$; this occurs exactly when its two unchanged edges have colour $1-c$, excluded by C. All other triples are unchanged. These cases prove necessity and sufficiency. A target with no monochromatic triple cannot result from a nonholding move. For $Q=T(Y)$, there is no earlier monochromatic target triple, so C alone says the selector stays equal after the flip. This is precisely the previously established recurrent criterion.

# Maximum fibres and all equality targets

[\[thm:max\]]{#thm:max label="thm:max"} The largest one-step fibre is $$M_n=\begin{cases}1,&n\le3,\\ \max\{4,n-2\},&n\ge4.\end{cases}$$ For a moving target, the inverse-triple family $\mathcal A(Y)$ is contained in a common-edge star or the four faces of a four-set.

If $P<Q$ are admissible, D for $Q$ forces $|P\cap Q|=2$. Such a family is a clique of the Johnson graph $J(n,3)$. Its classical star/top containment and capacities [@shuldiner2022clique Theorem 3.4 and Corollary 3.5] have this elementary specialization. Given members $abc,abd$, every other member either contains $ab$ or is $acd$ or $bcd$. If either latter triple occurs, each common-edge member must use $c$ or $d$ as its third vertex, so all members lie in the four-set $abcd$. Otherwise all share $ab$. Families of size at most one also satisfy the containment. Thus the capacities are $n-2$ and four. For $n\le3$, $F$ is a permutation, so every fibre has size one.

For the star lower bound, colour every edge incident with $0$ or $1$ by $c$, and every remaining edge by $1-c$. Each $01v$ is admissible: reversing it destroys all earlier monochromatic star triples, creates no earlier one, and leaves any outer monochromatic triple later. For the four-face bound, colour every edge by $c$ except $0v$ for $v\ge4$, which have colour $1-c$. Every face of $S=\{0,1,2,3\}$ is admissible. Other faces are destroyed by its flip. A triple containing $0$, an outside vertex and another vertex is mixed regardless of the flip, since the two edges to that outside vertex have different colours; two outside vertices with $0$ also give a mixed triple. Triples without $0$ and not contained in $S$ are later than every face containing $0$, and later than $123$. Hence no earlier monochromatic triple remains. Both capacities are attained for all $n\ge4$.

The following tests characterize the feasibility of a *full* star or four-face inverse family using only target colours and order. They do not call $F$ or require a prior inverse computation.

For $n\ge4$, choose $a<b$, set $U=[n]\setminus\{a,b\}$ and $c=y_{ab}$, and write $Q_z=\{a,b,z\}$ and $Q_*=Q_{\max U}$. Call $ab$ *star-certified* when:

S1

:   $y_{az}=y_{bz}=c$ for every $z\in U$.

S2

:   If $x<y$ are in $U$, $y_{xy}=c$, and $z\in U\setminus\{x,y\}$, then $Q_z<\{a,x,y\}$.

S3

:   Every monochromatic triple contained in $U$ is later than $Q_*$.

For a four-set $S$, let $Q_*$ be its last face. Call $S$ *face-certified* when:

K1

:   All six internal edges of $S$ have one colour $c$.

K2

:   Every monochromatic triple $P$ with $|P\cap S|\le1$ is later than $Q_*$.

K3

:   For $u\notin S$, $\{x,y\}\subset S$, set $P=\{u,x,y\}$. If $y_{ux}=y_{uy}=c$, then $P$ is later than every face not containing $xy$. If both equal $1-c$, it is later than every face containing $xy$. Mixed pairs impose no condition.

[\[thm:equality\]]{#thm:equality label="thm:equality"} Every target maximizes its fibre for $n\le3$. For $n=4,5$, a target maximizes exactly when it has a face-certified four-set. For $n=6$, it maximizes exactly when it has a star-certified edge or a face-certified four-set. For $n\ge7$, it maximizes exactly when it has a star-certified edge.

S1 is equivalent to all $Q_z$ being monochromatic. Under S1, reversing one star triple creates no other monochromatic triple: a putative shared edge incident with $a$ or $b$ has an unchanged outside edge of colour $c$, blocking creation in colour $1-c$. Other star triples are destroyed through $ab$. The other existing monochromatic triples involving an endpoint are $axy,bxy$ with $y_{xy}=c$. They survive a reversal of $Q_z$ exactly when $z\notin\{x,y\}$. Since $axy<bxy$, their exclusion before $Q_z$ is exactly S2. Outer monochromatic triples never change, giving S3. Thus S1--S3 hold exactly when every star triple is admissible.

K1 is equivalent to all four faces being monochromatic; each other face becomes mixed under a face reversal. Triples meeting $S$ in at most one vertex never change, giving K2. A triple $uxy$ with two vertices in $S$ changes only when $xy$ is in the reversed face. If its two outside edges have colour $c$, it is monochromatic exactly when $xy$ is not flipped; if both have colour $1-c$, exactly when it is flipped. Unequal outside colours always block monochromaticity. K3 is precisely the earlier-triple exclusion for these cases. Hence K1--K3 hold exactly when all faces are admissible. Finally equality in Theorem [\[thm:max\]](#thm:max){reference-type="ref" reference="thm:max"} fills a largest containing star or top. Their capacities tie only at $n=6$, yielding all the stated alternatives. The converse follows from the same certificates and the upper bound.

# Exact checks and scope

The standalone verifier enumerates every state through $n=6$, compares two literal representations, computes direct orbit paths, and checks complete predecessor sets against D/C and all S/K equality tests. Two fresh runs each passed $374\,812$ assertions with byte-identical output. Table [1](#tab:checks){reference-type="ref" reference="tab:checks"} reports finite corroboration; none of the all-size proofs depends on the enumeration.

::: {#tab:checks}
    $n$   States   Image   $H(n)$   $M_n$
  ----- -------- ------- -------- -------
      3        8       8        0       1
      4       64      46        1       4
      5     1024     594        2       4
      6    32768   19034        3       4

  : Complete small carriers; image counts are finite data, not an all-size formula.
:::

The fixed locus is the classical class containing neither a triangle nor an independent triple; Ramsey's elementary six-vertex argument excludes fixed states for $n\ge6$. These static facts and the generic two-cycle argument are not additional contributions. The results isolate a no-return vertex budget and ordered-colour feasibility for one schedule; they do not assert a new Johnson bound, a full basin census, or a closed count of all maximizing targets.

#### Scope and release status.

`HOLD_EXTERNAL`. The ownership comparison is bounded to the inspected literature and internal history. No global novelty or priority claim is made, and external release is not authorized.
