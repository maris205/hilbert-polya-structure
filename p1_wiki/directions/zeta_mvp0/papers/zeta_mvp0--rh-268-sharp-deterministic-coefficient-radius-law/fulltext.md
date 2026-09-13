---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-268-sharp-deterministic-coefficient-radius-law"
canonical_tex: "zeta_mvp0/papers/RH-268-sharp-deterministic-coefficient-radius-law/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-268-sharp-deterministic-coefficient-radius-law/main.pdf"
source_sha256: "208f98f8410b714a9fd47a1781cce71f981b8166a08dd385b58bf558a29f61bd"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The Sharp Coefficient Radius of the Deterministic Numerator

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-268-sharp-deterministic-coefficient-radius-law>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-268-sharp-deterministic-coefficient-radius-law/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-268-sharp-deterministic-coefficient-radius-law/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-268-sharp-deterministic-coefficient-radius-law/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-268-sharp-deterministic-coefficient-radius-law/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Let $q_*=(r_H\lambda)^{-1}$. We prove the sharp all-order law $a_n/q_*^n\to1$ for the Hardy-scaled deterministic numerator. Hence the logarithmic coefficient root rate is exactly $q_*$, the convergence radius is exactly $q_*^{-1}$, no smaller geometric base is possible, and the absolute logarithmic series diverges at the critical radius. These are deterministic target statements, not moving-cloud asymptotics.
author:
- Bin Wang
bibliography:
- references.bib
date: July 2026
title: The Sharp Coefficient Radius of the Deterministic Numerator
```

## Markdown 正文

# Odd and even limits

For odd $n\ge3$, the exact factor formula is [@WangRH15; @WangRH267] $$\frac{a_n}{q_*^n}=\frac1{1+\lambda^{-n}}\longrightarrow1.$$ For even $n=2m$, RH-263 gives $$\frac{a_{2m}}{q_*^{2m}}
 =2\lambda^{2m}\operatorname{tr}(T^m)
 +\frac{1-2\lambda^{-m}}{1-\lambda^{-2m}}.$$ If $m=3k+j$, the RH-13 trace-ideal estimate [@WangRH13] gives $$|\lambda^{2m}\operatorname{tr}(T^m)|
 \le \nu_j\lambda^{2j}(q_3\lambda^6)^k,
 \qquad q_3\lambda^6<0.801254.$$ Thus the trace term tends to zero, while the endpoint fraction tends to one.

For the complete sequence $n\ge2$, $$\boxed{\displaystyle\lim_{n\to\infty}\frac{a_n}{q_*^n}=1.}$$

# Radius and negative consequences

The power series $-\sum_{n\ge2}a_nz^n/n$ has exact radius $$\rho_*=q_*^{-1}=r_H\lambda=1.4267874838640739\ldots .$$

Since $n^{1/n}\to1$, the coefficient root rate of $a_n/n$ is $q_*$. The Cauchy--Hadamard formula gives the radius.

There are no constants $C<\infty$ and $q<q_*$ such that $|a_n|\le Cq^n$ for all $n$. Moreover $$\sum_{n\ge2}\frac{|a_n|\rho_*^n}{n}=\infty.$$

The first claim contradicts the exact root rate. For the second, $|a_n|\rho_*^n\to1$, so the terms are asymptotic to the harmonic series.

The order-2--28 ratios approach one numerically, but no finite fit is used in the proof. The sharp rate belongs only to the deterministic target. It does not provide a cloud coefficient bridge, legal selector, or uniform quotient tail. Gates A--E and all Hilbert--Polya/zeta/RH claims remain false/open.
