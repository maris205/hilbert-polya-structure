---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--143-boolean-row-inclusion-residual"
canonical_tex: "symbolic_dynamics/papers/143-boolean-row-inclusion-residual/main.tex"
canonical_pdf: "symbolic_dynamics/papers/143-boolean-row-inclusion-residual/main.pdf"
source_sha256: "13a4aa9f547e5bd0a09166895494abc232bff1c8300ad509ed1625c4a6f44a7b"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Row-Inclusion Residual Dynamics on Boolean Relations: Preorder Two-Cycles and Exact Fibres

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/143-boolean-row-inclusion-residual>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/143-boolean-row-inclusion-residual/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/143-boolean-row-inclusion-residual/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/143-boolean-row-inclusion-residual/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/143-boolean-row-inclusion-residual/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For an $n\times n$ Boolean matrix $A$, replace $A$ by the matrix that records inclusion among its row supports. The first image is always a labelled preorder, and on every preorder the update is transpose. We derive the global identity $\mathsf T_n^3=\mathsf T_n$: nonpreorders have tail one, equivalence relations are exactly the fixed points, and all other preorders form strict transpose two-cycles. This gives every temporal fixed-set count and the dynamical zeta function. We also solve the one-step inverse problem for every target. For a preorder $P$, preimages are canonically bijective to labelled induced order-embedding maps from its antisymmetric quotient into the Boolean lattice $\mathcal B_n$. Encoding Boolean coordinates as upper sets yields an explicit inclusion--exclusion formula for $|\mathsf T_n^{-1}(P)|$; nonpreorder targets have empty fibre. Relational self-residuation and its preorder property are standard background and receive no contribution credit. Exact exhaustion through $n=4$ is used only for falsification, and external release remains on hold.
author:
- Anonymous
bibliography:
- references.bib
title: |
  Row-Inclusion Residual Dynamics on Boolean Relations:\
  Preorder Two-Cycles and Exact Fibres
