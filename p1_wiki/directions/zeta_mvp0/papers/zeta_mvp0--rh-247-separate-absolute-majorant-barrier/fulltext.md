---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-247-separate-absolute-majorant-barrier"
canonical_tex: "zeta_mvp0/papers/RH-247-separate-absolute-majorant-barrier/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-247-separate-absolute-majorant-barrier/main.pdf"
source_sha256: "a4b504b631c16f999d76bb6360d5a534a9c8260a900e36e37d2a399b5c7f1905"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Separate-Absolute Majorant Barrier

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-247-separate-absolute-majorant-barrier>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-247-separate-absolute-majorant-barrier/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-247-separate-absolute-majorant-barrier/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-247-separate-absolute-majorant-barrier/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-247-separate-absolute-majorant-barrier/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The cloud-extracted trace is a cancellation-sensitive residual. We prove that a sectorwise absolute majorant, formed before physical/atomic cancellation, has root rate at least the Hardy-scaled Perron rate $r_H^{-1}>1$. The obstruction is exact and independent of the cloud size. An audit of 352 archived order cases confirms root rates from 1.2532 to 3.5568 and enormous majorant-to-residual gains. This rules out one cancellation-blind estimate, not signed or grouped quotient loops.
author:
- Bin Wang
bibliography:
- references.bib
date: July 2026
title: 'Separate-Absolute Majorant Barrier'
```

## Markdown 正文

# The cancellation-blind quantity

Write the scaled trace decomposition at a fixed noise value as $$\tau_n=t_n-p^n-q^n-\sum_{s\in S}s^n,$$ where $t_n=\operatorname{Tr}A^n$, $p$ is the Perron root, $q$ the parity root, and $S$ the selected cloud. Define the separate-absolute trace majorant $$\label{eq:majorant}
 U_n^{\rm sep}=|t_n|+|p|^n+|q|^n+\sum_{s\in S}|s|^n.$$ An absolute periodic-loop integral for the physical sector is no smaller than the first term in [\[eq:majorant\]](#eq:majorant){reference-type="eqref" reference="eq:majorant"}; hence [\[eq:majorant\]](#eq:majorant){reference-type="eqref" reference="eq:majorant"} is the most favorable sectorwise absolute test for the present purpose.

[\[thm:barrier\]]{#thm:barrier label="thm:barrier"} Suppose the scaled Perron root obeys $|p_\sigma|\ge\rho>1$ on a noise set. Then for every selected cloud and every $n\ge1$, $$U_n^{\rm sep}(\sigma)\ge\rho^n,
 \qquad
 \liminf_{n\to\infty}(U_n^{\rm sep}(\sigma))^{1/n}\ge\rho.$$ Consequently no estimate of the form $U_n^{\rm sep}(\sigma)\le Mq^n$ with $q<1$ can hold for all sufficiently large $n$ on that set.

The Perron summand in [\[eq:majorant\]](#eq:majorant){reference-type="eqref" reference="eq:majorant"} is nonnegative and equals $|p_\sigma|^n\ge\rho^n$. Taking $n$th roots and then a liminf proves the claim. A subunit geometric upper bound would force the limsup of the same roots to be at most $q<1$, a contradiction.

For the current Hardy scaling $r_H=0.85$, the archived Perron value is exactly $$|p_\sigma|=r_H^{-1}=1.1764705882352942.$$ This is the same normalization that makes the deterministic numerator target in RH-243 nontrivial. The obstruction is therefore structural, not a poor choice of numerical tolerance.

# Finite audit

Using the RH-222 clouds and RH-236 full/residual trace powers, we evaluated [\[eq:majorant\]](#eq:majorant){reference-type="eqref" reference="eq:majorant"} for all 32 endpoints and orders 2--12 [@WangRH236]. There are 352 cases. The resulting individual root rates $U_n^{\rm sep})^{1/n}$ lie in $$1.253165378203787\le (U_n^{\rm sep})^{1/n}
 \le3.5568338003788416,$$ so all 352 exceed one. The cancellation gain $U_n^{\rm sep}/|\tau_n|$ ranges from $42.68449383956666$ to $7.802289221403802\times10^{15}$; its maximum is at $(\sigma,\mathrm{side},n)=(0.005,\mathrm{right},10)$.

  quantity                                                 value
  --------------------------- ----------------------------------
  endpoints/orders                                      32 / 352
  root-rate range                             1.253165--3.556834
  cases with root rate $>1$                              352/352
  majorant/residual range       $42.6845$--$7.8023\times10^{15}$

# Scope and route consequence

Theorem [\[thm:barrier\]](#thm:barrier){reference-type="ref" reference="thm:barrier"} rules out only estimates that take absolute values of the physical, Perron, parity, and cloud sectors separately. It does not rule out the exact graded cancellation of RH-242, the orthogonal quotient of RH-245, complex kernel cancellations, or a different normalization in a new route. The finite audit uses floating archived roots and orders 2--12; it is not an all-order interval proof.

The viable envelope route must group sectors before majorization. The deterministic numerator anchor remains unresolved. Gate A remains open and Gates B--E are untouched. No Hilbert--Polya operator, zeta-divisor equality, Riemann-zero identification, or RH implication is claimed.
