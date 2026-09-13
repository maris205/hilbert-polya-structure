---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-sir-final-size-phase-portrait-route-a"
canonical_tex: "henon_dynamics/henon_sir_final_size_phase_portrait_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_sir_final_size_phase_portrait_route_a/paper/main.pdf"
source_sha256: "19f88a4feaf4229cf144b920fa3d3e86329cdec2d9efdbc63b625ff4c9458e81"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The Closed SIR Flow for All Positive Parameters: Phase Curves, Final-Size Branches, and the No-Recurrence Boundary

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_sir_final_size_phase_portrait_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_sir_final_size_phase_portrait_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_sir_final_size_phase_portrait_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_sir_final_size_phase_portrait_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We give one complete dynamical atlas for the closed mass-action SIR system at all positive transmission and removal rates. Exact scaling reduces the family to one planar flow; its first integral yields the phase curves, infection peak, time quadrature, final-size sensitivity and the correctly selected Lambert branch. A monotone removed coordinate proves global convergence and excludes every nonconstant recurrent orbit. A Lambert-free high-precision checker independently reconstructs both real final-size intersections. The result is an idealized mathematical certificate, with no clinical data or medical advice. Its monotonicity and absence of intrinsic prime arithmetic force strict Route-A rejection.
author:
- 'Route-A structural certificate C198'
title: |
  The Closed SIR Flow for All Positive Parameters:\
  Phase Curves, Final-Size Branches, and the No-Recurrence Boundary
