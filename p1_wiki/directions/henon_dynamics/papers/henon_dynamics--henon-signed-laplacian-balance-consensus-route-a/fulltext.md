---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-signed-laplacian-balance-consensus-route-a"
canonical_tex: "henon_dynamics/henon_signed_laplacian_balance_consensus_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_signed_laplacian_balance_consensus_route_a/paper/main.pdf"
source_sha256: "606f8e9cf39931bf8f5e54351a5f97d9650c3eb55253b900424937210b6ea6c0"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Static Signed Consensus on Every Finite Undirected Graph: Exact Semigroup Limits and the Full Pseudoforest Characteristic Polynomial

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_signed_laplacian_balance_consensus_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_signed_laplacian_balance_consensus_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_signed_laplacian_balance_consensus_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_signed_laplacian_balance_consensus_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We treat arbitrary finite, disconnected, static, undirected simple signed graphs with strictly positive edge weights. Structural balance determines the kernel of the signed Laplacian component by component, yielding an explicit orthogonal semigroup limit and an exact operator-norm convergence rate. The main combinatorial step expands every principal minor by components that are either one-root trees or root-free negative unicycles; summing root choices gives the complete characteristic polynomial, with a factor four for each negative unicycle. A bridge-plus-negative-triangle example disproves a tree-only minor formula, and a nonsymmetric example marks the directed boundary. Exhaustive exact checks cover all 760 signed simple graphs and all 11,894 root sets through four vertices, but the arbitrary-size positive-weight theorem is proved by quadratic forms and Cauchy--Binet, not by enumeration.
author:
- 'Route-A structural certificate C203'
title: |
  Static Signed Consensus on Every Finite Undirected Graph:\
  Exact Semigroup Limits and the Full Pseudoforest Characteristic Polynomial
