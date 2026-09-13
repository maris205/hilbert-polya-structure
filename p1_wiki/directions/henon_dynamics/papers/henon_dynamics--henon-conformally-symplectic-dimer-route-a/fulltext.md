---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-conformally-symplectic-dimer-route-a"
canonical_tex: "henon_dynamics/henon_conformally_symplectic_dimer_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_conformally_symplectic_dimer_route_a/paper/main.pdf"
source_sha256: "9f239e254af860cebd8e3fa3add98cb4b615ea2087ebf975c1f4a52e9102b45c"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Conformally Symplectic Damped Hénon Dimer: Exact Period-Two Mode Monodromy

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_conformally_symplectic_dimer_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_conformally_symplectic_dimer_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_conformally_symplectic_dimer_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_conformally_symplectic_dimer_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We construct an exact rational certificate for a damped two-site variational Hénon map. Its Jacobian is conformally symplectic with factor $1/2$ and determinant $1/4$. Two synchronous fixed points and one primitive synchronous period-two orbit are verified exactly. The two-step monodromy factors into longitudinal and transverse Laplacian modes with traces $-59/4$ and $-13$. An uncoupled control isolates a trace shift of $7/4$. The result is a finite low-period tangent witness, not a global transfer-operator theorem.
author:
- 'Route-A finite certificate C118'
title: |
  A Conformally Symplectic Damped Hénon Dimer:\
  Exact Period-Two Mode Monodromy
```

## Markdown 正文

# Damped variational model

For $q,p\in\mathbb Q^2$, let $$U(q)=\sum_{i=1}^2\left(\frac{13}{4}q_i^2-\frac13q_i^3\right)
 -\frac18(q_1-q_2)^2,
 \qquad F(q,p)=(\nabla U(q)-\tfrac12p,q).$$ Writing $$L=\begin{pmatrix}1&-1\\-1&1\end{pmatrix},\quad
 H(q)=\operatorname{diag}(13/2-2q_i)-\tfrac14L,$$ the Jacobian and its exact inverse are $$J(q)=\begin{pmatrix}H(q)&-I_2/2\\I_2&0\end{pmatrix},\qquad
 F^{-1}(Q,P)=(P,2(\nabla U(P)-Q)).$$ For $\Omega=\left(\begin{smallmatrix}0&I_2\\-I_2&0\end{smallmatrix}\right)$, direct multiplication gives $$J(q)^\mathsf T\Omega J(q)=\tfrac12\Omega,\qquad \det J(q)=\tfrac14.$$ There is also an exact primitive relation. With $\lambda=q\cdot dp$, $$F^*\lambda-\tfrac12\lambda
 =d\bigl(U(q)-\tfrac12p\cdot q\bigr).$$ These are polynomial identities, not numerical sample fits.

# Exact synchronous orbit witnesses

Synchrony is invariant because $L(1,1)^\mathsf T=0$. The fixed states are $$P_0=((0,0),(0,0)),\qquad P_5=((5,5),(5,5)).$$ The two distinct states $$C_2=((2,2),(6,6)),\qquad C_6=((6,6),(2,2))$$ satisfy $F(C_2)=C_6$ and $F(C_6)=C_2$, giving a primitive period-two witness. The direct four-dimensional two-step monodromy is $$M=\begin{pmatrix}
 -107/8&-7/8&23/8&-1/8\\
 -7/8&-107/8&-1/8&23/8\\
 9/4&1/4&-1/2&0\\1/4&9/4&0&-1/2
 \end{pmatrix},$$ with trace $-111/4$ and determinant $1/16$.

# Longitudinal and transverse factors

The Laplacian eigenvalues are $0$ and $2$. At synchronous coordinate $s$, the scalar Hessian value in mode $\ell$ is $$h_s(\ell)=13/2-2s-\ell/4.$$ Thus the mode pairs at $s=2,6$ are $(5/2,-11/2)$ and $(2,-6)$. A one-step mode matrix is $J_h=\left(\begin{smallmatrix}h&-1/2\\1&0\end{smallmatrix}\right)$. The exact two-step data are

  mode             $(h_2,h_6)$    $\operatorname{tr}(J_{h_6}J_{h_2})$   determinant
  -------------- --------------- ------------------------------------- -------------
  longitudinal    $(5/2,-11/2)$                 $-59/4$                    $1/4$
  transverse        $(2,-6)$                     $-13$                     $1/4$

Consequently the direct and mode reconstructions agree: $$\begin{aligned}
 \det(I-zM)&=(1+59z/4+z^2/4)(1+13z+z^2/4)\\
 &=1+\tfrac{111}{4}z+\tfrac{769}{4}z^2
   +\tfrac{111}{16}z^3+\tfrac1{16}z^4.\end{aligned}$$ At $\kappa=0$, the synchronous orbit remains valid but both modes are longitudinal: the full trace is $-59/2$. Coupling therefore shifts the direct trace by $7/4$ in this controlled tangent comparison.

# Reproducibility and scope

From the package directory run

    python3 code/c118_damped_dimer_producer.py
    python3 code/c118_damped_dimer_checker.py
    python3 code/c118_sympy_crosscheck.py
    python3 code/c118_replay.py
    python3 code/c118_mutation.py

The independent checker, 13 symbolic checks, canonical replay, and all 12 hostile mutations pass.

The verdict is $A1=\texttt{A1\_WEAK}$: only named fixed and period-two witnesses are certified. $A2=\texttt{A2\_FAIL}$ because tangent monodromy is not a source-owned transfer operator; $A3$ is not addressed and $A4$ fails. We claim no complete orbit atlas, transfer/Fredholm/nuclear owner, arithmetic local data, Euler factors, root numbers, automorphy, Hilbert--Pólya operator, or Route B. The firewall is `NO_BAD_EULER_OR_ROOT_NUMBER`.
