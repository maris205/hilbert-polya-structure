---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-45-bulk-two-step-trace-norm-determinant"
canonical_tex: "zeta_mvp0/papers/RH-45-bulk-two-step-trace-norm-determinant/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-45-bulk-two-step-trace-norm-determinant/bulk-two-step-trace-norm-determinant.pdf"
source_sha256: "3049da36ac45191cf4c8d4d8797307b2ef071100c5c25950d4cbea75e3058fc0"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Trace-Ideal Completion of the Intrinsic Bulk Two-Step Operator Hilbert--Schmidt Convergence, Trace-Norm Squares, and Fredholm Determinants

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-45-bulk-two-step-trace-norm-determinant>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-45-bulk-two-step-trace-norm-determinant/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-45-bulk-two-step-trace-norm-determinant/bulk-two-step-trace-norm-determinant.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-45-bulk-two-step-trace-norm-determinant/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-45-bulk-two-step-trace-norm-determinant/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  An intrinsic rank-two subtraction has isolated the Perron and negative parity modes of a folded-Gaussian Markov operator at fixed noise $\sigma=10^{-2}$. The resulting bulk operator $$\mathcal B=\mathcal K-\mathcal Q_+-\mathcal Q_-$$ is the natural one-step complement, but convergence of ordinary Fredholm determinants would require trace-norm control that is not supplied by the piecewise-constant discretization. We close the trace-ideal gap by passing to the intrinsic two-step operator.

  For the full exact-real midpoint family and the adaptive Gaussian-cutoff family, lifted to $L^2([0,1])$, we prove $$\left\lVert B_n-\mathcal B\right\rVert_{\mathfrak S_2}=O(n^{-1}).$$ Since products of two Hilbert--Schmidt operators are trace class, $$\left\lVert B_n^2-\mathcal B^2\right\rVert_{\mathfrak S_1}
   \le \left\lVert B_n-\mathcal B\right\rVert_{\mathfrak S_2}
       \bigl(\left\lVert B_n\right\rVert_{\mathfrak S_2}
             +\left\lVert \mathcal B\right\rVert_{\mathfrak S_2}\bigr)
   =O(n^{-1}).$$ Consequently every fixed even bulk trace converges, and the Fredholm determinants $$\mathcal D_{n,\mathrm{bulk}}(w)=\operatorname{det}(\mathrm I-wB_n^2)$$ converge locally uniformly on the entire $w$-plane to $\mathcal D_{\mathrm{bulk}}(w)=\operatorname{det}(\mathrm I-w\mathcal B^2)$. The construction is exactly the symmetric completion of the regularized one-step determinant: $$\operatorname{det}\nolimits_2(\mathrm I-z\mathcal B)\operatorname{det}\nolimits_2(\mathrm I+z\mathcal B)
   =\operatorname{det}(\mathrm I-z^2\mathcal B^2).$$

  The validated continuum bound is $\left\lVert \mathcal B\right\rVert_{\mathfrak S_2}\le15.418003788081082$. At $n=65536$ the outward bounds are $0.1281382922864061$ in Hilbert--Schmidt norm and $3.967692773690177$ in square trace norm. At $n=2^{30}$ they decrease to $3.785070933298939\times10^{-6}$ and $1.167164903022793\times10^{-4}$; on $|w|\le10^{-2}$ the corresponding uniform determinant error is at most $3.682918268863141\times10^{-4}$. A separate floating sparse-LU pilot at $2048$, $4096$, and $8192$ shows a mean dyadic determinant-difference ratio $0.2493$, but this sharper center behavior is not used in the theorem.

  All results are at fixed positive noise. No zero-noise limit, arithmetic trace formula, prime-power identity, zeta-zero correspondence, self-adjoint Hilbert--Pólya operator, or Riemann-hypothesis conclusion is asserted.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  A Trace-Ideal Completion of the Intrinsic Bulk Two-Step Operator\
  Hilbert--Schmidt Convergence, Trace-Norm Squares, and Fredholm Determinants
