---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-198-temporal-spectral-packet-alignment"
canonical_tex: "zeta_mvp0/papers/RH-198-temporal-spectral-packet-alignment/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-198-temporal-spectral-packet-alignment/main.pdf"
source_sha256: "14223c020b694df85a1e9db5395d85e9151ffa8421ad2fe160e0af71f73b2bbe"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Temporal--Spectral Packet Alignment A Graph Mechanism for the Physical Edge Quartet

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-198-temporal-spectral-packet-alignment>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-198-temporal-spectral-packet-alignment/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-198-temporal-spectral-packet-alignment/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-198-temporal-spectral-packet-alignment/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-198-temporal-spectral-packet-alignment/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-194 observes that late length-four temporal windows are close to the canonical physical edge-quartet spaces. This paper gives the exact graph coordinate behind that observation and audits its finite decay.

  For equal-dimensional subspaces $E$ and $T$ with orthonormal bases $Q_E,Q_T$ and invertible overlap $Q_E^*Q_T$, the space $T$ is the graph over $E$ of $$G=(I-Q_EQ_E^*)Q_T(Q_E^*Q_T)^{-1},$$ and $$\tan\theta_{\max}(E,T)=\left\lVert G\right\rVert,
   \qquad
   \sin\theta_{\max}(E,T)=\frac{\left\lVert G\right\rVert}{\sqrt{1+\left\lVert G\right\rVert^2}}.$$ For a Krylov synthesis split into selected and complementary spectral coordinates, this yields a conditional convergence theorem: decay of the complementary block relative to a uniformly invertible selected block forces the temporal range to the spectral range.

  In the physical data, all four right/left gap sequences have negative fitted log slopes and attain their minima at the latest accepted windows. Their descriptive per-step ratios lie in $[0.830,0.850]$ with fit $R^2\ge0.899$. Root errors decay faster, with ratios in $[0.695,0.739]$. The latest maximum subspace gap is below $0.051$.

  These rates summarize five or seven finite starts; they are not asymptotic constants. Uniform spectral-gap and selected-block inverse estimates remain the missing theoretical bridge to cross-scale transport.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Temporal--Spectral Packet Alignment\
  A Graph Mechanism for the Physical Edge Quartet
