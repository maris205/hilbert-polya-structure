---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-88-predictor-corrector-energy-contraction"
canonical_tex: "zeta_mvp0/papers/RH-88-predictor-corrector-energy-contraction/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-88-predictor-corrector-energy-contraction/main.pdf"
source_sha256: "ecc03ce36bcd2ee1f19a961ee037b1e7c04afbdb6feea344736a7b7917838a39"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Predictor--Corrector Energy Contraction Residual Rayleigh Factorization and the Global-Norm Barrier

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-88-predictor-corrector-energy-contraction>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-88-predictor-corrector-energy-contraction/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-88-predictor-corrector-energy-contraction/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-88-predictor-corrector-energy-contraction/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-88-predictor-corrector-energy-contraction/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-87 reduced dynamic packet control to the one-step Rayleigh injection $\iota_{j+1}$. This paper determines which multiplicative contraction mechanisms can and cannot control that scalar.

  For a packet $P_j$, current relative residual energy $\varepsilon_j$, and $X_{j+1}=AX_j$, the residual Rayleigh factorization is exact: $$\iota_{j+1}=\chi_j\varepsilon_j,
   \qquad
   \chi_j=
   \frac{\left\lVert AX_j(I-P_j)\right\rVert_2^2/\left\lVert X_j(I-P_j)\right\rVert_2^2}
   {\left\lVert AX_j\right\rVert_2^2/\left\lVert X_j\right\rVert_2^2}.$$ For the normalized-memory tail $E_j$, put $\theta_j=\iota_{j+1}/E_j$ and let $\gamma_{j+1}=E_{j+1}/(\iota_{j+1}+\eta E_j)$ be the variational reoptimization factor. The predictor-corrector contraction identity is $$\frac{E_{j+1}}{E_j}=\gamma_{j+1}(\theta_j+\eta),
   \qquad 0\le\gamma_{j+1}\le1.$$

  A 192-bit five-scale audit separates three routes. A rigorously tested global operator-norm coefficient exceeds one in all ten channels. The exact directional point-packet predictor contracts in only six channels, and the memory predictor in nine. After variational packet correction, all ten memory tails contract, with largest factor below $0.235$. In the finest right channel the predictor coefficient is about $1.0193$, but $\gamma\approx0.1502$ reduces the actual factor below $0.153$.

  Thus the global-norm barrier and point-packet barrier are branch-level negative results, not an obstruction to the memory route. The next theorem must quantify the reoptimization dividend. Uniform Stage A, Hilbert--Polya, and the Riemann Hypothesis remain open.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Predictor--Corrector Energy Contraction\
  Residual Rayleigh Factorization and the Global-Norm Barrier
