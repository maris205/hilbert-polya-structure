---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-isothermal-euler-riemann-solver-route-a"
canonical_tex: "henon_dynamics/henon_isothermal_euler_riemann_solver_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_isothermal_euler_riemann_solver_route_a/paper/main.pdf"
source_sha256: "3d96cb741470acf15fc2b824e490443b3ce4e0fdc602f87af804ef9ed90e3361"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The Complete Positive-Density Riemann Atlas for One-Dimensional Isothermal Euler Flow

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_isothermal_euler_riemann_solver_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_isothermal_euler_riemann_solver_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_isothermal_euler_riemann_solver_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_isothermal_euler_riemann_solver_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For one-dimensional isothermal Euler flow at sound speed $a>0$, we reduce every positive-density Riemann problem to one strictly monotone scalar equation. Its unique root yields the intermediate density and all four shock/rarefaction patterns with exact fan profiles and Rankine--Hugoniot speeds. \>0 We prove the Lax inequalities, strict mechanical-entropy selection and the absence of vacuum for every finite velocity jump. \>1 Zero-strength waves, density scaling and the singular pressureless limit are closed separately, and an executable certificate checks every branch without turning source wave data into target arithmetic evidence.
author:
- 'Route-A source-local certificate HCS-C300'
date: 2 September 2026
title: |
  The Complete Positive-Density Riemann Atlas\
  for One-Dimensional Isothermal Euler Flow
