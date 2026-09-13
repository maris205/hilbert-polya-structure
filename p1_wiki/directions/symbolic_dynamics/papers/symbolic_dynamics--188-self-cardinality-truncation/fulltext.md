---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--188-self-cardinality-truncation"
canonical_tex: "symbolic_dynamics/papers/188-self-cardinality-truncation/main.tex"
canonical_pdf: "symbolic_dynamics/papers/188-self-cardinality-truncation/main.pdf"
source_sha256: "f08712d1b1e43f707c1254ebf791724727e9387a5e0794dae3b5c40d4874ab39"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Self-Cardinality Truncation of Finite Sets: Rank Descent, Sharp Depth, and Exact Fibres

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/188-self-cardinality-truncation>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/188-self-cardinality-truncation/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/188-self-cardinality-truncation/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/188-self-cardinality-truncation/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/188-self-cardinality-truncation/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For $A\subseteq[n]$, intersect $A$ with the initial segment whose length is the current cardinality, and feed the result back into the same rule. We derive a pointwise all-time iterate from a scalar rank recursion and prove that every orbit ends at the longest initial segment contained in the source. The $n+1$ initial segments are the only recurrent states. For $n\geq2$, the sharp transient height is $n-1$, attained uniquely by $\{2,\ldots,n\}$. Every terminal basin has a closed power-of-two size. We also count every labelled target fibre at every time by a chain of binomial factors, obtain a necessary and sufficient first-image inequality, and show that the first image contains exactly the Fibonacci number $F_{n+2}$ of states; the empty target has $F_{n+1}$ one-step predecessors and is the unique largest fibre for $n\geq2$. Exhaustive finite checks are counterexample pressure, not proof or novelty evidence. Rank feedback and binomial--Fibonacci identities receive no contribution credit, and the paper remains `HOLD_EXTERNAL` pending a complete owner audit.
author:
- Anonymous
bibliography:
- references.bib
title: |
  Self-Cardinality Truncation of Finite Sets:\
  Rank Descent, Sharp Depth, and Exact Fibres
