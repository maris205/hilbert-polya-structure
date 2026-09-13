---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-353-critical-first-lower-actual-signed-completion-gap"
canonical_tex: "zeta_mvp0/papers/RH-353-critical-first-lower-actual-signed-completion-gap/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-353-critical-first-lower-actual-signed-completion-gap/main.pdf"
source_sha256: "d3c3badab1016ed42305f3620734d29189ee5ab0cc006d6d25e0ac53d91637b8"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Phase-Free Critical--First-Lower Actual Signed-Completion Gap

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-353-critical-first-lower-actual-signed-completion-gap>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-353-critical-first-lower-actual-signed-completion-gap/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-353-critical-first-lower-actual-signed-completion-gap/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-353-critical-first-lower-actual-signed-completion-gap/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-353-critical-first-lower-actual-signed-completion-gap/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-352 proves actual natural-scale cancellation on the growing lower-even ladder but excludes the critical order $2k$ and first lower sideband $2k-2$. We close those two normalized signed-completion coordinates on the same physical clock. Put $m=k-1$, $H_\ell=\ell R^{-2\ell}$, and $x=(\beta R)^2$. The source-locked direct coefficients are $$p_k^0=Y_k^0+\mathcal P_k^0-S_k^0,
   \qquad p_k^-=Y_k^-+\mathcal P_k^--S_k^-.$$ The actual modulus-complement cap and deterministic all-order envelope give $$\limsup_{k\to\infty}
   \left(
   \max\left\{
   \frac{|p_k^0|}{2H_kx^k},
   \frac{|p_k^-|}{2H_mx^m}
   \right\}\right)^{1/k}
   \le\max\left\{\frac{r_H^2\lambda^3}{4},\frac1\lambda\right\}<1.$$ Writing $\gamma_k=C_*C_M\lambda^{\eta_k}$, the critical and first-lower source laws then force the actual normalized remainders $$Z_k^0:=\frac{C_MY_k^0}{2H_kx^k}=2-\gamma_k+o(1),
   \qquad
   Z_k^-:=\frac{C_MY_k^-}{2H_mx^m}
   =1-\frac{\gamma_k}{\lambda}+o(1).$$ The physical phase cancels exactly across the two orders: $$Z_k^0-\lambda Z_k^-\longrightarrow2-\lambda>\frac3{10}.$$ Consequently $$\liminf_{k\to\infty}\max\{|Z_k^0|,|Z_k^-|\}
   \ge\frac{2-\lambda}{1+\lambda}>\frac19.$$ Thus the two-coordinate maximum of the actual boundary remainders supplies an exponentially large unnormalized weighted contribution; the maximizing order may depend on $k$. This is signed cancellation supply, not direct-prefix divergence: $p_k^0=o(H_k)$ and $p_k^-=o(H_m)$ remain open. Odd and upper-alias orders, full $E_{\rm off}$, RH-288, Gates A--E, and all Riemann-hypothesis claims remain open.
author:
- Bin Wang
bibliography:
- references.bib
date: August 2026
title: |
  A Phase-Free Critical--First-Lower\
  Actual Signed-Completion Gap
