---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-finite-abelian-power-map-route-a"
canonical_tex: "henon_dynamics/henon_finite_abelian_power_map_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_finite_abelian_power_map_route_a/paper/main.pdf"
source_sha256: "41f48fb7fb15f74ebeb04b834a5d96deb7d30903b83ee829d3334c97d33e7675"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Finite Abelian Power Maps: Complete Functional Graphs, Zeta Products, and Koopman Jordan Atlases

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_finite_abelian_power_map_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_finite_abelian_power_map_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_finite_abelian_power_map_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_finite_abelian_power_map_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For every finite abelian group $G$ and integer $d\geq1$, we classify the entire functional graph of $g\mapsto g^d$. A canonical prime-support split separates a periodic automorphism from a nilpotent transient factor. It gives all fixed and primitive counts and the complete finite dynamical zeta product. \>0 Every periodic vertex receives the same explicitly specified rooted in-tree, including every tail layer and its saturation height; the singular constant map $d=0$ is closed separately. \>1 For composition on the full function space we further determine every power rank, every zero Jordan-block size, and the characteristic polynomial. The theorem is parameter-uniform; exact finite enumeration is used only as a replayable regression certificate.
author:
- 'Route-A source-local certificate HCS-C264'
date: 31 August 2026
title: |
  Finite Abelian Power Maps:\
  Complete Functional Graphs, Zeta Products, and Koopman Jordan Atlases
