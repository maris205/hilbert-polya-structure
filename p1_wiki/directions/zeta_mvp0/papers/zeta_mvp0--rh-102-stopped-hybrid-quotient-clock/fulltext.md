---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-102-stopped-hybrid-quotient-clock"
canonical_tex: "zeta_mvp0/papers/RH-102-stopped-hybrid-quotient-clock/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-102-stopped-hybrid-quotient-clock/main.pdf"
source_sha256: "51d4e94b114bd92a91dc1a55f10703c9d6b130c813361e9bc7af9171bc0538f6"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Stopped Hybrid Quotient Clocks Exact Endpoint-Slack Control Without a Ritz Lipschitz Law

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-102-stopped-hybrid-quotient-clock>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-102-stopped-hybrid-quotient-clock/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-102-stopped-hybrid-quotient-clock/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-102-stopped-hybrid-quotient-clock/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-102-stopped-hybrid-quotient-clock/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Weak projected-cross modes can be removed locally by the gap-weighted theorem of RH-96, but local losses do not compose monotonically through the nonlinear Ritz refresh. RH-97 resolves this by exact hybrid replay, while RH-98--RH-99 show that the available smooth propagation constants are unusable. We turn the exact replay into a stopped quotient clock.

  Let $H_0$ be the endpoint value of the full-width chain and $H_k$ the hybrid endpoint after the first $k$ accepted quotients, followed by a full-width suffix. The exact debit of the $k$th candidate is $d_k\ge |H_k-H_{k-1}|$. If a clock accepts only while $B_k=\sum_{j\le k}d_j\le A$, then at every stopping time $$|H_k-H_0|\le B_k\le A.$$ For a reference lower bound $R_-$, baseline upper bound $H_0^+$, target $\Gamma>1$, and safety fraction $0\le\rho<1$, choose $$A=\rho\bigl(\Gamma R_--H_0^+\bigr)_+.$$ Whenever the baseline has positive slack, the stopped endpoint is rigorously below $\Gamma R_-$. No differentiability, monotonicity, or Lipschitz law for the recursive Ritz map is used.

  We compose this clock with RH-96 local gap certificates on all ten frozen channels, at relative quotient thresholds $10^{-8},10^{-6},10^{-4}$, using $\Gamma=1.01$, $\rho=0.99$, and 384-bit endpoint evaluation. All five primary $10^{-8}$ quotients are accepted with no stop. At $10^{-6}$ the unrestricted chain reaches $1.024921$; the clock rejects one candidate, stops one channel, and keeps all ten endpoints green with worst ratio $1.001172$. At $10^{-4}$ the unrestricted worst ratio is $1.014092$; two candidates are rejected and the stopped worst ratio is $1.006033$. All 30 channel--threshold clocks have exact hybrid telescoping, green local certificates for accepted quotients, and certified endpoint gates.

  The price is explicit: every candidate is still evaluated by a full-suffix hybrid replay, and the absolute clock can stop conservatively before a signed cancellation. Thus the stopped-horizon logic is closed, while the uniform quotient-supply and replay-cost problems remain. No unconditional Stage A, moving-cloud construction, Hilbert--Polya operator, zero identification, or Riemann Hypothesis result is claimed.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Stopped Hybrid Quotient Clocks\
  Exact Endpoint-Slack Control Without a Ritz Lipschitz Law
