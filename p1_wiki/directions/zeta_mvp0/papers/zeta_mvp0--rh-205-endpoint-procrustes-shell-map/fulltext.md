---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-205-endpoint-procrustes-shell-map"
canonical_tex: "zeta_mvp0/papers/RH-205-endpoint-procrustes-shell-map/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-205-endpoint-procrustes-shell-map/main.pdf"
source_sha256: "3b9634a0d21d9ae75c47cf1592fc3730106a938f0725fb44357b5266fcf8d493"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Endpoint-Determined Procrustes Maps for Spectral Shells Exact Existence, Optimal Cost, and the Predictivity Gap

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-205-endpoint-procrustes-shell-map>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-205-endpoint-procrustes-shell-map/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-205-endpoint-procrustes-shell-map/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-205-endpoint-procrustes-shell-map/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-205-endpoint-procrustes-shell-map/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  A poor Haar transport angle does not prevent an exact map between two equal-dimensional endpoint packets: one can always construct a partial isometry after seeing both spaces. This paper makes that statement precise and quantifies its cost for the physical edge quartets.

  For orthonormal packet frames $Q_c,Q_f$ and an ambient embedding $J$, the unitary polar factor of $Q_f^*JQ_c$ solves the orthogonal Procrustes problem. The resulting rank-four operator $H=Q_fUQ_c^*$ maps the coarse packet exactly onto the fine packet, satisfies $H^*H=Q_cQ_c^*$ and $HH^*=Q_fQ_f^*$, and minimizes the discrepancy from the embedded coarse frame. Its squared minimum cost is $2k-2\sum_j\cos\theta_j$.

  An 80-case identity audit has zero failures and maximum error $3.15\times10^{-15}$. For the four physical transitions the rank-normalized optimal costs range from $0.44075$ to $0.70099$. Moreover, exact range transport does not intertwine dynamics: the largest matched eigenvalue movement is $0.38160$. The construction is therefore a canonical endpoint alignment but not a predictive renormalization map, because it uses the fine packet it is meant to predict.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Endpoint-Determined Procrustes Maps for Spectral Shells\
  Exact Existence, Optimal Cost, and the Predictivity Gap