```

## Markdown 正文

# Two packets with different roles

The temporal packet is constructed without diagonalizing the physical operator. It is therefore dynamically meaningful but only approximately invariant. The canonical packet is built from Riesz projectors. It is exactly invariant but presently selected after seeing the spectrum.

The key local question is whether the first packet approaches the second in a controlled coordinate. Principal angles provide a basis-free answer; graph coordinates expose the mechanism that can later support estimates [@StewartSun1990].

# Exact graph representation

Let $E,T\subset\mathbb C^N$ have the same finite dimension $r$, with orthonormal frames $Q_E,Q_T$. Assume $$\label{eq:transverse}
 M=Q_E^*Q_T$$ is invertible. Set $\Pi_E=Q_EQ_E^*$ and $$\label{eq:graph-map}
 G=(I-\Pi_E)Q_TM^{-1}:\mathbb C^r\to E^\perp.$$

[\[thm:graph-angle\]]{#thm:graph-angle label="thm:graph-angle"} The subspace $T$ is the graph $$\label{eq:graph}
 T=\{Q_Ex+Gx:x\in\mathbb C^r\},$$ and $$\label{eq:angle-identities}
 \boxed{
 \tan\theta_{\max}(E,T)=\left\lVert G\right\rVert,
 \qquad
 \sin\theta_{\max}(E,T)=\frac{\left\lVert G\right\rVert}{\sqrt{1+\left\lVert G\right\rVert^2}}.
 }$$

For $y=Q_Ta$, put $x=Ma$. Then $\Pi_Ey=Q_Ex$ and $(I-\Pi_E)y=Gx$, proving the graph formula. The singular values of $M=Q_E^*Q_T$ are the principal cosines. In principal-vector coordinates the singular values of $G$ are the corresponding tangents, so the largest gives [\[eq:angle-identities\]](#eq:angle-identities){reference-type="eqref" reference="eq:angle-identities"}.

The formula is exact and remains valid for highly nonnormal dynamics because it concerns subspaces in the ambient Hilbert norm.

# Krylov spectral splitting

Assume for exposition that $A$ is diagonalizable and split its right spectral basis into a selected block $R_E$ and a complementary block $R_F$: $$\label{eq:diagonalization}
 A=[R_E,R_F]
 \begin{pmatrix}\Lambda_E&0\\0&\Lambda_F\end{pmatrix}
 [R_E,R_F]^{-1}.$$ For a matrix source $S$, a length-$r$ unnormalized window is $$\label{eq:krylov-window}
 J_t=[A^tS,A^{t+1}S,\ldots,A^{t+r-1}S],$$ with each matrix vectorized as one column.

In spectral coordinates write $$\label{eq:blocks}
 [R_E,R_F]^{-1}J_t=\begin{bmatrix}M_E(t)\\M_F(t)\end{bmatrix}.$$ The selected block contains eigenvalue powers and source coefficients; in the simple scalar-source model it is a diagonally weighted Vandermonde matrix.

[\[thm:conditional\]]{#thm:conditional label="thm:conditional"} Suppose $M_E(t)$ is invertible. Then the temporal range is a graph over the selected spectral range, and in compatible coordinates its graph map is bounded by $$\label{eq:graph-bound}
 \left\lVert G_t\right\rVert
 \le C_R\left\lVert M_F(t)\right\rVert\left\lVert M_E(t)^{-1}\right\rVert,$$ where $C_R$ depends only on the conditioning of the spectral coordinate map. In particular, if $$\label{eq:decay-hypothesis}
 \left\lVert M_F(t)\right\rVert\left\lVert M_E(t)^{-1}\right\rVert\le Cq^t,
 \qquad 0<q<1,$$ then the maximum subspace angle decays at least geometrically.

Eliminate selected coordinates with $M_E(t)^{-1}$. The complementary graph coefficient is $M_F(t)M_E(t)^{-1}$ before mapping back through the spectral basis. Norm equivalence contributes $C_R$. Apply Theorem [\[thm:graph-angle\]](#thm:graph-angle){reference-type="ref" reference="thm:graph-angle"}.

For nonnormal matrices, $C_R$ and the selected-block inverse may be large. The theorem isolates exactly the two missing uniform estimates: spectral separation and a nondegenerate source/Vandermonde block.

# Physical alignment sequences

The frozen RH-194 data give five accepted starts on the left and seven on the right [@WangRH194]. For each start we use the maximum principal sine between the temporal and canonical right spaces and, separately, the left spaces.

The log-linear descriptive fits are:

  side    space     per-step ratio      $R^2$   initial $\to$ final
  ------- ------- ---------------- ---------- ---------------------
  left    right           $0.8503$   $0.9543$     $0.0977\to0.0505$
  left    left            $0.8317$   $0.9519$     $0.0878\to0.0428$
  right   right           $0.8396$   $0.8993$     $0.0901\to0.0349$
  right   left            $0.8300$   $0.9783$     $0.1133\to0.0385$

All four slopes are negative and every final value is the minimum of its sequence. Two sequences have small local reversals, so monotonicity is not claimed at every step.

# Root and invariant errors

For each window define $$\label{eq:root-error}
 e_\lambda(t)=\max_j|\kappa_j(t)-\lambda_j|.$$ The fitted per-step ratios are $0.7385$ on the left and $0.6948$ on the right. The errors fall from $9.14\times10^{-4}$ to $2.72\times10^{-4}$ on the left and from $1.27\times10^{-3}$ to $1.43\times10^{-4}$ on the right.

Power-trace errors through order eight also decrease to below $7.7\times10^{-4}$ on the latest left window and $4.0\times10^{-4}$ on the latest right window. RH-199 separates this similarity-invariant convergence from the coordinate conditioning.

# Condition convergence as a second coordinate

RH-197 shows that the temporal condition numbers at the latest windows are within approximately one percent of the exact canonical optima [@WangRH197]. This is not implied by small principal angle alone when the canonical pairing is poorly conditioned. Its simultaneous occurrence is therefore an independent consistency check.

The combined finite picture is: $$\label{eq:combined-picture}
 \begin{gathered}
 \text{right and left subspace gaps decrease},\\
 \text{root, determinant, and trace errors decrease},\\
 \text{cross-angle condition approaches the canonical value}.
 \end{gathered}$$ No single diagnostic is carrying the conclusion.

# Why the fitted ratio is not a theorem

There are only five or seven starts at one scale. The normalized orbit eventually favors the outermost modulus pair and can lose four-dimensional conditioning; therefore a fitted ratio cannot be extrapolated indefinitely. Moreover the physical operator itself changes with $\sigma$.

An all-level theorem needs:

1.  a quartet separated from the complementary spectrum in a norm suitable for the nonnormal operator;

2.  lower bounds for source activation and the selected Vandermonde block;

3.  a window-selection rule that stays before late-time rank collapse;

4.  compatibility between left and right physical channels.

None follows from a short log-linear fit.

# Updated frontier

The temporal construction now has a credible exact endpoint and a conditional convergence mechanism. The next finite task is to transfer determinant and trace data, where large balanced frame norms cancel under similarity. Beyond that lies the genuinely hard step: prove a cross-scale selection and transport theorem for the quartet.

The work remains inside Gate A. It does not identify zeta zeros or claim a Hilbert--Pólya operator.
