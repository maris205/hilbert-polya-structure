---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--49-transient-phase-allocation-tree-shifts"
canonical_tex: "symbolic_dynamics/papers/49-transient-phase-allocation-tree-shifts/paper/main.tex"
canonical_pdf: "symbolic_dynamics/papers/49-transient-phase-allocation-tree-shifts/main.pdf"
source_sha256: "d97d3bc78e168dc5bc4ca7414660bc3d6f5b15e99c598308b3e3235a23958925"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Hausdorff Dimension for Complete Cyclic Markov Hom Tree-Shifts with an Unrestricted One-Level Feeder or Canonical Unrestricted $L$-Level Forced Chains

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/49-transient-phase-allocation-tree-shifts>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/49-transient-phase-allocation-tree-shifts/paper/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/49-transient-phase-allocation-tree-shifts/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/49-transient-phase-allocation-tree-shifts/PAPER_PLAN.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/49-transient-phase-allocation-tree-shifts/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We determine Hausdorff dimension for two reducible families of Markov hom tree-shifts built over a complete cyclic core. The core has phase sizes $a_0,\ldots,a_{p-1}$ on the rooted ordered $d$-ary tree. Its elementary cylinder calculation is used only as a supporting ingredient. Adding one unrestricted transient root produces an exact finite max--min problem: the $d$ children are allocated among the $p$ phases by an integer composition, and the least depth residue determines the dimension of each allocation. The spectral mean $p^{-1}\sum_j\log a_j$ bounds every allocation, with equality precisely when an associated circular convolution is constant. Consequently $p\mid d$ is always sufficient for saturation and is necessary under a full nonzero Fourier-support hypothesis; a period-four example shows why that hypothesis cannot be omitted. For the canonical unrestricted $L$-level forced chain, the exact allocation denominator is $d^L$. Its optimized dimensions are monotone in $L$ and lie within $p\max_j H_j/d^L$ of the spectral mean. A four-state binary example has cyclic-core dimension $\log 2/3$ but full dimension $\log 2/2$, so a maximum-over-cyclic-essential-components rule fails for Hausdorff dimension. The proofs use exact cylinder counts and a compatible uniform measure; separate exact-arithmetic implementations are used only for reproducibility and falsification controls.
author:
- Anonymous Authors
bibliography:
- references.bib
title: |
  Hausdorff Dimension for Complete Cyclic Markov Hom Tree-Shifts\
  with an Unrestricted One-Level Feeder or Canonical Unrestricted $L$-Level Forced Chains
