---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-25-directional-rouche-closure"
canonical_tex: "zeta_mvp0/papers/RH-25-directional-rouche-closure/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-25-directional-rouche-closure/directional-rouche-closure.pdf"
source_sha256: "ee6f308b88c89687755e1f608395781ab411ead33e778be3fc431c36e31fc35e"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Directional Rouché Closure Beyond a Global Resolvent Barrier at a Quadratic Band-Merging Map: Exact Residual Identities, Low-Rank Corrections, and a Small-Noise Stress Test

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-25-directional-rouche-closure>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-25-directional-rouche-closure/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-25-directional-rouche-closure/directional-rouche-closure.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-25-directional-rouche-closure/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-25-directional-rouche-closure/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  A contour Feshbach model for a finite noisy transfer matrix can predict a resonance with high floating-point accuracy while its transfer to the exact packet--complement decomposition remains conditional on an external resolvent bound. We show that the global norm $\sup_{z\in\Gamma}\left\lVert(z\mathrm I-B)^{-1}\right\rVert$ is sufficient but is not the quantity actually required by matrix Rouché theory. If $X_J(z)$ approximately solves $(z\mathrm I-B)X=C$, define $$R_J=C-(z\mathrm I-B)X_J,
   \qquad F_J=z\mathrm I-D-EX_J.$$ We prove the exact directional identity $$F-F_J=-E(z\mathrm I-B)^{-1}R_J$$ and the consequent sufficient condition $$\sup_{z\in\Gamma}
   \left\lVert F_J(z)^{-1}E(z\mathrm I-B)^{-1}R_J(z)\right\rVert_2<1.$$ Thus only the resolvent action on the low-rank residual block is needed. We also prove an a posteriori decomposition for an inexact residual solve, a conditional geometric depth-tail bound, and a singular-value Lipschitz extension from contour nodes to circular arcs.

  The identities are tested for the Perron/parity-extracted physical two-step matrices of the quadratic band-merging map. Across seven noise scales $10^{-2}\geq\sigma\geq10^{-4}$, dimensions $2048\leq n\leq204800$, and packet ranks $4\leq m\leq9$, the prescribed Arnoldi depth $J$ is extended to $J+8$ and $J+16$. All three projected determinants have sampled winding one. The maximum directional change between depths $J$ and $J+16$ is $9.14\times10^{-12}$ at $\sigma=2\times10^{-4}$ and $4.96\times10^{-11}$ at $\sigma=10^{-4}$. At the worst contour node, direct GMRES correction of the original external residual gives $9.07\times10^{-12}$ and $4.95\times10^{-11}$, respectively, and reduces the ambient relative residual to at most $1.66\times10^{-14}$. All attempted correction solves converge; coarser scales are limited by floating-point resolution rather than an observed geometric tail.

  As a complementary stress test, at $\sigma=10^{-2}$ a 32-node global singular-value computation of the ambient shifted complement yields a minimum candidate $s_{\min}(z\mathrm I-QAQ)=3.05\times10^{-3}$, a maximum candidate resolvent norm $327.8$, and a nodal scalar Rouché majorant $8.63\times10^{-11}$. The same grid gives no positive full-circle Lipschitz lower bound. At $\sigma=10^{-3}$, four cardinal global singular-value probes each exhaust a 20-second wall-clock budget, whereas the required directional correction remains inexpensive. These results identify a viable directional route and a concrete global-algorithm barrier. They are reproducible floating-point evidence for finite sparse matrices, not a computer-assisted contour proof, a continuum theorem, or a small-noise limit.
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
  **Directional Rouché Closure Beyond a Global Resolvent Barrier**\
  **at a Quadratic Band-Merging Map:**\
  Exact Residual Identities, Low-Rank Corrections, and a Small-Noise Stress Test