```

## Markdown 正文

trailerid \[\<C2642026083100000000000000000000\>\<C2642026083100000000000000000000\>\]

# Prime-support splitting

Write the group additively as $$G=\bigoplus_{i=1}^r C_{n_i},\qquad T_d(x)=dx.$$ For $d\geq1$, factor $n_i=a_i b_i$ so that $(a_i,d)=1$ and every prime divisor of $b_i$ divides $d$. Thus $(a_i,b_i)=1$. Put $$A=\bigoplus_i C_{a_i},\qquad B=\bigoplus_i C_{b_i}.$$ The Chinese remainder theorem identifies $G=A\times B$. Multiplication by $d$ is an automorphism on $A$, whereas every element of $B$ reaches zero. Functional graphs of power maps over finite groups provide the established lineage for this decomposition [@QR]; the theorem below is proved locally, and no literature-priority claim is made.

The periodic set of $T_d$ is exactly $A\times\{0\}$. For every $n\geq1$, $$F_n:=|\operatorname{Fix}(T_d^n)|=\prod_i\gcd(d^n-1,a_i).                 \tag{1}$$ The numbers of exact-period points and cycles are respectively $$P_m=\sum_{e\mid m}\mu(m/e)F_e,\qquad C_m=P_m/m.           \tag{2}$$ In particular, only finitely many $C_m$ are nonzero and $$\zeta_{T_d}(t):=\exp\!\left(\sum_{n\geq1}F_n\frac{t^n}{n}\right)
 =\prod_{m\geq1}(1-t^m)^{-C_m}.                            \tag{3}$$

If $(a,b)$ is periodic, then $d^k b=b$ for some $k>0$. But a power of $d$ annihilates $B$, so $b=0$; conversely the finite automorphism on $A$ makes every $(a,0)$ periodic. On $C_{a_i}$ the equation $(d^n-1)x=0$ has $\gcd(d^n-1,a_i)$ solutions, proving (1). Partitioning $F_m$ by exact period and applying Möbius inversion gives (2). Expanding $-\log(1-t^m)$ and collecting the coefficient of $t^n/n$ proves (3).

\>0

# Uniform transient trees and boundary faces

Define $$K_j=\left|\ker(T_d^j|_B)\right|=\prod_i\gcd(d^j,b_i),\qquad K_0=1.$$ If $b\in B$ first reaches zero after $j$ steps, then its exact tail is $j$. For each periodic vertex, invertibility on $A$ supplies a unique $A$-coordinate at every backward step. Hence its attached rooted tree is canonically the tree of $b\mapsto db$ on $B$, and its depth-$j$ population is $$L_j=K_j-K_{j-1}\quad(j\geq1),\qquad L_0=1.                \tag{4}$$ This specifies the complete graph: cycles are given by (2), and every cycle vertex is decorated by the same explicitly defined $B$-tree. The maximal tail height is $$h=\max_{p\mid d}\left\lceil
 \frac{\max_i v_p(b_i)}{v_p(d)}\right\rceil,              \tag{5}$$ with an empty maximum interpreted as zero.

The identity face $d=1$ lies inside the theorem: $A=G$, $B=0$, every point is fixed, and there is no transient sector. The exponent $d=0$ is kept outside the prime-support notation. It is the constant map to the identity, with one fixed point and $|G|-1$ vertices of exact tail one; its source zeta is $(1-t)^{-1}$.

\>1

# Full-function Koopman Jordan atlas

Let $U:\mathbb C^G\to\mathbb C^G$ be the composition operator $(Uf)(x)=f(T_d x)$. Distinct rows of its zero--one matrix are indexed by the distinct values of $T_d$, so $$\operatorname{rank}(U^j)=R_j:=|\operatorname{im}T_d^j|
 =|A|\prod_i\frac{b_i}{\gcd(d^j,b_i)}.                   \tag{6}$$ The ranks stabilize at $|A|$. For a nilpotent Jordan block of size $s$, the rank loss from power $j-1$ to $j$ is one exactly when $s\geq j$. Taking a second difference therefore gives the number of zero blocks of exact size $j$: $$Z_j=R_{j-1}-2R_j+R_{j+1}.                                \tag{7}$$ The recurrent quotient is a disjoint union of the cycles counted in (2), so its permutation characteristic factors are $\lambda^m-1$. Consequently the entire operator, including its transient algebraic multiplicity, satisfies $$\det(\lambda I-U)=\lambda^{|G|-|A|}
 \prod_{m\geq1}(\lambda^m-1)^{C_m}.                      \tag{8}$$ For $d=0$, $U^2=U$; it is diagonalizable with eigenvalues $1$ once and zero $|G|-1$ times. In general $U$ need not be normal or unitary; only the bijective face $B=0$ is a permutation operator.

# Exact certificate and Route-A boundary

The frozen corpus crosses 34 invariant-factor group types with $d=0,\ldots,18$: 646 maps and 21,280 directly enumerated case-elements. It stores 1,320 fixed-point cells, 933 cycle factors, 1,132 tail layers, and 485 nonzero zero-Jordan entries. An independent implementation closes 202,656 assertions without importing the producer. SymPy closes 1,029 exact characteristic-polynomial and rank checks on 220 full matrices; fresh byte replay passes, and repaired-hash mutations are rejected 33/33. These are regression receipts, not a finite-census proof of the theorem.

This certificate concerns a finite source dynamical system. It supplies no arithmetic local datum, bad Euler factor, root number, automorphy statement, target divisor, functional equation, or Hilbert--Pólya operator. Under `NO_BAD_EULER_OR_ROOT_NUMBER`, its frozen Route-A tuple is $$\begin{split}
(&\texttt{A0\_WEAK\_ARITHMETIC\_RELATION},
\texttt{A1\_PASS\_ANALYTIC},\texttt{A2\_FAIL},\\
&\texttt{A3\_FAIL},\texttt{A4\_FORMAL\_HINT}).
\end{split}$$ The verdict is `ROUTE_A_PARTIAL`; Route B is disabled. The Koopman matrix is a formal source operator, not a target spectral realization. We claim ownership only of this workspace certificate, not literature priority.

9 C. Qureshi and L. Reis, *On the functional graph of the power map over finite groups*, *Discrete Mathematics* **346** (2023), 113393, [doi:10.1016/j.disc.2023.113393](https://doi.org/10.1016/j.disc.2023.113393).
