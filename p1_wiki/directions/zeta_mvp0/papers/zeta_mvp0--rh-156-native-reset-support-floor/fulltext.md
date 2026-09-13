---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-156-native-reset-support-floor"
canonical_tex: "zeta_mvp0/papers/RH-156-native-reset-support-floor/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-156-native-reset-support-floor/main.pdf"
source_sha256: "5926c12cfcd2c6c25d27ef288eb8a0350958baf0d921b40ea36ee1740cd74dbc"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Native Reset Support Floor Sharp Endpoint Composition and a 62-Step Common Finite Tube

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-156-native-reset-support-floor>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-156-native-reset-support-floor/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-156-native-reset-support-floor/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-156-native-reset-support-floor/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-156-native-reset-support-floor/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The reset route now has three compatible ingredients. RH-153 transports a correlated Gram--tail pair through an overlap congruence without changing its relative tail. RH-154 supplies a well-conditioned terminal half. RH-155 constructs a native recent/tail pair with a subunit Loewner ratio at all 130 frozen snapshots.

  We compose these ingredients in one sharp endpoint theorem. Suppose the selected full-memory eigenvalues lie in $[\ell,u]$, the old tail has operator mass at most $\tau$, and the reset overlap singular values lie in $[\alpha,\beta]$. If $\ell>2\tau$, then the transported native support satisfies $$\mathcal S\geq
   \frac{\alpha}{\beta}
   \sqrt{\frac{\ell-\tau}{u}}
   \left(1-\sqrt{\frac{\tau}{\ell-\tau}}\right)^4.$$ The formula is jointly sharp from these scalar endpoints.

  All 120 frozen transitions have positive support lower. The minimum is $3.26204\times10^{-8}$, the median is $3.26385\times10^{-4}$, and 111 and 74 transitions exceed $10^{-6}$ and $10^{-4}$ respectively. All 62 terminal-half transitions form a common finite tube with the same minimum. This closes the finite native reset architecture. The support functional is not yet identified with the projected-cross directional quantity used in the earlier Stage-A route.
author:
- Prime Dynamics Theory Program
bibliography:
- references.bib
date: July 2026
title: |
  A Native Reset Support Floor\
  Sharp Endpoint Composition and a 62-Step Common Finite Tube
