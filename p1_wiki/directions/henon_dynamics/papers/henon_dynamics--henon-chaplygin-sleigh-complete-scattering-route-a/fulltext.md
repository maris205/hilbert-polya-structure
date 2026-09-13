---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-chaplygin-sleigh-complete-scattering-route-a"
canonical_tex: "henon_dynamics/henon_chaplygin_sleigh_complete_scattering_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_chaplygin_sleigh_complete_scattering_route_a/paper/main.pdf"
source_sha256: "5c93275475c82c134ebc4cba3cf67a1b80282d3c84872a878ddc393c98b98150"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The Chaplygin Sleigh for Every Signed Mass Offset: Exact Scattering, Physical Reconstruction, and the Recurrence Boundary

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_chaplygin_sleigh_complete_scattering_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_chaplygin_sleigh_complete_scattering_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_chaplygin_sleigh_complete_scattering_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_chaplygin_sleigh_complete_scattering_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We give a convention-complete theorem for the classical Chaplygin sleigh with mass $m>0$, central inertia $J>0$, and arbitrary signed longitudinal offset $a$. For $a\ne0$, every non-equilibrium positive-energy reduced orbit is an explicit heteroclinic: its blade rotates through an energy-independent angle and its contact point has two rigorously defined asymptotic lines. We also classify the stable equilibrium half-axis, half-plane Poisson structure, necessarily singular reduced density and its configuration-Haar lift, reversor, and all zero-offset and zero-angular- velocity boundaries. A finite exact/high-precision ledger checks conventions but is not used to prove the continuous theorem. The Poisson form gives only a formal Route-A hint; the absence of an intrinsic prime carrier and target determinant forces rejection.
author:
- 'Route-A structural certificate C199'
title: |
  The Chaplygin Sleigh for Every Signed Mass Offset:\
  Exact Scattering, Physical Reconstruction, and the Recurrence Boundary
