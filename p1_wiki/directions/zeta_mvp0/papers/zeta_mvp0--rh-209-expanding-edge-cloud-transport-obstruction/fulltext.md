---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-209-expanding-edge-cloud-transport-obstruction"
canonical_tex: "zeta_mvp0/papers/RH-209-expanding-edge-cloud-transport-obstruction/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-209-expanding-edge-cloud-transport-obstruction/main.pdf"
source_sha256: "2e07e515c3107d9530226c5b7e305a1beb175671496689b7bc6bb2f3c708351f"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Expanding the Modulus-Selected Edge Cloud Does Not Repair Transport A Rank-Two-to-Rank-Thirty-Two Principal-Angle Audit

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-209-expanding-edge-cloud-transport-obstruction>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-209-expanding-edge-cloud-transport-obstruction/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-209-expanding-edge-cloud-transport-obstruction/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-209-expanding-edge-cloud-transport-obstruction/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-209-expanding-edge-cloud-transport-obstruction/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The outer quartet may fail Haar transport because four modes are too few to absorb rotating spectral directions. We test this natural repair by selecting the $k$ largest-modulus modes at both adjacent levels for $k=2,4,6,8,12,16,24,32$ and comparing the embedded right and left invariant spaces.

  The repair fails on the declared rank grid. None of the 32 rank/transition/channel cases has both right and left maximum principal sines below $0.5$. The best joint sine is $0.69373$. On the $0.04\to0.02$ cases rank four is optimal among the tested ranks; on the $0.02\to0.01$ cases rank two is optimal. For ranks above four, the joint maximum sine often approaches one and reaches $0.999999993$.

  We also give an exact finite example showing that nested cloud dimensions do not force monotonic improvement of the largest principal angle: adding one orthogonal direction can change a zero angle to $\pi/2$. The result rejects only equal-rank, top-modulus clouds under the naive Haar map. It does not rule out adaptive clusters, unequal-rank transport, a renormalized embedding, or a scalar divisor limit.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Expanding the Modulus-Selected Edge Cloud Does Not Repair Transport\
  A Rank-Two-to-Rank-Thirty-Two Principal-Angle Audit
