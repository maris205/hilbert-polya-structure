---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-204-conjugate-branch-correspondence"
canonical_tex: "zeta_mvp0/papers/RH-204-conjugate-branch-correspondence/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-204-conjugate-branch-correspondence/main.pdf"
source_sha256: "11d34dd4f6d51fb09e088f6536201890c158e1b2537cd8fdc3665eff99782697"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Conjugate-Branch Correspondence Across Small-Noise Levels A Spectral Positive Surviving the State-Transport Obstruction

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-204-conjugate-branch-correspondence>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-204-conjugate-branch-correspondence/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-204-conjugate-branch-correspondence/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-204-conjugate-branch-correspondence/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-204-conjugate-branch-correspondence/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The naive Haar transport of outer-edge eigenspaces fails in RH-202, but this does not imply that the spectral branches themselves lose identity. For a real operator, a nonreal quartet is determined by its two upper-half-plane representatives. We order those representatives by real part and compare the direct and swapped assignments at adjacent noise scales.

  All four scale/channel cases have a unique direct correspondence. The minimum pointwise assignment margin is $0.08884$ and the minimum total-cost margin is $0.28813$. On the finer $0.02\to0.01$ step the pointwise margin increases beyond $0.714$. The same negative-real and positive-real branch labels work on both physical channels. At a fixed scale, the largest left/right mismatch of a branch representative is only $0.007578$.

  The maximum adjacent displacement decreases descriptively from about $0.382$ to $0.136$, a ratio at most $0.3581$. With only two transitions this is not a convergence law. The result establishes a finite spectral correspondence that is substantially more stable than raw eigenvector or Riesz-projector transport and provides the labels needed for later residue and divisor flows.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Conjugate-Branch Correspondence Across Small-Noise Levels\
  A Spectral Positive Surviving the State-Transport Obstruction
