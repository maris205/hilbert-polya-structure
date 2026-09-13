---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-brusselator-hopf-normal-form-route-a"
canonical_tex: "henon_dynamics/henon_brusselator_hopf_normal_form_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_brusselator_hopf_normal_form_route_a/paper/main.pdf"
source_sha256: "a25bf3690d895b81b693e2108e33e17e79a9ec01201606712865e6e9900d6a6c"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Convention-Explicit Hopf Atlas for the Brusselator

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_brusselator_hopf_normal_form_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_brusselator_hopf_normal_form_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_brusselator_hopf_normal_form_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_brusselator_hopf_normal_form_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For every $A>0$ and $B\ge0$, we prove positive-quadrant global existence for the Brusselator and give its complete node, focus, defective, and Hopf equilibrium atlas. \>0 With explicitly normalized right/left eigenvectors we derive the full complex $G_{21}$, distinguish three coefficient conventions, prove uniform supercriticality, and obtain leading cycle amplitude and frequency. \>1 Independent exact, symbolic, replay, mutation, and deterministic-build lanes audit the theorem and its strictly weak Route-A orbit signal.
author:
- 'Route-A source-local certificate HCS-C311'
date: 3 September 2026
title: 'A Convention-Explicit Hopf Atlas for the Brusselator'
```

## Markdown 正文

trailerid \[\<C3112026090300000000000000000000\>\<C3112026090300000000000000000000\>\]

# Global existence and complete linear atlas

Consider $$\label{eq:model}
 \dot x=A-(B+1)x+x^2y,\qquad \dot y=Bx-x^2y,
 \quad A>0,\ B\ge0.$$ At $x=0$ the first component equals $A>0$, and at $y=0$ the second is $Bx\ge0$; hence the closed nonnegative quadrant is invariant. There $(x+y)'=A-x\le A$, so neither coordinate can blow up in finite time. Every nonnegative solution is therefore global.

[\[thm:linear\]]{#thm:linear label="thm:linear"} Equation [\[eq:model\]](#eq:model){reference-type="eqref" reference="eq:model"} has the unique nonnegative equilibrium $E=(A,B/A)$. Put $\tau=B-1-A^2$. Its Jacobian is $$\label{eq:J}
 J=\begin{pmatrix}B-1&A^2\\-B&-A^2\end{pmatrix},
 \qquad \operatorname{tr}J=\tau,\quad\det J=A^2.$$ Within $B\ge0$, the increasing-$B$ atlas is

  range or boundary   type
  ------------------- -------------------------
  $B<(A-1)^2$         stable node
  $B=(A-1)^2$         defective stable node
  $(A-1)^2<B<1+A^2$   stable focus
  $B=1+A^2$           Hopf pair $\pm iA$
  $1+A^2<B<(A+1)^2$   unstable focus
  $B=(A+1)^2$         defective unstable node
  $B>(A+1)^2$         unstable node

Empty ranges are omitted; in particular $A=1,B=0$ is the stable defective boundary.

At equilibrium, adding the equations gives $x=A$, then the second gives $y=B/A$. Formula [\[eq:J\]](#eq:J){reference-type="eqref" reference="eq:J"} follows by differentiation. Its eigenvalues are $\tau/2\pm\sqrt{\tau^2-4A^2}/2$. The signs of $\tau$ and of this discriminant give every row. At equality the positive off-diagonal entry $A^2$ prevents $J$ from being scalar, hence the repeated eigenvalue is defective.

\>0

# Exact normalized Hopf coefficient

Set $B=1+A^2$ and translate $u=x-A$, $v=y-B/A$. The nonlinear expansion is $$\begin{aligned}
 \dot u&=A^2u+A^2v+(A+A^{-1})u^2+2Auv+u^2v,\\
 \dot v&=-(A^2+1)u-A^2v-(A+A^{-1})u^2-2Auv-u^2v.\end{aligned}$$ Fix right and adjoint eigenvectors $$\label{eq:qp}
 q=(1,-1+i/A)^{\mathsf T},\qquad
 p=((1+iA)/2,iA/2)^{\mathsf T},\qquad \bar p^{\mathsf T}q=1.$$ If $\mathcal B,\mathcal C$ are the second and third derivative multilinear forms, use the convention $$\begin{aligned}
\label{eq:G}
G_{21}=\bar p^{\mathsf T}\{&\mathcal C(q,q,\bar q)
-2\mathcal B(q,J^{-1}\mathcal B(q,\bar q))\\
&+\mathcal B(\bar q,(2iA I-J)^{-1}\mathcal B(q,q))\}.\end{aligned}$$ Direct substitution, with no numerical fitting, gives $$\label{eq:Gvalue}
 G_{21}=-\left(1+\frac2{A^2}\right)
 -i\frac{4A^4-7A^2+4}{3A^3},\qquad
 \ell_1=\frac{\operatorname{Re}G_{21}}{2A}=-\frac{A^2+2}{2A^3}<0.$$

[\[thm:hopf\]]{#thm:hopf label="thm:hopf"} Let $\mu=B-(1+A^2)$. The Hopf crossing is transverse with real-part derivative $1/2$. For all sufficiently small $\mu>0$ there is one local periodic-orbit branch modulo phase; it is stable. In the coordinate of [\[eq:qp\]](#eq:qp){reference-type="eqref" reference="eq:qp"}, $$\begin{aligned}
 r^2&=\frac{A^2}{A^2+2}\mu+O(\mu^2),\label{eq:r}\\
 \Omega&=A-\frac{4A^4-7A^2+4}{6A(A^2+2)}\mu+O(\mu^2).\label{eq:freq}\end{aligned}$$ The first harmonic of $x-A$ has amplitude $2A\sqrt{\mu/(A^2+2)}$ up to an $O(\mu)$ coordinate correction.

Near zero the eigenvalues are $\mu/2\pm i\sqrt{A^2-\mu^2/4}$, proving transversality and absence of linear frequency detuning. The physical-time normal form is $\dot w=(\mu/2+iA)w+(G_{21}/2)w|w|^2+$ higher terms. Its radial cubic coefficient is $-(A^2+2)/(2A^2)$, whereas $\ell_1$ in [\[eq:Gvalue\]](#eq:Gvalue){reference-type="eqref" reference="eq:Gvalue"} includes the additional division by $A$. Solving the radial equation gives [\[eq:r\]](#eq:r){reference-type="eqref" reference="eq:r"}; its derivative is negative at the nonzero root. The imaginary part of $G_{21}/2$ gives [\[eq:freq\]](#eq:freq){reference-type="eqref" reference="eq:freq"}, and $u=w+\bar w+O(|w|^2)$ gives the first harmonic.

The face $B=0$ is included in Theorem [\[thm:linear\]](#thm:linear){reference-type="ref" reference="thm:linear"}. The face $A=0$ is not: $B/A$ is singular and $x=0$ becomes an equilibrium line. No global uniqueness of periodic orbits is inferred from the local Hopf theorem.

\>1

# Evidence, collisions, and Route-A boundary

Twelve rational values $1/4\le A\le10$ produce 55 admissible chamber probes and 827 audited leaves. An independent checker performs 742 exact/numerical checks. A separate SymPy program differentiates the vector field and derives [\[eq:Gvalue\]](#eq:Gvalue){reference-type="eqref" reference="eq:Gvalue"} in 13 identities; replay is byte exact and 26 repaired-hash or parser attacks must fail. These lanes audit conventions, not the proof.

C249 owns the global Van der Pol Liénard cycle, C235 a simplex replicator, and C254 a washout/transcritical chemostat. C311 instead closes the Brusselator's all-$A$ chemical Hopf coefficient and linear chamber geometry.

The strict tuple is $$(\mathrm{A0\_FAIL},\mathrm{A1\_WEAK},\mathrm{A2\_FAIL},
 \mathrm{A3\_FAIL},\mathrm{A4\_FAIL}).$$ The local isolated cycle is genuine source dynamics, earning only A1 weak. Continuous reaction parameters carry no rational-prime local owner (A0) or logarithmic-prime clock (A2); the normal form gives no target determinant (A3) or self-adjoint target-zero operator (A4). Route A is rejected and Route B remains locked under `NO_BAD_EULER_OR_ROOT_NUMBER`. No target Euler factor, root number, automorphy statement, divisor law, functional equation, or zero correspondence is claimed.

#### AI use.

A generative language model assisted drafting and code scaffolding. The displayed derivation, independent symbolic reconstruction, adversarial tests, and archived artifacts define the audit record.

# Source lineage {#source-lineage .unnumbered}

9 I. Prigogine and R. Lefever, "Symmetry breaking instabilities in dissipative systems. II," *J. Chem. Phys.* 48 (1968), 1695--1700. DOI: [10.1063/1.1668896](https://doi.org/10.1063/1.1668896). Y. A. Kuznetsov, *Elements of Applied Bifurcation Theory*, 3rd ed., Springer, 2004. DOI: [10.1007/978-1-4757-3978-7](https://doi.org/10.1007/978-1-4757-3978-7).
