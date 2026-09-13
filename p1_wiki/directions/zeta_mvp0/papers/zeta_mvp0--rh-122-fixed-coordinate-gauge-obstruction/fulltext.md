---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-122-fixed-coordinate-gauge-obstruction"
canonical_tex: "zeta_mvp0/papers/RH-122-fixed-coordinate-gauge-obstruction/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-122-fixed-coordinate-gauge-obstruction/main.pdf"
source_sha256: "cf4d6b1f72cae70b598ad9a0ee0354b39046c87ab19e01d8f8125ea132ea39a8"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The Fixed-Coordinate Gauge Obstruction Identical Relative Tails with Arbitrarily Bad Loewner Transfer

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-122-fixed-coordinate-gauge-obstruction>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-122-fixed-coordinate-gauge-obstruction/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-122-fixed-coordinate-gauge-obstruction/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-122-fixed-coordinate-gauge-obstruction/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-122-fixed-coordinate-gauge-obstruction/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We prove that the gauge in RH-120 cannot be dropped. For every $0<\varepsilon\leq1$ there are positive four-dimensional pairs $(G,D)$ and $(G',D')$ with identical relative Rayleigh constants and identical generalized spectra, related by a coordinate swap, while the best fixed-coordinate RH-120 factor is exactly $1/\varepsilon$. The swapping gauge has factor one. Thus spectral agreement of the two relative pairs does not control a common-coordinate Loewner comparison. A 512-point audit from $10^{-1}$ to $10^{-14}$ has zero failures and log--log slope $-1$. This is a sharp negative theorem, not a failure of the gauge-covariant route.
author:
- Prime Dynamics Theory Program
bibliography:
- references.bib
date: July 2026
title: |
  The Fixed-Coordinate Gauge Obstruction\
  Identical Relative Tails with Arbitrarily Bad Loewner Transfer
```

## Markdown 正文

# Best constants without a gauge

For $G,G',D,D'\succ0$, the largest $a$ and smallest $b$ satisfying $$G'\succeq aG,\qquad D'\preceq bD$$ are $$a=\lambda_{\min}(G^{-1/2}G'G^{-1/2}),\qquad
 b=\lambda_{\max}(D^{-1/2}D'D^{-1/2}).$$ RH-120 then gives $\gamma'\leq\sqrt{b/a}\,\gamma$. These constants are optimal by the variational characterization of ordered eigenvalues [@Bhatia2007; @HornJohnson1991].

# Sharp swapped-axis obstruction

[\[thm:swap\]]{#thm:swap label="thm:swap"} Fix $\gamma>0$ and $0<\varepsilon\leq1$. Let $$G_\varepsilon=\operatorname{diag}(\varepsilon,1,2,3),\qquad
 D_\varepsilon=\gamma^2G_\varepsilon,$$ and let $P$ swap the first two coordinates. Put $G'_\varepsilon=P^*G_\varepsilon P$ and $D'_\varepsilon=P^*D_\varepsilon P$. Then $$\gamma(G_\varepsilon,D_\varepsilon)
 =\gamma(G'_\varepsilon,D'_\varepsilon)=\gamma,$$ but the best identity-gauge constants are $a=\varepsilon$ and $b=\varepsilon^{-1}$. Hence the fixed-coordinate transfer factor is $\sqrt{b/a}=\varepsilon^{-1}$.

Both relative matrices equal $\gamma^2I$, so the Rayleigh constants agree. The generalized eigenvalues of $(G',G)$ contain $\varepsilon$ and $\varepsilon^{-1}$, giving $a=\varepsilon$. Since $D'=\gamma^2G'$ and $D=\gamma^2G$, the corresponding upper factor is $b=\varepsilon^{-1}$.

Using $S=P$ gives $G'=S^*GS$ and $D'=S^*DS$, so RH-120 transfers with $a=b=1$ and no loss.

The example is deliberately stronger than a mismatch of scalar norms. The entire generalized spectrum is unchanged. What fails is the unproved identification of two anisotropic frame coordinates.

# Audit and route consequence

We evaluate the family at 512 logarithmically spaced anisotropies. The computed identity-gauge factor agrees with $1/\varepsilon$, source and target gammas agree, and the swapping gauge has factor one in every case. The fitted log--log slope is $-1$ to machine precision.

![The physical relative pair is invariant, while a forced common coordinate system creates an arbitrarily bad certificate.](<../../../../../zeta_mvp0/papers/RH-122-fixed-coordinate-gauge-obstruction/figures/fixed_coordinate_gauge_obstruction.pdf>){width="\\textwidth"}

RH-122 closes the no-gauge branch: a future cross-level proof must either construct a gauge or prove an additional common-coordinate coherence law. The negative result leaves the gauge-covariant route intact and motivates the defect-stable recurrence of RH-123. No uniform physical gauge, Stage A, Hilbert--Polya operator, zeta-zero identification, or Riemann Hypothesis claim is made.
