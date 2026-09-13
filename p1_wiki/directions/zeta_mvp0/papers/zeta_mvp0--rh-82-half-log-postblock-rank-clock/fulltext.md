---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-82-half-log-postblock-rank-clock"
canonical_tex: "zeta_mvp0/papers/RH-82-half-log-postblock-rank-clock/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-82-half-log-postblock-rank-clock/main.pdf"
source_sha256: "2a88af975212660b50765bdf6acd35b295d6df80ef235ca08737c6c050d68ef3"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Exponential Excess-Rank Tails and the Half-Logarithmic Postblock Clock From Endpoint Gaussian Resolution to a Concrete Stage-A Factorization Gate

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-82-half-log-postblock-rank-clock>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-82-half-log-postblock-rank-clock/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-82-half-log-postblock-rank-clock/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-82-half-log-postblock-rank-clock/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-82-half-log-postblock-rank-clock/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-77 found that the physical postblock states are extraordinarily compressible, while RH-81 identified an all-level effective-rank theorem as the preferred remaining Stage-A gate. This paper replaces that qualitative request by a specific factorization problem.

  RH-16 constructed the endpoint-projected Gaussian resolution operator $\mathcal R_\sigma$ and proved its half-logarithmic threshold-rank law. We sharpen that result from a count to a full approximation-number tail. Let $J_\sigma=\max\{k:\delta_k\ge\sigma\}$ for the geometric endpoint ladder. If $\delta_{k+1}/\delta_k\le q<1$ eventually and the unresolved projected-row energy satisfies $F(t)\le Ct^2$, then for every $\ell\ge0$, $$\tau_{J_\sigma+\ell}(\mathcal R_\sigma)
   \le \sqrt{\frac{C}{1-q^2}}q^\ell,$$ where $\tau_r$ is the optimal Hilbert--Schmidt rank-$r$ residual. Since $J_\sigma=\log(1/\sigma)/(2\log\lambda)+O(1)$, every extra rank beyond the half-logarithmic clock buys exponential tail decay.

  We then prove an ideal-property transfer theorem. If a physical postblock state factors as $$B_\sigma=U_\sigma\mathcal R_\sigma V_\sigma+E_\sigma,$$ then its rank tail is bounded by the endpoint tail multiplied by $\left\lVert U_\sigma\right\rVert\left\lVert V_\sigma\right\rVert$, plus $\left\lVert E_\sigma\right\rVert_2$. Polylogarithmic outer, remainder, and observability bounds therefore imply the RH-78 effective-rank corridor with rank $O(\log(1/\sigma))$.

  A 192-bit Arb audit tests the canonical schedule $r_\sigma=\lceil\log(1/\sigma)/(2\log\lambda)\rceil+2$ on all ten archived postblock channels. The ranks are four through seven, the maximum relative residual is $2.34\times10^{-7}$, and the maximum full-future Hardy perturbation is $5.05\times10^{-9}$. In the RH-16 linear endpoint-row model, the same clock-plus-two tail remains below $9.19\times10^{-8}$ from $\sigma=10^{-2}$ to $10^{-12}$.

  The actual endpoint-to-postblock factorization is not proved here. It is now the explicit first-open Stage-A gate. Unconditional Stage A4, Hilbert--Polya, and the Riemann Hypothesis remain open.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Exponential Excess-Rank Tails and the Half-Logarithmic Postblock Clock\
  From Endpoint Gaussian Resolution to a Concrete Stage-A Factorization Gate
