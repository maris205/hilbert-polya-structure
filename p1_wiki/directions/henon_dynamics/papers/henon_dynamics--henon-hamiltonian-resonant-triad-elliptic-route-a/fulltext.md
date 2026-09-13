---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-hamiltonian-resonant-triad-elliptic-route-a"
canonical_tex: "henon_dynamics/henon_hamiltonian_resonant_triad_elliptic_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_hamiltonian_resonant_triad_elliptic_route_a/paper/main.pdf"
source_sha256: "db43f7ca9eeec047be00cbec18a5b8fd23fe209ecf2bdb972dc6779c1e69356b"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Complete Elliptic Reduction and Two-Phase Return for a Hamiltonian Resonant Triad

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_hamiltonian_resonant_triad_elliptic_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_hamiltonian_resonant_triad_elliptic_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_hamiltonian_resonant_triad_elliptic_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_hamiltonian_resonant_triad_elliptic_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For the canonical complex resonant triad we prove global Liouville integrability and reduce every intensity orbit to a real cubic. Every regular orbit is written in Jacobi form with its exact intensity period. \>0 Two complete elliptic integrals of the third kind reconstruct the surviving torus phases and give the necessary and sufficient full-state return test. The zero-Hamiltonian transfer, its factor-two period, the equal-action separatrix, and maximal-Hamiltonian relative equilibria are closed separately. \>1 Finite exact receipts are separated from the continuum proof, and source, collision, and Route-A boundaries are recorded explicitly.
author:
- 'Route-A source-local certificate HCS-C344'
date: 3 September 2026
title: |
  Complete Elliptic Reduction and Two-Phase Return\
  for a Hamiltonian Resonant Triad
