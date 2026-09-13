---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-60-finite-horizon-phase-aware-tails"
canonical_tex: "zeta_mvp0/papers/RH-60-finite-horizon-phase-aware-tails/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-60-finite-horizon-phase-aware-tails/main.pdf"
source_sha256: "87a20cb0c32e029f1fed9ae0241807c00e9cd6d94a04c382a1446a1dc39c5b41"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Finite-Horizon Phase-Aware Stein Tails for Directional Hardy Fusion Completing the Schur Packet Route

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-60-finite-horizon-phase-aware-tails>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-60-finite-horizon-phase-aware-tails/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-60-finite-horizon-phase-aware-tails/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-60-finite-horizon-phase-aware-tails/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-60-finite-horizon-phase-aware-tails/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-59 built positive Stein supersolutions in a unitary Schur packet basis. Its all-time observation bound still had a large outer-packet cost. This paper completes that metric with an exact finite-horizon phase calculation. If $\widetilde O$ is any positive observability Stein supersolution, we prove the Loewner completion $$O\preceq O_L+(T^*)^L\widetilde O T^L,
   \qquad
   O_L=\sum_{m=0}^{L-1}(T^*)^mY^*YT^m.$$ The finite term retains all cross-packet phases. For packet tails with Stein upper norms $t_{j,L}$, the fused Hardy energy satisfies the phase-aware bound $\mathcal E\le E_L+\sum_jt_{j,L}$, where $E_L$ is the exact fused finite-horizon response energy. We also give packetwise square-sum completions and geometric tail estimates.

  On the five-scale all-column folded-Gaussian audit, the fixed horizon $L=32$ changes the RH-59 smallest-scale uppers from $19.2196$ and $12.1382$ to $1.47497$ and $1.76413$, against exact energies $1.46807$ and $1.76031$. The finite phase terms are $1.468073$ and $1.760309$; the remaining tail sums are only $0.006892$ and $0.003819$. The fitted growth exponents are $0.169$ and $0.200$, close to the exact-energy exponents $0.168$ and $0.199$. A 256-bit Arb model certifies the finite-horizon plus tail formula on a two-scalar-block system only. The production result remains binary64 evidence: no uniform physical-family horizon, Stage A1 theorem, arithmetic trace formula, self-adjoint realization, or Hilbert--Polya conclusion is claimed.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Finite-Horizon Phase-Aware Stein Tails for Directional Hardy Fusion\
  Completing the Schur Packet Route
