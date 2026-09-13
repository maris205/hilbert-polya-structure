---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-107-source-seeded-quotient-support-law"
canonical_tex: "zeta_mvp0/papers/RH-107-source-seeded-quotient-support-law/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-107-source-seeded-quotient-support-law/main.pdf"
source_sha256: "d0f1bd887be5a9c6d68697e05884557afb0190db1fb02c8ea6c3fd8be946beb9"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Source-Seeded Weak-Mode Support Laws Coarse-Boundary Quotients and a Finite-Extrapolation Barrier

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-107-source-seeded-quotient-support-law>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-107-source-seeded-quotient-support-law/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-107-source-seeded-quotient-support-law/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-107-source-seeded-quotient-support-law/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-107-source-seeded-quotient-support-law/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-106 identified the uniform quotient price as $c^2/g$, where $c$ is an omitted cross energy and $g$ is a retained-to-omitted spectral gap. The next question is whether this price must be controlled at every small-noise level. For the source-seeded adaptive rule with maximum enrichment width four, we show that the answer can instead be reduced to a support question.

  Let $s_1\ge s_2\ge s_3\ge s_4$ be the four projected-cross singular values and let $\tau$ be the relative cutoff. The exact selector identity is $$w_\tau<4\quad\Longleftrightarrow\quad
   \frac{s_4}{s_1}<\tau.$$ Consequently, if the fourth-cross ratio stays above the cutoff beyond a finite level $k_*$, the quotient support is empty there and the accumulated quotient price reduces to a finite coarse-layer sum. We prove the resulting support-to-price reduction and combine it with the stopped endpoint theorem: if the finite coarse price fits the endpoint allowance, no later quotient price can accumulate; if it does not, the stopped fallback remains safe.

  The five source-seeded scales exhibit a sharp coarse boundary. At cutoffs $10^{-8},10^{-6},10^{-4}$, the weak-mode events are respectively $$(4,1,0,0,0),\qquad(7,2,2,0,0),\qquad(8,8,6,0,0)$$ across $\sigma=(0.16,0.08,0.04,0.02,0.01)$. Thus even the $10^{-4}$ cutoff has no quotient event at the last two scales. The minimum fine-scale support margin is $7.3649$ times the cutoff. All 360 selector comparisons agree with the recorded adaptive widths, all 38 local gap certificates are green, and stopped endpoint ratios remain below $1.006033$.

  This is a positive sparse-supply result, not an all-level asymptotic theorem. We prove a finite-extrapolation barrier: separated and persistent-support cross-ratio sequences can agree on every finite audit and diverge afterward. Therefore the observed coarse boundary must ultimately be supplied by an analytic support-separation theorem. No Stage A, Hilbert--Polya, zero identification, or Riemann Hypothesis result is claimed.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Source-Seeded Weak-Mode Support Laws\
  Coarse-Boundary Quotients and a Finite-Extrapolation Barrier
