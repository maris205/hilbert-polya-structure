---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-kirchhoff-ellipse-love-stability-route-a"
canonical_tex: "henon_dynamics/henon_kirchhoff_ellipse_love_stability_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_kirchhoff_ellipse_love_stability_route_a/paper/main.pdf"
source_sha256: "6a12605861ee972ee83aecfeaba8f2fd43f4bae8aae44173c9e84688726df0ae"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The Complete Love-Mode Threshold Ladder for Kirchhoff's Uniform Elliptic Vortex

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_kirchhoff_ellipse_love_stability_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_kirchhoff_ellipse_love_stability_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_kirchhoff_ellipse_love_stability_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_kirchhoff_ellipse_love_stability_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For a uniform-vorticity ellipse in the unbounded plane, we separate the classical input from a complete all-mode consequence. The patch is an exact Euler relative equilibrium with shape rate $\Omega=\omega_0ab/(a+b)^2$. Love's dispersion relation factors into two dimensionless scalar terms: one is positive and the other has exactly one zero for every mode $m\ge3$. We prove strict ordering of all thresholds, the sharp first wall $a/b=3$, and an exact closed asymptotic description of the ladder. Exact rational evidence audits $35{,}904$ modal cells. Every stability statement is spectral and linear; no nonlinear stability, Jordan, or filamentation theorem is asserted.
author:
- 'HCS-C372 / HEN-O356'
date: 4 September 2026
title: |
  The Complete Love-Mode Threshold Ladder\
  for Kirchhoff's Uniform Elliptic Vortex
