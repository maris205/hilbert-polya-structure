---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-graph-directed-phase-holonomy-route-a"
canonical_tex: "henon_dynamics/henon_graph_directed_phase_holonomy_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_graph_directed_phase_holonomy_route_a/paper/main.pdf"
source_sha256: "130d7fd72ab001e5185abf77aca789dec2f80b3c59ff900e5a7b67c7febcaeb0"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Frozen Phase Holonomy for a Graph-Directed Hénon Hardy--Fredholm Owner

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_graph_directed_phase_holonomy_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_graph_directed_phase_holonomy_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_graph_directed_phase_holonomy_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_graph_directed_phase_holonomy_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We freeze a fifth-root character of the integer branch translations in a strongly separated graph-directed affine Hénon system. The resulting weighted-composition operator is trace class on a direct sum of bidisc Hardy spaces. We prove its all-order trace law, Fredholm lattice product, and primitive-cycle expansion. Two assignments with the same unordered image centers and identical untwisted determinant have different twisted determinants, while the trivial character recovers the prior owner exactly. This is finite-character position sensitivity, not geometric reconstruction or a target-facing statement.
author:
- 'Route-A structural certificate C129'
title: 'Frozen Phase Holonomy for a Graph-Directed Hénon Hardy--Fredholm Owner'
```

## Markdown 正文

# Frozen system and primitive cycles

On three copies of $\mathbb D_3^2$, set $$A=\begin{pmatrix}3/16&-1/32\\1/4&0\end{pmatrix},\quad
\phi_j(z)=Az+(t_j,0),\quad t=(-2,0,2),$$ and freeze $$B=\begin{pmatrix}1&1&0\\1&0&1\\1&0&0\end{pmatrix},\quad
c=(1/2,1/3,1/5),\quad
\chi(m)=\zeta_5^m,$$ where $\zeta_5$ is primitive. The eigenvalues of $A$ are $1/8,1/16$. The two coordinate image radii are $21/32$ and $3/4$; the largest first-coordinate extent is $85/32<3$, and adjacent images have gap $2-2(21/32)=11/16>0$. Thus the branches are compactly contained and pairwise disjoint.

Every admissible cyclic word $w$ has affine linear part $A^{|w|}$ and one fixed point. Strong separation makes its itinerary unique, so primitive necklaces biject with primitive geometric cycles at all periods. The exact finite replay is

  period                  1   2   3    4    5    6    7     8
  --------------------- --- --- --- ---- ---- ---- ---- -----
  rooted closed words     1   3   7   11   21   39   71   131
  primitive cycles        1   1   2    2    4    5   10    15

For example, $012$ has phase points $$\tfrac1{19929}(38912,-1600)\to
\tfrac1{19929}(-32512,9728)\to
\tfrac1{19929}(-6400,-8128),$$ monodromy $A^3$, rational weight $1/30$, and holonomy $\zeta_5^{5}=1$.

# Twisted Hardy owner

Put $W_\chi=B\operatorname{diag}(c_j\chi(t_j))$ and define $$\mathcal H=\bigoplus_{i=0}^2H^2(\mathbb D_3^2),\qquad
(\mathcal L_\chi f)_i(z)=\sum_jB_{ij}c_j\chi(t_j)f_j(\phi_j(z)).$$ All branch images lie in a concentric bidisc with restriction ratio $\rho=85/96<1$. Total degree $m$ has multiplicity $m+1$, so the compact-interior factorization has summable majorant $\sum_{m\ge0}(m+1)\rho^m$. Hence $\mathcal L_\chi$ is trace class. Translations lower degree and leave the diagonal graded blocks unchanged. Consequently, for every $n\ge1$, $$\operatorname{Tr}\mathcal L_\chi^n=
\frac{\operatorname{Tr}W_\chi^n}
{(1-8^{-n})(1-16^{-n})}. \tag{1}$$ The numerator is the exact phase-weighted sum over rooted closed words. Trace class and (1) give the normally convergent entire product $$D_\chi(z)=\det(I-z\mathcal L_\chi)=
\prod_{r,s\ge0}\det(I-z8^{-r}16^{-s}W_\chi). \tag{2}$$ Indeed $\sum_{r,s}8^{-r}16^{-s}<\infty$. Grouping rooted words by primitive cycle and repetition yields $$\log D_\chi(z)=-\sum_{[\gamma]}\sum_{m\ge1}
\frac{(c_\gamma\chi(M_\gamma)z^{\ell_\gamma})^m}
{m\det(I-A^{m\ell_\gamma})},$$ where $M_\gamma$ is the translation sum around the word. These formulas are all-period; period eight is only a replay prefix.

# Exact controls and progress

To keep the two character tests logically separate, compute first in $\mathbb Q[\mathbb Z/5]$ with basis $e_0,\ldots,e_4$ and $e_ae_b=e_{a+b\bmod5}$. Primitive-character evaluation sends $e_k\mapsto\zeta_5^k$, whereas augmentation sends every $e_k\mapsto1$. Thus trivial degeneration is not obtained by the invalid substitution $\zeta_5=1$ inside the cyclotomic quotient. The source symbolic determinant is $$\det(I-zW_\chi)=1-\tfrac12\zeta_5^3z
-\tfrac16\zeta_5^3z^2-\tfrac1{30}z^3. \tag{3}$$ Now assign the same unordered centers to branches as $t'=(0,-2,2)$, leaving $A,B,c$ fixed. Strong separation and every untwisted trace and determinant remain identical, but $$\det(I-zW'_\chi)=1-\tfrac12z
-\tfrac16\zeta_5^3z^2-\tfrac1{30}z^3. \tag{4}$$ The linear coefficients of the full Hardy determinants are therefore $-(64/105)\zeta_5^3$ and $-64/105$. At the trivial character the phases in (3)--(4) become one, so both operators recover the C124 trace and determinant at every order. The control $012$ phase points also move exactly to $$\tfrac1{19929}(32512,-9728),\quad
\tfrac1{19929}(6400,8128),\quad
\tfrac1{19929}(-38912,1600).$$

#### Progress over the prior gate.

C124's entire determinant was blind to all branch translations. C129 retains its same all-period cycle owner and global trace-class space but distinguishes the displayed translation assignment through a frozen phase. The character sees only residues modulo five and branch assignment: replacing any $t_j$ by $t_j+5k_j$ leaves its phase unchanged, and changing which branch owns a center changes the weighted graph data. It therefore cannot recover complete geometry. The exact gain is position sensitivity under this frozen translation-lattice character, no more.

# Validation and Route-A boundary

The exact producer, independent checker (71 assertions), SymPy reconstruction (49 checks, finite sections through dimension 30), byte replay, and all 35 registered repaired-hash hostile mutations pass. The checker fixes the operator, all-order trace formula, positive control, complete progress record, and their key schemas. No external source or tolerance enters.

The strict tuple is $(\texttt{A1\_WEAK},\texttt{A2\_FAIL},
\texttt{A3\_FAIL},\texttt{A4\_FORMAL\_HINT})$, overall `ROUTE_A_EXPLORATORY`. The frozen $U(1)$ character is a formal phase lift, not a natural unitary, Hamiltonian, or metaplectic quantization. No target divisor or target global structure is compared. We claim no prime-like correspondence, arithmetic/local data, Euler factors, root numbers, automorphy, Hilbert--Pólya operator, or Riemann-zero relation. Route B is unauthorized; the literal firewall is `NO_BAD_EULER_OR_ROOT_NUMBER`.
