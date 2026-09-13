---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-169-common-coordinate-riesz-transport"
canonical_tex: "zeta_mvp0/papers/RH-169-common-coordinate-riesz-transport/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-169-common-coordinate-riesz-transport/main.pdf"
source_sha256: "3aa783cb2a8e9d9c091f55bbcc095c83b0edffa8a8b0704c5164ec67513406fb"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Common-Coordinate Transport of Riesz Clouds Summable Resolvent Defects and Fixed-Rank Limits

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-169-common-coordinate-riesz-transport>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-169-common-coordinate-riesz-transport/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-169-common-coordinate-riesz-transport/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-169-common-coordinate-riesz-transport/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-169-common-coordinate-riesz-transport/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-162--168 give fixed-scale packet-to-Riesz certificates. An all-level interface also needs a coherent comparison of Riesz clouds living at different mesh and noise scales. After embedding two consecutive operators in a common Hilbert space, we prove $$\lVert\Pi_{j+1}-\Pi_j\rVert
   \le\frac{|\Gamma|}{2\pi}M_{j+1}M_j
   \lVert A_{j+1}-A_j\rVert,$$ where one contour $\Gamma$ lies in both resolvent sets and $M_j$ are its resolvent bounds. A step bound below one yields an invertible range transport with explicit inverse norm. If the step bounds are summable, the Riesz projections converge in operator norm to an idempotent of the same finite rank. A 512-pair Hermitian audit has no inequality failure. The theorem is restricted to fixed rank; a moving determinant cloud has growing rank and requires the shellwise correction developed next.
author:
- Prime Dynamics Theory Program
bibliography:
- references.bib
date: July 2026
title: |
  Common-Coordinate Transport of Riesz Clouds\
  Summable Resolvent Defects and Fixed-Rank Limits
