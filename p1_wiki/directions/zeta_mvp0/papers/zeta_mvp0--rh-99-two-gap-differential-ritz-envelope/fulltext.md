---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-99-two-gap-differential-ritz-envelope"
canonical_tex: "zeta_mvp0/papers/RH-99-two-gap-differential-ritz-envelope/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-99-two-gap-differential-ritz-envelope/main.pdf"
source_sha256: "fa8554c3321741339959655e0d68fd9552796292e07e67553d31ad84edbbbe48"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Two-Gap Differential Envelopes Infinitesimal Control of Adaptive Projected-Cross Ritz Refresh

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-99-two-gap-differential-ritz-envelope>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-99-two-gap-differential-ritz-envelope/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-99-two-gap-differential-ritz-envelope/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-99-two-gap-differential-ritz-envelope/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-99-two-gap-differential-ritz-envelope/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-98 shows that a replay-free endpoint bound requires a projector-Lipschitz constant for the future Ritz block, and that no universal unit constant exists. We derive the infinitesimal constant for one invariant projected-cross refresh.

  Let $P$ be the incoming rank-$r$ projector and $G=G^*\ge0$. Define the cross covariance $$C(P)=(I-P)GPG(I-P),$$ let $Q(P)$ be its leading rank-$k$ spectral projector, put $S(P)=P+Q(P)$, and let $F(P)$ be the leading rank-$r$ spectral projector of $S(P)GS(P)$. If the selected cross-covariance cluster has gap $\delta_c>0$ and the output Ritz cluster has gap $\delta_r>0$, then the cross covariance derivative formula and spectral projector Sylvester bound give the two-gap refresh derivative theorem $$\left\lVert DF(P)\right\rVert_{F\leftarrow F}
   \le
   \frac{4\left\lVert G\right\rVert_2}{\delta_r}
   \left(1+\frac{6\left\lVert G\right\rVert_2^2}{\delta_c}\right).$$ The two gaps control distinct branch choices: cross-direction selection and output Ritz selection.

  We audit the primary adaptive source-seeded chain at all 120 updates using six Grassmann tangent probes per update. Both guarded gaps are positive at 115 updates, and all 690 probes there lie below the theorem bound. Adaptive weak-mode quotienting improves the formal bound at each of its five updates, by as much as $9.44\times10^9$ relative to width four.

  The result is nevertheless negative at finite scale. Five fine-scale output Ritz gaps cannot be certified positive under the binary64 reconstruction residual guard. Available derivative bounds reach $1.44\times10^{40}$ and can exceed probe derivatives by $1.03\times10^{36}$. None of the five actual adaptive/full quotient displacements lies inside the first-order two-gap separation radius; the worst ratio exceeds $10^{33}$.

  Thus the differential formula is correct and identifies the right gaps, but it does not yet close a finite neighborhood tube. Higher-precision continuation, a gap-aware nonsmooth branch rule, or continued exact hybrid replay remains necessary. No replay-free block theorem, Hilbert--Polya operator, zero identification, or Riemann Hypothesis result is claimed.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Two-Gap Differential Envelopes\
  Infinitesimal Control of Adaptive Projected-Cross Ritz Refresh
