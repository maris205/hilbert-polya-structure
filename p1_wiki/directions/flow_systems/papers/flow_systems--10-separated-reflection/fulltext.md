---
p1_kind: "derived-fulltext-reading-copy"
route: "flow_systems"
logical_paper_id: "flow_systems--10-separated-reflection"
canonical_tex: "flow_systems/papers/10-separated-reflection/paper/manuscript.tex"
canonical_pdf: "flow_systems/papers/10-separated-reflection/paper/paper.pdf"
source_sha256: "27bae88814f16263de444bb1650e4a550d0f0eca327f3c551d7c2097f353d315"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Separated Reflections and Observable Collapse of Indiscrete Arithmetic Prime Packets

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../flow_systems/papers/10-separated-reflection>)
- [规范 TeX](<../../../../../flow_systems/papers/10-separated-reflection/paper/manuscript.tex>)
- [关联 PDF](<../../../../../flow_systems/papers/10-separated-reflection/paper/paper.pdf>)
- [支撑 Markdown](<../../../../../flow_systems/papers/10-separated-reflection/README.md>)
- [BibTeX](<../../../../../flow_systems/papers/10-separated-reflection/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Each fixed-prime packet in Deninger's finite-kernel rational-Witt flow is a nontrivial indiscrete space for its inherited topology. This paper determines exactly what remains when that input is passed through separated topological, continuous-observable, measurable, positive-finite-measure, continuous-character, and copied-component interfaces. For the packet, every inherited orbit, and the time-orbit quotient, the Kolmogorov, Hausdorff, and completely regular Hausdorff universal images are singletons. Continuous scalar functions are constant, the Borel algebra is trivial, measurable maps to countably separated targets are constant, positive finite measures are classified by total mass, and all Dirac measures coincide. A group law transported to the actual quotient through its fixed set bijection is continuous for the indiscrete topology, but its only continuous circle character is trivial. Continuous maps to one fixed bounded-operator carrier with the norm, strong, or weak operator topology are likewise constant. The ordinary circle is a strictly finer proxy: the actual-to-circle bijection is not continuous, whereas its inverse is. For an explicitly tagged countable coproduct of copied packets, the Kolmogorov quotient retains exactly the discrete labels and positive finite measures form the cone $\ell^1_+$ of component masses. Prime, composite, and arbitrary labels have the same abstract behavior; $p\mapsto\log p$ remains external data. Deterministic controls pass 24/24 tests but serve only as finite regression witnesses. The resulting Route-A records are exploratory or rejected, and Route B is not invoked.

  **Keywords:** arithmetic dynamics; rational Witt vectors; indiscrete topology; separated reflection; continuous observables; positive finite measures; tagged coproduct
author:
- |
  Liang Wang\
  School of Artificial Intelligence and Automation\
  Huazhong University of Science and Technology (HUST)\
  <wangliang.f@gmail.com>
bibliography:
- references.bib
date: 14 August 2026
title: |
  **Separated Reflections and Observable Collapse\
  of Indiscrete Arithmetic Prime Packets**
```

## Markdown 正文

**中文摘要**

Deninger 有限核有理 Witt 流中的每个固定素数包均为非平凡空间，其继承拓扑不可分。本文研究这些实际对象经过分离拓扑、连续观测、可测映射、正有限测度、连续特征以及复制分量接口后究竟保留哪些信息。对于实际素数包、其中每条继承轨道及时间轨道商，其 Kolmogorov、Hausdorff 与完全正则 Hausdorff 泛像均退化为单点；连续复值函数只能是常值，Borel 代数仅含空集与全集，到可数可分目标的可测映射均为常值，正有限测度完全由总质量决定，所有 Dirac 测度相同。通过固定集合双射输运到实际商上的群律与不可分拓扑相容，但到通常圆周群的连续特征只有平凡特征；到同一固定有界算子空间的范数、强算子和弱算子拓扑连续映射也全为常值。标准圆周只是严格更细的代理：从实际轨道到圆周的双射不连续，反向映射连续。对显式定义的可数带标签复制余积，Kolmogorov 商恰好保留离散标签，正有限测度由 $\ell^1_+$ 分量质量刻画。素数、合数与任意标签的抽象结论一致，$p\mapsto\log p$ 仍须由外部算术数据给出。24 项确定性控制全部通过，但仅作为有限回归证据；最终 Route A 结论为探索性或拒绝，Route B 未被启动。

**中文关键词：** 算术动力系统；有理 Witt 向量；不可分拓扑；分离反射；连续观测；正有限测度；带标签余积

# Introduction

Deninger's rational-Witt construction organizes arithmetic closed points by periodic structures inside a positive-real suspension flow. The finite-kernel object, fixed-prime packet coordinates, action, and stabilizer are described in the source construction [@Deninger2026 Eqs. (35) and (38)--(39), arXiv-v4 physical pp. 32--33; Section 6 and Theorem 6.1, physical pp. 38--39]. Those data are algebraic and equivariant at the set level; a displayed coordinate bijection does not by itself transfer a topology. The companion paper resolves this distinction for the exact inherited quotient topology. For every rational prime $p$, the genuine finite-kernel packet $\Gamma_p$, each of its inherited $\mathbb R_{>0}$-orbits, and the time-orbit quotient are nonempty, nontrivial indiscrete spaces [@Wang2026Packet Theorem 5.1 and Corollaries 5.2--5.4]. That theorem is the sole arithmetic-topology input imported here.

Indiscreteness is a strong negative separation statement, but it is not by itself a complete account of the interfaces normally used in topology, analysis, and measurable dynamics. A space can be replaced by a separated reflection, tested by continuous scalar or operator-valued functions, equipped with its topology-generated Borel algebra, or mapped to a better separated measurable target. One may also ask whether a set-level group law is compatible with the actual topology, whether continuous characters survive, and what changes when independently copied components are assembled by a tagged coproduct. Each operation has its own domain and universal property. Treating them as interchangeable would obscure precisely the owner distinction established by the companion paper.

The aim of this paper is therefore a typed classification, not a new proof of indiscreteness and not a spectral construction. The general mathematical engine is elementary: every continuous map from a nonempty indiscrete space to a $T_0$ target is constant. We use that engine to verify the universal properties of three singleton separated images, identify continuous scalar and fixed-operator observables, and establish a sharp measurable analogue for countably separated targets. We then classify positive countably additive finite measures without adding a regularity adjective. These results are standard consequences for a generic indiscrete space; the contribution is their exact assembly on the locked rational-Witt owners, together with the group-law, circle-direction, and tagged-copy boundaries.

The distinction between actual objects and proxies is central. The quotient $\mathsf{ACT\mbox{-}Q}_p$ has a frozen set bijection $\phi_p$ to an algebraic quotient $U_p/H_p$. We transport only the quotient-group law through $\phi_p$ and test that law against the independently fixed actual topology. We do not transport a topology back from $U_p/H_p$, call the law source-canonical, or promote $\phi_p$ to a homeomorphism. Likewise a basepoint choice gives a set bijection $\beta_{p,a}$ from an actual inherited orbit to an ordinary circle. The two directions have opposite continuity behavior, so the circle is a finer retopology proxy rather than a separated reflection of the actual orbit.

A second distinction separates an explicit modeling construction from the global source. Given a countable label set $I$ and a family of nonempty indiscrete spaces, their tagged topological coproduct has one clopen component for each label. Its Kolmogorov quotient is $I$ with the discrete topology. Its positive finite Borel measures are exactly nonnegative summable families of component masses. Applying this theorem to copied prime packets retains prime labels because the labels were inserted, not because topology detects primality. Replacing primes by composites or arbitrary labels gives the same classification. The arithmetic scalar $\log p$ can be placed on the discrete prime set, but it is unbounded, does not vanish at infinity, and is not selected by either topology or the measure cone.

The theorem ledger is summarized in [\[tab:mainledger\]](#tab:mainledger){reference-type="ref" reference="tab:mainledger"}. P10-1--P10-8 are mathematical statements. P10-9 records deterministic regression controls and is not proof. P10-10 is a formal same-owner Route adjudication: it does not combine coordinates from actual, proxy, copied, or historical records.

P0.13P0.29Y ID & Result & Boundary\
P10-1 & Three separated universal images are singletons. & Direct universal properties on exact actual owners; no general priority claim.\
P10-2 & $C(X)=C_b(X)=\mathbb C1_X$ isometrically and evaluations coincide. & No compact-Hausdorff or Gelfand-duality promotion.\
P10-3 & $\mathcal B(X)=\{\varnothing,X\}$ and separated measurable maps are constant. & Target must be countably separated; source is not standard Borel.\
P10-4 & $\mathcal M_{\mathrm{fin}}^+(X)\cong[0,\infty)$ by total mass; Dirac measures coincide. & No Radon, Haar, state, trace, support, signed, or complex-measure claim.\
P10-5 & The transported law is topological; continuous circle characters and fixed-operator maps collapse. & No algebraic-character, representation, measurable-field, or unbounded-operator theorem.\
P10-6 & $\beta_{p,a}$ is not continuous; $\beta_{p,a}^{-1}$ is continuous. & The ordinary circle is a proxy, not a factor or reflection.\
P10-7--8 & A tagged copied coproduct retains discrete labels and $\ell^1_+$ masses. & Modeling choice only; not the topology of a global suspension.\
P10-9--10 & 24/24 controls pass; five Route records are exploratory and two rejected. & Controls are finite witnesses; Route B remains false.\

## Proof architecture and quantifier discipline

The quantifiers are uniform but owner-specific. The prime $p$ is arbitrary, and whenever an inherited orbit is used its label $a\in U_p/H_p$ is arbitrary. A theorem stated for "each registered actual owner" therefore gives three separate applications of the same general reduction: one to $\mathsf{ACT\mbox{-}PACKET}_p$, one to every $\mathsf{ACT\mbox{-}ORBIT}_{p,a}$, and one to $\mathsf{ACT\mbox{-}Q}_p$. It does not form a union of those spaces or claim that a single map has all three as its domain. This point matters because packet, orbit, and quotient carry different set constructions even though Paper 9 proves the same separation type for each.

The proof has two layers. At the first layer, a generic nonempty indiscrete space $X$ is tested against precisely typed targets. This produces the constant-map lemma, direct separated universal properties, the scalar algebra, the Borel algebra, the countably-separated measurable-map result, the total-mass cone, and the fixed-operator target classification. None of these elementary statements is presented as new general topology. At the second layer, Paper 9's source-specific indiscreteness theorem licenses their application to the three rational-Witt owners. The arithmetic content enters only through that exact imported theorem and through the already frozen set/action data.

Each interface is proved from its own definition. The Kolmogorov quotient is computed from topological indistinguishability, while the Hausdorff and completely regular Hausdorff outputs are checked by direct factorization. The scalar result establishes equality of function sets before attaching the supremum norm. The Borel result generates a sigma-algebra from the actual topology rather than from coordinates. The measure result classifies positive finite countably additive functions on that exact sigma-algebra and never evaluates a nonmeasurable singleton. This ordering prevents a property from a better separated proxy from entering an actual-owner proof.

The group and operator assertions require additional type checks. The group law is a Paper-10 definition transported through the frozen set bijection $\phi_p$; continuity is then tested against the independently fixed actual topology. The character target is the ordinary Hausdorff circle, so only continuous characters are classified. For operators, norm, SOT, and WOT are considered separately on one fixed carrier $B(\ell^2(\mathbb N))$. No result about a homomorphism, representation, or unbounded domain is inferred from a theorem about arbitrary continuous maps.

The standard-circle comparison is directional. The domain and codomain topology are stated before either continuity test, and the two inverse set maps are checked independently. Noncontinuity of $\beta_{p,a}$ is a consequence of its nonconstancy and separated codomain; continuity of $\beta_{p,a}^{-1}$ follows from its indiscrete codomain. These facts identify a finer retopology without turning that retopology into a source-defined reflection.

The copied-component part begins again with an abstract theorem. A countable label set $I$ is arbitrary, every component is merely assumed nonempty and indiscrete, and the coproduct topology is explicitly declared. Only after opens, Borel sets, indistinguishability classes, continuous maps, and finite measures are classified do we set $I=\mathbb P$. The composite and arbitrary-label controls then follow from the same theorem rather than from a numerical analogy. This order exposes exactly which information came from the tags.

Finally, the deterministic suite and Route files have evidential roles distinct from proof. Controls test finite enumerations, transcription, schema, and reproducibility. They cannot establish the source-specific infinite statements. Route records evaluate the proved interfaces under the frozen A0--A4 rubric and cannot supply a missing theorem. Keeping these roles separate makes a negative verdict informative: it identifies the exact gate that fails without converting a control receipt or YAML field into mathematical evidence.

The source review was deliberately bounded. No direct precedent for the exact rational-Witt packet package was found within the bounded Phase-2 search as of 2026-08-14. This reports the outcome of a documented search; it is not a claim of priority or of global absence. Standard terminology for topological indistinguishability and Kolmogorov quotients follows Pirttimäki [@Pirttimaki2021 physical pp. 4--6, 9, 12--13]; categorical reflection vocabulary is aligned with the inspected literature [@CagliariMantovani2003 physical pp. 3--4 of the author preprint] and [@HernandezArzusaHernandez2020 arXiv-v2 physical pp. 2--6]. All specialized conclusions below are proved directly rather than delegated to those references.

# Typed objects and the indiscrete reduction {#sec:typed}

Fix a rational prime $p$. Write $$U_p=\prod_{\ell\ne p}\mathbb Z_\ell^{\times},\qquad H_p=p^{\widehat{\mathbb Z}},$$ using the algebraic symbols fixed in the companion construction. For $a\in U_p/H_p$, the three actual owners are $$\begin{aligned}
 \mathsf{ACT\mbox{-}PACKET}_p&=\Gamma_p,\\
 \mathsf{ACT\mbox{-}ORBIT}_{p,a}&=\text{the inherited orbit labeled by }a,\\
 \mathsf{ACT\mbox{-}Q}_p&=\Gamma_p/(\mathbb R_{>0}/p^{\mathbb Z}).\end{aligned}$$ The displayed names carry the inherited packet, subspace, and quotient topologies respectively. The set bijections used later are $$\phi_p:|\mathsf{ACT\mbox{-}Q}_p|\longrightarrow U_p/H_p,
 \qquad
 \beta_{p,a}:|\mathsf{ACT\mbox{-}ORBIT}_{p,a}|\longrightarrow|\mathsf{STD\mbox{-}CIRCLE}_p|.$$ Vertical bars emphasize that the maps are initially maps of underlying sets. No topology is assigned by these formulas. The standard circle $\mathsf{STD\mbox{-}CIRCLE}_p$ is an explicitly retopologized copy of $\mathbb R_{>0}/p^{\mathbb Z}$ with its ordinary Hausdorff circle topology.

[\[lem:t0\]]{#lem:t0 label="lem:t0"} Let $X$ be a nonempty indiscrete space and let $Y$ be a $T_0$ space. Every continuous map $f:X\to Y$ is constant.

Suppose $f(x)\ne f(y)$. Because $Y$ is $T_0$, some open set contains exactly one of $f(x)$ and $f(y)$. Its inverse image is then a nonempty proper open subset of $X$, contradicting $\tau_X=\{\varnothing,X\}$.

The hypothesis on the target is sharp. If $Y$ is a two-point indiscrete space, every set map $X\to Y$ is continuous because the only inverse images that must be checked are $\varnothing$ and $X$. When $X$ has at least two points, nonconstant examples exist. This negative control is important: the proofs below classify maps into named separated targets, not all topological targets.

For a space $X$, let $x\sim_0y$ mean that $x$ and $y$ have the same open neighborhoods. The quotient $X/{\sim_0}$ with the quotient topology is the Kolmogorov quotient $K_0(X)$. The relation, quotient topology, and quotient terminology agree with the standard survey account [@Pirttimaki2021 physical pp. 4--6, 9, and 12--13]. We use $\operatorname{Sep}_{\mathrm H}(X)$ and $\operatorname{Sep}_{\mathrm{CRH}}(X)$ only for the direct universal images verified below, against Hausdorff targets and against completely regular Hausdorff targets. We do not need a general theorem that an arbitrary full subcategory is reflective on every topological space.

The measurable notation is equally explicit. $\mathcal B(X)$ denotes the sigma-algebra generated by the actual topology, and $\mathcal M_{\mathrm{fin}}^+(X)$ denotes positive countably additive finite measures on $(X,\mathcal B(X))$. The basic sigma-algebra and positive-measure conventions are those in Fremlin's inspected results-only development chapter [@FremlinMeasureCh11Dev physical pp. 4--6 of Chapter 11]. No regularity, inner approximation, local finiteness, or completion is built into $\mathcal M_{\mathrm{fin}}^+(X)$.

# Separated and continuous-observable collapse {#sec:continuous}

[\[thm:reflections\]]{#thm:reflections label="thm:reflections"} For each registered actual owner $X$, $$K_0(X)\cong\operatorname{Sep}_{\mathrm H}(X)\cong\operatorname{Sep}_{\mathrm{CRH}}(X)\cong\{*\}.$$ For each of the three target classes, the unique map $q:X\to\{*\}$ has the existence, continuity, and uniqueness property required of the corresponding universal image.

The companion theorem makes each named $X$ nonempty and indiscrete. Every pair of its points has the same two possible open neighborhoods, so $\sim_0$ has one equivalence class and $K_0(X)=\{*\}$. Now let $f:X\to Y$ be continuous with $Y$ $T_0$. By [\[lem:t0\]](#lem:t0){reference-type="ref" reference="lem:t0"}, $f$ is constant. There is therefore exactly one set map $\bar f:\{*\}\to Y$ such that $f=\bar f\circ q$, and every map from a singleton is continuous. This proves the factorization and its uniqueness.

Hausdorff spaces and completely regular Hausdorff spaces are $T_0$, while the singleton belongs to both classes. The same argument gives the two additional direct universal properties. No ambient reflectivity theorem is needed.

The quotient $K_0(\mathsf{ACT\mbox{-}Q}_p)$ in [\[thm:reflections\]](#thm:reflections){reference-type="ref" reference="thm:reflections"} must not be confused with $\mathsf{ACT\mbox{-}Q}_p$ itself. The latter is the already formed, nontrivial time-orbit quotient and remains indiscrete. Applying a Kolmogorov reflection to that object produces a new singleton. Nor is the ordinary circle a candidate for this reflection, since any universal image into a $T_0$ space must be a singleton.

## What the universal property retains

The point of [\[thm:reflections\]](#thm:reflections){reference-type="ref" reference="thm:reflections"} is stronger than the cardinality statement "the quotient has one point." A quotient carrier of cardinality one could be written down without identifying its category or explaining why all admissible maps pass through it. Here the unit $q:X\to\{*\}$ controls every map to each named target class. The factorization is not chosen separately for each point or for each arithmetic coordinate: it is forced, continuous, and unique. This is precisely the information needed later when a proposed observable claims to land in a separated target. Once its domain is one of the actual owners and continuity is established, the map is already in the universal factorization class and cannot retain a within-owner coordinate.

The three reflections happen to share the same carrier and unit on an indiscrete source, but they remain three typed assertions. The $T_0$ universal property quantifies over all $T_0$ targets. The Hausdorff statement quantifies over the smaller class of Hausdorff targets, and the completely regular Hausdorff statement over a smaller class again. Their agreement is a theorem about this source, not permission to identify the three categories or to assume that their reflection functors agree on arbitrary spaces. Direct verification also avoids importing hypotheses from a general reflectivity theorem that are irrelevant to the present owner.

This perspective clarifies what could falsify the result. A nonconstant continuous map from an actual owner to any $T_0$ target would contradict [\[lem:t0\]](#lem:t0){reference-type="ref" reference="lem:t0"} and hence the stated universal property. By contrast, a nonconstant map to an indiscrete target is expected and does not threaten the theorem. Likewise an algebraic set map, an everywhere-defined formula that has not been shown continuous, or a map from a retopologized copy is not an admissible falsifier. Domain, topology, and target separation are part of the quantified statement.

There is no arithmetic information hidden in the singleton. Prime labels, orbit labels, time parameters, and points inside a packet all receive the same image when the reflection is applied to one fixed owner. The conclusion therefore supplies a negative structural prior for separated constructions: any recovery of those coordinates must use additional structure not visible to ordinary separated topology. It does not say that the coordinates were absent from the source set, only that the registered universal passage erases them.

[\[thm:scalar\]]{#thm:scalar label="thm:scalar"} For each registered actual owner $X$, $$C(X)=C_b(X)=\{c1_X:c\in\mathbb C\}$$ as unital $*$-algebras. After this equality is established, the correspondence $c\mapsto c1_X$ is isometric for the supremum norm. If $x,y\in X$, then $\operatorname{ev}_x=\operatorname{ev}_y$ on $C(X)$.

The complex plane is Hausdorff. Thus every continuous $f:X\to\mathbb C$ is constant by [\[lem:t0\]](#lem:t0){reference-type="ref" reference="lem:t0"}, and every constant function is bounded. This proves the algebraic equality before any norm is invoked. Since $X$ is nonempty, $$\lVert c1_X\rVert_\infty=\sup_{x\in X}|c|=|c|.$$ Finally, $f(x)=f(y)$ for every $f\in C(X)$, so the two evaluation homomorphisms coincide. As the actual owners are nontrivial, this also says that $C(X)$ does not separate their points.

The theorem classifies continuous complex-valued functions on the exact actual topology. It is not an application of compact-Hausdorff duality, does not identify a spectrum of a newly constructed $C^*$-algebra, and makes no claim about $C_0$ or compact support on a non-Hausdorff source. Those would require additional definitions and domain checks.

[\[thm:operator\]]{#thm:operator label="thm:operator"} Fix the common Hilbert space $H_0=\ell^2(\mathbb N)$ and the common carrier $B(H_0)$. Every continuous map from any registered actual owner $X$ into $B(H_0)$ is constant when the target is equipped, separately, with the norm topology, the strong operator topology, or the weak operator topology.

The norm topology is Hausdorff. If $A\ne B$, then $(A-B)\xi\ne0$ for some $\xi\in H_0$, so the strong-operator seminorm family separates the difference because $p_\xi(A-B)=\lVert(A-B)\xi\rVert>0$. For the weak operator topology one can additionally choose $\eta$ with $p_{\xi,\eta}(A-B)=|\langle(A-B)\xi,\eta\rangle|>0$. Thus both seminorm families separate points. These standard topologies are defined on the same carrier and have this separation behavior [@HoermannCStar2026 Section 4.1, physical p. 43 / printed p. 39]. Each target is therefore $T_0$, and [\[lem:t0\]](#lem:t0){reference-type="ref" reference="lem:t0"} applies.

The three conclusions are map classifications, not representation theorems. We have not required the maps to preserve products, adjoints, identities, or a group action. No measurable operator field, unbounded operator, operator domain, state, trace, or determinant is constructed. Keeping the carrier fixed also prevents an invalid comparison between topologies living on different operator spaces.

# Measurable and positive-finite-measure collapse {#sec:measure}

A measurable space $(Y,\Sigma_Y)$ is countably separated if a countable family $(E_n)$ in $\Sigma_Y$ distinguishes every two points. This is the target-side property used below; standard Borel spaces are countably separated under the usual definition [@Preston2008 physical p. 3 and Section 3, physical p. 13]. Cardinality alone is not a substitute for the measurable separation hypothesis.

[\[thm:borel\]]{#thm:borel label="thm:borel"} For every registered actual owner $X$, $$\mathcal B(X)=\{\varnothing,X\}.$$ Every measurable map from $(X,\mathcal B(X))$ to a countably separated measurable space is constant. Since $X$ is nontrivial, its own measurable space is neither countably separated nor standard Borel.

The indiscrete topology $\{\varnothing,X\}$ is already a sigma-algebra, so it equals the generated Borel algebra. Let $f:X\to Y$ be measurable and let $(E_n)$ be a countable separating family in $Y$. For every $n$, the inverse image $f^{-1}(E_n)$ is either $\varnothing$ or $X$. Consequently any two values in the image of $f$ have identical membership in every $E_n$. Separation forces those values to be equal, so $f$ is constant.

If $x\ne y$ in $X$, neither of the only two measurable sets distinguishes them. Thus no measurable family, countable or otherwise, separates the two points. The source is not countably separated and hence cannot be standard Borel.

This result includes a sharp target boundary. A two-point space with the trivial sigma-algebra is not countably separated, and every set map from $(X,\mathcal B(X))$ into it is measurable. Thus nonconstant measurable maps reappear as soon as target separation is removed. Paper 9 already records the immediate trivial-Borel and constant-$T_0$ consequences of its indiscreteness theorem; the new content here is their placement in the full separated, measurable, measure, group, operator, and copied-component classification.

[\[thm:mfin\]]{#thm:mfin label="thm:mfin"} For every registered actual owner $X$, total mass is a cone bijection $$\mathcal M_{\mathrm{fin}}^+(X)\longrightarrow[0,\infty),\qquad \mu\longmapsto\mu(X).$$ The inverse sends $m\ge0$ to the measure $\mu_m$ defined by $$\mu_m(\varnothing)=0,\qquad \mu_m(X)=m.$$ All Dirac measures $\delta_x$, $x\in X$, coincide with $\mu_1$.

A measure on $\mathcal B(X)=\{\varnothing,X\}$ is determined by its value on $X$, and positivity and finiteness require that value to lie in $[0,\infty)$. Conversely the two displayed values satisfy positive countable additivity. These assignments are inverse and preserve addition and nonnegative scalar multiplication.

For a measurable event $A$, define $\delta_x(A)=1$ if $x\in A$ and $0$ otherwise. The only choices are $A=\varnothing$ and $A=X$, so the value is independent of $x$. Every $\delta_x$ is the unique mass-one measure $\mu_1$.

The last statement must not be paraphrased as a calculation of mass on a singleton. Since $X$ is nontrivial, a proper singleton $\{x\}$ is not Borel, and $\delta_x(\{x\})$ is outside the measurable domain. We make no support claim. We also attach no regularity adjective to $\mathcal M_{\mathrm{fin}}^+(X)$. Radon terminology varies with ambient hypotheses and convention, and the present theorem deliberately stops at positive countably additive finite measures on the exact two-set Borel algebra. It gives no Haar measure, invariant probability, state, trace, disintegration, signed measure, or complex measure.

There is also no topology-selected nonzero mass. The parameter $m$ is arbitrary, including $m=0$. Normalizing to mass one would be an additional choice, not a consequence of the topology. This observation becomes more consequential for the copied coproduct, where an entire summable mass vector remains free.

## Compatibility of the measurable and continuous ledgers

The scalar and measure results describe different functors, yet they agree on the amount of actual point information retained. Every continuous scalar observable is a constant $c1_X$. Its integral against $\mu_m$ is $$\int_X c1_X\,d\mu_m=cm.$$ Thus the pairing depends only on the scalar constant and total mass. This formula is not a newly selected state or trace: both inputs remain free, and no normalization fixes $m=1$. It merely verifies that the continuous-function and positive-finite-measure classifications are mutually typed.

The agreement of Dirac measures has the same interpretation. For every continuous $f$, one has $\int f\,d\delta_x=f(x)=c$, independently of $x$. Equality of these integrals is not being used to infer equality of measures; the measures were first classified directly on the exact Borel algebra. Conversely, the proof never tries to distinguish points by integrating a nonmeasurable singleton indicator. That would silently replace the actual two-set Borel algebra with a coordinate sigma-algebra.

Countable separation on the target also cannot be shifted to the source. The source is explicitly not countably separated, while the theorem about measurable maps assumes that the target is. If one instead imposed a richer sigma-algebra on the same underlying set, the map and measure classifications could change. Such a choice would define a new measurable owner and would require a new theorem connecting it to the source construction. The present conclusions are exact for $\mathcal B(X)$ generated by the actual topology and no other sigma-algebra.

# Transported group law and the circle direction {#sec:group}

The set bijection $\phi_p:|\mathsf{ACT\mbox{-}Q}_p|\to U_p/H_p$ is frozen before any topology is discussed. Transport the algebraic quotient-group structure by defining $$x*_py=\phi_p^{-1}\!\bigl(\phi_p(x)\phi_p(y)\bigr),\qquad
 e_p=\phi_p^{-1}(H_p),\qquad
 x^{-*}=\phi_p^{-1}\!\bigl(\phi_p(x)^{-1}\bigr).$$ These are definitions on the actual carrier. They do not declare $\phi_p$ continuous and do not place a natural or profinite quotient topology on $\mathsf{ACT\mbox{-}Q}_p$.

[\[thm:characters\]]{#thm:characters label="thm:characters"} The operations above make $\mathsf{ACT\mbox{-}Q}_p$ a commutative topological group when "topological group" does not include Hausdorffness by definition. Its continuous character group into the ordinary circle is trivial: $$\operatorname{Hom}_{\mathrm{cont}}((\mathsf{ACT\mbox{-}Q}_p,*_p),\mathbb T)=\{1\}.$$

The group axioms and commutativity hold because $\phi_p$ transports them from the quotient group $U_p/H_p$. A finite product of nonempty indiscrete spaces is indiscrete: the product-basis rectangles have only empty or whole factors. Therefore every map $\mathsf{ACT\mbox{-}Q}_p\times\mathsf{ACT\mbox{-}Q}_p\to\mathsf{ACT\mbox{-}Q}_p$ is continuous because the codomain is indiscrete. In particular multiplication is continuous. The same codomain observation makes inversion continuous.

The ordinary circle $\mathbb T$ is Hausdorff. Any continuous character $\chi:\mathsf{ACT\mbox{-}Q}_p\to\mathbb T$ is constant by [\[lem:t0\]](#lem:t0){reference-type="ref" reference="lem:t0"}. If its constant value is $z$, the homomorphism identity gives $z=z^2$, and $z\in\mathbb T$ implies $z=1$. Thus only the trivial character remains.

The theorem is narrower than an abstract duality statement. Algebraic characters of the underlying group may be nontrivial, and a different topology on the same set may make other characters continuous. We have not shown that the transported law appears canonically in Deninger's construction. Its purpose is to answer one registered question: once the specific law is transported to the already fixed actual carrier, is it continuous, and which ordinary-circle characters are continuous for that actual topology?

Now fix $a\in U_p/H_p$ and a basepoint on its inherited orbit. The stabilizer $p^{\mathbb Z}$ gives a set parametrization by $\mathbb R_{>0}/p^{\mathbb Z}$, hence a basepoint-dependent bijection $$\beta_{p,a}:|\mathsf{ACT\mbox{-}ORBIT}_{p,a}|\longrightarrow|\mathsf{STD\mbox{-}CIRCLE}_p|.$$ The codomain receives the ordinary Hausdorff circle topology; the domain retains the actual inherited indiscrete topology.

[\[thm:circle\]]{#thm:circle label="thm:circle"} The map $\beta_{p,a}:\mathsf{ACT\mbox{-}ORBIT}_{p,a}\to\mathsf{STD\mbox{-}CIRCLE}_p$ is not continuous, whereas $$\beta_{p,a}^{-1}:\mathsf{STD\mbox{-}CIRCLE}_p\longrightarrow\mathsf{ACT\mbox{-}ORBIT}_{p,a}$$ is continuous. Under the underlying-set identification, the standard-circle topology is strictly finer than the actual topology. The standard circle is neither a continuous factor nor a $T_0$, Hausdorff, or completely regular Hausdorff reflection of the actual orbit.

Both sets are nontrivial and $\beta_{p,a}$ is a bijection, so it is nonconstant. A continuous map from the indiscrete domain to the $T_0$ circle would be constant by [\[lem:t0\]](#lem:t0){reference-type="ref" reference="lem:t0"}. Hence $\beta_{p,a}$ is not continuous. Every map into an indiscrete space is continuous, so its inverse is continuous. The two topologies cannot agree, and the circle topology is finer because the identity from the finer circle to the coarser actual topology is continuous. Finally, every continuous map from the actual orbit to a $T_0$ space is constant, ruling out a nontrivial circle factor; [\[thm:reflections\]](#thm:reflections){reference-type="ref" reference="thm:reflections"} identifies the relevant reflections as singletons.

This direction check prevents a common category error. A set/action parametrization may remain useful on the proxy, including its clock $\log p$, without becoming a homeomorphism for the actual inherited topology. Conversely, the continuity of $\beta^{-1}_{p,a}$ does not give the proxy any source-canonical status. It only records that an imposed finer topology maps continuously to the coarser indiscrete one.

# Tagged copied components {#sec:coproduct}

Let $I$ be a nonempty countable set. For each $i\in I$, let $X_i$ be a nonempty indiscrete space, and form the tagged coproduct $$X_I=\coprod_{i\in I}(\{i\}\times X_i)$$ with the topological coproduct structure. The tagged carrier and componentwise definition of the coproduct topology are standard [@StacksCoproduct0B1W Section 5.29 opening, Tag 0B1W]. For $S\subseteq I$, write $$X_S=\coprod_{i\in S}(\{i\}\times X_i).$$ The theorem below is abstract; only afterward do we specialize to copied prime packets.

[\[thm:coproduct\]]{#thm:coproduct label="thm:coproduct"} The topology and Borel algebra of $X_I$ are both $$\tau(X_I)=\mathcal B(X_I)=\{X_S:S\subseteq I\}.$$ Two points are topologically indistinguishable exactly when they have the same label. The label projection $$q_I:X_I\to I,\qquad (i,x)\mapsto i,$$ is the Kolmogorov-reflection unit onto $I$ with the discrete topology. For every $T_0$ space $Y$, composition with $q_I$ gives a natural bijection $$\operatorname{Cont}(X_I,Y)\cong\operatorname{Map}(I,Y).$$ Moreover total component masses give a cone bijection $$\mathcal M_{\mathrm{fin}}^+(X_I)\cong\ell^1_+(I).$$ Explicitly, if $m_i=\mu(X_{\{i\}})$, then $$\mu(X_S)=\sum_{i\in S}m_i,\qquad
 \sum_{i\in I}m_i=\mu(X_I)<\infty.$$

A subset of a topological coproduct is open exactly when its intersection with every component is open in that component. Each such intersection is either empty or the whole component, so every open subset is $X_S$ for a unique $S\subseteq I$. Conversely each $X_S$ has the required componentwise intersections and is open. Complements and countable unions correspond to complements and countable unions of label subsets. Thus the topology is already a sigma-algebra and equals the Borel algebra.

Two points with the same label meet exactly the same component-union opens. Points with different labels are separated by either of their clopen components. The indistinguishability classes are therefore the components, and $q_I$ is the set quotient. For every $S\subseteq I$, $q_I^{-1}(S)=X_S$ is open, so the quotient topology on $I$ is discrete.

If $f:X_I\to Y$ is continuous with $Y$ $T_0$, its restriction to each indiscrete component is constant by [\[lem:t0\]](#lem:t0){reference-type="ref" reference="lem:t0"}. Define $\bar f(i)$ to be that constant value. Then $f=\bar f\circ q_I$, and uniqueness is forced by surjectivity of $q_I$. Since $I$ is discrete, every map $\bar f:I\to Y$ is continuous, proving the stated bijection and the direct universal property.

For $\mu\in\mathcal M_{\mathrm{fin}}^+(X_I)$, countable additivity over disjoint clopen components gives the displayed formula. Finiteness gives $(m_i)\in\ell^1_+(I)$. Conversely any nonnegative summable family defines a positive finite measure on every Borel event $X_S$ by the same series. Nonnegative series are countably additive over disjoint subsets, so the construction is valid and inverse to the component-mass map.

The theorem includes zero masses. Point Dirac measures within a fixed component coincide because the component has only empty and whole-component events. Dirac measures in different components are distinguished by their clopen components. Thus the measurable interface retains label-level information and erases within-component coordinates. It does not choose a nonzero measure: on a bare countably infinite discrete label set, a finite measure invariant under every permutation must assign equal mass to all labels, hence must be zero.

[\[cor:primek0\]]{#cor:primek0 label="cor:primek0"} Let $$\mathsf{COPROD\mbox{-}PACKETS}
   =\coprod_{p\in\mathbb P}(\{p\}\times\mathsf{ACT\mbox{-}PACKET}_p)$$ be the explicitly tagged coproduct of copied actual packets. Then $$K_0(\mathsf{COPROD\mbox{-}PACKETS})\cong\mathbb P_{\mathrm{disc}}.$$ Every continuous map from this copied object to a $T_0$ target is exactly a prime-indexed family of target values, constant inside each copied packet.

Apply [\[thm:coproduct\]](#thm:coproduct){reference-type="ref" reference="thm:coproduct"} with $I=\mathbb P$ and $X_p=\mathsf{ACT\mbox{-}PACKET}_p$.

[\[cor:primemass\]]{#cor:primemass label="cor:primemass"} Positive finite Borel measures on the copied-prime object are in bijection with $\ell^1_+(\mathbb P)$. No nonzero vector is selected by the topology. Replacing $\mathbb P$ by the composite integers or by any nonempty countable label set gives the same abstract topological, continuous-map, Borel, and measure classification.

On $\mathbb P_{\mathrm{disc}}$, the externally supplied function $\lambda(p)=\log p$ is continuous but belongs to neither $C_b(\mathbb P_{\mathrm{disc}})$ nor $C_0(\mathbb P_{\mathrm{disc}})$.

The measure and label-neutrality statements are direct specializations of [\[thm:coproduct\]](#thm:coproduct){reference-type="ref" reference="thm:coproduct"}. Every function on a discrete space is continuous. The primes are unbounded, so $\log p$ is unbounded and not in $C_b$. It also fails to vanish at infinity: for any fixed positive threshold, infinitely many primes have logarithm above that threshold. Hence it is not in $C_0$ for the discrete locally compact topology.

The label function is external arithmetic data. It is not selected by the copied topology or by the cone $\ell^1_+$. In this owner it is not a proven return time, primitive-orbit weight, multiplicity, stability factor, phase, trace coefficient, or Route-A $A1$ datum. Nor does the copied object describe the topology inherited by a global rational-Witt or Deninger suspension. It is an explicit control model that isolates what tagged assembly alone can retain.

## Label neutrality and the global boundary

The coproduct theorem is insensitive to the internal cardinality and algebra of the components. It uses only nonemptiness, indiscreteness, and the declared tagged coproduct topology. Replacing a component by another nonempty indiscrete space leaves its one indistinguishability class unchanged. Reindexing by a bijection of label sets merely relabels the discrete quotient and the coordinates of $\ell^1_+$. These invariances explain why the construction cannot distinguish primes from composites without reading the tags that were supplied at the outset.

The same fact gives a useful arbitrary-label control. Let $I=\mathbb N$, let $I$ be the composite integers, or let $I$ be a countable set of uninterpreted symbols. In all cases, opens and Borel events are precisely component unions, $K_0(X_I)=I_{\mathrm{disc}}$, and finite positive measures are summable mass families. Calling the labels primes changes their external interpretation but not a single step of the proof. Therefore primality receives no intrinsic topological certificate from this model.

Nor is there a canonical mass vector. Any element of $\ell^1_+(I)$, including vectors with zero coordinates, defines a valid positive finite measure without changing the topology. A proposal that inserts a preferred vector must state the additional selection rule and justify its arithmetic or dynamical origin. Permutation invariance on a bare countably infinite label set selects only the zero finite measure, so symmetry alone cannot supply a nonzero weighting. In particular, the nonsummable family $m_p=1$ and the unbounded family $m_p=\log p$ are not members of $\ell^1_+(\mathbb P)$.

The external function $p\mapsto\log p$ and a component mass family also have different types. The former is a scalar function on the discrete quotient, while the latter specifies a positive finite measure. Multiplying or pairing them requires a separate summability domain. No such pairing is promoted here to a trace or orbit formula. This blocks a tempting but invalid splice in which the copied label, a proxy clock, and an arbitrary mass are treated as if one source construction had selected all three.

Finally, a coproduct topology is a modeling decision. A global source may glue components, create specializations between them, or use a carrier that is not their set-theoretic disjoint union. Without an explicit continuous comparison in both directions, the copied coproduct cannot be called a subspace, quotient, reflection, or decomposition of that global object. P10-7 and P10-8 therefore provide controls for tagged assembly, not a theorem about global rational-Witt topology.

# Deterministic controls and Route consequences {#sec:controls}

The deterministic package checks finite presentations of the registered logical interfaces. From the Paper-10 project directory, the entry point is

`./experiments/reproduce.sh`.

The final run passed 24 of 24 tests. Ten CSV artifacts contain 676 data rows in total. Verify-only validation passed, and two fresh generations were byte-identical. The implementation uses the Python standard library, makes no network request, uses no randomness, and contains no target zero data. The exact manifest SHA-256 is

.

The controls enumerate continuous maps between small finite topologies, measurable maps to separated and nonseparated targets, equality of finite Dirac ledgers, finite-group character checks, the two proxy directions, component-union opens, component-mass vectors with zeros, finite-prefix summability gates, and prime/composite/arbitrary label replacements. These are regression oracles for definitions and code. They do not prove an infinite-product theorem, the actual arithmetic indiscreteness input, the full $\ell^1$ classification, unboundedness of $\log p$, or a universal property. Those conclusions rest on the proofs above.

## Same-object certificate

The same-object gate keeps seven owners distinct. For actual fixed-prime owners, identity, inherited topology, and the tested separated/observable interface pass, but no closed-orbit package, invariant measure selection, trace, determinant, or arithmetic promotion follows. The standard circle passes its own proxy topology and ordinary continuous functions but fails actual-owner identity. The copied owner passes only the explicitly declared coproduct topology, discrete reflection, and component-mass interface. It has no source-global identity.

The frozen roadmap defines $A0$ as arithmetic relevance, $A1$ as primitive periodic or closed orbits, $A2$ as a dynamical-zeta or Fredholm-determinant realization, $A3$ as analytic structure and Weil-compression compatibility, and $A4$ as a natural quantization or operator lift. Same-object identity and prerequisites are separate evidence gates used before those Route coordinates are credited. Each Route record also contains nine validation fields used to audit its $A2$ verdict; those fields are not the definition of $A2$. The five actual or comparison owners have only a weak arithmetic relation at $A0$, while both copied controls fail $A0$. Every owner fails $A1$, $A2$, $A3$, and $A4$. This is a typed negative result, not permission to combine a prime label from one record, a circle character from another, and a historical scalar ledger from a third.

P0.30P0.19P0.15P0.25

\
Owner record & $A0$ & $A1$--$A4$ & Overall\
Owner record & $A0$ & $A1$--$A4$ & Overall\
Actual separated reflection & & all fail & [Route\_A\_Exploratory]{.smallcaps}\
Actual continuous observables & & all fail & [Route\_A\_Exploratory]{.smallcaps}\
Actual Borel/finite measure & & all fail & [Route\_A\_Exploratory]{.smallcaps}\
$\mathsf{ACT\mbox{-}Q}_p$ continuous characters & & all fail & [Route\_A\_Exploratory]{.smallcaps}\
Actual-orbit/circle comparison & & all fail & [Route\_A\_Exploratory]{.smallcaps}\
Copied-prime $K_0$ control & & all fail & [Route\_A\_Rejected]{.smallcaps}\
Copied-prime finite-measure control & & all fail & [Route\_A\_Rejected]{.smallcaps}\

The seven exact YAML records are stored under `evaluations/route_a/` with the date suffix `2026-08-14-stage10.yaml`. Their formal audit reports schema and enum validity, exactly nine $A2$ metrics per record, resolvable artifact paths, and no Stage-10 Route-B YAML. The Route audit SHA-256 is

.

Route adjudication is an evaluation of already proved, owner-typed results. It is not additional mathematical evidence.

## Interpretation of the negative Route result

The five exploratory verdicts should not be read as partially completed determinant or quantization constructions. Their $A0$ coordinate records a weak arithmetic relation because the owners descend from a fixed prime packet or compare directly with one. The remaining coordinates fail: no primitive closed-orbit package is supplied at $A1$, no dynamical zeta or Fredholm determinant is realized at $A2$, no analytic continuation or Weil-compression compatibility is established at $A3$, and no natural operator lift is constructed at $A4$. "Exploratory" preserves the arithmetic provenance while recording that the route has not crossed its structural gates.

The two copied controls are rejected more strongly. Their prime labels are inserted by the model, and the label-neutrality theorem shows that the same construction works for composites or arbitrary symbols. This is insufficient even for arithmetic relevance at $A0$ under the rubric. The rejection does not invalidate the coproduct theorems. It separates an exact mathematical classification from its inability to advance the proposed arithmetic spectral route.

The nine validation fields stored under each $A2$ record are a consistency device. They ask whether the same declared owner has the needed dynamical ingredients and whether the corresponding evidence paths resolve. A row of failing fields supports the $A2$ verdict, but it does not redefine $A2$ as a generic checklist or numerical score. The coordinate remains the concrete dynamical-zeta or Fredholm-determinant gate in the roadmap.

No Route-B evaluation is generated because the roadmap reserves Route B for a strong candidate with a coherent classical-to-quantum continuation. The present owners do not pass the earlier Route-A gates. Invoking Route B would therefore not be a deeper test of the same construction; it would attempt to bypass the missing classical and analytic structure. The exact result is the recorded negative prior: ordinary separated interfaces erase within-owner information, while copied labels retain only information explicitly inserted by the model.

# Limitations, integrity boundaries, and conclusion {#sec:limits}

The first limitation is inherited scope. Paper 10 assumes, rather than reproves, the companion theorem for each fixed rational prime and its finite-kernel actual packet, inherited orbit, and time-orbit quotient. Nothing here classifies the full global suspension. The tagged coproduct is declared by hand and cannot fill that gap.

Second, the target separation hypotheses are substantive. Non-$T_0$ topological targets and non-countably-separated measurable targets admit nonconstant maps from an indiscrete source. The results therefore do not say that all observables of every possible type collapse. They classify the named separated topological, scalar, fixed bounded-operator, and separated measurable interfaces.

Third, the measure theorem concerns positive countably additive finite measures on the topology-generated Borel algebra. It does not establish regularity, Radon properties under any convention, local finiteness beyond global finiteness, invariance, Haar theory, probability selection, states, traces, supports, signed measures, complex measures, or disintegration. All Dirac measures coincide as functions on measurable events even though proper singletons are nonmeasurable.

Fourth, transporting the quotient-group law through $\phi_p$ produces a mathematically well-defined topological group on the actual carrier, but does not prove that Deninger's source canonically chose that law. The continuous-character theorem does not classify abstract characters or characters for another topology. The fixed-operator result classifies arbitrary continuous maps to three named topologies on $B(\ell^2(\mathbb N))$; it does not construct a representation or address unbounded operators.

Fifth, the ordinary circle is a proxy. Its topology is strictly finer than the actual inherited orbit topology, and the actual-to-circle direction is not continuous. Standard-circle calculations can remain internally valid on that explicit owner, but they cannot be credited to the actual orbit without a new continuous comparison theorem. Similarly, the copied label set retains primes because the construction tagged components by primes. It provides no intrinsic primality test or weight selection.

Finally, this paper proves no determinant formula, analytic continuation, functional equation, zero matching, quantization, Hilbert--Pólya operator, or Route-B mechanism. The separated and observable collapses are exact negative structural priors. They show what ordinary separated interfaces erase and thereby identify where a future construction would have to add genuinely non-$T_0$, sheaf-theoretic, locale-theoretic, stack-like, or otherwise nonclassical structure. The sharp next question is whether such an interface can be defined canonically on the actual rational-Witt owner and retain nonconstant information without importing a proxy topology.

In conclusion, the three actual fixed-prime owners collapse to a singleton under every registered separated reflection, to constants under continuous scalar and fixed-operator observation, and to total mass under positive finite Borel measurement. The transported actual quotient group has only the trivial continuous circle character. The standard circle points in the continuous direction back to the actual orbit, not conversely. A tagged copied coproduct recovers discrete labels and arbitrary summable component masses, while retaining no within-component coordinates and selecting no arithmetic weight. These conclusions close the registered P10 interfaces without conflating actual, proxy, copied, or historical owners.

# Data and code availability {#data-and-code-availability .unnumbered}

The manuscript, native TikZ sources, deterministic-control code, ten CSV artifacts, and machine-readable manifest are contained in the Paper-10 project directory. The reproducibility command is `./experiments/reproduce.sh`; the final controls-manifest SHA-256 is stated in [7](#sec:controls){reference-type="ref" reference="sec:controls"}. The controls contain synthetic finite witnesses only and no target zero data. No external archive or DOI is asserted. Twelve third-party source PDFs are retained locally for verification and are excluded from the public synchronization payload; only manifests, checksum ledgers, preflight sidecars, canonical endpoints, locators, and hashes may be synchronized. The companion Paper-9 PDF is identified by its exact SHA-256 in the bibliography. An immutable public artifact URL for that companion manuscript remains a release-confirmation item before journal submission.

# Ethics statement {#ethics-statement .unnumbered}

This theoretical and deterministic-control study involved no human participants, animals, personal data, or clinical intervention. Human-subject consent and animal ethics approval are therefore not applicable.

# Author contributions {#author-contributions .unnumbered}

Provisional CRediT statement: Liang Wang---conceptualization, methodology, formal analysis, software, validation, visualization, writing (original draft), and writing (review and editing). The human author must confirm this statement before submission; repository inclusion is not that confirmation.

# Funding, competing interests, and acknowledgments {#funding-competing-interests-and-acknowledgments .unnumbered}

Funding statement: **AUTHOR TO CONFIRM**; no funding claim is inferred from the project record. Competing-interest statement: **AUTHOR TO CONFIRM**; no declaration is made on the author's behalf. Acknowledgments: **AUTHOR TO CONFIRM**. Affiliation wording, target venue, citation style, license, repository/archive release, and final journal-facing declarations likewise require human confirmation.

# AI-assistance disclosure {#ai-assistance-disclosure .unnumbered}

AI-assisted tools were used for structured literature search support, proof-domain checking, deterministic-control generation and review, Route-record checking, and manuscript drafting. Exact source manifestations, theorem domains, hashes, code outputs, and citation locators were checked against the frozen project artifacts. No target zero data, parameter fitting, random search, or external-model upload was used. The human author retains responsibility for every claim, citation, disclosure, and release decision and must confirm the final venue-specific wording before submission.

# Exact evidence ledger {#app:ledger}

The manuscript conclusions are bound to the immutable project artifacts in [\[tab:hashes\]](#tab:hashes){reference-type="ref" reference="tab:hashes"}. These hashes are provenance records, not scholarly citations and not substitutes for the proofs in this paper.

P0.46P0.47

\
Artifact & SHA-256\
Artifact & SHA-256\
&\
&\
&\
&\
&\
&\
&\
&\
&\
&\
&\
&\
&\
&\
&\
