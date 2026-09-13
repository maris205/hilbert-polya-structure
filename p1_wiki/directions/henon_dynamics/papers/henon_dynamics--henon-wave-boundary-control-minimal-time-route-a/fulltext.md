---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-wave-boundary-control-minimal-time-route-a"
canonical_tex: "henon_dynamics/henon_wave_boundary_control_minimal_time_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_wave_boundary_control_minimal_time_route_a/paper/main.pdf"
source_sha256: "ebf69b295c4342346a6643fefe5e2049181b3567e7823736d286d8e1eeeddb7f"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The Exact Minimal Time for One-End Observation and Control of a Finite String

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_wave_boundary_control_minimal_time_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_wave_boundary_control_minimal_time_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_wave_boundary_control_minimal_time_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_wave_boundary_control_minimal_time_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We determine the sharp one-end observation and boundary-control time for the one-dimensional Dirichlet wave equation. =0 The full energy wave group has least revival time $2L/c$, not $L/c$. \>0 At that exact time the endpoint normal derivative satisfies a Parseval identity with constant $4/c^3$, giving observability including the critical equality. \>1 Every shorter window misses a nonzero smooth periodic traveling profile, so the threshold is necessary as well as sufficient. Hilbert Uniqueness Method duality yields the matching one-end Dirichlet control theorem on the precise transposition space. Independent exact evidence audits constants without replacing the infinite-dimensional proof.
author:
- 'Route-A source-local certificate HCS-C287'
date: 2 September 2026
title: |
  The Exact Minimal Time for One-End Observation\
  and Control of a Finite String
