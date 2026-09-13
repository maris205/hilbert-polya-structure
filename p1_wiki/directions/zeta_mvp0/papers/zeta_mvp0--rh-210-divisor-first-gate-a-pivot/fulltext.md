---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-210-divisor-first-gate-a-pivot"
canonical_tex: "zeta_mvp0/papers/RH-210-divisor-first-gate-a-pivot/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-210-divisor-first-gate-a-pivot/main.pdf"
source_sha256: "58a47ce6809b2682ea4cda5775f2ccf1896d6bf16f397e51683ad22c178a80c4"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Divisor-First Pivot Inside Gate A Why Raw Projector Transport Is Sufficient but Not Necessary

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-210-divisor-first-gate-a-pivot>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-210-divisor-first-gate-a-pivot/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-210-divisor-first-gate-a-pivot/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-210-divisor-first-gate-a-pivot/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-210-divisor-first-gate-a-pivot/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-202--RH-209 produce a split verdict. The edge quartet has unique conjugate branch labels and a coherent left/right quartic divisor, but naive Haar transport fails for fixed and enlarged packets, and physical residues do not share one scalar renormalization. This paper determines the logical route consequence.

  We prove by an explicit rotating-similarity family that a spectral divisor can remain exactly fixed while a selected Riesz projector moves by operator norm one. Thus convergence of raw projectors is a sufficient route to a scalar determinant, but not a necessary condition for divisor stability. An 81-angle audit keeps the characteristic coefficients fixed within $2.84\times10^{-16}$ while the projector distance reaches one.

  The physical evidence supports a divisor-first research order: preserve the finite conjugate branch labels, densify and renormalize the quartic coefficient flow, and keep the source-dependent residue cocycle in a separate weighted ledger. This is a pivot within Gate A, not its closure. No coefficient limit, growing-cloud determinant, Fredholm realization, Hilbert--Pólya operator, or zeta-zero statement is obtained.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  A Divisor-First Pivot Inside Gate A\
  Why Raw Projector Transport Is Sufficient but Not Necessary
