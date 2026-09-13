---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-isochrone-action-frequency-route-a"
canonical_tex: "henon_dynamics/henon_isochrone_action_frequency_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_isochrone_action_frequency_route_a/paper/main.pdf"
source_sha256: "67dfefa37c6b19cb88106841853874ced4e7ed5b99606330e6e28644b3446b47"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Complete Bound Action--Frequency and Closed-Orbit Atlas for the Hénon Isochrone Potential

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_isochrone_action_frequency_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_isochrone_action_frequency_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_isochrone_action_frequency_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_isochrone_action_frequency_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We close the bound action--frequency geometry of the planar Hénon isochrone Hamiltonian, with its exact circular-energy boundary. =0 A quadratic turning-point reduction gives the angular-momentum-independent radial period and hence the radial action on its full admissible domain. \>0 An independent apsidal integral yields the frequency map and the exact noncircular closure criterion; circular, center-crossing, escape, signed angular-momentum, and Kepler-limit faces are separated explicitly. \>1 A 116-cell exact certificate, independent symbolic and quadrature checks, 87/87 hostile rejections, and a conservative Route-A audit accompany the proof. The finite grid is not the proof.
author:
- 'Route-A source-local certificate HCS-C295'
date: 2 September 2026
title: |
  A Complete Bound Action--Frequency and Closed-Orbit Atlas\
  for the Hénon Isochrone Potential
