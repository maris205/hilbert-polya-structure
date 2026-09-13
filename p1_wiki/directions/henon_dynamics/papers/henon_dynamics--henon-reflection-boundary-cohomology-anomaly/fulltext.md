---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-reflection-boundary-cohomology-anomaly"
canonical_tex: "henon_dynamics/henon_reflection_boundary_cohomology_anomaly/paper/paper.tex"
canonical_pdf: "henon_dynamics/henon_reflection_boundary_cohomology_anomaly/paper/paper.pdf"
source_sha256: "790e50248c8659a476a680243f6a764b751fc8c177a6523addf5ae49b006c444"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Norm-Two Cohomology Anomaly at the Hénon Reflection Boundary

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_reflection_boundary_cohomology_anomaly>)
- [规范 TeX](<../../../../../henon_dynamics/henon_reflection_boundary_cohomology_anomaly/paper/paper.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_reflection_boundary_cohomology_anomaly/paper/paper.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_reflection_boundary_cohomology_anomaly/README.md>)
- [BibTeX](<../../../../../henon_dynamics/henon_reflection_boundary_cohomology_anomaly/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Primitive odd reflection points of the full Hénon horseshoe admit two natural sampling conventions. Marking the reflection center converges to a non-invariant boundary Bernoulli law $\eta_J$, whereas cyclic orbit averaging converges to the invariant maximal-entropy law. We prove that marked packet pressure is not invariant under symbolic coboundaries. Its anomaly is the functional $$A_J(u)=\int (u-u\circ\sigma)\,d\eta_J,$$ whose dual total-variation norm is exactly two. Explicit locally constant functions $v_r$ satisfy $A_J(v_r)=2(1-2^{-r})$, so the extremal norm is approached by finite cylinders. By contrast, a coboundary sums to zero on every finite periodic orbit; consequently every uniformly orbit-averaged packet pressure is exactly gauge invariant before taking a limit. The result identifies orbit averaging as a necessary structural repair, while making no arithmetic trace or operator claim. An exact mutation-locked certificate accompanies the theorem.
author:
- |
  Liang Wang\
  School of Artificial Intelligence and Automation\
  Huazhong University of Science and Technology\
  Wuhan 430074, P. R. China
bibliography:
- references.bib
date: 'August 15, 2026'
title: 'A Norm-Two Cohomology Anomaly at the Hénon Reflection Boundary'
```

## Markdown 正文

# Reflection-boundary sampling

The area-preserving Hénon map $$H(x,y)=(6-x^2-y,x)$$ has a real chain-recurrent set conjugate to the full two-shift; its reversor is intertwined with sequence reversal. This follows from the Devaney--Nitecki horseshoe and Arai's hyperbolic plateau [@DevaneyNitecki1979; @Arai2007]. We use the standard left shift $(\sigma\omega)_k=\omega_{k+1}$ on $\{0,1\}^{\mathbb Z}$; basic symbolic cohomology terminology follows @LindMarcus1995.

Let $(\xi_k)_{k\geq0}$ be independent fair bits and define the marked reflection-boundary process $$\label{eq:eta}
 \omega_k=\omega_{-k}=\xi_k \qquad (k\geq0).$$ Its law is denoted by $\eta_J$. Earlier packet equidistribution shows that marked primitive reflection points converge to $\eta_J$, while uniformly averaging their time origins converges to the fair two-sided Bernoulli law. The present paper asks whether the marked pressure is an intrinsic object under the usual potential relation $$\label{eq:cohomology}
 f' = f+u-u\circ\sigma.$$

For a continuous potential $f$, write the marked packet pressure as $$\label{eq:pressuredef}
 P_J(f)=\frac12\log2-\int f\,d\eta_J.$$ This is the limiting extensive pressure proved for the preceding packet family; the formula also defines its continuous extension to arbitrary symbolic potentials.

# The boundary anomaly

Define $$\label{eq:anomaly}
 A_J(u)=\int (u-u\circ\sigma)\,d\eta_J.$$

[\[thm:gauge\]]{#thm:gauge label="thm:gauge"} For every continuous $f,u$, $$\label{eq:gaugelaw}
 P_J(f+u-u\circ\sigma)=P_J(f)-A_J(u).$$ In particular, marked pressure descends to symbolic cohomology classes if and only if $A_J$ vanishes identically.

Substitution of [\[eq:cohomology\]](#eq:cohomology){reference-type="eqref" reference="eq:cohomology"} into [\[eq:pressuredef\]](#eq:pressuredef){reference-type="eqref" reference="eq:pressuredef"} gives [\[eq:gaugelaw\]](#eq:gaugelaw){reference-type="eqref" reference="eq:gaugelaw"}. The last statement follows by testing every transfer function $u$.

The functional is nonzero because $\eta_J$ is not shift invariant. More is true. For a finite signed measure $\nu$, use the dual norm $$\lVert\nu\rVert_{\mathrm{TV}}
 =\sup_{\lVert u\rVert_\infty\leq1}\left|\int u\,d\nu\right|,$$ which equals two, rather than one, for the difference of mutually singular probability measures.

[\[thm:normtwo\]]{#thm:normtwo label="thm:normtwo"} The measures $\eta_J$ and $\sigma_*\eta_J$ are mutually singular, and $$\label{eq:normtwo}
 \lVert A_J\rVert
 =\lVert\eta_J-\sigma_*\eta_J\rVert_{\mathrm{TV}}=2.$$

The support of $\eta_J$ consists of sequences fixed by reflection about the marked origin. The support of $\sigma_*\eta_J$ consists of sequences fixed by reflection about the adjacent center. A sequence satisfying both symmetries is invariant under their composition, a shift by two, and hence is period two. This finite set has probability zero under either iid half-word construction. The measures are therefore mutually singular. The difference of two mutually singular probability measures has dual total-variation norm two. Finally, $A_J(u)=\int u\,d(\eta_J-\sigma_*\eta_J)$.

# Finite-cylinder extremizers

The norm in [\[thm:normtwo\]](#thm:normtwo){reference-type="ref" reference="thm:normtwo"} is not merely an abstract measure-theoretic quantity. For $r\geq1$, let $$\label{eq:ur}
 u_r(\omega)=\mathbf 1_{\{\omega_{-k}=\omega_k\;\text{for }1\leq k\leq r\}},
 \qquad v_r=2u_r-1.$$

[\[prop:witness\]]{#prop:witness label="prop:witness"} For every $r\geq1$, $$\label{eq:witness}
 \int u_r\,d\eta_J=1,
 \qquad
 \int u_r\circ\sigma\,d\eta_J=2^{-r},
 \qquad
 A_J(v_r)=2(1-2^{-r}).$$ Thus $\lVert v_r\rVert_\infty=1$ and $A_J(v_r)\to2$.

The first equality is built into [\[eq:eta\]](#eq:eta){reference-type="eqref" reference="eq:eta"}. After one shift, the $r$ constraints become $$\xi_{k-1}=\xi_{k+1},\qquad 1\leq k\leq r.$$ They leave precisely two free parity classes among the $r+2$ involved fair bits, so their probability is $2^2/2^{r+2}=2^{-r}$. Affine centering then gives the third equality.

This also gives a fully finite diagnosis: a radius-$r$ cylinder already detects all but $2^{1-r}$ of the maximal anomaly.

# Orbit averaging repairs the gauge

Let $\omega$ be periodic with period $n$. The coboundary identity telescopes: $$\label{eq:telescoping}
 \sum_{j=0}^{n-1}(u-u\circ\sigma)(\sigma^j\omega)
 =u(\omega)-u(\sigma^n\omega)=0.$$

[\[cor:orbit\]]{#cor:orbit label="cor:orbit"} Every packet statistic formed by uniformly averaging a potential over each complete periodic orbit is unchanged by [\[eq:cohomology\]](#eq:cohomology){reference-type="eqref" reference="eq:cohomology"}, at every finite period and for every transfer function $u$.

Apply [\[eq:telescoping\]](#eq:telescoping){reference-type="eqref" reference="eq:telescoping"} orbit by orbit before taking any packet sum or limit.

The contrast is structural. Marked reflection sampling retains a boundary and therefore a norm-two gauge defect. Complete cyclic sampling removes the boundary exactly. This proves that the frozen coordinate-Mahler marked law is a valid coordinate-dependent statistic, but not a canonical Livšic invariant. It also isolates the next theorem: among normalized linear samplers on an $n$-cycle, is uniform cyclic averaging the unique sampler that annihilates every coboundary?

# Executable certificate and claim boundary

The accompanying exact-arithmetic programs verify [\[eq:witness\]](#eq:witness){reference-type="eqref" reference="eq:witness"} for $1\leq r\leq12$, mutual-singularity support intersections on finite windows, and telescoping on every binary word through period $10$. Two independent implementations agree, seven unit tests pass in normal and optimized modes, and 19 hostile mutations of signs, shifts, normalizations, and endpoint claims are rejected. No floating-point evidence enters the theorem.

This paper proves a symbolic pressure obstruction and its exact repair. It does not produce rational-prime labels, von Mangoldt amplitudes, a Fredholm determinant, a self-adjoint operator, or a Hilbert--Pólya correspondence. Route A therefore remains exploratory and Route B is not authorized.