```

## Markdown 正文

# One clock and two excluded boundary orders

Use the physical natural clock and bounded phase $$\label{eq:clock}
 k=\frac{\log(1/\sigma)}{2\log\lambda}+O(1),
 \qquad
 \eta_k=k-\frac{\log(1/\sigma)}{2\log\lambda},
 \qquad \sup_k|\eta_k|<\infty.$$ Fix $$\label{eq:constants}
 r_H=\frac{17}{20},\qquad q=\frac12,\qquad R=\frac75,
 \qquad \frac{28}{17}<\lambda<\frac{17}{10},$$ and put $$\label{eq:scales}
 \beta=\frac1{r_H\sqrt\lambda},\qquad
 q_*=\frac1{r_H\lambda},\qquad
 x=(\beta R)^2>1,
 \qquad H_\ell=\ell R^{-2\ell}.$$ The strict multiplier bracket is source-certified in RH-262 and RH-336 [@WangBoundaryBudget2026; @WangProjectorMass2026].

Set $$\label{eq:m}
 m=k-1.$$ This is one noise sequence. The symbol $m$ is only the period parameter of the first-lower boundary orbit.

At the critical order, RH-344 and RH-345 give the exact direct coefficient $$\label{eq:critical}
 p_k^0:=p_{\sigma,k,2k}
 =Y_k^0+\mathcal P_k^0-S_k^0,
 \quad
 Y_k^0=\mathcal T_k^{\rm rest}-d_{\sigma,k,2k},
 \quad
 S_k^0=\mathcal A_{k,2k}+F_k^{\rm orb}.$$ Their deterministic and parity laws are $$\begin{aligned}
 S_k^0&=\frac{4k}{C_M}\beta^{2k}\{1+o(1)\},
 \label{eq:critical-S}\\
 \frac{\mathcal P_k^0}{\mathcal A_{k,2k}}
 &=C_*C_M\lambda^{\eta_k}\{1+o(1)\},
 \qquad
 \mathcal A_{k,2k}=\frac{2k}{C_M}\beta^{2k}\{1+o(1)\}.
 \label{eq:critical-P}\end{aligned}$$ At the first lower sideband, RH-346 and RH-347 give $$\label{eq:lower}
 p_k^-:=p_{\sigma,k,2m}
 =Y_k^-+\mathcal P_k^--S_k^-,
 \quad
 Y_k^-=\mathcal T_{k,m}^{\rm rest}-d_{\sigma,k,2m},
 \quad
 S_k^-=F_m^{\rm orb}+\mathcal A_{k,2m},$$ with $$\begin{aligned}
 S_k^-&=\frac{2m}{C_M}\beta^{2m}\{1+o(1)\},
 \label{eq:lower-S}\\
 \frac{\mathcal P_k^-}{S_k^-}
 &=C_*C_M\lambda^{\eta_k-1}\{1+o(1)\}.
 \label{eq:lower-P}\end{aligned}$$ All four quantities $Y_k^0,Y_k^-,p_k^0,p_k^-$ are actual signed coefficients or remainders in one physical data type. They are not scalar completions or synthetic operators [@WangCompleteCritical2026; @WangCriticalBalance2026; @WangCompleteLower2026; @WangLowerBalance2026].

# The actual two-order direct cap

The direct coefficient has the source-locked representation $$\label{eq:tau-a}
 p_{\sigma,k,n}=\tau_{\sigma,n}-a_n.$$ RH-282 and RH-267 prove, for all $n\ge2$, $$\label{eq:source-caps}
 |\tau_{\sigma,n}|\le\sigma^{-1}q^{n-2},
 \qquad |a_n|<48q_*^n.$$ These are actual modulus-complement and deterministic-target bounds, respectively; RH-288 and RH-340 identify their difference as the direct coefficient in [\[eq:tau-a\]](#eq:tau-a){reference-type="eqref" reference="eq:tau-a"} [@WangSpectralTail2026; @WangUnifiedEnvelope2026; @WangGluing2026; @WangSynchronization2026; @WangModulusCancellation2026].

Define $$\label{eq:V}
 V_k=\max\left\{
 \frac{|p_k^0|}{2H_kx^k},
 \frac{|p_k^-|}{2H_mx^m}
 \right\},
 \qquad
 \rho_N=\frac{r_H^2\lambda^3}{4},
 \quad \rho_T=\frac1\lambda.$$

[\[thm:cap\]]{#thm:cap label="thm:cap"} One has $$\label{eq:V-rate}
 \boxed{
 \limsup_{k\to\infty}V_k^{1/k}
 \le\max\{\rho_N,\rho_T\}<1.}$$ More precisely, $$\label{eq:rate-certificates}
 \rho_N<\frac{1419857}{1600000}<1,
 \qquad \rho_T<\frac{17}{28}<1.$$

For $\ell=k$ or $\ell=m=k-1$, the identities $2H_\ell x^\ell=2\ell\beta^{2\ell}$ and $\sigma^{-1}=\lambda^{2(k-\eta_k)}$ give $$\begin{aligned}
 \frac{|\tau_{\sigma,2\ell}|}{2H_\ell x^\ell}
 &\le \frac{2}{\ell}\sigma^{-1}
 (q^2r_H^2\lambda)^\ell,
 \label{eq:noisy-bound}\\
 \frac{|a_{2\ell}|}{2H_\ell x^\ell}
 &<\frac{24}{\ell}\lambda^{-\ell}.
 \label{eq:target-bound}\end{aligned}$$ For $\ell=k$, their $k$th-root ceilings are $\rho_N$ and $\rho_T$. Replacing $k$ by $k-1$ changes only fixed factors and has the same root ceilings. The triangle inequality in [\[eq:tau-a\]](#eq:tau-a){reference-type="eqref" reference="eq:tau-a"} proves [\[eq:V-rate\]](#eq:V-rate){reference-type="eqref" reference="eq:V-rate"}. The strict rational bounds follow from [\[eq:constants\]](#eq:constants){reference-type="eqref" reference="eq:constants"}, exactly as in RH-352.

The theorem is normalized at the leading boundary-demand scale. It does not imply $p_k^0=o(H_k)$ or $p_k^-=o(H_m)$ after the factors $x^k$ and $x^m$ are removed.

# Actual completion laws and phase elimination

Put $$\label{eq:gamma}
 \gamma_k=C_*C_M\lambda^{\eta_k}.$$ Bounded phase makes $\gamma_k$ bounded above and away from zero. Define the actual normalized signed remainders $$\label{eq:Z}
 Z_k^0=\frac{C_MY_k^0}{2H_kx^k},
 \qquad
 Z_k^-=\frac{C_MY_k^-}{2H_mx^m}.$$

[\[thm:completion\]]{#thm:completion label="thm:completion"} On every bounded-phase physical clock, $$\begin{aligned}
 \boxed{Z_k^0=2-\gamma_k+o(1),}
 \label{eq:critical-Z}\\
 \boxed{Z_k^-=1-\frac{\gamma_k}{\lambda}+o(1).}
 \label{eq:lower-Z}\end{aligned}$$

Since $2H_kx^k=2k\beta^{2k}$, [\[eq:critical-S\]](#eq:critical-S){reference-type="eqref" reference="eq:critical-S"} gives $$\frac{C_MS_k^0}{2H_kx^k}\longrightarrow2.$$ Equations [\[eq:critical-P\]](#eq:critical-P){reference-type="eqref" reference="eq:critical-P"} and boundedness of $\gamma_k$ give $$\frac{C_M\mathcal P_k^0}{2H_kx^k}=\gamma_k+o(1).$$ Solve [\[eq:critical\]](#eq:critical){reference-type="eqref" reference="eq:critical"} for $Y_k^0$ and use [\[thm:cap\]](#thm:cap){reference-type="ref" reference="thm:cap"} to obtain [\[eq:critical-Z\]](#eq:critical-Z){reference-type="eqref" reference="eq:critical-Z"}.

Likewise $2H_mx^m=2m\beta^{2m}$, so [\[eq:lower-S\]](#eq:lower-S){reference-type="eqref" reference="eq:lower-S"}--[\[eq:lower-P\]](#eq:lower-P){reference-type="eqref" reference="eq:lower-P"} imply $$\frac{C_MS_k^-}{2H_mx^m}\longrightarrow1,
 \qquad
 \frac{C_M\mathcal P_k^-}{2H_mx^m}
 =\frac{\gamma_k}{\lambda}+o(1).$$ Solving [\[eq:lower\]](#eq:lower){reference-type="eqref" reference="eq:lower"} and applying [\[thm:cap\]](#thm:cap){reference-type="ref" reference="thm:cap"} proves [\[eq:lower-Z\]](#eq:lower-Z){reference-type="eqref" reference="eq:lower-Z"}.

The two leading completion laws contain the same physical phase scalar. Their difference eliminates it.

[\[thm:gap\]]{#thm:gap label="thm:gap"} The actual remainder pair satisfies $$\label{eq:affine-gap}
 \boxed{
 Z_k^0-\lambda Z_k^-\longrightarrow2-\lambda>\frac3{10}.}$$ Consequently $$\label{eq:minimax-gap}
 \boxed{
 \liminf_{k\to\infty}\max\{|Z_k^0|,|Z_k^-|\}
 \ge\frac{2-\lambda}{1+\lambda}>\frac19.}$$ The constant is sharp for the leading affine family: equality in the minimax problem is attained at $$\label{eq:optimizer}
 \gamma_*=\frac{3\lambda}{1+\lambda},
 \qquad
 2-\gamma_*=\frac{2-\lambda}{1+\lambda},
 \qquad
 1-\frac{\gamma_*}{\lambda}
 =-\frac{2-\lambda}{1+\lambda}.$$

Subtract $\lambda$ times [\[eq:lower-Z\]](#eq:lower-Z){reference-type="eqref" reference="eq:lower-Z"} from [\[eq:critical-Z\]](#eq:critical-Z){reference-type="eqref" reference="eq:critical-Z"}; the two occurrences of $\gamma_k$ cancel. The upper multiplier bound gives $2-\lambda>3/10$.

For arbitrary real $u,v$, $$|u-\lambda v|\le |u|+\lambda|v|
 \le(1+\lambda)\max\{|u|,|v|\}.$$ Apply this to $u=Z_k^0$, $v=Z_k^-$ and pass to the lower limit. Since $\lambda<17/10$ and $t\mapsto(2-t)/(1+t)$ is decreasing, $$\frac{2-\lambda}{1+\lambda}>
 \frac{2-17/10}{1+17/10}=\frac19.$$ Direct substitution verifies [\[eq:optimizer\]](#eq:optimizer){reference-type="eqref" reference="eq:optimizer"}, so the leading minimax constant is sharp.

[\[cor:supply\]]{#cor:supply label="cor:supply"} The maximum of the two actual remainder contributions is exponentially large; the maximizing coordinate may vary with $k$. More precisely, $$\label{eq:supply}
 \liminf_{k\to\infty}
 \frac{C_M}{x^{k-1}}
 \max\left\{
 \frac{|Y_k^0|}{2H_k},
 \frac{|Y_k^-|}{2H_m}
 \right\}
 \ge\frac{2-\lambda}{1+\lambda}>\frac19.$$

The two unnormalized quantities are respectively $x^k|Z_k^0|/C_M$ and $x^{k-1}|Z_k^-|/C_M$. Since $x>1$, their maximum is at least $x^{k-1}\max\{|Z_k^0|,|Z_k^-|\}/C_M$. Apply [\[eq:minimax-gap\]](#eq:minimax-gap){reference-type="eqref" reference="eq:minimax-gap"}.

This divergence belongs to the actual signed remainders $Y$, not to the direct coefficients $p$. It is the leading supply that cancels the deterministic/parity packets in [\[eq:critical\]](#eq:critical){reference-type="eqref" reference="eq:critical"} and [\[eq:lower\]](#eq:lower){reference-type="eqref" reference="eq:lower"}.

# Executable protocol and claim boundary

The artifact checks the exact affine identity $(2-\gamma)-\lambda(1-\gamma/\lambda)=2-\lambda$, the exact minimax optimizer, the global rational bounds $2-\lambda>3/10$ and $(2-\lambda)/(1+\lambda)>1/9$, and the two natural-scale rate certificates. Its finite rows use the in-range rational fixture $\lambda=5/3$. They reproduce formulas only; they are not observations of $p$, $Y$, or the noisy operator and are not asymptotic evidence.

RH-353 proves actual leading natural-scale completion at the critical and first-lower orders and a phase-free cross-order remainder gap. It does not prove $p_k^0=o(H_k)$ or $p_k^-=o(H_m)$, control odd or upper-alias orders, decide the full $E_{\rm off}$ aggregate, prove head transport, or close the RH-241 moving noisy all-order envelope and coefficient bridge. RH-288 is inactive. Gates A--E remain false/open. This paper constructs no Hilbert--Polya operator, identifies no Riemann zero, proves no von Mangoldt-weighted prime-power trace, proves no completed-zeta divisor equality, and does not prove the Riemann Hypothesis.
