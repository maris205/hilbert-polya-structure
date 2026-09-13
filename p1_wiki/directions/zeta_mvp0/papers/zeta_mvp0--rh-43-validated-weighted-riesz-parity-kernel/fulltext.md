---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-43-validated-weighted-riesz-parity-kernel"
canonical_tex: "zeta_mvp0/papers/RH-43-validated-weighted-riesz-parity-kernel/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-43-validated-weighted-riesz-parity-kernel/validated-weighted-riesz-parity-kernel.pdf"
source_sha256: "b431a2362088b58179712387c08d31512f290649dd34a4aeb0b43fc8111ed179"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Validated Intrinsic Kernel for a Negative Parity Resonance Weighted-Riesz Factor Correction, Complement Schur Closure, and Adaptive Spectral Deflation

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-43-validated-weighted-riesz-parity-kernel>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-43-validated-weighted-riesz-parity-kernel/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-43-validated-weighted-riesz-parity-kernel/validated-weighted-riesz-parity-kernel.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-43-validated-weighted-riesz-parity-kernel/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-43-validated-weighted-riesz-parity-kernel/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The negative resonance of a folded-Gaussian Markov operator at the first quadratic band-merging parameter has been isolated in both $L^\infty$ and $L^2$, with a dimension-uniform Euclidean contour for full and sparse midpoint matrices. The remaining task in the gauge-free peripheral program is to turn that isolated eigenvalue into a validated intrinsic kernel that can be subtracted before trace and determinant analysis. We carry this out at fixed noise $\sigma=10^{-2}$.

  For the parity circle $$c=-0.9865481927458079,\qquad r=0.05,$$ we define $$\mathcal Q_-(T;\Gamma)
   =\frac{1}{2\pi i}\int_\Gamma z(z-T)^{-1}\,dz.$$ An orthogonal Schur decomposition against the full cell-average complement improves the continuum $L^2$ resolvent upper from $266.650$ to $112.95503061584434$. The weighted term $\mathcal Q_-(\mathcal K;\Gamma)$ is rank one and has a real smooth Hilbert--Schmidt kernel $q_-(x,y)$. We give explicit Hilbert--Schmidt bounds for $q_-$ and its derivatives through $\partial_x^2\partial_y^2q_-$, and enclose it in an $L^2([0,1]^2)$ ball of radius $2.427176139794529$ about the lifted archived $4096$ factor.

  A new two-sided residual theorem converts an approximate left--right factor into an exact weighted-Riesz certificate by a block-diagonalizing perturbation. Applied with componentwise outward arithmetic, it proves that the stored parity factors at dimensions $2048$, $4096$, and $8192$ are genuine spectral terms, with Euclidean errors at most $3.66\times10^{-10}$, $7.21\times10^{-10}$, and $1.43\times10^{-9}$. Consequently the two archived Haar transitions are now spectral, not merely algebraic: their actual ratios lie within $3.94\times10^{-4}$ of the quarter--half targets. A smooth-kernel Haar theorem explains these limits intrinsically.

  The improved continuum bound yields an all-dimension theorem from $n=65536$: full and fixed/adaptive sparse exact-real Markov matrices have one parity eigenvalue in the circle and uniform Euclidean resolvent upper $267.81252084743886$. Their full-to-sparse weighted-Riesz difference is at most $7.275887086007192\times10^{-10}$, while the corresponding intrinsically deflated operators differ by at most $7.277844418892396\times10^{-10}$. The full weighted term converges to the midpoint sample of $q_-$ at order $n^{-2}$, and adaptive support preserves the rate $O(n^{-2}(\log n)^{-1/4})$. No Perron rank-two completion, zero-noise limit, arithmetic trace formula, zeta-zero identification, self-adjoint Hilbert--Pólya operator, or Riemann-hypothesis claim is made.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  A Validated Intrinsic Kernel for a Negative Parity Resonance\
  Weighted-Riesz Factor Correction, Complement Schur Closure,\
  and Adaptive Spectral Deflation
