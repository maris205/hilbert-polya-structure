---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-lamb-oseen-self-similar-vortex-route-a"
canonical_tex: "henon_dynamics/henon_lamb_oseen_self_similar_vortex_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_lamb_oseen_self_similar_vortex_route_a/paper/main.pdf"
source_sha256: "068c9dc02df54258ad0b8b542d42075b054435a8be16a4ba1a94a4096d2b7a08"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The Radial Lamb--Oseen Similarity Class: Uniqueness, Exact Particle Angles, and Dissipation Boundaries

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_lamb_oseen_self_similar_vortex_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_lamb_oseen_self_similar_vortex_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_lamb_oseen_self_similar_vortex_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_lamb_oseen_self_similar_vortex_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We classify the bounded-at-origin, finite-circulation, radial forward-self- similar solutions of the planar viscous vorticity equation: the signed Lamb--Oseen Gaussian is the entire declared class. =0 We reconstruct its velocity, integrate every positive-radius particle path, and give all radial moments, finite $L^p$ norms, enstrophy, and palinstrophy. \>0 Beyond exact Eulerian and Lagrangian formulas, we separate the zero-age, inviscid, origin-particle, long-time, recurrence, and infinite-energy boundaries without extending uniqueness to arbitrary vortices. \>1 A 213-cell evidence certificate and independent symbolic, replay, mutation, and deterministic-build lanes support regression; the analytic proof remains global. The resulting Route-A tuple is five explicit failures.
author:
- 'Route-A source-local certificate HCS-C299'
date: 2 September 2026
title: |
  The Radial Lamb--Oseen Similarity Class:\
  Uniqueness, Exact Particle Angles, and Dissipation Boundaries
