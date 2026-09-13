---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-hysteretic-relay-oscillator-route-a"
canonical_tex: "henon_dynamics/henon_hysteretic_relay_oscillator_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_hysteretic_relay_oscillator_route_a/paper/main.pdf"
source_sha256: "5e6a365e3fd0cd5c6b84639d5b06e0d36777aeb0d690f55e5f35ebc5b3e81510"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# An Exact Event Atlas for a Two-Threshold Hysteretic Relay Oscillator

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_hysteretic_relay_oscillator_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_hysteretic_relay_oscillator_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_hysteretic_relay_oscillator_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_hysteretic_relay_oscillator_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We give a complete, guard-specific analysis of a two-threshold relay phase oscillator with a transverse linear cocycle. The phase legs, Poincare map, periodic set, grazing convention, and no-Zeno bound are all exact for every $h>0$ and $\gamma\geq0$. Eight rational receipts are independently checked, symbolically replayed, and hostile-tested. This is a source-local hybrid theorem: no arithmetic origin, Euler factor, root number, or Hilbert--Polya operator is claimed.
author:
- 'Route-A source-local certificate HCS-C252'
date: 30 August 2026
title: 'An Exact Event Atlas for a Two-Threshold Hysteretic Relay Oscillator'
```

## Markdown 正文

trailerid \[\<C2522026083000000000000000000000\>\<C2522026083000000000000000000000\>\]

# Frozen hybrid model

The state is $(\theta,y,\sigma)$ with $-h\leq\theta\leq h$, $y\in\mathbb R$, and $\sigma\in\{-1,+1\}$. In the interior, $$\dot\theta=\sigma,\qquad \dot y=-\gamma y,\qquad h>0,\ \gamma\geq0.
 \tag{1}$$ The guard has priority at equality: $\theta=h$ with $\sigma=+1$ is reset to $\sigma=-1$, and $\theta=-h$ with $\sigma=-1$ is reset to $\sigma=+1$. There is no sliding state in this frozen convention. The return section is $\Sigma_-=\{(\theta,y,\sigma)=(-h,y,+1)\}$.

# Event theorem

Every consistent interior or boundary state has a unique forward execution. A leg from one threshold to the other has duration $2h$ and maps $y\mapsto e^{-2\gamma h}y$. Therefore the Poincare map on $\Sigma_-$ is $$P(y)=e^{-4\gamma h}y, \qquad T_{\rm phase}=4h. \tag{2}$$ For $\gamma>0$, the unique periodic state in the transverse coordinate is $y=0$; for $\gamma=0$, every $y$ is periodic. Every interior point reaches a switching section in at most $2h$, and all successive event gaps equal $2h$.

On each mode, $\theta(t)=\theta_0+\sigma t$ reaches the opposite threshold in time $2h$; the equality rule chooses the only outgoing mode. Solving the scalar equation in (1) gives $y(t)=y_0e^{-\gamma t}$, so composition gives (2). Since $h>0$, the event gaps have a uniform positive lower bound, which rules out finite-time Zeno accumulation. The fixed-point equation for (2) gives the stated periodic set.

# Boundary and stability atlas

The multiplier of the full return is $m=e^{-4\gamma h}$. Thus $0<m<1$ for $\gamma>0$, while $m=1$ on the neutral face $\gamma=0$. The zero section $y=0$ is an invariant periodic phase orbit and is called the grazing label only to identify the transverse fixed set; it does not create a sliding segment. This convention separates geometric phase from the transverse cocycle, so the return multiplier is not a phase frequency. At $h=0$ the event lower bound disappears, so the face is excluded rather than regularized. An inconsistent boundary mode is corrected instantaneously by the guard before flow starts.

  regime                      rows   certified quantities
  --------------------------- ------ --------------------------------------
  contracting $\gamma>0$      5      leg map, return, multiplier, period
  neutral $\gamma=0$          1      continuum of fixed transverse levels
  zero transverse amplitude   1      invariant periodic phase
  grazing-labelled boundary   1      guard policy and no sliding

  : Exact receipt coverage (all inputs are rational).

# Executable certificate

The producer emits eight rows and two leg records per row. The producer- independent checker closes 189 assertions; a separate SymPy program closes ten flow, composition, guard, and semigroup identities. Two fresh producer runs are byte identical and the hostile suite rejects 21/21 altered payloads. Decimal exponentials are only serialized evaluations of the exact semigroup. The three manuscript rounds use fixed `SOURCE_DATE_EPOCH=1788048000`, embedded fonts, text extraction, and a content-addressed manifest. The exact guard ledger is checked before serialization, which preserves the strict separation between a hybrid receipt and any spectral claim.

# Route-A boundary

The strict evaluator tuple is `(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`. The arithmetic origin is `none`; no primitive target orbit, determinant, or target data are defined. The verdict is `ROUTE_A_REJECTED`, with `route_b_invocation_allowed: false`, under the scope literal `NO_BAD_EULER_OR_ROOT_NUMBER`. This event map is a hybrid mechanical receipt, not a target spectral determinant.

# Conclusion

A precise hysteresis convention turns a relay intuition into an auditable global event theorem. The exact return multiplier and the uniform event gap separate transverse stability from geometric period and make the stopping boundary transparent. No arithmetic bridge is inferred.

9 D. Liberzon, *Switching in Systems and Control*, Birkhäuser, 2003. A. F. Filippov, *Differential Equations with Discontinuous Righthand Sides*, Kluwer, 1988. M. di Bernardo et al., *Piecewise-smooth Dynamical Systems*, Springer, 2008.
