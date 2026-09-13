---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-79-intrinsic-determinant-diagonal-transfer"
canonical_tex: "zeta_mvp0/papers/RH-79-intrinsic-determinant-diagonal-transfer/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-79-intrinsic-determinant-diagonal-transfer/main.pdf"
source_sha256: "5a89e7e8ce9fcd5ab5f70009c38d1df159345de4a7b634b80530d20948749680"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Intrinsic Bulk-Square Transfer and the Shrinking-Disk Determinant Gate Diagonal Small-Noise Limits, Trace-Ideal Continuity, and the Fixed-Disk Exponential Barrier

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-79-intrinsic-determinant-diagonal-transfer>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-79-intrinsic-determinant-diagonal-transfer/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-79-intrinsic-determinant-diagonal-transfer/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-79-intrinsic-determinant-diagonal-transfer/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-79-intrinsic-determinant-diagonal-transfer/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-78 showed conditionally that either of two all-level Hardy corridors would close intrinsic identification on every strict mesh schedule $n\sigma^2\to\infty$. This paper determines exactly how far that conclusion propagates toward the two-step Fredholm determinant.

  Let $B^{\rm int}_{n,\sigma}$ be the intrinsic finite bulk and $B_\sigma$ the continuum-anchored bulk. If $$\left\lVert B^{\rm int}_{n,\sigma}-B_\sigma\right\rVert_2\le\varepsilon,
   \qquad \left\lVert B_\sigma\right\rVert_2\le M,$$ then $$\left\lVert(B^{\rm int}_{n,\sigma})^2-B_\sigma^2\right\rVert_1
   \le\delta:=\varepsilon(2M+\varepsilon).$$ For the Fredholm determinants on $|w|\le R$, $$|D_{n,\sigma}(w)-D_\sigma(w)|
   \le R\delta\exp\{1+RM^2+R(M+\varepsilon)^2\}.$$ Under RH-78's conditional polylogarithmic identification and the Gaussian bulk size $M=O(\sigma^{-1/2})$, the square error tends to zero along every strict $n\sigma^2\to\infty$ diagonal. The determinant bound is uniform on shrinking disks $R=O(\sigma)$, where the exponential remains $O(1)$.

  On a fixed disk, however, the same standard estimate contains $\exp(O(R/\sigma))$. It therefore does not transfer the small-noise limit, even though the trace-norm square error vanishes. This is a proof-method barrier, not a theorem of determinant divergence.

  A 256-bit Arb audit uses the RH-78 stress diagonal and the conservative bulk bound $M\le1.55\sigma^{-1/2}$. The trace-norm square upper decreases from $0.5754$ to $0.09180$. On $R=0.01\sigma$, the determinant upper decreases from $2.63\times10^{-3}$ to $2.62\times10^{-5}$. On the fixed disk $R=0.01$, the standard bound bottoms near $1.57\times10^{-2}$ and then worsens to $0.3051$.

  Thus conditional Stage A4 reaches trace-norm squares and shrinking-disk determinants. Entry to Stage A5 on fixed disks requires pole renormalization or a sharper relative determinant argument; additional finite precision is irrelevant to this exponential obstruction. A5, Hilbert--Polya, and the Riemann Hypothesis remain open.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Intrinsic Bulk-Square Transfer and the Shrinking-Disk Determinant Gate\
  Diagonal Small-Noise Limits, Trace-Ideal Continuity, and the Fixed-Disk Exponential Barrier
