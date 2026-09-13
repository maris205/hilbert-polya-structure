---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-196-canonical-biorthogonal-spectral-packet"
canonical_tex: "zeta_mvp0/papers/RH-196-canonical-biorthogonal-spectral-packet/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-196-canonical-biorthogonal-spectral-packet/main.pdf"
source_sha256: "c912264b01c383507c43176799ecbffd769a106dc565a65ddfcf945ce30c9849"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Canonical Biorthogonal Spectral Packet Balanced Coordinates on Source--Observation Riesz Channels

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-196-canonical-biorthogonal-spectral-packet>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-196-canonical-biorthogonal-spectral-packet/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-196-canonical-biorthogonal-spectral-packet/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-196-canonical-biorthogonal-spectral-packet/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-196-canonical-biorthogonal-spectral-packet/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-195 associates each selected simple physical eigenvalue with exact right and left matrix states $X_i=P_iS$ and $Y_i=P_i^*O^*$ whose cross pairing is diagonal with entries equal to transfer residues. This paper constructs optimal packet coordinates on the resulting right and left spectral spaces.

  Let $E_R=\operatorname{span}\{X_i\}$ and $E_L=\operatorname{span}\{Y_i\}$, assume every residue is nonzero, and let $Q_R,Q_L$ be orthonormal bases. If $Q_L^*Q_R=U\Sigma V^*$, define $$V_c=Q_RV\Sigma^{-1/2},
   \qquad
   W_c=Q_LU\Sigma^{-1/2}.$$ Then $W_c^*V_c=I$, both frame norms equal $\sigma_{\min}^{-1/2}$, and their norm product $\sigma_{\min}^{-1}$ is optimal among all biorthogonal coordinates on the same two spaces.

  Because $E_R$ and $E_L$ are exact invariant spaces, $$\mathcal L_AV_c=V_cK_c,
   \qquad
   \mathcal L_A^*W_c=W_cK_c^*.$$ Both directed residuals vanish, $K_c$ is similar to the selected physical spectral restriction, and its determinant and every power trace are exact. A 140-case complex nonnormal audit verifies all identities with zero failures.

  The packet is canonical relative to the chosen Riesz contours, source, and observation. It removes the complement self-energy inside that selected channel. Intrinsic contour selection, interval validation, and uniform cross-level transversality remain open.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  A Canonical Biorthogonal Spectral Packet\
  Balanced Coordinates on Source--Observation Riesz Channels
