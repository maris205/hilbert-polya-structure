---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-hemispherical-higgs-oscillator-route-a"
canonical_tex: "henon_dynamics/henon_hemispherical_higgs_oscillator_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_hemispherical_higgs_oscillator_route_a/paper/main.pdf"
source_sha256: "38f6485986b71afb96136692e2324493ef332c76960febe4e993349c41131859"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The Hemispherical Higgs Oscillator: Exact Actions, Friedrichs Spectrum, and Identity Revivals

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_hemispherical_higgs_oscillator_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_hemispherical_higgs_oscillator_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_hemispherical_higgs_oscillator_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_hemispherical_higgs_oscillator_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We close the classical and Friedrichs quantum mechanics of the isotropic Higgs oscillator on one open hemisphere, while keeping its singular boundary explicit. For positive classical coupling, a turning-point integral gives the exact radial action $I_r=(J-|L|-\omega R^2)/2$, where $J=(2R^2E+\omega^2R^4)^{1/2}$. The Hamiltonian in actions has an exact $2{:}1$ frequency lock, so every regular trajectory closes; circular, meridional, equilibrium, and zero-coupling faces are separated. For the quantum Friedrichs realization with nonnegative coupling, Jacobi modes have $E_N=\hbar^2(N+1)(N+1+2\nu)/(2R^2)$ and multiplicity $N+1$. Consecutive spectral gaps then prove that the propagator is the identity precisely when $\tau=\pi M$ and $M(3+2\nu)$ is even. Thus a positive identity revival exists if and only if $2\nu$ is rational, with an explicit least time. Exact finite enumeration is supplied only as a reproducibility receipt.
author:
- 'HCS-C373 theorem package'
date: 4 September 2026
title: |
  The Hemispherical Higgs Oscillator:\
  Exact Actions, Friedrichs Spectrum, and Identity Revivals
