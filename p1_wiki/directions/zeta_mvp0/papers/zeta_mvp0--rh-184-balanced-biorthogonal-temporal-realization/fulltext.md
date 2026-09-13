---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-184-balanced-biorthogonal-temporal-realization"
canonical_tex: "zeta_mvp0/papers/RH-184-balanced-biorthogonal-temporal-realization/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-184-balanced-biorthogonal-temporal-realization/main.pdf"
source_sha256: "d8fda0e9c7f1cc90dd6194e96b6112447b6344306b000582b17f7c4eae364975"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Balanced Biorthogonal Temporal Realization Canonical Cross-Gram Frames, Optimal Oblique Conditioning, and Gauge-Covariant Ritz Data

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-184-balanced-biorthogonal-temporal-realization>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-184-balanced-biorthogonal-temporal-realization/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-184-balanced-biorthogonal-temporal-realization/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-184-balanced-biorthogonal-temporal-realization/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-184-balanced-biorthogonal-temporal-realization/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The orthogonal temporal clock of RH-182--183 fails because one range must simultaneously support forward and adjoint dynamics. For a nonnormal operator this is unnecessarily restrictive. This paper gives a canonical finite replacement based on distinct right and left temporal subspaces.

  Let $Q_R,Q_L:\mathbb C^r\to\mathcal H$ be orthonormal frames and let $H=Q_L^*Q_R$. If the subspaces are transverse, $H$ is invertible. Writing $H=U\Sigma V^*$, define $$V_R=Q_RV\Sigma^{-1/2},
   \qquad
   W_L=Q_LU\Sigma^{-1/2}.$$ Then $W_L^*V_R=I$. The two frame norms are equal to $\sigma_{\min}(H)^{-1/2}$, their product and the norm of the oblique projector $P=V_RW_L^*$ equal $\sigma_{\min}(H)^{-1}$, and this norm product is minimal among all biorthogonal frames spanning the same two subspaces. The construction is canonical up to unitary choices inside repeated singular subspaces. Under an arbitrary invertible packet gauge, the compressed operator transforms by similarity and its spectrum is unchanged.

  The right and left residuals are $(I-P)AV_R$ and $(I-P^*)A^*W_L$. They are type-correct directed couplings, not defects of one orthogonal reducing subspace. A 120-case complex random audit verifies biorthogonality, projector idempotence, the optimal norm formula, residual block identities, and gauge covariance with zero failures.

  This closes the finite algebraic realization needed for a source/observation bi-Krylov clock. Physical transversality, conditioning, contour resolvents, and all-level transport remain open. No Riesz, Gate A, Hilbert--Polya, or RH claim is made.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Balanced Biorthogonal Temporal Realization\
  Canonical Cross-Gram Frames, Optimal Oblique Conditioning, and Gauge-Covariant Ritz Data
