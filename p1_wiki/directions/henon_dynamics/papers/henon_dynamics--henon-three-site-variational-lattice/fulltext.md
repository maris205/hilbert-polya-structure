---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-three-site-variational-lattice"
canonical_tex: "henon_dynamics/henon_three_site_variational_lattice/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_three_site_variational_lattice/paper/main.pdf"
source_sha256: "2ea268bf9aabbf5ea04a59ed7c349be92fabb11ee0dbe288d25d6bba995b63dc"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Three-Site Variational Hénon Ring: An Exact Fourier-Mode Period-Two Witness

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_three_site_variational_lattice>)
- [规范 TeX](<../../../../../henon_dynamics/henon_three_site_variational_lattice/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_three_site_variational_lattice/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_three_site_variational_lattice/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We give a small exact certificate for a genuinely three-site variational Hénon lattice. A triangular coupling graph, with $a=7$ and $\kappa=1/5$, yields a polynomial exact-symplectic map over $\mathbb{Q}$. Two synchronous fixed points and one primitive synchronous period-two orbit are verified by independent rational arithmetic. The two-step Jacobian splits into one longitudinal and two transverse Laplacian modes, giving the factorisation $(1+7z+z^2)(1+106z/25+z^2)^2$ for the finite monodromy polynomial. This is deliberately a low-period witness; no global zeta or arithmetic claim is made.
author:
- 'Route-A finite certificate C111'
title: |
  A Three-Site Variational Hénon Ring:\
  An Exact Fourier-Mode Period-Two Witness
```

## Markdown 正文

# Scope and model

This paper records package C111 in the exploratory Route-A line. The claim is an auditable finite calculation, not a global zeta theorem. Let $q,p\in
\mathbb{Q}^3$ and let $$L=\begin{pmatrix}2&-1&-1\\-1&2&-1\\-1&-1&2\end{pmatrix},\qquad
 U(q)=\sum_{i=1}^3\left(\frac{7}{2}q_i^2-\frac13q_i^3\right)
 -\frac1{10}\sum_{\{i,j\}}(q_i-q_j)^2 .$$ The sum has the three edges of the $3$-cycle. The map is $$F(q,p)=(G(q)-p,q),\qquad G(q)=\nabla U(q).
 \label{eq:map}$$ All computations use exact fractions. The evidence file and scripts are listed in the reproducibility paragraph below.

# Exact variational identities

The Hessian and Jacobian are $$H(q)=\operatorname{diag}(7-2q_i)-\tfrac15L,\qquad
 J(q)=\begin{pmatrix}H(q)&-I_3\\ I_3&0\end{pmatrix}.$$ With $\Omega=\left(\begin{smallmatrix}0&I_3\\-I_3&0\end{smallmatrix}\right)$, direct multiplication gives $J(q)^\mathsf{T}\Omega J(q)=\Omega$ and $\det J(q)=1$. The coordinate swap $R(q,p)=(p,q)$ is an involutory reversor: $RFR=F^{-1}$. For the canonical one-form $\lambda=q\mathbin{\cdot}dp$ one has the exact primitive identity $$F^*\lambda-\lambda=d\bigl(U(q)-p\mathbin{\cdot}q\bigr).$$ These are polynomial identities, checked both by the producer/checker and by the independent SymPy script.

# Certified orbit witnesses

The synchronous subspace is invariant because $L(1,1,1)^\mathsf{T}=0$. The two fixed states and the period-two states are $$\begin{aligned}
 P_0&=((0,0,0),(0,0,0)),\\
 P_5&=((5,5,5),(5,5,5)),\\
 C_3&=((3,3,3),(6,6,6)),\qquad
 C_6=((6,6,6),(3,3,3)).
\end{aligned}$$ Substitution into [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"} gives $F(P_i)=P_i$ and $F(C_3)=C_6$, $F(C_6)=C_3$. Since $C_3\ne C_6$, this is a primitive period-two witness. No completeness statement is made about other fixed or periodic points.

# Longitudinal and transverse modes

The Laplacian eigenvalues are $0,3,3$. At a synchronous point with scalar coordinate $s$, the Hessian eigenvalue in mode $\ell$ is $$h_s(\ell)=7-2s-\tfrac15\ell .$$ Thus the two points of the cycle have mode pairs $$(h_3(0),h_6(0))=(1,-5),\qquad
 (h_3(3),h_6(3))=(2/5,-28/5).$$ For a scalar mode, the two-step matrix $\left(\begin{smallmatrix}h_6&-1\\1&0\end{smallmatrix}\right)
\left(\begin{smallmatrix}h_3&-1\\1&0\end{smallmatrix}\right)$ has determinant one and trace $h_3h_6-2$. Therefore the mode traces are $$t_0=-7,\qquad t_\perp=-\frac{106}{25}
 \quad\text{(multiplicity two)}.$$ The direct $6\times6$ monodromy and the mode reconstruction agree exactly: $$\det(I-zM)=(1-t_0z+z^2)(1-t_\perp z+z^2)^2
 =1+\frac{387}{25}z+\frac{50211}{625}z^2
 +\frac{98002}{625}z^3+\frac{50211}{625}z^4
 +\frac{387}{25}z^5+z^6 .
 \label{eq:poly}$$

  mode            Laplacian eigenvalue    $(h_3,h_6)$      trace
  -------------- ---------------------- --------------- -----------
  longitudinal            $0$              $(1,-5)$        $-7$
  transverse 1            $3$            $(2/5,-28/5)$   $-106/25$
  transverse 2            $3$            $(2/5,-28/5)$   $-106/25$

  : Exact two-step mode data on the period-two witness.

As a finite coupling control, setting $\kappa=0$ at the same synchronous states gives the coefficient vector $$(1,21,150,385,150,21,1),$$ instead of the coefficients in [\[eq:poly\]](#eq:poly){reference-type="eqref" reference="eq:poly"}; the trace changes by $138/25$. This comparison isolates a coupling effect without interpreting either polynomial as a Fredholm determinant.

# Reproducibility and limits

From the package directory, run

    python3 code/c111_three_site_producer.py
    python3 code/c111_three_site_checker.py
    python3 code/c111_sympy_crosscheck.py
    python3 code/c111_replay.py
    python3 code/c111_mutation.py

The canonical evidence is `results/c111_three_site_evidence.json`; the mutation audit rejects all twelve semantic edits. The release manifest records hashes for every source, result, and paper artifact.

The route verdict is $A1=\texttt{A1\_WEAK}$ (certified low-period witnesses), $A2=\texttt{A2\_FAIL}$ (operator owner open), $A3$ not addressed, and $A4$ failed; overall status is `ROUTE_A_EXPLORATORY`. In particular, this package does not claim a complete primitive-orbit atlas, a global transfer or Fredholm operator, analytic continuation, Euler factors, root numbers, automorphy, or a Hilbert--Pólya operator. Its scope literal is `NO_BAD_EULER_OR_ROOT_NUMBER`.