```

## Markdown 正文

suppressoptionalinfo 611

**Keywords:** signed graph; structural balance; Altafini consensus; signed Laplacian; matrix-tree theorem; pseudoforest.

chinese-simplified

中文摘要

本文研究任意有限、可不连通、静态无向简单符号图，边权严格为正。结构平衡逐连通分量决定 符号拉普拉斯矩阵的核，从而得到显式正交半群极限和精确算子范数收敛率。进一步，本文用 恰含一个根的树与无根负单圈分量展开全部主子式，并由根集求和得到完整特征多项式； 每个负单圈贡献因子四。四阶以内的穷举只作实现校验，不代替任意规模的证明。

关键词：符号图；结构平衡；符号一致性；拉普拉斯矩阵；伪森林。

# Frozen graph and source ownership

Let $G=(V,E)$ be a finite undirected simple graph, not necessarily connected. Every edge $e=\{i,j\}$ has sign $\sigma_e\in\{\pm1\}$ and weight $w_e>0$. Choose any orientation and set $$b_e=\mathbf e_i-\sigma_e\mathbf e_j,\qquad
 B=[b_e]_{e\in E},\quad W=\operatorname{diag}(w_e),\quad L=BWB^{\mathsf T}.$$ Changing an edge orientation changes the corresponding column of $B$ at most by a sign and leaves $L$ unchanged. The frozen dynamics is $$\label{eq:flow} \dot x=-Lx.$$ Structural balance is classical [@Harary53]; the antagonistic-consensus context is due to Altafini [@Altafini13]; signed incidence/matrix-tree foundations and their erratum are recorded in [@Z82; @Z83]. We claim no priority for those results.

# Kernel, projector, and exact semigroup rate

For every $x\in\mathbb R^V$, $$\label{eq:qf}
 x^{\mathsf T}Lx=\sum_{e=ij}w_e(x_i-\sigma_e x_j)^2.$$ A connected component $C$ is balanced exactly when there is a switch vector $s_C\in\{\pm1\}^C$ satisfying $(s_C)_i=\sigma_{ij}(s_C)_j$ on every edge. An isolated vertex is balanced by this definition.

[\[thm:consensus\]]{#thm:consensus label="thm:consensus"} The nullity of $L$ equals the number of balanced connected components. Its orthogonal kernel projector is $$\label{eq:P}
 P=\sum_{C\ \mathrm{balanced}}\frac{s_Cs_C^{\mathsf T}}{|C|},$$ where vectors are extended by zero outside $C$. Moreover $$\label{eq:limit}
 e^{-tL}\longrightarrow P \qquad(t\to\infty).$$ If $L$ has positive spectrum and $\gamma=\min(\operatorname{spec}L\setminus
\{0\})$, then for every $t\ge0$, $$\label{eq:rate}
 \|e^{-tL}-P\|_2=e^{-\gamma t}.$$ If $L=0$, $P=I$ and the left side is identically zero.

Equation [\[eq:qf\]](#eq:qf){reference-type="eqref" reference="eq:qf"} shows that $x\in\ker L$ exactly when every edge constraint $x_i=\sigma_{ij}x_j$ holds. On a connected balanced component, propagation from one vertex gives precisely $\operatorname{span}\{s_C\}$. On an unbalanced component, propagation around a negative cycle gives $x_i=-x_i$, hence the only solution is zero. Disjoint supports make the normalized switch vectors orthonormal, proving [\[eq:P\]](#eq:P){reference-type="eqref" reference="eq:P"}. Orthogonal diagonalization of the real symmetric positive-semidefinite $L$ proves [\[eq:limit\]](#eq:limit){reference-type="eqref" reference="eq:limit"}; the largest remaining exponential multiplier is exactly $e^{-\gamma t}$, proving [\[eq:rate\]](#eq:rate){reference-type="eqref" reference="eq:rate"}.

Thus each balanced component reaches signed consensus $s_C(s_C^{\mathsf T}x_0)/|C|$, while every unbalanced component tends to zero. No global connectedness or global balance label is required.

\>0

# Every principal minor: rooted trees plus negative unicycles

For $R\subseteq V$, write $L[V\setminus R]$ for the principal submatrix on the nonroots. Let $\mathcal F_R$ be the spanning edge sets $F\subseteq E$ whose connected components are of exactly two permitted kinds:

1.  a tree containing exactly one vertex of $R$;

2.  a root-free unicyclic component whose unique cycle has negative sign.

Write $u(F)$ for the number of components of the second kind and $w(F)=\prod_{e\in F}w_e$.

[\[thm:minors\]]{#thm:minors label="thm:minors"} For every root set, including $R=\varnothing$ and $R=V$, $$\label{eq:minor}
 \det L[V\setminus R]=\sum_{F\in\mathcal F_R}4^{u(F)}w(F).$$

Put $U=V\setminus R$. Cauchy--Binet applied to $L[U]=B[U]WB[U]^{\mathsf T}$ gives $$\det L[U]=\sum_{S\subseteq E,\ |S|=|U|}
 \det(B[U,S])^2\prod_{e\in S}w_e.$$ The incidence minor is nonzero precisely when every selected-edge component is a tree with one deleted row (one root), or has no deleted row and is an unbalanced unicycle. Leaf elimination makes a rooted-tree determinant $\pm1$. Eliminating trees attached to a unicycle reduces it to its signed cycle incidence matrix, whose determinant is $0$ for a positive cycle and $\pm2$ for a negative cycle. Squaring and multiplying components gives $4^{u(F)}$, proving [\[eq:minor\]](#eq:minor){reference-type="eqref" reference="eq:minor"}. The empty $0\times0$ determinant and empty forest both equal one.

# The complete characteristic polynomial

Let $\mathcal F$ consist of spanning pseudoforests whose components are trees or negative unicycles. Let $t(F)$ count the tree components.

[\[cor:char\]]{#cor:char label="cor:char"} $$\label{eq:char}
 \det(\lambda I+L)=
 \sum_{F\in\mathcal F}4^{u(F)}w(F)\lambda^{t(F)}
 \prod_{T\in\operatorname{Tree}(F)}|V(T)|.$$

The coefficient identity $\det(\lambda I+L)=\sum_{R\subseteq V}\lambda^{|R|}
\det L[V\setminus R]$ sums all principal minors. For fixed $F\in\mathcal F$, every tree component must choose exactly one root, giving $|V(T)|$ choices, while negative unicycles choose none. Hence $|R|=t(F)$ and [\[eq:char\]](#eq:char){reference-type="eqref" reference="eq:char"} follows.

The formula simultaneously contains the determinant (no tree components), all cofactors and every intermediate coefficient. It also makes every principal minor nonnegative, consistently with $L\succeq0$.

# Two boundary counterexamples

Consider the positive bridge $0$--$1$ and the triangle $1$--$2$--$3$--$1$ with signs $-,+,+$. Its signed Laplacian is $$L=\begin{pmatrix}1&-1&0&0\\-1&3&1&-1\\0&1&2&-1\\0&-1&-1&2\end{pmatrix}.$$ Here $\det L=4$, but deleting root $0$ gives determinant $7$. Three comes from the ordinary spanning trees (the bridge and two triangle edges); four comes from the selected negative triangle plus the isolated root. Thus an all-root-set tree-only formula is false.

Symmetry is essential to Theorem [\[thm:consensus\]](#thm:consensus){reference-type="ref" reference="thm:consensus"}. The directed matrix $$A=\begin{pmatrix}1&-1\\-2&2\end{pmatrix}$$ has right zero vector $(1,1)^{\mathsf T}$ but normalized left zero vector $(2/3,1/3)$. Its limit projector has two identical rows $(2/3,1/3)$ and is not the orthogonal average. Directed, time-varying, nonlinear, nonpositive- weight and self-loop models are outside the frozen theorem.

\>1

# Independent exhaustive certificate and Route-A stop

Every labelled signed simple graph on $1\le n\le4$ is encoded by three states (absent, positive, negative) per possible edge. The ledger therefore contains $1+3+27+729=760$ graphs and all $2+3\cdot4+27\cdot8+729\cdot16=11{,}894$ root sets. It records 760 full characteristic polynomials, 548 balanced and 340 unbalanced component records, and 420 componentwise balanced graphs. The independent checker imports no producer, reconstructs matrices with SymPy, separately enumerates forests, and closes 46,766 assertions. A third path checks ten symbolic arbitrary-weight identities and 1,520 ledger identities. Replay is byte exact; twelve repaired-hash attacks (including unknown-key and six mathematical attacks) and one stale-hash attack are rejected.

This exhaustive unit-weight computation is a convention oracle, not a proof for arbitrary $n$ or weights; Theorems [\[thm:consensus\]](#thm:consensus){reference-type="ref" reference="thm:consensus"} and [\[thm:minors\]](#thm:minors){reference-type="ref" reference="thm:minors"} are the proof. Although the real symmetric $L$ supplies a canonical self-adjoint semigroup and exact finite determinant, it provides no intrinsic rational-prime primitive-orbit layer, prime-power repetition law, target analytic determinant, or target-spectrum operator. Therefore $$(A0,A1,A2,A3,A4)=(\mathrm{FAIL},\mathrm{FAIL},\mathrm{FAIL},
 \mathrm{FAIL},\mathrm{FORMAL\ HINT}),$$ overall `ROUTE_A_REJECTED`, Route B false, under `NO_BAD_EULER_OR_ROOT_NUMBER`.

#### Claim firewall.

We claim no arithmetic local datum, Euler factor, root number, automorphy, target divisor/functional equation, Hilbert--Pólya operator, directed extension, finite-regression proof, exhaustive priority, external review, or acceptance score.

#### Revision focus.

Round 0 proves the complete componentwise kernel, projector, signed-consensus limit and exact spectral-rate theorem.

#### Revision focus.

Round 1 adds all principal minors, the full characteristic pseudoforest expansion and two sharp boundary counterexamples.

#### Revision focus.

Round 2 adds exhaustive and symbolic certificate closure, source ownership, Route-A evaluation, nonclaims and disclosures.

# Declarations {#declarations .unnumbered}

#### Data and code availability.

Package-local synthetic exact evidence and deterministic code accompany the manuscript; no observational network data are used.

#### Ethics.

No human, animal, personal or sensitive data are used; approval is not applicable.

#### Author contributions (CRediT).

This anonymous certificate records Conceptualization, Formal analysis, Software, Validation, Writing---original draft, and Writing---review and editing. AI systems are not authors.

#### Funding.

No external funding is reported.

#### Conflicts of interest.

None known.

#### AI-use disclosure.

An AI coding assistant supported derivation, drafting and exact-code development; it was not an external reviewer or an independent peer-review process.

4 C. Altafini, "Consensus problems on networks with antagonistic interactions," *IEEE Trans. Automat. Control* 58(4) (2013), 935--946. DOI: 10.1109/TAC.2012.2224251. F. Harary, "On the notion of balance of a signed graph," *Michigan Math. J.* 2(2) (1953/54), 143--146. DOI: 10.1307/mmj/1028989917. T. Zaslavsky, "Signed graphs," *Discrete Appl. Math.* 4(1) (1982), 47--74. DOI: 10.1016/0166-218X(82)90033-6. T. Zaslavsky, "Erratum: Signed graphs," *Discrete Appl. Math.* 5(2) (1983), 248. DOI: 10.1016/0166-218X(83)90047-1.