```

## Markdown 正文

suppressoptionalinfo 611

**Keywords:** Chaplygin sleigh; nonholonomic mechanics; heteroclinic scattering; reconstruction; invariant measure; reversibility.

chinese-simplified

中文摘要

本文对质量、转动惯量均为正且质心纵向偏置可取任意符号的经典 [Chaplygin sleigh]{lang="en"}给出完整定理。偏置非零时，全部非平衡正能轨道均为 显式异宿轨道；刀刃转角与能量无关，接触点具有两条严格定义的渐近直线。本文还统一分类 稳定平衡半轴、半平面泊松结构、必然奇异的不变测度、时间反演以及零偏置等全部边界。 有限精确计算只校验约定，不代替连续参数证明；路线[A]{lang="en"}最终仍被拒绝。

关键词：非完整力学；异宿散射；重构；不变测度；时间反演。

# Convention, equations, and ownership

Let $r=(x,y)$ be the knife contact point, $\theta\in\mathbb S^1$ the *blade* angle, $u$ the signed contact velocity along the blade, and $\omega=\dot\theta$. Let $a\in\mathbb R$ be the signed longitudinal offset from contact point to centre of mass and put $I_c=J+ma^2$. In physical time, the reduced equations and reconstruction are $$\label{eq:system}
 \dot r=u\mathbf e(\theta),\quad \dot\theta=\omega,\quad
 \dot u=a\omega^2,\quad
 \dot\omega=-\frac{ma}{I_c}u\omega,\qquad
 \mathbf e(\theta)=(\cos\theta,\sin\theta).$$ They imply $$\label{eq:energy}
 H=\frac m2u^2+\frac{I_c}{2}\omega^2=\text{constant}.$$ The model, its nonholonomic reduction and Hamiltonization context are classical [@Bloch00; @BM09; @M87]. We claim a signed-parameter synthesis and certificate, not priority for those results.

# All nonzero-offset scattering orbits

[\[thm:normal\]]{#thm:normal label="thm:normal"} Assume $a\ne0$, $H>0$, and $\omega(0)\ne0$. Define $$R=\sqrt{2H/m},\quad A=\frac{m|a|R}{I_c},\quad
 \eta=\frac{\sqrt{I_c/m}}{|a|},\quad \sigma=\operatorname{sgn}\omega(0).$$ There are unique $t_0\in\mathbb R$ and $\theta_0$ modulo $2\pi$ such that, with $s=A(t-t_0)$, $$\label{eq:closed}
 u=\operatorname{sgn}(a)R\tanh s,
 \quad\omega=\sigma R\sqrt{m/I_c}\,\operatorname{sech}s,
 \quad\theta=\theta_0+\sigma\eta\arcsin(\tanh s).$$ It joins $(-\operatorname{sgn}(a)R,0)$ to $(\operatorname{sgn}(a)R,0)$ and its blade-angle deflection is $$\label{eq:deflection}
 \Delta\theta=\theta_+-\theta_-=\sigma\pi\eta,$$ which is independent of $H$.

The sign of a nonzero $\omega$ cannot change by uniqueness. On the energy ellipse write $u=\operatorname{sgn}(a)R\tanh s$ and $\omega=\sigma R\sqrt{m/I_c}\operatorname{sech}s$. The first reduced equation gives $\dot s=A$; substitution gives the second. Since $d\{\arcsin(\tanh s)\}/ds=\operatorname{sech}s$, integration of $\dot\theta=\omega$ proves [\[eq:closed\]](#eq:closed){reference-type="eqref" reference="eq:closed"}. Taking $s\to\pm\infty$ proves both endpoints and [\[eq:deflection\]](#eq:deflection){reference-type="eqref" reference="eq:deflection"}.

The endpoint table makes the signed convention explicit: $$\begin{array}{c|cc}
 &t\to-\infty&t\to+\infty\\ \hline
u&-\operatorname{sgn}(a)R&\operatorname{sgn}(a)R\\
\omega&0^\sigma&0^\sigma\\
\theta&\theta_0-\sigma\eta\pi/2&\theta_0+\sigma\eta\pi/2
\end{array}$$

\>0

# Contact-point reconstruction and two lines

Put $q=\tanh s\in(-1,1)$. Since $dt=dq/[A(1-q^2)]$, the full $SE(2)$ reconstruction reduces exactly to $$\label{eq:quad}
 r(q)-r(0)=\frac{\operatorname{sgn}(a)R}{A}
 \int_0^q\frac{y\,\mathbf e(\theta_0+\sigma\eta\arcsin y)}{1-y^2}\,dy.$$ This is a one-dimensional quadrature, not a claim of an elementary primitive.

Let $v_\pm=u_\pm\mathbf e(\theta_\pm)$. There are unique vectors $b_\pm$ such that $$r(t)=b_\pm+v_\pm t+o(1)\qquad(t\to\pm\infty).$$ Thus the contact trajectory scatters between two oriented affine lines.

As $s\to+\infty$, $u-u_+=O(e^{-2s})$ while $\theta-\theta_+=O(e^{-s})$; hence $u\mathbf e(\theta)-v_+=O(e^{-s})$, integrable in physical time because $s=At+O(1)$. Therefore $r(t)-v_+t$ has a finite limit. The negative end is identical. Uniqueness follows by subtracting two candidate intercepts.

The blade angle is not always the velocity heading. The physical heading is $\theta$ when $u>0$ and $\theta+\pi$ when $u<0$ (modulo $2\pi$). Therefore [\[eq:deflection\]](#eq:deflection){reference-type="eqref" reference="eq:deflection"} must not be silently relabelled as a velocity-heading deflection.

# Stability, Poisson form, measure, and reversibility

The entire line $\omega=0$ is reduced equilibrium. At $(u_*,0)$ its linearization has eigenvalues $0$ and $$\label{eq:eigen}
 \lambda_\perp=-\frac{ma}{I_c}u_*.$$ Hence precisely $au_*>0$ is transversely stable. On either open half-plane, $$\label{eq:poisson}
 \{u,\omega\}=\frac{a}{I_c}\omega$$ is a nondegenerate Poisson bracket and $\dot f=\{f,H\}$ reproduces the reduced flow. The density $\rho=1/|\omega|$ satisfies $\nabla\!\cdot(\rho\dot u,\rho\dot\omega)=0$ there.

No positive $C^1$ *reduced* invariant density can cross a nonzero reduced equilibrium: at $(u_*,0)$, invariance would give $0=\rho\,\nabla\!\cdot F=-\rho ma u_*/I_c$, a contradiction. Thus the reduced singularity is structural, not a removable normalization. Multiplying by configuration Haar volume gives an invariant full-flow measure off the singular line, and no smooth density of this Haar-factor form crosses it. However, $(u_*,0)$ with $u_*\ne0$ still reconstructs as translation in the full five-dimensional flow. The pointwise reduced argument therefore does not exclude every possible configuration-dependent full-flow $C^1$ density.

Finally, $$\mathcal R(r,\theta,u,\omega)=(r,\theta,-u,-\omega)$$ satisfies $F(\mathcal Rz)=-D\mathcal R\,F(z)$, so it is a physical-time reversor.

# All degenerate boundaries and recurrence

If $a\ne0$ but $\omega_0=0$, the reduced state is fixed and $r$ is a straight line; $H=0$ is the fully fixed case. Otherwise $\dot u=a\omega^2$ is strictly one-signed, excluding nonconstant recurrence.

If $a=0$, both $u$ and $\omega$ are constant. When $\omega\ne0$, $$r(t)-r(0)=\frac{u}{\omega}
 \bigl(\sin(\theta_0+\omega t)-\sin\theta_0,
 -\cos(\theta_0+\omega t)+\cos\theta_0\bigr),$$ and the complete $SE(2)$ state is periodic with period $2\pi/|\omega|$. When $\omega=0$, motion is straight (fixed if also $u=0$). Thus $a=0$ is a sharp recurrence boundary, not a regular member of the scattering family.

\>1

# Independent certificate and strict Route-A stop

The deterministic ledger uses six rational $(m,J,a,H)$ families, both signs of $a$ and $\omega$, 12 heteroclinic cases, 36 states, and four $a=0$ boundaries. An independent checker imports no producer and closes 737 assertions under recursively exact schema keys. A separate SymPy derivation checks 25 structural and 36 rational hyperbolic identities. Replay is byte exact; twelve repaired-hash attacks (including unknown-key and four mathematical attacks) plus one stale-hash attack are rejected. These tests audit signs and conventions; Theorem [\[thm:normal\]](#thm:normal){reference-type="ref" reference="thm:normal"} and the proofs above establish the continuous result.

The half-plane bracket and the quantum comparison in [@BR08] motivate only a formal operator hint. There is no intrinsic rational-prime primitive-orbit ledger, prime-power repetition law, target Fredholm determinant, target divisor/functional equation, or constructed same-clock operator with the required spectrum. Consequently $$(A0,A1,A2,A3,A4)=(\mathrm{FAIL},\mathrm{FAIL},\mathrm{FAIL},
 \mathrm{FAIL},\mathrm{FORMAL\ HINT}),$$ overall `ROUTE_A_REJECTED`, Route B false, under `NO_BAD_EULER_OR_ROOT_NUMBER`.

#### Claim firewall.

We claim no arithmetic local data, Euler factor, root number, automorphy, target analytic structure, Hilbert--Pólya operator, a smooth global reduced or configuration-Haar-factor density, exclusion of all configuration-dependent full-flow densities, finite-regression proof, exhaustive priority, external review, or acceptance score.

#### Revision focus.

Round 0 freezes the signed convention and proves the explicit all-energy heteroclinic scattering core.

#### Revision focus.

Round 1 adds physical reconstruction, affine asymptotes, stability, Poisson/measure obstruction, reversibility and every degenerate recurrence boundary.

#### Revision focus.

Round 2 adds independent executable closure, source ownership, Route-A evaluation, counterclaim firewall and disclosures.

# Declarations {#declarations .unnumbered}

#### Data and code availability.

Package-local synthetic exact evidence and deterministic code accompany the manuscript; no observational data are used.

#### Ethics.

No human, animal, personal or sensitive data are used; approval is not applicable.

#### Author contributions (CRediT).

This anonymous certificate records Conceptualization, Formal analysis, Software, Validation, Writing---original draft, and Writing---review and editing. AI systems are not authors.

#### Funding.

No external funding is reported.

#### Conflicts of interest.

None known.

#### AI-use disclosure.

An AI coding assistant supported derivation, drafting and exact-code development; it was not an external reviewer or an independent peer-review process.

4 A. M. Bloch, "Asymptotic Hamiltonian dynamics: the Toda lattice, the three-wave interaction and the non-holonomic Chaplygin sleigh," *Physica D* 141 (2000), 297--315. DOI: 10.1016/S0167-2789(00)00046-4. A. V. Borisov and I. S. Mamaev, "The dynamics of a Chaplygin sleigh," *J. Appl. Math. Mech.* 73 (2009), 156--161. DOI: 10.1016/j.jappmathmech.2009.04.005. N. K. Moshchuk, "On the motion of Chaplygin's sledge," *J. Appl. Math. Mech.* 51 (1987), 426--430. DOI: 10.1016/0021-8928(87)90079-7. A. M. Bloch and A. G. Rojo, "Quantization of a Nonholonomic System," *Phys. Rev. Lett.* 101 (2008), 030402. DOI: 10.1103/PhysRevLett.101.030402.
