---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-80-moving-cloud-relative-determinant"
canonical_tex: "zeta_mvp0/papers/RH-80-moving-cloud-relative-determinant/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-80-moving-cloud-relative-determinant/main.pdf"
source_sha256: "6851e71481dc6ac3e67a1209a0de4b56ee19081cf408f698878f1e1ddf01e45d"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Moving-Cloud Renormalization and the Relative Determinant Gate Why Fixed Double-Pole Cancellation Cannot Cross the Small-Noise Circle

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-80-moving-cloud-relative-determinant>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-80-moving-cloud-relative-determinant/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-80-moving-cloud-relative-determinant/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-80-moving-cloud-relative-determinant/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-80-moving-cloud-relative-determinant/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The intrinsic two-step program has reached trace-norm square transfer and Fredholm determinants on shrinking disks, but its generic absolute continuity estimate is nonuniform on fixed disks. Independently, the deterministic coefficient germ has the exact double pole $$\widehat F_0(w)=\frac{H(w)}{(1-w/\lambda)^2},
   \qquad \lambda=1.678573510428322\ldots .$$ This paper decides which pole renormalization can plausibly cross that circle.

  For the exact finite cloud $C_N(w)=\Pi_N(w/\lambda)^2$, the apparently natural fixed cancellation has the identity $$(1-w/\lambda)^2C_N(w)
   =\bigl(1-(w/\lambda)^{N+1}\bigr)^2.$$ It converges uniformly to one on every strict interior disk, but diverges at every fixed point $|w|>\lambda$. Thus multiplication by the limiting scalar pole factor is not a fixed-disk renormalization, even in the canonical model.

  The positive replacement is an exact moving-cloud quotient. If a finite-rank reducing projection isolates the noisy cloud of $T_\sigma=B_\sigma^2$, then the Fredholm determinant factors exactly as $D_\sigma=C_\sigma R_\sigma$. A uniform trace-norm bound on the complementary block makes the residual determinants a normal family on every fixed disk; trace-norm convergence gives an explicit locally uniform determinant bound. A coefficient deconvolution lemma identifies any such limit with the deterministic numerator $H$.

  A 256-bit Arb audit replays the archived RH-15 cloud coordinates. At $\sigma=10^{-4}$ the selected degree is seven, the centered two-step radius is $1.8751435740$, and the observed zero-radius band is $[1.7449450709,1.9816784182]$. The recentered five-point edge profile has mean error at most $0.03633$ and maximum error at most $0.11590$. This supports the moving factor geometrically but does not construct its Riesz projection or bound the complement. Stage A5 remains open with a sharper, operator-level gate; no Hilbert--Polya or Riemann-hypothesis conclusion is made.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Moving-Cloud Renormalization and the Relative Determinant Gate\
  Why Fixed Double-Pole Cancellation Cannot Cross the Small-Noise Circle
