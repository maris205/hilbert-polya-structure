---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--118-synchronous-mex-multipartite-dynamics"
canonical_tex: "symbolic_dynamics/papers/118-synchronous-mex-multipartite-dynamics/main.tex"
canonical_pdf: "symbolic_dynamics/papers/118-synchronous-mex-multipartite-dynamics/main.pdf"
source_sha256: "9433fc69d5e8d4cc5e508e1f893c3f155d197eb6ebac9e7e874bde7d49676082"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Synchronous Mex Dynamics on Complete Multipartite Graphs: Exact Fibres, Two-Cycles, and Basins

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/118-synchronous-mex-multipartite-dynamics>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/118-synchronous-mex-multipartite-dynamics/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/118-synchronous-mex-multipartite-dynamics/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/118-synchronous-mex-multipartite-dynamics/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/118-synchronous-mex-multipartite-dynamics/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Every vertex of a finite graph is updated simultaneously to the least nonnegative colour absent from its open neighbourhood. On $K_{a_1,\ldots,a_k}$, the first image is constant on each part and induces $T(y)_i=\operatorname{mex}\{y_j:j\ne i\}$. We retain the labelled information discarded by this quotient through the exact first-image fibre $N_{\mathbf a,q}(y)$. One formula uses inclusion--exclusion over missing lower colours; a materially different formula uses the part support of every named colour and multivariate labelled generating functions.

  The quotient has exactly $k!$ fixed states and $$b_k=\sum_{m=0}^{k-2}\frac{k!}{(k-m)!}$$ two-cycles. More strongly, a repeated coordinate in a graph image can only be its maximum; this forces the second iterate of every labelled colouring to be recurrent. Closed products give the fibre of every recurrent target. Together with explicit quotient preimages they yield every orbit basin and its depth-zero, one, and two layers. The 2003 serial-daemon mex correction, the 2018 synthesis of distributed Grundy protocols under explicit timing models, Grundy fixed points, generic labelled-EGF machinery, and zeta bookkeeping receive zero contribution credit. The residual scope is only this unconditional synchronous multipartite conjunction. Ownership, priority, and external circulation remain on hold.