```

## Markdown 正文

# Introduction {#sec:introduction}

Markov constraints on a rooted tree amplify local choices very differently from constraints on a one-dimensional shift. A decision made at a vertex is replicated across exponentially many descendants, while the natural metric assigns its scale through the size of an entire finite tree. In this setting, even one strictly transient graph state can affect a boundary-weighted dimension: its $d$ children can enter different cyclic phases, and the chosen phase proportions persist through exponentially large descendant subtrees. The phenomenon studied here is this finite integer allocation, not arbitrary reducibility.

Tree-shifts of finite type and Markov hom tree-shifts have an established entropy theory; see, among others, @aubrunBeal2012, @petersenSalama2018, and @petersenSalama2020. Reducible topological entropy need not be the maximum of the component entropies [@banEtAl2021; @banEtAl2022]. More recently, @banLaiWu2025 developed Hausdorff-dimension theory for irreducible Markov hom tree-shifts in the metric used below and identified the general reducible case as a separate problem. These results set the boundary of the present article: we neither claim the component-failure mechanism for topological entropy nor solve the general reducible Hausdorff problem.

Our core is deliberately rigid. Its alphabet is partitioned into $p$ nonempty phases $V_0,\ldots,V_{p-1}$, and every label in $V_j$ may be followed by every label in $V_{j+1}$, with indices modulo $p$. Put $a_j=|V_j|$ and $c_j=\log a_j$. For the complete core, direct counting gives the supporting quantity $$H_j(c)=\frac{d-1}{d^p-1}
 \sum_{t=0}^{p-1}d^{p-1-t}c_{j-t}.$$ The core dimension is $\min_j H_j(c)$. We then add one transient state $r$ that sees every core label and has no return edge. Fixing the phases of its ordered children gives a composition $m=(m_0,\ldots,m_{p-1})$ of $d$ and the dimension $$D_1(m;c)=\min_j\frac1d\sum_s m_s H_{s+j}(c).$$ There are only finitely many phase assignments, so maximizing this expression over integer compositions gives the dimension of the full one-level shift. This order of operations matters: the minimum over depth residues remains inside the integer optimization.

The complete-core calculation above is an ingredient rather than a novelty claim about irreducible theory. The residual contributions are as follows.

1.  We derive the exact phase-allocation max--min for the unrestricted one-level feeder. The proof includes both Hausdorff bounds, the finite-union step, and the fact that concentrated compositions dominate all core-root strata. The same argument covers only explicitly declared finite sets of one-level compositions.

2.  We identify the exact saturation arithmetic. Every allocation lies below the spectral mean $\bar c=p^{-1}\sum_jc_j$, and equality is equivalent to constancy of a circular convolution, or equivalently of shifted integer products. Uniform allocation proves $p\mid d$ sufficient. The converse is stated only when every nonzero Fourier mode of $c$ is nonzero; an explicit $p=4,d=2$ witness rejects an unconditional converse.

3.  We obtain closed formulas for two phases and extend the allocation to the canonical unrestricted $L$-level forced chain. The exact denominator is $d^L$, the optimized dimensions are monotone, and a balanced composition gives an explicit $O(d^{-L})$ distance to $\bar c$. Restricted multilevel variants are mentioned only with a stated balanced-access condition.

4.  We exhibit a four-state binary shift for which the sole cyclic essential strongly connected component has dimension $\log 2/3$, whereas the full reducible shift has dimension $\log 2/2$. Thus the cyclic-essential-SCC maximum fails. Exact programs replay the identities and negative controls, but no finite census substitutes for the universal proofs.

The proof strategy is elementary but sensitive to indices and metric scales. We first identify balls with finite-tree cylinders and prove a matching cylinder-cover/Frostman lemma. We then compute periodic weighted limits with the backward index $j-t$. Only after the exact one-level optimizer is proved do we study equality through a circulant operator and discrete Fourier modes. Finally, the map $m\mapsto dm$ embeds the depth-$L$ allocation grid in the depth-$(L+1)$ grid, while balanced integer compositions control the remaining gap.

The scope is narrow throughout. We assume positive phase sizes, complete phase-to-phase blocks, and no return to a feeder. Arbitrary finite strictly transient feeder shapes, incomplete blocks, communicating cyclic components, and nontransient reuse are excluded. Section [2](#sec:related){reference-type="ref" reference="sec:related"} fixes the source boundary; Sections [3](#sec:setting){reference-type="ref" reference="sec:setting"}--[7](#sec:deep){reference-type="ref" reference="sec:deep"} prove the main results; Section [8](#sec:example){reference-type="ref" reference="sec:example"} gives the four-state application and exact verification; and the appendices record endpoints and reproducibility.

# Related work and source boundary {#sec:related}

#### Tree-shifts and entropy.

The terminology and finite-type viewpoint for symbolic dynamics on regular rooted trees were developed in foundational work including @aubrunBeal2012. Entropy on regular trees differs from the amenable one-dimensional setting because boundary levels have non-negligible density; the normalization and resulting growth questions were studied by @petersenSalama2018 [@petersenSalama2020]. We use this background only for context. Every counting identity needed for the present dimension formulas is derived below.

#### Reducibility.

For topological entropy, @banEtAl2021 analyzed structural effects in tree-shifts of finite type, and @banEtAl2022 compared finite-type shifts over $\mathbb Z$ and trees. In particular, reducibility on a tree can produce entropy behavior not captured by simply maximizing over irreducible components. Accordingly, the broad conceptual observation that a transient or reducible part can defeat a component maximum is not a contribution of this article. Our residual statement concerns Hausdorff dimension in a specific tree metric and supplies matched upper and lower bounds for a frozen complete cyclic family.

#### Hausdorff dimension.

@banLaiWu2025 introduced the metric used in [\[def:metric\]](#def:metric){reference-type="ref" reference="def:metric"}, developed irreducible Hausdorff-dimension theory through a nonlinear Perron--Frobenius variational formulation, and discussed a spectral upper bound. Their work is the irreducible owner and leaves the general not-necessarily-irreducible dimension problem apart from that theory. We import the metric and object vocabulary, but no irreducible equality clause or spectral upper bound. The complete cyclic formula in [\[thm:core\]](#thm:core){reference-type="ref" reference="thm:core"} follows instead from exact cylinder counts and is used as a supporting calculation.

\@P0.20P0.22P0.25P0.25@ Source & Object class & Quantity and principal role & Boundary relative to this article\
@banEtAl2021 [@banEtAl2022] & Reducible tree-shifts of finite type & Topological entropy and component structure & Own the analogous component-failure phenomenon for entropy; do not supply the Hausdorff formula below.\
@banLaiWu2025 & Irreducible Markov hom tree-shifts & Hausdorff dimension in the rooted-tree metric; nonlinear variational theory & Own the metric and irreducible theory; no version-sensitive equality clause is imported here.\
Present article & Complete cyclic core with the unrestricted one-level feeder or the canonical unrestricted $L$-level forced chain & Exact Hausdorff phase-allocation optimizer, saturation arithmetic, and convergence & Explicit finite-composition one-level variants only; restricted multilevel variants require balanced access.\

The source search underlying this positioning was bounded and claim-shaped. It found no exact collision with the transient phase-allocation optimizer, but such a search cannot establish priority. We therefore use no "first" or exhaustive-novelty language. The precise residual scope is: complete cyclic cores with the unrestricted one-level feeder and the canonical unrestricted $L$-level forced chain; only declared finite-composition one-level variants; and restricted multilevel families only under an explicit balanced-access hypothesis. Arbitrary finite strictly transient feeder shapes and arbitrary reducible matrices are outside the claims.

# Setting, metric, and exact cylinders {#sec:setting}

Fix an integer $d\geq2$ and write $\Sigma=\{0,\ldots,d-1\}$. The rooted ordered $d$-ary tree is $$\mathbb T_d=\Sigma^*=\bigcup_{n\geq0}\Sigma^n,
 \qquad
 \Delta_n=\bigcup_{\ell=0}^n\Sigma^\ell,
 \qquad
 |\Delta_n|=\frac{d^{n+1}-1}{d-1}.$$ The empty word is the root, and the children of $w$ are $wi$, $i\in\Sigma$. For a finite alphabet $\mathcal A$ and a zero--one matrix $M=(M_{uv})_{u,v\in\mathcal A}$, the associated Markov hom tree-shift is $$T_M=\bigl\{x\in\mathcal A^{\mathbb T_d}:M_{x_w,x_{wi}}=1
       \text{ for every }w\in\mathbb T_d,\ i\in\Sigma\bigr\}.
 \label{eq:markov-shift}$$ A depth-$n$ pattern is a labeling of $\Delta_n$ satisfying these constraints; its cylinder is the set of configurations extending it.

[\[def:metric\]]{#def:metric label="def:metric"} For $x,y\in\mathcal A^{\mathbb T_d}$, put $$\kappa(x,y)=\sup\bigl(\{\,|\Delta_n|:
 x|_{\Delta_n}=y|_{\Delta_n}\,\}\cup\{0\}\bigr)$$ and set $D(x,y)=\exp(-\kappa(x,y))$, with $D(x,x)=0$. We use the restriction of $D$ to every shift and stratum below. Also set $\Delta_{-1}=\varnothing$ and $|\Delta_{-1}|=0$.

This is the metric of @banLaiWu2025. Its endpoint convention is useful: for $n\geq0$ and $$\mathrm e^{-|\Delta_n|}\leq r<\mathrm e^{-|\Delta_{n-1}|},
 \label{eq:ball-window}$$ the closed $D$-ball of radius $r$ around a point is exactly its depth-$n$ cylinder. Indeed, agreement on $\Delta_n$ gives distance at most the left endpoint, whereas disagreement somewhere on level $n$ gives distance at least the excluded right endpoint. This observation fixes both the metric normalization and the direction of the Frostman inequality used next.

[\[lem:cylinder-dimension\]]{#lem:cylinder-dimension label="lem:cylinder-dimension"} Let $X$ be a closed stratum considered in this article. Suppose that it has $P_n$ nonempty depth-$n$ cylinders and that a compatible Borel probability measure $\mu$ assigns mass $P_n^{-1}$ to each of them. Then $$\dim_{\mathrm H}X=\liminf_{n\to\infty}\frac{\log P_n}{|\Delta_n|}.
 \label{eq:cylinder-dimension}$$

Let the liminf in [\[eq:cylinder-dimension\]](#eq:cylinder-dimension){reference-type="eqref" reference="eq:cylinder-dimension"} be $L$. If $s>L$, choose $\varepsilon>0$ and a subsequence $n_q$ such that $\log P_{n_q}\leq(s-\varepsilon)|\Delta_{n_q}|$. The $P_{n_q}$ cylinders cover $X$ and have diameter at most $\mathrm e^{-|\Delta_{n_q}|}$. Their total $s$-cost is bounded by $$P_{n_q}\mathrm e^{-s|\Delta_{n_q}|}
 \leq \mathrm e^{-\varepsilon|\Delta_{n_q}|}\longrightarrow0,$$ so $\dim_{\mathrm H}X\leq L$.

Now take $0\leq s<L$. For all sufficiently large $n$, $P_n\geq\mathrm e^{s|\Delta_n|}$. If a ball $B$ has radius in [\[eq:ball-window\]](#eq:ball-window){reference-type="eqref" reference="eq:ball-window"}, it is contained in a depth-$n$ cylinder and hence $$\mu(B)\leq P_n^{-1}\leq\mathrm e^{-s|\Delta_n|}\leq r(B)^s.$$ The finitely many larger scales are absorbed into one multiplicative constant. The mass-distribution argument gives $\dim_{\mathrm H}X\geq s$; letting $s\uparrow L$ proves the result. When $L=0$, the lower bound is automatic.

All strata below satisfy the measure hypothesis: after phases at the transient frontier have been fixed, labels at each vertex are chosen independently and uniformly inside the phase forced at that vertex. The finite-dimensional marginals are compatible, and every admissible cylinder at a given depth has the same mass. We shall also use the standard identity $$\dim_{\mathrm H}\Bigl(\bigcup_{q=1}^Q X_q\Bigr)=\max_{1\leq q\leq Q}\dim_{\mathrm H}X_q
 \label{eq:finite-union}$$ for a finite union.

## Complete cyclic phases and the weighted kernel

Fix $p\geq1$ and pairwise disjoint nonempty phase alphabets $V_0,\ldots,V_{p-1}$ with $$a_j=|V_j|\in\mathbb N,
 \qquad c_j=\log a_j.$$ All phase indices are read in $\mathbb Z/p\mathbb Z$. The *complete cyclic block* $C(a)$ has all edges from $V_j$ to $V_{j+1}$ and no other edges. Thus a root phase determines every descendant phase, but labels inside a forced phase are independent.

For a real phase vector $x=(x_0,\ldots,x_{p-1})$, define $$H_j(x)=\frac{d-1}{d^p-1}
 \sum_{t=0}^{p-1}d^{p-1-t}x_{j-t},
 \qquad
 \bar x=\frac1p\sum_{j=0}^{p-1}x_j.
 \label{eq:H-definition}$$ The weights in $H_j$ are positive and sum to one. For $N\in\mathbb N$, let $$\mathcal C_p(N)=\{m\in\mathbb Z_{\geq0}^p:\textstyle\sum_{s=0}^{p-1}m_s=N\}
 \label{eq:compositions}$$ be the set of weak $p$-compositions of $N$.

[\[lem:weighted-limit\]]{#lem:weighted-limit label="lem:weighted-limit"} Let $x$ be a real $p$-periodic vector and $S_{n,h}(x)=\sum_{\ell=0}^n d^\ell x_{h+\ell}$. If $n\to\infty$ subject to $n\equiv r\pmod p$, then $$\frac{S_{n,h}(x)}{|\Delta_n|}\longrightarrow H_{h+r}(x).
 \label{eq:weighted-limit}$$

Put $u=n-\ell$. Along the stated residue class, $$\frac{S_{n,h}(x)}{|\Delta_n|}
 =\frac{d-1}{d-d^{-n}}
   \sum_{u=0}^n d^{-u}x_{h+n-u}
 \longrightarrow \frac{d-1}{d}
   \sum_{u=0}^{\infty}d^{-u}x_{h+r-u}.$$ Writing $u=t+kp$, $0\leq t<p$, and summing the geometric series gives $$\frac{d-1}{d}
 \sum_{t=0}^{p-1}\frac{d^{-t}}{1-d^{-p}}x_{h+r-t}
 =\frac{d-1}{d^p-1}\sum_{t=0}^{p-1}
 d^{p-1-t}x_{h+r-t},$$ which is [\[eq:weighted-limit\]](#eq:weighted-limit){reference-type="eqref" reference="eq:weighted-limit"}. The calculation also covers $p=1$.

The backward index $j-t$ in [\[eq:H-definition\]](#eq:H-definition){reference-type="eqref" reference="eq:H-definition"} is forced by reading levels backward from the boundary-dominant final level. It will be retained in every subsequent circular identity.

# Complete cyclic cores and one-level phase allocation {#sec:core-feeder}

We first compute the core from cylinders. This is the only irreducible calculation used later.

[\[thm:core\]]{#thm:core label="thm:core"} For $d\geq2$, $p\geq1$, and positive phase sizes $a=(a_0,\ldots,a_{p-1})$, the complete cyclic block satisfies $$\dim_{\mathrm H}T_{C(a)}=\min_{j\in\mathbb Z/p\mathbb Z}H_j(c),
 \qquad c_j=\log a_j.
 \label{eq:core-dimension}$$ Moreover, $$\rho(C(a))=\Bigl(\prod_{j=0}^{p-1}a_j\Bigr)^{1/p},
 \qquad \log\rho(C(a))=\bar c.
 \label{eq:core-spectral-mean}$$

Fix a root phase $h$. At level $\ell$ there are $d^\ell$ vertices and each has $a_{h+\ell}$ independent label choices. Hence the exact number of depth-$n$ cylinders in this root-phase stratum is $$P_{n,h}=\prod_{\ell=0}^n a_{h+\ell}^{d^\ell}.
 \label{eq:core-prefix-count}$$ By [\[lem:weighted-limit\]](#lem:weighted-limit){reference-type="ref" reference="lem:weighted-limit"}, along $n\equiv r\pmod p$, $$\frac{\log P_{n,h}}{|\Delta_n|}\longrightarrow H_{h+r}(c).$$ The $p$ residue limits form the same cyclic list for every $h$, so [\[lem:cylinder-dimension\]](#lem:cylinder-dimension){reference-type="ref" reference="lem:cylinder-dimension"} gives $\min_jH_j(c)$ for each root-phase stratum. The core shift is the finite union of those $p$ strata, proving [\[eq:core-dimension\]](#eq:core-dimension){reference-type="eqref" reference="eq:core-dimension"}.

For [\[eq:core-spectral-mean\]](#eq:core-spectral-mean){reference-type="eqref" reference="eq:core-spectral-mean"}, every row of $C(a)^p$ has sum $\prod_j a_j$. The all-one vector is therefore an eigenvector with that eigenvalue, while the maximum-row-sum norm gives the reverse bound on the spectral radius. Thus $\rho(C(a)^p)=\prod_j a_j$, and spectral mapping yields the displayed formula. This is an elementary block calculation, not an imported dimension--spectral-radius equality.

## The unrestricted one-level feeder

Add one state $r$ to the core. Put an edge from $r$ to every label in every $V_s$, no edge $r\to r$, and no edge from the core back to $r$. This is the *unrestricted one-level feeder*. For a phase composition $m\in\mathcal C_p(d)$, define $$\begin{aligned}
 b_k(m;c)&=\frac1d\sum_{s=0}^{p-1}m_s c_{s+k},
 \label{eq:b-definition}\\
 D_1(m;c)&=\min_{j\in\mathbb Z/p\mathbb Z}H_j(b(m;c)).
 \label{eq:D1-definition}\end{aligned}$$

[\[prop:fixed-one-level\]]{#prop:fixed-one-level label="prop:fixed-one-level"} Fix the phase of each of the $d$ ordered children of a root labeled $r$, and let $m_s$ count children assigned to phase $s$. The corresponding closed stratum $X_m$ has $$\dim_{\mathrm H}X_m=D_1(m;c)
 =\min_j\frac1d\sum_{s=0}^{p-1}m_sH_{s+j}(c).
 \label{eq:D1-two-forms}$$ The value depends only on the composition, although the stratum itself also depends on the ordered assignment.

For total depth $n\geq1$, each of the $m_s$ subtrees entering phase $s$ contributes $a_{s+\ell}^{d^\ell}$ choices at relative level $\ell$. Therefore $$P_{n,m}=\prod_{s=0}^{p-1}\prod_{\ell=0}^{n-1}
 a_{s+\ell}^{m_s d^\ell}.
 \label{eq:feeder-prefix-count}$$ Using [\[eq:b-definition\]](#eq:b-definition){reference-type="eqref" reference="eq:b-definition"}, this becomes $$\log P_{n,m}=d\sum_{\ell=0}^{n-1}d^\ell b_\ell(m;c).
 \label{eq:feeder-prefix-log}$$ Since $$\frac{d|\Delta_{n-1}|}{|\Delta_n|}\longrightarrow1,$$ [\[lem:weighted-limit\]](#lem:weighted-limit){reference-type="ref" reference="lem:weighted-limit"} shows that the residue limits of $\log P_{n,m}/|\Delta_n|$ are the cyclic list $H_j(b(m;c))$. The first identity in [\[eq:D1-two-forms\]](#eq:D1-two-forms){reference-type="eqref" reference="eq:D1-two-forms"} follows from [\[lem:cylinder-dimension\]](#lem:cylinder-dimension){reference-type="ref" reference="lem:cylinder-dimension"}. For the second, linearity and cyclic covariance give, term by term, $$H_j(b(m;c))=\frac1d\sum_s m_sH_{s+j}(c).$$

[\[thm:one-level\]]{#thm:one-level label="thm:one-level"} Let $M_1(a)$ denote the complete cyclic core with its unrestricted one-level feeder. Then $$\boxed{\displaystyle
 \dim_{\mathrm H}T_{M_1(a)}=
 \max_{m\in\mathcal C_p(d)}\min_{j\in\mathbb Z/p\mathbb Z}
 \frac1d\sum_{s=0}^{p-1}m_sH_{s+j}(c).}
 \label{eq:one-level-optimizer}$$ In particular, the maximum in [\[eq:one-level-optimizer\]](#eq:one-level-optimizer){reference-type="eqref" reference="eq:one-level-optimizer"} already dominates every core-root stratum.

There are $p^d$ ordered phase assignments for the children of $r$. The root-$r$ stratum is their finite union. Grouping by composition and applying [\[eq:finite-union,prop:fixed-one-level\]](#eq:finite-union,prop:fixed-one-level){reference-type="ref" reference="eq:finite-union,prop:fixed-one-level"} gives the maximum in [\[eq:one-level-optimizer\]](#eq:one-level-optimizer){reference-type="eqref" reference="eq:one-level-optimizer"} for that stratum.

It remains to verify that passing to the full shift, where the root may also lie in the core, does not increase the answer. For any phase $s$, take the concentrated composition $m=de_s$. Then $$D_1(de_s;c)=\min_j H_{s+j}(c)=\min_jH_j(c).
 \label{eq:concentrated-dominance}$$ Thus concentrated compositions recover the complete-core value, up to cyclic reindexing. The feeder maximum therefore dominates every core-root stratum. The full shift is a finite union of the feeder-root and core-root strata, so [\[eq:one-level-optimizer\]](#eq:one-level-optimizer){reference-type="eqref" reference="eq:one-level-optimizer"} follows.

[\[rem:finite-composition\]]{#rem:finite-composition label="rem:finite-composition"} Suppose a separately declared one-level feeder admits a nonempty finite set $F\subseteq\mathcal C_p(d)$ of phase compositions and no others, while retaining the complete cyclic core and having no return edge. The identical finite union proof gives $$\dim_{\mathrm H}(\text{feeder-root stratum})=\max_{m\in F}D_1(m;c).$$ The full-shift dimension is the maximum of this value and the core value unless $F$ contains a concentrated composition. This observation does not cover incomplete core blocks, arbitrary transient feeder shapes, or return edges.

Equation [\[eq:one-level-optimizer\]](#eq:one-level-optimizer){reference-type="eqref" reference="eq:one-level-optimizer"} explains why graph-theoretic transience is not dimension-negligible in this metric. The state $r$ appears only at the root of its stratum, but its phase allocation is inherited by $d^\ell$ vertices at every later relative level. The root itself has vanishing normalized weight; the descendant allocation it selects does not.

# Saturation: mean, convolution, and Fourier support {#sec:saturation}

The optimizer in [\[eq:one-level-optimizer\]](#eq:one-level-optimizer){reference-type="eqref" reference="eq:one-level-optimizer"} is always bounded by the spectral mean $\bar c=\log\rho(C(a))$. We now characterize equality without relaxing the integer composition.

[\[lem:H-invertible\]]{#lem:H-invertible label="lem:H-invertible"} The circulant map $x\mapsto H(x)$ defined in [\[eq:H-definition\]](#eq:H-definition){reference-type="eqref" reference="eq:H-definition"} preserves the phase mean and is invertible on $\mathbb R^p$. Consequently, $$H(x)\text{ is constant}\quad\Longleftrightarrow\quad x\text{ is constant}.
 \label{eq:H-constant-iff}$$

Because the kernel weights sum to one, cyclic reindexing gives $$\frac1p\sum_jH_j(x)=\frac1p\sum_jx_j.$$ For invertibility, evaluate the unnormalized kernel polynomial at a $p$th root of unity $z$: $$\sum_{t=0}^{p-1}d^{p-1-t}z^t
 =\frac{d^p-z^p}{d-z}=\frac{d^p-1}{d-z}.
 \label{eq:H-multiplier}$$ It is nonzero since $d\geq2$ and $|z|=1$. Thus every Fourier multiplier of $H$ is nonzero, which proves invertibility. Constants are preserved, so [\[eq:H-constant-iff\]](#eq:H-constant-iff){reference-type="eqref" reference="eq:H-constant-iff"} follows.

For later use, let $N\geq1$, $m\in\mathcal C_p(N)$, and set $$\Psi_j^{(N)}(m;c)=\frac1N\sum_{s=0}^{p-1}m_sH_{s+j}(c),
 \qquad
 \Psi_*^{(N)}(m;c)=\min_j\Psi_j^{(N)}(m;c).
 \label{eq:Psi-definition}$$ For $N=d$, this is exactly $D_1(m;c)$.

[\[thm:saturation\]]{#thm:saturation label="thm:saturation"} For every $N\geq1$ and $m\in\mathcal C_p(N)$, $$\Psi_*^{(N)}(m;c)\leq\bar c.
 \label{eq:spectral-mean-bound}$$ The following are equivalent:

1.  $\Psi_*^{(N)}(m;c)=\bar c$;

2.  $\sum_s m_sc_{s+k}$ is independent of $k\in\mathbb Z/p\mathbb Z$;

3.  $\prod_s a_{s+k}^{m_s}$ is independent of $k\in\mathbb Z/p\mathbb Z$.

Define $b_k=N^{-1}\sum_s m_sc_{s+k}$. By linearity and covariance, $H_j(b)=\Psi_j^{(N)}(m;c)$. Moreover, $$\frac1p\sum_kb_k
 =\frac{1}{Np}\sum_{s,k}m_sc_{s+k}
 =\bar c,$$ and [\[lem:H-invertible\]](#lem:H-invertible){reference-type="ref" reference="lem:H-invertible"} shows that the mean of the $p$ values $H_j(b)$ is also $\bar c$. Their minimum is at most their mean, proving [\[eq:spectral-mean-bound\]](#eq:spectral-mean-bound){reference-type="eqref" reference="eq:spectral-mean-bound"}. Equality holds exactly when all $H_j(b)$ equal the mean. By [\[eq:H-constant-iff\]](#eq:H-constant-iff){reference-type="eqref" reference="eq:H-constant-iff"}, this is equivalent to $b$ being constant, which is (b). Finally, $$\sum_sm_sc_{s+k}=\log\Bigl(\prod_sa_{s+k}^{m_s}\Bigr),$$ and injectivity of the logarithm gives the equivalence with (c).

The integer form (c) is useful both conceptually and computationally: exact saturation can be certified by shifted products, with no tolerance applied to linear combinations of logarithms.

## What divisibility does and does not say

For $q\in\mathbb Z/p\mathbb Z$, use the discrete Fourier convention $$\widehat c(q)=\sum_{j=0}^{p-1}c_j
 \exp\!\left(-\frac{2\pi\mathrm i qj}{p}\right).
 \label{eq:DFT}$$

[\[thm:fourier-divisibility\]]{#thm:fourier-divisibility label="thm:fourier-divisibility"} Let $N\geq1$.

1.  If $p\mid N$, the uniform composition $m_s=N/p$ saturates [\[eq:spectral-mean-bound\]](#eq:spectral-mean-bound){reference-type="eqref" reference="eq:spectral-mean-bound"}.

2.  Suppose $\widehat c(q)\neq0$ for every $q=1,\ldots,p-1$. Then a saturating composition in $\mathcal C_p(N)$ exists if and only if $p\mid N$, and every saturating composition is uniform.

In particular, the one-level sufficient condition is $p\mid d$. Its necessity requires the hypothesis in (ii).

If $m_s=N/p$, then $\sum_s m_sc_{s+k}=(N/p)\sum_sc_s$ for every $k$, so (i) follows from [\[thm:saturation\]](#thm:saturation){reference-type="ref" reference="thm:saturation"}.

For (ii), take the Fourier transform of $b_k=N^{-1}\sum_sm_sc_{s+k}$. With the convention [\[eq:DFT\]](#eq:DFT){reference-type="eqref" reference="eq:DFT"}, direct reindexing gives $$\widehat b(q)=N^{-1}\widehat m(-q)\widehat c(q).
 \label{eq:fourier-product}$$ If $m$ saturates, $b$ is constant by [\[thm:saturation\]](#thm:saturation){reference-type="ref" reference="thm:saturation"}; hence $\widehat b(q)=0$ for every nonzero mode. Full nonzero Fourier support of $c$ then forces all nonzero modes of $m$ to vanish. Fourier inversion makes $m$ constant. Its integer entries sum to $N$, so this is possible exactly when $p\mid N$, and then $m_s=N/p$. The converse is (i).

[\[ex:nondivisible\]]{#ex:nondivisible label="ex:nondivisible"} Take $$p=4,\qquad d=N=2,\qquad a=(2,3,2,3),\qquad m=(1,1,0,0).$$ For all four shifts $k$, $$\prod_{s=0}^3a_{s+k}^{m_s}=6.$$ Thus $m$ saturates by [\[thm:saturation\]](#thm:saturation){reference-type="ref" reference="thm:saturation"}, even though $4\nmid2$. The phase vector has period two, so its length-four Fourier transform has a missing nonzero mode. This example rules out any unconditional "saturation if and only if $p\mid d$" statement.

The distinction is between arithmetic availability and algebraic degeneracy. Divisibility makes the uniform integer allocation available for every phase profile. When the profile loses Fourier modes, a nonuniform allocation can be invisible to the circular convolution and can saturate for a different reason.

# Two phases: parity and strict gain {#sec:two-phase}

For two phases the max--min can be solved in closed form. The result makes the integer obstruction visible without Fourier notation.

[\[thm:two-phase\]]{#thm:two-phase label="thm:two-phase"} Let $p=2$ and put $$\mu=\frac{c_0+c_1}{2},
 \qquad
 \delta=|c_1-c_0|.$$ Then the complete cyclic core has $$\dim_{\mathrm H}T_{C(a)}
 =\mu-\frac{d-1}{2(d+1)}\delta.
 \label{eq:p2-core}$$ For the one-level composition $m=(k,d-k)$, $$D_1((k,d-k);c)
 =\mu-\frac{(d-1)|2k-d|}{2d(d+1)}\delta.
 \label{eq:p2-composition}$$ Consequently, $$\dim_{\mathrm H}T_{M_1(a)}=
 \begin{cases}
 \mu, & d\text{ even},\\[1mm]
 \displaystyle \mu-\frac{d-1}{2d(d+1)}\delta,
     & d\text{ odd}.
 \end{cases}
 \label{eq:p2-optimizer}$$ If $\delta>0$, the feeder strictly improves on the core for every $d\geq2$ and saturates the spectral mean exactly when $d$ is even. If $\delta=0$, every composition saturates.

For $p=2$, [\[eq:H-definition\]](#eq:H-definition){reference-type="eqref" reference="eq:H-definition"} becomes $$H_0(c)=\frac{dc_0+c_1}{d+1},
 \qquad
 H_1(c)=\frac{dc_1+c_0}{d+1}.$$ Their mean is $\mu$ and their absolute difference is $(d-1)\delta/(d+1)$. The smaller is therefore [\[eq:p2-core\]](#eq:p2-core){reference-type="eqref" reference="eq:p2-core"}.

For $m=(k,d-k)$, the vector in [\[eq:b-definition\]](#eq:b-definition){reference-type="eqref" reference="eq:b-definition"} has mean $\mu$ and $$b_0-b_1=\frac{2k-d}{d}(c_0-c_1).$$ Applying the preceding two-entry calculation to $b$ proves [\[eq:p2-composition\]](#eq:p2-composition){reference-type="eqref" reference="eq:p2-composition"}. The minimum of $|2k-d|$ over integers $0\leq k\leq d$ is zero for even $d$ and one for odd $d$, which gives [\[eq:p2-optimizer\]](#eq:p2-optimizer){reference-type="eqref" reference="eq:p2-optimizer"}. If $\delta>0$, the optimized feeder penalty is strictly smaller than the core penalty; it vanishes exactly in the even case. If $\delta=0$, every displayed penalty vanishes, independently of parity.

For a nonconstant two-phase profile, the strict gain occurs even at odd arity, where exact saturation is arithmetically unavailable. The feeder can balance the two phase weights more closely than any single core root, and the remaining imbalance is only one child out of $d$.

# Canonical deeper transient chains {#sec:deep}

We now iterate the one-level mechanism in one specific way. Fix $L\geq1$ and add transient states $r_0,\ldots,r_{L-1}$. The only transient edges are $$r_0\longrightarrow r_1\longrightarrow\cdots\longrightarrow r_{L-1}
 \longrightarrow\bigcup_{s=0}^{p-1}V_s.$$ An arrow to a single transient state forces all $d$ children to carry that state. The final state $r_{L-1}$ sees every core label, and the core has no edge back to the chain. We call this the *canonical unrestricted $L$-level forced chain*. Starting at $r_0$, level $L$ consists of $$N=d^L$$ ordered core roots whose phases may be selected independently.

For $m\in\mathcal C_p(d^L)$, define $$D_L(m;c)=\min_j\frac1{d^L}\sum_{s=0}^{p-1}m_sH_{s+j}(c),
 \qquad
 D_L^*(c)=\max_{m\in\mathcal C_p(d^L)}D_L(m;c).
 \label{eq:DL-definition}$$

[\[thm:deep-exact\]]{#thm:deep-exact label="thm:deep-exact"} The full Markov hom tree-shift consisting of the complete cyclic core and the canonical unrestricted $L$-level forced chain has Hausdorff dimension $$\dim_{\mathrm H}T_{M_L(a)}=D_L^*(c).
 \label{eq:deep-full-dimension}$$ For a fixed phase assignment at level $L$ with composition $m$, its top-root stratum has dimension $D_L(m;c)$. In particular, the denominator in [\[eq:DL-definition\]](#eq:DL-definition){reference-type="eqref" reference="eq:DL-definition"} is exactly $d^L$.

Fix a phase assignment of the $d^L$ level-$L$ core roots. At total depth $n\geq L$, its exact cylinder count is $$P_{n,L,m}=\prod_{s=0}^{p-1}\prod_{\ell=0}^{n-L}
 a_{s+\ell}^{m_s d^\ell}.
 \label{eq:deep-prefix-count}$$ The $L$ transient levels have forced labels and contribute no multiplicity. Since $$\frac{|\Delta_{n-L}|}{|\Delta_n|}\longrightarrow d^{-L},
 \label{eq:deep-scale-ratio}$$ the proof of [\[prop:fixed-one-level\]](#prop:fixed-one-level){reference-type="ref" reference="prop:fixed-one-level"}, now using [\[lem:weighted-limit\]](#lem:weighted-limit){reference-type="ref" reference="lem:weighted-limit"}, gives the residue limits $$\frac1{d^L}\sum_sm_sH_{s+j}(c).$$ The cylinder lemma proves the fixed-composition statement. There are only $p^{d^L}$ phase assignments, so their finite union has dimension $D_L^*(c)$ at the top root.

The full shift also allows roots in the core or at $r_q$ for $q>0$. A root at $r_q$ has $K=L-q$ transient levels and therefore value $D_K^*(c)$. If $m\in\mathcal C_p(d^K)$, then $dm\in\mathcal C_p(d^{K+1})$ and $$D_{K+1}(dm;c)=D_K(m;c).
 \label{eq:grid-embedding}$$ Thus $D_{K+1}^*(c)\geq D_K^*(c)$. A composition concentrated in one phase also recovers $\min_jH_j(c)$ at every $K$, so the top-root value dominates the core-root strata. The finite-union identity now proves [\[eq:deep-full-dimension\]](#eq:deep-full-dimension){reference-type="eqref" reference="eq:deep-full-dimension"}.

[\[thm:deep-convergence\]]{#thm:deep-convergence label="thm:deep-convergence"} For the canonical unrestricted chain, $$\begin{aligned}
 D_L(m;c)=\bar c
 &\quad\Longleftrightarrow\quad
 \sum_sm_sc_{s+k}\text{ is independent of }k,
 \label{eq:DL-saturation}\\
 D_L^*(c)&\leq\bar c,
 \label{eq:DL-upper}\\
 D_{L+1}^*(c)&\geq D_L^*(c),
 \label{eq:DL-monotone}\\
 0\leq\bar c-D_L^*(c)
 &\leq\frac{p\max_jH_j(c)}{d^L}.
 \label{eq:DL-rate}\end{aligned}$$ Consequently $D_L^*(c)\to\bar c$. If $p\mid d^L$, equality already holds at level $L$. Under the full nonzero Fourier-support hypothesis of [\[thm:fourier-divisibility\]](#thm:fourier-divisibility){reference-type="ref" reference="thm:fourier-divisibility"}, a saturating level-$L$ composition exists only if $p\mid d^L$; no such converse is asserted without that hypothesis.

The quantity $D_L(m;c)$ is $\Psi_*^{(N)}(m;c)$ from [\[eq:Psi-definition\]](#eq:Psi-definition){reference-type="eqref" reference="eq:Psi-definition"} with $N=d^L$. Therefore [\[eq:DL-saturation\]](#eq:DL-saturation){reference-type="eqref" reference="eq:DL-saturation"} and [\[eq:DL-upper\]](#eq:DL-upper){reference-type="eqref" reference="eq:DL-upper"} follow from [\[thm:saturation\]](#thm:saturation){reference-type="ref" reference="thm:saturation"}, and the divisibility statements follow from [\[thm:fourier-divisibility\]](#thm:fourier-divisibility){reference-type="ref" reference="thm:fourier-divisibility"}. Monotonicity is exactly the embedding [\[eq:grid-embedding\]](#eq:grid-embedding){reference-type="eqref" reference="eq:grid-embedding"}.

For the rate, choose a balanced composition $m\in\mathcal C_p(N)$, $N=d^L$, whose entries are $\lfloor N/p\rfloor$ or $\lceil N/p\rceil$. Write $m_s=N/p+e_s$. Then $\sum_se_s=0$ and $|e_s|<1$. Mean preservation gives, for every $j$, $$\begin{aligned}
 \left|\frac1N\sum_sm_sH_{s+j}(c)-\bar c\right|
 &=\left|\frac1N\sum_se_sH_{s+j}(c)\right|\\
 &\leq\frac{p\max_qH_q(c)}{N}.\end{aligned}$$ The optimized minimum is at least the minimum produced by this balanced composition and at most its phase mean $\bar c$. This proves [\[eq:DL-rate\]](#eq:DL-rate){reference-type="eqref" reference="eq:DL-rate"} and the limit.

[\[prop:balanced-access\]]{#prop:balanced-access label="prop:balanced-access"} Let $F_L\subseteq\mathcal C_p(d^L)$ be a nonempty finite family of compositions admitted by a separately declared depth-$L$ feeder, with the same complete core and no return edge. Its top-root dimension is $\max_{m\in F_L}D_L(m;c)$. If there is a constant $C$ and a choice $m^{(L)}\in F_L$ for every $L$ such that $$\max_s\left|m_s^{(L)}-\frac{d^L}{p}\right|\leq C,
 \label{eq:balanced-access}$$ then $$0\leq \bar c-\max_{m\in F_L}D_L(m;c)
 \leq\frac{Cp\max_jH_j(c)}{d^L}.
 \label{eq:restricted-rate}$$ Monotonicity for restricted families additionally requires a nesting condition such as $dF_L\subseteq F_{L+1}$; it is not inferred from [\[eq:balanced-access\]](#eq:balanced-access){reference-type="eqref" reference="eq:balanced-access"} alone.

The finite-union argument in [\[thm:deep-exact\]](#thm:deep-exact){reference-type="ref" reference="thm:deep-exact"} gives the exact maximum over $F_L$. Write $m_s^{(L)}=d^L/p+e_s$ and repeat the last estimate in the proof of [\[thm:deep-convergence\]](#thm:deep-convergence){reference-type="ref" reference="thm:deep-convergence"}, now with $|e_s|\leq C$.

The canonical chain is therefore more than a continuous-simplex heuristic: each finite $L$ is an exact integer optimization on the grid with denominator $d^L$. The limit follows because these grids contain balanced points with uniformly bounded coordinate discrepancy.

# A four-state obstruction and exact verification {#sec:example}

The smallest application needed here has one transient state and a two-phase complete core.

[\[cor:four-state\]]{#cor:four-state label="cor:four-state"} Let $d=2$, order the states as $(r,a,b_1,b_2)$, and take the adjacency matrix $$M=\begin{pmatrix}
 0&1&1&1\\
 0&0&1&1\\
 0&1&0&0\\
 0&1&0&0
 \end{pmatrix}.
 \label{eq:four-state-matrix}$$ Call a strongly connected component *cyclic essential* when it contains a directed cycle and supports an infinite core-rooted stratum. The only cyclic essential strongly connected component is $\{a,b_1,b_2\}$, and $$\dim_{\mathrm H}T_{M|\{a,b_1,b_2\}}=\frac{\log2}{3},
 \qquad
 \dim_{\mathrm H}T_M=\frac{\log2}{2}.
 \label{eq:four-state-values}$$ Hence Hausdorff dimension for an arbitrary reducible Markov hom tree-shift cannot equal the maximum dimension of its cyclic essential strongly connected components.

The core has phases $V_0=\{a\}$ and $V_1=\{b_1,b_2\}$, so $a=(1,2)$ and $c=(0,\log2)$. It is strongly connected, while $r$ has no incoming edge and is strictly transient. By [\[eq:p2-core\]](#eq:p2-core){reference-type="eqref" reference="eq:p2-core"} with $d=2$, the core dimension is $$\frac{\log2}{2}-\frac{\log2}{6}=\frac{\log2}{3}.$$ At a root labeled $r$, assign one child to each phase. The composition $(1,1)$ is uniform, so [\[thm:saturation\]](#thm:saturation){reference-type="ref" reference="thm:saturation"}, or directly [\[eq:p2-optimizer\]](#eq:p2-optimizer){reference-type="eqref" reference="eq:p2-optimizer"}, gives dimension $\bar c=\log2/2$. The universal mean bound shows that no feeder assignment can exceed this value, and [\[thm:one-level\]](#thm:one-level){reference-type="ref" reference="thm:one-level"} shows that it is the dimension of the full shift.

The corollary refutes the cyclic-essential-SCC maximum formula; it does not provide a formula for all reducible matrices. In particular, the proof uses the complete bipartite phase blocks and the absence of a return edge. It also does not claim the analogous topological-entropy mechanism, which belongs to the scope of @banEtAl2021 [@banEtAl2022].

## Role of exact computation

All universal statements above are proved analytically. Exact computation serves three narrower roles: it checks circular indices and finite-prefix normalizations, compares independent implementations on bounded domains, and ensures that hypothesis-breaking controls are rejected. Logarithmic expressions are stored as rational linear forms in logarithms of primes; equalities such as the four shifted products in [\[ex:nondivisible\]](#ex:nondivisible){reference-type="ref" reference="ex:nondivisible"} are decided by integer factorization rather than a floating-point tolerance.

\@P0.17P0.25P0.31P0.19@ Lane & Exact volume & Independence and role & Frozen anchor\
Stage-2 package & $73{,}517$ assertions & Closed-form and direct level-recursion engines; six mutation controls & `bea7a189ea0b3472cc6b469eb36e6460b60c4baeb19af6e8983f0da`\
Cross-audit & $56{,}710$ independent assertions & Independent formulas, recursion, optimizer replay, and six negative controls; active bytes before/after equal & `273f18e57b55f4fac76cefc3f9544e8d2297bdd9e4a3c781edb082d6`\
Independent fraction audit & $1{,}740$ profiles, $127{,}500$ compositions, $37{,}440$ prefix-residue checks & Separate rational implementation; nine nested-grid checks; all six theorem gates re-audited & `59b8451bd0356e70d95295209d60b5d128882e51afb5774ae806770dea450765`\

The plotted data in [\[fig:deep-convergence,fig:two-phase\]](#fig:deep-convergence,fig:two-phase){reference-type="ref" reference="fig:deep-convergence,fig:two-phase"} are also deterministic. Figure [\[fig:deep-convergence\]](#fig:deep-convergence){reference-type="ref" reference="fig:deep-convergence"} copies selected exact optimizer records and balanced-composition certificates from the frozen sweep. Figure [\[fig:two-phase\]](#fig:two-phase){reference-type="ref" reference="fig:two-phase"} evaluates the displayed closed formulas. Their data-generation script verifies the source hash, and a separate checker recomputes all plotted identities.

# Scope, limitations, and conclusion {#sec:conclusion}

For a complete cyclic core, the unrestricted one-level feeder converts a single transient choice into an integer allocation of $d$ phase-rooted subtrees. Although the feeder state itself occupies only one vertex, the allocation it selects is replicated across the boundary-dominant levels. This gives the exact max--min [\[eq:one-level-optimizer\]](#eq:one-level-optimizer){reference-type="eqref" reference="eq:one-level-optimizer"}. The constant-convolution criterion then separates equality with the spectral mean from mere improvement, and the canonical forced chain replaces the denominator $d$ by the exact grid denominator $d^L$.

The complete-cyclic core formula is a supporting calculation. The residual content begins with the transient optimizer, continues with its saturation arithmetic and canonical-chain convergence, and culminates in the Hausdorff cyclic-essential-SCC obstruction [\[eq:four-state-values\]](#eq:four-state-values){reference-type="eqref" reference="eq:four-state-values"}. The proofs are based on matching cylinder and mass-distribution estimates, so the full dimension statements do not rely on a spectral upper bound or a finite computation.

The scope is exact and limited. The principal families are the complete cyclic core with the unrestricted one-level feeder and the canonical unrestricted $L$-level forced chain. Only explicitly declared finite-composition one-level variants are covered by [\[rem:finite-composition\]](#rem:finite-composition){reference-type="ref" reference="rem:finite-composition"}; restricted multilevel variants require the balanced-access hypothesis [\[eq:balanced-access\]](#eq:balanced-access){reference-type="eqref" reference="eq:balanced-access"}. We exclude arbitrary finite strictly transient feeder shapes, incomplete phase blocks, return edges, nontransient reuse, and arbitrary reducible matrices. We also do not claim divisibility necessary without full Fourier support and do not import version-sensitive irreducible equality clauses from the literature.

Two concrete directions remain. First, selected non-complete cyclic blocks may admit exact phase summaries even though label choices cease to be equiprobable; identifying such summaries would require a new lower measure as well as an upper count. Second, controlled communication or return edges would replace the finite-union decomposition by an infinite recurrence. Any extension in that direction needs a matched upper and lower mechanism, not only a larger finite optimizer. Finally, the bounded source search used for positioning does not establish priority, and no such claim is made.

# Endpoint and proof bookkeeping {#app:bookkeeping}

This appendix collects boundary conventions that are easy to obscure in the main derivation.

#### $p=1$.

There is one phase and $$H_0(c)=c_0=\log a_0.$$ Every composition is the one-part composition $(N)$, all convolutions are constant, and the core, one-level, and forced-chain dimensions all equal $\log a_0$. The Fourier-support condition in [\[thm:fourier-divisibility\]](#thm:fourier-divisibility){reference-type="ref" reference="thm:fourier-divisibility"} is vacuous, while $1\mid N$ is automatic.

#### Unit phase sizes and zero dimension.

The assumption is $a_j\geq1$, not $a_j>1$. Thus some $c_j$ may vanish. The kernel $H$ remains invertible because its multiplier depends on $d$ and $p$, not on $c$. If all $a_j=1$, every admissible phase stratum is a singleton, all cylinder counts are one, and every displayed dimension is zero. The lower part of [\[lem:cylinder-dimension\]](#lem:cylinder-dimension){reference-type="ref" reference="lem:cylinder-dimension"} explicitly permits this case. An empty phase $a_j=0$ is excluded.

#### Closed-ball endpoints.

For $\mathrm e^{-|\Delta_n|}\leq r<\mathrm e^{-|\Delta_{n-1}|}$, a closed radius-$r$ ball is a depth-$n$ cylinder. At the left endpoint, points agreeing through $\Delta_n$ are included; at the right endpoint, points agreeing only through $\Delta_{n-1}$ would enter and are therefore excluded. This yields $\mathrm e^{-s|\Delta_n|}\leq r^s$ in the Frostman estimate, not the reverse inequality.

#### Ordered assignments versus compositions.

A one-level phase assignment is a map $\Sigma\to\mathbb Z/p\mathbb Z$, so there are $p^d$ assignments. A composition records only the multiplicities of its fibers. Different ordered assignments with the same composition define different closed strata but have the same cylinder count. Grouping them is legitimate only after applying the finite-union identity. At depth $L$, the same distinction gives $p^{d^L}$ assignments and compositions in $\mathcal C_p(d^L)$.

#### Covariance check.

If $b_k=N^{-1}\sum_sm_sc_{s+k}$, then $$\begin{aligned}
 H_j(b)
 &=\frac{d-1}{d^p-1}\sum_{t=0}^{p-1}d^{p-1-t}
   \frac1N\sum_sm_sc_{s+j-t}\\
 &=\frac1N\sum_sm_sH_{s+j}(c).\end{aligned}$$ This identity fixes the signs in [\[eq:D1-two-forms\]](#eq:D1-two-forms){reference-type="eqref" reference="eq:D1-two-forms"} and [\[eq:DL-definition\]](#eq:DL-definition){reference-type="eqref" reference="eq:DL-definition"}. Replacing $s+j$ by $s-j$ would contradict the backward boundary index in [\[lem:weighted-limit\]](#lem:weighted-limit){reference-type="ref" reference="lem:weighted-limit"}.

#### Why later roots do not dominate.

For the canonical chain, a root at $r_q$ sees only $K=L-q$ transient levels. The embedding $m\mapsto dm$ preserves $D_K$ exactly, so $D_K^*\leq D_L^*$. A core root is dominated by a concentrated composition. These two observations are both required for the full-shift statement [\[eq:deep-full-dimension\]](#eq:deep-full-dimension){reference-type="eqref" reference="eq:deep-full-dimension"}; the top-root calculation alone would not suffice.

#### Excluded mutations.

If one complete-block edge is deleted, labels are no longer independent within phases and [\[eq:core-prefix-count\]](#eq:core-prefix-count){reference-type="eqref" reference="eq:core-prefix-count"} can fail. A core-to-feeder return edge permits arbitrarily many feeder visits, invalidating the finite union. If the feeder does not see every core phase, the composition domain must be restricted explicitly. These are hypothesis failures, not small perturbations of the theorem.

# Exact verification and reproducibility {#app:reproducibility}

The proof package and its two audits were frozen before manuscript writing. The writer consumed complete byte inventories, not mutable directory names. The principal anchors are as follows.

**Stage-2 manifest.**

`bea7a189ea0b3472cc6b469eb36e6460b60c4bae66265659b19af6e89883f0da`.

**Cross-audit manifest.**

`273f18e57b55f4fac76cefc3f9544e8d180508cc2297bdd9e4a3c781edb082d6`.

**Independent-audit tree record.**

`59b8451bd0356e70d95295209d60b5d128882e51afb5774ae806770dea450765`. All manifest entries verified before drafting; the input trees contained no symbolic links, bytecode caches, or nonregular files.

## Independent exact lanes

The primary validation has two implementations. The closed-form lane stores each logarithmic expression as a rational vector of prime-log coefficients, enumerates weak compositions, and evaluates both the $H(b)$ and direct circular-convolution forms. The level-recursion lane does not import the closed-form engine: it loops directly over tree levels, uses the exact denominator $|\Delta_n|$, factors integers independently, and evaluates finite-tree pattern counts. An abstract-syntax check confirms the absence of cross-imports.

The deterministic domains were:

-   $d=2,3,4$, $p=1,2,3,4$, and every $a_j\in\{1,2,3\}$ for the general formulas, all one-level compositions, component depths through $2p+2$, and feeder depths $p+1$ and $2p+2$;

-   $d=2,\ldots,8$ and $a_0,a_1=1,\ldots,5$ for every two-phase composition;

-   $d=2,3$, $p=2,3,4$, two fixed phase profiles, and $L=1,2,3$ for all $d^L$-compositions;

-   $d=2,3,4$, $p=2,\ldots,6$, and $L=1,\ldots,8$ for balanced convergence controls.

The primary run made $73{,}517$ assertions. Its selected counts include $13{,}302$ exact core-prefix identities, $12{,}438$ exact feeder-prefix identities, $4{,}734$ residue comparisons, $6{,}219$ one-level compositions, $10{,}212$ depth-$L$ compositions, $816$ independent recursive core counts, and $1{,}086$ recursive feeder counts. The cross-audit rederived the ledger and made $56{,}710$ independent assertions. A third rational audit checked $1{,}740$ profiles, $127{,}500$ compositions, $37{,}440$ prefix-residue identities, and nine nested allocation grids.

## Negative controls

Six controls are required to fire:

1.  the nondivisible saturating witness in [\[ex:nondivisible\]](#ex:nondivisible){reference-type="ref" reference="ex:nondivisible"} rejects unconditional divisibility necessity;

2.  deletion of a complete-core edge rejects the complete-block count;

3.  insertion of a core-to-feeder return edge rejects the transient finite union;

4.  deletion of a feeder-to-core edge rejects the unrestricted composition domain;

5.  $d=1$, a zero phase size, and a composition with the wrong total are rejected at the parameter boundary;

6.  [\[eq:four-state-matrix\]](#eq:four-state-matrix){reference-type="ref" reference="eq:four-state-matrix"} rejects the arbitrary cyclic-essential-SCC dimension formula.

Both independent audits replayed these controls. Their purpose is to expose silent hypothesis drift, not to classify every graph outside the theorem.

## Figure and build receipts

The data source for [\[fig:deep-convergence\]](#fig:deep-convergence){reference-type="ref" reference="fig:deep-convergence"} has SHA-256 $$\texttt{cf8ae3ee10fd798d937bed725b6a55ad0635e5dcdfdb29fb0c1070f2290a63f9}.$$ From the writer artifact root, the commands

    python -B tools/generate_figure_data.py
    python -B tools/verify_figure_data.py

regenerate the canonical CSV/JSON files and independently verify 153 plotted data assertions. The generation script refuses a source-hash mismatch.

The manuscript uses only TikZ/PGFPlots and generated vector data. Builds fix `SOURCE_DATE_EPOCH=1787270400`. Because `latexmk` was absent from the frozen environment, the deterministic clean-build fallback is

    pdflatex main.tex
    bibtex main
    pdflatex main.tex
    pdflatex main.tex

inside the manuscript directory. Build reports record tool versions, source hashes, warnings, page count, embedded fonts, and equality across repeated clean builds. Finite validation never upgrades the status of an analytical claim.
