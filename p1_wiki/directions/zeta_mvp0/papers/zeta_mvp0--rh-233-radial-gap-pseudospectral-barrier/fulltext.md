---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-233-radial-gap-pseudospectral-barrier"
canonical_tex: "zeta_mvp0/papers/RH-233-radial-gap-pseudospectral-barrier/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-233-radial-gap-pseudospectral-barrier/main.pdf"
source_sha256: "8c64fe02d6256d6f7399e2c517b5b55604a643096ef50f87cf9c3b419392f24f"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Why Radial Shell Gaps Do Not Control Nonnormal Riesz Projections

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-233-radial-gap-pseudospectral-barrier>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-233-radial-gap-pseudospectral-barrier/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-233-radial-gap-pseudospectral-barrier/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-233-radial-gap-pseudospectral-barrier/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-233-radial-gap-pseudospectral-barrier/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The shell-complete resonance atlas has positive radial gaps, yet its biorthogonal cloud projectors become extremely ill-conditioned. We prove that there is no contradiction. For $$A_M=\begin{pmatrix}\lambda&M\\0&\mu\end{pmatrix},\qquad \lambda\ne\mu,$$ the spectral projector onto $\lambda$ is $$P_{\lambda,M}=\begin{pmatrix}1&M/(\lambda-\mu)\\0&0\end{pmatrix},$$ so $\left\lVert P_{\lambda,M}\right\rVert_2=\sqrt{1+|M/(\lambda-\mu)|^2}$. The eigenvalue gap is fixed while the projector norm is unbounded.

  In the RH-232 audit the minimum radial shell gap remains $7.40\times10^{-5}$, whereas the maximum projector norm reaches $2.26\times10^{12}$ and the minimum gap-to-projector ratio is $6.40\times10^{-16}$. Log--log fits against the noise give descriptive growth exponents $7.41$ and $6.55$ in the two channels. Radial separation is therefore not a pseudospectral certificate. The result marks a forbidden shortcut but leaves projection-free determinant factorization open.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: Why Radial Shell Gaps Do Not Control Nonnormal Riesz Projections
