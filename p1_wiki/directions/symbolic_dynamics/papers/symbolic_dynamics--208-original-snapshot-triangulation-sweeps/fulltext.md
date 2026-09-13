---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--208-original-snapshot-triangulation-sweeps"
canonical_tex: "symbolic_dynamics/papers/208-original-snapshot-triangulation-sweeps/main.tex"
canonical_pdf: "symbolic_dynamics/papers/208-original-snapshot-triangulation-sweeps/main.pdf"
source_sha256: "3664f35386e4b0de4aca8deb6e10f05f6edc198909e8a133f5b79f4e18ba348c"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Source Sets and Sharp Clocks of Original-Snapshot Triangulation Sweeps

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/208-original-snapshot-triangulation-sweeps>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/208-original-snapshot-triangulation-sweeps/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/208-original-snapshot-triangulation-sweeps/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/208-original-snapshot-triangulation-sweeps/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/208-original-snapshot-triangulation-sweeps/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We determine the source sets and recurrent dynamics of a fixed sweep on triangulations of a convex polygon with cyclic labels $0,\ldots,n-1$. At each iteration, the current internal diagonals are snapshotted, ordered lexicographically by their endpoint pairs, and flipped once in that order; new diagonals are not visited during the same sweep. Protected diagonals split the update into smaller cells and give an exact binary-tree recursion. A disjoint parser of seed and subsequent cells then constructs every labelled one-step predecessor, including the zero and comb boundaries. Every positive fibre is a power of two, and for $n\ge5$ the unique maximum target is the fan at vertex $1$, with $2^{n-4}$ predecessors. A size-preserving auxiliary map intertwines the two square phases of the sweep. Its stronger closed-class inclusion, together with a commuting odd phase, proves that the triangle is fixed and every $n\ge4$ carrier has a unique two-cycle. The maximum entrance time is zero for $n=3,4$ and exactly $n-2$ for $n\ge5$; explicit witnesses treat both parities. These are deductive all-size results. Complete finite checks on the original sizes $3\le n\le10$ provide separate numerical pressure.
author:
- Anonymous
bibliography:
- references.bib
title: |
  Source Sets and Sharp Clocks of\
  Original-Snapshot Triangulation Sweeps
