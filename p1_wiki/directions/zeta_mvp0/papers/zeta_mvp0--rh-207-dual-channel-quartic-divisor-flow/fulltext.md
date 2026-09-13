---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-207-dual-channel-quartic-divisor-flow"
canonical_tex: "zeta_mvp0/papers/RH-207-dual-channel-quartic-divisor-flow/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-207-dual-channel-quartic-divisor-flow/main.pdf"
source_sha256: "476059c301ecf18ea047f6698aac7b86253b4f7bf51c71b2aa3d4490494ad509"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Dual-Channel Coherence of the Quartic Spectral Divisor Newton Traces and a Nonstationary Small-Noise Flow

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-207-dual-channel-quartic-divisor-flow>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-207-dual-channel-quartic-divisor-flow/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-207-dual-channel-quartic-divisor-flow/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-207-dual-channel-quartic-divisor-flow/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-207-dual-channel-quartic-divisor-flow/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  State and residue transport are unstable under the naive adjacent-level map. This paper tests the basis-invariant object that remains: the monic characteristic polynomial of the source-observable edge quartet.

  At each of $\sigma=0.04,0.02,0.01$, the left and right physical channels produce quartic coefficient vectors agreeing to relative $\ell^2$ error at most $0.008112$. Their constant terms agree to relative errors $0.02716$, $0.01301$, and $0.007749$, respectively. This channel coherence is substantially stronger than the order-one projector and residue transport defects.

  Across scales the divisor is not stationary: adjacent coefficient errors range from $0.24023$ to $0.31674$. We prove that its coefficients and all unweighted power traces are equivalent through Newton identities and verify the reconstruction through power ten on 120 random complex quartets with zero failures. The result identifies a promising scalar flow, not a limit: three levels do not establish coefficient compactness, a renormalization law, a Fredholm determinant, or Gate A.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Dual-Channel Coherence of the Quartic Spectral Divisor\
  Newton Traces and a Nonstationary Small-Noise Flow
