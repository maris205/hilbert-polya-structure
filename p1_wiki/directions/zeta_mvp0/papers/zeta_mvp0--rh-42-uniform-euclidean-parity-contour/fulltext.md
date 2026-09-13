---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-42-uniform-euclidean-parity-contour"
canonical_tex: "zeta_mvp0/papers/RH-42-uniform-euclidean-parity-contour/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-42-uniform-euclidean-parity-contour/uniform-euclidean-parity-contour.pdf"
source_sha256: "de8853aaf8e8e0fbdc24dfe5d97e8303997ec5a11eeed1a03f6724bae2913062"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Uniform Euclidean Isolation of a Negative Parity Resonance A Hilbert--Galerkin Lift from the Continuum Operator to Fixed-Width and Adaptive Sparse Nyström Families

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-42-uniform-euclidean-parity-contour>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-42-uniform-euclidean-parity-contour/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-42-uniform-euclidean-parity-contour/uniform-euclidean-parity-contour.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-42-uniform-euclidean-parity-contour/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-42-uniform-euclidean-parity-contour/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  A preceding continuum certificate isolated one algebraically simple negative resonance of a folded-Gaussian Markov operator at fixed noise $\sigma=10^{-2}$, but its explicit resolvent bound was in $L^\infty$. The weighted-Riesz and hard-cutoff program still required a dimension-uniform Euclidean contour theorem for midpoint matrices. We close that Hilbert-space gate.

  At the exact first band-merging parameter $$u_{\mathrm c}^3-2u_{\mathrm c}^2+2u_{\mathrm c}-2=0,$$ let $\mathcal K$ be the continuum-normalized folded-Gaussian Markov operator and put $$c=-0.9865481927458079,\qquad r=0.05,\qquad
   \Gamma=\{z\in\mathbb C:|z-c|=r\}.$$ We prove $$\sup_{z\in\Gamma}\left\lVert (z-\mathcal K)^{-1}\right\rVert_{L^2\to L^2}
   \le266.6496824500989,$$ and the disk contains exactly one eigenvalue counted algebraically. It is real, negative, and simple.

  The finite-to-continuum proof starts with a new Euclidean Grushin certificate for the exact stored binary64 matrix at dimension $4096$. Outward $1$- and $\infty$-norm residuals imply a bordered $2$-norm residual below $1.181\times10^{-10}$, a reduced inverse upper $15.101$, and a stored contour-resolvent upper $84.008$. A 224-bit Arb Frobenius calculation bridges the stored matrix to the exact-parameter continuum-normalized midpoint matrix with spectral defect at most $1.056\times10^{-5}$.

  For the analytic lift, every target integral in the Hilbert--Schmidt derivative norms is evaluated in closed form; only one source integral remains for Arb validation. A midpoint-average Peano kernel with norm $h^{3/2}/\sqrt{320}$ yields a second-order Euclidean midpoint-to-Galerkin defect. Orthogonal cell averages give exact coarse consistency, while Poincaré--Wirtinger gives explicit Hilbert Haar blocks. Four Schur steps $4096\to65536$ have maximum product $0.149114$; the final Galerkin-to-continuum product is $0.576723$.

  Consequently, for every $n\ge131072$, the exact continuum-normalized midpoint matrices, the exactly discretely normalized full Markov matrices, and both the fixed eight-sigma and adaptive sparse matrices have algebraic count one inside $\Gamma$. Uniform Euclidean contour-resolvent uppers are $837.124$, $838.211$, and $838.211$, respectively. The fixed window is uniformly tiny in Euclidean norm even though its row-norm defect has the nonzero floor proved previously. The schedule $L_n=\max\{8,2\sqrt{\log n}\}$ additionally restores the $O(n^{-2}(\log n)^{-1/4})$ cutoff rate and closes the second-order weighted-Riesz transfer. No uniform theorem for every binary64 transcendental evaluation, zero-noise limit, zeta-zero identification, self-adjoint Hilbert--Pólya operator, or Riemann-hypothesis claim is made.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Uniform Euclidean Isolation of a Negative Parity Resonance\
  A Hilbert--Galerkin Lift from the Continuum Operator\
  to Fixed-Width and Adaptive Sparse Nyström Families
