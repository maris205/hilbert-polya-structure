---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--148-even-level-plane-tree-contraction"
canonical_tex: "symbolic_dynamics/papers/148-even-level-plane-tree-contraction/main.tex"
canonical_pdf: "symbolic_dynamics/papers/148-even-level-plane-tree-contraction/main.pdf"
source_sha256: "d48b8c37f66c16795474765c9fe328493c8c6888af9abe3a848512ea803ce3f6"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Even-Level Contraction of Plane Rooted Trees: Divisibility Iterates and Complete Size-Refined Fibres

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/148-even-level-plane-tree-contraction>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/148-even-level-plane-tree-contraction/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/148-even-level-plane-tree-contraction/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/148-even-level-plane-tree-contraction/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/148-even-level-plane-tree-contraction/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Delete every odd generation of a plane rooted tree, promote each deleted vertex's ordered child block to its parent, reset parity, and repeat. We analyze this literal map on the finite carrier of trees with at most $N$ vertices while keeping its exact-size source layers distinct. After $k$ steps, precisely the original depths divisible by $2^k$ survive. Hence a tree of height $h$ reaches the singleton after $\lceil\log_2(h+1)\rceil$ steps, and the sharp maximum on $n$ vertices is $\lceil\log_2n\rceil$. For every target $U$ with $m$ vertices and $I(U)$ internal vertices, a reversible ordered block-and-gap construction gives $$\sum_{E(T)=U}y^{|T|-m}=\frac{y^{I(U)}}{(1-y)^{2m-1}}.$$ Thus $U$ occurs from the exact $n$-vertex layer exactly when $m+I(U)\le n$, with an explicit binomial fibre. Weighting a target by its minimum predecessor size yields the algebraic series $H=z+z^2H/(1-H)$, and $H/(1-z)$ counts exact-layer images. An exact audit of all $23{,}714$ plane trees through $11$ vertices supplies counterexample pressure but is not used as proof.
author:
- Anonymous
bibliography:
- references.bib
title: |
  Even-Level Contraction of Plane Rooted Trees:\
  Divisibility Iterates and Complete Size-Refined Fibres
