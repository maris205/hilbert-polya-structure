---
p1_kind: "derived-fulltext-reading-copy"
route: "flow_systems"
logical_paper_id: "flow_systems--22-fppf-verschiebung-lifts"
canonical_tex: "flow_systems/papers/22-fppf-verschiebung-lifts/stage5_finalization/manuscript.tex"
canonical_pdf: "flow_systems/papers/22-fppf-verschiebung-lifts/stage5_finalization/paper.pdf"
source_sha256: "e90dd88109d4e53d1f789808286c15cc917003cd38b69f49ddaff8661b9158ed"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Descent Obstruction to Verschiebung Lifts on fppf and Finite-Flat Sites

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../flow_systems/papers/22-fppf-verschiebung-lifts>)
- [规范 TeX](<../../../../../flow_systems/papers/22-fppf-verschiebung-lifts/stage5_finalization/manuscript.tex>)
- [关联 PDF](<../../../../../flow_systems/papers/22-fppf-verschiebung-lifts/stage5_finalization/paper.pdf>)
- [支撑 Markdown](<../../../../../flow_systems/papers/22-fppf-verschiebung-lifts/README.md>)
- [BibTeX](<../../../../../flow_systems/papers/22-fppf-verschiebung-lifts/stage5_finalization/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Let $\omega\colon\mathcal Z\twoheadrightarrow\mathcal W$ be the epimorphism from the sheafified reduced monoid algebra to the rational big-Witt sheaf on a universe-small absolute site of noetherian affine schemes. We prove that, for every integer $N>1$, the additive Verschiebung $V_N(f)(T)=f(T^N)$ admits no additive sheaf lift through $\omega$, for either the fppf topology or the finite-flat topology. The obstruction is explicit. After writing $N=q^a d$ and passing from $k[x]$ to the finite-free root cover $k[s]$, $x=s^N$, injectivity over the Dedekind domain $k[s]$ forces a unique local preimage. Its two pullbacks disagree on the double overlap; specialization to $k[\varepsilon]/(\varepsilon^N)$ detects a nonzero kernel section. Consequently, for the extension $$0\longrightarrow\mathcal K\longrightarrow\mathcal Z
   \xrightarrow{\omega}\mathcal W\longrightarrow0,$$ one has $u_*e\ne V_N^*e$ for every endomorphism $u\colon\mathcal K\to\mathcal K$. The same example shows that the sectionwise Dedekind-ring assertion in Corollary 4.6 of Deninger's version-1 preprint, read literally, requires correction: sheaf epimorphy gives local rather than objectwise surjectivity. This answers the cited lifting question at every nontrivial index.
author:
- |
  Liang Wang^1^\
  ^1^School of Artificial Intelligence and Automation,\
  Huazhong University of Science and Technology,\
  Luoyu Road 1037, 430070, Hubei, P.R. China\
  Contact: `wangliang.f@gmail.com`
bibliography:
- references.bib
date: Draft of 25 August 2026
title: |
  **A Descent Obstruction to Verschiebung Lifts\
  on fppf and Finite-Flat Sites**
```

## Markdown 正文

中文摘要。设 $\omega\colon\mathcal Z\twoheadrightarrow\mathcal W$ 为诺特仿射概形绝对小站点上的层满态射，\
其定义域来自约化幺半群代数的层化，值域为有理大 Witt 层。\
本文证明：对每个整数 $N>1$，加法 Verschiebung $V_N(f)(T)=f(T^N)$ 在 fppf 拓扑和有限平坦拓扑上，\
都不能通过 $\omega$ 提升为 $\mathcal Z$ 的加法层自同态。\
证明给出显式下降障碍。写 $N=q^a d$，在有限自由根覆盖 $k[x]\to k[s]$、$x\mapsto s^N$ 上，\
Dedekind 整环 $k[s]$ 处的单射性迫使局部原像唯一； 其在双重交叠上的两个拉回并不相等。\
把交叠特化到 $k[\varepsilon]/(\varepsilon^N)$， 可检测到一个非零核截面。\
由此，对扩张类 $e$ 及任意 $u\colon\mathcal K\to\mathcal K$，均有 $u_*e\ne V_N^*e$。\
同一例子也说明 Deninger 预印本第一版推论 的逐截面 Dedekind 环断言按字面理解时需要修正：\
层的满态射只保证局部满射，并不保证每个对象上的截面满射。

**Keywords.** rational Witt vectors; Verschiebung; fppf descent; finite-flat topology; extensions of sheaves; reduced monoid algebra.

**MSC 2020 (provisional).** 13F35; 14F20; 18G15.

# Introduction and main results

The rational big-Witt functor admits a concrete presentation in terms of formal differences of elements of a multiplicative monoid. Deninger recently studied the sheaf-theoretic form of this presentation, constructed lifts of the big-Witt Frobenius operations, and asked whether the Verschiebung operations can likewise be lifted to the sheafified reduced monoid algebra [@Deninger2025Rational p. 25]. The question is deceptively close to an elementary factorization problem. Locally, the expression $1-xT^N$ can be split after adjoining an $N$-th root of $x$. Globally, however, the chosen factors must satisfy descent on the double overlap. We show that the local factorization forced by injectivity never satisfies this condition when $N>1$.

We work on a universe-small version $\mathscr C$ of the absolute category of noetherian affine schemes used in [@Deninger2025Rational Secs. 3--4]. It is equipped first with the fppf topology. The chosen universe is understood to contain all affine schemes and fiber products occurring in the proof. This formulation avoids treating an arbitrary skeleton as though it were automatically closed under the required base changes. Write $$\mathcal Z=\underline{\mathbb Z}(\mathcal O)^\sharp,\qquad
 \mathcal W=W_{\mathrm{rat}}(\mathcal O),\qquad
 \omega\colon\mathcal Z\twoheadrightarrow\mathcal W.$$ Here $\underline{\mathbb Z}(A)$ is the reduced integral monoid algebra of the multiplicative monoid of $A$, and the superscript ${}^\sharp$ denotes abelian sheafification. Deninger's Theorem 3.4 states that the rational Witt presheaf is already an fpqc sheaf on this noetherian-affine owner [@Deninger2025Rational Thm. 3.4, p. 19]; Proposition 4.3 gives the displayed epimorphism of sheaves [@Deninger2025Rational Prop. 4.3, p. 21].

For $N\geq1$, the additive big-Witt Verschiebung is $$V_N\colon\mathcal W\longrightarrow\mathcal W,\qquad
 V_N(f)(T)=f(T^N).$$ The word *additive* refers to the Witt addition, represented by multiplication of power series. Our principal result is the following.

[\[thm:fppf\]]{#thm:fppf label="thm:fppf"} For every integer $N>1$, there is no morphism of abelian sheaves $\widetilde V_N\colon\mathcal Z\to\mathcal Z$ satisfying $$\omega\circ\widetilde V_N=V_N\circ\omega$$ on $\mathscr C_{\mathrm{fppf}}$. For $N=1$, the identity morphism is a lift.

The topology called finite-flat in [@Deninger2025Rational Sec. 4] is distinct from the fppf topology. Here a finite-flat covering family of an affine scheme $U$ means a jointly surjective family $\{U_i\to U\}$ in which every morphism is finite and flat; on affines, the corresponding ring maps are finite locally free and their spectra jointly cover $U$. We use the associated subcanonical topology, so representable presheaves, and in particular the structure sheaf used below, satisfy descent. We therefore state the finite-flat conclusion separately rather than deriving it formally from Theorem [\[thm:fppf\]](#thm:fppf){reference-type="ref" reference="thm:fppf"}.

[\[thm:ff\]]{#thm:ff label="thm:ff"} On the same universe-small noetherian-affine category equipped with the finite-flat topology, no additive lift of $V_N$ through $\omega$ exists for any $N>1$.

Both theorems are proved by one finite-free root cover, but each use of injectivity and each sheaf-theoretic detector is checked for the topology in question. Choose a prime $q\mid N$, write $N=q^a d$ with $(q,d)=1$, and take a finite field $k$ of characteristic $q$ containing all $d$-th roots of unity. Over $$A=k[x]\longrightarrow B=k[s],\qquad x\longmapsto s^N,$$ the image of any hypothetical lift at the generator $x$ is forced to restrict to $$c(s)=q^a\sum_{\zeta\in\mu_d(k)}(\zeta s)\in\underline{\mathbb Z}(B).$$ On $B\otimes_A B$, the two pullbacks of $c(s)$ differ. The specialization $s_1\mapsto\varepsilon,\ s_2\mapsto0$ to $k[\varepsilon]/(\varepsilon^N)$ turns the difference into a nonzero section. Thus the obstruction is an explicit failed descent condition, not a dimension count or a formal appeal to an uncomputed cohomology group.

There is also a useful extension-theoretic formulation. For $\tau\in\{\mathrm{fppf},\mathrm{ff}\}$, regard $\omega\colon\mathcal Z\to\mathcal W$ as a morphism in $\mathrm{Ab}(\mathscr C_\tau)$, put $\mathcal K_\tau=\ker(\omega)$, and let $$e_\tau:\quad 0\longrightarrow\mathcal K_\tau\longrightarrow\mathcal Z
 \xrightarrow{\omega}\mathcal W\longrightarrow0
 \tag{1.1}\label{eq:extension}$$ denote its class in $\operatorname{Ext}^1_{\mathrm{Ab}(\mathscr C_\tau)}(\mathcal W,\mathcal K_\tau)$. When one topology is fixed below, the unadorned symbols $\mathcal K$ and $e$ abbreviate $\mathcal K_\tau$ and $e_\tau$, respectively. Standard pushout--pullback functoriality then gives the following consequence.

[\[cor:ext\]]{#cor:ext label="cor:ext"} For $\tau\in\{\mathrm{fppf},\mathrm{ff}\}$, $N>1$, and every endomorphism $u\colon\mathcal K_\tau\to\mathcal K_\tau$ in $\mathrm{Ab}(\mathscr C_\tau)$, $$u_*e_\tau\ne V_N^*e_\tau
 \qquad\text{in }
 \operatorname{Ext}^1_{\mathrm{Ab}(\mathscr C_\tau)}(\mathcal W,\mathcal K_\tau).$$ In particular, $e_\tau\ne0$ and $V_N^*e_\tau\ne0$ for both values of $\tau$.

The proof also isolates a distinction relevant to a statement in the source. Corollary 4.6 of [@Deninger2025Rational p. 23], in its version-1 formulation, asserts a sectionwise identification over Dedekind rings for the finite-flat site. For $A=k[x]$, the rational Witt section $1-xT^N$ in our construction is locally in the image of $\omega$ but has no global preimage. Read in this sectionwise sense, that assertion therefore requires correction. The issue is the passage from an epimorphism of sheaves to surjectivity on the sections of a fixed object. Proposition 4.3 remains the needed local surjectivity statement, and Proposition 4.5 remains compatible with the injectivity argument below.

The exact source is Deninger's version-1 preprint. Proposition 4.3 gives the sheaf epimorphism and hence local preimages, whereas Proposition 4.5 supplies the conditional injectivity used here after the required integral refinements [@Deninger2025Rational Props. 4.3 and 4.5, pp. 21--23]. Corollary 4.7 gives a positive comparison only on certain finer, non-subcanonical topologies [@Deninger2025Rational Cor. 4.7, p. 24]. The closest earlier algebraic presentation result is Deninger--Mellit's explicit kernel computation for a localized monoid-algebra map to truncated $S$-Witt vectors [@DeningerMellit2019 Thm. 1.1]. Its quotient is different and it does not treat sheafification or finite-flat/fppf descent. The Stacks references used below supply general local-exactness and pushout--pullback formalism [@StacksProject Tags 03CN, 010I, and 06XP], not the arithmetic lift or obstruction.

A bounded update completed on 25 August 2026 searched the current arXiv record, version history, and API; DataCite; exact DOI/title queries in OpenAlex; Crossref; and the relevant official publisher records. Query clusters combined the phrases *rational Witt vectors*, *Verschiebung*, *fppf*, *sheafification*, *finite flat*, *reduced monoid algebra*, and *descent*; separate post-7-August-2025 queries screened broader Witt--Verschiebung and Witt--descent hits. Inclusion required either the same sheafified reduced-monoid-algebra-to-rational-Witt owner and a finite-flat/fppf lift or nonlift, or a proposition-level presentation or descent comparison. The exact-owner clusters returned only the source or zero hits. Deninger--Mellit was retained as the nearest presentation result; the recent arithmetic-jet and p-typical associative-Witt hits, and the broader spherical, KEnd/TR, Galois-lifting, and Grothendieck--Witt hits, were excluded because they change the owner. Within this declared scope, the source remained at version 1 and no direct post-source solution to the finite-flat/fppf additive lifting question was located. This bounded negative result is not a claim of global priority.

Our contribution is correspondingly narrow: we answer the additive lifting question for $V_N$, compute a concrete all-index descent obstruction for the stated sheaf epimorphism, and record its formal extension consequence. We do not construct a lift of Frobenius, a compatible system of Witt operations, or a ring endomorphism.

The proof isolates a reusable descent-obstruction template. Let $$e:\quad 0\longrightarrow K\longrightarrow Z
 \xrightarrow{p}W\longrightarrow0$$ be an extension of abelian sheaves. Fix an object $U$, a source section $z_0\in Z(U)$, and an endomorphism $v\colon W\to W$, and put $w=v(p(z_0))\in W(U)$. Suppose that a cover $f\colon V\to U$ admits a unique section $z_V\in Z(V)$ with $p(z_V)=f^*w$, and that the two pullbacks of $z_V$ to $V\times_UV$ differ by a nonzero section of $\ker(p)$. Then $w$ has no global preimage in $Z(U)$: any global preimage would restrict to $z_V$ and hence would have equal pullbacks. For any $u\colon K\to K$, a middle-object map inducing $(u,v)$ would send $z_0$ to a global preimage of $v(p(z_0))=w$. Proposition [\[prop:extcriterion\]](#prop:extcriterion){reference-type="ref" reference="prop:extcriterion"} therefore turns this particular failed descent test into $u_*e\ne v^*e$ for every $u$. The relation between $z_0$, $v$, and $w$ is essential: failure of an unrelated target section to have a global preimage would not by itself imply these Ext inequalities.

In the present argument, $p=\omega$, $z_0=(x)^\sharp$, $v=V_N$, $w=1-xT^N$, $U=\operatorname{Spec}k[x]$, and $V=\operatorname{Spec}k[s]$. The roots-of-unity product supplies the local preimage, Dedekind injectivity makes it unique, finite freeness and subcanonicity validate the cover and its restrictions on each site, and the truncated-nilpotent big-Witt detector together with torsion-freeness proves that the overlap difference is nonzero. These are the arithmetic and site-specific inputs; the preceding conditional implication is the reusable categorical core.

The order of proof reflects these separations. Section [2](#sec:objects){reference-type="ref" reference="sec:objects"} fixes the presheaf, sheaf, and section-level notation and identifies the actual extension. Section [3](#sec:lemmas){reference-type="ref" reference="sec:lemmas"} proves the two detection statements and the site-dependent Dedekind injectivity lemma. Section [4](#sec:obstruction){reference-type="ref" reference="sec:obstruction"} constructs the forced local factorization and shows that it fails descent for all $N>1$. Section [5](#sec:ext){reference-type="ref" reference="sec:ext"} gives the extension formulation, while Section [6](#sec:finiteflat){reference-type="ref" reference="sec:finiteflat"} records the finite-flat consequence and the source-sensitive correction. The final section states the controls and the limits of the result.

# Rational Witt sheaves and the extension {#sec:objects}

For a commutative unital ring $A$, let $\mathbb Z[A]$ be the integral monoid algebra on the multiplicative monoid of $A$. We write $$\underline{\mathbb Z}(A)=\mathbb Z[A]/\mathbb Z(0).$$ Thus an element is represented additively by a finite formal sum $\sum_i n_i(a_i)$, with the basis element $(0)$ set equal to zero. This is the reduced monoid algebra in equation (4), p. 3, of [@Deninger2025Rational]. The power-series formula for Verschiebung used below, $V_N(f)(T)=f(T^N)$, is equation (20), p. 14, of the same source. The map to rational big-Witt vectors is $$\omega_A\!\left(\sum_i n_i(a_i)\right)
   =\prod_i(1-a_iT)^{n_i}.
 \tag{2.1}\label{eq:omega}$$ The target $W_{\mathrm{rat}}(A)$ is viewed as an additive group under multiplication of its representing rational power series. Formula [\[eq:omega\]](#eq:omega){reference-type="eqref" reference="eq:omega"} is natural in $A$, and the Teichmüller element $[a]$ is represented by $1-aT$.

Three levels of notation occur and should not be conflated. The first is the presheaf group $\underline{\mathbb Z}(A)$, in which a displayed finite sum is written. The second is the sheaf section group $\mathcal Z(\operatorname{Spec}A)$, to which that finite sum has a canonical image. The third is a section represented only after choosing a cover, which need not come from any element of $\underline{\mathbb Z}(A)$. The main local candidate happens to be defined already at the first level, whereas the hypothetical global preimage is allowed to be an arbitrary section at the second level. Thus the contradiction does not depend on an unjustified identification $\underline{\mathbb Z}(A)=\mathcal Z(\operatorname{Spec}A)$. Whenever a formal sum is displayed below, its canonical image in the corresponding sheaf section group is understood.

Let $\underline{\mathbb Z}(\mathcal O)$ and $W_{\mathrm{rat}}(\mathcal O)$ be the corresponding presheaves on $\mathscr C$. We retain the notation $$\mathcal Z=\underline{\mathbb Z}(\mathcal O)^\sharp,\qquad
 \mathcal W=W_{\mathrm{rat}}(\mathcal O).$$ The second equality uses the already-sheaf result quoted above and is made only on the noetherian-affine site under discussion. We do not silently extend that assertion to a larger affine site without sheafifying the target there.

It is essential that $\omega$ is an epimorphism *in the category of sheaves*. For sheaves of abelian groups, this means that a target section has preimages after passage to a cover. It does not mean that $$\mathcal Z(U)\longrightarrow\mathcal W(U)$$ is surjective for every object $U$. Equivalently, the cokernel sheaf vanishes even though an objectwise cokernel presheaf can have nonzero sections before sheafification; see the local exactness criterion in [@StacksProject Tag 03CN]. The distinction is precisely what permits a local factorization of $1-xT^N$ while obstructing its descent.

More concretely, if $w\in\mathcal W(\operatorname{Spec}A)$, epimorphy yields a covering family $A\to A_i$ and sections $z_i\in\mathcal Z(\operatorname{Spec}A_i)$ with $\omega(z_i)=w|_{A_i}$. It supplies neither a natural choice of the $z_i$ nor their equality over $A_i\otimes_A A_j$. By contrast, an endomorphism $\widetilde V_N$ applied to the global section $(x)^\sharp$ would give a global preimage before any cover was selected. Its restrictions would agree on every overlap by functoriality. The proof therefore tests exactly the extra compatibility that a sheaf epimorphism does not provide.

Objectwise define $$K_0(A)=\ker\bigl(\underline{\mathbb Z}(A)\longrightarrow W_{\mathrm{rat}}(A)\bigr).$$ In concrete terms, $$K_0(A)=
 \left\{\sum_i n_i(a_i):
   \prod_i(1-a_iT)^{n_i}=1\right\}.
 \tag{2.2}\label{eq:kernel}$$ Abelian sheafification is exact, so $$\mathcal K=K_0^\sharp=\ker(\omega).$$ This yields the genuine short exact sequence [\[eq:extension\]](#eq:extension){reference-type="eqref" reference="eq:extension"} in the abelian category $\mathrm{Ab}(\mathscr C_\tau)$, for $\tau=\mathrm{fppf}$ or $\tau=\mathrm{ff}$. Nothing here asserts that $K_0(A)$ vanishes, or that taking sections preserves the right exactness of [\[eq:extension\]](#eq:extension){reference-type="eqref" reference="eq:extension"}.

The operation $V_N$ is natural because substitution $T\mapsto T^N$ commutes with change of coefficients. On Teichmüller representatives, $$V_N([a])=1-aT^N.
 \tag{2.3}\label{eq:versch}$$ A lift in this paper always means a morphism of the underlying abelian sheaves satisfying the commuting square. Such a lift would preserve $\mathcal K$: if $z\in\mathcal K$, then $\omega(\widetilde V_Nz)=V_N(\omega z)=0$. Hence it would induce some endomorphism $u$ of the kernel. No multiplicative compatibility is assumed.

# Three descent lemmas {#sec:lemmas}

We collect the ingredients that make the overlap calculation survive sheafification. The first rules out the possibility that the integer coefficient $q^a$ kills the obstruction.

[\[lem:torsionfree\]]{#lem:torsionfree label="lem:torsionfree"} For every $m\geq1$, multiplication by $m$ is a monomorphism of $\mathcal Z$, for either topology.

The group $\mathbb Z[A]$ is free abelian on the underlying multiplicative monoid of $A$. The summand generated by $(0)$ is free and split as an abelian group, so $\underline{\mathbb Z}(A)=\mathbb Z[A]/\mathbb Z(0)$ is free abelian on the nonzero elements of $A$. Multiplication by $m$ is therefore objectwise injective. Exactness of sheafification of abelian presheaves preserves this monomorphism.

The sheaf conclusion is stronger than torsion-freeness at one selected ring. If a section has survived sheafification, no nonzero integer multiple of it can disappear after a further covering refinement. In the main calculation the detector first proves $y^\sharp\ne0$, and this lemma then proves $q^a y^\sharp\ne0$. Reversing those two steps would fail, because the big-Witt image of the multiple is deliberately the identity.

We next use the full big-Witt sheaf only as a detector. Under its standard power-series description, the Teichmüller map is injective because the coefficient of $T$ in $1-aT$ recovers $-a$.

[\[lem:detector\]]{#lem:detector label="lem:detector"} Let $\tau$ be either the fppf or finite-flat topology. If a section $z\in\mathcal Z(U)$ has nonidentity image in the big-Witt sheaf $W(\mathcal O)(U)$, then $z\ne0$.

Both topologies are subcanonical, and the big-Witt construction in its power-series model is a sheaf on them. The natural map $\mathcal Z\to W(\mathcal O)$ sends a formal sum to the product in [\[eq:omega\]](#eq:omega){reference-type="eqref" reference="eq:omega"}. A zero section must map to the identity power series. The contrapositive gives the claim. This is the same detection principle used for the class over $\mathbb F_2[\varepsilon]/(\varepsilon^2)$ in Deninger's Example 4.4 [@Deninger2025Rational p. 22].

Subcanonicity enters only in this detection step and in interpreting the displayed restrictions without changing the structure sheaf. The rational Witt map cannot detect the final obstruction, since that obstruction lies in its kernel by construction. Passing temporarily to the full big-Witt sheaf retains the lower-degree coefficient $\varepsilon^dT^d$, and torsion-freeness then transports nonvanishing back to the rational-kernel section that is needed.

The final lemma forces uniqueness of the local preimage on the root cover.

[\[lem:dedekind\]]{#lem:dedekind label="lem:dedekind"} Let $B$ be a Dedekind domain. The map $$\omega_B\colon\mathcal Z(\operatorname{Spec}B)\longrightarrow\mathcal W(\operatorname{Spec}B)$$ is injective on $\mathscr C_{\mathrm{fppf}}$. It is also injective when $\mathscr C$ is equipped with the finite-flat topology.

Deninger's Proposition 4.5 gives injectivity when the relevant covers admit refinements by integral schemes [@Deninger2025Rational Prop. 4.5, pp. 22--23]. We verify that hypothesis in the two cases used here.

First take an fppf covering of $\operatorname{Spec}B$. Because the target is quasi-compact, retain a finite subcover, written on rings as finitely presented flat $B$-algebras $C_i$. Each $C_i$ is noetherian. Replace it by its finitely many quotients $C_i/\mathfrak p$, where $\mathfrak p$ runs through the minimal primes. Flat going down implies $\mathfrak p\cap B=(0)$; compare [@StacksProject Tag 00HS]. Thus every $C_i/\mathfrak p$ is a domain and is torsion-free as a $B$-module. Over a Dedekind domain, torsion-free modules are flat [@StacksProject Tag 0AUW]. The quotient remains of finite presentation over $B$, and the irreducible components jointly cover $\operatorname{Spec}C_i$. These domains therefore form an fppf refinement of the original cover.

For clarity, the finite-presentation assertion uses no hidden excellence hypothesis: since $C_i$ is noetherian, each minimal prime is finitely generated, so $C_i/\mathfrak p$ is again a finitely presented $B$-algebra. The union of the closed subsets $\operatorname{Spec}(C_i/\mathfrak p)$ over all minimal primes is all of $\operatorname{Spec}C_i$. After composing with the original covering maps, the resulting family is therefore still jointly surjective over $\operatorname{Spec}B$. Zero components, if present, may simply be omitted. All rings retained in this finite construction lie in the fixed universe-small site chosen at the outset.

If the original cover is finite flat, each $C_i$ is finite over $B$. The same minimal-prime quotients are finite and torsion-free over $B$, hence finite locally free. They give a finite-flat domain refinement. Proposition 4.5 now applies separately in both topologies.

[\[rem:scope-site\]]{#rem:scope-site label="rem:scope-site"} Lemma [\[lem:dedekind\]](#lem:dedekind){reference-type="ref" reference="lem:dedekind"} is needed only at the polynomial ring $B=k[s]$, which is a principal ideal domain. The proof does not assert that $\omega$ is injective at arbitrary nonreduced objects; indeed, the nonreduced specialization in Section [4](#sec:obstruction){reference-type="ref" reference="sec:obstruction"} is where the kernel is detected.

# The all-index descent obstruction {#sec:obstruction}

We now give the common explicit calculation. Its output is slightly stronger than nonliftability: for every nontrivial index it produces a rational Witt section over a Dedekind domain that is locally, but not globally, in the image of $\omega$.

[\[prop:failure\]]{#prop:failure label="prop:failure"} Fix $N>1$, and let $\tau$ be either the fppf topology or the finite-flat topology. There are a finite field $k$, the Dedekind domain $A=k[x]$, and a section $$w_N=1-xT^N\in W_{\mathrm{rat}}(A)$$ such that $$w_N\notin
 \operatorname{im}\bigl(\omega_A\colon
 \mathcal Z(\operatorname{Spec}A)\longrightarrow\mathcal W(\operatorname{Spec}A)\bigr).$$ The section $w_N$ acquires a preimage on a finite-free faithfully flat cover of rank $N$.

Choose a prime divisor $q$ of $N$, and write $$N=q^a d,\qquad a\geq1,\qquad (q,d)=1.
 \tag{4.1}\label{eq:decompose}$$ There is a finite extension $k/\mathbb F_q$ containing all $d$-th roots of unity. Since $q\nmid d$, the group $\mu_d(k)$ has exactly $d$ elements. Set $$A=k[x],\qquad B=k[s],\qquad A\longrightarrow B,\quad x\longmapsto s^N.
 \tag{4.2}\label{eq:rootcover}$$ As an $A$-module, $B$ is free with basis $1,s,\ldots,s^{N-1}$; hence $\operatorname{Spec}B\to\operatorname{Spec}A$ is a finite-free faithfully flat cover. In particular, it is a cover for both topologies.

Define the formal section $$c_N(s)=q^a\sum_{\zeta\in\mu_d(k)}(\zeta s)
       \in\underline{\mathbb Z}(B)\longrightarrow\mathcal Z(\operatorname{Spec}B).
 \tag{4.3}\label{eq:candidate}$$ The elementary identity $$\prod_{\zeta\in\mu_d(k)}(1-\zeta u)=1-u^d
 \tag{4.4}\label{eq:roots}$$ and the characteristic-$q$ Frobenius identity give $$\begin{aligned}
 \omega_B(c_N(s))
  &=\prod_{\zeta\in\mu_d(k)}(1-\zeta sT)^{q^a}\\
  &=(1-s^dT^d)^{q^a}\\
  &=1-s^{dq^a}T^{dq^a}
   =1-s^NT^N.
 \tag{4.5}\label{eq:localimage}\end{aligned}$$ Thus $c_N(s)$ is a local preimage of the pullback of $w_N$. Moreover it is the only local preimage in $\mathcal Z(\operatorname{Spec}B)$, because $B=k[s]$ is a Dedekind domain and Lemma [\[lem:dedekind\]](#lem:dedekind){reference-type="ref" reference="lem:dedekind"} makes $\omega_B$ injective.

Suppose, for contradiction, that a global section $z\in\mathcal Z(\operatorname{Spec}A)$ satisfies $\omega_A(z)=w_N$. Its restriction to $\operatorname{Spec}B$ has the same Witt image as $c_N(s)$, so uniqueness forces $$z|_B=c_N(s).
 \tag{4.6}\label{eq:forced}$$ The double overlap is $$R=B\otimes_A B
   =k[s_1,s_2]/(s_1^N-s_2^N).
 \tag{4.7}\label{eq:overlap}$$ Because the two restrictions of a global section agree, equation [\[eq:forced\]](#eq:forced){reference-type="eqref" reference="eq:forced"} would imply $$c_N(s_1)=c_N(s_2)\qquad\text{in }\mathcal Z(\operatorname{Spec}R).
 \tag{4.8}\label{eq:descentneeded}$$

To test this equality, put $$D=k[\varepsilon]/(\varepsilon^N)
 \tag{4.9}\label{eq:D}$$ and use the homomorphism $R\to D$ defined by $s_1\mapsto\varepsilon$ and $s_2\mapsto0$. It is well defined since $\varepsilon^N=0$. Under the induced restriction map, the difference between the two sides of [\[eq:descentneeded\]](#eq:descentneeded){reference-type="eqref" reference="eq:descentneeded"} becomes $$q^a y^\sharp,\qquad
 y=\sum_{\zeta\in\mu_d(k)}(\zeta\varepsilon)\in\underline{\mathbb Z}(D).
 \tag{4.10}\label{eq:y}$$ We first detect $y^\sharp$, rather than its $q^a$-multiple, in the big-Witt sheaf: $$\prod_{\zeta\in\mu_d(k)}(1-\zeta\varepsilon T)
   =1-\varepsilon^dT^d\ne1.
 \tag{4.11}\label{eq:detecty}$$ Indeed $d<N$, because $a\geq1$, so $\varepsilon^d\ne0$ in $D$. Lemma [\[lem:detector\]](#lem:detector){reference-type="ref" reference="lem:detector"} therefore gives $y^\sharp\ne0$. Lemma [\[lem:torsionfree\]](#lem:torsionfree){reference-type="ref" reference="lem:torsionfree"} then gives $$q^a y^\sharp\ne0.
 \tag{4.12}\label{eq:qnonzero}$$ This contradicts [\[eq:descentneeded\]](#eq:descentneeded){reference-type="eqref" reference="eq:descentneeded"}.

For completeness, the nonzero section in [\[eq:qnonzero\]](#eq:qnonzero){reference-type="eqref" reference="eq:qnonzero"} lies in the kernel of the rational Witt map: $$\omega_D(q^a y^\sharp)
  =(1-\varepsilon^dT^d)^{q^a}
  =1-\varepsilon^NT^N=1.
 \tag{4.13}\label{eq:inkernel}$$ Thus the calculation identifies an actual nonzero kernel section. Notice the order of the argument: the big-Witt image detects $y^\sharp$, while torsion-freeness detects its $q^a$-multiple; the big-Witt image of that multiple is itself the identity.

## How the arithmetic factors enter {#subsec:factors}

Each part of the decomposition $N=q^a d$ has a distinct role. The field characteristic turns the coefficient $q^a$ in the monoid algebra into a $q^a$-th power on the Witt side. The equality $(1-u)^{q^a}=1-u^{q^a}$ then changes degree $d$ into degree $N$. The prime-to-$q$ factor is handled by the separable polynomial $X^d-1$: after a finite extension of $\mathbb F_q$, all of its roots are available and equation [\[eq:roots\]](#eq:roots){reference-type="eqref" reference="eq:roots"} packages them without multiplicity. No algebraic closure is needed, and the resulting field remains finite.

The strict inequality $d<N$ is equally important. It ensures that $\varepsilon^d$ survives in $D=k[\varepsilon]/(\varepsilon^N)$, so the inner section is visible to the big-Witt detector. At the same time, multiplication by $q^a$ raises the detected power series to $1-\varepsilon^NT^N=1$, placing the final nonzero section in the rational kernel. Thus the same factorization simultaneously creates visibility before multiplication and vanishing after multiplication.

Finally, the cover in [\[eq:rootcover\]](#eq:rootcover){reference-type="eqref" reference="eq:rootcover"} is not chosen merely for convenience. Its finite freeness places it in both sites, while its source $k[s]$ is a PID, where Lemma [\[lem:dedekind\]](#lem:dedekind){reference-type="ref" reference="lem:dedekind"} forces uniqueness. These two properties let a single overlap calculation address the two topologies while keeping their injectivity proofs logically separate.

The construction is uniform in the index but intentionally not in the coefficient field. For each $N$, a prime divisor $q$ and a finite extension of $\mathbb F_q$ containing $\mu_d$ are selected. This is enough to rule out a natural transformation on the absolute site: such a transformation must act on every object, so one counterexample object for each index is decisive. No single coefficient ring is claimed to detect all indices simultaneously.

Two possible escape routes are also excluded by the form of the proof. First, the section $z$, if it existed, could be an arbitrary sheaf section; it is not assumed to be represented by one formal sum over $A$. Only after restricting to $B$ does injectivity identify it with the displayed presheaf section $c_N(s)$. Second, a different covering family cannot avoid the contradiction. Any global section produced using such a family would still restrict to the fixed root cover and would again be forced to equal $c_N(s)$, so it would have the same nonzero overlap difference.

The direction of specialization is similarly important. The ring map $R\to D$ defines a morphism $\operatorname{Spec}D\to\operatorname{Spec}R$, hence a restriction of sheaf sections from the overlap to the truncated ring. Nonvanishing after this restriction proves nonvanishing before it. No claim is made that $D$ covers $R$, and none is needed: the specialization is a detector of inequality, not a descent cover. It is well defined precisely because both $s_1^N$ and $s_2^N$ map to zero. Every ring in this detection chain remains noetherian and affine.

The obstruction can be retained directly on the double overlap. Define $$\delta_N=c_N(s_1)-c_N(s_2)\in\mathcal Z(\operatorname{Spec}R).
 \tag{4.14}\label{eq:delta}$$ Since $s_1^N=s_2^N$ in $R$, equation [\[eq:localimage\]](#eq:localimage){reference-type="eqref" reference="eq:localimage"} shows that $\delta_N\in\mathcal K(\operatorname{Spec}R)$. Its image under $R\to D$ is the nonzero section $q^a y^\sharp$. Hence $\delta_N\ne0$. This gives a compact description of the failure: the only possible local preimage has a nonvanishing difference on the first overlap.

Fix one of the two topologies and suppose that $\widetilde V_N$ is a lift for some $N>1$. With $A=k[x]$ as in Proposition [\[prop:failure\]](#prop:failure){reference-type="ref" reference="prop:failure"}, apply the lift to the section $(x)^\sharp\in\mathcal Z(\operatorname{Spec}A)$. Naturality and the commuting-square condition give $$\omega_A\bigl(\widetilde V_N((x)^\sharp)\bigr)
  =V_N(1-xT)=1-xT^N=w_N.$$ This is a global preimage excluded by Proposition [\[prop:failure\]](#prop:failure){reference-type="ref" reference="prop:failure"}. The argument proves the fppf theorem. Separately, the root morphism [\[eq:rootcover\]](#eq:rootcover){reference-type="eqref" reference="eq:rootcover"} is finite free, the finite-flat form of Lemma [\[lem:dedekind\]](#lem:dedekind){reference-type="ref" reference="lem:dedekind"} supplies uniqueness, and the finite-flat topology is subcanonical; the same calculation therefore proves the finite-flat theorem without transferring a conclusion between sites. If $N=1$, $\widetilde V_1=\operatorname{id}_{\mathcal Z}$ satisfies the required identity.

## The first index as a source control

When $N=2$, take $q=2$, $a=1$, $d=1$, and $k=\mathbb F_2$. Then $$A=\mathbb F_2[x],\qquad B=\mathbb F_2[s],\qquad x=s^2,$$ and the unique local preimage is $c_2(s)=2(s)$. The overlap is $$\mathbb F_2[s_1,s_2]/(s_1^2-s_2^2)
  =\mathbb F_2[s_1,s_2]/((s_1-s_2)^2).$$ Specialization to $\mathbb F_2[\varepsilon]/(\varepsilon^2)$ gives the nonzero class $2(\varepsilon)^\sharp$ appearing in Deninger's Example 4.4 [@Deninger2025Rational p. 22]. The general proof may therefore be viewed as an all-index root-of-unity expansion of that first obstruction.

# The extension-theoretic formulation {#sec:ext}

For each $\tau\in\{\mathrm{fppf},\mathrm{ff}\}$, we relate the concrete failure to the topology-indexed extension class $e_\tau$ in [\[eq:extension\]](#eq:extension){reference-type="eqref" reference="eq:extension"}. The required statement is formal in the abelian category $\mathrm{Ab}(\mathscr C_\tau)$, but making the two functorial directions explicit prevents a common ambiguity.

[\[prop:extcriterion\]]{#prop:extcriterion label="prop:extcriterion"} Let $$e:\quad0\longrightarrow K\longrightarrow Z
   \xrightarrow{p}W\longrightarrow0$$ be an extension in an abelian category. Given $u\colon K\to K$ and $v\colon W\to W$, there exists a morphism $\widetilde v\colon Z\to Z$ inducing $u$ on $K$, inducing $v$ on $W$, and satisfying $p\widetilde v=vp$, if and only if $$u_*e=v^*e\qquad\text{in }\operatorname{Ext}^1(W,K).
 \tag{5.1}\label{eq:criterion}$$ When nonempty, the set of such middle-object morphisms is a torsor under $\operatorname{Hom}(W,K)$.

Push out the first copy of $e$ along $u$ and pull back the second copy along $v$. A morphism of the original extensions inducing the prescribed end maps produces an equivalence between these two extensions. Conversely, an equivalence between the pushout and pullback extensions, composed with their universal morphisms, produces a middle-object map with end maps $(u,v)$. This is the usual functoriality of extensions [@StacksProject Tag 010I]; identifying Yoneda extensions with $\operatorname{Ext}^1$ gives [\[eq:criterion\]](#eq:criterion){reference-type="eqref" reference="eq:criterion"} [@StacksProject Tag 06XP].

If $\widetilde v_1$ and $\widetilde v_2$ have the same end maps, their difference is zero on $K$ and has image in $K$. It therefore factors uniquely as $$Z\xrightarrow{p}W\xrightarrow{h}K\longrightarrow Z$$ for some $h\in\operatorname{Hom}(W,K)$. Adding such a factorization acts freely and transitively on the set of middle-object maps.

Fix $\tau\in\{\mathrm{fppf},\mathrm{ff}\}$. Apply Proposition [\[prop:extcriterion\]](#prop:extcriterion){reference-type="ref" reference="prop:extcriterion"} in $\mathrm{Ab}(\mathscr C_\tau)$ to the extension $e_\tau$ in [\[eq:extension\]](#eq:extension){reference-type="eqref" reference="eq:extension"}, with $v=V_N$. Equality $u_*e_\tau=V_N^*e_\tau$ would produce an additive middle-object morphism $\mathcal Z\to\mathcal Z$ on $\mathscr C_\tau$ lifting $V_N$, contrary to Theorem [\[thm:fppf\]](#thm:fppf){reference-type="ref" reference="thm:fppf"} when $\tau=\mathrm{fppf}$ and to Theorem [\[thm:ff\]](#thm:ff){reference-type="ref" reference="thm:ff"} when $\tau=\mathrm{ff}$. Hence the two classes are unequal for every $u\colon\mathcal K_\tau\to\mathcal K_\tau$. In the final paragraph of this proof, the unadorned $e$ and $\mathcal K$ abbreviate $e_\tau$ and $\mathcal K_\tau$.

Taking $u=0$, the pushout $0_*e$ is the zero extension class. The inequality therefore shows $V_N^*e\ne0$. Also $e\ne0$: if [\[eq:extension\]](#eq:extension){reference-type="eqref" reference="eq:extension"} split, the splitting would make $\omega$ surjective on the sections of every object, contradicting Proposition [\[prop:failure\]](#prop:failure){reference-type="ref" reference="prop:failure"}. Equivalently, a chosen decomposition $Z\simeq K\oplus W$ would allow the middle map $0\oplus V_N$.

The section $\delta_N$ in [\[eq:delta\]](#eq:delta){reference-type="eqref" reference="eq:delta"} is a necessary-descent detector for a specific finite-free cover. We do not claim that the associated Čech complex computes the full sheaf $\operatorname{Ext}^1(\mathcal W,\mathcal K)$. The passage from the explicit nonlift to the Ext inequality uses Proposition [\[prop:extcriterion\]](#prop:extcriterion){reference-type="ref" reference="prop:extcriterion"}, not a comparison theorem between Čech and derived cohomology.

## The connecting-section viewpoint

There is a second way to state the nonvanishing that remains below the level of a full Čech-to-derived comparison. Apply the section functor over $\operatorname{Spec}A$ to the short exact sequence [\[eq:extension\]](#eq:extension){reference-type="eqref" reference="eq:extension"}. Its long exact cohomology sequence contains a connecting morphism $$\partial_A\colon
 \mathcal W(\operatorname{Spec}A)\longrightarrow
 H^1_\tau(\operatorname{Spec}A,\mathcal K).
 \tag{5.2}\label{eq:connecting}$$ Exactness says that $\partial_A(w_N)=0$ precisely when $w_N$ has a global preimage in $\mathcal Z(\operatorname{Spec}A)$. Proposition [\[prop:failure\]](#prop:failure){reference-type="ref" reference="prop:failure"} therefore gives $$\partial_A(1-xT^N)\ne0.
 \tag{5.3}\label{eq:connectingnonzero}$$ The section $\delta_N$ is an explicit witness to the failed first descent condition for the chosen root cover. Equation [\[eq:connectingnonzero\]](#eq:connectingnonzero){reference-type="eqref" reference="eq:connectingnonzero"}, however, follows from the long exact sequence and objectwise nonsurjectivity, so it does not require the additional assertion that this particular Čech cocycle computes all of $H^1_\tau$, much less all of $\operatorname{Ext}^1$.

# The finite-flat site and the Dedekind-section assertion {#sec:finiteflat}

Although the same equations occur in both topologies, the finite-flat conclusion has its own site-dependent inputs. The cover $k[x]\to k[s]$ is finite free; its double overlap remains an object of the noetherian-affine site; the specialization to $k[\varepsilon]/(\varepsilon^N)$ is a valid restriction; and both the rational and full big-Witt targets are sheaves for the topology in use. Most importantly, the finite-flat half of Lemma [\[lem:dedekind\]](#lem:dedekind){reference-type="ref" reference="lem:dedekind"} refines a finite-flat cover of a Dedekind domain by finite-flat integral domains. These checks, rather than a change-of-site implication, justify Theorem [\[thm:ff\]](#thm:ff){reference-type="ref" reference="thm:ff"}.

We now spell out the consequence for the source statement. On the finite-flat site, take already the first index $$A=\mathbb F_2[x],\qquad w=1-xT^2\in W_{\mathrm{rat}}(A).
 \tag{6.1}\label{eq:cor46example}$$ The section $w$ has the local preimage $2(s)^\sharp$ on the finite-free cover $x=s^2$, as Proposition 4.3 predicts. Proposition 4.5, together with the Dedekind-domain refinement in Lemma [\[lem:dedekind\]](#lem:dedekind){reference-type="ref" reference="lem:dedekind"}, makes that preimage unique over $B=\mathbb F_2[s]$. Its two restrictions disagree on the overlap, as detected by $2(\varepsilon)^\sharp\ne0$. Consequently $$w\notin
 \operatorname{im}\bigl(
 \mathcal Z(\operatorname{Spec}\mathbb F_2[x])\longrightarrow
 W_{\mathrm{rat}}(\mathbb F_2[x])\bigr).
 \tag{6.2}\label{eq:notimage}$$

Corollary 4.6 of the version-1 source states a sectionwise equality over Dedekind rings for the finite-flat topology [@Deninger2025Rational p. 23]. Equation [\[eq:notimage\]](#eq:notimage){reference-type="eqref" reference="eq:notimage"} shows that this equality does not hold as stated. The proof in the source appears to use the epimorphism of Proposition 4.3 as though it were surjective on the section group at $\operatorname{Spec}A$. In a sheaf category, an epimorphism supplies local preimages; it does not ensure that a chosen local preimage descends. Proposition 4.5 supplies the relevant injectivity after the domain-refinement argument, but injectivity only makes the failed local choice unique. It cannot turn it into a global section.

This correction is deliberately limited. It does not affect the epimorphism of sheaves in Proposition 4.3, the conditional injectivity mechanism of Proposition 4.5, or the explicit noninjectivity phenomenon in Example 4.4. It concerns the objectwise-surjectivity step in the printed Corollary 4.6. The calculation is also independent of any response or future revision by the source author.

## Robustness of the section counterexample

The contradiction is not an artifact of having chosen an inconvenient local preimage. Suppose a global preimage of $w_N$ existed, perhaps constructed using a completely different covering family. Restricting that global section to the fixed root cover would still produce a preimage of $1-s^NT^N$ over $B=k[s]$. Dedekind injectivity would identify it with $c_N(s)$, whose overlap restrictions have already been proved unequal. Thus no alternative cover, refinement, or local factorization can repair the global section. The root cover is a test forced on every putative global preimage, not an assumption about how such a preimage must first be found.

Nor does the argument rely on $w_N$ lying only in a larger completion. It is the Verschiebung $V_N([x])$ of the rational Teichmüller element $[x]=1-xT$, so $w_N=1-xT^N$ is a rational Witt vector by naturality of $V_N$. All displayed products in the proof are finite. The specialization ring $D$ is used only to test equality of sheaf sections; it is not asserted to be Dedekind, and no injectivity claim is made there. This separation is what allows nilpotents to expose the kernel without weakening the uniqueness argument over $B$.

The source inputs consequently have distinct logical roles. Theorem 3.4 identifies the rational Witt target as the sheaf being evaluated; Proposition 4.3 explains why the target section has local preimages; Proposition 4.5, after the domain-refinement lemma, makes the preimage on $B$ unique; and Example 4.4 supplies the first-index nonvanishing control. Corollary 4.6 is not used as a premise at any stage. It is tested only after the independent descent calculation has been completed.

# Scope, controls, and conclusion {#sec:scope}

The index $N=1$ is a sharp elementary control: $V_1$ is the identity and is lifted by $\operatorname{id}_{\mathcal Z}$. For every $N>1$, the prime-power part $q^a$ of $N$ creates a nilpotent kernel class, while the prime-to-$q$ part $d$ is handled by the full set of $d$-th roots of unity. This explains why the same construction covers all composite patterns rather than only prime indices.

There is no contradiction with the positive comparator in Deninger's Corollary 4.7 [@Deninger2025Rational p. 24]. That result concerns certain finer, non-subcanonical topologies on which the relevant map becomes an isomorphism. Our detector and our obstruction are explicitly formulated for the subcanonical fppf and finite-flat topologies. A change to a non-subcanonical topology can annihilate exactly the nilpotent information used here.

Several boundaries are worth recording. First, the theorem concerns morphisms of abelian sheaves; it neither proves nor disproves the existence of unrelated nonlinear, derived, or topology-changing constructions. Second, no compatible Frobenius--Verschiebung law is addressed after Verschiebung itself fails to lift. Third, the result is absolute over the chosen noetherian-affine site; no relative base scheme or extension to all affine schemes is claimed. Fourth, the bounded source search underlying this draft supports owner subtraction but is not a global priority or novelty theorem.

The conclusion is therefore exact and modest. Local root factorization does produce the expected rational Witt section, but Dedekind injectivity forces a local representative whose double-overlap difference survives sheafification. That single explicit descent failure rules out an additive lift of $V_N$ for every $N>1$ on each of the two sites and, for each $\tau\in\{\mathrm{fppf},\mathrm{ff}\}$, gives $V_N^*e_\tau\ne0$.

The reusable mechanism is the conditional implication from a selected cover-local preimage, made unique, with a nonzero overlap difference to the absence of its global preimage, followed by the formal pushout--pullback translation for a source section mapped to that selected target. The example-specific verification combines Dedekind injectivity on the root-cover source; the rational-Witt sheaf, finite-flat-cover, and subcanonicity inputs that validate the cover and restrictions on each site; the full big-Witt detector on the truncated nilpotent ring; and torsion-freeness of the sheafified reduced monoid algebra. Within this larger proof package, four finite algebra calculations form the explicit computational core: a root cover, a roots-of-unity product, one tensor-product overlap, and one truncated-polynomial specialization. This core, together with the stated proof inputs, is the principal verification artifact of the note.

# Declarations {#declarations .unnumbered}

#### Data and materials availability.

No empirical data were generated or analyzed. The proof ledger, source locator audit, claim manifest, and compilation materials used to assemble this draft are available from the author upon reasonable request.

#### Ethics statement.

This is a theoretical mathematics study involving no human participants, animals, personal data, or field interventions; ethics approval and informed consent are not applicable.

#### Author contributions.

Liang Wang conceived the study, developed and verified the proofs, conducted the literature review, and wrote and revised the manuscript.

#### Funding.

The author received no specific funding for this work.

#### Competing interests.

The author declares no competing interests.

#### AI-use disclosure.

AI-assisted tools were used during literature triage, proof-audit support, and drafting. Every mathematical claim, reference, attribution, and wording choice requires final verification and responsibility by the named human author before dissemination. No AI system is listed as an author.

#### Limitations.

The result is limited to additive sheaf lifts of $V_N$ on the fixed absolute noetherian-affine fppf and finite-flat sites. It makes no venue-readiness claim, no claim about all affine schemes without a newly sheafified target, and no claim about future versions of the cited preprint.