```

## Markdown 正文

# From orthogonal reduction to Petrov--Galerkin reduction

RH-183 proves that no phase or scalar wrap repairs the declared orthogonal temporal spans [@WangRH183]. The dominant physical obstruction is in the adjoint direction. This is familiar in nonnormal spectral approximation: right and left invariant information naturally lives in different spaces [@StewartSun1990; @Kato1995].

The physical models already contain two canonical seeds: $$\label{eq:seeds}
 \text{source }S,
 \qquad
 \text{observation adjoint }O^*.$$ Their forward $A$-orbit and forward $A^*$-orbit generate right and left temporal subspaces. Before applying this physically, the finite geometry of two arbitrary subspaces must be fixed without a fitted target basis.

# Two subspaces and the cross Gram

Let $\mathcal R,\mathcal L\subset\mathcal H$ have equal finite dimension $r$. Choose orthonormal frames $$\label{eq:orthogonal-frames}
 Q_R,Q_L:\mathbb C^r\longrightarrow\mathcal H,
 \qquad Q_R^*Q_R=Q_L^*Q_L=I_r.$$ Define the cross Gram $$\label{eq:cross-gram}
 H=Q_L^*Q_R.$$ Its singular values are the cosines of the principal angles between the two subspaces. In particular, $$\label{eq:transverse}
 H\text{ invertible}
 \quad\Longleftrightarrow\quad
 \mathcal R\cap\mathcal L^\perp=\{0\}.$$ This is the transversality condition for a projection onto $\mathcal R$ along $\mathcal L^\perp$.

Write a singular-value decomposition $$\label{eq:svd}
 H=U\Sigma V^*,
 \qquad
 \Sigma=\operatorname{diag}(\sigma_1,\ldots,\sigma_r),
 \quad \sigma_1\ge\cdots\ge\sigma_r>0.$$

# Canonical balanced frames

[\[thm:balanced\]]{#thm:balanced label="thm:balanced"} Define $$\label{eq:balanced-frames}
 V_R=Q_RV\Sigma^{-1/2},
 \qquad
 W_L=Q_LU\Sigma^{-1/2}.$$ Then $$\label{eq:biorthogonality}
 W_L^*V_R=I_r.$$ Moreover, $$\label{eq:balanced-norms}
 \left\lVert V_R\right\rVert=\left\lVert W_L\right\rVert=\sigma_r^{-1/2}.$$

Using [\[eq:svd\]](#eq:svd){reference-type="eqref" reference="eq:svd"}, $$W_L^*V_R
 =\Sigma^{-1/2}U^*Q_L^*Q_RV\Sigma^{-1/2}
 =\Sigma^{-1/2}U^*U\Sigma V^*V\Sigma^{-1/2}=I.$$ Because $Q_RV$ and $Q_LU$ are isometries, both frame norms equal the largest diagonal entry of $\Sigma^{-1/2}$, namely $\sigma_r^{-1/2}$.

The frame pair is balanced in the literal sense that right and left pay the same conditioning price. Repeated singular values permit unitary rotations inside the repeated block, but the represented subspaces, oblique projector, and singular-value ledger are unchanged.

# Optimality and the oblique projector

Let $$\label{eq:projector}
 P=V_RW_L^*.$$ Then $P^2=P$, $\operatorname{Ran}P=\mathcal R$, and $\ker P=\mathcal L^\perp$.

[\[thm:optimal\]]{#thm:optimal label="thm:optimal"} Among all pairs $\widetilde V=Q_RA$ and $\widetilde W=Q_LB$ satisfying $\widetilde W^*\widetilde V=I$, one has $$\label{eq:lower-product}
 \left\lVert\widetilde V\right\rVert\left\lVert\widetilde W\right\rVert
 \ge \left\lVert H^{-1}\right\rVert=\sigma_r^{-1}.$$ The balanced pair attains equality. Furthermore, $$\label{eq:projector-norm}
 \left\lVert P\right\rVert=\sigma_r^{-1}.$$

Biorthogonality gives $B^*HA=I$, hence $H^{-1}=AB^*$. Therefore $$\left\lVert H^{-1}\right\rVert\le\left\lVert A\right\rVert\left\lVert B\right\rVert
 =\left\lVert\widetilde V\right\rVert\left\lVert\widetilde W\right\rVert,$$ because $Q_R$ and $Q_L$ are isometries. The balanced norms in [\[eq:balanced-norms\]](#eq:balanced-norms){reference-type="eqref" reference="eq:balanced-norms"} have product $\sigma_r^{-1}$.

For the projector, $$P=Q_RV\Sigma^{-1}U^*Q_L^*.$$ The exterior factors are partial isometries on the relevant ranges, so $\left\lVert P\right\rVert=\left\lVert\Sigma^{-1}\right\rVert=\sigma_r^{-1}$.

Thus the smallest cross singular value is not a removable numerical detail. It is the exact best possible conditioning of this two-subspace realization.

There is also a coordinate-free formula. Since $H^{-1}=V\Sigma^{-1}U^*$, $$\label{eq:coordinate-free-projector}
 P=Q_RH^{-1}Q_L^*.$$ If the orthonormal frames are replaced by $Q_RR$ and $Q_LL$ with unitary $R,L$, then the new cross Gram is $L^*HR$ and [\[eq:coordinate-free-projector\]](#eq:coordinate-free-projector){reference-type="eqref" reference="eq:coordinate-free-projector"} is unchanged. Hence the oblique projector is determined by the ordered pair $(\mathcal R,\mathcal L)$, not by the SVD or QR conventions used to compute it.

# Principal angles and perturbative transversality

Let $\theta_1\le\cdots\le\theta_r$ be the principal angles between $\mathcal R$ and $\mathcal L$. Then $\sigma_j=\cos\theta_j$ and $$\label{eq:angle-condition}
 \left\lVert P\right\rVert=\sec\theta_r.$$ The construction becomes singular precisely when the largest principal angle reaches $\pi/2$. This geometric form is useful because it separates dimension from transversality: increasing the packet rank is harmless only if the newly added directions do not approach orthogonality to the dual space.

The next proposition gives the elementary validation margin for a computed cross Gram.

Let $\widetilde H=H+E$, where $\gamma=\sigma_{\min}(H)>0$ and $\left\lVert E\right\rVert\le\eta<\gamma$. Then $$\begin{aligned}
 \sigma_{\min}(\widetilde H)&\ge\gamma-\eta,
 \label{eq:weyl-margin}\\
 \left\lVert\widetilde H^{-1}\right\rVert&\le\frac1{\gamma-\eta},
 \label{eq:inverse-margin}\\
 \left\lVert\widetilde H^{-1}-H^{-1}\right\rVert
 &\le\frac{\eta}{\gamma(\gamma-\eta)}.
 \label{eq:inverse-difference}\end{aligned}$$

The singular-value perturbation inequality gives [\[eq:weyl-margin\]](#eq:weyl-margin){reference-type="eqref" reference="eq:weyl-margin"}, which implies [\[eq:inverse-margin\]](#eq:inverse-margin){reference-type="eqref" reference="eq:inverse-margin"}. The resolvent identity $\widetilde H^{-1}-H^{-1}=-\widetilde H^{-1}EH^{-1}$ then gives [\[eq:inverse-difference\]](#eq:inverse-difference){reference-type="eqref" reference="eq:inverse-difference"}.

This proposition exposes the validation price of a tiny cross angle. To prove transversality by outward numerics, the operator error in $H$ must be strictly smaller than $\gamma$. For the later physical candidates with $\gamma$ near $10^{-3}$, a coarse floating reconstruction is not enough even when the raw Ritz residuals look small.

# Compressed operator and directed residuals

For a bounded operator $A$ on $\mathcal H$, define $$\begin{aligned}
 K&=W_L^*AV_R,
 \label{eq:compressed}\\
 R_R&=(I-P)AV_R,
 \label{eq:right-residual}\\
 R_L&=(I-P^*)A^*W_L.
 \label{eq:left-residual}\end{aligned}$$ Then $$\label{eq:block-actions}
 AV_R=V_RK+R_R,
 \qquad
 A^*W_L=W_LK^*+R_L.$$ The residuals are exactly the two directed off-diagonal couplings for the oblique decomposition $\mathcal H=\mathcal R\dotplus\mathcal L^\perp$.

[\[prop:criterion\]]{#prop:criterion label="prop:criterion"} The right space is invariant and the left space is adjoint-invariant with the common compressed operator $K$ if and only if $R_R=R_L=0$.

Equation [\[eq:block-actions\]](#eq:block-actions){reference-type="eqref" reference="eq:block-actions"} is an exact decomposition. The first residual vanishes precisely when $AV_R$ lies in $\mathcal R$; the second vanishes precisely when $A^*W_L$ lies in $\mathcal L$.

Unlike the RH-182 orthogonal construction, $P$ need not be self-adjoint. This is a feature, not a defect: the right and left physical packets are allowed to differ.

# Gauge covariance

For any invertible $G\in\mathbb C^{r\times r}$, set $$\label{eq:gauge}
 V_R'=V_RG,
 \qquad
 W_L'=W_LG^{-*}.$$ Then $W_L'^*V_R'=I$ and the projector is unchanged. The compressed operator transforms as $$\label{eq:gauge-K}
 K'=G^{-1}KG.$$ Hence its eigenvalues, determinant, and trace words are packet-gauge invariants. The residual columns transform covariantly. This is the correct finite canonicity statement: a particular balanced frame is a convenient representative of a gauge class.

# Finite identity audit

The implementation audit uses ambient dimensions $8,12,18,24$, ranks $2,3,4$, and ten complex random trials per pair, for 120 cases. It verifies:

1.  $W_L^*V_R=I$;

2.  $P^2=P$;

3.  $\left\lVert V_R\right\rVert=\left\lVert W_L\right\rVert=\sigma_r^{-1/2}$;

4.  $\left\lVert P\right\rVert=\sigma_r^{-1}$;

5.  similarity covariance of $K$ under a random invertible gauge;

6.  equality of the compressed spectra before and after the gauge.

All 120 cases pass at tolerance $10^{-9}$. The largest recorded errors are

  identity                               maximum error
  ----------------------------- ----------------------
  biorthogonality                 $1.20\times10^{-14}$
  projector idempotence           $1.49\times10^{-13}$
  projector norm formula          $3.56\times10^{-14}$
  compressed gauge covariance     $7.57\times10^{-14}$
  spectrum covariance             $2.30\times10^{-13}$

The audit deliberately samples gauges as well as subspaces. This catches a common implementation error: correcting the right frame without applying the inverse-adjoint correction to the left frame preserves neither biorthogonality nor the compressed similarity class. The stored checks separately verify the frame identity, the projector identity, and the compressed spectrum so that one successful equality cannot mask another failure.

For physical use, the recommended validated pipeline is therefore: enclose the two QR ranges, enclose their cross Gram, prove a positive lower bound in [\[eq:weyl-margin\]](#eq:weyl-margin){reference-type="eqref" reference="eq:weyl-margin"}, construct any convenient biorthogonal gauge, and carry the resulting oblique factor into all later residual and resolvent budgets. Balancing is optimal for norm display, but it does not remove the cross-angle obligation.

# Physical specialization

For a source $S$ and observation $O$, the intended right and left synthesis matrices are $$\begin{aligned}
 J_R(t,L)&=[\widehat{A^tS},\ldots,
 \widehat{A^{t+L-1}S}],
 \label{eq:right-krylov}\\
 J_L(t,L)&=[\widehat{(A^*)^tO^*},\ldots,
 \widehat{(A^*)^{t+L-1}O^*}],
 \label{eq:left-krylov}\end{aligned}$$ where hats denote Frobenius normalization and each matrix is vectorized into the physical Frobenius space. QR factorization gives $Q_R,Q_L$; the theorem then supplies the unique balanced cross-Gram gauge.

This construction is target-independent in the limited sense required here: it uses the physical operator, source, observation, start time, and predeclared length, but no target eigenvectors. It remains a finite-scale object. Whether $H$ is sufficiently transverse, whether $R_R,R_L$ are small, and whether the result matches the geometric cloud are empirical and analytic questions for RH-185.

# Boundary and next wall

This paper closes the finite algebraic leaf $$\label{eq:closed-leaf}
 (\mathcal R,\mathcal L)\longmapsto(V_R,W_L,K,R_R,R_L,P)$$ whenever the cross Gram is invertible. It also proves the exact unavoidable conditioning $\sigma_r^{-1}$.

It does not prove physical cross-Gram invertibility uniformly in scale, small physical residuals, bounded oblique conditioning, a complement resolvent, a Riesz rank theorem, shell transport, physical interface R, Gate A, or any Hilbert--Polya or Riemann-hypothesis claim.
