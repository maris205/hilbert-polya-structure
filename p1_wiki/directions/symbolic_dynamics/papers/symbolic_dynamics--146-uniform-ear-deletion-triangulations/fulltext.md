---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--146-uniform-ear-deletion-triangulations"
canonical_tex: "symbolic_dynamics/papers/146-uniform-ear-deletion-triangulations/main.tex"
canonical_pdf: "symbolic_dynamics/papers/146-uniform-ear-deletion-triangulations/main.pdf"
source_sha256: "991989128e15e54358426aaf74070c61316d628b3dad48f1ff8071ff972d854a"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Uniform Ear Deletion of a Convex Polygon: Exact Triangulation Masses and a Sharp Path-Dual Minimum

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/146-uniform-ear-deletion-triangulations>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/146-uniform-ear-deletion-triangulations/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/146-uniform-ear-deletion-triangulations/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/146-uniform-ear-deletion-triangulations/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/146-uniform-ear-deletion-triangulations/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Start with a labelled convex $n$-gon. Repeatedly choose a current vertex uniformly, delete it, and record the chord between its two current neighbours, stopping at a triangle. Although all $n!/6$ deletion histories are equiprobable, their triangulation endpoints need not be; nonuniformity first occurs at $n=6$. For a triangulation $T$ and one of its triangular faces $r$, root the weak dual at $r$ and let $s_v^{(r)}$ be the rooted-subtree size at $v$. We prove that the number of histories with endpoint $T$ and final face $r$ is $$H(T,r)=\frac{(n-3)!}{\prod_{v\ne r}s_v^{(r)}}.$$ Consequently $\mathbb P(T)=6H(T)/n!$, where $H(T)=\sum_r H(T,r)$. Equivalently, $H(T)$ counts complete leaf-deletion orders of the unrooted weak dual. This yields the sharp bound $H(T)\ge 2^{n-3}$, with equality exactly when the weak dual is a path. An exhaustive exact-arithmetic audit through $n=9$ checks every endpoint and final-face refinement. Classical ear clipping, triangulation enumeration, weak duals, and tree hook formulas are treated as inputs rather than contributions.
author:
- Anonymous
bibliography:
- references.bib
title: |
  Uniform Ear Deletion of a Convex Polygon:\
  Exact Triangulation Masses and a Sharp Path-Dual Minimum
