---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-153-congruence-covariant-reset-transport"
canonical_tex: "zeta_mvp0/papers/RH-153-congruence-covariant-reset-transport/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-153-congruence-covariant-reset-transport/main.pdf"
source_sha256: "6d8b74f1aa5785de2e790239d8771a36f35b11117c6da73389380a114362b3a7"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Congruence-Covariant Reset Transport Exact Tail-Ratio Cancellation and the Independent-Ball Positivity Wall

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-153-congruence-covariant-reset-transport>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-153-congruence-covariant-reset-transport/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-153-congruence-covariant-reset-transport/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-153-congruence-covariant-reset-transport/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-153-congruence-covariant-reset-transport/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  RH-152 proved that all 120 consecutive maps in the reset packet atlas remain invertible, but the worst inverse-overlap upper is $1.11\times10^4$. A matrix-by-matrix perturbation argument would square this factor under an inverse congruence and appears to threaten the outward route.

  We show that this loss is artificial when the reduced Gram and memory tail are transported as one correlated pair. For an invertible overlap $C$, $$(G,D)\longmapsto(C^{-*}GC^{-1},C^{-*}DC^{-1})$$ preserves Loewner dominance and the largest generalized tail ratio exactly. If the singular values of $C$ lie in $[\alpha,\beta]$, the normalized Gram base loses at most the single factor $\alpha/\beta$, and this constant is sharp. We also derive the independent-ball inverse-congruence radius, whose leading amplification is necessarily quadratic in $\alpha^{-1}$.

  The frozen audit combines RH-151 spectral-reset eigenvalue balls with the RH-152 robust overlap lowers. Every correlated transported base is positive; the minimum is $2.2304\times10^{-7}$, all 120 exceed $10^{-8}$, and 113 exceed $10^{-6}$. In contrast, separating the packet, Gram, and overlap balls before inversion certifies positive definiteness on only 68 of 120 transitions. Thus inverse overlap is not a wall for a paired reset object, but independent norm-ball assembly is the wrong information geometry. The next layer must construct a native reset Gram--tail pair before transport.
author:
- Prime Dynamics Theory Program
bibliography:
- references.bib
date: July 2026
title: |
  Congruence-Covariant Reset Transport\
  Exact Tail-Ratio Cancellation and the Independent-Ball Positivity Wall
