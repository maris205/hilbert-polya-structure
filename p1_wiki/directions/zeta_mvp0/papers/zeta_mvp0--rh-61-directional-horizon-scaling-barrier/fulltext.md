---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-61-directional-horizon-scaling-barrier"
canonical_tex: "zeta_mvp0/papers/RH-61-directional-horizon-scaling-barrier/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-61-directional-horizon-scaling-barrier/main.pdf"
source_sha256: "dc369cb1d5283d87acea361bdc428b2c5bc3374336385dd7381838929a8c9243"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Directional Horizon Scaling for Phase-Aware Stein Tails A Geometric Envelope Barrier and the Need for Residual Certificates

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-61-directional-horizon-scaling-barrier>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-61-directional-horizon-scaling-barrier/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-61-directional-horizon-scaling-barrier/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-61-directional-horizon-scaling-barrier/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-61-directional-horizon-scaling-barrier/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-60 retained the first finite time window of a Schur-packet Hardy calculation exactly and used a positive Stein supersolution only for the remaining tail. Its five-scale result was numerically close to the exact directional energy, but it left open whether the required horizon is uniform in the physical small-noise family. This paper isolates that question.

  We prove two elementary but decisive facts. First, a packetwise normalized Stein tail has the geometric envelope $$t_{j,L}\le t_{j,0}q_j^L,
   \qquad q_j=\|S_j\|<1.$$ Second, a reducing slow mode with contraction $q$ and nonzero tail amplitude forces $$L\ge \frac{\log(a/\varepsilon)}{-\log q}$$ before a tail tolerance $\varepsilon$ can be certified. If $1-q_\sigma\asymp\sigma^\beta$, this is a $\sigma^{-\beta}\log(1/\sigma)$ horizon law, not a polylogarithmic one. The lower bound concerns the norm-based tail certificate; it does not rule out cancellation in the exact finite phase Gram.

  We then reanalyze the archived RH-59/RH-60 five-scale family. At $\sigma=0.01$, the observed $L=32$ phase-aware completion is within $0.47\%$ (left) and $0.22\%$ (right) of the exact energy, while the rigorous packetwise geometric envelope would require horizons $850$ and $228$ for a $5\%$ tail target. The actual directional tail at $L=32$ is only $0.006892$ and $0.003819$, whereas the corresponding norm envelopes are $13.15$ and $5.62$. Thus phase fusion remains a viable route, but a uniform theorem needs a directional residual or Krylov tail estimate. No continuum uniformity, Stage A1 closure, self-adjoint operator, arithmetic trace formula, or Hilbert--Polya conclusion is claimed.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Directional Horizon Scaling for Phase-Aware Stein Tails\
  A Geometric Envelope Barrier and the Need for Residual Certificates