```

## Markdown 正文

# Introduction {#sec:introduction}

The nested-grid spectral program for the noisy quadratic map $f_u(x)=1-ux^2$ separates three logically different questions. First, one must certify a finite-dimensional spectral count. Second, that count must survive an infinite refinement and reach a continuum operator. Third, the smooth full-kernel theorem must be transferred to the sparse support rule used in computation.

The first two questions were developed through finite contour counts, dyadic Schur continuation, smooth-kernel Haar decay, and a validated continuum contour [@WangNested2026; @WangHaar2026; @WangContinuumContour2026]. At $\sigma=10^{-2}$ the last paper proved that the full continuum operator has one algebraically simple real negative resonance inside a specified circle, together with an explicit $L^\infty$ resolvent bound. This closed the simple-isolated parity premise of the gauge-free weighted-Riesz theorem [@WangRiesz2026].

One norm mismatch remained. The weighted-Riesz cutoff estimate is naturally stated in Euclidean matrix norm, and nonnormal resolvents cannot be moved between $\ell^\infty$ and $\ell^2$ by dimension-dependent norm equivalence. The inequality $$\left\lVert X\right\rVert_2\le\sqrt n\,\left\lVert X\right\rVert_\infty$$ is useless in an all-grid theorem. A genuine Hilbert-space argument is required [@TrefethenEmbree2005].

The support analysis of @WangCutoff2026 already provides the last perturbation once such a resolvent is available. If $P_n$ is the full discretely normalized folded-Gaussian matrix and $P_n^{(L)}$ its renormalized support truncation, then $$\left\lVert P_n^{(L)}-P_n\right\rVert_2$$ has a dimension-uniform Frobenius upper. For fixed $L=8$ this upper is extraordinarily small but need not vanish. For $L_n=2\sqrt{\log n}$ it is $O(n^{-2}(\log n)^{-1/4})$. Thus the missing object is a uniform Euclidean contour for the full matrix family.

This paper supplies that object. Its contributions are:

1.  a Euclidean version of the one-center Grushin certificate, obtained by combining outward $1$- and $\infty$-norm inverse residuals;

2.  a 224-bit exact-stored Frobenius bridge to the exact continuum midpoint matrix;

3.  closed target-variable formulas for all Hilbert--Schmidt derivative norms, reducing rigorous integration to one source variable;

4.  an explicit second-order midpoint-to-cell-average theorem based on the exact Peano-kernel constant $1/\sqrt{320}$;

5.  orthogonal Hilbert Haar and Schur bounds through dimension $65536$;

6.  a continuum $L^2$ contour theorem and an all-dimension Euclidean theorem from $n=131072$ onward; and

7.  unconditional Euclidean contour conditioning for both the fixed eight-sigma family and a growing support schedule, with the latter restoring the second-order weighted-Riesz rate.

Three evidence levels remain distinct.

Analytic theorem

:   Hilbert projection identities, Poincaré and Peano inequalities, Schur continuation, normalization, cutoff, and weighted-Riesz perturbation.

Outward certificate

:   Exact stored binary64 residuals, 224-bit Frobenius sums, and 160-bit Arb integrals.

Floating diagnostic

:   High-order Gauss--Legendre values used only to display the sharp scale of the Hilbert constants.

# Operator, matrices, and main results {#sec:model}

Let $u_{\mathrm c}$ be the unique real root in $(1.5,1.6)$ of $$p(u)=u^3-2u^2+2u-2.$$ Fix $\sigma=1/100$ and $$m(x)=1-u_{\mathrm c}x^2.$$ For $0\le x,y\le1$, define $$g(x,y)=
 \exp\!\left[-\frac{(y-m(x))^2}{2\sigma^2}\right]
 +
 \exp\!\left[-\frac{(y+m(x))^2}{2\sigma^2}\right],$$ $$Z(x)=\int_0^1g(x,y)\,dy,\qquad
 k(x,y)=\frac{g(x,y)}{Z(x)}.$$ The continuum Markov operator is $$(\mathcal Kf)(x)=\int_0^1k(x,y)f(y)\,dy.
 \label{eq:continuum}$$ Its smooth kernel defines a compact operator on every $L^p([0,1])$, $1\le p\le\infty$.

For $n\ge2$, put $h=1/n$ and $x_i=y_i=(i+\tfrac12)h$. The continuum-normalized midpoint matrix is $$(M_n)_{ij}=h\,k(x_i,y_j).
 \label{eq:midpoint}$$ The exactly discretely normalized full Markov matrix is $$(P_n)_{ij}
 =\frac{g(x_i,y_j)}{\sum_{q=0}^{n-1}g(x_i,y_q)}
 =h\frac{g(x_i,y_j)}{Z_n(x_i)},
 \qquad
 Z_n(x)=h\sum_qg(x,y_q).
 \label{eq:full-matrix}$$

For a declared support multiple $L>0$, define $$H_n(L)=\lceil L\sigma n\rceil+2,\qquad
 a_i=|m(x_i)|,\qquad
 c_i=\left\lfloor\frac{a_i}{h}-\frac12\right\rfloor.$$ Retain the columns satisfying $|j-c_i|\le H_n(L)$, clip to $0\le j<n$, and renormalize each retained row. The resulting exact-real sparse matrix is denoted $P_n^{(L)}$. We study both $L=8$ and $$L_n=\max\{8,2\sqrt{\log n}\}.
 \label{eq:adaptive-schedule}$$

The contour is $$c=-0.9865481927458079,\qquad
 r=0.05,\qquad
 \Gamma=\{z\in\mathbb C:|z-c|=r\}.
 \label{eq:contour}$$ Its minimum and maximum moduli obey $$\rho_\Gamma\ge0.9365481927458077,\qquad
 R_\Gamma\le1.036548192745808.$$

[\[thm:continuum\]]{#thm:continuum label="thm:continuum"} The exact operator [\[eq:continuum\]](#eq:continuum){reference-type="eqref" reference="eq:continuum"} on $L^2([0,1])$ satisfies $$\Gamma\subset\rho(\mathcal K),\qquad
 \sup_{z\in\Gamma}\left\lVert (z-\mathcal K)^{-1}\right\rVert_{2\to2}
 \le266.6496824500989.$$ The Riesz projection inside $\Gamma$ has rank one. The enclosed eigenvalue is real, negative, and algebraically simple.

[\[thm:uniform\]]{#thm:uniform label="thm:uniform"} For every integer $n\ge131072$, each of the matrices $$M_n,\qquad P_n,\qquad P_n^{(8)},\qquad P_n^{(L_n)}$$ has exactly one eigenvalue inside $\Gamma$, counted with algebraic multiplicity. It is real, negative, and simple. Uniformly in $n$, $$\begin{aligned}
 \sup_{z\in\Gamma}\left\lVert (z-M_n)^{-1}\right\rVert_2
 &\le837.1238351518642,
 \label{eq:midpoint-uniform}\\
 \sup_{z\in\Gamma}\left\lVert (z-P_n)^{-1}\right\rVert_2
 &\le838.2106715223996,
 \label{eq:full-uniform}\\
 \sup_{z\in\Gamma}\left\lVert (z-P_n^{(8)})^{-1}\right\rVert_2,\quad
 \sup_{z\in\Gamma}\left\lVert (z-P_n^{(L_n)})^{-1}\right\rVert_2
 &\le838.2106716588748.
 \label{eq:sparse-uniform}\end{aligned}$$

[\[cor:riesz\]]{#cor:riesz label="cor:riesz"} Let $$\mathcal Q(A;\Gamma)
 =\frac{1}{2\pi i}\int_\Gamma z(z-A)^{-1}\,dz.$$ For every $n\ge131072$, $$\left\lVert \mathcal Q(P_n^{(8)};\Gamma)-\mathcal Q(P_n;\Gamma)\right\rVert_2
 \le7.073141188685013\times10^{-9}.$$ The same uniform upper holds for $P_n^{(L_n)}$, and after the growing branch of [\[eq:adaptive-schedule\]](#eq:adaptive-schedule){reference-type="eqref" reference="eq:adaptive-schedule"} begins, $$\left\lVert \mathcal Q(P_n^{(L_n)};\Gamma)-\mathcal Q(P_n;\Gamma)\right\rVert_2
 =
 O\!\left(n^{-2}(\log n)^{-1/4}\right).$$ Thus the uniform Euclidean contour premise of the RH-40 parity weighted-Riesz bridge is closed for the exact-real sparse family.

The proofs occupy [\[sec:stored,sec:composition,sec:sparse\]](#sec:stored,sec:composition,sec:sparse){reference-type="ref" reference="sec:stored,sec:composition,sec:sparse"}.

# Orthogonal Galerkin geometry in $L^2$ {#sec:hilbert}

Let $I_i=[ih,(i+1)h)$ and let $V_n$ be the space of functions constant on these cells. Conditional expectation $P_n^{\mathrm G}:L^2\to V_n$ is the orthogonal projection. In the orthonormal basis $$e_i=h^{-1/2}\mathbf1_{I_i},$$ the finite-rank operator $$\mathcal A_n=P_n^{\mathrm G}\mathcal KP_n^{\mathrm G}$$ is represented by $$(A_n)_{ij}
 =\frac1h\int_{I_i}\int_{I_j}k(x,y)\,dy\,dx.
 \label{eq:galerkin}$$ Thus the standard Euclidean matrix norm of $A_n$ is exactly its operator norm on $V_n$. The same basis identifies the piecewise-constant lift of $M_n$ with the matrix norm in [\[eq:midpoint-uniform\]](#eq:midpoint-uniform){reference-type="eqref" reference="eq:midpoint-uniform"}; no factor of $\sqrt n$ appears.

[\[lem:poincare\]]{#lem:poincare label="lem:poincare"} For $f\in H^1([0,1])$, $$\left\lVert f-P_n^{\mathrm G}f\right\rVert_{L^2}
 \le\frac h\pi\left\lVert f'\right\rVert_{L^2}.$$

Apply the sharp mean-zero Poincaré inequality on every cell and sum the squares.

For a smooth kernel, write $$K_x=\left\lVert \partial_xk\right\rVert_{L^2([0,1]^2)},\qquad
 K_y=\left\lVert \partial_yk\right\rVert_{L^2([0,1]^2)},$$ and similarly $K_{xx},K_{xy},K_{yy},K_{xxyy}$.

[\[prop:continuum-defect\]]{#prop:continuum-defect label="prop:continuum-defect"} $$\left\lVert \mathcal K-P_n^{\mathrm G}\mathcal KP_n^{\mathrm G}\right\rVert_{2\to2}
 \le\frac h\pi(K_x+K_y).
 \label{eq:continuum-defect}$$

Decompose $$\mathcal K-P_n^{\mathrm G}\mathcal KP_n^{\mathrm G}
 =(\mathrm I-P_n^{\mathrm G})\mathcal K
 +P_n^{\mathrm G}\mathcal K(\mathrm I-P_n^{\mathrm G}).$$ The first term is bounded by the Hilbert--Schmidt norm of $(\mathrm I-P_n^{\mathrm G})_xk$, and [\[lem:poincare\]](#lem:poincare){reference-type="ref" reference="lem:poincare"} gives $hK_x/\pi$. Apply the same argument to the transposed kernel for the second term.

The dyadic fine space splits orthogonally as $$V_{2n}=V_n\oplus W_n,$$ where $W_n$ consists of the alternating constants on the two half-cells of each coarse cell. In this basis, $$\mathcal A_{2n}=
 \begin{pmatrix}
 \mathcal A_n&B_n\\
 C_n&D_n
 \end{pmatrix}.
 \label{eq:hilbert-blocks}$$ The upper-left block is exactly $\mathcal A_n$ by the tower property of conditional expectation.

[\[prop:hilbert-blocks\]]{#prop:hilbert-blocks label="prop:hilbert-blocks"} $$\left\lVert C_n\right\rVert_2\le\frac h\pi K_x,\qquad
 \left\lVert B_n\right\rVert_2\le\frac h\pi K_y,\qquad
 \left\lVert D_n\right\rVert_2\le\frac{h^2}{\pi^2}K_{xy}.
 \label{eq:hilbert-block-bounds}$$

The detail projection is dominated by $\mathrm I-P_n^{\mathrm G}$. One application of [\[lem:poincare\]](#lem:poincare){reference-type="ref" reference="lem:poincare"} in the source variable gives $C_n$; one application in the target variable gives $B_n$. Applying the inequality in both variables to the Hilbert--Schmidt kernel gives $D_n$.

[\[lem:schur\]]{#lem:schur label="lem:schur"} Suppose $$\sup_{z\in\Gamma}\left\lVert (z-\mathcal A_n)^{-1}\right\rVert_2\le M.$$ Put $$b=\left\lVert B_n\right\rVert_2,\quad q=\left\lVert C_n\right\rVert_2,\quad d=\left\lVert D_n\right\rVert_2,\quad
 R_d=(\rho_\Gamma-d)^{-1}.$$ If $d<\rho_\Gamma$ and $$M\,bR_dq<1,
 \label{eq:schur-gate}$$ then $\mathcal A_n$ and $\mathcal A_{2n}$ have the same algebraic count inside $\Gamma$. Set $$S=\frac{M}{1-MbR_dq}.$$ The fine resolvent is bounded by the Euclidean norm of the scalar matrix $$\begin{pmatrix}
 S&SbR_d\\
 R_dqS&R_d+R_dqSbR_d
 \end{pmatrix},
 \label{eq:block-majorant}$$ and hence by its Frobenius norm.

Take the Schur complement of $z-D_n$. The self-energy is bounded by $bR_dq$, so [\[eq:schur-gate\]](#eq:schur-gate){reference-type="eqref" reference="eq:schur-gate"} gives the Schur inverse. The four inverse blocks are majorized by [\[eq:block-majorant\]](#eq:block-majorant){reference-type="eqref" reference="eq:block-majorant"}. For count preservation, use the homotopy $$\begin{pmatrix}\mathcal A_n&tB_n\\tC_n&tD_n\end{pmatrix},
 \qquad0\le t\le1.$$ Every majorant is largest at $t=1$, so the contour remains invertible throughout.

Because $P_n^{\mathrm G}$ is orthogonal, the finite-rank operator $\mathcal A_n$ acts as zero on $(V_n)^\perp$. Therefore a matrix contour upper $M_n$ lifts to $$\sup_{z\in\Gamma}\left\lVert (z-\mathcal A_n)^{-1}\right\rVert_{2\to2}
 \le\max\{M_n,\rho_\Gamma^{-1}\}.
 \label{eq:orthogonal-zero-complement}$$

# A second-order Euclidean midpoint theorem {#sec:midpoint-theorem}

The bridge between [\[eq:midpoint\]](#eq:midpoint){reference-type="eqref" reference="eq:midpoint"} and [\[eq:galerkin\]](#eq:galerkin){reference-type="eqref" reference="eq:galerkin"} needs a second-order matrix estimate with an explicit Hilbert constant.

[\[lem:peano\]]{#lem:peano label="lem:peano"} On an interval $[-h/2,h/2]$, define $$\mathcal L_hf=f(0)-\frac1h\int_{-h/2}^{h/2}f(t)\,dt.$$ Then $$\mathcal L_hf=\int_{-h/2}^{h/2}\mathscr P_h(s)f''(s)\,ds,
\qquad
 \mathscr P_h(s)
 =-\frac{(h/2-|s|)^2}{2h},$$ and $$\left\lVert \mathscr P_h\right\rVert_{L^2}=\frac{h^{3/2}}{\sqrt{320}}.
 \label{eq:peano-norm}$$

The functional annihilates affine functions. Its second-order Peano kernel is obtained by applying it to $(t-s)_+$. Direct integration gives the displayed formula and $$2\int_0^{h/2}\frac{(h/2-s)^4}{4h^2}\,ds
 =\frac{h^3}{320}.$$

[\[thm:midpoint-galerkin\]]{#thm:midpoint-galerkin label="thm:midpoint-galerkin"} The matrices [\[eq:midpoint\]](#eq:midpoint){reference-type="eqref" reference="eq:midpoint"} and [\[eq:galerkin\]](#eq:galerkin){reference-type="eqref" reference="eq:galerkin"} satisfy $$\left\lVert M_n-A_n\right\rVert_2
 \le
 \frac{h^2}{\sqrt{320}}(K_{xx}+K_{yy})
 +\frac{h^4}{320}K_{xxyy}.
 \label{eq:midpoint-galerkin-bound}$$

On each cell rectangle write midpoint evaluation as average plus the Peano functional in each variable: $$E_xE_y-A_xA_y
 =\mathcal L_xA_y+A_x\mathcal L_y+\mathcal L_x\mathcal L_y.$$ By [\[lem:peano\]](#lem:peano){reference-type="ref" reference="lem:peano"}, Jensen's inequality in the averaged variable gives the cellwise bound $$|(E_xE_y-A_xA_y)k|
 \le
 \frac h{\sqrt{320}}
 \left(\left\lVert k_{xx}\right\rVert_{L^2(R)}+\left\lVert k_{yy}\right\rVert_{L^2(R)}\right)
 +\frac{h^3}{320}\left\lVert k_{xxyy}\right\rVert_{L^2(R)}.$$ The matrix Frobenius norm is $h$ times the Euclidean sum of these cell errors. Minkowski's inequality over all cells yields [\[eq:midpoint-galerkin-bound\]](#eq:midpoint-galerkin-bound){reference-type="eqref" reference="eq:midpoint-galerkin-bound"}, and spectral norm is bounded by Frobenius norm.

The fourth mixed derivative appears only with $h^4$. A deliberately coarse validated upper is therefore sufficient.

# Euclidean stored and Arb continuum bridges {#sec:stored}

## The exact stored Grushin problem

Let $P_{4096}^{\mathrm s}$ be the exact stored binary64 sparse Markov matrix from the RH-36 snapshot. With the archived approximate right and left parity modes $r_0,\ell_0$, center $c$, and scale $s=16$, define $$\mathcal G(z)=
 \begin{pmatrix}
 z\mathrm I-P_{4096}^{\mathrm s}&sr_0\\
 s^{-1}\ell_0^T&0
 \end{pmatrix}.$$ The one-center Grushin--Rouché argument is the same algebraic mechanism as in @WangContinuumContour2026; only the certified norm changes.

For a square matrix $X$ and residual $R=\mathrm I-\mathcal G(c)X$, $$\left\lVert X\right\rVert_2\le\sqrt{\left\lVert X\right\rVert_1\left\lVert X\right\rVert_\infty},\qquad
 \left\lVert R\right\rVert_2\le\sqrt{\left\lVert R\right\rVert_1\left\lVert R\right\rVert_\infty}.$$ If $\left\lVert R\right\rVert_2<1$, then $$\left\lVert \mathcal G(c)^{-1}\right\rVert_2
 \le\frac{\left\lVert X\right\rVert_2}{1-\left\lVert R\right\rVert_2}.$$ The same $1$--$\infty$ majorant is applied to the reduced block and to the right and left mode residuals. Every row and column sum is recomputed against the exact stored graph using componentwise outward arithmetic [@Rump2010; @WangOutward2026].

::: {#tab:grushin}
  quantity                                                                             rigorous value
  ------------------------------------------------------------ --------------------------------------
  bordered residual $\left\lVert R\right\rVert_2$                $\le1.180516523852333\times10^{-10}$
  approximate bordered inverse $\left\lVert X\right\rVert_2$                  $\le102.16148968743643$
  exact bordered inverse                                                      $\le102.16148969949678$
  center reduced inverse                                                      $\le15.100231161690903$
  center transport product                                                     $\le0.755011558084546$
  right mode residual                                            $\le3.106104383879701\times10^{-13}$
  left mode residual                                             $\le1.233253262479696\times10^{-12}$
  effective scalar boundary lower                                           $\ge0.049999999999652434$
  stored Euclidean contour resolvent                                            $\le84.0073245249997$

  : Exact-stored Euclidean Grushin ledger at dimension $4096$.
:::

The transport product is below one, and the scalar error $3.475\times10^{-13}$ is smaller than the affine boundary lower. Scalar Rouché [@Ahlfors1979; @SjoestrandZworski2007] therefore proves one stored eigenvalue and the last line of [1](#tab:grushin){reference-type="ref" reference="tab:grushin"}.

## Exact stored-to-midpoint Frobenius bridge

At 224-bit precision [@Johansson2017] the exact critical root is enclosed by the same $2\times10^{-60}$ interval used in the continuum certificate. The archived support geometry is constant throughout that interval. On every retained entry, the stored binary64 value is subtracted from the exact Arb midpoint entry and the square is accumulated. For omitted nonnegative entries, $$\sum_{j\notin S_i}(M_{4096})_{ij}^2
 \le
 \left(\sum_{j\notin S_i}(M_{4096})_{ij}\right)^2.$$ The uniform omitted mass is below $1.905\times10^{-15}$.

[\[prop:stored-midpoint\]]{#prop:stored-midpoint label="prop:stored-midpoint"} $$\left\lVert P_{4096}^{\mathrm s}-M_{4096}\right\rVert_2
 \le
 \left\lVert P_{4096}^{\mathrm s}-M_{4096}\right\rVert_{\mathrm F}
 \le1.055416712190961\times10^{-5}.
 \label{eq:stored-midpoint-defect}$$

The corresponding Neumann product is $$84.0073245249997
 \times1.055416712190961\times10^{-5}
 \le8.866273425013429\times10^{-4}.$$ Hence $M_{4096}$ has count one and contour-resolvent upper $84.08187381333138$.

## Validated Hilbert--Schmidt envelope

Direct two-dimensional interval integration is unnecessary. Every derivative used here has the form $$Dk(x,y)=\frac{
 P_+(y;x)e^{-(y-m(x))^2/(2\sigma^2)}
 +P_-(y;x)e^{-(y+m(x))^2/(2\sigma^2)}
 }{Z(x)},
 \label{eq:polynomial-gaussian-form}$$ where $P_\pm$ are polynomials of degree at most two, except for the deliberately coarse fourth mixed derivative.

Squaring [\[eq:polynomial-gaussian-form\]](#eq:polynomial-gaussian-form){reference-type="eqref" reference="eq:polynomial-gaussian-form"} gives two shifted Gaussian square terms and one cross term: $$\int_0^1(Dk)^2dy
 =Z(x)^{-2}\left\{
 I(P_+^2,m)+I(P_-^2,-m)
 +2e^{-m^2/\sigma^2}I(P_+P_-,0)
 \right\},$$ where $$I(P,a)=\int_0^1P(y)e^{-(y-a)^2/\sigma^2}\,dy.$$ For polynomial degree at most four, these integrals are exact combinations of endpoint exponentials and error functions. Arb therefore validates only the remaining source integral in $x$.

::: {#tab:hilbert-envelope}
  quantity                                                Arb norm upper
  ----------------------------------- ----------------------------------
  $\left\lVert k\right\rVert_{L^2}$                  $5.498549224049740$
  $K_x$                                              $669.4643679578433$
  $K_y$                                              $382.5709390570679$
  $K_{xx}$                                          $196077.82378278425$
  $K_{xy}$                                           $82003.43867251626$
  $K_{yy}$                                           $47446.59748497963$
  $K_{xxyy}$                            $1.444104830885426\times10^{10}$

  : Validated Hilbert--Schmidt derivative envelope. The $xxyy$ bound is intentionally coarse because it is multiplied by $h^4/320$.
:::

The first six interval values agree with an independent floating Gauss--Legendre calculation to the displayed scale. The floating values are diagnostic only.

# Hilbert continuation to the continuum {#sec:composition}

and [2](#tab:hilbert-envelope){reference-type="ref" reference="tab:hilbert-envelope"} give $$\left\lVert M_{4096}-A_{4096}\right\rVert_2
 \le0.0008115839277660032.$$ Its product with the transferred midpoint resolvent is $0.06823949740334896<1$, so $$\sup_{z\in\Gamma}\left\lVert (z-A_{4096})^{-1}\right\rVert_2
 \le90.23979185532137.$$

Four applications of [\[lem:schur\]](#lem:schur){reference-type="ref" reference="lem:schur"} now give [3](#tab:schur-chain){reference-type="ref" reference="tab:schur-chain"}.

::: {#tab:schur-chain}
  step                $\left\lVert C\right\rVert_2$   $\left\lVert B\right\rVert_2$   $\left\lVert D\right\rVert_2$   Schur product   fine resolvent
  ----------------- ------------------------------- ------------------------------- ------------------------------- --------------- ----------------
  $4096\to8192$            $5.20257{\times}10^{-2}$        $2.97305{\times}10^{-2}$        $4.95236{\times}10^{-4}$      $0.149114$      $106.27837$
  $8192\to16384$           $2.60128{\times}10^{-2}$        $1.48652{\times}10^{-2}$        $1.23809{\times}10^{-4}$     $0.0438867$      $111.21915$
  $16384\to32768$          $1.30064{\times}10^{-2}$        $7.43262{\times}10^{-3}$        $3.09523{\times}10^{-5}$     $0.0114806$      $112.53042$
  $32768\to65536$          $6.50321{\times}10^{-3}$        $3.71631{\times}10^{-3}$        $7.73807{\times}10^{-6}$    $0.00290392$      $112.86684$

  : Orthogonal Hilbert Schur continuation.
:::

The orthogonal zero-complement bound [\[eq:orthogonal-zero-complement\]](#eq:orthogonal-zero-complement){reference-type="eqref" reference="eq:orthogonal-zero-complement"} does not enlarge the last matrix constant. At $n=65536$, $$\left\lVert \mathcal K-\mathcal A_{65536}\right\rVert_{2\to2}
 \le0.005109760114093718.$$ The final product is $$112.86683027872749
 \times0.005109760114093718
 \le0.5767224275624271<1,$$ and the transferred resolvent is $$\frac{112.86683027872749}{1-0.5767224275624271}
 \le266.6496824500989.$$

The exact-stored Grushin count transfers through [\[prop:stored-midpoint\]](#prop:stored-midpoint){reference-type="ref" reference="prop:stored-midpoint"}, [\[thm:midpoint-galerkin\]](#thm:midpoint-galerkin){reference-type="ref" reference="thm:midpoint-galerkin"}, the four Schur steps, and the final continuum Neumann gate. Thus the $L^2$ Riesz projection has rank one and the displayed resolvent upper holds.

The kernel and contour are real and conjugation invariant. Count one therefore forces the enclosed eigenvalue to be real, while the circle lies strictly in the negative half-plane. Algebraic count one makes it simple. For completeness, every nonzero $L^2$ eigenfunction satisfies $f=\lambda^{-1}\mathcal Kf$ and is continuous; the same smoothing applies to generalized eigenvectors. Hence this is the same nonzero continuum resonance isolated in $L^\infty$ by @WangContinuumContour2026.

# From the continuum to full and sparse matrices {#sec:sparse}

## The exact continuum-normalized midpoint family

Combining [\[eq:continuum-defect,eq:midpoint-galerkin-bound\]](#eq:continuum-defect,eq:midpoint-galerkin-bound){reference-type="ref" reference="eq:continuum-defect,eq:midpoint-galerkin-bound"} gives $$\left\lVert \mathcal K-\widetilde M_n\right\rVert_{2\to2}
 \le
 \frac{K_x+K_y}{\pi n}
 +\frac{K_{xx}+K_{yy}}{\sqrt{320}\,n^2}
 +\frac{K_{xxyy}}{320\,n^4}.
 \label{eq:continuum-midpoint-family}$$ At $n=131072$, the right side is $0.002555672463059059$. Its product with the continuum resolvent is $0.6814692507211605<1$, giving $$\sup_{z\in\Gamma}\left\lVert (z-M_n)^{-1}\right\rVert_2
 \le837.1238351518642$$ for every $n\ge131072$, because the defect decreases with $n$.

## Discrete row normalization

The continuum normalizer has the exact uniform lower $$Z_{\min}
 =
 \sigma\sqrt{\frac\pi2}
 \operatorname{erf}\!\left(\frac{\sqrt2}{\sigma}\right)
 \ge0.012533141373155001.
 \label{eq:normalizer-lower}$$ Indeed, the Gaussian mass of $[-1,1]$ is minimized when its mean is at an endpoint.

For one unnormalized Gaussian, $$\int_\mathbb R
 \left|
 \frac{d^2}{dy^2}
 e^{-(y-a)^2/(2\sigma^2)}
 \right|dy
 =
 \frac{4e^{-1/2}}{\sigma}.$$ There are two folded terms. The integrated midpoint remainder therefore gives $$\sup_x|Z_n(x)-Z(x)|
 \le\frac{e^{-1/2}}{\sigma n^2}.
 \label{eq:normalizer-error}$$ Since $$P_n=\operatorname{diag}\!\left(\frac{Z(x_i)}{Z_n(x_i)}\right)M_n,$$ $$\left\lVert P_n-M_n\right\rVert_2
 \le
 \frac{\delta_n}{Z_{\min}-\delta_n}
 \left(\left\lVert k\right\rVert_{L^2}
       +\left\lVert M_n-A_n\right\rVert_2\right),
 \quad
 \delta_n=\frac{e^{-1/2}}{\sigma n^2}.
 \label{eq:normalization-defect}$$ At $n=131072$, this is at most $$1.548892476215473\times10^{-6},$$ and the corresponding Neumann product is $$0.001296614809927365,$$ proving [\[eq:full-uniform\]](#eq:full-uniform){reference-type="eqref" reference="eq:full-uniform"}.

## Fixed and growing support

The exact cutoff theorem of @WangCutoff2026 uses the effective support multiple $\Lambda_n\ge L$ and gives $$\begin{aligned}
 Q_n&=
 \frac{2e^{1/2}e^{-\Lambda_n^2/2}}
      {\sigma-h}
 \left(h+\frac{\sigma}{\Lambda_n}\right),\\
 \left\lVert P_n^{(L)}-P_n\right\rVert_2
 &\le\varepsilon_n
 =\sqrt{\Omega_n+\mathcal R_n},\end{aligned}$$ with explicit omitted and renormalization square terms. Replacing $\Lambda_n$ by its lower bound $L$ gives a rigorous relaxation.

At $n=131072$ and $L=8$, $$\varepsilon_n
 \le1.942434811504516\times10^{-13}.$$ For fixed $L=8$, every factor in the relaxed upper is nonincreasing as $n$ grows. Thus the same number is uniform for all $n\ge131072$. Its resolvent product is only $$1.628169587739687\times10^{-10},$$ which proves the fixed-width part of [\[eq:sparse-uniform\]](#eq:sparse-uniform){reference-type="eqref" reference="eq:sparse-uniform"}.

For [\[eq:adaptive-schedule\]](#eq:adaptive-schedule){reference-type="eqref" reference="eq:adaptive-schedule"}, $L_n\ge8$, so the same uniform theorem holds. Once $2\sqrt{\log n}>8$, $$e^{-L_n^2/2}\le n^{-2},\qquad
 e^{-L_n^2}\le n^{-4}.$$ The RH-39 formulas then give $$\varepsilon_n
 =O\!\left(n^{-2}(\log n)^{-1/4}\right).$$

The continuum-to-midpoint, normalization, and cutoff defects are monotone for $n\ge131072$. At the threshold their Neumann products are respectively $0.6814693$, $0.0012967$, and $1.629\times10^{-10}$. Each homotopy therefore keeps $\Gamma$ in the resolvent set and preserves Riesz rank one. The successive resolvent uppers are exactly [\[eq:midpoint-uniform\]](#eq:midpoint-uniform){reference-type="eqref" reference="eq:midpoint-uniform"}--[\[eq:sparse-uniform\]](#eq:sparse-uniform){reference-type="eqref" reference="eq:sparse-uniform"}. Reality, negativity, and simplicity follow as in [\[thm:continuum\]](#thm:continuum){reference-type="ref" reference="thm:continuum"}.

For two operators sharing $\Gamma$, the first resolvent identity gives $$\left\lVert \mathcal Q(A;\Gamma)-\mathcal Q(B;\Gamma)\right\rVert
 \le
 rR_\Gamma M_AM_B\left\lVert A-B\right\rVert.$$ Insert [\[eq:full-uniform\]](#eq:full-uniform){reference-type="eqref" reference="eq:full-uniform"} and [\[eq:sparse-uniform\]](#eq:sparse-uniform){reference-type="eqref" reference="eq:sparse-uniform"}, together with the cutoff upper at the threshold. This gives $7.073141188685013\times10^{-9}$. Under the growing schedule, the two resolvents remain uniformly bounded while the perturbation has the displayed adaptive rate.

The fixed eight-sigma family has a nonzero row-operator defect floor [@WangCutoff2026]; it is not a full-kernel $L^\infty$ approximation. Nevertheless its Euclidean cutoff defect is uniformly below $2\times10^{-13}$, which is more than sufficient for spectral isolation. Adaptive growth is needed not for the count, but for convergence of the sparse weighted term to the full-kernel weighted term at second order.

![The Euclidean contour closure. (a) Rigorous resolvent uppers from the exact stored matrix through the continuum and the all-grid sparse family. (b) All seven nonnormal transfer products are below one. (c) Closed target integrals and one-dimensional Arb validation give tight Hilbert--Schmidt constants except for the harmless $h^4$ derivative. (d) A fixed eight-sigma cutoff stays uniformly tiny in Euclidean norm, while adaptive growth begins at $n=e^{16}$ and restores decay.](<../../../../../zeta_mvp0/papers/RH-42-uniform-euclidean-parity-contour/figures/uniform_euclidean_parity_contour.pdf>){#fig:summary width="\\textwidth"}

# What is closed and what remains {#sec:boundary}

The norm hierarchy can now be stated without ambiguity.

1.  **Continuum parity isolation holds in both $L^\infty$ and $L^2$.** The present Hilbert certificate is independent of dimension-changing norm equivalence.

2.  **The exact full midpoint family has a uniform Euclidean contour.** From $n=131072$ onward, the full discretely normalized matrices have count one and resolvent upper $838.211$.

3.  **The fixed archived support rule preserves the count.** Its Euclidean perturbation is uniformly tiny even though its row defect does not vanish.

4.  **Adaptive support closes the second-order weighted-Riesz bridge.** The uniform contour and the RH-39 cutoff rate now satisfy every premise of the RH-40 perturbation theorem.

5.  **Exact-real and binary64 families remain distinct.** The $4096$ stored binary64 matrix is fully covered by the Grushin and Arb ledgers. The all-dimension theorem concerns the exact-real Gaussian formulas; it does not enclose every future transcendental binary64 evaluation.

6.  **Noise is still fixed.** The Hilbert derivative constants grow rapidly as $\sigma\downarrow0$. No uniform small-noise statement follows from this paper.

The result does not produce a self-adjoint generator, a $T\log T$ counting law, an arithmetic trace formula, a zeta-zero identification, or the Riemann hypothesis. It closes a functional-analytic discretization gate at one positive noise width.

# Archive and reproducibility {#sec:archive}

The archive contains four rigorous ledgers:

1.  the exact-stored Euclidean Grushin certificate;

2.  the 224-bit stored-to-midpoint Frobenius bridge;

3.  the 160-bit Hilbert--Schmidt envelope; and

4.  the complete Galerkin, continuum, normalization, and cutoff composition certificate.

The floating Gauss--Legendre pilot is archived separately and is never used as proof.

The complete replay is:

    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      -m pytest -q -p no:cacheprovider
    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/run_euclidean_grushin_certificate.py
    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/build_euclidean_midpoint_bridge.py
    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/build_hilbert_envelope_certificate.py
    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/build_uniform_euclidean_certificate.py
    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/estimate_hilbert_constants.py
    MPLBACKEND=Agg PYTHONDONTWRITEBYTECODE=1 \
      /root/math/.venv/bin/python experiments/make_figures.py
    latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
    cp main.pdf uniform-euclidean-parity-contour.pdf
    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/build_archive.py
    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/verify_archive.py

Every consumed cross-paper input, local source, result ledger, figure, and publication artifact is recorded by SHA-256.

# Conclusion

The continuum parity contour now has a dimension-uniform Hilbert-space realization. Exact stored Euclidean residuals start the count, Arb bridges the binary64 matrix to the analytic midpoint kernel, closed Gaussian moments validate the Hilbert envelope, and orthogonal Galerkin--Schur continuation reaches the continuum. Direct perturbation then controls every sufficiently fine full and sparse midpoint matrix in the same Euclidean norm.

The fixed eight-sigma window and the adaptive window play different roles. Fixed width is already uniformly harmless for the spectral count. Adaptive growth is what restores convergence of the sparse weighted term to the full continuum branch. This distinction closes the final norm condition left by the weighted-Riesz paper without conflating row and Euclidean topology.
