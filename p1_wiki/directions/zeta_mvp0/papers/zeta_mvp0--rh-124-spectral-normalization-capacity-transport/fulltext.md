---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-124-spectral-normalization-capacity-transport"
canonical_tex: "zeta_mvp0/papers/RH-124-spectral-normalization-capacity-transport/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-124-spectral-normalization-capacity-transport/main.pdf"
source_sha256: "df5cdac9bf57047fe47259a1038f77d04384c8e709229832c9279bfa6a9d6b2b"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Spectral Normalization and Capacity Transport Sharp Gram-Comparison Exponents and the Cost of Separate Factors

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-124-spectral-normalization-capacity-transport>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-124-spectral-normalization-capacity-transport/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-124-spectral-normalization-capacity-transport/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-124-spectral-normalization-capacity-transport/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-124-spectral-normalization-capacity-transport/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Suppose $mK^*K\preceq K'^*K'\preceq MK^*K$ and put $r=m/M$. We prove sharp cross-level factors: $q_4'\geq r^{1/2}q_4$, normalized four-volume $\nu_4'\geq r^{3/2}\nu_4$, and three-mode capacity $r\Lambda_{23}\leq\Lambda_{23}'\leq r^{-1}\Lambda_{23}$. Consequently, transporting volume and capacity as independent black boxes yields only $r^{5/2}q_4$, an extra loss $r^2$ relative to direct fourth-mode transport. All powers are sharp in separate diagonal families. A 4,096-instance audit has zero failures. This theorem fixes the normalization ledger but assumes, rather than proves, physical all-level Gram comparability.
author:
- Prime Dynamics Theory Program
bibliography:
- references.bib
date: July 2026
title: |
  Spectral Normalization and Capacity Transport\
  Sharp Gram-Comparison Exponents and the Cost of Separate Factors
```

## Markdown 正文

# Normalized quantities

Let $s_1\geq s_2\geq\cdots$ be singular values and set $$q_4=\frac{s_4}{s_1},\quad \Lambda_{23}=\frac{s_2s_3}{s_1^2},\quad \nu_4=\frac{s_2s_3s_4}{s_1^3}=\Lambda_{23}q_4.$$ The last identity is the RH-110 factor ledger. Two-sided Gram comparison implies $\sqrt m,s_j(K)\leq s_j(K')\leq\sqrt M,s_j(K)$ by ordered eigenvalue monotonicity [@HornJohnson1991; @Bhatia2007].

[\[thm:transport\]]{#thm:transport label="thm:transport"} Under $mK^*K\preceq K'^*K'\preceq MK^*K$, with $r=m/M$, $$r^{1/2}q_4\leq q_4'\leq r^{-1/2}q_4,$$ $$r\Lambda_{23}\leq\Lambda_{23}'\leq r^{-1}\Lambda_{23},\qquad
r^{3/2}\nu_4\leq\nu_4'\leq r^{-3/2}\nu_4.$$ Every displayed one-sided exponent is sharp.

Insert the singular-value bounds into each quotient after cancelling the common leading factor. Sharpness follows by diagonal scalings: use $\sqrt M$ on $s_1$ and $\sqrt m$ on $s_4$ for $q_4$; use $\sqrt M$ on $s_1$ and $\sqrt m$ on $s_2,s_3,s_4$ for $\nu_4$; reverse the first three choices for the capacity upper. The opposite bounds are analogous.

If one forgets the common operator and combines only $\nu_4'\geq r^{3/2}\nu_4$ with $\Lambda_{23}'\leq r^{-1}\Lambda_{23}$, then $$q_4'=\frac{\nu_4'}{\Lambda_{23}'}\geq r^{5/2}q_4.$$ This is weaker than the direct $r^{1/2}$ bound by exactly $r^2$.

The corollary is not a contradiction: separate sharp bounds need not be simultaneously attained. It quantifies the price of discarding correlation.

# Audit and consequence

We sample 4,096 source spectra, condition ratios spanning six decades, and independent singular scalings inside $[\sqrt m,\sqrt M]$. There are zero $q_4$, capacity, or volume failures. Three diagonal records attain the corresponding sharp factors.

![Transport-envelope efficiency and the $r^2$ loss caused by separate factorization.](<../../../../../zeta_mvp0/papers/RH-124-spectral-normalization-capacity-transport/figures/spectral_normalization_capacity_transport.pdf>){width="\\textwidth"}

RH-124 shows that a combined directional theorem should preserve common cross-level information whenever possible. It does not supply physical $m,M$ constants. No uniform Stage A, Hilbert--Polya operator, zeta-zero identification, or Riemann Hypothesis conclusion is claimed.
