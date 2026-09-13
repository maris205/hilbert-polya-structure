---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-heisenberg-nilmanifold-clean-fixed-sets-route-a"
canonical_tex: "henon_dynamics/henon_heisenberg_nilmanifold_clean_fixed_sets_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_heisenberg_nilmanifold_clean_fixed_sets_route_a/paper/main.pdf"
source_sha256: "e4671846a768600c592075ab7860a15437e7b3b89391d9d826ade9c0b616bbea"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Clean Fixed Circles Obstruct Isolated-Orbit Determinants on a Heisenberg Nilmanifold

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_heisenberg_nilmanifold_clean_fixed_sets_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_heisenberg_nilmanifold_clean_fixed_sets_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_heisenberg_nilmanifold_clean_fixed_sets_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_heisenberg_nilmanifold_clean_fixed_sets_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We freeze an explicit integer-lattice automorphism of the three-dimensional Heisenberg group. Its horizontal action is hyperbolic, while its center is fixed pointwise. Every iterate therefore owns a clean central fixed circle, has singular ordinary isolated-orbit stability factor, and has zero Lefschetz number. The horizontal torus provides an exact isolated-point control through iterate twenty. These are source-side obstruction results, not a target or arithmetic construction.
author:
- 'Route-A structural certificate C146'
title: |
  Clean Fixed Circles Obstruct Isolated-Orbit\
  Determinants on a Heisenberg Nilmanifold
```

## Markdown 正文

# The frozen lattice automorphism

Write the real Heisenberg group as $H=\mathbb R^3$ with $$(x,y,z)(X,Y,Z)=(x+X,y+Y,z+Z+xY),
\qquad \Gamma=\mathbb Z^3.$$ On the compact left quotient $N=\Gamma\backslash H$, freeze $$A=\begin{pmatrix}2&1\\1&1\end{pmatrix},\qquad
q(x,y)=x(x-1)+xy+\frac{y(y-1)}2,$$ and $$\Phi(x,y,z)=(2x+y,x+y,z+q(x,y)).                 \tag{1}$$ The central correction is forced by the coordinate cocycle. Direct expansion gives $$q(v+w)-q(v)-q(w)=2xX+xY+Xy+yY,$$ which equals $(2x+y)(X+Y)-xY$. Thus (1) is a group homomorphism. Moreover, $q(m,n)$ is integral for integer $m,n$, so the map preserves $\Gamma$. Since $A^{-1}$ is integral and the inverse central correction is $-q(A^{-1}v)$, the inverse preserves $\Gamma$ as well. Hence (1) is a lattice automorphism and descends to $N$.

# Clean fixation and singular stability

The embedded central circle $$C=\{[0,0,z]:z\in\mathbb R/\mathbb Z\}$$ is fixed pointwise by $\Phi$, hence by every positive iterate. The horizontal eigenvalues are $(3\pm\sqrt5)/2$, neither of whose positive powers is one. Consequently the horizontal fixed classes at each iterate are discrete, and $C$ is a one-dimensional fixed component. Along $C$, the derivative has blocks $\left(\begin{smallmatrix}A^n&0\\ \ell_n&1\end{smallmatrix}\right)$. The kernel equation first gives $(I-A^n)\delta v=0$, hence $\delta v=0$, while $\delta z$ is free. Therefore $\ker(I-D\Phi^n)=T C$, which is the clean condition.

The derivative is block lower triangular. For every $n\geq1$, its diagonal blocks are $A^n$ and $1$, so $$\det(I-D\Phi^n)=\det(I-A^n)(1-1)=0.              \tag{2}$$ Thus the usual stability denominator for an isolated periodic orbit is singular at every period. We do not introduce a clean-family regularization.

Let $\alpha=dx$, $\beta=dy$, and $\gamma=dz-x\,dy$, with $d\gamma=-\alpha\wedge\beta$. Heisenberg cohomology has dimensions $(1,2,2,1)$: by the Nomizu theorem the left-invariant complex computes the cohomology of this compact nilmanifold, and direct calculation gives bases $1$; $[\alpha],[\beta]$; $[\alpha\wedge\gamma],[\beta\wedge\gamma]$; and $[\alpha\wedge\beta\wedge\gamma]$. Direct differentiation gives $$\Phi^*\alpha=2\alpha+\beta,\qquad
\Phi^*\beta=\alpha+\beta,\qquad
\Phi^*\gamma=\gamma-\alpha-\tfrac12\beta.$$ The extra horizontal wedges are multiples of $\alpha\wedge\beta=-d\gamma$, hence exact. On the bases $[\alpha],[\beta]$ and $[\alpha\wedge\gamma],[\beta\wedge\gamma]$, pullback consequently has the same trace $\operatorname{tr}(A^n)$; it acts as the identity in degrees zero and three. Therefore $$L(\Phi^n)=1-\operatorname{tr}(A^n)+
\operatorname{tr}(A^n)-1=0.                    \tag{3}$$

# Horizontal control and exact validation

On the horizontal torus, fixed classes form $\ker(A^n-I:\mathbb T^2\to\mathbb T^2)$, so their number is $$|\det(A^n-I)|=\operatorname{tr}(A^n)-2=L_{2n}-2, \tag{4}$$ where $L_k$ is the Lucas sequence. Here $A=Q^2$ for $Q=\left(\begin{smallmatrix}1&1\\1&0\end{smallmatrix}\right)$, proving the last equality. Exact evidence records (4), (2), and (3) through $n=20$.

The toral number in (4) is not a nilmanifold component count. At $n=2$ the horizontal class $v=(1/5,2/5)$ satisfies $(A^2-I)v=(2,1)$, but $q(v)+q(Av)=0$. If a point $(v,z)$ were fixed on the left quotient, some $(2,1,k)\in\Gamma$ would obey $\Phi^2(v,z)=(2,1,k)(v,z)$. Its central coordinate would require $0=k+2(2/5)$, impossible for integral $k$. Thus this base class does not lift to a fixed circle, and we assert no full component count for $\operatorname{Fix}(\Phi^n)$.

The independent checker passes 687 assertions, the SymPy reconstruction passes 87 checks, byte replay passes, and all 31 hostile receipts (30 repaired- hash semantic mutations and one stale hash) are rejected.

# Route-A boundary

The strict tuple is $(\texttt{A1\_FAIL},\texttt{A2\_FAIL},
\texttt{A3\_FAIL},\texttt{A4\_FORMAL\_HINT})$, overall `ROUTE_A_EXPLORATORY`. The block determinant of $D\Phi$ is one, so the descended map preserves Haar volume. It gives a natural Koopman unitary $U_\Phi f=f\circ\Phi$ on all of $L^2(N)$, with $U_\Phi^n f=f\circ\Phi^n$ and hence the same iterate clock, but no bridge to the singular clean-family weights; it is only a formal hint. We claim no isolated primitive-orbit ledger, target divisor, target functional equation or counting law, arithmetic/local factor, Euler factor, root number, automorphy, Hilbert--Pólya construction, or Route-B authorization. The scope literal is `NO_BAD_EULER_OR_ROOT_NUMBER`.