```

## Markdown 正文

suppressoptionalinfo 611

**Keywords:** SIR model; phase portrait; final size; Lambert W; threshold; monotone dynamics; Route-A obstruction.

chinese-simplified

中文摘要

本文对全部正传播率与移除率的封闭质量作用[SIR]{lang="en"}系统给出统一动力学图谱。 精确无量纲化把全参数族化为一个平面流；第一积分同时确定相曲线、感染峰值、时间积分、 最终规模灵敏度及正确的[Lambert W]{lang="en"}分支。移除变量严格单调，因而全局收敛并 排除全部非常值回归轨道。本文只研究理想化数学模型，不使用临床数据，也不提供医疗建议。

关键词：[SIR]{lang="en"}模型；相图；最终规模；阈值；单调动力学。

# One phase portrait for all parameters

Fix $\beta,\gamma>0$ and physical time $t$ in $$\dot S=-\beta SI,\qquad \dot I=\beta SI-\gamma I,
 \qquad \dot R=\gamma I .$$ The model and its threshold/final-size analysis descend from Kermack and McKendrick [@KM27]; Lambert-branch analysis is treated explicitly by Pakes [@P15]. Put $$\kappa=\gamma/\beta,\qquad x=S/\kappa,\quad y=I/\kappa,
 \quad z=R/\kappa,\quad \tau=\gamma t.$$ Every parameter pair is thereby conjugate, without changing physical-time orientation, to $$\label{eq:flow}
 x'=-xy,\qquad y'=y(x-1),\qquad z'=y.$$ The nonnegative fixed-population simplex is invariant and compact, so solutions are global. Direct differentiation gives $$\label{eq:first}
 H(x,y)=x+y-\log x=H(x_0,y_0),\qquad
 y=y_0+x_0-x+\log(x/x_0).$$

For $y_0>0$, $x$ decreases strictly. If $x_0>1$, then $y$ grows until the unique crossing $x=1$ and $$y_{\max}=y_0+x_0-1-\log x_0.$$ If $x_0<1$, $y$ decreases from the start; at $x_0=1$ its first derivative is zero, after which decreasing $x$ makes it negative. Thus the threshold and peak are globally, not locally, classified.

\>0

# Global limit, branch, and stability

Since $z'=y\ge0$ and population is bounded, $\int_0^\infty y\,d\tau<\infty$; bounded derivatives give $y(\tau)\to0$. Also $x(\tau)=x_0\exp(-\int_0^\tau y\,ds)>0$. Hence every $y_0>0$ trajectory has $0<x_\infty<\min(x_0,1)$ and [\[eq:first\]](#eq:first){reference-type="eqref" reference="eq:first"} gives $$\label{eq:final}
 x_\infty e^{-x_\infty}=x_0e^{-x_0-y_0},\qquad
 x_\infty=-W_0(-x_0e^{-x_0-y_0}).$$ The function $x-\log x$ decreases on $(0,1)$ and increases on $(1,\infty)$. Thus $-W_{-1}$ is the other, upper intersection of the invariant curve; it is not the forward limit. The exact time representation is $$\tau=\int_{x(\tau)}^{x_0}
 \frac{du}{u\{y_0+x_0-u+\log(u/x_0)\}}.$$ Implicit differentiation of [\[eq:final\]](#eq:final){reference-type="eqref" reference="eq:final"} yields $\partial x_\infty/\partial y_0=x_\infty/(x_\infty-1)<0$.

If $y_0=0$, the initial point is already an equilibrium and remains fixed. In particular, when $x_0>1$ its final value is the upper root $x_0$, not the positive-infection $W_0$ branch. On each population simplex the equilibrium line has tangential eigenvalue zero and transverse physical eigenvalue $\beta S_\ast-\gamma$. Finally, $R$ is strictly increasing wherever $I>0$; there is no nonconstant periodic or recurrent orbit, and every trajectory converges to the disease-free line.

\>1

# Independent certificate and Route-A stop

The exact release uses 24 positive-infection phase curves: nine subcritical, three threshold and twelve supercritical starts, plus four physical scalings. The producer evaluates 48 real Lambert-branch values. The independent checker calls no Lambert routine: 100-digit Decimal logarithms and monotone bisection recover both intersections. A separate symbolic path proves seven structural identities and tests every branch equation. Replay is byte exact; twelve repaired-hash attacks and one stale-hash attack are rejected. This ledger tests conventions and does not replace the all-parameter proof.

The flow has no nonconstant primitive-periodic-orbit layer, rational-prime carrier, prime-power repetition or $\log p$ clock. Its terminal Lambert equation is not a dynamical Zeta or target Fredholm determinant, and the dissipative flow has no source-native same-clock unitary lift. Therefore $$(A0,A1,A2,A3,A4)=(\mathrm{FAIL},\mathrm{FAIL},\mathrm{FAIL},
 \mathrm{FAIL},\mathrm{FAIL}),$$ overall `ROUTE_A_REJECTED`, Route B false, under `NO_BAD_EULER_OR_ROOT_NUMBER`.

#### Safety and scope firewall.

This idealized model supplies no prediction, calibration, intervention advice or claim about a real outbreak. We claim no classical priority, elementary explicit formula for all components versus time, target zero/prime data, arithmetic local datum, Euler factor, root number, automorphy, target analytic structure, Hilbert--Pólya operator, external review or acceptance score.

#### Revision focus.

Round 0 freezes the physical model and proves the all-parameter scaling, first integral and complete peak atlas.

#### Revision focus.

Round 1 adds global convergence, both Lambert branches, quadrature, sensitivity, equilibrium stability and no recurrence.

#### Revision focus.

Round 2 adds the zero-infection boundary, independent branch validation, source ownership, safety and Route-A firewalls.

# Declarations {#declarations .unnumbered}

#### Data and code availability.

Package-local synthetic exact evidence and deterministic code accompany this manuscript; no clinical data are used.

#### Ethics.

No human, animal, clinical, personal or sensitive data are used; approval is not applicable.

#### Author contributions (CRediT).

This anonymous certificate records Conceptualization, Formal analysis, Software, Validation, Writing---original draft, and Writing---review and editing. AI systems are not authors.

#### Funding.

No external funding is reported.

#### Conflicts of interest.

None known.

#### AI-use disclosure.

An AI coding assistant supported drafting and exact-code development; it was not an external reviewer or independent error process.

2 W. O. Kermack and A. G. McKendrick, "A contribution to the mathematical theory of epidemics," *Proc. R. Soc. A* 115 (1927), 700--721. DOI: 10.1098/rspa.1927.0118. A. G. Pakes, "Lambert's W meets Kermack--McKendrick epidemics," *IMA J. Appl. Math.* 80 (2015), 1368--1386. DOI: 10.1093/imamat/hxu057.