```

## Markdown 正文

**Keywords:** stopped budget; nonlinear telescoping; adaptive Ritz quotient; endpoint certificate; hybrid replay; weak spectral mode.

**MSC 2020:** 47A75; 65F15; 65G20; 37M25; 15A18.

# Introduction

The adaptive packet route has two distinct notions of safety. A local quotient must not discard too much Ritz energy, and the accumulated nonlinear chain must remain inside its endpoint gate. RH-96 supplies the first notion: a retained-to-omitted spectral gap converts a weak omitted block into a certified local Ky Fan loss [@WangWeakMode2026]. RH-97 supplies an exact answer to the second: insert quotients one at a time, replay the remaining full-width suffix, and telescope the resulting endpoint differences [@WangHybridBudget2026].

The missing step is operational. An unrestricted threshold rule may accept several locally certified quotients and nevertheless overspend the endpoint allowance. This happens in the archived $10^{-6}$ and $10^{-4}$ chains. Trying to predict the propagation by a universal or differential Lipschitz constant is not currently viable: a positive finite-dimensional example amplifies projector loss by $44.49$, and the available two-gap constants can reach $10^{40}$ [@WangProjectorBarrier2026; @WangTwoGap2026].

This paper takes the finite exact route seriously. Each proposed quotient is priced by one exact hybrid replay. It is accepted only when its absolute endpoint debit fits the remaining rigorous slack; otherwise the process switches permanently to full width. The resulting theorem is a stopped nonlinear analogue of a variation-budget argument. It requires no local linearization and remains valid even when a future refresh reverses the sign of a local loss.

The theorem is developed abstractly in [\[sec:hybrids,sec:clock\]](#sec:hybrids,sec:clock){reference-type="ref" reference="sec:hybrids,sec:clock"}. The composition with gap-weighted local certificates appears in [4](#sec:composition){reference-type="ref" reference="sec:composition"}. The audit in [\[sec:audit,sec:results\]](#sec:audit,sec:results){reference-type="ref" reference="sec:audit,sec:results"} both salvages the two aggressive thresholds and exposes one deliberately conservative stop.

# Hybrid endpoints {#sec:hybrids}

Let $F_t$ denote the full-width update at time $t$, let $A_t$ denote a candidate quotient update, and let $J$ be a real endpoint functional. These maps may be nonlinear and may depend on time. Starting from $x$, suppose quotients have been accepted at times $$1\le t_1<\cdots<t_k\le N.$$ Define $H_k$ to be the endpoint obtained from the accepted decisions through $t_k$ and the full maps at every other time, in particular throughout the suffix after $t_k$. Thus $H_0=J(F_N\cdots F_1x)$ is the all-full baseline.

The exact propagated contribution of the $k$th accepted quotient is $$\delta_k=H_k-H_{k-1}.
 \label{eq:contribution}$$ It is computed by comparing two chains with the same previously accepted prefix: one uses $F_{t_k}$ and a full suffix, the other uses $A_{t_k}$ and the same full suffix. This is a nonlinear hybrid comparison, not a derivative.

[\[prop:telescoping\]]{#prop:telescoping label="prop:telescoping"} For every accepted sequence, $$H_k-H_0=\sum_{j=1}^k\delta_j.
 \label{eq:telescoping}$$ Consequently, for any certified debits $d_j\ge|\delta_j|$, $$|H_k-H_0|\le\sum_{j=1}^kd_j.
 \label{eq:absolute}$$

Equation [\[eq:telescoping\]](#eq:telescoping){reference-type="eqref" reference="eq:telescoping"} is the scalar telescoping sum of [\[eq:contribution\]](#eq:contribution){reference-type="eqref" reference="eq:contribution"}. The triangle inequality gives [\[eq:absolute\]](#eq:absolute){reference-type="eqref" reference="eq:absolute"}.

The signs need not be positive. In the primary audit two of the five accepted contributions are negative. Hence summing local positive losses is not an exact endpoint law, while summing absolute hybrid debits is.

# Stopped endpoint-slack theorem {#sec:clock}

Let $R>0$ be a reference endpoint scale and let the target gate be $$H\le\Gamma R,qquad \Gamma>1.
 \label{eq:gate}$$ In validated computation we use a lower bound $R_-$ for $R$ and an upper bound $H_0^+$ for the all-full baseline. Define the rigorous slack $$S=\bigl(\Gamma R_--H_0^+\bigr)_+.
 \label{eq:slack}$$ Fix $0\le\rho<1$ and set the stopped allowance $A=\rho S$.

The clock maintains $B_0=0$. At a candidate quotient it computes a debit $d\ge|H_{m candidate}-H_{m current}|$. The candidate is accepted only if $$B+d\le A.
 \label{eq:accept}$$ After the first rejection the current step and all later steps use full width.

[\[thm:stopped\]]{#thm:stopped label="thm:stopped"} Assume $S>0$. At every accepted time and at the terminal stopping time, $$\begin{aligned}
 |H_k-H_0|&\le B_k\le A,
 \label{eq:budget-bound}\\
 H_k&\le H_0^++A<\Gamma R_-\le\Gamma R.
 \label{eq:gate-bound}\end{aligned}$$ Therefore the stopped chain satisfies the endpoint gate [\[eq:gate\]](#eq:gate){reference-type="eqref" reference="eq:gate"} without a Lipschitz estimate for any update map.

The clock accepts exactly when the cumulative certified debits remain below $A$. Proposition [\[prop:telescoping\]](#prop:telescoping){reference-type="ref" reference="prop:telescoping"} gives the first inequality in [\[eq:budget-bound\]](#eq:budget-bound){reference-type="eqref" reference="eq:budget-bound"}; the clock gives the second. Since $A=\rho(\Gamma R_--H_0^+)$ and $\rho<1$, $$H_k\le H_0^++\rho(\Gamma R_--H_0^+)<\Gamma R_-.$$ The last inequality in [\[eq:gate-bound\]](#eq:gate-bound){reference-type="eqref" reference="eq:gate-bound"} follows from $R_-\le R$.

If $S=0$, the baseline itself has no certified gate slack and the clock accepts no debit. The theorem does not repair a failing baseline.

Stopping permanently at the first unaffordable candidate is stronger than necessary. One could skip that candidate and price later ones, or maintain a signed account with additional structure. The permanent stop is chosen because it makes the terminal chain exactly the last accepted hybrid and keeps the proof independent of cancellation.

# Composition with local quotient certificates {#sec:composition}

For one adaptive Ritz enrichment, write the full compression as $$\begin{pmatrix}A&C\\C^*&D\end{pmatrix}.$$ If the retained cutoff obeys $\lambda_r(A)\ge\alpha$, the omitted block obeys $D\preceq\beta I$, and $\alpha>\beta$, RH-96 proves that the local rank-$r$ Ky Fan loss is at most $$\frac{\left\lVert C\right\rVert_F^2}{\alpha-\beta}.
 \label{eq:local-gap}$$ This is the local admission certificate. It establishes that the proposed weak-mode quotient is geometrically legitimate at its current step.

The stopped algorithm requires two independent green lights:

1.  the local gap certificate [\[eq:local-gap\]](#eq:local-gap){reference-type="eqref" reference="eq:local-gap"};

2.  the exact propagated debit test [\[eq:accept\]](#eq:accept){reference-type="eqref" reference="eq:accept"}.

The first does not replace the second. A small local loss can encounter a sensitive future branch; conversely, a local loss can be partly reversed by the future full refresh. The endpoint debit prices the actual nonlinear future of the current accepted prefix.

[\[cor:composition\]]{#cor:composition label="cor:composition"} If every accepted quotient has a valid local gap certificate and every accepted propagated debit satisfies the stopped clock, then all accepted steps are locally certified and the terminal chain satisfies [\[eq:gate-bound\]](#eq:gate-bound){reference-type="eqref" reference="eq:gate-bound"}.

This corollary closes the logical $H_{\rm stop}$ gate selected in the RH-100 route review [@WangHundredLayer2026]. It does not remove the exact hybrid replay used to evaluate each debit.

# Frozen audit {#sec:audit}

We reuse the five RH-94 scales and two channels per scale. Their endpoints are $4,6,11,17,22$, their packet ranks are $4,5,6,6,7$, and the full enrichment width is four. At each proposed quotient we:

1.  evaluate the RH-96 retained-to-omitted gap certificate;

2.  replay the full suffix from both the full and quotient candidates;

3.  evaluate both endpoint tails in Arb at 384-bit precision;

4.  debit the outward upper bound on the absolute hybrid difference;

5.  accept only if the local certificate is green and the debit fits.

The endpoint gate is $\Gamma=1.01$ and the safety fraction is $\rho=0.99$. We test relative cross-mode thresholds $10^{-8}$, $10^{-6}$, and $10^{-4}$. The unrestricted comparator applies every quotient selected by its threshold. The stopped chain switches permanently to full width at its first rejected candidate.

For independent verification we check that the full-suffix baseline at each candidate equals the preceding accepted hybrid, that accepted contributions telescope to the final endpoint shift, and that the interval-certified endpoint upper bound remains below $1.01R_-$.

# Results {#sec:results}

All 30 channel--threshold clocks pass every local-global verification. The primary $10^{-8}$ rule proposes five quotients, accepts all five, and never stops. Its largest spent fraction of the stopped allowance is only $1.02\times10^{-3}$.

::: {#tab:decisions}
    threshold   candidates   accepted   rejected   stopped   unrestricted green   stopped green
  ----------- ------------ ---------- ---------- --------- -------------------- ---------------
    $10^{-8}$            5          5          0         0                10/10           10/10
    $10^{-6}$           11         10          1         1                 9/10           10/10
    $10^{-4}$           22         20          2         2                 9/10           10/10

  : Stopped-clock decisions across ten channels. The unrestricted column counts channels already below the $1.01$ endpoint gate.
:::

::: {#tab:endpoints}
    threshold   worst unrestricted   worst stopped   max spent/allowance
  ----------- -------------------- --------------- ---------------------
    $10^{-8}$           1.00117232      1.00117243               0.00102
    $10^{-6}$           1.02492119      1.00117243               0.01253
    $10^{-4}$           1.01409152      1.00603284               0.60936

  : Worst endpoint ratios and clock utilization.
:::

## The three stopping events

At $\sigma=0.08$ in the right channel, the $10^{-6}$ rule proposes one quotient at time six. Its propagated debit is $1.419\times10^{-15}$, whereas the stopped allowance is $5.637\times10^{-16}$. The quotient is rejected immediately and the final ratio is the full-width value $1.00000054$, instead of the unrestricted $1.02492119$.

For the $10^{-4}$ rule in the same channel, quotients at times three, four, and five are accepted. They spend $3.435\times10^{-16}$ of the $5.637\times10^{-16}$ allowance. The time-six debit $2.222\times10^{-16}$ is slightly larger than the remaining $2.202\times10^{-16}$, so the clock stops. Its endpoint ratio is $1.00603284$.

At $\sigma=0.04$ in the right channel, the $10^{-4}$ rule accepts a tiny time-ten debit and rejects the time-eleven debit $1.295\times10^{-16}$ against remaining allowance $9.098\times10^{-17}$. The stopped ratio is $1.00000399$, while the unrestricted ratio is $1.01409152$.

![Left: the stopped clock restores every endpoint gate at the two aggressive thresholds. Right: each rejected proposal would cross its channel-specific rigorous allowance.](<../../../../../zeta_mvp0/papers/RH-102-stopped-hybrid-quotient-clock/figures/stopped_hybrid_quotient_clock.pdf>){#fig:clock width="\\textwidth"}

## A conservative stop

The $\sigma=0.08$, right, $10^{-4}$ unrestricted endpoint is actually $1.00993513$, still below $1.01$. The absolute clock nevertheless stops because the final proposed debit marginally exceeds the remaining safe allowance. Signed future cancellation makes the unrestricted chain green, but the clock refuses to rely on it. This is the intended tradeoff: the theorem certifies every accepted prefix from absolute data, at the cost of occasionally rejecting a harmless continuation.

Across accepted events, ten propagated contributions are negative and twenty-five are positive over the three thresholds. The presence of both signs explains why unrestricted endpoint quality and absolute clock spending need not be ordered monotonically.

# Route consequence and claim boundary

The stopped-horizon gate now has an exact theorem and a finite stress test. An adaptive chain can be run safely without pretending that the recursive Ritz map has a usable uniform Lipschitz constant. The primary quotients all survive, and the aggressive thresholds are automatically curtailed before a certified endpoint failure.

Two open costs remain. First, exact full-suffix replay is performed for each candidate; RH-102 organizes that work but does not replace it by a cheap analytic envelope. Second, the theorem does not guarantee that an all-level family supplies useful locally gap-certified quotients. That is the remaining uniform gate $Q$ in the preferred packet route. RH-103 must still make the prefix, normalization, and observability factors explicit before the route can honestly say that only $Q$ remains inside Stage A.

Nothing here constructs a moving-cloud Riesz projection, coefficient bridge, trace-class complement, self-adjoint spectral operator, or arithmetic trace formula. In particular, no Hilbert--Polya operator, zero identification, or proof of the Riemann Hypothesis is claimed.

# Conclusion

Exact nonlinear replay becomes substantially more useful when treated as a budget clock. Each candidate quotient carries two prices: a local spectral certificate and an exact propagated endpoint debit. Accepting only while both are green yields a stopped theorem that is independent of differentiable Ritz stability.

The finite audit is decisive at the intended scale. All five primary weak modes are removed, while three aggressive proposals are stopped and every one of the 30 endpoint gates is certified. The remaining task is no longer to invent a propagation constant for these finite chains, but to expose the normalization/observability ledger and then confront the genuinely uniform gap-aware quotient law.
