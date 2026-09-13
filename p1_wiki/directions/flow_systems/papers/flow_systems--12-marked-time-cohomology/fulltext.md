---
p1_kind: "derived-fulltext-reading-copy"
route: "flow_systems"
logical_paper_id: "flow_systems--12-marked-time-cohomology"
canonical_tex: "flow_systems/papers/12-marked-time-cohomology/paper/manuscript.tex"
canonical_pdf: "flow_systems/papers/12-marked-time-cohomology/paper/paper.pdf"
source_sha256: "c6ad0f8c22d68840198d744a615da06e8b062d5ccdbeedb7f4ee76bf35073163"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Marked Time Cohomology and Orbitwise Standardization of Indiscrete Arithmetic Action Groupoids

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../flow_systems/papers/12-marked-time-cohomology>)
- [规范 TeX](<../../../../../flow_systems/papers/12-marked-time-cohomology/paper/manuscript.tex>)
- [关联 PDF](<../../../../../flow_systems/papers/12-marked-time-cohomology/paper/paper.pdf>)
- [支撑 Markdown](<../../../../../flow_systems/papers/12-marked-time-cohomology/README.md>)
- [BibTeX](<../../../../../flow_systems/papers/12-marked-time-cohomology/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Let a nonempty set carry a right real action and one global indiscrete topology. We define a globally continuous, unnormalized nerve cochain complex and prove, in every finite degree, that cochains with a $T_0$ coefficient target factor through time. For real coefficients the actual action groupoid has $H^1_{\mathrm{cnv}}=\mathbb R[c]$, $c(x,t)=t$, and its degree-one coboundaries vanish. On every unit of the fixed-prime packet, the source-normalized marked class has isotropy image $(\log p)\mathbb Z$. Strict maps preserve this subgroup, positive scaled maps transform it covariantly, and weaker categories admit explicit non-descent. When all stabilizers are the same cocompact lattice $H=L\mathbb Z$, the same carrier admits a section-free coproduct of standard $\mathbb R/H$ orbit topologies; this construction is fully faithful with global indiscretization. Its canonical automorphism extension has kernel $(\mathbb R/H)^Q$, while a split requires choices of orbit origins and is noncanonical. The standardized groupoid satisfies $H^1_{\mathrm{cnv}}=\mathbb R^Q$, the full algebraic Cartesian product, and its coboundaries are generally nonzero. The continuous identity $J:G_{\mathrm{std}}\to G_{\mathrm{actual}}$ induces the constant diagonal, exactly the strict-automorphism invariant subspace. The packet application uses only the bare nonempty orbit set: it transfers no count, measure, or actual quotient topology. Deterministic finite controls support reproducibility but replace neither proof nor source verification. We obtain no higher standardized cohomology, cohomology topology, trace, determinant, analytic continuation, or operator lift.

  **Keywords:** marked time cohomology; indiscrete action groupoid; orbitwise standardization; common period lattice; arithmetic flow; invariant diagonal
author:
- |
  Liang Wang\
  Huazhong University of Science and Technology\
  Academic unit and corresponding-author status: AUTHOR TO CONFIRM\
  <wangliang.f@gmail.com>
bibliography:
- references.bib
date: 15 August 2026
title: |
  **Marked Time Cohomology and Orbitwise Standardization\
  of Indiscrete Arithmetic Action Groupoids**
```

## Markdown 正文

**中文摘要**

设非空集合带实数右作用及整体不可分拓扑。我们定义整体连续、非正规化的神经上链复形，并证明对每个有限次数，取值于 $T_0$ 群的上链均经时间坐标分解。取实系数时，实际作用群胚满足 $H^1_{\mathrm{cnv}}=\mathbb R[c]$，且一次余边界为零。在固定素数包的每个单位上，源归一化标记类的迷向像为 $(\log p)\mathbb Z$；严格映射保持它，正比例映射使其协变，而较弱范畴存在明确的不下降反例。若各点稳定子同为余紧格 $H=L\mathbb Z$，则同一载体具有不依赖截面的标准 $\mathbb R/H$ 轨道拓扑余积，并与整体不可分化构成满且忠实的对应。其典范自同构正合列之核为 $(\mathbb R/H)^Q$；选择轨道原点才能得到非典范分裂。标准化群胚满足 $H^1_{\mathrm{cnv}}=\mathbb R^Q$，这里是完整代数直积，且标准化一次余边界通常非零。连续恒等函子 $J:G_{\mathrm{std}}\to G_{\mathrm{actual}}$ 诱导常值对角，其像恰为严格自同构不变子空间。固定素数应用只使用非空裸轨道集，不转移计数、测度或实际商拓扑。确定性有限控制仅支持复现，不能替代证明与来源核验。本文不建立更高次标准化上同调、上同调拓扑、迹、行列式、解析延拓或算子提升。

**中文关键词：** 标记时间上同调；不可分作用群胚；逐轨道标准化；共同周期格；算术流；不变对角

# Introduction {#sec:introduction}

Periodic time is easy to see set-theoretically and easy to lose categorically. If a real action is presented on a Hausdorff circle, its period lattice is built into the familiar quotient $\mathbb R/L\mathbb Z$. If the same carrier inherits one global indiscrete topology, every continuous map to a $T_0$ target forgets the unit coordinate. The marked time cocycle survives, but the topology no longer separates even distinct orbits. This paper makes the comparison without identifying the two topologies.

The arithmetic motivation comes from Deninger's suspension construction. In arXiv version 4, Section 6 and Theorem 6.1 on physical pp. 38--39 give the fixed-prime right flow, multiplicative isotropy $p^{\mathbb Z}$ at every packet point, and the logarithmic clock; additive time therefore gives the common stabilizer $(\log p)\mathbb Z$ [@Deninger2026Dynamical]. Equations (38)--(39) there are set parametrizations, not topology transport. A companion analysis establishes the globally indiscrete topology of the actual fixed-prime packet [@Wang2026PacketSeparation]; another studies its separated reflections [@Wang2026SeparatedReflections]; and a third supplies the range-first action-groupoid and convolution context [@Wang2026ContinuousConvolution]. We use those records only at those ceilings. The generic theorems below are proved from their stated hypotheses, so they do not depend on the public availability of a companion.

There are two mathematical layers. The first is the actual indiscrete layer. We compute every finite nerve chart, define the author-specific complex $C_{\mathrm{cnv}}^\bullet$, prove $d^2=0$ directly, and show that the full complex factors through time for $T_0$ coefficients. In real degree one, the continuous Cauchy equation leaves precisely the line generated by $c(x,t)=t$. Restriction to isotropy then turns the marked class into the subgroup $\lambda H_x\subset\mathbb R$.

The second layer assumes a common cocompact stabilizer $H=L\mathbb Z$, $L>0$. Every orbit receives its standard quotient topology, independently of an origin, and the carrier receives the coproduct topology. The ordinary facts about $\mathbb R/H$ and topological coproducts provide background [@EoMTopologicalGroup; @EoMHomogeneousSpace; @Stacks0B1W]; the same-carrier construction, its uniqueness, its exact categorical inverse, its automorphism extension, and its cohomology comparison are proved here.

The central statement is the following comparison, in which $Q=X/\mathbb R$ is a nonempty bare set and $\mathbb R^Q$ is the full algebraic Cartesian product.

[\[thm:main\]]{#thm:main label="thm:main"} Let $X$ be a nonempty globally indiscrete right $\mathbb R$-set with $\operatorname{Stab}_{\mathbb R}(x)=H=L\mathbb Z$ for every $x$, where $L>0$. Let $G_{\mathrm{actual}}$ be its range-first action groupoid with mark $c(x,t)=t$, and let $G_{\mathrm{std}}$ be the same-set orbitwise standardization. Then $$\label{eq:central-map}
\begin{aligned}
 H_{\mathrm{cnv}}^1(G_{\mathrm{actual}};\mathbb R)=\mathbb R[c]
 &\xrightarrow{\ J^*\ }
 H_{\mathrm{cnv}}^1(G_{\mathrm{std}};\mathbb R)=\mathbb R^Q,\\
 \operatorname{im}(J^*)&=(\mathbb R^Q)^{\operatorname{Aut}_{\mathbb R}(G_{\mathrm{std}})}\\
 &=\{\text{constant functions }Q\to\mathbb R\}.
\end{aligned}$$ Here $J:G_{\mathrm{std}}\to G_{\mathrm{actual}}$ is the continuous identity marked functor, and $\operatorname{Aut}_{\mathbb R}$ means strict time-preserving equivariant automorphisms. No topology is imposed on $\mathbb R^Q$, either cohomology group, or the automorphism group.

This theorem is the paper's center. The actual collapse is its input, not its conclusion, and the automorphism computation is a mechanism for the invariant statement rather than an arithmetic selection principle. The proof also keeps the variance straight: $J$ goes from the finer standard topology to the actual indiscrete topology, while cohomological pullback goes from actual to standard.

The closest formal action-groupoid lift/descent comparison we found is Gepner--Meier's Proposition 2.15, printed p. 2647, in compactly generated weak-Hausdorff spaces [@GepnerMeier2023]. A nontrivial globally indiscrete unit space is not weak Hausdorff, so that result is context, not a proof imported to the actual owner. Finite wreath phenomena occur in Guillou--May, Proposition 5.19, printed p. 3311 [@GuillouMay2017], and in Alp--Wensley, Section 3.1, published p. 481 [@AlpWensley2010]. Their finite hypotheses do not supply the arbitrary set-indexed extension here. The direct continuous-cohomology comparators are likewise kept within their audited domains: the one-object conditional comparison of Blanco--Uribe--Waldorf, Section 2.4 and Lemmas 2.3 and 2.5 [@BlancoUribeWaldorf2023]; the degree-one terminology of Farsi--Huang--Kumjian--Packer, Definition 3.7, printed p. 3336 [@FarsiHuangKumjianPacker2022]; the one-object loop-contractible comparison of Fuchssteiner--Wockel, Corollary II.8, author p. 7 [@FuchssteinerWockel2012]; and Mackenzie's different rigid theory under its locally trivial Hausdorff hypotheses, Theorem 3, printed pp. 298--299 [@Mackenzie1978]. None is renamed as the complex defined below.

A bounded source search through 2026-08-15 supports the status `SUPPORTED_WITHIN_SEARCH`. It did not identify a direct same-domain precedent for the exact conjunction in [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}. This is a dated search statement, not an absolute priority claim.

# Owners, conventions, and morphism boundaries {#sec:conventions}

Let $X$ be a nonempty set with a right action of the additive group $\mathbb R$, written $x\mathbin{\cdot}t$. Unless standardization is explicitly invoked, $X$ carries the global indiscrete topology. The range-first action groupoid is $$\label{eq:groupoid-operations}
 G=X\rtimes\mathbb R,\quad
 r(x,t)=x,\quad s(x,t)=x\mathbin{\cdot}t,\quad
 (x,t)(x\mathbin{\cdot}t,u)=(x,t+u),\quad
 (x,t)^{-1}=(x\mathbin{\cdot}t,-t).$$ The arrow topology is the product of the indiscrete topology on $X$ and the usual topology on $\mathbb R$. The marked coordinate is $$\label{eq:mark}
 c:G\longrightarrow\mathbb R,\qquad c(x,t)=t.$$ It is part of the object, not a class selected by the unmarked groupoid.

A *strict* marked isomorphism $F:(G,c)\to(G',c')$ satisfies $c'\circ F=c$. A *positive scaled* isomorphism is a pair $(F,\alpha)$, $\alpha>0$, with $c'\circ F=\alpha c$. An *unmarked* isomorphism has no equation involving $c$. Scaled composition multiplies the scale factors, and inversion replaces $\alpha$ by $\alpha^{-1}$. These are three different categories. In particular, an equality of period subgroups is not a converse characterization of strictness.

For a strict isomorphism, range and the marked value determine the arrow, so necessarily $$\label{eq:strict-normal-form}
 F(x,t)=(F_0(x),t),\qquad
 F_0(x\mathbin{\cdot}t)=F_0(x)\mathbin{\cdot}t.$$ The inverse gives an equivariant orbit bijection. Moreover $$\label{eq:stabilizer-strict}
 t\in\operatorname{Stab}_{\mathbb R}(x)
 \quad\Longleftrightarrow\quad
 t\in\operatorname{Stab}_{\mathbb R}(F_0(x)),$$ so a strict arrow preserves each stabilizer as a literal subgroup of the same time line. Conversely, an equivariant bijection of globally indiscrete carriers lifts uniquely by [\[eq:strict-normal-form\]](#eq:strict-normal-form){reference-type="ref" reference="eq:strict-normal-form"}; its arrow map and inverse are continuous because arrow opens have the form $X\times U$.

The terminology $C_{\mathrm{cnv}}/H_{\mathrm{cnv}}$ below always means the author-defined globally continuous unnormalized nerve complex. It is not an unqualified claim about a standard theory of arbitrary topological groupoids. The cited degree-one convention in @FarsiHuangKumjianPacker2022 uses the opposite representative sign for coboundaries; negating a unit function leaves the image subgroup unchanged.

Four fixed-prime records will be used later. They share an underlying orbit set only where the table says so; their topologies and categorical roles are not interchangeable.

P31mmYY Record & Exact type and topology & Prohibited transfer\
$\Gamma_p^{\mathrm{actual}}$ & Actual fixed-prime packet carrier with one global indiscrete topology. & No standard-circle topology is inherited.\
$\Gamma_p^{\mathrm{std}}$ & Same carrier, constructed as a coproduct of open standard $\mathbb R/(\log p)\mathbb Z$ orbits. & It is neither the actual topology nor a separated reflection.\
$Q_p^{\mathrm{actual}}$ & Actual orbit quotient with the indiscrete quotient topology. & No discreteness, count, enumeration, measure, or local triviality.\
$Q_p^{\mathrm{disc}}$ & The same bare orbit set used as the discrete component index of $\Gamma_p^{\mathrm{std}}$. & Its topology is not the topology of $Q_p^{\mathrm{actual}}$.\

# The actual indiscrete complex {#sec:actual}

This section needs no transitivity, stabilizer hypothesis, lattice, or arithmetic label. Let $A$ be a $T_0$ topological abelian group with continuous addition and inversion. Put $G^{(0)}=X$, and for $n\geq1$ let $G^{(n)}$ be the space of composable $n$-tuples with its subspace topology. Define $$\begin{aligned}
\label{eq:nerve-chart}
 \Psi_n(x;t_1,\ldots,t_n)
 ={}&\bigl((x,t_1),(x\mathbin{\cdot}t_1,t_2),\ldots,\\[-2mm]
 &\hspace{14mm}(x\mathbin{\cdot}(t_1+\cdots+t_{n-1}),t_n)\bigr).\end{aligned}$$

[\[prop:nerve\]]{#prop:nerve label="prop:nerve"} For each finite $n\geq1$, $\Psi_n:X\times\mathbb R^n\to G^{(n)}$ is a homeomorphism. The opens in these coordinates are exactly $\varnothing$ and $X\times U$, with $U$ open in $\mathbb R^n$.

Composability forces the successive range coordinates in [\[eq:nerve-chart\]](#eq:nerve-chart){reference-type="ref" reference="eq:nerve-chart"}, so the inverse remembers the first range and all time coordinates. After reordering $G^n=(X\times\mathbb R)^n$ as $X^n\times\mathbb R^n$, finite-product indiscreteness says that every ambient open is $X^n\times U$. Intersecting with the composable locus and pulling back gives $X\times U$, and every such set arises this way. Thus both the chart and its inverse are continuous and open. This is a proof for arbitrary finite $n$, not an inference from arrow degree.

For $n\geq2$, the faces in these coordinates are $$\begin{aligned}
\label{eq:faces}
 \partial_0^n\Psi_n(x;t_1,\ldots,t_n)
  &=\Psi_{n-1}(x\mathbin{\cdot}t_1;t_2,\ldots,t_n),\notag\\
 \partial_i^n\Psi_n(x;t_1,\ldots,t_n)
  &=\Psi_{n-1}(x;t_1,\ldots,t_i+t_{i+1},\ldots,t_n),
       &&1\leq i\leq n-1,\\
 \partial_n^n\Psi_n(x;t_1,\ldots,t_n)
  &=\Psi_{n-1}(x;t_1,\ldots,t_{n-1}).\notag\end{aligned}$$ In degree one, $\partial_0^1=s$ and $\partial_1^1=r$. The degeneracy $\sigma_i^n$ inserts a zero after $t_i$, with the empty endpoint strings omitted. Addition in $\mathbb R$, the action law, and projection show that all these maps are continuous. They also give the simplicial relation $$\label{eq:face-identity}
 \partial_i^{m-1}\partial_j^m
 =\partial_{j-1}^{m-1}\partial_i^m,\qquad 0\leq i<j\leq m.$$ The adjacent case is associativity of addition; the first adjacent case is $(x\mathbin{\cdot}t_1)\mathbin{\cdot}t_2
=x\mathbin{\cdot}(t_1+t_2)$.

[\[def:complex\]]{#def:complex label="def:complex"} For the trivial coefficient bundle $X\times A\to X$, set $$\label{eq:cochains}
 C_{\mathrm{cnv}}^0(G;A)=C(X,A),\qquad
 C_{\mathrm{cnv}}^n(G;A)=C(G^{(n)},A)\quad(n\geq1).$$ All maps are globally continuous. There is no support, boundedness, integrability, smoothness, decay, Borel-only, or normalization condition. For $h\in C_{\mathrm{cnv}}^0$ and $n\geq1$, define $$\begin{aligned}
\label{eq:differential}
 (d^0h)(\gamma)&=h(s\gamma)-h(r\gamma),\notag\\
 d^nf&=\sum_{i=0}^{n+1}(-1)^i(\partial_i^{n+1})^*f.\end{aligned}$$

[\[prop:d-square\]]{#prop:d-square label="prop:d-square"} The maps in [\[eq:differential\]](#eq:differential){reference-type="ref" reference="eq:differential"} are well typed and continuous, and $d^{n+1}d^n=0$ for every $n\geq0$.

Continuity follows from the continuous faces and the topological group operations of $A$. Expand the double differential. For every $i<j$, the term with composite $\partial_i\partial_j$ pairs, by [\[eq:face-identity\]](#eq:face-identity){reference-type="ref" reference="eq:face-identity"}, with the same composite indexed by the inner face $j-1$ and outer face $i$. Their signs are $(-1)^{i+j}$ and $(-1)^{i+j-1}$, so they cancel in the abelian group $A$. These pairs partition the double sum. Degree zero uses the same face identities, which are precisely the action and source/range laws there.

Define $Z_{\mathrm{cnv}}^n=\ker d^n$, $B_{\mathrm{cnv}}^0=0$, $B_{\mathrm{cnv}}^n=\operatorname{im}d^{n-1}$ for $n\geq1$, and $H_{\mathrm{cnv}}^n=Z_{\mathrm{cnv}}^n/B_{\mathrm{cnv}}^n$. These are algebraic groups, or real vector spaces for $A=\mathbb R$. No topology on a cochain group or cohomology quotient is defined.

[\[thm:factorization\]]{#thm:factorization label="thm:factorization"} For every $n\geq0$, every continuous $F:X\times\mathbb R^n\to A$ is independent of the $X$ coordinate. Time projection therefore induces a canonical isomorphism of cochain complexes from the one-object additive group $\mathbb R$, with the same author-defined signs and trivial coefficients, to $C_{\mathrm{cnv}}^\bullet(G;A)$.

For fixed $t\in\mathbb R^n$, the points $(x,t)$ and $(y,t)$ have the same open neighborhoods. If their images under $F$ were distinct, the $T_0$ axiom would provide an open in $A$ containing exactly one image; its inverse image would distinguish the two domain points. Thus $F(x,t)=F(y,t)$. The same argument without a time coordinate proves that every continuous $X\to A$ map is constant.

Choose any $x_0\in X$ only to write an inverse. Time pullback sends a one-object $n$-cochain $f$ to $$\label{eq:time-pullback}
 (T_nf)(\Psi_n(x;t_1,\ldots,t_n))=f(t_1,\ldots,t_n),$$ and evaluation at $x_0$ sends a groupoid cochain back to its value in that chart. The factorization just proved makes these maps inverse and shows that evaluation is independent of $x_0$. Each groupoid face projects to the corresponding one-object face. The first face changes the unit to $x\mathbin{\cdot}t_1$ but simultaneously drops $t_1$, so this statement also holds there. Hence $T_{n+1}d^n=d^nT_n$ in every degree.

The coefficient hypothesis is sharp. If both a two-point carrier and the coefficient group $\mathbb Z/2\mathbb Z$ are indiscrete, a nonconstant degree-zero map is continuous, but it does not factor through a point. Thus the theorem does not silently extend to non-$T_0$ targets.

Now take $A=\mathbb R$ with its usual topology. A continuous one-cochain has the form $b(x,t)=f(t)$ by [\[thm:factorization\]](#thm:factorization){reference-type="ref" reference="thm:factorization"}. In the range-first signs, $$\label{eq:cauchy-cocycle}
 (d^1b)(x;t,u)=f(u)-f(t+u)+f(t),$$ so $b$ is a cocycle exactly when $f$ is additive. The required continuous Cauchy step is elementary and needs no extra bibliographic owner. Additivity gives $f(q)=qf(1)$ for rational $q$. Given $t\in\mathbb R$, choose rationals $q_k\to t$; continuity gives $f(t)=\lim q_kf(1)=tf(1)$. Every continuous unit cochain $X\to\mathbb R$ is constant, so its coboundary vanishes.

[\[thm:actual-h1\]]{#thm:actual-h1 label="thm:actual-h1"} For every nonempty globally indiscrete right $\mathbb R$-action, $$\label{eq:actual-h1}
 Z_{\mathrm{cnv}}^1(G;\mathbb R)=\mathbb Rc,\qquad
 B_{\mathrm{cnv}}^1(G;\mathbb R)=0,
 \qquad H_{\mathrm{cnv}}^1(G;\mathbb R)=\mathbb R[c].$$

This conclusion is algebraic. The coordinate cocycle is not a compactly supported convolution test function: unless zero, it has full arrow-space support. The result classifies the author's real degree-one complex only; it says nothing about higher cohomology or analytic completions. The one-object discussion in @BlancoUribeWaldorf2023 and @FuchssteinerWockel2012, and Mackenzie's rigid transitive theory [@Mackenzie1978], are comparators under their own hypotheses, not names for [\[def:complex\]](#def:complex){reference-type="ref" reference="def:complex"}.

For a unit $x$, put $$\label{eq:isotropy}
 H_x=\operatorname{Stab}_{\mathbb R}(x)=\{t:x\mathbin{\cdot}t=x\},
 \qquad G_x^x=\{(x,t):t\in H_x\}.$$ Restriction of a cocycle to $G_x^x$ is a continuous homomorphism because the cocycle equation on isotropy is additive. Every coboundary vanishes pointwise there: if $t\in H_x$, then $(d^0h)(x,t)=h(x)-h(x)=0$. Thus the following definition is independent of the representative, before using the stronger actual fact $B_{\mathrm{cnv}}^1=0$.

[\[def:period\]]{#def:period label="def:period"} For $[b]\in H_{\mathrm{cnv}}^1(G;\mathbb R)$, define $$\label{eq:period-def}
 \operatorname{Per}_x([b])=\operatorname{im}\bigl(b|_{G_x^x}\bigr)\subset\mathbb R.$$ It is an additive subgroup; it is not asserted to be discrete, closed, or a lattice.

[\[prop:period\]]{#prop:period label="prop:period"} For all $\lambda\in\mathbb R$, $$\label{eq:period-formula}
 \operatorname{Per}_x([\lambda c])=\lambda H_x.$$ If the action is transitive, then $H_x$ and this image are independent of the unit. In particular, if $H_x=L\mathbb Z$, $L>0$, the marked class recovers $\operatorname{Per}_x([c])=L\mathbb Z$.

On isotropy, $(\lambda c)(x,t)=\lambda t$, proving [\[eq:period-formula\]](#eq:period-formula){reference-type="ref" reference="eq:period-formula"}. If $y=x\mathbin{\cdot}u$, commutativity of $\mathbb R$ shows $H_y=H_x$. Conjugation by $(x,u)$ carries $(y,t)$ to $(x,t)$, and a one-cocycle has the same value on these conjugate isotropy arrows because the values on the conjugating arrow and its inverse cancel.

The mark matters. If $[c]$ is forgotten and one ranges over every nonzero class on a lattice orbit, the collection $\{\lambda L\mathbb Z:\lambda\neq0\}$ is $\{r\mathbb Z:r>0\}$, independent of the original $L$. This is a precise scale-blindness statement, not a claim that free, dense-stabilizer, or nontransitive actions have lattice periods.

# Marked categories and the fixed-prime specialization {#sec:categories-packet}

The categories from [2](#sec:conventions){reference-type="ref" reference="sec:conventions"} separate what the marked class does and does not descend to. Suppose $(F,\alpha):(G,c)\to(G',c')$ is a positive scaled isomorphism. It maps $G_x^x$ bijectively to $G'_{F_0(x)}{}^{F_0(x)}$, whence $$\label{eq:scaled-covariance}
 \operatorname{Per}_{F_0(x)}([c'])=\alpha\operatorname{Per}_x([c]),
 \qquad H'_{F_0(x)}=\alpha H_x.$$ The inverse scale proves equality, not only inclusion. Strict maps are the case $\alpha=1$ and preserve the subgroup exactly.

This implication has no converse. For $L,M>0$, give $X_L=\mathbb R/L\mathbb Z$ and $X_M=\mathbb R/M\mathbb Z$ the indiscrete topology, and put $\alpha=M/L$. Then $$\label{eq:dilation}
 F_\alpha([r]_L,t)=([\alpha r]_M,\alpha t)$$ is a topological-groupoid isomorphism, with inverse obtained from $\alpha^{-1}$, and $c_M\circ F_\alpha=\alpha c_L$. It is well defined because $\alpha L=M$; range, source, multiplication, and inverse follow from linearity, while product-topology continuity follows from $X_L\times U\mapsto X_M\times\alpha U$. If $L\neq M$, it is scaled and unmarked but not strict. Thus unequal period generators are isomorphic in the weaker categories. This is existential non-descent, not a universal claim that every unmarked map destroys period data.

Even equality of lattices does not force strictness. Orientation reversal $$\label{eq:orientation-reversal}
 F_-([r]_L,t)=([-r]_L,-t)$$ is an unmarked involution and preserves $L\mathbb Z$ as a set, but $c_L\circ F_-=-c_L$. Because scaled morphisms here require a positive factor, $F_-$ is neither strict nor positive scaled.

The standard quotient $\mathbb R/H$ with its usual Hausdorff topology is therefore a normalized, pointed proxy only. A chosen unit $x$ gives the equivariant set bijection $$\label{eq:pointed-chart}
 \theta_x:\mathbb R/H\longrightarrow X,\qquad [t]\longmapsto x\mathbin{\cdot}t.$$ It is continuous into the actual indiscrete topology; its inverse is not continuous. Changing the basepoint from $x$ to $x'=x\mathbin{\cdot}u$ gives $\theta_{x'}=\theta_x\circ\tau_u$, where $\tau_u([t])=[u+t]$. For a scaled map, the quotient dilation $D_\alpha([t]_H)=[\alpha t]_{\alpha H}$ satisfies $D_\alpha(z\cdot u)=D_\alpha(z)\cdot(\alpha u)$, not strict equivariance unless $\alpha=1$. This proxy is neither the actual orbit topology nor a Hausdorff, Kolmogorov, or completely regular reflection of it.

We now specialize only the period statement. Deninger's right-flow normalization gives multiplicative isotropy $p^{\mathbb Z}$ and logarithmic additive time, hence $(\log p)\mathbb Z$ at every point of the fixed-prime packet [@Deninger2026Dynamical arXiv v4, physical pp. 38--39, Theorem 6.1]. On the companion's actual owner, the entire packet has one global indiscrete topology [@Wang2026PacketSeparation]. Forming the range-first groupoid and applying [\[prop:period\]](#prop:period){reference-type="ref" reference="prop:period"} yields the following conditional same-owner consequence.

[\[cor:packet-period\]]{#cor:packet-period label="cor:packet-period"} For a rational prime $p$, at every unit $x$ of the actual fixed-prime packet, $$\label{eq:packet-period}
 \operatorname{Per}_x([c])=(\log p)\mathbb Z.$$ This is a packet-level assertion: `ORBIT_ONLY=false`.

Deninger owns the packet, the right action, every-unit $p^{\mathbb Z}$, and the logarithmic clock. The companion owns the globally indiscrete actual topology. The present paper owns the author complex and the marked cohomological recovery. No step replaces the packet by a full suspension, selects primes from the generic theorem, compares different primes, or transfers a topology from Deninger's set parametrizations. The same period formula also admits composite, nonarithmetic, dense, trivial, and free stabilizer controls; that breadth is a ceiling on arithmetic specificity.

# Section-free orbitwise standardization {#sec:standardization}

Fix $H=L\mathbb Z$ with $L>0$ and suppose now that every unit has stabilizer $H$. Let $Q=X/\mathbb R$ denote only the nonempty set of orbits. For an orbit $O$ and any $x\in O$, evaluation defines $$\label{eq:quotient-chart}
 q_x:\mathbb R\longrightarrow O,\qquad q_x(t)=x\mathbin{\cdot}t.$$ Give $O$ the quotient topology for $q_x$. If $x'=x\mathbin{\cdot}u$, then $q_{x'}=q_x\circ T_u$, where $T_u(t)=u+t$ is a homeomorphism. The topology is therefore independent of the selected $x$. The induced bijection $$\label{eq:standard-orbit-chart}
 \bar q_x:\mathbb R/H\xrightarrow{\ \cong\ }O,\qquad
 [t]\longmapsto x\mathbin{\cdot}t$$ is an equivariant homeomorphism by the two quotient definitions.

For completeness, $\mathbb R/L\mathbb Z$ is compact Hausdorff. The formula $$\label{eq:quotient-metric}
 d_H([s],[t])=\inf_{k\in\mathbb Z}|s-t-kL|$$ is a metric inducing the quotient topology, while the quotient image of $[0,L]$ covers the space and proves compactness. This direct observation is the only compactness input in the uniqueness argument. The standard quotient background agrees with the ordinary homogeneous-space description [@EoMTopologicalGroup; @EoMHomogeneousSpace].

[\[def:std\]]{#def:std label="def:std"} On the same carrier $X$, define $$\label{eq:std-open}
 U\text{ open in }\operatorname{Std}_{\mathrm{coprod}}(X)
 \quad\Longleftrightarrow\quad
 U\cap O\text{ is open in }O\text{ for every orbit }O.$$ Thus $\operatorname{Std}_{\mathrm{coprod}}(X)$ is the topological coproduct of the standard orbit spaces. No orbit origin and no prior topology on $Q$ enters the definition.

The componentwise universal property in Stacks Project Tag 0B1W supplies the routine coproduct background [@Stacks0B1W]. The action-dependent same-carrier construction and its characterization are the content here.

[\[thm:std-topology\]]{#thm:std-topology label="thm:std-topology"} The space $\operatorname{Std}_{\mathrm{coprod}}(X)$ is Hausdorff, every orbit is open and closed, and the right $\mathbb R$-action is jointly continuous. It is the unique topology on the same $\mathbb R$-set with these three properties.

Each orbit is an open coproduct summand and its complement is the union of the other summands. Points in one orbit are separated through [\[eq:standard-orbit-chart\]](#eq:standard-orbit-chart){reference-type="ref" reference="eq:standard-orbit-chart"}; points in different orbits are separated by their disjoint summands. On an orbit, the action becomes $([u],t)\mapsto[u+t]$ on $(\mathbb R/H)\times\mathbb R$, which is continuous. The open sets $O\times\mathbb R$ cover $\operatorname{Std}_{\mathrm{coprod}}(X)\times\mathbb R$, so the action is jointly continuous globally.

Conversely, let $\tau$ be Hausdorff, make all orbits open, and make the action jointly continuous. For $x\in O$, evaluation $q_x$ is continuous and constant exactly on $H$-cosets. It induces a continuous bijection $\mathbb R/H\to(O,\tau|_O)$. Its domain is compact and its codomain Hausdorff, so it is a homeomorphism. Thus $\tau$ has the standard topology on every orbit. Because the orbits are $\tau$-open, a subset is $\tau$-open exactly when all of its orbit intersections are open. This is [\[eq:std-open\]](#eq:std-open){reference-type="ref" reference="eq:std-open"}.

The compact-to-Hausdorff step uses the cocompact lattice $L\mathbb Z$; no analogous uniqueness theorem is asserted here for $H=0$ or a noncocompact quotient. The identity $$\label{eq:identity-direction}
 \operatorname{id}_X:\operatorname{Std}_{\mathrm{coprod}}(X)\longrightarrow X_{\mathrm{indisc}}$$ is continuous because the target has only two opens. The reverse identity is not: $\operatorname{Std}_{\mathrm{coprod}}(X)$ is nontrivial Hausdorff, while a continuous map from a nontrivial indiscrete space to a $T_0$ space is constant. This is an action-and-mark-dependent retopologization. A separated reflection of the actual nonempty indiscrete space instead collapses it to one point [@Wang2026SeparatedReflections].

Let $\mathcal C_{\mathrm{common}}(H)$ have as objects the actual marked groupoids above with common stabilizer $H$, and strict marked isomorphisms as arrows. Let $\mathcal T_{\mathbb R}^{\mathrm{coprod}}(H)$ have as objects nonempty topological coproducts of standard right $\mathbb R/H$ torsors, and strictly equivariant homeomorphisms as arrows.

[\[thm:equivalence\]]{#thm:equivalence label="thm:equivalence"} The functor $$\label{eq:std-functor}
 \operatorname{Std}_{\mathrm{coprod}}:\mathcal C_{\mathrm{common}}(H)
 \longrightarrow\mathcal T_{\mathbb R}^{\mathrm{coprod}}(H)$$ is full and faithful. Replacing the whole target carrier topology by one global indiscrete topology defines a strict inverse $\operatorname{Indisc}$. Under the same-set convention, both composites are identities. The disjoint union of these categories over $L>0$ has the same property.

By [\[eq:strict-normal-form\]](#eq:strict-normal-form){reference-type="ref" reference="eq:strict-normal-form"}, a strict arrow is an equivariant orbit bijection. On an orbit it satisfies $F_0\circ q_x=q_{F_0(x)}$, so the quotient charts make its restriction a homeomorphism. Since it permutes open summands, it is a global homeomorphism. This defines $\operatorname{Std}_{\mathrm{coprod}}$ on arrows. Faithfulness follows because the unit map determines a strict arrow; fullness follows because any equivariant target homeomorphism has the unique lift $(x,t)\mapsto(\phi(x),t)$.

For a target object, $\operatorname{Indisc}$ retains its set and action, replaces the entire unit topology by one global indiscrete topology, and forms the marked range-first groupoid. The action into the indiscrete target is continuous, and every target arrow lifts strictly. Standardizing it restores each given standard orbit and then the given coproduct topology. Indiscretizing an actual object after standardization restores its original global indiscrete topology, action, mark, and arrow maps.

The inverse is *global* indiscretization. A coproduct of separately indiscrete components would generally not be an object of the actual category. Proposition 2.15 of @GepnerMeier2023 is a useful over-$B\mathbb R$ analogy for why strict equivariance determines the lift, but its weak-Hausdorff ambient category excludes the nontrivial actual owner; the direct proof above is therefore essential.

# Automorphisms of the standardized owner {#sec:automorphisms}

Put $A=\operatorname{Aut}_{\mathbb R}(\operatorname{Std}_{\mathrm{coprod}}(X))$. Every element permutes the open action orbits, so there is a canonical homomorphism $$\label{eq:orbit-permutation}
 \pi:A\longrightarrow\operatorname{Sym}(Q),\qquad
 \pi(\phi)(q)=\phi(O_q).$$

[\[thm:automorphism-extension\]]{#thm:automorphism-extension label="thm:automorphism-extension"} In ZFC there is a canonical exact sequence of abstract groups $$\label{eq:automorphism-extension}
 1\longrightarrow(\mathbb R/H)^Q\xrightarrow{\ i\ }
 \operatorname{Aut}_{\mathbb R}(\operatorname{Std}_{\mathrm{coprod}}(X))\xrightarrow{\ \pi\ }\operatorname{Sym}(Q)
 \longrightarrow1,$$ where, for $a:Q\to\mathbb R/H$, $$\label{eq:kernel-rotation}
 i(a)(x)=x\mathbin{\cdot}a(q),\qquad x\in O_q.$$ The injection and kernel identification are section-free. Surjectivity uses choice, and a choice of one origin in every orbit gives a noncanonical split.

The formula in [\[eq:kernel-rotation\]](#eq:kernel-rotation){reference-type="ref" reference="eq:kernel-rotation"} is independent of the representative of $a(q)$, equivariant, and a homeomorphism on every open orbit. It is an injective homomorphism because a rotation is the identity precisely when its class in $\mathbb R/H$ is zero.

If $\phi\in\ker\pi$, then on $O_q$ there is a unique displacement $a(q)\in\mathbb R/H$ with $\phi(x)=x\cdot a(q)$. If $y=x\cdot u$, equivariance gives $\phi(y)=\phi(x)\cdot u=y\cdot a(q)$, so the displacement is independent of $x$. This proves $\ker\pi=\operatorname{im}i$ without selecting origins.

For $\sigma\in\operatorname{Sym}(Q)$, use ZFC choice to select $x_q\in O_q$ for every $q$. The common stabilizer makes $$\label{eq:choice-lift}
 s_\sigma(x_q\mathbin{\cdot}t)=x_{\sigma(q)}\mathbin{\cdot}t$$ well defined. It is an equivariant homeomorphism between coproduct summands, and $\pi(s_\sigma)=\sigma$. With the origins fixed once, the formulas satisfy $s_\sigma s_\tau=s_{\sigma\tau}$ and give a split. Its semidirect coordinates obey $(\sigma\cdot a)(q)=a(\sigma^{-1}q)$. Changing the origins changes the split, but not $i$, $\pi$, or the kernel identification.

The product in [\[eq:automorphism-extension\]](#eq:automorphism-extension){reference-type="ref" reference="eq:automorphism-extension"} is the full Cartesian product, not a direct sum. No topology or continuous splitting is asserted. The finite-copy wreath results of @GuillouMay2017 [Proposition 5.19, printed p. 3311] and @AlpWensley2010 [Section 3.1, published p. 481] motivate the algebraic shape but do not prove the arbitrary-$Q$ topological statement or its choice accounting.

# Standardized degree-one cohomology {#sec:standard-h1}

Let $G_{\mathrm{std}}=\operatorname{Std}_{\mathrm{coprod}}(X)\rtimes\mathbb R$ and use the same complex as in [\[def:complex\]](#def:complex){reference-type="ref" reference="def:complex"}, now on the standardized topology. A continuous one-cochain $b:X\times\mathbb R\to\mathbb R$ is a cocycle precisely when $$\label{eq:std-cocycle}
 b(x,t+u)=b(x,t)+b(x\mathbin{\cdot}t,u).$$ The new unit topology permits independent behavior on different open orbits, and it also permits nonconstant unit cochains. Thus the actual factorization theorem cannot simply be copied to this owner.

For a class $[b]$ and an orbit $q\in Q$, choose any $x\in O_q$ and put $$\label{eq:slope-map}
 \rho([b])(q)=\frac{b(x,L)}{L}.$$

[\[lem:slope\]]{#lem:slope label="lem:slope"} The value in [\[eq:slope-map\]](#eq:slope-map){reference-type="ref" reference="eq:slope-map"} is independent of $x$ and of the cocycle representative. It defines a linear map $\rho:H_{\mathrm{cnv}}^1(G_{\mathrm{std}};\mathbb R)\to\mathbb R^Q$.

If $x'=x\cdot u$, apply [\[eq:std-cocycle\]](#eq:std-cocycle){reference-type="ref" reference="eq:std-cocycle"} to $u+L$ in both orders. Because $x\cdot L=x$, one obtains $$\begin{aligned}
 b(x,u+L)&=b(x,u)+b(x\cdot u,L),\\
 b(x,L+u)&=b(x,L)+b(x,u).\end{aligned}$$ Their left sides agree, so $b(x\cdot u,L)=b(x,L)$. Every point of $O_q$ has this form. If $b'=b+d^0h$, then $(d^0h)(x,L)=h(x\cdot L)-h(x)=0$. Thus the slope is also unchanged by a coboundary. The positive generator $L$ is unique for $H=L\mathbb Z$.

For every function $\lambda:Q\to\mathbb R$, define $$\label{eq:orbitwise-representative}
 b_\lambda(x,t)=\lambda([x])t.$$ On each open $O_q\times\mathbb R$, this is the continuous function $(x,t)\mapsto\lambda(q)t$, and the components cover the arrow space. The action preserves $[x]$, so [\[eq:std-cocycle\]](#eq:std-cocycle){reference-type="ref" reference="eq:std-cocycle"} holds and $\rho([b_\lambda])=\lambda$. No boundedness, finite support, or other condition is required. This is why the answer is all of $\mathbb R^Q$.

For injectivity, suppose a cocycle $b_0$ has zero slope on every orbit. Use ZFC choice to select $x_q\in O_q$ and define $$\label{eq:potential}
 h(x_q\mathbin{\cdot}t)=b_0(x_q,t).$$ The zero slope and the isotropy homomorphism property give $b_0(y,kL)=0$ for all units $y$ and $k\in\mathbb Z$. Hence [\[eq:potential\]](#eq:potential){reference-type="ref" reference="eq:potential"} is independent of the representing time. Its pullback along $q_{x_q}$ is the continuous function $t\mapsto b_0(x_q,t)$ and is constant on $H$-cosets, so it descends continuously to $O_q$. The open components glue these functions to a continuous $h:X\to\mathbb R$. Finally, for $y=x_q\cdot t$, the cocycle equation gives $$\label{eq:potential-coboundary}
 (d^0h)(y,u)
 =b_0(x_q,t+u)-b_0(x_q,t)=b_0(y,u).$$ Thus every zero-slope cocycle is a coboundary. The origin choice is only an existence device for a potential; it is not part of $\rho$ or of the canonical inverse $\lambda\mapsto[b_\lambda]$.

[\[thm:standard-h1\]]{#thm:standard-h1 label="thm:standard-h1"} The slope map is a canonical algebraic isomorphism $$\label{eq:standard-h1}
 \rho:H_{\mathrm{cnv}}^1(G_{\mathrm{std}};\mathbb R)\xrightarrow{\ \cong\ }\mathbb R^Q.$$

The representatives in [\[eq:orbitwise-representative\]](#eq:orbitwise-representative){reference-type="ref" reference="eq:orbitwise-representative"} prove surjectivity. The potential calculation proves that the kernel is zero. Equivalently, for an arbitrary cocycle $b$, the difference $b-b_{\rho([b])}$ has zero slope and is a coboundary.

Standardized coboundaries are generally nonzero. Choose an origin $x_0$ on one orbit and set $$\label{eq:nonzero-boundary}
 h(x_0\mathbin{\cdot}t)=\sin(2\pi t/L)
 \quad\text{on that orbit},\qquad h=0\quad\text{elsewhere}.$$ This is a continuous unit cochain, and $(d^0h)(x_0,L/4)=1$. The nonzero cocycle $d^0h$ has zero slopes, so it is not literally any $b_\lambda$ except at the level of its zero cohomology class. Consequently $$\label{eq:boundaries-warning}
 B_{\mathrm{cnv}}^1(G_{\mathrm{std}};\mathbb R)\neq0,
 \qquad
 Z_{\mathrm{cnv}}^1(G_{\mathrm{std}};\mathbb R)
 \neq\{b_\lambda:\lambda\in\mathbb R^Q\}$$ in general. The theorem classifies classes, not all cocycles.

Mackenzie's Theorem 3 concerns a different rigid cohomology under locally trivial, locally compact, Hausdorff/transitive and module hypotheses [@Mackenzie1978 printed pp. 298--299]. The one-object real comparators in @BlancoUribeWaldorf2023 [@FuchssteinerWockel2012] and the degree-one terminology in @FarsiHuangKumjianPacker2022 likewise do not prove the arbitrary coproduct result [\[eq:standard-h1\]](#eq:standard-h1){reference-type="ref" reference="eq:standard-h1"}. The latter is a direct statement about the author complex and only in degree one.

# The comparison functor and invariant diagonal {#sec:comparison}

On the same carrier and arrow set, the identity defines $$\label{eq:J}
 J:G_{\mathrm{std}}\longrightarrow G_{\mathrm{actual}}.$$ It is continuous: the unit identity is finer-to-indiscrete, and the inverse image of an actual arrow open $X\times U$ is the same standard arrow open. It preserves every algebraic operation and $c(x,t)=t$. The reverse identity is not continuous already on units. Pullback of nerve cochains commutes with the faces and has the contravariant direction $$\label{eq:Jstar}
 J^*:H_{\mathrm{cnv}}^1(G_{\mathrm{actual}};\mathbb R)
 \longrightarrow H_{\mathrm{cnv}}^1(G_{\mathrm{std}};\mathbb R).$$

By [\[thm:actual-h1\]](#thm:actual-h1){reference-type="ref" reference="thm:actual-h1"}, an actual class has representative $\lambda c$. Its pullback is the same formula on every standard orbit, and hence $$\label{eq:constant-diagonal}
 \rho\bigl(J^*(\lambda[c])\bigr)(q)=\lambda.$$ Because $Q$ is nonempty, the diagonal map is injective. Its image is the constant functions.

Let $\phi\in\operatorname{Aut}_{\mathbb R}(G_{\mathrm{std}})$ and let $\sigma_\phi=\pi(\phi)\in\operatorname{Sym}(Q)$. Raw cohomological pullback obeys $$\label{eq:raw-pullback}
 \rho(\phi^*[b])(q)=\rho([b])(\sigma_\phi(q)).$$ Indeed the strict arrow formula is $(x,t)\mapsto(\phi(x),t)$, so evaluation at $(x,L)$ becomes evaluation at $(\phi(x),L)$. If instead we declare a left action by $$\label{eq:left-action}
 \phi\mathbin{\cdot}[b]=(\phi^{-1})^*[b],$$ then the corresponding slope action is $$\label{eq:left-slope}
 (\phi\mathbin{\cdot}\lambda)(q)
 =\lambda(\sigma_\phi^{-1}(q)).$$ The inverse appears only after passing from raw pullback to this declared left action. must not be interchanged.

[\[thm:invariant-diagonal\]]{#thm:invariant-diagonal label="thm:invariant-diagonal"} For the left action in [\[eq:left-action\]](#eq:left-action){reference-type="ref" reference="eq:left-action"}, $$\label{eq:invariants}
 (\mathbb R^Q)^{\operatorname{Aut}_{\mathbb R}(G_{\mathrm{std}})}
 =\{\text{constant functions }Q\to\mathbb R\},
 \qquad
 \operatorname{im}(J^*)=(\mathbb R^Q)^{\operatorname{Aut}_{\mathbb R}(G_{\mathrm{std}})}.$$

Kernel rotations in [\[eq:automorphism-extension\]](#eq:automorphism-extension){reference-type="ref" reference="eq:automorphism-extension"} induce the identity permutation and act trivially on slopes. Surjectivity of $\pi$ says every permutation of $Q$ occurs. If a function is invariant and $q\neq r$, the transposition of $q$ and $r$ forces its two values to agree; the singleton case is immediate. Conversely every constant function is permutation invariant. identifies this space with the image of $J^*$.

Only strict time-preserving equivariant automorphisms enter this theorem. Positive scaled, unmarked, orientation-reversing, and arbitrary abstract groupoid automorphisms are outside its domain. No topology is present on $\operatorname{Aut}_{\mathbb R}(G_{\mathrm{std}})$ or $\mathbb R^Q$, and no fixed-point theorem from topological representation theory is being invoked.

In prose, the upper row of [\[fig:same-carrier-diagonal\]](#fig:same-carrier-diagonal){reference-type="ref" reference="fig:same-carrier-diagonal"} says that the identity $J$ is continuous from the finer orbitwise standard topology to the actual indiscrete topology, while the reverse identity is not continuous. The lower row reverses direction because cohomology is contravariant: $J^*$ sends the single actual slope to the same slope on every orbit. The image is exactly the constant diagonal fixed by strict automorphisms. The display also records two nontransfer statements: actual coboundaries vanish, standardized coboundaries generally do not, and the product $\mathbb R^Q$ is purely algebraic.

## Fixed-prime four-way application {#sec:four-way}

Fix a rational prime $p$. The source and actual-topology premises already used in [\[cor:packet-period\]](#cor:packet-period){reference-type="ref" reference="cor:packet-period"} put the whole packet in the common-lattice category with $H=(\log p)\mathbb Z$. The packet need not be transitive; indeed the standardization is designed for an arbitrary nonempty bare orbit set.

[\[cor:packet-comparison\]]{#cor:packet-comparison label="cor:packet-comparison"} Let $Q_p$ denote only the underlying set of fixed-prime packet orbits. Put the standard $\mathbb R/(\log p)\mathbb Z$ topology on every orbit of the same packet set and take their coproduct. Then $$\begin{gathered}
\label{eq:packet-comparison}
 \Gamma_p^{\mathrm{std}}\rtimes\mathbb R
 \xrightarrow{\ J_p\ }
 \Gamma_p^{\mathrm{actual}}\rtimes\mathbb R,\\
 H_{\mathrm{cnv}}^1(\Gamma_p^{\mathrm{actual}}\rtimes\mathbb R;\mathbb R)=\mathbb R[c],
 \qquad
 H_{\mathrm{cnv}}^1(\Gamma_p^{\mathrm{std}}\rtimes\mathbb R;\mathbb R)=\mathbb R^{Q_p},\notag\\
 \rho_p(\operatorname{im}J_p^*)
 =\{\text{constant functions on }Q_p\}
 =(\mathbb R^{Q_p})^{\operatorname{Aut}_{\mathbb R}(\Gamma_p^{\mathrm{std}}\rtimes\mathbb R)},\notag\end{gathered}$$ and there is a canonical abstract-group extension $$\label{eq:packet-automorphisms}
 1\longrightarrow
 \bigl(\mathbb R/(\log p)\mathbb Z\bigr)^{Q_p}
 \longrightarrow\operatorname{Aut}_{\mathbb R}(\Gamma_p^{\mathrm{std}})
 \longrightarrow\operatorname{Sym}(Q_p)\longrightarrow1.$$ Surjectivity and a noncanonical split use ZFC choice exactly as in [\[thm:automorphism-extension\]](#thm:automorphism-extension){reference-type="ref" reference="thm:automorphism-extension"}.

Deninger's every-unit stabilizer and logarithmic clock supply the common lattice; the actual-topology premise supplies the globally indiscrete carrier. Substituting $H=(\log p)\mathbb Z$ into [\[thm:std-topology,thm:equivalence,thm:automorphism-extension,thm:standard-h1,thm:invariant-diagonal\]](#thm:std-topology,thm:equivalence,thm:automorphism-extension,thm:standard-h1,thm:invariant-diagonal){reference-type="ref" reference="thm:std-topology,thm:equivalence,thm:automorphism-extension,thm:standard-h1,thm:invariant-diagonal"} gives each statement.

The four records remain those of [\[tab:packet-types\]](#tab:packet-types){reference-type="ref" reference="tab:packet-types"}. The actual quotient $Q_p^{\mathrm{actual}}$ is indiscrete, whereas $Q_p^{\mathrm{disc}}$ is discrete because the inverse image of any subset is a union of open standardized components. Only their bare underlying set is shared. Nothing here provides its cardinality, enumeration, measure, local triviality, arithmetic weighting, or a topology inherited from the source. Nor does the theorem compare different primes or extend to an unregistered full suspension.

In prose, [\[fig:packet-four-way-firewall\]](#fig:packet-four-way-firewall){reference-type="ref" reference="fig:packet-four-way-firewall"} follows the source facts into the actual packet groupoid, then separates the actual quotient from the constructed component index. The downward arrow is the same-set topology construction, not inheritance and not reflection. At the categorical boundary, strict maps retain the mark exactly, positive scaled maps obey [\[eq:scaled-covariance\]](#eq:scaled-covariance){reference-type="ref" reference="eq:scaled-covariance"}, and unmarked isomorphisms can relate unequal periods. None of these statements enriches the bare orbit set arithmetically.

# Deterministic controls, Route boundary, and limitations {#sec:controls-route}

## Control receipt

The frozen deterministic package passed 122/122 tests and produced 11 CSV files with 3,486 rows. It detected 14/14 intentional negatives. The large orbitwise-standardization ledger has 3,252 rows: 3,151 of them enumerate all automorphisms of the selected finite cyclic models, while the other blocks check topology, basepoint independence, coboundary/potential reconstruction, the diagonal, invariants, and two v4 negative directions. The other ledgers check finite nerve identities, the $T_0$ boundary, continuous-additive profiles, period formulas, category directions, packet-wide equality, labels, and one-sided quotient topology.

P38mmP19mmY Frozen control group & Rows & Exact manuscript role\
Orbitwise standardization $H^1$ & 3,252 & Finite topology, automorphism, potential, diagonal, invariant, and wrong-direction witnesses.\
Actual degree one and nerve/factorization & 143 & Finite face, $d^2$, $T_0$/non-$T_0$, Cauchy-profile, and boundary witnesses.\
Periods, packets, morphisms, labels, quotients & 70 & Exact finite examples of period, every-unit, strict/scaled/unmarked, selectivity, and topology stops.\
Target summary and explicit negatives & 21 & Nine target-level summaries and twelve legacy negative-ledger rows.\
Total & 3,486 & 122/122 tests; 14/14 intentional negatives.\

The generator and tests use the Python standard library only. There is no network call, external dataset, randomness, timestamp, fitting, hidden target, zeta-zero table, trace, determinant, earlier-paper coefficient, or analytic completion. Exact arithmetic is used except for the frozen $10^{-12}$ absolute tolerance on four displayed logarithm/square-root values. Checked-in, fresh-one, and fresh-two outputs were byte-identical in the independently reviewed top-level run. A duplicate-run orchestration incident was discarded and contributed neither accepted evidence nor residue; the top-level reproduction must not be run concurrently. These finite controls cannot prove the real or arbitrary-$Q$ theorems and do not replace source verification.

## Typed Route result

Eight owners were adjudicated separately. [\[tab:route\]](#tab:route){reference-type="ref" reference="tab:route"} reports the complete A0--A4 tuples but omits serialization fields and hashes, which remain in the reproducibility ledger. "Exploratory" is a scoped negative prior, not weak positive evidence for a determinant, explicit formula, or operator program.

P43mmP69mmY Owner & Exact A0--A4 tuple & Verdict\
`GEN-INDISC-R-ACTION-CNV` & $\begin{gathered}
  (\mathrm{A0\_FAIL},\mathrm{A1\_FAIL},\mathrm{A2\_FAIL},\\
  \mathrm{A3\_FAIL},\mathrm{A4\_FAIL})
  \end{gathered}$& Rejected\
`DEN-EF-ACTUAL-ORBIT-CNV-P-A` & $\begin{gathered}
  (\mathrm{A0\_ANALYTIC\_ARITHMETIC\_ORIGIN},\\
  \mathrm{A1\_WEAK},\mathrm{A2\_FAIL},\mathrm{A3\_FAIL},
  \mathrm{A4\_FAIL})
  \end{gathered}$& Exploratory\
`DEN-EF-ACTUAL-PACKET-CNV-P` & $\begin{gathered}
  (\mathrm{A0\_ANALYTIC\_ARITHMETIC\_ORIGIN},\\
  \mathrm{A1\_WEAK},\mathrm{A2\_FAIL},\mathrm{A3\_FAIL},
  \mathrm{A4\_FAIL})
  \end{gathered}$& Exploratory\
`DEN-EF-ACTUAL-ORBIT-MARKED-PERIOD-P-A` & $\begin{gathered}
  (\mathrm{A0\_ANALYTIC\_ARITHMETIC\_ORIGIN},\\
  \mathrm{A1\_WEAK},\mathrm{A2\_FAIL},\mathrm{A3\_FAIL},
  \mathrm{A4\_FAIL})
  \end{gathered}$& Exploratory\
`DEN-EF-ACTUAL-PACKET-MARKED-PERIOD-P` & $\begin{gathered}
  (\mathrm{A0\_ANALYTIC\_ARITHMETIC\_ORIGIN},\\
  \mathrm{A1\_WEAK},\mathrm{A2\_FAIL},\mathrm{A3\_FAIL},
  \mathrm{A4\_FAIL})
  \end{gathered}$& Exploratory\
`DEN-EF-STANDARD-PERIOD-QUOTIENT-P` & $\begin{gathered}
  (\mathrm{A0\_WEAK\_ARITHMETIC\_RELATION},\\
  \mathrm{A1\_WEAK},\mathrm{A2\_FAIL},\mathrm{A3\_FAIL},
  \mathrm{A4\_FAIL})
  \end{gathered}$& Exploratory\
`DEN-EF-STANDARDIZED-PACKET-H1-DIAGONAL-P` & $\begin{gathered}
  (\mathrm{A0\_WEAK\_ARITHMETIC\_RELATION},\\
  \mathrm{A1\_WEAK},\mathrm{A2\_FAIL},\mathrm{A3\_FAIL},
  \mathrm{A4\_FAIL})
  \end{gathered}$& Exploratory\
`UNMARKED-PERIOD-SCALING-CONTROL` & $\begin{gathered}
  (\mathrm{A0\_FAIL},\mathrm{A1\_WEAK},\mathrm{A2\_FAIL},\\
  \mathrm{A3\_FAIL},\mathrm{A4\_FAIL})
  \end{gathered}$& Rejected\

Each owner explicitly uses `NONE_BY_DESIGN_NO_DETERMINANT_OBJECT`. All nine required A2 metrics are negative or not applicable, every A3 and A4 coordinate fails, every adversarial verdict is `STOP_SCOPED`, and every Route-B flag is false. There are six Route-A exploratory records, two rejected records, zero positive A2--A4 coordinates, and no Route-B file. [Route B]{.smallcaps} remains closed. The generic and unmarked controls cannot donate evidence to the source owners, and the constructed standard proxy cannot inherit the actual topology or arithmetic selectivity.

## Limitations and prohibited inferences {#sec:limitations}

The topology uniqueness and equivalence require a common nonzero cocompact lattice $H=L\mathbb Z$. Mixed stabilizers are outside that category. The actual all-degree factorization accepts arbitrary $T_0$ coefficients, but the degree-one classification by slopes uses real coefficients and the direct continuous Cauchy argument. The standardized computation is degree one only. It does not calculate higher standardized cohomology.

The orbit set $Q$, and specifically $Q_p$, is bare. We impose no cardinality, enumeration, measure, local triviality, arithmetic weight, or actual quotient topology. The symbol $\mathbb R^Q$ means every algebraic function $Q\to\mathbb R$; it does not mean $C(Q,\mathbb R)$, a direct sum, bounded functions, or a topological product. The automorphism extension is an extension of abstract groups. Its kernel map is canonical, its surjectivity uses ZFC choice, and a split is noncanonical.

The invariant theorem is restricted to strict time-preserving equivariant automorphisms. It does not include positive scaled, unmarked, orientation-reversing, or arbitrary abstract automorphisms. The standard topology is constructed from the action and mark. It is not inherited from the actual packet and is not a separated reflection. The only continuous same-set direction is standard to actual.

The fixed-prime corollary recovers a source-normalized mark already present as the logarithm of Deninger's every-unit $p^{\mathbb Z}$. It does not select primes, compare primes, prove an orbit count, or extend to a full suspension. Neither the theorem nor its controls define a trace, dynamical determinant, analytic divisor, analytic continuation, quantization, completion, or natural operator lift. No such object may be inferred from the word "cohomology," and [Route B]{.smallcaps} supplies no rescue.

The bounded literature statement remains exactly `SUPPORTED_WITHIN_SEARCH through 2026-08-15`. We make no claim of being first, unprecedented, or globally without precedent.

The independently reviewed mathematical disposition is `STANDALONE_PASS`: the comparison in [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"} closes the earlier routine-reduction objection. This is a claim-level disposition, not a journal acceptance, citation, manuscript-quality, or public-release authorization. Public release remains conditional on the human and companion-identity requirements stated below.

# Conclusion and successor boundary {#sec:conclusion}

One carrier can support two sharply different continuous cohomology records. With the actual global indiscrete topology, every continuous real degree-one cocycle is one global time slope and every coboundary vanishes. With the section-free coproduct of standard common-period orbits, independent orbit slopes survive, producing the full algebraic product $\mathbb R^Q$, while nonzero coboundaries also appear. The continuous identity functor points from standard to actual, so pullback embeds the actual line as the constant diagonal. The canonical automorphism extension shows that this diagonal is exactly the strict invariant subspace.

For the fixed-prime packet, the same theorem recovers the source-normalized $(\log p)\mathbb Z$ mark at every unit and keeps the actual packet, standardized packet, actual quotient, and discrete component index separate. The result stops there. A later Paper 13 may ask whether an independently defined analytic object retains marked period information, but the present work assumes no twist, completion, trace, determinant, operator, or spectral construction for that successor.

# Declarations {#declarations .unnumbered}

#### Author metadata and contributions.

The provisional record is Liang Wang, Huazhong University of Science and Technology, <wangliang.f@gmail.com>. Final author list, academic unit, institution spelling, postal address if required, corresponding-author status, email, ORCID, and all CRediT roles: **AUTHOR TO CONFIRM**. Repository history is not used to infer sole authorship or contribution roles.

#### Funding.

**AUTHOR TO CONFIRM**. No absence of funding is inferred from the current project record.

#### Competing interests.

**AUTHOR TO CONFIRM**. No absence of conflicts is inferred from silence.

#### Acknowledgments.

**AUTHOR TO CONFIRM**.

#### Ethics.

This work consists of mathematical proof and deterministic controls. No human participant, animal, clinical intervention, personal, confidential, or sensitive data enters the control manifest. Venue-specific wording and the final not-applicable declaration: **AUTHOR TO CONFIRM**.

#### Data and code availability.

The local project contains the deterministic Python code, a manifest, and 11 generated CSV files. It uses no external experimental dataset. The controls are regression witnesses and falsifiers, not proofs. Public repository, immutable tag or archive, license, and DOI: **AUTHOR TO CONFIRM**.

#### AI assistance.

AI assistance was used for research-protocol structuring, bounded source discovery, exact-byte comparison, symbolic proof and deterministic-control drafting, adversarial review, Route-record checking, and composition planning. The human author verified the cited sources and remains responsible for every definition, theorem, computation, disclosure, and publication claim. The selected venue's current AI policy and final wording must be confirmed before submission.

#### Companion and release status.

The three companion records are unpublished and have no frozen immutable public URL. Before standalone public release, each load-bearing companion dependency must either be bound to an honest immutable public record for the audited version or be supplied self-containedly as an explicit premise or proof. Final venue, release date, public tag/archive, license, DOI, and release authorization are **AUTHOR TO CONFIRM**. Retained research source PDFs are internal verification material and are excluded from every public payload; the generated manuscript PDF is a project output, not a source PDF.