```

## Markdown 正文

# Positive-coupling classical system

Fix $R>0$, $\omega>0$, and polar coordinates $0\leq\theta<\pi/2$, $\phi\in\mathbb R/(2\pi\mathbb Z)$. With $L=p_\phi$, consider $$H=\frac{p_\theta^2}{2R^2}
 +\frac{L^2}{2R^2\sin^2\theta}
 +\frac{\omega^2R^2}{2}\tan^2\theta .
 \label{eq:H}$$ The positive coupling is part of the theorem: its divergent equatorial barrier confines every finite-energy trajectory away from the missing equator. Put $$J=(2R^2E+\omega^2R^4)^{1/2},\qquad x=\sin^2\theta .$$

For a regular trajectory with $L\ne0$, the two turning points $0<x_-<x_+<1$ are the roots of $$J^2x^2-(2R^2E+L^2)x+L^2=0.       \label{eq:turning}$$ The radial action and the Hamiltonian in actions are $$\begin{aligned}
 I_r&=\frac{1}{2\pi}\oint p_\theta\,\mathrm d\theta
     =\frac{J-|L|-\omega R^2}{2},                 \label{eq:action}\\
 H(I_r,L)&=\frac{(2I_r+|L|+\omega R^2)^2-
                    \omega^2R^4}{2R^2}.           \label{eq:inverse}\end{aligned}$$ The allowed chamber is $E\geq\omega|L|+L^2/(2R^2)$, with equality exactly on the circular face.

At energy $E$, direct rearrangement of [\[eq:H\]](#eq:H){reference-type="eqref" reference="eq:H"} gives $$p_\theta^2
 =2R^2E-\frac{L^2}{x}-\frac{\omega^2R^4x}{1-x}
 =\frac{J^2(x-x_-)(x_+-x)}{x(1-x)}.$$ Because $\,\mathrm d\theta=\,\mathrm dx/(2\sqrt{x(1-x)})$, the two branches of the closed radial loop give $$I_r=\frac{J}{2\pi}\int_{x_-}^{x_+}
 \frac{\sqrt{(x-x_-)(x_+-x)}}{x(1-x)}\,\mathrm dx .
 \label{eq:action-integral}$$ For $0<a<b<1$, substitute $x=a+(b-a)\sin^2u$ and split $1/[x(1-x)]=1/x+1/(1-x)$. The two elementary integrals yield $$\int_a^b\frac{\sqrt{(x-a)(b-x)}}{x(1-x)}\,\mathrm dx
 =\pi\{1-\sqrt{ab}-\sqrt{(1-a)(1-b)}\}.            \label{eq:root-integral}$$ Vieta's relations for [\[eq:turning\]](#eq:turning){reference-type="eqref" reference="eq:turning"} are $$x_-x_+=\frac{L^2}{J^2},\qquad
 (1-x_-)(1-x_+)=\frac{\omega^2R^4}{J^2}.$$ Equations [\[eq:action-integral\]](#eq:action-integral){reference-type="eqref" reference="eq:action-integral"} and [\[eq:root-integral\]](#eq:root-integral){reference-type="eqref" reference="eq:root-integral"} prove [\[eq:action\]](#eq:action){reference-type="eqref" reference="eq:action"}; solving for $J$ proves [\[eq:inverse\]](#eq:inverse){reference-type="eqref" reference="eq:inverse"}. The two roots coalesce exactly at the displayed energy threshold.

On either signed chamber $L>0$ or $L<0$, $$\Omega_r=\frac{\partial H}{\partial I_r}=\frac{2J}{R^2},
 \qquad
 \Omega_\phi=\frac{\partial H}{\partial L}
 =\operatorname{sgn}(L)\frac{J}{R^2}.$$ Every regular trajectory has radial period $\pi R^2/J$ and primitive phase-space period $2\pi R^2/J$.

Differentiate [\[eq:inverse\]](#eq:inverse){reference-type="eqref" reference="eq:inverse"}. During one radial return the azimuthal angle advances by $\pi\operatorname{sgn}(L)$, so it does not return to the same phase-space point. Two radial returns give angular increments $4\pi$ and $2\pi\operatorname{sgn}(L)$ in the two action angles, proving primitivity.

# Classical boundary atlas

The action formula has four distinct boundary interpretations.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  face                exact behavior
  ------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
  circular            $I_r=0$, $L\ne0$; the double root is $\sin^2\theta_c=|L|/(|L|+\omega R^2)$ and the angular period is $2\pi R^2/J$.

  meridional          $L=0$, $I_r>0$; the roots are $0$ and $1-(\omega R^2/J)^2$. A Cartesian tangent chart continues the orbit through the polar-coordinate singularity.

  north equilibrium   $I_r=L=0$, hence $E=0$ and the orbit is fixed.

  zero coupling       $\omega=0$ removes the equatorial barrier. The open hemisphere is then incomplete for crossing geodesics, so it is excluded from the classical periodic-flow theorem.
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This separation prevents a formula valid on regular Liouville tori from being silently extended through collapsed or incomplete faces.

\>0

# Friedrichs quantization on one hemisphere

Now allow $\omega\geq0$, retain $R,\hbar>0$, and take the Friedrichs realization of $$\widehat H=-\frac{\hbar^2}{2R^2}
 [\frac1{\sin\theta}\partial_\theta
 (\sin\theta\,\partial_\theta)
 +\frac1{\sin^2\theta}\partial_\phi^2]
 +\frac{\omega^2R^2}{2}\tan^2\theta .       \label{eq:operator}$$ Define $$\nu=\sqrt{(\omega R^2/\hbar)^2+\frac14}.$$

For $m\in\mathbb Z$, $n_r\in\mathbb Z_{\geq0}$, and $N=2n_r+|m|$, a separated eigenfunction, up to normalization, is $$\psi_{n_r,m}=\mathrm e^{im\phi}(\sin\theta)^{|m|}
 (\cos\theta)^{\nu+1/2}
 P_{n_r}^{(|m|,\nu)}(\cos2\theta),             \label{eq:mode}$$ with $$E_N=\frac{\hbar^2}{2R^2}(N+1)(N+1+2\nu).      \label{eq:energy}$$ The multiplicity of $E_N$ on one hemisphere is $N+1$, and these modes form a complete orthogonal basis of the Friedrichs realization.

Separation with $\mathrm e^{im\phi}$ gives a singular Sturm--Liouville problem. After extracting the north-pole factor $(\sin\theta)^{|m|}$ and the Friedrichs equatorial factor $(\cos\theta)^{\nu+1/2}$, set $y=\cos2\theta$. The remaining factor $v$ satisfies $$(1-y^2)v''+[\nu-|m|-(|m|+\nu+2)y]v'
 +n_r(n_r+|m|+\nu+1)v=0,                     \label{eq:jacobi}$$ the Jacobi equation. Polynomial termination gives [\[eq:mode\]](#eq:mode){reference-type="eqref" reference="eq:mode"} and [\[eq:energy\]](#eq:energy){reference-type="eqref" reference="eq:energy"}. Jacobi completeness with its positive weight, followed by Fourier completeness in $\phi$, proves completeness.

For fixed $N$, admissible labels obey $|m|\leq N$ and $N-|m|\in2\mathbb Z$. Directly counting the two signs for $m\ne0$ and one copy for $m=0$ gives $N+1$. This count is the proof of multiplicity; we do not use a conflicting prose degeneracy sentence in the historical separation source.

#### Limits and domain.

For fixed $N,\omega,\hbar$ and $R\to\infty$, $\nu=\omega R^2/\hbar+o(R^2)$, so $E_N\to\hbar\omega(N+1)$. At $\omega=0$, $\nu=1/2$ and $$E_N=\frac{\hbar^2}{2R^2}(N+1)(N+2).$$ Writing $l=N+1$, these are the Dirichlet-hemisphere levels $\hbar^2l(l+1)/(2R^2)$ with multiplicity $l$. They are the equator-odd sector, not the full-sphere spectrum with multiplicity $2l+1$. Thus $\omega=0$ is valid quantum mechanically only because the Friedrichs domain supplies the Dirichlet boundary omitted by the classical open flow.

\>1

# Exact identity revivals

Write $k=N+1\geq1$ and $\tau=\hbar t/(2R^2)$. By [\[eq:energy\]](#eq:energy){reference-type="eqref" reference="eq:energy"}, the phase on the $k$th energy space is $$\exp\{-i\tau(k^2+2\nu k)\}.$$

The full propagator is the identity at a positive time if and only if $$\tau=\pi M,\qquad M\in\mathbb Z_{>0},\qquad
 M(3+2\nu)\in2\mathbb Z.                            \label{eq:revival}$$ Such a time exists if and only if $2\nu\in\mathbb Q$. If $3+2\nu=a/b$ in lowest terms, then $$M_{\min}=\begin{cases}b,&a\text{ even},\\2b,&a\text{ odd},\end{cases}
 \qquad
 t_{\min}=\frac{2\pi R^2}{\hbar}M_{\min}.$$

If all spectral phases agree, every consecutive ratio is one. The exponent difference between $k+1$ and $k$ is $2k+1+2\nu$. Subtracting the gap condition at $k$ from the one at $k+1$ gives $2\tau\in2\pi\mathbb Z$, hence $\tau=\pi M$. The first gap, between $k=1$ and $k=2$, is then one precisely when $M(3+2\nu)$ is even. This proves necessity.

Conversely, under [\[eq:revival\]](#eq:revival){reference-type="eqref" reference="eq:revival"}, every consecutive-gap exponent in units of $\pi$ is $$M(2k+1+2\nu)=M(3+2\nu)+2M(k-1),$$ an even integer. All phases therefore agree. Their common $k=1$ exponent is $M(1+2\nu)=M(3+2\nu)-2M$, also even, so the common phase is exactly one, not an unspecified scalar. Existence is equivalent to rationality of $2\nu$. Reducedness of $a/b$ forces $b$ to divide $M$; the least multiple making $Ma/b$ even is $b$ for even $a$ and $2b$ for odd $a$.

# Exact receipt, sources, and Route-A boundary

The canonical artifact exhausts 2,048 exact classical action cells, all 8,385 admissible state labels through $N=128$, 256 rational and 256 irrational revival controls, and six boundary rows. An independent checker reconstructs every row. SymPy checks the action algebra, 81 Jacobi equations, 27 direct radial-operator substitutions, both limits, and the gap identities. These finite computations are regression receipts, not the proof of the unbounded theorems.

Higgs and Leemon own the curved oscillator and symmetry lineage [@Higgs; @Leemon]. Bellucci, Nersessian, Saghatelian, and Yeghikyan supply the modern action-angle comparison [@BNSY]. Hakobyan and Pogosyan supply the separated Jacobi background [@HP]; multiplicity here comes from the admissible-label count above, not from their prose degeneracy statement. The present theorem differs from the full-sphere Neumann oscillator, the spherical-pendulum focus-focus system, free-sphere dynamics, and nonlinear Schrödinger dynamics.

The assessment is $$(A0_{\rm fail},A1_{\rm weak},A2_{\rm fail},A3_{\rm fail},
 A4_{\rm natural\ quantization}),
 \qquad \text{overall: Route A rejected}.$$ The scope literal is `NO_BAD_EULER_OR_ROOT_NUMBER`. Rational revival is spectral commensurability, not arithmetic local data. We assert no target Euler factor, root number, automorphy, target divisor or functional equation, target-zero match, Hilbert--Pólya operator, or Route B bridge.

9 P. W. Higgs, "Dynamical symmetries in a spherical geometry. I," *J. Phys. A* 12 (1979), doi:10.1088/0305-4470/12/3/006. H. I. Leemon, "Dynamical symmetries in a spherical geometry. II," *J. Phys. A* 12 (1979), doi:10.1088/0305-4470/12/4/009. S. Bellucci, A. Nersessian, A. Saghatelian, and V. Yeghikyan, "Quantum ring models and action-angle variables," arXiv:1008.3865. Ye. M. Hakobyan and G. S. Pogosyan, "On Interbasis Expansion for Isotropic Oscillator on Two-Dimensional Sphere," arXiv:quant-ph/9803085.

round zero exact action and classical boundary atlas round one Friedrichs Jacobi spectrum and limit atlas round two identity revival and Route A closure
