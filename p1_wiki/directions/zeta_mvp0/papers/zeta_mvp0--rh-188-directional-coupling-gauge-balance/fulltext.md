---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-188-directional-coupling-gauge-balance"
canonical_tex: "zeta_mvp0/papers/RH-188-directional-coupling-gauge-balance/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-188-directional-coupling-gauge-balance/main.pdf"
source_sha256: "b5719e27d04e7eba2a77e66bcc77f0ba76adaa5cc0bfd980be5f3afff263ec60"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Directional Coupling and Gauge Balance A Surviving Schur Product Behind the Failed Oblique Maximum-Norm Gate

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-188-directional-coupling-gauge-balance>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-188-directional-coupling-gauge-balance/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-188-directional-coupling-gauge-balance/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-188-directional-coupling-gauge-balance/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-188-directional-coupling-gauge-balance/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-186--187 show that maximum-residual oblique budgets and cross-Gram clipping fail on every physical bi-Krylov window. Those tests combine the two directions too early. A Schur complement instead depends on the product of left and right couplings. This paper isolates its gauge structure.

  Under the scalar packet gauge $V\mapsto\alpha V$, $W\mapsto\alpha^{-1}W$, the right coupling scales by $\alpha$ and the left coupling by $\alpha^{-1}$. Their product is invariant. The maximum of the two is minimized uniquely at $\alpha=\sqrt{b/c}$, where both become $\sqrt{bc}$. Thus scalar balancing cannot improve the directed Schur product $adbc$, but it gives the optimal symmetric representative for numerical work.

  Replaying the 126 RH-185 windows, the absolute coupling product ranges from $0.2486$ to $2.6847\times10^{10}$. Eight windows have $bc<1$; all eight are in the local $\sigma=0.01,L=4$ branch. Twelve local windows have relative coupling product below $0.01$. Hence the failure of the coarse $\chi\max(\epsilon_R,\epsilon_L)$ gate does not by itself kill the sharp directional route.

  The result is intentionally incomplete. A Riesz theorem also requires the packet and complement resolvent factors $a$ and $d$. Neither is supplied here. The next paper constructs the exact oblique Feshbach factorization that defines those quantities.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  Directional Coupling and Gauge Balance\
  A Surviving Schur Product Behind the Failed Oblique Maximum-Norm Gate
