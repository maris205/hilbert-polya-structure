---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-44-validated-rank-two-peripheral-complement"
canonical_tex: "zeta_mvp0/papers/RH-44-validated-rank-two-peripheral-complement/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-44-validated-rank-two-peripheral-complement/validated-rank-two-peripheral-complement.pdf"
source_sha256: "d2354d039702996df0163f9e776d6b82512ba7f34820ee07c62cf0838bf5e71e"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Validated Intrinsic Rank-Two Peripheral Complement Perron Kernel, Spectral Haar Closure, and Exact Bulk Trace Factorization

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-44-validated-rank-two-peripheral-complement>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-44-validated-rank-two-peripheral-complement/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-44-validated-rank-two-peripheral-complement/validated-rank-two-peripheral-complement.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-44-validated-rank-two-peripheral-complement/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-44-validated-rank-two-peripheral-complement/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The negative resonance of a folded-Gaussian Markov operator has recently been converted into a validated intrinsic weighted-Riesz kernel. The other peripheral mode is the Perron eigenvalue $1$. Although strong positivity already makes that branch simple and isolated, a rank-two subtraction requires more: an explicit Euclidean contour, validated stored factors, a smooth continuum kernel, and simultaneous control of full and sparse matrix families. We close all four requirements at fixed noise $\sigma=10^{-2}$.

  For the Perron circle $|z-1|=0.05$, componentwise outward Grushin certificates prove that the stored $2048$, $4096$, and $8192$ factors are genuine spectral weighted terms, with Euclidean errors at most $2.17\times10^{-10}$, $4.22\times10^{-10}$, and $8.34\times10^{-10}$. A Hilbert--Galerkin and infinite-complement Schur continuation gives $$\sup_{|z-1|=0.05}\left\lVert (z-\mathcal K)^{-1}\right\rVert_{L^2\to L^2}
   \le81.30575843422578.$$ The corresponding weighted term is the Perron projection itself. It has the intrinsic kernel $q_+(x,y)=\pi(y)$, where $\mathcal K^*\pi=\pi$ and $\int_0^1\pi=1$. We enclose $q_+$ and its derivatives in Hilbert--Schmidt norms and place it in an $L^2([0,1]^2)$ ball of radius $1.463768820944639$ about the lifted archived $4096$ center.

  Adding the validated negative kernel $q_-$ produces a real smooth, gauge-free rank-two kernel $$q_{\mathrm{per}}(x,y)=\pi(y)+q_-(x,y).$$ The two contours are disjoint and each contains one algebraically simple eigenvalue. The actual stored rank-two Haar ratios now lie within $6.06\times10^{-4}$ of the quarter--half targets. For every $n\ge65536$, full and fixed/adaptive sparse exact-real midpoint matrices have one eigenvalue in each contour. Their union-contour Euclidean resolvent upper is $267.81252084743886$, the full-to-sparse rank-two weighted-term difference is at most $9.269128034310783\times10^{-10}$, and the intrinsically deflated difference is at most $9.271085367195988\times10^{-10}$.

  Finally, if $\mathcal B=\mathcal K-\mathcal Q_+-\mathcal Q_-$, then the Perron and parity eigenvalues are replaced by zero while the remaining spectrum is unchanged. For every $m\ge1$, $$\mathcal B^m=\mathcal K^m-\mathcal Q_+-\lambda_-^{m-1}\mathcal Q_-,
   \qquad
   \operatorname{tr}(\mathcal B^m)=\operatorname{tr}(\mathcal K^m)-1-\lambda_-^m,$$ and $$\operatorname{det}(\mathrm I-z\mathcal K)
   =(1-z)(1-z\lambda_-)\operatorname{det}(\mathrm I-z\mathcal B).$$ These are structural operator factorizations, not an arithmetic trace formula. No zero-noise, zeta-zero, self-adjoint Hilbert--Pólya, or Riemann-hypothesis claim is made.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  A Validated Intrinsic Rank-Two Peripheral Complement\
  Perron Kernel, Spectral Haar Closure, and Exact Bulk Trace Factorization
