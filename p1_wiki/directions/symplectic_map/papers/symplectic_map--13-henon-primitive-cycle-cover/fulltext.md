---
p1_kind: "derived-fulltext-reading-copy"
route: "symplectic_map"
logical_paper_id: "symplectic_map--13-henon-primitive-cycle-cover"
canonical_tex: "symplectic_map/papers/13-henon-primitive-cycle-cover/paper/main.tex"
canonical_pdf: "symplectic_map/papers/13-henon-primitive-cycle-cover/paper/main.pdf"
source_sha256: "f62f72ad129bc371d0e76d1daf48b0a2df82cf60d0d1e750d6c0f049047539ce"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Normalized Primitive-Cycle Covers in a Degenerating Hénon Family

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symplectic_map/papers/13-henon-primitive-cycle-cover>)
- [规范 TeX](<../../../../../symplectic_map/papers/13-henon-primitive-cycle-cover/paper/main.tex>)
- [关联 PDF](<../../../../../symplectic_map/papers/13-henon-primitive-cycle-cover/paper/main.pdf>)
- [支撑 Markdown](<../../../../../symplectic_map/papers/13-henon-primitive-cycle-cover/notes/CLAIMS_EVIDENCE_MATRIX.md>)
- [BibTeX](<../../../../../symplectic_map/papers/13-henon-primitive-cycle-cover/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For fixed integers $d,n\geq2$, we study the normalized family $H_{a,c}(x,y)=(ay+x^d+c,x)$ through the generic block of points of actual exact period $n$. The full cyclic fixed algebra is free of rank $d^n$, while the actual-period block is a field of Möbius degree $\nu=\sum_{e\mid n}\mu(n/e)d^e$. We prove that its relative normalization over $\mathbb{Q}[a,c]$ is geometrically integral and finite locally free of rank $\nu$, and that specialization to $a=0$ is exactly the reduced scalar dynatomic algebra, rather than an equality inferred from an unproved normalization--base-change principle. The proof isolates the generic idempotent by a Henselian lift and controls the scalar divisor through a unique prime of ramification index one, an $R_0+S_1$ argument, and a finite birational comparison; Reynolds averaging then gives the corresponding cycle quotient. On a common dense finite-étale open, the geometric monodromy on the $r=\nu/n$ cycles is the full symmetric group $S_r$. As a narrower second conclusion, the orbit sum and the pointwise trace of the ordered derivative return map separately generate the generic cycle field; their multiplication characteristic polynomials are integral and basis-free, and the exceptional case $(d,n)=(2,2)$ is explicitly linear.
author:
- Anonymous Authors
bibliography:
- references.bib
title: 'Normalized Primitive-Cycle Covers in a Degenerating Hénon Family'
```

## Markdown 正文

# Introduction {#sec:introduction}

The specialization $a=0$ turns $$H_{a,c}(x,y)=(ay+x^d+c,x)$$ into the scalar iteration $f_c(z)=z^d+c$, written in two consecutive orbit coordinates. Scalar dynatomic curves therefore form a natural boundary of this two-parameter family. Carrying that boundary into an integral model is not, however, a matter of inserting $a=0$ into a generic formula. The full fixed scheme contains lower-period points, actual exact period is a clopen condition only after passing to the generic finite-étale algebra, and the normalization of that generic block need not commute formally with specialization. Our main result constructs the relative normalization and identifies its scalar fiber scheme-theoretically.

Three points make the construction delicate. To begin, a dynatomic equation records formal period on special fibers, where its points can have smaller least period; this familiar phenomenon rules out an everywhere embedded "actual-period part" of the full fixed scheme [@hutz-2010-dynatomic-cycles]. We consequently isolate actual period by an idempotent only over the generic field. Second, even a finite flat normalization can acquire multiplicity or closed-point nilpotents after specialization. The equality with the scalar dynatomic algebra must pass through the unique prime above $(a)$, ramification index one, reducedness of the entire divisor, and a normal finite-birational comparison. Third, the scalar monodromy group maps into the global monodromy group. Thus the scalar image gives a lower bound only through the map from the scalar good locus to the global good locus, in that direction.

The construction keeps four algebras separate. The algebra $B_n$ describes all points fixed by $H_{a,c}^n$ in cyclic orbit coordinates. Inside its generic finite-étale algebra, an idempotent cuts out the actual-period block $E_n$. The integral closure $S$ of the parameter ring in this field is the normalized marked-point model, and $S_0=S^{C_n}$ is its affine cycle quotient. In compressed form the argument runs $$B_n\longrightarrow E_n\longrightarrow S\longrightarrow S_0
 \longrightarrow (\tau,\rho),$$ but these arrows stand for different operations: generic idempotent extraction, relative normalization, invariants, and evaluation of cycle functions. They do not describe one primitive subscheme embedded in every fiber.

The scalar geometric inputs are established results. Gao and Ou prove smoothness and geometric irreducibility of the unicritical affine dynatomic curves [@gao-ou-2014-dynatomic]. Morton proves the full scalar wreath group in every degree [@morton-1998-periodic-galois], and Fakhruddin's characteristic-zero formulation supplies the geometric constant-field version [@fakhruddin-2014-generic-endomorphisms]. Morton also proves that the scalar multiplier generates the scalar cycle field for all $d,n$ and that the scalar orbit sum does so when $d=2$ [@morton-1996-algebraic-curves]. Our coordinate theorem is therefore a subordinate layer: it lifts the two named functions to the two-parameter cycle field, treats the orbit sum uniformly for $d\geq3$, and constructs their integral characteristic polynomials. Recent trace-spectrum rigidity for fixed-degree Hénon maps concerns a different reconstruction problem, based on whole multisets of formal-period traces over finitely many periods [@cantat-dujardin-2026-multiplier-rigidity].

The contributions are the following.

1.  We prove that the generic actual-period field has a geometrically integral, finite-locally-free normalization over $\mathbb{Q}[a,c]$, and that its scheme-theoretic scalar fiber is exactly the normal affine scalar dynatomic algebra. The proof includes the divisor and nilpotent-exclusion steps needed for this equality.

2.  We form the affine cycle quotient by a Reynolds projector, prove arbitrary base-change compatibility for these invariants, and transfer the scalar wreath theorem to obtain full geometric cycle monodromy $S_r$ on a dense finite-étale open.

3.  As a narrower consequence, we prove separately that the orbit sum $\tau$ and the pointwise derivative-return trace $\rho$ generate the generic cycle field. Their multiplication polynomials are defined on the determinant line, and the rank-one case $(d,n)=(2,2)$ is calculated directly.

The proofs are entirely algebraic. Section [2](#sec:objects){reference-type="ref" reference="sec:objects"} fixes the four models and states the main results. Sections [3](#sec:fixed){reference-type="ref" reference="sec:fixed"}--[5](#sec:quotient){reference-type="ref" reference="sec:quotient"} construct the actual-period field, its normalization, exact scalar fiber, and quotient monodromy. Section [6](#sec:coordinates){reference-type="ref" reference="sec:coordinates"} treats the two cycle coordinates, while Section [7](#sec:prior){reference-type="ref" reference="sec:prior"} records the precise boundaries with scalar and low-period work. Appendices [9](#app:local){reference-type="ref" reference="app:local"}--[11](#app:det){reference-type="ref" reference="app:det"} give the local-algebra, scalar-branch, and determinant-line details.

# The family, its models, and the main results {#sec:objects}

## Orbit coordinates and the full fixed algebra

Fix integers $d,n\geq2$ throughout. Set $$A=\mathbb{Q}[a,c],\qquad K=\mathbb{Q}(a,c),\qquad
 H_{a,c}(x,y)=(ay+x^d+c,x).$$ Indices are read modulo $n$. If a periodic orbit is marked so that $(z_i,z_{i-1})$ maps to $(z_{i+1},z_i)$, its cyclic equations are $$\label{eq:cyclic-equations}
 g_i=z_i^d+az_{i-1}+c-z_{i+1}=0,
 \qquad i\in\mathbb Z/n\mathbb Z.$$ We define $$\label{eq:Bn}
 B_n=A[z_0,\ldots,z_{n-1}]/(g_0,\ldots,g_{n-1}).$$ This is the full cyclic fixed algebra: it parametrizes points fixed by $H_{a,c}^n$ and includes orbits whose least period properly divides $n$. The time shift $\sigma(z_i)=z_{i+1}$ acts on $B_n$.

Write $$\label{eq:nu-r}
 \nu=\nu_d(n)=\sum_{e\mid n}\mu(n/e)d^e,
 \qquad r=r_d(n)=\frac{\nu}{n}.$$ Here $\nu$ is the generic count of marked points of actual period $n$, and $r$ is the corresponding count of cycles.

## The generic actual-period block and relative models

The generic algebra $B_n\otimes_AK$ will be finite étale. Over $\overline{K}$, its points form a finite discrete Galois set. The points of least period exactly $n$ form a Galois-stable clopen subset, hence determine an idempotent $e_n$. We put $$\label{eq:En}
 E_n=e_n(B_n\otimes_AK).$$ The adjective *actual* always refers to this generic clopen block. It will be proved that $E_n$ is a field of degree $\nu$, not merely a product of fields.

Let $S$ be the integral closure of $A$ in $E_n$, and put $$\label{eq:S0F}
 S_0=S^{\langle\sigma\rangle},\qquad
 F=\operatorname{Frac}(S_0)=E_n^{\langle\sigma\rangle}.$$ On the scalar line $a=0$, let $f_c(z)=z^d+c$ and let $\Phi_{d,n}(z,c)$ be its $n$th dynatomic polynomial. We use only the affine algebras $$\label{eq:Dn}
 D_n=\mathbb{Q}[c,z]/(\Phi_{d,n}(z,c)),
 \qquad D_n^{C_n}.$$ No projective compactification is implicit in this notation.

## Two cycle observables

Set $$\label{eq:observables}
 u_i=d z_i^{d-1},\qquad
 M_i=DH_{a,c}(z_i,z_{i-1})=
 \begin{pmatrix}u_i&a\\1&0\end{pmatrix},$$ and define $$\label{eq:tau-rho}
 \tau=\sum_{i=0}^{n-1}z_i,
 \qquad
 \rho=\operatorname{tr}(M_{n-1}\cdots M_0).$$ Thus $\rho$ is the matrix trace of the derivative return map at a periodic point. It is neither the field trace $\operatorname{Tr}_{F/K}$ nor the determinant $(-a)^n$. For later use, direct multiplication at $n=2$ gives $$\label{eq:n2-matrix-check}
 \operatorname{tr}(M_1M_0)=u_0u_1+2a.$$

## Main results

[\[thm:A\]]{#thm:A label="thm:A"} For fixed $d,n\geq2$, the following statements hold.

1.  The algebra $B_n$ is a free $A$-module of rank $d^n$, with basis $$\left\{\prod_{i=0}^{n-1}z_i^{e_i}:0\leq e_i<d\right\}.$$

2.  The generic actual-period block $E_n$ is a field of degree $\nu$ over $K$.

3.  The integral closure $S$ is finite locally free of rank $\nu$ over $A$, and $\operatorname{Spec}S$ is geometrically integral over $\mathbb{Q}$.

4.  The scheme-theoretic scalar fiber is exactly $S/aS\simeq D_n$.

5.  The invariant algebra $S_0$ is finite locally free of rank $r$; invariants commute with arbitrary base change, and $S_0/aS_0\simeq D_n^{C_n}$.

6.  On a common dense open on which the marked-point and cycle covers are finite étale, the geometric monodromy on the $r$ cycles is $S_r$. When $r=1$, this means the trivial group $S_1$.

The proof proceeds in three blocks. A monic coefficient-ring Gröbner basis gives the full fixed algebra, and a Henselian lift of the scalar exact factor proves that the generic idempotent block is one field. Excellence, normal-surface Cohen--Macaulayness, and miracle flatness construct $S$; a multiplicity-one $a$-adic divisor and a finite birational comparison then identify its exact scalar fiber. Finally, Reynolds averaging constructs the cycle quotient, and the scalar full-wreath theorem enters the global cover through the correctly directed restriction map.

[\[thm:B\]]{#thm:B label="thm:B"} Let $F=\operatorname{Frac}(S_0)$ and let $\tau,\rho$ be as in [\[eq:tau-rho\]](#eq:tau-rho){reference-type="eqref" reference="eq:tau-rho"}. Then $$K(\tau)=F=K(\rho).$$ For $s\in\{\tau,\rho\}$, multiplication by $s$ on $S_0$ has a canonical characteristic polynomial $$\chi_s(T)=\det(T\operatorname{id}_{S_0}-m_s)\in A[T],$$ defined on $\bigwedge_A^rS_0$. Its generic polynomial is irreducible of degree $r$ over $K$.

The two generation statements are proved separately. Scalar branches at infinity distinguish $\tau$ by a root-of-unity word sum and distinguish $\rho$ by an independently derived inverse word product. Full $S_r$ monodromy converts each non-base statement into primitivity via the maximality of a point stabilizer. The determinant-line construction then keeps the integral characteristic polynomial independent of a choice of basis.

[\[prop:C\]]{#prop:C label="prop:C"} For $(d,n)=(2,2)$, $$\nu=2,\qquad r=1,\qquad \tau=a-1,$$ and $$z_0z_1=(a-1)^2+c,\qquad
 \rho=4a^2-6a+4+4c.$$ Both multiplication characteristic polynomials are linear. This case provides neither a non-base assertion nor nontrivial monodromy evidence.

[\[fig:architecture\]]{#fig:architecture label="fig:architecture"}

# The full fixed algebra and the generic actual-period field {#sec:fixed}

## A monic cyclic Gröbner basis

The initial algebraic step is integral: no generic rank computation is needed.

[\[lem:groebner\]]{#lem:groebner label="lem:groebner"} For any graded monomial order in the variables $z_0,\ldots,z_{n-1}$, with $A$ treated as the coefficient ring, the polynomials $g_i$ in [\[eq:cyclic-equations\]](#eq:cyclic-equations){reference-type="eqref" reference="eq:cyclic-equations"} form a monic Gröbner basis. Their standard monomials are precisely $\prod_i z_i^{e_i}$ with $0\leq e_i<d$.

Because the order is graded and $d\geq2$, the degree-$d$ term dominates all terms of degree at most one, so $\operatorname{LM}(g_i)=z_i^d$. These leading monomials are pairwise coprime and their leading coefficients are one. For $i\ne j$, the product criterion applies over $A$: the $S$-polynomial $$S(g_i,g_j)=z_j^d g_i-z_i^d g_j$$ has its two remaining leading contributions divisible by $z_i^d$ or $z_j^d$, and monic division reduces it to zero. Buchberger's criterion in its monic coefficient-ring form therefore applies without inverting any element of $A$.

Repeated monic division reduces every polynomial to an $A$-linear combination of monomials in which every exponent is smaller than $d$. Uniqueness follows because a nonzero element of the ideal has leading monomial divisible by some $z_i^d$, whereas no nonzero combination of these standard monomials does. The residue classes of the standard monomials are therefore an $A$-basis.

Lemma [\[lem:groebner\]](#lem:groebner){reference-type="ref" reference="lem:groebner"} proves Theorem [\[thm:A\]](#thm:A){reference-type="ref" reference="thm:A"}(1), including $$\label{eq:Bn-rank}
 \operatorname{rank}_A B_n=d^n.$$ In particular $B_n$ is finite flat over $A$. This conclusion concerns the full fixed algebra and does not yet separate any period divisor.

## Generic étale decomposition and the actual-period idempotent

On the scalar line, the recurrence $z_{i+1}=z_i^d+c$ identifies the full fixed algebra over $\mathbb{Q}(c)$ with $$\mathbb{Q}(c)[z]/(f_c^n(z)-z).$$ Its dynatomic factors are separable and pairwise coprime at the generic parameter. One scalar fiber of the finite-flat discriminant is thus étale, and the discriminant is not the zero element of $A$. It follows that $B_n\otimes_AK$ is a finite étale $K$-algebra.

[\[lem:idempotent\]]{#lem:idempotent label="lem:idempotent"} The actual least-period-$n$ points in $\operatorname{Spec}(B_n\otimes_A\overline{K})$ determine a unique $K$-rational idempotent $e_n$. The corresponding factor $E_n$ has $K$-dimension $$\dim_K E_n=\sum_{e\mid n}\mu(n/e)d^e=\nu.$$

A finite étale algebra over $\overline{K}$ is a product of copies of $\overline{K}$, so any subset of its geometric points is clopen. Least period is preserved by the absolute Galois action, and the subset of least-period-$n$ points is therefore Galois stable. Descent for idempotents produces a unique idempotent in $B_n\otimes_AK$. If $N_e$ denotes the number of points whose least period is $e$, then $d^n=\sum_{e\mid n}N_e$, since the scalar generic fiber of $f_c^n(z)-z$ has degree $d^n$ and simple roots. Möbius inversion gives $N_n=\nu$, which is the dimension of the idempotent factor.

The construction in Lemma [\[lem:idempotent\]](#lem:idempotent){reference-type="ref" reference="lem:idempotent"} is deliberately generic. A formal-period point may meet a lower-period locus after specialization, so the lemma does not produce an open-and-closed actual-period subscheme of $\operatorname{Spec}B_n$ over all of $\operatorname{Spec}A$.

## The Henselian connected lift

It remains to show that $E_n$ is one field. Let $$R=A_{(a)}=\mathbb{Q}[c,a]_{(a)}.$$ This is a discrete valuation ring with uniformizer $a$, fraction field $K$, and residue field $k=\mathbb{Q}(c)$. Write $R^h$ for its henselization.

The special full fixed algebra is finite étale over $k$. Since $B_n$ is finite free over $R$, the vanishing of the relative differentials after reduction and Nakayama's lemma show that $B_n\otimes_AR$ is finite étale over $R$. The scalar exact factor is $$\label{eq:scalar-exact-field}
 k[z]/(\Phi_{d,n}(z,c)).$$ It is a field by the geometric irreducibility of the scalar dynatomic curve [@gao-ou-2014-dynatomic]. Finite étale algebras over a Henselian pair are equivalent to finite étale algebras over its residue field [@stacks-0d49]; hence the idempotent of [\[eq:scalar-exact-field\]](#eq:scalar-exact-field){reference-type="eqref" reference="eq:scalar-exact-field"} lifts uniquely to a finite étale $R^h$-algebra $C$.

[\[lem:henselian-field\]]{#lem:henselian-field label="lem:henselian-field"} The algebra $C$ is a domain, its generic fiber $C[1/a]$ is a field, and $$E_n\otimes_K\operatorname{Frac}(R^h)\simeq C[1/a].$$ Consequently $E_n$ is a field of degree $\nu$ over $K$.

The residue algebra of $C$ is the field in [\[eq:scalar-exact-field\]](#eq:scalar-exact-field){reference-type="eqref" reference="eq:scalar-exact-field"}. Idempotents lift uniquely in a Henselian pair, so $C$ has no nontrivial idempotent and is connected. A finite étale algebra over the normal local domain $R^h$ is normal; a connected normal ring is a domain. Localizing preserves the domain property, and a finite-dimensional domain over the field $\operatorname{Frac}(R^h)$ is a field.

We next identify the lifted factor. If a generic point belongs to a lower-period factor, then for some proper divisor $e\mid n$ it satisfies the closed equation $H^e(P)=P$. Every specialization of that point satisfies the same equation and therefore cannot enter the scalar least-period-$n$ factor. Conversely, the lift of the scalar exact factor is disjoint from all lifted lower-period idempotents. The idempotent-extension argument in Lemma [\[lem:appendix-idempotent-identification\]](#lem:appendix-idempotent-identification){reference-type="ref" reference="lem:appendix-idempotent-identification"} therefore places $C[1/a]$ as a direct subfactor of $E_n\otimes_K\operatorname{Frac}(R^h)$. The two factors have the same dimension: $$\dim_{\operatorname{Frac}(R^h)}C[1/a]=\operatorname{rank}_{R^h}C=\nu
 =\dim_{\operatorname{Frac}(R^h)}(E_n\otimes_K\operatorname{Frac}(R^h)).$$ Hence the subfactor is the whole actual-period block, proving the displayed isomorphism.

If $E_n$ were a product of two nonzero $K$-algebras, its nontrivial idempotent would survive the faithfully flat field extension $K\subset\operatorname{Frac}(R^h)$. This contradicts the fact that the base change is a field. Thus $E_n$ is one field. Its degree is $\nu$ by Lemma [\[lem:idempotent\]](#lem:idempotent){reference-type="ref" reference="lem:idempotent"}.

This proves Theorem [\[thm:A\]](#thm:A){reference-type="ref" reference="thm:A"}(2). A more local account of the lifted factor and its valuation is given in Appendix [9](#app:local){reference-type="ref" reference="app:local"}.

# Relative normalization and the exact scalar fiber {#sec:normalization}

This section is the center of the construction. We obtain a finite flat normal model and then prove, rather than assume, that its fiber at $a=0$ is the scalar dynatomic algebra.

## Finite normalization

The polynomial ring $A$ is a finite-type algebra over $\mathbb{Q}$, hence excellent [@stacks-07qw]. Excellence implies the Nagata property [@stacks-07qv], and normalization in a finite extension of the fraction field is finite for a Nagata scheme [@stacks-035s]. Therefore the integral closure $$S=\overline{A}^{\,E_n}$$ is finite over $A$.

The ring $S$ is a normal domain of dimension two. Its local rings have dimension at most two and satisfy Serre's condition $S_2$; hence they are Cohen--Macaulay [@stacks-033p]. This surface property supplies the depth needed both for flatness and for excluding nilpotents in the scalar fiber.

## Miracle flatness

[\[prop:S-flat\]]{#prop:S-flat label="prop:S-flat"} The $A$-algebra $S$ is finite locally free of rank $\nu$.

Let $\mathfrak q\in\operatorname{Spec}S$ and set $\mathfrak p=\mathfrak q\cap A$. Since $S$ is finite integral over $A$, lying over and incomparability give $$\dim S_{\mathfrak q}=\dim A_{\mathfrak p},$$ and the local fiber has dimension zero. The ring $A_{\mathfrak p}$ is regular, while $S_{\mathfrak q}$ is Cohen--Macaulay. Miracle flatness [@stacks-00r4] shows that $S_{\mathfrak q}$ is flat over $A_{\mathfrak p}$. Hence $S$ is finite flat, and therefore finite locally free, over $A$. Its rank is constant because $\operatorname{Spec}A$ is connected, and the generic rank is $[E_n:K]=\nu$.

Proposition [\[prop:S-flat\]](#prop:S-flat){reference-type="ref" reference="prop:S-flat"} asserts no smoothness, reducedness, or étaleness for every parameter fiber. Such properties hold only after restricting to suitable open loci.

## The scalar divisor and exclusion of nilpotents

Let $T$ be the localization of $S$ over the DVR $R=A_{(a)}$. The Henselian algebra $C$ used in Lemma [\[lem:henselian-field\]](#lem:henselian-field){reference-type="ref" reference="lem:henselian-field"} is the integral model of the exact factor after Henselian base change. Its residue is the degree-$\nu$ field in [\[eq:scalar-exact-field\]](#eq:scalar-exact-field){reference-type="eqref" reference="eq:scalar-exact-field"}, and $C/R^h$ is étale. The valuation ledger therefore has one prime, ramification index $e=1$, and residue degree $f=\nu$; the equality $[E_n:K]=\sum e_if_i$ leaves no other prime or multiplicity [@stacks-09e4; @stacks-09e8].

Faithfully flat descent from $R^h$ to $R$ gives the following precise statement; Appendix [9](#app:local){reference-type="ref" reference="app:local"} supplies the semilocal argument.

[\[prop:a-divisor\]]{#prop:a-divisor label="prop:a-divisor"} There is a unique height-one prime $P\subset S$ above $(a)$, and $$\label{eq:div-a}
 \operatorname{div}_S(a)=P.$$ Its residue field is $\operatorname{Frac}(D_n)$ and its residue degree over $\mathbb{Q}(c)$ is $\nu$. Moreover, $S/aS$ is a reduced domain and $aS=P$.

The primes of $T$ above $a$ split after the faithfully flat Henselian base change into the primes of its normalization in $E_n\otimes_K\operatorname{Frac}(R^h)$. The latter is $C$ and has exactly one prime above $a$. Thus $T$, and hence $S$, has a unique height-one prime $P$ over $(a)$. The Henselian extension is unramified at that prime, so its ramification index is one. Residue degree is preserved and equals $\nu$; equivalently, the degree identity $ef=\nu$ is already exhausted by this prime. The coefficient of $P$ in the principal divisor of $a$ is therefore one, proving [\[eq:div-a\]](#eq:div-a){reference-type="eqref" reference="eq:div-a"}.

Because $S$ is a domain and $a\ne0$, multiplication by $a$ is injective. The quotient $S/aS$ is one-dimensional Cohen--Macaulay, so it satisfies $S_1$. Equation [\[eq:div-a\]](#eq:div-a){reference-type="eqref" reference="eq:div-a"} says that the localization of this quotient at its unique minimal prime is a field, hence reduced; this is the $R_0$ condition. The $R_0+S_1$ reducedness criterion [@stacks-033p] now shows that $S/aS$ is reduced everywhere, including at closed points. It has only one minimal prime, so it is a domain. The radical of $aS$ is $P$, and reducedness of the quotient gives $aS=P$.

The last paragraph is essential. Ramification index one controls generic multiplicity along the divisor, while the $S_1$ condition rules out embedded or closed-point nilpotents. As a check, $S/aS$ is flat of rank $\nu$ over $\mathbb{Q}[c]$. A nilradical whose reduced quotient already has that rank would be $\mathbb{Q}[c]$-torsion, impossible inside a torsion-free module. This rank check agrees with Proposition [\[prop:a-divisor\]](#prop:a-divisor){reference-type="ref" reference="prop:a-divisor"}; it does not replace the divisor argument.

## Finite birational comparison with the scalar algebra

The projections of the orbit coordinates to $E_n$ are integral over $A$, and hence lie in $S$. Modulo $a$, the cyclic recurrence becomes $$z_{i+1}=f_c(z_i).$$ Lemma [\[lem:henselian-valuation-descent\]](#lem:henselian-valuation-descent){reference-type="ref" reference="lem:henselian-valuation-descent"} gives $\Phi_{d,n}(z_0,c)=0$ after tensoring $S/aS$ with $k=\mathbb{Q}(c)$ over $\mathbb{Q}[c]$. Proposition [\[prop:S-flat\]](#prop:S-flat){reference-type="ref" reference="prop:S-flat"} makes $S/aS$ flat, hence torsion-free, over $\mathbb{Q}[c]$. The localization map $$S/aS\longrightarrow (S/aS)\otimes_{\mathbb{Q}[c]}k$$ is therefore injective, so the relation already vanishes in $S/aS$. Consequently there is a homomorphism $$\label{eq:D-to-fiber}
 D_n=\mathbb{Q}[c,z]/(\Phi_{d,n})\longrightarrow S/aS,
 \qquad z\longmapsto z_0.$$ It is finite because the target is finite over $\mathbb{Q}[c]$. Both source and target are domains, and Proposition [\[prop:a-divisor\]](#prop:a-divisor){reference-type="ref" reference="prop:a-divisor"} identifies their fraction fields with the same scalar exact-period function field.

Gao and Ou prove that the affine scalar dynatomic curve is smooth and geometrically integral in characteristic zero [@gao-ou-2014-dynatomic]; in particular, $D_n$ is normal. The target of [\[eq:D-to-fiber\]](#eq:D-to-fiber){reference-type="eqref" reference="eq:D-to-fiber"} is a finite birational overring of $D_n$ inside the same fraction field. An integrally closed domain has no proper integral overring in its fraction field [@stacks-0309]. Therefore $$\label{eq:exact-fiber}
 \boxed{S/aS\simeq D_n.}$$

The chain leading to [\[eq:exact-fiber\]](#eq:exact-fiber){reference-type="eqref" reference="eq:exact-fiber"} is worth keeping visible: $$\begin{gathered}
  \text{unique prime above }(a)\Longrightarrow e=1
    \Longrightarrow \operatorname{div}_S(a)=P\\
  \Longrightarrow R_0+S_1
    \Longrightarrow S/aS\text{ reduced}\\
  \Longrightarrow \text{finite birational equality}.
 \end{gathered}$$ Thus [\[eq:exact-fiber\]](#eq:exact-fiber){reference-type="eqref" reference="eq:exact-fiber"} is not an invocation of automatic compatibility between normalization and base change.

## Constants and geometric integrality

[\[prop:geometric-integrality\]]{#prop:geometric-integrality label="prop:geometric-integrality"} The field $\mathbb{Q}$ is algebraically closed in $E_n$, and $\operatorname{Spec}S$ is geometrically integral over $\mathbb{Q}$.

Let $k'$ be the relative algebraic closure of $\mathbb{Q}$ in $E_n$. Because $E_n$ is finitely generated over $\mathbb{Q}$, the extension $k'/\mathbb{Q}$ is finite. Every element of $k'$ is integral over $A$, hence lies in $S$. A nonzero element of $k'$ and its inverse both lie in $S$, so every nonzero constant is a unit. Reduction modulo $a$ therefore injects $k'$ into $\operatorname{Frac}(S/aS)$: a nonzero constant cannot lie in the proper ideal $aS$. Using [\[eq:exact-fiber\]](#eq:exact-fiber){reference-type="eqref" reference="eq:exact-fiber"}, we obtain $$k'\hookrightarrow\operatorname{Frac}(D_n).$$ Geometric integrality of $D_n$ implies that $\mathbb{Q}$ is algebraically closed in its function field. Thus $k'=\mathbb{Q}$.

In characteristic zero the finitely generated extension $E_n/\mathbb{Q}$ is geometrically reduced [@stacks-0322]; together with the constant-field conclusion, it is geometrically irreducible [@stacks-037p]. Hence $E_n\otimes_\mathbb{Q}\overline{\mathbb{Q}}$ is a domain. Flatness of $\overline{\mathbb{Q}}/\mathbb{Q}$ preserves the injection $S\hookrightarrow E_n$, so $$S\otimes_\mathbb{Q}\overline{\mathbb{Q}}\hookrightarrow E_n\otimes_\mathbb{Q}\overline{\mathbb{Q}}$$ is a domain. Geometric integrality can be checked after algebraic closure [@stacks-0fwf], which proves the assertion.

Propositions [\[prop:S-flat\]](#prop:S-flat){reference-type="ref" reference="prop:S-flat"}, [\[prop:a-divisor\]](#prop:a-divisor){reference-type="ref" reference="prop:a-divisor"}, and [\[prop:geometric-integrality\]](#prop:geometric-integrality){reference-type="ref" reference="prop:geometric-integrality"}, together with [\[eq:exact-fiber\]](#eq:exact-fiber){reference-type="eqref" reference="eq:exact-fiber"}, prove Theorem [\[thm:A\]](#thm:A){reference-type="ref" reference="thm:A"}(3)--(4).

# The cyclic quotient and geometric monodromy {#sec:quotient}

## Reynolds invariants and arbitrary base change

The shift $\sigma$ preserves the generic actual-period idempotent and hence acts on the field $E_n$. Every $K$-automorphism of $E_n$ carrying $A$ to itself preserves the integral closure of $A$, so $\sigma$ extends uniquely to $S$. On a geometric actual-period orbit, the shift has order exactly $n$; therefore its action on $E_n$ is faithful. Artin's fixed-field theorem gives $$\label{eq:fixed-field-degree}
 [E_n:E_n^{C_n}]=n,\qquad [F:K]=\frac{\nu}{n}=r.$$

Since $A$ is a $\mathbb{Q}$-algebra, $n$ is invertible in $A$. Define the Reynolds operator $$\label{eq:reynolds}
 \mathcal{R}=\frac{1}{n}\sum_{j=0}^{n-1}\sigma^j:S\longrightarrow S.$$ It is an idempotent whose image is exactly $S^{C_n}=S_0$. Thus $S=S_0\oplus\ker(\mathcal{R})$ as an $A$-module. In particular, $S_0$ is a finite projective, hence finite locally free, $A$-module. Its generic rank is $r$ by [\[eq:fixed-field-degree\]](#eq:fixed-field-degree){reference-type="eqref" reference="eq:fixed-field-degree"}.

The split description also proves the required base-change statement, rather than merely suggesting it.

[\[prop:invariants-base-change\]]{#prop:invariants-base-change label="prop:invariants-base-change"} For every $A$-algebra $A'$, the natural homomorphism $$S_0\otimes_AA'\longrightarrow(S\otimes_AA')^{C_n}$$ is an isomorphism. In particular, $$\label{eq:quotient-fiber}
 S_0/aS_0\simeq D_n^{C_n}.$$

After tensoring with $A'$, the map $\mathcal{R}\otimes1$ is still an idempotent, and the direct-sum decomposition becomes $$S\otimes_AA'=(S_0\otimes_AA')\oplus(\ker\mathcal{R}\otimes_AA').$$ For any element $x$ of $S\otimes_AA'$, the identity $\sigma x=x$ implies $(\mathcal{R}\otimes1)x=x$. Conversely, the image of the averaging operator is fixed by the group. Hence the invariant submodule is precisely the invariant summand. Taking $A'=A/(a)$ and using $S/aS\simeq D_n$ from [\[eq:exact-fiber\]](#eq:exact-fiber){reference-type="eqref" reference="eq:exact-fiber"} proves [\[eq:quotient-fiber\]](#eq:quotient-fiber){reference-type="eqref" reference="eq:quotient-fiber"}.

The quotient in [\[eq:quotient-fiber\]](#eq:quotient-fiber){reference-type="eqref" reference="eq:quotient-fiber"} is affine. The proposition does not assert that the cyclic action is free on every fiber, nor that every fiber of the quotient is smooth, reduced, or étale.

## From the scalar line to global cycle monodromy

Finite separability of $E_n/K$ and $F/K$, together with finite local freeness of $S$ and $S_0$, gives a dense open $U\subset\operatorname{Spec}A$ on which $$W=\operatorname{Spec}S\times_AU\longrightarrow U,
 \qquad
 V=\operatorname{Spec}S_0\times_AU\longrightarrow U$$ are finite étale of degrees $\nu$ and $r$. We may shrink $U$ so that its intersection $U_0$ with the scalar line contains a common good locus for the scalar marked-point and cycle covers. Proposition [\[prop:geometric-integrality\]](#prop:geometric-integrality){reference-type="ref" reference="prop:geometric-integrality"} implies geometric connectedness of the generic marked-point cover. The same holds for the cycle cover because the relative algebraic closure of $\mathbb{Q}$ in the subfield $F\subset E_n$ is again $\mathbb{Q}$.

For the scalar map $z^d+c$, Morton's all-degree theorem identifies the geometric permutation group on exact-period marked points with $C_n\mathbin{\wr}S_r$ [@morton-1998-periodic-galois]. Fakhruddin states the same product of wreath groups over every characteristic-zero constant field, so taking constants $\overline{\mathbb{Q}}$ makes this a geometric, rather than merely arithmetic, input [@fakhruddin-2014-generic-endomorphisms]. Passing to cycles gives $S_r$.

Choose compatible geometric base points. The inclusion of the scalar good locus induces $$\label{eq:pi1-direction}
 \pi_1\bigl((U_0)_{\overline{\mathbb{Q}}}\bigr)
 \longrightarrow
 \pi_1\bigl(U_{\overline{\mathbb{Q}}}\bigr)
 \longrightarrow S_r.$$ The image of the left-hand group is therefore a subgroup of the global image. It is already $S_r$ by the scalar theorem, while any global permutation of the $r$ sheets belongs to $S_r$. The two inclusions force $$\label{eq:cycle-monodromy}
 \operatorname{Mon}_{\mathrm{geom}}(V/U)=S_r.$$

At marked-point level there is also a useful upper bound. Geometric monodromy commutes with the globally defined time shift. The centralizer of a permutation consisting of $r$ disjoint $n$-cycles is $C_n\mathbin{\wr}S_r$. The global marked-point group is therefore contained in this wreath product, whereas its restriction to the scalar line contains the entire product. Hence marked-point equality follows as an auxiliary fact. Only the cycle statement [\[eq:cycle-monodromy\]](#eq:cycle-monodromy){reference-type="eqref" reference="eq:cycle-monodromy"} is needed below. When $r=1$, it reads $S_1$ and is tautologically trivial.

Proposition [\[prop:invariants-base-change\]](#prop:invariants-base-change){reference-type="ref" reference="prop:invariants-base-change"} and [\[eq:cycle-monodromy\]](#eq:cycle-monodromy){reference-type="eqref" reference="eq:cycle-monodromy"} prove Theorem [\[thm:A\]](#thm:A){reference-type="ref" reference="thm:A"}(5)--(6). Notice that the lower-bound direction in [\[eq:pi1-direction\]](#eq:pi1-direction){reference-type="eqref" reference="eq:pi1-direction"} is scalar to global; reversing it would not prove the theorem.

# Two primitive cycle coordinates {#sec:coordinates}

Theorem [\[thm:A\]](#thm:A){reference-type="ref" reference="thm:A"} supplies a degree-$r$ cycle field with full symmetric geometric monodromy. We now treat two integral functions on that cover. The arguments establishing that they are non-base functions remain separate until the common group-theoretic step.

## Cyclic invariance and the trace category

The orbit sum $\tau$ is fixed by cyclic permutation of its summands. A change of marked point cyclically rotates the product $M_{n-1}\cdots M_0$. Matrix trace satisfies $\operatorname{tr}(AB)=\operatorname{tr}(BA)$, and repeated cyclic rotation therefore fixes $\rho$. The coordinates $z_i$ are integral over $A$, so both observables are elements of $S^{C_n}=S_0$.

The order in [\[eq:tau-rho\]](#eq:tau-rho){reference-type="eqref" reference="eq:tau-rho"} is the derivative chain-rule order. For two steps, $$M_1M_0=
 \begin{pmatrix}
   u_1u_0+a&u_1a\\
   u_0&a
 \end{pmatrix},$$ which recovers [\[eq:n2-matrix-check\]](#eq:n2-matrix-check){reference-type="eqref" reference="eq:n2-matrix-check"}. In all periods $\det(M_{n-1}\cdots M_0)=(-a)^n$; this determinant is not the observable $\rho$.

## Formal branches at scalar infinity

We use the scalar line only to prove that the two global functions do not descend to the parameter field. Introduce a local parameter $q$ at $c=\infty$ by $$\label{eq:infinity-substitution}
 c=-q^{-d},\qquad z_i=q^{-1}v_i,\qquad
 \epsilon=q^{d-1}.$$ The scalar recurrence becomes $$\label{eq:v-recurrence}
 v_i^d=1+\epsilon v_{i+1}.$$ Let $\mu_d$ denote the $d$th roots of unity in $\overline{\mathbb{Q}}$. For every word $\boldsymbol{\omega}=(\omega_0,\ldots,\omega_{n-1})\in\mu_d^n$, the formal implicit function theorem gives a unique solution of [\[eq:v-recurrence\]](#eq:v-recurrence){reference-type="eqref" reference="eq:v-recurrence"} with $v_i\equiv\omega_i\pmod\epsilon$. Equivalently, $$\label{eq:branch-equation}
 v_i=\omega_i(1+\epsilon v_{i+1})^{1/d},$$ where the binomial root has constant term one. A word of least rotational period $n$ indexes an exact-period branch, and rotating the word changes only the marked point on its cycle.

Substitution into $\tau$ immediately gives $$\label{eq:tau-leading}
 \tau=q^{-1}\left(\sum_{i=0}^{n-1}\omega_i+O(\epsilon)\right).$$ The leading term for $\rho$ is derived independently. At $a=0$, $$M_i=\begin{pmatrix}d z_i^{d-1}&0\\1&0\end{pmatrix}.$$ Multiplying these matrices in the prescribed order shows that the trace is the product of their upper-left entries: $$\rho=d^n\prod_{i=0}^{n-1}z_i^{d-1}.$$ Using [\[eq:infinity-substitution\]](#eq:infinity-substitution){reference-type="eqref" reference="eq:infinity-substitution"}, and $\omega_i^{d-1}=\omega_i^{-1}$, gives $$\label{eq:rho-leading}
 \rho=d^nq^{-n(d-1)}
 \left(\prod_{i=0}^{n-1}\omega_i^{-1}+O(\epsilon)\right).$$ Thus the leading invariant for $\tau$ is a sum, whereas that for $\rho$ is an inverse product.

## Two separate non-base propositions

The passage from scalar branches to the global parameter field uses the intersection $$\label{eq:intersection-A}
 S_0\cap K=A.$$ Indeed, every element of $S_0$ is integral over $A$, and $A$ is integrally closed in $K$. If an element of $S_0$ belonged to $K$, it would therefore specialize at $a=0$ to an element of $\mathbb{Q}[c]$ and take the same value on every branch above a fixed base expansion.

[\[prop:tau-nonbase\]]{#prop:tau-nonbase label="prop:tau-nonbase"} If $r>1$, then $\tau\notin K$.

Suppose that $d\geq3$, and choose a primitive $d$th root of unity $\zeta$. The words $$(1,\ldots,1,\zeta)
 \quad\text{and}\quad
 (1,\ldots,1,\zeta^2)$$ have least rotational period $n$: each contains exactly one symbol different from $1$, and the two exceptional symbols are different. Their word sums are $n-1+\zeta$ and $n-1+\zeta^2$. These are unequal, so [\[eq:tau-leading\]](#eq:tau-leading){reference-type="eqref" reference="eq:tau-leading"} gives two exact-period scalar branches with different leading values of $\tau$.

Now let $d=2$ and $n\geq3$. Compare a binary word with exactly one $-1$ with a word having exactly two adjacent $-1$ entries. Each has least rotational period $n$: a nontrivial rotational repetition would repeat the number and pattern of negative entries in more than one block. Their sums are $n-2$ and $n-4$, again distinct. In either degree case, $\tau$ cannot specialize to one base function. Equation [\[eq:intersection-A\]](#eq:intersection-A){reference-type="eqref" reference="eq:intersection-A"} then implies $\tau\notin K$.

[\[prop:rho-nonbase\]]{#prop:rho-nonbase label="prop:rho-nonbase"} If $r>1$, then $\rho\notin K$.

For $d\geq3$, use the same two primitive words, but use no information about their sums. Their inverse products are $\zeta^{-1}$ and $\zeta^{-2}$, which differ. Formula [\[eq:rho-leading\]](#eq:rho-leading){reference-type="eqref" reference="eq:rho-leading"} distinguishes the two values of $\rho$.

For $d=2$ and $n\geq3$, the one-minus word has product $-1$, whereas the two-adjacent-minus word has product $1$. Their inverse products are therefore different, so [\[eq:rho-leading\]](#eq:rho-leading){reference-type="eqref" reference="eq:rho-leading"} again distinguishes the branches. The intersection [\[eq:intersection-A\]](#eq:intersection-A){reference-type="eqref" reference="eq:intersection-A"} now gives $\rho\notin K$ independently of Proposition [\[prop:tau-nonbase\]](#prop:tau-nonbase){reference-type="ref" reference="prop:tau-nonbase"}.

The restriction $r>1$ excludes exactly one pair. For $n=2$, $$r=\frac{d^2-d}{2},$$ which equals one only for $d=2$. For $n\geq3$, the explicit comparison words above yield at least two primitive rotation classes: for $d\geq3$ the two exceptional symbols cannot be rotations of one another, and for $d=2$ the two words have different numbers of minus signs. Thus $(2,2)$ is the only rank-one case.

Morton's scalar results provide a direct prior-art route in part of this argument. On the scalar point field, the orbit-shift fixed field is generated by the multiplier $\prod_i f_c'(f_c^i(z))=\rho|_{a=0}$ for every $d,n$, and in degree two it is also generated by the orbit sum $\tau|_{a=0}$ [@morton-1996-algebraic-curves]. Propositions [\[prop:tau-nonbase\]](#prop:tau-nonbase){reference-type="ref" reference="prop:tau-nonbase"} and [\[prop:rho-nonbase\]](#prop:rho-nonbase){reference-type="ref" reference="prop:rho-nonbase"} retain the word argument to treat the two functions uniformly and separately; they do not assign newness to those scalar generator statements.

## Full symmetric monodromy and separate generation

Let $L/K$ be a Galois closure of $F/K$. By [\[eq:cycle-monodromy\]](#eq:cycle-monodromy){reference-type="eqref" reference="eq:cycle-monodromy"}, the arithmetic permutation image on the $r$ conjugate cycles contains the geometric image $S_r$. It is also a subgroup of the ambient permutation group $S_r$, so the arithmetic image is $S_r$ as well. Choosing one cycle identifies $$F=L^{S_{r-1}}.$$ For $r\geq2$, the subgroup $S_{r-1}$ is maximal in $S_r$. An element $s\in F$ is fixed by $S_{r-1}$. If $s\notin K$, its stabilizer in $S_r$ is a proper subgroup containing $S_{r-1}$ and must consequently equal $S_{r-1}$. The orbit of $s$ then has size $r$.

Apply this argument to $s=\tau$ before considering $\rho$, using only Proposition [\[prop:tau-nonbase\]](#prop:tau-nonbase){reference-type="ref" reference="prop:tau-nonbase"}; it gives $[K(\tau):K]=r$ and hence $K(\tau)=F$. Apply it again to $s=\rho$, now using only Proposition [\[prop:rho-nonbase\]](#prop:rho-nonbase){reference-type="ref" reference="prop:rho-nonbase"}; it gives $K(\rho)=F$. Thus $$\label{eq:primitive-fields}
 \boxed{K(\tau)=F=K(\rho).}$$ Non-base behavior alone would not imply this equality for a general monodromy group. The full symmetric group and the maximal point stabilizer are the decisive ingredients.

## Determinant lines and irreducible multiplication polynomials

Let $s$ denote either $\tau$ or $\rho$. Multiplication defines an $A$-linear endomorphism $m_s:S_0\to S_0$. Since $S_0$ is finite locally free of rank $r$, the endomorphism $T\operatorname{id}-m_s$ acts on the invertible $A[T]$-module $\bigwedge_{A[T]}^r(S_0\otimes_AA[T])$. Its scalar action defines $$\label{eq:chi-s}
 \chi_s(T)=\det(T\operatorname{id}-m_s)\in A[T]$$ without choosing a global basis.

After tensoring with $K$, equation [\[eq:primitive-fields\]](#eq:primitive-fields){reference-type="eqref" reference="eq:primitive-fields"} makes $1,s,\ldots,s^{r-1}$ a basis of $F$. Equivalently, $$\label{eq:power-wedge}
 1\wedge s\wedge\cdots\wedge s^{r-1}\ne 0
 \quad\text{in }\bigwedge_K^rF.$$ The minimal polynomial of $s$ over $K$ consequently has degree $r$ and equals the characteristic polynomial in [\[eq:chi-s\]](#eq:chi-s){reference-type="eqref" reference="eq:chi-s"}. Hence $\chi_s$ is irreducible of degree $r$ in $K[T]$. It is monic with coefficients in the UFD $A$, so Gauss's lemma also makes it irreducible in $A[T]$.

Under the $r$ embeddings of $F$ into $L$, the wedge [\[eq:power-wedge\]](#eq:power-wedge){reference-type="eqref" reference="eq:power-wedge"} becomes the Vandermonde product $$\label{eq:vandermonde}
 \prod_{1\leq i<j\leq r}(s_i-s_j).$$ Its square is the discriminant of $\chi_s$ and is nonzero. This proves generic separability. It does not say that every specialization of $\chi_s$ is irreducible or separable.

## The complete rank-one boundary

For $d=n=2$, the two cyclic equations are $$\label{eq:22-equations}
 z_0^2+(a-1)z_1+c=0,
 \qquad
 z_1^2+(a-1)z_0+c=0.$$ Subtracting them gives $$\label{eq:22-factor}
 (z_0-z_1)\bigl(z_0+z_1-(a-1)\bigr)=0.$$ On the generic actual two-cycle block, $z_0\ne z_1$, so $\tau=z_0+z_1=a-1$. Substituting this sum into the sum of [\[eq:22-equations\]](#eq:22-equations){reference-type="eqref" reference="eq:22-equations"} yields $$z_0z_1=(a-1)^2+c.$$ Since $u_i=2z_i$, equation [\[eq:n2-matrix-check\]](#eq:n2-matrix-check){reference-type="eqref" reference="eq:n2-matrix-check"} gives $$\rho=4z_0z_1+2a=4a^2-6a+4+4c.$$ Finally, [\[eq:nu-r\]](#eq:nu-r){reference-type="eqref" reference="eq:nu-r"} gives $\nu=2$ and $r=1$. The two multiplication polynomials are therefore $$\chi_\tau(T)=T-(a-1),\qquad
 \chi_\rho(T)=T-(4a^2-6a+4+4c).$$ This proves Proposition [\[prop:C\]](#prop:C){reference-type="ref" reference="prop:C"} and completes Theorem [\[thm:B\]](#thm:B){reference-type="ref" reference="thm:B"}. The trivial group $S_1$ and these linear equations carry no nontrivial monodromy or non-base content.

# Prior work and precise positioning {#sec:prior}

## Scalar dynatomic geometry and monodromy

The scalar boundary rests on a mature dynatomic theory. Gao and Ou prove that the affine periodic dynatomic curves for $z^d+c$ are smooth and irreducible [@gao-ou-2014-dynatomic]. Their theorem supplies the normal geometrically integral algebra $D_n$ used in the Henselian, finite-birational, and constants steps; it does not supply the relative Hénon normalization. Hutz's formal dynatomic cycles make clear why formal period can specialize to smaller actual period [@hutz-2010-dynatomic-cycles]. Doyle and Poonen provide scalar dynatomic quotient and gonality context [@doyle-poonen-2020-gonality], but the quotient in this paper remains the affine invariant algebra rather than a projective modular curve.

The scalar full-centralizer theorem is also imported. Morton identifies the all-degree Galois group of $f_c^b(z)-z$ as the product of wreath groups over the period divisors, so the exact-period-$n$ factor is $C_n\mathbin{\wr}S_r$ [@morton-1998-periodic-galois]. Fakhruddin's formulation over an arbitrary characteristic-zero field supplies the geometric version [@fakhruddin-2014-generic-endomorphisms], and Gao's later table provides an all-degree corroboration [@gao-2016-preperiodic-dynatomic]. Schleicher records the quadratic analytic-continuation and Galois history [@schleicher-2017-internal-addresses]. What is proved here is the relative normalization, exact scalar degeneration, affine quotient, and special-to-global transfer as one two-parameter package; no scalar theorem is relabeled as a contribution.

## Scalar generators and trace-spectrum adjacency

Morton's earlier work is direct prior art for both scalar observables. For every $d,n$ in scope, the scalar orbit-shift fixed field is generated by the multiplier $\prod_i f_c'(f_c^i(z))$, which is precisely $\rho|_{a=0}$. In degree two, his irreducible orbit-sum polynomial likewise gives the generator $\tau|_{a=0}$ [@morton-1996-algebraic-curves]. The later corrigendum repairs a finite-characteristic lifting issue in a subsequent theorem and does not retract these characteristic-zero fixed-field statements [@morton-2011-corrigendum]. The coordinate result here is limited to the two-parameter lift, the uniform $d\geq3$ orbit-sum argument, and the integral basis-free characteristic-polynomial package.

Cantat and Dujardin study a neighboring but differently directed trace problem [@cantat-dujardin-2026-multiplier-rigidity]. Their data are whole multisets of pointwise traces on formal-period schemes, taken over finitely many periods, and their conclusion reconstructs parameters within a fixed-degree Hénon parameter space up to uniformly finite ambiguity. Theorem [\[thm:B\]](#thm:B){reference-type="ref" reference="thm:B"} instead fixes one actual period and asks whether one cycle value generates the degree-$r$ cycle function field over the parameter base. Neither statement implies the other.

## Low-period carriers and the Hénon setting

Orbit-sum carriers and cyclic-polynomial calculations already occur in low-period Hénon dynamics. For the quadratic Hénon map, Endler and Gallas use the period-four orbit sum as a carrier satisfying a cubic equation [@endler-gallas-2002-arithmetical-signatures]; their period-six work uses the corresponding sum together with stability equations [@endler-gallas-2004-ghost-orbits]. Zhang develops cyclic-polynomial elimination for polynomial maps and reports bounded-period Hénon calculations [@zhang-2014-cycles-logistic-map]. These sources preclude any claim to have introduced orbit-sum carriers, stability carriers, or cyclic-polynomial elimination.

Friedland and Milnor place the family inside the general theory of plane polynomial automorphisms and generalized Hénon maps [@friedland-milnor-1989-plane-automorphisms]. Our assertions concern only the normalized family $H_{a,c}$ above. Broader Hénon families can have different degenerations and require separate normalization arguments. The contribution claimed here is the exact conjunction proved in Theorems [\[thm:A\]](#thm:A){reference-type="ref" reference="thm:A"} and [\[thm:B\]](#thm:B){reference-type="ref" reference="thm:B"}; no historical-priority inference is drawn from the surrounding comparison.

# Limitations and conclusion {#sec:conclusion}

The dominant conclusion is the normalized primitive-point cover and its cycle quotient: the generic actual-period field extends to a finite locally free geometrically integral model whose scalar fiber is exactly the affine dynatomic algebra, and the cycle cover has full symmetric geometric monodromy. The two primitive coordinates form a narrower final layer that uses this monodromy and keeps the orbit-sum and derivative-trace arguments separate.

The construction is restricted to the fixed normalized family and to a generic actual-period idempotent. Its quotient is affine, its monodromy is asserted on a dense finite-étale open, and it gives no every-fiber smoothness, reducedness, étaleness, or free-torsor statement. The generic irreducibility and nonzero discriminants of the multiplication polynomials are not specialized-fiber assertions. Compactifications and more general Hénon families would require new boundary and normalization arguments.

Separately from the proof, a preregistered, seedless exact audit compared two independently implemented bounded routes in a single sealed run. An independent integrity review returned `RESULT_PASS` only for bounded implementation consistency. This computation is neither a proof nor a validation of the theorems, which rest on the mathematical argument and its independent source review. All available reviews used one model family, so correlated-error risk remains and no cross-model validation is claimed.

# Local algebra of the normalization and the scalar divisor {#app:local}

This appendix expands the local steps used in Sections [3](#sec:fixed){reference-type="ref" reference="sec:fixed"}--[4](#sec:normalization){reference-type="ref" reference="sec:normalization"}. Its purpose is to keep three logically distinct operations visible: lifting the scalar exact idempotent, normalizing its generic field over the two-dimensional base, and identifying the resulting special fiber. None of the arguments begins by assuming that normalization commutes with reduction modulo $a$.

## Finite-étale lifting over the $a$-adic pair

Recall $$R=A_{(a)},\qquad \mathfrak m_R=(a),\qquad
 k=R/(a)=\mathbb{Q}(c),$$ and let $R^h$ be the henselization. The monic basis from Lemma [\[lem:groebner\]](#lem:groebner){reference-type="ref" reference="lem:groebner"} identifies $B_n\otimes_AR$ with a free $R$-module of rank $d^n$. Reduction modulo $a$ identifies its algebra with $$k[z]/(f_c^n(z)-z).$$ The latter is finite étale over $k$: over the generic scalar parameter, the polynomial and its derivative have no common root. For a finite presentation, relative differentials commute with base change. Thus $$\Omega_{(B_n\otimes_AR)/R}\otimes_Rk=0.$$ The module of differentials is finite, so Nakayama's lemma gives $\Omega_{(B_n\otimes_AR)/R}=0$. Finite flatness was already proved by the monic basis, and hence $B_n\otimes_AR$ is finite étale.

The scalar algebra decomposes as the product of its dynatomic factors. Let $\bar e_n$ be the idempotent for the factor $k[z]/(\Phi_{d,n})$. The equivalence between finite étale algebras over the Henselian pair $(R^h,(a))$ and over $k$ lifts $\bar e_n$ uniquely [@stacks-0d49]. Denote the image factor by $C$. Then $$\label{eq:appendix-C-residue}
 C/aC\simeq k[z]/(\Phi_{d,n}),\qquad
 \operatorname{rank}_{R^h}C=\nu.$$ The right-hand algebra in [\[eq:appendix-C-residue\]](#eq:appendix-C-residue){reference-type="eqref" reference="eq:appendix-C-residue"} is a field. If $C$ had a nontrivial idempotent, its reduction would be a nontrivial idempotent of that field, contradicting Henselian idempotent lifting. Thus $C$ is connected. Since it is finite étale over the normal domain $R^h$, it is normal. A connected normal ring is a domain, and therefore $C[1/a]$ is a field.

[\[lem:appendix-idempotent-identification\]]{#lem:appendix-idempotent-identification label="lem:appendix-idempotent-identification"} The generic idempotent of $C[1/a]$ is the base change of $e_n$ from [\[eq:En\]](#eq:En){reference-type="eqref" reference="eq:En"}.

The generic finite-étale algebra is partitioned by the least periods $e\mid n$. For every proper divisor $e$, the corresponding factor is contained in the closed fixed locus cut out by $H^e(P)=P$. This equation survives specialization. Its closure cannot contain a scalar point of least period $n$, so the reduction of any lifted lower-period factor is disjoint from $\bar e_n$.

Set $B^h=B_n\otimes_AR^h$ and let $e_C\in B^h$ cut out $C$. The finite étale algebra $B^h$ is normal over the normal local ring $R^h$. Each of its connected factors is therefore a domain and remains connected after inverting $a$. Consequently localization induces a bijection from the idempotents of $B^h$ to those of $B^h[1/a]$: every generic period idempotent extends uniquely over $R^h$. Let $e_n^h$ be the extension of the base change of $e_n$. The disjointness from every proper-period factor and the identity that the period-factor idempotents sum to one give $$e_C[1/a]e_n^h=e_C[1/a].$$ Thus $C[1/a]$ is a direct subfactor of $E_n\otimes_K\operatorname{Frac}(R^h)$. Finally, $$\dim_{\operatorname{Frac}(R^h)}C[1/a]=\operatorname{rank}_{R^h}C=\nu,
 \qquad
 \dim_{\operatorname{Frac}(R^h)}(E_n\otimes_K\operatorname{Frac}(R^h))=\dim_KE_n=\nu.$$ A direct subfactor of the same finite dimension is the whole factor. Hence $e_C[1/a]=e_n^h$, which identifies $C[1/a]$ with the base change of the generic actual-period block and excludes every formal-period contribution of lower least period.

Lemma [\[lem:appendix-idempotent-identification\]](#lem:appendix-idempotent-identification){reference-type="ref" reference="lem:appendix-idempotent-identification"} gives $$E_n\otimes_K\operatorname{Frac}(R^h)\simeq C[1/a].$$ Any product decomposition of $E_n$ would produce a nontrivial idempotent after this field extension. The right side is a field, so no such decomposition exists. This is the promised connected-lift proof of the one-field assertion; irreducibility is not inferred only from the number of geometric points.

## Finiteness, local dimensions, and flatness

For completeness, we spell out the commutative-algebra chain used to pass from the field $E_n$ to the relative model. A finite-type algebra over a field is excellent [@stacks-07qw]; a quasi-excellent ring is Nagata [@stacks-07qv]; and normalization in a finite extension of the generic field is finite for a Nagata scheme [@stacks-035s]. These implications give $S$ as a finite $A$-algebra.

Normality implies $R_1$ and $S_2$. Since $S$ is finite over the two-dimensional domain $A$, every local ring $S_{\mathfrak q}$ has dimension at most two. The $S_2$ depth inequality is therefore exactly the Cohen--Macaulay equality at positive-dimensional local rings [@stacks-033p]. If $\mathfrak p=\mathfrak q\cap A$, integrality gives $$\dim S_{\mathfrak q}=\dim A_{\mathfrak p}.$$ One way to see the equality is to contract a maximal chain of primes in $S_{\mathfrak q}$ and use incomparability for the upper bound, then lift a chain in $A_{\mathfrak p}$ by going up for the lower bound. The local fiber is zero-dimensional because the map is finite.

The regular local ring $A_{\mathfrak p}$ and the Cohen--Macaulay local ring $S_{\mathfrak q}$ now satisfy the hypotheses of miracle flatness [@stacks-00r4]. Flatness at every $\mathfrak q$ makes $S$ finite flat over $A$. A finite flat module is locally free, and its generic rank is $\nu$. This argument uses the normal surface structure; it would not justify flatness for a higher-dimensional normal total space without an additional depth argument.

## Descent of the unique valuation

The following formulation isolates both what Henselization proves and what still has to be descended to the surface.

[\[lem:henselian-valuation-descent\]]{#lem:henselian-valuation-descent label="lem:henselian-valuation-descent"} Let $T=S\otimes_AR$, let $K^h=\operatorname{Frac}(R^h)$, and let $\widetilde T^h$ be the normalization of $R^h$ in $E_n\otimes_KK^h$. Then $$\widetilde T^h=C.$$ There is a unique prime $\mathfrak P$ of $T$ above $(a)$, and the associated extension of discrete valuations has ramification index $e=1$ and residue degree $f=\nu$. Its contraction $P$ to $S$ is the unique height-one prime above $(a)$, and $$\operatorname{div}_S(a)=P.$$ The last equality is an equality of Weil divisors; the ideal equality $aS=P$ requires the subsequent $R_0+S_1$ argument.

The ring $T$ is the integral closure of the DVR $R$ in the finite field extension $E_n/K$. It is a finite semilocal normal one-dimensional domain. Consequently, if $\mathfrak P_1,\ldots,\mathfrak P_t$ are its primes above $(a)$, then every $T_{\mathfrak P_i}$ is a DVR. Put $e_i=v_{\mathfrak P_i}(a)$ and let $f_i$ be the degree of its residue field over $k=\mathbb{Q}(c)$.

Lemma [\[lem:appendix-idempotent-identification\]](#lem:appendix-idempotent-identification){reference-type="ref" reference="lem:appendix-idempotent-identification"} identifies the extended generic algebra with $C[1/a]$: $$E_n\otimes_KK^h\simeq C[1/a].$$ The right side is a field. Moreover, $C$ is finite and étale over the normal ring $R^h$, hence is itself normal. It is therefore the integral closure of $R^h$ in that field, proving $\widetilde T^h=C$.

Normalization after passage from a DVR to its Henselization separates the extensions of the original valuation: its local factors are indexed by the primes $\mathfrak P_i$ above $(a)$. Distinct such primes give distinct open-and-closed factors. Here the normalization is $C$, and $C/aC$ is the single scalar exact-period field in [\[eq:appendix-C-residue\]](#eq:appendix-C-residue){reference-type="eqref" reference="eq:appendix-C-residue"}. Thus $C$ is connected and has one maximal ideal, so $t=1$. This is also the point at which faithful flatness matters: because $R\to R^h$ is faithfully flat, two distinct factors over $R$ cannot become one factor after base change, and a nonzero local factor cannot disappear.

The unique Henselian local extension is étale, so its uniformizer is still $a$ and its ramification index is one. Henselization has the same residue field $k$, while $$C/aC\simeq k[z]/(\Phi_{d,n}(z,c))$$ has $k$-dimension $\nu$; hence $f=\nu$. Equivalently, the fundamental degree identity $$[E_n:K]=\sum_{i=1}^{t}e_if_i$$ reads $\nu=1\cdot\nu$ and leaves no missing valuation or residual degree [@stacks-09e4; @stacks-09e8]. Ramification indices and residue degrees are unchanged by this faithfully flat, unramified Henselian base change, so the same values hold in $T_{\mathfrak P}$.

Since $T$ is obtained by localizing $S$ at the generic point of $(a)$, the prime $\mathfrak P$ contracts to one height-one prime $P$ of $S$ above $(a)$, and every such height-one prime appears this way. The coefficient of $P$ in the principal divisor of $a$ is $v_{S_P}(a)=e=1$. There are no other coefficients, proving $\operatorname{div}_S(a)=P$. This controls codimension one only: an ideal with that principal divisor can still have nilpotent or embedded structure supported in codimension two. Faithful-flat valuation descent therefore does not, by itself, justify replacing the divisor equality by $aS=P$.

## The $R_0+S_1$ step

We record the depth argument separately because it closes that last gap.

[\[lem:R0S1\]]{#lem:R0S1 label="lem:R0S1"} Let $R'$ be a Cohen--Macaulay domain of dimension two and let $t\in R'$ be a nonzerodivisor whose principal divisor is one height-one prime with coefficient one. Then $R'/tR'$ is reduced and has that prime as its sole minimal prime.

Quotienting a Cohen--Macaulay ring by a nonzerodivisor lowers both dimension and depth by one. Thus $R'/tR'$ is a one-dimensional Cohen--Macaulay ring and satisfies $S_1$. Its minimal primes correspond to height-one primes in the support of $\operatorname{div}(t)$, so there is exactly one. At this minimal prime, coefficient one says that $t$ is a uniformizer of the DVR $R'_P$; hence $(R'/tR')_P$ is its residue field and is reduced. The quotient therefore satisfies $R_0$. A Noetherian ring is reduced exactly when it satisfies $R_0$ and $S_1$ [@stacks-033p].

Applying Lemma [\[lem:R0S1\]](#lem:R0S1){reference-type="ref" reference="lem:R0S1"} to $R'=S$ and $t=a$ proves that $S/aS$ is reduced with sole minimal prime $P/aS$. It is consequently a domain and $aS=P$. The lemma is the point that rules out a nilpotent supported only at a closed point of the scalar divisor.

## Normal comparison and the constants lemma

Write $\theta:D_n\to S/aS$ for the map in [\[eq:D-to-fiber\]](#eq:D-to-fiber){reference-type="eqref" reference="eq:D-to-fiber"}. It is finite: the target is finite over $\mathbb{Q}[c]$, and any finite set of $\mathbb{Q}[c]$-module generators also generates it as a $D_n$-module. Tensoring with $k=\mathbb{Q}(c)$ gives $$\theta_k:
 D_n\otimes_{\mathbb{Q}[c]}k
 \longrightarrow
 (S/aS)\otimes_{\mathbb{Q}[c]}k.$$ The source is the scalar exact-period field. The target is the residue field of the unique valuation above $(a)$, and the Henselian identification in Lemma [\[lem:henselian-valuation-descent\]](#lem:henselian-valuation-descent){reference-type="ref" reference="lem:henselian-valuation-descent"} identifies it with the same field. Thus $\theta_k$ is an isomorphism.

This generic isomorphism makes the injectivity and surjectivity assertions separate and explicit. If $x\in\ker(\theta)$, then $x$ becomes zero after inverting the nonzero elements of $\mathbb{Q}[c]$. Hence some nonzero polynomial in $\mathbb{Q}[c]$ annihilates $x$. The domain $D_n$ is torsion-free over $\mathbb{Q}[c]$, so $x=0$. We may therefore regard $D_n$ as a subring of the domain $S/aS$. The isomorphism $\theta_k$ also says that their fraction fields agree.

Every $y\in S/aS$ is integral over $\mathbb{Q}[c]$, hence integral over the larger coefficient ring $D_n$. Viewed in the common fraction field, such an element belongs to $D_n$ because $D_n$ is normal by the scalar smoothness theorem. Thus the inclusion is also surjective and $$D_n\simeq S/aS.$$ In other words, finite birationality supplies the common fraction field, whereas integral closedness supplies the missing ring-theoretic equality [@stacks-0309].

Finally, let $k'$ be the algebraic closure of $\mathbb{Q}$ inside $E_n$. The extension $k'/\mathbb{Q}$ is finite, all of $k'$ lies in $S$, and every nonzero element of $k'$ is a unit. The composite $$k'\hookrightarrow S\longrightarrow S/aS\hookrightarrow\operatorname{Frac}(D_n)$$ is injective. Because $D_n$ is geometrically integral, $\mathbb{Q}$ is algebraically closed in its function field, so $k'=\mathbb{Q}$. In characteristic zero this is the regularity criterion: $E_n/\mathbb{Q}$ is geometrically reduced and geometrically irreducible [@stacks-0322; @stacks-037p]. Base change of $S\hookrightarrow E_n$ to $\overline{\mathbb{Q}}$ stays injective, and the target is a domain. Thus $S_{\overline{\mathbb{Q}}}$ is a domain, completing the geometric-integrality argument [@stacks-0fwf].

# Scalar restriction and infinity-branch lemmas {#app:branches}

## Extraction of the scalar exact-period factor

Morton's scalar theorem gives, for $f_c(z)=z^d+c$ and every $b\geq1$, the Galois group $$\label{eq:scalar-product-wreath}
 \operatorname{Gal}(f_c^b(z)-z\,/\,\mathbb{Q}(c))
 \simeq \prod_{e\mid b}\bigl(C_e\mathbin{\wr}S_{r_d(e)}\bigr)$$ in its natural action on all fixed points [@morton-1998-periodic-galois]. The product decomposition respects the dynatomic idempotents. Projecting [\[eq:scalar-product-wreath\]](#eq:scalar-product-wreath){reference-type="eqref" reference="eq:scalar-product-wreath"} to the $e=n$ factor therefore gives $C_n\mathbin{\wr}S_r$ on the $\nu=nr$ marked points of exact period $n$, not merely on the roots of the full fixed polynomial.

Fakhruddin's formulation replaces $\mathbb{Q}$ by an arbitrary characteristic-zero constant field [@fakhruddin-2014-generic-endomorphisms]. With constant field $\overline{\mathbb{Q}}$, the same exact-period factor is the geometric group. The normal subgroup $C_n^r$ changes the marked point independently inside each cycle, while the quotient $S_r$ permutes the cycles. This explains both the scalar input and the passage from point monodromy to cycle monodromy used in Section [5](#sec:quotient){reference-type="ref" reference="sec:quotient"}.

## Compatible loci and the fundamental-group map

Let $U\subset\operatorname{Spec}A$ be a dense open on which both normalized covers are finite étale. The complement is a proper closed subset containing all branch divisors of the two finite separable generic extensions. The scalar line is not contained in that complement because the scalar generic point is étale. Removing finitely many additional scalar points gives a nonempty open $U_0\subset\operatorname{Spec}\mathbb{Q}[c]$ whose inclusion factors through $U$.

Fix a geometric point $\bar\eta_0$ of $(U_0)_{\overline{\mathbb{Q}}}$ and a geometric path from its image to a chosen base point $\bar\eta$ of $U_{\overline{\mathbb{Q}}}$. Functoriality of finite étale covers gives, up to the harmless conjugacy determined by the path, $$\pi_1((U_0)_{\overline{\mathbb{Q}}},\bar\eta_0)
 \longrightarrow
 \pi_1(U_{\overline{\mathbb{Q}}},\bar\eta).$$ Restricting the global cycle representation along this homomorphism is exactly the scalar cycle representation, because $S_0/aS_0\simeq D_n^{C_n}$. Hence the scalar image lies inside the global image. Since the scalar image is $S_r$, this supplies the global lower bound. No specialization map in the reverse direction is used.

More explicitly, denote the two permutation representations by $\varpi_U$ and $\varpi_0$, and denote the displayed homomorphism of fundamental groups by $i_*$. After identifying the scalar and global fibers through the normal scalar-fiber isomorphism, functoriality says $$\varpi_0=\varpi_U\circ i_*.$$ It follows formally that $\operatorname{im}(\varpi_0)\subseteq\operatorname{im}(\varpi_U)$. Reversing this inclusion would assert that every global loop comes from the scalar line, which neither the inclusion of opens nor the normalization comparison implies.

For marked points, the global representation commutes with $\sigma$. Choose labels $(j,i)$ with $1\leq j\leq r$ for the cycle and $i\in\mathbb Z/n\mathbb Z$ for the position, so that $\sigma(j,i)=(j,i+1)$. A permutation commuting with $\sigma$ permutes the $r$ cycles and chooses an independent cyclic translation in each cycle. Its centralizer is therefore $$C_{\mathfrak S_{\nu}}(\sigma)=C_n^r\rtimes S_r=C_n\mathbin{\wr}S_r.$$ Indeed, if $g\sigma=\sigma g$ and $g(j,0)=(\pi(j),t_j)$, then $$g(j,i)=g\sigma^i(j,0)=\sigma^ig(j,0)
       =(\pi(j),i+t_j).$$ Thus $g$ is determined by $\pi\in S_r$ and independent offsets $t_j\in\mathbb Z/n\mathbb Z$; conversely every such choice commutes with $\sigma$. Passing to cycles forgets precisely the normal offset subgroup $C_n^r$. This gives the global upper bound that matches the scalar lower bound.

## Existence and uniqueness of the infinity branches

We now justify the formal branches used in [\[eq:tau-leading\]](#eq:tau-leading){reference-type="eqref" reference="eq:tau-leading"}--[\[eq:rho-leading\]](#eq:rho-leading){reference-type="eqref" reference="eq:rho-leading"}. Work over a field containing $\mu_d$. On the scalar divisor the orbit recurrence is $$z_{i+1}=z_i^d+c.$$ Choose a ramified parameter $q$ at infinity by $c=-q^{-d}$ and put $$z_i=q^{-1}v_i,
 \qquad \epsilon=q^{d-1}.$$ Substitution and multiplication by $q^d$ give $$q^{-1}v_{i+1}=q^{-d}(v_i^d-1)
 \quad\Longleftrightarrow\quad
 q^{d-1}v_{i+1}=v_i^d-1
 \quad\Longleftrightarrow\quad
 v_i^d=1+\epsilon v_{i+1}.$$ Thus the rescaling fixes both the sign and the exponent of the local parameter. Consider the resulting system $$F_i(\mathbf v,\epsilon)
 =v_i^d-1-\epsilon v_{i+1}=0,
 \qquad i\in\mathbb Z/n\mathbb Z.$$ At $\epsilon=0$ and $\mathbf v=\boldsymbol{\omega}\in\mu_d^n$, the Jacobian with respect to the $v_i$ is diagonal: $$\left(\frac{\partial F_i}{\partial v_j}\right)_{\epsilon=0,\mathbf v=\boldsymbol{\omega}}
 =\operatorname{diag}
 (d\omega_0^{d-1},\ldots,d\omega_{n-1}^{d-1}).$$ Its determinant is nonzero in characteristic zero. The formal implicit function theorem, equivalently multivariable Hensel lifting, gives a unique $\mathbf v(\epsilon)\in\overline{\mathbb{Q}}[[\epsilon]]^n$ with constant term $\boldsymbol{\omega}$. Choosing the $d$th-root branch with constant term $\omega_i$ gives $$v_i=\omega_i(1+\epsilon v_{i+1})^{1/d}.$$ If $v_i=\omega_i+b_{i,1}\epsilon+b_{i,2}\epsilon^2+\cdots$, comparison at order one yields $$d\omega_i^{d-1}b_{i,1}=\omega_{i+1},
 \qquad
 b_{i,1}=\frac{\omega_i\omega_{i+1}}{d}.$$ At order $m$, the coefficient $b_{i,m}$ occurs with the invertible scalar $d\omega_i^{d-1}$, while all other terms involve lower-order coefficients and $b_{i+1,m-1}$. This recursively determines the formal solution.

Rotation is compatible with the complete series. If $\operatorname{rot}(\boldsymbol{\omega})=(\omega_1,\ldots,\omega_{n-1},\omega_0)$, then $(v_1,\ldots,v_{n-1},v_0)$ solves the system with that rotated constant term, so uniqueness identifies it with the lift of $\operatorname{rot}(\boldsymbol{\omega})$. If $\boldsymbol{\omega}$ has least rotational period $n$, its lifted branch cannot satisfy $f_c^e(z)=z$ for a proper divisor $e\mid n$, because reduction would make $\boldsymbol{\omega}$ invariant under rotation by $e$. Conversely, a nonprimitive word and its unique lift are periodic under a proper rotation. Thus primitive words index the actual-period branches at infinity, and primitive necklaces index cycles.

[\[lem:laurent-separation\]]{#lem:laurent-separation label="lem:laurent-separation"} Let $s\in S_0$, and let $\bar s$ be its scalar reduction. Suppose that, for one fixed $q$ with $c=-q^{-d}$, two primitive necklace branches give $$\bar s=q^{-m}(\alpha+O(q)),
 \qquad
 \bar s=q^{-m}(\beta+O(q)),
 \qquad \alpha\ne\beta.$$ Then $\bar s\notin\mathbb{Q}(c)$ and $s\notin K$.

A rational function $h(c)$ pulls back to the single Laurent series $h(-q^{-d})$, independently of the branch above the punctured $q$-disc. The unequal coefficients therefore rule out $\bar s\in\mathbb{Q}(c)$. If $s\in K$, then integrality and $S_0\cap K=A$ give $s\in A$. Its scalar reduction would lie in $\mathbb{Q}[c]\subset\mathbb{Q}(c)$, a contradiction.

## Independent leading terms

From $z_i=q^{-1}v_i$ and $v_i=\omega_i+O(\epsilon)$, summation gives $$\tau=q^{-1}
 \left(\omega_0+\cdots+\omega_{n-1}+O(\epsilon)\right).$$ No derivative formula enters this calculation. The comparison words below have unequal leading sums, so applying Lemma [\[lem:laurent-separation\]](#lem:laurent-separation){reference-type="ref" reference="lem:laurent-separation"} to this display gives the non-base conclusion for $\tau$.

For $\rho$, set $a=0$ in the derivative matrices. An induction on $m$ gives $$M_mM_{m-1}\cdots M_0
 =
 \begin{pmatrix}
 \prod_{i=0}^{m}u_i&0\\
 \prod_{i=0}^{m-1}u_i&0
 \end{pmatrix}.$$ Taking $m=n-1$ yields $$\rho=\prod_{i=0}^{n-1}u_i
 =d^n\prod_{i=0}^{n-1}z_i^{d-1}.$$ Substitution of the formal branches gives $$\rho=d^nq^{-n(d-1)}
 \left(\prod_{i=0}^{n-1}\omega_i^{d-1}
 +O(\epsilon)\right)
 =d^nq^{-n(d-1)}
 \left(\prod_{i=0}^{n-1}\omega_i^{-1}
 +O(\epsilon)\right).$$ This induction fixes the exponent, sign, and matrix order independently of the word-sum calculation. The same words have unequal inverse products. Applying Lemma [\[lem:laurent-separation\]](#lem:laurent-separation){reference-type="ref" reference="lem:laurent-separation"} to the product display, separately from the sum argument, gives the non-base conclusion for $\rho$.

## Primitivity of the comparison words and the rank-one case

For $d\geq3$, choose a primitive root $\zeta\in\mu_d$; this includes $n=2$. A word with one entry $\zeta$ and all other entries one cannot be $B^m$ with $m>1$, because the exceptional entry would occur in every copy of $B$. The same argument applies to $\zeta^2$. Since $d\geq3$, the two exceptional values are distinct, and a rotation cannot change one into the other. Hence the words define primitive, distinct necklaces. Their sums and inverse products are respectively $$n-1+\zeta,\quad n-1+\zeta^2,
 \qquad
 \zeta^{-1},\quad\zeta^{-2}.$$ Both pairs are distinct.

For $d=2$ and $n\geq3$, let $\boldsymbol{\omega}_1$ have exactly one negative entry and let $\boldsymbol{\omega}_2$ have exactly two cyclically adjacent negative entries. If a word is $B^m$ with $m>1$, its number of negative entries is divisible by $m$. This proves primitivity of $\boldsymbol{\omega}_1$. For $\boldsymbol{\omega}_2$, only $m=2$ remains. Then $n$ is even and the two inherited negative entries are separated by $n/2$. For even $n\geq4$ that distance is not one in either cyclic direction; for $n=3$, divisibility by two already fails. Thus $\boldsymbol{\omega}_2$ is primitive in every allowed binary case. The words cannot be rotations because they have different numbers of negative entries. Their sums are $n-2$ and $n-4$, while their products are $-1$ and $1$.

These pairs exhibit two primitive necklaces whenever $n\geq3$. When $n=2$, Möbius inversion gives $$\nu=d^2-d,\qquad r=\frac{d(d-1)}{2}.$$ Hence $r=1$ exactly when $d=2$. This proves that $(2,2)$ is the only rank-one case and justifies excluding it before either non-base proposition.

# Determinant lines and the rank-one calculation {#app:det}

## Characteristic polynomials of a projective algebra

Let $P$ be a finite locally free $A$-module of constant rank $r$ and let $\varphi\in\operatorname{End}_A(P)$. After extension to $A[T]$, the map $T\operatorname{id}-\varphi$ acts on the invertible module $$\det(P)_{A[T]}
 =\bigwedge_{A[T]}^r(P\otimes_AA[T]).$$ Every endomorphism of an invertible module is multiplication by a unique element of the base ring. We define $$\det(T\operatorname{id}-\varphi)\in A[T]$$ to be that element. On any open set where $P$ is free, this definition is the usual determinant of a matrix. Changes of basis conjugate that matrix, so the local polynomials agree on overlaps. The construction is therefore global and involves no preferred basis or trivialization of $\det(P)$.

[\[lem:determinant-base-change\]]{#lem:determinant-base-change label="lem:determinant-base-change"} For every $A$-algebra $B$, put $P_B=P\otimes_AB$ and $\varphi_B=\varphi\otimes1$. There are canonical identifications $$\bigwedge_B^rP_B\simeq
 \left(\bigwedge_A^rP\right)\otimes_AB
 \quad\text{and}\quad
 \det(T\operatorname{id}-\varphi_B)
 =\det(T\operatorname{id}-\varphi)\otimes_A1
 \quad\text{in }B[T].$$ In particular, the characteristic polynomial of an endomorphism of a finite projective algebra specializes to the characteristic polynomial of the specialized endomorphism, even when that algebra is not a product of fields.

Exterior powers of a finite locally free module commute with arbitrary base change. On an open set where $P$ is free, both sides have the basis formed by the same ordered $r$-fold wedges; these local identifications agree on overlaps. Apply this fact over $A[T]$ to $T\operatorname{id}-\varphi$. Its action on the determinant line is multiplication by $\det(T\operatorname{id}-\varphi)$. After tensoring with $B[T]$, the action is multiplication by the image of that polynomial. Functoriality also identifies this base-changed action with the top exterior power of $T\operatorname{id}-\varphi_B$, whose scalar is $\det(T\operatorname{id}-\varphi_B)$ by definition. Equality of the two scalars proves the formula. No flatness assumption on $B$ is needed, because finite projectivity of $P$ is imposed before base change.

Apply this construction to $P=S_0$ and $\varphi=m_s$ for $s\in\{\tau,\rho\}$. The resulting $\chi_s(T)$ is monic of degree $r$ with coefficients in $A$. After tensoring with $K$, it is the characteristic polynomial of multiplication by $s$ on the field $F$. For a prime $\mathfrak p\subset A$, Lemma [\[lem:determinant-base-change\]](#lem:determinant-base-change){reference-type="ref" reference="lem:determinant-base-change"} identifies its coefficientwise reduction with the characteristic polynomial of multiplication by $s\otimes1$ on $S_0\otimes_A\kappa(\mathfrak p)$. The degree remains $r$ because the specialized algebra is an $r$-dimensional vector space. Irreducibility and separability are different questions and are not asserted for every fiber.

[\[lem:minimal-characteristic\]]{#lem:minimal-characteristic label="lem:minimal-characteristic"} If $F=K(s)$ and $[F:K]=r$, then $\chi_s$ is the minimal polynomial of $s$ over $K$ and is irreducible of degree $r$.

The generation assumption makes $1,s,\ldots,s^{r-1}$ a $K$-basis of $F$. The matrix of multiplication by $s$ in this power basis is the companion matrix of the degree-$r$ minimal polynomial. Its characteristic polynomial is that same polynomial. Equivalently, the nonvanishing of $1\wedge s\wedge\cdots\wedge s^{r-1}$ says that the minimal polynomial has degree at least $r$, while it cannot exceed $\dim_KF=r$.

Because $A=\mathbb{Q}[a,c]$ is a UFD, a monic polynomial in $A[T]$ that factors nontrivially in $A[T]$ also factors in $K[T]$. Lemma [\[lem:minimal-characteristic\]](#lem:minimal-characteristic){reference-type="ref" reference="lem:minimal-characteristic"} therefore proves irreducibility over both $K$ and $A$. This is a generic field statement: after specializing $a$ and $c$, the polynomial may factor or acquire repeated roots.

## The top wedge and the discriminant

Put $$\Omega_s=1\wedge s\wedge\cdots\wedge s^{r-1}
 \in\bigwedge_A^rS_0,
 \qquad
 \omega_s=\Omega_s\otimes_A1
 \in\bigwedge_K^rF.$$ The generic criterion, its fiberwise base change, and the discriminant calculation can be stated in the same determinant line.

[\[lem:power-wedge-vandermonde\]]{#lem:power-wedge-vandermonde label="lem:power-wedge-vandermonde"} Assume $r\geq2$, and let $L/K$ contain a Galois closure of $F/K$. For $s\in S_0$, the following conditions are equivalent:

1.  $\omega_s\ne0$;

2.  $1,s,\ldots,s^{r-1}$ are linearly independent over $K$;

3.  $K(s)=F$;

4.  the values $s_i=\iota_i(s)$ under the $r$ embeddings $\iota_i:F\hookrightarrow L$ are pairwise distinct.

Under the canonical base-change map on determinant lines, $\omega_s$ is sent, up to the ordering sign, to $$\left(\prod_{1\leq i<j\leq r}(s_j-s_i)\right)
 e_1\wedge\cdots\wedge e_r.$$ The square of this coefficient is the discriminant of $\chi_s$. For every prime $\mathfrak p\subset A$, the image of $\Omega_s$ in $$\bigwedge_{\kappa(\mathfrak p)}^r
 \left(S_0\otimes_A\kappa(\mathfrak p)\right)$$ is exactly the power wedge of the specialized element.

The equivalence of (i) and (ii) is the alternating-multilinear criterion for a top wedge to be nonzero. The degree of the minimal polynomial of $s$ is the dimension of the span of $1,s,s^2,\ldots$. Since $F$ has dimension $r$ over $K$, the displayed $r$ powers are independent exactly when that minimal polynomial has degree $r$, or equivalently when $K(s)=F$. This proves the equivalence through (iii).

Characteristic zero makes $F/K$ separable. Extension to $L$ gives the $L$-algebra isomorphism $$F\otimes_KL\longrightarrow L^r,
 \qquad
 x\otimes\lambda\longmapsto
 (\lambda\iota_1(x),\ldots,\lambda\iota_r(x)).$$ The vectors corresponding to $1,s,\ldots,s^{r-1}$ are the columns of $$\begin{pmatrix}
 1&s_1&s_1^2&\cdots&s_1^{r-1}\\
 1&s_2&s_2^2&\cdots&s_2^{r-1}\\
 \vdots&\vdots&\vdots&&\vdots\\
 1&s_r&s_r^2&\cdots&s_r^{r-1}
 \end{pmatrix}.$$ Taking their top wedge yields its Vandermonde determinant $\prod_{i<j}(s_j-s_i)$. The coefficient is nonzero exactly when the $s_i$ are pairwise distinct, proving (iv) and the displayed formula. Under the equivalent conditions these values are the roots of the minimal and characteristic polynomials, so the squared coefficient is the discriminant of $\chi_s$.

For specialization, apply Lemma [\[lem:determinant-base-change\]](#lem:determinant-base-change){reference-type="ref" reference="lem:determinant-base-change"} with $B=\kappa(\mathfrak p)$. Each factor $s^j$ maps to $(s\otimes1)^j$, and functoriality of the wedge gives the asserted fiberwise element. A nonzero $\omega_s$ makes $\Omega_s$ a nonzero section of the invertible module $\bigwedge_A^rS_0$, but that section can vanish on a proper closed subset. Concretely, on a trivializing open $W$ write $\Omega_s=\delta_W e_W$ for a generator $e_W$ of the determinant line. At $\mathfrak p\in W$, the specialized power wedge is nonzero precisely when $\delta_W\notin\mathfrak p$. The changes of generator multiply $\delta_W$ by units, so these principal opens glue to a well-defined nonvanishing locus. Since $\omega_s\ne0$, this locus contains the generic point and is dense. Its complement is the fiberwise dependence locus of $1,s,\ldots,s^{r-1}$. Generic primitivity therefore gives nonvanishing on a dense open without asserting that every specialization remains primitive or separable.

When $r=1$, the criterion has a separate, tautological form. The power wedge is the single element $1\in\bigwedge_K^1F=F$, the characteristic polynomial is $T-s$, and the Vandermonde product is the empty product $1$. Its discriminant is also $1$. This nonvanishing contains no information about non-base behavior or nontrivial monodromy, which is why $(d,n)=(2,2)$ is handled directly below rather than included in Lemma [\[lem:power-wedge-vandermonde\]](#lem:power-wedge-vandermonde){reference-type="ref" reference="lem:power-wedge-vandermonde"}.

## Ordered two-step product

For reference, direct multiplication of $$M_0=\begin{pmatrix}u_0&a\\1&0\end{pmatrix},
 \qquad
 M_1=\begin{pmatrix}u_1&a\\1&0\end{pmatrix}$$ gives $$M_1M_0=
 \begin{pmatrix}
 u_1u_0+a&u_1a\\
 u_0&a
 \end{pmatrix}.$$ Thus $\operatorname{tr}(M_1M_0)=u_0u_1+2a$, while $\det(M_1M_0)=a^2$. This calculation separates the pointwise derivative trace from the return determinant.

## Direct calculation at $(d,n)=(2,2)$

Möbius inversion gives $\nu=2^2-2=2$ and $r=\nu/2=1$. Subtraction of the two equations in [\[eq:22-equations\]](#eq:22-equations){reference-type="eqref" reference="eq:22-equations"} yields $$(z_0-z_1)(z_0+z_1-(a-1))=0.$$ The factor $z_0-z_1$ is the fixed-point component. On the generic actual two-cycle factor, the second factor vanishes, so $$z_0+z_1=a-1.$$ To obtain the product without division, add the two cyclic equations: $$z_0^2+z_1^2+(a-1)(z_0+z_1)+2c=0.$$ Using $z_0^2+z_1^2=(z_0+z_1)^2-2z_0z_1$ and the displayed sum gives $$(a-1)^2-2z_0z_1+(a-1)^2+2c=0,$$ and hence $$z_0z_1=(a-1)^2+c.$$ With $u_i=2z_i$, the ordered matrix calculation gives $$\rho=u_0u_1+2a
 =4\bigl((a-1)^2+c\bigr)+2a
 =4a^2-6a+4+4c.$$ Therefore $$\nu=2,\qquad r=1,\qquad \tau=a-1,$$ $$z_0z_1=(a-1)^2+c,\qquad
 \rho=4a^2-6a+4+4c.$$ Since $S_0$ has rank one, multiplication by either observable has the linear polynomial recorded in Section [6](#sec:coordinates){reference-type="ref" reference="sec:coordinates"}. The calculation is a boundary verification, not evidence for non-base behavior or nontrivial cycle monodromy.
