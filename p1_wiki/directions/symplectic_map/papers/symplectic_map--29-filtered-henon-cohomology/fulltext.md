---
p1_kind: "derived-fulltext-reading-copy"
route: "symplectic_map"
logical_paper_id: "symplectic_map--29-filtered-henon-cohomology"
canonical_tex: "symplectic_map/papers/29-filtered-henon-cohomology/paper/main.tex"
canonical_pdf: "symplectic_map/papers/29-filtered-henon-cohomology/build/natural-20260906-r0/work/main.pdf"
source_sha256: "2cf3dd2419e4349910055da786bed739e0de02177ba3f2fc869fb07c97df86ea"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Filtered polynomial cohomology and finite periodic tests for symplectic Hénon maps

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symplectic_map/papers/29-filtered-henon-cohomology>)
- [规范 TeX](<../../../../../symplectic_map/papers/29-filtered-henon-cohomology/paper/main.tex>)
- [关联 PDF](<../../../../../symplectic_map/papers/29-filtered-henon-cohomology/build/natural-20260906-r0/work/main.pdf>)
- [支撑 Markdown](<../../../../../symplectic_map/papers/29-filtered-henon-cohomology/README.md>)
- [BibTeX](<../../../../../symplectic_map/papers/29-filtered-henon-cohomology/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We characterize polynomial additive coboundaries of finite compositions of area-preserving Hénon maps over a field of characteristic zero, with exact control of the ordinary-degree filtration. Although substitution can increase degree, every coboundary of degree at most $D$ has a polynomial primitive of degree at most $D$; rational primitives give no additional solutions. An orbit-coordinate basis and the discrete convexity of its degrees give this bound, while a mixed-radix re-encoding yields the exact Hilbert series of the filtered obstruction space. The resulting dimensions are independent of all polynomial coefficients once the ordered phase degrees are fixed. We also prove that vanishing of an orbit sum on one sufficiently long complete fixed-point scheme is equivalent to global solvability. The required period is logarithmic in $D$, and the testing algebra has length at most $\delta^4D^4$, where $\delta$ is the degree product of the composition. For a single map of degree at least three, explicit aliases show that the leading constant four in the eventual uniform period threshold cannot be lowered. Binary and multiphase boundary examples explain the precise scope of this assertion. Finally, a univariate rigidity theorem determines the entire rational invariant field of a parameter-preserving symplectic lift, including its exact polynomial translation exception.
author:
- Anonymous
bibliography:
- references.bib
title: |
  Filtered polynomial cohomology and finite periodic tests\
  for symplectic Hénon maps
```

## Markdown 正文

# Introduction {#sec:introduction}

For a polynomial automorphism $F$ of the affine plane, the additive cohomological equation $$f\circ F-f=g
  \label{eq:cohomological-equation}$$ asks whether an observable $g$ is the difference of a function along one iteration. Its periodic sums must vanish whenever the equation is solvable. For polynomial observables, however, this necessary condition leaves several distinct questions: which polynomial obstructions are complete, how large a primitive must be, and whether bounded-degree solvability can be decided from one finite algebra of periodic data. We answer these questions for finite compositions of area-preserving Hénon maps, without assumptions of hyperbolicity, generic coefficients or simple periodic points.

Let $K$ be a field of characteristic zero and let $p_0,\ldots,p_{k-1}\in K[T]$, with $d_i=\deg p_i\ge2$. Throughout the first six sections we consider $$H_i(x,y)=(p_i(x)-y,x),\qquad
  F=H_{k-1}\circ\cdots\circ H_0,\qquad
  \delta=\prod_{i=0}^{k-1}d_i,
  \label{eq:intro-map}$$ and write $\sigma=F^*$ for pullback. Each factor preserves the area form $\mathrm dx\wedge\mathrm dy$. The leading coefficients of the $p_i$ need only be nonzero, and all their lower coefficients are unrestricted. Put $$A=K[x,y],\qquad V_D=A_{\le D},\qquad
  \mathcal H=A/(\sigma-1)A,\qquad
  \mathcal H_D=\mathop{\mathrm{im}}(V_D\longrightarrow\mathcal H).
  \label{eq:intro-filtration}$$ Here $\mathcal H$ is a quotient of vector spaces. The image $(\sigma-1)A$ is not being treated as an ideal, and the filtration is ordinary total degree in the specified coordinates $x,y$.

The degree filtration is the main additional constraint. Even when $f$ has small degree, $\sigma f$ can have much larger degree, so an a priori search for a primitive cannot simply assume that its degree is bounded by that of $g$. Nor does a finite-dimensional quotient recording periodic points automatically retain all global coboundary obstructions. Our proofs resolve both issues through one basis. The recurrence $p_i(X_i)=X_{i-1}+X_{i+1}$, with $X_0=x$ and $X_{-1}=y$, produces orbit coordinates indexed by the integers. Their bounded-exponent products form a basis permuted by the macro shift $i\mapsto i+k$. Its leading monomials are indexed bijectively by two nonnegative integers, through the mixed-radix expansions on the two sides of the initial coordinate pair. Thus the same basis records both the actual polynomial degree and the global shift obstructions.

The principal conclusions are as follows.

1.  *Complete obstructions with no degree loss.* The normal-form constant coefficient and the coefficient sum on every nonconstant basis orbit characterize all polynomial coboundaries. Whenever $g\in V_D$ is a coboundary, it has a primitive in $V_D$, unique modulo $K$. Rational primitives are automatically polynomial. The uniform degree bound is attained in the single-factor subclass (Theorem [\[thm:bounded-primitive\]](#thm:bounded-primitive){reference-type="ref" reference="thm:bounded-primitive"} and Corollary [\[cor:rational-reduction\]](#cor:rational-reduction){reference-type="ref" reference="cor:rational-reduction"}).

2.  *Exact filtered dimensions.* Theorem [\[thm:hilbert\]](#thm:hilbert){reference-type="ref" reference="thm:hilbert"} computes the associated-graded Hilbert series of $\mathcal H$ from an explicit permutation of $\{0,\ldots,\delta-1\}$ determined by the ordered phase degrees. In the single-factor case of degree $d$, the cumulative dimension satisfies $\dim_K\mathcal H_D=\frac{d-1}{2(d+1)}D^2+O_d(D)$. The full series can distinguish compositions having the same degree product; this is a statement about the specified coordinate filtration, not an arbitrary polynomial-conjugacy invariant.

3.  *One effective periodic scheme.* For an explicit phase-dependent support bound $L_{\rm ph}(D)$, every macro period $n$ with $kn\ge3$ and $kn>2L_{\rm ph}(D)$ detects all coboundaries in $V_D$ by one scheme identity. A logarithmic choice of $n$ gives a testing algebra of length at most $\delta^4D^4$ for $D\ge1$. For a single map of degree $d\ge3$, the leading constant four in the eventual uniform threshold is sharp. This sharpness concerns all periods above a threshold, not the shortest specially chosen test (Theorems [\[thm:periodic-test\]](#thm:periodic-test){reference-type="ref" reference="thm:periodic-test"}, [\[thm:effective-period\]](#thm:effective-period){reference-type="ref" reference="thm:effective-period"} and [\[thm:sharp-threshold\]](#thm:sharp-threshold){reference-type="ref" reference="thm:sharp-threshold"}).

4.  *A fixed-field application.* For one Hénon factor, a right-hand side depending only on $x$ forces the primitive to be linear in $x-y$. Applied over $K=\mathbb C(a)$, this rigidity determines the entire rational invariant field of the parameter-preserving symplectic lift studied in Section [8](#sec:symplectic-lift){reference-type="ref" reference="sec:symplectic-lift"}. Its additional invariant exists exactly for a polynomial translation of the potential; even in that case there is no rational Liouville pair (Theorems [\[thm:univariate\]](#thm:univariate){reference-type="ref" reference="thm:univariate"} and [\[thm:lift-field\]](#thm:lift-field){reference-type="ref" reference="thm:lift-field"}).

The periodic assertion uses a precise form of finite data. For $S_ng=\sum_{j=0}^{n-1}\sigma^jg$, the test is $$S_ng=0\quad\hbox{in }K[\mathop{\mathrm{Fix}}(F^n)].
  \label{eq:intro-scheme-test}$$ This coordinate algebra includes multiplicities and points whose least period divides $n$. The test is neither a scalar average over all periodic points nor a condition on one chosen orbit. If the fixed-point scheme is nonreduced, vanishing at every geometric point is weaker than [\[eq:intro-scheme-test\]](#eq:intro-scheme-test){reference-type="eqref" reference="eq:intro-scheme-test"}. The distinction is part of the statement, not a regularity assumption deferred to the proof.

#### Normal forms and prior algebraic constructions.

The orbit-algebra approach starts from Bousch's quadratic Hénon algebras [@Bousch1992HenonAlgebras]. His unpublished manuscript establishes bounded-exponent bases in the finite and infinite settings, wrapping onto cyclic indices, and the shift description of pullback; it also keeps track of nonreduced periodic algebras. We give the general-degree, multiphase construction needed here, including its identification with the actual coordinate ring. The coefficient-sum criterion on a permuted basis is then elementary linear algebra. Neither the basis mechanism nor this linear-algebra consequence is presented as a new framework. The further work is the strict control of ordinary degree, its exact filtered count, and the no-alias argument that turns one complete periodic scheme into a global test.

#### Finite periodic cohomology.

Finite Livšic results provide a related but different passage from periodic information to cohomological conclusions. Pollicott and Sharp [@PollicottSharp2004FiniteLivsic] obtain quantitative approximate conclusions for Hölder functions over transitive Anosov diffeomorphisms. Gouëzel and Lefeuvre [@GouezelLefeuvre2021FiniteLivsic] prove a finite approximate Livšic theorem for transitive Anosov flows. Those results concern analytic estimates from short periodic trajectories. Here the function class is polynomial, the equality is exact, and all data lie in a single complete fixed-point algebra. We impose no hyperbolic hypothesis, but we also make no claim that our algebraic theorem supplies their regularity or approximation conclusions.

#### Additive extensions and the application.

The fixed-field reduction uses the classical additive-extension criterion of Karr in the form recalled by Schneider [@Schneider2016DifferenceRings]. A related coefficient-comparison mechanism occurs in the contact lifts of Cerveau and Déserti [@CerveauDeserti2018Contact]. We include a short proof of the difference-field step, retaining the leading-coefficient ratio needed to identify the whole invariant field. The object-specific input is the univariate Hénon equation and the resulting exact condition on the polynomial potential. The contact setting is not identified with the four-dimensional symplectic setting considered here.

Sections [2](#sec:orbit-algebras){reference-type="ref" reference="sec:orbit-algebras"}--[4](#sec:hilbert-series){reference-type="ref" reference="sec:hilbert-series"} construct the basis, prove the degree bound and count the filtered obstructions. Sections [5](#sec:periodic-detection){reference-type="ref" reference="sec:periodic-detection"}--[6](#sec:effective-periods){reference-type="ref" reference="sec:effective-periods"} establish periodic detection and its boundary phenomena. Sections [7](#sec:univariate-rigidity){reference-type="ref" reference="sec:univariate-rigidity"}--[8](#sec:symplectic-lift){reference-type="ref" reference="sec:symplectic-lift"} give the rigidity theorem and fixed-field application. All proofs are included in the body. The quartic algebra-length estimate measures the size of one exact periodic certificate, not optimal computational complexity; the degree bound also permits a direct linear search for a primitive with $O(D^2)$ unknown coefficients.

# Orbit algebras and the Hénon composition {#sec:orbit-algebras}

The quadratic Hénon algebra basis, its finite and infinite versions, and the wrapping description of the dynamics are due to @Bousch1992HenonAlgebras. The construction below extends that normal-form argument to the prescribed phase degrees. We give the reduction and the identifications explicitly because both the ordinary-degree filtration and the scheme-valued periodic test will use the actual basis, not merely a generating family. The orbit-coefficient obstruction obtained from this basis in the next section is a linear-algebra consequence of its permutation action.

Throughout, $K$ is a field of characteristic zero and $A=K[x,y]$. Fix $k\ge1$ and polynomials $p_0,\ldots,p_{k-1}$ of degrees $d_i\ge2$, and extend the subscripts periodically to $\mathbb Z$. Write $$H_i(x,y)=(p_i(x)-y,x),\qquad
  F=H_{k-1}\circ\cdots\circ H_0,\qquad
  \sigma=F^*,\qquad \delta=\prod_{i=0}^{k-1}d_i.
  \label{eq:henon-composition}$$ Here $F^*f=f\circ F$. The inverse of $H_i$ is $(x,y)\mapsto(y,p_i(y)-x)$, so these maps and $F$ are polynomial automorphisms. They preserve $\mathrm dx\wedge\mathrm dy$, since $\mathrm d(p_i(x)-y)\wedge\mathrm dx=\mathrm dx\wedge\mathrm dy$. No normalization of their nonzero leading coefficients is imposed.

The orbit coordinates are the polynomials determined by $$X_0=x,\qquad X_{-1}=y,\qquad
  p_i(X_i)=X_{i-1}+X_{i+1}\quad(i\in\mathbb Z).
  \label{eq:orbit-recurrence}$$ The recurrence defines them in both directions: solve for $X_{i+1}$ starting at $i=0$, and for $X_{i-1}$ starting at $i=-1$. An exponent word is a finitely supported sequence $e=(e_i)_{i\in\mathbb Z}$ of integers with $0\le e_i<d_i$. For such a word put $$M_e=\prod_{i\in\mathbb Z}X_i^{e_i},\qquad
  \mathcal B=\{M_e:0\le e_i<d_i,\ e\text{ finitely supported}\}.
  \label{eq:standard-orbit-monomials}$$ The zero word gives $M_0=1$.

[\[thm:orbit-basis\]]{#thm:orbit-basis label="thm:orbit-basis"} The family $\mathcal B$ is a $K$-basis of $A$. More precisely, the evaluation map $Z_i\mapsto X_i$ identifies $A$ with $$A_\infty=
  K[Z_i:i\in\mathbb Z]\big/
  (p_i(Z_i)-Z_{i-1}-Z_{i+1}:i\in\mathbb Z),$$ and the residue classes of the monomials $\prod_iZ_i^{e_i}$ with $0\le e_i<d_i$ form a basis of this quotient.

Write $p_i(T)=a_iT^{d_i}+q_i(T)$, where $a_i\in K^*$ and $\deg q_i<d_i$. In $R_\infty=K[Z_i:i\in\mathbb Z]$ consider the rules $$Z_i^{d_i}\longrightarrow r_i,
  \qquad
  r_i=a_i^{-1}\bigl(Z_{i-1}+Z_{i+1}-q_i(Z_i)\bigr).
  \label{eq:pure-power-rewrite}$$ Every polynomial in $R_\infty$ involves only finitely many variables. Although a rule can introduce a neighboring index that was absent from the input, this does not prevent termination. Replacing a factor $Z_i^{d_i}$ in a monomial of total degree $m$ produces only monomials of degree at most $m-1$. A recursively expanded monomial therefore has a finitely branching reduction tree of depth at most $m$. Arbitrary orders of polynomial reduction terminate as well. If the input has degree at most $D$, list the numbers of its current nonzero monomial terms in degrees $D,D-1,\ldots,0$, in this order. Every reduction strictly decreases this finite tuple in lexicographic order: one term at the degree being reduced is removed, and only lower degrees can receive new terms. Cancellations can only decrease the tuple further. Lexicographic descent on a fixed finite product of copies of $\mathbb Z_{\ge0}$ is well founded.

We next prove uniqueness of reduction by induction on the degree of a monomial. Irreducible monomials require no choice. If a monomial admits two reductions by the same rule, the resulting polynomial is the same, since selecting a different copy of the identical pure-power factor does not change the quotient monomial. For different rules $i\ne j$, their pure powers are relatively prime. Thus a monomial $M$ divisible by both can be reduced, first at $i$ and then using the retained factor $Z_j^{d_j}$ in every expanded term, to $$\frac{M}{Z_i^{d_i}Z_j^{d_j}}\,r_ir_j.
  \label{eq:common-multiple-reduction}$$ Reversing the order gives the identical polynomial. This remains true when the indices are adjacent and $r_i$ contains $Z_j$: the original $Z_j^{d_j}$ factor is still present before the second replacement. All monomials after the first step have degree smaller than $\deg M$, so the induction hypothesis makes their subsequent complete reductions unique. Consequently the two first choices have the same normal form.

Extend this normal form linearly and denote it by $\mathop{\mathrm{NF}}_\infty$. The preceding argument also handles a reduction performed in any one term of a polynomial. For every monomial $M$ and every $i$ it gives $$\mathop{\mathrm{NF}}_\infty\bigl(M(Z_i^{d_i}-r_i)\bigr)=0.$$ Hence $\mathop{\mathrm{NF}}_\infty$ annihilates the relation ideal. Conversely, a reduction changes a polynomial by an element of that ideal and fixes each irreducible monomial. Every class is therefore spanned by the bounded-exponent monomials, and a linear combination of them lying in the ideal must be zero: applying $\mathop{\mathrm{NF}}_\infty$ leaves that combination unchanged. This proves linear independence as well as spanning.

It remains to identify the quotient with the specified phase space. The recurrence [\[eq:orbit-recurrence\]](#eq:orbit-recurrence){reference-type="eqref" reference="eq:orbit-recurrence"} gives a homomorphism $$\Psi:A_\infty\longrightarrow A,\qquad [Z_i]\longmapsto X_i.$$ In the reverse direction define $$\Theta:A\longrightarrow A_\infty,\qquad
  x\longmapsto[Z_0],\quad y\longmapsto[Z_{-1}].$$ The composite $\Psi\Theta$ fixes $x$ and $y$. Inside $A_\infty$, solving the defining relations successively to the right and to the left expresses each $[Z_i]$ as $X_i([Z_0],[Z_{-1}])$. Therefore $\Theta\Psi$ fixes every generator $[Z_i]$ and is the identity as well. These homomorphisms are inverse, and the abstract basis becomes precisely [\[eq:standard-orbit-monomials\]](#eq:standard-orbit-monomials){reference-type="eqref" reference="eq:standard-orbit-monomials"}.

For $g\in A$, its normal form means its unique finite expansion in $\mathcal B$. We identify the abstract bounded-exponent monomials with their polynomial images from now on. In particular, the coefficient of $M_0=1$ refers to this expansion and need not be the constant coefficient in the original variables $x,y$.

[\[prop:macro-shift\]]{#prop:macro-shift label="prop:macro-shift"} For every $i\in\mathbb Z$, $$\sigma X_i=X_{i+k}.
  \label{eq:macro-shift}$$ Thus $\sigma$ permutes $\mathcal B$ by shift-$k$, and normal-form reduction commutes with this shift.

Successive application of $H_0,\ldots,H_{k-1}$ sends $(x,y)$ to $(X_k,X_{k-1})$. This proves [\[eq:macro-shift\]](#eq:macro-shift){reference-type="eqref" reference="eq:macro-shift"} for $i=0,-1$. Applying $\sigma$ to [\[eq:orbit-recurrence\]](#eq:orbit-recurrence){reference-type="eqref" reference="eq:orbit-recurrence"} shows that $(\sigma X_i)_{i\in\mathbb Z}$ satisfies the same recurrence as $(X_{i+k})_{i\in\mathbb Z}$, because $p_{i+k}=p_i$. The two adjacent initial values determine all other values in both directions, which proves the formula for every $i$. Since $d_{i+k}=d_i$, a shifted admissible word is still admissible. The shift also preserves the relations in [\[eq:pure-power-rewrite\]](#eq:pure-power-rewrite){reference-type="eqref" reference="eq:pure-power-rewrite"}; uniqueness of their normal forms proves the last assertion.

The shift in this proposition is attached to the chosen composition. Even if some or all of the phase polynomials coincide, replacing shift-$k$ by shift-$1$ changes the cohomological equation for $F$.

For periodic data we need a finite version of the same algebra. Let $n\ge1$ and put $N=kn\ge3$. Since $k$ divides $N$, the phase data are well defined on $\mathbb Z/N\mathbb Z$. Define $$A_N=K[Z_i:i\bmod N]\big/
  (p_i(Z_i)-Z_{i-1}-Z_{i+1}:i\bmod N).
  \label{eq:finite-orbit-algebra}$$ All subscripts in this presentation are cyclic. Write $\sigma_N[Z_i]=[Z_{i+k}]$ for the induced automorphism.

[\[prop:periodic-algebra\]]{#prop:periodic-algebra label="prop:periodic-algebra"} For $N=kn\ge3$, the algebra $A_N$ has basis $$\mathcal B_N=
  \left\{\prod_{i=0}^{N-1}[Z_i]^{e_i}:0\le e_i<d_i\right\}
  \quad\text{and}\quad
  \dim_K A_N=\delta^n.
  \label{eq:finite-basis-length}$$ There is a surjective wrapping homomorphism $W_N:A\to A_N$ with $W_N(X_i)=[Z_{i\bmod N}]$, and $$\ker W_N=J_N:=(X_N-X_0,\ X_{N-1}-X_{-1}).
  \label{eq:fixed-scheme-ideal}$$ Consequently $$A_N\simeq A/J_N=K[\mathop{\mathrm{Fix}}(F^n)],\qquad
  W_N\sigma=\sigma_NW_N,\qquad \sigma_N^n=1.
  \label{eq:fixed-scheme-identification}$$ These are identities for the complete fixed-point scheme; no reducedness assumption is needed.

The cyclic version of [\[eq:pure-power-rewrite\]](#eq:pure-power-rewrite){reference-type="eqref" reference="eq:pure-power-rewrite"} still replaces each pure power by terms of strictly smaller total degree. Its distinct leading pure powers remain relatively prime, and the common-multiple calculation [\[eq:common-multiple-reduction\]](#eq:common-multiple-reduction){reference-type="eqref" reference="eq:common-multiple-reduction"} is unchanged. The termination, uniqueness, and independence argument in the proof of Theorem [\[thm:orbit-basis\]](#thm:orbit-basis){reference-type="ref" reference="thm:orbit-basis"} therefore applies to this finite set of variables. It gives $\mathcal B_N$ as a basis, with cardinality $\prod_{i=0}^{N-1}d_i=\delta^n$.

Sending every infinite index to its residue modulo $N$ respects all relations and defines $W_N$. Each finite generator is in its image, so it is surjective. Both generators of $J_N$ map to zero. To prove that they give the entire kernel, work first in $A/J_N$. The sequences $(X_{i+N})$ and $(X_i)$ have the same two adjacent values at $i=0,-1$. They satisfy the same recurrence since $p_{i+N}=p_i$. Induction in both directions gives $$X_{i+N}=X_i\quad\text{in }A/J_N\quad(i\in\mathbb Z).$$ It follows that $[Z_{i\bmod N}]\mapsto[X_i]$ defines a homomorphism $A_N\to A/J_N$. It is inverse to the homomorphism induced by $W_N$: one composite fixes all cyclic generators, and the other fixes the classes of $x,y$. This proves [\[eq:fixed-scheme-ideal\]](#eq:fixed-scheme-ideal){reference-type="eqref" reference="eq:fixed-scheme-ideal"}.

Proposition [\[prop:macro-shift\]](#prop:macro-shift){reference-type="ref" reference="prop:macro-shift"} gives $F^{n*}(x,y)=(X_N,X_{N-1})$. The equalizer of $F^n$ and the identity on the affine plane has exactly the ideal $J_N$, which proves the scheme identification, not only an identification of its point set. The intertwining formula follows on the generators $X_i$, and shifting by $nk=N$ fixes every cyclic generator. The dimension already proved is thus the algebra length of this scheme, including multiplicities.

# The ordinary-degree filtration and bounded primitives {#sec:filtered-primitives}

The basis of Section [2](#sec:orbit-algebras){reference-type="ref" reference="sec:orbit-algebras"} also records ordinary polynomial degree exactly. This is stronger than controlling the total number of factors in a word: an orbit coordinate far from $X_{-1},X_0$ has large degree in $x,y$. We first identify those degrees and show that different standard words cannot cancel their highest terms.

Set $V_D=\{g\in A:\deg g\le D\}$ for $D\ge0$ and $V_{-1}=0$, with the convention $\deg0=-\infty$. Define the phase-product weights $$w_0=w_{-1}=1,\qquad
  w_i=\prod_{h=0}^{i-1}d_h\quad(i\ge1),\qquad
  w_i=\prod_{h=i+1}^{-1}d_h\quad(i\le-2).
  \label{eq:phase-weights}$$ For an admissible exponent word $e$ put $$A(e)=\sum_{i\ge0}e_iw_i,\qquad
  B(e)=\sum_{i\le-1}e_iw_i,\qquad
  \mu(M_e)=A(e)+B(e).
  \label{eq:word-degree}$$ Both sums are finite. The symbols $A(e),B(e)$ in this pair denote nonnegative integers; the ambient polynomial ring remains $A=K[x,y]$.

[\[lem:degree-basis\]]{#lem:degree-basis label="lem:degree-basis"} The highest homogeneous part of $M_e$ is $$c_e x^{A(e)}y^{B(e)},\qquad c_e\in K^*,
  \label{eq:word-highest-term}$$ and $e\mapsto(A(e),B(e))$ is a bijection from admissible exponent words to $\mathbb Z_{\ge0}^2$. In particular, for every nonzero finite linear combination, $$\deg\left(\sum_e c'_eM_e\right)
    =\max_{c'_e\ne0}\mu(M_e).
  \label{eq:degree-no-cancellation}$$ The words of weight at most $D$ form a basis of $V_D$, and $\dim_K V_D=\binom{D+2}{2}$.

For $i\ge0$, the highest homogeneous part of $X_i$ is a nonzero multiple of $x^{w_i}$. At $i=0$ this is the definition, and at $i=1$ it follows from $X_1=p_0(x)-y$, since $d_0\ge2$. Suppose the assertion has been proved through index $i\ge1$. The degree of $p_i(X_i)$ is $d_iw_i=w_{i+1}$, with a nonzero pure $x$-power as its highest term. On the other hand, $\deg X_{i-1}=w_{i-1}<w_{i+1}$. Subtracting $X_{i-1}$ in [\[eq:orbit-recurrence\]](#eq:orbit-recurrence){reference-type="eqref" reference="eq:orbit-recurrence"} therefore cannot remove that term. This proves the positive assertion by induction.

For the negative direction start with $X_{-1}=y$ and $X_{-2}=p_{-1}(y)-x$. If the assertion is known at $i\le-2$ and $i+1$, then $$X_{i-1}=p_i(X_i)-X_{i+1},\qquad
  d_iw_i=w_{i-1}>w_{i+1}.$$ Thus the highest part of $X_{i-1}$ is a nonzero pure $y$-power of degree $w_{i-1}$. This proves the negative assertion too. Multiplying the highest homogeneous parts now gives [\[eq:word-highest-term\]](#eq:word-highest-term){reference-type="eqref" reference="eq:word-highest-term"}, including its nonzero coefficient.

On the nonnegative ray, the place values are $1,d_0,d_0d_1,\ldots$, and the digit at place $i$ is constrained by $0\le e_i<d_i$. Repeated Euclidean division gives each integer $a\ge0$ a unique expansion in these place values: divide $a$ by $d_0$ to obtain $e_0$ as remainder, divide the quotient by $d_1$ to obtain $e_1$, and continue. Each nonzero quotient strictly decreases because every divisor is at least two, so the expansion is finite. Conversely, successively taking these remainders recovers every digit from the expansion, proving uniqueness. On the negative ray the same procedure uses the successive bases $d_{-1},d_{-2},\ldots$ and the place values $w_{-1},w_{-2},\ldots$. The two choices are independent, proving the claimed bijection to pairs of nonnegative integers.

For a nonzero combination in [\[eq:degree-no-cancellation\]](#eq:degree-no-cancellation){reference-type="eqref" reference="eq:degree-no-cancellation"}, let $m$ be the largest word weight occurring. Words of smaller weight do not contribute to the homogeneous part of degree $m$. The words of weight $m$ contribute distinct monomials $x^{A(e)}y^{B(e)}$ by the bijection, each with a nonzero scalar coefficient. Their sum cannot vanish. This proves the exact degree formula. Applying it to the unique orbit-basis expansion of a polynomial shows that a polynomial belongs to $V_D$ exactly when all its occurring words have weight at most $D$. Finally, the number of pairs $(a,b)\in\mathbb Z_{\ge0}^2$ with $a+b\le D$ is $\binom{D+2}{2}$.

We now compute the additive obstructions before imposing a degree bound. The action of $\sigma$ on every nonconstant element of $\mathcal B$ has an infinite orbit. Indeed, if a nonzero power of shift-$k$ fixed an admissible nonempty word, it would fix its finite nonempty support under a nonzero translation of $\mathbb Z$. Comparing the least support index rules this out.

Choose one representative $M_O$ of each nonconstant $\sigma$-orbit $O$. For $g\in A$ its unique expansion can be written as $$g=c_0+\sum_O\sum_{r\in\mathbb Z}c_{O,r}\,\sigma^rM_O,
  \qquad c_O=\sum_{r\in\mathbb Z}c_{O,r}.
  \label{eq:orbit-coefficients}$$ Only finitely many coefficients in this display are nonzero. Changing a representative reindexes the inner sum and leaves $c_O$ unchanged. Here $c_0$ is the coefficient of the basis element $1$.

[\[thm:orbit-obstructions\]]{#thm:orbit-obstructions label="thm:orbit-obstructions"} For $g\in A$, the equation $\sigma f-f=g$ has a solution $f\in A$ if and only if $c_0=0$ and $c_O=0$ for every nonconstant orbit in [\[eq:orbit-coefficients\]](#eq:orbit-coefficients){reference-type="eqref" reference="eq:orbit-coefficients"}. When a solution exists, one is given by $$f=\sum_O\sum_{r\in\mathbb Z}u_{O,r}\,\sigma^rM_O,
  \qquad u_{O,r}=-\sum_{s\le r}c_{O,s}.
  \label{eq:cumulative-primitive}$$ All solutions differ by an element of $K$. Thus the vector-space quotient $\mathcal H=A/(\sigma-1)A$ has one basis class for the constant word and one for each nonconstant $\sigma$-orbit.

Write a prospective primitive in the same basis, with coefficients $u_{O,r}$. The coefficient of $\sigma^rM_O$ in $\sigma f-f$ is $u_{O,r-1}-u_{O,r}$. The coefficient of $1$ is zero, and summing the differences over an orbit gives zero because the sequence has finite support. This proves necessity.

Conversely, assume the stated obstructions vanish. For a fixed orbit, the cumulative sum in [\[eq:cumulative-primitive\]](#eq:cumulative-primitive){reference-type="eqref" reference="eq:cumulative-primitive"} is zero below the least index with $c_{O,r}\ne0$. It is also zero at and above the greatest such index, because the total coefficient sum is zero. It therefore has finite support, and only finitely many orbits occur. The formula defines a polynomial. Its coefficients satisfy $u_{O,r-1}-u_{O,r}=c_{O,r}$, so its difference is $g$.

If $\sigma f=f$, then the coefficients of $f$ are constant along each nonconstant orbit. An infinite orbit cannot support a nonzero constant coefficient sequence in a polynomial, so all these coefficients vanish. Thus $\ker(\sigma-1)=K$, proving uniqueness modulo constants. The obstruction map $g\mapsto(c_0,(c_O)_O)$ is surjective onto the direct sum of one copy of $K$ for each listed basis class, and the equivalence just proved identifies its kernel with $(\sigma-1)A$. This proves the description of the quotient.

The normal constant coefficient is essential. For example, if $k=1$ and $p(x)=x^2+c$, then $\sigma x-x=x^2-y-x+c$ has ordinary constant coefficient $c$, whereas its orbit-basis expression is $X_1-X_0$ and has normal constant coefficient zero.

The cumulative formula becomes degree effective because an orbit cannot leave and then reenter a degree sublevel set between two of its terms. The following argument establishes this property for arbitrary phase degrees, including across the two sides of the initial coordinate pair.

[\[thm:bounded-primitive\]]{#thm:bounded-primitive label="thm:bounded-primitive"} For every integer $D\ge0$, $$g\in V_D\cap(\sigma-1)A
  \quad\Longrightarrow\quad
  g=\sigma f-f\ \text{for some }f\in V_D.
  \label{eq:bounded-primitive}$$ The primitive may be taken to be [\[eq:cumulative-primitive\]](#eq:cumulative-primitive){reference-type="eqref" reference="eq:cumulative-primitive"}, and then $\sigma f\in V_D$ as well. The degree bound is attained for every $D\ge1$ within the scalar subclass $k=1$.

Fix a residue $u$ with $0\le u<k$ and set $a=w_u$, $b=w_{u-k}$. Phase periodicity and [\[eq:phase-weights\]](#eq:phase-weights){reference-type="eqref" reference="eq:phase-weights"} give the exact macro-step sequence $$\bigl(w_{u+rk}\bigr)_{r\in\mathbb Z}
  =\bigl(\ldots,\delta^2b,\delta b,b,a,
                 \delta a,\delta^2a,\ldots\bigr),
  \label{eq:macro-weight-sequence}$$ where $r=-1$ corresponds to $b$ and $r=0$ to $a$. On either geometric tail, the second difference is a positive multiple of $(\delta-1)^2$. At the two central entries $b$ and $a$ the second differences are, respectively, $$a+(\delta-2)b,\qquad b+(\delta-2)a.
  \label{eq:central-second-differences}$$ They are positive since $a,b>0$ and $\delta\ge2$. Thus $r\mapsto w_{i+rk}$ is discretely convex for every index $i$; changing $i$ within the same residue class only translates the sequence. No comparison between $a$ and $b$ is required.

For an admissible word, Proposition [\[prop:macro-shift\]](#prop:macro-shift){reference-type="ref" reference="prop:macro-shift"} and Lemma [\[lem:degree-basis\]](#lem:degree-basis){reference-type="ref" reference="lem:degree-basis"} give $$h_e(r):=\deg(\sigma^rM_e)=\sum_i e_iw_{i+rk}.$$ This finite nonnegative linear combination of discretely convex sequences is discretely convex. In particular, its first differences are nondecreasing. If $r_-<r<r_+$, comparison of the averages of these differences before and after $r$ gives $$h_e(r)\le
  \frac{r_+-r}{r_+-r_-}h_e(r_-)
  +\frac{r-r_-}{r_+-r_-}h_e(r_+).$$ Hence $\{r\in\mathbb Z:h_e(r)\le D\}$ is an integer interval.

Now expand the given coboundary $g$ as in [\[eq:orbit-coefficients\]](#eq:orbit-coefficients){reference-type="eqref" reference="eq:orbit-coefficients"}. Lemma [\[lem:degree-basis\]](#lem:degree-basis){reference-type="ref" reference="lem:degree-basis"} says that every word with a nonzero coefficient has degree at most $D$. On an orbit that occurs, let $r_-$ and $r_+$ be the least and greatest indices of these coefficients. Its zero total coefficient sum implies $r_-<r_+$. The cumulative coefficients $u_{O,r}$ vanish outside $r_-\le r<r_+$. The two endpoint words have degree at most $D$, so the interval property puts every word added by the cumulative formula in $V_D$. Summing the finitely many contributions gives $f\in V_D$ with $\sigma f-f=g$. Also $\sigma f=f+g\in V_D$. If no nonconstant orbit occurs, the zero constant obstruction forces $g=0$, and $f=0$ has the required bound.

For attainment, let $k=1$ and $D\ge1$. Since $\sigma y=x$, the polynomial $f=y^D$ has difference $g=x^D-y^D$, and both have degree $D$. Every other primitive is $y^D+c$ by Theorem [\[thm:orbit-obstructions\]](#thm:orbit-obstructions){reference-type="ref" reference="thm:orbit-obstructions"}, so its degree is also $D$. This proves the uniform sharpness claim within the scalar subclass; it does not assert attainment for every fixed multiphase composition.

Before using polynomial cohomology to study rational invariants, we record the reduction from rational to polynomial primitives. It uses affine pole divisors. Poles at infinity are neither excluded nor needed for this argument.

[\[cor:rational-reduction\]]{#cor:rational-reduction label="cor:rational-reduction"} No positive iterate of $\sigma$ has a nonconstant polynomial semi-invariant, even after extending $K$. The map $F$ has no periodic affine curve over an algebraic closure of $K$. If $f\in K(x,y)$ satisfies $\sigma f-f\in A$, then $f\in A$. Consequently $$K(x,y)^F=K,
  \label{eq:rational-fixed-field}$$ and polynomial and rational solvability of $\sigma f-f=g$, for $g\in A$, are equivalent. For $D\ge0$, if $\deg g\le D$ and a rational primitive exists, every such primitive has degree at most $D$.

Let $E/K$ be a field extension and $m\ge1$. The basis theorem and its shift description hold in $E[x,y]$ with the same phase degrees. Every nonconstant basis word has an infinite orbit under $\sigma^m$, because its support is translated by the nonzero step $mk$. If a nonzero polynomial $P$ satisfied $\sigma^mP=\lambda P$ for $\lambda\in E^*$, its finite set of occurring nonconstant basis words would be invariant under this permutation. Its intersection with any infinite orbit cannot be both nonempty and finite invariant. Thus $P$ must be constant. For a nonzero constant the equation also forces $\lambda=1$.

Over an algebraic closure, an irreducible affine plane curve has principal prime ideal $(P)$ for a nonconstant irreducible polynomial. If $F^m$ preserves the curve, its pullback preserves that ideal, so $(\sigma^mP)=(P)$. The units of the polynomial ring are nonzero field constants, giving a forbidden relation $\sigma^mP=\lambda P$. A curve with finitely many irreducible components cannot be periodic either: a periodic automorphism of its set of components fixes each component after some positive power. The use of pullback is consistent with this statement, since a set fixed by the forward iterate of an automorphism is also fixed by its inverse iterate.

Suppose now that $g=\sigma f-f\in A$. For an irreducible $P\in K[x,y]$, denote by $v_P$ the order along the corresponding height-one prime. A polynomial has $v_P(g)\ge0$. If $v_P(f)<0$, the equality $\sigma f=f+g$ gives $v_P(\sigma f)=v_P(f)$: terms with different orders cannot cancel the term of smaller order. Applying the same argument to $f=\sigma f-g$ gives the converse implication when $v_P(\sigma f)<0$. Therefore the effective affine pole divisors are equal, with their multiplicities: $$\operatorname{Pole}_{\mathbb A^2}(\sigma f)
    =\operatorname{Pole}_{\mathbb A^2}(f).
  \label{eq:affine-pole-invariance}$$ The left side is the pullback by $F$ of the right side. If this finite effective divisor were nonzero, its finitely many prime components would be permuted. A positive power would fix one such prime ideal $(P)$ and hence give $\sigma^mP=\lambda P$, contradicting the first part of the proof. This reasoning works directly over $K$; it does not require a descent argument from its algebraic closure.

Thus $f$ has no affine height-one poles. Express it as a reduced fraction $a/b$ in the unique factorization domain $K[x,y]$. Any irreducible factor of a nonconstant denominator $b$ would have negative valuation, since $a$ and $b$ are relatively prime. There can be no such factor, and $b\in K^*$, proving $f\in A$. Taking $g=0$ and using $\ker(\sigma-1)=K$ yields [\[eq:rational-fixed-field\]](#eq:rational-fixed-field){reference-type="eqref" reference="eq:rational-fixed-field"}. For general $g\in V_D$, Theorem [\[thm:bounded-primitive\]](#thm:bounded-primitive){reference-type="ref" reference="thm:bounded-primitive"} supplies a primitive in $V_D$. Every other rational primitive is now polynomial and differs from it by a constant, which proves the last assertion.

# Exact dimensions of the filtered obstruction space {#sec:hilbert-series}

The obstruction quotient $$\mathcal H=A/(\sigma-1)A,\qquad
  \mathcal H_D=\mathop{\mathrm{im}}(V_D\longrightarrow\mathcal H),\qquad \mathcal H_{-1}=0$$ is a filtered vector space. We do not assert that $(\sigma-1)A$ is an ideal, and no quotient-ring structure is used below. Its associated-graded Hilbert series is $$\mathop{\mathrm{Hilb}}_{\mathop{\mathrm{gr}}\mathcal H}(t)
    =\sum_{D\ge0}\dim_K(\mathcal H_D/\mathcal H_{D-1})t^D.
  \label{eq:filtered-hilbert-definition}$$ We will count the domain on which both a polynomial and its pullback stay below the degree bound. Theorem [\[thm:bounded-primitive\]](#thm:bounded-primitive){reference-type="ref" reference="thm:bounded-primitive"} then identifies its image with all coboundaries of bounded degree.

## Strictness and the phase re-encoding

Set $$W_D=V_D\cap\sigma^{-1}V_D
     =\{f\in V_D:\sigma f\in V_D\},\qquad E_D=\dim_K W_D.$$ The degree formula and basis permutation imply $$E_D=\#\{M_e\in\mathcal B:
       \max(\mu(M_e),\mu(\sigma M_e))\le D\}.
  \label{eq:two-degree-count}$$ Indeed, neither the expansion of $f$ nor the shifted expansion of $\sigma f$ allows cancellation between distinct highest monomials. Membership in the two degree subspaces can thus be checked word by word. Moreover, $$(\sigma-1)W_D=V_D\cap(\sigma-1)A.
  \label{eq:strict-filtered-image}$$ One inclusion follows from the definition of $W_D$. For the reverse inclusion, a coboundary $g\in V_D$ has a primitive $f\in V_D$ by Theorem [\[thm:bounded-primitive\]](#thm:bounded-primitive){reference-type="ref" reference="thm:bounded-primitive"}, and $\sigma f=f+g\in V_D$, so this primitive belongs to $W_D$. The kernel on $W_D$ is $K$. Rank--nullity therefore gives the cumulative dimension identity $$\dim_K\mathcal H_D=\binom{D+2}{2}-E_D+1.
  \label{eq:filtered-dimension}$$ The final $1$ accounts for the constant kernel, including at $D=0$.

To evaluate [\[eq:two-degree-count\]](#eq:two-degree-count){reference-type="eqref" reference="eq:two-degree-count"}, write $$\alpha=A(e),\qquad B(e)=\delta Q+R,
  \qquad Q\ge0,\quad0\le R<\delta.$$ The low $k$ negative digits determine $R$. Write them as $\varepsilon_j=e_{-j}$, $1\le j\le k$, so $0\le\varepsilon_j<d_{k-j}$. Define $$R=\sum_{j=1}^k\varepsilon_j
          \prod_{h=1}^{j-1}d_{k-h},\qquad
  \rho(R)=\sum_{j=1}^k\varepsilon_j
          \prod_{h=0}^{k-j-1}d_h,
  \label{eq:rho-reencoding}$$ with each empty product equal to one. The first expression is the negative-ray mixed-radix expansion in bases $d_{k-1},\ldots,d_0$. Under shift-$k$ its digit at index $-j$ moves to index $k-j$, whose positive weight is $\prod_{h=0}^{k-j-1}d_h$. The second expression is exactly the ordinary positive-ray encoding of the shifted block.

Both encodings biject the same admissible digit set with $\{0,\ldots,\delta-1\}$, so $\rho$ is a permutation of that set. It converts the negative block to the positive block, in that direction; when the phase bases are unequal it need not be an involution. The remaining positive digits acquire a factor $\delta$ in their weights under the shift. The negative digits below this block lose a factor $\delta$ and contribute $Q$. Consequently the unique word corresponding to $(\alpha,Q,R)$ satisfies $$\mu(M_e)=\alpha+\delta Q+R,\qquad
  \mu(\sigma M_e)=\delta\alpha+Q+\rho(R).
  \label{eq:two-macro-degrees}$$ Conversely, every $\alpha,Q\ge0$ and $0\le R<\delta$ corresponds to a unique word, by Lemma [\[lem:degree-basis\]](#lem:degree-basis){reference-type="ref" reference="lem:degree-basis"} and Euclidean division of $B(e)$ by $\delta$.

## The exact series

Put $$C_\rho(t)=\sum_{R=0}^{\delta-1}t^{\max(R,\rho(R))}.
  \label{eq:phase-count-polynomial}$$ This finite polynomial contains the phase dependence in the answer.

[\[thm:hilbert\]]{#thm:hilbert label="thm:hilbert"} For the composition [\[eq:henon-composition\]](#eq:henon-composition){reference-type="eqref" reference="eq:henon-composition"} in its given coordinates, the ordinary-degree filtered obstruction space has series $$\boxed{
  \mathop{\mathrm{Hilb}}_{\mathop{\mathrm{gr}}\mathcal H}(t)
    =1+\frac{1}{(1-t)^2}
      -\frac{C_\rho(t)+2t^\delta/(1-t)}{1-t^{\delta+1}}.}
  \label{eq:general-hilbert-series}$$ It depends only on the ordered phase degrees and the specified initial coordinates, and is independent of the nonzero leading coefficients and all lower coefficients of the phase polynomials.

Define the exact-weight generating function $$E(t)=\sum_{M_e\in\mathcal B}
      t^{\max(\mu(M_e),\mu(\sigma M_e))}.$$ Each coefficient is finite, since the words counted at exponent $D$ belong to the finite basis of $V_D$. Fix $R$ in [\[eq:two-macro-degrees\]](#eq:two-macro-degrees){reference-type="eqref" reference="eq:two-macro-degrees"} and partition the pairs $(\alpha,Q)$ into three disjoint regions.

If $\alpha=Q$, the maximum of the two degrees is $$(\delta+1)Q+\max(R,\rho(R)).$$ Summing over $Q\ge0$ gives $t^{\max(R,\rho(R))}/(1-t^{\delta+1})$. If $\alpha=Q+s$ with $s\ge1$, subtraction of the two degrees gives $$\mu(\sigma M_e)-\mu(M_e)
     =(\delta-1)s+\rho(R)-R\ge0.$$ The inequality follows from $0\le R,\rho(R)\le\delta-1$; it allows equality on the boundary. The maximum is thus $(\delta+1)Q+\delta s+\rho(R)$, and the contribution from this region is $$\frac{1}{1-t^{\delta+1}}\,
  \frac{t^\delta}{1-t^\delta}\,t^{\rho(R)}.$$ In the third region $Q=\alpha+s$, $s\ge1$, the degree difference in the opposite direction is $$\mu(M_e)-\mu(\sigma M_e)
     =(\delta-1)s+R-\rho(R)\ge0.$$ The maximum is $(\delta+1)\alpha+\delta s+R$ and its summed contribution is $t^\delta t^R/((1-t^{\delta+1})(1-t^\delta))$. Even when two degrees are equal, these three regions count each pair only once, since the partition is by $\alpha$ and $Q$.

For this fixed $R$ their sum is $$\frac{1}{1-t^{\delta+1}}
  \left[
    t^{\max(R,\rho(R))}
    +\frac{t^\delta}{1-t^\delta}
         \bigl(t^R+t^{\rho(R)}\bigr)
  \right].$$ Since $\rho$ is a permutation, $\sum_Rt^{\rho(R)}=\sum_Rt^R=(1-t^\delta)/(1-t)$. Summing the last display over all $R$ yields $$E(t)=\frac{C_\rho(t)+2t^\delta/(1-t)}{1-t^{\delta+1}}.
  \label{eq:exact-two-degree-series}$$

The distinction between exact and cumulative counts now matters. Equation [\[eq:two-degree-count\]](#eq:two-degree-count){reference-type="eqref" reference="eq:two-degree-count"} implies $\sum_{D\ge0}E_Dt^D=E(t)/(1-t)$. Using [\[eq:filtered-dimension\]](#eq:filtered-dimension){reference-type="eqref" reference="eq:filtered-dimension"} and $\sum_{D\ge0}\binom{D+2}{2}t^D=(1-t)^{-3}$, we obtain $$\sum_{D\ge0}\dim_K\mathcal H_D\,t^D
    =\frac{1}{(1-t)^3}-\frac{E(t)}{1-t}+
      \frac{1}{1-t}.$$ Multiplication by $1-t$ takes the successive differences of the cumulative dimensions, with $\mathcal H_{-1}=0$. Substituting [\[eq:exact-two-degree-series\]](#eq:exact-two-degree-series){reference-type="eqref" reference="eq:exact-two-degree-series"} gives [\[eq:general-hilbert-series\]](#eq:general-hilbert-series){reference-type="eqref" reference="eq:general-hilbert-series"}. In particular its constant coefficient is $1$, as required by the nonzero class of $1$. Every quantity in this computation is determined by the phase degrees; the filtration lemma already verified that arbitrary allowed coefficients of the $p_i$ do not change those counts.

[\[cor:scalar-hilbert\]]{#cor:scalar-hilbert label="cor:scalar-hilbert"} If $k=1$ and $d=\deg p$, then $$\mathop{\mathrm{Hilb}}_{\mathop{\mathrm{gr}}\mathcal H}(t)
    =1+\frac{t-t^d}{(1-t)^2(1-t^{d+1})}
    =1+\frac{t\sum_{j=0}^{d-2}t^j}
                  {(1-t)(1-t^{d+1})},
  \label{eq:scalar-hilbert-series}$$ and the cumulative dimensions satisfy $$\dim_K\mathcal H_D=\frac{d-1}{2(d+1)}D^2+O_d(D).
  \label{eq:scalar-cumulative-growth}$$

There is only one low negative digit, so $\rho$ is the identity and $C_\rho(t)=1+t+\cdots+t^{d-1}$. Substitution into [\[eq:general-hilbert-series\]](#eq:general-hilbert-series){reference-type="eqref" reference="eq:general-hilbert-series"} and cancellation give [\[eq:scalar-hilbert-series\]](#eq:scalar-hilbert-series){reference-type="eqref" reference="eq:scalar-hilbert-series"}. Dividing that series by $1-t$ gives the cumulative generating function. At $t=1$ its leading term is $$\frac{d-1}{d+1}\,(1-t)^{-3}.$$ After subtracting this term, the pole at $1$ has order at most two. The other poles, at nontrivial $(d+1)$st roots of unity, are at most simple. A partial-fraction expansion therefore gives an $O_d(D)$ remainder in the coefficient of $t^D$: an order-two pole at $1$ has coefficients of order $D$, and a simple root-of-unity pole has bounded coefficients. The leading term contributes $\frac{d-1}{d+1}\binom{D+2}{2}$, which proves [\[eq:scalar-cumulative-growth\]](#eq:scalar-cumulative-growth){reference-type="eqref" reference="eq:scalar-cumulative-growth"}.

[\[ex:same-degree\]]{#ex:same-degree label="ex:same-degree"} For the phase word $(d_0,d_1)=(2,2)$, the degree product is $\delta=4$ and the permutation sends $0,1,2,3$ to $0,2,1,3$. Thus $C_\rho(t)=1+2t^2+t^3$. For a single degree-four phase, $\rho$ is the identity and $C_\rho(t)=1+t+t^2+t^3$. Their Hilbert series differ by $$\mathop{\mathrm{Hilb}}_{(2,2)}(t)-\mathop{\mathrm{Hilb}}_{(4)}(t)
      =\frac{t-t^2}{1-t^5}.
  \label{eq:equal-degree-comparison}$$ For instance, the degree-one associated-graded dimensions are $2$ and $1$, respectively. These maps have the same ordinary macro degree four, but their chosen-coordinate filtered obstruction spaces are distinct.

The filtration in this section is the ordinary total-degree filtration in the original pair $x,y$. An arbitrary polynomial change of coordinates need not preserve it. The formulas therefore describe coordinate-filtered vector-space information; they neither assert a general polynomial-conjugacy invariant nor claim to recover the full ordered phase word from the series.

# Detection on one complete periodic scheme {#sec:periodic-detection}

The orbit obstructions of Theorem [\[thm:orbit-obstructions\]](#thm:orbit-obstructions){reference-type="ref" reference="thm:orbit-obstructions"} are indexed by words on the integer line. The periodic algebra replaces that line by a circle. A sufficiently long circle retains both the word and its macro phase, so the finite orbit sum recovers every obstruction separately.

For a nonconstant standard word $M_e=\prod_i X_i^{e_i}$, put $$E(M_e)=\{i\in\mathbb Z:e_i>0\},\qquad
 \mathop{\mathrm{diam}}(M_e)=\max E(M_e)-\min E(M_e).$$ In particular, a word supported at one index has diameter zero, regardless of that index. For the unique standard-word expansion $g=c_0+\sum_{M_e\ne1}c_eM_e$, define $$L(g)=\max\bigl(\{\mathop{\mathrm{diam}}(M_e):c_e\ne0,\ M_e\ne1\}\cup\{0\}\bigr).$$ This is a maximum of individual word diameters, not the diameter of the union of their supports. Widely separated translates of one word therefore do not enlarge $L(g)$.

Fix a macro period $n\ge1$ and write $N=kn\ge3$. We use the algebra $A_N$, its standard basis $\mathcal B_N$, the wrapping homomorphism $W_N:A\to A_N$, and the cyclic shift $\sigma_N$ of Proposition [\[prop:periodic-algebra\]](#prop:periodic-algebra){reference-type="ref" reference="prop:periodic-algebra"}. Thus $W_N\sigma=\sigma_NW_N$ and $\sigma_N^n=1$. The relation $k\mid N$ makes the exponents allowed at an index unchanged by wrapping. It will also preserve the phase of a word when the circle is cut open.

[\[lem:no-alias\]]{#lem:no-alias label="lem:no-alias"} Let $L\ge0$ be an integer and suppose that $N=kn\ge3$ and $N>2L$. For every nonconstant standard word $M$ with $\mathop{\mathrm{diam}}(M)\le L$, $W_NM$ is a nonconstant element of $\mathcal B_N$, and its $\sigma_N$-orbit has exactly $n$ elements. If two such words $M,M'$ have wrapped images in the same $\sigma_N$-orbit, then $M$ and $M'$ belong to the same $\sigma$-orbit on the integer line.

Write the occupied indices of $M$ as $a_1<\cdots<a_s$ and set $\ell=a_s-a_1\le L$. Since $\ell<N$, these indices remain distinct modulo $N$. Wrapping therefore neither adds exponents at a common index nor requires a reduction: the resulting monomial is already in $\mathcal B_N$.

Suppose first that $s\ge2$. In their cyclic order, the distances between successive occupied indices are $$a_2-a_1,\ldots,a_s-a_{s-1},\quad N+a_1-a_s.$$ Every internal distance is at most $L$, whereas the last distance is $N-\ell>L$. Hence the wrapped word has a unique gap longer than $L$. These are distances between occupied indices, not counts of unoccupied positions. If $s=1$, there is just one cyclic gap, of length $N$, with the occupied index as both endpoints; it has the same uniqueness property.

Cut the cyclic support across its unique long gap and list the occupied indices in the complementary order, retaining their exponents. This recovers the integer word up to simultaneous translation by a multiple of $N$. In particular, if $W_NM'=\sigma_N^jW_NM$, the translated word on the right has the same distinguished gap as the word on the left. Their lifts must satisfy $$M'=\text{the translate of }M\text{ by }jk+qN
     =\sigma^{j+qn}M
 \qquad\text{for some }q\in\mathbb Z.$$ The second equality uses $N=kn$; without it, recovery of an integer word would not by itself recover its macro phase.

Finally, suppose $\sigma_N^jW_NM=W_NM$ for $0<j<n$. The cyclic translation by $jk$ must preserve the unique long gap and, in particular, its endpoint immediately before the occupied arc. Thus $jk\equiv0\pmod N$. As $N=kn$, this implies $n\mid j$, a contradiction. The stabilizer is trivial, so the orbit has length $n$.

The sum to be tested is $$S_ng=\sum_{j=0}^{n-1}\sigma^jg.$$ Its image under $W_N$ is an element of the complete fixed-point scheme ring. We do not take a scalar trace of multiplication by this element.

[\[thm:periodic-test\]]{#thm:periodic-test label="thm:periodic-test"} Let $g\in A=K[x,y]$, and suppose that $N=kn\ge3$ and $N>2L(g)$. Then the following conditions are equivalent:

1.  The normal-form constant coefficient of $g$ is zero, and the sum of its coefficients on each nonconstant $\sigma$-orbit of standard words is zero.

2.  There is an $f\in K[x,y]$ such that $g=\sigma f-f$.

3.  There is an $f\in K(x,y)$ such that $g=\sigma f-f$.

4.  $W_N(S_ng)=0$ in $A_N=K[\mathop{\mathrm{Fix}}(F^n)]$.

If $\deg g\le D$ and these conditions hold, the polynomial primitive can be chosen with $\deg f\le D$ and is unique modulo $K$.

The first two conditions are equivalent by Theorem [\[thm:orbit-obstructions\]](#thm:orbit-obstructions){reference-type="ref" reference="thm:orbit-obstructions"}; Corollary [\[cor:rational-reduction\]](#cor:rational-reduction){reference-type="ref" reference="cor:rational-reduction"} gives the equivalence with the third. The degree bound and uniqueness are Theorem [\[thm:bounded-primitive\]](#thm:bounded-primitive){reference-type="ref" reference="thm:bounded-primitive"}. It remains to compare the orbit coefficients with the periodic sum.

Let $O$ range over the finitely many nonconstant $\sigma$-orbits that occur in $g$. Choose a representative $M_O$ that occurs in $g$, and write $$g=c_0+\sum_O\sum_{r\in\mathbb Z}c_{O,r}\sigma^rM_O,
 \qquad c_O=\sum_{r\in\mathbb Z}c_{O,r},$$ where all sums of coefficients are finite. Each $M_O$ has diameter at most $L(g)$. On the finite algebra, a full cyclic sum is unchanged if its starting point is shifted. Consequently $$W_N(S_ng)
 =nc_0+\sum_Oc_O\mathcal N_O,
 \qquad
 \mathcal N_O=\sum_{j=0}^{n-1}\sigma_N^jW_NM_O.$$ Lemma [\[lem:no-alias\]](#lem:no-alias){reference-type="ref" reference="lem:no-alias"} shows that each $\mathcal N_O$ is a sum of $n$ distinct nonconstant elements of $\mathcal B_N$. For distinct infinite orbits $O$, these finite supports are disjoint. They are also disjoint from the constant basis word. Linear independence of $\mathcal B_N$ now implies that $W_N(S_ng)=0$ if and only if every $c_O$ vanishes and $nc_0=0$. Since $K$ has characteristic zero, the last equality is equivalent to $c_0=0$. This proves that the fourth condition implies the first.

For the converse, a polynomial coboundary telescopes: $$S_n(\sigma f-f)=\sigma^nf-f.$$ Its wrapped image is zero because $\sigma_N^n=1$. This implication does not require the diameter bound.

[\[rem:scheme-values\]]{#rem:scheme-values label="rem:scheme-values"} The fourth condition in Theorem [\[thm:periodic-test\]](#thm:periodic-test){reference-type="ref" reference="thm:periodic-test"} is exactly the ideal membership $$S_ng\in J_N=(X_N-X_0,\ X_{N-1}-X_{-1})\subset K[x,y].$$ Vanishing at all geometric points of $\mathop{\mathrm{Fix}}(F^n)$, understood over an algebraic closure of $K$, only gives membership in $\sqrt{J_N}$. If $A_N$ is reduced, these conditions agree: in characteristic zero a finite reduced $K$-algebra remains reduced after extension to an algebraic closure, where it is a product of fields. No reducedness hypothesis was used above, so the scheme condition cannot be replaced without qualification by geometric values, still less by values at $K$-rational points alone.

For a small example of the distinction, take $H_p(x,y)=(p(x)-y,x)$ with $p(x)=x^2+2x$. Its fixed-point ideal is $$(p(x)-y-x,\ x-y)=(x^2,\ x-y),$$ and its coordinate ring is $K[x]/(x^2)$. The class of $x$ vanishes at the only geometric point but is not zero in this ring. This is a period-one example explaining the role of nilpotents; it is not a counterexample at any of the sufficiently long periods in the theorem.

# Effective periods and sharp boundary phenomena {#sec:effective-periods}

The support condition in Theorem [\[thm:periodic-test\]](#thm:periodic-test){reference-type="ref" reference="thm:periodic-test"} depends on the normal form of the input. The ordinary-degree filtration gives an exact worst-case support bound before that normal form is computed. The bound depends only on the phase degrees and the chosen initial coordinates, not on the coefficients of the polynomials $p_i$.

## The exact endpoint cost

Use the weights $w_i$ of [\[eq:phase-weights\]](#eq:phase-weights){reference-type="eqref" reference="eq:phase-weights"}. For an integer $D\ge0$, define $$L_{\mathrm{ph}}(D)
 =\max\bigl(\{b-a:a,b\in\mathbb Z,\ a<b,\ w_a+w_b\le D\}\cup\{0\}\bigr).$$ Both tails of the weight sequence grow at least geometrically, so only finitely many endpoint pairs can satisfy the displayed cost constraint. In particular, $L_{\mathrm{ph}}(D)$ is finite and is computable from the phase degrees.

[\[prop:exact-span\]]{#prop:exact-span label="prop:exact-span"} For every $D\ge0$, $$\max_{g\in V_D}L(g)=L_{\mathrm{ph}}(D).$$ For $D\ge2$, an endpoint word $X_aX_b$ attains the maximum. For $D=0,1$, the maximum is zero.

By Lemma [\[lem:degree-basis\]](#lem:degree-basis){reference-type="ref" reference="lem:degree-basis"}, every standard word $M_e$ occurring in an element of $V_D$ satisfies $\sum_i e_iw_i\le D$. If its support has at least two points, let $a<b$ be its endpoints. Since $e_a,e_b\ge1$, $$w_a+w_b\le\sum_i e_iw_i\le D.$$ Its diameter is therefore at most $L_{\mathrm{ph}}(D)$. Words with one support point have diameter zero, so the same bound holds for every $g\in V_D$.

For $D\ge2$, the pair $(-1,0)$ is admissible because $w_{-1}=w_0=1$; hence the maximum is attained by an admissible pair $a<b$. Since $d_a,d_b\ge2$, the word $X_aX_b$ is standard and has diameter $b-a$. Lemma [\[lem:degree-basis\]](#lem:degree-basis){reference-type="ref" reference="lem:degree-basis"} gives its exact ordinary degree as $w_a+w_b$, so it belongs to $V_D$ and attains the claimed bound. For $D=0,1$, two occupied indices would already cost at least two. Thus all possible word diameters are zero; the constant word suffices to attain that value.

The endpoint optimization has a closed form when all phase degrees are equal. The same expression is an upper bound for unequal phase degrees after replacing them by their minimum.

[\[prop:scalar-span\]]{#prop:scalar-span label="prop:scalar-span"} Let $d=\min_{0\le i<k}d_i$. For $D\ge2$, put $$h=\left\lfloor\log_d(D/2)\right\rfloor,
 \qquad
 L_d(D)=1+2h+\mathbf 1_{\{D\ge(d+1)d^h\}},$$ and set $L_d(0)=L_d(1)=0$. Then $$L_{\mathrm{ph}}(D)\le L_d(D)
 \le1+2\lfloor\log_dD\rfloor\qquad(D\ge2).$$ If every $d_i$ equals $d$, then $L_{\mathrm{ph}}(D)=L_d(D)$. In particular, this equality holds for a single Hénon map of degree $d$.

The weight of index $i$ is at least $d^{\mathop{\mathrm{dist}}(i,\{-1,0\})}$. Given an admissible pair $a<b$, set $$r=\mathop{\mathrm{dist}}(a,\{-1,0\}),\qquad
 s=\mathop{\mathrm{dist}}(b,\{-1,0\}).$$ Then $b-a\le1+r+s$ and $d^r+d^s\le D$. For fixed $r+s$, the least value of $d^r+d^s$ occurs when the two exponents differ by at most one. Indeed, if $r\ge s+2$, replacing $(r,s)$ by $(r-1,s+1)$ reduces the sum by $$(d-1)(d^{r-1}-d^s)>0.$$ Iteration reaches the balanced pair.

The least costs for distance sums $2h$, $2h+1$, and $2h+2$ are, respectively, $$2d^h,\qquad(d+1)d^h,\qquad2d^{h+1}.$$ The definition of $h$ says that the first cost is at most $D$ and the third is greater than $D$. Thus the largest affordable distance sum is $2h$, or $2h+1$ precisely when $D\ge(d+1)d^h$. This gives $L_{\mathrm{ph}}(D)\le L_d(D)$. Each affordable exponent is at most $\lfloor\log_dD\rfloor$, which also gives the stated simpler upper bound.

If all phase degrees are $d$, the weights are exactly $d^{\mathop{\mathrm{dist}}(i,\{-1,0\})}$. Take the balanced distances on opposite sides of the initial interval, with endpoints $a=-1-r$ and $b=s$. Their diameter is $1+r+s$, and their cost is $d^r+d^s$. The maximizing distances above therefore give equality. The convention for $D=0,1$ agrees with Proposition [\[prop:exact-span\]](#prop:exact-span){reference-type="ref" reference="prop:exact-span"}.

## A degree-uniform periodic test

[\[thm:effective-period\]]{#thm:effective-period label="thm:effective-period"} For $D\ge0$, let $$n_{\mathrm{eff}}(D)
 =\left\lceil\frac{\max\{3,\,2L_{\mathrm{ph}}(D)+1\}}{k}\right\rceil.$$ For every $n\ge n_{\mathrm{eff}}(D)$ and every $g\in V_D$, the four conditions of Theorem [\[thm:periodic-test\]](#thm:periodic-test){reference-type="ref" reference="thm:periodic-test"} are equivalent with $N=kn$. In particular, one test in $A_{kn_{\mathrm{eff}}(D)}$ decides whether $g$ has a polynomial, or equivalently rational, primitive. For $D\ge1$ this algebra has length $$\dim_K A_{kn_{\mathrm{eff}}(D)}
 =\delta^{n_{\mathrm{eff}}(D)}\le\delta^4D^4.$$

The chosen period satisfies $kn\ge3$ and $kn\ge2L_{\mathrm{ph}}(D)+1>2L(g)$ by Proposition [\[prop:exact-span\]](#prop:exact-span){reference-type="ref" reference="prop:exact-span"}. Theorem [\[thm:periodic-test\]](#thm:periodic-test){reference-type="ref" reference="thm:periodic-test"} therefore applies to every $g\in V_D$.

For the length bound, assume $D\ge1$ and set $t=\lfloor\log_\delta D\rfloor$. Write an outward distance from $\{-1,0\}$ as $qk+r$, where $q\ge0$ and $0\le r<k$. The corresponding weight contains $q$ complete phase blocks and is at least $\delta^q$. Any index with weight at most $D$ thus has $q\le t$. All such indices lie in $$[-kt-k,\ kt+k-1].$$ It follows that $$L_{\mathrm{ph}}(D)\le2kt+2k-1,
 \qquad
 2L_{\mathrm{ph}}(D)+1\le4kt+4k-1.$$ Since $\lceil3/k\rceil\le3\le4t+4$, the definition of $n_{\mathrm{eff}}$ gives $n_{\mathrm{eff}}(D)\le4t+4$. Finally, Proposition [\[prop:periodic-algebra\]](#prop:periodic-algebra){reference-type="ref" reference="prop:periodic-algebra"} identifies the length with $\delta^{n_{\mathrm{eff}}(D)}$, whence $$\delta^{n_{\mathrm{eff}}(D)}
 \le\delta^{4t+4}
 =\delta^4(\delta^t)^4\le\delta^4D^4.$$ The effective period itself is also defined for $D=0$; only the quartic estimate excludes that value.

The logarithmic period and the quartic algebra length measure different objects. The former counts iterates of the macro map, whereas the latter counts the dimension of the entire fixed-point algebra, including multiplicities. Neither bound is a statement about coefficient bit complexity or the cost of constructing a normal form.

## Sharpness of the eventual-uniform threshold

A failure at one period gives a lower bound for a threshold beyond which every period works. It need not rule out a specially chosen shorter period. To keep these quantifiers explicit, fix a scalar map $H_p$ with $\deg p=d\ge3$ and define $T_p(D)$ to be the least integer $T\ge3$ such that, for every integer $n\ge T$ and every $g\in V_D$, $$W_n(S_ng)=0\quad\Longleftrightarrow\quad g\in(\sigma-1)A.$$ Theorem [\[thm:effective-period\]](#thm:effective-period){reference-type="ref" reference="thm:effective-period"} shows that this threshold exists. Here $k=1$, so the cycle length and the macro period are both $n$.

[\[thm:sharp-threshold\]]{#thm:sharp-threshold label="thm:sharp-threshold"} For every scalar map of degree $d\ge3$ and every integer $r\ge1$, set $$g_r=X_{-r-1}X_r^2-X_{-r-1}^2X_r,
 \qquad D_r=3d^r.$$ Then $\deg g_r=D_r$ and $g_r\notin(\sigma-1)A$, but $$W_{4r+2}(S_{4r+2}g_r)=0.$$ Moreover, $$L(g_r)=L_d(D_r)=2r+1,
 \qquad T_p(D_r)=4r+3.$$ Consequently the leading constant $4$ in an eventual-uniform bound $4\log_dD+O(1)$ cannot be replaced by a smaller constant, even for one fixed scalar map of degree $d\ge3$.

Put $a=-r-1$, $b=r$, $L=b-a=2r+1$, and $m=d^r$. Lemma [\[lem:degree-basis\]](#lem:degree-basis){reference-type="ref" reference="lem:degree-basis"} gives nonzero constants $\alpha_r,\beta_r\in K$ such that the highest homogeneous terms of $X_b$ and $X_a$ are $\alpha_rx^m$ and $\beta_ry^m$, respectively. Hence the homogeneous part of degree $3m$ in $g_r$ is $$\alpha_r^2\beta_r x^{2m}y^m
 -\alpha_r\beta_r^2 x^my^{2m}.$$ The two monomials are distinct and their coefficients are nonzero. Thus $\deg g_r=3m=D_r$.

Both terms defining $g_r$ are standard, since $1,2<d$. Their exponent lists, read from the smaller occupied index to the larger one, are $(1,2)$ and $(2,1)$. An integer translation preserves that order and those exponents, so the terms lie in different infinite word orbits. Their orbit obstructions are $1$ and $-1$; Theorem [\[thm:orbit-obstructions\]](#thm:orbit-obstructions){reference-type="ref" reference="thm:orbit-obstructions"} proves that $g_r$ is not a coboundary. Each term has diameter $L$, giving $L(g_r)=L$.

On the circle of length $n=2L=4r+2$, translation by $L$ exchanges the two occupied positions. It therefore takes the wrapped first term of $g_r$ to the wrapped second term. Their full cyclic sums are equal, which proves $W_n(S_ng_r)=0$.

At $D=D_r$, we have $$\left\lfloor\log_d(D_r/2)\right\rfloor=r,
 \qquad D_r<(d+1)d^r,$$ because $1<3/2<d$ and $3<d+1$. These inequalities include $d=3$. Proposition [\[prop:scalar-span\]](#prop:scalar-span){reference-type="ref" reference="prop:scalar-span"} yields $L_d(D_r)=2r+1$. Theorem [\[thm:effective-period\]](#thm:effective-period){reference-type="ref" reference="thm:effective-period"} then gives $T_p(D_r)\le4r+3$. The failed test at $n=4r+2$ forces the reverse inequality: any smaller eventual threshold would include that period and the input $g_r$. Thus $T_p(D_r)=4r+3$.

Finally, $\log_dD_r=r+\log_d3$. If an eventual-uniform bound had the form $T_p(D)\le c\log_dD+C$ with $c<4$ and a constant $C$ independent of $D$, evaluation at $D_r$ would give $$4r+3\le cr+c\log_d3+C$$ for every $r$, which is impossible as $r$ tends to infinity.

The same examples show why the general diameter hypothesis must be strict: at $n=2L(g_r)$ the scheme sum loses a nonzero obstruction. The sharpness statement does not exclude an isolated valid period below $T_p(D)$, several shorter periods used jointly, or a method that uses no periodic algebra.

## Binary words and the macro-phase boundary

When $d=2$, the exponent $2$ is not an allowed standard digit, so the preceding two-word construction does not apply. At equality $n=2L$, the only ambiguous cut for a binary word is an antipodal pair, and that pair has identical endpoint digits.

[\[prop:binary-boundary\]]{#prop:binary-boundary label="prop:binary-boundary"} Let $k=1$ and $d=2$. The equivalences in Theorem [\[thm:periodic-test\]](#thm:periodic-test){reference-type="ref" reference="thm:periodic-test"} remain valid whenever $n\ge3$ and $n\ge2L(g)$. At the boundary $n=2L$, the cyclic sum of an antipodal two-point word is twice the sum over its distinct cyclic translates; this nonzero multiplicity does not affect detection. On the other hand, for every integer $L\ge2$ the polynomial $$g_L=X_0X_L-X_0X_{L-1}$$ is not a coboundary and satisfies $W_n(S_ng_L)=0$ at $n=2L-1\ge3$.

Only the equality case needs an argument beyond Theorem [\[thm:periodic-test\]](#thm:periodic-test){reference-type="ref" reference="thm:periodic-test"}. Write $n=2L\ge3$ and consider a nonconstant standard word of diameter $\ell\le L$. If $\ell<L$, its external gap is greater than $L$ and is unique. If $\ell=L$ and at least three indices are occupied, every internal gap is strictly less than $L$, whereas the external gap equals $L$. There is again a unique largest gap, which recovers the word on the line and gives a cyclic orbit of length $n$ by the proof of Lemma [\[lem:no-alias\]](#lem:no-alias){reference-type="ref" reference="lem:no-alias"}.

The remaining case is exactly the word $X_aX_{a+L}$: all nonzero binary digits are $1$. Its two gaps both have length $L$. Cutting across either gap yields two lifts related by translation by $L$, so they already lie in the same infinite scalar orbit. Thus different infinite word orbits still have disjoint finite orbit supports. The only cyclic translations preserving this pair are $0$ and $L$ modulo $n$. Its orbit has $n/2$ distinct words, each of which occurs twice in the full $n$-term sum. All other words under consideration have trivial stabilizer.

In the norm decomposition from the proof of Theorem [\[thm:periodic-test\]](#thm:periodic-test){reference-type="ref" reference="thm:periodic-test"}, each nonconstant orbit coefficient is therefore multiplied either by $1$ or by $2$, on its own disjoint finite basis support. The constant coefficient remains $nc_0$. Characteristic zero makes all these factors nonzero, so the scheme sum still detects exactly the orbit obstructions. The other equivalent conditions and the primitive statement follow from the same global results as before.

For the failure at $n=2L-1$, the two terms of $g_L$ have distinct diameters $L$ and $L-1$, and hence lie in different infinite translation orbits. The orbit obstruction criterion proves that $g_L$ is not a coboundary. Modulo $n$, translation by $L-1$ takes the support $\{0,L\}$ to $$\{L-1,2L-1\}=\{L-1,0\}\pmod n,$$ which is the support of the second term. Their cyclic sums are equal and cancel. The assumptions $L\ge2$ and $n=2L-1\ge3$ keep this example within the finite-cycle model used here.

[\[ex:phase-alias\]]{#ex:phase-alias label="ex:phase-alias"} Take $k=2$ with $d_0=d_1=2$, and set $N=6$, $n=3$. The polynomial $$g=X_0X_3-X_3X_6$$ has $L(g)=3$. Its two standard words differ by translation by $3$. They cannot differ by a multiple of $2$: comparing their smallest occupied indices would require $2j=3$. They therefore lie in different $\sigma$-orbits, and $g$ is not a coboundary for the macro map $F=H_1\circ H_0$. Nevertheless, $$W_6g=Z_0Z_3-Z_3Z_0=0,$$ so $W_6(S_3g)=0$ as well. The two equal gaps permit a shift by $3$, which preserves a scalar orbit but changes the macro phase. This example also works if $p_0=p_1$, because then the map under study is $H_p^2$, not $H_p$. Thus $k\mid N$ alone does not justify the scalar binary improvement; the general multiphase test retains $N>2L(g)$.

There is also a direct finite linear method that does not pass through a periodic scheme. By Theorem [\[thm:bounded-primitive\]](#thm:bounded-primitive){reference-type="ref" reference="thm:bounded-primitive"}, for $g\in V_D$ it is enough to insert $$f=\sum_{a+b\le D}u_{a,b}x^ay^b$$ into $\sigma f-f=g$ and compare polynomial coefficients. This gives an exact linear system with $\binom{D+2}{2}=O(D^2)$ unknowns; the constant coefficient accounts for the freedom in the primitive. The periodic test supplies an alternative exact certificate on one complete scheme. The number of unknowns in the direct method and the length of that scheme do not, by themselves, compare their running times or establish an optimal algorithm.

# Rigidity for a univariate right-hand side {#sec:univariate-rigidity}

For a single Hénon map, the restriction that the right-hand side depend only on the first coordinate gives a stronger conclusion than the general degree bound. Throughout this section, let $K$ have characteristic zero and let $$H_p(x,y)=(p(x)-y,x),\qquad
 p(x)=a_dx^d+\cdots+a_0,\qquad a_d\ne0,\qquad d\ge2.$$ Thus this is the case $k=1$, with $\sigma=H_p^*$. The classification below concerns this particular single-step map, not an arbitrary composition of the maps considered in the preceding sections.

The useful factorization of $H_p$ is into the two involutions $$\iota(x,y)=(y,x),\qquad
 r(x,y)=(x,p(x)-y),\qquad H_p=\iota\circ r.$$ The exchange involution $\iota$ also satisfies $\iota\circ H_p\circ\iota=H_p^{-1}$. To describe the polynomials fixed by $r$, set $$Q=y^2-p(x)y.$$ The change of coordinate $z=y-p(x)/2$ identifies $K[x,y]$ with $K[x,z]$, and $r$ acts by $z\mapsto-z$. A polynomial in $z$ is fixed by this action exactly when only even powers occur. Since $z^2=Q+p(x)^2/4$, it follows that $$K[x,y]^r=K[x,Q].
 \label{eq:reflection-invariant-ring}$$

We will use one consequence of this description for ordinary total degree. The highest homogeneous term of $Q$ is $-a_dx^dy$. If a nonzero polynomial $C\in K[x,Q]$ is written as $$C=\sum_{j\ge0}b_j(x)Q^j,$$ with finitely many nonzero $b_j$, the unique highest monomial of each nonzero summand is a nonzero multiple of $x^{\deg b_j+dj}y^j$. These monomials cannot cancel between different $j$, because their $y$ exponents differ. Consequently every monomial $x^iy^j$ in the highest homogeneous part of $C$ satisfies $$i\ge dj.
 \label{eq:invariant-highest-cone}$$ No description of the anti-invariant polynomials is needed.

[\[thm:univariate\]]{#thm:univariate label="thm:univariate"} Let $f\in K(x,y)$ and $R\in K[x]$. Then $$f\circ H_p-f=R(x)$$ if and only if there are $c,c_0\in K$ such that $$f=c(x-y)+c_0,\qquad R=c\bigl(p(x)-2x\bigr).
 \label{eq:univariate-classification}$$

By Corollary [\[cor:rational-reduction\]](#cor:rational-reduction){reference-type="ref" reference="cor:rational-reduction"}, a rational function with polynomial difference is polynomial, so $f\in K[x,y]$. The same corollary gives $K(x,y)^{\sigma}=K$.

Evaluate the given equation at $r(x,y)$. Since $H_p\circ r=\iota$ and $r$ preserves $x$, this gives $$f\circ\iota-f\circ r=R(x).$$ Together with $f\circ H_p=f+R(x)$ and $\iota\circ H_p=r$, it follows that $$(f+f\circ\iota)\circ H_p
 =f\circ H_p+f\circ r
 =f+f\circ\iota.$$ Thus $f+f\circ\iota$ is a constant. Subtracting half that constant from $f$ does not change its difference. We may therefore impose $$f\circ\iota=-f.
 \label{eq:exchange-antisymmetry}$$ The equation evaluated at $r$ now reads $$f(x,y)+f(x,p(x)-y)=-R(x).
 \label{eq:univariate-reflection-equation}$$

Put $C=f_y$. Differentiation of [\[eq:univariate-reflection-equation\]](#eq:univariate-reflection-equation){reference-type="eqref" reference="eq:univariate-reflection-equation"} with respect to $y$ yields $$C(x,y)-C(x,p(x)-y)=0.$$ Hence $C\in K[x,Q]$ by [\[eq:reflection-invariant-ring\]](#eq:reflection-invariant-ring){reference-type="eqref" reference="eq:reflection-invariant-ring"}. On the other hand, differentiating [\[eq:exchange-antisymmetry\]](#eq:exchange-antisymmetry){reference-type="eqref" reference="eq:exchange-antisymmetry"} once in each variable gives $$C_x(x,y)=f_{xy}(x,y)=-f_{xy}(y,x)=-C_x(y,x).
 \label{eq:mixed-derivative-antisymmetry}$$

Suppose $C$ is nonconstant, and let $C_D$ denote its highest homogeneous part, where $D>0$. Every monomial $x^iy^j$ in $C_D$ satisfies $i\ge dj$ by [\[eq:invariant-highest-cone\]](#eq:invariant-highest-cone){reference-type="eqref" reference="eq:invariant-highest-cone"}. In particular $i>0$: the possibility $i=0$ would imply $j=0$, contrary to $D>0$. Characteristic zero then ensures that $(C_D)_x\ne0$, and this derivative is the highest homogeneous part of $C_x$. For each monomial $x^ay^b$ in it, we have $$a+1\ge db.
 \label{eq:derivative-cone}$$ By [\[eq:mixed-derivative-antisymmetry\]](#eq:mixed-derivative-antisymmetry){reference-type="eqref" reference="eq:mixed-derivative-antisymmetry"}, the exchanged monomial $x^by^a$ also occurs with the negative coefficient. Applying [\[eq:derivative-cone\]](#eq:derivative-cone){reference-type="eqref" reference="eq:derivative-cone"} to that monomial gives $b+1\ge da$. If $a>b$, then $a\ge b+1$, and the latter inequality would give $$b+1\ge da\ge2a\ge2b+2,$$ which is impossible. Interchanging $a$ and $b$ excludes $b>a$. The only remaining possibility is $a=b$, but an exchange-anti-invariant polynomial has zero coefficient on each such diagonal monomial, since $2\ne0$ in $K$. This contradicts $(C_D)_x\ne0$.

It follows that $C$ is constant. Write $f=Cy+B(x)$, which is possible because $f_y=C$ in characteristic zero. Equation [\[eq:exchange-antisymmetry\]](#eq:exchange-antisymmetry){reference-type="eqref" reference="eq:exchange-antisymmetry"} becomes $$C(x+y)+B(x)+B(y)=0.$$ Taking $x=y=0$ gives $B(0)=0$, and then taking $y=0$ gives $B(x)=-Cx$. Restoring the constant subtracted earlier and putting $c=-C$, we obtain $f=c(x-y)+c_0$. Finally, $$(x-y)\circ H_p-(x-y)
 =(p(x)-y-x)-(x-y)=p(x)-2x,$$ which proves both the formula for $R$ and its converse.

The theorem covers every rational primitive, with no degree truncation or genericity condition on the coefficients of $p$. In particular a constant right-hand side is solvable only when it is zero, since $\deg(p-2x)=d\ge2$; in that case the primitive is constant.

The assumptions also delimit the statement. For the degree-one map with $p(x)=2x$, the function $x-y$ is invariant, so every polynomial in $x-y$ has zero difference. In characteristic $\ell>0$, the identity $$\sigma\bigl((x-y)^\ell\bigr)-(x-y)^\ell
 =\bigl(p(x)-2x\bigr)^\ell$$ gives primitives outside the linear form [\[eq:univariate-classification\]](#eq:univariate-classification){reference-type="eqref" reference="eq:univariate-classification"}. Finally, the reflection factorization used here is for the coefficient $-1$ of $y$, equivalently the displayed Jacobian-one Hénon map. The theorem makes no corresponding classification claim for a general dissipative coefficient or for a multiphase composition.

# Rational invariants of a parameter-preserving symplectic lift {#sec:symplectic-lift}

Let $V\in\mathbb C[t,a]$ have $\deg_tV=m\ge3$. On affine four-space with coordinates $(t,s,a,r)$, consider the map $\widehat F$ defined by $$a'=a,\qquad s'=s+V_t(t,a),\qquad
 t'=t+s',\qquad r'=r+V_a(t,a).
 \label{eq:symplectic-lift}$$ Here $r$ is the fourth coordinate, not the reflection from Section [7](#sec:univariate-rigidity){reference-type="ref" reference="sec:univariate-rigidity"}. The preserved parameter $a$ is already a rational first integral. Our question is whether there are any others, in the full field $\mathbb C(t,s,a,r)$.

The map is a polynomial symplectic automorphism for $$\omega=\mathrm dt\wedge\mathrm ds+\mathrm da\wedge\mathrm dr.$$ Indeed, first apply the kick $$(t,s,a,r)\longmapsto
 \bigl(t,s+V_t(t,a),a,r+V_a(t,a)\bigr).$$ Its pullback changes $\omega$ by $$V_{ta}\,\mathrm dt\wedge\mathrm da+
 V_{at}\,\mathrm da\wedge\mathrm dt=0.$$ The following drift $(t,s,a,r)\mapsto(t+s,s,a,r)$ also preserves $\omega$, because $\mathrm d(t+s)\wedge\mathrm ds=\mathrm dt\wedge\mathrm ds$. Both steps have polynomial inverses: subtract the same gradient in the kick, and subtract $s$ from $t$ in the drift. Their composition is [\[eq:symplectic-lift\]](#eq:symplectic-lift){reference-type="eqref" reference="eq:symplectic-lift"}.

Regard $a$ as a member of the constant field and put $$K=\mathbb C(a),\qquad x=t,\qquad y=t-s,\qquad
 p(x)=2x+V_t(x,a).
 \label{eq:lift-henon-coordinates}$$ Then $s=x-y$, and the induced map on $(x,y)$ is $$x'=p(x)-y,\qquad y'=x.$$ It is a single Hénon map $H_p$ over $K$, with $\deg_xp=m-1\ge2$. Write $L=K(x,y)$ and $\sigma=H_p^*$ for its pullback. Corollary [\[cor:rational-reduction\]](#cor:rational-reduction){reference-type="ref" reference="cor:rational-reduction"} gives $L^\sigma=K$. On the remaining transcendental coordinate, the pullback $\widehat\sigma=\widehat F^*$ acts by $$\widehat\sigma r=r+b,\qquad b=V_a(x,a)\in L,
 \qquad \widehat\sigma|_L=\sigma.$$

The reduction from an extra invariant to an additive coboundary is the classical additive-extension criterion of Karr, as recalled by Schneider [@Schneider2016DifferenceRings]. We give the coefficient argument, including the full constant field in the solvable case.

[\[lem:additive-extension\]]{#lem:additive-extension label="lem:additive-extension"} Let $L$ be a field of characteristic zero with automorphism $\sigma$, and let $K=L^\sigma$. For $b\in L$, extend $\sigma$ to an automorphism $\widehat\sigma$ of $L(r)$, where $r$ is transcendental over $L$, by $\widehat\sigma r=r+b$. If there is no $h\in L$ with $\sigma h-h=b$, then $$L(r)^{\widehat\sigma}=K.$$ If such an $h$ exists, then $$L(r)^{\widehat\sigma}=K(r-h).
 \label{eq:additive-fixed-field}$$

Let $I=P/Q$ be a nonzero invariant, where $P,Q\in L[r]$ are nonzero and coprime. Its invariance says $$(\widehat\sigma P)Q=P(\widehat\sigma Q).$$ Since $P$ and $Q$ are coprime, $P$ divides $\widehat\sigma P$ and $Q$ divides $\widehat\sigma Q$. The substitution $r\mapsto r+b$ preserves $r$-degree, so the quotients are nonzero members of $L$. The displayed identity makes them equal: for some $\lambda\in L^*$, $$\widehat\sigma P=\lambda P,\qquad
 \widehat\sigma Q=\lambda Q.
 \label{eq:additive-semiinvariants}$$ Let $p_j$ and $q_\ell$ be the leading coefficients of $P$ and $Q$, respectively. Comparing leading coefficients in [\[eq:additive-semiinvariants\]](#eq:additive-semiinvariants){reference-type="eqref" reference="eq:additive-semiinvariants"} gives $$\sigma p_j=\lambda p_j,\qquad
 \sigma q_\ell=\lambda q_\ell.$$ Thus the monic polynomials $P/p_j$ and $Q/q_\ell$ are individually fixed by $\widehat\sigma$. Moreover, the leading-coefficient ratio is fixed in the base field: $$\sigma(p_j/q_\ell)=p_j/q_\ell,
 \qquad p_j/q_\ell\in K.
 \label{eq:leading-coefficient-ratio}$$

If $I$ depends on $r$, at least one of the two monic polynomials has positive degree. Denote it by $$T=r^q+u_{q-1}r^{q-1}+\cdots+u_0,\qquad q\ge1.$$ The coefficient of $r^{q-1}$ in $\widehat\sigma T=T$ is $$qb+\sigma u_{q-1}=u_{q-1}.$$ Division by the nonzero integer $q$ yields $b=\sigma h-h$ with $h=-u_{q-1}/q$. Hence, when no such $h$ exists, every invariant lies in $L$ and therefore in $L^\sigma=K$.

Conversely, suppose $b=\sigma h-h$ and put $z=r-h$. Then $$\widehat\sigma z=r+b-\sigma h=r-h=z.$$ The element $z$ is transcendental over $L$, so $L(r)=L(z)$, and $K(z)$ is contained in the fixed field. To prove the reverse inclusion, write an arbitrary nonzero invariant as a coprime quotient in $L[z]$. The preceding divisibility and leading-coefficient argument applies with $z$ in place of $r$. It gives invariant monic numerator and denominator, and their leading-coefficient ratio belongs to $K$ by [\[eq:leading-coefficient-ratio\]](#eq:leading-coefficient-ratio){reference-type="eqref" reference="eq:leading-coefficient-ratio"}. Because $z$ is fixed, equality of each monic polynomial with its transform means that every coefficient is fixed by $\sigma$, hence belongs to $K$. The quotient, including its leading-coefficient ratio, is therefore in $K(z)$. This proves [\[eq:additive-fixed-field\]](#eq:additive-fixed-field){reference-type="eqref" reference="eq:additive-fixed-field"}.

The next-to-leading-coefficient reduction also occurs in the contact lifts studied by Cerveau and Déserti [@CerveauDeserti2018Contact]. Their contact setting is distinct from the four-dimensional symplectic map [\[eq:symplectic-lift\]](#eq:symplectic-lift){reference-type="eqref" reference="eq:symplectic-lift"}; here the specific remaining equation is the univariate Hénon coboundary equation classified in Theorem [\[thm:univariate\]](#thm:univariate){reference-type="ref" reference="thm:univariate"}.

[\[thm:lift-field\]]{#thm:lift-field label="thm:lift-field"} For the potential and map in [\[eq:symplectic-lift\]](#eq:symplectic-lift){reference-type="eqref" reference="eq:symplectic-lift"}, the field of all rational first integrals is $$\mathbb C(t,s,a,r)^{\widehat F}=
 \begin{cases}
  \mathbb C\bigl(a,r-c(a)s\bigr),
    &\text{if }V_a=c(a)V_t\text{ for some }c\in\mathbb C(a),\\
  \mathbb C(a),&\text{if no such }c\text{ exists}.
 \end{cases}
 \label{eq:lift-fixed-field}$$

The change [\[eq:lift-henon-coordinates\]](#eq:lift-henon-coordinates){reference-type="eqref" reference="eq:lift-henon-coordinates"} identifies $\mathbb C(t,s,a,r)$ with $L(r)$, and the pullback is the additive extension described above. Lemma [\[lem:additive-extension\]](#lem:additive-extension){reference-type="ref" reference="lem:additive-extension"} reduces the question to the existence of $h\in K(x,y)$ such that $$\sigma h-h=V_a(x,a).$$ Theorem [\[thm:univariate\]](#thm:univariate){reference-type="ref" reference="thm:univariate"}, applied over $K=\mathbb C(a)$, says precisely that such an $h$ exists if and only if $$V_a(x,a)=c(a)\bigl(p(x)-2x\bigr)=c(a)V_t(x,a)$$ for some $c\in K$. When it exists, every primitive is $h=c(a)(x-y)+c_0(a)=c(a)s+c_0(a)$. The constant $c_0(a)$ does not affect the field $K(r-h)$, which is $\mathbb C(a,r-c(a)s)$. The two alternatives of the lemma now give [\[eq:lift-fixed-field\]](#eq:lift-fixed-field){reference-type="eqref" reference="eq:lift-fixed-field"}.

In particular, [\[eq:lift-fixed-field\]](#eq:lift-fixed-field){reference-type="eqref" reference="eq:lift-fixed-field"} is not restricted to polynomial integrals or to a bounded degree. The calculation is over $\mathbb C(a)$ and does not assert that every specialized parameter fiber has an identical degree or invariant classification.

[\[prop:translation-exception\]]{#prop:translation-exception label="prop:translation-exception"} The condition $V_a=c(a)V_t$ for some $c\in\mathbb C(a)$ is equivalent to $$V(t,a)=W(t+A(a)),\qquad
 A\in\mathbb C[a],\qquad W\in\mathbb C[t].
 \label{eq:translation-potential}$$ In this case $c=A'$, and the coordinates $$u=t+A(a),\qquad \rho=r-A'(a)s,\qquad s,\qquad a
 \label{eq:translation-coordinates}$$ give a global polynomial symplectic change of variables. They transform $\widehat F$ into $$s'=s+W'(u),\qquad u'=u+s',\qquad a'=a,\qquad\rho'=\rho.
 \label{eq:decoupled-lift}$$ The symbol $\rho$ in this section denotes the coordinate in [\[eq:translation-coordinates\]](#eq:translation-coordinates){reference-type="eqref" reference="eq:translation-coordinates"}, independently of the finite digit permutation used in Section [4](#sec:hilbert-series){reference-type="ref" reference="sec:hilbert-series"}.

Write $$V(t,a)=\sum_{j=0}^m v_j(a)t^j,\qquad
 v_j\in\mathbb C[a],\qquad v_m\ne0.$$ Suppose $V_a=c(a)V_t$. The coefficient of $t^m$ on the right is zero, whereas on the left it is $v_m'$. Hence $v_m'=0$ and $v_m\in\mathbb C^*$. Comparing the coefficients of $t^{m-1}$ next gives $$v_{m-1}'=m c(a)v_m.$$ Define $$A(a)=\frac{v_{m-1}(a)}{m v_m}\in\mathbb C[a].
 \label{eq:translation-from-top-coefficients}$$ Then $c=A'$. In particular, the polynomial nature of this antiderivative follows from the two highest coefficients; it is not an assumption on the initially rational function $c$.

For a new variable $u$, the polynomial $\widetilde V(u,a)=V(u-A(a),a)$ satisfies, with $u$ held fixed, $$\frac{\partial\widetilde V}{\partial a}
 =V_a(u-A(a),a)-A'(a)V_t(u-A(a),a)=0.$$ Since $\widetilde V\in\mathbb C[u,a]$ and the characteristic is zero, every coefficient of a positive power of $a$ vanishes. Thus $\widetilde V=W(u)$ for a polynomial $W\in\mathbb C[u]$, proving [\[eq:translation-potential\]](#eq:translation-potential){reference-type="eqref" reference="eq:translation-potential"}. Conversely, differentiating [\[eq:translation-potential\]](#eq:translation-potential){reference-type="eqref" reference="eq:translation-potential"} gives $V_a=A'(a)W'(t+A(a))=A'(a)V_t$.

The inverse of [\[eq:translation-coordinates\]](#eq:translation-coordinates){reference-type="eqref" reference="eq:translation-coordinates"} is polynomial: $$t=u-A(a),\qquad r=\rho+A'(a)s,$$ with $a$ and $s$ unchanged. Its symplectic property follows from $$\mathrm du=\mathrm dt+A'(a)\mathrm da,\qquad
 \mathrm d\rho=\mathrm dr-A'(a)\mathrm ds-A''(a)s\,\mathrm da.$$ Indeed, $$\begin{aligned}
 \mathrm du\wedge\mathrm ds+\mathrm da\wedge\mathrm d\rho
 &=\mathrm dt\wedge\mathrm ds+A'(a)\mathrm da\wedge\mathrm ds
   +\mathrm da\wedge\mathrm dr-A'(a)\mathrm da\wedge\mathrm ds\\
 &=\mathrm dt\wedge\mathrm ds+\mathrm da\wedge\mathrm dr.\end{aligned}$$ The omitted $A''$ term has the factor $\mathrm da\wedge\mathrm da=0$. Finally, $V_t=W'(u)$ and $V_a=A'W'(u)$. Since $a'=a$, direct substitution in [\[eq:symplectic-lift\]](#eq:symplectic-lift){reference-type="eqref" reference="eq:symplectic-lift"} yields $$u'=t'+A(a)=u+s',\qquad
 \rho'=r+A'W'(u)-A'\bigl(s+W'(u)\bigr)=\rho,$$ as well as the other two equations in [\[eq:decoupled-lift\]](#eq:decoupled-lift){reference-type="eqref" reference="eq:decoupled-lift"}.

Thus the exceptional fixed field can be written as $\mathbb C(a,\rho)$, and the map is a product in the global symplectic coordinates $(u,s,a,\rho)$. This description requires the exact potential [\[eq:translation-potential\]](#eq:translation-potential){reference-type="eqref" reference="eq:translation-potential"}, without an arbitrary added polynomial in $a$. A nonconstant such polynomial has no effect on the two-dimensional base map but does change the fourth equation of the lift.

[\[cor:no-liouville-pair\]]{#cor:no-liouville-pair label="cor:no-liouville-pair"} The map [\[eq:symplectic-lift\]](#eq:symplectic-lift){reference-type="eqref" reference="eq:symplectic-lift"} has no pair of algebraically independent rational first integrals that Poisson commute for $\omega$.

Use the convention $\{t,s\}=\{a,r\}=1$, with brackets between the two coordinate pairs equal to zero. If the second case of [\[eq:lift-fixed-field\]](#eq:lift-fixed-field){reference-type="eqref" reference="eq:lift-fixed-field"} holds, the invariant field has transcendence degree one over $\mathbb C$, and so cannot contain two algebraically independent elements.

In the exceptional case the entire invariant field is $\mathbb C(a,\rho)$, and the symplectic coordinate change gives $\{a,\rho\}=1$. For any two of its elements $I,J$, the bracket is $$\{I,J\}=I_aJ_\rho-I_\rho J_a.
 \label{eq:invariant-field-poisson}$$ If $I,J$ are algebraically independent, $\mathbb C(a,\rho)$ is a finite algebraic extension of $\mathbb C(I,J)$, and it is separable in characteristic zero. Therefore $\mathrm dI$ and $\mathrm dJ$ remain linearly independent in the differential space over $\mathbb C(a,\rho)$. Equivalently, $$\mathrm dI\wedge\mathrm dJ
 =(I_aJ_\rho-I_\rho J_a)\,\mathrm da\wedge\mathrm d\rho\ne0.$$ Equation [\[eq:invariant-field-poisson\]](#eq:invariant-field-poisson){reference-type="eqref" reference="eq:invariant-field-poisson"} then gives $\{I,J\}\ne0$. This excludes every algebraically independent pair in the invariant field, not only its displayed generators.

For example, $V=t^3/3+at$ has $V_a=t$ and $V_t=t^2+a$, which are not proportional over $\mathbb C(a)$; its fixed field is $\mathbb C(a)$. The translation potential $V=(t+a^2)^3/3$ has $c=2a$ and the additional invariant $\rho=r-2as$. In contrast, $V=(t+a^2)^3/3+a$ has the same base map as the second example, but in the same coordinates $\rho'=\rho+1$. Indeed, its derivatives satisfy $V_a=2aV_t+1$, so comparison of the highest $t$ coefficient would force $c=2a$ and leave the nonzero constant $1$. Its fixed field is therefore again $\mathbb C(a)$. The distinction concerns the whole lift, not a classification of all base families whose parameter can be removed by some change of coordinates. The corollary likewise concerns rational integrals for the stated symplectic structure, not other function classes or local notions of integrability.

The ordinary-degree filtration connects the global coboundary equation to exact obstruction counts and to detection on a finite periodic scheme. For the lift, the same equation determines the entire rational invariant field and isolates a global polynomial translation exception. The periodic tests throughout the paper remain identities in complete fixed-point coordinate algebras. Over an algebraically closed field, geometric point values give the same test when the relevant algebra is reduced; without reducedness they only imply that the orbit sum is nilpotent. Whether the stated long-period hypotheses suffice for a geometric-point-only test without a reducedness assumption is not established here.

[\[main-body-end\]]{#main-body-end label="main-body-end"} [\[references-start\]]{#references-start label="references-start"}
