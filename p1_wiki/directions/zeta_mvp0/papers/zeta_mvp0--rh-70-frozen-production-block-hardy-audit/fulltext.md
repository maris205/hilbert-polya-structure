---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-70-frozen-production-block-hardy-audit"
canonical_tex: "zeta_mvp0/papers/RH-70-frozen-production-block-hardy-audit/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-70-frozen-production-block-hardy-audit/main.pdf"
source_sha256: "adc0798e4055fa54345354eaf74cb89fc1fb79370b3707b2d0cfddab5965a201"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Outward-Rounded Block Hardy Certificates for Frozen Production Matrices Exact-Dyadic Audit, a Sharp Block Tail Bound, and the Remaining Upstream Gate

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-70-frozen-production-block-hardy-audit>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-70-frozen-production-block-hardy-audit/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-70-frozen-production-block-hardy-audit/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-70-frozen-production-block-hardy-audit/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-70-frozen-production-block-hardy-audit/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The RH-60--RH-69 chain reduced a candidate Stage A1 estimate to a portfolio of finite-prefix and terminal-tail calculations, but the physical rows were still binary64 diagnostics. This paper validates the terminal calculation on the matrices actually produced by that pipeline.

  For finite matrices $A,X,Y$, define the directional Hardy energy $$\mathcal H(A;X,Y)^2=\sum_{n\ge0}\left\lVert YA^nX\right\rVert_{\mathrm F}^2.$$ If $q_M=\left\lVert A^M\right\rVert_{\mathrm F}<1$, we prove the block-power Hardy bound $$\mathcal H(A;X,Y)^2\le
   \sum_{r=0}^{M-1}\left\lVert YA^rX\right\rVert_{\mathrm F}^2
   +\left\lVert Y\right\rVert_{\mathrm F}^2\frac{q_M^2}{1-q_M^2}
    \sum_{r=0}^{M-1}\left\lVert A^rX\right\rVert_{\mathrm F}^2.$$ The estimate is exact for scalar systems, and every stable finite matrix has some admissible block length. We also give an augmented difference bridge that realizes the transfer error between a frozen system and a future upstream-enclosed system as one block-diagonal Hardy problem.

  The production pipeline is audited at $\sigma=0.16,0.08,0.04,0.02,0.01$. Its binary64 matrices are embedded as exact dyadic Arb/Acb inputs, after which every matrix product, Frobenius sum, square root, contraction margin, and division is outward rounded at 128-bit precision. Horizons $M=4,9,16,25,32$ certify all ten left/right channels. The largest certified $\left\lVert A^M\right\rVert_{\mathrm F}$ is below $0.022$, and every full upper is at most $1.009370$ times its certified finite prefix. Every archived binary64 Stein energy lies between the corresponding finite-prefix lower and full upper.

  This creates a precise two-layer verdict: the terminal frozen matrices are green, while the end-to-end pipeline remains amber because folded-Gaussian assembly, spectral deflation, and source/observation transfer occur before the exact-dyadic embedding. Stage A1 is therefore not closed, but its main interval gate has moved upstream. No Stage A4, prime-power trace formula, $T\log T$ counting law, Hilbert--Polya operator, or Riemann Hypothesis conclusion is claimed.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Outward-Rounded Block Hardy Certificates for Frozen Production Matrices\
  Exact-Dyadic Audit, a Sharp Block Tail Bound, and the Remaining Upstream Gate
