---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-irrational-roof-suspension-route-a"
canonical_tex: "henon_dynamics/henon_irrational_roof_suspension_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_irrational_roof_suspension_route_a/paper/main.pdf"
source_sha256: "b3e063054b7b9ae28a231adad4f7ec3a4779d61e29151e033109c177faf4b77d"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# An All-Period Nonlattice Suspension Determinant with Exact Clock-Sector Separation

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_irrational_roof_suspension_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_irrational_roof_suspension_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_irrational_roof_suspension_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_irrational_roof_suspension_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We freeze the full binary shift with roof values $1$ and $\sqrt2$. Its two-state bivariate matrix has determinant $1-u-v$; Laplace specialization gives the entire exponential polynomial $1-e^{-s}-e^{-\sqrt2s}$. The same source owns an all-period primitive dynamical Euler/trace identity. Irrationality separates symbol-count clock sectors and forbids a nonzero imaginary period, while the rational roof $(1,2)$ restores collisions and vertical periodicity. These are source-dynamical statements, not a target divisor or arithmetic correspondence.
author:
- 'Route-A structural certificate C130'
title: 'An All-Period Nonlattice Suspension Determinant with Exact Clock-Sector Separation'
```

## Markdown 正文

# Frozen mixing suspension

Let $B=\left(\begin{smallmatrix}1&1\\1&1\end{smallmatrix}\right)$ and let $\Sigma_B$ be the two-sided full binary shift. Since $B$ is positive, the shift is mixing. Freeze $\tau(0)=1$, $\tau(1)=\sqrt2$ and form $X^\tau=(\Sigma_B\times\mathbb R)/((x,t+\tau(x))\sim(\sigma x,t))$. For a closed word $w$, write $N_j(w)$ for its symbol populations and $$\ell(w)=N_0(w)+\sqrt2N_1(w).$$

# Bivariate owner and primitive identity

Destination-symbol weights give $$M(u,v)=B\operatorname{diag}(u,v)=
\begin{pmatrix}u&v\\u&v\end{pmatrix},\qquad
\Delta(u,v)=\det(I-M)=1-u-v.$$ The eigenvalues are $u+v,0$, hence for every $n\ge1$, $$\operatorname{Tr}M^n=(u+v)^n=
\sum_{k=0}^n\binom nk u^{n-k}v^k. \tag{1}$$ The trace sums all rooted binary closed words. For $|u|+|v|<1$, $$-\log\Delta(u,v)=\sum_{n\ge1}\frac{\operatorname{Tr}M(u,v)^n}{n}.$$ Decomposing each word uniquely as a repetition of a primitive cyclic word $\gamma$ and regrouping this absolutely convergent series gives $$\Delta(u,v)=\prod_{[\gamma]}
(1-u^{N_0(\gamma)}v^{N_1(\gamma)}). \tag{2}$$ Thus with $u=e^{-s}$ and $v=e^{-\sqrt2s}$, $$d_\tau(s)=1-e^{-s}-e^{-\sqrt2s}
=\prod_{[\gamma]}(1-e^{-s\ell(\gamma)}). \tag{3}$$ Equation (2) also holds formally in the total-degree completion, since each degree sees finitely many cycles. Let $h>0$ solve $e^{-h}+e^{-\sqrt2h}=1$. The product (3) converges absolutely for $\operatorname{Re}s>h$. The explicit left side is entire and its reciprocal is meromorphic; the product is not asserted to converge globally.

# Irrational clock and rational control

If $a+b\sqrt2=c+d\sqrt2$ for integers, irrationality gives $(a,b)=(c,d)$. Thus different population vectors never collide in suspension time. This is not orbit injectivity: the distinct primitive necklaces $000111$ and $001011$ both have vector $(3,3)$ and roof $3+3\sqrt2$.

The same independence forbids a nonzero imaginary period. Indeed, $d_\tau(s+iT)=d_\tau(s)$ for every $s$ forces $e^{-iT}=e^{-i\sqrt2T}=1$ by separating the two exponential coefficients. Thus both $T/(2\pi)$ and $\sqrt2T/(2\pi)$ are integers, so $T=0$.

For the control, change only the roof to $(1,2)$. Then $$d_{\rm rat}(s)=1-e^{-s}-e^{-2s}=1-q-q^2,\qquad q=e^{-s}.$$ The second repetition of $[0]$, with counts $(2,0)$, collides at time $2$ with primitive fixed orbit $[1]$, with counts $(0,1)$. Also $d_{\rm rat}(s+2\pi i)=d_{\rm rat}(s)$: lattice periodicity is restored.

# Replay and Route-A boundary

Exact replay gives

  $n$           1   2   3    4    5    6     7     8     9     10
  ----------- --- --- --- ---- ---- ---- ----- ----- ----- ------
  rooted        2   4   8   16   32   64   128   256   512   1024
  primitive     2   1   2    3    6    9    18    30    56     99
  sectors       2   3   4    5    6    7     8     9    10     11

Totals are $2046$ rooted words, $226$ primitive cycles, and $65$ sectors. The independent standard-library checker (139 assertions), fresh symbolic reconstruction (110 checks), and byte replay pass. The hostile suite rejects all 43 repaired-hash semantic forgeries and one separate stale-hash mutation.

The strict tuple is $(\texttt{A1\_WEAK},\texttt{A2\_FAIL},\texttt{A3\_FAIL},
\texttt{A4\_FAIL})$, overall `ROUTE_A_EXPLORATORY`; Route B is disabled. We claim no arithmetic Euler factors, root number, target divisor, functional equation, automorphy, natural Hilbert--Pólya lift, or orbit-level injectivity within a sector. The literal firewall is `NO_BAD_EULER_OR_ROOT_NUMBER`.