```

## Markdown 正文

trailerid \[\<C3442026090300000000000000000000\>\<C3442026090300000000000000000000\>\]

# Canonical convention and first integrals

On $\mathbb C^3$ use $$\{f,g\}=-i\sum_{j=1}^3
 \left(f_{z_j}g_{\bar z_j}-f_{\bar z_j}g_{z_j}\right)$$ and the real Hamiltonian $$\label{eq:H}
 H=z_1z_2\bar z_3+\bar z_1\bar z_2z_3.$$ Hamilton's equations are $$\label{eq:triad}
 i\dot z_1=\bar z_2z_3,\qquad
 i\dot z_2=\bar z_1z_3,\qquad
 i\dot z_3=z_1z_2.$$ Writing $I_j=|z_j|^2$ and $w=z_1z_2\bar z_3$ gives $$\dot I_1=\dot I_2=-2\operatorname{Im}w,\qquad
 \dot I_3=2\operatorname{Im}w.$$ Consequently $$\label{eq:MR}
 N_1=I_1+I_3,\qquad N_2=I_2+I_3,\qquad H$$ are conserved. Direct evaluation of the displayed bracket gives pairwise involution. On the open set $I_1I_2I_3\sin\Psi\ne0$, where $\Psi=\arg z_1+\arg z_2-\arg z_3$, the first two differentials are independent action differentials and $$\partial_\Psi H=-2\sqrt{I_1I_2I_3}\sin\Psi\ne0.$$ Thus the three integrals are generically independent. Their common levels are bounded because $0\le I_3\le\min(N_1,N_2)$ and $I_j=N_j-I_3$ for $j=1,2$. Polynomial local existence and boundedness give a global flow on all of $\mathbb R$.

# The real cubic and every regular intensity

Put $x=I_3$. Since $\dot x=2\operatorname{Im}w$ and $|w|^2=x(N_1-x)(N_2-x)$, $$\label{eq:cubic}
 \dot x^2=4x(N_1-x)(N_2-x)-H^2=:P(x).$$ Let $N_-:=\min(N_1,N_2)$ and $N_+:=\max(N_1,N_2)$. The function $f(x)=x(N_1-x)(N_2-x)$ has one maximum on $[0,N_-]$, at $$\label{eq:xstar}
 x_*=\frac{N_1+N_2-\sqrt{N_1^2-N_1N_2+N_2^2}}{3},\qquad
 H_{\max}=2\sqrt{f(x_*)}.$$ For $0<|H|<H_{\max}$, signs at $0$, the maximum, $N_-$, $N_+$, and infinity prove that $P$ has exactly three roots $$\label{eq:rootorder}
 0<r_1<r_2<N_-\le N_+<r_3.$$ They obey $$\label{eq:vieta}
 \sum r_j=N_1+N_2,\quad
 \sum_{j<k}r_jr_k=N_1N_2,\quad
 r_1r_2r_3=\frac{H^2}{4}.$$

[\[thm:regular\]]{#thm:regular label="thm:regular"} Let $0<|H|<H_{\max}$ and define $$m=\frac{r_2-r_1}{r_3-r_1},\qquad
 u=\sqrt{r_3-r_1}(t-t_0).$$ Every intensity orbit on this level is $$\label{eq:snsolution}
 x(t)=r_1+(r_2-r_1)\operatorname{sn}^2(u\mid m),
 \qquad T_x=\frac{2K(m)}{\sqrt{r_3-r_1}}.$$

On $[r_1,r_2]$ the cubic is $4(x-r_1)(r_2-x)(r_3-x)$. Substitute [\[eq:snsolution\]](#eq:snsolution){reference-type="eqref" reference="eq:snsolution"} and use $(\operatorname{sn}')^2=(1-\operatorname{sn}^2)(1-m\operatorname{sn}^2)$. The resulting identity is exact. Time translation selects either initial sign of $\dot x$, and $\operatorname{sn}^2$ has least real period $2K(m)$.

The analytic root argument and substitution are the *cubic elliptic owner* of revision round zero.

\>0

# Two phases, not one, control full return

When $H\ne0$, no $I_j$ can vanish. Writing $z_j=\sqrt{I_j}e^{i\phi_j}$, division of [\[eq:triad\]](#eq:triad){reference-type="eqref" reference="eq:triad"} by $z_j$ gives $$\label{eq:phasedot}
 \dot\phi_1=-\frac{H}{2(N_1-x)},\qquad
 \dot\phi_2=-\frac{H}{2(N_2-x)},\qquad
 \dot\phi_3=-\frac{H}{2x}.$$ With $\Pi(n\mid m)$ denoting the complete third-kind integral, integration over one intensity period yields $$\label{eq:deltas}
 \Delta_j=-\frac{H}{\sqrt{r_3-r_1}(N_j-r_1)}
 \Pi\left(\frac{r_2-r_1}{N_j-r_1}\mathrel|m\right),
 \qquad j=1,2.$$ Indeed, the integral over $0\le u\le2K$ is twice its complete-quarter integral. After $T_x$, both $x$ and $\dot x$ return; together with $H$ they determine $e^{i\Psi}$. Hence $\Delta_3=\Delta_1+\Delta_2$ modulo $2\pi$.

Because a return of the nonconstant full state must occur at an integer multiple of its least intensity period, the full complex orbit is periodic if and only if $$\label{eq:closure}
 \frac{\Delta_1}{2\pi}\in\mathbb Q,\qquad
 \frac{\Delta_2}{2\pi}\in\mathbb Q.$$ One scalar period therefore does not settle full-state recurrence.

# Zero Hamiltonian and double-root boundaries

Suppose first that $0<N_1<N_2$. With $A=\sqrt{N_1}$, $B=\sqrt{N_2}$, $m=A^2/B^2$, and $u=B(t-t_0)$, every non-equilibrium orbit, up to the two phase symmetries, is $$\label{eq:Hzero}
 \begin{aligned}
 z_1&=A\operatorname{cn}(u\mid m)e^{i\alpha},&
 z_2&=B\operatorname{dn}(u\mid m)e^{i\beta},\\
 z_3&=-iA\operatorname{sn}(u\mid m)e^{i(\alpha+\beta)}.
 \end{aligned}$$ The other ordering exchanges modes $1$ and $2$. The Jacobi derivative identities verify [\[eq:triad\]](#eq:triad){reference-type="eqref" reference="eq:triad"} directly, including both amplitude-zero crossings. Intensities have period $2K(m)/B$. Translation by $2K$ changes the signs of $\operatorname{cn}$ and $\operatorname{sn}$ but not $\operatorname{dn}$, so the full state has least period $4K(m)/B$.

At $N_1=N_2=N>0$, the limit $m=1$ gives $$\label{eq:separatrix}
 \sqrt N\left(\operatorname{sech}u\,e^{i\alpha},
 \operatorname{sech}u\,e^{i\beta},
 -i\tanh u\,e^{i(\alpha+\beta)}\right),\qquad
 u=\sqrt N(t-t_0).$$ It is heteroclinic between opposite points on the $z_3$-axis and has infinite period.

At $|H|=H_{\max}$, the two accessible roots coalesce at $x_*$. The intensities are constant and the phases have frequencies $$\label{eq:omegas}
 \omega_1=-\frac{H}{2(N_1-x_*)},\quad
 \omega_2=-\frac{H}{2(N_2-x_*)},\quad
 \omega_3=-\frac{H}{2x_*}=\omega_1+\omega_2.$$ The final equality is equivalent to $f'(x_*)=0$. This relative equilibrium is periodic exactly when $\omega_1/\omega_2$ is rational. The symmetric face is always periodic; the asymmetric example $(N_1,N_2)=(5,8)$ has $x_*=2$, $H_{\max}=12$, and absolute frequencies $(2,1,3)$.

The origin and each complex coordinate axis are equilibrium families. Introducing a real coupling $g$ multiplies the vector field by $g$: the $g=0$ face is the identity flow, and $g\ne0$ is the present theorem after $\tau=gt$. Complex conjugation paired with time reversal leaves all intensities unchanged. These clauses form the *two-phase return owner* added in revision round one.

\>1

# Executable receipts, collisions, and Route A

The evidence ledger contains $72$ regular signed-Hamiltonian rows, $12$ zero-Hamiltonian rows, and $24$ relative-equilibrium rows. Every regular root has an exact rational sign bracket. A producer-independent checker recomputes the roots, $K$, both complete third-kind integrals, the factor-two boundary period, and every relative frequency. A separate symbolic lane checks the Poisson signs, involution, cubic, Jacobi substitution, and explicit zero-Hamiltonian solution. Sampling proves none of the continuum claims; the preceding arguments do.

The nearest workspace systems are different. C211 treats a Hamiltonian Lotka--Volterra period annulus, C230 an open Toda lattice, C235 cyclic population dynamics, and C256 a KdV traveling-wave profile. None owns a complex resonant triad with two surviving phase returns.

The conservative Route-A tuple is $$(\mathrm{A0\_FAIL},\mathrm{A1\_WEAK},\mathrm{A2\_FAIL},
  \mathrm{A3\_FAIL},\mathrm{A4\_FORMAL\_HINT}).$$ Elliptic source dynamics gives only A1 weakly. A formal three-boson cubic analogy does not supply a self-adjoint domain theorem or a complete quantum spectrum. There is no rational-prime carrier, prime-power clock, arithmetic orbit dictionary, target Euler product, root number, automorphy, target divisor or functional equation, target-zero match, or Hilbert--Polya operator. Route B is false. This is the *finite evidence and route firewall* of the final revision.

# Source boundary {#source-boundary .unnumbered}

This paper is a source-local reconstruction, not a priority claim. Manley and Rowe own their energy relations; Armstrong et al. own the coupled optical amplitude setting and explicit three-wave solutions; Kaup, Reiman, and Bers give an authoritative primary treatment of broader resonant three-wave dynamics. The exact software receipts are local implementation checks and are not attributed to those sources.

9 J. M. Manley and H. E. Rowe, "Some General Properties of Nonlinear Elements---Part I. General Energy Relations," *Proceedings of the IRE* 44 (1956), 904--913, DOI [10.1109/JRPROC.1956.275145](https://doi.org/10.1109/JRPROC.1956.275145). J. A. Armstrong, N. Bloembergen, J. Ducuing, and P. S. Pershan, "Interactions between Light Waves in a Nonlinear Dielectric," *Physical Review* 127 (1962), 1918--1939, DOI [10.1103/PhysRev.127.1918](https://doi.org/10.1103/PhysRev.127.1918). D. J. Kaup, A. Reiman, and A. Bers, "Space-time evolution of nonlinear three-wave interactions. I. Interaction in a homogeneous medium," *Reviews of Modern Physics* 51 (1979), 275--309, DOI [10.1103/RevModPhys.51.275](https://doi.org/10.1103/RevModPhys.51.275).
