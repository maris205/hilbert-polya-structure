---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-200-conjugate-pair-edge-quartet-selection"
canonical_tex: "zeta_mvp0/papers/RH-200-conjugate-pair-edge-quartet-selection/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-200-conjugate-pair-edge-quartet-selection/main.pdf"
source_sha256: "784e2965e1b6a78c8aefa61201a0c350d92f3a439c1f6a7a7b566a5d4e30d72a"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Conjugate-Pair Parity and Edge-Quartet Selection A Finite Cross-Scale Canonicity Test for the Physical Packet

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-200-conjugate-pair-edge-quartet-selection>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-200-conjugate-pair-edge-quartet-selection/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-200-conjugate-pair-edge-quartet-selection/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-200-conjugate-pair-edge-quartet-selection/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-200-conjugate-pair-edge-quartet-selection/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The preceding papers identify a genuine four-mode source--observation packet at $\sigma=0.01$, but its selection was initially phrased as a match to post hoc physical eigenvalues. This paper asks whether a simpler dynamical rule selects the same object.

  Because the physical matrices are real, every nonreal simple eigenvalue is paired with its complex conjugate. If the outer spectral edge consists of four nonreal modes separated from the fifth modulus, its real invariant packet must have even dimension and, in the present geometry, exactly four dimensions. We therefore select the four largest-modulus source-observable modes.

  At scales $\sigma=0.04,0.02,0.01$ and on both physical channels, the four outer modes form two conjugate pairs, all have nonzero source--observation residue, and the radial gap after the quartet is positive. The minimum gap over six cases is $0.05949$. The length-three RH-185 candidates have zero two-sided passes at all audited scales, while the finest length-four branch has twelve.

  This supplies a finite selection principle and explains the parity mismatch of the odd clock branch. It is not a uniform edge-gap theorem, not a proof that every scale has a quartet, and not an arithmetic prime-pair or zeta identification.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Conjugate-Pair Parity and Edge-Quartet Selection\
  A Finite Cross-Scale Canonicity Test for the Physical Packet
