---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-billiard-primitive-heat-trace-route-a"
canonical_tex: "henon_dynamics/henon_billiard_primitive_heat_trace_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_billiard_primitive_heat_trace_route_a/paper/main.pdf"
source_sha256: "10ace603f2a1a7cdd9c10a6ee73b7950e5dcde6dc6f4459d6ce6a3559e84d68a"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Primitive-Direction Heat Transform for Square-Billiard Families

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_billiard_primitive_heat_trace_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_billiard_primitive_heat_trace_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_billiard_primitive_heat_trace_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_billiard_primitive_heat_trace_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We regularize the primitive direction families of the unit square billiard by a positive squared-length heat transform. Möbius inversion gives an exact theta factorization, and an elementary quarter-disk count plus Stieltjes integration gives its small-time law. Coincident lengths retain direction multiplicity. The construction is not a wave trace, isolated-orbit determinant, or target identity.
author:
- 'Route-A structural certificate C152'
title: |
  A Primitive-Direction Heat Transform\
  for Square-Billiard Families
```

## Markdown 正文

# Transform and factorization

For ordered positive coprime pairs, coordinate swap retained and axes excluded, set $$H_{\rm prim}(t)=\sum_{\substack{m,n\geq1\\(m,n)=1}}
 e^{-4t(m^2+n^2)},\qquad t>0.                    \tag{1}$$ The exponent is $-tL_{m,n}^2$ for square-billiard length $L_{m,n}=2\sqrt{m^2+n^2}$. With $\theta_+(u)=\sum_{k\geq1}e^{-uk^2}$, the coprimality identity gives $$H_{\rm prim}(t)=\sum_{d\geq1}\mu(d)\theta_+(4td^2)^2.      \tag{2}$$ The interchange is absolute because monotonicity gives $$\theta_+(4td^2)\leq\int_0^\infty e^{-4td^2x^2}\,dx
=\frac{\sqrt\pi}{4d\sqrt t},$$ so the absolute transformed sum is bounded by $\frac{\pi}{16t}\sum_{d\geq1}d^{-2}$. Each ordered primitive direction appears once, so different pairs of the same length add their multiplicities.

# Primitive density and small time

For real $R\geq0$, let $Q(R)$ count ordered positive lattice points in the quarter disk and let $N(R)$ count the coprime ones. Unit-square comparison gives $$Q(R)=\frac{\pi R^2}{4}+O(R+1).$$ Möbius inversion then yields $$N(R)=\sum_{d\leq R/\sqrt2}\mu(d)Q(R/d)
    =\frac{3R^2}{2\pi}+O(R\log R).               \tag{3}$$ Indeed, absolute Dirichlet convolution and the Basel sum give $\sum_{d\geq1}\mu(d)d^{-2}=1/\zeta(2)=6/\pi^2$; its omitted tail is $O(R^{-1})$, while the boundary errors sum to $O(R\sum_{d\leq R}d^{-1})$. Stieltjes integration by parts gives $$H_{\rm prim}(t)=8t\int_0^\infty r e^{-4tr^2}N(r)\,dr.$$ Substitution of (3) gives $$H_{\rm prim}(t)=\frac{3}{8\pi t}
 +O\!\left(t^{-1/2}\log(1/t)\right),\qquad t\downarrow0.  \tag{4}$$ The remainder follows directly from $t\int_0^\infty r^2\log(2+r)e^{-4tr^2}\,dr$ after the change $u=\sqrt t\,r$.

# Exact validation and boundary

If $b_s$ counts every ordered positive representation $s=a^2+b^2$ and $c_s$ the primitive ones, (2) is coefficientwise $c_s=\sum_{d^2\mid s}\mu(d)b_{s/d^2}$. Producer and independent checker agree for every $s\leq20000$ and on Euclidean radius counts through $200$; SymPy independently verifies initial coefficients and the leading integral.

This is a direction-label heat transform. It is not a clean wave trace, a Gutzwiller or isolated-orbit determinant, or the spectral heat trace of the Dirichlet Laplacian.

The tuple is $(\texttt{A1\_WEAK},\texttt{A2\_FAIL},\texttt{A3\_FAIL},
\texttt{A4\_NATURAL\_QUANTIZATION})$. We claim no target divisor, functional equation or counting law, arithmetic/local factor, Euler factor, root number, automorphy, Hilbert--Pólya construction, or Route-B authorization. Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.
