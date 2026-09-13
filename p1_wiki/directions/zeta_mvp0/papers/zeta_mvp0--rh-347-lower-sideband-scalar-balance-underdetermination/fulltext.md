---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-347-lower-sideband-scalar-balance-underdetermination"
canonical_tex: "zeta_mvp0/papers/RH-347-lower-sideband-scalar-balance-underdetermination/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-347-lower-sideband-scalar-balance-underdetermination/main.pdf"
source_sha256: "1b46e0cea7473a2bf70af9c4b67f702413edb97d3387ea5c20978151fd0065be"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Lower-Sideband Scalar Balance and Target-Scale Underdetermination

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-347-lower-sideband-scalar-balance-underdetermination>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-347-lower-sideband-scalar-balance-underdetermination/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-347-lower-sideband-scalar-balance-underdetermination/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-347-lower-sideband-scalar-balance-underdetermination/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-347-lower-sideband-scalar-balance-underdetermination/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  At the mandatory lower sideband $2m=2k-2$, RH-346 gives the exact physical coefficient $$p_{\sigma,k,2m}=Y_m^-+\mathcal P_{\sigma,2m}-S_m^-,
   \qquad
   Y_m^-=\mathcal T_{k,m}^{\rm rest}-d_{\sigma,k,2m},
   \qquad
   S_m^-=F_m^{\rm orb}+\mathcal A_{k,2m}.$$ Here $m=k-1$ is an orbit-period parameter on the same $(\sigma,k)$ noise clock, $F_m^{\rm orb}=2mG_m$, and $$\frac{S_m^-}{F_m^{\rm orb}}\longrightarrow1,\qquad
   \frac{G_m}{H_m}
   =\frac{(\beta R)^{2m}}{C_Mm}\{1+o(1)\}\longrightarrow\infty.$$ The inherited parity interface is $\mathcal P_{\sigma,2m}/S_m^-\to C_*C_M\lambda^{\eta-1}$. Thus, if the actual signed remainder satisfies $Y_m^-=o(H_m)$, every fixed phase other than $$\eta_-=1-\frac{\log(C_*C_M)}{\log\lambda}$$ has a divergent weighted lower contribution, with exact leading coefficient $|C_*C_M\lambda^{\eta-1}-1|/C_M$.

  At the balance phase we construct two exact scalar parity envelopes using the order-$2m$ inverse parity map. The choices $\mathcal P_m^{\rm close}=S_m^-$ and $\mathcal P_m^{\rm far}=S_m^-+F_m^{\rm orb}/m$ both lie in the legal domain eventually and satisfy the same square-root law on the same clock with $k=m+1$. In the scalar information class with $Y_m^-=0$, they give zero residual versus $F_m^{\rm orb}/m=2G_m$, whose weighted value is exactly $G_m/H_m\to\infty$. These scalar sequences are not noisy operators. Actual lower compensation, the remaining off-alias aggregate, determinant gluing, and Gates A--E remain open. No Riemann-hypothesis conclusion follows.
author:
- Bin Wang
bibliography:
- references.bib
date: August 2026
title: |
  Lower-Sideband Scalar Balance and\
  Target-Scale Underdetermination
