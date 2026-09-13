---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-mcmillan-rational-route-a"
canonical_tex: "henon_dynamics/henon_mcmillan_rational_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_mcmillan_rational_route_a/paper/main.pdf"
source_sha256: "0867366f4cef87958bb0849565c4d1e5e99adaf55ee965e9774cb5646c246548"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Reversible Rational McMillan Map: Exact Pole Exclusion and Low-Period Monodromy

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_mcmillan_rational_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_mcmillan_rational_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_mcmillan_rational_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_mcmillan_rational_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We examine the rational recurrence $M(x,y)=(-4x/(1+x^2)-y,x)$. Exact symbolic calculation verifies its rational inverse, coordinate-swap reversor, unit Jacobian determinant, and quartic first integral. The valid fixed locus over $\mathbb C$ contains one real and two nonreal points, while $(1,-1)\leftrightarrow(-1,1)$ is a genuine real primitive two-cycle. We expose and remove the factor $(x^2+1)^2$ introduced by denominator clearing: its roots are poles, not periodic points. The cycle's two-step monodromy is $-I_2$. These are finite low-period certificates, not a global orbit classification or transfer determinant.
author:
- 'Anonymous Route-A report'
title: |
  A Reversible Rational McMillan Map:\
  Exact Pole Exclusion and Low-Period Monodromy
```

## Markdown 正文

# Rational map and invariant

We freeze the McMillan/QRT-type family $$M_\mu(x,y)=\left(\frac{2\mu x}{1+x^2}-y,x\right),\qquad \mu=-2.$$ Over $\mathbb C$ the forward map excludes $x^2+1=0$. Its rational inverse is $$M^{-1}(x,y)=\left(y,-\frac{4y}{1+y^2}-x\right).$$ For the involution $S(x,y)=(y,x)$, direct composition gives $SMS=M^{-1}$. Differentiation gives $$DM(x,y)=\begin{pmatrix}
 4(x^2-1)/(1+x^2)^2&-1\\1&0
 \end{pmatrix},\qquad \det DM=1.$$ Substitution and cancellation also give $$I\circ M=I,\qquad I(x,y)=x^2y^2+x^2+y^2+4xy.$$

# Fixed points and a two-cycle

The fixed equations force $y=x$ and reduce to $$-\frac{2x(x^2+3)}{x^2+1}=0.$$ Thus the valid fixed points are $(0,0)$ and $(\pm i\sqrt3,\pm i\sqrt3)$, with matched signs. Only the origin is real. Direct substitution gives the distinct real cycle $$q_+=(1,-1)\longmapsto q_-=(-1,1)\longmapsto q_+,
 \qquad I(q_\pm)=-1.$$ Both cycle denominators equal $2$, so neither point is a pole.

For the second iterate, eliminating $y$ from the two cleared numerators gives $$-8x(x-1)(x+1)(x^2+1)^2(x^2+3).$$ The roots of $x^2+1$ cannot be tested as orbit points because the first application of $M$ is already undefined. Removing this pole factor leaves $x(x-1)(x+1)(x^2+3)$: the factors $x(x^2+3)$ recover the fixed locus and $x^2-1$ gives the primitive cycle.

  candidate       type                       $1+x^2$   status
  --------------- -------------------------- --------- ----------
  $0$             real fixed                 $1$       valid
  $\pm i\sqrt3$   nonreal fixed              $-2$      valid
  $\pm1$          real two-cycle             $2$       valid
  $\pm i$         cleared-denominator root   $0$       excluded

# Local period-two monodromy

At either cycle point the first derivative is $$J_\pm=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.$$ In chronological order the derivative of $M^2$ is therefore $$P_2=J_-J_+=-I_2,\qquad
 \det P_2=1,\quad \operatorname{tr}P_2=-2.$$ Consequently $$\det(\lambda I-P_2)=(\lambda+1)^2,
 \qquad \det(I-zP_2)=(1+z)^2.$$ As a one-step control, the real fixed point has $$J_0=DM(0,0)=\begin{pmatrix}-4&-1\\1&0\end{pmatrix},\qquad
 \det(I-zJ_0)=z^2+4z+1.$$ The unequal control polynomials prevent a one-step fixed-point linearization from being conflated with the chronological two-step cycle product.

The inverse, reversor, invariant, fixed points, pole exclusions, primitive cycle, and displayed monodromy identities are exact on their stated domains.

An independent checker recomputes both rational compositions, differentiates the map, substitutes into $I$, recomputes the raw resultant, tests every candidate denominator and orbit arrow, and multiplies the Jacobians without importing the evidence producer.

# Route-A boundary

The two displayed $z$-polynomials are characteristic data of finite local derivatives. They have neither orbit weights nor a trace identity over a global state space. In particular, $(1+z)^2$ belongs only to the local derivative of $M^2$ along one cycle. No transfer operator, finite transfer owner, function space, or tail bound has been constructed. The result is `A1_PARTIAL_CERTIFIED`, `A2_FAIL`, `A3_NOT_ADDRESSED`, and `A4_FAIL`. We do not claim a complete orbit atlas, global integrability classification, analytic Fredholm determinant, arithmetic data, or Route-B object. The scope firewall is `NO_BAD_EULER_OR_ROOT_NUMBER`.
