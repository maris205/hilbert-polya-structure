---
p1_kind: "derived-fulltext-reading-copy"
route: "symplectic_map"
logical_paper_id: "symplectic_map--14-henon-four-step-torus-escape"
canonical_tex: "symplectic_map/papers/14-henon-four-step-torus-escape/paper/main.tex"
canonical_pdf: "symplectic_map/papers/14-henon-four-step-torus-escape/paper/main.pdf"
source_sha256: "415f1395f07153ccb158e69cb70051e95e719802d0a1c3315df88be7ccfab538"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Four-Step Escape from Finite-Rank Tori for Monomial Henon Maps

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symplectic_map/papers/14-henon-four-step-torus-escape>)
- [规范 TeX](<../../../../../symplectic_map/papers/14-henon-four-step-torus-escape/paper/main.tex>)
- [关联 PDF](<../../../../../symplectic_map/papers/14-henon-four-step-torus-escape/paper/main.pdf>)
- [支撑 Markdown](<../../../../../symplectic_map/papers/14-henon-four-step-torus-escape/notes/CLAIMS_EVIDENCE_MATRIX.md>)
- [BibTeX](<../../../../../symplectic_map/papers/14-henon-four-step-torus-escape/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We study finite windows of the monomial Henon automorphism $H(x,y)=(b x^d+a y+c,x)$ whose coordinates remain in the square of a finite-rank multiplicative subgroup. Over every characteristic-zero field, for arbitrary nonzero coefficients and a subgroup of rank $r$, we prove $$\#T_4(H,\Gamma)
   \le 4d\exp\!\bigl(18^9(3r+1)\bigr)+81d^2.$$ Crucially, the estimate requires neither finite generation nor coefficient membership in the subgroup; all coefficients remain fixed in the unit equation throughout. Here $T_4$ contains five states and four transitions. The proof separates a nondegenerate fixed-coefficient unit equation from a complete symbolic analysis of its degenerate locus; the latter reduces to three labels, nine adjacent transitions, and the closure of the two free chains. We also give, for every $d\ge2$, a number-field example in a rank-one group for which $T_3$ is infinite, so the transition threshold is sharp. As a consequence, the same explicit expression bounds the weighted number of exact-period orbits whose entire orbit lies in the subgroup square.
author:
- Anonymous
bibliography:
- references.bib
title: 'Four-Step Escape from Finite-Rank Tori for Monomial Henon Maps'
```

## Markdown 正文

# Introduction and main results {#sec:introduction}

Let $K$ be a field and let $\Gamma\le K^\ast$ be a multiplicative subgroup. A polynomial automorphism need not preserve $\Gamma^2$, because membership in $\Gamma$ gives multiplicative closure but no additive closure. This paper asks a finite-window question instead: how many initial states have several consecutive states in $\Gamma^2$? The finite window allows a unit-equation argument, but only after all vanishing proper subsums have been controlled.

The finite-window formulation separates two quantifiers that are easily conflated. A return-time problem begins with one prescribed initial point and asks when its orbit meets a subgroup. Here the time interval is fixed, while the initial point ranges over all of $\Gamma^2$. Uniformity in the initial state is the source of the counting problem. It also explains why the answer can depend only on the degree and the rank even though the coefficients themselves are unrestricted nonzero elements of $K$.

Fix an integer $d\ge2$ and nonzero elements $a,b,c\in K$. We consider the monomial Henon map $$\label{eq:map}
 H(x,y)=(b x^d+a y+c,x).$$ Since $a\ne0$, this map is a polynomial automorphism. For $m\ge0$, define $$\label{eq:Tm}
 T_m(H,\Gamma)
 =
 \bigl\{P\in\Gamma^2:
 H^j(P)\in\Gamma^2\ \text{for every}\ 0\le j\le m\bigr\}.$$ Thus $T_m$ describes $m$ transitions and $m+1$ states. In particular, $T_4$ contains $$P,\ H(P),\ H^2(P),\ H^3(P),\ H^4(P),$$ not four states.

To see the arithmetic structure behind this definition, write these five states as $(x_j,x_{j-1})$. Membership in $T_4$ puts every coordinate $x_{-1},x_0,\ldots,x_4$ in $\Gamma$, and the four transitions give four three-term recurrence equations. At a nondegenerate equation, a finite-rank unit-equation theorem supplies a uniform count. At a degenerate equation, one proper subsum vanishes and can leave a free parameter. The length of a free degenerate chain, rather than the number of displayed states alone, determines the transition threshold.

Our principal result is uniform in the base field and all three coefficients.

[\[thm:four-step\]]{#thm:four-step label="thm:four-step"} Let $K$ be a field of characteristic zero, let $d\ge2$, let $a,b,c\in K^\ast$, and let $\Gamma\le K^\ast$ be a multiplicative subgroup of finite rank $r$. For the map [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"}, $$\label{eq:main-bound}
 \#T_4(H,\Gamma)
 \le
 4d\exp\!\bigl(18^9(3r+1)\bigr)+81d^2.$$

Finite rank in Theorem [\[thm:four-step\]](#thm:four-step){reference-type="ref" reference="thm:four-step"} does not mean finite generation: one may define the rank as $\dim_{\mathbb Q}(\Gamma\otimes_{\mathbb Z}\mathbb Q)$. There is also no assumption that $a,b,c$, or $-1$ belongs to $\Gamma$. The coefficients remain fixed coefficients in the unit equation; they are never absorbed into the variable group. The two summands in [\[eq:main-bound\]](#eq:main-bound){reference-type="eqref" reference="eq:main-bound"} are explicit rather than optimized: the first comes from the published unit-equation bound, and the second is a union bound over degeneracy words.

The four-transition threshold cannot be shortened uniformly.

[\[thm:three-step\]]{#thm:three-step label="thm:three-step"} For every integer $d\ge2$, there exist a number field $K$, nonzero coefficients $a,b,c\in K$, and a subgroup $\Gamma\le K^\ast$ of rank one such that $$\#T_3(H,\Gamma)=\infty.$$

The word sharpness in Theorem [\[thm:three-step\]](#thm:three-step){reference-type="ref" reference="thm:three-step"} refers only to the number of transitions. It does not assert that either summand in [\[eq:main-bound\]](#eq:main-bound){reference-type="eqref" reference="eq:main-bound"} is numerically optimal, nor does it classify all coefficient choices for which $T_3$ is infinite.

There is a direct periodic consequence, provided that containment is imposed on the whole orbit. Let $C_n^\Gamma(H)$ be the number of exact-period $n$ orbits $\mathcal O$ satisfying $\mathcal O\subseteq\Gamma^2$.

[\[cor:periodic\]]{#cor:periodic label="cor:periodic"} Under the hypotheses of Theorem [\[thm:four-step\]](#thm:four-step){reference-type="ref" reference="thm:four-step"}, $$\label{eq:periodic-bound}
 \sum_{n\ge1}n\,C_n^\Gamma(H)
 \le
 4d\exp\!\bigl(18^9(3r+1)\bigr)+81d^2.$$

The proof proceeds through seven steps, each of which remains visible in the main text.

1.  We index the scalar recurrence and record the polynomial inverse of $H$, so that a local-state count pulls back injectively to initial states.

2.  We normalize a local recurrence as a three-variable unit equation with variables in $\Gamma^3$ and arbitrary fixed coefficients.

3.  We combine the unit-equation bound, a $d$-th-root fiber count, and a four-index union bound for every point having a nondegenerate local equation.

4.  We show that every degenerate local equation has at least one of the labels $A,B,C$, obtained from the three possible vanishing two-term subsums.

5.  We derive all nine adjacent transitions. Only $BA$ and $CB$ can retain a free parameter; $BA$ closes after one more letter, and the exceptional continuation $CBA$ closes after the fourth letter.

6.  We cover simultaneous labels by choosing any valid label at each index and sum the $3^4$ per-word estimates, including a separate check that short periodic orbits introduce no new cases.

7.  We realize the free $CBA$ chain through three transitions in a rank-one number-field group and then inject every wholly contained periodic orbit into $T_4(H,\Gamma)$.

The first six steps prove Theorem [\[thm:four-step\]](#thm:four-step){reference-type="ref" reference="thm:four-step"}; the last step proves Theorem [\[thm:three-step\]](#thm:three-step){reference-type="ref" reference="thm:three-step"} and Corollary [\[cor:periodic\]](#cor:periodic){reference-type="ref" reference="cor:periodic"}. The appendices repeat the transition and closure algebra in audit-table form, but no implication needed for these three statements is deferred there.

# Arithmetic-dynamical context {#sec:context}

The proof imports one external theorem, while the remaining citations delimit the orbit and map regimes surrounding the result.

#### Finite-rank unit equations.

Evertse, Schlickewei, and Schmidt prove an explicit uniform bound for nondegenerate solutions of a linear equation in a finite-rank multiplicative group [@ESS2002 Theorem 1.1]. Their theorem allows arbitrary fixed nonzero coefficients. We apply it to a rank-$3r$ subgroup of $(K^\ast)^3$; the factor $4d$, the degeneracy analysis, and the sharpness construction are dynamical arguments developed below. One-dimensional image and orbit questions for $S$-units have a different shape [@KLSTYZ2015 Theorems 1.7--1.8]. Multiplicative dependence among consecutive univariate iterates, and finiteness for two distinct iterates under squarefreeness hypotheses, are treated in [@OSSZ2017 Corollary 4.9 and Theorem 4.11]. Neither condition is coordinatewise survival of all states in a two-dimensional window.

#### Fixed-orbit subgroup intersections.

Bell and Ghioca treat the return times of one fixed orbit of a rational self-map of a semiabelian variety to a finitely generated subgroup [@BG2024 Theorem 1.1]. Their Theorem 1.1(i) gives a finite union of arithmetic progressions together with a Banach-density-zero residual set. Under the regular-self-map hypothesis, part (ii) makes only the residual set finite; it does not make the whole return-time set finite. Moreover, the restriction of [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"} to $\mathbb{G}_{m}^2$ is generally rational rather than regular, since $b x^d+a y+c$ can vanish. These fixed-orbit statements do not count all initial states in a prescribed finite window.

#### Higher-dimensional and Henon boundaries.

Canonical-height theory for Henon maps addresses arithmetic height growth, not finite-rank finite-window survival [@Ingram2014]. Integral-point non-density in one fixed projective orbit under regularity and divisor hypotheses is likewise qualitative and has a different ambient setting [@GN2024 Theorem 1.2 and Corollary 1.5]; in particular, a Henon map does not extend to a regular self-map of $\mathbb P^2$.

Kim, Krieger, Postolache, and Szeto provide complementary abundance results for general-polynomial Henon maps [@KKPS2024 Theorems A--B]. Their Theorem A, for odd $d>2$, constructs a rational polynomial $s_d$ of degree at most $d$ for which $$h_d(x,y)=(y,-x+s_d(y))$$ has at least $(d-4)^2$ rational periodic points. Their Theorem B, for $d\equiv1\pmod6$, gives an integer cycle of length $(8d+10)/3$. This family is not restricted to a monomial plus a constant, and those degree-dependent lower bounds do not conflict with Theorem [\[thm:four-step\]](#thm:four-step){reference-type="ref" reference="thm:four-step"}.

Finally, Mello and Yasufuku study projective endomorphism semigroups over number fields and finitely generated subgroups [@MY2026 Theorems 1.1--1.2, Corollary 1.3, and Theorem 4.2]. Their main results are conditional on $\mathrm{Hyp}_\epsilon$ and require $\epsilon\ge(1+c_{\mathrm{MY}})/2$, where $c_{\mathrm{MY}}$ is their auxiliary constant, not the coefficient $c$ in [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"}. Under additional divisor hypotheses and Vojta's Main Conjecture, Theorem 4.2 supplies the relevant non-density only for sufficiently small $\epsilon$. It therefore does not verify the general hypothesis used by their main theorems. This conditional projective-semigroup result is distinct from the unconditional finite-window statement proved here.

These comparisons separate fixed-orbit return-time structure, general-polynomial periodic-point abundance, and conditional projective semigroup results from the all-initial-state finite-window question. They are scope comparisons and make no priority assertion.

# The nondegenerate contribution {#sec:nondegenerate}

Throughout the proof of Theorem [\[thm:four-step\]](#thm:four-step){reference-type="ref" reference="thm:four-step"}, write $$\label{eq:coordinates}
 P=(x_0,x_{-1}),\qquad H^j(P)=(x_j,x_{j-1}).$$ Equation [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"} becomes $$\label{eq:recurrence}
 x_{i+1}=b x_i^d+a x_{i-1}+c.$$ For $P\in T_4(H,\Gamma)$, the recurrence is available at precisely the four local indices $i=0,1,2,3$.

## Local states and pullback to the initial state

The change from a scalar recurrence to a two-dimensional automorphism is what allows a local count at any of the four indices to control the same set of initial points.

[\[lem:local-pullback\]]{#lem:local-pullback label="lem:local-pullback"} The inverse of $H$ is $$\label{eq:inverse}
 H^{-1}(X,Y)
 =
 \left(Y,\frac{X-bY^d-c}{a}\right).$$ Consequently, for every integer $i$, the map $$P\longmapsto H^i(P)=(x_i,x_{i-1})$$ is injective. A bound for the number of ordered local pairs $(x_i,x_{i-1})$ therefore gives the same bound for the corresponding initial states.

Substitution of [\[eq:inverse\]](#eq:inverse){reference-type="eqref" reference="eq:inverse"} into [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"}, in either order, returns the original pair. Division by $a$ is valid because $a\ne0$. Thus $H$ is an automorphism and so is every iterate $H^i$. If two initial points have the same pair $(x_i,x_{i-1})$, applying $H^{-i}$ to that pair gives the same initial point. This proves injectivity.

The pair used in the degeneracy calculations below is often written in the order $(x_{i-1},x_i)$. Swapping the two entries is a bijection, so this notational order does not change any count.

## Finite rank and the variable group

Only the variables, not the coefficients of a unit equation, contribute to the rank in the unit-equation theorem. We record the elementary rank calculation explicitly.

[\[lem:product-rank\]]{#lem:product-rank label="lem:product-rank"} Let $\Gamma$ be an abelian group of finite rank $r$. For every positive integer $q$, $$\operatorname{rank}(\Gamma^q)=qr.$$ In particular, if $x_{i-1},x_i,x_{i+1}\in\Gamma$, then $$(x_{i+1},x_i^d,x_{i-1})\in\Gamma^3,
 \qquad
 \operatorname{rank}(\Gamma^3)=3r.$$

For a finite direct product, tensoring with $\mathbb Q$ gives $$(\Gamma^q)\otimes_{\mathbb Z}\mathbb Q
 \cong
 \bigl(\Gamma\otimes_{\mathbb Z}\mathbb Q\bigr)^q.$$ The right side is a direct product of $q$ finite-dimensional $\mathbb Q$-vector spaces, each of dimension $r$, and hence has dimension $qr$. This calculation kills torsion automatically and does not require $\Gamma$ to be finitely generated. Since $\Gamma$ is a multiplicative group, $x_i^d\in\Gamma$; the asserted triple and the case $q=3$ follow.

## Fixed-coefficient specialization of the unit equation

We recall the sole external theorem used in the proof.

[\[thm:ess\]]{#thm:ess label="thm:ess"} Let $F$ be a field of characteristic zero. Let $G\le(F^\ast)^n$ have finite rank $R$, and fix $\lambda_1,\ldots,\lambda_n\in F^\ast$. The number of solutions $$(y_1,\ldots,y_n)\in G,\qquad
 \lambda_1y_1+\cdots+\lambda_ny_n=1,$$ for which no nonempty proper subsum on the left vanishes is at most $$\exp\!\bigl((6n)^{3n}(R+1)\bigr).$$

This is the published Theorem 1.1 of [@ESS2002]. Such a solution will be called nondegenerate. At every local index, divide [\[eq:recurrence\]](#eq:recurrence){reference-type="eqref" reference="eq:recurrence"} by $c$ and rearrange: $$\label{eq:unit}
 \frac1c x_{i+1}
 -\frac bc x_i^d
 -\frac ac x_{i-1}
 =1.$$ Set $$\label{eq:variables}
 Y_i=(x_{i+1},x_i^d,x_{i-1}).$$ For $P\in T_4(H,\Gamma)$, Lemma [\[lem:product-rank\]](#lem:product-rank){reference-type="ref" reference="lem:product-rank"} places $Y_i$ in the rank-$3r$ group $\Gamma^3$.

[\[lem:ess-specialization\]]{#lem:ess-specialization label="lem:ess-specialization"} At a specified index $i\in\{0,1,2,3\}$, the number of nondegenerate triples $Y_i$ arising from points of $T_4(H,\Gamma)$ is at most $$\label{eq:E}
 \mathcal{E}_{r}=E(3,3r)
 =
 \exp\!\bigl(18^9(3r+1)\bigr).$$ No membership condition on $a,b,c$ in $\Gamma$ is used.

Apply Theorem [\[thm:ess\]](#thm:ess){reference-type="ref" reference="thm:ess"} with $$F=K,\qquad G=\Gamma^3,\qquad n=3,\qquad R=3r$$ and with fixed coefficients $$\lambda_1=\frac1c,\qquad
 \lambda_2=-\frac bc,\qquad
 \lambda_3=-\frac ac.$$ All three coefficients lie in $K^\ast$ because $a,b,c\ne0$. The theorem does not require them to lie in $G$, and they are not coordinates of the variable triple. The set of triples that actually arise from $T_4(H,\Gamma)$ is a subset of the solutions in $G$, so the same upper bound applies. Finally, $$(6\cdot3)^{3\cdot3}=18^9,$$ which gives [\[eq:E\]](#eq:E){reference-type="eqref" reference="eq:E"}.

The distinction between variables and coefficients is essential. Replacing $Y_i$ by a coefficient-normalized triple would generally move the variables outside $\Gamma^3$ and would introduce a coefficient-dependent rank. Equation [\[eq:unit\]](#eq:unit){reference-type="eqref" reference="eq:unit"} avoids that operation entirely.

## Fibers over an ESS triple

An ESS solution counts a triple, whereas the dynamical object is an initial state. The next lemma accounts for the difference.

[\[lem:d-lift\]]{#lem:d-lift label="lem:d-lift"} Fix $i\in\{0,1,2,3\}$ and a triple $$(z,w,u)=(x_{i+1},x_i^d,x_{i-1})$$ arising from $T_4(H,\Gamma)$. At most $d$ initial states produce this triple.

The triple fixes $x_{i+1}=z$, $x_{i-1}=u$, and $x_i^d=w$. Every possible middle coordinate $x_i$ is a root in $K$ of $$X^d-w.$$ This is a nonzero polynomial of degree $d$, so it has at most $d$ roots in $K$. Each root fixes the local pair $(x_i,x_{i-1})=(x_i,u)$. Lemma [\[lem:local-pullback\]](#lem:local-pullback){reference-type="ref" reference="lem:local-pullback"} shows that at most one initial point pulls back from each such local pair. Some roots may fail to lie in $\Gamma$ or fail another window condition, but discarding them only lowers the count.

Combining Lemmas [\[lem:ess-specialization\]](#lem:ess-specialization){reference-type="ref" reference="lem:ess-specialization"} and [\[lem:d-lift\]](#lem:d-lift){reference-type="ref" reference="lem:d-lift"}, a fixed nondegenerate index accounts for at most $d\mathcal{E}_{r}$ initial states.

## Partition and the four-index union

For $i=0,1,2,3$, let $N_i$ denote the set of points in $T_4(H,\Gamma)$ for which [\[eq:unit\]](#eq:unit){reference-type="eqref" reference="eq:unit"} is nondegenerate at index $i$. Let $D$ denote the set for which all four indexed equations are degenerate.

[\[prop:nondegenerate\]]{#prop:nondegenerate label="prop:nondegenerate"} One has the exhaustive decomposition $$\label{eq:partition}
 T_4(H,\Gamma)=D\cup N_0\cup N_1\cup N_2\cup N_3.$$ Moreover, $$\#(N_0\cup N_1\cup N_2\cup N_3)\le4d\mathcal{E}_{r}.$$

For any point of $T_4(H,\Gamma)$, either at least one of the four local equations is nondegenerate or none is. The latter condition is exactly membership in $D$, so [\[eq:partition\]](#eq:partition){reference-type="eqref" reference="eq:partition"} is exhaustive. The class $D$ is disjoint from every $N_i$, but the four sets $N_i$ need not be pairwise disjoint. At a fixed index, Lemmas [\[lem:ess-specialization\]](#lem:ess-specialization){reference-type="ref" reference="lem:ess-specialization"} and [\[lem:d-lift\]](#lem:d-lift){reference-type="ref" reference="lem:d-lift"} give $\#N_i\le d\mathcal{E}_{r}$. Therefore the union bound gives $$\#(N_0\cup N_1\cup N_2\cup N_3)
 \le\sum_{i=0}^3\#N_i
 \le4d\mathcal{E}_{r}.$$ No choice of a preferred nondegenerate index is required.

It remains to bound $D$, the class in which all four local equations are degenerate.

# The degenerate locus {#sec:degenerate}

The nondegenerate estimate leaves a symbolic problem: classify every way in which four consecutive equations [\[eq:unit\]](#eq:unit){reference-type="eqref" reference="eq:unit"} can have a vanishing proper subsum. We first derive the local labels, then the nine adjacent transitions, and finally the two longer free chains.

## Proper subsums and the three labels

For one local equation, put $$\label{eq:L}
 L_1=\frac{x_{i+1}}c,\qquad
 L_2=-\frac{b x_i^d}c,\qquad
 L_3=-\frac{a x_{i-1}}c.$$ All three terms are nonzero, and $L_1+L_2+L_3=1$. The nonempty proper subsets of $\{1,2,3\}$ are the three singletons and the three pairs. A singleton cannot sum to zero because every $L_j\ne0$. Consequently a degenerate solution has a vanishing two-term subsum.

The three pairs give the following labels: $$\label{eq:labels}
\begin{aligned}
 A_i&:\quad a x_{i-1}+c=0,
 &x_{i-1}&=-\frac ca,
 &x_{i+1}&=b x_i^d,\\
 B_i&:\quad b x_i^d+c=0,
 &b x_i^d&=-c,
 &x_{i+1}&=a x_{i-1},\\
 C_i&:\quad b x_i^d+a x_{i-1}=0,
 &b x_i^d&=-a x_{i-1},
 &x_{i+1}&=c.
\end{aligned}$$ Indeed, $L_1+L_2=0$ first gives $x_{i+1}=b x_i^d$; substituting into [\[eq:recurrence\]](#eq:recurrence){reference-type="eqref" reference="eq:recurrence"} gives $a x_{i-1}+c=0$, which is $A_i$. For the second pair, $L_1+L_3=0$ gives $x_{i+1}=a x_{i-1}$, and the recurrence then gives $b x_i^d+c=0$, which is $B_i$. Finally, $L_2+L_3=0$ is the first equation in $C_i$, and the recurrence gives $x_{i+1}=c$. Each calculation is reversible, so the labels are equivalent to the three vanishing pairs and exhaust local degeneracy.

A local equation may carry two labels, a point addressed in Section [4.6](#subsec:simultaneous){reference-type="ref" reference="subsec:simultaneous"}. For now, a word records one chosen label at each consecutive local index: its first letter labels index $i$, its second labels $i+1$, and so on. This direction convention is fixed. Put $$u=x_{i-1},\qquad v=x_i,\qquad z=x_{i+1},\qquad
 \alpha=-\frac ca.$$

## All nine adjacent transitions

[\[lem:nine\]]{#lem:nine label="lem:nine"} For two consecutive degenerate equations, the constraints on the initial local state $(u,v)$ are as follows.

   word  constraint                                                bound
  ------ ------------------------------------------------------- ---------
   $AA$  $u=\alpha,\ v=\alpha$                                      $1$
   $AB$  $u=\alpha,\ b^{d+1}v^{d^2}=-c$                            $d^2$
   $AC$  $u=\alpha,\ b^{d+1}v^{d^2}=-av$                          $d^2-1$
   $BA$  $v=\alpha,\ b\alpha^d=-c$; if compatible, $u$ is free     free
   $BB$  $v^d=-c/b,\ u^d=-c/(ba^d)$                                $d^2$
   $BC$  $v^d=-c/b,\ u^d=-v/(ba^{d-1})$                            $d^2$
   $CA$  $v=\alpha,\ u=-b\alpha^d/a$                                $1$
   $CB$  $bc^d=-c,\ u=-bv^d/a$; if compatible, $v$ is free         free
   $CC$  $v=-bc^d/a,\ u=-bv^d/a$                                    $1$

Every finite entry has at most $d^2$ local states. The only adjacent words that can carry a free parameter are $BA$ and $CB$.

We derive the nine rows in the fixed index direction.

Suppose first that $A_i$ holds. Then $u=\alpha$ and $z=bv^d$. For $AA$, the equation $A_{i+1}$ is $av+c=0$, hence $v=\alpha$; both coordinates are fixed. For $AB$, the equation $B_{i+1}$ is $$bz^d+c=0
 \quad\Longleftrightarrow\quad
 b^{d+1}v^{d^2}=-c.$$ This is a nonzero polynomial equation of degree $d^2$ in $v$, while $u=\alpha$. For $AC$, the equation $C_{i+1}$ is $$bz^d+av=0
 \quad\Longleftrightarrow\quad
 b^{d+1}v^{d^2}=-av.$$ Since $v\in\Gamma\subset K^\ast$, division by $v$ gives $$b^{d+1}v^{d^2-1}=-a.$$ The leading and constant coefficients are nonzero, so this equation has at most $d^2-1$ roots.

Suppose next that $B_i$ holds. Then $$bv^d=-c,\qquad z=au.$$ For $BA$, the next $A$-condition is $av+c=0$, or $v=\alpha$. It is compatible with the first displayed equation precisely when $$b\alpha^d=-c.$$ When this coefficient relation holds, neither local equation has imposed an equation on $u$, so $u$ remains free. For $BB$, the next condition is $$b(au)^d=-c.$$ Thus $v^d=-c/b$ and $u^d=-c/(ba^d)$; each equation has at most $d$ roots, giving at most $d^2$ pairs. For $BC$, the next condition is $$b(au)^d+av=0,$$ and division by the nonzero coefficient $a$ gives $$u^d=-\frac{v}{ba^{d-1}}.$$ There are at most $d$ choices for $v$, and for each one at most $d$ choices for $u$.

Finally suppose that $C_i$ holds. Then $$u=-\frac ba v^d,\qquad z=c.$$ For $CA$, the next condition $av+c=0$ fixes $v=\alpha$ and then fixes $u=-b\alpha^d/a$. For $CB$, the next condition is $$bc^d+c=0,$$ which is independent of $v$. If it fails, there are no states. If it holds, equivalently if $bc^{d-1}=-1$, then $v$ remains free and $u$ is determined by $v$. For $CC$, the next condition is $$bc^d+av=0,$$ so $v=-bc^d/a$ and then $u=-bv^d/a$.

A nonzero polynomial of degree $e$ over $K$ has at most $e$ roots in $K$; imposing membership in $\Gamma$ can only reduce this number. The row-by-row counts therefore prove the table and identify $BA,CB$ as the only free adjacent words.

## Closure of the $BA$ branch

[\[lem:BA\]]{#lem:BA label="lem:BA"} Every three-letter word beginning with $BA$ has at most $d^2$ initial states.

The branch exists only if $$\label{eq:BA-compat}
 b\alpha^d=-c.$$ Let $t=x_{i-1}$. The condition $B_i$ gives $x_{i+1}=a x_{i-1}=at$, while $A_{i+1}$ fixes $x_i=\alpha$ and gives $x_{i+2}=b x_{i+1}^d$. Hence $$\label{eq:BA-coordinates}
 x_{i-1}=t,\quad x_i=\alpha,\quad
 x_{i+1}=at,\quad x_{i+2}=ba^dt^d.$$ The compatibility [\[eq:BA-compat\]](#eq:BA-compat){reference-type="eqref" reference="eq:BA-compat"} is exactly the remaining $B_i$ equation $b x_i^d=-c$.

At index $i+2$, label $A$ requires $$a x_{i+1}+c=a^2t+c=0,$$ equivalently $at=\alpha$, so $BAA$ has at most one state. Label $B$ requires $$b x_{i+2}^d=-c
 \quad\Longleftrightarrow\quad
 b^{d+1}a^{d^2}t^{d^2}=-c,$$ a degree-$d^2$ equation. Label $C$ requires $$b x_{i+2}^d=-a x_{i+1}
 \quad\Longleftrightarrow\quad
 b^{d+1}a^{d^2}t^{d^2}=-a^2t.$$ Here $t=x_{i-1}\in\Gamma$, so $t\ne0$. Dividing by $t$ gives the nonzero degree-$d^2-1$ equation $$b^{d+1}a^{d^2}t^{d^2-1}=-a^2.$$ Thus $$\label{eq:BA-close}
\begin{array}{c|c|c}
 \text{word}&\text{equation for }t&\text{bound}\\ \hline
 BAA&at=\alpha&1\\
 BAB&b^{d+1}a^{d^2}t^{d^2}=-c&d^2\\
 BAC&b^{d+1}a^{d^2}t^{d^2}=-a^2t&d^2-1.
\end{array}$$ A fourth label intersects one of these realization sets and cannot increase its cardinality.

## The $CB$ branch and exceptional $CBA$ continuation

[\[lem:CB\]]{#lem:CB label="lem:CB"} The $CBB$ and $CBC$ branches have at most $d$ initial states. The branch $CBA$ can remain free only when $$\label{eq:CBA-exception}
 a=-1,\qquad bc^{d-1}=-1,$$ and each of its four-letter extensions has at most $d^2$ initial states.

The $CB$ compatibility from Lemma [\[lem:nine\]](#lem:nine){reference-type="ref" reference="lem:nine"} is $$\label{eq:CB-compat}
 bc^d=-c,\qquad\text{or equivalently}\qquad bc^{d-1}=-1,$$ where division by $c\ne0$ is valid. Set $t=x_i$. The condition $C_i$ gives $x_{i-1}=-bt^d/a$ and $x_{i+1}=c$. Under $B_{i+1}$, the next coordinate is $x_{i+2}=a x_i=at$. Thus $$\label{eq:CB-coordinates}
 x_{i-1}=-\frac ba t^d,\quad x_i=t,\quad
 x_{i+1}=c,\quad x_{i+2}=at.$$

At index $i+2$, label $B$ gives $$b(at)^d=-c,$$ and label $C$ gives $$b(at)^d=-ac.$$ Each is a nonzero degree-$d$ equation in $t$. Label $A$ instead gives $$ac+c=0.$$ Since $c\ne0$, this last condition is equivalent to $a=-1$ and imposes no equation on $t$. Therefore $$\label{eq:CB-third}
\begin{array}{c|c|c}
 \text{word}&\text{condition}&\text{bound}\\ \hline
 CBB&ba^dt^d=-c&d\\
 CBC&ba^dt^d=-ac&d\\
 CBA&c=-c/a&\text{free only if }a=-1.
\end{array}$$

Under [\[eq:CBA-exception\]](#eq:CBA-exception){reference-type="eqref" reference="eq:CBA-exception"}, formula [\[eq:CB-coordinates\]](#eq:CB-coordinates){reference-type="eqref" reference="eq:CB-coordinates"} becomes $$\label{eq:CBA-coordinates}
 x_{i-1}=bt^d,\quad x_i=t,\quad x_{i+1}=c,\quad
 x_{i+2}=-t,\quad x_{i+3}=b(-t)^d.$$ At index $i+3$, label $A$ requires $a x_{i+2}+c=t+c=0$, or $-t=c$. Label $B$ requires $$b\bigl(b(-t)^d\bigr)^d=-c,$$ and label $C$ requires $$b\bigl(b(-t)^d\bigr)^d=-a x_{i+2}=-t.$$ Hence $$\label{eq:CBA-close}
\begin{array}{c|c|c}
 \text{word}&\text{equation for }t&\text{bound}\\ \hline
 CBAA&-t=c&1\\
 CBAB&b^{d+1}(-t)^{d^2}=-c&d^2\\
 CBAC&b^{d+1}(-t)^{d^2}=-t&d^2-1.
\end{array}$$ For $CBAC$, the parameter $t=x_i$ belongs to $\Gamma$ and is nonzero. After division by $t$, the equation is a nonzero polynomial equation of degree $d^2-1$. This closes the only free three-letter branch at the fourth letter.

## The per-word trichotomy

For a word $w=w_0w_1w_2w_3\in\{A,B,C\}^4$, let $\mathcal R(w)$ be the set of points $P\in T_4(H,\Gamma)$ for which the chosen label $w_j$ holds at index $j$. This definition does not require the label at an index to be unique.

[\[lem:per-word\]]{#lem:per-word label="lem:per-word"} For every $w\in\{A,B,C\}^4$, $$\#\mathcal R(w)\le d^2.$$

There are three exhaustive cases.

If the first two letters are neither $BA$ nor $CB$, Lemma [\[lem:nine\]](#lem:nine){reference-type="ref" reference="lem:nine"} gives at most $d^2$ choices for $(x_{-1},x_0)$. The third and fourth labels impose further equations and therefore select a subset of those choices.

If the word begins with $BA$, Lemma [\[lem:BA\]](#lem:BA){reference-type="ref" reference="lem:BA"} bounds every possible third-letter extension by $d^2$. Again, the fourth label only selects a subset.

If the word begins with $CB$, its third letter is $B,C$, or $A$. The prefixes $CBB$ and $CBC$ have at most $d\le d^2$ states by Lemma [\[lem:CB\]](#lem:CB){reference-type="ref" reference="lem:CB"}. A $CBA$ prefix is empty unless the two exceptional coefficient relations hold; when they do hold, its three fourth-letter extensions are bounded by [\[eq:CBA-close\]](#eq:CBA-close){reference-type="eqref" reference="eq:CBA-close"}.

These cases exhaust the first two letters and every later extension. At index $0$, the local pair is $(x_{-1},x_0)$, which is in bijection with the initial state $P=(x_0,x_{-1})$. More generally, the same conclusion at another fixed index follows from Lemma [\[lem:local-pullback\]](#lem:local-pullback){reference-type="ref" reference="lem:local-pullback"}. Thus the local root counts are initial-state counts.

## Simultaneous labels and the word cover {#subsec:simultaneous}

A degenerate local equation can satisfy two labels. In terms of [\[eq:L\]](#eq:L){reference-type="eqref" reference="eq:L"}, the pairwise intersections are $$\label{eq:overlaps}
\begin{aligned}
 A\cap B&:\quad (L_1,L_2,L_3)=(-1,1,1),\\
 A\cap C&:\quad (L_1,L_2,L_3)=(1,-1,1),\\
 B\cap C&:\quad (L_1,L_2,L_3)=(1,1,-1).
\end{aligned}$$ For example, $A\cap B$ means $L_1+L_2=L_1+L_3=0$. Hence $L_2=L_3=-L_1$, and the total-sum equation gives $-L_1=1$, producing the first triple. The other two calculations are the same equations with permuted indices.

All three labels cannot hold. If all three pair sums vanished, then $L_2=L_3=-L_1$ and $L_2+L_3=0$ would give $2L_2=0$. Characteristic zero gives $L_2=0$, contrary to [\[eq:L\]](#eq:L){reference-type="eqref" reference="eq:L"}. This intersection calculation is a consistency check; the covering argument below does not require the pairwise intersections to be disjoint.

[\[prop:degenerate\]]{#prop:degenerate label="prop:degenerate"} The number of points $P\in T_4(H,\Gamma)$ whose local equation is degenerate at every index $i=0,1,2,3$ is at most $81d^2$.

For an all-degenerate point, the proper-subsum argument gives at least one valid label at each of the four indices. Choose any one valid label at each index. The four choices form a word $w\in\{A,B,C\}^4$, and the point lies in $\mathcal R(w)$. Thus every all-degenerate point lies in $$\bigcup_{w\in\{A,B,C\}^4}\mathcal R(w).$$ A point satisfying two labels at one index may lie in several realization sets. This causes overcounting in the union bound but cannot omit the point. Lemma [\[lem:per-word\]](#lem:per-word){reference-type="ref" reference="lem:per-word"} applies to the full realization set for each word, including points with extra labels. Since there are $3^4=81$ words, $$\#D
 \le
 \sum_{w\in\{A,B,C\}^4}\#\mathcal R(w)
 \le81d^2.$$

## Short-period compatibility and completion

The indexed argument does not assume that the five displayed states are distinct.

[\[lem:short-periods\]]{#lem:short-periods label="lem:short-periods"} If $P\in T_4(H,\Gamma)$ has exact period $n\le4$, the nondegenerate and degenerate estimates above apply without an additional term.

The sequence attached to $P$ still satisfies [\[eq:recurrence\]](#eq:recurrence){reference-type="eqref" reference="eq:recurrence"} at every index $0,1,2,3$. Periodicity only adds relations of the form $x_{j+n}=x_j$. It does not delete any indexed equation. In the nondegenerate class, two indices may produce the same triple, so the four-index union bound may count $P$ more than once; a union bound permits this. The fiber argument remains valid because every $H^i$ is injective even on a periodic orbit.

In the all-degenerate class, a repeated local equation still has at least one valid label at each indexed occurrence. Choosing labels produces a four-letter word, possibly with repeated constraints. The realization set with those additional periodic equalities is a subset of the unrestricted realization set $\mathcal R(w)$, so the per-word bound cannot increase. Thus periods $1,2,3,4$ create compatibility conditions rather than new states.

Proposition [\[prop:nondegenerate\]](#prop:nondegenerate){reference-type="ref" reference="prop:nondegenerate"} bounds the union of points with at least one nondegenerate local equation by $4d\mathcal{E}_{r}$. Proposition [\[prop:degenerate\]](#prop:degenerate){reference-type="ref" reference="prop:degenerate"} bounds the complementary all-degenerate class by $81d^2$. Therefore $$\#T_4(H,\Gamma)
 \le4d\mathcal{E}_{r}+81d^2
 =
 4d\exp\!\bigl(18^9(3r+1)\bigr)+81d^2.$$ Lemma [\[lem:short-periods\]](#lem:short-periods){reference-type="ref" reference="lem:short-periods"} shows that the same partition already includes all short periodic orbits. This proves the theorem.

# Three-transition infinitude in rank one {#sec:sharpness}

We now show that the exceptional $CBA$ chain is not merely a formal free branch: it is realized by infinitely many group-valued initial states through three transitions.

Fix $d\ge2$. The polynomial $X^{d-1}+1$ has a root $c\in\overline{\mathbb Q}$, and every such root is nonzero. Choose one and set $$\label{eq:c-root}
 c^{d-1}=-1.$$ Define $$\label{eq:sharp-data}
 K=\mathbb Q(c),\qquad b=1,\qquad a=-1,\qquad
 \Gamma=\langle2,c,-1\rangle.$$ Because $c$ is algebraic, $K$ is a number field. Equation [\[eq:c-root\]](#eq:c-root){reference-type="eqref" reference="eq:c-root"} gives $c^{2(d-1)}=1$, so $c$ is torsion; $-1$ is torsion as well. Hence $\Gamma$ modulo its torsion subgroup is generated by the class of $2$, and $\operatorname{rank}\Gamma\le1$. The element $2$ has infinite multiplicative order in the characteristic zero field $K$, so its class is nonzero after tensoring with $\mathbb Q$. Therefore $$\operatorname{rank}\Gamma=1.$$

For every integer $n\ge0$, put $$t=2^n,\qquad P_t=(t,t^d).$$ Both coordinates of $P_t$ lie in $\Gamma$. Since $c^d=c\,c^{d-1}=-c$, direct substitution into $H(x,y)=(x^d-y+c,x)$ gives $$\begin{aligned}
 H(P_t)
  &=(t^d-t^d+c,t)=(c,t),\label{eq:sharp-one}\\
 H^2(P_t)
  &=(c^d-t+c,c)=(-t,c),\label{eq:sharp-two}\\
 H^3(P_t)
  &=((-t)^d-c+c,-t)=((-t)^d,-t).\label{eq:sharp-three}\end{aligned}$$ Every coordinate in these four states belongs to $\Gamma$: $t,t^d\in\langle2\rangle$, $c\in\Gamma$, $-t=(-1)t\in\Gamma$, and $(-t)^d\in\Gamma$. Thus $P_t\in T_3(H,\Gamma)$.

The points are pairwise distinct. If $P_{2^m}=P_{2^n}$, equality of the first coordinates gives $2^m=2^n$, hence $m=n$. Consequently the set $\{P_{2^n}:n\ge0\}$ is infinite and $$\#T_3(H,\Gamma)=\infty.$$

The three indexed degeneracies reproduce the exceptional word from Section [4](#sec:degenerate){reference-type="ref" reference="sec:degenerate"}. At index $0$, $$b x_0^d+a x_{-1}=t^d-t^d=0,$$ so $C_0$ holds. At index $1$, $$b x_1^d+c=c^d+c=0,$$ so $B_1$ holds. At index $2$, $$a x_1+c=-c+c=0,$$ so $A_2$ holds. The realized word is therefore $CBA$ in the fixed forward index direction.

The construction checks membership only through $H^3(P_t)$, exactly as the definition of $T_3$ requires. It proves that three transitions do not give a coefficient-uniform finiteness theorem under the hypotheses of Theorem [\[thm:four-step\]](#thm:four-step){reference-type="ref" reference="thm:four-step"}. Together with that theorem, this establishes sharpness of the transition threshold. It neither classifies all infinite $T_3$ coefficient strata nor asserts optimality of either numerical term in [\[eq:main-bound\]](#eq:main-bound){reference-type="eqref" reference="eq:main-bound"}.

# Periodic orbits and limitations {#sec:periodic}

## Injection of whole orbits into the finite window

Let $\mathcal C^\Gamma(H)$ be the collection of exact-period orbits $\mathcal O$ satisfying $\mathcal O\subseteq\Gamma^2$, and let $$U^\Gamma(H)=\bigcup_{\mathcal O\in\mathcal C^\Gamma(H)}\mathcal O.$$ The union is disjoint at the level of orbits because two orbits of an automorphism that share a point are the same orbit.

Take $P\in U^\Gamma(H)$, and let $\mathcal O$ be its orbit. Whole-orbit containment gives $$P,H(P),H^2(P),H^3(P),H^4(P)\in\mathcal O\subseteq\Gamma^2,$$ even when the period is less than five and some states repeat. Hence the identity map on points gives an injection $$U^\Gamma(H)\hookrightarrow T_4(H,\Gamma).$$ The target is finite by Theorem [\[thm:four-step\]](#thm:four-step){reference-type="ref" reference="thm:four-step"}; therefore $U^\Gamma(H)$ is finite, and only finitely many wholly contained periodic orbits occur. Each exact-period-$n$ orbit has exactly $n$ points, so disjointness gives $$\#U^\Gamma(H)=\sum_{n\ge1}n\,C_n^\Gamma(H).$$ Combining the last two displays with Theorem [\[thm:four-step\]](#thm:four-step){reference-type="ref" reference="thm:four-step"} yields $$\sum_{n\ge1}n\,C_n^\Gamma(H)
 \le \#T_4(H,\Gamma)
 \le
 4d\exp\!\bigl(18^9(3r+1)\bigr)+81d^2.$$ This is [\[eq:periodic-bound\]](#eq:periodic-bound){reference-type="eqref" reference="eq:periodic-bound"}.

Whole-orbit containment is indispensable in this argument. A periodic point $P\in\Gamma^2$ need not satisfy $H(P)\in\Gamma^2$, because $\Gamma$ is not additively closed. A single representative in $\Gamma^2$ therefore does not define a point of $T_4(H,\Gamma)$. Corollary [\[cor:periodic\]](#cor:periodic){reference-type="ref" reference="cor:periodic"} makes no assertion about the larger set $\operatorname{Per}(H)\cap\Gamma^2$ under that weaker condition.

## Limitations

The constants in [\[eq:main-bound\]](#eq:main-bound){reference-type="eqref" reference="eq:main-bound"} are explicit but coarse. The Evertse--Schlickewei--Schmidt exponential is used in its published uniform form, without optimization for the special three-variable recurrence. The factor $4$ is a union bound over local indices and can count one point at several nondegenerate indices. Likewise, $81d^2$ sums the same $d^2$ upper bound over all $3^4$ label words, including words that may be incompatible for a given coefficient tuple. None of these observations changes the stated uniform estimate, but none supports numerical optimality.

The result gives no complete coefficient stratification for $T_2$ or $T_3$. Theorem [\[thm:three-step\]](#thm:three-step){reference-type="ref" reference="thm:three-step"} is an existential construction for each $d$, not a description of every infinite three-transition stratum. Its points are not asserted to be periodic. Conversely, the proof of Theorem [\[thm:four-step\]](#thm:four-step){reference-type="ref" reference="thm:four-step"} supplies finiteness after four transitions but does not enumerate the surviving points or determine which degeneracy words are realized.

The map is restricted to the monomial-plus-linear-plus-constant family [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"}. The transition table uses the single monomial $b x_i^d$ at every index. The argument does not establish an analogue for a general polynomial Henon map, a composition of Henon maps, or an arbitrary polynomial automorphism. It also excludes $d=1$, positive characteristic, and zero coefficients; each change alters a step used in the root count or degeneracy analysis.

Finally, Theorem [\[thm:four-step\]](#thm:four-step){reference-type="ref" reference="thm:four-step"} controls a prescribed finite window. It is not a description of all return times along one orbit, a height estimate, an effective enumeration, or a classification of rational or integral periodic points. Every claim in the paper rests on symbolic algebra and the cited unit-equation theorem; no computational, numerical, or experimental evidence is used.

# Conclusion {#sec:conclusion}

Four consecutive transitions provide a uniform escape threshold for the family [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"}: the set of initial states that remain in $\Gamma^2$ through time four has the explicit degree-and-rank bound [\[eq:main-bound\]](#eq:main-bound){reference-type="eqref" reference="eq:main-bound"}. The fixed-coefficient formulation keeps the variable rank at $3r$, while the degenerate analysis isolates and closes the only free chains. The rank-one construction shows that three transitions do not suffice uniformly. These statements leave open the finer classification of shorter windows and any extension beyond the monomial family.

# Complete audit of the nine transitions {#app:nine}

Fix a local index $i$ and the notation from Lemma [\[lem:nine\]](#lem:nine){reference-type="ref" reference="lem:nine"}, $$u=x_{i-1},\qquad v=x_i,\qquad z=x_{i+1},\qquad
 \alpha=-\frac ca.$$ The table is a complete row-by-row substitution audit: the first label is at $i$, the second at $i+1$, and the last column counts initial pairs $(u,v)$.

   word  first-label data      reduced second-label condition                 degree       bound
  ------ --------------------- ------------------------------------------- ------------- ---------
   $AA$  $u=\alpha,\ z=bv^d$   $av+c=0$, hence $v=\alpha$                       $1$         $1$
   $AB$  $u=\alpha,\ z=bv^d$   $bz^d+c=0$, hence $b^{d+1}v^{d^2}=-c$           $d^2$       $d^2$
   $AC$  $u=\alpha,\ z=bv^d$   $bz^d+av=0$; divide by $v\ne0$                 $d^2-1$     $d^2-1$
   $BA$  $bv^d=-c,\ z=au$      $v=\alpha$, compatible iff $b\alpha^d=-c$    free in $u$    free
   $BB$  $bv^d=-c,\ z=au$      $bz^d=-c$, hence $u^d=-c/(ba^d)$                $d+d$       $d^2$
   $BC$  $bv^d=-c,\ z=au$      $bz^d=-av$, hence $u^d=-v/(ba^{d-1})$           $d+d$       $d^2$
   $CA$  $u=-bv^d/a,\ z=c$     $av+c=0$, hence $v=\alpha$                       $1$         $1$
   $CB$  $u=-bv^d/a,\ z=c$     $bc^d+c=0$, independent of $v$               free in $v$    free
   $CC$  $u=-bv^d/a,\ z=c$     $bc^d+av=0$, hence $v=-bc^d/a$                   $1$         $1$

Here $d+d$ means two successive degree-$d$ root choices and hence at most $d^2$ pairs. For the $A$-rows, substitution of $u=\alpha,z=bv^d$ gives respectively $v=\alpha$, $b^{d+1}v^{d^2}=-c$, and, after division by $v\ne0$, $b^{d+1}v^{d^2-1}=-a$. These are nonzero equations of degrees $1,d^2,d^2-1$. For the $B$-rows, $bv^d=-c,z=au$: the $A$-continuation is compatible precisely when $v=\alpha$ and $b\alpha^d=-c$, leaving $u$ free; the other two rows first choose at most $d$ roots $v$, then at most $d$ roots of $u^d=-c/(ba^d)$ or $u^d=-v/(ba^{d-1})$. For the $C$-rows, $u=-bv^d/a,z=c$: the next labels give respectively $v=\alpha$, the compatibility $bc^{d-1}=-1$ with $v$ free, and $v=-bc^d/a$. Thus every equation, compatibility, degree, and root count in the table follows without reversing the indices, and only $BA,CB$ are free.

# Expanded closure, overlap, and dependency checks {#app:closure}

We record the coordinate, division, overlap, and index checks behind the closure argument of the main text.

## Coordinate ledger for the $BA$ continuation {#coordinate-ledger-for-the-ba-continuation .unnumbered}

Assume $b\alpha^d=-c$ and put $t=x_{i-1}$. The four coordinates forced by $BA$ are $$\begin{array}{c|c|l}
\text{coordinate}&\text{value}&\text{source}\\ \hline
x_{i-1}&t&\text{free parameter}\\
x_i&\alpha&A_{i+1}\\
x_{i+1}&at&B_i\\
x_{i+2}&ba^dt^d&A_{i+1}.
\end{array}$$ The unused equation in $B_i$ is exactly the assumed compatibility. The label at $i+2$ gives $$\begin{array}{c|l|c}
\text{word}&\text{calculation}&\text{bound}\\ \hline
BAA&a(at)+c=0\Longleftrightarrow at=\alpha&1\\
BAB&b(ba^dt^d)^d=-c&d^2\\
BAC&b(ba^dt^d)^d=-a(at)&d^2-1.
\end{array}$$ For $BAC$, $t\in\Gamma\le K^\ast$, so division by $t$ turns the equation into the nonzero degree-$d^2-1$ equation $b^{d+1}a^{d^2}t^{d^2-1}+a^2=0$.

## Coordinate ledger for $CB$ and $CBA$ {#coordinate-ledger-for-cb-and-cba .unnumbered}

Assume $bc^{d-1}=-1$ and put $t=x_i$. The $CB$ coordinates are $$\begin{array}{c|c|l}
\text{coordinate}&\text{value}&\text{source}\\ \hline
x_{i-1}&-bt^d/a&C_i\\
x_i&t&\text{free parameter}\\
x_{i+1}&c&C_i\\
x_{i+2}&at&B_{i+1}.
\end{array}$$ The remaining equation in $B_{i+1}$ is $bc^d=-c$, equivalent to the assumed compatibility. The label at $i+2$ gives $$\begin{array}{c|l|c}
\text{word}&\text{calculation}&\text{bound}\\ \hline
CBB&b(at)^d=-c&d\\
CBC&b(at)^d=-ac&d\\
CBA&ac+c=0&\text{free iff }a=-1.
\end{array}$$ The first two rows are nonzero degree-$d$ equations; the last is free exactly when $a=-1$, since $c\ne0$.

Under $a=-1$, the ledger extends by $$x_{i-1}=bt^d,\qquad x_i=t,\qquad x_{i+1}=c,\qquad
 x_{i+2}=-t,\qquad x_{i+3}=b(-t)^d.$$ The fourth label is imposed at index $i+3$: $$\begin{array}{c|l|c}
\text{word}&\text{calculation}&\text{bound}\\ \hline
CBAA&(-1)(-t)+c=0\Longleftrightarrow -t=c&1\\
CBAB&b\bigl(b(-t)^d\bigr)^d=-c&d^2\\
CBAC&b\bigl(b(-t)^d\bigr)^d=-(-1)(-t)&d^2-1.
\end{array}$$ In the last row the right side is $-t$, as in [\[eq:CBA-close\]](#eq:CBA-close){reference-type="eqref" reference="eq:CBA-close"}; since $t=x_i\in\Gamma$, division by $t\ne0$ gives a nonzero equation of degree $d^2-1$. Hence the fourth label leaves no free parameter.

## Simultaneous-label calculation {#simultaneous-label-calculation .unnumbered}

Together with $L_1+L_2+L_3=1$, the vanished pairs give $$\begin{array}{c|c|c}
\text{overlap}&\text{vanishing equations}&(L_1,L_2,L_3)\\ \hline
A\cap B&L_1+L_2=L_1+L_3=0&(-1,1,1)\\
A\cap C&L_1+L_2=L_2+L_3=0&(1,-1,1)\\
B\cap C&L_1+L_3=L_2+L_3=0&(1,1,-1).
\end{array}$$ If all three pairs vanished, adding two and subtracting the third would give $2L_j=0$ for each $j$; characteristic zero and nonvanishing exclude this. Thus simultaneous labels cause overlap but never a missing case.

## Window-length and index audit {#window-length-and-index-audit .unnumbered}

The difference between $T_3$ and $T_4$ can be read directly from the coordinate indices: $$\begin{array}{c|c|c}
\text{survivor set}&\text{coordinates required in }\Gamma&
   \text{local equations available}\\ \hline
T_3&x_{-1},x_0,x_1,x_2,x_3&i=0,1,2\\
T_4&x_{-1},x_0,x_1,x_2,x_3,x_4&i=0,1,2,3.
\end{array}$$ The initial state supplies $x_0,x_{-1}$, and every transition one new coordinate. Hence $CBA$ uses exactly the equations available in $T_3$ and leaves $t=x_0$ free when $a=-1$ and $bc^{d-1}=-1$. Membership of $x_4$ makes the index-$3$ equation available for the nondegenerate/degenerate split. In an all-degenerate $T_4$ continuation, that equation is degenerate and therefore has a label $A$, $B$, or $C$, yielding exactly $CBAA,CBAB,CBAC$. Orientation is fixed by $C_0$, which relates $x_{-1}$ to $x_0^d$, followed by $B_1$, which imposes $b x_1^d+c=0$ (equivalently, its vanishing pair relates $x_2$ and $a x_0$), and then $A_2$, which fixes $x_1$. Thus the forward word is $CBA$, not $ABC$. Periodic coordinate identifications do not alter the available indexed equations.

## Covering and dependency audit {#covering-and-dependency-audit .unnumbered}

At each degenerate index choose any available proper-subsum label. Lemma [\[lem:per-word\]](#lem:per-word){reference-type="ref" reference="lem:per-word"} bounds the whole realization set of the resulting word, including points with additional labels, so the union over words covers the all-degenerate class without a disjoint stratification. The only assumptions used here are $$\operatorname{char}K=0,\qquad d\ge2,\qquad a,b,c\in K^\ast,\qquad
 \Gamma\le K^\ast.$$ Characteristic zero excludes triple overlap; coefficient nonvanishing and $\Gamma\le K^\ast$ justify every division. In particular, no coefficient is assumed to lie in $\Gamma$, and the closure calculation uses no extra finite-generation hypothesis.