```

## Markdown 正文

# The process and the theorem

Let $P_n$ be a convex polygon whose vertices have distinct labels. If its current cyclic vertex set has size at least four, choose one current vertex uniformly, join its two current neighbours, and delete it. Stop as soon as three vertices remain. The recorded chords form the random endpoint triangulation $T$. Ear clipping is classical in polygon triangulation algorithms [@EderHeldPalfrader2018], and convex-polygon ear deletion also appears in bijections for triangulations [@Regev2013]. Here the object of study is the endpoint law induced by uniform choice among *all* current vertices.

For a triangulation $T$, its weak dual $D_T$ has one vertex for each triangular face and one edge for each pair of faces sharing a diagonal. It is a tree on $m=n-2$ vertices. If a face $r$ is distinguished and $D_T$ is rooted at $r$, write $s_v^{(r)}$ for the number of vertices in the subtree rooted at $v$. Define $$\label{eq:root-hook}
 H(T,r):=\frac{(n-3)!}{\prod_{v\in V(D_T)\setminus\{r\}}s_v^{(r)}},
 \qquad H(T):=\sum_{r\in V(D_T)}H(T,r).$$

[\[thm:main\]]{#thm:main label="thm:main"} For every labelled convex $n$-gon, $n\ge3$, the following hold.

1.  The process lasts $n-3$ steps, and each complete deletion history has probability $6/n!$.

2.  For every triangulation $T$ and face $r$, exactly $H(T,r)$ histories end at $T$ with $r$ as the final face. In particular, $$\label{eq:endpoint-law}
           \mathbb P(T)=\frac{6}{n!}H(T).$$

3.  The endpoint multiplicity obeys $$\label{eq:lower}
           H(T)\ge 2^{n-3}.$$ Equality holds if and only if $D_T$ is a path. Thus the least endpoint probability is $6\,2^{n-3}/n!$, attained exactly by path-dual triangulations.

The theorem gives every endpoint mass, not just the extremum. Formula [\[eq:root-hook\]](#eq:root-hook){reference-type="eqref" reference="eq:root-hook"} is integer-valued because it counts histories; it is the familiar rooted-tree hook expression, used here after identifying the exact deletion poset. The forest hook formula and its refinements are classical [@BjornerWachs1989] and receive zero contribution credit.

# Histories as dual-tree orders

At a stage with $k$ current vertices, every vertex of the convex $k$-gon is an ear. Hence every ordered list of $n-3$ distinct original labels is a legal history. Its probability is $$\label{eq:history-prob}
 \frac1n\frac1{n-1}\cdots\frac14=\frac{3!}{n!},$$ and there are $n!/3!$ such lists. Each deletion inserts the diagonal that cuts off its ear. The induction invariant is that the remaining convex polygon together with the already cut-off ear triangles triangulates the original polygon. Thus the next neighbour chord is new and noncrossing. After $n-3$ steps there are exactly $n-3$ distinct diagonals, hence a triangulation.

Fix now an endpoint triangulation $T$ and a proposed final face $r$. Removing an ear of $T$ removes a leaf of $D_T$; the ear tip uniquely determines the leaf face, and conversely a leaf face different from $r$ has a unique ear tip that can be deleted. Iterating gives the following precise correspondence.

[\[lem:bijection\]]{#lem:bijection label="lem:bijection"} Histories ending at $(T,r)$ are in bijection with orders of $V(D_T)\setminus\{r\}$ in which every child occurs before its parent when $D_T$ is rooted at $r$.

Given a history, label each deleted vertex by the triangular face cut off at that step. A face can disappear only after all faces below it in the rooted dual have disappeared, so descendants occur before ancestors. The last triangle is $r$. Conversely, take any such order. Every prefix removes a descendant-closed set, so the unremoved faces form the connected ancestor-closed subtree containing $r$ and triangulate the current convex polygon. When a dual vertex $v$ is scheduled, all its children have gone while its parent remains. Thus $v$ is a leaf of the remaining dual and its unique ear tip is currently deletable. Deleting those tips reconstructs a unique polygon history and records exactly the diagonals of $T$. The two constructions are inverse.

[\[prop:hook\]]{#prop:hook label="prop:hook"} The number of orders in Lemma [\[lem:bijection\]](#lem:bijection){reference-type="ref" reference="lem:bijection"} is the quantity $H(T,r)$ in [\[eq:root-hook\]](#eq:root-hook){reference-type="eqref" reference="eq:root-hook"}.

Put $q=n-3=m-1$. For a rooted tree, split the $q$ nonroot vertices into the branches below the root, of sizes $q_1,\ldots,q_d$. Orders internal to different branches may be interleaved in $\binom{q}{q_1,\ldots,q_d}$ ways. Applying the same decomposition within each branch and cancelling the factorials gives $$\frac{q!}{\prod_{v\ne r}s_v^{(r)}}.$$ The one-vertex case initializes the induction. Lemma [\[lem:bijection\]](#lem:bijection){reference-type="ref" reference="lem:bijection"} then gives the asserted history count.

Summing Proposition [\[prop:hook\]](#prop:hook){reference-type="ref" reference="prop:hook"} over the mutually exclusive final faces gives $H(T)$. Multiplying by the common history probability [\[eq:history-prob\]](#eq:history-prob){reference-type="eqref" reference="eq:history-prob"} proves parts (1) and (2) of Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}. It also proves normalization without a separate identity: all $n!/6$ histories have exactly one endpoint and final face.

# The sharp path-dual minimum

For an unrooted tree $D$, let $L(D)$ be the number of ways to delete leaves one at a time until a single vertex remains. Choosing that final vertex as $r$ and then orienting all edges toward it partitions these orders by their surviving vertex. Lemma [\[lem:bijection\]](#lem:bijection){reference-type="ref" reference="lem:bijection"} therefore gives $$\label{eq:L=H}
       H(T)=L(D_T).$$ If $\mathop{Leaf}(D)$ is the leaf set, then $$\label{eq:recurrence}
 L(K_1)=1,
 \qquad
 L(D)=\sum_{v\in\mathop{Leaf}(D)}L(D-v)\qquad (|V(D)|\ge2).$$

[\[prop:min\]]{#prop:min label="prop:min"} For every tree $D$ on $m\ge1$ vertices, $$L(D)\ge2^{m-1},$$ with equality if and only if $D$ is a path (including the one-vertex path).

Proceed by induction on $m$. The claim is immediate for $m=1$. Every tree with $m\ge2$ has at least two leaves, and $D-v$ is a tree on $m-1$ vertices for each leaf $v$. By [\[eq:recurrence\]](#eq:recurrence){reference-type="eqref" reference="eq:recurrence"} and induction, $$L(D)\ge |\mathop{Leaf}(D)|\,2^{m-2}\ge2^{m-1}.$$ If equality holds, then $D$ has exactly two leaves; a finite tree with exactly two leaves is a path. Conversely, deleting either endpoint of a path leaves a path, so equality follows recursively from [\[eq:recurrence\]](#eq:recurrence){reference-type="eqref" reference="eq:recurrence"}.

Taking $m=n-2$ in Proposition [\[prop:min\]](#prop:min){reference-type="ref" reference="prop:min"}, using [\[eq:L=H\]](#eq:L=H){reference-type="eqref" reference="eq:L=H"}, proves part (3) of Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}.

# Exact audit and scope

An independent standard-library verifier enumerates every ordered deletion history through $n=9$. For each endpoint it reconstructs all triangular faces and the connected weak dual, checks every final-face count against [\[eq:root-hook\]](#eq:root-hook){reference-type="eqref" reference="eq:root-hook"}, independently computes the leaf-order recurrence, brute-forces bounded rooted linear extensions, checks total probability in exact rational arithmetic, and tests the equality class in Proposition [\[prop:min\]](#prop:min){reference-type="ref" reference="prop:min"}. Table [1](#tab:audit){reference-type="ref" reference="tab:audit"} is frozen output, not proof evidence.

::: {#tab:audit}
    $n$   histories   triangulations   $H_{\min}$   $H_{\max}$   path dual
  ----- ----------- ---------------- ------------ ------------ -----------
      3           1                1            1            1           1
      4           4                2            2            2           2
      5          20                5            4            4           5
      6         120               14            8           12          12
      7         840               42           16           28          28
      8        6720              132           32          112          64
      9       60480              429           64          316         144

  : Exhaustive endpoint audit. Here $H_{\min}$ and $H_{\max}$ are endpoint history multiplicities, and the last column counts path-dual triangulations.
:::

The claims are deliberately bounded. The polygon is convex, selection is uniform over current vertices, and the theorem does not address nonconvex visibility, weighted choices, or a classification of the maximum of $H(T)$. Ear clipping, Catalan enumeration, weak-dual trees, reduction-order/linear- extension correspondences---including a different-carrier example for phylogenetic networks [@CoronadoPonsRiera2024]---and the generic tree hook formula receive no priority claim. A bounded source search did not locate the combined endpoint law and sharp minimum above, but a search non-hit is not a novelty or priority certificate. The residual is elementary and owner-thin. The manuscript remains anonymous and under `HOLD_EXTERNAL`.