```

## Markdown 正文

**Keywords:** source-seeded packet; weak-mode support; adaptive Ritz width; quotient price; sparse supply; finite extrapolation.

**MSC 2020:** 47A75; 15A18; 65F15; 65G20; 37C30.

# Introduction

The source-seeded refresh construction tracks a finite packet from the source coordinates rather than repeatedly seeding late ambient directions [@WangSourceSeeded2026]. RH-96 used that packet to test adaptive weak-mode quotients. Its local theorem was favorable: an omitted block with coupling $C$ and retained-to-omitted gap $g$ costs at most $\left\lVert C\right\rVert_{\mathrm F}^2/g$ [@WangWeakQuotient2026]. Its global experiment was more subtle. A relative cutoff of $10^{-8}$ was safe, while more aggressive cutoffs failed after recursive accumulation even though every local certificate remained green.

RH-102 resolved endpoint safety by pricing the actual nonlinear future and stopping before the absolute debit exhausts the endpoint slack [@WangStoppedClock2026]. RH-106 then wrote an abstract no-stop condition in terms of candidate count, propagation factor, local price, and slack. It left open whether the candidate count itself grows through the fine scales.

This paper isolates a different route to uniformity. The adaptive rule has a hard maximum width. If the fourth projected-cross mode is not weak, no quotient is proposed at all. Hence a lower bound on the fourth-cross ratio, not a lower bound on the retained-to-omitted Ritz gap, can eliminate the fine part of the quotient problem.

The contributions are:

1.  an exact adaptive-support equivalence for the four-direction selector;

2.  a support-to-price reduction theorem and its stopped endpoint corollary;

3.  a finite-extrapolation barrier showing why five anchors cannot prove eventual support separation;

4.  a complete audit of the 120-update source-seeded chains at three thresholds.

# Adaptive support identity {#sec:selector}

At one source-seeded update, let the projected-cross singular values be $$s_1\ge s_2\ge s_3\ge s_4\ge0,
 \qquad s_1>0.
 \label{eq:singular}$$ For a relative cutoff $\tau>0$, the maximum-width-four selector used in RH-96 is $$w_\tau=\max\!\left\{2,\min\!\left(4,
 \#\{j\in\{1,2,3,4\}:s_j/s_1\ge\tau\}\right)\right\}.
 \label{eq:width}$$

The weak-mode support at cutoff $\tau$ is $$\mathcal W_\tau=\left\{t:\frac{s_4(t)}{s_1(t)}<\tau\right\}.$$ The support margin at a nonweak update is $$m_\tau(t)=\frac{s_4(t)/s_1(t)}{\tau}.$$

[\[thm:equivalence\]]{#thm:equivalence label="thm:equivalence"} Under [\[eq:singular\]](#eq:singular){reference-type="eqref" reference="eq:singular"} and [\[eq:width\]](#eq:width){reference-type="eqref" reference="eq:width"}, $$w_\tau<4
 \quad\Longleftrightarrow\quad
 t\in\mathcal W_\tau
 \quad\Longleftrightarrow\quad
 \frac{s_4(t)}{s_1(t)}<\tau.
 \label{eq:equivalence}$$ In particular, if $s_4(t)/s_1(t)\ge\tau$ on a collection of updates, all those updates use the full width four and generate no omitted-mode quotient.

Since the singular values are ordered, the number of indices satisfying $s_j/s_1\ge\tau$ is four exactly when the fourth ratio is at least $\tau$. The outer maximum and minimum in [\[eq:width\]](#eq:width){reference-type="eqref" reference="eq:width"} do not change the equivalence between width four and failure of that condition.

The theorem is elementary but important for the route. It converts an adaptive spectral statement into a binary support statement before any gap certificate is invoked.

# Support-to-price reduction {#sec:reduction}

Index the source-seeded noise levels by $k$ and updates within one level by $t$. At a weak update, let $\ell_{k,t}=c_{k,t}^2/g_{k,t}$ be the local gap-weighted price and let $K_{k,t}$ be a certified propagated-debit factor, so that the endpoint debit satisfies $$d_{k,t}\le K_{k,t}\ell_{k,t}.
 \label{eq:debit}$$ Define the total quotient price $$D_k(\tau)=\sum_{t\in\mathcal W_{k,\tau}}K_{k,t}\ell_{k,t}.
 \label{eq:total-price}$$

[\[thm:reduction\]]{#thm:reduction label="thm:reduction"} Suppose there is a level $k_*$ such that $$\frac{s_4(k,t)}{s_1(k,t)}\ge\tau
 \quad\text{for every }k\ge k_*\text{ and every update }t.
 \label{eq:fine-separation}$$ Then $$D_k(\tau)=0\qquad(k\ge k_*).
 \label{eq:fine-zero}$$ If the finitely many coarse levels $k<k_*$ have at most $N_*$ weak events, $K_{k,t}\le K_*$, and $\ell_{k,t}\le\ell_*$, then $$\sup_{k\ge0}D_k(\tau)\le N_*K_*\ell_*.
 \label{eq:coarse-price}$$

Theorem [\[thm:equivalence\]](#thm:equivalence){reference-type="ref" reference="thm:equivalence"} makes the support set empty for every $k\ge k_*$. This proves [\[eq:fine-zero\]](#eq:fine-zero){reference-type="eqref" reference="eq:fine-zero"}. On the remaining finite set of levels, the sum in [\[eq:total-price\]](#eq:total-price){reference-type="eqref" reference="eq:total-price"} contains at most $N_*$ terms, each bounded by $K_*\ell_*$. Taking the supremum proves [\[eq:coarse-price\]](#eq:coarse-price){reference-type="eqref" reference="eq:coarse-price"}.

[\[cor:stopped\]]{#cor:stopped label="cor:stopped"} Let $S_k$ be the rigorous endpoint slack and $A_k=\eta S_k$ the stopped allowance, with $0\le\eta<1$. Under the hypotheses of [\[thm:reduction\]](#thm:reduction){reference-type="ref" reference="thm:reduction"}, if $$N_*K_*\ell_*\le\inf_{k<k_*}A_k,$$ every coarse quotient and hence every candidate in the family is accepted without a stop, and every endpoint gate is preserved. If the inequality fails, accepting only while the cumulative propagated debits fit $A_k$ and switching permanently to full width still preserves every endpoint gate.

The first statement follows by summing the finite coarse prices and applying the endpoint-budget theorem of RH-102. The second is its stopped branch; the fine levels contribute zero quotient price by [\[eq:fine-zero\]](#eq:fine-zero){reference-type="eqref" reference="eq:fine-zero"}.

This reduction is different from proving a fine-scale lower bound on the retained-to-omitted Ritz gap. If no fourth mode is omitted, that gap never enters a quotient price. The physical target has therefore split into a cross-support separation problem and a finite coarse price problem.

# Finite-extrapolation barrier {#sec:barrier}

The support reduction is conditional. The next proposition states exactly why the five finite anchors cannot, by themselves, establish [\[eq:fine-separation\]](#eq:fine-separation){reference-type="eqref" reference="eq:fine-separation"} for all future levels.

[\[prop:barrier\]]{#prop:barrier label="prop:barrier"} Fix a cutoff $\tau>0$ and any finite observed sequence $(\theta_0,\ldots,\theta_{K})$ with $\theta_k>0$. There are two infinite extensions agreeing with all observed values: $$\begin{aligned}
 \theta_k^{\mathrm{sep}}&=2\tau,\qquad k>K,\\
 \theta_k^{\mathrm{pers}}&=\tfrac12\tau,\qquad k>K.
 \end{aligned}$$ The first has empty weak support beyond $K$, while the second has a weak event at every later level. Thus no finite cross-ratio audit alone proves eventual support separation.

Define the two extensions as displayed. Since $2\tau\ge\tau$ and $\tau/2<\tau$, the adaptive support equivalence gives the two claims.

The barrier is not a negative result about the source-seeded family. It identifies the exact missing analytic input: a structural lower bound for the fourth projected-cross ratio on the fine source-seeded chain.

# Five-scale source-seeded audit {#sec:audit}

We read all 120 updates in both channels at the five RH-94 source-seeded scales, for each of the three RH-96 cutoffs. The audit recomputes $s_4/s_1$, applies the selector identity, and independently reads the local coupling/gap price and RH-102 propagated debit. There are 360 selector comparisons in total.

::: {#tab:audit}
  $\tau$         event counts   fine level   min fine margin        total $\ell$   max stopped ratio
  ----------- --------------- ------------ ----------------- ------------------- -------------------
  $10^{-8}$     $(4,1,0,0,0)$      $k\ge2$             8.221   $4.297\,10^{-13}$            1.001173
  $10^{-6}$     $(7,2,2,0,0)$      $k\ge3$           736.493    $1.452\,10^{-9}$            1.001173
  $10^{-4}$     $(8,8,6,0,0)$      $k\ge3$             7.365    $7.500\,10^{-8}$            1.006033

  : Weak-mode support and coarse price by relative cutoff. Event counts are listed in scale order $0.16,0.08,0.04,0.02,0.01$.
:::

Every selector comparison agrees with the recorded adaptive width. The fine support is empty for every threshold. The absolute fourth-ratio lower bound on the fine levels is $8.221\times10^{-8}$ for $10^{-8}$, and $7.365\times10^{-4}$ for the two coarser cutoffs. Thus the weakest observed fine support margin is still $7.365$.

The local prices are concentrated in the coarse layer. The maximum total local price over the three thresholds is $7.5000\times10^{-8}$. Using the largest finite replay multiplier, the coarse support upper is $6.702\times10^{-8}$. The actual stopped chains are much tighter: all 38 local gap certificates are green, 35 candidates are accepted, three are rejected, and the worst stopped endpoint/reference ratio is $1.006033$.

![Left: weak-mode quotient events occur only on the coarse scales. Right: the minimum fourth-cross ratio over each scale's updates clears the corresponding cutoff on the fine scales.](<../../../../../zeta_mvp0/papers/RH-107-source-seeded-quotient-support-law/figures/source_seeded_quotient_support.pdf>){#fig:audit width="98%"}

The finite data therefore support a useful route refinement: at the current cutoffs, fine-scale quotient accumulation is absent, not merely small.

# Route consequence and claim boundary {#sec:route}

RH-107 supplies a new conditional decomposition of the uniform quotient gate:

1.  prove a fine source-seeded support-separation bound for $s_4/s_1$;

2.  price only the finite coarse weak-mode layer;

3.  use the stopped clock as a safety fallback if the coarse price does not fit.

This is more precise than asking for a uniform gap lower bound at every level. It also explains why the finite RH-96/RH-102 chains look easier at the fine scales: the quotient branch is not being entered there.

The analytic support-separation statement remains open because of [\[prop:barrier\]](#prop:barrier){reference-type="ref" reference="prop:barrier"}. Until it is proved, the result is a finite sparse-supply certificate and a route map, not an all-level theorem. The remaining absolute-scale leaves from RH-104 and RH-105 are unchanged.

No statement here constructs a Hilbert--Polya operator, proves a $T\log T$ law or prime-power trace formula, identifies zeta zeros, or proves the Riemann Hypothesis.

# Reproducibility

The directory contains the support selector helpers, full and smoke audits, figures, tests, and a hash-checked archive. Run:

    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \\
      experiments/build_support_audit.py
    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \\
      experiments/build_support_audit.py --smoke
    MPLBACKEND=Agg PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \\
      experiments/make_figures.py
    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/pytest -q -p no:cacheprovider

The archive scripts record the exact RH-96/RH-102 inputs and verify all publication hashes.
