---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-64-weighted-terminal-residuals"
canonical_tex: "zeta_mvp0/papers/RH-64-weighted-terminal-residuals/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-64-weighted-terminal-residuals/main.pdf"
source_sha256: "e83306eeb0a11e7031b254a37b85bd783b745a0b9b65351a40a9882e12f4ac05"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Observability-Weighted Terminal Residuals for Nested Krylov Stein Tails Turning Nonnormal Growth into a Metric Contraction

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-64-weighted-terminal-residuals>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-64-weighted-terminal-residuals/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-64-weighted-terminal-residuals/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-64-weighted-terminal-residuals/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-64-weighted-terminal-residuals/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-63 repaired the one-step residual failure by recursively expanding Arnoldi defects, but its terminal remainder was still propagated with the Euclidean operator norm. This paper replaces that final factor by a positive Lyapunov metric. For a stable matrix $A$, let $M$ solve $$M-A^*MA=I.$$ The induced norm has a strict contraction $\|M^{1/2}AM^{-1/2}\|<1$. We prove that the coherent nested residual certificate remains valid when its terminal remainder is propagated in this metric, and that it can be multiplied directly into a Stein tail.

  On the RH-61 slow/fast surrogate, the weighted certificate is essentially unchanged. On the RH-60 two-block model, the one-level gain drops from $66.41$ to $23.84$. On the nonnormal four-step chain, whose Euclidean operator norm is $1.110729$, the Lyapunov contraction is $0.987369$ and the one-level gain drops from $84.05$ to $2.485$. Full finite-dimensional breakdown remains exact. The new obstruction is metric conditioning: the four-step condition number is about $37.7$. No uniform physical-family conditioning theorem, Stage A1 closure, self-adjoint operator, arithmetic trace formula, or Hilbert--Polya conclusion is claimed.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Observability-Weighted Terminal Residuals for Nested Krylov Stein Tails\
  Turning Nonnormal Growth into a Metric Contraction
