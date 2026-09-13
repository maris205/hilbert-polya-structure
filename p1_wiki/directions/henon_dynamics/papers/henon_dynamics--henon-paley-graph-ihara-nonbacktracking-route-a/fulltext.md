---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-paley-graph-ihara-nonbacktracking-route-a"
canonical_tex: "henon_dynamics/henon_paley_graph_ihara_nonbacktracking_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_paley_graph_ihara_nonbacktracking_route_a/paper/main.pdf"
source_sha256: "c6047fe91ba7fb53d923b25033fdcb57b5fe43be050cdf3b28248424259d6e48"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Paley Graphs as Exact Ihara Nonbacktracking Dynamics

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_paley_graph_ihara_nonbacktracking_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_paley_graph_ihara_nonbacktracking_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_paley_graph_ihara_nonbacktracking_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_paley_graph_ihara_nonbacktracking_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For every odd prime power $q\equiv1\pmod4$, we give one closed algebraic description of the Paley graph and its directed nonbacktracking dynamics. The graph is strongly regular with parameters $(q,(q-1)/2,(q-5)/4,(q-1)/4)$; additive characters give its complete three-point adjacency spectrum. A self-contained incidence-matrix elimination then produces the full Bass factorization, every Hashimoto eigenvalue, every power trace, and every oriented primitive-cycle count. The small face $q=5$ is the five-cycle and has exactly two oriented prime circuits of length five. Exact computations reconstruct 13 fields, 25,901 adjacency cells, and 369,848 legal edge transitions. These are source-graph facts: the finite-field label is not a rational-prime orbit law, and the Ihara product is not a target Euler factor or an RH assertion.
author:
- Anonymous
date: 3 September 2026
title: Paley Graphs as Exact Ihara Nonbacktracking Dynamics
```

## Markdown 正文

#### Revision certificate.

Frozen Paley graph and character spectrum. Bass spectrum and primitive-cycle closure. Finite-field representation and Route-A boundary.

# Model and theorem

Let $q$ be an odd prime power with $q\equiv1\pmod4$. Extend the quadratic character $\chi$ of $\mathbb F_q$ by $\chi(0)=0$. The Paley graph $P(q)$ joins distinct $x,y$ precisely when $\chi(x-y)=1$. Put $$k=\frac{q-1}{2},\qquad m=\frac{qk}{2},\qquad
 r=\frac{-1+\sqrt q}{2},\qquad s=\frac{-1-\sqrt q}{2}.$$ Its directed-edge matrix is $$B_{(x,y),(y,z)}=1\quad\Longleftrightarrow\quad y\sim z\ \text{and }z\ne x.$$ Prime cycles are oriented and identified under cyclic shift, but not under reversal.

[\[thm:main\]]{#thm:main label="thm:main"} The graph $P(q)$ is connected and strongly regular with parameters $$\left(q,k,\frac{q-5}{4},\frac{q-1}{4}\right),$$ and adjacency spectrum $k^1,r^k,s^k$. Its nontrivial spectrum obeys the source Ramanujan bound $\max(|r|,|s|)\leq2\sqrt{k-1}$. Moreover $$\begin{aligned}
 \det(I-uB)={}&(1-u^2)^{m-q}(1-ku+(k-1)u^2)\notag\\
 &\mathrel{}\times(1-ru+(k-1)u^2)^k(1-su+(k-1)u^2)^k.\label{eq:bass}\end{aligned}$$ Thus every eigenvalue of $B$ is a root of $z^2-\lambda z+(k-1)$ for $\lambda\in\{k,r,s\}$, with the adjacency multiplicity, together with $+1$ and $-1$ each $m-q$ additional times. If $N_n=\operatorname{Tr}(B^n)$ and $\pi_n$ counts oriented prime cycles of length $n$, then $$N_n=\sum_{d\mid n}d\pi_d,\qquad
 \pi_n=\frac1n\sum_{d\mid n}\mu(d)N_{n/d},\qquad
 Z_{P(q)}(u)=\det(I-uB)^{-1}.$$ For $q=5$, the excess $m-q$ is zero and $\pi_5=2$.

# Character proof

Because $\chi(-1)=1$, adjacency is symmetric and every vertex has the $k$ nonzero squares as increments. Let $J(t)=(1+\chi(t)-\delta_0(t))/2$. For $a\ne0$, expansion of the two indicators and the elementary identity $\sum_t\chi(t)\chi(t-a)=-1$ give $$\sum_{t\in\mathbb F_q}J(t)J(t-a)=\frac{q-3-2\chi(a)}4.$$ This is $(q-5)/4$ on an edge and $(q-1)/4$ off an edge.

Fix a nontrivial additive character $\psi$ of $\mathbb F_p$ and write $\psi_b(x)=\psi(\operatorname{Tr}_{\mathbb F_q/\mathbb F_p}(bx))$. Convolution by the nonzero squares diagonalizes on these characters. The trivial eigenvalue is $k$, while for $b\ne0$ $$\lambda_b=\frac{-1+\chi(b)G}{2},\qquad
 G=\sum_t\chi(t)\psi(\operatorname{Tr}_{\mathbb F_q/\mathbb F_p}(t)),\qquad
 G^2=\chi(-1)q=q.$$ The sign of $G$ can exchange the labels $r,s$ but not their multiset. Half of the nonzero $b$ have each sign, proving $k^1,r^k,s^k$. Since the degree eigenvalue of a regular undirected graph has multiplicity equal to its number of connected components, $P(q)$ is connected. Finally, $$\max(|r|,|s|)=\frac{\sqrt q+1}{2}\leq\sqrt{2(q-3)}=2\sqrt{k-1}.$$ After squaring this is $2\sqrt q\leq7q-25$; the difference is increasing for $q\geq5$ and equals $10-2\sqrt5>0$ at five. This is only the Ramanujan bound for the source graph.

\>0

# Bass elimination and the entire edge spectrum

Let $S,T$ be tail and head incidence matrices from vertices to directed edges, and let $R$ reverse a directed edge. With our indexing, $$B=T^{\!*}S-R,\quad R^2=I,\quad SR=T,\quad ST^{\!*}=A,
 \quad SS^{\!*}=kI.$$ Factor $I-uB=(I+uR)[I-u(I+uR)^{-1}T^{\!*}S]$. Since $(I+uR)^{-1}=(I-uR)/(1-u^2)$, the identity $\det(I-XY)=\det(I-YX)$ reduces the second determinant to vertex space. Multiplication by $1-u^2$ and the displayed incidence identities give $I-uA+(k-1)u^2I$. Finally, $R$ is a direct sum of $m$ swaps, so $$\det(I-uB)=(1-u^2)^{m-q}\det(I-uA+(k-1)u^2I).$$ Substituting the adjacency spectrum proves [\[eq:bass\]](#eq:bass){reference-type="eqref" reference="eq:bass"}. Its degree is $2(m-q)+2q=2m$, hence no algebraic eigenvalue or multiplicity is omitted.

The entry $(B^n)_{e,e}$ counts based, closed, tailless nonbacktracking walks. A prime cycle of length $d\mid n$ contributes its $d$ possible base edges to the $n/d$ repetition. This proves $N_n=\sum_{d\mid n}d\pi_d$; Möbius inversion gives $\pi_n$. The formal trace--log identity $$-\log\det(I-uB)=\sum_{n\ge1}\frac{\operatorname{Tr}(B^n)}n u^n$$ gives the source Ihara zeta and its prime-cycle product. When $q=5$, the nonzero squares are $\{1,4\}$, so the graph is $C_5$. A nonbacktracking walk must preserve direction; its two orientations give $\pi_5=2$.

\>1

# Canonical evidence and scope

For extension fields, evidence represents elements by base-$p$ coefficient vectors modulo the lexicographically first monic irreducible polynomial, with coefficients ordered low to high. This choice only labels vertices; the theorem is invariant under field isomorphism. The exact grid $$5,9,13,17,25,29,37,41,49,53,61,73,81$$ contains 240 residue cells, 25,901 reconstructed adjacency cells, 12,704 directed edges, 369,848 legal transitions, and 156 trace/primitive rows. Independent field reconstruction, symbolic trace--log checks, isolated byte replay, and repaired-hash mutations protect the finite certificate. The proof above, rather than extrapolation from this grid, owns the universal theorem.

The closest local owners concern Heisenberg voltage graphs, cyclic quadratic Gauss sums, projective finite-field Möbius permutations, and finite-field Chebyshev functional graphs. None owns the quadratic-residue Cayley graph together with its complete nonbacktracking ledger.

The finite-field character is an intrinsic but weak arithmetic relation. Primitive cycles and repetitions are complete, so A1 passes analytically. No logarithmic-prime roof, target determinant, target divisor, functional equation, root number, automorphy statement, zero match, or Hilbert--Pólya operator follows. The Paley Ramanujan bound and Ihara product retain only their source-graph meanings. Route B is not invoked.

# Verified sources {#verified-sources .unnumbered}

R. E. A. C. Paley, "On Orthogonal Matrices," *J. Math. Phys.* 12 (1933), 311--320. DOI: 10.1002/sapm1933121311.

\>0 K. Hashimoto, "Zeta Functions of Finite Graphs and Representations of $p$-Adic Groups," *Adv. Stud. Pure Math.* 15 (1989), 211--280. DOI: 10.1016/B978-0-12-330580-0.50015-X.

H. Bass, "The Ihara--Selberg zeta function of a tree lattice," *Int. J. Math.* 3(6) (1992), 717--797. DOI: 10.1142/S0129167X92000357.