```

## Markdown 正文

# Why pass from states to a divisor

RH-202 rejects the direct Haar transport of the outer eigenspaces [@WangRH202], and RH-206 rejects one common scalar for their physical residues [@WangRH206]. Both failures concern coordinate- or source-dependent objects. The multiset of quartet eigenvalues is invariant under similarity and independent of eigenvector normalization.

For an ordered or unordered quartet $\Lambda=\{\lambda_1,\ldots,\lambda_4\}$ define $$\label{eq:divisor}
 D_\Lambda(z)=\prod_{j=1}^4(z-\lambda_j)
 =z^4+c_1z^3+c_2z^2+c_3z+c_4.$$ For two conjugate pairs all $c_j$ are real in exact arithmetic. We call the coefficient vector the finite spectral divisor ledger.

# Similarity and permutation invariance

[\[prop:invariance\]]{#prop:invariance label="prop:invariance"} The coefficients in [\[eq:divisor\]](#eq:divisor){reference-type="eqref" reference="eq:divisor"} are invariant under permutation of the quartet and under similarity of any matrix whose restricted spectrum is $\Lambda$. The constant term is $$\label{eq:det}
 c_4=\prod_{j=1}^4\lambda_j=\det K_\Lambda.$$

This allows the left and right physical channels to be compared without constructing a common eigenvector map.

# Newton trace equivalence

Define the unweighted power sums $$\label{eq:power}
 p_q=\sum_{j=1}^4\lambda_j^q.$$

[\[thm:newton\]]{#thm:newton label="thm:newton"} For $1\le q\le4$, $$\label{eq:newton-low}
 p_q+c_1p_{q-1}+\cdots+c_{q-1}p_1+qc_q=0.$$ For $q>4$, $$\label{eq:newton-high}
 p_q+c_1p_{q-1}+c_2p_{q-2}+c_3p_{q-3}+c_4p_{q-4}=0.$$ Thus the monic quartic determines every finite power trace, and $p_1,\ldots,p_4$ determine the quartic.

These are the Newton--Girard identities applied to the elementary symmetric functions of the roots. The first four equations solve successively for $c_1,\ldots,c_4$; the characteristic equation gives the later recurrence.

This ledger is unweighted. It must not be confused with physical moments $\sum_jr_j\lambda_j^q$, whose residues obey the RH-206 cocycle.

# Three physical quartics

The real coefficient vectors are:

  $\sigma$   side           $c_1$       $c_2$        $c_3$       $c_4$
  ---------- ------- ------------ ----------- ------------ -----------
  $0.04$     left      $-0.06975$   $0.56039$   $-0.07015$   $0.05860$
  $0.04$     right     $-0.07789$   $0.55866$   $-0.07409$   $0.05701$
  $0.02$     left       $0.06254$   $0.55984$   $-0.02530$   $0.30762$
  $0.02$     right      $0.06128$   $0.55822$   $-0.02615$   $0.30362$
  $0.01$     left       $0.04238$   $0.22166$   $-0.06578$   $0.33826$
  $0.01$     right      $0.04295$   $0.22785$   $-0.06733$   $0.33564$

Imaginary coefficient remnants are at roundoff scale because every packet is conjugation closed.

# Left/right channel coherence

For coefficient vectors $c^L,c^R$, record $$\label{eq:error}
 \varepsilon_{LR}=\frac{\left\lVert c^L-c^R\right\rVert_2}{\left\lVert c^L\right\rVert_2}.$$ The three errors are $0.008112$, $0.003851$, and $0.006398$. All lie below one percent.

The constant term discrepancies decrease across the three anchors: $$\label{eq:constant-flow}
 0.02716,\qquad0.01301,\qquad0.007749.$$ This is a descriptive finite trend. It is consistent with the two channels approximating one scalar spectral object, but does not prove that their difference tends to zero.

# Scale flow is not yet converged

Adjacent coefficient-vector errors are:

  step                   left       right
  --------------- ----------- -----------
  $0.04\to0.02$     $0.24023$   $0.24202$
  $0.02\to0.01$     $0.31674$   $0.30955$

Unlike the left/right discrepancy, the scale movement is not small and does not decrease on the finer transition. A raw coefficient limit cannot be inferred from these points.

The coefficient changes also occur in different coordinates: $c_4$ rises strongly from $\sigma=0.04$ to $0.02$, while $c_2$ changes strongly from $0.02$ to $0.01$. Any renormalization should therefore be tested on the full vector rather than fitted to one coefficient.

# Two intrinsic normalization candidates

The divisor itself supplies scale and center statistics. First define the determinant radius $$\label{eq:rho}
 \rho=|c_4|^{1/4}.$$ Under $\lambda_j'=\lambda_j/\rho$, the normalized coefficients are $$\label{eq:radial-coeff}
 c_j'=c_j/\rho^j,$$ so no levelwise regression parameter is introduced.

A second candidate removes translation. Since $\sum_j\lambda_j=-c_1$, the intrinsic center is $$\label{eq:center}
 \mu=-c_1/4.$$ Translate $\lambda_j\mapsto\lambda_j-\mu$ and divide by the centered root mean square radius. The resulting cubic coefficient vanishes exactly, and the quadratic energy is normalized. These two formulas are predeclared candidates for RH-212; neither is claimed to improve the present data until tested on denser anchors.

# Machine audit of Newton equivalence

For 120 random complex quartets we form the monic polynomial, reconstruct $p_1,\ldots,p_{10}$ with [\[eq:newton-low\]](#eq:newton-low){reference-type="eqref" reference="eq:newton-low"}--[\[eq:newton-high\]](#eq:newton-high){reference-type="eqref" reference="eq:newton-high"}, and compare with direct sums of powers. The maximum floating error is below the declared $10^{-8}$ gate and all cases pass. This verifies that the archived coefficient and trace ledgers use one exact algebraic convention.

# A scalar route and its requirements

The finite evidence suggests studying a map $$\label{eq:flow}
 c(\sigma)\longmapsto c(\sigma/2)$$ before insisting on convergence of raw projectors. A successful Gate-A argument would need at least:

1.  denser small-noise anchors and a predeclared branch rule;

2.  compactness or a contraction after intrinsic coefficient renormalization;

3.  control of omitted modes as the packet grows;

4.  convergence of finite determinants on a common complex domain;

5.  only then, a Fredholm or dynamical determinant interpretation.

The present quartic is a local test block and can never by itself produce an infinite spectral counting law.

# From one quartic to a determinant family

Suppose later contours select packets $\Lambda_{\sigma,k}$ of growing size. A meaningful determinant limit requires more than coefficientwise convergence at fixed $k$: the finite products must form a normal family on a common domain, and tails must be controlled uniformly in both $\sigma$ and $k$. Canonical products or regularized determinants may be required when ordinary products diverge [@Simon2005]. RH-207 supplies only the $k=4$ laboratory in which candidate normalizations can be falsified cheaply.

# What is not encoded

The divisor contains eigenvalues with multiplicity, but not the physical source residues, projector conditioning, or eigenvectors. It has no established arithmetic weights. In particular, the Newton traces here are not von Mangoldt traces, and the roots are not identified with zeta zeros.

# Claim boundary and next step

Similarity invariance and Newton equivalence are exact. Channel coherence and scale movement are finite floating observations at three levels. No coefficient limit, Fredholm determinant, $T\log T$ count, Gate A, or later macro gate is claimed. RH-208 next separates endpoint spectral isolation from the much harder certification of interlevel transport.
