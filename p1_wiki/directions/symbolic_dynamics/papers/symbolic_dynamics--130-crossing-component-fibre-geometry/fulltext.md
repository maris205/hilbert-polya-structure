---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--130-crossing-component-fibre-geometry"
canonical_tex: "symbolic_dynamics/papers/130-crossing-component-fibre-geometry/main.tex"
canonical_pdf: "symbolic_dynamics/papers/130-crossing-component-fibre-geometry/main.pdf"
source_sha256: "70f020aa1b89353b94f76b781bee19e6c6fbc2d56824431d95090e3e4fcb033a"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Fibre Geometry of a Cut-Dependent Crossing-Component Retraction

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/130-crossing-component-fibre-geometry>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/130-crossing-component-fibre-geometry/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/130-crossing-component-fibre-geometry/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/130-crossing-component-fibre-geometry/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/130-crossing-component-fibre-geometry/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Fix a cut in a chord matching and, simultaneously for every component of its crossing graph, replace the component by consecutive pairs on the same endpoint support. This is a one-step retraction onto noncrossing matchings. For a target matching $T$, its nesting forest turns the inverse problem into independent choices on the ordered lists of immediate siblings. We prove an all-size bijection: partition each sibling list noncrossingly and decorate every part by a crossing-connected matching. It gives the pointwise fibre product $$|\Phi_n^{-1}(T)|=\prod_v a_{d_T(v)},$$ where $d_T(v)$ is a child degree, including the virtual root, and $a_d$ is the already-known noncrossing-partition transform of connected chord diagrams. Strict supermultiplicativity then identifies the consecutive matching as the unique largest-fibre target. Component decompositions, parallel parts, Catalan counts, the transform and its coefficient sequence are explicitly treated as background. The owner search is bounded; no novelty or priority claim is made, and external release remains on hold.
author:
- Anonymous
bibliography:
- references.bib
title: |
  Fibre Geometry of a Cut-Dependent\
  Crossing-Component Retraction
