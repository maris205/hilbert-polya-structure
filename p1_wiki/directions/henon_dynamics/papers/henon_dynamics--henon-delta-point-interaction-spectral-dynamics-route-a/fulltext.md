---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-delta-point-interaction-spectral-dynamics-route-a"
canonical_tex: "henon_dynamics/henon_delta_point_interaction_spectral_dynamics_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_delta_point_interaction_spectral_dynamics_route_a/paper/main.pdf"
source_sha256: "4b5a3f3bce40e642025e42a22ab5fdcd4e2478e31f78ba9596720002429729e1"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Resolvent, Scattering, and Heat Dynamics of a One-Dimensional Delta Interaction

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_delta_point_interaction_spectral_dynamics_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_delta_point_interaction_spectral_dynamics_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_delta_point_interaction_spectral_dynamics_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_delta_point_interaction_spectral_dynamics_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We give a convention-complete solution of the one-center delta interaction on the real line in units $\hbar=2m=1$. =0 The closed quadratic form yields the exact continuity and derivative-jump domain, and a scalar interface equation gives the rank-one resolvent. \>0 Its pole produces exactly one attractive bound state; the remaining spectrum, left--right scattering, and odd/even channels are closed for every real coupling, including threshold and free faces. \>1 Laplace inversion gives the heat kernel and an integrable relative diagonal with explicit trace. Independent exact and high-precision evidence audits all constants without replacing the analytic proof. The model has a natural self-adjoint quantization but no arithmetic-orbit or target-determinant bridge.
author:
- 'Route-A source-local certificate HCS-C288'
date: 2 September 2026
title: |
  Resolvent, Scattering, and Heat Dynamics\
  of a One-Dimensional Delta Interaction
