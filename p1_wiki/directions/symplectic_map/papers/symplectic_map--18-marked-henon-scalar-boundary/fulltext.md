---
p1_kind: "derived-fulltext-reading-copy"
route: "symplectic_map"
logical_paper_id: "symplectic_map--18-marked-henon-scalar-boundary"
canonical_tex: "symplectic_map/papers/18-marked-henon-scalar-boundary/paper/main.tex"
canonical_pdf: "symplectic_map/papers/18-marked-henon-scalar-boundary/paper/main.pdf"
source_sha256: "65ed1e9fb328411737646d1385c053382469a31f3e2088946a161f4d92eebb2d"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Marked Trace Coordinates and Scheme-Theoretic Ramification at the Polynomial Boundary of Generalized Hénon Maps

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symplectic_map/papers/18-marked-henon-scalar-boundary>)
- [规范 TeX](<../../../../../symplectic_map/papers/18-marked-henon-scalar-boundary/paper/main.tex>)
- [关联 PDF](<../../../../../symplectic_map/papers/18-marked-henon-scalar-boundary/paper/main.pdf>)
- [支撑 Markdown](<../../../../../symplectic_map/papers/18-marked-henon-scalar-boundary/notes/CLAIMS_EVIDENCE_MATRIX.md>)
- [BibTeX](<../../../../../symplectic_map/papers/18-marked-henon-scalar-boundary/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We prove that for every integer $d\ge 2$ and every positive period vector of length $d-1$, the map formed by $-b$ and the traces of labelled, pairwise-disjoint, simple exact cycles is dominant and generically étale on the unique marked component of the generalized Hénon family $H_{b,p}(x,y)=(p(x)+by,x)$, with $p$ monic and centered of degree $d$, that contains the polynomial boundary. The difficulty is that point markings must be divided by independent cyclic shifts, the total incidence may have several components, fixed-$b$ fibers may be reducible, and the boundary map is not an automorphism. We identify the simple scalar incidence scheme with the marked polynomial incidence, use an arbitrary-period full-rank polynomial multiplier point, and read the block differential whose first row is the $-b$ direction. At every simple scalar tuple, formal étaleness gives compatible completed local coordinates and expansions $\rho_i=\lambda_i+bG_i$. The Cartesian scalar square then gives exact base change for relative differentials and zeroth Fitting ideals: the Hénon critical scheme restricts to the polynomial multiplier critical scheme, and $J_H\bmod b=\pm J_{\mathrm{poly}}$. Nonzero determinant sections yield effective Cartier divisors when nonempty, with the empty case allowed and generic component multiplicities preserved. The result concerns selected marked traces on the normal-form cover; it makes no global reconstruction, prescribed-fiber, reducedness, or transversality assertion.
bibliography:
- references.bib
title: 'Marked Trace Coordinates and Scheme-Theoretic Ramification at the Polynomial Boundary of Generalized Hénon Maps'
```

## Markdown 正文

# Introduction {#sec:introduction}

Fix a monic centered polynomial $$p(z)=z^d+\sum_{j=0}^{d-2}a_jz^j$$ of degree $d\geq 2$, and consider the extended generalized Hénon family $$H_{b,p}(x,y)=(p(x)+by,x).$$ For $b\neq 0$ this is a polynomial automorphism with constant Jacobian $-b$. The fiber $b=0$ is different: $H_{0,p}$ is not an automorphism, but it retains the one-variable dynamics of $p$ in a form that is sufficiently rigid to control nearby marked Hénon cycles. Our question is finite and labelled. Choose exactly $d-1$ pairwise-disjoint simple cycles, give them arbitrary prescribed positive periods, and ask whether their traces, together with $-b$, provide algebraic local coordinates.

This question is not a reformulation of reconstruction from a complete spectrum. A trace attached to a labelled cycle is a regular function on a marked incidence space. Selecting $d-1$ such functions leaves the other cycles unrecorded and retains the finite normal-form symmetry. The natural conclusion is therefore dominance and generic étaleness, not injectivity. Classical generalized Hénon normal forms and their low-degree fixed-point geometry provide the ambient context [@FM89]; the selected arbitrary-period problem requires different incidence bookkeeping.

Four issues intervene before the scalar argument can be used. First, a point-marked orbit has $n$ choices of starting point, whereas a cycle-marked orbit has none. The quotient is harmless only after exact period has been imposed, because only there is the cyclic action free. Second, the full marked incidence is not assumed irreducible. One must identify the unique regular component containing the entire simple scalar locus, rather than continue one convenient scalar point. Third, an irreducible total space can have reducible closed fibers, so a statement at general fixed $b$ must be formulated for the whole fiber and then for at least one of its reduced components. Fourth, equality of critical sets would lose nilpotent and multiplicity information. The correct boundary statement uses relative Kähler differentials and zeroth Fitting ideals.

Put $r=d-1$ and let $$\mathbf n=(n_1,\ldots,n_r)\in\mathbf Z_{>0}^r.$$ The integers $n_i$ may repeat. The cycles retain their labels, are required to be pairwise disjoint, have exact respective periods $n_i$, and satisfy $$\det(DH_{b,p}^{n_i}-I)\neq 0.$$ After taking the free product of cyclic-shift quotients, let $\mathcal S_{\mathbf n}$ denote the scalar cycle-marked locus and let $\mathcal C_{\mathbf n}$ be the unique component through it. If $$\rho_i=\operatorname{tr}(DH_{b,p}^{n_i}),
  \qquad
  \Psi=(-b,\rho_1,\ldots,\rho_r),$$ then the main result has five coupled parts. The component $\mathcal C_{\mathbf n}$ is étale and dominant over the coefficient--Jacobian base and has scalar fiber exactly $\mathcal S_{\mathbf n}$. The map $\Psi$ is étale at a scalar point, hence dominant and generically étale, and the $\rho_i$ are algebraically independent over $\mathbf C(b)$. On an unspecified nonempty open subset of $\mathbf G_m$, each whole fixed-$b$ trace map is dominant and at least one component of its reduced fiber is dominant and generically étale. At every simple scalar point the completed trace germs have the form $\rho_i=\lambda_i+bG_i$. Finally, the critical Fitting scheme of $\Psi$ restricts exactly to the critical Fitting scheme of the polynomial multiplier map, including generic component multiplicities.

The polynomial input is precise and limited. Gorbovickis proves irreducibility of the relevant marked polynomial space and supplies, for every $d\geq2$ and every positive period vector with at most $d-1$ markings, a point where the selected multiplier differential has full rank [@Gor13 Definition 1.3, Remark 1.4, Lemma 1.5, Theorem 1.6, and Lemma 2.1]. We use that result only at the scalar boundary. The Hénon component, the point-to-cycle descent, the block differential, the fixed-fiber argument, the completed local statement, and the Fitting-scheme restriction are proved here.

The main contributions can be summarized as follows.

-   We construct the simple cycle-marked incidence with repeated labelled periods allowed and isolate the unique component containing the full scalar locus, without asserting irreducibility of the total incidence.

-   We prove arbitrary-period trace independence over $\mathbf C(b)$ on that component by combining the scalar multiplier differential with the transverse coordinate $-b$.

-   We identify both completed local rings at every simple scalar tuple and prove exact base change for the critical Fitting scheme, including the Cartier-or-empty and generic-multiplicity qualifications.

-   We give a fixed-$b$ conclusion that remains valid when the specialized fiber is reducible, and we identify the residual $\mu_{d-1}$ action that prevents a global reconstruction statement on the normal-form cover.

The determinant identity $$\det(DH_{b,p}^{n_i})=(-b)^{n_i}$$ is essential to the terminology. Once the determinant is known, the trace records the unordered pair of eigenvalues of the return map. No individual eigenvalue branch is selected.

Section [2](#sec:incidence){reference-type="ref" reference="sec:incidence"} constructs point- and cycle-marked incidences. Section [3](#sec:loops){reference-type="ref" reference="sec:loops"} proves the universal finite-free loop lemma and states its limitations. Section [4](#sec:scalar){reference-type="ref" reference="sec:scalar"} identifies the scalar component, states the full theorem, and proves the coordinate parts. Sections [5](#sec:completion){reference-type="ref" reference="sec:completion"} and [6](#sec:fitting){reference-type="ref" reference="sec:fitting"} establish the completed local and scheme-theoretic ramification statements. Section [7](#sec:fibers){reference-type="ref" reference="sec:fibers"} treats general nonzero fibers and residual symmetry. Section [8](#sec:comparison){reference-type="ref" reference="sec:comparison"} gives the bounded comparison, exact limitations, and conclusion. Appendix [9](#sec:appendix){reference-type="ref" reference="sec:appendix"} expands only the cyclic-index edge algebra.

# Marked incidences and exact-cycle quotients {#sec:incidence}

## The parameter base and the three open conditions

Work throughout over $\mathbf C$. Let $$\mathcal P_d^{\mathrm{cm}}
  =
  \left\{
    z^d+\sum_{j=0}^{d-2}a_jz^j
  \right\}
  \simeq\mathbf A^{d-1},
  \qquad
  \mathcal B_d=\mathbf A^1_b\times\mathcal P_d^{\mathrm{cm}}.$$ Thus $\mathcal B_d$ is smooth, irreducible, and of dimension $d$. For the fixed period vector $\mathbf n$, begin with the closed point-marked incidence $$\widetilde{\mathcal X}_{\mathbf n}
  =
  \left\{
    (b,p,z_1,\ldots,z_r)\in
    \mathcal B_d\times(\mathbf A^2)^r:
    H_{b,p}^{n_i}(z_i)=z_i\ \text{for all }i
  \right\}.$$ Here $z_i$ is a chosen point, not merely an orbit. Each equation $H^{n_i}(z_i)-z_i=0$ contributes two coordinate equations.

Three open conditions cut out the locus used below. Exactness removes, for each proper divisor $m$ of $n_i$, the closed locus $H^m(z_i)=z_i$. Pairwise orbit disjointness removes the finitely many closed loci $$H^q(z_i)=H^{q'}(z_j),
  \qquad
  i\neq j,\quad
  0\leq q<n_i,\quad 0\leq q'<n_j.$$ This formulation is unchanged when $n_i=n_j$: the labels remain distinct and the underlying cycles still must not meet. Simplicity removes the vanishing locus of $$\Delta_i=\det(D_{z_i}H_{b,p}^{n_i}-I_2).$$ We write $\widetilde{\mathcal X}_{\mathbf n}^{\circ}$ for the resulting point-marked simple exact disjoint locus.

All three deletions are made before any quotient. This order keeps their meaning labelwise. If $n_i=n_j$, exactness says separately that the orbit in slot $i$ and the orbit in slot $j$ have that common minimal period, while disjointness says that the two resulting finite orbit sets do not coincide. There is no diagonal condition identifying the slots. Moreover, on the exact locus the $n_i$ points obtained by iterating $z_i$ are pairwise distinct, so the only ambiguity attached to slot $i$ is the choice of one of those points as its start. These observations identify in advance the product of cyclic groups that may be divided out and rule out an additional symmetric-group quotient when periods repeat.

#### Proof bridge 2: the relative Jacobian criterion.

The orbit coordinates, rather than the coefficients, make the incidence regular.

[\[lem:point-etale\]]{#lem:point-etale label="lem:point-etale"} The projection $$\widetilde\pi:\widetilde{\mathcal X}_{\mathbf n}^{\circ}\longrightarrow\mathcal B_d$$ is étale. In particular, $\widetilde{\mathcal X}_{\mathbf n}^{\circ}$ is regular and has pure dimension $d$.

Different markings have disjoint orbit variables. Consequently, the Jacobian of the $2r$ periodicity equations with respect to $(z_1,\ldots,z_r)$ is block diagonal, and its $i$th block is $$D_{z_i}H_{b,p}^{n_i}-I_2.$$ Every block is invertible on $\widetilde{\mathcal X}_{\mathbf n}^{\circ}$ by the simplicity condition. The relative Jacobian criterion therefore makes $\widetilde\pi$ étale. Since $\mathcal B_d$ is smooth of dimension $d$, the same is true of the source.

More explicitly, before the three open conditions are imposed, the ambient space is smooth of relative dimension $2r$ over $\mathcal B_d$, and periodicity is given by $2r$ equations. On the locus where $\prod_i\Delta_i$ is invertible, their relative Jacobian determinant is a unit. The resulting morphism is therefore locally of finite presentation, unramified, and flat of relative dimension zero. Localizing further to exact periods and disjoint orbits preserves these properties. This also shows directly that no hidden orbit direction survives in the relative tangent space: a first-order displacement of the marked points is uniquely determined by a first-order displacement of $(b,p)$. Smoothness and the dimension assertion then follow by composition with the smooth base.

The lemma is local on the simple open. It gives no regularity statement at a multiple periodic point, and it does not make the closed full incidence $\widetilde{\mathcal X}_{\mathbf n}$ irreducible.

## From point markings to cycle markings

For each $i$, the group $\mathbf Z/n_i\mathbf Z$ acts by moving $z_i$ forward around its orbit. These actions commute, giving $$G_{\mathbf n}=\prod_{i=1}^r\mathbf Z/n_i\mathbf Z.$$ If a nonzero class in $\mathbf Z/n_i\mathbf Z$ fixed $z_i$, then $z_i$ would return before $n_i$ iterates. Exactness therefore makes the action free. Notice that freeness need not extend across a lower-period point in the closure.

#### Proof bridge 3: free cyclic descent.

[\[lem:cycle-quotient\]]{#lem:cycle-quotient label="lem:cycle-quotient"} The quotient $$\mathcal X_{\mathbf n}^{\circ}
  =
  \widetilde{\mathcal X}_{\mathbf n}^{\circ}/G_{\mathbf n}$$ is a cycle-marked scheme, the quotient map is finite étale, and the induced map $$\pi:\mathcal X_{\mathbf n}^{\circ}\longrightarrow\mathcal B_d$$ is étale. The functions $\rho_i=\operatorname{tr}(DH_{b,p}^{n_i})$ descend to $\mathcal X_{\mathbf n}^{\circ}$.

The acting group is finite and constant over $\mathbf C$, and its order is invertible. A free action of such a group on the present quasi-affine finite-type scheme has a finite étale geometric quotient. Étaleness of the map to $\mathcal B_d$ can be checked after the surjective étale quotient map, where it is Lemma [\[lem:point-etale\]](#lem:point-etale){reference-type="ref" reference="lem:point-etale"}. The return matrices at two starting points of the same cycle are conjugate whenever $b\neq0$. There is also a formula that remains valid at the scalar boundary. If the one-step derivative matrices around a cycle are $M_0,\ldots,M_{n_i-1}$, changing the starting point cyclically permutes the factors in the return product. Over any commutative test algebra, $$\operatorname{tr}(M_{n_i-1}\cdots M_0)
  =\operatorname{tr}(M_0M_{n_i-1}\cdots M_1).$$ Repeated cyclic invariance proves equality for every starting point without inverting $b$. Hence $\rho_i$ is an invariant regular function on the full simple incidence and descends uniquely through the finite quotient.

The descent is labelwise. The factor $\mathbf Z/n_i\mathbf Z$ acts only on the chosen starting point for label $i$, so the product action has trivial stabilizer even if several $n_i$ are equal: an element fixing a tuple fixes each coordinate and hence is zero in every factor. Accordingly, the quotient remembers the ordered list of cycles. It forgets neither the label order nor the requirement that their underlying orbits be disjoint.

This description can also be checked on families. Over a test scheme, an exact labelled cycle of period $n_i$ becomes, after an étale localization, an ordered orbit together with one of its $n_i$ sections as starting point. The possible starts form a torsor under $\mathbf Z/n_i\mathbf Z$, independently for every label. Taking their product recovers precisely the fibers of the quotient map. When $n_i=n_j$, exchanging the two torsors would exchange two labelled slots and is not an element of $G_{\mathbf n}$. Thus the quotient represents families of labelled cycles rather than unordered collections of equal-period cycles. Because the trace equality above holds over every test algebra, its descent is compatible with these familywise identifications, including over $b=0$ where conjugation of return matrices is unavailable.

The quotient removes exactly the starting-point copies. It does not permute two labels whose numerical periods happen to agree. Nor does it remove the diagonal root-of-unity normal-form action treated in Section [7](#sec:fibers){reference-type="ref" reference="sec:fibers"}. Since finite étale descent preserves regularity, $\mathcal X_{\mathbf n}^{\circ}$ is regular of pure dimension $d$. A noetherian regular scheme can nevertheless have several disjoint irreducible components; this distinction will select $\mathcal C_{\mathbf n}$ in Section [4](#sec:scalar){reference-type="ref" reference="sec:scalar"}.

# Universal cyclic-loop algebra and simple incidence {#sec:loops}

## The full ordered-loop algebra

Set $$R_d=\mathbf C[b,a_0,\ldots,a_{d-2}]$$ and regard $p(X)=X^d+\sum_{k=0}^{d-2}a_kX^k$ as a polynomial over $R_d$. For $n\geq1$, indices in the following definition are read in $\mathbf Z/n\mathbf Z$: $$A_n
  =
  R_d[x_0,\ldots,x_{n-1}]
  \big/
  \left(
    p(x_j)+b x_{j-1}-x_{j+1}:j\in\mathbf Z/n\mathbf Z
  \right).$$ This algebra retains all ordered $n$-loops. Exactness, disjointness, and simplicity have not yet been imposed.

#### Proof bridge 1: monic finite freeness.

[\[lem:finite-free\]]{#lem:finite-free label="lem:finite-free"} The $R_d$-algebra $A_n$ is finite free of rank $d^n$, with basis $$\mathcal B_n
  =
  \left\{
    x_0^{e_0}\cdots x_{n-1}^{e_{n-1}}:
    0\leq e_j<d
  \right\}.$$ It represents the full scheme of points fixed by $H_{b,p}^n$, with an ordered starting point. For independent markings of periods $n_1,\ldots,n_r$, the product algebra is finite free of rank $d^{n_1+\cdots+n_r}$.

Let $$F_j=p(x_j)+b x_{j-1}-x_{j+1}.$$ Choose a monomial order in the loop variables that refines their total degree, treating $R_d$ as the coefficient ring. The relation $F_j$ is monic, and its leading monomial is $x_j^d$. For distinct indices the leading monomials are relatively prime. The monic version of Buchberger's criterion works over an arbitrary commutative coefficient ring: the $S$-polynomial of $F_j$ and $F_k$ reduces to zero because the leading coefficients are units and the least common multiple of the leading monomials is their product. Thus the $F_j$ form a monic Gröbner basis.

For completeness, write $F_j=x_j^d+L_j$, where no monomial of $L_j$ is divisible by $x_j^d$. For $j\neq k$ the only critical pair has $$S(F_j,F_k)=x_k^dL_j-x_j^dL_k.$$ Reduction first replaces $x_k^d$ by $-L_k$ and $x_j^d$ by $-L_j$; the remainder is $-L_kL_j+L_jL_k=0$. This computation uses only commutativity and the unit leading coefficients. In particular, it remains valid over $R_d$ itself rather than only after passage to its fraction field.

Division by this basis reduces every polynomial to an $R_d$-linear combination of the monomials in $\mathcal B_n$. If a nonzero $R_d$-linear combination of these standard monomials lay in the defining ideal, its leading monomial would be standard. The Gröbner-basis property would also force that leading monomial to be divisible by some $x_j^d$, a contradiction. The displayed spanning set is therefore a basis.

The basis assertion is stable under every specialization of the parameters. Indeed, tensoring the free $R_d$-module with any $R_d$-algebra preserves the displayed basis, even when the specialized fixed-point scheme is nonreduced. Thus finiteness and flatness here are properties of the complete ordered-loop algebra; no generic-fiber count is being smuggled into the statement.

The recurrence encoded by the relations is $$x_{j+1}=p(x_j)+b x_{j-1},
  \qquad
  H_{b,p}(x_j,x_{j-1})=(x_{j+1},x_j).$$ A cyclic solution yields the $H^n$-fixed point $(x_0,x_{n-1})$. Conversely, a fixed point of $H^n$ yields the cyclic list of first coordinates of its iterates. The two constructions are polynomial, functorial over every $R_d$-algebra, and inverse; hence they identify the represented schemes. Finally, tensoring the algebras $A_{n_i}$ over $R_d$ tensors their displayed bases and gives rank $d^{\sum_i n_i}$.

The coincident-index formulas are part of the statement, not an omitted convention. For $n=1$ the single relation is $$p(x_0)+(b-1)x_0,$$ with leading monomial $x_0^d$. For $n=2$ the relations are $$p(x_0)+(b-1)x_1,
  \qquad
  p(x_1)+(b-1)x_0,$$ with leading monomials $x_0^d$ and $x_1^d$. Appendix [9](#sec:appendix){reference-type="ref" reference="sec:appendix"} expands these reductions over the coefficient ring.

These edge formulas cannot be recovered by pretending that the neighboring indices are distinct and specializing afterward. In the one-step loop, both the predecessor and successor term contribute to the same variable; in the two-step loop, they contribute to the opposite variable. The coefficient $b-1$ may vanish, but it is never used as a divisor: the monic degree-$d$ terms still control reduction. Thus the ranks $d$ and $d^2$ hold over all of $\operatorname{Spec}R_d$. They remain ranks of full ordered fixed-point schemes, however, and at special parameters their geometric fibers may contain lower-period points or nonreduced structure.

## What finite freeness does and does not provide

Lemma [\[lem:finite-free\]](#lem:finite-free){reference-type="ref" reference="lem:finite-free"} controls the full ordered fixed-point scheme. That scheme includes points of periods properly dividing $n$, repeated starting points on the same orbit, collisions between separately labelled markings, nonsimple points, scheme multiplicities, and possibly nonreduced fibers. Its rank is therefore not a count of exact cycles. A finite free algebra may be reducible, so no irreducibility conclusion follows either.

After localizing away from lower-period, collision, and nonsimple loci, the projection becomes the étale quasi-finite morphism of Section [2](#sec:incidence){reference-type="ref" reference="sec:incidence"}. An open subscheme of a finite scheme over the base need not remain finite or proper over every base point. Thus the finite-free lemma yields neither all-base finiteness of $\mathcal X_{\mathbf n}^{\circ}$, nor a uniform fiber degree, nor reconstruction from the selected traces. Its role is structural: it supplies a global algebraic home for the orbit equations while the theorem uses the localized simple incidence.

# Scalar component and marked trace coordinates {#sec:scalar}

Let $$\mathcal S_{\mathbf n}=(\mathcal X_{\mathbf n}^{\circ})_{b=0}$$ be the scalar cycle-marked locus. On it, $\lambda_i$ denotes the one-variable multiplier of the corresponding labelled polynomial cycle. The first assertion below constructs the component $\mathcal C_{\mathbf n}$. Put $$T=\mathbf A^1_t\times\mathbf A^r_{q_1,\ldots,q_r}$$ and, on that component, set $$\Psi=(-b,\rho_1,\ldots,\rho_r):\mathcal C_{\mathbf n}\longrightarrow T.$$

[\[thm:main\]]{#thm:main label="thm:main"} For every $d\geq2$ and every $\mathbf n\in\mathbf Z_{>0}^{d-1}$, with repeated numerical periods allowed and with the cycles labelled, pairwise disjoint, exact, and simple, the following assertions hold.

1.  **Marked scalar component.** The scalar cycle-marked locus $\mathcal S_{\mathbf n}$ is nonempty and irreducible. It is contained in a unique irreducible component $\mathcal C_{\mathbf n}$ of $\mathcal X_{\mathbf n}^{\circ}$. The natural map $$\pi:\mathcal C_{\mathbf n}\longrightarrow\mathcal B_d$$ is étale and dominant, and $$(\mathcal C_{\mathbf n})_{b=0}=\mathcal S_{\mathbf n}$$ scheme-theoretically inside the simple exact disjoint incidence. Thus $\mathcal C_{\mathbf n}$ contains the full simple scalar fiber, not merely one scalar point.

2.  **Coordinate map.** The morphism $$\Psi=(-b,\rho_1,\ldots,\rho_r):
        \mathcal C_{\mathbf n}\longrightarrow\mathbf A^1\times\mathbf A^r$$ is étale at a scalar point and hence is dominant and generically étale. Consequently $\rho_1,\ldots,\rho_r$ are algebraically independent over $\mathbf C(b)$ in $\mathbf C(\mathcal C_{\mathbf n})$.

3.  **Safe fixed-$b$ specialization.** There is an unspecified nonempty Zariski-open subset $$U\subset\mathbf G_m$$ such that, for every $b_0\in U$, the whole-fiber trace map $$\rho_{b_0}:(\mathcal C_{\mathbf n})_{b_0}\longrightarrow\mathbf A^r$$ is dominant. For each such $b_0$, at least one irreducible component of $(\mathcal C_{\mathbf n})_{b_0,\mathrm{red}}$ maps dominantly and generically étale to $\mathbf A^r$. No irreducibility of the specialized fiber, no all-component assertion, and no conclusion for a prescribed nonzero $b_0$ is included.

4.  **Completed local form.** At every scalar point $s\in\mathcal S_{\mathbf n}$, with centered coefficient coordinates $u=(u_0,\ldots,u_{d-2})$ based at $\pi(s)$, there are compatible isomorphisms $$\widehat{\mathcal O}_{\mathcal C_{\mathbf n},s}
        \simeq\mathbf C[[b,u_0,\ldots,u_{d-2}]],
        \qquad
        \widehat{\mathcal O}_{\mathcal S_{\mathbf n},s}
        \simeq\mathbf C[[u_0,\ldots,u_{d-2}]],$$ under which $$\rho_i(b,u)=\lambda_i(u)+bG_i(b,u)$$ for a unique $G_i\in\mathbf C[[b,u]]$.

5.  **Fitting-scheme restriction.** Define $$\mathcal R_H
        =
        V\!\left(\operatorname{Fitt}_0\Omega_{\mathcal C_{\mathbf n}/T}\right),
        \qquad
        \mathcal R_{\mathrm{poly}}
        =
        V\!\left(\operatorname{Fitt}_0
          \Omega_{\mathcal S_{\mathbf n}/\mathbf A^r}\right).$$ Then, on the simple scalar locus, $$\mathcal R_H\times_{\mathcal C_{\mathbf n}}\mathcal S_{\mathbf n}
        =
        \mathcal R_{\mathrm{poly}}$$ as closed subschemes. In completed local coordinates, $$J_H\bmod b=\pm J_{\mathrm{poly}}.$$ Both determinant sections are nonzero sections. Their zero schemes are effective Cartier divisors when nonempty and may be empty. If $\mathcal R_{\mathrm{poly}}$ is empty, the component-multiplicity assertion is vacuous; otherwise, the equality preserves the generic multiplicity along each actual irreducible boundary component. For $d>2$, it gives no numerical intersection multiplicity at an arbitrary closed point without a separately justified proper transverse slice.

\@L0.19L0.18L0.13L0.41@ Assertion & Evidence class & Bridges & Dependency in the proof\
Finite-free lemma & Direct & 1 & Monic cyclic-loop reduction and functorial fixed-point identification\
Part (1) & Direct and imported & 2--6 & Simple incidence, free quotient, scalar identification, marked polynomial irreducibility, and regular-component separation\
Part (2) & Direct, imported, and formal corollary & 4, 5, 7, 12 & Scalar trace reduction, full-rank multiplier point, block differential, and the residual-symmetry scope guard\
Part (3) & Direct and formal corollary & 8 & Open image of the total étale locus and a finite component-image argument\
Part (4) & Direct with foundational support & 9 & Formal étaleness, exact scalar fiber, and divisibility by $b$\
Part (5) & Direct with foundational support and formal corollary & 10, 11 & Cartesian differential base change, Fitting base change, determinant reduction, and generic local lengths\

Table [\[tab:dependencies\]](#tab:dependencies){reference-type="ref" reference="tab:dependencies"} is only a map of logical dependence. Each direct step is proved in the surrounding text; the sole imported dynamics input is the marked polynomial result cited above.

## The scalar incidence as a polynomial incidence

#### Proof bridge 4: scheme-theoretic scalar identification.

[\[lem:scalar-identification\]]{#lem:scalar-identification label="lem:scalar-identification"} For every $n\geq1$, $$H_{0,p}^n(x,y)=\bigl(p^n(x),p^{n-1}(x)\bigr).$$ The scalar simple exact disjoint point-marked incidence is scheme-isomorphic to the corresponding marked polynomial incidence. Under this isomorphism the Hénon trace is the polynomial multiplier, and Hénon simplicity is polynomial simplicity.

The iterate formula follows by induction. At $n=1$ it is the definition of $H_{0,p}$; applying $H_{0,p}$ to the displayed pair replaces the first coordinate by its image under $p$ and shifts the old first coordinate into the second. The fixed equations are consequently $$p^n(x)=x,
  \qquad
  y=p^{n-1}(x).$$ Projection to $x$ and the displayed graph construction are inverse on every test algebra, so the identification is scheme-theoretic.

In coordinate rings, this says more than a bijection of periodic points. After imposing $b=0$, the second fixed-point equation eliminates $y$ by the monic linear relation $y-p^{n-1}(x)=0$, while the first becomes $p^n(x)-x=0$. Elimination therefore introduces neither a localization nor a reduction. For several labels the same operation occurs independently in each pair $(x_i,y_i)$, and the collision equations restrict to equality of polynomial iterates. The construction is equivariant for every cyclic shift, so it identifies the point-marked schemes first and then their cycle-marked quotients.

If $x$ has minimal polynomial period $m\mid n$, its lifted pair has minimal $H_{0,p}$-period $m$; the converse follows by projecting the first coordinate. Two lifted cycles meet exactly when the corresponding polynomial cycles meet. Thus exactness and disjointness agree.

Differentiation gives $$D_{(x,y)}H_{0,p}^n
  =
  \begin{pmatrix}
    (p^n)'(x)&0\\
    (p^{n-1})'(x)&0
  \end{pmatrix}.$$ Writing $\lambda=(p^n)'(x)$, we obtain $$\operatorname{tr}(DH_{0,p}^n)=\lambda,
  \qquad
  \det(DH_{0,p}^n-I_2)
  =
  \det
  \begin{pmatrix}
    \lambda-1&0\\
    *&-1
  \end{pmatrix}
  =1-\lambda.$$ Hence the simple opens agree, and the trace restricts exactly to the polynomial multiplier. All identities are invariant under cyclic shifts, so they descend to cycle markings.

The determinant calculation also explains why simplicity has the same scheme-theoretic open condition on both sides: the two determinants differ by the unit $-1$ after writing one as $1-\lambda$ and the other as $\lambda-1$. Thus localization at either determinant gives the same scalar coordinate ring. This prevents an unnoticed enlargement or shrinking of the polynomial locus when it is embedded at the Hénon boundary.

## The scalar locus and its unique component

#### Proof bridge 5: the arbitrary-period polynomial input.

For the marked polynomial space, Gorbovickis's construction gives an irreducible algebraic space independent of the initial admissible markings, and its Theorem 1.6 applies to every $d\geq2$, every $k\leq d-1$, and every positive period vector [@Gor13]. Taking $k=r=d-1$, all coefficient directions, and then the nonempty simple exact disjoint open gives an irreducible scalar point-marked locus. Its finite cyclic quotient $\mathcal S_{\mathbf n}$ is irreducible as well.

Here the order of the restrictions matters. Exactness and pairwise disjointness are imposed on the labelled marked space, and simplicity is the nonvanishing of the corresponding multiplier-minus-one functions. They form a common open subset. The full-rank configuration described below belongs to that open, so it is nonempty rather than merely formally defined. A nonempty open in an irreducible space is irreducible, and its surjective image under the finite cyclic quotient is irreducible. This is the only irreducibility assertion transferred from polynomial dynamics; it does not concern the complete Hénon incidence or a nonzero specialized fiber.

The same input supplies a full-rank point at $p_0(z)=z^d$. Lemma 2.1 in that work selects nonzero exact periodic points on distinct cycles such that $$\det\left(
    \frac{\partial\lambda_i}{\partial a_j}
  \right)_{\substack{1\leq i\leq r\\0\leq j\leq d-2}}
  \neq0.$$ At a nonzero exact $n_i$-periodic point of $z^d$, $$(p_0^{n_i})'(x)
  =
  d^{n_i}x^{d^{n_i}-1}
  =
  d^{n_i}\neq1,$$ so these cycles are simple. Repeated numerical periods are allowed because the selected cycles, not the integers $n_i$, are distinct. For $d=2$ there is one cycle, $k=1=d-1$, and the applicable statements remain Theorem 1.6 and Lemma 2.1; no use is made of the later corollary whose headline begins at degree three.

#### Proof bridge 6: regular-component separation.

[\[prop:unique-component\]]{#prop:unique-component label="prop:unique-component"} The irreducible locus $\mathcal S_{\mathbf n}$ is contained in a unique irreducible component $\mathcal C_{\mathbf n}$ of $\mathcal X_{\mathbf n}^{\circ}$. No other component meets $b=0$, and $$(\mathcal C_{\mathbf n})_{b=0}=\mathcal S_{\mathbf n}$$ scheme-theoretically. The map $\pi:\mathcal C_{\mathbf n}\to\mathcal B_d$ is étale and dominant.

The scheme $\mathcal X_{\mathbf n}^{\circ}$ is noetherian and regular by Lemma [\[lem:cycle-quotient\]](#lem:cycle-quotient){reference-type="ref" reference="lem:cycle-quotient"}. Every regular local ring is a domain, so there is exactly one irreducible component through each point. Hence distinct components are disjoint. A noetherian scheme has only finitely many irreducible components, so the complement of each component is a finite union of closed components; every component is consequently both open and closed. Since $\mathcal S_{\mathbf n}$ is nonempty and irreducible, it lies in one such component, denoted $\mathcal C_{\mathbf n}$, and it cannot meet another.

The local-ring argument is stronger than a connectedness observation. The minimal primes of the local ring at a point correspond to the irreducible components through that point; a regular local domain has one minimal prime, so two components have no common point even along a lower-dimensional stratum. Finiteness of the component set then makes the component index a finite discrete invariant. The map from the irreducible scalar locus to that finite set is constant, which places every scalar point on the same component without choosing a path or a distinguished continuation.

Now take the scheme-theoretic fiber of the open-and-closed decomposition at $b=0$. By definition $\mathcal S_{\mathbf n}$ is the scalar fiber of the entire simple cycle-marked incidence, and Lemma [\[lem:scalar-identification\]](#lem:scalar-identification){reference-type="ref" reference="lem:scalar-identification"} identifies that fiber, with its scheme structure, with the simple marked polynomial incidence. Every one of its points lies on $\mathcal C_{\mathbf n}$. The scalar fiber of each other open-and-closed component therefore has empty underlying space and is the empty scheme. Base change preserves the disjoint decomposition, so $$(\mathcal X_{\mathbf n}^{\circ})_{b=0}
  =(\mathcal C_{\mathbf n})_{b=0}
  =\mathcal S_{\mathbf n}$$ scheme-theoretically. In particular, the equality is not obtained by discarding nilpotents after specialization. Independently, since the ambient projection is étale, its scalar fiber is étale over the coefficient space and hence reduced, in agreement with the polynomial description.

One may see the scheme equality locally through the idempotents of the open-and-closed decomposition. On an affine neighborhood meeting the scalar fiber, the coordinate ring is a finite product of the rings belonging to the components. Tensoring that product with the quotient of the base by $(b)$ commutes with the product. The factors belonging to components other than $\mathcal C_{\mathbf n}$ have empty scalar spectrum and hence become the zero ring; the remaining factor is exactly the coordinate ring of $\mathcal S_{\mathbf n}$ supplied by the scalar-identification lemma. Thus the equality holds at the level of quotient rings. Reducedness of the étale scalar fiber is a consistency check, not a step that erases possible nilpotents.

The restriction of $\pi$ is étale. Étale morphisms are open, so its nonempty image is open in the irreducible base $\mathcal B_d$ and is therefore dense. This is dominance; surjectivity is neither needed nor asserted. The same argument also shows why the whole scalar locus, rather than a chosen full-rank point, is essential: continuation inside a regular incidence cannot jump from $\mathcal C_{\mathbf n}$ to another component.

This proves part (1) of Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}. It also explains why one cannot replace the selected component by the full marked Hénon incidence.

There is a useful codimension consequence that will be used only locally. Since $\pi$ is étale and $b$ is a coordinate on the smooth base, its pullback is a non-zero-divisor in every local ring of $\mathcal C_{\mathbf n}$. Therefore $\mathcal S_{\mathbf n}=V(b)$ is an effective Cartier divisor in the selected component. This does not say that the trace-critical divisor meets it transversely; it only supplies the exact regular boundary parameter needed for completion and for reduction of the Jacobian determinant.

## The block differential

At every point of the family, $$DH_{b,p}(x,y)
  =
  \begin{pmatrix}
    p'(x)&b\\
    1&0
  \end{pmatrix},
  \qquad
  \det DH_{b,p}=-b.$$ Multiplicativity around a marked cycle gives $$\label{eq:return-determinant}
  \det(DH_{b,p}^{n_i})=(-b)^{n_i}.$$

#### Proof bridge 7: the transverse parameter and multiplier block.

Let $s\in\mathcal S_{\mathbf n}$ be the full-rank point above. Since $\pi$ is étale, $(b,u_0,\ldots,u_{d-2})$, where the $u_j$ are centered coefficient coordinates, form local coordinates on $\mathcal C_{\mathbf n}$ at $s$. With target coordinates ordered as $(t,q_1,\ldots,q_r)$ and $t=-b$, the differential is $$D\Psi
  =
  \begin{pmatrix}
    -1&0&\cdots&0\\
    \partial_b\rho_1&&&\\
    \vdots&&
      \left(\partial_{u_j}\rho_i\right)&\\
    \partial_b\rho_r&&&
  \end{pmatrix}.$$ Lemma [\[lem:scalar-identification\]](#lem:scalar-identification){reference-type="ref" reference="lem:scalar-identification"} gives $\rho_i(0,u)=\lambda_i(u)$, and hence $$\det D\Psi(s)
  =
  \pm
  \det\left(
    \frac{\partial\lambda_i}{\partial u_j}
  \right)(s)
  \neq0.$$ Thus $\Psi$ is étale at $s$. Its étale locus maps openly to $T$, so the image contains a nonempty open subset. Since $\mathcal C_{\mathbf n}$ and $T$ are irreducible of the same dimension $d$, $\Psi$ is dominant and generically étale.

In local-ring terms, the displayed determinant is a unit at $s$, so the relative cotangent module of $\Psi$ vanishes there. Its nonvanishing locus is an open neighborhood of $s$. Because $\mathcal C_{\mathbf n}$ is irreducible, that neighborhood is dense; thus generic étaleness refers to the selected total component and is not a statement that every specialized fiber is étale.

Dominance makes $$\mathbf C[t,q_1,\ldots,q_r]\longrightarrow\mathbf C(\mathcal C_{\mathbf n}),
  \qquad
  t\longmapsto-b,\quad q_i\longmapsto\rho_i,$$ injective. A relation among the $\rho_i$ over $\mathbf C(b)$ could be cleared of denominators to give a nonzero polynomial relation among $b,\rho_1,\ldots,\rho_r$ over $\mathbf C$, contradicting this injection. Part (2) of Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"} follows.

More precisely, suppose $F(\rho_1,\ldots,\rho_r)=0$ for a nonzero $F\in\mathbf C(b)[X_1,\ldots,X_r]$. Multiplication by a common nonzero denominator produces $\widetilde F\in\mathbf C[b,X_1,\ldots,X_r]$. Removing the largest common power of any coefficient denominator ensures that $\widetilde F$ remains nonzero. Its substitution into $(b,\rho_1,\ldots,\rho_r)$ contradicts the injective coordinate-ring map coming from dominance. No specialization of $b$ is used in this argument, which is why the conclusion is independence over the rational function field rather than an assertion for every fixed parameter.

Equation [\[eq:return-determinant\]](#eq:return-determinant){reference-type="eqref" reference="eq:return-determinant"} also fixes the interpretation of a trace. The characteristic polynomial of the return matrix is $$X^2-\rho_iX+(-b)^{n_i}.$$ The trace and determinant therefore determine its roots as an unordered pair. The formula supplies no regular choice of one root.

# Completed local geometry at the polynomial boundary {#sec:completion}

The full-rank scalar point proves dominance, but the completed statement is uniform over the entire simple scalar locus. Fix an arbitrary $s\in\mathcal S_{\mathbf n}$ and let $u_j=a_j-a_j(\pi(s))$ be centered coefficient coordinates.

#### Proof bridge 9: formal étaleness and divisibility by $b$.

[\[prop:completion\]]{#prop:completion label="prop:completion"} There are compatible isomorphisms $$\widehat{\mathcal O}_{\mathcal C_{\mathbf n},s}
  \simeq
  \mathbf C[[b,u_0,\ldots,u_{d-2}]],
  \qquad
  \widehat{\mathcal O}_{\mathcal S_{\mathbf n},s}
  \simeq
  \mathbf C[[u_0,\ldots,u_{d-2}]].$$ For every label $i$ there is a unique $G_i\in\mathbf C[[b,u_0,\ldots,u_{d-2}]]$ such that $$\rho_i(b,u)=\lambda_i(u)+bG_i(b,u).$$

The morphism $\pi:\mathcal C_{\mathbf n}\to\mathcal B_d$ is étale at $s$, and the two residue fields equal $\mathbf C$. Formal étaleness identifies completed local rings: $$\widehat{\mathcal O}_{\mathcal C_{\mathbf n},s}
  \simeq
  \widehat{\mathcal O}_{\mathcal B_d,\pi(s)}.$$ In the chosen coordinates the ring on the right is $\mathbf C[[b,u_0,\ldots,u_{d-2}]]$. This is the completed-local behavior of étale morphisms recorded in the Stacks Project [@StacksProject Tags 02GH and 0257].

The isomorphism is compatible with the homomorphism from the base: each $u_j$ is the pullback of the corresponding centered coefficient and $b$ is the pullback of the Jacobian parameter. One way to see the absence of an extra formal choice is to apply the infinitesimal lifting property successively to the quotients by powers of the maximal ideal. At every order the lift through an étale morphism is unique, and the inverse limit gives the displayed complete local isomorphism.

Proposition [\[prop:unique-component\]](#prop:unique-component){reference-type="ref" reference="prop:unique-component"} says scheme-theoretically that the scalar fiber is cut out by $b$. Quotienting the first completed ring by $(b)$ yields the asserted completion of $\mathcal S_{\mathbf n}$. Compatibility of the two isomorphisms means precisely that the natural map from the first completion to the second becomes $$\mathbf C[[b,u_0,\ldots,u_{d-2}]]
  \longrightarrow
  \mathbf C[[u_0,\ldots,u_{d-2}]],
  \qquad b\longmapsto0.$$

There are two exactness points in this passage. First, for an étale local map with the same residue field, the isomorphisms on infinitesimal neighborhoods commute with the transition maps; taking their inverse limit therefore produces an isomorphism of complete local algebras, not merely an isomorphism of tangent spaces. Second, in these noetherian local rings the completion of the quotient by $(b)$ is the quotient of the completion by the closed ideal generated by $b$. Hence the lower completed ring and the specialization map are forced by the scheme-theoretic scalar fiber rather than chosen independently.

On that quotient, Lemma [\[lem:scalar-identification\]](#lem:scalar-identification){reference-type="ref" reference="lem:scalar-identification"} identifies the trace with the multiplier germ of the uniquely continued simple polynomial cycle: $$\rho_i(0,u)=\lambda_i(u).$$ It follows that $\rho_i-\lambda_i$ belongs to the principal ideal $(b)$. This is an ideal-membership assertion in the complete local ring, not only an equality on closed points. Thus some $G_i$ satisfies $\rho_i-\lambda_i=bG_i$. The power-series ring is a domain, so $b$ is a non-zero-divisor. If two power series had the required property, their difference would be annihilated by $b$ and would therefore vanish. This proves both existence and uniqueness of $G_i$.

This proves part (4) of Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}. The statement stays on the normal-form cover. Formal étaleness does not identify the completed local ring of a coarse root-of-unity quotient at a point with nontrivial stabilizer.

The proposition also determines the boundary square used next. Let $$T_0=\{t=0\}\times\mathbf A^r\subset T.$$ Because $t\circ\Psi=-b$ and the entire scalar fiber is $\mathcal S_{\mathbf n}$, not merely a dense open part of it, the square $$\label{eq:cartesian-square}
\begin{array}{ccc}
  \mathcal S_{\mathbf n}&\longrightarrow&\mathcal C_{\mathbf n}\\
  \big\downarrow{\Lambda}&&\big\downarrow{\Psi}\\
  T_0&\longrightarrow&T
\end{array}$$ is Cartesian, where $\Lambda=(\lambda_1,\ldots,\lambda_r)$ after identifying $T_0\simeq\mathbf A^r$.

Indeed, the pullback to $\mathcal C_{\mathbf n}$ of the ideal $(t)$ defining $T_0$ is the ideal $(b)$. Its vanishing subscheme is $(\mathcal C_{\mathbf n})_{b=0}=\mathcal S_{\mathbf n}$ by Proposition [\[prop:unique-component\]](#prop:unique-component){reference-type="ref" reference="prop:unique-component"}, while the remaining target coordinates restrict from $\rho_i$ to $\lambda_i$ by Lemma [\[lem:scalar-identification\]](#lem:scalar-identification){reference-type="ref" reference="lem:scalar-identification"}. Thus the universal fiber product, including nilpotent test schemes, is the displayed scalar square. This ideal calculation is the point at which a continuation through only one scalar point would be insufficient.

# Scheme-theoretic ramification and multiplicities {#sec:fitting}

## Relative differentials and zeroth Fitting ideals

Both $\mathcal C_{\mathbf n}$ and $T$ are smooth of dimension $d$. The cotangent map $$\Psi^*\Omega_T\longrightarrow\Omega_{\mathcal C_{\mathbf n}}$$ is therefore a map between locally free sheaves of rank $d$, with cokernel $\Omega_{\mathcal C_{\mathbf n}/T}$. Locally, its determinant generates $\operatorname{Fitt}_0\Omega_{\mathcal C_{\mathbf n}/T}$. The analogous description applies to $\Lambda:\mathcal S_{\mathbf n}\to\mathbf A^r$, because $\mathcal S_{\mathbf n}$ is étale over the smooth polynomial coefficient space and has dimension $r$.

Concretely, after choosing local coordinates, the standard exact sequence has a right-exact presentation $$\mathcal O_{\mathcal C_{\mathbf n}}^{\oplus d}
  \xrightarrow{D\Psi}
  \mathcal O_{\mathcal C_{\mathbf n}}^{\oplus d}
  \longrightarrow
  \Omega_{\mathcal C_{\mathbf n}/T}
  \longrightarrow0.$$ Changing either coordinate frame multiplies the determinant by a unit, so the ideal and its closed subscheme are intrinsic. The same construction for $\Lambda$ uses an $r$-by-$r$ presentation. The base-change proposition below compares these modules, not merely the supports of their determinant zero sets.

#### Proof bridge 10: Cartesian base change.

[\[prop:fitting-basechange\]]{#prop:fitting-basechange label="prop:fitting-basechange"} On the Cartesian square [\[eq:cartesian-square\]](#eq:cartesian-square){reference-type="eqref" reference="eq:cartesian-square"}, there is a natural isomorphism $$\Omega_{\mathcal C_{\mathbf n}/T}
  \otimes_{\mathcal O_{\mathcal C_{\mathbf n}}}
  \mathcal O_{\mathcal S_{\mathbf n}}
  \simeq
  \Omega_{\mathcal S_{\mathbf n}/T_0}.$$ Consequently, $$\operatorname{Fitt}_0\Omega_{\mathcal C_{\mathbf n}/T}\cdot
  \mathcal O_{\mathcal S_{\mathbf n}}
  =
  \operatorname{Fitt}_0\Omega_{\mathcal S_{\mathbf n}/T_0},$$ and $$\mathcal R_H\times_{\mathcal C_{\mathbf n}}\mathcal S_{\mathbf n}
  =
  \mathcal R_{\mathrm{poly}}$$ as closed subschemes.

Relative Kähler differentials commute with arbitrary base change. Applying that fact to the Cartesian square gives the first isomorphism. Locally this can be read without suppressing the scheme structure. If $B\to A$ presents $\Psi$, $B'=B/(t)$ presents $T_0$, and $A'=A\otimes_BB'=A/(b)$ presents $\mathcal S_{\mathbf n}$, then the universal derivation induces $$\Omega_{A/B}\otimes_AA'\simeq\Omega_{A'/B'}.$$ The equality $A'=A/(b)$ is exactly the Cartesian assertion proved above.

The modules are finitely presented because all schemes and morphisms are of finite type over $\mathbf C$. Choose locally a finite presentation matrix for $\Omega_{A/B}$. After tensoring with $A'$, the same matrix, with entries reduced modulo $b$, presents $\Omega_{A'/B'}$. Its maximal minors generate the respective zeroth Fitting ideals, so reduction of the minors proves $$\operatorname{Fitt}_0(\Omega_{A/B})A'
  =\operatorname{Fitt}_0(\Omega_{A'/B'}).$$ These local equalities glue. The precise foundational statements are Stacks Project Tag 07Z6, Lemma 15.8.4, and the associated scheme construction in Tag 0C3I [@StacksProject]. Passing from the ideal equality to its vanishing subschemes gives the final assertion.

No flatness of $B'$ over $B$ is used here; in fact $B'=B/(t)$ is the closed boundary base change. The base-change identity for relative differentials comes from the universal property of derivations, and the Fitting identity comes from reducing a finite presentation matrix. If $I_H$ denotes the local zeroth Fitting ideal, the fiber of its closed subscheme is defined by $(I_H+(b))/(b)$ in $A/(b)$. The minor calculation identifies this quotient ideal with the polynomial zeroth Fitting ideal itself. Consequently the result retains nilpotent structure and orders of vanishing; replacing the ideals by their radicals would prove only an equality of supports and would be insufficient for the multiplicity statement.

The proof uses the full simple scalar fiber in the Cartesian square. It does not extend across a nonsimple closure, where the incidence need not be étale and the selected component need not have the same local geometry.

## The local determinant congruence

Use the completed coordinates of Proposition [\[prop:completion\]](#prop:completion){reference-type="ref" reference="prop:completion"}. The first row of $D\Psi$ is $(-1,0,\ldots,0)$, so, up to the sign determined by the ordering of source and target coordinates, $$J_H
  =
  \pm\det\left(
    \frac{\partial\rho_i}{\partial u_j}
  \right).$$ Since $\rho_i=\lambda_i+bG_i$, $$\frac{\partial\rho_i}{\partial u_j}\bmod b
  =
  \frac{\partial\lambda_i}{\partial u_j}.$$ Compatible orderings therefore give the sign-unit identity $$\label{eq:jacobian-congruence}
  J_H\bmod b=\pm J_{\mathrm{poly}},
  \qquad
  J_{\mathrm{poly}}
  =
  \det\left(
    \frac{\partial\lambda_i}{\partial u_j}
  \right).$$ This local formula is the determinant form of Proposition [\[prop:fitting-basechange\]](#prop:fitting-basechange){reference-type="ref" reference="prop:fitting-basechange"}; it does not replace the scheme-level proof.

The sign can be seen directly from the block matrix. In the compatible source order $(b,u_0,\ldots,u_{d-2})$ and target order $(t,q_1,\ldots,q_r)$, the first row is exactly $(-1,0,\ldots,0)$. Expanding along it discards all entries $\partial_b\rho_i$ and leaves the coefficient-direction minor. Moreover, $$\partial_{u_j}(\lambda_i+bG_i)\bmod b
  =\partial_{u_j}\lambda_i,$$ because $b$ is independent of every $u_j$. Hence the reduction is the polynomial determinant up to only the permutation/orientation sign, not an uncontrolled function. This is compatible with the unit ambiguity of a determinant line after changing local frames.

## Cartier-or-empty critical schemes

#### Proof bridge 11: nonzero sections and generic lengths.

The determinant of $D\Psi$ is not the zero section because it is nonzero at the scalar point used in Section [4](#sec:scalar){reference-type="ref" reference="sec:scalar"}. Likewise, $J_{\mathrm{poly}}$ is nonzero at that point. Thus each is a nonzero section of a determinant line bundle on a smooth irreducible scheme. A nonzero section on an integral scheme is locally a non-zero-divisor wherever it is not a unit. Its zero scheme is consequently an effective Cartier divisor if it has a zero, and is empty if the section is everywhere invertible.

To make the dichotomy explicit, trivialize the determinant line bundle on an affine open. The section is represented by an element of the coordinate domain. Its image in the function field is independent of the trivialization up to a unit and is nonzero because of the full-rank scalar point. Hence every local representative is either a unit or a nonzero nonunit, and in the latter case it is a non-zero-divisor. These local principal ideals glue to an effective Cartier divisor. This argument establishes the Cartier property but says nothing about reducedness of the local equations.

The full-rank polynomial point proves that the polynomial determinant is not identically zero; it does not prove that the polynomial critical scheme is nonempty. This distinction is already visible in the quadratic one-marking case and is retained in the theorem.

Equation [\[eq:jacobian-congruence\]](#eq:jacobian-congruence){reference-type="eqref" reference="eq:jacobian-congruence"} also shows that the scalar Cartier divisor $(b=0)$ is not a component of $(J_H=0)$. If $\mathcal R_{\mathrm{poly}}$ is empty, there is no boundary component whose multiplicity could be compared, and the assertion is vacuous. Suppose it is nonempty, let $Z$ be an actual irreducible component, and write $\eta_Z$ for its generic point. Reduction modulo $b$ gives a canonical isomorphism $$\frac{\mathcal O_{\mathcal C_{\mathbf n},\eta_Z}}{(b,J_H)}
  \simeq
  \frac{\mathcal O_{\mathcal S_{\mathbf n},\eta_Z}}{(J_{\mathrm{poly}})}.$$ This isomorphism is obtained before any length calculation. If $A=\mathcal O_{\mathcal C_{\mathbf n},\eta_Z}$, then the local ring of the scalar fiber is $A/(b)$, and the image of $J_H$ there is the signed polynomial determinant. Quotienting first by $b$ and then by that image gives exactly the displayed right-hand ring. The same observation shows that the whole boundary cannot be a component of $(J_H=0)$: at the generic point of the irreducible scalar fiber, the polynomial determinant is nonzero.

Here is the local dimension check behind the multiplicity statement. At $\eta_Z$, the regular local ring from $\mathcal S_{\mathbf n}$ has dimension one, and the nonzero local equation $J_{\mathrm{poly}}$ is a parameter up to a positive power and a unit. Its quotient therefore has finite length. The corresponding local ring from $\mathcal C_{\mathbf n}$ has dimension two; $b$ is a non-zero-divisor, and the reduction of $J_H$ modulo $b$ is the same nonzero equation up to sign. Thus $(b,J_H)$ has zero-dimensional quotient. A module killed by $b$ has exactly the same submodules when regarded over the ambient local ring or over its quotient by $(b)$, and the residue fields are identical. The two composition lengths are consequently equal, giving $$\label{eq:length-equality}
  \operatorname{length}_{\mathcal O_{\mathcal C_{\mathbf n},\eta_Z}}
  \frac{\mathcal O_{\mathcal C_{\mathbf n},\eta_Z}}{(b,J_H)}
  =
  \operatorname{length}_{\mathcal O_{\mathcal S_{\mathbf n},\eta_Z}}
  \frac{\mathcal O_{\mathcal S_{\mathbf n},\eta_Z}}{(J_{\mathrm{poly}})}.$$ This is the generic component multiplicity retained by the closed-subscheme restriction.

The empty alternative fits the same algebra. If the polynomial determinant is a unit along the scalar locus, its Fitting zero scheme has no component $Z$, so there is no generic local length to measure. If a component exists, the one-dimensional regular local ring at its generic point is a discrete valuation ring, and the length is the valuation of its nonzero determinant equation. The base-change isomorphism preserves that valuation on restriction. It neither excludes additional Hénon critical components away from the boundary nor supplies a closed-point multiplicity where further parameters remain.

Equivalently, if a uniformizer $z$ of the one-dimensional regular local ring $\mathcal O_{\mathcal S_{\mathbf n},\eta_Z}$ writes $J_{\mathrm{poly}}=u z^m$ with $u$ a unit, then the right side of Equation [\[eq:length-equality\]](#eq:length-equality){reference-type="eqref" reference="eq:length-equality"} has length $m$. The Cartesian ideal identity says that the restriction of the Hénon critical scheme to the boundary has the same exponent $m$ at $Z$. It does not assign a multiplicity to a component that is absent, and it does not turn this generic valuation into a closed-point intersection number.

When $d>2$, the scalar locus has dimension $d-1$ and a nonempty Cartier component $Z$ has dimension $d-2>0$. At an arbitrary closed point the quotient by $(b,J_H)$ need not be Artinian. A numerical closed-point intersection would require a separately justified proper transverse slice, which is not part of the result. Neither the Fitting equality nor the length identity implies that either critical scheme is reduced or smooth, or that the boundary intersection is transverse or has normal crossings. Part (5) of Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"} is proved.

# General nonzero fibers and residual normal-form symmetry {#sec:fibers}

## A reducible-fiber-safe specialization

#### Proof bridge 8: the open image of the total étale locus.

Let $E\subset\mathcal C_{\mathbf n}$ be the nonempty étale locus of $\Psi$. The restriction $$\Psi|_E:E\longrightarrow T$$ is étale and hence open. Set $V=\Psi(E)$. Then $V$ is a nonempty open subset of $T$. The projection $\operatorname{pr}_t:T\to\mathbf A^1_t$ is smooth and therefore open, so $\operatorname{pr}_t(V)$ is a nonempty open subset of the $t$-line. For every $t_0$ in this projection, the slice $V_{t_0}$ is a nonempty open subset of $\mathbf A^r$ and hence is dense.

Indeed, $V_{t_0}$ is the intersection of the open set $V$ with the fiber $\{t_0\}\times\mathbf A^r$, viewed inside that fiber. Membership of $t_0$ in the projection says exactly that this intersection is nonempty. Since the fiber is irreducible, every such nonempty open is dense. Using the open image before specialization produces one common open set of parameter values; it does not choose a separate exceptional set for each trace coordinate.

Changing coordinates by $t=-b$, define $$U=
  \{-t:t\in\operatorname{pr}_t(V)\}\cap\mathbf G_m.$$ A nonempty open subset of $\mathbf A^1$ cannot be supported at the single point $0$, so $U$ is nonempty and open in $\mathbf G_m$. If $b_0\in U$, then the image of the whole fiber $(\mathcal C_{\mathbf n})_{b_0}$ contains the dense open set $V_{-b_0}$. The whole-fiber trace map is therefore dominant.

This conclusion uses the entire scheme-theoretic fiber. A point $q\in V_{-b_0}$ has, by the definition of $V$, a preimage $x\in E$ with $\Psi(x)=(-b_0,q)$. Since the first coordinate of $\Psi$ is exactly $-b$, the point $x$ lies in $(\mathcal C_{\mathbf n})_{b_0}$. Thus no constructibility or closure argument is needed to place $V_{-b_0}$ in the image; density of that nonempty open slice proves dominance directly.

Write the reduced finite-type fiber as the finite union of its irreducible components $D_1,\ldots,D_m$. The sets $E_{b_0}\cap D_j$ have images whose closures cover the closure of $V_{-b_0}=\mathbf A^r$. Since $\mathbf A^r$ is irreducible, at least one such closure is all of $\mathbf A^r$. Choose the corresponding $D_j$. It meets the base-changed étale locus in a nonempty open subset, and the restriction there is étale. Indeed, $E_{b_0}\to\mathbf A^r$ is obtained from the étale morphism $E\to T$ by the base change $t=-b_0$, so it is étale. Its intersection with the chosen component is dense in $D_j$ because its image is dense; therefore it contains a dense open part of that reduced component. Thus $D_j$ maps dominantly and generically étale. The finite-union step is also the precise reason for saying that at least one component works: irreducibility of the target forces one dense component image, but gives no information about the other $D_k$. This proves part (3) of Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"} without assuming that the fiber is irreducible and without asserting anything about the remaining components. The construction does not identify the complement of $U$ and gives no conclusion at a prescribed value, including $b=-1$.

For completeness, finiteness of the component list is essential in the dense-image step. Every point of $E_{b_0}$ lies on the reduction of some $D_j$, so $V_{-b_0}$ is covered by the finitely many component images. If all their closures were proper closed subsets of $\mathbf A^r$, their finite union could not equal the irreducible space $\mathbf A^r$. Hence one closure is the whole target. On the chosen component, the intersection with $E_{b_0}$ is open; its dense image makes it nonempty and dense in that component, and the map there is étale by base change. Passing to the reduced fiber is used only to name irreducible components. Dominance of the whole fiber was already proved for its original scheme structure, so no reducedness of that fiber is being asserted.

## Trace, determinant, and the unordered eigenpair

For the return map along the $i$th cycle, Equation [\[eq:return-determinant\]](#eq:return-determinant){reference-type="eqref" reference="eq:return-determinant"} gives determinant $(-b)^{n_i}$. Thus its characteristic polynomial is determined by $\rho_i$ and $b$, but its two roots are only an unordered pair. Near the discriminant there need not be a regular eigenvalue branch. The coordinate theorem concerns traces, not individually selected two-dimensional multipliers.

Algebraically, adjoining one eigenvalue requires solving $X^2-\rho_iX+(-b)^{n_i}=0$ and generally passes to a degree-two cover that ramifies where the discriminant vanishes. Nothing in the marked-cycle incidence chooses one sheet of that cover. Keeping the trace on the original incidence is therefore essential both for regularity of the coordinate functions and for the stated residual-symmetry guard.

## The residual root-of-unity action

#### Proof bridge 12: the finite normal-form symmetry.

For $\beta\in\mu_{d-1}$, let $$L_\beta(x,y)=(\beta x,\beta y),
  \qquad
  p_\beta(z)=\beta^{-1}p(\beta z).$$ The condition $\beta^{d-1}=1$ makes $p_\beta$ monic and centered, and direct substitution gives $$L_\beta^{-1}\circ H_{b,p}\circ L_\beta
  =
  H_{b,p_\beta}.$$ This conjugacy fixes $b$, transports each labelled cycle with its label, and preserves every return trace. It preserves $\mathcal S_{\mathbf n}$ and hence preserves $\mathcal C_{\mathbf n}$ by the uniqueness in Proposition [\[prop:unique-component\]](#prop:unique-component){reference-type="ref" reference="prop:unique-component"}.

On coefficients, the action is $$a_j\longmapsto \beta^{j-1}a_j,
  \qquad 0\leq j\leq d-2.$$ The leading coefficient remains one because $\beta^{d-1}=1$, and the missing $z^{d-1}$ coefficient remains zero. The constant coefficient has weight $\beta^{-1}$, which is faithful on $\mu_{d-1}$. Consequently the open set $a_0\neq0$ has trivial stabilizer. This supplies the asserted generic freeness without imposing any condition on the marked periods.

For a generic centered polynomial the stabilizer is trivial: the constant coefficient already has faithful weight under the action. When $d>2$, a generic $\mu_{d-1}$-orbit therefore consists of $d-1$ distinct points with the same values of $b,\rho_1,\ldots,\rho_r$. This obstructs generic injectivity and birationality on the monic-centered normal-form cover; it is not an exact computation of every fiber degree. For $d=2$, $\mu_1$ is trivial. At a point with nontrivial stabilizer, a coarse quotient can have a quotient singularity, so the completed-local statement is not transferred naively to that quotient.

# Comparison, limitations, and conclusion {#sec:comparison}

## Comparison by mathematical question

The comparison in this section is limited to the listed public versions available through 17 August 2026. It is a scope comparison, not an absolute-priority assertion.

#### Marked local coordinates.

The indispensable polynomial result is Gorbovickis's theorem on algebraic independence of multipliers of arbitrary marked polynomial cycles [@Gor13]. We import its irreducible marked space and one full-rank point; it contains no generalized Hénon, fixed-$b$, completion, or Fitting statement. Gorbovickis and Taflin treat independence of eigenvalue functions for regular polynomial endomorphisms in several variables [@GT24]. Generalized Hénon maps are not regular polynomial endomorphisms of projective space, and the degeneration $b=0$ and its trace Fitting scheme are outside that setting.

#### Complete spectra and global rigidity.

Huguin studies complete unmarked period-one and period-two multiplier spectra for polynomial moduli and finite birational recovery [@Hug24]. Cantat and Dujardin prove rigidity from the full Hénon multiplier spectrum and finite determination using complete low-period data [@CD26]. Those global data differ from an arbitrary labelled selection of exactly $d-1$ cycles, and their results do not supply the boundary base-change theorem. Bianchi and He use the full marked unstable spectrum analytically in a thermodynamic path metric on hyperbolic components [@BH26]; this does not give finite algebraic independence or scalar degeneration. Friedland and Milnor's normal forms and fixed-point calculations account for a low-degree, period-one overlap [@FM89], not the arbitrary-period scheme-theoretic statement proved here.

#### Boundary scheme structure.

The formal-local and Fitting operations used in Sections [5](#sec:completion){reference-type="ref" reference="sec:completion"} and [6](#sec:fitting){reference-type="ref" reference="sec:fitting"} are the exact foundational roles of the Stacks Project [@StacksProject]. They apply after the simple scalar square has been proved Cartesian. They supply no irreducibility theorem and no extension through nonsimple or compactified incidences.

## Exact limitations

For clarity, the mathematical boundary of the result is recorded explicitly.

1.  No irreducibility claim for the full marked Hénon incidence.

2.  No irreducibility claim for any or every specialized fixed-$b$ fiber.

3.  No local-coordinate claim for every nonzero $b$.

4.  No conclusion at any prescribed nonzero fiber, including $b=-1$.

5.  No global injectivity, birationality, or reconstruction claim on the monic-centered normal-form cover.

6.  No claim that every irreducible component of a general fixed-$b$ fiber dominates or is generically étale.

7.  No reducedness or smoothness claim for either critical/Fitting scheme.

8.  No transversality or normal-crossings claim for the boundary intersection.

9.  No global, nonsimple, or compactified Fitting-scheme equality beyond the simple scalar locus.

10. No closed-point numerical intersection multiplicity without a separately justified proper transverse slice; the theorem preserves generic multiplicities along boundary components.

11. No individual eigenvalue branch is a coordinate: $\det(DH_{b,p}^{n_i})=(-b)^{n_i}$, so trace records only the unordered eigenvalue pair once the determinant is known.

12. No interpretation of finite-free rank $d^n$ as an exact-cycle count.

13. The fiber $b=0$ is only the polynomial/proof boundary; $H_{0,p}$ is not a Hénon automorphism.

14. No positive-characteristic extension.

15. No extension to multi-factor or composed generalized Hénon maps.

16. Point-marked fibers contain cyclic-shift copies; passage to cycle markings removes only those shifts, not residual $\mu_{d-1}$ ambiguity.

17. No naive coarse $\mu_{d-1}$-quotient completed-local claim near stabilizers; stack or quotient-singularity analysis is required.

18. No claim that the simple exact open is finite or proper over all of $\mathcal B_d$, no uniform all-fiber degree, and no all-fiber reconstruction.

19. No absolute-priority or first-ever claim.

20. No computational, CAS, numerical, empirical, or experimental evidence or result.

## Conclusion

The scalar boundary performs two jobs at once. Its marked incidence selects one regular Hénon component through the entire simple polynomial locus, and its multiplier differential supplies the lower-right block of the trace coordinate map. The transverse coordinate $-b$ completes that block to a full-rank differential. At the same time, the exact scalar fiber makes the boundary square Cartesian, so relative differentials and their zeroth Fitting ideals retain the full critical scheme rather than only its support.

Consequently, arbitrary labelled positive periods yield generic marked trace coordinates on the selected component, while the polynomial multiplier critical scheme is recovered with its generic component multiplicities. The exceptional nonzero values of $b$ are not determined here. A separate analysis would also be needed to formulate completed coordinates on a stack quotient or on a stabilizer-free quotient. These questions do not alter the normal-form-cover and simple-boundary conclusions established above.

# Cyclic-loop algebra edge details {#sec:appendix}

This appendix expands the cyclic coincidences and the coefficient-ring reduction used in Lemma [\[lem:finite-free\]](#lem:finite-free){reference-type="ref" reference="lem:finite-free"}. It introduces no additional theorem.

## The one-step loop {#the-one-step-loop .unnumbered}

When $n=1$, both neighboring indices of $0$ are again $0$. The general relation $$p(x_0)+b x_{-1}-x_1$$ therefore becomes $$p(x_0)+(b-1)x_0
  =
  x_0^d+\sum_{k=0}^{d-2}a_kx_0^k+(b-1)x_0.$$ The coefficient of $x_0^d$ is the unit $1\in R_d$. Division by this single monic polynomial gives the unique remainder $$c_0+c_1x_0+\cdots+c_{d-1}x_0^{d-1},
  \qquad c_i\in R_d.$$ Thus the standard monomials remain $1,x_0,\ldots,x_0^{d-1}$ even at parameter values where lower coefficients specialize or the fiber becomes nonreduced.

## The two-step loop {#the-two-step-loop .unnumbered}

For $n=2$, the predecessor and successor of $0$ both equal $1$, while those of $1$ both equal $0$. Hence the relations are exactly $$F_0=p(x_0)+(b-1)x_1,
  \qquad
  F_1=p(x_1)+(b-1)x_0.$$ Their leading monomials are $x_0^d$ and $x_1^d$. They are relatively prime in $R_d[x_0,x_1]$. The only $S$-polynomial is $$x_1^dF_0-x_0^dF_1.$$ Replacing $x_0^d$ by the lower terms from $F_0$ and $x_1^d$ by the lower terms from $F_1$ cancels the leading product and reduces the expression to zero. No division by $b-1$ or by any coefficient parameter occurs. The basis is therefore $$\{x_0^{e_0}x_1^{e_1}:0\leq e_0,e_1<d\}$$ over the entire coefficient ring, including the special value $b=1$.

## Monic reduction over the coefficient ring {#monic-reduction-over-the-coefficient-ring .unnumbered}

For general $n$, the same reasoning uses only that each leading coefficient is $1$ and that distinct leading monomials involve distinct variables. Ordinary division over a field is unnecessary. At every reduction step a leading monomial $x_j^dM$ is replaced by $$-M\left(
    \sum_{k=0}^{d-2}a_kx_j^k+b x_{j-1}-x_{j+1}
  \right),$$ which strictly lowers the chosen monomial order. Termination produces a linear combination of the standard monomials. If a standard-monomial combination belonged to the relation ideal, the leading-term ideal $(x_0^d,\ldots,x_{n-1}^d)$ would contain its leading monomial, which is impossible. This proves independence without specializing the parameters.

Because the reductions are monic, they also commute with an arbitrary base change $R_d\to R'$. The images of the standard monomials form an $R'$-basis after specialization, even if two roots collide or a fiber acquires nilpotents. What may fail after deleting lower-period and nonsimple points is properness of the resulting open over the base, not the finite freeness of the unreduced ordered-loop algebra established here.

These calculations concern full ordered loops. They do not remove lower-period points, collisions, nonsimple points, or multiplicities. They prove neither irreducibility nor an exact-cycle count, and they do not make the deleted simple exact open finite or proper over every point of $\mathcal B_d$.
