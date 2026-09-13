---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-mu3-yukawa-mark-first-passage-comparable-delay"
canonical_tex: "henon_dynamics/henon_mu3_yukawa_mark_first_passage_comparable_delay/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_mu3_yukawa_mark_first_passage_comparable_delay/paper/main.pdf"
source_sha256: "99bbdb67abcaff46be0d520c7638c6f1a7cf86fb89536adc267043d760dc33f5"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Conditional Delays Between Comparable First-Passage Targets

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_first_passage_comparable_delay>)
- [规范 TeX](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_first_passage_comparable_delay/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_first_passage_comparable_delay/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_first_passage_comparable_delay/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We determine exact conditional delay laws for all 102 ordered comparable pairs in a frozen twenty-target subgroup first-passage model. The relation includes its twenty reflexive pairs. Two-dimensional finite differences of the C90 joint-survival cells, completed by C88 marginal boundary values, recover 29478 nonnegative joint probability-mass cells over all $16!$ label permutations. For every comparable pair we certify the pointwise target-time order, the law of the delay, its conditional laws given the lower-target time, exact means and variances, and both marginal identities. This is a finite combinatorial result under `NO_BAD_EULER_OR_ROOT_NUMBER`.
author:
- Anonymous
title: 'Conditional Delays Between Comparable First-Passage Targets'
```

## Markdown 正文

# Frozen model and question

Let $A_k$ be the set of the first $k$ labels in a uniform permutation of the sixteen frozen named labels, and let $$T_i=\min\{k:H_i\leq\Phi(A_k)\},\qquad 0\leq i\leq19.$$ C88 fixes the subgroup inclusion matrix and the marginal laws; C90 fixes $S_{ij}(k,\ell)=\#\{\pi:T_i>k,T_j>\ell\}$ for $0\leq k,\ell\leq16$. The C88 relation contains exactly 102 ordered comparable pairs, reflexive pairs included.

# Finite-difference recovery

Complete the survival grid by setting $S_{ij}(-1,-1)=16!$ and using the C88 marginal survival counts for $S_{ij}(-1,\ell)$ and $S_{ij}(k,-1)$. Define $$N_{ij}(a,b)=S_{ij}(a-1,b-1)-S_{ij}(a,b-1)
              -S_{ij}(a-1,b)+S_{ij}(a,b).$$ This boundary convention is essential at time zero; it also retains the trivial target $H_0$, for which $T_0=0$ deterministically.

For every C88-comparable pair $H_i\leq H_j$, $N_{ij}(a,b)$ is the exact number of permutations with $(T_i,T_j)=(a,b)$. It is nonnegative, sums to $16!$, and vanishes for $a>b$. Its row and column sums equal the two frozen C88 marginal masses, and every C90 survival cell is recovered by summing the upper-right tail of $N_{ij}$.

The displayed expression is inclusion--exclusion on the two survival events. Subgroup containment is monotone under enlarging a prefix support; therefore $H_i\leq H_j$ implies $T_i\leq T_j$ for every permutation. Row, column, and upper-right tail summation telescope to the stated marginals and survival counts.

# Conditional delay atlas

Put $D_{ij}=T_j-T_i$. The unconditional count at delay $d$ is $\sum_aN_{ij}(a,a+d)$. Given $T_i=t$ with positive mass, $$\Pr(D_{ij}=d\mid T_i=t)
 =\frac{N_{ij}(t,t+d)}{\sum_eN_{ij}(t,t+e)}.$$ The receipt stores this law for all seventeen conditioning times, with an explicit zero row when the event has zero mass, and stores the exact first two conditional moments and variance. In total 1041 conditional rows have positive mass. Reflexive pairs have delay zero. At the opposite boundary, the pair $(H_0,H_{19})$ recovers the top-target mean delay $36499/3960$, because $T_0=0$.

# Audit and scope

An independent implementation rebuilds all finite differences and checks all C90 tails and C88 marginals. SymPy verifies bivariate and delay generating polynomials, conditional normalization, and moment identities. Clean replay preserves evidence hash $$\texttt{53e5c9a1dbda2fa7e01af34ce6fc161ac102a312b003e1c86402ae7ec7373a3c}.$$ Seventeen hostile mutations are rejected. No arithmetic/local data, Euler factors, root numbers, automorphy, full Burnside ring or table of marks, or Hilbert--Polya operator is claimed.
