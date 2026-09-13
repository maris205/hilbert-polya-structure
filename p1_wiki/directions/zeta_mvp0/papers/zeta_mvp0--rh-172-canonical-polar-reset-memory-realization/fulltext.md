---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-172-canonical-polar-reset-memory-realization"
canonical_tex: "zeta_mvp0/papers/RH-172-canonical-polar-reset-memory-realization/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-172-canonical-polar-reset-memory-realization/main.pdf"
source_sha256: "d90cdd91381737b5a1b1bc86a5c5ff8dbc81df2602af5f778368593f56798b7a"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Canonical Polar Realization of Reset-Memory Packets An Exact Finite-History Solution to the Source-Space Type Problem

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-172-canonical-polar-reset-memory-realization>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-172-canonical-polar-reset-memory-realization/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-172-canonical-polar-reset-memory-realization/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-172-canonical-polar-reset-memory-realization/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-172-canonical-polar-reset-memory-realization/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The reset atlas of RH-151 selects a clock-rank packet from a recursive source-memory Gram matrix. The packet therefore lives in source-column space, whereas the moving-cloud determinant of RH-80 lives in a transfer space. RH-162 correctly identified the resulting ambient-space type gap, but did not exploit the special Gram structure of the archived reset data.

  We factor that structure exactly. If $S_k=A^kS_0$ and $\widehat S_k=S_k/\left\lVert S_k\right\rVert_F$, define $$F_t x=(\widehat S_t x,\sqrt\eta\widehat S_{t-1}x,
   \ldots,\eta^{t/2}\widehat S_0x).$$ Then the recursive memory is precisely $M_t=F_t^*F_t$. For any rank-$r$ spectral packet $P_t$ on which $M_t$ is positive, the partial polar map $$J_t=F_tP_t\bigl(P_tM_tP_t|_{\operatorname{Ran}P_t}\bigr)^{-1/2}$$ is an isometry from $\operatorname{Ran}P_t$ into the normalized history space. Its range projection is canonical, independent of packet-frame gauge and covariant under every unitary change of source coordinates. In an eigenframe $U_t^*M_tU_t=\Lambda_t$, the formula becomes $V_t=F_tU_t\Lambda_t^{-1/2}$.

  This closes a finite-dimensional source-memory-to-history realization, denoted $X_{\rm mem\to hist}$. It does not identify the history space with the RH-80 transfer/determinant space and therefore does not close the physical interface $X_{\rm phys}$. A 192-case complex synthetic audit checks the Gram, polar, source-gauge, and packet-gauge identities with maximum residual below $5.5\times10^{-15}$. The theorem is exact; the audit validates only its implementation. No all-level limit, Riesz cloud, canonical determinant, Hilbert--Polya operator, or Riemann-hypothesis conclusion is claimed.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Canonical Polar Realization of Reset-Memory Packets\
  An Exact Finite-History Solution to the Source-Space Type Problem