```

## Markdown 正文

# Why selection matters

RH-194 matched the four temporal roots to four physical eigenvalues after the temporal windows had been selected. This is strong evidence, but a post hoc match is not a canonical dynamical definition. A route toward Gate A needs a rule stated before matching.

Two physical symmetries are available:

1.  the matrices at the audited levels are real, so complex modes occur in conjugate pairs;

2.  the temporal packet is intended to describe the outer spectral edge, not an arbitrary interior cloud.

Together they suggest an outer-edge quartet rule.

# Conjugation parity

Let $A\in\mathbb R^{n\times n}$. If $Av=\lambda v$, then $A\overline v=\overline\lambda\,\overline v$. Algebraic Riesz projectors obey $$\label{eq:projector-conjugation}
 P_{\overline\lambda}=\overline{P_\lambda}$$ for simple conjugate modes [@Kato1995].

[\[thm:parity\]]{#thm:parity label="thm:parity"} Let $\Lambda$ be a finite isolated spectral set of a real matrix, invariant under complex conjugation and containing no real eigenvalues. Then the algebraic rank of its Riesz projector is even. In the simple-spectrum case the modes can be partitioned into conjugate pairs.

Conjugation is an antilinear bijection from the eigenspace at $\lambda$ to the eigenspace at $\overline\lambda$. Since $\Lambda$ contains no real points, its elements split into disjoint two-element conjugate orbits, with equal algebraic multiplicities.

A real packet of odd dimension may contain real modes. It cannot, however, be a conjugation-closed packet consisting only of nonreal edge modes. This is the relevant obstruction to a length-three approximation of two pairs.

# Outer-edge rule

Order the eigenvalues by modulus: $$\label{eq:modulus-order}
 |\lambda_1|\ge|\lambda_2|\ge\cdots\ge|\lambda_n|.$$ Suppose $$\label{eq:edge-gap}
 |\lambda_4|>|\lambda_5|,$$ and the first four eigenvalues are nonreal and conjugation closed.

[\[prop:edge\]]{#prop:edge label="prop:edge"} Under these hypotheses the outer four-mode Riesz set is uniquely defined by the modulus edge, is conjugation invariant, and has no three-dimensional conjugation-closed subpacket containing all outer modes. If the four modes have nonzero source-observation residues, the associated canonical packet is four-dimensional and exactly source-observable.

The rule is basis-free and does not use the temporal roots. It can fail if the edge gap closes, a real eigenvalue enters the edge, or a residue vanishes.

# Three-scale physical audit

We recompute the base spectra at $\sigma=0.04,0.02,0.01$ for both physical channels. The top four modes are always two conjugate pairs. The radial gap after the quartet is:

  scale       side   $|\lambda_4|-|\lambda_5|$   minimum quartet residue
  -------- ------- --------------------------- -------------------------
  $0.04$      left                   $0.06129$                  positive
  $0.04$     right                   $0.05949$                  positive
  $0.02$      left                   $0.32537$                  positive
  $0.02$     right                   $0.32745$                  positive
  $0.01$      left                   $0.11341$                  positive
  $0.01$     right                   $0.11766$                  positive

The maximum conjugate-pair mismatch in all six cases is below $2\times10^{-15}$ in the floating computation, as expected from real input data.

The selected moduli illustrate the branch: $$\begin{aligned}
\sigma=0.04:&\quad 0.6735,0.6735,0.3595,0.3595,\ldots,\\
\sigma=0.02:&\quad 0.7723,0.7723,0.7181,0.7181,\ldots,\\
\sigma=0.01:&\quad 0.7937,0.7937,0.7328,0.7328,\ldots.\end{aligned}$$ The gap is finite at every audited level, although it is not monotone in $\sigma$.

# Parity versus the length-three clock

The RH-185 candidate lengths are predeclared by the finite clock-rank rule. The observed gate counts are:

  scale      length   windows   two-sided passes
  -------- -------- --------- ------------------
  $0.04$          3        18                  0
  $0.02$          3        30                  0
  $0.01$          3        40                  0
  $0.01$          4        38                 12

This does not prove that every length-three construction must fail. It does show that the audited failures are consistent with a structural mismatch: the outer physical object is two nonreal conjugate pairs, while a three-dimensional real conjugation-closed packet cannot contain it.

The length-four success at the finest scale selects the same quartet as the outer-edge rule. RH-194 then shows that its roots match the physical modes.

# Canonicity and remaining dependence

The rule "four largest-modulus source-observable modes" is more intrinsic than "the four modes nearest the temporal roots." It uses only the physical operator, source/observation visibility, and an outer edge.

It is not yet fully canonical in the infinite program. One must prove:

1.  a uniform edge gap or a controlled cluster contour;

2.  stability of source-observation residues;

3.  compatibility of the edge rule under refinement and renormalization;

4.  a relation between this finite edge packet and the later cloud ledger.

The present three-scale audit supports, but does not establish, these claims.

# What the parity result does not say

The conjugate-pair theorem is elementary and local. It does not say that the edge quartet is a prime pair, that its phases encode prime gaps, or that its eigenvalues are zeta zeros. Those interpretations would require new arithmetic trace identities and are not present here.

Likewise, the failure of the length-three finite windows is not an all-level no-go theorem. A different odd packet could include a real mode, use a non-real coordinate convention, or target a different spectral region.

# Updated route

The ten-paper batch now has a coherent finite branch: $$\begin{gathered}
 \text{outer edge + conjugation parity}
 \longrightarrow\text{source-observable quartet}\\
 \longrightarrow\text{balanced exact packet}
 \longrightarrow\text{temporal determinant/trace ledger}.
 \end{gathered}$$ The next barrier is no longer identifying a local quartet. It is proving that the edge rule and its channel weights survive refinement and can be assembled into an intrinsic object. That is still Gate A; Gates B--E, Hilbert--Pólya, and RH remain untouched.