```

## Markdown 正文

# The cloud-enlargement hypothesis

The fixed quartet is necessarily only a local block: an infinite spectral count requires packet rank to grow. After RH-202 and RH-208 reject its naive Haar transport, a natural hypothesis is that omitted neighboring modes carry the missing directions. If so, enlarging the selected edge cloud should decrease the largest principal angles.

We test this hypothesis without changing two ingredients:

1.  modes are selected by decreasing eigenvalue modulus;

2.  the physical interlevel map is the dyadic Haar embedding.

Only the cloud rank changes.

# Selection and metric

Let $\lambda_1,\ldots,\lambda_n$ be ordered so that $$\label{eq:order}
 |\lambda_1|\ge\cdots\ge|\lambda_n|.$$ Let $E_c(k)$ and $E_f(k)$ be the right invariant spaces spanned by the first $k$ modes at adjacent levels, and let $F_c(k),F_f(k)$ be the corresponding left spaces.

For orthonormal bases $Q_c,Q_f$, the singular values of $Q_f^*JQ_c$ are the principal cosines [@StewartSun1990]. Define $$\label{eq:joint}
 g_k=\max\{\sin\theta_{\max}(JE_c(k),E_f(k)),
 \sin\theta_{\max}(JF_c(k),F_f(k))\}.$$ The predeclared exploratory gate is $$\label{eq:gate}
 g_k<0.5.$$ Passing would not prove transport, but would identify a cluster worth a more expensive oblique-projector and contour analysis.

# Why monotonicity is not automatic

[\[prop:nonmono\]]{#prop:nonmono label="prop:nonmono"} There exist nested pairs $E_c(1)\subset E_c(2)$ and $E_f(1)\subset E_f(2)$ such that the largest principal angle is zero at rank one and $\pi/2$ at rank two.

In $\mathbb R^3$, take $E_c(1)=E_f(1)=\operatorname{span}\{e_1\}$, $E_c(2)=\operatorname{span}\{e_1,e_2\}$, and $E_f(2)=\operatorname{span}\{e_1,e_3\}$. The rank-one spaces coincide, but the second principal cosine at rank two is zero.

Thus an increasing mean overlap can coexist with a worsening maximum angle. The latter is the relevant quantity for invertible packet correspondence.

# Thirty-two physical rank cases

The joint maximum sines are:

  step/side             $k=2$           $4$       $6$       $8$      $12$      $16$       $24$       $32$
  --------------------- --------- --------- --------- --------- --------- --------- ---------- ---------- --
  $0.04\to0.02$ left    $.8108$     $.7654$   $.9769$   $.9998$   $.9996$   $.9996$   $1.0000$   $1.0000$
  $0.04\to0.02$ right   $.8133$     $.7669$   $.9769$   $.9989$   $.9994$   $.9999$   $1.0000$   $1.0000$
  $0.02\to0.01$ left    $.6948$     $.8217$   $.9719$   $.9854$   $.9982$   $.9996$   $1.0000$   $1.0000$
  $0.02\to0.01$ right   $.6937$     $.8239$   $.9755$   $.9870$   $.9992$   $.9999$   $1.0000$   $1.0000$

No value passes [\[eq:gate\]](#eq:gate){reference-type="eqref" reference="eq:gate"}. More importantly, ranks six and above are uniformly worse than the best low-rank choice in every case.

# Best-rank pattern

The rank distribution of the minimizers is $$k=4\text{ in two cases},\qquad
 k=2\text{ in two cases},$$ with no minimizer at a larger rank. The quartet remains the best tested choice on the first transition, while one conjugate pair is best on the second.

This pattern argues against a simple rule of the form "take more outer modes until transport closes." The extra modes are not merely a buffer; some bring nearly orthogonal directions into the worst-angle metric.

# Interpretation of near-unit angles

A maximum sine near one means that at least one direction in one selected cloud is almost orthogonal to the other after embedding. It does not imply that all directions disagree: mean principal cosines can remain moderate. However, one lost direction is enough to make an equal-rank transport map ill conditioned or singular.

For oblique nonnormal packets the situation is stricter still. Good right angles would not guarantee good left angles, which is why the joint metric in [\[eq:joint\]](#eq:joint){reference-type="eqref" reference="eq:joint"} is used.

# Worst-angle versus average-overlap diagnostics

The mean principal cosine answers how much of a cloud overlaps on average; the minimum cosine answers whether every direction is recoverable. A determinant factor of equal degree needs the latter: losing one direction can change one root or make the transport singular even when most energy is captured. This explains why low-rank postblock energy compression from earlier papers does not automatically imply spectral-cloud transport.

For an unequal-rank future map, the appropriate diagnostics change. One should record injection angles from the coarse packet into a larger fine packet, the dimension of the captured image, and the residual fine complement. Such a test may succeed even when the equal-rank largest angle is near $\pi/2$; it is outside the claim of RH-209.

# What has been ruled out

The finite result rejects the compound rule $$\label{eq:rejected}
 \text{same rank at both levels}
 +\text{ largest-modulus selection}
 +\text{ Haar embedding}$$ on the specified rank grid and four physical cases.

It does not reject:

1.  a contour selected by branch continuation rather than modulus;

2.  different coarse and fine cloud ranks with an injective map;

3.  weighted subspace metrics adapted to source observability;

4.  a scale-dependent coordinate dilation or other renormalized embedding;

5.  convergence only of scalar characteristic data.

# Predeclared alternatives for a later cloud audit

Three nonmodulus rules are sufficiently concrete to test without post hoc selection: continue contours from the RH-204 branch labels; select modes by a joint modulus/residue threshold; or select the smallest conjugation-closed cluster whose transfer moments meet a declared error gate. Each rule must freeze its threshold before inspecting transport angles. Otherwise cloud growth can be tuned to manufacture an apparent match.

# Consequence for Gate A

The quartet should remain a local diagnostic and a branch-label seed, but it should not be promoted to a nested raw eigenspace shell. Likewise, blindly growing a modulus cloud is not supported. The strongest surviving signal is the dual-channel scalar divisor coherence found in RH-207.

This motivates a route decision: determine whether convergence of spectral divisors can be pursued independently of raw state transport. RH-210 proves that state convergence is sufficient but not necessary for divisor stability and records the resulting Gate-A pivot.

# Claim boundary

The nonmonotonicity proposition is exact. The rank-grid obstruction is finite and floating. It is not an all-rank or all-level theorem and does not exclude adaptive nonmodulus clouds. No infinite determinant, counting law, arithmetic trace, or Hilbert--Pólya statement follows.