```

## Markdown 正文

# Definition and contribution boundary

Write $[k]=\{1,\ldots,k\}$ and $[0]=\varnothing$. On the power set of $[n]$, including $n=0$, define $$\label{eq:T}
 T_n(A)=A\cap[|A|].$$ This is a synchronous finite map in the general language of finite parallel dynamics [@AledoMartinezValverde2015]. The operation couples a set to its own cardinality; the cutoff is recomputed after every step.

Initial-segment notation and monotone set deletion receive zero contribution credit. The same is true of rank recursions and classical binomial identities for Fibonacci numbers [@GrahamKnuthPatashnik1994]. Internally, this rule is neither the prefix-diversity feedback of P185 nor the rank-subtraction support map of P186: it acts on one subset, never reorders elements, and its scalar clock is self-cardinality. A bounded literal and semantic search did not return the full rule and theorem package. That non-hit is not a novelty or priority claim.

For $A\subseteq[n]$, define the rank function $$\label{eq:rank}
 r_A(k)=|A\cap[k]|,$$ and the scalar sequence $$\label{eq:k}
 k_0=|A|,\qquad k_{t+1}=r_A(k_t).$$ Let $$\label{eq:rho}
 \rho(A)=\max\{r:[r]\subseteq A\}$$ be the length of the initial run contained in $A$.

# All-time normal form and endpoint

[\[thm:iterate\]]{#thm:iterate label="thm:iterate"} For every $t\geq1$, $$\label{eq:iterate}
 T_n^t(A)=A\cap[k_{t-1}].$$ The sequence $(k_t)$ decreases to $\rho(A)$, and $$\label{eq:endpoint}
 T_n^t(A)=[\rho(A)]$$ for all sufficiently large $t$.

The case $t=1$ is [\[eq:T\]](#eq:T){reference-type="eqref" reference="eq:T"}. If [\[eq:iterate\]](#eq:iterate){reference-type="eqref" reference="eq:iterate"} holds at time $t$, then its cardinality is $r_A(k_{t-1})=k_t$; intersecting it with $[k_t]$ gives $A\cap[k_t]$, because $k_t\leq k_{t-1}$. This proves the formula by induction.

The sequence is nonincreasing because $r_A(k)\leq k$. It never falls below $\rho(A)$, since $[\rho(A)]\subseteq A$. If $k>\rho(A)$, the missing element $\rho(A)+1$ lies in $[k]$, so $r_A(k)\leq k-1$. Therefore the scalar sequence reaches and then remains at $\rho(A)$. Formula [\[eq:iterate\]](#eq:iterate){reference-type="eqref" reference="eq:iterate"} now gives [\[eq:endpoint\]](#eq:endpoint){reference-type="eqref" reference="eq:endpoint"}.

[\[cor:terminal\]]{#cor:terminal label="cor:terminal"} The fixed and recurrent states are exactly $$\label{eq:fixed}
 \varnothing,[1],[2],\ldots,[n].$$ For $0\leq r\leq n$, the number of sources whose endpoint is $[r]$ is $$\label{eq:basin}
 \#\{A:T_n^\infty(A)=[r]\}=
 \begin{cases}
 2^{n-r-1},&r<n,\\
 1,&r=n.
 \end{cases}$$

Theorem [\[thm:iterate\]](#thm:iterate){reference-type="ref" reference="thm:iterate"} makes every recurrent state fixed. A set is fixed only if a set of size $k$ is contained in $[k]$, which forces it to equal $[k]$. Endpoint $[r]$ means that $A$ contains $[r]$, omits $r+1$ when $r<n$, and makes arbitrary choices above $r+1$, proving [\[eq:basin\]](#eq:basin){reference-type="eqref" reference="eq:basin"}.

# Sharp transient height

[\[thm:height\]]{#thm:height label="thm:height"} For $n\geq2$, the maximum tail is $n-1$ and its unique attaining state is $$\label{eq:deepest}
 A_\star=\{2,3,\ldots,n\}.$$ For $n=0,1$, every state is fixed.

Unless $A$ is fixed, $T_n(A)$ is a proper subset of $A$: a set of size $k$ contained in $[k]$ would be exactly $[k]$. Along an orbit ending at $[\rho(A)]$, each transient step therefore lowers cardinality by at least one, and the tail is at most $|A|-\rho(A)$. If $\rho(A)=0$, omission of $1$ gives $|A|\leq n-1$. If $\rho(A)>0$ and $A$ is nonfixed, omission of $\rho(A)+1$ gives $|A|-\rho(A)\leq n-1-\rho(A)<n-1$. This proves the upper bound and shows that equality can only occur when $\rho(A)=0$ and $|A|=n-1$, which uniquely forces [\[eq:deepest\]](#eq:deepest){reference-type="eqref" reference="eq:deepest"}.

Starting from $A_\star$, each update removes its current largest element: $$\{2,\ldots,n\}\to\{2,\ldots,n-1\}\to\cdots\to\{2\}\to\varnothing.$$ There are $n-1$ arrows, so the bound is sharp. The two small carriers are immediate.

# Every-target inverse law

For a target $B$, put $b=|B|$ and $M(B)=\max B$, with $M(\varnothing)=0$. We use the convention $\binom uv=0$ unless $0\leq v\leq u$.

[\[thm:alltime-fibre\]]{#thm:alltime-fibre label="thm:alltime-fibre"} Fix $t\geq1$ and set $k_t=b$. Then $$\label{eq:alltime-fibre}
 |(T_n^t)^{-1}(B)|=
 \sum_{\substack{n\geq k_0\geq k_1\geq\cdots\geq k_{t-1}\\
                         k_{t-1}\geq\max\{b,M(B)\}}}
 \binom{n-k_0}{k_0-k_1}
 \prod_{j=1}^{t-1}
 \binom{k_{j-1}-k_j}{k_j-k_{j+1}}.$$ For $t=1$, the first binomial is read as $\binom{n-k_0}{k_0-b}$ and the product is empty. At time zero every target has its single identity predecessor. At every time, $$\label{eq:alltime-mass}
 \sum_{B\subseteq[n]}|(T_n^t)^{-1}(B)|=2^n.$$ For $t\geq n-1$, the only nonempty fibres are the terminal fibres in [\[eq:basin\]](#eq:basin){reference-type="eqref" reference="eq:basin"}.

Every source $A$ determines the unique rank chain [\[eq:k\]](#eq:k){reference-type="eqref" reference="eq:k"}. Fixing its values $k_0,\ldots,k_{t-1}$ partitions $[n]$ into the disjoint intervals $$(k_0,n],\ (k_1,k_0],\ldots,\ (k_{t-1},k_{t-2}],\ [k_{t-1}].$$ The intermediate intervals are absent when $t=1$. The first interval must contain $k_0-k_1$ source elements. For $1\leq j<t$, the interval $(k_j,k_{j-1}]$ must contain $k_j-k_{j+1}$ source elements. Inside the final interval the source is forced to equal $B$, which also requires $k_{t-1}\geq M(B)$. Independent choices in the preceding intervals give the product in [\[eq:alltime-fibre\]](#eq:alltime-fibre){reference-type="eqref" reference="eq:alltime-fibre"}. Conversely, every such choice realizes exactly the displayed rank chain and target, so neither omission nor overcounting is possible. Summing over targets partitions all $2^n$ sources and proves [\[eq:alltime-mass\]](#eq:alltime-mass){reference-type="eqref" reference="eq:alltime-mass"}. The terminal claim follows from Theorem [\[thm:height\]](#thm:height){reference-type="ref" reference="thm:height"} and Corollary [\[cor:terminal\]](#cor:terminal){reference-type="ref" reference="cor:terminal"}.

[\[thm:fibre\]]{#thm:fibre label="thm:fibre"} Every labelled target $B\subseteq[n]$ has $$\label{eq:fibre}
 |T_n^{-1}(B)|=
 \sum_{k=\max\{b,M(B)\}}^{\lfloor(n+b)/2\rfloor}
 \binom{n-k}{k-b},$$ where an empty sum is zero. Equivalently, $$\label{eq:imagecriterion}
 B\in\operatorname{im}T_n\quad\Longleftrightarrow\quad
 2M(B)\leq n+|B|.$$ The formula conserves all source mass: $$\label{eq:mass}
 \sum_{B\subseteq[n]}|T_n^{-1}(B)|=2^n.$$

Set $t=1$ and $k_0=k$ in Theorem [\[thm:alltime-fibre\]](#thm:alltime-fibre){reference-type="ref" reference="thm:alltime-fibre"}. Equivalently, fix a source cardinality $k$. The equality $T_n(A)=B$ requires $B\subseteq[k]$, no other source elements in $[k]$, and exactly $k-b$ source elements chosen from $\{k+1,\ldots,n\}$. These conditions contribute $\binom{n-k}{k-b}$ and are possible exactly when $$k\geq\max\{b,M(B)\},\qquad k-b\leq n-k.$$ Summing over $k$ gives [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"}. Since $M(B)\geq b$ for nonempty $B$ and both vanish for the empty set, the range is nonempty exactly under [\[eq:imagecriterion\]](#eq:imagecriterion){reference-type="eqref" reference="eq:imagecriterion"}. Finally, the construction partitions all sources by their unique target, proving [\[eq:mass\]](#eq:mass){reference-type="eqref" reference="eq:mass"}; this is also the time-one case of [\[eq:alltime-mass\]](#eq:alltime-mass){reference-type="eqref" reference="eq:alltime-mass"}.

Let $F_0=0,F_1=1$, and $F_{j+1}=F_j+F_{j-1}$.

[\[cor:fibonacci\]]{#cor:fibonacci label="cor:fibonacci"} For every $n\geq0$, $$\label{eq:imagecount}
 |\operatorname{im}T_n|=F_{n+2},\qquad |T_n^{-1}(\varnothing)|=F_{n+1}.$$

For the empty target, [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"} becomes the standard identity $\sum_k\binom{n-k}{k}=F_{n+1}$. For the image, targets of size $b$ satisfy [\[eq:imagecriterion\]](#eq:imagecriterion){reference-type="eqref" reference="eq:imagecriterion"} exactly when they lie in $[\lfloor(n+b)/2\rfloor]$. Hence $$|\operatorname{im}T_n|=\sum_{b=0}^n
 \binom{\lfloor(n+b)/2\rfloor}{b}=F_{n+2}.$$ Indeed, the terms with $n-b=2j$ and $n-b=2j+1$ are respectively $\binom{n-j}{j}$ and $\binom{n-j-1}{j}$. Their sums are the standard binomial forms of $F_{n+1}$ and $F_n$, so their total is $F_{n+2}$.

[\[cor:extremal\]]{#cor:extremal label="cor:extremal"} For each $0\leq b\leq n$, the first image contains exactly $$\label{eq:image-layer}
 \binom{\lfloor(n+b)/2\rfloor}{b}$$ targets of cardinality $b$. If $n\geq2$, the empty target is the unique largest one-step fibre, of size $F_{n+1}$. At $n=1$, both fibres have size one.

Criterion [\[eq:imagecriterion\]](#eq:imagecriterion){reference-type="eqref" reference="eq:imagecriterion"} says that a size-$b$ target may choose its elements freely from $[\lfloor(n+b)/2\rfloor]$, proving [\[eq:image-layer\]](#eq:image-layer){reference-type="eqref" reference="eq:image-layer"}. If $B$ is nonempty, set $j=k-b$ in [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"}. Dropping the lower restriction $k\geq M(B)$ gives $$|T_n^{-1}(B)|\leq
 \sum_{j\geq0}\binom{n-b-j}{j}=F_{n-b+1}\leq F_n.$$ For $n\geq2$, this is strictly smaller than the empty fibre $F_{n+1}$. The carrier $n=1$ is checked directly.

The rank recursion proves the forward theorem, while the inverse theorem partitions sources into nested rank intervals. Neither is inferred from the exhaustive verifier. The finite control checks all subsets through $n=18$, including $n=0$, and separately checks all-time fibres in smaller boxes, but cannot certify an all-parameter theorem or an ownership claim. External circulation remains prohibited.
