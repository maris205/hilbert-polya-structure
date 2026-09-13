---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-223-shell-complete-edge-selection-stability"
canonical_tex: "zeta_mvp0/papers/RH-223-shell-complete-edge-selection-stability/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-223-shell-complete-edge-selection-stability/main.pdf"
source_sha256: "b9b1a5d374e254f6a0e48f5cc92e70575e5184960e6d67d592865e07896e5567"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Shell-Complete Edge Selection and Candidate-Window Stability Why Fixed-Cardinality Spectral Prefixes Break Real Symmetry

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-223-shell-complete-edge-selection-stability>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-223-shell-complete-edge-selection-stability/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-223-shell-complete-edge-selection-stability/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-223-shell-complete-edge-selection-stability/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-223-shell-complete-edge-selection-stability/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-222 constructs rank-growing resonance clouds by grouping the resolved spectrum of a real operator into real singleton shells and nonreal conjugate pair shells. This paper determines whether that completion is necessary and whether it depends on the Arnoldi candidate margin.

  A naive prefix containing exactly the target number of largest-modulus roots fails conjugate closure at 23 of 32 physical endpoints, despite every target rank being even. Real roots entering before a cutoff change the parity of the number of nonreal slots, so even cardinality is not a conjugacy criterion.

  We prove that the first union of complete radial shells whose cumulative size reaches a target is the minimal shell-complete radial prefix. Its overshoot is at most one. If the gap after its last shell is positive, it is unique within the resolved radial ordering. In the physical atlas, 23 endpoints require one-root overshoot, every resolved gap is positive, and candidate prefixes with margins $4,8,12,14$ recover the reference cloud with zero multiset matching error.

  The theorem is exact for a supplied finite spectral multiset. The numerical audit does not interval-certify Arnoldi eigenvalues or prove a canonical all-level rank schedule. It supplies a stable finite selection layer for the global-cloud analysis that follows.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Shell-Complete Edge Selection and Candidate-Window Stability\
  Why Fixed-Cardinality Spectral Prefixes Break Real Symmetry
