---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-dubins-bounded-curvature-optimal-synthesis-route-a"
canonical_tex: "henon_dynamics/henon_dubins_bounded_curvature_optimal_synthesis_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_dubins_bounded_curvature_optimal_synthesis_route_a/paper/main.pdf"
source_sha256: "2324a9303b8658be495a311e63033563c0eaa0d0cec73848b1b5cb37fb436579"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Boundary-Safe Global Synthesis for the Dubins Car

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_dubins_bounded_curvature_optimal_synthesis_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_dubins_bounded_curvature_optimal_synthesis_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_dubins_bounded_curvature_optimal_synthesis_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_dubins_bounded_curvature_optimal_synthesis_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We give a complete executable form of the Dubins shortest-path theorem: all six $CSC/CCC$ words, feasibility tests, segment triples, and the global all-ties minimum for arbitrary oriented planar endpoints and turning radius. \>0 The theorem closes collapsed pieces, tangent and three-circle boundaries, coincident poses, inverse-angle conventions, scaling, reflection, and direct endpoint replay. \>1 An independent 180-cell audit and adversarial release pipeline test every candidate without promoting controlled paths to arithmetic orbits.
author:
- 'Route-A source-local certificate HCS-C310'
date: 3 September 2026
title: 'Boundary-Safe Global Synthesis for the Dubins Car'
```

## Markdown 正文

trailerid \[\<C3102026090300000000000000000000\>\<C3102026090300000000000000000000\>\]

# Six-word global synthesis

At unit speed and turning radius $R>0$, the car satisfies $$\label{eq:car}
 \dot x=\cos\vartheta,\qquad \dot y=\sin\vartheta,
 \qquad |\dot\vartheta|\le R^{-1},$$ and moves only forward. Rigid motion fixes the initial pose at $(0,0,0)$. Divide the target position by $R$ and write $$d=R^{-1}\sqrt{x^2+y^2},\quad \theta=\operatorname{atan2}(y,x),
 \quad \alpha=\mathop{\rm mod}_{2\pi}(-\theta),\quad \beta=\mathop{\rm mod}_{2\pi}(\phi-\theta).$$ Here $\mathop{\rm mod}_{2\pi}z$ is the representative in $[0,2\pi)$, with $\mathop{\rm mod}_{2\pi}(2\pi)=0$. Put $s_a=\sin\alpha$, $c_a=\cos\alpha$ and similarly for $b$, and $c_{ab}=\cos(\alpha-\beta)$. The following table is an explicit algorithm. Every square root requires its radicand $P\ge0$.

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  word    normalized segments $(t,p,q)$ and feasibility
  ------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  $LSL$   $P=2+d^2-2c_{ab}+2d(s_a-s_b)$, $\psi=\operatorname{atan2}(c_b-c_a,d+s_a-s_b)$; $(\mathop{\rm mod}_{2\pi}(-\alpha+\psi),\sqrt P,\mathop{\rm mod}_{2\pi}(\beta-\psi))$.

  $RSR$   $P=2+d^2-2c_{ab}+2d(s_b-s_a)$, $\psi=\operatorname{atan2}(c_a-c_b,d-s_a+s_b)$; $(\mathop{\rm mod}_{2\pi}(\alpha-\psi),\sqrt P,\mathop{\rm mod}_{2\pi}(-\beta+\psi))$.

  $LSR$   $P=-2+d^2+2c_{ab}+2d(s_a+s_b)$, $\psi=\operatorname{atan2}(-c_a-c_b,d+s_a+s_b)-\operatorname{atan2}(-2,\sqrt P)$; $(\mathop{\rm mod}_{2\pi}(-\alpha+\psi),\sqrt P,\mathop{\rm mod}_{2\pi}(-\beta+\psi))$.

  $RSL$   $P=-2+d^2+2c_{ab}-2d(s_a+s_b)$, $\psi=\operatorname{atan2}(c_a+c_b,d-s_a-s_b)-\operatorname{atan2}(2,\sqrt P)$; $(\mathop{\rm mod}_{2\pi}(\alpha-\psi),\sqrt P,\mathop{\rm mod}_{2\pi}(\beta-\psi))$.

  $RLR$   $h=(6-d^2+2c_{ab}+2d(s_a-s_b))/8$, $|h|\le1$; $p=\mathop{\rm mod}_{2\pi}(2\pi-\arccos h)$, $t=\mathop{\rm mod}_{2\pi}(\alpha-\operatorname{atan2}(c_a-c_b,d-s_a+s_b)+p/2)$, $q=\mathop{\rm mod}_{2\pi}(\alpha-\beta-t+p)$.

  $LRL$   $h=(6-d^2+2c_{ab}+2d(-s_a+s_b))/8$, $|h|\le1$; $p=\mathop{\rm mod}_{2\pi}(2\pi-\arccos h)$, $t=\mathop{\rm mod}_{2\pi}(-\alpha-\operatorname{atan2}(c_a-c_b,d+s_a-s_b)+p/2)$, $q=\mathop{\rm mod}_{2\pi}(\beta-\alpha-t+p)$.
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[\[thm:dubins\]]{#thm:dubins label="thm:dubins"} Compute every feasible row above, allowing zero segments. Then $$\label{eq:min}
 D_R((0,0,0),(x,y,\phi))
   =R\min_{w\in\{LSL,RSR,LSR,RSL,RLR,LRL\}}(t_w+p_w+q_w).$$ Every minimizing row is a global shortest curve, and every global shortest curve has one of these descriptions, up to zero-piece degeneracy.

The Pontryagin switching function makes a nonsingular extremal a concatenation of maximum-curvature left/right arcs and straight segments. The classical Dubins shortening argument removes repeated equal turns, excludes four or more essential pieces, and leaves precisely $CSC$ or $CCC$, hence the six rows. External and internal circle tangencies give the four radicands; the law of cosines for the three unit circles gives the two values $h$. Solving the remaining oriented angles yields the table. Thus evaluating all feasible rows proves [\[eq:min\]](#eq:min){reference-type="eqref" reference="eq:min"}; taking all equal minima retains every global tie.

\>0

# Boundaries, ties, and symmetries

For a pose $(X,Y,H)$, a normalized primitive of length $a$ is $$\begin{aligned}
 L_a &: (X+\sin(H+a)-\sin H,\;Y-\cos(H+a)+\cos H,\;H+a),\\
 R_a &: (X+\sin H-\sin(H-a),\;Y+\cos(H-a)-\cos H,\;H-a),\\
 S_a &: (X+a\cos H,\;Y+a\sin H,\;H).\end{aligned}$$ Substitution of each table row gives $(x/R,y/R,\phi)$ modulo $2\pi$; this is a direct endpoint proof independent of comparing lengths. It also shows that $R(t+p+q)\ge\sqrt{x^2+y^2}$.

At $P=0$ the straight tangent collapses. At $h=1$ the middle $CCC$ arc may collapse; at $h=-1$ it is a half turn. In these cells multiple word labels can describe the same geometric curve, and [\[eq:min\]](#eq:min){reference-type="eqref" reference="eq:min"} deliberately keeps all of them. For deterministic boundary coordinates we set $\operatorname{atan2}(0,0)=0$; changing that representative only redistributes zero or full-turn pieces and cannot lower the geometric minimum. Coincident poses, a pure heading change, heading wrap, and a completely zero path are therefore covered without an informal exception.

For every $s>0$, simultaneous replacement $(x,y,R)\mapsto(sx,sy,sR)$ multiplies the answer by $s$. Rigid motions of both poses preserve it. Reflection $(x,y,\phi)\mapsto(x,-y,-\phi)$ exchanges $L\leftrightarrow R$, pairing $LSL/RSR$, $LSR/RSL$, and $LRL/RLR$.

\>1

# Evidence and Route-A boundary

Thirty rational/rational-$\pi$ poses generate 180 word cells, of which 151 are feasible, and 1,978 audited leaves. All six words occur among retained minimizers. An independent implementation reconstructs every discriminant, segment and terminal pose in 2,087 checks; SymPy verifies 21 primitive, reflection, scaling and endpoint identity groups; replay is byte exact; and 30 repaired-hash or parser attacks must fail. Three PDF revisions are built twice at a fixed epoch. These controls regress conventions; Theorem [\[thm:dubins\]](#thm:dubins){reference-type="ref" reference="thm:dubins"} supplies globality.

C222 treats a second-order double integrator, C270 Heisenberg reversible sub-Riemannian motion, and C305 convex constant-wind navigation. C310 instead owns forward-only $SE(2)$ curvature and the boundary-safe six-word synthesis.

Under `NO_BAD_EULER_OR_ROOT_NUMBER`, the exact tuple is $$(\mathrm{A0\_FAIL},\mathrm{A1\_FAIL},\mathrm{A2\_FAIL},
  \mathrm{A3\_FAIL},\mathrm{A4\_FORMAL\_HINT}).$$ Poses and words have no rational-prime local meaning (A0); point-to-point controlled arcs are not intrinsic primitive periodic trajectories (A1); arc length is not a logarithmic-prime clock (A2); a finite minimum is no target determinant or functional equation (A3). Pontryagin's Hamiltonian is a source extremal device, not a self-adjoint Hilbert--Pólya operator or target-zero match (A4). Hence Route A is rejected and Route B stays locked. No target Euler factor, root number, automorphy, divisor law, functional equation, or zero correspondence is claimed.

#### AI use.

A generative language model assisted drafting and code scaffolding. Analytic derivations, independent replay, adversarial tests and the fixed artifacts define the audit record; responsibility remains with the authors.

# Source lineage {#source-lineage .unnumbered}

9 L. E. Dubins, "On curves of minimal length with a constraint on average curvature, and with prescribed initial and terminal positions and tangents," *American Journal of Mathematics* 79 (1957), 497--516. DOI: [10.2307/2372560](https://doi.org/10.2307/2372560).
