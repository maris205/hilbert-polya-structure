---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-248-anchored-shell-zonotope-reachability-obstruction"
canonical_tex: "zeta_mvp0/papers/RH-248-anchored-shell-zonotope-reachability-obstruction/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-248-anchored-shell-zonotope-reachability-obstruction/main.pdf"
source_sha256: "860afe0394d6c4f76c3420f3f718aa4defa4bd483c0fe7230657091b48a9c988"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Anchored Shell-Zonotope Reachability Obstruction

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-248-anchored-shell-zonotope-reachability-obstruction>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-248-anchored-shell-zonotope-reachability-obstruction/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-248-anchored-shell-zonotope-reachability-obstruction/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-248-anchored-shell-zonotope-reachability-obstruction/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-248-anchored-shell-zonotope-reachability-obstruction/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The anchored shell-prefix obstruction of RH-244 could have been caused by the prefix order. We remove that possibility in the frozen candidate window. Every conjugate-complete shell may be selected independently, and we solve the full convex box relaxation. An explicit LP dual certifies that the RH-243 deterministic anchor is unreachable at all 32 archived endpoints. The result is a finite zonotope obstruction, not a statement about expanded windows or signed spectral groupings.
author:
- Bin Wang
bibliography:
- references.bib
date: July 2026
title: 'Anchored Shell-Zonotope Reachability Obstruction'
```

## Markdown 正文

# Shell power zonotope

Let $b_n=\operatorname{tr}A^n-p^n-q^n$ and let $a_n$ be the RH-243 Hardy-scaled anchor [@WangRH243]. For each conjugate-complete shell $S_j$ in the RH-222 candidate window define the real power vector $$v_j=(\sum_{s\in S_j}s^n)_{n=2}^{12},
 \qquad d=(b_n-a_n)_{n=2}^{12}.$$ Conjugacy makes these vectors real; the archived imaginary leakage is zero to floating precision. A shell subset uses $w_j\in\{0,1\}$, while its box relaxation allows $0\le w_j\le1$. With weights $\omega_n=1/n$, set $$\label{eq:box}
 \delta_\Box=\min_{0\le w\le1}
 \sum_{n=2}^{12}\omega_n\left|d_n-\sum_jw_jv_{j,n}\right|.$$

[\[thm:dual\]]{#thm:dual label="thm:dual"} For the finite real matrix $V=(v_{j,n})$, $$\label{eq:dual}
 \delta_\Box=
 \max_{|y_n|\le\omega_n}
 \left[y^Td-\sum_j\max(0,y^Tv_j)\right].$$ Consequently, any feasible $y$ whose displayed value exceeds a tolerance already excludes every shell prefix, every contiguous shell interval, and every binary shell subset.

Use $|x|=\max_{|y|\le1}yx$ coordinatewise, absorb the weights into the constraints $|y_n|\le\omega_n$, and interchange the finite minimization and maximization. For fixed $y$, minimizing $-y^TVw$ over the box gives $-\sum_j\max(0,y^Tv_j)$. Strong finite-dimensional LP duality proves [\[eq:dual\]](#eq:dual){reference-type="eqref" reference="eq:dual"}.

# Audit

We reconstruct all 32 RH-222/RH-236 endpoints and solve both primal and dual LPs, in orders 2--12 and with tolerance $\varepsilon_\sigma=\sigma$ [@WangRH222; @WangRH236]. The aggregate candidate counts are $$543\ \text{prefixes},\qquad 5012\ \text{contiguous intervals},\qquad
 139572890\ \text{binary subsets of rank at least four}.$$ The exact dual lower bounds give zero passes for all three discrete classes and for the entire box relaxation.

  selection class         candidates   passes   best-distance range
  --------------------- ------------ -------- ---------------------
  prefix                         543     0/32    0.397238--0.484576
  contiguous interval           5012     0/32    0.397238--0.484576
  binary shell subset      139572890     0/32    0.168577--0.424018
  box relaxation                  --     0/32    0.146498--0.424018

The minimum box failure margin is $0.14524763462315904$, the minimum distance/tolerance ratio is $10.17255613514909$, and the maximum is $118.76033343311221$. The largest primal--dual gap is $7.72\times10^{-15}$. Every best interval begins at the outer shell. A single-coordinate certificate suffices at 24 endpoints (18 at order 2 and 6 at order 6); the other eight require the multi-order dual. The effective box ranks range from 12 to 31.430747812062542.

# Boundary

The theorem and audit concern only the frozen resolved candidate windows, complete conjugate shells used at most once, orders 2--12, real conjugate power vectors, and the RH-238 tolerance. They do not exclude deeper or additional roots, expanded windows, signed/complex grouping, continuum mechanisms, or unbounded shell multiplicities. In particular, a fractional box weight is a reachability certificate, not a legal spectral multiplicity.

The deterministic anchor is therefore not available inside the current single-use shell class. The next test may relax the upper bound on weights, while monitoring whether the required multiplicities cease to represent a finite algebraic cloud. Gate A remains open and Gates B--E are untouched. No Hilbert--Polya operator, zeta-divisor equality, Riemann-zero identification, or RH implication is claimed.
