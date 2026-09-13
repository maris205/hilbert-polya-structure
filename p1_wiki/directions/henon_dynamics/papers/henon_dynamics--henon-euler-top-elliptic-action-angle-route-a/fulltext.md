---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-euler-top-elliptic-action-angle-route-a"
canonical_tex: "henon_dynamics/henon_euler_top_elliptic_action_angle_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_euler_top_elliptic_action_angle_route_a/paper/main.pdf"
source_sha256: "2defae43f5a5818675ee3e4f51f2ea6b5d1a3db502ceb84c3ae968a6501c5fc2"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Complete Elliptic Atlas for the Triaxial Euler Top: Periods, KKS Actions, and Fixed-Circle Obstructions

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_euler_top_elliptic_action_angle_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_euler_top_elliptic_action_angle_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_euler_top_elliptic_action_angle_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_euler_top_elliptic_action_angle_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For every strictly triaxial free rigid body, every nonzero angular-momentum sphere, and every energy, we give two explicit Jacobi charts, exact minimal periods, all axial stability rates, the intermediate-axis heteroclinic network, and KKS action--angle coordinates. The same atlas classifies every fixed component of a sampled time map. Resonant components are whole circles, so sufficiently large iterates do not have finite isolated fixed-point counts. The Hamiltonian flow has a canonical unitary Koopman owner but no intrinsic arithmetic gate, target divisor, or Hilbert--Pólya interpretation.
author:
- 'Route-A structural certificate C186'
title: 'A Complete Elliptic Atlas for the Triaxial Euler Top: Periods, KKS Actions, and Fixed-Circle Obstructions'
```

## Markdown 正文

suppressoptionalinfo 611

**Keywords:** Euler top; Jacobi elliptic functions; action--angle variables; Koopman group; clean fixed sets.

chinese-simplified

中文摘要

本文对任意严格三轴自由刚体、任意非零角动量球面及全部能量层，统一给出两套 [Jacobi]{lang="en"} 椭圆图册、精确最小周期、六个主轴平衡点的稳定性、 中间轴异宿分离网以及 [KKS]{lang="en"} 作用量与角变量。固定时间映射 在共振能量上固定整条圆，因此足够高的迭代不具有有限的孤立不动点计数。该系统虽有 典范幺正 [Koopman]{lang="en"} 动力学，但没有内生素数时钟或目标除子。

关键词：欧拉陀螺；椭圆函数；作用量与角变量；固定圆；谱障碍。

# Frozen reduced system

Let $0<I_1<I_2<I_3$, set $a=I_1^{-1}>b=I_2^{-1}>c=I_3^{-1}$, and fix $|M|=G>0$. For $m=M/G$ the Euler equation and normalized energy are $$\dot m=Gm\times\operatorname{diag}(a,b,c)m,
 \qquad e=\frac{2E}{G^2}=am_1^2+bm_2^2+cm_3^2.       \tag{1}$$ Hence $c\le e\le a$. Exact Jacobi representations are classical; we use the modern computational account in [@Celledoni2008] and the explicit $4K$ convention in [@Pina2015]. Our contribution is the all-energy theorem, consequence ledger, executable convention audit, and strict owner boundary, not priority for the classical solution.

# All-energy theorem

#### Topology and axial modes.

The endpoint levels $e=c,a$ consist respectively of $\pm e_3$ and $\pm e_1$. Every regular level on either side of $b$ is two circles: $\operatorname{sgn}m_3$ distinguishes $c<e<b$, while $\operatorname{sgn}m_1$ distinguishes $b<e<a$. At $e=b$, the points $\pm e_2$ are joined by four heteroclinic branches. The squared nonzero tangent rates at axes $1,2,3$ are $$-G^2(a-b)(a-c),\quad G^2(a-b)(b-c),\quad
 -G^2(a-c)(b-c),                                      \tag{2}$$ so the outer axes are elliptic and the intermediate axis is hyperbolic.

#### Low-energy chart.

For $c<e<b$, put $$\begin{gathered}
 A^2=\frac{e-c}{a-c},\quad B^2=\frac{e-c}{b-c},\quad
 C^2=\frac{a-e}{a-c},\\
 k^2=\frac{(a-b)(e-c)}{(b-c)(a-e)},\qquad
\Omega^2=G^2(b-c)(a-e).
\end{gathered}$$ For $\sigma=\pm1$ and $u=\sigma\Omega(t-t_0)$, every orbit is $$(m_1,m_2,m_3)=(A\operatorname{cn}u,\ B\operatorname{sn}u,\ \sigma C\operatorname{dn}u),
 \qquad T_3(e)=\frac{4K(k)}{G\sqrt{(b-c)(a-e)}}.       \tag{3}$$

#### High-energy chart.

For $b<e<a$, put $$\begin{gathered}
 A^2=\frac{e-c}{a-c},\quad B^2=\frac{a-e}{a-b},\quad
 C^2=\frac{a-e}{a-c},\\
 k^2=\frac{(b-c)(a-e)}{(a-b)(e-c)},\qquad
\Omega^2=G^2(a-b)(e-c).
\end{gathered}$$ Then every orbit is $$(m_1,m_2,m_3)=(\sigma A\operatorname{dn}u,\ B\operatorname{sn}u,\ C\operatorname{cn}u),
 \quad u=\sigma\Omega(t-t_0),\quad
 T_1(e)=\frac{4K(k)}{G\sqrt{(a-b)(e-c)}}.             \tag{4}$$ In both charts $0<k<1$. Although $\operatorname{dn}$ has real period $2K$, the vector contains $\operatorname{sn}$ and $\operatorname{cn}$ and has minimal period $4K$.

#### Separatrix and endpoint periods.

At $e=b$, define $$A_s^2=\frac{b-c}{a-c},\quad C_s^2=\frac{a-b}{a-c},
 \qquad \rho=G\sqrt{(a-b)(b-c)}.$$ For $\varepsilon,\sigma=\pm1$ the four branches are $$m_1=\varepsilon A_s\operatorname{sech}u,\quad m_2=\tanh u,\quad
 m_3=\varepsilon\sigma C_s\operatorname{sech}u,\quad
 u=\sigma\rho(t-t_0).                                \tag{5}$$ Thus they are heteroclinic from one intermediate-axis rotation to the other, not periodic orbits. Since $K(k)\to\infty$ as $k\to1$, both regular periods diverge at $e=b$. At the stable endpoints, $$T_3(c)=\frac{2\pi}{G\sqrt{(b-c)(a-c)}},\qquad
 T_1(a)=\frac{2\pi}{G\sqrt{(a-b)(a-c)}}.              \tag{6}$$

# Proof and action--angle atlas

Taking scalar products of $M\times I^{-1}M$ with $M$ and $I^{-1}M$ proves both quadratic integrals. Lagrange multipliers on the sphere give the six critical points and the stated level topology; tangent linearization gives (2).

For (3), substitute $\operatorname{cn}^2=1-\operatorname{sn}^2$ and $\operatorname{dn}^2=1-k^2\operatorname{sn}^2$. The constant and $\operatorname{sn}^2$ coefficients in both quadratic integrals vanish. The rules $$\operatorname{sn}'=\operatorname{cn}\operatorname{dn},\qquad \operatorname{cn}'=-\operatorname{sn}\operatorname{dn},\qquad
 \operatorname{dn}'=-k^2\operatorname{sn}\operatorname{cn}$$ reduce the three equations (1) to the displayed $\Omega^2$; the proof of (4) is the same coefficient calculation with the $\operatorname{dn}$ component permuted. Taking $k\to1$ and using $\operatorname{sn}(u,1)=\tanh u$ and $\operatorname{cn}(u,1)=\operatorname{dn}(u,1)=\operatorname{sech}u$ proves (5). Taking $k\to0$ proves (6).

Freeze $\{F,H\}=-M\cdot(\nabla F\times\nabla H)$ and $\dot F=\{F,H\}$, so (1) has $\dot M=M\times\nabla H$. On a positive low component take $q=\arg(M_1+iM_2)$ and $P_3=G-M_3$; since $G$ is a Casimir, $\{q,P_3\}=1$. With $A_q=a\cos^2q+b\sin^2q$, its unsigned cap action $J_3=(2\pi)^{-1}\oint P_3\,dq$ is $$J_3(e)=G\left[1-\frac1{2\pi}\int_0^{2\pi}
 \sqrt{\frac{A_q-e}{A_q-c}}\,dq\right].              \tag{7}$$ For a positive high component take $q=\arg(M_2+iM_3)$ and $P_1=G-M_1$, so $\{q,P_1\}=1$. With $B_q=b\cos^2q+c\sin^2q$, $J_1=(2\pi)^{-1}\oint P_1\,dq$ is $$J_1(e)=G\left[1-\frac1{2\pi}\int_0^{2\pi}
 \sqrt{\frac{e-B_q}{a-B_q}}\,dq\right].              \tag{8}$$ The negative components have the same unsigned action. Differentiating enclosed symplectic area gives the one-degree-of-freedom identity $|dJ/dE|=T/(2\pi)$. Finally $\theta=\pi u/(2K(k))\pmod{2\pi}$ satisfies $\dot\theta=\pm2\pi/T(e)$.

# Sampled time, Koopman owner, and Route-A stop

Let $\Phi_\tau$ be the time-$\tau$ map, $\tau>0$. Its $n$th iterate fixes all six equilibria. A regular energy component is fixed pointwise exactly when $$n\tau=qT(e)\qquad(q\in\mathbb Z_{\ge1}),             \tag{9}$$ and no interior separatrix point is fixed. The periods are continuous, finite at the stable endpoints, and divergent at $b$. Therefore for every $\tau>0$, all sufficiently large iterates have at least one fixed circle. The full-sphere isolated-cardinality Artin--Mazur coefficients are thus not finite; selecting one energy circle would change the frozen owner.

KKS area preservation makes $U_t f=f\circ\Phi_t$ a canonical unitary Koopman group. Off the measure-zero critical levels it is a direct integral over the two regimes and two components; circle Fourier mode $\ell$ carries the phase $\exp(2\pi i\ell t/T(e))$. This is a natural A4 coordinate. It does not supply rational primes, prime powers, a logarithmic clock, a target divisor, or a Hilbert--Pólya operator. Hence $$(A0,A1,A2,A3,A4)=(\mathrm{FAIL},\mathrm{WEAK},\mathrm{FAIL},
 \mathrm{FAIL},\mathrm{NATURAL\ QUANTIZATION}),$$ overall `ROUTE_A_REJECTED`, Route B false, under `NO_BAD_EULER_OR_ROOT_NUMBER`.

#### Exact certificate.

The package records 180 rational sentinels across both regimes and 1,260 zero coefficient residuals. A producer-independent checker passes 4,268 assertions; a separate SymPy path proves 25 generic identities; replay is byte exact; 20 repaired-hash semantic corruptions and one stale-hash corruption are rejected. These rows audit conventions and do not replace the all-parameter proof above.

#### Revision-round focus.

Round 0 freezes the two Jacobi regimes and their common $4K$ vector period. It does not yet use the full sampled-time owner boundary.

#### Revision-round focus.

Round 1 adds all axial tangent rates, the four explicit heteroclinic branches, and both KKS cap-action charts.

#### Revision-round focus.

Round 2 makes the fixed-set statement iterate-exact and closes the positive-dimensional zeta obstruction, degenerate boundaries, evidence audit, and strict Route-A verdict.

#### Limitations.

$G=0$ is the stationary origin. Spherical and symmetric tops violate the strict inertia gaps and have equilibrium manifolds requiring separate elementary formulas. We do not continue the regular formula through $k=1$, count a fixed circle as finitely many points, claim arithmetic semantics, or claim literature novelty or external review.

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

2 E. Celledoni, F. Fassò, N. Säfström, and A. Zanna, "The exact computation of the free rigid body motion and its use in splitting methods," *SIAM J. Sci. Comput.* 30 (2008), 2084--2112. DOI: 10.1137/070704393. E. G. Pina, "Drawing the free rigid body dynamics according to Jacobi," arXiv:1505.06186 (2015).
