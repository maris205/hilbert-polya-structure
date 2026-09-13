---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-74-validated-upstream-hardy-bridge"
canonical_tex: "zeta_mvp0/papers/RH-74-validated-upstream-hardy-bridge/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-74-validated-upstream-hardy-bridge/main.pdf"
source_sha256: "cd77f73e3cb684d76233abf5938c5275af995f165c693e9212520f9476bf4b7d"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Validated Upstream-to-Frozen Hardy Bridges for the Folded-Gaussian Production Chain Analytic Factor Transport, Normalized Couplings, and a Robust Four-Block Difference Tail

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-74-validated-upstream-hardy-bridge>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-74-validated-upstream-hardy-bridge/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-74-validated-upstream-hardy-bridge/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-74-validated-upstream-hardy-bridge/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-74-validated-upstream-hardy-bridge/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-70 certified terminal Hardy bounds for exact-dyadic frozen production arrays, but folded-Gaussian assembly, spectral deflation, and normalized source/observation construction remained upstream of that certificate. RH-72 and RH-73 supplied the missing matrix and peripheral-factor balls. This paper composes those balls through the production formulas and closes the complete finite-scale upstream-to-frozen bridge.

  First, a norm-bounded perturbation of the repaired matrix is propagated through the stationary Neumann system, the bordered right-eigenpair Newton map, and the bordered left solve. This validates Perron/parity projectors and deflated bulk operators for the analytic folded-Gaussian midpoint matrices themselves. For nonzero coupling blocks $B,B_0$, we use $$\left\lVert B/\left\lVert B\right\rVert_{\mathrm F}-B_0/\left\lVert B_0\right\rVert_{\mathrm F}\right\rVert_{\mathrm F}
   \le \frac{2\varepsilon}{\left\lVert B_0\right\rVert_{\mathrm F}-\varepsilon},
   \qquad \left\lVert B-B_0\right\rVert_{\mathrm F}\le\varepsilon<\left\lVert B_0\right\rVert_{\mathrm F},$$ and product perturbation bounds to enclose every operator, source, and observation against its RH-70 frozen counterpart.

  Second, let $A=A_0+E$, $\left\lVert E\right\rVert\le\varepsilon_A$, and $C_k\ge\left\lVert A_0^k\right\rVert$. The discrete Volterra identity gives the rigorous recursion $$D_k=\varepsilon_A\sum_{j=0}^{k-1}C_{k-1-j}(C_j+D_j)
   \ge\left\lVert A^k-A_0^k\right\rVert.$$ This bounds every finite transfer-coefficient difference. A common block horizon certifies both $A^M$ and $A_0^M$ contractive; four block lengths then leave a geometric true/reference tail. The result is a robust realization of the augmented Hardy difference bridge.

  A 160-bit Arb audit covers both left and right channels at $\sigma=0.16,0.08,0.04,0.02,0.01$. The largest certified operator, source, and observation errors are $2.64\times10^{-11}$, $2.63\times10^{-11}$, and $1.74\times10^{-11}$. The largest full Hardy bridge is $2.03\times10^{-6}$. Every bridge lies below its inherited RH-71 one-percent headroom; the worst consumes only $0.217\%$ of that slack.

  Thus the five archived scales are now green from analytic folded-Gaussian assembly through rank-two deflation and terminal Hardy completion. This is a finite-scale closure, not a uniform small-noise theorem: Stage A1 and unconditional Stage A4 remain open, as do all later Hilbert--Polya and Riemann-Hypothesis objectives.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Validated Upstream-to-Frozen Hardy Bridges for the Folded-Gaussian Production Chain\
  Analytic Factor Transport, Normalized Couplings, and a Robust Four-Block Difference Tail