```

## Markdown 正文

# The finite map and the exact-layer question

Let $\mathcal{PT}_n$ be the set of plane rooted trees with $n$ vertices, and fix $N\ge1$. The literal dynamical carrier is the finite disjoint union $$\mathcal{PT}_{\le N}:=\bigsqcup_{1\le n\le N}\mathcal{PT}_n.$$ A tree is an ordered list of its child trees. If $T=(T_1,\ldots,T_d)$ and $T_i=(T_{i1},\ldots,T_{ir_i})$, define recursively $$\label{eq:E-recursive}
 E(T):=\bigl(E(T_{11}),\ldots,E(T_{1r_1}),
             \ldots,E(T_{d1}),\ldots,E(T_{dr_d})\bigr).$$ Geometrically, the root and every even-depth vertex are retained. Each odd-depth child is deleted, its child block is promoted, and the blocks are concatenated in the original plane order. Equation [\[eq:E-recursive\]](#eq:E-recursive){reference-type="eqref" reference="eq:E-recursive"} then resets parity within every retained grandchild subtree. The singleton $\boldsymbol{\cdot}$ is fixed.

The output uses a subset of the input vertices, so $E$ is a self-map of $\mathcal{PT}_{\le N}$. It is generally not a self-map of $\mathcal{PT}_n$. We therefore use $\mathcal{PT}_n$ only as an *exact source layer*: expressions such as $E(\mathcal{PT}_n)$ always mean the image of that subset inside the finite carrier. The formal fibre series below ranges coefficientwise over all finite source layers; for fixed $N$, it is truncated after source size $N$. Because $N$ is arbitrary, we state exact-layer results for every $n$; inside a fixed carrier they are read with $1\le n\le N$.

Plane-tree decompositions and parity-sensitive statistics have a mature enumerative literature [@ChenLiShapiro2007]. More directly, outward-contraction groups every even-level vertex with all its odd-level children and takes the resulting partition-tree [@SooKhoussainovLinz2022 Definition 6.6]. If $\operatorname{For}$ forgets plane order, then, with the same designated root, $$\label{eq:forgetful-owner}
 \operatorname{For}(E(T))\cong
 \operatorname{OutContr}(\operatorname{For}(T),\operatorname{root}(T)).$$ Indeed, the quotient vertices are indexed by the original even-depth vertices, and each quotient edge crosses an odd vertex to an original grandchild. Thus the unordered one-step rule, its partition-tree interpretation, and bare height compression receive zero contribution credit. Ordered child promotion also occurs inside generic forest contractions [@BerkemerSiederdissenStadler2021], while simultaneous plane-tree transitions [@NicholsEtAl2020] and Horton-style leaf pruning [@KovchegovZaliapin2016] give nearby but different dynamics. Catalan enumeration, parity statistics, generic contraction, transition vocabulary, and pruning clocks likewise receive zero credit. The residual claims concern the plane-order lift under repeated parity reset, its all-rank divisibility and sharp pointwise clock, and its complete ordered target inverse and exact-layer image series.

# Divisible-depth skeletons and the sharp clock

Write $h(T)$ for the maximum root depth and let $\tau(T)$ be the least $k\ge0$ such that $E^k(T)=\boldsymbol{\cdot}$.

[\[thm:clock\]]{#thm:clock label="thm:clock"} For every plane rooted tree $T$ and $k\ge0$, the vertices of $E^k(T)$ are exactly the original vertices whose depths are divisible by $2^k$. Each is joined to its nearest retained ancestor, and the plane order is induced by the original contour order. Consequently $$\label{eq:height-clock}
 h(E(T))=\left\lfloor\frac{h(T)}2\right\rfloor,
 \qquad
 \tau(T)=\left\lceil\log_2(h(T)+1)\right\rceil.$$ The singleton is the unique recurrent state, and for every $n\ge1$, $$\label{eq:max-clock}
       \max_{T\in\mathcal{PT}_n}\tau(T)=\lceil\log_2n\rceil.$$

Track original vertex identities. The assertion at $k=0$ is immediate. Assume that at rank $k$ an original vertex of depth $d$ survives precisely when $2^k\mid d$, in which case its current depth is $d/2^k$. The next contraction retains it precisely when this current depth is even, or equivalently when $2^{k+1}\mid d$. Promoting across the deleted current level joins nearest retained ancestors. Since concatenation of ordered blocks is associative, the resulting order is the one induced from the original contour. This proves the iterate assertion by induction.

A deepest root path contains a vertex at every depth from $0$ through $h(T)$. It follows that $h(E^k(T))=\lfloor h(T)/2^k\rfloor$. Thus $E^k(T)$ is the singleton exactly when $2^k>h(T)$, whose least solution is the second formula in [\[eq:height-clock\]](#eq:height-clock){reference-type="eqref" reference="eq:height-clock"}. Every nonsingleton loses at least one depth-one vertex, so it cannot be recurrent. Finally $h(T)\le n-1$, and the $n$-vertex path has height $n-1$; this proves [\[eq:max-clock\]](#eq:max-clock){reference-type="eqref" reference="eq:max-clock"}, including non-powers of two.

# A complete ordered block-and-gap inverse

For a target tree $U$, let $m=|U|$, let $d_U(v)$ be the outdegree of $v$, and let $$I(U):=|\{v\in U:d_U(v)>0\}|.$$ Weight every source vertex deleted in one contraction by $y$.

[\[lem:local\]]{#lem:local label="lem:local"} At a target vertex of outdegree $d$, the generating function for its inserted odd children is $$\label{eq:local-factor}
 A_0(y)=\frac1{1-y},
 \qquad
 A_d(y)=\frac{y}{(1-y)^{d+1}}\quad(d>0).$$ These choices form a reversible local construction.

For $d=0$, every odd child must be a leaf; an arbitrary number gives $A_0(y)$. Suppose $d>0$ and exactly $r$ odd children are productive. Their grandchildren split the ordered target child list into $r$ nonempty consecutive blocks, in $\binom{d-1}{r-1}$ ways. Any number of empty odd leaves may occupy each of the $r+1$ gaps before, between, and after those productive children. Hence $$\begin{aligned}
 A_d(y)
 &=\sum_{r=1}^d\binom{d-1}{r-1}\frac{y^r}{(1-y)^{r+1}}\\
 &=\frac{y}{(1-y)^2}
   \left(1+\frac{y}{1-y}\right)^{d-1}
 =\frac{y}{(1-y)^{d+1}}.\end{aligned}$$ The predecessor child list uniquely recovers which odd children are empty and which consecutive block each productive child carries. Thus the construction is reversible.

[\[thm:fibre\]]{#thm:fibre label="thm:fibre"} For every target $U$ with $m$ vertices, $$\label{eq:fibre-series}
 \sum_{E(T)=U}y^{|T|-m}
       =\frac{y^{I(U)}}{(1-y)^{2m-1}}.$$ Consequently, among sources in $\mathcal{PT}_n$ the fibre size is $$\label{eq:fibre-coefficient}
 |E^{-1}(U)\cap\mathcal{PT}_n|=
 \begin{cases}
 \displaystyle\binom{n-m-I(U)+2m-2}{2m-2},&n-m\ge I(U),\\[6pt]
 0,&n-m<I(U).
 \end{cases}$$

For a target $U$, write $$F_U(y):=\sum_{E(T)=U}y^{|T|-|U|}.$$ If $U=(U_1,\ldots,U_d)$, the reversible construction in Lemma [\[lem:local\]](#lem:local){reference-type="ref" reference="lem:local"} gives the coefficientwise formal-series recursion $$\label{eq:fibre-recursion}
                  F_U(y)=A_d(y)\prod_{j=1}^dF_{U_j}(y).$$ Indeed, each productive inserted odd child carries predecessor subtrees for one nonempty consecutive block of the ordered list $(U_1,\ldots,U_d)$; empty inserted odd children occupy the intervening gaps. The predecessor child list recovers both the block partition and every subtree predecessor, so the construction is injective and surjective with no double counting. Induction on $|U|$ proves [\[eq:fibre-recursion\]](#eq:fibre-recursion){reference-type="eqref" reference="eq:fibre-recursion"}; for each coefficient only finitely many inserted vertices occur.

Now apply Lemma [\[lem:local\]](#lem:local){reference-type="ref" reference="lem:local"} through this recursion. Internal vertices contribute one numerator factor $y$ and leaves contribute none. Since a rooted tree satisfies $\sum_vd_U(v)=m-1$, the total denominator exponent is $$\sum_{v\in U}(d_U(v)+1)=(m-1)+m=2m-1.$$ This proves [\[eq:fibre-series\]](#eq:fibre-series){reference-type="eqref" reference="eq:fibre-series"}. Extracting the coefficient of $y^{n-m}$ gives [\[eq:fibre-coefficient\]](#eq:fibre-coefficient){reference-type="eqref" reference="eq:fibre-coefficient"} by the negative-binomial expansion. For the singleton target, the formula correctly gives one source of every size: the corresponding star.

The temporal and inverse proofs use different structures. The first tracks depth divisibility, whereas the second reconstructs ordered child lists; the fibre is not inferred from the clock or a state census.

# Exact-size images and an algebraic series

[\[cor:image\]]{#cor:image label="cor:image"} A target $U$ lies in $E(\mathcal{PT}_n)$ if and only if $$\label{eq:image-condition}
                     |U|+I(U)\le n.$$

The coefficient in [\[eq:fibre-coefficient\]](#eq:fibre-coefficient){reference-type="eqref" reference="eq:fibre-coefficient"} is positive exactly under condition [\[eq:image-condition\]](#eq:image-condition){reference-type="eqref" reference="eq:image-condition"}.

Define the minimum-source-weight series $$\label{eq:H-def}
                    H(z):=\sum_Uz^{|U|+I(U)},$$ where the sum is over all finite plane rooted trees. A leaf contributes $z$. An internal root contributes $z^2$ and has a nonempty ordered sequence of child trees. Therefore $$\label{eq:H-equation}
          H=z+z^2\sum_{d\ge1}H^d
           =z+\frac{z^2H}{1-H}.$$ Equivalently, $H$ is the root with zero constant term of $$H^2-(1+z-z^2)H+z=0.$$ Explicitly, $$\label{eq:H-closed}
 H(z)=\frac{1+z-z^2-
 \sqrt{(1+z-z^2)^2-4z}}{2},$$ where the minus branch is forced by $H(0)=0$. Corollary [\[cor:image\]](#cor:image){reference-type="ref" reference="cor:image"} now gives $$\label{eq:image-gf}
 \sum_{n\ge1}|E(\mathcal{PT}_n)|z^n=\frac{H(z)}{1-z}.$$ The factor $(1-z)^{-1}$ takes cumulative sums of the minimum source weights; it does not turn $E$ into a size-preserving map.

# Exact audit and conclusion

An independent standard-library verifier generates every plane tree through $11$ vertices. For every state it labels original vertices, compares each iterate with the predicted divisible-depth skeleton, and checks the clock. For every target and source size it compares observed fibres with [\[eq:fibre-coefficient\]](#eq:fibre-coefficient){reference-type="eqref" reference="eq:fibre-coefficient"}; it also checks the local factors coefficientwise and solves [\[eq:H-equation\]](#eq:H-equation){reference-type="eqref" reference="eq:H-equation"} as a formal series. The $216{,}905$ exact assertions all pass. Table [1](#tab:audit){reference-type="ref" reference="tab:audit"} records the main profile; it is falsification pressure, not proof evidence.

::: {#tab:audit}
  $n$                       1   2   3   4    5    6     7     8      9     10      11
  ----------------------- --- --- --- --- ---- ---- ----- ----- ------ ------ -------
  $|\mathcal{PT}_n|$        1   1   2   5   14   42   132   429   1430   4862   16796
  $|E(\mathcal{PT}_n)|$     1   1   2   3    5    9    17    34     71    153     338
  $\max\tau$                0   1   2   2    3    3     3     3      4      4       4

  : Exact source-layer profile. The state column is the Catalan carrier count; it receives no contribution credit.
:::

The result identifies both what survives repeated reset-parity contraction and exactly how every target can be expanded one step. Its source-layer image series follows from the same local inverse threshold, while the literal dynamics remains on $\mathcal{PT}_{\le N}$.

# Limitations {#limitations .unnumbered}

The theorem is specific to finite plane rooted trees and the simultaneous deletion of every odd generation. It does not cover unordered trees, arbitrary selected levels, weighted contractions, or asymptotic random-tree questions. The unordered one-step shadow is the directly owned outward-contraction in [@SooKhoussainovLinz2022]; only the ordered iterate/fibre/image conjunction is retained. The reopened literature audit was bounded; no novelty or priority claim is made. Enumeration through $11$ vertices cannot replace the proofs. The manuscript remains under `HOLD_EXTERNAL`.

# Data Availability {#data-availability .unnumbered}

No external data were used. The anonymous artifact contains the standard-library verifier and its frozen exact output. External release of the artifact is not authorized at this stage.

# Ethics Statement {#ethics-statement .unnumbered}

The work uses no human participants, animals, personal data, or deployed decision system.

# Author Contributions {#author-contributions .unnumbered}

Contributor identities are withheld for anonymous review. The anonymous author team takes responsibility for conceptualization, formal analysis, software, validation, and writing.

# Conflict of Interest {#conflict-of-interest .unnumbered}

The authors declare no known conflict of interest relevant to this internal mathematical study.

# Funding {#funding .unnumbered}

No funding claim is made in this anonymous internal draft.