```

## Markdown 正文

trailerid \[\<C2992026090200000000000000000000\>\<C2992026090200000000000000000000\>\]

# Declared class and complete classification

On $\mathbb R^2$ consider $$\label{eq:NS}
 \partial_t\omega+u\cdot\nabla\omega=\nu\Delta\omega,
 \qquad \nabla\cdot u=0,\qquad \operatorname{curl}u=\omega,$$ with the decaying planar Biot--Savart velocity. Fix $\Gamma\in\mathbb R$, $\nu>0$, and $\tau=t+\tau_0>0$, where $\tau_0\ge0$.

[\[thm:class\]]{#thm:class label="thm:class"} Suppose a classical radial solution of [\[eq:NS\]](#eq:NS){reference-type="eqref" reference="eq:NS"} has $$\label{eq:ansatz}
 \omega(x,t)=\tau^{-1}F(\xi),\qquad \xi=|x|/\sqrt\tau,$$ where $F\in C^2([0,\infty))$ is bounded at the origin and $\int_0^\infty |F(\xi)|\xi\,\mathrm d\xi<\infty$. If $\int_{\mathbb R^2}\omega\,\mathrm dx=\Gamma$, then $$\label{eq:omega}
 \omega(x,t)=\frac{\Gamma}{4\pi\nu\tau}
 \exp\!\left(-\frac{|x|^2}{4\nu\tau}\right).$$ Thus [\[eq:omega\]](#eq:omega){reference-type="eqref" reference="eq:omega"} is the entire declared similarity class, including $\Gamma=0$.

Radial vorticity has radial gradient, whereas its Biot--Savart velocity is tangential; hence $u\cdot\nabla\omega=0$. Substitution of [\[eq:ansatz\]](#eq:ansatz){reference-type="eqref" reference="eq:ansatz"} into the heat equation yields $$\label{eq:ode}
 \nu(F''+\xi^{-1}F')+F+\frac{\xi}{2}F'=0.$$ Multiplying by $\xi$ and integrating once gives $$\label{eq:first}
 \nu\xi F'(\xi)+\frac{\xi^2}{2}F(\xi)=C.$$ The origin hypotheses make both left-hand terms tend to zero, so $C=0$. Therefore $F=Ae^{-\xi^2/(4\nu)}$. The normalization $\Gamma=2\pi\int_0^\infty F(\xi)\xi\,\mathrm d\xi=4\pi\nu A$ fixes $A$ and proves [\[eq:omega\]](#eq:omega){reference-type="eqref" reference="eq:omega"}.

The scope of Theorem [\[thm:class\]](#thm:class){reference-type="ref" reference="thm:class"} is essential: it classifies every profile satisfying [\[eq:ansatz\]](#eq:ansatz){reference-type="eqref" reference="eq:ansatz"} and the displayed regularity and integrability conditions, not arbitrary vortex filaments or arbitrary solutions of [\[eq:NS\]](#eq:NS){reference-type="eqref" reference="eq:NS"}. The classical Lamb--Oseen mechanism is source owned by Oseen; we claim no historical priority.

# Velocity and exact Lagrangian dynamics

Polar circulation reconstructs the velocity without an unrecorded constant: $$\label{eq:velocity}
 u_r=0,\qquad
 u_\theta(r,t)=\frac{\Gamma}{2\pi r}
 \left(1-e^{-r^2/(4\nu\tau)}\right)\quad(r>0),
 \qquad u(0,t)=0.$$ Indeed $2\pi r u_\theta=2\pi\int_0^r s\omega(s,t)\,\mathrm ds$; near zero, $u_\theta=\Gamma r/(8\pi\nu\tau)+O(r^3)$.

[\[prop:particle\]]{#prop:particle label="prop:particle"} For $r_0>0$, radius is invariant. Put $a=r_0^2/(4\nu)$ and $$\label{eq:primitive}
 \mathcal F_a(\tau)=\tau-\tau e^{-a/\tau}-a\operatorname{Ei}(-a/\tau).$$ Between positive ages $\tau_s<\tau_t$, $$\label{eq:angle}
 \theta(\tau_t)-\theta(\tau_s)
 =\frac{\Gamma}{2\pi r_0^2}
 [\mathcal F_a(\tau_t)-\mathcal F_a(\tau_s)].$$ Here $\theta$ denotes a continuous real-valued lift of polar angle, not only its class modulo $2\pi$. The origin is a fixed particle. If $\Gamma\ne0$ and $r_0>0$, then $$\label{eq:angleasymp}
 \theta(t)=\frac{\Gamma}{8\pi\nu}\log\tau+O(1)
 \qquad(\tau\to\infty).$$

Equation [\[eq:velocity\]](#eq:velocity){reference-type="eqref" reference="eq:velocity"} gives $\dot r=0$ and $$\dot\theta=\frac{\Gamma}{2\pi r_0^2}(1-e^{-a/\tau}).$$ Direct differentiation shows $\mathcal F_a'=1-e^{-a/\tau}$, proving [\[eq:angle\]](#eq:angle){reference-type="eqref" reference="eq:angle"}. The continuous origin value proves the fixed-point claim. Finally $1-e^{-a/\tau}=a/\tau+O(\tau^{-2})$, which gives [\[eq:angleasymp\]](#eq:angleasymp){reference-type="eqref" reference="eq:angleasymp"} because $a/r_0^2=1/(4\nu)$.

# All moments, norms, and exact dissipation

The change of variable $y=r^2/(4\nu\tau)$ evaluates the whole parameter family, rather than a finite selection.

[\[prop:norms\]]{#prop:norms label="prop:norms"} For every integer $k\ge0$ and every real $1\le p<\infty$, $$\begin{aligned}
 \int_{\mathbb R^2}|x|^{2k}\omega(x,t)\,\mathrm dx
 &=\Gamma k!(4\nu\tau)^k,\label{eq:moments}\\
 \|\omega(\cdot,t)\|_p^p
 &=\frac{|\Gamma|^p}{p(4\pi\nu\tau)^{p-1}}.\label{eq:lp}\end{aligned}$$ Also $\|\omega\|_\infty=|\Gamma|/(4\pi\nu\tau)$ and $$\begin{aligned}
 \int_{\mathbb R^2}\omega^2\,\mathrm dx&=\frac{\Gamma^2}{8\pi\nu\tau},
 \label{eq:enstrophy}\\
 \int_{\mathbb R^2}|\nabla\omega|^2\,\mathrm dx&=
 \frac{\Gamma^2}{16\pi\nu^2\tau^2},\label{eq:palinstrophy}\\
 \frac{\,\mathrm d}{\,\mathrm dt}\int_{\mathbb R^2}\omega^2\,\mathrm dx
 &=-2\nu\int_{\mathbb R^2}|\nabla\omega|^2\,\mathrm dx.\label{eq:dissipation}\end{aligned}$$

Polar integration and $y=r^2/(4\nu\tau)$ reduce [\[eq:moments\]](#eq:moments){reference-type="eqref" reference="eq:moments"} to $\int_0^\infty y^k e^{-y}\,\mathrm dy=k!$ and [\[eq:lp\]](#eq:lp){reference-type="eqref" reference="eq:lp"} to $\int_0^\infty e^{-py}\,\mathrm dy=1/p$. The supremum occurs at the origin. The case $p=2$ gives [\[eq:enstrophy\]](#eq:enstrophy){reference-type="eqref" reference="eq:enstrophy"}; differentiating [\[eq:omega\]](#eq:omega){reference-type="eqref" reference="eq:omega"} radially and integrating gives [\[eq:palinstrophy\]](#eq:palinstrophy){reference-type="eqref" reference="eq:palinstrophy"}. Differentiation in $t$ closes [\[eq:dissipation\]](#eq:dissipation){reference-type="eqref" reference="eq:dissipation"}.

\>0

# Boundary atlas and recurrence obstruction

The formulas remain useful only if singular endpoints are not silently substituted into a positive-parameter theorem.

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Boundary           Status        Exact conclusion
  ------------------ ------------- -----------------------------------------------------------------------------------------------------------------------------------------------
  $\Gamma=0$         included      $\omega=u=0$ at every positive age.

  $\tau_0>0$         included      Smooth finite-enstrophy initial profile.

  $\tau_0=0$         weak trace    $\omega(\cdot,t)\rightharpoonup\Gamma\delta_0$ as $t\downarrow0$; smooth for $t>0$.

  $\nu\downarrow0$   weak limit    Vorticity tends to $\Gamma\delta_0$; velocity tends off the origin to the point vortex.

  $r_0=0$            separate      The continuous velocity fixes the origin; formula [\[eq:angle\]](#eq:angle){reference-type="eqref" reference="eq:angle"} is only for $r_0>0$.

  $\tau\to\infty$    asymptotic    Positive-radius angular drift is logarithmic as in [\[eq:angleasymp\]](#eq:angleasymp){reference-type="eqref" reference="eq:angleasymp"}.

  $p>1$              obstruction   For $\Gamma\ne0$, every finite $L^p$ norm decreases strictly with age.

  $R\to\infty$       warning       Whole-plane kinetic energy diverges logarithmically.
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Positive viscosity is the theorem domain; $\nu=0$ is never inserted into [\[eq:omega\]](#eq:omega){reference-type="eqref" reference="eq:omega"}. The $L^p$ law implies that no nonzero vorticity state in this family can recur at two distinct ages. This fluid-state statement does not mislabel the nonautonomous angular motion as a primitive periodic orbit.

The far field $u_\theta=\Gamma/(2\pi r)+o(r^{-1})$ yields the sharp disk asymptotic $$\label{eq:energy}
 \frac12\int_{|x|<R}|u(x,t)|^2\,\mathrm dx
 =\frac{\Gamma^2}{4\pi}\log R+O(1).$$ Thus positive-age enstrophy and palinstrophy are finite, whereas nonzero whole-plane kinetic energy is not. These are different integrability tests.

\>1

# Exact evidence and hostile audit

The archived evidence covers eight signed field cases. Each contains nine similarity coordinates, nine even-moment receipts, and six $L^p$ receipts. Twelve positive-radius cases compare [\[eq:primitive\]](#eq:primitive){reference-type="eqref" reference="eq:primitive"} against independent 90-digit quadrature, and nine rows encode the boundary ledger: in total $72+72+48+12+9=213$ audited cells. This is regression evidence only; the global statements follow from the proofs above.

The independent checker imports no producer and reconstructs every rational or transcendental value. A separate SymPy lane verifies [\[eq:ode\]](#eq:ode){reference-type="eqref" reference="eq:ode"}, the heat equation, curl, all sampled moments and norms, the dissipation identity, the exponential-integral derivative, and both asymptotic coefficients. Byte replay, repaired-hash hostile mutations, duplicate-key and nonfinite-token rejection, exact YAML semantics, and six isolated fixed-epoch builds close the digital audit.

#### Collision boundaries.

C206 concerns Couette advection--diffusion and Fourier shearing on $\mathbb T\times\mathbb R$; here the planar velocity is reconstructed by Biot--Savart and radial geometry cancels nonlinear advection. C207 concerns scalar nonlinear diffusion and Barenblatt profiles; here diffusion is linear only after the vorticity reduction, and circulation, particle trajectories, the point-vortex boundary, and kinetic energy are part of the theorem.

# Route-A verdict and reproducibility

Under the frozen scope `NO_BAD_EULER_OR_ROOT_NUMBER`, the exact tuple is $$(\mathrm{A0\_FAIL},\mathrm{A1\_FAIL},\mathrm{A2\_FAIL},
   \mathrm{A3\_FAIL},\mathrm{A4\_FAIL}).$$ Circulation and Gaussian moments are not arithmetic local data (A0). Strict $L^p$ decay supplies no recurrent primitive-orbit bridge (A1). Physical viscous time, even with logarithmic angular drift, is not an arithmetic clock (A2). No target completed function or functional equation appears (A3). The dissipative heat/Navier--Stokes generator is not a self-adjoint Hilbert--Pólya operator (A4). The overall verdict is `ROUTE_A_REJECTED`, and Route B stays locked.

No target Euler factor, root number, automorphy statement, divisor law, functional equation, target-zero correspondence, or target spectral realization is claimed.

#### Reproducibility statement.

The release retains the producer, duplicate-rejecting checker, symbolic lane, byte replay, mutation suite, strict evaluation, three manuscript revisions, and self-excluding manifest. Source commit, evaluator digest, epoch, and scope are machine checked.

#### AI-use statement.

A generative language model assisted with drafting and verification-code scaffolding. Independent scripted lanes checked formulas, exact outputs, scope boundaries, and release artifacts; final responsibility remains with the authors.

# Source lineage {#source-lineage .unnumbered}

Oseen's 1912 line-vortex work is the classical owner token for the profile. Gallay and Wayne provide modern mathematical context for the two-dimensional Oseen vortex and its stability. These citations establish lineage, not a novelty or priority claim for the classical formula.

9 C. W. Oseen, "Über Wirbelbewegung in einer reibenden Flüssigkeit," *Arkiv för Matematik, Astronomi och Fysik* 7 (1912), no. 14.

T. Gallay and C. E. Wayne, "Global stability of vortex solutions of the two-dimensional Navier--Stokes equation," *Communications in Mathematical Physics* 255 (2005), 97--129. DOI: [10.1007/s00220-004-1254-9](https://doi.org/10.1007/s00220-004-1254-9).
