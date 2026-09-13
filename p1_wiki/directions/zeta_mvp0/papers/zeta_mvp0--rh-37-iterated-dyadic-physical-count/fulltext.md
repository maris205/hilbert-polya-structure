---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-37-iterated-dyadic-physical-count"
canonical_tex: "zeta_mvp0/papers/RH-37-iterated-dyadic-physical-count/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-37-iterated-dyadic-physical-count/iterated-dyadic-physical-count.pdf"
source_sha256: "b8da9c44a42108fb15048919079223892e2eef36e66c0a8f99675e25a80a7caa"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Iterated Dyadic Schur Continuation of a Physical Spectral Count A Hierarchical Resolvent Certificate from $2048$ to $8192$ Cells at a Quadratic Band-Merging Map

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-37-iterated-dyadic-physical-count>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-37-iterated-dyadic-physical-count/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-37-iterated-dyadic-physical-count/iterated-dyadic-physical-count.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-37-iterated-dyadic-physical-count/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-37-iterated-dyadic-physical-count/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  A preceding computer-assisted theorem proved that exact stored Perron/parity-extracted physical two-step matrices on $2048$ and $4096$ midpoint cells each have one eigenvalue inside a prescribed complex circle. Its direct coarse resolvent atlas did not by itself provide an efficient route to the next grid. We give a second rigorous dyadic continuation, at fixed Gaussian width $\sigma=10^{-2}$, and introduce a hierarchical resolvent estimate that avoids a direct $4096$-dimensional inverse atlas.

  For the $4096\to8192$ split, componentwise outward residuals around four rank-$96$ centers certify the coarse-consistency, coarse-to-detail, detail-to-coarse, and detail blocks by

  $$4.97036\times10^{-5},\quad 5.66125\times10^{-3},\quad
  6.86176\times10^{-3},\quad 3.26337\times10^{-5}.$$

  The resulting second-level effective perturbation is at most $1.52962\times10^{-4}$, so an $A_{4096}$ resolvent bound below $6537.58$ is sufficient. We tighten the inherited $A_{2048}$ atlas from 170 to 183 rigorous centers and form an exact 324-leaf rational contour partition. An exact Schur block-inverse formula propagates each leafwise $A_{2048}$ bound through the first refinement. The worst propagated $A_{4096}$ resolvent is $4843.82$, and the final matrix Rouché product is $0.740919<1$. Hence, for the exact archived binary64 matrices,

  $$\boxed{N_{\Gamma}(A_{2048})=N_{\Gamma}(A_{4096})
   =N_{\Gamma}(A_{8192})=1.}$$

  This is a finite stored-matrix theorem at one noise scale. It does not prove a continuum limit, an all-dimensions induction, a zero-noise limit, a zeta-zero identification, a Hilbert--Pólya construction, or the Riemann hypothesis.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Iterated Dyadic Schur Continuation of a Physical Spectral Count\
  A Hierarchical Resolvent Certificate from $2048$ to $8192$ Cells\
  at a Quadratic Band-Merging Map