```

## Markdown 正文

# The literal map and theorem

Let $\mathcal B_n=2^{[n]}$ be the Boolean lattice. For a Boolean matrix $A\in\{0,1\}^{n\times n}$, write $$R_i(A)=\{j\in[n]:A_{ij}=1\}.$$ Define the literal self-map $$\label{eq:map}
 \mathsf T_n(A)_{ij}=1
 \quad\Longleftrightarrow\quad
 R_i(A)\subseteq R_j(A).$$ We represent a preorder $P$ on $[n]$ by the Boolean matrix with $P_{ij}=1$ exactly when $i\le_Pj$. Let $q_n$ denote the number of labelled preorders on $[n]$, and let $B_n$ denote the $n$th Bell number.

For a finite preorder $S$, let $$J(S)=|\mathsf{Up}(S)|$$ be its number of upper sets. Given a preorder $P$, define $i\sim_Pj$ when $i\le_Pj$ and $j\le_Pi$, and let $Q=P/{\sim_P}$ be the resulting quotient poset. Put $$\label{eq:DQ}
 D_Q=\{(q,r)\in Q^2:q\not\le_Qr\}.$$ For $S\subseteq D_Q$, let $Q_S$ be the preorder obtained by adjoining every pair in $S$ to $Q$ and taking reflexive--transitive closure.

[\[thm:main\]]{#thm:main label="thm:main"} For every $n\geq1$, the following hold.

1.  The image of $\mathsf T_n$ is precisely the set of labelled preorders, and $$\label{eq:transpose}
                           \mathsf T_n(P)=P^{\mathsf T}$$ for every preorder $P$. In particular, $$\label{eq:T3}
                                 \mathsf T_n^3=\mathsf T_n.$$

2.  Every nonpreorder has tail exactly one. The fixed points are exactly the equivalence relations; every other preorder belongs to a strict transpose two-cycle. Consequently, for every $k\geq1$, $$\label{eq:fixed-iterates}
     |\operatorname{Fix}(\mathsf T_n^k)|=
     \begin{cases}
     B_n,&k\text{ odd},\\
     q_n,&k\text{ even},
     \end{cases}$$ and the Artin--Mazur zeta function is $$\label{eq:zeta}
     \zeta_{\mathsf T_n}(z)
     =(1-z)^{-B_n}(1-z^2)^{-(q_n-B_n)/2}.$$

3.  A target outside the preorders has empty fibre. For every preorder $P$, $$\label{eq:fibre}
     |\mathsf T_n^{-1}(P)|
     =\sum_{S\subseteq D_Q}(-1)^{|S|}J(Q_S)^n.$$ Equivalently, the fibre is canonically bijective to the set of labelled induced order-embedding maps $Q\hookrightarrow\mathcal B_n$; no quotient by automorphisms of $Q$ is taken.

The operation in [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"} is a row-oriented instance of relational self-residuation. Schmidt's [@Schmidt2011 §4.4, especially Fig. 4.4.2, p. 45] right-residual convention relates a row of the numerator to the rows of the denominator that it contains; reversing that displayed orientation gives exactly the row-containment convention in [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"}. Relation algebra and containment preorders are standard. Principal-upper-set representations are classical [@Botts1954 pp. 525--526], and induced embeddings in Boolean lattices belong to an established order-theoretic literature [@KatonaNagy2015]. Our scope is the iterated finite map and its complete inverse atlas, not invention of any of those constructions.

# Collapse to a preorder and order reversal

[\[lem:preorder\]]{#lem:preorder label="lem:preorder"} For every Boolean matrix $A$, the relation $\mathsf T_n(A)$ is reflexive and transitive.

Every row support contains itself, so $R_i(A)\subseteq R_i(A)$ gives reflexivity. If $R_i(A)\subseteq R_j(A)$ and $R_j(A)\subseteq R_k(A)$, then $R_i(A)\subseteq R_k(A)$, giving transitivity.

[\[lem:reverse\]]{#lem:reverse label="lem:reverse"} If $P$ is a preorder, then $\mathsf T_n(P)=P^{\mathsf T}$.

Row $i$ of $P$ is the principal upper set $\mathord{\uparrow}i=\{x:i\le_Px\}$. We claim $$\mathord{\uparrow}i\subseteq\mathord{\uparrow}j
 \quad\Longleftrightarrow\quad j\le_Pi.$$ If the inclusion holds, reflexivity puts $i$ in $\mathord{\uparrow}i$, hence in $\mathord{\uparrow}j$, so $j\le_Pi$. Conversely, $j\le_Pi\le_Px$ implies $j\le_Px$ by transitivity. Substitution in [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"} proves the lemma.

By [\[lem:preorder\]](#lem:preorder){reference-type="ref" reference="lem:preorder"}, the image is contained in the preorders. Conversely, if $P$ is a preorder then so is $P^{\mathsf T}$, and [\[lem:reverse\]](#lem:reverse){reference-type="ref" reference="lem:reverse"} gives $$\mathsf T_n(P^{\mathsf T})=P.$$ Thus every preorder occurs in the image. Applying [\[lem:reverse\]](#lem:reverse){reference-type="ref" reference="lem:reverse"} twice after the first update gives [\[eq:T3\]](#eq:T3){reference-type="eqref" reference="eq:T3"}.

A state is periodic only if it lies in the image, hence only if it is a preorder. On the preorder image the map is transpose, so every period is one or two. A preorder is fixed exactly when it is symmetric. A reflexive, transitive, symmetric relation is an equivalence relation, and the converse is immediate. Equivalence relations on $[n]$ are counted by $B_n$; the remaining $q_n-B_n$ preorder states pair into strict cycles.

Equation [\[eq:fixed-iterates\]](#eq:fixed-iterates){reference-type="eqref" reference="eq:fixed-iterates"} follows directly. Finally, using $\zeta_{\mathsf T_n}(z)=\exp(\sum_{k\geq1}|\operatorname{Fix}(\mathsf T_n^k)|z^k/k)$, or multiplying one factor for each cycle, yields [\[eq:zeta\]](#eq:zeta){reference-type="eqref" reference="eq:zeta"}.

The numbers $q_n$ also count finite labelled topologies, a classical correspondence and enumeration problem [@ErneStege1991]. We use this census only to state the periodic population; it is not part of the residual claim.

# Quotient-poset geometry of a fibre

[\[prop:embedding\]]{#prop:embedding label="prop:embedding"} Let $P$ be a preorder and $Q=P/{\sim_P}$. Sending a source matrix $A$ to its row-support map induces a bijection to labelled embedding maps $$\label{eq:bijection}
 \mathsf T_n^{-1}(P)
 \longleftrightarrow
 \{f:Q\hookrightarrow\mathcal B_n:
       q\le_Qr\Longleftrightarrow f(q)\subseteq f(r)\}.$$ No automorphism quotient is taken: the elements of $Q$ are the distinguished equivalence classes of the fixed labelled target $P$.

Suppose $\mathsf T_n(A)=P$. By definition, $$\label{eq:iff}
 i\le_Pj\quad\Longleftrightarrow\quad R_i(A)\subseteq R_j(A).$$ If $i\sim_Pj$, both inclusions in [\[eq:iff\]](#eq:iff){reference-type="eqref" reference="eq:iff"} hold and the rows are equal. Conversely, equal rows force both relations, so the row assignment descends to an injective map $f:Q\to\mathcal B_n$. The two directions in [\[eq:iff\]](#eq:iff){reference-type="eqref" reference="eq:iff"} say exactly that $f$ preserves and reflects order.

Conversely, from an induced order embedding $f$ assign row support $f([i])$ to every $i$. Order preservation and reflection then make [\[eq:iff\]](#eq:iff){reference-type="eqref" reference="eq:iff"} hold, so the resulting Boolean matrix maps to $P$. The two constructions are inverse.

The quotient is essential. Mutual comparability in a preorder is exactly the equality forced among source rows; treating all $n$ labels as distinct would incorrectly demand an injective embedding before this forced collapse.

# Every-target inclusion--exclusion

[\[lem:coordinates\]]{#lem:coordinates label="lem:coordinates"} For any finite preorder $S$, the number of order-preserving maps $f:S\to\mathcal B_n$ is $J(S)^n$.

For coordinate $c\in[n]$, put $$U_c=\{q\in S:c\in f(q)\}.$$ The map $f$ is order preserving exactly when every $U_c$ is an upper set. The $n$ coordinates are independently chosen, giving $J(S)^n$. Conversely, the chosen upper sets recover $f(q)=\{c:q\in U_c\}$.

A nonpreorder cannot be a target by [\[lem:preorder\]](#lem:preorder){reference-type="ref" reference="lem:preorder"}. Fix a preorder $P$ and its quotient poset $Q$. Begin with all order-preserving maps $f:Q\to\mathcal B_n$. For each $(q,r)\in D_Q$, let $E_{q,r}$ be the bad event $$f(q)\subseteq f(r).$$ Avoiding every such event is precisely order reflection, and hence, by [\[prop:embedding\]](#prop:embedding){reference-type="ref" reference="prop:embedding"}, membership in the desired fibre.

If all events indexed by $S\subseteq D_Q$ are imposed, then $f$ must preserve the original order of $Q$ together with every adjoined comparison in $S$. This is equivalent to being order preserving for the reflexive--transitive closure $Q_S$. By [\[lem:coordinates\]](#lem:coordinates){reference-type="ref" reference="lem:coordinates"}, the number of such maps is $J(Q_S)^n$. Inclusion--exclusion over the bad events gives [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"}.

The formula remains valid when added comparisons identify elements in $Q_S$: upper sets depend only on the resulting preorder. Standard inclusion--exclusion and poset enumeration are used in their ordinary senses [@Stanley2012]; no algorithmic novelty is asserted.

# Exact audit and limitations

The paper-local verifier exhausts all $2^{n^2}$ matrices for $n\leq4$. For each source it independently checks preorder formation, $\mathsf T(P)=P^{\mathsf T}$, and $\mathsf T^3=\mathsf T$. It then compares the formula [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"} with direct fibre counts for every preorder target. is a compact fingerprint of the frozen run.

::: {#tab:audit}
    $n$   states   preorders   fixed   strict states   min fibre   max fibre
  ----- -------- ----------- ------- --------------- ----------- -----------
      1        2           1       1               0           2           2
      2       16           4       2               2           2           5
      3      512          29       5              24           8          24
      4   65,536         355      15             340          16         600

  : Exact theorem-interface audit. "Strict states" counts states in strict two-cycles, not cycles.
:::

The run contains 265,050 exact assertions. Enumeration supplies no step of the proofs and says nothing about novelty beyond the tested boxes.

A second, independently implemented lane does not call the inclusion--exclusion evaluator. It enumerates labelled maps into Boolean lattices, tests order preservation and reflection, expands each map class-by-class to a source matrix, and compares the resulting set with every direct fibre through $n=4$. It also checks all 219 labelled four-element posets in $\mathcal B_5$. That lane executes 13,238,845 further exact assertions; it too is only counterexample pressure.

There are also substantive limitations. Formula [\[eq:fibre\]](#eq:fibre){reference-type="eqref" reference="eq:fibre"} is exact but exponential in the number of missing ordered pairs; we do not claim an efficient general evaluator. It does not simplify the still-difficult global enumeration of labelled preorders. Most importantly, the first-step self-residual construction is owned relation-algebra background. A bounded source search did not locate the precise iterated-plus-inverse conjunction, but a non-hit is not a priority or novelty certificate.

# Conclusion

Row-support inclusion sends the full Boolean-relation cube onto the preorder stratum in one step, and principal upper sets turn the next update into order reversal. This produces a complete one-step-tail, one/two-cycle dynamical atlas. Quotienting mutual comparability exposes the inverse geometry: source rows are labelled induced Boolean-lattice representation maps, and upper-set coordinates make every fibre accessible to inclusion--exclusion. These statements form an internally verified theorem package; external release, priority, authorship, and submission remain on hold.
