---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-hunter-saxton-periodic-wave-breaking-route-a"
canonical_tex: "henon_dynamics/henon_hunter_saxton_periodic_wave_breaking_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_hunter_saxton_periodic_wave_breaking_route_a/paper/main.pdf"
source_sha256: "cd24598bd9f4e282dbf38561c8ec4aa9172f2d9d44d7cdf69f9add4303c4f7d9"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Periodic Hunter--Saxton Flow: Exact Two-Sided Lifespan and Universal Wave Breaking

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_hunter_saxton_periodic_wave_breaking_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_hunter_saxton_periodic_wave_breaking_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_hunter_saxton_periodic_wave_breaking_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_hunter_saxton_periodic_wave_breaking_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For every nonconstant periodic $C^2$ datum, we solve the once-integrated Hunter--Saxton equation throughout its maximal classical characteristic interval. One scalar factor gives the exact Jacobian, both lifespan endpoints, and every first-breaking label. \>0 We prove conservation of slope energy and the universal coefficient $-2$ at all simultaneous first breaking points, and close the constant-data and post-breaking boundaries. \>1 An asymmetric exact regression family separates the minimum-controlled future from the maximum-controlled past; a strict Route-A audit remains negative.
author:
- 'Route-A source-local certificate HCS-C324'
date: 3 September 2026
title: |
  Periodic Hunter--Saxton Flow:\
  Exact Two-Sided Lifespan and Universal Wave Breaking