```

## Markdown 正文

trailerid \[\<C2882026090200000000000000000000\>\<C2882026090200000000000000000000\>\]

# The frozen singular Hamiltonian

For $\alpha\in\mathbb R$, consider the form $$\label{eq:form}
 q_\alpha[\psi]=\int_\mathbb R|\psi'(x)|^2\,\mathrm dx
    +\alpha|\psi(0)|^2,
 \qquad \mathcal D(q_\alpha)=H^1(\mathbb R).$$ The one-dimensional trace inequality makes point evaluation infinitesimally form bounded relative to the Dirichlet integral. Thus [\[eq:form\]](#eq:form){reference-type="eqref" reference="eq:form"} is closed and lower bounded and defines one self-adjoint operator $H_\alpha$. Integration by parts identifies its domain: $$\label{eq:domain}
 \begin{split}
 \mathcal D(H_\alpha)=\{\psi\in H^2(\mathbb R\setminus\{0\}):{}&
 \psi(0+)=\psi(0-),\\[-2pt]
 &\psi'(0+)-\psi'(0-)=\alpha\psi(0)\},
 \end{split}$$ and $H_\alpha\psi=-\psi''$ off zero. This normalization is the owner; changing the jump sign exchanges attractive and repulsive chambers.

Point interactions and their complete solvability are classical. The monograph of Albeverio, Gesztesy, Høegh-Krohn, and Holden contains a direct chapter on the one-center one-dimensional delta interaction [@AGHH1988]. Our contribution is the self-contained convention and executable closure below, not a priority claim.

# One scalar equation gives the resolvent

For $\kappa>0$, the free kernel at energy $-\kappa^2$ is $$G_\kappa(x,y)=\frac{e^{-\kappa|x-y|}}{2\kappa}.$$

[\[thm:resolvent\]]{#thm:resolvent label="thm:resolvent"} If $2\kappa+\alpha\ne0$, then $$\label{eq:resolvent}
 (H_\alpha+\kappa^2)^{-1}(x,y)
 =\frac1{2\kappa}\left\{e^{-\kappa|x-y|}
 -\frac{\alpha}{2\kappa+\alpha}
 e^{-\kappa(|x|+|y|)}\right\}.$$

Away from $x=y,0$, both exponentials solve the homogeneous equation. The free term is continuous and its derivative has jump $-1$ at $x=y$. At zero, the kernel value in [\[eq:resolvent\]](#eq:resolvent){reference-type="eqref" reference="eq:resolvent"} is $e^{-\kappa|y|}/(2\kappa+\alpha)$. The image term has derivative jump $\alpha e^{-\kappa|y|}/(2\kappa+\alpha)$, exactly $\alpha$ times that value. It therefore satisfies [\[eq:domain\]](#eq:domain){reference-type="eqref" reference="eq:domain"} and the resolvent source equation. Uniqueness follows from invertibility away from the displayed pole.

The formula is a Krein rank-one correction. The exceptional equation $2\kappa+\alpha=0$ has a positive solution precisely when $\alpha<0$; it is spectral data, not a missing regular grid point.

\>0

# Spectrum and two-channel scattering

The odd subspace automatically vanishes at zero, so $H_\alpha$ is free there. On the even subspace the interface becomes the half-line Robin condition $\psi'(0+)=(\alpha/2)\psi(0)$. The odd sine transform and the even Robin generalized eigenfunctions $$\varphi_{\alpha,k}(x)=\sqrt{\frac2\pi}\,
 \frac{2k\cos(kx)+\alpha\sin(kx)}{\sqrt{4k^2+\alpha^2}},
 \qquad x>0,\qquad k>0,$$ give the two continuum transforms; when $\alpha<0$, the even transform is completed by the single normalized bound vector in [\[eq:bound\]](#eq:bound){reference-type="eqref" reference="eq:bound"}.

[\[thm:spectrum\]]{#thm:spectrum label="thm:spectrum"} The essential spectrum is $[0,\infty)$ and is purely absolutely continuous; the singular-continuous spectrum is empty. If $\alpha<0$, there is exactly one simple eigenvalue and normalized eigenfunction, $$\label{eq:bound}
 E_b=-\frac{\alpha^2}{4},\qquad
 \phi_b(x)=\sqrt{-\frac\alpha2}\,e^{\alpha|x|/2}.$$ For $\alpha\ge0$ there is no eigenvalue.

For momentum $k>0$, a unit-amplitude wave incident from the left has $$\label{eq:scattering}
 r_\alpha(k)=\frac{\alpha}{2ik-\alpha},\qquad
 t_\alpha(k)=\frac{2ik}{2ik-\alpha}.$$ The scattering matrix has odd eigenvalue $1$ and even eigenvalue $(2ik+\alpha)/(2ik-\alpha)$, both of modulus one.

The resolvent pole gives [\[eq:bound\]](#eq:bound){reference-type="eqref" reference="eq:bound"}; direct integration gives $\|\phi_b\|_2^2=(-\alpha/2)(-2/\alpha)=1$. Stone's formula applied to the explicit odd Dirichlet and even Robin resolvents yields the Lebesgue-density transforms displayed above. Their denominator $4k^2+\alpha^2$ has no positive-real zero, the zero-energy solution is not in $L^2$, and the only off-continuum singularity is the displayed attractive pole. Hence there is no embedded point or singular-continuous spectrum. For scattering, write $e^{ikx}+re^{-ikx}$ on $x<0$ and $te^{ikx}$ on $x>0$. Continuity gives $t=1+r$ and the jump gives $2ikr=\alpha t$, proving [\[eq:scattering\]](#eq:scattering){reference-type="eqref" reference="eq:scattering"}. Finally $$|r|^2=\frac{\alpha^2}{4k^2+\alpha^2},\qquad
 |t|^2=\frac{4k^2}{4k^2+\alpha^2},$$ so flux is one; diagonalizing the symmetric left--right matrix gives the two channel phases.

At $\alpha=0$ the operator is exactly free. For nonzero coupling, the zero-energy limit is perfectly reflecting and the high-energy limit is transparent. The attractive pole occurs at $k=i|\alpha|/2$; a repulsive coupling has no upper-half-plane pole.

\>1

# Heat dynamics and the relative trace

Let $K_0(t;u)=(4\pi t)^{-1/2}e^{-u^2/(4t)}$. Laplace inversion of the two terms in [\[eq:resolvent\]](#eq:resolvent){reference-type="eqref" reference="eq:resolvent"} uses, for $\Re\sqrt{s}>\max\{0,-\alpha/2\}$, the one-line identity $$\mathcal L_{t\to s}\!\left[
 e^{\alpha a/2+\alpha^2t/4}
 \operatorname{erfc}\!\left(\frac{a}{2\sqrt t}+\frac{\alpha\sqrt t}{2}\right)\right]
 =\frac{2e^{-a\sqrt{s}}}{\sqrt{s}\,(2\sqrt{s}+\alpha)}.$$ It yields the following all-time expression.

[\[thm:heat\]]{#thm:heat label="thm:heat"} For $t>0$, $x,y\in\mathbb R$, and $a=|x|+|y|$, $$\label{eq:heat}
 K_\alpha(t;x,y)=K_0(t;x-y)-\frac\alpha4
 e^{\alpha a/2+\alpha^2t/4}
 \operatorname{erfc}\!\left(\frac{a}{2\sqrt t}+\frac{\alpha\sqrt t}{2}\right).$$ The diagonal difference from the free heat kernel is integrable and $$\label{eq:trace}
 \int_\mathbb R\{K_\alpha(t;x,x)-K_0(t;0)\}\,\mathrm dx
 =\frac12\left[e^{\alpha^2t/4}
 \operatorname{erfc}\!\left(\frac{\alpha\sqrt t}{2}\right)-1\right].$$

The Laplace transform in $t$ of [\[eq:heat\]](#eq:heat){reference-type="eqref" reference="eq:heat"} is [\[eq:resolvent\]](#eq:resolvent){reference-type="eqref" reference="eq:resolvent"}; uniqueness of the semigroup transform proves the kernel. For the trace, symmetry reduces the image term to $$-\frac\alpha2e^{\alpha^2t/4}
 \int_0^\infty e^{\alpha x}
 \operatorname{erfc}\!\left(\frac{x}{\sqrt t}+\frac{\alpha\sqrt t}{2}\right)\mathrm dx.$$ One integration by parts evaluates the integral as $$\frac{e^{-\alpha^2t/4}-
 \operatorname{erfc}(\alpha\sqrt t/2)}{\alpha},$$ with its continuous value at $\alpha=0$, giving [\[eq:trace\]](#eq:trace){reference-type="eqref" reference="eq:trace"}.

The trace defect tends to zero as $t\downarrow0$. For $\alpha<0$, its large-time leading term is $e^{\alpha^2t/4}$, the heat weight of the unique negative eigenvalue. This is not growth of the unitary group $e^{-itH_\alpha}$, which remains norm preserving. For $\alpha>0$, the relative trace tends to $-1/2$.

# Executable closure and Route-A boundary

The producer contains 32 regular resolvent cells, three deliberately separated poles, 28 scattering cells, three bound-state cells, and eight high-precision heat cells. A strict duplicate-rejecting checker reports 1,726 assertions and reconstructs the heat values by inverse Laplace transformation and an integrated diagonal resolvent; a symbolic engine reports 46 identities; two fresh outputs are byte identical; and 30/30 semantic, structural, raw-JSON, and stale-hash attacks fail as required. These finite receipts audit signs and factors; they do not prove Theorems [\[thm:resolvent\]](#thm:resolvent){reference-type="ref" reference="thm:resolvent"}--[\[thm:heat\]](#thm:heat){reference-type="ref" reference="thm:heat"}.

The natural self-adjoint Hamiltonian earns only `A4_NATURAL_QUANTIZATION`. No rational-prime carrier, primitive repetition law, logarithmic arithmetic clock, target divisor, target functional equation, or Hilbert--Pólya operator is constructed. Under the literal scope `NO_BAD_EULER_OR_ROOT_NUMBER`, the strict tuple is $$\begin{gathered}
 \texttt{(A0\_FAIL,A1\_FAIL,A2\_FAIL,}\\[-2pt]
 \texttt{A3\_FAIL,A4\_NATURAL\_QUANTIZATION)},
 \end{gathered}$$ the overall verdict is `ROUTE_A_REJECTED`, and Route B is disabled.

1 S. Albeverio, F. Gesztesy, R. Høegh-Krohn, and H. Holden, *Solvable Models in Quantum Mechanics*, Theoretical and Mathematical Physics, Springer, 1988, [doi:10.1007/978-3-642-88201-2](https://doi.org/10.1007/978-3-642-88201-2).
