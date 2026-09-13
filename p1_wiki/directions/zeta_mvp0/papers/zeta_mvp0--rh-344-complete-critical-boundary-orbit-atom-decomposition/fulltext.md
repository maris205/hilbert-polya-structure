---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-344-complete-critical-boundary-orbit-atom-decomposition"
canonical_tex: "zeta_mvp0/papers/RH-344-complete-critical-boundary-orbit-atom-decomposition/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-344-complete-critical-boundary-orbit-atom-decomposition/main.pdf"
source_sha256: "db30291df579aa6525348f5ed8a184c10f61205acb839e808964c0f44f01ddf5"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Complete Critical Boundary-Orbit Atom and the Double-Alias Compensation Demand

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-344-complete-critical-boundary-orbit-atom-decomposition>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-344-complete-critical-boundary-orbit-atom-decomposition/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-344-complete-critical-boundary-orbit-atom-decomposition/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-344-complete-critical-boundary-orbit-atom-decomposition/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-344-complete-critical-boundary-orbit-atom-decomposition/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  At the physical first alias, RH-338 extracted $2k-1$ marked points of the primitive boundary orbit from the frozen far cell. We complete that extraction across the full RH-334 raw partition. Let $$\Gamma_k=\{|f^j(p_k)|:0\le j<2k\},\qquad
   G_k=\frac{r_H^{-2k}}{1+|M_k|}.$$ The folded orbit has exactly $2k$ distinct points, every point has multiplier $M_k$, and finite-set localization has zero noisy trace. Thus the complete signed raw atom is $-F_k^{\rm orb}$, where $F_k^{\rm orb}=2kG_k$.

  The sole point not certified far by RH-338 is $\xi_k=h(p_k)<b$. With $\epsilon_k=\mathbf 1_{\{\xi_k\in J^-\}}$, the eventual orbit counts in $(J^-,J^+,F)$ are exactly $(\epsilon_k,0,2k-\epsilon_k)$. Removing the full orbit before evaluating the deterministic rest gives $$q_{\sigma,k,2k}=\mathcal T_k^{\rm rest}+\mathcal P_{\sigma,2k}
   -\mathcal A_{k,2k}-F_k^{\rm orb}.$$ Since the direct coefficient is $p=q-d$, critical direct closure requires $$\mathcal T_k^{\rm rest}+\mathcal P_{\sigma,2k}-d_{\sigma,k,2k}
   =\mathcal A_{k,2k}+F_k^{\rm orb}+o(H_k).$$ The missing point is not target-negligible. If $D_k^{\rm orb}=(2k-1)G_k$ is the RH-338 atom, then $F_k^{\rm orb}-D_k^{\rm orb}=G_k$ and $$\frac{G_k}{H_k}=\frac{(\beta R)^{2k}}{C_Mk}\{1+o(1)\}\longrightarrow\infty.$$ Moreover $F_k^{\rm orb}/\mathcal A_{k,2k}\to1$, so the required positive side is asymptotically twice the alias packet. This is an exact physical raw-trace decomposition and a necessary compensation law, not a compensation theorem. The orbit-free rest, critical verdict, strict prefix, determinant gluing, and Gates A--E remain open. No Riemann-hypothesis conclusion follows.