```

## Markdown 正文

**Keywords:** trace ideal; Fredholm determinant; diagonal limit; intrinsic bulk; pole renormalization; small noise.

**MSC 2020:** 47B10; 47B35; 47A55; 65G20.

# Introduction

At fixed positive noise, RH-45 proved Hilbert--Schmidt bulk convergence, trace-norm convergence of squares, and local uniform convergence of the two-step determinant [@WangTrace2026]. RH-46 then showed that the small-noise determinant germ has a genuine double-pole obstruction and that unrenormalized fixed-disk convergence is not the correct endpoint [@WangDoublePole2026].

RH-78 now supplies a conditional diagonal identification bound [@WangComposition2026]. It is natural to ask whether this alone permits the finite intrinsic determinant to be exchanged with the continuum and small-noise limits. The answer splits cleanly:

1.  bulk squares transfer in trace norm;

2.  determinants transfer on disks shrinking like $\sigma$;

3.  the generic fixed-disk determinant estimate is exponentially nonuniform and cannot open A5.

# Hilbert--Schmidt identification to trace-class squares

The following standard estimate is the bridge from Stage A4 to two-step trace ideals.

[\[thm:square\]]{#thm:square label="thm:square"} Let $B,\widetilde B\in\mathfrak S_2$ satisfy $\left\lVert\widetilde B-B\right\rVert_2\le\varepsilon$ and $\left\lVert B\right\rVert_2\le M$. Then $$\begin{aligned}
 \left\lVert\widetilde B\right\rVert_2&\le M+\varepsilon,\label{eq:size}\\
 \left\lVert\widetilde B^2-B^2\right\rVert_1
 &\le\varepsilon(2M+\varepsilon)=:\delta.
 \label{eq:square-error}\end{aligned}$$

Use $\widetilde B^2-B^2=(\widetilde B-B)\widetilde B+B(\widetilde B-B)$ and $\left\lVert XY\right\rVert_1\le\left\lVert X\right\rVert_2\left\lVert Y\right\rVert_2$.

Under RH-78's conditional corridor theorem, $$\varepsilon_{n,\sigma}
 =O\!\left(n^{-2}\sigma^{-13/4}L(\sigma)\right),
 \label{eq:epsilon}$$ where $L$ is polylogarithmic. The Gaussian bulk has $M_\sigma=O(\sigma^{-1/2})$. Hence $$\delta_{n,\sigma}
 =O\!\left(n^{-2}\sigma^{-15/4}L(\sigma)\right)
 +O(\varepsilon_{n,\sigma}^2).
 \label{eq:delta-clock}$$

[\[prop:diagonal\]]{#prop:diagonal label="prop:diagonal"} If $n\sigma^2\to\infty$, then $\delta_{n,\sigma}\to0$.

Write $n=\sigma^{-2}G(\sigma)$ with $G\to\infty$. The leading term in [\[eq:delta-clock\]](#eq:delta-clock){reference-type="eqref" reference="eq:delta-clock"} is $O(\sigma^{1/4}G^{-2}L)$; every fixed polylogarithm is dominated by $\sigma^{1/4}$.

Thus conditional intrinsic identification is strong enough for even traces and bulk-square trace-class convergence.

# Determinant disks

Define $$D_{n,\sigma}(w)=\det(I-w(B^{\rm int}_{n,\sigma})^2),qquad
 D_\sigma(w)=\det(I-wB_\sigma^2).$$ The standard trace-ideal determinant continuity estimate [@Simon2005] gives:

[\[thm:determinant\]]{#thm:determinant label="thm:determinant"} Under [\[thm:square\]](#thm:square){reference-type="ref" reference="thm:square"}, for every $R\ge0$, $$\sup_{|w|\le R}|D_{n,\sigma}(w)-D_\sigma(w)|
 \le R\delta
 \exp\!\left(1+RM^2+R(M+\varepsilon)^2\right).
 \label{eq:det-bound}$$

Apply $|\det(I+C)-\det(I+D)|\le\left\lVert C-D\right\rVert_1
e^{1+\left\lVert C\right\rVert_1+\left\lVert D\right\rVert_1}$ with $C=-w\widetilde B^2$, $D=-wB^2$, and use $\left\lVert B^2\right\rVert_1\le\left\lVert B\right\rVert_2^2$.

[\[cor:shrinking\]]{#cor:shrinking label="cor:shrinking"} If $R_\sigma\le\rho\sigma$ and $n\sigma^2\to\infty$, then the right side of [\[eq:det-bound\]](#eq:det-bound){reference-type="eqref" reference="eq:det-bound"} tends to zero.

Since $M^2=O(\sigma^{-1})$, the exponential is $O_\rho(1)$. The remaining factor is $O(\sigma\delta)$, which tends to zero by [\[prop:diagonal\]](#prop:diagonal){reference-type="ref" reference="prop:diagonal"}.

For fixed $R>0$, [\[eq:det-bound\]](#eq:det-bound){reference-type="eqref" reference="eq:det-bound"} contains $\exp(O(R/\sigma))$. No power or polylogarithmic decay in $\delta_{n,\sigma}$ controls that exponential on the minimal strict mesh schedule. This does not prove that $D_{n,\sigma}-D_\sigma$ diverges; it proves that generic absolute determinant continuity is the wrong fixed-disk tool.

# Five-anchor Arb audit

The audit uses RH-78's stress diagonal $n=\sigma^{-2}(k+2)$, its conditional identification ball, and $$M_\sigma\le1.55\sigma^{-1/2}.
 \label{eq:bulk-constant}$$ All scalar products, exponentials, and disk bounds are evaluated at 256-bit Arb precision [@Johansson2017].

::: {#tab:audit}
    $\sigma$   $\varepsilon$   square error    $R=0.01\sigma$   $R=0.01$
  ---------- --------------- -------------- ----------------- ----------
        0.16         0.07355         0.5754   $2.63\,10^{-3}$    0.02124
        0.08         0.02867         0.3150   $7.19\,10^{-4}$    0.01566
        0.04         0.01268         0.1966   $2.25\,10^{-4}$    0.01780
        0.02        0.005997         0.1315   $7.51\,10^{-5}$    0.03955
        0.01        0.002961        0.09180   $2.62\,10^{-5}$     0.3051

  : Conditional square and determinant transfer uppers.
:::

The shrinking-disk upper decreases monotonically by two orders of magnitude. The fixed-disk upper first improves and then deteriorates rapidly as the trace-norm exponential takes over.

![Conditional intrinsic error, square trace-norm transfer, shrinking versus fixed determinant disks, and the exponential penalty ratio.](<../../../../../zeta_mvp0/papers/RH-79-intrinsic-determinant-diagonal-transfer/figures/intrinsic_determinant_diagonal_transfer.pdf>){#fig:audit width="98%"}

# Route consequence

The Stage-A output is now sufficient for trace-class bulk squares along the small-noise diagonal. It also matches RH-46's natural shrinking coordinate $w=O(\sigma)$. What it does not supply is a nontrivial fixed-disk limit.

Stage A5 must therefore alter the object before taking the limit. The two remaining candidates are:

1.  divide out the explicit deterministic double-pole factor and prove a pole-renormalized determinant family is locally bounded;

2.  construct a relative determinant whose continuity depends on a renormalized trace norm rather than $\left\lVert B_\sigma^2\right\rVert_1=O(\sigma^{-1})$.

RH-80 tests this entry gate.

This paper is conditional on an all-level RH-78 corridor. It does not close Stage A1, unconditional Stage A4, or Stage A5; construct a Hilbert--Polya operator; prove a $T\log T$ law or prime-power trace formula; identify zeta zeros; or prove the Riemann Hypothesis.

# Conclusion

Intrinsic identification survives squaring and the strict diagonal limit. Determinants also transfer, but only on the shrinking scale naturally selected by the double-pole geometry. The fixed-disk exponential barrier makes the next move unambiguous: renormalize first, then seek a limit.