```

## Markdown 正文

# From residue coordinates to balanced coordinates

For pairwise disjoint simple eigenvalues, RH-195 gives right and left channel states $$\label{eq:channel-states}
 X_i=P_iS,
 \qquad Y_i=P_i^*O^*,$$ with $$\label{eq:residue-cross}
 \langle Y_i,X_j\rangle_F=\delta_{ij}r_i.$$ If $r_i\ne0$, the direct normalization $V_i=X_i$, $W_i=Y_i/\overline{r_i}$ is biorthogonal. It preserves mode labels and diagonalizes the compressed operator, but it need not balance coordinate norms [@WangRH195]. The cross-Gram balancing used below is the exact spectral specialization of the temporal construction in RH-184 [@WangRH184].

The geometry depends only on the two subspaces $$\label{eq:spaces}
 E_R=\operatorname{span}\{X_1,\ldots,X_r\},
 \qquad
 E_L=\operatorname{span}\{Y_1,\ldots,Y_r\}.$$ Nonzero residues imply that the pairing between them is nondegenerate.

# Cross-Gram geometry

Choose Frobenius-orthonormal bases $Q_R,Q_L\in\mathbb C^{N\times r}$ for the vectorized spaces and form $$\label{eq:cross-gram}
 H=Q_L^*Q_R.$$ The singular values of $H$ are the cosines of the principal angles between $E_L$ and $E_R$. Transversality is equivalent to $\sigma_{\min}(H)>0$.

Let $$\label{eq:svd}
 H=U\Sigma V^*.$$

[\[thm:balanced\]]{#thm:balanced label="thm:balanced"} Define $$\label{eq:balanced-frames}
 V_c=Q_RV\Sigma^{-1/2},
 \qquad
 W_c=Q_LU\Sigma^{-1/2}.$$ Then $$\label{eq:biorthogonal}
 W_c^*V_c=I,$$ and $$\label{eq:frame-norms}
 \left\lVert V_c\right\rVert=\left\lVert W_c\right\rVert=\sigma_{\min}(H)^{-1/2}.$$

Insert the singular-value decomposition into $W_c^*V_c$. Since $Q_R,Q_L,U,V$ are isometries, the operator norms of the frames equal the largest diagonal entry of $\Sigma^{-1/2}$.

# Optimality

Any frames $V,W$ spanning $E_R,E_L$ and satisfying $W^*V=I$ define the same oblique projector $\Pi=VW^*$ from the ambient space onto $E_R$ along $E_L^\perp$. Its norm is $$\label{eq:projector-norm}
 \left\lVert\Pi\right\rVert=\sigma_{\min}(H)^{-1}.$$

[\[thm:optimal\]]{#thm:optimal label="thm:optimal"} Every biorthogonal realization on $(E_R,E_L)$ obeys $$\label{eq:product-lower}
 \left\lVert V\right\rVert\left\lVert W\right\rVert\ge\sigma_{\min}(H)^{-1}.$$ The balanced frames attain equality. They also minimize $\max(\left\lVert V\right\rVert,\left\lVert W\right\rVert)$, whose optimal value is $\sigma_{\min}(H)^{-1/2}$.

Submultiplicativity gives $\left\lVert VW^*\right\rVert\le\left\lVert V\right\rVert\left\lVert W\right\rVert$, while the left side equals $\sigma_{\min}^{-1}$. The balanced norms attain the lower bound. For any positive numbers with product at least $c$, their maximum is at least $\sqrt c$; scalar gauge balancing attains this value.

The potentially large conditioning is intrinsic to the source-observation subspaces. No alternative basis can remove it.

# Exact two-sided invariance

The right space is invariant under $\mathcal L_A:X\mapsto AX$, and the left space is invariant under $\mathcal L_A^*$. Hence there are matrices $K_R,K_L$ with $$\label{eq:invariance}
 \mathcal L_AV_c=V_cK_R,
 \qquad
 \mathcal L_A^*W_c=W_cK_L.$$

[\[thm:exact-compression\]]{#thm:exact-compression label="thm:exact-compression"} With $$\label{eq:compressed}
 K_c=W_c^*\mathcal L_AV_c,$$ one has $$\label{eq:two-sided}
 \boxed{
 \mathcal L_AV_c=V_cK_c,
 \qquad
 \mathcal L_A^*W_c=W_cK_c^*.
 }$$ Thus both directed Ritz residuals vanish exactly.

The first invariant relation and $W_c^*V_c=I$ imply $K_R=K_c$. Taking the adjoint of the left invariant relation gives $W_c^*\mathcal L_A=K_L^*W_c^*$. Multiplying by $V_c$ shows $K_L^*=K_c$, hence the second identity.

This is the exact endpoint that the temporal bi-Krylov packet approximates. In these coordinates the packet-to-complement couplings are zero because the selected subspaces are reducing in the biorthogonal sense.

# Spectrum, determinant, and traces

In the residue-labeled frame, the compressed matrix is $\Lambda=\operatorname{diag}(\lambda_1,\ldots,\lambda_r)$. Every other biorthogonal frame on the same spaces differs by a gauge $V\mapsto VG$, $W\mapsto W(G^{-1})^*$, so $$\label{eq:gauge-similarity}
 K\mapsto G^{-1}KG.$$

[\[cor:ledger\]]{#cor:ledger label="cor:ledger"} For the balanced packet, $$\begin{aligned}
 \det(zI-K_c)&=\prod_{j=1}^r(z-\lambda_j),\label{eq:determinant}\\
 \operatorname{tr}K_c^q&=\sum_{j=1}^r\lambda_j^q
 \quad(q\ge1).\label{eq:traces}\end{aligned}$$

These are exact finite channel identities. They are not the determinant or trace of the complete Frobenius operator, whose multiplicities remain multiplied by $m$.

# Canonicity and its limits

The spaces $E_R,E_L$ are determined by $(A,S,O)$ and the selected Riesz contours. The balanced packet is unique up to unitary transformations within repeated singular-value blocks and harmless phase conventions. Its determinant and traces are fully invariant under this residual gauge.

This is a useful but conditional canonicity. If the contours were selected by first inspecting the target eigenvalues, the construction has not yet explained why those modes are dynamically privileged. Gate A needs an a priori selection principle, for example an edge-gap, source-history, or renormalization rule that survives refinement.

# Identity audit

The numerical audit uses 140 complex nonnormal systems with base dimensions 4--10 and source widths 1--4. Four spectral channels of largest modulus are formed from exact computed left/right eigendata. The code balances their right and left matrix-state spaces and verifies:

1.  equality of balanced frame norms;

2.  biorthogonality;

3.  zero right and left invariant residuals;

4.  equality of compressed and selected spectra;

5.  Newton power-trace identities through power eight.

All cases pass the declared $10^{-8}$ tolerance.

# Position in the route

The local route now contains an exact endpoint: $$\text{temporal packet}
 \longrightarrow
 \text{matched Riesz channels}
 \longrightarrow
 \text{balanced exact packet}.$$ The first arrow is finite and numerical; the second is exact once the contours are fixed. RH-197 measures the physical residues and the intrinsic cross-angle condition of the matched quartet. RH-198 then quantifies how the temporal packet approaches this exact endpoint.

No statement here constructs a self-adjoint operator, a Hilbert--Pólya spectrum, a prime-power trace formula, or a zeta divisor. The work remains inside the physical spectral interface portion of Gate A.
