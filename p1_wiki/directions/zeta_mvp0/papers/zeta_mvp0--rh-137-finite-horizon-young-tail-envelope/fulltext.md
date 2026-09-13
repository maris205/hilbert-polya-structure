---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-137-finite-horizon-young-tail-envelope"
canonical_tex: "zeta_mvp0/papers/RH-137-finite-horizon-young-tail-envelope/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-137-finite-horizon-young-tail-envelope/main.pdf"
source_sha256: "848b71ffcd789fd7fed13da4c349ce03b1b181e191e7b68967997e8dea31bb91"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Finite-Horizon Young Tail Envelopes Crossing 31 Long-Run Metric Walls and Isolating Two Birth Obstructions

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-137-finite-horizon-young-tail-envelope>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-137-finite-horizon-young-tail-envelope/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-137-finite-horizon-young-tail-envelope/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-137-finite-horizon-young-tail-envelope/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-137-finite-horizon-young-tail-envelope/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-136 proved that 33 of 216 recurrent packet transitions cannot support a contractive affine tail recurrence under any orthogonal gauge. Long-run contractivity, however, is stronger than finite-step viability. For a fixed gauge the Young family has the form $$x'\leq A(1+\tau)x+q+B(1+\tau^{-1}),\qquad \tau>0.$$ We eliminate $\tau$ exactly: $$x'\leq\mathcal F_{A,B,q}(x)
   :=q+(\sqrt{Ax}+\sqrt B)^2.$$ This bound is sharp for the Young split. It gives the exact safety radius $$R(A,B,q)=\frac{(\sqrt{1-q}-\sqrt B)^2}{A}$$ when $A>0$ and $q+B<1$. Thus a transition with $A\geq1$ may still be crossed whenever the incoming certified tail is below $R$.

  Every candidate map is monotone. We prove that choosing the smallest map at each step minimizes the propagated envelope at every later finite horizon within the fixed candidate family. Applying this theorem to the 33-gauge RH-136 family gives an 80-decimal audit of 330 transitions in 30 chains. The propagated bound dominates the actual tail at every transition. It certifies 328/330 transitions and 28/30 complete chains, exactly matching the actual safe/unsafe split. In particular, 31 of the 33 transitions with no contractive long-run gauge are crossed safely. The other two cannot be repaired within this recurrence: their gauge-independent birth term is $9.40589>1$, and the actual target relative tail is $9.43632>1$. The Euclidean polar gauge alone certifies only 318 transitions and 21 chains. The finite-horizon route therefore bypasses most isolated metric walls while exposing a genuinely different obstruction at coarse boundary injection.
author:
- Prime Dynamics Theory Program
bibliography:
- references.bib
date: July 2026
title: |
  Finite-Horizon Young Tail Envelopes\
  Crossing 31 Long-Run Metric Walls and Isolating Two Birth Obstructions
