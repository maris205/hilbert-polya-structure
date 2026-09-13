---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-48-intrinsic-riesz-identification"
canonical_tex: "zeta_mvp0/papers/RH-48-intrinsic-riesz-identification/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-48-intrinsic-riesz-identification/quadratic-schur-intrinsic-riesz-identification.pdf"
source_sha256: "f13ee582bdcb509a6e98e82b5d6c74bfffabaa160f693cac6c2ce92831449ab0"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Quadratic Schur Transport for Intrinsic Peripheral Riesz Identification A Dyadic Closure Theorem and the Remaining Directional Resolvent Gate

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-48-intrinsic-riesz-identification>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-48-intrinsic-riesz-identification/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-48-intrinsic-riesz-identification/quadratic-schur-intrinsic-riesz-identification.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-48-intrinsic-riesz-identification/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-48-intrinsic-riesz-identification/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For the small-noise folded-Gaussian transfer family, the continuum Perron and negative-parity weighted Riesz terms are known intrinsically, and their cell compression preserves the strict $n\sigma^2\to\infty$ bulk-square mesh law. The remaining defect compares that compressed continuum term with the finite Galerkin matrix's own spectral identification: $$\mathcal I_{n,\sigma}
   =\mathcal Q_{\rm per}(E_n\mathcal K_\sigma E_n)
    -E_n\mathcal Q_{\rm per}(\mathcal K_\sigma)E_n.$$ We isolate its exact mechanism.

  Relative to $L^2=V_n\oplus V_n^\perp$, write $$\mathcal K_\sigma=\begin{pmatrix}A_n&B_n\\C_n&D_n\end{pmatrix},
   \qquad
   \Sigma_n(z)=B_n(z-D_n)^{-1}C_n.$$ For either peripheral contour, the compressed fine weighted term minus the coarse weighted term is exactly $$\frac1{2\pi i}\int_\Gamma
   z\,(z-A_n-\Sigma_n(z))^{-1}
   B_n(z-D_n)^{-1}C_n(z-A_n)^{-1}\,dz.$$ Thus intrinsic identification starts quadratically in the two coarse--detail couplings. A Hilbert--Schmidt estimate requires only the directional actions $$(z-A_n-\Sigma_n(z))^{-1}B_n,
   \qquad C_n(z-A_n)^{-1},$$ not two global $L^2$ resolvent norms.

  For nested dyadic Galerkin spaces, the continuum defect is the convergent telescoping sum of adjacent defects. Gaussian derivative estimates give $$\left\lVert B_n\right\rVert_{\mathfrak S_2},\left\lVert C_n\right\rVert_{\mathfrak S_2}
   =O(n^{-1}\sigma^{-3/2}),
   \qquad
   \left\lVert D_n\right\rVert=O(n^{-2}\sigma^{-5/2}).$$ If the product of the normalized directional gains is $O(\sigma^{-\gamma})$ uniformly over dyadic refinements, then $$\left\lVert \mathcal I_{n,\sigma}\right\rVert_{\mathfrak S_2}
   =O(n^{-2}\sigma^{-3-\gamma}).$$ Consequently every schedule $n\sigma^2\to\infty$ remains sufficient when $\gamma\le1/2$. Uniform reduced directional resolvents would give only a polylogarithmic loss, because the already known residues grow like $\sqrt{\log(1/\sigma)}$; however that reduced-resolvent statement is not proved here.

  A binary64 audit uses exact Haar compression of sparse row-stochastic matrices at six noise levels, reaching dimension $204800$ and $133873007$ nonzero entries. Eighteen adjacent defects have joint fit $$0.01917\,n^{-1.99524}\sigma^{-1.97197},$$ and collapse to within nine percent on the candidate clock $C(n\sigma)^{-2}$. This sharper law is numerical evidence, not an analytic claim. The paper therefore closes the algebraic and mesh-power reduction while leaving one explicit directional small-noise gate. No arithmetic trace formula, self-adjoint spectral realization, zeta-zero identification, or Riemann-hypothesis conclusion is asserted.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Quadratic Schur Transport for Intrinsic Peripheral Riesz Identification\
  A Dyadic Closure Theorem and the Remaining Directional Resolvent Gate
