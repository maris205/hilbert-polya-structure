---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-40-weighted-riesz-projector-bridge"
canonical_tex: "zeta_mvp0/papers/RH-40-weighted-riesz-projector-bridge/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-40-weighted-riesz-projector-bridge/weighted-riesz-projector-bridge.pdf"
source_sha256: "a282fd132db2b2a3e553e0202d9a5c24299a6fa806bb7cd2e508130e5e63fb16"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Gauge-Free Weighted Riesz Terms for Nyström Peripheral Extraction A Second-Order Continuum Bridge and Exact Stored Haar Ledgers

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-40-weighted-riesz-projector-bridge>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-40-weighted-riesz-projector-bridge/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-40-weighted-riesz-projector-bridge/weighted-riesz-projector-bridge.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-40-weighted-riesz-projector-bridge/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-40-weighted-riesz-projector-bridge/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  A nested-grid spectral-count program subtracts a rank-two Perron/parity term from folded-Gaussian Markov matrices. Smooth-kernel Haar theory predicts second-order consistency and detail blocks and first-order cross blocks, but the missing projector bridge was previously phrased in terms of individual left and right eigenvectors. Those vectors have unavoidable scaling, sign, phase, and ordering ambiguities. We replace them by the intrinsic weighted Riesz term $$\mathcal Q(A;\Gamma)=A\Pi(A;\Gamma)
   =\frac{1}{2\pi i}\int_\Gamma z(z-A)^{-1}\,dz.$$

  First, for two bounded operators sharing an isolating contour, we prove the exact perturbation estimate $$\left\lVert \mathcal Q(A;\Gamma)-\mathcal Q(B;\Gamma)\right\rVert
   \le \frac{\operatorname{len}(\Gamma)}{2\pi}
         \max_{z\in\Gamma}|z|\,M_A M_B\left\lVert A-B\right\rVert,$$ where $M_A$ and $M_B$ are the contour resolvent suprema. Second, for a $C^2$ integral kernel and a simple isolated nonzero eigenvalue, midpoint Nyström approximation of the eigenvalue and of the right and transposed left eigenfunctions yields an intrinsic matrix estimate $$\left\lVert Q_h-Q_h^\circ\right\rVert_2=O(h^2).$$ Here $Q_h$ is the finite-dimensional weighted Riesz term and $Q_h^\circ$ is the midpoint matrix of the smooth continuum kernel $\lambda r(x)\ell(y)$. The argument is independent of every eigenvector gauge. Strong positivity makes the Perron instance unconditional for the full folded-Gaussian kernel. The negative parity instance remains conditional on the existence of a simple isolated continuum resonance. The adaptive cutoff bridge from the preceding paper transfers to $Q_h$ under one additional, explicit uniform Euclidean contour-resolvent bound.

  At $\sigma=10^{-2}$ we then audit the exact stored binary64 rank-two factors at dimensions $2048,4096,8192$. A 224-bit Arb calculation evaluates the low-rank Frobenius identities without materializing the dense matrices. The second-to-first Haar ratios are rigorously enclosed by $$0.249816736,\quad0.500028226,\quad0.500040220,\quad0.250029234$$ for the consistency, coarse-to-detail, detail-to-coarse, and detail blocks. The exact-stored biorthogonality defect is below $2.885\times10^{-15}$. Floating eigen-residuals and an observed radial gap of $0.31188$ support, but do not validate, the parity-isolation hypothesis. Thus the Perron bridge is closed analytically; continuum parity isolation is the remaining analytic gate. No zero-noise, zeta-zero, Hilbert--Pólya, or Riemann-hypothesis conclusion is made.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Gauge-Free Weighted Riesz Terms for Nyström Peripheral Extraction\
  A Second-Order Continuum Bridge and Exact Stored Haar Ledgers
