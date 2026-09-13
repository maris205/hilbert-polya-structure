---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-wilson-cycle-popping-weighted-ust-route-a"
canonical_tex: "henon_dynamics/henon_wilson_cycle_popping_weighted_ust_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_wilson_cycle_popping_weighted_ust_route_a/paper/main.pdf"
source_sha256: "a730404bd9fb4d8ee5c95fea469b09e3f7ebb94228f3994d5e4490eec7665c84"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# From Abelian Cycle Popping to Every Transfer-Current Minor

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_wilson_cycle_popping_weighted_ust_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_wilson_cycle_popping_weighted_ust_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_wilson_cycle_popping_weighted_ust_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_wilson_cycle_popping_weighted_ust_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  On a finite connected loopless conductance multigraph, we prove one convention-complete theorem linking infinite-stack cycle popping, Wilson's loop-erased random walks, weighted spanning trees, the matrix-tree normalization, and all transfer-current edge determinants. A local diamond and strip argument makes every legal cycle rule terminate with identical pop counts once one terminating order exists; Wilson exploration supplies such an order almost surely. A labelled last-exit formula then telescopes killed Green-function cofactors to give the exact weighted tree law. Finally, multivariate conductance perturbations yield every joint edge-inclusion minor, not only effective-resistance marginals. The statement includes the singleton, already-a-tree, distinctly labelled parallel-edge, orientation, and root-change boundaries. Exact evidence checks all 772 connected labelled simple graphs through five vertices, all 8,136 graph--tree pairs and 55,895 edge-subset events, plus 24 weighted multigraphs and 12,754 finite stack tables. Enumeration is only a reproducibility receipt: the proof owns the infinite-stack result. No arithmetic or target-zeta interpretation is made.
author:
- Anonymous
date: 3 September 2026
title: 'From Abelian Cycle Popping to Every Transfer-Current Minor'
```

## Markdown 正文

#### Revision certificate.

Core stochastic closure: abelian stacks, Wilson paths, and the weighted law. Determinantal boundary closure: all transfer-current minors and edge conventions. Route firewall receipt: exhaustive exact evidence, ownership, and nonclaims.

# Model and theorem

Let $G=(V,E)$ be a finite connected loopless undirected multigraph. Parallel edges remain distinctly labelled and have conductances $c_e>0$. Freeze one orientation per edge, $$b_e=\delta_{\mathrm{tail}(e)}-\delta_{\mathrm{head}(e)},\qquad
 B=(b_e)_{e\in E},\quad C=\operatorname{diag}(c_e),\quad L=BCB^{\mathsf T}.$$ Fix a root $r$ and put $c(v)=\sum_{e\ni v}c_e$. At each $v\ne r$ place an independent infinite stack $(X_{v,j})_{j\ge1}$ with $\mathbb P(X_{v,j}=e)=c_e/c(v)$ for $e\ni v$. Its visible card points from $v$ across $e$. A legal update selects a visible directed cycle and advances exactly the stack pointers on that cycle.

Let $L^+$ be the Moore--Penrose pseudoinverse and define $$H_{ef}=c_f b_e^{\mathsf T}L^+b_f,\qquad
 K_{ef}=\sqrt{c_ec_f}\,b_e^{\mathsf T}L^+b_f.                 \tag{1}$$ $H$ is convenient over rational conductances; $K$ is symmetric. They are diagonally similar and have the same principal minors.

[\[thm:main\]]{#thm:main label="thm:main"} For every fixed stack realization for which one finite legal pop sequence is terminal, all legal cycle choices terminate with the same vertexwise pop counts and terminal arborescence. Under the independent stack law this happens almost surely, and a canonical legal order is Wilson chronological loop erasure for any ordering of $V\smallsetminus\{r\}$.

The unoriented output satisfies, for every labelled spanning tree $T$, $$\mathbb P(\mathcal T=T)=\frac{\prod_{e\in T}c_e}{Z_c},\qquad
 Z_c:=\sum_{S\text{ tree}}\prod_{e\in S}c_e=\det L^{(r)},     \tag{2}$$ where $L^{(r)}$ deletes the root row and column. For every set of pairwise distinct labelled edges $S=\{e_1,\ldots,e_k\}$, $$\mathbb P(S\subseteq\mathcal T)=\det(H_{e_i e_j})_{i,j=1}^k
                    =\det(K_{e_i e_j})_{i,j=1}^k.            \tag{3}$$ Equations (2)--(3) are independent of the root and frozen orientations.

# Abelian stacks and Wilson equivalence

[\[lem:abelian\]]{#lem:abelian label="lem:abelian"} If a stack configuration admits a finite terminal legal sequence, then every legal sequence is finite and has the same pop-count vector and terminal state.

Two visible directed cycles that share a vertex coincide, since every nonroot vertex has one visible outgoing arrow. Distinct visible cycles are therefore vertex-disjoint; popping either leaves the other visible, and the two pointer increments commute.

Fix a terminal list $\alpha=(C_1,\ldots,C_m)$ and any cycle $D$ visible at the initial state. Unless $D=C_1$, the cycles are disjoint, so $D$ commutes past $C_1$ and remains visible. Continue along $\alpha$. It must eventually equal one of its cycles; otherwise $D$ would remain visible after the terminal list. Thus $D$ can be moved to the front of a terminal list without changing any pointer increment. Induction on $m$, after each arbitrary first choice, shows that every legal list has the same finite multiset of pointer increments and terminal state. An acyclic functional digraph with only $r$ lacking an outgoing arrow is an arborescence toward $r$: every forward orbit ends at $r$, or else repeats and makes a cycle.

Start with the built tree $\{r\}$. From the first ordered vertex outside it, follow visible arrows. When the path revisits a vertex, its intervening arrows are a visible cycle; pop them and retain the chronological loop erasure. Upon first hitting the built tree, adjoin the retained path and continue. Newly exposed cards are fresh conductance transitions, so each exploration is the random walk on the finite irreducible graph stopped on a nonempty set. It hits that set in finite time almost surely. Finitely many explorations give a terminal legal list, card for card equal to Wilson's algorithm. Lemma [\[lem:abelian\]](#lem:abelian){reference-type="ref" reference="lem:abelian"} promotes this one almost surely finite order to every legal rule.

# Last exits, telescoping, and the weighted law

Let $$P(x,y)=\sum_{e:x\leftrightarrow y}\frac{c_e}{c(x)}.$$ For a target set $A$, take a labelled self-avoiding path $\gamma=(x_0,e_0,x_1,\ldots,e_{q-1},x_q)$ with $x_q\in A$ and earlier vertices outside $A$. Set $D_i=V\smallsetminus(A\cup\{x_0,\ldots,x_{i-1}\})$ and $G_D=(I-P_D)^{-1}$.

[\[lem:last\]]{#lem:last label="lem:last"} $$\mathbb P(\operatorname{LE}=\gamma)=\prod_{i=0}^{q-1}
 G_{D_i}(x_i,x_i)\frac{c_{e_i}}{c(x_i)}.                     \tag{4}$$

Before the retained step from $x_i$, sum over all excursions that start and return to $x_i$ without leaving $D_i$. Their total mass is the diagonal killed Green entry. The next retained labelled edge has probability $c_{e_i}/c(x_i)$. The strong Markov property after that last exit repeats the argument in $D_{i+1}$, proving (4).

Cramer's rule gives $$G_D(x,x)=\frac{\det(I-P_{D\smallsetminus\{x\}})}{\det(I-P_D)}. \tag{5}$$ The factors (5) telescope along each Wilson path and then across all phases, from $D=V\smallsetminus\{r\}$ to the empty set. A fixed tree oriented toward $r$ uses one labelled edge $e(v)$ from each $v\ne r$, hence $$\mathbb P(\mathcal T=T)=
 \frac{\prod_{v\ne r}c_{e(v)}/c(v)}{\det(I-P^{(r)})}
 =\frac{\prod_{e\in T}c_e}{\det L^{(r)}},                  \tag{6}$$ because $I-P^{(r)}=D_r^{-1}L^{(r)}$ for $D_r=\operatorname{diag}(c(v):v\ne r)$. The output is almost surely exactly one tree. Summing (6) over all labelled trees proves both the normalization and the matrix-tree identity in (2); neither was inserted as an assumption.

\>0

# All transfer-current minors

Delete the root row of $B$ to obtain $R$, and put $A=RCR^{\mathsf T}=L^{(r)}$. If $b$ has coordinate sum zero, solutions of $Lx=b$ differ only by constants. Incidence vectors annihilate constants, so $$b_e^{\mathsf T}L^+b_f=R_e^{\mathsf T}A^{-1}R_f,
 \qquad H=R^{\mathsf T}A^{-1}RC.                            \tag{7}$$ This also proves that (7) is independent of the deleted root.

Introduce one commuting indeterminate $t_e$ per labelled edge and replace $c_e$ by $c_e(1+t_e)$. From (2), the normalized partition polynomial is $$\frac{Z(c_e(1+t_e))}{Z(c_e)}
 =\sum_T\mathbb P(\mathcal T=T)\prod_{e\in T}(1+t_e).                   \tag{8}$$ The matrix determinant lemma and Sylvester's determinant identity give the second representation $$\frac{\det(A+RC\operatorname{diag}(t)R^{\mathsf T})}{\det A}
 =\det(I+\operatorname{diag}(t)R^{\mathsf T}A^{-1}RC)
 =\det(I+\operatorname{diag}(t)H).                                       \tag{9}$$ The coefficient of $\prod_{e\in S}t_e$ in (8) is $\mathbb P(S\subseteq\mathcal T)$; its coefficient in (9) is the principal minor $\det H_S$. This proves (3) for every $k$ at once. If $D=\operatorname{diag}(\sqrt{c_e})$, then $K=DHD^{-1}$, while reversing frozen edge orientations conjugates either kernel by a diagonal sign matrix. Principal determinants are unchanged.

#### Boundary closure.

For a singleton, $E=\varnothing$, the empty tree and empty determinant both have value one. If $G$ is already a tree, it is the only output and the rank-$|E|$ projection $K$ is the identity. Parallel labels retain separate conductances; their incidence columns agree up to sign, so a minor containing two parallel edges vanishes, exactly as simultaneous tree inclusion does. Changing the root changes stack directions but not (2), (7), or any unoriented event. Loops and nonpositive conductances lie outside the model.

\>1

# Exact receipt, ownership, and scope

The exact ledger covers all 772 connected labelled simple graphs on at most five vertices, all 8,136 graph--tree pairs, and all 55,895 edge-subset events. It adds 24 positive-integer weighted multigraphs containing labelled parallel edges: 846 weighted trees and 7,032 further subset events. A separate all-schedule audit explores 12,754 depth-two stack tables over every root of every connected labelled simple graph through four vertices; every terminal table has one pop-count vector and agrees with canonical Wilson exploration. Producer-independent reconstruction, symbolic triangle/parallel/$K_4$ identities, isolated byte replay, repaired-hash mutation, and optimized-Python refusal close the executable boundary. These finite checks audit conventions, not almost-sure termination.

Wilson owns the LERW/cycle-popping lineage; Burton--Pemantle own the transfer-impedance theorem lineage; Kirchhoff and Chaiken own the determinant lineage. This source-local reconstruction claims no priority. C176 concerns sandpile translations, and C181 deterministic rotor-router torsors; neither owns independent resampling stacks plus the weighted UST edge process.

The Route-A tuple is $(\mathrm{A0\_FAIL},\mathrm{A1\_FAIL},
\mathrm{A2\_FAIL},\mathrm{A3\_FAIL},\mathrm{A4\_FORMAL\_HINT})$, overall rejected. The finite projection in (1) is only a formal source hint. The tree partition polynomial is not a target Euler factor or target zeta; no target local data, root number, automorphy, divisor, functional equation, zero match, RH claim, Hilbert--Pólya operator, or Route B invocation occurs.

#### Verified source lineage.

D. B. Wilson, "Generating random spanning trees more quickly than the cover time," STOC (1996), 296--303, [doi:10.1145/237814.237880](https://doi.org/10.1145/237814.237880). R. Burton and R. Pemantle, "Local Characteristics, Entropy and Limit Theorems for Spanning Trees and Domino Tilings Via Transfer-Impedances," *Ann. Probab.* 21 (1993), 1329--1371, [doi:10.1214/aop/1176989121](https://doi.org/10.1214/aop/1176989121). G. Kirchhoff, *Ann. Phys.* 148 (1847), 497--508, [doi:10.1002/andp.18471481202](https://doi.org/10.1002/andp.18471481202). S. Chaiken, *SIAM J. Algebraic Discrete Methods* 3 (1982), 319--329, [doi:10.1137/0603033](https://doi.org/10.1137/0603033). R. Lyons and Y. Peres, *Probability on Trees and Networks*, CUP (2016), [official author page](https://rdlyons.pages.iu.edu/prbtree/).
