---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-346-complete-lower-sideband-boundary-orbit-decomposition"
canonical_tex: "zeta_mvp0/papers/RH-346-complete-lower-sideband-boundary-orbit-decomposition/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-346-complete-lower-sideband-boundary-orbit-decomposition/main.pdf"
source_sha256: "5b433acd866763e9b12dddb0153b39e7b4733c625bec97f2476dc430cf982063"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Complete Lower-Sideband Boundary-Orbit Decomposition

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-346-complete-lower-sideband-boundary-orbit-decomposition>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-346-complete-lower-sideband-boundary-orbit-decomposition/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-346-complete-lower-sideband-boundary-orbit-decomposition/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-346-complete-lower-sideband-boundary-orbit-decomposition/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-346-complete-lower-sideband-boundary-orbit-decomposition/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We complete the physical boundary-orbit extraction at the mandatory lower sideband $n_-=2k-2=2m$, where $m=k-1$ is an orbit-period parameter on the same $(\sigma,k)$ noise clock. Let $$\Gamma_m=\{|f^j(p_{2m})|:0\le j<2m\},\qquad
   G_m=\frac{r_H^{-2m}}{1+|M_m|}.$$ The folded orbit has exactly $2m$ distinct marked points and contributes the complete signed raw atom $-F_m^{\rm orb}$, $F_m^{\rm orb}=2mG_m$. Its last critical point $\xi_m=h(p_{2m})$ lies in $J^-$ or $F$ according to $\epsilon_m=\mathbf 1_{\{\xi_m\in J^-\}}$. The eventual cell counts are $(\epsilon_m,0,2m-\epsilon_m)$, and on a fixed physical phase $$\frac{b-\xi_m}{\sqrt\sigma}
   \longrightarrow\frac{\sqrt{C_{\rm b}}}{2u_c}\lambda^{1-\eta}.$$ The factor $\lambda$ records that $m=k-1$ while the noise clock remains $k$.

  Removing the complete orbit gives the exact direct coefficient $$p_{\sigma,k,2m}=\mathcal T_{k,m}^{\rm rest}+\mathcal P_{\sigma,2m}
   -d_{\sigma,k,2m}-\mathcal A_{k,2m}-F_m^{\rm orb}.$$ The point omitted by RH-339 is again super-target: $G_m/H_m=(C_Mm)^{-1}(\beta R)^{2m}\{1+o(1)\}\to\infty$. The current period-$2k$ counterloop radial sideband has unknown sign but the sharp relative law $$\frac{\mathcal A_{k,2m}}{F_m^{\rm orb}}
   =\frac{C_M-1}{m}+o(m^{-1})\longrightarrow0.$$ Thus the combined deterministic demand is eventually positive and asymptotic to the complete orbit atom, while neither its radial correction nor the orbit-free rest is proved target-negligible. We also obtain the shifted scalar interface $\mathcal P_{\sigma,2m}/F_m^{\rm orb}\to C_*C_M\lambda^{\eta-1}$. No lower compensation, off-alias closure, determinant gluing, Gate progress, or Riemann-hypothesis conclusion follows.