```

## Markdown 正文

# Introduction {#sec:introduction}

The first operation in a peripheral spectral analysis should be intrinsic: remove the isolated spectral terms without choosing signs, scales, or a persistent ordering of left and right eigenvectors. For a nonnormal operator $T$ and a contour $\Gamma$ in its resolvent set, the appropriate object is the weighted Riesz term $$\mathcal Q(T;\Gamma)
 =\frac{1}{2\pi i}\int_\Gamma z(z-T)^{-1}\,dz
 =T\mathcal P(T;\Gamma).
 \label{eq:weighted-riesz-intro}$$ For a simple eigenvalue $\lambda$, this is $\lambda r\ell^T/(\ell^Tr)$, but the contour formula carries no gauge.

The analytic weighted-Riesz framework of @WangRiesz2026 showed that simple isolated smooth Nyström branches have a second-order intrinsic continuum limit. Strong positivity made the Perron instance unconditional, while the negative branch still required a validated continuum contour. That negative contour was established in @WangContinuumContour2026 [@WangEuclidean2026]; the resulting weighted term was then constructed as a real smooth continuum kernel in @WangParityKernel2026. The parity paper also validated all three stored negative factors and supplied an all-grid full/sparse Euclidean contour from $n=65536$.

At first sight the Perron half of the rank-two subtraction appears easier. The Markov identity gives $\mathcal K\mathbf1=\mathbf1$, and strong positivity gives a unique positive stationary density. Those qualitative facts are not yet a quantitative rank-two archive. Five gaps remain.

1.  The exact stored Perron factors must be shown to be spectral terms, rather than accurate floating eigensolver outputs.

2.  A fixed explicit circle about $1$ must be transported from the stored $4096$ matrix to the continuum $L^2$ operator.

3.  The stationary density must be packaged as an intrinsic smooth Hilbert--Schmidt kernel with explicit derivative bounds.

4.  The Perron and parity terms must be joined on a disjoint union contour and transferred uniformly to full and sparse families.

5.  The resulting complement should be related exactly to powers, traces, determinants, and the previously studied physical two-step matrices.

This paper closes those gaps. The main conceptual simplification is that the Perron weighted term is not merely rank one: its right factor is known exactly. If $\pi$ is normalized by $\langle\pi,\mathbf1\rangle=1$, then $$\mathcal Q_+f
 =\mathbf1\langle\pi,f\rangle,
 \qquad q_+(x,y)=\pi(y).
 \label{eq:perron-kernel-intro}$$ All source derivatives vanish. This both sharpens the kernel envelope and explains why the Perron contribution changes the $E$ and $B$ Haar blocks but not the leading $C$ and $D$ tensors.

The second simplification is algebraic. Weighted terms for disjoint simple spectral components commute and annihilate one another. Consequently the bulk complement $$\mathcal B=\mathcal K-\mathcal Q_+-\mathcal Q_-
 \label{eq:bulk-intro}$$ has exact power identities. The peripheral determinant factors are removed without an approximation and without asserting any arithmetic meaning for the residual determinant.

Three evidence levels remain separate throughout.

Analytic theorem

:   Strong-positive Perron structure, weighted Riesz calculus, smooth kernel identities, rank-two orthogonality, power and trace formulas, Fredholm determinant factorization, and Nyström convergence.

Outward certificate

:   Three exact stored Perron Grushin ledgers, two-sided factor corrections, Arb rank-two Haar intervals, Hilbert--Galerkin and Schur transfers, and all-grid normalization and cutoff gates.

Displayed center

:   The heat map is the exact archived $4096$ rank-two factor center. It is not a pointwise interval enclosure of the continuum kernel.

# Operator, contours, and main results {#sec:model}

Let $u_{\mathrm c}$ be the unique root in $(1.5,1.6)$ of $$u^3-2u^2+2u-2=0,$$ fix $\sigma=1/100$, and put $m(x)=1-u_{\mathrm c}x^2$. Define $$g(x,y)=
 e^{-(y-m(x))^2/(2\sigma^2)}
 +e^{-(y+m(x))^2/(2\sigma^2)},
 \qquad
 Z(x)=\int_0^1g(x,y)\,dy,$$ $$k(x,y)=\frac{g(x,y)}{Z(x)},
 \qquad
 (\mathcal Kf)(x)=\int_0^1k(x,y)f(y)\,dy
 \quad\text{on }L^2([0,1]).
 \label{eq:operator}$$ The kernel is real, strictly positive, and $C^\infty$ on the compact square. Moreover $$\mathcal K\mathbf1=\mathbf1.
 \label{eq:markov}$$

The two contours are $$\begin{aligned}
 \Gamma_+&=\{z\in\mathbb C:|z-1|=0.05\},
 \label{eq:perron-contour}\\
 \Gamma_-&=\{z\in\mathbb C:|z-c_-|=0.05\},
 \qquad c_-=-0.9865481927458079.
 \label{eq:parity-contour}\end{aligned}$$ They are disjoint. Write $\Gamma_{\mathrm{per}}=\Gamma_+\cup\Gamma_-$ with the positive orientation on each component, and define $$\mathcal Q_\pm
 =\frac{1}{2\pi i}\int_{\Gamma_\pm}z(z-\mathcal K)^{-1}\,dz,
 \qquad
 \mathcal Q_{\mathrm{per}}=\mathcal Q_++\mathcal Q_-.
 \label{eq:qpm}$$

For $n\ge2$, let $h=1/n$, $x_i=y_i=(i+\tfrac12)h$, and let $P_n^\circ$ be the continuum-normalized midpoint matrix $$(P_n^\circ)_{ij}=h k(x_i,y_j).$$ Let $P_n$ be the exact-real discretely row-normalized full matrix and $P_n^{(L)}$ its support-truncated and renormalized analogue. The fixed family uses $L=8$; the adaptive family uses the RH-39 schedule once growth is needed.

[\[thm:perron\]]{#thm:perron label="thm:perron"} The circle $\Gamma_+$ lies in the resolvent set of $\mathcal K$, contains exactly one eigenvalue counted algebraically, and $$\sup_{z\in\Gamma_+}\left\lVert (z-\mathcal K)^{-1}\right\rVert_2
 \le81.30575843422578.
 \label{eq:perron-resolvent}$$ The enclosed eigenvalue is exactly $1$ and algebraically simple. There is a unique real smooth strictly positive $\pi$ satisfying $$\mathcal K^*\pi=\pi,
 \qquad \int_0^1\pi(y)\,dy=1,$$ and $$\mathcal Q_+f=\mathbf1\langle\pi,f\rangle,
 \qquad q_+(x,y)=\pi(y).
 \label{eq:qplus-form}$$ In particular, $\mathcal Q_+$ has rank one and is both the Perron Riesz projection and its weighted term.

The kernel satisfies $$\begin{aligned}
 1&\le\left\lVert q_+\right\rVert_{L^2([0,1]^2)}\le4.065287921711291,
 \label{eq:qplus-norm}\\
 \left\lVert (q_+)_y\right\rVert_{L^2}&\le1555.261017746445,
 \qquad
 \left\lVert (q_+)_{yy}\right\rVert_{L^2}\le192884.0796819851,
 \label{eq:qplus-derivatives}\end{aligned}$$ while every derivative containing $x$ vanishes. At $n=65536$, its midpoint sample differs from its cell-average matrix by at most $$2.510507555832183\times10^{-6}.
 \label{eq:qplus-midpoint}$$ It lies in an operator-norm ball of radius $1.035040859379391$ and an $L^2$-kernel ball of radius $1.463768820944639$ about the lifted archived $4096$ Perron factor.

[\[thm:rank-two\]]{#thm:rank-two label="thm:rank-two"} The union contour $\Gamma_{\mathrm{per}}$ contains exactly two eigenvalues, $1$ and the real simple negative resonance $\lambda_-$ of RH-43. The intrinsic peripheral weighted term has rank two and smooth real kernel $$q_{\mathrm{per}}(x,y)=\pi(y)+q_-(x,y).
 \label{eq:rank-two-kernel}$$ It is gauge-free and obeys $$\mathcal Q_+\mathcal Q_-=\mathcal Q_-\mathcal Q_+=0.
 \label{eq:weighted-orthogonality}$$ The kernel is enclosed in an $L^2$ ball of radius $3.890944960739168$ about the lifted archived $4096$ rank-two center, and $$\left\lVert q_{\mathrm{per}}\right\rVert_{L^2}\le9.919454564031339.
 \label{eq:rank-two-hs}$$

The stored Perron and parity factors at $2048$, $4096$, and $8192$ are all genuine spectral weighted terms. The resulting actual rank-two Haar ratios satisfy $$\begin{aligned}
 E:&\ [0.2497518320109983,0.2498816430591350],
 \nonumber\\
 C:&\ [0.5000266705203903,0.5000297811731884],
 \nonumber\\
 B:&\ [0.5000390841288479,0.5000413558665742],
 \nonumber\\
 D:&\ [0.2494528393779779,0.2506059251560737].
 \label{eq:rank-two-ratios}\end{aligned}$$

[\[thm:families\]]{#thm:families label="thm:families"} For every integer $n\ge65536$, the exact-real full matrix $P_n$, the fixed eight-sigma sparse matrix, and the adaptive sparse matrix have exactly one eigenvalue in each of $\Gamma_+$ and $\Gamma_-$. On the union contour, their Euclidean resolvents are uniformly bounded by $$267.81252084743886.
 \label{eq:union-resolvent}$$ For the full and either sparse family, $$\left\lVert \mathcal Q_{\mathrm{per}}(P_n)
       -\mathcal Q_{\mathrm{per}}(P_n^{(L_n)})\right\rVert_2
 \le9.269128034310783\times10^{-10},
 \label{eq:rank-two-cutoff}$$ and for the intrinsically deflated matrices $$B_n=P_n-\mathcal Q_+(P_n)-\mathcal Q_-(P_n),
 \label{eq:matrix-bulk}$$ the full-to-sparse difference is at most $$9.271085367195988\times10^{-10}.
 \label{eq:bulk-cutoff}$$

The full rank-two weighted term converges to the midpoint sample of $q_{\mathrm{per}}$ at order $n^{-2}$. Adaptive support preserves the rate $O(n^{-2}(\log n)^{-1/4})$, and the same rate holds for the adaptive bulk operator relative to the full bulk family.

[\[thm:bulk-algebra\]]{#thm:bulk-algebra label="thm:bulk-algebra"} Let $$\mathcal B=\mathcal K-\mathcal Q_+-\mathcal Q_-.
 \label{eq:continuum-bulk}$$ Then $$\mathcal B\mathbf1=0,
 \qquad
 \langle\pi,\mathcal Bf\rangle=0,
 \label{eq:bulk-constraints}$$ the eigenvalues $1$ and $\lambda_-$ are replaced by zero, and every other spectral value is unchanged away from zero. For every integer $m\ge1$, $$\mathcal B^m
 =\mathcal K^m-\mathcal Q_+-\lambda_-^{m-1}\mathcal Q_-.
 \label{eq:power-identity}$$ The smooth Gaussian kernel is trace class. Consequently $$\operatorname{tr}(\mathcal B^m)=\operatorname{tr}(\mathcal K^m)-1-\lambda_-^m
 \label{eq:trace-identity}$$ and the Fredholm determinants satisfy $$\operatorname{det}(\mathrm I-z\mathcal K)
 =(1-z)(1-z\lambda_-)\operatorname{det}(\mathrm I-z\mathcal B).
 \label{eq:det-factorization}$$ The same identities hold exactly for every finite matrix family for which the two contours are valid.

# The Perron weighted term is the stationary kernel {#sec:perron-structure}

The qualitative Perron statement is analytic and independent of the computer-assisted contour.

[\[prop:positive-perron\]]{#prop:positive-perron label="prop:positive-perron"} The eigenvalue $1$ of $\mathcal K$ is algebraically simple. There exists a unique strictly positive $\pi\in C^\infty([0,1])$ with $\mathcal K^*\pi=\pi$ and $\langle\pi,\mathbf1\rangle=1$. The Riesz projection at $1$ is $$\mathcal P_+f=\mathbf1\langle\pi,f\rangle.
 \label{eq:perron-projector}$$ Since the eigenvalue is $1$, $\mathcal Q_+=\mathcal K\mathcal P_+=\mathcal P_+$.

The normalized kernel $k$ is strictly positive and smooth on the compact square, so $\mathcal K$ is compact and strongly positive. The Markov identity [\[eq:markov\]](#eq:markov){reference-type="eqref" reference="eq:markov"} fixes its spectral radius at $1$. Krein--Rutman theory and strong positivity make the eigenvalue algebraically simple and give a strictly positive dual eigenfunction [@Schaefer1974; @Kato1995]. Normalize it by $\langle\pi,\mathbf1\rangle=1$. The rank-one formula for a simple Riesz projection gives [\[eq:perron-projector\]](#eq:perron-projector){reference-type="eqref" reference="eq:perron-projector"}. Multiplication by $\mathcal K$ does not change that projection.

[\[prop:perron-envelope\]]{#prop:perron-envelope label="prop:perron-envelope"} Let $K_y$ and $K_{yy}$ denote the Hilbert--Schmidt operators obtained by differentiating $k(x,y)$ in the target variable. Then $$\left\lVert \pi'\right\rVert_2\le\left\lVert K_y\right\rVert_{\mathrm{HS}}\left\lVert \pi\right\rVert_2,
 \qquad
 \left\lVert \pi''\right\rVert_2\le\left\lVert K_{yy}\right\rVert_{\mathrm{HS}}\left\lVert \pi\right\rVert_2.
 \label{eq:pi-derivative}$$ If $Q_{+,n}^\circ$ is the midpoint sample and $Q_{+,n}^{\mathrm G}$ the cell-average matrix of $q_+$, then $$\left\lVert Q_{+,n}^\circ-Q_{+,n}^{\mathrm G}\right\rVert_2
 \le\frac{\left\lVert \pi''\right\rVert_2}{\sqrt{320}\,n^2}.
 \label{eq:perron-midpoint-bound}$$

The dual fixed-point equation is $$\pi(y)=\int_0^1k(x,y)\pi(x)\,dx.$$ Differentiate under the integral. The Hilbert--Schmidt operator inequality gives [\[eq:pi-derivative\]](#eq:pi-derivative){reference-type="eqref" reference="eq:pi-derivative"}. Since $q_+(x,y)=\pi(y)$, source derivatives and all mixed derivatives vanish. The one-dimensional midpoint-average Peano kernel has $L^2$ norm $h^{3/2}/\sqrt{320}$ on each cell; summing the cell errors yields [\[eq:perron-midpoint-bound\]](#eq:perron-midpoint-bound){reference-type="eqref" reference="eq:perron-midpoint-bound"}.

On $\Gamma_+$, the Riesz projection norm is bounded by $$\left\lVert \mathcal P_+\right\rVert_2
 \le0.05\sup_{z\in\Gamma_+}\left\lVert (z-\mathcal K)^{-1}\right\rVert_2.$$ Because $\left\lVert \mathbf 1\right\rVert_2=1$ and $\langle\pi,\mathbf1\rangle=1$, $$1\le\left\lVert \pi\right\rVert_2=\left\lVert \mathcal P_+\right\rVert_2.$$ Combining [\[eq:perron-resolvent\]](#eq:perron-resolvent){reference-type="eqref" reference="eq:perron-resolvent"} with the RH-42 derivative envelope gives [\[eq:qplus-norm\]](#eq:qplus-norm){reference-type="eqref" reference="eq:qplus-norm"}--[\[eq:qplus-midpoint\]](#eq:qplus-midpoint){reference-type="eqref" reference="eq:qplus-midpoint"}.

# Exact stored Perron factors {#sec:stored-perron}

The archived matrices at $n=2048,4096,8192$ contain a floating Perron eigenvalue approximation, a nearly constant right mode, and a positive left mode. Small residuals alone do not prove that the stored rank-one factor is the weighted Riesz term of the exact stored matrix. We use the two-sided correction theorem of @WangParityKernel2026.

For a stored matrix $A$, approximate eigenvalue $\lambda_0$, and left--right factor $$P_0=\frac{r_0\ell_0^T}{\ell_0^Tr_0},$$ define $$\widetilde A
 =\lambda_0P_0+(\mathrm I-P_0)A(\mathrm I-P_0).
 \label{eq:corrected-matrix}$$ Then $P_0$ reduces $\widetilde A$ exactly, and $$\widetilde A-A
 =-(A-\lambda_0\mathrm I)P_0-P_0(A-\lambda_0\mathrm I)
  +P_0(A-\lambda_0\mathrm I)P_0.
 \label{eq:correction}$$ The correction norm is controlled by the two residuals and the enclosed Gram factor. If $M\left\lVert \widetilde A-A\right\rVert<1$ on the contour, the resolvent identity transfers $\lambda_0P_0$ to the actual weighted Riesz term of $A$.

The inverse certificate treats every stored binary64 number as an exact real input. Sparse LU provides an approximate bordered inverse; componentwise outward residual arithmetic bounds its exact inverse in both the one- and infinity-norms, whose geometric mean gives a Euclidean upper [@WangOutward2026; @Rump2010]. The radius $0.1$ is too wide for this particular Grushin center: at $n=2048$ its transport product is $1.366$. The fixed radius $0.05$ closes all three levels with products near $0.683$.

::: {#tab:perron-factors}
     $n$       residual upper   contour resolvent   correction product   weighted-term error
  ------ -------------------- ------------------- -------------------- ---------------------
    2048   $4.3058\,10^{-11}$     $65.1669349545$    $6.314\,10^{-11}$    $2.1601\,10^{-10}$
    4096   $1.1923\,10^{-10}$     $65.2291154903$    $1.232\,10^{-10}$    $4.2167\,10^{-10}$
    8192   $3.3310\,10^{-10}$     $65.2559386375$    $2.434\,10^{-10}$    $8.3379\,10^{-10}$

  : Exact-stored Perron Grushin and weighted-factor certificates.
:::

The centers differ from $1$ by at most $2.5\times10^{-15}$. At the base level the exact target circle $|z-1|=0.05$ is obtained by a center-shift Neumann product $$2.896754635731181\times10^{-14}.
 \label{eq:center-shift}$$ The two circles enclose the same weighted term; only the resolvent upper is transported.

# From the stored Perron circle to the continuum {#sec:perron-continuum}

The RH-42 exact-stored-to-midpoint bridge is independent of which isolated mode is being followed. Its defect is $$\left\lVert P_{4096}^{\mathrm{stored}}-P_{4096}^\circ\right\rVert_2
 \le1.055416712190961\times10^{-5}.
 \label{eq:stored-midpoint-defect}$$ The first Neumann transfer gives the exact-midpoint Perron-circle resolvent $65.27405269296997$. The midpoint-to-cell-average Galerkin defect is $8.115839277660032\times10^{-4}$ and yields the $4096$ Hilbert-Galerkin resolvent $68.92540148121991$.

Let $V_n$ be the cell-average space and split $V_{2n}=V_n\oplus W_n$ by the orthogonal Haar transform. Relative to this decomposition, write $$A_{2n}=
 \begin{pmatrix}A_n&B_n\\C_n&D_n\end{pmatrix}.$$ The derivative envelope gives $$\left\lVert C_n\right\rVert\le\frac{K_x}{\pi n},
 \quad
 \left\lVert B_n\right\rVert\le\frac{K_y}{\pi n},
 \quad
 \left\lVert D_n\right\rVert\le\frac{K_{xy}}{\pi^2n^2}.$$ Since $\min_{z\in\Gamma_+}|z|=0.95$, the detail resolvent is controlled by $1/(0.95-\left\lVert D_n\right\rVert)$. The Schur self-energy $$\Sigma_n(z)=B_n(z-D_n)^{-1}C_n$$ then transfers the count whenever $M_n\sup_{\Gamma_+}\left\lVert \Sigma_n(z)\right\rVert<1$.

::: {#tab:perron-chain}
  step                            Schur/Neumann product   resulting resolvent upper
  ----------------------------- ----------------------- ---------------------------
  stored $\to$ exact midpoint         $6.8844\,10^{-4}$             $65.2740526930$
  midpoint $\to V_{4096}$             $5.2976\,10^{-2}$             $68.9254014812$
  $4096\to8192$                       $1.1228\,10^{-1}$             $77.8066710318$
  $8192\to16384$                      $3.1675\,10^{-2}$             $80.3990839395$
  $16384\to32768$                     $8.1817\,10^{-3}$             $81.0793334963$
  $32768\to65536$                     $2.0627\,10^{-3}$             $81.2562912048$
  full infinite complement            $5.1679\,10^{-4}$             $81.3057584342$

  : Validated Perron Hilbert--Galerkin and complement Schur chain.
:::

For the final step, decompose $L^2=V_{65536}\oplus V_{65536}^\perp$. The same derivative bounds apply to the full infinite complement. Its self-energy product is only $5.167900126933194\times10^{-4}$, proving [\[eq:perron-resolvent\]](#eq:perron-resolvent){reference-type="eqref" reference="eq:perron-resolvent"} and the count-one statement. Since $\mathcal K\mathbf1=\mathbf1$, the enclosed eigenvalue must be $1$; strong positivity identifies it as algebraically simple.

# Weighted transport and the Perron construction ball {#sec:perron-transport}

The Schur resolvent formula can be integrated around $\Gamma_+$. If the detail block has no spectrum inside the circle, the weighted fine term differs from $\operatorname{diag}(\mathcal Q(A_n),0)$ only through the Schur self-energy and the three coupling blocks. The Frobenius sum of those four block bounds gives an operator upper [@WangParityKernel2026].

Starting from the exact stored $4096$ Perron factor gives the ledger in [3](#tab:perron-transport){reference-type="ref" reference="tab:perron-transport"}. All numbers are Euclidean operator uppers.

::: {#tab:perron-transport}
  gate                                       weighted-term difference upper
  ---------------------------------------- --------------------------------
  stored factor $\to$ actual stored term              $4.2166963\,10^{-10}$
  stored $\to$ exact midpoint                                $0.0023592032$
  midpoint $\to V_{4096}$                                    $0.1916958114$
  $4096\to8192$                                              $0.5250689957$
  $8192\to16384$                                             $0.1885770690$
  $16384\to32768$                                            $0.0756069632$
  $32768\to65536$                                            $0.0347628684$
  finite rank $\to$ continuum complement                     $0.0169699485$
  total                                                      $1.0350408594$

  : Weighted Perron transport from the stored center to the continuum.
:::

The difference of two rank-one operators has rank at most two, hence its Hilbert--Schmidt norm is at most $\sqrt2$ times its operator norm. This gives the Perron $L^2$ construction radius in [\[thm:perron\]](#thm:perron){reference-type="ref" reference="thm:perron"}. Adding the RH-43 parity construction balls gives $$\begin{aligned}
 \left\lVert \mathcal Q_{\mathrm{per}}-Q_{\mathrm{per},4096}^{\mathrm{center}}\right\rVert_2
 &\le2.751313566962289,
 \label{eq:rank-two-construction-op}\\
 \left\lVert q_{\mathrm{per}}-q_{\mathrm{per},4096}^{\mathrm{center}}\right\rVert_{L^2}
 &\le3.890944960739168.
 \label{eq:rank-two-construction-hs}\end{aligned}$$

# The actual spectral rank-two Haar law {#sec:rank-two-haar}

For a smooth kernel $q$, midpoint sampling and the orthogonal Haar transform give four blocks. With the orientation used in the archive, $$\begin{aligned}
 h^{-2}E_h&\longrightarrow\frac{q_{xx}+q_{yy}}{32},
 \label{eq:haar-E}\\
 h^{-1}C_h&\longrightarrow\frac{q_x}{4},
 \label{eq:haar-C}\\
 h^{-1}B_h&\longrightarrow\frac{q_y}{4},
 \label{eq:haar-B}\\
 h^{-2}D_h&\longrightarrow\frac{q_{xy}}{16}
 \label{eq:haar-D}\end{aligned}$$ in Hilbert--Schmidt sampling; see @WangHaar2026 [@WangParityKernel2026]. For the Perron kernel, $$(q_+)_x=(q_+)_{xx}=(q_+)_{xy}=0.
 \label{eq:perron-haar-zero}$$ Thus its leading $C$ and $D$ tensors vanish exactly. In the combined kernel, the leading $C$ and $D$ tensors are precisely those of the parity kernel, whereas $E$ and $B$ include the stationary density.

The RH-40 Arb ledger enclosed the exact algebraic rank-two factors but did not prove that both factors were spectral. RH-43 closed the parity factor errors. The present Perron errors complete the spectral correction. If $e_n$ is the sum of the Perron and parity factor errors at level $n$, then $$\begin{aligned}
 e_{2048}&\le5.810907673369557\times10^{-10},\nonumber\\
 e_{4096}&\le1.141956473291731\times10^{-9},\nonumber\\
 e_{8192}&\le2.260221050983747\times10^{-9}.
 \label{eq:combined-factor-errors}\end{aligned}$$ Orthogonality of the Haar transform bounds the correction of $E$ by $\sqrt2(e_n+e_{2n})$ and the other three blocks by $\sqrt2e_{2n}$.

::: {#tab:rank-two-ratios}
  block        actual ratio interval       maximum target deviation
  ------- ------------------------------- --------------------------
  $E$      $[0.2497518320,0.2498816431]$       $2.482\,10^{-4}$
  $C$      $[0.5000266705,0.5000297812]$       $2.979\,10^{-5}$
  $B$      $[0.5000390841,0.5000413559]$       $4.136\,10^{-5}$
  $D$      $[0.2494528394,0.2506059252]$       $6.060\,10^{-4}$

  : Validated intervals for the actual spectral rank-two Haar ratios.
:::

The smallest block is $D$, so its interval widens most under the spectral correction. It nevertheless remains wholly within $10^{-3}$ of the target $1/4$. The quarter--half mechanism is therefore both analytic and spectral for the complete rank-two peripheral term.

# The intrinsic rank-two kernel {#sec:rank-two-kernel}

Let $\mathcal P_\pm$ be the Riesz projections. Since the contours are disjoint, functional calculus gives $$\mathcal P_+\mathcal P_-=\mathcal P_-\mathcal P_+=0,
 \qquad
 \mathcal K\mathcal P_\pm=\mathcal P_\pm\mathcal K.
 \label{eq:projection-orthogonality}$$ Moreover $$\mathcal Q_+=\mathcal P_+,
 \qquad
 \mathcal Q_-=\lambda_-\mathcal P_-.$$ This proves [\[eq:weighted-orthogonality\]](#eq:weighted-orthogonality){reference-type="eqref" reference="eq:weighted-orthogonality"}. Both summands have nonzero one-dimensional ranges, so their sum has rank two. The kernel is exactly [\[eq:rank-two-kernel\]](#eq:rank-two-kernel){reference-type="eqref" reference="eq:rank-two-kernel"}, independent of all eigenvector gauges.

Adding the specialized Perron envelope to the RH-43 parity envelope gives the explicit bounds in [5](#tab:rank-two-envelope){reference-type="ref" reference="tab:rank-two-envelope"}.

::: {#tab:rank-two-envelope}
  quantity                                                                    rigorous upper
  ----------------------------------------------------------- ------------------------------
  $\left\lVert q_{\mathrm{per}}\right\rVert_{L^2}$                       $9.919454564031339$
  $\left\lVert (q_{\mathrm{per}})_x\right\rVert_{L^2}$                   $3780.968408944756$
  $\left\lVert (q_{\mathrm{per}})_y\right\rVert_{L^2}$                   $3715.926624442619$
  $\left\lVert (q_{\mathrm{per}})_{xx}\right\rVert_{L^2}$          $1.107398829423627\,10^6$
  $\left\lVert (q_{\mathrm{per}})_{xy}\right\rVert_{L^2}$          $1.544489270236306\,10^6$
  $\left\lVert (q_{\mathrm{per}})_{yy}\right\rVert_{L^2}$          $4.608506732586612\,10^5$
  $\left\lVert (q_{\mathrm{per}})_{xxyy}\right\rVert_{L^2}$     $5.610208521245976\,10^{10}$

  : Hilbert--Schmidt envelope for the intrinsic rank-two kernel.
:::

At $n=65536$, the midpoint-to-cell-average defect is bounded by $$2.041176267936486\times10^{-5}.
 \label{eq:rank-two-midpoint-defect}$$ The displayed center in [1](#fig:summary){reference-type="ref" reference="fig:summary"} is not a pointwise interval enclosure. The validated object is the Hilbert--Schmidt ball and derivative envelope.

# Uniform full, sparse, and rank-two-deflated families {#sec:uniform}

At $n=65536$, the continuum-to-midpoint defect for the Markov kernel is $0.005112929739977326$. Applying it to the Perron contour gives product $0.4157106303297654$ and exact-midpoint resolvent $139.15323922479328$. Discrete row normalization then gives the full matrix resolvent $$139.27331158261282.
 \label{eq:perron-full-resolvent}$$ The eight-sigma cutoff defect is $$\varepsilon_{65536}
 \le1.957332885203985\times10^{-13},$$ and the sparse Perron resolvent is $139.27331158640953$.

For two operators on one circle, the resolvent identity gives $$\left\lVert \mathcal Q(A;\Gamma)-\mathcal Q(B;\Gamma)\right\rVert
 \le rR_\Gamma M_AM_B\left\lVert A-B\right\rVert.
 \label{eq:weighted-lipschitz}$$ Hence the Perron full-to-sparse weighted difference is $$1.993240948303590\times10^{-10}.
 \label{eq:perron-cutoff}$$ Adding the RH-43 parity bound yields [\[eq:rank-two-cutoff\]](#eq:rank-two-cutoff){reference-type="eqref" reference="eq:rank-two-cutoff"}; adding the matrix cutoff once yields [\[eq:bulk-cutoff\]](#eq:bulk-cutoff){reference-type="eqref" reference="eq:bulk-cutoff"}.

The parity contour remains the limiting condition. Its uniform sparse resolvent upper is $267.81252084743886$, larger than the Perron upper. Therefore the disjoint union contour inherits exactly the RH-43 threshold $n\ge65536$ and the same maximum resolvent constant.

The analytic Nyström theorem of @WangRiesz2026, now with both continuum premises closed, gives unconditionally $$\left\lVert \mathcal Q_{\mathrm{per}}(P_n)-Q_{\mathrm{per},n}^\circ\right\rVert_2
 =O(n^{-2}).
 \label{eq:rank-two-full-rate}$$ Combining this with the adaptive RH-39 cutoff gives $$\left\lVert \mathcal Q_{\mathrm{per}}(P_n^{(L_n)})
       -Q_{\mathrm{per},n}^\circ\right\rVert_2
 =O\!\left(n^{-2}(\log n)^{-1/4}\right).
 \label{eq:rank-two-adaptive-rate}$$

The fixed eight-sigma rank-two difference is uniformly below $9.28\times10^{-10}$, sufficient for the present contour and deflation theorems. The underlying fixed-width row defect has a nonzero continuum floor. Adaptive growth is required when convergence to the full continuum kernel is claimed.

# Exact bulk algebra, traces, and determinants {#sec:bulk}

The validated rank-two term now permits an exact intrinsic bulk operator. Its algebra is stronger than a perturbative subtraction.

[\[prop:bulk-powers\]]{#prop:bulk-powers label="prop:bulk-powers"} Let $\mathcal B$ be defined by [\[eq:continuum-bulk\]](#eq:continuum-bulk){reference-type="eqref" reference="eq:continuum-bulk"}. Then [\[eq:bulk-constraints\]](#eq:bulk-constraints){reference-type="eqref" reference="eq:bulk-constraints"} holds and, for every $m\ge1$, [\[eq:power-identity\]](#eq:power-identity){reference-type="eqref" reference="eq:power-identity"} holds.

The Markov and stationary identities give $$\mathcal K\mathbf1=\mathbf1,
 \qquad
 \mathcal Q_+\mathbf1=\mathbf1,
 \qquad
 \mathcal Q_-\mathbf1=0,$$ and their dual analogues give the left constraint. Functional calculus gives $$\begin{aligned}
 \mathcal K\mathcal Q_+&=\mathcal Q_+\mathcal K=\mathcal Q_+, & \mathcal Q_+^2&=\mathcal Q_+,\\
 \mathcal K\mathcal Q_-&=\mathcal Q_-\mathcal K=\lambda_-\mathcal Q_-,
 & \mathcal Q_-^2&=\lambda_-\mathcal Q_-,\end{aligned}$$ together with [\[eq:weighted-orthogonality\]](#eq:weighted-orthogonality){reference-type="eqref" reference="eq:weighted-orthogonality"}. Thus $\mathcal B$ vanishes on the two peripheral ranges and equals $\mathcal K$ on the invariant complementary spectral subspace. Raising this block decomposition to the $m$th power proves [\[eq:power-identity\]](#eq:power-identity){reference-type="eqref" reference="eq:power-identity"}.

The case $m=2$ is particularly relevant to the archived physical matrices: $$\mathcal B^2=\mathcal K^2-\mathcal Q_+-\lambda_-\mathcal Q_-.
 \label{eq:physical-two-step}$$ Thus the earlier Perron/parity-extracted physical two-step construction has an exact intrinsic continuum target. From [\[eq:rank-two-full-rate\]](#eq:rank-two-full-rate){reference-type="eqref" reference="eq:rank-two-full-rate"}--[\[eq:rank-two-adaptive-rate\]](#eq:rank-two-adaptive-rate){reference-type="eqref" reference="eq:rank-two-adaptive-rate"} and $$\left\lVert B_n^2-\mathcal B^2\right\rVert
 \le(\left\lVert B_n\right\rVert+\left\lVert \mathcal B\right\rVert)\left\lVert B_n-\mathcal B\right\rVert,$$ the full and adaptive physical two-step families inherit the same rates, provided the matrix and continuum operators are compared in the standard cell basis.

[\[prop:trace-determinant\]]{#prop:trace-determinant label="prop:trace-determinant"} The identities [\[eq:trace-identity\]](#eq:trace-identity){reference-type="eqref" reference="eq:trace-identity"} and [\[eq:det-factorization\]](#eq:det-factorization){reference-type="eqref" reference="eq:det-factorization"} hold.

The Gaussian kernel is $C^\infty$ on a compact one-dimensional square, so the associated integral operator is trace class; finite-rank subtraction preserves trace class [@Simon2005; @GohbergKrein1969]. Taking traces in [\[eq:power-identity\]](#eq:power-identity){reference-type="eqref" reference="eq:power-identity"} uses $$\operatorname{tr}(\mathcal Q_+)=1,
 \qquad
 \operatorname{tr}(\lambda_-^{m-1}\mathcal Q_-)=\lambda_-^m,$$ and gives [\[eq:trace-identity\]](#eq:trace-identity){reference-type="eqref" reference="eq:trace-identity"}. Relative to the invariant direct sum $$L^2=\operatorname{Ran}\mathcal P_+\dotplus\operatorname{Ran}\mathcal P_-\dotplus\mathcal H_{\mathrm{bulk}},$$ $\mathcal K$ has diagonal blocks $1$, $\lambda_-$, and the bulk restriction, whereas $\mathcal B$ has blocks $0$, $0$, and the same bulk restriction. The Fredholm determinant is multiplicative over this direct sum, proving [\[eq:det-factorization\]](#eq:det-factorization){reference-type="eqref" reference="eq:det-factorization"}.

Equation [\[eq:det-factorization\]](#eq:det-factorization){reference-type="eqref" reference="eq:det-factorization"} removes two validated noisy peripheral factors. It does not identify the remaining determinant with an arithmetic zeta function, a prime-power trace, or the spectrum of a self-adjoint operator. It is the correct structural input for such later questions, not their conclusion.

# Certificate summary and figure {#sec:certificate}

The complete certificate closes the following gates.

1.  exact stored Perron Euclidean Grushin counts at $2048$, $4096$, and $8192$;

2.  two-sided Perron factor errors below $8.34\times10^{-10}$;

3.  a continuum Perron contour with resolvent upper $81.306$;

4.  an intrinsic stationary kernel and a rank-two continuum kernel;

5.  actual spectral rank-two quarter--half intervals;

6.  an all-grid two-contour theorem from $n=65536$;

7.  rank-two weighted and deflated cutoff bounds below $9.28\times10^{-10}$;

8.  exact bulk power, trace, and Fredholm determinant factorizations.

![Validated intrinsic rank-two peripheral closure. (a) The exact archived $4096$ Perron-plus-parity factor center, displayed as a piecewise kernel; it is not a pointwise interval enclosure. (b) Actual weighted-term errors for the stored Perron and parity factors and their rank-two sum. (c) Corrected Frobenius intervals for the actual spectral rank-two Haar ratios. (d) Perron and parity contour resolvent constants; the disjoint union inherits the parity threshold and maximum.](<../../../../../zeta_mvp0/papers/RH-44-validated-rank-two-peripheral-complement/figures/validated_rank_two_peripheral_complement.pdf>){#fig:summary width="\\textwidth"}

# What is closed and what remains {#sec:boundary}

The present result changes the status of the peripheral route in five ways.

1.  **Both continuum peripheral modes are intrinsic kernels.** The Perron kernel is the stationary density in the target variable; the negative kernel is the RH-43 weighted parity term.

2.  **The union contour is quantitative.** Each component has count one and a dimension-uniform Euclidean resolvent for full and sparse families.

3.  **All six stored factors are spectral.** Perron and parity factors at three levels now have exact-stored Grushin and two-sided correction certificates.

4.  **The rank-two quarter--half law is actual.** Its intervals concern true matrix weighted terms, not only archived low-rank algebra.

5.  **The bulk operator has exact trace algebra.** Peripheral subtraction commutes with every power and removes the two elementary Fredholm determinant factors exactly.

Several boundaries remain essential.

1.  The noise width is fixed at $\sigma=1/100$.

2.  The exact continuum kernels are enclosed in Hilbert--Schmidt norms; no pointwise interval heat map is claimed.

3.  The all-dimension theorem concerns exact-real Gaussian formulas. The binary64 theorem concerns the six archived factors.

4.  Fixed eight-sigma support is spectrally stable but is not claimed to converge to the full kernel in row norm.

5.  The determinant factorization is structural. No arithmetic trace formula, prime-power identity, zeta-zero identification, $T\log T$ counting law, self-adjoint Hilbert--Pólya operator, or Riemann-hypothesis conclusion follows.

The natural next gate is now sharply defined: prove trace-norm convergence of the intrinsic bulk two-step family and construct its validated Fredholm determinant, without yet imposing an arithmetic interpretation. Unlike the earlier route, that step no longer carries dimension-dependent peripheral eigenvector gauges.

# Archive and reproducibility {#sec:archive}

The archive contains two principal ledgers:

1.  the multilevel exact-stored Perron Euclidean Grushin certificate; and

2.  the complete Perron contour, factor, rank-two Haar, continuum kernel, full/sparse family, cutoff, and bulk composition certificate.

Every cross-paper input, local source, result, figure, and publication artifact is recorded by SHA-256.

The complete replay is:

    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/run_multilevel_perron_grushin.py
    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/build_rank_two_certificate.py
    MPLBACKEND=Agg PYTHONDONTWRITEBYTECODE=1 \
      /root/math/.venv/bin/python experiments/make_figures.py
    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      -m pytest -q -p no:cacheprovider
    latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
    cp main.pdf validated-rank-two-peripheral-complement.pdf
    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/build_archive.py
    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/verify_archive.py

The $8192$ bordered inverse is the longest step, taking roughly six minutes on the current server. The composition, Arb Haar ledger, tests, figures, and archive verification take seconds.

# Conclusion

The peripheral subtraction is now complete at fixed positive noise. The Perron term is the stationary kernel $\pi(y)$; the negative term is the validated parity kernel. Their disjoint Riesz contours produce a smooth gauge-free rank-two object, and both the continuum and all sufficiently fine full/sparse matrix families carry exactly one eigenvalue on each branch.

This completion also resolves the last ambiguity in the archived rank-two Haar ledger. Every stored Perron and parity factor is now a genuine spectral weighted term, so the corrected quarter--half intervals concern the actual matrices. The union contour does not worsen the RH-43 threshold: the parity branch remains the limiting condition.

Most importantly, the residual bulk is no longer defined by an eigensolver convention. It is the intrinsic operator $\mathcal B=\mathcal K-\mathcal Q_+-\mathcal Q_-$, with exact power, trace, and Fredholm determinant factorizations. This does not supply an arithmetic spectrum, but it gives the next paper a clean operator: a validated rank-two-free bulk whose two-step trace and determinant can be studied without peripheral gauge or normalization artifacts.