```

## Markdown 正文

**Keywords:** spectral projector derivative; Sylvester equation; cross covariance; Ritz gap; Grassmann manifold; validated numerics.

**MSC 2020:** 47A75; 15A18; 65F15; 65G20; 37C30.

# Introduction

The projector factorization of RH-98 reduces endpoint propagation to three steps: a local gap converts energy loss to packet displacement, a future projector-Lipschitz constant propagates that displacement, and the endpoint Gram norm converts it back to tail energy [@WangProjectorBarrier2026]. The missing object is the middle constant.

For a smooth separated spectral branch, projector derivatives are governed by reduced resolvents or Sylvester equations [@Kato1995; @StewartSun1990]. The projected-cross Ritz map contains two such branches. First one chooses a leading cross-covariance subspace. Then one chooses a leading Ritz subspace inside the enrichment. Consequently one gap cannot control the full map.

This paper formulates the refresh directly on orthogonal projectors, removing frame gauge from the differentiation. It derives an explicit two-gap bound and tests that bound against tangent secants along the complete finite chain. The theorem succeeds infinitesimally wherever both gaps are certified. The audit then shows why this is not yet enough: several fine-scale output gaps are below the current verification resolution, and first-order separation radii are tiny compared with the actual adaptive quotient steps.

This is a useful negative result before the hundred-layer review. It distinguishes a correct local formula from a usable nonlinear tube and makes the remaining alternatives explicit.

# Invariant projected-cross refresh {#sec:map}

Let $\mathcal H$ be finite dimensional, $G=G^*\ge0$, and let $P=P^*=P^2$ have rank $r$. Define $$C(P)=(I-P)GPG(I-P).
 \label{eq:covariance}$$ This positive operator acts on $\operatorname{Ran}(I-P)$. Its nonzero eigenvalues are the squared singular values of the projected cross operator $(I-P)GV$ for any isometric frame $V$ of $\operatorname{Ran}P$.

Fix a width $k$. Suppose the $k$th and $(k+1)$st eigenvalues of $C(P)$ are separated: $$\delta_c=\mu_k(C(P))-\mu_{k+1}(C(P))>0.$$ Let $Q(P)$ be the corresponding leading rank-$k$ spectral projector. Since $Q(P)P=0$, the enrichment projector is $$S(P)=P+Q(P).$$ Define the enriched operator $$B(P)=S(P)GS(P).$$ If its leading rank-$r$ cluster has gap $$\delta_r=\lambda_r(B(P))-\lambda_{r+1}(B(P))>0,$$ the invariant refresh map is $$F(P)=\mathbf 1_{\text{leading }r}(B(P)).
 \label{eq:refresh}$$

# Cross covariance derivative formula {#sec:cross}

Let $P(t)$ be a differentiable projector curve with $\dot P=dP/dt$. Differentiating [\[eq:covariance\]](#eq:covariance){reference-type="eqref" reference="eq:covariance"} gives:

[\[prop:cross\]]{#prop:cross label="prop:cross"} $$\dot C
 =-\dot P\,GPG(I-P)
 +(I-P)G\dot P\,G(I-P)
 -(I-P)GPG\dot P.
 \label{eq:cross-derivative}$$ Consequently $$\left\lVert\dot C\right\rVert_F
 \le3\left\lVert G\right\rVert_2^2\left\lVert\dot P\right\rVert_F.
 \label{eq:cross-bound}$$

Apply the product rule to [\[eq:covariance\]](#eq:covariance){reference-type="eqref" reference="eq:covariance"}. Every orthogonal projector has operator norm one, so each of the three terms is bounded by $\left\lVert G\right\rVert_2^2\left\lVert\dot P\right\rVert_F$.

# Spectral projector Sylvester bound {#sec:sylvester}

Let $A(t)=A(t)^*$ have a separated spectral cluster with projector $\Pi(t)$. In a basis splitting the selected and complementary clusters, differentiation of $A\Pi=\Pi A$ gives a Sylvester equation for the off-diagonal block of $\dot\Pi$.

[\[thm:sylvester\]]{#thm:sylvester label="thm:sylvester"} If the selected and complementary spectra are separated by $\delta>0$, then $$\left\lVert\dot\Pi\right\rVert_F
 \le\frac{2}{\delta}\left\lVert\dot A\right\rVert_F.
 \label{eq:sylvester}$$

Write the off-diagonal derivative block as $X$. It solves $$A_{11}X-XA_{22}=-(\dot A)_{12}.$$ The inverse Sylvester operator has norm at most $\delta^{-1}$. Since $\dot\Pi$ has off-diagonal blocks $X$ and $X^*$, $\left\lVert\dot\Pi\right\rVert_F=\sqrt2\left\lVert X\right\rVert_F$. Replacing $\sqrt2$ by $2$ gives [\[eq:sylvester\]](#eq:sylvester){reference-type="eqref" reference="eq:sylvester"}. This is the differential form of standard sin-theta estimates [@DavisKahan1970].

# Two-gap refresh derivative theorem {#sec:theorem}

[\[thm:two-gap\]]{#thm:two-gap label="thm:two-gap"} Under the cross and Ritz separation hypotheses of [2](#sec:map){reference-type="ref" reference="sec:map"}, $$\left\lVert\dot F\right\rVert_F
 \le
 \frac{4\left\lVert G\right\rVert_2}{\delta_r}
 \left(1+\frac{6\left\lVert G\right\rVert_2^2}{\delta_c}\right)
 \left\lVert\dot P\right\rVert_F.
 \label{eq:two-gap}$$

Apply [\[thm:sylvester\]](#thm:sylvester){reference-type="ref" reference="thm:sylvester"} to $C(P)$ and use [\[eq:cross-bound\]](#eq:cross-bound){reference-type="eqref" reference="eq:cross-bound"}: $$\left\lVert\dot Q\right\rVert_F
 \le\frac{6\left\lVert G\right\rVert_2^2}{\delta_c}\left\lVert\dot P\right\rVert_F.$$ Thus $$\left\lVert\dot S\right\rVert_F
 \le\left(1+\frac{6\left\lVert G\right\rVert_2^2}{\delta_c}\right)
 \left\lVert\dot P\right\rVert_F.$$ Since $B=SGS$, $$\dot B=\dot S\,GS+SG\dot S,\qquad
 \left\lVert\dot B\right\rVert_F\le2\left\lVert G\right\rVert_2\left\lVert\dot S\right\rVert_F.$$ A second application of [\[thm:sylvester\]](#thm:sylvester){reference-type="ref" reference="thm:sylvester"}, now with gap $\delta_r$, gives [\[eq:two-gap\]](#eq:two-gap){reference-type="eqref" reference="eq:two-gap"}.

The theorem is local to a fixed pair of separated branches. It does not control a perturbation large enough to change the selected width, swap cross modes, or close the output Ritz gap.

## First-order separation radii

The derivative bounds suggest diagnostics $$\begin{aligned}
 R_c&=\frac{\delta_c}{12\left\lVert G\right\rVert_2^2},\\
 R_r&=\frac{\delta_r}
 {8\left\lVert G\right\rVert_2(1+6\left\lVert G\right\rVert_2^2/\delta_c)},\\
 R_{\rm lin}&=\min(R_c,R_r).
 \label{eq:radii}\end{aligned}$$ They correspond to spending one quarter of each gap under the first-order norm bounds. They are not nonlinear invariant radii; the audit uses them only to test whether the actual quotient displacement is even plausibly local.

# Finite audit {#sec:audit}

We run the primary $10^{-8}$ adaptive chain over the ten source-seeded channels of RH-96. At each of 120 updates we compute:

-   the selected cross squared-singular gap;

-   the output compressed Ritz gap, reduced by eigendecomposition residual and a binary64 roundoff guard;

-   the bound [\[eq:two-gap\]](#eq:two-gap){reference-type="eqref" reference="eq:two-gap"} when both guarded gaps are positive;

-   six deterministic random Grassmann tangent secants;

-   at quotient updates, the width-four bound and actual adaptive/full projector displacement.

Arb precision is set to 384 bits for consistency with the archived audit, while this paper's gap and derivative diagnostics concern the concrete binary64 matrices and selected branches [@Rump2010].

## Available differential certificates

Both guarded gaps are positive at 115 updates. All 690 tangent probes at those updates lie below the two-gap theorem bound. The largest observed probe derivative is $7.31\times10^6$.

The theorem bounds are far larger. The maximum is $$1.44\times10^{40},$$ and the largest bound/probe ratio is $1.03\times10^{36}$. Even the smallest bound/probe ratio is above $1.76\times10^4$. The formula is therefore a valid branch-sensitivity certificate, not yet a practical endpoint envelope.

## Gap failure and quotient improvement

All cross squared gaps are positive in the computed chain, reaching as low as $6.47\times10^{-30}$. Five fine-scale output Ritz gaps become nonpositive after the residual guard; hence no differential certificate is issued there. These are not claims of exact eigenvalue collision, but failures to certify the required branch separation at current precision.

At the five primary weak-mode quotient updates, adaptive width three improves the formal derivative bound relative to width four in every case. The largest improvement factor is $9.44\times10^9$. Nevertheless, none of the five actual adaptive/full projector distances lies below $R_{\rm lin}$. The worst distance/radius ratio is $1.21\times10^{33}$.

![Two-gap differential audit. Available bounds contain every tangent probe but are extremely conservative. Five Ritz gaps are unavailable, and no actual quotient displacement lies in the first-order tube.](<../../../../../zeta_mvp0/papers/RH-99-two-gap-differential-ritz-envelope/figures/two_gap_differential_ritz_envelope.pdf>){#fig:audit width="\\textwidth"}

# What remains for a finite neighborhood tube

The differential route can proceed only after one of three changes.

1.  *Higher-precision continuation:* certify the small Ritz gaps and integrate projector derivatives while monitoring both clusters.

2.  *Gap-aware nonsmooth selection:* modify the adaptive rule to avoid cross or Ritz branch boundaries, accepting a set-valued or hysteretic map.

3.  *Stopped finite certification:* retain exact hybrid replay and prove only that the process exits once the endpoint budget is met, rather than demanding a uniform smooth tube.

The hundred-layer review should compare these paths against the broader normalization and observability gates.

# Claim boundary

The cross covariance derivative formula, spectral projector Sylvester bound, and two-gap refresh derivative theorem are exact. The tangent audit validates only the concrete sampled directions where both guarded gaps are positive. It does not prove a finite neighborhood tube, uniform branch separation, replay-free block envelope, repeated-block contraction, Hilbert--Polya operator, zeta-zero identification, or the Riemann Hypothesis.

# Conclusion

One projected-cross Ritz refresh has the expected two-gap differential structure. Cross selection and output Ritz selection each contribute a resolvent denominator. This theorem explains both the benefit of weak-mode quotienting and the fragility of a smooth propagation route.

The finite audit stops short of a tube: five output gaps are unavailable, constants are enormous, and actual quotient steps are not infinitesimal on the certified radii. RH-100 must therefore treat the differential route as an open alternative, not a closed propagation theorem.