```

## Markdown 正文

**Keywords:** Feshbach map; matrix Rouché theorem; Arnoldi method; GMRES; nonnormal resolvent; low-rank residual; Gaussian transfer operator; quadratic map.

**MSC 2020:** 37E05; 47A10; 47A55; 47B65; 65F10; 65F15; 65P30.

# Introduction {#sec:introduction}

For a nonnormal operator, a small residual does not by itself imply a small spectral error. The missing multiplier is a resolvent, and its full operator norm can be much larger than the response in the few directions actually excited by the approximation. This distinction is especially important in Feshbach or Schur reductions: the discarded complement may be large and poorly conditioned, while the packet-to-complement forcing has small rank.

The preceding contour construction at the first quadratic band-merging parameter made this issue explicit [@WangContourFeshbach2026]. For a finite noisy transfer matrix, a target-blind packet--complement model produced a holomorphic shifted Arnoldi Feshbach matrix $F_J(z)$. On seven scale-dependent contours, its determinant winding, augmented zero count, and later full-matrix reference all selected the same simple resonance. The predicted roots agreed with the finite sparse-matrix references to between $10^{-15}$ and $10^{-14}$. The exact transfer of this projected count nevertheless remained open because the standard estimate used $$\left\lVert F_J^{-1}\right\rVert_2\,\left\lVert E\right\rVert_2\,
 \left\lVert(z\mathrm I-B)^{-1}\right\rVert_2\,\left\lVert R_J\right\rVert_2.$$ A validated upper bound for the global external resolvent was unavailable. Earlier packet-complement calculations had already found growing conditioning as the noise decreased [@WangPhysicalFeshbach2026].

The present paper asks whether that global norm is essential. Algebraically the answer is no. The Feshbach error contains the resolvent only through its action on the residual block $R_J$, whose rank is at most the packet rank. A matrix Rouché condition can therefore be evaluated by solving exactly those residual directions. This does not automatically create a rigorous certificate: a floating-point directional solve still requires a validated error enclosure, and finitely many contour nodes still require arc control. It does, however, replace one worst-direction problem by the specific low-rank problem dictated by the Schur algebra.

The contributions are as follows.

1.  **Exact directional identity.** We derive $F-F_J=-E(z\mathrm I-B)^{-1}R_J$ with a fixed sign convention and prove the corresponding matrix Rouché homotopy criterion.

2.  **A posteriori and depth-tail decompositions.** An inexact residual solve is separated into a computed low-rank correction and a remaining directional error. Consecutive Arnoldi-depth increments give a conditional geometric tail majorant, with the condition stated rather than inferred from two observations.

3.  **Seven-scale directional audit.** Retained ambient Arnoldi bases permit true residual reconstruction at depths $J$, $J+8$, and $J+16$. A direct correction at the worst node independently tests the depth extension.

4.  **Global-route stress test.** Floating smallest-singular-value probes quantify when the scalar majorant is numerically favorable, why a 32-node grid is not a continuous certificate, and how the normal-equation route loses scalability at the next noise scale.

Three evidence levels are kept separate throughout. The residual, homotopy, geometric-majorant, and Lipschitz statements are exact finite-dimensional results under their stated hypotheses. The reported windings, singular values, and GMRES corrections are floating-point results for explicit finite sparse matrices. A rigorous contour transfer would add validated arithmetic, continuous arc enclosures, and a certified tail or directional-solve error. No such completed computer-assisted proof is claimed here.

# Packet--complement setting {#sec:setting}

## Physical finite matrix and oblique packet pair

Let $K_\sigma^{(n)}$ be the folded Gaussian Markov discretization of $f_u(x)=1-ux^2$ at the first band-merging parameter. The dimension rule is $n\sigma=20.48$. After removing the real Perron and parity modes, let $A=A_\sigma$ denote the resulting physical two-step matrix. Its sparse construction is inherited unchanged from the earlier bulk and Feshbach audits [@WangBulkScattering2026; @WangPhysicalFeshbach2026].

Let $V\in\mathbb C^{n\times m}$ contain the propagated critical-branch packet histories and let $W\in\mathbb C^{m\times n}$ be the canonical Petrov analysis, normalized by $$WV=\mathrm I_m.
 \label{eq:wv}$$ Then $$P=VW,\qquad Q=\mathrm I-P$$ are complementary, generally oblique projectors. In packet and complement coordinates define $$D=WAV,\qquad C=QAV,\qquad E=WAQ,
 \qquad B=QAQ\big|_{\operatorname{Ran}Q}.
 \label{eq:blocks}$$ Here $D\in\mathbb C^{m\times m}$, $C:\mathbb C^m\to\operatorname{Ran}Q$, $E:\operatorname{Ran}Q\to\mathbb C^m$, and $B:\operatorname{Ran}Q\to\operatorname{Ran}Q$.

For $z\notin\operatorname{spec}B$, the exact Feshbach matrix is $$F(z)=z\mathrm I_m-D-E(z\mathrm I_{\operatorname{Ran}Q}-B)^{-1}C.
 \label{eq:exact-f}$$ The exact determinant and compressed-resolvent identities are $$\det(z\mathrm I_n-A)=\det(z\mathrm I_{\operatorname{Ran}Q}-B)\det F(z),
 \qquad W(z\mathrm I_n-A)^{-1}V=F(z)^{-1}.
 \label{eq:feshbach-identities}$$ Consequently, on a contour avoiding both spectra, $$\operatorname{wind}_\Gamma\det F=N_\Gamma(A)-N_\Gamma(B).
 \label{eq:exact-count}$$ These standard Schur identities are recalled to fix notation; detailed proofs and the target-blind contour protocol appear in @WangContourFeshbach2026; see also @Zhang2005.

## Shifted Arnoldi approximation

The columns of $C$ are reduced in independent, shift-invariant Arnoldi spaces. At depth $J$, the resulting full-orthogonalization approximation to $$(z\mathrm I-B)X(z)=C$$ is denoted by $X_J(z)$. It is reconstructed from retained ambient bases in the present audit. The projected Feshbach matrix is $$F_J(z)=z\mathrm I_m-D-EX_J(z).
 \label{eq:fj}$$ The column-wise Arnoldi realization makes $F_J$ one rational matrix-valued function of $z$, rather than a collection of unrelated pointwise solves [@Saad1980; @Saad2003]. It is the exact Schur complement of an explicit augmented matrix, so its zero-minus-pole count can be checked independently. This paper does not change that model; it examines the transfer from $F_J$ to $F$.

All ambient computations use $QAQ$ on $\mathbb C^n$. Because $C$ and every Arnoldi residual lie in $\operatorname{Ran}Q=\ker W$, solving the ambient shifted system at $z\ne0$ is equivalent to solving its restriction to $\operatorname{Ran}Q$.

# Exact directional Rouché closure {#sec:directional-theory}

## Residual identity

Fix the residual convention $$R_J(z)=C-(z\mathrm I-B)X_J(z).
 \label{eq:residual}$$ The sign matters because the Feshbach map subtracts the external self-energy.

[\[thm:directional-identity\]]{#thm:directional-identity label="thm:directional-identity"} For every $z\notin\operatorname{spec}B$, $$\begin{aligned}
 X(z)&=X_J(z)+(z\mathrm I-B)^{-1}R_J(z),
 \label{eq:x-correction}\\
 F(z)-F_J(z)&=-E(z\mathrm I-B)^{-1}R_J(z).
 \label{eq:f-correction}\end{aligned}$$ In particular, the exact Feshbach error depends only on the action of the external resolvent on the at-most-rank-$m$ residual block.

By [\[eq:residual\]](#eq:residual){reference-type="ref" reference="eq:residual"}, $$(z\mathrm I-B)\left[X_J+(z\mathrm I-B)^{-1}R_J\right]
 =(z\mathrm I-B)X_J+R_J=C.$$ This proves [\[eq:x-correction\]](#eq:x-correction){reference-type="ref" reference="eq:x-correction"}. Substitution into [\[eq:exact-f,eq:fj\]](#eq:exact-f,eq:fj){reference-type="ref" reference="eq:exact-f,eq:fj"} proves [\[eq:f-correction\]](#eq:f-correction){reference-type="ref" reference="eq:f-correction"}.

Define the directional Rouché ratio $$\eta_J(z)=
 \left\lVert F_J(z)^{-1}E(z\mathrm I-B)^{-1}R_J(z)\right\rVert_2.
 \label{eq:eta}$$

[\[thm:directional-rouche\]]{#thm:directional-rouche label="thm:directional-rouche"} Let $\Gamma$ be a closed contour on which $F_J$ is invertible and $z\notin\operatorname{spec}B$. If $$\sup_{z\in\Gamma}\eta_J(z)<1,
 \label{eq:rouche-condition}$$ then $$\operatorname{wind}_\Gamma\det F=\operatorname{wind}_\Gamma\det F_J.
 \label{eq:winding-transfer}$$

Let $\Delta F=F-F_J$ and $F_t=F_J+t\Delta F$ for $0\leq t\leq1$. On $\Gamma$, $$F_t=F_J\left(\mathrm I+tF_J^{-1}\Delta F\right).$$ By [\[eq:f-correction,eq:rouche-condition\]](#eq:f-correction,eq:rouche-condition){reference-type="ref" reference="eq:f-correction,eq:rouche-condition"}, the second factor is invertible by the Neumann lemma. Thus $\det F_t$ never vanishes on the contour. Homotopy invariance of the scalar winding gives [\[eq:winding-transfer\]](#eq:winding-transfer){reference-type="ref" reference="eq:winding-transfer"}. This is the finite-matrix form of the operator Rouché principle [@GohbergSigal1971].

[\[rem:not-global\]]{#rem:not-global label="rem:not-global"} Condition [\[eq:rouche-condition\]](#eq:rouche-condition){reference-type="ref" reference="eq:rouche-condition"} is uniform in the contour parameter, but it is directional in the external space. It does not ask for the response to arbitrary unit vectors in $\operatorname{Ran}Q$; it asks for the response to the columns of $R_J(z)$, followed by the observation $E$ and the small packet inverse $F_J(z)^{-1}$.

## An inexact directional solve

Suppose $\widehat Y(z)$ approximates the solution of $$(z\mathrm I-B)Y=R_J
 \label{eq:residual-system}$$ and define its residual $$S(z)=R_J(z)-(z\mathrm I-B)\widehat Y(z).
 \label{eq:second-residual}$$

[\[prop:two-level\]]{#prop:two-level label="prop:two-level"} For $z\notin\operatorname{spec}B$, $$F-F_J=-E\widehat Y-E(z\mathrm I-B)^{-1}S.
 \label{eq:two-level}$$ Consequently, $$\begin{aligned}
 \eta_J(z)
 &\leq \left\lVert F_J^{-1}E\widehat Y\right\rVert_2
 +\left\lVert F_J^{-1}E\right\rVert_2\,
   \left\lVert(z\mathrm I-B)^{-1}S\right\rVert_2,
 \label{eq:directional-aposteriori}\\
 &\leq \left\lVert F_J^{-1}E\widehat Y\right\rVert_2
 +\left\lVert F_J^{-1}E\right\rVert_2\,
   \left\lVert(z\mathrm I-B)^{-1}\right\rVert_2\,\left\lVert S\right\rVert_2.
 \label{eq:global-remainder}\end{aligned}$$

Apply [\[thm:directional-identity\]](#thm:directional-identity){reference-type="ref" reference="thm:directional-identity"} to $Y=\widehat Y+(z\mathrm I-B)^{-1}S$, then use the triangle and submultiplicative inequalities.

The first line of [\[eq:directional-aposteriori\]](#eq:directional-aposteriori){reference-type="ref" reference="eq:directional-aposteriori"} is the desired route: a certified error enclosure for the particular solve $Y$ suffices. The second line falls back to a global resolvent bound, but only for the remaining residual $S$, which can be many orders of magnitude smaller than $R_J$. Floating GMRES convergence supplies neither enclosure by itself; it is used below as numerical evidence, not as a proof.

## The conservative scalar majorant

For comparison, submultiplicativity applied directly to [\[eq:f-correction\]](#eq:f-correction){reference-type="ref" reference="eq:f-correction"} gives $$\eta_J(z)\leq
 \left\lVert F_J(z)^{-1}\right\rVert_2\,
 \left\lVert E\right\rVert_2\,
 \left\lVert(z\mathrm I-B)^{-1}\right\rVert_2\,
 \left\lVert R_J(z)\right\rVert_2.
 \label{eq:scalar-majorant}$$ This bound is useful when all four factors can be enclosed, but it discards the alignment among $R_J$, the external resolvent, $E$, and the packet inverse. It is therefore a sufficient fallback, not the defining quantity of the transfer problem.

# Depth extension and a conditional tail {#sec:depth-theory}

Let $J_0<J_1<J_2<\cdots$ be nested Arnoldi depths and suppose the rational matrices $F_{J_k}$ converge on $\Gamma$ to $F$. Relative to the base matrix $F_{J_0}$, put $$\delta_k(z)=
 \left\lVert F_{J_0}(z)^{-1}
 \left(F_{J_k}(z)-F_{J_{k-1}}(z)\right)\right\rVert_2,
 \qquad k\geq1.
 \label{eq:depth-increments}$$

[\[prop:geometric-tail\]]{#prop:geometric-tail label="prop:geometric-tail"} Assume that, for one $0\leq q<1$, $$\delta_{k+1}(z)\leq q\,\delta_k(z)
 \quad\text{for all }k\geq2\text{ and }z\in\Gamma.
 \label{eq:geometric-hypothesis}$$ Then $$\left\lVert F_{J_0}^{-1}(F-F_{J_0})\right\rVert_2
 \leq \delta_1+\frac{\delta_2}{1-q}
 \label{eq:geometric-bound}$$ pointwise on $\Gamma$. If the right-hand side is uniformly below one, the winding transfers from $F_{J_0}$ to $F$.

Telescope $F-F_{J_0}$, apply the triangle inequality, and sum the geometric series beginning with $\delta_2$. The final statement follows from the homotopy proof of [\[thm:directional-rouche\]](#thm:directional-rouche){reference-type="ref" reference="thm:directional-rouche"}.

In the numerical audit, $J_1=J_0+8$, $J_2=J_0+16$, and the displayed diagnostic uses $q=\delta_2/\delta_1$ where $\delta_1$ exceeds $10^{-12}$. Two increments do not prove [\[eq:geometric-hypothesis\]](#eq:geometric-hypothesis){reference-type="ref" reference="eq:geometric-hypothesis"}. Values below that floor are classified as roundoff-limited and are not used to infer contraction.

# From contour nodes to a continuous bound {#sec:continuous}

Directional or global inequalities must hold on all of $\Gamma$, not only at sampled nodes. One elementary component is available for the global shifted matrix.

[\[lem:lipschitz\]]{#lem:lipschitz label="lem:lipschitz"} Let $z_j=c+r\exp(2\pi i j/N)$, and suppose $\ell_j$ are rigorous lower bounds for $s_{\min}(z_j\mathrm I-B)$. Then every point of the circle satisfies $$s_{\min}(z\mathrm I-B)\geq
 \min_j\min(\ell_j,\ell_{j+1})
 -2r\sin\!\left(\frac{\pi}{2N}\right).
 \label{eq:lipschitz-circle}$$ The positive part of the right-hand side is therefore a valid full-circle lower bound.

For any matrices $M$ and $N$, Weyl's inequality gives $|s_{\min}(M)-s_{\min}(N)|\leq\left\lVert M-N\right\rVert_2$ [@HornJohnson2013]. Here $\left\lVert(z\mathrm I-B)-(w\mathrm I-B)\right\rVert_2=|z-w|$. Every point on the arc from $z_j$ to $z_{j+1}$ is within chord distance $2r\sin(\pi/(2N))$ of at least one endpoint. Apply the Lipschitz inequality and minimize over arcs.

The lemma is rigorous only if the nodal $\ell_j$ are rigorous. Ordinary `svds` outputs with small singular-triplet residuals remain floating-point candidates. Moreover, a positive nodal minimum can still produce a zero lower bound when the grid is too coarse. These two gaps are reported separately below.

# Numerical protocol {#sec:protocol}

## Seven-scale directional audit

The physical matrices, packet pairs, contours, and base Arnoldi depths are the frozen outputs of the target-blind RH-24 protocol [@WangContourFeshbach2026]. The scales are $$\sigma\in\{10^{-2},4\times10^{-3},2\times10^{-3},10^{-3},
 5\times10^{-4},2\times10^{-4},10^{-4}\}.$$ For each scale we rebuild the physical sparse matrix, retain the ambient Arnoldi bases through depth $J+16$, and evaluate $F_J$, $F_{J+8}$, and $F_{J+16}$ at 32 equally spaced nodes of the selected circle.

The ambient FOM solutions are reconstructed at depths $J$ and $J+16$. Their true residuals are evaluated by a fresh application of $QAQ$, so they include finite-precision Arnoldi recurrence defects rather than only the Hessenberg tail formula. At the node maximizing $$\left\lVert F_J^{-1}(F_{J+16}-F_J)\right\rVert_2,$$ we solve $(z\mathrm I-B)\widehat Y=R_J$ column by column with restarted GMRES [@SaadSchultz1986]. The absolute tolerance for column $i$ is $2\times10^{-14}\left\lVert c_i\right\rVert_2$; a column already below that threshold is skipped. The computed correction is $-E\widehat Y$, and its remaining ambient residual is evaluated explicitly.

## Global-resolvent and direct full-solve probes

At $\sigma=10^{-2}$, the Euclidean adjoint of the ambient extension $QAQ$ is implemented independently and checked by an inner-product identity. At 32 contour nodes, ARPACK applied through SciPy's `svds` computes the smallest singular triplet of $z\mathrm I-QAQ$ with tolerance $10^{-10}$. This full-space inverse norm is a conservative surrogate for sources restricted to $\operatorname{Ran}Q$. The maximum of the two singular equations is recorded as a triplet residual. We form the observation matrix $E$ explicitly because it has only four rows and evaluate the scalar candidate in [\[eq:scalar-majorant\]](#eq:scalar-majorant){reference-type="ref" reference="eq:scalar-majorant"}.

As a separate pointwise cross-check, zero-start GMRES solves the full forcing system $(z\mathrm I-B)X=C$ on 64 nodes with tolerance $2\times10^{-12}\left\lVert c_i\right\rVert_2$. This produces a direct floating approximation $\widehat F=z\mathrm I-D-E\widehat X$. Its determinant winding, true residuals, and difference from $F_J$ are recorded. It is not called the exact $F$.

At $\sigma=10^{-3}$, four cardinal contour points are submitted to the same global smallest-singular-value route with $\texttt{ncv}=24$, an ARPACK iteration cap of 120, and a 20-second wall-clock budget per point. A timeout is recorded as an algorithmic budget exhaustion, not as spectral evidence.

All matrix and vector calculations use complex double precision. The software stack is Python, NumPy, SciPy, and Matplotlib [@HarrisEtAl2020; @VirtanenEtAl2020; @Hunter2007]. Six unit tests cover the correction identity, scalar domination, geometric majorant, circular Lipschitz bound, winding calculation, and ambient FOM reconstruction.

# Directional closure results {#sec:directional-results}

## Winding, depth changes, and direct corrections

gives the complete seven-scale summary. The three entries in the winding column correspond to depths $J,J+8,J+16$. Residuals are Frobenius norms of the block residual divided by the Frobenius norm of $C$; every Rouché ratio uses the matrix 2-norm.

Every sampled winding is one. The largest adjacent determinant phase step over all depths and scales is $2.998<\pi$, so the 32-node phase sequence does not show aliasing. This is a floating sampling diagnostic, not an interval proof that the determinant is nonzero between nodes.

The two smallest scales are the informative regime. At $\sigma=2\times10^{-4}$, the extended-depth and direct ratios differ by $0.80\%$; at $\sigma=10^{-4}$, they differ by $0.23\%$. Thus the independently solved original residual reproduces the correction seen by adding 16 Arnoldi vectors. At the smallest scale the worst node is $$z=0.4010538961-0.4018727703i.$$ The correction matrix norm there is $1.24\times10^{-12}$, while the preconditioned packet ratio is $4.95\times10^{-11}$. All nine residual right-hand sides converge, with at most 39 iterations per column and 304 in total.

At $\sigma=2\times10^{-4}$, direct correction improves the base ambient residual by a factor $71.8$; at $10^{-4}$, by a factor $1086$. The corrected residual is approximately $10^{-14}$ at every scale. These figures support the computed $-E\widehat Y$, but without a certified error for $\widehat Y$ they do not establish [\[eq:rouche-condition\]](#eq:rouche-condition){reference-type="ref" reference="eq:rouche-condition"} exactly.

![Seven-scale directional closure. Top left: maximum depth increments. Top right: the $J$-to-$J+16$ change and the independent direct correction at its worst node. Bottom left: true ambient residuals. Bottom right: total direct-correction GMRES iterations. Values below $10^{-12}$ in the increment test are treated as roundoff-limited rather than evidence of geometric contraction.](<../../../../../zeta_mvp0/papers/RH-25-directional-rouche-closure/figures/directional_closure_summary.pdf>){#fig:directional-summary width="\\textwidth"}

## Where a geometric interpretation is informative

At the first five scales, every first depth increment is below the declared $10^{-12}$ interpretation floor. We therefore report no contraction ratio. At $\sigma=2\times10^{-4}$, six of 32 nodes are informative; all six have a second-to-first ratio below one, with maximum $0.0308$. Under the unproved continuation hypothesis of [\[prop:geometric-tail\]](#prop:geometric-tail){reference-type="ref" reference="prop:geometric-tail"}, the largest total tail majorant would be $9.33\times10^{-12}$. At $\sigma=10^{-4}$, eight nodes are informative, the maximum observed ratio is $0.0522$, and the conditional total is $4.99\times10^{-11}$.

These conditional totals closely track the direct corrections, but they are not substituted for a theorem about all future depths. The actual positive evidence is the finite extension and independent residual solve; the geometric interpretation is a roadmap for a later tail proof.

![Directional depth increments on three representative contours. At $\sigma=10^{-2}$ and $10^{-3}$, the structure lies at the floating-point floor. At $10^{-4}$, a resolved localized peak appears near $\theta=3\pi/4$, while the second increment is about two orders of magnitude smaller. Plotting zeros are displayed at $10^{-17}$.](<../../../../../zeta_mvp0/papers/RH-25-directional-rouche-closure/figures/directional_contour_profiles.pdf>){#fig:directional-profiles width="\\textwidth"}

## Cost of the direction actually required

The extended Arnoldi builds take $0.81$ seconds at $n=2048$, $158$ seconds at $n=102400$, and $367$ seconds at $n=204800$. The corresponding worst-node direct corrections take $0.04$, $160$, and $457$ seconds. The cost grows substantially, but the calculation remains a block of at most nine prescribed residual directions. It does not search for the worst response over the full $n$-dimensional unit sphere.

# The global-resolvent route {#sec:global-results}

## A favorable nodal result at coarse noise

At $\sigma=10^{-2}$, all 32 global singular-value solves converge. The independently implemented adjoint has relative inner-product defect $9.83\times10^{-20}$. The minimum sampled singular-value candidate is $$\min_js_{\min}(z_j\mathrm I-QAQ)=3.05054\times10^{-3},
 \label{eq:sampled-smin}$$ corresponding to a maximum resolvent-norm candidate $327.81$. The maximum singular-triplet residual is $1.08\times10^{-13}$, and $\left\lVert E\right\rVert_2=1.62192$. Combining these candidates with the true Arnoldi residual and the packet inverse gives $$\max_j
 \left\lVert F_J(z_j)^{-1}\right\rVert_2\left\lVert E\right\rVert_2
 s_{\min}(z_j\mathrm I-QAQ)^{-1}\left\lVert R_J(z_j)\right\rVert_2
 =8.63\times10^{-11}.
 \label{eq:sampled-global-majorant}$$ Thus the conservative global route is numerically favorable at the sampled nodes of the coarsest scale.

It is not yet a continuous or validated bound. The circle radius is $r=0.262499$, so the 32-node half-chord penalty in [\[eq:lipschitz-circle\]](#eq:lipschitz-circle){reference-type="ref" reference="eq:lipschitz-circle"} is $0.0257604$, more than eight times the minimum candidate in [\[eq:sampled-smin\]](#eq:sampled-smin){reference-type="ref" reference="eq:sampled-smin"}. The resulting full-circle lower candidate is zero. Even if the nodal values were rigorous, at least 271 equally spaced nodes would be needed merely to make this elementary penalty smaller than the observed minimum; additional nodes could reveal a smaller minimum. Validating every nodal singular value would remain a separate task.

## Direct full-forcing cross-check

The 64-node zero-start GMRES calculation supplies an independent approximation $\widehat F$. All 256 right-hand-side solves converge, with 72--91 total iterations per node. The maximum true block residual is $1.52\times10^{-12}$, and $$\max_j\left\lVert F_J(z_j)^{-1}(\widehat F(z_j)-F_J(z_j))\right\rVert_2
 =7.26\times10^{-12}.$$ The maximum unpreconditioned matrix difference is $5.46\times10^{-13}$. The sampled winding of $\det\widehat F$ is one and its maximum phase step is $1.838<\pi$. This cross-check is deliberately less accurate than the residual-direction solve at its tighter tolerance; its role is to show that a separately solved full forcing system gives the same finite sampled count.

![Global and direct probes at $\sigma=10^{-2}$. Left: sampled smallest singular-value candidates. Center: candidate resolvent norms and the corresponding scalar Rouché majorants. Right: the direct full-forcing GMRES difference from $F_J$ and its true residual. All quantities are floating point.](<../../../../../zeta_mvp0/papers/RH-25-directional-rouche-closure/figures/global_resolvent_probe.pdf>){#fig:global-probe width="\\textwidth"}

## Fixed-budget obstruction at the next scale

At $\sigma=10^{-3}$, the external dimension is 20480. Four cardinal nodes are tested with the same normal-equation singular-value route. Each exhausts its 20-second wall-clock budget before returning a singular triplet at tolerance $10^{-10}$. A separate unrestricted attempt during development also failed to return promptly and is not used as tabulated evidence.

This outcome has a narrow interpretation. It shows that the selected ARPACK/normal-equation implementation is already a poor scalable certification engine on this hardware and parameter choice. It does not show that $z\mathrm I-B$ is singular, that a lower bound cannot be proved by another method, or that the global majorant exceeds one. In contrast, the directional correction at this scale uses 22 total GMRES iterations and returns a ratio $7.14\times10^{-14}$. The comparison explains why the directional route is algorithmically relevant even before it is made rigorous.

# What is proved, what is observed, and what remains {#sec:status}

## Exact finite-dimensional conclusions

The following statements do not depend on the numerical results.

-   The correction identities [\[eq:x-correction,eq:f-correction\]](#eq:x-correction,eq:f-correction){reference-type="ref" reference="eq:x-correction,eq:f-correction"} are exact for every invertible shifted complement.

-   The uniform directional condition [\[eq:rouche-condition\]](#eq:rouche-condition){reference-type="ref" reference="eq:rouche-condition"} transfers the determinant winding by an exact homotopy argument.

-   An inexact directional solve separates exactly into a computed low-rank correction and the second residual term in [\[eq:two-level\]](#eq:two-level){reference-type="ref" reference="eq:two-level"}.

-   The global scalar product in [\[eq:scalar-majorant\]](#eq:scalar-majorant){reference-type="ref" reference="eq:scalar-majorant"} is sufficient but not necessary.

-   The geometric depth estimate is exact under [\[eq:geometric-hypothesis\]](#eq:geometric-hypothesis){reference-type="ref" reference="eq:geometric-hypothesis"}; two observed increments do not establish that hypothesis.

-   Rigorous nodal singular-value lower bounds extend to a circle by [\[eq:lipschitz-circle\]](#eq:lipschitz-circle){reference-type="ref" reference="eq:lipschitz-circle"}.

## Finite floating-point evidence

For the seven specified finite matrices, the computation supports the following narrower statements.

-   The sampled projected winding remains one at depths $J,J+8,J+16$.

-   At the two scales where the depth increment rises above the declared floor, direct correction of the original ambient residual agrees with the deeper Arnoldi model to within one percent.

-   The remaining residual after correction is at the $10^{-14}$ level, and all attempted correction solves converge.

-   At $\sigma=10^{-2}$, both a nodal global scalar calculation and a direct 64-node full-forcing solve are far below the Rouché threshold and have sampled winding one.

-   The elementary 32-node Lipschitz extension is zero, and the chosen global singular-value algorithm does not scale comfortably to $\sigma=10^{-3}$ under the recorded budget.

The first four observations strengthen the case that the RH-24 projected count reflects the finite-matrix Feshbach count. They still do not prove that $\det F$ is nonzero at every contour point, because neither the directional solve error nor the arcs between nodes have interval enclosures.

## A realistic certification route

The calculations suggest a more focused next step than a global pseudospectral enclosure.

1.  Construct a block residual solve for $(z\mathrm I-B)Y=R_J$ that returns a certified norm bound for $Y-\widehat Y$, preferably exploiting the retained Arnoldi relation and the rank $m\ll n$.

2.  Enclose the small matrices $F_J^{-1}E\widehat Y$ and $F_J^{-1}E$ on contour arcs. Analytic derivative bounds or interval rational evaluation can adapt the node density to the localized peak in [2](#fig:directional-profiles){reference-type="ref" reference="fig:directional-profiles"}.

3.  Combine those enclosures through [\[eq:directional-aposteriori\]](#eq:directional-aposteriori){reference-type="ref" reference="eq:directional-aposteriori"}, retaining the global resolvent only as an optional bound on a much smaller second residual.

4.  Validate the finite sparse-matrix and oblique-projection data, then separately address discretization convergence. Only after that step would a continuum or small-noise statement be meaningful.

A preconditioned contraction estimate for the residual block, a validated rational Krylov method, or a Grushin formulation with explicit inverse errors are plausible tools [@SjoestrandZworski2007; @TrefethenEmbree2005]. The present work does not select among them. Its contribution is to isolate the low-rank quantity that such a method must certify and to show that this quantity is numerically benign on the tested contours.

# Conclusion {#sec:conclusion}

The global external resolvent is not the intrinsic obstruction in the contour Feshbach transfer. Exact Schur algebra reduces the error to the resolvent action on the Arnoldi residual block, followed by the packet observation. On seven finite physical discretizations, extending the Krylov depth and directly correcting that block give consistent Rouché ratios, all below $5\times10^{-11}$, while true residuals are reduced to the $10^{-14}$ level. The projected winding remains one throughout.

The global route is informative but incomplete: it gives a small nodal majorant at coarse noise, fails a simple between-node Lipschitz test, and becomes computationally awkward at the next scale. This is an algorithmic barrier rather than a spectral no-go result. Directional closure opens a more economical route, but a rigorous result still requires certified directional errors and continuous contour control. The maze therefore has not ended; one broad dead end has been marked, and the next gate has been reduced to a concrete low-rank validation problem.

# Reproducibility and stored artifacts {#app:reproducibility}

The archived repository directory [@WangDirectionalCode2026] contains:

-   `src/directional_rouche`, implementing the exact correction, matrix ratio, scalar majorant, conditional geometric tail, circular Lipschitz extension, winding, and ambient FOM reconstruction;

-   , which performs the seven-scale extension and direct correction;

-   , which performs the global singular-value, direct full-forcing, and fixed-budget probes;

-   six unit tests and committed CSV, JSON, PDF, and PNG artifacts.

Run the unit tests with

    PYTHONPATH=src /root/math/.venv/bin/pytest -q

and reproduce the seven-scale audit with

    PYTHONPATH=src OPENBLAS_NUM_THREADS=16 /root/math/.venv/bin/python \
      experiments/run_directional_closure_audit.py

The independent probes are reproduced with

    PYTHONPATH=src:experiments OPENBLAS_NUM_THREADS=16 \
      /root/math/.venv/bin/python experiments/run_global_resolvent_probe.py

Figures and metadata can be regenerated from committed tables with `–reuse`. SHA-256 source hashes, software versions, and UTC generation times are stored in the JSON metadata. The fixed-budget probe is hardware-dependent by design and should be interpreted only together with its recorded dimension, tolerance, iteration cap, and wall-clock budget.