```

## Markdown 正文

**Keywords:** approximation numbers; effective rank; Gaussian resolution; postblock state; Hilbert--Schmidt tail; small noise.

**MSC 2020:** 47B10; 47B06; 37C30; 65G20.

# From a rank observation to a factorization gate

The RH-77 production audit showed that rank two captures at least $99\%$ and rank four at least $99.9999\%$ of every archived postblock state [@WangEffectiveRank2026]. RH-78 proved that a polylogarithmic rank and future residual are enough for Stage A1 [@WangTwoCorridors2026]. What remained unclear was why the physical family should possess such a rank law at all dyadic levels.

There is already an analytic logarithmic-rank object in the program. RH-16 associated normalized Gaussian rows to the endpoint ladder $$\delta_k=C_b\lambda^{-2k}(1+o(1)),
 \qquad \lambda=1.678573510428322\ldots,
 \label{eq:ladder}$$ removed their common endpoint vector, and obtained a Hilbert--Schmidt resolution operator $\mathcal R_\sigma$ [@WangEndpointRank2026]. Its squared Hilbert--Schmidt norm and fixed-threshold rank are $$H_\sigma+O(1),
 \qquad
 H_\sigma:=\frac{\log(1/\sigma)}{2\log\lambda}.
 \label{eq:clock}$$

A threshold count alone does not control the Frobenius tail required by RH-77. The first result supplies that missing estimate.

# Exponential tail beyond the half-log clock

Let $\psi_{\sigma,\delta_k}$ be the normalized endpoint Gaussian row, $Q_\sigma$ the orthogonal complement of the limiting endpoint row, and $$\mathcal R_\sigma e_k=Q_\sigma\psi_{\sigma,\delta_k}.
 \label{eq:R}$$ Write $$F(t)=\left\lVert Q_\sigma\psi_{\sigma,\delta}\right\rVert^2,
 \qquad t=\delta/\sigma.
 \label{eq:F}$$ The exact Gaussian geometry of RH-16 gives $F(t)\le Ct^2$ for $0\le t\le1$.

For a Hilbert--Schmidt operator $T$, define $$\tau_r(T)=\inf_{\operatorname{rank}L\le r}\left\lVert T-L\right\rVert_2
 =\left(\sum_{j>r}s_j(T)^2\right)^{1/2}.
 \label{eq:tau}$$

[\[thm:tail\]]{#thm:tail label="thm:tail"} Assume that for all $k\ge k_0$, $$0<\frac{\delta_{k+1}}{\delta_k}\le q<1.
 \label{eq:ratio}$$ Let $J_\sigma=\max\{k:\delta_k\ge\sigma\}$. For all sufficiently small $\sigma$ and every integer $\ell\ge0$, $$\boxed{
 \tau_{J_\sigma+\ell}(\mathcal R_\sigma)
 \le \sqrt{\frac{C}{1-q^2}}q^\ell.}
 \label{eq:tail-bound}$$ Moreover $J_\sigma=H_\sigma+O(1)$.

Truncate [\[eq:R\]](#eq:R){reference-type="eqref" reference="eq:R"} after column $J_\sigma+\ell$. The truncation has rank at most $J_\sigma+\ell$, hence $$\tau_{J_\sigma+\ell}(\mathcal R_\sigma)^2
 \le \sum_{m\ge1}
 F\!\left(\frac{\delta_{J_\sigma+\ell+m}}\sigma\right).$$ Maximality gives $\delta_{J_\sigma+1}<\sigma$. Iterating [\[eq:ratio\]](#eq:ratio){reference-type="eqref" reference="eq:ratio"} therefore gives $$\frac{\delta_{J_\sigma+\ell+m}}\sigma
 \le q^{\ell+m-1}\le1.$$ Using $F(t)\le Ct^2$ and summing the geometric series proves [\[eq:tail-bound\]](#eq:tail-bound){reference-type="eqref" reference="eq:tail-bound"}. The final clock identity follows from [\[eq:ladder\]](#eq:ladder){reference-type="eqref" reference="eq:ladder"}, as in RH-16.

[\[cor:accuracy\]]{#cor:accuracy label="cor:accuracy"} For every target $0<\varepsilon<1$, there is a rank $$r_{\sigma,\varepsilon}
 =H_\sigma+O\!\left(1+\log\frac1\varepsilon\right)
 \label{eq:accuracy-rank}$$ such that $$\tau_{r_{\sigma,\varepsilon}}(\mathcal R_\sigma)\le\varepsilon.$$ In particular, a polylogarithmic accuracy target costs only $O(\log\log(1/\sigma))$ ranks beyond the half-log clock.

This strengthens the RH-16 threshold theorem without changing its geometric input. The proof uses the unresolved end of the endpoint ladder, where the projected Gaussian rows vanish quadratically.

# Transfer through a physical postblock factorization

Let $B_\sigma$ denote the postblock state $A_\sigma^{M_\sigma}X_\sigma$. The desired bridge is a factorization through the endpoint resolution operator.

[\[thm:factor\]]{#thm:factor label="thm:factor"} Suppose $$B_\sigma=U_\sigma\mathcal R_\sigma V_\sigma+E_\sigma,
 \label{eq:factorization}$$ where $U_\sigma,V_\sigma$ are bounded and $E_\sigma$ is Hilbert--Schmidt. Then for every $\ell\ge0$, $$\boxed{
 \tau_{J_\sigma+\ell}(B_\sigma)
 \le
 \left\lVert U_\sigma\right\rVert\left\lVert V_\sigma\right\rVert
 \sqrt{\frac{C}{1-q^2}}q^\ell
 +\left\lVert E_\sigma\right\rVert_2.}
 \label{eq:factor-tail}$$

Let $R_{\sigma,r}$ be the column truncation used in [\[thm:tail\]](#thm:tail){reference-type="ref" reference="thm:tail"}. The operator $U_\sigma R_{\sigma,r}V_\sigma$ has rank at most $r$. The ideal property of the Hilbert--Schmidt class gives $$\left\lVert B_\sigma-U_\sigma R_{\sigma,r}V_\sigma\right\rVert_2
 \le\left\lVert U_\sigma\right\rVert\left\lVert V_\sigma\right\rVert
 \left\lVert\mathcal R_\sigma-R_{\sigma,r}\right\rVert_2+\left\lVert E_\sigma\right\rVert_2.$$ Insert [\[eq:tail-bound\]](#eq:tail-bound){reference-type="eqref" reference="eq:tail-bound"} and minimize over rank-$r$ approximants [@Simon2005].

[\[cor:stageA\]]{#cor:stageA label="cor:stageA"} Assume [\[eq:factorization\]](#eq:factorization){reference-type="eqref" reference="eq:factorization"} and that $$\left\lVert U_\sigma\right\rVert\left\lVert V_\sigma\right\rVert,\quad
 \left\lVert E_\sigma\right\rVert_2,\quad
 \left\lVert\mathcal O_\sigma\right\rVert^{1/2}
 \le \operatorname{polylog}(1/\sigma),
 \label{eq:polylog-factors}$$ where $\mathcal O_\sigma$ is the future observability Gramian. Then the reduced future and its residual are polylogarithmic at rank $r_\sigma=O(\log(1/\sigma))$. Consequently the RH-78 effective-rank premise holds, provided the already isolated finite-prefix bounds hold.

The RH-16 Hilbert--Schmidt law gives $\left\lVert\mathcal R_\sigma\right\rVert_2=O(\sqrt{\log(1/\sigma)})$. Thus the rank-$r$ factorized approximant has polylogarithmic Hilbert--Schmidt norm. Multiplication by $\left\lVert\mathcal O_\sigma\right\rVert^{1/2}$ controls its future Hardy seminorm. The same observability factor applied to [\[eq:factor-tail\]](#eq:factor-tail){reference-type="eqref" reference="eq:factor-tail"} controls the residual. RH-78 then supplies the stated composition.

The corollary is deliberately a criterion. This paper does not assert [\[eq:factorization\]](#eq:factorization){reference-type="eqref" reference="eq:factorization"} for the physical folded-Gaussian postblock state.

# Validated clock audit

The frozen audit uses exactly the RH-77 matrices and horizons. Binary64 matrix entries and SVD candidates are lifted exactly into Arb, and all matrix powers and residual norms are propagated at 192-bit precision. The rank is fixed before inspecting each channel: $$r_\sigma=\lceil H_\sigma\rceil+2.
 \label{eq:audit-rank}$$

::: {#tab:audit}
    $\sigma$   $H_\sigma$   rank   max relative residual        max future error
  ---------- ------------ ------ ----------------------- -----------------------
        0.16       1.7691      4    $2.340\times10^{-7}$    $5.044\times10^{-9}$
        0.08       2.4383      5   $7.528\times10^{-11}$   $2.111\times10^{-12}$
        0.04       3.1074      6   $1.937\times10^{-11}$   $7.256\times10^{-13}$
        0.02       3.7765      6   $2.870\times10^{-10}$   $6.262\times10^{-12}$
        0.01       4.4457      7   $1.048\times10^{-10}$   $1.752\times10^{-12}$

  : Outward-rounded maxima over the two physical channels.
:::

The coarsest channel is the worst one. Across all ten channels, energy capture is at least $0.999999999999945$. The clock-plus-two rule is therefore substantially stronger than the fixed rank-four engineering gate of RH-77.

As an independent model check, the RH-16 linear-row Gram operator was replayed on six noise levels from $10^{-2}$ to $10^{-12}$. The optimal Hilbert--Schmidt tail at [\[eq:audit-rank\]](#eq:audit-rank){reference-type="eqref" reference="eq:audit-rank"} lies between $8.93\times10^{-8}$ and $9.19\times10^{-8}$. This floating Gram diagnostic is consistent with a fixed excess rank, but the theorem comes from [\[thm:tail\]](#thm:tail){reference-type="ref" reference="thm:tail"}, not from the fit.

![Half-log clock, physical postblock residuals, endpoint-row model tails, and the geometric excess-rank majorant.](<../../../../../zeta_mvp0/papers/RH-82-half-log-postblock-rank-clock/figures/half_log_postblock_rank_clock.pdf>){#fig:clock width="\\textwidth"}

# Route consequence and boundary

The preferred Stage-A route is now narrower. It is unnecessary to guess a new singular-value law for the full physical matrices. The endpoint resolution operator already has the exact logarithmic rank and exponential tail required downstream. The next task is to build [\[eq:factorization\]](#eq:factorization){reference-type="eqref" reference="eq:factorization"}, with factor norms and remainder compatible with [\[eq:polylog-factors\]](#eq:polylog-factors){reference-type="eqref" reference="eq:polylog-factors"}.

This paper proves the endpoint excess-rank theorem and the abstract factorization transfer. It validates the half-log plus two schedule only for the five archived frozen families. It does not prove the physical factorization, uniform Stage A1, unconditional Stage A4, an A5 relative determinant, a self-adjoint Hilbert--Polya operator, a $T\log T$ law, a prime-power trace formula, a zeta-zero identification, or the Riemann Hypothesis.
