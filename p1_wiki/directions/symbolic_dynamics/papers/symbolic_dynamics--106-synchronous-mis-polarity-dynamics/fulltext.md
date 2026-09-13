---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--106-synchronous-mis-polarity-dynamics"
canonical_tex: "symbolic_dynamics/papers/106-synchronous-mis-polarity-dynamics/main.tex"
canonical_pdf: "symbolic_dynamics/papers/106-synchronous-mis-polarity-dynamics/main.pdf"
source_sha256: "e19cdbd0708bca16eacf83fad1a710bd05b4b9fb1d5dce2f5c1a55319c422fcb"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Synchronous MIS Polarity Dynamics: Cubic Collapse and a Bipartite Zeta Square Law

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/106-synchronous-mis-polarity-dynamics>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/106-synchronous-mis-polarity-dynamics/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/106-synchronous-mis-polarity-dynamics/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/106-synchronous-mis-polarity-dynamics/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/106-synchronous-mis-polarity-dynamics/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For a finite simple graph $G=(V,E)$, consider the synchronous Boolean network $$\mathcal N_G(A)=\{v\in V:N(v)\cap A=\varnothing\},\qquad A\subseteq V.$$ Its fixed configurations are the maximal independent sets, a known correspondence. We determine the rest of its functional graph. Symmetry of adjacency makes $\mathcal N_G$ an antitone polarity and forces the exact identity $\mathcal N_G^3=\mathcal N_G$. Thus every orbit has preperiod at most one and period one or two. If $m(G)$ is the number of maximal independent sets and $c(G)$ the number of configurations closed under $\mathcal N_G^2$, then $$\zeta_{\mathcal N_G}(z)
   =(1-z)^{-m(G)}(1-z^2)^{-(c(G)-m(G))/2}.$$ For every bipartite graph we prove the square law $c(G)=m(G)^2$, so the number of two-cycles is $m(G)(m(G)-1)/2$. On the path $P_n$, the number $m_n=m(P_n)$ satisfies $m_n=m_{n-2}+m_{n-3}$; this gives a closed zeta family. The proof separates the general polarity route from a bipartite formal-concept splitting, and exhaustive bitset controls independently test the identities. Known MIS-network fixed-point and formal-concept results are explicitly subtracted; no absolute novelty or priority claim is made.