```

## Markdown 正文

# The route decision forced by the batch

The preceding layers establish four finite facts:

1.  the naive Haar projector map has defect above one [@WangRH202];

2.  all four conjugate branch assignments are unique [@WangRH204];

3.  the left/right quartic coefficient discrepancy is below one percent [@WangRH207];

4.  increasing the top-modulus cloud to rank 32 does not repair the two-sided angle [@WangRH209].

These facts do not say that the spectral direction is wrong. They say that one specific state-space realization is not the stable object visible in the current data.

# A precise distinction

Let $A_n$ be finite operators, $P_n$ selected Riesz projectors, and $$\label{eq:divisor}
 D_n(z)=\det(zI-A_n|_{\operatorname{Ran}P_n}).$$ If transported restricted operators converge in trace norm, then their finite determinants converge on compact sets under standard hypotheses [@Simon2005]. Hence strong state/operator transport is a sufficient route.

The converse is false: determinants discard eigenvector geometry. The next theorem records this elementary but strategically important point.

# Rotating-projector counterexample

Let $$\label{eq:rotation}
 U_\theta=\begin{pmatrix}\cos\theta&-\sin\theta\\
 \sin\theta&\cos\theta\end{pmatrix},\qquad
 D=\begin{pmatrix}0.7&0\\0&-0.2\end{pmatrix},$$ and define $$\label{eq:family}
 A_\theta=U_\theta DU_\theta^*,\qquad
 P_\theta=U_\theta\begin{pmatrix}1&0\\0&0\end{pmatrix}U_\theta^*.$$

[\[thm:counterexample\]]{#thm:counterexample label="thm:counterexample"} For every $\theta$, $$\label{eq:fixed-divisor}
 \det(zI-A_\theta)=(z-0.7)(z+0.2),$$ while $$\label{eq:projector-drift}
 \left\lVert P_\theta-P_0\right\rVert_2=|\sin\theta|.$$ In particular the divisor is constant and the projector distance reaches one at $\theta=\pi/2$.

Unitary similarity preserves the characteristic polynomial. Direct calculation of the two rank-one orthogonal projectors gives singular values $|\sin\theta|$ for their difference.

The example is normal and therefore does not exploit nonnormal instability. It shows that the logical non-necessity is fundamental.

# Machine realization of the counterexample

We sample 81 equally spaced angles from $0$ to $\pi/2$. The maximum coefficient-vector drift is $2.8306\times10^{-16}$, while the maximum projector distance is exactly one to displayed precision. This audit tests the route logic and implementation; Theorem [\[thm:counterexample\]](#thm:counterexample){reference-type="ref" reference="thm:counterexample"} itself is exact.

# Physical evidence vector

The route audit imports the following predeclared facts:

  finite diagnostic                                           value
  ---------------------------------------------- ------------------
  largest naive Haar packet sine                          $0.82388$
  largest oblique-projector defect                        $2.29068$
  unique adjacent branch assignments                          $4/4$
  largest left/right quartic coefficient error           $0.008112$
  largest common-scalar residue residual                  $0.99985$
  endpoint isolation feasibility cases                        $6/6$
  naive transport feasibility cases                           $0/4$
  expanded-cloud angle-gate cases                  $0/24$ for $k>4$

The scalar divisor is the only tested object combining basis invariance with dual-channel coherence. It is therefore the most economical next target.

# Three ledgers, not one

We separate the program into:

Divisor ledger $Q$

:   Eigenvalue multisets, monic coefficients, and unweighted Newton traces.

State ledger $R$

:   Right/left Riesz spaces, projectors, interlevel maps, and conditioning.

Transfer ledger $W$

:   Source--observation residues and weighted physical moments.

The current data support finite $Q$, diagnose difficulties in $R$, and show that $W$ requires a branch-dependent cocycle. None should be silently substituted for another.

# The divisor-first route

The revised order inside Gate A is:

1.  retain the unique two-branch labels as the finite identity rule;

2.  sample additional small-noise levels and both physical channels;

3.  test intrinsic normalizations or recurrences for the full quartic coefficient vector;

4.  determine whether a growing family of divisors is normal and locally uniform on a fixed complex domain;

5.  only then seek a Fredholm/dynamical determinant realization;

6.  return to state transport when such a realization specifies the right renormalized coordinates.

This is not permission to ignore operators permanently. A dynamical determinant ultimately needs trace-class, nuclear, symbolic, or equivalent analytic structure. The pivot only postpones an unsupported raw-projector inductive limit.

# Why the fixed quartic is insufficient

Even perfect convergence of one quartic would produce four limiting roots, not a spectrum with a $T\log T$ count. Gate A requires a growing cloud and control of omitted factors. The quartet is useful as:

1.  a local branch-continuation seed;

2.  a test of dual-channel universality;

3.  a laboratory for coefficient renormalization;

4.  a finite factor in a possible later determinant product.

It is not the final determinant.

# What would falsify the pivot

The divisor-first route should be abandoned or revised if denser levels show any of:

1.  loss of the branch labels or edge separation;

2.  persistent left/right coefficient disagreement;

3.  no compactness under any intrinsic predeclared normalization;

4.  uncontrolled factor proliferation that destroys local uniformity;

5.  dependence of the divisor on source/observation choices.

Negative outcomes would still classify the finite quartet correctly as a local diagnostic.

# Route coordinate and claim boundary

The resulting coordinate is $$\boxed{\texttt{finite\_dual\_channel\_divisor\_flow\_open\_renormalization}}.$$ Gate A is open. Gates B--E remain untouched. The paper proves only a logical non-necessity theorem and records a finite evidence-based research order. It constructs no limiting divisor, Fredholm determinant, self-adjoint operator, arithmetic trace identity, zeta divisor, or RH proof.
