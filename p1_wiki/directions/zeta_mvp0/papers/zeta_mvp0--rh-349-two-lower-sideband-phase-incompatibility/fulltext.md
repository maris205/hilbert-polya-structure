---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-349-two-lower-sideband-phase-incompatibility"
canonical_tex: "zeta_mvp0/papers/RH-349-two-lower-sideband-phase-incompatibility/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-349-two-lower-sideband-phase-incompatibility/main.pdf"
source_sha256: "3dc3341b87ec8c5de3b383b8502523ba4176bfbf791d083aead3fdf747351da3"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Two Lower-Sideband Phase Incompatibility

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-349-two-lower-sideband-phase-incompatibility>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-349-two-lower-sideband-phase-incompatibility/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-349-two-lower-sideband-phase-incompatibility/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-349-two-lower-sideband-phase-incompatibility/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-349-two-lower-sideband-phase-incompatibility/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We isolate the first two orders of the punctured lower-even ladder, $m_j=k-j$ for $j=2,3$. At each order the exact direct coefficient is $$p_j=Y_j+\mathcal P_j-S_j,
   \qquad
   Y_j=\mathcal T_{k,m_j}^{\rm rest}-d_{\sigma,k,2m_j}.$$ For fixed $j$, $$S_j=\frac{2m_j}{C_M}\beta^{2m_j}\{1+o(1)\},\qquad
   \frac{\mathcal P_j}{S_j}\longrightarrow
   \gamma_j(\eta)=C_*C_M\lambda^{\eta-j}.$$ Thus $\gamma_3=\gamma_2/\lambda$. Under the two explicit, presently unproved actual hypotheses $Y_j=o(H_{m_j})$, where $H_m=mR^{-2m}$, put $W_j=|p_j|/(2H_{m_j})$ and $x=(\beta R)^2>1$. If $a=\gamma_2(\eta)>0$, then $$\frac{W_2+W_3}{x^{k-3}}
   \longrightarrow
   \frac{x|a-1|+|a/\lambda-1|}{C_M}.$$ The limit is uniformly positive. In fact, $$\inf_{a>0}\max\{|a-1|,|a/\lambda-1|\}
   =\frac{\lambda-1}{\lambda+1},$$ whereas the sharper physical weighting gives $$\inf_{a>0}\{x|a-1|+|a/\lambda-1|\}=1-\lambda^{-1}.$$ The second minimum occurs at $a=1$. Hence the two-order direct subprefix diverges exponentially conditional on both named remainder hypotheses. Neither hypothesis, unconditional full-prefix nonclosure, growing-depth uniformity, nor any Gate A--E condition is proved. No Riemann-hypothesis conclusion is made.
