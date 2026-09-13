---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-mu3-yukawa-mark-first-passage-triple-coupling"
canonical_tex: "henon_dynamics/henon_mu3_yukawa_mark_first_passage_triple_coupling/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_mu3_yukawa_mark_first_passage_triple_coupling/paper/main.pdf"
source_sha256: "7cd0d0e75420300bd61ab0849c34e04f952f0ec6db5bebb51f065110a7260636"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Exact Three-Target First-Passage Coupling

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_first_passage_triple_coupling>)
- [规范 TeX](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_first_passage_triple_coupling/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_first_passage_triple_coupling/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_first_passage_triple_coupling/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We compute the exact joint first-passage-time law for every unordered triple of twenty frozen targets on uniform permutations of sixteen labels. A nested-chain closure dynamic program and three-dimensional finite differences certify 1,140 arrays with $17^3$ cells, together 5,600,820 permutation-count cells. Pair and single marginals, exact moments through order three, covariances, and third interaction cumulants are independently checked. The result is finite combinatorics under `NO_BAD_EULER_OR_ROOT_NUMBER`.
author:
- Anonymous
title: 'Exact Three-Target First-Passage Coupling'
```

## Markdown 正文

# Joint survival and inversion

Let $T_i\in\{0,\ldots,16\}$ and $$S_{ijk}(a,b,c)=\#\{\pi:T_i>a,\ T_j>b,\ T_k>c\}.$$ After sorting thresholds, the relevant supports form a nested chain $A\subseteq B\subseteq C$. Closure states are propagated label by label and contracted with the target inclusion matrix. Boundary planes are supplied by the C88 single-target and C90 pair receipts. Three-dimensional Mobius inversion gives $$N_{ijk}(a,b,c)=\Delta_a\Delta_b\Delta_c S_{ijk}(a,b,c).$$

For all 1,140 unordered target triples, $N_{ijk}$ is nonnegative and sums to $16!$. Every pair and single marginal agrees with the frozen lower-order receipt, coordinate permutations agree, and all raw moments with exponents at most three are exact. The covariance matrix and third interaction cumulant computed from those moments are exact rational values.

The closure dynamic program partitions the $4^{16}$ nested-support chains, and factorial weights count all permutations with each chain of support sizes. The boundary substitutions are the defining C88/C90 survival counts. Finite Mobius inversion is therefore the exact pushforward PMF. Marginalization and coordinate permutation are identities of the same finite count; moments and cumulants are finite sums of integer counts divided by $16!$.

  certified object                           count
  ------------------------------------ -----------
  unordered target triples                   1,140
  joint PMF cells                        5,600,820
  pair / single marginal recoveries       400 / 20
  mixed-moment cells                        72,960
  covariance and interaction records         1,140

# Scope

This package is a finite probability certificate. It makes no arithmetic or local-data, Euler-factor, root-number, automorphy, full Burnside/table-of- marks, or Hilbert--Pólya operator claim.