```

## Markdown 正文

# The cutoff problem

Let a real matrix have resolved roots ordered by modulus. A common edge-cloud rule is to take the first $k$ roots. This is safe only if the cutoff lands after a complete conjugate pair. Even $k$ does not ensure that condition: real roots contribute one slot, whereas nonreal pairs contribute two.

RH-222 avoids the problem by selecting radial shells [@WangRH222]. Here we isolate the finite theorem behind that rule and test its dependence on how far the eigensolver is asked to look.

# Ordered shells

Let $\Sigma$ be a finite conjugate-closed multiset. Partition it into shells $$S_1,\ldots,S_m,\qquad |S_j|\in\{1,2\},$$ where a singleton is real and a two-element shell is $\{\lambda,\overline\lambda\}$. Order the shells by nonincreasing radius $$\rho_j=\max_{\lambda\in S_j}|\lambda|.$$ For target $k$, define $$\label{eq:index}
 J(k)=\min\left\{j:\sum_{\ell=1}^{j}|S_\ell|\ge k\right\},
 \qquad
 \mathcal C_k=\bigcup_{\ell=1}^{J(k)}S_\ell.$$

[\[thm:minimal\]]{#thm:minimal label="thm:minimal"} The cloud $\mathcal C_k$ is conjugate closed, has rank $k$ or $k+1$, and is the smallest complete-shell radial prefix of rank at least $k$.

The union is conjugate closed because every shell is. By minimality of $J(k)$, $$\sum_{\ell<J(k)}|S_\ell|<k.$$ The last shell has at most two elements, so the completed rank is at most $k+1$. Every complete-shell radial prefix reaching $k$ must include $S_1,\ldots,S_{J(k)}$, which proves minimality.

[\[cor:unique\]]{#cor:unique label="cor:unique"} If $\rho_{J(k)}>\rho_{J(k)+1}$, then $\mathcal C_k$ is the unique shell-complete prefix separated from its complement by a radial threshold in that gap.

Any threshold between the two radii includes exactly the first $J(k)$ shells. A threshold producing a rank at least $k$ cannot stop earlier, and one stopping later is not minimal.

The qualification within the resolved ordering matters. The theorem does not assert that a numerically unresolved eigenvalue cannot lie outside the candidate boundary.

# Why even targets split pairs

Suppose $r$ real roots occur before a nonreal block. The number of nonreal slots remaining in an even target $k$ has parity equal to $r$. If $r$ is odd, the fixed prefix must either stop before a complete pair or include one member of the next pair. Therefore target parity alone is irrelevant.

Define the conjugacy defect $$\label{eq:defect}
 \epsilon_{\rm conj}(\Lambda)
 =\max_{\lambda\in\Lambda}
   \min_{\mu\in\Lambda}|\mu-\overline\lambda|.$$ A complete finite multiset has zero defect in exact arithmetic. A split pair has defect comparable to the distance from its retained member to the nearest unrelated root.

In the RH-222 atlas, the naive target prefix has $\epsilon_{\rm conj}>10^{-8}$ at 23 endpoints. Exactly 23 shell-complete clouds overshoot their target by one. Thus the correction is not a rare roundoff detail; it is the dominant cutoff geometry for the expanding ranks.

# Candidate-margin audit

RH-222 resolves a candidate window extending beyond the target. To test selection stability without rerunning or relabeling eigenvalues, we take prefixes of the archived ordered candidate list with margins $$b\in\{4,8,12,14\}.$$ For each prefix we rebuild complete shells and select by Theorem [\[thm:minimal\]](#thm:minimal){reference-type="ref" reference="thm:minimal"}. The result is compared with the reference cloud by the bottleneck assignment distance $$\label{eq:match}
 d_{\rm match}(A,B)=
 \min_{\pi}\max_j|a_j-b_{\pi(j)}|.$$

All $32\times4=128$ comparisons have $$d_{\rm match}=0,\qquad \epsilon_{\rm conj}=0$$ at archived binary64 precision. Even the four-root margin contains enough complete shells to determine the selected cloud. The larger margins only add inner omitted shells.

  diagnostic                                              result
  -------------------------------------- -----------------------
  physical endpoints                                          32
  naive prefixes splitting a pair                             23
  one-root shell-completion overshoots                        23
  maximum overshoot                                            1
  candidate-margin comparisons                               128
  maximum matching error                                       0
  minimum reference radial gap             $7.3991\times10^{-5}$

# Perturbation interpretation

Positive radial gap gives a standard finite stability margin. If every resolved eigenvalue moves by less than $g/2$ in modulus, where $$g=\rho_{J(k)}-\rho_{J(k)+1}>0,$$ then selected and omitted shell radii cannot cross. Conjugate closure remains automatic for an exactly real perturbed matrix.

This observation should not be confused with a certified pseudospectral bound. Nonnormal eigenvalues can move much more than the matrix norm perturbation, and the current gaps are computed from floating-point Arnoldi roots. An interval or Riesz-contour certification would be needed to turn the observed $g$ into an operator-level theorem; see the perturbation framework of @Kato1995.

# What has and has not become canonical

The finite result supplies three useful invariances:

1.  permutation of roots inside a shell is irrelevant;

2.  every selected root polynomial has real coefficients;

3.  four tested candidate margins give the same cloud.

It does not supply:

1.  an all-level lower bound on radial gaps;

2.  certification that the Arnoldi window contains every larger-modulus operator resonance;

3.  a derivation of the target ladder $4,6,\ldots,34$.

Accordingly the justified phrase is shell-complete resolved edge cloud, not canonical infinite spectral divisor.

# Next layer

Once the finite cutoff respects real symmetry, one center and one scale may be assigned to the whole cloud without pairing ambiguities. RH-224 uses the global barycenter and RMS radius to obtain exact moment identities and a uniform tightness theorem. That compactness statement concerns empirical probability measures; it must still be separated from local finiteness of an unweighted zero divisor.

No determinant limit or arithmetic interpretation is obtained here. Gate A and all later macro gates remain open.
