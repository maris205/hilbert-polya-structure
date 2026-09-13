---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-adaptive-feedback-route-a"
canonical_tex: "henon_dynamics/henon_adaptive_feedback_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_adaptive_feedback_route_a/paper/main.pdf"
source_sha256: "c0106c9423934e25f61086dccc6b3131a5a11b320571484640e0bb1b88366786"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# An Adaptive-Feedback Hénon Automorphism: Exact Dissipation and a Primitive Two-Cycle

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_adaptive_feedback_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_adaptive_feedback_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_adaptive_feedback_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_adaptive_feedback_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We construct an exact three-dimensional Hénon-type map whose additive parameter is itself a contracting feedback variable. The map has a polynomial inverse and constant Jacobian determinant $1/2$. Two algebraic fixed points and one primitive period-two orbit are certified, together with its exact monodromy polynomial. Gain-zero and neighboring-gain controls show that the named orbit uses the adaptive channel. This is a finite low-period witness, not a transfer-operator or arithmetic construction.
author:
- 'Route-A finite certificate C122'
title: |
  An Adaptive-Feedback Hénon Automorphism:\
  Exact Dissipation and a Primitive Two-Cycle
```

## Markdown 正文

# Adaptive polynomial automorphism

Freeze $$G(x,y,a)=\left(x^2+a-y,\ x,\ \frac a2+3x-\frac12\right).$$ The third coordinate is an evolving parameter: it contracts and receives present-state feedback. Direct substitution gives the polynomial inverse $$G^{-1}(X,Y,A)=\left(Y,\,Y^2+2A-6Y+1-X,\,2A-6Y+1\right).$$ The Jacobian is $$J(x)=\begin{pmatrix}2x&-1&1\\1&0&0\\3&0&1/2\end{pmatrix},
 \qquad \det J(x)=\frac12.$$ Thus the model is invertible but volume contracting. These identities hold as polynomials, rather than on a finite sample alone.

# Exact orbit witnesses

A fixed point has $y=x$, $a=6x-1$, and $x^2+4x-1=0$. Hence the two certified fixed states are $$P_{\pm}=(-2\pm\sqrt5,-2\pm\sqrt5,-13\pm6\sqrt5).$$ More importantly, the two distinct rational states $$C_0=(1,-1,-3),\qquad C_1=(-1,1,1)$$ satisfy $G(C_0)=C_1$ and $G(C_1)=C_0$. They therefore form an oriented primitive period-two orbit. With chronological multiplication, its monodromy is $$M=J(-1)J(1)=
 \begin{pmatrix}
 -2&2&-3/2\\2&-1&1\\15/2&-3&13/4
 \end{pmatrix}.$$ Consequently $$\operatorname{tr}M=\frac14,\qquad \det M=\frac14,
 \qquad
 \det(I-zM)=1-\frac z4+\frac52z^2-\frac14z^3.$$ This last polynomial is local tangent data, not a Fredholm determinant.

# Feedback controls

Keep the two target states and parameter contraction $1/2$ fixed, but write the third update as $a/2+kx+d$. Closure at both states gives two linear equations whose unique solution is $$k=3,\qquad d=-\frac12.$$ At $k=0$ the first image has adaptive coordinate $-2$ rather than $1$, a residual $-3$. At the neighboring rational gain $k=5/2$, the residual is $-1/2$. The displayed cycle is therefore not inherited from an inert parameter coordinate.

The forward coordinate-degree prefix is $$(2,1,1),(4,2,2),(8,4,4),(16,8,8),(32,16,16),(64,32,32),$$ which is recorded only as a finite algebraic control.

# Validation and Route-A boundary

From the package directory run

    python3 code/c122_adaptive_producer.py
    python3 code/c122_adaptive_checker.py
    python3 code/c122_sympy_crosscheck.py
    python3 code/c122_replay.py
    python3 code/c122_mutation.py

The independent checker, 21 fresh symbolic identities, canonical replay, and all 16 hostile mutations pass in exact arithmetic; eight additional symbolic boundary checks make 29 checks in total.

The canonical verdict is $(\texttt{A1\_WEAK},\texttt{A2\_FAIL},\texttt{A3\_FAIL},
\texttt{A4\_FAIL})$, overall `ROUTE_A_EXPLORATORY`. The exact low-period witnesses have no prime-like target correspondence. The tangent polynomial has no target-divisor match or analytic bridge, and no global analytic structure is established. We claim no complete orbit atlas, global transfer/Fredholm/nuclear owner, arithmetic local data, Euler factors, root numbers, automorphy, Hilbert--Pólya operator, or Route B. The firewall is `NO_BAD_EULER_OR_ROOT_NUMBER`.
