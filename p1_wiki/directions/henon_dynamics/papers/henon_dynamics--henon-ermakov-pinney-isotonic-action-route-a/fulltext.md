---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-ermakov-pinney-isotonic-action-route-a"
canonical_tex: "henon_dynamics/henon_ermakov_pinney_isotonic_action_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_ermakov_pinney_isotonic_action_route_a/paper/main.pdf"
source_sha256: "524418750ffa50d33cfbc4841fcdbc6dd58a0a637fd807864850047b1dd157ac"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Quadratic Gram Lift for the Positive Ermakov--Pinney Oscillator

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_ermakov_pinney_isotonic_action_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_ermakov_pinney_isotonic_action_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_ermakov_pinney_isotonic_action_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_ermakov_pinney_isotonic_action_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We close an all-parameter, positive-component atlas for the singular oscillator $\ddot x+\omega^2x=\kappa x^{-3}$. A quadratic Gram representation in a pair of linear oscillator solutions gives the nonlinear trajectory, while the squared coordinate obeys a forced harmonic equation. This yields exact turning radii, the primitive period $\pi/\omega$, the isotonic action, and an Ermakov invariant, including explicit equilibrium and collision faces. Nine exact rational receipts are independently reconstructed, symbolically checked, replayed, and mutation tested. The result is source-local mechanics: arithmetic origin is absent and no zeta, Euler factor, root number, or Hilbert--Polya operator is claimed. The distinction between a mechanical action and a spectral determinant is maintained throughout the certificate.
author:
- 'Route-A source-local certificate HCS-C250'
date: 30 August 2026
title: 'A Quadratic Gram Lift for the Positive Ermakov--Pinney Oscillator'
```

## Markdown 正文

trailerid \[\<C2502026083000000000000000000000\>\<C2502026083000000000000000000000\>\]

# Scope and model

We work on $\mathcal P=\{(x,v):x>0,v\in\mathbb R\}$ with canonical form $dx\wedge dv$, parameters $\omega>0$ and $\kappa\geq0$, and physical time. The energy is $$E=\frac12\left(v^2+\omega^2x^2+\frac{\kappa}{x^2}\right).
 \label{eq:E}$$ The inverse-square face is kept in the model, but a trajectory is not continued through $x=0$ when $\kappa=0$. This convention is part of the theorem rather than a numerical regularization.

# The Gram/superposition theorem

Let $u(t)=\cos(\omega t)$ and $z(t)=\sin(\omega t)/\omega$. Their Wronskian is $u\dot z-\dot u z=1$. For initial data $x_0>0,v_0\in\mathbb R$, set $$a=x_0^2,\qquad b=x_0v_0,\qquad c=v_0^2+\kappa/x_0^2.
 \label{eq:abc}$$

The unique positive solution is $$x(t)^2=a u(t)^2+2b u(t)z(t)+c z(t)^2,\qquad ac-b^2=\kappa.
 \label{eq:gram}$$ For $\kappa>0$ the right side is strictly positive for every $t\in\mathbb R$. Writing $r=x^2$, one has $$r''+4\omega^2r=4E,
 \label{eq:radial}
 r_\pm=\frac{E\pm\sqrt{E^2-\omega^2\kappa}}{\omega^2}.$$ If $E>\omega\sqrt\kappa$, the primitive period is $T=\pi/\omega$; equality is the constant equilibrium $x=\kappa^{1/4}/\sqrt\omega$. The positive-component action is $J=E/(2\omega)-\sqrt\kappa/2$.

The determinant identity in [\[eq:gram\]](#eq:gram){reference-type="eqref" reference="eq:gram"} follows directly from [\[eq:abc\]](#eq:abc){reference-type="eqref" reference="eq:abc"}. Thus the quadratic form is positive definite for $\kappa>0$, and differentiating its square root, using $u''+\omega^2u=z''+\omega^2z=0$ and the unit Wronskian, gives $x''+\omega^2x=\kappa/x^3$. Conversely, the initial values select [\[eq:abc\]](#eq:abc){reference-type="eqref" reference="eq:abc"}, so uniqueness for the smooth vector field applies. Direct differentiation gives [\[eq:radial\]](#eq:radial){reference-type="eqref" reference="eq:radial"}. Its sinusoidal solution has mean $E/\omega^2$ and amplitude $\sqrt{E^2-\omega^2\kappa}/\omega^2$, proving the turning formula and the period. The action follows by integrating $p\,dx$ between the two turning radii (or, equivalently, by the standard radial action substitution); it is zero exactly at the double-root equilibrium.

# Invariant and boundary faces

For either normalized solution $q$ of $q''+\omega^2q=0$, define $$I_q=\frac12\left[(q\dot x-\dot q x)^2+\kappa(q/x)^2\right].
 \label{eq:inv}$$ Substitution of the equation of motion gives $\dot I_q=0$. The lower energy bound $E\geq\omega\sqrt\kappa$ is immediate from $\omega^2x^2+\kappa/x^2\geq2\omega\sqrt\kappa$. On the $\kappa=0$ face, the formula remains valid on each positive arc and the zero of the linear oscillator is a declared collision boundary. The faces $\omega=0$ and $\kappa<0$ are outside the frozen family; no hidden continuation is assigned.

  rows   regimes                             checked quantities
  ------ ----------------------------------- ---------------------------------------
  6      $\kappa>0$, $E>\omega\sqrt\kappa$   $(a,b,c),E,D,x(t),v(t),I_q,T,J$
  1      $\kappa=0$ collision face           Gram identity and positive-arc policy
  2      equilibrium ($D=0$)                 double turning root and zero action
  4      explicit boundary policies          excluded-face conventions

  : Receipt coverage. Inputs are exact rationals; displayed values are 90-digit working evaluations serialized to 64 digits.

# Executable evidence

The JSON receipt is generated by `code/c250_ep_producer.py`. The independent checker reconstructs all nine rows without importing the producer and closes 215 assertions. A separate SymPy program proves ten identities (linear pair, Wronskian, radial equation, energy, discriminant, and invariant). Two fresh producer runs are byte identical; the hostile suite rejects 26/26 altered payloads. The manuscript is compiled in three fixed-epoch rounds with embedded fonts and a content-addressed release manifest. The radial discriminant is evaluated exactly before decimal serialization, so the equilibrium and collision policies cannot be artifacts of rounding.

# Route-A boundary

The strict evaluator tuple is

`(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`

The arithmetic origin is `none`; there is no primitive target orbit, determinant convention, or target data. Hence the overall verdict is `ROUTE_A_REJECTED`; Route B is disabled (`route_b_invocation_allowed: false`). The scope literal is `NO_BAD_EULER_OR_ROOT_NUMBER`. In particular, the action $J$ is a mechanical action, not a target spectral determinant.

# Conclusion

The Gram lift turns the singular nonlinear oscillator into a globally auditable positive flow and makes its period/action boundary exact. The collision policy and the A0 stopping boundary are as important as the closed formula: they keep the theorem reproducible without overclaiming an arithmetic bridge.

9 V. P. Ermakov, "Second-order differential equations," University of Kiev (1880). E. Pinney, "The nonlinear differential equation $y''+p(x)y=cy^{-3}$," Proc. Amer. Math. Soc. 1 (1950), 681. J. F. Cariñena, M. F. Rañada, and M. Santander, "Central potentials and nonlinear superposition rules," J. Math. Phys. 46 (2005).
