---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-57-mixed-haar-channel-overlap-budget"
canonical_tex: "zeta_mvp0/papers/RH-57-mixed-haar-channel-overlap-budget/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-57-mixed-haar-channel-overlap-budget/main.pdf"
source_sha256: "d919a3de481ec63f6a1be74f2f9923877cb8c2a0b57a6c6b120a313dd06adc30"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Mixed Haar-Channel Riesz Overlap Budgets Cross-Stein Identities and a Radial-Block Obstruction

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-57-mixed-haar-channel-overlap-budget>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-57-mixed-haar-channel-overlap-budget/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-57-mixed-haar-channel-overlap-budget/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-57-mixed-haar-channel-overlap-budget/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-57-mixed-haar-channel-overlap-budget/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The remaining analytic premise in the intrinsic small-noise identification program is a uniform budget for two directional Hilbert--Schmidt Hardy energies. The preceding layer showed that a global strong-space mixing rate spends too much of the available exponent budget, and proposed retaining the mixed source--resonance--observation overlap of the adjacent Haar channels.

  This paper makes that proposal exact at finite dimension. For a stable operator and an arbitrary finite Riesz partition, we prove a cross-Stein identity: the complete Hardy energy is the quadratic form of a positive semidefinite Gram matrix whose entries are block cross-Gramians. No diagonalizability, individual eigenvector normalization, or normality is required. A normalized block coherence constant then gives the sufficient bound $$\mathcal E(r)^2\le \kappa\sum_j K_{jj},
   \qquad
   \kappa=\lambda_{\max}\!\left[
   \frac{K_{jk}}{\sqrt{K_{jj}K_{kk}}}\right].$$ For simple modes this reduces to the exact Hardy Cauchy kernel $\operatorname{tr}(Z_jZ_k^*)/(1-\mu_j\overline{\mu_k}/r^2)$.

  We then perform a deterministic all-column binary64 audit on the folded Gaussian matrices inherited from RH-51. Fixed radial Riesz blocks preserve the exact total energies, but their individual block energies and projector norms become rapidly oblique as the noise decreases. At the smallest stored scale the largest radial projector norm is about $2.7\times10^3$, while the aggregate left and right energies are only $1.4681$ and $1.7603$. Thus the cross-Stein theorem identifies the correct signed aggregate object, but a fixed radial blockwise absolute budget is not a closure of Stage A1. The five-scale fits are diagnostics, not asymptotic claims. A 256-bit Arb audit certifies the scalar two-block identities only. Stage A1, intrinsic identification, any Hilbert--Polya operator, and any arithmetic conclusion remain open.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Mixed Haar-Channel Riesz Overlap Budgets\
  Cross-Stein Identities and a Radial-Block Obstruction
