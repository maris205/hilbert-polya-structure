---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-314-optimal-endpoint-logarithm-polynomial-approximation"
canonical_tex: "zeta_mvp0/papers/RH-314-optimal-endpoint-logarithm-polynomial-approximation/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-314-optimal-endpoint-logarithm-polynomial-approximation/main.pdf"
source_sha256: "cba3760f5f4a66688b7d708b1d723e97958d37230de930f34453b41e9010b151"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Optimal Hardy Approximation of the Endpoint Logarithm

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-314-optimal-endpoint-logarithm-polynomial-approximation>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-314-optimal-endpoint-logarithm-polynomial-approximation/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-314-optimal-endpoint-logarithm-polynomial-approximation/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-314-optimal-endpoint-logarithm-polynomial-approximation/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-314-optimal-endpoint-logarithm-polynomial-approximation/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We compute the exact best polynomial approximation error for the universal endpoint logarithm. Orthogonality makes the Taylor projection optimal, its squared error is the reciprocal-square tail, and the norm is asymptotic to $N^{-1/2}$. The analytic remainder identified in RH-312 is exponentially smaller, so the full deterministic target has the same leading rate. This does not realize the approximants as spectra.
author:
- Bin Wang
date: July 2026
title: Optimal Hardy Approximation of the Endpoint Logarithm
```

## Markdown 正文

# Exact projection error

Let $L(w)=\log(1-w)+w=-\sum_{n\ge2}w^n/n$, and let $\mathcal P_N$ be the polynomials of degree at most $N$ in $H^2(\mathbb D)$.

The Taylor section $S_NL=-\sum_{2\le n\le N}w^n/n$ is the unique best approximation to $L$ from $\mathcal P_N$, and $$E_N(L)^2:=\inf_{p\in\mathcal P_N}\|L-p\|_{H^2}^2
 =\sum_{n>N}\frac1{n^2}.$$ Moreover $$\frac1{N+1}\le E_N(L)^2\le\frac1N,
 \qquad E_N(L)\sim N^{-1/2}.$$

The monomials are an orthonormal basis, so the Taylor section is the orthogonal projection. The norm identity is Parseval. Comparing the decreasing function $x^{-2}$ with its upper and lower integrals proves the bounds and the asymptotic.

# The complete deterministic target

Write the RH-312 endpoint target as $L+H_{\rm reg}$, where $H_{\rm reg}$ is analytic on $|w|<r_{\rm reg}$ for some $r_{\rm reg}>1$. Its Taylor tail is $O(r^{-N})$ for every $1<r<r_{\rm reg}$. Hence

The best degree-$N$ approximation error of the full deterministic endpoint target is $N^{-1/2}(1+o(1))$.

# Boundary

If an information class limits usable degree to $N\asymp\log M/\log(q_*/q)$, the theorem yields a $1/\sqrt{\log M}$ approximation scale. This translation is conditional on that degree constraint. It is not a rate theorem for an actual noisy cloud, and Gates A--E remain false/open.