```

## Markdown 正文

# Why products matter

For a right/left packet pair $V,W$ with $W^*V=I$, the directed residuals $$\label{eq:residuals}
 C=(I-P)AV,
 \qquad
 B^*=(I-P^*)A^*W,
 \qquad P=VW^*,$$ are the two off-diagonal couplings of the oblique block decomposition. A Schur--Feshbach feedback term has the schematic form $$\label{eq:feedback}
 \Sigma(z)=B(z-D)^{-1}C.$$ A sufficient rank-preservation condition is therefore controlled by $$\label{eq:schur-product}
 a(z)d(z)\left\lVert B\right\rVert\left\lVert C\right\rVert<1,$$ where $a$ bounds the packet resolvent and $d$ the complement resolvent [@GohbergGoldbergKaashoek1990; @WangRH171].

The maximum-norm gate of RH-186 is useful but stronger than [\[eq:schur-product\]](#eq:schur-product){reference-type="eqref" reference="eq:schur-product"}. Before rejecting the route, the two coupling directions should be balanced and their invariant product recorded.

# Scalar packet gauge

Let $b=\left\lVert B\right\rVert$ and $c=\left\lVert C\right\rVert$. For $\alpha>0$, apply $$\label{eq:scalar-gauge}
 V_\alpha=\alpha V,
 \qquad
 W_\alpha=\alpha^{-1}W.$$ Biorthogonality and the oblique projector remain unchanged. The compressed operator is unchanged for a scalar gauge, while $$\label{eq:coupling-scale}
 b_\alpha=\alpha^{-1}b,
 \qquad
 c_\alpha=\alpha c.$$

[\[thm:balance\]]{#thm:balance label="thm:balance"} If $b,c>0$, then $$\label{eq:product-invariant}
 b_\alpha c_\alpha=bc$$ for every $\alpha>0$, and $$\label{eq:minimax}
 \min_{\alpha>0}\max(b_\alpha,c_\alpha)=\sqrt{bc}.$$ The unique minimizer is $$\label{eq:optimal-alpha}
 \alpha_*=\sqrt{b/c},$$ at which $b_{\alpha_*}=c_{\alpha_*}=\sqrt{bc}$.

Equation [\[eq:product-invariant\]](#eq:product-invariant){reference-type="eqref" reference="eq:product-invariant"} follows immediately from [\[eq:coupling-scale\]](#eq:coupling-scale){reference-type="eqref" reference="eq:coupling-scale"}. For any two nonnegative numbers with product $bc$, their maximum is at least their geometric mean $\sqrt{bc}$, with equality exactly when they are equal. Solving $\alpha^{-1}b=\alpha c$ gives [\[eq:optimal-alpha\]](#eq:optimal-alpha){reference-type="eqref" reference="eq:optimal-alpha"}.

If one coupling vanishes, the product is zero and the remaining coupling can be made arbitrarily small by a singular limit of the scalar gauge. In finite numerical work one would retain a bounded gauge, but the Schur feedback is already zero.

The minimax statement has a useful weighted form. It applies when two directions are displayed in different coordinate norms.

[\[prop:weighted-balance\]]{#prop:weighted-balance label="prop:weighted-balance"} For $b,c,\mu,\nu>0$, $$\label{eq:weighted-minimax}
 \min_{\alpha>0}
 \max\!\left(\mu\alpha^{-1}b,\nu\alpha c\right)
 =\sqrt{\mu\nu bc}.$$ The unique minimizer is $$\label{eq:weighted-alpha}
 \alpha_*=\sqrt{\frac{\mu b}{\nu c}}.$$

The product of the two displayed terms is the invariant $\mu\nu bc$, so their maximum is at least its square root. Equality holds exactly when the two terms agree, which gives [\[eq:weighted-alpha\]](#eq:weighted-alpha){reference-type="eqref" reference="eq:weighted-alpha"}.

This weighted form can equalize outward left and right error bars, but it still cannot change their product. It is therefore a preconditioner for validated arithmetic, not an additional source of Schur margin.

# Gauge-invariant Schur condition

[\[cor:feedback\]]{#cor:feedback label="cor:feedback"} For fixed packet and complement resolvent bounds $a,d$, the sufficient Schur product $$\label{eq:invariant-feedback}
 \kappa=adbc$$ is invariant under [\[eq:scalar-gauge\]](#eq:scalar-gauge){reference-type="eqref" reference="eq:scalar-gauge"}. Scalar balancing can improve the largest displayed coupling but cannot turn a failing $\kappa$ into a passing one.

This separates presentation from substance. The balanced representative is best for symmetric floating-point ranges; the product is the proof datum.

# Physical coupling definitions

For each RH-185 record, the absolute couplings are $$\label{eq:physical-bc}
 c=\left\lVert AV-VK\right\rVert,
 \qquad
 b=\left\lVert A^*W-WK^*\right\rVert.$$ Their relative counterparts are $$\label{eq:relative-product}
 \widehat c=\frac c{\left\lVert AV\right\rVert},
 \qquad
 \widehat b=\frac b{\left\lVert A^*W\right\rVert},
 \qquad
 \widehat b\widehat c.$$ The relative product is a scale-normalized diagnostic; the absolute product is the quantity entering a fixed ambient Schur estimate.

# Physical audit

Across all 126 windows:

  quantity                                minimum      median                 maximum
  ------------------------ ---------------------- ----------- -----------------------
  $bc$                                  $0.24862$   $727.445$   $2.6847\times10^{10}$
  $\sqrt{bc}$                           $0.49862$   $26.9711$      $1.6385\times10^5$
  $\widehat b\widehat c$     $5.826\times10^{-4}$    $3.5002$      $4.0232\times10^5$

There are eight windows with $$\label{eq:bc-below-one}
 bc<1.$$ All eight occur at $\sigma=0.01,L=4$. There are twelve local length-four windows with $$\label{eq:relative-small}
 \widehat b\widehat c<0.01,$$ matching the twelve two-sided residual-gate windows from RH-185.

This is a genuine surviving signal. The exact oblique condition number can be hundreds while the product of the two actual coupling residuals is less than one. Therefore the negative maximum-residual result of RH-186 is not a logical no-go for the directed Schur route [@WangRH186].

The eight values below one should not be read as eight shell certificates. They omit both resolvent factors and use nominal floating couplings. Their proper role is triage: they identify a small set of windows for which a validated complement calculation is not ruled out before it starts. The remaining 118 windows already require a resolvent product below $1/(bc)$, which can be extremely small.

# Why the Riesz certificate is still open

The coupling product alone is not enough. On a contour $\Gamma$ around a candidate cycle root, one needs $$\label{eq:full-gate}
 \sup_{z\in\Gamma}
 \left\lVert(z-K)^{-1}\right\rVert
 \left\lVert(z-D)^{-1}\right\rVert
 bc<1.$$ Even the minimum $bc=0.2486$ can fail if the two resolvent factors have product larger than about four. Near a packet root, the packet resolvent is necessarily large on a small contour. The complement factor is completely unknown in the present physical realization.

The next requirement is therefore structural: define the complement block $D$ in a type-correct oblique coordinate system and derive the exact determinant/Feshbach identity. Only then can a contour audit distinguish a real complement obstruction from a crude norm artifact.

# Matrix gauges beyond scalars

An invertible matrix gauge $G$ transforms $V\mapsto VG$, $W\mapsto WG^{-*}$ and $K\mapsto G^{-1}KG$. Such a gauge can redistribute directions nonuniformly. The exact optimization becomes a matrix balancing problem and may improve computable upper bounds. It cannot change the underlying Schur self-energy as an ambient operator. This paper uses the scalar theorem because it is exact, transparent, and sufficient to show that the directional branch has not been eliminated.

More explicitly, in packet/complement coordinates $$\label{eq:block-gauge}
 \begin{pmatrix}K&B\\C&D\end{pmatrix}
 \longmapsto
 \begin{pmatrix}G^{-1}KG&G^{-1}B\\CG&D\end{pmatrix}.$$ Hence $$\label{eq:self-energy-gauge}
 B(z-D)^{-1}C
 \longmapsto
 G^{-1}B(z-D)^{-1}CG.$$ The self-energy spectrum and reduced determinant are gauge invariant even though a product of separate matrix norms need not be. Scalar gauges are special because both norms are multiplied by reciprocal positive scalars, making $bc$ itself invariant. A later matrix-balancing optimization must therefore report the exact self-energy or a rigorously transformed norm bound, not merely a smaller-looking pair of couplings.

# Requirements for the next certificate

For each surviving window a complete finite certificate needs four outward quantities on the same contour:

1.  a packet inverse bound for $zI-K$;

2.  a complement inverse bound for $zI-D$;

3.  an upper bound for the left coupling $B$;

4.  an upper bound for the right coupling $C$.

The gauge used to compute them must be recorded, and the final product must be invariant under any later change of packet coordinates. RH-189 supplies the exact block identity that makes these requirements type-correct.

# Boundary

This paper proves scalar-gauge invariance and the optimal minimax balance, and reports the physical coupling products. It does not provide packet or complement resolvent bounds, a continuous contour certificate, a physical Riesz rank, all-level scale transport, R, Gate A, or a downstream Hilbert--Polya/RH statement.