```

## Markdown 正文

**Keywords:** Hardy energy; Riesz projection; cross-Gramian; Stein equation; Haar channel; nonnormal operator; small noise.

**MSC 2020:** 47A10; 47B65; 37D25; 37M25; 65R20.

# Introduction

The fixed-noise intrinsic determinant and its dyadic continuum limit are rigorous within the transfer-operator model. The active question is whether the finite matrix's own Perron/parity-deflated bulk can be identified uniformly as the Gaussian width tends to zero. RH-48 reduced this question to directional reduced resolvents, RH-49 moved the two relevant actions into the Hilbert--Schmidt class, and RH-50 converted the contour problem into two time-domain Hardy energies [@WangIntrinsic2026; @WangDirectional2026; @WangHardy2026]. RH-51 through RH-56 supplied growing-horizon Stein tails, peripheral residue transfer, cutoff stability, and a quantitative obstruction to the global strong-space route [@WangStructuredStein2026; @WangFactorTransfer2026; @WangHardyTail2026; @WangFactorAware2026; @WangRieszCutoff2026; @WangHardyBarrier2026].

Let $T=G_{2n,\sigma}$ and use the adjacent orthogonal Haar decomposition $V_{2n}=V_n\oplus W_n$. With $U$ the coarse embedding and $B,C$ the two off-diagonal Haar couplings, RH-50 studies $$\begin{aligned}
 \mathcal E_B(r)^2
 &=\sum_{m\ge0}r^{-2m}
 \frac{\left\lVert U^*N_f^mQ_fUB\right\rVert_{\mathfrak S_2}^2}{\left\lVert B\right\rVert_{\mathfrak S_2}^2},
 \label{eq:left-energy}\\
 \mathcal E_C(r)^2
 &=\sum_{m\ge0}r^{-2m}
 \frac{\left\lVert CN_c^mQ_c\right\rVert_{\mathfrak S_2}^2}{\left\lVert C\right\rVert_{\mathfrak S_2}^2}.
 \label{eq:right-energy}\end{aligned}$$ Here $N_f,N_c$ are the intrinsic Perron/parity-deflated fine and coarse operators and $Q_f,Q_c$ remove the two peripheral ranges. RH-54 requires a combined power no larger than $1/4$: $$\mathcal E_B(r)=O(\sigma^{-\alpha_B}),\qquad
 \mathcal E_C(r)=O(\sigma^{-\alpha_C}),\qquad
 \alpha_B+\alpha_C\le\frac14.
 \label{eq:budget}$$

RH-56 showed that a global strong-space estimate can fail this budget even when finite-dimensional Hardy traces look modest. Its surviving suggestion was to retain the overlap between the special Haar source, the resonance space, and the observation. A sum of individual modal bounds is still unsatisfactory near clustered nonnormal modes. The present paper therefore asks for the invariant-block object before any individual eigenvector is chosen.

## Contributions and boundary {#contributions-and-boundary .unnumbered}

1.  We prove the cross-Stein Riesz-block identity and the associated normalized coherence bound for arbitrary finite stable operators.

2.  We give the simple-mode Hardy Cauchy kernel as a corollary and show how growing-horizon block certificates provide diagonal block-energy upper bounds.

3.  We implement a grouped left/right invariant-subspace audit which checks projector, commutator, partition, Stein, and Gram residuals without random trace probes.

4.  We locate a concrete route boundary: fixed radial blocks become highly oblique, so their absolute or square-summed budgets do not close the small-noise problem even though the signed aggregate Gram quadratic form remains modest on the stored levels.

No theorem in this paper establishes a uniform small-noise Hardy bound for the physical family. In particular, the numerical projector construction is not an interval contour proof, and the fitted five-level exponents are not asymptotic exponents.

# Directional Hardy triples {#sec:triples}

For either side of [\[eq:left-energy\]](#eq:left-energy){reference-type="eqref" reference="eq:left-energy"}--[\[eq:right-energy\]](#eq:right-energy){reference-type="eqref" reference="eq:right-energy"}, write the normalized triple in the common form $$\mathcal E(r)^2=\sum_{m\ge0}r^{-2m}\left\lVert YN^mX\right\rVert_{\mathfrak S_2}^2,
 \qquad \operatorname{spr}(N)<r,
 \label{eq:common-energy}$$ where $(X,Y)=(Q_fUB/\left\lVert B\right\rVert_{\mathfrak S_2},U^*)$ for the left triple and $(X,Y)=(C^*/\left\lVert C\right\rVert_{\mathfrak S_2},Q_c^*)$ after taking the adjoint for the right triple. Put $A=r^{-1}N$. Then $$\mathcal E(r)^2=\sum_{m\ge0}\left\lVert YA^mX\right\rVert_{\mathfrak S_2}^2.
 \label{eq:scaled-energy}$$ The ordinary controllability Gramian is $$G=\sum_{m\ge0}A^mXX^*(A^*)^m,
 \qquad G-AGA^*=XX^*.
 \label{eq:gramian}$$ RH-51 used this positive Stein equation for deterministic all-column calculations. The issue in the present layer is how to retain the decomposition of $G$ induced by the bulk resonance space without replacing it by a global operator norm.

# Cross-Stein Riesz identity {#sec:identity}

Let $P_1,\ldots,P_J$ be a Riesz partition of $A$: the projections are pairwise disjoint, commute with $A$, and sum to the identity on the state space. They may be oblique. Define $$X_j=P_jX,\qquad F_j=(YA^mX_j)_{m\ge0}\in\ell^2(\mathbb N_0;\mathfrak S_2).
 \label{eq:block-response}$$ The block cross-Gramians are $$G_{jk}=\sum_{m\ge0}A^mP_jXX^*P_k^*(A^*)^m.
 \label{eq:cross-gramian}$$

[\[thm:cross-stein\]]{#thm:cross-stein label="thm:cross-stein"} Let $A$ be a finite matrix with $\operatorname{spr}(A)<1$, let $X$ be a finite Hilbert--Schmidt source, and let $Y$ be a bounded observation. For any Riesz partition $\{P_j\}_{j=1}^J$ the series in [\[eq:cross-gramian\]](#eq:cross-gramian){reference-type="eqref" reference="eq:cross-gramian"} converge and satisfy $$G_{jk}-AG_{jk}A^*=P_jXX^*P_k^*.
 \label{eq:cross-stein}$$ If $$K_{jk}:=\operatorname{tr}(YG_{jk}Y^*)
       =\sum_{m\ge0}\operatorname{tr}\!\left(
          YA^mP_jXX^*P_k^*(A^*)^mY^*
        \right),
 \label{eq:block-gram}$$ then $K=(K_{jk})$ is positive semidefinite and $$\boxed{\mathcal E(r)^2=\sum_{j,k=1}^J K_{jk}.}
 \label{eq:exact-quadratic}$$ If $\operatorname{tr}K>0$, define the signed fusion ratio $$\eta(K):=\frac{\mathbf 1^*K\mathbf 1}{\operatorname{tr}K}.
 \label{eq:fusion-ratio}$$ In particular, if $e_j=K_{jj}^{1/2}$, $D=\operatorname{diag}(e_j)$ on the nonzero diagonal indices, and $C=D^{-1}KD^{-1}$, then $$\boxed{
 \mathcal E(r)^2=\eta(K)\sum_{j=1}^J e_j^2
 \le \lambda_{\max}(C)\sum_{j=1}^J e_j^2.}
 \label{eq:coherence-bound}$$ The coarser Gershgorin version is $$\lambda_{\max}(C)\le\max_j\sum_k|C_{jk}|.
 \label{eq:gershgorin}$$ No diagonalizability or normality assumption is used.

Since $\operatorname{spr}(A)<1$, the series in [\[eq:cross-gramian\]](#eq:cross-gramian){reference-type="eqref" reference="eq:cross-gramian"} converge in finite dimension. Separating the first term and shifting the index gives [\[eq:cross-stein\]](#eq:cross-stein){reference-type="eqref" reference="eq:cross-stein"}. The commutation relation $AP_j=P_jA$ gives $G_{jk}=P_jGP_k^*$, where $G$ is [\[eq:gramian\]](#eq:gramian){reference-type="eqref" reference="eq:gramian"}. For each $m$ set $R_{j,m}=YA^mP_jX$. With the trace inner product linear in its first argument, $$K_{jk}=\sum_{m\ge0}\operatorname{tr}(R_{j,m}R_{k,m}^*).$$ Thus $K$ is the Gram matrix of the vectors $F_j$ in $\ell^2(\mathbb N_0;\mathfrak S_2)$, and summing the responses gives [\[eq:exact-quadratic\]](#eq:exact-quadratic){reference-type="eqref" reference="eq:exact-quadratic"}. If $e_j>0$, write $K=DCD$. The vector of all ones gives $$\sum_{j,k}K_{jk}=e^*Ce\le\lambda_{\max}(C)e^*e,$$ Dividing the left side by $\operatorname{tr}K=e^*e$ gives [\[eq:fusion-ratio\]](#eq:fusion-ratio){reference-type="eqref" reference="eq:fusion-ratio"} and $0\le\eta(K)\le\lambda_{\max}(C)$. This proves [\[eq:coherence-bound\]](#eq:coherence-bound){reference-type="eqref" reference="eq:coherence-bound"}; Gershgorin gives [\[eq:gershgorin\]](#eq:gershgorin){reference-type="eqref" reference="eq:gershgorin"}. Zero diagonal blocks have zero response and are removed before forming $D^{-1}$.

[\[cor:cauchy\]]{#cor:cauchy label="cor:cauchy"} Suppose $N$ is diagonalizable with simple eigenvalues $\mu_j$, and write $Z_j=YP_jX$. Then $$\boxed{K_{jk}=\frac{\operatorname{tr}(Z_jZ_k^*)}
 {1-\mu_j\overline{\mu_k}/r^2}.}
 \label{eq:cauchy-kernel}$$ For a rank-one projector $P_j=v_j\otimes w_j$ normalized by $\langle w_j,v_j\rangle=1$, $$\left\lVert Z_j\right\rVert_{\mathfrak S_2}=\left\lVert Yv_j\right\rVert_2\,\left\lVert X^*w_j\right\rVert_2.
 \label{eq:rank-one-overlap}$$

In the scaled variable $A=N/r$, $A^mP_j=(\mu_j/r)^mP_j$. Substitution into [\[eq:block-gram\]](#eq:block-gram){reference-type="eqref" reference="eq:block-gram"} gives the geometric series and [\[eq:cauchy-kernel\]](#eq:cauchy-kernel){reference-type="eqref" reference="eq:cauchy-kernel"}. The rank-one formula follows by factoring $YP_jX$ into a column and a row.

The RH-56 modal triangle bound replaces the Gram quadratic form by $\sum_j e_j$. The new sufficient quantity is $\sqrt{\kappa\sum_j e_j^2}$, where $\kappa=\lambda_{\max}(C)$. This can be smaller when block responses are nearly orthogonal. The exact factor $\eta(K)$ also retains signed cancellation in the particular aggregate response, whereas the worst-direction coherence $\kappa$ generally does not. The worst-direction coherence bound can fail to be useful when a proposed Riesz partition is highly oblique: the individual $e_j$ can be large even though their aggregate quadratic form is small. The exact $\eta$ identity then points to the missing signed estimate rather than supplying one.

# Block tails and the dyadic target {#sec:target}

Let $A_j=AP_j$ and $X_j=P_jX$. For an integer $M_j\ge1$, put $$S_{j,M_j}=\sum_{m=0}^{M_j-1}A_j^mX_jX_j^*(A_j^*)^m,
 \qquad q_j=\left\lVert A_j^{M_j}\right\rVert_2.
 \label{eq:block-prefix}$$

[\[prop:block-tail\]]{#prop:block-tail label="prop:block-tail"} If $q_j<1$, then $$K_{jj}\le\operatorname{tr}(YS_{j,M_j}Y^*)+
 \frac{\left\lVert Y\right\rVert_{\mathfrak S_2}^2\left\lVert A_j^{M_j}S_{j,M_j}(A_j^*)^{M_j}\right\rVert_2}
 {1-q_j^2}.
 \label{eq:block-tail}$$ Consequently, diagonal estimates $K_{jj}\le b_j(\sigma)^2$ and a coherence bound $\kappa(\sigma)\le k(\sigma)$ imply $$\mathcal E(r)\le\sqrt{k(\sigma)\sum_jb_j(\sigma)^2}.
 \label{eq:finite-block-target}$$

After time $M_j$, the state is $A_j^{M_j}$ applied to a prefix state. The tail controllability Gramian is bounded by the geometric Neumann series with ratio $q_j^2$. Taking the observed trace gives [\[eq:block-tail\]](#eq:block-tail){reference-type="eqref" reference="eq:block-tail"}; insert the diagonal bounds into [\[eq:coherence-bound\]](#eq:coherence-bound){reference-type="eqref" reference="eq:coherence-bound"} for the last statement.

The resulting sufficient condition is sharper than the RH-56 absolute modal sum, but it is still a condition rather than a physical-family theorem. A direct signed route may replace $\kappa$ below by a proved upper for the specific Rayleigh ratio $\eta(K)$; that estimate must control the cross terms, not infer cancellation from finite data.

[\[cond:cross-budget\]]{#cond:cross-budget label="cond:cross-budget"} At every required small-noise level, choose invariant blocks for the left and right triples so that $$\kappa_B(\sigma)\sum_jK_{B,jj}(\sigma)=O(\sigma^{-2\alpha_B}),
 \qquad
 \kappa_C(\sigma)\sum_jK_{C,jj}(\sigma)=O(\sigma^{-2\alpha_C}),
 \label{eq:cross-budget}$$ with $\alpha_B+\alpha_C\le1/4$. The constants and block construction must be uniform over the dyadic schedule.

Condition [\[cond:cross-budget\]](#cond:cross-budget){reference-type="ref" reference="cond:cross-budget"}, together with the RH-50 contour Hardy upper and the RH-52--RH-55 peripheral, factor, and cutoff interfaces, closes the Hardy portion of intrinsic identification at the stated exponents. A bounded or polylogarithmic $\kappa$ with square-summed block energies is sufficient; it is not proved here for the physical family.

Apply [\[thm:cross-stein\]](#thm:cross-stein){reference-type="ref" reference="thm:cross-stein"} to the normalized left and right triples. The two square roots in [\[eq:cross-budget\]](#eq:cross-budget){reference-type="eqref" reference="eq:cross-budget"} give the two Hardy powers, whose sum is at most $1/4$. The remaining interfaces are precisely those already established in the cited layers.

# Binary64 grouped-block audit {#sec:numerics}

We use the folded midpoint Gaussian matrices from RH-51 and RH-53. The fine dimensions satisfy $N\sigma=5.12$ at $$(\sigma,N)=(0.16,32),(0.08,64),(0.04,128),(0.02,256),(0.01,512).$$ The Perron and negative parity branches are removed by the biorthogonal rank-two subtraction used in those layers. The left operator is $N_f/0.85$ with source $Q_fUB/\left\lVert B\right\rVert_{\mathfrak S_2}$ and observation $U^*$. The right operator is $N_c^*/0.85$ with source $C^*/\left\lVert C\right\rVert_{\mathfrak S_2}$ and observation $Q_c^*$.

For each triple, the bulk spectrum is grouped by physical modulus using the fixed cuts $0.15,0.35,0.55$. The groups are called central, inner cloud, middle cloud, and edge cloud; empty groups are omitted. A noncentral projector is formed from paired left and right eigenspaces, and the central projector is the complement of their sum. This is a grouped invariant- subspace construction, not a sum of individual eigenvector condition numbers.

The full controllability Gramian is solved densely in binary64 and every source column is included. We form the block Gram matrix from $$K_{jk}=\operatorname{tr}(YP_jGP_k^*Y^*).$$ The audit records Stein, partition, commutator, and Gram residuals.

::: {#tab:main-audit}
  ---------- -------- -------- --------- ---------- --------- ---------- --------- ---------

    $\sigma$     left    right      left      right      left      right      left     right
        0.16   0.9040   1.0026    1.4992     1.8343    1.9188     2.3977      4.21      4.03
        0.08   1.1626   1.2653    2.2621     4.2979    2.9871     5.8984     13.30     13.55
        0.04   1.3338   1.4845    4.3864     8.9683    6.1122    12.7305     51.45     48.42
        0.02   1.4096   1.6340   28.9725   127.4598   40.9396   180.2447    845.82    835.67
        0.01   1.4681   1.7603   57.6743   474.0177   81.6785   672.4059   2705.75   2531.73
  ---------- -------- -------- --------- ---------- --------- ---------- --------- ---------

  : Grouped radial Riesz audit at $r=0.85$. The exact column is the direct all-column Lyapunov energy. The square-sum column is $\sqrt{\sum_jK_{jj}}$, and the coherence column is $\sqrt{\lambda_{\max}(C)\sum_jK_{jj}}$. The last columns show the largest oblique projector norm. All entries are binary64 diagnostics.
:::

The block identity is numerically stable on these levels. The maximum relative reconstruction defect is $1.83\times10^{-12}$ and the maximum partition defect is $6.2\times10^{-14}$. The large upper bounds in [1](#tab:main-audit){reference-type="ref" reference="tab:main-audit"} are therefore not caused by omitted source columns; they are caused by the oblique invariant-block decomposition.

The fitted log--log slopes of the exact left and right energies are $0.168$ and $0.199$ over these five levels. The corresponding slopes for the coherence upper are approximately $1.46$ and $2.12$. These are descriptive finite-range fits only. The exact-energy fit is not an asymptotic theorem, and the rapidly growing block upper is not a proof that the physical Hardy energies diverge.

![Grouped-block audit. (a) The signed aggregate Lyapunov energies remain below the coherence-weighted radial-block upper. (b) Radial Riesz projectors become strongly oblique. (c) The signed fusion ratio decreases as large radial block responses cancel in the aggregate. This is a diagnostic, not a uniform cancellation theorem. (d) Right-channel normalized block Gram at $\sigma=0.01$.](<../../../../../zeta_mvp0/papers/RH-57-mixed-haar-channel-overlap-budget/figures/mixed_haar_channel_overlap.pdf>){#fig:audit width="\\textwidth"}

All production eigenspaces, Lyapunov solutions, and singular norms are binary64 and are not interval enclosures. A separate 256-bit Arb calculation evaluates a two-mode real model with $$\mu_1=0.72,\qquad \mu_2=-0.61,\qquad Z_1=0.37,\qquad Z_2=-0.29,$$ and certifies positivity of its cross-Gram matrix, the geometric-series Cauchy entries, and the coherence and triangle inequalities. It does not enclose a production Riesz projector.

# Route consequence {#sec:consequence}

Global strong-space black box

:   Quantitatively obstructed by RH-56; this paper does not reopen that route.

Individual modal absolute overlaps

:   Too sensitive to clustered nonnormal eigenvectors and not needed for the exact finite-dimensional identity.

Fixed radial Riesz blocks

:   Not a uniform closure route in the present audit. Their projector norms and diagonal block energies grow rapidly, even though the signed aggregate is moderate.

Cross-Stein aggregate

:   The invariant target is the quadratic form $\mathbf 1^*K\mathbf 1$, or a uniform upper obtained from normalized coherence and diagonal block energies.

Stage A1

:   Open. [\[cond:cross-budget\]](#cond:cross-budget){reference-type="ref" reference="cond:cross-budget"} is a sharper sufficient condition, not a theorem for the physical small-noise family.

Stage A4 intrinsic identification

:   Still conditional on Stage A1. RH-52--RH-55 close the peripheral, factor, and adaptive-cutoff interfaces once the Hardy budget is supplied.

The next meaningful gate is an angular or time-ordered block construction with uniform separation, a direct signed cross-Stein estimate, or a validated Schur/Gramian formulation that avoids individual spectral coordinates. Merely increasing the precision of the current five-scale eigensolver would not establish a dyadic theorem.

# No arithmetic or Hilbert--Polya conclusion

Nothing here supplies a von Mangoldt or prime-power trace formula, a zeta-zero spectral identity, a canonical self-adjoint operator, or a $T\log T$ counting law. No Riemann-hypothesis conclusion is drawn. The independent twin-prime branch is not used. This is a transfer-operator Hardy/Riesz route analysis and a delimited negative diagnostic for one block choice.

# Reproducibility

The directory contains the source algebra, tests, five-scale all-column results, the Arb scalar certificate, figure, publication hashes, and archive verification. The principal commands are:

    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/pytest -q -p no:cacheprovider
    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/run_overlap_pilot.py
    PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/run_arb_block_audit.py
    MPLBACKEND=Agg PYTHONDONTWRITEBYTECODE=1 /root/math/.venv/bin/python \
      experiments/make_figures.py
    latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex

The theorem, cross-Stein identities, and scalar Arb formulas are exact in their stated finite-dimensional scope. The grouped production eigendata are binary64 evidence only. Stage A1, unconditional intrinsic identification, any self-adjoint Hilbert--Polya realization, and all arithmetic conclusions remain outside the claims.
