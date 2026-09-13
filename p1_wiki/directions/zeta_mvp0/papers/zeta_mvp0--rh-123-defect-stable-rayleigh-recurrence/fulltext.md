---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-123-defect-stable-rayleigh-recurrence"
canonical_tex: "zeta_mvp0/papers/RH-123-defect-stable-rayleigh-recurrence/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-123-defect-stable-rayleigh-recurrence/main.pdf"
source_sha256: "7efbbe8609f605b8c564098379b9e3d6ce48363a4911600150532dd929611393"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Defect-Stable Rayleigh Recurrence Additive Loewner Errors and a Sharp Affine Law

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-123-defect-stable-rayleigh-recurrence>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-123-defect-stable-rayleigh-recurrence/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-123-defect-stable-rayleigh-recurrence/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-123-defect-stable-rayleigh-recurrence/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-123-defect-stable-rayleigh-recurrence/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Exact cross-level comparison is too rigid for validated computations. We prove the defect-stable form. If $H=S^*GS$, $G'\succeq a(1-\eta)H$, and $D'\preceq bS^*DS+\delta H$, where $a>0$ and $0\leq\eta<1$, then $$(\gamma')^2\leq\frac{b\gamma^2+\delta}{a(1-\eta)}.$$ The bound is sharp already for scalars and gives an affine recurrence for the squared relative tail constant. A 4,096-instance random matrix audit has zero failures. This establishes robust transfer algebra but does not prove physical all-level coefficients.
author:
- Prime Dynamics Theory Program
bibliography:
- references.bib
date: July 2026
title: |
  Defect-Stable Rayleigh Recurrence\
  Additive Loewner Errors and a Sharp Affine Law
```

## Markdown 正文

# The defect model

Let $G\succ0$, $D\succeq0$, and $D\preceq\gamma^2G$. A frame gauge gives $H=S^*GS$. Relative recent-Gram loss is represented by $\eta$, while an additive tail defect is measured in the same metric $H$. This choice is coordinate covariant and separates geometric loss from tail forcing.

[\[thm:defect\]]{#thm:defect label="thm:defect"} Assume $$G'\succeq a(1-\eta)H,\qquad
D'\preceq bS^*DS+\delta H$$ with $a>0$, $b,\delta\geq0$, and $0\leq\eta<1$. Then $$(\gamma')^2\leq\rho\gamma^2+q,qquad
\rho=\frac{b}{a(1-\eta)},\quad q=\frac{\delta}{a(1-\eta)}.$$

Congruence gives $S^*DS\preceq\gamma^2H$, hence $D'\preceq(b\gamma^2+\delta)H$. The Gram lower gives $H\preceq G'/[a(1-\eta)]$. Combining the inequalities and using the variational definition of $\gamma'$ proves the claim.

The argument is ordinary Loewner calculus [@Bhatia2007; @HornJohnson1991].

If $x_{n+1}\leq\rho x_n+q$, then for $\rho\ne1$, $$x_n\leq\rho^nx_0+q\frac{1-\rho^n}{1-\rho}.$$ For $0\leq\rho<1$, $\limsup x_n\leq q/(1-\rho)$.

# Sharpness

Take one-dimensional $G=H=1$, $D=\gamma^2$, $G'=a(1-\eta)$, and $D'=b\gamma^2+\delta$. Every hypothesis is an equality and so is the conclusion. Therefore no smaller universal coefficient of $\gamma^2$ or $\delta$ follows from this information class.

# Audit and route boundary

The audit samples 4,096 positive pairs, gauges, multiplicative constants, Gram losses, and additive tail defects. Targets are generated inside the two Loewner enclosures. There are zero hypothesis or conclusion failures, and the scalar sharp record agrees to relative error below $10^{-12}$.

![One-step efficiency and the contractive, critical, and expansive affine regimes.](<../../../../../zeta_mvp0/papers/RH-123-defect-stable-rayleigh-recurrence/figures/defect_stable_rayleigh_recurrence.pdf>){width="\\textwidth"}

RH-123 supplies the recurrence form needed for outward validation. A useful all-level result still requires physical control with $\rho<1$ and forcing small enough to keep the limiting gamma below one. RH-124 next transports normalization and capacity. No uniform Stage A, Hilbert--Polya operator, zeta-zero identification, or Riemann Hypothesis conclusion is claimed.