```

## Markdown 正文

# The common-coordinate input

Operators at different Ulam dimensions cannot be subtracted until maps into one ambient space have been chosen. Let $\mathcal H_j$ be the scale spaces, let $J_j:\mathcal H_j\to\mathcal K$ be isometries, and suppose extensions $\widetilde A_j\in\mathcal B(\mathcal K)$ have been specified. Their action outside $J_j\mathcal H_j$ is part of the construction; arbitrary zero extension can introduce spurious spectrum on a contour.

For the theorem, write $A_j$ for these common-space operators. Let one rectifiable Jordan curve $\Gamma$ satisfy $$\Gamma\subset\rho(A_j)\cap\rho(A_{j+1}),\qquad
 \sup_\Gamma\lVert(z-A_j)^{-1}\rVert\le M_j.$$ Define $$\Pi_j=\frac1{2\pi i}\int_\Gamma(z-A_j)^{-1}\,dz.$$

# Consecutive transport theorem

[\[thm:step\]]{#thm:step label="thm:step"} If $\lVert A_{j+1}-A_j\rVert\le\eta_j$, then $$\boxed{
 \lVert\Pi_{j+1}-\Pi_j\rVert
 \le \beta_j:=\frac{|\Gamma|}{2\pi}M_{j+1}M_j\eta_j.
 \ }$$

The resolvent identity gives $$(z-A_{j+1})^{-1}-(z-A_j)^{-1}
 =(z-A_{j+1})^{-1}(A_{j+1}-A_j)(z-A_j)^{-1}.$$ Integrate around $\Gamma$ and take norms [@Kato1995].

[\[cor:range\]]{#cor:range label="cor:range"} Suppose $\Pi_j$ and $\Pi_{j+1}$ have equal finite rank and $\beta_j<1$. Then $$\Pi_{j+1}|_{\operatorname{ran}\Pi_j}:
 \operatorname{ran}\Pi_j\longrightarrow\operatorname{ran}\Pi_{j+1}$$ is invertible, and its inverse norm is at most $(1-\beta_j)^{-1}$.

For $x\in\operatorname{ran}\Pi_j$, $$\lVert\Pi_{j+1}x\rVert\ge
 \lVert x\rVert-\lVert(\Pi_{j+1}-\Pi_j)x\rVert
 \ge(1-\beta_j)\lVert x\rVert.$$ Thus the map is injective; equal finite dimensions give surjectivity and the inverse bound.

# Summable fixed-rank limit

[\[thm:sum\]]{#thm:sum label="thm:sum"} Assume the same finite rank $r$ is enclosed at every scale and $$\sum_{j=1}^{\infty}\beta_j<\infty.$$ Then $\Pi_j$ converges in operator norm to a bounded idempotent $\Pi_\infty$ of rank $r$. The tail obeys $$\lVert\Pi_\infty-\Pi_n\rVert\le\sum_{j=n}^{\infty}\beta_j.$$

The telescoping inequality makes $(\Pi_j)$ norm-Cauchy. Completeness of $\mathcal B(\mathcal K)$ gives a limit, and multiplication is norm continuous, so $\Pi_\infty^2=\Pi_\infty$. For sufficiently large $j$, $\lVert\Pi_j-\Pi_\infty\rVert<1$; the close-projection restriction argument gives equal rank. The tail estimate follows from telescoping.

Summability is stronger than $\eta_j\to0$. Resolvent conditioning can grow fast enough that $M_jM_{j+1}\eta_j$ is not summable even when operators look close entrywise. This is the all-level analogue of the fixed-scale pseudospectral wall.

# Moving contours and homotopy compatibility

Consecutive physical shells may use different contours. They can be compared by Theorem [\[thm:step\]](#thm:step){reference-type="ref" reference="thm:step"} only after a common representative is chosen.

Let $\Gamma_0$ and $\Gamma_1$ be homologous closed contours in one connected open subset of $\rho(A)$, enclosing the same spectral component. Then their Riesz integrals are equal. Consequently, if both consecutive operators are resolvent-free throughout a common deformation corridor, either boundary may be used in the transport estimate.

The operator-valued resolvent is holomorphic on the corridor. Cauchy's theorem makes the two contour integrals equal [@Kato1995].

This adds a concrete schedule obligation. Merely labeling two independently chosen clouds by the same shell index does not prove they enclose the same spectral component; a joint resolvent corridor or an equivalent coefficient identification is required before telescoping.

# Vanishing steps are not enough

The summability hypothesis in Theorem [\[thm:sum\]](#thm:sum){reference-type="ref" reference="thm:sum"} cannot be replaced by $\beta_j\to0$ in this proof architecture.

There is a sequence of rank-one orthogonal projections on $\mathbb C^2$ such that $$\lVert P_{j+1}-P_j\rVert\longrightarrow0$$ but $(P_j)$ does not converge.

Let $$\theta_j=\sum_{k=1}^{j}\frac1k,qquad
 u_j=(\cos\theta_j,\sin\theta_j),\qquad P_j=u_ju_j^*.$$ Then $\lVert P_{j+1}-P_j\rVert=|\sin(1/(j+1))|\to0$. The angle $\theta_j$ keeps traversing the projective circle because its increments tend to zero while their sum diverges. Hence the ranges visit separated angular sectors infinitely often and do not converge.

Taking $A_j=P_j$, a fixed circle around the eigenvalue one gives uniformly bounded resolvents and Riesz projection $P_j$. Thus even an exact uniformly gapped spectral model can drift forever when the common-coordinate defects are nonsummable.

# Conditioning of the composed range transport

Let $$L_j=\Pi_{j+1}|_{\operatorname{ran}\Pi_j}$$ be the step maps from Corollary [\[cor:range\]](#cor:range){reference-type="ref" reference="cor:range"}. Their composition transports one initial cloud frame through the chain without making a new gauge choice at every scale.

If $\beta_j\le\beta_*<1$ and $\sum_j\beta_j<\infty$, then $$\prod_j\lVert L_j^{-1}\rVert
 \le\prod_j(1-\beta_j)^{-1}<\infty.$$ More explicitly, $$\log\prod_{j=n}^{N}(1-\beta_j)^{-1}
 \le\frac1{1-\beta_*}\sum_{j=n}^{N}\beta_j.$$

Corollary [\[cor:range\]](#cor:range){reference-type="ref" reference="cor:range"} gives the first finite-product inequality. For $0\le x\le\beta_*$, $-\log(1-x)\le x/(1-\beta_*)$. Sum this scalar inequality and exponentiate.

Thus the same summability that yields a projector limit also prevents the canonical stepwise coordinates from acquiring infinite inverse condition. This is stronger information than pairwise rank agreement and is relevant when shell coefficients or marked vectors must be transported coherently.

# Audit and boundary

The finite audit rotates a three-dimensional spectral packet inside eight- dimensional Hermitian matrices while keeping a unit-circle spectral gap. It evaluates the exact normal resolvent bound, the operator defect, and the projector distance for 512 pairs. No distance exceeds Theorem [\[thm:step\]](#thm:step){reference-type="ref" reference="thm:step"}'s envelope.

RH-169 proves the correct fixed-rank common-coordinate theorem. It does not construct the physical embeddings or extensions, prove summability, or handle the increasing degree of the RH-80 cloud. Therefore physical R, Gate A, and all later Hilbert--Polya interfaces remain open.
