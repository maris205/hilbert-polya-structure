---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-214-monotone-axial-shape-clock"
canonical_tex: "zeta_mvp0/papers/RH-214-monotone-axial-shape-clock/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-214-monotone-axial-shape-clock/main.pdf"
source_sha256: "df7ada946a700e2ac2955e7418ee9de1da327ee9c8a30b4b1ed092ff2bb36453"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Finite Monotone Axial Clock for the Quartet Shape Flow Sixteen Scales, Two Channels, and a Narrow Asymmetry Corridor

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-214-monotone-axial-shape-clock>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-214-monotone-axial-shape-clock/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-214-monotone-axial-shape-clock/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-214-monotone-axial-shape-clock/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-214-monotone-axial-shape-clock/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-213 reduces each centered physical quartet to exact shape coordinates $(u,\eta)\in[0,1]\times[-1,1]$. We now audit their scale ordering on sixteen small-noise levels from $0.04$ to $0.00125$. On both physical channels, $u$ increases strictly through all fifteen coarse-to-fine transitions. The net change is $0.69809$ on the left and $0.69673$ on the right; the smallest observed increments are $0.01529$ and $0.01513$.

  After the initial transient, defined in advance here by $\sigma\le0.02$, $\eta$ remains in narrow corridors: $[-0.10444,-0.06886]$ on the left and $[-0.10748,-0.07031]$ on the right. Their widths are $0.03557$ and $0.03717$. Mature left/right discrepancies are at most $0.003006$ in $u$ and $0.003043$ in $\eta$.

  Any strictly ordered finite data define an invertible piecewise-linear clock on their sampled log-scale interval; we state this elementary theorem to separate a legitimate finite clock from an unsupported all-level law. The observed trajectory is therefore well described as one dominant axial motion plus a bounded transverse corridor, but no monotonicity theorem below the finest level, autonomous flow, or small-noise limit is claimed.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  A Finite Monotone Axial Clock for the Quartet Shape Flow\
  Sixteen Scales, Two Channels, and a Narrow Asymmetry Corridor