```

## Markdown 正文

**Keywords:** Gram factorization; polar decomposition; reset packet; finite history; gauge covariance; nonselfadjoint dynamics.

# The precise type problem

RH-151 constructs, at each frozen scale and time, the top clock-rank spectral packet of a positive memory matrix [@WangRH151]. The memory acts on the columns of the source $S_0$, not on the state space on which the production transfer operator acts. Writing both packets with the same letter suppresses a genuine type distinction: $$P_t^{\rm reset}\in\mathcal B(\mathcal X),
 \qquad
 \Pi_t^{\rm cloud}\in\mathcal B(\mathcal H_{\rm transfer}).$$ RH-162 therefore required an ambient realization before applying a packet-to-Riesz theorem [@WangRH162].

The first question is narrower than the full physical bridge. Does the particular reset memory already carry a canonical Hilbert-space realization, without fitting target eigenvectors or choosing an arbitrary injection? The answer is yes. The target is a normalized finite-history space determined by the source dynamics itself. This paper constructs that target and proves its canonicity. Whether it is the correct transfer target is left open.

# Normalized source memory

Let $\mathcal X$ and $\mathcal Y$ be finite-dimensional complex Hilbert spaces. Let $A\in\mathcal B(\mathcal Y)$, let $S_0:\mathcal X\to\mathcal Y$ be nonzero, and suppose $S_k=A^kS_0\ne0$ for $0\le k\le t$. Fix $0\le\eta<1$ and put $$\alpha_k=\left\lVert S_k\right\rVert_F,
 \qquad \widehat S_k=\alpha_k^{-1}S_k.$$ The RH-94/RH-151 memory recursion is $$\label{eq:memory-recursion}
 M_{-1}=0,
 \qquad
 M_k=\widehat S_k^*\widehat S_k+\eta M_{k-1}.$$ Every $M_k$ is positive semidefinite and $\operatorname{tr}M_k=1+\eta+\cdots+\eta^k$.

Define the history space $$\mathcal K_t=\underbrace{\mathcal Y\oplus\cdots\oplus\mathcal Y}_{t+1\text{ copies}}$$ with current time first, and define $F_t:\mathcal X\to\mathcal K_t$ by $$\label{eq:history-factor}
 F_tx=
 \bigl(\widehat S_tx,\sqrt\eta\widehat S_{t-1}x,
 \ldots,\eta^{t/2}\widehat S_0x\bigr).$$

[\[thm:gram\]]{#thm:gram label="thm:gram"} For every finite time $t$, $$\label{eq:gram-factorization}
 M_t=F_t^*F_t
 =\sum_{k=0}^t\eta^{t-k}\widehat S_k^*\widehat S_k.$$ Consequently $\ker M_t=\ker F_t$ and $\operatorname{rank}M_t=\operatorname{rank}F_t$.

The direct-sum norm has no cross terms, hence $$\langle F_tx,F_ty\rangle
 =\sum_{k=0}^t\eta^{t-k}
 \langle\widehat S_kx,\widehat S_ky\rangle.$$ This proves the second identity in [\[eq:gram-factorization\]](#eq:gram-factorization){reference-type="eqref" reference="eq:gram-factorization"}. Iterating [\[eq:memory-recursion\]](#eq:memory-recursion){reference-type="eqref" reference="eq:memory-recursion"} gives the same sum. Finally, $\langle M_tx,x\rangle=\left\lVert F_tx\right\rVert^2$, so the kernels agree; rank equality follows in finite dimension.

The factor $F_t$ is not introduced by an eigenvector fit. It is forced by the actual recursion, including the normalization and forgetting weight. Thus the source memory already has an intrinsic realization, albeit on a history space rather than the desired transfer space.

# Canonical realization of a reset packet

Let $P$ be a rank-$r$ orthogonal projection on $\mathcal X$. Assume $$\label{eq:positive-packet}
 PM_tP|_{\operatorname{Ran}P}>0.$$ This condition is automatic when $P$ is spanned by $r$ positive eigenvalues of $M_t$. On $\operatorname{Ran}P$ define $$\label{eq:partial-polar}
 J_{t,P}=F_tP\bigl(PM_tP|_{\operatorname{Ran}P}\bigr)^{-1/2}.$$

[\[thm:polar\]]{#thm:polar label="thm:polar"} Under [\[eq:positive-packet\]](#eq:positive-packet){reference-type="eqref" reference="eq:positive-packet"}, $J_{t,P}:\operatorname{Ran}P\to\mathcal K_t$ is an isometry: $$J_{t,P}^*J_{t,P}=I_{\operatorname{Ran}P}.$$ Its range is $F_t(\operatorname{Ran}P)$, and its ambient projection is $$\label{eq:realized-projection}
 Q_{t,P}=J_{t,P}J_{t,P}^*.$$ Both $J_{t,P}$ and $Q_{t,P}$ are determined by $(F_t,P)$; no target eigenbasis is chosen.

By Theorem [\[thm:gram\]](#thm:gram){reference-type="ref" reference="thm:gram"}, $$(F_tP)^*(F_tP)|_{\operatorname{Ran}P}=PM_tP|_{\operatorname{Ran}P}.$$ Substitution in [\[eq:partial-polar\]](#eq:partial-polar){reference-type="eqref" reference="eq:partial-polar"} gives $J_{t,P}^*J_{t,P}=I$. The inverse square root is invertible on $\operatorname{Ran}P$, so multiplying by it does not change the image of $F_tP$. Uniqueness is the uniqueness of the polar partial isometry on the initial space $(\ker F_tP)^\perp=\operatorname{Ran}P$ [@Higham2008].

Suppose now that $U:\mathbb C^r\to\mathcal X$ is an orthonormal eigenframe, $$U^*U=I_r,
 \qquad P=UU^*,
 \qquad U^*M_tU=\Lambda=\operatorname{diag}(\lambda_1,\ldots,\lambda_r),$$ where every $\lambda_j>0$. Then Theorem [\[thm:polar\]](#thm:polar){reference-type="ref" reference="thm:polar"} becomes $$\label{eq:frame-formula}
 V=F_tU\Lambda^{-1/2},
 \qquad V^*V=I_r,
 \qquad Q_{t,P}=VV^*.$$ This is the formula used by the numerical audit.

# Gauge covariance and degeneracy

There are two unrelated gauges: a basis change in source space and a basis change inside the selected packet. A canonical construction must handle both.

[\[prop:source-gauge\]]{#prop:source-gauge label="prop:source-gauge"} Let $R$ be unitary on $\mathcal X$ and replace every source state by $S_k'=S_kR$. Then $$F_t'=F_tR,
 \qquad M_t'=R^*M_tR.$$ If $P'=R^*PR$, the realized history projection is unchanged: $$Q'_{t,P'}=Q_{t,P}.$$

Frobenius norms are invariant under right unitary multiplication, so every normalized block transforms by $\widehat S_k'=\widehat S_kR$. This proves the first two identities. The positive compression transforms by unitary conjugacy, and functional calculus gives $(P'M_t'P')^{-1/2}=R^*(PM_tP)^{-1/2}R$ on the transformed range. Hence $J'_{t,P'}R^*=J_{t,P}$ and the range projections agree.

[\[prop:packet-gauge\]]{#prop:packet-gauge label="prop:packet-gauge"} In [\[eq:frame-formula\]](#eq:frame-formula){reference-type="eqref" reference="eq:frame-formula"}, replace $U$ by $UW$ for a unitary $W\in\mathbb C^{r\times r}$. If the positive factor is transformed rather than rediagonalized, the polar frame becomes $VW$. Therefore $VV^*$ is independent of packet frame.

At a repeated eigenvalue, an eigenframe is not canonical, but the spectral projection is canonical whenever the selected cluster is separated from its complement. Theorem [\[thm:polar\]](#thm:polar){reference-type="ref" reference="thm:polar"} is deliberately formulated with $P$, not with an ordered eigenbasis. It therefore survives internal degeneracy. If the rank boundary itself has zero gap, the choice of $P$ is not canonical; this is a packet-selection issue already separated in RH-151.

# Conditioning and stable evaluation

Formula [\[eq:frame-formula\]](#eq:frame-formula){reference-type="eqref" reference="eq:frame-formula"} is exact but can be a poor floating-point algorithm when $\lambda_r$ is very small. Direct division by $\sqrt{\lambda_r}$ magnifies the Gram and eigenvector errors. A stable implementation forms $X=F_tU$ and computes its thin singular value decomposition $$X=L\Sigma R^*.$$ The polar isometry is then $$\label{eq:svd-polar}
 V=LR^*,
 \qquad H=R\Sigma R^*,
 \qquad X=VH.$$ In exact arithmetic [\[eq:svd-polar\]](#eq:svd-polar){reference-type="eqref" reference="eq:svd-polar"} equals [\[eq:frame-formula\]](#eq:frame-formula){reference-type="eqref" reference="eq:frame-formula"}. Numerically it enforces orthonormal columns without explicitly applying a large inverse square root [@Higham2008].

An SVD routine may choose different singular-vector phases or rotate a repeated singular subspace. Those choices alter the frame $V$ but not the projection $VV^*$. The mathematically canonical object is the polar partial isometry, or its range projection when only the realized subspace is needed.

# Synthetic implementation audit

The reproducibility script generates 192 complex cases with source dimensions $6,9,12$, history lengths $1,2,4,7$, ranks one and three, and eight random trials per configuration. Each case applies an independent unitary source gauge and an independent packet-frame gauge. The maximum residuals are:

  identity                                   maximum residual
  ------------------------------------ ----------------------
  $F_t^*F_t=M_t$                         $7.16\times10^{-16}$
  $V^*V=I$                               $2.02\times10^{-15}$
  polar factorization $F_tU=VH$          $1.42\times10^{-15}$
  source-gauge covariance                $1.26\times10^{-15}$
  packet-gauge equivariance              $5.43\times10^{-15}$
  packet-gauge projection invariance     $2.20\times10^{-15}$

The audit is ordinary floating-point arithmetic and is not an interval certificate. It checks that the code implements the proved identities. It does not validate the upstream physical matrices or establish an asymptotic bound.

# A universal property for competing ambient realizations

The history factor is canonical because the memory recursion specifies it, but the Gram matrix by itself never determines an ambient Hilbert space absolutely. The precise residual freedom is unitary equivalence.

[\[prop:universal\]]{#prop:universal label="prop:universal"} Let $G:\operatorname{Ran}P\to\mathcal Z$ be another injective realization on a Hilbert space $\mathcal Z$ satisfying $$\label{eq:competing-gram}
 G^*G=PM_tP|_{\operatorname{Ran}P}.$$ Let $$W_G=G(G^*G)^{-1/2}$$ be its polar isometry. Then there is a unique unitary $$U_G:F_t(\operatorname{Ran}P)\longrightarrow G(\operatorname{Ran}P)$$ such that $$\label{eq:universal-unitary}
 U_GJ_{t,P}=W_G.$$ Conversely, every unitary $U_G$ on the realized packet range produces a realization with the same compressed Gram.

Both $J_{t,P}$ and $W_G$ are isometries with initial space $\operatorname{Ran}P$. Define $U_G(J_{t,P}x)=W_Gx$. Isometry of both maps makes this definition well posed and inner-product preserving, and surjectivity onto $G(\operatorname{Ran}P)$ is immediate. Uniqueness follows because $J_{t,P}(\operatorname{Ran}P)$ is the whole domain of $U_G$. Conversely, if $G=U_GJ_{t,P}(PM_tP)^{1/2}$, then $G^*G=PM_tP$.

This proposition gives a necessary exact test for a proposed transfer-space realization. If a candidate analysis map $G_t$ on the transfer side has the same packet Gram as $F_t$, then the packet portions of history and transfer space are canonically unitarily equivalent through [\[eq:universal-unitary\]](#eq:universal-unitary){reference-type="eqref" reference="eq:universal-unitary"}. The remaining problem is no longer an equal-rank identification; it is to construct $G_t$ from the physical transfer dynamics and verify [\[eq:competing-gram\]](#eq:competing-gram){reference-type="eqref" reference="eq:competing-gram"}, or a controlled approximate version of it.

If a proposed transfer realization $G$ satisfies $G^*G\ne PM_tP$ on $\operatorname{Ran}P$, then no unitary between the two realized packet ranges can intertwine both analysis maps while fixing their source coordinates. Any bridge must include a nontrivial positive polar correction.

Thus RH-172 supplies not only one ambient realization but also a comparison principle for every future one. The physical leaf $X_{\rm hist\to transfer}$ can be attacked by estimating the Gram mismatch, the induced polar correction, and the commutator with time evolution.

# Exact progress and remaining interface

The physical leaf $X_{\rm phys}$ from RH-171 can now be refined as $$\label{eq:x-split}
 X_{\rm phys}
 =X_{\rm mem\to hist}\wedge X_{\rm hist\to transfer}.$$ This paper proves the first factor at every finite time for every nonzero selected eigenvalue. The second factor remains open. In particular, the history space $\mathcal K_t$ grows with $t$, is not the RH-80 transfer space, and has not been shown to intertwine the noisy transfer operator, its square, or the moving determinant cloud.

The construction nevertheless removes one ambiguity. Future attempts may no longer identify a source packet with a transfer packet by notation; they must either:

1.  construct a bounded map from the canonical history realization into the transfer space and control its polar correction and commutator; or

2.  bypass reset memory and construct the Riesz cloud from a different intrinsic model.

Failure of the first option would reject only the reset-history branch.

# Theorem boundary

The exact results are finite-history Gram factorization, canonical polar realization, source-coordinate covariance, packet-gauge invariance, and the stable SVD evaluation rule. They establish $X_{\rm mem\to hist}$.

They do not establish a history-to-transfer intertwiner, a physical contour or Riesz projection, a uniform all-level packet gap, a Schatten complement, a canonical relative determinant, directed marked-trace convergence, a self-adjoint completion, a $T\log T$ law, a prime-power trace formula, a zeta divisor identity, or the Riemann Hypothesis.
