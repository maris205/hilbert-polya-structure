---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-202-adjacent-edge-quartet-transport"
canonical_tex: "zeta_mvp0/papers/RH-202-adjacent-edge-quartet-transport/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-202-adjacent-edge-quartet-transport/main.pdf"
source_sha256: "5912e2d2bf6a1f354c93ed438267ea7fdea6d288e0d044e3ac91d684b21b0326"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Adjacent-Scale Transport of the Physical Edge Quartet A Finite Obstruction to the Naive Haar Shell Map

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-202-adjacent-edge-quartet-transport>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-202-adjacent-edge-quartet-transport/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-202-adjacent-edge-quartet-transport/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-202-adjacent-edge-quartet-transport/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-202-adjacent-edge-quartet-transport/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The outer four source-observable eigenmodes found in RH-200 form a canonical finite packet at each of three noise scales. This paper performs the first direct adjacent-level transport test. The packets at $\sigma=0.04,0.02,0.01$ are put in common coordinates by the dyadic Haar embedding. We compare right and left invariant spaces, oblique Riesz projectors, source and observation channel states, residues, eigenvalues, and quartic characteristic coefficients.

  The result is negative for the literal shell map. Across four adjacent scale/channel cases the largest right and left principal sines reach $0.82175$ and $0.82388$; the largest relative oblique-projector defect is $2.29068$. The quartet-restricted intertwining defect reaches $0.65573$, and one relative residue displacement reaches $8.18374$. Even the finer $0.02\to0.01$ step retains order-one projector defects.

  The spectral correspondence itself does not disappear: every packet remains conjugation closed and admits a unique minimum-cost matching. Thus the finite quartet is a valid local edge diagnostic but is not transported by the unmodified coarse-cell embedding. A renormalized map or a scalar divisor formulation is required. All results are finite floating audits; no all-level shell, Fredholm determinant, Hilbert--Pólya operator, or RH conclusion is asserted.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Adjacent-Scale Transport of the Physical Edge Quartet\
  A Finite Obstruction to the Naive Haar Shell Map