author:
- Bin Wang
bibliography:
- references.bib
date: August 2026
title: 'Two Lower-Sideband Phase Incompatibility'
```

## Markdown 正文

# The fixed two-sideband ledger

Retain the physical noise clock and phase $$\label{eq:clock}
 k=\frac{\log(1/\sigma)}{2\log\lambda}+O(1),\qquad
 \eta_\sigma=k-\frac{\log(1/\sigma)}{2\log\lambda}
 \longrightarrow\eta.$$ For the two fixed labels $j\in\{2,3\}$, set $$\label{eq:indices}
 m_j=k-j,\qquad n_j=2m_j,\qquad
 H_m=mR^{-2m},\qquad x=(\beta R)^2>1.$$ The orders $2k-4$ and $2k-6$ lie below the two selected orders $2k$ and $2k-2$, so both belong to the punctured lower-even family of RH-348 [@WangLowerLadder2026]. Abbreviate $$\label{eq:shorthand}
 p_j:=p_{\sigma,k,2m_j},\qquad
 \mathcal P_j:=\mathcal P_{\sigma,2m_j}.$$

The simultaneous complete-orbit extraction and the deterministic numerator anchor give the exact identities $$\label{eq:coefficient}
 \boxed{
 p_j=Y_j+\mathcal P_j-S_j,
 \quad
 Y_j=\mathcal T_{k,m_j}^{\rm rest}-d_{\sigma,k,2m_j},
 \quad
 S_j=F_{m_j}^{\rm orb}+\mathcal A_{k,2m_j}.}$$ Here $$\begin{aligned}
 F_m^{\rm orb}&=2mG_m,\qquad
 G_m=\frac{r_H^{-2m}}{1+|M_m|},\label{eq:orbit}\\
 \mathcal A_{k,2m}&=2(\beta^{2m}-\beta_k^{2m}),\qquad
 \beta_k=\frac{|M_k|^{-1/(2k)}}{r_H},
 \qquad \beta=\frac1{r_H\sqrt\lambda}.
 \label{eq:radial}\end{aligned}$$ The $p_j$ are direct coefficients. In particular, the noisy-head/counterloop defect remains inside the actual signed quantity $Y_j$; it is not silently discarded or reclassified as a full-trace term [@WangFirstAlias2026; @WangObservation2026].

[\[prop:fixed-laws\]]{#prop:fixed-laws label="prop:fixed-laws"} For each fixed $j\in\{2,3\}$, $$\begin{aligned}
 S_j&=\frac{2m_j}{C_M}\beta^{2m_j}\{1+o(1)\},
 \label{eq:S-scale}\\
 \frac{S_j}{2H_{m_j}}
 &=\frac{x^{m_j}}{C_M}\{1+o(1)\},
 \label{eq:S-target}\\
 \frac{\mathcal P_j}{S_j}
 &\longrightarrow\gamma_j(\eta)
 :=C_*C_M\lambda^{\eta-j}.
 \label{eq:gamma}\end{aligned}$$ Consequently, $$\label{eq:ratio}
 \boxed{\gamma_3(\eta)=\lambda^{-1}\gamma_2(\eta).}$$

The boundary multiplier law is $M_m=-C_M\lambda^m\{1+o(1)\}$, so $$G_m=C_M^{-1}\beta^{2m}\{1+o(1)\},\qquad
 F_m^{\rm orb}=\frac{2m}{C_M}\beta^{2m}\{1+o(1)\}.$$ Also $$\beta_k=\beta\exp\left[-\frac{\log C_M}{2k}+o(k^{-1})\right].$$ Since $m_j/k\to1$ for fixed $j$, equation [\[eq:radial\]](#eq:radial){reference-type="eqref" reference="eq:radial"} gives $\mathcal A_{k,2m_j}=O(\beta^{2m_j})$. This is $O(m_j^{-1})$ relative to $F_{m_j}^{\rm orb}$, proving [\[eq:S-scale\]](#eq:S-scale){reference-type="eqref" reference="eq:S-scale"}. Division by $2H_{m_j}=2m_jR^{-2m_j}$ proves [\[eq:S-target\]](#eq:S-target){reference-type="eqref" reference="eq:S-target"} [@WangBoundaryMonodromy2026; @WangProjectorMass2026; @WangCompleteLower2026].

For even order $2m$, the exact parity packet is $$\label{eq:parity-exact}
 \mathcal P_{\sigma,2m}
 =r_H^{-2m}\{1-(1-\delta_\sigma)^{2m}\},
 \qquad
 \delta_\sigma=C_*\sqrt\sigma+o(\sqrt\sigma).$$ The uniform quadratic remainder in RH-326 and $m_j\sqrt\sigma\to0$ yield $$\mathcal P_j=2m_jC_*\sqrt\sigma\,r_H^{-2m_j}\{1+o(1)\}.$$ After division by [\[eq:S-scale\]](#eq:S-scale){reference-type="eqref" reference="eq:S-scale"}, the remaining clock factor is $$\sqrt\sigma\lambda^{m_j}
 =\lambda^{\eta_\sigma-k+m_j}
 =\lambda^{\eta_\sigma-j}.$$ This proves [\[eq:gamma\]](#eq:gamma){reference-type="eqref" reference="eq:gamma"}; [\[eq:ratio\]](#eq:ratio){reference-type="eqref" reference="eq:ratio"} is immediate [@WangParityBoundary2026; @WangFirstAlias2026].

Every limit in [\[prop:fixed-laws\]](#prop:fixed-laws){reference-type="ref" reference="prop:fixed-laws"} is pointwise in the fixed label $j$. No uniformity for a depth $j=j_k\to\infty$ is asserted.

# Two exact phase minimax laws

Write $$\label{eq:a}
 a=\gamma_2(\eta)=C_*C_M\lambda^{\eta-2}>0.$$ Then $\gamma_3=a/\lambda$. The first minimax law measures the larger relative mismatch at the two coordinates.

[\[prop:relative-minimax\]]{#prop:relative-minimax label="prop:relative-minimax"} For every $\lambda>1$, $$\label{eq:relative-minimax}
 \boxed{
 \inf_{a>0}\max\{|a-1|,|a/\lambda-1|\}
 =\frac{\lambda-1}{\lambda+1}.}$$ The unique minimizer is $a_{\rm rel}=2\lambda/(\lambda+1)$.

For $0<a\le1$, the larger term is $1-a/\lambda$, which decreases to $1-1/\lambda$. For $1\le a\le\lambda$, the terms are respectively $a-1$ and $1-a/\lambda$. Their maximum is minimized at their unique intersection, $$a-1=1-a/\lambda,\qquad
 a=\frac{2\lambda}{\lambda+1},$$ where both equal $(\lambda-1)/(\lambda+1)$. For $a\ge\lambda$, the maximum is $a-1$ and increases. The intersection value is strictly smaller than the boundary values, proving the claim.

The prefix normalization does not weight these coordinates equally: $x^{m_2}/x^{k-3}=x$, whereas $x^{m_3}/x^{k-3}=1$.

[\[prop:weighted-minimax\]]{#prop:weighted-minimax label="prop:weighted-minimax"} If $\lambda>1$ and $x>1$, then $$\label{eq:weighted-minimax}
 \boxed{
 \inf_{a>0}\{x|a-1|+|a/\lambda-1|\}
 =1-\lambda^{-1}.}$$ The unique minimizer is $a_{\rm wt}=1$.

For $0<a\le1$, the objective is $$x+1-a(x+\lambda^{-1}),$$ which is strictly decreasing. For $1\le a\le\lambda$, it is $$x(a-1)+1-a/\lambda,$$ whose slope $x-\lambda^{-1}$ is positive. For $a\ge\lambda$, it is $x(a-1)+a/\lambda-1$, again strictly increasing. Hence the unique global minimum occurs at $a=1$ and equals $1-\lambda^{-1}$.

The two optimizers differ. Equalizing the relative mismatches is not the same operation as minimizing the actual prefix-weighted sum.

# Conditional physical two-order obstruction

Define the two actual weighted direct contributions $$\label{eq:W}
 W_j=\frac{|p_j|}{2H_{m_j}}
 =\frac{|p_j|R^{2m_j}}{2m_j},\qquad j=2,3.$$

[\[thm:conditional\]]{#thm:conditional label="thm:conditional"} Suppose an actual physical sequence satisfies [\[eq:clock\]](#eq:clock){reference-type="eqref" reference="eq:clock"} and, simultaneously, $$\label{eq:Y-hypotheses}
 \boxed{
 Y_2=o(H_{m_2}),\qquad Y_3=o(H_{m_3}).}$$ Then for each $j=2,3$, $$\label{eq:coordinate-limit}
 \frac{W_j}{x^{m_j}}
 \longrightarrow\frac{|\gamma_j(\eta)-1|}{C_M}.$$ Consequently, with $a$ as in [\[eq:a\]](#eq:a){reference-type="eqref" reference="eq:a"}, $$\label{eq:sum-limit}
 \boxed{
 \frac{W_2+W_3}{x^{k-3}}
 \longrightarrow
 \frac{x|a-1|+|a/\lambda-1|}{C_M}
 \ge\frac{1-\lambda^{-1}}{C_M}>0.}$$ In particular, $W_2+W_3$ diverges exponentially.

Equation [\[eq:S-target\]](#eq:S-target){reference-type="eqref" reference="eq:S-target"} and $x>1$ imply $H_{m_j}/S_j\to0$. Therefore each hypothesis in [\[eq:Y-hypotheses\]](#eq:Y-hypotheses){reference-type="eqref" reference="eq:Y-hypotheses"} gives $Y_j/S_j\to0$. Divide [\[eq:coefficient\]](#eq:coefficient){reference-type="eqref" reference="eq:coefficient"} by $S_j$ and apply [\[eq:gamma\]](#eq:gamma){reference-type="eqref" reference="eq:gamma"}: $$\frac{p_j}{S_j}\longrightarrow\gamma_j(\eta)-1.$$ Multiplication by [\[eq:S-target\]](#eq:S-target){reference-type="eqref" reference="eq:S-target"} proves [\[eq:coordinate-limit\]](#eq:coordinate-limit){reference-type="eqref" reference="eq:coordinate-limit"}, including the case in which the limiting mismatch is zero. Since $m_2=k-2$, $m_3=k-3$, and $\gamma_3=a/\lambda$, $$\frac{W_2+W_3}{x^{k-3}}
 =x\frac{W_2}{x^{m_2}}+\frac{W_3}{x^{m_3}}.$$ Taking limits and applying [\[prop:weighted-minimax\]](#prop:weighted-minimax){reference-type="ref" reference="prop:weighted-minimax"} proves [\[eq:sum-limit\]](#eq:sum-limit){reference-type="eqref" reference="eq:sum-limit"}.

[\[cor:bounded-phase\]]{#cor:bounded-phase label="cor:bounded-phase"} Suppose only that $\eta_\sigma$ remains in a fixed bounded interval, and assume the same two simultaneous actual remainder hypotheses [\[eq:Y-hypotheses\]](#eq:Y-hypotheses){reference-type="eqref" reference="eq:Y-hypotheses"}. Then $$\label{eq:liminf}
 \boxed{
 \liminf_{\sigma\to0}
 \frac{W_2+W_3}{x^{k-3}}
 \ge \frac{1-\lambda^{-1}}{C_M}>0.}$$

On a bounded phase interval, the quadratic parity remainder used in [\[prop:fixed-laws\]](#prop:fixed-laws){reference-type="ref" reference="prop:fixed-laws"} is uniform for each of the two fixed labels. Put $a_\sigma=C_*C_M\lambda^{\eta_\sigma-2}$. The proof of [\[thm:conditional\]](#thm:conditional){reference-type="ref" reference="thm:conditional"}, without taking a phase limit, gives $$\frac{W_2+W_3}{x^{k-3}}
 =\frac{x|a_\sigma-1|+|a_\sigma/\lambda-1|}{C_M}+o(1).$$ Apply [\[prop:weighted-minimax\]](#prop:weighted-minimax){reference-type="ref" reference="prop:weighted-minimax"} pointwise in $a_\sigma$ and take the lower limit.

The quantities $Y_j$ contain the actual signed orbit-free trace remainder and noisy-head/counterloop defect at their respective moving orders. The repository proves neither estimate in [\[eq:Y-hypotheses\]](#eq:Y-hypotheses){reference-type="eqref" reference="eq:Y-hypotheses"}. Thus [\[thm:conditional\]](#thm:conditional){reference-type="ref" reference="thm:conditional"} is a conditional theorem about two actual direct coefficients, not an unconditional physical nonclosure result. It does not provide an unconditional verdict for the full $\mathcal E_{\rm off}$ aggregate.

# Executable audit and route boundary

The artifact reconstructs the two boundary multipliers, complete orbit atoms, radial terms, demands, and exact parity-formula evaluations under the leading-law scalar fixture at $k=10,18,30,46$. It chooses the physically weighted optimizer $a=1$, uses $Y_2=Y_3=0$, and verifies the approach of $$C_M\frac{W_2+W_3}{x^{k-3}}
 \quad\hbox{to}\quad 1-\lambda^{-1}.$$ It also checks both exact minimax formulas and their distinct optimizers. These decimal rows reproduce formulas only. They are not interval certificates, asymptotic evidence, measurements of a noisy operator, or evidence for [\[eq:Y-hypotheses\]](#eq:Y-hypotheses){reference-type="eqref" reference="eq:Y-hypotheses"}.

RH-350 may audit a fixed-depth extension $j=2,\ldots,J$ and, separately, ask whether any slowly growing $J=J_k$ is supported. The latter requires new uniform control of the parity Taylor remainder, multiplier law, radial term, ratio $m_j/k$, and simultaneous actual remainder hypotheses. None is inferred from this fixed two-order theorem.

Odd orders, upper off-alias orders, actual signed remainder control, and unconditional full-direct-prefix behavior remain open, as do determinant gluing and RH-288. Gates A--E remain false/open. This paper constructs no Hilbert--Polya operator, identifies no Riemann zero, proves no von Mangoldt prime-power trace, proves no completed-zeta divisor equality, and does not prove the Riemann Hypothesis.