```

## Markdown 正文

trailerid \[\<C3002026090200000000000000000000\>\<C3002026090200000000000000000000\>\]

# One scalar equation for the full solver

Let $U=(\rho,m)$, $m=\rho u$, and $$\label{eq:euler}
 U_t+F(U)_x=0,
 \qquad F(U)=\left(m,\frac{m^2}{\rho}+a^2\rho\right),
 \qquad a>0,\quad \rho>0.$$ The characteristic speeds are $\lambda_1=u-a$ and $\lambda_2=u+a$. For $r,r_0>0$ define the continuous $C^1$, strictly increasing function $$\label{eq:f}
 f(r;r_0)=
 \begin{cases}
 a\log(r/r_0),&0<r\le r_0,\\[2pt]
 a(r-r_0)/\sqrt{rr_0},&r\ge r_0.
 \end{cases}$$

[\[thm:main\]]{#thm:main label="thm:main"} For arbitrary left and right states $(\rho_L,u_L),(\rho_R,u_R)$ with positive density and finite velocity, there is a unique $\rho_*>0$ satisfying $$\label{eq:root}
 f(\rho_*;\rho_L)+f(\rho_*;\rho_R)+u_R-u_L=0.$$ The unique intermediate velocity is $$\label{eq:ustar}
 u_*=u_L-f(\rho_*;\rho_L)=u_R+f(\rho_*;\rho_R).$$ The 1-wave from $L$ to $*$ is a rarefaction, zero wave, or Lax shock as $\rho_*<\rho_L$, $=$, or $>$; the 2-wave from $*$ to $R$ has the analogous classification relative to $\rho_R$. These waves and the constant intermediate sector form the unique self-similar Lax entropy solution. In particular, no finite datum in this chamber produces vacuum.

For fixed $r_0$, the two derivatives of $f(\cdot;r_0)$ are $a/r$ and $a(r+r_0)/(2r\sqrt{rr_0})$, respectively. They are positive and meet at $a/r_0$; moreover $f$ ranges from $-\infty$ to $+\infty$. Hence the left side of [\[eq:root\]](#eq:root){reference-type="eqref" reference="eq:root"} has exactly one positive zero; [\[eq:ustar\]](#eq:ustar){reference-type="eqref" reference="eq:ustar"} is then forced. The logarithmic branch is obtained by integrating $\mathrm du=\mp a\,\mathrm d\rho/\rho$ on the two integral curves. Eliminating the shock speed from the Rankine--Hugoniot equations gives $$\label{eq:hugoniot}
 (u-u_0)^2=a^2\frac{(\rho-\rho_0)^2}{\rho\rho_0}.$$ The compressive sign in family 1 is negative and that in family 2 is positive, which gives the second branch of [\[eq:f\]](#eq:f){reference-type="eqref" reference="eq:f"}. The explicit formulas and entropy check below complete the construction. Positivity of the unique root proves the no-vacuum assertion.

# The four patterns in one table

The two comparisons with the unique root give the full atlas.

     comparison      family  wave
  ----------------- -------- -------------
   $\rho_*<\rho_L$     1     rarefaction
   $\rho_*>\rho_L$     1     shock
   $\rho_*<\rho_R$     2     rarefaction
   $\rho_*>\rho_R$     2     shock

Equality deletes the wave continuously. Thus the two independent signs produce rarefaction--rarefaction, rarefaction--shock, shock--rarefaction, and shock--shock solutions without separate existence arguments.

For a 1-rarefaction, on $u_L-a\le\xi\le u_*-a$, $$\label{eq:r1}
 u(\xi)=\xi+a,\qquad
 \rho(\xi)=\rho_L\exp\!\left(\frac{u_L-u(\xi)}a\right).$$ For a 2-rarefaction, on $u_*+a\le\xi\le u_R+a$, $$\label{eq:r2}
 u(\xi)=\xi-a,\qquad
 \rho(\xi)=\rho_R\exp\!\left(\frac{u(\xi)-u_R}a\right).$$ If $r_L=\rho_*/\rho_L>1$, the 1-shock speed is $$\label{eq:s1}
 s_1=u_L-a\sqrt{r_L}=u_*-\frac a{\sqrt{r_L}}.$$ If $r_R=\rho_*/\rho_R>1$, the 2-shock speed is $$\label{eq:s2}
 s_2=u_R+a\sqrt{r_R}=u_*+\frac a{\sqrt{r_R}}.$$

\>0

# Lax ordering and mechanical entropy

Equations [\[eq:s1\]](#eq:s1){reference-type="eqref" reference="eq:s1"}--[\[eq:s2\]](#eq:s2){reference-type="eqref" reference="eq:s2"} give, by direct subtraction, $$\label{eq:lax}
 u_*-a<s_1<u_L-a,\qquad
 u_R+a<s_2<u_*+a,$$ whenever the corresponding shock exists. The fan speeds in [\[eq:r1\]](#eq:r1){reference-type="eqref" reference="eq:r1"}--[\[eq:r2\]](#eq:r2){reference-type="eqref" reference="eq:r2"} increase from left to right. Every 1-wave lies below $u_*$ and every 2-wave lies above $u_*$, so their ordering is strict.

In conservative variables a strictly convex entropy pair is $$\label{eq:entropy}
 \eta(\rho,m)=\frac{m^2}{2\rho}+a^2\rho\log\rho,
 \qquad q(\rho,m)=u\bigl(\eta+a^2\rho\bigr).$$ Indeed, $\eta_{mm}=1/\rho>0$ and $\det D^2\eta=a^2/\rho^2>0$. Smooth fans satisfy equality in the entropy law. For either shock, let $r>1$ be the compressed-to-outer density ratio and let $\rho_0$ be that outer, lower density. Direct substitution gives $$\label{eq:entropyproduction}
 [q]-s[\eta]=a^3\rho_0\sqrt r
 \left[\log r-\frac12(r-r^{-1})\right]<0.$$ Indeed, $h(r)=\frac12(r-r^{-1})-\log r$ obeys $h(1)=0$ and $h'(r)=(r-1)^2/(2r^2)>0$. Thus the compressive signs selected in [\[eq:lax\]](#eq:lax){reference-type="eqref" reference="eq:lax"} are strictly entropy admissible; the opposite algebraic signs are expansive and violate the Lax condition.

Every self-similar Lax solver with the prescribed family order must follow these exhaustive 1- and 2-wave curves. Their unique intersection from Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}, together with the strict wave ordering above, proves uniqueness of the assembled two-wave entropy solution.

The same monotonicity that constructs $\rho_*$ gives a useful global fact. Even when $u_R-u_L$ is arbitrarily large, the left side of [\[eq:root\]](#eq:root){reference-type="eqref" reference="eq:root"} reaches it only at a strictly positive root. Unlike the $\gamma>1$ polytropic case, the logarithm diverges at zero and prevents a finite-data vacuum gap.

\>1

# Boundaries, executable evidence, and Route A

Common multiplication of $\rho_L,\rho_R,\rho_*$ by a positive constant leaves all velocities, density ratios, branch choices and wave speeds invariant. If either comparison in the table is equality, that wave has zero strength; if both are equal, the datum is constant. Initial vacuum is excluded rather than hidden behind the logarithm.

The limit $a\downarrow0$ is singular: the two eigenvalues merge and [\[eq:root\]](#eq:root){reference-type="eqref" reference="eq:root"} loses coercivity. For example, with $\rho_L=\rho_R=1$ and $u_R-u_L=1$, the rarefaction--rarefaction root is $\rho_*=e^{-1/(2a)}\downarrow0$. Reversing the velocity jump gives a shock--shock root $\rho_*=y^2$, where $y-y^{-1}=1/(2a)$, so $\rho_*\to\infty$. These exact opposite limits expose vacuum and concentration scales; this paper makes no pressureless-limit solution theorem.

The accompanying exact certificate reconstructs rational shock cases, logarithmic rarefaction cases, all four patterns, residual signs, Lax ordering, density scaling and vanishing waves with an independent checker and symbolic lane. These finite rows regress formulas; Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"} follows from the analytic monotonicity and entropy argument.

C195 concerns scalar periodic viscous Burgers dynamics; the present owner is a two-field inviscid Riemann flow. Its strict Route-A tuple is $(\mathrm{A0\_FAIL},\mathrm{A1\_FAIL},\mathrm{A2\_FAIL},
\mathrm{A3\_FAIL},\mathrm{A4\_FAIL})$, and Route B is locked. Continuous wave data and a finite entropy fan are not prime-indexed primitive orbits, an arithmetic clock, a target determinant, or a Hilbert--Pólya operator. The overall verdict is `ROUTE_A_REJECTED`. The literal scope is `NO_BAD_EULER_OR_ROOT_NUMBER`.

# Literature ownership and AI-use statement {#literature-ownership-and-ai-use-statement .unnumbered}

The characteristic, shock and Riemann-solver framework belongs to the classical theory of hyperbolic conservation laws and gas dynamics [@Lax1957; @RozhdestvenskiiJanenko1983; @Dafermos2010]. We claim no literary priority; this source-local paper derives the frozen isothermal case completely. AI tools assisted algebraic checking, hostile boundary review and manuscript preparation. Every theorem and computation is exposed for independent verification.

9 P. D. Lax, "Hyperbolic systems of conservation laws II," *Communications on Pure and Applied Mathematics* 10 (1957), 537--566. DOI: [10.1002/cpa.3160100406](https://doi.org/10.1002/cpa.3160100406).

B. L. Rozhdestvenskii and N. N. Janenko, *Systems of Quasilinear Equations and Their Applications to Gas Dynamics*, AMS, 1983. DOI: [10.1090/mmono/055](https://doi.org/10.1090/mmono/055).

C. M. Dafermos, *Hyperbolic Conservation Laws in Continuum Physics*, 3rd ed., Springer, 2010. DOI: [10.1007/978-3-642-04048-1](https://doi.org/10.1007/978-3-642-04048-1).
