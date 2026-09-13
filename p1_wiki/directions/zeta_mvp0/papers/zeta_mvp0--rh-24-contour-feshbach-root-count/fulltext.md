---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-24-contour-feshbach-root-count"
canonical_tex: "zeta_mvp0/papers/RH-24-contour-feshbach-root-count/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-24-contour-feshbach-root-count/contour-feshbach-root-count.pdf"
source_sha256: "636fc2bb1ef2ae0f18450e4f24e8888b5c6ae580a82d85b1c8e20c772b1767ef"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Contour Feshbach Root Counting at a Quadratic Band-Merging Map: Blind Resonance Prediction, Holomorphic Shifted Krylov Reduction, and a Narrow Isolation Corridor

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-24-contour-feshbach-root-count>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-24-contour-feshbach-root-count/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-24-contour-feshbach-root-count/contour-feshbach-root-count.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-24-contour-feshbach-root-count/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-24-contour-feshbach-root-count/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  A packet--complement Feshbach closure can reproduce a physical eigenmode when that eigenmode is already known, but this does not yet constitute a spectral prediction. We close that gap for finite noisy transfer matrices at the first band-merging parameter of $f_u(x)=1-u x^2$. For an oblique packet pair $WV=\mathrm I$, put $P=VW$, $Q=\mathrm I-P$, and let $A$ be the Perron/parity-extracted physical two-step operator. On $\mathbb C^m\oplus\operatorname{Ran}Q$, define $$D=WAV,\qquad C=QAV,\qquad E=WAQ,\qquad
   B=QAQ\big|_{\operatorname{Ran}Q}.$$ Whenever $z\notin\operatorname{spec}B$, the exact Feshbach matrix is $$F(z)=z\mathrm I-D-E(z\mathrm I-B)^{-1}C.$$ We prove the finite-dimensional determinant, compressed-resolvent, and argument-principle identities $$\det(z\mathrm I-A)=\det(z\mathrm I-B)\det F(z),\qquad
   W(z\mathrm I-A)^{-1}V=F(z)^{-1},$$ $$\operatorname{wind}_\Gamma\det F=N_\Gamma(A)-N_\Gamma(B).$$

  To evaluate $F$ on an entire contour without destroying analyticity in $z$, every column of $C$ is reduced by a shift-invariant Arnoldi--FOM space. The resulting rational matrix $F_J(z)$ is the exact Schur complement of an explicit augmented matrix $M_J$ and therefore satisfies $$\det(z\mathrm I-M_J)
   =\prod_{i=1}^m\det(z\mathrm I-H_{i,J})\det F_J(z).$$ We also give an exact Arnoldi residual formula, a floating-point recurrence defect bound, and a conditional matrix-Rouché criterion transferring the projected count to the exact $F$. The missing ingredient for a validated transfer is an upper bound on the external resolvent; sampled depth comparisons are not substituted for that theorem.

  The numerical protocol is target-blind. It uses only the two real peripheral modes and the rightmost lower-half-plane eigenvalue of $D$ to choose concentric discovery contours. Nonreal full-matrix eigenvalues are computed only after the Feshbach root is frozen. Across seven noise scales $10^{-2}\ge\sigma\ge10^{-4}$, dimensions $2048\le n\le204800$, packet ranks $4\le m\le9$, and Arnoldi depths $36\le J\le62$, every selected contour has winding one, no projected pole, one augmented zero, and one captured outer full-matrix eigenvalue. Direct packet errors lie between $4.71\times10^{-2}$ and $2.48\times10^{-1}$; contour-Feshbach prediction errors lie between $1.36\times10^{-15}$ and $3.47\times10^{-14}$. The largest computable Arnoldi residual bound is $1.93\times10^{-11}$, and the largest sampled $J-8$ to $J$ Rouché ratio is $4.59\times10^{-6}$. The pole-free one-root corridors remain open but narrow to widths of order $10^{-2}$. Six packet-window variants preserve winding one, with maximum prediction error $6.01\times10^{-13}$. These are reproducible floating-point results for finite discretizations, not a validated continuum or small-noise theorem.
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
  **Contour Feshbach Root Counting** **at a Quadratic Band-Merging Map:**\
  Blind Resonance Prediction, Holomorphic Shifted Krylov Reduction,\
  and a Narrow Isolation Corridor
