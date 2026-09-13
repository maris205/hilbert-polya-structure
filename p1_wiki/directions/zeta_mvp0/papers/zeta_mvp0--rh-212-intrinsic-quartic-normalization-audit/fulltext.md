---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-212-intrinsic-quartic-normalization-audit"
canonical_tex: "zeta_mvp0/papers/RH-212-intrinsic-quartic-normalization-audit/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-212-intrinsic-quartic-normalization-audit/main.pdf"
source_sha256: "42677a513f29f0c994a4ccd547fbedce750fa6c4284246831078a47ed0072be4"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# An Intrinsic Normalization Audit for the Physical Quartic Divisor Eight Predeclared Levels and a Sixteen-Level Frozen Atlas

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-212-intrinsic-quartic-normalization-audit>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-212-intrinsic-quartic-normalization-audit/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-212-intrinsic-quartic-normalization-audit/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-212-intrinsic-quartic-normalization-audit/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-212-intrinsic-quartic-normalization-audit/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The divisor-first pivot of RH-210--RH-211 leaves a concrete question: can a simple intrinsic normalization turn the finite physical quartic into a contracting coefficient flow? We compare three representations on eight predeclared small-noise levels and both physical channels: the raw monic quartic, determinant-radius normalization, and centered root-mean-square normalization. No parameters are fitted level by level.

  The answer is negative for the two proposed normalizations. With adjacent error measured relative to the fine coefficient vector, the raw flow has range $0.04419$--$0.18945$ and mean $0.10661$. Determinant-radius normalization worsens these values to $0.06062$--$0.36787$ and $0.19322$; centered-RMS normalization gives $0.05941$--$0.23389$ and $0.16592$. Maximum left/right relative discrepancies are respectively $0.008112$, $0.019881$, and $0.009368$. Thus the raw coefficients remain the most stable of the three tested representations.

  We also freeze a sixteen-level dual-channel root atlas down to $\sigma=0.00125$. Sparse modulus-cloud extraction exactly reproduces the previous dense-spectrum anchors while avoiding repeated dense eigensolves. The negative contraction result is useful: centered-RMS normalization exposes an exact lower-dimensional shape structure, developed in RH-213, rather than another fitted scalar law. No coefficient limit, growing determinant, Fredholm realization, or Gate-A closure is claimed.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  An Intrinsic Normalization Audit for the Physical Quartic Divisor\
  Eight Predeclared Levels and a Sixteen-Level Frozen Atlas
