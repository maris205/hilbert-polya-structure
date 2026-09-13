---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-105-observation-residual-cancellation-law"
canonical_tex: "zeta_mvp0/papers/RH-105-observation-residual-cancellation-law/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-105-observation-residual-cancellation-law/main.pdf"
source_sha256: "a797fbde1de60f5f8a1b86508ba32d6828b2d2869905fe5b81c507e043b79396"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Observation--Residual Cancellation in Postblock Hardy Transfer A Signed-Power Theorem and a Sharp Rate-Matching Boundary

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-105-observation-residual-cancellation-law>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-105-observation-residual-cancellation-law/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-105-observation-residual-cancellation-law/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-105-observation-residual-cancellation-law/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-105-observation-residual-cancellation-law/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The postblock effective-rank route contains a product that should not be estimated by separately truncating both factors. If $B$ is a postblock state, $B_r$ a rank-$r$ approximation, $q=\left\lVert A^M\right\rVert_2<1$, and $$O_M=\sum_{j=0}^{M-1}(A^j)^*Y^*YA^j,
   \qquad
   \Omega=\sqrt{\frac{\left\lVert O_M\right\rVert_2}{1-q^2}},$$ then the full-future perturbation is bounded by $$|T(B)-T(B_r)|\le \Omega\,\tau_r(B).$$ We prove the associated signed-power law. If $\Omega=O(\sigma^{-o}\operatorname{polylog})$ and $\tau_r(B)=O(\sigma^{\rho}\operatorname{polylog})$, the product has growth power $\max(0,o-\rho)$. Thus residual decay of order at least the observability growth is exactly the zero-power threshold. A matched-scale factorization gives the equivalent criterion $$\Omega\tau_r(B)=
   (\sigma^\theta\Omega)(\sigma^{-\theta}\tau_r(B)),$$ with the natural mesh split $\theta=1/2$ when observation growth is of square-root order. We also prove sharpness by a scalar seminorm family.

  The five archived RH-77/RH-82 channels satisfy the algebraic cancellation with a large margin. The square-root-normalized observation factor is at most $2.12555$, the normalized residual is at most $3.07755\times10^{-9}$, and every recomposed future perturbation is below $5.044\times10^{-9}$. The recomposition agrees with the archived interval result to relative error below $5\times10^{-16}$. This is a positive theorem about composition and a strong finite audit, not an all-level residual-decay proof. The uniform observation law and uniform clock-residual law remain separate gates. No Stage A, Hilbert--Polya, zero identification, or Riemann Hypothesis result is claimed.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Observation--Residual Cancellation in Postblock Hardy Transfer\
  A Signed-Power Theorem and a Sharp Rate-Matching Boundary
