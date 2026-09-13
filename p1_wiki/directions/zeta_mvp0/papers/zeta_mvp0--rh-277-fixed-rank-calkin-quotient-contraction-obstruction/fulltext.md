---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-277-fixed-rank-calkin-quotient-contraction-obstruction"
canonical_tex: "zeta_mvp0/papers/RH-277-fixed-rank-calkin-quotient-contraction-obstruction/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-277-fixed-rank-calkin-quotient-contraction-obstruction/main.pdf"
source_sha256: "0e48f7e3c186eff8fe38b8fec3359b2dafea193aaf42300dd081cb654edc7c98"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Fixed-Rank Calkin Obstruction to Zero-Noise Quotient Contraction

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-277-fixed-rank-calkin-quotient-contraction-obstruction>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-277-fixed-rank-calkin-quotient-contraction-obstruction/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-277-fixed-rank-calkin-quotient-contraction-obstruction/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-277-fixed-rank-calkin-quotient-contraction-obstruction/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-277-fixed-rank-calkin-quotient-contraction-obstruction/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-269 asks for a contractive power of a limiting orthogonal quotient. We show that this cannot occur at the deterministic zero-noise endpoint under any fixed-rank removal in the natural stationary $L^2$ geometry. The deterministic Koopman limit is an isometry on an infinite-dimensional Perron/parity complement, and finite-rank compression leaves its Calkin class unchanged. After Hardy scaling every quotient power has norm at least $r_H^{-m}>1$. Rank-growing selectors and growing block depths are not excluded.
author:
- Bin Wang
date: July 2026
title: 'A Fixed-Rank Calkin Obstruction to Zero-Noise Quotient Contraction'
```

## Markdown 正文

# Calkin theorem

Let $U_0$ be the deterministic Koopman isometry on the invariant complement of the constant and component-sign functions. Let $P$ be any finite-rank orthogonal projection and $Q=I-P$.

For every $m\ge1$, $$\|(QU_0Q)^m\|\ge1,
 \qquad
 \|\{r_H^{-1}QU_0Q\}^m\|\ge r_H^{-m}>1.$$ Thus no fixed-rank limiting quotient in this geometry has a contractive power after Hardy scaling.

In the Calkin algebra finite-rank operators vanish, so $[QU_0Q]=[U_0]$. Since $U_0^*U_0=I$, the class $[U_0]$ is an isometry and $\|[U_0]^m\|=1$. The quotient norm is bounded above by the operator norm, which gives the first inequality. Scalar Hardy scaling gives the second.

# Rank firewall

A common isolating contour in the RH-269 setting gives norm-continuous Riesz projections and hence a locally constant finite rank. The RH-222 frozen cloud ranks, including Perron and parity, run from $6$ to $37$. Therefore a single fixed-rank contour cannot encode that rank-growing atlas. This is a logical rank mismatch, not a continuum theorem about the stored roots.

The theorem does not exclude $P=P_\sigma$ with rank tending to infinity, $m=m(\sigma)\to\infty$, or an anisotropic space whose zero-noise limit is not the stationary Koopman isometry.

# Boundary

Together with RH-276, the result closes the raw fixed-rank zero-noise $\mathcal S_2$/contraction branch. It does not close the rank-growing trace route, Gate A, or any later Gate.
