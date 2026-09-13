---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-118-conditional-composite-exterior-route"
canonical_tex: "zeta_mvp0/papers/RH-118-conditional-composite-exterior-route/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-118-conditional-composite-exterior-route/main.pdf"
source_sha256: "ec739001ca69478c6051eb3d87a03d81dbf45400d86f863c3581ad5a47148a9e"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Conditional Composite Exterior Route Liminf Closure and the Minimal Remaining Physical Hypotheses

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-118-conditional-composite-exterior-route>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-118-conditional-composite-exterior-route/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-118-conditional-composite-exterior-route/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-118-conditional-composite-exterior-route/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-118-conditional-composite-exterior-route/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We assemble the finite-memory exterior route into a single conditional all-level theorem. For each level, four independently valid lower candidates for the relative fourth singular mode are admitted: direct Weyl, spectral four-volume divided by three-mode capacity, normalized exterior trace divided by concentration and capacity, and a directional Rayleigh volume corrected by a relative tail factor. Their maximum is a lower bound, and a strict liminf crossing of the target threshold implies eventual support even when the winning route alternates with level. Route-specific outward transport losses enter only by downward degradation. The aligned five-scale audit has 360 threshold-labelled records. The RH-115 composite closes 321 of 322 genuinely supported records, while the internally consistent RH-116 adaptive route closes all 322; both have zero false positives and their support labels agree. The theorem isolates three minimal physical condition packets---direct margin, trace--concentration, and directional Rayleigh. Their finite algebra and audits are closed, but none of their all-level liminf conditions is proved. The result is a route map, not an unconditional Stage A or Riemann Hypothesis theorem.
author:
- Prime Dynamics Theory Program
bibliography:
- references.bib
date: July 2026
title: |
  A Conditional Composite Exterior Route\
  Liminf Closure and the Minimal Remaining Physical Hypotheses
