---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-33-certified-complement-resolvent-atlas"
canonical_tex: "zeta_mvp0/papers/RH-33-certified-complement-resolvent-atlas/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-33-certified-complement-resolvent-atlas/certified-complement-resolvent-atlas.pdf"
source_sha256: "562975b2fc5bcc69eb0d4db0b2a27d5683ecf0942b9acd18afc20dca06f2b049"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Certified Complement-Resolvent Atlas and a Relative Contour Count Full-Boundary Rouché Closure for a 2048-Dimensional Stored Quadratic Band-Merging Model

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-33-certified-complement-resolvent-atlas>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-33-certified-complement-resolvent-atlas/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-33-certified-complement-resolvent-atlas/certified-complement-resolvent-atlas.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-33-certified-complement-resolvent-atlas/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-33-certified-complement-resolvent-atlas/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  An end-to-end certificate ledger for a finite packet--complement spectral model left two independent gates: a validated complement-resolvent bound on the complete contour, and an interior count of complement poles. This paper closes the first gate at the stored scale $\sigma=10^{-2}$.

  Let $M$ be the stored sparse one-step matrix, $U=M-R_{\rm p}\Lambda L_{\rm p}^{\mathsf T}$, $Q=\mathrm I-VW$, and $B=QU^2Q$. No exact idempotence of the stored $Q$ is assumed. For $A(z)=z\mathrm I-B$, we use the unlifted two-step linearization $$\mathcal L_t(z)=
   \begin{pmatrix}z\mathrm I&-tQU\\-t^{-1}UQ&\mathrm I\end{pmatrix}.$$ Its leading inverse block is $A(z)^{-1}$. The off-diagonal factors are a sparse $M$ block plus $2p+2m=12$ peripheral and packet channels. A bordered Grushin realization therefore has dimension $4108$ when the physical dimension is $2048$.

  At each of 109 contour centers, sparse LU is used only to generate a binary64 trial right inverse $\mathcal R_j$. The exact stored-factor graph then independently encloses $\mathrm I-A(z_j)\mathcal R_j$ componentwise. All 109 residual Frobenius bounds are below $5.747\times10^{-9}$, and the resulting rigorous inverse bounds range from $50.486$ to $553.228$. These local certificates are transported with 256-bit Arb arithmetic to an exact rational cover. Of 936 inherited RH-28 parent arcs, 933 close without further subdivision; the remaining three close after dyadic refinement. The final cover has 949 leaves, no gap, and no unresolved leaf. Its largest rigorous Neumann product is $0.999870853<1$, while the largest transported-bound-to-RH-28-budget ratio is $2.107\times10^{-11}$.

  Consequently the RH-28 matrix Rouché inequality holds on the entire stored circle. Combining this with the independently certified RH-32 projected winding gives $\operatorname{wind}_\Gamma\det F=1$ for the exact stored Feshbach function. Moreover, for the exact augmented block realization $$\mathcal M_{\rm st}=\begin{pmatrix}D&E\\C&B\end{pmatrix},$$ the Schur determinant identity yields the rigorous relative count $$N_\Gamma(\mathcal M_{\rm st})-N_\Gamma(B)=1.$$ This is a full-boundary and relative-count theorem, not an ordinary one-zero theorem: the interior complement count remains open. No continuum limit, Hilbert--Pólya construction, zeta-zero identification, Riemann-hypothesis implication, or one-eigenvalue claim for the original physical discretization is made.
author:
- |
  Liang Wang\
  School of Artificial Intelligence and Automation,\
  Huazhong University of Science and Technology, Wuhan 430074, P.R. China\
  `wangliang.f@gmail.com`
bibliography:
- references.bib
date: July 2026
title: |
  **A Certified Complement-Resolvent Atlas and a\
  Relative Contour Count**\
  Full-Boundary Rouché Closure for a 2048-Dimensional\
  Stored Quadratic Band-Merging Model
