---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-planar-kepler-conic-collision-regularization-route-a"
canonical_tex: "henon_dynamics/henon_planar_kepler_conic_collision_regularization_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_planar_kepler_conic_collision_regularization_route_a/paper/main.pdf"
source_sha256: "a0e99c86f5cbfc78aabf846519eb10ea67e91ca8aea25afd440d2b26d51922b7"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Planar Kepler Conics, Collision Incompleteness, and the Levi--Civita Configuration Boundary

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_planar_kepler_conic_collision_regularization_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_planar_kepler_conic_collision_regularization_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_planar_kepler_conic_collision_regularization_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_planar_kepler_conic_collision_regularization_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We close a convention-locked theorem package for the attractive planar Kepler Hamiltonian. Runge--Lenz identities classify every nonzero-angular-momentum orbit as an ellipse, parabola, or hyperbola; the negative-energy period and radial action and the positive-energy scattering angle are normalized exactly. The zero-angular-momentum branch reaches the removed collision in finite physical time. Levi--Civita's fixed-energy change of variables gives a smooth configuration equation, while a time-period resonance fixes a continuum rather than isolated primitive orbits. \>0 The radial action is written both as a closed-cycle integral and as its turning-point half-cycle, and all three collision antiderivatives are displayed. \>1 An executable exact ledger and independent symbolic checks delimit the result: the configuration continuation is not a full Ligon--Schaaf symplectomorphism, and the strict Route-A arithmetic gates stop.
author:
- 'Route-A structural certificate HCS-C216'
title: |
  Planar Kepler Conics, Collision Incompleteness, and the\
  Levi--Civita Configuration Boundary
