---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-mu3-yukawa-mark-first-passage-label-sensitivity"
canonical_tex: "henon_dynamics/henon_mu3_yukawa_mark_first_passage_label_sensitivity/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_mu3_yukawa_mark_first_passage_label_sensitivity/paper/main.pdf"
source_sha256: "87dbb3637ee7ca340310e0c69d204d68cc67f857bdaa61555f1fd7f5b6f7e846"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Label Sensitivity of Exact Subgroup First Passage

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_first_passage_label_sensitivity>)
- [规范 TeX](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_first_passage_label_sensitivity/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_first_passage_label_sensitivity/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_first_passage_label_sensitivity/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We resolve the labelwise sensitivity of the exact random-order first-passage variables from the frozen sixteen-label closure model. For each of twenty subgroup targets and all sixteen labels, we enumerate the exact pivotal-rank law over all $16!$ permutations. The pivotal probabilities, rank-weighted contributions, and rank-square contributions recover the C88 first-passage mass, mean, and second moment by exact efficiency identities. The complete $20\times16$ atlas is independently reconstructed and checked symbolically. This is a finite combinatorial result under `NO_BAD_EULER_OR_ROOT_NUMBER`.
author:
- Anonymous
title: Label Sensitivity of Exact Subgroup First Passage
```

## Markdown 正文

# Definition

Let $L=\{S_1,\ldots,S_{16}\}$ and let $T_H$ be the C88 first prefix time whose generated subgroup contains $H$. A label $S_i$ is pivotal at rank $k$ when it belongs to the hitting prefix $A_k$ but deleting it from that prefix removes the target containment. Write $p_H(i,k)$ for the number of permutations with this event and first passage at $k$.

# Exact identity

For every target $H$, label $S_i$, and $k\geq1$, $$p_H(i,k)=\#\{A:|A|=k,S_i\in A,H\leq\Phi(A),
H\not\leq\Phi(A\setminus\{S_i\})\}(k-1)!(16-k)!.$$ For every nontrivial target, $$\sum_{i,k}p_H(i,k)=16!,\qquad
\sum_{i,k}k\,p_H(i,k)=16!\,\mathbb E[T_H],$$ and the analogous identity with $k^2$ recovers $16!\,\mathbb E[T_H^2]$. For the trivial target all terms vanish.

The displayed support count fixes the unordered prefix and its last label. The first $k-1$ positions and the suffix can then be ordered independently, giving the factorial factor. Each nontrivial permutation has exactly one last pivotal label at its first hitting prefix, so summing over labels and ranks partitions the first-passage permutations. Multiplication by $k$ or $k^2$ gives the moment identities.

# Complete finite atlas

The canonical receipt contains all 320 target-label rows, every rank cell, reduced pivotal probability, conditional pivotal rank mean, and the global label totals. The top target has mean $36499/3960$ as in C83/C88. The order two target is pivotal only through $S_9$. The top target has ten nonzero label contributions, all recorded in the receipt; these are observations of the frozen named coordinates, not an affine or arithmetic classification.

# Audit and scope

An independent checker reconstructs every pivotal row directly from the C88 hit bitsets. SymPy verifies the probability, first-moment, second-moment, and generating-polynomial identities. Clean replay preserves the evidence hash $$\texttt{902d6b2fd688abc525d2fab187559bfc9904c7f3c97dc51af62050586d145812}.$$ No arithmetic/local data, Euler factors, root numbers, automorphy, full Burnside ring or table of marks, or Hilbert--Polya operator is claimed.
