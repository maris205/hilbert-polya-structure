---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-114-psd-rayleigh-directional-tail"
canonical_tex: "zeta_mvp0/papers/RH-114-psd-rayleigh-directional-tail/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-114-psd-rayleigh-directional-tail/main.pdf"
source_sha256: "236287bed9565f91a85a6a1a3a3e00737ca226ec53ee07079a8844199ac1c9a8"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# PSD-Rayleigh Directional Memory Tails A Relative Gramian Bound for Fourth-Mode Support

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-114-psd-rayleigh-directional-tail>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-114-psd-rayleigh-directional-tail/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-114-psd-rayleigh-directional-tail/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-114-psd-rayleigh-directional-tail/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-114-psd-rayleigh-directional-tail/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The right-frame reduction of RH-113 leaves one missing quantity: the tail acting on four recent right singular directions. We prove a positive-tail cross-Gram inequality and turn it into a multiplicative exterior-volume bound. If $T\succeq0$, $\left\lVert T\right\rVert\leq\delta$, $P$ is a packet isometry, $Q$ is a right four-frame, and $R=(I-PP^*)TPQ$, then $$R^*R\preceq\delta Q^*P^*TPQ.$$ More generally, any PSD upper $D\succeq R^*R$ yields a generalized Rayleigh constant $\gamma$ and a four-volume factor $(1-\gamma)_+^4$. The five-scale audit has zero failures; on the fine chain the packet-block bound reduces the worst scalar gamma from $0.00134724$ to $0.000175802$. This is a directional theorem and finite audit, not an all-level physical law.
author:
- Prime Dynamics Theory Program
bibliography:
- references.bib
date: July 2026
title: |
  PSD-Rayleigh Directional Memory Tails\
  A Relative Gramian Bound for Fourth-Mode Support
