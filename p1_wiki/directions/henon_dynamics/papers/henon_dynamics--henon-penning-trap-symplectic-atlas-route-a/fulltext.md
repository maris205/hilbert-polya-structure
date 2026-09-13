---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-penning-trap-symplectic-atlas-route-a"
canonical_tex: "henon_dynamics/henon_penning_trap_symplectic_atlas_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_penning_trap_symplectic_atlas_route_a/paper/main.pdf"
source_sha256: "cafefde112c16ec18e82e222563c9edf53d44115e33fcfd7e7bd667b6109a6e7"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Exact Symplectic Flow and the Complete Stability--Resonance Atlas of the Ideal Penning Trap

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_penning_trap_symplectic_atlas_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_penning_trap_symplectic_atlas_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_penning_trap_symplectic_atlas_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_penning_trap_symplectic_atlas_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We solve the ideal axially symmetric Penning Hamiltonian throughout its signed field--axial-frequency plane. One entire rotating-frame formula gives the exact six-dimensional symplectic flow, the sharp magnetic-confinement threshold, its critical Jordan collision, and the unstable splitting. In the stable chamber we derive signed actions and the negative magnetron Krein sign. \>1 We also prove the active-mode resonance criterion, true minimal periods, and all stable and boundary strobe fixed spaces. Every zero-field, zero-axial, free, and field-sign boundary is explicit. The result is candidate-local and supplies no target spectral interpretation.
author:
- HCS Research Program
date: 1 September 2026
title: |
  Exact Symplectic Flow and the Complete\
  Stability--Resonance Atlas of the Ideal Penning Trap
