---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-101-finite-memory-packet-gram-action"
canonical_tex: "zeta_mvp0/papers/RH-101-finite-memory-packet-gram-action/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-101-finite-memory-packet-gram-action/main.pdf"
source_sha256: "eb63145b4e9b4394dbf395623754de578fddf16e25287a769190d6f504ec8124"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Finite-Memory Packet Actions for Normalized Gram Recursions Exact Matrix-Free Expansion and a Five-Snapshot Frozen Closure

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-101-finite-memory-packet-gram-action>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-101-finite-memory-packet-gram-action/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-101-finite-memory-packet-gram-action/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-101-finite-memory-packet-gram-action/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-101-finite-memory-packet-gram-action/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The source-seeded projected-cross Ritz chain of RH-94 avoids repeated ambient eigenspace resets, but every refresh still appears to require the ambient memory Gramian. We remove that assembly step exactly.

  Let $$Q_t=\frac{X_t^*X_t}{\left\lVert X_t\right\rVert_F^2},\qquad
   G_t=Q_t+\eta G_{t-1},\qquad G_{-1}=0,quad 0\le\eta<1.$$ For every trial packet $V$ and memory depth $m\le t+1$ we prove $$G_tV=\sum_{j=0}^{m-1}\eta^j
   \frac{X_{t-j}^*(X_{t-j}V)}{\left\lVert X_{t-j}\right\rVert_F^2}
   +\eta^mG_{t-m}V,$$ with the last term absent when $m=t+1$. Thus a complete-history action is exact and matrix free. Dropping the old-history term gives a positive operator error $E_{t,m}=\eta^mG_{t-m}$ satisfying $$\operatorname{tr}E_{t,m}\le\frac{\eta^m}{1-\eta},\qquad
   \left\lVert E_{t,m}V\right\rVert_F\le\frac{\eta^m\sqrt r}{1-\eta}$$ for an isometric rank-$r$ packet. The same tail controls projected-cross actions, Ritz compressions, and residual energies.

  We audit the theorem on all 120 RH-94 updates, using $\eta=1/512$, packet ranks four through seven, width-four enrichment, and 384-bit endpoint evaluation. Complete-history state actions agree with assembled Gram actions to $8.88\times10^{-16}$ in Frobenius norm. Every discarded-action norm lies below its geometric bound. Among depths two through eight, depth five is the first common depth preserving all ten $1.01$ endpoint gates; depth four fails one channel with ratio $1.05493$, whereas depth five has worst ratio $1.001172$.

  The result closes the ambient-Gram assembly subproblem, not the nonlinear stability problem. Nearly machine-precision action differences can still rotate recursively selected Ritz projectors by $1.75\times10^{-4}$. A uniform gap-aware quotient law therefore remains necessary. No uniform Stage A theorem, moving-cloud construction, Hilbert--Polya operator, zero identification, or Riemann Hypothesis result is claimed.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Finite-Memory Packet Actions for Normalized Gram Recursions\
  Exact Matrix-Free Expansion and a Five-Snapshot Frozen Closure
