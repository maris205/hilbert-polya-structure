---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-unique-gauge-invariant-orbit-sampler"
canonical_tex: "henon_dynamics/henon_unique_gauge_invariant_orbit_sampler/paper/paper.tex"
canonical_pdf: "henon_dynamics/henon_unique_gauge_invariant_orbit_sampler/paper/paper.pdf"
source_sha256: "ec7d5aec8fad39561a9649e31f8cdfdc49e2c071c6dec07f9db1c32434a780ae"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The Unique Gauge-Invariant Sampler on Reflection-Selected Hénon Orbits

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_unique_gauge_invariant_orbit_sampler>)
- [规范 TeX](<../../../../../henon_dynamics/henon_unique_gauge_invariant_orbit_sampler/paper/paper.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_unique_gauge_invariant_orbit_sampler/paper/paper.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_unique_gauge_invariant_orbit_sampler/README.md>)
- [BibTeX](<../../../../../henon_dynamics/henon_unique_gauge_invariant_orbit_sampler/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Marked reflection-boundary pressure for the full Hénon horseshoe has a norm-two symbolic cohomology anomaly, while uniform orbit averaging removes that anomaly. We prove that this repair is canonical. On a primitive $n$-cycle, a normalized real linear sampler annihilates every coboundary $u-u\circ\sigma$ if and only if all its weights equal $1/n$. No positivity hypothesis is needed, and every nonuniform sampler has an explicit one-site transfer-function witness. Combining this finite-dimensional theorem with primitive reflection-packet equidistribution yields, for every continuous potential $f$, the universal extensive pressure $$\mathcal P_f(s)=\tfrac12\log2-s\int f\,d\mu_B,$$ where $\mu_B$ is maximal-entropy Bernoulli measure. The finite packet functional and its limit are exactly invariant under continuous coboundaries, affine in the potential, and Lipschitz in uniform norm. This is a canonical reflection-packet thermodynamic functional, not the ordinary full-shift topological pressure and not an arithmetic trace. Exact rank, packet, and mutation certificates accompany the result.
author:
- |
  Liang Wang\
  School of Artificial Intelligence and Automation\
  Huazhong University of Science and Technology\
  Wuhan 430074, P. R. China
bibliography:
- references.bib
date: 'August 15, 2026'
title: 'The Unique Gauge-Invariant Sampler on Reflection-Selected Hénon Orbits'
```

## Markdown 正文

# From a boundary anomaly to a canonical sampler

For the area-preserving Hénon map $H(x,y)=(6-x^2-y,x)$, the real chain-recurrent set is conjugate to the full two-shift and the reversor is intertwined with sequence reversal [@DevaneyNitecki1979; @Arai2007]; we use standard symbolic cohomology terminology from @LindMarcus1995. Earlier reflection-packet results establish two different limits. Marking the reflection center gives a non-invariant boundary law, while uniformly averaging time origins gives the fair two-sided Bernoulli law $\mu_B$. The marked law has a norm-two anomaly under the standard symbolic cohomology relation $$\label{eq:cohomology}
 f\sim f+u-u\circ\sigma.$$

Uniform orbit averaging cancels [\[eq:cohomology\]](#eq:cohomology){reference-type="eqref" reference="eq:cohomology"} by telescoping. The remaining question is whether this is merely one repair among many or is forced by gauge invariance. We answer it on every primitive finite orbit.

Let $C_n=\mathbb Z/n\mathbb Z$ and write $$\label{eq:sampler}
 L_w(f)=\sum_{j\in C_n}w_jf_j,
 \qquad \sum_{j\in C_n}w_j=1,$$ where the weights may be arbitrary real numbers. The cyclic coboundary operator is $$\label{eq:D}
 (Du)_j=u_j-u_{j+1}.$$

# Uniqueness of cyclic Haar averaging

[\[thm:unique\]]{#thm:unique label="thm:unique"} For a normalized linear sampler [\[eq:sampler\]](#eq:sampler){reference-type="eqref" reference="eq:sampler"}, the following are equivalent:

1.  $L_w(Du)=0$ for every $u:C_n\to\mathbb R$;

2.  $w_0=w_1=\cdots=w_{n-1}=1/n$.

Thus uniform cyclic averaging is the unique normalized real linear sampler that descends to potentials modulo coboundaries.

Reindexing the second term gives $$\label{eq:adjoint}
 L_w(Du)=\sum_{j\in C_n}(w_j-w_{j-1})u_j.$$ This vanishes for every $u$ if and only if $w_j=w_{j-1}$ for every $j$. The weights are therefore constant, and normalization fixes the constant to $1/n$. Conversely, constant weights make [\[eq:adjoint\]](#eq:adjoint){reference-type="eqref" reference="eq:adjoint"} vanish.

[\[cor:witness\]]{#cor:witness label="cor:witness"} If $w$ is normalized but nonuniform, choose an index $k$ with $w_k\ne w_{k-1}$ and let $u=\mathbf 1_{\{k\}}$. Then $$\label{eq:witness}
 L_w(Du)=w_k-w_{k-1}\ne0.$$

This result applies to a primitive symbolic orbit because its $n$ points are distinct. Arbitrary prescribed values on that finite set may be realized by a continuous locally constant symbolic function. The proof therefore does not hide a regularity assumption.

Equivalently, the cyclic incidence matrix has rank $n-1$ and its left kernel is the one-dimensional span of the all-ones vector. Normalization selects the Haar probability measure on $C_n$.

# Reflection packets and a universal potential

For odd $n$, let $A_n$ be the set of primitive reflection-centered words and let $$\label{eq:Dn}
 D_n=|A_n|=\sum_{d\mid n}\mu(n/d)2^{(d+1)/2}.$$ Define the canonical packet measure and mean by $$\begin{aligned}
\label{eq:packetmeasure}
 \nu_n^{\mathrm{orb}}
 &=\frac1{nD_n}\sum_{\omega\in A_n}\sum_{j=0}^{n-1}
   \delta_{\sigma^j\omega},\\
 b_n(f)&=\int f\,d\nu_n^{\mathrm{orb}}.\end{aligned}$$ Primitive reflection-packet equidistribution gives $$\label{eq:equidistribution}
 \nu_n^{\mathrm{orb}}\Longrightarrow\mu_B,
 \qquad
 \frac1n\log D_n\longrightarrow\frac12\log2$$ along odd $n$; the cylinder estimate and primitive subtraction behind this statement were proved in the preceding packet theorem. Weak convergence implies $b_n(f)\to\int f\,d\mu_B$ for every continuous $f$.

For fixed $s\in\mathbb R$, define $$\label{eq:Zn}
 Z_n(s;f)=D_n\exp\{-sn b_n(f)\}.$$

[\[thm:pressure\]]{#thm:pressure label="thm:pressure"} For every continuous $f$ and fixed real $s$, $$\label{eq:pressure}
 \mathcal P_f(s)
 :=\lim_{\substack{n\to\infty\\n\ \mathrm{odd}}}
   \frac1n\log Z_n(s;f)
 =\frac12\log2-s\int f\,d\mu_B.$$ Moreover: $$\begin{aligned}
 b_n(f+u-u\circ\sigma)&=b_n(f),\label{eq:finitegauge}\\
 \mathcal P_{f+u-u\circ\sigma}(s)&=\mathcal P_f(s),\label{eq:limitgauge}\\
 |\mathcal P_f(s)-\mathcal P_g(s)|&\le |s|\,\lVert f-g\rVert_\infty.
 \label{eq:lipschitz}\end{aligned}$$ The first identity holds exactly at every finite $n$.

Equation [\[eq:pressure\]](#eq:pressure){reference-type="eqref" reference="eq:pressure"} follows immediately from [\[eq:Zn\]](#eq:Zn){reference-type="eqref" reference="eq:Zn"} and [\[eq:equidistribution\]](#eq:equidistribution){reference-type="eqref" reference="eq:equidistribution"}. Applying [\[thm:unique\]](#thm:unique){reference-type="ref" reference="thm:unique"} orbit by orbit gives [\[eq:finitegauge\]](#eq:finitegauge){reference-type="eqref" reference="eq:finitegauge"}; passage to the limit gives [\[eq:limitgauge\]](#eq:limitgauge){reference-type="eqref" reference="eq:limitgauge"}. Finally, $\mu_B$ is a probability measure, so $|\int(f-g)d\mu_B|\le\lVert f-g\rVert_\infty$.

The base entropy in [\[eq:pressure\]](#eq:pressure){reference-type="eqref" reference="eq:pressure"} is the half entropy of the reflection packet, and the slope is expectation against a fixed measure. This affine functional is therefore not the full-shift topological pressure $P_{\mathrm{top}}(-sf)$ in general. Its content is canonical sampling of a sparse packet, not a variational principle over all invariant measures.

# Exact certificate and claim boundary

The accompanying programs compute the cyclic difference rank for $2\le n\le12$, independently test all basis transfer functions through $n=17$, and exhibit a one-site anomaly for every tested nonuniform sampler. They also enumerate primitive palindromic packets through odd period $21$, check a two-block Bernoulli cylinder bound, and verify exact finite telescoping. Eight tests pass in normal and optimized modes, five upstream artifacts are hash locked, and 21 hostile claim mutations are rejected.

The theorem supplies a canonical, gauge-invariant thermodynamic functional for reflection-selected Hénon packets. It does not supply an intrinsic rational-prime labeling, von Mangoldt amplitudes, a source-native Fredholm determinant, a self-adjoint operator, or a Hilbert--Pólya correspondence. Route A remains exploratory and Route B is not authorized. The next non-micro gate is to construct a reflection-packet determinant or trace whose logarithmic derivative realizes the canonical orbit functional and then test its arithmetic semantics.