```

## Markdown 正文

**Keywords:** observation--residual cancellation; effective rank; Hardy seminorm; signed sigma power; postblock compression.

**MSC 2020:** 47A10; 47B35; 65F30; 93B28; 65G20.

# Introduction

RH-77 established the basic mechanism by which a low-rank postblock state can be transferred through the complete future: the full observability Gramian turns a Frobenius state residual into a Hardy-energy residual [@WangEffectiveRank2026]. RH-82 supplied a half-logarithmic rank clock and found extremely small residuals at the five production anchors [@WangClock2026]. RH-103 subsequently exposed a bookkeeping hazard: the observability factor may grow with the mesh while the state residual decays, so their powers must be composed with signs intact [@WangPowerLedger2026].

The distinction is not cosmetic. If one first replaces every factor by a nonnegative growth power, a decaying residual is recorded as power zero and its cancellation with observation growth disappears. Conversely, a small finite residual can look persuasive while failing to supply the decay rate needed at all levels. The purpose of this paper is to isolate exactly what is proved, what is sharp, and what remains open.

The contributions are:

1.  an observation--residual cancellation theorem in signed sigma powers;

2.  a matched-scale criterion and a finite propagator fallback bound;

3.  a scalar sharpness example showing that the rate threshold cannot be weakened to mere residual convergence;

4.  an independent recomposition of the five RH-77/RH-82 channels.

The result closes an algebraic ambiguity in the route. It does not close the physical all-level hypotheses that feed the algebra.

# Full-future observability and rank residuals {#sec:setup}

Let $A\in\mathbb C^{d\times d}$, $Y\in\mathbb C^{p\times d}$, and let $B,B_r\in\mathbb C^{d\times m}$. For a stable $A$, define the future Hardy seminorm $$T(Z)^2=\sum_{\ell\ge0}\left\lVert YA^\ell Z\right\rVert_{\mathrm F}^2.
 \label{eq:T}$$ At a block horizon $M$, set $$O_M=\sum_{j=0}^{M-1}(A^j)^*Y^*YA^j,
 \qquad q=\left\lVert A^M\right\rVert_2.
 \label{eq:OM}$$ Regrouping time indices in blocks gives the positive Gramian identity $$O=\sum_{b\ge0}(A^{*M})^bO_M(A^M)^b,
 \qquad
 \left\lVert O\right\rVert_2\le\frac{\left\lVert O_M\right\rVert_2}{1-q^2},
 \label{eq:O}$$ whenever $q<1$. Define the certified future observability factor $$\Omega_M=\sqrt{\frac{\left\lVert O_M\right\rVert_2}{1-q^2}}.
 \label{eq:Omega}$$

[\[prop:transfer\]]{#prop:transfer label="prop:transfer"} If $q<1$, then for every $B,B_r$, $$\left|T(B)-T(B_r)\right|
 \le \Omega_M\left\lVert B-B_r\right\rVert_{\mathrm F}.
 \label{eq:transfer}$$ In particular, if $\tau_r(B)$ is the optimal rank-$r$ Frobenius residual, $$\tau_r(B)=\left(\sum_{j>r}s_j(B)^2\right)^{1/2},
 \label{eq:tau}$$ then a truncated SVD satisfies $$\left|T(B)-T(B_r)\right|\le\Omega_M\tau_r(B).
 \label{eq:rank-transfer}$$

Equation [\[eq:O\]](#eq:O){reference-type="eqref" reference="eq:O"} implies $T(Z)=\left\lVert O^{1/2}Z\right\rVert_{\mathrm F}$ and $\left\lVert O\right\rVert_2^{1/2}\le\Omega_M$. The reverse triangle inequality for this seminorm gives [\[eq:transfer\]](#eq:transfer){reference-type="eqref" reference="eq:transfer"}. The Eckart--Young theorem supplies [\[eq:tau\]](#eq:tau){reference-type="eqref" reference="eq:tau"} and the rank-$r$ approximation.

This proposition is valid for nonnormal, non-diagonalizable matrices. The remaining question is how the two factors in [\[eq:rank-transfer\]](#eq:rank-transfer){reference-type="eqref" reference="eq:rank-transfer"} scale together.

# Signed powers and exact cancellation {#sec:powers}

For a nonnegative family $f_\sigma$, a signed power $a$ means $$f_\sigma=O\!\left(\sigma^{-a}\operatorname{polylog}(1/\sigma)\right).$$ Thus $a>0$ records growth and $a<0$ records decay. A final norm growth exponent is truncated below at zero only after all products have been formed.

[\[thm:cancellation\]]{#thm:cancellation label="thm:cancellation"} Suppose, along a small-noise family, $$\begin{aligned}
 \Omega_\sigma&=O\!\left(\sigma^{-o}L_\Omega(\sigma)\right),
 \label{eq:omega-power}\\
 \tau_r(B_\sigma)&=O\!\left(\sigma^{\rho}L_\tau(\sigma)\right),
 \label{eq:tau-power}
 \end{aligned}$$ where $o,\rho\in\mathbb R$ and the $L$ factors are polylogarithmic. Then $$\left|T(B_\sigma)-T(B_{\sigma,r})\right|
 =O\!\left(\sigma^{\rho-o}
 L_\Omega(\sigma)L_\tau(\sigma)\right),
 \label{eq:product-power}$$ and its nonnegative growth power is $$\boxed{\beta=\max\{0,o-\rho\}.}
 \label{eq:beta}$$ In particular, $\rho\ge o$ is sufficient for zero power, and $\rho>o$ gives a decaying weighted residual up to logarithms.

Multiply the two estimates in [\[prop:transfer\]](#prop:transfer){reference-type="ref" reference="prop:transfer"}. Powers multiply by addition in the signed convention: $\sigma^{-o}\sigma^\rho
 =\sigma^{\rho-o}$. If $\rho-o\ge0$, the product is bounded by a polylogarithm; otherwise it grows as $\sigma^{-(o-\rho)}$.

[\[cor:matched\]]{#cor:matched label="cor:matched"} For any fixed $\theta\in\mathbb R$, $$\Omega_\sigma\tau_r(B_\sigma)
 =\bigl(\sigma^\theta\Omega_\sigma\bigr)
  \bigl(\sigma^{-\theta}\tau_r(B_\sigma)\bigr).
 \label{eq:matched}$$ If both factors on the right are polylogarithmic, the weighted residual has zero sigma power. The natural square-root split is $\theta=1/2$ when $\Omega_\sigma$ has the mesh scale $\sigma^{-1/2}$.

This is the exact identity obtained by inserting cancelling powers of $\sigma$ into the product. The polylogarithmic conclusion follows from [\[thm:cancellation\]](#thm:cancellation){reference-type="ref" reference="thm:cancellation"}.

[\[prop:fallback\]]{#prop:fallback label="prop:fallback"} Define $$K_M(A)^2=\sum_{j=0}^{M-1}\left\lVert A^j\right\rVert_2^2.$$ Then $$\Omega_M
 \le \frac{\left\lVert Y\right\rVert_2 K_M(A)}{\sqrt{1-q^2}}.
 \label{eq:fallback}$$ Consequently, if $K_M$ is polylogarithmic, $q$ is uniformly below one, $\left\lVert Y\right\rVert_2=O(\sigma^{-1/2}\operatorname{polylog})$, and $\tau_r(B)=O(\sigma^{1/2}\operatorname{polylog})$, then the weighted residual is polylogarithmic.

By submultiplicativity, $$\left\lVert O_M\right\rVert_2
 \le\sum_{j<M}\left\lVert A^j\right\rVert_2^2\left\lVert Y\right\rVert_2^2
 =K_M(A)^2\left\lVert Y\right\rVert_2^2.$$ Insert this into [\[eq:Omega\]](#eq:Omega){reference-type="eqref" reference="eq:Omega"}; the final claim is [\[cor:matched\]](#cor:matched){reference-type="ref" reference="cor:matched"} with $\theta=1/2$.

If the finite propagator is nonexpansive, $K_M\le\sqrt M$. Thus a log-square horizon contributes only a polylogarithm. The proposition is a fallback criterion, not an assertion that the production matrices are one-step contractions.

# Sharpness of the rate threshold {#sec:sharp}

The inequality in [\[thm:cancellation\]](#thm:cancellation){reference-type="ref" reference="thm:cancellation"} is rate-sharp, even in one dimension.

[\[prop:sharp\]]{#prop:sharp label="prop:sharp"} Let $o,\rho\ge0$ and consider the scalar seminorm $$T_\sigma(z)=\sigma^{-o}|z|,
 \qquad B_\sigma=\sigma^\rho,
 \qquad B_{\sigma,r}=0.$$ Then $\tau_r(B_\sigma)=\sigma^\rho$ and $$\left|T_\sigma(B_\sigma)-T_\sigma(B_{\sigma,r})\right|
 =\sigma^{\rho-o}.
 \label{eq:sharp}$$ If $\rho<o$, the weighted residual has exactly growth power $o-\rho$. Hence no theorem based only on $\tau_r(B_\sigma)\to0$ can guarantee zero power.

All assertions follow by direct substitution. The scalar example saturates the product estimate, so the exponent in [\[thm:cancellation\]](#thm:cancellation){reference-type="ref" reference="thm:cancellation"} cannot be improved without additional structure.

The barrier is a logical rate boundary, not a counterexample to the folded-Gaussian production family. It says that an all-level proof must establish a quantitative residual rate matched to the observation scale.

# Five-anchor recomposition {#sec:audit}

The audit independently reads RH-77's outward-rounded full observability norms and RH-82's outward-rounded clock residuals. It takes the square root of the former, multiplies by the latter, and compares the result with the archived full-future perturbation. No archived product is used as an input to the recomposition.

::: {#tab:audit}
    $\sigma$   rank   $\max\Omega$        $\max\tau_r$   $\max\sqrt\sigma\Omega$   $\max\tau_r/\sqrt\sigma$   $\max\Omega\tau_r$
  ---------- ------ -------------- ------------------- ------------------------- -------------------------- --------------------
        0.16      4          4.097    $1.231\,10^{-9}$                     1.639           $3.078\,10^{-9}$     $5.043\,10^{-9}$
        0.08      5          6.076   $3.473\,10^{-13}$                     1.719          $1.228\,10^{-12}$    $2.110\,10^{-12}$
        0.04      6          9.299   $7.893\,10^{-14}$                     1.860          $3.946\,10^{-13}$    $7.255\,10^{-13}$
        0.02      6         14.099   $4.471\,10^{-13}$                     1.994          $3.161\,10^{-12}$    $6.262\,10^{-12}$
        0.01      7         21.255   $8.275\,10^{-14}$                     2.126          $8.276\,10^{-13}$    $1.752\,10^{-12}$

  : Largest left/right values at each dyadic anchor.
:::

The raw observation factor grows by a factor of about five from the first to the last anchor. The square-root-normalized factor remains below $2.126$, while the normalized residual is below $3.078\times10^{-9}$. The largest recomposed product is $5.0430244\times10^{-9}$, and the largest relative discrepancy from the archived product is $4.93\times10^{-16}$.

![The matched square-root factors and their product at the five anchors. The observation factor grows, but the residual factor is much smaller; the signed product remains below the displayed audit gate.](<../../../../../zeta_mvp0/papers/RH-105-observation-residual-cancellation-law/figures/observation_residual_cancellation.pdf>){#fig:audit width="98%"}

The numerical result is stronger than the minimal rate-matching threshold at these anchors. It does not, however, prove that the residual retains a comparable exponent for every dyadic level. The clock construction itself is logarithmic; the missing physical theorem is the uniform supply of the tiny residual after the clock rank.

# Route consequence {#sec:route}

RH-105 settles the algebraic question in the absolute-scale ledger: observation growth and residual decay must be carried as a signed pair until their product is formed. In the notation of RH-103, the signed residual power is $r_s=-\rho_s$, so the term previously written as $o_s+r_s$ is $o_s-\rho_s$. It has the exact threshold $$\text{zero weighted power}\quad\Longleftrightarrow\quad
 \rho_s\ge o_s
 \quad\Longleftrightarrow\quad r_s\le-o_s.$$ The finite propagator fallback shows one way to obtain the square-root split, but only under an additional bound on the preblock powers of $A$.

The remaining dependency graph is therefore:

-   RH-105 proves the signed cancellation theorem and its sharp rate boundary;

-   RH-77/RH-82 supply strong finite evidence for the matched factors;

-   the all-level observation growth law is still open;

-   the all-level clock-residual decay law is still open;

-   their combination can be used only after both physical laws are proved uniformly.

This is a positive route refinement, not a Stage-A closure. No claim here constructs a Hilbert--Polya operator, proves a $T\log T$ law or prime-power trace formula, identifies zeta zeros, or proves the Riemann Hypothesis.

# Reproducibility

The directory contains the cancellation helpers, a full and smoke audit, the figure, tests, and a hash-checked publication archive. Run:

    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \\
      experiments/build_cancellation_audit.py
    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \\
      experiments/build_cancellation_audit.py --smoke
    MPLBACKEND=Agg PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \\
      experiments/make_figures.py
    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/pytest -q -p no:cacheprovider

The archive scripts record the exact RH-77/RH-82 inputs and verify all publication hashes.
