---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-kingman-coalescent-genealogy-route-a"
canonical_tex: "henon_dynamics/henon_kingman_coalescent_genealogy_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_kingman_coalescent_genealogy_route_a/paper/main.pdf"
source_sha256: "13171efbe71a1cc0c61e2666faf8a205f6e273cb72d7580e8b0c5dde9056a058"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The Kingman Coalescent: An All--$n$ Genealogy and Branch-Length Atlas

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_kingman_coalescent_genealogy_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_kingman_coalescent_genealogy_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_kingman_coalescent_genealogy_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_kingman_coalescent_genealogy_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We treat the partition-valued Kingman coalescent as one mathematical owner. Unit rate per unordered block pair gives a pure-death block count with $\lambda_k=\binom{k}{2}$. Partial fractions close every hypoexponential transition, independent holding times close the MRCA law, and a projective coupling gives finite infinite-sample absorption. Scaling by the number of branches identifies total tree length with the maximum of iid $\operatorname{Exp}(1/2)$ variables, yielding an exact CDF. Markov determinants are not Artin--Mazur zeta functions.
author:
- 'HCS--C215 research certificate'
date: 28 August 2026
title: 'The Kingman Coalescent: An All--$n$ Genealogy and Branch-Length Atlas'
```

## Markdown 正文

suppressoptionalinfo 611

# Partition owner and block chain

For each $n\geq1$, start from the discrete partition of $[n]$ and merge each unordered pair of current blocks at rate one. The labelled partition process is the Kingman coalescent. Its block count $K_t$ starts at $n$ and has $$\lambda_k=\binom{k}{2}=k(k-1)/2,\qquad
Q_{k,k-1}=\lambda_k,\quad Q_{k,k}=-\lambda_k,$$ with state $1$ absorbing. Conditional on $k$ blocks, the next pair is uniform. The family is coupled by restricting a partition on $[n+1]$ to $[n]$.

For $1\leq j\leq i$ the all--$n$ transition law is hypoexponential: $$p_{ij}(t)=\left(\prod_{m=j+1}^{i}\lambda_m\right)
\sum_{\ell=j}^{i}\frac{e^{-\lambda_\ell t}}
 {\prod_{m=j,m\ne\ell}^{i}(\lambda_m-\lambda_\ell)}.
\label{eq:hypo}$$ The empty-product convention gives $p_{ii}(t)=e^{-\lambda_i t}$ and the $i=1$ absorbing row.

The formula can also be read as a semigroup certificate. Its Laplace transform is $$\int_0^\infty e^{-st}p_{ij}(t)\,dt
 =\frac{\prod_{m=j+1}^{i}\lambda_m}{\prod_{m=j}^{i}(s+\lambda_m)},$$ and direct multiplication of these triangular kernels gives $P(t+u)=P(t)P(u)$. Thus no independently fitted transition table is needed.

# MRCA time and projective limit

Let $E_k\sim\operatorname{Exp}(\lambda_k)$ be the holding time at level $k$. The pair-clock construction and memorylessness make the $E_k$ independent of one another and of the uniform merger choices. Thus $$T_n=\sum_{k=2}^{n}E_k,\qquad
M_n(s):=\mathbb E[e^{-sT_n}]=\prod_{k=2}^{n}\frac{\lambda_k}{\lambda_k+s}.$$ Consequently, $$\mathbb E[T_n]=\sum_{k=2}^{n}\frac1{\lambda_k}=2\left(1-\frac1n\right),
\qquad
\operatorname{Var}(T_n)=\sum_{k=2}^{n}\frac1{\lambda_k^2}.
\label{eq:mrca}$$

The restriction coupling is essential for the infinite statement. It gives $T_n\leq T_{n+1}$ on one probability space, hence $T_n\uparrow T_\infty$ almost surely. Summability of the means and variances implies finite absorption and $$\mathbb E[T_\infty]=2,\qquad
\operatorname{Var}(T_\infty)=4\bigl(2\zeta(2)-3\bigr)=\frac{4\pi^2}{3}-12,$$ with Laplace transform the convergent product obtained by sending $n\to\infty$. This is a projective-coupling assertion, not a claim that independent marginal sums share a sample path.

The monotonicity can be seen directly from the partition restriction: every ancestor of $[n]$ is also represented in the restricted $(n+1)$ process, while the extra leaf can only postpone the time at which all labels have coalesced. This coupling argument is separate from the elementary independent-sum calculation used for each fixed $n$.

# Total branch length

Define $L_n=\int_0^{T_n}K_t\,dt=\sum_{k=2}^{n}kE_k$. Since scaling an exponential by $k$ changes its rate to $(k-1)/2$, $$\mathbb E[e^{-sL_n}]=\prod_{j=1}^{n-1}\frac{j/2}{j/2+s},\qquad
\mathbb E[L_n]=2H_{n-1},\qquad
\operatorname{Var}(L_n)=4H_{n-1}^{(2)}.$$ Let $Y_1,\ldots,Y_{n-1}$ be iid $\operatorname{Exp}(1/2)$ variables. Their order-statistic spacings, read from the largest backwards, have rates $(n-1)/2,(n-2)/2,\ldots,1/2$. Therefore the sum above has the same law as $\max_iY_i$, and the exact CDF is $$\Pr\{L_n\leq\ell\}=\bigl(1-e^{-\ell/2}\bigr)^{n-1},\qquad \ell\geq0.
\label{eq:cdf}$$ At $n=1$, $L_1=T_1=0$ and the convention in [\[eq:cdf\]](#eq:cdf){reference-type="eqref" reference="eq:cdf"} is the constant one.

For orientation, the first Bell numbers are $$1,\ 2,\ 5,\ 15,\ 52,\ 203,\ 877,\ 4140$$ for $n=1,\ldots,8$; they are used only as an independent finite partition ledger, not as an approximation to the infinite process.

# Certificate and source boundary

The evidence payload contains 312 transition rows through $n=12$, 12 holding rows, 48 MRCA rows, 60 branch rows, and an independent Bell-number partition ledger through $n=8$. The checker recomputes partial fractions, row sums, Chapman--Kolmogorov, moments, the maximum CDF, and the $n=1$ boundary. SymPy independently verifies the rational transforms and beta-integral behind [\[eq:cdf\]](#eq:cdf){reference-type="eqref" reference="eq:cdf"}; replay and hostile mutations test reproducibility and schema closure.

The construction is attributed to Kingman (1982), without a priority or novelty claim. It has no intrinsic rational-prime carrier, primitive orbit clock, or arithmetic divisor. The strict Route-A verdict is $$\texttt{(A0\_FAIL,A1\_FAIL,A2\_FAIL,A3\_FAIL,A4\_FAIL)},\qquad
\texttt{ROUTE\_A\_REJECTED}.$$ The scope literal is `NO_BAD_EULER_OR_ROOT_NUMBER`. In particular, a finite Markov determinant, trace-log, or Laplace product is not an Artin--Mazur dynamical zeta and is not used as one.

  certificate block             rows      independent audit
  ----------------------------- --------- ----------------------------------------------
  transitions ($n\leq12$)       312       partial fractions, sums, Chapman--Kolmogorov
  MRCA / tree length            48 / 60   moments, products, exact CDF
  partition ledger ($n\leq8$)   8         Bell-number enumeration

9 J. F. C. Kingman, "The coalescent," *Stochastic Processes and their Applications* 13, 235--248 (1982), [doi:10.1016/0304-4149(82)90011-4](https://doi.org/10.1016/0304-4149(82)90011-4).
