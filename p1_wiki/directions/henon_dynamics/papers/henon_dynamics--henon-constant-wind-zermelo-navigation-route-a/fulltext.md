---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-constant-wind-zermelo-navigation-route-a"
canonical_tex: "henon_dynamics/henon_constant_wind_zermelo_navigation_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_constant_wind_zermelo_navigation_route_a/paper/main.pdf"
source_sha256: "6fc96d5e713e100d4fe0be092f5811e8b698472de36d18eb268f502483273e94"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Constant-Wind Zermelo Navigation Beyond the Randers Chamber

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_constant_wind_zermelo_navigation_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_constant_wind_zermelo_navigation_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_constant_wind_zermelo_navigation_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_constant_wind_zermelo_navigation_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For every finite $d\ge1$, constant wind $W\in\mathbb R^d$, control cap $c\ge0$, and target, we give the complete minimum-time atlas for $\dot x=W+u$, $|u|\le c$. A single theorem covers weak, critical, and strong wind, including exact reachability, value formulas, and all attainable times. \>0 It also proves the unique constant optimizer, HJB equation, symmetries, Mach-cone regularity, and all zero-data faces. \>1 A 744-cell archive and independent checker, symbolic, replay, mutation, and deterministic-build lanes supply regression evidence without replacing proof.
author:
- 'Route-A source-local certificate HCS-C305'
date: 3 September 2026
title: 'Constant-Wind Zermelo Navigation Beyond the Randers Chamber'
```

## Markdown 正文

trailerid \[\<C3052026090300000000000000000000\>\<C3052026090300000000000000000000\>\]

# The all-chamber value theorem

Consider measurable controls $u$ satisfying $|u(t)|\le c$ a.e. and $$\label{eq:system}
 \dot x=W+u,\qquad x(0)=0.$$ For a target $y$, write $$w=|W|,\qquad p=W\cdot y,\qquad r=|y|,
 \qquad a=w^2-c^2,\qquad D=p^2-ar^2.$$

[\[thm:atlas\]]{#thm:atlas label="thm:atlas"} At exact time $t\ge0$, the reachable set is $$\label{eq:ball}
 \mathcal R(t)=Wt+ct\overline B.$$ For $y\ne0$, minimum time and all attainable times are as follows.

1.  If $w<c$, every $y$ is reachable, $$\label{eq:weak}
     T(y)=\frac{\sqrt{p^2+(c^2-w^2)r^2}-p}{c^2-w^2},
     \qquad \mathcal I(y)=[T,\infty).$$

2.  If $w=c>0$, reachability is equivalent to $p>0$, and then $$\label{eq:critical}
     T(y)=\frac{r^2}{2p},\qquad \mathcal I(y)=[T,\infty).$$

3.  If $w>c$, reachability is equivalent to $p>0$ and $D\ge0$. Then $$\label{eq:strong}
     T_\mp(y)=\frac{p\mp\sqrt D}{w^2-c^2},\qquad
     T(y)=T_-(y),\qquad \mathcal I(y)=[T_-,T_+].$$

For every nonzero reachable target the time-optimal control is unique up to null sets and constant: $$\label{eq:control}
 u_*(s)=y/T(y)-W,\qquad |u_*|=c.$$

Integrating [\[eq:system\]](#eq:system){reference-type="eqref" reference="eq:system"} shows that control averages fill $c\overline B$, proving [\[eq:ball\]](#eq:ball){reference-type="eqref" reference="eq:ball"}. Thus $y$ is attainable at $t$ exactly when $$\label{eq:quadratic}
 |y-Wt|^2\le c^2t^2
 \quad\Longleftrightarrow\quad
 f(t)=at^2-2pt+r^2\le0.$$ For $y\ne0$, $f(0)>0$. If $a<0$, its roots have opposite signs and the positive root is [\[eq:weak\]](#eq:weak){reference-type="eqref" reference="eq:weak"}; the inequality holds thereafter. If $a=0$, it is linear and crosses zero at positive time exactly when $p>0$, giving [\[eq:critical\]](#eq:critical){reference-type="eqref" reference="eq:critical"}. If $a>0$, it has a nonnegative-time sublevel interval exactly when $p>0$ and $D\ge0$. Both roots are then positive and the sublevel set is precisely [\[eq:strong\]](#eq:strong){reference-type="eqref" reference="eq:strong"}; in particular the minimum is the smaller root, not $T_+$.

At first contact, $|y-WT|=cT$. Any optimal control obeys $$\left|T^{-1}\int_0^T u(s)\,ds\right|=c
 \le T^{-1}\int_0^T|u(s)|\,ds\le c.$$ Equality in the strictly convex Euclidean triangle inequality forces the control to equal $y/T-W$ a.e. For $c=0$ this conclusion is immediate.

\>0

# Value geometry, HJB, and exact boundaries

[\[prop:hjb\]]{#prop:hjb label="prop:hjb"} For every orthogonal $Q$, $\lambda>0$, and $s>0$, $$\label{eq:symmetry}
 T_{QW,c}(Qy)=T_{W,c}(y),\quad
 T_{W,c}(\lambda y)=\lambda T_{W,c}(y),\quad
 T_{sW,sc}(y)=s^{-1}T_{W,c}(y).$$ On each interior component where $T$ is finite and $y\ne0$, it is smooth and $$\label{eq:hjb}
 W\cdot\nabla T+c|\nabla T|=1.$$

Equation [\[eq:symmetry\]](#eq:symmetry){reference-type="eqref" reference="eq:symmetry"} follows from [\[eq:system\]](#eq:system){reference-type="eqref" reference="eq:system"}, or directly from $p,r,w,c$. First assume $c>0$. At first contact put $F(y,T)=|y-WT|^2-c^2T^2=0$. Implicit differentiation gives $$\label{eq:gradient}
 \nabla T=\frac{y-WT}{p-(w^2-c^2)T}.$$ The denominator is $\sqrt D>0$ on the selected smooth radical branch and is $p>0$ in critical wind. Using $|y-WT|=cT$ in [\[eq:gradient\]](#eq:gradient){reference-type="eqref" reference="eq:gradient"} yields [\[eq:hjb\]](#eq:hjb){reference-type="eqref" reference="eq:hjb"} with the displayed plus sign. If $c=0$ and $d>1$, the reachable ray has empty Euclidean interior. If $c=0$, $d=1$, and $W\ne0$, write $e=W/|W|$ and $y=se$ on the open forward ray. Then $T=s/|W|$, $\nabla T=e/|W|$, and $W\cdot\nabla T=1$ directly.

The formulas remain exact on their stated faces, but the domains change.

  ----------------------------------------------------------------------------------------------
  Face             Exact conclusion
  ---------------- -----------------------------------------------------------------------------
  $y=0$            $T=0$; every $t\ge0$ is feasible if $w\le c$, only $t=0$ if $w>c$.

  $W=0<c$          $T(y)=|y|/c$ for every target.

  $c=0$, $W\ne0$   only $y=tW$, $t\ge0$, is reachable; $u=0$ is forced.

  $W=c=0$          only the zero target is reachable.

  $w=c>0$          nonzero finite-value domain is the open half-space $p>0$.

  $0<c<w$          full finite-value domain is the closed cone $\{0\}\cup\{y\ne0:p>0,D\ge0\}$.

  $D=0$            double time root and square-root loss on a nontrivial cone boundary.
  ----------------------------------------------------------------------------------------------

In one dimension with $0<c<w$, the nonzero reachable ray lies in the smooth interior algebraically; a nontrivial angular cone boundary requires higher dimension. When $c=0$, the ray is handled separately. Weak wind is the gauge of a velocity ball containing the origin, but the strong-wind value is not a global Finsler norm because it is infinite outside its cone.

\>1

# Evidence, hostile audit, and Route-A boundary

The archive has 29 exact cases: zero wind; generic weak wind; reachable and unreachable critical targets; strong-wind axis, interior, double-root cone, exterior, and backward cases; zero cap; zero velocity; and zero targets in all chambers. Twelve smooth probes reconstruct [\[eq:gradient\]](#eq:gradient){reference-type="eqref" reference="eq:gradient"}, [\[eq:hjb\]](#eq:hjb){reference-type="eqref" reference="eq:hjb"}, and both scalings. Together with eight boundary rows this is 744 audited leaves. An independent checker performs 734 assertions, a separate SymPy lane checks 27 identities, isolated replay is byte-exact, and 85 repaired-hash or parser mutations must all fail.

The hostile suite changes the selected strong root, finite time window, critical sign, zero-target time set, optimizer, HJB sign and values, exact keys/types/IDs, and Route-A semantics. Duplicate/nonfinite JSON and duplicate/anchor/alias/merge YAML are rejected. Three round variants are rebuilt twice at a fixed epoch; the final PDF is the round-2 alias. Warnings, fonts, text, pages, and rasterization are checked. These finite lanes regress the theorem; the global proof is the quadratic argument [\[eq:quadratic\]](#eq:quadratic){reference-type="eqref" reference="eq:quadratic"}.

#### Collision and claim boundaries.

C222 is a second-order double-integrator bang--bang system; C270 uses Heisenberg sub-Riemannian geometry; C268 is an uncontrolled constant-field Lorentz flow. C305 closes first-order controlled Euclidean navigation in every finite dimension and all wind chambers. It does not claim variable wind, obstacles, state constraints, manifolds, or literature novelty.

Under `NO_BAD_EULER_OR_ROOT_NUMBER`, the exact tuple is $$(\mathrm{A0\_FAIL},\mathrm{A1\_FAIL},\mathrm{A2\_FAIL},
  \mathrm{A3\_FAIL},\mathrm{A4\_FAIL}).$$ Travel data are not arithmetic local factors (A0); point-to-point controls are not a primitive periodic-orbit ledger (A1); physical time is not a rational-prime clock (A2); no target determinant or functional equation is constructed (A3); HJB supplies no self-adjoint Hilbert--Pólya operator or target-zero match (A4). Therefore the overall verdict is `ROUTE_A_REJECTED`, and Route B stays locked. No target Euler factor, root number, automorphy, divisor law, functional equation, or zero correspondence is asserted.

#### Reproducibility and AI use.

The release retains canonical evidence, independent executable lanes, three substantive manuscript revisions, and a self-excluding manifest. A generative language model assisted drafting and code scaffolding; independent checks audit formulas, artifacts, and scope, and final responsibility remains with the authors.

# Source lineage {#source-lineage .unnumbered}

Zermelo's 1931 paper is the historical owner token for the navigation problem. Bao, Robles, and Shen provide navigation/Randers geometric context. The citations establish lineage, not novelty or priority.

9 E. Zermelo, "Über das Navigationsproblem bei ruhender oder veränderlicher Windverteilung," *ZAMM* 11 (1931), 114--124. DOI: [10.1002/zamm.19310110205](https://doi.org/10.1002/zamm.19310110205). D. Bao, C. Robles, and Z. Shen, "Zermelo navigation on Riemannian manifolds," *J. Differential Geom.* 66 (2004), 377--435. DOI: [10.4310/jdg/1098137838](https://doi.org/10.4310/jdg/1098137838).
