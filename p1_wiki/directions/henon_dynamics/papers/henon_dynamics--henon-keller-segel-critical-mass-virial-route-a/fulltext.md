---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-keller-segel-critical-mass-virial-route-a"
canonical_tex: "henon_dynamics/henon_keller_segel_critical_mass_virial_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_keller_segel_critical_mass_virial_route_a/paper/main.pdf"
source_sha256: "19b5b457cac66b6b96d8e57bb936b107457a9038ef43f4991051e18613c25a5a"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Why Eight Pi Is Critical: Energy, Virial, and Stationary Profiles in Planar Keller--Segel Flow

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_keller_segel_critical_mass_virial_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_keller_segel_critical_mass_virial_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_keller_segel_critical_mass_virial_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_keller_segel_critical_mass_virial_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For the parabolic--elliptic Keller--Segel equation on the plane, we derive the critical mass $8\pi$ from two independent exact mechanisms. A mass-preserving dilation changes free energy by $2M(1-M/(8\pi))\log\lambda$, while Newtonian-kernel symmetrization gives the finite-moment virial law $I'=4M(1-M/(8\pi))$. The latter forces every supercritical classical finite-moment solution to leave that regime no later than an explicit time. At critical mass we verify the full translated and dilated stationary family, then compute its logarithmically infinite second moment; this hypothesis check removes an apparent conflict with the zero virial slope. We also derive the radial cumulative-mass equation and its critical equilibrium. Exact symbolic, rational, replay, and hostile receipts audit coefficients but do not replace the PDE proof. No literature-priority, weak-continuation, or arithmetic-target claim is made.
author:
- 'HCS-C363 source-local reconstruction'
date: 4 September 2026
title: |
  Why Eight Pi Is Critical:\
  Energy, Virial, and Stationary Profiles in Planar Keller--Segel Flow
