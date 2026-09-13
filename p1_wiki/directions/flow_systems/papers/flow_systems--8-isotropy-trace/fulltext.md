---
p1_kind: "derived-fulltext-reading-copy"
route: "flow_systems"
logical_paper_id: "flow_systems--8-isotropy-trace"
canonical_tex: "flow_systems/papers/8-isotropy-trace/paper/manuscript.tex"
canonical_pdf: "flow_systems/papers/8-isotropy-trace/paper/paper.pdf"
source_sha256: "c58392dcd2b92125ff46d9fbaee90d134210e36dbaa516fd359d89c08a6729fa"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Isotropy Averaging Erases Returns: Character Traces and a Fixed-Map Normality Obstruction on Deninger Prime Orbits

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../flow_systems/papers/8-isotropy-trace>)
- [规范 TeX](<../../../../../flow_systems/papers/8-isotropy-trace/paper/manuscript.tex>)
- [关联 PDF](<../../../../../flow_systems/papers/8-isotropy-trace/paper/paper.pdf>)
- [支撑 Markdown](<../../../../../flow_systems/papers/8-isotropy-trace/README.md>)
- [BibTeX](<../../../../../flow_systems/papers/8-isotropy-trace/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For an actual periodic orbit already chosen inside Deninger's finite-kernel prime packet, with primitive period $L=\log p$, we construct the continuous transformation groupoid and identify its full and reduced $C^*$-algebras with the same unstabilized algebra $C(\mathbb{T})\otimes\mathcal{K}(L^2[0,L))$. The isotropy character $\chi_\theta(rL)=\mathrm{e}^{\mathrm{i}r\theta}$ produces Floquet frequencies $(2\pi n-\theta)/L$ and the trace formula $$\tau_\theta(a_f)=L\sum_{r\in\mathbb{Z}}f(rL)\mathrm{e}^{\mathrm{i}r\theta},
   \qquad f\in C_c^\infty(\mathbb{R}).$$ In contrast, the Zak-decomposed source-fibre regular representation has bicommutant $L^\infty(\mathbb{T},\,\mathrm{d}\theta/(2\pi))\bar\otimes\mathcal{B}(L^2[0,L))$, and its faithful normal semifinite trace is $\mathrm{T}_L(a_f)=Lf(0)$: dual-Haar averaging erases every nonzero return. Each $\tau_\theta$ is a lower-semicontinuous, densely defined, semifinite, nonfaithful, unbounded $C^*$-trace, but a full finite rank-one corner proves that it has no normal extended-positive extension along this fixed one-orbit map. Thus the fixed local analogue is [refuted]{.smallcaps}. The packet-level question remains [not\_testable]{.smallcaps}, because packet Hausdorff/local-compactness and a same-map packet restriction or disintegration theorem are unavailable. Separately, closed-point counting gives the positive-time scalar Radon measure $\Theta_+=\sum_p\log p\sum_{r\geq1}\delta_{r\log p}$, so that typed scalar claim is a [pass]{.smallcaps}. Deterministic target-free controls verify signs, scales, finite-corner witnesses, and domain separation, but provide no packet, determinant, or spectral claim.

  **Keywords:** transformation groupoid; isotropy character; Plancherel trace; lower-semicontinuous trace; normal extension; Poisson summation; arithmetic dynamics
author:
- |
  Liang Wang\
  School of Artificial Intelligence and Automation\
  Huazhong University of Science and Technology (HUST)\
  <wangliang.f@gmail.com>
bibliography:
- references.bib
date: 14 August 2026
title: '**Isotropy Averaging Erases Returns: Character Traces and a Fixed-Map Normality Obstruction on Deninger Prime Orbits**'
```

## Markdown 正文

**中文摘要**

本文从 Deninger 有限核素数包中一个已经选定的真实周期轨道出发，并严格保留其本原周期 $L=\log p$。轨道作用群胚的满与约化 $C^*$-代数相同，且可具体写成未再稳定化的 $C(\mathbb{T})\otimes\mathcal{K}(L^2[0,L))$。各向同性特征 $\chi_\theta(rL)=\mathrm{e}^{\mathrm{i}r\theta}$ 导出 Floquet 频率 $(2\pi n-\theta)/L$ 以及带相位的返回梳状迹；平凡特征保留全部双向重复返回。与此相反，同一局部对象的源纤维正则表示经 Zak 分解后，其忠实正规半有限迹仅给出 $Lf(0)$，对偶 Haar 平均精确消去所有非零返回。有限满秩一角上的递减尖峰进一步表明，特征迹不能沿这一固定局部映射正规延拓，因此固定单轨道版本的结论为 [refuted]{.smallcaps}。由于原始素数包的 Hausdorff/局部紧致性以及包层面的同映射限制或分解桥梁尚未证明，包层面的主要问题仍为 [not\_testable]{.smallcaps}，而不能由局部反例替代。另一方面，按有理闭点计数所得的正时间标量测度 $\Theta_+=\sum_p\log p\sum_{r\geq1}\delta_{r\log p}$ 在紧集上局部有限，故这一严格分型的标量结论为 [pass]{.smallcaps}。文中的无目标控制只检查符号、归一化、角压缩和定义域边界；本文不提出包群胚完成、全素数算子、行列式、解析延拓或 Hilbert--Pólya 型结论。

**中文关键词：** 变换群胚；各向同性特征；Plancherel 迹；下半连续迹；正规延拓；Poisson 求和；算术动力系统

# Introduction

Deninger's rational-Witt construction associates to a rational closed point $(p)\subset\operatorname{Spec}\mathbb{Z}$ a packet of periodic trajectories whose common primitive period is $\log p$ [@Deninger2026 Section 6 and Theorem 6.1, arXiv-v4 pp. 38--39]; the compact-packet statement is also recorded in [@Deninger2023 Theorem 4.2, arXiv-v1 pp. 11--12]. This source fact suggests an operator-algebraic question that must be typed carefully: can the packet's common isotropy select a return-sensitive trace that is normal on a source-selected regular completion? Three logically separate answers emerge.

First, for one actual orbit that has already been chosen, the local operator problem is completely decidable. The groupoid algebra is $C(\mathbb{T})\otimes\mathcal{K}$; integration over the isotropy dual gives a faithful normal semifinite (FNS) trace, while evaluation at one isotropy character gives a lower-semicontinuous $C^*$-trace. The former retains only time zero and the latter retains a phase-weighted return comb. A full finite corner then proves that the character trace cannot extend normally through the fixed regular representation. The fixed one-orbit analogue is therefore [refuted]{.smallcaps}.

Second, the inherited packet is not interchangeable with one orbit. Its open-cover compactness and second countability are available, but the Hausdorff and locally compact Hausdorff (LCH) gates needed for the frozen standard groupoid completion are open. No restriction, compression, or disintegration theorem puts the local corner and a packet trace on one represented map. Consequently the packet-level question is [not\_testable]{.smallcaps}, not refuted. The distinction is mathematical rather than rhetorical: a normal-extension assertion has no truth value until both its domain map and codomain von Neumann algebra have been constructed.

Third, a scalar assembly does not require such a packet completion. There is one rational closed point $(p)$ for each prime, and its source clock is $L_p=\log p$. Counting these closed points once produces a locally finite positive-time Radon measure. This scalar result is a [pass]{.smallcaps}, but it is neither a packet trace nor a global all-prime operator.

## Contributions and verdict hierarchy

The central contribution is the fixed-map normality obstruction. Its force comes from comparing two traces on one exact local $C^*$-algebra and one exact embedding into a diffuse regular von Neumann algebra. The calculation also makes a structural loss visible: Plancherel averaging is normal precisely where it integrates over the character circle and annihilates every nonzero Fourier coefficient. The return-sensitive point fibre avoids that cancellation only by becoming nonnormal relative to the fixed regular completion.

The remaining contributions close the mathematical bookkeeping required to make that statement valid: an actual, unstabilized $C(\mathbb{T})\otimes\mathcal{K}$ completion; the sign-locked induced representations; trace-class Poisson summation; the Zak bicommutant and FNS domains; a corrected orbit-versus-packet topology split; a positive-time scalar ledger; and target-free falsification controls. records the adjudicated scope.

P0.08P0.19Y Y Target & Verdict & Proved content & Mandatory boundary\
P8-1 & split pass / [not\_testable]{.smallcaps}& Every chosen actual orbit closes; the packet has a free compact action and an open quasi-compact second-countable quotient. & Packet and quotient Hausdorff/LCH gates remain open.\
P8-2 & closed locally & $A_L\cong C(\mathbb{T})\otimes\mathcal{K}(H_0)$ as an actual unstabilized isomorphism. & The trivialization is choice-dependent and one-orbit only.\
P8-3 & closed locally & Trace-class Floquet fibres with frequency $(2\pi n-\theta)/L$ and phase $\mathrm{e}^{\mathrm{i}r\theta}$. & The symbolic proof, not finite controls, owns the sign.\
P8-4 & closed on fixed map & Zak bicommutant and FNS trace $\mathrm{T}_L(a_f)=Lf(0)$. & Normality and cancellation belong only to the fixed regular owner.\
P8-5 & closed locally & The l.s.c., densely defined, semifinite, nonfaithful character trace gives the full phase comb. & It is unbounded and not normal in the fixed regular completion.\
P8-6 & closed on fixed map & A full finite corner gives the no-normal-extension theorem; distinct singular corner-state extensions exist. & No full singular extension of the unbounded trace is constructed.\
P8-7 & scoped pass & Continuous orbit averaging and local/finite/positive-time scalar ledgers are valid on typed domains. & No packet Radon lift, packet trace, or same-map bridge.\
P8-8 & pass as controls & Eighteen target-free checks and nine deterministic CSV artifacts pass. & Finite checks are witnesses, not proofs.\
P8-9 & pass as audit & T0--T7 and Route coordinates are evaluated record by record. & No coordinate may be spliced across owners.\

## Prior mathematics, search boundary, and nonclaims

The operator-algebraic ingredients are classical. Green imprimitivity [@Green1978 Proposition 3, p. 203], transitive-groupoid equivalence [@MuhlyRenaultWilliams1987 Theorems 2.8 and 3.1, pp. 10 and 16], and the exact homogeneous-space specialization [@Williams2007 equation (4.63) and Theorem 4.30, p. 138] identify the local algebra. Stable isomorphism alone would be weaker [@BrownGreenRieffel1977 Theorem 1.2, pp. 351--352]; we do not cancel a stabilization. Amenability supplies full/reduced equality [@AnantharamanDelaroche2002 Examples 2.7(2) and Theorem 5.3]. Invariant-measure crossed-product traces, Plancherel weights, lower-semicontinuous traces, Morita induction, and normality criteria are available in [@BourneRennie2018; @Renault2021; @ElliottRobertSantiago2011; @CombesZettl1983; @Jones2009]. Our use of Poisson summation follows the Fourier convention of [@Laugesen2017 Definition 14.1 and Theorem 23.5].

The source-to-operator conjunction is stated only with a dated search boundary. To our knowledge, based on the arXiv, OpenAlex, Crossref-metadata, publisher/author-page, exact-web, and retained-full-text searches documented through 14 August 2026, we did not locate a primary paper that connects Deninger's rational-Witt finite-kernel prime packets to the continuous-$\mathbb{R}$ transformation-groupoid $C^*$/Plancherel construction or formulates the same fixed-object trivial-isotropy-character normality obstruction. This is support within the documented search, not an absolute priority claim. Generic groupoid imprimitivity, Plancherel theory, Poisson summation, and the singularity of point evaluation relative to diffuse $L^\infty$ are prior mathematics.

No determinant is defined here. There is no claim of analytic continuation, functional equation, Gamma factor, completed divisor, zero counting, Weil-form compression, natural quantization, Hilbert--Pólya operator, or [Route A]{.smallcaps} coordinate A3/A4. There is also no packet completion, no global all-prime $C^*$- or $L^1$-operator, no assertion of one orbit per packet, and no [Route B]{.smallcaps} invocation. The local refutation is not a packet refutation.

# Source object and the topology split

## An actual orbit, not a prescribed circle

Let $E_f$ denote the finite-kernel subsystem in Deninger's arithmetic dynamical construction. For a rational prime $p$, write $\Gamma_p$ for the corresponding inherited prime packet and put $$L=L_p=\log p.$$ Deninger's finite-kernel parametrization is given by equation (35) on arXiv-v4 p. 32, and his suspension theorem identifies the common isotropy as $p^{\mathbb{Z}}$, hence as $L\mathbb{Z}$ in additive time [@Deninger2026 equation (35), p. 32; Theorem 6.1, pp. 38--39]. We now make a choice that the source does not canonically make: fix one actual orbit $\mathcal O\subset\Gamma_p$.

[\[prop:orbit\]]{#prop:orbit label="prop:orbit"} The chosen inherited orbit $\mathcal O$, with its subspace topology and source flow, is homeomorphic to $\mathbb{R}/(L\mathbb{Z})$. Under the restricted Deninger--Morishita map, the flow orientation may reverse, but the absolute primitive period and isotropy remain $L$ and $L\mathbb{Z}$.

Morishita's target prime orbit is the Hausdorff circle $\mathbb{R}_+/p^{\mathbb{Z}}$, or $\mathbb{R}/(L\mathbb{Z})$ after logarithms [@Morishita2026 equation (1.1.5), p. 5]. His character/adelic map is continuous and becomes flow anti-equivariant after suspension [@Morishita2026 Lemmas 3.4--3.5, pp. 23--24]. The printed ambient statement cannot simply be imported: Remark 2.1.13 explicitly omits Deninger's character refinement, and the proof of Theorem 3.6 checks only the zero $p$-component [@Morishita2026 Remark 2.1.13, p. 13; Theorem 3.6 discussion, pp. 24--25]. Restrict instead to the genuine $E_f$ orbit. Deninger's exact isotropy makes the orbit map $\mathbb{R}/(L\mathbb{Z})\to\mathcal O$ bijective. Its composite with Morishita's restricted continuous map is the standard bijection to the Hausdorff target circle. The source orbit is compact in the inherited packet by Deninger's compact-orbit theorem [@Deninger2023 Theorem 4.2, pp. 11--12]; a continuous bijection from this compact circle to the inherited orbit, together with the continuous Hausdorff target separation, gives the asserted homeomorphism. Anti-equivariance only reverses the time parameter.

The proposition is a corrected source-specialized lemma, not Morishita's printed full-character homeomorphism. It proves no product chart for $\Gamma_p$, no canonical selection of $\mathcal O$, and no transverse measure.

## What is and is not known for the packet

Deninger's topology results give metrizable/Hausdorff pre-suspension stages under the stated hypotheses and continuous-bijection decompositions that need not be homeomorphisms [@Deninger2026 Propositions 7.4, 7.6, and 7.7; Corollaries 7.8--7.9; Theorem 7.10 and remarks, arXiv-v4 pp. 43--47]. After restriction to the admissible finite-kernel subsystem, those stage results persist, but they do not prove that the inherited suspended packet $\Gamma_p$ is Hausdorff. Accordingly, "compact" for $\Gamma_p$ below means open-cover compact, or quasi-compact, unless separation is stated.

The common isotropy lets the source flow descend to a continuous action of the compact group $$K_p=\mathbb{R}/(L\mathbb{Z})$$ on $\Gamma_p$. Exact isotropy makes this action free. Define the intrinsic orbit quotient $$q_p:\Gamma_p\longrightarrow Q_p:=\Gamma_p/K_p.$$ Because $q_p^{-1}(q_p(U))=\bigcup_{k\in K_p}U\cdot k$, the quotient map is open. The quotient is quasi-compact and second countable. However, neither $Q_p$ Hausdorffness nor a locally trivial $K_p$-bundle chart has been proved. In particular, $Q_p$ is not identified with a separately parametrized base $B_p$.

P0.28P0.22Y Property & Status & Consequence\
Actual chosen orbit $\mathcal O$ Hausdorff, compact, second countable, LCH & proved & Standard one-orbit groupoid theory applies.\
$\Gamma_p$ open-cover compact and second countable & proved & A genuine source packet exists, but separation is not supplied.\
$K_p$ action on $\Gamma_p$ continuous and free & proved & $Q_p=\Gamma_p/K_p$ is intrinsic.\
$q_p$ open; $Q_p$ quasi-compact and second countable & proved & Continuous orbit averages descend to the quotient.\
$\Gamma_p$ Hausdorff/LCH & open & The frozen standard packet groupoid completion is unavailable.\
$Q_p$ Hausdorff or locally trivial; $Q_p=B_p$ & open & No product chart or Radon disintegration may be imported.\
Packet same-map restriction/disintegration/compression & [not\_testable]{.smallcaps}& The local finite corner cannot be promoted to a packet obstruction.\

# The locked one-orbit groupoid and its exact completion

## Arrow convention, Haar system, and convolution

Identify $\mathcal O$ with $\mathbb{R}/(L\mathbb{Z})$, written additively, and let $x\cdot t=x+t\pmod L$. The transformation groupoid is $$G_L=\mathcal O\rtimes\mathbb{R}=\mathcal O\times\mathbb{R},$$ where $(x,t)$ is the arrow from $x$ to $x\cdot t$. Thus $$s(x,t)=x,\quad r(x,t)=x\cdot t,\quad
 (x,t)(x\cdot t,u)=(x,t+u),\quad
 (x,t)^{-1}=(x\cdot t,-t).$$ Lebesgue measure $\,\mathrm{d}t$ on each source fibre is a continuous Haar system. On $C_c(G_L)$ we freeze $$\begin{aligned}
 (F_1*F_2)(x,t)&=\int_{\mathbb{R}} F_1(x,s)F_2(x\cdot s,t-s)\,\mathrm{d}s,\label{eq:conv}\\
 F^{*}(x,t)&=\overline{F(x\cdot t,-t)}.\label{eq:star}\end{aligned}$$ The unit space is compact Hausdorff and second countable, so $G_L$ is LCH and second countable. Since $\mathbb{R}$ is amenable, its action is amenable; full and reduced norms coincide [@AnantharamanDelaroche2002 Examples 2.7(2) and Theorem 5.3].

## Actual unstabilized completion

Let $H=L\mathbb{Z}\subset\mathbb{R}$ be the isotropy subgroup and $H_0=L^2([0,L),\,\mathrm{d}u)$. Counting measure on $H$, Lebesgue measure on $\mathbb{R}$, and quotient length measure $\,\mathrm{d}u$ obey the quotient integral formula $$\int_{\mathbb{R}} g(t)\,\mathrm{d}t
 =\int_0^L\sum_{r\in\mathbb{Z}}g(u+rL)\,\mathrm{d}u.$$ This is the specialization of Williams's equation (4.63) [@Williams2007 p. 138].

[\[thm:completion\]]{#thm:completion label="thm:completion"} For the chosen actual orbit, $$A_L:=C^*(G_L)=C_r^*(G_L)
 \cong C^*(L\mathbb{Z})\otimes\mathcal{K}(H_0)
 \cong C(\mathbb{T})\otimes\mathcal{K}(H_0).$$ The isomorphism is actual and unstabilized. Its displayed continuous-field trivialization depends on the quotient section and compatible induction choices; it is not packet data.

The action is transitive and $\mathcal O\cong\mathbb{R}/H$. Green's theorem gives Morita equivalence with $C^*(H)$ [@Green1978 Proposition 3, p. 203], and the transitive groupoid equivalence theorem gives the corresponding compact-operator model [@MuhlyRenaultWilliams1987 Theorems 2.8 and 3.1]. The stronger statement needed here is Williams's homogeneous-space theorem: $$C_0(\mathbb{R}/H)\rtimes\mathbb{R}
 \cong C^*(H)\otimes\mathcal{K}(L^2(\mathbb{R}/H,\,\mathrm{d}u)),$$ with the quotient measure fixed above [@Williams2007 Theorem 4.30, p. 138]. It is already unstabilized. Pontryagin duality identifies $C^*(L\mathbb{Z})$ with $C(\widehat{L\mathbb{Z}})\cong C(\mathbb{T})$. Amenability gives the full/reduced equality. Brown--Green--Rieffel stable isomorphism [@BrownGreenRieffel1977 Theorem 1.2] is consistent with, but is not used to strengthen, the displayed result.

The algebraic centre of $C(\mathbb{T})\otimes\mathcal{K}(H_0)$ is zero because $H_0$ is infinite-dimensional. The continuous algebra $C(\mathbb{T})$ will reappear in a full finite rank-one corner, not as $Z(A_L)$. This distinction is essential in .

## Character convention

Parametrize $\widehat H$ by $\theta\in[0,2\pi)$ and freeze $$\chi_\theta(rL)=\mathrm{e}^{\mathrm{i}r\theta}.\label{eq:character}$$ The corresponding induced Hilbert space is realized by quasiperiodic functions satisfying $$\eta(u+rL)=\mathrm{e}^{-\mathrm{i}r\theta}\eta(u),\qquad u\in[0,L),\ r\in\mathbb{Z}.\label{eq:quasi}$$ An orthonormal Floquet basis is $$e_{n,\theta}(u)=L^{-1/2}\exp(\mathrm{i}k_{n,\theta}u),\qquad
 k_{n,\theta}=\frac{2\pi n-\theta}{L}.$$ The minus sign in $k_{n,\theta}$ and the plus sign in the eventual return phase are one coupled convention; changing only one is an error.

For $f\in C_c^\infty(\mathbb{R})$, let $a_f\in C_c(G_L)$ be the time kernel $a_f(x,t)=f(t)$. We use $$\widehat f(\xi)=\int_{\mathbb{R}} f(t)\mathrm{e}^{-\mathrm{i}t\xi}\,\mathrm{d}t.\label{eq:fourier}$$ In the induced representation $\pi_\theta$, translation by $t$ acts as $\eta(u)\mapsto\eta(u-t)$, so $$\pi_\theta(a_f)e_{n,\theta}
 =\widehat f(k_{n,\theta})e_{n,\theta}.\label{eq:diagonal}$$ The compatibility of Green induction with ordinary induced representations is Williams's Theorem 5.12 [@Williams2007 p. 161]; equations [\[eq:quasi\]](#eq:quasi){reference-type="eqref" reference="eq:quasi"}--[\[eq:diagonal\]](#eq:diagonal){reference-type="eqref" reference="eq:diagonal"} are its convention-locked specialization.

# Character traces and the shifted Poisson formula

## Trace class before the trace formula

Because $f\in C_c^\infty(\mathbb{R})$, repeated integration by parts makes $\widehat f$ rapidly decreasing [@Laugesen2017 Theorems 14.10--14.11, pp. 84--85]. Hence $$\sum_{n\in\mathbb{Z}}\left|\widehat f\left(\frac{2\pi n-\theta}{L}\right)\right|<\infty$$ uniformly in $\theta$. Thus $\pi_\theta(a_f)$ is trace class before its trace is taken. We write $$T_\theta(f):=\operatorname{Tr}(\pi_\theta(a_f)).$$

[\[thm:poisson\]]{#thm:poisson label="thm:poisson"} For $f\in C_c^\infty(\mathbb{R})$ and every $\theta\in[0,2\pi)$, $$T_\theta(f)
 =\sum_{n\in\mathbb{Z}}\widehat f\left(\frac{2\pi n-\theta}{L}\right)
 =L\sum_{r\in\mathbb{Z}}f(rL)\mathrm{e}^{\mathrm{i}r\theta}.\label{eq:poisson}$$ The two series are absolutely convergent. At $\theta=0$, every return has coefficient one.

Apply Poisson summation in the convention [\[eq:fourier\]](#eq:fourier){reference-type="eqref" reference="eq:fourier"} [@Laugesen2017 Theorem 23.5, p. 137] to the modulated function $t\mapsto f(t)\mathrm{e}^{\mathrm{i}\theta t/L}$, followed by the lattice rescaling $t\mapsto Lt$. Its Fourier transform at $2\pi n/L$ is $\widehat f((2\pi n-\theta)/L)$, while modulation contributes $\mathrm{e}^{\mathrm{i}r\theta}$ at $t=rL$. Rapid decay gives absolute convergence and justifies the rearrangement.

The theorem is local to an already selected orbit. It does not choose that orbit inside $\Gamma_p$, supply packet multiplicity, or construct a packet trace.

## The extended-positive $C^*$-traces

Fix a compatible induced-character trivialization $\Phi:A_L\to C(\mathbb{T})\otimes\mathcal{K}(H_0)$ from , satisfying $\Phi(a)(\theta)=\pi_\theta(a)$. Evaluation followed by the ordinary compact-operator trace defines $$\tau_\theta(a)=\operatorname{Tr}\bigl((\operatorname{ev}_\theta\otimes\operatorname{id})\Phi(a)\bigr),
 \qquad a\in(A_L)_+,\label{eq:taudef}$$ with values in $[0,\infty]$. The trace extends linearly to its trace ideal, which contains every $a_f$ above. Pullback of a lower-semicontinuous trace along a $^{*}$-homomorphism preserves lower semicontinuity and traciality [@ElliottRobertSantiago2011 Section 3.3 and Theorem 3.11, arXiv-v2 physical p. 12]; trace induction and semifiniteness are consistent with the Morita framework of [@CombesZettl1983 Proposition 2.2, pp. 72--73].

[\[prop:tau\]]{#prop:tau label="prop:tau"} Each $\tau_\theta$ is a lower-semicontinuous, densely defined, semifinite, nonfaithful, unbounded $C^*$-trace. On the time-kernel trace ideal, $$\tau_\theta(a_f)=L\sum_{r\in\mathbb{Z}}f(rL)\mathrm{e}^{\mathrm{i}r\theta},
 \qquad
 \tau_0(a_f)=L\sum_{r\in\mathbb{Z}}f(rL).$$

The standard trace on $\mathcal{K}(H_0)$ is lower semicontinuous, densely defined, and semifinite. Its pullback through the surjective fibre map has the same first three properties. Elementary continuous fields with finite-rank compact value form a dense trace-finite ideal. Nonfaithfulness follows by taking a nonzero positive field $g\otimes e$ with $g(\theta)=0$, and unboundedness follows from increasing finite-rank projections in the fibre. The time-kernel formula is .

# The fixed regular trace and exact cancellation

## Zak decomposition of the source-fibre representation

Let $m$ be normalized dual Haar measure, $$\,\mathrm{d}m(\theta)=\frac{\,\mathrm{d}\theta}{2\pi}.\label{eq:dualhaar}$$ This normalization is forced by Fourier isometry for counting Haar on $L\mathbb{Z}$, in accordance with the uniqueness principle for dual Haar measure and the Plancherel weight [@Renault2021 pp. 416--418]. It is not the orbit length measure $\,\mathrm{d}u$, nor the orbit probability $\,\mathrm{d}u/L$.

For $\xi\in C_c(\mathbb{R})$, define the Zak transform $$(Z\xi)(\theta,u)=\sum_{r\in\mathbb{Z}}\xi(u+rL)\mathrm{e}^{\mathrm{i}r\theta},
 \qquad 0\le u<L.\label{eq:zak}$$ Parseval on $\mathbb{Z}$, followed by the quotient integral formula, gives $$\int_{\mathbb{T}}\int_0^L |Z\xi(\theta,u)|^2\,\mathrm{d}u\,\mathrm{d}m(\theta)
 =\int_{\mathbb{R}}|\xi(t)|^2\,\mathrm{d}t.$$ Thus $Z$ extends to a unitary $$L^2(\mathbb{R})\longrightarrow\int_{\mathbb{T}}^{\oplus} H_0\,\mathrm{d}m(\theta).$$ Moreover $Z\xi(\theta,u+L)=\mathrm{e}^{-\mathrm{i}\theta}Z\xi(\theta,u)$, so its fibre is exactly the induced space in [\[eq:quasi\]](#eq:quasi){reference-type="eqref" reference="eq:quasi"}. Direct calculation on $C_c(G_L)C_c(\mathbb{R})$ shows that $Z$ intertwines the source-fibre regular representation $\lambda_L$ with $\int_{\mathbb{T}}^{\oplus}\pi_\theta\,\mathrm{d}m(\theta)$.

[\[thm:fns\]]{#thm:fns label="thm:fns"} The source-fibre regular representation is faithful and, under the same Zak trivialization, $$M_L^{\mathrm{reg}}:=\lambda_L(A_L)''
 =L^\infty(\mathbb{T},m)\,\bar\otimes\,\mathcal{B}(H_0).\label{eq:bicommutant}$$ The weight $$\mathrm{T}_L(X)=\int_{\mathbb{T}}\operatorname{Tr}(X(\theta))\,\mathrm{d}m(\theta),\qquad X\in(M_L^{\mathrm{reg}})_+,\label{eq:fns}$$ is faithful, normal, and semifinite. For $f\in C_c^\infty(\mathbb{R})$, and more generally on the stated bounded $L^1$ time-kernel domain, $$\mathrm{T}_L(\lambda_L(a_f))=Lf(0).\label{eq:regular}$$

Faithfulness follows from full/reduced equality and the faithful regular realization. The Zak unitary makes $C(\mathbb{T})\otimes\mathcal{K}(H_0)$ act as continuous compact-operator fields. Its bicommutant is the decomposable algebra in [\[eq:bicommutant\]](#eq:bicommutant){reference-type="eqref" reference="eq:bicommutant"}; the model $vN(\mathbb{Z})=L^\infty(\mathbb{T},m)$ and its identity-coefficient trace are standard [@Jones2009 pp. 15--16]. The tensor product of integration against $m$ and the ordinary trace is FNS. On a positive field, Tonelli gives [\[eq:fns\]](#eq:fns){reference-type="eqref" reference="eq:fns"}; the square-integrable and trace-ideal domains are the usual ones. On a complex time kernel whose fibre trace norms are integrable, Fubini and give $$\begin{aligned}
 \mathrm{T}_L(\lambda_L(a_f))
 &=\int_{\mathbb{T}} L\sum_{r\in\mathbb{Z}}f(rL)\mathrm{e}^{\mathrm{i}r\theta}\,\mathrm{d}m(\theta)\\
 &=L f(0),\end{aligned}$$ because $\int_{\mathbb{T}}\mathrm{e}^{\mathrm{i}r\theta}\,\mathrm{d}m(\theta)=0$ for $r\ne0$. The same equality on the bounded $L^1$ kernel domain follows first on the dense smooth core and then by the trace-norm estimate.

The construction is the fixed one-orbit analogue of standard invariant-measure traces on continuous crossed products [@BourneRennie2018 Proposition 3.2 and Lemma 7.4]. It does not identify a packet representation. Normality of $\mathrm{T}_L$ and full/reduced equality are separate facts.

P0.23Y Y Field & Regular trace $\mathrm{T}_L$ & Character trace $\tau_\theta$\
Owner & $M_L^{\mathrm{reg}}=L^\infty(\mathbb{T},m)\bar\otimes\mathcal{B}(H_0)$ & $A_L\cong C(\mathbb{T})\otimes\mathcal{K}(H_0)$\
Type & faithful normal semifinite & l.s.c., densely defined, semifinite, nonfaithful, unbounded $C^*$-trace\
Selection & integrates all characters using $m=\,\mathrm{d}\theta/(2\pi)$ & evaluates one character $\theta$\
Time kernel & $Lf(0)$ & $L\sum_r f(rL)\mathrm{e}^{\mathrm{i}r\theta}$\
Nonzero returns & all erased & retained with phase; all have weight one at $\theta=0$\
Completion relation & native FNS owner & no normal extension along the fixed map\

# The full finite-corner normality obstruction {#sec:corner}

## The same projection in the same represented map

Choose a rank-one projection $e\in\mathcal{K}(H_0)$ and set $$q=1_{C(\mathbb{T})}\otimes e\in A_L.$$ This projection is full because $e$ is full in $\mathcal{K}(H_0)$, and it is trace-finite for every character: $$qA_Lq\cong C(\mathbb{T}),\qquad \tau_\theta(q)=1.$$ Under the fixed regular embedding $\iota:A_L\hookrightarrow M_L^{\mathrm{reg}}$, the same projection satisfies $$qM_L^{\mathrm{reg}}q\cong L^\infty(\mathbb{T},m).$$ This is a corner statement, not a centre statement.

[\[thm:normal\]]{#thm:normal label="thm:normal"} For every $\theta\in\mathbb{T}$, there is no normal extended-positive weight $W$ on $M_L^{\mathrm{reg}}$ such that $$W(\iota(a))=\tau_\theta(a)\qquad\text{for all }a\in(A_L)_+.$$ Equivalently, the character trace has no normal extension along this fixed one-orbit regular map.

Suppose $W$ exists. Since $W(q)=\tau_\theta(q)=1$, compression gives a finite normal positive functional $\omega(x)=W(qxq)$ on $qM_L^{\mathrm{reg}}q\cong L^\infty(\mathbb{T},m)$. On the continuous corner it agrees with point evaluation at $\theta$.

Let $d$ be circular distance and define continuous peaks $$h_n(z)=\max\{1-n d(z,\theta),0\},\qquad n\ge1.$$ Then $0\le h_{n+1}\le h_n\le1$, $h_n(\theta)=1$, and $h_n\downarrow0$ $m$-almost everywhere because singletons have Haar measure zero. Normality is order continuity on bounded decreasing positive sequences [@Jones2009 Definition 7.1.2 and Theorem 7.1.3, pp. 43--44], so $$\omega(h_n)\downarrow0.$$ But agreement with the continuous corner gives $\omega(h_n)=h_n(\theta)=1$ for every $n$, a contradiction.

The theorem refutes only the one-orbit normal-extension analogue. A packet-level refutation would require a packet algebra, a represented packet map, and a theorem carrying this same projection through restriction, compression, or disintegration. None is available.

## What singular extension does mean here

The phrase "point evaluation on $L^\infty$" is ill-posed because $L^\infty$ consists of almost-everywhere equivalence classes. Nevertheless, the state $g\mapsto g(\theta)$ on the embedded $C(\mathbb{T})$ has state extensions to $L^\infty(\mathbb{T},m)$ by positive Hahn--Banach extension. Every such extension is singular by the peak argument above.

[\[prop:singular\]]{#prop:singular label="prop:singular"} There are at least two distinct singular states on $qM_L^{\mathrm{reg}}q\cong L^\infty(\mathbb{T},m)$ whose restrictions to $qA_Lq\cong C(\mathbb{T})$ are evaluation at $\theta$.

Choose a measurable set $E$ formed from alternating annuli shrinking to $\theta$, so both $E$ and $E^c$ meet every neighbourhood of $\theta$ in positive Haar measure. In the measure algebra, the neighbourhood filter of $\theta$ can be enlarged consistently either by $E$ or by $E^c$. Extend each to an ultrafilter. The corresponding characters of the abelian $C^*$-algebra $L^\infty(\mathbb{T},m)$ agree with $g(\theta)$ for every continuous $g$, because the ultrafilters converge through all neighbourhoods of $\theta$, but they take different values on $1_E$. Neither character is normal by .

These are extensions only of the finite-corner state. We construct no singular extended-positive tracial extension of the full unbounded $\tau_\theta$.

# The packet and quotient boundary

The local proof is now complete, so we can state exactly why it does not decide the primary packet question. The natural topological action groupoid $\Gamma_p\rtimes\mathbb{R}$ exists as a set and topological category. The standard $C^*$-completion frozen for this project, however, requires the relevant LCH/Hausdorff hypotheses. Those hypotheses have not been proved for $\Gamma_p$. Replacing it by a product proxy would supply the missing topology by definition and would change the object being tested.

[\[prop:quotient\]]{#prop:quotient label="prop:quotient"} The compact group $K_p=\mathbb{R}/(L\mathbb{Z})$ acts continuously and freely on $\Gamma_p$; the quotient map $q_p:\Gamma_p\to Q_p$ is open; and $Q_p$ is quasi-compact and second countable. For every $\varphi\in C(\Gamma_p)$, $$(\mathcal A_p\varphi)(x)=\frac1L\int_0^L\varphi(x\cdot t)\,\mathrm{d}t\label{eq:average}$$ is continuous and $K_p$-invariant, hence descends to a continuous function on $Q_p$. These assertions do not prove that $Q_p$ is Hausdorff, locally trivial, or equal to a parametrizing base, and [\[eq:average\]](#eq:average){reference-type="eqref" reference="eq:average"} is not a packet Radon-measure or trace theorem.

Continuity of the residual action follows from the source flow, and freeness follows from exact common isotropy $L\mathbb{Z}$. Openness of $q_p$, quasi-compactness, and second countability were established in Section 2. Joint continuity of the action and compactness of $K_p$ imply continuity of the integral in [\[eq:average\]](#eq:average){reference-type="eqref" reference="eq:average"}; Haar invariance makes it constant on orbits. None of these steps chooses a Borel probability on $Q_p$ or lifts one through a Radon disintegration.

Even if a Borel probability on $Q_p$ were given, the resulting averaging functional would depend on that extra choice for transverse observables. The source does not select such a probability, prove exhaustion of invariant measures, or choose cross-prime masses. Packet topology and the packet same-map bridge therefore remain [not\_testable]{.smallcaps}. This is the endpoint of the packet branch in this paper.

# Scalar ledgers and target-free controls

## Local, finite, and positive-time objects

For a prime $p$ define the two-sided local scalar return distribution $$R_p=L_p\sum_{r\in\mathbb{Z}}\delta_{rL_p},\qquad L_p=\log p.\label{eq:Rp}$$ On one chosen orbit, $R_p(f)=\tau_0(a_f)$. This equality is only a local trace restriction. For a finite prime set $S$, the sum $R_S=\sum_{p\in S}R_p$ is a finite scalar distribution; it is not a direct-sum operator unless an operator and its domain are separately supplied.

The all-prime object must exclude time zero. Define $$\Theta_+=\sum_{p\ \mathrm{prime}}\log p\sum_{r\ge1}\delta_{r\log p}
 \quad\text{on }(0,\infty).\label{eq:theta+}$$

[\[thm:scalar\]]{#thm:scalar label="thm:scalar"} The expression [\[eq:theta+\]](#eq:theta+){reference-type="eqref" reference="eq:theta+"} defines a positive locally finite Radon measure on $(0,\infty)$. Its coefficient one is the counting multiplicity of the rational closed point $(p)$, and its factor $\log p$ is the orbit length. It is not a packet-orbit multiplicity, a packet trace, or a global $C^*$- or $L^1$-operator trace.

Let $K\subset(0,\infty)$ be compact, with $K\subset[a,b]$ and $a>0$. A term $r\log p\in K$ implies $p\le\mathrm{e}^b$, so only finitely many primes occur. For each such prime, $1\le r\le b/\log p$, so only finitely many repetitions occur. Hence $\Theta_+(K)<\infty$. Positivity and local finiteness on the locally compact space $(0,\infty)$ give a Radon measure. The indexing uses the unique rational closed point $(p)$ once; Deninger's clock supplies $\log p$. No statement about the number of orbits in $\Gamma_p$ enters the proof.

At time zero, summing $L_p\delta_0$ over all primes has infinite mass. The positive-time restriction is therefore a mathematical domain condition, not a cosmetic cutoff.

P0.22P0.25Y Y Object & Domain & Proved meaning & Forbidden promotion\
$R_p$ & one prime, all $r\in\mathbb{Z}$ & scalar distribution; local $\tau_0(a_f)$ restriction & not a packet trace\
$R_S$ & finite $S$, all $r\in\mathbb{Z}$ & finite scalar sum & not a global direct-sum operator\
$\Theta_+$ & all primes, $r\ge1$, time $>0$ & positive locally finite Radon measure & not an all-prime $C^*/L^1$ trace\
All-prime two-sided sum & includes $r=0$ & infinite mass at zero & not defined as a Radon measure on all time\

## Generic clocks and ownership

The local compiler is not arithmetically unique. For every $L>0$, the circle $\mathbb{R}/(L\mathbb{Z})$ has the same groupoid completion and the same character/regular trace split. Composite labels and arbitrary positive clock families also reproduce the analytic formulas. What distinguishes [\[eq:theta+\]](#eq:theta+){reference-type="eqref" reference="eq:theta+"} is source provenance: rational closed points of $\operatorname{Spec}\mathbb{Z}$ are indexed by primes, not composites, and Deninger's theorem supplies $L_p=\log p$ before any target comparison.

[\[prop:generic\]]{#prop:generic label="prop:generic"} For any locally finite positive clock family $\{\ell_j\}$ and assigned nonnegative weights $w_j$, the positive-time expression $\sum_jw_j\sum_{r\ge1}\delta_{r\ell_j}$ is locally finite under the corresponding properness condition. Copying a component adds its weight, and composite clocks remain analytically valid. Therefore local finiteness and the one-orbit character formula alone do not establish arithmetic provenance.

The proposition is a falsification boundary: the actual prime record retains arithmetic ownership because its labels and clocks are source-derived; the generic compiler does not grant such ownership to controls.

## Deterministic controls

The accompanying standard-library Python suite contains no randomness, network dependency, external dataset, Riemann-zero data, Euler-target comparison, fitted phase, fitted clock, fitted mass, or fitted transverse probability. The reproduction script ran 18 tests and generated nine CSV artifacts with 129 data rows; two fresh generations were byte-identical. The locked result-manifest SHA-256 is $$\texttt{20801ebe4c927f939c462842e38569555f96f5fef78859755b6caa8cbcf38b07}.$$

P0.29Y Y Control & What it detects & What it does not establish\
Shifted Poisson and nontrivial phase & coupled minus frequency / plus return-phase convention & infinite Poisson theorem\
Finite character grid & exact cancellation of represented nonzero modes & Haar-integration theorem\
Trivial versus regular; zero time & comb versus $Lf(0)$, with zero exposed & equality or normality of traces\
Common length/probability scale & both traces rescale together by $1/L$ & independently fitted normalization\
Rank-one peaks and representatives & point value survives as Haar mass vanishes; a.e. classes matter & bicommutant or normality proof\
Transverse probabilities & time-only blindness and transverse-observable variation & a canonical packet probability\
Copied/arbitrary/composite clocks & additivity and genericity of the compiler & arithmetic provenance\
Local/finite/positive-time domains & rejects zero-time and all-prime operator conflation & global operator existence\

# Same-object and Route audit

## T0--T7 ownership

The T0--T7 discipline prevents a proof on one owner from repairing a missing field on another. T0--T2 record source identity, topology, and clock; T3--T5 record groupoid/Haar, measure, and representation/trace ownership; T6 records the formula and its domain; T7 records arithmetic promotion and coefficient ownership.

P0.30Y Record & Exact [Route A]{.smallcaps} tuple and T0--T7 typed status\
`DEN-EF-PACKET-ACTION-GRPD-P` & `` `` `` `` ``

Actual packet/clock pass partially; packet T1 and T3--T6 are open or [not\_testable]{.smallcaps}; T7 owns only the prime label and clock.\
`DEN-EF-ORBIT-ACTION-GRPD` & `` `` `` `` ``

A chosen actual orbit owns local T0--T5 and the local formulas; no packet selection, multiplicity, or cross-prime trace mass.\
`DEN-EF-ORBIT-GRPD-REG-TRACE` & `` `` `` `` ``

Fixed FNS owner; T6 is $Lf(0)$, so nonzero-return A1 is refuted for this trace.\
```` & `` `` `` `` ``

Local l.s.c. trace owns the phase comb and the fixed-map obstruction; no packet mass or normality.\
`DEN-EF-GRPD-TIME-RETURN-POS` & `` `` `` `` ``

Scalar type: T3--T5 are N/A, while positive-time T6 and coefficient-one closed-point T7 pass.\

Every record has overall verdict `ROUTE_A_EXPLORATORY`. All five have A2, A3, and A4 equal to `FAIL`; no record owns a determinant, global analytic structure, or natural quantization. Every final YAML sets `route_b_invocation_allowed=false`, and there is no [Route B]{.smallcaps} record.

The anti-splice rules are immediate from . The packet cannot borrow the orbit's LCH completion. The regular trace cannot borrow the character trace's return comb. The character trace cannot borrow the regular trace's normality. The scalar ledger cannot borrow either local operator or a packet completion. A coordinatewise maximum over these rows would describe no mathematical object.

# Limitations and conclusion

The strongest conclusion is local and negative in a precise sense. For one already chosen actual Deninger prime orbit, the trivial-isotropy-character trace is a rigorous lower-semicontinuous, densely defined, semifinite, nonfaithful, unbounded $C^*$-trace with the entire return comb, but it has no normal extended-positive extension along the fixed Zak-regular map. The finite corner is full and trace-finite, so the obstruction is not caused by choosing a negligible algebraic ideal. It is caused by the incompatibility between point-character sensitivity and normality over diffuse dual Haar.

The regular FNS trace is equally rigorous but answers a different question. It averages the character field and returns $Lf(0)$. Its cancellation of every nonzero return is exact, not numerical. Normality therefore does not coexist with the desired return sensitivity on this fixed local completion.

The primary packet question remains [not\_testable]{.smallcaps}. This paper does not prove $\Gamma_p$ or $Q_p$ Hausdorff/LCH, a packet groupoid $C^*$-completion, a source-selected transverse probability, packet Radon disintegration, packet trace, or a same-map bridge transporting the local corner. Closing packet Hausdorff/LCH would still leave measure selection and same-map transport as separate problems. The next smallest topological test is whether the restricted diagonal equivalence relation defining one $\Gamma_p$ is closed.

The positive-time scalar ledger is a separate [pass]{.smallcaps}. It is locally finite because compact positive-time support sees finitely many primes and repetitions, and coefficient one belongs to rational closed-point counting. It is not evidence that a packet contains one orbit and not an all-prime operator trace.

Finally, the generic-clock controls show why scope matters: the local compiler works for arbitrary and composite clocks. Arithmetic provenance enters through the source closed points and their $\log p$ clocks, not through the analytic mechanism alone. No determinant, A3 or A4 structure, [Route B]{.smallcaps}, global spectral operator, or Hilbert--Pólya claim follows.

# Locked crossed-product convention

Write $y-t$ for $y\cdot(-t)$ on $\mathcal O$, and set $$\alpha_tg(y)=g(y-t),\qquad F_a(t)(y)=a(y-t,t).$$ Then $a\mapsto F_a$ carries the convolution and involution in [\[eq:conv\]](#eq:conv){reference-type="eqref" reference="eq:conv"} to those of $C(\mathcal O)\rtimes_\alpha\mathbb{R}$: directly, $$\begin{aligned}
 (F_a*F_b)(t)(y)&=\int_{\mathbb{R}}a(y-v,v)b(y-t,t-v)\,\,\mathrm{d}v=F_{a*b}(t)(y),\\
 F_{a^{*}}(t)(y)&=\overline{a(y,-t)}=\alpha_t(F_a(-t)^{*})(y).\end{aligned}$$ This is the crossed-product bridge used by the completion and representation arguments, and it is compatible with [\[eq:character\]](#eq:character){reference-type="eqref" reference="eq:character"}--[\[eq:diagonal\]](#eq:diagonal){reference-type="eqref" reference="eq:diagonal"}. Quotient length Haar has mass $L$, while orbit probability is $\,\mathrm{d}u/L$. Passing to probability scale divides both $\mathrm{T}_L$ and every $\tau_\theta$ by the same $L$.

# Zak Parseval and dense-core identities

For $\xi,\zeta\in C_c(\mathbb{R})$, Fourier orthogonality gives $$\begin{aligned}
 \int_{\mathbb{T}}\int_0^L (Z\xi)(\theta,u)\overline{(Z\zeta)(\theta,u)}\,\mathrm{d}u\,\mathrm{d}m(\theta)
 &=\int_0^L\sum_{r\in\mathbb{Z}}\xi(u+rL)\overline{\zeta(u+rL)}\,\mathrm{d}u\\
 &=\langle\xi,\zeta\rangle_{L^2(\mathbb{R})}.\end{aligned}$$ The compact-support assumption makes the pointwise sums finite; density gives the unitary extension. Intertwining is checked first for $F\in C_c(G_L)$ and $\xi\in C_c(\mathbb{R})$, where all integrations are absolutely convergent, and then extended by continuity. In each fibre, [\[eq:diagonal\]](#eq:diagonal){reference-type="eqref" reference="eq:diagonal"} implies $$\|\pi_\theta(a_f)\|_2^2
 =\sum_{n\in\mathbb{Z}}\left|\widehat f\left(\frac{2\pi n-\theta}{L}\right)\right|^2,$$ and integrating over $m$ unfolds the shifted intervals to the Fourier Plancherel integral with the locked normalization.

# FNS and complex trace domains

For $X\in(M_L^{\mathrm{reg}})_+$, [\[eq:fns\]](#eq:fns){reference-type="eqref" reference="eq:fns"} is defined without assuming finiteness. Its finite cone is $$\mathfrak M_{\mathrm{T}_L}^+=\left\{X\ge0:\int_{\mathbb{T}}\operatorname{Tr}(X(\theta))\,\mathrm{d}m(\theta)<\infty\right\}.$$ The square-integrable left ideal is $$\mathfrak N_{\mathrm{T}_L}=\{X:\mathrm{T}_L(X^*X)<\infty\},$$ and the complex trace ideal is the linear span of products $Y^*X$ with $X,Y\in\mathfrak N_{\mathrm{T}_L}$. Formula [\[eq:regular\]](#eq:regular){reference-type="eqref" reference="eq:regular"} for complex $a_f$ is asserted only after membership in this ideal, supplied by uniform rapid decay for $C_c^\infty$ kernels. The bounded $L^1$ extension means kernels for which the represented field is bounded and the fibre trace norm is $m$-integrable; it is not an all-prime $L^1$ claim.

# Lower semicontinuity and projection independence

For $a_n\to a$ in norm with all $a_n,a\ge0$, fibre evaluation is norm continuous and the compact-operator trace is norm lower semicontinuous, hence $$\tau_\theta(a)\le\liminf_n\tau_\theta(a_n).$$ If $e_1,e_2$ are rank-one projections in $\mathcal{K}(H_0)$, a unitary in $\mathcal{B}(H_0)$ conjugates them. The resulting corners $1\otimes e_j$ are Murray--von Neumann equivalent in the multiplier algebra, have character trace one, and yield the same decreasing-peak contradiction. Thus the obstruction does not depend on a preferred rank-one vector. Fullness follows because the closed ideal generated by any nonzero rank-one projection in $\mathcal{K}(H_0)$ is all of $\mathcal{K}(H_0)$.

# Reproduction inventory

From the repository root, the complete deterministic check is

`./papers/8-isotropy-trace/experiments/reproduce.sh`.

It executes 18 unit tests, verifies implementation and active-lock hashes, produces nine CSV artifacts, and compares two fresh generations byte for byte. The artifacts cover shifted Poisson convention, finite character-grid cancellation, nontrivial character phase, trace scaling, rank-one peaks, $L^\infty$ representatives, clock/copy/composite controls, transverse-probability controls, and domain boundaries. The symbolic proofs in the main text remain the theorem owners.

# Expanded ownership certificate

T0 fixes the actual source object; T1 its topology and Borel prerequisites; T2 its flow, clock, and exact isotropy; T3 the groupoid, Haar system, and completion; T4 invariant or transverse measure selection; T5 the represented algebra and trace; T6 the formula with its positive and complex domains; and T7 the arithmetic coefficient and promotion rule. For the packet, T0 and T2 pass, parts of T1 pass, and T3--T6 are blocked. For one chosen orbit, T0--T6 close locally, while T7 supplies only the source prime and clock. For $\Theta_+$, operator fields T3--T5 are inapplicable by scalar type, whereas T6 and the closed-point-counting part of T7 pass. These statements reproduce the type barriers in ; they do not create an aggregate candidate.

# Declarations {#declarations .unnumbered}

#### Data and code availability.

No external empirical dataset was used. Paper 8 uses deterministic Python standard-library code, 18 tests, a reproduction script, nine CSV artifacts, and a hash manifest. The controls test conventions, falsification cases, and domain regressions; they are not mathematical proofs. Repository paths and final release hashes are recorded in the accompanying README files.

#### Ethics approval and consent.

This work involved no human participants, animals, clinical intervention, or personal data. Institutional review-board approval, informed consent, and consent for publication are not applicable.

#### Author contributions.

Liang Wang: Conceptualization, Methodology, Formal analysis, Investigation, Software, Validation, Data curation, Visualization, Writing---original draft, and Writing---review & editing.

#### Competing interests.

The author declares no financial or non-financial conflict of interest.

#### Funding.

No project-specific external funding source was declared.

#### Generative-AI disclosure.

Generative AI assisted source triage, proof and domain cross-checking, deterministic-code drafting, adversarial review, manuscript drafting, and formatting. The workflow retained exact source manifestations, locators, hashes, typed amendments, independent review records, and target-free controls. No unpublished manuscript was uploaded to a secondary model, and no cross-model review is claimed. The human author directed the research question and acceptance criteria, must verify every mathematical statement and citation before submission, and takes responsibility for the final manuscript. An AI system is not an author.

#### Source and citation integrity.

All load-bearing sources were retained with versioned manifestations, exact locators, and SHA-256 checksums. The topology and trace source PDFs, together with the retained novelty corpus, passed the recorded page-count preflights. For the five groupoid sources, the ARS sidecar preflight was unavailable in the audit environment; their page counts and readable content were instead checked with `pdfinfo`, text extraction, and representative image fallback. DOI fields are included only when verified in the source audits. Technical page locators to Deninger and Morishita refer to the explicitly named arXiv manifestations, not assumed journal pagination. Redistribution rights for retained PDFs must be checked separately from citation reproducibility.

#### Acknowledgments.

No personal acknowledgments are declared.