```

## Markdown 正文

**Keywords:** matrix-free Gram action; finite memory; Ritz packet; geometric tail; positive operator; adaptive subspace iteration.

**MSC 2020:** 47A58; 65F15; 65F50; 15A18; 37M25.

# Introduction

The recursive packet route developed in RH-93--RH-100 has separated several operations that were initially hidden inside an ambient eigensolve. The source packet can be seeded once from the source right singular space, four projected-cross directions carry it through every archived prefix, and weak fourth modes can be quotiented with local energy certificates [@WangSourceSeeded2026; @WangReducedCross2026; @WangWeakMode2026]. The hundred-layer review nevertheless retained a structural gate: how should the normalized memory Gramian act on a changing clock-rank packet without ever forming the full Gram matrix [@WangHundredLayer2026]?

This question is algebraic before it is asymptotic. The memory Gramian is not arbitrary. It obeys a scalar-decay recursion driven by normalized state snapshots. Iterating that recursion after applying it to a packet produces an exact state-action formula. The old history is itself a positive Gramian multiplied by $\eta^m$, so trace normalization immediately yields a uniform geometric tail.

Three distinctions are essential.

1.  *Assembly versus action.* We remove $X_t^*X_t$ and $G_t$ as ambient stored matrices. We do not remove the products $X_tV$ and $X_t^*(X_tV)$.

2.  *Action versus selected subspace.* A small perturbation of $G_tV$ need not imply a comparably small perturbation of a Ritz projector when a cross or output gap is weak [@Kato1995; @StewartSun1990].

3.  *Uniform formula versus uniform Stage A.* The expansion and tail bound hold at every level. Their use inside the nonlinear recursive packet chain still requires the scale-uniform gap-aware quotient gate isolated in RH-96 and RH-100.

The exact theorem and its positive-tail consequences occupy [\[sec:identity,sec:tail\]](#sec:identity,sec:tail){reference-type="ref" reference="sec:identity,sec:tail"}. describes a genuinely matrix-free Ritz refresh and its cost. The finite audit in [\[sec:audit,sec:results\]](#sec:audit,sec:results){reference-type="ref" reference="sec:audit,sec:results"} identifies depth five as the first common tested memory and also records a nontrivial sensitivity warning.

# Normalized memory Gramians {#sec:setting}

Let $X_t\in\mathbb C^{p_t\times d}$ be nonzero and define $$Q_t=\frac{X_t^*X_t}{\left\lVert X_t\right\rVert_F^2}.
 \label{eq:snapshot}$$ Every $Q_t$ is positive semidefinite and $\operatorname{tr}Q_t=1$. Fix $0\le\eta<1$ and initialize $$G_{-1}=0,\qquad G_t=Q_t+\eta G_{t-1}.
 \label{eq:memory}$$ The archived packet chain uses $\eta=1/512$.

Let $V\in\mathbb C^{d\times r}$ satisfy $V^*V=I_r$. In a projected-cross refresh one needs $$G_tV,\qquad K_t(V)=(I-VV^*)G_tV.
 \label{eq:needed-actions}$$ After selecting a few left singular directions of $K_t(V)$ and forming an isometric enrichment $W$, one also needs the compressed matrix $W^*G_tW$. All three objects can be obtained from actions on thin matrices; none logically requires an ambient $d\times d$ Gramian.

# Exact finite-history action {#sec:identity}

For $1\le m\le t+1$, define the recent-history action $$\mathcal A_{t,m}(V)=
 \sum_{j=0}^{m-1}\eta^j
 \frac{X_{t-j}^*(X_{t-j}V)}{\left\lVert X_{t-j}\right\rVert_F^2}.
 \label{eq:recent-action}$$

[\[thm:action\]]{#thm:action label="thm:action"} For every $t\ge0$, $1\le m\le t+1$, and trial matrix $V$, $$G_tV=\mathcal A_{t,m}(V)+\eta^mG_{t-m}V,
 \label{eq:action-identity}$$ where $G_{-1}=0$. In particular, $$G_tV=\mathcal A_{t,t+1}(V)
 \label{eq:full-history}$$ is an exact matrix-free complete-history formula.

Applying [\[eq:memory\]](#eq:memory){reference-type="eqref" reference="eq:memory"} to $V$ gives $$G_tV=Q_tV+\eta G_{t-1}V.$$ Substitute the same identity into the final term $m-1$ times. Since $Q_sV=X_s^*(X_sV)/\left\lVert X_s\right\rVert_F^2$, the resulting sum is [\[eq:recent-action\]](#eq:recent-action){reference-type="eqref" reference="eq:recent-action"}, followed by $\eta^mG_{t-m}V$. For $m=t+1$ the remainder is $\eta^{t+1}G_{-1}V=0$.

The packet may change arbitrarily between refreshes. The theorem is applied to the current $V$ and does not assume that $G_{t-1}V$ was stored for the previous packet. This is exactly why the state-action expansion is useful.

[\[cor:trace\]]{#cor:trace label="cor:trace"} For every $s\ge0$, $$\operatorname{tr}G_s=\sum_{j=0}^{s}\eta^j
 =\frac{1-\eta^{s+1}}{1-\eta}le\frac1{1-\eta}.
 \label{eq:trace-clock}$$

Take traces in [\[eq:memory\]](#eq:memory){reference-type="eqref" reference="eq:memory"}, use $\operatorname{tr}Q_s=1$, and iterate.

# Positive geometric tail {#sec:tail}

Write $$\widetilde G_{t,m}=\sum_{j=0}^{m-1}\eta^jQ_{t-j},
 \qquad E_{t,m}=G_t-\widetilde G_{t,m}.$$ When $m=t+1$, set $E_{t,m}=0$.

[\[thm:tail\]]{#thm:tail label="thm:tail"} If $1\le m\le t$, then $$E_{t,m}=\eta^mG_{t-m}\succeq0
 \label{eq:positive-tail}$$ and $$\begin{aligned}
 \operatorname{tr}E_{t,m}
 &=\eta^m\frac{1-\eta^{t-m+1}}{1-\eta}
 \le\frac{\eta^m}{1-\eta},
 \label{eq:trace-tail}\\
 \left\lVert E_{t,m}V\right\rVert_F
 &\le\frac{\eta^m\sqrt r}{1-\eta}.
 \label{eq:action-tail}\end{aligned}$$ The same Frobenius bound holds for the projected-cross error $$(I-VV^*)G_tV-(I-VV^*)\widetilde G_{t,m}V.$$

Equation [\[eq:positive-tail\]](#eq:positive-tail){reference-type="eqref" reference="eq:positive-tail"} is [\[thm:action\]](#thm:action){reference-type="ref" reference="thm:action"} before applying the operators to $V$. Positivity and [\[cor:trace\]](#cor:trace){reference-type="ref" reference="cor:trace"} give $\left\lVert G_{t-m}\right\rVert_2\le\operatorname{tr}G_{t-m}$, proving [\[eq:trace-tail\]](#eq:trace-tail){reference-type="eqref" reference="eq:trace-tail"}. Since $\left\lVert V\right\rVert_F=\sqrt r$, $$\left\lVert E_{t,m}V\right\rVert_F
 \le\left\lVert E_{t,m}\right\rVert_2\left\lVert V\right\rVert_F
 \le\operatorname{tr}(E_{t,m})\sqrt r.$$ Finally, left multiplication by the orthogonal projector $I-VV^*$ is nonexpansive in Frobenius norm.

[\[cor:depth\]]{#cor:depth label="cor:depth"} Given an absolute action tolerance $\varepsilon>0$, it is enough to choose $$m\ge
 \left\lceil
 \frac{\log\!\bigl(\sqrt r/((1-\eta)\varepsilon)\bigr)}
      {\log(1/\eta)}
 \right\rceil_+,
 \label{eq:depth-choice}$$ where $\lceil\cdot\rceil_+$ is at least one. This choice is independent of the horizon $t$.

The positivity contains more information than an action norm alone. Let $P=VV^*$ and define the residual energy $R_G(P)=\operatorname{tr}((I-P)G)$.

[\[prop:consequences\]]{#prop:consequences label="prop:consequences"} Let $W$ be any isometry with $q$ columns. Then $$\begin{aligned}
 0&\le R_{G_t}(P)-R_{\widetilde G_{t,m}}(P)
 \le\operatorname{tr}E_{t,m},
 \label{eq:residual-tail}\\
 0&\preceq W^*G_tW-W^*\widetilde G_{t,m}W
 \preceq \left\lVert E_{t,m}\right\rVert_2I_q.
 \label{eq:compression-tail}\end{aligned}$$ Consequently every ordered Ritz value moves upward by at most $\operatorname{tr}E_{t,m}$, and any rank-$r$ Ky Fan sum moves by at most $r\operatorname{tr}E_{t,m}$.

The residual difference equals $\operatorname{tr}((I-P)E_{t,m})$, which lies between zero and $\operatorname{tr}E_{t,m}$ because both factors are positive semidefinite. The compression statement follows from $0\preceq E_{t,m}\preceq
\left\lVert E_{t,m}\right\rVert_2I$. Eigenvalue and Ky Fan bounds then follow from monotonicity and Weyl's inequality [@Bhatia1997; @HornJohnson2013].

# Matrix-free refresh and cost {#sec:implementation}

A width-$k$ refresh can now be executed as follows.

1.  Evaluate $Y=\mathcal A_{t,m}(V)$ by the state products in [\[eq:recent-action\]](#eq:recent-action){reference-type="eqref" reference="eq:recent-action"}.

2.  Form $K=Y-V(V^*Y)$ and select its leading $k$ left singular vectors.

3.  Orthonormalize those directions with $V$ to obtain $W\in\mathbb C^{d\times(r+k)}$.

4.  Evaluate $Z=\mathcal A_{t,m}(W)$ and diagonalize only the small matrix $W^*Z$.

The algorithm never forms $Q_s$, $\widetilde G_{t,m}$, or $G_t$. If $X_s$ has $p_s$ rows and the trial width is $q$, one state action costs $O(p_sdq)$ arithmetic and $O(dq)$ additional packet storage. A depth-$m$ action costs the sum over the retained snapshots. By comparison, explicitly forming $X_s^*X_s$ costs $O(p_sd^2)$ and storing an ambient Gramian costs $O(d^2)$.

This does not make the continuum problem free. Recent states must be available or regenerable, and the products $X_sV$ may themselves be costly. Moreover, [\[eq:action-tail\]](#eq:action-tail){reference-type="eqref" reference="eq:action-tail"} is an absolute operator-action estimate. To deduce a projector estimate for the nonlinear refresh, one still needs separation of the cross selection and output Ritz selection. RH-99 shows that naive differential constants can be unusable near weak gaps [@WangTwoGap2026].

# Frozen-prefix audit {#sec:audit}

We reuse the two finite channels at each of the five RH-94 scales $$\sigma\in\{0.16,0.08,0.04,0.02,0.01\}.$$ Their refresh endpoints are respectively $4,6,11,17,22$, and the half-log packet ranks are $4,5,6,6,7$. The source right singular packet is propagated recursively with width-four projected-cross enrichment. There are 120 updates in total.

For each update we perform three checks.

1.  Compare the complete-history state action $\mathcal A_{t,t+1}(V)$ with an independently assembled $G_tV$.

2.  For every $m\in\{2,3,4,5,6,7,8\}$, evaluate the discarded action $\eta^mG_{t-m}V$ and compare it with the finite and uniform bounds of [\[thm:tail\]](#thm:tail){reference-type="ref" reference="thm:tail"}.

3.  Run a complete recursive matrix-free chain at each depth, then evaluate its endpoint residual against the assembled full Gramian and the ambient leading-packet reference. The inherited gate is endpoint/reference $\le1.01$.

The production chains are binary64. Endpoint residuals are evaluated as quadratic forms in Arb at 384-bit precision, following RH-94 [@Rump2010]. Ambient Gramians are assembled only for independent audit and are not used by the structured refresh.

# Results {#sec:results}

## Exact action and geometric certificate

Across all 120 updates, the largest Frobenius discrepancy between a complete-history state action and the independently assembled action is $$8.88\times10^{-16}.$$ Every nonzero discarded action satisfies [\[eq:action-tail\]](#eq:action-tail){reference-type="eqref" reference="eq:action-tail"}. The largest observed ratio to the finite trace bound is $0.494$. The trace of every discarded positive matrix agrees with [\[eq:trace-tail\]](#eq:trace-tail){reference-type="eqref" reference="eq:trace-tail"} to floating-point roundoff.

::: {#tab:depth}
    $m$   omissions       max action error   error/bound   green   worst endpoint ratio
  ----- ----------- ---------------------- ------------- ------- ----------------------
      2         110    $3.77\times10^{-6}$         0.494    8/10               1.132832
      3         100    $7.13\times10^{-9}$         0.477    8/10               1.030882
      4          90   $1.37\times10^{-11}$         0.383    9/10               1.054930
      5          80   $2.66\times10^{-14}$         0.382   10/10               1.001172
      6          72   $5.20\times10^{-17}$         0.382   10/10               1.001173
      7          64   $9.94\times10^{-20}$         0.374   10/10               1.001172
      8          58   $1.94\times10^{-22}$         0.374   10/10               1.001173

  : Depth audit over the ten channels. "Omissions" counts updates at which the retained history is genuinely shorter than the available history.
:::

## First common tested depth

Depth five is the first tested common depth preserving all ten endpoint gates. Depth four fails the right channel at $\sigma=0.16$, reaching $1.05492958$. At depth five the worst endpoint/reference ratio is $1.00117186$. The complete-history structured chain has worst ratio $1.00117229$, consistent with the RH-94 assembled chain.

The endpoint ratios are not monotone in $m$. In particular, the worst depth four endpoint is larger than the worst depth three endpoint even though its operator-action tail is much smaller. This is not a contradiction: each depth follows a different nonlinear sequence of singular-vector and Ritz choices. The theorem gives monotone action accuracy, not monotone recursive projector accuracy.

![Left: endpoint ratios for every channel and their maximum; depth five is the first common tested depth below the inherited $1.01$ gate. Right: the discarded packet action decays geometrically beneath the uniform theorem bound.](<../../../../../zeta_mvp0/papers/RH-101-finite-memory-packet-gram-action/figures/finite_memory_packet_gram_action.pdf>){#fig:audit width="\\textwidth"}

## A sensitivity boundary

The largest action discrepancy between complete-history and assembled implementations is below $10^{-15}$, yet the recursively obtained endpoint projectors can differ by $$\left\lVert P_{\rm assembled}-P_{\rm structured}\right\rVert_2
 =1.75\times10^{-4}.$$ Both packets retain essentially the same endpoint residual. This is direct evidence that packet coordinates and even projectors can be sensitive along weak branches while the captured energy is stable. It reinforces the program's division of labor: the present paper supplies the structured Gram action; the remaining quotient theorem must formulate stability in a gap-aware or energy-aware metric rather than demand coordinatewise agreement.

# Route consequence and claim boundary

The structured packet Gram-action gate selected by RH-100 is closed in the following narrow sense: for every level and every trial packet there is an exact matrix-free history action, together with a horizon-independent geometric truncation law. Five retained snapshots suffice on the complete archived prefix.

What is not closed is equally explicit. The theorem does not remove state propagation, source-coordinate singular vectors, or the state-packet products. It does not turn an absolute action tolerance into a uniform recursive Ritz-projector tolerance. That conversion is the separate scale-uniform gap-aware quotient gate $Q$ in the RH-100 dependency ledger. Nor does a ten-channel fixed-scale audit prove an all-level Stage A theorem.

Moving-cloud Riesz projections, coefficient bridges, trace-class complements, self-adjoint counting, arithmetic zero identification, and the Hilbert--Polya program remain downstream. In particular, this paper proves neither a Hilbert--Polya operator nor the Riemann Hypothesis.

# Conclusion

Normalized Gram memory has more structure than a generic dense positive matrix. On a thin packet, its action is an exact sum of state actions, and its forgotten history is a positive geometric tail. This removes ambient Gram assembly from the recursive packet route and yields explicit residual, compression, and complexity bounds.

The finite audit is positive but appropriately limited. Depth five is the first common tested memory that preserves every RH-94 endpoint gate. At the same time, tiny implementation-level action differences can rotate weak Ritz branches substantially. The next route layer should therefore retain this matrix-free action while replacing unrestricted quotienting by an exact stopped budget clock.
