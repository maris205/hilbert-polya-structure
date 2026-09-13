---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-finite-field-chebyshev-functional-graph-route-a"
canonical_tex: "henon_dynamics/henon_finite_field_chebyshev_functional_graph_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_finite_field_chebyshev_functional_graph_route_a/paper/main.pdf"
source_sha256: "65fe3b9c9d54b3dc36cb4adc859beb4913cfc38986371f2f3b241121edb7eff3"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Finite-Field Chebyshev Dynamics: Ramified Functional Graphs, Zeta, and Koopman Jordan Data

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_finite_field_chebyshev_functional_graph_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_finite_field_chebyshev_functional_graph_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_finite_field_chebyshev_functional_graph_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_finite_field_chebyshev_functional_graph_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For every prime power $q$ and integer $d\geq1$, we classify the complete functional graph of the non-normalized Chebyshev map $T_d$ on $\mathbb F_q$. The graph is the inversion quotient of power maps on cyclic tori of orders $q-1$ and $q+1$, with their ramified intersection glued exactly. This gives every fixed and primitive count and the finite source zeta. \>0 Prime-support splitting further gives the full tail filtration, all image ranks, every zero Jordan-block size, and the full-function Koopman characteristic polynomial, without pretending that branch-folded trees are uniform. \>1 An independent exact corpus includes nonprime fields and characteristic two; it is regression evidence rather than the proof.
author:
- 'Route-A source-local certificate HCS-C269'
date: 1 September 2026
title: |
  Finite-Field Chebyshev Dynamics:\
  Ramified Functional Graphs, Zeta, and Koopman Jordan Data
