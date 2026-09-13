---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--c426-affine-good-models"
canonical_tex: "henon_dynamics/research_c424_c428/papers/C426_affine_good_models/main.tex"
canonical_pdf: "henon_dynamics/research_c424_c428/papers/C426_affine_good_models/main.pdf"
source_sha256: "a93a7fd80103e2e1ffa384f0d7bd6d4b395bd3b0d8af6616a157324e0a8ba9ee"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Affine good models of single-factor Hénon maps: unique local discs and the ideal-square obstruction

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/research_c424_c428/papers/C426_affine_good_models>)
- [规范 TeX](<../../../../../henon_dynamics/research_c424_c428/papers/C426_affine_good_models/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/research_c424_c428/papers/C426_affine_good_models/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/research_c424_c428/papers/C426_affine_good_models/README.md>)
- [BibTeX](<../../../../../henon_dynamics/research_c424_c428/papers/C426_affine_good_models/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Let $F(x,y)=(y,f(y)-ax)$ over a number field, with $a\ne0$ and $\deg f=d\ge2$. We classify every two-dimensional affine coordinate change in which $F$ has regular good reduction. Locally, the highest homogeneous terms of the map and its inverse, together with separation of their reduced indeterminacy points, force the affine lattice to be the square of one unique disc. This gives a finite coefficient test in every residue characteristic, including primes dividing $d$. If all local tests pass and $b$ is the leading coefficient of $f$, the scale ideal $I$ is determined by $(b)I^{d-1}=\mathcal O_K$. A single global affine good model exists exactly when $I^2$ is principal. We give an explicit basis construction and describe all models as one left coset of the integral affine group. Examples distinguish repair by a mixed affine matrix from repair by a common scalar, and exhibit a genuine local--global obstruction. The proof is self-contained apart from standard arithmetic of ideals and requires no computer-assisted certificate.
bibliography:
- references.bib
title: |
  Affine good models of single-factor Hénon maps:\
  unique local discs and the ideal-square obstruction
```

## Markdown 正文

# Introduction

An affine coordinate change can remove denominators from a polynomial automorphism without preserving its degree or its regularity after reduction. For a Hénon map, these conditions must be imposed on both the map and its inverse. Even when appropriate coordinates exist at every finite place, their local lattices need not admit one global basis. The question addressed here is to classify all such coordinate changes for one Hénon factor over an arbitrary number field.

The local argument is genuinely about the full group $\operatorname{Aff}(\mathbb A^2)$: diagonal scaling and equal translations are conclusions, not restrictions on the search. Two independent indeterminacy directions force a common scale. The remaining coefficient condition is encoded by the auxiliary polynomial $q(Y)=f(Y)-aY$. Its good-reduction disc is unique. Globally, the unique local lattices assemble to $I\oplus I$, and the obstruction is the ideal class of $I^2$, not that of $I$ itself.

#### Relation to prior work.

We use Kawaguchi's regular good-reduction definition [@Kawaguchi2013 Definition 4.1]; his Propositions 4.2--4.3 provide the adjacent local height theory. Bruin and Molnar study affine minimal models for one-dimensional rational maps, including nonprincipal-ideal phenomena [@BruinMolnar2012 Proposition 2.10 and Section 6]. Their affine matrix notation concerns the projective line, not the full affine group of the plane. Petsche and Stout prove a global minimal-model theorem for projective endomorphisms over a principal ideal domain [@PetscheStout2014]; their lattice-patching mechanism is relevant background but does not give the present statement for arbitrary class groups for a map with indeterminacy at infinity. Allen, DeMark and Petsche classify the unit-ball regime for a standard quadratic Hénon family over complete locally compact non-Archimedean fields of odd residue characteristic [@AllenDeMarkPetsche2018 Theorem 11].

Accordingly, neither good reduction, the elementary escape criterion, additive approximation, nor the determinant/Steinitz obstruction is claimed as a new general mechanism. The contribution is their exact application after the all-affine rigidity argument: all coefficients, all finite places, all mixed affine matrices and all ideal classes are covered by one classification. Table [1](#tab:ownership){reference-type="ref" reference="tab:ownership"} records the specific distinctions. The complete argument develops the frozen internal proof package [@GR5WorkingNotes]; that source is an unpublished AI-assisted working document, not an external theorem or human peer-review certificate.

::: {#tab:ownership}
  Source                                             Existing input or adjacent mechanism                       Distinction here
  -------------------------------------------------- ---------------------------------------------------------- ----------------------------------------------------------------------
  Kawaguchi [@Kawaguchi2013]                         Regular good reduction and local height properties         Classification of all affine good coordinates
  Bruin--Molnar [@BruinMolnar2012]                   Rational-map minimal models and nonprincipal ideals        Two-dimensional mixed matrices and two indeterminacy directions
  Petsche--Stout [@PetscheStout2014]                 Lattice patching for projective endomorphisms over a PID   Arbitrary number-field class group and exact $I^2$ obstruction
  Allen--DeMark--Petsche [@AllenDeMarkPetsche2018]   Quadratic unit-ball regime in odd residue characteristic   All degrees and wild places, followed by global model classification

  : Source ownership and the scope not supplied by those results. The comparison concerns hypotheses and objects, not a claim of an exhaustive priority search.
:::

#### Organization.

Section [2](#sec:classification){reference-type="ref" reference="sec:classification"} states the classification. Sections [3](#sec:rigidity){reference-type="ref" reference="sec:rigidity"} and [4](#sec:localtest){reference-type="ref" reference="sec:localtest"} prove the local rigidity and finite centre test. Section [5](#sec:global){reference-type="ref" reference="sec:global"} patches the centres and constructs a global basis exactly when the determinant ideal is principal. Section [6](#sec:examples){reference-type="ref" reference="sec:examples"} proves the resulting class-group criterion and gives explicit examples.

# The classification {#sec:classification}

Fix a number field $K$, put $R=\mathcal O_K$, and take $a\in K^\times$ and $f\in K[Y]$ of degree $d\ge2$. Let $$\label{eq:Fq}
 F(x,y)=(y,f(y)-ax),\qquad
 q(Y)=f(Y)-aY=\sum_{j=0}^d q_jY^j.$$ Write $b=q_d\ne0$. For a finite place $v$, let $E=K_v$, let $O=\mathcal O_{K_v}$, and normalize $v:E^\times\to\mathbb Z$. The residue field is $\kappa_v$. A coordinate map $T$ sends the new coordinates to the original ones, so its model is $G=T^{-1}FT$.

[\[def:good\]]{#def:good label="def:good"} An affine map $T\in\operatorname{Aff}(\mathbb A^2_E)$ is a *good coordinate map* if $G$ and $G^{-1}$ have coefficients in $O$, both coefficient reductions have degree $d$, and their degree-$d$ homogenizations have disjoint indeterminacy sets in $\mathbb P^2_{\overline{\kappa_v}}$. A global good coordinate map is a $T\in\operatorname{Aff}(\mathbb A^2_K)$ satisfying these conditions at every finite place.

The geometric condition in Definition [\[def:good\]](#def:good){reference-type="ref" reference="def:good"} is checked over the algebraic closure of the residue field. The coordinate map itself must remain over $K_v$ or $K$ as specified; extending the field is not allowed. Write $\operatorname{Aff}_2(O)=\operatorname{GL}_2(O)\ltimes O^2$, and similarly for $R$. All ideals below are nonzero fractional ideals.

[\[thm:main\]]{#thm:main label="thm:main"} For the map [\[eq:Fq\]](#eq:Fq){reference-type="eqref" reference="eq:Fq"}, the following statements hold.

1.  At a finite place $v$, good coordinates exist if and only if $$\label{eq:localconditions}
     v(a)=0,\qquad k_v=-\frac{v(b)}{d-1}\in\mathbb Z,
     \qquad Q_{s,r}(Y):=\frac{q(sY+r)-r}{s}\in O[Y]$$ for some $r\in E$, where $s\in E^\times$ is any fixed element with $v(s)=k_v$. The leading coefficient of $Q_{s,r}$ is then a unit. Set $$\label{eq:candidates}
     r_0=-\frac{q_{d-1}}{db},\qquad e_v=v(d),\qquad
     r=r_0+\frac{s}{d}\beta\quad(\beta\in B_v),$$ where $B_v$ is any full set of representatives for $O/dO$. It suffices to check the $|\kappa_v|^{e_v}$ candidates in [\[eq:candidates\]](#eq:candidates){reference-type="eqref" reference="eq:candidates"}; at most one passes modulo $sO$.

2.  If $(s,r)$ passes, define $S_{s,r}(x,y)=(sx+r,sy+r)$. The entire set of local good coordinate maps is $$\label{eq:localcoset}
     S_{s,r}\operatorname{Aff}_2(O).$$ Every such map has image lattice $(r+sO)^2$, and this disc is unique. The expression [\[eq:localcoset\]](#eq:localcoset){reference-type="eqref" reference="eq:localcoset"} is a left coset, or equivalently one orbit under right composition by the integral affine group.

3.  If all local tests pass, put $$\label{eq:scaleideal}
     I=\prod_{v\text{ finite}}\mathfrak p_v^{k_v},
     \qquad (b)I^{d-1}=R.$$ There is an $r\in K$ for which every local good disc is $r+I\mathcal O_{K_v}$. A global good coordinate map exists if and only if $$\label{eq:obstruction}
     I\oplus I\text{ is free over }R
     \quad\Longleftrightarrow\quad I^2\text{ is principal}
     \quad\Longleftrightarrow\quad [I]^2=1\text{ in }\operatorname{Cl}(R).$$ When these conditions hold, all global good coordinate maps are exactly $$\label{eq:allglobal}
     \left\{z\longmapsto Az+c:
     A R^2=I\oplus I,\quad c-(r,r)\in I\oplus I\right\}.$$ This set is one left coset of $\operatorname{Aff}_2(R)$. In every such model, both the map and its inverse have coefficients in $R$.

All tests and descriptions are independent of the choices of local scale generators, residue representatives and patched centre.

The theorem separates four exhaustive failure branches: a nonunit Jacobian, a nonintegral scale exponent, failure of every local centre candidate, and a nonprincipal ideal square after all local tests pass. There is no imposed bound on degree, ramification or the class group.

The polynomial $q$ is an algebraic device for identifying the good coordinate disc. Its iterates will occur in one uniqueness proof; they do not replace the native iterations of the Hénon map. The observable classified in this article is the set of good models, not periodic orbits or their counts.

# Why every affine good lattice is a disc square {#sec:rigidity}

Fix a finite place and suppress $v$ from the notation.

[\[lem:rigidity\]]{#lem:rigidity label="lem:rigidity"} If $T(z)=Az+c$ is good, then $a\in O^\times$ and $T=S_{s,r}B$ for some $s\in E^\times$, $r\in E$ and $B\in\operatorname{Aff}_2(O)$. Moreover, right composition of any good coordinate map by an element of $\operatorname{Aff}_2(O)$ preserves goodness.

The Jacobians of $F$ and $F^{-1}$ are $a$ and $a^{-1}$, respectively. Affine conjugation preserves their constant determinants. Integral coefficients of $G$ and $G^{-1}$ therefore imply $a,a^{-1}\in O$. This argument does not require a derivative to retain its degree after reduction.

Let $\ell_1,\ell_2$ be the nonzero row forms of $A$, and let $e_1,e_2$ be the standard column vectors. The highest homogeneous parts are $$\label{eq:topterms}
 G_d=b A^{-1}e_2\ell_2^d,\qquad
 (G^{-1})_d=(b/a)A^{-1}e_1\ell_1^d.$$ Write $\ell_i=s_i u_i$, where $s_i\in E^\times$ and $u_i$ is *primitive*: its coefficients lie in $O$ and at least one is a unit. The polynomial $u_i^d$ is still primitive in every residue characteristic. Indeed, a unit coefficient of $u_i$ gives a unit coefficient of the corresponding pure $d$th power monomial, without any use of binomial coefficients.

For $w_2=bs_2^d A^{-1}e_2$, integrality of $G_d=w_2u_2^d$ forces both components of $w_2$ to lie in $O$. Degree preservation forces at least one of them to be a unit. The same statement holds for $w_1=(b/a)s_1^d A^{-1}e_1$. Consequently the two indeterminacy sets of the reduced maps are exactly $$\label{eq:indeterminacy}
 I^+(\overline G)=\{\overline u_2=0\},\qquad
 I^-(\overline G)=\{\overline u_1=0\}
 \quad\text{on }\mathbb P^1_{\overline\kappa}.$$ To justify this description, homogenize with last coordinate $Z^d$. There is no indeterminacy in the affine chart. At least one top coordinate is nonzero, so the homogeneous coordinates have no common $Z$ factor. On $Z=0$, their simultaneous zeros are precisely the single zero of the indicated nonzero linear form.

Separation in [\[eq:indeterminacy\]](#eq:indeterminacy){reference-type="eqref" reference="eq:indeterminacy"} means that $\overline u_1$ and $\overline u_2$ are linearly independent. Thus the matrix $U$ with rows $u_1,u_2$ lies in $\operatorname{GL}_2(O)$, and $$\label{eq:rowfactor}
 A=\operatorname{diag}(s_1,s_2)U.$$ If $B\in\operatorname{Aff}_2(O)$, the model for $TB$ is $B^{-1}GB$. It and its inverse are integral. Both $B$ and its reduction extend to projective linear automorphisms, preserving degrees and separation of the indeterminacy sets. This proves the asserted invariance.

Right-composing by $U^{-1}$ now reduces $T$ to $T_1(x,y)=(sx+r,ty+w)$. The first coordinate of the forward model and the second coordinate of the inverse model are, respectively, $$\label{eq:linearterms}
 \frac ts y+\frac{w-r}{s},\qquad
 \frac st x+\frac{r-w}{t}.$$ Their integrality gives $t/s,s/t\in O$ and hence $t/s\in O^\times$. Right composition by $\operatorname{diag}(1,s/t)$ makes both scales $s$. Equation [\[eq:linearterms\]](#eq:linearterms){reference-type="eqref" reference="eq:linearterms"} also gives $(w-r)/s\in O$. An integral translation of the second new coordinate by $(r-w)/s$ then makes both centres $r$. All right-compositions made were in $\operatorname{Aff}_2(O)$, proving the factorization and the image formula $T(O^2)=(r+sO)^2$.

The two independent indeterminacy directions are essential to the proof: mere preservation of an integral lattice by a polynomial automorphism would not force the primitive row directions in [\[eq:rowfactor\]](#eq:rowfactor){reference-type="eqref" reference="eq:rowfactor"} to form an integral basis.

# A finite local test in every residue characteristic {#sec:localtest}

[\[lem:scalar\]]{#lem:scalar label="lem:scalar"} For $S_{s,r}(x,y)=(sx+r,sy+r)$, goodness is equivalent to $a\in O^\times$, $Q_{s,r}\in O[Y]$ and $bs^{d-1}\in O^\times$.

Direct substitution gives $$\begin{aligned}
 S_{s,r}^{-1}FS_{s,r}(x,y)
 &=\left(y,\frac{f(sy+r)-(a+1)r}{s}-ax\right)\notag\\
 &=\bigl(y,Q_{s,r}(y)+ay-ax\bigr),\label{eq:scalarmodel}\end{aligned}$$ whose inverse is $$\label{eq:scalarinverse}
 (x,y)\longmapsto
 \left(\frac{Q_{s,r}(x)+ax-y}{a},x\right).$$ For unit $a$, integrality in both directions is equivalent to $Q_{s,r}\in O[Y]$. Preservation of degree is equivalent to the leading coefficient $bs^{d-1}$ being a unit. Under those conditions, the top terms are $(0,bs^{d-1}y^d)$ and $((bs^{d-1}/a)x^d,0)$. Their indeterminacy points are $[1:0:0]$ and $[0:1:0]$, so regularity after reduction also holds.

The leading-coefficient condition gives the unique possible exponent $v(s)=-v(b)/(d-1)$. If that number is not an integer, no scale over $E$ can work. Scales with the same valuation differ by a unit, so one may fix any scale with the required valuation.

[\[lem:centres\]]{#lem:centres label="lem:centres"} Suppose the Jacobian and scale conditions in [\[eq:localconditions\]](#eq:localconditions){reference-type="eqref" reference="eq:localconditions"} hold. Every good centre is congruent modulo $sO$ to a candidate in [\[eq:candidates\]](#eq:candidates){reference-type="eqref" reference="eq:candidates"}. The full coefficient test for a candidate is $$\begin{aligned}
Q_{s,r}&=\frac{q(r)-r}{s},\label{eq:coefftest0}\\
 [Y^j]Q_{s,r}&=s^{j-1}\sum_{m=j}^d q_m\binom mj r^{m-j}
 \quad(1\le j\le d).\label{eq:coefftest}\end{aligned}$$

The coefficient of $Y^{d-1}$ equals $$\label{eq:subleading}
 s^{d-2}(dbr+q_{d-1})=dbs^{d-2}(r-r_0).$$ If $k=v(s)$ and $e=v(d)$, then $v(dbs^{d-2})=e-k$. Integrality of [\[eq:subleading\]](#eq:subleading){reference-type="eqref" reference="eq:subleading"} therefore forces $r\in r_0+(s/d)O$. When $d=2$, the coefficient here is $q_1=f_1-a$, not $f_1$.

For $u\in O$, let $\tau_u(Y)=Y+u$. The identity $$\label{eq:centretranslation}
 Q_{s,r+su}=\tau_u^{-1}\circ Q_{s,r}\circ\tau_u$$ shows that the integral, unit-leading-coefficient condition depends only on $r$ modulo $sO$. The quotient of $(s/d)O$ by $sO$ is isomorphic to $O/dO$, which has $|\kappa|^e$ elements. This proves exhaustiveness and the stated count. Expanding $q(sY+r)$ proves [\[eq:coefftest0\]](#eq:coefftest0){reference-type="eqref" reference="eq:coefftest0"}--[\[eq:coefftest\]](#eq:coefftest){reference-type="eqref" reference="eq:coefftest"}. Those formulas check all coefficients, not merely the subleading one; they divide by no factorial that might vanish in the residue field.

[\[lem:unique\]]{#lem:unique label="lem:unique"} All passing pairs $(s,r)$ determine the same disc $r+sO$. In particular, for fixed $s$ there is at most one passing centre class modulo $sO$.

If $Q\in O[Y]$ has degree $d\ge2$ and unit leading coefficient, then $Q(O)\subset O$. If $|y|>1$, its top term strictly dominates all lower terms, and $$\label{eq:escape}
 |Q(y)|=|y|^d,\qquad |Q^n(y)|=|y|^{d^n}\longrightarrow\infty.$$ Thus the set of elements of $E$ with bounded forward $Q$-orbit is exactly $O$. For $h(Y)=sY+r$ one has $Q_{s,r}=h^{-1}qh$, and $q^n(h(y))=h(Q_{s,r}^n(y))$. A nonzero affine map preserves whether a sequence is bounded. Hence the bounded-forward-orbit set of $q$ is exactly $r+sO$ whenever $(s,r)$ passes. That set is intrinsic to $q$, proving the first assertion. Two discs with the same scale are equal precisely when their centres differ by an element of $sO$.

Lemmas [\[lem:rigidity\]](#lem:rigidity){reference-type="ref" reference="lem:rigidity"}--[\[lem:unique\]](#lem:unique){reference-type="ref" reference="lem:unique"} prove the first two parts of Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}. Indeed, every good coordinate map reduces to a passing scalar pair, all such pairs have the same image disc, and two scalar maps with the same disc differ by an integral affine map. Right composition gives exactly the coset [\[eq:localcoset\]](#eq:localcoset){reference-type="eqref" reference="eq:localcoset"}.

#### Wild-centre check.

The candidates cannot be collapsed to $r_0$ when $v(d)>0$. For example, over $\mathbb Q_2$ let $a=1$ and $f(Y)=Y^2+Y+\tfrac14$. Then $q(Y)=Y^2+\tfrac14$, $s=1$ and $r_0=0$. The two candidate classes are $0$ and $\tfrac12$ modulo $\mathbb Z_2$. The first fails its constant coefficient, whereas $$Q_{1,1/2}(Y)=(Y+\tfrac12)^2+\tfrac14-\tfrac12=Y^2+Y$$ passes. This is a direct substitution illustrating the already proved test, not a computational search or an additional classification.

# Patching centres and the ideal-square obstruction {#sec:global}

## Only finitely many local tests are needed

First check $a\in R^\times$ and that every nonzero valuation of $b$ is divisible by $d-1$. These questions use finite factorizations of principal fractional ideals. Let $S$ be the finite set of places where $v(b)\ne0$ or $v(q_j)<0$ for at least one $j$. Outside $S$, the choice $s=1,r=0$ passes. In particular, a place dividing $d$ need not be searched merely because its residue characteristic is wild.

For $v\in S$, a scale $s_v\in K^\times$ with valuation $k_v$ can be chosen: an element of $\mathfrak p_v\setminus\mathfrak p_v^2$ has valuation one, and an integer power gives the required scale. This does not require the prime ideal to be principal. Representatives of $\mathcal O_{K_v}/d\mathcal O_{K_v}$ can be taken in $R$, using $$R/\mathfrak p_v^{e_v}\simeq
 \mathcal O_{K_v}/\mathfrak p_v^{e_v}\mathcal O_{K_v}
 =\mathcal O_{K_v}/d\mathcal O_{K_v}.$$ Consequently all tested centres $r_v=r_0+(s_v/d)\beta$ can be taken in $K$. If every place passes, set $r_v=0,s_v=1$ outside $S$. Then $I$ in [\[eq:scaleideal\]](#eq:scaleideal){reference-type="eqref" reference="eq:scaleideal"} has finite support and its prescribed valuations immediately give $(b)I^{d-1}=R$.

[\[lem:patch\]]{#lem:patch label="lem:patch"} For these local discs $r_v+I\mathcal O_{K_v}$ there exists $r\in K$ such that $r-r_v\in I\mathcal O_{K_v}$ at every finite place. The set of all such $r$ is one coset of $I$ in $K$.

Choose $0\ne D\in R$ clearing denominators so that $J=DI$ is an integral ideal and every $Dr_v$ is integral at every place. This is possible since only finitely many $r_v$ are nonzero elements of $K$. Write $n_v=v(J)\ge0$. For the finitely many places with $n_v>0$, the local residue $Dr_v$ modulo $\mathfrak p_v^{n_v}$ has a representative in $R$. The Chinese remainder theorem supplies $z\in R$ satisfying $$z\equiv Dr_v\pmod{\mathfrak p_v^{n_v}\mathcal O_{K_v}}
 \qquad(n_v>0).$$ This includes any new places introduced by clearing denominators; it is not restricted to $S$. When $n_v=0$, both terms are already integral. Thus $z-Dr_v\in J\mathcal O_{K_v}$ at every place, and $r=z/D$ has the required property. Two solutions differ by an element of $K\cap\bigcap_v I\mathcal O_{K_v}=I$, by the valuation description of a fractional ideal. Conversely every element of that coset works.

## Necessity of a principal square

Assume now that $T(z)=Az+c$ is globally good and choose $r$ as in Lemma [\[lem:patch\]](#lem:patch){reference-type="ref" reference="lem:patch"}. Local uniqueness gives $$\label{eq:localmodule}
 A\mathcal O_{K_v}^2=I\mathcal O_{K_v}\oplus I\mathcal O_{K_v},\qquad
 c-(r,r)\in I\mathcal O_{K_v}\oplus I\mathcal O_{K_v}.$$ These imply $AR^2=I\oplus I$ and $c-(r,r)\in I\oplus I$. For the first equality, one inclusion follows by localization. If $x\in I\oplus I$, then $A^{-1}x\in\mathcal O_{K_v}^2$ for every finite $v$, hence $A^{-1}x\in R^2$, giving the other inclusion. Taking second exterior powers in $\bigwedge^2K^2\simeq K$ yields $$\label{eq:detideal}
 I^2=(\det A).$$ This is the necessary determinant obstruction. In particular it does not assert that $I$ itself must be principal.

## An explicit global basis

We include the needed Dedekind-module construction to keep the sufficiency argument valid for nonprincipal ideals.

[\[lem:twogen\]]{#lem:twogen label="lem:twogen"} Every nonzero fractional ideal of $R$ has two $R$-generators.

Clear denominators and assume $I$ is integral. Choose $0\ne\alpha\in I$ and let $P$ be the finite set of prime ideals where $v(\alpha)>v(I)$. For each $\mathfrak p\in P$ choose $\beta_{\mathfrak p}\in I\setminus\mathfrak p I$. Such an element exists since the invertible ideal $I$ has one-dimensional nonzero quotient $I/\mathfrak p I$ over $R/\mathfrak p$. The module version of the Chinese remainder theorem gives $\beta\in I$ congruent to $\beta_{\mathfrak p}$ modulo $\mathfrak p I$ for all $\mathfrak p\in P$. At such primes $v(\beta)=v(I)$; at all other primes $v(\alpha)=v(I)$. Thus $(\alpha,\beta)$ and $I$ have the same valuations and are equal. If $P$ is empty, take $\beta=0$. Restoring denominators proves the fractional case.

[\[lem:basis\]]{#lem:basis label="lem:basis"} If $I^2=(\gamma)$, there is an explicit matrix $A\in\operatorname{GL}_2(K)$ with $AR^2=I\oplus I$.

Write $I=(\alpha,\beta)$ by Lemma [\[lem:twogen\]](#lem:twogen){reference-type="ref" reference="lem:twogen"}. From $II^{-1}=R$ choose $u,v\in I^{-1}$ with $\alpha u+\beta v=1$. Set $$\label{eq:basis}
 A=\begin{pmatrix}\alpha&-\gamma v\\
                    \beta&\gamma u\end{pmatrix}.$$ All entries lie in $I$ because $\gamma I^{-1}=I$, and $\det A=\gamma$. For $x,y\in I$, $$\label{eq:basisinverse}
 A^{-1}\binom xy
 =\binom{ux+vy}{(-\beta x+\alpha y)/\gamma}\in R^2.$$ The first entry is integral by $I^{-1}I=R$, and the second by $I^2=(\gamma)$. This proves both inclusions in $AR^2=I\oplus I$.

The two lemmas and [\[eq:detideal\]](#eq:detideal){reference-type="eqref" reference="eq:detideal"} prove [\[eq:obstruction\]](#eq:obstruction){reference-type="eqref" reference="eq:obstruction"}, including the equivalence with freeness. For sufficiency in the dynamical theorem, take the matrix [\[eq:basis\]](#eq:basis){reference-type="eqref" reference="eq:basis"} and $T(z)=Az+(r,r)$. At a finite place, use the previous passing pair $(s_v,r_v)$. Then $$\label{eq:localfactor}
 S_{s_v,r_v}^{-1}T(z)
 =\frac{A}{s_v}z+\frac{r-r_v}{s_v}(1,1).$$ Here $A/s_v\in\operatorname{GL}_2(\mathcal O_{K_v})$ by equality of the local lattices, and the translation is integral by Lemma [\[lem:patch\]](#lem:patch){reference-type="ref" reference="lem:patch"}. Lemma [\[lem:rigidity\]](#lem:rigidity){reference-type="ref" reference="lem:rigidity"} therefore makes $T$ good at every place. The coefficients of $T^{-1}FT$ and its inverse lie in $K\cap\bigcap_v\mathcal O_{K_v}=R$.

## All coordinate maps and choice independence

The necessity argument proved that every global map satisfies [\[eq:allglobal\]](#eq:allglobal){reference-type="eqref" reference="eq:allglobal"}. Conversely, for every $A,c$ satisfying that formula the same local factorization [\[eq:localfactor\]](#eq:localfactor){reference-type="eqref" reference="eq:localfactor"}, with $c-(r_v,r_v)$ in its translation part, is integral and invertible. Hence it gives a good model. If $T_1,T_2$ satisfy the formula, $T_1^{-1}T_2$ has linear part in $\operatorname{GL}_2(R)$ and translation in $R^2$, because it carries $R^2$ bijectively to itself. This proves the global left-coset statement.

Changing $s_v$ by a unit preserves the scale ideal; changing a passing centre within $s_v\mathcal O_{K_v}$ preserves its disc; changing the patched $r$ within $I$ preserves [\[eq:allglobal\]](#eq:allglobal){reference-type="eqref" reference="eq:allglobal"}. The ideal $I$ itself is uniquely prescribed by the valuations of $b$. If the original map is expressed in another global affine coordinate system, its unique local lattice is carried by that coordinate change; its determinant ideal changes by a principal factor. Thus the vanishing of the obstruction is also invariant under such a reexpression. This completes the proof of Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}.

#### A terminating arithmetic prescription.

For clarity, the constructive content is the following finite rule.

1.  Factor $(a)$ and $(b)$. Reject unless $a\in R^\times$ and $(d-1)\mid v(b)$ at every finite place.

2.  At each place in the finite set $S$, choose a scale of the required valuation and enumerate [\[eq:candidates\]](#eq:candidates){reference-type="eqref" reference="eq:candidates"}. Test all coefficients by [\[eq:coefftest0\]](#eq:coefftest0){reference-type="eqref" reference="eq:coefftest0"}--[\[eq:coefftest\]](#eq:coefftest){reference-type="eqref" reference="eq:coefftest"}; reject if no candidate passes.

3.  Form $I$ and patch $r$ using Lemma [\[lem:patch\]](#lem:patch){reference-type="ref" reference="lem:patch"}. Test whether $I^2$ is principal. If not, reject the global model problem.

4.  If $I^2=(\gamma)$, obtain two generators, solve $\alpha u+\beta v=1$ in $I^{-1}$ and use [\[eq:basis\]](#eq:basis){reference-type="eqref" reference="eq:basis"}. Formula [\[eq:allglobal\]](#eq:allglobal){reference-type="eqref" reference="eq:allglobal"} then describes every answer.

The prescription uses exact number-field ideal arithmetic and finite residue rings. It states no practical complexity bound and was not implemented or executed as part of this proof.

# Class-group consequences and explicit examples {#sec:examples}

If all local tests pass, a global good coordinate map of the form $S_{s,r}$ exists exactly when $I$ is principal.

Such a map forces $I=sR$ by the local scale valuations. Conversely, if $I=sR$, choose the patched centre $r$ and apply the local scalar condition at every finite place.

Thus a nonprincipal ideal of order two is precisely the kind of scale obstruction that mixed two-dimensional coordinates can repair while a common global scalar cannot.

[\[cor:classgroup\]]{#cor:classgroup label="cor:classgroup"} Fix $K$ and $d\ge2$. Every degree-$d$ single-factor Hénon map over $K$ that is locally affine-good at every finite place has a global affine good model if and only if $$\label{eq:classcriterion}
 \operatorname{Cl}(R)[d-1]\subseteq\operatorname{Cl}(R)[2],
 \qquad \operatorname{Cl}(R)[m]=\{C\in\operatorname{Cl}(R):C^m=1\}.$$

The sufficiency follows from $(b)I^{d-1}=R$ and Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}. Conversely, take any ideal class in $\operatorname{Cl}(R)[d-1]$, represent it by $I$, and choose $b\in K^\times$ with $(b)I^{d-1}=R$. Define $$\label{eq:realization}
 a=1,\qquad f(Y)=bY^d+Y,\qquad q(Y)=bY^d.$$ Locally choose $s_v\mathcal O_{K_v}=I\mathcal O_{K_v}$ and $r_v=0$. Then $Q_{s_v,0}=bs_v^{d-1}Y^d$ has unit leading coefficient, so all local tests pass and the global obstruction is exactly $[I]^2$. The stated universal local--global property therefore forces every class in $\operatorname{Cl}(R)[d-1]$ into $\operatorname{Cl}(R)[2]$.

Degrees two and three always satisfy the local--global property, although in degree three the global model may require a mixed matrix. The corollary is a criterion for the given class group, not a claim about the distribution of class groups of number fields.

## A nonprincipal two-torsion ideal repaired by mixing

Let $K=\mathbb Q(\sqrt{-5})$, put $t=\sqrt{-5}$ and $R=\mathbb Z[t]$, and set $I=(2,1+t)$. Since $R/I\simeq\mathbb F_2$, the ideal has norm two. The generators $4,2+2t,-4+2t$ of $I^2$ lie in $(2)$. After division by two, the resulting ideal contains $2,1+t,-2+t$; the latter two differ by three, so this ideal contains one. Hence $I^2=(2)$. If $I$ were principal, its integral generator would have norm two, but $N(m+nt)=m^2+5n^2=2$ has no integer solution. The ideal class has exact order two.

Consider $$\label{eq:twoexample}
 F(x,y)=\left(y,\tfrac12y^3+y-x\right).$$ It is locally good everywhere by [\[eq:realization\]](#eq:realization){reference-type="eqref" reference="eq:realization"}, and its scale ideal is $I$. No common global scalar is possible. Nevertheless the matrix $$\label{eq:explicitmatrix}
 A=\begin{pmatrix}2&1+t\\1+t&t-1\end{pmatrix},\qquad\det A=2$$ has $AR^2=I\oplus I$: its entries lie in $I$, and its inverse has entries in $I/2=I^{-1}$. The coordinate map $T(z)=Az$ is therefore globally good by [\[eq:localfactor\]](#eq:localfactor){reference-type="eqref" reference="eq:localfactor"}. This verifies every good-reduction condition, not merely the unit Jacobian. The ideal itself is a classical example; the point here is the distinction between the two allowed coordinate groups.

## A three-torsion ideal preventing every global affine model

Let $K=\mathbb Q(\sqrt{-23})$, let $\omega=(1+\sqrt{-23})/2$, and put $R=\mathbb Z[\omega]$. Then $\omega^2-\omega+6=0$. Set $$I=(2,\omega-1),\qquad J=(2,\omega),\qquad\alpha=\omega+1.$$ The polynomial of $\omega$ has two distinct linear factors modulo two, so $I,J$ are the two primes above two and both have norm two. The element $\alpha$ is zero modulo $I$ and one modulo $J$, while $N(\alpha)=8$. Thus its principal ideal has no factor above any other rational prime and none at $J$, giving $I^3=(\alpha)$. On the other hand, $$N(m+n\omega)=m^2+mn+6n^2
 =(m+n/2)^2+23n^2/4$$ cannot equal two: for $n\ne0$ it is at least $23/4$, and for $n=0$ it is a square. Therefore $I$ is nonprincipal. If $I^2$ were principal, then $I=I^3/I^2$ would be principal as well, a contradiction.

Now take $$\label{eq:threeexample}
 F(x,y)=\left(y,\frac{y^4}{\omega+1}+y-x\right).$$ Since $I^3=(\omega+1)$, [\[eq:realization\]](#eq:realization){reference-type="eqref" reference="eq:realization"} gives local good models at every finite place. The nonprincipal square $I^2$ excludes every global affine coordinate map. Mixed matrices, independent translations and wild primes are all covered by this exclusion. No calculation of the entire class group is needed.

# Scope and evidence

The classification concerns a single Hénon factor over the stated field and the complete two-dimensional affine coordinate group. It does not classify nonaffine polynomial conjugacies, birational changes of compactification, products of Hénon factors, or good models after field extension. No archimedean integrality condition is imposed. The finite prescription decides the model question; it does not compute periodic points, zeta functions, bad Euler factors or root numbers.

All mathematical conclusions in this article follow from the displayed proofs and standard ideal arithmetic over the Dedekind domain $\mathcal O_K$. There were zero mathematical program executions for this result. The explicit examples were verified by the shown algebra. The originating frozen proof package and its source comparisons received current-team internal nonauthor review before manuscript preparation. This article was prepared with AI assistance; that internal review is not human peer review or a claim of global priority. Typesetting builds are recorded separately from mathematical evidence. The source audit accompanying the manuscript identifies the accessed versions and does not certify unperformed retraction, venue or competing-interest checks.

The central distinction is structural: local regularity leaves only one disc square, but a global basis for that square requires only $I^2$ to be principal. This explains both the finite all-characteristic local test and the exact possibility of local good reduction without one global affine good model.
