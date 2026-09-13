---
p1_kind: "derived-fulltext-reading-copy"
route: "flow_systems"
logical_paper_id: "flow_systems--7-packet-groupoid"
canonical_tex: "flow_systems/papers/7-packet-groupoid/paper/manuscript.tex"
canonical_pdf: "flow_systems/papers/7-packet-groupoid/paper/paper.pdf"
source_sha256: "5fd2f30d072b5c629a67c2be95b8fcc95a917e694f7e6be13a45f347f0e0c384"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Prime Packets without a Packet Trace: Decomposable Proxies, a Zero-Mode Ledger, and the Same-Object Boundary

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../flow_systems/papers/7-packet-groupoid>)
- [规范 TeX](<../../../../../flow_systems/papers/7-packet-groupoid/paper/manuscript.tex>)
- [关联 PDF](<../../../../../flow_systems/papers/7-packet-groupoid/paper/paper.pdf>)
- [支撑 Markdown](<../../../../../flow_systems/papers/7-packet-groupoid/README.md>)
- [BibTeX](<../../../../../flow_systems/papers/7-packet-groupoid/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Deninger's rational-Witt flow over $\operatorname{Spec}\mathbb Z$ assigns a compact packet of periodic circles to each rational prime, with least period $\log p$, but the audited source does not supply a packet measure, a von Neumann algebra, or a trace. This paper asks what survives after those missing analytic structures are added explicitly and kept under separate ownership. For the selected decomposable type-I proxy, a concrete faithful normal semifinite trace yields an exact component Poisson formula. The global time-smearing block is bounded, yet for every nonzero test function it belongs to the bounded trace ideal exactly when $\sum_p m_p\log p<\infty$; unit masses fail. The resulting positive-time return record is therefore defined independently as a locally finite Radon measure. A distinct zero-mode family has affiliated $L^1$ membership under weighted summability, whereas bounded trace-ideal membership also requires $\operatorname{Re}s\geq0$. On the open relative-norm domain, its branch-fixed principal trace-log scalar is holomorphic and gives the exact branch-fixed Euler product on its domain; with unit masses the domain is $\operatorname{Re}s>1$. Probability-base and arbitrary-clock controls show that this scalar is a general ledger compiler and cannot validate packet geometry. Finally, a corrected restriction of Morishita's map gives a continuous flow-anti-equivariant intertwiner on Deninger's finite-kernel subsystem, packetwise onto the adelic prime orbit but strictly not globally onto; it collapses transverse labels and transports no measure, operator, or determinant. The exact proxy theorems and the source-owned packet structure therefore cannot be combined into one same-object certificate.
author:
- |
  Liang Wang\
  School of Artificial Intelligence and Automation,\
  Huazhong University of Science and Technology, Wuhan 430074, P.R. China\
  `wangliang.f@gmail.com`
bibliography:
- references.bib
date: 14 August 2026
title: |
  **Prime Packets without a Packet Trace:**\
  Decomposable Proxies, a Zero-Mode Ledger, and the Same-Object Boundary
```

## Markdown 正文

**Keywords:** semifinite trace; direct integral; Poisson summation; trace ideal; adelic dynamics; source ownership

**中文摘要**

Deninger 在 $\operatorname{Spec}\mathbb Z$ 上的有理 Witt 流把每个质数对应到一个周期圆轨道包， 其最小周期为 $\log p$；然而，经核验的原始文献并未给出轨道包上的测度、 von Neumann 代数或迹。本文把缺失的解析结构明确加入一个可分解的 I 型代理， 并严格区分来源与代理的所有权。所得忠实、正规、半有限迹给出逐分量 Poisson 公式，但对任意非零测试函数，全局时间平滑算子属于有界迹理想，当且仅当 $\sum_p m_p\log p<\infty$；单位权重不满足此条件。因此，正时间回归记录必须 另行定义为局部有限 Radon 测度。另一个零模态族在加权和收敛时属于附属 $L^1$，但有界迹理想还要求 $\operatorname{Re}s\geq0$。在相对范数的开域上， 固定主支的迹对数标量全纯，单位权重时于 $\operatorname{Re}s>1$ 给出 Euler 乘积。任意概率基底与任意时钟控制证明此机制只是一个普遍的账本编译器， 不能反证式地确认轨道包几何。最后，对 Morishita 映射作有限核限制后，可得 连续且反转时间的交织映射；它在每个质数轨道包上满射到同一 adelic 质数圆， 却非全局满射，并压缩横向标签，且不传输测度、算子或行列式。故代理上的 精确解析定理不能与来源上的轨道包结构合并为同一对象的证书。

**关键词：** 半有限迹；直积分；Poisson 求和；迹理想；adelic 动力系统；来源所有权

# Introduction

Deninger's dynamical programme supplies a striking arithmetic orbit ledger. For $\operatorname{Spec}\mathbb Z$, rational primes index packets of periodic circles, each packet has isotropy $p^{\mathbb Z}$, and the least additive period is $\log p$ [@Deninger2026 Theorems 5.2 and 6.1]. The author survey further states that these packets are compact and fibred over a compact group [@Deninger2023 Theorem 4.2]. Those statements are topological and orbit-theoretic. They do not, by themselves, define a transverse disintegration, a trace, a trace ideal, or a determinant.

The distinction matters because a correct scalar identity can be owned by the wrong object. One may select a probability space transverse to each circle, integrate the ordinary trace of the circle operator, and assemble the components with arbitrary positive masses. That construction is mathematically legitimate. It is not thereby a theorem about the published rational-Witt flow. Conversely, source-owned packets and periods cannot be attached to a proxy-owned determinant merely because both are indexed by primes. The central problem is thus one of typed ownership: which object owns the set, topology, measure, representation, operator, trace domain, and scalar normalization used in each assertion?

This paper resolves that question for one explicit proxy. It makes three contributions. First, it proves the local and global trace domains rather than inferring them from formal sums. A component time smearing is traceable and obeys Poisson summation, but the global block is outside the trace ideal for unit masses. What remains is a separately defined positive-time Radon measure, not a regularized value of the global trace. Second, it studies a different operator: the projection onto the constant circle mode. The corresponding analytic family admits a branch-fixed principal trace-log scalar on a precise open half-plane. Its formula is exact, but it survives arbitrary probability bases and arbitrary locally finite clock ledgers. Third, it performs a same-object audit. The limited Deninger-to-adelic map obtained by repairing Morishita's full-character statement is real and useful, yet it collapses all transverse circles over a prime and transports none of the proxy's analytic fields.

The paper uses four records throughout. The original rational-Witt flow is `DEN-WITT-Z-FIN`. The selected measured algebraic enrichment is `DEN-WITT-PACKET-DECOMP-MASS-FAM`. Its componentwise return measure is `DEN-WITT-PACKET-DECOMP-RETURN-DIST-M`. The conditional unit-mass zero-mode record is `DEN-WITT-PACKET-DECOMP-K0-M1`. The records share motivation and some clocks; they do not share analytic ownership. Figure [\[fig:owners\]](#fig:owners){reference-type="ref" reference="fig:owners"} displays that separation.

The analysis is deliberately confined to the right-half-plane trace-log domain. It proves no continuation, functional equation, completed divisor, critical-line statement, or spectral realization. It also makes no universal claim that a future packet enrichment is impossible. The negative conclusion is bounded by the explicit sources and transport fields audited through 14 August 2026.

# Source lock and typed ownership {#sec:source-lock}

## What the published flow owns

Deninger's construction fixes auxiliary data before giving the packet coordinates. In particular, equations (37)--(39) of the arXiv v4 source produce equivariant set parametrizations, while the paragraph containing equation (40) states that the earlier maps and the fibration depend on the chosen point above the residue-field point and on an embedding of roots of unity [@Deninger2026 Section 5, equations (32), (35), and (37)--(40)]. For $\operatorname{Spec}\mathbb Z$ these formulas motivate the abstract group $$B_p=\widehat{\mathbb Z}_{(p)}^{\times}/p^{\widehat{\mathbb Z}}
  \qquad\text{and the chosen product}\qquad
  Y_p=B_p\times \mathbb R/(\log p)\mathbb Z.
  \label{eq:BpYp}$$ They do not state that the actual packet $\Gamma_p$ is canonically homeomorphic or Borel isomorphic to $Y_p$. No transition theorem between different auxiliary choices was found in the audited source.

The source does own the packet-level ledger. Theorem 6.1 gives a bijection between finite-residue-field points and packets, says that every periodic orbit belongs to a unique packet, and fixes the isotropy and period [@Deninger2026 Section 6, Theorem 6.1]. For $\operatorname{Spec}\mathbb Z$ this becomes $$(p)\longleftrightarrow \Gamma_p,
  \qquad \operatorname{Iso}(\Gamma_p)=p^{\mathbb Z},
  \qquad L_p=\log p .
  \label{eq:source-ledger}$$ The packet is not a single circle. It is a transverse family of circles with the same least period. The compactness of $\Gamma_p$ and of its abstract base is corroborated by Deninger's survey [@Deninger2023 Theorem 4.2].

Normalized Haar probability on the abstract compact group $B_p$ is a standard consequence of compact-group theory. Transporting that Haar measure to the actual packet, independently of the coordinate choices, is a different statement. The audited Deninger texts, including the later rational-Witt sheaf paper [@Deninger2025Witt], contain no such disintegration theorem. They likewise contain no packet von Neumann algebra, normal semifinite packet trace, zero-mode family, or determinant. Deninger's Section 11 Haar convolution algebra has a different inverse-limit group and no theorem maps it to the packet proxy used here [@Deninger2026 Section 11].

## Four candidate owners

Table [1](#tab:owners){reference-type="ref" reference="tab:owners"} records the non-inheritance rule. The mass-family proxy is a selected construction. It is never assigned a source-owned convolution structure, a source-owned operator algebra, or a canonical analytic completion of the source.

::: {#tab:owners}
  Record             Owned fields                                                                                                     Non-inherited fields
  ------------------ ---------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------
  Source             Prime packets, repetitions, compactness, $\log p$ clocks                                                         Product Borel structure, transverse Haar, algebra, trace, $L^1$, zero mode, determinant
  Mass family        Chosen $Y_p$, probability Haar on abstract $B_p$, representation, $\mathcal M_p$, positive masses and $\tau_m$   Source canonicity, source generation, or source Route coordinates
  Return record      $C_{p,f}$ and the positive-time component ledger $\Theta_m$                                                      Global trace outside its domain; zero-mode determinant
  Zero-mode record   Unit-mass $K_s$ and the local scalar $D^{\mathrm{pr}}_{\tau}$                                                    Source mass provenance, primitive-orbit ownership, packet geometry, continuation

  : Typed owners and fields that do not transfer automatically.
:::

Counting measure on the prime closed points is a target-free definition. It makes "one unit per prime-indexed packet" a natural ledger convention. It does not map that unit to a central trace coefficient of the chosen algebra. That last step remains a modeling choice until a theorem transports the closed-point counting measure through the packet, representation, and trace.

# The selected decomposable algebra and its trace {#sec:algebra}

Let $\mu_p$ be normalized Haar probability on the abstract group $B_p$, let $S_{L}=\mathbb R/L\mathbb Z$ with Lebesgue measure $du$ on $[0,L)$, and set $$\begin{aligned}
  \mathcal K_p&=L^2(S_{L_p},du),\\
  \mathcal H_p&=L^2(B_p,\mu_p)\otimes \mathcal K_p,\\
  \mathcal M_p&=L^\infty(B_p,\mu_p)\,\bar\otimes\,\mathcal B(\mathcal K_p),\\
  \mathcal M&=\prod_p^{\infty}\mathcal M_p
     =\{(A_p)_p:\sup_p\left\lVert A_p\right\rVert<\infty\}.
 \end{aligned}
 \label{eq:algebra}$$ This is a concrete decomposable type-I representation. For a fixed sequence $0<m_p<\infty$, define on the positive cone $$\tau_p(A_p)=\int_{B_p}\operatorname{Tr}_{\mathcal K_p}(A_p(b))\,d\mu_p(b),
 \qquad
 \tau_m(A)=\sum_p m_p\tau_p(A_p).
 \label{eq:trace}$$ Direct-integral trace disintegration is standard in the semifinite setting [@Hiai1988 p. 118 and Lemma 2.1], and countable sufficient families of normal semifinite traces can be assembled into a faithful trace [@BagarelloTrapaniTriolo2006 Theorem 2.1]. The concrete hypotheses are verified next rather than imported as a label.

[\[prop:fns\]]{#prop:fns label="prop:fns"} For every positive finite mass sequence $(m_p)_p$, formula [\[eq:trace\]](#eq:trace){reference-type="eqref" reference="eq:trace"} defines a faithful normal semifinite trace on $\mathcal M$. For a bounded block $A=(A_p)_p$, $$A\in \mathcal L^1_{\tau_m}(\mathcal M):=\mathcal M\cap L^1(\mathcal M,\tau_m)
 \quad\Longleftrightarrow\quad
 \sum_p m_p\left\lVert A_p\right\rVert_{1,\tau_p}<\infty .
 \label{eq:blockL1}$$

On each direct-integral fibre, the ordinary trace is tracial and faithful; integration preserves both properties. Normality holds for arbitrary increasing nets by the direct-integral trace theorem. For semifiniteness, let $Q_{p,N}$ project $\mathcal K_p$ onto the Fourier modes $|n|\leq N$ and put $$E_{p,N}=1_{B_p}\otimes Q_{p,N},
 \qquad A_p^{(N)}=A_p^{1/2}E_{p,N}A_p^{1/2}.
 \label{eq:local-cutdown}$$ The congruence form is essential: $A_p^{(N)}$ increases to $A_p$ strongly, lies below $A_p$, and satisfies $$\tau_p(A_p^{(N)})
 =\tau_p(E_{p,N}A_pE_{p,N})
 \leq \left\lVert A_p\right\rVert(2N+1)<\infty .$$ Globally, take finite sets $F$ of primes and one cutoff $N_p$ for each $p\in F$. The corresponding finite-prime, finite-mode blocks increase strongly to $A$ and have trace at most $\left\lVert A\right\rVert\sum_{p\in F}m_p(2N_p+1)$. Thus $\tau_m$ is semifinite.

If $A_i\uparrow A$, local normality gives the component suprema. On a finite prime set, directedness provides a common upper index for the finitely many component approximations. Taking the supremum over finite prime sets proves $$\sup_i\sum_p m_p\tau_p(A_{i,p})
 =\sum_p m_p\sup_i\tau_p(A_{i,p})
 =\sum_p m_p\tau_p(A_p),$$ so the global trace is normal. Positivity of every finite $m_p$ gives faithfulness. Finally, functional calculus is componentwise, hence $|A|=(|A_p|)_p$ and [\[eq:blockL1\]](#eq:blockL1){reference-type="eqref" reference="eq:blockL1"} follows from the positive-cone formula. The full affiliated $L^1$ space and its bounded intersection are therefore distinct objects. See also the generalized singular-number integral of @FackKosaki1986 [Proposition 2.7 and Corollary 2.8] and the bounded relative ideal used by @HochsKaadSchemaitat2018 [Section 6.2].

The relative Banach norm used later is $$\left\lVert A\right\rVert_{\mathrm{rel}}=\left\lVert A\right\rVert+\left\lVert A\right\rVert_{1,\tau_m}.
  \label{eq:relative-norm}$$ No Dirichlet-series convergence was used to establish Proposition [\[prop:fns\]](#prop:fns){reference-type="ref" reference="prop:fns"}. This ordering prevents an analytic special case from being mistaken for the existence theorem for the trace itself.

# Branch F: component traces and the global obstruction {#sec:branch-f}

## Fourier convention and the component Poisson trace

For $L>0$, use the normalized Fourier basis $$e_{n,L}(u)=L^{-1/2}e^{2\pi inu/L},\qquad n\in\mathbb Z,$$ and the right-regular translation $(U_L(t)g)(u)=g(u-t)$. Fix $$\widehat f(\xi)=\int_{\mathbb R}f(t)e^{-it\xi}\,dt,
 \qquad
 f(t)=\frac{1}{2\pi}\int_{\mathbb R}\widehat f(\xi)e^{it\xi}\,d\xi .
 \label{eq:fourier}$$ This is the convention in @Laugesen2009 [Definition 14.1]; its scaled Poisson formula follows from the same source's Theorem 23.5. For $f\in C_c^\infty(\mathbb R)$ define $$T_L(f)=\int_{\mathbb R}f(t)U_L(t)\,dt,
 \qquad
 C_{p,f}=1_{B_p}\otimes T_{L_p}(f).
 \label{eq:Cpf}$$

[\[thm:p71\]]{#thm:p71 label="thm:p71"} For every prime $p$ and every $f\in C_c^\infty(\mathbb R)$, $C_{p,f}\in\mathcal L^1_{\tau_p}(\mathcal M_p)$ and $$\begin{aligned}
 \left\lVert C_{p,f}\right\rVert_{1,\tau_p}
   &=\sum_{n\in\mathbb Z}\left\lvert \widehat f(2\pi n/L_p)\right\rvert,
   \label{eq:component-norm}\\
 \tau_p(C_{p,f})
   &=\sum_{n\in\mathbb Z}\widehat f(2\pi n/L_p)
     =L_p\sum_{r\in\mathbb Z}f(rL_p).
   \label{eq:poisson-trace}\end{aligned}$$

The frozen translation sign gives $T_L(f)e_{n,L}=\widehat f(2\pi n/L)e_{n,L}$. Since $\widehat f$ is Schwartz, the eigenvalue lattice is absolutely summable. Thus $T_L(f)$ is ordinary trace class on the circle factor. Integrating its constant decomposable field over the probability base gives [\[eq:component-norm\]](#eq:component-norm){reference-type="eqref" reference="eq:component-norm"} and the first sum in [\[eq:poisson-trace\]](#eq:poisson-trace){reference-type="eqref" reference="eq:poisson-trace"}. Periodize $f$ by $F_L(u)=\sum_{r\in\mathbb Z}f(u+rL)$. Its $n$th Fourier coefficient is $L^{-1}\widehat f(2\pi n/L)$, and absolute convergence permits evaluation at zero. This gives the last equality.

The component ideal in Theorem [\[thm:p71\]](#thm:p71){reference-type="ref" reference="thm:p71"} is the semifinite ideal. When $L^2(B_p)$ is infinite-dimensional, the tensor product $1_{B_p}\otimes T_{L_p}(f)$ need not be ordinary Hilbert trace class even though its $\tau_p$-trace norm is finite. Section [5.4](#sec:det-taxonomy){reference-type="ref" reference="sec:det-taxonomy"} proves that infinitude for the actual frozen $B_p$.

## Bounded globally, but generally not traceable

The block $C_f=(C_{p,f})_p$ always lies in $\mathcal M$, since $$\left\lVert C_{p,f}\right\rVert=\sup_n\left\lvert \widehat f(2\pi n/L_p)\right\rvert
 \leq \left\lVert f\right\rVert_{L^1(\mathbb R)}.$$ Boundedness is not traceability. Proposition [\[prop:fns\]](#prop:fns){reference-type="ref" reference="prop:fns"} gives $$C_f\in\mathcal L^1_{\tau_m}(\mathcal M)
 \quad\Longleftrightarrow\quad
 \sum_p m_p\sum_{n\in\mathbb Z}
       \left\lvert \widehat f(2\pi n/L_p)\right\rvert<\infty .
 \label{eq:global-C-criterion}$$

[\[thm:p72\]]{#thm:p72 label="thm:p72"} If $f\in C_c^\infty(\mathbb R)$ is nonzero, then $$C_f\in\mathcal L^1_{\tau_m}(\mathcal M)
 \quad\Longleftrightarrow\quad
 \sum_p m_p\log p<\infty .
 \label{eq:global-exact}$$ In particular, unit masses give a bounded block outside the global trace ideal.

Put $g(\xi)=|\widehat f(\xi)|$. The whole-line Riemann-sum theorem yields $$\frac{2\pi}{L}\sum_{n\in\mathbb Z}g(2\pi n/L)
 \longrightarrow \int_{\mathbb R}g(\xi)\,d\xi .$$ Hence, as $p\to\infty$, $$\left\lVert C_{p,f}\right\rVert_{1,\tau_p}
 \sim c_f\log p,
 \qquad
 c_f=\frac{1}{2\pi}\int_{\mathbb R}|\widehat f(\xi)|\,d\xi>0.
 \label{eq:trace-asymptotic}$$ The strict positivity follows from Fourier injectivity. Eventual two-sided bounds in [\[eq:trace-asymptotic\]](#eq:trace-asymptotic){reference-type="eqref" reference="eq:trace-asymptotic"} reduce [\[eq:global-C-criterion\]](#eq:global-C-criterion){reference-type="eqref" reference="eq:global-C-criterion"} exactly to [\[eq:global-exact\]](#eq:global-exact){reference-type="eqref" reference="eq:global-exact"}. For unit masses the summands do not even tend to zero.

## A separately owned positive-time return measure

Let $f\in C_c^\infty((0,\infty))$. Because its support excludes zero, the component Poisson formula has only positive repetitions. Define $$\Theta_m(f)
 =\sum_p m_pL_p\sum_{r\geq1}f(rL_p),
 \qquad
 \Theta_m=\sum_p\sum_{r\geq1}m_pL_p\,\delta_{rL_p}.
 \label{eq:Theta}$$

[\[thm:p73\]]{#thm:p73 label="thm:p73"} For any sequence of positive finite masses, $\Theta_m$ is a locally finite positive Radon measure on $(0,\infty)$, hence a distribution of order zero. If $C_f$ lies in the global trace ideal, then $\tau_m(C_f)=\Theta_m(f)$. Outside that domain, $\Theta_m(f)$ remains defined by [\[eq:Theta\]](#eq:Theta){reference-type="eqref" reference="eq:Theta"} but is not a value or distributional extension of $\tau_m(C_f)$.

If $\operatorname{supp}f\subset[a,b]$ with $a>0$, a contributing pair $(p,r)$ must satisfy $p\leq e^b$ and $r\leq b/\log2$. Only finitely many pairs occur, regardless of the growth of masses away from that compact set. This proves local finiteness. Under [\[eq:global-C-criterion\]](#eq:global-C-criterion){reference-type="eqref" reference="eq:global-C-criterion"}, absolute trace-norm summability licenses the component sum. Without it, the normal semifinite trace has no finite complex value on the block, so the right-hand side must retain its separate definition and owner.

Time zero is not harmless. If it is admitted, the $r=0$ term contributes $$f(0)\sum_p m_p\log p.
 \label{eq:zero-time}$$ No regularization of [\[eq:zero-time\]](#eq:zero-time){reference-type="eqref" reference="eq:zero-time"} is introduced here. This is the first point at which the two analytic branches diverge permanently: failure of the global trace does not authorize relabeling the component ledger as a flat or groupoid trace.

# Branch K: zero modes and the principal trace-log scalar {#sec:branch-k}

Let $e_{0,p}=L_p^{-1/2}$ be the constant circle mode and define $$P_{0,p}=1_{B_p}\otimes |e_{0,p}\rangle\langle e_{0,p}|,
 \qquad \tau_p(P_{0,p})=1,
 \qquad K_s=(p^{-s}P_{0,p})_p .
 \label{eq:zero-mode}$$ This family is not the time-smearing block $C_f$. It owns a different operator, domain, and scalar.

## The versioned P7-4 correction

The preregistered general-mass target wrote one unqualified $L^1$ condition. The proof found that this conflated a possibly unbounded affiliated operator with an element of the bounded von Neumann product. The change was recorded non-retroactively as amendment `P7-PH3-AMEND-2026-08-14-v1`; the historical statement was retained in the protocol and superseded rather than silently rewritten.

[\[thm:p74\]]{#thm:p74 label="thm:p74"} Write $\sigma=\operatorname{Re}s$. Then $$\begin{aligned}
 K_s\in L^1(\mathcal M,\tau_m)\text{ as an affiliated operator}
 &\quad\Longleftrightarrow\quad
 \sum_p m_pp^{-\sigma}<\infty,
 \label{eq:affiliated-domain}\\
 K_s\in\mathcal L^1_{\tau_m}(\mathcal M)
 &\quad\Longleftrightarrow\quad
 \sigma\geq0\ \text{and}\
 \sum_p m_pp^{-\sigma}<\infty.
 \label{eq:bounded-domain}\end{aligned}$$ For unit masses, both relevant trace-ideal conditions hold exactly when $\operatorname{Re}s>1$.

Componentwise functional calculus gives $$\left\lVert K_s\right\rVert=\sup_p p^{-\sigma},
 \qquad
 \tau_m(|K_s|)=\sum_p m_pp^{-\sigma}.
 \label{eq:Ks-norms}$$ The first quantity is finite exactly for $\sigma\geq0$. This proves [\[eq:bounded-domain\]](#eq:bounded-domain){reference-type="eqref" reference="eq:bounded-domain"}. The closed block-diagonal operator is affiliated for every $s$; applying the extended trace to its bounded spectral truncations proves [\[eq:affiliated-domain\]](#eq:affiliated-domain){reference-type="eqref" reference="eq:affiliated-domain"}. For unit masses, $\sum_p p^{-\sigma}$ converges for $\sigma>1$ as a subseries of $\sum_{n\geq2}n^{-\sigma}$. For $0<\sigma\leq1$ it dominates $\sum_p1/p$, which diverges by the finite Euler-product comparison with harmonic partial sums; for $\sigma\leq0$ its terms do not tend to zero.

The correction is material for general masses. For example, $m_p=p^{-3}$ and $\sigma=-1$ make the trace sum finite but $\left\lVert K_s\right\rVert=\infty$. The operator is then affiliated and integrable, but it does not belong to the bounded relative determinant algebra. For unit masses the proved half-plane is unchanged.

## Relative-norm holomorphy

Let $\sigma_c(m)$ be the abscissa of convergence of $\sum_pm_pp^{-\sigma}$ and set $$\mathfrak H_m
 =\{s\in\mathbb C:\operatorname{Re}s>\max(0,\sigma_c(m))\}.
 \label{eq:Hm}$$ The set may be empty when $\sigma_c(m)=+\infty$. It is open; on it $K_s\in\mathcal L^1_{\tau_m}(\mathcal M)$ and $\left\lVert K_s\right\rVert<1$.

[\[prop:relative-holo\]]{#prop:relative-holo label="prop:relative-holo"} The maps $s\mapsto K_s$ and $$\operatorname{Log}_0(I-K_s)=-\sum_{r\geq1}\frac{K_s^r}{r}
 \label{eq:log-series}$$ are holomorphic on $\mathfrak H_m$ in the relative norm [\[eq:relative-norm\]](#eq:relative-norm){reference-type="eqref" reference="eq:relative-norm"}; the series in [\[eq:log-series\]](#eq:log-series){reference-type="eqref" reference="eq:log-series"} and its derivative converge locally uniformly in that norm.

Fix a compact set $C\subset\mathfrak H_m$ and put $a=\min_{s\in C}\operatorname{Re}s$. Choose $\sigma_c(m)<\sigma_0<a$ and let $\delta=a-\sigma_0$. For each $k\geq0$, $$\sum_p m_p(\log p)^kp^{-\operatorname{Re}s}
 \leq C_{k,\delta}\sum_p m_pp^{-\sigma_0},
 \qquad s\in C.
 \label{eq:trace-derivative-bound}$$ The tail of the independent operator-norm component satisfies $$\sup_{p>P}(\log p)^kp^{-a}\longrightarrow0.
 \label{eq:operator-tail}$$ Thus finite-prime entire truncations converge locally uniformly in both operator and trace norm, for every derivative order. This proves relative-norm holomorphy of $K_s$.

Put $q=2^{-a}<1$ and $M_0=\sum_pm_pp^{-a}$. Uniformly on $C$, $$\left\lVert K_s^r\right\rVert\leq q^r,
 \qquad
 \left\lVert K_s^r\right\rVert_{1,\tau_m}\leq M_0q^{r-1}.
 \label{eq:log-bounds}$$ The two geometric majorants give convergence of [\[eq:log-series\]](#eq:log-series){reference-type="eqref" reference="eq:log-series"} in the combined norm. Since the diagonal blocks commute, $\frac{d}{ds}(K_s^r/r)=K_s^{r-1}K_s'$, and the same estimates give locally uniform derivative convergence.

## The scalar lift and Euler ledger

The relative determinant framework treats the bounded trace ideal as a relative Banach-algebra pair [@HochsKaadSchemaitat2018 Sections 6.2--6.4]. The de la Harpe--Skandalis construction is naturally quotient-valued [@deLaHarpeSkandalis1984 Definition and Proposition 2]; it does not provide an automatic global complex scalar for an unbounded trace. The power series in Proposition [\[prop:relative-holo\]](#prop:relative-holo){reference-type="ref" reference="prop:relative-holo"} instead fixes one local logarithm path at the identity.

[\[thm:p75\]]{#thm:p75 label="thm:p75"} For $s\in\mathfrak H_m$, define $$D^{\mathrm{pr}}_{\tau}(s)
 :=\exp\!\left(\tau_m(\operatorname{Log}_0(I-K_s))\right),
 \qquad Z_m(s):=D^{\mathrm{pr}}_{\tau}(s)^{-1}.
 \label{eq:D-def}$$ Then $D^{\mathrm{pr}}_{\tau}$ is holomorphic and nonzero, and $$\begin{aligned}
 D^{\mathrm{pr}}_{\tau}(s)
 &=\exp\!\left(-\sum_{r\geq1}\frac{\tau_m(K_s^r)}{r}\right)
   \label{eq:D-trace-log}\\
 &=\exp\!\left(-\sum_p m_p\sum_{r\geq1}\frac{p^{-rs}}{r}\right)
  =\exp\!\left(\sum_p m_p\operatorname{Log}_0(1-p^{-s})\right).
 \label{eq:D-product}\end{aligned}$$ For nonintegral $m_p$, the final exponential is the definition of the branch-fixed product notation. For unit masses, $$D^{\mathrm{pr}}_{\tau}(s)=\prod_p(1-p^{-s}),
 \qquad Z_m(s)=\prod_p(1-p^{-s})^{-1}=\zeta(s),
 \qquad \operatorname{Re}s>1.
 \label{eq:unit-product}$$

The trace is continuous on the relative ideal, so Proposition [\[prop:relative-holo\]](#prop:relative-holo){reference-type="ref" reference="prop:relative-holo"} makes [\[eq:D-def\]](#eq:D-def){reference-type="eqref" reference="eq:D-def"} holomorphic. Since $P_{0,p}^r=P_{0,p}$, $\tau_m(K_s^r)=\sum_pm_pp^{-rs}$. On compact subsets of $\mathfrak H_m$ the double series is absolutely and locally uniformly convergent, because for $\sigma>0$, $$\sum_p\sum_{r\geq1}\frac{m_pp^{-r\sigma}}r
 \leq \frac{\sum_pm_pp^{-\sigma}}{1-2^{-\sigma}}.$$ This licenses the trace and sum interchanges and gives the principal scalar logarithm term by term. Unit masses yield the classical absolutely convergent Euler product in its right half-plane.

Equation [\[eq:unit-product\]](#eq:unit-product){reference-type="eqref" reference="eq:unit-product"} is an exact proxy theorem, not a provenance theorem. The scalar is denoted $D^{\mathrm{pr}}_{\tau}$ precisely to prevent it from being confused with an ordinary Fredholm determinant, a positive Fuglede--Kadison determinant, a Breuer index, or a dynamical orbit determinant.

## Determinant taxonomy and ordinary multiplicity {#sec:det-taxonomy}

The ordinary-Hilbert contrast must be proved for the actual $B_p$, not only for a generic infinite control base. Write $$G_p=\widehat{\mathbb Z}_{(p)}^\times=\prod_{\ell\neq p}\mathbb Z_\ell^\times,
 \qquad H_p=p^{\widehat{\mathbb Z}}\subset G_p,
 \qquad B_p=G_p/H_p .$$ Let $S_p$ be the coordinatewise sign subgroup on the infinitely many odd primes $\ell\neq p$. It is isomorphic to an infinite product of copies of $C_2$. A procyclic profinite group has at most one nonidentity involution: otherwise a finite cyclic quotient would contain two. Consequently $|S_p\cap H_p|\leq2$, so $B_p$ is infinite.

An infinite compact group has infinite-dimensional Haar $L^2$. For every $N$, choose $N$ distinct points and disjoint nonempty open neighborhoods. Each neighborhood has positive Haar measure, and their indicator functions are nonzero and mutually orthogonal. Therefore $$\dim L^2(B_p,\mu_p)=\infty .
 \label{eq:Bp-infinite-L2}$$ It follows that $P_{0,p}=I_{L^2(B_p)}\otimes|e_0\rangle\langle e_0|$ has infinite ordinary Hilbert rank and trace, even though $\tau_p(P_{0,p})=1$.

::: {#tab:taxonomy}
  Construction                        Codomain and domain                        Status for the frozen zero-mode family
  ----------------------------------- ------------------------------------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------
  Ordinary Fredholm                   Complex scalar on $I+\mathcal S_1$         Unavailable in the intended representation: each nonzero $P_{0,p}$ has infinite Hilbert rank [@Bornemann2010 Section 3].
  Relative de la Harpe--Skandalis     Quotient by the trace image of $K_0$       Underlying relative framework applies; $D^{\mathrm{pr}}_{\tau}$ is only the local scalar lift selected by $\operatorname{Log}_0$.
  Semifinite Fuglede--Kadison         Positive real number $\exp\tau(\log|g|)$   Applies and equals $|D^{\mathrm{pr}}_{\tau}(s)|$; it discards complex phase [@HochsKaadSchemaitat2018 Definition 7.4].
  Breuer--Fredholm                    Index in the semifinite Fredholm theory    $I-K_s$ is already invertible on $\mathfrak H_m$, hence index zero; no scalar determinant follows [@BenameurEtAl2006 Section 3].
  Finite-trace analytic determinant   Scalar trace-log for a trace state         Its finite-state theorem cannot be applied verbatim because $\tau_m(1)=\infty$; even there, a product law may fail [@GuidoIsolaLapidus2009 Remark 4.5].

  : Determinant and index constructions relevant to $I-K_s$.
:::

For completeness, the positive semifinite determinant satisfies $$\Delta_{\tau_m}(I-K_s)
 =\exp\!\left(\sum_pm_p\log|1-p^{-s}|\right)
 =|D^{\mathrm{pr}}_{\tau}(s)|.
 \label{eq:FK-modulus}$$ The original finite-factor determinant is likewise positive-valued [@FugledeKadison1952 Definition and Lemma 1, p. 521]. Equality in [\[eq:FK-modulus\]](#eq:FK-modulus){reference-type="eqref" reference="eq:FK-modulus"} does not make that positive invariant a complex holomorphic Euler product. The expression "Breuer determinant" is not used: Breuer--Fredholm theory supplies an index, and the relevant index here is trivially zero.

# Mass freedom, coefficient uniqueness, and controls {#sec:controls}

## P7-6: the exact scope of the mass family

Fix the local traces $\tau_p$. Proposition [\[prop:fns\]](#prop:fns){reference-type="ref" reference="prop:fns"} shows that every sequence $0<m_p<\infty$ gives an FNS trace. Within the frozen central-scalar ansatz $$\tau_m|_{z_p\mathcal M}=m_p\tau_p,
 \label{eq:central-ansatz}$$ the mass is recovered as $m_p=\tau_m(P_{0,p})$. Positive finite sequences therefore classify this central-scalar family. They do not classify all FNS traces: a nonconstant positive central density $w_p(b)$ can give $\int w_p(b)\operatorname{Tr}(A_p(b))\,d\mu_p(b)$, outside the frozen scalar ansatz.

Multiplying by $m_p$ preserves every local symmetry already known to preserve $\tau_p$, including circle translations and fibre-unitary conjugacy. It does not prove that an unverified packet coordinate change preserves $\mu_p$. If one component is copied as an orthogonal central summand with the same local trace and mass, its contribution doubles: $$\tau_{\mathrm{copy}}(A_p\oplus A_p)=2m_p\tau_p(A_p).
 \label{eq:copy}$$ Splitting the old mass between the copies would be a new normalization. Thus copying exposes additivity but does not select $m_p=1$. This is the scoped content of P7-6.

## P7-7: uniqueness after imposing the target

On a common half-plane of absolute convergence, Theorem [\[thm:p75\]](#thm:p75){reference-type="ref" reference="thm:p75"} gives $$-\frac{Z_m'(s)}{Z_m(s)}
 =\sum_p\sum_{r\geq1}m_p(\log p)p^{-rs}.
 \label{eq:log-derivative}$$ If this is required to equal the unit-coefficient prime-power series, then uniqueness of absolutely convergent Dirichlet series forces $m_p=1$ for every $p$: the coefficient at the primitive index $n=p$ is $(m_p-1)\log p$. A self-contained proof takes the least nonzero coefficient, multiplies the zero Dirichlet series by its index to the power $s$, and lets real $s\to\infty$.

This is uniqueness conditional on the desired target, not independent provenance. Selecting the trace masses because [\[eq:log-derivative\]](#eq:log-derivative){reference-type="eqref" reference="eq:log-derivative"} then agrees with that target uses the requested coefficients as input. The argument is therefore a consistency diagnostic and cannot close the source-to-proxy mass transport gate.

## P7-8: probability-base and clock blindness

Replace $B_p$ by a singleton or by any probability space $(\Omega_p,\nu_p)$, while keeping the fibre operators constant. Then $$\int_{\Omega_p}\operatorname{Tr}(T)\,d\nu_p=\operatorname{Tr}(T).
 \label{eq:base-blind}$$ Consequently the component trace and trace norm, $\tau_p(P_{0,p})$, every $\tau_m(K_s^r)$, $\Theta_m$, and $D^{\mathrm{pr}}_{\tau}$ are unchanged. Only total base mass enters. A non-probability total mass can be absorbed into $m_p$.

The ordinary trace behaves differently: on a singleton base the projection has ordinary rank one, while on the intended $B_p$ it has infinite rank by [\[eq:Bp-infinite-L2\]](#eq:Bp-infinite-L2){reference-type="eqref" reference="eq:Bp-infinite-L2"}. The equality of the semifinite formulas across these two situations is therefore a genuine base-blindness witness.

More generally, let $(L_j)_{j\in J}$ be a countable locally finite list of positive lengths, meaning that only finitely many $L_j$ lie below each fixed bound. Repeating the construction gives $$\begin{aligned}
 \Theta_{m,L}
   &=\sum_j\sum_{r\geq1}m_jL_j\delta_{rL_j},
   \label{eq:clock-return}\\
 D^{\mathrm{pr}}_{\tau,L}(s)
   &=\exp\!\left(\sum_jm_j\operatorname{Log}_0(1-e^{-sL_j})\right)
   \label{eq:clock-product}\end{aligned}$$ on the latter expression's actual trace-ideal and strict-norm domain. Local finiteness of the clock list suffices for [\[eq:clock-return\]](#eq:clock-return){reference-type="eqref" reference="eq:clock-return"}. It does not ensure that $\sum_jm_je^{-\sigma L_j}$ converges for any $\sigma$; the domain of [\[eq:clock-product\]](#eq:clock-product){reference-type="eqref" reference="eq:clock-product"} can be empty. Prime clocks, arbitrary clocks, and composite-augmented clocks all compile their corresponding ledgers whenever those independent analytic gates hold.

::: {#tab:controls}
  Control                           Preserved quantity                                                                                            Consequence
  --------------------------------- ------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------
  Probability-base replacement      Component trace, return measure, zero-mode scalar                                                             Transverse topology and cardinality are unnecessary to the semifinite formula.
  Copied component                  Additive trace, return, and trace-log exponent                                                                Multiplicity requires a separate normalization; local invariance does not fix it.
  Positive mass perturbation        All component theorems and weighted ledgers                                                                   Unit central mass is not forced within the proxy.
  Arbitrary locally finite clocks   Positive-time return ledger                                                                                   The return mechanism is a general clock compiler.
  Composite-augmented clocks        The analytic compiler, when convergent                                                                        Analytic survival does not supply rational-prime provenance.
  Ordinary Hilbert trace            Fails on the intended infinite base                                                                           Finite semifinite trace is not an ordinary represented trace.
  Zero time                         Positive partial sums in [\[eq:zero-time\]](#eq:zero-time){reference-type="eqref" reference="eq:zero-time"}   A separately named regularization would be required.

  : Falsification controls and their interpretation.
:::

The controls prove too much for scalar exactness to certify geometry: the same formal mechanism works after the transverse packet has been replaced by a point and after arithmetic clocks have been replaced by an arbitrary ledger. That does not make the construction useless. It identifies its valid role as a transparent analytic compiler and blocks a stronger inference.

# The restricted adelic intertwiner {#sec:morishita}

The only audited post-source bridge points to a third object, the Connes--Consani adelic system, not to the Paper-7 proxy. Its exact scope must be reconstructed because Morishita's printed comparison uses an enlarged full-character space.

## Why the printed full-character statements do not close

Morishita defines the unrefined space with the complete character set $\operatorname{Hom}_{\mathrm{Gr}}(\overline{\mathbb F}_p^\times,\mathbb C^\times)$ and explicitly notes that Deninger's refinement is omitted [@Morishita2026 equation (2.1.5) and Remark 2.1.13]. Equation (2.2.7) then displays a surjection $$\widehat{\mathbb Z}_{(p)}^\times\times\mathbb N
 \longrightarrow
 \operatorname{Hom}_{\mathrm{Gr}}(\overline{\mathbb F}_p^\times,\mathbb C^\times),
 \qquad
 (a,n)\longmapsto\chi_P\circ(\cdot)^a\circ(\cdot)^n .
 \label{eq:mor-full}$$ Every character in the displayed image has finite kernel: $a$ is an automorphism, the $n$th-power map has finite kernel, and $\chi_P$ is injective. The trivial character lies in the printed full Hom set and has infinite kernel. Thus the full-space surjectivity claim in [\[eq:mor-full\]](#eq:mor-full){reference-type="eqref" reference="eq:mor-full"} cannot hold as written.

The printed proof of Theorem 3.6(2) has a second, independent gap. It checks that the exponent adele has $\alpha_p=0$. Membership in the standard prime orbit $C_p$ also requires every finite coordinate away from $p$ to be nonzero and normalizable. On the unrefined full space the trivial character has every finite coordinate equal to zero, and quotient multiplication cannot change its zero-coordinate set. The theorem used below is consequently a new finite-kernel restriction, not the unmodified printed theorem.

## The exact $E_{\mathrm f}$ repair

Deninger's equation (35) identifies the fixed-fibre finite-kernel class $E_{\mathrm f}$: every such character is represented by a positive integer $n$ and a unit $a\in\widehat{\mathbb Z}_{(p)}^\times$ [@Deninger2026 equation (35)]. Deninger's admissibility results make $E_{\mathrm f}$ invariant under the Frobenius and Galois actions, and Section 7 supplies the corresponding subspace, quotient, and inductive-limit topologies. Morishita's root-of-unity map is continuous and equivariant by Lemmas 3.4--3.5 [@Morishita2026]. Restriction to the invariant $E_{\mathrm f}$ subsystem and descent through the quotients are therefore legitimate.

[\[thm:ef\]]{#thm:ef label="thm:ef"} Let $X_{\mathrm{Den}}^{E_{\mathrm f}}$ be Deninger's finite-kernel system for $\operatorname{Spec}\mathbb Z$. Restricting Morishita's root-of-unity map gives a continuous map $$\Psi_{E_{\mathrm f}}:X_{\mathrm{Den}}^{E_{\mathrm f}}\longrightarrow X_{\mathbb Q}$$ such that, for $u>0$, $$\Psi_{E_{\mathrm f}}(\phi_u x)=u^{-1}\Psi_{E_{\mathrm f}}(x).
 \label{eq:anti-equivariant}$$ For every prime $p$ and every periodic source circle $\gamma\subset\Gamma_p$, $$\Psi_{E_{\mathrm f}}(\gamma)=C_p.
 \label{eq:packetwise-onto}$$ The map is not globally surjective onto $X_{\mathbb Q}$.

Continuity and [\[eq:anti-equivariant\]](#eq:anti-equivariant){reference-type="eqref" reference="eq:anti-equivariant"} follow from the invariant restriction and Morishita's Lemmas 3.4--3.5. On a closed $p$-fibre, Deninger's equation (35) writes a finite-kernel character with $a\in\widehat{\mathbb Z}_{(p)}^\times$ and $n\in\mathbb N$. Its exponent adele satisfies $$\alpha_p=0,
 \qquad \alpha_q=na_q\neq0\quad(q\neq p).
 \label{eq:away-coordinates}$$ Multiplication by $n^{-1}\in\mathbb Q^\times$ and then by the appropriate element of $\widehat{\mathbb Z}^\times$ normalizes every away-from-$p$ coordinate to one while the $p$-coordinate remains zero. Thus one point of the source circle maps into $C_p$. Flow anti-equivariance then sends the full source circle onto the full target orbit, proving [\[eq:packetwise-onto\]](#eq:packetwise-onto){reference-type="eqref" reference="eq:packetwise-onto"}.

For the global negative statement, Deninger's equations (62)--(68) show that the root-of-unity exponent image has either no finite zero coordinate or one such coordinate [@Deninger2026 equations (62)--(68)]. The adelic target contains a class represented by an adele with zeros at two distinct primes and ones elsewhere. Multiplication by $\mathbb Q^\times$ or $\widehat{\mathbb Z}^\times$ preserves its two-element zero set; the same invariant is explicit in the adelic quotient description of @ConnesConsani2025 [equation (2)]. The class has no preimage, so $\Psi_{E_{\mathrm f}}$ is strictly not globally onto.

Every source circle over $p$ has the same image $C_p$. The induced map on transverse orbit labels is therefore constant. This is transverse collapse, not a packet homeomorphism, conjugacy, or measured equivalence. Figure [\[fig:ef\]](#fig:ef){reference-type="ref" reference="fig:ef"} makes the object boundary visible.

No theorem in the audited Deninger, Morishita, or Connes--Consani sources transports a transverse measure, Haar disintegration, representation, von Neumann algebra, FNS trace, trace ideal, return functional, zero-mode projection, analytic family, or determinant along $\Psi_{E_{\mathrm f}}$. A continuous map that collapses fibres cannot choose such data by itself.

# P7-9: the same-object transport certificate {#sec:p79}

The transport certificate asks whether the source and proxy own the same data, in the same representation, with the same domains and normalizations. Table [4](#tab:t0t7){reference-type="ref" reference="tab:t0t7"} records the result. A partial clock or label match does not repair a failed object identity or an absent trace.

::: {#tab:t0t7}
  Gate   Audited evidence                                                                                                         Verdict
  ------ ------------------------------------------------------------------------------------------------------------------------ -----------------------------------
  T0     Distinct candidate IDs; only choice-dependent set coordinates; the $E_{\mathrm f}$ arrow has a different adelic target   Fail for proxy identity
  T1     Packet, prime label, repetitions, and $\log p$ intrinsic; no trace amplitude                                             Partial
  T2     No packet trace or trace test class in the audited source                                                                Not testable
  T3     No source packet operator/domain/spectrum tied to a trace                                                                Not testable
  T4     Exact packet theorems plus a restricted, collapsing topological intertwiner                                              Scoped only
  T5     Clock sourced; central mass, density, phase, and determinant coefficient not transported                                 Fail for analytic weights
  T6     $p^{\mathbb Z}$ and $\log p$ sourced; Fourier, trace, branch, and determinant normalizations selected by proxy           Partial
  T7     Prime support reaches the orbit ledger; analytic prime-power weights do not travel                                       Partial; no determinant promotion

  : T0--T7 transport from the published source to the Paper-7 proxy.
:::

The unit-mass sub-certificate has the same outcome. The map $(p)\leftrightarrow\Gamma_p$ is a source theorem. Counting measure on the set of prime closed points is a target-free new definition. The assignment of that unit to the central trace coefficient $m_p$ is not supplied by either fact. Compatibility with copied proxy components and with the choice-dependent packet coordinates is likewise unproved. Therefore `DEN-WITT-PACKET-DECOMP-K0-M1` remains a modeling choice even though Theorem [\[thm:p75\]](#thm:p75){reference-type="ref" reference="thm:p75"} is exact.

[\[thm:p79\]]{#thm:p79 label="thm:p79"} Within the four full-text ownership sources, the operator-source corpus, and the bounded update search through 14 August 2026, no theorem transports the Paper-7 proxy's product Borel structure, transverse probability, representation, algebra, trace, $L^1$ domain, return record, zero mode, analytic family, or determinant to [`DEN-WITT-Z-FIN`]{.nodecor}. The source owns the packet, repetitions, and clock. The proxy theorems remain proxy-owned.

Theorem [\[thm:p79\]](#thm:p79){reference-type="ref" reference="thm:p79"} is an audited absence statement, not a universal nonexistence theorem. A future enrichment could change the result, but it would need a newly typed object and an explicit transport of every field in Table [4](#tab:t0t7){reference-type="ref" reference="tab:t0t7"}. In particular, a newly introduced groupoid would need specified units, arrows, topology, and Haar system before its trace could be compared with $\tau_m$.

# Route ceilings and non-combinability {#sec:routes}

The route assessment is object-specific. It is invalid to take the arithmetic-origin coordinate from the source, the exact analytic coordinate from the zero-mode proxy, and the best available coordinate from a third record. Such a coordinatewise maximum would certify no single object.

::: {#tab:route}
  Candidate           Final tuple $(A0,A1,A2,A3,A4)$                                                                Overall; B
  ------------------- --------------------------------------------------------------------------------------------- ----------------------
  Published source    (`A0_ANALYTIC_ARITHMETIC_ORIGIN`, `A1_WEAK`, `A2_FAIL`, `A3_FAIL`, `A4_FAIL`)                 `EXPLORATORY`; false
  Mass-family proxy   (`A0_WEAK_ARITHMETIC_RELATION`, `A1_WEAK`, `A2_FAIL`, `A3_FAIL`, `A4_FAIL`)                   `EXPLORATORY`; false
  Return record       (`A0_WEAK_ARITHMETIC_RELATION`, `A1_PASS_ANALYTIC`, `A2_FAIL`, `A3_FAIL`, `A4_FAIL`)          `EXPLORATORY`; false
  Zero-mode record    (`A0_WEAK_ARITHMETIC_RELATION`, `A1_FAIL`, `A2_ANALYTIC_DETERMINANT`, `A3_FAIL`, `A4_FAIL`)   `EXPLORATORY`; false

  : Final object-specific Route-A v0.2.0 verdicts. Tuple coordinates cannot be combined across rows.
:::

The independent object-specific audit is locked at SHA-256 . Each row has the final overall label `ROUTE_A_EXPLORATORY`, and Route-B invocation is false. The common label means only that each object retains a bounded research question; it does not make their coordinates interchangeable. No record receives an analytic-continuation, functional-equation, Gamma, divisor, asymptotic-counting, or Weil-compression credit from [\[eq:unit-product\]](#eq:unit-product){reference-type="eqref" reference="eq:unit-product"}. Route B is closed for every row: no single object owns a Route-A-ready arithmetic/orbit/determinant chain together with a transported operator, domain, and self-adjointness argument. The present result is an exact local analytic statement plus a negative ownership certificate, not a spectral promotion.

# Deterministic controls and reproducibility {#sec:repro}

The proofs above are analytic. A standard-library-only Python package serves as a regression layer for conventions and finite identities; it is not a proof runner. The frozen entry point runs unit tests, regenerates nine CSV tables, verifies artifact and implementation hashes, makes two further regenerations in fresh temporary directories, and compares all bytes.

At the reviewed snapshot the receipt was: $$\text{21/21 tests passed},\quad
 \text{9 CSV artifacts},\quad
 \text{407 data rows},\quad
 \text{669 primes through 5000}.$$ The manifest SHA-256 is

`fe12ec4c6b0a950d35d267c830119945652acafb9a5ddae2aa6b86db92943b26`.

It locks six implementation files as well as the generated tables. The verification suite rejects a tampered CSV, a tampered implementation file, and missing or extra implementation-manifest entries.

The determinant quantities are explicitly named in every relevant table: $$\tau\!\operatorname{-Log}D
   =\sum_jm_j\log(1-e^{-\sigma L_j})<0,
 \quad
 \log Z=-\tau\!\operatorname{-Log}D,
 \quad
 D=e^{\tau\operatorname{-Log}D},
 \quad Z=D^{-1}.
 \label{eq:control-sign}$$ The maximum observed finite Poisson-convention residual was $4.44\times10^{-16}$; the finite product residuals were at most $2.67\times10^{-15}$. The controls use no network, random generator, external dataset, target-zero data, or fitted mass, clock, shift, phase, or cutoff. Finite agreement checks neither establish the infinite theorems nor resolve source ownership.

# Discussion and limitations {#sec:discussion}

The global trace-domain result changes how the prime-period ledger should be read. At a fixed prime, smoothing the circle translation is benign: the Fourier eigenvalues are rapidly decreasing, and the component trace is a standard Poisson sum. Across primes, the trace norm grows like $\log p$. The signed component traces can vanish for all sufficiently large primes when the test function has compact positive-time support, yet the sum of absolute trace norms still diverges. Cancellation in the Fourier lattice is not a domain extension of a normal trace. This is why $\Theta_m$ must be owned by a new distribution record.

The zero-mode branch solves a different problem. It suppresses every nonconstant circle mode and retains one normalized projection per component. This produces the desired logarithmic repetition weights, but the operation is almost maximally insensitive to the transverse object. Replacing a packet base by a point changes the ordinary Hilbert multiplicity from infinite to one and leaves the semifinite formula unchanged. Replacing prime clocks by a general locally finite list likewise retains the compiler when its separate summability domain is nonempty. Exactness therefore establishes a theorem about this ledger design; it does not retroactively identify the design with source geometry.

Five limitations are load-bearing. First, the product topology, base Haar probability, algebra, and trace are selected proxy data. Second, unit masses are a modeling choice at the central trace level, even though prime-index counting is natural. Third, the restricted $E_{\mathrm f}$ map is many-to-one on transverse orbit labels and has a different adelic codomain. Fourth, the source search is bounded: four ownership full texts, the operator corpus, and the documented update screen through the cutoff. Fifth, this paper proves only the right-half-plane principal trace-log scalar and its ownership boundary. None of these limitations is repaired by finite numerical agreement.

The smallest meaningful next theorem is not another scalar identity. It is a same-object construction that begins with the actual packet, supplies a choice-independent Borel or topological transverse model and disintegration, defines the representation and FNS trace from those data, and proves that the relevant test operators and zero modes transport isometrically in the trace ideal. Anything weaker leaves the central ownership gap unchanged.

# Conclusion

The selected packet proxy supports two exact but nonexchangeable analytic records. Branch F gives a trace-class component Poisson formula, a sharp global $L^1$ obstruction, and a separately defined positive-time return measure. Branch K gives a version-corrected affiliated/bounded domain split, relative-norm holomorphy, and a branch-fixed principal trace-log scalar. Its unit-mass Euler product is exact on $\operatorname{Re}s>1$.

That analytic success does not close the source problem. The zero-mode mechanism is blind to probability-base geometry and compiles arbitrary clock ledgers. Unit central masses remain untransported. The corrected $E_{\mathrm f}$ intertwiner supplies genuine continuity, time reversal, and packetwise surjectivity onto the adelic prime orbit, but it is strictly not globally onto, collapses the transverse labels, and carries none of the measured/operator fields. The strongest conclusion is therefore intentionally compound: the proxy theorem is valid, the source ownership certificate is negative, and the two must not be merged into one Route claim.

# P7-1--P7-9 status and dependency ledger

::: {#tab:p7-status}
  Target   Status                         Boundary
  -------- ------------------------------ ---------------------------------------------------------------------------------------------------------------------------
  Target   Status                         Boundary
  P7-1     Proved                         Component bounded $\tau_p$-trace ideal and Poisson formula; not an ordinary Hilbert trace on the intended representation.
  P7-2     Proved                         Global block bounded; for nonzero $f$, global $L^1$ iff $\sum_pm_p\log p<\infty$; unit masses fail.
  P7-3     Proved                         $\Theta_m$ locally finite on positive time; outside global $L^1$ it is not $\tau_m(C_f)$.
  P7-4     Proved, versioned correction   Affiliated summability separated from bounded membership; unit-mass half-plane unchanged.
  P7-5     Proved                         Relative-norm holomorphy and local principal trace-log scalar; determinant taxonomy and ordinary multiplicity closed.
  P7-6     Proved, scoped                 Positive sequences classify only the frozen central-scalar trace family; copied blocks add.
  P7-7     Proved                         Target-series equality forces $m_p=1$ but is circular as a provenance argument.
  P7-8     Proved                         Probability-base blind; arbitrary clocks compile only on their exact independent domains.
  P7-9     Scoped negative certificate    Packets, repetitions, and clocks sourced; no audited measured/operator/determinant transport to proxy.

  : Final theorem/audit status with the surviving boundary.
:::

# Research integrity and declarations

## Source and citation integrity {#source-and-citation-integrity .unnumbered}

All fifteen locally read mathematical PDFs used for source ownership, operator terminology, and determinant comparison are enumerated in the canonical Paper-7 source manifest and had same-stem read-integrity sidecars reporting identical declared, enumerated, and reader page counts. Every positive load-bearing source claim in the main text names a theorem, equation, page, or section locator; bounded whole-text negative searches are identified as such in the source audit. The sources cited for load-bearing facts are primary articles, author preprints, or official journal manifestations. The source audit distinguishes source theorems, new derivations, new definitions, modeling choices, and bounded negative searches.

## Data and code availability {#data-and-code-availability .unnumbered}

No external empirical dataset was used. The deterministic source code, tests, reproduction script, nine result tables, and schema-v2 hash manifest are distributed with the accompanying Paper-7 research directory. Running `./experiments/reproduce.sh` from that directory regenerates and verifies the package. The controls are finite regression witnesses and must not be interpreted as proof of an infinite theorem or a source-transport claim.

## Ethics statement {#ethics-statement .unnumbered}

This mathematical study involved no human participants, animals, clinical records, or personal data. Institutional review and informed consent are not applicable.

## Author identity and contributions {#author-identity-and-contributions .unnumbered}

Liang Wang: Conceptualization, Methodology, Formal analysis, Investigation, Software, Validation, Data curation, Visualization, Writing---original draft, and Writing---review and editing. An AI system is not an author and cannot accept responsibility for the work.

## Competing interests {#competing-interests .unnumbered}

The author declares no financial or non-financial conflict of interest.

## Funding {#funding .unnumbered}

No project-specific external funding source was declared.

## AI-use disclosure {#ai-use-disclosure .unnumbered}

Generative AI assisted literature triage, proof and domain cross-checking, deterministic-code drafting, adversarial review, manuscript drafting, and formatting. The research workflow retained exact source manifestations, locators, hashes, versioned amendments, independent review records, and target-free controls. No unpublished material was uploaded to a secondary model, and no cross-model review was claimed. The human author directed the research questions and acceptance criteria, must verify every mathematical statement and citation before submission, and takes full responsibility for the final manuscript.

## Acknowledgments {#acknowledgments .unnumbered}

No personal acknowledgments are declared.