```

## Markdown 正文

trailerid \[\<C2692026090100000000000000000000\>\<C2692026090100000000000000000000\>\]

# Two cyclic covers and ramified gluing

Normalize the first-kind Dickson--Chebyshev family by $$T_0(X)=2,\quad T_1(X)=X,\quad T_d(X)=XT_{d-1}(X)-T_{d-2}(X).$$ Then $T_d(z+z^{-1})=z^d+z^{-d}$ in every characteristic. In $\mathbb F_{q^2}^{*}$ put $$G_-:=\mathbb F_q^*,\qquad G_+:=\ker N_{\mathbb F_{q^2}/\mathbb F_q},\qquad
 \eta(z):=z+z^{-1}.$$ The cover orders are $q-1,q+1$, and $|G_-\cap G_+|=\gcd(2,q-1)$. For $u\mid q-1$, $v\mid q+1$, define $$\mathcal Q_q(u,v)=\frac{u+\gcd(2,u)}2+\frac{v+\gcd(2,v)}2-1
 -\mathbf 1_{q\ {\rm odd},\,2\mid u,\,2\mid v}.                 \tag{1}$$ This is the size of the two inversion-quotient subgroups after subtracting their common $+1$ branch and, when present twice, their common $-1$ branch.

Take disjoint functional graphs of $z\mapsto z^d$ on $G_-$ and $G_+$, identify $z\sim z^{-1}$ in each, and glue the two images of every element of $G_-\cap G_+$. The induced graph is conjugate through $\eta$ to the complete functional graph of $T_d:\mathbb F_q\to\mathbb F_q$.

For $D=d^n$ and $N\in\{q-1,q+1\}$ set $$s_N(D)=\gcd(D-1,N)+\gcd(D+1,N)-\gcd(D-1,D+1,N),$$ $$i_N(D)=1+\mathbf 1_{2\mid N,\,D\ {\rm odd}}.$$ Then $$F_n:=|\operatorname{Fix}(T_d^n)|=\sum_{N=q-1,q+1}\frac{s_N(D)+i_N(D)}2
 -1-\mathbf 1_{q\ {\rm odd},\,D\ {\rm odd}}.                  \tag{2}$$ Thus exact-period points and cycles are $$E_m=\sum_{e\mid m}\mu(m/e)F_e,\qquad C_m=E_m/m,          \tag{3}$$ and $$\zeta_{T_d}(t)=\exp\!\left(\sum_{n\geq1}F_n\frac{t^n}{n}\right)
 =\prod_{m\geq1}(1-t^m)^{-C_m}.                           \tag{4}$$

The roots of $Z^2-xZ+1$ are inverse. If they are not in $\mathbb F_q$, Frobenius exchanges them, so $z^q=z^{-1}$ and they lie in $G_+$. Hence $\eta$ is surjective and has precisely the stated inversion fibres and glued intersection. The Chebyshev identity intertwines every directed edge.

Upstairs, a fixed lift obeys $z^D=z$ or $z^D=z^{-1}$. The union of these two cyclic kernels has size $s_N(D)$. Burnside adds its $i_N(D)$ inversion-fixed lifts and divides by two. The last two terms of (2) remove the branch values counted on both covers. Möbius inversion proves (3), and expanding $-\log(1-t^m)$ proves (4).

The quotient statement is also the full tree theorem: regular inverse pairs fold together, while the one characteristic-two branch or two odd-characteristic branches retain their exceptional folded and glued trees. This construction follows the arbitrary-degree structural lineage of Qureshi--Panario [@QP]; Gassert treated the earlier prime-degree case [@Gassert]. Workspace ownership does not assert literature priority.

\>0

# Tail, image, and Koopman Jordan atlases

Factor $$q-1=a_-b_-,\qquad q+1=a_+b_+,$$ where $(a_\pm,d)=1$ and every prime of $b_\pm$ divides $d$. The periodic population and the population of tail at most $j$ are respectively $$P=\mathcal Q_q(a_-,a_+),\qquad
 H_j=\mathcal Q_q\!\left(a_-\gcd(d^j,b_-),
 a_+\gcd(d^j,b_+)\right).                                \tag{5}$$ Thus exact tail zero has size $P$, exact tail $j\geq1$ has size $H_j-H_{j-1}$, and the height is the least $h$ with $b_-\mid d^h$ and $b_+\mid d^h$. Equation (5), together with the labeled quotient theorem, retains each local tree rather than inferring a false uniform tree after ramification.

The image of the $j$th power has cover orders $$m_\pm(j)=\frac{q\pm1}{\gcd(d^j,q\pm1)},$$ so $$R_j:=|\operatorname{im}T_d^j|=\mathcal Q_q(m_-(j),m_+(j)). \tag{6}$$ These numbers stabilize at $P$.

Let $U:\mathbb C^{\mathbb F_q}\to\mathbb C^{\mathbb F_q}$ be composition, $(Uf)(x)=f(T_d(x))$. Distinct rows of $U^j$ correspond to distinct image values; hence $\operatorname{rank}U^j=R_j$. Second differences give the number of zero Jordan blocks of exact size $j$, $$Z_j=R_{j-1}-2R_j+R_{j+1}.                                \tag{7}$$ The recurrent quotient is the cycle permutation from (3), and therefore $$\det(\lambda I-U)=\lambda^{q-P}
 \prod_{m\geq1}(\lambda^m-1)^{C_m}.                      \tag{8}$$ The identity face $d=1$ is included. The separate $d=0$ face has $T_0=2$ (zero in characteristic two): one fixed point, $q-1$ points of tail one, zeta $(1-t)^{-1}$, ranks $q,1,1,\ldots$, and a diagonalizable composition operator with eigenvalues $1,0^{q-1}$.

\>1

# Exact evidence, distinction, and Route-A boundary

The frozen regression corpus crosses 11 exact field models with $d=0,\ldots,10$: 121 maps and 1,914 directly followed case-vertices. It contains 77 nonprime-field and 33 characteristic-two cases, 535 fixed cells, 203 cycle cells, 250 tail cells, 371 image-rank cells, and 121 nonzero zero-Jordan cells. A separately implemented checker closes 32,499 assertions. SymPy closes 311 exact matrix/rank identities across 64 maps; byte replay passes and repaired-hash mutations are rejected 41/41. The last attack replaces the $q=4,d=0$ modulus by a reducible polynomial after repairing the payload hash; the independent field-model gate still rejects it. None of these finite receipts is used as the all-parameter proof.

HCS-C264 concerns one abstract finite abelian power map and its product tree. Here two cyclic covers of different orders are folded by inversion and ramifiedly glued to produce a nonlinear polynomial on the field line. The special branch components are therefore part of the theorem, not erased by borrowing C264's uniform-tree language.

Finite-field provenance gives only a weak intrinsic arithmetic relation: no rational prime labels a primitive cycle and no $\log p$ clock emerges. The finite zeta in (4) is source-local. Although the composition operator in (8) is canonical on the finite function space, this supplies only a formal operator hint: it is generally neither unitary nor self-adjoint, and no self-adjoint realization is constructed. Under `NO_BAD_EULER_OR_ROOT_NUMBER`, the strict tuple is $$\begin{split}
(&\texttt{A0\_WEAK\_ARITHMETIC\_RELATION},
\texttt{A1\_PASS\_ANALYTIC},\texttt{A2\_FAIL},\\
&\texttt{A3\_FAIL},\texttt{A4\_FORMAL\_HINT}).
\end{split}$$ The verdict is `ROUTE_A_EXPLORATORY`; Route B is disabled. No arithmetic local datum, bad Euler factor, root number, automorphy, target divisor, functional equation, or Hilbert--Pólya operator is claimed.

9 C. Qureshi and D. Panario, *The graph structure of Chebyshev polynomials over finite fields and applications*, *Designs, Codes and Cryptography* **87** (2019), 393--416, [doi:10.1007/s10623-018-0545-7](https://doi.org/10.1007/s10623-018-0545-7). T. A. Gassert, *Chebyshev action on finite fields*, *Discrete Mathematics* **315--316** (2014), 83--94, [doi:10.1016/j.disc.2013.10.014](https://doi.org/10.1016/j.disc.2013.10.014).