```

## Markdown 正文

**Revision certificate.** =0 Round zero energy scaling and critical mass closure. =1 Round one virial bound and stationary profile closure. Round two radial dynamics, evidence, and Route A closure.

# Equation, hypotheses, and main result

We use the Newtonian convention $$\rho_t=\Delta\rho-\nabla\!\cdot(\rho\nabla c),\quad
 -\Delta c=\rho,\quad
 c(x)=-\frac1{2\pi}\int_{\mathbb R^2}\rho(y)\log|x-y|\,dy. \label{eq:pde}$$ Every assertion is made on an open interval where $\rho$ is nonnegative, $C^1$ in time and $C^2$ in space, has finite mass, the logarithmic convolution defining $c$ exists, and all displayed fluxes, derivatives, and cutoff limits are integrable. Barycenter conservation requires a finite first moment; the virial law requires a finite second moment. The free-energy identity further requires finite entropy and interaction energy, strict positivity when $M>0$, and finite dissipation. The zero solution is treated separately without invoking $\log\rho$. These assertion-specific hypotheses are part of the theorem.

[\[thm:atlas\]]{#thm:atlas label="thm:atlas"} Let $M=\int\rho$ and, when finite, $B=\int x\rho$ and $I=\int |x|^2\rho$. Along [\[eq:pde\]](#eq:pde){reference-type="eqref" reference="eq:pde"}, $$\begin{aligned}
 M'&=0,\quad B'=0,                                   \label{eq:conserve}\\
 \frac{d}{dt}\mathcal F[\rho]
 &=-\int\rho\left|\nabla(\log\rho-c)\right|^2,\quad
 \mathcal F[\rho]=\int\rho\log\rho-\frac12\int\rho c,        \label{eq:diss}\\
 I'&=4M\left(1-\frac{M}{8\pi}\right).                \label{eq:virial}\end{aligned}$$ For $\rho_\lambda(x)=\lambda^2\rho(\lambda x)$, $$\mathcal F[\rho_\lambda]-\mathcal F[\rho]
 =2M\left(1-\frac{M}{8\pi}\right)\log\lambda.        \label{eq:scale}$$ If $M>8\pi$, a classical finite-second-moment solution cannot persist beyond $$T_*=\frac{2\pi I(0)}{M(M-8\pi)}.                    \label{eq:bound}$$ At $M=8\pi$, every $\lambda>0$ and $a\in\mathbb R^2$ give a stationary pair $$\rho_{\lambda,a}(x)=
 \frac{8\lambda^2}{(\lambda^2+|x-a|^2)^2},\quad
 c_{\lambda,a}(x)=-2\log(\lambda^2+|x-a|^2)+C.       \label{eq:profile}$$ It has mass $8\pi$ and infinite second moment.

# Conservation, energy, and scaling

Integrating [\[eq:pde\]](#eq:pde){reference-type="eqref" reference="eq:pde"} proves mass conservation. For the barycenter, diffusion integrates to zero and $$\int\rho(x)\nabla c(x)\,dx
 =-\frac1{2\pi}\iint \rho(x)\rho(y)
       \frac{x-y}{|x-y|^2}\,dx\,dy=0,$$ because exchanging $x,y$ negates the integrand. This proves [\[eq:conserve\]](#eq:conserve){reference-type="eqref" reference="eq:conserve"}.

The first equation in [\[eq:pde\]](#eq:pde){reference-type="eqref" reference="eq:pde"} is $$\rho_t=\nabla\!\cdot\{\rho\nabla(\log\rho-c)\}.      \label{eq:gradient}$$ The first variation of $\mathcal F$ is $\log\rho+1-c$; the constant contributes nothing because mass is conserved. Integration by parts gives [\[eq:diss\]](#eq:diss){reference-type="eqref" reference="eq:diss"}.

Dilation contributes $2M\log\lambda$ to $\int\rho\log\rho$. Since $$-\frac12\int\rho c
 =\frac1{4\pi}\iint\rho(x)\rho(y)\log|x-y|\,dx\,dy,$$ changing variables in the double integral contributes $-M^2\log\lambda/(4\pi)$. Their sum is [\[eq:scale\]](#eq:scale){reference-type="eqref" reference="eq:scale"}. Hence free energy increases along concentration dilations below $8\pi$, is scale invariant at $8\pi$, and decreases along concentration dilations above $8\pi$. This scaling statement alone is not an existence or blow-up theorem.

\>0

# Virial obstruction and critical equilibria

Diffusion contributes $4M$ to $I'$. Put $J=\int x\cdot\rho(x)\nabla c(x)\,dx$. Kernel substitution and exchange of the variables give the following identity. To justify the exchange, first exclude $|x-y|\le\varepsilon$; local integrability of the Newtonian gradient and the stated decay and moment assumptions permit the cutoff limit: $$\begin{aligned}
 2J&=-\frac1{2\pi}\iint\rho(x)\rho(y)
 \frac{x\cdot(x-y)+y\cdot(y-x)}{|x-y|^2}\,dx\,dy\\
 &=-\frac{M^2}{2\pi}.\end{aligned}$$ The drift contribution is $2J$, proving [\[eq:virial\]](#eq:virial){reference-type="eqref" reference="eq:virial"}. For $M>8\pi$, $$I(t)=I(0)-\frac{M(M-8\pi)}{2\pi}t.$$ A nonnegative density cannot have negative second moment. Thus the stated classical finite-moment regime fails by [\[eq:bound\]](#eq:bound){reference-type="eqref" reference="eq:bound"}, possibly earlier; the argument does not select a weak continuation.

We verify [\[eq:profile\]](#eq:profile){reference-type="eqref" reference="eq:profile"} directly. By translation take $a=0$ and write $r=|x|$. Radial differentiation gives $$-\left(c_{rr}+\frac1r c_r\right)
 =\frac{8\lambda^2}{(\lambda^2+r^2)^2}=\rho_{\lambda,0},
 \quad \partial_r\log\rho_{\lambda,0}=\partial_r c_{\lambda,0}. \label{eq:stationary}$$ The flux in [\[eq:gradient\]](#eq:gradient){reference-type="eqref" reference="eq:gradient"} vanishes. Polar integration yields $$2\pi\int_0^R r\rho_{\lambda,0}(r)\,dr
 =\frac{8\pi R^2}{\lambda^2+R^2}\longrightarrow8\pi. \label{eq:mass}$$ The truncated second moment is $$8\pi\lambda^2\left(
 \log\frac{\lambda^2+R^2}{\lambda^2}
 +\frac{\lambda^2}{\lambda^2+R^2}-1\right),          \label{eq:moment}$$ and diverges as $R\to\infty$. Therefore [\[eq:virial\]](#eq:virial){reference-type="eqref" reference="eq:virial"}, whose proof requires finite $I$, cannot be applied to this stationary family. The endpoint is consistent.

\>1

# Radial cumulative equation and boundaries

For a radial solution regular at the origin define $$m(r,t)=2\pi\int_0^r s\rho(s,t)\,ds,\quad n=m/(2\pi).$$ Then $m(0,t)=m_r(0,t)=0$. For $r>0$, the elliptic equation gives $c_r=-m/(2\pi r)$. Integrating the parabolic equation over a disc and using $\rho=m_r/(2\pi r)$ yields $$m_t=m_{rr}-\frac1r m_r+\frac{m\,m_r}{2\pi r},
 \quad n_t=n_{rr}-\frac1r n_r+\frac{n\,n_r}{r}.      \label{eq:radial}$$ For [\[eq:profile\]](#eq:profile){reference-type="eqref" reference="eq:profile"}, $n=4r^2/(\lambda^2+r^2)$, and substitution makes the right-hand side of [\[eq:radial\]](#eq:radial){reference-type="eqref" reference="eq:radial"} zero. At $r=0$, [\[eq:radial\]](#eq:radial){reference-type="eqref" reference="eq:radial"} is understood through the regular radial limit.

Zero density is stationary, but its logarithmic dissipation formula is not invoked. Below $8\pi$, [\[eq:virial\]](#eq:virial){reference-type="eqref" reference="eq:virial"} has positive slope only while the classical finite-moment solution exists; no convergence claim follows. At $8\pi$, the profiles [\[eq:profile\]](#eq:profile){reference-type="eqref" reference="eq:profile"} lie outside that moment class. As $\lambda\downarrow0$ they converge weakly to $8\pi\delta_a$, outside the smooth phase space. As $\lambda\to\infty$ they tend pointwise to zero while mass spreads to infinity. Above $8\pi$, [\[eq:bound\]](#eq:bound){reference-type="eqref" reference="eq:bound"} is a classical-persistence obstruction, not a complete measure-solution theory.

# Evidence, sources, and Route-A boundary

The certificate contains 21 virial rows, 21 scaling rows, nine profile rows, nine radial rows, and seven boundary rows. An independent implementation reconstructs every entry; SymPy checks 17 identities; two isolated replays agree byte for byte; and 61 repaired-hash or parser attacks are rejected. These receipts test signs and normalizations. They do not prove regularity or persistence; the analytic argument and its hypotheses do.

Keller and Segel provide the model lineage [@kellersegel]; Blanchet, Dolbeault, and Perthame provide critical-mass context [@blanchet]. Every coefficient used above is rederived, and no priority claim is made.

The strict Route-A tuple is $$(\mathrm{A0\_FAIL},\mathrm{A1\_FAIL},\mathrm{A2\_FAIL},
  \mathrm{A3\_FAIL},\mathrm{A4\_FAIL}).$$ The continuum mass and dissipative clock furnish no intrinsic rational-prime objects, prime-power repetitions, or logarithmic-prime clock. No target determinant, analytic bridge, or natural target-zero quantization is constructed. Route A is rejected and Route B is locked. No target arithmetic local data, Euler factors, bad-prime data, root number, automorphy, target divisor or counting law, target functional equation, target-zero match, or Hilbert--Pólya operator is claimed.

The package does not construct post-concentration weak solutions, prove general subcritical convergence, or classify nonradial critical dynamics.

9 E. F. Keller and L. A. Segel, *Initiation of slime mold aggregation viewed as an instability*, J. Theoret. Biol. 26 (1970), 399--415. [doi:10.1016/0022-5193(70)90092-5](https://doi.org/10.1016/0022-5193(70)90092-5).

A. Blanchet, J. Dolbeault, and B. Perthame, *Two-dimensional Keller--Segel model: optimal critical mass and qualitative properties of the solutions*, Electron. J. Differential Equations 2006 (2006), no. 44, 1--33. [official journal PDF](https://ejde.math.txstate.edu/Volumes/2006/44/blanchet.pdf).