```

## Markdown 正文

**Keywords:** Feshbach map; argument principle; Arnoldi method; nonlinear eigenvalue problem; oblique projection; Gaussian transfer operator; nonnormal spectrum; quadratic map.

**MSC 2020:** 37E05; 47A10; 47A55; 47B65; 65F15; 65P30.

# Introduction {#sec:introduction}

Finite-rank reductions of nonnormal transfer operators face a basic distinction. A reduced model can *explain* a known eigenpair, or it can *predict* an eigenvalue without using that eigenpair. The first task is an algebraic closure test; the second requires a spectral parameter, a contour on which the discarded complement is solved, and a stable root count. This paper performs the second task for the physical small-noise operator at a quadratic band-merging map.

The preceding construction began with a parity-extracted bulk scattering model and an exact endpoint pole [@WangBulkScattering2026]. A time-ordered boundary word and Gaussian packet propagation then identified the relevant cycle and its physical realization [@WangTimeOrdered2026; @WangGaussianReturn2026]. Subsequent work tested the branch and complement structure. One-branch closure misses an order-one sibling contribution; an unconstrained time lift produces Floquet copies rather than new physical attenuation [@WangComplement2026]. Two critical branches yield a nearly rank-one bright channel, while peripheral biorthogonalization gives a valid oblique packet projector and exposes branch-history collapse [@WangSectorBranch2026; @WangBiorthogonal2026]. A scalar local dark channel has the wrong sign or insufficient self-energy, ruling out that shortcut [@WangDarkSchur2026].

The full packet complement was therefore retained in @WangPhysicalFeshbach2026. That work corrected the spectral target: if $K_{\mathrm b,\sigma}r_\sigma=\mu_\sigma r_\sigma$, the exact two-step eigenvalue is the complex number $\nu_\sigma=\mu_\sigma^2$, not the positive radius $|\mu_\sigma|^2$. It proved the exact packet and external block equations and found that the packet component of the right eigenvector shrinks while the external resolvent becomes increasingly ill-conditioned. The compressed pole nevertheless stays visible because left weight and resolvent amplification compensate the small right projection. Crucially, that audit inserted the already known physical eigenpair into the block equations. It validated the mechanism but did not independently locate a root.

The present paper makes four advances.

1.  **Exact contour count.** The oblique Feshbach determinant is related to the full and external characteristic polynomials. Its winding equals the number of full eigenvalues minus external eigenvalues inside a contour.

2.  **Holomorphic shifted reduction.** Independent Arnoldi spaces for the columns of $QAV$ produce one rational matrix $F_J(z)$ valid for all shifts. The dependence on $z$ remains holomorphic away from projected poles, which is essential for the argument principle.

3.  **Projected count and conditional transfer.** An explicit augmented matrix makes the projected zero-minus-pole count exact. An Arnoldi residual identity and matrix-Rouché condition isolate precisely what is still required to transfer that count rigorously to the original external block.

4.  **Blind finite-matrix prediction.** The nonreal reference eigensystem is withheld until after the contour and root are frozen. Seven scales, depth variation, node refinement, and packet-window variation test the resulting prediction.

The evidence hierarchy is important. The Schur identities, augmented determinant identity, and conditional error criterion are exact finite-dimensional statements. The winding and root counts for $F_J$ are floating-point evaluations of an explicit rational matrix, cross-checked by ordinary eigenvalue counts of $M_J$. Agreement with the later full-matrix reference is numerical evidence for the physical finite discretization. No interval enclosure of the contour, no validated upper external-resolvent bound, and no continuum or $\sigma\downarrow0$ theorem is claimed.

# Physical operator, packet pair, and blind protocol {#sec:physical}

## Perron/parity-extracted two-step operator

Let $$f_u(x)=1-u x^2$$ at the first algebraic band-merging parameter $u=u_{\mathrm c}$. The discretization used below is the folded Gaussian Markov matrix $K_\sigma^{(n)}$ on positive midpoints, with the dimension rule $n\sigma=20.48$. Its construction and normalization are inherited unchanged from the earlier sparse-operator audit [@WangBulkScattering2026; @WangPhysicalFeshbach2026].

Let $R_\perp,L_\perp\in\mathbb R^{n\times2}$ contain the right and left Perron and parity modes, normalized by $$L_\perp^{\mathsf T}R_\perp=\mathrm I_2,
\qquad
 \Lambda_\perp=\operatorname{diag}(\lambda_{\rm P},\lambda_{\rm par}).$$ The one-step bulk operator and the physical two-step operator are $$K_{\mathrm b,\sigma}
 =K_\sigma^{(n)}-R_\perp\Lambda_\perp L_\perp^{\mathsf T},
 \qquad
 A_\sigma=K_{\mathrm b,\sigma}^2.
 \label{eq:bulk-two-step}$$ Every contour calculation in this paper concerns the complex spectrum of $A_\sigma$. The positive return radius used in earlier cycle diagnostics is not substituted for this complex target.

## Canonical packet and complement

The packet trial matrix $V\in\mathbb R^{n\times m}$ is assembled from propagated critical-branch histories. Regular slices retain their normalized bright sum and the final critical slice retains both disjoint branch labels. The canonical Petrov analysis $W\in\mathbb R^{m\times n}$ removes the two peripheral modes and obeys $$WV=\mathrm I_m.
 \label{eq:biorthogonal-pair}$$ Thus $$P=VW,
 \qquad Q=\mathrm I-P$$ are complementary, generally oblique projectors. We use the direct packet matrix $$D=W A_\sigma V
 \label{eq:direct-matrix}$$ only as a target-free center generator. Among its eigenvalues in the lower half-plane, define $$z_{\rm d}
 =\underset{\lambda\in\operatorname{spec}D,\ \Im\lambda<0}{\operatorname{argmax}}
 \bigl(\Re\lambda,|\lambda|\bigr),
 \label{eq:direct-center-rule}$$ where the second entry breaks ties. No nonreal eigenvalue of $K_\sigma^{(n)}$ appears in this rule.

## What "blind" means {#sec:blind-definition}

The implementation separates construction and reference stages.

1.  A construction eigensolve requests eight largest-modulus left and right modes. Only the two real Perron/parity modes are selected; all nonreal values and vectors are discarded from the returned object.

2.  The packet, $D$, the complement Krylov model, the discovery contour, the winding, and the nonlinear root are computed and frozen.

3.  A separate reference eigensolve then requests 24 outer left and right modes. The unique captured two-step eigenvalue inside the frozen contour is reported as the blind reference.

The construction eigensolver may internally traverse nonreal Krylov directions, as any iterative eigensolver can. Blindness here is an information-flow statement: no nonreal Ritz value or vector is read, stored in the construction object, used to select $z_{\rm d}$, or used to place the contour. The separate reference call occurs after the prediction.

# Exact oblique Feshbach algebra on a contour {#sec:exact-feshbach}

Suppress the scale index and write $A=A_\sigma$. On the complementary decomposition $\mathbb C^n=\operatorname{Ran}P\oplus\operatorname{Ran}Q$, define $$D=WAV,\qquad C=QAV,\qquad E=WAQ,
 \qquad B=QAQ\big|_{\operatorname{Ran}Q}.
 \label{eq:block-definitions}$$ Here $C:\mathbb C^m\to\operatorname{Ran}Q$, $E:\operatorname{Ran}Q\to\mathbb C^m$, and $B:\operatorname{Ran}Q\to\operatorname{Ran}Q$.

[\[thm:exact-feshbach\]]{#thm:exact-feshbach label="thm:exact-feshbach"} For $z\notin\operatorname{spec}B$, set $$F(z)=z\mathrm I_m-D-E(z\mathrm I_{\operatorname{Ran}Q}-B)^{-1}C.
 \label{eq:exact-feshbach}$$ Then $$\begin{aligned}
 \det(z\mathrm I_n-A)
 &=\det(z\mathrm I_{\operatorname{Ran}Q}-B)\det F(z),
 \label{eq:exact-det-factorization}\\
 W(z\mathrm I_n-A)^{-1}V&=F(z)^{-1}
 \label{eq:compressed-resolvent}\end{aligned}$$ whenever the displayed inverses exist.

The map $$S:\mathbb C^m\oplus\operatorname{Ran}Q\longrightarrow\mathbb C^n,
 \qquad S(\alpha,q)=V\alpha+q$$ is an isomorphism with inverse $S^{-1}x=(Wx,Qx)$. In these coordinates, $$S^{-1}AS=
 \begin{pmatrix}
  D&E\\ C&B
 \end{pmatrix}.$$ Taking the Schur complement of $z\mathrm I-B$ proves [\[eq:exact-det-factorization\]](#eq:exact-det-factorization){reference-type="ref" reference="eq:exact-det-factorization"}. Block inversion gives the upper-left block $F(z)^{-1}$, which is exactly $W(z\mathrm I-A)^{-1}V$.

Let $\Omega$ be the interior of a positively oriented simple contour $\Gamma$, and let $N_\Gamma(T)$ denote the algebraic number of eigenvalues of $T$ in $\Omega$.

[\[thm:argument-principle\]]{#thm:argument-principle label="thm:argument-principle"} Assume $\Gamma$ meets neither $\operatorname{spec}A$ nor $\operatorname{spec}B$. Then $$\operatorname{wind}_\Gamma\det F
 =\frac{1}{2\pi i}\int_\Gamma
   \operatorname{tr}\!\left(F(z)^{-1}F'(z)\right)\,dz
 =N_\Gamma(A)-N_\Gamma(B).
 \label{eq:feshbach-count}$$ In particular, if $N_\Gamma(B)=0$ and the winding is one, $\Gamma$ contains exactly one eigenvalue of $A$, counted algebraically.

Apply the scalar argument principle to [\[eq:exact-det-factorization\]](#eq:exact-det-factorization){reference-type="ref" reference="eq:exact-det-factorization"}. Away from zeros and poles, Jacobi's formula gives $$\frac{(\det F)'}{\det F}=\operatorname{tr}(F^{-1}F'),$$ as required [@Ahlfors1979; @HornJohnson2013].

[\[rem:meromorphic\]]{#rem:meromorphic label="rem:meromorphic"} The winding of $\det F$ is generally a zero-minus-pole count. Calling it a full eigenvalue count requires excluding external eigenvalues from the interior, not merely solving the external equation at points on the boundary. This distinction motivates the projected pole audit below.

# A holomorphic shifted Arnoldi Feshbach model {#sec:arnoldi}

Directly solving $(z\mathrm I-B)X=C$ for every contour node and every packet column is expensive. More importantly, an independently restarted least-squares solve at each $z$ need not define one holomorphic matrix-valued function of $z$. The argument principle applies to a function, not to an unrelated collection of pointwise approximations. We therefore use the shift invariance of polynomial Krylov spaces [@Saad1980; @Saad2003].

## Column-wise Arnoldi--FOM reduction

Write $C=[c_1,\ldots,c_m]$. For each column, construct a Euclidean orthonormal Arnoldi basis $$U_{i,J}=[u_{i,1},\ldots,u_{i,J}],
 \qquad c_i=\beta_i u_{i,1},$$ with relation $$B U_{i,J}
 =U_{i,J}H_{i,J}
  +h_{i,J+1,J}u_{i,J+1}e_J^*.
 \label{eq:arnoldi-relation}$$ The packet observation of this basis is $$G_{i,J}=E U_{i,J}\in\mathbb C^{m\times J}.$$ For every shift away from $\operatorname{spec}H_{i,J}$, define $$y_{i,J}(z)=(z\mathrm I_J-H_{i,J})^{-1}\beta_i e_1,
 \qquad
 x_{i,J}(z)=U_{i,J}y_{i,J}(z).
 \label{eq:fom-solution}$$ The projected self-energy and Feshbach matrix are $$\begin{aligned}
 \Sigma_J(z)
 &=\bigl[G_{1,J}y_{1,J}(z),\ldots,G_{m,J}y_{m,J}(z)\bigr],
 \label{eq:projected-self-energy}\\
 F_J(z)&=z\mathrm I_m-D-\Sigma_J(z).
 \label{eq:projected-feshbach}\end{aligned}$$ Sparse applications of $B$ to the $m$ current Arnoldi vectors are batched, but each column is orthogonalized only against its own basis. This avoids the quadratic cross-column orthogonalization cost of one large block basis.

## Exact augmented realization

Let $$\mathcal H_J=\operatorname{diag}(H_{1,J},\ldots,H_{m,J}),
 \qquad
 \mathcal G_J=[G_{1,J}\ \cdots\ G_{m,J}],$$ and let $\mathcal C_J\in\mathbb C^{mJ\times m}$ have $i$th block column $\beta_i e_1$. Define $$M_J=
 \begin{pmatrix}
  D&\mathcal G_J\\
  \mathcal C_J&\mathcal H_J
 \end{pmatrix}.
 \label{eq:augmented-matrix}$$

[\[thm:projected-determinant\]]{#thm:projected-determinant label="thm:projected-determinant"} For $z\notin\bigcup_i\operatorname{spec}H_{i,J}$, $$\det(z\mathrm I_{m+mJ}-M_J)
 =\left[\prod_{i=1}^m\det(z\mathrm I_J-H_{i,J})\right]\det F_J(z).
 \label{eq:projected-det-identity}$$ Consequently, $$\operatorname{wind}_\Gamma\det F_J
 =N_\Gamma(M_J)-\sum_{i=1}^m N_\Gamma(H_{i,J})
 \label{eq:projected-count}$$ for every contour avoiding the projected zeros and poles.

Take the Schur complement of $z\mathrm I_{mJ}-\mathcal H_J$ in $z\mathrm I-M_J$. Its upper-left block is exactly $F_J(z)$. The determinant factorization and argument principle then give the two claims.

This theorem gives two independent finite computations of the projected count: phase winding of the small $m\times m$ determinant and ordinary eigenvalue counts of $M_J$ and the $H_{i,J}$. It also explains why the column-wise realization produces repeated projected pole--zero clusters: each right-hand side carries its own approximation of the external block. Those clusters are numerical realization events, not automatically new physical resonances.

## Derivative, moments, and Newton refinement

Differentiating [\[eq:projected-feshbach\]](#eq:projected-feshbach){reference-type="ref" reference="eq:projected-feshbach"} gives the $i$th column of $F_J'(z)$ as $$F_J'(z)e_i
 =e_i+G_{i,J}(z\mathrm I_J-H_{i,J})^{-2}\beta_i e_1.
 \label{eq:feshbach-derivative}$$ Thus the projected count and first moment are $$\begin{aligned}
 n_J&=\frac{1}{2\pi i}\int_\Gamma
 \operatorname{tr}(F_J^{-1}F_J')\,dz,
 \label{eq:cauchy-count}\\
 s_J&=\frac{1}{2\pi i}\int_\Gamma
 z\,\operatorname{tr}(F_J^{-1}F_J')\,dz.
 \label{eq:cauchy-moment}\end{aligned}$$ If the contour contains one zero and no pole, $s_J/n_J$ is its Cauchy centroid. A simple zero is refined by the log-determinant Newton step $$z_{k+1}=z_k-
 \left[\operatorname{tr}\!\left(F_J(z_k)^{-1}F_J'(z_k)\right)\right]^{-1},
 \label{eq:newton}$$ as in contour methods for nonlinear eigenvalue problems [@Beyn2012].

## Residuals and the exact missing estimate

In exact arithmetic, [\[eq:arnoldi-relation\]](#eq:arnoldi-relation){reference-type="ref" reference="eq:arnoldi-relation"} implies $$\frac{\|c_i-(z\mathrm I-B)x_{i,J}(z)\|}{\|c_i\|}
 =\frac{|h_{i,J+1,J}e_J^*y_{i,J}(z)|}{\beta_i}.
 \label{eq:ideal-residual}$$ At deep convergence this expression can fall below the floating-point recurrence floor. The implementation therefore records every actual Arnoldi relation defect $d_{i,k}$. If $y=(y_1,\ldots,y_J)^\mathsf T$, it reports the computable bound $$\|c_i-(z\mathrm I-B)x_{i,J}\|
 \le |h_{i,J+1,J}y_J|
    +\sum_{k=1}^J |y_k|\,\|d_{i,k}\|.
 \label{eq:floating-residual-bound}$$ This prevents a formal $10^{-40}$ Krylov residual from being presented as physical accuracy when the recurrence itself is accurate only near machine precision.

Let $X_J=[x_{1,J},\ldots,x_{m,J}]$ and $$R_J(z)=C-(z\mathrm I-B)X_J(z).$$

[\[thm:conditional-rouche\]]{#thm:conditional-rouche label="thm:conditional-rouche"} Suppose $\Gamma$ and its interior avoid $\operatorname{spec}B$ and the poles of $F_J$. Then $$F(z)-F_J(z)=-E(z\mathrm I-B)^{-1}R_J(z).
 \label{eq:feshbach-error-identity}$$ If $$\sup_{z\in\Gamma}
 \left\|F_J(z)^{-1}E(z\mathrm I-B)^{-1}R_J(z)\right\|_2<1,
 \label{eq:exact-rouche-condition}$$ then $F$ and $F_J$ have the same number of zeros inside $\Gamma$, counted algebraically.

The residual identity gives $(z\mathrm I-B)^{-1}C-X_J=(z\mathrm I-B)^{-1}R_J$ and hence [\[eq:feshbach-error-identity\]](#eq:feshbach-error-identity){reference-type="ref" reference="eq:feshbach-error-identity"}. The matrix-valued Rouché theorem applied to $F_J+(F-F_J)$ proves the count equality [@GohbergSigal1971].

A sufficient scalar bound is $$\sup_\Gamma\|F_J^{-1}\|\,\|E\|\,
 \sup_\Gamma\|(z\mathrm I-B)^{-1}\|\,
 \sup_\Gamma\|R_J\|<1.
 \label{eq:scalar-rouche-bound}$$ The residual is computed, but no validated upper bound for the middle external resolvent is available. The experiment also reports $$\widehat\eta_{J-8,J}
 =\max_{z_\ell\in\Gamma}
 \left\|F_{J-8}(z_\ell)^{-1}
       \bigl(F_J(z_\ell)-F_{J-8}(z_\ell)\bigr)\right\|_2.
 \label{eq:sampled-rouche}$$ This is a useful sampled depth-stability diagnostic. It is not the supremum in [\[eq:exact-rouche-condition\]](#eq:exact-rouche-condition){reference-type="ref" reference="eq:exact-rouche-condition"}, does not contain the exact external resolvent, and is not advertised as a proof.

# Numerical design {#sec:numerics}

## Seven scales and Krylov dimensions

The baseline uses the canonical packet half-width of six local standard deviations. The sparse dimensions, component periods, packet ranks, and Arnoldi depths are listed in [1](#tab:settings){reference-type="ref" reference="tab:settings"}.

::: {#tab:settings}
            $\sigma$           $n$   component period $k$   packet rank $m$   depth $J$
  ------------------ ------------- ---------------------- ----------------- -----------
           $10^{-2}$     $2{,}048$                      3                 4          36
    $4\times10^{-3}$     $5{,}120$                      4                 5          42
    $2\times10^{-3}$    $10{,}240$                      5                 6          46
           $10^{-3}$    $20{,}480$                      6                 7          50
    $5\times10^{-4}$    $40{,}960$                      6                 7          54
    $2\times10^{-4}$   $102{,}400$                      7                 8          58
           $10^{-4}$   $204{,}800$                      8                 9          62

  : Physical discretizations and column-wise Arnoldi depths.
:::

Each Arnoldi step applies $B$ to all $m$ current vectors in one sparse matrix--matrix operation. Two reorthogonalization passes are used. The maximum observed loss of orthogonality is below $3.10\times10^{-14}$.

## Discovery, isolation, and reference {#sec:discovery-protocol}

For each scale the protocol is as follows.

1.  Compute $z_{\rm d}$ from [\[eq:direct-center-rule\]](#eq:direct-center-rule){reference-type="ref" reference="eq:direct-center-rule"}.

2.  Scan the 45 target-free circles $$\Gamma_\rho:\quad z=z_{\rm d}+\rho|z_{\rm d}|e^{i\theta},
      \qquad \rho=0.04,0.05,\ldots,0.48,$$ using 128 nodes. Retain circles with determinant winding one, projected pole count zero, and maximum phase increment below $0.85\pi$.

3.  Use the best-conditioned retained circle to obtain a Cauchy centroid and Newton root $z_J$.

4.  Compute the spectra of $M_J$ and the $H_{i,J}$. Along the radial family centered at $z_{\rm d}$, let $r_*$ be the target-root radius and $r_{\rm next}$ the next projected zero or pole radius. Place the final contour at $$r_\Gamma=\frac{r_*+r_{\rm next}}{2}.
      \label{eq:mid-corridor}$$ This maximizes radial clearance inside that one-root corridor.

5.  Recompute winding, Cauchy moments, residuals, and Newton refinement using 512 nodes. Only then run the separate 24-mode reference eigensolve.

The contour placement uses projected zeros and poles, which are part of the constructed rational model; it never uses the withheld full-matrix target. Every next event in the seven-scale baseline is a nearly coincident projected pole--zero cluster. We use the cluster as a conservative contour barrier and do not interpret it as a physical resonance.

## Cross-checks

Five checks are recorded.

1.  The phase winding of $\det F_J$ is compared with the augmented count $N_\Gamma(M_J)-\sum_iN_\Gamma(H_{i,J})$.

2.  Arnoldi depths $J-16$, $J-8$, and $J$ are compared on the same final contour.

3.  Contour node counts $64,96,128,192,256,384,512$ test phase and Cauchy quadrature stability.

4.  The 24 captured outer one-step eigenvalues are squared only after the prediction. At every scale exactly one lies in the frozen contour. The contour's radial floor exceeds the smallest captured two-step modulus, so the outer-spectrum comparison extends well below the contour, although it remains an ARPACK computation rather than an interval proof.

5.  Packet half-widths $5,6,7$ are tested at $\sigma=10^{-3}$ and $10^{-4}$.

All calculations use NumPy and SciPy; figures use Matplotlib [@HarrisEtAl2020; @VirtanenEtAl2020; @Hunter2007]. Source, tests, CSV data, small serialized rational models, and figures are archived with the paper [@WangContourFeshbachCode2026].

# Seven-scale root-count results {#sec:results}

## The complement changes approximation into prediction

The central result is summarized in [\[tab:main-results\]](#tab:main-results){reference-type="ref" reference="tab:main-results"}. All seven selected windings equal one. All selected projected pole counts are zero, all augmented counts are one, and exactly one captured outer full-matrix eigenvalue lies in each frozen contour. Twelve-step factorization spot checks have maximum relative residual $1.59\times10^{-14}$, and the closest maximum-depth augmented eigenvalue differs from the Newton root by at most $7.94\times10^{-15}$.

The direct packet matrix is not already the answer: its error remains between $0.0471$ and $0.248$. The full complement self-energy moves the root to the later reference at floating-point accuracy. The improvement factor is at least $1.50\times10^{12}$ on the computed range. This does not mean twelve digits have been proved for an infinite-dimensional operator; it means the converged rational Feshbach model reproduces the selected finite sparse-matrix eigenvalue to the stated floating-point error.

![Baseline root prediction and contour diagnostics. Top left: the direct packet centers miss the reference track, while the contour-Feshbach roots lie on it. Top right: direct and Feshbach errors. Bottom left: normalized one-root corridors, with the final contour at each midpoint. Bottom right: floating Arnoldi residual bounds and sampled depth-change Rouché ratios.](<../../../../../zeta_mvp0/papers/RH-24-contour-feshbach-root-count/figures/contour_feshbach_summary.pdf>){#fig:summary width="\\textwidth"}

## A renormalized contour, not a fixed circle

The target-root radius relative to $|z_{\rm d}|$ changes from $0.3884$ at $\sigma=10^{-2}$ to $0.0834$ at $10^{-4}$. The selected contour factor therefore changes from $0.4110$ to $0.0915$. A fixed relative circle would either miss the target at coarse noise or cross projected pole--zero clusters at fine noise. The computed route is explicitly nonuniform: the contour must be centered and rescaled at each noise level.

The absolute corridor widths lie between $0.0101$ and $0.0288$; the relative widths lie between $0.0161$ and $0.0454$. They are not monotone, so no power-law extrapolation is fitted. The important finite-range fact is that all seven corridors remain open, while the smallest one is narrow enough that coarse contour placement would be unsafe.

![Representative optimized circles. The center is selected from the direct packet matrix; the contour-Feshbach root is computed before the full-matrix reference is revealed. The target and reference markers overlap at plotting resolution.](<../../../../../zeta_mvp0/papers/RH-24-contour-feshbach-root-count/figures/selected_one_root_contours.pdf>){#fig:selected-contours width="\\textwidth"}

## Depth and contour-node convergence

At depth $J-8$, the root changes from its depth-$J$ value by at most $5.18\times10^{-9}$; at depth $J$ the residual bound is at most $1.93\times10^{-11}$. The two quantities need not have the same scale in a nonnormal problem. The sampled matrix-Rouché ratio between $J-8$ and $J$, evaluated on 128 contour nodes, is below one at all scales and at most $4.59\times10^{-6}$. This strongly supports projected depth stability but remains subject to the qualification after [\[eq:sampled-rouche\]](#eq:sampled-rouche){reference-type="ref" reference="eq:sampled-rouche"}.

![Convergence with the number of Arnoldi vectors per right-hand side. At the smallest scales, shallow spaces visibly miss the converged root, but the prescribed maximum depths reach the floating recurrence floor.](<../../../../../zeta_mvp0/papers/RH-24-contour-feshbach-root-count/figures/arnoldi_depth_convergence.pdf>){#fig:depth width="\\textwidth"}

All node counts from 64 through 512 return integer winding one on every optimized contour. At 512 nodes the maximum determinant phase increment is $0.273<\pi$, the largest Cauchy count error is $1.01\times10^{-12}$, and the largest Cauchy-centroid error against the Newton root is $4.27\times10^{-14}$.

![Contour quadrature refinement. The Cauchy count and first-moment centroid converge rapidly, while adjacent determinant phases remain safely below the phase-aliasing threshold $\pi$.](<../../../../../zeta_mvp0/papers/RH-24-contour-feshbach-root-count/figures/contour_node_stability.pdf>){#fig:nodes width="\\textwidth"}

# Packet-window robustness {#sec:window}

The packet half-width is a modeling choice, so reproducing one root only at the baseline value six would be insufficient. We rebuild the complete Feshbach model at widths five and seven for $\sigma=10^{-3}$ and $10^{-4}$. The direct center, complement, Arnoldi bases, projected poles, discovery scan, and optimized contour all change with the window. The frozen full-matrix reference is used only after each root is selected.

The smallest-window, smallest-noise case is the least accurate, as its residual bound and root error both increase. They remain small compared with the direct error, and the pole-free corridor stays open. Hence the single-root result is stable under this finite packet-window variation, not exactly invariant under arbitrary packet choices.

![Packet-window robustness at two representative scales. The direct matrix and selected contour move with the packet, but the predicted physical root remains stable.](<../../../../../zeta_mvp0/papers/RH-24-contour-feshbach-root-count/figures/packet_window_root_stability.pdf>){#fig:window width="\\textwidth"}

# What is established and what remains open {#sec:limits}

The computation changes the status of the packet-complement route, but only within a clearly delimited hierarchy.

## Exact finite-dimensional conclusions

The following statements require no numerical hypothesis beyond the stated invertibility conditions.

-   The oblique packet decomposition gives the exact determinant and compressed-resolvent identities in [\[thm:exact-feshbach\]](#thm:exact-feshbach){reference-type="ref" reference="thm:exact-feshbach"}.

-   The Feshbach winding is the full-minus-external eigenvalue count in [\[thm:argument-principle\]](#thm:argument-principle){reference-type="ref" reference="thm:argument-principle"}.

-   The shifted Arnoldi model is one rational, meromorphic matrix function, not unrelated pointwise fits.

-   Its determinant is exactly the Schur complement of $M_J$, giving the zero-minus-pole identity in [\[thm:projected-determinant\]](#thm:projected-determinant){reference-type="ref" reference="thm:projected-determinant"}.

-   The exact-model error obeys [\[eq:feshbach-error-identity\]](#eq:feshbach-error-identity){reference-type="ref" reference="eq:feshbach-error-identity"}, and [\[eq:exact-rouche-condition\]](#eq:exact-rouche-condition){reference-type="ref" reference="eq:exact-rouche-condition"} is sufficient to transfer the count.

## Finite floating-point evidence

For the seven specified sparse matrices and six window variants, the recorded data support all of the following.

-   A target-free packet center leads to a pole-free contour of projected winding one.

-   Phase winding and augmented eigenvalue counting agree.

-   The projected root stabilizes with Arnoldi depth and contour nodes.

-   The prediction, frozen before the reference solve, matches the unique captured full-matrix eigenvalue in the contour.

-   The required circle is nonuniform in $\sigma$ but an isolation corridor remains open throughout the computed range.

These are stronger than inserting a known eigenpair into an exact block equation: the eigenvalue is now independently reconstructed from the packet, complement action, and contour. They are weaker than a validated spectral theorem because every phase, residual, and reference eigenvalue is still floating point.

## The next rigorous obstruction

The principal missing estimate is not another root finder. It is a uniform or scale-renormalized upper bound for $$\sup_{z\in\Gamma_\sigma}
 \|(z\mathrm I-B_\sigma)^{-1}\|.$$ RH-23 gave growing lower bounds, so a naive uniform-small-complement argument is unavailable. A useful upper bound must respect nonnormality and the shrinking one-root corridor. Possible routes include validated pseudospectral enclosures, interval block solves on contour arcs, or a Grushin formulation with explicit inverse estimates [@TrefethenEmbree2005; @SjoestrandZworski2007]. Without such a bound, small residuals and depth agreement cannot close [\[eq:scalar-rouche-bound\]](#eq:scalar-rouche-bound){reference-type="ref" reference="eq:scalar-rouche-bound"} rigorously.

Three further issues remain.

1.  The independent column realizations duplicate external Ritz poles. A common block or rational Krylov realization could separate genuine external spectral events from near-cancelling realization clusters.

2.  The finite-section rule $n\sigma=20.48$ must be embedded in a discretization-convergence argument, followed by a controlled $\sigma\downarrow0$ limit. The present seven points do not establish either limit.

3.  The contour follows one selected outer resonance. Extending the construction to a multi-root region requires resolving adjacent physical roots and external poles without losing phase or conditioning control.

# Conclusion {#sec:conclusion}

The packet-complement construction has advanced from a closure identity for an already known eigenmode to an independent finite-matrix spectral prediction. Exact Feshbach algebra turns the desired eigenvalue count into a determinant winding. Shift-invariant Arnoldi reduction preserves the analytic spectral parameter, and an augmented realization makes every projected zero-minus-pole count independently checkable. On seven physical discretizations, the resulting contour has one root and no projected pole, and its root agrees with a later full-matrix reference to between $10^{-15}$ and $10^{-14}$ in the baseline. The result survives packet-window variation, Arnoldi-depth variation, and contour refinement.

The positive conclusion is therefore specific: a renormalized nonuniform Feshbach route is numerically viable and can predict the selected physical resonance. The equally important limitation is specific: a validated upper bound on the exact external resolvent is still absent. That bound, rather than further pointwise agreement, is the next mathematical gate.

# Reproducibility and stored artifacts {#app:reproducibility}

The repository directory contains:

-   the generic package `src/contour_feshbach`, implementing column-wise Arnoldi models, projected determinants, Cauchy counts, Newton refinement, and sampled Rouché comparisons;

-   six unit tests for Arnoldi residuals, analytic derivatives, augmented determinant factorization, zero-minus-pole winding, Newton refinement, and sampled matrix-Rouché diagnostics;

-   `experiments/run_contour_feshbach_audit.py`, which performs the blind seven-scale calculation;

-   `experiments/run_packet_window_audit.py`, which performs the two-scale window variation;

-   committed CSV, JSON, small serialized rational models, and all plotted figures.

The baseline is reproduced with

    PYTHONPATH=src OPENBLAS_NUM_THREADS=16 /root/math/.venv/bin/python \
      experiments/run_contour_feshbach_audit.py

and the window audit with

    PYTHONPATH=src:experiments OPENBLAS_NUM_THREADS=16 \
      /root/math/.venv/bin/python experiments/run_packet_window_audit.py

Figures can be regenerated from committed tabular data using `–reuse`. SHA-256 hashes of the experiment and algebra sources are recorded in the summary JSON files. The seven baseline rational models occupy less than one megabyte in compressed form, so contour and depth checks can be repeated without rebuilding the large sparse operators.