```

## Markdown 正文

# The apparent inverse-overlap wall

Let $U,V$ be equal-rank orthonormal reset frames and $C=U^*V$. RH-152 gives a positive outward lower for $\sigma_{\min}(C)$ at every frozen transition. Representing target coordinates in the source chart naturally introduces $C^{-1}$. If each matrix is enclosed separately, two-sided transport seems to cost $\|C^{-1}\|^2$ and cumulative products become enormous.

That reasoning ignores the fact that the recent Gram and its memory tail describe the same coordinates. The relevant object is an ordered positive pair $(G,D)$, not either matrix in isolation. Congruence is the natural change of chart for such a pair [@HornJohnson2013].

# Exact covariance of a Gram--tail pair

For $G\succ0$ and $D\succeq0$, write $$\gamma^2(G,D)=\lambda_{\max}(G^{-1/2}DG^{-1/2})
 =\inf\{y\geq0:D\preceq yG\}.$$

[\[thm:covariance\]]{#thm:covariance label="thm:covariance"} Let $C$ be invertible and define $$\Phi_C(G)=C^{-*}GC^{-1},\qquad
 \Phi_C(D)=C^{-*}DC^{-1}.$$ Then, for every $y\geq0$, $$D\preceq yG\quad\Longleftrightarrow\quad
 \Phi_C(D)\preceq y\Phi_C(G).$$ Consequently $\gamma^2(\Phi_C(G),\Phi_C(D))=\gamma^2(G,D)$.

Congruence by an invertible matrix is an order isomorphism on Hermitian matrices. Applying $C^{-*}(\cdot)C^{-1}$ proves the forward implication, and congruence by $C^*$ and $C$ proves the reverse implication. Taking the least admissible $y$ gives the generalized-ratio identity.

Thus no inverse-overlap factor enters the relative tail envelope. This is an exact cancellation, not a perturbative approximation.

# The one-factor normalized-base law

Put $$a(G)=\sqrt{\lambda_{\min}(G)/\lambda_{\max}(G)}.$$

[\[thm:base\]]{#thm:base label="thm:base"} If $0<\alpha\leq\sigma_{\min}(C)$ and $\sigma_{\max}(C)\leq\beta$, then $$a(\Phi_C(G))\geq\frac{\alpha}{\beta}a(G).$$ The coefficient $\alpha/\beta$ is optimal from these four scalar endpoints. For overlaps of orthonormal frames, $\beta\leq1$, so $a(\Phi_C(G))\geq\alpha a(G)$.

For every vector, $$\lambda_{\min}(G)\|C^{-1}x\|^2
 \leq x^*\Phi_C(G)x
 \leq\lambda_{\max}(G)\|C^{-1}x\|^2.$$ Hence $\lambda_{\min}(\Phi_C(G))\geq
\lambda_{\min}(G)/\beta^2$ and $\lambda_{\max}(\Phi_C(G))\leq
\lambda_{\max}(G)/\alpha^2$. Taking the square-root ratio proves the bound. Diagonal $C=\operatorname{diag}(\alpha,\beta)$ and a diagonal $G$ assigning its largest eigenvalue to the $\alpha$ direction and its smallest to the $\beta$ direction attain equality.

Combined with Theorem [\[thm:covariance\]](#thm:covariance){reference-type="ref" reference="thm:covariance"}, a directional support lower of the form $a(G)(1-\sqrt y)_+^4$ loses only the one overlap factor while the tail parameter $y$ is unchanged.

# What independent balls really cost

Let $\widehat C,\widehat H$ be nominal matrices with $$\sigma_{\min}(\widehat C)=\alpha,\quad
 \|C-\widehat C\|\leq\eta<\alpha,\quad
 \|H-\widehat H\|\leq\rho.$$ Set $a=\alpha-\eta$.

[\[prop:radius\]]{#prop:radius label="prop:radius"} The inverse identity gives $$\|C^{-1}-\widehat C^{-1}\|\leq\frac{\eta}{\alpha a}.$$ Moreover, $$\begin{aligned}
 &\|C^{-*}HC^{-1}-\widehat C^{-*}\widehat H\widehat C^{-1}\|\\
 &\quad\leq
 \frac{\rho}{a^2}
 +\|\widehat H\|\frac{\eta}{\alpha a}
 \left(\frac1a+\frac1\alpha\right).\end{aligned}$$ The $a^{-2}$ growth cannot be improved for independent scalar norm balls.

Use $C^{-1}-\widehat C^{-1}=C^{-1}(\widehat C-C)\widehat C^{-1}$, then add and subtract the two mixed congruence terms. Submultiplicativity gives the displayed radius. In one dimension, perturbing $H$ while fixing $C=a$ produces the term $\rho/a^2$, proving the unavoidable order.

The proposition is valid, but it forgets that a native spectral reset ties the frame, reduced Gram, and selected eigenvalue endpoints to one ambient operator. It is therefore a diagnostic fallback rather than the primary transport theorem [@StewartSun1990; @Bhatia1997].

# The 120-transition comparison

At each target snapshot, RH-151 supplies an ambient memory-Gram radius and a spectral-center error. If $\widehat\lambda_r$ and $\widehat\lambda_1$ are the nominal selected endpoints and $R$ is the sum of those two outward errors, then the native reset base obeys $$a(G)\geq
 \sqrt{\frac{(\widehat\lambda_r-R)_+}
 {\widehat\lambda_1+R}}.$$ Multiplying by the RH-152 robust overlap lower implements Theorem [\[thm:base\]](#thm:base){reference-type="ref" reference="thm:base"}. All 120 results are positive. Their minimum is $2.2304\times10^{-7}$, the median is $3.2669\times10^{-4}$, and the counts above $10^{-8},10^{-6},10^{-4}$ are respectively 120, 113, and 74.

For comparison, we polar-align the endpoint frame balls independently, compress the target ambient Gram with a generic frame radius, and then apply Proposition [\[prop:radius\]](#prop:radius){reference-type="ref" reference="prop:radius"}. Only 68 pullback balls exclude singularity; 52 have radius at least their nominal minimum eigenvalue. The maximum radius-to-minimum ratio is about $1.47\times10^{11}$. This does not contradict the positive correlated result: the independent product ball contains combinations of frame and Gram errors that cannot arise from one spectral reset.

![Correlated congruence transport retains all reset bases, whereas independent inverse-congruence balls lose 52 positive-definiteness gates.](<../../../../../zeta_mvp0/papers/RH-153-congruence-covariant-reset-transport/figures/congruence_covariant_reset_transport.pdf>){#fig:audit width="\\textwidth"}

# Consequence and boundary

The conditioning spike from RH-152 is not by itself a fatal wall. The correct invariant is the generalized Gram--tail pair, for which inverse factors cancel exactly in the relative tail. The finite base remains positive after paying one robust overlap factor at every individual transition.

This paper has not yet constructed the reset memory tail on the native spectral packet, propagated one correlated pair through all levels, proved a uniform overlap or base lower, closed the delayed support cocycle, established Stage A, constructed a Hilbert--Polya operator, identified zeta zeros, or proved the Riemann Hypothesis.
