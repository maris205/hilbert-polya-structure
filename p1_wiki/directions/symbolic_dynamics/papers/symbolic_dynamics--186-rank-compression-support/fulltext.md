---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--186-rank-compression-support"
canonical_tex: "symbolic_dynamics/papers/186-rank-compression-support/main.tex"
canonical_pdf: "symbolic_dynamics/papers/186-rank-compression-support/main.pdf"
source_sha256: "e7f407c5200e2e308885d61bd1328c8e3d20f57e50f219ab5ad104609cee0394"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Gap Erosion and All-Time Fibres for Rank-Compression Support Dynamics

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/186-rank-compression-support>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/186-rank-compression-support/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/186-rank-compression-support/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/186-rank-compression-support/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/186-rank-compression-support/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Order a subset $A=\{a_0<\cdots<a_{k-1}\}$ of $\{0,\ldots,n-1\}$, subtract the rank $j$ from $a_j$, discard multiplicity, and iterate the resulting support map. We prove that at time $t$ each original consecutive gap $g$ contributes $g-t$ exactly when $g>t$, and otherwise disappears. This gives an exact pointwise clock and all basins; for $n\ge2$, there is a unique state of depth $n-1$. A nonempty set $B$ is in the time-$t$ image exactly when $\max B+t(|B|-1)<n$. Every such target has a coefficient-sum fibre formula in which arbitrary short-gap words occupy the slots around forced long gaps; at one step it reduces to $\binom{n-\max B}{|B|}$, and the first image has $F_{n+2}$ states. A bounded-gap generating function gives every depth population. Classical strict/weak sequence shifts, stars and bars, beta sets, and Fibonacci summation receive no contribution credit. The retained conjunction is [owner\_amber]{.smallcaps}; circulation remains [hold\_external]{.smallcaps}.
author:
- Anonymous
bibliography:
- references.bib
title: |
  Gap Erosion and All-Time Fibres for\
  Rank-Compression Support Dynamics
