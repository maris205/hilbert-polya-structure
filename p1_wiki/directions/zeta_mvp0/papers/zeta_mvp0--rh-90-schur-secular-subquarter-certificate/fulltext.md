---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-90-schur-secular-subquarter-certificate"
canonical_tex: "zeta_mvp0/papers/RH-90-schur-secular-subquarter-certificate/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-90-schur-secular-subquarter-certificate/main.pdf"
source_sha256: "2c50d75e47cd349af0dbac8c57fee756f7450d5ac423345333e8d0a72894b879"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Schur--Secular Sub-Quarter Contraction Certificates Full-Reference-Free Validation of Rank-One Packet Correction

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-90-schur-secular-subquarter-certificate>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-90-schur-secular-subquarter-certificate/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-90-schur-secular-subquarter-certificate/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-90-schur-secular-subquarter-certificate/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-90-schur-secular-subquarter-certificate/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-89 showed that one complement direction and an $(r+1)$-dimensional Ritz solve recover more than $96\%$ of the full floating correction dividend at all ten anchors. This paper removes the full reference packet from the finite contraction certificate.

  Write the enriched compression as $$H=\begin{pmatrix}A&b\\b^*&d\end{pmatrix}.$$ Its rank-$r$ correction gain over the old coordinate packet is exactly $\Delta=d-\lambda_{\min}(H)$. For any $\delta\ge0$ and vector $x$, define $$\Phi_\delta(x)=
   x^*(A-(d-\delta)I)x-2\operatorname{Re}(x^*b)+\delta.$$ The Schur trial gain certificate states that $\Phi_\delta(x)\le0$ implies $\Delta\ge\delta$. It is a one-vector Rayleigh test and needs neither an inverse nor an eigengap. If $C$ is the old-packet predictor tail, $E$ the previous memory tail, and $\delta=C-\rho E$, the target contraction corollary gives a corrected tail at most $\rho E$.

  For $\rho=0.24$, one archived channel is already below target before correction. In all nine remaining channels, a binary linear-solve trial has a strictly negative 256-bit Schur form. The smallest actual-to-required gain ratio exceeds $1.003$, and direct corrected residuals are below $0.24E$ in all ten channels. The hardest certified Schur margin is about $2.9\times10^{-16}$; solve dimensions never exceed seven.

  This is a full-reference-free certificate for the frozen models, not a uniform Schur-margin theorem. Stage A, Hilbert--Polya, and the Riemann Hypothesis remain open.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Schur--Secular Sub-Quarter Contraction Certificates\
  Full-Reference-Free Validation of Rank-One Packet Correction
```

## Markdown 正文

**Keywords:** Schur complement; secular equation; Rayleigh certificate; dynamic packet; validated numerics.

**MSC 2020:** 47A75; 65F15; 15A18; 65G20.

# Removing the full reference packet

RH-89 constructs the old-packet/new-Gram cross direction and solves a rank-$r$ Ritz problem in dimension $r+1$ [@WangRitz2026]. Its audit compared the small corrected packet with a full floating reference packet. For an all-level proof this comparison is unnecessary: one only needs enough gain to cross a prescribed contraction threshold.

Let $H$ be the Hermitian compression to the enriched coordinates, partitioned as above. The old packet captures $\operatorname{tr}A$. Retaining the top $r$ eigenvalues of $H$ captures $\operatorname{tr}H-\lambda_{\min}(H)$, so the exact gain is $$\Delta=d-\lambda_{\min}(H).
 \label{eq:gain}$$

# Schur trial gain certificate

[\[thm:schur\]]{#thm:schur label="thm:schur"} For any $\delta\ge0$ and $x\in\mathbb C^r$, if $$\Phi_\delta(x)=
 x^*(A-(d-\delta)I)x-2\operatorname{Re}(x^*b)+\delta\le0,
 \label{eq:phi}$$ then $\Delta\ge\delta$.

Set $y=(x,-1)$. Direct expansion gives $$y^*(H-(d-\delta)I)y=\Phi_\delta(x)\le0.$$ The Rayleigh principle therefore implies $\lambda_{\min}(H)\le d-\delta$. Insert this inequality into [\[eq:gain\]](#eq:gain){reference-type="eqref" reference="eq:gain"} [@Bhatia1997; @HornJohnson2013].

No inverse is part of the theorem. Numerically, one may choose $x$ by approximately solving $(A-(d-\delta)I)x=b$ and then validate [\[eq:phi\]](#eq:phi){reference-type="eqref" reference="eq:phi"} directly. Ill conditioning affects how the trial is found, but not the logic of the final sign certificate.

[\[cor:target\]]{#cor:target label="cor:target"} Let $E>0$ be the previous memory tail and $C$ the new tail obtained by retaining the old packet. Fix $0<\rho<1$ and set $\delta=C-\rho E$. If $\delta\le0$, the predictor already meets the target. If $\delta>0$ and [\[eq:phi\]](#eq:phi){reference-type="eqref" reference="eq:phi"} holds, the rank-one Ritz corrected tail is at most $\rho E$.

The corrected tail equals $C-\Delta$. Apply [\[thm:schur\]](#thm:schur){reference-type="ref" reference="thm:schur"} to obtain $C-\Delta\le C-\delta=\rho E$.

This criterion needs only one rank-$r$ trial solve and one scalar sign.

# Ten-channel 256-bit audit

We set $\rho=0.24$ at the final predictor-corrector update. The old and corrected residual energies are evaluated directly after exact binary lifting. The small Schur form uses the frozen compressed matrix and a lifted floating trial vector. The enriched-basis orthogonality defect remains below $2\times10^{-15}$.

::: {#tab:audit}
    $\sigma$   channels needing correction   min gain ratio   min negative margin   max corrected
  ---------- ----------------------------- ---------------- --------------------- ---------------
        0.16                             2             1.57    $4.0\times10^{-8}$          0.0043
        0.08                             2             2.49   $1.0\times10^{-12}$          0.0212
        0.04                             1             2.09   $3.2\times10^{-14}$          0.0584
        0.02                             2            1.003   $2.9\times10^{-16}$          0.2385
        0.01                             2             1.10   $4.7\times10^{-15}$          0.1900

  : Worst rounded Schur and direct-contraction quantities by scale. Gain ratio means actual small Ritz gain divided by the gain required for the $0.24$ target.
:::

The near-active case is the left channel at $\sigma=0.02$. Its trial system is highly conditioned, but the theorem uses only the final quadratic sign, which remains strictly negative at 256 bits. No full optimal packet appears in this certificate.

![Predictor demand, gain sufficiency, certified Schur margins, and direct full-reference-free contraction.](<../../../../../zeta_mvp0/papers/RH-90-schur-secular-subquarter-certificate/figures/schur_secular_subquarter_certificate.pdf>){#fig:audit width="\\textwidth"}

# Boundary and next theorem

The remaining analytic statement is now small and explicit: after a suitable burn-in, construct a cross-block trial vector $x_{\sigma,j}$ and prove $\Phi_{C-\rho E}(x_{\sigma,j})\le0$ uniformly with clock rank $O(\log(1/\sigma))$. A proof may estimate the three terms in [\[eq:phi\]](#eq:phi){reference-type="eqref" reference="eq:phi"} directly, without tail eigengaps or ambient singular vectors.

RH-90 proves the Schur and target-contraction results and validates all ten frozen channels. It does not prove a uniform Schur margin, close Stage A1 or Stage A4, construct a relative determinant or self-adjoint Hilbert--Polya operator, identify zeta zeros, or prove the Riemann Hypothesis.
