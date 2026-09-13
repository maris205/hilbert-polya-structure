---
p1_kind: "derived-fulltext-reading-copy"
route: "flow_systems"
logical_paper_id: "flow_systems--13-circle-twists"
canonical_tex: "flow_systems/papers/13-circle-twists/paper/manuscript.tex"
canonical_pdf: "flow_systems/papers/13-circle-twists/paper/paper.pdf"
source_sha256: "c8c9b7522e9bf63a30ed199fe3468d642cb3e572e324680ccd6893857fbe9701"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Technical Note: Gauge-Trivial Circle Twists and Constant-Diagonal Corona Records for Indiscrete Real Actions

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../flow_systems/papers/13-circle-twists>)
- [规范 TeX](<../../../../../flow_systems/papers/13-circle-twists/paper/manuscript.tex>)
- [关联 PDF](<../../../../../flow_systems/papers/13-circle-twists/paper/paper.pdf>)
- [支撑 Markdown](<../../../../../flow_systems/papers/13-circle-twists/README.md>)
- [BibTeX](<../../../../../flow_systems/papers/13-circle-twists/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  This Technical Note concerns continuous circle twists on author records of globally indiscrete real actions and their same-carrier standard comparison; it is not a standalone classification. Real-line multiplier triviality and the twisted-convolution, gauge, amenability, $c_0$-sum, multiplier, and corona mechanisms are prior or standard. Companion Papers 2, 8, 9, 11, and 12 respectively supply the continuum lower bound; the one-orbit proxy and trace/return boundary; the actual packet, topology, stabilizer, and period; the untwisted actual records; and all-degree factorization, standardization, and the comparison map. At a fixed normalization, we verify the time/actual gauge bridge and give a direct sign-exact real-line trivialization. We then construct separately typed twisted test, maximal, and reduced author records with oriented gauge covariance. Exactly four registered outputs become constant after tags are forgotten, while literal stabilizers, topology, and periods remain. Actual-to-standard function pullback has an exact support formula and a zero/finite/infinite criterion. On each standard component, the selected time images are separately isometric for maximal and reduced norms. Only after those isometries is the corona statement invoked: it is a generic constant-diagonal lemma for an arbitrary $c_0$-sum. Its fixed-prime instances hold for both completions but do not distinguish or recover the prime. Finite deterministic checks remain diagnostics. No topology transfer, globally named actual twisted groupoid $C^*$-algebra, trace, determinant, or spectral promotion is obtained.
author:
- |
  **AUTHOR TO CONFIRM**\
  Author list, order, affiliations, and correspondence: AUTHOR TO CONFIRM
bibliography:
- references.bib
date: 15 August 2026
title: |
  **Technical Note: Gauge-Trivial Circle Twists and\
  Constant-Diagonal Corona Records for Indiscrete Real Actions**
```

## Markdown 正文

**Keywords:** continuous multipliers; twisted convolution; indiscrete action groupoids; gauge equivalence; support transfer; corona algebras.

**中文摘要**

本文是一篇技术说明，研究不可分实数作用的作者记录、连续圆周乘子及同载体标准化比较，并不主张独立分类。实直线乘子的规范平凡性以及扭曲卷积、规范变换、可数消失直和、乘子代数与冠商方法均属先行或标准工具。前序论文二、八、九、十一、十二分别拥有连续统下界，单轨道代理和迹与返回边界，实际分组的拓扑、稳定子与周期，未扭曲作者记录，以及全次数因子化、标准化和比较映射。本文在固定符号下核对时间与实际记录的规范桥，并给出符号精确的直接平凡化证明；测试、最大与约化记录始终分开且满足规范协变。忘去标签后保持常值的恰为四个登记输出，稳定子、嵌入、拓扑和周期仍被保留。实际到标准记录的函数拉回具有精确支撑公式，并区分零函数、有限指标集与无限指标集。每个标准分量上的选定时间像在两种范数下分别等距；此后所用冠商结论是任意指标集上可数消失直和的一般常对角引理。固定素数实例对两种完备化均成立，却不区分素数，也不能恢复算术参数。有限计算只作诊断；本文不转移拓扑，不命名未经审计的实际扭曲群胚代数，也不构造迹、行列式或谱对象。

**中文关键词：** 连续乘子；扭曲卷积；不可分作用群胚；规范等价；支撑转移；冠代数。

# Introduction and positioning {#sec:introduction}

The problem addressed here is narrow but sign-sensitive. A globally indiscrete right action of the usual group $\mathbb R$ has an actual author record, whereas its orbitwise standardization has a disjoint-union topology. A circle multiplier is read through time on the former, while component crossed-product and corona constructions live on the latter. Confusing any two of those owners reverses a pullback, transfers a topology, or silently changes a completion. This document is therefore an explicitly labelled *technical note*: it assembles the already proved facts at their exact owners and verifies the residual signs and norm chains. Its retained status is the NOTE branch with `STANDALONE_PASS=false`.

The word "author" is used here in a deliberately local sense: it labels the project-defined test and completion records that are actually available on the indiscrete owner. It is not a claim that a conventional global twisted groupoid completion has been identified. Conversely, the standard coproduct is a genuine Hausdorff component owner, but it does not inherit the actual topology. Keeping those two facts visible is more important than compressing the notation. The same discipline applies to maximal and reduced norms: even when a common selected subalgebra has equal norms, its two ambient component records retain their names and domains.

The subtraction precedes the contribution. First, the official abstract of Sorkin's 1978 paper advertises continuous remultiplication of every continuous multiplier of the real line to the identity [@Sorkin1978Triviality]. We use that record only for existence-level prior credit: the full text was not available in the audited corpus, so no normalization, sign, proof step, or actual-owner transfer is imported. Twisted group and crossed-product mechanisms are standard prior background, with Packer--Raeburn used only at publisher-level scope [@PackerRaeburn1989Twisted]. Likewise, ordinary $c_0$ sums, multiplier products, quotient norms, and corona algebras are not isolated contributions of this note.

Second, five companion manuscripts own the application-side premises. Paper 2 proves the hard sign-subgroup/procyclic continuum lower bound [@Wang2026ArithmeticPeriodPackets Proposition `prop:uncountable`]. Paper 8 owns the one-orbit standard-circle proxy, trace and return formulas, the local/packet firewall, and the positive-time scalar ledger [@Wang2026IsotropyAveraging]. Paper 9 owns the actual prime packet, its indiscrete topology, literal stabilizer and period, and the bare quotient $U_p/H_p$ [@Wang2026PacketSeparation Corollaries `cor:packet` and `cor:orbit`]. Paper 11 owns the actual time-only collapse and the untwisted author test, maximal, and reduced records [@Wang2026ContinuousConvolution Theorems `thm:phi`, `thm:star-algebra`, and `thm:completions`]. Paper 12 owns all-degree factorization, same-carrier standardization, compact open orbit components, the continuous map $J$ from standard to actual, and its invariant-diagonal comparator [@Wang2026MarkedTime Theorem `thm:factorization` and Corollary `cor:packet-comparison`].

P0.20YY Owner & Retained result & Not credited to this note\
Sorkin and standard theory & advertised real-line collapse; twisted and operator-algebra mechanisms & original classification or standard machinery\
Paper 2 & fixed-prime continuum lower bound & sign/procyclic lower-bound proof\
Paper 8 & one-orbit proxy; trace/return and scalar ledgers & any trace or return formula\
Paper 9 & actual packet, topology, stabilizer, period, bare quotient & actual-owner construction\
Paper 11 & actual time collapse and untwisted author records & untwisted test/full/reduced theory\
Paper 12 & factorization, standardization, components, $J$, comparator & topology and cochain comparison\

(trace artifact `P13-TAB-02-PRIOR-SUBTRACTION`; package README, "Strict six-key artifact traces") is the subtraction ledger used in this introduction: Sorkin and standard mechanisms, followed by the distinct premises owned by Papers 2, 8, 9, 11, and 12, are removed before the residual contribution is stated.

After those subtractions, the permitted centre is an exact sign- and owner-safe verification of the normalized time/actual gauge bridge, the twisted author test/maximal/reduced records, four named nonretention outputs, the actual-to-standard support criterion, the selected component norm chain, and the gauge-covariant instantiation of a generic constant-diagonal corona lemma, together with sharp fixed-prime nonselectivity. In particular, the corona theorem is *generic after component isometries*; it is not an owner-specific obstruction dressed in packet notation.

fixes the owners and signs. verifies continuous trivialization and author transports. proves the four-output and support statements; proves the selected maximal/reduced component isometries. Only then does state the generic diagonal lemma and its typed instantiations. records the diagnostic and Route ceilings, and closes the NOTE scope.

# Owners, conventions, and source ceilings {#sec:owners}

Let $X$ be a nonempty set with a right action $(x,t)\mapsto x\mathbin{.}t$ of the usual locally compact group $\mathbb R$. Give $X$ the indiscrete topology. We use the range-first convention $$r(x,t)=x,\qquad s(x,t)=x\mathbin{.}t,\qquad
 (x,t)(x\mathbin{.}t,u)=(x,t+u),\qquad
 (x,t)^{-1}=(x\mathbin{.}t,-t).$$ The resulting actual action groupoid is $G_{\mathrm{actual}}(X)=X_{\mathrm{indisc}}\rtimes\mathbb R$. The coefficient group is $\mathbb T$ with trivial action. Time cochains live on $\mathbb R$ or $\mathbb R^2$; actual cochains live on the corresponding nerve charts of $G_{\mathrm{actual}}(X)$. The abstract gauge quotient is only an algebraic quotient: no quotient topology is asserted.

A continuous normalized time multiplier is a map $\sigma:\mathbb R^2\to\mathbb T$ satisfying $$\sigma(s,0)=\sigma(0,t)=1,
 \qquad
 \sigma(s,t)\sigma(s+t,u)=\sigma(t,u)\sigma(s,t+u).$$ For a continuous normalized $\alpha:\mathbb R\to\mathbb T$ we freeze $$\label{eq:gauge-direction}
 \sigma\,\overline\tau=\delta\alpha,
 \qquad
 (\delta\alpha)(s,t)=\alpha(s)\alpha(t)
 \overline{\alpha(s+t)},
 \qquad
 U_\alpha:A_\sigma\longrightarrow A_\tau.$$ This regularity is continuous/continuous. Kleppner's Section 7 supplies historical Borel multiplier and Borel similarity terminology only [@Kleppner1965Multipliers]; it is not a source for a continuous trivializer.

Suppose now that every orbit has a common cocompact stabilizer $H=L\mathbb Z$, $L>0$. Write $Q^{\mathrm{bare}}=X/\mathbb R$ for the *bare* orbit set; it has no topology. Paper 12 constructs $$\operatorname{Std}(X)=\coprod_{q\in Q^{\mathrm{bare}}}O_q,
 \qquad O_q\cong \mathbb R/H,
 \qquad G_{\mathrm{std}}(X)=\operatorname{Std}(X)\rtimes\mathbb R,$$ with every $O_q$ a compact Hausdorff torsor. The identity on arrows is a continuous functor $$J:G_{\mathrm{std}}(X)\longrightarrow G_{\mathrm{actual}}(X),$$ so functions pull back in the opposite direction, $J^*F=F\circ J$. The existence and componentwise topology of arbitrary topological coproducts are standard set-indexed facts [@Stacks0B1W Section 5.29 and Lemma 5.29.1]; that source supplies no action, count, measure, or completion theorem.

For each $q$ and $\epsilon\in\{\max,\mathrm r\}$, let $B_{q,\sigma}^{\epsilon}$ denote the separately defined twisted component record on $O_q\rtimes\mathbb R$. Set $$A_{\mathrm{std},\sigma}^{\epsilon}
   =\bigoplus_{q\in Q^{\mathrm{bare}}}^{c_0}B_{q,\sigma}^{\epsilon},
 \qquad
 M(A_{\mathrm{std},\sigma}^{\epsilon}),
 \qquad
 \operatorname{Cor}(A_{\mathrm{std},\sigma}^{\epsilon})
   =M(A_{\mathrm{std},\sigma}^{\epsilon})/
      A_{\mathrm{std},\sigma}^{\epsilon}.$$ No enumeration of $Q^{\mathrm{bare}}$ and no common origin for its torsors is chosen. The maximal and reduced symbols remain serialized; equality on a selected time image will not be promoted to equality of the whole component algebras.

P0.20P0.24YY Record & Topology & Analytic use & Firewall\
usual $\mathbb R$ & standard group topology & multiplier and time completions & no action-owner data\
$G_{\mathrm{actual}}(X)$ & indiscrete units; actual product topology & author global-QC test and transported norms & no standard groupoid $C^*$ name\
$Q^{\mathrm{bare}}$ & none & arbitrary index set & not $Q^{\mathrm{actual}}$ or $Q^{\mathrm{disc}}$\
$G_{\mathrm{std}}(X)$ & coproduct of compact torsors & component tests and $c_0$ assembly & no topology transfer from actual\
$B_{q,\sigma}^{\max}$, $B_{q,\sigma}^{\mathrm r}$ & one Hausdorff component & separately typed norms & selected images only\

(trace artifact `P13-TAB-01-OWNER-DICTIONARY`; package README, "Strict six-key artifact traces") fixes the owner, topology, analytic domain, and completion labels used below; in particular, it does not turn a selected-image comparison into an equality of ambient records.

The ordinary untwisted Hausdorff component bridge is supported by Buss--Holkar--Meyer, whose Corollary 6.2 removes the relevant second-countability dependence and whose Theorem 7.1 treats transformation groupoids [@BussHolkarMeyer2018Universal pp. 21, 23]. That source does *not* impose a second-countability obstruction here and supplies no twisted actual record. The audited Hausdorff *étale* framework of Austad--Ortega assumes second countability and does not apply to the nondiscrete one-object group $\mathbb R$ or to the actual owner [@AustadOrtega2022Uniqueness arXiv v1, pp. 1, 3]. Tu's convention is locally Hausdorff and likewise does not admit an actual owner with at least two indiscrete units [@Tu2004NonHausdorff Definition 1.1 and Definition 4.6]. Thus the correct ceiling is that these *named audited* frameworks do not apply to that actual owner---not that no framework exists.

Three quotient records must also remain distinct in the fixed-prime application. The set $Q_p^{\mathrm{actual}}$ carries the inherited indiscrete quotient topology; $Q_p^{\mathrm{bare}}$ is the same carrier with no topology; and $Q_p^{\mathrm{disc}}$ is the deliberately added discrete record used by the standard coproduct. A statement about one is not a statement about the other two. Likewise, "compact support" below means Hausdorff compact support on $G_{\mathrm{std}}(X)$, whereas the Paper 11 actual author test space uses its separately proved quasi-compact-support convention. This distinction explains why $J^*$ is always a continuous function pullback but need not take a nonzero actual author test function into the standard compact-support algebra.

The owner choices also delimit source use. The Hausdorff component sources justify ordinary components after a direct gauge transport, not a global actual theorem. The named comparator sources justify the displayed framework sentence, not an impossibility theorem. Finally, the abstract gauge quotient records equivalence classes only. No topology, Borel structure, Haar measure, or completion is placed on that quotient anywhere in this note.

The owner/pullback directions and the zero/finite/infinite support firewall are summarized in [\[fig:owner-support\]](#fig:owner-support){reference-type="ref" reference="fig:owner-support"} (trace artifact `P13-FIG-01-OWNER-SUPPORT`; package README, "Strict six-key artifact traces").

# Normalized twist collapse and author transports {#sec:twists}

Paper 12's all-degree factorization theorem gives unique time cochains $\alpha_0$ and $\sigma_0$ with $$\alpha(x,t)=\alpha_0(t),\qquad
 \Sigma((x,s),(x\mathbin{.}s,t))=\sigma_0(s,t).$$ This is an inherited premise, not a new factorization result. Direct substitution in the range-first nerve formulas shows that normalization, the cocycle equation, pointwise products, and $\sigma\overline\tau=\delta\alpha$ commute with pullback and evaluation. Consequently the actual and time normalized gauge quotients are algebraically identified, without transferring topology.

For clarity, write an actual degree-two cochain in range-first variables as $\Sigma(x;s,t)$. Factorization says $\Sigma(x;s,t)=\sigma_0(s,t)$, while an actual degree-one cochain is $a(x;t)=\alpha_0(t)$. The actual normalization $\Sigma(x;s,0)=\Sigma(x;0,t)=1$ is therefore exactly the time normalization. The actual cocycle identity on the composable triple $(x,s),(x\mathbin{.}s,t),(x\mathbin{.}(s+t),u)$ becomes $$\sigma_0(s,t)\sigma_0(s+t,u)
 =\sigma_0(t,u)\sigma_0(s,t+u).$$ Likewise, the actual coboundary becomes $\alpha_0(s)\alpha_0(t)\overline{\alpha_0(s+t)}$ with no inverse or source swap. These elementary evaluations are the entire typed bridge: Paper 12 owns factorization, while this note checks that the normalized operations respect it at the frozen convention.

The official abstract of Sorkin advertises continuous real-line multiplier triviality [@Sorkin1978Triviality]. The following proof is included because our normalization and the direction in [\[eq:gauge-direction\]](#eq:gauge-direction){reference-type="ref" reference="eq:gauge-direction"} must be checked directly; it is not presented as the original classification.

[\[thm:collapse\]]{#thm:collapse label="thm:collapse"} Every continuous normalized $\sigma:\mathbb R^2\to\mathbb T$ has a continuous normalized $\alpha:\mathbb R\to\mathbb T$ such that $\sigma=\delta\alpha$. Two trivializers differ by a continuous character of $\mathbb R$.

Lift $\sigma$ uniquely through $e^{i(\cdot)}:\mathbb R\to\mathbb T$ to a continuous $q:\mathbb R^2\to\mathbb R$ with $q(0,0)=0$. Normalization and connectedness make $q(s,0)=q(0,t)=0$ exactly. The lifted cocycle defect is continuous and $2\pi\mathbb Z$-valued on connected $\mathbb R^3$, hence zero. Thus $q$ is a normalized real cocycle. Its commutator $b(s,t)=q(s,t)-q(t,s)$ is continuous and additive in each variable. The continuous Cauchy equation gives $b(s,t)=\kappa st$; alternation gives $\kappa=0$, so $q$ is symmetric.

Choose $\rho\in C_c^\infty(\mathbb R)$ with $\int\rho=1$, define $h(s)=\int q(s,u)\rho(u)\,du$, and put $q_1=q-\delta h$. Then $$q_1(s,t)=\int_{\mathbb R}[q(s,t+u)-q(s,u)]\rho(u)\,du$$ has a jointly continuous second partial derivative. With $a(r)=\partial_2q_1(r,0)$, differentiation of the cocycle identity at the third variable $0$ yields $\partial_2q_1(s,t)=a(s+t)-a(t)$. If $A(t)=\int_0^t a(v)\,dv$, integration gives $q_1(s,t)=A(s+t)-A(s)-A(t)=\delta(-A)(s,t)$. Therefore $q=\delta(h-A)$ and $\alpha(t)=\exp(i(h(t)-A(t)))$ has the required normalization and sign. Finally, if $\delta\alpha=\delta\beta$, then $\chi=\beta/\alpha$ satisfies $\chi(s+t)=\chi(s)\chi(t)$; conversely every continuous character preserves the trivializer equation.

On $A_\sigma=C_c(\mathbb R)$ use the formulas audited for the usual time group [@Austad2021Spectral pp. 5--6]: $$\begin{aligned}
 (f*_{\sigma}g)(t)
   &=\int_{\mathbb R}f(u)g(t-u)\sigma(u,t-u)\,du,
   \label{eq:twisted-product}\\
 f^{*_{\sigma}}(t)
   &=\overline{\sigma(t,-t)}\,\overline{f(-t)}.
   \label{eq:twisted-star}\end{aligned}$$ The support inclusion $\operatorname{supp}(f*_{\sigma}g)\subseteq\operatorname{supp}(f)+\operatorname{supp}(g)$ gives closure. Absolute Fubini and the cocycle identity give associativity; the inverse-face identity gives both involution laws. If $\sigma\overline\tau=\delta\alpha$, direct cancellation in [\[eq:twisted-product,eq:twisted-star\]](#eq:twisted-product,eq:twisted-star){reference-type="ref" reference="eq:twisted-product,eq:twisted-star"} gives $$U_\alpha f(t)=\alpha(t)f(t),\qquad
 U_\alpha(f*_{\sigma}g)=U_\alpha f*_{\tau}U_\alpha g,
 \qquad U_\alpha(f^{*_{\sigma}})=(U_\alpha f)^{*_{\tau}}.$$

The sign in this gauge identity can be audited without shorthand. At the integrand pair $(u,t-u)$, [\[eq:gauge-direction\]](#eq:gauge-direction){reference-type="ref" reference="eq:gauge-direction"} is equivalent to $$\alpha(t)\sigma(u,t-u)
 =\alpha(u)\alpha(t-u)\tau(u,t-u),$$ which is precisely the factor needed on the two inputs to the $\tau$-product. At the inverse face it yields $\alpha(t)\overline{\sigma(t,-t)}=
\overline{\tau(t,-t)}\overline{\alpha(-t)}$, precisely the involution factor. Circle multiplication changes neither absolute values nor support. Thus the same identity controls product, star, support, and every later gauge square.

For associativity, the two iterated integrals are absolutely integrable because the three functions have compact support. After a change of variables places both expressions over $(u,v)$, their scalar factors are $\sigma(u,v)\sigma(u+v,t-u-v)$ and $\sigma(v,t-u-v)\sigma(u,t-u)$; the cocycle equation identifies them. For the star law, normalization and the cocycle identity at inverse faces give the required conjugate factor. These verifications occur on $C_c(\mathbb R)$ before any norm or completion is introduced.

The intrinsic projective left regular representation is $$(\lambda_\sigma(s)\xi)(t)=\sigma(s,t-s)\xi(t-s),
 \qquad
 \Lambda_\sigma(f)=\int_{\mathbb R}f(s)\lambda_\sigma(s)\,ds.$$ It satisfies $\lambda_\sigma(s)\lambda_\sigma(u)=
\sigma(s,u)\lambda_\sigma(s+u)$ and integrates to a $*$-representation. Multiplication by the trivializer intertwines it with the untwisted regular representation. We define the time maximal and reduced norms separately and only then use amenability of the usual group $\mathbb R$: Austad's exact endpoint is Proposition 2.4 on printed p. 7, cited there as a continuous specialization of Leptin's Satz 6 on printed p. 204 [@Austad2021Spectral; @Leptin1968Darstellungen]. Hulanicki's invariant-mean and weak-containment results provide group-level context [@Hulanicki1966Folner pp. 87--88] [@Hulanicki1964WeakContainment visible printed pp. 56--58]; the latter bibliography retains the official 27--59 pagination despite the official scan beginning visibly at p. 37. None of these sources proves an actual non-Hausdorff completion.

More explicitly, $M_\alpha\xi(t)=\alpha(t)\xi(t)$ satisfies $M_\alpha\lambda_\sigma(s)M_{\overline\alpha}
=\alpha(s)\lambda_1(s)$ when $\sigma=\delta\alpha$. After integration this is the same oriented gauge as $U_\alpha$. The reduced norm is $\lVert\Lambda_\sigma(f)\rVert$; the maximal norm is the supremum over the audited $L^1$-continuous $*$-representations. Gauge transport identifies each norm with its untwisted time counterpart, and amenability identifies the two time endpoints. This order is essential: amenability is not asserted for the actual owner, and equality is not inferred merely from the existence of a projective representation.

Paper 11 supplies the bijection $$\Phi_X:C_c(\mathbb R)\longrightarrow C_{\mathrm{glob}}(G_{\mathrm{actual}}(X)),
 \qquad \Phi_X(f)(x,t)=f(t),$$ whose actual support is $X\times\operatorname{supp}(f)$ and is quasi-compact at the actual owner. For $\Sigma=\pi_2^*\sigma$, we *define* the twisted author product, star, and both transported norms through $\Phi_X$. Hence $$\Phi_X(f)*_\Sigma\Phi_X(g)=\Phi_X(f*_{\sigma}g),
 \qquad
 \Phi_X(f)^{*_{\Sigma}}=\Phi_X(f^{*_{\sigma}}).$$ The word "define" is load-bearing. The actual topology makes every continuous separated-target scalar function depend only on time, and Paper 11 supplies the untwisted author support and completion contracts. Here we pull the proved time twist through that bijection and do not appeal to a general non-Hausdorff twisted groupoid construction. Support remains $X\times\operatorname{supp}(f)$ because neither a circle gauge nor $\Phi_X$ changes the zero set in the time variable. Associativity and both star laws therefore arrive only after their time formulas have been checked above.

The completed records $\mathrm{TW\!-!FULL\!-!TRANSPORT}_X(\Sigma)$ and $\mathrm{TW\!-!RED\!-!TRANSPORT}_X(\Sigma)$ are separate author records, even though the amenable time endpoint makes their transported norms agree on the common dense image. This construction deliberately does not name a global twisted groupoid $C^*$-algebra on $G_{\mathrm{actual}}(X)$.

If $\beta$ is another trivializer, then $\chi=\beta/\alpha$ is a continuous character. The two untwisted presentations consequently differ by the character automorphisms $U_\chi$ and $M_\chi$, so the transported normed records are choice-independent in the stated sense. This does not select a preferred trivializer, Fourier coordinate, or orbit origin. Nor does the time full/reduced equality license erasing the two author record names: their separate typing is retained for every later naturality square.

# Named nonretention and support transfer {#sec:support}

The gauge collapse has a precisely bounded nonretention consequence. Tags may record an owner and a chosen multiplier, but after those tags are forgotten only the four outputs in [\[tab:nonretention\]](#tab:nonretention){reference-type="ref" reference="tab:nonretention"} have a common value. This is trace artifact `P13-TAB-03-NONRETENTION` in the package README, "Strict six-key artifact traces."

[\[prop:four\]]{#prop:four label="prop:four"} Across the registered globally indiscrete right-real action owners, the tag-forgotten outputs `TIME-GAUGE`, `ACTUAL-TW-TEST`, `ACTUAL-TW-FULL`, and `ACTUAL-TW-RED` are constant. No claim is made about every invariant of the owner.

makes the time gauge class zero. The oriented maps $U_\alpha$ identify the time test records and extend isometrically to the two separately transported completions. Conjugating through the Paper 11 maps $\Phi_X$ gives inter-owner test, maximal, and reduced isomorphisms. These calculations account for exactly the registered rows and no others.

For two owners $X$ and $Y$, the test-level comparison is explicitly $\Phi_Y\Phi_X^{-1}$ after both twists have been transported to the common time record. The maximal comparison is the unique isometric extension of that map to the separately named maximal completions; the reduced comparison is constructed again on the separately named reduced completions. This is why the proposition is an inter-owner statement about four registered outputs rather than a claim that the actions themselves are isomorphic. Strict equivariant maps are natural because their pullbacks fix every time-only function $f(t)$.

P0.25YY Named output & Tag-forgotten value & Mandatory retention\
`TIME-GAUGE` & zero gauge class & literal owner and cochain tier\
`ACTUAL-TW-TEST` & common twisted test $*$-class & actual support convention\
`ACTUAL-TW-FULL` & common transported maximal class & maximal label\
`ACTUAL-TW-RED` & common transported reduced class & reduced label\

If $H_x\subset\mathbb R$ is a literal stabilizer, restriction of a globally trivial multiplier has zero class in the registered restricted continuous gauge quotient: $(\delta\alpha)|_{H_x}=\delta(\alpha|_{H_x})$. This does not erase $H_x$, its embedding, topology, period, clock, or representation theory. In the fixed-prime owner, Paper 9 retains $H=(\log p)\mathbb Z$ and period $\log p$; the scalar twist adds no registered restricted continuous cohomology-class invariant and therefore cannot recover $p$.

The restriction statement is intentionally cohomological rather than set-theoretic. It says that a class represented by $\delta\alpha$ remains a coboundary after applying the restriction map. It does not say that the subgroup $H_x$ becomes trivial, that two embedded lattices are equal, or that the quotient circle loses its marked period. In particular, characters of $H_x$ and representations built from the literal subgroup remain available even though this one continuous degree-two class vanishes.

We next compare actual quasi-compact support with standard compact support. For $f\in C_c(\mathbb R)$ put $K=\operatorname{supp}(f)$ and $\Psi_X(f)=J^*\Phi_X(f)$. Since $J$ is identity on the arrow carrier, $$\label{eq:support-product}
 \operatorname{supp}_{\mathrm{std}}\Psi_X(f)
   =\operatorname{Std}(X)\times K
   =\coprod_{q\in Q^{\mathrm{bare}}}(O_q\times K).$$

[\[thm:support\]]{#thm:support label="thm:support"} For a nonempty common-period owner, $$\Psi_X(f)\in C_c(G_{\mathrm{std}}(X))
 \quad\Longleftrightarrow\quad
 f=0\ \text{or}\ Q^{\mathrm{bare}}\ \text{is finite}.$$ If $Q^{\mathrm{bare}}$ is infinite and $T_X=J^*\Phi_X(C_c(\mathbb R))\subset C(G_{\mathrm{std}}(X))$, then $$T_X\cap C_c(G_{\mathrm{std}}(X))=\{0\}.$$ Every allowed circle gauge preserves this dichotomy.

For $f=0$, the support is empty. If $f\ne0$ and $Q^{\mathrm{bare}}$ is finite, [\[eq:support-product\]](#eq:support-product){reference-type="ref" reference="eq:support-product"} is a finite union of compact sets $O_q\times K$. If $Q^{\mathrm{bare}}$ is infinite, the nonempty component sets $O_q\times K$ form an open cover of the support with no finite subcover, so the support is not compact. Injectivity of $\Psi_X$ gives the intersection statement. Finally, a circle gauge $\alpha$ is nowhere zero, hence $\operatorname{supp}(\alpha f)=\operatorname{supp}(f)$.

Thus [\[eq:support-product,thm:support\]](#eq:support-product,thm:support){reference-type="ref" reference="eq:support-product,thm:support"} is exactly the support branch displayed in [\[fig:owner-support\]](#fig:owner-support){reference-type="ref" reference="fig:owner-support"} (trace artifact `P13-FIG-01-OWNER-SUPPORT`; package README, "Strict six-key artifact traces"); no topology or completion arrow is inferred from that schematic.

The product-support formula itself uses no countability. The nonzero locus of $\Psi_X(f)$ is $\operatorname{Std}(X)\times\{t:f(t)\ne0\}$, and for a nonempty space $Z$ one has $\overline{Z\times E}=Z\times\overline E$ in $Z\times\mathbb R$. This proves [\[eq:support-product\]](#eq:support-product){reference-type="ref" reference="eq:support-product"} directly, including the empty-support case. On an infinite coproduct, the component sets $O_q\times K$ are nonempty relatively open subsets of the support. Their cover has no finite subcover; no finite diagnostic, sequence of components, or limiting argument is being used.

For finite $Q^{\mathrm{bare}}$, direct substitution into the standard component convolution makes $\Psi_X$ an injective $*$-map onto the time-only unit-coordinate-constant test subalgebra. This optional finite branch is only a test-function statement: it yields no norm comparison or completion map. For infinite $Q^{\mathrm{bare}}$, the continuous pullback still exists, but no nonzero time-only actual test function lands in the standard compact-support test algebra.

# Selected component isometries {#sec:components}

Fix a compact standard orbit $O_q$ and $\epsilon\in\{\max,\mathrm r\}$. On the component test record use $$\begin{aligned}
 (F*_{\sigma}G)(x,t)
  &=\int_{\mathbb R}F(x,u)G(x\mathbin{.}u,t-u)
       \sigma(u,t-u)\,du,\\
 F^{*_{\sigma}}(x,t)
  &=\overline{\sigma(t,-t)}
       \overline{F(x\mathbin{.}t,-t)}.\end{aligned}$$ For these range-first coordinates the component $I$-norm is $$\lVert F\rVert_I=\max\left\{
 \sup_{x\in O_q}\int_{\mathbb R}|F(x,t)|\,dt,
 \sup_{x\in O_q}\int_{\mathbb R}|F(x\mathbin{.}t,-t)|\,dt
 \right\}.$$ The maximal record is the universal completion over $I$-norm-decreasing test representations. The reduced record is the completion for the supremum of the intrinsic unit-regular representations. If $\sigma\overline\tau=\delta\alpha$, then $U_{\alpha,q}F(x,t)=\alpha(t)F(x,t)$ preserves the component product, star, support, and $I$-norm. Taking $\tau=1$ transports the component record to the audited ordinary compact-orbit record without choosing a torsor origin; it also shows that both proposed completions exist.

The ordinary untwisted component owner is the transformation crossed product described by Buss--Holkar--Meyer, while Williams supplies the ordinary universal dense algebra, regular norms, homogeneous-space model, and amenable-action endpoint [@Williams2007CrossedProducts Lemma 2.27, Remarks 2.29--2.30, Theorem 4.30, and Theorem 7.13]. We do not use Williams's injective group-valued multiplier map as a $C^*$-faithfulness proof. Instead the following chain is direct.

Define the origin-free constant-in-the-unit map $$d_{q,\sigma}:C_c(\mathbb R)\longrightarrow C_c(O_q\rtimes\mathbb R,\sigma),
 \qquad d_{q,\sigma}(f)(x,t)=f(t).$$ Its support is $O_q\times\operatorname{supp}(f)$, compact because $O_q$ is compact; hence it really belongs to the component test algebra. Substitution shows that it preserves product and star, and nonemptiness of $O_q$ gives injectivity at test level. Notice what is not used: there is no basepoint of $O_q$, no identification of two different torsors, and no listing of components. The map is intrinsic because being constant in the unit variable is preserved by every equivariant translation.

For the component reduced norm, its every-unit regular representation is exactly $\Lambda_\sigma(f)$, so $$\label{eq:reduced-component}
 \lVert d_{q,\sigma}(f)\rVert_{B_{q,\sigma}^{\mathrm r}}
 =\lVert f\rVert_{C^*_{\mathrm r}(\mathbb R,\sigma)}.$$ Here the source fibre at $x$ is intrinsically parameterized by $t\mapsto(x\mathbin{.}(-t),t)$, and the corresponding regular action is $$[\operatorname{Reg}_{q,x,\sigma}(F)\xi](t)
 =\int_{\mathbb R}F(x\mathbin{.}(-t),u)\sigma(u,t-u)
       \xi(t-u)\,du.$$ Its kernel is bounded by Schur's test using the two terms of the displayed $I$-norm. Thus every unit-regular representation is among those dominated by the maximal norm. When $F=d_{q,\sigma}(f)$ the coefficient loses its unit variable and the formula becomes $\Lambda_\sigma(f)$ at every $x$, which proves the equality in [\[eq:reduced-component\]](#eq:reduced-component){reference-type="ref" reference="eq:reduced-component"}, not merely one inequality.

For the maximal norm, every component representation restricted along $d_{q,\sigma}$ is an $L^1(\mathbb R,\sigma)$-continuous $*$-representation; therefore $$\label{eq:max-component}
 \lVert d_{q,\sigma}(f)\rVert_{B_{q,\sigma}^{\max}}
 \leq \lVert f\rVert_{C^*_{\max}(\mathbb R,\sigma)}.$$

The maximal estimate also has the correct direction for a reason. On the constant-in-unit image, both terms of the component $I$-norm equal $\lVert f\rVert_1$. Therefore restriction of any representation counted by the component universal norm gives an admissible time representation. The time maximal norm is the supremum over all such time representations, so it dominates the restricted component norm. Faithfulness cannot be read off from a canonical group-valued multiplier map; it follows only after this upper bound is closed against the reduced lower endpoint.

[\[thm:component-isometry\]]{#thm:component-isometry label="thm:component-isometry"} For every $q$, $f\in C_c(\mathbb R)$, and separately for $\epsilon=\max$ and $\epsilon=\mathrm r$, $$\lVert d_{q,\sigma}(f)\rVert_{B_{q,\sigma}^{\epsilon}}
   =\lVert f\rVert_{C^*_{\epsilon}(\mathbb R,\sigma)}.$$ Thus $d_{q,\sigma}$ extends to an isometric faithful $*$-homomorphism $d_{q,\sigma}^{\epsilon}:C^*_{\epsilon}(\mathbb R,\sigma)
\to B_{q,\sigma}^{\epsilon}$ whose image lies in the component algebra.

Combine [\[eq:reduced-component,eq:max-component\]](#eq:reduced-component,eq:max-component){reference-type="ref" reference="eq:reduced-component,eq:max-component"}, domination of reduced by maximal norm, and amenability only at the time endpoint: $$\lVert f\rVert_{\mathrm{time},\max}
 \geq \lVert d_q(f)\rVert_{\mathrm{component},\max}
 \geq \lVert d_q(f)\rVert_{\mathrm{component},\mathrm r}
 =\lVert f\rVert_{\mathrm{time},\mathrm r}
 =\lVert f\rVert_{\mathrm{time},\max}.$$ Every inequality is equality. Completion gives the two isometries separately. If $f_n$ converges in the time completion, then $d_{q,\sigma}(f_n)$ converges inside $B_{q,\sigma}^{\epsilon}$, so the completed image is not merely a multiplier.

The theorem identifies only the selected time images. It gives neither $B_{q,\sigma}^{\max}=B_{q,\sigma}^{\mathrm r}$ nor a common origin across components, an orbit enumeration, or a globally named standard twisted groupoid completion.

Gauge covariance is already present at component level: $U_{\alpha,q}^{\epsilon}d_{q,\sigma}^{\epsilon}
=d_{q,\tau}^{\epsilon}U_\alpha^{\epsilon}$. Both sides are first equal on the dense test algebra and then extend by isometry. Because no origin was used in the regular fibre parameterization or in $d_{q,\sigma}$, changing a temporary presentation $O_q\cong\mathbb R/H$ by an equivariant translation fixes the constant-in-unit image. These facts will permit a coordinatewise diagonal without introducing simultaneous identifications among the components.

The selected-image qualification is substantive. A general component function depends on its unit coordinate, so its norm is not tested by the constant-in-unit restriction alone. The chain above proves the norm of $d_{q,\sigma}(f)$ exactly; it says nothing about a complementary subspace or about whether the canonical maximal-to-reduced quotient is injective on the entire component algebra. This is why both superscripts remain present in the diagonal construction below even though their time inputs have equal norms.

# Generic constant diagonals and typed instantiations {#sec:generic}

The next theorem is deliberately generic and occurs only after [\[thm:component-isometry\]](#thm:component-isometry){reference-type="ref" reference="thm:component-isometry"}. It contains no prime, packet, twist, orbit topology, common origin, or enumeration.

[\[thm:generic-diagonal\]]{#thm:generic-diagonal label="thm:generic-diagonal"} Let $I$ be a nonempty set, let $C$ and $B_i$ be $C^*$-algebras, and let $\varphi_i:C\to B_i$ be isometric $*$-homomorphisms. Put $A=\bigoplus_{i\in I}^{c_0}B_i$. Then $$M(A)\cong\prod_{i\in I}^{\mathrm{bounded}}M(B_i),
 \qquad
 \Delta(c)=(\varphi_i(c))_{i\in I}\in M(A)$$ defines an isometric faithful $*$-homomorphism $\Delta:C\to M(A)$. Moreover $$\Delta(c)\in A\quad\Longleftrightarrow\quad c=0\ \text{or}\ I\text{ is finite}.$$ If $I$ is infinite, then $$\lVert\Delta(c)+A\rVert_{M(A)/A}
   =\operatorname{dist}(\Delta(c),A)=\lVert c\rVert,$$ so the corona composite is isometric and faithful.

Recall that an arbitrary-index $c_0$ sum means $$A=\left\{(b_i):\sup_i\lVert b_i\rVert<\infty,
 \ \{i:\lVert b_i\rVert\geq\eta\}\text{ is finite for every }\eta>0
 \right\}.$$ This definition does not ask that $I$ be countable or enumerated. It also shows why the multiplier product in [\[thm:generic-diagonal\]](#thm:generic-diagonal){reference-type="ref" reference="thm:generic-diagonal"} must not be substituted for $A$: the bounded product is the multiplier algebra, while the $c_0$ condition continues to define the essential ideal.

Realize a multiplier of $A$ as a double centralizer $(L,R)$. Orthogonality of distinct coordinate ideals, tested against approximate identities, forces $(L,R)$ to preserve every $B_i$. Restriction gives a uniformly bounded family $(m_i)\in\prod_i M(B_i)$. Conversely, a uniformly bounded family acts coordinatewise on $A$ and preserves the condition that norms vanish at infinity. These assignments are inverse, and testing on a single coordinate shows that their norm is $\sup_i\lVert m_i\rVert$.

Since every $\varphi_i$ is isometric, $\sup_i\lVert\varphi_i(c)\rVert=\lVert c\rVert$. A constant-norm family is $c_0$ precisely when it is zero or the index set is finite. If $I$ is infinite and $b=(b_i)\in A$, then for every $\eta>0$ only finitely many $i$ satisfy $\lVert b_i\rVert\geq\eta$. Choose an index outside that set; then $\lVert\varphi_i(c)-b_i\rVert\geq\lVert c\rVert-\eta$. Taking the supremum, then $\eta\downarrow0$, gives the lower bound for the distance; $b=0$ gives the reverse bound.

The theorem separates a reusable operator-algebra fact from every later owner label. In particular, the equality of the quotient norm is proved by distance to the $c_0$ ideal, not inferred from the bare assertion that a class is nonzero. The zero, finite-index, and infinite-index cases are all part of the same generic statement.

That generic theorem, including its zero/finite/infinite branches and the subsequent separately typed maximal/reduced instantiations, is diagrammed in [\[fig:generic-diagonal\]](#fig:generic-diagonal){reference-type="ref" reference="fig:generic-diagonal"}. The reverse trace artifact is `P13-FIG-02-GENERIC-DIAGONAL`. Its locator is the package README, "Strict six-key artifact traces."

Now take $I=Q^{\mathrm{bare}}$, $C=C^*_{\epsilon}(\mathbb R,\sigma)$, and $\varphi_q=d_{q,\sigma}^{\epsilon}$ from [\[thm:component-isometry\]](#thm:component-isometry){reference-type="ref" reference="thm:component-isometry"}. The resulting isometry is $$D_\sigma^{\epsilon}:C^*_{\epsilon}(\mathbb R,\sigma)
 \longrightarrow M(A_{\mathrm{std},\sigma}^{\epsilon}),
 \qquad
 D_\sigma^{\epsilon}(a)=(d_{q,\sigma}^{\epsilon}(a))_q.$$ For the actual author record with $\Sigma=\pi_2^*\sigma$, let $\widehat\Phi_{X,\Sigma}^{\epsilon}$ be the completed Paper 11 transport and define only the named comparison $$\Delta_{X,\Sigma}^{\epsilon}
   =D_\sigma^{\epsilon}\circ
     (\widehat\Phi_{X,\Sigma}^{\epsilon})^{-1}.$$ This is a map from the named actual author record to the multiplier of the componentwise standard record; it creates no additional global completion.

The finite and infinite branches now follow without owner-specific argument. If $Q^{\mathrm{bare}}$ is finite, every diagonal lies in the $c_0$ sum and its corona image is zero. If $Q^{\mathrm{bare}}$ is infinite, a nonzero diagonal has the same positive norm in every coordinate, so it misses the $c_0$ sum and survives isometrically in the corona. This completed dichotomy is the exact analogue of the test-support split in [\[thm:support\]](#thm:support){reference-type="ref" reference="thm:support"}, but neither theorem is used as a proof of the other.

If $\sigma\overline\tau=\delta\alpha$, the component gauges assemble coordinatewise to $\mathcal U_\alpha^{\epsilon}:A_{\mathrm{std},\sigma}^{\epsilon}
\to A_{\mathrm{std},\tau}^{\epsilon}$, extend to multipliers, and descend to coronas. On test functions both sides equal $\alpha(t)f(t)$, so $$\begin{aligned}
 M(\mathcal U_\alpha^{\epsilon})D_\sigma^{\epsilon}
   &=D_\tau^{\epsilon}U_\alpha^{\epsilon},\\
 M(\mathcal U_\alpha^{\epsilon})\Delta_{X,\pi_2^*\sigma}^{\epsilon}
   &=\Delta_{X,\pi_2^*\tau}^{\epsilon}
       \widehat U_{\alpha,X}^{\epsilon}.\end{aligned}$$ The same squares commute after quotienting. Different trivializers differ by character automorphisms, so membership and corona norms are independent of that choice.

For a rational prime $p$, Paper 9 supplies the bare fixed-prime set $Q_p^{\mathrm{bare}}=U_p/H_p$ and Paper 2 supplies its hard continuum lower bound. This note adds only the elementary upper closure: there are countably many coordinates, each of cardinal at most $2^{\aleph_0}$, hence $|U_p|\leq(2^{\aleph_0})^{\aleph_0}=2^{\aleph_0}$. Thus $$|Q_p^{\mathrm{bare}}|=2^{\aleph_0}.$$ The actual quotient $Q_p^{\mathrm{actual}}$ remains indiscrete and second countable. Only the discrete record, standard coproduct, and standard arrow space acquire the corresponding non-second-countability and non-$\sigma$-compactness consequences. Those are direct coproduct consequences, not topology transferred from the actual quotient.

Indeed, the standard components are pairwise disjoint nonempty open sets, so a countable base cannot distinguish continuum many of them. Every compact subset of a coproduct meets only finitely many components, because the component opens cover it; consequently a countable union of compact subsets meets at most countably many components. This proves the stated non-second-countability and non-$\sigma$-compactness directly for the standard and discrete records while leaving the actual quotient unchanged.

[\[cor:prime\]]{#cor:prime label="cor:prime"} For every rational prime $p$, every continuous normalized $\sigma$, both $\epsilon=\max$ and $\epsilon=\mathrm r$, and every $a\in C^*_{\epsilon}(\mathbb R,\sigma)$, $$D_{p,\sigma}^{\epsilon}(a)\in
 A_{\mathrm{std},p,\sigma}^{\epsilon}
 \quad\Longleftrightarrow\quad a=0,
 \qquad
 \lVert D_{p,\sigma}^{\epsilon}(a)+A_{\mathrm{std},p,\sigma}^{\epsilon}\rVert
 =\lVert a\rVert.$$ The analogous statements hold for the named actual author map $\Delta_{\Gamma_p,\Sigma}^{\epsilon}$ and are gauge covariant.

The inherited cardinality makes $Q_p^{\mathrm{bare}}$ infinite. Apply the generic [\[thm:generic-diagonal\]](#thm:generic-diagonal){reference-type="ref" reference="thm:generic-diagonal"} separately to the two isometric families proved in [\[thm:component-isometry\]](#thm:component-isometry){reference-type="ref" reference="thm:component-isometry"}, then compose with the actual author transport.

The result is unconditional for each fixed prime and both completion types, but nonselective: every prime enters the same infinite-index branch. It cannot recover $p$ or $\log p$ and supplies no trace, determinant, zeta, analytic continuation, or spectral operator.

# Controls, Route, and limitations {#sec:controls}

The frozen replacement diagnostics passed 176 of 176 tests and produced 12 CSV files with 2,665 body rows, including 67 negative controls. The receipt covers 13 generated artifacts including the manifest, two fresh generations, and three byte-identical copies. These computations were not rerun during composition. They check finite sign, support, owner, gauge, and policy cases; they do not prove continuum cardinality, an arbitrary-index multiplier identity, the component norm chain, or corona faithfulness.

The reported tuple is the independently reviewed replacement run. A historical first-run implementation finding is not smuggled into the note as current evidence: the replacement generator, tests, reproduction script, manifest, and outputs were the tuple that received the effective zero-finding review. Serialization matters here as well. Because the composition gate forbids an unsolicited rerun, this manuscript reports the frozen receipt and does not compete for a supposed second execution of the control lane.

No control row is used as a scholarly citation or as a substitute for a proof locator.

The independent Route audit contains ten Route-A owner records: three are exploratory and seven rejected. Every A2, A3, and A4 coordinate fails; every determinant convention has the exact status $$\texttt{NONE\_BY\_DESIGN\_NO\_DETERMINANT\_OBJECT},$$ and Route B is false. Exploratory status records only a limited source relation, not determinant, spectral, or quantization evidence. The dated external comparison supports only the bounded phrase $$\texttt{SUPPORTED\_WITHIN\_SEARCH}$$ at the 15 August 2026 cutoff; it proves no firstness, priority, or standalone weight.

P0.17YY Layer & What it supports & What it cannot support\
Mathematical proof & sign-exact collapse, support criterion, selected isometries, generic diagonal and typed instances & topology transfer, whole-algebra equality, full-corona classification, prime selection\
Finite controls & regression, negative examples, manifest and owner-policy checks & continuum, arbitrary-index, norm, or faithfulness theorems\
Route audit & three exploratory and seven rejected owner dispositions & A2, A3, A4, determinant, zeta, spectral object, or Route-B promotion\
Source search & no exact package match in the bounded search & absence, novelty, priority, or standalone status\

The remaining boundary is explicit. We name no global actual twisted groupoid $C^*$-algebra; transfer no topology among actual, bare, standard, and discrete records; classify no full corona; and obtain no prime-sensitive invariant, trace, determinant, zeta object, analytic continuation, quantization, Hilbert--Pólya operator, or Route-B object. A literal stabilizer and its period remain even when the restricted gauge class is zero.

Mathematical proof, diagnostic execution, and Route policy are therefore three noninterchangeable evidence layers. A green regression row cannot replace an infinite-index argument; an exploratory Route status cannot turn a generic diagonal into a determinant; and a correct theorem cannot repair the retained standalone-positioning finding. (trace artifact `P13-TAB-04-LIMITATIONS`; package README, "Strict six-key artifact traces") records this separation so that later editing cannot collapse the layers into a single "pass" label.

# Conclusion {#sec:conclusion}

This Technical Note has one practical purpose: to make a chain of valid facts usable without changing their owners. The real-line twist collapses at the frozen gauge sign by a direct phase-lift and smoothing proof, and the resulting gauge maps transport the time test, maximal, and reduced records to the separately named actual author records. Four, and only four, registered tag-forgotten outputs are constant. Actual-to-standard pullback has the exact product-support formula, whose zero/finite/infinite split explains why an infinite standard coproduct contains no nonzero time-only compactly supported pullback.

The gain is precision rather than promotion: each arrow, norm, and quotient is now attached to the record on which it was actually proved.

The analytic order matters. Reduced and maximal component bounds are proved separately, amenability is used only at the usual time-group endpoint, and the resulting isometries concern selected time images rather than whole component algebras. Only after those isometries does the corona argument appear, as a reusable generic constant-diagonal lemma for arbitrary $c_0$-sums. The actual-author and fixed-prime statements are typed instantiations of that lemma. Their exact norm is useful bookkeeping, but their uniformity across primes is also their sharp limitation: they recover no arithmetic parameter.

That generic reduction is why the mathematics closes and why the retained standalone status does not change. The NOTE branch remains selected and `STANDALONE_PASS=false`. Finite controls and Route records support diagnosis and scope discipline only. Nothing here promotes the actual owner to an unaudited completion framework or constructs a trace, determinant, zeta function, analytic continuation, quantization, or spectral operator.

# Declarations and integrity status {#declarations-and-integrity-status .unnumbered}

**Author information, affiliations, correspondence, and CRediT roles:** **AUTHOR TO CONFIRM**.

**Funding, competing interests, and acknowledgments:** **AUTHOR TO CONFIRM**; no "none" declaration is inferred from silence.

**Data and code availability:** Local deterministic-control artifacts and reproduction scripts exist. Public repository coordinates, immutable tag, archive accession, DOI, and licences are **AUTHOR TO CONFIRM**.

**Ethics and consent:** The audited scope contains mathematical proof and deterministic finite controls, with no identified human, animal, or sensitive participant data. Venue-specific ethics and consent wording, including whether "not applicable" is accepted, is **AUTHOR TO CONFIRM**.

**Tool assistance and responsibility:** A tool-assisted research and composition workflow occurred; an AI system is not an author or mathematical authority. Venue-compliant disclosure wording and signed human responsibility for every claim and citation are **AUTHOR TO CONFIRM**.
