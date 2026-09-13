---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-uniform-mobius-bergman-family-route-a"
canonical_tex: "henon_dynamics/henon_uniform_mobius_bergman_family_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_uniform_mobius_bergman_family_route_a/paper/main.pdf"
source_sha256: "e9918086cdc6c14c3b87b2cf9940ebe853e3d1763b0aef0af1f119f1ac453437"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Uniform Trace-Class Möbius--Bergman Families with Quantified Order Sensitivity

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_uniform_mobius_bergman_family_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_uniform_mobius_bergman_family_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_uniform_mobius_bergman_family_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_uniform_mobius_bergman_family_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We promote a two-branch Möbius transfer operator from one digit pair to the rectangle $(a,b)\in[3,7/2]\times[6,7]$. The closed branch images remain separated by at least $1/45$, while the unweighted composition sum on normalized Bergman space is trace class with norm at most $89/16$ and is trace-norm Lipschitz in both parameters. Every word has an exact quadratic-surds trace, giving all power traces and a primitive Fredholm product. The non-cyclic same-count words $aaabb$ and $aabab$ have matrix trace gap $a(b-a)^2\ge175/8$, so order sensitivity holds uniformly. These are source-dynamical statements, not an arithmetic or target spectral identification.
author:
- 'Hénon Route-A Working Series, C137'
date: 24 August 2026
title: |
  Uniform Trace-Class Möbius--Bergman Families\
  with Quantified Order Sensitivity
