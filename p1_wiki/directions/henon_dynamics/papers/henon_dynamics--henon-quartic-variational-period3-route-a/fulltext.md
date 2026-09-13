---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-quartic-variational-period3-route-a"
canonical_tex: "henon_dynamics/henon_quartic_variational_period3_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_quartic_variational_period3_route_a/paper/main.pdf"
source_sha256: "c219462025aac0a6ffd4661b8535d28129b18a9fc3c1ff9aaece29dc8d34fe3f"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# An Exact Quartic Variational Period-Three Certificate

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_quartic_variational_period3_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_quartic_variational_period3_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_quartic_variational_period3_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_quartic_variational_period3_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We give an exact rational certificate for a primitive period-three orbit of an area-preserving quartic variational map. The coordinate-swap reversor and type-one generating function are verified symbolically. Chronological monodromy is a nontrivial Jordan matrix at multiplier $-1$, while the cyclic action has value $1/2$ and a nondegenerate index-two Hessian. Three negative controls localize the result to the frozen parameter, cubic term, and cyclic word. This is finite low-period evidence, not a global orbit, transfer, or spectral theorem.
author:
- 'Route-A finite certificate C120'
title: 'An Exact Quartic Variational Period-Three Certificate'
```

## Markdown 正文

# Reversible variational map

Let $$V(q)=\frac{q^4}{4}-q^2,\qquad
 F(q,p)=(V'(q)-p,q)=(q^3-2q-p,q).$$ The Jacobian, inverse, and coordinate-swap reversor $R$ are $$B(q)=\begin{pmatrix}3q^2-2&-1\\1&0\end{pmatrix},\quad
 F^{-1}(Q,P)=(P,P^3-2P-Q),\quad R(q,p)=(p,q).$$ Direct polynomial multiplication gives $\det B(q)=1$ and $RFR=F^{-1}$; both compositions with the displayed inverse are the identity. The type-one generating function $$S(q,Q)=qQ-V(q)$$ recovers $F$ under the explicit convention $p=-\partial_qS$ and $P=\partial_QS$: namely $Q=V'(q)-p$ and $P=q$. This sign convention is part of the frozen source rather than an inferred numerical fit.

The fixed equation is $q^3-3q=q$, hence $$q(q-2)(q+2)=0,$$ and the phase-space fixed points are $(0,0),(2,2),(-2,-2)$.

# Primitive three-cycle and tangent data

The three distinct states $$x_0=(0,-1),\qquad x_1=(1,0),\qquad x_2=(-1,1)$$ satisfy $F(x_0)=x_1$, $F(x_1)=x_2$, and $F(x_2)=x_0$. They therefore form a primitive period-three orbit. The chronological derivative is $$M=B(-1)B(1)B(0)
 =\begin{pmatrix}-1&0\\-3&-1\end{pmatrix}.$$ Consequently $$\operatorname{tr}M=-2,\qquad \det M=1,\qquad
 \det(I-zM)=1+2z+z^2=(1+z)^2.$$ Thus the named cycle has a repeated multiplier $-1$ and a nontrivial Jordan part. These statements concern one finite monodromy matrix only.

# Action and Morse certificate

Write the orbit states as $(q_i,q_{i-1})$ with cyclic indices and define $$\mathcal A(q_0,q_1,q_2)=\sum_{i=0}^{2}
 \bigl(q_iq_{i+1}-V(q_i)\bigr).$$ Its stationarity equations are $q_{i-1}+q_{i+1}-V'(q_i)=0$, exactly the orbit recurrence. At $q_*=(0,1,-1)$, direct evaluation gives $$\mathcal A(q_*)=0-\frac14+\frac34=\frac12,\qquad
 \nabla\mathcal A(q_*)=0,$$ and $$H=D^2\mathcal A(q_*)=
 \begin{pmatrix}2&1&1\\1&-1&1\\1&1&-1\end{pmatrix}.$$ The exact Hessian data are $$\det H=4,\qquad
 \det(\lambda I-H)=(\lambda+2)(\lambda^2-2\lambda-2).$$ Its eigenvalues are $-2,1-\sqrt3,1+\sqrt3$. Hence the critical point is nondegenerate and has Morse index two. The nondegenerate action Hessian and the parabolic phase-space monodromy are distinct, compatible finite certificates; neither is promoted to a global classification.

# Controls, reproducibility, and scope

Three exact controls test attribution:

  control             tested transition      actual-minus-target residual
  ------------------- ---------------------- ------------------------------
  $q^3-\tfrac52q-p$   $(1,0)\mapsto(-1,1)$   $(-1/2,0)$
  delete $q^3$        $(1,0)\mapsto(-1,1)$   $(-1,0)$
  word $(0,1,0)$      second transition      $(-1,0)$

Each residual is nonzero, so the frozen certificate is neither parameter- agnostic nor a property of an arbitrary length-three word.

From the package directory run

    python3 code/c120_variational_period3_producer.py
    python3 code/c120_variational_period3_checker.py
    python3 code/c120_sympy_crosscheck.py
    python3 code/c120_replay.py
    python3 code/c120_mutation.py

The independent checker, 29 direct symbolic checks, canonical replay, and all 21 hostile mutations pass.

The evaluator-native verdicts are $$\begin{aligned}
 A1&=\texttt{A1\_WEAK}, & A2&=\texttt{A2\_FAIL},\\
 A3&=\texttt{A3\_FAIL}, & A4&=\texttt{A4\_FORMAL\_HINT}.
 \end{aligned}$$ The overall status is `ROUTE_A_EXPLORATORY`. The exact cycle and Morse data are finite structural evidence, but there is no target prime correspondence or complete enumeration, no source-owned dynamical zeta/Fredholm object, and no target divisor or global analytic structure. The generating structure is only a formal liftability hint: no quantum object, Hilbert space, or operator domain is defined. We claim no arithmetic local data, Euler factors, root numbers, automorphy, Hilbert--Pólya operator, or Route B. The firewall is `NO_BAD_EULER_OR_ROOT_NUMBER`.
