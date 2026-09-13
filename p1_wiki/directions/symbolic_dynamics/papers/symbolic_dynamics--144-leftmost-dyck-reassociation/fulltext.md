---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--144-leftmost-dyck-reassociation"
canonical_tex: "symbolic_dynamics/papers/144-leftmost-dyck-reassociation/main.tex"
canonical_pdf: "symbolic_dynamics/papers/144-leftmost-dyck-reassociation/main.pdf"
source_sha256: "497009603cecf0b1e57383ccb347e42fa414404cc098e6d46d5dad88d2964112"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Leftmost Reassociation of Dyck Components: Exact Transient Layers and Terminal Depth Fibres

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/144-leftmost-dyck-reassociation>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/144-leftmost-dyck-reassociation/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/144-leftmost-dyck-reassociation/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/144-leftmost-dyck-reassociation/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/144-leftmost-dyck-reassociation/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Let a nonempty Dyck path have primitive factorisation $P=C_1\cdots C_k$, with $C_1=UAD$. We iterate the deterministic rule that fixes $P$ when $k=1$ and otherwise replaces its first two components by $UAC_2D$. The complete orbit is explicit: for $0\le t\le k-1$, after $t$ updates the first component has absorbed $C_2,\ldots,C_{t+1}$, and the endpoint is fixed thereafter. Consequently the entry time is exactly $k-1$, all recurrent paths are fixed and primitive, and the unique path of maximum depth $n-1$ in semilength $n$ is $(UD)^n$. The number of paths at depth $k-1$ is $$\frac{k}{2n-k}\binom{2n-k}{n}.$$ We also resolve every terminal basin by depth. If a fixed target is $UQD$ and the interior $Q$ has $r$ primitive factors, then it has exactly one basin state at each depth $0,\ldots,r$. Hence its depth-fibre polynomial is $1+u+\cdots+u^r$, and the unique largest terminal fibre has size $n$. First-return decomposition, Catalan and ballot enumeration, ground-level comb/Tamari covers, deterministic leftmost-rotation precedents, and the ordered-tree graft/lift representation are treated as background inputs. The residual is only the exact temporal/target-fibre conjunction for this literal selector. No priority follows, and external circulation remains on hold.
author:
- Anonymous
bibliography:
- references.bib
title: 'Leftmost Reassociation of Dyck Components: Exact Transient Layers and Terminal Depth Fibres'
```

## Markdown 正文

# Introduction {#sec:introduction}

A local cover relation does not by itself determine a dynamical system: one must also specify which available cover is chosen at each state. This note fixes a particularly rigid selector on Dyck paths. At every nonfixed state, we perform the reassociation at the leftmost return to ground level. The selected down-step crosses the next primitive Dyck component, and no other part of the path changes.

The atomic reassociation belongs to the Tamari setting. Associativity orders and their lattice property go back to Huang and Tamari [@HuangTamari1972Associativity]; path formulations of Tamari-type covers also appear in the $m$-Tamari literature [@BousquetMelouFusyPrevilleRatelle2012Intervals]. Primitive decomposition of Dyck words and enumeration by the number of primitive components are likewise established topics [@PanayotopoulosSapounakis2002Prime], while Catalan and ballot enumeration are standard background [@Stanley2015Catalan]. We assign all of these ingredients zero contribution credit.

Two closer rotation precedents further narrow the boundary. Pallo studies a uniquely selected leftmost left-rotation on binary trees and the resulting rooted directed tree, rank, and distance [@Pallo2006Rotational pp. 802--803]. That deterministic map is not the map below: after adjoining a loop at its terminal root it has one fixed tree, whereas our map has $\operatorname{Cat}_{n-1}$ fixed paths, more than one for $n\geq3$. Thus it is neither equal nor conjugate, by mirror or reversal, to our map. Separately, Chapoton identifies the comb-order covers on Dyck paths as exactly the Tamari covers whose moved subpath lies at height zero [@Chapoton2020DyckOrder §1.2, p. 438], tracing the comb order to Pallo's right-arm rotations [@Pallo2003RightArm]. Every nonfixed update below is one of those ground-level covers, chosen at the leftmost ground return. The idea of a deterministic leftmost scheduler and the ground-level cover correspondence both receive zero contribution credit.

The purpose here is narrower: to record, for this particular selector, the exact conjunction of its full temporal law with its target-indexed inverse fibres. None of the scheduler, its individual covers, its tree model, or its component census is claimed separately. The argument has four parts.

1.  We give a closed formula for every iterate. It turns the number of primitive factors into the pointwise clock $\tau(P)=\kappa(P)-1$ and identifies $(UD)^n$ as the unique depth-$n-1$ path.

2.  We derive the complete temporal census: depth $k-1$ contains $\frac{k}{2n-k}\binom{2n-k}{n}$ states.

3.  For every fixed target and every feasible depth, we construct one basin state and prove that no second state exists at that depth.

4.  We derive the depth-fibre polynomial and classify the unique target of largest fibre.

The closed iterate in [\[lem:closed-orbit\]](#lem:closed-orbit){reference-type="ref" reference="lem:closed-orbit"} is the common mechanism: it proves the clock and leaves only a suffix cut to invert an endpoint. No figure is needed because that formula exposes the whole state change.

This package is owner-thin. The source boundary in [7](#sec:ownership){reference-type="ref" reference="sec:ownership"} is a conservative credit assignment, not a priority or originality decision. The record is maintained for internal theorem evaluation under [hold\_external]{.smallcaps}.

# Dyck factors and the literal map {#sec:setup}

A *Dyck path of semilength $n$* is a word in $U,D$ with $n$ occurrences of each letter such that every prefix contains at least as many $U$'s as $D$'s. Let $\mathcal D_n$ denote the set of such paths. A nonempty Dyck path is *primitive* if its only return to height zero occurs after its final step. Cutting at all positive returns gives a unique factorisation $$\label{eq:primitive-factorisation}
                         P=C_1C_2\cdots C_k$$ into primitive Dyck paths. We write $\kappa(P)=k$.

Every primitive first factor has a unique first-return form $C_1=UAD$ with $A$ a possibly empty Dyck path. Define $$\label{eq:literal-map}
 \Phi_n(P)=
 \begin{cases}
 P,&k=1,\\
 UAC_2D\,C_3\cdots C_k,&k\geq2.
 \end{cases}$$ We suppress the subscript $n$ when the semilength is fixed. The word $AC_2$ is a Dyck path, so $UAC_2D$ is primitive. Thus [\[eq:literal-map\]](#eq:literal-map){reference-type="eqref" reference="eq:literal-map"} lies in $\mathcal D_n$ and is well defined.

There is a standard ordered-tree form of the same rule. Under the contour bijection between Dyck paths and rooted ordered plane trees [@Stanley2015Catalan Theorem 1.5.1], the primitive factors $C_1,\ldots,C_k$ encode the ordered subtrees rooted at the $k$ children of the tree root. Write these subtrees as $T_1,\ldots,T_k$. For $k\geq2$, [\[eq:literal-map\]](#eq:literal-map){reference-type="eqref" reference="eq:literal-map"} is precisely $$\label{eq:tree-graft}
 (T_1,T_2,T_3,\ldots,T_k)
 \longmapsto
 (T_1\mathbin{\triangleleft}T_2,T_3,\ldots,T_k),$$ where $T_1\mathbin{\triangleleft}T_2$ appends $T_2$ as the rightmost child of the root of $T_1$. Thus the factor clock below is just root degree minus one. This contour conjugacy and graft description are representation-level background, not residual claims.

Let $\tau(P)$ be the least $t\geq0$ for which $\Phi^t(P)$ is fixed, and put $$\operatorname E(P)=\Phi^{\tau(P)}(P).$$ A path is *recurrent* when it lies on a directed cycle of $\Phi_n$. For a fixed target $T$, define its depth-fibre polynomial $$\label{eq:fibre-definition}
                 \mathcal B_T(u)=\sum_{P:\,\operatorname E(P)=T}u^{\tau(P)}.$$

The complete claim package follows. We use $\operatorname{Cat}_m=\frac{1}{m+1}\binom{2m}{m}$.

[\[thm:main\]]{#thm:main label="thm:main"} For every $n\geq1$, the map $\Phi_n$ has the following properties.

1.  Every nonfixed update reduces $\kappa$ by exactly one. The recurrent paths are exactly the fixed paths, these are exactly the primitive paths, and there are $\operatorname{Cat}_{n-1}$ of them.

2.  If $P$ has $k$ primitive factors, then $$\label{eq:pointwise-clock}
                                 \tau(P)=k-1.$$ The maximum entry time is $n-1$, attained uniquely by $(UD)^n$.

3.  For $1\leq k\leq n$, the number of paths at depth $k-1$ is $$\label{eq:ballot-layer}
     \bigl|\{P\in\mathcal D_n:\tau(P)=k-1\}\bigr|
           =\frac{k}{2n-k}\binom{2n-k}{n}.$$

4.  Let $T=UQD$ be fixed, and factor its interior as $Q=Q_1\cdots Q_r$ into primitive paths. For every $0\leq d\leq r$, the unique basin state of $T$ at depth $d$ is $$\label{eq:source-formula}
     P_d=\bigl(UQ_1\cdots Q_{r-d}D\bigr)
                 Q_{r-d+1}\cdots Q_r,$$ with the empty-prefix and empty-suffix conventions. Consequently $$\label{eq:terminal-polynomial}
                                  \mathcal B_T(u)=1+u+\cdots+u^r.$$ The unique terminal fibre of maximum size is the fibre over $$\label{eq:largest-target}
                             T_n^{\max}=U(UD)^{n-1}D,$$ and it contains $n$ states.

# The factor-count clock {#sec:clock}

The first primitive component absorbs exactly one following component per round. The next lemma makes that statement precise at every time.

[\[lem:closed-orbit\]]{#lem:closed-orbit label="lem:closed-orbit"} Let $P=C_1\cdots C_k$, where $C_1=UAD$. For every $0\leq t\leq k-1$, $$\label{eq:closed-orbit}
 \Phi^t(P)=UA\,C_2\cdots C_{t+1}D\,
                         C_{t+2}\cdots C_k.$$ When $t=0$, the block $C_2\cdots C_{t+1}$ is empty; when $t=k-1$, the suffix $C_{t+2}\cdots C_k$ is empty.

At $t=0$, [\[eq:closed-orbit\]](#eq:closed-orbit){reference-type="eqref" reference="eq:closed-orbit"} reads $UADC_2\cdots C_k=P$. Suppose the formula holds for some $t<k-1$. The word $$UA\,C_2\cdots C_{t+1}D$$ is primitive: after its initial $U$, the Dyck word $AC_2\cdots C_{t+1}$ stays at or above height one, and the displayed $D$ is its first return to height zero. Hence the primitive factorisation of the right-hand side of [\[eq:closed-orbit\]](#eq:closed-orbit){reference-type="eqref" reference="eq:closed-orbit"} consists of that first word, followed by $C_{t+2},\ldots,C_k$. Applying [\[eq:literal-map\]](#eq:literal-map){reference-type="eqref" reference="eq:literal-map"} moves the closing $D$ across $C_{t+2}$ and gives $$UA\,C_2\cdots C_{t+1}C_{t+2}D\,
                         C_{t+3}\cdots C_k,$$ which is [\[eq:closed-orbit\]](#eq:closed-orbit){reference-type="eqref" reference="eq:closed-orbit"} at time $t+1$. Induction proves the claim.

[\[cor:clock\]]{#cor:clock label="cor:clock"} The statements in [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}(i)--(ii) hold.

For $t<k-1$, the factorisation displayed in the proof of [\[lem:closed-orbit\]](#lem:closed-orbit){reference-type="ref" reference="lem:closed-orbit"} has one first component and $k-t-1$ untouched components, for a total of $k-t$ primitive factors. Thus each nonfixed step decreases $\kappa$ by one. At $t=k-1$, the formula is the single primitive path $$\label{eq:endpoint-formula}
                         \operatorname E(P)=UAC_2\cdots C_kD.$$ It is fixed, so $\tau(P)=k-1$.

If $k=1$, the definition fixes $P$. If $k>1$, the strict decrease of $\kappa$ prevents $P$ from lying on a cycle. Fixed and recurrent paths are therefore exactly the primitive paths. Deleting the first $U$ and last $D$ is a bijection from primitive paths in $\mathcal D_n$ to $\mathcal D_{n-1}$, giving $\operatorname{Cat}_{n-1}$ fixed paths.

Every primitive factor has semilength at least one, so $k\leq n$. Equality holds only when all $k$ factors have semilength one, and the only such factor is $UD$. In view of [\[eq:pointwise-clock\]](#eq:pointwise-clock){reference-type="eqref" reference="eq:pointwise-clock"}, the depth is at most $n-1$, with equality exactly at $(UD)^n$.

The proof gives more than a global bound: the component statistic is the exact amount of time remaining at every state. In particular, no transient can merge with another transient of a different factor count before their depths agree.

# Complete temporal layers {#sec:layers}

The clock reduces temporal enumeration to a component census. We include the coefficient calculation to fix the boundary case and normalisation, while treating the enumerative machinery as background.

Let $$C(z)=\sum_{m\geq0}\operatorname{Cat}_m z^m$$ be the Catalan series, which satisfies $C(z)=1+zC(z)^2$. A primitive path is $UAD$ with $A$ an arbitrary Dyck path, so the semilength generating function for one primitive component is $$\label{eq:primitive-gf}
                              R(z)=zC(z).$$

[\[prop:layers\]]{#prop:layers label="prop:layers"} For $1\leq k\leq n$, the number of paths in $\mathcal D_n$ with exactly $k$ primitive factors is the right-hand side of [\[eq:ballot-layer\]](#eq:ballot-layer){reference-type="eqref" reference="eq:ballot-layer"}.

A path with $k$ primitive factors is an ordered sequence of $k$ primitive paths. By [\[eq:primitive-gf\]](#eq:primitive-gf){reference-type="eqref" reference="eq:primitive-gf"}, its number is $$\label{eq:power-coefficient}
                  [z^n]R(z)^k=[z^{n-k}]C(z)^k.$$ Put $m=n-k$ and $W=C-1$. Then $W=z(1+W)^2$. If $m=0$, the coefficient in [\[eq:power-coefficient\]](#eq:power-coefficient){reference-type="eqref" reference="eq:power-coefficient"} is $1$, which agrees with $k(2n-k)^{-1}\binom{2n-k}{n}=1$ because $n=k$.

For $m\geq1$, Lagrange inversion gives $$\begin{aligned}
C(z)^k
  &=[z^m](1+W)^k\\
  &=\frac{1}{m}[w^{m-1}]k(1+w)^{k-1}(1+w)^{2m}\\
  &=\frac{k}{m}\binom{2m+k-1}{m-1}\\
  &=\frac{k}{2m+k}\binom{2m+k}{m}.\end{aligned}$$ Substituting $m=n-k$ and using binomial symmetry yields $$\frac{k}{2n-k}\binom{2n-k}{n-k}
             =\frac{k}{2n-k}\binom{2n-k}{n},$$ as required.

Combining [\[cor:clock,prop:layers\]](#cor:clock,prop:layers){reference-type="ref" reference="cor:clock,prop:layers"} proves [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}(iii). It also gives the complete temporal polynomial $$\label{eq:temporal-polynomial}
 \sum_{P\in\mathcal D_n}u^{\tau(P)}
   =\sum_{k=1}^{n}\frac{k}{2n-k}\binom{2n-k}{n}u^{k-1}.$$ Across all semilengths, the same sequence construction yields $$\label{eq:bivariate-gf}
 \sum_{n\geq1}\sum_{P\in\mathcal D_n}u^{\tau(P)}z^n
                  =\frac{R(z)}{1-uR(z)}
                  =\frac{zC(z)}{1-uzC(z)}.$$ Equations [\[eq:temporal-polynomial\]](#eq:temporal-polynomial){reference-type="eqref" reference="eq:temporal-polynomial"}--[\[eq:bivariate-gf\]](#eq:bivariate-gf){reference-type="eqref" reference="eq:bivariate-gf"} package the clock after it has been proved; generic generating-function extraction is not part of the residual theorem claim.

# The terminal depth-fibre atlas {#sec:fibres}

The endpoint formula [\[eq:endpoint-formula\]](#eq:endpoint-formula){reference-type="eqref" reference="eq:endpoint-formula"} absorbs every component after the first into the interior of one primitive path. Inverting it amounts to choosing how many final primitive components of the target interior should be moved back outside.

[\[thm:fibres\]]{#thm:fibres label="thm:fibres"} Let $T=UQD\in\mathcal D_n$ be primitive, and let $Q=Q_1\cdots Q_r$ be the primitive factorisation of its interior. For each $0\leq d\leq r$, the path $P_d$ in [\[eq:source-formula\]](#eq:source-formula){reference-type="eqref" reference="eq:source-formula"} is the unique path satisfying $$\operatorname E(P_d)=T,
                    \qquad \tau(P_d)=d.$$ There is no basin state of $T$ at any other depth.

Fix $d\in\{0,\ldots,r\}$. The word $$UQ_1\cdots Q_{r-d}D$$ is primitive because its interior is a Dyck path. The suffix $Q_{r-d+1},\ldots,Q_r$ consists of $d$ primitive paths. Hence $P_d$ has exactly $d+1$ primitive factors. By [\[cor:clock\]](#cor:clock){reference-type="ref" reference="cor:clock"}, its depth is $d$, and the endpoint formula gives $$\operatorname E(P_d)=UQ_1\cdots Q_{r-d}Q_{r-d+1}\cdots Q_rD=T.$$ This proves existence.

For uniqueness, take any $P$ with $\operatorname E(P)=T$ and $\tau(P)=d$. The clock implies that $P$ has $d+1$ primitive factors, say $$P=B_1B_2\cdots B_{d+1},
                         \qquad B_1=UAD.$$ Its endpoint is $UA B_2\cdots B_{d+1}D$. Equality with $UQD$ implies $$\label{eq:interior-split}
                         Q=A B_2\cdots B_{d+1}.$$ Because $A$ is a Dyck path, the boundary immediately after $A$ is a return of $Q$ unless $A$ is empty. Each $B_i$ for $i\geq2$ is primitive. Therefore the unique factorisation of $Q$ into primitive paths forces $$A=Q_1\cdots Q_{r-d},\qquad
 (B_2,\ldots,B_{d+1})=(Q_{r-d+1},\ldots,Q_r).$$ Thus $P=P_d$. The same argument shows that $d$ must lie between $0$ and $r$, so no other depth occurs.

The boundary cases are included in the construction. If $r=0$, then $T=UD$ and only $d=0$ occurs. For arbitrary $r$, the case $d=0$ gives $P_0=T$, while $d=r$ gives $P_r=(UD)Q_1\cdots Q_r$.

In the ordered-tree language of [\[eq:tree-graft\]](#eq:tree-graft){reference-type="eqref" reference="eq:tree-graft"}, the fixed target has a root with one child $S$, and $Q_1,\ldots,Q_r$ encode the ordered children of $S$. The source $P_d$ is obtained by lifting the last $d$ children of $S$, in order, to become root-level siblings after $S$. Hence the suffix-cut and suffix-lift descriptions are the same elementary inverse operation; the graft/lift representation itself receives zero contribution credit.

[\[cor:max-fibre\]]{#cor:max-fibre label="cor:max-fibre"} Equations [\[eq:terminal-polynomial\]](#eq:terminal-polynomial){reference-type="eqref" reference="eq:terminal-polynomial"}--[\[eq:largest-target\]](#eq:largest-target){reference-type="eqref" reference="eq:largest-target"} hold.

By [\[thm:fibres\]](#thm:fibres){reference-type="ref" reference="thm:fibres"}, the coefficient of $u^d$ in $\mathcal B_T(u)$ is one for $0\leq d\leq r$ and zero otherwise. This proves [\[eq:terminal-polynomial\]](#eq:terminal-polynomial){reference-type="eqref" reference="eq:terminal-polynomial"}; in particular, the ordinary fibre size is $\mathcal B_T(1)=r+1$.

The interior $Q$ has semilength $n-1$. Since every $Q_i$ has positive semilength, $r\leq n-1$, and hence $\mathcal B_T(1)\leq n$. Equality forces all $r=n-1$ factors to have semilength one. The only primitive factor of semilength one is $UD$, so equality occurs exactly when $Q=(UD)^{n-1}$. This gives the unique target [\[eq:largest-target\]](#eq:largest-target){reference-type="eqref" reference="eq:largest-target"}.

The terminal atlas is pointwise: it identifies the source word, not merely the number of sources. It also records when each source enters the fixed set, rather than collapsing all depths into one ordinary fibre count.

# Exact finite controls {#sec:controls}

The standard-library program `verify_p144.py` supplies finite counterexample pressure. It generates every Dyck path of semilength at most twelve. The literal map is implemented from the first two return positions, whereas the closed iterate is implemented separately from the initial primitive-factor list. Basin profiles are accumulated from the enumerated functional graph and compared with the constructive source formula for every fixed target and every feasible depth.

::: {#tab:controls}
    $n$    states   fixed targets   maximum depth   maximum fibre   assertions
  ----- --------- --------------- --------------- --------------- ------------
      1         1               1               0               1           24
      4        14               5               3               4          277
      8     1,430             429               7               8       28,901
     12   208,012          58,786              11              12    4,308,839

  : Selected exact control sizes. The audit is exhaustive within each displayed semilength and uses no random sampling.
:::

Across semilengths $1$ through $12$, the run covers $290{,}511$ states and $82{,}500$ fixed targets. It performs $6{,}005{,}502$ exact assertions and ends in `STATUS=PASS`. The frozen transcript is `verification_output.txt`. The audit checks closure, factor drop, every iterate, every temporal layer, the unique sharp source, all terminal depth profiles, and the unique maximum target.

Finite enumeration does not prove an all-parameter identity. The proofs in [\[sec:clock,sec:layers,sec:fibres\]](#sec:clock,sec:layers,sec:fibres){reference-type="ref" reference="sec:clock,sec:layers,sec:fibres"} establish the theorem; the program can only reveal errors within its exhaustive range. It also supplies no evidence about priority or ownership.

# Ownership boundary and conclusion {#sec:ownership}

The ownership subtraction is now explicit. Huang--Tamari and the $m$-Tamari path literature own the lattice and atomic cover background [@HuangTamari1972Associativity; @BousquetMelouFusyPrevilleRatelle2012Intervals]. Pallo's right-arm rotations and Chapoton's Dyck-path comparison own the comb order and its height-zero cover characterisation [@Pallo2003RightArm; @Chapoton2020DyckOrder]. Pallo's later leftmost left-rotation supplies a direct precedent for a unique deterministic leftmost-rotation scheduler, a rooted rotation tree, a grading, and a distance [@Pallo2006Rotational]. Its unique terminal root separates that map from $\Phi_n$, whose terminal set has size $\operatorname{Cat}_{n-1}$, but the general leftmost-scheduling idea is not residual here.

Prime factorisation and component enumeration are also direct background [@PanayotopoulosSapounakis2002Prime]. The standard contour bijection [@Stanley2015Catalan] turns the literal move into the root-child graft [\[eq:tree-graft\]](#eq:tree-graft){reference-type="eqref" reference="eq:tree-graft"}, makes the clock root degree minus one, and turns the inverse formula into a suffix lift. We therefore assign zero separate credit to the scheduler, atomic or ground-level rotations, primitive decomposition, comb/height-zero correspondence, root-degree clock, graft/lift representation, ballot layers, Catalan enumeration, and generic coefficient extraction.

After those deductions, the only retained internal residual is the exact conjunction, for the particular map [\[eq:literal-map\]](#eq:literal-map){reference-type="eqref" reference="eq:literal-map"}, of the all-time iterate formula with the targetwise assertion that every feasible depth has one specified preimage. Its polynomial and extremal consequences are kept only as consequences of that conjunction. This is a bookkeeping residual, not a novelty or ownership claim: the bounded searches recorded in the source ledger did not establish an owner, but a non-hit provides no priority evidence. We do not classify other schedulers or arbitrary chains. The manuscript therefore remains owner-thin and anonymous under [hold\_external]{.smallcaps}.