author:
- Anonymous
bibliography:
- references.bib
title: 'Synchronous Mex Dynamics on Complete Multipartite Graphs: Exact Fibres, Two-Cycles, and Basins'
```

## Markdown 正文

# Introduction

The local instruction *take the least colour absent from the open neighbourhood* is classical in Grundy colouring. In particular, @HedetniemiJacobsSrimani2003 use the same value, shifted to positive colours, in self-stabilizing algorithms controlled by a daemon. Later protocol synthesis explicitly includes distributed Grundy colouring under specified timing models [@FaghihEtAl2018]; parallel, asynchronous, local-search, and dynamic-colouring work includes [@FirozZalewskiLumsdaine2019; @BossekEtAl2021]. The local correction, protocol synthesis, Grundy fixed points, and scheduler-dependent algorithmic convergence therefore receive zero contribution credit here.

We instead fix an unconditional Jacobi clock: every vertex updates on every round from the unchanged old colouring. This scheduler does not generally converge; even the uniform state can alternate. Complete multipartite graphs give a tractable family, because vertices in one part have identical open neighbourhoods. Yet replacing each part by one coordinate erases the ordered size vector $\mathbf a=(a_1,\ldots,a_k)$.

The key device is to retain the weight of every first-round quotient state. For a part vector $y$, let $N_{\mathbf a,q}(y)$ be the number of labelled vertex colourings whose first image is $y$. We derive this weight twice. Inclusion--exclusion counts violated presence requirements. A second proof fixes, for every named colour, the set of parts in which it occurs, and counts onto assignments. Their equality is a useful exact bridge rather than an algorithmic complexity claim.

The temporal classification then has three steps. An elementary identity for the quotient keeps unique colours below a global mex and replaces all other coordinates by that mex. A separate image-shape lemma says that only the maximum first-image value can repeat. Together they put the second graph iterate directly in an explicit fixed/two-cycle list. Finally, closed recurrent fibres and quotient preimages turn the classification into all basin and layer counts.

We do not treat arbitrary graphs or asynchronous schedules. Conflict guards and the closed-neighbourhood variant are also outside our scope. A bounded owner search did not locate this exact synchronous multipartite functional graph, but a search non-hit is not novelty or priority evidence. External dissemination remains **HOLD**.

# The graph map and its quotient

Let $k\ge1$, let $a_i\ge1$, and let $$G=K_{a_1,\ldots,a_k},\qquad
 V(G)=V_1\sqcup\cdots\sqcup V_k,\qquad |V_i|=a_i.$$ All vertices are labelled. Put $n=\sum_i a_i$ and $$\Delta=n-\min_i a_i.$$ For an integer $q\ge\Delta+1$, let $C_q=\{0,\ldots,q-1\}$. The canonical phase uses $q=\Delta+1$; the larger-palette extension will make surplus-colour dependence explicit. Since $\Delta\ge k-1$, the standing hypothesis also gives $q\ge k$, so every quotient state displayed below lies in the palette.

[\[def:map\]]{#def:map label="def:map"} For $c:V(G)\to C_q$, define $$\Phi(c)(v)=\operatorname{mex}\{c(u):uv\in E(G)\}.$$ Every value on the right is read from $c$, and all vertices update simultaneously.

Every neighbourhood has at most $\Delta<q$ vertices, so its mex belongs to $C_q$. Vertices in one part have the same open neighbourhood. Hence $\Phi(c)$ is part-monochromatic, represented by $$y(c)=(y_1(c),\ldots,y_k(c)),\qquad
 y_i(c)=\operatorname{mex}c(V(G)\setminus V_i).$$ Subsequent rounds are governed by $$\label{eq:T}
                    T(y)_i=\operatorname{mex}\{y_j:j\ne i\}.$$ Thus $\Phi^t(c)$ is represented by $T^{t-1}(y(c))$ for $t\ge1$. Define the exact first-image fibre $$N_{\mathbf a,q}(y)=|\{c\in C_q^{V(G)}:y(c)=y\}|.$$

# Two exact fibre formulas

## Bad-event inclusion--exclusion

For $y\in C_q^k$, put $$\mathcal E(y)=\{(i,r):1\le i\le k,\ 0\le r<y_i\}.$$ For $J\subseteq\mathcal E(y)$ and $1\le h\le k$, define the set $$B_h(y,J)=\{y_i:i\ne h\}
 \cup\{r:(i,r)\in J,\ i\ne h\}.$$ Repeated values in this union are counted once.

[\[thm:IE\]]{#thm:IE label="thm:IE"} For every $y\in C_q^k$, $$\label{eq:IE}
 \boxed{
 N_{\mathbf a,q}(y)=
 \sum_{J\subseteq\mathcal E(y)}(-1)^{|J|}
 \prod_{h=1}^k\bigl(q-|B_h(y,J)|\bigr)^{a_h}.}$$ Impossible targets automatically have value zero.

The equality $y_i=\operatorname{mex}c(V\setminus V_i)$ requires colour $y_i$ to be absent outside $V_i$, and every $r<y_i$ to occur there. Impose all the absence requirements first. For $(i,r)\in\mathcal E(y)$, let the bad event be that $r$ is also absent outside $V_i$. Under a selected set $J$ of bad events, a vertex in $V_h$ cannot use $y_i$ for $i\ne h$ and cannot use $r$ when $(i,r)\in J$ with $i\ne h$. Its forbidden set is exactly $B_h(y,J)$. Vertex choices now factor by parts, and inclusion--exclusion over $J$ gives [\[eq:IE\]](#eq:IE){reference-type="eqref" reference="eq:IE"}.

## Colour supports and labelled EGFs

For a named colour $r$, let $P_r\subseteq[k]$ be the set of parts in which it occurs. Define $\mathcal A_r(y)$ to consist of the supports $P\subseteq[k]$ satisfying $$\begin{aligned}
 y_i=r&\ \Longrightarrow\ P\subseteq\{i\},               \label{eq:support1}\\
 y_i>r&\ \Longrightarrow\ P\nsubseteq\{i\}.              \label{eq:support2}\end{aligned}$$ Let $s(a,d)=d!S(a,d)$ be the number of onto maps from an $a$-element labelled set to $d$ named colours, with $s(a,0)=0$ for $a\ge1$. Put $$G_r^y(x_1,\ldots,x_k)=
 \sum_{P\in\mathcal A_r(y)}
 \prod_{i\in P}(e^{x_i}-1).$$

[\[thm:support\]]{#thm:support label="thm:support"} For every $y\in C_q^k$, $$\begin{aligned}
 N_{\mathbf a,q}(y)
 &=\left(\prod_{i=1}^k a_i!\right)
 [x_1^{a_1}\cdots x_k^{a_k}]
 \prod_{r=0}^{q-1}G_r^y(x_1,\ldots,x_k),                 \label{eq:EGF}\\
 &=\sum_{\substack{P_r\in\mathcal A_r(y)\\0\le r<q}}
 \prod_{i=1}^k s(a_i,d_i),\qquad
 d_i=|\{r:i\in P_r\}|.                                  \label{eq:onto}\end{aligned}$$ If $M=\max_i y_i$, the factors with $r>M$ combine to $$\exp\!\bigl((q-1-M)(x_1+\cdots+x_k)\bigr).$$

Conditions [\[eq:support1\]](#eq:support1){reference-type="eqref" reference="eq:support1"}--[\[eq:support2\]](#eq:support2){reference-type="eqref" reference="eq:support2"} are exactly the absence and lower-colour presence conditions for each target coordinate. After all supports are fixed, part $V_i$ uses $d_i$ named colours, each at least once, giving $s(a_i,d_i)$. Multiplication over parts and summation over supports proves [\[eq:onto\]](#eq:onto){reference-type="eqref" reference="eq:onto"}.

In labelled-EGF form, one named colour with support $P$ contributes $\prod_{i\in P}(e^{x_i}-1)$. Multiplying over named colours and extracting all labelled vertices proves [\[eq:EGF\]](#eq:EGF){reference-type="eqref" reference="eq:EGF"}; see [@FlajoletSedgewick2009] for the generic labelled construction. For $r>M$, every support is allowed, and $$\sum_{P\subseteq[k]}\prod_{i\in P}(e^{x_i}-1)
 =e^{x_1+\cdots+x_k},$$ which gives the last assertion.

# The recurrent quotient and two-round collapse

For $y\in C_q^k$, let $g=\operatorname{mex}\{y_1,\ldots,y_k\}$.

[\[lem:Tformula\]]{#lem:Tformula label="lem:Tformula"} $$T(y)_i=
 \begin{cases}
 y_i,&y_i<g\ \text{and \(y_i\) occurs exactly once in \(y\)},\\
 g,&\text{otherwise}.
 \end{cases}$$

Every value below $g$ occurs in $y$, while $g$ does not. Removing coordinate $i$ creates a missing value below $g$ exactly when $y_i<g$ and that value was unique. Otherwise all lower values remain and $g$ remains missing.

Write $[m]_0=\{0,\ldots,m-1\}$. For $0\le m\le k-2$ and an injection $\iota:[m]_0\hookrightarrow[k]$, define $$x^\pm_{\iota,m}(i)=
 \begin{cases}
 r,&i=\iota(r),\\
 m,&i\notin\operatorname{im}\iota\quad\text{for }x^-,\\
 m+1,&i\notin\operatorname{im}\iota\quad\text{for }x^+.
 \end{cases}$$ The last two lines mean that the uninjected coordinates are filled by $m$ in $x^-$ and by $m+1$ in $x^+$.

[\[thm:quotient\]]{#thm:quotient label="thm:quotient"} The recurrent states of $T$ are exactly:

1.  the $k!$ permutations of $0,\ldots,k-1$, all fixed; and

2.  the pairs $x^-_{\iota,m}\leftrightarrow x^+_{\iota,m}$ above.

Every quotient state enters this list in at most two rounds. The number of two-cycles is $$b_k=\sum_{m=0}^{k-2}\frac{k!}{(k-m)!},$$ with an empty sum for $k=1$.

shows that one quotient update retains some unique values below $g$ and fills every other coordinate by $g$. Let $m$ be the least nonnegative integer missing from the retained unique values, so $m\le g$. If $m<g$, a second use of the lemma retains precisely the initial segment $0,\ldots,m-1$ and fills all other coordinates by $m$. Here $m$ occurs in the original vector but was not retained, so it occurs at least twice. Hence at least two coordinates remain and the result is $x^-_{\iota,m}$.

If $m=g$, the first image already retains every value $0,\ldots,g-1$. It is therefore $x^-_{\iota,g}$ when at least two coordinates remain. If one remains then $g=k-1$, and if none remains then $g=k$; in both boundary cases the first image is a permutation. Direct substitution shows that every permutation is fixed and that each displayed pair is swapped. The repeated fill value and the positions of the lower unique values recover $m$ and $\iota$, so the indexed pairs are disjoint. This proves exhaustion. For fixed $m$, the number of injections is $k!/(k-m)!$.

Graph images satisfy a stronger shape restriction.

[\[lem:maxrepeat\]]{#lem:maxrepeat label="lem:maxrepeat"} Assume $k\ge2$. If $y_i(c)=y_j(c)=r$ for $i\ne j$, then $r=\max_\ell y_\ell(c)$.

The target condition at $i$ makes colour $r$ absent from $V\setminus V_i$; the condition at $j$ makes it absent from $V\setminus V_j$. Those two sets cover all vertices, so $r$ is globally absent. A target larger than $r$ would require $r$ to occur in its open neighbourhood, a contradiction.

[\[thm:two-round\]]{#thm:two-round label="thm:two-round"} For every labelled colouring $c$, $$T(y(c))\in\mathcal R_k,$$ where $\mathcal R_k$ is the recurrent list in [\[thm:quotient\]](#thm:quotient){reference-type="ref" reference="thm:quotient"}. Equivalently, $\Phi^2(c)$ is recurrent, so every original-state preperiod is at most two.

For $k=1$, the graph is edgeless, every colouring has first image $(0)$, and this quotient state is fixed. We now assume $k\ge2$ and put $$M=\max_i y_i(c),\qquad
 g=\operatorname{mex}\{y_1(c),\ldots,y_k(c)\}.$$ If $g\le M$, [\[lem:maxrepeat\]](#lem:maxrepeat){reference-type="ref" reference="lem:maxrepeat"} makes every value below $g$ unique. therefore retains one copy of $0,\ldots,g-1$ and fills the remaining coordinates by $g$, giving a permutation or $x^-_{\iota,g}$.

If $g=M+1$, every value $0,\ldots,M$ occurs. makes $0,\ldots,M-1$ unique. If $M$ is unique, $y(c)$ is a fixed permutation. If it repeats, the quotient update retains the lower initial segment and replaces every $M$ by $M+1$, giving $x^+_{\iota,M}$.

Every periodic graph colouring lies in $\operatorname{im}\Phi$ and hence is part-monochromatic. On the part-monochromatic subspace, coordinate identification intertwines $\Phi$ with $T$. Therefore the periodic graph states are exactly the lifts of $\mathcal R_k$, so the graph map has $$R_k=k!+2b_k$$ recurrent states. Standard finite-cycle bookkeeping [@ArtinMazur1965] gives:

[\[cor:zeta\]]{#cor:zeta label="cor:zeta"} $$\zeta_{\Phi}(z)
                   =(1-z)^{-k!}(1-z^2)^{-b_k}.$$

# Closed recurrent fibres

The general fibre formulas simplify on every recurrent target. Empty products equal one, and $0^0=1$ has its combinatorial meaning.

[\[prop:closed\]]{#prop:closed label="prop:closed"} [(i)]{.upright} Let $x$ be a fixed permutation and let $i_r$ be the part with $x_{i_r}=r$. With $h=q-k$, $$N_{\mathbf a,q}(x)=
 \left[\prod_{r=0}^{k-2}
 ((h+1)^{a_{i_r}}-h^{a_{i_r}})\right]
 (h+1)^{a_{i_{k-1}}}.                                  \tag{5.1}$$

[(ii)]{.upright} For $x^-_{\iota,m}$, put $R=[k]\setminus\operatorname{im}\iota$, $A_R=\sum_{j\in R}a_j$, $i_r=\iota(r)$, and $v=q-m-1$. Then $$N_{\mathbf a,q}(x^-_{\iota,m})=
 \left[\prod_{r=0}^{m-1}
 ((v+1)^{a_{i_r}}-v^{a_{i_r}})\right]v^{A_R}.           \tag{5.2}$$

[(iii)]{.upright} For $x^+_{\iota,m}$, put $u=q-m-2$ and $$\begin{aligned}
 L_1&=\prod_{r=0}^{m-1}
 ((u+2)^{a_{i_r}}-(u+1)^{a_{i_r}}),\\
 L_0&=\prod_{r=0}^{m-1}
 ((u+1)^{a_{i_r}}-u^{a_{i_r}}),\\
 Q&=(u+1)^{A_R},\\
 Q_{\ge2}&=Q-u^{A_R}
 -\sum_{j\in R}((u+1)^{a_j}-u^{a_j})u^{A_R-a_j}.\end{aligned}$$ Then $$N_{\mathbf a,q}(x^+_{\iota,m})=(L_1-L_0)Q+L_0Q_{\ge2}. \tag{5.3}$$

For a fixed permutation, low colour $r$ is confined to $V_{i_r}$. It is required there for $r<k-1$, while colour $k-1$ is optional; the $h$ larger colours are free. This gives (5.1).

For $x^-$, every low colour is confined to and required in its injected part. The repeated target $m$ makes colour $m$ globally absent, and the $v$ larger colours are free. This gives (5.2).

For $x^+$, colour $m+1$ is globally absent. If colour $m$ occurs in an injected low part, it automatically occurs outside every part in $R$; this contributes $(L_1-L_0)Q$. If it occurs in no low part, it must occur in at least two distinct $R$-parts. The expression $Q_{\ge2}$ subtracts from all $R$-assignments the cases where colour $m$ is absent or occurs in exactly one part. This gives (5.3).

# Every basin and depth layer

The quotient preimages needed below are also explicit.

[\[prop:preimages\]]{#prop:preimages label="prop:preimages"} For a fixed permutation $x$ with $x_{i_r}=r$, $$T^{-1}(x)=
 \{y:y_{i_r}=r\ (r<k-1),\
       y_{i_{k-1}}\in\{k-1,\ldots,q-1\}\}.               \tag{6.1}$$ For a two-cycle indexed by $(\iota,m)$, put $i_r=\iota(r)$ and $R=[k]\setminus\operatorname{im}\iota$. Then $$\begin{aligned}
 T^{-1}(x^-_{\iota,m})
 &=\{y:y_{i_r}=r\ (r<m),\
 y_j\in\{m+1,\ldots,q-1\}\ (j\in R)\},                  \tag{6.2}\\
 T^{-1}(x^+_{\iota,m})
 &=\{y:y_{i_r}=r\ (r<m),\
 y_j\in\{m\}\cup\{m+2,\ldots,q-1\}\ (j\in R),\nonumber\\
 &\hspace{35mm}|\{j\in R:y_j=m\}|\ge2\}.                \tag{6.3}\end{aligned}$$

Apply [\[lem:Tformula\]](#lem:Tformula){reference-type="ref" reference="lem:Tformula"}. To output a fixed permutation, every value below $k-1$ must be unique at its prescribed coordinate, while the last coordinate can carry any value at least $k-1$. To output $x^-$, the prescribed low values are unique and all other coordinates lie strictly above $m$. To output $x^+$, the global mex is $m+1$; the low values are prescribed, $m+1$ is absent, and $m$ must repeat.

Put $$S_{\mathbf a,q}=\sum_{x\in\mathcal R_k}N_{\mathbf a,q}(x),
\qquad
 H_x=\sum_{\substack{y\in C_q^k\\T(y)=x}}N_{\mathbf a,q}(y).$$ The sums defining $H_x$ use the finite sets in [\[prop:preimages\]](#prop:preimages){reference-type="ref" reference="prop:preimages"}; impossible first images simply have fibre zero.

For a labelled graph colouring $c$, define $$\operatorname{depth}(c)=\min\{t\ge0:\Phi^t(c)\text{ is part-monochromatic and its
 quotient lies in }\mathcal R_k\}.$$

[\[thm:basins\]]{#thm:basins label="thm:basins"} The exact numbers of labelled graph colourings at depths zero, one, and two are $$\boxed{D_0=R_k,\qquad
 D_1=S_{\mathbf a,q}-R_k,\qquad
 D_2=q^n-S_{\mathbf a,q}.}                              \tag{6.4}$$ If $\mathcal O\subseteq\mathcal R_k$ is one fixed orbit or one two-cycle, then its basin size and its three layers are $$\begin{aligned}
 B_{\mathcal O}&=\sum_{x\in\mathcal O}H_x,               \tag{6.5}\\
 B_{\mathcal O,0}&=|\mathcal O|,                         \tag{6.6}\\
 B_{\mathcal O,1}
 &=\sum_{x\in\mathcal O}N_{\mathbf a,q}(x)-|\mathcal O|, \tag{6.7}\\
 B_{\mathcal O,2}
 &=B_{\mathcal O}-\sum_{x\in\mathcal O}
 N_{\mathbf a,q}(x).                                    \tag{6.8}\end{aligned}$$

A state has depth at most one exactly when its first image belongs to $\mathcal R_k$; summing its fibres gives $S_{\mathbf a,q}$. Removing the $R_k$ recurrent states gives $D_1$, and [\[thm:two-round\]](#thm:two-round){reference-type="ref" reference="thm:two-round"} puts every remaining state at depth two.

Moreover, $\Phi^2(c)=x$ exactly when $T(y(c))=x$. Hence $H_x$ counts the states whose second image is $x$, and summing over one recurrent orbit gives its whole basin. Its recurrent states form layer zero. Its states of depth at most one are precisely the fibres over its recurrent targets. Subtracting successively proves the displayed formulas.

::: {#tab:k12}
  recurrent orbit                 recurrent target fibres   basin size   layer profile
  ----------------------------- ------------------------- ------------ ---------------
  fixed $(0,1)$                                $N(0,1)=4$            4       $(1,3,0)$
  fixed $(1,0)$                                $N(1,0)=6$           10       $(1,5,4)$
  $(0,0)\leftrightarrow(1,1)$                       $8,3$           13       $(2,9,2)$
  all orbits                                                        27      $(4,17,6)$

  : Canonical $K_{1,2}$ signal with $q=3$. The unequal fixed fibres retain the ordered part sizes after quotient collapse.
:::

# Controls, credit boundary, and conclusion

The deterministic verifier enumerates every labelled colouring and every quotient vector in fifteen parameter lanes. It independently compares literal fibres, [\[thm:IE\]](#thm:IE){reference-type="ref" reference="thm:IE"}, support/onto counts from [\[thm:support\]](#thm:support){reference-type="ref" reference="thm:support"}, the products in [\[prop:closed\]](#prop:closed){reference-type="ref" reference="prop:closed"}, all quotient preimages, the complete recurrent quotient list and two-round entrance, pointwise depths, and every basin layer. The grid includes $K_{1,2,3}$ with $46{,}656$ states, $K_{2,2,2}$ with $15{,}625$, enlarged palettes, and $k=1$. A fresh run passes $202{,}965$ exact assertions. Computation is control evidence, not a proof of the parameterized statements.

The closest located rule-level owner is @HedetniemiJacobsSrimani2003: the local mex correction and Grundy fixed-point interpretation receive full prior credit. The synchronous and other explicit timing models used to synthesize distributed Grundy protocols by @FaghihEtAl2018 also receive zero credit. Generic labelled generating functions [@FlajoletSedgewick2009] and finite-map zeta products [@ArtinMazur1965] likewise receive zero credit. The residual is only the unconditional synchronous complete-multipartite conjunction: two exact part-sensitive fibre formulas, the repeated-maximum image shape, two-round recurrence, closed recurrent fibres, and all basin layers.

No polynomial-time evaluation claim is made; inclusion--exclusion can be exponential. No arbitrary-graph or asynchronous conclusion is implied. The owner search remains bounded, and external ownership, novelty, priority, and dissemination remain on hold.