```

## Markdown 正文

# Factor ledger at one level

Let $K$ be a nonzero projected cross with singular ratios $$q_j=\frac{s_j(K)}{s_1(K)},\qquad
 \nu_4=q_2q_3q_4,
 \qquad \Lambda_{23}=q_2q_3.$$ The exact identity is $$\label{eq:identity}
 q_4=\frac{\nu_4}{\Lambda_{23}}.$$ Assume all numerical quantities below enclose this same operator $K$, or have first been transported to it by an outward perturbation radius in the sense of interval analysis [@Moore1966].

Let $D^-$ be any direct lower for $q_4$, let $V^-$ be any lower for $\nu_4$, and let $L^+>0$ satisfy $\Lambda_{23}\leq L^+$. Then $V^-/L^+\leq q_4$ by [\[eq:identity\]](#eq:identity){reference-type="eqref" reference="eq:identity"}.

The trace route can be written intrinsically. Define $$\Theta_4(K)=\frac{e_4(s(K)^2)}{s_1(K)^8},\qquad
 \kappa_4(K)=
 \frac{e_4(s(K)^2)}{s_1(K)^2s_2(K)^2s_3(K)^2s_4(K)^2}.$$ Whenever the denominator is nonzero, $$\label{eq:traceidentity}
 \nu_4(K)^2=\frac{\Theta_4(K)}{\kappa_4(K)}.$$ Thus $\Theta^-\leq\Theta_4$ and $\kappa_4\leq\kappa^+$ give $$q_4\geq \frac{\sqrt{\Theta^-/\kappa^+}}{L^+}.$$ RH-111 provides the finite-memory mechanism for constructing these one-sided inputs.

For the directional route, let $A$ be a four-column recent-frame action and let the residual action satisfy the relative Gram inequality $$R^*R\preceq (\gamma^+)^2 A^*A.$$ The RH-114 determinant comparison gives a multiplicative factor $(1-\gamma^+)_+^4$. If $a^-$ is a normalized lower for the recent-frame four-volume, then $$q_4\geq
 \frac{(1-\gamma^+)_+^4a^-}{L^+}.$$ The matrix inequalities used in these conversions are standard singular and Rayleigh comparison principles [@HornJohnson1991].

# The conditional all-level gate

Index levels by $n$. At level $n$, assume admitted one-sided data $$D_n^-,\quad V_n^-,\quad \Theta_n^-,\quad \kappa_n^+,
 \quad a_n^-,\quad \gamma_n^+,quad L_n^+.$$ Zero is used whenever a route lacks a valid input. Define $$\label{eq:gate}
 B_n=\max\left\{
 D_n^-,\
 \frac{V_n^-}{L_n^+},\
 \frac{\sqrt{\Theta_n^-/\kappa_n^+}}{L_n^+},\
 \frac{(1-\gamma_n^+)_+^4a_n^-}{L_n^+}
 \right\}.$$

[\[thm:gate\]]{#thm:gate label="thm:gate"} If every input in [\[eq:gate\]](#eq:gate){reference-type="eqref" reference="eq:gate"} has the stated one-sided validity for the same $K_n$, then $$B_n\leq q_4(K_n).$$

The direct term is valid by assumption. The spectral term follows from [\[eq:identity\]](#eq:identity){reference-type="eqref" reference="eq:identity"}, the trace term from [\[eq:traceidentity\]](#eq:traceidentity){reference-type="eqref" reference="eq:traceidentity"} and [\[eq:identity\]](#eq:identity){reference-type="eqref" reference="eq:identity"}, and the directional term from the relative Rayleigh comparison followed by [\[eq:identity\]](#eq:identity){reference-type="eqref" reference="eq:identity"}. The maximum of valid lower bounds remains a lower bound.

[\[cor:liminf\]]{#cor:liminf label="cor:liminf"} For a fixed threshold $\tau>0$, if $$\mathop{\mathrm{lim\,inf}}_{n\to\infty} B_n>\tau,$$ then $q_4(K_n)\geq\tau$ for every sufficiently large $n$.

A strict liminf gap makes $B_n>\tau$ eventually. Apply Theorem [\[thm:gate\]](#thm:gate){reference-type="ref" reference="thm:gate"} level by level.

No single route has to win eventually. Direct, trace, and directional terms may alternate indefinitely; only their admitted maximum needs a strict liminf gap. This is the alternating-route closure permitted by the composite theorem.

RH-116 supplies an exact algorithmic interpretation for the direct term. Along nested geometric memory windows, the Weyl lower is monotone in depth; the first passing depth is cost-minimal, and full-history search is complete for that certificate family. A uniform depth bound would improve cost, but is not logically required by Corollary [\[cor:liminf\]](#cor:liminf){reference-type="ref" reference="cor:liminf"}.

# Outward robustness

Different numerical assemblies cannot be fused solely because they agree to displayed digits. Suppose candidate $C_{i,n}$ has an outward transport loss $r_{i,n}\geq0$. Its admitted value is $$\widetilde C_{i,n}=\max\{0,C_{i,n}-r_{i,n}\}.$$

[\[prop:outward\]]{#prop:outward label="prop:outward"} If the transported candidates are valid for one enclosed $K_n$ and $$\mathop{\mathrm{lim\,inf}}_{n\to\infty}\max_i\widetilde C_{i,n}>\tau,$$ then eventual support follows. In particular, any uniform strict gate gap larger than the worst transport loss survives outward admission.

Downward transport preserves the lower-bound direction. Apply Corollary [\[cor:liminf\]](#cor:liminf){reference-type="ref" reference="cor:liminf"} to the transported maximum.

This proposition formalizes the RH-115 admission filter. RH-116 avoids the specific weak-mode interface by using one internally consistent Gram path; its numerical lower values are therefore reported as a separate self-contained route rather than silently merged with RH-115 values.

# Minimal physical condition packets

Within the present ledger, all-level closure can arrive through any one of three compound inequalities.

  packet        compound liminf condition                   primitive physical inputs                        status
  ------------- ------------------------------------------- ------------------------------------------------ --------
  direct        $D_n^->\tau$                                recent fourth-mode margin vs. tail               open
  trace         $\sqrt{\Theta_n^-/\kappa_n^+}/L_n^+>\tau$   trace lower; concentration and capacity uppers   open
  directional   $(1-\gamma_n^+)_+^4a_n^-/L_n^+>\tau$        frame-volume lower; gamma and capacity uppers    open

  : Minimal condition packets relative to the current theorem ledger.

"Minimal" here is ledger-relative: each row is one scalar closing condition after all algebraic factors have been eliminated. It is not a claim that no future theorem could discover a different primitive route. The trivial universal capacity bound $\Lambda_{23}\leq1$ is available, but a sharper physical capacity estimate can greatly reduce the required volume lower.

RH-117 proves that five anchors, even together with the range $0<\Lambda_{23}<1$, cannot establish any of these liminf conditions by extrapolation. A new inequality linking levels is necessary.

# Complete finite-gate audit

The audit aligns RH-115's admitted candidates and RH-116's adaptive direct certificates on five scales, two sides, three thresholds, and 360 labelled records. Reconstructing the RH-115 maximum produces zero discrepancies. The two assembly paths agree on all support labels and have no false positives.

  threshold     actual   direct   trace   directional   composite   adaptive
  ----------- -------- -------- ------- ------------- ----------- ----------
  $10^{-8}$        115      113     113           114         114        115
  $10^{-6}$        109      109     105           109         109        109
  $10^{-4}$         98       98      95            98          98         98

  : Full-chain support counts out of 120 updates per threshold.

Across thresholds there are 322 genuinely supported records. The admitted RH-115 composite closes 321 and misses one weak $10^{-8}$ record. The self-contained adaptive route closes all 322. Every fine-chain record is closed at every threshold. Within the RH-115 maximum, direct Weyl wins 189 labelled records and directional Rayleigh wins 171; the winner genuinely alternates.

![Left: finite support coverage. Right: route alternation and the unresolved all-level boundary.](<../../../../../zeta_mvp0/papers/RH-118-conditional-composite-exterior-route/figures/conditional_composite_exterior_route.pdf>){width="\\textwidth"}

# Consequence and boundary

The route is now logically complete in conditional form. Algebraic factorization, monotone fusion, outward degradation, and finite-depth search no longer hide implicit assumptions. What remains is physical: prove a strict all-level liminf condition for at least one packet, together with same-operator outward enclosures where independent numerical paths are used.

At present the count of proved all-level physical packets is zero out of three. Therefore this paper does not close uniform Stage A, construct a Hilbert--Polya operator, identify zeta zeros, or prove the Riemann Hypothesis.