```

## Markdown 正文

**Keywords:** finite-horizon Gramian; Stein tail; Schur packet; phase coherence; Hardy energy; nonnormal operator; small noise.

**MSC 2020:** 47A10; 47B65; 93B07; 93D05; 65F35.

# Introduction

The active small-noise problem in the quadratic transfer program is a pair of directional Hilbert--Schmidt Hardy energies. RH-50 expressed the remaining intrinsic identification gate in this form [@WangHardy2026]. RH-56 ruled out uniform fixed-step strong-space contraction [@WangHardyBarrier2026]; RH-57 showed that fixed radial Riesz blocks become severely oblique [@WangRieszOverlap2026].

RH-58 moved to a unitary, time-ordered Schur flag and proved dual positive packet Gram identities [@WangSchurGram2026]. That coordinate change removed the oblique projector wall, but a scalar absolute sum over all feed-forward paths grew to $1922.4$ and $380.4$ at the finest stored level. RH-59 replaced that path ledger by flag-adapted block Lyapunov metrics and exact positive dissipation [@WangFlagMetric2026]. The resulting packetwise uppers fell to $19.22$ and $12.14$, but an outer-packet endpoint cost remained.

The key observation of RH-60 is temporal. The metric is being asked to bound the observation in every direction at every time, including the short times where the actual packet phases have not yet mixed. We can retain the first $L$ time steps exactly and use the positive metric only for the tail. This is not a new choice of Schur weights. It is a completion theorem that can be applied to any valid Stein supersolution.

## Contributions and boundary {#contributions-and-boundary .unnumbered}

1.  We prove a finite-horizon Loewner completion from an observability Stein supersolution.

2.  We prove a global phase-aware Minkowski upper that fuses all finite packet cross terms before summing only the tails.

3.  We give packetwise hybrid bounds and a geometric tail corollary.

4.  We audit a fixed horizon $L=32$ on the RH-59 five-scale family and record a horizon sweep through $L=64$.

The finite-dimensional statements are exact. The production Gramians, Schur forms, inherited metrics, and fitted laws are binary64 diagnostics. The fact that $L=32$ works on five stored levels is not a continuum or dyadic theorem.

# Hardy packets and supersolutions {#sec:setup}

Let $A$ be stable, with source $X$ and observation $Y$. The directional Hardy energy and observability Gramian are $$\mathcal E^2=\sum_{m\ge0}\left\lVert YA^mX\right\rVert_{\mathfrak S_2}^2=\operatorname{tr}(X^*OX),
 \qquad O-A^*OA=Y^*Y.
 \label{eq:hardy}$$ Use a unitary Schur form and block partition [@GolubVanLoan2013; @HornJohnson2013] $$A=QTQ^*,\qquad
 T=\begin{pmatrix}
 D_1&T_{12}&\cdots&T_{1J}\\
 0&D_2&\cdots&T_{2J}\\
 \vdots&\ddots&\ddots&\vdots\\
 0&\cdots&0&D_J
 \end{pmatrix}.
 \label{eq:schur}$$ Set $\widehat X=Q^*X$, $\widehat Y=YQ$, and $X_j=E_j\widehat X$. The response of packet $j$ is the Hilbert-space vector $$F_j=(\widehat YT^mX_j)_{m\ge0}\in\ell^2(\mathfrak S_2),
 \qquad F=\sum_{j=1}^JF_j.
 \label{eq:responses}$$ RH-58's packet Gram is $K_{ij}=\langle F_i,F_j\rangle$, so $\mathcal E=\left\lVert F\right\rVert$ and its diagonal entries are the exact packet energies.

For each packet, upper triangularity leaves the first $j$ Schur blocks invariant. On that prefix let $T^{(j)}$ and $Y^{(j)}$ denote the restricted operator and observation. RH-59 supplies a positive matrix $\widetilde O_j$ satisfying $$\widetilde O_j-(T^{(j)})^*\widetilde O_jT^{(j)}
 \succeq (Y^{(j)})^*Y^{(j)}.
 \label{eq:supersolution}$$ For its flag metric, this was $\widetilde O_j=\kappa_jP_j$; RH-60 does not need that special form.

# Finite-horizon phase completion {#sec:completion}

Define the finite-horizon observability Gramian $$O_{j,L}=\sum_{m=0}^{L-1}
 ((T^{(j)})^*)^m(Y^{(j)})^*Y^{(j)}(T^{(j)})^m,
 \qquad O_{j,0}=0.
 \label{eq:finite-observation}$$

[\[thm:completion\]]{#thm:completion label="thm:completion"} Assume $T^{(j)}$ is stable and [\[eq:supersolution\]](#eq:supersolution){reference-type="eqref" reference="eq:supersolution"} holds. Then, for every integer $L\ge0$, $$\boxed{
 O^{(j)}\preceq O_{j,L}
 +((T^{(j)})^*)^L\widetilde O_j(T^{(j)})^L.}
 \label{eq:loewner-completion}$$ Consequently, with $X_j$ restricted to the prefix, $$e_j^2\le h_{j,L}^2+t_{j,L}^2,
 \label{eq:packet-completion}$$ where $$\begin{aligned}
 h_{j,L}^2&=\operatorname{tr}(X_j^*O_{j,L}X_j),\\
 t_{j,L}^2&=\operatorname{tr}\!\left(X_j^*((T^{(j)})^*)^L
             \widetilde O_j(T^{(j)})^LX_j\right).
 \label{eq:tail-terms}\end{aligned}$$

The exact Gramian splits at time $L$: $$O^{(j)}=O_{j,L}+((T^{(j)})^*)^LO^{(j)}(T^{(j)})^L.$$ Since the tail factor is a positive congruence and $O^{(j)}\preceq\widetilde O_j$ by iteration of the positive Stein residual, the second term is bounded by the corresponding congruence of $\widetilde O_j$. Testing on $X_j$ gives [\[eq:packet-completion\]](#eq:packet-completion){reference-type="eqref" reference="eq:packet-completion"}--[\[eq:tail-terms\]](#eq:tail-terms){reference-type="eqref" reference="eq:tail-terms"}.

The finite term is phase-aware because it is not split into packet norms. For $0\le m<L$, define $$F_{j,L}=(\widehat YT^mX_j)_{0\le m<L},
 \qquad K^{(L)}_{ij}=\langle F_{i,L},F_{j,L}\rangle.
 \label{eq:finite-gram}$$ Then $K^{(L)}\succeq0$ and $$E_L:=\left\lVert\sum_jF_{j,L}\right\rVert=\sqrt{\mathbf1^*K^{(L)}\mathbf1}
 \label{eq:finite-fused}$$ contains every finite-time cross phase.

[\[thm:global\]]{#thm:global label="thm:global"} Let $t_{j,L}$ be any valid tail upper in [\[eq:tail-terms\]](#eq:tail-terms){reference-type="eqref" reference="eq:tail-terms"}. Then $$\boxed{\mathcal E\le E_L+\sum_{j=1}^Jt_{j,L}.}
 \label{eq:global-completion}$$ Also, $$\mathcal E\le\sum_{j=1}^J\sqrt{h_{j,L}^2+t_{j,L}^2}.
 \label{eq:packet-global}$$

Decompose $F=F_{<L}+F_{\ge L}$, where $F_{<L}=\sum_jF_{j,L}$. By Minkowski and the triangle inequality, $$\left\lVert F\right\rVert\le\left\lVert F_{<L}\right\rVert+\sum_j\left\lVert F_{j,\ge L}\right\rVert
 \le E_L+\sum_jt_{j,L}.$$ The packetwise statement follows by applying [\[thm:completion\]](#thm:completion){reference-type="ref" reference="thm:completion"} to each packet and then summing its norm bounds.

At $L=0$, [\[eq:global-completion\]](#eq:global-completion){reference-type="eqref" reference="eq:global-completion"} is exactly the RH-59 metric absolute upper. As $L\to\infty$ for a fixed finite stable matrix, the tail terms vanish and $E_L\to\mathcal E$. The practical question is whether a small, uniform horizon suffices before any continuum limit is taken.

[\[prop:tail-decay\]]{#prop:tail-decay label="prop:tail-decay"} Suppose $\widetilde O_j=\kappa_jP_j$, put $S_j=P_j^{1/2}T^{(j)}P_j^{-1/2}$, and let $W_j=P_j^{1/2}X_j$. Then $$t_{j,L}=\sqrt{\kappa_j}\left\lVert S_j^LW_j\right\rVert_{\mathfrak S_2}
 \le\sqrt{\kappa_j}\left\lVert S_j\right\rVert_2^L\left\lVert W_j\right\rVert_{\mathfrak S_2}.
 \label{eq:tail-decay}$$

Substitute $\widetilde O_j=\kappa_jP_j$ into [\[eq:tail-terms\]](#eq:tail-terms){reference-type="eqref" reference="eq:tail-terms"} and conjugate by $P_j^{1/2}$. The final inequality is submultiplicativity.

The first expression in [\[eq:tail-decay\]](#eq:tail-decay){reference-type="eqref" reference="eq:tail-decay"}, rather than its geometric last expression, is used in the production audit. It retains source alignment inside the normalized flag.

# Five-scale audit {#sec:audit}

We inherit the RH-59 all-column folded-Gaussian family, with $$(\sigma,N)=(0.16,32),(0.08,64),(0.04,128),(0.02,256),(0.01,512),
 \qquad N\sigma=5.12,$$ Hardy radius $r=0.85$, and cuts $0.15,0.35,0.55$. The RH-59 local metrics, packet scales, and $\kappa_j$ values are read from its archived binary64 result. No reoptimization is performed in RH-60.

For each $L\in\{0,1,2,4,8,16,32,64\}$ we compute the exact finite Gram $K^{(L)}$ and $E_L$, then apply the RH-59 packet tail certificate to obtain $t_{j,L}$. The selected comparison uses the fixed $L=32$ for all five levels. All finite Grams pass positive-semidefinite binary64 checks; no interval enclosure is claimed.

::: {#tab:main}
  ---------- -------- -------- --------- --------- -------- --------

    $\sigma$     left    right      left     right     left    right
        0.16   0.9040   1.0026    1.1719    1.5183   0.9040   1.0026
        0.08   1.1626   1.2653    2.1206    2.4307   1.1626   1.2653
        0.04   1.3338   1.4845    2.8953    4.0798   1.3338   1.4846
        0.02   1.4096   1.6340    3.9855    7.5263   1.4101   1.6349
        0.01   1.4681   1.7603   19.2196   12.1382   1.4750   1.7641
  ---------- -------- -------- --------- --------- -------- --------

  : Exact energies, inherited RH-59 all-time metric uppers, and the phase-aware finite-horizon completion. The last column pair is a valid finite-matrix upper in exact arithmetic; displayed values are binary64.
:::

At the finest scale, the $L=32$ finite phase terms are $1.4680734$ and $1.7603090$, while the tail sums are only $0.0068921$ and $0.0038190$. The selected upper therefore differs from the exact energy by $0.47\%$ and $0.22\%$. The fitted growth exponents of the selected upper are $0.169$ and $0.200$, compared with $0.168$ and $0.199$ for the exact energies and $0.898$ and $0.763$ for RH-59's all-time metric upper.

::: {#tab:horizon}
  ----- ------------------- ---------- ------------------- ----------

    $L$   phase-aware upper   tail sum   phase-aware upper   tail sum
      0             19.2196    19.2196             12.1382    12.1382
      4              7.3786     6.0386              6.0341     4.6707
      8              3.4136     1.9614              3.0186     1.3570
     16              1.7612     0.2934              1.9256     0.1666
     32              1.4750     0.0069              1.7641     0.0038
     64              1.4681     0.0000              1.7603     0.0000
  ----- ------------------- ---------- ------------------- ----------

  : Horizon sweep at $\sigma=0.01$. At $L=0$ the completion is the RH-59 metric bound. The $L=64$ tail values are below $5\times10^{-6}$ in both directions.
:::

![Phase-aware completion audit. (a) Fixed $L=32$ uppers track the exact energies. (b) The horizon sweep collapses the RH-59 endpoint wall. (c) At $L=32$ the finite phase term dominates the residual tail. (d) The completion ratio stays near one while the all-time metric ratio grows.](<../../../../../zeta_mvp0/papers/RH-60-finite-horizon-phase-aware-tails/figures/finite_horizon_phase_tail.pdf>){#fig:audit width="\\textwidth"}

## Outward-rounded model audit

A 256-bit Arb calculation [@Johansson2017] uses the real two-block model $$T=\begin{pmatrix}0.2&0.3\\0&0.7\end{pmatrix},\quad
 Y=(0.8,0.6),\quad X=(0,0.4)^T,
 \quad(s_1,s_2)=(0.25,1),$$ and horizon $L=8$. The supersolution multiplier is inflated by $1+10^{-6}$ so that its interval residual is strictly positive. Arb certifies the finite energy square, the exact full energy square, the tail upper, and a positive completion gap. The model certificate does not interval-validate a production Schur form.

# Program consequence {#sec:consequence}

RH-59 all-time metric

:   Remains a valid finite-dimensional tail engine, but is too pessimistic when applied from time zero.

Finite phase Gram

:   Restores the observed cross-packet cancellation over a short time window.

Fixed $L=32$ audit

:   Nearly closes the stored five-scale numerical budget and matches the exact finite-range growth exponent.

Uniform theorem

:   Still open. The horizon, Schur packets, and inherited metric weights have not been controlled as a physical continuum family.

Stage A1

:   Not closed. RH-60 supplies a sharper decomposition of the target, not a dyadically uniform bound.

Stage A4

:   Still conditional on Stage A1; no later factor or cutoff interface changes.

The next analytic target is now sharply defined: prove a physical-family finite-horizon Gram estimate and a matching tail estimate with $L$ bounded or growing only polylogarithmically in the noise. If that target fails, the failure should be localized to either short-time packet phase control or the long-time outer tail, rather than hidden in an all-time norm.

# No arithmetic or Hilbert--Polya conclusion

Nothing here constructs a self-adjoint operator, a $T\log T$ counting law, a von Mangoldt or prime-power trace formula, or a zeta-zero identity. No Riemann-hypothesis conclusion is drawn. The independent twin-prime branch is not used.

# Reproducibility

The archive contains the finite-horizon algebra, tests, horizon sweep, five-scale results, Arb model certificate, figures, dependency hashes, and publication artifacts. Principal commands are

    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/pytest -q -p no:cacheprovider
    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/run_phase_tail_pilot.py
    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/run_arb_phase_tail_audit.py
    MPLBACKEND=Agg PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/make_figures.py
    latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex

The finite-horizon Loewner completion, phase-aware Gram fusion, packet completion, and geometric tail estimate are analytic finite-dimensional results. Production asymptotics remain numerical. Stage A1, unconditional intrinsic identification, and every arithmetic or Hilbert--Polya conclusion remain outside the claims.