```

## Markdown 正文

# Question inherited from the transport frontier

RH-207 identified a coherent left/right quartic divisor, while RH-202--RH-210 showed that naive state-space transport is not its stable realization [@WangRH207; @WangRH210; @WangRH211]. Let $$\label{eq:raw}
 D_{\sigma,s}(z)=\prod_{j=1}^{4}(z-\lambda_{\sigma,s,j})
 =z^4+c_{1,\sigma,s}z^3+c_{2,\sigma,s}z^2
   +c_{3,\sigma,s}z+c_{4,\sigma,s},$$ where $s\in\{L,R\}$ labels the two physical channels. Three coarse anchors showed channel coherence but not stationarity in $\sigma$.

The present audit asks a deliberately narrow question. Is the scale motion mostly an affine gauge that can be removed by one natural formula at every level? A positive answer would produce a candidate compact coefficient family. A negative answer rules out only the tested formulas, not every renormalization.

# Predeclared scale protocol

The normalization comparison uses $$\label{eq:auditscales}
 0.04,\ 0.032,\ 0.025,\ 0.02,\ 0.016,\ 0.0125,\ 0.01,\ 0.008.$$ The frozen atlas additionally contains $$\label{eq:extrascales}
 0.00625,\ 0.005,\ 0.004,\ 0.0032,\ 0.0025,\ 0.002,\ 0.0016,\ 0.00125.$$ The last eight points are not used to redefine the RH-212 winner. They are published so that subsequent papers can state their own training and holdout rules without recomputing the matrix spectrum.

At each scale we retain the same inherited physical rule: remove the Perron and negative parity modes and select the next four eigenvalues by modulus. The selected set is checked for conjugate closure. All 32 endpoint packets are conjugate closed to the reported floating precision.

# Three intrinsic representations

## Raw monic coefficients

The baseline is simply the coefficient vector $$C^{\rm raw}_{\sigma,s}=(1,c_1,c_2,c_3,c_4).$$ It retains location, radius, and shape. It is similarity invariant but not invariant under affine changes of the spectral variable.

## Determinant-radius normalization

Set $$\label{eq:detradius}
 \rho=\left|\prod_{j=1}^{4}\lambda_j\right|^{1/4}
      =|c_4|^{1/4},\qquad \widehat\lambda_j=\lambda_j/\rho.$$ Then the constant coefficient of $\prod_j(z-\widehat\lambda_j)$ has modulus one.

[\[prop:detintrinsic\]]{#prop:detintrinsic label="prop:detintrinsic"} For every quartet with nonzero product, $\rho$ is invariant under root permutation and operator similarity. The normalized constant term has modulus one.

Both statements follow from the elementary symmetric product and $\prod_j\widehat\lambda_j=\rho^{-4}\prod_j\lambda_j$.

This normalization does not remove translation. It can also amplify the remaining coefficients when $|c_4|$ is small.

## Centered RMS normalization

Define $$\label{eq:rms}
 \mu=\frac14\sum_{j=1}^{4}\lambda_j,
 \qquad
 r=\left(\frac14\sum_{j=1}^{4}|\lambda_j-\mu|^2\right)^{1/2},
 \qquad q_j=\frac{\lambda_j-\mu}{r}.$$

[\[prop:rmsgauge\]]{#prop:rmsgauge label="prop:rmsgauge"} For every nonconstant quartet, $$\frac14\sum_j q_j=0,
 \qquad \frac14\sum_j|q_j|^2=1.$$ The multiset $\{q_j\}$ is invariant under translation $\lambda_j\mapsto\lambda_j+a$ and positive dilation $\lambda_j\mapsto b\lambda_j$ with $b>0$.

Centering gives the first identity and the definition of $r$ gives the second. Under translation, the barycenter translates by the same amount. Under positive dilation, both centered roots and $r$ are multiplied by $b$.

For conjugate-closed quartets, $\mu$ is real and the normalized polynomial has real coefficients and zero cubic coefficient. This exact structural gain will matter even though contraction fails.

# Error functional

For adjacent coarse/fine scales $\sigma_c>\sigma_f$, write $C_c,C_f$ for one of the three monic coefficient vectors and define $$\label{eq:error}
 E_f(C_c,C_f)=\frac{\left\lVert C_f-C_c\right\rVert_2}{\left\lVert C_f\right\rVert_2}.$$ The fine denominator is fixed in advance and treats the refined endpoint as the target. Maximum absolute coefficient error and the reverse denominator are also archived, but no conclusion depends on changing the metric after inspection.

At a fixed scale, channel discrepancy is $$\label{eq:channelerror}
 E_{LR}=\frac{\left\lVert C_L-C_R\right\rVert_2}{\left\lVert C_L\right\rVert_2}.$$

# Finite normalization verdict

The 14 adjacent/channel cases for each representation give:

  representation         min $E_f$   max $E_f$   mean $E_f$   max $E_{LR}$
  -------------------- ----------- ----------- ------------ --------------
  raw                    $0.04419$   $0.18945$    $0.10661$     $0.008112$
  determinant radius     $0.06062$   $0.36787$    $0.19322$     $0.019881$
  centered RMS           $0.05941$   $0.23389$    $0.16592$     $0.009368$

[\[prop:negative\]]{#prop:negative label="prop:negative"} On the eight predeclared levels and both channels, neither determinant-radius nor centered-RMS normalization improves the mean, maximum, or minimum adjacent fine-relative coefficient error simultaneously. The raw vector has the smallest mean and maximum, and it also has the smallest worst channel discrepancy.

This is the direct comparison in the displayed table, generated from the frozen endpoint roots by the exact formulas above.

The word "negative" is important. The data do not establish that every intrinsic normalization fails. They reject two concrete formulas as a uniformly better cross-scale coordinate on this audit.

# Why normalization can worsen the flow

The determinant radius forces one coefficient to a fixed modulus, but the other coefficients transform with different powers of $\rho^{-1}$. Small relative motion in $c_4$ can therefore induce larger motion in lower-order terms. The operation removes one scalar without separating translation from shape.

Centered-RMS normalization removes two affine degrees of freedom. If the remaining shape itself moves substantially, the normalized vector must show that motion more clearly. Consequently a larger coefficient error is not a defect of the quotient. It can be evidence that location and radius were masking a genuine shape trajectory.

Indeed, every centered-RMS polynomial in the atlas has zero cubic term and lies, to roundoff, on one algebraic surface in the remaining three coefficients. RH-213 proves that this surface is exactly two-dimensional. Thus RH-212 changes the next question from "which scalar should be fitted?" to "what exact geometry remains after the affine gauge is removed?"

# Sparse extraction and reproducibility

The historical construction formed a dense deflated bulk operator. Its outer nontrivial eigenvalues are unchanged if one instead computes a modulus cloud of the original sparse folded-Gaussian matrix, removes the Perron and negative real parity roots, and takes the next quartet. At the old anchors $0.04,0.02,0.01$, the resulting roots and coefficients reproduce the frozen dense results to floating roundoff.

This shortcut is not a new spectral theorem. It is an algebraic consequence of replacing two selected eigenvalues by zero in the inherited finite model, combined with a cloud large enough to resolve the radial gap. The archive retains dimensions, roots, coefficients, centers, radii, and conjugacy diagnostics for every endpoint.

# Claim boundary and route consequence

The following remain open:

1.  existence of either a raw or normalized coefficient limit;

2.  stability under all smaller noise levels;

3.  a rank-growing cloud with controlled omitted factors;

4.  local uniform convergence to a nonzero analytic determinant;

5.  a dynamical or Fredholm realization.

Gate A is therefore open. Gates B--E are untouched. No self-adjoint operator, $T\log T$ law, arithmetic trace identity, zeta divisor, or RH statement is inferred. The immediate route is the exact centered shape manifold, not another post-hoc normalization.
