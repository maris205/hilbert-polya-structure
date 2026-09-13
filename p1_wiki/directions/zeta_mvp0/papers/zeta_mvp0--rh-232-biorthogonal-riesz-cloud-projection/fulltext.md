---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-232-biorthogonal-riesz-cloud-projection"
canonical_tex: "zeta_mvp0/papers/RH-232-biorthogonal-riesz-cloud-projection/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-232-biorthogonal-riesz-cloud-projection/main.pdf"
source_sha256: "72cfa03bec7ed0d93d2b67f6156b4b9f47202445b4861411ac7a8faaaf7b71d8"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Biorthogonal Riesz-Cloud Projection and Its Conditioning Wall

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-232-biorthogonal-riesz-cloud-projection>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-232-biorthogonal-riesz-cloud-projection/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-232-biorthogonal-riesz-cloud-projection/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-232-biorthogonal-riesz-cloud-projection/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-232-biorthogonal-riesz-cloud-projection/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-231 reduced the next determinant step to a moving cloud factor and a uniformly controlled complement. We test the most literal implementation: construct the finite spectral projector from matched right and left Arnoldi eigenspaces. If $R,L\in\mathbb C^{d\times k}$ and $G=L^*R$ is invertible, then $P=RG^{-1}L^*$ is the unique projector with range $\operatorname{ran}R$ and kernel $\ker L^*$. For exact paired invariant spaces it is reducing.

  All 32 shell-complete RH-222 endpoints admit floating projector candidates. The right and left eigenpair residuals are at most $1.60\times10^{-12}$ and $2.16\times10^{-12}$, respectively. Nevertheless the smallest overlap singular value is $5.67\times10^{-13}$, the largest overlap condition number is $1.47\times10^{12}$, and the projector norm grows from about $40.75$ to $2.26\times10^{12}$. Seventeen endpoints exceed $10^6$.

  Thus the finite Riesz formula is available, but its direct numerical realization does not supply a uniform small-noise projector bound. This is a conditioning result, not an interval-certified nonexistence theorem. Gate A and all later Hilbert--Polya gates remain open.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: 'Biorthogonal Riesz-Cloud Projection and Its Conditioning Wall'