```

## Markdown 正文

**Keywords:** Stein tail; horizon scaling; Schur packet; directional decay; Hardy energy; slow mode; small noise.

**MSC 2020:** 47A10; 47B65; 93B07; 93D05; 65F35.

# Introduction

The active analytic gate in the quadratic prime-dynamics program is a directional Hilbert--Schmidt Hardy estimate. RH-50 reduced the intrinsic identification problem to such energies, while RH-56 ruled out a uniform fixed-step strong-space contraction route [@WangHardy2026; @WangHardyBarrier2026]. RH-58 then moved to unitary Schur packets and exact cross-Gramians, and RH-59 constructed positive flag-adapted Stein metrics [@WangSchurGram2026; @WangFlagMetric2026].

RH-60 made the finite-time cancellation explicit. For a horizon $L$, its finite packet Gram keeps all cross phases, while the positive metric is used only after time $L$. On the stored five-scale family, $L=32$ nearly recovers the exact energy. That observation has a subtle limitation: the usual geometric estimate for the remaining metric tail sees the largest norm contraction of every packet, not the direction actually reached by the physical source after the transient.

This paper is a route audit for that distinction. It does not add another black-box matrix norm. Instead, it proves the exact scalar implication of the norm tail, proves a slow-mode lower bound for that certificate, and compares both quantities with the finite phase-aware tail already archived in RH-60.

## Contributions and boundary {#contributions-and-boundary .unnumbered}

1.  We formulate the packetwise geometric tail envelope and the exact integer horizon required by it.

2.  We prove a reducing slow-mode lower bound and its $\sigma^{-\beta}\log(1/\sigma)$ consequence.

3.  We give a reproducible five-scale reanalysis of the RH-59/RH-60 archives, including geometric and observed phase horizons.

4.  We identify the next theorem target: a directional tail profile that is stronger than the largest normalized operator norm.

The algebraic statements are finite-dimensional and unconditional under their displayed hypotheses. The contraction-gap powers, horizon powers, and all production values are archived binary64 diagnostics or fits. They are not asymptotic statements about a continuum physical family.

# Packet tails and horizon envelopes {#sec:setup}

Let $T$ be a stable matrix, $X$ a matrix-valued source, and $Y$ an observation. The directional Hardy energy is $$\mathcal E(T,X,Y)^2=\sum_{m\ge0}\left\lVert YT^mX\right\rVert_{\mathfrak S_2}^2.
 \label{eq:energy}$$ Suppose that a unitary Schur decomposition has produced packet sources $X=\sum_{j=1}^JX_j$. RH-60 gives, for every $L\ge0$, $$\mathcal E\le E_L+\sum_{j=1}^J t_{j,L},
 \label{eq:phase-completion}$$ where $E_L$ is the exact fused finite-horizon response energy and $t_{j,L}$ is a positive Stein upper for the tail of packet $j$.

For clarity, write the normalized packet tail in the form $$t_{j,L}=\sqrt{\kappa_j}\left\lVert S_j^L z_j\right\rVert_{\mathfrak S_2},
 \qquad
 S_j=P_j^{1/2}T_jP_j^{-1/2},
 \qquad z_j=P_j^{1/2}X_j,
 \label{eq:normalized-tail}$$ where $P_j$ is the positive flag metric and $\kappa_j$ is the observation multiplier. The formula also covers a general positive Stein supersolution after factoring its positive matrix.

[\[prop:geometric\]]{#prop:geometric label="prop:geometric"} Assume $q_j=\left\lVert S_j\right\rVert<1$. Then, for every integer $L\ge0$, $$t_{j,L}\le t_{j,0}q_j^L,
 \qquad
 \sum_jt_{j,L}\le \sum_jt_{j,0}q_j^L.
 \label{eq:geometric-envelope}$$ Consequently the smallest horizon certified by this envelope for a tail budget $\varepsilon>0$ is $$L_{\rm geo}(\varepsilon)=
 \min\left\{L\in\mathbb N_0:
 \sum_jt_{j,0}q_j^L\le\varepsilon\right\}.
 \label{eq:geo-horizon}$$

Submultiplicativity gives $\left\lVert S_j^Lz_j\right\rVert_{\mathfrak S_2}\le q_j^L\left\lVert z_j\right\rVert_{\mathfrak S_2}$. Multiplication by $\sqrt{\kappa_j}$ and summation give [\[eq:geometric-envelope\]](#eq:geometric-envelope){reference-type="eqref" reference="eq:geometric-envelope"}. The definition of $L_{\rm geo}$ is then exactly the first integer at which the displayed sufficient inequality holds.

The proposition is deliberately packetwise. Replacing all $q_j$ by $q=\max_jq_j$ gives the simpler but often much looser bound $$\sum_jt_{j,L}\le q^L\sum_jt_{j,0}.
 \label{eq:common-envelope}$$ The RH-61 audit retains the separate $q_j$ values whenever they are available.

# A slow-mode horizon obstruction {#sec:slow-mode}

The geometric envelope is an upper bound, not a lower bound for the exact transfer energy. A lower bound does hold when the slowly contracting direction is a genuine reducing component of the normalized tail dynamics.

[\[thm:slow-mode\]]{#thm:slow-mode label="thm:slow-mode"} Let $S_\sigma$ be a normalized packet operator and let $P_\sigma$ be an orthogonal projection such that $$S_\sigma P_\sigma=P_\sigma S_\sigma=q_\sigma P_\sigma,
 \qquad 0<q_\sigma<1.
 \label{eq:reducing-mode}$$ Assume the positive tail metric obeys $\widetilde O_\sigma\succeq\mu_\sigma I$ and put $a_\sigma=\sqrt{\mu_\sigma}\left\lVert P_\sigma z_\sigma\right\rVert_{\mathfrak S_2}$. Then $$\sqrt{\operatorname{tr}\!\left((S_\sigma^Lz_\sigma)^*
 \widetilde O_\sigma S_\sigma^Lz_\sigma\right)}
 \ge a_\sigma q_\sigma^L.
 \label{eq:slow-lower}$$ In particular, any certificate that makes this tail at most $\varepsilon_\sigma$ must have $$L\ge
 \left\lceil\frac{\log(a_\sigma/\varepsilon_\sigma)}
 {-\,\log q_\sigma}\right\rceil
 \quad\text{when }a_\sigma>\varepsilon_\sigma.
 \label{eq:slow-horizon}$$

The reducing relation gives the orthogonal decomposition $S_\sigma^Lz_\sigma=q_\sigma^LP_\sigma z_\sigma+
S_\sigma^L(I-P_\sigma)z_\sigma$. Hence its Hilbert--Schmidt norm is at least $q_\sigma^L\left\lVert P_\sigma z_\sigma\right\rVert_{\mathfrak S_2}$. Since $\widetilde O_\sigma\succeq\mu_\sigma I$, the weighted norm is at least $\sqrt{\mu_\sigma}$ times the unweighted norm. Solving $a_\sigma q_\sigma^L\le\varepsilon_\sigma$ gives [\[eq:slow-horizon\]](#eq:slow-horizon){reference-type="eqref" reference="eq:slow-horizon"}.

[\[cor:power-gap\]]{#cor:power-gap label="cor:power-gap"} Suppose for all sufficiently small $\sigma$ that $$a_\sigma\ge c_a\sigma^a,
 \qquad 1-q_\sigma\le C_q\sigma^\beta,
 \qquad \varepsilon_\sigma\le C_\varepsilon\sigma^p,
 \label{eq:power-assumptions}$$ with $p>a$, $\beta>0$, and $q_\sigma\ge1/2$. Then there are constants $c>0$ and $\sigma_0>0$ such that every slow-mode tail certificate requires $$L\ge c\,\sigma^{-\beta}\log(1/\sigma),
 \qquad 0<\sigma<\sigma_0.
 \label{eq:power-horizon}$$

The numerator in [\[eq:slow-horizon\]](#eq:slow-horizon){reference-type="eqref" reference="eq:slow-horizon"} is at least $(p-a)\log(1/\sigma)+O(1)$. For $q\ge1/2$, $-\log q\le 2(1-q)\le2C_q\sigma^\beta$. Substitution gives the claim.

The theorem does not say that the exact fused finite Gram has a slow-mode lower bound. Short-time packet phases can cancel, and a physical source can leave the slow norm direction rapidly. The theorem only identifies what a uniform proof based on the displayed positive tail metric must control. That distinction is the central route boundary of this paper.

# Archived physical-family audit {#sec:audit}

We reanalyze, without recomputing or reoptimizing, the five rows archived by RH-59 and RH-60. The family has $N\sigma=5.12$, Hardy radius $r=0.85$, and radial Schur cuts $(0.15,0.35,0.55)$. The RH-59 packet records supply $t_{j,0}$ and $q_j$; RH-60 supplies the exact finite phase Grams and the stored tail sums. The reanalysis is therefore deterministic algebra on the archived inputs.

For each side and each tolerance $\eta$, we record the first integer $L_{\rm geo}$ for which the geometric tail is at most $\eta\mathcal E$, and the first stored horizon for which the phase-aware completion is at most $(1+\eta)\mathcal E$. The latter is censored by the stored grid $\{0,1,2,4,8,16,32,64\}$.

::: {#tab:horizon}
    $\sigma$   $N$   $1-q_L$   $1-q_R$   $L_{\rm geo,L}$   $L_{\rm geo,R}$   $(L_{\rm obs,L},L_{\rm obs,R})$
  ---------- ----- --------- --------- ----------------- ----------------- ---------------------------------
        0.16    32     0.372     0.353                 5                 6                           $(4,4)$
        0.08    64     0.183     0.180                14                16                           $(8,8)$
        0.04   128    0.0637    0.0673                42                46                         $(16,16)$
        0.02   256    0.0225    0.0333               149               118                         $(16,16)$
        0.01   512   0.00614    0.0198               850               228                         $(32,32)$

  : Contraction gaps and 5% horizons. The geometric column is a rigorous consequence of the stored packet metrics; the observed column is the first horizon in the RH-60 grid.
:::

Log--log fits over these five rows give contraction-gap powers $1.486$ and $1.075$ for the left and right channels. The corresponding relaxation times $(-\log q)^{-1}$ have fitted growth exponents $1.562$ and $1.144$. The geometric 5% horizons have fitted growth exponents $1.823$ and $1.338$. These are diagnostics, not asymptotic claims; they show why a fixed $L=32$ cannot be promoted simply by citing the five-scale table.

At the endpoint $\sigma=0.01$, the contrast is sharper:

::: {#tab:endpoint}
  channel     exact $\mathcal E$   phase tail sum   geometric envelope   phase-aware upper / exact
  --------- -------------------- ---------------- -------------------- ---------------------------
  left                  1.468074         0.006892               13.149                    1.004695
  right                 1.760310         0.003819                5.617                    1.002169

  : Endpoint tail comparison at $L=32$.
:::

The geometric envelope is valid but uninformative at this horizon. The finite phase Gram has already moved the physical source away from the worst-case norm direction, a fact not represented by $q_j$ alone.

![RH-61 audit. The top row shows the stored contraction gaps and the separation between the guaranteed geometric and observed phase horizons. At the endpoint (bottom left), the directional tail falls many orders of magnitude faster than the norm envelope. The bottom right shows the recovery of the exact fused energy by the finite phase window.](<../../../../../zeta_mvp0/papers/RH-61-directional-horizon-scaling-barrier/figures/directional_horizon_scaling.pdf>){#fig:audit width="98%"}

# What is proved and what remains open {#sec:boundary}

The exact theorem-level content of RH-61 is summarized as follows.

1.  For every finite matrix and every packetwise positive Stein metric, the geometric envelope [\[eq:geometric-envelope\]](#eq:geometric-envelope){reference-type="eqref" reference="eq:geometric-envelope"} is valid.

2.  Under a reducing slow-mode hypothesis, the horizon lower bound [\[eq:slow-horizon\]](#eq:slow-horizon){reference-type="eqref" reference="eq:slow-horizon"} is valid. The power-gap corollary makes the obstruction quantitative.

3.  On the archived five-scale family, the phase-aware finite completion is numerically close to the exact energy at $L=32$, while the norm-only envelope is much larger.

The following stronger statement is not proved: $$\sup_{\sigma,n} \mathcal E_{\rm phase}(L(\sigma))
 =O((\log(1/\sigma))^b)
 \quad\text{for a polylogarithmic }L(\sigma).
 \label{eq:unproved-target}$$ Nor do we prove that the observed slow direction is a reducing mode of the physical continuum operator. The contraction-gap fits cannot establish that assertion.

The next viable theorem target is therefore a directional residual estimate. One useful form would be a decomposition $$S_j^Lz_j=R_{j,L}z_j,
 \qquad
 \left\lVert R_{j,L}z_j\right\rVert_{\mathfrak S_2}
 \le C_j(\sigma)\exp(-c_j(\sigma)L)\left\lVert z_j\right\rVert_{\mathfrak S_2},
 \label{eq:directional-target}$$ where $c_j(\sigma)$ is controlled on the actual Krylov range rather than by $-\log\left\lVert S_j\right\rVert$. A finite-rank residual, a block Arnoldi certificate, or an observability-weighted Gramian could supply such an estimate. Any one of these would explain the observed gap between the bottom-left curves in [1](#fig:audit){reference-type="ref" reference="fig:audit"} and could turn RH-60's finite window into a physical-family theorem.

# No arithmetic or Hilbert--Polya conclusion

This paper concerns only a finite-dimensional tail-completion mechanism in the nonselfadjoint transfer route. It constructs no self-adjoint operator, no $T\log T$ counting law, no von Mangoldt or prime-power trace formula, and no completed-zeta spectral identity. It therefore makes no Hilbert--Polya or Riemann-hypothesis claim. The independent twin-prime branch is not used.

# Reproducibility

The directory contains the scalar algebra, tests, the archived-input audit, the 256-bit Arb equality-case check, figures, hashes, and this manuscript. The main commands are:

    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/pytest -q -p no:cacheprovider
    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/run_horizon_scaling_audit.py
    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/run_arb_horizon_audit.py
    MPLBACKEND=Agg PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/make_figures.py
    latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex

The archived production rows remain binary64. The Arb calculation covers only the displayed scalar equality-case model. Stage A1 and Stage A4, directional tail uniformity, a self-adjoint Hilbert--Polya operator, a prime-power trace formula, and a zeta-zero identity remain outside the claims.