```

## Markdown 正文

# The endpoint data

Let $M=R+D$ be the full, recent, and old-tail memories compressed to the exact reset packet. RH-155 gives $$\ell I\preceq M\preceq uI,
 \qquad 0\preceq D\preceq\tau I,$$ so $$R\succeq(\ell-\tau)I,qquad
 D\preceq xR,quad x=\frac{\tau}{\ell-\tau}.$$ Let $C$ be an invertible overlap map with singular values in $[\alpha,\beta]$, and transport both matrices by $\Phi_C(A)=C^{-*}AC^{-1}$. The relative tail $x$ is unchanged by RH-153.

For a positive pair define the native support functional $$\mathcal S(G,D)=
 \sqrt{\frac{\lambda_{\min}(G)}{\lambda_{\max}(G)}}
 \left(1-\sqrt{\gamma^2(G,D)}\right)_+^4,$$ where $\gamma^2(G,D)=\inf\{y:D\preceq yG\}$.

# Sharp support composition

[\[thm:support\]]{#thm:support label="thm:support"} Assume $0<\alpha\leq\beta$, $0\leq\tau<\ell\leq u$, and use the endpoint data above. Then $$\mathcal S(\Phi_C(R),\Phi_C(D))\geq
 \frac{\alpha}{\beta}
 \sqrt{\frac{\ell-\tau}{u}}
 \left(1-\sqrt{\frac{\tau}{\ell-\tau}}\right)_+^4.$$ The right side is positive exactly when $\ell>2\tau$ and $\alpha>0$. The complete expression is sharp from the five scalar endpoints.

The recent eigenvalue endpoints give $$a(R):=\sqrt{\lambda_{\min}(R)/\lambda_{\max}(R)}
 \geq\sqrt{(\ell-\tau)/u},$$ because $R\preceq M\preceq uI$. Inverse congruence lowers this normalized base by at most $\alpha/\beta$. Loewner covariance preserves the tail ratio, which is at most $\tau/(\ell-\tau)$. The fourth-power factor is decreasing, so multiplication proves the formula.

For sharpness, take two dimensions with $M=\operatorname{diag}(u,\ell)$, $D=\operatorname{diag}(0,\tau)$, and $C=\operatorname{diag}(\alpha,\beta)$. Assigning the $u$ direction to $\alpha$ and the $\ell-\tau$ direction to $\beta$ attains the base endpoint, while the second direction attains the tail ratio. Hence all factors are simultaneously attained [@Bhatia1997; @HornJohnson2013].

[\[cor:tube\]]{#cor:tube label="cor:tube"} For any finite reset family satisfying the theorem, the minimum of the displayed endpoint lowers is a valid common support floor. Congruence conditioning is paid once per independently reset snapshot, not multiplied through a recursive chain.

The last sentence is essential. The atlas is reanchored at every snapshot; we do not multiply 120 support lowers or inverse-overlap factors.

# Frozen support audit

For each RH-153 transition we use its robust overlap lower and selected full-memory eigenvalue upper. The lower selected eigenvalue is the minimum of the independently reconstructed RH-153 and RH-155 outward values. The geometric tail mass is taken from RH-155. Since overlaps of orthonormal frames have $\beta\leq1$, we set $\beta=1$.

Every one of the 120 transitions is positive. The smallest lower, $3.26204\times10^{-8}$, is the terminal $\sigma=0.01$ left snapshot. There the recent-base lower is $4.2620\times10^{-7}$ and the conservative tail factor is $0.0765374$. Thus the weakest support is caused by both terminal spectral thinning and the largest certified tail ratio, not by an overlap birth spike.

The median support lower is $3.26385\times10^{-4}$ and the maximum is $0.197087$. All 120 exceed $10^{-8}$, 111 exceed $10^{-6}$, and 74 exceed $10^{-4}$. The RH-154 terminal-half family contains 62 transitions; all are positive and their common floor is again $3.26204\times10^{-8}$. Delayed start improves conditioning while leaving the terminal support wall visible.

![All transition support lowers, separation of base and tail losses, full-versus-delayed channel floors, and threshold counts.](<../../../../../zeta_mvp0/papers/RH-156-native-reset-support-floor/figures/native_reset_support_floor.pdf>){#fig:audit width="\\textwidth"}

# A conditional all-level endpoint criterion

The finite formula also identifies the exact analytic packets needed for an eventual theorem. Let $(\ell_n,u_n,\tau_n,\alpha_n,\beta_n)$ be outward endpoint data for an all-level reset family and suppose each transition is reanchored independently.

[\[cor:eventual\]]{#cor:eventual label="cor:eventual"} Assume that, after a finite index, $$\ell_n\geq\ell_*>2\tau_*,\qquad
 \tau_n\leq\tau_*,\qquad
 u_n\leq u_*<\infty,$$ and $$0<\alpha_*\leq\alpha_n\leq\beta_n\leq\beta_*<\infty.$$ Then the native reset support has the uniform eventual floor $$\liminf_{n\to\infty}\mathcal S_n\geq
 \frac{\alpha_*}{\beta_*}
 \sqrt{\frac{\ell_*-\tau_*}{u_*}}
 \left(1-\sqrt{\frac{\tau_*}{\ell_*-\tau_*}}\right)^4>0.$$ For trace-one geometric memory one may take $\tau_*=\eta^d/(1-\eta)$.

Apply Theorem [\[thm:support\]](#thm:support){reference-type="ref" reference="thm:support"} at every sufficiently large index and use monotonicity in the five endpoints. A finite omitted prefix does not alter the liminf.

Within this scalar endpoint architecture, none of the three qualitative requirements can simply be dropped. If $\alpha_n/\beta_n\to0$, the chart can flatten the normalized base. If $\ell_n\downarrow2\tau_*$, the tail factor tends to zero. If $u_n/(\ell_n-\tau_n)\to\infty$, the recent base can vanish even while the tail remains subunit. Diagonal examples realize all three boundaries. Thus the next asymptotic work is not an unspecified compactness argument: it must control overlap conditioning, the selected weak eigenvalue relative to the universal tail mass, and the selected spectral spread.

# What has and has not closed

The finite native route is now internally complete: source-memory balls select reset packets, overlaps provide coherent charts, correlated congruence preserves the tail ratio, a delayed suffix removes finite birth conditioning, and Theorem [\[thm:support\]](#thm:support){reference-type="ref" reference="thm:support"} supplies one common positive support floor.

However, this native functional uses the recent memory compressed directly to the reset packet. The older directional construction used a projected cross action, a four-direction frame, wedge volume, leading singular value, and capacity. Equality or domination between those functionals has not been proved. Nor have we established all-level endpoint laws, Stage A, a Hilbert--Polya operator, zeta-zero identification, or the Riemann Hypothesis.
