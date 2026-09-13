---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-75-log-square-block-contraction-law"
canonical_tex: "zeta_mvp0/papers/RH-75-log-square-block-contraction-law/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-75-log-square-block-contraction-law/main.pdf"
source_sha256: "720eb57701a06a3afd9db28798416911bca2dfc6383b580d76c9c1931883481a"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Log-Square Horizons and the Square-Root Block-Contraction Law A Sufficient Dyadic Criterion for Polylogarithmic Directional Hardy Energy

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-75-log-square-block-contraction-law>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-75-log-square-block-contraction-law/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-75-log-square-block-contraction-law/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-75-log-square-block-contraction-law/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-75-log-square-block-contraction-law/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-74 closed the folded-Gaussian production chain at five fixed noise scales. The remaining Stage A1 problem is no longer finite-scale validation but a uniform theorem over the small-noise dyadic family. This paper isolates a sharp sufficient scaling law for that theorem.

  Let $\sigma_k=\sigma_0 2^{-k}$ and let $(A_k,X_k,Y_k)$ be a directional bulk triple. Suppose there are block horizons $M_k\le(k+a)^2$ such that $$\left\lVert A_k^{M_k}\right\rVert_2\le C_q\sqrt{\sigma_k},\qquad
   \sigma_k\left\lVert Y_k\right\rVert_{\mathrm F}^2\le C_y,$$ and suppose the one-block source energy and finite transfer prefix obey $$\sum_{r<M_k}\left\lVert A_k^rX_k\right\rVert_{\mathrm F}^2
   \le C_s(k+a)^s,qquad
   \sum_{r<M_k}\left\lVert Y_kA_k^rX_k\right\rVert_{\mathrm F}^2
   \le C_f(k+a)^f.$$ Then the infinite block tail satisfies $$T_k^2\le
   \frac{C_yC_q^2C_s}{1-C_q^2\sigma_0}(k+a)^s,$$ and the full Hardy energy squared is $O((k+a)^{\max\{s,f\}})$. Thus a log-square growing horizon is fully compatible with the required polylogarithmic Stage A1 input. The $\sqrt{\sigma_k}$ factor is the exact scale that cancels the $\left\lVert Y_k\right\rVert_{\mathrm F}^2=O(\sigma_k^{-1})$ mesh growth.

  A 256-bit Arb audit combines the analytic-upstream block contractions of RH-74 with RH-70's source, observation, prefix, and tail balls. At the five levels $k=0,\dots,4$, all ten channels satisfy common constants $$a=2,quad C_q=0.086,quad C_y=2.561,quad C_s=3.1,quad
   s=0,quad C_f=0.552,quad f=1.$$ The common tail envelope is $0.058788$, while the largest certified tail is $0.049421$.

  This identifies the correct all-level target but does not prove it beyond the five anchors. The next open mechanism is phase compression or effective-rank decay sufficient to imply the square-root block law. Stage A1, unconditional Stage A4, Hilbert--Polya, and the Riemann Hypothesis remain open.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Log-Square Horizons and the Square-Root Block-Contraction Law\
  A Sufficient Dyadic Criterion for Polylogarithmic Directional Hardy Energy
