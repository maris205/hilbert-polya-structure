---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-112-global-wedge-lipschitz-barrier"
canonical_tex: "zeta_mvp0/papers/RH-112-global-wedge-lipschitz-barrier/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-112-global-wedge-lipschitz-barrier/main.pdf"
source_sha256: "923c0dd3694e72769a419669063c8cf1792df7be8d4bbb9c59b1d597195e01d5"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The Global Wedge-Lipschitz Barrier A Sharp Negative Result for Fourth-Mode Support

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-112-global-wedge-lipschitz-barrier>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-112-global-wedge-lipschitz-barrier/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-112-global-wedge-lipschitz-barrier/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-112-global-wedge-lipschitz-barrier/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-112-global-wedge-lipschitz-barrier/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We test a natural shortcut in finite-memory fourth-mode certification: perturb the fourth exterior operator directly instead of perturbing four singular values. If $K=A+E$, $\left\lVert E\right\rVert\leq\delta$, then $$\left\lVert\mathop{\bigwedge}\nolimits^4K-\mathop{\bigwedge}\nolimits^4A\right\rVert\leq(\left\lVert A\right\rVert+\delta)^4-\left\lVert A\right\rVert^4.$$ The constant is sharp using only $\left\lVert A\right\rVert$ and $\delta$. We prove, however, that the normalized lower certificate obtained from this inequality is always dominated by the product Weyl certificate. Its exact positivity radius is $s_1((1+\widehat\nu_4)^{1/4}-1)\sim
  s_1\widehat\nu_4/4$, compared with $s_4$ for product Weyl. A 360-record five-scale audit has zero domination failures and quantifies the loss. This is a negative result for global norm-only exterior perturbation, not for directional wedge methods.
author:
- Prime Dynamics Theory Program
bibliography:
- references.bib
date: July 2026
title: |
  The Global Wedge-Lipschitz Barrier\
  A Sharp Negative Result for Fourth-Mode Support