```

## Markdown 正文

# Existence is not yet transport theory

RH-204 provides a unique correspondence between the two conjugate branches at adjacent scales [@WangRH204]. It is tempting to declare that this already gives a shell map. Linear algebra shows that an exact map indeed exists, but also shows why that fact alone is weak: any two subspaces of the same finite dimension admit a partial isometry.

The useful questions are instead:

1.  which exact map is closest to the predeclared physical embedding;

2.  how large is that correction;

3.  does the map intertwine the compressed dynamics;

4.  can it be constructed from the coarse level alone?

# Packet frames and principal cosines

Let $Q_c\in\mathbb C^{n_c\times k}$ and $Q_f\in\mathbb C^{n_f\times k}$ have orthonormal columns, and let $J:\mathbb C^{n_c}\to\mathbb C^{n_f}$ be an isometry. Set $$\label{eq:overlap}
 M=Q_f^*JQ_c.$$ The singular values $s_j$ of $M$ are the principal cosines between $\operatorname{Ran}(JQ_c)$ and $\operatorname{Ran}(Q_f)$ [@StewartSun1990]. Write $$\label{eq:svd}
 M=L\Sigma R^*,\qquad U=LR^*.$$

# Optimal endpoint map

[\[thm:procrustes\]]{#thm:procrustes label="thm:procrustes"} The unitary $U$ in [\[eq:svd\]](#eq:svd){reference-type="eqref" reference="eq:svd"} minimizes $$\label{eq:minimization}
 \min_{Z^*Z=I_k}\left\lVert Q_fZ-JQ_c\right\rVert_F.$$ The minimum obeys $$\label{eq:cost}
 \min\left\lVert Q_fZ-JQ_c\right\rVert_F^2
 =2k-2\sum_{j=1}^k s_j.$$ Moreover, $$\label{eq:H}
 H=Q_fUQ_c^*$$ is a partial isometry with $$\label{eq:projectors}
 H^*H=Q_cQ_c^*,\qquad HH^*=Q_fQ_f^*.$$

Expanding the squared norm gives $$2k-2\operatorname{Re}\operatorname{tr}(Z^*M).$$ Von Neumann's trace inequality bounds the last real part by $\sum_js_j$, with equality for $Z=LR^*$. Substituting [\[eq:H\]](#eq:H){reference-type="eqref" reference="eq:H"} and using orthonormality gives [\[eq:projectors\]](#eq:projectors){reference-type="eqref" reference="eq:projectors"}.

We normalize the reported cost by $\sqrt{k}$, so it measures the root mean square frame correction per mode.

# Physical Procrustes costs

For the four adjacent physical cases, the optimal costs are:

  step            side      right cost   left cost   max $|\Delta\lambda|$
  --------------- ------- ------------ ----------- -----------------------
  $0.04\to0.02$   left       $0.48343$   $0.45464$               $0.38105$
  $0.04\to0.02$   right      $0.45582$   $0.51047$               $0.38160$
  $0.02\to0.01$   left       $0.69446$   $0.44075$               $0.13643$
  $0.02\to0.01$   right      $0.44486$   $0.70099$               $0.13458$

The endpoint correction is never small, and refinement does not improve both the right and left costs simultaneously. The asymmetry exchanges between channels on the fine step, a signature of nonnormal dual geometry.

# Exact range map versus dynamical intertwining

Suppose the branch correspondence orders eigenvector frames $V_c,V_f$ and diagonal eigenvalue matrices $\Lambda_c,\Lambda_f$. Any map $T$ satisfying $TV_c=V_f$ obeys $$\label{eq:dynamics}
 (A_fT-TA_c)V_c=V_f(\Lambda_f-\Lambda_c).$$ Thus exact range transport cannot make the dynamical defect vanish unless the matched eigenvalues agree. In a conditioned norm, the right side gives an unavoidable spectral movement term.

The largest movement is $0.38160$ on the first transition. It falls to about $0.136$ on the second, but remains a visible floor. The Procrustes map optimizes geometry, not dynamics.

# Right and left maps are distinct

For a normal operator one might use one unitary map for both right and left spaces. Here the packet projectors are oblique. Applying Theorem [\[thm:procrustes\]](#thm:procrustes){reference-type="ref" reference="thm:procrustes"} separately gives $H_R$ and $H_L$, with different costs. Nothing in the theorem ensures $$H_L^*H_R=I$$ on biorthogonal packet coordinates. Enforcing that condition would be an oblique, not orthogonal, Procrustes problem and would inherit the large cross-Gram conditioning measured in RH-197.

# An eigenvector-interpolating alternative

Once matched biorthogonal eigenvector frames $V_c,W_c$ and $V_f,W_f$ are known, one may define on the coarse packet $$\label{eq:interpolating-map}
 T_R=V_fW_c^*,\qquad T_L=W_fV_c^*.$$ These maps carry individual labeled right and left vectors exactly when the frames are biorthonormal. They make the spectral defect in [\[eq:dynamics\]](#eq:dynamics){reference-type="eqref" reference="eq:dynamics"} transparent, but their norms inherit oblique conditioning and they are even more endpoint dependent than the orthogonal Procrustes map.

Thus there are at least three distinct optimization targets: smallest orthogonal frame correction, exact labeled-eigenvector interpolation, and smallest dynamical intertwining defect. They coincide only in special normal, spectrally stationary settings. The physical packets do not satisfy those hypotheses.

# Identity audit

Eighty random complex tests use packet ranks two through five, rectangular ambient isometries, and independent endpoint frames. We check both identities in [\[eq:projectors\]](#eq:projectors){reference-type="eqref" reference="eq:projectors"} and equality of the computed residual with [\[eq:cost\]](#eq:cost){reference-type="eqref" reference="eq:cost"}. There are zero failures at tolerance $10^{-10}$; the maximum error over all recorded identities is $3.1415\times10^{-15}$.

# The predictivity gap

The map $H$ is endpoint determined: computing $Q_f^*JQ_c$ requires knowing the fine spectral packet. Therefore it cannot prove that the fine packet exists, predict where it lies, or define an inductive limit without prior spectral information.

This distinguishes two notions:

Retrospective transport

:   align two already computed endpoint packets;

Predictive renormalization

:   construct the fine packet and its error from coarse data and uniform analytic bounds.

RH-205 proves the former and explicitly leaves the latter open.

# Four levels of canonicity

It is useful to reserve separate language for:

1.  existence of some finite packet isomorphism;

2.  the optimal endpoint map relative to a declared ambient embedding;

3.  a map determined from coarse data and the scale parameter;

4.  a uniform map producing a convergent inductive system.

Theorem [\[thm:procrustes\]](#thm:procrustes){reference-type="ref" reference="thm:procrustes"} reaches level two. Gate A requires substantially more than level three because the packet rank must eventually grow.

# Next invariant: physical residues

The branch labels permit one to compare residues without choosing an eigenvector phase. RH-206 asks whether a single scale-dependent scalar can renormalize all four residues or whether a genuinely branch-dependent cocycle is forced. This test is independent of the endpoint partial isometry.

# Claim boundary

The Procrustes theorem and partial-isometry identities are exact. The four physical costs are finite floating measurements. No intrinsic coarse-only map, uniform scale estimate, inductive-limit Hilbert space, Gate-A determinant, or Hilbert--Pólya consequence is obtained.