```

## Markdown 正文

# The moving-cloud projector problem

The RH-222 atlas selects conjugacy-closed outer resonance clouds whose ranks grow from four to $34$--$35$ as the noise decreases [@WangRH222; @WangRH231]. RH-80 showed that a reducing cloud projection would give an exact determinant factorization and would isolate the only block for which a uniform ideal bound is needed [@WangRH80]. The present question is narrower: can the archived finite eigendata be converted into a numerically stable reducing projector?

For a nonnormal matrix, right eigenvectors alone do not determine a bounded projection. The left/right angle is decisive; this is standard in nonnormal perturbation theory [@Kato1995; @TrefethenEmbree2005].

# Biorthogonal projector formula

[\[thm:projector\]]{#thm:projector label="thm:projector"} Let $A\in\mathbb C^{d\times d}$. Suppose the columns of $R,L\in\mathbb C^{d\times k}$ are linearly independent and $G=L^*R$ is invertible. Then $$P=RG^{-1}L^*$$ satisfies $P^2=P$, $\operatorname{ran}P=\operatorname{ran}R$, and $\ker P=\ker L^*$.

If there is a matrix $\Lambda\in\mathbb C^{k\times k}$ such that $$AR=R\Lambda,
 \qquad
 A^*L=L\Lambda^*,$$ then $AP=PA$.

The identity $L^*R=G$ gives $$P^2=RG^{-1}(L^*R)G^{-1}L^*=RG^{-1}L^*=P.$$ Also $PR=R$, so the range is exactly $\operatorname{ran}R$, while $Px=0$ precisely when $L^*x=0$. Invariance gives $$AP=R\Lambda G^{-1}L^*,
 \qquad
 PA=RG^{-1}\Lambda L^*.$$ Since $L^*AR=(A^*L)^*R=\Lambda L^*R$ and also $L^*AR=L^*R\Lambda$, one has $\Lambda G=G\Lambda$; hence the two expressions coincide.

The formula is exact but potentially unstable. The inverse overlap $G^{-1}$ can be large even when each eigenpair residual is tiny. A reduced QR factorization evaluates the nonzero singular values of $P$ without ever forming a dense $d\times d$ matrix.

[\[prop:angle\]]{#prop:angle label="prop:angle"} Let $R=Q_RX$ and $L=Q_LY$ be thin QR factorizations, where $Q_R,Q_L$ have orthonormal columns and $X,Y$ are invertible. Set $H=Q_L^*Q_R$. If $H$ is invertible, then $$P=Q_RH^{-1}Q_L^*,
 \qquad
 \left\lVert P\right\rVert_2=\left\lVert H^{-1}\right\rVert_2=\frac{1}{s_{\min}(H)}.$$ Equivalently, if $\theta_{\max}$ is the largest principal angle between $\operatorname{ran}R$ and $\operatorname{ran}L$, then $\left\lVert P\right\rVert_2=\sec\theta_{\max}$.

Substitution into $R(L^*R)^{-1}L^*$ cancels $X$ and $Y^*$ and gives the first formula. Left multiplication by $Q_R$ is isometric, while every vector in $\mathbb C^k$ is $Q_L^*x$ for some unit-space vector $x$ of the same norm. Hence $\left\lVert Q_RH^{-1}Q_L^*\right\rVert_2=\left\lVert H^{-1}\right\rVert_2$. The singular values of $Q_L^*Q_R$ are the cosines of the principal angles.

Proposition [\[prop:angle\]](#prop:angle){reference-type="ref" reference="prop:angle"} removes a possible ambiguity in interpreting the audit. The large norms are not caused by a poor normalization of the individual eigenvectors: QR normalization cancels that freedom. They record an intrinsic near-orthogonality of the right cloud and the dual left cloud. Thus a uniform projector theorem would need a uniform lower bound for $s_{\min}(Q_L^*Q_R)$, or an equivalent contour-resolvent estimate.

# Frozen finite audit

At each endpoint we reconstruct the same row-stochastic folded Gaussian matrix used in RH-222. The right endpoint is the Haar-coarse compression of the corresponding fine matrix. We scale by the same Hardy radius $0.85$, match the Perron root, parity root, and shell-complete cloud, and independently solve the transposed problem for the left space.

     $\sigma$    side   rank incl. peripheral   $\left\lVert P\right\rVert_2$      overlap condition
  ----------- ------- ----------------------- ------------------------------- ----------------------
       $0.04$    left                       6               $4.159\times10^1$                    ---
       $0.04$   right                       6               $4.075\times10^1$                    ---
      $0.005$    left                      25               $4.476\times10^6$                    ---
      $0.005$   right                      25               $4.972\times10^6$                    ---
    $0.00125$    left                      37            $2.261\times10^{12}$   $1.466\times10^{12}$
    $0.00125$   right                      36            $5.436\times10^{10}$                    ---

  : Representative floating biorthogonal projector candidates. Dashes mean that only the batch extremum, not the displayed row value, is quoted.

The smallest observed ratio between radial gap and projector norm is $6.40\times10^{-16}$. Moreover the absolute floating commutator defect can become large because residuals of size $10^{-12}$ are amplified by a projector of size $10^{12}$. This is precisely the regime where a posteriori residuals cease to imply a robust invariant subspace.

# Conditioning versus residual accuracy

Small eigenpair residuals and a stable spectral subspace answer different questions. A residual bound certifies that each computed vector is close to being invariant in an absolute sense. Passing from those vectors to an oblique projector requires inversion of the overlap matrix. First-order perturbations of $G^{-1}$ contain the factor $$\delta(G^{-1})=-G^{-1}(\delta G)G^{-1}+O(\left\lVert\delta G\right\rVert^2),$$ so the overlap condition number enters twice in a naive perturbation bound. At the last endpoints, ordinary double-precision perturbations are therefore not small relative to the inverse-overlap scale, even though the Arnoldi residuals themselves remain near $10^{-12}$.

This observation also explains why forming the full matrix $P$ is avoided in the archived calculation. The norm is evaluated from the reduced overlap in Proposition [\[prop:angle\]](#prop:angle){reference-type="ref" reference="prop:angle"}; idempotence and commutator diagnostics are reported only as floating consistency checks. They are not used as certificates of a small-noise limiting projection.

# What a certified continuation would require

There are at least three mathematically distinct ways to improve the finite construction.

1.  *Interval biorthogonality:* enclose both invariant spaces and prove a positive lower bound for the smallest overlap singular value.

2.  *Contour control:* choose a shell-complete contour and bound the resolvent uniformly on it, thereby defining the Riesz projector without pairing individual roots.

3.  *Adapted function spaces:* conjugate the transfer operator into a norm in which the left/right angle remains controlled as the noise and mesh vanish.

The current data neither proves nor disproves any of these stronger possibilities. It does show that the unweighted Euclidean realization cannot be promoted to a uniform theorem merely from residual accuracy.

# What is and is not proved

Theorem [\[thm:projector\]](#thm:projector){reference-type="ref" reference="thm:projector"} is unconditional finite-dimensional algebra. The audit establishes that the archived eigenvalues can be paired with left and right Arnoldi vectors, but it does not provide interval enclosures for the eigenvalues, an interval lower bound for $s_{\min}(G)$, or a certified contour resolvent estimate.

The negative conclusion is correspondingly precise: the direct floating biorthogonal construction does not support a uniform projector bound. A different function space, an analytic contour argument, or a determinant factorization that avoids projector norms may still succeed. RH-233 tests whether the positive radial shell gaps can rescue the construction; RH-234 develops the projection-free alternative.

No self-adjoint operator, $T\log T$ law, prime-power trace formula, zeta-zero identification, or Riemann-hypothesis implication is asserted.
