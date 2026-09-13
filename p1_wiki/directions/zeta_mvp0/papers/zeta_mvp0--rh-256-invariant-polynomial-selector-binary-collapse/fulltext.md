---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-256-invariant-polynomial-selector-binary-collapse"
canonical_tex: "zeta_mvp0/papers/RH-256-invariant-polynomial-selector-binary-collapse/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-256-invariant-polynomial-selector-binary-collapse/main.pdf"
source_sha256: "6111477291cefdf6bec7eb51e881448148e28825b96244e730e93b33cc9d58e5"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Invariant Polynomial-Selector Binary Collapse

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-256-invariant-polynomial-selector-binary-collapse>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-256-invariant-polynomial-selector-binary-collapse/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-256-invariant-polynomial-selector-binary-collapse/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-256-invariant-polynomial-selector-binary-collapse/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-256-invariant-polynomial-selector-binary-collapse/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-255 excludes every single-use shell subset in the expanded margin-32 window, leaving a signed/complex quotient selector as the next proposed input. We prove a necessary firewall: if the selector is an idempotent polynomial in the finite operator, then it is zero or the identity on each generalized root space. Its monomial coefficients may be signed or complex, but its spectral mask remains binary. Hence no real, conjugate-closed invariant idempotent polynomial supported on the resolved RH-254 window escapes the RH-255 obstruction. A finite interpolation audit exhibits complex polynomial coordinates with nodal residual below $7.31\times10^{-14}$; this is only a coordinate diagnostic. Non-idempotent quotient grouping remains open.
author:
- Bin Wang
bibliography:
- references.bib
date: July 2026
title: 'Invariant Polynomial-Selector Binary Collapse'
```

## Markdown 正文

# Invariant spectral algebra

Let $A$ be a finite complex matrix, with primary decomposition $$V=\bigoplus_{j=1}^s E_j,
 \qquad A|_{E_j}=\lambda_j I+N_j,
 \label{eq:primary}$$ where each $N_j$ is nilpotent. A polynomial selector has the form $P=p(A)$. The quotient identity of RH-245 uses a genuine invariant root space and its orthogonal quotient; it does not authorize arbitrary moment weights [@WangRH245].

[\[thm:collapse\]]{#thm:collapse label="thm:collapse"} If $P=p(A)$ and $P^2=P$, then for every primary component $E_j$, $$P|_{E_j}=\varepsilon_j I_{E_j},
 \qquad \varepsilon_j\in\{0,1\}.
 \label{eq:binary}$$ Consequently $$\operatorname{Tr}(A^nP)
 =\sum_{j=1}^s\varepsilon_j\operatorname{Tr}(A^n|_{E_j}).
 \label{eq:trace}$$ For a simple spectrum this is $\sum_j\varepsilon_j\lambda_j^n$.

On $E_j$, polynomial functional calculus gives $P=c_jI+K_j$, where $c_j=p(\lambda_j)$ and $K_j$ is nilpotent. The spectrum of an idempotent lies in $\{0,1\}$, while the spectrum of $c_jI+K_j$ is the singleton $\{c_j\}$; hence $c_j\in\{0,1\}$. If $c_j=0$, then $P|_{E_j}$ is both nilpotent and idempotent, so it is zero. If $c_j=1$, then $I-P|_{E_j}$ is nilpotent and idempotent, so it is zero. This proves [\[eq:binary\]](#eq:binary){reference-type="eqref" reference="eq:binary"}; the trace identity follows from the direct sum.

If $A$ and $P$ are real, conjugate primary components receive the same $\varepsilon_j$. Thus a real polynomial idempotent is a binary mask on real roots and complete conjugate shells.

Complex conjugation commutes with real $A$ and $P$, carrying the action on $E_\lambda$ to the action on $E_{\bar\lambda}$.

# Finite consequence for the expanded window

RH-255 proves that the full box relaxation of the expanded shell masks misses the deterministic anchor at all 32 endpoints [@WangRH255]. Since every binary mask lies in that box, Theorem [\[thm:collapse\]](#thm:collapse){reference-type="ref" reference="thm:collapse"} gives:

No real, conjugate-closed idempotent polynomial selector supported on the RH-254 expanded roots reaches the archived deterministic anchor tolerance. The finite class contains 62,030,604,700 eligible binary masks in aggregate.

The word "supported" is essential. The result says nothing about unresolved root spaces, infinite-dimensional functional calculi, or non-idempotent quotient kernels.

# Polynomial-coordinate diagnostic

For the first six complete shells at each endpoint we interpolate the mask that selects the first three shells. The polynomial is represented in the monomial basis. Across 32 endpoints we find

  quantity                                   range or maximum
  ------------------------------ ----------------------------
  interpolation residual              $\le7.31\times10^{-14}$
  nodal idempotence error          finite floating diagnostic
  coefficient $\ell^1$ norm                   7.92--33,664.62
  Vandermonde condition number          223--$1.07\times10^7$
  idempotent anchor passes                               0/32

Large and sometimes complex-looking coefficients therefore do not imply new spectral multiplicities. At the spectral nodes the values are still exactly the binary mask, subject to interpolation error.

# Route boundary

The only surviving signed route is non-idempotent grouping forced by an exact quotient or loop identity. Arbitrary signed least squares would merely fit moments and would not define a legal spectral selector. Gates A--E remain false/open. No Hilbert--Polya operator, zeta-divisor equality, Riemann-zero identification, or RH implication is claimed.
