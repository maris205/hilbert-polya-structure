---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--199-first-one-stirling-splice"
canonical_tex: "symbolic_dynamics/papers/199-first-one-stirling-splice/main.tex"
canonical_pdf: "symbolic_dynamics/papers/199-first-one-stirling-splice/main.pdf"
source_sha256: "33e5e27fe6c9cedef8490bc33628ce06dcef0416784ed4e2671c341cdbc80beb"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Cyclically Relabelled Stirling Join: Exact Depth Layers and Root-Cut Fibres

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/199-first-one-stirling-splice>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/199-first-one-stirling-splice/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/199-first-one-stirling-splice/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/199-first-one-stirling-splice/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/199-first-one-stirling-splice/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  On Stirling permutations of order $n$, join the two occurrences of label one at their first position and then cyclically decrement all labels. The resulting fixed-rank self-map has an exact entrance clock: the largest label whose two occurrences are not adjacent. Its recurrent states are the $n!$ doubled permutations, each of exact period $n$ when $n\ge2$. For $n\ge1$ and $0\le t\le n-1$, the number of states with entrance time at most $t$ is $(n+t)!/(2^t t!)$. Independently, every predecessor is reconstructed by one cut in a target's ordered root-child list. This gives image size $2^{n-1}(n-1)!$, maximum fibre $n$, and every maximizing target. The empty and singleton orders are explicit. The local join and its tree-contraction interpretation are prior work; the results concern this particular autonomous schedule and its joint depth and inverse formulae.
author:
- Anonymous
bibliography:
- references.bib
title: |
  A Cyclically Relabelled Stirling Join:\
  Exact Depth Layers and Root-Cut Fibres
