---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-197-physical-residue-transversality-audit"
canonical_tex: "zeta_mvp0/papers/RH-197-physical-residue-transversality-audit/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-197-physical-residue-transversality-audit/main.pdf"
source_sha256: "08fc81c6bd0caf39a6fe4b78c5e6101543108f5d4e7c9f6d8c4f1e2283ef1f58"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Physical Residues and Spectral Transversality Conditioning of the Canonical Edge Quartet

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-197-physical-residue-transversality-audit>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-197-physical-residue-transversality-audit/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-197-physical-residue-transversality-audit/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-197-physical-residue-transversality-audit/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-197-physical-residue-transversality-audit/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-194 identifies one physical edge quartet on each side of the $\sigma=0.01$ model, and RH-196 proves that the corresponding source--observation Riesz channels admit an exact optimally balanced packet. This paper measures the physical geometry of those packets.

  All eight unique modes have nonzero transfer residue; the minimum residue modulus is $1.107\times10^{-2}$. The canonical minimum cross singular value is $5.207\times10^{-3}$ on the left and $1.052\times10^{-3}$ on the right. Therefore the optimal biorthogonal frame norm products are respectively $192.05$ and $950.26$. These are finite transverse packets, but they are not well conditioned.

  The large condition is not merely a defective temporal coordinate choice. At the latest accepted windows, the temporal oblique condition numbers are within two percent of the canonical spectral optima. Simultaneously the temporal-to-spectral principal-angle gaps are below $0.051$ on all four right/left comparisons. Thus the late clock is converging to both the physical subspaces and their intrinsic oblique geometry.

  This is a finite positive result with a sharp warning: no all-level residue or cross-angle lower bound is known. Any later determinant route should seek gauge-invariant cancellation of the large condition rather than claim uniformly benign coordinates.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Physical Residues and Spectral Transversality\
  Conditioning of the Canonical Edge Quartet
