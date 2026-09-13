---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-26-primal-dual-directional-certificate"
canonical_tex: "zeta_mvp0/papers/RH-26-primal-dual-directional-certificate/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-26-primal-dual-directional-certificate/primal-dual-directional-certificate.pdf"
source_sha256: "4297f1d414449ceb35ccf678d1c5e76e40879bb57acb01cf8742c0b78c668ff4"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Primal--Dual Residual Squaring for Directional Feshbach Certification at a Quadratic Band-Merging Map: Goal-Oriented Error Identities, Enlarged Resolvent Budgets, and an Inverse-Information No-Go Theorem

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-26-primal-dual-directional-certificate>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-26-primal-dual-directional-certificate/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-26-primal-dual-directional-certificate/primal-dual-directional-certificate.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-26-primal-dual-directional-certificate/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-26-primal-dual-directional-certificate/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Directional Feshbach closure replaces a global complement-resolvent norm by the resolvent action on a low-rank primal residual, but a floating directional solve still leaves an error proportional to one residual and an unknown inverse norm. We introduce a goal-oriented primal--dual identity that squares this residual mechanism. Let $A_z=z\mathrm I-B$, let $R$ be a primal block right-hand side, and let $E$ be the packet observation. For arbitrary approximations $\widehat Y$ and $\widehat Z$, define $$r=R-A_z\widehat Y,
   \qquad s=E^*-A_z^*\widehat Z.$$ We prove the exact identity $$-EA_z^{-1}R
   =-E\widehat Y-\widehat Z^*r-s^*A_z^{-1}r.$$ Thus the computable correction is $-E\widehat Y-\widehat Z^*r$, while the only unresolved term contains both the primal and adjoint residuals. If $F_J$ is the base Feshbach matrix and $M\geq\left\lVert A_z^{-1}\right\rVert_2$, the remaining matrix-Rouché contribution is bounded by $$M\,\left\lVert F_J^{-1}s^*\right\rVert_2\,\left\lVert r\right\rVert_2.$$ This gives an explicit admissible resolvent budget $M_*(z)$. We also prove a sharp no-free-lunch statement: unit primal and dual residuals can produce an arbitrarily large bilinear remainder even when $\left\lVert A_z\right\rVert_2\leq1$. Primal--dual residuals greatly relax, but cannot logically eliminate, the need for some inverse information unless one residual vanishes exactly.

  The construction is tested on the seven finite noisy transfer matrices and contours of the quadratic band-merging Feshbach program. The primal approximation is the depth increment from $J$ to $J+16$; independent shifted Arnoldi families for $B^*$, driven by the columns of $E^*$, provide dual approximations at depths $J,J+8,J+16$. Across $10^{-2}\geq\sigma\geq10^{-4}$, dimensions $2048\leq n\leq204800$, and packet ranks $4\leq m\leq9$, every 32-node primal--dual corrected determinant has sampled winding one. The maximum computed Rouché ratio is $4.97\times10^{-11}$. The minimum one-sided resolvent budget over all scales is $4.22\times10^{10}$; after dual weighting the minimum is $3.35\times10^{24}$. The worst seven-scale budget gain is $5.48\times10^{13}$. Deep dual true residuals are at most $2.63\times10^{-14}$, and changing the dual depth across the three prescribed levels changes the minimum budget by at most $2.83\%$.

  These are exact finite-dimensional identities and reproducible floating-point stress tests. The large budgets are not themselves certificates: the residuals are not interval-enclosed, no rigorous upper bound for $\left\lVert A_z^{-1}\right\rVert$ is supplied, and contour arcs remain unvalidated. The result changes the next requirement from a sharp global resolvent estimate to any sufficiently crude validated bound compatible with rigorously inflated primal and dual residuals.
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
  **Primal--Dual Residual Squaring for Directional Feshbach Certification**\
  **at a Quadratic Band-Merging Map:**\
  Goal-Oriented Error Identities, Enlarged Resolvent Budgets,\
  and an Inverse-Information No-Go Theorem
