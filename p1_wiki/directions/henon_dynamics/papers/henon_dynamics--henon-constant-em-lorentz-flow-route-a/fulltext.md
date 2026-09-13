---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-constant-em-lorentz-flow-route-a"
canonical_tex: "henon_dynamics/henon_constant_em_lorentz_flow_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_constant_em_lorentz_flow_route_a/paper/main.pdf"
source_sha256: "5972a1835c35f00063ced9d1eef632973bedaeda2548d1a2dc5a63862b85112e"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Invariant Planes, Exact Motion, and Null Degeneration of a Constant Electromagnetic Lorentz Flow

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_constant_em_lorentz_flow_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_constant_em_lorentz_flow_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_constant_em_lorentz_flow_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_constant_em_lorentz_flow_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We classify proper-time Lorentz motion in every constant electromagnetic field. The characteristic polynomial produces complementary boost and rotation planes, an exact exponential, and an exact position integral. \>0 We then classify velocity periods, prove physical worldline nonclosure, and resolve electric, magnetic, and secular faces. \>1 The vanishing-invariant nonzero null field is closed separately by cubic nilpotency, with executable sign and degeneration audits. Proper time is never replaced by coordinate time.
author:
- 'Route-A source-local certificate HCS-C268'
date: 31 August 2026
title: |
  Invariant Planes, Exact Motion, and Null Degeneration\
  of a Constant Electromagnetic Lorentz Flow