author:
- Bin Wang
bibliography:
- references.bib
date: August 2026
title: 'A Complete Critical Boundary-Orbit Atom and the Double-Alias Compensation Demand'
```

## Markdown 正文

# Source-locked orbit and observation type

Let $u_c\in(1,2)$ be the real root of $$\label{eq:uc}
 u_c^3-2u_c^2+2u_c-2=0,$$ and put $$\label{eq:physical}
 f(x)=1-u_cx^2,\qquad r=u_c-1,\qquad
 \lambda=2u_cr>1,\qquad b=u_c^{-1/2}.$$ The two-step component map is $S=f^2$. Its inverse branch used by the boundary word is $$\label{eq:h}
 h(x)=\sqrt{\frac{1-\sqrt{(1-x)/u_c}}{u_c}},
 \qquad h(1)=b.$$ Let $p_k=p_{2k}$ be the primitive point coded by $CA(CB)^{k-1}$. RH-17 proves that the $S$-orbit is the ordered chain $$\label{eq:S-chain}
 p_k,h^{k-1}(p_k),h^{k-2}(p_k),\ldots,h(p_k),$$ and that its physical multiplier obeys $$\label{eq:M}
 M_k=(f^{2k})'(p_k)=(S^k)'(p_k)
 =-C_M\lambda^k\{1+o(1)\},\qquad C_M>0.$$ Primitivity gives $2k$ distinct signed marked points [@WangLongCycle2026; @WangBoundaryMonodromy2026].

Work on the exact physical clock and Hardy normalization $$\label{eq:clock}
 k=\frac{\log(1/\sigma)}{2\log\lambda}+O(1),\qquad
 r_H=\frac{17}{20},\qquad R=\frac75,\qquad
 H_k=kR^{-2k}.$$ For fixed $A>0$, freeze the corrected RH-334 partition $$\begin{aligned}
 J^-&=[0,1]\cap[b-A\sqrt\sigma,b),\label{eq:Jminus}\\
 J^+&=[0,1]\cap[b,b+A\sqrt\sigma],\label{eq:Jplus}\\
 F&=[0,1]\setminus(J^-\cup J^+).\label{eq:F}\end{aligned}$$ For measurable $J\subset[0,1]$ let $$\label{eq:localized}
 L_{\sigma,n}(J)=\operatorname{Tr}(M_JK_\sigma^n),\qquad
 P_n^{\rm abs}(J)=
 \sum_{\substack{f^n(x)=x\\ |x|\in J}}
 \frac1{|1-(f^n)'(x)|}.$$ RH-334 proves that absolute value is a multiplier-preserving bijection from the signed fixed points to the folded fixed points, preserving minimal period and marked-point multiplicity. It also proves the exact raw partition $$\label{eq:raw}
 \mathcal T_{\sigma,n}:=r_H^{-n}
 \{\operatorname{Tr}K_\sigma^n-P_n\}
 =\mathcal B_{\sigma,k,n}+\mathcal S_{\sigma,k,n}+\mathcal R_{\sigma,k,n},$$ where each slot is the localized noisy trace minus the localized deterministic flat trace on the corresponding frozen cell [@WangObservation2026]. These are cyclic trace observations, not forward probabilities.

# Complete cellwise orbit extraction

Define the complete folded marked orbit and its critical member by $$\label{eq:Gamma}
 \Gamma_k=\{|f^j(p_k)|:0\le j<2k\},\qquad
 \xi_k=|f^{2k-2}(p_k)|=h(p_k)<b.$$ RH-338 proves that the other $2k-1$ marked points form a set $\Omega_k\subset F$ eventually. The location of $\xi_k$ is left open there because its distance from $b$ is on the window scale [@WangFarAtom2026].

Put $$\label{eq:G}
 G_k=\frac{r_H^{-2k}}{1+|M_k|},\qquad
 \epsilon_k=\mathbf 1_{\{\xi_k\in J^-\}}.$$

[\[thm:cellwise\]]{#thm:cellwise label="thm:cellwise"} For all sufficiently large $k$, $\Gamma_k$ consists of $2k$ distinct folded marked points with common flat-trace weight $(1+|M_k|)^{-1}$. Its counts in $(J^-,J^+,F)$ are $$\label{eq:counts}
 (\epsilon_k,0,2k-\epsilon_k).$$ Define orbit-free rest slots by applying the same localized raw ledger to $J^-\setminus\Gamma_k$, $J^+\setminus\Gamma_k$, and $F\setminus\Gamma_k$. Then exactly $$\begin{aligned}
 \mathcal B_{\sigma,k,2k}&=\mathcal B_k^{\rm rest}-\epsilon_kG_k,
 \label{eq:Brest}\\
 \mathcal S_{\sigma,k,2k}&=\mathcal S_k^{\rm rest},
 \label{eq:Srest}\\
 \mathcal R_{\sigma,k,2k}&=\mathcal R_k^{\rm rest}-(2k-\epsilon_k)G_k.
 \label{eq:Rrest}\end{aligned}$$ Consequently, with $$\label{eq:Trest}
 \mathcal T_k^{\rm rest}=\mathcal B_k^{\rm rest}+\mathcal S_k^{\rm rest}
 +\mathcal R_k^{\rm rest},\qquad F_k^{\rm orb}=2kG_k,$$ the full raw trace has the partition-independent decomposition $$\label{eq:raw-complete}
 \boxed{\mathcal T_{\sigma,2k}=\mathcal T_k^{\rm rest}-F_k^{\rm orb}.}$$

The folding bijection and primitivity give the cardinality and common multiplier. Equation [\[eq:M\]](#eq:M){reference-type="eqref" reference="eq:M"} is negative eventually, so each physical weight is $(1+|M_k|)^{-1}$. The $2k-1$ points of $\Omega_k$ lie in $F$, while $\xi_k<b$ lies in either $J^-$ or $F$ and never in $J^+$. This proves [\[eq:counts\]](#eq:counts){reference-type="eqref" reference="eq:counts"}.

A finite set has zero multiplication operator on $L^2[0,1]$. Therefore its localized noisy trace vanishes exactly. Removing a marked point changes a raw cell ledger only by deleting its positive deterministic weight, which proves [\[eq:Brest\]](#eq:Brest){reference-type="eqref" reference="eq:Brest"}--[\[eq:Rrest\]](#eq:Rrest){reference-type="eqref" reference="eq:Rrest"}. Summation cancels the allocation $\epsilon_k$ and gives [\[eq:raw-complete\]](#eq:raw-complete){reference-type="eqref" reference="eq:raw-complete"}.

The rest still contains the noisy trace over a full-measure set and every other deterministic periodic point. No sign, localization estimate, or smallness claim is attached to it. The analytic subpartition exposes an exact constituent of the already-frozen physical observation; it does not replace that observation by a fitted window.

# The typed critical coefficient

Retain the RH-334 parity and alias packets $$\begin{aligned}
 \mathcal P_{\sigma,n}&=r_H^{-n}\{(-1)^n-\lambda_-(\sigma)^n\},
 \label{eq:parity}\\
 \mathcal A_{k,n}&=s_{k,n}-p_n^{\rm pole}.
 \label{eq:alias-general}\end{aligned}$$ At $n=2k$, $$\label{eq:alias}
 \mathcal A_{k,2k}=(2k-2)\beta_k^{2k}+2\beta^{2k},\qquad
 \beta_k^{2k}=\frac{r_H^{-2k}}{|M_k|},\qquad
 \beta=\frac1{r_H\sqrt\lambda}.$$ The Hardy full-trace constituent and direct modulus-complement coefficient obey $$\label{eq:pq}
 q_{\sigma,k,n}=\mathcal T_{\sigma,n}+\mathcal P_{\sigma,n}-\mathcal A_{k,n},
 \qquad
 p_{\sigma,k,n}=q_{\sigma,k,n}-d_{\sigma,k,n},$$ where $d_{\sigma,k,n}=h_{\sigma,n}-s_{k,n}$ is the separate noisy-head/counterloop defect [@WangObservation2026].

[\[thm:critical\]]{#thm:critical label="thm:critical"} At the physical critical order, $$\begin{aligned}
 q_{\sigma,k,2k}
 &=\mathcal T_k^{\rm rest}+\mathcal P_{\sigma,2k}
   -\mathcal A_{k,2k}-F_k^{\rm orb},\label{eq:q-complete}\\
 p_{\sigma,k,2k}
 &=\mathcal T_k^{\rm rest}+\mathcal P_{\sigma,2k}-d_{\sigma,k,2k}
   -\mathcal A_{k,2k}-F_k^{\rm orb}.
 \label{eq:p-complete}\end{aligned}$$ Consequently $$\label{eq:compensation}
 p_{\sigma,k,2k}=o(H_k)
 \quad\Longleftrightarrow\quad
 \mathcal T_k^{\rm rest}+\mathcal P_{\sigma,2k}-d_{\sigma,k,2k}
 =\mathcal A_{k,2k}+F_k^{\rm orb}+o(H_k).$$ In particular, vanishing of the direct weighted prefix at the strict cut $2\le n<4k$ implies [\[eq:compensation\]](#eq:compensation){reference-type="eqref" reference="eq:compensation"}.

Substitute [\[eq:raw-complete\]](#eq:raw-complete){reference-type="eqref" reference="eq:raw-complete"} into [\[eq:pq\]](#eq:pq){reference-type="eqref" reference="eq:pq"}; this gives [\[eq:q-complete\]](#eq:q-complete){reference-type="eqref" reference="eq:q-complete"} and [\[eq:p-complete\]](#eq:p-complete){reference-type="eqref" reference="eq:p-complete"}. Rearrangement proves the equivalence. The critical summand in the nonnegative direct prefix is $$\frac{|p_{\sigma,k,2k}|R^{2k}}{2k}
 =\frac{|p_{\sigma,k,2k}|}{2H_k}.$$ Thus prefix vanishing forces $p_{\sigma,k,2k}=o(H_k)$.

This theorem expands the quantity used by RH-340. If $D_k^{\rm orb}=(2k-1)G_k$ and $C_k^0=q_{\sigma,k,2k}+D_k^{\rm orb}$, then exactly $$\label{eq:C0}
 \boxed{C_k^0=\mathcal T_k^{\rm rest}+\mathcal P_{\sigma,2k}
 -\mathcal A_{k,2k}-G_k.}$$ Hence the RH-340 law $C_k^0-d=D_k^{\rm orb}+o(H_k)$ is algebraically equivalent to [\[eq:compensation\]](#eq:compensation){reference-type="eqref" reference="eq:compensation"}; the advance is the physical decomposition of its previously unexpanded combined complement [@WangSynchronizedPrefix2026].

# The omitted marked point is super-target

[\[thm:scales\]]{#thm:scales label="thm:scales"} As $k\to\infty$, $$\begin{aligned}
 F_k^{\rm orb}
 &=\frac{2k}{C_M}\beta^{2k}\{1+o(1)\},
 \label{eq:F-asymptotic}\\
 \frac{F_k^{\rm orb}}{\mathcal A_{k,2k}}&\longrightarrow1,
 \label{eq:F-over-A}\\
 \frac{F_k^{\rm orb}}{H_k}
 &=\frac2{C_M}(\beta R)^{2k}\{1+o(1)\}\longrightarrow\infty.
 \label{eq:F-over-H}\end{aligned}$$ Moreover $$\label{eq:F-D}
 \frac{F_k^{\rm orb}}{D_k^{\rm orb}}=\frac{2k}{2k-1},
 \qquad F_k^{\rm orb}-D_k^{\rm orb}=G_k,$$ but $$\label{eq:G-over-H}
 \frac{G_k}{H_k}
 =\frac1{C_Mk}(\beta R)^{2k}\{1+o(1)\}
 \longrightarrow\infty.$$ Finally, $$\begin{aligned}
 \mathcal A_{k,2k}+F_k^{\rm orb}
 &=\frac{4k}{C_M}\beta^{2k}\{1+o(1)\},
 \label{eq:double}\\
 \frac{\mathcal A_{k,2k}+F_k^{\rm orb}}{\mathcal A_{k,2k}}
 &\longrightarrow2.
 \label{eq:double-ratio}\end{aligned}$$

Equation [\[eq:M\]](#eq:M){reference-type="eqref" reference="eq:M"} gives $$G_k=\frac1{C_M}\beta^{2k}\{1+o(1)\}.$$ Multiplication by $2k$ proves [\[eq:F-asymptotic\]](#eq:F-asymptotic){reference-type="eqref" reference="eq:F-asymptotic"}. RH-338 gives the same leading asymptotic for [\[eq:alias\]](#eq:alias){reference-type="eqref" reference="eq:alias"}, proving [\[eq:F-over-A\]](#eq:F-over-A){reference-type="eqref" reference="eq:F-over-A"}. Division by $H_k$ gives [\[eq:F-over-H\]](#eq:F-over-H){reference-type="eqref" reference="eq:F-over-H"}. The exact RH-336 certificate $\beta R>1$ makes the limit infinite [@WangProjectorMass2026; @WangFarAtom2026].

Equations [\[eq:F-D\]](#eq:F-D){reference-type="eqref" reference="eq:F-D"} are immediate from the exact marked-point counts. Dividing the asymptotic for $G_k$ by $H_k$ proves [\[eq:G-over-H\]](#eq:G-over-H){reference-type="eqref" reference="eq:G-over-H"}; an exponential with base $\beta R>1$ dominates $k$. Adding the two equal leading asymptotics proves [\[eq:double\]](#eq:double){reference-type="eqref" reference="eq:double"}--[\[eq:double-ratio\]](#eq:double-ratio){reference-type="eqref" reference="eq:double-ratio"}.

Thus the relative statement $F_k^{\rm orb}=D_k^{\rm orb}\{1+o(1)\}$ is true, but the target-scale replacement $F_k^{\rm orb}=D_k^{\rm orb}+o(H_k)$ is false. The exact finite-$k$ normalization also gives $$\label{eq:finite-relation}
 \mathcal A_{k,2k}-F_k^{\rm orb}
 =2(\beta^{2k}-\beta_k^{2k})
 +\frac{2k\beta_k^{2k}}{1+|M_k|}.$$ The repository does not lock the sign of this expression, and none is used.

Relative to the positive demand in [\[eq:compensation\]](#eq:compensation){reference-type="eqref" reference="eq:compensation"}, target closure requires precision $$\label{eq:precision}
 o\!\left(\frac{H_k}{\mathcal A_{k,2k}+F_k^{\rm orb}}\right)
 =o\!\left((\beta R)^{-2k}\right).$$ This remains a signed aggregate requirement. Taking separate absolute values of the alias, orbit, parity, rest, and head terms cannot demonstrate the cancellation.

# Phase-resolved cell allocation

The aggregate atom is independent of the unresolved cell allocation, but the latter can be stated sharply. Define $$\label{eq:qb}
 q_{{\rm b},\sigma,k}=\frac{b-h(p_k)}{\sqrt\sigma},\qquad
 \eta_\sigma=k-\frac{\log(1/\sigma)}{2\log\lambda}.$$ The half-open endpoint convention gives the exact finite relation $$\label{eq:epsilon}
 \epsilon_k=\mathbf 1_{\{q_{{\rm b},\sigma,k}\le A\}}.$$ RH-327 proves, along $\eta_\sigma\to\eta$, $$\label{eq:qb-limit}
 q_{{\rm b},\sigma,k}\longrightarrow
 Q(\eta):=\frac{\sqrt{C_{\rm b}}\lambda^{-\eta}}{2u_c}.$$ Therefore $\epsilon_k$ is eventually one if $Q(\eta)<A$ and eventually zero if $Q(\eta)>A$. At $Q(\eta)=A$, the available $o(1)$ expansion does not decide stabilization. Exact finite equality belongs to $J^-$ because its left endpoint is included. This phase sensitivity is why $F_k^{\rm orb}$ is a complete raw-partition atom, not always a far atom [@WangNeighboringBudget2026].

# Executable audit and claim boundary

The artifact reconstructs the boundary orbit at $k=2,4,8,16,32$, checks all $2k$ folded points and their cell counts, evaluates the exact missing-point and complete-orbit identities, and reproduces the approach to the scale ratios. A rational fixture independently verifies the typed equations [\[eq:q-complete\]](#eq:q-complete){reference-type="eqref" reference="eq:q-complete"}--[\[eq:p-complete\]](#eq:p-complete){reference-type="eqref" reference="eq:p-complete"}. These finite rows are formula checks only, never all-order or physical-convergence evidence.

The exact new edge is limited to the complete physical orbit subledger, its cellwise raw decomposition, the target-supercritical missing point, and the necessary compensation law. No theorem estimates $\mathcal T_k^{\rm rest}-d_{\sigma,k,2k}$ at moving order. Hence critical signed compensation and critical nonclosure both remain `NOT_TESTABLE`/open. No conclusion follows for the actual $D_{4k}$ head budget, the lower sideband, the remaining off-alias background, or the direct strict prefix.

RH-343's finite normal models are not substituted for this physical raw trace [@WangEqualInvariant2026]. RH-288 remains inactive, and the ten-layer frontier of RH-341 is not promoted [@WangActualFrontier2026]. Gates A--E remain false/open. This paper constructs no Hilbert--Polya operator, identifies no Riemann zero, proves no von Mangoldt prime-power trace, proves no completed-zeta divisor equality, and does not prove the Riemann Hypothesis.
