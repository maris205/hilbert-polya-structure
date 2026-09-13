---
p1_kind: "derived-fulltext-reading-copy"
route: "symplectic_map"
logical_paper_id: "symplectic_map--16-henon-support-size-torus-escape"
canonical_tex: "symplectic_map/papers/16-henon-support-size-torus-escape/paper/main.tex"
canonical_pdf: "symplectic_map/papers/16-henon-support-size-torus-escape/paper/main.pdf"
source_sha256: "2bd2dc0f3ddc2d9e75b48aef06b71bede5ecc5840ab1af7b0363a5c6c3f821d9"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Support Size and Finite-Rank Torus Escape for Generalized Hénon Maps

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symplectic_map/papers/16-henon-support-size-torus-escape>)
- [规范 TeX](<../../../../../symplectic_map/papers/16-henon-support-size-torus-escape/paper/main.tex>)
- [关联 PDF](<../../../../../symplectic_map/papers/16-henon-support-size-torus-escape/paper/main.pdf>)
- [支撑 Markdown](<../../../../../symplectic_map/papers/16-henon-support-size-torus-escape/notes/CLAIMS_EVIDENCE_MATRIX.md>)
- [BibTeX](<../../../../../symplectic_map/papers/16-henon-support-size-torus-escape/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We study consecutive visits of generalized Hénon orbits to the square of a finite-rank multiplicative subgroup. Let $K$ have characteristic zero, let $\Gamma\leq K^*$ have rank $r$, and consider $H(x,y)=(P(x)+ay,x)$, where $P(X)=c+\sum_{j=1}^{s}b_jX^{e_j}$ has collected nonconstant support $1\leq e_1<\cdots<e_s=d$ and all displayed coefficients are nonzero. For $s\geq2$, we prove the coefficient-uniform two-transition estimate $$\#T_2(H,\Gamma)\leq d\mathcal A(s+2,3r)+\mathcal M(\mathbf e)\mathcal S_*,$$ with every constant explicit. The obstacle is a vanishing proper subsum in the first local unit equation. We resolve it by an exhaustive four-type incidence ledger: two types are sparse polynomial graphs, while two fix the first coordinate on controlled root sets and are closed by the second recurrence. A quantitative sparse-image lemma treats arbitrary torsion and the possible cancellation of the vertical constant term. Together, the graph and root arguments convert every coefficient specialization into finitely many degree-controlled pieces. The window is sharp: every prescribed support with $s\geq2$ admits a rational rank-one family with infinite $T_1$. In contrast, support one has a longer exceptional cancellation chain; we give a complete internal proof that $T_4$ is uniformly finite, with bound $4d\mathcal A(3,3r)+81d^2$, whereas $T_3$ can be infinite in rank one.
author:
- Anonymous
bibliography:
- references.bib
title: 'Support Size and Finite-Rank Torus Escape for Generalized Hénon Maps'
```

## Markdown 正文

# Introduction and main results {#sec:introduction}

Let $K$ be a field of characteristic zero and let $\Gamma\leq K^*$ be a multiplicative subgroup of finite rank $r$. We do not assume that $\Gamma$ is finitely generated, and its torsion subgroup may be infinite. Consider the generalized Hénon automorphism $$H(x,y)=\bigl(P(x)+ay,x\bigr),
 \qquad
 P(X)=c+\sum_{j=1}^{s}b_jX^{e_j},
 \label{eq:map}$$ where $$1\leq e_1<\cdots<e_s=d,
 \qquad
 a,c,b_1,\ldots,b_s\in K^*.
 \label{eq:support}$$ The exponents in [\[eq:support\]](#eq:support){reference-type="eqref" reference="eq:support"} describe the actual nonconstant support: equal powers have first been combined and zero coefficients deleted. The constant $c$ is separate from that support. For $m\geq0$, define $$T_m(H,\Gamma)=
 \{Q\in\Gamma^2:H^j(Q)\in\Gamma^2\text{ for }0\leq j\leq m\}.
 \label{eq:survivor}$$ Thus $T_m$ records $m$ transitions and $m+1$ consecutive states. Our question is how short a window forces the set of all surviving initial states to be finite, uniformly in the nonzero coefficients.

Put $$\mathcal A(q,R)=(8q)^{4q^4(q+R+1)}
 \qquad(q\geq2,\ R\geq0),
 \label{eq:A}$$ and, for $2\leq q\leq s+1$, put $$\mathcal S_q(d,r)=d\bigl(\mathcal A(q,2r)+2^q-q-2\bigr),
 \qquad
 \mathcal S_*=\max_{2\leq q\leq s+1}\mathcal S_q(d,r).
 \label{eq:S}$$ For a nonempty $J\subseteq[s]=\{1,\ldots,s\}$, write $e_{\max J}=\max_{j\in J}e_j$ and $e_{\min J}=\min_{j\in J}e_j$. Define $$\boxed{
 \begin{aligned}
 \mathcal M(\mathbf e)={}&2(2^s-1)\\
 &+\sum_{\substack{J\subseteq[s]\\ |J|\geq2}}
       (e_{\max J}-e_{\min J})
 +\sum_{\varnothing\neq J\subseteq[s]}e_{\max J}.
 \end{aligned}}
 \label{eq:M-definition}$$ The subset-sum expression, rather than either checksum derived later, is the definition.

[\[thm:pc1\]]{#thm:pc1 label="thm:pc1"} Assume [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"}--[\[eq:support\]](#eq:support){reference-type="eqref" reference="eq:support"} with $s\geq2$. Then $$\boxed{
 \#T_2(H,\Gamma)
 \leq d\mathcal A(s+2,3r)+\mathcal M(\mathbf e)\mathcal S_*.
 }
 \label{eq:pc1-bound}$$ The bound is uniform in all nonzero coefficients, none of which is required to belong to $\Gamma$.

The first term in [\[eq:pc1-bound\]](#eq:pc1-bound){reference-type="eqref" reference="eq:pc1-bound"} is the nondegenerate unit-equation contribution. The second accounts for every possible vanishing proper subsum. The proof records four exhaustive membership types, handles their endpoint subsets, and closes the root types using the next recurrence. This explicit local mechanism is the principal result.

[\[prop:pc2\]]{#prop:pc2 label="prop:pc2"} For every $1\leq e_1<\cdots<e_s$ with $s\geq2$, there are rational nonzero coefficients and a rank-one subgroup $\Gamma\leq\mathbb Q^*$ for which $T_1(H,\Gamma)$ is infinite.

Support one is different, rather than an omitted endpoint of Theorem [\[thm:pc1\]](#thm:pc1){reference-type="ref" reference="thm:pc1"}.

[\[thm:pc3\]]{#thm:pc3 label="thm:pc3"} Let $P(X)=c+bX^d$, where $d\geq2$ and $a,b,c\in K^*$. Then $$\boxed{
 \#T_4(H,\Gamma)
 \leq4d\mathcal A(3,3r)+81d^2.
 }
 \label{eq:pc3-bound}$$ For every $d\geq2$, there is a number field, a rank-one multiplicative subgroup, and nonzero coefficients for which $T_3(H,\Gamma)$ is infinite.

Together these statements give an exact transition-depth dichotomy. Actual support one has a coefficient-uniform finite window at $T_4$, and $T_3$ may be infinite. Actual support at least two has a coefficient-uniform finite window at $T_2$, and $T_1$ may be infinite. The assertions concern the normal form [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"}; they do not turn numerical support into a conjugacy invariant.

## Why the window is the invariant being counted

The condition in [\[eq:survivor\]](#eq:survivor){reference-type="eqref" reference="eq:survivor"} is coordinatewise and consecutive. It is stronger than asking that one coordinate of one iterate be multiplicatively special, but it is weaker than requiring an entire infinite orbit to stay in the torus. The initial state is not fixed. We count every $Q\in\Gamma^2$ whose first $m$ transitions survive, and the bound must hold uniformly over all nonzero coefficient choices. Those three features distinguish the problem: all initial states are allowed, the time interval is short, and the coefficient dependence is suppressed from the final cardinality.

The Hénon form converts these geometric conditions into a scalar recurrence with memory one. A point $Q=(x_0,x_{-1})$ gives $$x_{i+1}=P(x_i)+ax_{i-1},
 \qquad H^i(Q)=(x_i,x_{i-1}).$$ Thus $T_2$ is governed by two linked equations in four group elements. Either equation separately may have a positive-dimensional family arising from cancellation. The useful fact is that the free variable of a root-type cancellation in the first equation becomes the input of a sparse polynomial in the second. Actual support at least two makes that second polynomial remain sparse even after its constant term vanishes.

The uniformity in Theorem [\[thm:pc1\]](#thm:pc1){reference-type="ref" reference="thm:pc1"} is deliberately strong in coefficients and deliberately narrow in form. The coefficients may satisfy arbitrary algebraic relations, may lie outside $\Gamma$, and may cause several proper subsums to vanish at once. None of those phenomena is excluded by a genericity hypothesis. On the other hand, the polynomial must already be collected, every displayed coefficient must be nonzero, and the map must be in the displayed generalized Hénon normal form. The examples in Section [6](#sec:sharpness){reference-type="ref" reference="sec:sharpness"} show why the two nonzero structural coefficients cannot be discarded.

The three results have different logical roles. Theorem [\[thm:pc1\]](#thm:pc1){reference-type="ref" reference="thm:pc1"} is the dominant finiteness theorem. Proposition [\[prop:pc2\]](#prop:pc2){reference-type="ref" reference="prop:pc2"} proves that its two-transition depth cannot be shortened, for every support rather than for one convenient support. Theorem [\[thm:pc3\]](#thm:pc3){reference-type="ref" reference="thm:pc3"} supplies the complete support-one comparison and shows that support one cannot be folded into the same proof with a weaker estimate. In particular, the support-one obstruction is a realized cancellation chain, not merely a failure of our counting method.

## Anatomy of the explicit bound

The first term in [\[eq:pc1-bound\]](#eq:pc1-bound){reference-type="eqref" reference="eq:pc1-bound"} comes from one $(s+2)$-term nondegenerate unit equation in a rank-$3r$ tuple group, followed by a degree-$d$ power fiber. The factor $\mathcal S_*$ in the second term is a worst-case sparse-image budget. It combines a rank-$2r$ nondegenerate count, the exact number $2^q-q-2$ of possible proper degenerate subsets of size at least two, and one degree-$d$ fiber.

The multiplier $\mathcal M(\mathbf e)$ is more geometric. Its first summand counts the two graph-label families. Its first subset sum counts nonzero roots of monomial subsums after the lowest power is factored. Its second subset sum counts roots of a constant-plus-monomials equation. Retaining these contributions as separate subset sums makes the proof auditable: each quantity corresponds to one family in Table [1](#tab:four-types){reference-type="ref" reference="tab:four-types"}. The closed formula [\[eq:M-closed\]](#eq:M-closed){reference-type="eqref" reference="eq:M-closed"} is useful for checking arithmetic, but it hides that geometry and is therefore not used as the definition.

Nothing in the theorem says that every bound is attained. The estimates intentionally use unions, maximum sparse budgets, and algebraic-closure root counts. Their function is to prove a coefficient-independent finite ceiling while preserving the exact transition depth.

Section [2](#sec:context){reference-type="ref" reference="sec:context"} gives arithmetic context. Section [3](#sec:setup){reference-type="ref" reference="sec:setup"} fixes the rank and field bridge. Section [4](#sec:sparse){reference-type="ref" reference="sec:sparse"} proves the sparse-image lemma. Section [5](#sec:pc1proof){reference-type="ref" reference="sec:pc1proof"} proves Theorem [\[thm:pc1\]](#thm:pc1){reference-type="ref" reference="thm:pc1"}. Section [6](#sec:sharpness){reference-type="ref" reference="sec:sharpness"} proves Proposition [\[prop:pc2\]](#prop:pc2){reference-type="ref" reference="prop:pc2"} and audits essential hypotheses. Section [7](#sec:supportone){reference-type="ref" reference="sec:supportone"} proves Theorem [\[thm:pc3\]](#thm:pc3){reference-type="ref" reference="thm:pc3"}. The appendices repeat calculations as audits; no main implication depends on them.

# Arithmetic-dynamical context {#sec:context}

The proof belongs to the quantitative theory of linear equations in multiplicative groups, but the statement is organized by a dynamical window. A local Hénon recurrence produces a linear equation whose variable tuple lies in a homomorphic image of $\Gamma^3$. A nondegenerate solution is controlled uniformly. The essential work begins when a proper subsum vanishes: a local unit equation alone does not say that the full solution set is finite. Support converts every degenerate branch either into a sparse graph or into a finite root set followed by a sparse graph.

The sole external theorem used in a proof is Amoroso and Viada's explicit nondegenerate unit-equation estimate, Theorem 6.2 of [@amorosoViada2009]. Its constant is exactly $\mathcal A(q,R)$ from [\[eq:A\]](#eq:A){reference-type="eqref" reference="eq:A"}. The earlier theorem of Evertse, Schlickewei, and Schmidt gives a foundational uniform bound for nondegenerate linear equations in finite-rank multiplicative groups [@ess2002 Theorem 1.1]. We cite it only for historical context. It is not the source of $\mathcal A(q,R)$, and no constant from it enters a proof.

Krieger, Levin, Scherr, Tucker, Yasufuku, and Zieve study uniform boundedness of $S$-units in one-variable arithmetic dynamics [@kriegerEtAl2015]. In their published numbering, Theorem 1.7 is a monic $S$-integral polynomial-image bound. Theorem 1.8 is a local non-Archimedean valuation statement for one exceptional coefficient, and Corollary 1.9 gives the associated number-field, one-orbit consequence. These statements concern a one-variable image or specified orbit. They neither count all initial points in a two-dimensional Hénon window nor supply our four incidence types.

Bell and Ghioca treat intersections of one fixed orbit with a finitely generated subgroup in a semiabelian variety [@bellGhioca2024 Theorem 1.1]. Part (i) gives finitely many arithmetic progressions with a residual set of zero Banach density. In the regular-map setting, part (ii) makes the residual finite, not the entire hitting-time set. Here the initial point varies over all of $\Gamma^2$, finite rank need not mean finite generation, and consecutive survival is imposed over a short window. Moreover, although $H$ is regular on affine space, its restriction to $\mathbb G_m^2$ is generally rational because its first coordinate can vanish. We do not import a regular torus-map conclusion.

Ji, Xie, and Zhang prove cyclotomic periodic-point non-density in their Hénon setting, with a plane positive-entropy consequence [@jiXieZhang2026 Theorem 1.8 and Corollary 1.9]. Non-density is not finiteness, and those results do not give a finite-rank cardinality or fixed-window estimate. Mello and Yasufuku study higher-dimensional integrality and multiplicative dependence for semigroup dynamics [@melloYasufuku2026]. Their Theorems 1.1--1.2 and Corollary 1.3 invoke $\mathrm{Hyp}_{\epsilon}$ in the range $\epsilon\geq(1+c)/2$, whereas Theorem 4.2 combined with Vojta applies for sufficiently small $\epsilon$ and under additional divisor hypotheses. We do not merge those regimes, and that framework supplies no step here.

Kim, Krieger, Postolache, and Szeto construct Hénon maps with many rational periodic points [@kimEtAl2025]. Their Theorem A concerns odd $d>2$, maps of degree at most $d$, and at least $(d-4)^2$ rational periodic points. Their Theorem B concerns $d\equiv1\pmod6$ and a selected integer cycle of length $(8d+10)/3$. These are lower-bound constructions for selected maps, not classifications or upper bounds for all rational or integral periodic points.

The comparison is deliberately bounded. It supports the observation that none of the cited statements is the theorem package proved here. It does not establish precedence, exhaust every language or database, or rule out unpublished work. All cited arithmetic-dynamics papers above are boundary context only. Amoroso--Viada is the unique cited proof input, and even there only nondegenerate solutions are external; the degenerate analysis is internal.

There is a structural reason not to formulate the result as an orbit-intersection theorem. A set $T_m$ mixes many initial states, and constraints at successive times share variables. If one counts a first local equation alone, degenerate components can have a free parameter. The second local equation interacts with the first through the swapped coordinate, closing every branch when $s\geq2$. When $s=1$, three pairwise cancellations can align, and a fourth local equation is needed.

## Nondegeneracy and dynamical degeneracy

A quantitative unit-equation theorem counts solutions only after proper zero subsums have been removed. This qualification is substantial. For instance, if two terms cancel identically along a parameter, the remaining terms may satisfy the normalized equation without constraining that parameter. In a dynamical recurrence, such a parameter is not disposable: it is an orbit coordinate and must be carried to the next local equation. The present proof may therefore be viewed as a finite-state resolution of all proper-subsums at two adjacent times.

The sparse-image lemma of Section [4](#sec:sparse){reference-type="ref" reference="sec:sparse"} is the bridge between unit equations and this resolution. It applies the external nondegenerate estimate to a tuple formed from two group variables, then treats every degenerate subsum by an elementary polynomial root bound. In the main theorem, that lemma is used on a graph as soon as one of the two complementary equations has at least two terms. When a subsum contains neither or both of the distinguished linear terms, it instead fixes the input coordinate on a finite root set. The next recurrence then supplies the graph. This graph-versus-root distinction is why the component budget has two qualitatively different kinds of summands.

The support-one proof exhibits a different finite-state structure. A three-term local equation has exactly three possible pair-cancellation labels. Most adjacent label words immediately constrain both local coordinates. Two words retain a parameter; one closes after the third label, while the other has a single compatible three-letter continuation. A fourth label closes that continuation. The resulting $A/B/C$ ledger is included in full because replacing it by a generic finiteness assertion would conceal both the sharp depth and the coefficient compatibility of the infinite example.

## Scope comparison with the cited arithmetic dynamics

The one-variable $S$-unit results cited above constrain images or points on a specified orbit under number-field and integrality hypotheses. Our variables live in an arbitrary finite-rank subgroup of an arbitrary characteristic-zero field. Conversely, our conclusion is only about a fixed consecutive window, not the full orbit. Neither statement contains the other. The same separation holds for fixed-orbit intersection theorems: a structural description of return times for one point does not count all points that survive a prescribed initial window.

Cyclotomic non-density results and periodic-point constructions also operate at different quantifiers. Non-density permits an infinite exceptional set, whereas [\[eq:pc1-bound\]](#eq:pc1-bound){reference-type="eqref" reference="eq:pc1-bound"} is a cardinality bound. Periodic constructions select maps and exhibit many special points, whereas our upper bound is uniform over nonzero coefficients but concerns only short torus survival. These distinctions are stated explicitly to prevent a nearby theorem from being silently strengthened into the claim used here.

The cited recent semigroup work illustrates another boundary. Conditional conclusions must retain both the numerical range of their auxiliary hypothesis and the divisor assumptions used to justify that hypothesis. Since the relevant ranges recorded in Section [2](#sec:context){reference-type="ref" reference="sec:context"} do not align, no unconditional consequence is extracted. This paper instead uses only the unit-equation theorem whose exact hypotheses are stated in Theorem [\[thm:av\]](#thm:av){reference-type="ref" reference="thm:av"}.

## Why finite rank, rather than finite generation, is natural here

Every variable tuple used below is produced by a homomorphism from a finite Cartesian power of $\Gamma$. Rank therefore propagates transparently: two free group variables cost at most $2r$, and three cost at most $3r$. No generating set is selected, so neither the statement nor proof needs finite generation. This is important in the torsion audit. An infinite torsion subgroup has rank zero, but it can contain infinitely many elements. The proof never bounds a fiber by saying that the torsion is finite. It bounds fibers by the degree of a polynomial.

This rank-only organization also keeps coefficients outside the group. Adjoining $a,c,b_j$ to $\Gamma$ would produce an unnecessary auxiliary group and would obscure coefficient uniformity. The linear equation theorem already permits fixed coefficients. We use that permission directly, leaving the variable group as a homomorphic image of $\Gamma^2$ or $\Gamma^3$.

# Setup and quantitative unit equations {#sec:setup}

The rank of an abelian group $G$ is $$\operatorname{rank}G=\dim_{\mathbb Q}(G\otimes_{\mathbb Z}\mathbb Q).$$ Finite rank permits arbitrary torsion and does not imply finite generation. Every homomorphic image of $\Gamma^k$ has rank at most $kr$. Fixed scalars used as coefficients of a linear equation are not generators of the variable group.

The inverse of [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"} is $$H^{-1}(X,Y)=\left(Y,\frac{X-P(Y)}a\right).
 \label{eq:inverse}$$ Thus $a\neq0$ makes $H$ an automorphism and ensures that a recovered adjacent scalar state determines a finite orbit segment in either direction. We write $$H^i(x_0,x_{-1})=(x_i,x_{i-1}),
 \qquad
 x_{i+1}=P(x_i)+ax_{i-1}.$$

[\[thm:av\]]{#thm:av label="thm:av"} Let $q\geq2$, let $\mathcal G\leq(\overline K^*)^q$ have rank at most $R$, and fix $\alpha_1,\ldots,\alpha_q\in\overline K^*$. Then $$\alpha_1X_1+\cdots+\alpha_qX_q=1,
 \qquad (X_1,\ldots,X_q)\in\mathcal G,
 \label{eq:unit}$$ has at most $\mathcal A(q,R)$ solutions for which no nonempty proper subsum on the left vanishes.

This is the form of Amoroso--Viada, Theorem 6.2, used here [@amorosoViada2009]. Its published field is algebraically closed of characteristic zero. For arbitrary $K$, choose an algebraic closure $\overline K$ and include $K^*$ and $\Gamma$ into $\overline K^*$. The abstract rank of $\Gamma$ is unchanged. Each tuple group below is an image of $\Gamma^2$ or $\Gamma^3$, hence has rank at most $2r$ or $3r$. Every solution over $K$ injects into the solution set over $\overline K$, so a bound there bounds the original set. We make no descent claim and do not claim equality of the solution sets.

The coefficients $\alpha_i$ in [\[eq:unit\]](#eq:unit){reference-type="eqref" reference="eq:unit"} are fixed. Multiplying a variable coordinate by $a,c$, or $b_j$ changes a coefficient and does not enlarge $\mathcal G$. An output may therefore lie in a fixed coefficient coset while genuine variables remain in $\Gamma$.

We also use two elementary facts. For $\eta\in\overline K^*$ and $1\leq k\leq d$, the equation $X^k=\eta$ has at most $k\leq d$ roots. A nonzero polynomial of degree at most $d$ has at most $d$ roots. Both remain valid with infinite torsion: they are polynomial degree bounds, not group-size bounds.

A local equation splits into a nondegenerate and a degenerate locus. Theorem [\[thm:av\]](#thm:av){reference-type="ref" reference="thm:av"} controls only the first. On the second, at least one nonempty proper subsum vanishes. A point may have several such subsums. We choose any witness and union over all possible labels; the sets need not be disjoint. This intentional overcount prevents simultaneous cancellations from being omitted.

## Window coordinates and recovery

For clarity, the first few survivor conditions can be written without iterate notation. A point $(v,u)$ lies in $T_1$ precisely when $$u,v,z\in\Gamma,\qquad z=P(v)+au.$$ It lies in $T_2$ precisely when, in addition, $$w=P(z)+av\in\Gamma.$$ For the support-one $T_4$ problem there are four local recurrences and six scalar entries $x_{-1},x_0,\ldots,\allowbreak x_4$. The statement that $T_m$ has $m$ transitions and $m+1$ states is therefore literal, not a shifted indexing convention.

Recovery is used only after a local tuple has been counted. In the general-support nondegenerate equation, the tuple contains $z,u$ and all powers $v^{e_j}$; a fixed tuple has at most $d$ possible $v$. In a root branch, $v=\rho$ and $z$ determine $u$ through division by the nonzero $a$. In the monomial proof, a triple at any local index and a choice of the $d$-th root determine an adjacent state, after which [\[eq:inverse\]](#eq:inverse){reference-type="eqref" reference="eq:inverse"} propagates back to the initial state. These are finite-to-one maps, so counting the larger local tuple sets safely bounds initial states.

## The algebraic-closure bridge in detail

There are three separate assertions in the bridge, and keeping them separate avoids a hidden descent step. First, the inclusion $K^*\to\overline K^*$ is injective, so it identifies the abstract group $\Gamma$ with its image and preserves its rank. Second, applying a fixed monomial homomorphism after this inclusion cannot raise the rank beyond that of its source. Thus the rank bounds $2r$ and $3r$ remain valid over the algebraic closure. Third, every tuple satisfying an equation over $K$ is one of the tuples satisfying it over $\overline K$. The latter set can be larger, but an upper bound for it is still an upper bound for the injected $K$-set.

We never assert that a solution over $\overline K$ descends to $K$, and we never use equality of the solution sets. Similarly, the degree bounds are first valid over $\overline K$; restricting their root sets to $K$ or $\Gamma$ only decreases cardinality. This one-way reasoning is sufficient throughout.

## Proper subsums and simultaneous witnesses

For an equation with $q$ nonzero terms summing to $1$, the entire set of terms cannot be a zero subsum. A singleton cannot vanish. Therefore a degenerate witness has size between $2$ and $q-1$. In the sparse-image lemma we union all such subsets. In the Hénon equation we exploit the special roles of $Z$ and $U$ and classify witnesses by their membership.

A solution can have several witnesses. For example, two disjoint pair cancellations can hold simultaneously, or a pair cancellation can coexist with a larger cancellation. Assigning one label is only a device for proving coverage. Because the proof unions all labels, every solution with at least one witness is present in the union. Multiple membership can only increase the right side. No uniqueness of the chosen witness, no automaton determinism, and no inclusion--exclusion identity is assumed.

# Sparse polynomial images in finite-rank tori {#sec:sparse}

[\[lem:sparse-image\]]{#lem:sparse-image label="lem:sparse-image"} Let $$F(X)=\sum_{\ell=1}^{q} f_\ell X^{m_\ell}\in K[X],
 \qquad
 0\leq m_1<\cdots<m_q\leq d,
 \label{eq:sparse-F}$$ have exactly $q\geq2$ nonzero terms, and let $\lambda\in K^*$. Then $$\#\{(t,u)\in\Gamma^2:\lambda u=F(t)\}
 \leq d\bigl(\mathcal A(q,2r)+2^q-q-2\bigr).
 \label{eq:sparse-bound}$$

Normalize as $$\sum_{\ell=1}^{q}
 \frac{f_\ell}{\lambda}\,t^{m_\ell}u^{-1}=1.
 \label{eq:sparse-normalized}$$ The tuple $(t^{m_1}u^{-1},\ldots,t^{m_q}u^{-1})$ lies in a homomorphic image of $\Gamma^2$, of rank at most $2r$. Theorem [\[thm:av\]](#thm:av){reference-type="ref" reference="thm:av"}, after the field bridge, gives at most $\mathcal A(q,2r)$ nondegenerate image tuples. The ratio of coordinates $i<j$ gives $$t^{m_j-m_i}=X_j/X_i.
 \label{eq:power-recovery}$$ Since $1\leq m_j-m_i\leq d$, a tuple has at most $d$ preimages $t$. Then $u=F(t)/\lambda$ is unique. The nondegenerate contribution is at most $d\mathcal A(q,2r)$.

For a degenerate solution, a nonempty proper $I\subset[q]$ satisfies $$\sum_{\ell\in I}f_\ell t^{m_\ell}u^{-1}=0.
 \label{eq:sparse-degenerate}$$ A singleton cannot vanish. Thus $2\leq|I|\leq q-1$, and there are exactly $$\sum_{k=2}^{q-1}\binom qk=2^q-q-2$$ candidate subsets. Multiplying by $u$ gives the nonzero polynomial equation $$F_I(t)=0,\qquad F_I(X)=\sum_{\ell\in I}f_\ell X^{m_\ell}.$$ Distinct exponents make $F_I$ nonzero; its degree is at most $d$, so it has at most $d$ roots. For each root, $u$ is unique. A union bound contributes $d(2^q-q-2)$, proving the result.

[\[rem:torsion-cosets\]]{#rem:torsion-cosets label="rem:torsion-cosets"} The external estimate is rank-based, while every remaining fiber is a polynomial root fiber. No finiteness of torsion is needed. If the relation contains fixed multiples of $t$ or $u$, those multiples are absorbed into $\lambda$ and the $f_\ell$; the variable tuple still comes from $\Gamma^2$.

[\[cor:vertical\]]{#cor:vertical label="cor:vertical"} Assume $s\geq2$, fix $\rho\in K^*$, and put $$F_\rho(Z)=(c+a\rho)+\sum_{j=1}^{s}b_jZ^{e_j}.
 \label{eq:vertical-polynomial}$$ Then $$\#\{(z,w)\in\Gamma^2:w=F_\rho(z)\}\leq\mathcal S_*.$$

If $c+a\rho\neq0$, $F_\rho$ has $s+1$ terms with exponents $0,e_1,\ldots,e_s$, so Lemma [\[lem:sparse-image\]](#lem:sparse-image){reference-type="ref" reference="lem:sparse-image"} gives $\mathcal S_{s+1}$. If $c+a\rho=0$, the constant disappears but exactly $s\geq2$ nonzero terms remain, giving $\mathcal S_s$. Both are at most $\mathcal S_*$.

This cancellation audit is essential. With one monomial, removal of the constant leaves a monomial graph and a free torus parameter can survive. Section [7](#sec:supportone){reference-type="ref" reference="sec:supportone"} identifies the resulting exceptional chain. The lemma is nevertheless uniform over arbitrary coefficient values, because exact cancellations only choose which of the two permitted term counts applies.

## Two model applications of the lemma

The graph equations in the main proof illustrate both exponent patterns allowed in Lemma [\[lem:sparse-image\]](#lem:sparse-image){reference-type="ref" reference="lem:sparse-image"}. If $J$ has at least two elements, the polynomial $B_J(v)$ has no constant term, but distinct positive exponents. Coordinate ratios in the normalized unit equation still recover a positive power of $v$. If the graph is $c+B_{J^c}(v)$, exponent zero is present and the same argument applies. Thus the lemma does not privilege constant-plus-monomial polynomials over purely positive sparse polynomials.

A vertically cancelled graph is likewise not treated by continuity or specialization. When $c+a\rho=0$, one applies the lemma anew to the exact $s$-term polynomial $\sum b_jZ^{e_j}$. Its coefficients remain nonzero because $\rho$ affects only the constant coefficient. Consequently the count is $\mathcal S_s$, not an unproved limit of the $s+1$-term count. This direct case split is what prevents a monomial-style free branch.

The degree factor in $\mathcal S_q$ is deliberately common to the two parts of the proof. A nondegenerate tuple has at most $d$ input lifts. A degenerate subset has at most $d$ input roots. Adding those estimates before multiplying gives $$d\mathcal A(q,2r)+d(2^q-q-2)
 =d\bigl(\mathcal A(q,2r)+2^q-q-2\bigr).$$ No estimate for the number of outputs is added, because each input determines the output in the original graph equation.

## Uniformity under torsion-rich groups

Suppose, for example, that $\Gamma$ contains roots of unity of unbounded order. A fixed equation $t^k=\eta$ still has at most $k$ roots in the field, even though varying $k$ would encounter arbitrarily many torsion elements. Here every exponent $k$ is bounded by the fixed degree $d$. Similarly, a degenerate subpolynomial has fixed degree at most $d$. The proof therefore remains uniform without placing any independent bound on torsion.

This observation is also why rank-zero groups are not automatically harmless. They may be infinite, as noted after Proposition [\[prop:pc2\]](#prop:pc2){reference-type="ref" reference="prop:pc2"}. Finiteness follows here from the equations and degree bounds, not from rank zero by itself.

The lemma gives a cardinality, not an effective procedure. It does not provide heights, generators for a non-finitely-generated group, or an algorithm for locating the pairs. It also does not use additive closure of $\Gamma$: the equation is tested in $K$, while only $t$ and $u$ are required to be group elements.

## Exact accounting in the sparse-image lemma

The factor $d$ in the nondegenerate contribution is uniform even when no exponent equals zero. The ratio in [\[eq:power-recovery\]](#eq:power-recovery){reference-type="eqref" reference="eq:power-recovery"} eliminates $u^{-1}$ and yields a positive exponent difference. Any pair of distinct exponents works, and the largest possible difference is at most $d$. Once $t$ is chosen, the original unnormalized equation fixes $u$; a value with $F(t)=0$ cannot produce a solution because $\lambda u\neq0$.

For a degenerate subset $I$, multiplication by $u$ removes the common inverse factor. If the least selected exponent is positive, one may factor $t^{m_{\min I}}$, which is nonzero on $\Gamma$. The residual polynomial has nonzero constant term and degree $m_{\max I}-m_{\min I}\leq d$. If exponent zero is selected, the same conclusion holds without factoring. Thus the coarse degree-$d$ count covers both cases and does not rely on a constant term being present in $F$.

The number $2^q-q-2$ also includes all possible simultaneous degeneracies. It is the number of nonempty proper subsets after the $q$ singletons are removed. We do not divide by complementary pairs, because a chosen zero subset and its complement need not both vanish: the full sum equals $1$, so if one vanishes its complement sums to $1$. Counting every candidate separately is the correct safe union.

## Sparse graphs used at endpoints

A graph may present itself with the output multiplied by a coefficient. Relations such as $$-au=c+B_{J^c}(v)
 \quad\text{or}\quad
 au=-B_J(v)$$ fit Lemma [\[lem:sparse-image\]](#lem:sparse-image){reference-type="ref" reference="lem:sparse-image"} with $\lambda=-a$ or $a$. The input and output remain $v,u\in\Gamma$. Nothing requires $au\in\Gamma$, because $\lambda u$ is the left side of the field equation rather than a variable coordinate in the finite-rank tuple.

The endpoint $J=[s]$ may remove the constant-plus-complement side, but then the all-monomial side has $s$ terms. The endpoint $|J|=1$ may leave a monomial on one side, but the complementary side has the constant plus $s-1$ monomials, again $s$ terms. Exactly because $s\geq2$, an endpoint never forces us to apply the lemma to one term.

Corollary [\[cor:vertical\]](#cor:vertical){reference-type="ref" reference="cor:vertical"} is a second endpoint audit. Its two cases are exhaustive because the only possible merger of terms is cancellation of the exponent-zero coefficient $c+a\rho$. The positive exponents were collected in advance and their coefficients $b_j$ remain nonzero, so no further term disappears. This is why actual collected support, not a formal presentation with repeated or zero terms, enters the theorem.

# Two-transition finiteness for support $s\geq2$ {#sec:pc1proof}

## Two recurrences and the normalized first equation

Write $$Q=(v,u),\qquad H(Q)=(z,v),\qquad H^2(Q)=(w,z).
 \label{eq:three-states}$$ Then $Q\in T_2$ means $u,v,z,w\in\Gamma$ and $$\begin{aligned}
 z&=c+\sum_{j=1}^{s}b_jv^{e_j}+au,
 \label{eq:first-recurrence}\\
 w&=c+\sum_{j=1}^{s}b_jz^{e_j}+av.
 \label{eq:second-recurrence}\end{aligned}$$

## The rank-$3r$ nondegenerate locus

Set $$Z=\frac zc,\qquad U=-\frac{au}{c},\qquad
 M_j=-\frac{b_jv^{e_j}}c.
 \label{eq:ZU}$$ The first recurrence becomes $$Z+U+\sum_{j=1}^{s}M_j=1.
 \label{eq:first-unit}$$ The variable tuple $(z,u,v^{e_1},\ldots,v^{e_s})$ is an image of $\Gamma^3$, with rank at most $3r$. The factors $1/c,-a/c,-b_j/c$ are fixed coefficients. On the nondegenerate locus, Theorem [\[thm:av\]](#thm:av){reference-type="ref" reference="thm:av"} gives $\mathcal A(s+2,3r)$ tuples. Recovering $v$ costs at most $d$, while $z,u$ are fixed, so this locus contributes at most $$d\mathcal A(s+2,3r).
 \label{eq:pc1-nondeg}$$

## The four incidence types

Suppose [\[eq:first-unit\]](#eq:first-unit){reference-type="eqref" reference="eq:first-unit"} is degenerate and choose one nonempty proper zero subsum. Put $$B_J(X)=\sum_{j\in J}b_jX^{e_j}.
 \label{eq:BJ}$$ Except for R1, $J$ is the selected monomial set; for R1 it is the nonempty complementary monomial set. Membership of $Z,U$ gives Table [1](#tab:four-types){reference-type="ref" reference="tab:four-types"}.

::: {#tab:four-types}
  Type   Membership        Equations and convention                                          Label budget
  ------ ----------------- ----------------------------------------------------------------- ---------------------------------------
  GZ     $Z$ in, $U$ out   $z=B_J(v)$, $-au=c+B_{J^c}(v)$; $\varnothing\neq J\subseteq[s]$   one $\mathcal S_*$
  GU     $Z$ out, $U$ in   $au=-B_J(v)$, $z=c+B_{J^c}(v)$; $\varnothing\neq J\subseteq[s]$   one $\mathcal S_*$
  R0     neither in        $B_J(v)=0$, $|J|\geq2$                                            $(e_{\max J}-e_{\min J})\mathcal S_*$
  R1     both in           $c+B_J(v)=0$; $J$ complementary and nonempty                      $e_{\max J}\mathcal S_*$

  : The four zero-subsum incidence types.
:::

For GZ, selected and complementary equations are $$z=B_J(v),\qquad -au=c+B_{J^c}(v).
 \label{eq:GZ}$$ Their term counts are $|J|$ and $1+s-|J|$, whose sum is $s+1\geq3$. If $J=[s]$, use the first equation, with $s$ terms. If $|J|=1$, use the second, also with $s$ terms. Otherwise either multi-term side works. Lemma [\[lem:sparse-image\]](#lem:sparse-image){reference-type="ref" reference="lem:sparse-image"} bounds the graph by $\mathcal S_*$. Once $v$ is known, $z,u$ are fixed. There are $2^s-1$ labels.

For GU, $$au=-B_J(v),\qquad z=c+B_{J^c}(v).
 \label{eq:GU}$$ The identical term-count argument handles $J=[s]$, $|J|=1$, and the interior. Each graph costs $\mathcal S_*$, for another $2^s-1$ labels. The factor $a$ is an arbitrary fixed output coefficient; $a\in\Gamma$ is not required.

For R0, neither $Z$ nor $U$ occurs, so a witness contains at least two monomials and $$B_J(v)=0.
 \label{eq:R0}$$ Factoring $v^{e_{\min J}}$ leaves a nonzero polynomial with nonzero constant term and degree $e_{\max J}-e_{\min J}$. Thus there are at most that many roots $v=\rho$.

For R1, both $Z,U$ occur. The subsum is proper, so at least one monomial is complementary. With $J$ denoting that nonempty complement, the complementary equation is $$c+B_J(v)=0.
 \label{eq:R1}$$ It is nonzero of degree $e_{\max J}$, giving at most $e_{\max J}$ roots.

The four patterns exhaust a chosen witness. A point may have several witnesses, perhaps in different rows. We union every label and assert no disjointness, so simultaneous zero subsums are overcounted rather than lost.

## Root fibers and the budget

For an R0 or R1 root $v=\rho$, the second recurrence becomes $$w=(c+a\rho)+\sum_{j=1}^{s}b_jz^{e_j}.
 \label{eq:vertical-step}$$ It has $s+1$ terms if $c+a\rho\neq0$, and exactly $s\geq2$ if the constant cancels. Corollary [\[cor:vertical\]](#cor:vertical){reference-type="ref" reference="cor:vertical"} gives at most $\mathcal S_*$ pairs $(z,w)$. Then the first recurrence recovers $$u=\frac{z-P(\rho)}a.
 \label{eq:u-recovery}$$ Every root therefore costs at most $\mathcal S_*$.

Summing yields $$\begin{aligned}
 \#T_2(H,\Gamma)\leq{}&d\mathcal A(s+2,3r)\notag\\
 &+\Bigg[2(2^s-1)
 +\sum_{\substack{J\subseteq[s]\\|J|\geq2}}
 (e_{\max J}-e_{\min J})
 +\sum_{\varnothing\neq J\subseteq[s]}e_{\max J}\Bigg]\mathcal S_*.
 \label{eq:pc1-sum}\end{aligned}$$ This is [\[eq:pc1-bound\]](#eq:pc1-bound){reference-type="eqref" reference="eq:pc1-bound"} by [\[eq:M-definition\]](#eq:M-definition){reference-type="eqref" reference="eq:M-definition"}.

We verify both checksums. A nonempty subset with largest index $k$ includes $k$ and any subset of $[k-1]$, hence $$\sum_{\varnothing\neq J\subseteq[s]}e_{\max J}
 =\sum_{k=1}^{s}2^{k-1}e_k.
 \label{eq:max-sum}$$ In the spread sum the coefficients of $e_k$ as maximum and minimum are $2^{k-1}-1$ and $2^{s-k}-1$. Therefore $$\sum_{\substack{J\subseteq[s]\\|J|\geq2}}
 (e_{\max J}-e_{\min J})
 =\sum_{k=1}^{s}(2^{k-1}-2^{s-k})e_k.
 \label{eq:spread-sum}$$ It follows that $$\mathcal M(\mathbf e)=2^{s+1}-2+\sum_{k=1}^{s}(2^k-2^{s-k})e_k.
 \label{eq:M-closed}$$ Bounding every spread and maximum by $d$, and counting $2^s-s-1$ subsets of size at least two and $2^s-1$ nonempty subsets, gives $$\mathcal M(\mathbf e)\leq2(2^s-1)+d(2^{s+1}-s-2).
 \label{eq:M-crude}$$ Both are checksums only. The two subset sums in [\[eq:M-definition\]](#eq:M-definition){reference-type="eqref" reference="eq:M-definition"} define $\mathcal M$.

This closes the proof of Theorem [\[thm:pc1\]](#thm:pc1){reference-type="ref" reference="thm:pc1"}. Characteristic zero supports the unit-equation and root bounds; $c\neq0$ supports normalization; $a\neq0$ supports recovery; collected nonzero monomials make every subsum polynomial genuine; and $s\geq2$ closes graph endpoints and vertically cancelled fibers. No generic coefficient condition, additive group closure, or label disjointness was used.

## A second audit of the nondegenerate-to-degenerate split

The local tuple count in [\[eq:pc1-nondeg\]](#eq:pc1-nondeg){reference-type="eqref" reference="eq:pc1-nondeg"} and the component count in [\[eq:pc1-sum\]](#eq:pc1-sum){reference-type="eqref" reference="eq:pc1-sum"} cover complementary logical cases. If no nonempty proper subsum of [\[eq:first-unit\]](#eq:first-unit){reference-type="eqref" reference="eq:first-unit"} vanishes, the state is charged to the first term. Otherwise at least one witness exists and the state is charged to one of the four rows. The split is made at the first local equation only. We never need to classify degeneracy of the second equation globally: for a graph branch it is irrelevant, and for a root branch the sparse-image lemma already includes both the nondegenerate and degenerate parts of the second-step graph.

This organization avoids multiplying two large unit-equation constants. A naive approach could apply a nondegenerate theorem independently at two times and then struggle with mixed degeneracy. Here the first equation supplies either a finite tuple, a sparse graph, or a root. Only the root requires the second equation, where a two-variable sparse-image bound is enough. The rank consequently drops from $3r$ in the leading term to $2r$ inside $\mathcal S_*$.

The degree-$d$ lift of a nondegenerate tuple is safe even when the exponents have a common divisor. The tuple contains every selected power, including $v^d$; fixing that coordinate gives at most $d$ values of $v$. Using a greatest common divisor could sometimes improve the fiber, but the theorem seeks a support-uniform expression and makes no optimality claim. Once $v$ is fixed, the already counted tuple fixes $z,u$, so there is no second power multiplicity.

For a graph label, Lemma [\[lem:sparse-image\]](#lem:sparse-image){reference-type="ref" reference="lem:sparse-image"} counts ordered pairs, not merely possible inputs. This matters if a sparse polynomial takes the same output at different inputs. Its proof charges that multiplicity through the power-recovery factor and the degenerate root union. Therefore the graph contribution needs no additional degree factor in Section [5](#sec:pc1proof){reference-type="ref" reference="sec:pc1proof"}. Conversely, a root label first counts possible $v$ and then uses a full ordered-pair bound on $(z,w)$, which is why its contribution is a root count multiplied by $\mathcal S_*$.

The complementary equations in GZ and GU also certify that the output used in the sparse lemma is nonzero. For an actual survivor, $z,u\in\Gamma\subset K^*$. If a right side in [\[eq:GZ\]](#eq:GZ){reference-type="eqref" reference="eq:GZ"} or [\[eq:GU\]](#eq:GU){reference-type="eqref" reference="eq:GU"} vanished, that equality could not hold for the corresponding nonzero output. The lemma itself counts only pairs in $\Gamma^2$, so such field roots are automatically excluded. No separate removal of zero outputs is needed.

Finally, the component sum remains valid when a chosen zero subsum and its complement have special cancellations of their own. The selected witness gives one of the displayed necessary systems. Further cancellation merely places the state on a smaller intersection or produces another label. Since every budget bounds a superset of the actual survivor locus for that label, additional equations cannot enlarge it.

## Coverage before counting

We can verify the four-type classification directly from [\[eq:first-unit\]](#eq:first-unit){reference-type="eqref" reference="eq:first-unit"}. Let a witness select monomial indices $I$, and ask independently whether it selects $Z$ and $U$. If it selects $Z$ but not $U$, multiplying its zero equation by $c$ gives $z=B_I(v)$; subtracting it from the full recurrence gives the second GZ equation. If it selects $U$ but not $Z$, the same operation gives GU. If it selects neither, only selected monomials remain and at least two are needed, giving R0. If it selects both, propriety leaves a nonempty complementary monomial set $J$, and the complementary equation gives R1. These alternatives are exhaustive because membership in a chosen subset is binary.

The sign convention in [\[eq:ZU\]](#eq:ZU){reference-type="eqref" reference="eq:ZU"} matters. With $M_j=-b_jv^{e_j}/c$, selecting $Z$ and monomials yields $z=B_J(v)$, not $z=-B_J(v)$. Selecting $U$ and monomials yields $au=-B_J(v)$. Fixing this normalization once avoids changing labels when passing between the normalized equation and the recurrence.

For GZ and GU, the graph bound counts the input-output pair and the complementary equation fixes the remaining first-step coordinate. For example, if $z=B_J(v)$ is the multi-term graph, a pair $(v,z)$ fixes $u$ by the other equation. If $-au=c+B_{J^c}(v)$ is used instead, $(v,u)$ fixes $z$. The second recurrence is not needed for graph closure, so requiring $w\in\Gamma$ can only reduce the counted set.

For a root type, the first equation does not necessarily fix $z$. That is why [\[eq:vertical-step\]](#eq:vertical-step){reference-type="eqref" reference="eq:vertical-step"} is indispensable. Its sparse-image count is on $(z,w)$, and only afterward does [\[eq:u-recovery\]](#eq:u-recovery){reference-type="eqref" reference="eq:u-recovery"} give $u$. This order prevents an invalid attempt to regard an affine expression for $u$ as a group homomorphism.

## Degree bounds for the root types

For R0, write $j_0$ for the selected index of minimum exponent. Then $$B_J(X)=X^{e_{\min J}}
 \left(b_{j_0}+\sum_{j\in J\setminus\{j_0\}}
 b_jX^{e_j-e_{\min J}}\right).$$ A root $v\in\Gamma$ is nonzero, so only the parenthesized polynomial matters. Its constant coefficient is $b_{j_0}\neq0$, and its leading degree is $e_{\max J}-e_{\min J}$. This proves the exact spread bound rather than merely the coarser degree $d$.

For R1, the constant-plus-monomials polynomial $$c+B_J(X)$$ has nonzero constant coefficient and highest exponent $e_{\max J}$. It is never the zero polynomial, irrespective of algebraic relations among the numerical coefficients, because its exponents are distinct and $c\neq0$. Hence the degree bound is exactly $e_{\max J}$.

These algebraic-closure root counts may include roots outside $K$ and outside $\Gamma$. That only enlarges the sets used for the upper bound. For each actual root $\rho\in\Gamma$, vertical closure is applied over the original variables $z,w\in\Gamma$. A root occurring under several labels can be charged several times, consistently with the global union convention.

## Reading the component budget

The coefficient $2(2^s-1)$ in $\mathcal M(\mathbf e)$ is a number of graph labels, not a root count. Each GZ and GU label receives one $\mathcal S_*$. The spread sum is the total number of possible R0 roots before vertical closure, and the maximum sum is the analogous R1 total. Multiplying all three families by the common worst-case $\mathcal S_*$ gives a convenient uniform expression.

The maximum defining $\mathcal S_*$ is needed because different graph labels can have different term counts. At a GZ endpoint the chosen graph may have $s$ terms; away from the endpoint it may have any value from two through $s$. The vertical graph has $s$ or $s+1$ terms. Taking the maximum for $2\leq q\leq s+1$ covers every case without asserting monotonicity of the explicit formula in $q$.

The closed checksum [\[eq:M-closed\]](#eq:M-closed){reference-type="eqref" reference="eq:M-closed"} can contain negative individual coefficients $2^k-2^{s-k}$ for small $k$, but the total is positive because it equals the defining sum of nonnegative component counts. This is another reason to retain [\[eq:M-definition\]](#eq:M-definition){reference-type="eqref" reference="eq:M-definition"} as the definition. The crude checksum [\[eq:M-crude\]](#eq:M-crude){reference-type="eqref" reference="eq:M-crude"} discards exponent spacing and is useful only as a quick universal comparison.

## No surviving monomial curve

One possible source of a counterexample would be a monomial curve on which the first local equation degenerates identically and the second imposes no new sparse constraint. The four-type proof rules this out under the hypotheses. Graph types already have finite torus intersection by Lemma [\[lem:sparse-image\]](#lem:sparse-image){reference-type="ref" reference="lem:sparse-image"}. Root types fix $v$ on finite sets, and [\[eq:vertical-step\]](#eq:vertical-step){reference-type="eqref" reference="eq:vertical-step"} has at least two terms after every possible constant cancellation. Hence no free chain survives two transitions.

This statement is local to the collected generalized Hénon form. It is not a classification of all algebraic curves invariant under a map, and it says nothing about coefficients after arbitrary conjugacy. It is exactly the closure needed for the finite window $T_2$.

# Sharpness and essential hypotheses {#sec:sharpness}

Fix the support and take $$K=\mathbb Q,\quad a=1,\quad b_1=\cdots=b_s=1,\quad
 c=-s,\quad\Gamma=\langle2\rangle.
 \label{eq:pc2-data}$$ Then $P(1)=0$. For every $n\geq0$, $$(1,2^n)\longmapsto(2^n,1).
 \label{eq:pc2-orbit}$$ Both states lie in $\Gamma^2$; the initial states are distinct. Thus $T_1$ is infinite in rank one for every prescribed support. With Theorem [\[thm:pc1\]](#thm:pc1){reference-type="ref" reference="thm:pc1"}, two transitions are shortest.

Over a field containing all roots of unity, a rank-zero variant uses $\Gamma=\mu_\infty$. It is secondary and not a classification.

The condition $c\neq0$ is essential. For $$c=0,\qquad P(X)=X^d+X,\qquad a=-1,
 \label{eq:c-zero-data}$$ and any infinite $\Gamma$, $$(t,t^d)\longmapsto(t,t)\longmapsto(t^d,t)
 \label{eq:c-zero-orbit}$$ for all $t\in\Gamma$. Thus $T_2$ is infinite with two monomials.

The condition $a\neq0$ is also essential. For $$a=0,\qquad P(X)=-1+X+X^2,
 \label{eq:a-zero-data}$$ one has $P(1)=1$, and $$(1,t)\longmapsto(1,1)\longmapsto(1,1)
 \label{eq:a-zero-orbit}$$ for every $t$ in an infinite subgroup. The triangular map forgets its second coordinate.

These examples do not classify all excluded coefficient strata. They show that a coefficient-uniform theorem cannot simply drop $a\neq0$ or $c\neq0$. Proposition [\[prop:pc2\]](#prop:pc2){reference-type="ref" reference="prop:pc2"} proves optimality of transition depth, not of the numerical constants.

## What the examples establish

In [\[eq:pc2-data\]](#eq:pc2-data){reference-type="eqref" reference="eq:pc2-data"}, the identity $P(1)=0$ is independent of the exponents. This is why one construction proves sharpness for every prescribed support. The free parameter appears as the second coordinate of the initial state and becomes the first coordinate after one transition. A second transition is not claimed to survive, and none is needed to prove that $T_1$ is infinite.

The $c=0$ example is stronger in a different direction. It survives two transitions and retains two actual monomials, showing that the constant is what permits the normalization and the complementary constant equations in the proof. The $a=0$ example shows that invertibility is not cosmetic: once the map forgets the second coordinate, an entire vertical family can collapse to one fixed state.

These examples are exact substitutions rather than limiting arguments. They do not imply that every map with $a=0$ or $c=0$ has an infinite survivor set. They establish the failure of a theorem uniform over all such coefficients. Nor do they address optimal cardinality constants within the nondegenerate coefficient range.

# The complete support-one comparison {#sec:supportone}

## Statement and scalar recurrence

Let $P(X)=c+bX^d$, $d\geq2$, and write $$x_{i+1}=bx_i^d+ax_{i-1}+c,\qquad
 H^i(x_0,x_{-1})=(x_i,x_{i-1}).
 \label{eq:monomial-recurrence}$$

## Nondegenerate local equations

For $Q\in T_4$, there are four local equations, at $i=0,1,2,3$. Normalize one as $$\frac{x_{i+1}}c-\frac bcx_i^d-\frac acx_{i-1}=1.
 \label{eq:monomial-unit}$$ The variable triple $(x_{i+1},x_i^d,x_{i-1})$ has rank at most $3r$. Theorem [\[thm:av\]](#thm:av){reference-type="ref" reference="thm:av"} bounds nondegenerate triples by $\mathcal A(3,3r)$, and recovering $x_i$ costs at most $d$. Since $a\neq0$, the local state determines the string forward and backward. Unioning the four indices contributes $$4d\mathcal A(3,3r).
 \label{eq:pc3-nondeg}$$

## Derivation of the $A/B/C$ labels

For the fully degenerate locus, put $\alpha=-c/a$. Each three-term equation has at least one pair cancellation, producing $$\begin{aligned}
 A_i:\quad&x_{i-1}=\alpha,&x_{i+1}&=bx_i^d,
 \label{eq:A-label}\\
 B_i:\quad&bx_i^d=-c,&x_{i+1}&=ax_{i-1},
 \label{eq:B-label}\\
 C_i:\quad&bx_i^d=-ax_{i-1},&x_{i+1}&=c.
 \label{eq:C-label}\end{aligned}$$ Choose one label if several occur and union all choices.

## Nine adjacent words

Put $u=x_{i-1}$, $v=x_i$. Direct substitution gives Table [2](#tab:nine-words){reference-type="ref" reference="tab:nine-words"}.

::: {#tab:nine-words}
  Word   Necessary conditions on $u,v$     Bound or status
  ------ --------------------------------- -----------------
  $AA$   $u=\alpha,\ v=\alpha$             $1$
  $AB$   $u=\alpha,\ b^{d+1}v^{d^2}=-c$    $d^2$
  $AC$   $u=\alpha,\ b^{d+1}v^{d^2}=-av$   $d^2-1$
  $BA$   $v=\alpha,\ b\alpha^d=-c$         $u$ free
  $BB$   $v^d=-c/b,\ u^d=-c/(ba^d)$        $d^2$
  $BC$   $v^d=-c/b,\ u^d=-v/(ba^{d-1})$    $d^2$
  $CA$   $v=\alpha,\ u=-b\alpha^d/a$       $1$
  $CB$   $bc^d=-c,\ u=-bv^d/a$             $v$ free
  $CC$   $v=-bc^d/a,\ u=-bv^d/a$           $1$

  : All adjacent support-one label words.
:::

For $A_i$, one has $u=\alpha$, $x_{i+1}=bv^d$. The next $A,B,C$ labels yield $$v=\alpha,\qquad b(bv^d)^d=-c,\qquad b(bv^d)^d=-av.$$ For $B_i$, one has $bv^d=-c$, $x_{i+1}=au$, and the next labels yield $$v=\alpha,\qquad b(au)^d=-c,\qquad b(au)^d=-av.$$ For $C_i$, one has $u=-bv^d/a$, $x_{i+1}=c$, and the next labels yield $$v=\alpha,\qquad bc^d=-c,\qquad bc^d=-av.$$ These derive every row. Only $BA$ and $CB$ remain free after two labels.

## The $BA$ continuation

For $BA$, compatibility is $b\alpha^d=-c$, and, with $t=u$, the chain is $$t,\quad\alpha,\quad at,\quad ba^dt^d.
 \label{eq:BA-chain}$$

::: {#tab:BA}
  Word    New equation                    Bound
  ------- ------------------------------- ---------
  $BAA$   $at=\alpha$                     $1$
  $BAB$   $b^{d+1}a^{d^2}t^{d^2}=-c$      $d^2$
  $BAC$   $b^{d+1}a^{d^2}t^{d^2}=-a^2t$   $d^2-1$

  : Every continuation of $BA$.
:::

The first equation fixes $t$. The other two arise by raising $ba^dt^d$ to the $d$-th power and applying the next cancellation. In $BAC$, divide by $t\neq0$. Every $BA$ continuation closes at the third label.

## The $CB$ and $CBA$ continuations

For $CB$, the chain and compatibility are $$-bt^d/a,\quad t,\quad c,\quad at,
 \qquad bc^{d-1}=-1.
 \label{eq:CB-chain}$$

::: {#tab:CB-CBA}
  Word     Compatibility or equation         Bound or status
  -------- --------------------------------- -----------------
  $CBA$    $c=\alpha$, equivalently $a=-1$   $t$ free
  $CBB$    $ba^dt^d=-c$                      $d$
  $CBC$    $ba^dt^d=-ac$                     $d$
  $CBAA$   $-t=c$                            $1$
  $CBAB$   $b^{d+1}(-t)^{d^2}=-c$            $d^2$
  $CBAC$   $b^{d+1}(-t)^{d^2}=-t$            $d^2-1$

  : Closure of $CB$ and the unique free three-letter branch.
:::

The third $A$ label says $c=\alpha=-c/a$, hence $a=-1$; it is the only third letter that leaves $t$ free. Under $$a=-1,\qquad bc^{d-1}=-1,
 \label{eq:CBA-compatibility}$$ the chain is $$bt^d,\quad t,\quad c,\quad -t,\quad b(-t)^d.
 \label{eq:CBA-chain}$$ The fourth label gives the last three table rows. All are nonzero polynomial equations of degree at most $d^2$. Thus no four-letter word remains free.

## The word union and sharpness

There are $3^4=81$ four-letter choices. Table [2](#tab:nine-words){reference-type="ref" reference="tab:nine-words"} closes every word except those beginning $BA,CB$; Table [3](#tab:BA){reference-type="ref" reference="tab:BA"} closes the former at letter three; Table [4](#tab:CB-CBA){reference-type="ref" reference="tab:CB-CBA"} closes the latter by letter four. Each word has at most $d^2$ initial states. Multiple labels merely repeat a point, so the fully degenerate contribution is at most $$81d^2.
 \label{eq:pc3-degenerate}$$ Together with [\[eq:pc3-nondeg\]](#eq:pc3-nondeg){reference-type="eqref" reference="eq:pc3-nondeg"}, this proves [\[eq:pc3-bound\]](#eq:pc3-bound){reference-type="eqref" reference="eq:pc3-bound"}.

For sharpness choose $$c^{d-1}=-1,\quad K=\mathbb Q(c),\quad b=1,\quad a=-1,\quad
 \Gamma=\langle2,c,-1\rangle.
 \label{eq:pc3-sharp-data}$$ The elements $c,-1$ are torsion and $2$ has infinite order, so $\Gamma$ has rank one. For $t=2^n$, let $Q_t=(t,t^d)$. The scalar segment is $$x_{-1},x_0,x_1,x_2,x_3
 =t^d,\quad t,\quad c,\quad -t,\quad(-t)^d.
 \label{eq:pc3-sharp-chain}$$ Since $c^d=-c$, $$t^d-t^d+c=c,\qquad c^d-t+c=-t,\qquad
 (-t)^d-c+c=(-t)^d.$$ All entries lie in $\Gamma$, so $Q_t\in T_3$. Distinct $t=2^n$ give infinitely many points. The cancellations are $C,B,A$, realizing the free chain exactly. This proves Theorem [\[thm:pc3\]](#thm:pc3){reference-type="ref" reference="thm:pc3"}.

## Consistency of the continuation coordinates

The scalar chains used in the exceptional rows can be checked directly from the recurrence. On $BA$, start with $x_{i-1}=t$ and $x_i=\alpha$. The $B_i$ relation gives $b\alpha^d=-c$, and the complementary recurrence gives $x_{i+1}=at$. The $A_{i+1}$ relation then gives $x_{i+2}=b(at)^d=ba^dt^d$. Thus every equation in Table [3](#tab:BA){reference-type="ref" reference="tab:BA"} is imposed at the next index on the ordered chain [\[eq:BA-chain\]](#eq:BA-chain){reference-type="eqref" reference="eq:BA-chain"}; no coordinate has been reversed.

On $CB$, start with $x_i=t$. The $C_i$ relation gives $x_{i-1}=-bt^d/a$, while the recurrence gives $x_{i+1}=c$. The $B_{i+1}$ relation is exactly $bc^d=-c$, and its complementary recurrence gives $x_{i+2}=at$. Under the next label $A$, the equation $x_i=\alpha$ would appear if $A$ were at the original index, but $A_{i+2}$ instead requires $x_{i+1}=\alpha$, namely $c=\alpha$. This indexing distinction is what leaves $t$ free and forces only $a=-1$.

Once $a=-1$, the initial coordinate on the $CB$ chain becomes $bt^d$, so the compatible chain is [\[eq:CBA-chain\]](#eq:CBA-chain){reference-type="eqref" reference="eq:CBA-chain"}. At the fourth label, $A$ requires the preceding coordinate $-t$ to equal $\alpha=c$, giving $-t=c$. The $B$ and $C$ choices evaluate $b[b(-t)^d]^d$; using the compatibility $bc^{d-1}=-1$ reduces the right-side linear term exactly to the equations in Table [4](#tab:CB-CBA){reference-type="ref" reference="tab:CB-CBA"}. The displayed equations therefore incorporate, rather than ignore, both coefficient compatibilities.

The uniform $d^2$ word ceiling remains valid for words whose locus is empty. It also remains valid for small degrees such as $d=2$: the expressions of degree $d^2-1$ are then nonconstant of degree three, and all constants used to form them are nonzero. No exceptional parity is required. Parity affects the concrete value $(-t)^d$ in the sharp chain but not its membership in $\Gamma$ or the recurrence verification.

The automaton is used only for four consecutive local equations. It does not assert that $A,B,C$ form a global symbolic coding of all orbits, that every label word is realizable, or that a compatible word extends indefinitely. The sharp example realizes $CBA$ for three local equations and proves exactly the failure of uniform $T_3$ finiteness. The upper-bound ledger proves that a fourth label cannot keep a parameter free.

## Detailed derivation of the adjacent bounds

The entries $AA,CA,CC$ in Table [2](#tab:nine-words){reference-type="ref" reference="tab:nine-words"} fix $u,v$ directly. The row $AC$ gives $$b^{d+1}v^{d^2}+av=0.$$ Since $v\neq0$, dividing by $v$ gives a nonzero polynomial of degree $d^2-1$. The same nonzero-variable division is used in $BAC$ and $CBAC$. It is legitimate even with torsion because it is algebra in the field, not a statement about orders in the group.

For $AB$, one polynomial of degree $d^2$ fixes $v$, and $u=\alpha$. For $BB$, the equations $v^d=-c/b$ and $u^d=-c/(ba^d)$ give at most $d^2$ pairs. For $BC$, the first equation gives at most $d$ values of $v$, and for each such value the second gives at most $d$ values of $u$. The row $CB$ has only coefficient compatibility because $x_{i+1}=c$ is substituted into $B_{i+1}$; hence its parameter genuinely remains free at length two.

Every bound is a count over the algebraic closure. A fortiori it bounds the solutions in $\Gamma$. Once $u,v$ are fixed, the recurrence and $a\neq0$ determine the initial state and the finite string. Thus the table does not omit a further multiplicity in passing from local coordinates to $Q$.

## Why $BA$ and $CB$ are the only free pairs

A free adjacent word must make its second cancellation a coefficient relation or an equation in a coordinate already fixed independently of the parameter. Under $A$, the first coordinate $u$ is fixed but $v$ remains; each second label either fixes $v$ or imposes a nonzero polynomial in $v$. Under $B$, $v$ is restricted to finitely many roots while $u$ remains; only $A$ fails to constrain $u$, giving $BA$. Under $C$, $u$ is a monomial in $v$ and the next state is the constant $c$; only $B$ becomes the coefficient relation $bc^d=-c$, giving $CB$. This exhausts the nine rows conceptually as well as computationally.

On $BA$, the free parameter moves to $at$, and every possible third label sees it or a nonconstant power of it. The equations in Table [3](#tab:BA){reference-type="ref" reference="tab:BA"} are consequently nonzero. On $CB$, the third $A$ label sees only the constant coordinate $c$, so it can reduce to $a=-1$ without seeing $t$. The other third labels see $at$ through a $d$-th power and close. This isolates $CBA$ as the only possible three-letter free word.

Under the two compatibility conditions for $CBA$, the parameter alternates from $t$ to $-t$ while the constant $c$ occupies the middle coordinate. The fourth local equation sees $-t$ or $b(-t)^d$, and each label gives a nonzero polynomial. The degree never exceeds $d^2$, explaining why one uniform word budget $d^2$ suffices.

## Word coverage and simultaneous labels

A fully degenerate string need not have a unique word. At an index, two pair subsums could vanish, causing two labels. Choose one available letter independently at each of the four indices. This produces at least one word in $\{A,B,C\}^4$, and the corresponding table equations are necessary for the string. Taking all $81$ words therefore covers it. If another choice produces another word, the string is counted again, which is harmless.

The word bound is not multiplied by a further number of orbit positions. The four letters are attached to the fixed indices $0,1,2,3$. The local pair $u=x_{-1},v=x_0$ is the initial scalar state, so at most $d^2$ possible pairs under a word means at most $d^2$ initial points. The separate factor four occurs only in [\[eq:pc3-nondeg\]](#eq:pc3-nondeg){reference-type="eqref" reference="eq:pc3-nondeg"}, where one unions the possibility that any one of the four local equations is nondegenerate.

## Audit of the sharp chain

The relation $c^{d-1}=-1$ implies $c^{2(d-1)}=1$, so $c$ is torsion in $K^*$. Hence adjoining $c$ and $-1$ to $\langle2\rangle$ does not change rank. The points $Q_t=(t,t^d)$ are distinct because their first coordinates $2^n$ are distinct.

The scalar ordering in [\[eq:pc3-sharp-chain\]](#eq:pc3-sharp-chain){reference-type="eqref" reference="eq:pc3-sharp-chain"} is important. The initial point is $(x_0,x_{-1})=(t,t^d)$. The first transition gives $(x_1,x_0)=(c,t)$, the second gives $(-t,c)$, and the third gives $((-t)^d,-t)$. Thus exactly four states lie in $\Gamma^2$, as required for $T_3$. No assertion is made about the fourth transition.

At the three local indices, the cancellations are $$x_0^d-x_{-1}=0,\qquad c^d+c=0,\qquad -x_1+c=0,$$ which correspond to $C,B,A$ with $a=-1,b=1$. The example therefore verifies both the abstract sharpness statement and the precise exceptional branch in the ledger.

# Phase transition, limitations, and conclusion {#sec:conclusion}

## The support-size phase transition

For collected support at least two, $T_2$ is uniformly finite and $T_1$ can be infinite. For support one, $T_4$ is uniformly finite and $T_3$ can be infinite. The proof explains the discontinuity: after a root branch fixes the first coordinate, the second-step polynomial retains at least two terms when $s\geq2$, even if its constant cancels. With one monomial, that cancellation leaves a monomial and permits $CBA$.

The phase transition concerns window length, not eventual escape time for each individual orbit. A point outside $T_2$ fails within two transitions, while a point inside $T_2$ is merely one of finitely many short survivors; the theorem does not assert when or whether its later orbit leaves $\Gamma^2$. Similarly, the support-one bound concerns five consecutive states and is not a periodicity theorem.

The coefficient-uniform estimates also do not identify exceptional coefficient loci sharply. The ledgers describe every local cancellation used for counting, but their unions may overlap substantially and their degree bounds may be far from attained. What is sharp is the shortest window valid uniformly across the stated coefficient class.

The distinction between theorem scope and proof technique is also useful. Unit equations are a means of obtaining the displayed cardinality, but the theorem is not presented as a general statement about all polynomial equations over finite-rank groups. The Hénon recurrence supplies a very specific sharing of variables between two local equations. The four-type ledger exploits that sharing, and its conclusion should not be transported to an unrelated recurrence without a new degeneracy analysis.

Likewise, the support-one automaton is complete only for the three terms $bx_i^d,ax_{i-1},c$ in the stated scalar recurrence. Adding terms changes both the local labels and their continuation rules; in the present paper those additional terms are handled by the sparse graph argument instead. Removing a structural term can produce the counterexamples of Section [6](#sec:sharpness){reference-type="ref" reference="sec:sharpness"}. These boundaries are part of the mathematical statement, not qualifications added merely for exposition.

The explicit estimates are finite but extremely large. Their value here is uniform logical closure: every dependence on $s,d,r$ is displayed, and every coefficient is absent from the right side. Improving constants would require sharper nondegenerate unit-equation input, finer power fibers, or less wasteful overlap accounting. None of those possible refinements changes the sharp transition depth proved by the examples.

The constants separate every source of loss. Nondegenerate local equations use rank $3r$; sparse graphs use rank $2r$; the remaining factors are power fibers, polynomial roots, subset labels, or label words. This makes the result coefficient-uniform without suggesting numerical optimization.

## Limitations and conclusion

1.  No positive-characteristic analogue is asserted.

2.  The two-transition theorem does not allow $c=0$, $a=0$, or a zero displayed $b_j$.

3.  Equal exponents are combined and zero coefficients deleted before support is counted.

4.  Support size is not asserted invariant under affine or polynomial conjugacy.

5.  None of the displayed constants is asserted optimal.

6.  No effective enumeration algorithm for $T_2$ or $T_4$ is provided.

7.  No height estimate is obtained.

8.  Periodic points, rational periodic points, and integral cycles are not classified.

9.  Every coefficient stratum with an infinite shorter window is not classified.

10. No theorem is given for arbitrary rational maps, polynomial automorphisms, Hénon compositions, or normal forms.

11. Finite-rank scope is not enlarged to arbitrary subgroups.

12. Finite rank is not replaced by finite generation.

13. No coefficient is assumed to lie in $\Gamma$.

14. No additive closure of $\Gamma$ is assumed.

15. The bounded literature comparison neither establishes precedence nor excludes unpublished work.

16. Bell--Ghioca's finite residual is not treated as finiteness of the whole hitting-time set, and the torus restriction is not declared regular.

17. Ji--Xie--Zhang non-density is not converted into finiteness.

18. The Mello--Yasufuku $\epsilon$-regimes are not merged.

19. The restricted constructions of Kim and collaborators are not made universal bounds.

20. No code, computer algebra, computation, scan, experiment, data, or numerical check is theorem evidence.

21. The support-one result receives no separate precedence assertion and is proved internally rather than used as a black box.

Within these boundaries, increasing actual support from one monomial to at least two lowers the sharp coefficient-uniform finite-rank torus-survival threshold from four transitions to two.

## Publication relation

An earlier manuscript by the same authors treated only the one-monomial case. The present paper reproduces that theorem and proof in full as part of the support-size phase transition, thereby absorbing the earlier manuscript; the two manuscripts will not be submitted in parallel, and the present paper is the sole intended external version of the overlapping material.

# Rank and power-fiber audit {#app:rank}

For the sparse-image equation define $$\phi(t,u)=(t^{m_1}u^{-1},\ldots,t^{m_q}u^{-1}).$$ Its image has rank at most $2r$. A coordinate ratio specifies $t^{m_j-m_i}$, whose fiber has at most $d$ elements. Then $u$ is unique. Fixed coefficient multipliers do not enter $\phi$.

For the first Hénon equation, the map $$(z,u,v)\longmapsto(z,u,v^{e_1},\ldots,v^{e_s})$$ has image rank at most $3r$. The normalized $Z,U,M_j$ differ only by fixed scalars, and a power coordinate recovers $v$ with at most $d$ choices. The support-one triple has the same $3r$ rank and $d$ fiber.

Embedding $K$ in $\overline K$ leaves these abstract maps and ranks unchanged. Original solutions inject into algebraic-closure solutions. The larger field is used only for Theorem [\[thm:av\]](#thm:av){reference-type="ref" reference="thm:av"}; no descent is inferred.

Infinite torsion causes no further multiplicity. Every recovery equation is a nonzero polynomial of degree at most $d$, and every degenerate subsum is likewise a polynomial root condition.

More formally, tensoring the domain of each monomial map with $\mathbb Q$ gives a vector space of dimension $2r$ or $3r$; the image dimension cannot exceed the domain dimension. Torsion maps to zero under this tensor operation, which is why rank alone does not bound a power-map kernel. The kernel is instead bounded inside each fiber by the degree of $X^k-\eta$. This separation between rank and degree is used in every nondegenerate contribution.

For a degenerate sparse subset, no power recovery is necessary. The zero subsum itself gives a polynomial in the input. Factoring a nonzero lowest power does not add the root $0$, because all inputs lie in $K^*$. Once an input root is chosen, the full sparse equation determines its output uniquely. Thus the same arbitrary-torsion audit applies to both halves of Lemma [\[lem:sparse-image\]](#lem:sparse-image){reference-type="ref" reference="lem:sparse-image"}.

## Homomorphism matrices {#homomorphism-matrices .unnumbered}

Modulo torsion, choose coordinates on $\Gamma\otimes_{\mathbb Z}\mathbb Q$. The sparse-image homomorphism is represented by $q$ rows $$(m_1,-1),\ (m_2,-1),\ \ldots,\ (m_q,-1),$$ acting on two copies of that rank-$r$ vector space. Its image dimension is at most $2r$, independently of the sizes of the exponents. The first Hénon tuple map is represented schematically by $$(1,0,0),\ (0,1,0),\
 (0,0,e_1),\ldots,(0,0,e_s)$$ on the $z,u,v$ factors, so its image dimension is at most $3r$. The support-one map uses $$(1,0,0),\ (0,d,0),\ (0,0,1)$$ on $x_{i+1},x_i,x_{i-1}$ and has the same bound.

Multiplication by $1/c,-a/c,-b_j/c$ translates these image groups coordinatewise but does not alter the variable homomorphisms or their ranks. The unit-equation theorem allows those fixed coefficients directly. Consequently the ranks used in the three applications are exactly bounded by $2r,3r,3r$, with no auxiliary coefficient rank.

The three relevant inclusions and rank inequalities may therefore be summarized as $$\phi(\Gamma^2)\hookrightarrow(\overline K^*)^q,
 \quad \operatorname{rank}\phi(\Gamma^2)\leq2r;
 \qquad
 \psi(\Gamma^3)\hookrightarrow(\overline K^*)^{s+2},
 \quad \operatorname{rank}\psi(\Gamma^3)\leq3r;$$ $$\chi(\Gamma^3)\hookrightarrow(\overline K^*)^3,
 \quad \operatorname{rank}\chi(\Gamma^3)\leq3r.$$ Every original tuple injects into the corresponding algebraic-closure equation. Fixed coefficient translations affect the linear equation but not these inequalities, and restricting the resulting finite algebraic-closure set back to $K$ cannot increase its cardinality.

In particular, the constants are applied with $$(q,R)=(q,2r),\qquad (s+2,3r),\qquad (3,3r),$$ and with no coefficient-generated correction to $R$. This exhausts the three rank computations used in the article.

# PC1 subset and component ledger {#app:pc1-ledger}

For GZ and GU there are $2^s-1$ nonempty subsets each. Their endpoint equations always leave one polynomial with at least $s\geq2$ terms: $$z=B_{[s]}(v),\qquad
 -au=c+B_{J^c}(v)\quad(|J|=1),$$ or their GU analogues. Fixed factors are coefficients, not group generators.

R0 produces $$\sum_{\substack{J\subseteq[s]\\|J|\geq2}}
 (e_{\max J}-e_{\min J})$$ roots after the least monomial is removed. R1, with complementary nonempty $J$, produces $$\sum_{\varnothing\neq J\subseteq[s]}e_{\max J}$$ roots. Every root is closed by $$w=(c+a\rho)+\sum_{j=1}^{s}b_jz^{e_j},$$ with $s+1$ terms or exactly $s$ after cancellation.

A maximum $e_k$ appears in $2^{k-1}$ nonempty subsets. Its net spread coefficient is $2^{k-1}-2^{s-k}$. These counts reproduce [\[eq:M-closed\]](#eq:M-closed){reference-type="eqref" reference="eq:M-closed"}; bounding degrees by $d$ reproduces [\[eq:M-crude\]](#eq:M-crude){reference-type="eqref" reference="eq:M-crude"}. Simultaneous labels only repeat states in the union.

The two graph counts do not depend on exponent gaps. By contrast, R0 remembers the spread within each selected subset, while R1 remembers its maximum. This explains the two different subset sums and also shows why replacing them immediately by $d$ loses structural information.

For an endpoint graph, the polynomial with two or more terms may be on either side of the pair of complementary equations. Applying the sparse lemma to that side fixes the shared input and one output; the other equation then fixes the remaining coordinate. No multiplication by a coefficient is treated as membership in $\Gamma$. For a root label, the second recurrence is always used, including when the vertical constant cancels. These observations reproduce the exact budgets of Table [1](#tab:four-types){reference-type="ref" reference="tab:four-types"}.

## Combinatorial reconstruction {#combinatorial-reconstruction .unnumbered}

For the maximum sum, partition nonempty subsets by their largest index. If $\max J=k$, then $k\in J$, no index above $k$ occurs, and each of the $k-1$ lower indices is optional. Thus there are $2^{k-1}$ such subsets and their contribution is $2^{k-1}e_k$.

For the spread sum, a subset of size at least two with maximum $k$ is obtained from the same choices except that at least one lower index must be selected. Its maximum contribution is therefore $$(2^{k-1}-1)e_k.$$ A subset with minimum $k$ contains $k$, contains no lower index, and selects a nonempty subset of the $s-k$ higher indices. Its minimum contribution is $$(2^{s-k}-1)e_k.$$ Subtracting minimum contributions from maximum contributions and then adding the separate maximum sum gives $$\sum_{k=1}^{s}
 \left[(2^{k-1}-1)-(2^{s-k}-1)+2^{k-1}\right]e_k
 =
 \sum_{k=1}^{s}(2^k-2^{s-k})e_k.$$ After the graph term $2(2^s-1)=2^{s+1}-2$ is restored, this is exactly [\[eq:M-closed\]](#eq:M-closed){reference-type="eqref" reference="eq:M-closed"}.

For the crude check, the number of subsets with at least two elements is $$2^s-\binom s0-\binom s1=2^s-s-1.$$ The number of nonempty subsets is $2^s-1$. Replacing every spread and every maximum by $d$ gives $$2(2^s-1)+d\bigl((2^s-s-1)+(2^s-1)\bigr)
 =
 2(2^s-1)+d(2^{s+1}-s-2),$$ which is [\[eq:M-crude\]](#eq:M-crude){reference-type="eqref" reference="eq:M-crude"}. This reconstruction keeps the graph labels, spread roots, and constant-plus-monomial roots visibly separate.

## Redundancy and dependency check {#redundancy-and-dependency-check .unnumbered}

The main proofs remain complete if all three appendices are removed. Lemma [\[lem:sparse-image\]](#lem:sparse-image){reference-type="ref" reference="lem:sparse-image"} proves its rank, power-fiber, degenerate-subset, and torsion claims in Section [4](#sec:sparse){reference-type="ref" reference="sec:sparse"}. Theorem [\[thm:pc1\]](#thm:pc1){reference-type="ref" reference="thm:pc1"} proves all four incidence types, their endpoint graph choices, root degrees, vertical closure, simultaneous-label convention, and both checksums in Section [5](#sec:pc1proof){reference-type="ref" reference="sec:pc1proof"}. Theorem [\[thm:pc3\]](#thm:pc3){reference-type="ref" reference="thm:pc3"} derives all nine adjacent words and both continuation ledgers in Section [7](#sec:supportone){reference-type="ref" reference="sec:supportone"}. The appendices provide alternate reading orders and arithmetic checks only.

The audit also shows that no coefficient-membership statement is hidden in notation. Whenever a relation is written with $au$, $av$, or a coefficient multiple of a power, the genuine group variable remains $u,v$, or the power base. The coefficient is fixed in $K^*$. Every invocation of Theorem [\[thm:av\]](#thm:av){reference-type="ref" reference="thm:av"} uses a group that is explicitly a homomorphic image of a Cartesian power of $\Gamma$, and every invocation of Lemma [\[lem:sparse-image\]](#lem:sparse-image){reference-type="ref" reference="lem:sparse-image"} uses input and output variables in $\Gamma$.

There are two different uses of algebraic closure. The external theorem requires it, and elementary polynomial root counts may be taken there for convenience. Both uses enlarge the ambient solution set. Neither creates a solution claimed to belong to $K$, and neither changes the rank of the embedded source group. All final survivor sets are still defined over the original $K$.

The constants can be reconstructed from the proof dependencies. A $q$-term sparse graph contributes $d\mathcal A(q,2r)$ on its nondegenerate locus and at most $d$ roots for each of $2^q-q-2$ degenerate subsets. A general-support local equation contributes $d\mathcal A(s+2,3r)$. Its graph labels number $2(2^s-1)$, while its two root families contribute the defining subset sums. A support-one window has four local indices and $3^4$ degenerate words. These reconstructions give exactly [\[eq:S\]](#eq:S){reference-type="eqref" reference="eq:S"}, [\[eq:pc1-bound\]](#eq:pc1-bound){reference-type="eqref" reference="eq:pc1-bound"}, and [\[eq:pc3-bound\]](#eq:pc3-bound){reference-type="eqref" reference="eq:pc3-bound"}.

# Support-one continuation ledger {#app:support-one-ledger}

Starting with $A_i$ gives $u=\alpha$, $x_{i+1}=bv^d$, and the next labels give $$v=\alpha,\qquad b^{d+1}v^{d^2}=-c,\qquad
 b^{d+1}v^{d^2}=-av.$$ Starting with $B_i$ gives $bv^d=-c$, $x_{i+1}=au$, and $$v=\alpha,\qquad ba^du^d=-c,\qquad ba^du^d=-av.$$ Only $BA$ leaves $u$ free. Its chain $t,\alpha,at,ba^dt^d$ gives $$at=\alpha,\qquad b^{d+1}a^{d^2}t^{d^2}=-c,\qquad
 b^{d+1}a^{d^2}t^{d^2}=-a^2t.$$

Starting with $C_i$ gives $u=-bv^d/a$, $x_{i+1}=c$, and $$v=\alpha,\qquad bc^d=-c,\qquad bc^d=-av.$$ Only $CB$ leaves $v$ free. Under $bc^{d-1}=-1$, its next labels give $$c=\alpha,\qquad ba^dt^d=-c,\qquad ba^dt^d=-ac.$$ Only the first can remain free, exactly when $a=-1$. The fourth labels impose $$-t=c,\qquad b^{d+1}(-t)^{d^2}=-c,\qquad
 b^{d+1}(-t)^{d^2}=-t.$$ Thus $CBA$ alone is free at length three and no word is free at length four. The $3^4$ word union gives $81d^2$, while simultaneous labels merely overcount.

The nine adjacent substitutions use only the label identities [\[eq:A-label\]](#eq:A-label){reference-type="eqref" reference="eq:A-label"}--[\[eq:C-label\]](#eq:C-label){reference-type="eqref" reference="eq:C-label"}; no genericity assumption enters. If a listed compatibility fails, the corresponding word locus is empty and its stated upper bound remains valid. If it holds, the next displayed polynomial controls the free parameter. The largest possible degree is $d^2$, coming from applying a $d$-th power to a coordinate already proportional to a $d$-th power.

The union count treats each word as a necessary-condition locus. It is unnecessary to solve the labels simultaneously or prove that different words are disjoint. This is the support-one analogue of the simultaneous-subsums convention in Section [5](#sec:pc1proof){reference-type="ref" reference="sec:pc1proof"}.