```

## Markdown 正文

# Problem and inherited packet

RH-192--RH-201 corrected the state type of the temporal construction and isolated a genuine source--observation packet [@WangRH201]. At each audited scale and on both physical channels, the four largest-modulus modes are two nonreal conjugate pairs, all with nonzero transfer residue. The minimum radial gap after the fourth mode is $0.05949$ [@WangRH200].

Local selection is not yet Gate A. A spectral block can contribute to an all-level determinant only if its identity is coherent under refinement. The first candidate map is the isometric Haar embedding $$\label{eq:haar}
 J_ne_j=2^{-1/2}(e_{2j}+e_{2j+1}),
 \qquad J_n^*J_n=I.$$ When matrix channel states double in both dimensions we also use a column embedding $K_m$ and transport $X$ as $J_nXK_m^*$.

# Objects transported

Let $A_c$ and $A_f$ denote adjacent coarse and fine physical operators. Their outer quartets have right and left frames $V_c,W_c$ and $V_f,W_f$, normalized by $$\label{eq:biorthogonal}
 W_c^*V_c=W_f^*V_f=I_4.$$ The oblique packet projectors are $$\label{eq:projectors}
 P_c=V_cW_c^*,\qquad P_f=V_fW_f^*.$$

The right-space transport angle is determined by the singular values of $Q_f^*JQ_c$, where $Q_c,Q_f$ are orthonormal bases. If $s_4$ is the smallest singular value, we record $$\label{eq:angle}
 \sin\theta_{\max}=\sqrt{1-s_4^2}.$$ Left spaces are treated independently because the operators are nonnormal.

For every simple mode $\lambda$, with projector $P_\lambda$, source $S$, and observation $O$, the physical channel states are $$\label{eq:states}
 X_\lambda=P_\lambda S,
 \qquad Y_\lambda=P_\lambda^*O^*,
 \qquad r_\lambda=\langle Y_\lambda,X_\lambda\rangle_F.$$ The comparison therefore tests both the base eigenspace and the actual source--observation state.

# Predeclared correspondence

At each endpoint we select the four largest-modulus eigenvalues before any cross-level matching. The minimum-total-distance permutation then matches the two finite sets. This permutation is used simultaneously for eigenvalues, right/left modes, channel states, and residues. It is not used to alter the Haar map.

For the monic quartet polynomial $$\label{eq:quartic}
 D_\sigma(z)=\prod_{j=1}^4(z-\lambda_{\sigma,j}),$$ we compare the complete coefficient vector. This scalar comparison is basis invariant and will become important after the state-space obstruction.

# Four adjacent-level cases

The principal-angle and projector data are:

  step            side      right sine   left sine   $\left\lVert P_f-JP_cJ^*\right\rVert_F/\left\lVert P_f\right\rVert_F$   polynomial error
  --------------- ------- ------------ ----------- ----------------------------------------------------------------------- ------------------
  $0.04\to0.02$   left        $0.5766$    $0.7654$                                                                $2.2907$           $0.2402$
  $0.04\to0.02$   right       $0.7669$    $0.6116$                                                                $2.2361$           $0.2420$
  $0.02\to0.01$   left        $0.8217$    $0.6206$                                                                $1.0154$           $0.3167$
  $0.02\to0.01$   right       $0.6267$    $0.8239$                                                                $1.0077$           $0.3096$

None of these values is a small perturbative transport parameter. In particular, refining the grid does not make the naive projector defect small on the two available transitions.

The operator and channel defects tell the same story. The quartet-restricted intertwining defects range from $0.23623$ to $0.65573$. Source transport defects lie between $0.78134$ and $0.81991$. Observation defects are near $2^{-1/2}$, reflecting both refinement and the changing physical observation map.

# Mode and residue movement

The largest eigenvalue displacement is $0.38160$ on the first transition and $0.13643$ on the second. Hence a recognizable spectral branch survives, but its endpoint is moving.

Residues are less stable. On the left $0.04\to0.02$ transition, one matched mode changes from approximately $$-0.09768-0.11776i
 \quad\text{to}\quad
 -0.00593-0.01569i.$$ Its relative displacement, normalized by the fine residue, is $8.18374$. The minimum cosine between transported and fine source states over all sixteen mode records is $0.48096$; the corresponding observation minimum is $0.60264$.

These are gauge-invariant channel quantities. Rephasing an eigenvector cannot remove the residue discrepancy.

# Finite obstruction statement

[\[prop:obstruction\]]{#prop:obstruction label="prop:obstruction"} For the six physical endpoint packets and four adjacent cases audited here, the rule $$(P_c,X_c,Y_c)\longmapsto
 (JP_cJ^*,JX_cK^*,JY_cK^*)$$ does not provide a small-defect transport of the outer quartet. In particular, the maximum subspace sine exceeds $0.82$ and every relative oblique-projector defect exceeds $1$.

The proposition is a statement about these matrices and this predeclared map. It is not an all-level theorem and does not rule out a scale-dependent renormalization, a different cluster, or a scalar spectral construction.

# What survives the negative result

Three facts remain useful:

1.  the edge quartet is isolated and source observable at every endpoint;

2.  the matched eigenvalues retain a common conjugate-branch geometry;

3.  the monic quartic is meaningful without choosing eigenvector gauges.

Thus the failure is specifically one of raw state transport. It does not invalidate the local Riesz packet or its spectral divisor.

# Audit protocol and dimensional ledger

The left operator dimensions at $\sigma=0.04,0.02,0.01$ are respectively $128,256,512$; the right dimensions are $64,128,256$. Source column counts are $64,128,256$ on both sides. Thus every adjacent comparison doubles both the base-state resolution and the source-column resolution. The row and column Haar maps are constructed independently with the normalization [\[eq:haar\]](#eq:haar){reference-type="eqref" reference="eq:haar"}.

For reproducibility, the calculation uses the following fixed order:

1.  construct each physical model directly from its declared $\sigma$;

2.  compute the complete finite eigendecomposition;

3.  select four indices by modulus before looking at another level;

4.  biorthogonalize the selected right/left frames as one block;

5.  solve one minimum-cost eigenvalue assignment;

6.  reuse that assignment for every state, residue, and polynomial metric.

No Procrustes correction is applied in RH-202. This is essential: allowing an endpoint-fitted unitary would answer a different question, developed only in RH-205.

The order-one defects are far above eigensolver residual and conjugation errors, but this does not make them interval statements. Their role is to reject the naive map as the next perturbative target, not to certify a sharp lower bound for an exact continuum operator.

# Next mathematical wall

The resolvent identity should be used to separate the causes of transport failure. If $E=A_fJ-JA_c$, then on a common resolvent set one expects $$R_f(z)J-JR_c(z)=R_f(z)ER_c(z).$$ RH-203 develops this identity, integrates it over Riesz contours, and separates projector defects from source defects. Later layers must decide whether to renormalize the state map or move first to the scalar divisor.

# Claim boundary

The eigendecompositions and all norms in this paper are double-precision finite calculations. No interval enclosure of the input matrices, resolvents, contours, or projectors is claimed. The negative finite result is robust as a diagnostic because the measured defects are order one, but it is not promoted to an analytic zero-noise theorem. Gate A remains open; Gates B--E are untouched.