```

## Markdown 正文

**Keywords:** Lyapunov metric; weighted residual; nested Krylov; Stein tail; nonnormal operator.

**MSC 2020:** 47A10; 47B65; 65F35; 93B07; 93D05.

# Introduction

The directional tail route now has three finite-dimensional layers. RH-61 identified the gap between actual and norm tails. RH-62 projected the source onto an Arnoldi space, and RH-63 recursively projected the residual chain. Both still used an ordinary norm for the terminal residual.

That last choice is structurally poor for nonnormal matrices. A stable matrix can have $\|A\|>1$ even though its orbit decays. A Lyapunov metric records the decay in a positive norm and is standard in discrete-time stability theory [@ZhouDoyleGlover1996]. The question is whether it can be inserted without destroying the coherent nested identity.

## Contributions and boundary {#contributions-and-boundary .unnumbered}

1.  We construct the positive metric $M$ from the discrete Lyapunov equation and prove strict weighted contraction.

2.  We derive the weighted nested terminal-residual certificate.

3.  We audit three finite models and quantify the conditioning cost.

All values are deterministic binary64 finite-matrix calculations, with a 256-bit Arb check only for the displayed two-block metric.

# Weighted residual theorem {#sec:theorem}

Let $A$ be stable and let $M$ be the positive solution of $$M-A^*MA=I.
\label{eq:lyapunov}$$ Define $\left\lVert x\right\rVert_M=\left\lVert M^{1/2}x\right\rVert_2$ and $$q_M=\left\lVert M^{1/2}AM^{-1/2}\right\rVert_2.
\label{eq:qmetric}$$

[\[prop:contraction\]]{#prop:contraction label="prop:contraction"} The metric in [\[eq:lyapunov\]](#eq:lyapunov){reference-type="eqref" reference="eq:lyapunov"} is positive definite and $q_M<1$.

Stability gives the convergent series $M=\sum_{j\ge0}(A^*)^jA^j$, hence positivity. From [\[eq:lyapunov\]](#eq:lyapunov){reference-type="eqref" reference="eq:lyapunov"}, $$M^{-\frac12}A^*MA M^{-\frac12}
 =I-M^{-1}.$$ The largest eigenvalue of the right side is strictly below one.

[\[thm:weighted\]]{#thm:weighted label="thm:weighted"} Suppose a coherent nested Arnoldi expansion has the form $$A^Lz=\mathcal A_L+\sum_i c_i A^{u_i}g_i.$$ Then $$\left\lVert A^Lz\right\rVert_M
 \le \left\lVert\mathcal A_L\right\rVert_M+
 \sum_i |c_i|q_M^{u_i}\left\lVert g_i\right\rVert_M.
\label{eq:weighted-upper}$$ For a Stein tail $t_L=\sqrt{\kappa}\left\lVert A^Lz\right\rVert_M$, multiplication by $\sqrt{\kappa}$ preserves the upper.

The Lyapunov similarity gives $\left\lVert A^ug\right\rVert_M\le q_M^u\left\lVert g\right\rVert_M$. Insert this estimate into the coherent decomposition and apply the triangle inequality only after all projected terms have been combined.

[\[cor:conditioning\]]{#cor:conditioning label="cor:conditioning"} If $\lambda_{\max}(M)\le K$ and $\lambda_{\min}(M)\ge k>0$, then $$\left\lVert x\right\rVert_M\le\sqrt K\left\lVert x\right\rVert,
 \qquad
 \left\lVert x\right\rVert\le k^{-1/2}\left\lVert x\right\rVert_M.$$ Thus a weighted residual certificate transfers to Euclidean or Hilbert--Schmidt quantities with a factor controlled by $\sqrt{K/k}$.

These are the extremal eigenvalue inequalities for a positive matrix.

The theorem does not assert that the Lyapunov metric is canonical across a noise-dependent physical family. Its finite-dimensional existence is easy; uniform condition numbers and compatibility with Schur packets are the actual analytic questions.

# Finite-model audit {#sec:audit}

The pilot repeats the RH-63 models and compares the Euclidean one-level certificate with the Lyapunov-weighted one at $L=32$.

::: {#tab:results}
  model                   $\left\lVert A\right\rVert$      $q_M$   cond$(M)$   Euclidean gain   weighted gain
  --------------------- ----------------------------- ---------- ----------- ---------------- ---------------
  slow/fast surrogate                        0.993861   0.993861       78.43           1.0000          1.0000
  two-block model                            0.765889   0.739799        2.13          66.4095         23.8441
  four-step chain                            1.110729   0.987369       37.66          84.0539          2.4848

  : Weighted terminal residual results.
:::

The weighted contraction removes the qualitative obstruction $\left\lVert A\right\rVert>1$ in the chain. It does not by itself close the tail: the gain remains above one, and the metric condition number is nontrivial.

![Lyapunov weighting. The left panel compares Euclidean and weighted propagation contractions. The right panel compares one-level residual gains with the unweighted RH-63 certificate.](<../../../../../zeta_mvp0/papers/RH-64-weighted-terminal-residuals/figures/weighted_terminal_residuals.pdf>){#fig:audit width="98%"}

A 256-bit Arb computation certifies the two-block Lyapunov entries, the identity $M-A^*MA=I$, positivity, and strict weighted contraction. It does not validate the production folded-Gaussian family.

# Route consequence {#sec:consequence}

The route now has a positive terminal mechanism: $$\text{nested Krylov projection}
\longrightarrow
\text{Lyapunov-weighted residual}
\longrightarrow
\text{Stein tail}.
\label{eq:route}$$ The next gate is not existence of a metric but a family-level ledger:

1.  bound the metric condition number on the physical packet prefixes;

2.  preserve block cross-column Gram structure;

3.  compare the weighted metric with the inherited phase-aware observation metric without double counting conditioning.

If the condition number grows faster than the directional savings, this route becomes a finite-dimensional repair only. If it remains polylogarithmic, RH-64 supplies the missing terminal estimate needed for a physical-family transfer.

# No arithmetic or Hilbert--Polya conclusion

This paper constructs no self-adjoint operator, no $T\log T$ counting law, no prime-power trace formula, and no completed-zeta identity. It makes no Hilbert--Polya or Riemann-hypothesis claim.

# Reproducibility

The directory contains the weighted algebra, tests, model pilot, Arb audit, figures, hashes, and publication artifacts. The main commands are:

    pytest -q -p no:cacheprovider
    python experiments/run_weighted_residual_pilot.py
    python experiments/run_arb_weighted_audit.py
    MPLBACKEND=Agg python experiments/make_figures.py
    latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex

The Lyapunov identities and weighted finite-dimensional certificate are analytic. The model rows are binary64 evidence. Stage A1, Stage A4, uniform metric conditioning, a self-adjoint Hilbert--Polya operator, a prime-power trace formula, and a zeta-zero identity remain open.
