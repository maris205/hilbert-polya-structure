---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-double-integrator-bang-bang-time-optimal-route-a"
canonical_tex: "henon_dynamics/henon_double_integrator_bang_bang_time_optimal_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_double_integrator_bang_bang_time_optimal_route_a/paper/main.pdf"
source_sha256: "6ad5e8e1e9e8965af03e031c82f22a63c154fa7aac23aea5fcd2e93fcbfa8fdd"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Global Bang--Bang Value Formula for the Bounded Double Integrator

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_double_integrator_bang_bang_time_optimal_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_double_integrator_bang_bang_time_optimal_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_double_integrator_bang_bang_time_optimal_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_double_integrator_bang_bang_time_optimal_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For the physical double integrator $\dot x=v$, $\dot v=u$, $|u|\leq a$, we close the minimum-time problem to rest at the origin on the entire state plane. The switching function $F_a=x+v|v|/(2a)$ selects either direct braking or a unique one-switch control. We give the two arc lengths, switch state and a closed value function, and verify exact termination and the Hamilton--Jacobi equation off the nonsmooth switching curve. A sharp rearrangement bound for the endpoint control moments supplies a global sufficiency proof; the affine Pontryagin switching function is an independent structural check. Origin, zero acceleration, reflection and parabolic scaling are retained explicitly. Executable exact/high-precision, symbolic, replay and hostile-mutation audits accompany the theorem.
author:
- HCS Research Program
date: 28 August 2026(revision 2)
title: 'A Global Bang--Bang Value Formula for the Bounded Double Integrator'
```

## Markdown 正文

suppressoptionalinfo 611

# Convention and synthesis

Fix $a>0$ and let $T_a(x,v)$ be the least physical time for $$\dot x=v,\qquad \dot v=u,\qquad |u|\leq a$$ to reach $(0,0)$. Set $$F_a(x,v)=x+\frac{v|v|}{2a}.$$ This convention fixes the state ordering, acceleration sign, terminal state and time clock; no rescaled or fitted clock is used.

[\[thm:main\]]{#thm:main label="thm:main"} At $(0,0)$, $T_a=0$. If $F_a=0$ and $v\ne0$, the direct brake $u=-a\operatorname{sign}v$ is optimal and $T_a=|v|/a$.

If $F_a\ne0$, let $s=\operatorname{sign}F_a$ and $$D=\frac{v^2}{2a^2}+\frac{sx}{a}.$$ Then $D>0$ and $$t_1=\frac{sv}{a}+\sqrt D\geq0,\qquad t_2=\sqrt D>0,
 \qquad T_a(x,v)=\frac{sv}{a}+2\sqrt D.                 \tag{1}$$ Up to null sets, the optimal control is $u=-sa$ for time $t_1$ and $u=sa$ for time $t_2$. Its switch state is $$(x_1,v_1)=\left(\frac{saD}{2},-sa\sqrt D\right),       \tag{2}$$ and the second arc terminates at $(0,0)$. Moreover, $$T_a(-x,-v)=T_a(x,v),\qquad
 T_a(\lambda^2x,\lambda v)=\lambda T_a(x,v)\quad(\lambda>0). \tag{3}$$

The assertion $D>0$ follows directly from $sF_a>0$; if $sv<0$, that same strict inequality gives $\sqrt D>|v|/a$, and otherwise $t_1\geq0$ is immediate. Integrating the first constant-control arc gives (2). Since $v_1|v_1|=-sa^2D$, (2) lies on $F_a=0$. The second arc has duration $\sqrt D$, so $v_1+sa\sqrt D=0$ and $x_1+v_1\sqrt D+saD/2=0$. Reflection and scaling follow by substitution in (1). The global lower bound is proved below.

# Two independent optimality certificates

For a normal minimum-time extremal, the costate satisfies $\dot p_x=0$ and $\dot p_v=-p_x$. Hence $p_v$ is affine in time and the minimizing control $u=-a\operatorname{sign}p_v$ switches at most once. This explains the structure but, as a necessary condition, is not by itself the global sufficiency proof.

Off $F_a=0$, differentiating (1) gives $$(T_a)_x=\frac{s}{a\sqrt D},\qquad
 (T_a)_v=\frac{s}{a}+\frac{v}{a^2\sqrt D}.$$ The inequality used above gives $\operatorname{sign}(T_a)_v=s$, and therefore $$1+v(T_a)_x-a|(T_a)_v|=0.                               \tag{4}$$ Thus the displayed control attains the minimum in the HJB equation wherever the value is smooth.

\>0

# Sharp reachable-moment lower bound

The missing sufficiency step has a particularly short source-local proof. If a control reaches rest in time $T$, integration of velocity and position gives $$\int_0^T u(t)\,dt=-v,\qquad
 \int_0^T t\,u(t)\,dt=x.                                \tag{5}$$

[\[lem:moment\]]{#lem:moment label="lem:moment"} Every measurable $u$ satisfying $|u|\leq a$ and the first identity in (5) obeys $$-\frac{aT^2}{4}-\frac{vT}{2}+\frac{v^2}{4a}
 \leq \int_0^T t u(t)\,dt \leq
 \frac{aT^2}{4}-\frac{vT}{2}-\frac{v^2}{4a}.            \tag{6}$$ The upper endpoint is attained by placing $-a$ first and $+a$ last; the lower endpoint reverses that order. Apart from null sets these are the only endpoint controls.

Write $u=-a+2aw$ with $0\leq w\leq1$. Its prescribed integral fixes $\int_0^T w=(T-v/a)/2$. The bathtub principle maximizes $\int_0^Ttw(t)\,dt$ by putting $w=1$ on the latest interval of that measure, and minimizes it by putting $w=1$ on the earliest interval. Direct integration gives (6), including the equality cases.

For $F_a>0$, the least feasible time makes the upper inequality in (6) an equality; solving it gives (1) with $s=1$. For $F_a<0$, the lower inequality is active and gives (1) with $s=-1$. The equality cases are precisely the constructed controls. Consequently no shorter transfer is admissible, which completes the global proof of Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}. In viscosity language, the continuous value solves the HJB equation globally, with (4) its classical restriction away from the switch.

# Boundary atlas

On $F_a=0$, both adjacent formulas meet $|v|/a$, but the value need not be classically differentiable. The origin is the zero-duration case. At $a=0$, velocity is constant; only $(0,0)$ can reach rest at the origin in finite time, so every other value is infinite. These branches are not obtained by blindly dividing a positive-$a$ formula by zero.

\>1

# Executable evidence and Route-A boundary

The released ledger contains 105 rational state cases: three origin rows, eight nonzero direct-braking rows and 94 one-switch rows. A producer- independent checker makes 2,278 assertions while reconstructing every branch, radicand, duration, switch and terminal state and HJB residual at 100 digits. SymPy checks 20 generic identities on both sides; clean-process replay is byte exact. Twenty-three repaired-hash semantic/schema mutations and one stale-hash mutation are rejected. These finite rows are regression evidence, not the proof of the all-state result.

The strict Route-A tuple is

(A0\_FAIL, A1\_FAIL, A2\_FAIL, A3\_FAIL, A4\_FORMAL\_HINT),

with `overall=ROUTE_A_REJECTED` and `route_b_invocation_allowed=false`. The Pontryagin Hamiltonian is only a source-local formal hint: it supplies no intrinsic rational-prime carrier, primitive periodic owner, target determinant or analytic structure, and no same-clock Hilbert--Polya operator.

# Source note {#source-note .unnumbered}

Romano and Curti [@romano2020] treat minimum-time bounded normal LTI systems, reduction to an origin transfer, and the double-integrator context. We claim no priority for bang--bang synthesis or Pontryagin's principle; the release contribution is the convention-locked theorem/boundary synthesis and reproducible audit.

9 M. Romano and F. Curti, *Time-optimal control of linear time invariant systems between two arbitrary states*, *Automatica* 120 (2020), 109151. DOI: 10.1016/j.automatica.2020.109151.

# Declarations {#declarations .unnumbered}

**Scope.** `NO_BAD_EULER_OR_ROOT_NUMBER`; no target arithmetic, target-zero or operator claim. **Data and code.** The theorem, canonical ledger and independent audits are released with HCS-C222. **AI-use disclosure.** Generative tools assisted drafting and code generation; the internal artifact chain checked the displayed claims and metadata. This is not external peer review.