```

## Markdown 正文

trailerid \[\<C3242026090300000000000000000000\>\<C3242026090300000000000000000000\>\]

# Exact characteristic theorem

Let $\mathbb T=\mathbb R/\mathbb Z$ and consider the once-integrated equation $$\label{eq:HS}
 u_{tx}+u u_{xx}+\frac12u_x^2=-\frac12E,
 \qquad E=\int_{\mathbb T}u_x(t,x)^2\,dx.$$ This is our classical formulation for $C^2$ data; the differentiated third-order equation is not asserted pointwise at that regularity. Put $w_0=u_{0x}$, $m=\min w_0$, and $M=\max w_0$. Nonconstant periodicity implies $E>0$ and $m<0<M$.

[\[thm:main\]]{#thm:main label="thm:main"} Define, for a characteristic label $a$, $$\begin{aligned}
 F(t,a)&=\cos\frac{\sqrt E t}{2}
   +\frac{w_0(a)}{\sqrt E}\sin\frac{\sqrt E t}{2},\label{eq:F}\\
 T_+&=\frac2{\sqrt E}\arctan\frac{\sqrt E}{-m},
 &T_-&=-\frac2{\sqrt E}\arctan\frac{\sqrt E}{M}.\label{eq:T}\end{aligned}$$ There is a degree-one characteristic diffeomorphism $\eta(t,\cdot)$ for exactly $T_-<t<T_+$, normalized up to a common translation, such that $$\label{eq:formulas}
 \eta_a=F^2,\qquad
 u_x(t,\eta(t,a))=\frac{2F_t}{F}
 =\frac{-\sqrt E\sin(\sqrt E t/2)+w_0(a)\cos(\sqrt E t/2)}{F(t,a)}.$$ The first positive breaking labels are exactly $\operatorname*{argmin}w_0$; all of them break simultaneously. At each such label, $$\label{eq:rate}
 u_x(t,\eta(t,a))=-\frac2{T_+-t}+O(1)
 \quad(t\uparrow T_+).$$ Backward degeneration occurs exactly at $\operatorname*{argmax}w_0$ and time $T_-$. No earlier degeneration occurs in either direction.

Equation [\[eq:HS\]](#eq:HS){reference-type="eqref" reference="eq:HS"} yields along $\eta_t=u(t,\eta)$ the Riccati equation $$\dot w=-\frac12(w^2+E),\qquad w(t,a)=u_x(t,\eta(t,a)).$$ Its solution is $w=2F_t/F$. Since $\dot\eta_a=w\eta_a$ and $\eta_a(0,a)=1$, this gives $\eta_a=F^2$. Moreover $$\int_{\mathbb T}F^2\,da=\cos^2\frac{\sqrt Et}{2}
 +\sin^2\frac{\sqrt Et}{2}=1,$$ because $\int w_0=0$ and $\int w_0^2=E$. Conversely this identity makes the construction explicit: set $$\eta(t,a)=b(t)+\int_0^aF(t,s)^2\,ds,
 \qquad u(t,\eta(t,a))=\eta_t(t,a),$$ where $b(0)=0$ and $b'(0)=u_0(0)$. Then $\eta(0,a)=a$, $u(0,a)=u_0(a)$, and differentiating in $a$ gives $u_x\circ\eta=\eta_{ta}/\eta_a=2F_t/F$. Its Riccati equation is precisely [\[eq:HS\]](#eq:HS){reference-type="eqref" reference="eq:HS"} along every characteristic. The free common translation $b(t)$ is the harmless additive gauge. Thus the construction is a degree-one circle diffeomorphism exactly while $F$ is positive.

For fixed $t>0$ before the first pole, $F$ is increasing in $w_0$. Its first zero is therefore attained precisely where $w_0=m$, and solving $F=0$ gives $T_+$. Reversing time makes the maximum decisive and gives $T_-$. At a future first label, $F(T_+,a)=0$ and $F_t(T_+,a)\ne0$. Thus $2F_t/F=2/(t-T_+)+O(1)$, proving [\[eq:rate\]](#eq:rate){reference-type="eqref" reference="eq:rate"} and the complete label statement.

\>0

# Energy, degeneracies, and the endpoint

The same representation closes the conservation law without dividing by the Jacobian at its endpoint: $$\label{eq:energy}
 w(t,a)^2\eta_a(t,a)=E\left[-\sin\frac{\sqrt Et}{2}
 +\frac{w_0(a)}{\sqrt E}\cos\frac{\sqrt Et}{2}\right]^2.$$ Integrating [\[eq:energy\]](#eq:energy){reference-type="eqref" reference="eq:energy"}, the mixed term vanishes and the remaining two terms sum to $E$. Consequently $\int_{\mathbb T}u_x^2\,dx=E$ throughout $(T_-,T_+)$, consistently closing [\[eq:HS\]](#eq:HS){reference-type="eqref" reference="eq:HS"}.

If $E=0$, then $w_0=0$ and the solution is spatially constant; neither formula in [\[eq:T\]](#eq:T){reference-type="eqref" reference="eq:T"} is interpreted by division through zero. A flat interval or several isolated points may realize the global minimum, and Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"} includes the entire minimizing set rather than a generic singleton. At $t=T_+$ the map ceases to be a diffeomorphism. This paper neither constructs nor selects a conservative, dissipative, or other weak continuation.

\>1

# Asymmetric audit and Route-A boundary

Single harmonics cannot detect an accidental exchange of $m$ and $M$. For $\theta=2\pi k a$, take $$w_0=\cos\theta+\tfrac12\cos2\theta
     =(\cos\theta+\tfrac12)^2-\tfrac34.$$ Then $E=5/8$, $M=3/2$ occurs at $k$ labels, and $m=-3/4$ occurs at $2k$ labels. Its negative swaps the extrema and multiplicities. The certificate checks both signs for $k=1,2,3$, in addition to twelve Pythagorean single harmonics. It records 2,354 scalar leaves. The producer-independent checker performs 3,857 checks, SymPy closes 1,508 identities, two isolated replays are byte exact, and 60 hostile mutations are rejected. These are convention regressions; the proof above covers all declared data.

The nearest registered models have different mechanisms: C195 is viscous Burgers smoothing, C256 is dispersive KdV cnoidal motion, and C278 is a finite-dimensional Camassa--Holm two-peakon weak manifold.

Under `NO_BAD_EULER_OR_ROOT_NUMBER`, the strict tuple is $$(\mathrm{A0\_FAIL},\mathrm{A1\_FAIL},\mathrm{A2\_FAIL},
  \mathrm{A3\_FAIL},\mathrm{A4\_FORMAL\_HINT}).$$ The geometric interpretation is only a formal hint. There is no arithmetic prime owner, primitive-orbit Euler ledger, Euler product, target functional equation, counting law, target-zero match, or Hilbert--Pólya operator. Route A is rejected and Route B stays locked. No target local data, root number, or automorphy is claimed.

#### AI use.

A generative language model assisted drafting and code scaffolding. The displayed proof, independent recomputation, hostile tests, and deterministic artifacts define the audit record.

# Source lineage {#source-lineage .unnumbered}

9 J. K. Hunter and R. Saxton, "Dynamics of director fields," *SIAM J. Appl. Math.* 51 (1991), 1498--1521. DOI: [10.1137/0151075](https://doi.org/10.1137/0151075). J. Lenells, "The Hunter--Saxton Equation: A Geometric Approach," *SIAM J. Math. Anal.* 40 (2008), 266--277. DOI: [10.1137/050647451](https://doi.org/10.1137/050647451). Z. Yin, "On the Structure of Solutions to the Periodic Hunter--Saxton Equation," *SIAM J. Math. Anal.* 36 (2004), 272--283. DOI: [10.1137/S0036141003425672](https://doi.org/10.1137/S0036141003425672).
