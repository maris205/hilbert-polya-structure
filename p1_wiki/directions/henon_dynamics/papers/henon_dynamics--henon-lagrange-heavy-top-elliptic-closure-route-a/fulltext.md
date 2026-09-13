---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-lagrange-heavy-top-elliptic-closure-route-a"
canonical_tex: "henon_dynamics/henon_lagrange_heavy_top_elliptic_closure_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_lagrange_heavy_top_elliptic_closure_route_a/paper/main.pdf"
source_sha256: "9fa50f6180161b99de0ee8ede19e3aa79f073b8542f165c56f76618df1971fed"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The Lagrange Top: Cubic Nutation, Two-Phase Reconstruction, and Exact Closure

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_lagrange_heavy_top_elliptic_closure_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_lagrange_heavy_top_elliptic_closure_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_lagrange_heavy_top_elliptic_closure_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_lagrange_heavy_top_elliptic_closure_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For the positive-inertia Lagrange symmetric heavy top we close the regular reduction--reconstruction problem. The inclination is inverted by one Jacobi function, both cyclic phases are complete third-kind elliptic integrals, and the full configuration closes exactly when two normalized phase increments are rational. Pole and repeated-root degenerations are kept outside singular Euler formulas. Exact computation certifies conventions, not the continuum proof.
author:
- 'Source-local theorem reconstruction'
date: '2026-09-03'
title: 'The Lagrange Top: Cubic Nutation, Two-Phase Reconstruction, and Exact Closure'
```

## Markdown 正文

trailerid \[\<C3542026090300000000000000000000\>\<C3542026090300000000000000000000\>\]

# Frozen convention and reduced cubic

Let $A=I_1=I_2>0$, $C=I_3>0$, and $\gamma>0$. In regular $z$-$y$-$z$ Euler angles put $u=\cos\theta$, $L=p_\phi$, and $G=p_\psi$. Our convention is $$H=\frac{p_\theta^2}{2A}+\frac{(L-Gu)^2}{2A(1-u^2)}
   +\frac{G^2}{2C}+\gamma u.                                    \label{eq:H}$$ The two momenta and $E=H$ are conserved. Since $p_\theta=A\dot\theta$, energy gives the reduced cubic owner $$A^2\dot u^2=P(u):=
 2A\left(E-\frac{G^2}{2C}-\gamma u\right)(1-u^2)-(L-Gu)^2.       \label{eq:P}$$ In particular $$P(1)=-(L-G)^2,\qquad P(-1)=-(L+G)^2.                            \label{eq:poles}$$ The smooth Hamiltonian flow is complete: its potential is bounded on compact $\operatorname{SO}(3)$, and positive kinetic energy makes each energy sublevel compact.

[\[thm:main\]]{#thm:main label="thm:main"} A nonsteady regular inclination has finite period if and only if its allowed component of $P\geq0$ is bounded by two simple roots in $(-1,1)$. In the pole-incompatible chamber $L\ne\pm G$, label the roots $$-1<r_1<r_2<1<r_3,\qquad
 P=2A\gamma(u-r_1)(u-r_2)(u-r_3).$$ This is the complete root classification for the regular reduced motion. \>0 The formulas below give its least reduced period, reconstruction, and full closure test.

#### Proof of the reduction.

Allowed positions are exactly $P\geq0$. At a simple turning root the time integral is locally $\int s^{-1/2}ds$, while a double root gives $\int s^{-1}ds$. Equation [\[eq:poles\]](#eq:poles){reference-type="eqref" reference="eq:poles"}, the positive leading coefficient, and the cubic sign pattern give the stated ordering. This also separates finite nutation from a separatrix.

\>0

# Elliptic inversion and two phase increments

Set $$d=r_2-r_1,\quad R=r_3-r_1,\quad
 k^2=\frac{d}{R},\quad \nu^2=\frac{\gamma R}{2A},\quad
 Q_0=\sqrt{2A\gamma R}.$$ Direct substitution proves $$u(t)=r_1+d\,\operatorname{sn}^2(\nu(t-t_0),k),\qquad
 T=\frac{4A}{Q_0}K(k).                                          \label{eq:sn}$$ Indeed $z=(u-r_1)/d$ obeys $A^2d^2\dot z^2=2A\gamma d^2Rz(1-z)(1-k^2z)$.

Hamilton's equations are $$\dot\phi=\frac{L-Gu}{A(1-u^2)},\qquad
\dot\psi=\frac{G}{C}-u\dot\phi .$$ Define the finite complete integrals $$I_N=\frac{2}{Q_0(1-r_1)}
 \Pi\left(\frac{d}{1-r_1},k\right),\qquad
 I_S=\frac{2}{Q_0(1+r_1)}
 \Pi\left(-\frac{d}{1+r_1},k\right).$$ Partial fractions on the outbound and return legs give the two phase reconstruction $$\begin{aligned}
 \Delta\phi&=(L-G)I_N+(L+G)I_S,                                 \label{eq:dphi}\\
 \Delta\psi&=G(1/C-1/A)T+(G-L)I_N+(G+L)I_S.                    \label{eq:dpsi}\end{aligned}$$

[\[thm:closure\]]{#thm:closure label="thm:closure"} The full phase state in $T^*\operatorname{SO}(3)$ closes if and only if $$\frac{\Delta\phi}{2\pi}\in\mathbb Q,\qquad
 \frac{\Delta\psi}{2\pi}\in\mathbb Q.$$ If their reduced denominators are $q_\phi,q_\psi$, the least number of nutations in a full return is $\operatorname{lcm}(q_\phi,q_\psi)$.

After one least return of $(u,\dot u)$, autonomy makes the two angle increments constant. Rational increments therefore suffice. Conversely, a full return must occur after an integer number of reduced returns. For $0<\theta<\pi$, the $z$-$y$-$z$ decomposition is unique modulo independent $2\pi$ shifts of $\phi,\psi$, so both increments must be rational multiples of $2\pi$.

\>1

# Degenerate faces and quantum boundary

If $P(u_0)=P'(u_0)=0$, initial data at $u_0$ give steady precession with two constant angular rates; its regular closure is their rational-ratio test. A nonconstant branch approaching the same double root takes infinite time. A triple root is another critical face and is not inserted into [\[eq:sn\]](#eq:sn){reference-type="eqref" reference="eq:sn"}.

Equation [\[eq:poles\]](#eq:poles){reference-type="eqref" reference="eq:poles"} makes $L=G$ necessary at the north pole and $L=-G$ necessary at the south pole. Euler angles are singular there, so existence and uniqueness come from the smooth group Hamiltonian. If $L=G$ and two turning roots remain interior, formulas [\[eq:sn\]](#eq:sn){reference-type="eqref" reference="eq:sn"}--[\[eq:dpsi\]](#eq:dpsi){reference-type="eqref" reference="eq:dpsi"} have the finite limiting root $r_3=1$; an orbit that reaches the pole is reconstructed in a group chart, not by dividing by $1-u^2$. Sleeping tops, $G=0$, $\gamma=0$ (the quadratic free-top boundary), and $A=C$ are separate faces.

The positive rigid-body metric yields a symmetric elliptic kinetic operator on $C^\infty(\operatorname{SO}(3))$. Elliptic completeness on the closed manifold makes it essentially self-adjoint; bounded real multiplication by $\gamma u$ preserves that property. Its unique closure equals the Friedrichs operator and has compact resolvent. We claim no closed spectrum.

# Evidence, collision boundary, and scope

The executable artifact checks twelve rational parameter rows, sixty reconstruction probes, exact Sturm isolators, four Jacobi substitutions, and the steady/pole faces. A producer-independent checker and a symbolic lane own every stored field; repaired-hash mutations test the schema. These are finite convention receipts, not an enumeration proof.

C186 is the gravity-free Euler top; C244 has no body-axis spin momentum; C344 has a different complex-amplitude Poisson owner; C349 is a holonomic sphere oscillator. Thus this theorem owns the rigid-body two-phase reconstruction. The Route-A tuple is $$(\mathrm{A0\_FAIL},\mathrm{A1\_WEAK},\mathrm{A2\_FAIL},
 \mathrm{A3\_FAIL},\mathrm{A4\_NATURAL\_QUANTIZATION}),$$ and the overall verdict is rejection. Scope is `NO_BAD_EULER_OR_ROOT_NUMBER`; Route B is false. No target local data, Euler factor, root number, automorphy, target divisor or functional equation, target-zero match, or Hilbert--Pólya operator is asserted.

# Sources

Cushman and Bates give an authoritative global Lagrange-top and reduction lineage [@CB]; Audin supplies an authoritative spinning-top integrability source [@Audin]. The formulas and software here are independently reconstructed, without a priority claim.

9 R. Cushman and L. Bates, *Global Aspects of Classical Integrable Systems*, 2nd ed., Birkhäuser, 2015. DOI: [10.1007/978-3-0348-0918-4](https://doi.org/10.1007/978-3-0348-0918-4). M. Audin, *Spinning Tops: A Course on Integrable Systems*, Cambridge University Press, 1996, ISBN 978-0-521-56129-7.