```

## Markdown 正文

trailerid \[\<C2682026083100000000000000000000\>\<C2682026083100000000000000000000\>\]

# Convention and invariant factorization

Use $\eta=\operatorname{diag}(1,-1,-1,-1)$ and $\kappa=q/m$. We freeze $$A=\kappa\begin{pmatrix}
0&E_x&E_y&E_z\\ E_x&0&B_z&-B_y\\ E_y&-B_z&0&B_x\\ E_z&B_y&-B_x&0
\end{pmatrix}.                                                   \tag{1}$$ Thus $A^T\eta+\eta A=0$, and for $u=(u^0,u^0\mathbf v)$ the spatial part of $u'=Au$ is $\mathbf u'=\kappa u^0(\mathbf E+\mathbf v\times\mathbf B)$. This fixes both electric and magnetic signs. The prime denotes proper time $\tau$, and $x'=u$. Exact constant-field Lorentz evolution has a long lineage; see Chin [@Chin]. We make no priority claim.

There are unique $a,b\ge0$ such that $$\begin{aligned}
 \chi_A(z)&=(z^2-a^2)(z^2+b^2),                              \tag{2}\\
 a^2-b^2&=\kappa^2(|\mathbf E|^2-|\mathbf B|^2),\qquad
 a^2b^2=\kappa^4(\mathbf E\!\cdot\!\mathbf B)^2.            \tag{3}\end{aligned}$$ If $D=a^2+b^2>0$, then $$P_h=\frac{A^2+b^2I}{D},\qquad P_r=\frac{-A^2+a^2I}{D}        \tag{4}$$ are complementary projectors, with $A^2P_h=a^2P_h$ and $A^2P_r=-b^2P_r$.

A direct determinant of (1) gives $z^4+\kappa^2(|\mathbf B|^2-|\mathbf E|^2)z^2
-\kappa^4(\mathbf E\cdot\mathbf B)^2$; solving its quadratic in $z^2$ gives (2)--(3). Cayley--Hamilton then verifies every identity in (4).

# Exact velocity and position

Write all quotients below by analytic continuation at $a=0$ or $b=0$.

For $D>0$, $$\begin{aligned}
 e^{\tau A}={}&P_h\left(\cosh(a\tau)I+\frac{\sinh(a\tau)}aA\right)
 +P_r\left(\cos(b\tau)I+\frac{\sin(b\tau)}bA\right),       \tag{5}\\
 \Phi(\tau)={}&P_h\left(\frac{\sinh(a\tau)}aI+
 \frac{\cosh(a\tau)-1}{a^2}A\right)\nonumber\\
 &+P_r\left(\frac{\sin(b\tau)}bI+
 \frac{1-\cos(b\tau)}{b^2}A\right).                       \tag{6}\end{aligned}$$ The solution is $u(\tau)=e^{\tau A}u_0$ and $x(\tau)=x_0+\Phi(\tau)u_0$. Moreover $\eta(u,u)=\eta(u_0,u_0)$ and $\det e^{\tau A}=1$.

Functional calculus on (4) gives (5), and direct integration gives (6). Since $A^T\eta+\eta A=0$, differentiation of $e^{\tau A^T}\eta e^{\tau A}$ gives zero. Finally $\det e^{\tau A}=e^{\tau\operatorname{tr}A}=1$.

\>0

# Period, nonclosure, and boundary atlas

On $P_h$ the flow has real exponents $\pm a$; on $P_r$ it rotates with frequency $b$. Hence a nonconstant $u(\tau)$ is periodic exactly when $$b>0,\quad P_ru_0\ne0,\quad\text{and}\quad(a=0\ \text{or}\ P_hu_0=0), \tag{7}$$ and its least period is $2\pi/b$. Notice the magnetic face: when $a=0<b$, $P_hu_0$ is constant and does not obstruct periodicity. When $a>0$, a nonzero hyperbolic component does. If $b=0$, no nonconstant velocity is periodic.

For a future-timelike physical initial velocity, the flow in (5) stays in the identity component of the Lorentz group. Thus $u^0(\tau)>0$, so $x^0(\tau)$ is strictly increasing. No physical worldline closes, even when its velocity is periodic. This is a proper-time statement; it is not a claim of periodicity in coordinate time.

If $a,b>0$, (5)--(6) split motion into hyperbolic and rotational planes. For $a>0=b$ (electric-like), the rotation plane becomes a kernel and (6) has a secular $\tau P_r$ term. For $a=0<b$ (magnetic-like), the boost plane becomes a kernel and produces $\tau P_h$, alongside the cyclotron rotation. At $A=0$, $u=u_0$ and $x=x_0+\tau u_0$.

\>1

# Nonzero null field

If $a=b=0$ but $A\ne0$, equivalently $|\mathbf E|=|\mathbf B|$ and $\mathbf E\cdot\mathbf B=0$ in this electromagnetic owner, direct multiplication gives $A^3=0$ (and $A^2\ne0$). Therefore no singular projector limit is needed: $$e^{\tau A}=I+\tau A+\frac{\tau^2}{2}A^2,\qquad
 \Phi(\tau)=\tau I+\frac{\tau^2}{2}A+\frac{\tau^3}{6}A^2.   \tag{8}$$ If $e^{TA}u_0=u_0$ for $T>0$, applying $A$ to the resulting equation first forces $A^2u_0=0$ and then $Au_0=0$. Thus a null field has no nonconstant periodic velocity.

# Certificate and Route-A boundary

The exact receipt covers twelve signed zero, electric, magnetic, parallel, crossed-null, and generic fields at 48 proper times, with 1,536 exponential and integral cells. An independent implementation closes 1,871 assertions using exact characteristic and minimal polynomials plus direct matrix exponentials and augmented-matrix integrals. SymPy closes 128 identities, byte replay is exact, and repaired-hash hostile testing rejects 24/24 changes. Finite matrices are regression receipts; the symbolic arguments above prove the all-parameter theorem.

Under `NO_BAD_EULER_OR_ROOT_NUMBER`, this owner supplies no target arithmetic local datum, Euler factor, root number, automorphy, divisor, functional equation, or Hilbert--Pólya operator. Its conservative tuple is $$\texttt{(A0\_FAIL,A1\_WEAK,A2\_FAIL,A3\_FAIL,A4\_FORMAL\_HINT)}.$$ The verdict is `ROUTE_A_REJECTED`; Route B is disabled.

9 S. A. Chin, *Relativistic Motion in a Constant Electromagnetic Field*, arXiv:0809.0859 \[math-ph\] (2008), [doi:10.1063/1.3064796](https://doi.org/10.1063/1.3064796).