author:
- Anonymous
bibliography:
- references.bib
date: 'Internal Stage 2 draft, 29 August 2026'
title: 'Synchronous MIS Polarity Dynamics: Cubic Collapse and a Bipartite Zeta Square Law'
```

## Markdown 正文

# Introduction

Let every vertex of a graph update in parallel: it becomes active exactly when none of its neighbors was active at the previous time. In Boolean coordinates this is the AND--NOT rule $$x'_v=\bigwedge_{u\sim v}\neg x_u.$$ The same local rule appears as the MIS network. Its fixed points are known to be the characteristic vectors of maximal independent sets, and much of the recent algorithmic work concerns sequential update schedules rather than the synchronous functional graph [@GadouleauKutner2025]. Fixed points of related AND--NOT and conjunctive networks also have an established literature [@Aracena2004; @AracenaRichardSalinas2017]. We assign those facts zero novelty credit.

The elementary-looking synchronous map has a rigid global feature. It is the polarity associated with the symmetric nonincidence relation, so its third iterate equals its first. That identity determines every possible period and reduces the zeta function to two graph counts. Bipartiteness then splits the closure independently across the two color classes. The two one-sided closure systems are anti-isomorphic, and each closed element specifies one maximal independent set. This produces a square law for the entire periodic set, not merely a fixed-point count.

Antitone Galois connections and their closure lattices are standard in formal concept analysis [@GanterWille1999]. The residual contribution here is the exact finite-dynamical package for this synchronous update: the cubic identity, cycle census and zeta reduction, bipartite square law, and path specialization. A bounded search found no source containing this same conjunction, but that is not an exhaustive novelty certificate. External release remains **HOLD**.

# The synchronous network as a polarity

Let $G=(V,E)$ be a finite simple graph, with open neighborhood $N(v)$. For $A\subseteq V$, define $$\label{eq:update}
 F(A):=\{v\in V:N(v)\cap A=\varnothing\}.$$ We use open rather than closed neighborhoods. In particular, an active vertex can persist when none of its distinct neighbors is active.

[\[lem:polarity\]]{#lem:polarity label="lem:polarity"} For all $A,B\subseteq V$,

1.  $A\subseteq B$ implies $F(B)\subseteq F(A)$;

2.  $A\subseteq F^2(A)$;

3.  $F^3(A)=F(A)$.

The first assertion follows immediately from [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"}. If $v\in A$ and $u\in F(A)$, then $u$ has no neighbor in $A$ and hence is not adjacent to $v$. Symmetry of adjacency therefore gives $N(v)\cap F(A)=\varnothing$, so $v\in F^2(A)$.

Applying antitonicity to $A\subseteq F^2(A)$ gives $F^3(A)\subseteq F(A)$. Applying the second assertion to the set $F(A)$ gives the reverse inclusion $F(A)\subseteq F^3(A)$.

The use of an undirected graph is essential: for a directed relation, the two antitone maps generally live on different sides and a single-map cubic identity need not hold.

[\[thm:orbit\]]{#thm:orbit label="thm:orbit"} Every orbit of $F$ has preperiod at most one and eventual period at most two. More precisely, $$\operatorname{im}F=\operatorname{Fix}(F^2)=\{A\subseteq V:F^2(A)=A\}.$$ Moreover, $F(A)=A$ if and only if $A$ is a maximal independent set of $G$.

The identity $F^3=F$ shows that $F(A),F^2(A),F(A),\ldots$ alternates. It also gives $F^2(F(A))=F(A)$, hence $\operatorname{im}F\subseteq\operatorname{Fix}(F^2)$. Conversely, if $F^2(A)=A$, then $A=F(F(A))$ lies in the image.

If $F(A)=A$, then every vertex of $A$ has no neighbor in $A$, so $A$ is independent. Every vertex outside $A$ fails membership in $F(A)$ and therefore has a neighbor in $A$; thus $A$ is dominating and hence maximal independent. The converse is the same argument in reverse.

Call the elements of $\operatorname{Fix}(F^2)$ *closed configurations*. This is the closure system of the extensive, monotone, idempotent map $F^2$. Write $$\label{eq:mc}
 m(G):=|\operatorname{Fix}(F)|,\qquad c(G):=|\operatorname{Fix}(F^2)|.$$ Thus $m(G)$ is the number of maximal independent sets. Closed configurations not fixed by $F$ occur in disjoint pairs $\{A,F(A)\}$.

# Periodic census and zeta function

For a map on a finite set, its Artin--Mazur zeta function is $$\label{eq:zeta-def}
 \zeta_F(z)=\exp\left(\sum_{k\ge1}\frac{|\operatorname{Fix}(F^k)|}{k}z^k\right).$$

[\[cor:zeta\]]{#cor:zeta label="cor:zeta"} For every finite simple graph, $$\label{eq:fix-sequence}
 |\operatorname{Fix}(F^k)|=
 \begin{cases}
 m(G),&k\text{ odd},\\
 c(G),&k\text{ even},
 \end{cases}$$ and $$\label{eq:zeta}
 \boxed{\displaystyle
 \zeta_F(z)=(1-z)^{-m(G)}
 (1-z^2)^{-(c(G)-m(G))/2}.}$$ The functional graph has $m(G)$ one-cycles and $(c(G)-m(G))/2$ two-cycles.

For $k\ge1$, [\[lem:polarity\]](#lem:polarity){reference-type="ref" reference="lem:polarity"} gives $F^k=F$ when $k$ is odd and $F^k=F^2$ when $k$ is even. This proves [\[eq:fix-sequence\]](#eq:fix-sequence){reference-type="eqref" reference="eq:fix-sequence"}. The cycle factorization of [\[eq:zeta-def\]](#eq:zeta-def){reference-type="eqref" reference="eq:zeta-def"}, or direct summation of its odd and even terms, gives [\[eq:zeta\]](#eq:zeta){reference-type="eqref" reference="eq:zeta"}.

The integer parity in [\[eq:zeta\]](#eq:zeta){reference-type="eqref" reference="eq:zeta"} is automatic: the involution $F$ on the closed configurations has exactly $m(G)$ fixed elements.

# Bipartite square law

Suppose now that $G$ is bipartite with a fixed bipartition $V=X\sqcup Y$. Define antitone maps $$\begin{aligned}
 \alpha(P)&:=\{y\in Y:N(y)\cap P=\varnothing\},&&P\subseteq X,
 \label{eq:alpha}\\
 \beta(Q)&:=\{x\in X:N(x)\cap Q=\varnothing\},&&Q\subseteq Y.
 \label{eq:beta}\end{aligned}$$ They form a polarity: $P\subseteq\beta\alpha(P)$, $Q\subseteq\alpha\beta(Q)$, and $\alpha\beta\alpha=\alpha$, $\beta\alpha\beta=\beta$.

For $A=P\sqcup Q$, bipartiteness separates the update: $$\label{eq:split}
 F(P\sqcup Q)=\beta(Q)\sqcup\alpha(P),
 \qquad
 F^2(P\sqcup Q)=\beta\alpha(P)\sqcup\alpha\beta(Q).$$

[\[thm:square\]]{#thm:square label="thm:square"} For every finite bipartite graph $G$, $$\label{eq:square-law}
 \boxed{c(G)=m(G)^2.}$$ Consequently, $$\label{eq:bip-zeta}
 \boxed{\displaystyle
 \zeta_F(z)=(1-z)^{-m(G)}
 (1-z^2)^{-m(G)(m(G)-1)/2}.}$$ In particular, the number of two-cycles is $\binom{m(G)}2$.

Let $$\mathcal C_X=\{P\subseteq X:\beta\alpha(P)=P\},\qquad
 \mathcal C_Y=\{Q\subseteq Y:\alpha\beta(Q)=Q\}.$$ The maps $\alpha$ and $\beta$ restrict to mutually inverse antitone bijections between $\mathcal C_X$ and $\mathcal C_Y$; write their common cardinality as $r$. By [\[eq:split\]](#eq:split){reference-type="eqref" reference="eq:split"}, a full configuration $P\sqcup Q$ is closed exactly when $P\in\mathcal C_X$ and $Q\in\mathcal C_Y$. Hence $c(G)=r^2$.

A full configuration is fixed exactly when $Q=\alpha(P)$ and $P=\beta(Q)$. Such pairs are in bijection with $P\in\mathcal C_X$, so $m(G)=r$. This proves [\[eq:square-law\]](#eq:square-law){reference-type="eqref" reference="eq:square-law"}; [\[eq:bip-zeta\]](#eq:bip-zeta){reference-type="eqref" reference="eq:bip-zeta"} follows from [\[cor:zeta\]](#cor:zeta){reference-type="ref" reference="cor:zeta"}.

The square law includes isolated vertices without modification. An isolated vertex belongs to every maximal independent set, and the same one-sided closure calculation forces it in the corresponding concept.

# Paths

Let $P_n$ be the path on $n$ vertices, and put $m_n=m(P_n)$, with the empty path convention $m_0=1$. The resulting Padovan recurrence for maximal independent sets of paths is classical [@EulerOleksikSkupien2013 Remark 2.2]; we include the short endpoint decomposition because it also fixes our empty-path convention.

[\[prop:path\]]{#prop:path label="prop:path"} The initial values and recurrence are $$\label{eq:path-rec}
 m_0=m_1=1,\qquad m_2=2,\qquad
 m_n=m_{n-2}+m_{n-3}\quad(n\ge3).$$ Equivalently, $$\label{eq:path-gf}
 \sum_{n\ge0}m_nx^n=\frac{1+x+x^2}{1-x^2-x^3}.$$ The synchronous MIS network on $P_n$ therefore has $$\label{eq:path-zeta}
 \zeta_{P_n}(z)=(1-z)^{-m_n}
 (1-z^2)^{-m_n(m_n-1)/2}.$$

In a maximal independent set of $P_n$, either vertex $1$ is chosen and vertex $2$ is not, leaving an arbitrary maximal independent set on the path induced by vertices $3,\ldots,n$; or vertex $1$ is not chosen, which forces vertex $2$ to be chosen and vertex $3$ not to be chosen, leaving an arbitrary maximal independent set on vertices $4,\ldots,n$. These two cases give [\[eq:path-rec\]](#eq:path-rec){reference-type="eqref" reference="eq:path-rec"}. The generating function follows by the standard recurrence calculation, and [\[eq:path-zeta\]](#eq:path-zeta){reference-type="eqref" reference="eq:path-zeta"} is [\[thm:square\]](#thm:square){reference-type="ref" reference="thm:square"}.

The first values are $$1,1,2,2,3,4,5,7,9,12,16,21,28,37,\ldots$$ starting at $n=0$. Thus even this sparse graph family carries a rapidly growing set of synchronous two-cycles: their number is $m_n(m_n-1)/2$.

# Independent exact controls and scope

The accompanying exact program has two implementations of [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"}: an integer-bitset neighborhood rule and a literal set/relation rule. It exhausts every simple graph through six vertices, exhausts all bipartite graphs with both color classes of size at most three, and exhausts every state of paths through seventeen vertices. The registered checks include $F^3=F$, the maximal-independent fixed-point criterion, image/closure equality, the bipartite square law, the path recurrence, and the odd/even fixed sequence. These computations are falsification controls, not proofs.

No figure is needed: the complete functional-graph shape is already encoded by the two cycle factors in [\[eq:zeta\]](#eq:zeta){reference-type="eqref" reference="eq:zeta"}. The paper does not claim the MIS fixed-point correspondence, Galois-closure identities in general, or the recurrence for maximal independent sets as new in isolation. The claim is restricted to the displayed synchronous dynamical package and remains subject to external expert literature review.

# Conclusion

The parallel "activate exactly when no neighbor is active" rule is not a long-transient Boolean system on an undirected graph. Symmetry makes it a polarity, collapses every orbit to period at most two after one update, and reduces its zeta function to maximal independent sets and Galois-closed configurations. Bipartiteness then turns the entire periodic count into the square of the fixed count. This supplies a complete temporal description while keeping the known fixed-point and formal-concept owners explicit.
