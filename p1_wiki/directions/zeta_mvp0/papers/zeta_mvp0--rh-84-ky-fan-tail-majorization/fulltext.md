---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-84-ky-fan-tail-majorization"
canonical_tex: "zeta_mvp0/papers/RH-84-ky-fan-tail-majorization/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-84-ky-fan-tail-majorization/main.pdf"
source_sha256: "59a15a9156baa5150f6689716cb3f014ef687f88428c8e47cd46954f21d6b4e9"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Ky Fan Tail Majorization and a Weaker Endpoint Corridor to Stage A Captured Energy, Rank Staircases, and Seven-Scale Stress Evidence

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-84-ky-fan-tail-majorization>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-84-ky-fan-tail-majorization/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-84-ky-fan-tail-majorization/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-84-ky-fan-tail-majorization/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-84-ky-fan-tail-majorization/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-83 proved that termwise singular-value majorization is sufficient for an optimal endpoint factorization, but dyadic singular staircases make that condition stronger than the downstream problem requires. This paper isolates the weaker invariant that RH-78 actually uses: the Hilbert--Schmidt energy left outside a low-rank postblock space.

  For a Hilbert--Schmidt operator $B$ with Gramian $G=B^*B$, Ky Fan's principle gives $$\tau_r(B)^2
   =\operatorname{tr}G-\sum_{j=1}^r\lambda_j(G)
   \le \left\lVert B(I-P)\right\rVert_2^2$$ for every rank-$r$ orthogonal projector $P$. Thus a validated captured-energy lower bound certifies the optimal tail without resolving each singular value.

  If the physical postblock state satisfies the tail-majorization condition $$\tau_{J_\sigma+\ell}(B_\sigma)
   \le \alpha_\sigma
   \tau_{J_\sigma+\ell}(\mathcal R_\sigma)+\varepsilon_\sigma,$$ then RH-82 immediately yields an exponential excess-rank tail. Polylogarithmic $\alpha_\sigma$, remainder, and observability bounds close the RH-78 effective-rank corridor. This condition neither identifies coordinates nor controls the leading singular values, and is strictly weaker than the RH-83 factorization gate.

  The numerical audit keeps the five 192-bit interval-certified postblock tails and adds two out-of-sample levels: $\sigma=0.005$ at dimension $1024$ and $\sigma=0.0025$ at dimension $2048$. The clock rank grows only from four to eight. At every level the physical clock-plus-two tail is below $1.4\%$ of the linear endpoint-model tail. The largest interval-certified relative tail is $2.34\times10^{-7}$; the two extended binary64 stress tails are below $1.56\times10^{-15}$.

  The result narrows the all-level problem to a captured-energy theorem for a clock-dimensional postcritical packet space. The two new levels are diagnostic, not a proof of uniformity. Stage A1, unconditional Stage A4, Hilbert--Polya, and the Riemann Hypothesis remain open.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Ky Fan Tail Majorization and a Weaker Endpoint Corridor to Stage A\
  Captured Energy, Rank Staircases, and Seven-Scale Stress Evidence