```

## Markdown 正文

# Family-level progress

Let $\mathbb D=\{z:|z|<1\}$ and equip $A^2(\mathbb D)$ with normalized area, so $e_n(z)=\sqrt{n+1}z^n$ is orthonormal. Freeze $$\phi_x(z)=\frac1{x+z},\qquad
 \mathcal L_{a,b}=C_{\phi_a}+C_{\phi_b},\qquad
 (a,b)\in\mathcal R_*=[3,7/2]\times[6,7].$$ The advance over a fixed pair is uniform: no conclusion below depends on choosing one parameter sample.

# Uniform geometry and nuclearity

The image of $\overline\mathbb D$ under $\phi_x$ is the closed disk with center $x/(x^2-1)$ and radius $1/(x^2-1)$. Its real extremes are $1/(x+1)$ and $1/(x-1)$, hence the gap between the two images is $$g(a,b)=\frac1{a+1}-\frac1{b-1}\ge
 \frac1{9/2}-\frac15=\frac1{45}.$$ This is a rectangle theorem rather than a corner sample: $1/(a+1)$ decreases with $a$, whereas $-1/(b-1)$ increases with $b$. The minimum is therefore attained at the exact corner $(a,b)=(7/2,6)$.

The endpoint is substantive. On the initially tempting larger rectangle $[3,4]\times[6,7]$, the same monotonic calculation gives $g(4,6)=1/5-1/5=0$. The two open images remain disjoint at that corner, but their closures are tangent. Thus pointwise open-image separation cannot be promoted to a positive uniform closed gap on the larger rectangle.

[\[thm:nuclear\]]{#thm:nuclear label="thm:nuclear"} For every $(a,b)\in\mathcal R_*$, $\mathcal L_{a,b}$ is trace class and $\|\mathcal L_{a,b}\|_1\le89/16$.

The rank-one expansion $C_{\phi_x}f=\sum_{n\ge0}\langle f,e_n\rangle\sqrt{n+1}\phi_x^n$ is nuclear because $\sup_{\mathbb D}|\phi_a|\le1/2$ and $\sup_{\mathbb D}|\phi_b|\le1/5$. Using $\sqrt{n+1}\le n+1$ gives $$\|\mathcal L_{a,b}\|_1\le\sum_{n\ge0}(n+1)2^{-n}
 +\sum_{n\ge0}(n+1)5^{-n}=4+\frac{25}{16}.$$

[\[prop:lip\]]{#prop:lip label="prop:lip"} For two parameters in $\mathcal R_*$, $$\|\mathcal L_{a,b}-\mathcal L_{a',b'}\|_1
 \le4|a-a'|+\frac5{32}|b-b'|.$$

The resolvent identity gives $|\phi_x-\phi_y|\le|x-y|/(m-1)^2$ on $\mathbb D$ when $x,y\ge m$. If both symbols have modulus at most $r$, then $|\phi_x^n-\phi_y^n|\le nr^{n-1}|\phi_x-\phi_y|$. The same rank-one decomposition as in Theorem [\[thm:nuclear\]](#thm:nuclear){reference-type="ref" reference="thm:nuclear"} now bounds the trace norm by $$\frac{|x-y|}{(m-1)^2}
 \sum_{n\ge1}(n+1)nr^{n-1}
 =\frac{2|x-y|}{(m-1)^2(1-r)^3}.$$ The choices $(m,r)=(3,1/2)$ and $(6,1/5)$ give $4$ and $5/32$.

# All words and the determinant

Put $M_x=\left(\begin{smallmatrix}0&1\\1&x\end{smallmatrix}\right)$. For $M_w=\left(\begin{smallmatrix}A&B\\C&D\end{smallmatrix}\right)$, write $t=\operatorname{tr}M_w$, $\delta=(-1)^{|w|}$, and $\Delta=t^2-4\delta$. Directly solving the fixed equation gives $$z_w=\frac{A-D+\sqrt\Delta}{2C},\quad
 \lambda_w=\frac{t-\sqrt\Delta}{t+\sqrt\Delta},\quad
 \operatorname{Tr}C_{\Phi_w}=\frac12+\frac{t}{2\sqrt\Delta}.$$ Here $M_{x_1}\cdots M_{x_n}$ represents $\phi_{x_1}\circ\cdots\circ\phi_{x_n}$. Composition operators multiply in the reversed function order. Reversal is a bijection on all length-$n$ words, so it preserves the complete trace sum without asserting a false termwise order equality. Expansion of $\mathcal L_{a,b}^n$ therefore gives every power trace. Regrouping repetitions in the Fredholm logarithm yields $$\label{eq:product}
 \det(I-z\mathcal L_{a,b})=\prod_{[p]}\prod_{k\ge0}
 (1-z^{|p|}\lambda_p^k),\qquad |z|<\tfrac12 .$$ Cyclic rotation preserves the trace and determinant of a matrix product, so $\lambda_p$ is well defined on the class $[p]$. There are at most $2^\ell/\ell$ primitive classes of length $\ell$, while the chain rule gives $|\lambda_p|\le4^{-\ell}$. Consequently the absolute factor arguments are bounded by a constant multiple of $\sum_{\ell\ge1}(2|z|)^\ell/\ell$. This proves raw-product convergence for $|z|<1/2$; the near-zero logarithmic identity extends across that disk by the identity theorem. The left side is entire by Theorem [\[thm:nuclear\]](#thm:nuclear){reference-type="ref" reference="thm:nuclear"}, but analytic continuation of the determinant does not claim convergence of the displayed raw factors outside their proved disk.

# Uniform order sensitivity

The words $aaabb$ and $aabab$ have the same symbol population and are not cyclic rotations. Exact multiplication gives $$\begin{aligned}
 t_1&=a^3b^2+a^3+2a^2b+2ab^2+3a+2b,\\
 t_2&=a^3b^2+4a^2b+ab^2+3a+2b,\end{aligned}$$ so $$t_1-t_2=a(b-a)^2\ge\frac{175}{8}.$$ Every coefficient in the displayed polynomial for $t_1$ is positive on $\mathcal R_*$, so it is coordinatewise increasing and $t_1\le t_1(7/2,7)=10731/4$. For $F(t)=1/2+t/(2\sqrt{t^2+4})$, $F'(t)=2/(t^2+4)^{3/2}$. The mean-value theorem therefore gives $$F(t_1)-F(t_2)\ge
 \frac{2800}{(10731^2+64)^{3/2}}>0.$$ Both traces are positive throughout $\mathcal R_*$, so the derivative bound is applied on exactly the interval between $t_2$ and $t_1$; no squaring or branch choice is hidden in this comparison.

# Exact receipt and boundary

At nine rational sentinels, the release reconstructs all words through period ten: $9(2^1+\cdots+2^{10})=18{,}414$ rooted receipts and $9\cdot226=2{,}034$ primitive-parameter receipts. A separate symbolic run performs $18{,}379$ exact checks; replay is byte-identical and 40 repaired-hash plus one stale-hash mutations are rejected. The grid audits the implementation and is not the proof of uniformity.

The exact verdict is $$(\mathrm{A1\_WEAK},\mathrm{A2\_FAIL},\mathrm{A3\_FAIL},
 \mathrm{A4\_FAIL}).$$ There is no target divisor, prime or zero table, arithmetic Euler factor, root number, automorphy claim, unitary lift, or Hilbert--Pólya operator. Route B is unauthorized under `NO_BAD_EULER_OR_ROOT_NUMBER`.

# Conclusion

C137 proves that nonlinear order sensitivity and trace-class determinant control persist on a compact parameter family. Connecting this source-owned family to any external target is a separate unsupported problem.
