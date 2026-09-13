---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--c432-local-global-reversibility"
canonical_tex: "henon_dynamics/research_c429_c433/papers/C432_local_global_reversibility/main.tex"
canonical_pdf: "henon_dynamics/research_c429_c433/papers/C432_local_global_reversibility/main.pdf"
source_sha256: "e83ee44b45b9a4be1e98a150ec05514a3f47fcbc3f87342da90cfed55d3201c8"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Everywhere-local reversibility without a global reversor

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/research_c429_c433/papers/C432_local_global_reversibility>)
- [规范 TeX](<../../../../../henon_dynamics/research_c429_c433/papers/C432_local_global_reversibility/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/research_c429_c433/papers/C432_local_global_reversibility/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/research_c429_c433/papers/C432_local_global_reversibility/PAPER_PLAN.md>)
- [BibTeX](<../../../../../henon_dynamics/research_c429_c433/papers/C432_local_global_reversibility/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We construct a composition of four generalized Hénon maps over $K=\mathbb Q(\sqrt7)$ that has a polynomial reversor over every completion of $K$, but has no polynomial reversor over $K$. The global exclusion allows arbitrary polynomial degrees and orders; the local witnesses happen to be affine involutions. The construction belongs to a scalar family for which we determine the entire polynomial reversing coset over every number field. On the Jung--van der Kulk tree, the degree cycle $(7,15,15,7)$ forces every centralizer translation to be a power of the original map. An explicit calculation of the pointwise axis stabilizer then reduces reversibility to one eighth-power equation. The classical Wang class $16$, which is an eighth power in every completion of $\mathbb Q(\sqrt7)$ but not in that field, supplies the arithmetic obstruction. The contribution is its realization for the constrained pair consisting of one map and its inverse, with all alternative polynomial reversors excluded.
author:
- Anonymous Authors
bibliography:
- references.bib
title: |
  Everywhere-local reversibility\
  without a global reversor
```

## Markdown 正文

# The all-place reversibility question {#sec:introduction}

A polynomial automorphism can be conjugate to its inverse over every completion of a number field without being conjugate to its inverse over that field. We give an explicit example in the group of polynomial automorphisms of the affine plane. The distinction concerns existence of a polynomial reversor, not just existence of a reversor in a selected affine family.

For a field $L$, let $\mathop{\mathrm{Aut}}_L(\mathbb A^2)$ denote the group of polynomial maps of the affine plane with polynomial inverses, all defined over $L$. Group multiplication is composition, with the rightmost map acting first. For $F\in\mathop{\mathrm{Aut}}_L(\mathbb A^2)$, put $$\mathop{\mathrm{Rev}}_L(F)=
  \{R\in\mathop{\mathrm{Aut}}_L(\mathbb A^2):RFR^{-1}=F^{-1}\}.$$ We call $F$ *reversible over $L$* when this set is nonempty. Our notation $\mathop{\mathrm{Rev}}_L(F)$ includes reversors only, not the union of reversors and commuting symmetries.

Let $\Omega_K$ be the set of all finite and infinite places of a number field $K$. The local-global question is whether $$\label{eq:hasse-question}
  \bigl[\mathop{\mathrm{Rev}}_{K_v}(F)\ne\varnothing
       \text{ for every }v\in\Omega_K\bigr]
  \quad\Longrightarrow\quad
  \mathop{\mathrm{Rev}}_K(F)\ne\varnothing$$ for every finite nonempty composition of generalized Hénon maps $$H_i(x,y)=(y,P_i(y)-a_i x),\qquad
  P_i\in K[y],\quad \deg P_i\ge2,\quad a_i\in K^\times.$$ There is no degree or order bound on a proposed reversor. No completion may be enlarged or omitted, and $F$ is the full ordered composition, not an iterate chosen in its place.

For $c\ne0$ and $d\ge2$, write $$\label{eq:hcd}
  H_{c,d}(x,y)=(y,cy^d-x).$$ Its inverse is $(x,y)\mapsto(cx^d-y,x)$. Each such map therefore satisfies the preceding Hénon hypotheses.

[\[thm:counterexample\]]{#thm:counterexample label="thm:counterexample"} Set $$\label{eq:counterexample}
  K=\mathbb Q(\sqrt7),\qquad
  F=H_{4,7}H_{1/16,15}H_{16,15}H_{1/4,7}.$$ For every $v\in\Omega_K$ there is an affine involution $R_v\in\mathop{\mathrm{Aut}}_{K_v}(\mathbb A^2)$ such that $R_vFR_v^{-1}=F^{-1}$. Nevertheless, $$\mathop{\mathrm{Rev}}_K(F)=\varnothing.$$ In particular, implication [\[eq:hasse-question\]](#eq:hasse-question){reference-type="eqref" reference="eq:hasse-question"} is false even when the search for a global reversor includes all polynomial degrees and orders.

Although $F$ has rational coefficients, the base field in Theorem [\[thm:counterexample\]](#thm:counterexample){reference-type="ref" reference="thm:counterexample"} is the specified field $K$. Both of its infinite places are real; it has no complex places. The local witnesses and global exclusion will be proved over precisely these fields.

The main algebraic step is an exhaustive calculation for a scalar family. For a number field $L$ and $a\in L^\times$, define $$\label{eq:family}
  F_a=H_{a,7}H_{a^{-2},15}H_{a^2,15}H_{a^{-1},7},
  \qquad R_t(x,y)=(t^{-1}y,tx)\quad(t\ne0).$$

[\[thm:family\]]{#thm:family label="thm:family"} For every number field $L$ and every $a\in L^\times$, $$\label{eq:family-classification}
  \mathop{\mathrm{Rev}}_L(F_a)=
  \{F_a^jR_t:j\in\mathbb Z,\ t\in L^\times,\ t^8=a^2\}.$$ Consequently, $F_a$ is reversible over $L$ if and only if $a^2\in L^{\times8}$.

The integer $j$ in [\[eq:family-classification\]](#eq:family-classification){reference-type="eqref" reference="eq:family-classification"} is unrestricted. The theorem is an equality for the entire polynomial reversor set, not an affine ansatz. It will also provide the explicit local construction: whenever $t^8=a^2$ in a characteristic-zero field, $R_t$ reverses $F_a$.

## Classical inputs and the distinction from conjugacy {#classical-inputs-and-the-distinction-from-conjugacy .unnumbered}

The polynomial group structure used here is classical. The Jung--van der Kulk amalgam, its reduced words, and the associated symmetry and reversor methods are described in Gómez--Meiss [@gomez2004reversors] and Baake--Roberts [@baake2005symmetries]. We specialize that machinery to one four-factor word and prove the required full centralizer equality directly. A commuting-subgroup inclusion would not suffice. In particular, the field hypothesis on roots of unity in [@baake2005symmetries Theorem 2 and Corollary 1] cannot be imposed during a calculation over $\mathbb C$.

The arithmetic obstruction is also classical. The exceptional eighth-power class over $\mathbb Q(\sqrt7)$ is recorded in Song Wang's account of the Grunwald--Wang theorem [@wang2015grunwald]; we verify every place directly below. Scalar twisting together with exhaustive centralizer descent is not a new method: the final example of Cantat--Dujardin [@cantat2024holomorphically Section 2.2] already controls the field of polynomial conjugacy of two scalar-twisted Hénon maps through their full centralizer. Combining that example with the Wang class gives an analogous all-place failure for two independently specified maps. That consequence of the cited mechanisms does not identify the second map with the first map's inverse. Here the remaining task is to realize the obstruction for the constrained pair $(F,F^{-1})$ and exclude every alternative reversor.

The proof first determines the entire geometric centralizer, including its translation image on the amalgam tree (Sections [2](#sec:axis){reference-type="ref" reference="sec:axis"}--[3](#sec:centralizer){reference-type="ref" reference="sec:centralizer"}). Section [4](#sec:descent){reference-type="ref" reference="sec:descent"} then proves Theorem [\[thm:family\]](#thm:family){reference-type="ref" reference="thm:family"} by a scalar twist and original-field descent. Section [5](#sec:places){reference-type="ref" reference="sec:places"} proves Theorem [\[thm:counterexample\]](#thm:counterexample){reference-type="ref" reference="thm:counterexample"}. The two-factor control in Section [6](#sec:control){reference-type="ref" reference="sec:control"} explains why failure of a selected affine swap cannot replace the full-group argument.

# The full polynomial group and a primitive axis {#sec:axis}

We work over $\mathbb C$ in this section and the next. Let $G=\mathop{\mathrm{Aut}}_{\mathbb C}(\mathbb A^2)$, let $\mathcal A$ be its affine subgroup, and set $$\mathcal E=
  \{(x,y)\mapsto(\alpha x+p(y),\beta y+\eta):
       \alpha\beta\ne0,\ p\in\mathbb C[y]\},\qquad
  \mathcal B=\mathcal A\cap\mathcal E.$$ Thus $\mathcal B$ consists of upper triangular affine automorphisms. The Jung--van der Kulk theorem gives the full-group equality $$\label{eq:amalgam}
  G=\mathcal A*_{\mathcal B}\mathcal E.$$ We use the reduced-word formulation: a nonempty alternating product of elements of $\mathcal A\setminus\mathcal B$ and $\mathcal E\setminus\mathcal B$ cannot belong to $\mathcal B$. The exact input is available in [@gomez2004reversors Section 2.1] and [@baake2005symmetries Section 2, Facts 1--2 and Proposition 1]. Equation [\[eq:amalgam\]](#eq:amalgam){reference-type="eqref" reference="eq:amalgam"} applies to the entire polynomial automorphism group, so the following argument does not restrict a commuting map to a chosen normal-form family.

## The tree and the axis

Construct a graph $\mathcal T$ with vertex set $G/\mathcal A\sqcup G/\mathcal E$ and edges $G/\mathcal B$: the edge $g\mathcal B$ joins $g\mathcal A$ and $g\mathcal E$. The graph is connected because $\mathcal A$ and $\mathcal E$ generate $G$. A non-backtracking closed edge path would give a nonempty alternating word of non-$\mathcal B$ elements of the two factors lying in $\mathcal B$, contrary to the reduced-word theorem. Therefore $\mathcal T$ is a tree. Give each edge length one. Left multiplication by $G$ acts by isometries and preserves the two vertex types, so no group element inverts an edge.

Put $$\tau(x,y)=(y,x),\qquad
  H_d=H_{1,d},\qquad e_d(x,y)=(-x+y^d,y).$$ Then $H_d=\tau e_d$. Define the monic word $$\label{eq:monic-word}
  F_0=H_7H_{15}H_{15}H_7
     =\tau e_7\,\tau e_{15}\,\tau e_{15}\,\tau e_7.$$ Here $F_0$ denotes the monic word, not the undefined value $a=0$ of the family [\[eq:family\]](#eq:family){reference-type="eqref" reference="eq:family"}; it equals $F_a$ when $a=1$. Each displayed factor of the last expression lies outside $\mathcal B$, and the first and last factors belong to different groups. Thus the word is cyclically reduced.

Starting from the base edge $\mathcal B$, the successive prefix edges are $$\label{eq:prefix-edges}
  \mathcal B,\quad \tau\mathcal B,\quad
  H_7\mathcal B,\quad H_7\tau\mathcal B,\quad
  \ldots,\quad F_0\mathcal B.$$ Consecutive edges meet without backtracking. Repeating this path by $F_0^j$ for $j\in\mathbb Z$ introduces no backtracking at its joins because the word is cyclically reduced. The result is a bi-infinite geodesic $\mathcal L$, translated by $F_0$ through eight edge lengths. Write $C_G(F_0)=\{h\in G:hF_0=F_0h\}$ for its centralizer.

[\[lem:axis\]]{#lem:axis label="lem:axis"} The line $\mathcal L$ is the minimal-displacement set of $F_0$. Every member of the centralizer $C_G(F_0)$ preserves $\mathcal L$ and acts on it as a translation by an even integer number of edges.

For a point $z$ in the metric tree, let $q$ be its projection to $\mathcal L$. If $z$ is off the line, its branch and the branch containing $F_0z$ attach at the distinct points $q$ and $F_0q$. The unique path from $z$ to $F_0z$ therefore has length $$\label{eq:displacement}
  d(z,F_0z)=8+2d(z,\mathcal L).$$ The same equality holds for $z\in\mathcal L$. Hence $\mathcal L$ is precisely the set on which displacement is minimal. If $hF_0=F_0h$, then $d(hz,F_0hz)=d(z,F_0z)$, so $h$ preserves this line. An orientation-reversing isometry of a line conjugates a nonzero translation to its inverse. Since $h$ commutes with $F_0$, its restriction cannot reverse orientation. It is therefore a translation, possibly the identity. It takes vertices to vertices of the same type, which forces an even edge displacement.

## An intrinsic label on each elementary turn

At an $\mathcal E$-vertex of $\mathcal L$ represented by $g\mathcal E$, its two incident axis edges have representatives $ge_1\mathcal B$ and $ge_2\mathcal B$ with $e_1,e_2\in\mathcal E$. Define $$\label{eq:turn}
  \mathop{\mathrm{turn}}(g\mathcal E)=\deg(e_1^{-1}e_2).$$ The degree of a polynomial map means the maximum of the total degrees of its coordinates.

[\[lem:turn\]]{#lem:turn label="lem:turn"} The label [\[eq:turn\]](#eq:turn){reference-type="eqref" reference="eq:turn"} is well defined for the unordered pair of incident edges, is at least two, and is preserved by the action of every element of $G$.

The two edges are distinct, so $e_1^{-1}e_2\notin\mathcal B$. It is an elementary map and hence has degree at least two. Changing the vertex representative $g$ to $ge$ replaces each $e_i$ by $e^{-1}e_i$ and leaves their relative product unchanged. Changing the edge representatives on the right by $b_1,b_2\in
\mathcal B$ replaces the relative map by $b_1^{-1}e_1^{-1}e_2b_2$. Left or right multiplication of a nonlinear elementary map by a triangular affine map preserves its degree: the substitution in $y$ is invertible affine, its leading term is rescaled by a nonzero scalar, and all other added terms have degree at most one. Exchanging the edges replaces the relative elementary map by its inverse, whose degree is the same. Finally, left multiplication by any element of $G$ leaves the relative pair of representatives unchanged. These checks prove all assertions.

Along $\mathcal L$, the labels in one orientation are $$\label{eq:label-cycle}
  \ldots,7,15,15,7,\ 7,15,15,7,\ldots.$$ This sequence has least positive shift period four: shifts one and two change its first entry, while shift three changes its second.

[\[prop:primitive-translation\]]{#prop:primitive-translation label="prop:primitive-translation"} For every $h\in C_G(F_0)$ there is $j\in\mathbb Z$ such that $h_0=hF_0^{-j}$ fixes $\mathcal L$ pointwise and still centralizes $F_0$.

By Lemma [\[lem:axis\]](#lem:axis){reference-type="ref" reference="lem:axis"}, $h$ acts by a translation. It preserves the turn labels by Lemma [\[lem:turn\]](#lem:turn){reference-type="ref" reference="lem:turn"}. Its displacement must therefore be a multiple of four $\mathcal E$-vertices, or eight edges, by [\[eq:label-cycle\]](#eq:label-cycle){reference-type="eqref" reference="eq:label-cycle"}. The map $F_0$ realizes exactly this positive displacement. Removing the corresponding signed power $F_0^j$ makes the action on $\mathcal L$ trivial, and commutation with $F_0$ is preserved.

The proposition controls every polynomial commuting map, including those of arbitrarily large degree. In particular, it rules out a shorter translation generated by a hidden root of the original word.

# The complete centralizer and geometric reversing coset {#sec:centralizer}

It remains to compute the centralizers whose action on $\mathcal L$ is trivial. For $\zeta\in\mathbb C^\times$ write $S_\zeta(x,y)=(\zeta x,\zeta^{-1}y)$, and let $\mu_8=\{\zeta\in\mathbb C:\zeta^8=1\}$.

[\[prop:centralizer\]]{#prop:centralizer label="prop:centralizer"} The full centralizer of the monic word is $$\label{eq:full-centralizer}
  C_G(F_0)=\{S_\zeta F_0^j:\zeta\in\mu_8,\ j\in\mathbb Z\}
          \cong\mu_8\times\mathbb Z.$$

Take the pointwise-axis centralizer $h_0$ supplied by Proposition [\[prop:primitive-translation\]](#prop:primitive-translation){reference-type="ref" reference="prop:primitive-translation"}. The edges $\mathcal B$ and $\tau\mathcal B$ belong to [\[eq:prefix-edges\]](#eq:prefix-edges){reference-type="eqref" reference="eq:prefix-edges"}, so their stabilizers force $$\label{eq:diagonal-affine}
  h_0\in\mathcal B\cap\tau\mathcal B\tau^{-1}
  =\{(x,y)\mapsto(\alpha x+c,\beta y+e):\alpha\beta\ne0\}.$$ The equality follows by intersecting upper and lower triangular affine maps. At this point both translations are allowed.

Let $(d_1,d_2,d_3,d_4)=(7,15,15,7)$, put $P_0=\mathrm{id}$, and set $P_i=H_{d_1}\cdots H_{d_i}$ for $1\le i\le4$. Both $P_i\mathcal B$ and $P_i\tau\mathcal B$ lie on the axis for $0\le i\le4$; the last pair belongs to the next translated segment. Thus each $h_i=P_i^{-1}h_0P_i$ is diagonal affine, and $$h_i=H_{d_i}^{-1}h_{i-1}H_{d_i}\quad(1\le i\le4),
  \qquad h_4=F_0^{-1}h_0F_0=h_0.$$

For $D(x,y)=(\alpha x+c,\beta y+e)$, direct substitution gives $$\label{eq:affine-conjugation}
  H_d^{-1}DH_d(x,y)
  =\bigl((\alpha y+c)^d-\beta y^d+\beta x-e,\ \alpha y+c\bigr).$$ For this map to be diagonal affine, the coefficient of $y^d$ must vanish, giving $\beta=\alpha^d$. The coefficient of $y^{d-1}$ is then $d\alpha^{d-1}c$, so $c=0$ in characteristic zero. The degrees used here are seven and fifteen. The resulting map is $(\beta x-e,\alpha y)$. Applying the next factor forces its first translation $-e$ to vanish. Hence both translations in [\[eq:diagonal-affine\]](#eq:diagonal-affine){reference-type="eqref" reference="eq:diagonal-affine"} are zero.

The four successive conjugations now interchange the two diagonal scalars and give precisely $$\label{eq:scalar-equations}
  \beta=\alpha^7,\qquad
  \alpha=\beta^{15},\qquad
  \beta=\alpha^{15},\qquad
  \alpha=\beta^7.$$ The first and third equations imply $\alpha^8=1$, and then $\beta=\alpha^{-1}$. Conversely, those two conditions satisfy all four equations. Moreover, $H_d^{-1}S_\zeta H_d=S_{\zeta^{-1}}$ for $d\in\{7,15\}$ and $\zeta^8=1$, so every $S_\zeta$ really commutes with $F_0$. Proposition [\[prop:primitive-translation\]](#prop:primitive-translation){reference-type="ref" reference="prop:primitive-translation"} now gives equality in [\[eq:full-centralizer\]](#eq:full-centralizer){reference-type="eqref" reference="eq:full-centralizer"}. The finite diagonal subgroup commutes with $\langle F_0\rangle$. Their intersection is trivial, since every nonzero power of $F_0$ has a nonzero axis translation. This proves the direct-product assertion as well.

[\[cor:geometric-reversors\]]{#cor:geometric-reversors label="cor:geometric-reversors"} Every polynomial reversor of $F_0$ over $\mathbb C$ belongs to the coset $$\label{eq:monic-reversors}
  \mathop{\mathrm{Rev}}_{\mathbb C}(F_0)=
  \{S_\zeta F_0^j\tau:\zeta^8=1,\ j\in\mathbb Z\}.$$

The identity $\tau H_d\tau=H_d^{-1}$ holds by direct substitution. Since the ordered word in [\[eq:monic-word\]](#eq:monic-word){reference-type="eqref" reference="eq:monic-word"} is a palindrome, $\tau F_0\tau=F_0^{-1}$. For any reversor $R$, the map $R\tau$ centralizes $F_0$. Conversely, multiplying any centralizer by $\tau$ gives a reversor. Proposition [\[prop:centralizer\]](#prop:centralizer){reference-type="ref" reference="prop:centralizer"} proves the equality.

No order condition on $R$ was used in this argument. The existence of one involution made the coset accessible; the full centralizer calculation made the answer exhaustive.

# Scalar twisting and descent over the original field {#sec:descent}

We now prove Theorem [\[thm:family\]](#thm:family){reference-type="ref" reference="thm:family"}. Fix a number field $L$ and $a\in L^\times$. Choose an embedding $L\hookrightarrow\mathbb C$ and $u\in\mathbb C$ with $u^8=a$, and set $A_u=\mathop{\mathrm{diag}}(u,u^{-1})$. These choices are proof devices for a geometric classification; the statement remains over $L$.

The identities $$\label{eq:alternating-twist}
  A_u^{-1}H_dA_u^{-1}=H_{u^{d+1},d},
  \qquad
  A_uH_dA_u=H_{u^{-(d+1)},d}$$ follow by evaluating the two coordinates. Inserting alternating $A_u$ and $A_u^{-1}$ between the four factors gives $$\begin{aligned}
  A_u^{-1}F_0A_u
  &=(A_u^{-1}H_7A_u^{-1})(A_uH_{15}A_u)
    (A_u^{-1}H_{15}A_u^{-1})(A_uH_7A_u)\notag\\
  &=H_{a,7}H_{a^{-2},15}H_{a^2,15}H_{a^{-1},7}
   =F_a. \label{eq:family-conjugation}\end{aligned}$$ The conjugated swap is $$\label{eq:twisted-swap}
  A_u^{-1}\tau A_u=R_{t_0},\qquad t_0=u^2,\qquad t_0^8=a^2.$$ Since $A_u$ commutes with all $S_\zeta$, the preceding full centralizer and reversing-coset equalities conjugate to the same equalities for $F_a$. In particular, $$\label{eq:all-geometric-twists}
  \mathop{\mathrm{Rev}}_{\mathbb C}(F_a)
  =\{F_a^jR_t:j\in\mathbb Z,\ t^8=a^2\}.$$ Indeed, $S_\zeta R_{t_0}=R_{\zeta^{-1}t_0}$, and $\zeta^{-1}t_0$ runs through all eight roots of $a^2$. Thus roots with $t^4=-a$ are retained; the necessary scalar equation is not the stronger equation $t^4=a$.

Let $R\in\mathop{\mathrm{Rev}}_L(F_a)$. After the chosen embedding, [\[eq:all-geometric-twists\]](#eq:all-geometric-twists){reference-type="eqref" reference="eq:all-geometric-twists"} writes $R=F_a^jR_t$ for some $j\in\mathbb Z$ and $t\in\mathbb C^\times$ with $t^8=a^2$. For either sign of $j$, the map $F_a^{-j}$ is a polynomial automorphism over $L$. Therefore $$F_a^{-j}R=R_t\in\mathop{\mathrm{Aut}}_L(\mathbb A^2).$$ The coefficient of $x$ in the second coordinate of $R_t$ is $t$, so $t\in L^\times$. This proves necessity in every integer component, regardless of the degree of the original $R$. Conversely, a root $t\in L^\times$ gives $R_t$ by [\[eq:all-geometric-twists\]](#eq:all-geometric-twists){reference-type="eqref" reference="eq:all-geometric-twists"}, and each $F_a^jR_t$ is then defined over $L$ and reverses $F_a$. This proves the full equality [\[eq:family-classification\]](#eq:family-classification){reference-type="eqref" reference="eq:family-classification"} and its existence criterion.

[\[lem:local-construction\]]{#lem:local-construction label="lem:local-construction"} Let $E$ be any characteristic-zero field, let $a,t\in E^\times$, and suppose $t^8=a^2$. Then the affine involution $R_t$ reverses $F_a$ over $E$.

In an algebraic closure of $E$, choose $u^8=a$ and put $t_0=u^2$. The coordinate identities [\[eq:alternating-twist\]](#eq:alternating-twist){reference-type="eqref" reference="eq:alternating-twist"}--[\[eq:twisted-swap\]](#eq:twisted-swap){reference-type="eqref" reference="eq:twisted-swap"} hold over this closure. Put $\zeta=t_0/t$; then $\zeta^8=1$. The identity $H_d^{-1}S_\zeta H_d=S_{\zeta^{-1}}$ for $d=7,15$ proves that $S_\zeta$ commutes with $F_0$. It also commutes with $A_u$, and hence with $F_a=A_u^{-1}F_0A_u$. Thus $S_\zeta R_{t_0}=R_t$ reverses $F_a$. Both sides of the reversal identity have coefficients in $E$, so the identity already holds over $E$. Finally, $R_t^2=\mathrm{id}$ by its two-coordinate formula.

The lemma constructs the witnesses over completions without requiring an embedding of a completion into $\mathbb C$. Only the global classification uses such an embedding for a number field. Removing the original-field native power in the proof of Theorem [\[thm:family\]](#thm:family){reference-type="ref" reference="thm:family"} is also essential: coefficient cancellation in a high-degree expression $F_a^jR_t$ cannot evade that operation.

# The Wang class at every original completion {#sec:places}

We give the full arithmetic check, including the dyadic and infinite places. The exceptional class itself is classical; the precise field, exponent, and class appear in the remark following Proposition 2.1 of the accessible preprint of [@wang2015grunwald].

[\[prop:wang\]]{#prop:wang label="prop:wang"} For $K=\mathbb Q(\sqrt7)$ one has $$\label{eq:wang}
  16\in K_v^{\times8}\quad\text{for every }v\in\Omega_K,
  \qquad 16\notin K^{\times8}.$$

First let $p$ be an odd rational prime. At least one of $2,-2,-1$ is a square modulo $p$. To see this, write $\chi$ for the quadratic character of $\mathbb F_p^\times$. If neither $2$ nor $-1$ is a square, then $\chi(-2)=\chi(-1)\chi(2)=1$. These three elements are nonzero modulo $p$, so each square root found there lifts to $\mathbb Q_p$ by Hensel's lemma: the derivative of $X^2-b$ is nonzero at a nonzero root modulo the odd prime $p$. If $r^2=2$ or $r^2=-2$, then $r^8=16$. If $i^2=-1$, then $$(1+i)^2=2i,\qquad (1+i)^4=-4,\qquad (1+i)^8=16.$$ Thus $\mathbb Q_p$ contains an eighth root of $16$ for every odd $p$. Each completion $K_v$ above $p$ contains $\mathbb Q_p$, proving the required statement at all these places, including those above the ramified prime seven.

Next consider the rational prime two. The element $7$ is not a square in $\mathbb Q_2$: an odd square is congruent to $1$ modulo $8$. Hence $$K\otimes_\mathbb Q\mathbb Q_2=\mathbb Q_2(\sqrt7)$$ is a field, and $K$ has exactly one place above two. On the other hand $-7$ is a square in $\mathbb Q_2$. The strong Hensel criterion for $f(X)=X^2+7$ at $X=1$ applies because $$v_2(f(1))=3>2v_2(f'(1))=2,$$ where $v_2(2)=1$. Choose $b\in\mathbb Q_2$ with $b^2=-7$. In the original dyadic completion, $i=\sqrt7/b$ satisfies $i^2=-1$. Consequently $1+i$ is an eighth root of $16$ there. Equivalently, that completion is $\mathbb Q_2(i)$.

The field $K$ is real quadratic. Both infinite completions are $\mathbb R$, and each contains $t=\sqrt2$ with $t^8=16$. There are no complex places.

Finally, any real solution of $t^8=16$ is $\sqrt2$ or $-\sqrt2$. Neither lies in $\mathbb Q(\sqrt7)$. Indeed, if $(b+c\sqrt7)^2=2$ with $b,c\in\mathbb Q$, comparison of the coefficient of $\sqrt7$ forces $bc=0$. The two alternatives would require a rational square to equal $2$ or $2/7$, respectively. Both numbers have odd $2$-adic valuation, which is impossible for a rational square. This proves [\[eq:wang\]](#eq:wang){reference-type="eqref" reference="eq:wang"}.

::: {#tab:places}
  Places                     An eighth root of $16$
  -------------------------- ---------------------------------------------------------------------------------------------------------------------
  All $v$ above odd $p$      A square root of $2$ or $-2$ in $\mathbb Q_p$, or $1+i$ when $i^2=-1$ in $\mathbb Q_p$; at least one option exists.
  The unique $v$ above $2$   $1+i$ in $K_v=\mathbb Q_2(\sqrt7)=\mathbb Q_2(i)$.
  The two real places        $\sqrt2$ in each completion $\mathbb R$.

  : The local roots used for $K=\mathbb Q(\sqrt7)$. Every row concerns the original completions. The complete proofs are in Proposition [\[prop:wang\]](#prop:wang){reference-type="ref" reference="prop:wang"}; $K$ has no complex places.
:::

Take $a=4$ in [\[eq:family\]](#eq:family){reference-type="eqref" reference="eq:family"}; the resulting $F_a$ is the word [\[eq:counterexample\]](#eq:counterexample){reference-type="eqref" reference="eq:counterexample"}, and $a^2=16$. At each original place $v$, Proposition [\[prop:wang\]](#prop:wang){reference-type="ref" reference="prop:wang"} supplies $t_v\in K_v^\times$ with $t_v^8=16$. Lemma [\[lem:local-construction\]](#lem:local-construction){reference-type="ref" reference="lem:local-construction"} gives $$R_v(x,y)=(t_v^{-1}y,t_vx),\qquad
  R_v^2=\mathrm{id},\qquad R_vFR_v^{-1}=F^{-1}$$ over that same $K_v$. If any polynomial reversor existed over $K$, Theorem [\[thm:family\]](#thm:family){reference-type="ref" reference="thm:family"} would force an eighth root of $16$ in $K$, contrary to Proposition [\[prop:wang\]](#prop:wang){reference-type="ref" reference="prop:wang"}. This excludes all global polynomial reversors, not only the local affine formulas.

# A two-factor control and the scope of the result {#sec:control}

The two-factor analogue shows why a failed affine equation is not a global obstruction. Consider $$T=H_{4,7}H_{1/4,7},\qquad X=y^7/4-x.$$ Then $T(x,y)=(X,4X^7-y)$. Define polynomial involutions over $K$ by $$E_1(x,y)=(y^7/4-x,y),\qquad
  E_2(x,y)=(x,4x^7-y).$$ Direct substitution gives $E_1^2=E_2^2=\mathrm{id}$ and $T=E_2E_1$. Consequently $$E_1TE_1=E_1E_2=T^{-1}.$$ Thus $T$ is globally reversible by a nonlinear polynomial involution. In contrast, the second coordinate of $R_tTR_t$ is $(t^8/4)x^7-y$, whereas the second coordinate of $T^{-1}$ is $4x^7-y$. A reversor of the selected form $R_t$ would therefore require $t^8=16$, which has no solution in $K$ by Proposition [\[prop:wang\]](#prop:wang){reference-type="ref" reference="prop:wang"}. Its repeated degree cycle does not give the primitive four-factor translation restriction established for $F_0$. This control identifies the role of the whole-group argument: one must exclude the other polynomial reversing components, not only a chosen scalar formula.

Theorem [\[thm:counterexample\]](#thm:counterexample){reference-type="ref" reference="thm:counterexample"} gives a negative answer to [\[eq:hasse-question\]](#eq:hasse-question){reference-type="eqref" reference="eq:hasse-question"} for one original nonlinear map. The supporting family criterion is part of that same construction. Neither theorem classifies all reversible Hénon words or asserts that this example has minimal degree or shortest possible word length. No integrality or good-reduction hypothesis is imposed. The arithmetic obstruction, the amalgam methods, and scalar-twist descent remain classical inputs; the conclusion concerns their realization for the intrinsic symmetry relating $F$ to $F^{-1}$.

## Preparation and verification {#preparation-and-verification .unnumbered}

This manuscript was prepared with AI assistance and current-team internal mathematical and source review. Those checks are not external peer review or publication acceptance. The complete construction and exclusion arguments are included above; their classical inputs are the cited amalgam theorem and basic local-field facts, including Hensel's lemma. No numerical experiment or computer-algebra verification is used as a premise.
