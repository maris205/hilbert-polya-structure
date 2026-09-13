---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-163-two-sided-schur-packet-riesz-certificate"
canonical_tex: "zeta_mvp0/papers/RH-163-two-sided-schur-packet-riesz-certificate/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-163-two-sided-schur-packet-riesz-certificate/main.pdf"
source_sha256: "46f3a6274ff20261a7be9993cb55eaed6d1cda86f89c6088fda50214914ed5fb"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Two-Sided Schur Certificate for Packet-to-Riesz Lifting Directed Feedback Beyond the Symmetric Neumann Gate

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-163-two-sided-schur-packet-riesz-certificate>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-163-two-sided-schur-packet-riesz-certificate/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-163-two-sided-schur-packet-riesz-certificate/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-163-two-sided-schur-packet-riesz-certificate/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-163-two-sided-schur-packet-riesz-certificate/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-161 certifies a packet-to-Riesz lift from the symmetric condition $M\lVert E\rVert<1$. For an orthogonal packet decomposition the off-diagonal operator has norm $\max(\lVert B\rVert,\lVert C\rVert)$, so this test is governed by the larger directed coupling even when the return coupling is tiny. We prove a strictly sharper Schur-feedback theorem.

  On a separating contour let $a,d$ bound the packet and complement resolvents, and put $b=\lVert B\rVert$, $c=\lVert C\rVert$. If $$\kappa=adbc<1,$$ the contour remains in the resolvent of every off-diagonal homotopy, hence the enclosed Riesz rank equals the packet rank. We give an explicit scalar $2\times2$ bound for the full projector error. The criterion certifies families with $b\to\infty$, $c\to0$, and $bc$ bounded; triangular systems have zero feedback regardless of the surviving coupling. A 512-matrix audit has no bound failures. This is certificate technology: no physical all-level contour or coupling estimate is asserted.
author:
- Prime Dynamics Theory Program
bibliography:
- references.bib
date: July 2026
title: |
  A Two-Sided Schur Certificate for Packet-to-Riesz Lifting\
  Directed Feedback Beyond the Symmetric Neumann Gate
