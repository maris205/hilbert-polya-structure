---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-235-trace-vs-hilbert-schmidt-separation"
canonical_tex: "zeta_mvp0/papers/RH-235-trace-vs-hilbert-schmidt-separation/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-235-trace-vs-hilbert-schmidt-separation/main.pdf"
source_sha256: "198c1d92fa633c273905505fdeb01da8eeb20f1632e43218b5f292aa84885816"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Trace Powers versus Hilbert--Schmidt Mass in Nonnormal Cloud Complements

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-235-trace-vs-hilbert-schmidt-separation>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-235-trace-vs-hilbert-schmidt-separation/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-235-trace-vs-hilbert-schmidt-separation/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-235-trace-vs-hilbert-schmidt-separation/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-235-trace-vs-hilbert-schmidt-separation/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-229 found that the whole-complement Frobenius estimate grows roughly like $\sigma^{-1}$ and cannot prove a normal relative determinant family. We show that this failure is not a determinant obstruction. The $N$-dimensional nilpotent shift has $\left\lVert S_N\right\rVert_2^2=N-1$, while $\operatorname{tr}(S_N^n)=0$ for every $n\ge1$ and $\det_2(I-zS_N)\equiv1$. Nonnormal singular-value mass can therefore diverge without contributing any spectral determinant mass.

  For each RH-222 endpoint we compute the exact finite trace of the squared scaled matrix and subtract the Perron, parity, and selected-cloud squares. The maximum complement second-trace modulus is $0.12952$, whereas the inherited Hilbert--Schmidt squared upper bound reaches $308.75$. The largest ratio is $2.36\times10^6$. Hence the Frobenius route is too strong; the next meaningful target is a uniform envelope for the cloud-extracted power traces.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: 'Trace Powers versus Hilbert--Schmidt Mass in Nonnormal Cloud Complements'