```

## Markdown 正文

# Introduction

The stored continuation certificates of @WangNested2026 [@WangIterated2026] use a folded-Gaussian Markov matrix $P_h$, remove its Perron and negative parity contributions, and square the remaining one-step operator. A subsequent deterministic theorem [@WangHaar2026] explained the observed dyadic law $$\left\lVert E_h\right\rVert_2,\left\lVert D_h\right\rVert_2=O(h^2),\qquad
 \left\lVert C_h\right\rVert_2,\left\lVert B_h\right\rVert_2=O(h).
 \label{eq:quarter-half-intro}$$ One Haar difference extracts one derivative, while two differences extract a mixed second derivative. Discrete row normalization, subtraction of a smooth finite-rank kernel, and exact squaring preserve these powers.

That result isolated two bridges between the smooth continuum theorem and the sparse stored family. The hard support window has now been treated separately [@WangCutoff2026]: a fixed eight-sigma window is negligible at the archived dimensions but has a nonzero full-kernel continuum defect, whereas a slowly growing support gives an $O(h^2)$ Euclidean perturbation. The remaining bridge concerns the peripheral term.

A direct comparison of eigenvectors is the wrong invariant. If $r$ and $\ell$ are a biorthogonal right-left pair, then $$r\longmapsto c r,\qquad \ell\longmapsto c^{-1}\ell$$ changes both vectors but leaves the spectral contribution unchanged. Signs and complex phases are special cases, and several modes introduce ordering and basis ambiguities. Numerical continuation can impose conventions, but an analytic theorem should not depend on them.

The matrix actually subtracted in the stored construction is $$Q_h=R_h\Lambda_hL_h^T,
 \qquad L_h^TR_h=I,
 \label{eq:stored-weighted-term}$$ not the unweighted projector $R_hL_h^T$. Intrinsically, it is the part of $P_h$ selected by holomorphic functional calculus [@Kato1995]: $$\mathcal Q(P_h;\Gamma)=P_h\Pi(P_h;\Gamma).
 \label{eq:intro-riesz}$$ This observation turns the missing bridge into a resolvent and Nyström question.

The contributions of this paper are:

1.  a gauge-free definition of the weighted peripheral term for a simple eigenvalue or a finite cluster;

2.  an explicit resolvent-Lipschitz estimate and a Neumann-series contour persistence criterion;

3.  a second-order Euclidean matrix theorem for smooth midpoint Nyström weighted terms, proved by treating the transposed kernel on the same footing as the original kernel;

4.  an unconditional application to the full-kernel Perron branch and a sharply stated conditional application to the negative parity branch;

5.  transfer of an $O(h^2)$ Markov cutoff defect to the weighted Riesz term under uniform contour conditioning; and

6.  an exact-stored Arb ledger for the rank-two factors and all four dyadic Haar blocks at the three archived dimensions.

Three evidence levels are kept distinct.

Analytic theorem

:   Functional-calculus perturbation bounds and smooth Nyström convergence.

Exact-stored ledger

:   Arb enclosures after every archived binary64 factor is treated as an exact real input.

Floating diagnostic

:   Sparse eigen-residuals and a leading-spectrum isolation audit; these are not interval enclosures of the eigensolver or of the full matrix.

The result closes an analytic mechanism, not an arithmetic identification. The resonances studied here are eigenvalues of a non-self-adjoint noisy transfer operator at fixed positive noise.

# Weighted Riesz terms {#sec:riesz}

Let $A$ be a bounded operator on a complex Banach space, and let $\Gamma$ be a positively oriented rectifiable Jordan contour contained in the resolvent set of $A$. Assume that its interior contains a finite isolated spectral cluster.

[\[def:weighted-riesz\]]{#def:weighted-riesz label="def:weighted-riesz"} Define $$\begin{aligned}
 \Pi(A;\Gamma)
 &=\frac{1}{2\pi i}\int_\Gamma(z-A)^{-1}\,dz,
 \label{eq:riesz-projector}\\
 \mathcal Q(A;\Gamma)
 &=\frac{1}{2\pi i}\int_\Gamma z(z-A)^{-1}\,dz.
 \label{eq:weighted-riesz}\end{aligned}$$

[\[prop:intrinsic\]]{#prop:intrinsic label="prop:intrinsic"} The weighted term satisfies $$\mathcal Q(A;\Gamma)=A\Pi(A;\Gamma)=\Pi(A;\Gamma)A.$$ If the contour encloses one simple eigenvalue $\lambda$, with $Ar=\lambda r$, $\ell A=\lambda\ell$, and $\ell(r)=1$, then $$\mathcal Q(A;\Gamma)=\lambda\,r\otimes\ell.
 \label{eq:simple-term}$$ This expression is invariant under $r\mapsto cr$ and $\ell\mapsto c^{-1}\ell$ for every $c\ne0$.

The identity $z(z-A)^{-1}=I+A(z-A)^{-1}$ and the vanishing contour integral of the constant operator give the first formula. The standard simple Riesz projector is $r\otimes\ell$, which proves the second. The two gauge factors cancel exactly.

For a semisimple cluster, one may write $\mathcal Q=R\Lambda L^T$ in any biorthogonal basis. A change of basis alters the factors but not $\mathcal Q$. The contour formula also remains valid for nonsemisimple clusters, where an eigenvector-only description would need Jordan data.

[\[thm:resolvent-lipschitz\]]{#thm:resolvent-lipschitz label="thm:resolvent-lipschitz"} Let $A$ and $B$ be bounded operators on the same Banach space, and suppose $\Gamma\subset\rho(A)\cap\rho(B)$. Put $$M_A=\max_{z\in\Gamma}\left\lVert (z-A)^{-1}\right\rVert,\qquad
 M_B=\max_{z\in\Gamma}\left\lVert (z-B)^{-1}\right\rVert,$$ and $R_\Gamma=\max_{z\in\Gamma}|z|$. Then $$\boxed{
 \left\lVert \mathcal Q(A;\Gamma)-\mathcal Q(B;\Gamma)\right\rVert
 \le
 \frac{\operatorname{len}(\Gamma)}{2\pi}R_\Gamma M_AM_B\left\lVert A-B\right\rVert.}
 \label{eq:resolvent-lipschitz}$$

The first resolvent identity gives $$(z-A)^{-1}-(z-B)^{-1}
 =(z-A)^{-1}(A-B)(z-B)^{-1}.$$ Insert this into [\[eq:weighted-riesz\]](#eq:weighted-riesz){reference-type="eqref" reference="eq:weighted-riesz"}, take norms along the contour, and bound the Bochner integral by its arclength integral.

[\[cor:contour-persistence\]]{#cor:contour-persistence label="cor:contour-persistence"} Let $\delta=\left\lVert A-B\right\rVert$ and assume $M_A\delta<1$. Then $\Gamma\subset\rho(B)$, $$M_B\le\frac{M_A}{1-M_A\delta},
 \label{eq:perturbed-resolvent}$$ and $$\left\lVert \mathcal Q(A;\Gamma)-\mathcal Q(B;\Gamma)\right\rVert
 \le
 \frac{\operatorname{len}(\Gamma)}{2\pi}R_\Gamma
 \frac{M_A^2\delta}{1-M_A\delta}.
 \label{eq:one-sided-transfer}$$

Factor $$z-B=\{I-(B-A)(z-A)^{-1}\}(z-A).$$ The first factor is invertible by a uniformly convergent Neumann series. This proves [\[eq:perturbed-resolvent\]](#eq:perturbed-resolvent){reference-type="eqref" reference="eq:perturbed-resolvent"}; then apply [\[thm:resolvent-lipschitz\]](#thm:resolvent-lipschitz){reference-type="ref" reference="thm:resolvent-lipschitz"}.

The factor $M_AM_B$ is essential in a nonnormal problem. A geometric distance from $\Gamma$ to the spectrum does not, by itself, replace it. This is exactly where a visually stable eigenvalue gap stops being a validated projector theorem.

# A second-order Nyström bridge {#sec:nystrom}

Let $I=[0,1]$ and $k\in C^2(I\times I)$. Define $$(\mathcal Kf)(x)=\int_0^1k(x,y)f(y)\,dy.
 \label{eq:continuum-operator}$$ For $h=1/n$, use midpoint nodes $x_i=(i+\tfrac12)h$, $0\le i<n$, and the matrix $$(K_h)_{ij}=h k(x_i,x_j).
 \label{eq:nystrom-matrix}$$ Here $T$ denotes algebraic transpose: $l_h^T$ is the row eigenfunctional. For the archived real branches this agrees with the usual real left-vector notation; no Hermitian gauge convention is being imposed.

Suppose $\lambda\ne0$ is a simple isolated eigenvalue of $\mathcal K$. Its right eigenfunction and left eigenfunctional have $C^2$ representatives $r$ and $\ell$ because $$r=\lambda^{-1}\mathcal Kr,
 \qquad
 \ell=\lambda^{-1}\mathcal K^T\ell,$$ where $(\mathcal K^Tg)(y)=\int_0^1k(x,y)g(x)\,dx$. Choose the bilinear normalization $$\int_0^1\ell(x)r(x)\,dx=1.
 \label{eq:continuum-normalization}$$ The continuum weighted Riesz kernel is $$q(x,y)=\lambda r(x)\ell(y),
 \label{eq:continuum-weighted-kernel}$$ and its midpoint matrix is $$(Q_h^\circ)_{ij}=h q(x_i,x_j).
 \label{eq:continuum-sampled-term}$$

[\[thm:nystrom-weighted\]]{#thm:nystrom-weighted label="thm:nystrom-weighted"} For all sufficiently small $h$, $K_h$ has a simple eigenvalue $\lambda_h$ inside a fixed isolating contour for $\lambda$. Let $r_h,l_h\in\mathbb C^n$ be any corresponding right and left vectors normalized by $l_h^Tr_h=1$, and put $$Q_h=\lambda_h r_hl_h^T=\mathcal Q(K_h;\Gamma).
 \label{eq:discrete-weighted-term}$$ Then $$\left\lVert Q_h-Q_h^\circ\right\rVert_2=O(h^2).
 \label{eq:nystrom-weighted-rate}$$ The estimate is unchanged by every admissible rescaling of $r_h,l_h$.

Collectively compact Nyström theory gives spectral exactness for the nonzero isolated eigenvalue. Composite midpoint quadrature is second order on the smooth eigenfunctions. Applied to $k$ and to the transposed kernel $k^T(x,y)=k(y,x)$, the standard simple-branch estimates [@Atkinson1967; @Anselone1971; @Atkinson1997; @Chatelin1983] give compatible node vectors $\rho_h,\eta_h$ such that $$\begin{aligned}
 |\lambda_h-\lambda|&=O(h^2),\label{eq:eigenvalue-rate}\\
 \max_i|\rho_{h,i}-r(x_i)|
 +\max_i|\eta_{h,i}-\ell(x_i)|&=O(h^2),
 \label{eq:mode-rate}\end{aligned}$$ with $K_h\rho_h=\lambda_h\rho_h$ and $K_h^T\eta_h=\lambda_h\eta_h$.

Set $$a_h=h\sum_{i=0}^{n-1}\eta_{h,i}\rho_{h,i}.$$ By [\[eq:continuum-normalization\]](#eq:continuum-normalization){reference-type="eqref" reference="eq:continuum-normalization"}, [\[eq:mode-rate\]](#eq:mode-rate){reference-type="eqref" reference="eq:mode-rate"}, and the midpoint rule, $a_h=1+O(h^2)$. Hence we may choose $$r_h=\rho_h,\qquad l_h=\frac{h}{a_h}\eta_h,$$ which gives $l_h^Tr_h=1$. Uniform boundedness of $r,\ell$ and their approximants now implies, entrywise, $$\left|
 \lambda_h(r_h)_i(l_h)_j
 -h\lambda r(x_i)\ell(x_j)
 \right|=O(h^3).$$ For an $n\times n$ matrix with maximum entry $O(h^3)$, both the $1$- and $\infty$-norms are $O(nh^3)=O(h^2)$; their geometric mean bounds the spectral norm. This proves [\[eq:nystrom-weighted-rate\]](#eq:nystrom-weighted-rate){reference-type="eqref" reference="eq:nystrom-weighted-rate"}. Finally, $Q_h$ itself is invariant under the right-left gauge by [\[prop:intrinsic\]](#prop:intrinsic){reference-type="ref" reference="prop:intrinsic"}.

[\[cor:simple-cluster\]]{#cor:simple-cluster label="cor:simple-cluster"} If a fixed finite cluster consists of simple isolated nonzero eigenvalues with disjoint isolating contours, the sum of their weighted terms satisfies the same $O(h^2)$ matrix estimate.

Apply [\[thm:nystrom-weighted\]](#thm:nystrom-weighted){reference-type="ref" reference="thm:nystrom-weighted"} to each branch and add finitely many estimates.

The proof chooses one convenient normalization only to obtain an entrywise bound. The conclusion concerns $Q_h$, which is independent of that choice. Thus no sign-alignment, phase-alignment, or mode-ordering algorithm appears in the theorem statement.

## Discretely normalized smooth kernels

The archived full Markov matrix uses a discrete row normalizer. Let a positive $C^2$ raw kernel $g$ have continuum normalizer $$Z(x)=\int_0^1g(x,y)\,dy>0$$ and normalized kernel $k(x,y)=g(x,y)/Z(x)$. Its full midpoint Markov matrix is $$(P_h)_{ij}=\frac{g(x_i,x_j)}{\sum_m g(x_i,x_m)}.
 \label{eq:discrete-markov}$$ Equivalently, $P_h$ is the Nyström matrix of the $h$-dependent smooth kernel $g(x,y)/Z_h(x)$, where $Z_h(x)=h\sum_mg(x,x_m)$. Midpoint quadrature gives $Z_h-Z=O(h^2)$ uniformly.

[\[prop:discrete-normalization\]]{#prop:discrete-normalization label="prop:discrete-normalization"} If $\lambda\ne0$ is a simple isolated eigenvalue of the continuum-normalized operator with kernel $k=g/Z$, then its weighted term for the matrices $P_h$ in [\[eq:discrete-markov\]](#eq:discrete-markov){reference-type="eqref" reference="eq:discrete-markov"} is $O(h^2)$ close in spectral norm to the midpoint matrix of the continuum weighted kernel.

Positivity and compactness separate $Z$ uniformly from zero. Composite midpoint quadrature and $g\in C^2$ give $$\left\lVert Z_h-Z\right\rVert_\infty=O(h^2),\qquad
 \left\lVert g/Z_h-g/Z\right\rVert_\infty=O(h^2).$$ The $h$-dependent kernels $g/Z_h$ and their transposes remain uniformly smooth and collectively compact. The simple right and transposed-left Nyström branches therefore satisfy the estimates [\[eq:eigenvalue-rate\]](#eq:eigenvalue-rate){reference-type="eqref" reference="eq:eigenvalue-rate"}--[\[eq:mode-rate\]](#eq:mode-rate){reference-type="eqref" reference="eq:mode-rate"}; repeating the normalization and entrywise argument in [\[thm:nystrom-weighted\]](#thm:nystrom-weighted){reference-type="ref" reference="thm:nystrom-weighted"} proves the claim.

[\[cor:perron\]]{#cor:perron label="cor:perron"} Fix $\sigma>0$ and a smooth map $f$. On $I=[0,1]$, let $$g_\sigma(x,y)=
 \exp\!\left[-\frac{(y-f(x))^2}{2\sigma^2}\right]
 +
 \exp\!\left[-\frac{(y+f(x))^2}{2\sigma^2}\right].
 \label{eq:folded-kernel}$$ The continuum-normalized operator is compact, Markov, and strongly positive. Its eigenvalue $1$ is algebraically simple and isolated. Consequently the weighted Perron term of the full discretely normalized midpoint matrices satisfies [\[eq:nystrom-weighted-rate\]](#eq:nystrom-weighted-rate){reference-type="eqref" reference="eq:nystrom-weighted-rate"} without an additional spectral hypothesis.

The normalized kernel is strictly positive and smooth on the compact square. Strong positivity and Krein--Rutman theory make $1$ algebraically simple and exclude every other peripheral spectral value [@Schaefer1974; @WangContinuum2026]. Apply [\[prop:discrete-normalization\]](#prop:discrete-normalization){reference-type="ref" reference="prop:discrete-normalization"}.

[\[cor:parity\]]{#cor:parity label="cor:parity"} If the full folded-Gaussian continuum operator has a simple isolated nonzero negative resonance $\lambda_-$ continuing the archived parity branch, then its weighted Nyström term is $O(h^2)$ close in spectral norm to the midpoint matrix of $\lambda_-r_-(x)\ell_-(y)$. The combined Perron/parity rank-two term has the same rate.

The hypothesis in [\[cor:parity\]](#cor:parity){reference-type="ref" reference="cor:parity"} is not proved by three convergent-looking matrix eigenvalues. Establishing it requires either a validated continuum contour resolvent or an equivalent analytic isolation argument.

# Transfer through a Gaussian support cutoff {#sec:cutoff}

Let $P_h$ denote the full discretely normalized folded-Gaussian matrix and $\widehat P_h$ a support-truncated and renormalized version of the same dimension. Suppose $$\left\lVert \widehat P_h-P_h\right\rVert_2\le\varepsilon_h.
 \label{eq:markov-bridge}$$ For a fixed cluster contour $\Gamma$, put $$M_h=\max_{z\in\Gamma}\left\lVert (z-P_h)^{-1}\right\rVert_2.$$

[\[prop:cutoff-transfer\]]{#prop:cutoff-transfer label="prop:cutoff-transfer"} If $\sup_hM_h\le M<\infty$ and $M\varepsilon_h<1$ for all sufficiently small $h$, then $$\left\lVert \mathcal Q(\widehat P_h;\Gamma)-\mathcal Q(P_h;\Gamma)\right\rVert_2
 \le
 \frac{\operatorname{len}(\Gamma)}{2\pi}R_\Gamma
 \frac{M^2\varepsilon_h}{1-M\varepsilon_h}.
 \label{eq:cutoff-riesz-bound}$$ In particular, an $O(h^2)$ Markov bridge gives an $O(h^2)$ weighted-Riesz bridge.

Apply [\[cor:contour-persistence\]](#cor:contour-persistence){reference-type="ref" reference="cor:contour-persistence"} at each dimension.

The adaptive support schedule of @WangCutoff2026, $$L(h)=\max\{5,2\sqrt{\log(1/h)}\},
 \label{eq:adaptive-cutoff}$$ gives $$\varepsilon_h=O\!\left(h^2(\log(1/h))^{-1/4}\right).$$ Thus it transfers through [\[prop:cutoff-transfer\]](#prop:cutoff-transfer){reference-type="ref" reference="prop:cutoff-transfer"} under the displayed uniform resolvent condition. A fixed eight-sigma window is extraordinarily small at the archived grids, but it does not converge to the full kernel in row-operator norm when held fixed forever. The finite-grid observation and the all-grid theorem are therefore different statements.

For the Perron branch, [\[cor:perron\]](#cor:perron){reference-type="ref" reference="cor:perron"} closes the full smooth continuum bridge unconditionally. For the parity branch, two logically separate conditions remain: simple continuum isolation for [\[cor:parity\]](#cor:parity){reference-type="ref" reference="cor:parity"}, and uniform Euclidean contour conditioning for transfer through the nonsmooth cutoff. The latter may follow from a sufficiently strong validated version of the former, but it is not inferred from eigenvalue locations alone.

# Exact-stored rank-two Haar ledger {#sec:ledger}

We now study the binary64 factors archived in the two dyadic continuation papers. This section does not assert that they are exact eigenvectors of an exact-real sparse matrix. Instead, every stored binary64 number is treated as an exact real input and all subsequent low-rank identities are enclosed by Arb interval arithmetic [@Johansson2017; @Rump2010].

At dimension $n$, the stored term is $$Q_n=R_n\Lambda_nL_n^T,
 \qquad R_n,L_n\in\mathbb R^{n\times2}.
 \label{eq:stored-Q}$$ For a fine level $2n$, define paired right averages and differences $$\overline R_i=\frac{(R_{2n})_{2i}+(R_{2n})_{2i+1}}2,
 \qquad
 \delta R_i=\frac{(R_{2n})_{2i}-(R_{2n})_{2i+1}}2,$$ and paired left sums and differences $$\Sigma L_i=(L_{2n})_{2i}+(L_{2n})_{2i+1},
 \qquad
 \Delta L_i=(L_{2n})_{2i}-(L_{2n})_{2i+1}.$$ The exact unnormalized Haar blocks are then $$\begin{aligned}
 E_n&=\overline R\Lambda_{2n}(\Sigma L)^T
       -R_n\Lambda_nL_n^T,
 \label{eq:E-factor}\\
 C_n&=\delta R\Lambda_{2n}(\Sigma L)^T,
 \label{eq:C-factor}\\
 B_n&=\overline R\Lambda_{2n}(\Delta L)^T,
 \label{eq:B-factor}\\
 D_n&=\delta R\Lambda_{2n}(\Delta L)^T.
 \label{eq:D-factor}\end{aligned}$$ Thus $E_n$ has rank at most four and the other blocks rank at most two. No dense $n\times n$ block is needed.

For real low-rank factors $A,B$, $$\left\lVert AB^T\right\rVert_F^2
 =\operatorname{tr}\!\left((A^TA)(B^TB)\right).
 \label{eq:low-rank-frobenius}$$ The implementation forms both small Gram matrices using exact binary64 inputs inside 224-bit Arb balls. This matters most for $E_n$, whose two rank-two contributions nearly cancel; a binary64 evaluation of the small Gram identity loses visible digits even though no large dense matrix is formed.

## Rigorous block enclosures

gives outward-rounded Frobenius intervals. Their widths are much smaller than the printed precision.

::: {#tab:block-enclosures}
  block                                        $2048\to4096$                                      $4096\to8192$
  ------- -------------------------------------------------- --------------------------------------------------
  $E$       $[8.350827302101823,8.350827302101826]\,10^{-5}$   $[2.086176416513942,2.086176416513943]\,10^{-5}$
  $C$       $[2.574357393980523,2.574357393980524]\,10^{-3}$   $[1.287251360405133,1.287251360405134]\,10^{-3}$
  $B$       $[3.525041944225770,3.525041944225772]\,10^{-3}$   $[1.762662749289979,1.762662749289980]\,10^{-3}$
  $D$       $[6.244505599125109,6.244505599125111]\,10^{-6}$   $[1.561308946412573,1.561308946412575]\,10^{-6}$

  : 224-bit Arb enclosures for exact-stored weighted-term Haar block Frobenius norms.
:::

Dividing the second interval by the first with outward rounding gives [2](#tab:ratios){reference-type="ref" reference="tab:ratios"}. This is a rigorous property of the exact stored factors, not an asymptotic theorem inferred from two ratios.

::: {#tab:ratios}
  block                 ratio enclosure
  ------- -------------------------------------------
  $E$      $[0.2498167356411347,0.2498167356411349]$
  $C$      $[0.5000282258458135,0.5000282258458139]$
  $B$      $[0.5000402199971905,0.5000402199971907]$
  $D$      $[0.2500292331599994,0.2500292331599995]$

  : Outward-rounded exact-stored second-to-first Frobenius ratios.
:::

::: {#tab:renormalized}
  block              $2048\to4096$                       $4096\to8192$
  ------- ----------------------------------- -----------------------------------
  $E$      $[350.2590835651,350.2590835652]$   $[350.0023235396,350.0023235397]$
  $C$      $[5.272283942872,5.272283942873]$   $[5.272581572219,5.272581572220]$
  $B$      $[7.219285901774,7.219285901775]$   $[7.219866621091,7.219866621092]$
  $D$      $[26.19135481243,26.19135481244]$   $[26.19441743669,26.19441743670]$

  : Outward-rounded renormalized exact-stored Frobenius constants. $E,D$ are divided by $h^2$ and $C,B$ by $h$.
:::

The two second-order ratios lie within $1.84\times10^{-4}$ and $2.93\times10^{-5}$ of one quarter. The two first-order ratios lie within $2.83\times10^{-5}$ and $4.03\times10^{-5}$ of one half. This is the exact stored-factor counterpart of the smooth theorem in [\[eq:quarter-half-intro\]](#eq:quarter-half-intro){reference-type="eqref" reference="eq:quarter-half-intro"}.

## Biorthogonality and floating isolation audit

The Arb ledger also encloses $L_n^TR_n-I$ directly. Sparse eigen-residuals and the leading spectrum are then recomputed in binary64 only as diagnostics.

::: {#tab:isolation}
     $n$         $\lambda_{-,n}$   $\left\lVert L_n^TR_n-I\right\rVert_2$ upper        max residual   parity/bulk radial gap
  ------ ----------------------- ---------------------------------------------- ------------------- ------------------------
    2048   $-0.9865534036028739$                             $2.0070\,10^{-15}$   $3.307\,10^{-15}$              $0.3118841$
    4096   $-0.9865481927458079$                             $2.8849\,10^{-15}$   $3.516\,10^{-15}$              $0.3118789$
    8192   $-0.9865468907775788$                             $1.3674\,10^{-15}$   $3.395\,10^{-15}$              $0.3118776$

  : Stored branch and isolation audit. Only the biorthogonality column is an exact-stored Arb upper; the eigenvalues, residuals, and observed bulk are floating diagnostics.
:::

The successive parity increments are exactly evaluated from the stored binary64 eigenvalues inside Arb balls. Their ratio is enclosed by $$0.24985683017206403
 \le\frac{\lambda_{8192}-\lambda_{4096}}
          {\lambda_{4096}-\lambda_{2048}}
 \le0.24985683017206410.
 \label{eq:parity-ratio}$$ The two second-order Richardson extrapolates are $$\begin{aligned}
 R_1&=-0.9865464557934524962\ldots,\\
 R_2&=-0.9865464567881691756\ldots,\end{aligned}$$ with $$|R_2-R_1|\le9.947166793959168\times10^{-10}.
 \label{eq:richardson-gap}$$

The largest stored weighted-term spectral norm is $1.24055$, and the largest unweighted projector spectral norm is $1.14810$. These moderate values and the stable observed radial gap explain why ordinary floating continuation is well behaved on the three grids. They do not bound the resolvent on a continuum contour.

![Weighted-Riesz bridge diagnostics. (a) The archived negative branch is consistent with second-order Nyström convergence, including two nearly coincident Richardson extrapolates. (b) Arb intervals close the exact-stored quarter--half Frobenius ledger. (c) Division by the predicted powers leaves nearly level-independent constants. (d) The negative branch remains separated from the twelve-mode observed bulk while eigen-residual and biorthogonality diagnostics stay near machine precision. Panel (d) is not a validated continuum isolation result.](<../../../../../zeta_mvp0/papers/RH-40-weighted-riesz-projector-bridge/figures/weighted_riesz_projector_bridge.pdf>){#fig:summary width="\\textwidth"}

# What is closed and what remains {#sec:boundary}

The projector bridge can now be stated without conflating evidence levels.

1.  **Weighted Riesz stability is analytic.** is an exact operator theorem and includes the nonnormal conditioning explicitly.

2.  **The full smooth Nyström bridge is analytic.** A simple isolated nonzero branch gives $\left\lVert Q_h-Q_h^\circ\right\rVert_2=O(h^2)$ without choosing a persistent eigenvector gauge.

3.  **The Perron instance is unconditional.** Strong positivity supplies simplicity and isolation for the full folded-Gaussian continuum operator.

4.  **The parity instance is conditional.** The same conclusion follows if the archived negative branch is shown to continue a simple isolated continuum resonance. The current eigenvalue table does not prove that premise.

5.  **The cutoff transfer is conditional on contour conditioning.** The adaptive $O(h^2)$ matrix bridge propagates to $Q_h$ once a uniform Euclidean contour-resolvent bound is supplied.

6.  **The stored Haar ledger is rigorous for its stated inputs.** The Arb intervals prove exact algebraic properties of the stored binary64 factors. Their status as spectral factors of the stored sparse matrices is still supported only by floating residuals.

Accordingly, the single remaining *analytic* gate in the rank-two continuum bridge is parity simplicity and isolation, preferably in a form that also controls the contour resolvent needed by [\[prop:cutoff-transfer\]](#prop:cutoff-transfer){reference-type="ref" reference="prop:cutoff-transfer"}. A fully validated finite-grid statement would add two computational gates: interval enclosure of the sparse eigensolver and outward-rounded construction of the binary64 Gaussian matrices.

Only two dyadic transitions are archived. They strongly identify the quarter--half mechanism but cannot prove a uniform all-level constant by themselves. The present paper also does not address the later hierarchical Schur-resolvent recursion, a zero-noise limit, a self-adjoint generator, or any arithmetic spectral identification.

# Archive and reproducibility {#sec:archive}

The repository contains the exact-stored factors only through hashes of the RH-36 and RH-37 snapshots; the snapshots themselves remain in their source paper directories. The RH-40 certificate records those hashes together with the RH-38 Haar and RH-39 cutoff certificates.

The fast replay is

    python -m pytest -q -p no:cacheprovider
    python experiments/run_projector_pilot.py
    python experiments/build_projector_certificate.py
    MPLBACKEND=Agg python experiments/make_figures.py
    latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
    cp main.pdf weighted-riesz-projector-bridge.pdf
    python experiments/build_archive.py
    python experiments/verify_archive.py

The pilot recomputes sparse residuals and leading eigenvalues. The certificate then treats the resulting archived factors as exact inputs and uses the low-rank identity [\[eq:low-rank-frobenius\]](#eq:low-rank-frobenius){reference-type="eqref" reference="eq:low-rank-frobenius"}. The archive verifier checks dependency hashes, formulas, interval gates, publication artifacts, and the explicit limitations.

# Conclusion

The appropriate continuum object for peripheral subtraction is not a chosen pair of eigenvectors but the weighted Riesz term $A\Pi$. This replacement removes every gauge convention and exposes the only perturbative quantity that a nonnormal theorem genuinely needs: the contour resolvent.

For a smooth simple Nyström branch, the weighted term is second-order close in Euclidean matrix norm to the midpoint sample of its continuum kernel. Strong positivity closes this statement for the Perron branch of the full folded-Gaussian operator. The same theorem is ready for the archived negative branch as soon as its continuum simplicity and isolation are established. Under uniform contour conditioning, the adaptive Gaussian cutoff passes through the weighted Riesz calculus at the same order.

The exact-stored rank-two factors independently obey the predicted dyadic quarter--half law, with Arb-enclosed ratios within $2\times10^{-4}$ of their ideal values and biorthogonality defects below $3\times10^{-15}$. The maze has therefore narrowed again: vector normalization is no longer an obstruction, and the next mathematically meaningful target is a validated continuum contour for the negative resonance.