```

## Markdown 正文

**Keywords:** Hardy energy; block-power tail; interval arithmetic; exact dyadic matrix; Stein equation; validated numerics.

**MSC 2020:** 47A10; 47B65; 65G20; 65F35; 93B28.

# Introduction

The current route does not begin with a putative self-adjoint operator. It begins with a smaller technical obligation: control the directional response of a finite noisy transfer family without confusing an observed binary64 stability pattern with a theorem. RH-60 supplied finite-horizon phase fusion [@WangPhaseTail2026]; RH-61 showed why a naive one-step geometric tail can require very long horizons [@WangHorizonBarrier2026]; RH-64--RH-68 developed weighted, block, covariance, and lower-gate alternatives; RH-69 assembled them into a safe portfolio [@WangWeightedResiduals2026; @WangPortfolio2026].

The remaining question at the terminal layer is concrete. Given the operator, source, and observation arrays emitted by the production code, can the displayed Hardy completion be certified by outward-rounded arithmetic? This paper answers yes for the frozen arrays at all five archived scales.

That answer is deliberately narrower than end-to-end validation. A floating point matrix can be treated exactly after it has been generated because every binary64 number is a dyadic rational. Such a calculation proves a statement about that frozen rational matrix. It does not retroactively enclose the analytic folded-Gaussian operator, the eigenspaces used in spectral deflation, or the transfer factors that produced the array; see [@Higham2002] for the general distinction between floating-point execution and validated enclosure.

## Contributions {#contributions .unnumbered}

1.  We prove a finite-prefix plus block-power upper for matrix-valued Hardy energy and establish scalar sharpness.

2.  We show that block contraction is eventually available for every stable finite matrix, even when one-step Frobenius contraction fails.

3.  We formulate an exact-dyadic interval audit whose successful gates are machine-checkable.

4.  We certify ten production channels and separate the resulting frozen green status from the end-to-end amber status.

5.  We give an augmented difference bridge for the next upstream interval step.

# Directional Hardy energy and the block tail {#sec:block}

Let $A\in\mathbb C^{d\times d}$, $X\in\mathbb C^{d\times s}$, and $Y\in\mathbb C^{t\times d}$. The associated transfer coefficients are $K_n=YA^nX$. Whenever the series converges, define $$\mathcal H(A;X,Y)^2=\sum_{n=0}^{\infty}\left\lVert K_n\right\rVert_{\mathrm F}^2.
 \label{eq:hardy}$$ This is the finite-dimensional matrix-valued $H^2$ energy. It can also be written through a discrete Lyapunov or Stein solution [@Antoulas2005; @LancasterRodman1995], but the block argument below avoids solving an interval Lyapunov equation.

For a positive integer $M$, set $$\begin{aligned}
 F_M^2&=\sum_{r=0}^{M-1}\left\lVert YA^rX\right\rVert_{\mathrm F}^2,\label{eq:finite}\\
 S_M^2&=\sum_{r=0}^{M-1}\left\lVert A^rX\right\rVert_{\mathrm F}^2,\label{eq:source}\\
 q_M&=\left\lVert A^M\right\rVert_{\mathrm F}.\label{eq:q}\end{aligned}$$

[\[thm:block\]]{#thm:block label="thm:block"} If $q_M<1$, then [\[eq:hardy\]](#eq:hardy){reference-type="eqref" reference="eq:hardy"} converges and $$\mathcal H(A;X,Y)^2
 \le F_M^2+\left\lVert Y\right\rVert_{\mathrm F}^2
       \frac{q_M^2}{1-q_M^2}S_M^2.
 \label{eq:block-bound}$$

Write every $n\ge0$ uniquely as $n=kM+r$, with $0\le r<M$. The $k=0$ block is exactly $F_M^2$. For $k\ge1$, submultiplicativity gives $$\begin{aligned}
 \left\lVert YA^{kM+r}X\right\rVert_{\mathrm F}
 &=\left\lVert Y(A^M)^kA^rX\right\rVert_{\mathrm F}\\
 &\le \left\lVert Y\right\rVert_{\mathrm F}\left\lVert(A^M)^k\right\rVert_2\left\lVert A^rX\right\rVert_{\mathrm F}\\
 &\le \left\lVert Y\right\rVert_{\mathrm F}q_M^k\left\lVert A^rX\right\rVert_{\mathrm F}.\end{aligned}$$ Squaring and summing first over $k\ge1$ and then over $r$ yields the geometric factor $q_M^2/(1-q_M^2)$. Moreover, $\rho(A)^M\le\left\lVert A^M\right\rVert_2\le q_M<1$, so the series converges.

[\[prop:sharp\]]{#prop:sharp label="prop:sharp"} For $d=s=t=1$, inequality [\[eq:block-bound\]](#eq:block-bound){reference-type="eqref" reference="eq:block-bound"} is an equality for every $M$ with $|A|<1$.

Write $A=a$, $X=x$, and $Y=y$. The proposed tail is $$|y|^2\frac{|a|^{2M}}{1-|a|^{2M}}
 |x|^2\sum_{r=0}^{M-1}|a|^{2r}
 =|xy|^2\frac{|a|^{2M}}{1-|a|^2},$$ which is exactly the portion of [\[eq:hardy\]](#eq:hardy){reference-type="eqref" reference="eq:hardy"} after the first $M$ terms.

[\[prop:eventual\]]{#prop:eventual label="prop:eventual"} If $\rho(A)<1$, then there exists $M_0$ such that $\left\lVert A^M\right\rVert_{\mathrm F}<1$ for every $M\ge M_0$.

In finite dimension, $A^M\to0$ in every matrix norm whenever $\rho(A)<1$. Hence its Frobenius norm eventually falls below one.

The last proposition explains why a block certificate can succeed when $\left\lVert A\right\rVert_{\mathrm F}>1$. It does not provide a uniform horizon over a changing family; RH-61 and RH-68 give complementary obstructions to such a claim.

# Exact-dyadic interval audit {#sec:interval}

The audit has two phases. First, the existing production routines generate binary64 arrays $(A,X,Y)$. Second, each real and imaginary component is converted with its exact integer ratio, so the initial Arb/Acb balls are point balls containing precisely those dyadic rationals. The second phase uses 128-bit ball arithmetic [@Johansson2017].

For each channel, the code encloses the quantities in [\[eq:finite\]](#eq:finite){reference-type="eqref" reference="eq:finite"}--[\[eq:q\]](#eq:q){reference-type="eqref" reference="eq:q"}, forms $$D_M=1-q_M^2,
 \qquad
 T_M^2=\left\lVert Y\right\rVert_{\mathrm F}^2\frac{q_M^2}{D_M}S_M^2,
 \qquad
 U_M=(F_M^2+T_M^2)^{1/2},
 \label{eq:interval-quantities}$$ and accepts a row only if the lower endpoint of $D_M$ is positive.

[\[thm:interval\]]{#thm:interval label="thm:interval"} Suppose outward-rounded ball operations enclose every matrix product and scalar operation in [\[eq:interval-quantities\]](#eq:interval-quantities){reference-type="eqref" reference="eq:interval-quantities"}. If the resulting ball for $D_M$ has positive lower endpoint, then the upper endpoint of the ball for $U_M$ is a rigorous upper bound for the Hardy energy of the frozen dyadic matrices.

Inclusion isotonicity of ball arithmetic places every exact dyadic matrix product inside its computed Acb matrix. Summing squared complex magnitudes therefore encloses $F_M^2,S_M^2,q_M^2$, and $\left\lVert Y\right\rVert_{\mathrm F}^2$. A positive lower endpoint for $D_M$ validates division by the entire denominator ball. The nonnegative square root is inclusion preserving. The upper endpoint thus bounds the right side of [\[eq:block-bound\]](#eq:block-bound){reference-type="eqref" reference="eq:block-bound"}, which bounds the exact energy by [\[thm:block\]](#thm:block){reference-type="ref" reference="thm:block"}.

The theorem starts after $(A,X,Y)$ have been generated. Hashes of their complex128 byte arrays identify the audited inputs. The theorem does not enclose roundoff or eigenspace sensitivity in the preceding construction.

# Production family {#sec:family}

The five-scale family is inherited from RH-58--RH-60. At fine dimension $n$, a folded-Gaussian row-stochastic matrix is split into coarse and detail channels. The stationary mode is biorthogonally deflated. After division by the fixed Hardy contour radius, the left channel uses the fine bulk operator, while the right channel uses the adjoint coarse bulk operator. The sources and observations are the archived coarse/detail transfer blocks.

The horizons were selected by a binary64 prescreen and then accepted only if the interval run met both gates $$\sup q_M<1,
 \qquad
 \sup\frac{U_M}{F_M}\le1.01.
 \label{eq:gates}$$ No interval result is used to choose a smaller horizon after seeing a failed ball; all displayed horizons are rerunnable constants.

::: {#tab:audit}
    $\sigma$   $n$   $M$   $q_M$ left   $q_M$ right   $U_M/F_M$ left      right
  ---------- ----- ----- ------------ ------------- ---------------- ----------
        0.16    32     4     0.021022      0.019852         1.003567   1.003213
        0.08    64     9     0.015749      0.014310         1.003996   1.003102
        0.04   128    16     0.017083      0.017136         1.009370   1.009116
        0.02   256    25     0.011997      0.011132         1.009237   1.007802
        0.01   512    32     0.008170      0.007917         1.008566   1.007943

  : Outward-rounded frozen-matrix audit. The dimension $n$ is the fine dimension; the right bulk dimension is $n/2$. The last two columns are the certified full-upper/finite-prefix factors.
:::

All ten contraction margins are positive by interval arithmetic, and all ten completion factors are below $1.01$. The largest factor is $1.009369374$ at $\sigma=0.04$ on the left. The most demanding matrices, at $\sigma=0.01$, have certified block norms below $0.008170$ and $0.007917$.

As a diagnostic cross-check, the archived binary64 infinite Stein energy for each channel lies between the lower endpoint of $F_M$ and the upper endpoint of $U_M$. This cross-check is not promoted to an independent exact result: the rigorous statement remains the upper bound from [\[thm:interval\]](#thm:interval){reference-type="ref" reference="thm:interval"}.

![Horizons, certified block contractions, completion excesses, and the two-layer validation ledger. Green applies to the terminal frozen matrices; amber applies to the unvalidated upstream construction and hence to Stage A1 as a whole.](<../../../../../zeta_mvp0/papers/RH-70-frozen-production-block-hardy-audit/figures/frozen_production_block_hardy_audit.pdf>){#fig:audit width="98%"}

# The augmented difference bridge {#sec:bridge}

The next step must compare the frozen arrays with arrays enclosed directly from the analytic construction. This comparison can use the same block certificate rather than a new perturbation formalism.

Let $(A,X,Y)$ and $(\widetilde A,\widetilde X,\widetilde Y)$ have compatible input/output sizes and equal state dimension. Define $$\mathbb A=\begin{pmatrix}A&0\\0&\widetilde A\end{pmatrix},
 \qquad
 \mathbb X=\begin{pmatrix}X\\\widetilde X\end{pmatrix},
 \qquad
 \mathbb Y=\begin{pmatrix}Y&-\widetilde Y\end{pmatrix}.
 \label{eq:augmented}$$

[\[prop:bridge\]]{#prop:bridge label="prop:bridge"} For every $m\ge0$, $$\mathbb Y\mathbb A^m\mathbb X
 =YA^mX-\widetilde Y\widetilde A^m\widetilde X.
 \label{eq:difference}$$ Consequently, $$\mathcal H(\mathbb A;\mathbb X,\mathbb Y)^2
 =\sum_{m\ge0}
 \left\lVert YA^mX-\widetilde Y\widetilde A^m\widetilde X\right\rVert_{\mathrm F}^2.
 \label{eq:difference-energy}$$ If this difference energy is at most $\delta^2$, then $$\mathcal H(\widetilde A;\widetilde X,\widetilde Y)
 \le \mathcal H(A;X,Y)+\delta.
 \label{eq:triangle}$$

Powers of a block-diagonal matrix remain block diagonal, giving [\[eq:difference\]](#eq:difference){reference-type="eqref" reference="eq:difference"}. Summation gives [\[eq:difference-energy\]](#eq:difference-energy){reference-type="eqref" reference="eq:difference-energy"}. Finally, the matrix-valued coefficient sequences form a Hilbert space under the $\ell^2$ Frobenius norm, so [\[eq:triangle\]](#eq:triangle){reference-type="eqref" reference="eq:triangle"} is the triangle inequality.

Thus an interval enclosure of the upstream construction can be connected to the frozen green certificate by one additional block audit. This is useful only if the true matrices are first proved to belong to the proposed balls; the present paper does not supply that enclosure.

# Validation ledger and route consequence {#sec:ledger}

L0.38cL0.40 Layer & Status & Meaning\
Block-power Hardy theorem & green & Exact finite-dimensional inequality\
Frozen exact-dyadic Acb execution & green & All ten audited arrays pass\
Folded-Gaussian matrix assembly & amber & Generated in binary64 before embedding\
Spectral deflation and biorthogonal bases & amber & No eigenspace interval enclosure\
Source/observation transfer & amber & No end-to-end interval propagation\
Uniform $\sigma\downarrow0$ Stage A1 estimate & amber & Five scales do not prove an asymptotic law\

The result removes one plausible failure mode: outward rounding does not destroy the terminal block contraction or the one-percent completion budget on any archived scale. It also localizes the next task. Repeating more precision on the same frozen arrays cannot turn the end-to-end row green; the missing information is upstream inclusion, not terminal arithmetic.

The correct next target is therefore a validated construction of the folded-Gaussian matrices and their stationary deflation, followed by the augmented difference bridge. If that bridge remains uniformly controlled, the terminal portfolio can be reused. If eigenspace conditioning destroys the enclosure, the failure will be an informative obstruction at a precisely named layer.

# Limitations and nonclaims

The finite audit does not prove a uniform small-noise bound, and hence does not close Stage A1. It does not establish the later Stage A4 arithmetic identification, a prime-power trace formula, a $T\log T$ eigenvalue counting law, self-adjointness, or a Hilbert--Polya realization. In particular, it does not prove the Riemann Hypothesis. The result is a validated terminal component and a sharper map of the remaining route.

# Conclusion

A simple block decomposition turns a stable transfer problem into a finite prefix plus a geometric block tail. The bound is scalar-sharp, eventually available for every stable finite matrix, and well suited to exact-dyadic ball arithmetic. On the five-scale production family, all ten terminal channels are frozen green with less than one percent certified completion excess. The end-to-end verdict remains amber, but the uncertainty is now concentrated in folded-Gaussian assembly, spectral deflation, and transfer construction. The augmented difference bridge gives a direct mechanism for testing that next layer.