```

## Markdown 正文

# The directional problem

Let $A$ be a recent finite-memory cross action and $K=A+R$ its full action on a packet. RH-113 showed that a four-column action $Y=AQ$ gives a lower bound for the full fourth exterior norm. A scalar error $\left\lVert R\right\rVert\leq\delta$ leads to a weak-mode penalty because the relative constant is bounded by $\delta/s_4(Y)$. The purpose of this paper is to preserve the Gramian of the tail in the same four-dimensional frame.

We work in a Hilbert space, with $P$ an isometry from packet coordinates into the ambient domain and $Q:\mathbb C^4\to\operatorname{ran}P$ an isometry. Write $\Pi=PP^*$ and let $T\succeq0$ be a discarded memory tail. Its directional cross action is $$R=(I-\Pi)TPQ,
 \qquad Y=(I-\Pi)APQ.$$ All matrix inequalities below are in the usual Loewner order; the exterior volume identities use the standard singular-value calculus [@HornJohnson1991].

# Positive-tail cross-Gram theorem

[\[thm:positive\]]{#thm:positive label="thm:positive"} If $T\succeq0$ and $\left\lVert T\right\rVert\leq\delta$, then $$\label{eq:block}
 R^*R\preceq\delta Q^*P^*TPQ.$$

Since $0\preceq I-\Pi\preceq I$, $$T(I-\Pi)T\preceq T^2\preceq\delta T.$$ Compress this inequality on the left and right by $PQ$ to obtain [\[eq:block\]](#eq:block){reference-type="eqref" reference="eq:block"}. No commutation between $T$ and the packet projection is needed.

The scalar upper $R^*R\preceq\delta^2I$ follows from $\left\lVert R\right\rVert\leq\delta$. Equation [\[eq:block\]](#eq:block){reference-type="eqref" reference="eq:block"} is stronger when the tail has little energy in the current packet directions. It is also compatible with matrix-free action: only the four columns $TPQ$ and the $4\times4$ packet block are required.

# Relative Rayleigh volume theorem

Let $G=Y^*Y$ be positive definite and suppose $D\succeq R^*R$. Define $$\gamma^2=\lambda_{\max}(G^{-1/2}DG^{-1/2}).$$

[\[thm:rayleigh\]]{#thm:rayleigh label="thm:rayleigh"} If $\gamma<1$, then $$\label{eq:rayleigh}
 (Y+R)^*(Y+R)\succeq(1-\gamma)^2G,
 \qquad
 D_4(Y+R)\geq(1-\gamma)^4D_4(Y).$$ For arbitrary $\gamma$, the second lower bound is understood with $(1-\gamma)_+^4$.

The definition of $\gamma$ is equivalent to $R^*R\preceq\gamma^2G$. Therefore $\left\lVert Rx\right\rVert\leq\gamma\left\lVert Yx\right\rVert$ for every $x$. The reverse triangle inequality gives $\left\lVert(Y+R)x\right\rVert\geq(1-\gamma)\left\lVert Yx\right\rVert$ when $\gamma<1$, which is the first Loewner inequality. Determinants are monotone on positive definite $4\times4$ matrices, so taking square roots of determinants gives the second claim.

Under Theorem [\[thm:positive\]](#thm:positive){reference-type="ref" reference="thm:positive"}, use $D=\delta Q^*P^*TPQ$ in Theorem [\[thm:rayleigh\]](#thm:rayleigh){reference-type="ref" reference="thm:rayleigh"}. If $U\geq\left\lVert K\right\rVert$, then the normalized fourth exterior volume obeys $$\frac{\left\lVert\bigwedge^4K\right\rVert_2}{U^4}
 \geq (1-\gamma)_+^4\frac{D_4(Y)}{U^4}.$$

# Sharpness and comparison

The factor is sharp: take $R=-\gamma Y$, so $R^*R=\gamma^2G$ and $D_4(Y+R)=(1-\gamma)^4D_4(Y)$. The scalar specialization has $$\gamma_{\rm scalar}\leq\frac{\delta}{s_4(Y)},
 \qquad D_{\rm scalar}=\delta^2I.$$ The packet-block version replaces the isotropic identity by the tail energy seen by $PQ$. It can be better by orders of magnitude, but it cannot be used unless that PSD block is itself controlled or computed with a validated upper enclosure.

# Five-scale audit

We recompute the RH-110 finite-memory chain at five scales, two channels, three thresholds, and 360 records. At each update we form the positive tail Gramian, the recent top-four frame, and three upper choices: scalar $\delta^2I$, positive packet-block $\delta Q^*P^*TPQ$, and the exact directional residual Gramian. The analytic tail radius is enlarged only by outward floating-point guards; PSD corrections are recorded separately.

There are zero block-dominance and certificate failures. On the 234 fine records, the largest generalized constants are

  upper choice                     minimum $\gamma$         maximum $\gamma$   fine support at $10^{-8}$
  ------------------------ ------------------------ ------------------------ ---------------------------
  scalar $\delta^2I$         $1.2571\times10^{-12}$               0.00134724                          78
  positive packet block       $3.83\times10^{-159}$              0.000175802                          78
  exact directional Gram                          0   6.59362$\times10^{-6}$                          78

  : Fine-chain generalized tail constants. The exact lower endpoint is an audit reference; the packet-block line is the structured theorem route.

The three certificates have the same fine threshold counts: 78, 72, and 55 for thresholds $10^{-8}$, $10^{-6}$, and $10^{-4}$, respectively. This is not a failure of the theorem: the archived thresholds are already crossed by the product-Weyl lower bound. The gain is quantitative slack and a route to future scales where the scalar bound may cease to be usable.

![Left: median generalized tail constants by scale. Right: median normalized lower certificates on the finest threshold.](<../../../../../zeta_mvp0/papers/RH-114-psd-rayleigh-directional-tail/figures/psd_rayleigh_directional_tail.pdf>){width="\\textwidth"}

# Route consequence and boundary

RH-114 turns a vague directional-tail hope into a precise sufficient condition: control one $4\times4$ PSD block and one generalized eigenvalue. The positive-tail proof is unconditional for finite PSD tails. What remains open is an all-level physical bound on that block, compatible with memory depth and the changing right frame. RH-115 will compose the scalar, packet-block, trace-concentration, and capacity certificates and keep the strongest valid lower endpoint.

No all-level exterior law, uniform Stage A, Hilbert--Polya operator, zeta-zero identification, or Riemann Hypothesis conclusion is claimed.
