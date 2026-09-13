---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-183-projective-wrap-obstruction"
canonical_tex: "zeta_mvp0/papers/RH-183-projective-wrap-obstruction/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-183-projective-wrap-obstruction/main.pdf"
source_sha256: "8148197c2a3b9af0a949c46c3775420503b23ef95d7b0d5fc49fc1e78f28d5e9"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The Projective Wrap Obstruction Exact Phase and Scalar Lower Bounds for Finite Temporal Cycles

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-183-projective-wrap-obstruction>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-183-projective-wrap-obstruction/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-183-projective-wrap-obstruction/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-183-projective-wrap-obstruction/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-183-projective-wrap-obstruction/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-182 found no orthogonal finite temporal clock passing a joint wrap, primal, and adjoint gate. A possible concern is that this negative result could be an artifact of a sign, phase convention, or poorly normalized final edge. This paper removes that ambiguity.

  For unit vectors $x_0,x_L$ in a complex Hilbert space, the best unimodular wrap has phase $\omega=\langle x_0,x_L\rangle/|\langle x_0,x_L\rangle|$ and chord $\sqrt{2-2|\langle x_0,x_L\rangle|}$. If the final edge is allowed an arbitrary complex scalar, the exact minimum residual is the physical edge amplitude times $\sqrt{1-|\langle x_0,x_L\rangle|^2}$. Hence the projective return distance is an unavoidable lower bound for every one-edge cyclic closure with the declared temporal span. For a polar-orthogonalized synthesis, the residual is bounded above and below by the same rank-one defect divided by the extreme square roots of its Gram spectrum.

  Eighty deterministic formula cases verify the rank-one, scalar-optimal, and polar-bound identities with zero failures; the largest direct formula error is $4.45\times10^{-16}$. Replaying the 126 RH-182 physical windows, 43 negative orientation marks improve the endpoint chord, by as much as $1.5849$. Nevertheless no projective return distance is at most $0.25$ and no orthogonal three-way gate survives.

  This gives a rigorous finite obstruction for the declared temporal spans: phase repair cannot rescue the orthogonal branch. It is not an all-level no-go theorem and does not constrain a construction with distinct right and left spaces. No physical Riesz or Hilbert--Polya conclusion is claimed.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  The Projective Wrap Obstruction\
  Exact Phase and Scalar Lower Bounds for Finite Temporal Cycles