```

## Markdown 正文

trailerid \[\<C2952026090200000000000000000000\>\<C2952026090200000000000000000000\>\] suppressoptionalinfo 512

# Model, conventions, and provenance

Let $\mu,b>0$. In polar variables the unit-mass Hamiltonian is $$\label{eq:H}
 H(r,p_r,L)=\frac{p_r^2}{2}+\frac{L^2}{2r^2}
 -\frac{\mu}{b+\sqrt{b^2+r^2}}.$$ Put $\ell=\lvert L\rvert$, $$\label{eq:AB}
 A=\sqrt{\ell^2+4\mu b},\qquad B=\ell+A,$$ and use physical Hamiltonian time. For $\ell>0$, the radial action is $$\label{eq:actiondef}
 J_r=\frac1\pi\int_{r_p}^{r_a}
 \sqrt{2(E-U_\ell(r))}\,\mathrm dr,
 \quad
 U_\ell(r)=\frac{\ell^2}{2r^2}
 -\frac{\mu}{b+\sqrt{b^2+r^2}}.$$ At $\ell=0$ we use its continuous half-line limit and discuss the full Cartesian return separately.

The potential and its orbit mechanics are classical, originating in Hénon's two 1959 papers [@HenonI; @HenonII]. Ramond and Perez give a modern isochrone-mechanics treatment [@RamondPerez]; Fouvry and Prunet record the frequency map in their official Appendix C [@FouvryPrunet]. We rederive the formulas to close a reproducible certificate and make no claim of literature priority.

# Complete bound action theorem

[\[thm:core\]]{#thm:core label="thm:core"} For fixed $\mu,b>0$ and $\ell\geq0$, define $$\label{eq:circ}
 s_c=\frac{B^2}{4\mu},\qquad r_c^2=s_c^2-b^2,
 \qquad E_c=-\frac{\mu}{2s_c}=-\frac{2\mu^2}{B^2}.$$ Bound motion exists exactly for $E_c\leq E<0$. On this domain, $$\begin{aligned}
 J_r&=\frac{\mu}{\sqrt{-2E}}-\frac B2,\label{eq:J}\\
 H(J_r,\ell)&=-\frac{\mu^2}{2(J_r+B/2)^2},\label{eq:HJ}\\
 T_r&=\frac{2\pi\mu}{(-2E)^{3/2}},\qquad
 \Omega_r=\frac{(-2E)^{3/2}}{\mu}.\label{eq:Tr}\end{aligned}$$ In particular, $J_r\geq0$ is equivalent to $E\geq E_c$ inside $E<0$, and $T_r$ is independent of angular momentum.

Write $s=\sqrt{b^2+r^2}\geq b$. For $\ell>0$, differentiation of $$U_\ell(s)=-\frac{\mu}{b+s}
 +\frac{\ell^2}{2(s^2-b^2)}$$ gives the circular equation $\mu(s-b)^2=\ell^2s$. Its unique solution above $b$ is $s_c=B^2/(4\mu)$, and substitution gives [\[eq:circ\]](#eq:circ){reference-type="eqref" reference="eq:circ"}. The effective potential tends to $+\infty$ at zero, to $0^-$ at infinity, and has only this critical point, hence this is its global minimum. When $\ell=0$, the potential increases from $-\mu/(2b)$ to zero, and the same formulas give the central minimum. This proves the asserted energy domain.

For the period, set $$\label{eq:xQ}
 x=b+\sqrt{b^2+r^2},\quad r^2=x(x-2b),\quad
 Q(x)=2Ex^2+(2\mu-4bE)x-(4\mu b+\ell^2).$$ A direct substitution in the energy equation gives $$\label{eq:dt}
 \mathrm dt=\frac{x-b}{\sqrt{Q(x)}}\,\mathrm dx.$$ For a noncircular bound orbit, put $q=-2E>0$ and write $Q=q(x_a-x)(x-x_p)$. Vieta's identities give $$\label{eq:vieta}
 x_p+x_a=2b+\frac{2\mu}{q},\qquad
 x_px_a=\frac{A^2}{q}.$$ The arcsine substitution on $[x_p,x_a]$ therefore yields $$\int_{x_p}^{x_a}\frac{x-b}{\sqrt{Q(x)}}\,\mathrm dx
 =\frac{\pi}{\sqrt q}\left(\frac{x_p+x_a}{2}-b\right)
 =\frac{\pi\mu}{q^{3/2}}.$$ Doubling proves [\[eq:Tr\]](#eq:Tr){reference-type="eqref" reference="eq:Tr"}; the circular value follows by continuity.

Finally, differentiation of the one-dimensional action integral gives $\partial_EJ_r=T_r/(2\pi)=\mu/(-2E)^{3/2}$. Thus $J_r=\mu/\sqrt{-2E}+C(\ell)$. The circular cycle collapses, so $J_r(E_c,\ell)=0$; since $\mu/\sqrt{-2E_c}=B/2$, this fixes $C=-B/2$ and proves [\[eq:J\]](#eq:J){reference-type="eqref" reference="eq:J"}. Inversion gives [\[eq:HJ\]](#eq:HJ){reference-type="eqref" reference="eq:HJ"}, and differentiating it in $J_r$ gives $\Omega_r$.

Below the circular minimum no real radial interval exists. At $E=0$ the motion reaches the marginal escape threshold, while $E>0$ is unbound. Equations [\[eq:J\]](#eq:J){reference-type="eqref" reference="eq:J"} and [\[eq:Tr\]](#eq:Tr){reference-type="eqref" reference="eq:Tr"} show that both action and period diverge as $E\uparrow0$; the threshold is not a finite action point.

\>0

# Apsidal map and noncircular closure

[\[thm:closure\]]{#thm:closure label="thm:closure"} For $L\geq0$ and $\ell>0$, $$\label{eq:beta}
 \frac{\Omega_\phi}{\Omega_r}=\beta(\ell)
 =\frac12\left(1+\frac{\ell}{\sqrt{\ell^2+4\mu b}}\right),
 \qquad \frac12<\beta<1.$$ The azimuthal advance in one radial period is $2\pi\beta$. A noncircular bound phase-space orbit closes if and only if $\beta\in\mathbb Q$. If $\beta=p/q$ in lowest terms, its primitive period is $qT_r$.

Because $\dot\phi=\ell/r^2$, equations [\[eq:dt\]](#eq:dt){reference-type="eqref" reference="eq:dt"} and [\[eq:xQ\]](#eq:xQ){reference-type="eqref" reference="eq:xQ"} reduce the half-cycle angular integral by $$\label{eq:pf}
 \frac{x-b}{x(x-2b)}=\frac12\left(\frac1x+\frac1{x-2b}\right).$$ Besides [\[eq:vieta\]](#eq:vieta){reference-type="eqref" reference="eq:vieta"}, Vieta gives the shifted product $$\label{eq:shifted}
 (x_p-2b)(x_a-2b)=\frac{\ell^2}{q}.$$ Using $\int_{x_p}^{x_a}\mathrm dx/[x\sqrt{(x_a-x)(x-x_p)}]
=\pi/\sqrt{x_px_a}$ and its shifted counterpart in [\[eq:pf\]](#eq:pf){reference-type="eqref" reference="eq:pf"}, the periapsis-to-apoapsis angle is $$\frac{\ell}{2\sqrt q}\left(
 \frac\pi{\sqrt{x_px_a}}+
 \frac\pi{\sqrt{(x_p-2b)(x_a-2b)}}\right)
 =\frac\pi2\left(1+\frac\ell A\right).$$ Doubling proves the advance and [\[eq:beta\]](#eq:beta){reference-type="eqref" reference="eq:beta"}. The same ratio follows by differentiating [\[eq:HJ\]](#eq:HJ){reference-type="eqref" reference="eq:HJ"}: $\Omega_\phi=\partial_\ell H$ and $\partial_\ell(B/2)=\beta$.

For a nonconstant radial phase, a phase-space return must occur after an integer number $q$ of radial cycles. Angular return is then exactly $q\beta\in\mathbb Z$, equivalent to rational $\beta$; lowest terms give primitivity.

# Exceptional and limiting faces

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Face                          Exact interpretation
  ----------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Circular, $E=E_c$, $\ell>0$   The orbit is closed for every value of the epicyclic ratio. Its actual period is $2\pi/\Omega_\phi$; the noncircular rationality test does not apply.

  Central equilibrium           At $\ell=0,E=E_c=-\mu/(2b)$, the particle is stationary at the smooth center.

  Center crossing               At $\ell=0,E_c<E<0$, the radius repeats after $T_r$, but velocity orientation reverses. The full Cartesian period is $2T_r$; the one-sided limiting ratio is $1/2$.

  Signed momentum               Replacing $L>0$ by $L<0$ reverses $\Omega_\phi$. The geometry and radial formulas depend only on $\ell=\lvert L\rvert$.

  Kepler limit                  At fixed $\ell>0$, $b\downarrow0$ gives $J_r\to\mu/\sqrt{-2E}-\ell$ and $\beta\to1$. The simultaneous $b,\ell\to0$ corner reaches the Kepler collision singularity.
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

These clauses are logically necessary. In particular, calling every irrational-ratio circle nonclosed, or calling $T_r$ the full Cartesian period at $L=0$, would be false.

\>1

# Finite certificate and independent validation

The deterministic certificate samples $\mu,b\in\{1,2,3\}$, $\ell\in\{0,1,2,3\}$, and $I=kB/2$ for $k\in\{1,2,3\}$. Its 108 orbit cells store exact quadratic-field coefficients $a+c\sqrt d$, supplemented by eight boundary cells. Their closure partition is 36 circular or equilibrium, 18 radial center-crossing, 14 rational resonant, and 40 irrational rosette cells.

The producer-independent checker reconstructs every algebraic field and performs direct 90-digit period and apsidal quadratures. A separate SymPy program checks 1,099 symbolic/exact identities; two fresh paths replay the evidence byte for byte. A hostile suite rejects 87/87 repaired-hash and raw parser attacks. Both JSON and YAML use strict duplicate-key-rejecting validation; YAML anchors, aliases, merges, non-string keys, and implicit timestamp coercion are excluded. Enumeration is regression evidence only: Theorem [\[thm:core\]](#thm:core){reference-type="ref" reference="thm:core"} and Theorem [\[thm:closure\]](#thm:closure){reference-type="ref" reference="thm:closure"} are all-parameter analytic statements.

# Natural quantization and Route-A boundary

In Cartesian coordinates, $$V(x)=-\frac{\mu}{b+\sqrt{b^2+\lvert x\rvert^2}}$$ is a real bounded function, $-\mu/(2b)\leq V<0$. Hence $-\hbar^2\Delta/2+V$ is self-adjoint on $H^2(\mathbb R^2)$ and semibounded, by the bounded-perturbation theorem. This is a natural Schrödinger quantization, but its spectrum is not analyzed here and it is not a target Hilbert--Pólya operator.

Resonant closed orbits are intrinsic, but form continuous energy and rotational families rather than an isolated primitive ledger. Therefore the frozen evaluator assigns $$(A0\_FAIL,A1\_WEAK,A2\_FAIL,A3\_FAIL,
 A4\_NATURAL\_QUANTIZATION),$$ with overall `ROUTE_A_REJECTED`. There is no arithmetic local carrier, dynamical determinant, target analytic bridge, or Route-B input.

# Limitations, scope, and declarations

The scope literal is `NO_BAD_EULER_OR_ROOT_NUMBER`. We do not assert arithmetic local data, Euler factors, root numbers, automorphy, a target divisor law, a target functional equation, a target zero match, or a Hilbert--Pólya realization. Closed resonant tori are not relabeled as isolated arithmetic primitive owners, and classical isochrone formulas are not claimed as new.

#### Data and code availability.

All evidence, source, strict evaluation, replay and mutation programs, three paper rounds, and the self-excluding release manifest are included in the HCS-C295 package.

#### Ethics.

No human participants, animals, personal data, or field interventions were involved.

#### Conflicts and funding.

No competing interests or external funding are declared.

#### Contributor roles.

The route-certificate author performed derivation, software construction, validation design, and manuscript preparation.

#### AI-use disclosure.

Generative tooling assisted drafting and code scaffolding. Exact identities, independent implementations, adversarial tests, and release hashes provide the stated verification; AI output is not treated as evidence by itself.

9 M. Hénon, "L'amas isochrone I," *Annales d'Astrophysique* **22** (1959), 126--139; ADS bibcode 1959AnAp\...22..126H.

M. Hénon, "L'amas isochrone II: Le calcul des orbites," *Annales d'Astrophysique* **22** (1959), 491--498; ADS bibcode 1959AnAp\...22..491H.

P. Ramond and J. Perez, "New Methods of Isochrone Mechanics," *Journal of Mathematical Physics* **62** (2021), 112704; [DOI 10.1063/5.0056957](https://doi.org/10.1063/5.0056957), [arXiv:2104.05643](https://arxiv.org/abs/2104.05643).

J.-B. Fouvry and S. Prunet, "Linear response theory and damped modes of stellar clusters," *Monthly Notices of the Royal Astronomical Society* **509** (2022), 2443--2456; [DOI 10.1093/mnras/stab3020](https://doi.org/10.1093/mnras/stab3020).
