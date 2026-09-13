---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-mellin-parity-obstruction"
canonical_tex: "henon_dynamics/henon_mellin_parity_obstruction/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_mellin_parity_obstruction/paper/main.pdf"
source_sha256: "62c17f83472ff70f705c6e980bff45ee1743415711ed191254c05f30c2a264b0"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Reciprocal and Critical-Line-Unitary, Yet Off-Line: A Certified Hénon Mellin--Scattering Obstruction

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_mellin_parity_obstruction>)
- [规范 TeX](<../../../../../henon_dynamics/henon_mellin_parity_obstruction/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_mellin_parity_obstruction/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_mellin_parity_obstruction/README.md>)
- [BibTeX](<../../../../../henon_dynamics/henon_mellin_parity_obstruction/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We prove that a natural Hénon Mellin--scattering candidate fails despite having the two formal symmetries most often associated with a spectral functional equation. The cubic phase $P_6(u)=2u^3-u$ yields a forced two-sign Mellin matrix whose parity scattering ratio satisfies $S_H(z)S_H(1-z)=I$ and is unitary on $\mathop{\mathrm{Re}}z=1/2$. We derive its meromorphic hypergeometric continuation and use complex-ball arithmetic together with an analytic Rouché estimate to certify exactly one simple zero of the zeta-even channel in the disc of radius $10^{-12}$ centered at $0.7286922241147175+1.6054479123346985i$. Full-disc lower bounds exclude the mirror, odd-channel, and linear-parent cancellations, while direct ball evaluation proves that the completed Riemann function is nonzero there. The scattering determinant therefore acquires a pole--zero quartet inside the open critical strip and off the critical line. This rejects the unrenormalized candidate at the divisor gate and shows that reciprocity plus critical-line unitarity does not control an RH-compatible divisor. We also prove that Mellin diagonalization does not furnish an ordinary Fredholm determinant, then identify a sharper alternative: a homogeneous Hénon deformation whose strip-safe symbol reduces the problem to a Poisson-boundary index or anomaly.
author:
- Anonymous Research Note
bibliography:
- references.bib
date: 13 August 2026
title: |
  Reciprocal and Critical-Line-Unitary, Yet Off-Line:\
  A Certified Hénon Mellin--Scattering Obstruction
```

## Markdown 正文

# Introduction

A useful Hilbert--Pólya candidate must do more than reproduce the visual symmetries of the completed zeta function. Its determinant or scattering function must also have the right divisor. This distinction is easy to state and surprisingly easy to lose when a construction automatically produces both a $z\leftrightarrow1-z$ relation and unitarity on the critical line.

We test that distinction on a natural Mellin reduction of an area-preserving Hénon system. The underlying map is $$\label{eq:h6}
H_6(q,p)=(1-6q^2-p,q),$$ with cubic generating phase $P_6(q)=2q^3-q$. Earlier work in this project placed its cubic chirp in an adelic Poisson/scaling architecture. Dilation does not produce finitely many static boundary functionals; it produces the full family $P_a(x)=P_6(ax)$. Mellin transformation is therefore the intrinsic way to diagonalize the scaling variable.

The resulting two-sign symbol looks promising. In a parity basis its formal scattering matrix is $$\label{eq:scattering-intro}
S_H(z)=\operatorname{diag}\left(
\frac{A(1-z)}{A(z)},\frac{B(1-z)}{B(z)}
\right).$$ Both reciprocity and critical-line unitarity follow exactly. The decisive calculation, however, goes the other way: the zeta-relevant even factor $A$ has a certified simple zero away from the critical line. The companion factors do not cancel it, so [\[eq:scattering-intro\]](#eq:scattering-intro){reference-type="eqref" reference="eq:scattering-intro"} has an additional pole and mirror zero in the strip.

Our contributions are concrete and falsifiable.

1.  We derive a meromorphic hypergeometric continuation, a three-step recurrence, and the forced parity decomposition of the cubic Mellin symbol.

2.  We certify one simple even-channel zero in an explicit rational disc using Arb enclosures and a global second-derivative majorant. The exact Rouché margin is more than three orders of magnitude larger than the remainder bound.

3.  We certify that the mirror, odd, and natural linear-parent factors are nonzero on the relevant discs, and that the completed Riemann function is nonzero there. The scattering divisor is therefore genuinely additional.

4.  We separate the pointwise matrix determinant from an ordinary Fredholm determinant and use the failure to select a new large gate: an index or anomaly for the homogeneous cubic on the Poisson boundary quotient.

The analysis uses only the Hénon phase and interval arithmetic. It does not inspect a Riemann-zero table or fit a spectral correspondence. The negative result is consequently a structural filter, not a failed numerical match.

# Context and claim boundary

#### Hénon dynamics and scaling.

The source Hénon model motivates an area-preserving quadratic map and its cubic generating function [@Wang2026HenonModel]. The immediate input to this paper is the exact Poisson boundary identity for its adelic chirp. Under dilation, $$\label{eq:dilation}
D_aM_{P_6}D_a^{-1}=M_{P_a},
\qquad P_a(x)=2a^3x^3-ax=P_6(ax).$$ The coefficient functionals indexed by $a$ span an infinite-dimensional space before the Poisson map. A finite static projection-rank bound cannot therefore be promoted to a finite-channel dynamical theorem. Equation [\[eq:dilation\]](#eq:dilation){reference-type="eqref" reference="eq:dilation"} instead points to Mellin transformation in $a$.

#### Mellin and Poisson analysis.

Mellin continuation, contour rotation, and generalized hypergeometric functions are classical tools; we follow standard conventions summarized by the NIST Digital Library of Mathematical Functions [@DLMFMellin; @DLMFHyper]. The adelic Poisson/scaling framework and its spectral interpretation originate in the Connes program [@Connes1999; @ConnesConsani2020]. We do not claim those mechanisms as new. Our question is narrower: what divisor is forced when the Hénon cubic boundary family is Mellin diagonalized without fitted normalization?

#### Certified complex analysis.

The proof uses Arb midpoint-radius arithmetic through the python-flint interface. Arb provides rigorous enclosures rather than ordinary floating-point estimates [@Johansson2017Arb]. The software evaluation is only one part of the proof: a symbolic contour formula and an analytic second-derivative majorant convert the enclosures into a Rouché count.

#### Scope.

We call $S_H$ a *formal scattering symbol*. No wave operators, trace-class resolvent difference, or Hilbert-space scattering pair is constructed here. The word "determinant" refers to the pointwise $2\times2$ matrix determinant unless explicitly qualified. These distinctions prevent a symbol-level functional equation from being mistaken for a Hilbert--Pólya operator theorem.

# The exact Mellin--parity symbol

For $\sigma\in\{+1,-1\}$, define initially by oscillatory continuation $$\label{eq:kappa}
\kappa_\sigma(z)=\int_0^\infty
e^{\sigma2\pi i(2u^3-u)}u^{z-1}\,du.$$ The two half-lines force the symmetric matrix $$\label{eq:K}
K(z)=\begin{pmatrix}\kappa_+(z)&\kappa_-(z)\\
\kappa_-(z)&\kappa_+(z)\end{pmatrix}.$$ Its parity eigen-symbols are $$\label{eq:AB}
A(z)=\kappa_+(z)+\kappa_-(z),\qquad
B(z)=\frac{\kappa_+(z)-\kappa_-(z)}{i}.$$

[\[prop:continuation\]]{#prop:continuation label="prop:continuation"} Let $\lambda=2\pi/(4\pi)^{1/3}$ and $X=-2\pi^2/27$. Then $$\begin{aligned}
\kappa_\sigma(z)
=\frac{(4\pi)^{-z/3}e^{\sigma i\pi z/6}}3\Bigg[&
\Gamma(z/3){}_1F_2(z/3;1/3,2/3;X)\notag\\
&+\lambda e^{-\sigma i\pi/3}\Gamma((z+1)/3)
{}_1F_2((z+1)/3;2/3,4/3;X)\notag\\
&+\frac{\lambda^2e^{-2\sigma i\pi/3}}2
\Gamma((z+2)/3){}_1F_2((z+2)/3;4/3,5/3;X)
\Bigg].\label{eq:hyper}\end{aligned}$$ Moreover, $$\label{eq:recurrence}
12\pi\kappa_\sigma(z+3)-2\pi\kappa_\sigma(z+1)
=\sigma iz\kappa_\sigma(z),$$ and $\kappa_-(z)=\overline{\kappa_+(\overline z)}$.

Rotate $u=e^{\sigma i\pi/6}r$. The cubic exponential becomes $e^{-4\pi r^3}$, while the linear term remains of exponential order one. Expanding the latter and integrating termwise gives a gamma series. Grouping indices modulo three gives [\[eq:hyper\]](#eq:hyper){reference-type="eqref" reference="eq:hyper"}. Integration by parts gives [\[eq:recurrence\]](#eq:recurrence){reference-type="eqref" reference="eq:recurrence"}; conjugation gives the final identity. Full estimates appear in [8](#app:majorant){reference-type="ref" reference="app:majorant"}.

The phase is odd, so $A$ is the cosine Mellin symbol and $B$ the sine Mellin symbol. Both are real-type. The formal parity scattering symbol $$\label{eq:SH}
S_H(z)=K(1-z)K(z)^{-1}
=\operatorname{diag}\left(\frac{A(1-z)}{A(z)},
\frac{B(1-z)}{B(z)}\right)$$ satisfies $$\label{eq:symmetries}
S_H(z)S_H(1-z)=I,
\qquad
S_H(1/2+it)^*S_H(1/2+it)=I,$$ wherever it is defined. The first identity is algebraic. For the second, $1-z=\overline z$ on the critical line and the parity symbols are real-type.

# A certified off-critical divisor

Set $$\label{eq:disc}
c=0.7286922241147175+1.6054479123346985i,
\qquad r=10^{-12},
\qquad \mathcal{D}=\{z:|z-c|\le r\}.$$ Both coordinates of $c$ and the radius are stored as exact rationals.

[\[thm:obstruction\]]{#thm:obstruction label="thm:obstruction"} The even symbol $A$ has exactly one zero, counted with multiplicity, in $\mathcal{D}$. That zero is simple. The disc lies in $0<\mathop{\mathrm{Re}}z<1$, is disjoint from $\mathop{\mathrm{Re}}z=1/2$, and satisfies $$\label{eq:nonzero}
\inf_{\mathcal{D}}|A(1-z)|>3/10,
\quad \inf_{\mathcal{D}}|B(z)|>4/5,
\quad \inf_{\mathcal{D}}|B(1-z)|>13/10.$$ For $$\label{eq:xi}
\xi(z)=\tfrac12z(z-1)\pi^{-z/2}\Gamma(z/2)\zeta(z),$$ one also has $\inf_{\mathcal{D}}|\xi(z)|>9/20$. Consequently $\det S_H$ has one pole in $\mathcal{D}$ and one zero in $1-\mathcal{D}$, plus their conjugates. All four are off the critical line in the open strip and are additional to the Riemann divisor.

Certified ball evaluation gives $$\label{eq:center-bounds}
|A(c)|<10^{-16},\qquad |A'(c)|>2/5.$$ The contour estimate in [8](#app:majorant){reference-type="ref" reference="app:majorant"} gives $\sup_{\mathcal{D}}|A''|<1200$. On $|z-c|=r$, $$\begin{aligned}
|A(z)-A'(c)(z-c)|
&\le |A(c)|+\tfrac12\sup_{\mathcal{D}}|A''|r^2\\
&<10^{-16}+600\cdot10^{-24}
<\tfrac25\,10^{-12}
\le |A'(c)(z-c)|.\end{aligned}$$ Rouché's theorem compares $A$ with the linear function $A'(c)(z-c)$, proving the zero count. Count one also proves simplicity. Complex-ball evaluation on the full input discs proves [\[eq:nonzero\]](#eq:nonzero){reference-type="eqref" reference="eq:nonzero"}. Direct Arb evaluation of [\[eq:xi\]](#eq:xi){reference-type="eqref" reference="eq:xi"} on the full disc gives the stated $9/20$ lower bound; no Riemann-zero table is read. The functional equation gives the corresponding nonvanishing on $1-\mathcal{D}$. The determinant identity $$\label{eq:detS}
\det S_H(z)=\frac{A(1-z)B(1-z)}{A(z)B(z)}$$ then gives the local divisor statement. Real-type symmetry gives the conjugates.

::: {#tab:bounds}
  Quantity                       Certified direction   Threshold
  ------------------------------ --------------------- ------------
  $|A(c)|$                       upper                 $10^{-16}$
  $|A'(c)|$                      lower                 $2/5$
  $\sup_{\mathcal{D}}|A''|$      upper                 $1200$
  $\inf_{\mathcal{D}}|A(1-z)|$   lower                 $3/10$
  $\inf_{\mathcal{D}}|B(z)|$     lower                 $4/5$
  $\inf_{\mathcal{D}}|B(1-z)|$   lower                 $13/10$
  $\inf_{\mathcal{D}}|\xi(z)|$   lower                 $9/20$

  : Release thresholds used by the independent certificate. The inequalities hold on full complex balls, not only at sampled points.
:::

The natural linear reference does not cancel the pole. Its even symbol is $$\label{eq:linear}
A_{\mathrm{lin}}(z)=2(2\pi)^{-z}\Gamma(z)\cos(\pi z/2),$$ and the certificate proves $\inf_{\mathcal{D}}|A_{\mathrm{lin}}|>7/10$. No Riemann-zero data enter this conclusion.

# Operator meaning and Route-A decision

The obstruction in [\[thm:obstruction\]](#thm:obstruction){reference-type="ref" reference="thm:obstruction"} concerns the most natural unrenormalized symbol. It does not assume that the symbol already comes from a complete scattering theory. In fact, a second obstruction prevents that promotion by the ordinary Fredholm route.

[\[prop:multiplier\]]{#prop:multiplier label="prop:multiplier"} Let $F$ be a measurable matrix function on a non-atomic measure space. The multiplication operator $M_F$ on vector-valued $L^2$ is compact only if $F=0$ almost everywhere. Hence a nontrivial Mellin multiplier $S_H-I$ is not trace class.

If $F$ is nonzero on a set of positive measure, restrict to a subset on which one fixed matrix entry $|F_{ij}|$ is bounded below. Split that subset into countably many disjoint positive-measure sets and multiply their normalized indicators by the fixed basis vector $e_j$. They form an orthonormal sequence, while the $i$th components of their images have norms bounded below. Compactness fails.

Thus the scalar function [\[eq:detS\]](#eq:detS){reference-type="eqref" reference="eq:detS"} is a fiber determinant, not an ordinary Fredholm determinant on global Mellin $L^2$. A Birman--Krein determinant would need a constructed scattering pair and trace-class resolvent difference. A semifinite or crossed-product determinant would need a specified algebra and trace. Neither follows from parity diagonalization.

The strict Route-A classification of the frozen candidate is $$\label{eq:route}
(A1\_\mathrm{WEAK},A2\_\mathrm{FAIL},A3\_\mathrm{FAIL},
A4\_\mathrm{NATURAL\_QUANTIZATION}),$$ with overall decision

`ROUTE_A_REJECTED_FOR_UNRENORMALIZED`\
`MELLIN_PARITY_CANDIDATE`.

The Hénon phase and its quantization are intrinsic, but there is no ordinary determinant and the certified extra divisor lies where the target completed Riemann function is certified nonzero. Route B is not invoked.

The odd parity factor does not rescue the construction. The completed Riemann zeta function belongs to the trivial real-place parity, which is the even channel. Keeping only $B$ changes the target archimedean character. Similarly, dividing by a factor designed from the computed zero would fit the divisor after the fact. Only a reference operator derived independently from the same dynamics could authorize cancellation, and the linear parent [\[eq:linear\]](#eq:linear){reference-type="eqref" reference="eq:linear"} supplies none.

# The homogeneous pivot: anomaly or closure

The certified obstruction identifies the inhomogeneous linear term as the source of the unsafe Mellin divisor. Removing it yields the area-preserving homogeneous deformation $$\label{eq:h0}
H_0(q,p)=(-6q^2-p,q),\qquad P_0(q)=2q^3.$$ Its Mellin symbols are elementary: $$\label{eq:kappa0}
\kappa_\pm^{(0)}(z)=\frac13(4\pi)^{-z/3}
\Gamma(z/3)e^{\pm i\pi z/6}.$$ The parity factors are gamma times $\cos(\pi z/6)$ and $\sin(\pi z/6)$. Neither has a zero or pole in the open critical strip.

Equation [\[eq:kappa0\]](#eq:kappa0){reference-type="eqref" reference="eq:kappa0"} clears the divisor gate but creates a sharper structural test. Exact homogeneity makes the scaling cocycle an ambient coboundary. A nontrivial contribution can survive only if the Poisson boundary quotient carries an index or anomaly that obstructs removal of the coboundary. The next large gate is therefore:

> Construct the homogeneous Hénon cocycle on a canonical Poisson boundary quotient and prove either a nonzero index with an intrinsic analytic determinant, or an exact trivialization theorem.

This fork is preferable to another finite zero scan. A nonzero index would provide the missing Hénon-essential bridge toward Route A. Exact trivialization would close the polynomial-chirp adelic branch at its most symmetric point.

# Conclusion

The natural H6 parity symbol passes two conspicuous symmetry tests and fails the test that matters most: its divisor. A rigorous radius-$10^{-12}$ disc contains one simple even-channel zero off the critical line, and independent full-disc bounds exclude every local companion cancellation and certify $\xi\neq0$ there. The resulting scattering pole--zero quartet rejects the unrenormalized candidate. This example gives a concrete warning for Hilbert--Pólya searches: reciprocal symmetry and critical-line unitarity are necessary design features, not divisor theorems.

The certificate is intentionally local. It does not count every zero of the cubic Mellin symbols, construct wave operators, or make an ordinary Fredholm determinant out of a noncompact multiplier. Those limitations do not weaken the rejection of the frozen candidate. They determine the next experiment: the homogeneous cubic removes the unsafe strip divisor and asks whether the Poisson boundary creates a genuine index from an ambient coboundary. That anomaly-or-closure theorem is the next large Hénon gate.

# Rotated-contour majorant {#app:majorant}

After the contour rotation, differentiation under the integral gives $$\begin{aligned}
\kappa_\sigma''(z)
=e^{\sigma i\pi z/6}\int_0^\infty
&e^{-4\pi t^3+2\pi e^{-\sigma i\pi/3}t}t^{z-1}\notag\\
&\times\left(\log t+\frac{\sigma i\pi}{6}\right)^2dt.
\label{eq:second}\end{aligned}$$ On the certified disc, $\mathop{\mathrm{Re}}z>18/25$ and $|\Im z|<161/100$. Use $\pi<22/7$, $e^\pi<24$, and $e^{\pi(161/100)/6}<3$. For $0<t<1$, discard the negative cubic term and bound the remaining logarithmic moment by $$\int_0^1 t^{18/25-1}\left(|\log t|+\pi/6\right)^2dt<8.$$ For $t\ge1$, the exponent satisfies $-4\pi t^3+\pi t\le-9t$, and $$\int_1^\infty e^{-9t}(t+1)^2dt<1$$ dominates the remaining factor. Each sign in [\[eq:second\]](#eq:second){reference-type="eqref" reference="eq:second"} is then bounded by 579. Summation yields $|A''|<1158<1200$ on the disc.

The bound is deliberately coarse. Its role is to produce a transparent analytic inequality, while Arb supplies the much sharper center and companion enclosures.

# Reproducibility contract

The release certificate uses Python, python-flint 0.9.0, and 80 decimal digits of Arb working precision. Its immutable inputs are the original Hénon source, the C35 theorem and derivation packages, and the Route-A evaluator. The producer stores exact rational disc and threshold data, complex-ball output strings, the Rouché inequality, companion nonzero gates, scope, and Route-A decision.

An independent checker reconstructs the hypergeometric formula rather than trusting the producer verdict. Mutation tests require rejection after rehashing changes to the disc, thresholds, zero count, source locks, no-cancellation gates, completed-$\xi$ nonvanishing, Route-A labels, and nested schema. The default runner generates temporary artifacts and compares them byte for byte with the released certificate before verifying the hash manifest. No prime table or Riemann-zero data are read.

The certificate label `NUMERICALLY_CERTIFIED` means a mathematical interval certificate, not an ordinary high-precision approximation. The global statement is limited to the local divisor consequence proved in [\[thm:obstruction\]](#thm:obstruction){reference-type="ref" reference="thm:obstruction"}.