author:
- Bin Wang
bibliography:
- references.bib
date: August 2026
title: 'A Complete Lower-Sideband Boundary-Orbit Decomposition'
```

## Markdown 正文

# One noise clock and the mandatory sideband

Work on the physical clock $$\label{eq:clock}
 k=\frac{\log(1/\sigma)}{2\log\lambda}+O(1),\qquad
 \eta_\sigma=k-\frac{\log(1/\sigma)}{2\log\lambda},\qquad
 R=\frac75.$$ Set $$\label{eq:m}
 m=k-1,\qquad n_-=2m=2k-2,\qquad H_m=mR^{-2m}.$$ The symbol $m$ indexes a deterministic boundary orbit. It does not define a new noise sequence. Every one-alias cut $2k<h_\sigma\le4k$ contains $n_-$ in its strict off-alias prefix [@WangLowerAtom2026].

Retain the same corrected folded noisy operator and the same frozen RH-334 cells $$\begin{aligned}
 J^-&=[0,1]\cap[b-A\sqrt\sigma,b),\label{eq:Jminus}\\
 J^+&=[0,1]\cap[b,b+A\sqrt\sigma],\label{eq:Jplus}\\
 F&=[0,1]\setminus(J^-\cup J^+).\label{eq:F}\end{aligned}$$ For every order $n\ge2$, the all-order physical identity is $$\label{eq:five-slot}
 q_{\sigma,k,n}=\mathcal B_{\sigma,k,n}+\mathcal S_{\sigma,k,n}
 +\mathcal R_{\sigma,k,n}+\mathcal P_{\sigma,n}-\mathcal A_{k,n},$$ and the direct coefficient is $$\label{eq:direct}
 p_{\sigma,k,n}=q_{\sigma,k,n}-d_{\sigma,k,n}.$$ Here $d$ is the separate noisy-head/counterloop defect. No full-trace/direct identification is assumed [@WangObservation2026; @WangSynchronizedPrefix2026].

At $n=2m$, the current period-$2k$ counterloop contributes the exact radial sideband $$\label{eq:radial}
 \mathcal A_{k,2m}=2(\beta^{2m}-\beta_k^{2m}),
 \qquad
 \beta_k=\frac{|M_k|^{-1/(2k)}}{r_H},
 \qquad
 \beta=\frac1{r_H\sqrt\lambda}.$$ It is not an alias impulse of the period-$2k$ counterloop, and its sign is not fixed below [@WangFirstAlias2026].

# Complete period-$2m$ orbit extraction

Let $p_{2m}$ be the primitive boundary point and put $$\label{eq:Gamma}
 \Gamma_m=\{|f^j(p_{2m})|:0\le j<2m\},
 \qquad \xi_m=h(p_{2m})<b.$$ RH-17 gives the ordered orbit and multiplier $$\label{eq:Mm}
 M_m=(f^{2m})'(p_{2m})=-C_M\lambda^m\{1+o(1)\},
 \qquad C_M>0,$$ and RH-339 proves that the other $2m-1$ folded points lie in $F$ eventually [@WangBoundaryMonodromy2026; @WangLowerAtom2026].

Define $$\label{eq:Gm}
 G_m=\frac{r_H^{-2m}}{1+|M_m|},
 \qquad
 \epsilon_m=\mathbf 1_{\{\xi_m\in J^-\}}.$$

[\[thm:complete\]]{#thm:complete label="thm:complete"} For all sufficiently large $k$, $\Gamma_m$ has exactly $2m$ distinct folded marked points with counts $$\label{eq:counts}
 (\epsilon_m,0,2m-\epsilon_m)$$ in $(J^-,J^+,F)$. Define orbit-free raw rest slots by deleting $\Gamma_m$ from each frozen cell. Then $$\begin{aligned}
 \mathcal B_{\sigma,k,2m}&=\mathcal B_{k,m}^{\rm rest}-\epsilon_mG_m,
 \label{eq:Brest}\\
 \mathcal S_{\sigma,k,2m}&=\mathcal S_{k,m}^{\rm rest},
 \label{eq:Srest}\\
 \mathcal R_{\sigma,k,2m}&=\mathcal R_{k,m}^{\rm rest}-(2m-\epsilon_m)G_m.
 \label{eq:Rrest}\end{aligned}$$ Thus, with $$\label{eq:Trest}
 \mathcal T_{k,m}^{\rm rest}=\mathcal B_{k,m}^{\rm rest}
 +\mathcal S_{k,m}^{\rm rest}+\mathcal R_{k,m}^{\rm rest},
 \qquad F_m^{\rm orb}=2mG_m,$$ the exact aggregate raw identity is $$\label{eq:raw-complete}
 \boxed{\mathcal T_{\sigma,2m}=\mathcal T_{k,m}^{\rm rest}-F_m^{\rm orb}.}$$

Primitivity and the RH-334 multiplier-preserving folding bijection give the cardinality and common weight. The retained $2m-1$ points lie in $F$, while $\xi_m<b$ lies in $J^-$ or $F$ and never in $J^+$. A finite set has zero multiplication operator on $L^2$, so its localized noisy trace vanishes. Deleting its deterministic marked-point weights gives [\[eq:Brest\]](#eq:Brest){reference-type="eqref" reference="eq:Brest"}--[\[eq:Rrest\]](#eq:Rrest){reference-type="eqref" reference="eq:Rrest"}; summation proves [\[eq:raw-complete\]](#eq:raw-complete){reference-type="eqref" reference="eq:raw-complete"}.

The exact allocation is phase sensitive. Put $$\label{eq:qbm}
 q_{{\rm b},m}=\frac{b-\xi_m}{\sqrt\sigma}.$$ The RH-327 inverse-branch expansion, applied to the period parameter $m$ but the same $\sigma$, gives $$\label{eq:qbm-limit}
 q_{{\rm b},m}\longrightarrow
 \frac{\sqrt{C_{\rm b}}}{2u_c}\lambda^{1-\eta}$$ along $\eta_\sigma\to\eta$. Indeed $C_{\rm b}\lambda^{-2m}/\sigma
\to C_{\rm b}\lambda^{2-2\eta}$. Therefore $\epsilon_m=\mathbf 1_{\{q_{{\rm b},m}\le A\}}$ stabilizes away from equality of the limit with $A$; at equality the source $o(1)$ term does not decide stabilization [@WangNeighboringBudget2026].

# Exact typed lower coefficient

[\[thm:coefficient\]]{#thm:coefficient label="thm:coefficient"} At $n_-=2m$, $$\begin{aligned}
 q_{\sigma,k,2m}
 &=\mathcal T_{k,m}^{\rm rest}+\mathcal P_{\sigma,2m}
 -\mathcal A_{k,2m}-F_m^{\rm orb},
 \label{eq:q-lower}\\
 p_{\sigma,k,2m}
 &=\mathcal T_{k,m}^{\rm rest}+\mathcal P_{\sigma,2m}-d_{\sigma,k,2m}
 -\mathcal A_{k,2m}-F_m^{\rm orb}.
 \label{eq:p-lower}\end{aligned}$$ Consequently $$\label{eq:direct-compensation}
 p_{\sigma,k,2m}=o(H_m)
 \quad\Longleftrightarrow\quad
 \mathcal T_{k,m}^{\rm rest}+\mathcal P_{\sigma,2m}-d_{\sigma,k,2m}
 =\mathcal A_{k,2m}+F_m^{\rm orb}+o(H_m).$$ The analogous full-trace statement omits $d_{\sigma,k,2m}$.

Substitute [\[eq:raw-complete\]](#eq:raw-complete){reference-type="eqref" reference="eq:raw-complete"} into [\[eq:five-slot\]](#eq:five-slot){reference-type="eqref" reference="eq:five-slot"}, then use [\[eq:direct\]](#eq:direct){reference-type="eqref" reference="eq:direct"}. Rearrangement proves the equivalence.

Every direct prefix containing $2m$ has the nonnegative summand $$\label{eq:weighted}
 \frac{|p_{\sigma,k,2m}|R^{2m}}{2m}
 =\frac{|p_{\sigma,k,2m}|}{2H_m}.$$ Thus direct prefix closure implies [\[eq:direct-compensation\]](#eq:direct-compensation){reference-type="eqref" reference="eq:direct-compensation"}. Likewise RH-339's off-alias full-trace prefix forces the $q$ version. Neither converse controls the remaining orders.

If $D_m^{\rm orb}=(2m-1)G_m$ is the RH-339 partial atom and $C_k^-=q_{\sigma,k,2m}+D_m^{\rm orb}$, then exactly $$\label{eq:Cminus}
 C_k^-=\mathcal T_{k,m}^{\rm rest}+\mathcal P_{\sigma,2m}
 -\mathcal A_{k,2m}-G_m.$$ This physically expands the combined complement used in the earlier necessary compensation law.

# Missing point and radial sideband scales

[\[thm:scales\]]{#thm:scales label="thm:scales"} As $m=k-1\to\infty$, $$\begin{aligned}
 F_m^{\rm orb}
 &=\frac{2m}{C_M}\beta^{2m}\{1+o(1)\},
 \label{eq:F-scale}\\
 \frac{F_m^{\rm orb}}{H_m}
 &=\frac2{C_M}(\beta R)^{2m}\{1+o(1)\}
 \longrightarrow\infty.
 \label{eq:F-over-H}\end{aligned}$$ Moreover $$\label{eq:partial-full}
 \frac{F_m^{\rm orb}}{D_m^{\rm orb}}=\frac{2m}{2m-1},
 \qquad
 F_m^{\rm orb}-D_m^{\rm orb}=G_m,$$ and $$\label{eq:G-over-H}
 \frac{G_m}{H_m}
 =\frac1{C_Mm}(\beta R)^{2m}\{1+o(1)\}
 \longrightarrow\infty.$$ The radial counterloop term satisfies the sharp relative law $$\label{eq:radial-relative}
 \boxed{
 \frac{\mathcal A_{k,2m}}{F_m^{\rm orb}}
 =\frac{C_M-1}{m}+o(m^{-1})\longrightarrow0.}$$ Consequently $$\label{eq:combined-positive}
 S_m^-:=F_m^{\rm orb}+\mathcal A_{k,2m}>0
 \quad\hbox{eventually},
 \qquad
 \frac{S_m^-}{F_m^{\rm orb}}\longrightarrow1.$$

The multiplier law [\[eq:Mm\]](#eq:Mm){reference-type="eqref" reference="eq:Mm"} gives $G_m=C_M^{-1}\beta^{2m}\{1+o(1)\}$, proving [\[eq:F-scale\]](#eq:F-scale){reference-type="eqref" reference="eq:F-scale"}--[\[eq:G-over-H\]](#eq:G-over-H){reference-type="eqref" reference="eq:G-over-H"}; RH-336 supplies the exact $\beta R>1$ certificate [@WangProjectorMass2026].

For the current period-$2k$ counterloop, $$\label{eq:beta-k-asymptotic}
 \beta_k=\beta\exp\left[-\frac{\log C_M}{2k}+o(k^{-1})\right].$$ Since $m/k\to1$, $$\frac{\beta_k^{2m}}{\beta^{2m}}
 =\exp\{-\tfrac{m}{k}\log C_M+o(1)\}
 \longrightarrow C_M^{-1}.$$ Insert this into [\[eq:radial\]](#eq:radial){reference-type="eqref" reference="eq:radial"}: $$\mathcal A_{k,2m}
 =2\beta^{2m}\{1-C_M^{-1}+o(1)\}.$$ Division by [\[eq:F-scale\]](#eq:F-scale){reference-type="eqref" reference="eq:F-scale"} proves [\[eq:radial-relative\]](#eq:radial-relative){reference-type="eqref" reference="eq:radial-relative"}. Equation [\[eq:combined-positive\]](#eq:combined-positive){reference-type="eqref" reference="eq:combined-positive"} follows without any sign assumption on the radial term.

The radial sideband is small only relative to the full orbit atom. Because $F_m^{\rm orb}/H_m\to\infty$, [\[eq:radial-relative\]](#eq:radial-relative){reference-type="eqref" reference="eq:radial-relative"} does not prove $\mathcal A_{k,2m}=o(H_m)$. Its sign and target scale remain source-unresolved. The missing point $G_m$, by contrast, is definitely super-target.

# Shifted lower parity interface

The actual square-root parity law gives, since $m\sqrt\sigma\to0$, $$\label{eq:P-lower-asymptotic}
 \mathcal P_{\sigma,2m}
 =2mC_*\sqrt\sigma\,r_H^{-2m}\{1+o(1)\}.$$

[\[cor:phase\]]{#cor:phase label="cor:phase"} Along $\eta_\sigma\to\eta$, $$\label{eq:lower-phase}
 \frac{\mathcal P_{\sigma,2m}}{F_m^{\rm orb}}
 \longrightarrow C_*C_M\lambda^{\eta-1},
 \qquad
 \frac{\mathcal P_{\sigma,2m}}{S_m^-}
 \longrightarrow C_*C_M\lambda^{\eta-1}.$$

Divide [\[eq:P-lower-asymptotic\]](#eq:P-lower-asymptotic){reference-type="eqref" reference="eq:P-lower-asymptotic"} by [\[eq:F-scale\]](#eq:F-scale){reference-type="eqref" reference="eq:F-scale"}. The remaining clock factor is $\sqrt\sigma\lambda^m=\lambda^{\eta_\sigma-k+m}
=\lambda^{\eta_\sigma-1}$. The second limit uses [\[eq:combined-positive\]](#eq:combined-positive){reference-type="eqref" reference="eq:combined-positive"}.

Thus the unique symbolic scalar balance for RH-347 is $$\label{eq:eta-minus}
 \eta_-=1-\frac{\log(C_*C_M)}{\log\lambda}.$$ This is an interface, not a compensation result: the signed orbit-free remainder in [\[eq:p-lower\]](#eq:p-lower){reference-type="eqref" reference="eq:p-lower"} is still unestimated.

# Executable audit and claim boundary

The artifact reconstructs the lower boundary orbit at $k=3,5,9,17,33$, checks the complete counts and closure, evaluates the missing point, radial sideband, and shifted parity ratios, and verifies an independent rational typed ledger. Finite decimals, including the observed radial sign, are reproduction checks only and are not interval certificates or asymptotic evidence.

RH-346 proves the complete physical lower orbit subledger, exact coefficient decomposition, super-target missing point, sharp radial/full relative law, and shifted parity interface. It proves neither lower compensation nor lower noncompensation. One sideband does not close the punctured off-alias aggregate, and no head transport or direct prefix theorem follows.

RH-347 may audit the scalar mechanism only with the exact combined demand $S_m^-$; RH-345 is not copied with a changed label [@WangCriticalPhase2026]. RH-288 remains inactive. Gates A--E remain false/open. This paper constructs no Hilbert--Polya operator, identifies no Riemann zero, proves no von Mangoldt prime-power trace, proves no completed-zeta divisor equality, and does not prove the Riemann Hypothesis.
