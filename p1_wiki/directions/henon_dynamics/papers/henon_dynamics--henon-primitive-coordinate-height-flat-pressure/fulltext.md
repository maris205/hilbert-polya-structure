---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-primitive-coordinate-height-flat-pressure"
canonical_tex: "henon_dynamics/henon_primitive_coordinate_height_flat_pressure/paper/paper.tex"
canonical_pdf: "henon_dynamics/henon_primitive_coordinate_height_flat_pressure/paper/paper.pdf"
source_sha256: "845a261a77bafddb2a6ec0f56e8f28ea95d2e16196b57d53da67da95d075563e"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Primitive Coordinate Heights and a Flat-Pressure Obstruction for the Area-Preserving Hénon Map

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_primitive_coordinate_height_flat_pressure>)
- [规范 TeX](<../../../../../henon_dynamics/henon_primitive_coordinate_height_flat_pressure/paper/paper.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_primitive_coordinate_height_flat_pressure/paper/paper.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_primitive_coordinate_height_flat_pressure/README.md>)
- [BibTeX](<../../../../../henon_dynamics/henon_primitive_coordinate_height_flat_pressure/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For the area-preserving Hénon map $H_6(q,p)=(1-6q^2-p,q)$, previous all-period results make every odd primitive mixed-axis divisor reduced, effective, and totally real. This invites a pressure formed by weighting each primitive root with its absolute logarithmic Weil height. We prove that this pressure is necessarily flat. After the integral scaling $x=6q$, every primitive root is an algebraic integer and all its conjugates are real periodic coordinates. A maximum principle for the cyclic recurrence gives the sharp uniform bound $|x|\le1+\sqrt7$, hence $h(x)\le\log(1+\sqrt7)$ at every period. The height-weighted root count therefore differs from its unweighted degree by only a period-independent factor. Its pressure is exactly $\frac12\log2$ for every fixed real height parameter. Exact finite certificates reconstruct the scaled primitive polynomials through odd period 11 and independently verify the root bound through period 9. The result is a normalization obstruction, not an arithmetic promotion: a nontrivial next pressure must use an extensive observable such as period times height, packet Mahler height, or discriminant/ramification height.
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
  Primitive Coordinate Heights and a Flat-Pressure\
  Obstruction for the Area-Preserving Hénon Map
```

## Markdown 正文

# Introduction

Arithmetic dynamics routinely uses absolute Weil height to measure the complexity of algebraic points; see, for example, @Silverman2007. In a periodic-orbit pressure, however, the relevant weight must also be extensive in the orbit clock. These two roles need not agree.

This paper isolates that mismatch for the frozen map $$\label{eq:H6}
H_6(q,p)=(1-6q^2-p,q).$$ Earlier work combines the hyperbolic plateau of @Arai2007, the large-parameter full horseshoe of @DevaneyNitecki1979, and the complex fixed-point count of @FriedlandMilnor1989. At the parameter in [\[eq:H6\]](#eq:H6){reference-type="eqref" reference="eq:H6"}, every complex periodic point is a distinct real hyperbolic point. Consequently every odd mixed-axis primitive divisor is squarefree, effective, and totally real.

The next proposed object was $$\label{eq:proposed}
\mathcal P_{\rm coord}(s)
=\limsup_{\substack{n\to\infty\\n\ {m odd}}}
\frac1n\log\sum_{\widetilde\Psi_n(\alpha)=0}
e^{-sh(\alpha)},$$ where $\widetilde\Psi_n$ is the integrally scaled primitive polynomial. Our main result shows that [\[eq:proposed\]](#eq:proposed){reference-type="eqref" reference="eq:proposed"} contains no new pressure information: it is identically the unweighted half entropy.

# Frozen primitive divisor and integral model

Put $x=6q$ and $y=6p$. The conjugate map is $$\label{eq:integral-map}
(x,y)\longmapsto(6-x^2-y,x),$$ and a cyclic period-$n$ orbit satisfies $$\label{eq:recurrence}
x_{j+1}=6-x_j^2-x_{j-1}.$$ The cyclic equations are monic in $x_j^2$ with pairwise coprime leading monomials. Their quotient algebra is therefore finite free over $\mathbb Z$, with squarefree standard-monomial basis. In particular every periodic coordinate is an algebraic integer.

For odd $n$, let $\Psi_n(X)\in\mathbb Q[X]$ be the monic primitive mixed-axis quotient established in the preceding reflection-divisor work, and write $D_n=\deg\Psi_n$. Define $$\label{eq:scaled-poly}
\widetilde\Psi_n(T)=6^{D_n}\Psi_n(T/6).$$ Every root of [\[eq:scaled-poly\]](#eq:scaled-poly){reference-type="eqref" reference="eq:scaled-poly"} is an algebraic integer. Since the polynomial is monic with rational coefficients, its coefficients are rational algebraic integers and hence ordinary integers. The previous algebraic-exhaustion theorem also makes it squarefree and totally real.

The exact primitive degree is $$\label{eq:degree}
D_n=\sum_{d\mid n}\mu(n/d)2^{(d+1)/2}
=2^{(n+1)/2}+O\!\left(n2^{n/6+1/2}\right).$$ Thus $$\label{eq:degree-entropy}
\lim_{\substack{n\to\infty\\n\ {m odd}}}\frac1n\log D_n
=\frac12\log2.$$

# A sharp uniform bound for every conjugate

[\[lem:max\]]{#lem:max label="lem:max"} Every coordinate on every real periodic orbit of [\[eq:integral-map\]](#eq:integral-map){reference-type="eqref" reference="eq:integral-map"} satisfies $$\label{eq:root-bound}
|x_j|\le B:=1+\sqrt7.$$ The constant is sharp.

Choose $j$ with $M=|x_j|$ maximal along the orbit. Equation [\[eq:recurrence\]](#eq:recurrence){reference-type="eqref" reference="eq:recurrence"} gives $$M^2=|6-x_{j-1}-x_{j+1}|\le6+2M.$$ Hence $M^2-2M-6\le0$, whose nonnegative endpoint is $1+\sqrt7$. For sharpness, the fixed-coordinate equation is $x^2+2x-6=0$; its negative root is $-1-\sqrt7$.

[\[cor:conjugate\]]{#cor:conjugate label="cor:conjugate"} If $\alpha$ is any root of $\widetilde\Psi_n$, every Galois conjugate $\sigma(\alpha)$ is real and satisfies $|\sigma(\alpha)|\le B$.

The minimal polynomial of $\alpha$ divides $\widetilde\Psi_n$. Hence every conjugate is another root of the same primitive divisor. Algebraic exhaustion identifies every such root with a real periodic coordinate, so Lemma [\[lem:max\]](#lem:max){reference-type="ref" reference="lem:max"} applies.

# Uniform Weil height

Let $h(\alpha)$ denote the absolute logarithmic Weil height. If $\alpha$ is an algebraic integer, its nonarchimedean contributions vanish, and $$\label{eq:height}
h(\alpha)=\frac1{[K:\mathbb Q]}
\sum_{\sigma:K\hookrightarrow\mathbb C}
\log\max\{1,|\sigma(\alpha)|\}$$ for any number field $K$ containing it.

[\[thm:height\]]{#thm:height label="thm:height"} For every odd period and every root of the scaled primitive divisor, $$\label{eq:height-bound}
0\le h(\alpha)\le C:=\log(1+\sqrt7).$$

Combine algebraic integrality with Corollary [\[cor:conjugate\]](#cor:conjugate){reference-type="ref" reference="cor:conjugate"} in [\[eq:height\]](#eq:height){reference-type="eqref" reference="eq:height"}.

The upper bound is deliberately uniform rather than asymptotic. It does not assert that the finite heights converge, nor that primitive polynomials stay irreducible.

# The flat-pressure theorem

For $s\in\mathbb R$, define the distinct-root partition function $$\label{eq:partition}
Z_n(s)=\sum_{\widetilde\Psi_n(\alpha)=0}e^{-sh(\alpha)}.$$ Squarefreeness ensures that each primitive root is counted once.

[\[thm:flat\]]{#thm:flat label="thm:flat"} For every fixed real $s$, the limit in [\[eq:proposed\]](#eq:proposed){reference-type="eqref" reference="eq:proposed"} exists and $$\label{eq:flat}
\mathcal P_{\rm coord}(s)=\frac12\log2.$$

Theorem [\[thm:height\]](#thm:height){reference-type="ref" reference="thm:height"} gives the uniform sandwich $$\label{eq:sandwich}
e^{-|s|C}D_n\le Z_n(s)\le e^{|s|C}D_n.$$ After taking logarithms and dividing by $n$, the two errors are bounded by $|s|C/n$. Equation [\[eq:degree-entropy\]](#eq:degree-entropy){reference-type="eqref" reference="eq:degree-entropy"} proves [\[eq:flat\]](#eq:flat){reference-type="eqref" reference="eq:flat"}.

The ordinary individual coordinate height cannot change the exponential primitive-root growth rate at any fixed $s$. In particular it cannot, by itself, generate a new pressure singularity or a nonconstant pressure curve.

[\[cor:scaling\]]{#cor:scaling label="cor:scaling"} Let $c\ne0$ be a fixed algebraic number and replace every root $\alpha$ in [\[eq:partition\]](#eq:partition){reference-type="eqref" reference="eq:partition"} by $c\alpha$. The resulting pressure is still $\frac12\log2$ for every fixed real $s$.

The standard height inequality $h(c\alpha)\le h(\alpha)+h(c)$ gives a period-independent upper bound. The same sandwich proof applies.

This conclusion is scoped to the observable in [\[eq:partition\]](#eq:partition){reference-type="eqref" reference="eq:partition"}. The weights $e^{-snh(\alpha)}$, a packet Mahler mass, and discriminant or ramification heights are different objects.

# Finite exact and numerical certificate

The executable package reconstructs the primitive quotient before applying [\[eq:scaled-poly\]](#eq:scaled-poly){reference-type="eqref" reference="eq:scaled-poly"}. Exact arithmetic verifies monic integral coefficients and factorization; 50-digit roots provide diagnostics only.

    $n$   $D_n$   $h$ (diagnostic)   $\max|\alpha|$ (diagnostic)
  ----- ------- ------------------ -----------------------------
      1       2     0.895879734614                3.645751311065
      3       2     0.693147180560                3.236067977500
      5       6     0.592642696020                3.353191857132
      7      14     0.648968099587                3.605741786740
      9      28     0.660700003269                3.640173216825
     11      62     0.670373466816                3.644971653259

  : Finite primitive scaled-coordinate diagnostics. Heights are factor heights; all displayed finite polynomials are irreducible, a fact not promoted beyond the table.

The first two exact polynomials are $$T^2+2T-6,\qquad T^2-2T-4.$$ Their heights are $(1/2)\log6$ and $\log2$, respectively. An independent implementation reconstructs periods through 9 and uses exact rational Sturm intervals. The endpoint root at period 1 is checked by exact equality rather than by a false strict interval. Ordinary and optimized test runs agree, and all 24 hostile mutations are rejected.

# What the next pressure must measure

Theorem [\[thm:flat\]](#thm:flat){reference-type="ref" reference="thm:flat"} identifies a missing clock factor. Three natural repairs remain:

1.  the extensive individual weight $e^{-snh(\alpha)}$;

2.  a packet weight built from $\log M(\widetilde\Psi_n)=\sum_\alpha\log^+|\alpha|$;

3.  discriminant, different, or ramification height, which measures conjugate interaction rather than one bounded coordinate.

The first two invite an equidistribution theorem for the complete reflection root ensemble under the full two-shift. None automatically supplies a rational-prime label or von Mangoldt amplitude.

# Route evaluation and claim boundary

At Route A, the all-period primitive population remains analytic and exact, but the tested height pressure is a proved obstruction rather than an arithmetic bridge. We record $$(A1_{\rm analytic},A2_{\rm inherited},A3_{\rm partial},A4_{\rm formal}),$$ with overall status `ROUTE_A_EXPLORATORY`. Route B is not testable: there is no proposed Hilbert space, operator domain, self-adjoint realization, prime-power trace, or completed-$\xi$ determinant.

No result here proves a prime correspondence, a Hilbert--Pólya realization, the Riemann hypothesis, or even a nontrivial extensive height pressure.

# Conclusion

The complete real algebraic exhaustion of the Hénon periodic points makes a simple recurrence estimate unexpectedly decisive. Ordinary primitive coordinate heights stay bounded while the root population grows exponentially, forcing the corresponding pressure to be flat. This closes a misnormalized all-period bridge and replaces it with a sharper task: identify and control an extensive packet observable before attempting any arithmetic trace.