```

## Markdown 正文

# The map and its owned local operation

A Stirling permutation of order $n$ is a word in which every label in $[n]=\{1,\ldots,n\}$ occurs twice and all entries strictly between the two occurrences of $j$ exceed $j$. Write $\mathcal Q_n$ for this set, with $\mathcal Q_0=\{\varnothing\}$. For $n\ge1$, factor a word uniquely as $w=A1B1C$ and define $$\label{eq:map}
 T_n(A1B1C)=\operatorname{dec}(A)\,nn\,\operatorname{dec}(B)\operatorname{dec}(C),
 \qquad \operatorname{dec}(j)=j-1\quad(j>1).$$ The empty word is fixed. The insertion slot in [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"} is the old first occurrence of one, not an arbitrary gap.

The usual contour correspondence identifies $\mathcal Q_n$ with increasing plane trees on labels $\{0,\ldots,n\}$, rooted at zero: read a nonroot vertex's label when entering and leaving its subtree. Labels increase along each root-to-leaf path. This correspondence and maximum-label insertion are classical [@janson2008plane; @janson2011generalized]. For completeness, the pair intervals in a Stirling word cannot cross: an order $a\,b\,a\,b$ with $a<b$ would put $a$ between the copies of $b$. The intervals therefore form a nested ordered family. Their immediate containers define parents, and the exposed intervals define root children. This gives the inverse contour construction.

Vertex one must be a root child. In its root slot, replace it by a new leaf followed by its former ordered children, decrement every surviving positive label, and label the new leaf $n$. Every surviving parent-child inequality is preserved. The contour is exactly [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"}, proving that $T_n$ is a self-map.

The local surgery is not a new operation. Brualdi and Dahl [@brualdi2024multipermutations Theorem 8 and Section 5] define the left-join, prove reduction to doubled permutations in at most $n-1$ joins, and describe the associated edge contraction and pendant replacement. Extending a join to the identity on an adjacent pair, put $$\label{eq:owner}
 J_1(A1B1C)=A11BC,\qquad
 c(1)=n,\quad c(j)=j-1\ (j>1).
 \qquad T_n=c\circ J_1 .$$ The last identity is an exact comparison of the two definitions. Relabelling by $c$ alone does not preserve $\mathcal Q_n$: at order two, $1221$ becomes $2112$. Thus [\[eq:owner\]](#eq:owner){reference-type="eqref" reference="eq:owner"} is not a conjugacy of two Stirling self-maps. The joins, flattening mechanism, and bare $n-1$ scale receive no contribution credit here. The object of study is the precise clock, depth distribution, and target inverse structure of this composite.

For a finite self-map, a state is recurrent if it lies on a directed cycle. Its entrance time $\tau$ is the least nonnegative time to the recurrent set. We determine this time first, then count its levels and solve the inverse problem.

# The nonleaf-label clock and recurrent cycles

Let $I(w)$ be the labels with nonadjacent occurrences. In the contour tree these are the internal nonroot vertices. A tree with $I(w)=\varnothing$ is an ordered star, whose contour is a doubled permutation.

[\[thm:clock\]]{#thm:clock label="thm:clock"} For every $n\ge0$ and $w\in\mathcal Q_n$, $$I(T_nw)=\{j-1:j\in I(w),\ j\ge2\},
 \qquad \tau(w)=\max I(w),$$ where $\max\varnothing=0$. For $n\ge1$ the maximum entrance time is $n-1$. The recurrent set consists of the $n!$ ordered stars. For $n\ge2$ each has exact period $n$, giving $(n-1)!$ cycles. At $n=0,1$ there is one fixed point.

Deleting vertex one removes its own leaf or internal status. Every surviving vertex $j\ge2$ retains its ordered child list and receives label $j-1$. The inserted vertex $n$ is a leaf. This proves the set-transport identity and, by iteration, $$I(T_n^t w)=\{j-t:j\in I(w),\ j>t\}.$$ With $d=\max I(w)$, the tree is a star at time $d$, and if $d>0$ it is not a star at time $d-1$. On an ordered star the root slots remain fixed and the label in every slot changes by $c$. Hence the stars are permuted by $T_n$ and are recurrent. A state with nonempty $I(w)$ cannot return to itself, because its maximum internal label strictly decreases until it disappears. Thus $\tau(w)=d$.

The largest label is always a leaf, so $d\le n-1$. For $n\ge2$ the word $$11\,22\,\cdots\,(n-2)(n-2)\,(n-1)\,nn\,(n-1)$$ has $n-1$ internal and attains equality (the doubled prefix is empty at $n=2$). The assertion at $n=1$ follows from $T_1(11)=11$. There are $n!$ possible orders of star leaves. For $n\ge2$, returning to the same labelled star requires $c^t$ to fix the label in each slot, which occurs exactly when $n$ divides $t$. Each cycle consequently contains $n$ stars. The empty boundary is direct.

# Protected gaps and the exact depth distribution

The clock converts a temporal event into a labelled leaf condition. Define $F_n(t)=|\{w\in\mathcal Q_n:\tau(w)\le t\}|$.

[\[thm:depth\]]{#thm:depth label="thm:depth"} For $n\ge1$ and $0\le t\le n-1$, $$\label{eq:cdf}
 F_n(t)=\frac{(n+t)!}{2^t t!}.$$ The number at exact depth $t$ is $F_n(t)-F_n(t-1)$, with $F_n(-1)=0$. For $n=0$ the unique state has depth zero.

Every order-$k$ word is uniquely obtained by inserting the adjacent pair $kk$ into one of the $2k-1$ gaps of its order-$(k-1)$ predecessor. The condition $\tau\le t$ says that all labels $t+1,\ldots,n$ are leaves in the final tree. In the insertion construction a leaf can cease to be a leaf only by insertion into its internal pair gap, and it can never become a leaf again. Thus these internal gaps must remain unused.

For $k\le t$ there are $2k-1$ available gaps. Before inserting $k>t$, the $k-t-1$ protected pairs with labels $t+1,\ldots,k-1$ have distinct forbidden internal gaps. There are therefore $k+t$ available choices. Uniqueness of maximum-pair deletion means that multiplying these choices counts each word once: $$F_n(t)=
 \prod_{k=1}^{t}(2k-1)\prod_{k=t+1}^{n}(k+t)
 =\frac{(2t)!}{2^t t!}\,\frac{(n+t)!}{(2t)!}.$$ This is [\[eq:cdf\]](#eq:cdf){reference-type="eqref" reference="eq:cdf"}; subtraction of nested sublevel sets gives the exact layers. Empty products handle $t=0$.

The endpoints are $F_n(0)=n!$ and $F_n(n-1)=(2n-1)!!=|\mathcal Q_n|$, where the double factorial has its usual odd-factor product meaning. The latter carrier count also follows directly from unrestricted insertion. Equation [\[eq:cdf\]](#eq:cdf){reference-type="eqref" reference="eq:cdf"} is a cumulative count, not the population at exact depth $t$.

# Every target fibre and the one-step image

Tree labels and root-child order remain part of the state. In particular, the condition that $n$ is a root leaf is stronger than adjacency of $nn$ in the contour: the maximum pair is adjacent in every Stirling word.

[\[thm:inverse\]]{#thm:inverse label="thm:inverse"} Let $n\ge1$ and $y\in\mathcal Q_n$. If vertex $n$ is not a root child, then $T_n^{-1}(y)=\varnothing$. Otherwise write its root-child list as $$\label{eq:rootlist}
 (a_1,\ldots,a_p,\ n,\ b_1,\ldots,b_r).$$ For each $k=0,\ldots,r$, remove $n$, increment every surviving positive label, and insert a root child labelled one in its vacated slot, adopting exactly the first $k$ subtrees $b_1,\ldots,b_k$. These $r+1$ trees are all the predecessors, without repetition. Consequently $$\label{eq:fibre}
 |T_n^{-1}(y)|=
 \begin{cases}r+1,&\text{if \eqref{eq:rootlist} holds},\\
 0,&\text{otherwise}.\end{cases}$$ The maximum fibre has size $n$. Its targets are precisely the ordered stars whose first root child is $n$, numbering $(n-1)!$.

Every output has the inserted $n$ as a root leaf, so the negative case has no source. For each stated cut, label one is smaller than all adopted subtree labels. The reconstructed tree is increasing, and applying the forward splice returns [\[eq:rootlist\]](#eq:rootlist){reference-type="eqref" reference="eq:rootlist"} with all subtrees unchanged. The cuts are distinct because they give vertex one different numbers of children.

Conversely, any source has one in the root slot occupied by the target's $n$. The children promoted out of one occur consecutively immediately after $n$, followed by the old subsequent root children. Their boundary is exactly one cut in the suffix $(b_1,\ldots,b_r)$. There is no other choice in reconstructing the source: surviving labels and internal subtree orders are determined by the target. This proves completeness.

There are only $n$ nonroot vertices, so $r+1\le n$. Equality forces $r=n-1$, leaving no vertex before $n$ and no vertex below any root child. The target is therefore exactly a star with $n$ first. Every such star attains equality, and its remaining labels have $(n-1)!$ possible orders.

[\[cor:image\]]{#cor:image label="cor:image"} For $n\ge1$, $$\operatorname{im}T_n=\{y\in\mathcal Q_n:n\text{ is a root leaf}\},
 \qquad |\operatorname{im}T_n|=2^{n-1}(n-1)!.$$ At order zero the image, the sole fibre, and its unique maximizing target all have size one.

The cut $k=0$ proves sufficiency of the root-leaf condition. To count it, let $$R_m(z)=\sum_U z^{d_0(U)+1},\qquad R_0(z)=z,$$ where $U$ ranges over increasing plane trees with $m$ nonroot vertices and $d_0$ is the root outdegree. A tree with exponent $e=d_0+1$ has $2m+1$ total insertion gaps, of which $e$ are root gaps. Root insertion raises the exponent by one; every other insertion leaves it unchanged. Summing $e z^{e+1}+(2m+1-e)z^e$ gives $$R_{m+1}(z)=z(z-1)R_m'(z)+(2m+1)R_m(z).$$ Differentiating at $z=1$ yields $R_{m+1}'(1)=(2m+2)R_m'(1)$, hence $R_m'(1)=2^m m!$. Deleting the root leaf $n$ from a target records an arbitrary order-$(n-1)$ tree and one of its $d_0+1$ root gaps. The desired count is therefore $R_{n-1}'(1)$. The empty boundary is immediate.

# Exact controls and scope

The paper-local Python verifier constructs ordered child arrays, applies the tree surgery, and checks the literal word rule and the factor [\[eq:owner\]](#eq:owner){reference-type="eqref" reference="eq:owner"}. It builds each complete functional graph through $n=7$, derives tails by indegree peeling, and extracts cycles without using the proposed clock. Every reconstructed inverse set is compared with the entire graph predecessor set, including targets with no source. Two fresh runs agree byte for byte. Table [1](#tab:checks){reference-type="ref" reference="tab:checks"} records selected rows of this finite check, which supplements the all-order proofs.

::: {#tab:checks}
    $n$   states   image   recurrent   max. tail   max. fibre   maximizers
  ----- -------- ------- ----------- ----------- ------------ ------------
      0        1       1           1           0            1            1
      1        1       1           1           0            1            1
      2        3       2           2           1            2            1
      6    10395    3840         720           5            6          120
      7   135135   46080        5040           6            7          720

  : Complete finite controls: image and recurrence are counted separately; the last column counts all maximum-fibre targets.
:::

The retained results combine a label clock, protected insertion counts, and a target-side cut construction for the fixed schedule [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"}. They do not assert a closed formula for all iterated inverse sets or a new local tree move. The internal comparison also assigns no credit to generic commuting-idempotent bookkeeping or generic ordered-tree inverse cuts. The source search was bounded, and six unavailable historical manuscripts in the project (P51--P56) could not be inspected. Neither finite verification nor a search non-hit establishes priority. The manuscript remains `HOLD_EXTERNAL` pending a broader owner assessment and the separate paper-review process.