```

## Markdown 正文

# Two different notions of complement size

The regularized determinant has logarithmic germ $$\log\det_2(I-zB)=-\sum_{n\ge2}\frac{z^n}{n}\operatorname{tr}(B^n).$$ An ideal-norm argument controls these traces through $|\operatorname{tr}(B^n)|\le\left\lVert B^n\right\rVert_1$, for example $\left\lVert B^2\right\rVert_1\le\left\lVert B\right\rVert_2^2$ [@Simon2005]. The inequality is sufficient but can be extremely wasteful for nonnormal operators.

RH-229 measured precisely this sufficient budget and found it divergent [@WangRH229]. The present question is whether the divergence is spectral or merely singular-value mass.

# Exact nilpotent separation

Let $S_N\in\mathbb C^{N\times N}$ be the shift with ones on the first superdiagonal and zero elsewhere. Then $$\left\lVert S_N\right\rVert_2^2=N-1,
 \qquad
 \operatorname{tr}(S_N^n)=0\quad(n\ge1),
 \qquad
 \det_2(I-zS_N)=1.$$ In particular $\left\lVert S_N\right\rVert_2\to\infty$ while the regularized determinant is identically constant.

There are $N-1$ unit entries, proving the Hilbert--Schmidt identity. The matrix is strictly upper triangular, as is every positive power, so every power trace vanishes. All eigenvalues are zero, hence the canonical regularized product equals one.

This example is maximally nonnormal, but that is exactly its purpose: no logical implication from a divergent Hilbert--Schmidt norm to determinant divergence can hold without additional structure.

Let $B$ be any fixed finite matrix and let $a_N\in\mathbb C$. Define $$A_N=B\oplus a_NS_N.$$ Then, for every $n\ge1$, $$\operatorname{tr}(A_N^n)=\operatorname{tr}(B^n),
 \qquad
 \det_2(I-zA_N)=\det_2(I-zB),$$ whereas $$\left\lVert A_N\right\rVert_2^2=\left\lVert B\right\rVert_2^2+|a_N|^2(N-1).$$ Thus the Hilbert--Schmidt mass can diverge while an arbitrary fixed nontrivial regularized determinant is preserved exactly.

Powers and traces split over direct sums. The nilpotent block contributes zero to every power trace and has regularized determinant one. The Hilbert--Schmidt identity is the Pythagorean formula for block direct sums.

This extension shows that the separation is not tied to the constant determinant one. An arbitrarily complicated fixed spectral factor may coexist with an increasingly large nonnormal singular-value sector that is invisible to all power traces.

# Second-trace extraction

Let $A_{\sigma,d}$ denote either the fine or Haar-coarse scaled matrix. If $p_\sigma$, $q_\sigma$, and $C_\sigma$ denote the Perron root, parity root, and selected cloud, define $$\tau_{2,\sigma}
 =\operatorname{tr}(A_{\sigma,d}^2)
  -p_\sigma^2-q_\sigma^2
  -\sum_{\lambda\in C_\sigma}\lambda^2.$$ For a sparse real matrix, $$\operatorname{tr}(A^2)=\sum_{i,j}A_{ij}A_{ji},$$ so this coefficient can be computed without diagonalizing the unresolved matrix.

  Batch statistic                                         value
  ------------------------------------- -----------------------
  Endpoint count                                             32
  Maximum $|\tau_{2,\sigma}|$                       $0.1295197$
  Minimum $|\tau_{2,\sigma}|$             $3.8778\times10^{-5}$
  Maximum complement HS-squared upper                $308.7521$
  Maximum HS-squared/$|\tau_2|$ ratio        $2.3619\times10^6$

  : Spectral trace versus singular-value budget.

The full scaled Frobenius mass grows strongly as the mesh resolves the narrow kernel. By contrast, $\operatorname{tr}(A^2)$ itself remains near $1.633$ at the finest scales, and the selected cloud removes nearly all of the remaining spectral second moment.

# Cancellation efficiency in the archived family

It is useful to record the dimensionless ratio $$\mathcal E_{2,\sigma}
 =\frac{\text{complement HS-squared upper}}
        {|\tau_{2,\sigma}|}.$$ This is not a condition number and becomes infinite when the denominator vanishes. It measures only how much larger the cancellation-blind sufficient budget is than the signed spectral coefficient that actually enters $\log\det_2$ at order two. Across the batch it ranges from ordinary two-digit values at the coarsest endpoints to $2.36\times10^6$. The sign of $\tau_2$ also changes with noise and channel, confirming that phase and nonnormal cancellation, rather than positive mass, govern this coefficient.

The sparse identity $\operatorname{tr}(A^2)=\sum_{i,j}A_{ij}A_{ji}$ avoids an unresolved eigendecomposition, but subtraction can still lose relative accuracy when $\tau_2$ is tiny. Accordingly the archive treats the values as frozen double-precision observations. A theorem would require interval control of the full trace and the extracted cloud sum, or an analytic trace formula in which their cancellation is performed before numerical evaluation.

# Why one trace coefficient is not enough

The second coefficient is the first nontrivial term of the regularized logarithm, so its smallness is necessary for convergence to a normalized limit with vanishing quadratic coefficient. It is not sufficient for a normal determinant family. Higher traces may remain large even when $\tau_2=0$, and no bound on $\tau_n$ for $n\ge3$ follows from signed cancellation at order two.

There are therefore two logically separate lessons:

1.  failure of a Hilbert--Schmidt bound does not close the determinant route;

2.  success at one or finitely many trace orders does not close it either.

The useful replacement is an order-uniform, noise-uniform trace envelope, not merely a smaller norm surrogate.

# What the separation buys

The nilpotent theorem and the finite audit jointly show that the route $$\text{uniform HS complement}
 \Longrightarrow
 \text{normal relative determinant}$$ is sufficient but not necessary. It is therefore legitimate to replace the failed norm gate by a direct trace gate.

This replacement has a cost. One must control every $n\ge2$, not merely $n=2$. RH-236 computes orders through twelve and RH-240 formulates an all-order geometric criterion. Until such a bound is proved, no locally uniform determinant family follows.

No claim about a Hilbert--Polya operator, zeta zeros, or the Riemann Hypothesis is made.
