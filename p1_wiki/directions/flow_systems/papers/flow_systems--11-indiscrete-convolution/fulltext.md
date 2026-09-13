---
p1_kind: "derived-fulltext-reading-copy"
route: "flow_systems"
logical_paper_id: "flow_systems--11-indiscrete-convolution"
canonical_tex: "flow_systems/papers/11-indiscrete-convolution/paper/manuscript.tex"
canonical_pdf: "flow_systems/papers/11-indiscrete-convolution/paper/paper.pdf"
source_sha256: "eb1aa4d7060cf1aa53a729e7c7be89a5724a6133ef3bf000cb800bf786de1002"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Continuous Convolution Collapse on Indiscrete Arithmetic Orbit Groupoids

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../flow_systems/papers/11-indiscrete-convolution>)
- [规范 TeX](<../../../../../flow_systems/papers/11-indiscrete-convolution/paper/manuscript.tex>)
- [关联 PDF](<../../../../../flow_systems/papers/11-indiscrete-convolution/paper/paper.pdf>)
- [支撑 Markdown](<../../../../../flow_systems/papers/11-indiscrete-convolution/README.md>)
- [BibTeX](<../../../../../flow_systems/papers/11-indiscrete-convolution/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For every rational prime $p$ and every normalized label $a$, consider the transformation groupoid of one rational-Witt fixed orbit equipped with its actual inherited-indiscrete unit topology. We prove that every continuous arrow map to a $T_0$ target factors uniquely through real time. Adding the open-cover quasi-compact support condition gives a canonical $*$-isomorphism between the author-defined global algebra $C_{\mathrm{qc}}^{\mathrm{glob}}(G_{p,a}^{\mathrm{act}})$ and ordinary $C_c(\mathbb R)$. Direct range-fibre convolution and source-fibre calculations identify the author-defined unit-regular family with the left regular representation of $\mathbb R$; the unit-regular reduced completion and the separately transported full completion consequently reduce to group-$\mathbb R$ records. The result is convention-sensitive. The raw span of zero-extensions from Hausdorff arrow opens is zero and is diagnostic only, while the retained standard actual-groupoid frameworks are inapplicable because their audited hypotheses fail. The ordinary-circle proxy is strictly finer: the actual-to-standard set-groupoid map $J$ is not continuous, $J^{-1}$ is continuous, and the contravariant test-function map has the proper image $A_{\mathrm{const}}$ of functions constant in the unit coordinate. No completion extension is proved. A generic theorem and adversarial controls show that the algebra, unit-regular norm, and transported completions are unchanged by trivial, transitive, nontransitive, label, or period variations; thus the action, $p$, $a$, $\log p$, orbit decomposition, and stabilizer do not survive in the analytic output. The deterministic package passes 57/57 tests, produces 12 CSVs with 642 rows, and detects 5/5 intentional negatives; these controls are witnesses, not proofs. Three typed Route-A records are exploratory negative priors, four are rejected, and Route B is false. As of 2026-08-15, the documented bounded Phase-2 search located no precedent for the exact rational-Witt actual-orbit convention-split package; no absolute priority claim is made.

  **Keywords:** rational-Witt flow; indiscrete topology; non-Hausdorff groupoid; quasi-compact support; convolution; action blindness; standard-circle proxy
author:
- |
  Liang Wang\
  School of Artificial Intelligence and Automation\
  Huazhong University of Science and Technology\
  <wangliang.f@gmail.com>
bibliography:
- references.bib
date: 15 August 2026
title: |
  **Continuous Convolution Collapse on\
  Indiscrete Arithmetic Orbit Groupoids**
```

## Markdown 正文

**中文摘要**

对每个有理素数 $p$ 与每个规范化轨道标签 $a$，本文考察一个采用实际继承不可分拓扑的有理 Witt 固定轨道变换群胚。取值于 $T_0$ 空间的连续箭头函数唯一地经实时间坐标分解；加入开覆盖意义下的拟紧支撑条件后，作者定义的 $C_{\mathrm{qc}}^{\mathrm{glob}}$ 与 $C_c(\mathbb R)$ 典范 $*$-同构。对值域纤维卷积和源纤维算子的直接计算表明，作者定义的单位正则族以及分别定义后再输运的完备化均退化为群 $\mathbb R$ 的相应对象。该结论严格依赖函数约定：原始 HOpen 生成空间为零且仅是诊断量，保留审计的标准框架因假设不成立而不适用于实际对象。普通圆周代理严格更细；$J$ 不连续而 $J^{-1}$ 连续，$I$ 仅在测试函数层面有真子代数像 $A_{\mathrm{const}}$，并未证明任何完备化延拓。一般作用盲定理与对抗控制进一步说明，作用、$p,a,L_p=\log p$、轨道分解和稳定子均不保留在解析输出中。确定性程序通过 57/57 项测试，生成 12 个 CSV、共 642 行，并检出 5/5 个故意负控；这些控制仅作见证而非普遍定理的证明。七个类型化 Route A 记录中，三个是探索性负先验、四个被拒绝，Route B 为假。限定检索未发现覆盖这一精确组合的先例，但本文不作绝对优先权声明。

**中文关键词：** 有理 Witt 流；不可分拓扑；非 Hausdorff 群胚；拟紧支撑；卷积；作用盲性；标准圆周代理

# Introduction {#sec:introduction}

Deninger's arithmetic dynamical construction places fixed-prime data in a positive-real suspension flow. Its fixed-prime set, right $+t$ action, $p^{\mathbb Z}$ multiplicative isotropy, and logarithmic period are source-owned inputs [@Deninger2026 arXiv v4, physical pp. 32--33, Eqs. (35), (38)--(39); physical pp. 38--39, Section 6 and Theorem 6.1]. A companion result determines the topology that these orbits actually inherit: every registered fixed-prime orbit is nonempty, nontrivial, and indiscrete [@Wang2026Packets Corollary 5.3, p. 11]. The present paper asks what happens if one forms the transformation groupoid of that actual orbit without silently replacing its topology by the ordinary circle topology suggested by a set-level periodic coordinate.

This question has no convention-free answer. On a locally Hausdorff groupoid, compactly supported test functions are commonly assembled from Hausdorff patches. Several standard sources make that construction inside precise ambient hypotheses [@Tu2004 physical pp. 3, 17, and 19; printed pp. 567, 581, and 583]; they do not license the same terminology on an arbitrary non-Hausdorff owner. Muhly and Williams likewise distinguish a raw Hausdorff-patch span from globally continuous ambient functions, but do so under Hausdorff-unit and compact-Hausdorff-neighborhood assumptions [@MuhlyWilliams2008 pp. 3--7 and Proposition 4.4, pp. 21--23]. Exel's non-Hausdorff-arrow setting retains a locally compact Hausdorff unit space and an etale boundary [@Exel2011 arXiv v3, physical/printed p. 1, Section 1]. The universal-property framework of Buss, Holkar, and Meyer is explicitly Hausdorff [@BussHolkarMeyer2018 arXiv v2, physical pp. 1--2]. The actual rational-Witt orbit groupoid considered here meets none of those retained actual-owner domains.

We therefore keep three function records separate. The first is an author-defined space $C_{\mathrm{qc}}^{\mathrm{glob}}$ of globally continuous complex functions whose ambient supports are quasi-compact in the open-cover sense. The second is a raw diagnostic $C_c^{\mathrm{HOp}}$, the span of zero-extensions from Hausdorff arrow opens. The third is the usual test-function algebra of an ordinary-circle Hausdorff proxy. On the actual topology, the first record is nonzero and canonically $C_c(\mathbb R)$; the second is zero. These are not competing names for one standard algebra. They are different typed constructions, and the zero record carries no convolution, norm, or completion status.

The positive result is direct rather than framework-derived. Every complex- valued continuous arrow function depends only on the real-time coordinate. The support condition becomes ordinary compact support in time, and the range-first convolution formula becomes group convolution on $\mathbb R$. We verify continuity, support, associativity, involution, and the fibre integrals explicitly. We then parametrize the exact source fibres before extending the dense-domain integral to $L^2$. Every author-defined unit operator is unitarily left convolution on $L^2(\mathbb R)$. This yields the reduced norm directly. A separate full norm is defined by transport from the group $C^*(\mathbb R)$. Only after these owner-specific calculations do we use ordinary group harmonic analysis to identify both author completions with the group model $C_0(\mathbb R)$ [@Williams2007 author manuscript v3.1, physical/printed p. 38/26, Example 1.80; p. 94/82, Proposition 3.1; pp. 210--211/198--199, Examples 7.9 and 7.11 and Theorem 7.13].

The standard circle remains useful as a calibration object. A chosen orbit chart defines a set-groupoid isomorphism $J$ from the actual groupoid to the ordinary-circle proxy. Its topology direction is one-sided: $J$ is not continuous, while $J^{-1}$ is. Pullback in the continuous direction gives an injective test-function $*$-map into the proxy, but its image consists exactly of functions constant in the unit coordinate and is proper. No boundedness theorem is available for a proxy norm, so the comparison stops at test functions. Proxy full crossed-product, Morita, stable, and tensor results remain proxy-only and retain their distinct theorem strengths [@Green1978 Proposition 3, physical p. 13 / printed p. 203] [@MuhlyRenaultWilliams1987 Theorem 2.8, physical p. 8 / printed p. 10] [@BrownGreenRieffel1977 Theorem 1.2, physical p. 4 / printed p. 351] [@BussHolkarMeyer2018; @Williams2007].

The strongest negative conclusion is more general than the arithmetic application. For every nonempty indiscrete space and every right $\mathbb R$-action, the global algebra, fibre formulas, unit-regular family, and transported completions collapse to the same group-$\mathbb R$ records. Trivial, nontransitive, and arbitrary-period actions all pass the same theorem. The rational-Witt conclusion must therefore be stated afterward as an application. The host still possesses its action and stabilizer, but the analytic output does not remember them. The theorem succeeds on too many arithmetically irrelevant systems to acquire periodic-orbit credit merely from its host.

The contributions are consequently exact but deliberately bounded:

1.  a complete classification of the actual arrow topology, its quasi-compact subsets, and continuous and measurable separated-target observables;

2.  the direct global-QC convolution $*$-algebra and unit-regular calculation, with separately defined transported completions;

3.  the distinct raw Hausdorff-open zero diagnostic and an audited framework non-applicability result;

4.  a one-sided actual/proxy topology theorem and a strict test-function monomorphism with no completion extension;

5.  a generic action-blind theorem, finite adversarial witnesses, and a seven-owner negative Route ledger.

We construct no standard actual-groupoid $C^*$-algebra, determinant, quantization, Hilbert--Polya operator, prime coproduct, full suspension, or Route-B object.

*Prose equivalent for [\[fig:convention-split\]](#fig:convention-split){reference-type="ref" reference="fig:convention-split"}.* Starting from the actual product $X_{p,a}\times\mathbb R$, one branch selects globally continuous functions with quasi-compact ambient support and yields $C_{\mathrm{qc}}^{\mathrm{glob}}\cong C_c(\mathbb R)$. The other branch selects raw extensions from Hausdorff arrow opens and yields zero. Standard frameworks are not applied because their stated actual-owner hypotheses fail.

# Source input, actual owner, and convention dictionary {#sec:owners}

Fix a rational prime $p$ and a normalized companion-paper orbit label $a$. Write $L_p=\log p$ and let $X_{p,a}$ be the corresponding inherited orbit. Deninger's source owns the underlying right action and its stabilizer $L_p\mathbb Z$; the companion theorem owns the actual nontrivial indiscrete topology. Paper 11 forms the transformation groupoid and owns the analytic definitions below. No ordinary-circle topology is imported into $X_{p,a}$.

It is useful to begin in a generic domain. Let $X$ be a nonempty indiscrete space and let $$\alpha:X\times\mathbb R\longrightarrow X,\qquad (x,t)\longmapsto x\cdot t,$$ be any right action of the additive group $\mathbb R$. It is jointly continuous because the codomain is indiscrete. Set $G(X,\alpha)=X\times\mathbb R$ with the product topology and the range-first operations $$\begin{aligned}
 r(x,t)&=x, & s(x,t)&=x\cdot t,\label{eq:range-source}\\
 (x,t)(x\cdot t,u)&=(x,t+u), & (x,t)^{-1}&=(x\cdot t,-t).
 \label{eq:groupoid-operations}\end{aligned}$$ No transitivity, freeness, period, or stabilizer is assumed in the generic theorems. The arithmetic specialization is $X=X_{p,a}$ and $G(X,\alpha)=G_{p,a}^{\mathrm{act}}$.

Throughout, *quasi-compact* means that every open cover has a finite subcover. It does not imply Hausdorffness. For a function on $G$, support means the closure of its nonzero set in the ambient product topology.

The author global-QC space is $$C_{\mathrm{qc}}^{\mathrm{glob}}(G)=\{f:G\to\mathbb C:f\text{ is continuous and }\operatorname{supp}_G(f)
 \text{ is quasi-compact}\}.$$ When $X$ is nontrivial, the raw HOpen record is $$C_c^{\mathrm{HOp}}(G)=\operatorname{span}\{\widetilde h:
 U\subseteq G\text{ open Hausdorff},\ h\in C_c(U)\},$$ where $\widetilde h$ is the raw zero-extension. This record is a diagnostic only. Finally, $C_c(G_p^{\mathrm{std}})$ denotes the ordinary compactly supported continuous functions on the standard Hausdorff proxy defined below.

For each $x\in X$, let $G^x=r^{-1}(x)$ and $$\rho_x:\mathbb R\to G^x,\qquad \rho_x(t)=(x,t),\qquad
 \lambda^x=(\rho_x)_*dt.$$ The name *GLOB-FIBRE-FAMILY* refers only to this author-defined family and the properties proved in [4](#sec:convolution){reference-type="ref" reference="sec:convolution"}. Let $\lambda_x=(\operatorname{inv})_*\lambda^x$ on $G_x=s^{-1}(x)$ and define the author source-fibre operator $\operatorname{Ind}_x$ by the dense-domain formula in [5](#sec:regular){reference-type="ref" reference="sec:regular"}. The completion $C_{\mathrm{glob}}^{\mathrm{full}}(G)$ is defined through the norm transported from $C^*(\mathbb R)$ after the dense $*$-isomorphism is proved. $C_{\mathrm{glob}}^{\mathrm{red}}(G)$ is defined through $\sup_x\|\operatorname{Ind}_x(\cdot)\|$. These are not denoted $C^*(G)$ or $C_r^*(G)$.

For the standard proxy, choose a set-level orbit chart $$\theta:S_p^{\mathrm{std}}=\mathbb R/L_p\mathbb Z\longrightarrow X_{p,a},
 \qquad \theta([r])=x^0\cdot r,$$ with inverse $\beta$. The circle $S_p^{\mathrm{std}}$ carries its ordinary compact Hausdorff topology. Put $G_p^{\mathrm{std}}=S_p^{\mathrm{std}}\times\mathbb R$ with the same right-action, range-first formulas and define $$J:G_{p,a}^{\mathrm{act}}\to G_p^{\mathrm{std}},\quad J(x,t)=(\beta(x),t),\qquad
 J^{-1}([r],t)=(\theta([r]),t).
 \label{eq:J}$$ The function map, if well-defined, is contravariant: $$I(f)=f\circ J^{-1}.
 \label{eq:I}$$ The directions in [\[eq:J,eq:I\]](#eq:J,eq:I){reference-type="ref" reference="eq:J,eq:I"} are part of the theorem, not a notational choice.

# Arrow topology and factorization through time {#sec:topology}

[\[lem:topology\]]{#lem:topology label="lem:topology"} The opens of $G=X\times\mathbb R$ are exactly $X\times U$ with $U$ open in $\mathbb R$, and the closed sets are exactly $X\times F$ with $F$ closed. For every $A\subseteq G$, $$\overline A^{\,G}=X\times\overline{\pi_{\mathbb R}(A)}^{\,\mathbb R},
 \qquad \pi_{\mathbb R}(x,t)=t.
 \label{eq:closure}$$ Every relative open subset of $K\subseteq G$ is $K\cap\pi_{\mathbb R}^{-1}(U)$ for an open $U\subseteq\mathbb R$.

The only nonempty basic products are $X\times U$, and unions preserve this form. Complements give the closed sets. A neighborhood of $(x,t)$ has the form $X\times U$ with $t\in U$, so it meets $A$ exactly when $U$ meets $\pi_{\mathbb R}(A)$. This proves [\[eq:closure\]](#eq:closure){reference-type="ref" reference="eq:closure"}; intersecting ambient opens with $K$ proves the relative statement.

[\[thm:qc\]]{#thm:qc label="thm:qc"} For every $K\subseteq G$, $$K\text{ is quasi-compact}\quad\Longleftrightarrow\quad
 \pi_{\mathbb R}(K)\text{ is compact in }\mathbb R.
 \label{eq:qc}$$

The continuous image of a quasi-compact space is quasi-compact, and in Hausdorff $\mathbb R$ this is ordinary compactness. Conversely, an open cover of $K$ consists, after restriction, of sets $K\cap\pi_{\mathbb R}^{-1}(U_i)$. Their time projections cover the compact set $\pi_{\mathbb R}(K)$, so finitely many suffice and the corresponding relative opens cover $K$.

The arrow space is second countable. Each point has the quasi-compact neighborhood $X\times[t-\varepsilon,t+\varepsilon]$ and a basis of open neighborhoods with quasi-compact closure. These positive local statements do not imply local Hausdorffness. If $X$ is nontrivial, $(x,t)$ and $(y,t)$ for $x\ne y$ have identical neighborhoods. Hence $G$ is not $T_0$, no nonempty arrow open is Hausdorff, and the space is nowhere locally Hausdorff. Moreover, no nonempty arrow open is quasi-compact: its nonempty open time projection cannot be compact in the connected line.

[\[prop:topological-groupoid\]]{#prop:topological-groupoid label="prop:topological-groupoid"} The operations in [\[eq:range-source,eq:groupoid-operations\]](#eq:range-source,eq:groupoid-operations){reference-type="ref" reference="eq:range-source,eq:groupoid-operations"} make $G$ a topological groupoid. The composable-pair chart $$\Psi:X\times\mathbb R\times\mathbb R\longrightarrow G^{(2)},\qquad
 \Psi(x,t,u)=((x,t),(x\cdot t,u))$$ is a homeomorphism.

The groupoid identities follow from the right-action law and addition. Both the product subspace $G^{(2)}$ and $X\times\mathbb R^2$ have opens determined only by $(t,u)$, making $\Psi$ and its inverse continuous. Range and source are continuous because their target is indiscrete. In the chart, multiplication is $(x,t,u)\mapsto(x,t+u)$, and inversion changes the time coordinate by $t\mapsto-t$; both are continuous. The unit map is continuous for the same reason.

[\[thm:t0-factor\]]{#thm:t0-factor label="thm:t0-factor"} Let $Y$ be a $T_0$ space. A map $F:G\to Y$ is continuous if and only if there is a unique continuous $g:\mathbb R\to Y$ with $$F=g\circ\pi_{\mathbb R}.
 \label{eq:continuous-factor}$$

Equal-time points are topologically indistinguishable. A continuous map into a $T_0$ target therefore takes the same value on each time fibre. Choose $x_0\in X$ and set $g(t)=F(x_0,t)$. The section $t\mapsto(x_0,t)$ is continuous, hence so is $g$. Conversely, the pullback of a continuous $g$ by $\pi_{\mathbb R}$ is continuous, and surjectivity of the projection gives uniqueness.

The separation hypothesis is sharp. A nonconstant map from a nontrivial indiscrete $X$ into a nontrivial indiscrete target is continuous and may be used at every time. Thus the theorem does not classify arbitrary targets.

[\[thm:measurable-factor\]]{#thm:measurable-factor label="thm:measurable-factor"} The topology-generated sigma-algebra is $$\mathcal B(G)=\{X\times B:B\in\mathcal B(\mathbb R)\}.
 \label{eq:borel}$$ If $(Y,\Sigma_Y)$ is countably separated, a map $F:(G,\mathcal B(G))\to(Y,\Sigma_Y)$ is measurable if and only if it factors uniquely as $g\circ\pi_{\mathbb R}$ for a measurable $g$ on $\mathbb R$.

The displayed family is a sigma-algebra containing all opens. Conversely, the sets $B\subseteq\mathbb R$ for which $X\times B$ is Borel form a sigma-algebra containing the time opens, proving [\[eq:borel\]](#eq:borel){reference-type="ref" reference="eq:borel"}. Let $(E_n)$ be a countable separating family in $Y$. Each $F^{-1}(E_n)$ is $X\times B_n$, so membership cannot distinguish two equal-time unit labels. The separating family forces $F$ to be constant on every time fibre. A measurable section then constructs $g$, and the converse and uniqueness are immediate.

When $X$ is nontrivial, $(G,\mathcal B(G))$ is not countably separated even though its sigma-algebra is countably generated. No standard-Borel-source claim is made.

# Global-QC functions and author fibre convolution {#sec:convolution}

For $g:\mathbb R\to\mathbb C$, define $$\Phi(g)(x,t)=g(t).$$

[\[thm:phi\]]{#thm:phi label="thm:phi"} The map $$\Phi:C_c(\mathbb R)\longrightarrow C_{\mathrm{qc}}^{\mathrm{glob}}(G)$$ is a linear bijection. For every continuous $g$, with no support assumption, $$\operatorname{supp}_G\Phi(g)=X\times\operatorname{supp}_{\mathbb R}(g).
 \label{eq:support}$$

Apply [\[thm:t0-factor\]](#thm:t0-factor){reference-type="ref" reference="thm:t0-factor"} to the Hausdorff target $\mathbb C$. This classifies all globally continuous functions as unique time pullbacks. Their nonzero locus is $X\times\{t:g(t)\ne0\}$, and [\[eq:closure\]](#eq:closure){reference-type="ref" reference="eq:closure"} gives [\[eq:support\]](#eq:support){reference-type="ref" reference="eq:support"}. By [\[thm:qc\]](#thm:qc){reference-type="ref" reference="thm:qc"}, the ambient support is quasi-compact exactly when $\operatorname{supp}_{\mathbb R}(g)$ is compact. Both directions of the support gate are therefore explicit.

[\[thm:fibres\]]{#thm:fibres label="thm:fibres"} For each $x\in X$, $\rho_x$ is a homeomorphism $\mathbb R\to G^x$ and $\lambda^x$ is a positive full-support Radon measure on that locally compact Hausdorff fibre. If $f=\Phi(g)\in C_{\mathrm{qc}}^{\mathrm{glob}}(G)$, then $$\int_{G^x}f\,d\lambda^x=\int_{\mathbb R} g(t)\,dt,
 \label{eq:fibre-integral}$$ which is absolutely finite and independent of $x$. The family also satisfies left invariance on the named function domain.

The subspace opens of $G^x=\{x\}\times\mathbb R$ are exactly $\{x\}\times U$, so the first assertion is transport from Lebesgue measure. The compact time support of $g$ proves absolute integrability and [\[eq:fibre-integral\]](#eq:fibre-integral){reference-type="ref" reference="eq:fibre-integral"}. If $\gamma=(x,t)$ and $\eta=(x\cdot t,u)\in G^{s(\gamma)}$, then $\gamma\eta=(x,t+u)$; translation invariance gives $$\int_{G^{s(\gamma)}} f(\gamma\eta)\,d\lambda^{s(\gamma)}(\eta)
 =\int_{\mathbb R} g(t+u)\,du
 =\int_{\mathbb R} g(v)\,dv.$$

This verifies the GLOB-FIBRE-FAMILY contract directly. It does not invoke a retained Haar-system theorem on the actual owner.

For $f,h\in C_{\mathrm{qc}}^{\mathrm{glob}}(G)$ define, using the range-first coordinates, $$\begin{aligned}
 (f*h)(x,t)&=\int_{\mathbb R} f(x,u)h(x\cdot u,t-u)\,du,\label{eq:arrow-convolution}\\
 f^*(x,t)&=\overline{f(x\cdot t,-t)}.\label{eq:arrow-involution}\end{aligned}$$

[\[thm:star-algebra\]]{#thm:star-algebra label="thm:star-algebra"} For $g,k\in C_c(\mathbb R)$ put $$(g*k)(t)=\int_{\mathbb R} g(u)k(t-u)\,du,
 \qquad g^{\sharp}(t)=\overline{g(-t)}.$$ Then $$\Phi(g)*\Phi(k)=\Phi(g*k),\qquad
 \Phi(g)^*=\Phi(g^{\sharp}),
 \label{eq:intertwining}$$ and $\Phi$ is a $*$-isomorphism from the ordinary compactly supported group convolution algebra onto $C_{\mathrm{qc}}^{\mathrm{glob}}(G)$.

Substitution in [\[eq:arrow-convolution\]](#eq:arrow-convolution){reference-type="ref" reference="eq:arrow-convolution"} gives $$(\Phi(g)*\Phi(k))(x,t)
 =\int_{\mathbb R} g(u)k(t-u)\,du.$$ The integrand is supported on $\operatorname{supp}(g)\cap(t-\operatorname{supp}(k))$, so it is absolutely integrable. Uniform continuity of a compactly supported continuous function yields $$|(g*k)(t+h)-(g*k)(t)|
 \le \|g\|_1\sup_v|k(v+h)-k(v)|\longrightarrow0.$$ Also $\operatorname{supp}(g*k)\subseteq\operatorname{supp}(g)+\operatorname{supp}(k)$, a compact set. The inverse formula gives the second identity in [\[eq:intertwining\]](#eq:intertwining){reference-type="ref" reference="eq:intertwining"}, with $\operatorname{supp}(g^{\sharp})=-\operatorname{supp}(g)$.

For associativity, the absolute-integrability estimate $$\iint_{\mathbb R^2}|g(u)k(v-u)\ell(t-v)|\,du\,dv
 \le \|\ell\|_{\infty}\|g\|_1\|k\|_1$$ licenses Fubini and the substitution $w=v-u$. This proves $(g*k)*\ell=g*(k*\ell)$. Conjugation under the integral and reflection give $(g*k)^{\sharp}=k^{\sharp}*g^{\sharp}$ and $(g^{\sharp})^{\sharp}=g$. Transport through the bijection in [\[thm:phi\]](#thm:phi){reference-type="ref" reference="thm:phi"} completes the proof.

The action has disappeared from [\[eq:intertwining\]](#eq:intertwining){reference-type="ref" reference="eq:intertwining"} as a conclusion of the global factorization theorem. We did not assume that the transformation groupoid was the group $\mathbb R$.

# Unit-regular operators and transported completions {#sec:regular}

The exact source fibre is $$G_x=\{(x\cdot(-t),t):t\in\mathbb R\},\qquad
 \vartheta_x(t)=(x\cdot(-t),t).
 \label{eq:source-fibre}$$ It has the subspace topology transported from $\mathbb R$. Inversion sends $(x,v)$ to $\vartheta_x(-v)$, so reflection invariance of Lebesgue measure gives $$\lambda_x=(\operatorname{inv})_*\lambda^x=(\vartheta_x)_*dt.
 \label{eq:source-measure}$$ Consequently $$U_x:L^2(G_x,\lambda_x)\to L^2(\mathbb R),\qquad
 (U_x\xi)(t)=\xi(\vartheta_x(t))
 \label{eq:Ux}$$ is unitary.

[\[thm:regular\]]{#thm:regular label="thm:regular"} For $f=\Phi(g)$ and initially $\xi\in C_c(G_x)$, set $$(\gamma)=
 \int_{G_x}f(\gamma\eta^{-1})\xi(\eta)\,d\lambda_x(\eta).
 \label{eq:Ind}$$ The integral is pointwise absolutely finite on this dense domain and extends uniquely to a bounded operator on $L^2(G_x,\lambda_x)$. Under [\[eq:Ux\]](#eq:Ux){reference-type="ref" reference="eq:Ux"}, $$(t)
 =\int_{\mathbb R} g(t-u)\zeta(u)\,du
 =[\lambda_{\mathbb R}(g)\zeta](t),
 \label{eq:regular-kernel}$$ and $\|\operatorname{Ind}_x(\Phi(g))\|\le\|g\|_1$.

Write $\gamma=\vartheta_x(t)$ and $\eta=\vartheta_x(u)$. Then $\eta^{-1}=(x,-u)$ and the range-first product is $$\gamma\eta^{-1}=(x\cdot(-t),t-u).$$ This proves the sign $g(t-u)$ in [\[eq:regular-kernel\]](#eq:regular-kernel){reference-type="ref" reference="eq:regular-kernel"}. On compactly supported vectors, the integrand is bounded on compact support and hence absolutely integrable. Young's inequality follows from Minkowski and translation invariance: $$\|\lambda_{\mathbb R}(g)\zeta\|_2
 \le\int_{\mathbb R}|g(v)|\,\|\zeta(\,\cdot-v)\|_2\,dv
 =\|g\|_1\|\zeta\|_2.$$ Density gives the unique bounded extension. For arbitrary $L^2$ vectors, the equality is an $L^2$ identity, not a claim that every equivalence-class representative has a pointwise integral everywhere.

[\[prop:regular-star\]]{#prop:regular-star label="prop:regular-star"} Each $\operatorname{Ind}_x$ is an author-defined bounded $*$-representation: $$\operatorname{Ind}_x(f*h)=\operatorname{Ind}_x(f)\operatorname{Ind}_x(h),\qquad
 \operatorname{Ind}_x(f^*)=\operatorname{Ind}_x(f)^*.$$ Moreover, $\lambda_{\mathbb R}$ is faithful on $C_c(\mathbb R)$.

Associativity on $C_c(\mathbb R)$ gives multiplicativity on the dense vector domain and boundedness extends the identity. With the inner product linear in the first variable, absolute Fubini and a change of variables give $\lambda_{\mathbb R}(g)^*=\lambda_{\mathbb R}(g^{\sharp})$. For faithfulness, if $g\ne0$ take $\zeta(u)=\overline{g(-u)}$. Then $$[\lambda_{\mathbb R}(g)\zeta](0)=\int_{\mathbb R}|g(-u)|^2\,du>0.$$ The convolution is continuous, so it represents a nonzero $L^2$ class.

[\[cor:reduced\]]{#cor:reduced label="cor:reduced"} For every nonempty $X$ and every $g\in C_c(\mathbb R)$, $$\|\Phi(g)\|_{\mathrm{red,glob}}
 :=\sup_{x\in X}\|\operatorname{Ind}_x(\Phi(g))\|
 =\|\lambda_{\mathbb R}(g)\|.
 \label{eq:rednorm}$$ This is a norm.

All base units have the same kernel and norm. This conclusion was obtained from the exact source fibre and the inversion-pushed measure, not from a standard actual-groupoid regular-representation theorem.

Define the full norm separately by $$\|\Phi(g)\|_{\mathrm{full,glob}}:=\|g\|_{C^*(\mathbb R)}.
 \label{eq:fullnorm}$$

[\[thm:completions\]]{#thm:completions label="thm:completions"} Completion of the two named norms gives author-defined $*$-isomorphisms $$C_{\mathrm{glob}}^{\mathrm{full}}(G)\cong C^*(\mathbb R),\qquad
 C_{\mathrm{glob}}^{\mathrm{red}}(G)\cong C_r^*(\mathbb R).
 \label{eq:transport}$$ Because $\mathbb R$ is abelian and amenable, the group full and reduced norms agree. With $$\widehat g(\xi)=\int_{\mathbb R} g(t)e^{-it\xi}\,dt,$$ the group Fourier theorem yields $$C_{\mathrm{glob}}^{\mathrm{full}}(G)\cong C_{\mathrm{glob}}^{\mathrm{red}}(G)\cong C_0(\mathbb R).
 \label{eq:Fourier-model}$$

The first line is definitional for the full norm and follows from [\[eq:rednorm\]](#eq:rednorm){reference-type="ref" reference="eq:rednorm"} for the reduced norm. Williams identifies the left-regular group norm, proves the LCA Fourier model, and records the abelian/amenable full--reduced equality [@Williams2007 Example 1.80, Proposition 3.1, Examples 7.9 and 7.11, and Theorem 7.13]. These theorems belong to the group $\mathbb R$ and apply only after [\[eq:transport\]](#eq:transport){reference-type="ref" reference="eq:transport"} has been established.

The definitions in [\[eq:rednorm,eq:fullnorm\]](#eq:rednorm,eq:fullnorm){reference-type="ref" reference="eq:rednorm,eq:fullnorm"} are different even though their completions have isomorphic final models. Equality is credited to amenability of the group $\mathbb R$, not to amenability of the actual groupoid.

# Hausdorff-open diagnostic and strict standard proxy {#sec:proxy}

[\[prop:hopen\]]{#prop:hopen label="prop:hopen"} If $X$ is nontrivial indiscrete, no nonempty open subset of $G$ is Hausdorff and $$C_c^{\mathrm{HOp}}(G)=\{0\}.
 \label{eq:hopen-zero}$$

A nonempty open is $X\times U$. Choose $t\in U$ and distinct $x,y\in X$. The equal-time points $(x,t)$ and $(y,t)$ have identical relative neighborhoods, so the open is not even $T_0$. Thus the empty patch is the only Hausdorff open and contributes only the zero extension.

The zero in [\[eq:hopen-zero\]](#eq:hopen-zero){reference-type="ref" reference="eq:hopen-zero"} is [diagnostic\_only]{.smallcaps}. It has no licensed convolution, norm, completion, or standard-algebra status. If $g\in C_c(\mathbb R)$ is nonzero, $\Phi(g)$ is an explicit nonzero element of $C_{\mathrm{qc}}^{\mathrm{glob}}(G)$ on the same topology. The two records therefore form a genuine convention split.

P0.19P0.30P0.20Y Record & Audited actual-owner obstruction & Classification & Licensed role\
Tu [@Tu2004] & Tu-local compactness requires compact Hausdorff neighborhoods and hence local Hausdorffness & [not\_applicable]{.smallcaps}& terminology and raw HOpen comparator\
Muhly--Williams [@MuhlyWilliams2008] & Hausdorff units and compact Hausdorff arrow neighborhoods fail & [not\_applicable]{.smallcaps}& accepted raw patch-span practice only\
Exel [@Exel2011] & unit is non-Hausdorff and continuous-$\mathbb R$ range/source are not etale & [not\_applicable]{.smallcaps}& independent boundary only\
Buss--Holkar--Meyer [@BussHolkarMeyer2018] & Hausdorff groupoid standing hypothesis fails & [not\_applicable]{.smallcaps}& full proxy bridge only\
$C_c^{\mathrm{HOp}}(G)$ & direct author raw diagnostic & [diagnostic\_only]{.smallcaps}& exact value $0$, no algebraic promotion\
GLOB-FIBRE-FAMILY, $\operatorname{Ind}_x$ & direct author definitions with proved contracts & [author\_defined\_direct]{.smallcaps} & actual global domain only\
Group $\mathbb R$ & ordinary LCA harmonic analysis & [applicable\_group\_R]{.smallcaps} & transport after direct dense/norm proofs\
Standard proxy & ordinary compact Hausdorff circle and arrow space & [applicable\_proxy\_only]{.smallcaps} & full crossed-product and comparison records\

The table proves non-applicability of named sources, not nonexistence of every conceivable theory. The direct global-QC construction itself demonstrates why the latter statement would be false.

[\[thm:J\]]{#thm:J label="thm:J"} The map $J$ in [\[eq:J\]](#eq:J){reference-type="ref" reference="eq:J"} is a set-groupoid isomorphism. Its topology direction is strict: $$J\text{ is not continuous},\qquad J^{-1}\text{ is continuous}.
 \label{eq:J-direction}$$

Equivariance $\beta(x\cdot t)=\beta(x)+t$ verifies source and product: $$J((x,t)(x\cdot t,u))=(\beta(x),t+u)
 =J(x,t)J(x\cdot t,u),$$ and inverse and units follow similarly. Every actual arrow open is $X\times U$, whose inverse image under $J^{-1}$ is $S_p^{\mathrm{std}}\times U$, proving continuity of $J^{-1}$. If $V$ is a nonempty proper open circle arc, then $V\times\mathbb R$ is proxy-open but its inverse image under $J$ is $\beta^{-1}(V)\times\mathbb R$, a nonempty proper unit-coordinate subset and therefore not actual-open.

[\[thm:I\]]{#thm:I label="thm:I"} The map $$I:C_{\mathrm{qc}}^{\mathrm{glob}}(G_{p,a}^{\mathrm{act}})\longrightarrow C_c(G_p^{\mathrm{std}}),\qquad I(f)=f\circ J^{-1},$$ is an injective $*$-homomorphism at the test-function level. It preserves the range-fibre Lebesgue measures, fibre integrals, support, convolution, and involution. Its exact image is $$A_{\mathrm{const}}=\{F\in C_c(G_p^{\mathrm{std}}):F([r],t)=F([s],t)
 \text{ for all }[r],[s],t\},
 \label{eq:Aconst}$$ and $A_{\mathrm{const}}$ is a proper subalgebra.

If $f=\Phi(g)$, then $$I(f)([r],t)=g(t),\qquad
 \operatorname{supp}_{\mathrm{std}}I(f)=S_p^{\mathrm{std}}\times\operatorname{supp}_{\mathbb R}(g),$$ which is compact. Surjectivity of $J^{-1}$ gives injectivity. On each range fibre, $J$ preserves the time coordinate and hence the pushed-forward Lebesgue measure. The proxy operations are $$\begin{aligned}
 (F*_{\mathrm{std}}H)([r],t)
 &=\int_{\mathbb R} F([r],u)H([r+u],t-u)\,du,\\
 F^*([r],t)&=\overline{F([r+t],-t)},\end{aligned}$$ so unit-constant functions reproduce the formulas in [\[eq:intertwining\]](#eq:intertwining){reference-type="ref" reference="eq:intertwining"}.

Every image lies in $A_{\mathrm{const}}$. Conversely, if $F$ lies in $A_{\mathrm{const}}$, set $g(t)=F([r_0],t)$. Compactness of $\operatorname{supp}(F)$ projects to compactness of $\operatorname{supp}(g)$, and $F=I(\Phi(g))$. Finally, for nonzero $k\in C_c(\mathbb R)$, $$F_{\mathrm{out}}([r],t)=e^{2\pi i r/L_p}k(t)
 \label{eq:strict-witness}$$ is continuous and compactly supported on the proxy but varies with $[r]$. Thus it is not in $A_{\mathrm{const}}$.

#### Completion stop.

Theorem [\[thm:I\]](#thm:I){reference-type="ref" reference="thm:I"} gives no map between any completions. Such a map would require a named target norm and an independent boundedness or isometry proof. The proxy source ladder does not provide this missing estimate. BHM gives a full transformation-groupoid/full crossed-product bridge [@BussHolkarMeyer2018 Theorem 7.1]; Green and MRW give full-level Morita equivalence [@Green1978 Proposition 3, physical p. 13 / printed p. 203] [@MuhlyRenaultWilliams1987 Theorem 2.8, physical p. 8 / printed p. 10]; Brown--Green--Rieffel gives stable isomorphism under its hypotheses [@BrownGreenRieffel1977 Theorem 1.2, physical p. 4 / printed p. 351]; and Williams gives a separate unstabilized full homogeneous-space tensor model [@Williams2007 Eq. (4.63) and Theorem 4.30]. These strengths are not interchangeable and remain proxy-only. In particular, none proves boundedness, density, Morita equivalence, stable isomorphism, or a completion extension of $I$.

*Prose equivalent for [\[fig:proxy-action-blind\]](#fig:proxy-action-blind){reference-type="ref" reference="fig:proxy-action-blind"}.* The actual and proxy groupoids are set-groupoid isomorphic, but continuity holds only from the proxy to the actual topology. Pullback gives a strict test-function inclusion whose image is unit-constant, and the comparison stops before norms. Independently, trivial, transitive, nontransitive, and label-period controls all collapse to the same group-$\mathbb R$ algebra and norm.

# Action blindness, controls, and Route consequences {#sec:controls-route}

[\[thm:action-blind\]]{#thm:action-blind label="thm:action-blind"} Let $X$ be any nonempty indiscrete space and let $\alpha$ be any right $\mathbb R$-action. Then

1.  $\Phi_X:C_c(\mathbb R)\to C_{\mathrm{qc}}^{\mathrm{glob}}(G(X,\alpha))$ is a canonical $*$-isomorphism;

2.  the author range-fibre integrals, convolution, and involution are independent of $X$ and $\alpha$ under $\Phi_X$;

3.  every author unit-regular operator is unitarily $\lambda_{\mathbb R}$;

4.  the author reduced and transported full norms are the ordinary group norms, and their completions are the group-$\mathbb R$ models in [\[eq:Fourier-model\]](#eq:Fourier-model){reference-type="ref" reference="eq:Fourier-model"}.

If $X$ is nontrivial, $C_c^{\mathrm{HOp}}(G(X,\alpha))=0$. If $X$ is a singleton, the global convolution conclusion remains true but the HOpen-zero statement does not: the singleton product is Hausdorff.

The topology, factorization, and support arguments in [\[lem:topology,thm:qc,thm:t0-factor,thm:phi\]](#lem:topology,thm:qc,thm:t0-factor,thm:phi){reference-type="ref" reference="lem:topology,thm:qc,thm:t0-factor,thm:phi"} do not mention the action. For $f=\Phi_X(g)$ and $h=\Phi_X(k)$, $$(f*h)(x,t)=\int g(u)k(t-u)\,du,
 \qquad f^*(x,t)=\overline{g(-t)},$$ so the action disappears from the operations. The range-fibre formula is ordinary Lebesgue integration. The source chart $\vartheta_x(t)=(x\cdot(-t),t)$ and the computation $\vartheta_x(t)\vartheta_x(u)^{-1}=(x\cdot(-t),t-u)$ give the same regular kernel at every unit. The norm and completion statements follow exactly as in [5](#sec:regular){reference-type="ref" reference="sec:regular"}. For nontrivial $X$, [\[prop:hopen\]](#prop:hopen){reference-type="ref" reference="prop:hopen"} is independent of the action. The singleton exception is immediate.

[\[cor:math-controls\]]{#cor:math-controls label="cor:math-controls"} The conclusion of [\[thm:action-blind\]](#thm:action-blind){reference-type="ref" reference="thm:action-blind"} is unchanged for:

1.  a nontrivial indiscrete $X$ with the trivial action, whose stabilizers are all of $\mathbb R$;

2.  $X=(\{0,1\}\times\mathbb R/\mathbb Z)_{\mathrm{indisc}}$ with two nontransitive circle orbits and stabilizer $\mathbb Z$;

3.  $X_{\ell,L}=(\{\ell\}\times\mathbb R/L\mathbb Z)_{\mathrm{indisc}}$ with arbitrary $L>0$ and a transitive action;

4.  independent prime, composite, or arbitrary labels and independent positive periods.

The nontransitive control is deliberately infinite. Since $\mathbb R$ is divisible, it has no nontrivial finite quotient, so a nontrivial action of $\mathbb R$ on a finite set would be a false control. The exact controls show that the theorem proves too much for arithmetic specificity: different orbit decompositions and stabilizers yield the same analytic signature.

[\[cor:rational-witt\]]{#cor:rational-witt label="cor:rational-witt"} For every rational prime $p$ and every normalized companion-paper orbit label $a$, the actual fixed-orbit groupoid $G_{p,a}^{\mathrm{act}}$ satisfies $$C_{\mathrm{qc}}^{\mathrm{glob}}(G_{p,a}^{\mathrm{act}})\cong C_c(\mathbb R),\qquad
 C_c^{\mathrm{HOp}}(G_{p,a}^{\mathrm{act}})=0,$$ and its author unit-regular norms and transported completions are the group $\mathbb R$ records of [\[eq:rednorm,eq:Fourier-model\]](#eq:rednorm,eq:Fourier-model){reference-type="ref" reference="eq:rednorm,eq:Fourier-model"}. The analytic output retains none of $p$, $a$, $L_p$, the action, the orbit decomposition, or the stabilizer $L_p\mathbb Z$.

The host-versus-analytic distinction is essential. The concrete groupoid still has $X_{p,a}$, its source and range maps, right action, and stabilizer as relations. The corollary states only that these data vanish after passage to the named function, operator, norm, and completion records. It is fixed- orbit only and supplies no prime-coproduct, packet, or full-suspension theorem.

## Deterministic reproducibility receipt

The direct proofs above establish the universal continuous statements. A standard-library-only Python package supplies finite regression oracles and adversarial witnesses. Its frozen manifest has SHA-256 `de55c58ad7efc133b0d0865f392a30b52f6b05f89f64878cea0910b7eab557ea`. The exact receipt is:

-   57/57 unit tests passed;

-   12 CSV artifacts containing 642 data rows;

-   5/5 intentional source/range and sign negatives detected;

-   strict verify-only passed for checked-in results and for two fresh generations;

-   all 13 generated artifacts were byte-identical across checked-in, fresh-one, and fresh-two runs;

-   the forbidden Python cache/bytecode scan passed.

The suite includes topology enumeration, $T_0$ and measurable target factorization, support projection, convolution and involution, unit-regular matrices, HOpen zero, proxy strictness, action blindness, and independent label-period changes. It uses no network, external package, external dataset, randomness, fitted parameter, target-zero table, or timestamp. These finite checks are witnesses and regression guards. They do not prove the universal topological or analytic theorems.

## Typed Route ledger

Seven Stage-11 records evaluate seven nonconflated owners. The concrete actual algebra and HOpen diagnostic retain only a weak host relation. The test map has a weak relation with evidence status [modeling\_choice]{.smallcaps}. The abstract algebra, transported completions, and generic control have already erased their arithmetic host. Every record fails A1 through A4; every A2--A4 failure is [not\_testable]{.smallcaps}, because the same owner has no determinant, global analytic object, or natural lift.

P0.20P0.22P0.34Y Candidate & SHA-256 & $(A0,A1,A2,A3,A4)$ & Overall\
`DEN-EF-ACTUAL-GLOB-QC-CONV-P` & `ce52ba0f...e551` & $(\mathrm{WEAK},\mathrm{FAIL},\mathrm{FAIL},\mathrm{FAIL},\mathrm{FAIL})$ & exploratory\
`DEN-EF-GLOB-QC-ABSTRACT-CCR` & `775fb3ac...6ccd` & $(\mathrm{FAIL},\mathrm{FAIL},\mathrm{FAIL},\mathrm{FAIL},\mathrm{FAIL})$ & rejected\
`DEN-EF-GLOB-FULL-TRANSPORT-R` & `fb1f8bf7...8830` & $(\mathrm{FAIL},\mathrm{FAIL},\mathrm{FAIL},\mathrm{FAIL},\mathrm{FAIL})$ & rejected\
`DEN-EF-GLOB-RED-REGULAR-R` & `45887d09...24b5` & $(\mathrm{FAIL},\mathrm{FAIL},\mathrm{FAIL},\mathrm{FAIL},\mathrm{FAIL})$ & rejected\
`DEN-EF-ACTUAL-HOPEN-DIAGNOSTIC-P` & `25908c99...c6d7` & $(\mathrm{WEAK},\mathrm{FAIL},\mathrm{FAIL},\mathrm{FAIL},\mathrm{FAIL})$ & exploratory\
`DEN-EF-ACTUAL-STD-TEST-MAP-P` & `e904f85d...cfac` & $(\mathrm{WEAK},\mathrm{FAIL},\mathrm{FAIL},\mathrm{FAIL},\mathrm{FAIL})$ & exploratory\
`INDISC-R-ACTION-GLOB-CONV-CONTROL` & `23480710...a1b` & $(\mathrm{FAIL},\mathrm{FAIL},\mathrm{FAIL},\mathrm{FAIL},\mathrm{FAIL})$ & rejected\

The abbreviated hashes in [\[tab:route-ledger\]](#tab:route-ledger){reference-type="ref" reference="tab:route-ledger"} correspond, in order, to the full SHA-256 values $$\begin{aligned}
&\texttt{ce52ba0fddf39652a37992ff7babeb590bfcb5ce8853ee6aa87b2c877634e551},\\
&\texttt{775fb3ac86771744d3f15f708a73fc634992f770a8d7b3d04f570563054a6ccd},\\
&\texttt{fb1f8bf736099a2eca5175d818ad7a00f7f1de2d0ddb699135e035ab311d8830},\\
&\texttt{45887d091bb97853febaf0329e7035655e69ec44c49ee7919ce55a8ef3de24b5},\\
&\texttt{25908c995d5a1f2a6f8478d62715e7cf4fc653b76ae2f6bf9fdfe71f8cc3c6d7},\\
&\texttt{e904f85d078e84188f6d40a07e3e1fb1c7426068b8c4a9c4a773df221fd2cfac},\\
&\texttt{23480710707367d9f77b4896a7c85e073b17dcc5a4f8aae3814bff972d27ba1b}.\end{aligned}$$ The corresponding tuples, again in table order and transcribed without abbreviation, are:

1.  `(A0_WEAK_ARITHMETIC_RELATION,` `A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`;

2.  `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`;

3.  `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`;

4.  `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`;

5.  `(A0_WEAK_ARITHMETIC_RELATION,` `A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`;

6.  `(A0_WEAK_ARITHMETIC_RELATION,` `A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`;

7.  `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`.

Exactly three rows are exploratory negative priors and four are rejected. No A-coordinate is borrowed from another owner. An abstract bounded convolution representation on $L^2(\mathbb R)$ is not a Hilbert--Polya operator, and every record has $A4\_\mathrm{FAIL}$. Hence Route B is false and no Route-B record exists.

# Limitations and conclusion {#sec:conclusion}

This paper establishes an exact theorem plus an obstruction. On every hash-locked rational-Witt fixed orbit with its actual inherited topology, the author global-QC convention gives a nonzero convolution $*$-algebra canonically isomorphic to $C_c(\mathbb R)$. The author source-fibre family is unitarily the left regular group representation, and the separately defined transported completions identify with $C_0(\mathbb R)$. Under the raw Hausdorff-open convention, however, the diagnostic span is zero. The ordinary-circle proxy supplies more test functions, but the actual image is only the proper unit-coordinate-constant subalgebra and the proof stops before every norm comparison.

Several limitations are structural rather than technical. First, the framework audit is finite: it establishes that the retained Tu, Muhly--Williams, Exel, and BHM actual-owner hypotheses fail. It does not prove that no other non-Hausdorff convolution framework could be developed. Second, GLOB-FIBRE-FAMILY, $\operatorname{Ind}_x$, $C_{\mathrm{glob}}^{\mathrm{full}}$, and $C_{\mathrm{glob}}^{\mathrm{red}}$ are explicit author records. Their direct proofs do not turn them into standard actual-groupoid objects. Third, the comparison with the standard proxy is test-level only. Nothing here proves density, boundedness, an isometry, Morita equivalence, stable isomorphism, or a completion extension of $I$. Fourth, the result is fixed-orbit only. No packet aggregation, prime coproduct, full suspension, determinant, functional equation, explicit formula, quantization, or Route-B entry is constructed.

The novelty assessment is likewise bounded. As of 2026-08-15, the documented bounded Phase-2 search located no precedent for the exact rational-Witt actual-orbit convention-split package. This sentence reports only the documented search. The generic indiscrete-product theorem, group convolution on $\mathbb R$, the HOpen literature, and standard transformation- groupoid theory receive no individual priority claim.

Most importantly, the generic theorem separates the host from its analytic shadow. The host still contains the rational-Witt action, orbit, and stabilizer. Global separated-valued continuity removes the unit coordinate, after which convolution, regular operators, and transported norms cannot recover it. The same result on trivial and nontransitive actions is not a defect in the proof; it is the decisive evidence that the collapsed analytic object is unsuitable for arithmetic promotion.

Any successor owner should therefore meet three minimum conditions before receiving arithmetic credit. It should be source-canonical rather than a retopologized modeling choice, it should retain enough action data to survive its analytic functor, and it should distinguish the rational-Witt action from at least one trivial or nontransitive control. An enriched local, sheaf, or stack construction may be investigated only after a fresh source, owner, and domain lock; none is asserted to work here. In particular, the actual host, the erased group-$\mathbb R$ completion, and the standard proxy may not be spliced together to manufacture a positive result.

# Declarations {#declarations .unnumbered}

#### Author contributions.

Final CRediT roles: **AUTHOR TO CONFIRM**. The provisional single author is Liang Wang.

#### Funding.

**AUTHOR TO CONFIRM**. No grant number is asserted in this manuscript.

#### Conflicts of interest.

**AUTHOR TO CONFIRM**.

#### Acknowledgments.

**AUTHOR TO CONFIRM**.

#### Ethics.

This mathematical proof study used no human participants, animals, clinical records, personal information, confidential information, or sensitive data. Human- or animal-subject approval is not applicable.

#### Data and code availability.

The results use deterministic exact finite controls rather than an external empirical dataset. The repository contains the standard-library-only source, tests, reproduction script, 12 CSV artifacts, and the hash-locked manifest. The public repository tag, license, archive, DOI, and release date are **AUTHOR TO CONFIRM**; no permanent archive is promised here.

#### AI assistance.

AI assistance was used for research-protocol structuring, bounded source discovery, exact-byte comparison, symbolic proof drafting, deterministic control generation, adversarial review, Route-record checking, composition planning, and manuscript formatting. The author verified the cited sources and retains responsibility for every definition, theorem, computation, and publication claim. Venue-specific wording remains **AUTHOR TO CONFIRM** against the venue's current policy.
