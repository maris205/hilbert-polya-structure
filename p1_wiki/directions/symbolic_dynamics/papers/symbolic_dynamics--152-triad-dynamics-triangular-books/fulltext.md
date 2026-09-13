---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--152-triad-dynamics-triangular-books"
canonical_tex: "symbolic_dynamics/papers/152-triad-dynamics-triangular-books/main.tex"
canonical_pdf: "symbolic_dynamics/papers/152-triad-dynamics-triangular-books/main.pdf"
source_sha256: "442d06a74281ce79f2e845ceb656035b5a1c7ae54c4ee2afe69927aa269f196e"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Joint Absorption and Spine-Flip Laws for Local Triad Dynamics on Triangular Books

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/152-triad-dynamics-triangular-books>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/152-triad-dynamics-triangular-books/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/152-triad-dynamics-triangular-books/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/152-triad-dynamics-triangular-books/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/152-triad-dynamics-triangular-books/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For the established $p=1/3$ local triad dynamics, we specialize to the triangular book $B(3,r)=K_{1,1,r}$ and count active imbalanced-triad update epochs. The page-imbalance count is a reflected one-dimensional quotient. We solve its transform jointly marked by absorption time and common-spine flips in an explicit Chebyshev-rational form. The mean absorption time is the quadratic $k(r+2-k)/2$, with sharp extrema over the starting count. The mean together with the probability of odd spine parity exactly identifies the book size and initial imbalance count, subject to an explicit integer feasibility criterion, while either statistic alone has concrete collisions. A private-edge block supplies a uniform absorption certificate. All formulas include the $r=1$, $r=2$, $z=0$, coincident-arrow, and clock-convention boundaries. An exact-arithmetic audit performs $199{,}581$ rational and integer checks.
author:
- Anonymous
bibliography:
- references.bib
title: 'Joint Absorption and Spine-Flip Laws for Local Triad Dynamics on Triangular Books'
```

## Markdown 正文

# Owned process, special carrier, and theorem {#sec:setup}

Let $$B_r=B(3,r)=K_{1,1,r},\qquad r\geq1,$$ be the graph obtained by joining $r$ triangles along one common *edge*, called the spine. Thus each page has two private edges. Give every physical edge a sign in $\{\pm1\}$, and call a page imbalanced when the product of its three edge signs is negative. At an update epoch, choose a currently imbalanced page uniformly, choose one of its three physical edges uniformly, and flip that sign. Stop when all pages are balanced.

Write $x_i\in\{0,1\}$ for the imbalance bit of page $i$ and $K=\sum_i x_i$. Let $T$ be the number of these *active update epochs* until absorption, and let $J$ be the number of spine flips before absorption. Expectations conditional on any sign state with $K=k$ are denoted by $\mathbb E_k$; strong lumpability below makes this notation unambiguous.

This stochastic rule is the $p=1/3$ specialization of local triad dynamics of Antal--Krapivsky--Redner [@AntalKrapivskyRedner2005; @AntalKrapivskyRedner2006]. The 2005 all-triad clock samples balanced pages too and hence inserts no-op holds; the process above is its chain embedded at active epochs. The 2006 formulation directly selects an imbalanced triad. Istrate owns the same probabilistic kernel on general graphs and its triadic-dual/XOR representation [@Istrate2009]; later hypergraph particle-system and drift methods are also background [@IstrateBonchisMarin2019]. Signed-book work owns the carrier and its static switching-class count indexed by negative pages [@SehrawatBhattacharjya2022]. Table [1](#tab:subtraction){reference-type="ref" reference="tab:subtraction"} makes the resulting claim boundary explicit.

::: {#tab:subtraction}
  Source                                                                            Owned input                                                                                                              Residual used here
  --------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------
  Antal--Krapivsky--Redner [@AntalKrapivskyRedner2005; @AntalKrapivskyRedner2006]   local triad dynamics and the $p=1/3$ equiprobable-edge update                                                            exact joint law after specialization to $B(3,r)$ and the active clock
  Istrate and Istrate--Bonchis--Marin [@Istrate2009; @IstrateBonchisMarin2019]      same general-graph kernel, triadic dual/XOR encoding, hypergraph particle systems, drift, and convergence-time program   reflected count recurrence, closed transform, and coarse inverse on the one-spine carrier only
  Sehrawat--Bhattacharjya [@SehrawatBhattacharjya2022]                              signed-book carrier and static switching classes indexed by page count                                                   no carrier, switching, coloring, or static-class claim
  Generic finite-chain tools                                                        Bellman/resolvent rationality, Chebyshev facts, tail sums, and quadratic concavity                                       only the boundary-complete formula conjunction stated below

  : Primary-source subtraction. The middle column receives zero contribution credit; the right column is the special-carrier residual.
:::

For $0\leq k\leq r$, define the joint transform $$\label{eq:F-def}
 F_k(z,u)=\mathbb E_k[z^T u^J],\qquad F_0(z,u)=1.$$ Let $U_j$ denote the Chebyshev polynomial of the second kind, with $U_{-1}=0$, $U_0=1$, and $U_{j+1}(x)=2xU_j(x)-U_{j-1}(x)$.

[\[thm:main\]]{#thm:main label="thm:main"} For the process on $B_r$ started with $K=k$, $1\leq k\leq r$, the following hold.

(i) The full sign chain is strongly lumpable by $K$, with count transitions $$\label{eq:quotient}
     k\longrightarrow k-1\quad\text{with probability }\frac23,
     \qquad
     k\longrightarrow r-k\quad\text{with probability }\frac13.$$ If the targets coincide, the two masses add.

(ii) For $r\geq2$ and $z\neq0$, put $$\label{eq:xi}
      \xi=\frac{9+z^2(4-u^2)}{12z}.$$ Then, as identities of reduced rational functions, $$\begin{aligned}
      F_k(z,u)&=U_{k-1}(\xi)F_1(z,u)-U_{k-2}(\xi),
            \label{eq:Fk}\\
      F_1(z,u)&=
      \frac{3U_{r-2}(\xi)-2zU_{r-3}(\xi)+zu}
           {3U_{r-1}(\xi)-2zU_{r-2}(\xi)}.             \label{eq:F1}\end{aligned}$$ For probability-transform evaluation, these identities hold on $|z|<1$, $|u|\leq1$, with removable points taken from the Bellman system. The boundary values are $$\label{eq:small-boundaries}
      r=1:\quad F_1=\frac{z(2+u)}3;\qquad
      r=2:\quad F_1=\frac{2z}{3-zu};\qquad
      z=0:\quad F_k=\mathbf 1_{\{k=0\}}.$$

(iii) The mean is $$\label{eq:mean}
       m_k:=\mathbb E_kT=\frac{k(r+2-k)}2.$$ For $r>1$, its unique minimum over nonabsorbing counts is at $k=1$, with value $(r+1)/2$. Its maxima are $$\label{eq:extrema}
       \begin{cases}
       k=(r+2)/2,\quad m_k=(r+2)^2/8, & r\text{ even},\\
       k=(r+1)/2,(r+3)/2,\quad m_k=((r+2)^2-1)/8,
         & r\text{ odd}.
       \end{cases}$$ For $r=1$, the sole nonabsorbing state is both extremizers and has mean one.

(iv) If $q_k=\mathbb P_k(J\text{ is odd})$, then $$\label{eq:parity}
      \mathbb E_k[(-1)^J]=\frac{r+2-2k}{r+2},
      \qquad q_k=\frac{k}{r+2}.$$ Given an exact real candidate pair $(m,q)$ for a nonabsorbing start, declare it infeasible unless $m>0$ and $0<q<1$. On that domain set $$\label{eq:R}
      R=\sqrt{\frac{2m}{q(1-q)}}.$$ The pair is feasible if and only if $R$ is an integer with $R\geq3$ and $k=qR$ is an integer satisfying $1\leq k\leq R-2$. In that case $$\label{eq:inverse}
      r=R-2,\qquad k=qR$$ are uniquely recovered. Both observations are necessary in general.

(v) For every integer $n\geq0$, $$\label{eq:tail}
     \mathbb P_k(T>nr)\leq\left[1-\left(\frac23\right)^r\right]^n.$$ In particular, absorption is almost sure and $T$ has an exponential tail.

The theorem recovers only the carrier size and initial imbalance *count*. It neither reconstructs a full edge-sign configuration nor supplies stability under noisy observations.

# Strong lumping and an absorption certificate {#sec:lumping}

Flipping either private edge of the selected active page clears that page and changes no other imbalance bit. Both private choices therefore send every state of count $k$ to the count $k-1$. Flipping the common spine toggles all $r$ imbalance bits and sends count $k$ to $r-k$. The probabilities are the same for every full sign state within the count fibre, which proves strong lumpability and [\[eq:quotient\]](#eq:quotient){reference-type="eqref" reference="eq:quotient"}. If $k-1=r-k$, the private and spine choices are different physical updates with the same quotient target, so their probabilities combine rather than producing two arrows.

Pre-generate the private/spine type of the next $r$ edge choices. At each active epoch the type is private with probability $2/3$, independently of the state. If all $r$ types are private, each performed update lowers $K$ by one, so absorption occurs within the block, possibly before all pre-generated choices are used. This event has probability $(2/3)^r$. Conditional on survival to any block boundary, the same bound applies. Iteration with the Markov property proves [\[eq:tail\]](#eq:tail){reference-type="eqref" reference="eq:tail"}, and hence almost-sure absorption.

On the friendship or Dutch-windmill graph, the triangles share only a vertex, not an edge. Every physical edge is then private, so $K\mapsto K-1$ and $T=K$ deterministically. That carrier does not satisfy [\[eq:quotient\]](#eq:quotient){reference-type="eqref" reference="eq:quotient"}.

# The spine-marked Chebyshev transform {#sec:transform}

First-step conditioning in the quotient gives, for $1\leq k\leq r$, $$\label{eq:bellman}
 F_k=z\left(\frac23F_{k-1}+\frac{u}{3}F_{r-k}\right).$$ The factor $u$ marks precisely a common-spine flip; it does not mark all sign flips or the terminal number of negative edges.

Work first in the rational-function field with $z\neq0$. For $1\leq k<r$, equations [\[eq:bellman\]](#eq:bellman){reference-type="eqref" reference="eq:bellman"} at $k$ and $r-k$ give $$\label{eq:elim-pairs}
 uF_{r-k}=\frac{3}{z}F_k-2F_{k-1},\qquad
 F_{r-k-1}=\frac{3}{2z}F_{r-k}-\frac{u}{2}F_k.$$ Insert the second identity into [\[eq:bellman\]](#eq:bellman){reference-type="eqref" reference="eq:bellman"} at $k+1$, then use the first. No division by $u$ is needed, and simplification gives $$\label{eq:cheb-rec}
 F_{k+1}=\frac{9+z^2(4-u^2)}{6z}F_k-F_{k-1}
        =2\xi F_k-F_{k-1}.$$ Since $F_0=1$, the Chebyshev solution of [\[eq:cheb-rec\]](#eq:cheb-rec){reference-type="eqref" reference="eq:cheb-rec"} is [\[eq:Fk\]](#eq:Fk){reference-type="eqref" reference="eq:Fk"}. At the terminal count, [\[eq:bellman\]](#eq:bellman){reference-type="eqref" reference="eq:bellman"} becomes $$\label{eq:terminal}
 F_r=\frac{2z}{3}F_{r-1}+\frac{zu}{3}.$$ Substituting [\[eq:Fk\]](#eq:Fk){reference-type="eqref" reference="eq:Fk"} into [\[eq:terminal\]](#eq:terminal){reference-type="eqref" reference="eq:terminal"} and collecting the $F_1$ terms gives [\[eq:F1\]](#eq:F1){reference-type="eqref" reference="eq:F1"}.

For $r=1$, every edge choice absorbs in one epoch; two choices are private and one is the marked spine, which gives the first formula in [\[eq:small-boundaries\]](#eq:small-boundaries){reference-type="eqref" reference="eq:small-boundaries"}. When $r=2$, a spine flip from $k=1$ is a self-loop, so [\[eq:bellman\]](#eq:bellman){reference-type="eqref" reference="eq:bellman"} directly gives $F_1=2z/(3-zu)$. Equivalently, the unreduced Chebyshev ratio is $$\frac{3+zu}{6\xi-2z},\qquad
 6\xi-2z=\frac{(3-zu)(3+zu)}{2z};$$ the removable factor $3+zu$ must be cancelled before pointwise evaluation. Finally, $\xi$ is undefined at $z=0$, whereas [\[eq:bellman\]](#eq:bellman){reference-type="eqref" reference="eq:bellman"} gives $F_0=1$ and $F_k=0$ for $k>0$. Thus [\[eq:Fk\]](#eq:Fk){reference-type="eqref" reference="eq:Fk"}--[\[eq:F1\]](#eq:F1){reference-type="eqref" reference="eq:F1"} are read as reduced rational identities with these Bellman continuations.

Uniform choices matter. Nonuniform page weights generally destroy count lumpability, while nonuniform physical-edge weights change the coefficients in both [\[eq:quotient\]](#eq:quotient){reference-type="eqref" reference="eq:quotient"} and [\[eq:bellman\]](#eq:bellman){reference-type="eqref" reference="eq:bellman"}.

# Quadratic clock and exact coarse inverse {#sec:inverse}

The exponential tail justifies first-step conditioning of the mean: $$\label{eq:mean-bellman}
 m_0=0,\qquad
 m_k=1+\frac23m_{k-1}+\frac13m_{r-k}.$$ Use [\[eq:mean-bellman\]](#eq:mean-bellman){reference-type="eqref" reference="eq:mean-bellman"} at $k$, $r-k$, and $k+1$. Eliminating the two reflected terms yields $$m_{k+1}-2m_k+m_{k-1}=-1\qquad(1\leq k<r).$$ The terminal equation is $m_r=1+(2/3)m_{r-1}$. Together with $m_0=0$, these conditions have the unique quadratic solution [\[eq:mean\]](#eq:mean){reference-type="eqref" reference="eq:mean"}.

For $r>1$, strict concavity makes the minimum occur at an endpoint; since $m_1=(r+1)/2<m_r=r$, it is uniquely at $k=1$. The vertex is $(r+2)/2$, so the nearest admissible integer or integers give exactly [\[eq:extrema\]](#eq:extrema){reference-type="eqref" reference="eq:extrema"}. The one-state case $r=1$ is immediate.

Put $h_k=\mathbb E_k[(-1)^J]$. A private flip preserves the parity sign and a spine flip reverses it, whence $$\label{eq:parity-bellman}
 h_0=1,\qquad h_k=\frac23h_{k-1}-\frac13h_{r-k}.$$ The affine values $(r+2-2k)/(r+2)$ satisfy every equation. Iterating the bounded first-step identity to $T\wedge n$ and using almost-sure absorption and bounded convergence identifies them with $\mathbb E_k[(-1)^J]$. The second identity in [\[eq:parity\]](#eq:parity){reference-type="eqref" reference="eq:parity"} follows from $\mathbb E[(-1)^J]=1-2\mathbb P(J\text{ odd})$.

Let $R_0=r+2$. Equations [\[eq:mean\]](#eq:mean){reference-type="eqref" reference="eq:mean"} and [\[eq:parity\]](#eq:parity){reference-type="eqref" reference="eq:parity"} give $$m=\frac{k(R_0-k)}2,\qquad
 q(1-q)=\frac{k(R_0-k)}{R_0^2}.$$ In particular, every genuine pair has $m>0$ and $0<q<1$. Therefore [\[eq:R\]](#eq:R){reference-type="eqref" reference="eq:R"} equals the positive integer $R_0$, and $qR_0=k$ is an integer in $[1,R_0-2]$. Conversely, if the stated feasibility conditions hold, the pair $r=R-2$, $k=qR$ is admissible and the two displayed identities reproduce $(m,q)$. This proves both feasibility and uniqueness.

The central value $q=1/2$ is regular: it occurs when $r$ is even and $k=(r+2)/2$. Neither scalar alone suffices. Indeed, $$(r,k)=(1,1),(4,2)\quad\text{both give }q=\frac13,
 \qquad
 (r,k)=(2,2),(3,1)\quad\text{both give }m=2.$$

# Exact pressure, controls, and limitations {#sec:audit}

A standard-library verifier enumerates every nonzero imbalance vector through $r=9$, solves independent rational Bellman systems, and compares them with the closed formulas. It also compares the inverse criterion with the literal two-statistic image on $7{,}335$ bounded exact candidate pairs, including $7{,}266$ rejections, checks both printed scalar collisions, enumerates exact private-block masses, and propagates $546$ finite tail probabilities. Table [2](#tab:audit){reference-type="ref" reference="tab:audit"} records the frozen lanes.

::: {#tab:audit}
  Lane                                            Exact assertions
  --------------------------------------------- ------------------
  Chebyshev elimination and transform vectors                4,416
  Inverse iff grid and scalar collisions                     7,655
  Inverse states and absorption certificate                180,600
  Literal strong lumpability                                 2,026
  Mean, parity, and extrema                                  3,958
  Private-block probability and tail                           648
  $r=1$, $r=2$, and $z=0$ boundaries                           278
  Total                                                    199,581

  : Deterministic exact-arithmetic falsification. Enumeration supports debugging; the preceding symbolic arguments prove the all-parameter theorem.
:::

The exact control uses only integers and rational numbers. It is neither a proof of the theorem nor an ownership, novelty, priority, or release certificate. The primary-source screen is bounded, and any direct owner of the special-book law would require claim subtraction anew.

Internally adjacent objects are separated by the literal update. A triangular-book edge-deletion process removes edges; here every edge remains and the spine flip reflects $k$ to $r-k$. Vertex-push orientation chains are stationary group walks, whereas this process selects an active imbalanced page and absorbs. Deterministic prefix-XOR feedback and unequal-spider first passage use different state spaces and proof engines; the bivariate spine-marked reflection law, rather than XOR notation or a mean alone, is the organizing object here.

# Limitations {#limitations .unnumbered}

The results require uniform selection of active pages and physical edges, use the active update-epoch clock, and assume the known carrier $B(3,r)=K_{1,1,r}$. They do not cover the all-triad physical clock, nonuniform weights, arbitrary graphs, friendship/windmill carriers, noisy inverse data, or recovery of a full sign state. The inverse uses exact $(m,q)$ and identifies only $(r,k)$.

# Data Availability {#data-availability .unnumbered}

No external data were used. The paper-local verifier and its frozen transcript contain the complete deterministic exact control.

# Ethics Statement {#ethics-statement .unnumbered}

This mathematical study involved no human participants, animals, personal data, or field intervention.

# Author Contributions {#author-contributions .unnumbered}

The anonymous author performed the mathematical derivations, exact checks, source-boundary audit, and manuscript preparation.

# Conflict of Interest {#conflict-of-interest .unnumbered}

The author declares no conflict of interest.

# Funding {#funding .unnumbered}

No external funding is declared.

# External Status {#external-status .unnumbered}

This artifact remains `HOLD_EXTERNAL`; it is not cleared for posting, submission, circulation, or author contact.
