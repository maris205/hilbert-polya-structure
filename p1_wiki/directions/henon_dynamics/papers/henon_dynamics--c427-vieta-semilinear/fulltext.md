---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--c427-vieta-semilinear"
canonical_tex: "henon_dynamics/research_c424_c428/papers/C427_vieta_semilinear/main.tex"
canonical_pdf: "henon_dynamics/research_c424_c428/papers/C427_vieta_semilinear/main.pdf"
source_sha256: "b2692505b12faf8ff30598d1be3d7563170d078173b2474853d0948e35fdf184"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A semilinear atlas for integral Vieta recurrence cycles

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/research_c424_c428/papers/C427_vieta_semilinear>)
- [规范 TeX](<../../../../../henon_dynamics/research_c424_c428/papers/C427_vieta_semilinear/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/research_c424_c428/papers/C427_vieta_semilinear/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/research_c424_c428/papers/C427_vieta_semilinear/README.md>)
- [BibTeX](<../../../../../henon_dynamics/research_c424_c428/papers/C427_vieta_semilinear/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For every integer $n\ge3$ and $a\in\mathbb Z$, consider the polynomial automorphism $F(x_1,\ldots,x_n)=(x_2,\ldots,x_n,x_2\cdots x_n+a-x_1)$. We give a terminating exact construction of its entire integral periodic set as a finite union of integer linear sets with free nonnegative parameters and exact least-period labels. The unbounded output sets account for every unbounded family; the remaining finite set is uniform across all invariant levels. The new argument, for $n\ge4$, is a local rigidity statement for maximal nonzero blocks of a periodic coordinate sequence. Every nonzero update product containing a coordinate whose absolute value exceeds $|a|+4$ has exactly one large factor, with all other factors units. The full periodic recurrence consequently becomes a finite collection of integer linear systems. Classical integral-period bounds and a constructive integer-cone argument complete the parametrization, including all least-period degeneracies. The three-dimensional case uses a previously established computer-assisted classification. We also give finite-level counting rules, while making no claim of efficient complexity or of an executed all-input atlas.
author:
- Anonymous
bibliography:
- references.bib
date: 9 September 2026
title: A semilinear atlas for integral Vieta recurrence cycles
```

## Markdown 正文

**Keywords:** integral dynamics; Vieta recurrence; semilinear set; least period; polynomial automorphism; integer cone.

# The complete integral periodic set {#sec:statement}

Fix $n\ge3$ and $a\in\mathbb Z$, and set $$F(x_1,\ldots,x_n)
 =(x_2,\ldots,x_n,x_2\cdots x_n+a-x_1).
 \label{eq:map}$$ One application of $F$ is one time step throughout. We keep every integer point, including zero coordinates and points on singular levels. The inverse and invariant are $$\begin{aligned}
 F^{-1}(y_1,\ldots,y_n)
   &=(y_1\cdots y_{n-1}+a-y_n,y_1,\ldots,y_{n-1}),\label{eq:inverse}\\
 K(x)&=\sum_{j=1}^n x_j^2-\prod_{j=1}^n x_j-a\sum_{j=1}^n x_j.
 \label{eq:invariant}\end{aligned}$$ Indeed, with the other coordinates fixed, the part depending on a coordinate $t$ is $t^2-(Q+a)t$, where $Q$ is their product. Replacing $t$ by $Q+a-t$ preserves it, and $K$ is invariant under cyclic permutations.

Write $\mathbb N=\{0,1,2,\ldots\}$. An *integer linear set* in $\mathbb Z^n$ means a set $$\mathcal L(v;w_1,\ldots,w_s)
   =\left\{v+\sum_{j=1}^s m_jw_j:m_1,\ldots,m_s\in\mathbb N\right\},
 \qquad v,w_j\in\mathbb Z^n.\label{eq:linear-set}$$ A finite union of such sets is *semilinear*. The parameters are free: no further polynomial equation is imposed on them. We do not require linearly independent directions, an injective parametrization, or disjoint output sets. An empty direction list gives a singleton; after zero directions are deleted, a nonempty list gives an unbounded set, called a *channel* here. This is a parametrization convention, not a claim of maximality or irreducible decomposition.

[\[thm:main\]]{#thm:main label="thm:main"} There is an exact algorithm which terminates for every input $(n,a)$ and outputs finitely many sets of the form [\[eq:linear-set\]](#eq:linear-set){reference-type="eqref" reference="eq:linear-set"}, each labelled by a positive integer, with the following properties.

1.  Their union is exactly $\operatorname{Per}(F,\mathbb Z^n)$, and every point in an output set has the labelled native least period.

2.  The sets with nonzero directions, together with a finite explicit set $E_{n,a}$, give the entire periodic set. Both the channels and $E_{n,a}$ are determined independently of the invariant level $D$.

3.  The algorithm gives the complete semilinear locus of every possible least period. For any $D\in\mathbb Z$, the periodic points and oriented native cycles on $K=D$ are finite and effectively countable.

The new proof in dimensions $n\ge4$ is entirely analytic and algebraic. The case $n=3$ uses the previously established, computer-assisted classification in C421 [@c421].

The construction is finite but may be very large. It does not assert that an atlas has been computed for every input, that its directions are minimal, or that its complexity is practical. Describing the periodic set merely as $F^L(x)=x$ would leave nonlinear integer equations unsolved. The theorem instead outputs unrestricted generators and base points as in [\[eq:linear-set\]](#eq:linear-set){reference-type="eqref" reference="eq:linear-set"}.

## Classical inputs and the additional argument

The unforced map belongs to the Markoff--Hurwitz setting studied by Hu, Tan and Zhang [@huTanZhang2015]. Their object is the full group preserving the unforced polynomial, not this one forced native map. Uniform integral-period mechanisms are classical; Whang [@whang2023] proves effective bounds and decidability in considerably greater generality than needed here. Effective semilinear descriptions and their logical closure properties belong to the classical theory of Ginsburg and Spanier [@ginsburgSpanier1966]. We give explicit proofs of the particular period and integer-cone facts we use, without claiming them as new results.

::: {#tab:ownership}
  Input or contribution      Exact role and ownership boundary
  -------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------
  Uniform integral periods   Classical input; an explicit coarse divisibility bound is proved in Section [3.1](#sec:period){reference-type="ref" reference="sec:period"}.
  Semilinear machinery       Classical input; Section [3.2](#sec:cone){reference-type="ref" reference="sec:cone"} gives a finite integer-cone construction.
  $n=3$ cycles               The complete C421 classification, including its finite computational dependency, is inherited.
  Nonzero-block rigidity     The new $n\ge4$ step controls every mixed-zero window and makes the entire periodic recurrence linear after tagging.

  : The single integrated contribution is the full nonlinear periodic-set reduction and atlas, not its separate classical inputs.
:::

A uniform period bound by itself is not enough. Consider the polynomial automorphism $$H(x,y,z)=(x,y,z+y-x^2).$$ Every periodic point is fixed and satisfies $y=x^2$. Its projection to $(x,y)$ is not semilinear: an integer ray $(x_0,y_0)+m(u,v)$ contained in this parabola for every $m\in\mathbb N$ must have $u=0$ by the quadratic coefficient and then $v=0$. A finite union of such projected linear sets is finite, whereas the parabola has infinitely many integer points. Thus even a uniform least-period bound of one does not supply a semilinear atlas.

For [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"}, the additional mechanism is local to each maximal nonzero block. It handles the mixed-zero domain without assuming that all unbounded cycles belong to a single previously exhibited family. Section [2](#sec:blocks){reference-type="ref" reference="sec:blocks"} proves this mechanism; Sections [3.1](#sec:period){reference-type="ref" reference="sec:period"}--[4](#sec:atlas){reference-type="ref" reference="sec:atlas"} complete the atlas. The ordinary zeta functions at the end concern only this source dynamical system, not target Euler factors or spectral zero data.

# Rigidity of each nonzero block {#sec:blocks}

A periodic orbit of $F$ is encoded by a bi-infinite periodic integer sequence satisfying $$x_{i+n}+x_i=\prod_{j=1}^{n-1}x_{i+j}+a.
 \label{eq:recurrence}$$ Its consecutive length-$n$ blocks are the native states. In this section $n\ge4$, $A=|a|$, and $B=A+4$.

[\[lem:internal\]]{#lem:internal label="lem:internal"} If a periodic sequence has no zero, all its coordinates have absolute value at most $B$. If it has zeros, let $x_1,\ldots,x_r$ be a maximal nonzero block, with $x_0=x_{r+1}=0$, and put $M=\max_{1\le j\le r}|x_j|$. When $r\ge n-1$ and $M>B$, every occurrence of absolute value $M$ in this block is an endpoint.

For a nonzero window of length $n-1$ contained in this block, its two external neighbours belong either to the block or to its adjacent zeros. Therefore $$\left|\prod_{j=1}^{n-1}x_{i+j}\right|\le2M+A.
 \label{eq:local-product-bound}$$ This is a block-local estimate, independent of the heights in other blocks beyond the zeros.

Suppose an internal position has absolute value $M>A$. Because $n-1\ge3$, choose a length-$(n-1)$ window within the block which contains that position strictly internally. Write its external neighbours as $z_-,z_+$. Moving the window one place left preserves the maximum factor and all nonzero internal factors. If the new factor $z_-$ is zero, the inequality $M|z_-|\le2M+A$ is immediate; otherwise the shifted window is in the same block and [\[eq:local-product-bound\]](#eq:local-product-bound){reference-type="eqref" reference="eq:local-product-bound"} proves it. The right shift similarly gives $M|z_+|\le2M+A$. Since $M>A$, both neighbours have absolute value less than three, and thus at most two. The unshifted recurrence now gives $$M\le\left|\prod x_j\right|=|z_-+z_+-a|\le A+4=B.$$ This contradicts $M>B$. If the whole sequence is nonzero, use its global maximum in an internal window; the identical argument proves the first assertion. The all-zero sequence needs no block analysis.

[\[lem:large-block\]]{#lem:large-block label="lem:large-block"} Every maximal nonzero block of length at least $n-1$ containing a coordinate of absolute value greater than $B$ has length exactly $n$. Its $n-2$ internal coordinates are units. After possibly reversing indices in the proof, its endpoints satisfy $$x_n=\varepsilon x_1+a,\qquad
 \varepsilon=\prod_{j=2}^{n-1}x_j\in\{1,-1\},\qquad
 (1+\varepsilon)a=0.
 \label{eq:block-relations}$$

If the block length is $n-1$, the recurrence across its two zeros gives $\prod_{j=1}^{n-1}x_j=-a$. The product is a nonzero integer, so $a\ne0$ and every factor has absolute value at most $A$. It cannot be a large block.

Suppose the length is at least $n$ and its maximum is $M>B$. Lemma [\[lem:internal\]](#lem:internal){reference-type="ref" reference="lem:internal"} places a maximum at an endpoint. The recurrence is preserved by index reversal with the same $a$, so assume $|x_1|=M$. This reversal is a proof device, not an identification of oriented native orbits. Put $C=\prod_{j=2}^{n-1}x_j$. The recurrence at the left zero gives $x_n=Cx_1+a$, whence $$M|C|\le M+A<2M.$$ The nonzero integer $C$ is therefore a sign $\varepsilon$, and each of its factors is a unit. If the length equals $n$, the next recurrence gives $x_1=\varepsilon x_n+a$, proving [\[eq:block-relations\]](#eq:block-relations){reference-type="eqref" reference="eq:block-relations"}. The second endpoint need not also exceed $B$; no such assumption is used.

It remains to exclude a length at least $n+1$. The next coordinate is $$x_{n+1}=\varepsilon x_n+a-x_1=(1+\varepsilon)a.$$ It is nonzero, so $a\ne0$, $\varepsilon=1$, and $x_{n+1}=2a$. The window $x_3,\ldots,x_{n+1}$ has unit factors up to $x_{n-1}$ and remaining factors $x_n,2a$. Its external neighbours are the unit $x_2$ and a coordinate $x_{n+2}$ of absolute value at most $M$ (possibly the right zero). Consequently $$2A|x_n|\le M+A+1,\qquad
 (2A-1)M\le2A^2+A+1.$$ Here $|x_n|=|x_1+a|\ge M-A$ and $A\ge1$. But $$(2A-1)(A+4)-(2A^2+A+1)=6A-5>0,$$ contradicting $M>A+4$. A right-end maximum is covered by the same reversal argument.

[\[cor:window\]]{#cor:window label="cor:window"} In any periodic sequence, each nonzero update product in [\[eq:recurrence\]](#eq:recurrence){reference-type="eqref" reference="eq:recurrence"} either has all factors of absolute value at most $B$, or has exactly one factor exceeding $B$ in absolute value, with all its other factors in $\{1,-1\}$.

The zero-free case follows from Lemma [\[lem:internal\]](#lem:internal){reference-type="ref" reference="lem:internal"}. Otherwise a nonzero window lies in one maximal nonzero block. Blocks shorter than $n-1$ cannot contain such a window; blocks of length $n-1$ are bounded. A block with a large factor has exactly $n$ entries by Lemma [\[lem:large-block\]](#lem:large-block){reference-type="ref" reference="lem:large-block"}. Its two possible nonzero windows of length $n-1$ each omit one endpoint. Thus a window with a large factor has only one large endpoint, and all companions are units. If neither endpoint in that window is large, it is the first case.

The corollary includes arbitrarily many large coordinates separated by zeros: an update product containing a zero is zero regardless of the other factors. It imposes no independence assumption on distinct blocks, no bound on their number, and no guess about the dimension of a channel. These are the cases which a zero-free height bound alone leaves untreated.

# Classical finite constructions

## A uniform native-period divisor {#sec:period}

For later use define the explicitly computable integers $$E_n=|\operatorname{AGL}_n(\mathbb F_2)|
     =2^n\prod_{j=0}^{n-1}(2^n-2^j),\qquad
 L_n=2E_n\operatorname{lcm}(1,2,\ldots,2^n).
 \label{eq:period-divisor}$$ The following coarse bound is a classical local integral-period argument. Its role is only to make the subsequent construction finite; neither the bound nor general decidability is a new contribution. For broader results see Whang [@whang2023].

[\[lem:near-identity\]]{#lem:near-identity label="lem:near-identity"} Let $g(z)=z+4U(z)$ with $U\in\mathbb Z_2[z_1,\ldots,z_n]^n$. Every finite-period point of $g$ in $\mathbb Z_2^n$ is fixed.

Use the vector valuation $v_2(w)=\min_jv_2(w_j)$, with value $+\infty$ at zero. Suppose $\delta=g(z)-z\ne0$ and $m=v_2(\delta)\ge2$. Integer polynomials are $1$-Lipschitz, so $$g^2(z)-z=2\delta+4\bigl(U(z+\delta)-U(z)\bigr)
          \equiv2\delta\pmod{2^{m+2}}.$$ Its valuation is exactly $m+1$. The polynomial $g^2$ again has the form $\mathrm{id}+4V$. Repeating gives $$v_2\bigl(g^{2^j}(z)-z\bigr)=m+j\qquad(j\ge0).$$ Put $h=g^{2^j}=\mathrm{id}+4V$ and $m'=m+j$. Each intermediate $h^i(z)$ is congruent to $z$ modulo $2^{m'}$, by induction. Hence each displacement $h^{i+1}(z)-h^i(z)$ is congruent to $h(z)-z$ modulo $2^{m'+2}$. For odd $q$, summing the $q$ displacements shows that $h^q(z)-z$ has valuation $m'$, not infinity. Every positive integer is $2^jq$ with $q$ odd, so $z$ never returns.

[\[prop:period-divisor\]]{#prop:period-divisor label="prop:period-divisor"} For any integer polynomial automorphism $G$ of $\mathbb A^n$, with integer polynomial inverse, the least period of every point in $\operatorname{Per}(G,\mathbb Z^n)$ divides $L_n$.

Let $P$ be periodic, and let $r$ be its period modulo two. Reduction of $G$ is a permutation of $\mathbb F_2^n$, so $1\le r\le2^n$. On the returning residue ball introduce $$g(z)=\frac{G^r(P+2z)-P}{2}.$$ This map and its inverse have integer coefficients. Its terms of degree at least two have even coefficients, so its coefficientwise reduction is an element of $\operatorname{AGL}_n(\mathbb F_2)$. Let that element have order $e$, which divides $E_n$. Then $h=g^e=\mathrm{id}+2V$ with integer polynomial $V$, and $$h^2(z)=z+2V(z)+2V(z+2V(z))=z+4W(z)$$ for an integer polynomial $W$. The point zero is periodic under $g$ and hence under $h^2$. Lemma [\[lem:near-identity\]](#lem:near-identity){reference-type="ref" reference="lem:near-identity"} implies $g^{2e}(0)=0$, or $G^{2re}(P)=P$. The least period therefore divides $2re$, which divides $L_n$.

The inverse [\[eq:inverse\]](#eq:inverse){reference-type="eqref" reference="eq:inverse"} shows that the proposition applies to $F$ for all $a$ and all ordinary points, without a smoothness or nonzero-coordinate qualification. Iterates in this proof provide a divisibility bound; they do not replace the native time unit.

## A constructive integer-cone lemma {#sec:cone}

The next elementary construction lies within classical semilinear theory [@ginsburgSpanier1966]. It records all finite enumeration steps so that the atlas does not hide an unknown truncation.

[\[lem:cone\]]{#lem:cone label="lem:cone"} Given an integer matrix $M$ and an integer vector $b$, the set $$S=\{u\in\mathbb N^k:Mu=b\}
 \label{eq:integer-system}$$ can be effectively expressed as a finite union of integer linear sets. The same holds with finitely many integer linear inequalities, and after any integer affine projection.

Form the rational pointed cone $$C=\{(q,u)\in\mathbb R_{\ge0}^{k+1}:Mu=qb\}.$$ If $C\ne\{0\}$, its intersection with $q+\sum_j u_j=1$ is a compact rational polytope. Enumerating finite subsets of the coordinate hyperplanes and solving the corresponding rational linear systems gives its vertices, including lower-dimensional and degenerate-rank cases. The polytope is the convex hull of these vertices. Clearing denominators gives finitely many integer ray generators $w_1,\ldots,w_t$ of $C$. If $C=\{0\}$, take no ray generators.

Set $R_\ell=\sum_{j=1}^t(w_j)_\ell$ and enumerate the finite set $$H=\{z\in C\cap\mathbb Z^{k+1}:0\le z_\ell\le R_\ell
                          \text{ for all }\ell\}.$$ It generates the additive monoid $C\cap\mathbb Z^{k+1}$. Indeed, write $z=\sum_j\lambda_jw_j$ with $\lambda_j\ge0$. Then $$z=\sum_j\lfloor\lambda_j\rfloor w_j+
       \sum_j(\lambda_j-\lfloor\lambda_j\rfloor)w_j.$$ The remainder is an integer point of $C$, and each of its coordinates is bounded by $R_\ell$. Thus it belongs to $H$, as does each $w_j$. The case $C=\{0\}$ has $H=\{0\}$ and satisfies the same assertion.

An element of this monoid with first coordinate one has exactly one generator of first coordinate one in any such decomposition, and all other used generators have first coordinate zero. Generators with first coordinate at least two cannot occur. It follows that $$S=\bigcup_{(1,v)\in H}
       \left(v+\sum_{(0,h)\in H}\mathbb Nh\right).
 \label{eq:cone-output}$$ An empty union means no solutions. Zero directions can be removed; the construction also covers $k=0$.

Replace an integer inequality $c\cdot u\ge d$ by $c\cdot u-t=d$ with a new variable $t\in\mathbb N$. This reduces finitely many inequalities to [\[eq:integer-system\]](#eq:integer-system){reference-type="eqref" reference="eq:integer-system"}. Finally an integer affine map sends a base point and each generator to another integer base point and generator, preserving a representation of the form [\[eq:linear-set\]](#eq:linear-set){reference-type="eqref" reference="eq:linear-set"}.

No minimal Hilbert basis, optimal ray list or efficient integer programming method is needed. Every enumeration has an explicit finite range obtained by rational linear algebra from its input.

# The exact finite construction {#sec:atlas}

Fix $n\ge4$ and $a$, and use $B=|a|+4$ and $L=L_n$ from [\[eq:period-divisor\]](#eq:period-divisor){reference-type="eqref" reference="eq:period-divisor"}. All indices in this section are read modulo $L$. Proposition [\[prop:period-divisor\]](#prop:period-divisor){reference-type="ref" reference="prop:period-divisor"} implies that any periodic point has a coordinate word of length $L$, possibly with a smaller least period.

## Finite tags and actual products

Enumerate every length-$L$ array in the finite alphabet $$\mathcal A_B=\{-B,-B+1,\ldots,B\}\cup\{\star_+,\star_-\}.$$ Arrays are not identified under cyclic rotation: every initial phase is retained. A constant label $c$ imposes $X_i=c$. For each large label introduce its own nonnegative integer variable $u_i$ and impose $$X_i=B+1+u_i\quad(\star_+),\qquad
 X_i=-B-1-u_i\quad(\star_-).
 \label{eq:large-tags}$$ These substitutions make the label semantics exact, including the threshold and the sign. Zero occurs only as the constant label zero.

For each window $i+1,\ldots,i+n-1$, apply the exhaustive rule in Table [2](#tab:tags){reference-type="ref" reference="tab:tags"}. If any window is rejected, discard its entire array. For every retained array, let $P_i$ be the expression in the table and impose all $L$ equations $$X_{i+n}+X_i=P_i+a\qquad(0\le i<L).
 \label{eq:linear-recurrence}$$

::: {#tab:tags}
  Labels in a length-$(n-1)$ window                    Product expression or action
  ---------------------------------------------------- -------------------------------------------------------------------------------------------------------------
  At least one constant zero                           $P_i=0$, with any number of large labels.
  No zero and no large label                           $P_i$ is the product of all constant labels.
  No zero; exactly one large label; all others units   $P_i=\varepsilon X_j$, where $j$ is the large position and $\varepsilon$ is the product of the unit labels.
  Every other case                                     Reject the array.

  : Exact product cases. The rejection is necessary for a periodic word by Corollary [\[cor:window\]](#cor:window){reference-type="ref" reference="cor:window"}; the retained cases are actual integer products, not approximations.
:::

After [\[eq:large-tags\]](#eq:large-tags){reference-type="eqref" reference="eq:large-tags"}, equations [\[eq:linear-recurrence\]](#eq:linear-recurrence){reference-type="eqref" reference="eq:linear-recurrence"} form an integer linear system $Mu=b$, $u\in\mathbb N^k$. In particular, no two undetermined variables are multiplied. Lemma [\[lem:cone\]](#lem:cone){reference-type="ref" reference="lem:cone"} supplies all solutions with free nonnegative parameters. Project them to $(X_0,\ldots,X_{n-1})$.

[\[prop:tag-exact\]]{#prop:tag-exact label="prop:tag-exact"} The union of these projected solution sets is exactly $\operatorname{Per}(F,\mathbb Z^n)$.

For necessity, take any periodic point and its actual length-$L$ coordinate word. Label small coordinates by their values and large coordinates by their signs. Corollary [\[cor:window\]](#cor:window){reference-type="ref" reference="cor:window"} shows that none of its windows is rejected. Its actual large offsets are nonnegative integers, and the recurrence gives every equation [\[eq:linear-recurrence\]](#eq:linear-recurrence){reference-type="eqref" reference="eq:linear-recurrence"}.

Conversely, take a solution from any retained array. The substitutions [\[eq:large-tags\]](#eq:large-tags){reference-type="eqref" reference="eq:large-tags"} ensure that the labels are true statements about the resulting integer coordinates. In each retained case the expression $P_i$ is therefore the actual product of the coordinates in that window. All equations [\[eq:linear-recurrence\]](#eq:linear-recurrence){reference-type="eqref" reference="eq:linear-recurrence"} are exactly the original recurrence. Starting from its first $n$ coordinates, $F$ moves along this word one native step at a time and returns at time $L$. Thus every projected solution is a genuine periodic point.

## Exact least-period labels

For each positive divisor $r\mid L$, add to each retained system the linear equations $$X_{i+r}=X_i\qquad(0\le i<L).
 \label{eq:r-periodic}$$ For every proper divisor $d\mid r$, exclude period $d$ by requiring some index $i_d$ with $X_{i_d+d}\ne X_{i_d}$. This is a finite union of linear cases: choose $i_d\in\{0,\ldots,L-1\}$ and $\eta_d\in\{1,-1\}$, and impose $$\eta_d(X_{i_d+d}-X_{i_d})\ge1.
 \label{eq:exclude-period}$$ Enumerate all such choices for all proper divisors. If $r=1$, there are no exclusion inequalities. Add nonnegative slack variables and apply Lemma [\[lem:cone\]](#lem:cone){reference-type="ref" reference="lem:cone"} once more.

These systems have exactly least scalar period $r$: [\[eq:r-periodic\]](#eq:r-periodic){reference-type="eqref" reference="eq:r-periodic"} makes the least period divide $r$, and [\[eq:exclude-period\]](#eq:exclude-period){reference-type="eqref" reference="eq:exclude-period"} excludes every proper divisor. Conversely a word with least period $r$ supplies at least one index and sign for every excluded divisor, so is included in the finite union. Integer strict inequalities are encoded without losing equality or sign boundary cases.

The least scalar shift period equals the least native state period. A repeated state determines all subsequent entries by the recurrence and all preceding entries by its inverse; hence it repeats the entire word. The converse follows immediately by taking consecutive length-$n$ states. Thus each projected linear set can be labelled by $r$ without a change of clock or an orbit quotient.

## Channels, finite remainder and termination

In every projected linear set remove zero direction vectors. If a nonzero direction remains, taking its nonnegative multiples already gives an unbounded sequence of points. The whole set has the exact least-period label just established. If no direction remains, the output is one explicit point. Collect all such points in $E_{n,a}$. We obtain the complete equality $$\operatorname{Per}(F,\mathbb Z^n)=E_{n,a}\ \cup\
 \bigcup_{j=1}^{J}
    \mathcal L(v_j;w_{j1},\ldots,w_{js_j}),
 \qquad s_j\ge1,\quad w_{jk}\ne0.
 \label{eq:atlas}$$ The lists may overlap, but no periodic point is missing. Every output labelled by one period consists solely of points with that period, so different period strata cannot overlap.

All numbers $L,B$, all tag arrays, all divisors and exclusion choices, all cone vertices, and all boxes used in Lemma [\[lem:cone\]](#lem:cone){reference-type="ref" reference="lem:cone"} are computable and finite. This proves termination for every $(n,a)$, without an empirical stopping rule. Once the list is produced, $$R_{n,a}=\max\bigl(\{0\}\cup
          \{\|P\|_\infty:P\in E_{n,a}\}\bigr)$$ is an explicit finite remainder bound. It depends on $n,a$, not on an invariant level. If desired, singleton entries lying in a channel can be removed by a nonnegative linear-system membership test. Such removal is optional and does not affect [\[eq:atlas\]](#eq:atlas){reference-type="eqref" reference="eq:atlas"} or the finiteness of the remainder.

This completes the new $n\ge4$ part of Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}. No step assumes that each channel is a line, that zero-separated blocks can be chosen independently, or that all large cycles arise from a single special family.

# Three dimensions, level counts and scope {#sec:completion}

## The inherited three-dimensional case

The preceding internal-window argument needs $n-1\ge3$ and is not applied when $n=3$. In that dimension, Theorem 2.1 and its complete table in C421 [@c421] classify every integral periodic orbit of $(x,y,z)\mapsto(y,z,yz+a-x)$, with exact native least periods $$\{1,2,3,4,5,6,8,9,12\}.$$ That theorem is an explicitly inherited computer-assisted result, not a new computation-free conclusion of this paper.

For clarity, its table gives precisely the structure needed here. For fixed $a$, the constant words satisfy $a=2r-r^2$ and form a finite set. The two-periodic alternating words satisfy $$(u-1)(v-1)=1-a.$$ If $a\ne1$, finite divisor enumeration gives all integer pairs; if $a=1$, the solutions lie on $u=1$ or $v=1$. The exact-period and orientation exclusions in that table are linear inequalities or removal of finitely many parameters. Every other parametric word is affine in its integer parameter, with linear range conditions, and the two sporadic words give finitely many points. Taking every consecutive triple of these words preserves this description. An unrestricted integer parameter splits into its nonnegative and negative rays, and a finite exclusion splits a ray into finitely many rays or points. Thus all these sets are effectively of the form [\[eq:linear-set\]](#eq:linear-set){reference-type="eqref" reference="eq:linear-set"}, with the exact least-period labels supplied by the table. This proves the $n=3$ part of Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"} using exactly the stated prior theorem.

The C421 proof reduces its residual to a finite exact certificate, with independently rebuilt cycles, and retains all unbounded families symbolically. Its source, actual certificate and review are available with that manuscript. None was rerun for the present paper. In particular, our hand proof for $n\ge4$ must not be used to relabel the three-dimensional imported theorem as computation-free.

## Finite levels and ordinary cycle counts

Appendix [6](#app:height){reference-type="ref" reference="app:height"} reproduces a previously completed auxiliary height argument, including its degenerate branches. For any $n\ge3$ and $a,D\in\mathbb Z$, it gives $$\|P\|_\infty\le R(n,a,D)
       :=2n^2\bigl(|a|+|D|+n+2\bigr)
 \label{eq:level-bound}$$ for every periodic point on $K=D$. This is a level-dependent bound, not a common bound over all levels.

Enumerate all integer points of $K=D$ in the box $[-R(n,a,D),R(n,a,D)]^n$. Put an arrow $P\to F(P)$ when both ends are in this finite set. Its directed cycles are exactly the periodic points on the level: every genuine periodic orbit is inside the box by [\[eq:level-bound\]](#eq:level-bound){reference-type="eqref" reference="eq:level-bound"}, and every graph cycle is an actual native orbit. The cycle length is its least period. This gives an exact terminating counting rule using only finite integer arithmetic. The graph is a proved algorithm, not a reported execution over all inputs.

Alternatively, use the atlas membership tests on this finite set. Always count distinct coordinate points, not their possibly repeated semilinear parameter representations. If $N_r(a,D)$ is the number of points of least period $r$, then $c_r(a,D)=N_r(a,D)/r$ is the number of oriented native cycles. Consequently $$\begin{aligned}
 \#\operatorname{Fix}(F^m\mid K=D,\mathbb Z^n)&=\sum_{r\mid m}r\,c_r(a,D),\\
 \zeta_{a,D}(z)&=\prod_r(1-z^r)^{-c_r(a,D)}.
 \label{eq:level-zeta}\end{aligned}$$ There are only finitely many nonzero factors. These are ordinary source-dynamical counts with no multiplicity weighting, prime relabeling or altered clock. A finite-count zeta on the entire integer lattice is not asserted.

For example, when $n=4$ and $a\ne0$, the previously observed zero-product family $P=(0,a,0,t)$, $t\in\mathbb Z$, follows the word $$(0,a,0,t,a,0,a,a-t).$$ Every cyclic window of length three contains a zero, so this is an actual $F$-word with period dividing eight. Four steps send its first coordinate from $0$ to $a$, excluding all proper divisors of eight; its least period is eight for every $t$. Its invariant is $t(t-a)$, illustrating why an unbounded channel can meet each fixed level in only finitely many points. This family is an illustration, not the basis of the exhaustive atlas or an additional contribution counted separately.

## Limitations and reproducibility

The result concerns the specified single native map over the ordinary integer lattice. It does not classify rational or complex periodic schemes, arbitrary words in all Vieta involutions, or unrelated additive forcing in each coordinate. The output is not a canonical or minimal channel decomposition. The elementary constant $L_n$ is large, and no useful complexity bound is claimed.

All new $n\ge4$ arguments, the classical finite constructions, and the level-height proof are included here. The research-stage bounded exploratory program is not a proof dependency; it neither generated the full atlas nor replaces any infinite-parameter argument. The inherited $n=3$ computation is identified above. Source ownership and actual access limits are recorded in the accompanying source audit. These bounded checks do not certify worldwide priority or journal acceptance.

The ordinary factors in [\[eq:level-zeta\]](#eq:level-zeta){reference-type="eqref" reference="eq:level-zeta"} do not establish target arithmetic Euler factors, root numbers, automorphy, a spectral zero correspondence or a Hilbert--Pólya realization. The result is a source-system classification.

#### Availability and preparation.

The LaTeX source, proof notes, source audit and internal review records accompany this manuscript; the cited C421 package contains its own exact computational evidence. Preparation and internal checking used AI assistance; no human peer review is claimed. No human participants or sensitive personal data are involved. Named-author contribution, funding and competing-interest information was not supplied, and no such declaration is inferred from the anonymous working-paper format.

# An explicit complete height bound on each level {#app:height}

We reproduce the previously completed V4-H auxiliary argument so that the finite-level assertion has a typeset proof. Its starting fork inequality has classical antecedents in the unforced Markoff--Hurwitz setting [@huTanZhang2015] and in the forced three-variable inequalities of Maloni, Palesi and Tan [@maloniPalesiTan2015]. The following case analysis is for the specified native cyclic map; it does not substitute a full-group fundamental domain such as that of Shin [@shin2023] for a native periodic orbit.

[\[prop:height\]]{#prop:height label="prop:height"} For every $n\ge3$ and $a,D\in\mathbb Z$, each periodic orbit of $F$ on $K=D$ is contained in the box of radius $2n^2(|a|+|D|+n+2)$ in the maximum norm.

Put $A=|a|$ and choose a point of the finite orbit maximizing $h(P)=\sum_j|P_j|$. Write it as $$P=(y,z_1,\ldots,z_{n-2},x),\qquad
 u=|x|,\quad v=|y|,\quad Q=\prod_{j=1}^{n-2}z_j,$$ and set $S=u+v$, $M=\max(u,v,|z_1|,\ldots,|z_{n-2}|)$. The preceding native state updates $x$ before a cyclic permutation; the following state updates $y$. The maximality of $h$ gives both $$|Qy+a-x|\le u,\qquad |Qx+a-y|\le v.
 \label{eq:fork-two}$$ Adding the resulting triangle inequalities yields $$(|Q|-2)S\le2A.
 \label{eq:fork-sum}$$ If $|Q|=2$, the two inequalities also give $$|u-v|\le A/2.
 \label{eq:fork-difference}$$ We show in every case that $$M\le B_0:=2n(A+|D|+n+2).
 \label{eq:local-height-target}$$ Any coordinate of any orbit point is then at most its $h$-value, which is at most $h(P)\le nB_0$. This gives the claimed radius; the extra factor $n$ is retained because we maximized $h$, not one coordinate.

*Case $Q=0$.* The complete coordinate product is zero, and $$D=\sum_jP_j^2-a\sum_jP_j\ge M^2-nAM.$$ If $M>nA+|D|+1$, the last quantity exceeds $|D|$, a contradiction. This proves [\[eq:local-height-target\]](#eq:local-height-target){reference-type="eqref" reference="eq:local-height-target"} without requiring later update products to remain zero.

*Case $|Q|\ge3$.* If $S=0$, [\[eq:fork-two\]](#eq:fork-two){reference-type="eqref" reference="eq:fork-two"} forces $a=0$, and $D=\sum_jz_j^2\ge M^2$. If $S>0$, integrality gives $S\ge1$, and [\[eq:fork-sum\]](#eq:fork-sum){reference-type="eqref" reference="eq:fork-sum"} implies $S\le2A$ and $|Q|\le2+2A$. Every $z_j$ is a nonzero integer, so $|z_j|\le|Q|$, and hence $M\le2+2A$. Both branches satisfy [\[eq:local-height-target\]](#eq:local-height-target){reference-type="eqref" reference="eq:local-height-target"}.

*Case $|Q|=1$.* Every $|z_j|=1$. The inequality $|xy|\le(x^2+y^2)/2$ gives $$D=x^2+y^2-Qxy+\sum_jz_j^2-a\left(x+y+\sum_jz_j\right)
   \ge M^2/2-nAM.$$ If $M>2nA+2|D|+2$, this exceeds $|D|$, again a contradiction. The resulting bound is smaller than $B_0$.

*Case $|Q|=2$, with a small endpoint.* Each $|z_j|\le2$. If $\min(u,v)\le A+1$, then [\[eq:fork-difference\]](#eq:fork-difference){reference-type="eqref" reference="eq:fork-difference"} gives $M\le\max(2,3A/2+1)<B_0$.

*Case $Q=2$, with $u,v>A+1$.* For real numbers, $|b-x|\le|x|$ says that $b$ lies between $0$ and $2x$. In [\[eq:fork-two\]](#eq:fork-two){reference-type="eqref" reference="eq:fork-two"}, $Qy+a$ and $Qx+a$ are nonzero and have the signs of $Qy$ and $Qx$, respectively, because $2u,2v>A$. Therefore $Qxy>0$. When $Q=2$, write $x=\sigma u$, $y=\sigma v$ with $\sigma\in\{1,-1\}$. The two inequalities become $$0\le2v+\sigma a\le2u,\qquad
 0\le2u+\sigma a\le2v.$$ Thus $\sigma a\le-2|u-v|$. If $a\ne0$, then $\sigma a=-A$, and $$D=(u-v)^2+A(u+v)+\sum_j(z_j^2-a z_j)
   \ge A(u+v)-2A(n-2).$$ Since $A\ge1$, this gives $u+v\le|D|+2(n-2)$ and the desired bound. If $a=0$, the two inequalities force $u=v$; in that residual case the individual updates of both $x$ and $y$ are fixed.

*Case $Q=-2$, with $u,v>A+1$.* The same sign argument gives $x=\sigma u$, $y=-\sigma v$. Now [\[eq:fork-two\]](#eq:fork-two){reference-type="eqref" reference="eq:fork-two"} becomes $$0\le2v+\sigma a\le2u,\qquad
 0\le2u-\sigma a\le2v.$$ Hence $\sigma a=2(u-v)$, or $x+y=a/2$. Direct substitution shows that the individual updates of $x$ and $y$ are again fixed. For odd $a$, this integer subcase is empty.

*The remaining fixed-endpoint directions.* Both residual cases just obtained have fixed updates at $x,y$, nonzero $Q$ with $|Q|=2$, and [\[eq:fork-difference\]](#eq:fork-difference){reference-type="eqref" reference="eq:fork-difference"}. After the next native update of $y$, only a cyclic permutation has occurred. The following native step updates $z_1$ to $$z_1'=(Q/z_1)xy+a-z_1.$$ Here $Q/z_1$ is a nonzero integer. Both new states remain in the same orbit, so $$uv-A-2\le|z_1'|\le h(P)\le u+v+2(n-2),$$ and therefore $$(u-1)(v-1)\le A+2n-1.
 \label{eq:degenerate-product}$$ If $\max(u,v)>A+2n+3$, the two factors on the left, by [\[eq:fork-difference\]](#eq:fork-difference){reference-type="eqref" reference="eq:fork-difference"}, are respectively greater than $A+2n+2$ and $A/2+2n+2$. Their product exceeds $A+2n-1$, contradicting [\[eq:degenerate-product\]](#eq:degenerate-product){reference-type="eqref" reference="eq:degenerate-product"}. Thus $M\le A+2n+3<B_0$ in the final cases as well. All cases are exhausted, proving [\[eq:local-height-target\]](#eq:local-height-target){reference-type="eqref" reference="eq:local-height-target"} and the result.

The argument includes zero coordinates, both signs, $a=0$, singular levels and the degenerate $Q=\pm2$ directions. It does not assume that every Vieta generator decreases height. Only the two adjacent native updates at a maximum and, in the residual case, the next native update are used.
