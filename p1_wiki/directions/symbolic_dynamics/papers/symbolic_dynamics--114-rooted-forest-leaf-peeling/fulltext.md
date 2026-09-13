---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--114-rooted-forest-leaf-peeling"
canonical_tex: "symbolic_dynamics/papers/114-rooted-forest-leaf-peeling/main.tex"
canonical_pdf: "symbolic_dynamics/papers/114-rooted-forest-leaf-peeling/main.pdf"
source_sha256: "916e484b96487c3593f649c824a1aa886ebfff68372825bb24f3b5ac6f745bb6"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Exact Basins and Fibres for Parallel Leaf Peeling on Labelled Rooted Forests

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/114-rooted-forest-leaf-peeling>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/114-rooted-forest-leaf-peeling/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/114-rooted-forest-leaf-peeling/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/114-rooted-forest-leaf-peeling/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/114-rooted-forest-leaf-peeling/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  On every rooted forest carried by a subset of $[n]$, delete all nonroot leaves in parallel and keep the roots. We determine the resulting finite dynamical system. Its depth is the forest height, its $2^n$ recurrent states are fixed, and, for $n\geq2$, its sharp maximum depth is $n-1$, attained by exactly $n!$ states. (For $n=0,1$ the maximum depth is zero.) A fixed root set of size $r$ has basin $$\sum_{k=0}^{n-r}\binom{n-r}{k}r(r+k)^{k-1}.$$ Nested exponential generating functions give every bounded-depth part of every basin. We also determine every local indegree: if a target has $m$ vertices and $s$ nonroot leaves, its one-step fibre has size $$\sum_{j=0}^{s}(-1)^j\binom{s}{j}(m-j+1)^{n-m}.$$ A peeling clock, determinant/species basin controls, and a separate target-leaf inclusion--exclusion together close the global basins, all transient shells, local fibres, periodic census, and parameter recovery. Parallel leaf removal, Cayley-forest counts, height enumeration, and the general tools are inputs; the residual internal scope is only this finite-map conjunction.
author:
- Anonymous
bibliography:
- references.bib
title: Exact Basins and Fibres for Parallel Leaf Peeling on Labelled Rooted Forests
```

## Markdown 正文

# The system and the complete statement

Fix $n\geq0$ and write $[n]=\{1,\ldots,n\}$. A state is a pair $F=(S,p)$ with $S\subseteq[n]$ and $p:S\to S$ such that every orbit of $p$ reaches a fixed point. Equivalently, $p$ orients a rooted forest toward its roots $$R(F)=\{v\in S:p(v)=v\}.$$ A child of $v$ is a $w\ne v$ with $p(w)=v$. Let $L(F)$ be the nonroot vertices having no children. Our update is $$T(F)=\bigl(S\setminus L(F),p|_{S\setminus L(F)}\bigr).       \tag{1.1}$$ The restriction is well defined: a deleted leaf points to a vertex that is not deleted. The empty forest is allowed. Define the forest height $H(F)$ to be the maximum root--vertex distance when $F$ is nonempty and set $H(\varnothing)=0$; thus an edgeless forest, including the empty one, has height zero.

For a fixed $R\subseteq[n]$, let $E_R$ denote the edgeless forest on $R$. For $r\geq1$ define $$\begin{aligned}
 B_{n,r}&=\sum_{k=0}^{n-r}\binom{n-r}{k}r(r+k)^{k-1},          \tag{1.2}\label{eq:basin}\\
 A_0(x)&=1,\qquad A_h(x)=\exp\!\bigl(xA_{h-1}(x)\bigr),       \tag{1.3}\label{eq:Ah}\\
 B_{n,r}^{(h)}
 &=\sum_{k=0}^{n-r}\binom{n-r}{k}k![x^k]A_h(x)^r.            \tag{1.4}\label{eq:bounded-basin}\end{aligned}$$ The $k=0$ term in [\[eq:basin\]](#eq:basin){reference-type="eqref" reference="eq:basin"} is one. Put $B_{n,0}=B_{n,0}^{(h)}=1$ for $h\geq0$, and put $B_{n,r}^{(-1)}=0$ for every $0\leq r\leq n$.

[\[thm:main\]]{#thm:main label="thm:main"} For every $n\geq0$ the following statements hold.

1.  Every orbit terminates at $E_{R(F)}$, and its entry time is the maximum root--vertex distance in $F$, namely $H(F)$ under the empty-state convention above.

2.  The basin of each $E_R$, $|R|=r$, has size $B_{n,r}$; exactly $B_{n,r}^{(h)}$ of its states have entry time at most $h$. Hence its exact depth-$h$ shell is $B_{n,r}^{(h)}-B_{n,r}^{(h-1)}$ for every $h\geq0$.

3.  If a target $G$ has $m$ present vertices and $s$ nonroot leaves, then $$|T^{-1}(G)|=\sum_{j=0}^{s}(-1)^j\binom{s}{j}(m-j+1)^{n-m}.   \tag{1.5}\label{eq:fibre}$$ This includes the empty target, whose only preimage is itself.

4.  The phase size, periodic data, and Artin--Mazur zeta function are $$|\mathcal F_n|=\sum_{m=0}^{n}\binom nm(m+1)^{m-1},\qquad
     |\operatorname{Fix}(T^q)|=2^n\ (q\geq1),\qquad
     \zeta_T(z)=(1-z)^{-2^n}.                                    \tag{1.6}\label{eq:periodic}$$ For $n\geq2$ the largest entry time is $n-1$, and precisely $n!$ states have this depth.

Consequently any one of the fixed-count sequence, the zeta exponent, or the functional graph determines $n$.

The constituent tools and the temporal primitive are classical. Cayley's tree count and its rooted-forest extensions are standard [@Cayley1889; @Moon1970], with the all-minors determinant supplied by [@Chaiken1982]; labelled-tree height enumeration predates the species formulation [@Riordan1960; @RenyiSzekeres1967], while nested height generating functions fit the general labelled-species framework [@BergeronLabelleLeroux1998; @FlajoletSedgewick2009]. Leaf erasure as a height-governed pruning dynamics is explicit in [@KovchegovZaliapin2020]; the literal parallel *RAKE* primitive appears in [@MillerReif1985]; and recent parallel leaf stripping on random recursive trees appears in [@AddarioBerryEtAl2025]. We use the usual dynamical zeta convention [@ArtinMazur1965]. We assign no novelty or priority credit to the height clock, semigroup/absorption mechanism, Cayley counts, height EGFs, inclusion--exclusion, zeta conversion, or elementary Hamilton-path extremal argument. The residual internal result is only the simultaneous finite-map package in [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}, especially the endpoint-resolved depth series and local-fibre statistic [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"}.

# Peeling time and the recurrent core

For a vertex $v$, let $H_F(v)$ be the maximum length of a directed path that starts at a descendant leaf and ends at $v$; take $H_F(v)=0$ when $v$ has no nontrivial descendants. This is a subtree height, not the distance of $v$ from its root.

[\[lem:clock\]]{#lem:clock label="lem:clock"} A nonroot vertex $v$ is deleted in round $H_F(v)+1$. Therefore $T^hF$ is fixed if and only if $H(F)\leq h$.

Induct on $H_F(v)$. A nonroot vertex of height zero is a leaf and is deleted in round one. If $H_F(v)=a>0$, at least one child has height $a-1$, every child has height at most $a-1$, and induction says that the last child disappears in round $a$. Thus $v$ becomes a leaf precisely for round $a+1$. The final nonroot deletion in a nontrivial component occurs beside its root on a longest root--leaf path, in the round equal to that path length. An edgeless or empty forest is already fixed and has $H(F)=0$ by convention.

Roots never move, while a nonfixed state loses a vertex. Hence there are no nontrivial cycles and every endpoint is $E_{R(F)}$. Conversely every $E_R$ is fixed, giving $2^n$ fixed states and all periodic assertions in [\[eq:periodic\]](#eq:periodic){reference-type="eqref" reference="eq:periodic"}. The zeta identity follows from $\exp(\sum_{q\geq1}2^nz^q/q)=(1-z)^{-2^n}$.

For $n\geq2$, any forest on at most $n$ vertices has height at most $n-1$. Equality forces one component to contain all $n$ labels along one root--leaf path, so the state is a rooted Hamilton path whose root is an endpoint. Listing its vertices from the opposite leaf to the root is a bijection with permutations of $[n]$. This proves the sharp depth and the $n!$ deepest count for $n\geq2$. For $n=0$ the unique empty state has depth zero; for $n=1$ both the empty state and the singleton-root state have depth zero.

# Global basins by two enumerative routes

Fix $R\subseteq[n]$, $|R|=r>0$, and first choose a set of $k$ nonroot labels. For $k=0$ there is exactly the edgeless forest $E_R$. For $k\geq1$, the all-minors matrix-tree theorem applied to the complete graph on $m=r+k$ vertices counts forests oriented to the specified roots [@Chaiken1982]. Standard all-minors statements orient away from roots; reversing every edge of the undirected complete graph bijects those forests with our parent maps oriented toward roots. The count is $$\det(mI_k-J_k)=r\,m^{k-1}.                                  \tag{3.1}\label{eq:matrix-tree}$$ Indeed $mI_k-J_k$ has eigenvalue $r=m-k$ on the all-ones line and eigenvalue $m$ on its $(k-1)$-dimensional complement. Formula [\[eq:basin\]](#eq:basin){reference-type="eqref" reference="eq:basin"} follows after choosing the $k$ labels. For arbitrary roots on a fixed $m$-set, summing [\[eq:matrix-tree\]](#eq:matrix-tree){reference-type="eqref" reference="eq:matrix-tree"} gives $(m+1)^{m-1}$, and then choosing the $m$ present labels gives the phase count in [\[eq:periodic\]](#eq:periodic){reference-type="eqref" reference="eq:periodic"}; its $m=0$ term is the empty state and equals one. Thus the basin partition also yields the exact identity $$\sum_{r=0}^{n}\binom nr B_{n,r}
 =\sum_{m=0}^{n}\binom nm(m+1)^{m-1}.                         \tag{3.2}$$

There is a second route that retains time. Give one root a fixed unlabelled marker and label all other vertices. A height-zero tree is just its root. A height-at-most-$h$ tree is a set of child-rooted trees of height at most $h-1$, which gives exactly [\[eq:Ah\]](#eq:Ah){reference-type="eqref" reference="eq:Ah"}. The $r$ distinguished roots support a root-indexed product of $r$ such species. Therefore, on a prescribed set of $k$ nonroot labels, the count is $$k![x^k]A_h(x)^r.                                             \tag{3.3}\label{eq:height-coeff}$$ Choosing these labels in $[n]\setminus R$ proves [\[eq:bounded-basin\]](#eq:bounded-basin){reference-type="eqref" reference="eq:bounded-basin"}; [\[lem:clock\]](#lem:clock){reference-type="ref" reference="lem:clock"} converts height into entry time. Coefficientwise, $A_h$ stabilizes to the rooted labelled-tree series as $h\to\infty$, so [\[eq:height-coeff\]](#eq:height-coeff){reference-type="eqref" reference="eq:height-coeff"} also recovers [\[eq:matrix-tree\]](#eq:matrix-tree){reference-type="eqref" reference="eq:matrix-tree"}. Thus the determinant and species arguments are independent controls on the complete basin.

# Every local fibre

Let $G=(S,p)$ have $m=|S|$ and let $Q$ be its set of $s$ nonroot leaves. If $m=0$, then $G$ is empty and its only predecessor is empty: every root or nonroot parent-map vertex would survive one update. Hence assume $m\geq1$. Suppose $T(F)=G$ and put $L=V(F)\setminus S$. Every element of $L$ must be a leaf of $F$, so its parent lies in $S$: if one new vertex pointed to another, the latter would have a child and would survive. Conversely, every nonroot leaf of $G$ must receive at least one new child, or it too would be deleted. No other condition is needed, since roots are immortal and every other nonroot vertex of $G$ already has a child in $G$.

For a specified $\ell$-set $L\subseteq[n]\setminus S$, inclusion--exclusion therefore gives $$\#\{L\to S:\text{every element of }Q\text{ is hit}\}
 =\sum_{j=0}^{s}(-1)^j\binom sj(m-j)^\ell.                    \tag{4.1}$$ Summing over the choice of $L$ and using the binomial theorem yields $$\sum_{j=0}^{s}(-1)^j\binom sj
 \sum_{\ell=0}^{n-m}\binom{n-m}{\ell}(m-j)^\ell
 =\sum_{j=0}^{s}(-1)^j\binom sj(m-j+1)^{n-m},$$ which is [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"}. This also proves that the local indegree depends on the target only through $(m,s)$, despite the nonuniform global basins.

# Scope, collision firewall, and exact controls

The closest internal deletion motif is cycle-minimum pruning on permutations. That system keeps permutation cycles as its components and deletes one distinguished element per nontrivial cycle; its clock is a cycle-length statistic and its counts use permutation assembly. Here the phase is a union of labelled rooted-forest spaces, the update deletes all exposed nonroot leaves, the clock is height, and the counts use Cayley determinants, height species, and a target-leaf inclusion--exclusion. Thus the systems and proof engines are different even though both are finite absorbers.

A bounded owner audit also located direct external sources for parallel *RAKE* [@MillerReif1985], height-driven dynamical pruning [@KovchegovZaliapin2020], recursive parallel leaf stripping [@AddarioBerryEtAl2025], labelled height enumeration [@Riordan1960; @RenyiSzekeres1967], and the all-minors determinant [@Chaiken1982]. These mechanisms, enumerations, absorption observations, fixed/zeta conversion, and Hamilton-path extremality are explicit inputs, not claimed advances. The residual description is only the endpoint-indexed assembly and elementary $(m,s)$ fibre calculation. The bounded search did not establish priority for either, and no absence-of-owner inference is made.

The accompanying deterministic verifier enumerates every parent function whose only cycles are loops on all subsets of $[n]$ for $0\leq n\leq6$. It compares literal updates and functional-graph fibres with [\[eq:basin\]](#eq:basin){reference-type="eqref" reference="eq:basin"}--[\[eq:periodic\]](#eq:periodic){reference-type="eqref" reference="eq:periodic"}, expands the nested EGFs with exact rational arithmetic, checks every endpoint/depth cell, and identifies every deepest state. The canonical run contains $400{,}105$ exact assertions; the $n=6$ lane alone contains $26{,}830$ states. These computations fix conventions and attack boundary cases; the proofs above carry the arbitrary-$n$ statements.

External posting, priority, and submission remain on hold.
