---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-mu3-yukawa-mark-first-passage-moments-cumulants"
canonical_tex: "henon_dynamics/henon_mu3_yukawa_mark_first_passage_moments_cumulants/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_mu3_yukawa_mark_first_passage_moments_cumulants/paper/main.pdf"
source_sha256: "f4cb40120a0f40bcaf10cf05339f5319712e8ce52ce804a26ce454f2293a7dfd"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Exact Moments and Cumulants of Twenty Frozen First-Passage Times

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_first_passage_moments_cumulants>)
- [规范 TeX](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_first_passage_moments_cumulants/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_first_passage_moments_cumulants/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_first_passage_moments_cumulants/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The C88 frozen sixteen-label model supplies exact first-passage distributions for twenty subgroup targets. We compute their raw, falling-factorial, central, and cumulant moments through order six. Every entry is a rational number. A second representation reconstructs the laws from the complete C88 hit bitsets, while survival-tail summation independently recovers both ordinary and factorial moments. Probability-generating functions, clean replay, and thirteen hostile mutations complete the finite audit. The scope is `NO_BAD_EULER_OR_ROOT_NUMBER`.
author:
- Anonymous
title: 'Exact Moments and Cumulants of Twenty Frozen First-Passage Times'
```

## Markdown 正文

# Frozen random variables

Let $L$ be the sixteen named labels and let $A_k$ be the first $k$ entries of a uniformly random permutation. For each actual frozen subgroup $H$ define $T_H=\min\{k:H\leq\Phi(A_k)\}$. C88 records the exact count $N_H(k)$ of permutations with $T_H=k$.

# Moment theorem

For every one of the twenty targets and $0\leq r\leq6$, the certificate contains the exact values $$m_r=\mathbb E[T_H^r],\qquad f_r=\mathbb E[(T_H)_r],\qquad
\mu_r=\mathbb E[(T_H-\mathbb ET_H)^r],$$ and cumulants $\kappa_1,\ldots,\kappa_6$. If $S_H(k)=\Pr(T_H>k)$, then $$m_r=\sum_{k=0}^{15}((k+1)^r-k^r)S_H(k),\quad
f_r=r!\sum_{k=0}^{15}{k\choose r-1}S_H(k)\quad(r\geq1).$$

The first two identities are the finite tail-sum formulas for a nonnegative integer-valued variable. Raw moments determine central moments and cumulants through the standard binomial and moment-cumulant recursions. The producer evaluates the left sides from C88 permutation counts; the independent checker evaluates the same quantities from C88's support bitsets.

# Inventory and audit

The canonical receipt has twenty rows and $17$ distribution cells per row, then $7$ raw, factorial, and central cells and $6$ cumulants per target. The mean in every row equals its C88 expectation; the top target is $36499/3960$. SymPy verifies normalized generating functions, derivatives at one, exact central moments, and both tail identities. A clean subprocess replay preserves evidence digest $$\texttt{86a589505280721590674235626ddc21e37d57c891c726c7e6fbba98b2bd3af9}.$$

No arithmetic/local-data, Euler-factor, root-number, automorphy, full Burnside/table-of-marks, or Hilbert--Polya operator claim is made.