```

## Markdown 正文

# The rooted map and the subtraction boundary

Put the endpoints $1<\cdots<2n$ on a circle with a fixed cut immediately before $1$. Let $\mathcal M_n$ be the perfect matchings of these endpoints. Thus "rooted" means the fixed linear order, not a distinguished chord. Chords $(a,b)$ and $(c,d)$, written with smaller endpoint first, *cross* when $a<c<b<d$ or $c<a<d<b$. The crossing graph $G(M)$ has the chords of $M$ as vertices and these crossings as edges.

For a component $K$ of $G(M)$, sort all its endpoints as $s_1<\cdots<s_{2k}$. Define $\Phi_n(M)$ by replacing, simultaneously for every component, its chords by $$(s_1,s_2),(s_3,s_4),\ldots,(s_{2k-1},s_{2k}).          \label{eq:map}$$ The cut is essential: rotating an unrooted diagram need not commute with [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"}.

We record the ownership boundary before proving anything. Kreweras owns the classical noncrossing-partition framework [@Kreweras1972]; Flajolet--Noy own connected chord-diagram decomposition and enumeration [@FlajoletNoy2000]; and Nabergall gives a decorated even-block decomposition in this setting [@Nabergall2022]. Acan treats chord intersection graphs and their components [@Acan2017]. Callan owns the generic noncrossing-partition transform [@Callan2008], while Alman--Lian--Tran directly enumerate the full-wiring sequence that occurs below, including its recurrence and asymptotics [@AlmanLianTran2015]. Igusa's definition of parallel parts and his adjacency criterion [@Igusa2025 Definition 1.7 and Proposition 1.8] specialize exactly to the nonempty matching sibling lists used below: top-level chords are maximal parts, while members of a nonempty list of immediate siblings are covered by the same parent chord and no endpoint of that parent lies between them. Degree-zero lists contribute only the singleton $\mathcal A_0$ bookkeeping factor. Sibling localization and compatible noncrossing merging therefore receive zero credit, as does Thomas Lam's uncrossing order on matchings [@Lam2015]. In particular, the Lam paper is by *Thomas Lam*, not by Alman--Lian--Tran. We claim only the literal cut-dependent section together with its connected decorations, target-wise fibre product and unique maximizer. The bounded search found no direct owner of that conjunction; a bounded non-hit is not a novelty certificate.

For a matching $M$, let $\pi(M)$ be the partition of $[2n]$ into endpoint supports of the components of $G(M)$. The classical component-support lemma says that $\pi(M)$ is a noncrossing partition into even blocks [@FlajoletNoy2000; @Nabergall2022]. If $P$ is such a partition, let $s(P)$ pair successive elements of each block. Then $$\Phi_n=s\circ\pi.              \label{eq:factor}$$

[\[prop:retraction\]]{#prop:retraction label="prop:retraction"} The map $\Phi_n$ is a retraction onto the noncrossing matchings: $$\Phi_n^2=\Phi_n,
 \qquad \operatorname{im}\Phi_n=\operatorname{Fix}\Phi_n=\operatorname{NC}_2(n).$$ Hence the image and fixed-set size is $\operatorname{Cat}_n$, every nonfixed state has depth one and indegree zero, and $$\zeta_{\Phi_n}(z)=(1-z)^{-\operatorname{Cat}_n}.$$ For $n=0$, $\mathcal M_0=\{\varnothing\}$, $(-1)!!=\operatorname{Cat}_0=1$, and the empty matching is fixed.

Equation [\[eq:factor\]](#eq:factor){reference-type="eqref" reference="eq:factor"} makes every image noncrossing. A noncrossing matching has singleton crossing components and is unchanged, proving the retraction statements and the Catalan count. If $\Phi(y)=x$ then $\Phi(x)=\Phi^2(y)=x$, so a nonfixed $x$ has no predecessor. Finally every positive iterate has the same $\operatorname{Cat}_n$ fixed points, which gives the stated fixed-$n$ Artin--Mazur zeta function. These are formal consequences of a one-step retraction and receive no contribution credit.

# The section fibre and its sibling inverse

Fix $T\in\operatorname{NC}_2(n)$. Its *nesting forest* has one vertex per chord: a chord $x=(a,b)$ is below the least chord $(c,d)$ satisfying $c<a<b<d$, if one exists. Add a virtual root $\widehat0$ above all top-level chords. Children are ordered from left to right. Write $d_T(v)$ for the number of immediate children of $v$, including $v=\widehat0$.

Let $c_k$ be the number of crossing-connected matchings on $[2k]$ and put $c_1=1$. Define $\mathcal A_d$ to consist of a noncrossing partition $\rho\in\operatorname{NC}(d)$ together with, for every block $B$ of $\rho$, a crossing-connected matching on $[2|B|]$. Set $$a_d=|\mathcal A_d|
     =\sum_{\rho\in\operatorname{NC}(d)}\prod_{B\in\rho}c_{|B|},
 \qquad a_0=1.                                         \label{eq:ad}$$

We use one elementary property repeatedly: if $P$ is a noncrossing partition and $B$ is one of its blocks, every other block lies in one of the open cyclic gaps between consecutive elements of $B$. This is equivalent to the absence of alternating elements from two blocks.

[\[thm:inverse\]]{#thm:inverse label="thm:inverse"} For every $T\in\operatorname{NC}_2(n)$, extraction from a source gives a bijection $$\Phi_n^{-1}(T)
 \longleftrightarrow
 \prod_{v\in V(T)\cup\{\widehat0\}}\mathcal A_{d_T(v)}. \label{eq:bijection}$$ Consequently $$|\Phi_n^{-1}(T)|
          =\prod_{v\in V(T)\cup\{\widehat0\}}a_{d_T(v)}. \label{eq:fibre}$$

We prove the promised inverse in four directions.

*Step 1: forward localization.* Take $M\in\Phi_n^{-1}(T)$ and set $P=\pi(M)$. For a block $B=\{b_1<\cdots<b_{2k}\}$ of $P$, its section chords are $x_i=(b_{2i-1},b_{2i})$. They are pairwise disjoint, so no two are in an ancestor--descendant relation. We claim that they are immediate siblings. If $x_i$ has parent $p_i$, the endpoints of $p_i$ belong to a different block of $P$. By the cyclic-gap property, those endpoints can enclose $x_i$ only by lying on opposite sides in the outer gap of $B$; hence $p_i$ encloses *every* element of $B$. Thus the parents of any two $x_i$ and $x_j$ both enclose all section chords. They are comparable by nesting, and if they were unequal, say $p_i$ lay strictly inside $p_j$, then $p_i$ would enclose $x_j$ as well. Thus $p_i$ would be a strict intermediate container between $x_j$ and its alleged immediate parent $p_j$, a contradiction. Hence all parents coincide. If one $x_i$ is top-level, any parent of another $x_j$ would enclose $x_i$ as well, again a contradiction. The claim follows, with the virtual root in the top-level case.

For a fixed parent $v$, the $P$-blocks therefore group its ordered sibling list. These groups form a noncrossing partition of the sibling indices. Indeed, groups containing indices $i<k$ and $j<\ell$, with $i<j<k<\ell$, would give alternating endpoints from their two $P$-blocks, contrary to noncrossing of $P$. We have extracted a unique $\rho_v\in\operatorname{NC}(d_T(v))$ for every $v$.

*Step 2: converse section construction.* Conversely choose all $\rho_v$ independently. For each block $Q$ of $\rho_v$, form an endpoint block $B_Q$ by taking both endpoints of the siblings indexed by $Q$. Every target chord is a child exactly once and every sibling index belongs to one block of its $\rho_v$; hence the $B_Q$ are disjoint and cover $[2n]$. They therefore form an even-block partition $P$.

We prove that $P$ is noncrossing by induction from the leaves. Assume for a parent $v$ that the blocks constructed strictly below each child already form a noncrossing partition inside that child's open interval. At $v$, nonalternation of the index blocks in $\rho_v$ is exactly nonalternation of the corresponding endpoint blocks. Fix a child $x=x_i=(a,b)$ and a parent-level block $B_Q$. If $i\in Q$, then $a,b$ are consecutive in the sorted list of $B_Q$, so the descendant interval $I_x=(a,b)$ is a gap of $B_Q$. If $i\notin Q$, the whole closed support $[a,b]$ lies strictly inside one gap of $B_Q$ (the outer cyclic gap when all members of $Q$ lie on one side). Thus every block constructed strictly below $x$, being contained in $I_x$, lies in one gap of every parent-level block. Blocks below different children lie in disjoint intervals, and the already distinct $B_Q$ neither merge nor alternate across levels. The leaf induction therefore proves noncrossing in every chord subtree. The same two-case argument for the top-level children at the virtual root closes the induction and proves that no two blocks of $P$ cross.

If $Q=\{i_1<\cdots<i_r\}$, the elements of $B_Q$ occur as the left and right endpoints of child $i_1$, then those of child $i_2$, and so on. Descendant endpoints lie inside these chord intervals but are in other blocks. Successive pairing inside $B_Q$ therefore recovers precisely those siblings. Every chord is a child exactly once, so $s(P)=T$.

*Step 3: connected decorations.* For each $Q$, choose the connected matching recorded by its $\mathcal A$-decoration and transport it order-preservingly from $[2|Q|]$ to $B_Q$. Take the union over all $Q$ and all parents. Chords on distinct blocks cannot cross because $P$ is noncrossing; within $B_Q$ the decoration is crossing-connected. Thus the crossing components of the constructed source $M$ have supports *exactly* the blocks $B_Q$. It follows that $\pi(M)=P$ and $\Phi_n(M)=s(P)=T$.

*Step 4: mutual inverse.* Starting from $M$, its crossing components recover $P$ uniquely. Step 1 recovers the unique sibling groups, and order-standardizing each component recovers its connected decoration. Step 3 then returns the same chords of $M$. In the other direction, Step 3 proves that the constructed blocks are the exact crossing components, so extraction returns every chosen $\rho_v$ and decoration. The constructions are mutual inverses in every size, including repeated block sizes and the virtual-root case. Independence over $v$ now gives [\[eq:bijection\]](#eq:bijection){reference-type="eqref" reference="eq:bijection"} and [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"}.

For the noncrossing endpoint partition whose parts are the chords of $T$, each nonempty immediate-sibling list (including the nonempty top-level list) is exactly an Igusa parallel set [@Igusa2025 Definition 1.7]; his [@Igusa2025 Proposition 1.8] also owns the compatible-merge criterion. An empty child list contributes only the singleton factor $\mathcal A_0$ and is not identified with an Igusa parallel set. The localization and static merge geometry in Steps 1--2 are therefore fully zero-credit. The residual is only their use inside this specified cut-dependent section, where connected decorations identify the exact crossing components and yield every target fibre. The nesting forest is a proof coordinate, not a tree dynamic. This separates the result from the cyclic partition shift--join dynamics of P110 (whose deepest-shell witness uses one two-element chord block), the tree involution of P120, graph-component complementation in P123, and the run/composition maps P117, P122 and P126. Componentwise behavior alone receives no portfolio credit.

# Formal transform and the unique largest fibre

Let $$C(u)=\sum_{k\ge1}c_ku^k,
 \qquad A(u)=\sum_{d\ge0}a_du^d.$$ The owned noncrossing-partition transform applied to [\[eq:ad\]](#eq:ad){reference-type="eqref" reference="eq:ad"} gives the identity of *formal* ordinary power series $$A(u)=1+C\bigl(uA(u)\bigr).      \label{eq:formal}$$ There is no convergence or asymptotic claim: connected chord counts grow factorially. The first values are

    $d$      0   1   2   3    4     5      6       7
  ------- ---- --- --- --- ---- ----- ------ -------
   $c_d$    --   1   1   4   27   248   2830   38232
   $a_d$     1   1   2   8   52   464   5184   68928

This is an all-size identification, not an inference from the displayed prefix: the owned decomposition of full wiring diagrams into connected pieces underlying [\[eq:formal\]](#eq:formal){reference-type="eqref" reference="eq:formal"} identifies $\mathcal A_d$ with that class for every $d$. Thus $a_d=X_d$ in the notation of Alman--Lian--Tran. Their Theorem 4.1.6 gives the full-wiring recurrence, Remark 4.1.7 identifies the sequence A111088, Theorem 4.1.8 gives its coefficient identity, and Theorem 4.2.1 gives its asymptotic [@AlmanLianTran2015]. All of those enumerative facts, as well as the transform itself, receive zero credit here.

[\[thm:max\]]{#thm:max label="thm:max"} For every $n\ge0$, the unique largest fibre of $\Phi_n$ lies over the consecutive matching $$T_n^{\mathrm{con}}=(1,2)(3,4)\cdots(2n-1,2n),$$ and has size $a_n$.

For $i,j>0$, juxtaposition gives an injection $\mathcal A_i\times\mathcal A_j\hookrightarrow\mathcal A_{i+j}$. It is not onto: a one-block noncrossing partition with a connected $(i+j)$-chord decoration is outside its image. Such a decoration exists in every size $k=i+j$: pair $r$ with $r+k$ for $1\le r\le k$, making all chords cross. Therefore $$a_i a_j<a_{i+j}.                \label{eq:strict}$$

Every chord has exactly one parent in the virtual-rooted forest, so $\sum_v d_T(v)=n$. Repeated use of [\[eq:strict\]](#eq:strict){reference-type="eqref" reference="eq:strict"}, with $a_0=1$, shows that the product in [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"} is at most $a_n$, strictly unless only one vertex has positive child degree. A chord vertex cannot have all $n$ chords as children, since it would be an additional chord; hence that sole vertex must be $\widehat0$. All chords are then top-level. A noncrossing chord spanning a nonempty interval would contain another chord, so every chord is consecutive and $T=T_n^{\mathrm{con}}$. Conversely this target has $d_T(\widehat0)=n$ and all other degrees zero, giving fibre size $a_n$. The empty case has the sole empty target and uses $a_0=1$.

[\[cor:census\]]{#cor:census label="cor:census"} For every $n\ge0$, $$\sum_{T\in\operatorname{NC}_2(n)}\prod_v a_{d_T(v)}=(2n-1)!!.$$ The consecutive target has fibre $a_n$, whereas the fully nested rainbow target has fibre $1$; the fibres are already nonuniform at $n=2$.

The sum partitions the finite domain $\mathcal M_n$ into the fibres of [\[thm:inverse\]](#thm:inverse){reference-type="ref" reference="thm:inverse"}. For the rainbow target every positive child degree is one and $a_1=1$.

# Exact finite control and claim ceiling

A paper-local standard-library verifier exhausts all matchings through seven chords: 146,600 states including the empty state and 626 noncrossing targets. It checks the literal map, component-support noncrossing, idempotence, forward sibling extraction, [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"}, the formal coefficients, strict inequalities, and an independent converse construction that rebuilds every one of the 146,600 sources. The canonical run makes 735,609 assertions. This is counterexample pressure, not a replacement for the all-size proof above.

The admissible contribution ceiling is exactly [\[thm:inverse,thm:max\]](#thm:inverse,thm:max){reference-type="ref" reference="thm:inverse,thm:max"} for the specified cut-dependent map. The Catalan image, idempotence, zeta, component counts, A111088, [\[eq:formal\]](#eq:formal){reference-type="eqref" reference="eq:formal"}, generic parallel-part geometry, and generic uncrossing are background. No analytic asymptotic, unrooted canonicity, novelty, priority, or external-release assertion is made.