```

## Markdown 正文

# Directed block data

Let $P$ be a finite-rank orthogonal projection, $Q=I-P$, and write $$A=\begin{pmatrix}A_P&B\\ C&A_Q\end{pmatrix},\qquad
 A_t=\begin{pmatrix}A_P&tB\\ tC&A_Q\end{pmatrix},\quad0\le t\le1.$$ Let $\Gamma$ be a positively oriented rectifiable Jordan curve enclosing $\sigma(A_P)$ and excluding $\sigma(A_Q)$. Set $$X(z)=(z-A_P)^{-1},\quad Y(z)=(z-A_Q)^{-1},$$ and assume $$\sup_\Gamma\lVert X\rVert\le a,\qquad
 \sup_\Gamma\lVert Y\rVert\le d,
 \qquad\lVert B\rVert\le b,\quad\lVert C\rVert\le c.$$ The letters $B$ and $C$ are ordered: $C$ sends the packet outward and $B$ returns the complement to the packet. RH-162 shows how primal and adjoint ambient defects can supply these two numbers [@WangRH162].

# Schur-feedback rank preservation

[\[thm:schur\]]{#thm:schur label="thm:schur"} If $\kappa=adbc<1$, then $\Gamma\subset\rho(A_t)$ for every $t\in[0,1]$. The Riesz projection $$\Pi=\frac{1}{2\pi i}\int_\Gamma(z-A)^{-1}\,dz$$ has $\operatorname{rank}\Pi=\operatorname{rank}P$.

For $z\in\Gamma$, eliminate the complementary block. The packet Schur complement is $$S_t(z)=(z-A_P)-t^2BY(z)C
       =(z-A_P)\bigl(I-t^2X(z)BY(z)C\bigr).$$ The second factor is invertible because $\lVert t^2XBYC\rVert\le t^2\kappa<1$. Since $z-A_Q$ is invertible, the block factorization makes $z-A_t$ invertible. The Riesz projections vary continuously with $t$ and have constant finite rank. At $t=0$ the projection is $P$, proving the claim [@Kato1995].

The condition is invariant under reciprocal scalar rescaling of the two blocks. It records the closed feedback loop $P\to Q\to P$, rather than the largest one-way excursion.

# An explicit projector bound

For a scalar matrix $H=(h_{ij})_{i,j=1}^2$, write $\lVert H\rVert_2$ for its Euclidean operator norm.

[\[thm:bound\]]{#thm:bound label="thm:bound"} Under Theorem [\[thm:schur\]](#thm:schur){reference-type="ref" reference="thm:schur"}, for every $z\in\Gamma$, $$\lVert(z-A)^{-1}-(z-A_0)^{-1}\rVert
 \leq\frac1{1-\kappa}
 \left\|
 \begin{pmatrix}
 a\kappa&abd\\ acd&d\kappa
 \end{pmatrix}\right\|_2.$$ Consequently $$\lVert\Pi-P\rVert\leq
 \frac{|\Gamma|}{2\pi(1-\kappa)}
 \left\|
 \begin{pmatrix}
 a\kappa&abd\\ acd&d\kappa
 \end{pmatrix}\right\|_2=:\delta_S.$$ If $\delta_S<1$, the Riesz range is a graph over the packet with slope at most $\delta_S/(1-\delta_S)$.

The Schur inverse formula and the Neumann series give $$\begin{aligned}
 \lVert R_{11}-X\rVert&\le a\kappa/(1-\kappa),&
 \lVert R_{12}\rVert&\le abd/(1-\kappa),\\
 \lVert R_{21}\rVert&\le acd/(1-\kappa),&
 \lVert R_{22}-Y\rVert&\le d\kappa/(1-\kappa).\end{aligned}$$ The norm of an operator block matrix is bounded by the norm of the scalar matrix of block bounds. Contour integration proves the projector estimate. The graph conclusion is the standard close-projection argument used in RH-161 [@WangRH161].

# Strict improvement and exact limiting cases

The symmetric RH-161 condition, with the exact off-diagonal norm, is $$\max(a,d)\max(b,c)<1.$$ Take $a=d=1$, $b=L$, and $c=\theta/L$ with $0<\theta<1$. Then the Schur product is $\kappa=\theta$ for every $L$, while the symmetric product equals $\max(L,\theta/L)$ and diverges. Thus the improvement is unbounded.

If $C=0$, the packet is invariant and the block matrix is upper triangular. The feedback product is zero, so Theorem [\[thm:schur\]](#thm:schur){reference-type="ref" reference="thm:schur"} preserves the packet spectrum for arbitrary $B$. The Riesz projection may be highly oblique, and the projector bound correctly still contains $abd$. Rank preservation and graph conditioning are different conclusions.

# Pointwise sharpness of the feedback threshold

The constant one in the Schur test cannot be improved from norm data alone. Consider scalar blocks at a fixed contour point $z_0$: $$z_0-A=
 \begin{pmatrix}x^{-1}&-b\\-c&y^{-1}\end{pmatrix},
 \qquad |x|=a,\quad |y|=d.$$

For phases chosen so that $xybc=1$, the point $z_0$ belongs to $\sigma(A)$. Hence the non-strict condition $adbc\le1$ cannot certify a resolvent contour uniformly over the displayed norm class.

The determinant of $z_0-A$ equals $x^{-1}y^{-1}-bc$. It vanishes when $xybc=1$. Phases of the scalar couplings can always realize the equality whenever $adbc=1$.

This witness is local: a physical certificate needs a strict margin at every point of the contour. An average value of $adbc$, or a favorable value on a dense but uncertified mesh, does not exclude a single threshold contact. It also explains why the finite-mesh denominator developed later must be strictly below one.

# Audit and boundary

The companion calculation samples 512 finite block systems. It synthesizes block resolvents $X,Y$, forms the exact full inverse, and compares its difference from $X\oplus Y$ with the scalar envelope of Theorem [\[thm:bound\]](#thm:bound){reference-type="ref" reference="thm:bound"}. Every accepted sample satisfies the bound. The audit is a regression test, not validated prime-dynamics data.

RH-163 proves that the first rank gate inside physical interface R should be tested with $adbc$, not a symmetric maximum. It does not provide the ambient realization, the contour, any of the four physical bounds, a uniform scale margin, the complementary Schatten limit, Gate A, or any Hilbert--Polya or zeta conclusion.
