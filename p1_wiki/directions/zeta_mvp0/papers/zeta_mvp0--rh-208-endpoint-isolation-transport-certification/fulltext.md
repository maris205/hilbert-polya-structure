---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-208-endpoint-isolation-transport-certification"
canonical_tex: "zeta_mvp0/papers/RH-208-endpoint-isolation-transport-certification/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-208-endpoint-isolation-transport-certification/main.pdf"
source_sha256: "6b8e9bf608674b8dd11508eeecf7caba79d91b5d88a6a1f0323fc89a7afb6813"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Endpoint Isolation Versus Interlevel Transport Certification A Conditioning-Scaled Feasibility Audit for the Edge Quartet

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-208-endpoint-isolation-transport-certification>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-208-endpoint-isolation-transport-certification/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-208-endpoint-isolation-transport-certification/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-208-endpoint-isolation-transport-certification/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-208-endpoint-isolation-transport-certification/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Validated Riesz projectors and validated cross-level transport are different tasks. This paper separates them before an expensive interval computation. For a computed simple eigenpair we record the local condition number $\kappa=\|v\|\|w\|/|w^*v|$, residual $\eta=\|Av-\lambda v\|$, spectral separation $\delta$, and feasibility ratio $$\beta=2\kappa\eta/\delta.$$

  At each of six physical scale/channel endpoints, every outer-quartet mode has $\beta<1$ by more than twelve orders of magnitude; the largest endpoint ratio is $3.25\times10^{-13}$. This indicates that a dedicated interval eigenpair or contour validation is numerically plausible.

  Using the Haar lift of a coarse eigenvector as an approximate fine eigenvector gives the opposite result. Across four adjacent cases the minimum conditioning-scaled transport ratio is $3.3486$ and the maximum is $29.4916$; no case has all four ratios below one. Thus endpoint isolation should be validated directly, while the naive interlevel homotopy should not be expected to close. The ratios are floating feasibility diagnostics, not interval certificates; no validated projector is claimed.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Endpoint Isolation Versus Interlevel Transport Certification\
  A Conditioning-Scaled Feasibility Audit for the Edge Quartet
