---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-mu3-yukawa-mark-first-passage-minmax-aggregation"
canonical_tex: "henon_dynamics/henon_mu3_yukawa_mark_first_passage_minmax_aggregation/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_mu3_yukawa_mark_first_passage_minmax_aggregation/paper/main.pdf"
source_sha256: "1e655ac32a6abf798f74c8eda4f710c116cd13ebd74fc3043a6b6f79bf5464b7"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Exact Minimum and Maximum Aggregation for Finite First Passage

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_first_passage_minmax_aggregation>)
- [规范 TeX](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_first_passage_minmax_aggregation/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_first_passage_minmax_aggregation/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_first_passage_minmax_aggregation/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We derive the exact distributions of the minimum and maximum of every ordered pair of twenty frozen first-passage variables on uniform permutations of sixteen labels. Two-dimensional finite differences of the C90 joint survival arrays produce 400 joint laws, from which 13600 minimum/maximum coefficient cells and 13600 tail/CDF identities are certified. The pointwise sum identity and diagonal reductions are checked exactly. The result is finite combinatorics under `NO_BAD_EULER_OR_ROOT_NUMBER`.
author:
- Anonymous
title: Exact Minimum and Maximum Aggregation for Finite First Passage
```

## Markdown 正文

# Aggregation identities

Let $T_i\in\{0,\ldots,16\}$ and $S_{ij}(k,\ell)=\#\{T_i>k,T_j>\ell\}$. Finite Mobius inversion gives $$N_{ij}(a,b)=S_{ij}(a-1,b-1)-S_{ij}(a,b-1)-S_{ij}(a-1,b)+S_{ij}(a,b).$$ Define $U_{ij}=\min(T_i,T_j)$ and $V_{ij}=\max(T_i,T_j)$. Then $$\#\{U_{ij}>k\}=S_{ij}(k,k),\qquad
\#\{V_{ij}\le k\}=16!-S_i(k)-S_j(k)+S_{ij}(k,k).$$

For all 400 ordered pairs the derived minimum and maximum laws are nonnegative, normalized, transpose-compatible, and satisfy $$\mathbb E U_{ij}+\mathbb E V_{ij}=\mathbb E T_i+\mathbb E T_j.$$ On the diagonal, $U_{ii}=V_{ii}=T_i$ exactly.

The coefficient laws are pushforwards of the exact joint PMF. The two tail identities follow from the definitions and inclusion--exclusion. The expectation equality is the pointwise identity $\min(x,y)+\max(x,y)=x+y$. Diagonal and transpose assertions follow from $T_i=T_i$ and $N_{ij}(a,b)=N_{ji}(b,a)$.

  certified object                                count
  --------------------------------------- -------------
  ordered target pairs                              400
  minimum and maximum coefficient cells           13600
  joint PMF cells independently checked          115600
  minimum-tail / maximum-CDF identities     6800 / 6800
  sum and diagonal identities                  400 / 20

# Scope

The package is a finite probability certificate. It makes no arithmetic/local data, Euler-factor, root-number, automorphy, full Burnside/table-of-marks, or Hilbert--Pólya operator claim.