```

## Markdown 正文

**Keywords:** Hardy norm; interval arithmetic; spectral projector; normalized coupling; Volterra identity; robust systems.

**MSC 2020:** 47A10; 47A55; 47B35; 65G20; 93B28.

# Introduction

The production chain used in the recent RH layers has four stages: $$\text{folded kernel}
 \longrightarrow \text{Perron/parity deflation}
 \longrightarrow \text{normalized transfer blocks}
 \longrightarrow \text{Hardy completion}.
 \label{eq:chain}$$ RH-70 proved the last arrow rigorous after the generated binary64 arrays were embedded as exact dyadic Arb inputs [@WangFrozen2026]. Its result was therefore "frozen green" but "end-to-end amber." RH-71 quantified the remaining upstream bridge budget: all ten channels retain positive headroom inside a one-percent finite-scale target [@WangReview2026].

RH-72 certified the analytic folded-Gaussian midpoint matrices against exact stochastic dyadic repairs, including Haar coarse and cross blocks [@WangAssembly2026]. RH-73 then validated the stationary and negative parity factors of those repaired matrices [@WangPeripheral2026]. Two tasks remain before these results can be inserted into RH-70:

1.  transfer the repaired spectral factors across the RH-72 analytic matrix ball and through all source/observation normalizations;

2.  certify the Hardy norm of the difference between every resulting analytic transfer sequence and the frozen sequence.

The first task is delicate because projectors and normalized couplings are nonlinear. The second cannot use a one-step geometric estimate: the scaled bulk matrices are stable but nonnormal, and their one-step Euclidean norms need not be below one. The correct object is the already certified block contraction.

This paper supplies both pieces. All binary64 arrays serve only as exact dyadic centers. Scalar decisions and matrix products used by the certificate are recomputed at 160-bit Arb precision [@Johansson2017; @Higham2002].

# The analytic and frozen triples {#sec:triples}

Let $P_f$ be the analytic fine folded-Gaussian midpoint matrix and let $U,W$ be the exact Haar coarse and detail embeddings. Define $$P_c=U^TP_fU,qquad B=U^TP_fW,qquad C=W^TP_fU.$$ For either fine or coarse matrix, let $\Pi_+$ and $\Pi_-$ denote its Perron and negative parity Riesz projectors, let $\lambda_-$ be the parity eigenvalue, and put $$Q=I-\Pi_+-\Pi_-,qquad
 K=P-\Pi_+-\lambda_-\Pi_-.$$

At the fixed Hardy radius $R_H=0.85$, the true left and right production triples are $$\begin{aligned}
 A_L&=K_f/R_H,&
 X_L&=Q_fU\frac{B}{\left\lVert B\right\rVert_{\mathrm F}},&
 Y_L&=U^T,\label{eq:left}\\
 A_R&=K_c^T/R_H,&
 X_R&=\frac{C^T}{\left\lVert C\right\rVert_{\mathrm F}},&
 Y_R&=Q_c^T.\label{eq:right}\end{aligned}$$ The frozen triples $(A_{0,s},X_{0,s},Y_{0,s})$ use the RH-70 binary64 matrix, Haar constant, eigendecomposition, and normalizations, interpreted as exact dyadic arrays.

Our goal is to certify $$\left\lVert A_s-A_{0,s}\right\rVert_2\le\varepsilon_{A,s},
 \quad
 \left\lVert X_s-X_{0,s}\right\rVert_{\mathrm F}\le\varepsilon_{X,s},
 \quad
 \left\lVert Y_s-Y_{0,s}\right\rVert_{\mathrm F}\le\varepsilon_{Y,s},
 \label{eq:triple-errors}$$ and then bound the full transfer difference $$\Delta_s^2
 =\sum_{k\ge0}
 \left\lVert Y_sA_s^kX_s-Y_{0,s}A_{0,s}^kX_{0,s}\right\rVert_{\mathrm F}^2.
 \label{eq:bridge}$$

# Transporting repaired factors to the analytic matrix {#sec:factors}

Let $A_r$ be an exact repaired stochastic matrix and let $A=A_r+E$, $\left\lVert E\right\rVert_2\le\delta$, be the corresponding analytic matrix. RH-73 provides stationary and parity centers together with inverse, residual, and contraction bounds for $A_r$.

## Stationary factor

Let $$L_r=I-A_r^T+\frac1n\mathbf1\mathbf1^T,
 \qquad L=L_r-E^T.$$ If $M_r\ge\left\lVert L_r^{-1}\right\rVert$ and $M_r\delta<1$, then $$\left\lVert L^{-1}\right\rVert
 \le\frac{M_r}{1-M_r\delta}.
 \label{eq:stationary-transfer}$$ If the repaired stationary vector obeys $\left\lVert\pi_r-\pi_0\right\rVert\le e_r$, subtraction of $L\pi=L_r\pi_r=n^{-1}\mathbf1$ gives $$\left\lVert\pi-\pi_0\right\rVert
 \le e_r+
 \frac{M_r\delta(\left\lVert\pi_0\right\rVert+e_r)}{1-M_r\delta}.
 \label{eq:stationary-ball}$$ Since the analytic matrix is exactly stochastic, its Perron right vector is again $\mathbf1$ and the projector error is $\sqrt n$ times [\[eq:stationary-ball\]](#eq:stationary-ball){reference-type="eqref" reference="eq:stationary-ball"}.

## Bordered parity factors

For the RH-73 right Newton system, let $\beta,\gamma,M$ be the repaired preconditioned residual, Jacobian defect, and inverse norm. The matrix ball augments them to $$\widehat\beta=\beta+M\delta\left\lVert r_0\right\rVert,qquad
 \widehat\gamma=\gamma+M\delta.
 \label{eq:augmented-newton}$$

[\[prop:right\]]{#prop:right label="prop:right"} If $$\widehat\beta+\widehat\gamma\rho+M\rho^2\le\rho,
 \qquad \widehat\gamma+M\rho<1,$$ then every matrix in the norm ball, in particular $A$, has a unique normalized right parity eigenpair in the joint radius-$\rho$ ball around the archived center.

The perturbation contributes $Er_0$ to the center residual and $E$ to the right-vector block of the Jacobian. Their preconditioned norms are bounded by the two added terms in [\[eq:augmented-newton\]](#eq:augmented-newton){reference-type="eqref" reference="eq:augmented-newton"}. The bilinear remainder is unchanged, so the RH-73 contraction proof applies uniformly over the matrix ball.

For the bordered left system, matrix and eigenvalue perturbations contribute at most $M_\ell(\delta+\rho)$. Thus, with repaired defect $\gamma_\ell$, inverse norm $M_\ell$, center residual correction $\beta_{\ell,0}$, and left center norm $L_0$, we use $$\begin{aligned}
 \Gamma_\ell&=\gamma_\ell+M_\ell(\delta+\rho),\label{eq:left-defect}\\
 e_\ell&=
 \frac{\beta_{\ell,0}+M_\ell(\delta+\rho)L_0}{1-\Gamma_\ell}.
 \label{eq:left-ball}\end{aligned}$$ Every archived channel has $\Gamma_\ell<1$. RH-73's normalized projector formula then gives analytic $\Pi_-$, rank-two, complement, and bulk balls. The bulk bound additionally contains the base matrix error $\delta$.

# Normalized source/observation transfer {#sec:normalization}

[\[prop:normalization\]]{#prop:normalization label="prop:normalization"} Let $B_0\ne0$ and suppose $\left\lVert B-B_0\right\rVert_{\mathrm F}\le\varepsilon<\left\lVert B_0\right\rVert_{\mathrm F}$. Then $$\left\lVert B/\left\lVert B\right\rVert_{\mathrm F}-B_0/\left\lVert B_0\right\rVert_{\mathrm F}\right\rVert_{\mathrm F}
 \le\frac{2\varepsilon}{\left\lVert B_0\right\rVert_{\mathrm F}-\varepsilon}.
 \label{eq:normalized}$$

Insert $B_0/\left\lVert B\right\rVert_{\mathrm F}$ and use $|\left\lVert B\right\rVert_{\mathrm F}-\left\lVert B_0\right\rVert_{\mathrm F}|\le\varepsilon$ and $\left\lVert B\right\rVert_{\mathrm F}\ge\left\lVert B_0\right\rVert_{\mathrm F}-\varepsilon$.

RH-72 gives a common two-norm error $e_H$ for exact analytic coarse and cross blocks against the frozen pipeline. For an $m\times m$ block, $$\left\lVert B-B_0\right\rVert_{\mathrm F},\ \left\lVert C-C_0\right\rVert_{\mathrm F}le\sqrt m\,e_H.
 \label{eq:cross-frob}$$ It also gives $\left\lVert U-U_0\right\rVert_2\le e_U$ and hence $\left\lVert U-U_0\right\rVert_{\mathrm F}\le\sqrt m,e_U$.

For example, if $e_Q\ge\left\lVert Q_f-Q_{f,0}\right\rVert_2$ and $N_{Q,0}\ge\left\lVert Q_{f,0}\right\rVert_2$, the left source obeys $$\left\lVert X_L-X_{L,0}\right\rVert_{\mathrm F}
 \le e_Q+N_{Q,0}e_U
 +N_{Q,0}\left\lVert U_0\right\rVert_2 e_{\widehat B},
 \label{eq:left-source}$$ where $e_{\widehat B}$ is the right side of [\[eq:normalized\]](#eq:normalized){reference-type="eqref" reference="eq:normalized"}. The right source error is $e_{\widehat C}$, the left observation error is $\sqrt m,e_U$, and the right observation error is the Frobenius complement ball. Together with the bulk bounds, these are exactly the triple errors in [\[eq:triple-errors\]](#eq:triple-errors){reference-type="eqref" reference="eq:triple-errors"}.

# A robust augmented Hardy difference bridge {#sec:hardy}

Fix one channel and suppress its subscript. Write $A=A_0+E$ and let $\left\lVert E\right\rVert_2\le\varepsilon_A$. Suppose $C_k\ge\left\lVert A_0^k\right\rVert_2$.

[\[thm:volterra\]]{#thm:volterra label="thm:volterra"} Define $D_0=0$ and $$D_k=\varepsilon_A
 \sum_{j=0}^{k-1}C_{k-1-j}(C_j+D_j).
 \label{eq:volterra}$$ Then $\left\lVert A^k-A_0^k\right\rVert_2\le D_k$ and $\left\lVert A^k\right\rVert_2\le C_k+D_k$ for every $k$.

The discrete Volterra identity is $$A^k-A_0^k
 =\sum_{j=0}^{k-1}A_0^{k-1-j}EA^j.$$ Induction and submultiplicativity give [\[eq:volterra\]](#eq:volterra){reference-type="eqref" reference="eq:volterra"}.

Let $x_0=\left\lVert X_0\right\rVert_{\mathrm F}$, $y_0=\left\lVert Y_0\right\rVert_{\mathrm F}$, and let $\varepsilon_X,\varepsilon_Y$ be the source and observation errors. Put $x=x_0+\varepsilon_X$. From a three-term expansion of the transfer coefficient, $$\begin{split}
 d_k:={}&\varepsilon_Y(C_k+D_k)x\\
 &+y_0\{D_kx+C_k\varepsilon_X\}
 \end{split}
 \label{eq:coefficient}$$ bounds $\left\lVert YA^kX-Y_0A_0^kX_0\right\rVert_{\mathrm F}$.

The reference block horizon $M$ is inherited from RH-70. Arb computes exact dyadic prefix power bounds $C_r$ for $0\le r\le M$ and $q_0=C_M<1$. For $k=bM+r$, we use $$C_k=q_0^bC_r.
 \label{eq:block-powers}$$ Let $q=C_M+D_M<1$, and let $S,S_0$ bound the true and reference source-state energies over one block.

[\[thm:bridge\]]{#thm:bridge label="thm:bridge"} For any integer $b\ge1$, $$\begin{split}
 \Delta^2\le{}&\sum_{k=0}^{bM-1}d_k^2\\
 &+2(y_0+\varepsilon_Y)^2
   \frac{q^{2b}}{1-q^2}S
 +2y_0^2\frac{q_0^{2b}}{1-q_0^2}S_0.
 \end{split}
 \label{eq:bridge-upper}$$

The finite prefix follows from [\[eq:coefficient\]](#eq:coefficient){reference-type="eqref" reference="eq:coefficient"}. After $b$ blocks, the true and reference state blocks contract geometrically by $q$ and $q_0$. The squared norm of their transfer difference is at most twice the sum of the two squared norms. Summing both geometric tails proves [\[eq:bridge-upper\]](#eq:bridge-upper){reference-type="eqref" reference="eq:bridge-upper"}.

This theorem is the uncertainty-robust form of RH-70's augmented difference bridge. The exact block-diagonal realization identifies the transfer difference; [\[thm:volterra,thm:bridge\]](#thm:volterra,thm:bridge){reference-type="ref" reference="thm:volterra,thm:bridge"} enclose every realization allowed by the upstream triple balls without replacing those balls by independent entrywise intervals.

# Five-scale interval audit {#sec:audit}

The implementation uses $b=4$ and 160-bit Arb arithmetic. All repaired and frozen entries are exact rationals; all center differences, row/column sums, Frobenius norms, factor-transfer denominators, normalized-coupling denominators, Volterra recursions, finite energies, and tails are outward rounded.

::: {#tab:triple}
    $\sigma$   $n$    $\varepsilon_A$    $\varepsilon_X$    $\varepsilon_Y$
  ---------- ----- ------------------ ------------------ ------------------
        0.16    32   $1.44\,10^{-13}$   $2.86\,10^{-13}$   $9.62\,10^{-14}$
        0.08    64   $4.22\,10^{-13}$   $6.70\,10^{-13}$   $2.89\,10^{-13}$
        0.04   128   $1.28\,10^{-12}$   $1.70\,10^{-12}$   $8.14\,10^{-13}$
        0.02   256   $5.68\,10^{-12}$   $6.34\,10^{-12}$   $3.70\,10^{-12}$
        0.01   512   $2.64\,10^{-11}$   $2.63\,10^{-11}$   $1.74\,10^{-11}$

  : Certified upstream triple errors. Each row reports the larger of the left and right channel values.
:::

The growth is visible but remains tiny relative to every normalization and block-contraction margin. In particular, the largest true block-power upper is $0.021022$.

::: {#tab:bridge}
  ------------------------ ----------------- ----------------- ------------ ----------------- ----------------- -------------

    (lr)2-4(l)5-7 $\sigma$            bridge             slack          use            bridge             slack           use
                      0.16   $1.42\,10^{-6}$   $5.82\,10^{-3}$   $0.0245\%$   $1.26\,10^{-6}$   $6.81\,10^{-3}$    $0.0185\%$
                      0.08   $8.13\,10^{-7}$   $6.98\,10^{-3}$   $0.0117\%$   $5.85\,10^{-7}$   $8.73\,10^{-3}$   $0.00670\%$
                      0.04   $1.83\,10^{-6}$   $8.42\,10^{-4}$    $0.217\%$   $2.03\,10^{-6}$   $1.32\,10^{-3}$     $0.155\%$
                      0.02   $6.64\,10^{-7}$   $1.08\,10^{-3}$   $0.0617\%$   $5.65\,10^{-7}$   $3.60\,10^{-3}$    $0.0158\%$
                      0.01   $3.12\,10^{-7}$   $2.11\,10^{-3}$   $0.0149\%$   $2.55\,10^{-7}$   $3.63\,10^{-3}$   $0.00704\%$
  ------------------------ ----------------- ----------------- ------------ ----------------- ----------------- -------------

  : Full Hardy bridge upper, inherited one-percent slack, and percentage of slack consumed.
:::

Every channel therefore satisfies the RH-71 composition criterion $$\Delta_s\le(1.01)F_s-U_s,$$ where $F_s$ is the certified frozen finite-prefix lower and $U_s$ the frozen full upper. Combining the triangle inequality with RH-70 proves an end-to-end one-percent finite-scale Hardy upper for the analytic production triple.

![Certified triple errors, full upstream bridges versus inherited headroom, and the fraction of slack consumed.](<../../../../../zeta_mvp0/papers/RH-74-validated-upstream-hardy-bridge/figures/validated_upstream_hardy_bridge.pdf>){#fig:audit width="98%"}

# Route consequence and claim boundary {#sec:boundary}

The finite-scale chain [\[eq:chain\]](#eq:chain){reference-type="eqref" reference="eq:chain"} is now closed at all five archived scales. The result includes:

1.  analytic folded-Gaussian and Haar assembly;

2.  analytic Perron/parity factor transfer and rank-two deflation;

3.  normalized source/observation transfer;

4.  a robust augmented Hardy difference bridge;

5.  composition with the frozen terminal Hardy certificate.

This changes the route map. "Upstream interval inclusion" is no longer an open finite-scale gate. Full Stage A1 still requires a uniform theorem for the small-noise/dyadic family: the archived dimensions, horizons, factor condition numbers, and triple errors must be replaced by analytic functions of $\sigma$ and the dyadic level. The next papers should therefore study uniform horizon, phase, and effective-rank scaling.

The present finite list does not close Stage A1, unconditional Stage A4, or a renormalized determinant limit. It constructs no self-adjoint Hilbert--Polya operator, proves no $T\log T$ counting law or prime-power trace formula, identifies no zeta zeros, and does not prove the Riemann Hypothesis.

# Conclusion

The earlier amber status came from a genuine certificate boundary, not from a large numerical discrepancy. Once the RH-72 and RH-73 balls are propagated through the exact production formulas, the complete upstream mismatch is only of order $10^{-6}$ in Hardy norm and consumes at most $0.217\%$ of the available bridge slack. The finite-scale production chain is therefore rigorous end to end.

The surviving wall is asymptotic. RH-75 should begin replacing the five observed block horizons by a uniform small-noise horizon law, while preserving the blockwise mechanism that made the present closure possible.
