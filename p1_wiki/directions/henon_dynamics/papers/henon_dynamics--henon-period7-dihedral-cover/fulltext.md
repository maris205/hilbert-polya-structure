---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-period7-dihedral-cover"
canonical_tex: "henon_dynamics/henon_period7_dihedral_cover/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_period7_dihedral_cover/paper/main.pdf"
source_sha256: "80c998923e2ed7788c4ed31c0d286685a5c822752766b34305a3501ae62a8c43"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Dihedral closure and chronology-induced real multiplication in a period-seven Hénon curve

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_period7_dihedral_cover>)
- [规范 TeX](<../../../../../henon_dynamics/henon_period7_dihedral_cover/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_period7_dihedral_cover/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_period7_dihedral_cover/README.md>)
- [BibTeX](<../../../../../henon_dynamics/henon_period7_dihedral_cover/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For a corrected period-seven coordinate curve of the area-preserving Hénon map, we identify the ordered-edge lift with the connected dihedral Galois closure. The closure has group $D_7$, genus eight, and six reflection branch values. Its rotation quotient is the genus-two discriminant curve $w^2=Q_6(\sigma)$, and the degree-seven map to that quotient is unramified; its reflection quotient is the previously obtained genus-three scalar curve. An explicit degree-six divisor gives the branch locus of the quadratic edge extension. A rational permutation-character relation yields $\operatorname{Jac}(E)\sim_\mathbb Q\operatorname{Jac}(B)\times\operatorname{Jac}(C)^2$. More importantly for chronology, the unnormalized push-pull of one Hénon time step is a Rosati-self-adjoint endomorphism of $\operatorname{Jac}(C)$ with exact minimal polynomial $T^3+T^2-2T-1$. Thus the scalar Jacobian has real multiplication by $\mathbb Q(\zeta_7+\zeta_7^{-1})$. At $p=5,11,13$, a tame-inertia, purity, and simultaneous-normalization argument proves good reduction and promotes three independently counted scalar numerators to genuine Hasse--Weil factors. They factor exactly as norms of quadratic polynomials over the real cubic field. General dihedral and real-multiplication mechanisms are classical; the new content is their exact source-locked realization on this Hénon curve. The result retains chronological characters but also proves that the ordinary oriented-cover spectrum is only the genus-two quotient plus two scalar copies. Period remains fixed at seven, so no Riemann divisor or Hilbert--Pólya operator follows.
author:
- Anonymous research note
bibliography:
- references.bib
date: 8 August 2026
title: |
  Dihedral closure and chronology-induced real multiplication\
  in a period-seven Hénon curve
```

## Markdown 正文

# Introduction

The area-preserving Hénon recurrence $$\label{eq:henon}
 x_{i+1}=a-x_i^2-x_{i-1}$$ has exact periodic-orbit algebra, time reversal, and a natural symplectic origin. These features motivate its use as a structural test bed in the foundational model of Wang [@wang2026henon]. The algebraic organization of its chiral periodic orbits was developed by Endler and Gallas [@endler2006chiral].

A preceding source audit and exact computation [@hcs19] isolated an apparent constant-placement error in a printed period-seven formula, adopted the placement selected by an exact orbit fibre, and then proved the adopted septic generically rather than trusting that fibre. If $a=\sigma^2-2\sigma$, the seven roots of the resulting $P(\sigma,x)$ form one simple Hénon cycle. The scalar normalization $C$ has genus three, but it forgets which neighbor is previous. Its ordered edges form a degree-14 cover carrying $$\tau(x,y)=(a-x^2-y,x),\qquad
 J(x,y)=(x,a-x^2-y),$$ with $\tau^7=J^2=1$ and $J\tau J=\tau^{-1}$.

The natural next question is not another scalar point count. It is whether the ordered-edge object is connected, what its compactified geometry is, and whether Hénon time produces arithmetic character sectors. We answer all three questions exactly. The answer connects the specific Hénon curve to the classical theory of dihedral covers, double-coset endomorphisms, and real multiplication developed by Ellenberg [@ellenberg2001endomorphism] and made explicit for genus-three curves by Hoffman, Liang, Sakai, and Wang [@hoffman2016genus3]. Prym varieties of the relevant unramified degree-seven covers have also been studied extensively [@lange2016prym]. We use these mechanisms; we do not claim them as new general theory.

The contributions for this Hénon specialization are:

1.  the ordered-edge curve $E$ is the connected $D_7$ splitting curve of $P$, with $g(E)=8$;

2.  the complete quotient diagram is explicit: the rotation quotient is $B:w^2=Q_6(\sigma)$ of genus two, the reflection quotient is $C$ of genus three, and $E\to B$ is unramified cyclic of degree seven;

3.  the quadratic extension $E\to C$ is $\mathbb Q(C)(\sqrt{Q_6})/\mathbb Q(C)$ and its six branch points have an exact coordinate formula;

4.  $\operatorname{Jac}(E)\sim_\mathbb Q\operatorname{Jac}(B)\times\operatorname{Jac}(C)^2$;

5.  one Hénon step induces a Rosati-self-adjoint correspondence on $\operatorname{Jac}(C)$ generating $\mathbb Q(\zeta_7+\zeta_7^{-1})$; and

6.  at $p=5,11,13$, tame vertical-inertia exclusion and a two-chart normalization comparison certify the scalar and ordered-edge local factors.

The last item is the relevant spectral structure. It explains why a degree-six scalar Frobenius polynomial should be the norm of one quadratic over a real cubic field, and the three certified rows satisfy that law exactly. It also imposes a limitation: forgetting the $\tau$ labels, the ordinary cohomology of $E$ contains only $H^1(B)$ and two copies of $H^1(C)$. Orientation refines the spectrum equivariantly but does not create new ordinary eigenvalues.

# The dihedral splitting curve {#sec:geometry}

Define $$\label{eq:q6}
\begin{split}
Q_6(\sigma)={}&64\sigma^6-448\sigma^5+848\sigma^4+80\sigma^3\\
&-1048\sigma^2+152\sigma-151.
\end{split}$$ The frozen scalar calculation gives $$\label{eq:disc}
 \operatorname{Disc}_xP=(4\sigma-9)^2Q_6(\sigma)^3,
 \qquad \operatorname{Disc}Q_6=2^{63}\cdot97.$$

[\[thm:d7\]]{#thm:d7 label="thm:d7"} Let $E$ be the smooth projective normalization of the ordered-edge correspondence of $P$. Then $E$ is geometrically connected, its function field is the splitting field of $P$ over $\mathbb Q(\sigma)$, and $$\operatorname{Gal}(\mathbb Q(E)/\mathbb Q(\sigma))\cong D_7.$$ The only branch values of $E\to\mathbb P^1_\sigma$ are the six roots of $Q_6$; their inertia groups are reflections. Moreover $$\boxed{g(E)=8}.$$

The exact neighbor theorem says that the seven geometric roots of $P$ form one Galois-invariant cycle. Geometric monodromy is transitive and embeds in the automorphism group of that cycle, hence in $D_7$. A transitive subgroup is either the rotation group $C_7$ or all of $D_7$. Equation [\[eq:disc\]](#eq:disc){reference-type="eqref" reference="eq:disc"} has nontrivial square class $[Q_6]$ even over $\overline\mathbb Q(\sigma)$, because $Q_6$ is squarefree. Thus geometric monodromy contains an odd permutation, whereas every seven-cycle is even. It follows that the group is $D_7$.

An ordered pair of adjacent coordinates determines the remaining five by Eq. [\[eq:henon\]](#eq:henon){reference-type="eqref" reference="eq:henon"}; its field therefore contains the splitting field. The opposite inclusion is immediate. The ordered-edge field has degree 14 and the rational maps $\tau,J$ generate 14 deck transformations, proving the arithmetic statement as well.

Over a root of $Q_6$, the scalar cover has cycle type $2^3 1$, which in $D_7$ is a reflection. The scalar normalization is unramified at the double discriminant value $\sigma=9/4$ and at infinity. Since the vertex action of $D_7$ is faithful, the Galois closure cannot have nontrivial inertia acting trivially on every scalar sheet. Hence there are no further branch values. A degree-14 regular cover has seven points of index two over each of the six reflection values. Riemann--Hurwitz gives $$2g(E)-2=14(-2)+6\cdot7=14,$$ and therefore $g(E)=8$.

This proof also rules out a tempting but incorrect picture in which the two orientations form disconnected degree-seven covers. Fibrewise they form two $\tau$-orbits, but reflection monodromy exchanges them globally.

[\[prop:branch\]]{#prop:branch label="prop:branch"} Let $C=E/\langle J\rangle$. Then $$\label{eq:kummer}
 \mathbb Q(E)=\mathbb Q(C)(\sqrt{Q_6(\sigma)}).$$ The map $E\to C$ has exactly six simple branch points, one over each root of $Q_6$. Modulo $Q_6$, their scalar coordinate is $$\label{eq:u}
 u(\sigma)=-\frac{
160\sigma^5-760\sigma^4+412\sigma^3+1120\sigma^2
-111\sigma+166}{4}.$$ There is no deck branching at the finite node or infinity.

The sign character of the seven-root action is trivial on rotations and nontrivial on reflections. Its quadratic field is the discriminant field, so $$\mathbb Q(E)^{\langle\tau\rangle}
 =\mathbb Q(\sigma,\sqrt{\operatorname{Disc}_xP})
 =\mathbb Q(\sigma,\sqrt{Q_6}).$$ Because $\langle J\rangle\cap\langle\tau\rangle=1$, adjoining this quadratic field to $\mathbb Q(C)$ gives all of $\mathbb Q(E)$, proving Eq. [\[eq:kummer\]](#eq:kummer){reference-type="eqref" reference="eq:kummer"}.

At a root of $Q_6$, the normalized scalar fibre has valuations $2,2,2,1$ for $Q_6$: three coordinates are simply ramified over the base and one is unramified. Only the last point branches in the Kummer extension. Exact substitution gives $$P(\sigma,u)\equiv0\pmod{Q_6}$$ and $$P_x(\sigma,u)\equiv
2(8\sigma^4-36\sigma^3+16\sigma^2+39\sigma+37)
\pmod{Q_6}.$$ The resultant of the last polynomial and $Q_6$ is $2^{42}$, proving that the displayed root is simple. At the node, $Q_6(9/4)=-7/64$. On every infinity branch, with $t=1/\sigma$, $$Q_6=t^{-6}(64-448t+\cdots),$$ so the valuation is even and the leading unit is a square. These observations exhaust the divisor of $Q_6$.

As a check, the quadratic Riemann--Hurwitz formula gives $$2g(E)-2=2(2g(C)-2)+6=2\cdot4+6=14.$$

# The sign quotient and the Jacobian {#sec:quotients}

Put $$B=E/\langle\tau\rangle.$$ The discriminant-field calculation in Proposition [\[prop:branch\]](#prop:branch){reference-type="ref" reference="prop:branch"} gives an explicit model immediately.

[\[thm:quotient\]]{#thm:quotient label="thm:quotient"} The rotation quotient is $$B:\quad w^2=Q_6(\sigma),\qquad g(B)=2.$$ The map $E\to B$ is an unramified cyclic cover of degree seven. The natural quotients fit into $$\begin{array}{ccc}
&E&\\
\swarrow^{7}&&\searrow^{2}\\
B&&C\\
&\searrow^{2}\quad\swarrow^{7}&\\[-1mm]
&\mathbb P^1_\sigma.&
\end{array}$$ Here $g(E),g(B),g(C)=(8,2,3)$; the left upper map is unramified and the right upper map has the six branch points in Proposition [\[prop:branch\]](#prop:branch){reference-type="ref" reference="prop:branch"}.

The model for $B$ follows from the unique sign quadratic subfield. A squarefree polynomial of degree six gives genus two, and its square leading coefficient gives two rational points at infinity. Every inertia group of $E\to\mathbb P^1$ is a reflection and intersects the rotation subgroup trivially. Thus no nonidentity deck transformation of $E\to B$ fixes a point, proving that this cyclic cover is unramified. The remaining assertions follow from the quotient definitions and the preceding genus calculations.

The genus pattern is the standard one for an unramified cyclic cover of a genus-two hyperelliptic curve. In this setting the Prym is a product of two copies of a genus-three Jacobian [@lange2016fibres].

[\[thm:isogeny\]]{#thm:isogeny label="thm:isogeny"} There is a $\mathbb Q$-isogeny $$\label{eq:isogeny}
 \boxed{\operatorname{Jac}(E)\sim_\mathbb Q\operatorname{Jac}(B)\times\operatorname{Jac}(C)^2.}$$ It is not asserted to be an isomorphism of principally polarized abelian varieties.

Let $G=D_7$, $N=\langle\tau\rangle$, and $H=\langle J\rangle$. The rational permutation characters obey $$\label{eq:brauer}
 \mathbb Q[G/1]\oplus2\mathbb Q[G/G]
 \cong \mathbb Q[G/N]\oplus2\mathbb Q[G/H].$$ Indeed, both sides have value 16 at the identity, 2 at a nonidentity rotation, and 2 at a reflection. The associated idempotent relation for quotient Jacobians [@kani1989idempotent] gives $$\operatorname{Jac}(E)\times\operatorname{Jac}(E/G)^2
 \sim_\mathbb Q\operatorname{Jac}(E/N)\times\operatorname{Jac}(E/H)^2.$$ Now $E/G=\mathbb P^1$, $E/N=B$, and $E/H=C$, so the genus-zero factor vanishes and Eq. [\[eq:isogeny\]](#eq:isogeny){reference-type="eqref" reference="eq:isogeny"} follows.

At every common prime of good reduction, Theorem [\[thm:isogeny\]](#thm:isogeny){reference-type="ref" reference="thm:isogeny"} implies the ordinary cohomological factorization $$\label{eq:local-product}
 L_{E,p}(T)=L_{B,p}(T)L_{C,p}(T)^2.$$ Thus the oriented cover has more phase information, but after forgetting the $D_7$ action it has no Frobenius eigenvalues beyond the sign quotient and two copies of the scalar quotient.

The same argument has a useful general form. If an odd-prime $D_\ell$ cover of $\mathbb P^1$ has six reflection branch values, then its rotation quotient has genus two, its Galois curve has genus $\ell+1$, and a reflection quotient has genus $(\ell-1)/2$. The analogue of Eq. [\[eq:isogeny\]](#eq:isogeny){reference-type="eqref" reference="eq:isogeny"} holds. This is a classical dihedral mechanism, but it is a precise fixed-period spectral collapse in the present dynamical application.

# Chronology-induced real multiplication {#sec:rm}

Let $q:E\to C$ be the reflection quotient. The two maps $$E\overset{q}{\longrightarrow}C,
 \qquad
 E\overset{q\circ\tau^{-1}}{\longrightarrow}C$$ define a degree-$(2,2)$ correspondence on $C$. Its unnormalized push-pull on the Jacobian is $$\label{eq:A}
 A=q_*\tau^*q^*.$$ The word "unnormalized" is important: the idempotent $e_J=(1+J)/2$ gives $e_J\tau e_J=A/2$ on scalar cohomology and therefore a rescaled polynomial.

[\[thm:rm\]]{#thm:rm label="thm:rm"} The endomorphism $A$ is Rosati self-adjoint and has exact minimal polynomial $$\label{eq:minpoly}
 m(X)=X^3+X^2-2X-1.$$ Consequently $$\boxed{
 \mathbb Q(\zeta_7+\zeta_7^{-1})
 \hookrightarrow \operatorname{End}_\mathbb Q^0(\operatorname{Jac}(C)).
 }$$

Put $V=H^1(E,\mathbb Q)$ and $H=\langle J\rangle$. Pullback identifies $H^1(C,\mathbb Q)$ with $V^H$, and $q^*q_*=1+J$ on $V$. For $v\in V^H$, $$q^*A(q^*)^{-1}v
 =(1+J)\tau v
 =\tau v+\tau^{-1}v.$$ Thus $A$ is the adjacency operator $X=\tau+\tau^{-1}$ on the reflection-fixed subspace.

There is no rotation-fixed vector in $V^H$: such a vector would be fixed by all of $D_7$, whereas $V^{D_7}=H^1(E/D_7,\mathbb Q)=H^1(\mathbb P^1,\mathbb Q)=0$. Hence $1+\tau+\cdots+\tau^6=0$ on every relevant eigenspace. Pair inverse powers and use $$\tau^2+\tau^{-2}=X^2-2,
 \qquad
 \tau^3+\tau^{-3}=X^3-3X$$ to obtain $m(X)=0$.

It remains to prove that the cubic is minimal, not merely annihilating. Let $\varepsilon$ be the reflection sign representation and let $W$ be the six-dimensional rational irreducible whose complexification is the sum of the three nontrivial two-dimensional representations. Quotient genera give $$H^1(E,\mathbb Q)\cong\varepsilon^{\oplus4}\oplus W^{\oplus2}.$$ Indeed, there are no trivial summands; $C_7$-invariants have dimension $2g(B)=4$; and reflection invariants have dimension $2g(C)=6$. On $W^H$, $X$ has all three distinct eigenvalues $$\zeta_7^k+\zeta_7^{-k},\qquad k=1,2,3,$$ each twice on $H^1(C)$. Thus the characteristic polynomial of $A$ is $m^2$ and its minimal polynomial is the irreducible cubic $m$, whose discriminant is 49.

Finally, the Rosati adjoint of Eq. [\[eq:A\]](#eq:A){reference-type="eqref" reference="eq:A"} is $q_*(\tau^{-1})^*q^*$. Since $\tau^{-1}=J\tau J$ and $q\circ J=q$, this is again $A$. The generated field is totally real and fixed pointwise by Rosati, proving the stated real multiplication.

This is precisely the double-coset mechanism of Ellenberg [@ellenberg2001endomorphism]; genus-three realizations with the same cubic were constructed explicitly in [@hoffman2016genus3]. The theorem identifies the Hénon time step as the generator for the present curve. We do not prove that this cubic field is the entire endomorphism algebra or that $\operatorname{Jac}(C)$ is absolutely simple.

The complex $\tau$-character dimensions follow at once: $$\dim H^1(E)_{k=0}=4,
 \qquad
 \dim H^1(E)_{k}=2\quad(1\le k\le6),$$ and reversal pairs $k$ with $-k$. These dimensions are group-forced; the arithmetic content lies in the rank-two Frobenius action inside each paired sector.

# Selected-prime good reduction and arithmetic factors {#sec:arithmetic}

The plane model used for point counting is singular even in characteristic zero, so good reduction cannot be inferred from a reciprocal polynomial. Here we close that logical gap at exactly the three frozen primes.

[\[thm:good\]]{#thm:good label="thm:good"} For $p\in\{5,11,13\}$, the curves $B,E,C$ have smooth proper models over $\mathbb Z_p$. If $\mathcal X$ is the integral projective plane closure of $P(\sigma,x)=0$, the model $\mathcal C$ of $C$ is its total-space normalization, and $$\mathcal C_{\mathbb F_p}=\operatorname{Norm}(\mathcal X_{\mathbb F_p}).$$ For every $r\geq1$, $$\label{eq:count-correction}
 \#\mathcal C(\mathbb F_{p^r})=A_{p,r}+7+\epsilon_{p,r},
 \qquad
 \epsilon_{p,r}=\begin{cases}
 +1,&-7\text{ is a square in }\mathbb F_{p^r},\\
 -1,&-7\text{ is a nonsquare},
 \end{cases}$$ where $A_{p,r}$ is the affine count of $P=0$.

The two hyperelliptic charts $$w^2=Q_6(\sigma),\qquad
 v^2=t^6Q_6(1/t),\quad (t,v)=(\sigma^{-1},w/\sigma^3),$$ give a smooth proper model $\mathcal B/\mathbb Z_p$: the discriminant $2^{63}\cdot97$ is a unit and the two infinity points are $v=\pm8$. Its special fibre is geometrically integral, so the algebraic constant field of $\mathbb F_p(\mathcal B_{\mathbb F_p})$ is $\mathbb F_p$.

Normalize $\mathcal B$ in $\mathbb Q_p(E)$. Horizontally, $E\to B$ is an unramified $C_7$-cover. At the vertical generic DVR, nontrivial inertia would be all of $C_7$. Since $p\ne7$, this would be a totally tamely ramified cyclic extension of degree seven with residue degree one, forcing $\mu_7\subset\mathbb F_p(\mathcal B_{\mathbb F_p})$. The constant-field statement would then force $7\mid p-1$, false for all three primes. Thus every codimension-one inertia group is trivial. Finiteness of normalization and purity of the branch locus [@stacks-purity] give a finite étale degree-seven cover $\mathcal E\to\mathcal B$. It is smooth proper, and its special fibre is geometrically connected because geometric connected-component number is locally constant in a proper smooth family.

The reflection $J$ induces $w\mapsto-w$ on $\mathcal B$ and extends to the integral closure $\mathcal E$. The quotient $\mathcal C=\mathcal E/\langle J\rangle$ is smooth: away from fixed points this is étale local, while at a geometric fixed point, since $2$ is a unit, a formal parameter has $J(z)=-z$ and the invariant ring is $\mathbb Z_p^{\rm sh}[[z^2]]$. Hence $C$ has good reduction.

On the affine chart, $P$ is monic in $x$, so the integral closure of $\mathbb Z_p[\sigma,x]/(P)$ in $\mathbb Q_p(C)$ equals the integral closure of $\mathbb Z_p[\sigma]$. On the infinity chart the same statement holds for the monic polynomial $$t^7P(1/t,y/t),\qquad (t,y)=(\sigma^{-1},x/\sigma).$$ These charts cover because $P^h(S,X,0)=(X-S)^4(X+S)^3$. Thus $\mathcal C$ is the total-space normalization of $\mathcal X$.

For $(p,\sigma_0)=(5,0),(11,0),(13,1)$, respectively, the specializations are the irreducible polynomials $$\begin{split}
&x^7-x^4+x^3-2x^2+2x-2,\\
&x^7+4x^4+x^3-2x^2+2x+3,\\
&x^7-x^6+5x^5-x^4-3x^3-5x+1.
\end{split}$$ Monicity and Gauss's lemma therefore make $P\bmod p$ irreducible over $\mathbb F_p(\sigma)$. The plane special fibre is integral of degree seven over $\mathbb P^1$, while $\mathcal C_{\mathbb F_p}\to\mathbb P^1$ also has degree seven. Their finite comparison map has degree one and is the normalization. Geometric integrality of the plane model is neither assumed nor needed.

Finally, the affine singular screen leaves only the rational point $(\sigma,x)=(9/4,1/4)$. Its residual $\gcd(P,P_x)$ is, for the three primes, $x+1,x-3,x+3$, respectively, and its tangent discriminant is $-7\ne0$. It is an ordinary node and contributes the correction $\epsilon_{p,r}$. The exact infinity blowups separate four branches above $x/\sigma=1$ and three above $x/\sigma=-1$; all seven labels remain rational and distinct at the selected primes. This contributes seven points and proves Eq. [\[eq:count-correction\]](#eq:count-correction){reference-type="eqref" reference="eq:count-correction"}.

The independent counts for $r=1,2,3$ are $$\label{eq:c-counts}
\begin{array}{c|c|l}
p&(N_1,N_2,N_3)&L_{C,p}(T)\\ \hline
5&(9,39,147)&
1+3T+11T^2+31T^3+55T^4+75T^5+125T^6\\
11&(19,167,1171)&
1+7T+47T^2+161T^3+517T^4+847T^5+1331T^6\\
13&(16,242,2131)&
1+2T+38T^2+51T^3+494T^4+338T^5+2197T^6.
\end{array}$$ The genus-three functional equation determines the remaining coefficients from these three counts.

Now put $$F=\mathbb Q(\theta),\qquad \theta^3+\theta^2-2\theta-1=0.$$ This is the maximal real subfield of $\mathbb Q(\zeta_7)$. Exact reduction in $\mathbb Z[\theta]$ proves $$\label{eq:norm-law}
 L_{C,p}(T)=\operatorname{Norm}_{F/\mathbb Q}(1-a_pT+pT^2),$$ with $$a_5=-4+\theta+2\theta^2,\qquad
 a_{11}=-4+\theta^2,\qquad
 a_{13}=-2+\theta+\theta^2.$$ Thus the real-multiplication prediction is not merely shape-compatible: it recovers the certified local numerators exactly.

The sign quotient supplies the independent genus-two factors $$\label{eq:b-factors}
\begin{array}{c|c|l}
p&(N_1,N_2)&L_{B,p}(T)\\ \hline
5&(8,30)&1+2T+4T^2+10T^3+25T^4\\
11&(14,120)&1+2T+T^2+22T^3+121T^4\\
13&(10,178)&1-4T+12T^2-52T^3+169T^4.
\end{array}$$ At these proved-good primes the isogeny in Theorem [\[thm:isogeny\]](#thm:isogeny){reference-type="ref" reference="thm:isogeny"} now gives the genuine oriented-cover identity $$\label{eq:e-factor}
 \boxed{L_{E,p}(T)=L_{B,p}(T)L_{C,p}(T)^2.}$$ It is reciprocal of degree 16, as required by $g(E)=8$. No good-reduction claim is made for primes outside the displayed set.

# Route-A evaluation and the fixed-period boundary {#sec:route}

The dihedral closure supplies the strongest arithmetic structure yet found in this Hénon line: an exact time action, a self-adjoint algebraic correspondence, a totally real endomorphism field, and character-compatible Frobenius factorization. It also makes the remaining obstruction sharper.

#### A1: weak.

The primitive object at period seven is exact. The 14 ordered states, their two orientations, the six nontrivial time characters, and reversal pairing are all retained. But $n=7$ is fixed. There is no enumeration over varying primitive periods, stability-multiplier ledger, or prime-like repetition clock.

#### A2: fail.

The norm law is a fixed-period cohomological factorization, not a weighted dynamical or Fredholm determinant. No trace-class kernel or cross-period primitive product is defined. Ordinary cohomology moreover satisfies the collapse $H^1(E)\simeq H^1(B)\oplus H^1(C)^{\oplus2}$ up to isogeny.

#### A3: fail.

There is no map to the Riemann divisor, global Hénon Euler product, gamma factor, continuation theorem, functional equation of the required type, or Riemann--von Mangoldt counting law.

#### A4: formal hint.

The source-derived operator $A$ is Rosati self-adjoint and generates a totally real cubic field. This is genuine rather than cosmetic operator structure, but it acts on the finite-dimensional Jacobian of one fixed-period curve. No Hilbert space completion, unbounded operator domain, quantization, or spectral identification with Riemann zeros exists.

Thus the formal tuple remains $$\boxed{(\mathrm{A1\_WEAK},\mathrm{A2\_FAIL},
 \mathrm{A3\_FAIL},\mathrm{A4\_FORMAL\_HINT})}$$ with overall status `ROUTE_A_EXPLORATORY`. Route B is not invoked.

The correct next breadth-first experiment changes the period rather than refining this scalar quotient again. For the full Hénon automorphism $$F_a(x,y)=(a-x^2-y,x),$$ one should construct the marked primitive schemes $$\mathcal M_n^{\rm prim}=\operatorname{Fix}(F_a^n)^{\rm prim},
 \qquad n=1,2,\ldots,$$ and preserve the two axes $$\#\operatorname{Fix}(\operatorname{Frob}_p^r\circ F_a^n)$$ without identifying Frobenius degree $r$ with Hénon period $n$. Only after an intrinsic primitive/repetition law is proved should a two-variable Lefschetz or dynamical determinant be attempted.

# Conclusion

The ordered-edge lift of the adopted period-seven Hénon septic is not a formal doubling and not two disconnected orientations. It is the connected genus-eight $D_7$ splitting curve. Its sign quotient is the explicit genus-two discriminant curve, its scalar quotient has genus three, and its cyclic degree-seven map to the sign quotient is unramified. The six branch points of the scalar double cover are explicit.

Hénon time survives quotienting as a symmetric push-pull correspondence. That correspondence has the exact cubic expected from a seven-cycle and proves real multiplication of the scalar Jacobian. At $p=5,11,13$, a selected-prime good-reduction theorem identifies the plane branch corrections with the smooth quotient counts. The resulting genuine scalar local polynomials satisfy the real-cubic norm law exactly, and the genus-eight local factors split as $L_B L_C^2$.

This is a positive arithmetic-dynamics result and a negative ordinary-spectrum result at the same time. Orientation supplies canonical character labels, but the unlabelled genus-eight spectrum is only the sign quotient plus two scalar copies. The construction remains locked to period seven. A viable Hilbert--Pólya search must now cross periods and prove a primitive repetition law; further fixed-period scalar tuning would add detail without crossing the main logical gap.

# Reproducibility ledger {#app:reproduce}

The frozen input polynomial is $$\begin{aligned}
P(\sigma,x)={}&x^7-\sigma x^6+(-3\sigma^2+8\sigma)x^5
 +(3\sigma^3-8\sigma^2+4)x^4\\
&+(3\sigma^4-16\sigma^3+20\sigma^2+2\sigma+1)x^3\\
&+(-3\sigma^5+16\sigma^4-20\sigma^3-10\sigma^2+19\sigma-2)x^2\\
&+(-\sigma^6+8\sigma^5-20\sigma^4+14\sigma^3+3\sigma^2+2\sigma+2)x\\
&+\sigma^7-8\sigma^6+20\sigma^5-10\sigma^4-23\sigma^3
 +24\sigma^2-6\sigma+3.\end{aligned}$$ This is algebraically identical to the expanded certificate input.

From the project directory, run

    python code/c20_producer.py --output results/c20_certificate.json
    python code/c20_independent_check.py \
      --certificate results/c20_certificate.json \
      --output results/c20_independent_check.json
    python -m unittest discover -s code -p 'test_c20.py' -v

The producer certifies the discriminant and branch inputs, quotient/genus ledger, $D_7$ character identities, and real-cubic norm identities. At the three selected primes it also records the vertical-inertia and purity hypotheses, irreducible specialization witnesses, residual-node gcds, and seven separated infinity branches. It directly counts the plane septic over $\mathbb F_{p^r}$ for $r=1,2,3$, applies the proved normalization correction, and reconstructs $L_{C,p}$ by Newton identities.

The checker imports neither the producer nor any HCS-C19 code or artifact. It validates source hashes and schema before independently repeating the symbolic, finite-field, normalization, and local-factor calculations. Stored finite-prime rows use no Riemann zeros, prime targets, fitted scales, or averaged chronological matrices.

The theorem depends on the exact HCS-C19 generic-neighbor certificate. The source-correction caveat remains inherited: the adopted septic is one proved generic period-seven Hénon component, but exhaustion of the full saturated period-seven scheme and a publisher-issued erratum are not claimed.
