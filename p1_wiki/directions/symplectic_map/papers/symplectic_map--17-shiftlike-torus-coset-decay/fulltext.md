---
p1_kind: "derived-fulltext-reading-copy"
route: "symplectic_map"
logical_paper_id: "symplectic_map--17-shiftlike-torus-coset-decay"
canonical_tex: "symplectic_map/papers/17-shiftlike-torus-coset-decay/paper/main.tex"
canonical_pdf: "symplectic_map/papers/17-shiftlike-torus-coset-decay/paper/main.pdf"
source_sha256: "9cf03af659631ad7ec4228c05927733c620b111bb3840fa3555b32325cfcc977"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Sharp Torus-Coset Decay for Sparse Shift-Like Recurrences: Constant Anchors and the Exact Zero-Constant Boundary

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symplectic_map/papers/17-shiftlike-torus-coset-decay>)
- [规范 TeX](<../../../../../symplectic_map/papers/17-shiftlike-torus-coset-decay/paper/main.tex>)
- [关联 PDF](<../../../../../symplectic_map/papers/17-shiftlike-torus-coset-decay/paper/main.pdf>)
- [支撑 Markdown](<../../../../../symplectic_map/papers/17-shiftlike-torus-coset-decay/notes/CLAIMS_EVIDENCE_MATRIX.md>)
- [BibTeX](<../../../../../symplectic_map/papers/17-shiftlike-torus-coset-decay/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We determine how many multiplicative torus directions can survive a finite window of a sparse shift-like recurrence. For a type-$\nu$ map in dimension $k$, when the defining polynomial has a nonzero constant term and at least two actual nonconstant monomials, every connected torus translate contained in the $m$-step survivor variety has dimension at most $k-m$ for $0\leq m\leq k$. We construct saturated subtori attaining equality at every window and compatible rank-one examples with an infinite $(k-1)$-step arithmetic survivor set. At the next step, the arithmetic survivor set is finite for every finite-rank multiplicative subgroup over any characteristic-zero field, including groups with arbitrary torsion. We then delete the constant term and classify the planar boundary. Linear support retains a one-dimensional coset in every window. Among nonlinear supports, a positive-dimensional two-step coset occurs only for $P(X)=\beta X+\delta X^d$ on $a=-\beta^2$; there the coset is explicit and unique, and it cannot survive a third step. Every other nonlinear support closes after two steps. The proof combines character-basis cancellation, an integral pivot argument, and an exhaustive local pairing calculus. The arithmetic conclusions follow from a qualitative torus-intersection theorem after an internal division-hull and field-embedding reduction. They provide no effective cardinality or enumeration.
author:
- Anonymous
bibliography:
- references.bib
title: |
  Sharp Torus-Coset Decay for Sparse Shift-Like Recurrences:\
  Constant Anchors and the Exact Zero-Constant Boundary
```

## Markdown 正文

# Introduction and anchor-loss question {#sec:introduction}

A finite segment of a polynomial recurrence can impose much more multiplicative rigidity than any one of its equations suggests. The natural geometric object is not a single orbit but the locus of all scalar strings satisfying a prescribed number of successive recurrence equations inside an algebraic torus. A translate of a subtorus contained in that locus records a family in which some multiplicative parameters remain free throughout the window. The basic question is therefore quantitative: how many independent torus parameters survive after $m$ transitions?

We answer this question for the type-$\nu$ shift-like recurrence $$x_{n+k}=P(x_{n+k-\nu})+a x_n,
\label{eq:intro-recurrence}$$ where $k\geq2$, $1\leq\nu\leq k-1$, and $a\neq0$. When $P$ has a nonzero constant term and at least two actual nonconstant monomials, every connected torus translate in the $m$-transition survivor variety has dimension at most $k-m$ for $0\leq m\leq k$. The loss of one direction per equation is sharp at every window: under an explicit coefficient condition, a saturated subtorus of dimension $k-m$ lies in the survivor variety. At $m=k-1$ this construction can meet a rank-one multiplicative group infinitely, whereas at $m=k$ a qualitative theorem on intersections with division groups makes every finite-rank arithmetic survivor set finite.

The source of the exact deficit is a fixed character supplied by the constant term. On restricting one recurrence equation to a torus translate, each coordinate becomes a scalar times a character. If the middle character were nontrivial, the constant and at least two distinct powers would give three distinct group-algebra characters, while the lag and output contribute only two further terms. Some nonzero term would remain unpaired. Once the middle character is forced to be trivial, the equation supplies two integral lattice relations. We prove that the resulting $2m$ relations are independent, including when middle coordinates have already moved into the future part of the window.

This mechanism poses a precise boundary question: what survives if the constant character is removed? In the planar zero-constant recurrence, a local equation has two endpoints and the power terms of its middle coordinate. Linear support retains a one-dimensional coset in every finite window. For nonlinear support, two endpoint terms can pair with two distinct powers only in two orientations. Composing those orientations leaves one word, forces support $\{1,d\}$, and then forces the coefficient relation $a=-\beta^2$. The resulting two-step coset is explicit and unique, but a third recurrence closes it. Thus the second theorem is the exact failure analysis of the first theorem's anchoring step, rather than an independent classification attached to it.

Our contributions are the following.

1.  We prove the sharp all-window dimension bound $\dim H\leq k-m$ for anchored type-$\nu$ recurrences, with no arithmetic genericity and no condition involving $\gcd(k,\nu)$.

2.  We construct saturated equality subtori at every window and compatible rank-one examples showing that the arithmetic threshold between $k-1$ and $k$ transitions cannot be lowered uniformly.

3.  We classify the planar zero-anchor phase: the sole nonlinear two-step resonance is $\{1,d\}$ on $a=-\beta^2$, its positive-dimensional coset is unique, and every nonlinear support has no positive-dimensional coset after three transitions.

Shift-like polynomial maps originate in the complex-dynamical study of higher-dimensional polynomial automorphisms; the standard family and type convention appear in [@BedfordPambuccian1998], with further complex-dynamical developments in [@Bera2018; @BeraVerma2013]. Those works concern analytic and dynamical structure rather than finite-rank survivor windows. The group-algebra fact that distinct characters are linearly independent is also standard. Our contribution is not that fact in isolation, but the recurrence-specific integral relation law and the exhaustive anchor-loss classification built from it. The literature comparison used here is bounded and does not support a global priority or exhaustive-search claim.

Section [2](#sec:setup){reference-type="ref" reference="sec:setup"} fixes the scalar indexing, survivor varieties, and the qualitative arithmetic bridge. Section [3](#sec:characters){reference-type="ref" reference="sec:characters"} develops the character lemmas. Sections [4](#sec:anchored){reference-type="ref" reference="sec:anchored"} and [5](#sec:equality){reference-type="ref" reference="sec:equality"} prove and sharpen the anchored theorem. Sections [6](#sec:local){reference-type="ref" reference="sec:local"} and [7](#sec:phase){reference-type="ref" reference="sec:phase"} classify the zero-anchor boundary. Section [8](#sec:boundaries){reference-type="ref" reference="sec:boundaries"} records the exact assumption and comparison boundaries before concluding.

# Shift-like recurrences, survivor varieties, and the Laurent bridge {#sec:setup}

## Map, scalar orientation, and windows

Let $\Omega$ be an algebraically closed field of characteristic zero. Fix $$k\geq2,\qquad 1\leq\nu\leq k-1,\qquad a\in\Omega^*.$$ For $P\in\Omega[X]$, define the type-$\nu$ shift-like map $$S(z_1,\ldots,z_k)
 =\bigl(z_2,\ldots,z_k,P(z_{k-\nu+1})+az_1\bigr).
\label{eq:map}$$ It is a polynomial automorphism. If $w=S(z)$, then $$z_1=a^{-1}\bigl(w_k-P(w_{k-\nu})\bigr),
\qquad z_i=w_{i-1}\quad(2\leq i\leq k).$$ The location $k-\nu+1$ in the one-based state coordinates becomes $n+k-\nu$ in zero-based scalar coordinates. Namely, if the time-$n$ state is $$S^n(x_0,\ldots,x_{k-1})=(x_n,\ldots,x_{n+k-1}),$$ then the last coordinate of the next state gives $$x_{n+k}=P(x_{n+k-\nu})+a x_n.
\label{eq:recurrence}$$ This orientation will remain fixed throughout the article.

For $m\geq0$, let $V_m\subset\mathbb{G}_{m}^{k+m}$, with coordinates $x_0,\ldots,x_{k+m-1}$, be cut out by $$x_{n+k}=P(x_{n+k-\nu})+a x_n,
\qquad 0\leq n<m.
\label{eq:Vm}$$ We set $V_0=\mathbb{G}_{m}^k$.

The equations in [\[eq:Vm\]](#eq:Vm){reference-type="eqref" reference="eq:Vm"} are Laurent-polynomial equations on the ambient torus, so $V_m$ is closed there. They also give a useful scheme-level sanity check. Start with $$A_0=\Omega[x_0^{\pm1},\ldots,x_{k-1}^{\pm1}].$$ At stage $n$, all coordinates appearing on the right side of the $n$th recurrence have already been expressed in the preceding ring. Write that expression as $g_n=P(x_{n+k-\nu})+ax_n$. Eliminating the monic variable $x_{n+k}$ and retaining its invertibility replaces the current domain $A_n$ by the localization $$A_{n+1}=A_n[g_n^{-1}].$$ Induction identifies the coordinate ring of $V_m$ with an iterated localization of $A_0$. It is therefore a domain, and $V_m$ is integral. No later character argument relies on a set-theoretic replacement of the defining scheme.

Here is the ring induction in full. After the first $n$ equations have been imposed, let $$R_n=\Omega[x_0^{\pm1},\ldots,x_{k+n-1}^{\pm1}]
 /(x_{k+j}-P(x_{k+j-\nu})-a x_j:0\leq j<n).$$ The inductive isomorphism identifies $R_n$ with $A_n$ and sends every coordinate already created to its recursively determined Laurent function. Adjoining the next invertible coordinate and its equation gives $$R_{n+1}\simeq
 A_n[y,y^{-1}]/(y-g_n).$$ Evaluation at $y=g_n$ defines a homomorphism from this quotient to $A_n[g_n^{-1}]$. In the other direction, the image of $y^{-1}$ is an inverse for $g_n$, so the universal property of localization supplies the inverse homomorphism. Thus $$A_n[y,y^{-1}]/(y-g_n)\simeq A_n[g_n^{-1}]$$ as rings, not merely on closed points. The function $g_n$ is nonzero: it is the next scalar-coordinate function obtained from an iterate of the polynomial automorphism [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"}, and an automorphism cannot pull a nonzero coordinate function back to zero. Localization therefore preserves the domain property at every step. This also proves inductively that no embedded or extra irreducible component is hidden by the recurrence notation.

The order of elimination matters only for clarity, not for the resulting variety. At the $n$th stage, the index $n+k-\nu$ is strictly smaller than $n+k$ because $\nu\geq1$. It is therefore either an initial coordinate or one of the future coordinates eliminated at an earlier stage. The recurrence is monic in the new coordinate $x_{n+k}$, so it introduces no algebraic choice and no extra component. Requiring $x_{n+k}\neq0$ in the ambient torus is exactly the localization at $g_n$. This induction also shows that the projection from $V_m$ to the initial-coordinate torus is an open immersion onto the locus where all successive recurrence expressions are nonzero. We shall not use that stronger description, but it explains why the scalar string is determined without multiplicity.

All geometric containment statements are understood after extension to $\Omega$. Extending the ground field preserves the equations, the torus structure, and the dimension of a contained coset. Conversely, the arithmetic point set in [\[eq:projection\]](#eq:projection){reference-type="eqref" reference="eq:projection"} is formed over the stated field $K$. Keeping these two ground fields separate prevents the later complex embedding argument from being mistaken for an assumption on the original field.

Now let $K$ be any characteristic-zero field over which the coefficients are defined, and let $\Gamma\leq K^*$ have finite rank. We use $$T_m(S,\Gamma)=\{z\in\Gamma^k:S^j(z)\in\Gamma^k
 \text{ for every }0\leq j\leq m\}.
\label{eq:Tm}$$ Thus $m$ counts transitions and equations; the retained states occur at times $0,1,\ldots,m$. Each initial tuple determines its future scalar coordinates uniquely through [\[eq:recurrence\]](#eq:recurrence){reference-type="eqref" reference="eq:recurrence"}. Projection to the first $k$ coordinates consequently gives a bijection $$V_m\cap\Gamma^{k+m}\longrightarrow T_m(S,\Gamma).
\label{eq:projection}$$ Dimension statements below concern torus translates contained in the geometric variety $V_m$. They are not dimension statements about the arithmetic set $T_m$.

The windows are nested on arithmetic points: $$T_{m+1}(S,\Gamma)\subseteq T_m(S,\Gamma).$$ There is also a compatible truncation map $V_{m+1}\to V_m$, but the geometric varieties need not be subgroups and their dimensions alone do not control the size of their intersections with $\Gamma^{k+m}$. The bridge from geometry to arithmetic will instead use the structure of finite-rank intersections with torus subvarieties.

## The qualitative torus-intersection input

We use one external proof theorem, in a qualitative form due to Laurent [@Laurent1984]. If $X$ is a closed subvariety of a complex algebraic torus and $\Lambda$ is a finitely generated subgroup, write $$\Lambda^{\mathrm{div}}=\{g:g^N\in\Lambda\text{ for some }N\geq1\}.$$ Laurent's theorem implies that $X\cap\Lambda^{\mathrm{div}}$ is a finite union of intersections with torus cosets contained in $X$. We need only the following immediate consequence.

The cosets in this statement are geometric cosets in the ambient algebraic torus. Their occurrence is not inferred from an abstract decomposition of the arithmetic group. This distinction is why our task is to exclude positive-dimensional cosets from $V_k$, $V_2^0$, or $V_3^0$ before applying the theorem. Laurent's result does not supply any of the recurrence-specific character relations proved in later sections.

[\[cor:laurent\]]{#cor:laurent label="cor:laurent"} If $X$ contains no positive-dimensional torus coset, then $X\cap\Lambda^{\mathrm{div}}$ is finite.

Every torus coset supplied by the theorem and contained in $X$ is then zero-dimensional. Such a coset is a point, so a finite union of its intersections with $\Lambda^{\mathrm{div}}$ is finite.

## Finite rank, arbitrary torsion, and arbitrary fields

The complex theorem applies to division groups of finitely generated groups. Our arithmetic statements concern arbitrary finite-rank subgroups, which need not be finitely generated and may have unbounded or infinite torsion. The next two lemmas provide the required bridge rather than silently strengthening the imported theorem.

[\[lem:division-hull\]]{#lem:division-hull label="lem:division-hull"} Let $\Gamma$ be an abelian multiplicative group such that $\operatorname{rank}(\Gamma/\Gamma_{\mathrm{tor}})=r<\infty$. There is a finitely generated subgroup $\Gamma_0\leq\Gamma$ for which $\Gamma\subseteq\Gamma_0^{\mathrm{div}}$.

Choose $\gamma_1,\ldots,\gamma_r$ whose classes form a $\mathbb{Q}$-basis of $\Gamma\otimes_{\mathbb{Z}}\mathbb{Q}$, and put $\Gamma_0=\langle\gamma_1,\ldots,\gamma_r\rangle$. For $\gamma\in\Gamma$, clearing denominators in the rational relation for its class gives integers $N>0$ and $n_i$ such that $$\tau=\gamma^N\prod_{i=1}^r\gamma_i^{-n_i}$$ is torsion. The individual element $\tau$ has some finite order $M$. Raising the displayed relation to the $M$th power gives $\gamma^{NM}\in\Gamma_0$, and hence $\gamma\in\Gamma_0^{\mathrm{div}}$.

The exponent $M$ is allowed to depend on $\gamma$. Thus the argument assumes neither bounded torsion nor finite generation of $\Gamma$. It includes arbitrary infinite torsion: every root of unity has finite order and already belongs to the division hull of the identity.

[\[lem:field-transfer\]]{#lem:field-transfer label="lem:field-transfer"} Let $X\subset\mathbb{G}_{m}^N$ be defined over a characteristic-zero field $K$, and let $\Gamma\leq K^*$ have finite rank. If $X$ contains no positive-dimensional torus coset after extension to an algebraic closure, then $X\cap\Gamma^N$ is finite.

Choose $\Gamma_0$ as in Lemma [\[lem:division-hull\]](#lem:division-hull){reference-type="ref" reference="lem:division-hull"}. Let $L$ be the subfield generated over $\mathbb{Q}$ by the finitely many coefficients defining $X$ and the finitely many generators of $\Gamma_0$. The field $L$ is finitely generated over $\mathbb{Q}$ and embeds in $\mathbb{C}$. Every $\gamma\in\Gamma$ is algebraic over $L$, because a positive power of $\gamma$ belongs to $\Gamma_0$. Extend the chosen embedding of $L$ to an algebraic closure containing the relevant elements. We do not assert that the whole field $K$ embeds in $\mathbb{C}$.

Under the extended embedding, every point of $X\cap\Gamma^N$ lies in the division hull of the finitely generated group $\Gamma_0^N$. The absence of a positive-dimensional torus coset is preserved by the field embedding. Corollary [\[cor:laurent\]](#cor:laurent){reference-type="ref" reference="cor:laurent"} makes the embedded intersection finite, and injectivity transfers finiteness back. The same reasoning applies in every Cartesian power needed below.

Lemmas [\[lem:division-hull\]](#lem:division-hull){reference-type="ref" reference="lem:division-hull"} and [\[lem:field-transfer\]](#lem:field-transfer){reference-type="ref" reference="lem:field-transfer"} retain the distinction between finite rank and finite generation. They also explain why arbitrary torsion, including all roots of unity when present, is within the theorem's scope.

Two details of this reduction are useful later. First, the power that places one element of $\Gamma$ in $\Gamma_0$ need not work for any other element. Uniform torsion control is neither asserted nor needed. Second, a point of $X\cap\Gamma^N$ has finitely many coordinates, each algebraic over $L$ by its power relation. All coordinates therefore lie in one finite algebraic extension of $L$ for that point, inside the fixed algebraic closure to which the embedding has been extended. The complex intersection theorem controls all such points at once because they all lie in $(\Gamma_0^N)^{\mathrm{div}}$. This is an elementwise division-hull argument, not an attempt to embed an arbitrary large characteristic-zero field in $\mathbb{C}$.

For clarity, the field transfer may be read coordinatewise. The subgroup $\Gamma_0^N$ is finitely generated by the finitely many vectors that place one generator of $\Gamma_0$ in one coordinate and $1$ in the others. If $g=(g_1,\ldots,g_N)\in\Gamma^N$, then for each $i$ some positive power of $g_i$ lies in $\Gamma_0$; taking the product of those finitely many exponents shows that one common positive power of $g$ lies in $\Gamma_0^N$. Hence $g\in(\Gamma_0^N)^{\mathrm{div}}$. This common exponent is attached to the point and is not required to be uniform over the intersection.

Likewise, only the algebraic extension generated by elements of $\Gamma$ is embedded. Once $L\hookrightarrow\mathbb{C}$ is fixed, the embedding-extension property for algebraic field extensions places the algebraic field $L(\Gamma)$ inside an algebraic closure of the image of $L$ in $\mathbb{C}$. The defining coefficients of $X$ already lie in $L$, so evaluation commutes with this injection. A positive-dimensional coset in the resulting complex base change would remain such after passage to a common algebraically closed overfield, contradicting the geometric hypothesis. We may therefore apply Corollary [\[cor:laurent\]](#cor:laurent){reference-type="ref" reference="cor:laurent"} to the single complex variety and the single division group $(\Gamma_0^N)^{\mathrm{div}}$. Injectivity then returns distinct complex points to distinct original points. Neither a bound on torsion orders nor an embedding of all of $K$ has entered.

# Characters on recurrence cosets {#sec:characters}

The geometric arguments take place on a translate $\xi H$ of a connected subtorus of an ambient torus. We record the character facts in a form that applies to both the anchored and zero-anchor recurrences.

## Restriction to a group algebra

Let $M=X^*(H)$ be the character lattice of $H$. Because $H$ is connected, $M$ is a free abelian group. If $x_i$ is an ambient coordinate, then its restriction to $\xi H$ has the form $$x_i|_{\xi H}=\xi_i\chi_i,
\qquad \xi_i\in\Omega^*,\quad \chi_i\in M.
\label{eq:coordinate-restriction}$$ Here and below the same symbol $\chi_i$ denotes both a character and its basis monomial in the group algebra $\Omega[M]$.

The scalar $\xi_i$ records the chosen translate and is always nonzero because the ambient space is a torus. The character $\chi_i$ records variation along $H$. A coordinate is constant on the coset precisely when $\chi_i=1$. This separation lets us treat character coincidences and scalar cancellations in the correct order: first collect all summands carrying the same character, then inspect the scalar coefficient of each collected block. In particular, two distinct monomials of $P$ may cancel after the middle character has become trivial; that possibility is the reason for the exact $P(\xi)$ split in both parts of the article.

[\[lem:singleton\]]{#lem:singleton label="lem:singleton"} Suppose $$\sum_{i=1}^r c_i\chi_i=0\qquad\text{in }\Omega[M],$$ where every $c_i$ is nonzero. After equal characters are collected, every coefficient is zero. In particular, a character occurring in exactly one nonzero summand is impossible.

The coordinate ring of $H$ is the group algebra $\Omega[M]$. Its character monomials form an $\Omega$-basis, so their coefficients in any identity vanish separately.

[\[lem:distinct-powers\]]{#lem:distinct-powers label="lem:distinct-powers"} If $\chi\in M$ is nontrivial and $0<e_1<\cdots<e_s$, then $1,\chi^{e_1},\ldots,\chi^{e_s}$ are pairwise distinct.

An equality $\chi^u=\chi^v$ gives $(u-v)\chi=0$ in additive notation for $M$. Torsion-freeness forces $u=v$. The same argument shows that a positive power of a nontrivial character is nontrivial.

The singleton rule and torsion-freeness are standard character theory. The work below lies in identifying exactly which recurrence-specific relations they force and proving that those relations remain independent across a full window.

The lemma does not say that every term in a restricted recurrence must be paired with exactly one other term. Several summands may share a character, and their coefficients may add to zero. What it does say is decisive: after all such aggregation, no block with a single nonzero coefficient can remain. Our anchored proof produces a singleton among at least three distinct constant-or-power characters. Our zero-anchor proof instead enumerates all partitions of four terms that avoid a singleton. Stating the rule at the aggregated level prevents coefficient cancellation from being silently discarded.

## Ambient generation and connected components

For an embedded connected subtorus $H\leq\mathbb{G}_{m}^N$, restriction gives a surjection $$\varphi:\mathbb{Z}^N=X^*(\mathbb{G}_{m}^N)\longrightarrow X^*(H),
\qquad \varepsilon_i\longmapsto\chi_i.
\label{eq:ambient-map}$$ Thus all ambient coordinate characters generate $X^*(H)$, and $$\dim H=\operatorname{rank}X^*(H)=\operatorname{rank}\operatorname{im}\varphi.
\label{eq:dimension-rank}$$ This generation statement is indispensable: showing that a selected list of coordinate characters vanishes would not control dimension unless the future coordinates were also accounted for.

One can also see surjectivity in [\[eq:ambient-map\]](#eq:ambient-map){reference-type="eqref" reference="eq:ambient-map"} directly. The inclusion $H\hookrightarrow\mathbb{G}_{m}^N$ is a closed immersion of diagonalizable groups. On character groups it becomes a quotient of the free ambient lattice by the saturated lattice of monomial relations defining $H$. Consequently, the rank of any explicitly constructed subgroup of $\ker\varphi$ subtracts from the ambient rank. The proof of Theorem [\[thm:anchored\]](#thm:anchored){reference-type="ref" reference="thm:anchored"} will construct a rank-$2m$ subgroup of this kernel over $\mathbb{Z}$, so no saturation or rational-rank ambiguity can weaken the dimension estimate.

The connected hypothesis loses no dimension information for a possibly disconnected algebraic subgroup. If $D$ is such a subgroup and $\xi D\subset X$, then $D$ is a finite union of translates of its identity component $D^0$. Each corresponding translate of $D^0$ is contained in $X$, and $$\dim D=\dim D^0.
\label{eq:component-dimension}$$ We therefore carry out every lattice argument on a connected torus and pass to components only after the argument is complete.

This order separates two kinds of torsion that should not be confused. $X^*(H)$ is torsion-free because $H$ is connected, which permits deductions such as $(d^2-1)u=0\Rightarrow u=0$. The arithmetic group $\Gamma$, on the other hand, may contain arbitrary torsion. Its torsion is handled by Lemma [\[lem:division-hull\]](#lem:division-hull){reference-type="ref" reference="lem:division-hull"} and is never inserted into the geometric character lattice.

## The restricted recurrence identity

Consider $\xi H\subset V_m$ and use [\[eq:coordinate-restriction\]](#eq:coordinate-restriction){reference-type="eqref" reference="eq:coordinate-restriction"}. The $n$th recurrence restricts to $$\xi_{n+k}\chi_{n+k}
-a\xi_n\chi_n
-P\bigl(\xi_{n+k-\nu}\chi_{n+k-\nu}\bigr)=0
\qquad\text{in }\Omega[M].
\label{eq:restricted-recurrence}$$ The signs and indices in this identity will be used without alteration. In the anchored case the polynomial expansion contains the trivial character and at least two distinct power characters. In the zero-anchor case, the trivial character disappears and the remaining terms must be classified by their possible partitions. This is the common point from which the two parts diverge.

The ambient coordinate characters in [\[eq:restricted-recurrence\]](#eq:restricted-recurrence){reference-type="eqref" reference="eq:restricted-recurrence"} include future coordinates. We shall never assume in advance that they are generated by the initial coordinates through the recurrence. Instead, the anchored equations themselves will first yield the copy relations $\chi_{n+k}=\chi_n$, after which future middle indices can safely be reduced to initial residues. In the planar zero-anchor case, adjacent local labels play the analogous role: the output character of one equation is the middle character of the next, and the compatibility of those two descriptions is what closes almost every branch.

# Sharp anchored torus-coset decay {#sec:anchored}

Throughout this section, write the polynomial in collected form $$P(X)=c+\sum_{j=1}^s b_jX^{e_j},
\qquad 0<e_1<\cdots<e_s,
\label{eq:anchored-P}$$ where $a,c,b_1,\ldots,b_s$ are nonzero and $s\geq2$. The word "actual" means that equal exponents have already been combined and every resulting zero coefficient has been deleted.

[\[thm:anchored\]]{#thm:anchored label="thm:anchored"} For every $0\leq m\leq k$, let $H$ be a connected embedded subtorus of $\mathbb{G}_{m}^{k+m}$. If $\xi H\subseteq V_m$, then $$\dim H\leq k-m.
\label{eq:dimension-bound}$$ If $D$ is a possibly disconnected algebraic subgroup and $\xi D\subseteq V_m$, every component of $D$ is a translate of $D^0$, and hence the same bound holds for $\dim D$.

## Two relations from one equation

Fix $\xi H\subseteq V_m$, put $M=X^*(H)$, and write every restricted coordinate as in [\[eq:coordinate-restriction\]](#eq:coordinate-restriction){reference-type="eqref" reference="eq:coordinate-restriction"}. For $0\leq n<m$, abbreviate $$t=k+n-\nu.$$ Expanding [\[eq:restricted-recurrence\]](#eq:restricted-recurrence){reference-type="eqref" reference="eq:restricted-recurrence"} by [\[eq:anchored-P\]](#eq:anchored-P){reference-type="eqref" reference="eq:anchored-P"} gives $$\xi_{n+k}\chi_{n+k}-a\xi_n\chi_n-c
-\sum_{j=1}^s b_j\xi_t^{e_j}\chi_t^{e_j}=0.
\label{eq:anchored-identity}$$

Suppose first that $\chi_t$ is nontrivial. Lemma [\[lem:distinct-powers\]](#lem:distinct-powers){reference-type="ref" reference="lem:distinct-powers"} says that $$1,\chi_t^{e_1},\ldots,\chi_t^{e_s}$$ are $s+1\geq3$ distinct characters, all occurring with nonzero coefficients in [\[eq:anchored-identity\]](#eq:anchored-identity){reference-type="eqref" reference="eq:anchored-identity"}. The lag character $\chi_n$ and output character $\chi_{n+k}$ can match at most two of them. At least one constant-or-power character remains a nonzero singleton, contradicting Lemma [\[lem:singleton\]](#lem:singleton){reference-type="ref" reference="lem:singleton"}. Hence every equation forces $$\chi_{k+n-\nu}=1.
\label{eq:middle-trivial}$$ This conclusion uses both the nonzero constant and the two distinct nonconstant powers; an informal count that ignores collected coefficients would not suffice.

To make the counting step explicit, the endpoint characters are allowed to coincide with one another, with the trivial character, or with power characters. None of these coincidences can cover more than two members of the set $\{1,\chi_t^{e_1},\ldots,\chi_t^{e_s}\}$ because there are only two endpoint summands. If the endpoints coincide with each other, they cover at most one member and the contradiction is stronger. Every coefficient attached to a constant-or-power character is nonzero before aggregation: $c\neq0$ and $b_j\xi_t^{e_j}\neq0$. Thus the uncovered member really is a nonzero singleton. This argument is uniform in the numerical values of the coefficients and does not invoke a generic choice.

After [\[eq:middle-trivial\]](#eq:middle-trivial){reference-type="eqref" reference="eq:middle-trivial"}, all polynomial terms in the restricted equation aggregate to a scalar: $$\xi_{n+k}\chi_{n+k}-a\xi_n\chi_n-P(\xi_t)=0.
\label{eq:aggregated}$$ There are exactly two scalar branches. If $P(\xi_t)\neq0$, the trivial character occurs with nonzero coefficient. If the endpoint characters were distinct, one would be a singleton; if they were equal and nontrivial, the trivial character would be a singleton. Therefore $$\chi_n=\chi_{n+k}=1
\qquad\text{when }P(\xi_t)\neq0.
\label{eq:nonroot-branch}$$ If $P(\xi_t)=0$, equation [\[eq:aggregated\]](#eq:aggregated){reference-type="eqref" reference="eq:aggregated"} has two nonzero terms. They must have the same character and cancel scalarly, giving $$\chi_{n+k}=\chi_n,
\qquad \xi_{n+k}=a\xi_n.
\label{eq:root-branch}$$ The zero branch is not a genericity exception: it retains the endpoint-copy relation needed below. In both branches we obtain $$\chi_{k+n-\nu}=1,
\qquad \chi_{k+n}=\chi_n.
\label{eq:two-character-relations}$$

These two branches exhaust coefficient cancellation after the middle character is trivial. Indeed, all polynomial summands then carry the same trivial character, and their total coefficient is exactly $-P(\xi_t)$. There is no finer partition to consider. When this total is nonzero, both endpoint characters are killed; when it is zero, the two endpoint terms cancel each other and give the character and scalar copies in [\[eq:root-branch\]](#eq:root-branch){reference-type="eqref" reference="eq:root-branch"}. In the stronger nonroot branch the relation $\chi_{n+k}=\chi_n$ still holds because both sides are trivial.

## Integral independence

Let $\varepsilon_0,\ldots,\varepsilon_{k+m-1}$ be the standard basis of the ambient character lattice, and let $\varphi$ be the surjection in [\[eq:ambient-map\]](#eq:ambient-map){reference-type="eqref" reference="eq:ambient-map"}. For $0\leq n<m$, define $$A_n=\varepsilon_{k+n-\nu},
\qquad B_n=\varepsilon_{k+n}-\varepsilon_n.
\label{eq:AnBn}$$ Relations [\[eq:two-character-relations\]](#eq:two-character-relations){reference-type="eqref" reference="eq:two-character-relations"} place all $A_n$ and $B_n$ in $\ker\varphi$. Table [1](#tab:pivots){reference-type="ref" reference="tab:pivots"} records the supports used in the independence proof; the argument following the table proves each entry.

The use of the full ambient lattice is deliberate. A middle pivot $A_n$ may itself be a future coordinate, and a copy relation $B_n$ always links an initial coordinate to a future one. Counting only relations among the initial variables before proving how future characters reduce would invite circular reasoning. In $\mathbb{Z}^{k+m}$, by contrast, every relation has the literal support shown in Table [1](#tab:pivots){reference-type="ref" reference="tab:pivots"}, so independence can be checked coordinate by coordinate.

::: {#tab:pivots}
  Relation   Support                        Distinguished coordinate   Consequence
  ---------- ------------------------------ -------------------------- --------------------------------
  $A_n$      $\{k+n-\nu\}$                  distinct pivot in $I$      kills one middle character
  $B_n$      $\{n,k+n\}$                    an endpoint outside $I$    copies output to lag
  $0<m<k$    $|I|=m$                        pair separation $k$        all $2m$ relations independent
  $m=0$      empty families                 no pivot needed            rank bound is $\dim H\leq k$
  $m=k$      $\operatorname{span}(I)=k-1$   no pair lies in $I$        rank bound is $\dim H\leq0$

  : The relation/pivot audit. Here $I=[k-\nu,k+m-1-\nu]$. The prose proof uses an outside endpoint of each $B_n$ before using the distinct $A_n$ pivots.
:::

The $A_n$ have distinct pivot coordinates in the integer interval $$I=[k-\nu,k+m-1-\nu].
\label{eq:pivot-interval}$$ When $m>0$, this interval has $m$ entries and span $m-1\leq k-1$; when $m=0$, both relation families are empty. The support pairs $$\{n,k+n\},\qquad 0\leq n<m,
\label{eq:endpoint-pairs}$$ of the $B_n$ are pairwise disjoint. Their low endpoints lie below $m\leq k$, their high endpoints are at least $k$, and distinct values of $n$ give distinct coordinates. Moreover, no pair can lie wholly in $I$: the two endpoints differ by $k$, while the span of $I$ is at most $k-1$.

Consider an integral dependence $$\sum_{n=0}^{m-1}u_nA_n+\sum_{n=0}^{m-1}v_nB_n=0.
\label{eq:integral-dependence}$$ For each $B_n$, choose one endpoint outside $I$. That coordinate occurs in no $A_j$ and, because the pairs are disjoint, in no other $B_j$. Its coefficient in [\[eq:integral-dependence\]](#eq:integral-dependence){reference-type="eqref" reference="eq:integral-dependence"} is $v_n$ or $-v_n$, so $v_n=0$. After every $B_n$ is removed, the distinct pivots force every $u_n=0$. Thus the $2m$ relations are independent over $\mathbb{Z}$, not merely over $\mathbb{Q}$.

The endpoint choice in this argument is simultaneous. Indeed, write $J_n=\{n,k+n\}$. The sets $J_n$ are mutually disjoint, and each $J_n$ meets the consecutive interval $I$ in at most one point. Choose $j_n\in J_n\setminus I$. In the matrix whose rows are $A_0,\ldots,A_{m-1},B_0,\ldots,B_{m-1}$, the column $j_n$ has a single nonzero entry among all $B$ rows and has zero entries among all $A$ rows. Reading the $j_n$ columns of any integral dependence therefore erases the $B$ coefficients one at a time, without division and without a choice of field. What remains is a diagonal collection of unit entries in the distinct $A$-pivot columns. This is the promised integral calculation of all $2m$ relations; tensoring with $\mathbb{Q}$ is unnecessary.

It is also worth spelling out why these are relations in the correct lattice. The embedding $H\hookrightarrow\mathbb{G}_{m}^{k+m}$ induces the surjection $$\varphi:\mathbb{Z}^{k+m}=X^*(\mathbb{G}_{m}^{k+m})\longrightarrow X^*(H)=M.$$ The image of $\varepsilon_i$ is precisely the restricted coordinate character $\chi_i$. Thus [\[eq:two-character-relations\]](#eq:two-character-relations){reference-type="eqref" reference="eq:two-character-relations"} says literally that $\varphi(A_n)=\varphi(B_n)=0$. Since the coordinate characters generate $M$, there is no further unrecorded character-lattice quotient between the ambient calculation and $\dim H$. The kernel has rank at least $2m$, so rank additivity for free abelian groups gives the displayed bound.

The ambient lattice has rank $k+m$. Since $\varphi$ is surjective and its kernel contains these $2m$ independent vectors, $$\operatorname{rank}X^*(H)=\operatorname{rank}\operatorname{im}\varphi
 \leq k+m-2m=k-m.$$ This proves [\[eq:dimension-bound\]](#eq:dimension-bound){reference-type="eqref" reference="eq:dimension-bound"}. At $m=0$ the relation set is empty and the statement is tautological. At $m=k$, the pivot interval has span exactly $k-1$, so the same outside-endpoint proof still applies and forces $H$ to be zero-dimensional.

Notice that the proof establishes a lower bound on the integral kernel rank, not an equality. In the nonroot branch an equation kills both endpoints and can contribute more relations than $A_n$ and $B_n$. Additional coincidences between different equations may also shrink the torus further. The theorem uses only the universally present $2m$-relation subsystem, which is why its upper bound is uniform over all scalar branches. Equality requires a separate construction in Section [5](#sec:equality){reference-type="ref" reference="sec:equality"}; it is not inferred from the rank calculation alone.

## Future characters and the translated residue set

The rank proof already accounts for every ambient coordinate, but the relations also expose which initial characters are killed. From $B_n\in\ker\varphi$ we have $$\chi_{k+n}=\chi_n,
\qquad 0\leq n<m.
\label{eq:future-copy}$$ Thus every future coordinate character is first reduced to an initial coordinate character. If $n<\nu$, the middle coordinate $k+n-\nu$ is already initial. If $n\geq\nu$, it is a future coordinate, and [\[eq:future-copy\]](#eq:future-copy){reference-type="eqref" reference="eq:future-copy"} reduces it to the initial coordinate $n-\nu$. Consequently, [\[eq:middle-trivial\]](#eq:middle-trivial){reference-type="eqref" reference="eq:middle-trivial"} kills exactly the initial residues $$R_m=\{n-\nu\bmod k:0\leq n<m\}.
\label{eq:Rm}$$ Translation modulo $k$ is injective on the interval $0\leq n<m\leq k$, so $R_m$ has exactly $m$ elements. It is a translate of consecutive residues, not the iterated orbit $\{-j\nu\bmod k\}$. Hence no hypothesis, case distinction, or conclusion involving $\gcd(k,\nu)$ occurs.

The distinction can be checked directly at the wrap point. For $0\leq n<\nu$, the killed representative is $k+n-\nu$; these are the last $\nu$ initial positions, beginning at $k-\nu$. For $\nu\leq n<m$, the killed representative is $n-\nu$; these are the first $m-\nu$ positions when that range is nonempty. The two pieces are disjoint and together form the translation of $0,\ldots,m-1$ by $-\nu$. Multiplying the step number by $\nu$ never occurs, so rotation cycles and their gcd are irrelevant.

One may now recover the same dimension bound from initial characters as a consistency check. Equation [\[eq:future-copy\]](#eq:future-copy){reference-type="eqref" reference="eq:future-copy"} shows that the initial characters generate $M$, and [\[eq:Rm\]](#eq:Rm){reference-type="eqref" reference="eq:Rm"} kills $m$ distinct members of that generating list. At most $k-m$ initial generators remain. This argument depends on the future-copy step already proved, whereas the integral pivot proof did not. Their agreement verifies both the lattice rank and the index bookkeeping.

More explicitly, every ambient character is generated by the initial ones after imposing the copy relations: for $i<k$ there is nothing to show, while for $i=k+n$ with $0\leq n<m$, $\chi_i=\chi_n$ by [\[eq:future-copy\]](#eq:future-copy){reference-type="eqref" reference="eq:future-copy"}. The middle relation for step $n$ then kills $\chi_{k+n-\nu}$ directly when $n<\nu$, and kills $\chi_{n-\nu}$ after one such future-to-initial reduction when $n\geq\nu$. No recursive chain of length depending on $n$ is being suppressed. The $m$ killed residues are distinct because their step indices differ by less than $k$. Consequently the surviving list has exactly $k-m$ positions, although some of its characters may coincide or be trivial; those further relations can only decrease the rank. This is the ambient-generation reason that the inequality remains valid in every root/nonroot scalar pattern.

Finally, if $\xi D\subseteq V_m$ for a disconnected algebraic subgroup $D$, each component is a translate of $D^0$ contained in $V_m$. The connected argument applies to every such translate, and [\[eq:component-dimension\]](#eq:component-dimension){reference-type="eqref" reference="eq:component-dimension"} gives $\dim D=\dim D^0\leq k-m$. This completes the proof of Theorem [\[thm:anchored\]](#thm:anchored){reference-type="ref" reference="thm:anchored"}.

# Equality subtori and sharp arithmetic clock {#sec:equality}

The upper bound is attained at every permitted window. The construction also separates geometric sharpness from arithmetic sharpness: first we identify a saturated subtorus, and then we choose coefficients and a finite-rank group for which that subtorus contains infinitely many survivor strings.

[\[prop:equality\]]{#prop:equality label="prop:equality"} Assume $a=1$ and $P(1)=0$. For $0\leq m\leq k$, let $R_m$ be the set in [\[eq:Rm\]](#eq:Rm){reference-type="eqref" reference="eq:Rm"}. Define $H_m\subset\mathbb{G}_{m}^{k+m}$ by $$x_r=1\quad(r\in R_m),
\qquad x_{k+n}=x_n\quad(0\leq n<m),
\label{eq:Hm-definition}$$ leaving the initial coordinates outside $R_m$ free. Then $$H_m\subseteq V_m,\qquad
H_m\simeq\mathbb{G}_{m}^{k-m},\qquad
\dim H_m=k-m.$$ Its relation lattice is saturated, so $H_m$ is connected.

Fix an equation index $0\leq n<m$. If $n<\nu$, then $k+n-\nu$ is the initial representative of the residue $n-\nu$ and belongs to $R_m$. Hence $x_{k+n-\nu}=1$. If $n\geq\nu$, the middle coordinate is future, and [\[eq:Hm-definition\]](#eq:Hm-definition){reference-type="eqref" reference="eq:Hm-definition"} gives $$x_{k+n-\nu}=x_{n-\nu}=1,$$ because $n-\nu\in R_m$. In either case, the $n$th recurrence on $H_m$ becomes $$x_{k+n}=x_n=P(1)+x_n.$$ Thus every defining equation of $V_m$ holds.

This verification also covers the extreme windows. At $m=0$ there are no equations and no fixed residues, so $H_0=\mathbb{G}_{m}^k$. At $m=k$, every initial residue lies in $R_k$, every initial coordinate is fixed to $1$, and all future coordinates copy it; the resulting subgroup is the one point of dimension zero predicted by Theorem [\[thm:anchored\]](#thm:anchored){reference-type="ref" reference="thm:anchored"}. For intermediate $m$, each newly imposed recurrence adds one new fixed initial residue and one copied future coordinate.

Projection to the $k-m$ initial coordinates outside $R_m$ is an explicit inverse to the monomial parametrization of $H_m$. On character lattices, fixed coordinates map to zero, each copied future coordinate maps to its initial basis character, and the free initial coordinates form a basis of the quotient. The quotient is therefore the free lattice $\mathbb{Z}^{k-m}$. Equivalently, the defining relation lattice is a direct summand of the ambient lattice and hence saturated. The associated subgroup is connected and isomorphic to $\mathbb{G}_{m}^{k-m}$.

More concretely, order the free initial indices as $j_1,\ldots,j_{k-m}$. Map the ambient basis vector $\varepsilon_{j_\ell}$ to the $\ell$th basis vector of $\mathbb{Z}^{k-m}$, map a fixed initial coordinate to zero, and map $\varepsilon_{k+n}$ to the image of $\varepsilon_n$. This map is surjective and its kernel is exactly the lattice generated by the relations in [\[eq:Hm-definition\]](#eq:Hm-definition){reference-type="eqref" reference="eq:Hm-definition"}. The inclusion sending the $\ell$th quotient basis vector back to $\varepsilon_{j_\ell}$ splits the quotient. Hence the kernel is a direct summand over $\mathbb{Z}$, which is the promised saturation rather than merely a parametrized-image argument.

The conditions $a=1$ and $P(1)=0$ give a sufficient equality family. We do not assert that they are necessary, nor do we classify all equality cosets or all maximal cosets in $V_m$.

[\[cor:terminal-finite\]]{#cor:terminal-finite label="cor:terminal-finite"} Let the anchored polynomial satisfy [\[eq:anchored-P\]](#eq:anchored-P){reference-type="eqref" reference="eq:anchored-P"}, let the map be defined over an arbitrary characteristic-zero field $K$, and let $\Gamma\leq K^*$ have finite rank with arbitrary torsion. Then $T_k(S,\Gamma)$ is finite. Moreover, $T_m(S,\Gamma)$ is finite for every $m\geq k$.

Theorem [\[thm:anchored\]](#thm:anchored){reference-type="ref" reference="thm:anchored"} at $m=k$ excludes every positive-dimensional torus coset from $V_k$. Lemma [\[lem:field-transfer\]](#lem:field-transfer){reference-type="ref" reference="lem:field-transfer"} makes $V_k\cap\Gamma^{2k}$ finite, and the projection bijection [\[eq:projection\]](#eq:projection){reference-type="eqref" reference="eq:projection"} identifies this intersection with $T_k(S,\Gamma)$. For $m\geq k$, survival through time $m$ implies survival through time $k$, so $T_m(S,\Gamma)\subseteq T_k(S,\Gamma)$.

The conclusion is qualitative. It supplies no effective bound for the number of survivor states and no procedure for listing them.

The order of this deduction is important. Theorem [\[thm:anchored\]](#thm:anchored){reference-type="ref" reference="thm:anchored"} first proves that $V_k$ has no positive-dimensional geometric coset over the algebraic closure. Only then do Lemma [\[lem:field-transfer\]](#lem:field-transfer){reference-type="ref" reference="lem:field-transfer"} and Laurent's theorem enter. No arithmetic finiteness statement is used to justify the geometric rank bound.

[\[prop:sharp-clock\]]{#prop:sharp-clock label="prop:sharp-clock"} For every $k\geq2$, every $1\leq\nu\leq k-1$, and every prescribed actual support size $s\geq2$, there are coefficients over $\mathbb{Q}$ and a rank-one group for which $T_{k-1}$ is infinite.

Choose any distinct positive exponents $e_1<\cdots<e_s$ and set $$a=1,\qquad b_1=\cdots=b_s=1,\qquad c=-s,
\qquad \Gamma=\langle2\rangle.
\label{eq:sharp-coefficients}$$ Then $P(1)=0$. At $m=k-1$, the translated set $R_{k-1}$ contains all initial residues except $$q=k-1-\nu.
\label{eq:free-residue}$$ Put $x_q=t$, set every other initial coordinate equal to $1$, and impose $x_{k+n}=x_n$ for $0\leq n<k-1$. Proposition [\[prop:equality\]](#prop:equality){reference-type="ref" reference="prop:equality"} shows that the resulting scalar string lies in $V_{k-1}$. With $t=2^N$, every coordinate lies in $\Gamma$ and distinct integers $N$ give distinct initial states. Hence $T_{k-1}(S,\Gamma)$ is infinite.

For a coordinate-level check, the active middle coordinate in every one of the first $k-1$ equations has residue in $R_{k-1}$ and is therefore $1$. The polynomial contribution is $P(1)=0$, while $a=1$, so the recurrence reads $x_{k+n}=x_n$ exactly as imposed. The free coordinate $q$ is never an active middle residue during this window, though it may appear as a lag or a copied output; those appearances preserve its value $t$. Hence every entry of the scalar string is either $1$ or $t$, and all belong to $\langle2\rangle$ when $t=2^N$.

Together, Corollary [\[cor:terminal-finite\]](#cor:terminal-finite){reference-type="ref" reference="cor:terminal-finite"} and Proposition [\[prop:sharp-clock\]](#prop:sharp-clock){reference-type="ref" reference="prop:sharp-clock"} give an exact uniform clock: $k$ transitions always suffice under the anchored hypotheses, while $k-1$ transitions need not suffice for compatible coefficients and a compatible rank-one group. This is not a claim that every coefficient choice or every finite-rank group realizes equality.

# Zero-anchor local partition calculus {#sec:local}

We now delete the constant term and fix the planar type $$k=2,\qquad \nu=1,\qquad a\in\Omega^*.$$ Let $$P(X)=\sum_{e\in E}b_eX^e,
\label{eq:zero-P}$$ where $E$ is a nonempty finite set of positive integers, every $b_e$ is nonzero, and equal powers have been collected. Write $V_m^0\subset\mathbb{G}_{m}^{m+2}$ for the variety defined by $$x_{n+2}=P(x_{n+1})+a x_n,
\qquad 0\leq n<m.
\label{eq:zero-recurrence}$$ The first three equations, in the orientation used below, are $$\begin{aligned}
x_2&=P(x_1)+a x_0,\\
x_3&=P(x_2)+a x_1,\\
x_4&=P(x_3)+a x_2.
\end{aligned}
\label{eq:first-three}$$

Let $\xi H\subset V_m^0$ be a connected torus translate. We use additive notation $u_i\in M=X^*(H)$ for the coordinate characters, so $x_i=\xi_i[u_i]$ in the group algebra. Restriction of the $n$th equation gives $$\xi_{n+2}[u_{n+2}]-a\xi_n[u_n]
-\sum_{e\in E}b_e\xi_{n+1}^e[e u_{n+1}]=0.
\label{eq:zero-local-identity}$$

## The trivial-middle split

[\[lem:A-branch\]]{#lem:A-branch label="lem:A-branch"} Suppose $u_{n+1}=0$. If $P(\xi_{n+1})\neq0$, then $u_n=u_{n+2}=0$. If $P(\xi_{n+1})=0$, then $$u_{n+2}=u_n,
\qquad \xi_{n+2}=a\xi_n.
\label{eq:root-copy}$$

When the middle character is trivial, all polynomial terms in [\[eq:zero-local-identity\]](#eq:zero-local-identity){reference-type="eqref" reference="eq:zero-local-identity"} aggregate to $$\xi_{n+2}[u_{n+2}]-a\xi_n[u_n]-P(\xi_{n+1})[0]=0.$$ If the last coefficient is nonzero, the singleton rule forces both endpoints to be trivial, by the same three-character analysis as in [\[eq:aggregated\]](#eq:aggregated){reference-type="eqref" reference="eq:aggregated"}. If it vanishes, the two remaining nonzero terms must have the same character and cancel scalarly, giving [\[eq:root-copy\]](#eq:root-copy){reference-type="eqref" reference="eq:root-copy"}.

To see that no scalar subcase is omitted, call the endpoint characters $v=u_n$ and $w=u_{n+2}$. When $P(\xi_{n+1})\neq0$, the trivial-character block is nonzero. If $v$ and $w$ are distinct, at least one endpoint is a singleton; if $v=w\neq0$, the trivial block is a singleton. The only remaining possibility is $v=w=0$, which is exactly the asserted nonroot conclusion. When $P(\xi_{n+1})=0$, both surviving endpoint coefficients $\xi_{n+2}$ and $-a\xi_n$ are nonzero. Linear independence of distinct characters first gives $v=w$ and then gives $\xi_{n+2}=a\xi_n$. Thus a root can preserve an endpoint character only by copying it; it cannot create a new character or change its integral multiple.

We call the combined trivial-middle relation $$A:\quad u_{n+1}=0,\qquad u_{n+2}=u_n
\label{eq:A-label}$$ the $A$ label. A nonzero endpoint in an $A$ label necessarily belongs to the root-copy branch. The nonroot and root-copy scalar cases remain distinct even though the character shorthand is common.

## Linear support

Suppose $E=\{1\}$ and $P(X)=\beta X$. Choose a root $r\in\Omega$ of $$r^2=\beta r+a.
\label{eq:linear-root}$$ Since $a\neq0$, such a root is nonzero. For every $m\geq0$, direct substitution gives $$L_{r,m}=\{(t,rt,\ldots,r^{m+1}t):t\in\mathbb{G}_{m}\}\subseteq V_m^0,
\label{eq:linear-coset}$$ because $r^{n+2}t=\beta r^{n+1}t+a r^nt$. Thus linear support can retain a one-dimensional coset in every finite window.

The geometry can be arithmetically compatible. Take $$\beta=2,\qquad a=-1,\qquad r=1,\qquad
\Gamma=\langle2\rangle.
\label{eq:linear-compatible}$$ For $t=2^N$, the constant scalar string $(t,\ldots,t)$ belongs to every window, so $T_m$ is infinite for every $m$ for these data. The later nonlinear finiteness statements explicitly exclude this linear class.

## Nonlinear monomial support

Let $E=\{d\}$ with $d\geq2$, so $P(X)=bX^d$ for $b\neq0$. If a middle character is trivial, then $P(\xi_{n+1})=b\xi_{n+1}^d\neq0$ and Lemma [\[lem:A-branch\]](#lem:A-branch){reference-type="ref" reference="lem:A-branch"} kills both endpoint characters. If $u_{n+1}\neq0$, the three terms in [\[eq:zero-local-identity\]](#eq:zero-local-identity){reference-type="eqref" reference="eq:zero-local-identity"} can avoid a singleton only when all three characters agree: $$u_{n+2}=u_n=d u_{n+1}.
\label{eq:monomial-local}$$ For two consecutive equations, a nontrivial first middle character would give $$u_2=u_0=d u_1,
\qquad u_3=u_1=d u_2,$$ and hence $(d^2-1)u_1=0$. Since $M$ is torsion-free and $d\geq2$, we get $u_1=0$, then all four coordinate characters vanish. Ambient generation therefore shows that $V_2^0$ contains no positive-dimensional torus coset.

This two-step closure does not place nonlinear monomials in a no-finite-window class. The preceding one-step window can be infinite for compatible data. With $$P(X)=X^e,\qquad e\geq2,\qquad a=1,\qquad
\Gamma=\langle2\rangle,\qquad t=2^N,
\label{eq:monomial-data}$$ the correctly oriented tuple is $$(x_0,x_1,x_2)=(t^e,t,2t^e),
\label{eq:monomial-tuple}$$ since $P(x_1)+ax_0=t^e+t^e=2t^e$. Distinct integers $N$ give distinct initial pairs $(t^e,t)$, so this is an infinite subset of $T_1$. Interchanging the first two coordinates would not satisfy [\[eq:zero-recurrence\]](#eq:zero-recurrence){reference-type="eqref" reference="eq:zero-recurrence"} in general.

## Supports of size at least three

Assume $|E|\geq3$. If $u_{n+1}\neq0$, the characters $e u_{n+1}$ for $e\in E$ are pairwise distinct. The two endpoints in [\[eq:zero-local-identity\]](#eq:zero-local-identity){reference-type="eqref" reference="eq:zero-local-identity"} can match at most two of them, leaving a nonzero singleton. Hence every local equation forces $u_{n+1}=0$.

In $V_2^0$, the first and second equations give $u_1=u_2=0$. If the first equation is in its nonroot branch, it already kills $u_0$ and $u_2$. If it is a root-copy, then $u_2=u_0$, and the second equation forces $u_2=0$, hence $u_0=0$. Applying the same split to the second equation also gives $u_3=0$. All ambient characters vanish, so no positive-dimensional coset lies in $V_2^0$. This explicitly closes every scalar root-copy branch rather than assuming generic middle scalars.

The order of this closure is important. The first equation alone permits $u_0=u_2\neq0$ when its middle scalar is a root of $P$. The second equation does not merely supply another copy relation: because its middle character is $u_2$, the distinct-power singleton argument first forces $u_2=0$. Only after that conclusion do we return to the first copy and obtain $u_0=0$. With $u_2=0$, Lemma [\[lem:A-branch\]](#lem:A-branch){reference-type="ref" reference="lem:A-branch"} applied to the second equation gives either the nonroot conclusion $u_1=u_3=0$ or the root copy $u_3=u_1=0$. Hence both choices of middle scalar in both equations are accounted for, including the root--root combination.

Every prescribed actual support size $s\geq2$ nevertheless has a compatible infinite one-step family. Write $E=\{e_1<\cdots<e_s\}$ and choose $$b_{e_1}=\cdots=b_{e_{s-1}}=1,\qquad b_{e_s}=-(s-1),
\qquad a=1.
\label{eq:multisupport-coefficients}$$ All coefficients are nonzero in characteristic zero and $P(1)=0$. With $\Gamma=\langle2\rangle$ and $t=2^N$, the tuple $$(x_0,x_1,x_2)=(t,1,t)
\label{eq:multisupport-tuple}$$ satisfies the first recurrence. This family is separate from the two-step resonance classified below.

## Binomial support and the exhaustive local labels

Let $$E=\{p,q\},\qquad 1\leq p<q,
\qquad P(X)=b_pX^p+b_qX^q.
\label{eq:binomial-P}$$ For one local equation put $u=u_{n+1}$. If $u=0$, Lemma [\[lem:A-branch\]](#lem:A-branch){reference-type="ref" reference="lem:A-branch"} gives label $A$ and its exact scalar split. Suppose $u\neq0$. The middle characters $pu$ and $qu$ are distinct. A partition of the four terms in [\[eq:zero-local-identity\]](#eq:zero-local-identity){reference-type="eqref" reference="eq:zero-local-identity"} with no singleton must pair each endpoint with one of the two power characters. Pairing the two endpoints together would leave both distinct powers as singletons, so it cannot produce another case. There are exactly two endpoint-to-power orientations, called $B$ and $C$ in Table [2](#tab:ABC){reference-type="ref" reference="tab:ABC"}.

::: {#tab:ABC}
   Label  Character relations          Scalar equations
  ------- ---------------------------- -------------------------------------------------------------------------------------
    $A$   $u_{n+1}=0$, $u_{n+2}=u_n$   If $P(\xi_{n+1})=0$, then $\xi_{n+2}=a\xi_n$; otherwise both endpoints are trivial.
    $B$   $u_n=pu$, $u_{n+2}=qu$       $a\xi_n=-b_p\xi_{n+1}^{p}$, $\xi_{n+2}=b_q\xi_{n+1}^{q}$
    $C$   $u_n=qu$, $u_{n+2}=pu$       $a\xi_n=-b_q\xi_{n+1}^{q}$, $\xi_{n+2}=b_p\xi_{n+1}^{p}$

  : The exhaustive local $A/B/C$ labels. The two nontrivial rows are the two possible endpoint-to-power pairings, with scalar signs inherited from [\[eq:zero-local-identity\]](#eq:zero-local-identity){reference-type="eqref" reference="eq:zero-local-identity"}.
:::

For completeness, the scalar signs in the table follow by collecting coefficients within each equal-character block. In label $B$, the lag term pairs with the $p$th power, so $-a\xi_n-b_p\xi_{n+1}^p=0$, while the output pairs with the $q$th power, so $\xi_{n+2}-b_q\xi_{n+1}^q=0$. Label $C$ reverses the two powers and gives the other two displayed equations. Thus Table [2](#tab:ABC){reference-type="ref" reference="tab:ABC"} records every local possibility and fixes the orientation used in the adjacent-word calculation.

# Exact zero-constant phase and third-step closure {#sec:phase}

We now compose the local labels. The calculation both locates the only nonlinear two-step resonance and proves that no nonlinear support retains a positive-dimensional coset through a third transition.

[\[thm:zero-phase\]]{#thm:zero-phase label="thm:zero-phase"} Assume the planar zero-constant setup [\[eq:zero-P\]](#eq:zero-P){reference-type="eqref" reference="eq:zero-P"}--[\[eq:zero-recurrence\]](#eq:zero-recurrence){reference-type="eqref" reference="eq:zero-recurrence"}.

1.  If $E=\{1\}$ and $P(X)=\beta X$, then the one-dimensional coset $L_{r,m}$ in [\[eq:linear-coset\]](#eq:linear-coset){reference-type="eqref" reference="eq:linear-coset"} lies in $V_m^0$ for every $m\geq0$ and every nonzero root $r$ of $r^2=\beta r+a$.

2.  If $E=\{d\}$ with $d\geq2$, if $E=\{p,q\}$ with $2\leq p<q$, or if $|E|\geq3$, then $V_2^0$ contains no positive-dimensional connected torus coset.

3.  Suppose $E=\{1,d\}$, $d\geq2$, and $P(X)=\beta X+\delta X^d$. The variety $V_2^0$ contains a positive-dimensional connected torus coset if and only if $$a=-\beta^2.
    \label{eq:resonance}$$ On this locus the unique such coset is $$C_d=\left\{\left(
    \frac{\delta}{\beta^2}t^d,\ t,\ \beta t,\
    \delta\beta^dt^d\right):t\in\mathbb{G}_{m}\right\}.
    \label{eq:Cd}$$ For every coefficient choice in every nonlinear support, including the locus [\[eq:resonance\]](#eq:resonance){reference-type="eqref" reference="eq:resonance"}, $V_3^0$ contains no positive-dimensional torus coset.

Parts (a) and the monomial and large-support cases of part (b) were proved in Section [6](#sec:local){reference-type="ref" reference="sec:local"}. It remains to compose the exhaustive binomial labels and then close the unique surviving word.

## All adjacent words

First consider a word containing $A$. For $AA$, the first label gives $u_1=0$ and $u_2=u_0$, while the second gives $u_2=0$ and $u_3=u_1$; all four characters vanish. For $AB$ or $AC$, the first label gives $u_1=0$, whereas the second nontrivial label requires its lag $u_1$ to be a positive multiple of its nonzero middle $u_2$, a contradiction. For $BA$ or $CA$, the first label has nonzero output $u_2$, whereas the second label requires its middle $u_2$ to vanish. These five words therefore carry no nonzero character solution, including when the first $A$ arose from a scalar root-copy.

This five-word elimination already includes the scalar branches of $A$. In $AA$, if the first $A$ is a root-copy, the second label's condition $u_2=0$ kills the copied character $u_0$; if it is a nonroot, that character was already zero. The second $A$ similarly makes $u_3=0$ whether its middle scalar is a root or not. In $AB$ and $AC$, the second label is defined only with $u_2\neq0$, and its lag relation is respectively $u_1=p u_2$ or $u_1=q u_2$; torsion-freeness contradicts $u_1=0$. In $BA$ and $CA$, the first output is respectively $q u_1$ or $p u_1$, hence nonzero, while the second $A$ requires that same character $u_2$ to be zero. No choice among the scalar equations in Table [2](#tab:ABC){reference-type="ref" reference="tab:ABC"} can overcome a character contradiction.

For two nontrivial labels, assume $u_1\neq0$ and compare the output relation of the first label with the lag relation of the second. The four possibilities are $$\begin{aligned}
BB:&\quad u_1=p u_2=pq\,u_1,
\label{eq:BB}\\
BC:&\quad u_1=q u_2=q^2u_1,
\label{eq:BC}\\
CB:&\quad u_1=p u_2=p^2u_1,
\label{eq:CB}\\
CC:&\quad u_1=q u_2=pq\,u_1.
\label{eq:CC}\end{aligned}$$ Torsion-freeness of $M$ turns these into integer equalities. Because $1\leq p<q$, the requirements $pq=1$ and $q^2=1$ are impossible. The word $CB$ can survive only when $p^2=1$, hence only when $p=1$. Table [3](#tab:words){reference-type="ref" reference="tab:words"} records these nine words and, in the surviving row, the complete third-step closure that will be proved below.

For reference, the four displayed equations come directly from the two oriented rows of Table [2](#tab:ABC){reference-type="ref" reference="tab:ABC"}. At the first position, $B$ means $$(u_0,u_2)=(p u_1,q u_1),$$ whereas $C$ means $(u_0,u_2)=(q u_1,p u_1)$. At the second position, $B$ means $(u_1,u_3)=(p u_2,q u_2)$, whereas $C$ means $(u_1,u_3)=(q u_2,p u_2)$. Substitution gives $pq$, $q^2$, $p^2$, and $pq$ in the order $BB,BC,CB,CC$. Since $u_1\neq0$ in a nontrivial label, an equality $N u_1=u_1$ forces $N=1$ in the torsion-free lattice $M$. Thus scalar cancellation is consulted only for $CB$ with $p=1$; the other eight words have already failed the complete character partition.

::: {#tab:words}
  Word   Character condition                                      Outcome and possible continuation
  ------ -------------------------------------------------------- --------------------------------------------------------------------------------------------------------
  $AA$   $u_1=u_2=0$, $u_2=u_0$, $u_3=u_1$                        all four characters vanish
  $AB$   $u_1=0$ but $u_1$ is a positive multiple of $u_2\neq0$   contradiction
  $AC$   $u_1=0$ but $u_1$ is a positive multiple of $u_2\neq0$   contradiction
  $BA$   first output has $u_2\neq0$, second middle has $u_2=0$   contradiction
  $CA$   first output has $u_2\neq0$, second middle has $u_2=0$   contradiction
  $BB$   $u_1=pq\,u_1$                                            requires $pq=1$, impossible
  $BC$   $u_1=q^2u_1$                                             requires $q^2=1$, impossible
  $CB$   $u_1=p^2u_1$                                             only $p=1$; then third $A$ is impossible, third $B$ gives $(d-1)u=0$, and third $C$ gives $(d^2-1)u=0$
  $CC$   $u_1=pq\,u_1$                                            requires $pq=1$, impossible

  : The adjacent-word and third-step closure matrix. All nine two-label words occur; only $CB$ with $p=1$ reaches the third-equation test.
:::

The word calculation proves part (b) for every binomial whose lower exponent is at least two. It also proves that a positive-dimensional binomial coset in $V_2^0$ must have support $\{1,d\}$ and local word $CB$.

## Scalar compatibility and the resonant coset

Put $p=1$, $q=d\geq2$, and write $$P(X)=\beta X+\delta X^d.
\label{eq:resonant-P}$$ For the surviving word, let $u=u_1\neq0$. The first $C$ relation and the second $B$ relation force the character vector $$(u_0,u_1,u_2,u_3)=(du,u,u,du).
\label{eq:CB-vector}$$ The scalar equations from the first, $C$-labelled recurrence are $$a\xi_0=-\delta\xi_1^d,
\qquad \xi_2=\beta\xi_1.
\label{eq:first-C-scalars}$$ Those from the second, $B$-labelled recurrence are $$a\xi_1=-\beta\xi_2,
\qquad \xi_3=\delta\xi_2^d.
\label{eq:second-B-scalars}$$ These four equations can also be recovered directly from the group-algebra blocks, which checks both signs and orientation. In the first recurrence, the $C$ character relation pairs the lag character $u_0=d u_1$ with the degree-$d$ middle character. Their two coefficients are $-a\xi_0$ and $-\delta\xi_1^d$, so their sum is zero precisely when the first equation of [\[eq:first-C-scalars\]](#eq:first-C-scalars){reference-type="eqref" reference="eq:first-C-scalars"} holds. The same $C$ relation pairs the output character $u_2=u_1$ with the linear middle character; their coefficients $\xi_2$ and $-\beta\xi_1$ give the second equation. For the next recurrence, label $B$ pairs the lag $u_1=u_2$ with the linear middle character. The coefficient block $-a\xi_1-\beta\xi_2$ gives the first equation of [\[eq:second-B-scalars\]](#eq:second-B-scalars){reference-type="eqref" reference="eq:second-B-scalars"}. Its output character $u_3=d u_2$ pairs with the nonlinear middle character, giving $\xi_3-\delta\xi_2^d=0$. Every coefficient divided out below is nonzero: $a,\beta,\delta$ are actual coefficients and each $\xi_i$ is a torus coordinate.

This block computation also explains why the character screen precedes the scalar screen. For eight of the nine words a nonzero character would be a singleton or would satisfy an impossible integral multiple relation, so no scalar equality can make that word valid. For the sole surviving word, the four blocks above are all the blocks in the two restricted equations. Their compatibility is therefore necessary, while direct substitution in the recurrence proves sufficiency. Substitution of $\xi_2=\beta\xi_1$ into the first equation of [\[eq:second-B-scalars\]](#eq:second-B-scalars){reference-type="eqref" reference="eq:second-B-scalars"}, with $\xi_1\neq0$, yields exactly $a=-\beta^2$. On this locus, the remaining scalars are forced: $$\xi_0=\frac{\delta}{\beta^2}\xi_1^d,
\qquad \xi_2=\beta\xi_1,
\qquad \xi_3=\delta\beta^d\xi_1^d.
\label{eq:forced-scalars}$$ Thus every positive-dimensional connected coset in $V_2^0$ is contained in $C_d$.

Conversely, $C_d$ satisfies both recurrence equations directly. For its first equation, $$\beta t+\delta t^d-\beta^2
  \left(\frac{\delta}{\beta^2}t^d\right)=\beta t.$$ For its second equation, $$\beta(\beta t)+\delta(\beta t)^d-\beta^2t
=\delta\beta^dt^d.$$ Hence $C_d\subseteq V_2^0$ when [\[eq:resonance\]](#eq:resonance){reference-type="eqref" reference="eq:resonance"} holds.

It remains to justify uniqueness as a geometric subset, rather than only uniqueness of the displayed equations. Vector [\[eq:CB-vector\]](#eq:CB-vector){reference-type="eqref" reference="eq:CB-vector"} shows that every ambient coordinate character lies in the cyclic subgroup generated by $u=u_1$. Conversely, $u$ is itself an ambient coordinate character. Since ambient characters generate $X^*(H)$, a positive-dimensional $H$ has a cyclic character lattice and therefore dimension one. A nonzero character on a one-dimensional torus is surjective over the algebraically closed field $\Omega$. The coordinate $x_1=\xi_1u$ consequently ranges through all of $\mathbb{G}_{m}$, and formulas [\[eq:forced-scalars\]](#eq:forced-scalars){reference-type="eqref" reference="eq:forced-scalars"} make the coset equal to all of $C_d$. Off [\[eq:resonance\]](#eq:resonance){reference-type="eqref" reference="eq:resonance"}, the sole possible nonzero word fails its scalar compatibility. This proves the two-step claims and uniqueness in part (c).

## The third equation closes every nonlinear support

On the resonant word $CB$, the first four characters are $(du,u,u,du)$ with $u\neq0$. A third local label uses middle character $u_3=du$ and lag character $u_2=u$. Label $A$ is impossible because it requires its middle character to vanish. Label $B$ requires the lag to equal the first power of the middle, so $u=du$ and $(d-1)u=0$. Label $C$ requires the lag to equal $d$ times the middle, so $u=d^2u$ and $(d^2-1)u=0$. Torsion-freeness and $d\geq2$ rule out all three possibilities, exactly as recorded in Table [3](#tab:words){reference-type="ref" reference="tab:words"}.

This third equation also accounts for the fifth ambient character $u_4$. If it had a valid local partition, Table [2](#tab:ABC){reference-type="ref" reference="tab:ABC"} would assign that partition one of $A,B,C$. The contradiction for $A$ uses the known middle $u_3=du\neq0$; the contradictions for $B$ and $C$ use the known lag $u_2=u$ before any value of the output $u_4$ is chosen. Thus no fifth character can complete the resonant four-character vector to a character solution of the third restricted equation. This is stronger than checking that the displayed scalar parametrization fails one selected continuation: the local partition list is exhaustive.

For every other nonlinear support, the first two equations already force $u_0,u_1,u_2,u_3$ to vanish. In the third recurrence the lag and middle characters are then trivial. If the output character $u_4$ were nontrivial, its output term would be a nonzero singleton in the group algebra. Hence $u_4=0$ as well. Ambient generation excludes a positive-dimensional coset in $V_3^0$. The same observation handles the all-trivial first-four-character branch on the resonant support. This completes the proof of Theorem [\[thm:zero-phase\]](#thm:zero-phase){reference-type="ref" reference="thm:zero-phase"}.

Indeed, after $u_2=u_3=0$, every polynomial term in the third equation has trivial character, as does the lag term. Their scalar coefficients may aggregate to zero or not, but the output coefficient $\xi_4$ is nonzero because the coset lies in the ambient torus. Therefore a nontrivial $u_4$ would occur in a block by itself. The singleton lemma forces $u_4=0$ without a genericity assumption on $\xi_3$. Since $u_0,\ldots,u_4$ are the images of all standard ambient characters for $V_3^0\subset\mathbb{G}_{m}^5$, their simultaneous vanishing makes $X^*(H)$ trivial.

## Arithmetic phase and sharp examples

[\[cor:zero-arithmetic\]]{#cor:zero-arithmetic label="cor:zero-arithmetic"} Let the planar zero-constant map be defined over a characteristic-zero field $K$, and let $\Gamma\leq K^*$ have finite rank with arbitrary torsion.

1.  For every nonlinear support other than a resonant $\{1,d\}$ support, $T_2(S,\Gamma)$ is finite.

2.  On the resonant $\{1,d\}$ locus, $T_3(S,\Gamma)$ is finite.

Apply Lemma [\[lem:field-transfer\]](#lem:field-transfer){reference-type="ref" reference="lem:field-transfer"} to the no-positive-dimensional-coset conclusions for $V_2^0$ and $V_3^0$ in Theorem [\[thm:zero-phase\]](#thm:zero-phase){reference-type="ref" reference="thm:zero-phase"}, and then use the projection bijection [\[eq:projection\]](#eq:projection){reference-type="eqref" reference="eq:projection"} with $k=2$.

Linear support is excluded from Corollary [\[cor:zero-arithmetic\]](#cor:zero-arithmetic){reference-type="ref" reference="cor:zero-arithmetic"}; the compatible family [\[eq:linear-compatible\]](#eq:linear-compatible){reference-type="eqref" reference="eq:linear-compatible"} can make every $T_m$ infinite. On the nonlinear resonance, existence of $C_d$ is geometric and does not imply that $T_2(S,\Gamma)$ is infinite for every fixed $\Gamma$. Arithmetic compatibility must be checked separately. For example, take $$\beta=\delta=1,\qquad a=-1,\qquad \Gamma=\langle2\rangle.
\label{eq:resonant-data}$$ For $t=2^N$, the strings $$(x_0,x_1,x_2,x_3)=(t^d,t,t,t^d)
\label{eq:resonant-tuple}$$ lie in $C_d\cap\Gamma^4$ and give infinitely many points of $T_2$. This example proves sharpness for the specified group, not a universal intersection claim.

# Assumption boundaries, contextual separation, and conclusion {#sec:boundaries}

The two theorems form an exact phase only within their stated assumptions. We collect those boundaries here so that arithmetic corollaries and neighboring dynamical questions are not conflated with the proved geometry.

## Assumption audit

Characteristic zero enters the arithmetic conclusion through the finitely generated field embedding used in Lemma [\[lem:field-transfer\]](#lem:field-transfer){reference-type="ref" reference="lem:field-transfer"}. We make no theorem in positive characteristic. The condition $a\neq0$ makes [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"} an automorphism and preserves two nonzero endpoint terms; the case $a=0$ is outside both classifications. The support is a finite collected set of positive polynomial exponents. Negative Laurent exponents, rational maps with poles, and arbitrary polynomial automorphisms require different geometric arguments and are not covered.

Actual collected support refers to the displayed coordinate expression after equal powers are combined. We do not assert that this support is invariant under affine conjugacy. The anchored bound is stated only for $0\leq m\leq k$. Finiteness at later windows follows from the inclusion $T_m\subseteq T_k$, not from extending the expression $k-m$ to a negative dimension. The equality subtori prove attainment but do not classify all equality cosets, all maximal cosets, or all coefficient loci on which equality can occur.

The arithmetic conclusions remain qualitative. Laurent's theorem supplies no effective cardinality, exceptional-locus algorithm, height estimate, or enumeration for these survivor sets. We also derive no periodic-point classification. The bounded comparison with existing work is not a global or exhaustive claim, does not establish a first-result assertion, and says nothing about unpublished work.

## Nearby questions and the predecessor boundary

The present finite-window problem varies the initial state and requires all coordinates in a whole recurrence segment to lie in a multiplicative group. This differs from asking when one fixed orbit meets a subgroup, as in the semiabelian setting studied by Bell and Ghioca [@BellGhioca2024]. It also differs from cyclotomic rigidity questions for affine dynamics [@JiXieZhang2026] and from multiplicative dependence or integrality along semigroup orbits [@MelloYasufuku2026]. Linear multiple-reachability problems can also use torus-subvariety methods [@KarimovKelmendiOuaknineWorrell2024], but their systems, targets, and algorithmic questions are distinct from the nonlinear recurrence geometry here. These sources provide context only; none is a proof dependency for the dimension law, equality family, local partition calculus, resonance, or third-step closure.

An earlier companion treatment established stronger explicit bounds for the planar nonzero-constant problem and subsumed its own support-one precursor. The present article neither reproduces nor improves those planar estimates; its contribution is the all-dimensional torus-coset decay profile and the exact zero-constant boundary.

The comparison removes the planar anchored specialization from the claimed contribution. In particular, the present results do not improve any explicit cardinality estimate for that specialization, and the earlier treatment is neither imported as a black box nor included in the bibliography.

## Conclusion

A nonzero constant term fixes a trivial character in every restricted recurrence. With two actual nonconstant powers, that character forces the middle coordinate to be trivial and leaves an endpoint-copy relation. Across $m$ equations, the middle pivots and disjoint endpoint pairs form $2m$ independent integral relations, producing the sharp deficit $\dim H\leq k-m$. Saturated equality subtori show that every step of this deficit is real, and the qualitative torus-intersection theorem converts the terminal geometric statement into finite-rank arithmetic finiteness.

Deleting the constant removes exactly the term responsible for the singleton deficit. In the plane, the remaining four-term identity has two nontrivial endpoint-to-power orientations. Their complete transition calculus leaves only the $C$-then-$B$ word on support $\{1,d\}$, and its scalar equations force $a=-\beta^2$ and the coset $C_d$. A third equation admits no continuation. The anchored law and the zero-anchor phase are therefore two sides of one character-deficit mechanism, with the proved conclusions ending at qualitative finiteness and the exact stated assumptions.