```

## Markdown 正文

**Keywords:** complement resolvent; certified atlas; Grushin problem; Feshbach map; matrix Rouché theorem; verified numerical linear algebra; nonnormal spectrum.

**MSC 2020:** 15A18; 47A10; 47A11; 47A55; 65F05; 65F35; 65F50; 65G20; 65P30.

# Introduction {#sec:introduction}

The contour program considered here studies a finite noisy transfer matrix near a quadratic band-merging parameter. A small packet block is retained, the ambient complement is eliminated by a Feshbach map, and a rational Arnoldi realization supplies a tractable projected determinant. Successive papers made the comparison more explicit: primal--dual identities isolated the complement inverse, outward arithmetic enclosed the stored residuals, and exact rational arcs replaced sampled contour nodes [@WangContourFeshbach2026; @WangOutwardCode2026; @WangArcwise2026].

The remaining inverse problem is genuinely nonnormal. A one-channel lift and sparse two-step Grushin linearization certified selected centers, while a threshold-inertia route provided independent local certificates [@WangDeflated2026; @WangSparseGrushin2026; @WangThresholdInertia2026]. The end-to-end ledger then made the limitation precise: one selected center reached only one RH-28 arc, so it could not be promoted to a complete contour theorem [@WangLedger2026].

The natural next object is not one especially sharp center but a finite *resolvent atlas*. Each chart consists of a validated inverse bound at one center together with the neighborhood reached by the resolvent identity. Compactness suggests that finitely many charts should cover a pole-free boundary; the difficulty is to certify every chart without assembling the dense square $QU^2Q$ or trusting a computed smallest singular value.

This paper implements that route at $\sigma=10^{-2}$. Its contributions are:

1.  an unlifted sparse two-step Grushin realization with exact physical inverse block $A(z)^{-1}$ and only $2p+2m$ low-rank channels;

2.  109 deterministic all-column Frobenius--Neumann certificates whose residuals are reevaluated against the exact stored-factor target;

3.  a rational adaptive atlas that may place new centers inside RH-28 parent arcs rather than only at archived parent midpoints;

4.  a 256-bit Arb transport audit proving a complete 949-leaf cover of the stored circle;

5.  full-boundary activation of the RH-28 matrix Rouché inequality;

6.  an exact winding-one theorem for the stored Feshbach function and an exact augmented-block-minus-complement eigenvalue count of one; and

7.  an explicit separation of that relative count from the still-open interior complement count.

The evidence hierarchy is maintained throughout.

-   Schur complements, low-rank channel identities, the resolvent transport, boundary homotopy, and relative count are exact algebra.

-   Center residuals and the final atlas are rigorous computer-assisted results for exact serialized binary64 inputs under the stated IEEE arithmetic assumptions.

-   Sparse LU factors and timings are computational devices and diagnostics. No floating singular value is used as an upper bound.

# Exact stored Feshbach function and relative count {#sec:stored-model}

Fix the stored scale $\sigma=10^{-2}$ and let $n=2048$. The serialized factors are interpreted componentwise as exact dyadic real or complex numbers. Let $M\in\mathbb C^{n\times n}$ be the sparse one-step matrix, let $R_{\rm p},L_{\rm p}\in\mathbb C^{n\times p}$ with $p=2$ be the stored peripheral factors, and let $\Lambda\in\mathbb C^{p\times p}$ contain their stored values. Put $$U=M-R_{\rm p}\Lambda L_{\rm p}^{\mathsf T}.
 \label{eq:stored-u}$$ The packet synthesis and analysis matrices are $V\in\mathbb C^{n\times m}$ and $W\in\mathbb C^{m\times n}$ with $m=4$, and $$Q=\mathrm I-VW.
 \label{eq:stored-q}$$ As in the outward-rounded stored-factor model, no exact idempotence of $Q$ is assumed. Define $$B=QU^2Q,\qquad C=QU^2V,\qquad D=WU^2V,\qquad E=WU^2Q.
 \label{eq:stored-blocks}$$ For $$A(z)=z\mathrm I_n-B,
 \label{eq:complement-shift}$$ the exact stored Feshbach function is $$F(z)=z\mathrm I_m-D-EA(z)^{-1}C
 \label{eq:stored-feshbach}$$ wherever $A(z)$ is invertible.

Even without assuming that $Q$ is a projector, this rational function has an exact block realization. Set $$\mathcal M_{\rm st}=
 \begin{pmatrix}
  D&E\\ C&B
 \end{pmatrix}
 \in\mathbb C^{(m+n)\times(m+n)}.
 \label{eq:stored-augmented-block}$$

[\[prop:stored-schur\]]{#prop:stored-schur label="prop:stored-schur"} For $z\notin\operatorname{spec}B$, $$\det(z\mathrm I_{m+n}-\mathcal M_{\rm st})=\det A(z)\det F(z).
 \label{eq:stored-schur-determinant}$$ If a positively oriented simple contour $\Gamma$ meets neither $\operatorname{spec}B$ nor $\operatorname{spec}\mathcal M_{\rm st}$, then $$\operatorname{wind}_\Gamma\det F=N_\Gamma(\mathcal M_{\rm st})-N_\Gamma(B).
 \label{eq:stored-relative-count}$$

The matrix $z\mathrm I_{m+n}-\mathcal M_{\rm st}$ has block form $$\begin{pmatrix}
  z\mathrm I_m-D&-E\\ -C&z\mathrm I_n-B
 \end{pmatrix}.$$ Taking the Schur complement of $A(z)=z\mathrm I_n-B$ gives [\[eq:stored-schur-determinant\]](#eq:stored-schur-determinant){reference-type="ref" reference="eq:stored-schur-determinant"}. Both determinants in the quotient are polynomials, so the scalar argument principle gives [\[eq:stored-relative-count\]](#eq:stored-relative-count){reference-type="ref" reference="eq:stored-relative-count"} [@Ahlfors1979; @HornJohnson2013].

[\[rem:augmented-scope\]]{#rem:augmented-scope label="rem:augmented-scope"} The matrix $\mathcal M_{\rm st}$ is the exact finite block realization of the stored function [\[eq:stored-feshbach\]](#eq:stored-feshbach){reference-type="ref" reference="eq:stored-feshbach"}. If $WV=\mathrm I_m$ exactly, it is the usual oblique-coordinate representation of the physical two-step operator. The serialized stored model does not assume that exact identity, so the present paper does not silently identify $\mathcal M_{\rm st}$ with the original physical discretization.

The projected rational Feshbach function $F_J$ and the circle $\Gamma$ are inherited from RH-28. RH-32 reconstructed the exact RH-28 base realization, enclosed all augmented and pole eigenvalues with 256-bit Arb arithmetic, and proved at the present scale that $$\operatorname{wind}_\Gamma\det F_J=1,\qquad
 \det F_J(z)\ne0\quad(z\in\Gamma).
 \label{eq:projected-winding-one}$$ The circle has stored center and radius $$c=-0.3233504401504541-0.5508412474453575i,\qquad
 R=0.2624987592858511.
 \label{eq:stored-circle}$$ The task below is to transfer [\[eq:projected-winding-one\]](#eq:projected-winding-one){reference-type="ref" reference="eq:projected-winding-one"} to $F$ on the entire boundary.

# Unlifted sparse two-step Grushin realization {#sec:grushin}

For $t>0$ and a spectral parameter $z$, define $$\mathcal L_t(z)=
 \begin{pmatrix}
  z\mathrm I_n&-tQU\\
  -t^{-1}UQ&\mathrm I_n
 \end{pmatrix}.
 \label{eq:two-step-linearization}$$

[\[lem:physical-inverse\]]{#lem:physical-inverse label="lem:physical-inverse"} The Schur complement of the lower-right identity in [\[eq:two-step-linearization\]](#eq:two-step-linearization){reference-type="ref" reference="eq:two-step-linearization"} is $A(z)$. Consequently $\mathcal L_t(z)$ is invertible if and only if $A(z)$ is invertible, and $$_{11}=A(z)^{-1}.
 \label{eq:leading-inverse-block}$$

The Schur complement is $$z\mathrm I_n-(-tQU)(-t^{-1}UQ)=z\mathrm I_n-QU^2Q=A(z).$$ The block inverse formula gives [\[eq:leading-inverse-block\]](#eq:leading-inverse-block){reference-type="ref" reference="eq:leading-inverse-block"}.

The dense-looking factors $QU$ and $UQ$ are low-rank corrections of the sparse matrix $M$. Write $C_{\rm p}=R_{\rm p}\Lambda$. Exact algebra gives $$\begin{aligned}
 M-QU&=C_{\rm p}L_{\rm p}^{\mathsf T}+V(WU),
 \label{eq:top-correction}\\
 M-UQ&=C_{\rm p}L_{\rm p}^{\mathsf T}+(UV)W.
 \label{eq:bottom-correction}\end{aligned}$$ Define the sparse base $$\mathcal L_{0,t}(z)=
 \begin{pmatrix}
  z\mathrm I_n&-tM\\
  -t^{-1}M&\mathrm I_n
 \end{pmatrix}.
 \label{eq:sparse-base}$$ Equations [\[eq:top-correction,eq:bottom-correction\]](#eq:top-correction,eq:bottom-correction){reference-type="ref" reference="eq:top-correction,eq:bottom-correction"} express $\mathcal L_t(z)-\mathcal L_{0,t}(z)$ as $XY$ with $$X\in\mathbb C^{2n\times r},\qquad Y\in\mathbb C^{r\times2n},\qquad r=2p+2m=12.
 \label{eq:channel-rank}$$ The explicit channels are listed in [10](#app:channels){reference-type="ref" reference="app:channels"}.

[\[thm:sparse-grushin\]]{#thm:sparse-grushin label="thm:sparse-grushin"} Let $$\mathcal G_t(z)=
 \begin{pmatrix}
  \mathcal L_{0,t}(z)&X\\
  Y&-\mathrm I_r
 \end{pmatrix}.
 \label{eq:bordered-grushin}$$ Let $J_n:\mathbb C^n\to\mathbb C^{2n+r}$ inject into the first $n$ coordinates. Then $\mathcal G_t(z)$ is invertible if and only if $A(z)$ is invertible, and $$J_n^*\mathcal G_t(z)^{-1}J_n=A(z)^{-1}.
 \label{eq:grushin-physical-block}$$ The bordered dimension is $2n+2p+2m=4108$.

The Schur complement of $-\mathrm I_r$ is $\mathcal L_{0,t}(z)+XY=\mathcal L_t(z)$. Hence the leading $2n$ inverse block of $\mathcal G_t(z)^{-1}$ is $\mathcal L_t(z)^{-1}$. Apply [\[lem:physical-inverse\]](#lem:physical-inverse){reference-type="ref" reference="lem:physical-inverse"} to its first $n$ coordinates.

Each channel may be balanced by multiplying its column and dividing its row by the same nonzero scalar. This preserves $XY$ and the physical inverse block. The implementation chooses the square root of the row-to-column Euclidean norm ratio. The choice affects sparse factorization quality, not the target of the final certificate [@Davis2006; @WangSparseGrushin2026].

# Direct exact-target center certificates {#sec:center-certificates}

At a center $z_j$, a binary64 sparse LU factorization of $\mathcal G_1(z_j)$ solves $$\widehat{\mathcal G}_1(z_j)x_k=J_ne_k,\qquad k=1,\ldots,n.
 \label{eq:trial-solves}$$ Retaining the first $n$ coordinates produces a stored trial matrix $\mathcal R_j\in\mathbb C^{n\times n}$. Neither the rounded assembly nor the LU factors are asserted to be exact.

[\[thm:frobenius-neumann\]]{#thm:frobenius-neumann label="thm:frobenius-neumann"} Let $T,R\in\mathbb C^{n\times n}$. If rigorous bounds $\rho,\varepsilon$ satisfy $$\left\lVert R\right\rVert_F\leq\rho,\qquad
 \left\lVert\mathrm I-TR\right\rVert_F\leq\varepsilon<1,
 \label{eq:fn-inputs}$$ then $T$ is invertible and $$\left\lVert T^{-1}\right\rVert_2\leq\frac{\rho}{1-\varepsilon}.
 \label{eq:fn-bound}$$

Let $\Delta=\mathrm I-TR$. Since $\left\lVert\Delta\right\rVert_2\leq\left\lVert\Delta\right\rVert_F<1$, the Neumann lemma makes $\mathrm I-\Delta$ invertible and $T[R(\mathrm I-\Delta)^{-1}]=\mathrm I$. A square matrix with a right inverse is invertible. Therefore $$\left\lVert T^{-1}\right\rVert_2
 \leq\left\lVert R\right\rVert_2\left\lVert(\mathrm I-\Delta)^{-1}\right\rVert_2
 \leq\frac{\left\lVert R\right\rVert_F}{1-\left\lVert\Delta\right\rVert_F}.$$ Apply [\[eq:fn-inputs\]](#eq:fn-inputs){reference-type="ref" reference="eq:fn-inputs"}.

For the present target, the stored-factor graph reevaluates $$X\longmapsto z_jX-Q\bigl(U(U(QX))\bigr)
 \label{eq:exact-target-action}$$ componentwise with one outward complex-disc radius per entry. Sparse and dense dot products use conservative Higham $\gamma_k$ factors, and every positive bound operation is rounded outward [@Higham2002; @Rump2010]. Thus the residual $$\Delta_j=\mathrm I-A(z_j)\mathcal R_j
 \label{eq:center-residual}$$ is enclosed against the exact stored target, not against the rounded Schur complement of the sparse LU matrix.

The 2048 physical columns are processed in chunks of 256. Chunk Frobenius bounds are combined by an outward square root of the sum of squares. The center bound is $$M_j=\frac{\rho_j}{1-\varepsilon_j},\qquad
 \rho_j\geq\left\lVert\mathcal R_j\right\rVert_F,\quad
 \varepsilon_j\geq\left\lVert\Delta_j\right\rVert_F.
 \label{eq:center-bound}$$

::: {#tab:center-certificates}
  quantity                                                       certified or archived value
  ------------------------------------------ -----------------------------------------------
  physical dimension $n$                                                                2048
  packet rank $m$; peripheral rank $p$                                               $4;\ 2$
  border rank $r$; bordered dimension                                            $12;\ 4108$
  bordered matrix nonzeros                                                         1,290,892
  LU nonzeros, minimum--maximum                                         3,672,780--3,672,782
  number of center certificates                                                          109
  $\rho_j$, minimum--maximum                                           50.485781--553.227390
  $\varepsilon_j$, minimum--maximum            $1.1195\times10^{-10}$--$5.7464\times10^{-9}$
  $M_j$, minimum--maximum                                              50.485781--553.227394
  factor time per center                                                        2.26--2.36 s
  exact-target certificate time per center                                    27.15--31.35 s

  : Stored sparse realization and all-center certificate ranges. The time entries are per center; the runs were performed in parallel batches.
:::

[\[thm:center-inverses\]]{#thm:center-inverses label="thm:center-inverses"} Assume the archived binary64 factors are exact inputs and IEEE round-to-nearest arithmetic has no overflow or harmful underflow. Every one of the 109 archived center certificates is admissible. In particular, $$50.485780584110735\leq M_j\leq553.2273931275126,
 \qquad j=1,\ldots,109,
 \label{eq:center-range}$$ and each $A(z_j)$ is invertible.

For every center, the archived all-column calculation gives $\varepsilon_j<5.747\times10^{-9}<1$. Apply [\[thm:frobenius-neumann\]](#thm:frobenius-neumann){reference-type="ref" reference="thm:frobenius-neumann"} to $T=A(z_j)$ and $R=\mathcal R_j$. The displayed extrema are the outward bounds in the committed center manifest.

# Adaptive rational resolvent atlas {#sec:atlas}

The RH-28 boundary consists of 936 accepted parent arcs with exact rational turn endpoints. Parent $a$ lies on $$\gamma(\theta)=c+Re^{i\theta}
 \label{eq:circle-parameterization}$$ and is enclosed by a stored disc $\overline{\mathbb D}(\zeta_a,r_a)$. It carries a downward conditional budget $L_a^-$ such that $$\sup_{z\in a}\left\lVert A(z)^{-1}\right\rVert_2<L_a^-
 \label{eq:rh28-resolvent-gate}$$ activates the RH-28 matrix Rouché inequality on that parent [@WangArcwise2026].

[\[lem:chart-transport\]]{#lem:chart-transport label="lem:chart-transport"} Suppose $\left\lVert A(z_j)^{-1}\right\rVert_2\leq M_j$. Let a target disc have center $\zeta$ and radius $r$, and put $$d=|\zeta-z_j|+r.
 \label{eq:chart-distance}$$ If $dM_j<1$, then every $z$ in the target disc satisfies $$\left\lVert A(z)^{-1}\right\rVert_2\leq\frac{M_j}{1-dM_j}.
 \label{eq:chart-transport}$$

Since $A(z)=A(z_j)+(z-z_j)\mathrm I$, factor $$A(z)=A(z_j)\bigl[\mathrm I+(z-z_j)A(z_j)^{-1}\bigr].$$ The Neumann lemma applies for $|z-z_j|M_j<1$, and every point of the target disc has $|z-z_j|\leq d$.

All quantities in [\[eq:chart-distance,eq:chart-transport\]](#eq:chart-distance,eq:chart-transport){reference-type="ref" reference="eq:chart-distance,eq:chart-transport"} are evaluated with 256-bit Arb arithmetic. Each binary64 real and imaginary component, disc radius, center bound, and parent budget is embedded as its exact dyadic value. A target closes only when the upper Arb product is strictly below one and the upper transported bound is strictly below the exact dyadic lower budget. Thus the final atlas does not rely on a plotted distance or a single-successor approximation to a Euclidean norm [@Johansson2017].

## Adaptive construction

The construction begins with 64 approximately angle-uniform RH-28 parent midpoints. Additional parent midpoints are inserted at uncovered runs, giving 88 parent-center certificates. At that point a parent-only strategy becomes inefficient: a large parent can fail as one disc even when smaller subarcs are locally coverable.

The adaptive stage performs the following exact rational loop.

1.  Bisect every unresolved parent leaf up to a prescribed extra depth.

2.  Merge adjacent unresolved leaves by exact rational endpoint equality, including the $0/1$ turn seam.

3.  Place one new center at the rational-turn midpoint of each connected unresolved component.

4.  Certify every new center by [\[thm:frobenius-neumann\]](#thm:frobenius-neumann){reference-type="ref" reference="thm:frobenius-neumann"} and repeat.

The first gap round contributes 13 centers and the second contributes 8. Hence the final atlas consists of 88 parent midpoints and 21 adaptive gap-midpoints. Every one of the 109 centers is used by at least one final leaf.

## Complete cover

The final exact partition contains 949 leaves. Of the 936 original parents, 933 are accepted whole. Parents 691, 754, and 892 require subdivision; the maximum extra depth actually used is six. Sorting all final rational intervals gives first endpoint $0$, exact pairwise endpoint equality, and last endpoint $1$.

::: {#tab:atlas}
  quantity                                                                        rigorous value
  --------------------------------------------- ------------------------------------------------
  RH-28 parent arcs                                                                          936
  whole parents closed                                                                       933
  final rational leaves                                                                      949
  unresolved leaves                                                                            0
  center charts                                                                              109
  maximum extra refinement used                                                                6
  maximum Neumann product upper                                               0.9998708523281207
  minimum Neumann denominator lower                            $1.2914767187932605\times10^{-4}$
  transported inverse upper, minimum--maximum                               121.930--801,137.545
  RH-28 budget lower, minimum--maximum            $3.97259\times10^{13}$--$6.76045\times10^{19}$
  maximum transported-bound/budget ratio                                 $2.10638\times10^{-11}$
  minimum budget margin factor                                            $4.74748\times10^{10}$

  : Final complement-resolvent atlas at $\sigma=10^{-2}$. Every displayed extremum is taken from the outward leaf ledger.
:::

[\[thm:full-atlas\]]{#thm:full-atlas label="thm:full-atlas"} Under the stored-model and arithmetic assumptions of [\[thm:center-inverses\]](#thm:center-inverses){reference-type="ref" reference="thm:center-inverses"}, the exact rational leaves form a complete cover of $\Gamma$. For each leaf $\ell$ there exists an archived center $z_j$ such that $$\sup_{z\in\ell}\left\lVert A(z)^{-1}\right\rVert_2
 \leq\frac{M_j}{1-d_{j\ell}M_j}
 <L_{p(\ell)}^-,
 \label{eq:leaf-closure}$$ where $p(\ell)$ is its RH-28 parent. In particular, $A(z)$ is invertible for every $z\in\Gamma$.

Every center bound follows from [\[thm:center-inverses\]](#thm:center-inverses){reference-type="ref" reference="thm:center-inverses"}. For each of the 949 ledger rows, the 256-bit Arb upper product is strictly below one, so [\[lem:chart-transport\]](#lem:chart-transport){reference-type="ref" reference="lem:chart-transport"} applies. Its upper transported bound is strictly below the inherited downward parent budget. Exact rational endpoint checks show that the leaves cover one complete turn without gaps or overlaps.

![Top left: the 109 rigorous center inverse bounds, with adaptive gap-midpoints concentrated near the nonnormal peak. Bottom left: every exact-target Frobenius residual remains far below one. Top right: all 949 leafwise Neumann products are rigorously below one. Bottom right: the transported bounds remain many orders of magnitude below the RH-28 conditional budgets.](<../../../../../zeta_mvp0/papers/RH-33-certified-complement-resolvent-atlas/figures/certified_resolvent_atlas.pdf>){#fig:atlas width="99%"}

# Full-boundary Rouché closure and relative winding {#sec:rouche}

For each RH-28 parent, the outward primal--dual theorem gives constants $\bar\eta_a<1$ and $\bar c_a>0$ with $$\left\lVert F_J(z)^{-1}(F(z)-F_J(z))\right\rVert_2
 \leq \bar\eta_a+\bar c_a\left\lVert A(z)^{-1}\right\rVert_2,\qquad z\in a,
 \label{eq:rh28-bound}$$ and the inherited budget is $$L_a^-=\operatorname{down}\frac{1-\bar\eta_a}{\bar c_a}.
 \label{eq:rh28-budget}$$ Every refined leaf is a subset of its parent, so the parent constants remain valid on it.

[\[thm:full-rouche\]]{#thm:full-rouche label="thm:full-rouche"} On the complete stored circle, $$\left\lVert F_J(z)^{-1}(F(z)-F_J(z))\right\rVert_2<1,\qquad z\in\Gamma.
 \label{eq:full-rouche}$$ Consequently $F(z)$ is invertible on $\Gamma$ and $$\operatorname{wind}_\Gamma\det F=\operatorname{wind}_\Gamma\det F_J=1.
 \label{eq:stored-winding-one}$$

By [\[thm:full-atlas\]](#thm:full-atlas){reference-type="ref" reference="thm:full-atlas"}, every point lies in a leaf whose transported inverse upper bound is below the corresponding parent budget. Substitution into [\[eq:rh28-bound,eq:rh28-budget\]](#eq:rh28-bound,eq:rh28-budget){reference-type="ref" reference="eq:rh28-bound,eq:rh28-budget"} gives [\[eq:full-rouche\]](#eq:full-rouche){reference-type="ref" reference="eq:full-rouche"} on each leaf and hence on $\Gamma$.

For $s\in[0,1]$, define $$F_s(z)=F_J(z)+s(F(z)-F_J(z))
 =F_J(z)\bigl[\mathrm I+sF_J(z)^{-1}(F(z)-F_J(z))\bigr].$$ The second factor is invertible by the Neumann lemma, uniformly on the boundary. Thus $\det F_s$ is a nonvanishing boundary homotopy, so its winding is constant in $s$. Apply the independently certified projected winding [\[eq:projected-winding-one\]](#eq:projected-winding-one){reference-type="ref" reference="eq:projected-winding-one"}; equivalently one may invoke the boundary form of matrix Rouché theory [@GohbergSigal1971].

The theorem uses only boundary invertibility and a boundary homotopy. It does not assume that $F$ is holomorphic throughout the disk.

[\[cor:relative-count\]]{#cor:relative-count label="cor:relative-count"} For the exact stored matrices $B$ and $\mathcal M_{\rm st}$, $$N_\Gamma(\mathcal M_{\rm st})-N_\Gamma(B)=1.
 \label{eq:relative-count-one}$$ In particular, $\mathcal M_{\rm st}$ has at least one eigenvalue in the circle, counted algebraically.

The atlas excludes $\operatorname{spec}B$ from the boundary. The full Rouché inequality and [\[eq:projected-winding-one\]](#eq:projected-winding-one){reference-type="ref" reference="eq:projected-winding-one"} exclude zeros of $\det F$ from the boundary. Hence [\[prop:stored-schur\]](#prop:stored-schur){reference-type="ref" reference="prop:stored-schur"} applies, and [\[eq:stored-winding-one\]](#eq:stored-winding-one){reference-type="ref" reference="eq:stored-winding-one"} gives [\[eq:relative-count-one\]](#eq:relative-count-one){reference-type="ref" reference="eq:relative-count-one"}. Since $N_\Gamma(B)$ is a nonnegative integer, $N_\Gamma(\mathcal M_{\rm st})=N_\Gamma(B)+1\geq1$.

[\[rem:not-one-zero\]]{#rem:not-one-zero label="rem:not-one-zero"} The rational function $F$ may have poles at interior complement eigenvalues. If $q=N_\Gamma(B)$, the present theorem gives $N_\Gamma(\mathcal M_{\rm st})=q+1$ and boundary winding one. It gives exactly one augmented eigenvalue, or exactly one ordinary zero of $\det F$, only after proving $q=0$.

# Provenance, reproducibility, and evidence level {#sec:reproducibility}

The committed archive contains one JSON record for every center. Each record stores the center, sparse dimensions, LU fill, $\rho_j$, $\varepsilon_j$, $M_j$, timings, and SHA-256 hashes of the streamed trial inverse, residual centers, and residual radii. The aggregate center table and manifest contain 109 rows and verify that every center certificate is admissible.

The leaf ledger contains all 949 final rational intervals, the winning center identifier, the Arb distance upper bound, Neumann product upper bound, transported inverse upper bound, inherited budget lower bound, and their ratio. Independent archive tests reconstruct the exact rational partition from integer endpoints and require every row to be closed.

The dependency manifest hashes the consumed RH-28 arc and scale archives, the RH-32 projected count, the RH-27 componentwise arithmetic and factor graph, the RH-28 rational geometry, and the RH-30 Frobenius--Neumann helper. These hashes establish object provenance; they do not replace the mathematical assumptions of the source theorems.

The rigorous computation concerns exact dyadic inputs. It assumes the standard IEEE round-to-nearest model used by the outward arithmetic, with no overflow or harmful underflow. Sparse LU is outside the trusted base: any LU error merely changes the trial matrix and is remeasured by the exact-target residual.

# Scope, limitations, and next gate {#sec:limitations}

The paper proves four concrete statements at $\sigma=10^{-2}$:

1.  109 exact-target center inverse bounds for the stored complement family;

2.  a complete rational boundary resolvent atlas;

3.  the full RH-28 matrix Rouché inequality on the stored circle; and

4.  stored Feshbach winding one and augmented-block-minus-complement count one.

The following statements are not proved.

1.  The interior complement count $N_\Gamma(B)$ is not known. Therefore no ordinary one-zero count for $F$ and no exactly-one count for $\mathcal M_{\rm st}$ follows.

2.  Because exact idempotence of the serialized $Q$ is not assumed, the augmented stored block is not silently identified with the original physical two-step discretization. Such an identification would need an exact packet-pair correction or a separate perturbation theorem.

3.  The same full atlas has not been computed at $\sigma=4\times10^{-3}$ or smaller scales. The all-column certificate has quadratic-like cost, although the sparse factorization itself remains favorable at the next stored scale.

4.  The stored finite factors are not enclosed relative to an exact Gaussian integral operator, exact critical constants, or a zero-noise limit.

5.  No self-adjoint Hilbert--Pólya operator, prime-power trace formula, zeta-zero identification, or statement about the Riemann hypothesis is obtained.

The immediate spectral gate is now narrower than in RH-32. Boundary resolvent control is no longer missing at the coarsest stored scale. What remains is an interior complement count. Natural routes include a contour argument principle for the complement determinant, a pole-free homotopy, a validated sparse inertia count for an interior family, or a Schur self-energy exclusion. Each route addresses a different question from adding more boundary centers [@SjoestrandZworski2007; @TrefethenEmbree2005].

# Conclusion {#sec:conclusion}

A single local inverse bound could not traverse the RH-28 contour. A finite atlas can. The practical reason is that sparse LU need not be validated as a factorization: it only proposes local right inverses, while the exact stored-factor graph certifies every residual independently. Exact rational gap geometry then places new centers only where previous charts fail.

At $\sigma=10^{-2}$, 109 charts cover the full boundary. This closes the conditional resolvent gate left by RH-28 and RH-32, promotes projected winding one to exact stored Feshbach winding one, and yields an exact relative count for the augmented stored block. The result does not jump the last wall. Interior complement poles still decide whether relative count one becomes an ordinary one-zero theorem. That distinction is the next problem, not a caveat to be hidden by numerical evidence.

# Explicit low-rank channels {#app:channels}

Write a channel column as $x=(x_{\rm top},x_{\rm bottom})^{\mathsf T}$ and a channel row as $y=(y_{\rm left},y_{\rm right})$. The $2p+2m$ channels in [\[eq:channel-rank\]](#eq:channel-rank){reference-type="ref" reference="eq:channel-rank"} are $$\begin{aligned}
 x_{{\rm tp},k}&=(t(C_{\rm p})_k,0)^{\mathsf T},
 &y_{{\rm tp},k}&=(0,(L_{\rm p}^{\mathsf T})_k),\\
 x_{{\rm tk},k}&=(tV_k,0)^{\mathsf T},
 &y_{{\rm tk},k}&=(0,(WU)_k),\\
 x_{{\rm bp},k}&=(0,t^{-1}(C_{\rm p})_k)^{\mathsf T},
 &y_{{\rm bp},k}&=((L_{\rm p}^{\mathsf T})_k,0),\\
 x_{{\rm bk},k}&=(0,t^{-1}(UV)_k)^{\mathsf T},
 &y_{{\rm bk},k}&=(W_k,0).\end{aligned}$$ The first and third families have $p$ channels; the second and fourth have $m$ channels. Summing $xy$ gives precisely the corrections in [\[eq:top-correction,eq:bottom-correction\]](#eq:top-correction,eq:bottom-correction){reference-type="ref" reference="eq:top-correction,eq:bottom-correction"}.

# Reproduction {#app:reproduction}

From this paper directory, run the fast tests and rebuild the compact archive by

    PYTHONDONTWRITEBYTECODE=1 python -m pytest -q -p no:cacheprovider
    PYTHONDONTWRITEBYTECODE=1 python experiments/build_archive.py
    MPLBACKEND=Agg python experiments/make_figures.py

The expensive center certificates are resumable. One parent-center batch is run with

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
    python experiments/run_atlas_batch.py --sigma 0.01 \
      --workers 8 --chunk-size 256 --arcs <arc identifiers>

After a partial atlas, generate rational gap midpoints and certify them by

    python experiments/audit_refined_atlas.py \
      --sigma 0.01 --max-extra-refinement 8
    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
    python experiments/run_atlas_batch.py --sigma 0.01 \
      --workers 8 --chunk-size 256 \
      --target-file results/refined_atlas_sigma_1e-02.json

The final audit is rerun until its status is `full_refined_atlas`. The manuscript is built with

    latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