```

## Markdown 正文

# Two certification problems

The local problem asks whether a quartet at one finite endpoint is isolated and has the advertised rank. The transport problem asks whether a predeclared coarse packet map stays inside the corresponding fine spectral cluster. The second requires the first plus an interlevel perturbation estimate.

RH-203 expresses this distinction exactly through $$\label{eq:riesz-transport}
 P_fJ-JP_c=\frac{1}{2\pi i}\int_\Gamma
 R_f(z)(A_fJ-JA_c)R_c(z)\,dz$$ [@WangRH203]. The present paper asks whether the floating scales in this formula are even compatible with a sharp validated calculation.

# Local condition and residual

For a simple right/left eigenpair of a nonnormal matrix, define $$\label{eq:kappa}
 \kappa(\lambda)=\frac{\left\lVert v\right\rVert_2\left\lVert w\right\rVert_2}{|w^*v|}.$$ This quantity is invariant under separate nonzero scalings of $v,w$ and is the norm of the rank-one spectral projector under biorthogonal normalization [@StewartSun1990; @TrefethenEmbree2005].

For a computed pair $(\widehat\lambda,\widehat v)$ let $$\label{eq:residual}
 \eta=\left\lVert A\widehat v-\widehat\lambda\widehat v\right\rVert_2,
 \qquad
 \delta=\min_{\mu\ne\widehat\lambda}|\widehat\lambda-\mu|.$$ The dimensionless ratio $$\label{eq:beta}
 \beta=\frac{2\kappa\eta}{\delta}$$ compares the conditioning-amplified residual with half the observed separation.

The inequality $\beta<1$ is used here as a feasibility gate, not as a standalone validated eigenvalue theorem. A proof still needs outward-rounded matrix data and an appropriate interval, Krawczyk, Schur, or contour argument. Conversely, $\beta\gg1$ warns that this particular residual budget cannot separate the mode.

# Endpoint result

The maximum ratio and largest local condition in each endpoint packet are:

  $\sigma$   side      max $\beta_{\rm endpoint}$   max $\kappa$
  ---------- ------- ---------------------------- --------------
  $0.04$     left            $3.25\times10^{-13}$        $31.46$
  $0.04$     right           $3.11\times10^{-13}$        $30.69$
  $0.02$     left            $1.09\times10^{-13}$         $8.39$
  $0.02$     right           $7.20\times10^{-14}$         $8.40$
  $0.01$     left            $1.63\times10^{-13}$        $17.54$
  $0.01$     right           $2.30\times10^{-13}$        $17.69$

All 24 endpoint mode records are deep inside the feasibility gate. The projectors are nonnormal but not so ill conditioned that double-precision eigenpair residuals consume the spectral separation.

This supports a targeted validation strategy: enclose each input matrix, validate four simple endpoint eigenpairs or one rank-four contour, and then form outward projector/residue bounds locally.

# Lifted coarse modes as fine approximants

Let $(\lambda_c,v_c)$ be a coarse mode and $J$ the Haar embedding. Its fine residual at the unchanged eigenvalue is $$\label{eq:lifted-residual}
 \eta_{c\to f}=\left\lVert A_fJv_c-\lambda_cJv_c\right\rVert_2.$$ This residual includes both eigenvalue motion and eigenspace rotation. We scale it by the condition and separation of the matched fine mode using [\[eq:beta\]](#eq:beta){reference-type="eqref" reference="eq:beta"}.

  step            side      min $\beta_{c\to f}$   max $\beta_{c\to f}$
  --------------- ------- ---------------------- ----------------------
  $0.04\to0.02$   left                   $7.793$               $20.990$
  $0.04\to0.02$   right                  $3.349$                $3.730$
  $0.02\to0.01$   left                  $12.015$               $29.492$
  $0.02\to0.01$   right                  $5.982$               $13.856$

Every transported mode fails the unit feasibility gate. This agrees with the order-one subspace angles of RH-202 and shows that the issue is not roundoff error in the endpoint eigendecomposition.

# Why endpoint validation can succeed while transport fails

The endpoint residual is generated by solving the fine eigenproblem itself and is near machine precision. The transported residual tests a physical hypothesis about how two different operators are related. There is no reason for it to be small unless a renormalization theorem enforces that relationship.

Thus the logical implication is one-way: $$\text{good interlevel certificate}
 \Longrightarrow \text{isolated endpoints},$$ but isolated endpoints do not imply a good Haar transport certificate.

# Avoiding the full eigenvector condition number

The physical bulk matrices contain removed peripheral directions and highly clustered interior modes. The condition number of a complete eigenvector matrix can be enormous and is not the right local quantity for one isolated simple mode. We therefore use the rank-one projector condition [\[eq:kappa\]](#eq:kappa){reference-type="eqref" reference="eq:kappa"}. A validated contour method would similarly estimate the resolvent only on the selected contour rather than diagonalize the complete operator.

# Recommended validated workflow

The finite audit supports the following order:

1.  enclose the six finite input matrices with outward rounding;

2.  validate endpoint quartet counts and separations independently;

3.  enclose local Riesz projectors and residues;

4.  do not spend interval effort on the unmodified Haar homotopy;

5.  first derive a smaller-defect renormalized map or move to a scalar divisor formulation.

This makes validation proportional to the evidence rather than using an expensive contour computation to rescue a map already contradicted by order-one residuals.

# Three possible endpoint validators

There are several compatible rigorous implementations:

1.  an interval Newton or Krawczyk argument for each simple eigenpair, including a normalization equation for the eigenvector;

2.  a validated Schur decomposition followed by cluster separation and a Sylvester-equation projector enclosure;

3.  an argument-principle or contour-resolvent computation validating the rank-four cluster as a whole.

The third route avoids labeling individual conjugate modes, while the first connects most directly to residue enclosures. A complete implementation must include rounding error in constructing the physical matrices, not only the error of the eigensolver applied to already rounded input.

The endpoint ratios suggest that all three methods have numerical room. The transport ratios show that none should use the Haar-lifted coarse vector as a tight initial enclosure for the fine eigenvector.

# Claim boundary

All $\beta$ values use floating eigenvalues, vectors, and separations. They are feasibility indicators only. No interval matrix enclosure, Krawczyk proof, validated contour rank, or validated Riesz projector appears here. The endpoint result is positive evidence for such work; the transport result is a finite negative for the naive map. Gate A remains open.

# Next question

One possible response is to enlarge the outer quartet into a larger modulus-selected cloud. RH-209 tests ranks $2$ through $32$ on every adjacent case. If larger clouds absorb the rotating directions, their principal angles should improve; if not, the selection rule itself must change.