```

## Markdown 正文

# Introduction

The previous nested-grid certificate [@WangNested2026] answered one discretization-stability question: a contour count proved at dimension $2048$ survives the refinement to $4096$. Repeating that proof naively at the next scale would require a direct atlas of rigorous inverses for a $4096$-dimensional nonnormal matrix. Such an atlas is possible in principle, but it discards the exact coarse/detail structure already certified at the first refinement.

This paper asks a sharper question. Can the first Schur decomposition be used not only to transfer a count, but also to transfer a *resolvent bound* strong enough to close the next count comparison? The answer is yes for the exact stored matrices studied here. The proof chain is

$$\begin{gathered}
\text{direct }A_{2048}\text{ resolvent centers}
\longrightarrow
\text{first Schur effective inverse}
\longrightarrow
\text{full }A_{4096}\text{ resolvent}\notag\\
\longrightarrow
\text{second Schur effective comparison}
\longrightarrow
N_{\Gamma}(A_{8192})=N_{\Gamma}(A_{4096}).
\end{gathered}$$

The distinction matters because these transfer matrices are strongly nonnormal. Eigenvalue displacements alone do not control contour counts; resolvent amplification is the relevant quantity [@Kato1995; @TrefethenEmbree2005]. The new estimate keeps that amplification visible at both refinement levels.

The principal contributions are as follows.

1.  We certify the exact $4096\to8192$ coarse/detail blocks by componentwise factor-graph residuals. Relative to the first split, the two consistency/detail blocks are approximately one quarter as large and the cross channels approximately one half as large.

2.  We prove a norm-preserving block-inverse propagation formula. It turns a leafwise $A_{2048}$ resolvent upper $M_0$ into a rigorous $A_{4096}$ upper without constructing a $4096$-dimensional inverse.

3.  We tighten the inherited direct atlas with only 13 additional centers. The resulting exact rational partition closes both the first effective inverse gate and the second matrix Rouché gate.

4.  We bitwise identify the $A_{4096}$ factor object used here with the one certified in the preceding theorem, thereby obtaining the three-scale count chain.

The observed scaling is encouraging, but this paper does not promote two finite ratios to an asymptotic law. An induction would require uniform block estimates and a uniformly controlled hierarchical resolvent atlas, neither of which is proved here.

# Stored matrices, contour, and inherited count {#sec:objects}

Let $P_m$ be the archived row-normalized folded Gaussian midpoint matrix on $m$ positive cells. Let

$$X_m,Y_m\in\mathbb R^{m\times2},\qquad
\Lambda_m\in\mathbb R^{2\times2}$$

be the stored right modes, left modes, and peripheral eigenvalue diagonal. The Perron/parity-extracted one-step and physical two-step matrices are

$$U_m=P_m-X_m\Lambda_mY_m^T,
 \qquad A_m=U_m^2.
 \label{eq:physical}$$

Every binary64 entry in these factors is treated as an exact real number. We write

$$A_0=A_{2048},\qquad A_1=A_{4096},\qquad A_2=A_{8192}.$$

The positively oriented counting circle is

$$\Gamma:\quad z=z_0+r e^{i\theta},\qquad 0\le\theta\le2\pi,
 \label{eq:contour}$$

with stored values

$$z_0=-0.3233504401504541-0.5508412474453575i,
 \qquad r=0.2624987592858511.
 \label{eq:contour-values}$$

The distance from the origin to the closed counting disk satisfies

$$\rho_0=|z_0|-r\ge0.376235604149098.
 \label{eq:origin-distance}$$

For a matrix $A$, let $N_{\Gamma}(A)$ denote the algebraic number of eigenvalues in the interior of $\Gamma$.

[\[prop:inherited\]]{#prop:inherited label="prop:inherited"} For the exact archived factors at $\sigma=10^{-2}$,

$$N_{\Gamma}(A_0)=N_{\Gamma}(A_1)=1.$$

The $A_1$ sparse matrix, right and left peripheral modes, and peripheral values consumed in the present snapshot are bitwise identical to those in the preceding certificate.

The count is the main theorem of @WangNested2026, built on the exact packet-pair count of @WangPacketPair2026. The present replay hashes the sparse data, indices, row pointers, right modes, left modes, and peripheral values independently. All six hashes agree with the inherited $A_1$ object, and the inherited snapshot and theorem hashes also agree with the archive.

We distinguish exact algebra, rigorous stored-binary64 certificates, and floating diagnostics. Only the first two enter the theorem. Sparse eigensolves are reported later solely to localize the counted eigenvalue.

# Exact dyadic coordinates at two levels {#sec:coordinates}

For a dyadic refinement from $n$ to $2n$, define replication and alternating-detail injections by

$$(Jx)_{2k}=(Jx)_{2k+1}=x_k,
\qquad
(Ky)_{2k}=y_k,\quad (Ky)_{2k+1}=-y_k.$$

Define the corresponding restrictions

$$R=\frac12J^T,\qquad S=\frac12K^T,$$

and set

$$T=[J\ K],\qquad T^{-1}=\begin{bmatrix}R\\S\end{bmatrix}.$$

These identities are exact over the stored reals. Moreover $T=\sqrt2\,Q$ for an orthogonal $Q$, so

$$T^{-1}MT=Q^TMQ,\qquad \left\lVert T^{-1}MT\right\rVert_2=\left\lVert M\right\rVert_2.
 \label{eq:norm-invariance}$$

Thus the unnormalized integer-valued coordinate maps introduce no condition number loss in the Euclidean norm.

At refinement level $j=1,2$, the exact coordinate block form is

$$T_j^{-1}A_jT_j=
 \begin{pmatrix}
 A_{j-1}+E_j & B_j\\
 C_j & D_j
 \end{pmatrix}.
 \label{eq:block-form}$$

Here $C_j$ maps coarse coordinates to detail coordinates, while $B_j$ maps detail coordinates back to coarse coordinates. Whenever $z-D_j$ is invertible, define

$$\begin{aligned}
 R_{D,j}(z)&=(z-D_j)^{-1},\label{eq:detail-resolvent}\\
 \Delta_j(z)&=E_j+B_jR_{D,j}(z)C_j,\label{eq:self-energy}\\
 F_j(z)&=z-A_{j-1}-\Delta_j(z).\label{eq:effective}\end{aligned}$$

The exact Schur determinant identity is

$$\det(z-A_j)=\det(z-D_j)\det F_j(z).
 \label{eq:schur-determinant}$$

If $\left\lVert D_j\right\rVert_2<\rho_0$, every eigenvalue of $D_j$ lies in the origin-centered disk of radius $\left\lVert D_j\right\rVert_2$, which is disjoint from the counting disk. In that case

$$\sup_{z\in\Gamma}\left\lVert R_{D,j}(z)\right\rVert_2
 \le d_j:=\frac{1}{\rho_0-\left\lVert D_j\right\rVert_2},
 \label{eq:detail-bound}$$

and

$$\sup_{z\in\Gamma}\left\lVert \Delta_j(z)\right\rVert_2
 \le \varepsilon_j:=\left\lVert E_j\right\rVert_2+
 \left\lVert B_j\right\rVert_2d_j\left\lVert C_j\right\rVert_2.
 \label{eq:epsilon}$$

# Certified second-level block bounds {#sec:blocks}

The proof objects for each block are stored rank-$96$ factors $L\Sigma V^T$. They are not assumed exact singular decompositions. The following elementary estimate explains how they enter the certificate.

[\[lem:low-rank\]]{#lem:low-rank label="lem:low-rank"} Let $H$ be an exact stored block, and let $L,\Sigma,V$ be stored factors. If

$$\left\lVert L^TL-I\right\rVert_F\le\delta_L,
\qquad
\left\lVert V^TV-I\right\rVert_F\le\delta_V,$$

then

$$\left\lVert H\right\rVert_2\le
 \sqrt{1+\delta_L}\,\left\lVert \Sigma\right\rVert_2\sqrt{1+\delta_V}
 +\left\lVert H-L\Sigma V^T\right\rVert_F.
 \label{eq:low-rank-bound}$$

The Gram estimates imply $\left\lVert L\right\rVert_2\le\sqrt{1+\delta_L}$ and $\left\lVert V\right\rVert_2\le\sqrt{1+\delta_V}$. Apply the triangle inequality, submultiplicativity, and $\left\lVert R\right\rVert_2\le\left\lVert R\right\rVert_F$.

Every matrix action used to form the residual in [\[eq:low-rank-bound\]](#eq:low-rank-bound){reference-type="eqref" reference="eq:low-rank-bound"} is evaluated by componentwise outward arithmetic. The reported Frobenius residual contains both the residual center and its complete radius. Standard verified-floating-point principles are described in @Higham2002 [@Rump2010]; the factor-graph implementation is inherited from @WangOutwardCode2026.

::: {#tab:blocks}
  block               first-level upper            second-level upper        ratio            second residual
  ------- ----------------------------- ----------------------------- ------------ --------------------------
  $E$       $1.98877177\!\times10^{-4}$   $4.97035044\!\times10^{-5}$   $0.249921$   $7.4855\!\times10^{-10}$
  $C$       $1.13214379\!\times10^{-2}$   $5.66124305\!\times10^{-3}$   $0.500046$    $1.5175\!\times10^{-8}$
  $B$       $1.37226417\!\times10^{-2}$   $6.86175172\!\times10^{-3}$   $0.500031$    $7.1604\!\times10^{-9}$
  $D$       $1.30522077\!\times10^{-4}$   $3.26336986\!\times10^{-5}$   $0.250024$   $3.3016\!\times10^{-10}$

  : Certified block norms at the two dyadic levels. The last column is the full second-level Frobenius residual after subtracting the stored rank-$96$ center.
:::

For the second split, [\[eq:detail-bound\]](#eq:detail-bound){reference-type="eqref" reference="eq:detail-bound"} gives

$$d_2\le2.658139564401696.
 \label{eq:d2}$$

The second Schur self-energy and total effective perturbation satisfy

$$\begin{aligned}
 \left\lVert B_2\right\rVert_2d_2\left\lVert C_2\right\rVert_2
 &\le1.0325820704184003\times10^{-4},\label{eq:self2}\\
 \varepsilon_2
 &\le1.5296171140743076\times10^{-4}.
 \label{eq:epsilon2}\end{aligned}$$

Consequently, a contour-wide $A_1$ resolvent bound below

$$\varepsilon_2^{-1}\ge6537.583757391333
 \label{eq:second-threshold}$$

is sufficient for the second matrix Rouché comparison.

# Hierarchical propagation of the 4096-dimensional resolvent {#sec:propagation}

The threshold in [\[eq:second-threshold\]](#eq:second-threshold){reference-type="eqref" reference="eq:second-threshold"} could be tested by direct $4096$-dimensional inverse certificates. Instead we propagate the existing direct $A_0$ atlas through the first exact block decomposition.

[\[prop:resolvent-propagation\]]{#prop:resolvent-propagation label="prop:resolvent-propagation"} Fix $z\in\Gamma$. Suppose

$$\left\lVert (z-A_0)^{-1}\right\rVert_2\le M_0,
\qquad M_0\varepsilon_1<1.$$

Let $d_1$ be the first detail-resolvent upper from [\[eq:detail-bound\]](#eq:detail-bound){reference-type="eqref" reference="eq:detail-bound"}. Then

$$\begin{split}
 \left\lVert (z-A_1)^{-1}\right\rVert_2
 \le M_1(M_0):={}&d_1\\
 &+\sqrt{1+(d_1\left\lVert C_1\right\rVert_2)^2}
 \sqrt{1+(d_1\left\lVert B_1\right\rVert_2)^2}
 \frac{M_0}{1-M_0\varepsilon_1}.
\end{split}
\label{eq:propagated-bound}$$

Write $R_0=(z-A_0)^{-1}$. By [\[eq:self-energy\]](#eq:self-energy){reference-type="eqref" reference="eq:self-energy"}--[\[eq:effective\]](#eq:effective){reference-type="eqref" reference="eq:effective"},

$$F_1=(z-A_0)\bigl(I-R_0\Delta_1(z)\bigr).$$

The Neumann bound gives

$$\left\lVert F_1^{-1}\right\rVert_2\le\frac{M_0}{1-M_0\varepsilon_1}.
 \label{eq:effective-inverse-bound}$$

The exact inverse of the first block matrix factors as

$$\begin{split}
 &\left(
 z-\begin{pmatrix}A_0+E_1&B_1\\C_1&D_1\end{pmatrix}
 \right)^{-1}\\
 &\qquad=
 \begin{bmatrix}I\\R_{D,1}C_1\end{bmatrix}
 F_1^{-1}
 \begin{bmatrix}I&B_1R_{D,1}\end{bmatrix}
 +\begin{pmatrix}0&0\\0&R_{D,1}\end{pmatrix}.
\end{split}
\label{eq:block-inverse}$$

The column and row graph factors obey

$$\left\|\begin{bmatrix}I\\R_{D,1}C_1\end{bmatrix}\right\|_2
\le\sqrt{1+(d_1\left\lVert C_1\right\rVert_2)^2},$$

$$\left\|\begin{bmatrix}I&B_1R_{D,1}\end{bmatrix}\right\|_2
\le\sqrt{1+(d_1\left\lVert B_1\right\rVert_2)^2}.$$

Combine these estimates with [\[eq:effective-inverse-bound\]](#eq:effective-inverse-bound){reference-type="eqref" reference="eq:effective-inverse-bound"}. Finally, [\[eq:norm-invariance\]](#eq:norm-invariance){reference-type="eqref" reference="eq:norm-invariance"} identifies the coordinate-space norm with the ambient $A_1$ resolvent norm.

The first-level certificate supplies

$$d_1\le2.658831394912469,
 \qquad
 \varepsilon_1\le6.119533154024968\times10^{-4}.
 \label{eq:first-constants}$$

The two graph factors in [\[eq:propagated-bound\]](#eq:propagated-bound){reference-type="eqref" reference="eq:propagated-bound"} are bounded by

$$1.000452956430038,\qquad1.000665399669618.$$

Thus the only remaining task is a sufficiently tight leafwise bound for the direct $A_0$ resolvent.

# A tightened direct atlas and two simultaneous gates {#sec:atlas}

At a rigorous direct center $\zeta$, let

$$\left\lVert (\zeta-A_0)^{-1}\right\rVert_2\le M_\zeta.$$

For a circular-arc enclosure contained in a disk satisfying $M_\zeta\delta<1$, the resolvent identity yields

$$\sup_{|z-\zeta|\le\delta}\left\lVert (z-A_0)^{-1}\right\rVert_2
 \le\frac{M_\zeta}{1-M_\zeta\delta}.
 \label{eq:center-transport}$$

The inherited archive contains 170 such centers. We request the stronger first-level target

$$M_0\varepsilon_1<0.75,
 \qquad
 M_0<\frac{0.75}{\varepsilon_1}=1225.583686080214\ldots.
 \label{eq:tight-target}$$

Only 13 additional direct centers are needed. Adaptive exact bisection then produces 324 rational leaves, with maximum refinement level eight and no unresolved component. The leaves form an exact partition of one contour turn.

::: {#tab:atlas}
  quantity                                                              certified upper
  -------------------------------------------------------------- ----------------------
  transported $A_0$ resolvent $M_0$                                $1221.3793571000042$
  first effective product $M_0\varepsilon_1$                       $0.7474271469415178$
  first effective inverse $\left\lVert F_1^{-1}\right\rVert_2$      $4835.750724236383$
  propagated $A_1$ resolvent $M_1$                                  $4843.819104431207$
  second continuation product $M_1\varepsilon_2$                   $0.7409188599618061$

  : Outward-rounded maxima over the exact 324-leaf propagated atlas.
:::

Both products are evaluated leaf by leaf; the maxima need not occur on the same leaf. In particular, the final value in [2](#tab:atlas){reference-type="ref" reference="tab:atlas"} lies well below one and the propagated $A_1$ bound lies below the independent threshold in [\[eq:second-threshold\]](#eq:second-threshold){reference-type="eqref" reference="eq:second-threshold"}.

# The certified three-scale count {#sec:theorem}

We use the finite-dimensional analytic matrix form of Rouché's theorem [@Ahlfors1979; @GohbergSigal1971]. If $A(z)$ is invertible on $\Gamma$, $B(z)$ is analytic on and inside the contour, and

$$\sup_{z\in\Gamma}\left\lVert A(z)^{-1}B(z)\right\rVert_2<1,$$

then $A$ and $A+B$ have the same determinant zero count inside the contour.

[\[thm:main\]]{#thm:main label="thm:main"} At $\sigma=10^{-2}$, for the exact stored binary64 physical two-step matrices defined in [\[eq:physical\]](#eq:physical){reference-type="eqref" reference="eq:physical"},

$$\boxed{N_{\Gamma}(A_{2048})=N_{\Gamma}(A_{4096})
=N_{\Gamma}(A_{8192})=1.}$$

By [\[prop:inherited\]](#prop:inherited){reference-type="ref" reference="prop:inherited"}, $N_{\Gamma}(A_1)=1$. The second detail block satisfies

$$\left\lVert D_2\right\rVert_2\le3.2633698567\times10^{-5}<\rho_0,$$

so $z-D_2$ is invertible on and inside the counting disk and $N_{\Gamma}(D_2)=0$. Hence $\Delta_2(z)$ is analytic there.

On every leaf, [\[prop:resolvent-propagation\]](#prop:resolvent-propagation){reference-type="ref" reference="prop:resolvent-propagation"} and the direct center transport [\[eq:center-transport\]](#eq:center-transport){reference-type="eqref" reference="eq:center-transport"} give a rigorous bound for $(z-A_1)^{-1}$. The exact rational partition covers all of $\Gamma$, and [2](#tab:atlas){reference-type="ref" reference="tab:atlas"} gives

$$\sup_{z\in\Gamma}
\left\lVert (z-A_1)^{-1}\Delta_2(z)\right\rVert_2
\le0.7409188599618061<1.$$

Matrix Rouché therefore shows that

$$N_{\Gamma}(F_2)=N_{\Gamma}(z-A_1)=1.$$

The exact determinant factorization [\[eq:schur-determinant\]](#eq:schur-determinant){reference-type="eqref" reference="eq:schur-determinant"} yields

$$N_{\Gamma}(A_2)=N_{\Gamma}(D_2)+N_{\Gamma}(F_2)=0+1=1.$$

Combining this with the inherited count proves the stated chain.

# Finite-scale diagnostics and what they do not prove {#sec:diagnostics}

![Second dyadic continuation diagnostics and certificates. (a) The second certified consistency and detail blocks are approximately one quarter of the first-level bounds, while the cross channels are approximately one half. (b) Floating sparse eigenvalues are shown only for localization; the count theorem does not use them. (c) The direct $A_{2048}$ leaf bounds are propagated to $A_{4096}$ by [\[eq:propagated-bound\]](#eq:propagated-bound){reference-type="eqref" reference="eq:propagated-bound"}, remaining below the second-level threshold. (d) Both outward-rounded continuation products stay below one.](figures/iterated_dyadic_physical_count.pdf){#fig:summary width="\\textwidth"}

The floating pilot resolves one eigenvalue inside $\Gamma$ at each of the two larger dimensions. Their approximate locations are

$$-0.0994035212675-0.4441920040123i$$

and

$$-0.0994142875185-0.4441895651018i,$$

with displacement $1.10391\times10^{-5}$. Residuals are below $1.3\times10^{-15}$. These values help visualize the theorem but do not certify the count.

The second-to-first block ratios are

$$0.249921,\quad0.500046,\quad0.500031,\quad0.250024.$$

The self-energy and full effective perturbation ratios are respectively $0.249974$ and $0.249957$. This is consistent with a first-order decay of cross channels and a second-order decay of consistency/detail errors under one additional dyadic refinement. It is evidence for a possible multilevel estimate, not a proof of one. A genuine induction would have to control:

1.  the block ratios uniformly over all sufficiently fine grids;

2.  the growth of the recursively propagated nonnormal resolvent;

3.  the number and quality of direct base-grid centers needed to cover the full contour; and

4.  the relation of the stored finite matrices to a continuum operator.

The present theorem closes one additional finite level and isolates these remaining obstructions quantitatively.

# Archive and reproducibility {#sec:archive}

The archive separates proof inputs from diagnostics.

-   The exact $A_{8192}$ sparse factor object is stored separately from four rank-$96$ center archives. Every file is below the repository's single-file limit. The hash of the original monolithic construction snapshot and every constituent array hash are retained.

-   The second block certificate records factor Gram defects, singular scale uppers, full residual Frobenius uppers, and residual hashes.

-   The direct center archive contains 170 inherited and 13 additional rigorous $A_{2048}$ center bounds.

-   The 324-leaf CSV ledger records exact rational endpoints, center transport data, first effective products, propagated $A_{4096}$ bounds, and second continuation products.

-   A final JSON certificate composes object identity, detail exclusion, inherited count, exact partition, and both Rouché gates.

The fast verification sequence is

    python -m pytest -q -p no:cacheprovider
    python experiments/build_final_certificate.py
    python experiments/build_archive.py
    MPLBACKEND=Agg python experiments/make_figures.py
    latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
    cp main.pdf iterated-dyadic-physical-count.pdf
    python experiments/verify_archive.py

Recomputing the componentwise second-level residual certificate is the most expensive replay step. It is run by

    OPENBLAS_NUM_THREADS=32 OMP_NUM_THREADS=32 \
    python experiments/run_second_dyadic_block_certificate.py \
      --chunk-size 128

The theorem is intentionally narrow. It compares exact finite stored binary64 matrices at one Gaussian width. It does not enclose discretization error relative to a continuum transfer operator, prove an arbitrary-grid limit, move $\sigma$ toward zero, identify a zeta zero, construct a self-adjoint Hilbert--Pólya operator, or imply the Riemann hypothesis.

# Conclusion

The $4096\to8192$ physical count continuation closes without a direct $4096$-dimensional inverse atlas. The decisive step is the exact first-level block inverse, which turns a tightened direct $A_{2048}$ atlas into a rigorous $A_{4096}$ resolvent atlas. Combined with the quarter-scale second effective perturbation, this yields a final product $0.740919<1$ and the certified three-grid count chain

$$N_{\Gamma}(A_{2048})=N_{\Gamma}(A_{4096})=N_{\Gamma}(A_{8192})=1.$$

The result does not yet establish multilevel convergence, but it converts the next question from "can one afford another direct atlas?" to the more structural problem of proving uniform block decay and hierarchical resolvent control.