```

## Markdown 正文

# Hamiltonian and exact flow

In the symmetric gauge, absorb mass and charge into the signed cyclotron frequency $c\in\mathbb R$, and let the axial frequency be $\zeta\geq0$. For $X=(x,y,z,p_x,p_y,p_z)$ put $$H=\frac12\{(p_x+cy/2)^2+(p_y-cx/2)^2+p_z^2\}
   +\frac{\zeta^2}{2}\left(z^2-\frac{x^2+y^2}{2}\right).
 \tag{1}$$ \>1 Brown and Gabrielse [@BrownGabrielse1982] are cited here only for the ideal-trap Hamiltonian and frequency normalization as model lineage; no displayed formula or proof step is outsourced to that source. Set $u=x+iy$, $v=\dot u$, and $\Delta=c^2-2\zeta^2$. Hamilton's equations are $$u''+icu'-\frac{\zeta^2}{2}u=0,\qquad z''+\zeta^2z=0. \tag{2}$$ Define the entire fundamental pair $$C_\Delta(t)=\cos(\sqrt\Delta\,t/2),\qquad
 S_\Delta(t)=\frac{\sin(\sqrt\Delta\,t/2)}{\sqrt\Delta/2},$$ where $(C_0,S_0)=(1,t)$ and negative $\Delta$ means the corresponding $\cosh/\sinh$ continuation.

For every $(c,\zeta,t)\in\mathbb R\times[0,\infty)\times\mathbb R$, $$\begin{aligned}
u(t)&=e^{-ict/2}\{(C_\Delta+icS_\Delta/2)u_0+S_\Delta v_0\},\tag{3}\\
v(t)&=e^{-ict/2}\{\zeta^2S_\Delta u_0/2+(C_\Delta-icS_\Delta/2)v_0\}.\tag{4}\end{aligned}$$ Together with $z(t)=\cos(\zeta t)z_0+\sin(\zeta t)v_{z0}/\zeta$ and its $\zeta=0$ limit, these formulas define a real canonical matrix $M_c(t)\in\mathrm{Sp}(6,\mathbb
R)$, with $M_c(t+s)=M_c(t)M_c(s)$, determinant one, and conserved $H$.

For $\zeta>0$, every orbit is bounded exactly when $\Delta>0$. At $\Delta=0$ generic radial solutions grow linearly and boundedness is equivalent to $v_0=-icu_0/2$. For $\Delta<0$ generic radial growth has exponent $\sqrt{-\Delta}/2$; the all-time bounded space is the axial plane, while the forward-bounded radial plane is $$v_0=-\{\sqrt{-\Delta}/2+ic/2\}u_0.$$

The rotation $u=e^{-ict/2}w$ reduces (2) to $w''+\Delta w/4=0$. Its fundamental matrix is $\bigl(\begin{smallmatrix}C_\Delta&S_\Delta\\
-\Delta S_\Delta/4&C_\Delta\end{smallmatrix}\bigr)$; undoing the rotation gives (3)--(4). In physical variables $$v_x=p_x+cy/2,\quad v_y=p_y-cx/2,\quad v_z=p_z,$$ let $T_c(q,p)=(q,v)$. The exact canonical matrix is therefore $M_c(t)=T_c^{-1}V_c(t)T_c$, where $V_c$ is the real form of (3)--(4) together with the axial block. This is an explicit $6$ by $6$ formula.

Alternatively, differentiating it at zero gives $A=J\nabla^2H$. Since $A^{T}J+JA=0$, uniqueness gives $M_c(t)=e^{tA}$ and hence symplecticity, the group law, determinant one, and conservation of the quadratic Hamiltonian. For positive, zero, or negative $\Delta$, the reduced equation is respectively elliptic, a two-step Jordan shear, or hyperbolic. The stated subspaces follow by setting the growing/Jordan coefficient to zero; the axial oscillator is always bounded when $\zeta>0$.

# Signed stable actions

Assume $\zeta>0$ and $\Delta>0$. Then $c\ne0$; write $r=\sqrt\Delta$, $\sigma=\operatorname{sgn}(c)$, and $$\omega_+=\frac{|c|+r}{2},\qquad \omega_-=\frac{|c|-r}{2}.$$ \>1 The modified-cyclotron and magnetron labels follow the systematic ideal-trap review of Brown and Gabrielse [@BrownGabrielse1986]; the amplitudes, signed normal form, and Krein conclusion below are derived locally.

There are unique amplitudes $$A_+=\frac{i\sigma v_0-\omega_-u_0}{r},\qquad
 A_-=\frac{\omega_+u_0-i\sigma v_0}{r}$$ such that $u=A_+e^{-i\sigma\omega_+t}+A_-e^{-i\sigma\omega_-t}$. With $$I_+=\frac r2|A_+|^2,\quad I_-=\frac r2|A_-|^2,\quad
 I_z=\frac{v_z^2+\zeta^2z^2}{2\zeta},$$ the Hamiltonian is $$H=\omega_+I_+-\omega_-I_-+\zeta I_z. \tag{5}$$ Thus the Krein/energy signs are positive modified-cyclotron, negative magnetron, and positive axial.

The amplitudes solve the two equations at $t=0$. Since $\omega_+\omega_-=\zeta^2/2$ and $\omega_+-\omega_-=r$, substituting the two modes into $H_{\rm rad}=|v|^2/2-\zeta^2|u|^2/4$ cancels the cross terms and gives the first two terms of (5). The axial term gives the third. The energy signs of the three elliptic symplectic planes are their Krein signs. In particular, the negative magnetron sign is not dynamical growth inside $\Delta>0$.

# Full boundedness and boundary audit

The theorem already resolves $\zeta>0$. Its real dimensions are $$\begin{array}{c@{\quad}c@{\quad}c}
\Delta>0&\Delta=0&\Delta<0\\
\dim E_{\rm b}=6&\dim E_{\rm b}=4&\dim E_{\rm b}=2,\quad
\dim E_{\rm fb}=4.
\end{array}$$

\>0

If $\zeta=0$ and $c\ne0$, the radial motion is a cyclotron circle about a fixed guiding centre and $z=z_0+t v_{z0}$; hence the all-time bounded space has dimension five. If $c=\zeta=0$, the motion is free and its bounded subspace has dimension three. If $c=0,\zeta>0$, radial growth has exponent $\zeta/\sqrt2$, so electrostatic axial confinement alone cannot confine the radial plane. Finally $$R(x,y,z,p_x,p_y,p_z)=(x,-y,z,p_x,-p_y,p_z)$$ obeys $RM_c(t)R=M_{-c}(t)$.

Putting $\zeta=0$ in (2) gives $v(t)=e^{-ict}v_0$ and a constant guiding centre; only nonzero axial velocity is unbounded. The corner $c=0$ leaves three free coordinates. At $c=0,\zeta>0$, $\Delta=-2\zeta^2$ gives the stated hyperbolic exponent. Direct substitution in (1), or in Hamilton's equations, proves the conjugacy. Thus the limits $\zeta=0$, $B=0$, complete freedom, and signed-field reversal introduce no omitted chamber.

At the magnetic-confinement threshold $\Delta=0$, writing $q=v+icu/2$ gives $$u(t)=e^{-ict/2}(u_0+tq_0),\qquad q(t)=e^{-ict/2}q_0.$$ This exhibits the critical Jordan direction and proves that its linear growth cannot be removed by diagonalizing coincident frequencies.

\>1

# Active modes, minimal periods, and strobes

For an orbit in the stable chamber, call a mode active when its complex amplitude (or axial action) is nonzero.

A nonstationary stable orbit is closed if and only if its active labeled modes in $(\omega_+,\omega_-,\zeta)$ are rationally commensurate. If the active frequencies are $n_jg$, where $n_j\in\mathbb N$ and $\gcd_j n_j=1$, then its minimal period is $2\pi/g$. Put $(f_1,f_2,f_3)=(\omega_+,\omega_-,\zeta)$, retaining mode labels when frequencies coincide. For every strobe time $\tau>0$, $$\dim\operatorname{Fix}M_c(\tau)=2\#\{j\in\{1,2,3\}:f_j\tau\in2\pi\mathbb Z\}. \tag{6}$$ On the critical face, the radial contribution is two exactly when $c\tau/2\in2\pi\mathbb Z$; the Jordan direction never fixes. For $\zeta=0,c\ne0$, the fixed dimension is three plus two when $|c|\tau\in2\pi\mathbb Z$. At the free corner it is three.

On each active elliptic plane the flow is a genuine rotation. Linear independence of the mode planes makes a return equivalent to simultaneous phase returns. Rational commensurability is therefore necessary and sufficient. If a smaller positive time returned every phase, its multiple of $g$ would be a common period of the primitive integers $n_j$, contradicting their gcd; hence $2\pi/g$ is minimal. Counting the two real dimensions of each returning block gives (6).

At criticality, the displayed shear fixes a nonzero radial vector only when the common rotation returns and $q_0=0$, giving dimension two; the Jordan direction cannot fix for $\tau>0$. On the zero-axial face, two guiding-centre coordinates and constant $z$ always fix, while the cyclotron plane adds two at return. The free shear fixes precisely the zero-velocity space. In the unstable chamber the radial multipliers have moduli different from one, so only an axial return can contribute a fixed plane.

The same argument classifies closed boundary orbits. Critical bounded orbits may activate the radial rotation and the axial oscillator, whose ratio is $\sqrt2$ and hence forbids a mixed return; unstable closed orbits lie on the axial plane; zero-axial bounded nonstationary orbits have cyclotron period $2\pi/|c|$; and free closed orbits are stationary.

# Evidence, Route A, and claim boundary

The deterministic receipt contains 48 complete $6$ by $6$ flow matrices, 24 mode/action rows, 13 strobe rows, 7 minimal-period rows, and 9 boundary rows, for 2,743 explicitly recounted numeric cells. A producer-independent implementation passes 3,664 assertions; the symbolic audit passes 96 identities; replay is byte-exact; and all 26/26 repaired-hash hostile mutations are rejected. These are regression checks, not a finite proof of the theorem.

\>1

  Receipt or gate                                                    Result
  ----------------------------------------------- -------------------------
  Flow / mode / strobe / period / boundary rows              $48/24/13/7/9$
  Independent assertions / symbolic identities            $3{,}664/96$ PASS
  Fresh byte replay / repaired-hash mutations       PASS / $26/26$ rejected
  Evidence SHA-256                                    `d926343f3071…c1ddca`

The active-mode resonance theorem earns only `A1_WEAK`: resonant trajectories fill clean positive-dimensional invariant families, not an isolated primitive ledger. Canonical ideal-trap quantization is natural, but the signed magnetron ladder is candidate-local and is not a target divisor, determinant, or Hilbert--Pólya spectrum. The strict tuple is

`(A0_FAIL, A1_WEAK, A2_FAIL, A3_FAIL,`\
`A4_NATURAL_QUANTIZATION)`, hence `ROUTE_A_REJECTED`.

Route B is not invoked. The theorem status is **PROVABLE AS STATED**. The scope firewall is

`NO_BAD_EULER_OR_ROOT_NUMBER`.

No arithmetic local data, Euler factor, root number, automorphy, target counting law, target divisor, or Hilbert--Pólya operator is claimed.

\>1

9 L. S. Brown and G. Gabrielse, "Precision spectroscopy of a charged particle in an imperfect Penning trap," *Physical Review A* **25**, no. 4 (1982), 2423(R)--2425(R). DOI: [10.1103/PhysRevA.25.2423](https://doi.org/10.1103/PhysRevA.25.2423).

L. S. Brown and G. Gabrielse, "Geonium theory: Physics of a single electron or ion in a Penning trap," *Reviews of Modern Physics* **58**, no. 1 (1986), 233--311. DOI: [10.1103/RevModPhys.58.233](https://doi.org/10.1103/RevModPhys.58.233).

These primary records establish model lineage and terminology only; no displayed result or proof step is delegated to them, and no priority or experimental-performance claim is made.

# Primary sources {#primary-sources .unnumbered}

L. S. Brown and G. Gabrielse, "Precision spectroscopy of a charged particle in an imperfect Penning trap," *Physical Review A* **25** (1982), 2423(R). DOI: [10.1103/PhysRevA.25.2423](https://doi.org/10.1103/PhysRevA.25.2423).

L. S. Brown and G. Gabrielse, "Geonium theory: Physics of a single electron or ion in a Penning trap," *Reviews of Modern Physics* **58** (1986), 233--311. DOI: [10.1103/RevModPhys.58.233](https://doi.org/10.1103/RevModPhys.58.233). These primary records establish model lineage and terminology; no priority or experimental-performance claim is made.
