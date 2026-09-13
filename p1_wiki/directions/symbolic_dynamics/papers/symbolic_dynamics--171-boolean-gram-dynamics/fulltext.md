---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--171-boolean-gram-dynamics"
canonical_tex: "symbolic_dynamics/papers/171-boolean-gram-dynamics/main.tex"
canonical_pdf: "symbolic_dynamics/papers/171-boolean-gram-dynamics/main.pdf"
source_sha256: "1a1ca296a922d02a12fe8d01ae3c4122eee892ef5f6a5c83e801c218247cc197"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Boolean Gram Closure as a Finite Dynamical System

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/171-boolean-gram-dynamics>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/171-boolean-gram-dynamics/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/171-boolean-gram-dynamics/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/171-boolean-gram-dynamics/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/171-boolean-gram-dynamics/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Let $\mathbb B=\{0,1\}$ with Boolean addition and multiplication, and iterate $\Gamma_n(A)=AA^{\mathsf T}$ on the $n\times n$ Boolean matrices. We give the complete finite functional graph. If $G=AA^{\mathsf T}$, then $\Gamma_n^t(A)=G^{2^{t-1}}$ for $t\geq1$. Thus every orbit ends at the looped clique completion of the active components of the row-intersection graph. The recurrent states are precisely partial equivalence relations, all fixed; a nonfixed source has depth $1+\lceil\log_2 D(G)\rceil$, with a zero logarithmic term for $D(G)\leq1$. The sharp carrier height is zero at $n=1$ and $1+\lceil\log_2(n-1)\rceil$ for $n\geq2$. There are $B_{n+1}$ fixed states. Independently, for every prescribed target we count the complete ordered-column fibre by inclusion--exclusion over its loop and edge requirements. The image criterion is a loop-sensitive edge-clique-cover bound. Boolean powers, transitive closure, graph intersection representations, clique covers, and symmetric Boolean factorization are treated as prior mechanisms; the note remains on external hold.
author:
- Anonymous
bibliography:
- references.bib
title: Boolean Gram Closure as a Finite Dynamical System
```

## Markdown 正文

# The literal map and its graph factor

Write $\mathbb B^{n\times n}$ for the set of zero--one matrices, with $$(PQ)_{ij}=\bigvee_{r=1}^{n}(P_{ir}\wedge Q_{rj}).$$ Our self-map is $$\label{eq:literal}
 \Gamma_n:\mathbb B^{n\times n}\longrightarrow\mathbb B^{n\times n},
 \qquad \Gamma_n(A)=AA^{\mathsf T}.$$ If $R_i=\{r:A_{ir}=1\}$ is row $i$ regarded as a subset of $[n]$, then $$\label{eq:intersection}
 \Gamma_n(A)_{ij}=1\quad\Longleftrightarrow\quad R_i\cap R_j\ne\varnothing.$$ Hence $G=\Gamma_n(A)$ is a symmetric relation. A vertex $i$ has a loop exactly when $R_i$ is nonempty, and every off-diagonal edge has loops at both ends. We call these vertices *active*. On the active vertices, $G$ is an ordinary undirected graph with a loop at each vertex; inactive vertices are unlooped and isolated.

The interpretation [\[eq:intersection\]](#eq:intersection){reference-type="eqref" reference="eq:intersection"} is the classical set-intersection representation of a graph. Its equivalence with an edge clique cover goes back at least to Szpilrajn--Marczewski and Erdős--Goodman--Pósa [@SzpilrajnMarczewski1945; @ErdosGoodmanPosa1966]. Boolean matrix powers and transitive-closure algorithms are also classical [@Warshall1962; @Kim1982]. More specifically, Fitting records the monotone chain $(AA^{\mathsf T})\leq(AA^{\mathsf T})^2\leq\cdots$ and examples with arbitrarily many strict inclusions as dimension grows [@Fitting2003 Theorem 8 and Example 9]. Exact symmetric Boolean factorization $M=WW^{\mathsf T}$ and its clique-cover and hypergraph interpretations are explicit in recent algorithmic work [@ChenSongTaoZhang2022]. These mechanisms are background here. Our scope is the exact functional graph of the literal self-map [\[eq:literal\]](#eq:literal){reference-type="eqref" reference="eq:literal"}, paired with all of its finite ordered-column fibres; no priority claim is made.

For a finite self-map, $\operatorname{depth}(A)$ is the least $d\geq0$ for which $\Gamma_n^d(A)$ is recurrent. Put $D(G)=0$ when $G$ has no active edge between distinct vertices; otherwise $D(G)$ is the largest diameter of an active connected component.

[\[thm:temporal\]]{#thm:temporal label="thm:temporal"} Let $A\in\mathbb B^{n\times n}$ and $G=AA^{\mathsf T}$.

(i) For every $t\geq1$, $$\label{eq:iterate}
     \Gamma_n^t(A)=G^{2^{t-1}}.$$ The endpoint is obtained by replacing every active connected component of $G$ by a fully looped clique and leaving every inactive vertex unlooped and isolated.

(ii) The recurrent states are exactly the partial equivalence relations: disjoint unions of fully looped cliques together with unlooped isolated vertices. Every recurrent state is fixed. Their number is $$\label{eq:bell}
      |\operatorname{Fix}(\Gamma_n)|=\sum_{k=0}^{n}\binom nk B_k=B_{n+1},$$ where $B_k$ is the $k$th Bell number. Consequently the Artin--Mazur zeta function is $$\label{eq:zeta}
      \zeta_{\Gamma_n}(z)=(1-z)^{-B_{n+1}}.$$

(iii) The exact source-dependent clock is $$\label{eq:clock}
       \operatorname{depth}(A)=
       \begin{cases}
       0,&A\text{ is a partial equivalence relation},\\[1mm]
       1+\lceil\log_2 D(G)\rceil,&\text{otherwise},
       \end{cases}$$ where the ceiling term is declared to be zero for $D(G)\leq1$. The sharp height of the whole carrier is $$\label{eq:height}
       h_n=\max_A\operatorname{depth}(A)=
       \begin{cases}
       0,&n=1,\\
       1+\lceil\log_2(n-1)\rceil,&n\geq2.
       \end{cases}$$

The relation $G$ is symmetric, so $\Gamma_n(G)=GG^{\mathsf T}=G^2$. Every Boolean power of $G$ is symmetric; induction therefore gives $$\Gamma_n(G^{2^s})=G^{2^s}(G^{2^s})^{\mathsf T}=G^{2^{s+1}},$$ which proves [\[eq:iterate\]](#eq:iterate){reference-type="eqref" reference="eq:iterate"}.

For active vertices $i,j$, the entry $(G^r)_{ij}$ is one precisely when there is a walk of length $r$ from $i$ to $j$. Loops pad a shorter path to any larger length, so this is equivalent to graph distance at most $r$. Thus $G^{2^{t-1}}$ completes every active component exactly when $2^{t-1}\geq D(G)$, and its stable value is the asserted partial equivalence relation. This proves the endpoint and [\[eq:clock\]](#eq:clock){reference-type="eqref" reference="eq:clock"}, including $D(G)=0,1$.

If $A=AA^{\mathsf T}$, then $A$ is symmetric, every nonempty row has its diagonal entry, and $A=A^2$ is transitive. Its active components are therefore fully looped cliques. Conversely, such a partial equivalence relation $A$ is symmetric and idempotent, hence $AA^{\mathsf T}=A^2=A$. Every orbit reaches one of these states, so there can be no other recurrent state. To count them, choose the $k$ active vertices and partition them into clique components. This gives the sum in [\[eq:bell\]](#eq:bell){reference-type="eqref" reference="eq:bell"}; adjoining a distinguished element to the inactive vertices is the standard bijection with partitions of an $(n+1)$-element set. Every periodic point is fixed, so $|\operatorname{Fix}(\Gamma_n^r)|=B_{n+1}$ for every $r\geq1$, and the definition of the Artin--Mazur zeta function gives [\[eq:zeta\]](#eq:zeta){reference-type="eqref" reference="eq:zeta"}.

Finally, $D(G)\leq n-1$, proving the upper bound in [\[eq:height\]](#eq:height){reference-type="eqref" reference="eq:height"}. For $n\geq2$, label the edges of the path $1-2-\cdots-n$ by $1,\ldots,n-1$ and let row $i$ of $A$ contain the labels of the path edges incident with $i$; leave column $n$ empty. Then $AA^{\mathsf T}$ is the fully looped path, of diameter $n-1$, and $A$ is not fixed. Its depth is the claimed bound. At $n=1$, both Boolean matrices are fixed.

# Every-target ordered-column fibres

We now solve the one-step inverse problem without assuming that the target lies in the image. For a Boolean relation $H$ on $[n]$, define $$\mathcal C(H)=\{C\subseteq[n]:H_{ij}=1\text{ for every }i,j\in C\}.$$ Thus $\varnothing\in\mathcal C(H)$, and every nonempty member is a fully looped clique of $H$. When $H$ is symmetric and each edge has both endpoint loops, let $$\label{eq:atoms}
 E^*(H)=\bigl\{\{i\}:H_{ii}=1\bigr\}
 \cup\bigl\{\{i,j\}:i<j,\ H_{ij}=1\bigr\}.$$ For $S\subseteq E^*(H)$ put $$\label{eq:cHS}
 c_H(S)=\#\{C\in\mathcal C(H): e\nsubseteq C
                         \text{ for every }e\in S\}.$$

[\[thm:fibre\]]{#thm:fibre label="thm:fibre"} If $H$ is nonsymmetric, or if some entry $H_{ij}=1$ has $H_{ii}H_{jj}=0$, then $\Gamma_n^{-1}(H)=\varnothing$. For every remaining target, $$\label{eq:fibre}
 \boxed{\quad
 |\Gamma_n^{-1}(H)|=
 \sum_{S\subseteq E^*(H)}(-1)^{|S|}\,c_H(S)^n.
 \quad}$$ Moreover, $H$ lies in the image exactly when the atoms $E^*(H)$ can be covered by at most $n$ members of $\mathcal C(H)\setminus\{\varnothing\}$, where $C$ covers $e$ when $e\subseteq C$.

The necessary symmetry and loop conditions follow immediately from [\[eq:intersection\]](#eq:intersection){reference-type="eqref" reference="eq:intersection"}. Suppose they hold and write $C_r$ for the support of column $r$ of a prospective source matrix $A$. Boolean multiplication gives the exact union identity $$\label{eq:square-union}
 AA^{\mathsf T}=\bigcup_{r=1}^{n} C_r\times C_r.$$ No zero of $H$ is changed to one exactly when each $C_r\in\mathcal C(H)$. Every one of $H$ is obtained exactly when, for each atom $e\in E^*(H)$, at least one chosen $C_r$ contains $e$.

For a fixed set $S$ of atoms, there are $c_H(S)^n$ ordered column sequences that miss every atom of $S$. Inclusion--exclusion over the events "atom $e$ is missed by all columns" gives [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"}. The columns are labelled, so their order matters; equal column supports are allowed, and the empty support is an allowed padding column. Consequently such a sequence exists precisely when at most $n$ nonempty allowed cliques cover all atoms.

Ignoring loops, the last statement specializes to the classical intersection-number/edge-clique-cover criterion [@ErdosGoodmanPosa1966]. The singleton atoms in [\[eq:atoms\]](#eq:atoms){reference-type="eqref" reference="eq:atoms"} are essential: an isolated looped vertex still needs a nonempty singleton column support. Compatibility alone is not sufficient. For example, the fully looped $K_{2,3}$ target at $n=5$ has six edges, every allowed nontrivial clique is an edge, and hence its fibre is zero.

Some small fibres illustrate the ordered convention. Let $I_3$ and $J_3$ be the identity and all-one relations, and let $P_3^\circ$ be the three-vertex path with all three loops. Formula [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"} gives

  target $H$               $0_3$   $I_3$   $P_3^\circ$   $J_3$
  ---------------------- ------- ------- ------------- -------
  $|\Gamma_3^{-1}(H)|$       $1$     $6$          $30$   $175$

For $0_n$, all columns must be empty, so the fibre is one. For an isolated single loop and $n-1$ inactive vertices, exactly a nonempty subset of the $n$ labelled columns may equal that singleton, giving $2^n-1$. These examples also expose the zero target, isolated-loop, repeated-column, and empty-column boundaries.

# Exact finite controls and scope

A standalone standard-library verifier exhausts every source and every target through $n=4$. It compares literal fibres with [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"}, checks the cover criterion, temporal identity, exact diameter clock, fixed census, and sharp path witnesses; the latter are also replayed through $n=64$. Its frozen summaries are

    $n$   states   image   fixed   max depth   max fibre
  ----- -------- ------- ------- ----------- -----------
      1        2       2       2           0           1
      2       16       5       5           1           7
      3      512      18      15           2         175
      4   65,536     113      52           3      17,887

The same program explicitly exercises $n=1$, the zero matrix, the $D(G)\leq1$ convention, isolated loops, unlooped incident-edge targets, and empty columns. Finite computation is evidence against transcription or boundary errors, not a substitute for the all-parameter proofs above.

The claims deliberately stop at this exact package. Boolean semiring algebra, graph squaring and component closure, Bell enumeration, intersection representations, edge clique covers, and inclusion--exclusion are not claimed contributions. In particular, Theorem [\[thm:fibre\]](#thm:fibre){reference-type="ref" reference="thm:fibre"} does not solve the optimization or reconstruction variants of symmetric Boolean factorization. This document is an anonymous author-side Round-0 record with external status `HOLD_EXTERNAL`; it makes no submission, release, novelty, or priority assertion.
