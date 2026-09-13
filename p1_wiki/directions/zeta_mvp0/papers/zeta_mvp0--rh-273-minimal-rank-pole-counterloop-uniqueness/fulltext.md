---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-273-minimal-rank-pole-counterloop-uniqueness"
canonical_tex: "zeta_mvp0/papers/RH-273-minimal-rank-pole-counterloop-uniqueness/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-273-minimal-rank-pole-counterloop-uniqueness/main.pdf"
source_sha256: "467d40637a040b969e6d9e8108942acc3c772afee3faa3ef3b6d2b6314e8cbbf"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Minimal Rank and Uniqueness of a Pole-Resolving Counterloop

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-273-minimal-rank-pole-counterloop-uniqueness>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-273-minimal-rank-pole-counterloop-uniqueness/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-273-minimal-rank-pole-counterloop-uniqueness/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-273-minimal-rank-pole-counterloop-uniqueness/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-273-minimal-rank-pole-counterloop-uniqueness/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We sharpen the resolution-clocked counterloop of RH-272. In the conjugate- symmetric class with zero odd moments, matching the even pole moments through order $2N$ requires at least $2N$ atoms. At equality the factor is uniquely $\Pi_N((\beta z)^2)$, hence its counterloop atoms are the nontrivial $(2N+2)$-th root directions on the pole circle. This is an algebraic minimality theorem for a graded counterterm, not a theorem about the noisy spectral cloud.
author:
- Bin Wang
date: July 2026
title: 'Minimal Rank and Uniqueness of a Pole-Resolving Counterloop'
```

## Markdown 正文

# Setup

Let $\nu_1,\ldots,\nu_r$ be a finite multiset closed under conjugation and write $S_n=\sum_j\nu_j^n$. For a fixed $\beta>0$, assume $S_{2m+1}=0$ for $0\le m\le N-1$ and $S_{2m}=-2\beta^{2m}$ for $1\le m\le N$.

# Theorem

Under these assumptions $r\ge2N$. If $r=2N$, then $$\prod_{j=1}^{2N}(1-z\nu_j)=\Pi_N((\beta z)^2)$$ and the multiset of counterloop atoms is $\{\beta e^{\pm i j\pi/(N+1)}:1\le j\le N\}$.

Put $F(z)=\prod_{j=1}^r(1-z\nu_j)$. At the origin, $$\log F(z)=-\sum_{n\ge1}\frac{S_n}{n}z^n.$$ The prescribed moments therefore make the Taylor series of $\log F$ agree through degree $2N$ with $$\sum_{m=1}^N\frac{(\beta z)^{2m}}m
 =\log\Pi_N((\beta z)^2)+O(z^{2N+2}).$$ Exponentiation shows that $F$ and $\Pi_N((\beta z)^2)$ have identical coefficients through degree $2N$. The latter has nonzero coefficient $\beta^{2N}$ at degree $2N$, so $r\ge2N$. If $r=2N$, the two polynomials have the same degree and all their coefficients agree, hence they are equal. Factoring the geometric section gives the stated roots.

# Boundary

The theorem explains why the RH-272 rank clock is forced for a pole prefix. It does not provide a spectral selector for $A_\sigma$, and it does not upgrade finite noisy roots to this equality case. Gates A--E remain false/open.