```

## Markdown 正文

suppressoptionalinfo 611

**Keywords:** Kepler problem; Runge--Lenz vector; collision regularization; radial action; fixed-point continuum; Route A.

# Frozen Hamiltonian and invariants

Identify the plane with $\mathbb C$ only when the Levi--Civita map is introduced. For $q\in\mathbb R^2\setminus\{0\}$, $p\in\mathbb R^2$, and $\mu>0$, set $$H(q,p)=\frac{|p|^2}{2}-\frac{\mu}{r},\qquad r=|q|.$$ Hamilton's equations are $\dot q=p$ and $\dot p=-\mu q/r^3$. Along a collision-free solution define $$E=H,\qquad L=q_1p_2-q_2p_1,\qquad
 A=(|p|^2-\mu/r)q-(q\!\cdot\!p)p .                         \tag{1}$$ Differentiation gives $\dot E=\dot L=\dot A=0$. Taking the scalar product and norm of $A$ gives the two identities $$A\!\cdot q=L^2-\mu r,\qquad |A|^2=\mu^2+2EL^2 .          \tag{2}$$

# All-energy conics, period, action, and scattering

Suppose $L\ne0$, let $e=|A|/\mu$, and measure $\theta$ from $A$. Equation (2) is equivalent to $$r(\theta)=\frac{L^2/\mu}{1+e\cos\theta},\qquad
 e^2-1=\frac{2EL^2}{\mu^2}.                                \tag{3}$$ Thus $E<0$ is an ellipse (a circle when $e=0$), $E=0$ a parabola, and $E>0$ a hyperbola. In the bound case put $a=-\mu/(2E)$ and $r_\pm=a(1\pm e)$. Kepler's period and the radial momentum are $$P(E)=2\pi\mu(-2E)^{-3/2},\qquad
 p_r^2=2\left(E+\frac\mu r\right)-\frac{L^2}{r^2}.          \tag{4}$$ The normalization is part of the theorem, not a convention left implicit: $$J_r=\frac{1}{2\pi}\oint p_r\,\,\mathrm dr
 =\frac{1}{\pi}\int_{r_-}^{r_+}p_r\,\,\mathrm dr
 =\frac{\mu}{\sqrt{-2E}}-|L|,\qquad E<0 .                \tag{5}$$ The turning-point substitution also gives $\partial_EJ_r=P(E)/(2\pi)$. For $E>0$, the asymptotic directions of (3) have $\cos\theta_\infty=-1/e$, so the unsigned hyperbolic deflection is $$\chi=2\arcsin(1/e),\qquad e>1 .                          \tag{6}$$

\>0

# The radial collision boundary

When $L=0$, the inward branch obeys $$\dot r^2=2(E+\mu/r),\qquad
 t_{\rm coll}(r_0)=\int_0^{r_0}\frac{\,\mathrm dr}{\sqrt{2(E+\mu/r)}}<\infty, \tag{7}$$ for every admissible starting radius. The endpoint $r=0$ is absent from the physical phase space, hence the physical flow is incomplete. With $\alpha=-E>0$, $u=\arcsin\sqrt{\alpha r_0/\mu}$ gives $$t_{\rm coll}=\frac{\mu}{\sqrt2\alpha^{3/2}}
 (u-\sin u\cos u);$$ for $E=0$ it is $2r_0^{3/2}/(3\sqrt{2\mu})$, while for $E>0$, with $u=\operatorname{arsinh}\sqrt{Er_0/\mu}$, it is $$t_{\rm coll}=\frac{\mu}{\sqrt2E^{3/2}}
 (\sinh u\cosh u-u).                                       \tag{8}$$ These formulas separate the collision boundary from the $L\ne0$ conic classification; no collision is silently counted as a periodic orbit.

\>1

# Levi--Civita equation and what is (not) extended

Write $q=u^2$ with $u\in\mathbb C$, and set $\,\mathrm dt=|u|^2\,\mathrm d\tau$. On a fixed energy level, direct substitution gives $$u''=\frac E2u,\qquad 2|u'|^2-E|u|^2=\mu,\qquad
 L=2\operatorname{Im}(\bar u u').                           \tag{9}$$ The equation in $\tau$ is smooth through $u=0$, so (9) supplies a configuration-level collision continuation. The physical time density then vanishes at the collision. We make no claim of a global canonical transformation, a full Ligon--Schaaf symplectomorphism, or a three-dimensional regularization theorem.

# Fixed-time resonance and strict stop

Every collision-free ellipse at energy $E<0$ has the same period $P(E)$. Consequently a time-$T$ map has the fixed continuum $$\{H=E,\ L\ne0\}\quad\text{whenever}\quad T=mP(E),\qquad m\in\mathbb N. \tag{10}$$ This set has dimension three in the four-dimensional phase space, so ordinary isolated Artin--Mazur primitive-orbit counting is undefined on the resonant shells. Parabolic and hyperbolic noncollision trajectories escape and have no finite period.

The release ledger has 10 exact orbit rows, 4 radial rows, 12 Levi--Civita rows, and 5 fixed-set rows. The producer-independent checker passes 260 assertions; the SymPy cross-check passes 17 identities; replay is byte exact; and 25 hostile mutations are rejected (24 repaired-hash plus one stale-hash, including an unknown-key injection). These finite rows are regression evidence only.

The source-attributed classical references are Levi--Civita [\[LC1920\]](https://doi.org/10.1007/BF02404404), Moser [\[M70\]](https://doi.org/10.1002/cpa.3160230406), and Ligon--Schaaf [\[LS76\]](https://doi.org/10.1016/0034-4877(76)90061-6); no priority claim is made. With scope `NO_BAD_EULER_OR_ROOT_NUMBER`, $$(A0,A1,A2,A3,A4)=({\rm FAIL},{\rm WEAK},{\rm FAIL},{\rm FAIL},
 {\rm NATURAL\ QUANTIZATION}),$$ overall `ROUTE_A_REJECTED`; Route B is false. The natural Coulomb/oscillator quantization hint is not an operator construction. No target primes or zeros, arithmetic local data, Euler factors, root numbers, automorphy, target functional equation, or Hilbert--Pólya operator is used or claimed.

3 T. Levi--Civita, "Sur la régularisation du problème des trois corps," *Acta Mathematica* 42 (1920), 99--144. DOI: [10.1007/BF02404404](https://doi.org/10.1007/BF02404404). J. Moser, "Regularization of Kepler's problem and the averaging method on a manifold," *Communications on Pure and Applied Mathematics* 23 (1970), 609--636. DOI: [10.1002/cpa.3160230406](https://doi.org/10.1002/cpa.3160230406). T. Ligon and M. Schaaf, "On the global symmetry of the classical Kepler problem," *Reports on Mathematical Physics* 9 (1976), 281--300. DOI: [10.1016/0034-4877(76)90061-6](https://doi.org/10.1016/0034-4877(76)90061-6).

#### Revision focus.

Round 0 freezes the Hamiltonian, invariants, conic equation, and energy-sign classification.

#### Revision focus.

Round 1 adds the action normalization, all collision antiderivatives, and the physical incompleteness boundary.

#### Revision focus.

Round 2 adds Levi--Civita scope, integer strobe resonance, executable counts, source attribution, and the strict Route-A stop.

# Declarations {#declarations .unnumbered}

**Data and code.** Synthetic exact probes and package-local deterministic code accompany the manuscript; no training data are used. **Ethics/funding.** No human or animal data; no external funding reported. **AI disclosure.** An AI coding assistant supported drafting and exact-code development; it was not an external reviewer or independent error process.