```

## Markdown 正文

**Keywords:** Ky Fan principle; singular-value tail; effective rank; captured energy; postblock state; small noise.

**MSC 2020:** 47B10; 47A75; 15A18; 65G20.

# Why termwise majorization is more than needed

The RH-83 optimal factorization theorem compares every leading physical singular value with the corresponding endpoint singular value [@WangSingularFactor2026]. This is natural for an operator factorization, but individual ratios can jump when a new singular staircase enters between neighboring dyadic scales. RH-78 does not use those ratios. It uses only the residual left after a low-rank approximation [@WangEffectiveRank2026].

RH-82 already supplies the mediator estimate $$\tau_{J_\sigma+\ell}(\mathcal R_\sigma)
 \le C_Rq^\ell,
 \qquad J_\sigma=\frac{\log(1/\sigma)}{2\log\lambda}+O(1),
 \label{eq:endpoint-tail}$$ with $0<q<1$ [@WangHalfLog2026]. The question is how little information about $B_\sigma$ is required to inherit this tail.

# Ky Fan certification of a postblock tail

Let $B:\mathcal H_1\to\mathcal H_2$ be Hilbert--Schmidt and let $G=B^*B$. Define $$\tau_r(B)=\inf_{\operatorname{rank}L\le r}\left\lVert B-L\right\rVert_2.$$

[\[thm:kyfan\]]{#thm:kyfan label="thm:kyfan"} For every integer $r\ge0$, $$\tau_r(B)^2
 =\operatorname{tr}G-\sum_{j=1}^r\lambda_j(G).
 \label{eq:optimal-tail}$$ If $P$ is any rank-$r$ orthogonal projection on $\mathcal H_1$, then $$\boxed{
 \tau_r(B)^2\le\left\lVert B(I-P)\right\rVert_2^2
 =\operatorname{tr}G-\operatorname{tr}(PG).}
 \label{eq:candidate-tail}$$

The first identity is the Eckart--Young formula. Ky Fan's maximum principle states $$\operatorname{tr}(PG)
 \le\sum_{j=1}^r\lambda_j(G).$$ Subtract from $\operatorname{tr}G$ to obtain [\[eq:candidate-tail\]](#eq:candidate-tail){reference-type="eqref" reference="eq:candidate-tail"} [@Bhatia1997].

The theorem is suited to interval work: one may fix a floating candidate subspace and evaluate the residual directly in rigorous arithmetic. No interval eigendecomposition of the tiny tail eigenvalues is required.

# Tail-majorization transfer

[\[thm:transfer\]]{#thm:transfer label="thm:transfer"} Suppose that for a rank schedule $r_\sigma=J_\sigma+\ell_\sigma$, $$\tau_{r_\sigma}(B_\sigma)
 \le\alpha_\sigma\tau_{r_\sigma}(\mathcal R_\sigma)
 +\varepsilon_\sigma.
 \label{eq:tail-majorization}$$ Then $$\boxed{
 \tau_{r_\sigma}(B_\sigma)
 \le\alpha_\sigma C_Rq^{\ell_\sigma}
 +\varepsilon_\sigma.}
 \label{eq:transferred-tail}$$ If $\alpha_\sigma$, $\varepsilon_\sigma$, and the square root of the future observability norm are polylogarithmic, then a logarithmic or polylogarithmic $r_\sigma$ satisfies the RH-78 effective-rank residual gate.

Insert [\[eq:endpoint-tail\]](#eq:endpoint-tail){reference-type="eqref" reference="eq:endpoint-tail"} into [\[eq:tail-majorization\]](#eq:tail-majorization){reference-type="eqref" reference="eq:tail-majorization"}. Multiplication by the future observability factor transfers the Hilbert--Schmidt residual to the directional Hardy future exactly as in RH-77.

This is strictly weaker than an RH-83 factorization. A factorization implies [\[eq:tail-majorization\]](#eq:tail-majorization){reference-type="eqref" reference="eq:tail-majorization"} by the ideal property, but a tail inequality says nothing about the leading singular vectors or even their individual sizes.

# Seven-scale audit

The first five levels retain the 192-bit Arb residuals from RH-82. The audit then builds two new frozen matrices at constant spatial resolution per noise width: $$(\sigma,n,M)=(0.005,1024,49),
 \qquad(0.0025,2048,64).$$ These horizons continue the proposed log-square schedule. They are not an analytic horizon theorem.

For each channel, the endpoint model uses the linear powered-row Gram matrix and the physical rank is $$r_\sigma=\lceil H_\sigma\rceil+2.
 \label{eq:rank}$$

::: {#tab:audit}
    $\sigma$   fine dimension   rank   max physical/endpoint tail          evidence
  ---------- ---------------- ------ ---------------------------- -----------------
        0.16               32      4         $1.393\times10^{-2}$               Arb
        0.08               64      5         $3.814\times10^{-6}$               Arb
        0.04              128      6         $9.969\times10^{-7}$               Arb
        0.02              256      6         $5.143\times10^{-6}$               Arb
        0.01              512      7         $9.257\times10^{-7}$               Arb
       0.005             1024      8        $4.687\times10^{-12}$   binary64 stress
      0.0025             2048      8        $1.050\times10^{-12}$   binary64 stress

  : Maximum over both directional channels. Only the first five physical tails are interval certified.
:::

The worst ratio occurs at the coarsest scale. At smaller noise the physical tail is much smaller than the already small endpoint tail. The ambient dimension grows by a factor $64$, while the tested rank only doubles.

![Tail-majorization ratios, interval and stress residuals, excess-rank gain at the finest level, and logarithmic rank versus ambient dimension.](<../../../../../zeta_mvp0/papers/RH-84-ky-fan-tail-majorization/figures/ky_fan_tail_majorization.pdf>){#fig:tail width="\\textwidth"}

# Next theorem and boundary

The all-level target can now be stated without singular-value matching: construct a rank-$O(\log(1/\sigma))$ postcritical packet projector $P_\sigma$ and prove $$\operatorname{tr}(P_\sigma B_\sigma^*B_\sigma)
 \ge\left\lVert B_\sigma\right\rVert_2^2
 -\operatorname{polylog}(1/\sigma)^2.
 \label{eq:captured-energy-target}$$ Combined with [\[thm:kyfan\]](#thm:kyfan){reference-type="ref" reference="thm:kyfan"}, this is enough. The packet vectors may be rotated by the dynamics; they need not equal sampled endpoint rows.

This paper proves the Ky Fan and tail-transfer theorems and validates the five inherited interval scales plus two floating stress levels. It does not prove [\[eq:captured-energy-target\]](#eq:captured-energy-target){reference-type="eqref" reference="eq:captured-energy-target"} uniformly, close Stage A1 or unconditional Stage A4, construct an A5 relative determinant, produce a self-adjoint Hilbert--Polya operator, derive a $T\log T$ or prime-power law, identify zeta zeros, or prove the Riemann Hypothesis.
