---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-mu3-yukawa-mark-first-passage-joint-coupling"
canonical_tex: "henon_dynamics/henon_mu3_yukawa_mark_first_passage_joint_coupling/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_mu3_yukawa_mark_first_passage_joint_coupling/paper/main.pdf"
source_sha256: "53d210cc2e42b70ede5a478c29ec5ca1813faa6b6d5b97d200c30ae45c6a49ce"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Exact Joint Survival and Mixed Moments for Twenty First-Passage Targets

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_first_passage_joint_coupling>)
- [规范 TeX](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_first_passage_joint_coupling/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_first_passage_joint_coupling/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_first_passage_joint_coupling/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We compute the complete joint first-passage coupling induced by a uniform ordering of the sixteen frozen labels. For every ordered pair of the twenty actual subgroup targets, all $17\times17$ joint survival counts and reduced probabilities are exact. Nested support enumeration supplies the counts, while two-dimensional tail summation gives mixed moments through bidegree six and covariance. Every marginal is recovered in 400 independent pair checks. A separate bitset/zeta reconstruction, SymPy arithmetic, clean replay, and thirteen hostile mutations audit the receipt. The scope is `NO_BAD_EULER_OR_ROOT_NUMBER`.
author:
- Anonymous
title: 'Exact Joint Survival and Mixed Moments for Twenty First-Passage Targets'
```

## Markdown 正文

# Joint survival surface

Let $T_i$ and $T_j$ be C88 first-passage times and define $$J_{ij}(k,l)=\#\{\pi:T_i(\pi)>k,\ T_j(\pi)>l\},\qquad 0\leq k,l\leq16.$$ For $k\leq l$, choose a non-hit $k$-support $A$ for $i$ and a non-hit $l$-support $B\supseteq A$ for $j$. The pair has $k!(l-k)!(16-l)!$ completions to a full permutation. The reverse order is obtained by transposition.

The canonical C90 receipt contains every $J_{ij}(k,l)$ for all 400 ordered pairs. With $\Delta_a(k)=(k+1)^a-k^a$ and $a,b\leq6$, $$\mathbb E[T_i^aT_j^b]=\frac1{16!}\sum_{k,l=0}^{15}
 \Delta_a(k)\Delta_b(l)J_{ij}(k,l).$$ Orders $(a,0)$ and $(0,b)$ recover the exact C89 marginal raw moments, and the covariance is $\mathbb E[T_iT_j]-\mathbb E[T_i]\mathbb E[T_j]$.

The first statement follows by partitioning permutations according to their two nested prefix supports. The displayed formula is the finite two-variable tail-sum identity; the marginal and covariance formulas are immediate specializations.

# Exact inventory and audit

There are $400\cdot289=115600$ joint survival cells, $400\cdot49$ mixed moment cells, and 400 covariance values. The checker reconstructs all cells from C88 hit bitsets using an independent superset zeta transform. Pair transpose symmetry, diagonal single-target survival recovery, monotone tail surfaces, and both marginal axes are checked exactly. SymPy verifies every mixed moment and covariance. Clean replay preserves $$\texttt{c457a267b2621c71f7f5ad810ce9dec41aacfe25de3e843fab1398be75571978}.$$

No arithmetic/local-data, Euler-factor, root-number, automorphy, full Burnside/table-of-marks, or Hilbert--Polya operator claim is made.
