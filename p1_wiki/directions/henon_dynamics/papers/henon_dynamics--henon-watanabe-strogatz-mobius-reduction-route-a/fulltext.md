---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-watanabe-strogatz-mobius-reduction-route-a"
canonical_tex: "henon_dynamics/henon_watanabe_strogatz_mobius_reduction_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_watanabe_strogatz_mobius_reduction_route_a/paper/main.pdf"
source_sha256: "034798c09b856b85d79bb693f5c251f8cf80e68bff7f450693a60e8eec342f51"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Common First-Harmonic Forcing as a Möbius Flow: Cross-Ratio Leaves, Collision Strata, and the Constant Trichotomy

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_watanabe_strogatz_mobius_reduction_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_watanabe_strogatz_mobius_reduction_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_watanabe_strogatz_mobius_reduction_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_watanabe_strogatz_mobius_reduction_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For every $N\ge3$ and every common time-dependent first-harmonic forcing, we lift the identical phase equations to one $\operatorname{SU}(1,1)$ fundamental matrix and hence one $\operatorname{PSU}(1,1)$ Möbius flow acting on all phases. Three distinct phases determine the moving frame; a generic labelled configuration has exactly $N-3$ independent real cross ratios. Injectivity retains every collision partition and gives orbit dimensions one, two, and three for one, two, and at least three clusters. For constant forcing, a scalar quadratic identity classifies identity, elliptic, parabolic, and hyperbolic generators; the elliptic projected period is $2\pi/\sqrt{\omega^2-|H|^2}$. Exact finite certificates audit these conventions but do not prove the infinite family. Elliptic resonances fix continua and the parameters have no intrinsic arithmetic origin, so Route A stops before a dynamical Euler product.
author:
- 'Route-A structural certificate C189'
title: 'Common First-Harmonic Forcing as a Möbius Flow: Cross-Ratio Leaves, Collision Strata, and the Constant Trichotomy'
```

## Markdown 正文

suppressoptionalinfo 611

**Keywords:** identical phase oscillators; Watanabe--Strogatz reduction; Möbius group; cross ratio; collision strata.

chinese-simplified

中文摘要

对任意 $N\ge3$ 及任意共同的时变一阶谐波强迫，本文把全体相位方程提升为同一个 [SU(1,1)]{lang="en"} 基本矩阵，从而得到作用于全部相位的单一 [Möbius]{lang="en"} 流。三个互异相位决定移动标架；一般标号构型 恰有 $N-3$ 个独立实交比。映射的单射性保持所有碰撞分拆，并统一覆盖同步及多簇 边界。常系数生成元由一个二次恒等式完整分为恒等、椭圆、抛物及双曲四类，且椭圆 投影周期精确为 $2\pi/\sqrt{\omega^2-|H|^2}$。有限精确证据仅用于核验约定，不替代 全参数证明；共振不动集是连续族，系统也没有内生算术来源。

关键词：相同相位振子；交比；碰撞分层；群作用；周期连续族。

# Frozen common-forcing system

Let $I$ be an interval, let $f:I\to\mathbb R$ and $H:I\to\mathbb C$ be continuous, and set $z_j=e^{i\theta_j}$. The frozen equations are $$\dot\theta_j=f(t)+\operatorname{Im}\!\left(H(t)e^{-i\theta_j}\right),\qquad
 \dot z_j=ifz_j+\frac12\left(H-\overline H z_j^2\right).       \tag{1}$$ This is the classical Watanabe--Strogatz family [@WS1994]. The disk automorphism formulation was made explicit by Marvel, Mirollo, and Strogatz [@MMS2009]; partial integrability for oscillator populations is also developed in [@PR2008]. We claim no priority for that reduction. The contribution here is a convention-locked all-forcing synthesis, collision-stratum closure, constant-generator atlas, executable audit, and strict Route-A boundary.

# One projective group flow

Put $J=\operatorname{diag}(1,-1)$ and $$A(t)=\frac12\begin{pmatrix}if(t)&H(t)\\
                    \overline{H(t)}&-if(t)\end{pmatrix}.       \tag{2}$$ Then $\operatorname{tr}A=0$ and $A^*J+JA=0$. If $G'=AG$ and $G(t_0)=I$, differentiation of $G^*JG$ and $\det G$ gives $$G(t)=\begin{pmatrix}a&b\\\overline b&\overline a\end{pmatrix}
 \in\operatorname{SU}(1,1),\qquad |a|^2-|b|^2=1.                           \tag{3}$$ Projectivizing the same linear equation yields, simultaneously for every label, $$z_j(t)=M_{t,t_0}(z_j(t_0)),\qquad
 M(z)=\frac{az+b}{\overline b z+\overline a}
 =e^{i\psi}\frac{z+\alpha}{1+\overline\alpha z},             \tag{4}$$ where $\alpha=b/a$, $|\alpha|<1$, and $e^{i\psi}=a/\overline a$. Indeed, for a projective coordinate $z$, (2) gives $\dot z=A_{11}z+A_{12}-z(A_{21}z+A_{22})$, exactly (1). This proves the group representation for arbitrary common time dependence, without an autonomy or small-coupling assumption.

\>0

# Cross-ratio leaves and every collision stratum

Use $$[x_1,x_2;x_3,x_4]
 =\frac{(x_1-x_3)(x_2-x_4)}{(x_1-x_4)(x_2-x_3)}.$$ For a distinct labelled configuration, the $N-3$ quantities $$\chi_j=[z_j,z_1;z_2,z_3],\qquad j=4,\ldots,N,                \tag{5}$$ are real and constant. They are independent and separate diagonal group orbits on each fixed circular-order component: a boundary Möbius map is fixed by three distinct landmark images, and the remaining normalized images are precisely (5). Thus a generic orbit has dimension three and its quotient has dimension $N-3$.

Equation (4) is injective, so $z_j(t)=z_k(t)$ exactly when the equality held initially. Every labelled collision partition is therefore invariant. If $m$ distinct clusters remain, stabilizers give

   distinct clusters $m$   stabilizer dimension   orbit dimension   quotient coordinates
  ----------------------- ---------------------- ----------------- ----------------------
            $1$                    $2$                  $1$                 $0$
            $2$                    $1$                  $2$                 $0$
          $m\ge3$                  $0$                  $3$                $m-3$

This treats synchronization and repeated phases intrinsically; no singular choice of WS gauge is used at a collision boundary.

# The constant-generator atlas

For $f=\omega\in\mathbb R$ and constant $H\in\mathbb C$, define $\Delta=\omega^2-|H|^2$. Direct multiplication gives $$A^2=-\frac{\Delta}{4}I.                                  \tag{6}$$ If $(\omega,H)=(0,0)$, the flow is the identity. If $\Delta>0$, put $\nu=\sqrt\Delta$; then $$e^{tA}=\cos(\nu t/2)I+\frac{2}{\nu}\sin(\nu t/2)A,
 \qquad T_{\rm ell}=\frac{2\pi}{\nu}.                     \tag{7}$$ At $T_{\rm ell}$ the matrix is $-I$, already the identity in the projective group. No smaller positive projective time is the identity, and there is no boundary equilibrium. If $\Delta=0$ but $A\ne0$, then $e^{tA}=I+tA$ is parabolic with one boundary equilibrium. If $\Delta<0$, the hyperbolic formula has two boundary equilibria and every other boundary orbit joins the repeller to the attractor. In both nonidentity cases the equilibria are the unit-modulus roots of $$\overline H z^2-2i\omega z-H=0.                            \tag{8}$$ Equations (6)--(8) also prevent two common convention errors: calling the zero generator parabolic and doubling the projected elliptic period to the full matrix period.

# Proof closure and the Route-A stop

Fractional-linear maps preserve cross ratios, and four concyclic points have real cross ratio. A projective map fixing three distinct boundary points is the identity, proving the independence claim in (5). The stabilizer of one boundary point has dimension two, that of two distinct labelled points has dimension one, and that of three is trivial; this proves the stratum table. The fixed-root discriminant of (8) is $4(|H|^2-\omega^2)$, so its unit-circle root count gives the constant trichotomy.

In an elliptic constant system, a rational sampled-time ratio $\tau/T_{\rm ell}$ makes some iterate the identity on every configuration stratum. The fixed set is a continuum, not a finite isolated primitive-orbit ledger. Parabolic and hyperbolic flows have fixed clusters but no nonfixed periodic boundary orbit; arbitrary time-dependent forcing has no intrinsic autonomous period census. Moreover $(f,H,N)$ have no rational-prime origin or logarithmic prime clock. Therefore $$(A0,A1,A2,A3,A4)=(\mathrm{FAIL},\mathrm{WEAK},\mathrm{FAIL},
 \mathrm{FAIL},\mathrm{FORMAL\ HINT}),                      \tag{9}$$ overall `ROUTE_A_REJECTED`, with Route B false under `NO_BAD_EULER_OR_ROOT_NUMBER`. The $2\times2$ lift is a formal linearization, not a target quantization.

\>1

#### Exact regression certificate.

The release records 96 rational Riccati jets, 48 exact Möbius-action rows, 128 cross-ratio cells, 40 independent three-landmark reconstructions, 712 circle residual cells, and eight constant generators. A producer-independent checker passes 2,646 assertions; a separate SymPy path proves 18 generic identities; replay is byte exact; 24 repaired-hash semantic corruptions and one stale-hash corruption are rejected. These finite rows audit formulas and do not establish the all-parameter theorem.

#### Hostile boundaries.

The common Riccati owner generally disappears under heterogeneous natural frequencies, oscillator-specific forcing, delay, or higher phase harmonics. Cross ratios are used only for four distinct arguments; collision strata use distinct cluster representatives. Central matrix signs are removed only after passing from $\operatorname{SU}(1,1)$ to $\operatorname{PSU}(1,1)$. None of these source parameters is re-labelled as a prime, prime power, zero, Euler factor, or root number.

#### Revision-round focus.

Round 0 establishes the common Riccati lift and the constant discriminant atlas. The invariant quotient and hostile boundary are not yet expanded.

#### Revision-round focus.

Round 1 adds the explicit $N-3$ invariant family, three-point rigidity, all collision strata, and the central-sign period correction.

#### Revision-round focus.

Round 2 closes the fixed-continuum obstruction, exact evidence ledger, forcing boundary, and strict arithmetic nonclaims.

#### Limitations.

The theorem does not cover heterogeneous or higher-harmonic phase equations. It does not assign arithmetic meaning to labels, forcing, discriminants, or periods; construct a dynamical Euler product; claim a target functional equation; or claim literature novelty or external review.

# Declarations {#declarations .unnumbered}

#### Data and code availability.

Exact evidence and deterministic code accompany this manuscript.

#### Ethics.

No human, animal, clinical, personal, or sensitive data are used; approval is not applicable.

#### Contributions.

This anonymous certificate records formal analysis, software, validation, drafting, and revision. AI systems are not authors.

#### Funding and conflicts.

No external funding is reported; no conflict is known.

#### AI-use disclosure.

An AI coding assistant supported drafting and exact-code development; it was not an external reviewer or independent error process.

3 S. Watanabe and S. H. Strogatz, "Constants of motion for superconducting Josephson arrays," *Physica D* 74 (1994), 197--253. DOI: 10.1016/0167-2789(94)90196-1. S. A. Marvel, R. E. Mirollo, and S. H. Strogatz, "Identical phase oscillators with global sinusoidal coupling evolve by Möbius group action," *Chaos* 19 (2009), 043104. DOI: 10.1063/1.3247089. A. Pikovsky and M. Rosenblum, "Partially integrable dynamics of hierarchical populations of coupled oscillators," *Physical Review Letters* 101 (2008), 264103. DOI: 10.1103/PhysRevLett.101.264103.
