---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-mu3-rational-yukawa-surface"
canonical_tex: "henon_dynamics/henon_mu3_rational_yukawa_surface/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_mu3_rational_yukawa_surface/paper/main.pdf"
source_sha256: "add1e877c601d54f13a1d8fa819265a702f88ecca5d23399f8a4d2a41e8800a3"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Four-Parameter CY3-Type Variation and Its Rational Yukawa Cubic

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_mu3_rational_yukawa_surface>)
- [规范 TeX](<../../../../../henon_dynamics/henon_mu3_rational_yukawa_surface/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_mu3_rational_yukawa_surface/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_mu3_rational_yukawa_surface/README.md>)
- [BibTeX](<../../../../../henon_dynamics/henon_mu3_rational_yukawa_surface/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We study a rational form of a smooth quadric--cubic complete-intersection fivefold endowed with a nonconstant finite étale dihedral group scheme of rank $24$. The invariant abstract deformation space is four-dimensional. We algebraize it by taking a rational transverse slice in the smooth fixed Hilbert germ; this avoids identifying tangent representatives with a displayed linear family. The norm of the relative action graph cuts out a polarizable rank-$10$ variation in fifth cohomology. After exactly one Tate twist, its Hodge numbers are $(1,4,4,1)$, and its infinitesimal period map is an isomorphism in the first Hodge direction.

  Using the bigraded Cayley Jacobian ring, we then compute the third Gauss--Manin derivative and its polarized top pairing. Semilinear descent gives a rational projective Yukawa tensor. In a frozen rational tangent basis it has a primitive integral representative with $20$ nonzero coefficients. Its homogeneous gradient algebra has Hilbert series $(1+t)^4$ and length $16$; hence its zero locus is a smooth geometrically irreducible cubic surface over $\mathbf Q$. Projective equivalence of this cubic is a necessary local condition for realization by a four-modulus Calabi--Yau threefold variation. It is not sufficient for such a realization and yields no motivic conclusion.
author:
- 'Hilbert--Pólya Dynamical Structure Exploration Project'
bibliography:
- references.bib
date: August 2026
title: |
  A Four-Parameter CY3-Type Variation\
  and Its Rational Yukawa Cubic
```

## Markdown 正文

# Introduction {#sec:introduction}

Odd-dimensional Fano varieties can carry middle Hodge structures that look, after a Tate twist, like the third cohomology of a Calabi--Yau threefold. This phenomenon is formalized by the notion of a Fano manifold of Calabi--Yau Hodge type [@IlievManivel2015]. A particularly concrete example is a smooth complete intersection of a quadric and a cubic in $\mathbf P^7$: its variable fifth cohomology has $$h^{4,1}=h^{1,4}=1,\qquad h^{3,2}=h^{2,3}=83.$$ The precise Cayley-ring model for this fivefold is developed in [@FaveroIlievKatzarkov2014 §5].

The object studied here is a rationally descended member of this family with a finite dihedral symmetry. Averaging over the symmetry isolates a rank-$10$ middle core with Hodge multiplicities $$(4,1)^1+(3,2)^4+(2,3)^4+(1,4)^1.                 \tag{1.1}$$ Hodge numbers alone do not determine whether such a core behaves like the cohomology of a four-modulus Calabi--Yau threefold. The first genuinely differential invariant is the Yukawa cubic: the polarized third derivative of a local generator of the extreme Hodge line.

Two gaps must be closed before this invariant is meaningful. First, four invariant tangent vectors do not automatically produce a four-parameter algebraic family. We close this gap by working in the Hilbert scheme. Second, the symmetry is not a constant group of $24$ rational automorphisms. It is a nonconstant finite étale $\mathbf Q$-group scheme $\mathscr G$, split by $\mathbf Q(\rho)$. Both its relative action and its Reynolds correspondence must therefore be defined intrinsically over $\mathbf Q$.

## Main result

Let $X_0/\mathbf Q$ be the fivefold defined in [2](#sec:source){reference-type="ref" reference="sec:source"}, and let $\mathscr G$ be its rank-$24$ dihedral group form.

[\[thm:main\]]{#thm:main label="thm:main"} There are a pointed smooth algebraic $\mathbf Q$-germ $(B_{\mathrm{core}},0)$ of dimension four, a smooth projective family $$f:\mathcal X\longrightarrow B_{\mathrm{core}},$$ and a fiberwise action of $\mathscr G_{B_{\mathrm{core}}}$ such that $\mathcal X_0=X_0$ and $$\operatorname{KS}_0:T_{B_{\mathrm{core}},0}\xrightarrow{\sim}
 H^1(X_0,T_{X_0})^{\mathscr G}.                       \tag{1.2}$$ The germ is a transverse slice in the fixed Hilbert locus; the entire fixed Hilbert germ need not have dimension four.

The relative norm graph $$e_{\mathrm{rel}}
 =\frac1{24}\alpha_*[\mathscr G_{B_{\mathrm{core}}}\times_{B_{\mathrm{core}}}\mathcal X]
 \in\operatorname{CH}^5(\mathcal X\times_{B_{\mathrm{core}}}\mathcal X)_{\mathbf Q},
 \qquad \alpha(g,x)=(x,gx),                         \tag{1.3}$$ is self-transpose and idempotent. Its image $$\mathbb V_{\mathrm{core}}=
 \operatorname{im}\!\left(e_{\mathrm{rel}}:R^5f_*\mathbf Q\to R^5f_*\mathbf Q\right)(1)  \tag{1.4}$$ is a polarizable rank-$10$, weight-$3$ rational variation of Hodge structure of type $(1,4,4,1)$. Its period map is immersive at the origin.

In the rational tangent basis fixed in [6](#sec:rational-cubic){reference-type="ref" reference="sec:rational-cubic"}, the projective Yukawa tensor has the primitive integral representative $Y_H$ displayed in [\[eq:yukawa-polynomial\]](#eq:yukawa-polynomial){reference-type="ref" reference="eq:yukawa-polynomial"}. The surface $$S_H=V(Y_H)\subset\mathbf P^3_{\mathbf Q}                        \tag{1.5}$$ is smooth and geometrically irreducible.

In this paper *rational cubic* means a cubic defined over $\mathbf Q$. We do not claim that $S_H$ is a rational variety over $\mathbf Q$.

## Method and proof boundary

The algebraic family follows from three vanishing calculations, fixed-point smoothness for a linearly reductive group scheme [@Hartshorne2010; @Romagny2022], and a rational transverse-slice argument. The relative projector is the norm of the action graph and requires no relative Chow--Künneth decomposition.

The Yukawa calculation uses the complete-intersection residue ring and its perfect pairing [@Nagel1997; @Konno1991]. Four Cayley classes with different roles must remain distinct: $$\begin{array}{c|c}
\text{role}&\text{class}\\ \hline
\text{tangent operator}&[yp]\\
\text{first Hodge variation}&[y^2p]\\
\text{third Gauss--Manin variation}&[y^4p^3]\\
\text{paired top trace}&[y^5p^3].
\end{array}                                         \tag{1.6}$$ The number of Gauss--Manin derivatives is three; the fifth power of $y$ arises only after the original Hodge generator is included in the final pairing.

All variety-specific quotient ranks, semilinear descent scalars, and polynomial coefficients are checked by exact arithmetic over $\mathbf Q(\rho)$ and $\mathbf Q$. The geometric implications are proved in the text rather than delegated to computer algebra. The replay boundary and immutable release-candidate evidence tuple are recorded in [10](#sec:exact-replay){reference-type="ref" reference="sec:exact-replay"}.

## Scope

The result constructs a CY3-*type* variation; it does not construct a Calabi--Yau threefold. Projective equivalence of Yukawa cubics is necessary under a pointed polarized-VHS isomorphism, but a match does not determine the full connection, monodromy, integral lattice, or an algebraic correspondence. In particular, neither a Yukawa match nor finite-prime agreement proves a motive.

The paper is organized as follows. gives the rational fivefold and nonconstant symmetry. constructs the four-germ. builds the relative Reynolds core. proves local maximality. compute the Yukawa cubic and prove the surface theorem. state the honest-CY3 gate and comparator boundary. Exact replay data and supporting calculations occupy [\[sec:exact-replay,app:cohomology,app:cayley,app:coefficients\]](#sec:exact-replay,app:cohomology,app:cayley,app:coefficients){reference-type="ref" reference="sec:exact-replay,app:cohomology,app:cayley,app:coefficients"}.

# The rational fivefold and its nonconstant symmetry {#sec:source}

## Split and rational equation models

Put $$K=\mathbf Q(\rho),\qquad \rho^2+\rho+1=0,\qquad
 \tau(\rho)=\rho^2.$$ In split coordinates $x_0,\ldots,x_7$, consider $$C=\sum_{i=0}^7x_i^3,\qquad
 Q_\rho=\sum_{i=0}^6x_ix_{i+1}+\rho x_7x_0,\qquad
 X=V(C,Q_\rho)\subset\mathbf P^7_K.                       \tag{2.1}$$ The fivefold is smooth. A rational model $X_0=V(C_0,Q_0)\subset\mathbf P^7_\mathbf Q$, in coordinates $w_0,\ldots,w_7$, is given by $$\begin{aligned}
C_0={}&w_0^3+2w_1^3-18w_1w_2^2+2w_3^3-18w_3w_4^2\\
     &+2w_5^3-18w_5w_6^2-w_7^3,
\end{aligned}                                      \tag{2.2}$$ and $$\begin{aligned}
Q_0={}&w_0w_1+3w_0w_2+w_1w_3+3w_1w_4
       +3w_2w_3-3w_2w_4\\
     &+w_3w_5+3w_3w_6+3w_4w_5-3w_4w_6+2w_5w_7.
\end{aligned}                                      \tag{2.3}$$ To describe the descent, set $\theta=1+2\rho$, so $\theta^2=-3$. The change of coordinates $x=Bw$ is $$\begin{gathered}
x_0=w_0,\quad x_1=w_1+\theta w_2,\quad
x_7=w_1-\theta w_2,\\
x_2=w_3+\theta w_4,\quad
x_6=\rho(w_3-\theta w_4),\\
x_3=w_5+\theta w_6,\quad
x_5=w_5-\theta w_6,\quad
x_4=(1+\rho)w_7.
\end{gathered}                                      \tag{2.4}$$ Then $\det B=24\theta$ and $$C(Bw)=C_0(w),\qquad Q_\rho(Bw)=(1+\rho)Q_0(w).
\tag{2.5}
\label{eq:split-rational}$$

Let $M$ be the monomial matrix $$(Mx)_i=\rho^{\epsilon_i}x_{-i\!\!\pmod 8},\qquad
 \epsilon_i=
 \begin{cases}
 1,&i\ne0\text{ even},\\
 0,&\text{otherwise}.
 \end{cases}                                       \tag{2.6}$$ It satisfies $M\tau(M)=I$, $C(Mx)=C(x)$, and $Q_\rho(Mx)=\rho Q_{\rho^2}(x)$. Moreover $M\tau(B)=B$, which realizes [\[eq:split-rational\]](#eq:split-rational){reference-type="ref" reference="eq:split-rational"} as effective quadratic descent.

## The split dihedral action

A projective monomial transformation has the form $$x_i\longmapsto \rho^{a_i}x_{\sigma(i)}.$$ The relevant split group is $$G=\operatorname{Dih}(C_{12})
 =\langle r,s\mid r^{12}=s^2=1,\ srs=r^{-1}\rangle,
 \qquad |G|=24.                                    \tag{2.7}$$ One choice of generators is $$\begin{aligned}
r:&\quad \sigma=(6,7,0,1,2,3,4,5),&
(a_i)&=(0,1,1,0,1,0,1,0),\\
s:&\quad \sigma=(7,6,5,4,3,2,1,0),&
(a_i)&=(0,1,0,1,0,1,0,1).
\end{aligned}                                      \tag{2.8}$$ Both preserve $C=0$ and the line spanned by $Q_\rho$. The statement classifies the projective *monomial* source symmetry used here; it is not a classification of the full projective automorphism group.

Conjugation by the descent datum transports the split group through $$\delta(r)=r^{-1},\qquad \delta(s)=rs.              \tag{2.9}$$ Consequently $G$, with this Galois transport, descends to a finite étale $\mathbf Q$-group scheme $\mathscr G$ of rank $24$. It is nonconstant: only two of its geometric elements are rational points.

[\[lem:ambient-descent\]]{#lem:ambient-descent label="lem:ambient-descent"} The split projective representation descends to a morphism $$\mathscr G\longrightarrow\operatorname{PGL}_{8,\mathbf Q}
\tag{2.10}
\label{eq:ambient-action}$$ whose action preserves $X_0$.

For every $g\in G$, the exact cocycle is $$\delta(g)=M\tau(g)M^{-1}.$$ Using $M\tau(B)=B$ gives $$\tau(B^{-1}gB)=B^{-1}\delta(g)B.                  \tag{2.11}$$ Thus the conjugated split representation is equivariant for the quadratic descent datum. Effective descent gives [\[eq:ambient-action\]](#eq:ambient-action){reference-type="ref" reference="eq:ambient-action"}. Direct covariance of the two equation lines under all $24$ split elements shows that the descended action preserves the homogeneous ideal $(C_0,Q_0)$.

Here and below, summing over the group means summing over all $24$ geometric elements after a finite étale splitting base change. It never means averaging over only the two $\mathbf Q$-rational points.

# Algebraizing the equivariant deformation germ {#sec:deformation}

We now construct the base $B_{\mathrm{core}}$ in [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}. The key point is that the invariant abstract tangent space is a quotient of the invariant embedded tangent space. It is not the tangent space of the entire fixed Hilbert locus.

## Abstract and embedded unobstructedness

Adjunction gives $$K_{X_0}\simeq\mathcal O_{X_0}(-3),\qquad
 T_{X_0}\simeq\Omega^4_{X_0}(3).                   \tag{3.1}$$ Akizuki--Kodaira--Nakano vanishing, in the form [@Demailly1994 Theorem 4.11], gives $$H^2(X_0,T_{X_0})
 =H^2(X_0,\Omega^4_{X_0}(3))=0,                   \tag{3.2}$$ because $4+2>5$. The calculation may be made after base change to $\mathbf C$; faithful base change then gives the asserted rational vanishing. Thus the abstract Kuranishi germ is smooth.

Since $X_0$ is a regular complete intersection, $$N_{X_0/\mathbf P^7}
 \simeq\mathcal O_{X_0}(2)\oplus\mathcal O_{X_0}(3).$$ Kodaira vanishing yields $$H^1(X_0,N_{X_0/\mathbf P^7})=0.                         \tag{3.3}$$ The Hilbert scheme is therefore smooth at $[X_0]$, with tangent $$T_{\operatorname{Hilb}(\mathbf P^7),[X_0]}=H^0(X_0,N_{X_0/\mathbf P^7});
                                                               \tag{3.4}$$ see [@Hartshorne2010 Theorem 1.1(b),(c)].

The restricted Euler sequence and Kodaira vanishing give $$H^1(X_0,T_{\mathbf P^7}|_{X_0})=0.$$ Consequently the normal sequence induces a surjection $$\kappa:H^0(N_{X_0/\mathbf P^7})
 \twoheadrightarrow H^1(T_{X_0}).                  \tag{3.5}
\label{eq:3.5}$$ For orientation, exact Hilbert-function calculations give $$h^0(N)=35+111=146,\qquad
 h^0(T_{\mathbf P^7}|_{X_0})=63.                         \tag{3.6}
\label{eq:3.6}$$ These two numbers alone do not prove $h^1(T_{X_0})=83$, because $H^0(T_{X_0})$ also occurs in the long exact sequence.

For an independent closure, the full linearized ideal-stabilizer equations are $$\delta_AQ_\rho=\nu Q_\rho,\qquad
 \delta_AC=\mu C+LQ_\rho.                          \tag{3.7}$$ They form a coefficient matrix with $156$ rows and $74$ unknowns: $64$ entries of $A$, the two scalars $\nu,\mu$, and eight coefficients of $L$. Exact row reduction has rank $73$, and its kernel is precisely $$(A,\nu,\mu,L)=\lambda(I_8,2,3,0).                 \tag{3.8}$$ Hence the projective infinitesimal stabilizer is zero, $H^0(T_{X_0})=0$, and [\[eq:3.6\]](#eq:3.6){reference-type="ref" reference="eq:3.6"} then gives $h^1(T_{X_0})=83$. This is a Lie-algebra calculation, not a classification of the full $\operatorname{PGL}_8$-stabilizer.

## The fixed Hilbert point

By [\[lem:ambient-descent\]](#lem:ambient-descent){reference-type="ref" reference="lem:ambient-descent"}, $\mathscr G$ acts on a smooth Hilbert neighborhood of $[X_0]$. It is finite locally free of invertible order in characteristic zero and therefore linearly reductive. Romagny's fixed-point smoothness theorem [@Romagny2022 Theorems 1.2.1(2) and 4.3.6] implies that the fixed-point germ $$H^{\mathscr G}:=\operatorname{Hilb}(\mathbf P^7)^{\mathscr G}$$ is smooth at $[X_0]$. Its tangent is $$T_{H^{\mathscr G},[X_0]}=H^0(N)^{\mathscr G}.         \tag{3.9}$$ Exactness of invariants turns [\[eq:3.5\]](#eq:3.5){reference-type="ref" reference="eq:3.5"} into $$H^0(N)^{\mathscr G}\twoheadrightarrow
 H^1(T_{X_0})^{\mathscr G}.                          \tag{3.10}$$

The exact Cayley computation in [5](#sec:cayley-local){reference-type="ref" reference="sec:cayley-local"} gives $$\dim_\mathbf QH^1(T_{X_0})^{\mathscr G}=4.                \tag{3.11}$$ Choose a rational complement $$H^0(N)^{\mathscr G}=\ker(\kappa^{\mathscr G})\oplus L,
 \qquad \dim_\mathbf QL=4.                               \tag{3.12}$$ Because $H^{\mathscr G}$ is smooth over $\mathbf Q$ at a rational point, one may choose an étale coordinate chart whose differential sends $L$ to the first four coordinate axes. The inverse image of those axes is a smooth locally closed rational four-germ $(B_{\mathrm{core}},0)$. By construction, $$T_{B_{\mathrm{core}},0}=L,\qquad
 \operatorname{KS}_0:T_{B_{\mathrm{core}},0}\xrightarrow{\sim}
 H^1(T_{X_0})^{\mathscr G}.                          \tag{3.13}
\label{eq:3.13}$$

Restricting the Hilbert universal family gives $$f:\mathcal X\longrightarrow B_{\mathrm{core}}.$$ The ambient action restricts to a fiberwise $\mathscr G_{B_{\mathrm{core}}}$-action. Smoothness of the central fiber is open, so we shrink the germ and obtain a smooth projective family.

The full fixed Hilbert germ has tangent $H^0(N)^{\mathscr G}$ and retains ambient-coordinate and equation-gauge directions; it is not asserted to have dimension four. Moreover, a tangent direction represented by a cubic polynomial is not silently promoted to a literal family $C+\sum t_ip_i=Q_\rho=0$. The actual family is the restricted Hilbert universal family.

After a splitting base change and an embedding into $\mathbf C$, the completed family maps to the fixed Kuranishi germ. Both germs are smooth of dimension four and the derivative is [\[eq:3.13\]](#eq:3.13){reference-type="ref" reference="eq:3.13"}; hence the completed map is formally étale. Rim's equivariant versality theorem [@Rim1980 p. 225] supplies the compatible abstract equivariant comparison, but it is not used to algebraize the family.

# The relative Reynolds core {#sec:relative}

Set $B=B_{\mathrm{core}}$ and write $\mathscr G_B=\mathscr G\times_\mathbf QB$. The relative action defines $$\alpha:\mathscr G_B\times_B\mathcal X
\longrightarrow\mathcal X\times_B\mathcal X,\qquad
(g,x)\longmapsto(x,gx).$$ Define the norm graph $$e_{\mathrm{rel}}
 =\frac1{24}\alpha_*[\mathscr G_B\times_B\mathcal X]
 \in\operatorname{CH}^5(\mathcal X\times_B\mathcal X)_\mathbf Q.        \tag{4.1}
\label{eq:4.1}$$ This expression is intrinsic over $\mathbf Q$; it does not require $24$ individual rational graph cycles.

[\[prop:relative-projector\]]{#prop:relative-projector label="prop:relative-projector"} The cycle $e_{\mathrm{rel}}$ is self-transpose and idempotent.

After the finite étale splitting base change, $$e_{\mathrm{rel}}=\frac1{24}\sum_{g\in G}\Gamma_g.$$ In the square of the sum, every graph $\Gamma_k$ occurs exactly $24$ times because $gh=k$ has $24$ solutions. This proves idempotence. Moreover ${}^t\Gamma_g=\Gamma_{g^{-1}}$, and inversion permutes the group, so the sum is self-transpose. The two cycle identities descend faithfully to $\mathbf Q$.

An algebraic relative correspondence acts horizontally on $R^5f_*\mathbf Q$ and preserves its Hodge filtration. Thus $$\mathbb W:=\operatorname{im}\!\left(
 e_{\mathrm{rel}}:R^5f_*\mathbf Q\longrightarrow R^5f_*\mathbf Q
 \right)                                           \tag{4.2}$$ is a rational sub-variation. Since $e_{\mathrm{rel}}$ is self-transpose, the restriction of the middle polarization to its image is nondegenerate.

At the central fiber, the action of [\[eq:4.1\]](#eq:4.1){reference-type="ref" reference="eq:4.1"} on $H^5$ is the Reynolds average already used to isolate the middle core. Inserting the central middle Chow--Künneth projector $\pi_5$ does not change its action on $H^5$. The central rank and Hodge ledger are therefore $$\operatorname{rank}\mathbb W=10,\qquad
 (h^{4,1},h^{3,2},h^{2,3},h^{1,4})=(1,4,4,1).
                                                               \tag{4.3}$$ After shrinking the connected germ, all four ranks are locally constant.

[\[thm:vhs\]]{#thm:vhs label="thm:vhs"} The Tate twist $$\mathbb V_{\mathrm{core}}=\mathbb W(1)                               \tag{4.4}$$ is a polarizable rational variation of Hodge structure of weight $3$, rank $10$, and Hodge type $$(h^{3,0},h^{2,1},h^{1,2},h^{0,3})=(1,4,4,1).
 \tag{4.5}
\label{eq:4.5}$$

The untwisted variation has weight $5$. The convention $\mathbf Q(1):(p,q)\mapsto(p-1,q-1)$ sends $$(4,1),(3,2),(2,3),(1,4)
 \longmapsto(3,0),(2,1),(1,2),(0,3).$$ It lowers the weight by two and gives [\[eq:4.5\]](#eq:4.5){reference-type="ref" reference="eq:4.5"}. Polarizability follows from the nondegenerate restriction described above.

Exactly one Tate twist occurs. A twist by $\mathbf Q(2)$ would give the wrong weight and Hodge types. We also emphasize that [\[eq:4.1\]](#eq:4.1){reference-type="ref" reference="eq:4.1"} acts directly on $R^5f_*\mathbf Q$; no relative Chow--Künneth projector is constructed or used.

# Cayley operators and local maximality {#sec:cayley-local}

## The bigraded Jacobian ring

Over $K$, introduce auxiliary variables $y,z$ and set $$F=yC+zQ_\rho.$$ Give the polynomial ring the bigrading $$\deg x_i=(0,1),\qquad
 \deg y=(1,-3),\qquad
 \deg z=(1,-2).                                    \tag{5.1}$$ Let $$R=K[x_0,\ldots,x_7,y,z]/J(F),                     \tag{5.2}$$ where $J(F)$ is the full Jacobian ideal. Nagel's residue identification [@Nagel1997 Definition 2.15 and Proposition 2.16] specializes to $$H_{\mathrm{var}}^{5-p,p}(X)\simeq R_{p,-3}.
                                                               \tag{5.3}$$ In particular, $$H^{4,1}_{\mathrm{var}}\simeq R_{1,-3}=K[y],
 \qquad
 H^{3,2}_{\mathrm{var}}\simeq R_{2,-3}.            \tag{5.4}$$

The embedded deformation operator belongs to a different component: $$H^1(T_X)\simeq R_{1,0}.                            \tag{5.5}
\label{eq:5.5}$$ If $p$ is a cubic tangent representative, its operator class is $[yp]\in R_{1,0}$. Acting on the extreme Hodge generator $\omega=[y]\in R_{1,-3}$ gives $$[yp]\cdot[y]=[y^2p]\in R_{2,-3}.                  \tag{5.6}$$ This is the multiplication realization of infinitesimal variation in [@Nagel1997 Lemma 3.1] and [@Konno1991 Theorem 6.1(2),(3)].

## Exact tangent calculation

The ambient bidegree-$(1,0)$ component has dimension $$120+36=156,$$ coming from $y$ times cubics and $z$ times quadrics. The Jacobian relations have rank $73$, hence $$\dim_KR_{1,0}=83.                                  \tag{5.7}$$ Multiplication by $y$ gives an $83\times83$ matrix $$m_y:R_{1,0}\longrightarrow R_{2,-3},\qquad
 [yp]\longmapsto[y^2p],                             \tag{5.8}
\label{eq:5.8}$$ of exact rank $83$. Thus $m_y$ is an isomorphism.

The group action on residues contains the determinant correction $$\omega(g)=\frac{\det M_g}{\det A_g},$$ where $$\binom C{Q_\rho}(M_gx)=A_g\binom C{Q_\rho}(x).
                                                               \tag{5.9}$$ This correction makes the action independent of the scalar lift of the projective map. Averaging four frozen seed monomials gives a four-dimensional invariant subspace of $R_{2,-3}$. The exact all-$24$ Reynolds computation and quadratic semilinear descent give $$\dim_\mathbf QR_{2,-3}^{\mathscr G}=4.                    \tag{5.10}$$ By [\[eq:5.5\]](#eq:5.5){reference-type="ref" reference="eq:5.5"}, this is $\dim_\mathbf QH^1(T_{X_0})^{\mathscr G}=4$, as used in [3](#sec:deformation){reference-type="ref" reference="sec:deformation"}.

[\[thm:local-maximality\]]{#thm:local-maximality label="thm:local-maximality"} Contraction by a generator of $F^3{\mathbb V_{\mathrm{core}}}_0$ induces an isomorphism $$T_{B_{\mathrm{core}},0}\xrightarrow{\sim}
 F^2{\mathbb V_{\mathrm{core}}}_0/F^3{\mathbb V_{\mathrm{core}}}_0.                     \tag{5.11}$$ Consequently the projected period map is immersive at $0$, and after shrinking $B_{\mathrm{core}}$ it is a local immersion.

The Kodaira--Spencer map identifies $T_{B_{\mathrm{core}},0}$ with the invariant part of $R_{1,0}$. The extreme Hodge generator is $[y]$. The isomorphism $m_y$ in [\[eq:5.8\]](#eq:5.8){reference-type="ref" reference="eq:5.8"} restricts to an isomorphism on the four invariant directions and sends them to the invariant $(3,2)$-piece before twisting, equivalently to $F^2/F^3$ after $\mathbf Q(1)$. This is exactly the differential of the period map.

Once a tangent operator has acted on $[y]$, the resulting class lies in $R_{2,-3}$. It is not legitimate to multiply such already contracted classes inside that same bidegree and call the result higher infinitesimal variation. This distinction is explicit in the complete-intersection discussion of [@FaveroIlievKatzarkov2014 §5.6]. Higher derivatives below are formed by repeatedly applying the original $R_{1,0}$ operators.

# The rational projective Yukawa cubic {#sec:rational-cubic}

## Third variation and the top pairing

Let $v_i=[yp_i]\in R_{1,0}$ be tangent operators and let $\omega=[y]\in R_{1,-3}$. Repeated operator application has the bidegree ledger $$\begin{array}{c|c|c}
\text{stage}&\text{class}&\text{component}\\ \hline
\omega&[y]&R_{1,-3}\\
v_i\omega&[y^2p_i]&R_{2,-3}\\
v_jv_i\omega&[y^3p_ip_j]&R_{3,-3}\\
v_kv_jv_i\omega&[y^4p_ip_jp_k]&R_{4,-3}.
\end{array}                                         \tag{6.1}$$ The perfect residue pairing is $$R_{1,-3}\times R_{4,-3}\longrightarrow R_{5,-6}\simeq K.
                                                               \tag{6.2}$$ It is the Cayley-ring realization of the polarized Hodge pairing; see [@Konno1991 Theorem 6.1(4) and Lemma 6.2]. Therefore the symmetric Yukawa tensor is, up to one common nonzero residue normalization, $$Y_{ijk}=\operatorname{Tr}\!\left(y^5p_ip_jp_k\right).            \tag{6.3}
\label{eq:6.3}$$ The last factor $y$ comes from pairing the third variation with $\omega$; it is not a fourth derivative. Residue constants at successive Hodge stages depend only on the stage, so their product rescales every entry of [\[eq:6.3\]](#eq:6.3){reference-type="ref" reference="eq:6.3"} by the same nonzero scalar. No direction-dependent normalization is allowed.

## Semilinear descent of the top line

On polynomial representatives, the descent operator is $$D(p)(x)=\tau(p)(M^{-1}x),\qquad
 D(C)=C,\qquad D(Q_\rho)=\rho^2Q_\rho.              \tag{6.4}$$ Compatibility with $F=yC+zQ_\rho$ forces $$D(y)=y,\qquad D(z)=\rho z,\qquad D(F)=F.           \tag{6.5}$$ In particular, $D(z)=\rho^2z$ is the wrong extension.

The exact quotient calculation gives $$\dim_KR_{5,-6}=1.                                  \tag{6.6}$$ In the producer term order, a top standard monomial is $$m_{\mathrm{top}}=x_6^2x_7^2z^5.$$ Under $D$, the $x$-part contributes $\rho$, the $z^5$-part contributes $\rho^2$, and hence the raw image is $$D(m_{\mathrm{top}})=x_1^2x_2^2z^5                \tag{6.7}$$ with total prefactor $1$. The raw monomial is not fixed. Reducing the image in $R_{5,-6}$ gives $$D(m_{\mathrm{top}})=d\,m_{\mathrm{top}},\qquad
 d=\frac{
 1314394345202493849331539+
 420337540641585096809035\,\rho}
 {1162680891851795197142359}.                      \tag{6.8}$$ Exact arithmetic verifies $$d\,\tau(d)=1.                                     \tag{6.9}$$ Hilbert 90 therefore gives a $K^\times$-rescaling of $m_{\mathrm{top}}$ fixed by $D$, and hence a one-dimensional $\mathbf Q$-form of the top line. The frozen certificate records one such rescaling. Only the resulting projective tensor is intrinsic.

## A rational tangent basis

Let $\mathcal R_G$ denote the Reynolds operator on $R_{2,-3}$. Define $$\begin{aligned}
e_0&=\mathcal R_G[y^2x_3x_5x_7],&
e_1&=\mathcal R_G[y^2x_3^2x_5],\\
e_2&=\mathcal R_G[y^2x_2^2x_6],&
e_3&=\mathcal R_G[y^2x_2^2x_4].
\end{aligned}                                      \tag{6.10}$$ These four classes are independent and $G$-invariant. Their semilinear fixed $\mathbf Q$-basis is $$\begin{aligned}
q_0&=e_0,&
q_1&=e_1+e_3,\\
q_2&=(1+2\rho)(e_1-e_3),&
q_3&=-\rho e_2.
\end{aligned}                                      \tag{6.11}
\label{eq:6.11}$$ The normalization $q_0=e_0$, rather than $2e_0$, is fixed throughout. Using the isomorphism $m_y$ in [\[eq:5.8\]](#eq:5.8){reference-type="ref" reference="eq:5.8"}, let the corresponding tangent operators be $[yp_0],\ldots,[yp_3]$.

For $v(u)=\sum_{i=0}^3u_i[yp_i]$, define $$Y_H(u)=Y(v(u),v(u),v(u)).$$ Thus a tensor entry with index multiset $iij$ occurs in the polynomial with multiplicity $3$, and an entry $ijk$ with three distinct indices occurs with multiplicity $6$.

[\[thm:yukawa\]]{#thm:yukawa label="thm:yukawa"} Up to a common nonzero scalar, the Yukawa tensor in the basis [\[eq:6.11\]](#eq:6.11){reference-type="ref" reference="eq:6.11"} has the primitive integral representative $$\tag{6.12}
\label{eq:yukawa-polynomial}
\begin{aligned}
Y_H={}&75081586157u_0^3-28576620789u_0^2u_1
+164150208636u_0u_1^2+6898957820u_1^3\\
&-122000922135u_0^2u_2-415458334296u_0u_1u_2
+1132596902196u_1^2u_2\\
&+1158143874300u_0u_2^2-2054867641020u_1u_2^2
+2646295985484u_2^3\\
&-5364921951u_0^2u_3+151070718312u_0u_1u_3
-30413540316u_1^2u_3\\
&+114691988016u_0u_2u_3+151980984216u_1u_2u_3
+560186573940u_2^2u_3\\
&+113572676646u_0u_3^2+36794420832u_1u_3^2
+706181383584u_2u_3^2+1884468968u_3^3.
\end{aligned}$$ Its coefficient gcd is one.

All $20$ unordered products $y^5p_ip_jp_k$ reduce to the top line. Semilinear fixedness of the basis and of the chosen top trace makes all coefficient ratios rational. Clearing denominators and dividing by the coefficient gcd produces a primitive integral cubic, unique up to sign; the sign is fixed by requiring the $u_0^3$-coefficient to be positive.

The exact producer reduces the cubic at $20$ interpolation points. Independently, the checker reduces all $20$ unordered traces, inserts the $1/3/6$ multiplicities, and reconstructs the same polynomial. It also repeats the raw trace calculation in a different top gauge and obtains one common nonzero $K^\times$-ratio across all entries. The resulting coefficients are those in [\[eq:yukawa-polynomial\]](#eq:yukawa-polynomial){reference-type="ref" reference="eq:yukawa-polynomial"}; the normalized tensor entries are listed in [14](#app:coefficients){reference-type="ref" reference="app:coefficients"}.

# The Yukawa cubic surface {#sec:cubic-surface}

Let $$S=\mathbf Q[u_0,u_1,u_2,u_3],\qquad
 J_{\nabla Y_H}
 =(\partial_{u_0}Y_H,\ldots,\partial_{u_3}Y_H).$$ The four generators are homogeneous quadrics. Exact Gröbner reduction gives $$\operatorname{Hilb}_{S/J_{\nabla Y_H}}(t)=(1+t)^4
 =1+4t+6t^2+4t^3+t^4.
\tag{7.1}
\label{eq:gradient-hilbert}$$ Equivalently, the Hilbert numerator over $S$ is $$1-4t^2+6t^4-4t^6+t^8,                            \tag{7.2}$$ and $$\dim_\mathbf QS/J_{\nabla Y_H}=16.                      \tag{7.3}$$ The producer obtains a $12$-element Gröbner basis in degree-reverse lexicographic order. An independent computation reverses both the variable and Jacobian-generator orders and obtains the same length and Hilbert numerator.

[\[thm:cubic-surface\]]{#thm:cubic-surface label="thm:cubic-surface"} The cubic surface $$S_H=V(Y_H)\subset\mathbf P^3_\mathbf Q$$ is smooth over $\overline{\mathbf Q}$ and geometrically irreducible.

The finite-dimensional quotient in [\[eq:gradient-hilbert\]](#eq:gradient-hilbert){reference-type="ref" reference="eq:gradient-hilbert"} shows that the homogeneous partial derivatives have no common nonzero zero over an algebraic closure. Hence the projective singular locus is empty and $S_H$ is geometrically smooth.

Suppose $Y_H$ factored over $\overline{\mathbf Q}$ as $GH$, with both factors of positive degree. The two projective hypersurfaces $V(G)$ and $V(H)$ meet in $\mathbf P^3_{\overline{\mathbf Q}}$. At any intersection point, $$\nabla(GH)=H\nabla G+G\nabla H=0,$$ contradicting smoothness. Thus $Y_H$ is geometrically irreducible.

The independent exact backend also finds a single degree-$3$ factor over $\mathbf Q$, but rational factorization alone is not the proof of geometric irreducibility. Conversely, the theorem makes no claim that the $\mathbf Q$-defined surface is $\mathbf Q$-rational as a variety. The intrinsic object is the projective pair $$\bigl(\mathbf P(T_{B_{\mathrm{core}},0}),\,V([Y_H])\bigr);$$ a change of rational tangent basis acts by $\operatorname{PGL}_4(\mathbf Q)$, and a common trace normalization leaves its zero locus unchanged.

# A necessary gate for an honest CY3 realization {#sec:realization}

The cubic in [\[thm:yukawa\]](#thm:yukawa){reference-type="ref" reference="thm:yukawa"} is an invariant of the pointed polarized variation, up to projective tangent change and a common scalar. It therefore supplies a one-sided realization obstruction.

[\[thm:realization-gate\]]{#thm:realization-gate label="thm:realization-gate"} Let $g:Y\to T$ be a smooth projective family of Calabi--Yau threefolds with $h^{2,1}=4$. Suppose there are an isomorphism of pointed complex base germs $$\phi:(T,t)\xrightarrow{\sim}(B_{\mathrm{core}},0)$$ and an isomorphism of polarized rational variations of Hodge structure $$\Phi:R^3g_*\mathbf Q\xrightarrow{\sim}\phi^*\mathbb V_{\mathrm{core}}.       \tag{8.1}
\label{eq:8.1}$$ If $A=d\phi_t$, then the two Yukawa cubics satisfy $$Y_Y(v)=\lambda\,Y_H(Av)
 \quad\text{for some }\lambda\in\mathbf C^\times.         \tag{8.2}
\label{eq:8.2}$$ Thus failure of projective $\operatorname{GL}_4(\mathbf C)$-equivalence is a pointed local polarized-VHS obstruction.

The isomorphism $\Phi$ is horizontal, filtration-preserving, and polarization-preserving. It identifies the one-dimensional $F^3$ lines. Choose local generators $\Omega_Y$ and $\Omega_H$; at the base point their images differ by a nonzero scalar. Horizontality intertwines the three Gauss--Manin derivatives, and the base-germ isomorphism transports directions through $A$. Pairing the third derivative with the original Hodge generator gives [\[eq:8.2\]](#eq:8.2){reference-type="ref" reference="eq:8.2"}; the two choices of generator contribute only a common nonzero scalar. This is the functoriality of the generalized Yukawa tensor used for manifolds of Calabi--Yau Hodge type [@IlievManivel2015 §2].

Projective equality of one cubic at one point does not identify the higher Yukawa jets, the full Gauss--Manin connection, monodromy, the integral lattice, or an algebraic correspondence. A central-fiber Hodge correspondence is likewise insufficient: an algebraic correspondence would support [\[thm:realization-gate\]](#thm:realization-gate){reference-type="ref" reference="thm:realization-gate"} only if it extended relatively and induced the horizontal isomorphism [\[eq:8.1\]](#eq:8.1){reference-type="ref" reference="eq:8.1"}. No Hodge, Yukawa, or finite-prime match alone proves an isomorphism of motives.

This gives a useful hierarchy of tests: $$\begin{array}{c}
\text{projective cubic}\\
\Downarrow\\
\text{higher jets and full connection}\\
\Downarrow\\
\text{monodromy and integral structure}\\
\Downarrow\\
\text{relative algebraic correspondence}.
\end{array}$$ Failure at any gate rules out every stronger claim below it. Passage downward from a weaker match to a stronger conclusion requires new evidence.

# Comparator scope {#sec:comparators}

Braun, Candelas, and Davies construct smooth quotients by $\operatorname{Dic}_3$ and $\mathbf Z_{12}$, both with $$(h^{1,1},h^{2,1})=(1,4)$$ and four projective complex-structure parameters [@BraunCandelasDavies2010]. These are natural honest-CY3 candidates for [\[thm:realization-gate\]](#thm:realization-gate){reference-type="ref" reference="thm:realization-gate"}. Their paper explicitly leaves Yukawa couplings undiscussed. It also identifies the enhanced $\operatorname{Dih}_6$ locus $c_0=c_1=0$; the generic member of that locus has three nodes and is not a smooth substitute.

The later special-geometry calculation [@BraunCandelasDelaOssa2015] studies the one-parameter complex-structure variation of the mirror, equivalently the one-Kähler-parameter special geometry on the original side, and computes a scalar Yukawa coupling. It is not the full four-variable B-model tensor required here, and we do not identify it with a restriction of that tensor. The small-Hodge catalogue [@CandelasConstantinMishra2018] records the candidate families but does not provide the missing tensor or a uniqueness theorem.

A bounded search of the primary literature located no published full four-variable B-model Yukawa tensor for either quotient. We therefore make no named comparison and assign the exact status $$\boxed{\text{\rm NOT-COMPARABLE-WITH-CURRENT-DATA}.}$$ Promotion of a comparator would require both a full four-variable tensor and an exact incidence calculation $$Y_{\mathrm{candidate}}(c;u)
 =\lambda\,Y_H(Au),\qquad
 A\in\operatorname{GL}_4(\mathbf C),\quad\lambda\ne0.$$ Hodge-number agreement, a mirror-side one-parameter calculation, or a nodal enhanced-symmetry locus does not meet this gate.

# Exact replay and evidence boundary {#sec:exact-replay}

The deformation, correspondence, Hodge, and geometric arguments in [\[sec:deformation,sec:relative,sec:cubic-surface\]](#sec:deformation,sec:relative,sec:cubic-surface){reference-type="ref" reference="sec:deformation,sec:relative,sec:cubic-surface"} are written proofs. Exact computation supplies the finite, instance-specific inputs: quotient ranks, all-$24$ covariance, semilinear fixed spaces, top-line reduction, the $20$ tensor entries, and the gradient algebra.

## Independent finite gates

The project-local replay has four layers.

1.  The producer reconstructs the source ring over $K=\mathbf Q(\rho)$, enumerates the group, computes the quotient components, and emits a canonical certificate.

2.  The checker independently rebuilds the group action, tangent quotients, infinitesimal stabilizer, top line, Yukawa reductions, and gradient algebra. It does not accept producer conclusion fields as premises.

3.  A complete scalar-leaf classifier separates central semantic leaves, independently derived leaves, and explicitly nonsemantic chronology. Every central leaf is rebound after both enclosing digests are recomputed.

4.  A rollback-atomic runner builds and checks temporary artifacts before grouped promotion. Failure injections verify zero residual `.new`/`.bak` files. This is an exception-safety claim, not a power-loss durability claim.

The $13$ executed semantic gates are summarized below.

  Gate family                  Exact result
  ---------------------------- ----------------------------------------------------------------------------------------------------------------------------
  Envelope and provenance      Canonical payload and schema digests; committed HCS-C52--C54 dependency tuples
  Complete intersection        $156\times74$ linearized ideal matrix, rank $73$, unique kernel $\lambda(I_8,2,3,0)$
  Equivariant tangent          $R_{1,0}$ dimension $83$, four Reynolds directions, four-dimensional semilinear $\mathbf Q$-form
  First variation              Multiplication by $y$ has rank $83$ and carries all four frozen operator lifts to their first images
  Ambient and Cayley descent   $576$ group-table automorphism tests, $48$ equation-line covariance tests, $D(z)=\rho z$, and exact top cocycle
  Yukawa                       $20$ direct cubic evaluations, $20$ unordered traces, full-rank interpolation, and $1/3/6$ reconstruction
  Independent raw gauge        Reversed Jacobian-generator order and a different top monomial give one common nonzero $K^\times$-ratio across all entries
  Cubic surface                Primitive coefficient gcd $1$, gradient length $16$, Hilbert numerator $1-4t^2+6t^4-4t^6+t^8$
  Scope                        Wrong Tate twist, literal-family, fixed-Hilbert, honest-CY3, motive, and wrong-$D(z)$ mutations all fail closed

The independent Yukawa backend uses the weighted order $\mathrm{Wp}(1,1,1,1,1,1,1,1,1,2)$ with reversed Jacobian-generator order and a top gauge different from the producer's. The independent smoothness backend uses degree reverse lexicographic order with reversed variables and partial-derivative order. No cached Gröbner basis is shared.

## Frozen release-candidate tuple

The replay passes $13/13$ named gates and $15/15$ test methods. The certificate contains $1589$ scalar leaves, partitioned exactly as $$1589=292\ \text{central}+1296\ \text{derived}
      +1\ \text{chronology-only}.                  \tag{10.1}$$ The tests mutate every one of the $292$ central leaves while rebinding payload and schema hashes. They also include duplicate-key, unknown-key, type-confusion, optimized-Python, stale-output, and rollback controls.

The immutable release-candidate code/results identifiers used by this manuscript are:

  ----------------------- ------------------------------------------------------------------
  payload                 6afc529d2ab9e849592d9eba7b76324cc7a840670f50c669f90fdd079c0b4323
  certificate             aa6a57bc496d78afd5728640083179bb0dd24963deb44e31459c59edc71c381f
  independent check       e24c90fac1b222ed161eec677c06209c901f0decc335e769dc7df4ce53c68469
  schema                  2961eb6b5b4aefa0e12ffcb59c9e1095b14f0309e2045fd6d8a7f636dc6dca53
  code/results manifest   7f1fa8bc6f22dd89b6b9a41ae2353129853f39430ba932f048ff295e56ba30e6
  ----------------------- ------------------------------------------------------------------

The last line is the digest of `results/CODE_RESULTS_HASHES.sha256`. Its $11$ entries bind seven code files and four result files while excluding both manifest files. The producer and checker digests are, respectively, $$\begin{aligned}
&\texttt{3975ad77301939f23754920643b3baa205d67f1451791db3643df693d99c27ba},\\
&\texttt{38d7c144389ba116fc9f6d52bb4327cbe4479f7b7ac71f447c406e69c633834b}.
\end{aligned}$$

The test-suite digest is

`ccff76d883b2511a2f7491ed28a3f0af2384af2777c402829ef72de6cdf82281`.

The promotion changed only the top-level artifact status. Removing that field from the prefreeze and release-candidate payloads gives the same 30,949-byte canonical mathematical subpayload, with SHA-256 `a3da70ceaea6f0ac270cb746a78840ca63367e9b01e02835ad6020e4c76f37ec`.

The code/results lane was promoted to `RELEASE_CANDIDATE` before the official paper build. The persistent 11-entry scoped manifest is the default identity for that build and release. The current 47-entry full-project successor is verified separately under an external-only hash policy, so it does not create a self-hash cycle or replace the embedded scoped identity. The implementation commit is a later provenance stage and is not a theorem input.

## Negative claim boundary

Computer algebra does not prove the existence of the relative family, the horizontal VHS splitting, or the motivic implications excluded in [8](#sec:realization){reference-type="ref" reference="sec:realization"}. The result makes no claim of a literal linear family, a four-dimensional full fixed Hilbert germ, a relative Chow--Künneth decomposition, an honest Calabi--Yau threefold, a $\mathbf Q$-rational cubic surface, or a motive. The comparator branch remains at the status in [9](#sec:comparators){reference-type="ref" reference="sec:comparators"}.

# Declarations {#sec:declarations}

#### Data and code availability.

No external dataset, numerical fit, or trained parameter is used. The exact producer, independent checker, mutation suite, and certificates are maintained inside the HCS-C55 project directory. records the immutable scoped code/results tuple used for the manuscript. The implementation commit remains a later provenance stage and must not alter the frozen mathematics or paper.

#### Primary-source audit.

Bibliographic metadata, theorem and section locators, and local source-copy digests are recorded in the project-local source audit. The comparator search is a bounded primary-literature screen, not a systematic review or an exhaustive priority certificate.

#### Computational boundary.

Machine calculations certify finite exact algebra and adversarial schema behavior. The deformation, descent, correspondence, Hodge, smoothness, and realization implications are written mathematical arguments.

#### Author contributions.

The work was carried out collaboratively: conceptualization, formal analysis, exact verification design, source control, writing, and curation.

#### Competing interests.

The authors declare no competing interests.

#### Funding.

No external funding is declared for this project.

#### Ethics.

The work uses no human participants, animal subjects, or personal data.

# Cohomology and the transverse-slice lemma {#app:cohomology}

## Line-bundle cohomology

For a $(2,3)$ complete intersection in $\mathbf P^7$, the homogeneous coordinate-ring Hilbert series is $$\frac{(1-t^2)(1-t^3)}{(1-t)^8}.$$ Its first values are $$h^0(\mathcal O_{X_0})=1,\quad
 h^0(\mathcal O_{X_0}(1))=8,\quad
 h^0(\mathcal O_{X_0}(2))=35,\quad
 h^0(\mathcal O_{X_0}(3))=111.                    \tag{A.1}$$ The normal bundle therefore has $146$ global sections.

For $k=0,1,2,3$, $$\mathcal O_{X_0}(k)
 =K_{X_0}\otimes\mathcal O_{X_0}(k+3),$$ and the second factor is ample. Kodaira vanishing gives $$H^q(X_0,\mathcal O_{X_0}(k))=0\qquad(q>0).
 \tag{A.2}
\label{eq:A.2}$$ In particular $H^1(N)=0$. Restricting the Euler sequence, $$0\longrightarrow\mathcal O_{X_0}
 \longrightarrow\mathcal O_{X_0}(1)^{\oplus8}
 \longrightarrow T_{\mathbf P^7}|_{X_0}
 \longrightarrow0,                                 \tag{A.3}$$ and using [\[eq:A.2\]](#eq:A.2){reference-type="ref" reference="eq:A.2"} gives $$H^1(T_{\mathbf P^7}|_{X_0})=0,\qquad
 h^0(T_{\mathbf P^7}|_{X_0})=8\cdot8-1=63.              \tag{A.4}$$

The normal sequence then has the exact segment $$\begin{aligned}
0\to H^0(T_{X_0})\to H^0(T_{\mathbf P^7}|_{X_0})
\to H^0(N)\to H^1(T_{X_0})\to0.
\end{aligned}                                      \tag{A.5}$$ The exact ideal-stabilizer calculation gives $H^0(T_{X_0})=0$; therefore $$h^1(T_{X_0})=146-63=83.                           \tag{A.6}$$ The order is essential: the subtraction is valid only after the vector-field kernel has been proved to vanish.

## A rational slice

We isolate the elementary algebraic step used in [3](#sec:deformation){reference-type="ref" reference="sec:deformation"}.

[\[lem:rational-slice\]]{#lem:rational-slice label="lem:rational-slice"} Let $H/\mathbf Q$ be smooth at a rational point $h$, let $W$ be a finite dimensional $\mathbf Q$-space, and let $$\kappa:T_{H,h}\twoheadrightarrow W$$ be a rational surjection. If $L\subset T_{H,h}$ is a rational complement to $\ker\kappa$, then there is a smooth locally closed rational germ $(B,h)\subset(H,h)$ such that $T_{B,h}=L$ and $\kappa|_{T_{B,h}}$ is an isomorphism.

Let $n=\dim H$ and $d=\dim W$. Smoothness supplies an étale map $\psi:(H,h)\to(\mathbf A^n,0)$. Compose with a rational linear automorphism of $\mathbf A^n$ so that $d\psi_h(L)$ is the span of the first $d$ coordinate vectors. Let $A=\mathbf A^d\times\{0\}\subset\mathbf A^n$, and take $$(B,h)=\bigl(\psi^{-1}(A),h\bigr).$$ Étaleness makes $B$ smooth of dimension $d$ and gives $T_{B,h}=L$. The restriction of $\kappa$ is an isomorphism by the choice of $L$.

Apply the lemma with $H=\operatorname{Hilb}(\mathbf P^7)^{\mathscr G}$, $W=H^1(T_{X_0})^{\mathscr G}$, and $\kappa$ the invariant embedded Kodaira--Spencer map. This produces $B_{\mathrm{core}}$ without placing equations on a guessed linear deformation.

# Cayley and normalization ledger {#app:cayley}

## Components and roles

  Object             Component    Meaning
  ------------------ ------------ ---------------------------
  $[y]$              $R_{1,-3}$   generator of $H^{4,1}$
  $[yp]$             $R_{1,0}$    deformation operator
  $[y^2p]$           $R_{2,-3}$   first Hodge variation
  $[y^3p_ip_j]$      $R_{3,-3}$   second Hodge variation
  $[y^4p_ip_jp_k]$   $R_{4,-3}$   third Hodge variation
  $[y^5p_ip_jp_k]$   $R_{5,-6}$   top product after pairing

The perfect top pairing is $$R_{1,-3}\otimes R_{4,-3}\longrightarrow R_{5,-6}.$$ The C55 fivefold lies in neither the K3 exception of [@Konno1991 Theorem 6.1(2)] nor the odd-dimensional $(2,2)$ exception of [@Konno1991 Theorem 6.1(4)]. Thus the operator identification and pairing apply exactly in the required components.

## Frozen directions

The four seed monomials, before the Reynolds average, are $$\begin{array}{c|c}
a&m_a\\ \hline
0&x_3x_5x_7\\
1&x_3^2x_5\\
2&x_2^2x_6\\
3&x_2^2x_4.
\end{array}                                         \tag{B.1}$$ Writing $e_a=\mathcal R_G[y^2m_a]$, the rational basis is $$(q_0,q_1,q_2,q_3)
 =(e_0,\ e_1+e_3,\ (1+2\rho)(e_1-e_3),\ -\rho e_2).
 \tag{B.2}
\label{eq:B.2}$$ The certificate stores all sparse reduced representatives of the $e_a$, checks invariance under every group element, and verifies the semilinear cocycle on the span. Multiplication by $y$ is an isomorphism, so [\[eq:B.2\]](#eq:B.2){reference-type="ref" reference="eq:B.2"} determines unique operator classes in $R_{1,0}$.

## Normalization conventions

For an unordered triple $i\le j\le k$, let $T_{ijk}$ denote the symmetric tensor entry after a common projective normalization. The coefficient of the corresponding monomial in $Y_H(u)=Y_H(v(u),v(u),v(u))$ is $$\begin{cases}
 T_{iii},&i=j=k,\\
 3T_{iij},&\text{exactly two indices coincide},\\
 6T_{ijk},&i,j,k\text{ are distinct}.
 \end{cases}                                       \tag{B.3}$$ The common residue and top-line normalization is allowed to rescale all $T_{ijk}$ together. It cannot change one direction independently.

The semilinear convention is $$D(C)=C,\qquad D(Q_\rho)=\rho^2Q_\rho,\qquad
 D(y)=y,\qquad D(z)=\rho z.                        \tag{B.4}$$ For the producer top gauge, the raw action is $$x_6^2x_7^2z^5\longmapsto x_1^2x_2^2z^5
\longmapsto d\,x_6^2x_7^2z^5
 \quad\text{in }R_{5,-6}.                          \tag{B.5}$$ The first arrow must not be replaced by a claim that the raw standard monomial is fixed. The quotient-reduction scalar $d$ satisfies $d\tau(d)=1$, which is the exact descent criterion for the top line.

# Tensor coefficients and gradient quadrics {#app:coefficients}

## All symmetric tensor entries

The following table lists the $20$ entries after the primitive projective normalization of [\[eq:yukawa-polynomial\]](#eq:yukawa-polynomial){reference-type="ref" reference="eq:yukawa-polynomial"}. The final column is the ordinary polynomial coefficient, including the indicated multinomial factor.

    $(i,j,k)$   multiplicity         $T_{ijk}$   coefficient in $Y_H$
  ----------- -------------- ----------------- ----------------------
    $(i,j,k)$   multiplicity         $T_{ijk}$   coefficient in $Y_H$
    $(0,0,0)$              1     $75081586157$          $75081586157$
    $(0,0,1)$              3     $-9525540263$         $-28576620789$
    $(0,0,2)$              3    $-40666974045$        $-122000922135$
    $(0,0,3)$              3     $-1788307317$          $-5364921951$
    $(0,1,1)$              3     $54716736212$         $164150208636$
    $(0,1,2)$              6    $-69243055716$        $-415458334296$
    $(0,1,3)$              6     $25178453052$         $151070718312$
    $(0,2,2)$              3    $386047958100$        $1158143874300$
    $(0,2,3)$              6     $19115331336$         $114691988016$
    $(0,3,3)$              3     $37857558882$         $113572676646$
    $(1,1,1)$              1      $6898957820$           $6898957820$
    $(1,1,2)$              3    $377532300732$        $1132596902196$
    $(1,1,3)$              3    $-10137846772$         $-30413540316$
    $(1,2,2)$              3   $-684955880340$       $-2054867641020$
    $(1,2,3)$              6     $25330164036$         $151980984216$
    $(1,3,3)$              3     $12264806944$          $36794420832$
    $(2,2,2)$              1   $2646295985484$        $2646295985484$
    $(2,2,3)$              3    $186728857980$         $560186573940$
    $(2,3,3)$              3    $235393794528$         $706181383584$
    $(3,3,3)$              1      $1884468968$           $1884468968$

## The four exact partial derivatives

$$\begin{aligned}
\partial_{u_0}Y_H={}&
225244758471u_0^2-57153241578u_0u_1-244001844270u_0u_2\\
&-10729843902u_0u_3+164150208636u_1^2-415458334296u_1u_2\\
&+151070718312u_1u_3+1158143874300u_2^2
+114691988016u_2u_3+113572676646u_3^2,\\[2mm]
\partial_{u_1}Y_H={}&
-28576620789u_0^2+328300417272u_0u_1-415458334296u_0u_2\\
&+151070718312u_0u_3+20696873460u_1^2+2265193804392u_1u_2\\
&-60827080632u_1u_3-2054867641020u_2^2
+151980984216u_2u_3+36794420832u_3^2,\\[2mm]
\partial_{u_2}Y_H={}&
-122000922135u_0^2-415458334296u_0u_1+2316287748600u_0u_2\\
&+114691988016u_0u_3+1132596902196u_1^2
-4109735282040u_1u_2\\
&+151980984216u_1u_3+7938887956452u_2^2
+1120373147880u_2u_3+706181383584u_3^2,\\[2mm]
\partial_{u_3}Y_H={}&
-5364921951u_0^2+151070718312u_0u_1+114691988016u_0u_2\\
&+227145353292u_0u_3-30413540316u_1^2
+151980984216u_1u_2\\
&+73588841664u_1u_3+560186573940u_2^2
+1412362767168u_2u_3+5653406904u_3^2.\end{aligned}$$

Their homogeneous quotient has Hilbert function $$(1,4,6,4,1)$$ and no terms in degree $>4$. This is the length-$16$ exact control used in [\[thm:cubic-surface\]](#thm:cubic-surface){reference-type="ref" reference="thm:cubic-surface"}.
