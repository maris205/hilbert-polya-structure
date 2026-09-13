---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-homogeneous-boundary-index-obstruction"
canonical_tex: "henon_dynamics/henon_homogeneous_boundary_index_obstruction/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_homogeneous_boundary_index_obstruction/paper/main.pdf"
source_sha256: "a2222a70e49704569c2d8908b86d07df02c895a9a4142a3e8689637671e739a4"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Gauge-Trivial Yet Non-Restricted: A Homogeneous Hénon Boundary-Index Obstruction

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_homogeneous_boundary_index_obstruction>)
- [规范 TeX](<../../../../../henon_dynamics/henon_homogeneous_boundary_index_obstruction/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_homogeneous_boundary_index_obstruction/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_homogeneous_boundary_index_obstruction/README.md>)
- [BibTeX](<../../../../../henon_dynamics/henon_homogeneous_boundary_index_obstruction/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We test the most favorable homogeneous pivot of an adelic Hénon--Tate program. The area-preserving map $H_0(q,p)=(-6q^2-p,q)$ has cubic generating phase $P_0(x)=2x^3$, whose Mellin channels are explicit and have no divisor in the open critical strip. Nevertheless, the corresponding scalar scaling cocycle is exactly and simultaneously trivial on rational descent and on idele scaling. Every prime repetition therefore has unit Hénon holonomy. Before Poisson summation, the only canonical pair of boundary hyperplanes has trace-class projection difference and zero essential codimension; we give an explicit counterexample showing why that index cannot be transported through an arbitrary noninjective Poisson map. Finally, the real cubic chirp is quantitatively outside $\mathop{\mathrm{VMO}}(\mathbb{R})$, so its Hardy commutator is noncompact and the standard restricted-Grassmannian determinant-line anomaly is unavailable. Thus the strip-safe homogeneous symbol is a gauge shadow rather than a new Hilbert--Pólya determinant. The result closes the scalar homogeneous anomaly route while leaving a precise nonscalar, graded escape.
author:
- Anonymous Research Note
bibliography:
- references.bib
date: 13 August 2026
title: |
  Gauge-Trivial Yet Non-Restricted:\
  A Homogeneous Hénon Boundary-Index Obstruction
```

## Markdown 正文

# Introduction

An area-preserving Hénon map supplies several ingredients that are tempting in a Hilbert--Pólya search: a canonical symplectic clock, a generating action, a unitary chirp quantization, and a periodic-orbit language [@Wang2026HenonModel]. Previous experiments in this program showed, however, that each attractive ingredient must be tested as part of one invariant object. Importing a zeta divisor from a scaling system and placing an unrelated Hénon unitary beside it is not a construction.

The immediate motivation is the obstruction found for the inhomogeneous phase $2x^3-x$: its natural two-channel Mellin scattering symbol is reciprocal and critical-line unitary, but has a certified off-line divisor. Removing the linear term yields the homogeneous map $$\label{eq:H0}
  H_0(q,p)=(-6q^2-p,q).$$ Its Mellin transform becomes elementary and strip-safe. This creates a sharp question: can the missing arithmetic content survive as a Poisson-boundary index or determinant-line anomaly?

We answer that question negatively for the scalar, functorial, standard Hardy realization. The contribution is not another root scan. It is a three-level obstruction:

1.  the full rational-and-scaling cocycle is an exact equivariant coboundary;

2.  the intrinsic pre-Poisson boundary-hyperplane index is zero, while its passage through a noninjective Poisson map is logically unproved;

3.  the cubic gauge is not in the standard restricted unitary group, so the usual determinant-line rescue is not defined.

The first point uses the same scaling architecture that underlies the adelic trace-formula viewpoint [@Connes1999; @ConnesConsani2021]. The third uses the classical compact-commutator characterization through $\mathop{\mathrm{VMO}}$ [@Uchiyama1978]. We do not claim novelty for those general theories. The new statement is their exact Hénon specialization and the resulting Route-A decision.

The scope matters. A deliberately nonfunctorial Poisson quotient could in principle break the gauge, but it must then come with an independently proved kernel/index theorem. Matrix-valued, projective, or graded lifts are also not scalar coboundaries. Our conclusion is therefore a decisive closure of one large door, not a universal no-go for Hénon dynamics.

# The homogeneous Hénon lift

Let $$\label{eq:generating}
  S_0(q,Q)=qQ+2q^3.$$ With $p=-\partial_qS_0$ and $P=\partial_QS_0$, this gives [\[eq:H0\]](#eq:H0){reference-type="eqref" reference="eq:H0"}. Moreover $$DH_0(q,p)=\begin{pmatrix}-12q&-1\\1&0\end{pmatrix},
  \qquad \det DH_0=1.$$ Thus the pivot remains an authentic area-preserving Hénon system, rather than a separate arithmetic model attached after the fact.

Let $\psi:\mathbb{A}/\mathbb{Q}\to\mathbb{C}^\times$ be the standard additive character and set $$\label{eq:phi}
  \phi(x)=\psi(P_0(x)),\qquad P_0(x)=2x^3.$$ The function $\phi$ is nonvanishing and unitary. Multiplication by it preserves the Schwartz--Bruhat space. For $a\in\mathbb{A}^\times$, define the half-density dilation $D_af(x)=|a|^{1/2}f(ax)$. Conjugation gives $$\label{eq:cocycle}
  D_aM_\phi D_a^{-1}M_\phi^{-1}
  =M_{c(a,\cdot)},
  \qquad
  c(a,x)=\frac{\phi(ax)}{\phi(x)}
         =\psi\!\left(2(a^3-1)x^3\right).$$

We distinguish three levels throughout:

1.  the transformation groupoid before Poisson summation;

2.  static boundary hyperplanes in a chosen completion;

3.  images or compressions under a possibly noninjective Poisson map.

Only constructions that preserve equivariant isomorphisms are called *functorial descendants*. This convention prevents a choice of noninvariant compression from being mistaken for a cocycle invariant.

For the boundary calculation, write $$\Lambda_Q(f)=\int_{\mathbb{A}}\psi(Q(x))f(x)\,dx,
  \qquad V=\ker(ev_0).$$ The distributional identities hold on $\mathcal{S}(\mathbb{A})$. Whenever orthogonal projections are used, we explicitly assume a Hilbert completion on which the relevant functionals are continuous and nonzero. Evaluation and integration are not asserted to be bounded on raw $L^2$.

# Simultaneous equivariant trivialization

[\[thm:gauge\]]{#thm:gauge label="thm:gauge"} The function $c$ in [\[eq:cocycle\]](#eq:cocycle){reference-type="eqref" reference="eq:cocycle"} is a chronological one-cocycle. The same gauge $$\label{eq:gauge}
  T(x,v)=(x,\phi(x)^{-1}v)$$ simultaneously trivializes the twisted $\mathbb{Q}^\times$-descent and the full idele-scaling lift. Hence its transformation-groupoid $H^1$-class and its equivariant line-bundle class are zero.

The cocycle identity is the telescoping equality $$c(ab,x)=\frac{\phi(abx)}{\phi(x)}
  =c(a,bx)c(b,x).$$ Twist either the rational or idele action by $g\cdot(x,v)=(gx,c(g,x)v)$. Then $$T(gx,c(g,x)v)
  =(gx,\phi(gx)^{-1}c(g,x)v)
  =(gx,\phi(x)^{-1}v),$$ which is the untwisted action in the new coordinate. Because the formula is identical for rational descent and idele scaling, their compatibility square is trivialized as well.

This statement is stronger than checking a few local vacua. It says that every gauge-invariant representation, descent, or determinant functor sees the trivial scalar class.

[\[cor:prime\]]{#cor:prime label="cor:prime"} For every prime $p$ and $r\ge1$, the Hénon scalar holonomy around the scaling loop of length $r\log p$ equals one.

Along the successive scales, the exponent is $$\sum_{j=0}^{r-1}2(p^3-1)p^{3j}x^3
  =2(p^{3r}-1)x^3.$$ The rational endpoint identification contributes the inverse gauge $P_0(x)-P_0(p^rx)=-2(p^{3r}-1)x^3$. Their product is one. Equivalently, this is the closed-loop form of the telescoping proof of [\[thm:gauge\]](#thm:gauge){reference-type="ref" reference="thm:gauge"}.

The clock and the inherited scaling Euler factor may remain meaningful, but they are not generated by a nontrivial scalar Hénon holonomy. Any opposite claim must exhibit exactly where functoriality or gauge admissibility is broken.

# Boundary hyperplanes and the Poisson firewall

Fix $a>0$, let $P_a(x)=2a^3x^3$, and define $$K_0=V\cap\ker\Lambda_0,
  \qquad K_a=V\cap\ker\Lambda_{-P_a},
  \qquad W=K_0\cap K_a.$$ The restrictions of the two functionals to $V$ are independent. To make this adelic statement concrete, restrict to factorized tests whose finite components have nonzero integral and are supported in a compact open set on which both finite characters are trivial. The question then reduces to real Schwartz functions $f_\infty$ with $f_\infty(0)=0$. If a linear combination vanished on this real kernel, then as a distribution on $\mathbb{R}$ it would be a multiple of $ev_0$. Away from the origin its smooth density would therefore vanish. The kernels $1$ and $e^{-i\tau a^3x^3}$ are linearly independent, since the constant and cubic Taylor equations are $$\alpha+\beta=0,
  \qquad -i\tau a^3\beta=0.$$ Thus $\dim(K_0/W)=\dim(K_a/W)=1$.

[\[prop:index\]]{#prop:index label="prop:index"} Suppose the two boundary functionals have nonzero Riesz vectors $u,v$ in a Hilbert completion of $V$. Then $$P_{K_0}-P_{K_a}=p_v-p_u\in\mathcal S_1,
  \qquad
  \mathop{\mathrm{Tr}}(P_{K_0}-P_{K_a})=0,$$ and the compression $P_{K_a}|_{K_0}:K_0\to K_a$ is Fredholm with index zero.

After normalizing the Riesz vectors, $P_{K_0}=I-p_u$ and $P_{K_a}=I-p_v$. Their difference has rank at most two and trace $1-1=0$. The kernel of the compression is $K_0\cap\operatorname{span}(v)$, while its cokernel is isomorphic to $K_a\cap\operatorname{span}(u)$. Both dimensions are one when $u\perp v$, and both are zero otherwise.

This is an essential-codimension statement, not a "Fredholm pair" claim under conventions that require a finite-dimensional intersection. It is also strictly pre-Poisson.

[\[prop:firewall\]]{#prop:firewall label="prop:firewall"} Knowing only that two source hyperplanes have relative index zero and each image gains at most one direction over a common image does not determine the relative index of their images under a noninjective map.

Let $$V=K\oplus\mathbb{C}e_1\oplus\mathbb{C}e_2,
  \quad M=K\oplus\mathbb{C}e_1,
  \quad N=K\oplus\mathbb{C}e_2.$$ Their source relative index is zero. Let $E$ be the identity on $K$, set $E(e_1)=0$, and set $E(e_2)=f\perp K$. Then $E(M)=K$ but $E(N)=K\oplus\mathbb{C}f$, so the image essential codimension is $-1$ in the convention $\mathop{\mathrm{Tr}}(P_{E(M)}-P_{E(N)})$.

Consequently, a genuine post-Poisson anomaly would require a specified completion, a kernel calculation proving equal collapse or a controlled asymmetry, bounded projections, and an analytic determinant theorem. The distributional boundary defect alone supplies none of these.

# The standard Hardy escape is non-restricted

At the real place the homogeneous chirp is $$b(x)=e^{4\pi i x^3}.$$ An anomaly in the standard determinant line would require the corresponding multiplier to lie in the restricted unitary group. We now give a direct quantitative obstruction.

[\[thm:vmo\]]{#thm:vmo label="thm:vmo"} For every integer $n\ge2$, set $$I_n=\left[n,n+\frac{1}{12n^2}\right].$$ Then $|I_n|\to0$ and $$\label{eq:variance}
  \frac1{|I_n|}\int_{I_n}|b-b_{I_n}|^2\,dx>\frac{51}{100}.$$ In particular $b$ is outside the real-line vanishing mean-oscillation compactness class (also denoted $\mathrm{CMO}$ in part of the literature); we write $b\notin\mathop{\mathrm{VMO}}(\mathbb{R})$.

Write $x=n+y/(12n^2)$, $0\le y\le1$. After removing the constant phase, $$\label{eq:phase-expansion}
  4\pi(x^3-n^3)
  =\pi y+\frac{\pi}{12n^3}y^2+
    \frac{\pi}{432n^6}y^3.$$ Using $3<\pi<22/7$, the last two terms have modulus less than $1/30$ uniformly for $n\ge2$. Therefore the normalized interval average has modulus at most $$\left|\int_0^1e^{i\pi y}\,dy\right|+\frac{1}{30}
  =\frac{2}{\pi}+\frac{1}{30}<\frac{7}{10}.$$ Since $|b|=1$, its mean-square oscillation equals $1-|b_{I_n}|^2$, which is greater than $1-(7/10)^2=51/100$.

By the compact-commutator criterion for bounded symbols [@Uchiyama1978], $[P_+,M_b]$ is noncompact. Hence it is not Hilbert--Schmidt, and $M_b$ does not define the usual restricted-unitary or restricted-Grassmannian determinant-line anomaly.

The same obstruction is intrinsic in logarithmic scaling coordinates. For $\widetilde b(t)=e^{4\pi i e^{3t}}$, intervals $J_T=[T,T+e^{-3T}/12]$ have vanishing length, while the normalized phase converges uniformly to $e^{i\pi u}$. Thus $\widetilde b\notin\mathop{\mathrm{VMO}}(\mathbb{R})$ as well.

The shrinking-interval witness violates the common local vanishing condition, so the conclusion is independent of the VMO/CMO naming convention.

We do not infer that every Toeplitz operator built from $b$ is non-Fredholm, nor do we rule out an exotic semifinite polarization. The conclusion is exactly that the standard Hardy restricted-group mechanism does not turn this gauge into an index.

# Mellin shadow and Route-A decision

The homogeneous pivot was attractive because its archimedean Mellin channels close exactly. Rotating the cubic oscillatory contour gives $$\label{eq:kappa}
  \kappa^{(0)}_\pm(z)=
  \int_0^\infty e^{\pm4\pi i u^3}u^{z-1}\,du
  =\frac13(4\pi)^{-z/3}\Gamma(z/3)e^{\pm i\pi z/6}.$$ In the parity basis, $$\begin{aligned}
  A_0(z)&=\frac23(4\pi)^{-z/3}\Gamma(z/3)
          \cos(\pi z/6),\label{eq:even}\\
  B_0(z)&=\frac23(4\pi)^{-z/3}\Gamma(z/3)
          \sin(\pi z/6).\label{eq:odd}\end{aligned}$$ Neither channel has a zero or pole in $0<\Re z<1$. This is a genuine analytic improvement over the inhomogeneous phase.

It is nevertheless not a new zeta factor. The entire gamma--trigonometric content in [\[eq:even\]](#eq:even){reference-type="eqref" reference="eq:even"}--[\[eq:odd\]](#eq:odd){reference-type="eqref" reference="eq:odd"} is forced by homogeneity, and the underlying scalar cocycle has already been conjugated to the trivial one in [\[thm:gauge\]](#thm:gauge){reference-type="ref" reference="thm:gauge"}. After dividing only by this fully derived kinematic reference, the relative channels are $(1,1)$. No ordinary Fredholm determinant is produced, and importing the completed Riemann function from the mother scaling system would not count as Hénon-generated evidence.

The resulting Route-A assessment is $$\boxed{(A1_{\rm WEAK},A2_{\rm FAIL},
  A3_{\rm PARTIAL\ ANALYTIC\ STRUCTURE},
  A4_{\rm NATURAL\ QUANTIZATION})}.$$ Here A1 is weak because the prime clock is inherited but every Hénon scalar holonomy is one. A2 fails because neither a determinant-class boundary operator nor a nonzero intrinsic index exists. A3 records the exact strip-safe Mellin structure but no Riemann divisor. A4 records the natural area-preserving map and unitary chirp without upgrading them to a self-adjoint Hilbert--Pólya operator. The overall verdict is $$\texttt{ROUTE\_A\_REJECTED\_FOR\_SCALAR\_HOMOGENEOUS\_ANOMALY}.$$

This is a useful negative result: even exact reciprocity, strip safety, a prime clock, and a natural Hénon quantization do not combine when the coupling class itself is a scalar coboundary.

# Conclusion and the next large door

The homogeneous pivot resolves the ambiguity left by the previous Mellin obstruction. Removing the linear term eliminates the off-line strip divisor, but it also exposes the deeper reason: the scalar cubic scaling lift is globally gauge-trivial. Prime repetitions carry no new holonomy, the canonical static boundary index is zero, and the standard Hardy polarization is not admissible for a determinant-line anomaly.

The remaining Poisson possibility is narrow and testable. One must define a nonfunctorial quotient or compression, compute its kernel on both boundary directions, prove a nonzero stable index, and construct an analytic determinant. shows that such an index cannot be inferred from codimension bookkeeping. Without those bridges, the scalar homogeneous route is closed.

The next large experiment should change representation category rather than tune another scalar phase. The cubic suggests a $\mathbb Z/3$-graded Kummer/Tate lift in which scaling acts on a genuine three-component local system. The decisive first question is whether its closed prime holonomies define a nontrivial gauge-invariant supertrace with correct repetition chronology. If that class is again a coboundary, the whole polynomial-chirp adelic branch should be closed; if not, it supplies the first plausible route from Hénon arithmetic to an analytic superdeterminant.

# Exact oscillation bounds {#app:bounds}

For completeness, the uniform error in [\[eq:phase-expansion\]](#eq:phase-expansion){reference-type="eqref" reference="eq:phase-expansion"} is maximal at $n=2$, $y=1$. Its coefficient of $\pi$ is $$\frac1{96}+\frac1{27648}=\frac{289}{27648}.$$ Consequently $$\left|\frac{\pi}{12n^3}y^2+
  \frac{\pi}{432n^6}y^3\right|
  \le \frac{22}{7}\frac{289}{27648}<\frac1{30}.$$ The ideal half-turn average has modulus $$\left|\int_0^1e^{i\pi y}\,dy\right|=\frac2\pi<\frac23.$$ The triangle inequality therefore gives the rational bound $7/10$, and the exact mean-square identity for a unit-modulus function gives $$1-\left(\frac7{10}\right)^2=\frac{51}{100}.$$ The certificate records every rational numerator and denominator and the independent checker reconstructs them rather than trusting the verdict.

# Reproducibility and claim boundary {#app:repro}

The release contains a deterministic exact producer, an independently structured checker, mutation tests, and a fail-closed artifact manifest. The machine certificate reconstructs the area-preserving Jacobian, the cocycle and quotient compatibility identities, prime repetition telescoping, the zero static essential codimension, and the rational $51/100$ VMO bound. It also freezes the conservative Route-A tuple and the forbidden promotions.

The checker does not certify an unspecified post-Poisson index, an exotic semifinite determinant, or RH. Those statements are absent from the schema and mutations that insert or promote them are rejected. The exact reproduction command is

    ./code/run_c37.sh

from the project directory. The default runner is read-only; manifest refresh requires an explicit flag during release preparation.