```

## Markdown 正文

**Keywords:** Feshbach map; dual-weighted residual; matrix Rouché theorem; Arnoldi method; a posteriori error; nonnormal resolvent; Gaussian transfer operator; quadratic map.

**MSC 2020:** 37E05; 47A10; 47A55; 47B65; 65F10; 65F15; 65P30.

# Introduction {#sec:introduction}

A posteriori error analysis is most effective when it estimates the quantity of interest rather than the full state error. In finite-element and iterative-solver settings this principle leads naturally to adjoint or dual-weighted residuals [@BeckerRannacher2001; @GilesSuli2002]. The same idea is particularly well matched to a Feshbach reduction: the desired quantity is a small packet matrix, whereas the discarded complement may have hundreds of thousands of degrees of freedom and be strongly nonnormal.

The preceding contour calculation isolated the relevant one-sided quantity [@WangDirectionalRouche2026]. If $X_J$ approximately solves $(z\mathrm I-B)X=C$, then with $$R_J=C-(z\mathrm I-B)X_J,
 \qquad F_J=z\mathrm I-D-EX_J,$$ the exact Feshbach error is $$F-F_J=-E(z\mathrm I-B)^{-1}R_J.
 \label{eq:rh25-directional}$$ Consequently, matrix Rouché theory requires only the resolvent action on the at-most-rank-$m$ residual block. Extending the primal Arnoldi spaces by 16 vectors and directly solving the worst residual direction gave consistent perturbation ratios below $5\times10^{-11}$ on seven finite physical discretizations. This bypassed the computationally expensive search for the worst response over the entire complement.

One logical gap remained. If a computed directional solve $\widehat Y$ has residual $r$, then $$-E(z\mathrm I-B)^{-1}R_J
 =-E\widehat Y-E(z\mathrm I-B)^{-1}r.$$ Bounding the second term by norms reintroduces $\left\lVert(z\mathrm I-B)^{-1}\right\rVert$, albeit multiplied by a much smaller residual. At the finest scales, the selected global smallest-singular-value algorithm was already unattractive [@WangDirectionalRouche2026].

This paper applies a dual residual before taking that final norm. An approximate solution of $$(\overline z\mathrm I-B^*)Z=E^*$$ weights the primal residual directly. The remaining error then contains the product of the primal and dual residuals. This has four consequences.

1.  **Exact goal-oriented identity.** The full packet correction decomposes into a computed primal term, a computed dual-weighted term, and one bilinear remainder.

2.  **An explicit resolvent budget.** The matrix-Rouché margin determines the largest external inverse norm compatible with the computed residual factors. The dual residual enlarges this budget by at least 13 orders of magnitude on the tested contours.

3.  **A precise no-go boundary.** Residual norms alone cannot uniformly bound the bilinear remainder. Some inverse information remains mathematically necessary unless a primal or dual solve is exact.

4.  **A seven-scale matrix-free audit.** Shift-invariant primal and adjoint Arnoldi families evaluate all 32 contour nodes while true residuals are checked by fresh sparse operator calls.

The evidence hierarchy is essential. The primal--dual identity, budget criterion, and no-go theorem are exact finite-dimensional statements. The reported budgets use floating matrices and floating residuals. They measure how much room a later validated calculation would have; they do not constitute that validated calculation. No continuum or small-noise theorem is asserted.

# Packet--complement setting {#sec:setting}

Let $A\in\mathbb C^{n\times n}$ be the Perron/parity-extracted physical two-step matrix at one noise scale. Let $V\in\mathbb C^{n\times m}$ and $W\in\mathbb C^{m\times n}$ be the canonical packet pair with $WV=\mathrm I_m$, and put $$P=VW,\qquad Q=\mathrm I-P.$$ In packet--complement coordinates define $$D=WAV,\qquad C=QAV,\qquad E=WAQ,
 \qquad B=QAQ\big|_{\operatorname{Ran}Q}.
 \label{eq:blocks}$$ For $z\notin\operatorname{spec}B$, write $$A_z=z\mathrm I_{\operatorname{Ran}Q}-B,
 \qquad
 F(z)=z\mathrm I_m-D-EA_z^{-1}C.
 \label{eq:az-f}$$ The oblique Schur factorization and argument principle give $$\begin{aligned}
 \det(z\mathrm I_n-A)&=\det(A_z)\det F(z),
 \label{eq:det-factorization}\\
 \operatorname{wind}_\Gamma\det F&=N_\Gamma(A)-N_\Gamma(B)
 \label{eq:winding-count}\end{aligned}$$ on admissible contours. The blind contour construction, shifted Arnoldi realization, and projected zero-minus-pole audit are developed in @WangContourFeshbach2026; the growing physical one-vector resolvent lower bounds appear in @WangPhysicalFeshbach2026.

At base Arnoldi depth $J$, let $X_J(z)$ be the FOM approximation and $$R_J=C-A_zX_J,
 \qquad F_J=z\mathrm I_m-D-EX_J.
 \label{eq:base-residual}$$ The present goal is to transfer the sampled winding of $F_J$ toward the exact $F$ without first computing a sharp global norm of $A_z^{-1}$.

# Exact primal--dual correction {#sec:identity}

## Goal-oriented residual identity

The algebra is stated for a general primal right-hand side $R\in\mathbb C^{n\times m}$. In the application, $R=R_J$. Let $\widehat Y,\widehat Z\in\mathbb C^{n\times m}$ be arbitrary approximations and define their true residual blocks $$r=R-A_z\widehat Y,
 \qquad
 s=E^*-A_z^*\widehat Z.
 \label{eq:primal-dual-residuals}$$

[\[thm:primal-dual\]]{#thm:primal-dual label="thm:primal-dual"} For every invertible $A_z$, $$-EA_z^{-1}R
 =-E\widehat Y-\widehat Z^*r-s^*A_z^{-1}r.
 \label{eq:primal-dual-identity}$$

From [\[eq:primal-dual-residuals\]](#eq:primal-dual-residuals){reference-type="ref" reference="eq:primal-dual-residuals"}, $$R=A_z\widehat Y+r,
 \qquad
 E=\widehat Z^*A_z+s^*.$$ Therefore $$EA_z^{-1}R
 =E\widehat Y+EA_z^{-1}r
 =E\widehat Y+\widehat Z^*r+s^*A_z^{-1}r.$$ Multiplication by $-1$ proves the claim.

Define the computable correction and exact remainder by $$\begin{aligned}
 \widehat\Delta(z)&=-E\widehat Y-\widehat Z^*r,
 \label{eq:computed-delta}\\
 \mathcal R_{\rm pd}(z)&=-s^*A_z^{-1}r.
 \label{eq:pd-remainder}\end{aligned}$$ The second term in [\[eq:computed-delta\]](#eq:computed-delta){reference-type="ref" reference="eq:computed-delta"} is a standard dual-weighted residual. It is an $m\times m$ matrix even though both approximations live in the ambient space.

[\[cor:exact-side\]]{#cor:exact-side label="cor:exact-side"} If either $r=0$ or $s=0$, then $\mathcal R_{\rm pd}=0$, so $\widehat\Delta=-EA_z^{-1}R$ exactly. In particular, an exact dual solve recovers the packet correction for any primal approximation.

This corollary concerns the small goal matrix, not the full primal state. It explains why adjoint accuracy can be more valuable than another global primal norm estimate.

## A conditional matrix-Rouché certificate

Precondition the computed and remaining corrections by the base packet matrix: $$\begin{aligned}
 \widehat\eta(z)&=\left\lVert F_J(z)^{-1}\widehat\Delta(z)\right\rVert_2,
 \label{eq:eta-hat}\\
 c_{\rm pd}(z)&=
 \left\lVert F_J(z)^{-1}s(z)^*\right\rVert_2\,\left\lVert r(z)\right\rVert_2.
 \label{eq:pd-coefficient}\end{aligned}$$

[\[thm:pd-rouche\]]{#thm:pd-rouche label="thm:pd-rouche"} Suppose $F_J$ and $A_z$ are invertible on a closed contour $\Gamma$. Let $M(z)$ satisfy $M(z)\geq\left\lVert A_z^{-1}\right\rVert_2$. If $$\sup_{z\in\Gamma}
 \left[\widehat\eta(z)+M(z)c_{\rm pd}(z)\right]<1,
 \label{eq:pd-condition}$$ then $$\operatorname{wind}_\Gamma\det F=\operatorname{wind}_\Gamma\det F_J.
 \label{eq:pd-winding-transfer}$$

By [\[eq:pd-remainder\]](#eq:pd-remainder){reference-type="ref" reference="eq:pd-remainder"}, $$\left\lVert F_J^{-1}\mathcal R_{\rm pd}\right\rVert_2
 \leq
 \left\lVert F_J^{-1}s^*\right\rVert_2\left\lVert A_z^{-1}\right\rVert_2\left\lVert r\right\rVert_2
 \leq M c_{\rm pd}.$$ Hence $\left\lVert F_J^{-1}(F-F_J)\right\rVert_2<1$ on $\Gamma$. The homotopy $F_J+t(F-F_J)$ remains invertible there by the Neumann lemma, so its determinant winding is constant [@GohbergSigal1971].

Whenever $\widehat\eta(z)<1$ and $c_{\rm pd}(z)>0$, define the pointwise admissible resolvent budget $$M_*^{\rm pd}(z)=
 \frac{1-\widehat\eta(z)}{c_{\rm pd}(z)}.
 \label{eq:pd-budget}$$ Any rigorous inverse bound strictly below $\inf_{z\in\Gamma}M_*^{\rm pd}(z)$, combined with rigorous residual and packet enclosures, would satisfy [\[eq:pd-condition\]](#eq:pd-condition){reference-type="ref" reference="eq:pd-condition"}.

## One-sided baseline and budget gain

Without the dual term, the computed correction is $-E\widehat Y$, the remainder is $-EA_z^{-1}r$, and a corresponding coefficient is $$c_{\rm p}(z)=\left\lVert F_J(z)^{-1}E\right\rVert_2\,\left\lVert r(z)\right\rVert_2.
 \label{eq:one-coefficient}$$ Writing $\eta_{\rm p}=\left\lVert F_J^{-1}E\widehat Y\right\rVert_2$, its budget is $$M_*^{\rm p}(z)=\frac{1-\eta_{\rm p}(z)}{c_{\rm p}(z)}.
 \label{eq:one-budget}$$ The gain $M_*^{\rm pd}/M_*^{\rm p}$ measures how much the adjoint residual relaxes the still-missing inverse estimate. It is not an estimate of the inverse itself.

If validated residual upper bounds inflate $\left\lVert r\right\rVert$ and $\left\lVert s\right\rVert$ by factors $\alpha$ and $\beta$, respectively, then the primal--dual coefficient grows by at most $\alpha\beta$. This simple product law makes the budget a useful stress margin for a later interval implementation.

# Why inverse information cannot disappear completely {#sec:nogo}

The dual residual can make $c_{\rm pd}$ extremely small, but no theorem can bound [\[eq:pd-remainder\]](#eq:pd-remainder){reference-type="ref" reference="eq:pd-remainder"} from the two residual norms alone.

[\[thm:no-go\]]{#thm:no-go label="thm:no-go"} For every $L>0$ and every dimension $n\geq2$, there exist an invertible matrix $A\in\mathbb C^{n\times n}$ and unit vectors $r,s\in\mathbb C^n$ such that $$\left\lVert A\right\rVert_2=1,
 \qquad |s^*A^{-1}r|>L.
 \label{eq:no-go}$$ Consequently, no finite upper bound for the bilinear remainder can depend only on $\left\lVert A\right\rVert_2$, $\left\lVert r\right\rVert_2$, and $\left\lVert s\right\rVert_2$.

Take $r=s=e_1$ and $$A_\varepsilon=\operatorname{diag}(\varepsilon,1,\ldots,1)$$ with $0<\varepsilon<L^{-1}$. Then $\left\lVert A_\varepsilon\right\rVert_2=1$, while $$s^*A_\varepsilon^{-1}r=\varepsilon^{-1}>L.$$

The theorem is deliberately elementary and sharp. Residual squaring is a conditioning strategy, not magic: it replaces the need for a sharp inverse bound by the need for any bound below a vastly enlarged budget. An exact primal or dual solve is the only residual-only escape, as [\[cor:exact-side\]](#cor:exact-side){reference-type="ref" reference="cor:exact-side"} shows.

# Shift-invariant primal and dual realization {#sec:realization}

## The primal increment

The RH-25 base and deep approximations are $X_J$ and $X_{J+16}$. In [\[thm:primal-dual\]](#thm:primal-dual){reference-type="ref" reference="thm:primal-dual"}, choose $$R=R_J,
 \qquad
 \widehat Y=X_{J+16}-X_J.
 \label{eq:primal-choice}$$ Then, in exact arithmetic, $$r=R_J-A_z(X_{J+16}-X_J)=R_{J+16}.
 \label{eq:deep-residual}$$ Thus the first computed correction is exactly the depth increment $$-E\widehat Y=F_{J+16}-F_J.
 \label{eq:depth-correction}$$ In the implementation both sides are reconstructed independently; their maximum matrix 2-norm defect is reported.

## Adjoint Arnoldi families

The dual source is the fixed block $E^*=[e_1,\ldots,e_m]$. For each column construct an Arnoldi basis for $B^*$, $$B^*U_{i,K}^{\rm d}
 =U_{i,K}^{\rm d}H_{i,K}^{\rm d}
 +h_{i,K+1,K}^{\rm d}u_{i,K+1}^{\rm d}e_K^*.
 \label{eq:dual-arnoldi}$$ For every contour shift, the dual FOM approximation is $$\widehat z_{i,K}(z)=
 U_{i,K}^{\rm d}
 (\overline z\mathrm I_K-H_{i,K}^{\rm d})^{-1}
 \left\lVert e_i\right\rVert_2 e_1.
 \label{eq:dual-fom}$$ Collecting these columns gives $\widehat Z_K(z)$. One basis therefore serves the entire contour; independent pointwise adjoint solves are not required [@Saad1980; @Saad2003].

The dual depths are $K=J,J+8,J+16$. Fresh applications of $B^*$ evaluate $$s_K=E^*-(\overline z\mathrm I-B^*)\widehat Z_K,$$ including floating Arnoldi recurrence defects. The Euclidean adjoint of the ambient $QAQ$ realization is implemented explicitly and checked by an inner-product identity.

# Numerical protocol {#sec:protocol}

The finite matrices, packet pairs, base depths, and circular contours are inherited unchanged from RH-24 and RH-25 [@WangContourFeshbach2026; @WangDirectionalRouche2026]. The noise scales are $$10^{-2},\ 4\times10^{-3},\ 2\times10^{-3},\ 10^{-3},\
 5\times10^{-4},\ 2\times10^{-4},\ 10^{-4},$$ with $n\sigma=20.48$. Packet ranks increase from four to nine, base depths from 36 to 62, and maximum primal and dual depths from 52 to 78.

For each scale the calculation performs the following steps.

1.  Rebuild the physical sparse matrix, packet pair, and primal Arnoldi family through depth $J+16$.

2.  Form the adjoint action matrix-free, build independent dual Arnoldi families from the columns of $E^*$, and retain their ambient bases.

3.  On 32 equally spaced contour nodes, reconstruct $X_J$, $X_{J+16}$, and $\widehat Z_K$ at all three dual depths.

4.  Evaluate true primal and dual residuals by new sparse operator calls, then compute $\widehat\Delta$, $c_{\rm p}$, $c_{\rm pd}$, and both budgets using small dense packet algebra.

5.  Record determinant phases of $F_J+\widehat\Delta$, the RH-25 direct-correction comparison, and the earlier RH-23 physical-eigenmode resolvent lower bound.

The RH-23 lower bound is evaluated at a physical eigenmode, not uniformly on the present contour. Its comparison with $M_*^{\rm pd}$ is only a conditioning scale: a lower bound can never replace the upper bound required by [\[thm:pd-rouche\]](#thm:pd-rouche){reference-type="ref" reference="thm:pd-rouche"}.

All calculations use complex double precision with NumPy and SciPy; figures use Matplotlib [@HarrisEtAl2020; @VirtanenEtAl2020; @Hunter2007]. Seven unit tests cover the exact identity, exact primal and dual edge cases, budget algebra, the matrix-free residual interface, the norm majorant, and the no-go construction.

# Seven-scale results {#sec:results}

## Correction and budget summary

reports the maximum computed correction ratio and the minimum budgets over each 32-node contour at the deepest dual level. The gain column is the minimum pointwise ratio $M_*^{\rm pd}/M_*^{\rm p}$, not the ratio of the two separately minimized columns. The final column divides the primal--dual budget by the RH-23 one-vector lower bound and is contextual only.

The primal--dual budget remains enormous throughout the tested range. Its smallest value is $3.35\times10^{24}$, at the finest scale, and the smallest gain over the one-sided budget is $5.48\times10^{13}$. Even the one-sided deep-residual budget never falls below $4.22\times10^{10}$. These figures do not estimate $\left\lVert A_z^{-1}\right\rVert$; they state how large a later rigorous upper bound could be before this particular sufficient criterion loses its margin.

At $\sigma=2\times10^{-4}$, the maximum primal--dual ratio differs from the RH-25 direct correction by $0.58\%$; at $10^{-4}$, by $0.39\%$. At coarser scales the dual-weighted term acts on floating residuals near the roundoff floor and can exceed the tiny primal depth increment. It remains below $4\times10^{-13}$ there and is not interpreted as physical structure.

![Seven-scale primal--dual audit. Top left: deep primal, primal--dual, and RH-25 direct correction ratios. Top right: one-sided and primal--dual admissible inverse budgets, with the RH-23 one-vector lower bound shown only as a scale comparison. Bottom left: true primal and dual residuals. Bottom right: minimum pointwise budget gain from the adjoint residual.](<../../../../../zeta_mvp0/papers/RH-26-primal-dual-directional-certificate/figures/primal_dual_summary.pdf>){#fig:summary width="\\textwidth"}

## Residuals, depth, and winding

The maximum deep primal true residual relative to $C$ ranges from $4.13\times10^{-15}$ to $2.91\times10^{-13}$. The maximum deep dual true residual relative to $E^*$ ranges from $1.82\times10^{-15}$ to $2.63\times10^{-14}$. The primal correction reconstructed as $-E(X_{J+16}-X_J)$ agrees with $F_{J+16}-F_J$ to a maximum absolute 2-norm defect $3.07\times10^{-15}$.

Increasing the dual depth from $J$ through $J+8$ to $J+16$ changes the minimum budget by at most $2.83\%$ at any scale. The adjoint family has therefore reached its floating residual floor by the base depth on this finite range; it is not the observed depth bottleneck.

Every deepest-dual corrected determinant has sampled winding one. The largest adjacent phase step is $2.998<\pi$, and the minimum sampled singular value of a corrected packet matrix is $2.14\times10^{-3}$. As before, finite phase samples are not a rigorous enclosure of the arcs between nodes.

![Pointwise inverse budgets on three representative contours. The localized minimum follows the same sensitive angular sector identified by the RH-25 directional correction, but primal--dual weighting lifts the budget by roughly 14 orders of magnitude at every node.](<../../../../../zeta_mvp0/papers/RH-26-primal-dual-directional-certificate/figures/primal_dual_contour_budgets.pdf>){#fig:contour-budgets width="\\textwidth"}

## Cost

At $n=2048$, the primal and dual Arnoldi builds take 0.78 and 0.85 seconds. At $n=102400$, they take 145 and 177 seconds; at $n=204800$, 336 and 403 seconds. The adjoint calculation roughly doubles the basis construction cost, but it is shift-invariant and serves all contour nodes. The retained basis memory, rather than a global smallest-singular-value iteration, is the principal computational cost of this audit.

# Status of the certificate {#sec:status}

## What is exact

The following conclusions are theorem-level finite-dimensional statements.

-   The decomposition [\[eq:primal-dual-identity\]](#eq:primal-dual-identity){reference-type="ref" reference="eq:primal-dual-identity"} is exact for any primal and dual approximations with explicitly defined residuals.

-   The sufficient matrix-Rouché condition [\[eq:pd-condition\]](#eq:pd-condition){reference-type="ref" reference="eq:pd-condition"} follows from a norm bound on the single bilinear remainder.

-   The admissible budget [\[eq:pd-budget\]](#eq:pd-budget){reference-type="ref" reference="eq:pd-budget"} is an exact rearrangement of that sufficient condition.

-   If either residual is zero, the goal correction is exact.

-   Without inverse information, the bilinear remainder is unbounded in general by [\[thm:no-go\]](#thm:no-go){reference-type="ref" reference="thm:no-go"}.

## What is floating-point evidence

For the seven specified finite sparse matrices, the data support the following narrower observations.

-   Primal and dual shifted Arnoldi residuals are simultaneously small on the sampled contours.

-   Their product enlarges the admissible inverse budget by at least $5.48\times10^{13}$ relative to the one-sided deep-residual estimate.

-   The computed packet correction remains below $4.98\times10^{-11}$, agrees with the independent RH-25 correction at the informative scales, and preserves sampled winding one.

-   The base dual depth is already sufficient at floating precision on the tested range.

The recorded residuals are ordinary double-precision evaluations. The very large budgets partly reflect residuals near the floating recurrence floor. They must be recomputed using outward-rounded bounds before entering a proof.

## The next rigorous gate

Primal--dual squaring changes the character of the missing estimate. A future validated calculation can proceed as follows.

1.  Enclose the sparse primal and dual residual blocks, including matrix construction, oblique projection, Arnoldi recurrence, and dot-product rounding errors.

2.  Enclose the small matrices $F_J^{-1}\widehat\Delta$ and $F_J^{-1}s^*$ on adaptive contour arcs.

3.  Obtain any rigorous upper bound for $\left\lVert A_z^{-1}\right\rVert$ below the residual-inflated minimum budget. Because the present uninflated minimum is $3.35\times10^{24}$, this bound need not be pseudospectrally sharp.

4.  Apply [\[thm:pd-rouche\]](#thm:pd-rouche){reference-type="ref" reference="thm:pd-rouche"}, then separately address finite-section and small-noise limits.

Possible tools for the third step include a validated preconditioned contraction, block interval solves, or a Grushin inverse with explicit error estimates [@SjoestrandZworski2007; @TrefethenEmbree2005]. The no-go theorem prevents deleting this step altogether; the numerical budgets make it substantially less demanding.

# Conclusion {#sec:conclusion}

The directional Feshbach error has a natural primal--dual structure. A shifted adjoint solve converts the remaining one-sided error into a dual-weighted correction plus a bilinear remainder containing both true residuals. This identity is exact, matrix-free, and tailored to the small packet quantity of interest.

On seven finite physical discretizations, residual squaring raises the minimum admissible complement-resolvent budget from at least $4.22\times10^{10}$ to at least $3.35\times10^{24}$, while preserving the sampled one-root winding and the previously observed directional correction. The improvement is large enough that a future proof need not begin with a sharp global pseudospectral calculation.

There is also a firm boundary. Nonzero primal and dual residuals cannot be controlled with no inverse information at all. The next gate is therefore not gone; it has been widened from a tight global-resolvent problem to a coarse validated inverse bound coupled to rigorous residual and contour enclosures.

# Reproducibility and stored artifacts {#app:reproducibility}

The archived repository directory [@WangPrimalDualCode2026] contains:

-   , implementing the dense reference identity, matrix-free residual interface, norm coefficients, and budget algebra;

-   , implementing the seven-scale primal and adjoint Arnoldi audit with resumable per-scale output;

-   seven unit tests, 672 contour-depth rows, seven summary rows, source hashes, and PDF/PNG figures.

Run the tests with

    PYTHONPATH=src /root/math/.venv/bin/pytest -q

and reproduce the full audit with

    PYTHONPATH=src:experiments OPENBLAS_NUM_THREADS=16 \
      /root/math/.venv/bin/python experiments/run_primal_dual_audit.py

Interrupted runs can preserve completed scales using `–resume`. Figures and metadata can be regenerated from the committed tables with `–reuse`. The JSON metadata records software versions, UTC generation time, and SHA-256 hashes of the algebra and experiment sources.