```

## Markdown 正文

# Exact coordinates and finite question

For each physical channel $s\in\{L,R\}$ and scale $\sigma$, RH-213 writes the centered-RMS quartet as $$\label{eq:roots}
 \sqrt{u_{\sigma,s}}\pm i\sqrt{(1-u_{\sigma,s})(1+\eta_{\sigma,s})},
 \quad
 -\sqrt{u_{\sigma,s}}\pm i\sqrt{(1-u_{\sigma,s})(1-\eta_{\sigma,s})}$$ [@WangRH213]. The coefficient vector is an exact function of these two coordinates. RH-212 supplies a frozen sixteen-level root atlas [@WangRH212].

We ask three finite questions:

1.  Is $u$ ordered consistently as $\sigma$ decreases?

2.  Does $\eta$ enter a narrower post-transient corridor?

3.  Do both physical channels track the same coordinate path within small finite discrepancy?

None of these questions presupposes a limiting value.

# Scale order and clock convention

Write $$\label{eq:time}
 t=\log(1/\sigma).$$ The sixteen anchors are ordered by increasing $t$, equivalently decreasing $\sigma$. Let $t_0<\cdots<t_{15}$ and let $u_k=u_{\sigma_k,s}$ on one channel.

[\[thm:clock\]]{#thm:clock label="thm:clock"} If $$\label{eq:strict}
 u_0<u_1<\cdots<u_n,$$ then there is a unique continuous function $U:[t_0,t_n]\to[u_0,u_n]$ that is affine on each interval $[t_k,t_{k+1}]$ and satisfies $U(t_k)=u_k$. It is strictly increasing and hence a homeomorphism onto its image.

Linear interpolation is unique on every subinterval. Its slope there is $(u_{k+1}-u_k)/(t_{k+1}-t_k)>0$, so the pieces join to a strictly increasing continuous bijection. A continuous strictly monotone map on a compact interval has continuous inverse.

The theorem is intentionally finite. It neither extends $U$ beyond the sampled interval nor says that the piecewise-linear interpolation is the physical law.

# Sixteen-level axial verdict

For each transition define $$\Delta u_{k,s}=u_{k+1,s}-u_{k,s}.$$ All thirty channel-transition increments are positive.

  axial diagnostic                                 left        right
  ---------------------------------------- ------------ ------------
  transition count                                   15           15
  positive increments                                15           15
  minimum increment                          $0.015295$   $0.015130$
  maximum increment                          $0.104022$   $0.106002$
  net change                                 $0.698086$   $0.696733$
  total variation                            $0.698086$   $0.696733$
  rank correlation with $\log(1/\sigma)$            $1$          $1$

Equality of total variation and net change is simply another expression of finite monotonicity. The factor-of-seven spread between minimum and maximum increments warns against treating the anchor index itself as constant-speed time.

# Representative dyadic subsequence

The following equal-log-step subsequence displays the dominant motion:

     $\sigma$       $u_L$       $u_R$     $\eta_L$     $\eta_R$
  ----------- ----------- ----------- ------------ ------------
       $0.04$   $0.02027$   $0.02077$   $-0.57806$   $-0.59358$
       $0.02$   $0.24887$   $0.24794$   $-0.06886$   $-0.07031$
       $0.01$   $0.40529$   $0.40229$   $-0.10443$   $-0.10748$
      $0.005$   $0.54098$   $0.54034$   $-0.08934$   $-0.09080$
     $0.0025$   $0.65874$   $0.65801$   $-0.09050$   $-0.09181$
    $0.00125$   $0.71835$   $0.71750$   $-0.09303$   $-0.09444$

The first transition contains a large transverse relaxation. Thereafter the axial coordinate advances while $\eta$ fluctuates around roughly $-0.09$.

# The mature asymmetry corridor

For a finite ordered sequence $x_k$, define $$\operatorname{width}(x)=\max_kx_k-\min_kx_k,
 \qquad
 \operatorname{TV}(x)=\sum_k|x_{k+1}-x_k|.$$ On the levels with $\sigma\le0.02$:

  transverse diagnostic            left         right
  ----------------------- ------------- -------------
  minimum $\eta$            $-0.104434$   $-0.107477$
  maximum $\eta$            $-0.068864$   $-0.070311$
  width                      $0.035570$    $0.037166$
  mean                      $-0.089618$   $-0.091187$
  RMS about mean             $0.009378$    $0.009636$
  total variation            $0.070188$    $0.074222$

The total variation is about twice the width, so $\eta$ is not monotone. A "transverse fixed point" would overstate the evidence. The justified term is a finite corridor.

# Dual-channel synchronization

At fixed $\sigma$, define $$\delta_u(\sigma)=|u_{\sigma,L}-u_{\sigma,R}|,
 \qquad
 \delta_\eta(\sigma)=|\eta_{\sigma,L}-\eta_{\sigma,R}|.$$ Across all sixteen scales, $$\max\delta_u=0.004229,
 \qquad \max\delta_\eta=0.015523,$$ where the transverse maximum occurs in the initial transient. On the mature subset, $$\label{eq:maturesync}
 \max\delta_u=0.003006,
 \qquad \max\delta_\eta=0.003043.$$

These discrepancies are small compared with the net axial displacement, but they are not interval-certified errors. They quantify agreement of two finite discretizations/channels under the same root-selection rule.

# A near-one-dimensional description

The phrase "near one-dimensional" has a precise finite meaning here:

1.  one coordinate is strictly ordered through every observed transition;

2.  the other remains in a post-transient interval of width below $0.038$;

3.  both channels agree to roughly $3\times10^{-3}$ in each mature coordinate.

It does not mean that $\eta$ is a function of $u$ at all levels, that the trajectory lies on an invariant curve, or that a one-dimensional generator has been found.

# Why finite monotonicity matters

The raw quartic coefficient flow looked irregular because location, radius, axial separation, and transverse asymmetry were mixed. The exact shape coordinates show that one component has a stable order. This gives a useful clock for:

1.  predeclared out-of-sample extrapolation;

2.  boundary-distance estimates;

3.  sensitivity decompositions;

4.  equal-log-step recurrence audits.

These uses remain finite unless accompanied by uniform estimates.

# Claim boundary and next test

The data do not prove:

-   $u_\sigma$ is monotone for every sufficiently small $\sigma$;

-   $u_\sigma$ has a limit, much less limit one;

-   $\eta_\sigma$ converges;

-   a scale-independent map advances the shape;

-   a growing determinant exists.

RH-215 therefore freezes seven fine levels as training data and withholds two finer levels for prediction. Gate A stays open, and no statement about Gates B--E or zeta zeros is made.
