---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-variational-coupled-henon-lattice"
canonical_tex: "henon_dynamics/henon_variational_coupled_henon_lattice/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_variational_coupled_henon_lattice/paper/main.pdf"
source_sha256: "280325a01b05b91162be5e143f82b1887369098cf7fc71251ef24771516fbe57"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# C106: An Exact Coupling Witness in a Variational Two-Site Hénon Lattice

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_variational_coupled_henon_lattice>)
- [规范 TeX](<../../../../../henon_dynamics/henon_variational_coupled_henon_lattice/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_variational_coupled_henon_lattice/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_variational_coupled_henon_lattice/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We record an exact, deliberately small audit of a two-site variational Hénon map. The map is reversible and symplectic by construction. At rational parameters we certify two fixed points and one genuine synchronous period-two orbit using rational arithmetic, and compare its finite monodromy polynomial with the uncoupled control. Coupling changes both the trace and the quadratic coefficient. This is an A1 low-period witness only: no completeness theorem, transfer-operator owner, or Fredholm determinant is claimed.
author:
- 'Route-A exploratory research note'
date: 22 August 2026
title: 'C106: An Exact Coupling Witness in a Variational Two-Site Hénon Lattice'
```

## Markdown 正文

# Model and scope

Let $q=(x,y)$ and $p=(u,v)$, and define $$U(q)=\frac a2(x^2+y^2)-\frac{x^3+y^3}{3}-\frac{\kappa}{2}(x-y)^2,
 \qquad F(q,p)=(\nabla U(q)-p,q),
 \label{eq:model}$$ with $(a,\kappa)=(7,1/4)$. In the coordinate order $(q_1,q_2,p_1,p_2)$ use $\Omega=\left(\begin{smallmatrix}0&I\\-I&0\end{smallmatrix}\right)$ and $R(q,p)=(p,q)$. The exact producer and independent checker are included in the accompanying artifact.

For every twice differentiable $U$, $$DF=\begin{pmatrix}D^2U&-I\\I&0\end{pmatrix},\qquad
 DF^T\Omega DF=\Omega,\qquad \det DF=1,$$ and direct substitution gives $RFR=F^{-1}$. With $\lambda=q\cdot dp$, one also has the exact primitive identity $F^*\lambda-\lambda=d(U(q)-p\cdot q)$. These identities are checked over $\mathbb{Q}$ at all reported orbit points and at three independent rational samples.

# Certified low-period data

The fixed points $(0,0;0,0)$ and $(5,5;5,5)$ satisfy $\nabla U(q)=2q$. A non-fixed period-two orbit is $$z_0=(3,3;6,6),\qquad z_1=(6,6;3,3),\qquad F(z_0)=z_1,\quad F(z_1)=z_0.$$ For $M=DF(z_1)DF(z_0)$, exact arithmetic gives the following table.

  object                 period   $\operatorname{tr}M$                        $\det(I-zM)$
  --------------------- -------- ---------------------- --------------------------------------------------------
  origin                   1             $27/2$          $1-\frac{27}{2}z+\frac{95}{2}z^2-\frac{27}{2}z^3+z^4$
  synchronous fixed        1            $-13/2$          $1+\frac{13}{2}z+\frac{25}{2}z^2+\frac{13}{2}z^3+z^4$
  synchronous 2-cycle      2            $-47/4$          $1+\frac{47}{4}z+\frac{141}{4}z^2+\frac{47}{4}z^3+z^4$

The two-cycle has determinant one. With the same $a$ and the same synchronous states but $\kappa=0$, the last polynomial becomes $$1+14z+51z^2+14z^3+z^4.$$ Thus the coupled-minus-uncoupled trace difference is $9/4$, while the $z^2$ coefficient difference is $-63/4$. This is a finite-dimensional product-versus-coupled control; it is not a Fredholm determinant.

# Route-A boundary

The ledger certifies only the displayed low-period witnesses. It does not establish a complete primitive-orbit enumeration, a Markov partition, a common anisotropic function space, nuclearity, a trace formula, or a zero-counting theorem. Accordingly the package records $$(A1,A2,A3,A4)=\bigl(\text{partial low-period},\ \text{operator owner open},\ \text{not addressed},\ \text{fail}\bigr),$$ with overall status `ROUTE_A_EXPLORATORY`. In the formal evaluator vocabulary this is `A1_WEAK` and `A2_FAIL`, with the qualification that the displayed finite operator owner remains open. In particular, no arithmetic local data, Euler factors, root numbers, automorphy, or Hilbert--Pólya operator is asserted.

# Reproducibility

The JSON evidence is canonicalized and checked byte-for-byte. A separate checker reconstructs the gradients, Jacobians, symplectic form, reversor, monodromy, and uncoupled control. A SymPy script supplies an independent symbolic check; replay and eleven hostile semantic mutations complete the integrity audit. All calculations use exact rationals and no random input.

#### Data availability.

The scripts and evidence are in the C106 package directory.\
The scope firewall is `NO_BAD_EULER_OR_ROOT_NUMBER`.