```

## Markdown 正文

**Keywords:** Fredholm determinant; spectral cloud; pole renormalization; trace ideal; normal family; small noise.

**MSC 2020:** 47B10; 47B35; 47A55; 30D45; 65G20.

# The fixed-disk fork

RH-46 proved that the deterministic symmetric two-step germ has a genuine double pole at $w=\lambda$ and that the unrenormalized positive-noise entire determinants cannot form a normal family on a disk crossing that point [@WangDoublePole2026]. RH-79 subsequently transferred conditional intrinsic operator control to trace-norm squares and shrinking-disk determinants, while exposing the generic fixed-disk factor $\exp(O(R/\sigma))$ [@WangDiagonalTransfer2026].

There are therefore two superficially similar operations:

1.  multiply by the fixed deterministic factor $(1-w/\lambda)^2$;

2.  divide by the finite spectral polynomial carried by the actual noisy cloud.

The first operation cancels the limiting meromorphic pole germ. The second removes the finite-dimensional mechanism that resolves that pole at positive noise. The distinction is decisive on a disk crossing $|w|=\lambda$.

# Exact failure of fixed scalar cancellation

Set $$\Pi_N(q)=1+q+\cdots+q^N,
 \qquad C_N(w)=\Pi_N(w/\lambda)^2.$$ This is the exact squared geometric cloud factor from RH-46.

[\[thm:fixed-failure\]]{#thm:fixed-failure label="thm:fixed-failure"} For $q=w/\lambda$, $$(1-q)^2C_N(w)=(1-q^{N+1})^2.
 \label{eq:exact-cancellation}$$ Consequently, for every $0\le r<1$, $$\sup_{|q|\le r}
 \left|(1-q)^2C_N(\lambda q)-1\right|
 \le 2r^{N+1}+r^{2N+2}.
 \label{eq:interior-bound}$$ At every fixed $q_0$ with $|q_0|>1$, $$\left|(1-q_0)^2C_N(\lambda q_0)\right|
 \ge \bigl(|q_0|^{N+1}-1\bigr)^2\longrightarrow\infty.
 \label{eq:exterior-growth}$$ Hence the fixed-cancelled canonical family is not locally bounded on any disk $|w|<R$ with $R>\lambda$.

The geometric identity $(1-q)\Pi_N(q)=1-q^{N+1}$ gives [\[eq:exact-cancellation\]](#eq:exact-cancellation){reference-type="eqref" reference="eq:exact-cancellation"}. Subtracting one and applying the triangle inequality proves [\[eq:interior-bound\]](#eq:interior-bound){reference-type="eqref" reference="eq:interior-bound"}. The reverse triangle inequality gives [\[eq:exterior-growth\]](#eq:exterior-growth){reference-type="eqref" reference="eq:exterior-growth"}. Every disk with $R>\lambda$ contains a real point $q_0\in(1,R/\lambda)$, so pointwise unboundedness rules out local boundedness.

The theorem is stronger than a failure of one estimate: the fixed factor fails in the exact model that generated the double pole. At degree $N=64$, the certified interior error is at most $1.01\times10^{-6}$ on $|q|\le0.8$, while at the nearby exterior point $q=1.05$ the fixed-cancelled magnitude is at least $5.2166\times10^2$. The circle, not arithmetic precision, separates the two regimes.

# The exact moving-cloud quotient

Let $T_\sigma\in\mathcal S_1(\mathcal H_\sigma)$ denote a two-step trace-class operator. A bounded finite-rank projection $P_\sigma$ is called a reducing cloud projection when $P_\sigma T_\sigma=T_\sigma P_\sigma$. Put $Q_\sigma=I-P_\sigma$ and use the invariant direct sum $\mathcal H_\sigma=\operatorname{ran}P_\sigma\oplus\operatorname{ran}Q_\sigma$.

[\[thm:relative\]]{#thm:relative label="thm:relative"} For every reducing cloud projection, $$D_\sigma(w):=\det(I-wT_\sigma)
 =C_\sigma(w)R_\sigma(w),
 \label{eq:block-factor}$$ where $$C_\sigma(w)=\det_{\operatorname{ran}P_\sigma}
  (I-wT_\sigma|_{\operatorname{ran}P_\sigma}),
 \qquad
 R_\sigma(w)=\det_{\operatorname{ran}Q_\sigma}
  (I-wT_\sigma|_{\operatorname{ran}Q_\sigma}).$$ Both factors are entire and the quotient $D_\sigma/C_\sigma$ extends through all cloud zeros as the entire function $R_\sigma$.

If the residual blocks, transported to a common Hilbert space, satisfy $$\sup_\sigma\left\lVert S_\sigma\right\rVert_1\le K,
 \label{eq:uniform-complement}$$ then for every $R>0$, $$\sup_{|w|\le R}|R_\sigma(w)|\le e^{RK}.
 \label{eq:normal-bound}$$ Thus the residual family is normal on $\mathbb C$. If additionally $\left\lVert S_\sigma-S_0\right\rVert_1\le\varepsilon_\sigma\to0$, then $$\sup_{|w|\le R}|R_\sigma(w)-R_0(w)|
 \le R\varepsilon_\sigma
 e^{1+R\left\lVert S_\sigma\right\rVert_1+R\left\lVert S_0\right\rVert_1}.
 \label{eq:relative-continuity}$$

Commutation makes $T_\sigma$ block diagonal on the invariant direct sum, and the Fredholm determinant is multiplicative across trace-class direct sums. The standard inequalities $|\det(I+A)|\le e^{\left\lVert A\right\rVert_1}$ and $$|\det(I+A)-\det(I+B)|
 \le\left\lVert A-B\right\rVert_1e^{1+\left\lVert A\right\rVert_1+\left\lVert B\right\rVert_1}$$ give [\[eq:normal-bound\]](#eq:normal-bound){reference-type="eqref" reference="eq:normal-bound"} and [\[eq:relative-continuity\]](#eq:relative-continuity){reference-type="eqref" reference="eq:relative-continuity"} [@Simon2005].

The full trace norm of $T_\sigma=B_\sigma^2$ may grow like $\sigma^{-1}$, which caused the RH-79 absolute determinant barrier. The criterion [\[eq:uniform-complement\]](#eq:uniform-complement){reference-type="eqref" reference="eq:uniform-complement"} asks whether that growth is confined to the extracted finite cloud. If so, the exponential contains $RK$ rather than $O(R/\sigma)$.

# Identification of the residual limit

Normality alone gives subsequences. The coefficient bridge identifies their only possible limit.

[\[prop:deconvolution\]]{#prop:deconvolution label="prop:deconvolution"} Let $D_j=C_jR_j$ be germs at zero with $C_j(0)=1$. Suppose the Taylor coefficients of $D_j$ and $C_j$ converge coefficientwise to those of $D_0=C_0R_0$, where $C_0(0)=1$. Then every Taylor coefficient of $R_j$ converges to the corresponding coefficient of $R_0$.

If the $R_j$ are locally bounded on a connected domain containing zero, then $R_j\to R_0$ locally uniformly there whenever $R_0$ has a holomorphic continuation to that domain.

Writing $d_{j,m}=\sum_{k=0}^m c_{j,k}r_{j,m-k}$ and using $c_{j,0}=1$ determines $r_{j,m}$ recursively from lower coefficients. Induction proves coefficient convergence. Local boundedness gives subsequential compactness by Montel's theorem; every subsequential limit has the same derivatives at zero and therefore equals $R_0$ by the identity theorem [@Conway1978]. Uniqueness upgrades subsequential convergence to full convergence.

For the ideal cloud, the coefficients of $C_N$ converge to those of $(1-w/\lambda)^{-2}$. Together with the RH-46 coefficient bridge, [\[prop:deconvolution\]](#prop:deconvolution){reference-type="ref" reference="prop:deconvolution"} identifies a normal relative limit with the holomorphic numerator $H$. For the actual noisy dynamics, however, one must still prove both the cloud-factor coefficient bridge and [\[eq:uniform-complement\]](#eq:uniform-complement){reference-type="eqref" reference="eq:uniform-complement"}.

# Validated replay of the archived cloud

The numerical audit reads the decimal cloud coordinates archived by RH-15 [@WangBulkScattering2026]. Arb at 256-bit precision propagates those decimals through radial centering, the two-step cloud product, and the finite geometric edge profile. This validates the replay arithmetic, not the upstream floating eigensolver.

::: {#tab:cloud}
                $\sigma$   $N$    center   mismatch      zero-radius band   mean error
  ---------------------- ----- --------- ---------- --------------------- ------------
               $10^{-2}$     3   2.70658    0.61243   \[2.19694,3.61314\]      0.00855
    $2\!\times\!10^{-3}$     4   2.00651    0.19537   \[1.84466,2.16455\]      0.01399
    $5\!\times\!10^{-4}$     5   1.99166    0.18652   \[1.78723,2.25347\]      0.04079
    $2\!\times\!10^{-4}$     6   1.90530    0.13507   \[1.75548,2.06217\]      0.03644
               $10^{-4}$     7   1.87515    0.11711   \[1.74495,1.98168\]      0.03633

  : Selected rows from the seven-level cloud audit. Mismatch is relative to $\lambda$; mean error is over $s=-1,-1/2,0,1/2,1$. Bounds are rounded outward from the archived Arb certificate.
:::

The center moves substantially toward $\lambda$, and the finest recentered profile remains close to the exact finite-section shape. Yet degree seven is far too small to infer asymptotic cloud identification, the center is still $11.71\%$ high, and no complement determinant is contained in the archived data. The evidence selects the moving-factor route without closing it.

![The RH-80 fork. Fixed cancellation converges strictly inside the pole circle (a) and grows outside it (b). The archived noisy zero band moves toward the deterministic pole (c), while recentered finite-section agreement remains a floating-cloud diagnostic (d).](<../../../../../zeta_mvp0/papers/RH-80-moving-cloud-relative-determinant/figures/moving_cloud_relative_determinant.pdf>){#fig:route width="\\textwidth"}

# Route consequence and theorem boundary

RH-80 eliminates a tempting but incorrect fixed-disk shortcut. Multiplying by $(1-w/\lambda)^2$ only recovers the deterministic numerator on strict interior disks. Crossing the pole circle requires division by the actual finite spectral cloud, followed by a uniform theorem for its complementary block.

The next strict gate is therefore:

1.  construct a moving Riesz projection whose finite determinant is the actual cloud polynomial;

2.  prove that the complementary two-step block is uniformly trace class, or prove a sharper relative determinant bound with the same normal-family consequence;

3.  establish the cloud coefficient bridge so that the residual limit is identified with $H$.

The exact factorization and its sufficient convergence theorem are unconditional functional analysis. Their application to the present noisy dynamical family is conditional on the three gates above. Stage A5 is not closed. Nothing here constructs a self-adjoint Hilbert--Polya operator, proves a $T\log T$ law or prime-power trace formula, identifies zeta zeros, or proves the Riemann Hypothesis.
