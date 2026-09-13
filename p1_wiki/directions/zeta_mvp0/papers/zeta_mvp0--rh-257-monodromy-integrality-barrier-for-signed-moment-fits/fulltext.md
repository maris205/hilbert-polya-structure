---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-257-monodromy-integrality-barrier-for-signed-moment-fits"
canonical_tex: "zeta_mvp0/papers/RH-257-monodromy-integrality-barrier-for-signed-moment-fits/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-257-monodromy-integrality-barrier-for-signed-moment-fits/main.pdf"
source_sha256: "51afa566ebd5506f546b2cedc402a2951ac23487a59216f147d79cb3458dbba8"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Monodromy Integrality Barrier for Signed Moment Fits

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-257-monodromy-integrality-barrier-for-signed-moment-fits>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-257-monodromy-integrality-barrier-for-signed-moment-fits/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-257-monodromy-integrality-barrier-for-signed-moment-fits/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-257-monodromy-integrality-barrier-for-signed-moment-fits/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-257-monodromy-integrality-barrier-for-signed-moment-fits/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  After idempotent polynomial selectors collapse to binary masks, one may try arbitrary signed shell weights. On the expanded RH-254 windows, minimum-norm real weights fit the order-$2$--$12$ anchor tolerance at all 32 endpoints. Every fit is fractional, however, and maximum weights range from $39.64$ to $3.02\times10^{11}$. We prove that the weighted moment germ equals $\prod_j(1-\lambda_jz)^{w_j}$ near zero and has monodromy $e^{2\pi i w_j}$ around $\lambda_j^{-1}$. Integer combined exponents are therefore necessary for a single-valued meromorphic determinant quotient. The 32 continuous signed fits are finite compressions, not legal selectors.
author:
- Bin Wang
bibliography:
- references.bib
date: July 2026
title: Monodromy Integrality Barrier for Signed Moment Fits
```

## Markdown 正文

# Weighted moment germs

Let $\lambda_1,\dots,\lambda_J$ be distinct nonzero complex numbers and let $w_j\in\mathbb C$. Define the local logarithmic moment germ $$\mathcal F_w(z)=\exp\left[-\sum_{n\ge1}\frac{z^n}{n}
 \sum_{j=1}^Jw_j\lambda_j^n\right]
 \label{eq:germ}$$ for $|z|<\min_j|\lambda_j|^{-1}$.

[\[thm:monodromy\]]{#thm:monodromy label="thm:monodromy"} On the initial disk, $$\mathcal F_w(z)=\prod_{j=1}^J(1-\lambda_jz)^{w_j}.
 \label{eq:product}$$ Analytic continuation once around $z=\lambda_j^{-1}$ multiplies the germ by $e^{2\pi i w_j}$. Hence $\mathcal F_w$ is single-valued meromorphic near all reciprocal roots if and only if every combined exponent at a repeated root is an integer.

The power-series identity $-\sum_{n\ge1}(\lambda z)^n/n=\log(1-\lambda z)$ proves [\[eq:product\]](#eq:product){reference-type="eqref" reference="eq:product"} on the initial disk. Continuing the logarithm once around its zero changes it by $2\pi i$; exponentiation therefore produces the stated factor. Trivial monodromy is equivalent to $e^{2\pi iw_j}=1$, or $w_j\in\mathbb Z$. Integer powers are rational meromorphic factors, proving the converse.

Integer weights are necessary for a determinant ratio, but an operator realization also requires the corresponding algebraic multiplicities and invariant spaces. Negative integers describe denominator or superdeterminant contributions; they are not automatically present in the noisy operator.

# Expanded-window signed fit

At each endpoint let $V$ be the real order-$2$--$12$ shell-power matrix and $d$ the difference between the Perron/parity-removed trace and deterministic anchor. We solve the unconstrained minimum-norm problem $$\min\{\|w\|_2:Vw\ \text{is the least-squares approximation to }d\}.
 \label{eq:lstsq}$$ This is deliberately more permissive than the RH-255 box [@WangRH255].

  quantity                                                      value
  ---------------------------------- --------------------------------
  endpoints within local tolerance                              32/32
  full row-rank systems                                         28/32
  weighted residual range              $2.15\times10^{-15}$--0.003783
  fractional weights per endpoint                              20--34
  maximum absolute weight range            39.64--$3.02\times10^{11}$
  integer-weight fits                                            0/32
  maximum monodromy defect                               1.9999999996

The four rank-deficient systems still meet their comparatively larger local tolerances. The smallest singular value across the batch is $2.71\times10^{-19}$, which helps explain the coefficient explosion. The fit is therefore both nonintegral and numerically ill-conditioned.

None of the 32 least-norm signed fits defines a single-valued finite determinant quotient with the fitted shell exponents.

Every fitted vector contains at least 20 weights farther than $10^{-8}$ from the integer lattice. Apply Theorem [\[thm:monodromy\]](#thm:monodromy){reference-type="ref" reference="thm:monodromy"}.

# Boundary and next route

This result does not exclude a bounded integer signed selector or a non-product quotient-kernel cancellation. It does exclude the inference "finite signed fit implies determinant selector." RH-258 should audit a small integer lattice and then separately ask for an operator realization. Gates A--E remain false/open. No Hilbert--Polya operator, Riemann-zero identification, zeta-divisor equality, or RH implication is claimed.
