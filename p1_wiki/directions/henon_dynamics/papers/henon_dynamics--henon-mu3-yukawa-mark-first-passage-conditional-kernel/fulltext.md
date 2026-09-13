---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-mu3-yukawa-mark-first-passage-conditional-kernel"
canonical_tex: "henon_dynamics/henon_mu3_yukawa_mark_first_passage_conditional_kernel/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_mu3_yukawa_mark_first_passage_conditional_kernel/paper/main.pdf"
source_sha256: "6590c45424e9ac17cca054ac2ed1cbd189d1231f2e39019e433d27ab642d9f42"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Exact Conditional Kernels and Variance Decompositions for Finite First Passage

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_first_passage_conditional_kernel>)
- [规范 TeX](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_first_passage_conditional_kernel/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_first_passage_conditional_kernel/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_mu3_yukawa_mark_first_passage_conditional_kernel/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We construct all exact conditional kernels $\Pr(T_j=b\mid T_i=a)$ for a frozen family of twenty first-passage variables on uniform permutations of sixteen named labels. Two-dimensional finite differences of the exact joint survival arrays give 400 nonnegative joint laws. Of 6800 candidate conditioning rows, 4980 have positive mass and 1820 are correctly left undefined. Every ordered pair satisfies cellwise Bayes balance and exact laws of total expectation and total variance; the twenty diagonal kernels are identities. The certificate is finite combinatorics under `NO_BAD_EULER_OR_ROOT_NUMBER`.
author:
- Anonymous
title: Exact Conditional Kernels and Variance Decompositions for Finite First Passage
```

## Markdown 正文

# Joint inversion

Let $T_i\in\{0,\ldots,16\}$ be the first prefix time at which target $H_i$ is hit. On the uniform space of $16!$ label permutations, write $$S_{ij}(k,\ell)=\#\{T_i>k,\ T_j>\ell\}.$$ For threshold $-1$, the corresponding boundary is the exact one-variable survival count, and $S_{ij}(-1,-1)=16!$. Define $$N_{ij}(a,b)=S_{ij}(a-1,b-1)-S_{ij}(a,b-1)
              -S_{ij}(a-1,b)+S_{ij}(a,b).
 \label{eq:mobius}$$

The array $N_{ij}$ is the exact joint PMF in permutation counts. It is nonnegative, sums to $16!$, and its row and column marginals equal the frozen single-target laws of $T_i$ and $T_j$.

Equation [\[eq:mobius\]](#eq:mobius){reference-type="eqref" reference="eq:mobius"} is two-dimensional finite Mobius inversion on the threshold grid. Summing over one coordinate telescopes to the relevant one-dimensional boundary. Summing both coordinates gives $16!$. Exact enumeration certifies nonnegativity in all $400\cdot17^2=115600$ cells.

# Conditional-kernel theorem

Put $m_i(a)=\sum_bN_{ij}(a,b)$, independent of $j$. When $m_i(a)>0$, define $$K_{ij}(a,b)=\frac{N_{ij}(a,b)}{m_i(a)}.$$ When $m_i(a)=0$, there is no conditional probability space; the certificate stores the probability row and all conditional moments as `null`.

Across all 400 ordered pairs, exactly 4980 of 6800 candidate rows define normalized kernels; the remaining 1820 are empty. Every cell obeys $$\Pr(T_i=a)K_{ij}(a,b)
 =\Pr(T_j=b)K_{ji}(b,a)
 =\frac{N_{ij}(a,b)}{16!}.
 \label{eq:bayes}$$ For every ordered pair, $$\begin{aligned}
 \mathbb E[\mathbb E(T_j\mid T_i)]&=\mathbb E(T_j),\\
 \mathbb E[\operatorname{Var}(T_j\mid T_i)]
 +\operatorname{Var}(\mathbb E[T_j\mid T_i])&=\operatorname{Var}(T_j).\end{aligned}$$ Moreover $K_{ii}(a,b)$ is the identity kernel on every attainable time.

Positive row mass gives normalization directly. Joint transpose $N_{ij}(a,b)=N_{ji}(b,a)$ proves [\[eq:bayes\]](#eq:bayes){reference-type="eqref" reference="eq:bayes"}. Weighting each conditional mean by $m_i(a)/16!$ and interchanging finite sums proves total expectation. Expanding the conditional second moments and subtracting the squared mean proves total variance. For $i=j$, the two passage times coincide pointwise, so joint mass lies only on $a=b$.

  certified object                                        count
  ----------------------------------------------- -------------
  ordered kernels / joint PMFs                              400
  joint cells and Bayes balances                         115600
  attainable / empty rows                           4980 / 1820
  total-expectation / total-variance identities       400 / 400
  diagonal identity kernels                                  20

# Independent certificate and scope

The checker reconstructs the complete canonical receipt independently. It also intersects packed support indicators to rebuild all 6800 synchronous survival cells $S_{ij}(k,k)$ directly from the single-target source, followed by factorial completion. SymPy verifies every defined rational row, moment, variance split, and reverse cell. Clean replay preserves $$\texttt{49179ea34f6f10b7e20c68914cdd7aa5bb5df775cefade69f1a40163f2e933cb},$$ and all 16 hostile mutations are rejected.

No arithmetic/local data, Euler factors, root numbers, automorphy, full Burnside ring or table of marks, or Hilbert--Polya operator is claimed.