```

## Markdown 正文

# Question and conclusion

Let $s_1(A)\geq\cdots\geq s_r(A)$ and $$\widehat\nu_4=\frac{s_1s_2s_3s_4}{s_1^4}.$$ RH-109 used individual Weyl inequalities to propagate this normalized four-volume through a finite-memory tail. The global alternative is to view $A\mapsto\mathop{\bigwedge}\nolimits^4A$ as one polynomial operator and apply a Lipschitz estimate. The appeal is coordinate freedom. The obstruction is that a norm-only constant charges all four slots at $s_1$, erasing the weak-mode geometry.

Our conclusion is exact: the global method cannot improve product Weyl for any spectrum or tail radius. Since the global constant is itself sharp, improvement requires directional or structured information.

# Sharp exterior perturbation law

Exterior powers are understood as operators between the fourth exterior spaces, equipped with their Hilbert norms [@HornJohnson1991].

Let $A,E$ be bounded operators between finite-dimensional Hilbert spaces and $\left\lVert E\right\rVert\leq\delta$. For every positive integer $k$, $$\label{eq:lipschitz}
 \left\lVert\mathop{\bigwedge}\nolimits^k(A+E)-\mathop{\bigwedge}\nolimits^kA\right\rVert
 \leq (\left\lVert A\right\rVert+\delta)^k-\left\lVert A\right\rVert^k.$$ The right side cannot be reduced using only $\left\lVert A\right\rVert$ and $\delta$.

Expand the alternating $k$-linear map into terms containing $j$ copies of $E$. There are $\binom{k}{j}$ such terms, each with norm at most $\left\lVert A\right\rVert^{k-j}\delta^j$. Summing for $j\geq1$ gives [\[eq:lipschitz\]](#eq:lipschitz){reference-type="eqref" reference="eq:lipschitz"}. For $A=\alpha I$ and $E=\delta I$ on a $k$-space, both exterior operators are scalar and equality holds.

For $k=4$, write $a=s_1(A)$, $P=s_1s_2s_3s_4$, and $R_4(a,\delta)=(a+\delta)^4-a^4$. Since $s_1(K)\leq a+\delta$, the global certificate is $$\label{eq:global}
 B_{\rm glob}=
 \frac{[P-R_4(a,\delta)]_+}{(a+\delta)^4}.$$

# Weyl domination theorem

The product certificate is $$\label{eq:weyl}
 B_{\rm Weyl}=\frac{\prod_{j=1}^4(s_j-\delta)_+}{(s_1+\delta)^4}.$$

[\[thm:domination\]]{#thm:domination label="thm:domination"} For every nonincreasing nonnegative spectrum and every $\delta\geq0$, $$0\leq B_{\rm glob}\leq B_{\rm Weyl}.$$

If $\delta\geq s_4$, then $P\leq s_1^3\delta$ while $R_4(s_1,\delta)\geq4s_1^3\delta$, so the global numerator is zero. If $\delta<s_4$, telescope the loss produced by replacing each $s_j$ by $s_j-\delta$. Each of the four terms is at most $s_1^3\delta$, hence $$P-\prod_{j=1}^4(s_j-\delta)\leq4s_1^3\delta
 \leq R_4(s_1,\delta).$$ Rearrangement and the common denominator prove the claim.

This theorem is stronger than a data-dependent comparison: it closes the entire norm-only global route.

# Exact tolerance penalty

The global numerator is positive precisely when $$s_1^4\widehat\nu_4>(s_1+\delta)^4-s_1^4.$$ Thus its maximal positive radius is $$\label{eq:radius}
 \delta_{\rm glob}=s_1\bigl((1+\widehat\nu_4)^{1/4}-1\bigr),
 \qquad \delta_{\rm Weyl}=s_4.$$ For small four-volume, $\delta_{\rm glob}=s_1\widehat\nu_4/4+O(\widehat\nu_4^2)$. Because $\widehat\nu_4=(s_2/s_1)(s_3/s_1)(s_4/s_1)$, the global method pays both the three-mode capacity and an additional factor near four.

Sharpness of [\[eq:lipschitz\]](#eq:lipschitz){reference-type="eqref" reference="eq:lipschitz"} does not say every fixed spectrum attains the loss. It says no theorem retaining only $\left\lVert A\right\rVert$ and $\delta$ can uniformly remove it. A better route must preserve a frame, a tail Gramian, or another directional datum.

# Five-scale audit

We reuse the finite-memory packets and outward-rounded tail radii archived in RH-110. The dataset has five scales, two channels, three thresholds, and 360 threshold-labelled records; 234 records lie on the three fine scales. For every record we evaluate [\[eq:global\]](#eq:global){reference-type="eqref" reference="eq:global"}, [\[eq:weyl\]](#eq:weyl){reference-type="eqref" reference="eq:weyl"}, and the two positivity radii in [\[eq:radius\]](#eq:radius){reference-type="eqref" reference="eq:radius"}.

  threshold     fine global support   fine product-Weyl support
  ----------- --------------------- ---------------------------
  $10^{-8}$                      72                          78
  $10^{-6}$                      68                          72
  $10^{-4}$                      55                          55

  : Certified fine updates out of 78 per threshold. Values are filled from the archived audit before release.

There are zero domination failures and zero discrepancies with the archived RH-110 product formula. Figure [1](#fig:audit){reference-type="ref" reference="fig:audit"} shows both the certificate loss and the exact ratio of admissible positive radii.

![Left: product Weyl dominates the global wedge-Lipschitz lower bound on every archived update. Right: the global method tolerates only a fraction of the tail radius admitted by the weak singular mode.](<../../../../../zeta_mvp0/papers/RH-112-global-wedge-lipschitz-barrier/figures/global_wedge_lipschitz_barrier.pdf>){#fig:audit width="\\textwidth"}

# Route consequence and claim boundary

This negative result is constructive. It identifies exactly why the global shortcut fails and which information was discarded. RH-113 should freeze the recent top-four right singular frame and propagate only its four directional images. Such a determinant remains a lower bound for the full exterior norm but no longer charges every error direction at $s_1$.

What is proved is the sharp global wedge law, universal Weyl domination, and the exact positivity radius. What is not proved is a directional wedge bound, an all-level physical four-volume law, uniform Stage A, a Hilbert--Polya operator, identification of zeta zeros, or the Riemann Hypothesis. The phrase "negative result" applies only to the global norm-only branch.
