---
p1_kind: "derived-fulltext-reading-copy"
route: "symplectic_map"
logical_paper_id: "symplectic_map--19-shiftlike-translate-gcd-obstruction"
canonical_tex: "symplectic_map/papers/19-shiftlike-translate-gcd-obstruction/paper/main.tex"
canonical_pdf: ""
source_sha256: "c8eb38dcc13a78bebb267d8021965315ab82f7e1ec5d7317f93a49e148b6d588"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Claims--Evidence Matrix

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symplectic_map/papers/19-shiftlike-translate-gcd-obstruction>)
- [规范 TeX](<../../../../../symplectic_map/papers/19-shiftlike-translate-gcd-obstruction/paper/main.tex>)
- [支撑 Markdown](<../../../../../symplectic_map/papers/19-shiftlike-translate-gcd-obstruction/notes/CLAIMS_EVIDENCE_MATRIX.md>)
- [BibTeX](<../../../../../symplectic_map/papers/19-shiftlike-translate-gcd-obstruction/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Finite windows of a sparse shift-like recurrence define subvarieties of algebraic tori, but their character relations do not by themselves decide whether a torus translate is actually contained in the window. We separate these two layers and solve the extremal lifting problem in two regimes. For a polynomial with a nonzero constant and at least two nonconstant monomials, every translate of maximum possible dimension $k-m$ has one canonical subgroup. Its normalized translating scalars form an explicit scheme $E_m$; we classify its geometric points, prove coefficientwise nonemptiness, determine its reduced components and nilpotent root directions, and construct a flat relative local-complete-intersection family over the fixed-support coefficient torus. For $P=c+bX^d$, writing $g=\gcd(k,\nu)$, $q=k/g$, and $L=(k-\nu)/g$, we prove that $q^2$ core equations extinguish all characters, whereas $q^2-1$ equations leave one colored Laurent shadow. The shadow has no compatible translating scalars when $q\geq3$, so the full window already excludes positive-dimensional translates at $kq-1$; this is an upper-window obstruction, not an optimal threshold. When $q=2$, a lift exists exactly when $a=-1$ and $bc^{d-1}=-1$, including every gcd residue. Laurent's qualitative torus theorem then yields the corresponding finite-rank consequences.
bibliography:
- references.bib
```

## Markdown 正文

**Maximum-Dimensional Torus Translates in Sparse Shift-Like Recurrences:**

**Coefficientwise Moduli and a Support-One GCD Obstruction**

# Introduction {#sec:introduction}

A finite orbit condition for a polynomial automorphism can be encoded by a finite list of polynomial recurrence equations. When all coordinates are required to lie in a multiplicative group, those equations become a problem about a subvariety of an algebraic torus. The basic geometric obstruction is familiar: a positive-dimensional translated subtorus can carry infinitely many finite-rank points. The difficult direction is to decide exactly which character patterns come from a contained translate, because a relation among characters is only the first half of the containment identity. The translating scalars must satisfy a second, nonlinear system.

This paper makes that distinction effective for the type-$\nu$ shift-like maps introduced in complex dynamics by @bedfordpambuccian1998dynamics and subsequently studied in several forms [@bera2019polynomial; @beraverma2018aspects; @kaur2026remarks]. We work over an algebraically closed field $\Omega$ of characteristic zero and consider $$S(z_1,\ldots,z_k)
   =\bigl(z_2,\ldots,z_k,P(z_{k-\nu+1})+az_1\bigr),
 \qquad 1\leq \nu<k,\quad a\neq0.$$ In zero-based orbit coordinates, its defining recurrence is $$\label{eq:intro-recurrence}
 x_{n+k}=P(x_{n+k-\nu})+a x_n .$$ For $m$ consecutive equations, let $V_m\subset\mathbb{G}_{\mathrm m}^{k+m}$ be the resulting window variety. A connected translate $\xi H\subset V_m$ contributes two kinds of data: restrictions $u_i\in X^\ast(H)$ of ambient coordinate characters, and nonzero scalars $\xi_i$. Our common method first determines the extremal pattern of the $u_i$, then asks whether the $\xi_i$ lift that pattern.

The answer has two complementary forms.

1.  For $$P(X)=c+\sum_{\ell=1}^{s}b_\ell X^{e_\ell},
     \qquad 0<e_1<\cdots<e_s,\quad s\geq2,$$ with every displayed coefficient nonzero, an anchored dimension bound from an anonymous companion work [@companionDecay] is rigid at equality. Every $(k-m)$-dimensional translate has the same subgroup $H_m$. After a unique normalization, all translating scalars are classified by an explicit locally closed scheme $E_m$. The active-coordinate count is $$\alpha_m=\min(m,k-m,\nu,k-\nu).$$ Every assignment of roots at those active coordinates survives the open nonvanishing conditions. This gives the exact squarefree and reduced geometric component counts, the multiple-root nilpotents, and a fixed-support universal family that is flat relative lci and smooth away from the discriminant.

2.  For $P(X)=c+bX^d$, let $$g=\gcd(k,\nu),\qquad q=k/g,\qquad L=(k-\nu)/g.$$ The $g$ residue classes reduce the character problem to the core recurrence $$F_{j+q}=F_j+T F_{j+L}.$$ The reduction is valid in arbitrary character rank: different scaling components receive independent colors, and a cycle argument supplies integer heights. Exactly $q^2$ core equations force extinction. One equation earlier there is a unique colored Laurent shadow, with generating functions $$\frac{1+Tz^L}{1+Tz^L+z^q}
     \quad\text{and}\quad
     \frac{z^{q-1}}{1+Tz^{q-L}+z^q}.$$ For $q\geq3$, seven forced local labels make its scalar lift contradictory. For $q=2$, the lift exists precisely on $a=-1$, $bc^{d-1}=-1$, and a polynomial-automorphism argument fills all inactive residues.

These results answer the same question from opposite sides. In the anchored multi-support case, the extremal character pattern admits a complete coefficientwise lift scheme. In the support-one case, the last possible character shadow usually does not lift at all. The distinction matters arithmetically. Laurent's qualitative theorem [@laurent1984equations] transfers absence of positive-dimensional translates to finiteness for every finite-rank group. Conversely, a saturated one-dimensional translate produces compatible infinitude after adjoining its finitely many scalars. Thus Part A gives coefficientwise infinitude at $k-1$ and finite-rank finiteness at $k$, while Part B gives finiteness at $kq$, already at $kq-1$ for $q\geq3$, and an exact resonant exception for $q=2$.

The qualifications are part of the statements. We classify only translates of dimension exactly $k-m$ in Part A, not all lower-dimensional or inclusion-maximal translates. The scheme $E_m$ is an explicit normalized parameter scheme, not a Hilbert scheme, a Fano scheme, or a fine moduli functor. Component counts are geometric-fiber statements, and the smooth count requires $P$ squarefree. Coefficientwise sharpness means existence after a compatible finite extension and for a compatible finitely generated group; it is not a statement about every fixed group. For $q\geq3$, the conclusion at $kq-1$ is a universal penultimate obstruction. No survivor is constructed at a shorter window, so no exact, shortest, minimal, or optimal scalar threshold is asserted.

Section [2](#sec:preliminaries){reference-type="ref" reference="sec:preliminaries"} fixes the recurrence, character, lattice, and arithmetic tools. Sections [3](#sec:rigidity){reference-type="ref" reference="sec:rigidity"}--[6](#sec:partA-arithmetic){reference-type="ref" reference="sec:partA-arithmetic"} prove the Part A classification, family geometry, and arithmetic consequence. Sections [7](#sec:labels){reference-type="ref" reference="sec:labels"}--[10](#sec:scalar){reference-type="ref" reference="sec:scalar"} establish the arbitrary-rank core theorem and scalar obstruction. Section [11](#sec:conclusion){reference-type="ref" reference="sec:conclusion"} places the quantifiers beside related work and records the exact boundary of the conclusions.

# Recurrences, character lattices, Laurent bridge, and predecessor boundary {#sec:preliminaries}

## Finite recurrence windows

Fix an algebraically closed field $\Omega$ of characteristic zero, integers $k\geq2$ and $1\leq\nu<k$, and $a\in\Omega^\ast$. For $P\in\Omega[X]$, the inverse of $S$ is $$S^{-1}(w_1,\ldots,w_k)
 =
 \bigl(a^{-1}(w_k-P(w_{k-\nu})),w_1,\ldots,w_{k-1}\bigr).$$ Thus $S$ is a polynomial automorphism, and an orbit has the zero-based scalar recurrence $$\label{eq:recurrence}
 x_{n+k}=P(x_{n+k-\nu})+a x_n.$$ For $m\geq0$, define $$V_m=\left\{(x_0,\ldots,x_{k+m-1})\in\mathbb{G}_{\mathrm m}^{k+m}:
 \eqref{eq:recurrence}\ \text{holds for }0\leq n<m\right\},$$ and put $V_0=\mathbb{G}_{\mathrm m}^k$. Here $m$ counts transitions: the ambient tuple records the states at times $0,\ldots,m$.

Let $K$ be a characteristic-zero field containing the coefficients and let $\Gamma\leq K^\ast$. Set $$T_m(S,\Gamma)=
 \left\{z\in\Gamma^k:S^j(z)\in\Gamma^k\text{ for }0\leq j\leq m\right\}.$$ Every initial $k$-tuple determines all later coordinates through [\[eq:recurrence\]](#eq:recurrence){reference-type="eqref" reference="eq:recurrence"}; conversely, every point of $V_m$ projects to its initial tuple. Projection therefore restricts to a bijection $$\label{eq:projection-bijection}
 V_m\cap\Gamma^{k+m}\ \xrightarrow{\;\sim\;}\ T_m(S,\Gamma).$$ We use geometric dimension only for a translate $\xi H\subset V_m$, never for the point set $T_m(S,\Gamma)$.

## Characters and saturated lattices

Let $\xi H\subset\mathbb{G}_{\mathrm m}^N$, where $H$ is a connected closed subtorus. Write $$M=X^\ast(H),\qquad x_i|_{\xi H}=\xi_i\chi^{u_i},
 \quad \xi_i\in\Omega^\ast,\quad u_i\in M.$$ The restriction homomorphism $$\label{eq:ambient-surjection}
 \mathbb{Z}^N=X^\ast(\mathbb{G}_{\mathrm m}^N)\longrightarrow X^\ast(H)=M$$ is surjective. Consequently, the ambient restrictions $u_i$ generate the actual character lattice $M$.

[\[lem:character-independence\]]{#lem:character-independence label="lem:character-independence"} Distinct characters of $H$ are linearly independent over $\Omega$. In a vanishing linear combination of characters, the coefficient sum in each character class is zero. Moreover, the coordinate restrictions $u_0,\ldots,u_{N-1}$ generate $M$.

The coordinate ring of $H$ is the group algebra $\Omega[M]$, whose monomials $\chi^u$, $u\in M$, form an $\Omega$-basis. The first assertion is therefore the uniqueness of the group-algebra expansion. The second assertion is exactly the surjectivity of [\[eq:ambient-surjection\]](#eq:ambient-surjection){reference-type="eqref" reference="eq:ambient-surjection"}, which is dual to the closed immersion $H\hookrightarrow\mathbb{G}_{\mathrm m}^N$.

[\[lem:saturated-kernels\]]{#lem:saturated-kernels label="lem:saturated-kernels"} Let $L\subset\mathbb{Z}^N$ be saturated. If $L$ lies in the character kernel of a connected subtorus and the two lattices have the same rank, then they are equal.

Saturation gives $L=(L\otimes_\mathbb{Z}\mathbb{Q})\cap\mathbb{Z}^N$. An equal-rank over-lattice inside $\mathbb{Z}^N$ has the same rational span; every one of its elements therefore lies in $(L\otimes\mathbb{Q})\cap\mathbb{Z}^N=L$.

## The qualitative arithmetic bridge

We use one external theorem. Laurent's torus Mordell--Lang theorem implies that, for a closed subvariety $X$ of a complex torus and the division hull of a finitely generated subgroup, $X$ meets that hull in a finite union of intersections with torus translates contained in $X$ [@laurent1984equations]. In particular, if $X$ contains no positive-dimensional torus translate, that intersection is finite. We use no effective cardinality, algorithm, or recurrence-specific exceptional set from this theorem.

[\[prop:finite-rank-bridge\]]{#prop:finite-rank-bridge label="prop:finite-rank-bridge"} Let $X$ be a closed subvariety of a torus over a characteristic-zero field $K$. If $X_{\overline K}$ contains no positive-dimensional torus translate, then $X(K)\cap\Gamma^N$ is finite for every finite-rank subgroup $\Gamma\leq K^\ast$, including groups with arbitrary torsion.

Choose $\gamma_1,\ldots,\gamma_r\in\Gamma$ whose classes form a $\mathbb{Q}$-basis of $\Gamma\otimes_\mathbb{Z}\mathbb{Q}$, and let $\Gamma_0=\langle\gamma_1,\ldots,\gamma_r\rangle$. For $\gamma\in\Gamma$, a rational relation expresses a positive power $\gamma^e$ as an element of $\Gamma_0$ up to torsion. Raising once more by the torsion order shows that a positive power of $\gamma$ lies in $\Gamma_0$. Hence $$\Gamma\subset\Gamma_0^{\mathrm{div}}
 :=\{\alpha\in\overline K^\ast:\alpha^n\in\Gamma_0
 \text{ for some }n\geq1\}.$$

Let $K_0$ be the finitely generated field generated over its prime field by the coefficients defining $X$ and by $\gamma_1,\ldots,\gamma_r$. Since $K_0$ has characteristic zero, it embeds in $\mathbb C$, and the embedding extends to an algebraic closure containing all relevant division points. Laurent's theorem applies after this embedding. It makes $X\cap(\Gamma_0^{\mathrm{div}})^N$ finite because no positive-dimensional translate is contained in $X_{\overline K}$. The desired intersection is a subset. This argument embeds only the finitely generated coefficient-and-generator field, not an arbitrary large ground field.

## The anchored predecessor bound

For the multi-support polynomial in Part A, an anonymous companion manuscript proves the following dimension theorem [@companionDecay]. It is the only delimited nonlocal recurrence input used below; Laurent's theorem remains the sole external imported theorem.

[\[thm:anchored-bound\]]{#thm:anchored-bound label="thm:anchored-bound"} Assume that $P$ has nonzero constant term and at least two actual nonconstant monomials, all with nonzero coefficients. If $0\leq m\leq k$ and $\xi H\subset V_m$ is a connected translate, then $$\dim H\leq k-m.$$

The mechanism of Theorem [\[thm:anchored-bound\]](#thm:anchored-bound){reference-type="ref" reference="thm:anchored-bound"} is short enough to make the equality analysis transparent. Character independence kills the middle character in each recurrence equation; the remaining endpoint relation and the killed middle coordinate give $2m$ independent saturated relations. Section [3](#sec:rigidity){reference-type="ref" reference="sec:rigidity"} proves those facts explicitly and uses equality of ranks to identify the subgroup. The upper bound and its special equality examples remain results of the companion work, not new claims here.

# Saturated equality rigidity {#sec:rigidity}

Throughout Sections [3](#sec:rigidity){reference-type="ref" reference="sec:rigidity"}--[6](#sec:partA-arithmetic){reference-type="ref" reference="sec:partA-arithmetic"}, assume $$\label{eq:partA-polynomial}
 P(X)=c+\sum_{\ell=1}^{s}b_\ell X^{e_\ell},
 \qquad 0<e_1<\cdots<e_s,\quad s\geq2,$$ where $a,c,b_1,\ldots,b_s\in\Omega^\ast$, and fix $1\leq m<k$. Suppose $\xi H\subset V_m$, and write the restricted coordinate characters as $u_i\in M=X^\ast(H)$.

[\[prop:middle-collapse\]]{#prop:middle-collapse label="prop:middle-collapse"} For every $0\leq n<m$, $$u_{k+n-\nu}=0.$$ Moreover, $$u_{k+n}=u_n$$ whenever either character is nonzero, and in all cases the character kernel contains $$A_n=\varepsilon_{k+n-\nu},
 \qquad B_n=\varepsilon_{k+n}-\varepsilon_n.$$

Put $t=k+n-\nu$. Restriction of the $n$-th recurrence equation to $\xi H$ gives the identity in $\Omega[M]$ $$\label{eq:partA-group-algebra}
 \xi_{n+k}\chi^{u_{n+k}}
 -a\xi_n\chi^{u_n}
 -c-\sum_{\ell=1}^{s}b_\ell\xi_t^{e_\ell}
       \chi^{e_\ell u_t}=0.$$ If $u_t\neq0$, torsion-freeness of $M$ makes $$0,e_1u_t,\ldots,e_su_t$$ pairwise distinct. These are at least three character classes. The two endpoint terms can meet at most two of them, so one polynomial term would be a nonzero singleton, contrary to Lemma [\[lem:character-independence\]](#lem:character-independence){reference-type="ref" reference="lem:character-independence"}. Hence $u_t=0$.

After collecting constant-character terms, [\[eq:partA-group-algebra\]](#eq:partA-group-algebra){reference-type="eqref" reference="eq:partA-group-algebra"} becomes $$\label{eq:partA-collected}
 \xi_{n+k}\chi^{u_{n+k}}
 -a\xi_n\chi^{u_n}-P(\xi_t)=0.$$ If $P(\xi_t)\neq0$, the constant character occurs and independence forces both endpoint characters to be zero. If $P(\xi_t)=0$, the two nonzero endpoint terms must share a character and cancel, so $$u_{n+k}=u_n,\qquad \xi_{n+k}=a\xi_n.$$ In both cases $A_n$ and $B_n$ lie in the ambient character kernel.

Define $$R_m=\{\,n-\nu\bmod k:0\leq n<m\,\}\subset\{0,\ldots,k-1\}$$ and let $L_m\subset\mathbb{Z}^{k+m}$ be generated by the $2m$ vectors $A_n,B_n$ from Proposition [\[prop:middle-collapse\]](#prop:middle-collapse){reference-type="ref" reference="prop:middle-collapse"}.

[\[lem:free-quotient\]]{#lem:free-quotient label="lem:free-quotient"} The quotient $\mathbb{Z}^{k+m}/L_m$ is freely generated by the initial coordinate classes $\varepsilon_i$ with $i\notin R_m$. In particular, $L_m$ is saturated of rank $2m$.

First quotient by the relations $B_n$. They identify the future class $\varepsilon_{k+n}$ with the initial class $\varepsilon_n$, and eliminate all $m$ future generators without torsion. Under those identifications, the $A_n$ kill precisely the $m$ distinct initial classes indexed by $R_m$. The remaining initial classes form a free basis. Thus the quotient is free of rank $k-m$, which proves both saturation and $\operatorname{rank}L_m=2m$.

Let $H_m\subset\mathbb{G}_{\mathrm m}^{k+m}$ be the connected subtorus defined by $$\label{eq:Hm}
 x_r=1\quad(r\in R_m),\qquad
 x_{k+n}=x_n\quad(0\leq n<m).$$ Its character kernel is $L_m$.

[\[thm:equality-rigidity\]]{#thm:equality-rigidity label="thm:equality-rigidity"} If $\xi H\subset V_m$ and $\dim H=k-m$, then $H=H_m$.

The ambient character map $\mathbb{Z}^{k+m}\to X^\ast(H)$ has kernel of rank $$(k+m)-(k-m)=2m.$$ Proposition [\[prop:middle-collapse\]](#prop:middle-collapse){reference-type="ref" reference="prop:middle-collapse"} puts $L_m$ inside that kernel, and Lemma [\[lem:free-quotient\]](#lem:free-quotient){reference-type="ref" reference="lem:free-quotient"} proves that it is saturated of rank $2m$. Theorem [\[thm:anchored-bound\]](#thm:anchored-bound){reference-type="ref" reference="thm:anchored-bound"} identifies $\dim H=k-m$ as the equality case of the predecessor bound. Lemma [\[lem:saturated-kernels\]](#lem:saturated-kernels){reference-type="ref" reference="lem:saturated-kernels"} now makes the two kernel lattices equal. Equation [\[eq:Hm\]](#eq:Hm){reference-type="eqref" reference="eq:Hm"} defines the subtorus with exactly that kernel, hence $H=H_m$.

Theorem [\[thm:equality-rigidity\]](#thm:equality-rigidity){reference-type="ref" reference="thm:equality-rigidity"} is an equality classification, not a classification of lower-dimensional or inclusion-maximal translates. This distinction will also matter when $E_m$ is introduced: it parameterizes normalized translates with the subgroup $H_m$, rather than arbitrary subschemes of $V_m$.

# Normalized translates and nonemptiness {#sec:normalized-scheme}

Continue with [\[eq:partA-polynomial\]](#eq:partA-polynomial){reference-type="eqref" reference="eq:partA-polynomial"}, now writing $e_s=\delta$. Thus the displayed exponents are the actual support of $P-c$, and none of $a,c,b_1,\ldots,b_s$ may vanish. Fix $1\leq m\leq k-1$. Recall that $$R_m=\{n-\nu\bmod k:0\leq n<m\}$$ and that $H_m$ is characterized by $$h_{k+n-\nu}=1,\qquad h_{k+n}=h_n\qquad(0\leq n<m).$$ Its initial coordinates $h_r$, $r\notin R_m$, are free.

Define the active interval $$\label{eq:active-interval}
 \mathcal A_m=
 \{n\in\mathbb{Z}:\max(0,m-\nu)\leq n<\min(m,k-\nu)\}$$ and put $$\label{eq:alpha}
 \alpha=\alpha_m:=|\mathcal A_m|
 =\min(m,k-m,\nu,k-\nu).$$ An integer interval is empty when its lower endpoint is at least its upper endpoint.

[\[lem:active-interval\]]{#lem:active-interval label="lem:active-interval"} For $0\leq n<m$, the coordinate $h_n$ is nonconstant on $H_m$ if and only if $n\in\mathcal A_m$. Equivalently, $$\mathcal A_m=\{0,\ldots,m-1\}\setminus R_m.$$ Its cardinality is $\alpha$ in [\[eq:alpha\]](#eq:alpha){reference-type="eqref" reference="eq:alpha"}.

Reduction of $n-\nu$ modulo $k$ gives $$R_m\cap\{0,\ldots,m-1\}
 =
 \{0,\ldots,m-\nu-1\}\sqcup\{k-\nu,\ldots,m-1\},$$ with the empty-interval convention. The complement is [\[eq:active-interval\]](#eq:active-interval){reference-type="eqref" reference="eq:active-interval"}. Its length is $$\min(m,k-\nu)-\max(0,m-\nu).$$ Splitting according to $m\leq\nu$ or $m>\nu$, and independently according to $m\leq k-\nu$ or $m>k-\nu$, identifies this expression with $\min(m,k-m,\nu,k-\nu)$.

On $\mathbb{G}_{\mathrm m}^m$, with coordinates $y_0,\ldots,y_{m-1}$, set $$\begin{aligned}
 F_n&=y_n-P(y_{n-\nu}) &&(\nu\leq n<m), \label{eq:F-open}\\
 G_j&=P(y_j)+a y_{j+\nu-k} &&(k-\nu\leq j<m), \label{eq:G-open}\\
 D_m&=\prod_{\nu\leq n<m}F_n\prod_{k-\nu\leq j<m}G_j.
 \label{eq:D-open}\end{aligned}$$ Empty products equal $1$. Define the normalized translation scheme $$\label{eq:Em-definition}
 E_m=\operatorname{Spec}
 \frac{\Omega[y_0^{\pm1},\ldots,y_{m-1}^{\pm1},D_m^{-1}]}
      {(P(y_i):i\in\mathcal A_m)}.$$ Its two open conditions are explicitly $$\begin{aligned}
 y_n&\neq P(y_{n-\nu}) &&(\nu\leq n<m), \label{eq:first-open}\\
 P(y_j)+a y_{j+\nu-k}&\neq0 &&(k-\nu\leq j<m).
 \label{eq:second-open}\end{aligned}$$

A representative $\xi\in(\Omega^\ast)^{k+m}$ of $\xi H_m$ is *normalized* if $$\xi_r=1\qquad(r\in\{0,\ldots,k-1\}\setminus R_m).$$ Every translate of $H_m$ has exactly one normalized representative: the free initial coordinates of $H_m$ normalize the entries outside $R_m$, and then $h_{k+j}=h_j$ fixes the output coordinates of the normalizing element.

[\[prop:reconstruction\]]{#prop:reconstruction label="prop:reconstruction"} For $y=(y_0,\ldots,y_{m-1})\in E_m$, define the initial coordinates of $\xi(y)$ by $$\begin{aligned}
 \xi_{k+n-\nu}(y)&=y_n
 &&(0\leq n<\min(m,\nu)), \label{eq:reconstruct-tail}\\
 \xi_{n-\nu}(y)&=a^{-1}\bigl(y_n-P(y_{n-\nu})\bigr)
 &&(\nu\leq n<m), \label{eq:reconstruct-head}\\
 \xi_r(y)&=1
 &&(r\in\{0,\ldots,k-1\}\setminus R_m), \label{eq:reconstruct-free}\end{aligned}$$ and define every output coordinate by $$\label{eq:reconstruct-output}
 \xi_{k+j}(y)=P(y_j)+a\xi_j(y)\qquad(0\leq j<m).$$ These formulas give a torus point with $$\xi(y)H_m\subseteq V_m.$$ Conversely, each normalized $\xi$ satisfying $\xi H_m\subseteq V_m$ comes from a unique $y\in E_m$ by these formulas. Both constructions are morphisms of schemes.

The assignments [\[eq:reconstruct-tail\]](#eq:reconstruct-tail){reference-type="eqref" reference="eq:reconstruct-tail"}--[\[eq:reconstruct-free\]](#eq:reconstruct-free){reference-type="eqref" reference="eq:reconstruct-free"} cover the initial indices exactly once. Condition [\[eq:first-open\]](#eq:first-open){reference-type="eqref" reference="eq:first-open"} makes every coordinate in [\[eq:reconstruct-head\]](#eq:reconstruct-head){reference-type="eqref" reference="eq:reconstruct-head"} nonzero. Partition $0\leq j<m$. If $j+\nu<m$, equation [\[eq:reconstruct-head\]](#eq:reconstruct-head){reference-type="eqref" reference="eq:reconstruct-head"} with $n=j+\nu$ gives $$\xi_{k+j}=P(y_j)+a\xi_j=y_{j+\nu}.$$ If $j+\nu\geq m$ and $j\in\mathcal A_m$, then $\xi_j=1$ and $P(y_j)=0$, so $\xi_{k+j}=a$. In the remaining case, Lemma [\[lem:active-interval\]](#lem:active-interval){reference-type="ref" reference="lem:active-interval"} forces $j\geq k-\nu$, and $$\xi_{k+j}=P(y_j)+a y_{j+\nu-k}=G_j,$$ which is nonzero by [\[eq:second-open\]](#eq:second-open){reference-type="eqref" reference="eq:second-open"}. Thus $\xi(y)$ is a torus point.

For $h\in H_m$, one has $\xi_{k+j-\nu}=y_j$, $h_{k+j-\nu}=1$, and $h_{k+j}=h_j$. The $j$-th recurrence identity on $\xi(y)h$ is $$P(y_j)+a\xi_jh_j-\bigl(P(y_j)+a\xi_j\bigr)h_j
 =P(y_j)(1-h_j).$$ If $j\in R_m$, then $h_j=1$; otherwise $j\in\mathcal A_m$ and $P(y_j)=0$. Every equation therefore vanishes on the translate.

Conversely, let $\xi$ be normalized and set $y_j=\xi_{k+j-\nu}$. The recurrence identity reads $$P(y_j)+a\xi_jh_j-\xi_{k+j}h_j=0.$$ When $j\notin R_m$, the character $h_j$ is nonconstant, so character independence gives $P(y_j)=0$ and $\xi_{k+j}=a\xi_j$. These are precisely the active root equations. When $j\in R_m$, one has $h_j=1$ and $\xi_{k+j}=P(y_j)+a\xi_j$. Comparing overlapping middle and output coordinates gives [\[eq:reconstruct-head\]](#eq:reconstruct-head){reference-type="eqref" reference="eq:reconstruct-head"}; the initial tail and normalization give [\[eq:reconstruct-tail\]](#eq:reconstruct-tail){reference-type="eqref" reference="eq:reconstruct-tail"} and [\[eq:reconstruct-free\]](#eq:reconstruct-free){reference-type="eqref" reference="eq:reconstruct-free"}. Nonvanishing of $\xi$ gives both open families. All formulas are regular after localizing at $D_m$, so they are inverse morphisms.

[\[thm:normalized-classification\]]{#thm:normalized-classification label="thm:normalized-classification"} For every algebraically closed extension $L/\Omega$, the assignment $$y\longmapsto\xi(y)H_m$$ is a bijection from $E_m(L)$ to the torus translates contained in $(V_m)_L$ whose subgroup has dimension exactly $k-m$. Each subgroup is $H_m$, and each translate has exactly one normalized representative. Proposition [\[prop:reconstruction\]](#prop:reconstruction){reference-type="ref" reference="prop:reconstruction"} identifies $E_m$ with the scheme of normalized translating points. No translate of lower dimension is classified.

Theorem [\[thm:anchored-bound\]](#thm:anchored-bound){reference-type="ref" reference="thm:anchored-bound"} bounds every contained translate by $k-m$, and Theorem [\[thm:equality-rigidity\]](#thm:equality-rigidity){reference-type="ref" reference="thm:equality-rigidity"} identifies the subgroup at equality with $H_m$. Normalize its representative and apply Proposition [\[prop:reconstruction\]](#prop:reconstruction){reference-type="ref" reference="prop:reconstruction"}. The converse and uniqueness are the forward direction and normalization statement of that proposition.

[\[lem:avoidance\]]{#lem:avoidance label="lem:avoidance"} Choose a root $\rho_i\in\Omega^\ast$ of $P$ for every $i\in\mathcal A_m$. Imposing $y_i=\rho_i$ at the active indices leaves a reduced torus $$T_\rho\simeq\mathbb{G}_{\mathrm m}^{m-\alpha},$$ and $T_\rho\cap E_m$ is a nonempty irreducible open subset. If $\alpha=m$, both families of open conditions are empty and this intersection is one point.

Theorem [\[thm:normalized-classification\]](#thm:normalized-classification){reference-type="ref" reference="thm:normalized-classification"} reduces coefficientwise nonemptiness to showing that no root choice is lost under the localization. The nonzero constant term makes every root of $P$ nonzero. It therefore suffices to show that no factor of $D_m$ vanishes identically on $T_\rho$. For $F_n=y_n-P(y_{n-\nu})$, if $n\notin\mathcal A_m$, then $y_n$ is free and its linear occurrence makes $F_n$ nonzero. If $n\in\mathcal A_m$ and $n\geq\nu$, then $n-\nu<m-\nu$, hence $n-\nu\notin\mathcal A_m$; the variable $y_{n-\nu}$ is free, and $P(y_{n-\nu})$ is nonconstant. Thus $F_n$ is again nonzero.

For $k-\nu\leq j<m$, the index $j$ lies outside $\mathcal A_m$. The variable $y_j$ is free, and the leading term $b_s y_j^\delta$ makes $G_j$ nonzero. The restriction of $D_m$, a product of nonzero Laurent polynomials in the domain $\Omega[T_\rho]$, is nonzero. Its principal open is nonempty and irreducible. If $\alpha=m$, [\[eq:alpha\]](#eq:alpha){reference-type="eqref" reference="eq:alpha"} gives $m\leq\nu$ and $m\leq k-\nu$, so both open index ranges are empty.

[\[thm:partA-geometry\]]{#thm:partA-geometry label="thm:partA-geometry"} Suppose $P$ has $r$ distinct roots in $\Omega$, with multiplicities $\mu_1,\ldots,\mu_r$. Then $(E_m)_{\mathrm{red}}$ is the disjoint union of $r^\alpha$ nonempty smooth irreducible varieties of dimension $m-\alpha$, indexed by a distinct-root choice at each active coordinate.

If $P$ is squarefree, then $r=\delta$, the full scheme $E_m$ is smooth, and it has exactly $\delta^\alpha$ irreducible components. If $P$ has a multiple root, every nonempty active-root stratum using it carries nontrivial nilpotent structure. Since $\alpha\geq1$ for $1\leq m\leq k-1$, $E_m$ is reduced if and only if $P$ is squarefree.

Before localization, the reduced root equation at each active coordinate is a disjoint union of $r$ points. Independent choices give $r^\alpha$ reduced strata. Lemma [\[lem:avoidance\]](#lem:avoidance){reference-type="ref" reference="lem:avoidance"} leaves on each a nonempty open of $\mathbb{G}_{\mathrm m}^{m-\alpha}$, hence a smooth irreducible variety of dimension $m-\alpha$.

If $P$ is squarefree, each root equation is étale, giving the assertion for the full scheme. At a root $\rho$ of multiplicity $\mu>1$, $$P(y_i)=(y_i-\rho)^\mu u_i(y_i),\qquad u_i(\rho)\neq0.$$ Thus $y_i-\rho$ supplies nilpotent structure on every surviving stratum using $\rho$. Proposition [\[prop:completed-fiber\]](#prop:completed-fiber){reference-type="ref" reference="prop:completed-fiber"} gives the precise completed form.

# Fixed-fiber and universal geometry {#sec:universal-family}

Fix the exponent set $0<e_1<\cdots<e_s=\delta$. The coefficient base preserving this actual support is $$\mathcal B=\operatorname{Spec}\mathcal R,\qquad
 \mathcal R=\mathbb{Q}[a^{\pm1},c^{\pm1},b_1^{\pm1},\ldots,b_s^{\pm1}],$$ and the universal polynomial is $$\mathcal P(X)=c+\sum_{\ell=1}^{s}b_\ell X^{e_\ell}.$$ The units in $\mathcal R$ prevent specialization from deleting a displayed monomial.

[\[lem:universal-root\]]{#lem:universal-root label="lem:universal-root"} The root scheme $$\mathcal Z=\operatorname{Spec}
 \frac{\mathcal R[X,X^{-1}]}{(\mathcal P(X))}
 \longrightarrow\mathcal B$$ is finite locally free of rank $\delta$. Over $$\mathcal B^{\rm sf}
 =D\bigl(\operatorname{Disc}_X(\mathcal P)\bigr),$$ it is finite étale.

Because $b_s$ is a unit, $b_s^{-1}\mathcal P(X)$ is monic of degree $\delta$. Because $c$ is a unit, the defining relation $$c=-X\sum_{\ell=1}^{s}b_\ell X^{e_\ell-1}$$ makes $X$ invertible already in $\mathcal R[X]/(\mathcal P)$. Therefore $$\mathcal R[X,X^{-1}]/(\mathcal P)
 =\mathcal R[X]/(\mathcal P)$$ is free over $\mathcal R$ on $1,X,\ldots,X^{\delta-1}$. On the discriminant complement, the polynomial and its derivative have no common geometric root, so this finite flat morphism is étale.

Put $$\mathcal F_n=y_n-\mathcal P(y_{n-\nu}),\qquad
 \mathcal G_j=\mathcal P(y_j)+a y_{j+\nu-k},$$ over the respective index ranges in [\[eq:F-open\]](#eq:F-open){reference-type="eqref" reference="eq:F-open"} and [\[eq:G-open\]](#eq:G-open){reference-type="eqref" reference="eq:G-open"}, and set $$\mathcal D_m=
 \prod_{\nu\leq n<m}\mathcal F_n
 \prod_{k-\nu\leq j<m}\mathcal G_j.$$ Define $$\label{eq:universal-Em}
 \mathcal E_m=\operatorname{Spec}
 \frac{\mathcal R[y_0^{\pm1},\ldots,y_{m-1}^{\pm1},
                       \mathcal D_m^{-1}]}
      {(\mathcal P(y_i):i\in\mathcal A_m)}.$$

[\[thm:universal-translation\]]{#thm:universal-translation label="thm:universal-translation"} The morphism $\mathcal E_m\to\mathcal B$ is flat and relative local complete intersection of relative dimension $m-\alpha$. Its geometric fiber at a coefficient tuple is exactly $E_m$ from [\[eq:Em-definition\]](#eq:Em-definition){reference-type="eqref" reference="eq:Em-definition"}. Reconstruction [\[eq:reconstruct-tail\]](#eq:reconstruct-tail){reference-type="eqref" reference="eq:reconstruct-tail"}--[\[eq:reconstruct-output\]](#eq:reconstruct-output){reference-type="eqref" reference="eq:reconstruct-output"}, with $P$ replaced by $\mathcal P$, is universal over $\mathcal B$. Moreover, $$\mathcal E_m|_{\mathcal B^{\rm sf}}\longrightarrow\mathcal B^{\rm sf}$$ is smooth of relative dimension $m-\alpha$.

Before localizing at $\mathcal D_m$, the scheme in [\[eq:universal-Em\]](#eq:universal-Em){reference-type="eqref" reference="eq:universal-Em"} is, after merely reordering coordinates, the product over $\mathcal B$ of $\alpha$ copies of $\mathcal Z$ and $m-\alpha$ copies of $\mathbb{G}_{\mathrm m,\mathcal B}$. Its coordinate ring is free of rank $\delta^\alpha$ over the Laurent polynomial ring in the inactive variables, hence flat over $\mathcal R$. Localization preserves flatness.

Inside the smooth relative torus $\mathbb{G}_{\mathrm m,\mathcal B}^m$, the equations $\mathcal P(y_i)$, $i\in\mathcal A_m$, form a regular sequence. Adjoin them one at a time: each is monic, after multiplying by the unit $b_s^{-1}$, in a variable unused by the preceding equations, hence is a nonzerodivisor. The codimension is $\alpha$, proving the relative lci and dimension claims.

Base change gives [\[eq:Em-definition\]](#eq:Em-definition){reference-type="eqref" reference="eq:Em-definition"} with exactly the two open families. Theorem [\[thm:normalized-classification\]](#thm:normalized-classification){reference-type="ref" reference="thm:normalized-classification"} identifies every such fiber with normalized maximum-dimensional translates. The reconstruction calculation is algebraic over $\mathcal R$, so it commutes with base change. Over $\mathcal B^{\rm sf}$, the root factors are finite étale and the inactive factors are relative tori. Their product is smooth; its open subscheme remains smooth.

[\[prop:completed-fiber\]]{#prop:completed-fiber label="prop:completed-fiber"} Let $\bar b\to\mathcal B$ be a geometric point with algebraically closed residue field $L$, and let $y\in(\mathcal E_m)_{\bar b}(L)$. Enumerate the active indices as $i_1,\ldots,i_\alpha$, and let $\mu_r$ be the multiplicity of $y_{i_r}$ as a root of the specialized polynomial. Then $$\label{eq:completed-fiber}
 \widehat{\mathcal O}_{(\mathcal E_m)_{\bar b},y}
 \simeq
 \frac{L[[t_1,\ldots,t_{m-\alpha},z_1,\ldots,z_\alpha]]}
      {(z_1^{\mu_1},\ldots,z_\alpha^{\mu_\alpha})}.$$ Thus inactive coordinates give the $m-\alpha$ smooth parameters, while each active multiple root gives one truncated parameter with its root multiplicity.

For each active index $i_r$, write in the completed one-variable local ring $$P_{\bar b}(y_{i_r}+z_r)=z_r^{\mu_r}u_r(z_r),\qquad u_r(0)\neq0.$$ The unit $u_r$ can be removed from the ideal. Each inactive torus coordinate supplies an ordinary parameter $t_j$, and different coordinates are independent. Completing their tensor product gives [\[eq:completed-fiber\]](#eq:completed-fiber){reference-type="eqref" reference="eq:completed-fiber"}. Every factor of $\mathcal D_m$ is nonzero at $y$, hence becomes a unit after completion and imposes no new relation.

These statements concern a fixed actual support. On the discriminant boundary we assert the displayed fiber-local equations, but no irreducibility or reducedness theorem for the total family and no description of its complete total singular locus. The root-scheme, discriminant, and lci facts are standard; the recurrence-specific content is their exact identification with the normalized translation scheme.

# Coefficientwise arithmetic sharpness {#sec:partA-arithmetic}

The group in the infinitude statement may depend on the coefficient tuple; that dependence is what *coefficientwise* means.

[\[cor:partA-arithmetic\]]{#cor:partA-arithmetic label="cor:partA-arithmetic"} Let $K_0=\mathbb{Q}(a,c,b_1,\ldots,b_s)\subseteq\Omega$. For every coefficient tuple with the actual support [\[eq:partA-polynomial\]](#eq:partA-polynomial){reference-type="eqref" reference="eq:partA-polynomial"}:

1.  there are a finite algebraic extension $K/K_0$, contained in $\Omega$, and a finitely generated subgroup $\Gamma\leq K^\ast$ for which $$T_{k-1}(S,\Gamma)
     \ \simeq\ V_{k-1}(K)\cap\Gamma^{2k-1}$$ is infinite;

2.  for every finite-rank subgroup $\Lambda\leq\Omega^\ast$, $$T_k(S,\Lambda)
     \ \simeq\ V_k(\Omega)\cap\Lambda^{2k}$$ is finite.

At $m=k-1$, [\[eq:alpha\]](#eq:alpha){reference-type="eqref" reference="eq:alpha"} gives $$\alpha_{k-1}=\min(k-1,1,\nu,k-\nu)=1.$$ Choose a root at the unique active index. It lies in a finite extension $K_1/K_0$. Theorem [\[thm:partA-geometry\]](#thm:partA-geometry){reference-type="ref" reference="thm:partA-geometry"} gives the corresponding nonempty geometric component, and Lemma [\[lem:avoidance\]](#lem:avoidance){reference-type="ref" reference="lem:avoidance"} realizes it as a nonempty open subset of a split torus defined over $K_1$. Its finitely many proper forbidden hypersurfaces do not cover all $K_1$-points because $K_1$ is infinite; after a finite extension if necessary, choose $y\in E_{k-1}(K)$. Proposition [\[prop:reconstruction\]](#prop:reconstruction){reference-type="ref" reference="prop:reconstruction"} gives $$\xi=\xi(y)\in(K^\ast)^{2k-1},\qquad
 \xi H_{k-1}\subseteq V_{k-1}.$$

The split subtorus $H_{k-1}$ has dimension one. Choose a primitive nontrivial cocharacter $$\lambda:\mathbb{G}_{\mathrm m}\longrightarrow H_{k-1},\qquad
 \lambda(t)=(t^{w_0},\ldots,t^{w_{2k-2}})$$ with $w_i\in\mathbb{Z}$. Let $\Gamma$ be generated by $2$, the coefficients, and the finitely many $\xi_i$. For every $n\in\mathbb{Z}$, $$\xi\lambda(2^n)
 =(\xi_i2^{nw_i})_{0\leq i\leq2k-2}
 \in V_{k-1}(K)\cap\Gamma^{2k-1}.$$ These points are distinct because $\lambda$ is nontrivial and $2$ is not a root of unity in characteristic zero. Projection [\[eq:projection-bijection\]](#eq:projection-bijection){reference-type="eqref" reference="eq:projection-bijection"} proves the first claim.

At $m=k$, the delimited anchored dimension theorem, owned by the cited companion manuscript, bounds every contained translate by dimension $k-k=0$. Proposition [\[prop:finite-rank-bridge\]](#prop:finite-rank-bridge){reference-type="ref" reference="prop:finite-rank-bridge"}, whose sole external theorem input is Laurent's qualitative result [@laurent1984equations], then makes the displayed intersection finite, and projection gives the second claim.

This endpoint is qualitative. It supplies no effective cardinality, positive-characteristic assertion, lower-dimensional translate classification, or group uniform across coefficient tuples. The dimension law, its special equality examples, and terminal $k$-window conclusion retain their predecessor ownership; the new assertion here is the coefficientwise lift furnished by the full $E_{k-1}$ classification.

# Exclusive labels and gcd cores {#sec:labels}

Throughout Sections [7](#sec:labels){reference-type="ref" reference="sec:labels"}--[10](#sec:scalar){reference-type="ref" reference="sec:scalar"}, assume $$P(X)=c+bX^d,\qquad a,b,c\in\Omega^\ast,\qquad d\geq2.$$ Set $$\label{eq:g-q-L}
 g=\gcd(k,\nu),\qquad q=\frac{k}{g},\qquad L=\frac{k-\nu}{g}.$$ Then $q\geq2$, $1\leq L<q$, and $\gcd(q,L)=1$. Fix a residue $r\in\{0,\ldots,g-1\}$. Writing an original index as $r+gj$, the recurrence restricted to this residue is $$\label{eq:core-recurrence}
 x_{j+q}=c+b x_{j+L}^{d}+a x_j.$$ Here a subscript denotes the core index; its original coordinate is $r+gj$. On a torus translate $\xi H$, write $$x_j|_{\xi H}=\eta_j\chi^{u_j},\qquad
 \eta_j\in\Omega^\ast,\qquad u_j\in M:=X^\ast(H).$$

[\[lem:exclusive-labels\]]{#lem:exclusive-labels label="lem:exclusive-labels"} For each core equation, exactly one of the following four mutually exclusive character patterns occurs: $$\begin{aligned}
 A&:(u_j,u_{j+L},u_{j+q})=(0,v,dv),&
 B&:(u_j,u_{j+L},u_{j+q})=(v,0,v),\\
 C&:(u_j,u_{j+L},u_{j+q})=(dv,v,0),&
 Z&:(u_j,u_{j+L},u_{j+q})=(0,0,0).
 \end{aligned}$$ where $v\neq0$ in rows $A,B,C$. The scalar conditions are $$\begin{aligned}
 A:\quad&\eta_{j+q}=b\eta_{j+L}^{d},
          &a\eta_j&=-c, \label{eq:label-A}\\
 B:\quad&\eta_{j+q}=a\eta_j,
          &b\eta_{j+L}^{d}&=-c, \label{eq:label-B}\\
 C:\quad&\eta_{j+q}=c,
          &a\eta_j&=-b\eta_{j+L}^{d}, \label{eq:label-C}\\
 Z:\quad&\eta_{j+q}=c+b\eta_{j+L}^{d}+a\eta_j. &&
          \label{eq:label-Z}\end{aligned}$$ Consequently, for the support bit $s_i=0$ when $u_i=0$ and $s_i=1$ otherwise, $$\label{eq:support-recurrence}
 s_{j+q}=s_j+s_{j+L}\qquad\text{in }\mathbb{F}_2.$$

Restriction of [\[eq:core-recurrence\]](#eq:core-recurrence){reference-type="eqref" reference="eq:core-recurrence"} gives $$\label{eq:four-term-identity}
 \eta_{j+q}[u_{j+q}]-c[0]
 -b\eta_{j+L}^{d}[du_{j+L}]-a\eta_j[u_j]=0
 \qquad\text{in }\Omega[M].$$ All four coefficients are nonzero. Lemma [\[lem:character-independence\]](#lem:character-independence){reference-type="ref" reference="lem:character-independence"} says that each character class must occur at least twice. A partition with a block of size three leaves a singleton, so either every term has character zero or the terms split into two pairs.

Pairing future with middle and constant with old gives $u_j=0$, $u_{j+q}=du_{j+L}$, and [\[eq:label-A\]](#eq:label-A){reference-type="eqref" reference="eq:label-A"}; this is $A$ when $v=u_{j+L}\neq0$. Pairing future with old and constant with middle gives $u_{j+L}=0$, $u_{j+q}=u_j$, and [\[eq:label-B\]](#eq:label-B){reference-type="eqref" reference="eq:label-B"}; this is $B$ for $v=u_j\neq0$. Pairing future with the constant and old with middle gives $u_{j+q}=0$, $u_j=du_{j+L}$, and [\[eq:label-C\]](#eq:label-C){reference-type="eqref" reference="eq:label-C"}; this is $C$ for $v=u_{j+L}\neq0$. If every character is zero, the coefficient identity is [\[eq:label-Z\]](#eq:label-Z){reference-type="eqref" reference="eq:label-Z"}. Requiring $v\neq0$ makes the rows disjoint. Reading their support patterns proves [\[eq:support-recurrence\]](#eq:support-recurrence){reference-type="eqref" reference="eq:support-recurrence"}.

[\[lem:gcd-cores\]]{#lem:gcd-cores label="lem:gcd-cores"} The original recurrence equations split into $g$ independent core systems of the form [\[eq:core-recurrence\]](#eq:core-recurrence){reference-type="eqref" reference="eq:core-recurrence"}, one for each residue modulo $g$.

For an original equation index $n=r+gj$, $$n+k=r+g(j+q),\qquad n+k-\nu=r+g(j+L).$$ Thus old, middle, and future have the same residue. Conversely, each original equation has exactly one residue, so different cores do not interact.

[\[prop:colored-heights\]]{#prop:colored-heights label="prop:colored-heights"} Let a finite core word take values in an arbitrary torsion-free character lattice $M$ and satisfy Lemma [\[lem:exclusive-labels\]](#lem:exclusive-labels){reference-type="ref" reference="lem:exclusive-labels"}. Its nonzero positions split into graph components carrying integer heights. Give each component $\mathcal C$ an independent color $e_{\mathcal C}$, and set $$F_i=\begin{cases}
 T^{h_i}e_{\mathcal C},&i\in\mathcal C,\\
 0,&u_i=0.
 \end{cases}$$ Then $F_i$ belongs to $$\mathcal M_{\rm col}
 =\bigoplus_{\mathcal C}\mathbb{F}_2[T,T^{-1}]e_{\mathcal C}$$ and satisfies $$\label{eq:colored-recurrence}
 F_{j+q}=F_j+T F_{j+L}$$ at every core equation.

By Lemma [\[lem:gcd-cores\]](#lem:gcd-cores){reference-type="ref" reference="lem:gcd-cores"}, it is enough to work in one independent core. Take its nonzero positions as vertices. For each active triple, join its two nonzero positions by one directed edge: $$\begin{aligned}
 A&:\ j+L\longrightarrow j+q\quad\text{with weight }1,\\
 B&:\ j\longrightarrow j+q\quad\text{with weight }0,\\
 C&:\ j+L\longrightarrow j\quad\text{with weight }1.
 \end{aligned}$$ An edge of weight $e$ says that the target character is $d^e$ times the source. Traverse an undirected closed walk, assigning the displayed weight forward and its negative backward. If the signed total is $s$, the character relations give $v=d^s v$ in $M\otimes_\mathbb{Z}\mathbb{Q}$ for a nonzero $v$. Torsion-freeness makes $M\to M\otimes\mathbb{Q}$ injective, and $d\geq2$, so $s\neq0$ is impossible. Every closed walk has total weight zero. The edge weights are therefore differences of integer vertex heights, unique up to a constant on each component.

Independent colors are essential: disconnected components may carry equal actual characters without becoming one graph component. Equation [\[eq:colored-recurrence\]](#eq:colored-recurrence){reference-type="eqref" reference="eq:colored-recurrence"} now follows label by label. In $A$, future is $T$ times middle and old is zero. In $B$, future equals old and middle is zero. In $C$, old is $T$ times middle and future is zero, so the two right-hand terms cancel in characteristic two. In $Z$, all three vanish. This proves the identity in the direct sum, without any rank-one hypothesis on $M$.

# Component-height extinction and structural uniqueness {#sec:component-extinction}

[\[lem:minimum-height\]]{#lem:minimum-height label="lem:minimum-height"} Fix one nonzero colored component and choose a vertex of minimum height.

1.  If the equations are indexed by $0\leq j\leq q^2-1$, then some $r\in\{0,\ldots,q-1\}$ satisfies $$\begin{aligned}
     u_{r+jq}&\neq0 &&(0\leq j\leq q-1), \label{eq:full-B-column}\\
     u_{r+tL+jq}&=0 &&(1\leq t\leq q,\ 0\leq j\leq q-t).
     \label{eq:full-zero-triangle}\end{aligned}$$

2.  If the equations are indexed by $0\leq j\leq q^2-2$, then every surviving component has $r=q-1$, and $$\begin{aligned}
     u_{q-1+jq}&\neq0 &&(0\leq j\leq q-1), \label{eq:short-B-column}\\
     u_{q-1+tL+jq}&=0
       &&(1\leq t\leq q-1,\ 0\leq j\leq q-1-t).
     \label{eq:short-zero-triangle}\end{aligned}$$

Every displayed zero is the zero character in the actual lattice $M$, not merely the absence of the selected color.

Let $i$ be a minimum-height vertex. If $i\geq q$, it is the output of the equation indexed by $i-q$. That equation is available because an involved coordinate extends at most $q$ places past the last equation. Its nonzero output makes its label $A$ or $B$. Label $A$ would give a middle vertex one height lower, contradicting minimality. Thus the label is $B$, and the old vertex $i-q$ lies in the same component at the same minimum height. Repetition reaches a minimum-height vertex $r\in\{0,\ldots,q-1\}$.

An equation whose old vertex $u_{r+jq}$ is nonzero and minimum-height cannot have label $A$ or $Z$, whose old character is zero. It cannot have label $C$, whose middle vertex would be one height lower. It is $B$. Hence $$\label{eq:B-persistence-step}
 u_{r+(j+1)q}\neq0,\qquad u_{r+L+jq}=0$$ for every available step. In the full window, all equations $r+jq$, $0\leq j\leq q-1$, occur. This proves [\[eq:full-B-column\]](#eq:full-B-column){reference-type="eqref" reference="eq:full-B-column"} and the first row $u_{r+L+jq}=0$, $0\leq j\leq q-1$, of the triangle. If two entries separated by $q$ in one row are zero, [\[eq:support-recurrence\]](#eq:support-recurrence){reference-type="eqref" reference="eq:support-recurrence"} at the first index forces the intermediate $L$-shifted entry to be zero. Induction on $t$ gives [\[eq:full-zero-triangle\]](#eq:full-zero-triangle){reference-type="eqref" reference="eq:full-zero-triangle"}.

In the shortened window, if $r\leq q-2$, then $$r+(q-1)q\leq q^2-2.$$ The full persistence column and full zero triangle still fit. In particular, the triangle gives $u_{r+qL}=0$, whereas persistence through its $L$-th step gives $u_{r+Lq}\neq0$. Since $qL=Lq$, this is already a contradiction. Therefore a surviving component has $r=q-1$. The available $B$-equations are $q-1+jq$, $0\leq j\leq q-2$. Their outputs give [\[eq:short-B-column\]](#eq:short-B-column){reference-type="eqref" reference="eq:short-B-column"}, and the same triangular induction gives [\[eq:short-zero-triangle\]](#eq:short-zero-triangle){reference-type="eqref" reference="eq:short-zero-triangle"}.

[\[thm:q2-extinction\]]{#thm:q2-extinction label="thm:q2-extinction"} A character word in an arbitrary torsion-free lattice that satisfies $q^2$ consecutive core equations is zero on every involved coordinate.

If a nonzero component existed, Lemma [\[lem:minimum-height\]](#lem:minimum-height){reference-type="ref" reference="lem:minimum-height"} would put $u_{r+qL}=0$ in its full zero triangle. The $B$-persistence column, however, remains nonzero through its $L$-th step, so $u_{r+Lq}\neq0$. The indices agree because $qL=Lq$, a contradiction. The argument applies separately to each color, so no nonzero component exists. It imposes no rank restriction on the ambient character lattice.

For the shortened window put $$\label{eq:Astar-Nstar}
 A_\ast=Lq,\qquad N_\ast=(L+1)q-1.$$

[\[lem:central-coverage\]]{#lem:central-coverage label="lem:central-coverage"} The zero set in [\[eq:short-zero-triangle\]](#eq:short-zero-triangle){reference-type="eqref" reference="eq:short-zero-triangle"} contains every index in $$[A_\ast,N_\ast-1]=[Lq,(L+1)q-2].$$

Fix $s\in\{0,\ldots,q-2\}$. Multiplication by $L$ permutes the nonzero residue classes modulo $q$, so a unique $t\in\{1,\ldots,q-1\}$ satisfies $tL\equiv s+1\pmod q$. Write $$tL=hq+s+1,\qquad j=L-1-h.$$ Then $$\label{eq:central-coverage-index}
 (q-1)+tL+jq=Lq+s.$$ We verify that $(t,j)$ belongs to the shortened triangle. From $tL\leq(q-1)L<Lq$ follows $h\leq L-1$, hence $j\geq0$. Moreover, $$\label{eq:central-lower-bound}
 tL-q(t+L-q)=(q-t)(q-L)>0.$$ If $h\leq t+L-q-1$, then $s+1\leq q-1$ would imply $$tL=hq+s+1
 \leq q(t+L-q-1)+(q-1)<q(t+L-q),$$ contradicting [\[eq:central-lower-bound\]](#eq:central-lower-bound){reference-type="eqref" reference="eq:central-lower-bound"}. Hence $h\geq t+L-q$, so $j=L-1-h\leq q-1-t$. The pair is admissible in [\[eq:short-zero-triangle\]](#eq:short-zero-triangle){reference-type="eqref" reference="eq:short-zero-triangle"}; [\[eq:central-coverage-index\]](#eq:central-coverage-index){reference-type="eqref" reference="eq:central-coverage-index"} makes $u_{Lq+s}=0$. Varying $s$ proves the interval claim.

[\[thm:structural-uniqueness\]]{#thm:structural-uniqueness label="thm:structural-uniqueness"} Suppose a character word satisfies the $q^2-1$ core equations $0\leq j\leq q^2-2$. If it is nonzero, its colored graph has exactly one nonzero component. After shifting its height and suppressing its color, one may normalize $$\label{eq:central-delta-block}
 F_{N_\ast}=1,\qquad
 (F_{A_\ast},F_{A_\ast+1},\ldots,F_{N_\ast})=(0,0,\ldots,0,1).$$ The recurrence [\[eq:colored-recurrence\]](#eq:colored-recurrence){reference-type="eqref" reference="eq:colored-recurrence"} then determines at most one nonzero colored word on the entire involved window.

Lemma [\[lem:minimum-height\]](#lem:minimum-height){reference-type="ref" reference="lem:minimum-height"} says that every surviving component has minimum initial residue $q-1$. Its persistence column contains $$(q-1)+Lq=N_\ast$$ because $1\leq L\leq q-1$. Thus every nonzero component contains the same vertex $N_\ast$. Components have disjoint vertex sets, so exactly one survives.

Lemma [\[lem:central-coverage\]](#lem:central-coverage){reference-type="ref" reference="lem:central-coverage"} kills coordinates $A_\ast,\ldots,N_\ast-1$. Shift the sole component's heights to make $F_{N_\ast}=1$; this gives the central delta block. Those are $q$ consecutive values. The recurrence determines future values from earlier ones. It also gives $$F_j=F_{j+q}+T F_{j+L},$$ so descending induction determines earlier values. This proves uniqueness on the full involved window.

# Laurent shadow, original windows, and seven labels {#sec:laurent-shadow}

[\[prop:laurent-formulas\]]{#prop:laurent-formulas label="prop:laurent-formulas"} The normalized delta block [\[eq:central-delta-block\]](#eq:central-delta-block){reference-type="eqref" reference="eq:central-delta-block"} has unique formal backward and forward continuations under [\[eq:colored-recurrence\]](#eq:colored-recurrence){reference-type="eqref" reference="eq:colored-recurrence"}. Define $$G_t=F_{N_\ast-t},\qquad G(z)=\sum_{t\geq0}G_tz^t.$$ Then $$\label{eq:G-function}
 G(z)=\frac{1+Tz^L}{1+Tz^L+z^q}
     =1+\frac{z^q}{1+Tz^L+z^q},$$ and, for $t\geq q$, $$\label{eq:G-coefficients}
 G_t=\sum_{\substack{\alpha,\beta\geq0\\
                     \alpha q+\beta L=t-q}}
 \left(\binom{\alpha+\beta}{\beta}\bmod2\right)T^\beta.$$ Put $p=q-L$, and define $$H_t=F_{A_\ast+t},\qquad H(z)=\sum_{t\geq0}H_tz^t.$$ Then $$\label{eq:H-function}
 H(z)=\frac{z^{q-1}}{1+Tz^p+z^q},$$ and $$\label{eq:H-coefficients}
 H_t=\sum_{\substack{\alpha,\beta\geq0\\
                     \alpha q+\beta p=t-q+1}}
 \left(\binom{\alpha+\beta}{\beta}\bmod2\right)T^\beta.$$ An empty sum is zero.

The central block gives $G_0=1$ and $G_1=\cdots=G_{q-1}=0$. Backward recurrence gives $G_t=G_{t-q}+T G_{t-L}$ for $t\geq q$. Therefore $$(1+Tz^L+z^q)G(z)=1+Tz^L,$$ which proves [\[eq:G-function\]](#eq:G-function){reference-type="eqref" reference="eq:G-function"}. In the formal power-series ring over $\mathbb{F}_2[T,T^{-1}]$, $$\frac{1}{1+Tz^L+z^q}
 =\sum_{n\geq0}(Tz^L+z^q)^n.$$ Expanding and extracting the coefficient after the leading factor $z^q$ gives [\[eq:G-coefficients\]](#eq:G-coefficients){reference-type="eqref" reference="eq:G-coefficients"}.

Similarly, $H_0=\cdots=H_{q-2}=0$ and $H_{q-1}=1$. For $t\geq q$, the recurrence with output index $A_\ast+t$ reads $H_t=H_{t-q}+T H_{t-p}$. Thus $$(1+Tz^p+z^q)H(z)=z^{q-1},$$ which gives [\[eq:H-function\]](#eq:H-function){reference-type="eqref" reference="eq:H-function"}; expansion of the denominator gives [\[eq:H-coefficients\]](#eq:H-coefficients){reference-type="eqref" reference="eq:H-coefficients"}.

[\[lem:semigroup-uniqueness\]]{#lem:semigroup-uniqueness label="lem:semigroup-uniqueness"} Let $s\geq1$ and $\gcd(q,s)=1$. If $D<qs$, then $$\label{eq:semigroup-representation}
 D=\alpha q+\beta s,\qquad \alpha,\beta\in\mathbb{Z}_{\geq0},$$ has at most one solution.

Two solutions would give $$\alpha-\alpha'=s\ell,\qquad \beta-\beta'=-q\ell$$ for an integer $\ell$. If $\ell>0$, then $\alpha\geq s$, so $D\geq sq$; if $\ell<0$, exchange the solutions. Thus $D<qs$ permits no distinct pair.

[\[cor:unique-shadow\]]{#cor:unique-shadow label="cor:unique-shadow"} The $q^2-1$ core equations have a unique nonzero character shadow, up to the choice of a nonzero character generator. Every involved colored coefficient is zero or a single monomial $T^\beta$. The first additional output coordinate is $$\label{eq:first-collision}
 F_{q^2+q-1}=1+T^q.$$ It is the first collision of two distinct monomials.

The smallest involved coordinate is zero. In [\[eq:G-coefficients\]](#eq:G-coefficients){reference-type="eqref" reference="eq:G-coefficients"}, the largest degree needed backward is $$(N_\ast-0)-q=Lq-1.$$ Since $\gcd(q,L)=1$, Lemma [\[lem:semigroup-uniqueness\]](#lem:semigroup-uniqueness){reference-type="ref" reference="lem:semigroup-uniqueness"} makes each required backward coefficient zero or one monomial. The last coordinate involved by $q^2-1$ equations is $q^2+q-2$. The largest forward degree is $$(q^2+q-2-A_\ast)-q+1=(q-L)q-1=pq-1,$$ and $\gcd(q,p)=1$ gives the same conclusion forward.

Fix nonzero $w$ in a torsion-free lattice and set $$\label{eq:shadow-characters}
 u_i=\begin{cases}d^\beta w,&F_i=T^\beta,\\0,&F_i=0.\end{cases}$$ Equation [\[eq:colored-recurrence\]](#eq:colored-recurrence){reference-type="eqref" reference="eq:colored-recurrence"} yields one of the four exclusive patterns at every triple. If both right-hand monomials occur, the single-monomial property forces equality and cancellation, giving $C$; if one occurs, the label is $A$ or $B$; if neither occurs, it is $Z$. Thus this is a genuine character shadow. Theorem [\[thm:structural-uniqueness\]](#thm:structural-uniqueness){reference-type="ref" reference="thm:structural-uniqueness"} proves uniqueness up to $w$. No scalar lift has been claimed.

At the next output, the degree is $D=pq$. The equation $$\alpha q+\beta p=pq$$ has exactly the solutions $(p,0)$ and $(0,q)$, both with odd binomial coefficient. Formula [\[eq:H-coefficients\]](#eq:H-coefficients){reference-type="eqref" reference="eq:H-coefficients"} gives [\[eq:first-collision\]](#eq:first-collision){reference-type="eqref" reference="eq:first-collision"}. Since $1+T^q$ is neither zero nor a monomial, it cannot represent one character in the surviving component.

[\[prop:original-window\]]{#prop:original-window label="prop:original-window"} Let $\xi H$ be an actual torus translate for the original recurrence, and put $M=X^\ast(H)$.

1.  If $\xi H\subseteq V_{kq}$, then every ambient coordinate character $u_0,\ldots,u_{kq+k-1}$ is zero. Hence $M=0$ and $H$ is trivial.

2.  If $\xi H\subseteq V_{kq-1}$ and $H$ is positive-dimensional, residues $0,\ldots,g-2$ carry only zero characters and residue $g-1$ carries the unique shadow. If $w$ is the character at $N_\ast$ in that residue, then $$\label{eq:actual-character-lattice}
     X^\ast(H)=\mathbb{Z}w.$$ In particular, $w$ is primitive and $\dim H=1$.

Because $k=gq$, one has $kq=gq^2$. At $m=kq$, original equation indices are $0,\ldots,gq^2-1$. Each residue modulo $g$ receives exactly the $q^2$ core equations $j=0,\ldots,q^2-1$. Theorem [\[thm:q2-extinction\]](#thm:q2-extinction){reference-type="ref" reference="thm:q2-extinction"} kills every involved character in each residue, namely core coordinates $0,\ldots,q^2+q-1$. Their union is exactly the original ambient range through $kq+k-1$. Since ambient coordinate restrictions generate the actual lattice $M$, we obtain $M=0$.

At $m=kq-1=gq^2-1$, the original equation indices stop at $gq^2-2$. A residue $r\leq g-2$ contains the $q^2$ equations $j=0,\ldots,q^2-1$, whereas residue $g-1$ contains $j=0,\ldots,q^2-2$. The first $g-1$ residues are extinguished; the last either vanishes or has the unique shadow.

There is no uncovered ambient coordinate. The full cores cover core coordinates through $q^2+q-1$, and the final shortened core through $q^2+q-2$; together they cover every original coordinate through $kq+k-2$. Thus every ambient restriction is zero or $d^\beta w$, while $w$ itself occurs at $N_\ast$. Surjectivity [\[eq:ambient-surjection\]](#eq:ambient-surjection){reference-type="eqref" reference="eq:ambient-surjection"} therefore gives the equality $M=\mathbb{Z}w$, rather than merely a rank-one sublattice of $M$. Hence $w$ is primitive and $H$ has dimension one. This full-window generation step is what excludes unused character directions.

For $q\geq3$, define $$\label{eq:zstar}
 z_\ast=N_\ast-2L=(q-2)L+q-1.$$

[\[lem:seven-labels\]]{#lem:seven-labels label="lem:seven-labels"} For $q\geq3$, the unique shadow has these seven triples: $$\begin{array}{c|c|c}
 j&(F_j,F_{j+L},F_{j+q})&\text{label}\\ \hline
 L-1&(T^{q-1},T^{q-2},0)&C\\
 q-1&(1,0,1)&B\\
 z_\ast-q&(T^2,T,0)&C\\
 z_\ast+L-q&(T,1,0)&C\\
 z_\ast&(0,0,0)&Z\\
 z_\ast+L&(0,1,T)&A\\
 z_\ast+q&(0,T,T^2)&A.
\end{array}$$ Every equation index lies in $[0,q^2-2]$. If two indices coincide for a small parameter choice, both coincident rows have label $C$.

The coefficient formulas and semigroup uniqueness give $$F_{L-1}=T^{q-1},\quad F_{2L-1}=T^{q-2},\quad
 F_{q-1}=1,\quad F_{z_\ast-q}=T^2,\quad
 F_{z_\ast+L-q}=T,\quad F_{N_\ast-q}=1.$$ For instance, $$N_\ast-(L-1)-q=L(q-1),\qquad
 N_\ast-(z_\ast-q)-q=2L,$$ whose unique backward representations are $(0,q-1)$ and $(0,2)$. The other values follow identically. The recurrence gives $$F_{L+q-1}=F_{L-1}+T F_{2L-1}=0,$$ so the first row is $C$, and this zero is the middle entry of the $B$-row at $q-1$.

We prove the zero row at $z_\ast$. Its middle value $F_{z_\ast+L}=F_{N_\ast-L}$ lies in the central zero block. If $2L<q$, then $F_{z_\ast}=G_{2L}=0$; the forward degree for $F_{z_\ast+q}$ is $q-2L$, strictly between $0$ and $p=q-L$, and so has no semigroup representation. If $2L>q$, the backward degree for $F_{z_\ast}$ is $2L-q$, strictly between $0$ and $L$, and $F_{z_\ast+q}=G_{2L-q}=0$. The equality $2L=q$ would force $L=1,q=2$ by coprimality, contrary to $q\geq3$. Thus the entire row is zero.

The forward formula gives $F_{N_\ast+p}=T$ and $F_{N_\ast+2p}=T^2$. Together with $F_{N_\ast-L}=0$ and $F_{N_\ast}=1$, these are the last two $A$-rows. The two other $C$-rows follow from the computed values and the recurrence.

Finally, $$z_\ast-q=(q-2)L-1\geq0,\qquad
 q^2-2-(z_\ast+q)=(q-2)(q-L)-1\geq0.$$ All seven indices lie between these bounds. Put $$a=L-1,\quad b=q-1,\quad c=(q-2)L-1,\quad d=(q-1)L-1,$$ and let $e=c+q$, $f=d+q$, and $h=e+q$. Then $$a\leq c<d<e<f<h,$$ because $c-a=(q-3)L$, $d-c=L$, $e-d=q-L$, $f-e=L$, and $h-f=q-L$. Equality $a=c$ occurs exactly when $q=3$, and both rows are $C$. The remaining index $b$ is distinct from this chain: equality $b=c$ would give $q=(q-2)L$, which with $\gcd(q,L)=1$ forces $q\mid2$, while equality $b=d$ would give $q=(q-1)L$, which forces $q\mid L$; both contradict $q\geq3$ and $L<q$. Also $b>a$ and $e>b$. Hence the sole possible coincidence identifies two $C$-rows, and no scalar rule conflicts.

# Scalar obstruction, $q=2$ fill, and arithmetic consequences {#sec:scalar}

[\[thm:scalar-obstruction\]]{#thm:scalar-obstruction label="thm:scalar-obstruction"} Assume $q\geq3$. Then $V_{kq-1}$ contains no positive-dimensional torus translate.

Suppose $\xi H\subseteq V_{kq-1}$ with $H$ positive-dimensional. Proposition [\[prop:original-window\]](#prop:original-window){reference-type="ref" reference="prop:original-window"} forces the unique shadow in residue $g-1$, so all seven rows in Lemma [\[lem:seven-labels\]](#lem:seven-labels){reference-type="ref" reference="lem:seven-labels"} obey the scalar rules in Lemma [\[lem:exclusive-labels\]](#lem:exclusive-labels){reference-type="ref" reference="lem:exclusive-labels"}.

The $C$-label at $L-1$ gives $\eta_{q+L-1}=c$. The $B$-label at $q-1$ uses the same coordinate as its middle scalar and gives $b\eta_{q+L-1}^d=-c$. Therefore $$\label{eq:first-scalar-obstruction}
 bc^{d-1}=-1.$$ The $C$-label at $z_\ast+L-q$ gives $\eta_{z_\ast+L}=c$. The $A$-label at $z_\ast+L$ uses this coordinate as its old scalar, so $a\eta_{z_\ast+L}=-c$, whence $$\label{eq:second-scalar-obstruction}
 a=-1.$$ The $C$-labels at $z_\ast-q$ and $z_\ast+L-q$ give $$\eta_{z_\ast}=c,\qquad \eta_{z_\ast+L}=c.$$ The old-scalar rule in the $A$-label at $z_\ast+q$, together with $a=-1$, gives $\eta_{z_\ast+q}=c$. The $Z$-equation at $z_\ast$ is the full scalar recurrence, so $$c=\eta_{z_\ast+q}
   =c+b\eta_{z_\ast+L}^d+a\eta_{z_\ast}
   =c+bc^d+ac=-c.$$ Thus $2c=0$, contrary to characteristic zero and $c\neq0$.

#### The false-sharpness boundary.

Theorem [\[thm:scalar-obstruction\]](#thm:scalar-obstruction){reference-type="ref" reference="thm:scalar-obstruction"} rules out the false implication from the unique $q^2-1$ character shadow to a universal scalar lift. For $q\geq3$, it is a universal obstruction at the penultimate character window, equivalently a one-step improvement over the $q^2$-equation character-extinction bound. It constructs no survivor in a shorter window and therefore proves no exact, optimal, shortest, minimal, or sharp scalar escape threshold.

[\[thm:q2-resonance\]]{#thm:q2-resonance label="thm:q2-resonance"} Assume $q=2$. Then $L=1$, and $V_{kq-1}$ contains a positive-dimensional torus translate if and only if $$\label{eq:q2-resonance}
 a=-1,\qquad bc^{d-1}=-1.$$ Whenever these equalities hold, such a translate may be chosen with a saturated one-dimensional underlying subtorus, for every $g\geq1$. At $V_{kq}$, no positive-dimensional translate exists.

Coprimality and $1\leq L<2$ force $L=1$. The unique three-equation shadow is $$(F_0,F_1,F_2,F_3,F_4)=(T,1,0,1,T),$$ or in character form $$\label{eq:q2-character-word}
 (u_0,u_1,u_2,u_3,u_4)=(dw,w,0,w,dw).$$ Its labels are $C,B,A$. The $C$-output and the $B$-middle are the shared scalar $\eta_2=c$, so $bc^d=-c$, giving $bc^{d-1}=-1$. The same $C$-output is the old scalar in $A$, so $ac=-c$, giving $a=-1$. This proves necessity.

Conversely assume [\[eq:q2-resonance\]](#eq:q2-resonance){reference-type="eqref" reference="eq:q2-resonance"}. For $s\in\Omega^\ast$, put $$\label{eq:q2-five-scalars}
 \eta_0=bs^d,\quad \eta_1=s,\quad \eta_2=c,\quad
 \eta_3=-s,\quad \eta_4=b(-s)^d.$$ For $\tau\in\mathbb{G}_{\mathrm m}$, set $x_i=\eta_i\tau^{e_i}$ with $$(e_0,e_1,e_2,e_3,e_4)=(d,1,0,1,d).$$ The three equations are $$c+b(s\tau)^d-bs^d\tau^d=c,\qquad
 c+bc^d-s\tau=-s\tau,\qquad
 c+b(-s\tau)^d-c=b(-s)^d\tau^d.$$ Thus the active core is a translate with [\[eq:q2-character-word\]](#eq:q2-character-word){reference-type="eqref" reference="eq:q2-character-word"}. The exponent vector contains $1$, so it is primitive and the resulting one-dimensional subtorus is closed and saturated.

For $g=1$ this is the full original window. Suppose $g>1$. The active core occupies residue $g-1$. Each earlier residue has zero characters and needs a nonzero scalar segment satisfying four core equations, hence six nonzero scalar coordinates. Under $a=-1$, define $$\label{eq:Phi}
 \Phi(x,y)=(y,c+by^d-x),$$ with polynomial inverse $$\label{eq:Phi-inverse}
 \Phi^{-1}(u,v)=(c+bu^d-v,u).$$ If $\Phi^j(y_0,y_1)=(y_j,y_{j+1})$, then $y_{j+2}=c+by_{j+1}^d-y_j$. Each coordinate of every required forward or inverse iterate is a nonzero polynomial because it is a coordinate of a polynomial automorphism. Add the two initial coordinate functions. Their finitely many zero sets are proper hypersurfaces of $\mathbb{A}^2$, whose union cannot cover $\mathbb{A}^2$ over the infinite field $\Omega$. Choose $(y_0,y_1)$ outside the union, so all six required coordinates are nonzero. Make this choice independently in every inactive residue. Lemma [\[lem:gcd-cores\]](#lem:gcd-cores){reference-type="ref" reference="lem:gcd-cores"} shows that the residues do not interact. Combining their constant scalar segments with the active translate produces the required full translate for arbitrary $g$, without adding any character direction.

Finally, $V_{kq}$ has $q^2$ core equations in every residue. Theorem [\[thm:q2-extinction\]](#thm:q2-extinction){reference-type="ref" reference="thm:q2-extinction"} and Proposition [\[prop:original-window\]](#prop:original-window){reference-type="ref" reference="prop:original-window"} exclude positive-dimensional translates there. For $g=1$, the $CBA$ construction recovers the planar endpoint proved in the anonymous companion manuscript [@companionSupport]; that specialization is cited for provenance, not claimed as new.

[\[cor:finite-rank-consequences\]]{#cor:finite-rank-consequences label="cor:finite-rank-consequences"} Let the recurrence be defined over a characteristic-zero field $K$, and let $\Gamma\leq K^\ast$ have finite rank with arbitrary torsion.

1.  For every $q\geq2$, $T_{kq}(S,\Gamma)$ is finite.

2.  If $q\geq3$, $T_{kq-1}(S,\Gamma)$ is finite.

3.  If $q=2$ and [\[eq:q2-resonance\]](#eq:q2-resonance){reference-type="eqref" reference="eq:q2-resonance"} fails, $T_{kq-1}(S,\Gamma)$ is finite.

4.  If $q=2$ and [\[eq:q2-resonance\]](#eq:q2-resonance){reference-type="eqref" reference="eq:q2-resonance"} holds, then after a compatible finite extension of $K$ there is a compatible finitely generated group $\Gamma'$ for which $T_{kq-1}(S,\Gamma')$ is infinite while $T_{kq}(S,\Gamma')$ is finite.

Every conclusion is qualitative.

At $m=kq$, Proposition [\[prop:original-window\]](#prop:original-window){reference-type="ref" reference="prop:original-window"} excludes positive-dimensional translates. For $q\geq3$, Theorem [\[thm:scalar-obstruction\]](#thm:scalar-obstruction){reference-type="ref" reference="thm:scalar-obstruction"} does so at $m=kq-1$. For $q=2$ off [\[eq:q2-resonance\]](#eq:q2-resonance){reference-type="eqref" reference="eq:q2-resonance"}, the necessity half of Theorem [\[thm:q2-resonance\]](#thm:q2-resonance){reference-type="ref" reference="thm:q2-resonance"} excludes the sole possible nonzero shadow. Proposition [\[prop:finite-rank-bridge\]](#prop:finite-rank-bridge){reference-type="ref" reference="prop:finite-rank-bridge"}, using Laurent's qualitative torus theorem [@laurent1984equations], gives the three finiteness claims. Arbitrary torsion and the finitely generated field reduction are already included in that bridge.

On the resonant $q=2$ locus, carry out the construction over an algebraic closure of the coefficient field. Its finitely many translating scalars lie in a finite extension $K'/K$. Let $\Gamma'\leq(K')^\ast$ be generated by those scalars and $2$. Characteristic zero makes $2$ infinite-order. The substitutions $\tau=2^N$, $N\geq0$, give pairwise distinct points with all coordinates in $\Gamma'$. The projection bijection [\[eq:projection-bijection\]](#eq:projection-bijection){reference-type="eqref" reference="eq:projection-bijection"} makes $T_{kq-1}(S,\Gamma')$ infinite, while the first part keeps $T_{kq}(S,\Gamma')$ finite. Laurent's theorem enters only after the geometric statements and provides no effective count or algorithm.

#### Scope of Part B.

The proof uses characteristic zero, $a,b,c\neq0$, and $d\geq2$ at the stated places. It asserts no positive-characteristic, zero-coefficient, linear-support, rational-support, Laurent-support, or arbitrary-automorphism extension. It classifies neither lower-dimensional nor inclusion-maximal translates, assigns no geometric dimension to $T_m$, and provides no effective enumeration, height theorem, or periodic-point classification.

# Related work, ownership limits, and conclusion {#sec:conclusion}

The contained-translate question sits beside several established subjects but has different quantifiers. Work on subvarieties of tori and intersections with algebraic subgroups provides the ambient language [@habegger2008intersecting; @suciuyangzhao2013intersections]; results on lacunary polynomials, unlikely intersections, torsion cosets, and torsion-point algorithms address nearby sparse systems [@corvajalevinzannier2021intersections; @amorososombrazannier2017unlikely; @martinez2019torsion; @leroux2012torsion; @dillgallinaro2025likely]. Those problems concern intersections, exceptional loci, or torsion phenomena rather than classifying an entire translate contained in a finite shift-like recurrence window. Likewise, projective Fano schemes motivate why our explicit normalized affine scheme should not be given a Hilbert--Fano interpretation [@iltenzotine2017fano; @iltenkelly2022fano].

Arithmetic-dynamical work on $S$-units, orbit--subgroup intersections, cyclotomic points, multiplicative dependence, and rank-two recurrences asks related but distinct fixed-orbit or density questions [@bellchenhossain2021rational; @bellghioca2024orbits; @jixiezhang2025cyclotomic; @melloyasufuku2026integrality; @zhang2026ranktwo]. Here the initial state varies and the finite survivor variety itself is the object. A bounded primary-source comparison through 19 August 2026 found no direct collision with the combined normalized-scheme classification and gcd scalar obstruction. This is not a priority claim: unindexed, non-English, unpublished, and private work remain unresolved.

Three anonymous companion manuscripts delimit provenance. The dimension law and terminal anchored finiteness used here belong to *Sharp Torus-Coset Decay for Sparse Shift-Like Recurrences: Constant Anchors and the Exact Zero-Constant Boundary* [@companionDecay]. The planar $CBA$ endpoint belongs to *Support Size and Finite-Rank Torus Escape for Generalized Hénon Maps* [@companionSupport]. *Marked Trace Coordinates and Scheme-Theoretic Ramification at the Polynomial Boundary of Generalized Hénon Maps* studies a different marked trace problem; the shared scheme-theoretic vocabulary does not supply a theorem used here [@companionTrace]. Laurent's theorem is the sole external imported theorem, while the first companion is the only delimited nonlocal recurrence input.

The common conclusion is a separation principle. Character identities determine a candidate subgroup or shadow; scalar equations decide containment. In Part A, equality in the anchored dimension bound rigidifies the subgroup, and the remaining lift problem is the explicit normalized scheme $E_m$, nonempty coefficient by coefficient and geometrically controlled over the fixed-support coefficient torus. In Part B, arbitrary-rank component colors first prove extinction and uniqueness without assuming a rank-one ambient torus; only after the original-coordinate coverage step does the actual lattice become $\mathbb{Z}w$. Seven scalar labels then obstruct the penultimate shadow for $q\geq3$, whereas $q=2$ lifts precisely on its resonant coefficient locus.

All conclusions retain their stated boundaries. There is no classification of lower-dimensional translates, no Hilbert or Fano moduli theorem, no effective count, no positive-characteristic assertion, and no exact scalar escape threshold for $q\geq3$. These limits are not ancillary: they mark exactly where the character problem ends and the scalar lifting problem begins.