```

## Markdown 正文

# Exact lower-sideband scalar ledger

Use the physical clock and target $$\label{eq:clock}
 k=\frac{\log(1/\sigma)}{2\log\lambda}+O(1),\qquad
 \eta_\sigma=k-\frac{\log(1/\sigma)}{2\log\lambda},\qquad
 m=k-1,\qquad H_m=mR^{-2m},$$ where $R=7/5$. The replacement $m=k-1$ does not define a second noise sequence. It only identifies the period parameter of the lower boundary orbit.

RH-346 completes that orbit extraction and proves the exact direct identity $$\label{eq:lower}
 \boxed{
 p_{\sigma,k,2m}=Y_m^-+\mathcal P_{\sigma,2m}-S_m^-,
 \quad
 Y_m^-=\mathcal T_{k,m}^{\rm rest}-d_{\sigma,k,2m},
 \quad
 S_m^-=F_m^{\rm orb}+\mathcal A_{k,2m}.}$$ The two deterministic constituents are $$\begin{aligned}
 F_m^{\rm orb}&=2mG_m,\qquad
 G_m=\frac{r_H^{-2m}}{1+|M_m|},\label{eq:full-atom}\\
 \mathcal A_{k,2m}&=2(\beta^{2m}-\beta_k^{2m}),\qquad
 \beta_k=\frac{|M_k|^{-1/(2k)}}{r_H},\qquad
 \beta=\frac1{r_H\sqrt\lambda}.\label{eq:radial}\end{aligned}$$ The radial sideband need not have a source-locked sign. What is proved is the relative law $$\label{eq:relative}
 \frac{\mathcal A_{k,2m}}{F_m^{\rm orb}}
 =\frac{C_M-1}{m}+o(m^{-1})\longrightarrow0.$$ Consequently $S_m^->0$ eventually and $$\begin{aligned}
 S_m^-&=\frac{2m}{C_M}\beta^{2m}\{1+o(1)\},
 \label{eq:S-scale}\\
 \frac{S_m^-}{H_m}
 &=\frac2{C_M}(\beta R)^{2m}\{1+o(1)\}
 \longrightarrow\infty,\label{eq:S-over-H}\\
 \frac{G_m}{H_m}
 &=\frac1{C_Mm}(\beta R)^{2m}\{1+o(1)\}
 \longrightarrow\infty.\label{eq:G-over-H}\end{aligned}$$ The strict inequality $\beta R>1$ is already certified in the source chain [@WangProjectorMass2026; @WangCompleteLower2026].

The actual even parity packet is $$\label{eq:parity}
 \mathcal P_{\sigma,2m}
 =r_H^{-2m}\{1-(1-\delta_\sigma)^{2m}\},
 \qquad
 \delta_\sigma=C_*\sqrt\sigma+o(\sqrt\sigma),\quad C_*>0.$$ On bounded physical phase, RH-346 proves $$\label{eq:phase-law}
 \frac{\mathcal P_{\sigma,2m}}{S_m^-}
 =C_*C_M\lambda^{\eta_\sigma-1}\{1+o(1)\}.$$ The factor $\lambda^{-1}$ is forced by keeping $k=m+1$ in [\[eq:clock\]](#eq:clock){reference-type="eqref" reference="eq:clock"}; it is not a change of normalization [@WangParityBoundary2026; @WangFirstAlias2026].

# Conditional obstruction away from scalar balance

Put $$\label{eq:gamma}
 \gamma_-(\eta)=C_*C_M\lambda^{\eta-1}.$$ Since $C_*,C_M>0$ and $\lambda>1$, this function is strictly increasing. Its unique leading balance phase is $$\label{eq:eta-minus}
 \boxed{\eta_-=1-\frac{\log(C_*C_M)}{\log\lambda}},
 \qquad \gamma_-(\eta_-)=1.$$ This symbolic interface is inherited from RH-346; it is not the new theorem of the present paper.

[\[thm:off-balance\]]{#thm:off-balance label="thm:off-balance"} Consider an actual physical sequence on [\[eq:clock\]](#eq:clock){reference-type="eqref" reference="eq:clock"} with $\eta_\sigma\to\eta$. If $$\label{eq:Y-small}
 Y_m^-=o(H_m)$$ and $\eta\ne\eta_-$, then $$\label{eq:exact-rate}
 \boxed{
 \frac{|p_{\sigma,k,2m}|}{2H_m}
 =\frac{|C_*C_M\lambda^{\eta-1}-1|}{C_M}
  (\beta R)^{2m}\{1+o(1)\}
 \longrightarrow\infty.}$$ Equivalently, the single weighted prefix contribution $|p_{\sigma,k,2m}|R^{2m}/(2m)$ diverges.

By [\[eq:S-over-H\]](#eq:S-over-H){reference-type="eqref" reference="eq:S-over-H"}, hypothesis [\[eq:Y-small\]](#eq:Y-small){reference-type="eqref" reference="eq:Y-small"} gives $Y_m^-/S_m^-\to0$. Divide [\[eq:lower\]](#eq:lower){reference-type="eqref" reference="eq:lower"} by $S_m^-$ and use [\[eq:phase-law\]](#eq:phase-law){reference-type="eqref" reference="eq:phase-law"}: $$\frac{p_{\sigma,k,2m}}{S_m^-}
 \longrightarrow \gamma_-(\eta)-1\ne0.$$ Moreover [\[eq:S-scale\]](#eq:S-scale){reference-type="eqref" reference="eq:S-scale"} gives $$\frac{S_m^-}{2H_m}
 =\frac1{C_M}(\beta R)^{2m}\{1+o(1)\}.$$ Multiplication proves [\[eq:exact-rate\]](#eq:exact-rate){reference-type="eqref" reference="eq:exact-rate"}. The weighted identity follows from $H_m=mR^{-2m}$.

The remainder $Y_m^-$ contains the actual signed orbit-free raw contribution and the actual head defect. No repository theorem proves [\[eq:Y-small\]](#eq:Y-small){reference-type="eqref" reference="eq:Y-small"}. Therefore [\[thm:off-balance\]](#thm:off-balance){reference-type="ref" reference="thm:off-balance"} excludes parity as an isolated scalar compensation mechanism under a named physical hypothesis; it does not prove actual lower-sideband or aggregate prefix nonclosure.

# Balance requires exponentially sharper information

At $\eta=\eta_-$, the source law [\[eq:phase-law\]](#eq:phase-law){reference-type="eqref" reference="eq:phase-law"} has leading ratio one, but target closure requires more than a relative $o(1)$ estimate.

[\[prop:precision\]]{#prop:precision label="prop:precision"} Under [\[eq:Y-small\]](#eq:Y-small){reference-type="eqref" reference="eq:Y-small"}, lower-sideband closure is equivalent to $$\label{eq:target-match}
 \mathcal P_{\sigma,2m}=S_m^-+o(H_m).$$ Relative to the positive demand, the required precision is $$\label{eq:relative-precision}
 o\!\left(\frac{H_m}{S_m^-}\right)
 =o\!\left((\beta R)^{-2m}\right).$$ The inherited relative $o(1)$ in [\[eq:phase-law\]](#eq:phase-law){reference-type="eqref" reference="eq:phase-law"} does not decide [\[eq:target-match\]](#eq:target-match){reference-type="eqref" reference="eq:target-match"}.

Rearrange [\[eq:lower\]](#eq:lower){reference-type="eqref" reference="eq:lower"} and use [\[eq:Y-small\]](#eq:Y-small){reference-type="eqref" reference="eq:Y-small"}. Formula [\[eq:S-over-H\]](#eq:S-over-H){reference-type="eqref" reference="eq:S-over-H"} gives [\[eq:relative-precision\]](#eq:relative-precision){reference-type="eqref" reference="eq:relative-precision"}. An unspecified vanishing relative error need not be exponentially small.

Ordinary substitution of archived decimal constants gives $\eta_-=4.0609149137\ldots$. Those decimals are reproduction inputs, not directed interval enclosures. In particular, this numerical value cannot be used as a rigorous theorem excluding the balance phase from the usual canonical clock window. The analytic argument below therefore treats the symbolic balance phase directly.

# Exact scalar underdetermination at balance

Freeze the same physical clock at the symbolic balance: $$\label{eq:balance-clock}
 k=m+1,\qquad
 \sigma_m=\lambda^{-2(k-\eta_-)}.$$ Using [\[eq:eta-minus\]](#eq:eta-minus){reference-type="eqref" reference="eq:eta-minus"}, $$\label{eq:expected-delta}
 C_*\sqrt{\sigma_m}
 =\frac1{C_M}\lambda^{-m}.$$ For a desired scalar packet $0<X_m<r_H^{-2m}$, define the exact inverse parity map $$\label{eq:inverse}
 \delta_m(X)
 =1-\{1-r_H^{2m}X_m\}^{1/(2m)},\qquad
 \lambda_{-,m}(X)=-(1-\delta_m(X)).$$ Then $\lambda_{-,m}(X)\in(-1,0)$ and substitution in [\[eq:parity\]](#eq:parity){reference-type="eqref" reference="eq:parity"} recovers $X_m$ exactly.

[\[thm:completions\]]{#thm:completions label="thm:completions"} For all sufficiently large $m$, let $$\label{eq:two-packets}
 X_m^{\rm close}=S_m^-,
 \qquad
 X_m^{\rm far}=S_m^-+\frac{F_m^{\rm orb}}m.$$ Both packets satisfy the legal domain $$\label{eq:domain}
 0<r_H^{2m}X_m^{\rm close}<1,\qquad
 0<r_H^{2m}X_m^{\rm far}<1,$$ and their inverse images obey the same leading physical law $$\label{eq:common-law}
 \delta_m(X^{\rm close})
 =C_*\sqrt{\sigma_m}\{1+o(1)\},\qquad
 \delta_m(X^{\rm far})
 =C_*\sqrt{\sigma_m}\{1+o(1)\}.$$ In the scalar information class with $Y_m^-=0$, the close sequence has $p_{\sigma,k,2m}=0$, whereas the far sequence has $$\label{eq:far-residual}
 p_{\sigma,k,2m}=\frac{F_m^{\rm orb}}m=2G_m$$ and the exact weighted identity $$\label{eq:far-weighted}
 \frac{|p_{\sigma,k,2m}|}{2H_m}
 =\frac{G_m}{H_m}
 =\frac1{C_Mm}(\beta R)^{2m}\{1+o(1)\}
 \longrightarrow\infty.$$

Equations [\[eq:S-scale\]](#eq:S-scale){reference-type="eqref" reference="eq:S-scale"} and $\beta r_H=\lambda^{-1/2}$ give $$\label{eq:scaled-close}
 r_H^{2m}S_m^-=\frac{2m}{C_M}\lambda^{-m}\{1+o(1)\}
 \longrightarrow0.$$ Likewise $$r_H^{2m}\frac{F_m^{\rm orb}}m
 =\frac2{C_M}\lambda^{-m}\{1+o(1)\}\longrightarrow0.$$ Eventual positivity of $S_m^-$ proves [\[eq:domain\]](#eq:domain){reference-type="eqref" reference="eq:domain"}. For $x_m\to0$, $$\label{eq:root-expansion}
 1-(1-x_m)^{1/(2m)}
 =\frac{x_m}{2m}\{1+o(1)\}.$$ Apply this with $x_m=r_H^{2m}X_m$. The far correction is smaller than $S_m^-$ by a factor $m^{-1}\{1+o(1)\}$, so both choices give $$\delta_m(X)
 =\frac1{C_M}\lambda^{-m}\{1+o(1)\}
 =C_*\sqrt{\sigma_m}\{1+o(1)\},$$ proving [\[eq:common-law\]](#eq:common-law){reference-type="eqref" reference="eq:common-law"}. Exact recovery by [\[eq:inverse\]](#eq:inverse){reference-type="eqref" reference="eq:inverse"} and substitution in [\[eq:lower\]](#eq:lower){reference-type="eqref" reference="eq:lower"} with $Y_m^-=0$ give zero and $F_m^{\rm orb}/m=2G_m$. Dividing the latter by $2H_m$ proves the exact first equality in [\[eq:far-weighted\]](#eq:far-weighted){reference-type="eqref" reference="eq:far-weighted"}; [\[eq:G-over-H\]](#eq:G-over-H){reference-type="eqref" reference="eq:G-over-H"} completes the proof.

The map [\[eq:inverse\]](#eq:inverse){reference-type="eqref" reference="eq:inverse"} constructs scalar eigenvalue sequences satisfying the exact packet formula and the leading square-root law. It does not construct noisy transfer operators, replace the actual $\lambda_-(\sigma)$, or prescribe the actual orbit-free remainder. The opposite target behaviors prove insufficiency of the scalar information class only.

# Executable protocol, verdict, and next route

The executable artifact evaluates the exact period-$2m$ boundary multiplier, the period-$2k$ radial sideband, and the two inverse parity envelopes at $m=8,16,24,40$ with $k=m+1$. It checks:

1.  the same-clock relation and the exact phase equation;

2.  positivity and the legal inverse-map domain for both packets;

3.  exact recovery at exponent $1/(2m)$;

4.  convergence of both gap ratios to the common square-root law;

5.  zero versus $F_m^{\rm orb}/m=2G_m$ scalar residuals; and

6.  equality of the far weighted term with $G_m/H_m$.

The finite rows are formula-reproduction checks only. They are not interval certificates, asymptotic evidence, or observations of an actual noisy operator.

The lower scalar route is therefore `STOP_SCOPED`: off balance it fails under a target-negligible actual remainder, and at balance the proved scalar information admits opposite exact target behavior. Actual lower compensation and noncompensation remain `NOT_TESTABLE`/open.

RH-348 must return to the punctured strict-prefix aggregate $$2\le n<4k,\qquad n\notin\{2k,2k-2\},$$ and either control it as one signed physical object or isolate another physical sideband atom. Two selected-order analyses do not close $E_{\rm off,(4k)}$ [@WangSynchronizedPrefix2026; @WangActualFrontier2026; @WangCriticalPhase2026].

RH-288 remains inactive. Gates A--E remain false/open. This paper constructs no Hilbert--Polya operator, identifies no Riemann zero, proves no von Mangoldt prime-power trace, proves no completed-zeta divisor equality, and does not prove the Riemann Hypothesis.