```

## Markdown 正文

# Spectral separation versus invariant-subspace separation

For normal operators a spectral gap controls the orthogonal spectral projection. For nonnormal operators, eigenvalue location and invariant-space angle are different data [@Kato1995; @TrefethenEmbree2005]. RH-222 recorded the first; RH-232 measured the second [@WangRH222; @WangRH232].

The simplest triangular family already contains the entire obstruction.

# Exact fixed-gap counterexample

[\[thm:fixed-gap\]]{#thm:fixed-gap label="thm:fixed-gap"} Let $\lambda\ne\mu$ and $$A_M=\begin{pmatrix}\lambda&M\\0&\mu\end{pmatrix}.$$ The Riesz projector associated with $\lambda$ is $$P_{\lambda,M}=\frac{A_M-\mu I}{\lambda-\mu}
 =\begin{pmatrix}1&M/(\lambda-\mu)\\0&0\end{pmatrix}.$$ Consequently $$\left\lVert P_{\lambda,M}\right\rVert_2
 =\sqrt{1+\frac{|M|^2}{|\lambda-\mu|^2}}
 \longrightarrow\infty$$ as $|M|\to\infty$, while the eigenvalue gap $|\lambda-\mu|$ is unchanged.

The polynomial formula follows because the minimal polynomial is $(z-\lambda)(z-\mu)$. The displayed projector has only one nonzero row, so its operator norm is the Euclidean norm of that row.

[\[cor:radial\]]{#cor:radial label="cor:radial"} No bound depending only on a positive eigenvalue gap, radial or otherwise, can control the norm of a nonnormal spectral projector.

This statement does not say that gaps are useless. They identify a contour that avoids the spectrum. What they do not control is the resolvent on that contour, and the Riesz formula integrates the resolvent rather than the set of eigenvalues alone.

# The missing datum is a resolvent bound

[\[thm:contour\]]{#thm:contour label="thm:contour"} Let $\Gamma$ be a positively oriented rectifiable contour in the resolvent set of a bounded operator $A$, enclosing an isolated spectral component. Its Riesz projector satisfies $$P_\Gamma=\frac{1}{2\pi i}\int_\Gamma(zI-A)^{-1}\,dz,
 \qquad
 \left\lVert P_\Gamma\right\rVert
 \le \frac{\operatorname{length}(\Gamma)}{2\pi}
       \sup_{z\in\Gamma}\left\lVert(zI-A)^{-1}\right\rVert.$$ Consequently, a uniform contour length and a uniform resolvent bound do give a uniform projector bound; a spectral gap alone supplies neither.

The first identity is the Riesz functional calculus. Taking norms under the Bochner integral gives the second inequality.

For the triangular family the resolvent can be written explicitly: $$(zI-A_M)^{-1}
 =\begin{pmatrix}
 (z-\lambda)^{-1} & M((z-\lambda)(z-\mu))^{-1}\\
 0 & (z-\mu)^{-1}
 \end{pmatrix}.$$ On the circle $|z-\lambda|=r<|\lambda-\mu|$, its norm is at least the modulus of the upper-right entry, and hence at some---indeed every---point obeys $$\left\lVert(zI-A_M)^{-1}\right\rVert
 \ge \frac{|M|}{r(|\lambda-\mu|+r)}.$$ The contour remains a fixed positive distance from both eigenvalues while the resolvent diverges linearly in $|M|$. The same off-diagonal coupling that creates the oblique projector therefore appears as pseudospectral inflation.

If $A=V\Lambda V^{-1}$ is diagonalizable, the elementary estimate $$\left\lVert(zI-A)^{-1}\right\rVert
 \le \frac{\left\lVert V\right\rVert\,\left\lVert V^{-1}\right\rVert}
          {\operatorname{dist}(z,\sigma(A))}$$ shows exactly which datum supplements the spectral gap: a controlled eigenbasis condition number. In infinite-dimensional transfer problems an adapted resolvent estimate is the more invariant formulation.

# Archived dynamical audit

The finite model uses $\lambda=0.8$, $\mu=0.5$, and couplings from $1$ to $10^9$. The gap stays $0.3$ while the projector norm grows by a factor $9.58\times10^8$.

For the RH-232 endpoint family, the projector norms grow much faster than the radial gaps shrink. Representative values are shown below.

     $\sigma$   left $\left\lVert P\right\rVert_2$   right $\left\lVert P\right\rVert_2$        conclusion
  ----------- ------------------------------------ ------------------------------------- -----------------
       $0.04$                     $4.16\times10^1$                      $4.07\times10^1$   already oblique
      $0.008$                     $2.79\times10^5$                      $1.10\times10^6$          unstable
     $0.0032$                     $4.34\times10^9$                      $3.62\times10^9$            severe
    $0.00125$                  $2.26\times10^{12}$                   $5.44\times10^{10}$           extreme

  : Projector norms inherited from RH-232.

The fitted power exponents are diagnostics, not asymptotic theorems: the log residuals are large and the rank changes with the noise. The robust conclusion is only that no bounded trend is visible and radial gaps alone cannot supply one.

# Scope of the negative result

Corollary [\[cor:radial\]](#cor:radial){reference-type="ref" reference="cor:radial"} is a no-go theorem for any argument whose only input is eigenvalue location. It does not prohibit estimates that use positivity, reversibility, a symmetrizing density, analytic distortion, or a semiclassical anisotropic norm. Nor does it prove that the archived projectors actually diverge in the continuum limit: the finite exponents are descriptive and the matrices change dimension with $\sigma$.

The practical distinction is useful. A future positive result must expose where its resolvent control enters; it cannot cite the shell gap as a proxy. Conversely, failure of the Euclidean projector does not contaminate spectral quantities, such as a canonical determinant product, that depend only on algebraic eigenvalues.

# Route consequence

The RH-222 shell gaps remain valid finite spectral observations. What fails is the implication $$\text{positive radial gap}
 \quad\Longrightarrow\quad
 \text{uniformly bounded Riesz projector}.$$ Any operator-level continuation must add a resolvent estimate, an adapted norm, or a different factorization principle. RH-234 uses the canonical eigenvalue product for $\det_2$, which evaluates a finite cloud factor without ever multiplying by the ill-conditioned projector.

This paper does not exclude a certified contour on a different Banach space and does not close Gate A or any later arithmetic gate.