```

## Markdown 正文

# Introduction {#sec:introduction}

Spectral subtraction is straightforward for a normal matrix with an orthonormal eigenbasis: one removes the relevant eigenvalue times its orthogonal projector. The noisy quadratic transfer operators studied here are nonnormal. Their left and right modes carry arbitrary scale, sign, and ordering conventions, and those conventions become increasingly fragile under grid refinement. The invariant object is instead the weighted Riesz term $$\mathcal Q(T;\Gamma)=T\mathcal P(T;\Gamma)
 =\frac{1}{2\pi i}\int_\Gamma z(z-T)^{-1}\,dz,$$ where $\mathcal P$ is the Riesz projection. For a simple real eigenvalue $\lambda$ this equals $\lambda r\ell^T/(\ell^Tr)$, but the contour formula does not choose a gauge.

The analytic weighted-Riesz framework of @WangRiesz2026 proved that a simple isolated smooth Nyström branch has a second-order intrinsic continuum bridge. It also showed that an adaptive Gaussian support cutoff passes through the same calculus under a dimension-uniform Euclidean contour bound. At that stage three statements were still conditional: the negative continuum resonance had not been proved simple and isolated, the required Euclidean conditioning was absent, and the stored factors used in the Haar ledger were known to be spectral only through floating residuals.

The first two conditions were subsequently closed. A validated continuum Grushin--Rouché argument isolated one real negative resonance [@WangContinuumContour2026]; a Hilbert--Galerkin lift then established the same circle in $L^2$ and controlled every sufficiently fine full and sparse midpoint family in the Euclidean norm [@WangEuclidean2026]. The present paper uses those results rather than opening another contour. Its purpose is to construct the intrinsic parity kernel itself and to close the exact-stored factor gate.

Four additional ideas are needed.

1.  A two-sided residual correction makes a chosen rank-one factor exact for a nearby matrix, after which contour stability compares it with the true weighted Riesz term.

2.  The dyadic Schur formulas can be integrated around the contour. This bounds the change of the weighted term block by block, much more sharply than a direct perturbation by the whole fine operator.

3.  The final finite-rank-to-continuum passage should also be Schur, with the full orthogonal complement as the detail space. Its self-energy is quadratic in the mesh and is far smaller than the direct Galerkin defect.

4.  The quarter--half law has a continuum explanation. Four midpoint samples in a coarse cell give leading tensors $q_{xx}+q_{yy}$, $q_x$, $q_y$, and $q_{xy}$ in the four Haar blocks.

These steps produce an intrinsic deflation $$\mathcal K_\perp=\mathcal K-\mathcal Q_-(\mathcal K;\Gamma)$$ that removes the negative branch exactly while leaving the remaining spectrum unchanged away from zero. This is the operator that later trace and determinant papers can use without carrying a left--right gauge.

Three evidence levels remain separate throughout.

Analytic theorem

:   Two-sided factor correction, weighted contour stability, infinite complement Schur continuation, smooth-kernel Haar limits, Nyström convergence, and intrinsic deflation.

Outward certificate

:   Exact stored binary64 bordered residuals, Arb Frobenius identities, the Hilbert derivative envelope, and every explicit Neumann or Schur gate.

Displayed center

:   The heat map in [1](#fig:summary){reference-type="ref" reference="fig:summary"} is the exact archived $4096$ factor center. It is not a pointwise interval enclosure of the continuum kernel.

# Operator, contour, and main results {#sec:model}

Let $u_{\mathrm c}$ be the unique root in $(1.5,1.6)$ of $$u^3-2u^2+2u-2=0,$$ fix $\sigma=1/100$, and put $$m(x)=1-u_{\mathrm c}x^2.$$ For $0\le x,y\le1$, define $$g(x,y)=
 e^{-(y-m(x))^2/(2\sigma^2)}
 +e^{-(y+m(x))^2/(2\sigma^2)},$$ $$Z(x)=\int_0^1g(x,y)\,dy,
 \qquad
 k(x,y)=\frac{g(x,y)}{Z(x)},$$ and the compact Markov operator $$(\mathcal Kf)(x)=\int_0^1k(x,y)f(y)\,dy
 \quad\text{on }L^2([0,1]).
 \label{eq:continuum-operator}$$

The parity contour is $$c=-0.9865481927458079,
 \qquad r=0.05,
 \qquad \Gamma=\{z\in\mathbb C:|z-c|=r\}.
 \label{eq:contour}$$ Write $$\rho_\Gamma=0.9365481927458077,
 \qquad R_\Gamma=1.036548192745808.$$ For any bounded operator $T$ with $\Gamma\subset\rho(T)$, define $$\begin{aligned}
 \mathcal P_-(T;\Gamma)
 &=\frac{1}{2\pi i}\int_\Gamma(z-T)^{-1}\,dz,
 \label{eq:riesz-projection}\\
 \mathcal Q_-(T;\Gamma)
 &=\frac{1}{2\pi i}\int_\Gamma z(z-T)^{-1}\,dz
 =T\mathcal P_-(T;\Gamma).
 \label{eq:weighted-riesz}\end{aligned}$$

For $n\ge2$, let $h=1/n$ and $x_i=y_i=(i+\tfrac12)h$. The continuum- normalized midpoint matrix and exactly discretely normalized Markov matrix are $$(M_n)_{ij}=h k(x_i,y_j),
 \qquad
 (P_n)_{ij}=\frac{g(x_i,y_j)}{\sum_qg(x_i,y_q)}.
 \label{eq:matrix-families}$$ Let $P_n^{(8)}$ be the archived fixed eight-sigma truncation and let $$L_n=\max\{8,2\sqrt{\log n}\}
 \label{eq:adaptive-schedule}$$ define the adaptive sparse family $P_n^{(L_n)}$ as in @WangCutoff2026 [@WangEuclidean2026].

[\[thm:continuum-kernel\]]{#thm:continuum-kernel label="thm:continuum-kernel"} The circle [\[eq:contour\]](#eq:contour){reference-type="eqref" reference="eq:contour"} lies in the $L^2$ resolvent set of $\mathcal K$ and $$\sup_{z\in\Gamma}\left\lVert (z-\mathcal K)^{-1}\right\rVert_{2\to2}
 \le112.95503061584434.
 \label{eq:improved-continuum-resolvent}$$ The operator $$Q_-=\mathcal Q_-(\mathcal K;\Gamma)$$ has rank one and a real $C^\infty$ kernel $q_-(x,y)$. Its Hilbert--Schmidt norm lies in $$0.9365481927458077
 \le\left\lVert q_-\right\rVert_{L^2([0,1]^2)}
 \le5.854166642320046.$$ The derivative uppers are recorded in [3](#tab:kernel-envelope){reference-type="ref" reference="tab:kernel-envelope"}.

Let $\widehat Q_{4096}$ be the stored binary64 factor $$\widehat Q_{4096}
 =c\,\frac{r_0\ell_0^T}{\ell_0^Tr_0}$$ lifted to the cell space $V_{4096}$. Then $$\begin{aligned}
 \left\lVert Q_- -\widehat Q_{4096}\right\rVert_{2\to2}
 &\le1.716272707582898,
 \label{eq:construction-operator-ball}\\
 \left\lVert q_- -\widehat q_{4096}\right\rVert_{L^2([0,1]^2)}
 &\le2.427176139794529.
 \label{eq:construction-kernel-ball}\end{aligned}$$ Thus the continuum weighted term is a validated intrinsic kernel, not only an eigenvalue count.

[\[thm:stored-factors\]]{#thm:stored-factors label="thm:stored-factors"} For each $n\in\{2048,4096,8192\}$, let $A_n^{\mathrm s}$ be the exact stored binary64 Markov matrix, let $c_n,r_n,\ell_n$ be its archived parity data, and put $$\widehat Q_n=c_n\frac{r_n\ell_n^T}{\ell_n^Tr_n}.$$ The circle $|z-c_n|=0.05$ contains exactly one eigenvalue of $A_n^{\mathrm s}$. Its true weighted Riesz term $Q_n^{\mathrm s}$ obeys $$\left\lVert Q_n^{\mathrm s}-\widehat Q_n\right\rVert_2
 \le
 \begin{cases}
  3.650836314181483\times10^{-10},&n=2048,\\
  7.202868434316492\times10^{-10},&n=4096,\\
  1.426439999332510\times10^{-9},&n=8192.
 \end{cases}$$ Consequently the actual spectral Haar ratios satisfy the intervals in [2](#tab:haar-ratios){reference-type="ref" reference="tab:haar-ratios"}. Every interval is within $10^{-3}$ of its smooth- kernel quarter--half target.

[\[thm:uniform-family\]]{#thm:uniform-family label="thm:uniform-family"} For every integer $n\ge65536$, each of $$M_n,\qquad P_n,\qquad P_n^{(8)},\qquad P_n^{(L_n)}$$ has exactly one eigenvalue inside $\Gamma$, counted algebraically. It is real, negative, and simple. Uniformly in $n$, $$\begin{aligned}
 \sup_{z\in\Gamma}\left\lVert (z-M_n)^{-1}\right\rVert_2
 &\le267.3688881197896,
 \label{eq:uniform-midpoint-resolvent}\\
 \sup_{z\in\Gamma}\left\lVert (z-P_n)^{-1}\right\rVert_2
 &\le267.8125208334001,
 \label{eq:uniform-full-resolvent}\\
 \sup_{z\in\Gamma}\left\lVert (z-P_n^{(8)})^{-1}\right\rVert_2,quad
 \sup_{z\in\Gamma}\left\lVert (z-P_n^{(L_n)})^{-1}\right\rVert_2
 &\le267.81252084743886.
 \label{eq:uniform-sparse-resolvent}\end{aligned}$$ Moreover, $$\left\lVert \mathcal Q_-(P_n^{(8)};\Gamma)-\mathcal Q_-(P_n;\Gamma)\right\rVert_2,
 \quad
 \left\lVert \mathcal Q_-(P_n^{(L_n)};\Gamma)-\mathcal Q_-(P_n;\Gamma)\right\rVert_2
 \le7.275887086007192\times10^{-10}.
 \label{eq:uniform-weighted-cutoff}$$ Define the intrinsic deflations $$P_{n,\perp}=P_n-\mathcal Q_-(P_n;\Gamma),
 \qquad
 P_{n,\perp}^{(L)}
 =P_n^{(L)}-\mathcal Q_-(P_n^{(L)};\Gamma).$$ Then $$\left\lVert P_{n,\perp}^{(8)}-P_{n,\perp}\right\rVert_2,
 \quad
 \left\lVert P_{n,\perp}^{(L_n)}-P_{n,\perp}\right\rVert_2
 \le7.277844418892396\times10^{-10}.
 \label{eq:uniform-deflated-cutoff}$$

[\[cor:weighted-bridge\]]{#cor:weighted-bridge label="cor:weighted-bridge"} Let $$(Q_n^\circ)_{ij}=h q_-(x_i,y_j).$$ Then $$\begin{aligned}
 \left\lVert \mathcal Q_-(P_n;\Gamma)-Q_n^\circ\right\rVert_2
 &=O(n^{-2}),
 \label{eq:full-second-order}\\
 \left\lVert \mathcal Q_-(P_n^{(L_n)};\Gamma)-Q_n^\circ\right\rVert_2
 &=O\!\left(n^{-2}(\log n)^{-1/4}\right).
 \label{eq:adaptive-second-order}\end{aligned}$$ Thus every hypothesis of the conditional parity theorem in @WangRiesz2026 is now proved. No eigenvector gauge appears in either statement.

# Two-sided residual correction of a weighted factor {#sec:factor-correction}

The first new ingredient closes the gap between a stored low-rank factor and the actual spectral term of the stored matrix. It is purely algebraic and applies to any nonnormal matrix.

[\[prop:factor-correction\]]{#prop:factor-correction label="prop:factor-correction"} Let $A\in\mathbb C^{n\times n}$ and let $\lambda_0\in\mathbb C$. Choose nonzero vectors $r_0,\ell_0$ with $$g=\ell_0^Tr_0\ne0,
 \qquad
 P_0=\frac{r_0\ell_0^T}{g}.$$ Put $R_0=A-\lambda_0\mathrm I$ and $$\Delta=-R_0P_0-P_0R_0+P_0R_0P_0.
 \label{eq:block-correction}$$ Then $$\widetilde A=A+\Delta
 =\lambda_0P_0+(\mathrm I-P_0)A(\mathrm I-P_0),
 \label{eq:corrected-matrix}$$ and $$\widetilde AP_0=P_0\widetilde A=\lambda_0P_0.$$ If $$u=R_0r_0,
 \qquad
 v^T=\ell_0^TR_0,
 \qquad
 p=\frac{\left\lVert r_0\right\rVert_2\left\lVert \ell_0\right\rVert_2}{|g|},$$ then $$\left\lVert \Delta\right\rVert_2
 \le
 \frac{\left\lVert u\right\rVert_2\left\lVert \ell_0\right\rVert_2}{|g|}
 +\frac{\left\lVert r_0\right\rVert_2\left\lVert v\right\rVert_2}{|g|}
 +p\min\!\left\{
 \frac{\left\lVert u\right\rVert_2\left\lVert \ell_0\right\rVert_2}{|g|},
 \frac{\left\lVert r_0\right\rVert_2\left\lVert v\right\rVert_2}{|g|}
 \right\}.
 \label{eq:correction-upper}$$

Since $P_0^2=P_0$, expansion of $\lambda_0P_0+(\mathrm I-P_0)A(\mathrm I-P_0)-A$ gives [\[eq:block-correction\]](#eq:block-correction){reference-type="eqref" reference="eq:block-correction"}. The invariance identities follow immediately. Moreover, $$R_0P_0=\frac{u\ell_0^T}{g},
 \qquad
 P_0R_0=\frac{r_0v^T}{g}.$$ Their spectral norms are the first two terms of [\[eq:correction-upper\]](#eq:correction-upper){reference-type="eqref" reference="eq:correction-upper"}. Finally, $$\left\lVert P_0R_0P_0\right\rVert_2
 \le\min\{\left\lVert P_0\right\rVert_2\left\lVert R_0P_0\right\rVert_2,
           \left\lVert P_0R_0\right\rVert_2\left\lVert P_0\right\rVert_2\},$$ which gives the third term.

[\[thm:validated-factor\]]{#thm:validated-factor label="thm:validated-factor"} Let $\Gamma$ be a circle of radius $r$ and maximum modulus $R_\Gamma$. Suppose $A$ has algebraic count one inside $\Gamma$ and $$\sup_{z\in\Gamma}\left\lVert (z-A)^{-1}\right\rVert_2\le M.$$ Assume $\lambda_0$ lies inside $\Gamma$ and let $\varepsilon$ be the right side of [\[eq:correction-upper\]](#eq:correction-upper){reference-type="eqref" reference="eq:correction-upper"}. If $M\varepsilon<1$, then $$\left\lVert \mathcal Q_-(A;\Gamma)-\lambda_0P_0\right\rVert_2
 \le
 rR_\Gamma
 \frac{M^2\varepsilon}{1-M\varepsilon}.
 \label{eq:weighted-factor-bound}$$ In particular, $\lambda_0P_0$ is a validated center for the actual weighted Riesz term.

By [\[prop:factor-correction\]](#prop:factor-correction){reference-type="ref" reference="prop:factor-correction"}, $\left\lVert \widetilde A-A\right\rVert_2\le\varepsilon$. The Neumann lemma keeps $\Gamma$ in the resolvent set of $\widetilde A$, with resolvent upper $M/(1-M\varepsilon)$, and preserves the algebraic count. The projection $P_0$ commutes with $\widetilde A$, its range carries the eigenvalue $\lambda_0$, and the total count is one. Hence $$\mathcal Q_-(\widetilde A;\Gamma)=\lambda_0P_0.$$ The first resolvent identity in the contour formula [\[eq:weighted-riesz\]](#eq:weighted-riesz){reference-type="eqref" reference="eq:weighted-riesz"} now gives [\[eq:weighted-factor-bound\]](#eq:weighted-factor-bound){reference-type="eqref" reference="eq:weighted-factor-bound"}; this is the weighted Lipschitz theorem of @WangRiesz2026 with all constants displayed.

The Grushin certificate gives, throughout its disk, $$\left|E_{-+}(z)+\frac{z-c_n}{g_n}\right|\le\varepsilon_{*,n}.$$ The maximum principle extends the boundary bound to the interior. At the unique zero, $$|\lambda_n-c_n|\le |g_n|\varepsilon_{*,n}.$$ The resulting uppers at $2048$, $4096$, and $8192$ are respectively $1.782\times10^{-13}$, $3.475\times10^{-13}$, and $6.849\times10^{-13}$.

# Exact stored factors and the spectral quarter--half law {#sec:stored}

The stored matrices come from the RH-36 and RH-37 snapshots [@WangNested2026; @WangIterated2026]. For each parity center, a sparse LU approximation to the bordered inverse is recomputed. Every residual row and column is then evaluated against the exact stored graph using componentwise outward arithmetic [@Rump2010; @WangOutward2026]. The inequality $$\left\lVert X\right\rVert_2\le\sqrt{\left\lVert X\right\rVert_1\left\lVert X\right\rVert_\infty}$$ converts the exact $1$- and $\infty$-norm ledgers into Euclidean bounds.

::: {#tab:stored-ledger}
       $n$   $\left\lVert R\right\rVert_2$   contour resolvent   $\left\lVert \Delta\right\rVert_2$   $M\left\lVert \Delta\right\rVert_2$   $\left\lVert Q_n^{\mathrm s}-\widehat Q_n\right\rVert_2$
  -------- ------------------------------- ------------------- ------------------------------------ ------------------------------------- ----------------------------------------------------------
    $2048$         $4.262{\times}10^{-11}$          $83.92380$              $1.001{\times}10^{-12}$               $8.394{\times}10^{-11}$                                    $3.651{\times}10^{-10}$
    $4096$         $1.181{\times}10^{-10}$          $84.00733$              $1.970{\times}10^{-12}$               $1.655{\times}10^{-10}$                                    $7.203{\times}10^{-10}$
    $8192$         $3.296{\times}10^{-10}$          $84.03470$              $3.898{\times}10^{-12}$               $3.276{\times}10^{-10}$                                     $1.427{\times}10^{-9}$

  : Exact stored Euclidean Grushin and factor-correction ledger.
:::

All three correction products are below $4\times10^{-10}$. Thus the archived parity factors are not merely small-residual diagnostics: they are centers of exact spectral weighted terms with explicit Euclidean radii.

Let $\mathscr H_{2n}$ be the orthogonal pairwise Haar transform. Write $$\mathscr H_{2n}Q_{2n}^{\mathrm s}\mathscr H_{2n}^T
 =\begin{pmatrix}A_n&B_n\\C_n&D_n\end{pmatrix},
 \qquad
 E_n=A_n-Q_n^{\mathrm s}.$$ The Arb factor algebra from RH-40 gives exact Frobenius intervals for the same blocks built from $\widehat Q_n$ [@Johansson2017; @WangRiesz2026]. If $e_n=\left\lVert Q_n^{\mathrm s}-\widehat Q_n\right\rVert_2$, then every compressed error has rank at most two, and therefore $$\left\lVert B_n-\widehat B_n\right\rVert_{\mathrm F},
 \left\lVert C_n-\widehat C_n\right\rVert_{\mathrm F},
 \left\lVert D_n-\widehat D_n\right\rVert_{\mathrm F}
 \le\sqrt2\,e_{2n},$$ while $$\left\lVert E_n-\widehat E_n\right\rVert_{\mathrm F}
 \le\sqrt2(e_n+e_{2n}).$$ This converts the exact-factor ledger into actual spectral intervals.

::: {#tab:haar-ratios}
  block        rigorous ratio interval       smooth target    maximum deviation
  ------- --------------------------------- --------------- ----------------------
  $E$      $[0.2497729080,\ 0.2498601648]$       $1/4$       $2.271\times10^{-4}$
  $C$      $[0.5000272443,\ 0.5000292074]$       $1/2$       $2.921\times10^{-5}$
  $B$      $[0.5000320106,\ 0.5000338986]$       $1/2$       $3.390\times10^{-5}$
  $D$      $[0.2496654557,\ 0.2503931293]$       $1/4$       $3.932\times10^{-4}$

  : Validated ratios of actual spectral parity Haar blocks.
:::

This closes the exact-stored spectral-factor limitation stated explicitly in RH-40. It does not validate every future binary64 rebuild; it validates the three archived matrices and factors whose hashes are recorded in the certificate.

# The smooth intrinsic continuum kernel {#sec:kernel}

Let $$\Pi_-=\mathcal P_-(\mathcal K;\Gamma),
 \qquad Q_-=\mathcal Q_-(\mathcal K;\Gamma).$$ The continuum count is one, so $\Pi_-$ and $Q_-$ have rank one. If $\lambda_-$ is the enclosed eigenvalue, then $$Q_-=\lambda_-\Pi_-,
 \qquad
 \mathcal K\Pi_-=\Pi_-\mathcal K=Q_-.
 \label{eq:spectral-identities}$$

[\[prop:smooth-kernel\]]{#prop:smooth-kernel label="prop:smooth-kernel"} The weighted term $Q_-$ has a real $C^\infty$ kernel $q_-(x,y)$. If $$M_\Gamma=sup_{z\in\Gamma}\left\lVert (z-\mathcal K)^{-1}\right\rVert_{2\to2},$$ then $$\left\lVert \Pi_-\right\rVert_{2\to2}\le rM_\Gamma,
 \qquad
 \left\lVert Q_-\right\rVert_{2\to2}\le rR_\Gamma M_\Gamma.
 \label{eq:projection-weighted-bounds}$$ Because $Q_-$ has rank one, $$\left\lVert q_-\right\rVert_{L^2([0,1]^2)}=\left\lVert Q_-\right\rVert_{2\to2}.$$ For source derivatives, $$\left\lVert \partial_x^a q_-\right\rVert_{L^2}
 \le\left\lVert \partial_x^ak\right\rVert_{L^2}\left\lVert \Pi_-\right\rVert_{2\to2},$$ and analogously for pure target derivatives. Mixed derivatives satisfy $$\left\lVert \partial_x^a\partial_y^bq_-\right\rVert_{L^2}
 \le
 \rho_\Gamma^{-1}
 \left\lVert \partial_x^ak\right\rVert_{L^2}
 \left\lVert \Pi_-\right\rVert_{2\to2}
 \left\lVert \partial_y^bk\right\rVert_{L^2}.
 \label{eq:mixed-kernel-envelope}$$

The kernel $k$ is smooth. Since a Hilbert--Schmidt operator composed with a bounded operator remains Hilbert--Schmidt, $Q_-=\mathcal K\Pi_-$ has a kernel and source derivatives are obtained by differentiating the left kernel factor. The identity $Q_-=\Pi_-\mathcal K$ gives the target derivatives. Repeated differentiation is permitted because every derivative kernel is Hilbert--Schmidt.

The contour length is $2\pi r$, giving [\[eq:projection-weighted-bounds\]](#eq:projection-weighted-bounds){reference-type="eqref" reference="eq:projection-weighted-bounds"}. Rank one makes the Hilbert--Schmidt and operator norms equal. Finally, $$\mathcal K\Pi_-\mathcal K=\lambda_-Q_-,$$ so $$Q_-=\lambda_-^{-1}\mathcal K\Pi_-\mathcal K.$$ Differentiate the two outer kernels and use $|\lambda_-|\ge\rho_\Gamma$ to obtain [\[eq:mixed-kernel-envelope\]](#eq:mixed-kernel-envelope){reference-type="eqref" reference="eq:mixed-kernel-envelope"}. Reality follows from the real operator, the conjugation-invariant circle, and algebraic count one.

The RH-42 Arb envelope gives the explicit constants in [3](#tab:kernel-envelope){reference-type="ref" reference="tab:kernel-envelope"}.

::: {#tab:kernel-envelope}
  quantity                                                            rigorous upper
  ----------------------------------------------- ----------------------------------
  $\left\lVert q_-\right\rVert_{L^2}$                            $5.854166642320046$
  $\left\lVert (q_-)_x\right\rVert_{L^2}$                        $3780.968408944756$
  $\left\lVert (q_-)_y\right\rVert_{L^2}$                        $2160.665606696173$
  $\left\lVert (q_- )_{xx}\right\rVert_{L^2}$          $1.107398829423628\times10^6$
  $\left\lVert (q_- )_{xy}\right\rVert_{L^2}$          $1.544489270236306\times10^6$
  $\left\lVert (q_- )_{yy}\right\rVert_{L^2}$          $2.679665935766761\times10^5$
  $\left\lVert (q_- )_{xxyy}\right\rVert_{L^2}$     $5.610208521245975\times10^{10}$

  : Validated Hilbert--Schmidt envelope for the intrinsic parity kernel.
:::

Applying the midpoint-average Peano theorem of @WangEuclidean2026 to $q_-$ itself gives, at $n=65536$, $$\left\lVert Q_n^\circ-Q_n^{\mathrm G}\right\rVert_2
 \le1.790125512353268\times10^{-5},
 \label{eq:kernel-midpoint-defect}$$ where $Q_n^{\mathrm G}$ is the cell-average matrix of $q_-$. Thus the intrinsic kernel has a direct second-order midpoint discretization even before it is compared with the weighted term of $P_n$.

# Infinite-complement Schur closure {#sec:complement-schur}

RH-42 passed from the last Galerkin operator to the continuum through the direct defect $\left\lVert \mathcal K-P_n^{\mathrm G}\mathcal KP_n^{\mathrm G}\right\rVert$. That estimate is valid but adds the two one-sided errors. The complement can instead be retained as a Schur block, where its influence on the parity branch is quadratic.

Let $P=P_n^{\mathrm G}$ be the orthogonal cell-average projection and $Q=\mathrm I-P$. Relative to $L^2=V_n\oplus V_n^\perp$, $$\mathcal K=
 \begin{pmatrix}
  A_n&B_n\\C_n&D_n
 \end{pmatrix},
 \qquad
 A_n=P\mathcal KP.
 \label{eq:continuum-blocks}$$ The cellwise Poincaré--Wirtinger inequality gives $$\left\lVert C_n\right\rVert_2\le\frac{K_x}{\pi n},
 \qquad
 \left\lVert B_n\right\rVert_2\le\frac{K_y}{\pi n},
 \qquad
 \left\lVert D_n\right\rVert_2\le\frac{K_{xy}}{\pi^2n^2}.
 \label{eq:complement-block-bounds}$$ These are the same formulas as the dyadic Haar bounds, but the detail space is now the full infinite-dimensional complement.

[\[thm:complement-schur\]]{#thm:complement-schur label="thm:complement-schur"} Suppose $$\sup_{z\in\Gamma}\left\lVert (z-A_n)^{-1}\right\rVert_2\le M,$$ and write $b,c,d$ for the three uppers in [\[eq:complement-block-bounds\]](#eq:complement-block-bounds){reference-type="eqref" reference="eq:complement-block-bounds"}. If $$d<\rho_\Gamma,
 \qquad
 M b(\rho_\Gamma-d)^{-1}c<1,$$ then $\mathcal K$ and $A_n$ have the same algebraic count inside $\Gamma$. The full resolvent is bounded by the Frobenius norm of $$\begin{pmatrix}
 S&SbR_d\\R_dcS&R_d+R_dcSbR_d
 \end{pmatrix},$$ where $$R_d=(\rho_\Gamma-d)^{-1},
 \qquad
 S=\frac{M}{1-MbR_dc}.$$ At $n=65536$ the Schur product is $$0.0007281434256176882$$ and the resulting continuum resolvent upper is [\[eq:improved-continuum-resolvent\]](#eq:improved-continuum-resolvent){reference-type="eqref" reference="eq:improved-continuum-resolvent"}.

The detail spectrum lies in $|z|\le d$, disjoint from the disk bounded by $\Gamma$. Take the Schur complement of $z-D_n$. The self-energy $B_n(z-D_n)^{-1}C_n$ has norm at most $bR_dc$, so the displayed product gives the Schur inverse and the four block bounds. Homotoping $B_n,C_n$ to zero keeps the detail block fixed and the majorants decrease. At the decoupled endpoint $A_n\oplus D_n$, the detail block contributes no eigenvalue inside $\Gamma$, proving count preservation. The argument uses only operator norms and therefore does not require the detail space to be finite-dimensional.

This improves the previous continuum upper by a factor $2.36$. More importantly, it supplies the constants for a sharp weighted-term transport.

# Weighted Schur transport and the construction ball {#sec:weighted-schur}

The block resolvent formula contains more information than the norm of the full resolvent. Let $$T=\begin{pmatrix}A&B\\C&D\end{pmatrix}$$ and suppose the detail block has no spectrum in $\Gamma$. Put $$R_A=(z-A)^{-1},
 \quad R_D=(z-D)^{-1},
 \quad S=(z-A-BR_DC)^{-1}.$$ Then $$(z-T)^{-1}=
 \begin{pmatrix}
 S&SBR_D\\R_DCS&R_D+R_DCSBR_D
 \end{pmatrix}.$$ Since $\mathcal Q_-(D;\Gamma)=0$, subtracting the decoupled weighted term leaves only $$\begin{aligned}
 S-R_A&=SBR_DCR_A,\\
 SBR_D,&\qquad R_DCS,\qquad R_DCSBR_D.\end{aligned}$$

[\[prop:weighted-schur\]]{#prop:weighted-schur label="prop:weighted-schur"} Assume uniform bounds $$\left\lVert R_A\right\rVert\le M,
 \quad\left\lVert R_D\right\rVert\le R_d,
 \quad\left\lVert S\right\rVert\le S_*,
 \quad\left\lVert B\right\rVert\le b,
 \quad\left\lVert C\right\rVert\le c$$ on $\Gamma$. Then $$\left\lVert \mathcal Q_-(T;\Gamma)-
       \operatorname{diag}(\mathcal Q_-(A;\Gamma),0)\right\rVert_2$$ is at most the Frobenius norm of $$rR_\Gamma
 \begin{pmatrix}
 S_*bR_dcM&S_*bR_d\\
 R_dcS_*&R_dcS_*bR_d
 \end{pmatrix}.
 \label{eq:weighted-schur-majorant}$$

Insert the four resolvent differences above into [\[eq:weighted-riesz\]](#eq:weighted-riesz){reference-type="eqref" reference="eq:weighted-riesz"}. The contour length contributes $r$ and the weight contributes $R_\Gamma$. A block operator whose block norms are bounded entrywise by a nonnegative $2\times2$ matrix has norm at most the matrix spectral norm, hence at most its Frobenius norm.

The construction of [\[thm:continuum-kernel\]](#thm:continuum-kernel){reference-type="ref" reference="thm:continuum-kernel"} starts with the validated stored factor at $4096$ and applies the weighted Lipschitz or weighted Schur bound at every subsequent gate. The ledger is shown in [4](#tab:weighted-chain){reference-type="ref" reference="tab:weighted-chain"}.

::: {#tab:weighted-chain}
  gate                                     weighted-term difference upper
  -------------------------------------- --------------------------------
  stored factor $\to$ exact stored $Q$              $7.203\times10^{-10}$
  exact stored $\to M_{4096}$                         $0.003863696504533$
  $M_{4096}\to A_{4096}$                              $0.319148940875075$
  $A_{4096}\to A_{8192}$                              $0.891990587282860$
  $A_{8192}\to A_{16384}$                             $0.312894707103005$
  $A_{16384}\to A_{32768}$                            $0.114813078602118$
  $A_{32768}\to A_{65536}$                            $0.049768188532663$
  $A_{65536}\to\mathcal K$ complement                 $0.023793507962359$
  total                                               $1.716272707582898$

  : Validated operator-norm construction of the continuum weighted term.
:::

The first and final operators both have rank one, so their difference has rank at most two. Therefore its Hilbert--Schmidt norm is at most $\sqrt2$ times its operator norm, yielding [\[eq:construction-kernel-ball\]](#eq:construction-kernel-ball){reference-type="eqref" reference="eq:construction-kernel-ball"}.

# The smooth quarter--half Haar theorem {#sec:haar-theorem}

The exact stored ratios in [2](#tab:haar-ratios){reference-type="ref" reference="tab:haar-ratios"} have a simple continuum origin. Let $q\in C^4([0,1]^2)$ and form its midpoint matrix $$(Q_h^\circ)_{ij}=h q(x_i,y_j).$$ Within each coarse cell, the two fine midpoints are $x_i\pm h/4$ and $y_j\pm h/4$. Choose the detail orientation so that the signed coefficient is $+1$ at the positive offset. The Haar blocks of the fine midpoint matrix have entries $$\begin{aligned}
 (A_h)_{ij}
 &=\frac h4\sum_{\varepsilon,\eta=\pm1}
   q(x_i+\varepsilon h/4,y_j+\eta h/4),\\
 (C_h)_{ij}
 &=\frac h4\sum_{\varepsilon,\eta=\pm1}
   \varepsilon q(x_i+\varepsilon h/4,y_j+\eta h/4),\\
 (B_h)_{ij}
 &=\frac h4\sum_{\varepsilon,\eta=\pm1}
   \eta q(x_i+\varepsilon h/4,y_j+\eta h/4),\\
 (D_h)_{ij}
 &=\frac h4\sum_{\varepsilon,\eta=\pm1}
   \varepsilon\eta q(x_i+\varepsilon h/4,y_j+\eta h/4).
 \label{eq:four-point-haar}\end{aligned}$$ Put $E_h=A_h-Q_h^\circ$.

[\[thm:haar-limits\]]{#thm:haar-limits label="thm:haar-limits"} Under the piecewise-constant Hilbert--Schmidt identification, $$\begin{aligned}
 h^{-2}E_h&\longrightarrow\frac{q_{xx}+q_{yy}}{32},
 \label{eq:E-limit}\\
 h^{-1}C_h&\longrightarrow\frac{q_x}{4},
 \label{eq:C-limit}\\
 h^{-1}B_h&\longrightarrow\frac{q_y}{4},
 \label{eq:B-limit}\\
 h^{-2}D_h&\longrightarrow\frac{q_{xy}}{16}
 \label{eq:D-limit}\end{aligned}$$ in Hilbert--Schmidt norm. Whenever the corresponding limiting tensor is nonzero, refinement $h\mapsto h/2$ gives norm ratios $$\frac14,\qquad\frac12,\qquad\frac12,\qquad\frac14$$ for $E,C,B,D$, respectively.

Taylor-expand the four samples in [\[eq:four-point-haar\]](#eq:four-point-haar){reference-type="eqref" reference="eq:four-point-haar"}. Symmetry cancels all odd terms in $A_h$, all terms except those odd in $x$ in $C_h$, all terms except those odd in $y$ in $B_h$, and all terms except those odd in both variables in $D_h$. Entrywise, $$\begin{aligned}
 E_h&=\frac{h^3}{32}(q_{xx}+q_{yy})+O(h^5),\\
 C_h&=\frac{h^2}{4}q_x+O(h^4),\\
 B_h&=\frac{h^2}{4}q_y+O(h^4),\\
 D_h&=\frac{h^3}{16}q_{xy}+O(h^5),\end{aligned}$$ uniformly on the coarse midpoint grid. An $n\times n$ midpoint matrix with entries $h f(x_i,y_j)$ has Frobenius norm converging to $\left\lVert f\right\rVert_{L^2}$. Divide by the displayed powers of $h$ and use midpoint Riemann convergence. The ratio statement follows if the limiting norm is positive.

Applied to the intrinsic $q_-$ from [\[thm:continuum-kernel\]](#thm:continuum-kernel){reference-type="ref" reference="thm:continuum-kernel"}, this theorem explains why the validated stored ratios already sit so close to their quarter--half limits. The theorem is gauge-free: it concerns the kernel $q_-$, not separately normalized left and right modes.

# Uniform sparse transfer and intrinsic deflation {#sec:deflation}

The improved continuum resolvent changes the all-grid threshold. Combining the continuum Galerkin defect and the second-order midpoint defect gives, at $n=65536$, $$\left\lVert \mathcal K-\widetilde M_n\right\rVert_{2\to2}
 \le0.005112929739977326.$$ Its product with [\[eq:improved-continuum-resolvent\]](#eq:improved-continuum-resolvent){reference-type="eqref" reference="eq:improved-continuum-resolvent"} is $$0.5775311353158<1,$$ which yields [\[eq:uniform-midpoint-resolvent\]](#eq:uniform-midpoint-resolvent){reference-type="eqref" reference="eq:uniform-midpoint-resolvent"}. The defect decreases for every larger integer $n$.

The exact normalizer lower is $$Z_{\min}\ge0.012533141373155001.$$ At the threshold, the discrete row-normalization defect is $$\left\lVert P_n-M_n\right\rVert_2\le6.19557781914536\times10^{-6},$$ with Neumann product $0.0016565047527645261$. Finally, the relaxed eight-sigma cutoff theorem gives $$\left\lVert P_n^{(8)}-P_n\right\rVert_2
 \le1.957332885203986\times10^{-13}.$$ Every factor in this fixed-width upper is nonincreasing with $n$. Since $L_n\ge8$, the same number controls the adaptive family. This proves the resolvent and count statements in [\[thm:uniform-family\]](#thm:uniform-family){reference-type="ref" reference="thm:uniform-family"}.

The weighted first-resolvent identity gives $$\left\lVert \mathcal Q_-(A;\Gamma)-\mathcal Q_-(B;\Gamma)\right\rVert_2
 \le rR_\Gamma M_AM_B\left\lVert A-B\right\rVert_2.$$ Inserting the full and sparse resolvent uppers proves [\[eq:uniform-weighted-cutoff\]](#eq:uniform-weighted-cutoff){reference-type="eqref" reference="eq:uniform-weighted-cutoff"}.

[\[prop:deflation\]]{#prop:deflation label="prop:deflation"} Let $T$ have one algebraically simple eigenvalue $\lambda$ inside $\Gamma$, and put $Q=\mathcal Q_-(T;\Gamma)$. Then $$T_\perp=T-Q$$ commutes with the Riesz projection, is zero on its range, and agrees with $T$ on its complementary invariant subspace. Hence $$\operatorname{spec}(T_\perp)\setminus\{0\}
 =\operatorname{spec}(T)\setminus\{\lambda\}
 \label{eq:deflated-spectrum}$$ with algebraic multiplicity away from zero.

For a simple branch, $Q=\lambda\mathcal P_-$. Both $T$ and $Q$ commute with $\mathcal P_-$. On $\operatorname{Ran}\mathcal P_-$ their difference is zero, while on $\ker\mathcal P_-$ the weighted term vanishes. The invariant direct-sum decomposition gives [\[eq:deflated-spectrum\]](#eq:deflated-spectrum){reference-type="eqref" reference="eq:deflated-spectrum"}.

For full and sparse matrices, $$\begin{aligned}
 \left\lVert P_{n,\perp}^{(L)}-P_{n,\perp}\right\rVert_2
 &\le\left\lVert P_n^{(L)}-P_n\right\rVert_2\\
 &\quad+\left\lVert \mathcal Q_-(P_n^{(L)};\Gamma)
                  -\mathcal Q_-(P_n;\Gamma)\right\rVert_2.\end{aligned}$$ This proves [\[eq:uniform-deflated-cutoff\]](#eq:uniform-deflated-cutoff){reference-type="eqref" reference="eq:uniform-deflated-cutoff"}. Under the adaptive schedule, RH-39 gives $$\left\lVert P_n^{(L_n)}-P_n\right\rVert_2
 =O\!\left(n^{-2}(\log n)^{-1/4}\right),$$ so both the weighted term and the deflated sparse family inherit the same rate relative to their full counterparts.

Finally, RH-40 already proves $$\left\lVert \mathcal Q_-(P_n;\Gamma)-Q_n^\circ\right\rVert_2=O(n^{-2})$$ for a simple isolated smooth continuum branch. The continuum simplicity and the uniform Euclidean cutoff condition are now both unconditional, so [\[cor:weighted-bridge\]](#cor:weighted-bridge){reference-type="ref" reference="cor:weighted-bridge"} follows from @Atkinson1967 [@Anselone1971; @Chatelin1983; @WangRiesz2026].

The fixed eight-sigma weighted difference is uniformly below $7.28\times10^{-10}$, which is ample for spectral deflation. Nevertheless the underlying row-norm cutoff has a mathematically nonzero continuum floor. Adaptive growth is required when convergence to the full continuum kernel, rather than uniform spectral stability, is the claim.

# Certificate summary and figure {#sec:certificate}

The complete certificate closes the following gates.

1.  exact stored Euclidean Grushin counts at $2048$, $4096$, and $8192$;

2.  two-sided correction products below $3.28\times10^{-10}$;

3.  actual spectral quarter--half intervals at both stored transitions;

4.  an infinite-complement Schur product below $7.29\times10^{-4}$;

5.  a continuum weighted-term construction ball;

6.  an all-grid exact-real theorem from $n=65536$;

7.  full-to-sparse weighted and deflated differences below $7.28\times10^{-10}$.

![Validated intrinsic parity-kernel closure. (a) The exact archived $4096$ factor center, displayed as a piecewise kernel; it is not a pointwise interval enclosure of $q_-$. (b) The block-diagonalizing corrections and actual weighted-term errors for all three stored factors. (c) Corrected Frobenius intervals for the actual spectral Haar ratios, together with the smooth-kernel quarter--half targets. (d) The continuum complement Schur step improves the continuum and all-grid resolvent constants and halves the stable certified threshold.](<../../../../../zeta_mvp0/papers/RH-43-validated-weighted-riesz-parity-kernel/figures/validated_weighted_parity_kernel.pdf>){#fig:summary width="\\textwidth"}

# What is closed and what remains {#sec:boundary}

The present result changes the status of the weighted-Riesz route in four ways.

1.  **The negative continuum branch is now an intrinsic kernel.** It is rank one, smooth, gauge-free, and enclosed in operator and Hilbert--Schmidt norms around an archived center.

2.  **The stored parity factors are actual spectral terms.** Their previous floating residual status has been replaced by exact stored-matrix Grushin and correction certificates at all three levels.

3.  **The quarter--half mechanism is both analytic and spectral.** The continuum theorem identifies the derivative tensors, while the stored ratio intervals now concern the true matrix weighted terms.

4.  **Parity deflation is ready for later trace work.** The operator $\mathcal K_\perp$ and its matrix analogues remove the negative eigenvalue without a mode normalization convention.

Several boundaries are equally important.

1.  The noise width remains fixed at $\sigma=1/100$.

2.  The continuum kernel is enclosed in $L^2$ and derivative Hilbert--Schmidt norms; no pointwise interval heat map is claimed.

3.  The all-dimension theorem concerns exact-real Gaussian formulas. The binary64 theorem concerns only the three archived matrices.

4.  The Perron weighted term has not been merged with the parity term. A validated rank-two intrinsic deflation is the natural next gate.

5.  No self-adjoint generator, $T\log T$ law, arithmetic trace formula, prime-power identity, zeta-zero identification, or Riemann-hypothesis conclusion follows from this paper.

# Archive and reproducibility {#sec:archive}

The archive contains two principal ledgers:

1.  the multilevel exact-stored Euclidean Grushin certificate; and

2.  the complete factor, Haar, complement, kernel, family, cutoff, and deflation composition certificate.

Every cross-paper input, local source, result, figure, and publication artifact is recorded by SHA-256.

The complete replay is:

    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/run_multilevel_euclidean_grushin.py
    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/build_weighted_kernel_certificate.py
    MPLBACKEND=Agg PYTHONDONTWRITEBYTECODE=1 \
      /root/math/.venv/bin/python experiments/make_figures.py
    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      -m pytest -q -p no:cacheprovider
    latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
    cp main.pdf validated-weighted-riesz-parity-kernel.pdf
    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/build_archive.py
    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/verify_archive.py

The $8192$ bordered inverse replay is the longest step, taking roughly six minutes on the current server. The composition, Arb Haar ledger, tests, and figures take only seconds.

# Conclusion

An isolated eigenvalue is not yet a usable spectral subtraction. The appropriate object is its weighted Riesz term. Here that term has been constructed as a validated smooth continuum kernel, connected by an explicit chain to the archived $4096$ factor, and transferred uniformly to full and adaptive sparse matrix families.

The same argument resolves two older ambiguities. Two-sided residuals now prove that all three archived parity factors are genuine spectral terms, and the quarter--half Haar law follows from both a smooth-kernel theorem and corrected actual-matrix intervals. Treating the infinite orthogonal complement by Schur rather than by a direct norm defect improves the continuum conditioning enough to halve the stable all-grid threshold.

The resulting deflated operator removes the negative branch exactly and preserves the rest of the spectrum away from zero. This is the first strictly intrinsic continuum object in the route that can be handed to a subsequent trace or determinant construction. The next step is not an arithmetic identification; it is the validated addition of the Perron term and the formation of a rank-two intrinsic complement.
