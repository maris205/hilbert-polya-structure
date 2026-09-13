---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-orbit-resolved-reflection-euler-boundary"
canonical_tex: "henon_dynamics/henon_orbit_resolved_reflection_euler_boundary/paper/paper.tex"
canonical_pdf: "henon_dynamics/henon_orbit_resolved_reflection_euler_boundary/paper/paper.pdf"
source_sha256: "2866d399bfa8c2f68051211cbc5ca7774e104213115f914b6cd0cfb01a0922c8"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The Moving Essential Boundary of an Orbit-Resolved Hénon Reflection Euler Product

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_orbit_resolved_reflection_euler_boundary>)
- [规范 TeX](<../../../../../henon_dynamics/henon_orbit_resolved_reflection_euler_boundary/paper/paper.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_orbit_resolved_reflection_euler_boundary/paper/paper.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_orbit_resolved_reflection_euler_boundary/README.md>)
- [BibTeX](<../../../../../henon_dynamics/henon_orbit_resolved_reflection_euler_boundary/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We construct the full Euler product carrying the individual symmetry-defect weights of every primitive odd reflection word in the full Hénon horseshoe. If $A_n$ is the primitive marked packet and $S_n\chi$ is the orbit sum of $\chi(s)=\mathbf1\{s_{-1}=s_1\}$, set $$\mathcal Z_{\rm orb}(z,q)=
   \prod_{n\ {\rm odd}}\prod_{\omega\in A_n}
   (1-z^nq^{S_n\chi(\omega)})^{-1}.$$ Its logarithmic derivative has the exact primitive/repetition coefficient $\sum_{n\mid m}nE_n(q^{m/n})$, where $E_n$ is the primitive moment polynomial. For every $q>0$, the convergence radius is $R(q)=(1+q^2)^{-1/2}$ and $$\log\mathcal Z_{\rm orb}(z,q)
   =\frac{q}{\sqrt{1+q^2}\,[1-\sqrt{1+q^2}\,z]}+G_q(z)$$ near the positive boundary, with $G_q$ analytic. Thus the boundary is exponentially essential. The aggregate-mean radius is $(2q)^{-1/2}$ and is strictly too large unless $q=1$. This closes the orbit-resolved analytic germ but leaves relative Lind/Fredholm renormalization and arithmetic semantics open.
author:
- |
  Liang Wang\
  School of Artificial Intelligence and Automation\
  Huazhong University of Science and Technology\
  Wuhan 430074, P. R. China
bibliography:
- references.bib
date: 'August 16, 2026'
title: |
  The Moving Essential Boundary of an\
  Orbit-Resolved Hénon Reflection Euler Product
```

## Markdown 正文

# From moments to individual Euler factors

For $H(x,y)=(6-x^2-y,x)$, the inherited full-horseshoe coding and reversor identify odd reflection packets with reversal-fixed binary words [@DevaneyNitecki1979; @Arai2007]. Let $A_n$ be the primitive marked packet and put $$\chi(s)=\mathbf1\{s_{-1}=s_1\},\qquad
 S_n\chi(s)=\sum_{j=0}^{n-1}\chi(\sigma^js).$$ The primitive moment polynomial $$\label{eq:En}
 E_n(q)=\sum_{\omega\in A_n}q^{S_n\chi(\omega)}$$ was computed exactly from the reflected rank-two transfer matrix: $$\begin{aligned}
 F_{2m+1}(q)&=2q(1+q^2)^m,\label{eq:Fn}\\
 E_n(q)&=\sum_{k\mid n}\mu(k)F_{n/k}(q^k).\label{eq:primitive}\end{aligned}$$

For $q>0$, define the orbit-resolved product $$\label{eq:product}
 \mathcal Z_{\rm orb}(z,q)=\prod_{\substack{n\ge1\\n\ {\rm odd}}}
 \prod_{\omega\in A_n}
 \left(1-z^nq^{S_n\chi(\omega)}\right)^{-1}.$$ Unlike an aggregate-mean product, [\[eq:product\]](#eq:product){reference-type="eqref" reference="eq:product"} retains every individual energy in [\[eq:En\]](#eq:En){reference-type="eqref" reference="eq:En"}.

[\[thm:ledger\]]{#thm:ledger label="thm:ledger"} In the disk of absolute convergence, $$\begin{aligned}
 \log\mathcal Z_{\rm orb}(z,q)&=\sum_{r\ge1}\frac1r E(z^r,q^r),
 \qquad E(z,q):=\sum_{n\ {\rm odd}}E_n(q)z^n,\label{eq:log}\\
 [z^m]\,z\partial_z\log\mathcal Z_{\rm orb}(z,q)
 &=\sum_{\substack{n\mid m\\n\ {\rm odd}}}
 nE_n(q^{m/n}).\label{eq:derivative}\end{aligned}$$

Expand each factor of [\[eq:product\]](#eq:product){reference-type="eqref" reference="eq:product"} by $-\log(1-w)=\sum_{r\ge1}w^r/r$. An $r$-fold repetition replaces both $z^n$ by $z^{nr}$ and $q^{S_n\chi}$ by $q^{rS_n\chi}$. Summing first over $\omega$ gives $E_n(q^r)$, proving [\[eq:log\]](#eq:log){reference-type="eqref" reference="eq:log"}; differentiation and collection of $m=nr$ gives [\[eq:derivative\]](#eq:derivative){reference-type="eqref" reference="eq:derivative"}.

# The two-variable primitive series

[\[prop:primitive-series\]]{#prop:primitive-series label="prop:primitive-series"} For $q>0$ and sufficiently small $z$, $$\label{eq:Eseries}
 E(z,q)=\sum_{\substack{k\ge1\\k\ {\rm odd}}}
 \mu(k)\frac{2(qz)^k}
 {1-(1+q^{2k})z^{2k}}.$$ Its first positive singularity is $$\label{eq:radius}
 R(q)=\frac1{\sqrt{1+q^2}}.$$ Near $R(q)$, $$\label{eq:Eprincipal}
 E(z,q)=
 \frac{q/\sqrt{1+q^2}}{1-\sqrt{1+q^2}\,z}+G_{1,q}(z),$$ where $G_{1,q}$ is analytic.

Insert [\[eq:Fn\]](#eq:Fn){reference-type="eqref" reference="eq:Fn"} into [\[eq:primitive\]](#eq:primitive){reference-type="eqref" reference="eq:primitive"}, multiply by $z^n$, and interchange the sums to obtain [\[eq:Eseries\]](#eq:Eseries){reference-type="eqref" reference="eq:Eseries"}. The $k=1$ denominator gives [\[eq:radius\]](#eq:radius){reference-type="eqref" reference="eq:radius"} and the displayed principal part. For odd $k\ge3$, $$(1+q^{2k})^{1/k}<1+q^2$$ by the strict binomial inequality. Therefore their positive singular radii are all larger than $R(q)$.

# Moving essential boundary

[\[thm:boundary\]]{#thm:boundary label="thm:boundary"} For every fixed $q>0$, there is a function $G_q$, analytic near $R(q)$, such that $$\label{eq:principal}
 \log\mathcal Z_{\rm orb}(z,q)=
 \frac{q}{\sqrt{1+q^2}\,[1-\sqrt{1+q^2}\,z]}+G_q(z).$$ Consequently $\mathcal Z_{\rm orb}(\,\cdot\,,q)$ has an essential singularity at $R(q)$.

The $r=1$ term of [\[eq:log\]](#eq:log){reference-type="eqref" reference="eq:log"} is handled by [\[prop:primitive-series\]](#prop:primitive-series){reference-type="ref" reference="prop:primitive-series"}. For $r\ge2$, the first positive singular radius of $E(z^r,q^r)$ is $$(1+q^{2r})^{-1/(2r)}>R(q),$$ again by the strict binomial inequality. Hence all repetition terms are analytic near $R(q)$. Equation [\[eq:principal\]](#eq:principal){reference-type="eqref" reference="eq:principal"} follows, and exponentiating a simple pole gives an essential singularity.

The object in [\[eq:product\]](#eq:product){reference-type="eqref" reference="eq:product"} is still a restricted marked-packet product, not the full Lind zeta of the infinite-dihedral action [@KimLeePark2003; @Ryu2019]. The latter includes all finite-index subgroup fixed-point data.

# The exact cost of mean-field weighting

Write $q=e^{-s}$. The orbit-resolved pressure is $\frac12\log(1+q^2)$, while the aggregate-mean pressure is $\frac12\log(2q)$. Thus their radii obey $$\label{eq:ratio}
 \frac{R(q)}{R_{\rm mf}(q)}
 =\sqrt{\frac{2q}{1+q^2}}
 =\frac1{\sqrt{(q+q^{-1})/2}}\le1.$$ Equality holds only for $q=1$. Mean-field weighting therefore predicts a strictly too-large disk at every nontrivial positive weight. At $q=1$, [\[eq:product\]](#eq:product){reference-type="eqref" reference="eq:product"} specializes coefficientwise to the unweighted canonical packet product.

# Certificate and route boundary

The exact certificate constructs [\[eq:derivative\]](#eq:derivative){reference-type="eqref" reference="eq:derivative"} as integer polynomials through degree $31$, checks the rational values $q=1/2,1,2$, and locks the $q=1$ coefficients to the earlier product. An independent program audits [\[eq:radius\]](#eq:radius){reference-type="eqref" reference="eq:radius"}--[\[eq:ratio\]](#eq:ratio){reference-type="eqref" reference="eq:ratio"} at five positive weights. Eight tests pass in normal and optimized modes, six dependencies are locked, and 24 hostile mutations are rejected.

The result closes a full orbit-resolved Route-A Euler germ and its boundary curve. Its essential singularity prevents naive Fredholm promotion but does not exclude a separately proved relative counterterm. No rational-prime labels, von Mangoldt amplitudes, Hilbert space, or self-adjoint operator have been constructed. Route B is not authorized. The next major problem is a source-native comparison with the full flip/Lind zeta and an explicit relative renormalization test.