```

## Markdown 正文

# The map and the subtraction boundary

Let $[n]_0=\{0,\ldots,n-1\}$ and $\mathcal X_n=2^{[n]_0}$. For $A=\{a_0<\cdots<a_{k-1}\}$ define $$\label{eq:map}
 T_n(A)=\operatorname{supp}\{a_j-j:0\le j<k\},\qquad T_n(\varnothing)=\varnothing,$$ where $\operatorname{supp}$ discards multiplicity. The integers $a_j-j$ are weakly increasing and lie in $[n]_0$, so this is a total finite self-map.

The strict-to-weak sequence shift behind $a_j-j$ and the resulting stars-and-bars identities are classical [@Stanley2012]. Beta sets are also standard partition coordinates; see, for example, their use in core partition theory [@Fayers2023]. We assign those encodings, bounded compositions, Fibonacci identities, and generic functional-graph bookkeeping no contribution credit. The scoped residual is only the autonomous support iteration [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"}, its all-time gap law, and the simultaneous pointwise/image/every-target inverse atlas below. A bounded search found no source stating that literal iterative conjunction. This non-hit is neither novelty nor priority evidence.

Internally, P163 acts on families by complemented shadows, P169 transfers last occurrences between set-partition blocks, and P179 randomly isolates labels through commuting idempotents. None is [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"}; nevertheless their shadow, partition, and inverse vocabulary is fully subtracted. P100's digit-erasure clock and P178's image-tower bookkeeping likewise receive no separation credit.

For nonempty $A$, put $m(A)=a_0$ and define its positive gap word $$\label{eq:gaps}
 g(A)=(g_1,\ldots,g_{k-1}),\qquad g_j=a_j-a_{j-1}.$$ The empty word is allowed. Given a positive word $g$, let $E_t(g)$ be the subsequence $(g_j-t:g_j>t)$, in the original order.

# Pointwise dynamics and the sharp clock

[\[thm:gap\]]{#thm:gap label="thm:gap"} For every $A\in\mathcal X_n$ and $t\ge0$, the empty set remains empty. If $A$ is nonempty, then $\min T_n^t(A)=m(A)$ and $$\label{eq:gap-iterate}
             g(T_n^t(A))=E_t(g(A)).$$ Equivalently, start at $m(A)$ and cumulatively add, in order, the terms $g_j-t$ for which $g_j>t$.

The recurrent states are precisely $\varnothing$ and the $n$ singletons. Writing $\tau(A)$ for entrance time into this fixed set, $$\label{eq:clock}
 \tau(A)=
 \begin{cases}
 0,&|A|\le1,\\
 \max_{1\le j<|A|}g_j,&|A|\ge2.
 \end{cases}$$ For $n\ge2$ the global height is $n-1$, attained uniquely by $\{0,n-1\}$. The basin of $\{m\}$ has size $2^{n-m-1}$, and the empty basin has size one.

Put $b_j=a_j-j$. Consecutive differences in the weakly increasing list $(b_j)$ satisfy $$\label{eq:difference}
                 b_j-b_{j-1}=g_j-1.$$ Taking support deletes exactly the zero differences. Deleting repetitions does not merge positive increments: it retains, in their old order, exactly the positive values $g_j-1$. The minimum remains $b_0=a_0$. One application therefore replaces the gap word by $E_1(g)$, and induction proves [\[eq:gap-iterate\]](#eq:gap-iterate){reference-type="eqref" reference="eq:gap-iterate"}.

If $|A|\ge2$, all gaps have disappeared at time $\max g_j$, while a gap equal to that maximum is still positive one epoch earlier. This proves the least-time formula [\[eq:clock\]](#eq:clock){reference-type="eqref" reference="eq:clock"} and excludes nonfixed recurrence. A gap is at most $n-1$, with equality only when two consecutive selected elements are $0,n-1$; no third selected element can then occur. This proves the sharp and unique extremal statement. Finally, a nonempty orbit preserves its minimum and ends at that singleton. The subsets with minimum $m$ are $\{m\}\cup C$ with $C\subseteq\{m+1,\ldots,n-1\}$, giving the basin count.

# All-time images and target-local fibres

For $t\ge0$, write $$\label{eq:short-series}
 S_t(z)=z+\cdots+z^t,$$ with $S_0(z)=0$.

[\[thm:fibre\]]{#thm:fibre label="thm:fibre"} Fix $t\ge0$. The empty target has the unique source $\varnothing$. A nonempty target $B=\{b_0<\cdots<b_r\}$ occurs at time $t$ if and only if $$\label{eq:image-condition}
                  b_r+tr<n.$$ For every $B$ (with a negative upper limit interpreted as zero), $$\label{eq:fibre}
 |(T_n^t)^{-1}(B)|=
 \sum_{s=0}^{n-1-b_0-(b_r-b_0)-tr}
 [z^s]\bigl(1-S_t(z)\bigr)^{-(r+1)}.$$ Consequently, $$\label{eq:image-size}
 |\operatorname{im}T_n^t|=1+\sum_{r\ge0}\binom{n-tr}{r+1},$$ where impossible binomial coefficients vanish. At one step, $$\begin{aligned}
 |T_n^{-1}(B)|&=\binom{n-\max B}{|B|}\quad(B\ne\varnothing),
 \label{eq:first-fibre}\\
 |\operatorname{im}T_n|&=F_{n+2},                                      \label{eq:fibonacci}\end{aligned}$$ for $F_0=0,F_1=1$.

Let $h_i=b_i-b_{i-1}$ for $1\le i\le r$. By Theorem [\[thm:gap\]](#thm:gap){reference-type="ref" reference="thm:gap"}, a source mapping to $B$ at time $t$ has the unique gap factorisation $$\label{eq:factorization}
 U_0,(h_1+t),U_1,(h_2+t),\ldots,(h_r+t),U_r,$$ where each $U_i$ is an arbitrary ordered word with letters in $\{1,\ldots,t\}$. Conversely every such factorisation yields $B$: the $U_i$ letters disappear and the distinguished gaps lose $t$.

The distinguished gaps consume total span $$\sum_{i=1}^r(h_i+t)=b_r-b_0+tr.$$ The available span after the invariant minimum $b_0$ is $n-1-b_0$. Each short-gap slot has ordinary generating function $(1-S_t(z))^{-1}$, so summing its $(r+1)$-slot coefficients through the remaining span proves [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"}. With every $U_i$ empty, feasibility is exactly [\[eq:image-condition\]](#eq:image-condition){reference-type="eqref" reference="eq:image-condition"}; this also proves sufficiency.

For fixed $r$, condition [\[eq:image-condition\]](#eq:image-condition){reference-type="eqref" reference="eq:image-condition"} chooses an $(r+1)$-set from $\{0,\ldots,n-1-tr\}$, which proves [\[eq:image-size\]](#eq:image-size){reference-type="eqref" reference="eq:image-size"}. If $t=1$, then $S_1(z)=z$ and the hockey-stick identity reduces [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"} to [\[eq:first-fibre\]](#eq:first-fibre){reference-type="eqref" reference="eq:first-fibre"}. Finally, $1+\sum_{r\ge0}\binom{n-r}{r+1}=F_{n+2}$, proving [\[eq:fibonacci\]](#eq:fibonacci){reference-type="eqref" reference="eq:fibonacci"}.

Formula [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"} is target-local and remains informative after the first image: its $r+1$ factors distinguish the short-gap words before, between, and after the long gaps that survive to $B$. In particular, it is not inferred by dividing the carrier size by the image size.

# Every depth population

[\[prop:depth\]]{#prop:depth label="prop:depth"} Let $C_n(h)=|\{A\in\mathcal X_n:\tau(A)\le h\}|$ and put $Q_h(z)=(1-S_h(z))^{-1}$. For every $h\ge0$, $$\label{eq:depth-cdf}
 C_n(h)=1+\sum_{s=0}^{n-1}(n-s)[z^s]Q_h(z).$$ Thus the exact depth-$h$ population is $C_n(h)-C_n(h-1)$ for $h\ge1$, while $C_n(0)=n+1$.

Besides the empty set, choose the minimum $m$ and then an arbitrary ordered gap word with letters at most $h$. Such a word of total span $s$ is counted by $[z^s]Q_h(z)$ and permits exactly $n-s$ minima $m\in\{0,\ldots,n-1-s\}$. The clock formula says precisely that these are the states of depth at most $h$. Summation proves [\[eq:depth-cdf\]](#eq:depth-cdf){reference-type="eqref" reference="eq:depth-cdf"}; at $h=0$ only the empty gap word remains.

For orientation, at $n=4$ the arrows include $$\{0,3\}\longmapsto\{0,2\}\longmapsto\{0,1\}
 \longmapsto\{0\},$$ which witnesses the sharp height. At $n=18$, exhaustive evaluation gives 6,765 first-image targets, 19 fixed states, maximum one-step fibre 2,002, and the unique depth-17 state $\{0,17\}$.

# Exact control, limitations, and declarations

The paper-local standard-library verifier exhausts all $2^n$ subsets through $n=18$. It compares literal iteration with [\[eq:gap-iterate\]](#eq:gap-iterate){reference-type="eqref" reference="eq:gap-iterate"}, checks the least pointwise clock, reconstructs every time-$t$ image and every target fibre through [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"}, and checks [\[eq:depth-cdf\]](#eq:depth-cdf){reference-type="eqref" reference="eq:depth-cdf"} independently. Finite computation is falsification pressure, not proof.

The rule depends on the ambient linear order and on discarding multiplicity; neither feature is invariant under arbitrary relabelling. We do not treat random updates, asymptotic limit shapes, or a classification of analogous multiset maps. The owner search was bounded, and the elementary nature of the rank subtraction leaves a live ownership risk. The status is therefore [owner\_amber / hold\_external]{.smallcaps}; no circulation or priority claim is authorized.

#### Data availability.

No external data were used. The exact verifier and canonical transcript accompany the source.

#### Ethics statement.

The work uses no human participants, animals, personal data, or experiments requiring ethics approval.

#### CRediT author statement.

The anonymous author performed conceptualization, formal analysis, software, validation, and writing.

#### Competing interests.

The author declares no competing interests.

#### Funding.

No external funding is declared.

#### AI-use statement.

Generative AI assisted drafting and code generation. All mathematical, bibliographic, and artifact claims require human verification before any external use.
