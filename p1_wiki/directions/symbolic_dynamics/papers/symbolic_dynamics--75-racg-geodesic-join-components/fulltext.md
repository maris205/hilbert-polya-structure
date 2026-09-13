---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--75-racg-geodesic-join-components"
canonical_tex: "symbolic_dynamics/papers/75-racg-geodesic-join-components/main.tex"
canonical_pdf: "symbolic_dynamics/papers/75-racg-geodesic-join-components/main.pdf"
source_sha256: "e4f3828790f64777184bf471008655967406facfd0865d094ae78ab21371c18b"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Join Decomposition, Entropy, and Maximal Measures of Right-Angled Coxeter Clique-Automaton Edge Shifts

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/75-racg-geodesic-join-components>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/75-racg-geodesic-join-components/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/75-racg-geodesic-join-components/main.pdf>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/75-racg-geodesic-join-components/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The standard geodesic language of a right-angled Coxeter group is recognized by a clique automaton. We determine the recurrent-component structure of the automaton's state-decorated two-sided edge shift directly from the join decomposition of the defining graph. If the complement graph has nontrivial components $\Delta_1,\ldots,\Delta_r$ and $t$ isolated vertices, the component indexed by $\varnothing\neq S\subseteq\{1,\ldots,r\}$ has adjacency matrix equal to the Kronecker sum $\mathbin{\widehat\oplus}_{i\in S}A_i$ of the local clique automata. Hence its spectral radius is $\sum_{i\in S}\rho(A_i)$. The maximal support uses every nontrivial factor, while the $t$ universal-vertex coordinates of the automaton state may be frozen in or out. The edge presentation therefore has exactly $2^t$ maximal components and $2^t$ ergodic measures of maximal entropy. We also obtain a product determinant formula for its zeta function. A graph-atlas audit through seven vertices verifies the component matrices and counts in 1252 cases. These multiplicities are presentation-level and are not asserted for the unadorned label shift.
author:
- Anonymous
bibliography:
- references.bib
date: 'Internal Stage 2 draft, 27 August 2026'
title: 'Join Decomposition, Entropy, and Maximal Measures of Right-Angled Coxeter Clique-Automaton Edge Shifts'
```

## Markdown 正文

# Introduction

Let $\Gamma$ be a finite simple graph. Its right-angled Coxeter group has one involutory generator for each vertex, with two generators commuting exactly when their vertices are adjacent. Geodesic words over the standard generators form a regular language. The associated finite automaton, and the resulting geodesic growth series, are standard tools in the subject [@BrinkHowlett1993; @AntolinCiobanu2013]. Existing work studies how graph combinatorics controls growth and gives examples with coincident growth data.

Here we retain the automaton state as a two-sided edge presentation and ask how that presentation decomposes. The answer is controlled by the canonical join decomposition of $\Gamma$, equivalently by the connected components of its complement $\Delta=\overline\Gamma$. A state is a clique of $\Gamma$, hence an independent set in $\Delta$. Reading a generator changes only the join factor containing that generator. Once a factor appears in a state it never disappears completely, so factor support is monotone; it must be constant on a recurrent component.

For a nontrivial connected component of $\Delta$, we prove that the local clique automaton is strongly connected. The global recurrent component is then an asynchronous product, whose adjacency matrix is a Kronecker sum. This gives entropy, zeta, and maximal-measure formulas at once. We do not claim the geodesic automaton or rationality of geodesic growth; those are owner results. The residual statement is the recurrent decomposition of the state-decorated edge shift and its presentation-level consequences.

# The clique automaton and its two-sided shift

Write $V=V(\Gamma)$. For a clique $C\subseteq V$ and a letter $v\notin C$, define $$\label{eq:transition}
 T_v(C)=\{v\}\cup(C\cap\operatorname{link}_\Gamma(v)).$$ The standard deterministic automaton has the empty start state, all cliques as accepting states, and transition [\[eq:transition\]](#eq:transition){reference-type="eqref" reference="eq:transition"}; reading $v\in C$ goes to a fail state. The nonfail transition graph recognizes the geodesic language [@AntolinCiobanu2013].

Let $\mathsf G_\Gamma$ be the finite directed multigraph on the nonempty cliques, with one edge labelled $v$ from $C$ to $T_v(C)$ whenever $v\notin C$. We keep parallel labelled edges in its adjacency matrix. Let $X_\Gamma^{\rm edge}$ be the two-sided edge shift of $\mathsf G_\Gamma$, and let $Y_\Gamma$ be the sofic label shift consisting of bi-infinite generator sequences all of whose finite blocks are geodesic. Edge labelling gives a factor map $$\pi_{\rm lab}:X_\Gamma^{\rm edge}\longrightarrow Y_\Gamma.$$ Every edge-label block is geodesic because it is a subword of a word readable from the start state; conversely, compactness lifts every point of $Y_\Gamma$ to this edge presentation. The factor need not be one-to-one. All component, maximal-measure, and zeta statements below concern $X_\Gamma^{\rm edge}$, not the unadorned label shift $Y_\Gamma$.

Let $$\Delta=\overline\Gamma=\Delta_1\sqcup\cdots\sqcup\Delta_r
 \sqcup\{u_1\}\sqcup\cdots\sqcup\{u_t\},$$ where the $\Delta_i$ are connected and have at least two vertices, and the $u_j$ are isolated vertices of $\Delta$. Thus $$\Gamma=\Gamma_1*\cdots*\Gamma_r*K_t,$$ where $*$ denotes graph join and each $u_j$ is a universal vertex of $\Gamma$.

For a clique state $C$, define its nontrivial-factor support $$\operatorname{supp}(C)=\{i:C\cap V(\Delta_i)\neq\varnothing\}$$ and record separately the subset $C\cap\{u_1,\ldots,u_t\}$ of universal vertices.

# Irreducibility of a complement-connected factor

Let $A_i$ be the adjacency matrix, with label multiplicity, of the clique automaton on the nonempty cliques of $\Gamma_i=\overline{\Delta_i}$.

[\[lem:local\]]{#lem:local label="lem:local"} If $\Delta_i$ is connected and has at least two vertices, then its nonempty clique automaton is strongly connected.

We work in $\Delta_i$. A clique of $\Gamma_i$ is an independent set of $\Delta_i$, and reading $v$ replaces the current set $C$ by $$\{v\}\cup(C\setminus N_{\Delta_i}(v)).$$

First reduce any state $C$ to a singleton. Since $C$ is independent and $\Delta_i$ is connected with at least two vertices, $V(\Delta_i)\setminus C$ is nonempty. Start there and take a finite walk visiting every vertex, for example a traversal of a spanning tree. Each next vertex is readable because its predecessor in the walk is present and adjacent to it in $\Delta_i$. Every nonfinal occurrence is removed by its adjacent successor. Each original member of $C$ is either removed when a neighbour is visited or is itself read later and then removed after its final nonterminal occurrence. The terminal state is therefore exactly the singleton containing the last vertex of the walk.

Any singleton $\{u\}$ can be moved to any other singleton $\{v\}$ by reading the vertices after $u$ along a path from $u$ to $v$ in $\Delta_i$; consecutive vertices do not commute, so the state remains a singleton. Finally, from a singleton belonging to a target clique $D$, read the remaining vertices of $D$. They are pairwise nonadjacent in $\Delta_i$, hence commute in $\Gamma_i$, and accumulate without deletion. Thus every state reaches every other state.

In particular $A_i$ is irreducible and $\rho(A_i)\geq1$: any edge of the connected complement supplies a directed two-cycle between its singleton states.

# The recurrent join decomposition

For square matrices $B_1,\ldots,B_s$, write $$B_1\mathbin{\widehat\oplus}\cdots\mathbin{\widehat\oplus}B_s
 =\sum_{j=1}^s I\otimes\cdots\otimes B_j\otimes\cdots\otimes I$$ for their Kronecker sum.

[\[thm:components\]]{#thm:components label="thm:components"} Assume $r\geq1$. The recurrent strongly connected components of $\mathsf G_\Gamma$ are indexed by pairs $$(S,T),\qquad \varnothing\neq S\subseteq\{1,\ldots,r\},
 \quad T\subseteq\{u_1,\ldots,u_t\}.$$ On this component the nontrivial support is $S$, the universal subset is $T$, and the adjacency matrix is $$\label{eq:kron-sum}
 A_S=\mathbin{\widehat\oplus}_{i\in S}A_i.$$ Consequently $$\label{eq:rho-sum}
 \rho(A_S)=\sum_{i\in S}\rho(A_i).$$ There are $(2^r-1)2^t$ recurrent components.

Vertices from different components of $\Delta$ are adjacent in $\Gamma$. Thus reading a vertex in factor $i$ changes only the $i$th clique coordinate and leaves all other coordinates fixed. A nonempty coordinate never becomes empty, because every transition adds the newly read vertex. Factor support is therefore monotone along paths and constant on a strongly connected component. A universal vertex, once present, is similarly frozen, and if it is absent it can only be added.

Fix $(S,T)$. Within that support, a transition changes exactly one nontrivial coordinate according to its local clique automaton. By [\[lem:local\]](#lem:local){reference-type="ref" reference="lem:local"}, each local factor is strongly connected; their asynchronous product is strongly connected and has adjacency matrix [\[eq:kron-sum\]](#eq:kron-sum){reference-type="eqref" reference="eq:kron-sum"}. It contains cycles. Conversely, every recurrent component must have constant support and hence is one of these products. Supports containing only universal vertices have no internal edge and do not belong to a two-sided recurrent component.

If $x_i>0$ is a Perron vector of $A_i$, then $\bigotimes_{i\in S}x_i$ is a positive eigenvector of $A_S$ with eigenvalue $\sum_{i\in S}\rho(A_i)$. Perron--Frobenius theory makes this the spectral radius, proving [\[eq:rho-sum\]](#eq:rho-sum){reference-type="eqref" reference="eq:rho-sum"}. Counting $S$ and $T$ gives the last assertion.

If $r=0$, then $\Gamma$ is complete and the Coxeter group is finite. Support strictly increases until no letter is readable, so the two-sided geodesic edge shift is empty. We exclude this degenerate case below.

# Entropy, maximal measures, and zeta

[\[cor:entropy\]]{#cor:entropy label="cor:entropy"} For $r\geq1$, $$\label{eq:entropy}
 h_{\rm top}(X_\Gamma^{\rm edge})=
 \log\left(\sum_{i=1}^r\rho(A_i)\right).$$ The maximal recurrent components are precisely $$(\{1,\ldots,r\},T),\qquad T\subseteq\{u_1,\ldots,u_t\}.$$ Hence $X_\Gamma^{\rm edge}$ has exactly $2^t$ ergodic measures of maximal entropy.

Every $\rho(A_i)$ is positive, so [\[eq:rho-sum\]](#eq:rho-sum){reference-type="eqref" reference="eq:rho-sum"} is maximized uniquely in the nontrivial coordinate by taking all $r$ factors. The universal subset does not alter the matrix, yielding $2^t$ copies of the maximal irreducible edge shift. Each irreducible finite-state edge shift has one Parry measure; an ergodic invariant measure cannot charge transient edges between recurrent components. This proves both assertions.

Thus universal-vertex coordinates have a presentation-level signature invisible to entropy: each may be permanently present or absent in a maximal automaton state, doubling the number of maximal edge components without changing their entropy.

[\[rem:labels\]]{#rem:labels label="rem:labels"} For fixed nontrivial support $S$, the $2^t$ components indexed by $T$ have identical labelled images: the frozen universal coordinates decorate states but do not occur on internal edges. Thus the $2^t$ multiplicity of Parry measures and the exponent $2^t$ in the zeta function need not survive the factor $\pi_{\rm lab}$. For example, join an edgeless graph on $\{a,b\}$ with one universal vertex $u$. The two maximal edge components are both labelled by the alternating sequences in $a,b$ and their Parry measures have the same image. A point of $Y_\Gamma$ can contain $u$ at most once, so every invariant measure gives $[u]$ mass zero. Consequently the MME and zeta multiplicities below are invariants of the stated clique-automaton edge presentation, not of the bare geodesic label language.

[\[cor:zeta\]]{#cor:zeta label="cor:zeta"} The Artin--Mazur zeta function of the clique-automaton edge shift is $$\label{eq:zeta}
 \zeta_{X_\Gamma^{\rm edge}}(z)=
 \prod_{\varnothing\neq S\subseteq\{1,\ldots,r\}}
 \det(I-zA_S)^{-2^t}.$$

A periodic path stays in one recurrent component. For an edge shift with adjacency $A$, its period-$n$ fixed count is $\operatorname{tr}(A^n)$ and its zeta function is $\det(I-zA)^{-1}$. Multiply over the components in [\[thm:components\]](#thm:components){reference-type="ref" reference="thm:components"}; each nontrivial support occurs for all $2^t$ universal subsets.

# An explicit family

Let $\Gamma$ be the join of two edgeless two-vertex graphs and a complete graph on $t$ universal vertices. Each nontrivial local automaton is the two-cycle $$A_1=A_2=\begin{pmatrix}0&1\\1&0\end{pmatrix}.$$ The maximal adjacency is $A_1\mathbin{\widehat\oplus}A_2$, with spectrum $\{2,0,0,-2\}$. Therefore $$h_{\rm top}=\log2,
 \qquad \#\{\text{ergodic MMEs}\}=2^t,$$ and every maximal component has zeta function $$\frac1{1-4z^2}.$$ Including the two one-factor supports, the full zeta function is $$\zeta_{X_\Gamma^{\rm edge}}(z)
 =\left((1-z^2)^{-2}(1-4z^2)^{-1}\right)^{2^t}.$$

# Finite audit and scope

The deterministic audit visits all $1252$ unlabeled graphs in the NetworkX atlas with at most seven vertices. There are $996$ graphs with connected complement, of which $995$ have at least two vertices and exercise the local irreducibility lemma. For every atlas graph, the script identifies each recurrent component by its support and universal subset, constructs its ordered state set, and compares its adjacency matrix entrywise with the predicted Kronecker sum. It also verifies the component and maximal-component counts. The explicit two-factor spectrum is extracted from an actual joined defining graph. These computations are finite regression evidence; the general proof is [\[lem:local,thm:components\]](#lem:local,thm:components){reference-type="ref" reference="lem:local,thm:components"}.

The established theory already supplies automaticity and rational geodesic growth [@BrinkHowlett1993; @AntolinCiobanu2013], and later work constrains right-angled Coxeter geodesic growth rates [@KolpakovTalambutsa2020]. We do not claim those results, a group-isomorphism invariant, or a classification of defining graphs by symbolic data. Our edge shift depends on both the standard generating graph and the stated clique-automaton presentation; [\[rem:labels\]](#rem:labels){reference-type="ref" reference="rem:labels"} records what does not descend to label dynamics. The bounded source review located no exact collision for the edge-presentation join theorem, but it is not a worldwide priority certificate; external release remains on hold.
