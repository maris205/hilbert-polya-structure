---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-reflection-boundary-mahler-pressure"
canonical_tex: "henon_dynamics/henon_reflection_boundary_mahler_pressure/paper/paper.tex"
canonical_pdf: "henon_dynamics/henon_reflection_boundary_mahler_pressure/paper/paper.pdf"
source_sha256: "793af31c793bcf274616d1b2787a580e14666eb62e037bdbd0f103a76e97ea87"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Reflection-Boundary Equidistribution and Extensive Mahler Packet Pressure for a Hénon Horseshoe

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_reflection_boundary_mahler_pressure>)
- [规范 TeX](<../../../../../henon_dynamics/henon_reflection_boundary_mahler_pressure/paper/paper.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_reflection_boundary_mahler_pressure/paper/paper.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_reflection_boundary_mahler_pressure/README.md>)
- [BibTeX](<../../../../../henon_dynamics/henon_reflection_boundary_mahler_pressure/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For the area-preserving Hénon map $H(x,y)=(6-x^2-y,x)$, previous full-horseshoe and algebraic-exhaustion results make every odd primitive mixed-axis coordinate divisor reduced, totally real, and of degree $D_n=\sum_{d\mid n}\mu(n/d)2^{(d+1)/2}$. Ordinary coordinate Weil height is uniformly bounded, so its fixed-parameter pressure is flat. We identify the correct extensive packet limit. Primitive coordinates sampled at their marked reflection axis converge to a non-invariant reflection-boundary Bernoulli measure, while time-averaging the same selected orbits converges to the invariant maximal-entropy Bernoulli measure. The marked limit implies convergence of normalized logarithmic Mahler measures and a nonconstant linear packet pressure $$\lim_{\substack{n\to\infty\\ n\ \mathrm{odd}}}
   \frac1n\log\!\left(D_ne^{-snD_n^{-1}\log M(\widetilde\Psi_n)}\right)
   =\frac12\log2-s\kappa_J,$$ where $0<\kappa_J\le\log(1+\sqrt7)$. Exact symbolic enumeration through period $21$ and independent primitive-polynomial diagnostics through period $11$ accompany the theorem. The result is a packet-level thermodynamic statement; it does not prove an individual height pressure, a prime trace, or a Hilbert--Pólya operator.
author:
- |
  Liang Wang\
  School of Artificial Intelligence and Automation\
  Huazhong University of Science and Technology\
  Wuhan 430074, P. R. China
bibliography:
- references.bib
date: 'August 15, 2026'
title: |
  Reflection-Boundary Equidistribution and\
  Extensive Mahler Packet Pressure for a Hénon Horseshoe
```

## Markdown 正文

# Introduction

Consider the scaled Hénon automorphism $$\label{eq:H}
 H(x,y)=(6-x^2-y,x).$$ It is linearly conjugate to the repository normalization $(q,p)\mapsto(1-6q^2-p,q)$. Arai's certified hyperbolic plateau [@Arai2007] transports the Devaney--Nitecki full-shift horseshoe [@DevaneyNitecki1979] to parameter $6$. Combining this with the Friedland--Milnor complex fixed-point count [@FriedlandMilnor1989] exhausts every complex periodic point by the real full two-shift. In particular, the odd mixed-axis primitive coordinate polynomial is reduced, effective and totally real.

The integral recurrence $$\label{eq:recurrence}
 x_{j+1}=6-x_j^2-x_{j-1}$$ gives the sharp periodic bound $|x_j|\le1+\sqrt7$. Thus an ordinary fixed-parameter height weight is non-extensive. The first natural repair is the packet-average Mahler mass $$\label{eq:an-intro}
 a_n=\frac1{D_n}\log M(\widetilde\Psi_n),$$ multiplied by the period clock $n$.

A subtlety appears before pressure: mixed-axis roots are marked at a reflection axis. They are sparse, symmetry-centered points rather than generic marked periodic points. We prove that their axis distribution is a reflected one-sided Bernoulli process, not the invariant two-sided Bernoulli measure. Time-averaging the same orbits does recover maximal entropy. This separation is the main structural result and prevents a false identification of the two Mahler slopes.

# Equivariant full-shift coding

Define the involution $$\label{eq:J}
 J(x,y)=(x,6-x^2-y).$$ Then $J^2=1$ and $JHJ=H^{-1}$. Let $\sigma$ be the left shift on $\{-,+\}^{\mathbb Z}$ and let $$\label{eq:rho}
 (\rho\omega)_k=\omega_{-k}.$$

[\[lem:equivariant\]]{#lem:equivariant label="lem:equivariant"} There is a homeomorphism $\pi:\{-,+\}^{\mathbb Z}\to\Lambda$, where $\Lambda$ is the real chain recurrent set of [\[eq:H\]](#eq:H){reference-type="eqref" reference="eq:H"}, such that $$\label{eq:equivariant}
 \pi\sigma=H\pi,\qquad \pi\rho=J\pi.$$

At a Devaney--Nitecki large-parameter anchor, the sign itinerary is a one-to-one full-shift coding. Since $J$ preserves the first coordinate and $H^kJ=JH^{-k}$, that coding intertwines $J$ with [\[eq:rho\]](#eq:rho){reference-type="eqref" reference="eq:rho"}.

Continue the basic set and its conjugacy along Arai's connected uniformly hyperbolic plateau from the anchor to parameter $6$. Choose the structural continuation $h_a$ in the standard small-neighborhood normalization. Both $h_a$ and $J_a h_aJ_{10}$ conjugate the anchor dynamics to the parameter-$a$ dynamics and are close to the identity. Expansivity gives uniqueness in this normalization, so $J_a h_aJ_{10}=h_a$. Composing the anchor itinerary with $h_6$ proves [\[eq:equivariant\]](#eq:equivariant){reference-type="eqref" reference="eq:equivariant"}.

This is a specialization of standard symbolic/hyperbolic continuation machinery; @LindMarcus1995 gives symbolic background, and @Kang2018 gives broader reversible-periodic context. Neither source is used to assert the counting or limit theorem below.

# Reflection half-words and primitive removal

Fix an odd integer $n=2m+1$. The intersection $\operatorname{Fix}(\sigma^n)\cap\operatorname{Fix}(\rho)$ consists of the words $$\label{eq:palindrome}
 (\omega_0,\omega_1,\ldots,\omega_m,
  \omega_m,\ldots,\omega_1),$$ so it has cardinality $2^{m+1}$. Under [\[lem:equivariant\]](#lem:equivariant){reference-type="ref" reference="lem:equivariant"}, these are exactly the marked points in $\operatorname{Fix}(H^n)\cap\operatorname{Fix}(J)$. The mixed-axis closure has degree $2^{m+1}$ and consists of simple points, so no symbolic point or algebraic root is missing.

Let $\Omega_n^{\mathrm{prim}}$ denote the exact-period subset and put $$\label{eq:Dn}
 D_n=\#\Omega_n^{\mathrm{prim}}
 =\sum_{d\mid n}\mu(n/d)2^{(d+1)/2}.$$

[\[lem:primitive\]]{#lem:primitive label="lem:primitive"} If $U_n=\operatorname{Fix}(\sigma^n)\cap\operatorname{Fix}(\rho)$, then $$\label{eq:primitive-bound}
 \frac{\#(U_n\setminus\Omega_n^{\mathrm{prim}})}{\#U_n}
 \le \tau(n)2^{-n/3}.$$ Consequently uniform measure on $U_n$ and on $\Omega_n^{\mathrm{prim}}$ differ in total variation by a quantity tending exponentially to zero.

Every proper divisor $d$ of an odd integer $n$ satisfies $d\le n/3$. Bounding all lower-period contributions by $\sum_{d\mid n,d<n}2^{(d+1)/2}$ and dividing by $2^{(n+1)/2}$ gives [\[eq:primitive-bound\]](#eq:primitive-bound){reference-type="eqref" reference="eq:primitive-bound"}. The total variation identity follows because the primitive family is a subset of the full family.

In particular, $$\label{eq:entropy}
 \lim_{\substack{n\to\infty\\n\ \mathrm{odd}}}\frac1n\log D_n
 =\frac12\log2.$$

# Two different weak-star limits

Let $\eta_n$ be uniform measure on $\Omega_n^{\mathrm{prim}}$, with the reflection axis marked at coordinate zero. Let $(\xi_k)_{k\ge0}$ be iid fair signs and form a two-sided sequence by $$\label{eq:boundary-process}
 \omega_k=\omega_{-k}=\xi_k\qquad(k\ge0).$$ Denote its law by $\eta_J$.

[\[thm:axis\]]{#thm:axis label="thm:axis"} As odd $n$ tends to infinity, $$\label{eq:axis-limit}
 \eta_n\stackrel{*}{\longrightarrow}\eta_J.$$ The limit is not shift invariant and is not the fair two-sided Bernoulli measure $\mu_B$.

For a fixed cylinder radius $r$ and $n>2r$, the free coordinates $\omega_0,\ldots,\omega_r$ in [\[eq:palindrome\]](#eq:palindrome){reference-type="eqref" reference="eq:palindrome"} are independent fair signs. The negative coordinates are their reflected copies. This proves cylinder convergence for the full family; [\[lem:primitive\]](#lem:primitive){reference-type="ref" reference="lem:primitive"} transfers it to the primitive family.

Under $\eta_J$, the event $\{\omega_{-1}=\omega_1\}$ has probability one, whereas it has $\mu_B$-probability $1/2$. After applying one shift, the same event pulls back to $\{\omega_0=\omega_2\}$, which has $\eta_J$-probability $1/2$. Hence $\eta_J$ is not shift invariant.

Now erase the distinguished axis by averaging over each cyclic orbit: $$\label{eq:orbit-average}
 \bar\eta_n=\frac1n\sum_{j=0}^{n-1}(\sigma^j)_*\eta_n.$$

[\[thm:orbit\]]{#thm:orbit label="thm:orbit"} For odd $n\to\infty$, $$\label{eq:orbit-limit}
 \bar\eta_n\stackrel{*}{\longrightarrow}\mu_B.$$ More precisely, for a cylinder $C$ depending on coordinates $[-r,r]$, $$\label{eq:cylinder-bound}
 |\bar\eta_n(C)-\mu_B(C)|
 \le \frac{4r+1}{n}+\tau(n)2^{-n/3}.$$

First use all palindromes. A window centered at $j$ contains two positions paired by reflection only if $2j\equiv-(a+b)\pmod n$ for some $a,b\in[-r,r]$. Because $n$ is odd, each value of $a+b\in[-2r,2r]$ produces at most one bad center, so there are at most $4r+1$. At every other center the window reads distinct free half-word coordinates and has exactly the fair Bernoulli law. Average over centers and then apply [\[lem:primitive\]](#lem:primitive){reference-type="ref" reference="lem:primitive"}.

# Extensive packet pressure

Write $x(z)$ for the first scaled coordinate and set $$\label{eq:phi}
 \phi(z)=\log^{+}|x(z)|.$$ This is continuous on the compact horseshoe and satisfies $0\le\phi\le\log(1+\sqrt7)$. Define $$\label{eq:kappas}
 \kappa_J=\int\phi\,d(\pi_*\eta_J),\qquad
 \kappa_{\max}=\int\phi\,d(\pi_*\mu_B).$$

[\[prop:kappa-positive\]]{#prop:kappa-positive label="prop:kappa-positive"} One has $$\label{eq:kappa-bound}
 0<\kappa_J\le\log(1+\sqrt7).$$

The upper bound is immediate. The constant negative itinerary represents the fixed point with first coordinate $-1-\sqrt7$. By continuity, a finite cylinder around this sequence has $\phi>0$. That cylinder has positive $\eta_J$-measure, proving strict positivity.

Let $\widetilde\Psi_n\in\mathbb Z[T]$ be the monic integral primitive coordinate polynomial. Total reality and squarefreeness give $$\label{eq:mahler}
 a_n:=\frac1{D_n}\log M(\widetilde\Psi_n)
 =\frac1{D_n}\sum_{\widetilde\Psi_n(\alpha)=0}\log^{+}|\alpha|.$$ The right side is the $\phi$-average under $\pi_*\eta_n$.

[\[thm:pressure\]]{#thm:pressure label="thm:pressure"} For every fixed $s\in\mathbb R$, $$\label{eq:packet-pressure}
 \lim_{\substack{n\to\infty\\n\ \mathrm{odd}}}
 \frac1n\log\left(D_n\exp(-sn a_n)\right)
 =\frac12\log2-s\kappa_J.$$ This pressure is nonconstant.

By [\[thm:axis\]](#thm:axis){reference-type="ref" reference="thm:axis"} and continuity, $a_n\to\kappa_J$. Combine this with [\[eq:entropy\]](#eq:entropy){reference-type="eqref" reference="eq:entropy"}. Nonconstancy follows from [\[prop:kappa-positive\]](#prop:kappa-positive){reference-type="ref" reference="prop:kappa-positive"}.

Similarly, define $$\label{eq:bn}
 b_n=\frac1{nD_n}\sum_{\alpha}\sum_{j=0}^{n-1}
 \phi(H^jz_\alpha),$$ where $z_\alpha\in\operatorname{Fix}(J)$ is the point with first coordinate $\alpha$. Then [\[thm:orbit\]](#thm:orbit){reference-type="ref" reference="thm:orbit"} gives $b_n\to\kappa_{\max}$ and $$\label{eq:orbit-pressure}
 \lim\frac1n\log\left(D_n\exp(-sn b_n)\right)
 =\frac12\log2-s\kappa_{\max}.$$

# Executable certificate

The primary certificate enumerates every primitive palindrome through odd period $21$. For radius-two cylinders, the marked-axis total variation from fair Bernoulli stabilizes at $3/4$, whereas the orbit-averaged values decrease toward zero. It independently rebuilds the primitive integral polynomials and reports the diagnostics in [1](#tab:numerics){reference-type="ref" reference="tab:numerics"}.

::: {#tab:numerics}
    $n$   marked Mahler average       orbit average
  ----- ----------------------- -------------------
      1       0.895879734614027   0.895879734614027
      3       0.693147180559945   0.767528364331349
      5       0.592642696019558   0.775457104945456
      7       0.648968099586674   0.786446733777541
      9       0.660700003269176   0.790519108637561
     11       0.670373466816018   0.789976524363231

  : Finite diagnostics. These decimals are not used to prove [\[thm:axis,thm:orbit,thm:pressure\]](#thm:axis,thm:orbit,thm:pressure){reference-type="ref" reference="thm:axis,thm:orbit,thm:pressure"}.
:::

A second implementation uses a different least-period test through period $17$ and the exact period-one/three polynomial sentinels. Normal and optimized test runs agree, and 26 contract mutations are rejected.

# Claim boundary and next theorem

The pressure in [\[eq:packet-pressure\]](#eq:packet-pressure){reference-type="eqref" reference="eq:packet-pressure"} weights the complete packet by its average Mahler mass. It is not the individual partition $\sum_\alpha e^{-sn h(\alpha)}$. If $\widetilde\Psi_n$ factors, different factors may have different Weil heights; weak convergence of all roots does not control that finer distribution.

The finite rows suggest $\kappa_J\ne\kappa_{\max}$, but a theorem requires certified cylinder enclosures and a tail estimate for [\[eq:phi\]](#eq:phi){reference-type="eqref" reference="eq:phi"}. No prime-power family, von Mangoldt amplitude, determinant continuation, self-adjoint operator, zeta-zero correspondence, or Riemann-hypothesis statement is obtained here.

# Conclusion

The reflection slice supports a genuine extensive packet pressure, but its natural marked measure is a boundary process rather than an invariant equilibrium state. Orbit averaging restores maximal entropy. This distinction turns a false shortcut into two exact limit theorems and isolates a concrete next task: rigorously separate the two Hénon Mahler slopes.
