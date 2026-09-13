---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-227-reciprocal-local-count-small-noise-gate"
canonical_tex: "zeta_mvp0/papers/RH-227-reciprocal-local-count-small-noise-gate/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-227-reciprocal-local-count-small-noise-gate/main.pdf"
source_sha256: "14a20e0ed4adf116b705d2b0fe5a3b591cf50ecfccd4ec0b27de70107498e529"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Reciprocal Local-Count Gate for the Small-Noise Limit Rouche Stability versus Proliferating Fredholm Zeros

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-227-reciprocal-local-count-small-noise-gate>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-227-reciprocal-local-count-small-noise-gate/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-227-reciprocal-local-count-small-noise-gate/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-227-reciprocal-local-count-small-noise-gate/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-227-reciprocal-local-count-small-noise-gate/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  At every fixed positive noise, the Hilbert--Schmidt determinant exists and its zeros are reciprocal resonances. A locally uniform small-noise limit requires more: zero counts on any contour avoiding the limiting divisor must eventually stabilize.

  We formulate this requirement as a Rouche local-count gate and audit the rank-growing reciprocal clouds on the predeclared radii $1.2,1.5,2,3,5$. All 160 endpoint-contour pairs have positive finite clearance; the minimum is $1.3338\times10^{-4}$. Nevertheless none of the five left-channel count sequences and only one right-channel sequence is constant over the last four scales. The largest first-to-last count growth is 18. On radius two, both channels grow from two to ten selected reciprocal zeros.

  This is a finite gate failure, not an asymptotic no-go theorem. The selected cloud is not the complete determinant divisor, and additional smaller-noise levels could eventually stabilize. The result says that local uniformity is not yet supported and that moving-cloud or relative-determinant renormalization cannot be skipped.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  A Reciprocal Local-Count Gate for the Small-Noise Limit\
  Rouche Stability versus Proliferating Fredholm Zeros
```

## Markdown 正文

# A necessary condition for local uniformity

Let $\Omega\subset\mathbb C$ be a domain and let $f_n,f$ be holomorphic on $\Omega$.

[\[thm:rouche\]]{#thm:rouche label="thm:rouche"} Suppose $f_n\to f$ locally uniformly and $f\not\equiv0$. Let $\Gamma\subset\Omega$ be a positively oriented simple closed contour on which $f$ has no zero. Then, for all sufficiently large $n$, $f_n$ and $f$ have the same number of zeros inside $\Gamma$, counted with multiplicity.

Compactness of $\Gamma$ and nonvanishing of $f$ give $\min_\Gamma|f|>0$. Local uniform convergence eventually gives $\max_\Gamma|f_n-f|<\min_\Gamma|f|$. Rouche's theorem then proves the claim [@Conway1978].

Thus every nonzero locally uniform determinant limit has eventual local divisor stability away from its boundary zeros. This condition is necessary, not sufficient.

# Finite reciprocal clouds

For each selected resonance cloud $\Lambda_{\sigma,s}$ from RH-222, define $$Z_{\sigma,s}=
 \{\lambda^{-1}:\lambda\in\Lambda_{\sigma,s}\}.$$ RH-226 proves that these are exactly the zeros of the selected regularized Fredholm factor [@WangRH226]. For radius $R$, define $$\label{eq:count}
 N_{\sigma,s}(R)=
 \#\{z\in Z_{\sigma,s}:|z|<R\}$$ with multiplicity, and finite contour clearance $$\label{eq:clearance}
 c_{\sigma,s}(R)=
 \min_{z\in Z_{\sigma,s}}\bigl||z|-R\bigr|.$$

Positive $c_{\sigma,s}(R)$ makes each individual finite count unambiguous. It does not give a uniform lower bound or identify the zero count of the unresolved operator complement.

# Predeclared gate

The radii $$\mathcal R=\{1.2,1.5,2,3,5\}$$ probe, respectively, the first near-unit reciprocal zeros and progressively larger parts of the selected divisor. The finite diagnostic asks whether each count is constant over the last four frozen noise levels $$\sigma=0.0025,\;0.002,\;0.0016,\;0.00125.$$ Four levels are a diagnostic window, not a definition of eventuality.

The complete count sequences are:

   side    $R$  first eight levels       last eight levels
  ------- ----- ------------------------ ---------------------------
   left    1.2  $0,0,0,0,0,0,0,0$        $2,2,2,2,2,2,4,4$
   left    2.0  $2,4,4,4,4,4,6,6$        $6,6,8,8,8,8,8,10$
   left    5.0  $4,6,7,10,11,11,12,13$   $14,17,16,20,20,19,23,22$
   right   1.2  $0,0,0,0,0,0,0,0$        $2,2,2,2,2,2,2,4$
   right   2.0  $2,4,4,4,4,4,6,6$        $6,6,8,8,8,8,8,10$
   right   5.0  $4,6,7,9,10,13,12,15$    $14,17,16,18,20,19,23,22$

The nonmonotonicity at larger radii is allowed: changing $\sigma$ moves old zeros as well as adding selected shells. Rank growth alone does not make fixed-disk counts monotone.

# Audit verdict

  diagnostic                                                  result
  ------------------------------------------ -----------------------
  endpoint-contour cases                                         160
  minimum finite contour clearance             $1.3338\times10^{-4}$
  largest first-to-last count growth                              18
  left radii constant on last four levels                      $0/5$
  right radii constant on last four levels                     $1/5$
  all-radius finite gate                                      failed

The single stable right sequence is $R=1.5$, with final counts $8,8,8,8$. It does not compensate for the failures at the other radii.

At $R=2$, both channels move from count two to count ten. If this growth continued without bound while the selected clouds captured all reciprocal zeros in the disk, it would obstruct a nonzero locally uniform limit by Theorem [\[thm:rouche\]](#thm:rouche){reference-type="ref" reference="thm:rouche"}. The finite data do not establish either premise.

# Why this is not a disproof

There are four logical gaps between the audit and an asymptotic no-go theorem:

1.  only sixteen noise levels are observed;

2.  the rank schedule is a stress test, not a complete spectral cutoff;

3.  Arnoldi roots and contour clearances are not interval certified;

4.  a relative determinant may remove a growing near-unit factor before taking a limit.

Therefore the exact conclusion is that the current finite family does not pass a necessary diagnostic. We do not claim that eventual stability is false.

RH-80 gives an abstract moving-cloud relative determinant route [@WangRH80]. To use it here one must construct a reducing cloud and bound the complementary determinant uniformly. Before attempting that harder operator step, the next paper asks a narrower question: are the complete shells already resolved beyond the selected cloud controllable as an omitted regularized-product tail?

# Claim boundary

Theorem [\[thm:rouche\]](#thm:rouche){reference-type="ref" reference="thm:rouche"} is exact. The five-radius verdict is finite. No small-noise determinant limit is disproved, and no new determinant is constructed. Gates A--E remain open. In particular the reciprocal Markov zeros are not asserted to be self-adjoint energies or zeta zeros.
