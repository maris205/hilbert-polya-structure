---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-graph-directed-hardy-trace-route-a"
canonical_tex: "henon_dynamics/henon_graph_directed_hardy_trace_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_graph_directed_hardy_trace_route_a/paper/main.pdf"
source_sha256: "5ff83142b0c84d97d98811260b979e84a89a403c48dd58b69b98c5a565d84b63"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# An All-Period Hardy--Fredholm Owner for Strongly Separated Graph-Directed Hénon Contractions

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_graph_directed_hardy_trace_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_graph_directed_hardy_trace_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_graph_directed_hardy_trace_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_graph_directed_hardy_trace_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We freeze a three-state graph-directed affine Hénon system with pairwise disjoint branch images. Primitive admissible necklaces then own primitive geometric cycles at every period. The same branches define a trace-class operator on a direct sum of bidisc Hardy spaces. We prove its all-order trace law, entire Fredholm product, and primitive repetition expansion. A second strongly separated translation triple moves the cycles but preserves the full determinant, exposing an exact geometric non-identifiability. These are source-dynamical statements; no target divisor or arithmetic correspondence is claimed.
author:
- 'Route-A structural certificate C124'
title: |
  An All-Period Hardy--Fredholm Owner for Strongly\
  Separated Graph-Directed Hénon Contractions
```

## Markdown 正文

# Frozen graph-directed contraction

On three copies of $\mathbb D_3^2$, set $$A=\begin{pmatrix}3/16&-1/32\\1/4&0\end{pmatrix},\qquad
\phi_j(z)=Az+(t_j,0),\quad (t_0,t_1,t_2)=(-2,0,2),$$ and freeze $$B=\begin{pmatrix}1&1&0\\1&0&1\\1&0&0\end{pmatrix},\quad
c=(1/2,1/3,1/5),\quad
W=B\operatorname{diag}(c).$$ The eigenvalues of $A$ are $1/8,1/16$ and $\|A\|_\infty=1/4$. The first- and second-coordinate image radii are $21/32$ and $3/4$. The largest first-coordinate extent is $2+21/32=85/32<3$, while adjacent first-coordinate images have gap $2-2(21/32)=11/16>0$. Thus every branch is compactly contained and the three images are pairwise disjoint.

# Primitive cycles

For a cyclic admissible word $w$, the affine composition has linear part $A^{|w|}$. Since $I-A^{|w|}$ is invertible, it has one fixed point. Strong separation makes the itinerary unique; hence primitive cyclic words modulo rotation are in bijection with primitive geometric cycles, with rooted phases and repetitions retained. This is an all-period statement. Exact replay through period eight gives

  period                  1   2   3    4    5    6    7     8
  --------------------- --- --- --- ---- ---- ---- ---- -----
  rooted closed words     1   3   7   11   21   39   71   131
  primitive cycles        1   1   2    2    4    5   10    15

For example, $012$ is primitive, has weight $1/30$, and has phase points $$\frac1{19929}(38912,-1600)\to
\frac1{19929}(-32512,9728)\to
\frac1{19929}(-6400,-8128).$$ Its monodromy is $$A^3=\begin{pmatrix}15/4096&-7/8192\\7/1024&-3/2048\end{pmatrix},
\qquad \det(I-A^3)=\frac{2092545}{2097152}.$$

# Trace-class Hardy owner and determinant

Let $$\mathcal H=\bigoplus_{i=0}^2H^2(\mathbb D_3^2),\qquad
(\mathcal Lf)_i(z)=\sum_jB_{ij}c_j f_j(\phi_j(z)).$$ All images lie in the concentric bidisc of radius $85/32$, so the restriction ratio is $\rho=85/96<1$. Total degree $m$ has multiplicity $m+1$, and the monomial restriction factorization has summable majorant $\sum_{m\ge0}(m+1)\rho^m$. Hence every composition block, and thus $\mathcal L$, is trace class. Translations lower degree and do not change the diagonal graded blocks. Therefore a length-$n$ word satisfies $$\operatorname{Tr}C_{\phi_w}=\sum_{r,s\ge0}8^{-rn}16^{-sn}
=\frac1{(1-8^{-n})(1-16^{-n})}.$$ Summing the rooted closed paths gives, for every $n\ge1$, $$\operatorname{Tr}\mathcal L^n=
\frac{\operatorname{Tr}W^n}{(1-8^{-n})(1-16^{-n})}. \tag{1}$$ In particular the first two traces are $64/105$ and $4096/6885$. Trace class and (1) yield the entire product $$D_H(z)=\det(I-z\mathcal L)
=\prod_{r,s\ge0}\det(I-z8^{-r}16^{-s}W), \tag{2}$$ where $\det(I-uW)=1-u/2-u^2/6-u^3/30$. Normal convergence follows from $\sum_{r,s\ge0}8^{-r}16^{-s}<\infty$ and finite-dimensional $W$; thus (2) is an entire source determinant, not merely a formal series. Grouping by primitive cycles gives the orbit-owned identity $$\log D_H(z)=-\sum_{[\gamma]}\sum_{m\ge1}
\frac{(c_\gamma z^{\ell_\gamma})^m}
{m\det(I-A^{m\ell_\gamma})}.$$

# Blindness control and progress

Replace $t$ by $\widetilde t=(-3/2,0,3/2)$. Its image gap is still $3/16>0$. The $012$ phase points become $$\frac1{6643}(9728,-400),\quad
\frac1{6643}(-8128,2432),\quad
\frac1{6643}(-1600,-2032),$$ but $A,B,c,W$, every trace in (1), and all of (2) are unchanged. Thus the determinant sees symbolic weights and common stability, but not translations or orbit locations, even inside the strongly separated class.

#### Progress over the prior gate.

C119 had a global trace-class owner but no nontrivial cycles; C123 had periodic words and a finite degree-four moment operator but no all-period orbit-derived determinant. C124 places nontrivial primitive cycles and a global trace-class Fredholm owner in the same frozen source. Translation blindness is the exact remaining internal limitation, not evidence of a target match.

# Validation and Route-A boundary

The producer, independent checker (53 assertions), fresh SymPy reconstruction (31 checks, including explicit polynomial finite sections), byte replay, and all 17 hostile mutations pass. No external source or tolerance is used.

The strict tuple is $(\texttt{A1\_WEAK},\texttt{A2\_FAIL},\texttt{A3\_FAIL},
\texttt{A4\_FAIL})$, overall `ROUTE_A_EXPLORATORY`. A2 fails because no frozen target divisor is compared; A3 and A4 likewise have no target global structure or natural lift. Route B is not authorized. We claim no prime-like correspondence, arithmetic/local data, Euler factors, root numbers, automorphy, Hilbert--Pólya operator, or Riemann-zero relation. The literal firewall is `NO_BAD_EULER_OR_ROOT_NUMBER`.