```

## Markdown 正文

suppressoptionalinfo 512 trailerid \[\<C3722026090400000000000000000000\>\<C3722026090400000000000000000000\>\]

# The exact Euler relative equilibrium

Consider the planar Euler vorticity equation $$\label{eq:euler}
 \partial_t\omega+u\mathbin{\cdot}\nabla\omega=0,
 \qquad \nabla\mathbin{\cdot}u=0,
 \qquad \operatorname{curl}u=\omega,$$ with velocity decaying modulo its circulation field at infinity. Let $$\label{eq:patch}
 E_0=\left\{(x,y):\frac{x^2}{a^2}+\frac{y^2}{b^2}<1\right\},
 \qquad a\ge b>0,
 \qquad \omega(x,0)=\omega_0\mathbf1_{E_0}.$$ Positive $\omega_0$ is counterclockwise.

[\[thm:kirchhoff\]]{#thm:kirchhoff label="thm:kirchhoff"} For $a>b$, the Kirchhoff patch evolution from [\[eq:patch\]](#eq:patch){reference-type="eqref" reference="eq:patch"} is the relative equilibrium $$\label{eq:omega}
 E_t=R_{\Omega t}E_0,
 \qquad \Omega=\frac{\omega_0ab}{(a+b)^2}.$$ The interior velocity at the displayed orientation is $$\label{eq:inside}
 u(x,y)=\frac{\omega_0}{a+b}(-ay,bx).$$ The area, circulation, and quadratic vorticity moment are $$\label{eq:invariants}
 |E_t|=\pi ab,\qquad
 \Gamma=\pi\omega_0ab,\qquad
 I:=\int_{\mathbb R^2}|x|^2\omega(x,t)\,dx
 =\frac{\pi\omega_0ab(a^2+b^2)}4.$$ If $\Omega\ne0$, the unmarked patch has minimal period $\pi/|\Omega|$; an oriented-axis lift has period $2\pi/|\Omega|$.

With $u=(-\psi_y,\psi_x)$, the interior streamfunction is $$\psi_{\rm in}=\frac{\omega_0}{2(a+b)}(bx^2+ay^2),$$ which gives [\[eq:inside\]](#eq:inside){reference-type="eqref" reference="eq:inside"}, zero divergence, and curl $\omega_0$. In elliptic coordinates $x=c\cosh\xi\cos\eta$, $y=c\sinh\xi\sin\eta$, the harmonic exterior expression $$\psi_{\rm out}=\frac{\omega_0ab}{2}\xi
 +\frac{\omega_0ab}{4}e^{-2\xi}\cos2\eta+C$$ matches the boundary Cauchy data for a suitable constant $C$; this is the classical Kirchhoff construction [@MitchellRossi]. At $(a\cos\theta,b\sin\theta)$, dotting the difference between [\[eq:inside\]](#eq:inside){reference-type="eqref" reference="eq:inside"} and $\Omega(-y,x)$ with the unnormalized normal $(\cos\theta/a,\sin\theta/b)$ gives $$\sin\theta\cos\theta\left\{
 \frac{\omega_0(a-b)}{a+b}
 -\frac{\Omega(a^2-b^2)}{ab}\right\}.$$ It vanishes exactly for [\[eq:omega\]](#eq:omega){reference-type="eqref" reference="eq:omega"}; tangential differences only reparametrize the contour. The contour therefore rotates without changing shape. Direct ellipse integration gives [\[eq:invariants\]](#eq:invariants){reference-type="eqref" reference="eq:invariants"}. Finally, $R_\pi E_0=E_0$ while no smaller positive rotation fixes a noncircle, proving the two period statements.

\>0

# Love factorization and every finite-mode wall

This revision is the **all-mode spectral-wall owner**. Put $$\label{eq:variables}
 \gamma=\frac ab\ge1,\qquad
 \delta=\frac{a-b}{a+b}\in[0,1),\qquad
 \kappa=\frac{2ab}{(a+b)^2}=\frac{1-\delta^2}{2}.$$

[\[prop:love\]]{#prop:love label="prop:love"} Resolve the boundary perturbation in elliptic coordinates whose axes co-rotate with the unperturbed ellipse. Thus the Fourier label $m\ge1$ is measured relative to the instantaneous principal axes, and $\lambda_m$ is the co-rotating-frame frequency under the convention $e^{-i\lambda_mt}$. The linearized contour equation has characteristic square $$\label{eq:love}
 \lambda_m^2=\frac{\omega_0^2}{4}
 \left\{\left[\frac{2mab}{(a+b)^2}-1\right]^2
 -\left(\frac{a-b}{a+b}\right)^{2m}\right\}.$$ Equation [\[eq:love\]](#eq:love){reference-type="eqref" reference="eq:love"} is classical Love theory, not a newly derived linearization here [@Love; @MitchellRossi]. The results below are exact consequences of this sourced characteristic equation.

Define $$\label{eq:FG}
 F_m(\delta)=\frac m2(1-\delta^2)-1-\delta^m,
 \qquad
 G_m(\delta)=\frac m2(1-\delta^2)-1+\delta^m.$$

[\[thm:wall\]]{#thm:wall label="thm:wall"} The symmetry modes obey $$\label{eq:symmetry}
 \lambda_1^2=\Omega^2,\qquad \lambda_2^2=0
 \quad\hbox{for every ellipse}.$$ For each $m\ge3$, $F_m$ has a unique zero $\delta_m\in(0,1)$, while $G_m(\delta)>0$ on $[0,1)$. For $\omega_0\ne0$, mode $m$ is oscillatory when $\delta<\delta_m$, critical at equality, and has an exponentially growing/decaying spectral pair when $\delta>\delta_m$.

The thresholds are strictly ordered: $$\label{eq:ordered}
 \delta_3<\delta_4<\cdots,\qquad
 \gamma_m:=\frac{1+\delta_m}{1-\delta_m},\qquad
 \gamma_3<\gamma_4<\cdots.$$ The first wall is sharp: $$\label{eq:first}
 \delta_3=\frac12,\qquad \gamma_3=3.$$ Thus all $m\ge3$ squares are positive for $1\le\gamma<3$; at $\gamma=3$ only $m=3$ reaches zero, and for $\gamma>3$ the $m=3$ square is negative. These are spectral statements; zero or repeated characteristic roots are not a claim about Jordan structure.

Equations [\[eq:variables\]](#eq:variables){reference-type="eqref" reference="eq:variables"} and [\[eq:love\]](#eq:love){reference-type="eqref" reference="eq:love"} give, without dividing by the possibly zero vorticity, $$\label{eq:factor}
 4\lambda_m^2=\omega_0^2F_m(\delta)G_m(\delta).$$ Substitution of $m=1,2$ proves [\[eq:symmetry\]](#eq:symmetry){reference-type="eqref" reference="eq:symmetry"}. For $m\ge3$, $$F_m(0)=m/2-1>0,\quad F_m(1)=-2,\quad
 F_m'(\delta)=-m\delta-m\delta^{m-1}<0$$ on $(0,1)$, proving existence and uniqueness. The other factor satisfies $$\label{eq:G}
 G_m'(\delta)=m\delta(\delta^{m-2}-1)<0,\qquad G_m(1)=0,$$ so $G_m>0$ on $[0,1)$. This proves the sign classification.

At every $0\le\delta<1$, $$\label{eq:difference}
 F_{m+1}(\delta)-F_m(\delta)
 =\frac{1-\delta^2}{2}+\delta^m(1-\delta)>0.$$ Hence $F_{m+1}(\delta_m)>0$; strict decrease places its zero to the right of $\delta_m$. The map from $\delta$ to $\gamma$ is increasing. Finally, direct factorization gives $$\label{eq:m3}
 16\lambda_3^2
 =\omega_0^2(1-\delta^2)^2(1-4\delta^2),$$ which proves [\[eq:first\]](#eq:first){reference-type="eqref" reference="eq:first"} and the global first-wall statement.

\>1

# Asymptotic ladder and finite instability count

This revision is the **asymptotic--boundary--route owner**.

[\[thm:asymptotic\]]{#thm:asymptotic label="thm:asymptotic"} Let $W$ be the principal Lambert function and set $$\label{eq:cstar}
 c_*=1+W(e^{-1}),\qquad c_*=1.2784\ldots.$$ Then $$\label{eq:asymptotic}
 m(1-\delta_m)\longrightarrow c_*,
 \qquad \frac{\gamma_m}{m}\longrightarrow\frac{2}{c_*}.$$ Consequently, for each fixed finite $\gamma$, only finitely many modes have negative square. Because of [\[eq:ordered\]](#eq:ordered){reference-type="eqref" reference="eq:ordered"}, they form an initial block $m=3,\ldots,M$, possibly empty, with at most one next mode critical.

Write $c_m=m(1-\delta_m)$. The equation $F_m(\delta_m)=0$ becomes $$\label{eq:scaled}
 c_m-\frac{c_m^2}{2m}=1+\left(1-\frac{c_m}{m}\right)^m.$$ The left-minus-right side at $c=1$ is negative. At $c=2$ it equals $1-2/m-(1-2/m)^m>0$, since $0<1-2/m<1$ and $m\ge3$. Uniqueness of $\delta_m$ gives $1<c_m<2$. Along any convergent subsequence, [\[eq:scaled\]](#eq:scaled){reference-type="eqref" reference="eq:scaled"} tends to $c=1+e^{-c}$. The difference $c-1-e^{-c}$ is strictly increasing and has one zero; writing $c-1=e^{-c}$ gives $c=c_*$ in [\[eq:cstar\]](#eq:cstar){reference-type="eqref" reference="eq:cstar"}. Thus the entire sequence converges. Since $$\frac{\gamma_m}{m}=\frac{2-c_m/m}{c_m},$$ the second limit follows, as do divergence of $\gamma_m$ and the finite initial-block assertion.

::: {#tab:thresholds}
  $m$                3       4       5       6        8       16       32       64
  ------------ ------- ------- ------- ------- -------- -------- -------- --------
  $\gamma_m$     3.000   4.612   6.197   7.774   10.917   23.450   48.488   98.552

  : Readable midpoints of exact $2^{-96}$ threshold brackets; only the first entry is asserted as an exact decimal.
:::

The canonical evidence covers $561$ reduced rational aspects $1\le\gamma\le8$ with denominator at most $16$, all $64$ modes, and hence $35{,}904$ exact modal cells. It also stores $62$ threshold certificates for $3\le m\le64$ and $390$ rigid-solution rows. The producer uses rational arithmetic; a checker that never imports it reconstructs the unfactorized Love square and locates the adjacent dyadics by integer binary search. Finite evidence is regression, not proof by sampling.

# Boundary atlas and claim boundary

At $a=b$, the patch is the Rankine circle: its shape is stationary and orientation is unobservable. The continuation value $\Omega=\omega_0/4$ is therefore a gauge for the degenerating ellipse orientation, while the interior fluid rotates at $\omega_0/2$. Formula [\[eq:love\]](#eq:love){reference-type="eqref" reference="eq:love"} reduces to $\lambda_m^2=\omega_0^2(m-2)^2/16$. At $\omega_0=0$, the velocity, $\Omega$, and all modal squares vanish. Swapping $a,b$ reverses $\delta$ but leaves [\[eq:love\]](#eq:love){reference-type="eqref" reference="eq:love"} unchanged. The limit $b\downarrow0$ ($\delta\uparrow1$) is a singular strip boundary, not a bounded ellipse in the theorem. Negative vorticity reverses shape rotation but does not change the modal-square signs.

Mitchell and Rossi supply the modern planar convention and compare linear modes with simulations [@MitchellRossi]. Miyazaki and Hanazaki study a stratified baroclinic problem [@MiyazakiHanazaki]; it is cited as an excluded extension, not as support for the planar Love formula. C284 uses finite point vortices, C299 uses viscous Lamb--Oseen diffusion, and C368 uses source/sink Laplacian growth. None owns this inviscid distributed-patch threshold ladder. We claim no classical priority.

No nonlinear orbital or Lyapunov stability, Jordan classification, finite-amplitude filamentation or fission, viscous or wall effect, three-dimensional instability, or post-threshold morphology is proved. The continuous aspect family has no rational-prime carrier or isolated primitive-orbit ledger; the modal characteristic polynomial is not a dynamical zeta, target determinant, or Euler product. The Route-A record is $$(A0_{\rm FAIL},A1_{\rm WEAK},A2_{\rm FAIL},A3_{\rm FAIL},
 A4_{\rm FORMAL\_HINT}),$$ with overall verdict `ROUTE_A_REJECTED`. The formal Hamiltonian linearization hint is not a same-clock self-adjoint quantization. Under `NO_BAD_EULER_OR_ROOT_NUMBER`, no target zero match, Hilbert--Pólya operator, or Route B is claimed.

9 A. E. H. Love, *On the Stability of certain Vortex Motions*, Proceedings of the London Mathematical Society s1-25 (1893), 18--43. <https://doi.org/10.1112/plms/s1-25.1.18>. T. B. Mitchell and L. F. Rossi, *The evolution of Kirchhoff elliptic vortices*, Physics of Fluids 20 (2008), 054103. <https://doi.org/10.1063/1.2912991>. T. Miyazaki and H. Hanazaki, *Baroclinic instability of Kirchhoff's elliptic vortex*, Journal of Fluid Mechanics 261 (1994), 253--271. <https://doi.org/10.1017/S0022112094000339>.