```

## Markdown 正文

# Why a noncontractive step can still be safe

Let $x=\gamma^2$ denote the squared relative tail constant. After choosing a packet gauge, RH-134--RH-136 give $$\label{eq:young}
 x'\leq A(1+\tau)x+q+B(1+\tau^{-1}),
 \qquad \tau>0.$$ Here $A$ is the metric-decay base, $B$ is the target-normalized frame-forcing base, and $q$ is the boundary-birth forcing. RH-136 studied whether some $\tau$ makes $A(1+\tau)<1$, which is equivalent to $A<1$. That criterion is appropriate for a stationary affine fixed floor, but a finite chain asks a different question: given the certified current value $x$, is the next upper bound below one?

The distinction matters because the old tail may be extremely small. A large multiplier can act once without reaching the support wall. The Young parameter should therefore be optimized for the current state rather than for a hypothetical repeated constant-coefficient recurrence.

# Exact pointwise Young optimization

The scalar optimization is an equality case of the arithmetic--geometric mean inequality [@HardyLittlewoodPolya1952].

[\[thm:envelope\]]{#thm:envelope label="thm:envelope"} For $A,B,q,x\geq0$, $$\begin{aligned}
 \inf_{\tau>0}\bigl[A(1+\tau)x+q+B(1+\tau^{-1})\bigr]
 &=q+(\sqrt{Ax}+\sqrt B)^2\\
 &:=\mathcal F_{A,B,q}(x).\end{aligned}$$ If $AxB>0$, the unique minimizer is $\tau_*=\sqrt{B/(Ax)}$. If one of $Ax,B$ vanishes, the same formula is the corresponding boundary infimum. The result is sharp already for a scalar matrix recurrence whose Young inequality is attained.

Expanding [\[eq:young\]](#eq:young){reference-type="eqref" reference="eq:young"}, the only $\tau$-dependent terms are $Ax\tau+B/\tau$. Their product is $ABx$, so $$Ax\tau+\frac B\tau\geq2\sqrt{ABx},$$ with equality at the stated $\tau_*$. Adding $Ax+B+q$ gives the formula. Scalar equality in the underlying quadratic Young inequality gives sharpness.

The optimized map is increasing and concave in $x$. It retains the same long-run information as the optimized affine fixed floor, but it is strictly more informative at a specified finite state.

[\[cor:radius\]]{#cor:radius label="cor:radius"} Assume $A>0$. If $q+B<1$, then $$\mathcal F_{A,B,q}(x)<1
 \quad\Longleftrightarrow\quad
 x<R(A,B,q):=\frac{(\sqrt{1-q}-\sqrt B)^2}{A}.$$ If $q+B\geq1$, no nonnegative incoming $x$ is certified safe. If $A=0$ and $q+B<1$, every incoming $x$ is safe because the old tail is absent.

The inequality is equivalent to $\sqrt{Ax}+\sqrt B<\sqrt{1-q}$. Solving for $x$ proves the statement.

This radius quantifies the difference between a wall and a fatal wall. When $A\geq1$, no contractive affine fixed floor exists, but $R$ can still be positive and the step can be crossed from a sufficiently small state.

[\[prop:fixed\]]{#prop:fixed label="prop:fixed"} If $A<1$, $\mathcal F_{A,B,q}$ has the unique nonnegative fixed point $$x_*=\left(
 \frac{\sqrt{AB}+\sqrt{B+(1-A)q}}{1-A}
 \right)^2.$$ This is the minimum constant affine fixed floor obtainable from [\[eq:young\]](#eq:young){reference-type="eqref" reference="eq:young"}. If $A\geq1$ and $B+q>0$, then $\mathcal F_{A,B,q}(x)>x$ for every $x\geq0$, although one or more finite steps may remain below one.

Set $z=\sqrt{x}$ in $x=\mathcal F(x)$ and solve the resulting quadratic $(1-A)z^2-2\sqrt{AB}z-(B+q)=0$. The positive root gives the formula. At a fixed point, Theorem [\[thm:envelope\]](#thm:envelope){reference-type="ref" reference="thm:envelope"} chooses the same Young parameter as the fixed-floor minimization, proving equality of the two optima. For $A\geq1$, direct subtraction gives $\mathcal F(x)-x=(A-1)x+B+q+2\sqrt{ABx}>0$ in the nondegenerate case.

# Greedy propagation is finite-horizon optimal

At time $t$, let $\mathcal C_t$ be a finite family of gauge candidates. Each $c\in\mathcal C_t$ supplies nonnegative coefficients $(A_{t,c},B_{t,c},q_t)$ and hence a monotone map $F_{t,c}$. Define $$\label{eq:greedy}
 y_0\geq x_0,
 \qquad
 y_{t+1}=\min_{c\in\mathcal C_t}F_{t,c}(y_t).$$

[\[thm:greedy\]]{#thm:greedy label="thm:greedy"} For every horizon $n$, the value $y_n$ in [\[eq:greedy\]](#eq:greedy){reference-type="eqref" reference="eq:greedy"} is the smallest upper envelope obtainable by any sequence of candidates from $\mathcal C_0,\ldots,\mathcal C_{n-1}$ with pointwise-optimal Young parameters. If every candidate recurrence is valid and $y_0\geq x_0$, then $y_t\geq x_t$ for all $t$.

Every $F_{t,c}$ is increasing. Suppose the greedy value at time $t$ is no larger than the value from any other candidate history. Applying any next map to the greedy value cannot exceed applying that same map to the larger competitor value. Taking the minimum over next maps preserves the inequality. Induction proves horizon optimality. The same monotonicity, combined with the valid one-step recurrence, proves domination of the true state.

This is a dynamic-programming conclusion without a backward search: the state is scalar and all controls are order preserving. The theorem is exact for a specified finite gauge family. It does not assert that the 33 RH-136 candidates exhaust $O(4)$ or any nonorthogonal enlargement.

# Thirty-chain packet audit

We use the same 30 packet chains, rank four, depth eight, and $\eta=1/512$ as RH-134--RH-136. A recurrent step has the Euclidean polar gauge, two determinant-compatible metric endpoints, and polar projections of 17 interpolation points toward each endpoint, with duplicates removed. A birth step has only its gauge-independent boundary term. Starting from $y_0=0$, we propagate [\[eq:greedy\]](#eq:greedy){reference-type="eqref" reference="eq:greedy"}; no actual intermediate $x_t$ is fed back into the certificate. All $4\times4$ generalized spectra are recomputed at 80 decimal digits, which is a high-precision audit rather than an interval proof [@Higham2002].

::: {#tab:audit}
    $\sigma$   transitions   greedy safe   polar safe   actual safe   crossed walls
  ---------- ------------- ------------- ------------ ------------- ---------------
        0.16            18            18           18            18               0
        0.08            30            28           26            28             4/6
        0.04            60            60           52            60           15/15
        0.02            96            96           96            96             9/9
        0.01           126           126          126           126             3/3
       total           330           328          318           328           31/33

  : Finite-horizon safety by scale. "Crossed walls" counts recurrent steps with no possible contractive orthogonal gauge that nevertheless retain a subunit propagated envelope.
:::

There are zero dominance failures: all 330 propagated bounds exceed the directly computed target relative tail. The greedy strategy certifies 328 transitions and 28 complete chains. The actual data have exactly the same 328/330 and 28/30 safe split. By contrast, propagating the Euclidean polar gauge alone certifies 318 transitions and only 21 chains. Using only the best metric endpoint reaches the same safety count as greedy, but the interpolated greedy choice improves its recurrent bound on 187 of 216 steps. It improves the polar bound on all 216 recurrent steps; the median greedy-to-polar ratio is $0.1321$.

![The nonlinear envelope is composable, crosses 31 isolated long-run walls, and reproduces the finite safe/unsafe classification without using actual intermediate tails as inputs.](<../../../../../zeta_mvp0/papers/RH-137-finite-horizon-young-tail-envelope/figures/finite_horizon_young_tail_envelope.pdf>){#fig:audit width="\\textwidth"}

Among the 328 safe transitions, the largest propagated envelope is $0.62639$ and the median positive envelope is $1.20\times10^{-14}$. For the 31 crossed long-run walls, the incoming envelope is at most $0.01270$ of the sharp safety radius; most ratios are far smaller. Thus these crossings are not numerically marginal.

The two failures are both the final recurrent transition of coarse $\sigma=0.08$ left-channel chains, at thresholds $10^{-8}$ and $10^{-6}$. Their selected metric base is $7176.13$, but this is not the decisive obstruction: the target-frame birth term itself is $q=9.40589>1$. Therefore Corollary [\[cor:radius\]](#cor:radius){reference-type="ref" reference="cor:radius"} gives zero safety radius for every old-frame gauge in the current recurrence. The propagated bound is $10.13353$, while the actual target relative tail is $9.43632>1$. These are physical finite failures of the present rank-four/depth-eight packet, not false negatives caused by the envelope.

# Route consequence and claim boundary

RH-137 removes the need to demand long-run contraction at every finite step. Thirty-one of the 33 RH-136 walls are harmless when visited from the actual certified state, so isolated metric expansion is not the main finite-chain bottleneck. The remaining obstruction is qualitatively different: a large new boundary slice enters the target weak Gram direction and is already superunit before old-tail propagation matters.

There are three natural responses: start the certificate after the coarse birth event, enlarge or reshape the target packet so that the birth slice is better normalized, or introduce a validated reset whose direct target bound is subunit. Any such modification must be audited together with the directional normalized base. The next synthesis should combine the finite-horizon tail envelope, a positive finite base, and the RH-127 outward Loewner guards while keeping finite and all-level claims separate.

We have not globally optimized over all orthogonal gauges, bypassed the two birth failures, proved an infinite-horizon uniform recurrence, proved a positive normalized-base liminf, closed uniform Stage A, constructed a Hilbert--Polya operator, identified zeta zeros, or proved the Riemann Hypothesis.