```

## Markdown 正文

**Keywords:** block contraction; Hardy energy; dyadic family; small noise; logarithmic horizon; interval arithmetic.

**MSC 2020:** 47A10; 47B35; 65G20; 93B28.

# Introduction

The earlier directional-Hardy program deliberately separated finite matrix identities from small-noise family statements. RH-61 showed that a worst-case one-step geometric envelope may require a power-law horizon when the norm gap closes [@WangHorizon2026]. RH-68 then proved that stability, spectral radius, and even a perfectly conditioned Lyapunov metric cannot force a universal fixed Krylov depth [@WangBarrier2026]. These are genuine barriers to fixed-depth arguments, not barriers to a controlled growing depth.

RH-70 found production block horizons $$4,9,16,25,32$$ at dyadic noise scales $0.16,0.08,0.04,0.02,0.01$ and certified the frozen tails [@WangFrozen2026]. RH-74 transported those contractions to the analytic upstream triples and closed the complete finite-scale bridge [@WangBridge2026]. The horizon list suggests the log-square schedule $(k+2)^2$, but a schedule alone is not enough: the observation Frobenius norm grows with dimension.

The decisive empirical quantity is instead $$\frac{\left\lVert A_k^{M_k}\right\rVert}{\sqrt{\sigma_k}}.
 \label{eq:ratio}$$ It remains bounded by $0.086$ in every validated channel. This paper explains why [\[eq:ratio\]](#eq:ratio){reference-type="eqref" reference="eq:ratio"}, rather than a fixed contraction constant, is the natural uniform target.

# Dyadic block setting

Let $$\sigma_k=\sigma_0 2^{-k},\qquad k\ge0,$$ and consider finite directional triples $(A_k,X_k,Y_k)$. Define $$\begin{aligned}
 S_k(M)&=\sum_{r=0}^{M-1}\left\lVert A_k^rX_k\right\rVert_{\mathrm F}^2,
 \label{eq:source-block}\\
 F_k(M)&=\sum_{r=0}^{M-1}\left\lVert Y_kA_k^rX_k\right\rVert_{\mathrm F}^2,
 \label{eq:finite-block}\\
 H_k^2&=\sum_{r\ge0}\left\lVert Y_kA_k^rX_k\right\rVert_{\mathrm F}^2.
 \label{eq:hardy}\end{aligned}$$ The block-power theorem gives, whenever $q_k=\left\lVert A_k^M\right\rVert_{\mathrm F}<1$, $$H_k^2\le F_k(M)
 +\left\lVert Y_k\right\rVert_{\mathrm F}^2\frac{q_k^2}{1-q_k^2}S_k(M).
 \label{eq:block-tail}$$

For the mesh-locked production family, the fine dimension obeys $n_k\sigma_k=5.12$ and the observation rank is proportional to $n_k$. Consequently $\left\lVert Y_k\right\rVert_{\mathrm F}^2=O(\sigma_k^{-1})$. A merely uniform $q_k<q<1$ would leave a power divergence in [\[eq:block-tail\]](#eq:block-tail){reference-type="eqref" reference="eq:block-tail"}. The block contraction must improve with the mesh.

# The square-root block law

[\[thm:criterion\]]{#thm:criterion label="thm:criterion"} Fix constants $a>0$, $C_q,C_y,C_s,C_f\ge0$ and exponents $s,f\ge0$. Suppose for every $k\ge0$ there is an integer $M_k$ such that $$\begin{aligned}
 M_k&\le(k+a)^2,
 \label{eq:horizon-law}\\
 q_k:=\left\lVert A_k^{M_k}\right\rVert_{\mathrm F}&\le C_q\sqrt{\sigma_k},
 \label{eq:sqrt-law}\\
 \sigma_k\left\lVert Y_k\right\rVert_{\mathrm F}^2&\le C_y,
 \label{eq:observation-law}\\
 S_k(M_k)&\le C_s(k+a)^s,
 \label{eq:source-law}\\
 F_k(M_k)&\le C_f(k+a)^f.
 \label{eq:finite-law}\end{aligned}$$ If $C_q^2\sigma_0<1$, then $$H_k^2\le C_f(k+a)^f
 +\frac{C_yC_q^2C_s}{1-C_q^2\sigma_0}(k+a)^s.
 \label{eq:uniform-hardy}$$ In particular, $H_k=O((k+a)^{\max\{s,f\}/2})$, equivalently a polylogarithmic bound in $1/\sigma_k$.

Insert [\[eq:sqrt-law\]](#eq:sqrt-law){reference-type="eqref" reference="eq:sqrt-law"}--[\[eq:finite-law\]](#eq:finite-law){reference-type="eqref" reference="eq:finite-law"} into [\[eq:block-tail\]](#eq:block-tail){reference-type="eqref" reference="eq:block-tail"}. Since $\sigma_k\le\sigma_0$, $$\frac{\left\lVert Y_k\right\rVert_{\mathrm F}^2q_k^2}{1-q_k^2}
 \le\frac{(C_y/\sigma_k)C_q^2\sigma_k}
 {1-C_q^2\sigma_0}.$$ Multiplication by [\[eq:source-law\]](#eq:source-law){reference-type="eqref" reference="eq:source-law"} proves [\[eq:uniform-hardy\]](#eq:uniform-hardy){reference-type="eqref" reference="eq:uniform-hardy"}. Finally $k=\log_2(\sigma_0/\sigma_k)$.

If $q_k=O(\sigma_k^\theta)$ while $\left\lVert Y_k\right\rVert_{\mathrm F}^2=O(\sigma_k^{-1})$, the raw tail prefactor scales as $\sigma_k^{2\theta-1}$. Thus $\theta=1/2$ is the threshold between a power loss and a bounded prefactor. Additional source growth may still be polylogarithmic.

The theorem permits $M_k=O(k^2)=O(\log^2(1/\sigma_k))$. It is therefore consistent with both RH-61's geometric-horizon warning and RH-68's exact fixed-depth no-go theorem.

# Five-anchor Arb certificate

The audit reads the exact-dyadic RH-70 balls and the analytic true-block balls from RH-74. Every derived ratio and common envelope is recomputed at 256-bit Arb precision [@Johansson2017].

::: {#tab:q}
    $k$   $\sigma_k$   $M_k$   $(k+2)^2$   $\max_s q_{k,s}/\sqrt{\sigma_k}$
  ----- ------------ ------- ----------- ----------------------------------
      0         0.16       4           4                           0.052554
      1         0.08       9           9                           0.055679
      2         0.04      16          16                           0.085680
      3         0.02      25          25                           0.084832
      4         0.01      32          36                           0.081695

  : Selected horizon and largest left/right normalized block contraction at each dyadic level.
:::

The common constants are $$a=2,quad C_q=0.086,quad C_y=2.561,quad C_s=3.1,quad
 s=0,quad C_f=0.552,quad f=1.
 \label{eq:constants}$$ For these values the theorem gives the level-independent tail envelope $$\frac{C_yC_q^2C_s}{1-C_q^2\sigma_0}
 <0.058788.
 \label{eq:tail-envelope}$$

::: {#tab:inputs}
    $\sigma$   $\sigma\left\lVert Y\right\rVert_{\mathrm F}^2$    $S_k$   $F_k/(k+2)$   actual tail
  ---------- ------------------------------------------------- -------- ------------- -------------
        0.16                                            2.5600   1.1565        0.5027      0.006471
        0.08                                            2.5600   1.5997        0.5337      0.010823
        0.04                                            2.5600   2.2047        0.5510      0.040363
        0.02                                            2.5600   2.6711        0.5340      0.041824
        0.01                                            2.5600   3.0993        0.5165      0.049421

  : Largest channel values entering the common envelope.
:::

All entries remain below [\[eq:constants\]](#eq:constants){reference-type="eqref" reference="eq:constants"}; every actual tail remains below [\[eq:tail-envelope\]](#eq:tail-envelope){reference-type="eqref" reference="eq:tail-envelope"}. The resulting conditional all-level estimate is $$H_k^2\le0.552(k+2)+0.058788,
 \qquad H_k=O(\sqrt{k}).$$

![The log-square schedule, square-root contraction ratio, mesh-growth cancellation inputs, and common tail envelope.](<../../../../../zeta_mvp0/papers/RH-75-log-square-block-contraction-law/figures/log_square_block_contraction.pdf>){#fig:audit width="98%"}

# What remains to prove

The theorem converts the vague phrase "uniform horizon control" into four specific all-level inequalities: [\[eq:sqrt-law\]](#eq:sqrt-law){reference-type="eqref" reference="eq:sqrt-law"}--[\[eq:finite-law\]](#eq:finite-law){reference-type="eqref" reference="eq:finite-law"}. The five interval anchors show that these inequalities are compatible with the physical production family and have nontrivial margin. They do not establish an induction in $k$ or a continuum estimate.

The next plausible mechanisms are:

1.  phase support compressed to arcs whose width shrinks along the dyadic family, giving polynomial approximation at depth $O(k^2)$;

2.  weighted effective-rank decay, allowing a small exceptional phase tail;

3.  a direct strong--weak block estimate for the noisy transfer operator.

RH-76 addresses the first mechanism. If phase compression fails, RH-77 will test whether effective-rank decay can replace it.

No all-dyadic law is proved here, so uniform Stage A1 and unconditional Stage A4 remain open. This paper does not construct a renormalized determinant, self-adjoint Hilbert--Polya operator, $T\log T$ counting law, prime-power trace formula, zeta-zero identity, or proof of the Riemann Hypothesis.

# Conclusion

A universal fixed horizon is neither necessary nor expected. The correct target is a log-square horizon paired with a square-root-in-noise block contraction. That factor precisely neutralizes the observation's mesh growth and leaves a polylogarithmic Hardy bound. Five validated levels satisfy a single conservative constant ledger. The route remains open, but its next mathematical obligation is now explicit.
