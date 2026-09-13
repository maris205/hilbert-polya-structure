---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-mu3-yukawa-line-field"
canonical_tex: "henon_dynamics/henon_mu3_yukawa_line_field/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_mu3_yukawa_line_field/paper/main.pdf"
source_sha256: "b955a144aa39da473f62c289aa1b2b10881d2bef72d203218e33e115e67d8232"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The Twenty-Seven-Line Field of the Fourth Hénon Yukawa Surface

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_mu3_yukawa_line_field>)
- [规范 TeX](<../../../../../henon_dynamics/henon_mu3_yukawa_line_field/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_mu3_yukawa_line_field/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_mu3_yukawa_line_field/README.md>)
- [BibTeX](<../../../../../henon_dynamics/henon_mu3_yukawa_line_field/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We determine the arithmetic of the $27$-line scheme of a specific smooth cubic surface over $\mathbf Q$, namely the surface cut out by the four-variable Yukawa cubic associated with the fourth Hénon core. An exact Grassmannian calculation produces a degree-$27$ eliminant and a quotient with standard monomial counts $(1,4,10,12,0)$. Direct back-substitution, followed by a scheme-theoretic open-and-closed argument, identifies the complete Fano scheme with $\mathop{\mathrm{Spec}}(E)$ for a degree-$27$ number field $E$. Four complete squarefree factorizations modulo $7,19,29,37$ have degree patterns $$(3,3,3,3,3,6,6),\quad(1,4,4,6,12),\quad
  (1,2,8,8,8),\quad(2,5,5,5,10).$$ Their factor-degree subset sums intersect only in $\{0,27\}$, proving that the eliminant is irreducible. The last Frobenius type, combined with an exact enumeration of the $51840$-element Weyl group, excludes its index-two Coxeter-even subgroup and gives $\mathop{\mathrm{Gal}}(K/\mathbf Q)\cong W(E_6)$ for the normal closure $K$ of $E$. Consequently the geometric and arithmetic Picard ranks are $7$ and $1$. No line is defined over $\mathbf Q$; more generally, every finite extension $L/\mathbf Q$ over which a line is defined has degree divisible by $27$. The result concerns lines and Picard ranks only: it makes no assertion about rational points, rationality, Brauer--Manin obstructions, motives, or Calabi--Yau realizations.
author:
- 'Hilbert--Pólya Dynamical Structure Exploration Project'
bibliography:
- references.bib
date: August 2026
title: |
  The Twenty-Seven-Line Field\
  of the Fourth Hénon Yukawa Surface
```

## Markdown 正文

# Introduction {#sec:introduction}

A smooth cubic surface has $27$ geometric lines, but the base field need not see any of them individually. Their Galois action can split into several orbits, and even a transitive action need not be the full incidence group $W(E_6)$. For a fixed surface, determining the line field therefore requires more than smoothness or the classical line count.

This paper carries out that determination for the exact cubic surface $Y/\mathbf Q$ displayed in [\[eq:cubic\]](#eq:cubic){reference-type="ref" reference="eq:cubic"}. The equation arose as a four-variable Yukawa cubic in the preceding Hénon-core construction, but the present problem is independent of the Hodge-theoretic origin. Its object is the finite scheme $$F_1(Y)\subset\mathop{\mathrm{Gr}}(2,4),$$ and its central questions are arithmetic: is this scheme connected, what is the normal field of its geometric points, and what does the resulting action fix in the Picard lattice?

Three points make the calculation delicate. First, a zero-dimensional calculation on one Grassmann chart does not automatically recover the global Fano scheme. We close that gap by first proving that $F_1(Y)$ is finite $\mathrm{\acute{e}tale}$ of rank $27$; an open chart is then open-and-closed, and a rank-$27$ closed subscheme must be the whole line scheme. Second, a transitive subgroup containing an element of order five may still be the index-two simple subgroup $U\subset W(E_6)$. The required parity is the determinant in the $E_6$ reflection representation, not ordinary permutation sign: every element of $W(E_6)$ acts evenly on the $27$ lines. Third, the degree-$27$ residue field of one line is not the common normal line field. We denote the former by $E$ and its normal closure by $K$ throughout.

The main result is as follows.

[\[thm:main\]]{#thm:main label="thm:main"} For the cubic surface $Y/\mathbf Q$ in [\[eq:cubic\]](#eq:cubic){reference-type="ref" reference="eq:cubic"}, there is an irreducible polynomial $g\in\mathbf Z[d]$ of degree $27$ such that $$F_1(Y)\cong\mathop{\mathrm{Spec}}(E),\qquad E=\mathbf Q[d]/(g).$$ Thus $F_1(Y)$ is connected and finite $\mathrm{\acute{e}tale}$ of rank $27$. If $K$ is the splitting field of $g$, then $$\mathop{\mathrm{Gal}}(K/\mathbf Q)\cong W(E_6),\qquad [K:\mathbf Q]=51840.$$ Moreover, $$\rho(Y_{\overline{\mathbf Q}})=7,\qquad \rho(Y/\mathbf Q)=1.$$ If a finite extension $L/\mathbf Q$ defines a line on $Y$, then $$27\mid[L:\mathbf Q].$$ In particular, $Y$ has no $\mathbf Q$-rational line.

The proof combines written geometry and group theory with finite exact calculations. Its four principal contributions are:

1.  We reconstruct the complete line scheme from one exact Grassmann chart. The degree-order quotient has dimension $27$ and Hilbert counts $(1,4,10,12,0)$; a four-polynomial lexicographic shape gives a degree-$27$ eliminant and three linear back-substitutions. All four original line equations reduce to zero.

2.  We prove irreducibility by complete modular data rather than a black-box rational factorization. The factor-degree subset-sum intersections shrink through $$\{0,3,6,\ldots,27\},\quad
    \{0,6,9,12,15,18,21,27\},\quad
    \{0,9,18,27\},\quad
    \{0,27\}.$$

3.  We prove maximal Galois action. The prime $37$ gives cycle type $(2,5,5,5,10)$. Exact enumeration finds $5184$ elements of this type in $W(E_6)$, all outside the Coxeter-even subgroup $U$, and none inside it. Together with the transitive order-five criterion of Elsenhans--Jahnel, this forces the full Weyl group [@ElsenhansJahnel2009].

4.  We reconstruct the Picard reflection model and find a one-dimensional fixed space. Hochschild--Serre is used only after tensoring with $\mathbf Q$, so the conclusion is equality of ranks rather than an unqualified integral equality of Picard groups.

The arithmetic conclusion about lines is intentionally narrow. A surface without a rational line may still have rational points, and nothing here decides rationality, stable rationality, the Hasse principle, or a Brauer--Manin obstruction. The Yukawa origin supplies the distinguished equation but does not turn the line-field computation into a motivic or Calabi--Yau realization theorem.

The rest of the paper is organized as follows. fixes the surface and establishes the global finite $\mathrm{\acute{e}tale}$ line scheme. gives the chart presentation and the open-and-closed bridge. proves that the degree-$27$ algebra is a field. determines its normal closure, and [6](#sec:picard-lines){reference-type="ref" reference="sec:picard-lines"} derives the Picard and line-definition consequences. Exact replay and scope are recorded in [\[sec:exact-replay,sec:context-scope\]](#sec:exact-replay,sec:context-scope){reference-type="ref" reference="sec:exact-replay,sec:context-scope"}; the appendices contain source locators and the compact exact data.

# The fixed surface and its Fano scheme {#sec:surface-fano}

## The cubic

In homogeneous coordinates $u_0,u_1,u_2,u_3$, let $$\begin{aligned}
F={}&75081586157u_0^3-28576620789u_0^2u_1
-122000922135u_0^2u_2-5364921951u_0^2u_3\nonumber\\
&+164150208636u_0u_1^2-415458334296u_0u_1u_2
+151070718312u_0u_1u_3\nonumber\\
&+1158143874300u_0u_2^2+114691988016u_0u_2u_3
+113572676646u_0u_3^2\nonumber\\
&+6898957820u_1^3+1132596902196u_1^2u_2
-30413540316u_1^2u_3\nonumber\\
&-2054867641020u_1u_2^2+151980984216u_1u_2u_3
+36794420832u_1u_3^2\nonumber\\
&+2646295985484u_2^3+560186573940u_2^2u_3
+706181383584u_2u_3^2+1884468968u_3^3,
\label{eq:cubic}\end{aligned}$$ and set $Y=V(F)\subset\mathbf P^3_{\mathbf Q}$. The coefficient content is one and the first coefficient is positive, which fixes the common-scalar convention. The current exact replay reconstructs all twenty sparse coefficient rows and verifies projective smoothness over $\mathbf Q$ by unit ideals on the four standard affine charts. It also verifies good reduction at $7,19,29,37$.

The equation is the only Hénon/Yukawa input used below. A rational coordinate transformation in $\operatorname{GL}_4(\mathbf Q)$, or multiplication of $F$ by an element of $\mathbf Q^\times$, changes its presentation but not any line-scheme or Picard conclusion; see [\[cor:projective-invariance\]](#cor:projective-invariance){reference-type="ref" reference="cor:projective-invariance"}.

## The line section

Let $\mathcal S$ be the tautological rank-two subbundle on $\mathop{\mathrm{Gr}}(2,4)$. Restriction of $F$ to a two-plane defines a section $$\sigma_F\in H^0\!\left(\mathop{\mathrm{Gr}}(2,4),
             \operatorname{Sym}^3(\mathcal S^\vee)\right),
  \qquad [S]\longmapsto F|_S .
\label{eq:line-section}$$ Its zero scheme is the Fano scheme $F_1(Y)$. This is exactly the construction in Kass--Wickelgren, Definition 41 [@KassWickelgren2021].

Two distinct external inputs control its geometric size and reducedness. The rank of the arithmetic count in Kass--Wickelgren, Theorem 2, is $15+12=27$, recovering the total geometric degree $27$ for a smooth cubic surface. Corollary 53, on the other hand, says that the zero of $\sigma_F$ corresponding to every line disjoint from the singular locus is simple. Since $Y$ is smooth, every line satisfies that condition. Corollary 54 separately records separability of the residue fields. We do not attribute the total count $27$ to Corollary 53.

[\[prop:fano-etale\]]{#prop:fano-etale label="prop:fano-etale"} The scheme $F_1(Y)$ is finite $\mathrm{\acute{e}tale}$ over $\mathbf Q$ of rank $27$.

The zero scheme of $\sigma_F$ is closed in the projective Grassmannian. Over $\overline{\mathbf Q}$, the total-degree statement gives $27$ zeros and Kass--Wickelgren Corollary 53 makes every zero simple. Thus $F_1(Y)_{\overline{\mathbf Q}}$ is a disjoint union of $27$ reduced points. Consequently $F_1(Y)$ is zero-dimensional and proper, hence finite. Geometric reducedness over the characteristic-zero field $\mathbf Q$ makes the finite scheme $\mathrm{\acute{e}tale}$, with rank $27$.

[\[rem:global-first\]]{#rem:global-first label="rem:global-first"} is proved before any affine chart is used. This order is needed in [3](#sec:chart-scheme){reference-type="ref" reference="sec:chart-scheme"}: it makes every chart open in $F_1(Y)$ also closed, preventing a hidden assumption that one chart already contains all lines.

# A degree-$27$ chart presentation {#sec:chart-scheme}

## The $U_{01}$ equations

On the standard Plücker chart $U_{01}$, write a line as the row span of $$M(a,b,c,d)=
 \begin{pmatrix}
 1&0&a&b\\
 0&1&c&d
 \end{pmatrix}.
\label{eq:chart-matrix}$$ With parameters $s,t$, its points are $$(s,t,as+ct,bs+dt).$$ Restricting [\[eq:cubic\]](#eq:cubic){reference-type="ref" reference="eq:cubic"} gives $$F(s,t,as+ct,bs+dt)
 =f_0s^3+f_1s^2t+f_2st^2+f_3t^3.
\label{eq:restricted-cubic}$$ The four sparse polynomials $f_i\in\mathbf Q[a,b,c,d]$ are printed in [11](#app:chart-data){reference-type="ref" reference="app:chart-data"}. Their common zero scheme is $F_1(Y)\cap U_{01}$.

The degree-order calculation has a $21$-element Gröbner basis. Its standard monomials have total-degree counts $$(H_0,H_1,H_2,H_3,H_{\ge4})=(1,4,10,12,0),
\label{eq:chart-hilbert}$$ so the quotient dimension is $27$. Exact FGLM conversion gives a four-element lexicographic shape $$\begin{aligned}
 g(d)&=0,\\
 \lambda_c c+h_c(d)&=0,\\
 \lambda_b b+h_b(d)&=0,\\
 \lambda_a a+h_a(d)&=0,
\end{aligned}
\qquad
\lambda_a\lambda_b\lambda_c\ne0,
\label{eq:lex-shape}$$ where $g\in\mathbf Z[d]$ is primitive of degree $27$, and each $h_\bullet$ has degree at most $26$. The complete coefficient arrays are carried by the exact electronic certificate; the compact invariants and the coefficient endpoints of $g$ are recorded in [11](#app:chart-data){reference-type="ref" reference="app:chart-data"}.

The shape computation alone is not used as an ideal-membership proof. Instead, the independent replay substitutes $$a=-\frac{h_a(d)}{\lambda_a},\qquad
 b=-\frac{h_b(d)}{\lambda_b},\qquad
 c=-\frac{h_c(d)}{\lambda_c}
\label{eq:back-substitution}$$ into each $f_i$, clears the three constant denominators, and reduces the resulting numerator modulo $g$. All four remainders are exactly zero.

## From the chart to the global scheme

Let $$A_g=\mathbf Q[d]/(g).$$ The four direct remainder identities induce a surjection $$\mathbf Q[a,b,c,d]/(f_0,f_1,f_2,f_3)
 \twoheadrightarrow A_g,
\label{eq:chart-surjection}$$ because the image contains the class of $d$. Dually, this gives a closed immersion $$Z:=\mathop{\mathrm{Spec}}(A_g)\hookrightarrow F_1(Y)\cap U_{01}.
\label{eq:chart-closed}$$

[\[lem:clopen\]]{#lem:clopen label="lem:clopen"} The immersion in [\[eq:chart-closed\]](#eq:chart-closed){reference-type="ref" reference="eq:chart-closed"} is a closed immersion into the global scheme $F_1(Y)$.

By [\[prop:fano-etale\]](#prop:fano-etale){reference-type="ref" reference="prop:fano-etale"}, $F_1(Y)$ is a finite $\mathrm{\acute{e}tale}$ scheme over a field. Its underlying space is finite and discrete, and every open subscheme is a union of connected components. Thus $F_1(Y)\cap U_{01}$ is open-and-closed in $F_1(Y)$. Composing [\[eq:chart-closed\]](#eq:chart-closed){reference-type="ref" reference="eq:chart-closed"} with this closed inclusion proves the claim.

[\[prop:complete-chart\]]{#prop:complete-chart label="prop:complete-chart"} There is an isomorphism $$F_1(Y)\cong\mathop{\mathrm{Spec}}\!\bigl(\mathbf Q[d]/(g)\bigr).$$ In particular all $27$ geometric lines lie in $U_{01}$.

The algebra $A_g$ has $\mathbf Q$-dimension $27$, because $\deg g=27$. Hence $Z$ and $F_1(Y)$ are finite schemes of the same rank. The global closed immersion from [\[lem:clopen\]](#lem:clopen){reference-type="ref" reference="lem:clopen"} corresponds to a surjective map between their $27$-dimensional coordinate algebras. It is therefore an isomorphism.

## Independent complement guard

The exact replay also generates the other five standard charts and adds the equation $p_{01}=0$, which cuts out the complement of $U_{01}$. Each resulting ideal has reduced Gröbner basis $\{1\}$:

    chart     row-coordinate convention   equation for $p_{01}=0$
  ---------- --------------------------- -------------------------
   $U_{02}$      $(s,as+ct,t,bs+dt)$               $c=0$
   $U_{03}$      $(s,as+ct,bs+dt,t)$               $c=0$
   $U_{12}$      $(as+ct,s,t,bs+dt)$               $c=0$
   $U_{13}$      $(as+ct,s,bs+dt,t)$               $c=0$
   $U_{23}$      $(as+ct,bs+dt,s,t)$             $ad-bc=0$

This calculation independently audits the chart convention. It is not used circularly to justify [\[lem:clopen\]](#lem:clopen){reference-type="ref" reference="lem:clopen"}; global equality already follows from finite $\mathrm{\acute{e}tale}$ rank comparison.

# Four-prime irreducibility {#sec:irreducibility}

identifies the full line scheme with a degree-$27$ finite $\mathbf Q$-algebra. To prove connectedness, it remains to show that $g$ is irreducible.

[\[lem:subset-sum\]]{#lem:subset-sum label="lem:subset-sum"} Let $g\in\mathbf Z[d]$ be primitive of degree $n$. Suppose that, for a prime $p$, its leading coefficient survives modulo $p$ and $$\bar g=u_p\prod_{j=1}^{r_p}q_{p,j}$$ is a squarefree factorization into distinct monic irreducibles of degrees $e_{p,1},\ldots,e_{p,r_p}$. If $g$ has a rational factor of degree $m$, then $$m\in S_p:=
 \left\{\sum_{j\in J}e_{p,j}:
 J\subseteq\{1,\ldots,r_p\}\right\}.$$

Gauss's lemma supplies a primitive integral factorization $g=vw$ with $\deg v=m$. Since the leading coefficient of $\bar g$ is nonzero, reduction preserves the degrees of both factors. Squarefreeness makes $\bar v$ a product of a subset of the distinct $q_{p,j}$, so its degree is a subset sum of their degrees.

## Complete modular witnesses

The exact factorizations are squarefree, preserve degree, and multiply back to the reduction of $g$. Their compact data are:

   $p$    leading coefficient   factorization unit  factor degrees
  ------ --------------------- -------------------- -------------------
   $7$            $2$                  $2$          $(3,3,3,3,3,6,6)$
   $19$           $8$                  $8$          $(1,4,4,6,12)$
   $29$          $26$                  $26$         $(1,2,8,8,8)$
   $37$          $29$                  $29$         $(2,5,5,5,10)$

All multiplicities are one, and in each case $\gcd(\bar g,\bar g')=1$. The monic factors themselves are listed in [12](#app:modular-data){reference-type="ref" reference="app:modular-data"}; recording only their degrees would not certify factor multiplication or squarefreeness.

The corresponding subset-sum sets are $$\begin{aligned}
S_7={}&\{0,3,6,9,12,15,18,21,24,27\},\nonumber\\
S_{19}={}&\{0,1,4,5,6,7,8,9,10,11,12,13,14,15,16,17,
18,19,20,21,22,23,26,27\},\nonumber\\
S_{29}={}&\{0,1,2,3,8,9,10,11,16,17,18,19,24,25,26,27\},\nonumber\\
S_{37}={}&\{0,2,5,7,10,12,15,17,20,22,25,27\}.
\label{eq:subset-sets}\end{aligned}$$ Their successive intersections are $$\begin{aligned}
S_7&=\{0,3,6,9,12,15,18,21,24,27\},\\
S_7\cap S_{19}&=\{0,6,9,12,15,18,21,27\},\\
S_7\cap S_{19}\cap S_{29}&=\{0,9,18,27\},\\
S_7\cap S_{19}\cap S_{29}\cap S_{37}&=\{0,27\}.
\end{aligned}
\label{eq:intersection-chain}$$

[\[prop:g-irreducible\]]{#prop:g-irreducible label="prop:g-irreducible"} The polynomial $g$ is irreducible over $\mathbf Q$. Consequently $$E:=\mathbf Q[d]/(g)$$ is a degree-$27$ number field and $$F_1(Y)\cong\mathop{\mathrm{Spec}}(E)$$ is connected and finite $\mathrm{\acute{e}tale}$.

If $g$ had a proper rational factor of degree $m$, then $1\le m\le26$. Applying [\[lem:subset-sum\]](#lem:subset-sum){reference-type="ref" reference="lem:subset-sum"} at all four primes would put $m$ in the last intersection of [\[eq:intersection-chain\]](#eq:intersection-chain){reference-type="ref" reference="eq:intersection-chain"}, which is $\{0,27\}$. This is impossible. The remaining assertions follow from [\[prop:complete-chart\]](#prop:complete-chart){reference-type="ref" reference="prop:complete-chart"}.

The proof uses the complete modular factorizations as exact identities. A rational CAS declaration that $g$ is irreducible is neither needed nor treated as an independent proof.

# The normal line field and the full Weyl group {#sec:weyl-galois}

## The two fields

Let $K$ be the splitting field of the irreducible eliminant $g$. The $27$ embeddings $E\hookrightarrow\overline{\mathbf Q}$ send the class of $d$ to the $27$ roots of $g$, hence to the $27$ geometric points of $F_1(Y)$. The rational back-substitutions in [\[eq:back-substitution\]](#eq:back-substitution){reference-type="ref" reference="eq:back-substitution"} recover $a,b,c$ from each root. Thus $K$ contains the coordinates of every line.

Conversely, a normal extension over which all $27$ lines are defined contains all of their $d$-coordinates and therefore every root of $g$. It contains $K$. Hence $K$ is the least normal common field of definition of the lines and is the normal closure of $E$.

This distinction will matter numerically: $$[E:\mathbf Q]=27,\qquad [K:\mathbf Q]=51840.$$ In particular $E\ne K$.

## Transitivity and the order-five gate

Set $$G=\mathop{\mathrm{Gal}}(K/\mathbf Q).$$ The action of $G$ on the roots is faithful by definition of a splitting field and transitive by [\[prop:g-irreducible\]](#prop:g-irreducible){reference-type="ref" reference="prop:g-irreducible"}. The intersections among the reconstructed lines are defined geometrically and are preserved by Galois. Elsenhans--Jahnel Fact 3 therefore embeds $G$ into the Weyl group $W(E_6)$ acting on the Schläfli configuration [@ElsenhansJahnel2009].

At $p=37$, the leading coefficient survives and the complete factorization is squarefree. The prime is therefore unramified in the root permutation, and the factor degrees give a Frobenius element $$\varphi\in G\subseteq W(E_6)
 \quad\text{with cycle type}\quad(2,5,5,5,10).
\label{eq:frob-type}$$ Its order is $10$, and $\varphi^2$ has order $5$. Elsenhans--Jahnel Lemma 8 applies to the transitive group $G$: it leaves exactly the alternatives $$G=U\qquad\text{or}\qquad G=W(E_6),
\label{eq:two-alternatives}$$ where $U$ is the simple index-two subgroup of order $25920$. The order-five argument alone does not choose between them.

## The parity firewall

The subgroup $U$ is the kernel of determinant on the six-dimensional $E_6$ reflection representation. Equivalently, it is the subgroup of even Coxeter word parity. This is not ordinary permutation parity on the $27$ lines. Elsenhans--Jahnel Remark 5 states that the entire image of $W(E_6)$ on those lines lies in $A_{27}$. In particular, $$\operatorname{sgn}_{S_{27}}(w)=+1
 \quad\text{for every }w\in W(E_6).
\label{eq:s27-even}$$ The target type in [\[eq:frob-type\]](#eq:frob-type){reference-type="ref" reference="eq:frob-type"} also has ordinary sign $+1$; ordinary sign cannot exclude $U$.

The exact Picard-lattice enumeration constructs $W(E_6)$ from its six simple reflections and obtains:

  quantity                              exact value
  ----------------------------------- -------------
  elements of $W(E_6)$                      $51840$
  elements of $U$                           $25920$
  orbit size on line classes                   $27$
  elements of type $(2,5,5,5,10)$            $5184$
  target-type elements in $U$                   $0$
  target-type elements outside $U$           $5184$
  elements acting oddly in $S_{27}$             $0$

Thus every element of the Frobenius type lies outside $U$. This instance computation agrees with Elsenhans--Jahnel Algorithm 10 and Remarks 11--13: the pattern $(2,5,5,5,10)$ is one of their selected outside-$U$ classes and simultaneously supplies an order-five element.

[\[thm:weyl\]]{#thm:weyl label="thm:weyl"} The common normal line field $K$ satisfies $$\mathop{\mathrm{Gal}}(K/\mathbf Q)\cong W(E_6),\qquad [K:\mathbf Q]=51840.$$ The degree-$27$ field $E$ is not Galois over $\mathbf Q$.

The Frobenius element $\varphi$ lies outside $U$, so the first alternative in [\[eq:two-alternatives\]](#eq:two-alternatives){reference-type="ref" reference="eq:two-alternatives"} is impossible. Hence $G=W(E_6)$, whose exact order is $51840$. If $E/\mathbf Q$ were Galois, its normal closure would equal $E$ and have degree $27$, contradicting the degree of $K$.

# Picard ranks and fields defining a line {#sec:picard-lines}

## The geometric Picard lattice

Over $\overline{\mathbf Q}$, a smooth cubic surface is the blow-up of $\mathbf P^2$ at six points. Write $$\mathop{\mathrm{Pic}}(Y_{\overline{\mathbf Q}})
 =\mathbf ZH\oplus\mathbf ZE_1\oplus\cdots\oplus\mathbf ZE_6,$$ with intersection form $$\operatorname{diag}(1,-1,-1,-1,-1,-1,-1).
\label{eq:intersection-form}$$ Thus $\rho(Y_{\overline{\mathbf Q}})=7$. The $27$ line classes are $$E_i,\qquad H-E_i-E_j\ (i<j),\qquad
 2H-\sum_{j\ne i}E_j .
\label{eq:line-classes}$$

The six roots $$E_1-E_2,\ E_2-E_3,\ E_3-E_4,\ E_4-E_5,\ E_5-E_6,\
 H-E_1-E_2-E_3
\label{eq:simple-roots}$$ all have self-intersection $-2$. For such a root $\alpha$, the reflection is $$s_\alpha(x)=x+(x\mathbin{\cdot}\alpha)\alpha.
\label{eq:reflection}$$ The exact replay verifies that these six maps preserve [\[eq:intersection-form\]](#eq:intersection-form){reference-type="ref" reference="eq:intersection-form"}, the $27$ classes in [\[eq:line-classes\]](#eq:line-classes){reference-type="ref" reference="eq:line-classes"}, and their full intersection matrix. They generate a group of order $51840$, act transitively on the line classes, and have determinant $-1$ on the $E_6$ root space.

The anticanonical class $$-K_Y=3H-E_1-\cdots-E_6$$ is fixed by every reflection. The six roots span its orthogonal complement. Therefore a rational Picard vector fixed by all reflections is a multiple of $-K_Y$, and $$\mathop{\mathrm{rank}}\left(
 \mathop{\mathrm{Pic}}(Y_{\overline{\mathbf Q}})\otimes\mathbf Q
 \right)^{W(E_6)}=1.
\label{eq:weyl-fixed-rank}$$ The independent matrix calculation gives the same fixed rank by stacking the six matrices $s_\alpha-I$.

## Hochschild--Serre at the rank level

By [\[thm:weyl\]](#thm:weyl){reference-type="ref" reference="thm:weyl"}, the Galois image on the geometric Picard lattice is the full group $W(E_6)$. Hence [\[eq:weyl-fixed-rank\]](#eq:weyl-fixed-rank){reference-type="ref" reference="eq:weyl-fixed-rank"} gives $$\mathop{\mathrm{rank}}\mathop{\mathrm{Pic}}(Y_{\overline{\mathbf Q}})^{G_{\mathbf Q}}=1.$$ The low-degree Hochschild--Serre sequence, together with Hilbert 90, contains $$0\longrightarrow\mathop{\mathrm{Pic}}(Y)
 \longrightarrow\mathop{\mathrm{Pic}}(Y_{\overline{\mathbf Q}})^{G_{\mathbf Q}}
 \longrightarrow\mathop{\mathrm{Br}}(\mathbf Q),
\label{eq:hs-picard}$$ as recorded, for example, in Viray, §2.1, equation (24) and the following exact sequence [@Viray2023]. Since $\mathop{\mathrm{Br}}(\mathbf Q)$ is torsion, the cokernel of the Picard injection is torsion. Tensoring [\[eq:hs-picard\]](#eq:hs-picard){reference-type="ref" reference="eq:hs-picard"} with $\mathbf Q$ therefore gives equality of ranks. Moreover, $\operatorname{Pic}^0(Y_{\overline{\mathbf Q}})=0$ because a smooth cubic surface is geometrically rational. Thus its Picard group equals its Néron--Severi group, and the common rank is the arithmetic Picard number: $$\rho(Y/\mathbf Q)
 =\mathop{\mathrm{rank}}\mathop{\mathrm{Pic}}(Y)
 =\mathop{\mathrm{rank}}\mathop{\mathrm{Pic}}(Y_{\overline{\mathbf Q}})^{G_{\mathbf Q}}
 =1.
\label{eq:arithmetic-picard}$$ We do not assert an integral equality $\mathop{\mathrm{Pic}}(Y)=\mathop{\mathrm{Pic}}(Y_{\overline{\mathbf Q}})^{G_{\mathbf Q}}$.

## Line-definition fields

[\[cor:line-fields\]]{#cor:line-fields label="cor:line-fields"} Let $L/\mathbf Q$ be finite. If $Y$ has a line defined over $L$, then $$27\mid[L:\mathbf Q].$$ In particular $Y$ has no $\mathbf Q$-rational line.

An $L$-defined line is an $L$-point of $F_1(Y)$. By [\[prop:g-irreducible\]](#prop:g-irreducible){reference-type="ref" reference="prop:g-irreducible"}, this is a $\mathbf Q$-algebra map $E\to L$. Because $E$ is a field, the map is injective. Its image is a conjugate $E'\subset L$ with $[E':\mathbf Q]=27$, and the tower law gives $$[L:\mathbf Q]=[L:E'][E':\mathbf Q]=27[L:E'].$$

[\[rem:no-rationality\]]{#rem:no-rationality label="rem:no-rationality"} concerns rational lines, not rational points. It proves neither $Y(\mathbf Q)=\varnothing$ nor any statement about rationality, stable rationality, the Hasse principle, or a Brauer--Manin obstruction.

[\[cor:projective-invariance\]]{#cor:projective-invariance label="cor:projective-invariance"} A rational projective coordinate change and multiplication of $F$ by an element of $\mathbf Q^\times$ preserve the isomorphism class of $F_1(Y)$, the fields $E$ and $K$ up to $\mathbf Q$-isomorphism, the Galois permutation representation on the $27$ lines, and both Picard ranks.

A coordinate change transports the line section [\[eq:line-section\]](#eq:line-section){reference-type="ref" reference="eq:line-section"} along the induced Grassmannian automorphism, while a common nonzero scalar leaves its zero scheme unchanged. The remaining objects and ranks are functorial consequences of that finite scheme and its incidence configuration.

# Exact replay and evidence boundary {#sec:exact-replay}

The proof separates three kinds of evidence. General theorems control the geometry of line sections and the subgroup alternatives. Exact computation supplies the large instance-specific identities. Written arguments connect those inputs to the global scheme, Galois, and Picard conclusions.

## Claim-to-evidence ledger

  Claim                                                 Exact machine input                                                               Written or external bridge
  ----------------------------------------------------- --------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------
  $F_1(Y)$ finite $\mathrm{\acute{e}tale}$, rank $27$   exact smoothness replay                                                           Kass--Wickelgren Theorem 2 gives total rank; Corollary 53 gives simple zeros
  global chart equality                                 quotient dimension $27$, lex shape, four direct zero remainders                   finite $\mathrm{\acute{e}tale}$ makes the chart open-and-closed; equal rank gives equality
  $g$ irreducible                                       four complete squarefree modular factorizations and subset sums                   Gauss's lemma and [\[lem:subset-sum\]](#lem:subset-sum){reference-type="ref" reference="lem:subset-sum"}
  $\mathop{\mathrm{Gal}}(K/\mathbf Q)=W(E_6)$           prime-$37$ factorization and exact Weyl/Coxeter enumeration                       Frobenius cycle type, Elsenhans--Jahnel Lemma 8, exclusion of $U$
  $\rho(Y/\mathbf Q)=1$                                 fixed rank $1$ for the explicit $W(E_6)$-action on the geometric Picard lattice   Hochschild--Serre torsion cokernel, followed by tensoring with $\mathbf Q$
  no $\mathbf Q$-line                                   connected degree-$27$ Fano scheme                                                 the universal property of $\mathop{\mathrm{Spec}}(E)$ and the tower law

The Picard row is a release-critical boundary. The machine calculation does *not* directly certify the arithmetic Picard rank. It certifies the rank-one fixed subspace of the geometric Picard representation. The passage to $\rho(Y/\mathbf Q)=1$ is the written Hochschild--Serre argument in [\[eq:hs-picard,eq:arithmetic-picard\]](#eq:hs-picard,eq:arithmetic-picard){reference-type="ref" reference="eq:hs-picard,eq:arithmetic-picard"}.

## Independent finite gates

The producer reconstructs the frozen twenty-term cubic, generates the six Grassmann chart systems, computes the degree-order and lexicographic bases, factors the eliminant at the four selected primes, and constructs the Weyl group from Picard reflections. It emits a strict canonical JSON payload.

The checker imports no producer module. It independently:

1.  validates the layered frozen C55 source contract before importing the cubic;

2.  rebuilds the surface and all chart equations;

3.  recomputes the standard monomial box and all four direct remainders;

4.  verifies the five complementary unit ideals;

5.  multiplies every stored modular factor, checks derivative gcds, and recomputes every subset-sum set;

6.  rebuilds the Picard lattice, the $27$ line classes, all six reflections, the $51840$-element group, Coxeter kernel, target class counts, and fixed rank;

7.  derives each terminal theorem gate from those data rather than trusting a producer conclusion string.

The schema rejects unknown or missing keys, duplicate JSON keys, floats, booleans in integer fields, noncanonical integers, oversized input, and optimized execution that would suppress assertions. The hostile suite mutates every classified scalar leaf while rebinding the exposed envelope digests; semantic leaves must still be rejected for mathematical reasons. It also exercises source drift, symlink and path attacks, stale outputs, promotion-order failures, rollback after every move, and byte/mtime nonmutation in read-only check mode.

## Official code/results prefreeze tuple

The refreshed prefreeze payload encodes the machine fixed rank and the requirement for the written Hochschild--Serre bridge as separate leaves. A fresh default replay passes all ten semantic gates. The exact code/results prefreeze tuple used by this source draft is:

  field                                         prefreeze value
  --------------------------------------------- ---------------------------------------------------------------------------------------------------------
  semantic gates                                `10/10`
  semantic rebound sweep                        `2684/2684 = 2662 payload + 20 schema + 2 envelope`
  test methods                                  `15/15`
  payload SHA-256                               `5b17c9ed7bea60680556af70297199b653d51188bb30ce59f7c2c6bfbc94f661`
  certificate SHA-256                           `26739ce5aedb4a3467645f9c1b2036d4d3eec9ce4d0dbce23d67ea7b67e5fbc4`
  canonical schema SHA-256                      `ef26d7204a38e28aaf00eed8188b31d34d590c9c8a19924f1d0798e40b052d5f`
  schema-file SHA-256                           `adab34998a944c8a4af8db774e511f0453839ea6a6e14e9437ffc259be3da504`
  independent-check SHA-256                     `4ccfb09139a4bfa812ea9c57ff8b65a6a8e603dbdb00e245355a4563386489a9`
  scoped-manifest SHA-256 and entry count       `20d29af97128e766bb5e59bf6f82f8401c6ed62f279371b031febcefd5d99b4a`; $12$ entries
  producer/checker/test direct release fields   bound by the scoped manifest; otherwise `null`
  implementation commit                         `b32402f1dd276a2684d3e849dae26150ebb595e1`
  provenance commit                             `null`; external/not separately promoted
  full-project successor                        root `FULL_PROJECT_HASHES.sha256`; self-excluding 46 entries; verified separately; digest external-only

The self-excluding scoped manifest remains the default code/results identity and default runner scope. The code/results state is `PREFREEZE_CODE_RESULTS_PASS`, while the project is `RELEASE_FROZEN` at the displayed implementation commit. The separate provenance commit remains null/external. The separately verified root successor covers the 46-entry release-wide tree without replacing that scoped identity; its digest is external-only to avoid self-reference. Temporary architecture, reconnaissance, and hostile-review digests are chronology only and are never theorem inputs.

## Computational boundary

Computer algebra certifies finite identities: coefficients, ideal membership, quotient dimensions, modular products, group enumeration, and matrix ranks. It does not supply the classical line theorem, the open-and-closed scheme argument, the subgroup theorem, the Hochschild--Serre rank bridge, or the universal property used for fields of definition. Conversely, the cited theorems do not verify the eliminant, factors, or Weyl enumeration for this surface. Both layers are needed.

A controlled bootstrap live build completed after the independent isolated source audit. It produced an (18)-page A4 PDF with zero final-pass TeX/BibTeX warnings, box warnings, unresolved references or citations, duplicate destinations, and rerun requests; all (26) fonts were embedded, subsetted Type 1 fonts. Its diagnostic predecessor identifiers were:

  ------------------------ ---------------------------------------------------------------------
  bootstrap PDF SHA-256    `241d631aad89aea4a8885fb36187b8509ce2316a51d19ef6b51a82824c478f0c`
  bootstrap log SHA-256    `9a6595a90af1bf5f8091ded907aab00721e4542cbfda9944fb20550e21e8df30`
  bootstrap text SHA-256   `037a5dd42a69b2f0219af912f96ca4629628c09306bbd0c427d189b6f4729c91`.
  ------------------------ ---------------------------------------------------------------------

These three bootstrap digests are chronology-only and are not release authority. The controlled final rebuild supersedes them; its paper-source, PDF, log, extracted-text, and compilation-report digests are recorded externally in the Route record and compilation report, rather than embedded here, to avoid a self-hash cycle.

# Context, novelty boundary, and limitations {#sec:context-scope}

#### The $27$-sheeted incidence problem.

The moduli space of smooth complex cubic surfaces has a natural incidence cover obtained by marking a line. Das studies this cover and its topology [@Das2021]. Our object is one arithmetic fibre of that general construction, presented as an explicit degree-$27$ field rather than as a family-level topological cover.

#### Arithmetic line counts.

The possible numbers of rational lines and their dependence on the base field have a long classical history. McKean gives a modern field-theoretic treatment using subgroups acting on the Schläfli graph [@McKean2021]. Here the absence of a rational line is not inferred from a classification table: it follows directly because the entire line scheme is the spectrum of one degree-$27$ field.

#### Galois computations and symmetry.

Elsenhans--Jahnel develop modular tests for Galois groups of cubic surfaces, including the transitive order-five criterion used in [5](#sec:weyl-galois){reference-type="ref" reference="sec:weyl-galois"} [@ElsenhansJahnel2009]. Recent work of Pichon-Pharabod--Telen studies monodromy groups in symmetric linear systems and finds that symmetry often forces proper subgroups of $W(E_6)$ [@PichonPharabodTelen2025]. That nearby result makes a maximality calculation essential for the present distinguished surface; symmetry or provenance cannot substitute for the outside-$U$ witness.

#### Bounded novelty statement.

On 2026-08-15 we screened exact-title and arXiv queries combining the terms Yukawa cubic surface, 27 lines, Galois, and $W(E_6)$, together with recent 2024--2026 cubic-surface neighbors. The bounded search did not locate a prior computation of the four-prime degree-$27$ line field and full Weyl closure for the exact twenty-term surface in [\[eq:cubic\]](#eq:cubic){reference-type="ref" reference="eq:cubic"}. This statement is limited by the listed query families, indexed sources, and search date. We do not claim exhaustive priority or use priority language.

## What the theorem does not decide

The result has four deliberate boundaries.

1.  A rational line is a special rational point of the Grassmannian Fano scheme. Its absence says neither that $Y(\mathbf Q)$ is empty nor that $Y$ is nonrational.

2.  The torsion target in [\[eq:hs-picard\]](#eq:hs-picard){reference-type="ref" reference="eq:hs-picard"} is used only to compare Picard ranks. We compute no Brauer class and claim no Hasse-principle or Brauer--Manin obstruction.

3.  The full line-field group is an instance result for [\[eq:cubic\]](#eq:cubic){reference-type="ref" reference="eq:cubic"}. It is not a generic theorem for Yukawa, Hénon, symmetric, or arbitrary cubic surfaces.

4.  The Hodge-theoretic origin of $F$ does not turn an agreement of line schemes, Picard ranks, or Galois groups into a motive, a polarized variation of Hodge structure, or an honest Calabi--Yau realization.

The theorem is also projective: replacing the tangent-coordinate basis by an element of $\operatorname{GL}_4(\mathbf Q)$ changes the displayed chart and eliminant but not the finite line scheme, its normal closure, or its Picard representation.

# Conclusion and declarations {#sec:conclusion}

## Conclusion

The line scheme of the fourth Hénon Yukawa cubic is one connected finite $\mathrm{\acute{e}tale}$ point of degree $27$. Its normal closure has the largest Galois group compatible with cubic-surface incidence, namely $W(E_6)$ of order $51840$. The same action leaves only the anticanonical line in the rational geometric Picard space; the Hochschild--Serre rank bridge then gives Picard ranks $7/1$. Every finite extension $L/\mathbf Q$ over which a line is defined has degree divisible by $27$.

The proof is designed so that no single computational shortcut carries a global conclusion. Direct remainders certify chart membership, finite $\mathrm{\acute{e}tale}$ geometry supplies the clopen bridge, complete modular factors prove irreducibility, Coxeter determinant excludes the index-two subgroup, and a written descent argument converts geometric fixed rank to arithmetic Picard rank. The documentation build and provenance audit bind the project `RELEASE_FROZEN` at its implementation commit while leaving the exact machine evidence at `PREFREEZE_CODE_RESULTS_PASS`; they add no new mathematical implication.

## Declarations

#### Data and code availability.

No external dataset, numerical fit, or trained parameter is used. The exact producer, independent checker, mutation suite, certificate, and compact scoped manifest are maintained in the HCS-C56 project. That 12-entry manifest remains the default code/results identity. A separate self-excluding 46-entry root successor records the release-wide tree and is verified externally; its digest is not embedded here. The current prefreeze identifiers are recorded in [7](#sec:exact-replay){reference-type="ref" reference="sec:exact-replay"}; no temporary digest is a substitute.

#### Primary-source audit.

Bibliographic metadata and theorem locators were checked against the DOI, publisher, author, and arXiv records listed in [10](#app:source-ledger){reference-type="ref" reference="app:source-ledger"}. The recent-neighbor screen is bounded rather than systematic or exhaustive.

#### Computational boundary.

Machine calculations establish finite exact algebra and adversarial certificate behavior. The clopen scheme bridge, modular subset-sum lemma, subgroup implication, Hochschild--Serre rank step, and field-degree corollary are written mathematical arguments.

#### Author contributions.

The work was carried out collaboratively: conceptualization, formal analysis, exact verification design, source control, writing, and curation.

#### Competing interests.

The authors declare no competing interests.

#### Funding.

No external funding is declared for this project.

#### Ethics.

The work uses no human participants, animal subjects, or personal data.

# Primary-source locator ledger {#app:source-ledger}

The proof uses external sources only for general statements. Every instance-specific polynomial, factorization, group count, and matrix rank is supplied by the exact C56 replay.

  source                                              exact locator                                                                        use and boundary
  --------------------------------------------------- ------------------------------------------------------------------------------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  source                                              exact locator                                                                        use and boundary
  Kass--Wickelgren [@KassWickelgren2021]              Theorem 2; §5, Definition 41; Corollary 53, p. 701; Corollary 54, p. 702             Definition 41 identifies the zero scheme of the $\operatorname{Sym}^3(\mathcal S^\vee)$ section with the line scheme. Theorem 2 has rank $27$. Corollary 53 gives simple zeros on a smooth cubic, and Corollary 54 gives separable residue fields. Corollary 53 alone is not cited for the number $27$.
  Elsenhans--Jahnel [@ElsenhansJahnel2009]            Fact 3; Remarks 4--5; Lemma 8; Algorithm 10; Remarks 11--13; author-PDF pp. 3--7     Fact 3 places the common line-field group in $W(E_6)$. Lemma 8 reduces a transitive subgroup containing order five to $U$ or $W(E_6)$. Remarks 11--13 certify the role of type $(2,5,5,5,10)$. Remark 5 says the $27$-line action lies in $A_{27}$; ordinary $S_{27}$ sign does not define $U$.
  Viray [@Viray2023]                                  §2.1, p. 10, equation (24) and the immediately following low-degree exact sequence   Supplies the Picard-to-Brauer segment of Hochschild--Serre. Since the field Brauer group is torsion, it yields rank equality after tensoring with $\mathbf Q$, not integral surjectivity and not a Brauer--Manin conclusion.
  Das [@Das2021]                                      Introduction and the incidence cover $\widetilde{\mathcal M}\to\mathcal M$           Context for the $27$-sheeted moduli cover that marks one line. It does not determine the arithmetic fibre studied here.
  Pichon-Pharabod--Telen [@PichonPharabodTelen2025]   Abstract and §1 around Theorem 2 and Table 1                                         Recent context showing that symmetric cubic-surface families often have proper monodromy subgroups. It is not an exact line-field calculation for [\[eq:cubic\]](#eq:cubic){reference-type="ref" reference="eq:cubic"}.
  McKean [@McKean2021]                                Theorems 1.1--1.2, §1.2, and Appendix A                                              Context for rational-line counts and subgroup actions on the Schläfli graph. The no-line conclusion here instead follows from $F_1(Y)=\mathop{\mathrm{Spec}}(E)$.

The Elsenhans--Jahnel chapter belongs to Progress in Mathematics volume 269; the publisher record carries copyright year 2009 and electronic publication in 2010. The bibliography uses the volume year 2009. The remaining published metadata were checked against the DOI records, and the preprint metadata against the official arXiv records, on 2026-08-15.

The recent-neighbor search used the query families listed in [8](#sec:context-scope){reference-type="ref" reference="sec:context-scope"}. No temporary download path or digest is a bibliographic or theorem authority.

# Chart equations and eliminant data {#app:chart-data}

## The four restricted equations

For the chart convention in [\[eq:chart-matrix\]](#eq:chart-matrix){reference-type="ref" reference="eq:chart-matrix"}, direct expansion gives $$\begin{aligned}
f_0={}&2646295985484a^3+560186573940a^2b+1158143874300a^2\\
&+706181383584ab^2+114691988016ab-122000922135a\\
&+1884468968b^3+113572676646b^2-5364921951b+75081586157,\\[2pt]
f_1={}&7938887956452a^2c+560186573940a^2d-2054867641020a^2\\
&+1120373147880abc+1412362767168abd+151980984216ab\\
&+2316287748600ac+114691988016ad-415458334296a\\
&+706181383584b^2c+5653406904b^2d+36794420832b^2\\
&+114691988016bc+227145353292bd+151070718312b\\
&-122000922135c-5364921951d-28576620789,\\[2pt]
f_2={}&7938887956452ac^2+1120373147880acd-4109735282040ac\\
&+706181383584ad^2+151980984216ad+1132596902196a\\
&+560186573940bc^2+1412362767168bcd+151980984216bc\\
&+5653406904bd^2+73588841664bd-30413540316b\\
&+1158143874300c^2+114691988016cd-415458334296c\\
&+113572676646d^2+151070718312d+164150208636,\\[2pt]
f_3={}&2646295985484c^3+560186573940c^2d-2054867641020c^2\\
&+706181383584cd^2+151980984216cd+1132596902196c\\
&+1884468968d^3+36794420832d^2-30413540316d+6898957820.\end{aligned}$$

## Degree-order and lexicographic summaries

The $27$ standard monomials in the degree-order quotient are $$\begin{gathered}
1;\quad d,d^2,d^3;\quad c,cd,cd^2,c^2,c^2d;\\
b,bd,bd^2,bc,bcd,bc^2,b^2,b^2d,b^2c;\\
a,ad,ad^2,ac,acd,ab,abd,a^2,a^2d.
\end{gathered}
\label{eq:standard-monomials}$$ They give the exact degree counts $(1,4,10,12,0)$. The degree-order Gröbner basis has $21$ rows, while the lexicographic shape has the four rows in [\[eq:lex-shape\]](#eq:lex-shape){reference-type="ref" reference="eq:lex-shape"}; both quotient dimensions are $27$. The independent checker reduces the original four equations and the four back-substituted numerators to zero.

## Primitive eliminant

Write $$g(d)=\sum_{i=0}^{27}g_i d^i.$$ The polynomial has content one and positive leading coefficient. The exact coefficient vector is:

    $i$ $g_i$
  ----- ------------------------------------------------------------------------------------------------------------------------
    $i$ $g_i$
      0 629260545097578647925157650368826090566763053593125389687879139376966065914503487965224614417834357220517357813760000
      1 9366270079009131419019779786422876336788058920318023693134329099887650746185243453901519542697433222020561360650240000
      2 6421765206260576247651291587263332452080068117295127373092548718032347250347259224021797092604341757295981232128000000
      3 0408650271469927335315244482396907303429777847113115044721049200473897440014624060709633385776097845568475590819840000
      4 4419065413260097407163014586033426737087926886255847447234470211881456411655007340530876271251323151671360285573120000
      5 3532521993787759082586898745484711682712345468996080950983746003303177011231225201488210891048743198806834659459072000
      6 6171734291944309627331533999602557036486004806429247115491176388244983999707946480020558142636990742037916071886848000
      7 9235902816296957809704648019986552462559139443040644921332577499053588818656195462705941543019918146002932745830400000
      8 7545851632188369520236460056165563100179695285195560055183468215116095902293582943218418032018478826994564264558592000
      9 7048867277940128448578420890155040590363880689584965907344008427905768621893181016601521275723986434887264926760960000
     10 0053702600091119414003374855350049267483933529876907846864607374920077439417717594136212163713650578304020668058828800
     11 4173062633180071049560589648386219040575383237105065662849809940522601705263330345135853744733457011706544175338291200
     12 7680395572090536837512159249626174145912654038526001775510724161697318383174498266865978864469468443584043795345408000
     13 3467152549458502145298128980818482279871469578963893973547802403207903040336363618651053454880425435604774858553548800
     14 9817216880011667733483098678268820040625421287504832971710737498474592388678424961411587655595975725978325624349798400
     15 6274497323475051294963220983412948686032906458779775817894231628828944794618937844084186401539249411491403946603550720
     16 4163688082640332580802272950135360204533665743430282065601187769111491848740989960560194411766488608566820412255278080
     17 2346549572265353574274063666923761555562750173681312786104795465497625120129893558839216762193269052253387379841049600
     18 9856484827588293653943289669418256846056759950553853722047396287717936315106929177141413980211305204291388268616675840
     19 0580631154324411551430617544677904897535942527010303565732141162598321141628122420367138574645844007801758973751468160
     20 4060418448353410266715894994407035958110599930408547112390042644445558543920386284685438145840010008278530278600489792
     21 404312868763534150585415112436068112670140711406290160899876792798418105875511842395537344101999727313243053223672608
     22 549462697104196670393147532384334003583342408236849064318706185517859610777325419277009260979341906384550981039991360
     23 752293358737855278642943710056492833078145447498563053721811177199596053680417151748718105278513864909993467518548640
     24 24478056595566980820143200116375195216045436346240962932386410473707774409190009533790761714727560223103875184399540
     25 01608779861154001502056032273822513203762122783172949799107571227211453024532912761192870274438295117740022622649634
     26 5462779354702996061739529703470402236515964956802147119332151397926754772909464298373324521537413520408849192062561
     27 3755070876956086903822785359778411467689262548788913537399544245964424834360406200467338436153217360729270457864920

The back-substitution arrays in [\[eq:lex-shape\]](#eq:lex-shape){reference-type="ref" reference="eq:lex-shape"} are substantially larger than the eliminant. They are retained without truncation in the canonical machine-readable certificate. Their mathematical use in the paper is fully replayable without trusting an FGLM label: the checker performs the four cleared substitutions into the displayed $f_i$ and recomputes zero remainders modulo the coefficient vector above.

# Complete modular factors and Weyl-lattice data {#app:modular-data}

## Complete monic factors

All coefficients below are taken in $\mathbf F_p$. In each display the listed scalar is the factorization unit and all factors occur with multiplicity one.

#### $p=7$.

$$\bar g=2\prod_{j=1}^{7}\phi_{7,j},$$ where $$\begin{aligned}
\phi_{7,1}&=d^3+5d^2+d+3,&
\phi_{7,2}&=d^3+3d^2+4d+3,\\
\phi_{7,3}&=d^3+3d^2+5d+4,&
\phi_{7,4}&=d^3+d^2+3d+5,\\
\phi_{7,5}&=d^3+5d^2+6d+5,\\
\phi_{7,6}&=d^6+3d^5+5d^4+5d+3,\\
\phi_{7,7}&=d^6+2d^5+2d^4+3d^3+5d^2+5d+6.\end{aligned}$$

#### $p=19$.

$$\bar g=8\prod_{j=1}^{5}\phi_{19,j},$$ where $$\begin{aligned}
\phi_{19,1}&=d+7,\\
\phi_{19,2}&=d^4+7d^3+12d^2+12d+11,\\
\phi_{19,3}&=d^4+14d^3+17d^2+4d+15,\\
\phi_{19,4}&=d^6+11d^5+17d^3+6d^2+7d+17,\\
\phi_{19,5}&=d^{12}+4d^{11}+4d^{10}+14d^9+6d^8+17d^7\\
&\qquad+15d^6+10d^5+14d^4+12d^3+13d^2+11d+4.\end{aligned}$$

#### $p=29$.

$$\bar g=26\prod_{j=1}^{5}\phi_{29,j},$$ where $$\begin{aligned}
\phi_{29,1}&=d+12,\\
\phi_{29,2}&=d^2+27d+3,\\
\phi_{29,3}&=d^8+5d^7+20d^6+21d^5+25d^4+22d^3+4d^2+3d+9,\\
\phi_{29,4}&=d^8+4d^7+6d^6+27d^5+3d^4+2d^3+23d^2+8d+11,\\
\phi_{29,5}&=d^8+12d^7+18d^6+16d^5+21d^4+7d^3+11d^2+6d+13.\end{aligned}$$

#### $p=37$.

$$\bar g=29\prod_{j=1}^{5}\phi_{37,j},$$ where $$\begin{aligned}
\phi_{37,1}&=d^2+28d+28,\\
\phi_{37,2}&=d^5+3d^4+17d^3+3d^2+2d+19,\\
\phi_{37,3}&=d^5+34d^4+16d^3+22d^2+34d+23,\\
\phi_{37,4}&=d^5+12d^4+30d^3+29d^2+27d+26,\\
\phi_{37,5}&=d^{10}+24d^9+23d^8+3d^7+2d^5
 +23d^4+5d^3+34d^2+30d+5.\end{aligned}$$

Direct multiplication reproduces the $28$-entry coefficient vector of $g$ modulo each prime, and every derivative gcd has degree zero. The prime-$37$ conclusion is deliberately split into four checks: smooth surface reduction; nonzero leading coefficient and squarefree eliminant; complete factor multiplication with cycle type $(2,5,5,5,10)$; and exclusion of that type from the Coxeter-even kernel.

## Picard reflection model

In the ordered basis $(H,E_1,\ldots,E_6)$, the intersection matrix is $$J=\operatorname{diag}(1,-1,-1,-1,-1,-1,-1),$$ and the anticanonical vector is $$(3,-1,-1,-1,-1,-1,-1).$$ The six simple-root rows are $$\begin{pmatrix}
0&1&-1&0&0&0&0\\
0&0&1&-1&0&0&0\\
0&0&0&1&-1&0&0\\
0&0&0&0&1&-1&0\\
0&0&0&0&0&1&-1\\
1&-1&-1&-1&0&0&0
\end{pmatrix}.$$ Each row has square $-2$, and its reflection preserves $J$, the anticanonical vector, the $27$ line classes in [\[eq:line-classes\]](#eq:line-classes){reference-type="ref" reference="eq:line-classes"}, and their intersection matrix.

The exhaustive enumeration ledger is:

  test                                                          exact result
  -------------------------------------------------- -----------------------
  reflection-group order                                             $51840$
  kernel of reflection determinant                                   $25920$
  determinants of the six simple reflections           $(-1,-1,-1,-1,-1,-1)$
  orbit of one line class                                               $27$
  target cycle type                                           $(2,5,5,5,10)$
  target-type count                                                   $5184$
  target-type count inside determinant kernel                            $0$
  target-type count outside determinant kernel                        $5184$
  ordinary $S_{27}$-odd elements in the full group                       $0$
  rank of common Picard fixed space                                      $1$

The last row is the machine input to, not the output of, the Hochschild--Serre argument. The arithmetic Picard number is derived in [6](#sec:picard-lines){reference-type="ref" reference="sec:picard-lines"}; it is not a separately machine-computed lattice rank.
