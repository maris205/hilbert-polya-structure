---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-mu3-yukawa-mark-pair-dependence-geometry"
canonical_tex: "henon_dynamics/henon_mu3_yukawa_mark_pair_dependence_geometry/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_mu3_yukawa_mark_pair_dependence_geometry/paper/main.pdf"
source_sha256: "c8578b3dfae364a32dbcdb8d1a95983d2dca68a1df20825e49f7023f5725a1c9"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Exact Dependence Geometry for Finite First Passage

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_pair_dependence_geometry>)
- [规范 TeX](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_pair_dependence_geometry/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_pair_dependence_geometry/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_pair_dependence_geometry/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We derive exact dependence geometry for all 400 ordered pairs of twenty frozen first-passage variables. Two-dimensional finite differences give 115600 joint PMF cells, exact covariance and Pearson-square data, total variation and L1 product discrepancies, and Frechet interval geometry. The relation spectrum is 20 diagonal, 164 strict-comparable, and 216 incomparable pairs. All claims are finite probability statements under `NO_BAD_EULER_OR_ROOT_NUMBER`.
author:
- Anonymous
title: Exact Dependence Geometry for Finite First Passage
```

## Markdown 正文

# Joint law and dependence

Let $S_{ij}(k,\ell)=\#\{T_i>k,T_j>\ell\}$. The exact joint count is $$N_{ij}(a,b)=S_{ij}(a-1,b-1)-S_{ij}(a,b-1)-S_{ij}(a-1,b)+S_{ij}(a,b).$$ From $N_{ij}$ we compute $\operatorname{Cov}(T_i,T_j)$, $\rho_{ij}^2$, total variation from $P_i\otimes P_j$, the corresponding L1 distance, and the cellwise Frechet interval width and violation.

All 400 joint laws are nonnegative, normalized, and recover both C88 marginals. Transpose cells agree exactly; diagonal cells lie on the identity and have covariance equal to the target variance. Every cell obeys its Frechet interval, so the violation ledger is zero.

Finite Mobius inversion gives the joint PMF and telescoping gives the marginals. Transposition follows from exchanging the two thresholds. The diagonal is the law of $(T_i,T_i)$, and Frechet bounds are the elementary two-event bounds applied cellwise.

  certified object                        count
  --------------------------------- -----------
  ordered target pairs                      400
  joint PMF cells                        115600
  covariance/correlation records            400
  TV and L1 product discrepancies     400 / 400
  Frechet cell records                   115600

# Scope

No arithmetic/local data, Euler factors, root numbers, automorphy, full Burnside/table-of-marks, or Hilbert--Pólya operator is claimed.