```

## Markdown 正文

# Why a separate wrap theorem is needed

The weighted temporal clock of RH-182 has exact chain columns. Its only intertwining error is the endpoint-to-seed wrap [@WangRH182]. In the real physical data, many length-four endpoint correlations are negative. A positive wrap edge therefore overstates the error. The orientation mark corrects that sign, but one must still know whether some more general phase or scalar can eliminate the defect.

The answer is exact and elementary. It is useful because it separates three increasingly permissive questions:

1.  positive wrap: compare $x_L$ with $x_0$;

2.  phase-marked wrap: compare $x_L$ with $\omega x_0$, $|\omega|=1$;

3.  arbitrary scalar wrap: compare $x_L$ with $\beta x_0$, $\beta\in\mathbb C$.

If the third question still has a large residual, neither sign nor amplitude normalization is the problem.

# Phase optimization

Let $u,v\in\mathcal H$ be unit vectors and put $c=\langle u,v\rangle$.

[\[thm:phase\]]{#thm:phase label="thm:phase"} If $c\ne0$, the minimizer of $\left\lVert v-\omega u\right\rVert$ over $\omega\in\mathbb T$ is $$\label{eq:optimal-phase}
 \omega_*=\frac{c}{|c|}.$$ The minimum is $$\label{eq:phase-chord}
 d_{\mathbb T}(u,v)
 =\sqrt{2-2|c|}.$$ If $c=0$, every phase is minimizing and the minimum is $\sqrt2$.

For $|\omega|=1$, $$\left\lVert v-\omega u\right\rVert^2
 =2-2\operatorname{Re}(\overline\omega c).$$ The real part is at most $|c|$, with equality at $\omega=c/|c|$. Substitution gives [\[eq:phase-chord\]](#eq:phase-chord){reference-type="eqref" reference="eq:phase-chord"}.

The quantity in [\[eq:phase-chord\]](#eq:phase-chord){reference-type="eqref" reference="eq:phase-chord"} is a chord distance on projective space. For small principal angle it is comparable to that angle, but the exact formula is retained in the audit.

# Arbitrary scalar optimization

Allowing an arbitrary scalar gives the orthogonal projection of $v$ onto $\mathbb Cu$.

[\[thm:scalar\]]{#thm:scalar label="thm:scalar"} For $a\ge0$, $$\label{eq:scalar-min}
 \min_{\beta\in\mathbb C}\left\lVert av-\beta u\right\rVert
 =a\sqrt{1-|\langle u,v\rangle|^2}.$$ The minimizing scalar is $\beta_*=a\langle u,v\rangle$.

Decompose $v=\langle u,v\rangle u+v_\perp$ with $v_\perp\perp u$. Then $$av-\beta u
 =(a\langle u,v\rangle-\beta)u+av_\perp.$$ The two summands are orthogonal. The first vanishes exactly at $\beta_*$, while $\left\lVert v_\perp\right\rVert^2=1-|\langle u,v\rangle|^2$.

Define the projective return distance $$\label{eq:projective-distance}
 d_{\mathbb P}(u,v)=
 \sqrt{1-|\langle u,v\rangle|^2}.$$ It is no larger than the phase chord, but unlike the phase chord it permits amplitude adjustment. A large value of [\[eq:projective-distance\]](#eq:projective-distance){reference-type="eqref" reference="eq:projective-distance"} is therefore a stronger obstruction.

For unit vectors $u,v$, $$\label{eq:distance-relation}
 d_{\mathbb T}(u,v)^2
 =\frac{2}{1+|\langle u,v\rangle|}
 d_{\mathbb P}(u,v)^2.$$ Consequently $$\label{eq:distance-comparison}
 d_{\mathbb P}(u,v)\le d_{\mathbb T}(u,v)
 \le\sqrt2\,d_{\mathbb P}(u,v).$$

Put $s=|\langle u,v\rangle|$. Then $d_{\mathbb T}^2=2(1-s)$ and $d_{\mathbb P}^2=(1-s)(1+s)$. Their ratio is $2/(1+s)$, which lies in $[1,2]$.

Equation [\[eq:distance-relation\]](#eq:distance-relation){reference-type="eqref" reference="eq:distance-relation"} quantifies exactly what is gained by allowing amplitude as well as phase. The gain is never more than a factor $\sqrt2$ in norm. Hence a projective failure cannot be attributed to a minor convention about endpoint normalization.

# Application to one-edge temporal closure

Let $x_j$ be the normalized orbit from RH-182 and let $J=[x_t,\ldots,x_{t+L-1}]$. The physical final edge is $$\label{eq:physical-final-edge}
 \mathcal A x_{t+L-1}=a_{t+L-1}x_{t+L}.$$

[\[cor:final-column\]]{#cor:final-column label="cor:final-column"} Among all cyclic final columns that land in the seed line $\mathbb Cx_t$, the minimum physical residual is $$\label{eq:final-lower-bound}
 a_{t+L-1}d_{\mathbb P}(x_t,x_{t+L}).$$ The best phase-only residual is $a_{t+L-1}d_{\mathbb T}(x_t,x_{t+L})$.

Thus no alternative wrap normalization can beat [\[eq:final-lower-bound\]](#eq:final-lower-bound){reference-type="eqref" reference="eq:final-lower-bound"} without changing the temporal span or the physical final image.

The same argument identifies the minimal structural repair. Let $E\subset\mathcal H$ be any proposed $k$-dimensional return space and let $P_E$ be its orthogonal projection.

For a unit endpoint $v$ and amplitude $a\ge0$, $$\label{eq:return-subspace}
 \min_{z\in E}\left\lVert av-z\right\rVert=a\left\lVert(I-P_E)v\right\rVert.$$

The orthogonal decomposition $av=P_E(av)+(I-P_E)(av)$ shows that the unique best approximation is $z=P_E(av)$ and that the residual is the orthogonal component in [\[eq:return-subspace\]](#eq:return-subspace){reference-type="eqref" reference="eq:return-subspace"}.

The one-edge cyclic closure is the special case $E=\mathbb Cu$. Therefore a successful repair must enlarge or change the return space, alter the temporal span, or use distinct right and left spaces. Reweighting the same seed line cannot help.

# Polar conditioning bounds

Assume $G=J^*J>0$ and $V=JG^{-1/2}$. Let $C(\omega)$ be the phase-marked cycle and $K=G^{1/2}C(\omega)G^{-1/2}$. The polar residual is $$\label{eq:polar-residual}
 R=\mathcal AV-VK
 =a_{t+L-1}(x_{t+L}-\omega x_t)e_{L-1}^*G^{-1/2}.$$

[\[prop:gram-bound\]]{#prop:gram-bound label="prop:gram-bound"} Let $\lambda_{\min}$ and $\lambda_{\max}$ be the extreme eigenvalues of $G$. Then $$\label{eq:gram-bound}
 \frac{a_{t+L-1}d_{\mathbb T}}
 {\sqrt{\lambda_{\max}}}
 \le \left\lVert R\right\rVert\le
 \frac{a_{t+L-1}d_{\mathbb T}}
 {\sqrt{\lambda_{\min}}}.$$

Equation [\[eq:polar-residual\]](#eq:polar-residual){reference-type="eqref" reference="eq:polar-residual"} is a rank-one operator. Its norm equals $a_{t+L-1}d_{\mathbb T}\left\lVert e_{L-1}^*G^{-1/2}\right\rVert$. The norm of $G^{-1/2}$ lies between $\lambda_{\max}^{-1/2}$ and $\lambda_{\min}^{-1/2}$ on every unit vector, giving [\[eq:gram-bound\]](#eq:gram-bound){reference-type="eqref" reference="eq:gram-bound"}.

The upper bound explains why an ill-conditioned temporal Gram can amplify a moderate endpoint error. The lower bound shows that polar normalization cannot make the defect disappear.

# Formula audit

The deterministic audit uses dimensions $4,5,8,11$, lengths $3,4$, and ten random trials per pair, for 80 cases. It compares:

1.  the direct matrix norm of the rank-one wrap with its closed formula;

2.  the optimized arbitrary-scalar residual with $a d_{\mathbb P}$;

3.  the actual polar residual with both bounds in [\[eq:gram-bound\]](#eq:gram-bound){reference-type="eqref" reference="eq:gram-bound"}.

All 80 cases pass. The maximum direct rank-one formula error is $4.45\times10^{-16}$, the scalar formula error is zero at stored precision, and every polar residual lies in its declared interval.

These tests are not physical evidence. They certify the implementation of the exact finite theorem.

# Replay of the physical windows

The RH-182 archive contains 126 predeclared windows. Forty-three have a negative real endpoint correlation, so the orientation mark changes the sign of the wrap. Exactly those 43 windows show a nontrivial phase-mark improvement. The largest chord reduction is $1.5849$.

Despite that substantial correction, $$\label{eq:no-projective-return}
 \#\{d_{\mathbb P}\le0.25\}=0.$$

The minimum is $0.37202$, leaving a finite gap $0.12202$ above the declared threshold even after arbitrary scalar optimization. Since [\[eq:return-subspace\]](#eq:return-subspace){reference-type="eqref" reference="eq:return-subspace"} is an exact lower bound, Gram conditioning and polar normalization can only redistribute or amplify the remaining defect; they cannot erase its component orthogonal to the seed line.

# Stability of the obstruction under endpoint perturbations

For unit pairs $(u,v)$ and $(\widetilde u,\widetilde v)$, Cauchy--Schwarz gives $$\label{eq:correlation-stability}
 \left|
 |\langle u,v\rangle|-|\langle\widetilde u,\widetilde v\rangle|
 \right|
 \le \left\lVert u-\widetilde u\right\rVert+\left\lVert v-\widetilde v\right\rVert.$$ Thus an outward enclosure of the two endpoint vectors immediately yields an outward enclosure of the correlation and hence of both projective distances. This observation is useful for a later interval implementation: one need not validate a nonlinear phase optimizer separately. It suffices to validate the endpoint balls and apply the closed formulas.

The present replay is not such an interval proof, so the finite margin is reported as floating data. The point of [\[eq:correlation-stability\]](#eq:correlation-stability){reference-type="eqref" reference="eq:correlation-stability"} is methodological: the exact obstruction is compatible with rigorous outward rounding should the same branch ever need a certified finite rejection. The minimum projective distance is $0.3720$. Hence even an arbitrary complex final-edge scalar cannot meet the declared return threshold in any audited window. The orthogonal wrap/primal/adjoint success count remains zero.

The length-four windows at $\sigma=0.01$ illustrate the distinction. Their endpoint correlations are commonly negative and large in magnitude, so the phase mark repairs a sign. Yet a correlation magnitude near $0.9$ still corresponds to a projective distance around $0.4$, and the adjoint residual is larger still. The issue is not a missing minus sign.

# What is rejected and what remains

Within the fixed temporal span, the following rescue attempts are now closed: $$\label{eq:closed-repairs}
 \text{positive wrap}
 \longrightarrow
 \text{phase wrap}
 \longrightarrow
 \text{arbitrary scalar wrap}.$$ None reaches the physical gate. A different start time was already included in the 126-window audit.

The theorem does not constrain a left temporal space distinct from the right one. In a nonnormal problem, a Petrov--Galerkin pair can have small right and left residuals without any single orthogonal reducing range. The physical source and observation provide canonical seeds for such a pair. The next paper therefore replaces one orthogonal frame by balanced biorthogonal frames.

# Boundary

This paper proves exact phase, scalar, projective, and Gram-conditioned wrap formulas and reports their finite physical replay. It does not prove an all-level no-go theorem, reject lagged or biorthogonal clocks, validate a complement resolvent, construct a physical Riesz shell, close interface R or Gate A, or establish any Hilbert--Polya or Riemann-hypothesis statement.