```

## Markdown 正文

# Data and quantities

The input is the frozen RH-194 eigendecomposition and root matching [@WangRH194]. For each side there are four simple physical modes with source and observation states $$\label{eq:states}
 X_i=P_iS,
 \qquad Y_i=P_i^*O^*,$$ and transfer residues $$\label{eq:residues}
 r_i=\langle Y_i,X_i\rangle_F.$$

Let $Q_R,Q_L$ be orthonormal bases of the two four-dimensional spans. The cross singular values are those of $$\label{eq:cross}
 H=Q_L^*Q_R.$$ Write $$\label{eq:gamma}
 \gamma=\sigma_{\min}(H).$$ By RH-196, the optimal product of norms of biorthogonal frames on these spaces is exactly $$\label{eq:condition}
 \chi_{\rm can}=\gamma^{-1},$$ and each balanced frame has norm $\gamma^{-1/2}$ [@WangRH196].

# Residue audit

The unique-mode residue ranges are:

  side      minimum $|r_i|$   median $|r_i|$   maximum $|r_i|$
  ------- ----------------- ---------------- -----------------
  left            $0.02610$        $0.04562$         $0.06514$
  right           $0.01107$        $0.04532$         $0.07956$

All residues are well separated from floating underflow and from the $10^{-12}$ visibility threshold. Thus no selected pole is canceled in the scalar source-observation transfer function at this anchor.

Residue magnitude alone is not a coordinate-free angle. Define the normalized mode overlap $$\label{eq:mode-overlap}
 \eta_i=\frac{|r_i|}{\left\lVert X_i\right\rVert_F\left\lVert Y_i\right\rVert_F}.$$ The minimum is $5.458\times10^{-3}$ on the left and $1.125\times10^{-3}$ on the right. Its reciprocal is the optimal norm product for that single labeled mode pair. The complete four-space condition also reflects nonorthogonality among modes on each side.

# Canonical four-space condition

The cross singular values are:

  side      $\sigma_1$   $\sigma_2$   $\sigma_3$   $\sigma_4$
  ------- ------------ ------------ ------------ ------------
  left      $0.006738$   $0.006565$   $0.005549$   $0.005207$
  right     $0.002516$   $0.002104$   $0.001158$   $0.001052$

[\[prop:transverse\]]{#prop:transverse label="prop:transverse"} Both canonical quartet pairings are nonsingular. Their optimal biorthogonal norm products and balanced frame norms are

  side      $\chi_{\rm can}=1/\gamma$   $\sqrt{\chi_{\rm can}}$
  ------- --------------------------- -------------------------
  left                     $192.0508$                 $13.8582$
  right                    $950.2581$                 $30.8263$

This proves finite transversality and rejects a stronger informal hope that the exact spectral packet would be nearly orthogonal. The right channel is intrinsically close to a tangential source-observation pairing.

# Nonnormality of the base modes

For normalized left/right eigenvectors $w_i^*v_i=1$, the base spectral projector norm is $$\label{eq:projector-norm}
 \left\lVert P_i\right\rVert=\left\lVert v_i\right\rVert\left\lVert w_i\right\rVert.$$ The selected values range up to $17.54$ on the left and $17.69$ on the right. Thus the edge quartet is moderately nonnormal even before the source and observation are applied.

The much larger packet condition, especially on the right, comes from the combined geometry of spectral nonnormality, source activation, observation activation, and near-tangency of the two four-spaces. It cannot be inferred from eigenvalue spacing alone.

# Comparison with temporal conditioning

Let $\chi_t$ be the RH-185 oblique condition number of an accepted temporal window. Compare it with the exact spectral optimum through $$\label{eq:ratio}
 R_t=\frac{\chi_t}{\chi_{\rm can}}.$$ The spaces differ, so $R_t$ can lie below one; the canonical optimum is an optimum only for the canonical pair of spaces.

At the latest windows the values are approximately

  side      start    $\chi_t$      $R_t$
  ------- ------- ----------- ----------
  left         18   $193.974$   $1.0100$
  right        18   $956.830$   $1.0069$

Both relative discrepancies are below two percent.

[\[prop:geometry-convergence\]]{#prop:geometry-convergence label="prop:geometry-convergence"} At the latest accepted windows, temporal subspace gaps are below $0.051$ and temporal oblique conditions differ from the canonical spectral optima by less than two percent on both sides.

The proposition is a finite conjunction, not an asymptotic theorem. It shows that two independent diagnostics---subspace angle and cross-angle condition---point to the same spectral endpoint.

# Why clipping is not the response

RH-187 studies singular-value clipping of the temporal cross Gram and proves the exact defect/conditioning tradeoff [@WangRH187]. Clipping the small singular values improves coordinate norms only by sacrificing exact biorthogonality, and no audited clipping level closes the old coarse gate.

The present audit explains why. Small cross singular values persist in the exact canonical spectral spaces. They are not solely noisy temporal directions that should be deleted. A later successful route should instead use quantities invariant under balanced gauge, such as eigenvalues, determinants, traces, and self-energy products in correctly reduced spaces.

# What would be needed uniformly

A transportable all-level packet would need estimates of the form $$\label{eq:uniform-needs}
 \inf_k\min_i|r_{k,i}|>0,
 \qquad
 \inf_k\sigma_{\min}(Q_{L,k}^*Q_{R,k})>0,$$ or a renormalized replacement in which their decay is explicitly canceled. The present single-anchor numbers do not support either conclusion.

Indeed, a condition near $950$ leaves little room for untracked operator perturbations. Interval validation at one level is feasible, but a direct uniform perturbation argument may be too expensive without additional structure.

# Next use of the canonical packet

RH-198 will audit the window-by-window approach to the canonical spaces and fit only descriptive finite decay diagnostics. RH-199 will then compare the temporal determinant and power traces with their exact four-mode values. These quantities may converge despite large frame norms because they are similarity invariant.

The route remains inside Gate A. Finite nonzero residues do not construct a self-adjoint operator, prove a $T\log T$ law, recover prime-power weights, or identify a zeta divisor.