```

## Markdown 正文

# Why a weaker invariant is useful

RH-202 compares full right and left packet spaces and obtains principal sines above $0.82$ [@WangRH202]. RH-203 explains this through an exact intertwining identity: state transport depends on operator, resolvent, source, and observation defects simultaneously [@WangRH203].

Eigenvalues are less demanding objects. They can possess a coherent branch label even when the associated nonnormal projectors move substantially. This paper asks only whether the two conjugate pairs can be followed without using temporal roots or an eigenvector gauge.

# Conjugate reduction

Let $A$ be real and let $\Lambda$ be an isolated quartet of simple nonreal eigenvalues. Then $$\label{eq:quartet}
 \Lambda=\{a_-,\overline{a_-},a_+,\overline{a_+}\},
 \qquad \operatorname{Im}a_\pm>0.$$ We label the representatives so that $$\label{eq:order}
 \operatorname{Re}a_-<\operatorname{Re}a_+.$$

[\[prop:reduction\]]{#prop:reduction label="prop:reduction"} For conjugation-closed simple nonreal quartets, a bijection between the two upper-half-plane representatives determines a unique conjugation-compatible bijection of the full quartets.

Map the conjugate of each representative to the conjugate of its image. Since no representative is real, the two conjugate orbits are disjoint and the extension is unique.

The reduction removes arbitrary ordering of the four eigensolver outputs and makes the matching problem two-dimensional.

# Assignment criterion and margin

For coarse representatives $a_-,a_+$ and fine representatives $b_-,b_+$, define $$\begin{aligned}
\label{eq:costs}
 C_{\rm dir}&=|a_--b_-|+|a_+-b_+|,\\
 C_{\rm swap}&=|a_--b_+|+|a_+-b_-|.\end{aligned}$$ The direct assignment is the unique minimum-cost matching if $$\label{eq:margin}
 M=C_{\rm swap}-C_{\rm dir}>0.$$ We also record the stronger pointwise margin $$\label{eq:pointwise}
 m=\min\bigl\{|a_--b_+|-|a_--b_-|,
 |a_+-b_-|-|a_+-b_+|\bigr\}.$$

[\[prop:robust\]]{#prop:robust label="prop:robust"} If $m>0$, each coarse branch has its direct fine branch as unique nearest neighbor. Perturbing every one of the four representatives by less than $m/4$ preserves the signs of both pointwise comparisons.

Each distance changes by at most the sum of its endpoint perturbations, hence by less than $m/2$. The difference of a wrong and correct distance changes by less than $m$, so a strictly positive original margin remains positive.

This is a finite stability statement. It does not identify analytic eigenvalue branches in the sense of Kato [@Kato1995] because the operators live on changing dimensions.

# Adjacent-scale result

The four audited cases are:

  step            side      $|\Delta a_-|$   $|\Delta a_+|$         $M$         $m$
  --------------- ------- ---------------- ---------------- ----------- -----------
  $0.04\to0.02$   left           $0.32821$        $0.38105$   $0.28813$   $0.09014$
  $0.04\to0.02$   right          $0.32726$        $0.38160$   $0.29001$   $0.08884$
  $0.02\to0.01$   left           $0.11977$        $0.13643$   $1.46722$   $0.71671$
  $0.02\to0.01$   right          $0.11841$        $0.13458$   $1.46117$   $0.71441$

Every direct assignment is unique under both criteria. The dramatic growth of the margin on the finer transition results from increased separation between the two branches: their distance grows from about $0.74$ at $\sigma=0.02$ to about $0.97$ at $\sigma=0.01$.

# Endpoint branch geometry

For reference, the upper-half-plane representatives are:

  $\sigma$   side                    $a_-$                $a_+$
  ---------- ------- --------------------- --------------------
  $0.04$     left      $-0.05937+0.67084i$   $0.09424+0.34688i$
  $0.04$     right     $-0.05817+0.67300i$   $0.09711+0.33987i$
  $0.02$     left      $-0.38757+0.66804i$   $0.35630+0.62352i$
  $0.02$     right     $-0.38536+0.66674i$   $0.35472+0.62140i$
  $0.01$     left      $-0.49683+0.61899i$   $0.47564+0.55740i$
  $0.01$     right     $-0.49427+0.62026i$   $0.47280+0.55682i$

The negative-real branch changes mainly in real part, while its imaginary part varies more slowly. The positive-real branch moves in both coordinates on the first transition and then settles closer to the negative branch's imaginary scale. These observations motivate a two-dimensional complex normalization rather than a fit based only on modulus.

# Dual-channel synchronization

The left physical operator acts on the fine bulk, while the right operator is built from the transposed coarse bulk. Agreement between them is therefore a nontrivial finite consistency check.

  $\sigma$     negative-real branch   positive-real branch      maximum
  ---------- ---------------------- ---------------------- ------------
  $0.04$                 $0.002468$             $0.007578$   $0.007578$
  $0.02$                 $0.002561$             $0.002642$   $0.002642$
  $0.01$                 $0.002857$             $0.002902$   $0.002902$

The common real-order labels survive on both channels at all three scales. The discrepancy is one to two orders of magnitude below the interlevel branch movement.

# Descriptive contraction and its limit

For each side, divide the maximum $0.02\to0.01$ displacement by the maximum $0.04\to0.02$ displacement. The ratios are below $0.359$. This is an encouraging finite trend, but two increments cannot establish geometric convergence, differentiability in $\sigma$, or even monotonicity at the next scale.

A future theorem would need a family $A_\sigma$ in common renormalized coordinates and a uniform separated-cluster estimate. Neither is supplied here.

# Relation to the projector obstruction

There is no contradiction between unique eigenvalue matching and large projector angles. For nonnormal matrices, eigenvectors and Riesz projectors can be much more sensitive than eigenvalues [@StewartSun1990]. In the present data: $$\text{branch mismatch across channels}<0.008,
 \qquad
 \text{Haar packet sine}>0.82.$$ The stable object may therefore be a scalar divisor or branch ledger rather than a directly embedded eigenspace.

# What the branch labels enable

The correspondence fixes the ordering needed to study:

1.  endpoint-determined optimal maps between packet spaces;

2.  branchwise residue multipliers and their conjugation symmetry;

3.  scale evolution of the real quartic characteristic polynomial;

4.  denser small-noise samples without post hoc root matching.

RH-205 next constructs the best endpoint partial isometry and distinguishes existence of a shell map from predictivity of that map.

# How to extend the correspondence audit

A denser experiment should freeze the labels by continuation from the nearest already accepted anchor, then check the assignment margin before recording any coefficient fit. If the pointwise margin changes sign, the branch should be declared ambiguous rather than relabeled to preserve a desired trend. Real modes entering the edge or closure of the fourth/fifth radial gap are separate failure events and must also be logged.

# Claim boundary

The ordering and assignment propositions are exact. Their physical input is a finite floating eigendecomposition at three scales. No all-level edge gap, analytic branch continuation, eigenvalue limit, arithmetic meaning, or zeta-zero correspondence is asserted. Gate A remains open.