```

## Markdown 正文

**Keywords:** residual Rayleigh quotient; predictor-corrector; packet reoptimization; Ky Fan energy; interval arithmetic.

**MSC 2020:** 47A75; 47B10; 15A18; 65G20.

# From additive injection to multiplicative contraction

RH-86 defined the normalized memory Gramian and its optimal packet [@WangMemory2026]. RH-87 proved $$E_{j+1}\le\iota_{j+1}+\eta E_j,
 \label{eq:rh87}$$ reducing the all-level problem to a scalar injection law [@WangInjection2026]. A tempting next step is to bound injection by a constant times $E_j$. There are three distinct constants: a global operator norm, a point-packet residual quotient, and a memory predictor quotient.

# Residual Rayleigh factorization

Let $$\varepsilon_j(P)=\frac{\left\lVert X_j(I-P)\right\rVert_2^2}{\left\lVert X_j\right\rVert_2^2},
 \qquad
 \iota_{j+1}(P)=\frac{\left\lVert AX_j(I-P)\right\rVert_2^2}{\left\lVert AX_j\right\rVert_2^2}.$$

[\[thm:rayleigh\]]{#thm:rayleigh label="thm:rayleigh"} If $X_j(I-P)\ne0$, then $$\boxed{\iota_{j+1}(P)=\chi_j(P)\varepsilon_j(P)},
 \label{eq:factorization}$$ where $$\chi_j(P)=
 \frac{\left\lVert AX_j(I-P)\right\rVert_2^2/\left\lVert X_j(I-P)\right\rVert_2^2}
 {\left\lVert AX_j\right\rVert_2^2/\left\lVert X_j\right\rVert_2^2}.$$ Moreover, $$\chi_j(P)\le
 \chi_j^{\mathrm{glob}}
 :=\frac{\left\lVert A\right\rVert^2}{\left\lVert AX_j\right\rVert_2^2/\left\lVert X_j\right\rVert_2^2}.
 \label{eq:global}$$

Divide the definition of $\iota_{j+1}$ by that of $\varepsilon_j$ and regroup the two Rayleigh growth factors. The global bound follows from $\left\lVert AY\right\rVert_2\le\left\lVert A\right\rVert\left\lVert Y\right\rVert_2$.

The quotient $\chi_j$ measures selective damping of the actual residual directions relative to the full state. It can be much smaller than the global bound, but it need not be below one at every step.

# Predictor-corrector contraction identity

Let $P_j$ be the optimal rank-$r$ memory packet, let $E_j=E_r(G_j)$, and define $$\theta_j=\frac{\iota_{j+1}(P_j)}{E_j},
 \qquad
 \gamma_{j+1}=
 \frac{E_{j+1}}{\iota_{j+1}(P_j)+\eta E_j}.$$

[\[thm:pc\]]{#thm:pc label="thm:pc"} Whenever $E_j>0$, $$\boxed{
 \frac{E_{j+1}}{E_j}=\gamma_{j+1}(\theta_j+\eta),
 \qquad 0\le\gamma_{j+1}\le1.}
 \label{eq:pc}$$ Thus contraction follows either from predictor contraction $\theta_j+\eta<1$, or from a reoptimization factor satisfying $\gamma_{j+1}<1/(\theta_j+\eta)$.

The identity is algebraic. The inequality $\gamma_{j+1}\le1$ is exactly the RH-87 variational bound [\[eq:rh87\]](#eq:rh87){reference-type="eqref" reference="eq:rh87"}: retaining $P_j$ is the predictor, while optimizing the new packet is the corrector.

This factorization explains why an old-packet upper may fail to contract even though the newly optimized tail contracts strongly.

# Ten-channel audit

We use $\eta=1/512$, the clock rank, and the last update ending at $\lceil2M/3\rceil$. The point quotient $\chi_j$ is evaluated directly in 192-bit Arb arithmetic. For the global coefficient, a lifted top singular test vector gives a rigorous lower bound; a lower bound above one proves that the named global-norm sufficient condition cannot certify contraction. Memory tails and reoptimization factors are positive binary64 variational diagnostics.

::: {#tab:audit}
    $\sigma$   point contractions   memory predictors   corrected   worst corrected   global min
  ---------- -------------------- ------------------- ----------- ----------------- ------------
        0.16                  0/2                 2/2         2/2            0.0034         6.82
        0.08                  1/2                 2/2         2/2            0.0133         5.30
        0.04                  2/2                 2/2         2/2            0.0515         2.66
        0.02                  2/2                 2/2         2/2             0.235         3.61
        0.01                  1/2                 1/2         2/2             0.189         9.23

  : Predictor and corrector verdicts. The final column is the smaller rigorous tested-global coefficient before adding $\eta$.
:::

All global coefficients remain well above one. Four point-packet predictors fail, showing that pointwise selective damping is not uniform at the anchors. Only the finest right memory predictor slightly exceeds one; its strong corrector dividend restores contraction.

![The global-norm barrier, mixed point prediction, universal corrected contraction, and the reoptimization factor.](<../../../../../zeta_mvp0/papers/RH-88-predictor-corrector-energy-contraction/figures/predictor_corrector_energy_contraction.pdf>){#fig:audit width="\\textwidth"}

# Boundary and next theorem

The surviving mechanism is predictor plus low-dimensional correction. The next target is an explicit lower bound on the Ky Fan energy recovered by rotating or swapping a small number of old packet directions toward the new residual cross-Gramian. Such a theorem would bound $\gamma_{j+1}$ without a global spectral gap.

RH-88 proves the two factorization identities and rigorously closes the named global-norm sufficient route at the anchors. It does not prove a uniform corrector dividend, all-level packet contraction, Stage A1 or Stage A4, a relative determinant, a self-adjoint Hilbert--Polya operator, a zeta-zero identity, or the Riemann Hypothesis.