```

## Markdown 正文

# The sweep and its two conclusions {#sec:setup}

A flip is reversible, but resetting an ordered list of diagonals after a whole sweep need not be. We study this reset operation on the full set of triangulations of a convex $n$-gon, $n\ge3$, whose vertices carry fixed cyclic labels $0,1,\ldots,n-1$. Write each internal diagonal as $(a,b)$ with $a<b$, snapshot the $n-3$ diagonals, and sort these pairs lexicographically. In the current triangulation, flip each diagonal of this original list once, in that order. Denote the resulting self-map by $F_n$, or $F$ when the size is understood. The snapshot is reset at every iteration; it is never refreshed during an iteration.

We use the classical ordered-tree dictionary rooted at the boundary edge $(0,n-1)$: the triangle incident to that edge gives an ordered pair of subpolygons, recursively [@pallo2006]. A boundary interval is a leaf $e$, and a tree is $e$ or an ordered pair $(L,R)$. A polygon tree has $N=n-1$ leaves and $m=n-2$ internal vertices. The one-leaf tree is only an auxiliary recursion boundary. We extend $F(e)=e$. Write $|T|$ for the number of leaves and $q(T)=|T|-1$ for the internal size. Let $$c=(e,e),\qquad \mathrm{LC}_1=\mathrm{RC}_1=e,\qquad
 \mathrm{LC}_{a+1}=(\mathrm{LC}_a,e),\qquad \mathrm{RC}_{a+1}=(e,\mathrm{RC}_a).$$ All trees are ordered, so the dictionary retains every polygon label.

[\[thm:inverse\]]{#thm:inverse label="thm:inverse"} The recursive construction in Section [3](#sec:sources){reference-type="ref" reference="sec:sources"} produces every labelled one-step source of every target exactly once. A nonleaf target $Y$ has fibre $$|F^{-1}(Y)|=
 \begin{cases}
 h(R),&Y=(\mathrm{LC}_l,R),\quad l\ge1,\\
 0,&\text{its root left child is not a left comb},
 \end{cases}$$ where the evaluated recursion for $h$, including $h(e)=1$, is [\[eq:h\]](#eq:h){reference-type="eqref" reference="eq:h"}. Every positive fibre is a power of two. For $n\ge5$, the maximum is $2^{n-4}$, attained only at the fan at vertex $1$. For $n=3,4$, every target has one source.

Define $$Z_1=e,\qquad Z_2=c,\qquad Z_N=(c,Z_{N-2})\quad(N\ge3).$$ An entrance time is the least $t\ge0$ for which $F^t(T)$ is periodic; thus a periodic starting state has entrance zero.

[\[thm:clock\]]{#thm:clock label="thm:clock"} The triangle is fixed. For every $n\ge4$, the unique recurrent component is the two-cycle $$Z_N\ \longleftrightarrow\ (e,Z_{N-1}),\qquad N=n-1.$$ The maximum entrance time over the full carrier is zero for $n=3,4$, and exactly $n-2$ for every $n\ge5$.

The two conclusions share a geometric recursion but use different deductions: a source-set parser for Theorem [\[thm:inverse\]](#thm:inverse){reference-type="ref" reference="thm:inverse"}, and exact square-phase transport through a map $K$ for Theorem [\[thm:clock\]](#thm:clock){reference-type="ref" reference="thm:clock"}. The flip primitive, its edge-labelled lift, static counting and generic prefix freezing are not claimed as separate contributions; Section [7](#sec:scope){reference-type="ref" reference="sec:scope"} states these deductions and the limits of the comparison.

# Protected cells and the exact recursion {#sec:cells}

For a nonleaf $T$, its left-spine list is the unique nonempty list $\mathop{\mathrm{LS}}(T)=[B_1,\ldots,B_k]$ such that $$T=\mathop{\mathrm{Fold}}(B_1,\ldots,B_k)
   =(\cdots((e,B_1),B_2),\ldots,B_k).$$ Let $\iota(S,A)$ replace the leftmost leaf of $S$ by $A$; hence $\iota(e,A)=A$ and $\iota((L,R),A)=(\iota(L,A),R)$. Put $G(B)=F((e,B))$, and for lists of length at least two define $$\label{eq:product}
 P(B_1,B_2)=F((B_1,B_2)),\qquad
 P(B_1,\ldots,B_k)=\iota\bigl(G(B_k),P(B_1,\ldots,B_{k-1})\bigr)
 \quad(k\ge3).$$ Unlike $F$, $G$ adds one leaf.

[\[lem:cells\]]{#lem:cells label="lem:cells"} Every scheduled diagonal is present at its visit. The geometric sweep is given exactly by $$\begin{aligned}
 F(e)&=e,\qquad F(c)=c,\qquad G(e)=c, \label{eq:bases}\\
 F(T)&=(e,P(\mathop{\mathrm{LS}}(T))) &&\text{if }|\mathop{\mathrm{LS}}(T)|\ge2, \label{eq:non-ear}\\
 G((e,C))&=\iota(G(C),c), \label{eq:ear-one}\\
 G(B)&=(c,P(\mathop{\mathrm{LS}}(B))) &&\text{if }|\mathop{\mathrm{LS}}(B)|\ge2. \label{eq:ear-many}\end{aligned}$$ The recursion is well founded, with strictly smaller recursive cells.

Flipping one diagonal removes only that diagonal, so every unvisited original diagonal remains present. Its replacement crosses the removed original. Since the original set is noncrossing, this replacement was not original and will never be scheduled. Every inserted diagonal is therefore protected for the remainder of this sweep.

Suppose first that vertex $0$ is not an ear. Its original neighbours are $1=a_0<a_1<\cdots<a_k=n-1$, $k\ge2$. The triangles incident to $0$ are $(0,a_{j-1},a_j)$; their other-side subpolygons encode $B_j$ in $\mathop{\mathrm{LS}}(T)$. The first scheduled diagonals are $(0,a_1),\ldots,(0,a_{k-1})$. At visit $i$, the adjacent triangles are $(0,1,a_i)$ and $(0,a_i,a_{i+1})$: for $i>1$, the preceding flip has created the first triangle. Thus the flip inserts $(1,a_{i+1})$.

These new diagonals protect the ear at $0$ and partition its complement into cells. The first cell, bounded by $(1,a_2)$, has the initial tree $(B_1,B_2)$. Its remaining scheduled diagonals include the original root of each nonleaf $B_1,B_2$, not only the roots' proper descendants. For $j\ge3$, the cell between $(1,a_{j-1})$, $(1,a_j)$ and the boundary arc encoded by $B_j$ has tree $(e,B_j)$, with the preceding prefix represented by one boundary interval. Its scheduled diagonals are exactly the original root of $B_j$, if nonleaf, and its descendants.

The increasing relabelling within each cell preserves every comparison of endpoint pairs. Consequently the restriction of the original schedule is precisely the smaller lexicographic sweep. Protected boundaries prevent flips in other cells from changing its interior; any interleaving of different cells is harmless for this reason. Induction gives cell outputs $F((B_1,B_2))$ and $G(B_j)$. Gluing in increasing order replaces the leftmost leaf of each later cell by the preceding union. This is [\[eq:product\]](#eq:product){reference-type="eqref" reference="eq:product"}; the outer ear gives [\[eq:non-ear\]](#eq:non-ear){reference-type="eqref" reference="eq:non-ear"}.

Now suppose $0$ is an ear, so $T=(e,B)$. If $B=e$, the triangle has no diagonals. If $B=(e,C)$, the only original diagonal incident to $1$ is $(1,n-1)$. Its opposite vertices are $0,2$, so its flip creates the protected edge $(0,2)$. Contract the triangle on $0,1,2$ to a boundary leaf. The remaining initial tree is $(e,C)$, with exactly the remaining original diagonals, including the root of $C$ when present. Increasing relabelling of $0,2,\ldots,n-1$ gives its smaller sweep $G(C)$. Expanding the contracted leaf gives [\[eq:ear-one\]](#eq:ear-one){reference-type="eqref" reference="eq:ear-one"}, including $C=e$.

Finally, let $\mathop{\mathrm{LS}}(B)=[C_1,\ldots,C_r]$, $r\ge2$. Write the neighbours of $1$, other than $0$, as $2=b_0<b_1<\cdots<b_r=n-1$. The first $r-1$ fan flips create the protected edges $(2,b_2),\ldots,(2,b_r)$. The final original fan diagonal $(1,n-1)$ has adjacent triangles $(0,1,n-1)$ and $(1,2,n-1)$; it flips to $(0,2)$. Beyond the protected ear, the seed and later cells are exactly those of the preceding non-ear argument for $C_1,\ldots,C_r$, with the same scheduled root edges. Their glued output is $P(\mathop{\mathrm{LS}}(B))$; the ear contributes the root left cherry, proving [\[eq:ear-many\]](#eq:ear-many){reference-type="eqref" reference="eq:ear-many"}. Every cell has fewer leaves than the input under consideration. Triangle cells use $F(c)=c$. This completes the induction.

The same recursion implies an output-shape fact used throughout: every nonleaf $F$-output is $(\mathrm{LC}_l,R)$, $l\ge1$. Every $G(B)$ for $B\ne e$ has $l\ge2$, whereas $G(e)=c$. Indeed [\[eq:non-ear\]](#eq:non-ear){reference-type="eqref" reference="eq:non-ear"} begins with a leaf, [\[eq:ear-many\]](#eq:ear-many){reference-type="eqref" reference="eq:ear-many"} begins with $c$, and [\[eq:ear-one\]](#eq:ear-one){reference-type="eqref" reference="eq:ear-one"} extends the root left comb of its smaller output by one leaf. In particular every first image has root left child $e$ or a nonleaf left comb.

# An operational decoder for every source {#sec:sources}

We specify sets, not just their cardinalities. Let $\mathsf A(Y)=\{T:F(T)=Y\}$ and $\mathsf B(Y)=\{B:G(B)=Y\}$; the following recursion constructs them without searching the carrier. For nonleaf $R$, let $\mathsf D(R)$ be the set of lists of length at least two whose $P$-output is $R$. Write $W_0(T)=T$ and $W_{j+1}(T)=(e,W_j(T))$. For a set of lists $\mathcal L$, notation $W_j\mathop{\mathrm{Fold}}(\mathcal L)$ means $\{W_j(\mathop{\mathrm{Fold}}(\mathbf B)):\mathbf B\in\mathcal L\}$.

[\[lem:inverse-boundaries\]]{#lem:inverse-boundaries label="lem:inverse-boundaries"} For nonleaf targets, the source sets are given by the following table. In its last three rows $R\ne e$. The formal bases are $\mathsf A(e)=\{e\}$, $\mathsf B(e)=\varnothing$. $$\begin{array}{c|c|c}
 \text{target }Y&\mathsf A(Y)&\mathsf B(Y)\\ \hline
 \text{noncomb root left child}&\varnothing&\varnothing\\
 \mathrm{LC}_s,\ s\ge2&\{\mathrm{RC}_s\}&\{\mathrm{RC}_{s-1}\}\\
 (e,R)&\mathop{\mathrm{Fold}}(\mathsf D(R))&\varnothing\\
 (c,R)&W_1\mathop{\mathrm{Fold}}(\mathsf D(R))&\mathop{\mathrm{Fold}}(\mathsf D(R))\\
 (\mathrm{LC}_l,R),\ l>2&W_{l-1}\mathop{\mathrm{Fold}}(\mathsf D(R))&
                         W_{l-2}\mathop{\mathrm{Fold}}(\mathsf D(R))
\end{array}$$

We induct simultaneously on leaf count. The output shape excludes the first row. For $l=1$ and $R\ne e$, a source must have a nonleaf left child, and [\[eq:non-ear\]](#eq:non-ear){reference-type="eqref" reference="eq:non-ear"} identifies it with exactly a list in $\mathsf D(R)$. No $G$-source exists by the stronger $G$-output shape.

For a $G$-target $(c,R)$, $R\ne e$, [\[eq:ear-many\]](#eq:ear-many){reference-type="eqref" reference="eq:ear-many"} gives exactly $\mathop{\mathrm{Fold}}(\mathsf D(R))$. The other branch [\[eq:ear-one\]](#eq:ear-one){reference-type="eqref" reference="eq:ear-one"} would require a $G$-output $(e,R)$ with nonleaf $R$, which has just been excluded. Its $F$-sources attach one leading $e$, yielding the fourth row. For $l>2$, only [\[eq:ear-one\]](#eq:ear-one){reference-type="eqref" reference="eq:ear-one"} can produce the longer left comb; removing its leftmost cherry uniquely reduces $l$ by one and removes one leading $e$ from the source. This proves the last row.

When the target is a comb, $P$ cannot contribute a leaf right child: its seed pair has at least two leaves and its output is nonleaf. The forced leading-$e$ reduction instead ends at $F(c)=c$ or $G(e)=c$. It gives exactly the right combs stated in the second row. In particular the triangle and the exceptional root-comb targets have not acquired an extra seed branch.

Here is the promised construction of $\mathsf D(R)$. Cut the nonempty list $\mathop{\mathrm{LS}}(R)$ in every possible way into nonempty consecutive blocks $Q_0,Q_1,\ldots,Q_s$, with $s\ge0$. For the seed, choose any ordered pair $$(B_1,B_2)\in\mathsf A(\mathop{\mathrm{Fold}}(Q_0)).$$ For each later block choose $B_{j+2}\in\mathsf B(\mathop{\mathrm{Fold}}(Q_j))$, $1\le j\le s$. Output $[B_1,B_2,B_3,\ldots,B_{s+2}]$. A choice from an empty source set contributes nothing. The seed target is nonleaf, so its source really is an ordered pair. Together with Lemma [\[lem:inverse-boundaries\]](#lem:inverse-boundaries){reference-type="ref" reference="lem:inverse-boundaries"}, these instructions are a terminating recursion: each $\mathsf D(R)$ uses inverse problems on at most $|R|$ leaves, whereas the target $(\mathrm{LC}_l,R)$ using it has strictly more leaves.

[\[prop:parser\]]{#prop:parser label="prop:parser"} The block construction gives precisely $\mathsf D(R)$, without repeated lists. Therefore the displayed decoder gives precisely all labelled polygon sources, without repetitions.

Following the leftmost branch gives the exact concatenation identity $$\mathop{\mathrm{LS}}(\iota(S,A))=\mathop{\mathrm{LS}}(A)\,\mathop{\mathrm{LS}}(S).$$ Thus each chosen seed and later source produces, by [\[eq:product\]](#eq:product){reference-type="eqref" reference="eq:product"}, the concatenated output list $\mathop{\mathrm{LS}}(R)$; folding reconstructs $R$. Conversely, an original list $[B_1,\ldots,B_k]$ determines its seed output $F((B_1,B_2))$ and every later output $G(B_j)$. Each has a nonempty left-spine list, and their lengths locate every cut. The same original list also determines the seed pair and each later source. Hence two different cut-and-source choices cannot give the same list. The forced wrappers and comb cases of Lemma [\[lem:inverse-boundaries\]](#lem:inverse-boundaries){reference-type="ref" reference="lem:inverse-boundaries"} are disjoint, so the same property holds for $\mathsf A$. Finally the ordered-tree dictionary fixes the leaf intervals and therefore every polygon endpoint label.

For evaluation it is useful to describe exactly which blocks survive. An all-leaf block has any positive length, in either position, and has multiplicity one by the comb row. A block ending in a nonleaf $D$ has form $e^aD$. Its seed is allowed for $a\ge0$; a later block requires $a\ge1$, by the $l=1$ exclusion for $\mathsf B$. In either case its multiplicity is $|\mathsf D(D)|$. A block of any other shape has no source. These are consequences of the simultaneous source construction, not assumptions about possible cuts.

# Evaluating fibres and the unique maximum {#sec:extremum}

Set $h(e)=1$. If $R\ne e$, write its unique left-spine list as $$\mathop{\mathrm{LS}}(R)=e^{a_0}D_1e^{a_1}\cdots D_re^{a_r},
 \qquad a_i\ge0,\quad D_j\ne e.$$ For $r=0$, the list has $a_0\ge1$ leaves. Define $$\label{eq:h}
 \begin{aligned}
 h(R)&=
 \begin{cases}
 2^{a_0-1},&r=0,\\
 0,&r\ge1\text{ and some }a_i=0,\ 1\le i<r,\\
 2^{E(R)}\displaystyle\prod_{j=1}^r h(D_j),&\text{otherwise},
 \end{cases}\\
 E(R)&=\max(a_0-1,0)+
       \sum_{i=1}^{r-1}(a_i-1)+\max(a_r-1,0).
 \end{aligned}$$ The last row is also zero if a recursive factor vanishes.

Put $p(R)=|\mathsf D(R)|$ for nonleaf $R$. We prove $p(R)=h(R)$ by leaf-count induction using Proposition [\[prop:parser\]](#prop:parser){reference-type="ref" reference="prop:parser"}. An all-leaf list of length $s\ge1$ has one source choice per block, and its $s-1$ internal cut positions give $2^{s-1}$ partitions.

Between two successive nonleaf decorations, a gap of $a$ leaves must give at least one leaf to the next decorated block. If $a=0$, no partition is allowed. If $a\ge1$, take the final $k\ge1$ leaves into that block, and cut the remaining $a-k$ leaves into all-leaf blocks. There is one choice for zero remaining leaves and $2^{a-k-1}$ otherwise. The total is $1+\sum_{j=1}^{a-1}2^{j-1}=2^{a-1}$. For a leading run of length $a\ge1$, either the first decoration ends the seed, consuming the entire run, or it ends a later block preceded by a nonempty all-leaf composition. This gives the same sum; length zero has one choice because the decoration itself may end the seed. A trailing run is an arbitrary composition, giving one choice at length zero and $2^{a-1}$ at positive length. The independent run factors and the recursively smaller multiplicities $p(D_j)=h(D_j)$ give [\[eq:h\]](#eq:h){reference-type="eqref" reference="eq:h"}. Lemma [\[lem:inverse-boundaries\]](#lem:inverse-boundaries){reference-type="ref" reference="lem:inverse-boundaries"} then gives the full target formula, including its zero and comb branches. Its positive values are powers of two.

[\[lem:strict\]]{#lem:strict label="lem:strict"} For nonleaf $R$, $h(R)\le 2^{q(R)-1}$, with equality if and only if $R$ is a left comb.

A left comb has an all-leaf left-spine list and attains the bound. For a positive fibre with $r\ge1$, put $A=\sum_{i=0}^r a_i$. The spine contains $A+r$ internal vertices, so $q(R)=A+r+\sum_jq(D_j)$. The gap exponent in [\[eq:h\]](#eq:h){reference-type="eqref" reference="eq:h"} is at most $A$. Induction bounds the exponent supplied by each decoration by $q(D_j)-1$. Hence $$\log_2h(R)\le A+\sum_j(q(D_j)-1)
             =q(R)-2r\le q(R)-2<q(R)-1.$$ A zero fibre cannot attain the positive bound. This proves both the inequality and all its equality cases.

For a target $(\mathrm{LC}_l,R)$ of internal size $m$, $q(R)=m-l$. If $m\ge3$, a leaf $R$ gives fibre one, strictly below $2^{m-2}$. For nonleaf $R$, Lemma [\[lem:strict\]](#lem:strict){reference-type="ref" reference="lem:strict"} gives at most $2^{m-l-1}\le2^{m-2}$; equality forces $l=1$ and $R=\mathrm{LC}_m$. This is exactly the fan at vertex $1$. At $m=1$ the cherry is fixed, and at $m=2$ the two comb orientations each have one source. The extremal part of Theorem [\[thm:inverse\]](#thm:inverse){reference-type="ref" reference="thm:inverse"} follows, with no uniqueness assertion at these small sizes.

# The size-preserving map and its stronger closure {#sec:k}

For $a\ge2$, abbreviate $D_a(R)=\iota(G(R),\mathrm{LC}_{a-1})$. The protected-cell product gives $$\label{eq:comb-action}
 F((\mathrm{LC}_a,R))=(e,D_a(R)),\qquad
 G((\mathrm{LC}_a,R))=(c,D_a(R)).$$ Indeed the left-spine list is $e^{a-1}R$. At $a=2$ its product is $F((e,R))=G(R)$; at $a>2$ the preceding all-leaf product is $\mathrm{LC}_{a-1}$, so the final gluing gives $D_a(R)$. This includes $R=e$. In particular $G((c,R))=(c,G(R))$.

If $B\ne e$, write $G(B)=(\mathrm{LC}_l,Q)$, where $l\ge2$. Define $$\label{eq:k-definition}
 K(e)=e,\qquad K(B)=D_l(Q).
 \quad\text{Then}\quad G^2(B)=(c,K(B))\quad\text{for every }B.$$ The last equality follows from [\[eq:comb-action\]](#eq:comb-action){reference-type="eqref" reference="eq:comb-action"}; for $B=e$, it reads $G^2(e)=G(c)=\mathrm{LC}_3=(c,e)$. Since $G$ adds one leaf twice and $c$ has two leaves, $K$ preserves leaf count.

[\[lem:k\]]{#lem:k label="lem:k"} The identities $$\label{eq:intertwine}
 KG=GK,\qquad K((c,R))=(c,K(R))$$ hold. Define $$\mathcal C_N=\{(\mathrm{LC}_a,R):a\ge2,\ a+|R|=N\}\quad(N\ge3),
 \qquad \mathcal C_1=\{e\},\quad\mathcal C_2=\{c\}.$$ For every $N\ge3$, $K(\mathcal T_N)\subseteq\mathcal C_N$, where $\mathcal T_N$ is the full set of $N$-leaf trees. Moreover, $$\label{eq:strong-closure}
 K(\mathcal C_N)\subseteq\{(c,S):S\in\mathcal C_{N-2}\}.$$

Compute $G^3(B)$ as $G(G^2(B))$ and as $G^2(G(B))$. Using $G((c,S))=(c,G(S))$, their equality becomes $(c,G(K(B)))=(c,K(G(B)))$. Cancellation proves commutation. Applying the same displayed identity twice to $G^2((c,R))$ and using [\[eq:k-definition\]](#eq:k-definition){reference-type="eqref" reference="eq:k-definition"} gives $$(c,K((c,R)))=G^2((c,R))=(c,G^2(R))=(c,(c,K(R))),$$ which proves the second identity.

For the first inclusion, use $K(B)=D_l(Q)$. If $Q\ne e$, the root left comb of $G(Q)$ has at least two leaves; substitution of $\mathrm{LC}_{l-1}$ cannot shorten it. If $Q=e$, the result is $\mathrm{LC}_l$; size preservation and $N\ge3$ force $l=N\ge3$. Thus $K(B)\in\mathcal C_N$.

For the stronger inclusion, take $T=(\mathrm{LC}_a,R)\in\mathcal C_N$. Equation [\[eq:comb-action\]](#eq:comb-action){reference-type="eqref" reference="eq:comb-action"} followed by [\[eq:k-definition\]](#eq:k-definition){reference-type="eqref" reference="eq:k-definition"} gives $K(T)=G(D_a(R))$. When $N\ge4$, $D_a(R)\in\mathcal C_{N-1}$. For $R=e$ it is $\mathrm{LC}_a$, with $a=N-1\ge3$; for $R\ne e$, substitution lengthens an already nonleaf root left comb. Write $D_a(R)=(\mathrm{LC}_s,Q)$, $s\ge2$. Then $K(T)=(c,D_s(Q))$. If $N-2\ge3$, the same two cases apply to $D_s(Q)$: a nonleaf $Q$ provides a nonleaf root left comb, while $Q=e$ gives $\mathrm{LC}_s$ with $s=N-2\ge3$. Thus its right child belongs to $\mathcal C_{N-2}$. At $N=4$, that child has two leaves and must be $c$. At $N=3$, the only member of $\mathcal C_3$ is $\mathrm{LC}_3$, and direct substitution gives $K(\mathrm{LC}_3)=\mathrm{LC}_3=(c,e)$. These are precisely the two boundary cases of [\[eq:strong-closure\]](#eq:strong-closure){reference-type="eqref" reference="eq:strong-closure"}.

[\[prop:k-clock\]]{#prop:k-clock label="prop:k-clock"} Each $Z_N$ is the unique recurrent state of $K$ at its size. For $N\ge3$, entrance to $Z_N$ takes at most $$d_C(N)=\left\lfloor\frac{N-2}{2}\right\rfloor
 \quad\text{from }\mathcal C_N,\qquad
 d_{\mathrm{all}}(N)=\left\lfloor\frac N2\right\rfloor
 \quad\text{from }\mathcal T_N.$$ The one- and two-leaf auxiliary classes are already fixed.

The bases $e,c$ are $K$-fixed, and [\[eq:intertwine\]](#eq:intertwine){reference-type="eqref" reference="eq:intertwine"} fixes all $Z_N$. In [\[eq:strong-closure\]](#eq:strong-closure){reference-type="eqref" reference="eq:strong-closure"}, one application of $K$ fixes the initial cherry; subsequent applications act by $K$ on its right child. At $N=3$, $\mathcal C_3=\{Z_3\}$; at $N=4$, one step reaches $Z_4$. For $N\ge5$, induction gives $1+\lfloor(N-4)/2\rfloor=\lfloor(N-2)/2\rfloor$. An arbitrary tree reaches $\mathcal C_N$ in one step, adding one to this bound. Every orbit therefore reaches $Z_N$, excluding any other periodic state.

# Both sweep phases and the sharp entrance {#sec:clock}

[\[lem:squares\]]{#lem:squares label="lem:squares"} For every tree $R$, and every $T$ with a nonleaf root left child, respectively, $$\label{eq:squares}
 F^2((e,R))=(e,K(R)),\qquad F^2(T)=K(T).$$ The second identity does not require $T\in\mathcal C_N$. Also, $$\label{eq:core-action}
 G(Z_j)=Z_{j+1},\qquad F(Z_N)=(e,Z_{N-1})\quad(N\ge3).$$

For $R=e$, the first identity is $F^2(c)=c$. Otherwise write $G(R)=(\mathrm{LC}_l,Q)$, $l\ge2$, and apply [\[eq:comb-action\]](#eq:comb-action){reference-type="eqref" reference="eq:comb-action"}: $F(G(R))=(e,D_l(Q))=(e,K(R))$. For the second identity put $P_T=P(\mathop{\mathrm{LS}}(T))$. The protected-cell equations give $F(T)=(e,P_T)$ and $G(T)=(c,P_T)$. Thus $F^2(T)=G(P_T)$; also $G^2(T)=G((c,P_T))=(c,G(P_T))$, so $K(T)=G(P_T)$. The bases $G(e)=c$, $G(c)=(c,e)$, together with $G((c,S))=(c,G(S))$, give $G(Z_j)=Z_{j+1}$ by induction. Finally the product for $Z_N=(c,Z_{N-2})$ is $G(Z_{N-2})=Z_{N-1}$, proving its $F$-action.

For $N\ge3$, the two distinct states $Z_N$ and $(e,Z_{N-1})$ are exchanged by [\[eq:core-action\]](#eq:core-action){reference-type="eqref" reference="eq:core-action"}. Their root left children are nonleaf and leaf, respectively. Every first image belongs to $\mathcal C_N$ or has form $(e,R)$, by the output-shape fact.

For a first image in $\mathcal C_N$, the second square identity and Proposition [\[prop:k-clock\]](#prop:k-clock){reference-type="ref" reference="prop:k-clock"} give at most $2\lfloor(N-2)/2\rfloor\le N-2$ further sweep steps. For a first image $(e,R)$ and $N\ge4$, the even iterates are $(e,K^t(R))$, giving the bound $2\lfloor(N-1)/2\rfloor$. There is a second, essential representation of the odd iterates: $$F^{2t+1}((e,R))=G(K^t(R))=K^t(G(R)).$$ Here commutation is [\[eq:intertwine\]](#eq:intertwine){reference-type="eqref" reference="eq:intertwine"}, and $G(R)\in\mathcal C_N$, since $R$ is nonleaf. The class clock gives the independent bound $1+2\lfloor(N-2)/2\rfloor$. Their minimum is exactly $$\min\left\{2\left\lfloor\frac{N-1}{2}\right\rfloor,\,
           1+2\left\lfloor\frac{N-2}{2}\right\rfloor\right\}=N-2.$$ Adding the first-image step proves the global upper bound $N-1=n-2$. It also shows that every orbit enters the displayed pair, so no other recurrent component exists. At $N=3$, the full carrier consists of exactly these two trees, already recurrent. At $N=2$, the carrier is the fixed cherry. Hence the entrance maximum is zero for $n=3,4$.

To retain the final unit in the upper bound, define a witness family $$S_3=(e,c),\qquad S_N=(S_{N-1},e)\quad(N\ge4),\qquad J(S)=(c,S).$$ For $N\ge4$ the root left child of $S_N$ is nonleaf, but need not be a comb, which is why the unrestricted second clause of [\[eq:squares\]](#eq:squares){reference-type="eqref" reference="eq:squares"} is needed. Its left-spine list is $[c,e,\ldots,e]$; the seed is $F((c,e))=(e,c)=S_3$, and every later $G(e)=c$ appends a right leaf. Consequently $$\label{eq:witness}
 F(S_N)=(e,S_{N-1}),\qquad
 K(S_4)=\mathrm{LC}_4,\qquad K(S_N)=J(S_{N-2})\quad(N\ge5).$$ The last two statements follow from $K(S_N)=G(S_{N-1})$ and $G(S_3)=\mathrm{LC}_4$. Also $KJ=JK$ and $GJ=JG$ by [\[eq:intertwine\]](#eq:intertwine){reference-type="eqref" reference="eq:intertwine"} and [\[eq:comb-action\]](#eq:comb-action){reference-type="eqref" reference="eq:comb-action"}.

For even $N=2k\ge4$, repeated use of [\[eq:witness\]](#eq:witness){reference-type="eqref" reference="eq:witness"} gives $$F^{N-2}(S_N)=K^{k-1}(S_N)=J^{k-2}(\mathrm{LC}_4).$$ This has a nonleaf root left child and therefore is not $(e,Z_{N-1})$. It is not $Z_N=J^{k-2}(Z_4)$ either, because $\mathrm{LC}_4\ne Z_4=(c,c)$.

For odd $N=2k+1\ge5$, the same recurrence first gives $K^{k-1}(S_N)=J^{k-1}(S_3)$. Using $F((c,S))=(e,G(S))$, and then $GJ=JG$, yields $$F^{N-2}(S_N)
   =F(J^{k-1}(S_3))
   =(e,J^{k-2}(G(S_3)))
   =(e,J^{k-2}(\mathrm{LC}_4)).$$ Its left child is a leaf, so it is not $Z_N$. The four-leaf tail again excludes $(e,Z_{N-1})$, whose corresponding tail is $Z_4$. Thus in both parities $S_N$ is outside the core at time $N-2$. The proved upper bound puts it inside by $N-1$. Its entrance is exactly $N-1=n-2$, completing Theorem [\[thm:clock\]](#thm:clock){reference-type="ref" reference="thm:clock"}.

# Source deductions, validation and limitations {#sec:scope}

#### Flips, rotations and resetting.

The classical tree--triangulation dictionary and deterministic choices of rotations precede this map. In particular, @pallo2006 studies the uniquely selected leftmost rotation and a weight coordinate which reaches its maximum and stays there. Fan building, deterministic scheduling and prefix-fixing arguments therefore carry no separate claim here.

There is also an exact lift to the edge-labelled flips of @bose2018, not just an analogy. Let $\mathcal R$ label the original diagonals $1,\ldots,n-3$ in lexicographic order, let $\tau_i$ flip the edge with label $i$ and transfer that label to its replacement, and let $\mathcal E$ erase labels. Then $$F=\mathcal E\,\tau_{n-3}\cdots\tau_1\,\mathcal R.$$ Before $\tau_i$, flips of other labels leave its original edge intact. Each $\tau_i$ is an involution on the larger labelled carrier; erasing and resetting the labels removes that invertibility. Thus noninjectivity does not exclude this composition. Our claims concern its explicit geometric source sets and its repeated reset dynamics, not a new flip primitive or a general scheduling principle.

#### Nearby inverse and orbit results.

Lattice pop-stack operators send an element to the meet of itself and its lower covers. Tamari image enumeration [@hong2022], torsion-class preimage descriptions and Cambrian orbit bounds [@barnard2023 Theorem 5.3 and Section 9], and ornamentation-lattice image and orbit results [@ajran2025] are relevant precedents. They show that all-target preimages and extremal orbit lengths are established questions on related Catalan structures. They are not used as black-box proofs of either theorem here. Already on the two-element quadrilateral Tamari chain, descending pop-stack sends both states to its minimum, whereas this sweep exchanges them. This excludes a direct same-carrier conjugacy there, but does not exclude enlarged carriers, reset lifts such as the displayed one, or every composed adapter.

#### What is and is not counted as a conclusion.

Once the disjoint parser is proved, its binary-cut factors and recursive products are elementary. The associated static Catalan/avoidance series also coincides with an older Dyck-path specialization [@mansour2006]; it is not a third result of this paper. Equality of a series does not identify its labelled objects. The retained inverse statement is which seed and later blocks reconstruct each source of this precise map, including the excluded boundaries and the unique fan extremum. On the temporal side it is the exact $K$ factorization, stronger closed-class inclusion and two-phase transport, not generic prefix freezing alone.

#### Bounded validation.

The standalone author checker generates every tree for $3\le n\le10$, all $2055$ polygon states, and independently performs each literal geometric sweep. It compares those transitions with the recursive dictionary, reconstructs each complete source set, tests the evaluated fibres and all maximizers, and extracts the full $F$- and $K$-graphs. Its canonical output contains every labelled transition, source set and entrance depth, not only aggregate counts or hashes. Auxiliary identities are tested only when their constructed trees stay within the original maximum size. Both sharp witness parities are checked. The implementation adapts the original author code, so this is author evidence rather than an independent review. The all-size conclusions rest on the proofs above, not on this finite enumeration.

The conclusions are confined to fixed cyclic labels and this precise original-snapshot lexicographic sweep. They do not assert a result for arbitrary schedules or unlabelled quotients, an all-time inverse or basin atlas, or global priority among all possible encodings. A directly applicable prior theorem or complete adapter would require reassessing the corresponding contribution.