```

## Markdown 正文

trailerid \[\<C2872026090200000000000000000000\>\<C2872026090200000000000000000000\>\]

# Frozen string and its full revival

Let $L,c>0$ and consider $$\label{eq:wave}
 u_{tt}-c^2u_{xx}=0,\quad 0<x<L,\qquad
 u(0,t)=u(L,t)=0.$$ The adjoint data lie in $H_0^1(0,L)\times L^2(0,L)$, with conserved energy $$\label{eq:energy}
 E(t)=\frac12\int_0^L\bigl(|u_t(x,t)|^2+c^2|u_x(x,t)|^2\bigr)\,dx.$$ The observation is $u_x(L,\cdot)$. There is no zero mode: the frequencies are $\omega_n=n\pi c/L$, $n\ge1$.

[\[lem:revival\]]{#lem:revival label="lem:revival"} The least positive time for which the wave group is the identity on the full energy space is $$T_\ast=\frac{2L}{c}.$$

At time $T_\ast$, every phase $e^{\pm i\omega_nT_\ast}=e^{\pm2\pi in}$ is one. Conversely, an identity time must return the $n=1$ mode and is therefore an integer multiple of $2L/c$. In particular, $L/c$ multiplies the $n$th mode by $(-1)^n$ and is not the full-space identity.

\>0

# Critical endpoint Parseval identity

Every finite-energy Dirichlet solution has the periodic d'Alembert form $$\label{eq:dalembert}
 u(x,t)=F(x+ct)-F(-x+ct),\qquad F(s+2L)=F(s),\quad F'\in L^2(\mathbb R/2L\mathbb Z).$$ Constants in $F$ are irrelevant. Differentiating gives $$\label{eq:coordinates}
 u_x(L,t)=2F'(L+ct),\qquad
 E=c^2\int_0^{2L}|F'(s)|^2\,ds.$$ The energy equality follows by adding the squares of $u_t$ and $cu_x$ and changing variables over the two reflected halves.

[\[thm:identity\]]{#thm:identity label="thm:identity"} Every solution of [\[eq:wave\]](#eq:wave){reference-type="eqref" reference="eq:wave"} satisfies $$\label{eq:identity}
 \int_0^{2L/c}|u_x(L,t)|^2\,dt=\frac4{c^3}E(0).$$ Consequently one-end boundary observability holds for every $T\ge2L/c$, including equality.

At the critical time, $s=L+ct$ traverses one complete period. Hence $$\int_0^{2L/c}|u_x(L,t)|^2dt
 =\frac4c\int_0^{2L}|F'(s)|^2ds=\frac4{c^3}E(0).$$ For a longer interval, integrate the nonnegative observation over its first critical subinterval.

For comparison, if $$u(x,t)=\sum_{n\ge1}\left(a_n\cos\omega_nt+\frac{b_n}{\omega_n}
 \sin\omega_nt\right)\sin\frac{n\pi x}{L},$$ orthogonality over $[0,2L/c]$ gives [\[eq:identity\]](#eq:identity){reference-type="eqref" reference="eq:identity"} mode by mode. The periodic proof is stronger for the sharpness argument below because it does not truncate the solution.

\>1

# Every shorter window misses a smooth wave

[\[thm:sharp\]]{#thm:sharp label="thm:sharp"} If $0\le T<2L/c$, a nonzero smooth solution of [\[eq:wave\]](#eq:wave){reference-type="eqref" reference="eq:wave"} exists with $$u_x(L,t)=0\qquad(0\le t\le T).$$ Thus no observability inequality, and hence no dual exact one-end control, holds before $2L/c$.

On the circle $\mathbb R/2L\mathbb Z$, the observed arc $\{L+ct:0\le t\le T\}$ has length $cT<2L$. Its complement contains an open arc. Choose two smooth bumps of opposite integrals inside that complement; their sum is a nonzero smooth mean-zero function $G$. Let $F'=G$ and take a periodic primitive. Equations [\[eq:dalembert\]](#eq:dalembert){reference-type="eqref" reference="eq:dalembert"}--[\[eq:coordinates\]](#eq:coordinates){reference-type="eqref" reference="eq:coordinates"} give a nonzero smooth energy solution whose endpoint trace vanishes on the whole observation window.

This is an infinite-dimensional obstruction. A finite Galerkin Gramian can be nonsingular on a shorter interval and cannot replace Theorem [\[thm:sharp\]](#thm:sharp){reference-type="ref" reference="thm:sharp"}.

# HUM duality and function spaces

For the controlled state, keep $y(0,t)=0$ and prescribe the Dirichlet value $y(L,t)=h(t)$. With $h\in L^2(0,T)$, solutions are understood by transposition in $$L^2(0,L)\times H^{-1}(0,L).$$ Green duality pairs the boundary control with $c^2u_x(L,t)$. Define the control-adjoint observation by $\mathcal O_T(u_0,u_1)=c^2u_x(L,\cdot)$. At $T=2L/c$, Theorem [\[thm:identity\]](#thm:identity){reference-type="ref" reference="thm:identity"} is the norm identity $\|\mathcal O_T(u_0,u_1)\|_{L^2(0,T)}^2=4cE(0)$: thus $\mathcal O_T$ is a scaled isometry onto its closed range, not a claimed surjection onto all of $L^2(0,T)$. The HUM Gramian $\mathcal O_T^*\mathcal O_T$ is therefore coercive and, after the energy-space Riesz identification, an isomorphism onto the dual state space. Time reversibility gives exact control between arbitrary states in this dual space for every $T\ge2L/c$; Theorem [\[thm:sharp\]](#thm:sharp){reference-type="ref" reference="thm:sharp"} proves failure below it.

HUM was introduced systematically by Lions [@Lions1988]. Sharp boundary geometric control for waves is owned by Bardos, Lebeau, and Rauch [@BLR1992]; in one dimension characteristics encode the ray condition. We claim the explicit convention-complete identity and executable boundary audit here, not priority for HUM or geometric control.

# Executable receipt and Route-A boundary

The retained receipt has 16 positive $(L,c)$ rows, 256 exact modal cells, 16 revival cells, and 16 strict subcritical arcs. A checker derived from the periodic coordinate reports 2,804 assertions; a separate symbolic route reports 86 identities; two isolated outputs are byte identical; and 23/23 repaired/stale-hash attacks fail. These cells audit [\[eq:identity\]](#eq:identity){reference-type="eqref" reference="eq:identity"}; they do not prove infinite-dimensional observability or HUM.

The wave group has nonisolated periodic families, not an arithmetic primitive ledger. The Dirichlet Laplacian gives a natural source quantization but no rational-prime carrier, prime-power amplitude, target determinant, or same-clock target bridge. Under `NO_BAD_EULER_OR_ROOT_NUMBER`, the tuple is $$\begin{gathered}
 \texttt{(A0\_FAIL,A1\_WEAK,A2\_FAIL,}\\[-2pt]
 \texttt{A3\_FAIL,A4\_NATURAL\_QUANTIZATION)},
 \end{gathered}$$ the overall verdict is `ROUTE_A_REJECTED`, and Route B is disabled.

2 J.-L. Lions, *Exact controllability, stabilization and perturbations for distributed systems*, SIAM Review **30**(1) (1988), 1--68, [doi:10.1137/1030001](https://doi.org/10.1137/1030001). C. Bardos, G. Lebeau, and J. Rauch, *Sharp sufficient conditions for the observation, control, and stabilization of waves from the boundary*, SIAM Journal on Control and Optimization **30**(5) (1992), 1024--1065, [doi:10.1137/0330055](https://doi.org/10.1137/0330055).