```

## Markdown 正文

**Keywords:** Hilbert--Schmidt operator; trace ideal; Fredholm determinant; regularized determinant; Riesz projection; Markov operator; Nyström approximation.

**MSC 2020:** 47B10; 47A10; 65R20; 37M25; 60J05.

# Introduction {#sec:introduction}

The useful spectral object in a noisy dynamical system is often not the full transfer operator but the complement left after isolated peripheral modes have been removed. For the folded-Gaussian Markov operator studied in this series, the Perron eigenvalue $1$ and a simple negative resonance near $-1$ have now been isolated by explicit Euclidean contours. Their weighted Riesz terms are intrinsic, real, smooth, and gauge-free. Thus the one-step bulk operator $$\mathcal B=\mathcal K-\mathcal Q_+-\mathcal Q_-
 \label{eq:bulk-intro}$$ is no longer a numerical ansatz: it is a rigorously defined continuum operator with validated full and sparse discretizations [@WangParityKernel2026; @WangRankTwo2026].

That completion leaves a trace-ideal mismatch. The most natural cellwise comparison is Hilbert--Schmidt. If $k_n$ is a piecewise-constant kernel approximation to a smooth kernel $k$, then $$\left\lVert k_n-k\right\rVert_{L^2([0,1]^2)}=O(n^{-1})$$ without requiring pointwise interpolation. Under the standard isometry between matrices and piecewise-constant integral operators, this is exactly Hilbert--Schmidt convergence. It does not by itself imply trace-norm convergence. Therefore one cannot simply pass from $B_n\to\mathcal B$ in $\mathfrak S_2$ to local uniform convergence of $\operatorname{det}(\mathrm I-zB_n)$.

The two-step operator has the missing regularity automatically. The trace ideal product rule $$\mathfrak S_2\mathfrak S_2\subset\mathfrak S_1$$ turns the elementary factorization $$B_n^2-\mathcal B^2=(B_n-\mathcal B)B_n+\mathcal B(B_n-\mathcal B)$$ into a trace-norm estimate. This is the central mechanism of the paper. It is abstract, short, and independent of normality or self-adjointness. All dynamical work enters through the explicit Hilbert--Schmidt error ledger for $B_n-\mathcal B$.

There are three reasons that the squared determinant is the correct next object.

1.  It is intrinsic. Both peripheral branches have already been removed by weighted Riesz calculus; no ordering or normalization of eigenvectors remains in the definition.

2.  It is trace class under exactly the topology delivered by the discretization. No unproved trace-norm approximation of the one-step operator is inserted.

3.  It joins the regularized determinant of the long-cycle analysis by the exact identity $$\operatorname{det}\nolimits_2(\mathrm I-z\mathcal B)\operatorname{det}\nolimits_2(\mathrm I+z\mathcal B)
      =\operatorname{det}(\mathrm I-z^2\mathcal B^2).$$ The linear regularization terms cancel between $z$ and $-z$.

The distinction between these statements and a Hilbert--Pólya construction is substantial. The operator $\mathcal B$ is nonnormal, the determinant is attached to one fixed positive noise width, and no arithmetic trace formula is available. Squaring packages the even spectral traces; it does not make the operator self-adjoint and it does not identify any determinant zero with a Riemann zero. The result established here is a functional-analytic bridge needed before such comparisons can even be formulated cleanly.

## Main contribution and evidence levels {#main-contribution-and-evidence-levels .unnumbered}

The paper keeps three logical layers separate.

Analytic theorem

:   Hilbert--Schmidt-to-trace-norm squaring, even-trace convergence, Fredholm determinant continuity, and the symmetric $\det_2$ identity.

Outward certificate

:   Explicit continuum kernel bounds, Hilbert--Galerkin errors, midpoint and row-normalization errors, adaptive Gaussian-cutoff errors, and Perron/parity weighted-Riesz transport for every $n\ge65536$.

Floating diagnostic

:   Sparse-LU determinant values for the exact archived binary64 matrices at $2048$, $4096$, and $8192$. These values illustrate stabilization but prove no continuum statement.

# Operator, contours, and discretizations {#sec:operator}

Let $u_{\mathrm c}$ be the unique root in $(1.5,1.6)$ of $$u^3-2u^2+2u-2=0,$$ fix $\sigma=1/100$, and put $$m(x)=1-u_{\mathrm c}x^2.$$ For $x,y\in[0,1]$, define $$\begin{aligned}
 g(x,y)&=
 e^{-(y-m(x))^2/(2\sigma^2)}
 +e^{-(y+m(x))^2/(2\sigma^2)},
 \label{eq:g-kernel}\\
 Z(x)&=\int_0^1g(x,y)\,dy,
 \qquad
 k(x,y)=\frac{g(x,y)}{Z(x)}.
 \label{eq:normalized-kernel}\end{aligned}$$ The folded Markov operator on $H=L^2([0,1])$ is $$(\mathcal Kf)(x)=\int_0^1k(x,y)f(y)\,dy.
 \label{eq:markov-operator}$$ Its kernel is real, strictly positive, and smooth on the compact square, and $\mathcal K\mathbf1=\mathbf1$.

The validated contours are $$\begin{aligned}
 \Gamma_+&=\{z\in\mathbb C:|z-1|=0.05\},
 \label{eq:perron-contour}\\
 \Gamma_-&=\{z\in\mathbb C:|z+0.9865481927458079|=0.05\}.
 \label{eq:parity-contour}\end{aligned}$$ Each contains one algebraically simple eigenvalue, and the circles are disjoint. Their weighted Riesz terms are $$\mathcal Q_\pm
 =\frac{1}{2\pi i}\int_{\Gamma_\pm}
 z(z-\mathcal K)^{-1}\,dz.
 \label{eq:weighted-riesz}$$ For the Perron branch, $\mathcal Q_+$ is also the rank-one projection $f\mapsto\mathbf1\langle\pi,f\rangle$, where $\mathcal K^*\pi=\pi$ and $\int_0^1\pi=1$. For the negative branch, $\mathcal Q_-=\lambda_-\mathcal P_-$, where $\mathcal P_-$ is its Riesz projection. The terms commute with $\mathcal K$, annihilate one another, and have smooth real rank-one kernels. We use the bulk definition [\[eq:bulk-intro\]](#eq:bulk-intro){reference-type="eqref" reference="eq:bulk-intro"}.

## Cell spaces and lifted matrices

Let $I_{n,j}=[j/n,(j+1)/n)$ and let $V_n\subset H$ be the space of functions constant on the $n$ cells. The vectors $$e_{n,j}=\sqrt n\,\mathbf1_{I_{n,j}},
 \qquad 0\le j<n,$$ form an orthonormal basis. Write $E_n$ for the orthogonal projection onto $V_n$ and $J_n:\mathbb C^n\to V_n$ for the corresponding isometry. Every matrix $A_n$ is compared with the continuum through the zero-complement lift $$\widehat A_n=J_nA_nJ_n^*.
 \label{eq:matrix-lift}$$ Then $$\left\lVert \widehat A_n\right\rVert_{\mathfrak S_2}=\left\lVert A_n\right\rVert_{\mathrm F}.$$ We suppress the hat after this convention has been fixed.

Let $x_i=y_i=(i+\tfrac12)/n$ and $h=1/n$. The continuum-normalized midpoint matrix is $$(P_n^\circ)_{ij}=h k(x_i,y_j).
 \label{eq:midpoint-matrix}$$ The full exact-real matrix $P_n$ row-normalizes the unnormalized folded Gaussian midpoint weights. The adaptive matrix $P_n^{\mathrm{ad}}$ first retains destinations within $L_n\sigma$ of either folded mean and then renormalizes, where $$L_n=\max\{8,2\sqrt{\log n}\}.
 \label{eq:adaptive-schedule}$$ At $n=2048,4096,8192$, one has $L_n=8$, so the archived fixed-width matrices are also exact members of the declared adaptive sequence.

For $F_n\in\{P_n,P_n^{\mathrm{ad}}\}$, define $$Q_{\pm,n}
 =\frac{1}{2\pi i}\int_{\Gamma_\pm}
 z(z-F_n)^{-1}\,dz,
 \qquad
 B_n=F_n-Q_{+,n}-Q_{-,n}.
 \label{eq:discrete-bulk}$$ The all-grid contour theorem of the preceding work makes these definitions valid for every integer $n\ge65536$.

# The abstract trace-ideal mechanism {#sec:abstract}

We write $\mathfrak S_2(H)$ and $\mathfrak S_1(H)$ for the Hilbert--Schmidt and trace-class ideals. Their norms are denoted by $\left\lVert \cdot\right\rVert_2$ and $\left\lVert \cdot\right\rVert_1$ in this section.

[\[lem:square-continuity\]]{#lem:square-continuity label="lem:square-continuity"} If $X,Y\in\mathfrak S_2(H)$, then $X^2,Y^2\in\mathfrak S_1(H)$ and $$\left\lVert X^2-Y^2\right\rVert_1
 \le \left\lVert X-Y\right\rVert_2\bigl(\left\lVert X\right\rVert_2+\left\lVert Y\right\rVert_2\bigr).
 \label{eq:square-continuity}$$

Use $$X^2-Y^2=(X-Y)X+Y(X-Y)$$ and the ideal inequality $\left\lVert AC\right\rVert_1\le\left\lVert A\right\rVert_2\left\lVert C\right\rVert_2$ for $A,C\in\mathfrak S_2(H)$ [@Simon2005; @GohbergKrein1969].

[\[thm:abstract\]]{#thm:abstract label="thm:abstract"} Suppose $B_n,B\in\mathfrak S_2(H)$ and $$\left\lVert B_n-B\right\rVert_2\le\varepsilon_n,
 \qquad
 \left\lVert B\right\rVert_2\le M.
 \label{eq:abstract-hs-input}$$ Put $$\delta_n=\varepsilon_n(2M+\varepsilon_n).
 \label{eq:delta-definition}$$ Then $$\begin{aligned}
 \left\lVert B^2\right\rVert_1&\le M^2,
 \label{eq:continuum-square-trace-upper}\\
 \left\lVert B_n^2\right\rVert_1&\le(M+\varepsilon_n)^2,
 \label{eq:discrete-square-trace-upper}\\
 \left\lVert B_n^2-B^2\right\rVert_1&\le\delta_n.
 \label{eq:trace-norm-square-error}\end{aligned}$$ For every fixed integer $m\ge1$, $$\left|\operatorname{tr}(B_n^{2m})-\operatorname{tr}(B^{2m})\right|
 \le m\delta_n
 \left[\max\{M^2,(M+\varepsilon_n)^2\}\right]^{m-1}.
 \label{eq:even-trace-error}$$ Moreover, with $$\mathcal D_n(w)=\operatorname{det}(\mathrm I-wB_n^2),
 \qquad
 \mathcal D(w)=\operatorname{det}(\mathrm I-wB^2),
 \label{eq:determinants-defined}$$ one has, for every $R\ge0$, $$\sup_{|w|\le R}|\mathcal D_n(w)-\mathcal D(w)|
 \le R\delta_n
 \exp\!\left(1+RM^2+R(M+\varepsilon_n)^2\right).
 \label{eq:determinant-disk-bound}$$ In particular, $\varepsilon_n\to0$ implies local uniform convergence $\mathcal D_n\to\mathcal D$ on $\mathbb C$.

The first three bounds follow from $\left\lVert AC\right\rVert_1\le\left\lVert A\right\rVert_2\left\lVert C\right\rVert_2$, the triangle inequality, and [\[lem:square-continuity\]](#lem:square-continuity){reference-type="ref" reference="lem:square-continuity"}. For traces, put $A_n=B_n^2$ and $A=B^2$. The telescoping identity $$A_n^m-A^m
 =\sum_{j=0}^{m-1}A_n^j(A_n-A)A^{m-1-j}$$ and $\left\lVert RST\right\rVert_1\le\left\lVert R\right\rVert\,\left\lVert S\right\rVert_1\,\left\lVert T\right\rVert$ give $$\left\lVert A_n^m-A^m\right\rVert_1
 \le m\left\lVert A_n-A\right\rVert_1
 \max\{\left\lVert A_n\right\rVert,\left\lVert A\right\rVert\}^{m-1}.$$ Use $\left\lVert A\right\rVert\le\left\lVert A\right\rVert_1$ and $|\operatorname{tr}C|\le\left\lVert C\right\rVert_1$.

For determinants, the standard trace-ideal continuity estimate is $$|\operatorname{det}(\mathrm I+C)-\operatorname{det}(\mathrm I+D)|
 \le\left\lVert C-D\right\rVert_1
 e^{1+\left\lVert C\right\rVert_1+\left\lVert D\right\rVert_1}
 \label{eq:standard-determinant-bound}$$ for trace-class $C,D$ [@Simon2005]. Apply it to $C=-wB_n^2$ and $D=-wB^2$, then maximize over $|w|\le R$.

[\[rem:one-step-boundary\]]{#rem:one-step-boundary label="rem:one-step-boundary"} At the fixed smooth Gaussian kernel, stronger trace-class regularity of $\mathcal B$ is available. What is not supplied by the present discretization ledger is convergence $B_n\to\mathcal B$ in trace norm. The theorem therefore does not infer convergence of $\operatorname{det}(\mathrm I-zB_n)$ from Hilbert--Schmidt convergence. Passing to $B_n^2$ is the rigorously justified trace-ideal completion.

# Hilbert--Schmidt convergence of the intrinsic bulk {#sec:hs-convergence}

The dynamical part of the argument is to construct an explicit $\varepsilon_n$ in [\[eq:abstract-hs-input\]](#eq:abstract-hs-input){reference-type="eqref" reference="eq:abstract-hs-input"}. It has a Markov-kernel part and two weighted-Riesz parts.

## Continuum to cell-average Galerkin

Let $k_n^{\mathrm G}$ be the kernel of $E_n\mathcal KE_n$. Applying the cellwise Poincaré--Wirtinger inequality in the source and target variables gives $$\left\lVert \mathcal K-E_n\mathcal KE_n\right\rVert_{\mathfrak S_2}
 =\left\lVert k-k_n^{\mathrm G}\right\rVert_{L^2([0,1]^2)}
 \le\frac{1}{\pi n}
 \left(\left\lVert k_x\right\rVert_{L^2}+\left\lVert k_y\right\rVert_{L^2}\right).
 \label{eq:hs-galerkin}$$ This first-order term is the asymptotic bottleneck of the current proof. It is the natural price of lifting a smooth kernel by cell constants rather than a higher-order basis.

## Midpoint and exact row normalization

The one-dimensional midpoint-average Peano kernel has $L^2$ norm $h^{3/2}/\sqrt{320}$. Tensor decomposition therefore gives $$\left\lVert E_n\mathcal KE_n-P_n^\circ\right\rVert_{\mathfrak S_2}
 \le \frac{h^2}{\sqrt{320}}
 \left(\left\lVert k_{xx}\right\rVert_{L^2}+\left\lVert k_{yy}\right\rVert_{L^2}\right)
 +\frac{h^4}{320}\left\lVert k_{xxyy}\right\rVert_{L^2}.
 \label{eq:midpoint-hs}$$

Let $Z_*>0$ be the validated normalizer lower bound and put $$a_n=\frac{e^{-1/2}}{\sigma}h^2,
 \qquad
 \rho_n=\frac{a_n}{Z_*-a_n}.
 \label{eq:normalization-scaling}$$ Exact row normalization is a diagonal left scaling whose relative defect is at most $\rho_n$. Hence $$\left\lVert P_n-P_n^\circ\right\rVert_{\mathfrak S_2}
 \le \rho_n
 \left(\left\lVert k\right\rVert_{L^2}+\left\lVert E_n\mathcal KE_n-P_n^\circ\right\rVert_{\mathfrak S_2}\right).
 \label{eq:normalization-hs}$$ Although the inherited certificate field was originally named "spectral norm defect," its derivation is a relative row-scaling bound times a Frobenius kernel norm. It is therefore also a valid Hilbert--Schmidt upper bound.

## Adaptive Gaussian cutoff

For a declared support multiple $L$, the omitted row mass obeys $$\mu_{n,L}
 \le
 \frac{2\sqrt e\,e^{-L^2/2}(h+\sigma/L)}{\sigma-h}.
 \label{eq:cutoff-mass}$$ Writing $\alpha_{n,L}=\mu_{n,L}/(1-\mu_{n,L})$, the omitted and renormalization terms give the Frobenius-square ledger $$\begin{aligned}
 \left\lVert P_n^{(L)}-P_n\right\rVert_{\mathfrak S_2}^2
 \le{}&
 \frac{4e\,e^{-L^2}(h+\sigma/(2L))}{(\sigma-h)^2}
 \notag\\
 &+\frac{e\alpha_{n,L}^2(4h+2\sqrt\pi\sigma)}{(\sigma-h)^2}.
 \label{eq:cutoff-hs}\end{aligned}$$ Thus [\[eq:adaptive-schedule\]](#eq:adaptive-schedule){reference-type="eqref" reference="eq:adaptive-schedule"} gives $$\left\lVert P_n^{\mathrm{ad}}-P_n\right\rVert_{\mathfrak S_2}
 =O\!\left(n^{-2}(\log n)^{-1/4}\right).
 \label{eq:adaptive-cutoff-rate}$$ The certificate field for [\[eq:cutoff-hs\]](#eq:cutoff-hs){reference-type="eqref" reference="eq:cutoff-hs"} is also historically named "spectral norm upper," but it is explicitly the square root of a Frobenius-square ledger and may be used in $\mathfrak S_2$.

## Weighted-Riesz transport

For a circle $\Gamma$ of radius $r$, with $R_\Gamma=\max_{z\in\Gamma}|z|$, the resolvent identity gives $$\left\lVert \mathcal Q(A;\Gamma)-\mathcal Q(C;\Gamma)\right\rVert
 \le rR_\Gamma M_A M_C\left\lVert A-C\right\rVert,
 \label{eq:weighted-lipschitz}$$ provided the two contour resolvents are bounded by $M_A$ and $M_C$. The validated continuum bounds are $$\sup_{\Gamma_+}\left\lVert (z-\mathcal K)^{-1}\right\rVert
 \le81.30575843422578,
 \qquad
 \sup_{\Gamma_-}\left\lVert (z-\mathcal K)^{-1}\right\rVert
 \le112.95503061584434.
 \label{eq:continuum-resolvents}$$

The comparison between the continuum weighted term and its Galerkin compression uses the orthogonal splitting $H=V_n\oplus V_n^\perp$. The source-to-detail and target-to-detail blocks are $O(n^{-1})$, while the detail block is $O(n^{-2})$. Schur inversion leaves four weighted resolvent blocks. In particular, the top-left Schur inverse is the $V_n$ compression of the complete continuum resolvent, so its norm is at most the corresponding bound in [\[eq:continuum-resolvents\]](#eq:continuum-resolvents){reference-type="eqref" reference="eq:continuum-resolvents"}. This is the reason the certificate may use the continuum resolvent as the "Schur-inverse upper."

Let $\eta_{\pm,n}$ denote the complete operator-norm weighted-term error after the complement Schur transport, midpoint transfer, exact normalization, and, when applicable, adaptive cutoff. Since both the continuum and discrete weighted terms have rank one, $$\operatorname{rank}(Q_{\pm,n}-\mathcal Q_\pm)\le2,
 \qquad
 \left\lVert Q_{\pm,n}-\mathcal Q_\pm\right\rVert_{\mathfrak S_2}
 \le\sqrt2\,\eta_{\pm,n}.
 \label{eq:rank-two-hs-conversion}$$ All transferred contour gates are closed at $n=65536$. Every input defect decreases with $n$, and $L_n$ is nondecreasing, so the same is true for every integer $n\ge65536$.

[\[thm:bulk-hs\]]{#thm:bulk-hs label="thm:bulk-hs"} For the full and adaptive families in [\[eq:discrete-bulk\]](#eq:discrete-bulk){reference-type="eqref" reference="eq:discrete-bulk"}, and every integer $n\ge65536$, there are explicit outward numbers $\varepsilon_n^{\mathrm{full}}$ and $\varepsilon_n^{\mathrm{ad}}$ such that $$\begin{aligned}
 \left\lVert B_n^{\mathrm{full}}-\mathcal B\right\rVert_{\mathfrak S_2}
 &\le\varepsilon_n^{\mathrm{full}}=O(n^{-1}),
 \label{eq:full-hs-rate}\\
 \left\lVert B_n^{\mathrm{ad}}-\mathcal B\right\rVert_{\mathfrak S_2}
 &\le\varepsilon_n^{\mathrm{ad}}=O(n^{-1}).
 \label{eq:adaptive-hs-rate}\end{aligned}$$ They are composed as $$\varepsilon_n
 =\eta_{K,n}+\sqrt2(\eta_{+,n}+\eta_{-,n}),
 \label{eq:bulk-ledger-composition}$$ where $\eta_{K,n}$ is the appropriate full or adaptive Markov Hilbert--Schmidt defect.

The intrinsic continuum bulk satisfies $$\left\lVert \mathcal B\right\rVert_{\mathfrak S_2}
 \le \left\lVert \mathcal K\right\rVert_{\mathfrak S_2}
     +\left\lVert \mathcal Q_++\mathcal Q_-\right\rVert_{\mathfrak S_2}
 \le15.418003788081082.
 \label{eq:bulk-hs-upper}$$

Add [\[eq:hs-galerkin\]](#eq:hs-galerkin){reference-type="eqref" reference="eq:hs-galerkin"}, [\[eq:midpoint-hs\]](#eq:midpoint-hs){reference-type="eqref" reference="eq:midpoint-hs"}, and [\[eq:normalization-hs\]](#eq:normalization-hs){reference-type="eqref" reference="eq:normalization-hs"}, together with [\[eq:cutoff-hs\]](#eq:cutoff-hs){reference-type="eqref" reference="eq:cutoff-hs"} for the adaptive family. Add the two weighted-term errors using [\[eq:rank-two-hs-conversion\]](#eq:rank-two-hs-conversion){reference-type="eqref" reference="eq:rank-two-hs-conversion"}. The first-order terms are the cellwise Galerkin defect and the continuum-complement weighted transport; all other terms are second order or smaller. The final continuum bound uses the validated values $$\left\lVert \mathcal K\right\rVert_{\mathfrak S_2}\le5.498549224049743,
 \qquad
 \left\lVert \mathcal Q_++\mathcal Q_-\right\rVert_{\mathfrak S_2}
 \le9.919454564031339.$$

The fixed-width family remains uniformly spectrally stable and its peripheral terms are well defined. Its omitted Gaussian mass has a nonzero continuum floor, so this paper does not claim that the fixed eight-sigma family converges to $\mathcal B$ in Hilbert--Schmidt norm. Adaptive growth is essential to the continuum theorem.

# Trace-norm squares and even bulk traces {#sec:trace-norm}

Combining [\[thm:abstract,thm:bulk-hs\]](#thm:abstract,thm:bulk-hs){reference-type="ref" reference="thm:abstract,thm:bulk-hs"} immediately closes the two-step trace ideal.

[\[thm:bulk-square\]]{#thm:bulk-square label="thm:bulk-square"} For the full and adaptive families, every integer $n\ge65536$ satisfies $$\left\lVert (B_n^{\star})^2-\mathcal B^2\right\rVert_{\mathfrak S_1}
 \le\delta_n^{\star}
 :=\varepsilon_n^{\star}
 \left(30.836007576162164+\varepsilon_n^{\star}\right),
 \qquad
 \star\in\{\mathrm{full},\mathrm{ad}\}.
 \label{eq:validated-trace-norm}$$ In particular, $$\left\lVert (B_n^{\star})^2-\mathcal B^2\right\rVert_{\mathfrak S_1}=O(n^{-1}).
 \label{eq:trace-norm-rate}$$ For every fixed $m\ge1$, $$\operatorname{tr}\!\left((B_n^{\star})^{2m}\right)
 \longrightarrow\operatorname{tr}(\mathcal B^{2m}).
 \label{eq:even-trace-convergence}$$ The explicit coefficient error is [\[eq:even-trace-error\]](#eq:even-trace-error){reference-type="eqref" reference="eq:even-trace-error"} with $M=15.418003788081082$ and $\varepsilon_n=\varepsilon_n^\star$.

The result is stronger than convergence of a finite list of computed eigenvalues. Trace-norm convergence controls the complete compact spectrum of the two-step operator at the level needed by Fredholm determinants. It also controls each even trace without a spectral diagonalization and without assuming normality.

At the threshold $n=65536$, the full ledger decomposes as $$\begin{aligned}
 \eta_{K,n}&\le0.005119125317796473,
 \notag\\
 \eta_{+,n}&\le0.026770586570540194,
 \qquad
 \eta_{-,n}\le0.06021710060888367,
 \label{eq:threshold-components}\\
 \sqrt2(\eta_{+,n}+\eta_{-,n})
 &\le0.12301916696860951.
 \notag\end{aligned}$$ Thus $$\varepsilon_{65536}^{\mathrm{full}}
 \le0.1281382922864061,
 \qquad
 \delta_{65536}^{\mathrm{full}}
 \le3.967692773690177.$$ The threshold constants are intentionally conservative: their purpose is to certify the topology and the asymptotic convergence, not to approximate the determinant sharply at the smallest admitted grid.

::: {#tab:certificate}
         $n$   $\varepsilon_n^{\rm full}$   $\varepsilon_n^{\rm ad}$   $\delta_n^{\rm full}$     $\Delta_n(10^{-3})$     $\Delta_n(10^{-2})$
  ---------- ---------------------------- -------------------------- ----------------------- ----------------------- -----------------------
    $2^{16}$        $1.2814\times10^{-1}$      $1.2814\times10^{-1}$                $3.9677$   $1.7419\times10^{-2}$    $1.3027\times10^{1}$
    $2^{20}$        $3.9318\times10^{-3}$      $3.9318\times10^{-3}$   $1.2126\times10^{-1}$   $5.3031\times10^{-4}$   $3.8309\times10^{-1}$
    $2^{24}$        $2.4245\times10^{-4}$      $2.4245\times10^{-4}$   $7.4761\times10^{-3}$   $3.2693\times10^{-5}$   $2.3592\times10^{-2}$
    $2^{30}$        $3.7851\times10^{-6}$      $3.7851\times10^{-6}$   $1.1672\times10^{-4}$   $5.1039\times10^{-7}$   $3.6829\times10^{-4}$

  : Selected outward ledgers. Here $\varepsilon_n$ is the bulk Hilbert--Schmidt error, $\delta_n$ is the bulk-square trace-norm error, and $\Delta_n(R)$ is the full-family determinant upper on $|w|\le R$ from [\[eq:determinant-disk-bound\]](#eq:determinant-disk-bound){reference-type="eqref" reference="eq:determinant-disk-bound"}. Full and adaptive values agree to the displayed precision because the adaptive cutoff is much smaller than the first-order Galerkin term.
:::

The scaled final values are $$2^{30}\varepsilon_{2^{30}}^{\mathrm{full}}
 \le4064.188967889787,
 \qquad
 2^{30}\delta_{2^{30}}^{\mathrm{full}}
 \le125323.3771880477.
 \label{eq:scaled-final}$$ They exhibit the certified first-order regime. The constants are larger at $2^{16}$ because the contour-resolvent transfers have not yet reached their asymptotic values.

# Fredholm determinants and the symmetric regularization identity {#sec:determinants}

Since $\mathcal B^2\in\mathfrak S_1$, define the intrinsic bulk two-step determinant $$\mathcal D_{\mathrm{bulk}}(w)
 =\operatorname{det}(\mathrm I-w\mathcal B^2).
 \label{eq:bulk-square-determinant}$$ It is entire in $w$. In the norm-safe disk $|w|\left\lVert \mathcal B^2\right\rVert<1$, its logarithm has the trace expansion $$\log\mathcal D_{\mathrm{bulk}}(w)
 =-\sum_{m\ge1}\frac{w^m}{m}\operatorname{tr}(\mathcal B^{2m}).
 \label{eq:bulk-square-trace-series}$$ Thus the coefficients are precisely the even intrinsic bulk traces closed in [\[thm:bulk-square\]](#thm:bulk-square){reference-type="ref" reference="thm:bulk-square"}.

[\[thm:determinant-convergence\]]{#thm:determinant-convergence label="thm:determinant-convergence"} For $\star\in\{\mathrm{full},\mathrm{ad}\}$, put $$\mathcal D_{n,\mathrm{bulk}}^\star(w)
 =\operatorname{det}\!\left(\mathrm I-w(B_n^\star)^2\right).
 \label{eq:discrete-square-determinant}$$ Then $$\mathcal D_{n,\mathrm{bulk}}^\star
 \longrightarrow\mathcal D_{\mathrm{bulk}}
 \quad\text{locally uniformly on }\mathbb C.
 \label{eq:local-uniform}$$ For every $R\ge0$, the explicit error is $$\sup_{|w|\le R}
 \left|\mathcal D_{n,\mathrm{bulk}}^\star(w)
       -\mathcal D_{\mathrm{bulk}}(w)\right|
 \le R\delta_n^\star
 e^{1+R(15.418003788081082)^2
      +R(15.418003788081082+\varepsilon_n^\star)^2}.
 \label{eq:validated-determinant-bound}$$

At $n=65536$, the $R=10^{-2}$ upper is $13.0265$, so it is a convergence certificate rather than a useful pointwise enclosure. The same formula falls below $1$ before $n=2^{20}$ and reaches $3.682918268863141\times10^{-4}$ at $2^{30}$. Smaller disks are already effective at the threshold: the $R=10^{-4}$ upper is $1.131494590077742\times10^{-3}$.

## Connection to the second regularized determinant

For $T\in\mathfrak S_2$, the natural one-step determinant is $$\operatorname{det}\nolimits_2(\mathrm I-zT)
 =\operatorname{det}\!\left((\mathrm I-zT)e^{zT}\right)
 =\prod_j(1-z\lambda_j)e^{z\lambda_j}.
 \label{eq:det2-definition}$$ This was the regularization used in the long-cycle analysis [@WangLongCycle2026]. The two-step determinant is its exact symmetric completion.

[\[prop:symmetric-det2\]]{#prop:symmetric-det2 label="prop:symmetric-det2"} For every $T\in\mathfrak S_2(H)$ and every $z\in\mathbb C$, $$\operatorname{det}\nolimits_2(\mathrm I-zT)\operatorname{det}\nolimits_2(\mathrm I+zT)
 =\operatorname{det}(\mathrm I-z^2T^2).
 \label{eq:symmetric-det2}$$ In particular, $$\operatorname{det}\nolimits_2(\mathrm I-z\mathcal B)\operatorname{det}\nolimits_2(\mathrm I+z\mathcal B)
 =\mathcal D_{\mathrm{bulk}}(z^2).
 \label{eq:bulk-symmetric-det2}$$

Both $(\mathrm I-zT)e^{zT}-\mathrm I$ and $(\mathrm I+zT)e^{-zT}-\mathrm I$ are trace class. All factors are functions of $T$ and commute, so $$\bigl((\mathrm I-zT)e^{zT}\bigr)
 \bigl((\mathrm I+zT)e^{-zT}\bigr)
 =\mathrm I-z^2T^2.$$ Multiplicativity of the ordinary Fredholm determinant on $\mathrm I+\mathfrak S_1$ proves the identity.

The identity removes a possible regularization ambiguity. The linear counterterms $e^{\pm zT}$ cancel exactly. Equivalently, the trace series on the left keeps only the even coefficients: $$\begin{aligned}
 \log\operatorname{det}\nolimits_2(\mathrm I-zT)+\log\operatorname{det}\nolimits_2(\mathrm I+zT)
 &=-\sum_{m\ge2}\frac{z^m+(-z)^m}{m}\operatorname{tr}(T^m)
 \notag\\
 &=-\sum_{j\ge1}\frac{z^{2j}}{j}\operatorname{tr}(T^{2j}).
 \label{eq:even-det2-series}\end{aligned}$$ This is exactly [\[eq:bulk-square-trace-series\]](#eq:bulk-square-trace-series){reference-type="eqref" reference="eq:bulk-square-trace-series"} with $w=z^2$.

The zeros of $\mathcal D_{\mathrm{bulk}}(w)$ encode the nonzero eigenvalues of $\mathcal B^2$, with algebraic multiplicity. The squaring map combines the $\lambda$ and $-\lambda$ channels and therefore does not retain their one-step sign. This is appropriate for the physical two-step operator but must not be confused with a self-adjoint spectral realization.

# Stored sparse determinant pilot {#sec:pilot}

The theorem above does not require a numerical determinant evaluation. We nevertheless audit the three stored adaptive matrices to test whether the intrinsic determinant is numerically stable under the two archived dyadic refinements.

Let $P$ be one stored sparse matrix, let $R,L\in\mathbb R^{n\times2}$ be its archived right and left peripheral factors, and let $\Lambda=\operatorname{diag}(\lambda_+,\lambda_-)$. The stored bulk center is $$B=P-R\Lambda L^T.
 \label{eq:stored-bulk}$$ For a real parameter $s$ with $|s|<1$, set $A_s=\mathrm I-sP$. The matrix determinant lemma gives $$\det(\mathrm I-sB)
 =\det(A_s)
 \det\!\left(\mathrm I_2+sL^TA_s^{-1}R\Lambda\right).
 \label{eq:determinant-lemma}$$ Thus the dense rank-two subtraction never needs to be materialized. Two sparse LU factorizations give $$\det(\mathrm I-wB^2)
 =\det(\mathrm I-\sqrt w B)\det(\mathrm I+\sqrt w B).
 \label{eq:pilot-symmetric-product}$$

The archived biorthogonality errors are below $4.30\times10^{-15}$, and the maximum relative left/right eigenvector residual is below $3.52\times10^{-15}$. These figures describe binary64 centers. The preceding papers separately certify that the stored peripheral factors correspond to the true spectral terms, but the LU determinants computed here are not interval-enclosed.

::: {#tab:pilot-values}
     $n$   $\operatorname{tr}B_n$   $\mathcal D_n(10^{-4})$   $\mathcal D_n(10^{-3})$   $\mathcal D_n(10^{-2})$
  ------ ------------------------ ------------------------- ------------------------- -------------------------
    2048       0.3598968178381147         1.000079193893711         1.000792450343546         1.007975861190471
    4096       0.3598916069810533         1.000079192866708         1.000792440045341         1.007975756517583
    8192       0.3598903050128218         1.000079192611279         1.000792437474647         1.007975730366091

  : Floating sparse-LU pilot for the stored fixed-eight-sigma matrices. At these three dimensions the fixed family coincides with the adaptive schedule. Values are diagnostics, not rigorous enclosures.
:::

The consecutive absolute differences at $w=10^{-2}$ are $$1.046728883569159\times10^{-7},
 \qquad
 2.615149163887054\times10^{-8},
 \label{eq:pilot-differences}$$ and their ratio is $0.24984$. Across the five values $w=10^{-4},3\times10^{-4},10^{-3},3\times10^{-3},10^{-2}$, the mean ratio is $0.2493$. This is consistent with a second-order midpoint center, as expected from the smooth Nyström analysis. It does not improve the rigorous $O(n^{-1})$ theorem, whose first-order term comes from comparing the piecewise-constant lift with the entire continuum operator in Hilbert--Schmidt norm.

The finite-dimensional symmetric $\det_2$ identity was also evaluated at every level and every pilot radius. The maximum binary64 discrepancy was $2.220446049250313\times10^{-16}$.

# Certificate architecture and reproducibility {#sec:certificate}

The certificate is a composition of already validated contour and kernel objects with the new trace-ideal ledger. Its main gates are:

1.  the RH-42 Hilbert--Schmidt envelope for $k$ and its derivatives;

2.  the RH-43 continuum parity resolvent and weighted Schur transport;

3.  the RH-44 Perron contour and intrinsic rank-two kernel bound;

4.  continuum-to-Galerkin Hilbert--Schmidt Poincaré control;

5.  midpoint, exact-normalization, and adaptive-cutoff Frobenius control;

6.  rank-at-most-two conversion for each weighted-term difference;

7.  Hilbert--Schmidt-to-trace-norm squaring;

8.  even-trace and determinant continuity bounds.

The displayed ledger contains dimensions $2^{16},\ldots,2^{30}$. These rows are convenient checkpoints, not a restriction to dyadic grids. The analytic defect formulas are valid for every integer $n\ge65536$, and their monotonicity closes the all-grid theorem.

![Trace-ideal completion of the intrinsic bulk. (a) Outward Hilbert--Schmidt errors for the full and adaptive one-step bulk families. (b) The resulting trace-norm errors for their squares. Both carry the first-order cellwise Galerkin rate. (c) Rigorous local-uniform Fredholm determinant bounds on three $w$-disks. (d) Floating consecutive differences of the stored sparse determinants; their approximately quarter scaling is diagnostic and is not used in panels (a)--(c).](<../../../../../zeta_mvp0/papers/RH-45-bulk-two-step-trace-norm-determinant/figures/bulk_two_step_trace_norm_determinant.pdf>){#fig:summary width="\\textwidth"}

The archive hashes every consumed external certificate, local source, result, figure, manuscript, and publication PDF. The complete replay is listed in the repository README. Rebuilding the rigorous trace ledger, tests, figures, and archive takes seconds. Rebuilding the stored 8192 determinant pilot takes approximately four minutes on the reference server because each of the five radii requires two sparse LU factorizations.

# What is closed and what remains {#sec:boundary}

The present result closes a precise functional-analytic gap.

1.  The intrinsic one-step bulk now converges in the natural Hilbert--Schmidt topology for full and adaptive discretizations.

2.  Its square converges in trace norm, with a completely explicit first-order bound.

3.  Every fixed even bulk trace has a rigorous continuum limit.

4.  The intrinsic two-step Fredholm determinant is the local-uniform limit of computable finite determinants.

5.  The determinant is exactly the symmetric product of the two regularized one-step determinants from the long-cycle framework.

Several harder bridges remain open.

1.  The theorem fixes $\sigma=10^{-2}$. Uniform trace-ideal control as $\sigma\downarrow0$ is not proved.

2.  The fixed eight-sigma family is spectrally stable but is not a continuum-convergent family in the norm used here.

3.  No arithmetic formula identifies $\operatorname{tr}(\mathcal B^{2m})$ with a prime or prime-power coefficient.

4.  No $T\log T$ zero-counting law has been derived for $\mathcal D_{\mathrm{bulk}}$ under any scaling.

5.  The nonnormal operator $\mathcal B$ is not a self-adjoint Hilbert--Pólya operator. Squaring does not change that fact.

A natural next step is a two-parameter audit: retain the rigorous trace-ideal topology while allowing the noise width and grid dimension to vary jointly. Such a result would determine whether the intrinsic two-step determinant has a controlled small-noise limit or whether a new renormalization is required. Either outcome is mathematically informative.

The current theorem should therefore be read as infrastructure, not as an arithmetic identification. It constructs a strict intrinsic cycle-trace and spectral-determinant object at fixed noise and proves that the archived finite-dimensional route converges to it in the correct ideal topology.

# Data and code availability {#data-and-code-availability .unnumbered}

All source code, outward certificates, stored binary64 inputs, figures, tests, dependency hashes, archive verification, and the manuscript source are available in the accompanying repository directory <https://github.com/maris205/prime_dynamics_theory/tree/main/papers/RH-45-bulk-two-step-trace-norm-determinant>.
