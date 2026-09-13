---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-mu3-d12-calabi-yau-core-projector"
canonical_tex: "henon_dynamics/henon_mu3_d12_calabi_yau_core_projector/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_mu3_d12_calabi_yau_core_projector/paper/main.pdf"
source_sha256: "3525df6a6281b76a3d24602c22ad50f9a8addf2104dccc1e69e25692edb493d0"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Dihedral Chow Projector and the Extreme-Hodge Gate for a Hénon $\boldsymbol\mu_3$ Fivefold

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_mu3_d12_calabi_yau_core_projector>)
- [规范 TeX](<../../../../../henon_dynamics/henon_mu3_d12_calabi_yau_core_projector/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_mu3_d12_calabi_yau_core_projector/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_mu3_d12_calabi_yau_core_projector/README.md>)
- [BibTeX](<../../../../../henon_dynamics/henon_mu3_d12_calabi_yau_core_projector/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Let $K=\mathbf Q(\rho)$, where $\rho^2+\rho+1=0$, and consider the smooth $(2,3)$ fivefold $$X=\left\{\sum_{i=0}^{7}x_i^3=
   \sum_{i=0}^{6}x_ix_{i+1}+\rho x_7x_0=0\right\}\subset\mathbf P^7_K$$ arising from the fourth cohomological moment of a normalized Hénon-type Euler germ. We determine its projective monomial source stabilizer: it is an order-$24$ group $\operatorname{Dih}(C_{12})=C_{12}\rtimes C_2$. Composing its Reynolds graph correspondence with explicit ordinary Chow--Künneth projectors gives two $K$-rational Chow idempotents on the middle cohomology. A residue-corrected Cayley-ring character calculation shows that their Hodge ranks are $10$ and $158$, with ledgers $$(1,4,4,1)\quad\text{and}\quad(0,79,79,0).$$ The first becomes of Calabi--Yau-threefold Hodge type after one Tate twist. We also prove that rank $10$ is optimal among idempotents in the rational graph algebra that retain the extreme $H^{4,1}$ line: the same trivial representation occurs four times in $H^{3,2}$. This obstruction is confined to the graph algebra. We do not claim a full automorphism classification, coniveau or an abelian realization of the complement, automorphy, a functional equation, or a new analytic half-plane.
author:
- 'Hilbert--Pólya Dynamical Structure Exploration Project'
bibliography:
- references.bib
date: August 2026
title: |
  A Dihedral Chow Projector and the Extreme-Hodge Gate\
  for a Hénon $\boldsymbol{\mu_3}$ Fivefold
```

## Markdown 正文

# Introduction

The Hilbert--Pólya dynamical-structure program explored here starts from chronological Hénon-type orbit data, forms character-weighted local determinants, and asks whether the resulting normalized Euler germ admits an arithmetic or spectral reorganization. Earlier stages of the program converted its second, third, and fourth logarithmic moments into cohomological trace packets. The fourth odd packet is $$O_4=H^5(X)(2),$$ where $X$ is the fivefold in the abstract. Its Hodge types before the twist are $$(4,1)^1+(3,2)^{83}+(2,3)^{83}+(1,4)^1.$$ The extreme pair suggested a concrete projector gate: can source-native algebraic symmetries isolate a small Calabi--Yau-type summand?

This paper gives a deliberately two-sided answer. On the positive side, the complete projective monomial source stabilizer produces a genuine Chow projector of rank $10$. On the negative side, its graph algebra cannot refine the invariant block to rank $2$. The two conclusions are independent of any conjectural functional equation.

The Hodge numbers and Cayley-ring model for smooth $(2,3)$ fivefolds are standard. Favero--Iliev--Katzarkov record $h^{4,1}=1$, $h^{3,2}=83$ in their Section 5.1, equation (6), and give the relevant bigraded Cayley description in Section 5.4, equation (8) [@FIK2012]. Their special diagonal basis and their Griffiths-group results are not projector theorems for the present non-diagonal quadric.

Laterveer writes the ordinary ambient Chow--Künneth projectors and middle complement in the proof of Theorem 4.1 [@Laterveer2021]. The multiplicative result there assumes even ambient projective dimension; the odd case relevant to $X\subset\mathbf P^7$ is not covered. We therefore prove the required ordinary Chow compositions directly. General graph-character projectors occur in Laterveer--Nagel--Peters, Section 6, equation (4) [@LNP2017], but their coniveau and finite-dimensional-motive conclusions require additional hypotheses that are not established here.

Two recent works delimit rather than supply the present theorem. Ciurca--Tanimoto--Tschinkel develop equivariant intermediate-Jacobian-torsor methods for threefold rationality and linearizability [@CTT2024 §§2--3 and Theorem 3.3]; our object is a fivefold and our correspondence is a Chow graph average. Xu studies natural Chow--Künneth decompositions and motivic multiplicativity defects for complete intersections [@Xu2026 Theorems 1.4 and 4.19], but does not produce the source-specific dihedral middle split used here.

High symmetry can produce interesting factors in other Fano settings: Iliev--Roulleau obtain an invariant abelian ninefold from a $\mathrm{PSL}_2(\mathbf F_{19})$-symmetric cubic sevenfold [@IlievRoulleau2013 abstract, Theorem 1, and Corollary 10]. This provides a conceptual neighbor, not a result about our $(2,3)$ fivefold or its field of definition.

## Main contributions {#main-contributions .unnumbered}

1.  We exhaust the phase equations and prove that the projective monomial source stabilizer is the order-$24$ group $\operatorname{Dih}(C_{12})$.

2.  We give explicit $K$-rational Chow idempotents $\pi_{\mathrm{core}}$ and $\pi_{\mathrm{lev}}$, with no MCK assumption.

3.  We include the determinant ratio $\det(M_g)/\det(A_g)$ required by the residue action and compute the exact $\operatorname{Dih}(C_{12})$-character on the Cayley quotient.

4.  We obtain the rank-$10$/rank-$158$ Hodge splitting and prove that rank $10$ is sharp inside $\mathbf Q[G]$.

The term *source* is essential throughout: we classify projective monomial transformations preserving the displayed pair of equations. We do not classify the full automorphism group of $X$.

## Claim boundary {#claim-boundary .unnumbered}

The same $K$-rational Chow idempotent acts in every standard realization, and its $\ell$-adic action is $G_K$-equivariant. We do not call this a computed strict compatible system: common local Frobenius polynomials are a successor experiment. Nor do we infer an actual Calabi--Yau threefold, an abelian $79$-fold over $K$, coniveau, automorphy, a Hasse--Weil functional equation, a new Euler continuation domain, or a Hilbert--Pólya operator.

# The source and the main theorem

Fix $$K=\mathbf Q(\rho),\qquad \rho^2+\rho+1=0,$$ and define $$\label{eq:source}
 C(x)=\sum_{i=0}^{7}x_i^3,\qquad
 Q(x)=\sum_{i=0}^{6}x_ix_{i+1}+\rho x_7x_0.$$ Let $X=\{C=Q=0\}\subset\mathbf P^7_K$. Characteristic-zero smoothness is inherited from the preceding fourth-moment construction; the release machine source lock records the exact C50 certificate path and SHA-256. The variety has dimension $5$, degree $6$, and middle Hodge numbers $$h^{4,1}=h^{1,4}=1,\qquad
 h^{3,2}=h^{2,3}=83.$$

A *projective monomial source symmetry* is a projective transformation represented by $$x_i\longmapsto \rho^{e_i}x_{\sigma(i)}$$ that preserves $C$ and $Q$ up to their individual nonzero scalars. Let $G_{\mathrm{mon}}$ be the group of all such transformations.

Put $h=c_1(\mathcal O_X(1))$. Define $$\label{eq:ambient-projectors}
 \pi_{2i}=\frac16h^{5-i}\times h^i\quad(0\le i\le5),
 \qquad
 \pi_5=\Delta_X-\sum_{i=0}^{5}\pi_{2i},$$ and $$\label{eq:middle-projectors}
 e_G=\frac1{24}\sum_{g\in G_{\mathrm{mon}}}[\Gamma_g],\qquad
 \pi_{\mathrm{core}}=\pi_5e_G,\qquad
 \pi_{\mathrm{lev}}=\pi_5-\pi_5e_G.$$

[\[thm:main\]]{#thm:main label="thm:main"} The projective monomial source stabilizer is $$G_{\mathrm{mon}}\cong\operatorname{Dih}(C_{12})=C_{12}\rtimes C_2,
 \qquad |G_{\mathrm{mon}}|=24.$$ The Reynolds correspondence $e_G$ is a self-transpose idempotent. The two middle correspondences $\pi_{\mathrm{core}}$ and $\pi_{\mathrm{lev}}$ are mutually orthogonal self-transpose idempotents in $\operatorname{CH}^5(X\times_KX)_{\mathbf Q}$. Their middle realizations have Hodge ledgers $$\begin{aligned}
 \pi_{\mathrm{core}}H^5(X)&:
 (4,1)^1+(3,2)^4+(2,3)^4+(1,4)^1,\\
 \pi_{\mathrm{lev}}H^5(X)&:
 (3,2)^{79}+(2,3)^{79}.
\end{aligned}$$ In particular, their ranks are $10$ and $158$. After one Tate twist the first ledger is $$(3,0)^1+(2,1)^4+(1,2)^4+(0,3)^1.$$ The same Chow projectors split every standard Weil realization; each $\ell$-adic projector is $G_K$-equivariant.

[\[thm:optimum\]]{#thm:optimum label="thm:optimum"} Let $q\in\mathbf Q[G_{\mathrm{mon}}]$ be an idempotent whose graph correspondence acts as the identity on $H^{4,1}(X)$. Then $$\operatorname{rank}(qH^5(X))\ge10.$$ The bound is attained by $e_G$. In particular, the rational graph algebra cannot isolate only the rank-two extreme Hodge pair.

Theorem [\[thm:optimum\]](#thm:optimum){reference-type="ref" reference="thm:optimum"} is confined to graph correspondences in $\mathbf Q[G_{\mathrm{mon}}]$. It does not exclude a $K$-rational algebraic correspondence outside that algebra, a projector after extending coefficients, or a different categorical construction.

# The projective monomial source group

## Finite reduction

Suppose a monomial transformation $x_i\mapsto a_ix_{\sigma(i)}$ sends $C$ to $\alpha C$. Coefficient comparison gives $a_i^3=\alpha$ for all $i$. After a common projective rescaling, it therefore has the form $$x_i\longmapsto \rho^{e_i}x_{\sigma(i)},\qquad
 e_i\in\mathbf F_3,\quad e_0=0.                            \tag{3.1}$$ The support of $Q$ is an eight-cycle, so $\sigma$ lies in its order-$16$ dihedral automorphism group. Write $$r_k(i)=i+k,\qquad s_k(i)=k-i\pmod8.$$

Let $c(E)\in\mathbf F_3$ be zero on the seven ordinary edges and one on the closing edge $\{7,0\}$. Preservation of $Q$ up to $\rho^{q_g}$ is equivalent to $$\label{eq:phase-system}
 c(\{i,i+1\})+e_i+e_{i+1}
 =q_g+c(\{\sigma(i),\sigma(i+1)\})$$ for all cyclic indices $i$. This is an affine linear system over $\mathbf F_3$.

[\[prop:enum\]]{#prop:enum label="prop:enum"} The only support permutations admitting solutions to [\[eq:phase-system\]](#eq:phase-system){reference-type="eqref" reference="eq:phase-system"} are $$r_0,r_2,r_4,r_6,s_1,s_3,s_5,s_7.$$ Each admits exactly three normalized phase vectors. Hence $|G_{\mathrm{mon}}|=24$.

Row reduction of [\[eq:phase-system\]](#eq:phase-system){reference-type="eqref" reference="eq:phase-system"} for the sixteen possible support permutations yields the complete table in Appendix [9](#app:tables){reference-type="ref" reference="app:tables"}. Substitution verifies every surviving row, and the exhausted support list proves completeness.

## Presentation

Choose $$\begin{aligned}
r:&\quad \sigma=(6,7,0,1,2,3,4,5),&
e&=(0,1,1,0,1,0,1,0),\\
s:&\quad \sigma=(7,6,5,4,3,2,1,0),&
e&=(0,1,0,1,0,1,0,1).
\end{aligned}                                      \tag{3.2}$$ Direct substitution gives $$C(rx)=C(sx)=C(x),\qquad Q(rx)=Q(sx)=\rho Q(x).$$ Exact phase-permutation multiplication gives $$r^{12}=s^2=1,\qquad srs=r^{-1}.                   \tag{3.3}$$ The twelve $r^k$ and twelve $sr^k$ are distinct. By Proposition [\[prop:enum\]](#prop:enum){reference-type="ref" reference="prop:enum"}, they exhaust $G_{\mathrm{mon}}$. This proves $$G_{\mathrm{mon}}\cong\operatorname{Dih}(C_{12})=C_{12}\rtimes C_2.$$ We always specify order $24$, since dihedral-group notation is not uniform across the literature.

The proof uses the particular embedding of the two equations in $\mathbf P^7$. It does not rule out nonmonomial automorphisms of $X$.

# A Chow-level middle splitting

We now prove that the projector is algebraic before taking any cohomological realization. Since $\deg X=2\cdot3=6$, $$\int_Xh^5=6.                                      \tag{4.1}$$

[\[lem:ambient-idempotents\]]{#lem:ambient-idempotents label="lem:ambient-idempotents"} The correspondences $\pi_{2i}$ in [\[eq:ambient-projectors\]](#eq:ambient-projectors){reference-type="eqref" reference="eq:ambient-projectors"} are mutually orthogonal idempotents in $\operatorname{CH}^5(X\times_KX)_{\mathbf Q}$.

For decomposable correspondences on a smooth fivefold, $$(a\times b)\circ(c\times d)
 =\left(\int_Xda\right)c\times b.                  \tag{4.2}$$ Putting $a=h^{5-i}$, $b=h^i$, $c=h^{5-j}$, and $d=h^j$, the integral vanishes unless $i=j$ and equals $6$ if $i=j$. The normalizing factors in [\[eq:ambient-projectors\]](#eq:ambient-projectors){reference-type="eqref" reference="eq:ambient-projectors"} therefore give $$\pi_{2i}\circ\pi_{2j}=\delta_{ij}\pi_{2i}.$$

It follows immediately that $\pi_5$ is an idempotent orthogonal to the six ambient projectors. Weak Lefschetz identifies the nonmiddle cohomology with the ambient powers of $h$, so $\pi_5$ realizes precisely the middle cohomology. Also $\pi_{2i}^t=\pi_{10-2i}$, and therefore $\pi_5^t=\pi_5$.

[\[lem:reynolds\]]{#lem:reynolds label="lem:reynolds"} The graph average $e_G$ commutes with $\pi_5$, satisfies $e_G^2=e_G=e_G^t$, and $\pi_{\mathrm{core}},\pi_{\mathrm{lev}}$ in [\[eq:middle-projectors\]](#eq:middle-projectors){reference-type="eqref" reference="eq:middle-projectors"} are mutually orthogonal self-transpose idempotents.

Every $g\in G_{\mathrm{mon}}$ is induced by a projective linear transformation, so $g^*h=h$. Thus its graph commutes with each $\pi_{2i}$ and with $\pi_5$. Moreover, $$[\Gamma_g][\Gamma_{g'}]=[\Gamma_{gg'}],
 \qquad
 [\Gamma_g]^t=[\Gamma_{g^{-1}}].                  \tag{4.3}$$ In the double sum defining $e_G^2$, each group element occurs exactly $24$ times. This proves idempotence. Inversion permutes the group, proving self-transposition. Commutation with $\pi_5$ then proves all claims by direct expansion.

This argument proves ordinary Chow projector identities modulo rational equivalence. It does not assert compatibility with the small diagonal, and therefore does not invoke an MCK theorem. This distinction is essential because the even-ambient-dimension hypothesis in [@Laterveer2021 Theorem 4.1] is not satisfied by $X\subset\mathbf P^7$.

# The residue-twisted Cayley character

## The quotient and the projective action

Set $$\mathcal F=yC+zQ,\qquad
 R=K[x_0,\ldots,x_7,y,z]/J(\mathcal F),$$ with bidegrees $$\deg x_i=(0,1),\qquad
 \deg y=(1,-3),\qquad
 \deg z=(1,-2).                                    \tag{5.1}$$ The Cayley description [@FIK2012 §5.4, equation (8)] gives $$H^{4,1}_{\mathrm{prim}}(X)\cong R_{1,-3},
 \qquad
 H^{3,2}_{\mathrm{prim}}(X)\cong R_{2,-3}.         \tag{5.2}$$

Choose a lift $M_g\in\operatorname{GL}_8(K)$ and let $A_g$ be defined by $$\binom C Q(M_gx)=A_g\binom C Q(x).                \tag{5.3}$$ The induced Cayley transformation is $$(x,(y,z)^t)\longmapsto
 (M_gx,A_g^{-t}(y,z)^t).                           \tag{5.4}$$ The residue class has the additional orientation multiplier $$\label{eq:orientation}
 \omega(g)=\frac{\det M_g}{\det A_g}.$$

[\[lem:lift\]]{#lem:lift label="lem:lift"} The action consisting of polynomial pullback under $(5.4)$ and the multiplier $\omega(g)$ in [\[eq:orientation\]](#eq:orientation){reference-type="eqref" reference="eq:orientation"} is independent of the scalar lift $M_g$.

Replacing $M_g$ by $\lambda M_g$ replaces $A_g$ by $\operatorname{diag}(\lambda^3,\lambda^2)A_g$. For a representative in $R_{p,-3}$, the simultaneous Cayley polynomial pullback has total scalar $\lambda^{-3}$: the $x$-, $y$-, and $z$-degrees combine using the second bidegree $-3$. The determinant ratio changes by $\lambda^{8-3-2}=\lambda^3$, so the factors cancel. For the explicit control $\lambda=2$, these are $2^{-3}$ and $2^3$.

For the chosen generators, $$A_r=A_s=\operatorname{diag}(1,\rho),\qquad
 \det M_r=\det M_s=\rho,$$ so $\omega(r)=\omega(s)=1$. This accidental simplification does not justify removing [\[eq:orientation\]](#eq:orientation){reference-type="eqref" reference="eq:orientation"}.

## Exact character

The ambient bidegree-$(2,-3)$ monomials form $$y^2K[x]_3\oplus yzK[x]_2\oplus z^2K[x]_1,$$ of dimension $$\binom{10}{3}+\binom92+8=164.$$ The corresponding Jacobian relations have rank $81$, hence $\dim R_{2,-3}=83$. Exact quotient matrices give $$\begin{aligned}
 \operatorname{tr}(r^k)
 &=(83,-1,-3,-1,-7,-1,3,-1,-7,-1,-3,-1),
                                                        \tag{5.5}\\
 \operatorname{tr}(sr^k)&=3\qquad(0\le k\le11).                       \tag{5.6}\end{aligned}$$

The four one-dimensional characters, ordered by $$(r,s)\longmapsto(1,1),(1,-1),(-1,1),(-1,-1),$$ occur with multiplicities $$(4,1,3,3).                                        \tag{5.7}$$ For $1\le j\le5$, let $$\vartheta_j(r^k)=2\cos\left(\frac{\pi jk}{6}\right),
 \qquad \vartheta_j(sr^k)=0.$$ Their multiplicities are $$(7,8,6,8,7).                                      \tag{5.8}$$ The dimension check is $$4+1+3+3+2(7+8+6+8+7)=83.$$

Finally, $R_{1,-3}=Ky$ is the trivial representation. The group average therefore retains one dimension in $H^{4,1}$, four in $H^{3,2}$, and their conjugates. This proves the first Hodge ledger in Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}. Subtracting from the total $(1,83,83,1)$ gives the second.

The release computation must reconstruct the quotient action and the character over an exact coefficient field. A trace list supplied by the producer without an independent quotient replay is not sufficient evidence.

# The graph-algebra optimum

Let $$\varepsilon:\mathbf Q[G_{\mathrm{mon}}]\longrightarrow\mathbf Q,\qquad
 \varepsilon\left(\sum_ga_gg\right)=\sum_ga_g$$ be the augmentation. If $V_{\mathrm{triv}}$ is any copy of the trivial representation, then every $a\in\mathbf Q[G_{\mathrm{mon}}]$ acts on it by the single scalar $\varepsilon(a)$.

If $q^2=q$, then $$\varepsilon(q)^2=\varepsilon(q),$$ so $\varepsilon(q)$ is either zero or one. The line $H^{4,1}(X)$ is trivial. Requiring $q$ to act as the identity there forces $\varepsilon(q)=1$. Equation (5.7) shows that $H^{3,2}(X)$ contains four more trivial copies, and $q$ must act as the identity on all of them. Because $q$ is a rational graph correspondence, the conjugate pieces are retained as well. Thus $$\operatorname{rank}(qH^5(X))\ge1+4+4+1=10.$$ The Reynolds idempotent $e_G$ acts as the identity exactly on the invariant subspace, whose rank is $10$, so the bound is sharp.

This obstruction is representation-theoretic, not a universal indecomposability theorem. In particular, it does not control correspondences outside the image of $\mathbf Q[G_{\mathrm{mon}}]$ in $\operatorname{CH}^5(X\times_KX)_{\mathbf Q}$. It also does not control projectors after a coefficient extension.

## What the Hodge ledgers do not imply

After one Tate twist, the invariant core has Hodge numbers $$h^{3,0}=h^{0,3}=1,\qquad h^{2,1}=h^{1,2}=4.$$ We call this a Calabi--Yau-threefold Hodge type only. No threefold realizing it is constructed.

After the C51 twist by two, the complement has Hodge types $$(1,0)^{79}+(0,1)^{79}.$$ Over $\mathbf C$, polarizable effective weight-one Hodge structures are related to abelian varieties up to isogeny, but descent of an arbitrary $G_K$-representation to an abelian variety over $K$ is an extra arithmetic statement; see the discussion in [@ACMV2020 Introduction, pp. 2--3]. Theorem A and Theorem 6.1 of that work give sufficient constructions under additional geometric hypotheses, such as coniveau or a full level-one complete-intersection packet; they do not apply automatically to our projected summand. We have proved neither the needed geometric realization nor coniveau one. Thus the notation $A_{79}/K$ would be unjustified here.

# Route-A impact and the next gate

The result is structural rather than analytic. It preserves the chronological fourth-moment source and refines its odd cohomological packet by algebraic correspondences. This is a substantial improvement to the arithmetic organization of the candidate, but it does not by itself improve the normalized Euler germ.

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Criterion   C52 status
  ----------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  A1          Source chronology inherited unchanged from C51.

  A2          Analytic determinant and normalized logarithmic germ inherited; no new determinant theorem.

  A3          Algebraic packet control improved by the rank-$10/158$ Chow splitting; no local Frobenius polynomials, automorphy, full functional equation, or new continuation domain.

  A4          `A4_NATURAL_QUANTIZATION` is inherited because the source two-step quantization is unchanged; no self-adjoint global generator is constructed.
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The overall Route-A status is therefore exploratory. There is no Riemann-divisor match: in particular, the paper makes no claim that the center or zeros of a Hasse--Weil factor, even if later constructed, already match the Riemann critical line.

## C53 gate

The next paper must open a different door. It should compute full local Frobenius polynomials of the rank-$10$ core at good split primes and test the commutant beyond $\mathbf Q[G_{\mathrm{mon}}]$. A positive theorem would construct a new $K$-rational algebraic correspondence refining the trivial isotypic block. A negative theorem would prove, from exact local polynomials and a controlled correspondence algebra, that no such low-rank refinement occurs there.

Neither full local polynomial data nor an incidence correspondence is claimed in C52. Consequently C52 proves no automorphy, Hasse--Weil functional equation, or new analytic half-plane.

# Limitations

The group enumeration is complete only for projective monomial transformations preserving the frozen source equations up to scalar. The character calculation depends on exact quotient linear algebra and must remain tied to the residue determinant ratio. The optimality theorem applies only to the rational graph algebra. The Hodge ledgers do not establish coniveau, finite-dimensionality, abelian type, or geometric realization by lower-dimensional varieties.

On the dynamical side, the construction analyzes one cohomological packet extracted from the fourth logarithmic moment. It does not produce a global self-adjoint operator, a functional equation for the full Hénon object, or a proof of the Riemann hypothesis.

# Data availability {#data-availability .unnumbered}

The exact source equations, phase table, character ledger, and proof specification are included in the project directory. Release certificates, independent checks, mutation tests, and the final manifest are archived with the paper. The compilation and integrity reports record the immutable artifact hashes.

# Ethics statement {#ethics-statement .unnumbered}

This research is mathematical and computational. It involved no human participants, personal data, animals, or biological materials.

# Author contributions {#author-contributions .unnumbered}

Conceptualization, formal analysis, methodology, software design, validation design, writing, and project administration were carried out within the Hilbert--Pólya Dynamical Structure Exploration Project. Human review is required before external submission.

# Conflict of interest {#conflict-of-interest .unnumbered}

No conflict of interest is declared.

# Funding {#funding .unnumbered}

No dedicated external funding is declared for this manuscript.

# AI-use statement {#ai-use-statement .unnumbered}

Generative AI systems assisted with conjecture generation, exact derivation organization, software drafting, literature routing, and manuscript preparation. Mathematical claims are separated from machine evidence and are subject to exact producer/checker replay and human verification. AI assistance is not treated as evidence for a theorem.

# Exact phase and character tables {#app:tables}

An eight-digit word records $(e_0,\ldots,e_7)$.

   Support permutation  Normalized phase words
  --------------------- ----------------------------------
          $r_0$         $00000000,\ 01010101,\ 02020202$
          $r_2$         $01010110,\ 02020211,\ 00000012$
          $r_4$         $01011010,\ 02021111,\ 00001212$
          $r_6$         $01101010,\ 02111111,\ 00121212$
          $s_1$         $01101010,\ 02111111,\ 00121212$
          $s_3$         $01011010,\ 02021111,\ 00001212$
          $s_5$         $01010110,\ 02020211,\ 00000012$
          $s_7$         $00000000,\ 01010101,\ 02020202$

For the rotation generator, the exact $R_{2,-3}$ traces are $$\begin{array}{c|rrrrrrrrrrrr}
k&0&1&2&3&4&5&6&7&8&9&10&11\\
\hline
\operatorname{tr}(r^k)&83&-1&-3&-1&-7&-1&3&-1&-7&-1&-3&-1
\end{array}$$ and $\operatorname{tr}(sr^k)=3$ for all $k$. The resulting multiplicities are $$\begin{array}{c|rrrr}
(\chi(r),\chi(s))&(1,1)&(1,-1)&(-1,1)&(-1,-1)\\
\hline
\text{multiplicity}&4&1&3&3
\end{array}$$ for the one-dimensional characters and $$\begin{array}{c|rrrrr}
j&1&2&3&4&5\\
\hline
\text{multiplicity of }\vartheta_j&7&8&6&8&7
\end{array}$$ for the two-dimensional characters $\vartheta_j(r^k)=2\cos(\pi jk/6)$.
