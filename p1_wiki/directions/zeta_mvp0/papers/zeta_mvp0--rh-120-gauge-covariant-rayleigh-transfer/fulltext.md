---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-120-gauge-covariant-rayleigh-transfer"
canonical_tex: "zeta_mvp0/papers/RH-120-gauge-covariant-rayleigh-transfer/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-120-gauge-covariant-rayleigh-transfer/main.pdf"
source_sha256: "64d389b76d909aad1b46edffd75a83532526500fcb4a60798d9999958e31f69e"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Gauge-Covariant Rayleigh Transfer A Sharp Cross-Level Theorem for Directional Tail Gramians

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-120-gauge-covariant-rayleigh-transfer>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-120-gauge-covariant-rayleigh-transfer/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-120-gauge-covariant-rayleigh-transfer/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-120-gauge-covariant-rayleigh-transfer/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-120-gauge-covariant-rayleigh-transfer/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The directional route of RH-114 isolates a positive Gramian $G$ for four recent directions and a positive tail upper $D$, with relative constant $\gamma^2=\lambda_{\max}(G^{-1/2}DG^{-1/2})$. We prove the basic cross-level theorem needed to compare two such pairs. If $S$ is invertible and $$G'\succeq aS^*GS,\qquad D'\preceq bS^*DS,$$ then $\gamma'\leq\sqrt{b/a}\,\gamma$. In dimension four, $\sqrt{\det G'}\geq a^2|\det S|\sqrt{\det G}$. Both conclusions are simultaneously sharp, and exact congruence leaves $\gamma$ invariant. A 4,096-instance audit has zero failures. The result supplies exact transfer algebra; it does not prove that the physical scale sequence has uniform values of $a$, $b$, or $S$.
author:
- Prime Dynamics Theory Program
bibliography:
- references.bib
date: July 2026
title: |
  Gauge-Covariant Rayleigh Transfer\
  A Sharp Cross-Level Theorem for Directional Tail Gramians
```

## Markdown 正文

# Relative directional data

Let $G\succ0$ and $D\succeq0$ act on a four-dimensional frame coordinate space. Define $$\label{eq:gamma}
 \gamma(G,D)^2=\lambda_{\max}(G^{-1/2}DG^{-1/2})
 =\inf\{t^2:D\preceq t^2G\}.$$ When $G=Y^*Y$ is the recent-action Gramian and $D\succeq R^*R$ is a tail upper, RH-114 gives the volume lower $(1-\gamma)_+^4\sqrt{\det G}$ for $Y+R$. The unresolved issue is how this pair changes from one level to the next. Coordinates themselves may rotate or shear, so a comparison that silently identifies two frames is not intrinsic. We therefore include an invertible gauge $S$.

# The transfer theorem

[\[thm:transfer\]]{#thm:transfer label="thm:transfer"} Let $G,G'\succ0$, $D,D'\succeq0$, and let $S$ be invertible. If $a>0$, $b\geq0$, and $$\label{eq:loewner}
 G'\succeq aS^*GS,\qquad D'\preceq bS^*DS,$$ then $$\label{eq:gammatransfer}
 \gamma(G',D')\leq\sqrt{\frac ba}\,\gamma(G,D).$$

By definition, $D\preceq\gamma(G,D)^2G$. Congruence by $S$ and [\[eq:loewner\]](#eq:loewner){reference-type="eqref" reference="eq:loewner"} give $$D'\preceq bS^*DS
 \preceq b\gamma(G,D)^2S^*GS
 \preceq\frac ba\gamma(G,D)^2G'.$$ The variational characterization in [\[eq:gamma\]](#eq:gamma){reference-type="eqref" reference="eq:gamma"} proves the claim.

The proof uses only Loewner order and congruence, so it remains valid over a complex Hilbert space with transposes replaced by adjoints [@Bhatia2007; @HornJohnson1991].

[\[cor:volume\]]{#cor:volume label="cor:volume"} Under the first inequality in [\[eq:loewner\]](#eq:loewner){reference-type="eqref" reference="eq:loewner"}, in dimension four, $$\label{eq:volume}
 \sqrt{\det G'}\geq a^2|\det S|\sqrt{\det G}.$$

Determinant is monotone on positive definite matrices. Hence $\det G'\geq\det(aS^*GS)=a^4|\det S|^2\det G$.

If $G'=S^*GS$ and $D'=S^*DS$, then $\gamma(G',D')=\gamma(G,D)$ and $\sqrt{\det G'}=|\det S|\sqrt{\det G}$.

Theorem [\[thm:transfer\]](#thm:transfer){reference-type="ref" reference="thm:transfer"} gives one inequality. Apply it again with $S^{-1}$ to obtain the reverse inequality. The determinant identity is exact.

# Sharpness and information content

Take any $G\succ0$, set $D=\gamma^2G$, and choose an invertible $S$. For $a>0$ and $b\geq0$, put $$G'=aS^*GS,\qquad D'=bS^*DS.$$ Then $$\gamma(G',D')=\sqrt{b/a}\,\gamma,
 \qquad
 \sqrt{\det G'}=a^2|\det S|\sqrt{\det G}.$$ Thus neither factor can be improved from the two Loewner hypotheses alone. In particular, a good geometric alignment of $G$ is insufficient if the same gauge makes $D$ grow rapidly. The meaningful next quantity is the smallest admissible $b$ among gauges that align the two recent Gramians.

The theorem is deliberately one-sided. It does not assert that a gauge is unique, well conditioned, or physically natural. Those are separate questions. It also shows exactly where a numerical enclosure must enter: one must certify the two matrix inequalities, not merely observe that their eigenvalues are close.

# Computational audit

We generated 4,096 pairs of random positive definite $4\times4$ Gramians, random invertible gauges, gram factors over three decades, and tail factors over three decades. Target Gramians were enlarged by independent PSD increments and target tails were contracted inside the allowed upper. The audit directly evaluates both minimum Loewner slacks, both generalized Rayleigh constants, and both determinants.

There are zero hypothesis, gamma, or volume failures. A separate scalar-congruence record attains both bounds to relative error below $10^{-12}$. Figure [1](#fig:audit){reference-type="ref" reference="fig:audit"} displays the efficiency distributions; values below one represent legitimate slack introduced in the random target pair.

![Transferred versus actual relative-tail constants and four-volume lower bounds. The independent sharp family attains equality in both.](<../../../../../zeta_mvp0/papers/RH-120-gauge-covariant-rayleigh-transfer/figures/gauge_covariant_rayleigh_transfer.pdf>){#fig:audit width="\\textwidth"}

# Consequence for the route

RH-120 removes one algebraic ambiguity from the directional-Rayleigh frontier packet: cross-level transport is possible without identifying the two frame coordinates. What remains is physical rather than formal. One must choose gauges for the archived scale pairs, determine the least tail inflation compatible with exact Gram alignment, and then seek a uniform or recursive bound on those constants. RH-121 addresses the optimal-gauge problem and audits the existing five-scale chain.

No all-level physical gauge law, uniform Stage A, Hilbert--Polya operator, zeta-zero identification, or Riemann Hypothesis conclusion is claimed.