```

## Markdown 正文

**Keywords:** weighted Riesz projection; Schur complement; Feshbach map; Galerkin approximation; Hilbert--Schmidt operator; small noise; transfer operator.

**MSC 2020:** 47A10; 47B10; 65R20; 37M25; 47A55.

# Introduction {#sec:introduction}

The fixed-noise spectral construction for the quadratic band-merging map now has two intrinsic peripheral kernels. The Perron term has kernel $\pi_\sigma(y)$ and the negative branch has kernel $\lambda_-(\sigma)h_\sigma(x)g_\sigma(y)$. Their sum $$\mathcal Q_{\mathrm{per},\sigma}
 =\mathcal Q_{+,\sigma}+\mathcal Q_{-,\sigma}
 \label{eq:qper-intro}$$ is independent of eigenvector gauge and can be subtracted before forming the trace-class bulk square [@WangWeightedKernel2026; @WangRankTwo2026].

The first small-noise analysis separated spatial resolution from the deterministic singular limit. For the raw folded-Gaussian kernel, $$\begin{aligned}
 \left\lVert \mathcal K_\sigma\right\rVert_{\mathfrak S_2}&=O(\sigma^{-1/2}),
 \label{eq:raw-size-intro}\\
 \left\lVert E_n\mathcal K_\sigma E_n-\mathcal K_\sigma\right\rVert_{\mathfrak S_2}
 &=O(n^{-1}\sigma^{-3/2}),
 \label{eq:raw-mesh-intro}\end{aligned}$$ and therefore $n\sigma^2\to\infty$ suffices for two-step trace-norm convergence [@WangSmallNoiseMesh2026]. The subsequent endpoint theorem showed that the peripheral residues are not uniformly bounded in $L^2$: $$\left\lVert P_{+,\sigma}\right\rVert,\left\lVert P_{-,\sigma}\right\rVert
 =\Theta\!\left(\sqrt{\log(1/\sigma)}\right).
 \label{eq:residue-log-intro}$$ Hence a fixed-circle global resolvent cannot be $O(1)$ in $L^2$. Nevertheless direct differentiation of the rank-two kernel gives $$\left\lVert E_n\mathcal Q_{\mathrm{per},\sigma}E_n-\mathcal Q_{\mathrm{per},\sigma}\right\rVert_{\mathfrak S_2}
 =O(n^{-1}\sigma^{-3/2}),
 \label{eq:qper-compression-intro}$$ so the continuum-anchored bulk retains the raw $p>2$ threshold [@WangLogConditioning2026].

The actual finite matrix does not use the continuum factors. Put $$G_{n,\sigma}=E_n\mathcal K_\sigma E_n
 \label{eq:galerkin-intro}$$ on the $n$-cell space. Its intrinsic bulk is $$B_{n,\sigma}^{\rm int}
 =G_{n,\sigma}-\mathcal Q_{\rm per}(G_{n,\sigma}),
 \label{eq:intrinsic-bulk-intro}$$ whereas the continuum-anchored compression is $$\widetilde B_{n,\sigma}
 =G_{n,\sigma}-E_n\mathcal Q_{\mathrm{per},\sigma}E_n.
 \label{eq:anchored-bulk-intro}$$ Their difference is exactly $$B_{n,\sigma}^{\rm int}-\widetilde B_{n,\sigma}
 =-\mathcal I_{n,\sigma},
 \qquad
 \mathcal I_{n,\sigma}
 :=\mathcal Q_{\rm per}(G_{n,\sigma})-E_n\mathcal Q_{\mathrm{per},\sigma}E_n.
 \label{eq:identification-intro}$$ This was the single unresolved arrow in the preceding paper.

The naive resolvent identity writes the weighted-term error as a product of two complete contour resolvents and the one-step Galerkin defect. It is valid, but it discards the geometry of an orthogonal compression. The correct block calculation starts and ends in $V_n$. An excursion into $V_n^\perp$ must therefore leave the coarse space and return. The first nonzero term is quadratic in the two couplings.

That observation has two consequences. First, the global logarithmic resolvent obstruction is no longer the relevant quantity. Only resolvent action on the coupling ranges appears. Second, an adjacent dyadic defect has order $n^{-2}$ rather than the $n^{-1}$ order of direct kernel compression. Summing adjacent defects over all refinements then recovers the continuum identification defect.

## Main results {#main-results .unnumbered}

The paper proves four statements.

1.  **Exact top-left Schur identity.** For a block operator $T=\left(\begin{smallmatrix}A&B\\C&D\end{smallmatrix}\right)$, the difference between the compressed weighted Riesz term of $T$ and that of $A$ is the contour integral of $$zSBR_DCR_A,
      \quad
      R_A=(z-A)^{-1},\quad R_D=(z-D)^{-1},\quad
      S=(z-A-BR_DC)^{-1}.$$

2.  **Directional Hilbert--Schmidt bound.** The integral is bounded by the product of $\left\lVert SB\right\rVert_{\mathfrak S_2}$ and $\left\lVert CR_A\right\rVert$, or by the symmetric placement of the Hilbert--Schmidt norm. No global bound for $S$ or $R_A$ is required.

3.  **Dyadic telescoping.** If $\Delta_{n,\sigma}$ denotes the exact adjacent defect between $n$ and $2n$, then $$\mathcal I_{n,\sigma}
      =\sum_{j\ge0}E_n\Delta_{2^jn,\sigma}E_n.$$ A quadratic $4^{-j}$ ledger therefore costs only the geometric factor $4/3$.

4.  **Conditional small-noise closure.** If the product of the normalized directional gains is $O(\sigma^{-\gamma})$, then $$\left\lVert \mathcal I_{n,\sigma}\right\rVert_{\mathfrak S_2}
      =O(n^{-2}\sigma^{-3-\gamma}).$$ For $\gamma\le1/2$, every strict $p>2$ schedule remains sufficient for the intrinsic bulk square.

The fourth statement is deliberately conditional. The paper does not derive a uniform small-noise upper for the reduced directional resolvents. It replaces the vague request for "uniform contour control" by a precise two-range condition with an exact allowable exponent. Positive and negative future results can now be compared against the threshold $\gamma=1/2$.

## Logical layers {#logical-layers .unnumbered}

The evidence is separated as follows.

Unconditional operator theory

:   The Schur identity, directional Schatten bound, residue--reduced decomposition, and dyadic telescoping theorem.

Previously proved analytic input

:   Gaussian derivative scales, continuum peripheral factor growth, direct rank-two compression, and the anchored bulk-square theorem [@WangSmallNoiseMesh2026; @WangLogConditioning2026].

Explicit remaining condition

:   A dyadically uniform bound on two normalized directional resolvent actions.

Floating diagnostic

:   Exact Haar compression of binary64 sparse matrices. "Exact" here refers to the algebraic nesting of the displayed finite matrices, not to interval validation of the continuum operator.

# Folded-Gaussian family and weighted peripheral terms {#sec:setup}

Let $I=[0,1]$ and let $u_{\rm c}$ be the first band-merging parameter. In folded coordinates the deterministic map is $$f(x)=1-u_{\rm c}x^2.
 \label{eq:map}$$ For $\sigma>0$, define the conditioned folded-Gaussian kernel $$k_\sigma(x,y)
 =\frac{\phi_\sigma(y-f(x))+\phi_\sigma(-y-f(x))}
 {Z_\sigma(x)},
 \qquad
 \phi_\sigma(t)=\frac{e^{-t^2/(2\sigma^2)}}
 {\sqrt{2\pi}\sigma},
 \label{eq:kernel}$$ where the row normalizer makes $\int_0^1k_\sigma(x,y)\,dy=1$. The Markov operator on observables is $$(\mathcal K_\sigma v)(x)=\int_0^1k_\sigma(x,y)v(y)\,dy.
 \label{eq:operator}$$ It is compact and strongly positive on $L^2(I)$ for every fixed $\sigma>0$.

The Perron branch has eigenvalue $1$, right observable $\mathbf1$, and stationary density $\pi_\sigma$. The negative branch has a simple real eigenvalue $\lambda_-(\sigma)\to-1$, right observable $h_\sigma$, and left density $g_\sigma$, normalized by $$\mathcal K_\sigma h_\sigma=\lambda_-h_\sigma,
 \quad
 \mathcal K_\sigma^*g_\sigma=\lambda_-g_\sigma,
 \quad
 \int_Ih_\sigma g_\sigma=1.
 \label{eq:parity-factors}$$ The weighted Riesz terms are $$\begin{aligned}
 (\mathcal Q_{+,\sigma}v)(x)
 &=\int_I\pi_\sigma(y)v(y)\,dy,
 \label{eq:perron-term}\\
 (\mathcal Q_{-,\sigma}v)(x)
 &=\lambda_-(\sigma)h_\sigma(x)
   \int_Ig_\sigma(y)v(y)\,dy.
 \label{eq:parity-term}\end{aligned}$$

For a positively oriented contour $\Gamma$ in the resolvent set of a bounded operator $T$, define $$\mathcal Q_\Gamma(T)
 :=\frac1{2\pi i}\int_\Gamma z(z-T)^{-1}\,dz.
 \label{eq:weighted-riesz}$$ If $\Gamma$ encloses one simple eigenvalue $\lambda$, then $\mathcal Q_\Gamma(T)=\lambda P_\lambda$. We use two disjoint fixed-geometry contours $\Gamma_+$ and $\Gamma_-$ around the Perron and parity branches and put $$\mathcal Q_{\rm per}(T)
 =\mathcal Q_{\Gamma_+}(T)+\mathcal Q_{\Gamma_-}(T).
 \label{eq:peripheral-functional}$$

Let $E_n$ be orthogonal averaging on the $n$ equal cells of $I$, and write $V_n=\operatorname{Ran}E_n$. All finite Galerkin operators are understood as operators on $V_n$ or as zero-extended operators on $L^2(I)$, according to context.

# The exact top-left Schur identity {#sec:schur}

We first work on an arbitrary Hilbert space. Let $P$ be an orthogonal projection, $Q=\mathrm I-P$, and decompose $$T=\begin{pmatrix}A&B\\C&D\end{pmatrix}
 \quad\text{on}\quad
 H=PH\oplus QH,
 \label{eq:block-T}$$ where $$A=PTP,
 \quad B=PTQ,
 \quad C=QTP,
 \quad D=QTQ.
 \label{eq:block-definitions}$$

For $z$ in the resolvent set of $D$, put $$R_D(z)=(z-D)^{-1},
 \quad
 \Sigma(z)=BR_D(z)C,
 \quad
 S(z)=(z-A-\Sigma(z))^{-1}.
 \label{eq:schur-objects}$$ The familiar block inverse is $$(z-T)^{-1}
 =\begin{pmatrix}
 S&SBR_D\\
 R_DCS&R_D+R_DCSBR_D
 \end{pmatrix}.
 \label{eq:block-resolvent}$$

[\[thm:exact-schur\]]{#thm:exact-schur label="thm:exact-schur"} Let $\Gamma$ lie in the resolvent sets of $T$, $A$, and $D$. Then $$P\mathcal Q_\Gamma(T)P-\mathcal Q_\Gamma(A)
 =\frac1{2\pi i}\int_\Gamma
 zS(z)B R_D(z)C(z-A)^{-1}\,dz.
 \label{eq:exact-schur-identity}$$ In particular, the top-left weighted-Riesz defect starts quadratically in $B$ and $C$.

The top-left block of [\[eq:block-resolvent\]](#eq:block-resolvent){reference-type="eqref" reference="eq:block-resolvent"} is $S$. With $R_A=(z-A)^{-1}$, the resolvent identity gives $$S-R_A=S\Sigma R_A=SBR_DCR_A.
 \label{eq:schur-resolvent-difference}$$ Insert this identity into the contour definition [\[eq:weighted-riesz\]](#eq:weighted-riesz){reference-type="eqref" reference="eq:weighted-riesz"}.

The theorem is stronger than applying the ordinary resolvent identity to $T$ and $A\oplus0$. The latter sees the off-diagonal perturbation $\left(\begin{smallmatrix}0&B\\C&D\end{smallmatrix}\right)$ linearly and pays for two complete resolvents. The top-left Schur identity records that an excursion contributing to $PH\to PH$ must contain both $C$ and $B$.

## Directional Schatten bound

The exact formula naturally places the Schatten norm on one composed directional factor.

[\[thm:directional-bound\]]{#thm:directional-bound label="thm:directional-bound"} Under the hypotheses of [\[thm:exact-schur\]](#thm:exact-schur){reference-type="ref" reference="thm:exact-schur"}, suppose $B,C\in\mathfrak S_2$. Put $$\begin{aligned}
 L_B^{(2)}
 &:=\sup_{z\in\Gamma}\left\lVert S(z)B\right\rVert_{\mathfrak S_2},
 &
 L_C^{(\infty)}
 &:=\sup_{z\in\Gamma}\left\lVert C(z-A)^{-1}\right\rVert,
 \label{eq:left-right-directional}\\
 L_B^{(\infty)}
 &:=\sup_{z\in\Gamma}\left\lVert S(z)B\right\rVert,
 &
 L_C^{(2)}
 &:=\sup_{z\in\Gamma}\left\lVert C(z-A)^{-1}\right\rVert_{\mathfrak S_2}.
 \label{eq:left-right-directional-symmetric}\end{aligned}$$ Then $$\begin{aligned}
 \left\lVert P\mathcal Q_\Gamma(T)P-\mathcal Q_\Gamma(A)\right\rVert_{\mathfrak S_2}
 \le{}&
 \frac{\operatorname{length}(\Gamma)}{2\pi}
 \max_{z\in\Gamma}|z|
 \sup_{z\in\Gamma}\left\lVert R_D(z)\right\rVert
 \notag\\
 &\times
 \min\!\left\{
 L_B^{(2)}L_C^{(\infty)},
 L_B^{(\infty)}L_C^{(2)}
 \right\}.
 \label{eq:directional-schur-bound}\end{aligned}$$

Use [\[eq:exact-schur-identity\]](#eq:exact-schur-identity){reference-type="eqref" reference="eq:exact-schur-identity"}, the ideal inequalities $\left\lVert XY\right\rVert_{\mathfrak S_2}\le\left\lVert X\right\rVert_{\mathfrak S_2}\left\lVert Y\right\rVert$ and $\left\lVert XY\right\rVert_{\mathfrak S_2}\le\left\lVert X\right\rVert\left\lVert Y\right\rVert_{\mathfrak S_2}$, and then integrate the uniform majorant around $\Gamma$.

The quantities in [\[eq:left-right-directional\]](#eq:left-right-directional){reference-type="eqref" reference="eq:left-right-directional"} ask only how the coarse resolvents act after entrance through $B$ and before exit through $C$. They may stay small even when the global resolvent is large on an unrelated direction. This is the same goal-oriented principle that appears in directional Feshbach and primal--dual residual estimates, now applied to the weighted Riesz term itself.

## Residues versus reduced directional resolvents

The logarithmic lower bound in [\[eq:residue-log-intro\]](#eq:residue-log-intro){reference-type="eqref" reference="eq:residue-log-intro"} comes from the residue. It should not be confused with an upper for the reduced complement. The Schur formula permits an exact separation.

Assume $\Gamma$ encloses one simple eigenvalue $\lambda$ of $T$ and one simple eigenvalue $\mu$ of $A$. Let $\Pi_T$ and $\Pi_A$ be their Riesz projections. The top-left resolvent residue is $$\widehat\Pi_T=P\Pi_TP.
 \label{eq:compressed-residue}$$ On $\Gamma$ write $$\begin{aligned}
 S(z)&=\frac{\widehat\Pi_T}{z-\lambda}+S^\circ(z),
 \label{eq:S-reduced}\\
 (z-A)^{-1}&=\frac{\Pi_A}{z-\mu}+R_A^\circ(z).
 \label{eq:RA-reduced}\end{aligned}$$

[\[prop:residue-reduced\]]{#prop:residue-reduced label="prop:residue-reduced"} Let $$d_T=\min_{z\in\Gamma}|z-\lambda|,
 \qquad
 d_A=\min_{z\in\Gamma}|z-\mu|.
 \label{eq:pole-distances}$$ Then $$\begin{aligned}
 L_B^{(2)}
 &\le
 \sup_\Gamma\left\lVert S^\circ(z)B\right\rVert_{\mathfrak S_2}
 +d_T^{-1}\left\lVert \widehat\Pi_TB\right\rVert_{\mathfrak S_2},
 \label{eq:left-reduced-bound}\\
 L_C^{(\infty)}
 &\le
 \sup_\Gamma\left\lVert CR_A^\circ(z)\right\rVert
 +d_A^{-1}\left\lVert C\Pi_A\right\rVert.
 \label{eq:right-reduced-bound}\end{aligned}$$ The symmetric bounds hold with the Schatten norm interchanged.

Multiply [\[eq:S-reduced\]](#eq:S-reduced){reference-type="eqref" reference="eq:S-reduced"} by $B$ and [\[eq:RA-reduced\]](#eq:RA-reduced){reference-type="eqref" reference="eq:RA-reduced"} by $C$, then apply the triangle inequality.

Suppose the contours have fixed geometry, the fine and coarse projection norms are both $O(\sqrt{\log(1/\sigma)})$, and the normalized reduced directional actions are $O(1)$. Then the product in [\[eq:directional-schur-bound\]](#eq:directional-schur-bound){reference-type="eqref" reference="eq:directional-schur-bound"} is at most $O(\log(1/\sigma))$ after the two coupling norms are factored out. The global reduced resolvent may be much larger; [\[prop:residue-reduced\]](#prop:residue-reduced){reference-type="ref" reference="prop:residue-reduced"} does not ask for it. Conversely, this paper does not prove even the weaker directional $O(1)$ statement. It identifies it as the exact next analytic gate.

# Dyadic telescoping of the continuum defect {#sec:dyadic}

The Schur identity compares one fine operator with one coarse block. We now show that adjacent comparisons sum exactly to the continuum identification defect.

Let the cell spaces be nested dyadically: $$V_n\subset V_{2n}\subset V_{4n}\subset\cdots,
 \qquad
 E_nE_{2n}=E_n.
 \label{eq:nested-spaces}$$ For fixed $\sigma$, put $$A_{n,\sigma}=E_n\mathcal K_\sigma E_n.
 \label{eq:An}$$ All weighted terms below use the same pair of peripheral contours.

[\[def:adjacent-defect\]]{#def:adjacent-defect label="def:adjacent-defect"} Define $$\Delta_{n,\sigma}
 :=\mathcal Q_{\rm per}(A_{n,\sigma})
 -E_n\mathcal Q_{\rm per}(A_{2n,\sigma})E_n.
 \label{eq:adjacent-defect}$$ The continuum defect is $$\mathcal I_{n,\sigma}
 =\mathcal Q_{\rm per}(A_{n,\sigma})
 -E_n\mathcal Q_{\rm per}(\mathcal K_\sigma)E_n.
 \label{eq:continuum-defect}$$

[\[lem:dyadic-recursion\]]{#lem:dyadic-recursion label="lem:dyadic-recursion"} Whenever the displayed weighted terms are defined, $$\mathcal I_{n,\sigma}
 =\Delta_{n,\sigma}+E_n\mathcal I_{2n,\sigma}E_n.
 \label{eq:dyadic-recursion}$$

Add and subtract $E_n\mathcal Q_{\rm per}(A_{2n,\sigma})E_n$ in [\[eq:continuum-defect\]](#eq:continuum-defect){reference-type="eqref" reference="eq:continuum-defect"}, and use $E_nE_{2n}=E_n$.

For each fixed $\sigma>0$, the kernel is smooth and compact. Standard collectively compact Galerkin theory gives convergence of isolated Riesz terms once the contours are fixed in the resolvent set [@Chatelin1983; @Kato1995]. Thus $$\left\lVert \mathcal I_{2^mn,\sigma}\right\rVert_{\mathfrak S_2}\longrightarrow0
 \qquad(m\to\infty).
 \label{eq:fixed-sigma-tail}$$

[\[thm:dyadic-series\]]{#thm:dyadic-series label="thm:dyadic-series"} For fixed $\sigma$, suppose the two peripheral contours remain admissible along the dyadic chain and [\[eq:fixed-sigma-tail\]](#eq:fixed-sigma-tail){reference-type="eqref" reference="eq:fixed-sigma-tail"} holds. Then $$\mathcal I_{n,\sigma}
 =\sum_{j=0}^\infty
 E_n\Delta_{2^jn,\sigma}E_n,
 \label{eq:dyadic-series}$$ where each adjacent defect is naturally extended to $L^2(I)$. In particular, if $$\left\lVert \Delta_{2^jn,\sigma}\right\rVert_{\mathfrak S_2}
 \le M_{n,\sigma}4^{-j},
 \label{eq:quadratic-dyadic-ledger}$$ then $$\left\lVert \mathcal I_{n,\sigma}\right\rVert_{\mathfrak S_2}
 \le\frac43M_{n,\sigma}.
 \label{eq:four-thirds}$$

Iterate [\[eq:dyadic-recursion\]](#eq:dyadic-recursion){reference-type="eqref" reference="eq:dyadic-recursion"} $m$ times. Orthogonal compression is a contraction in $\mathfrak S_2$, so the finite sum is dominated by the sum of the adjacent norms. Let $m\to\infty$ and use [\[eq:fixed-sigma-tail\]](#eq:fixed-sigma-tail){reference-type="eqref" reference="eq:fixed-sigma-tail"}. Under [\[eq:quadratic-dyadic-ledger\]](#eq:quadratic-dyadic-ledger){reference-type="eqref" reference="eq:quadratic-dyadic-ledger"}, sum the geometric series $\sum_{j\ge0}4^{-j}=4/3$.

This theorem is useful both analytically and computationally. A future validated proof need not compare one finite matrix directly with an infinite-dimensional contour integral. It may certify a sequence of adjacent Schur steps and sum their explicit tails.

# Gaussian block scales {#sec:block-scales}

Take the adjacent split $$V_{2n}=V_n\oplus W_n,
 \label{eq:haar-split}$$ where $W_n$ is the Haar detail space, and write $$A_{2n,\sigma}
 =\begin{pmatrix}
 A_{n,\sigma}&B_{n,\sigma}\\
 C_{n,\sigma}&D_{n,\sigma}
 \end{pmatrix}.
 \label{eq:adjacent-blocks}$$

Let $$K_x(\sigma)=\left\lVert \partial_xk_\sigma\right\rVert_{L^2(I^2)},
 \quad
 K_y(\sigma)=\left\lVert \partial_yk_\sigma\right\rVert_{L^2(I^2)},
 \quad
 K_{xy}(\sigma)=\left\lVert \partial_x\partial_yk_\sigma\right\rVert_{L^2(I^2)}.
 \label{eq:derivative-envelopes}$$ The one-dimensional Poincaré--Wirtinger inequality applied in the appropriate cell variable gives $$\begin{aligned}
 \left\lVert B_{n,\sigma}\right\rVert_{\mathfrak S_2}
 &\le\frac{K_y(\sigma)}{\pi n},
 \label{eq:B-bound}\\
 \left\lVert C_{n,\sigma}\right\rVert_{\mathfrak S_2}
 &\le\frac{K_x(\sigma)}{\pi n},
 \label{eq:C-bound}\\
 \left\lVert D_{n,\sigma}\right\rVert_{\mathfrak S_2}
 &\le\frac{K_{xy}(\sigma)}{\pi^2n^2}.
 \label{eq:D-bound}\end{aligned}$$ These are the infinite-complement and adjacent-Haar estimates used in the validated fixed-noise Schur constructions [@WangWeightedKernel2026; @WangRankTwo2026].

For the normalized folded Gaussian, differentiation of the kernel and its row normalizer gives, for fixed derivative order, $$\left\lVert \partial_x^a\partial_y^b k_\sigma\right\rVert_{L^2(I^2)}
 =O(\sigma^{-a-b-1/2}).
 \label{eq:gaussian-all-derivatives}$$ In particular, $$\begin{aligned}
 K_x(\sigma)+K_y(\sigma)&=O(\sigma^{-3/2}),
 \label{eq:first-derivatives}\\
 K_{xy}(\sigma)&=O(\sigma^{-5/2}).
 \label{eq:mixed-derivative}\end{aligned}$$ Thus $$\begin{aligned}
 \left\lVert B_{n,\sigma}\right\rVert_{\mathfrak S_2}
 +\left\lVert C_{n,\sigma}\right\rVert_{\mathfrak S_2}
 &=O(n^{-1}\sigma^{-3/2}),
 \label{eq:coupling-clock}\\
 \left\lVert D_{n,\sigma}\right\rVert
 &=O(n^{-2}\sigma^{-5/2}).
 \label{eq:detail-clock}\end{aligned}$$

Let $\rho_\Gamma=\min_{z\in\Gamma}|z|$. If $\left\lVert D_{n,\sigma}\right\rVert<\rho_\Gamma$, then $$\sup_{z\in\Gamma}\left\lVert (z-D_{n,\sigma})^{-1}\right\rVert
 \le\frac1{\rho_\Gamma-\left\lVert D_{n,\sigma}\right\rVert}.
 \label{eq:detail-resolvent}$$ Under $n\sigma^2\to\infty$, $$n^{-2}\sigma^{-5/2}
 =(n\sigma^2)^{-2}\sigma^{3/2}\longrightarrow0,
 \label{eq:detail-vanishes}$$ so the detail resolvent is uniformly $O(1)$ on either fixed peripheral contour. The unresolved growth lies entirely in the two coarse directional actions.

# The directional small-noise condition {#sec:directional-condition}

For each branch $s\in\{+,-\}$, let $\Gamma_s$ be its contour. Relative to the adjacent split [\[eq:adjacent-blocks\]](#eq:adjacent-blocks){reference-type="eqref" reference="eq:adjacent-blocks"}, define $$\begin{aligned}
 R_{A,s}(z)&=(z-A_{n,\sigma})^{-1},
 \notag\\
 R_{D,s}(z)&=(z-D_{n,\sigma})^{-1},
 \notag\\
 S_s(z)&=
 \left(z-A_{n,\sigma}
 -B_{n,\sigma}R_{D,s}(z)C_{n,\sigma}\right)^{-1}.
 \label{eq:branch-schur-objects}\end{aligned}$$

When the denominator coupling norm is nonzero, put $$\begin{aligned}
 \ell_{B,s}^{(2)}(n,\sigma)
 &:=\sup_{z\in\Gamma_s}
 \frac{\left\lVert S_s(z)B_{n,\sigma}\right\rVert_{\mathfrak S_2}}
 {\left\lVert B_{n,\sigma}\right\rVert_{\mathfrak S_2}},
 \label{eq:normalized-left-hs}\\
 \ell_{C,s}^{(\infty)}(n,\sigma)
 &:=\sup_{z\in\Gamma_s}
 \frac{\left\lVert C_{n,\sigma}R_{A,s}(z)\right\rVert}
 {\left\lVert C_{n,\sigma}\right\rVert},
 \label{eq:normalized-right-op}\end{aligned}$$ and define the symmetric pair by interchanging the Schatten norm. Zero couplings are assigned zero gain. The combined directional gain is $$\mathcal L_{n,\sigma}
 :=\sum_{s\in\{+,-\}}
 \min\!\left\{
 \ell_{B,s}^{(2)}\ell_{C,s}^{(\infty)},
 \ell_{B,s}^{(\infty)}\ell_{C,s}^{(2)}
 \right\}.
 \label{eq:combined-gain}$$ Fixed contour length, maximum modulus, and the bounded detail resolvent are absorbed into constants below.

[\[cond:directional-gain\]]{#cond:directional-gain label="cond:directional-gain"} There are $C<\infty$, $\sigma_0>0$, and $n_0(\sigma)$ such that the two contours lie in the required resolvent sets and $$\sup_{j\ge0}\mathcal L_{2^jn,\sigma}
 \le C\sigma^{-\gamma}
 \label{eq:gain-condition}$$ for $0<\sigma<\sigma_0$ and $n\ge n_0(\sigma)$.

This condition is weaker than a global reduced-resolvent bound. It does not control the resolvent on vectors orthogonal to the two coupling ranges. It also retains the full fine Schur inverse on the left, so no perturbative replacement by the coarse resolvent is hidden in the definition.

[\[thm:adjacent-bound\]]{#thm:adjacent-bound label="thm:adjacent-bound"} Under [\[cond:directional-gain\]](#cond:directional-gain){reference-type="ref" reference="cond:directional-gain"} and the Gaussian derivative estimates, $$\left\lVert \Delta_{n,\sigma}\right\rVert_{\mathfrak S_2}
 =O(n^{-2}\sigma^{-3-\gamma}).
 \label{eq:adjacent-small-noise}$$ The same bound holds uniformly at level $2^jn$ with an additional factor $4^{-j}$.

Apply [\[thm:directional-bound\]](#thm:directional-bound){reference-type="ref" reference="thm:directional-bound"} to each contour and use [\[eq:coupling-clock\]](#eq:coupling-clock){reference-type="eqref" reference="eq:coupling-clock"}, [\[eq:detail-resolvent\]](#eq:detail-resolvent){reference-type="eqref" reference="eq:detail-resolvent"}, and [\[eq:gain-condition\]](#eq:gain-condition){reference-type="eqref" reference="eq:gain-condition"}. The two coupling norms contribute $n^{-2}\sigma^{-3}$; replacing $n$ by $2^jn$ contributes $4^{-j}$.

[\[thm:intrinsic-identification\]]{#thm:intrinsic-identification label="thm:intrinsic-identification"} Under the hypotheses of [\[thm:adjacent-bound\]](#thm:adjacent-bound){reference-type="ref" reference="thm:adjacent-bound"} and the fixed-$\sigma$ Galerkin convergence in [\[thm:dyadic-series\]](#thm:dyadic-series){reference-type="ref" reference="thm:dyadic-series"}, $$\boxed{
 \left\lVert \mathcal I_{n,\sigma}\right\rVert_{\mathfrak S_2}
 =O(n^{-2}\sigma^{-3-\gamma}).}
 \label{eq:intrinsic-identification-bound}$$ If $\gamma\le1/2$ and $$n(\sigma)\sigma^2\longrightarrow\infty,
 \label{eq:p-two-again}$$ then $$\left\lVert \mathcal I_{n,\sigma}\right\rVert_{\mathfrak S_2}
 =o(n^{-1}\sigma^{-3/2}).
 \label{eq:identification-lower-order}$$

The first statement follows from [\[thm:dyadic-series\]](#thm:dyadic-series){reference-type="ref" reference="thm:dyadic-series"} and the factor $4/3$. Divide [\[eq:intrinsic-identification-bound\]](#eq:intrinsic-identification-bound){reference-type="eqref" reference="eq:intrinsic-identification-bound"} by the anchored one-step clock: $$\frac{n^{-2}\sigma^{-3-\gamma}}
 {n^{-1}\sigma^{-3/2}}
 =\frac{\sigma^{1/2-\gamma}}{n\sigma^2}.
 \label{eq:relative-clock}$$ For $\gamma\le1/2$, the numerator is bounded and the denominator tends to infinity.

For a pure power $n(\sigma)\asymp\sigma^{-p}$, the intrinsic defect has exponent $$2p-3-\gamma,
 \label{eq:identification-power}$$ while its ratio to the anchored one-step error has exponent $$p-\frac32-\gamma.
 \label{eq:relative-power}$$ Combining this with the anchored trace threshold $p>2$ gives the sufficient condition $$p>\max\!\left\{2,\frac32+\gamma\right\}.
 \label{eq:general-p-threshold}$$ Thus $\gamma=1/2$ is the precise boundary at which all strict $p>2$ schedules survive.

[\[cor:polylog-closure\]]{#cor:polylog-closure label="cor:polylog-closure"} If, for some fixed $m$, the dyadic directional gain satisfies $$\sup_{j\ge0}\mathcal L_{2^jn,\sigma}
 =O((\log(1/\sigma))^m),
 \label{eq:polylog-gain}$$ then $$\left\lVert \mathcal I_{n,\sigma}\right\rVert_{\mathfrak S_2}
 =O\!\left(
 n^{-2}\sigma^{-3}(\log(1/\sigma))^m
 \right),
 \label{eq:polylog-identification}$$ and every schedule [\[eq:p-two-again\]](#eq:p-two-again){reference-type="eqref" reference="eq:p-two-again"} satisfies [\[eq:identification-lower-order\]](#eq:identification-lower-order){reference-type="eqref" reference="eq:identification-lower-order"}.

Every fixed power of $\log(1/\sigma)$ is $o(\sigma^{-1/2})$. Repeat [\[eq:relative-clock\]](#eq:relative-clock){reference-type="eqref" reference="eq:relative-clock"}.

By [\[prop:residue-reduced\]](#prop:residue-reduced){reference-type="ref" reference="prop:residue-reduced"}, uniformly bounded reduced directional resolvents together with $O(\sqrt{\log})$ bounds for both the fine and coarse residues would give [\[cor:polylog-closure\]](#cor:polylog-closure){reference-type="ref" reference="cor:polylog-closure"} with $m=1$. The continuum residue law is known; its dyadically uniform coarse counterpart and the reduced directional bounds remain part of the premise. The implication is rigorous, but that premise is not proved here.

# Transfer to the actual intrinsic bulk square {#sec:bulk-transfer}

The continuum-anchored theorem gives $$\begin{aligned}
 \left\lVert \widetilde B_{n,\sigma}-\mathcal B_\sigma\right\rVert_{\mathfrak S_2}
 &=O(n^{-1}\sigma^{-3/2}),
 \label{eq:anchored-hs-recall}\\
 \left\lVert \widetilde B_{n,\sigma}^2-\mathcal B_\sigma^2\right\rVert_{\mathfrak S_1}
 &=O(n^{-1}\sigma^{-2})+O(n^{-2}\sigma^{-3}),
 \label{eq:anchored-trace-recall}\\
 \left\lVert \widetilde B_{n,\sigma}\right\rVert_{\mathfrak S_2}
 &=O(\sigma^{-1/2}).
 \label{eq:anchored-size-recall}\end{aligned}$$ The exact relation [\[eq:identification-intro\]](#eq:identification-intro){reference-type="eqref" reference="eq:identification-intro"} now transfers those bounds.

[\[cor:intrinsic-bulk-square\]]{#cor:intrinsic-bulk-square label="cor:intrinsic-bulk-square"} Under [\[cond:directional-gain\]](#cond:directional-gain){reference-type="ref" reference="cond:directional-gain"} with $\gamma\le1/2$ and $n\sigma^2\to\infty$, $$\begin{aligned}
 \left\lVert B_{n,\sigma}^{\rm int}-\mathcal B_\sigma\right\rVert_{\mathfrak S_2}
 &=O(n^{-1}\sigma^{-3/2}),
 \label{eq:intrinsic-hs-final}\\
 \left\lVert (B_{n,\sigma}^{\rm int})^2-\mathcal B_\sigma^2\right\rVert_{\mathfrak S_1}
 &\longrightarrow0.
 \label{eq:intrinsic-trace-final}\end{aligned}$$ For $n\asymp\sigma^{-p}$, every $p>2$ is sufficient.

Equation [\[eq:identification-lower-order\]](#eq:identification-lower-order){reference-type="eqref" reference="eq:identification-lower-order"} and [\[eq:identification-intro\]](#eq:identification-intro){reference-type="eqref" reference="eq:identification-intro"} preserve [\[eq:anchored-hs-recall\]](#eq:anchored-hs-recall){reference-type="eqref" reference="eq:anchored-hs-recall"}. For the square difference between intrinsic and anchored bulks, $$\begin{aligned}
 \left\lVert (B_{n,\sigma}^{\rm int})^2
       -\widetilde B_{n,\sigma}^2\right\rVert_{\mathfrak S_1}
 &\le
 \left\lVert \mathcal I_{n,\sigma}\right\rVert_{\mathfrak S_2}
 \left(2\left\lVert \widetilde B_{n,\sigma}\right\rVert_{\mathfrak S_2}
       +\left\lVert \mathcal I_{n,\sigma}\right\rVert_{\mathfrak S_2}\right).
 \label{eq:intrinsic-square-difference}\end{aligned}$$ The leading additional clock is $n^{-2}\sigma^{-7/2-\gamma}$. Relative to the leading anchored trace clock $n^{-1}\sigma^{-2}$, its ratio is again $n^{-1}\sigma^{-3/2-\gamma}$, equal to the right-hand side of [\[eq:relative-clock\]](#eq:relative-clock){reference-type="eqref" reference="eq:relative-clock"}. It tends to zero for $\gamma\le1/2$ under $n\sigma^2\to\infty$. Combine with [\[eq:anchored-trace-recall\]](#eq:anchored-trace-recall){reference-type="eqref" reference="eq:anchored-trace-recall"}.

The conclusion is important but conditional: the finite matrix's actual weighted-Riesz subtraction inherits the anchored theorem if and only if the new directional gate is met. The paper has not silently replaced that gate by the observed finite-matrix scaling.

# Exact-Haar floating audit {#sec:numerics}

The analytic theorem identifies a quadratic clock. We test that clock on the same row-normalized eight-sigma sparse folded-Gaussian family used in the preceding small-noise studies.

## Nested construction

For each $\sigma$, build one finest row-stochastic matrix $K_N$ with $$N\sigma\simeq40.96.
 \label{eq:finest-resolution}$$ Every coarser matrix is then obtained by exact orthogonal Haar compression, not by rebuilding a separate midpoint quadrature. If $R$ averages each pair of fine values and $L$ repeats a coarse value on both children, then $$K_{N/2}=RK_NL,
 \qquad RL=\mathrm I.
 \label{eq:exact-haar-compression}$$ Thus each displayed adjacent comparison is an exact finite-dimensional instance of [\[thm:exact-schur\]](#thm:exact-schur){reference-type="ref" reference="thm:exact-schur"}, up to floating eigensolver error.

Let a weighted rank-two term be represented as $$Q_N=U_NV_N^{\mathsf T},
 \label{eq:factorization}$$ where the columns of $U_N$ are the right value vectors and the columns of $V_N$ are the left cell-mass vectors, with the parity column multiplied by $\lambda_-$. Under a compression ratio $r$, the exact coarse factors of $RQ_NL$ are $$(U_N)_{\rm comp}=\operatorname{blockmean}_r(U_N),
 \qquad
 (V_N)_{\rm comp}=\operatorname{blocksum}_r(V_N).
 \label{eq:factor-compression}$$ All Frobenius norms and singular values are evaluated from matrices of size at most $4\times4$ using factor Gram matrices. The dense rank-two operator is never formed.

## Observed dyadic law

The full audit uses six noise levels and four nested dimensions at each level. The largest matrix has dimension $204800$ and $133873007$ nonzero entries. reports the finest adjacent defect, whose coarse level satisfies $n\sigma=20.48$.

::: {#tab:dyadic-audit}
        $\sigma$        $n$   $\left\lVert \Delta_{n,\sigma}\right\rVert_{\mathfrak S_2}$   $(n\sigma)^2\left\lVert \Delta\right\rVert_{\mathfrak S_2}$     mesh fit   finest nonzeros
  -------------- ---------- ------------------------------------------------------------- ------------------------------------------------------------- ------------ -----------------
       $10^{-2}$     $2048$                                          $4.1943879\,10^{-5}$                                                  $0.01759254$   $-1.99553$         $2457479$
    $4\,10^{-3}$     $5120$                                          $4.0657159\,10^{-5}$                                                  $0.01705285$   $-1.99543$         $6399048$
    $2\,10^{-3}$    $10240$                                          $4.0158494\,10^{-5}$                                                  $0.01684369$   $-1.99523$        $13032853$
       $10^{-3}$    $20480$                                          $3.8877260\,10^{-5}$                                                  $0.01630630$   $-1.99511$        $26379457$
    $5\,10^{-4}$    $40960$                                          $3.8771105\,10^{-5}$                                                  $0.01626178$   $-1.99511$        $53184355$
    $2\,10^{-4}$   $102400$                                          $3.8402422\,10^{-5}$                                                  $0.01610714$   $-1.99502$       $133873007$

  : Floating exact-Haar intrinsic identification audit.
:::

At every fixed $\sigma$, a three-level regression of the weighted rank-two defect against $n$ lies between $$-1.99553\quad\text{and}\quad-1.99502.
 \label{eq:mesh-fit-range}$$ The joint eighteen-point regression is $$\left\lVert \Delta_{n,\sigma}\right\rVert_{\mathfrak S_2}
 \approx
 0.0191729\,n^{-1.995237}\sigma^{-1.971971},
 \label{eq:joint-fit}$$ with maximum log residual $0.01579$. Equivalently, at fixed $n\sigma$ the fitted $\sigma$ power is approximately $0.0232$, close to zero. Across the six noise levels, the normalized quantity at $n\sigma=20.48$ varies by less than nine percent.

The branch-resolved defect is parity dominated. At the smallest noise, $$\left\lVert \Delta_+\right\rVert_{\mathfrak S_2}=1.3958552\,10^{-5},
 \qquad
 \left\lVert \Delta_-\right\rVert_{\mathfrak S_2}=3.5944471\,10^{-5},
 \label{eq:smallest-branch-defects}$$ while the combined weighted rank-two value is $3.8402422\times10^{-5}$.

## Double-resolution replay

To test whether the apparent collapse is an artifact of the chosen finest matrix, the experiment is repeated at $$N\sigma\simeq81.92
 \label{eq:double-resolution}$$ for $\sigma=0.004$ and $0.001$. Four overlapping defects at $n\sigma=20.48$ and $10.24$ change by at most $$1.5676\times10^{-4}
 \label{eq:replay-relative}$$ in relative terms. The three-level mesh slopes sharpen to $-1.99885$ and $-1.99878$, respectively.

![Quadratic Schur identification and its exact remaining gate. (a) Adjacent exact-Haar defects at six noise levels; every fitted slope is near $-2$. (b) Collapse after multiplication by $(n\sigma)^2$. (c) Perron, negative-parity, and combined weighted defects at $n\sigma=20.48$. (d) The analytic threshold $p>\max\{2,3/2+\gamma\}$: every strict $p>2$ schedule survives when $\gamma\le1/2$. Panels (a)--(c) are binary64 diagnostics; panel (d) is the proved exponent ledger under [\[cond:directional-gain\]](#cond:directional-gain){reference-type="ref" reference="cond:directional-gain"}.](figures/intrinsic_riesz_identification.pdf){#fig:summary width="\\textwidth"}

The numerical law $$\left\lVert \Delta_{n,\sigma}\right\rVert_{\mathfrak S_2}
 \asymp(n\sigma)^{-2}
 \label{eq:candidate-law}$$ is one full power of $\sigma$ better than the generic product of two Hilbert--Schmidt derivative bounds. It may reflect cancellation, sharper mixed-norm coupling estimates, or the special entrance and exit directions of the two peripheral modes. Distinguishing those mechanisms is a mathematical problem, not a regression exercise. We therefore archive [\[eq:candidate-law\]](#eq:candidate-law){reference-type="eqref" reference="eq:candidate-law"} as a candidate law only.

# What is closed and what remains {#sec:conclusion}

The intrinsic identification problem has now separated into an algebraic part, a mesh part, and a genuinely spectral part.

1.  **Algebraic part: closed.** The exact top-left difference is a Schur self-energy integral and begins quadratically in the coarse--detail couplings.

2.  **Trace-ideal part: closed.** The Hilbert--Schmidt estimate needs only two directional resolvent actions. Adjacent quadratic defects telescope with geometric factor $4/3$.

3.  **Small-noise exponent reduction: closed.** If the directional product grows like $\sigma^{-\gamma}$, the exact mesh threshold is [\[eq:general-p-threshold\]](#eq:general-p-threshold){reference-type="eqref" reference="eq:general-p-threshold"}. The previous $p>2$ theorem survives for every $\gamma\le1/2$ and, in particular, for every polylogarithmic loss.

4.  **Directional reduced-resolvent estimate: open.** The present paper does not prove a uniform or $\sigma^{-1/2}$ upper for the normalized directional gain. The global $L^2$ residue obstruction neither proves nor disproves that estimate.

5.  **Sharper $(n\sigma)^{-2}$ law: open.** Exact-Haar data strongly support it, but the available Gaussian Hilbert--Schmidt derivative envelope proves only the more conservative $n^{-2}\sigma^{-3}$ self-energy clock before directional gain.

The next useful theorem should therefore target one of two statements: $$\sup_{j\ge0}\mathcal L_{2^jn,\sigma}
 =O((\log(1/\sigma))^m)
 \label{eq:next-polylog-target}$$ for some fixed $m$, or at least $$\sup_{j\ge0}\mathcal L_{2^jn,\sigma}
 =O(\sigma^{-1/2}).
 \label{eq:next-half-power-target}$$ Possible tools include a reduced Grushin system built from the known left and right peripheral factors, a primal--dual enclosure of the two coupling ranges, or a mixed Banach/Hilbert norm that separates deterministic bulk transport from endpoint residues. A negative result with growth exponent $\gamma>1/2$ would also be decisive: it would show that the strict $p>2$ route needs a stronger mesh schedule or a different intrinsic subtraction.

The scope remains operator-theoretic. None of the results identifies a dynamical trace with primes or prime powers, constructs a self-adjoint Hilbert--Pólya operator, derives a $T\log T$ counting law, locates a Riemann zero, or proves the Riemann hypothesis.

# Data and code availability {#data-and-code-availability .unnumbered}

All source code, exact-Haar floating data, theorem certificates, tests, figures, hashes, and the manuscript are available at <https://github.com/maris205/prime_dynamics_theory/tree/main/papers/RH-48-intrinsic-riesz-identification>.
