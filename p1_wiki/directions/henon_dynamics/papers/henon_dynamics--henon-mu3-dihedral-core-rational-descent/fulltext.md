---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-mu3-dihedral-core-rational-descent"
canonical_tex: "henon_dynamics/henon_mu3_dihedral_core_rational_descent/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_mu3_dihedral_core_rational_descent/paper/main.pdf"
source_sha256: "6930752f977a236ad4670541665be88353fb648f1ad3f9f8f4c12b09d148dfed"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Rational Descent and the Rank-Ten Dihedral Core of the Fourth Hénon Moment Packet

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_mu3_dihedral_core_rational_descent>)
- [规范 TeX](<../../../../../henon_dynamics/henon_mu3_dihedral_core_rational_descent/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_mu3_dihedral_core_rational_descent/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_mu3_dihedral_core_rational_descent/README.md>)
- [BibTeX](<../../../../../henon_dynamics/henon_mu3_dihedral_core_rational_descent/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Let $K=\mathbf Q(\rho)$, with $\rho^2+\rho+1=0$, and let $$X_n=\left\{\sum_{i=0}^{2n-1}x_i^3=
  \sum_{i=0}^{2n-2}x_ix_{i+1}+\rho x_{2n-1}x_0=0\right\}
  \subset\mathbf P_K^{2n-1}.$$ These source-ordered complete intersections encode the cohomological moments of a normalized Hénon Euler germ. We give an explicit semilinear reversal and a closed fixed basis that descend $X_n$ to $\mathbf Q$ for every $n\ge2$. The equation theorem is unconditional; the motivic statements use only the certified smooth rows $n=2,3,4$. Their rational moment packets have ranks $15,63,255$. At every good split rational prime, the C51 exponent $2/n$ over the two $K$-places becomes $4/n$ on one rational factor. The fourth-row half-power therefore equals one ordinary rank-$255$, exponent-one rational local factor, whereas the third row remains fractional with exponent $4/3$. For $n=4$, Galois transport twists the order-$24$ dihedral source group rather than fixing its elements. Its Reynolds graph sum nevertheless descends and splits the rational middle motive into ranks $10+158$. The raw rank-$10$ summand has an $\ell$-independent degree-$10$ polynomial in $\mathbf Z[T]$, pure of weight $5$, at every good prime. The split identity does not extend to inert primes and yields no global square root, continuation, or functional equation.
author:
- 'Hilbert--Pólya Dynamical Structure Exploration Project'
bibliography:
- references.bib
date: August 2026
title: |
  Rational Descent and the Rank-Ten Dihedral Core\
  of the Fourth Hénon Moment Packet
```

## Markdown 正文

# Introduction

The fourth cohomological moment in the Hénon source program carries an apparently awkward half-power over the quadratic field $K=\mathbf Q(\rho)$. A direct $K$-compatible system cannot realize that half-power without acquiring a nonintegral rank. The obstruction leaves one algebraic escape: the two $K$-places above a split rational prime could be the conjugate copies of a single object over $\mathbf Q$.

This paper constructs that rational object. The construction begins at the equation level, before any local factor is manipulated. Reversal of the source chronology is accompanied by alternating powers of $\rho$; the resulting monomial map is a Weil descent datum. Solving its fixed-vector equations gives one rational coordinate system in every row and preserves the weighted closing edge. Thus the repair is geometric rather than a formal choice of a square-root branch.

The fourth row contains more structure. The preceding source analysis found an order-$24$ group $\operatorname{Dih}(C_{12})$ and a rank-$10$ Reynolds summand in the middle cohomology. Conjugation by the rational descent does not fix the twenty-four transformations individually. Instead it acts by $$r\longmapsto r^{-1},\qquad s\longmapsto sr^{-1}.$$ The correct rational object is consequently a nonconstant finite étale group scheme split by $K$. Its graph sum is invariant, so rational restriction and corestriction descend the Chow projector.

## Contributions {#contributions .unnumbered}

The paper proves four claims.

1.  For every $n\ge2$, we construct an explicit $\mathbf Q$-model of the source-ordered $(2,3)$ intersection and prove a closed determinant formula for the coordinate change. This statement concerns equations; smoothness and motives are not promoted beyond the certified rows.

2.  For $n=2,3,4$, we descend the full cohomological packet of rank $4^n-1$. At good split primes, its exponent changes from $2/n$ over $K$ to $4/n$ over $\mathbf Q$. The $n=4$ half-power clears exactly.

3.  We descend the order-$24$ Reynolds correspondence and obtain rational Chow summands of ranks $10$ and $158$. The rank-$10$ summand has Hodge ledger $(1,4,4,1)$ and becomes of Calabi--Yau-threefold Hodge type after one Tate twist.

4.  At good primes, the raw rank-$10$ Frobenius polynomial is $\ell$-independent, belongs to $\mathbf Z[T]$, has weight $5$, and obeys the expected degree-five reciprocity. This strict compatibility statement does not use semisimplicity.

## Relation to existing geometry {#relation-to-existing-geometry .unnumbered}

Favero--Iliev--Katzarkov give the Hodge numbers and Cayley-ring description for smooth $(2,3)$ fivefolds in $\mathbf P^7$ [@FIK2012 §5.1, equation (6), and §5.4, equation (8)]. Those results supply context for the ledger, not the source-specific descent or projector. Laterveer records ordinary nonmiddle Chow--Künneth projectors for intersections of a quadric and a cubic [@Laterveer2021 proof of Theorem 4.1]; the multiplicative theorem there assumes even ambient dimension and does not apply to $\mathbf P^7$. Vial gives broader finite-dimensional-motive context [@Vial2013 Example 4.12]. None of these references identifies the Hénon-derived rational form or its twisted dihedral core.

Our descent proof is explicit and therefore avoids a general effectivity claim for arbitrary projective descent data. For Chow cycles, we use the standard proper-pushforward and flat-pullback degree formulas [@Fulton1998 §§1.4, 1.7]. Kahn's motivic descent theorem [@Kahn2023 Theorems 1 and 7.1] gives a modern categorical backdrop, but the graph-sum argument below is elementary with rational coefficients. For local polynomials, the comparison input is the correspondence-trace theorem of Katz--Messing [@KatzMessing1974 Theorem 2(2)].

## Scope {#scope .unnumbered}

Every Frobenius in this paper is geometric, normalized by $\operatorname{Frob}_p\mid\mathbf Q_\ell(-1)=p$. The rational exponent clearing is local to good split primes. At inert primes, Frobenius eigenvalues are squared rather than duplicated, which blocks a global half-root. We do not claim smoothness for $n\ge5$, automorphy, meromorphic continuation, a functional equation, a Calabi--Yau realization, or Chow indecomposability. The exact irreducibility gate for the rank-$10$ polynomial is recorded only as a successor problem.

# The source family and main theorem {#sec:source-main}

Let $$K=\mathbf Q(\rho),\qquad \rho^2+\rho+1=0,\qquad
\tau(\rho)=\rho^2.$$ For $n\ge2$, set $N=2n$ and $$C_n=\sum_{i=0}^{N-1}x_i^3,\qquad
Q_{n,\rho}=\sum_{i=0}^{N-2}x_ix_{i+1}+\rho x_{N-1}x_0.
\label{eq:source-forms}$$ The source variety is $$X_n=V(C_n,Q_{n,\rho})\subset\mathbf P_K^{N-1}.$$ The order of the variables and the coefficient on $x_{N-1}x_0$ are part of the definition.

Define $\sigma(i)=-i\bmod N$, and put $$e_i=\begin{cases}
1,&i\ne0\text{ and }i\text{ is even},\\
0,&i=0\text{ or }i\text{ is odd}.
\end{cases}$$ Let $M_n$ be the monomial transformation $$(M_nx)_i=\rho^{e_i}x_{\sigma(i)}.
\label{eq:M-definition}$$ Finally set $\theta=1+2\rho$, so that $\theta^2=-3$ and $\tau(\theta)=-\theta$.

[\[thm:family-descent\]]{#thm:family-descent label="thm:family-descent"} For every $n\ge2$, $$C_n(M_nx)=C_n(x),\qquad
Q_{n,\rho}(M_nx)=\rho Q_{n,\rho^2}(x),\qquad
M_n\tau(M_n)=I.$$ In rational coordinates $$(u_0,a_1,b_1,\ldots,a_{n-1},b_{n-1},c),$$ define $B_n$ by $$\begin{aligned}
x_0&=u_0,\nonumber\\
x_i&=a_i+\theta b_i,\qquad
x_{N-i}=\rho^{e_i}(a_i-\theta b_i)
       &&(1\le i<n),\label{eq:B-pairs}\\
x_n&=\kappa_nc,\qquad
\kappa_n=\begin{cases}1,&n\text{ odd},\\1+\rho,&n\text{ even}.
\end{cases}\nonumber\end{aligned}$$ Then $$M_n\tau(B_n)=B_n,\qquad
\det B_n=(2\theta)^{n-1}\rho^{\lfloor(n-1)/2\rfloor}\kappa_n\ne0.
\label{eq:B-det}$$ The forms $$C_{n,0}=u_0^3+\sum_{i=1}^{n-1}(2a_i^3-18a_ib_i^2)
          +(-1)^{n+1}c^3
\label{eq:C0}$$ and $$\begin{aligned}
Q_{n,0}={}&u_0(a_1+3b_1)\nonumber\\
&+\sum_{i=1}^{n-2}
(a_ia_{i+1}+3a_ib_{i+1}+3b_ia_{i+1}-3b_ib_{i+1})
+R_n,\label{eq:Q0}\\
R_n={}&
\begin{cases}
(a_{n-1}+3b_{n-1})c,&n\text{ odd},\\
2a_{n-1}c,&n\text{ even}
\end{cases}\nonumber\end{aligned}$$ satisfy $$C_n(B_nu)=C_{n,0}(u),\qquad
Q_{n,\rho}(B_nu)=(1+\rho)Q_{n,0}(u).$$ Consequently $$X_{n,0}=V(C_{n,0},Q_{n,0})\subset\mathbf P_\mathbf Q^{2n-1}$$ base-changes to $X_n$.

Theorem [\[thm:family-descent\]](#thm:family-descent){reference-type="ref" reference="thm:family-descent"} is an identity theorem for equations. The source work certifies smoothness only for $n=2,3,4$; no later row is declared smooth here.

[\[thm:packets-repair\]]{#thm:packets-repair label="thm:packets-repair"} For $n=2,3,4$, the normalized even and odd packets descend to a rational packet $$\mathsf W_n=\mathsf E_n\oplus\mathsf O_n,\qquad
\operatorname{rank}\mathsf W_n=4^n-1.$$ Their ranks are $15,63,255$. At every good split rational prime, $$\frac2n\operatorname{Log}_0L_{K,p}(\mathsf W_{n,K},u)
=\frac4n\operatorname{Log}_0L_{\mathbf Q,p}(\mathsf W_n,u).$$ The reduced rational denominator is $n/\gcd(n,4)$. In particular, $$\left(L_{K,p}(\mathsf W_{4,K},u)\right)^{1/2}_{\operatorname{Log}_0}
=L_{\mathbf Q,p}(\mathsf W_4,u).
\label{eq:split-repair}$$ The right side is one rank-$255$, exponent-one rational local factor.

[\[thm:core-main\]]{#thm:core-main label="thm:core-main"} For $n=4$, the order-$24$ Reynolds middle projector descends to $\mathbf Q$. It gives mutually orthogonal self-transpose Chow projectors $\pi_{\mathrm{core},0}$ and $\pi_{\mathrm{lev},0}$ of ranks $10$ and $158$. The full rational packet decomposes by ranks $$87+10+158=255.$$ The raw rank-$10$ summand $\mathsf M_0=(X_{4,0},\pi_{\mathrm{core},0},0)$ has Hodge numbers $$h^{4,1}=h^{1,4}=1,\qquad h^{3,2}=h^{2,3}=4.$$

[\[thm:compatible-main\]]{#thm:compatible-main label="thm:compatible-main"} Outside a finite set, for every $\ell\ne p$, $$P_p(T)=\det(1-\operatorname{Frob}_pT\mid H_\ell(\mathsf M_0))
=\sum_{k=0}^{10}a_kT^k$$ is a degree-$10$ polynomial in $\mathbf Z[T]$, independent of $\ell$, and pure of weight $5$. It satisfies $$a_{10-k}=p^{25-5k}a_k
\quad(0\le k\le10).$$ The twice-twisted system $\mathsf M_0(2)$ has weight $1$ and local polynomial $P_p(T/p^2)\in\mathbf Q[T]$.

# The semilinear reversal and its fixed basis {#sec:explicit-descent}

## The cocycle identities

Because $\rho^3=1$ and $\sigma$ is a permutation, $$C_n(M_nx)=\sum_i\rho^{3e_i}x_{\sigma(i)}^3=C_n(x).$$ For the quadric, separate the edge indexed by $i=0$, the edges $1\le i\le N-2$, and the closing edge. Reversal sends the $i=0$ edge to the closing pair with phase $1$. Every edge indexed by $1\le i\le N-2$ has exactly one nonzero even endpoint and therefore acquires phase $\rho$. The closing term in $Q_{n,\rho}$ is sent to the edge $x_0x_1$, still with coefficient $\rho$. Hence $$Q_{n,\rho}(M_nx)
=x_{N-1}x_0+\rho\sum_{i=0}^{N-2}x_ix_{i+1}
=\rho Q_{n,\rho^2}(x).$$ Finally $e_{\sigma(i)}=e_i$. Applying the conjugate matrix after $M_n$ multiplies coordinate $i$ by $$\rho^{e_i}\tau(\rho^{e_{\sigma(i)}})
=\rho^{e_i+2e_i}=1,$$ which proves $M_n\tau(M_n)=I$.

## Fixed vectors

The relation $\tau(\theta)=-\theta$ makes the pair in [\[eq:B-pairs\]](#eq:B-pairs){reference-type="eqref" reference="eq:B-pairs"} fixed: $$\rho^{e_i}\tau(x_{N-i})
=\rho^{e_i}\rho^{2e_i}(a_i+\theta b_i)=x_i.$$ The reverse identity is the same calculation. At the central index, $\sigma(n)=n$. If $n$ is odd, then $e_n=0$ and $x_n=c$ is fixed. If $n$ is even, then $e_n=1$, and $$\rho\tau(1+\rho)=\rho(1+\rho^2)=1+\rho,$$ so $x_n=(1+\rho)c$ is fixed.

[\[lem:determinant\]]{#lem:determinant label="lem:determinant"} In the source row order and the rational variable order of Theorem [\[thm:family-descent\]](#thm:family-descent){reference-type="ref" reference="thm:family-descent"}, $$\det B_n=(2\theta)^{n-1}
\rho^{\lfloor(n-1)/2\rfloor}\kappa_n.$$

After pairing rows $i,N-i$, the block for $(a_i,b_i)$ is $$\begin{pmatrix}
1&\theta\\
\rho^{e_i}&-\rho^{e_i}\theta
\end{pmatrix},$$ with determinant $-2\rho^{e_i}\theta$. The permutation from the source row order to the paired order has sign $(-1)^{n-1}$, which cancels the product of the $n-1$ block signs. Exactly $\lfloor(n-1)/2\rfloor$ indices in $1,\ldots,n-1$ are even. The unpaired coordinates contribute $1$ and $\kappa_n$. Multiplying the blocks proves the formula.

The formula is nonzero in $K$, so fixed vectors supply a full basis. This proves effectivity directly. In particular, no general assertion about arbitrary projective descent data is needed; compare the standard descent cautions and the smoothness-locality statement in Stacks Project Tags 08KE and 02VL [@StacksProject].

## Expansion over the rational field

The cubic calculation uses $$(a+\theta b)^3+(a-\theta b)^3
=2a^3+6a\theta^2b^2=2a^3-18ab^2.$$ If $n$ is odd, the central cube is $c^3$. If $n$ is even, then $(1+\rho)^3=-1$, so the central cube is $-c^3$. These two cases give [\[eq:C0\]](#eq:C0){reference-type="eqref" reference="eq:C0"}.

For adjacent paired coordinates, expansion and $\theta^2=-3$ give $$a_ia_{i+1}+3a_ib_{i+1}+3b_ia_{i+1}-3b_ib_{i+1}$$ after the common scalar $1+\rho$ is removed. The initial edge gives $u_0(a_1+3b_1)$. At the center, the two incident edges give $$R_n=\begin{cases}
(a_{n-1}+3b_{n-1})c,&n\text{ odd},\\
2a_{n-1}c,&n\text{ even}.
\end{cases}$$ This proves [\[eq:Q0\]](#eq:Q0){reference-type="eqref" reference="eq:Q0"} and completes Theorem [\[thm:family-descent\]](#thm:family-descent){reference-type="ref" reference="thm:family-descent"}.

## The fourth rational model

For $n=4$, write $$(u_0,u_1,u_2,u_3,u_4,u_5,u_6,u_7)
=(u_0,a_1,b_1,a_2,b_2,a_3,b_3,c).$$ The rational model is $$\begin{aligned}
C_{4,0}={}&u_0^3+2u_1^3-18u_1u_2^2
+2u_3^3-18u_3u_4^2\\
&+2u_5^3-18u_5u_6^2-u_7^3,\\
Q_{4,0}={}&u_0u_1+3u_0u_2+u_1u_3+3u_1u_4
+3u_2u_3-3u_2u_4\\
&+u_3u_5+3u_3u_6+3u_4u_5-3u_4u_6+2u_5u_7.\end{aligned}$$ Lemma [\[lem:determinant\]](#lem:determinant){reference-type="ref" reference="lem:determinant"} gives $\det B_4=24\theta$. Smoothness follows from the certified smooth $K$-model by base change; this implication does not certify any untested source row.

# Rational packets and the split half-power {#sec:rational-packets}

Let $S_n=V(\sum x_i^3)$ over $\mathbf Q$. For the certified smooth rows $n=2,3,4$, define $$\mathsf E_n=\mathbf 1\oplus(S_n,\pi_{\mathrm{prim}}^{S_n},n-1),
\qquad
\mathsf O_n=(X_{n,0},\pi_{2n-3}^{X_n},n-2),$$ and $$\mathsf W_n=\mathsf E_n\oplus\mathsf O_n.$$ The projectors are the ordinary hyperplane projectors and their middle complements. For the fivefold $X_{4,0}$, for example, $$\pi_{2i}=\frac16h^{5-i}\times h^i,\qquad
\pi_5=\Delta-\sum_{i=0}^5\pi_{2i}.
\label{eq:pi5}$$ The coefficient $1/6$ is the inverse degree of the complete intersection. No multiplicative Chow--Künneth assertion is used.

The source cohomology calculation gives $$\operatorname{rank}\mathsf E_n=\frac{4^n+5}{3},\qquad
\operatorname{rank}\mathsf O_n=\frac{2(4^n-4)}3.
\label{eq:packet-ranks}$$ Both summands are now defined over $\mathbf Q$: the Fermat cubic was rational from the outset, and Theorem [\[thm:family-descent\]](#thm:family-descent){reference-type="ref" reference="thm:family-descent"} supplies $X_{n,0}$. Base change preserves the projectors and ranks. Adding [\[eq:packet-ranks\]](#eq:packet-ranks){reference-type="eqref" reference="eq:packet-ranks"} proves $$\operatorname{rank}\mathsf W_n=4^n-1,$$ which is $15,63,255$ in the three certified rows.

## Placewise quadratic base change

For a rational prime $p$ outside the common bad set, write $$L_{K,p}(\mathsf W_{n,K},u)
=\prod_{v\mid p}L_{K,v}(\mathsf W_{n,K},u).$$ If $p$ splits in $K$, both residue fields equal $\mathbf F_p$. Because $\mathsf W_{n,K}$ is the base change of $\mathsf W_n$, the two local factors are identical: $$L_{K,p}(\mathsf W_{n,K},u)
=L_{\mathbf Q,p}(\mathsf W_n,u)^2.
\label{eq:split-square}$$ Apply the power-series logarithm normalized by $\operatorname{Log}_0(1)=0$. Multiplication by the C51 exponent $2/n$ yields $$\frac2n\operatorname{Log}_0L_{K,p}
=\frac4n\operatorname{Log}_0L_{\mathbf Q,p}.$$ The remaining denominator is $n/\gcd(n,4)$. Hence the third row retains exponent $4/3$, while the fourth row has exponent one. Exponentiating in the same origin-normalized branch proves [\[eq:split-repair\]](#eq:split-repair){reference-type="eqref" reference="eq:split-repair"}.

The fourth-row result is ordinary in rank and local multiplicity: one rank-$255$ rational factor occurs with exponent one. The packet contains Tate-normalized pieces, so its polynomial is naturally in $\mathbf Q[T]$ and need not be integral. The integral statement in Theorem [\[thm:compatible-main\]](#thm:compatible-main){reference-type="ref" reference="thm:compatible-main"} concerns the untwisted rank-$10$ smooth-projective summand.

Theorem [\[thm:packets-repair\]](#thm:packets-repair){reference-type="ref" reference="thm:packets-repair"} now follows. For $n\ge5$, the same denominator arithmetic is only conditional on smoothness and an analogous source-packet extraction. The all-$n$ theorem proved in this paper remains the equation descent.

# The twisted dihedral group and Chow descent {#sec:dihedral-core}

The fourth $K$-model carries the source group $$G=\operatorname{Dih}(C_{12})
=\langle r,s\mid r^{12}=s^2=1,\ srs=r^{-1}\rangle,
\qquad |G|=24.$$ Transport through the semilinear descent datum gives $$\delta(r)=r^{-1},\qquad \delta(s)=sr^{-1}=rs.
\label{eq:delta-generators}$$ Consequently $$\delta(r^k)=r^{-k},\qquad
\delta(r^ks)=r^{1-k}s.
\label{eq:delta-elements}$$ These formulas define a Galois action by group automorphisms. Descent of the constant group $G_K$ along this action gives a finite étale $\mathbf Q$-group scheme $\mathscr G$ of rank $24$, split by $K$. It is not constant: only $1$ and $r^6$ are fixed geometric elements. Thus the statement is not that twenty-four separate automorphisms are defined over $\mathbf Q$.

## The invariant graph sum

On $X_{4,K}\times X_{4,K}$, let $$e_G=\frac1{24}\sum_{g\in G}[\Gamma_g].
\label{eq:reynolds}$$ Equation [\[eq:delta-elements\]](#eq:delta-elements){reference-type="eqref" reference="eq:delta-elements"} permutes all twenty-four graph cycles, so $\tau(e_G)=e_G$. Let $$q:(X_{4,0}\times X_{4,0})_K
\longrightarrow X_{4,0}\times X_{4,0}$$ be quadratic base change and define $$e_{\mathscr G}=\frac12q_*e_G.
\label{eq:transfer}$$ The pull-push identities for cycles [@Fulton1998 §§1.4, 1.7] give $$q^*e_{\mathscr G}
=\frac12(e_G+\tau e_G)=e_G,\qquad
q_*q^*=2.$$ Therefore $q^*$ is injective on Chow groups with rational coefficients. The two denominators have different origins: $1/24$ is Reynolds averaging, whereas $1/2$ is field transfer.

Over $K$, the group average is an idempotent, is fixed by transposition, and commutes with $\pi_5$. Each assertion is a polynomial identity in correspondences. Pullback injectivity descends all of them to $\mathbf Q$. Define $$\pi_{\mathrm{core},0}=\pi_5e_{\mathscr G},\qquad
\pi_{\mathrm{lev},0}=\pi_5-\pi_5e_{\mathscr G}.
\label{eq:core-level}$$ These are mutually orthogonal self-transpose Chow projectors. This proves the descent assertion of Theorem [\[thm:core-main\]](#thm:core-main){reference-type="ref" reference="thm:core-main"}. Rational coefficients are essential; the transfer argument does not supply an integral Chow projector.

## Ranks and Hodge types

The frozen character calculation over $K$ gives rank $10$ for $\pi_5e_G$ and rank $158$ for its middle complement. Since base change preserves realization ranks, [\[eq:core-level\]](#eq:core-level){reference-type="eqref" reference="eq:core-level"} has the same ranks over $\mathbf Q$. The even packet has rank $87$, so $$\operatorname{rank}\mathsf W_4=87+10+158=255.$$ The raw core has Hodge realization $$(4,1)^1+(3,2)^4+(2,3)^4+(1,4)^1.$$ After one Tate twist, this becomes $$(3,0)^1+(2,1)^4+(1,2)^4+(0,3)^1,$$ which is of Calabi--Yau-threefold Hodge type. The source-normalized odd packet uses the second twist: $$\mathsf M_0(2):
(2,-1)^1+(1,0)^4+(0,1)^4+(-1,2)^1.$$ Neither Hodge ledger identifies an actual Calabi--Yau variety or proves that the motive is of abelian type.

# Strictly compatible polynomials of the raw core {#sec:compatible}

Let $$\mathsf M_0=(X_{4,0},\pi_{\mathrm{core},0},0).$$ Spread $X_{4,0}$, the hyperplane class, and the rational correspondence $\pi_{\mathrm{core},0}$ over the complement of a finite set $S$ of rational primes. At $p\notin S$, specialization of the projector commutes with geometric Frobenius $F_p$.

## Rationality and coefficient-field independence

Choose an integer $D>0$ that clears the denominator of the projector. For every $m\ge1$, the trace of $\pi_{\mathrm{core},0}F_p^m$ is a rational multiple of the trace of an integral algebraic correspondence. The correspondence comparison theorem of Katz--Messing makes these traces independent of the chosen Weil cohomology, hence independent of $\ell$ [@KatzMessing1974 Theorem 2(2), pp. 76--77]. Applying Newton identities to the first ten traces gives one polynomial $$\chi_{p,\mathrm{core}}(U)
=\det(U-F_p\mid H_\ell(\mathsf M_0))\in\mathbf Q[U]
\label{eq:chi-core-Q}$$ of degree $10$, independent of $\ell$.

No semisimplicity is used. The idempotent itself decomposes the realization into its image and kernel, both stable under Frobenius.

## The separate integrality step

Denominator clearing in the cycle does not by itself prove integral coefficients. Instead, consider the full middle characteristic polynomial $$\chi_{p,H^5}(U)=\det(U-F_p\mid H^5_{\mathrm{\acute et}})
\in\mathbf Z[U].$$ The projector decomposition gives a factorization $$\chi_{p,H^5}(U)=
\chi_{p,\mathrm{core}}(U)\chi_{p,\mathrm{lev}}(U)$$ into monic polynomials in $\mathbf Q[U]$. Every root of either factor is a root of the full polynomial and is therefore an algebraic integer. The rational coefficients of each factor are algebraic integers, hence integers. Thus $$\chi_{p,\mathrm{core}}(U)\in\mathbf Z[U].$$ Reversing coefficients now gives $$P_p(T)=\det(1-F_pT\mid H_\ell(\mathsf M_0))
=T^{10}\chi_{p,\mathrm{core}}(T^{-1})\in\mathbf Z[T].
\label{eq:P-from-chi}$$ The polynomial $\chi_{p,\mathrm{core}}$ is monic; $P_p$, whose constant term is $1$, is not called monic.

## Purity and reciprocity

The roots of $\chi_{p,\mathrm{core}}$ are eigenvalues on $H^5$, so they are pure of weight $5$. The middle Poincaré pairing takes values in $\mathbf Q_\ell(-5)$, hence $$\langle F_px,F_py\rangle=p^5\langle x,y\rangle.$$ Self-transposition and idempotence give $$\ker\pi_{\mathrm{core},0}=(\operatorname{im}\pi_{\mathrm{core},0})^\perp,$$ so the restricted pairing is nondegenerate. The spread projector commutes with $F_p$, and its image is stable. Frobenius is therefore a similitude of multiplier $p^5$ on the core, and its ten eigenvalues occur in pairs $$\alpha,\quad \frac{p^5}{\alpha}.$$ Their product is $p^{25}$, and $$P_p(T)=p^{25}T^{10}P_p\left(\frac1{p^5T}\right).
\label{eq:reciprocity}$$ Writing $P_p(T)=\sum_{k=0}^{10}a_kT^k$ and comparing coefficients yields $$a_{10-k}=p^{25-5k}a_k.$$ This argument uses the invariant direct summand supplied by the idempotent, not a semisimplicity hypothesis.

Finally, geometric Frobenius acts as $p$ on $\mathbf Q_\ell(-1)$, hence as $p^{-2}$ on $\mathbf Q_\ell(2)$. The normalized core $\mathsf M_0(2)$ has weight $1$ and polynomial $$P_p^{(2)}(T)=P_p(T/p^2)\in\mathbf Q[T].$$ Its denominators are the prescribed Tate denominators, not a failure of compatibility. This completes Theorem [\[thm:compatible-main\]](#thm:compatible-main){reference-type="ref" reference="thm:compatible-main"}.

# Quadratic Artin formalism and proof boundaries {#sec:artin-scope}

Let $V$ be any of the rational realizations constructed above, and let $\chi_K$ be the quadratic character of $K/\mathbf Q$. Induction and restriction give $$\operatorname{Ind}_{G_K}^{G_\mathbf Q}\operatorname{Res}_{G_K}^{G_\mathbf Q}V
\simeq V\oplus(V\otimes\chi_K).$$ The corresponding Artin formalism [@Deligne1973 §3, Proposition 3.8] gives, away from a common finite bad set, $$L_K(V|_{G_K},s)=L_\mathbf Q(V,s)L_\mathbf Q(V\otimes\chi_K,s).
\label{eq:artin-global}$$ Equation [\[eq:artin-global\]](#eq:artin-global){reference-type="eqref" reference="eq:artin-global"} is an identity of incomplete Euler products. We do not define bad-place Weil--Deligne factors here.

At a split prime, $\chi_K(p)=1$, so the two local rational factors coincide. This is [\[eq:split-square\]](#eq:split-square){reference-type="eqref" reference="eq:split-square"}. At an inert prime, there is one $K$-place $v$ with residue field $\mathbf F_{p^2}$, and $$F_v=F_p^2.$$ If $$P_p(U)=\prod_{i=1}^r(1-\alpha_iU),$$ then $$P_{K,v}(T)=\prod_{i=1}^r(1-\alpha_i^2T),
\qquad
P_{K,v}(U^2)=P_p(U)P_p(-U).
\label{eq:inert-rule}$$ The last expression is generally not a square. The split half-power is therefore a placewise identity, not the local shadow of a global square root.

## One-prime irreducibility: exact scope

Suppose a future computation produces the full rank-$10$ polynomial $P_p(T)$ at one good prime and proves it irreducible over $\mathbf Q$. Any Chow projector over $\mathbf Q$ has a $G_\mathbf Q$-equivariant $\ell$-adic realization and hence commutes with $F_p$. If its image were nonzero and proper, the idempotent decomposition into image and kernel would factor $P_p(T)$ over $\mathbf Q$. Irreducibility would therefore exclude every rational Chow projector whose cohomological image is nonzero and proper. Semisimplicity is not needed: the idempotent itself provides the direct sum.

This criterion does not exclude a projector with zero or full realization, which would require a faithfulness or nilpotence input. Nor does it exclude projectors after extending the coefficient field, prove absolute Chow indecomposability, or imply automorphy. The uncertified pre-C53 reconnaissance anchor records only the first raw trace $-469$ at $p=7$, not the full polynomial, so the criterion remains a future gate.

## Geometric realization boundary

A conic-bundle or Prym realization is not part of the C53 certificate. A future route would first need an independent flatness theorem, followed by a discriminant and intersection-motive analysis. No such result is used in this paper.

# Exact replay and adversarial gates {#sec:replay}

The accompanying certificate implements exact arithmetic in $\mathbf Q[\rho]/(\rho^2+\rho+1)$. It checks the family formulas for $2\le n\le10$, including the cocycle, fixed basis, determinant, and rational substitutions. These finite controls test the implementation; the symbolic argument in [3](#sec:explicit-descent){reference-type="ref" reference="sec:explicit-descent"} proves the all-$n$ theorem.

For the fourth row, the replay reconstructs all twenty-four group elements, verifies the transported group law on all $24^2=576$ pairs, and partitions the elements into the two fixed points and eleven conjugate pairs. Separate gates enforce the Reynolds denominator $24$, the field transfer denominator $2$, and the distinction among the raw motive $\mathsf M_0$, its Calabi--Yau-type twist $\mathsf M_0(1)$, and the source-normalized twist $\mathsf M_0(2)$.

The local-factor gates independently test the split exponent conversion and the inert identity [\[eq:inert-rule\]](#eq:inert-rule){reference-type="eqref" reference="eq:inert-rule"}. They reject a constant rational dihedral group, an inert half-root, a rank-$255/2$ compatible system, automatic integrality after a Tate twist, and any functional equation promotion.

At the release-candidate stage, the independent checker passes all $20$ semantic gates, and the targeted mutation suite rejects all $63$ alterations. The locked certificate, payload, independent-check, and code/results-manifest SHA-256 hashes are $$\begin{split}
&\texttt{f4325a5987933e2acf81656389d46701d82d38912c546d1e5996123f617f6e79},\\
&\texttt{8064224eda63fa9d890efd26ec9aa167c7cd9458662620be3135196a09494d41},\\
&\texttt{0d38643ded626c2a5e1536c8a4df9c56ae98c4fda01e1d15660996ea8c495e67},\\
&\texttt{b62f353d119d6c8565f513dad771a047a5e6343411d08ad2e91562fe84923480}.
\end{split}$$ They form the final code/results evidence tuple. The full-project manifest and implementation-provenance backfill are separate release-integration steps.

The $p=7$ value is labeled . It records raw core trace $-469$, or $-67/7$ after the second Tate twist. The checker verifies the recorded arithmetic but does not independently reconstruct the fixed-locus counts, and no C52 provenance is asserted. This paper is not a table of Frobenius traces, and the anchor is not used to infer irreducibility.

# Limitations and reproducibility

#### Limitations.

The explicit equation descent holds for every $n\ge2$, but the smooth motivic packet is certified only for $n=2,3,4$. The exponent-one fourth-row factor is proved only at good split primes. The paper does not construct bad local factors, a global half-root, analytic continuation, a functional equation, automorphy, an actual Calabi--Yau threefold, or an all-correspondence indecomposability theorem.

#### Reproducibility.

The certificate records the C52 implementation commit $$\text{\ttfamily 208feef86365cd92ace8dad02904acff6623eeec}$$ and the frozen C52 certificate hash $$\text{\footnotesize\ttfamily
a2b0b281bfb311f979c7ed65e441a184ebe338b05f5fec8a60768610965c9c94}.$$ The producer and independent checker use separate exact arithmetic paths. The default runner regenerates the certificate in a temporary directory, compares bytes, executes the mutation suite, and verifies the manifest. No fitted parameter, floating-point theorem gate, zero table, or post-hoc local projector is used.

#### Data and ethics.

The work uses generated exact algebraic data and public mathematical literature; it involves no human subjects or personal data. The source chronology and every excluded promotion are machine-gated.

# Additional proof details {#app:proof-details}

## The fourth fixed matrix

In the ordered variables $(u_0,u_1,v_1,u_2,v_2,u_3,v_3,u_4)$, the coordinate change is $$\begin{pmatrix}
x_0\\x_1\\x_2\\x_3\\x_4\\x_5\\x_6\\x_7
\end{pmatrix}
=
\begin{pmatrix}
u_0\\
u_1+\theta v_1\\
u_2+\theta v_2\\
u_3+\theta v_3\\
(1+\rho)u_4\\
u_3-\theta v_3\\
\rho(u_2-\theta v_2)\\
u_1-\theta v_1
\end{pmatrix}.$$ The semilinear reversal is $$M_4(x_0,\ldots,x_7)
=(x_0,x_7,\rho x_6,x_5,\rho x_4,x_3,\rho x_2,x_1).$$ Direct conjugation gives $M_4\tau(B_4)=B_4$, and $$\det B_4=(2\theta)^3\rho(1+\rho)=24\theta.$$

## The quadratic edge ledger

For completeness, the transformed quadric has three edge classes: $$\begin{array}{ccl}
i=0&:&x_0x_1\mapsto x_0x_{N-1}
       \quad\text{with phase }1,\\
1\le i\le N-2&:&x_ix_{i+1}\mapsto
       x_{N-i}x_{N-i-1}
       \quad\text{with phase }\rho,\\
\text{closing}&:&\rho x_{N-1}x_0\mapsto
       \rho x_1x_0.
\end{array}$$ Thus the transformed closing coefficient is $1$ and every nonclosing coefficient is $\rho$. Since $\rho\cdot\rho^2=1$, this is exactly $\rho Q_{n,\rho^2}$.

## The transported group automorphism

Let $t=sr^{-1}$. Then $$t^2=sr^{-1}sr^{-1}=1,\qquad
t r^{-1}t=r.$$ Therefore $r\mapsto r^{-1}$, $s\mapsto t$ respects the dihedral presentation and defines an automorphism. It fixes $r^k$ only when $2k=0\bmod12$, giving $1,r^6$, and fixes no reflection because $2k=1\bmod12$ has no solution. Hence the Galois orbits have sizes $$1,1,\underbrace{2,\ldots,2}_{11\text{ times}}.$$ The twist is outer. Indeed, an inner automorphism that inverts $r$ is conjugation by a reflection, and sends $s$ to $r^{2a}s$ for some $a$; it cannot send $s$ to $rs$.

## Correspondence identities after transfer

Over $K$, $$e_G^2=e_G,\qquad {}^te_G=e_G,\qquad e_G\pi_5=\pi_5e_G.$$ The first formula follows by counting the $24$ pairs $(g,h)$ with $gh=k$ for each $k\in G$; the second uses closure under inversion; the third uses preservation of the hyperplane class. Pullback of $e_{\mathscr G}=2^{-1}q_*e_G$ is $e_G$. Since $q^*$ is injective on rational Chow groups, all three identities hold over $\mathbf Q$. They imply $$\pi_{\mathrm{core},0}^2=\pi_{\mathrm{core},0},\quad
\pi_{\mathrm{lev},0}^2=\pi_{\mathrm{lev},0},\quad
\pi_{\mathrm{core},0}\pi_{\mathrm{lev},0}=0,$$ and self-transposition of both projectors.

## Four steps in reciprocity

The coefficient relation in Theorem [\[thm:compatible-main\]](#thm:compatible-main){reference-type="ref" reference="thm:compatible-main"} uses the following four facts.

1.  The middle Poincaré pairing is $$H^5\times H^5\longrightarrow\mathbf Q_\ell(-5).$$ With geometric Frobenius, $\langle F_px,F_py\rangle=p^5\langle x,y\rangle$.

2.  Since $\pi_{\mathrm{core},0}$ is a self-transpose idempotent, $$\ker\pi_{\mathrm{core},0}=(\operatorname{im}\pi_{\mathrm{core},0})^\perp.$$ The pairing restricted to its image is therefore nondegenerate.

3.  The spread projector is defined over $\mathbf F_p$, so it commutes with $F_p$; its image is Frobenius-stable.

4.  A Frobenius similitude of multiplier $p^5$ on this ten-dimensional nondegenerate summand has eigenvalues paired as $\alpha,p^5/\alpha$. Comparing coefficients in [\[eq:reciprocity\]](#eq:reciprocity){reference-type="eqref" reference="eq:reciprocity"} gives $$a_{10-k}=p^{25-5k}a_k.$$

No diagonalization or semisimplicity hypothesis enters these steps.

## Why one trace is not a polynomial

The uncertified pre-C53 reconnaissance anchor at $p=7$ records $$\operatorname{tr}(F_7\mid\mathsf M_0)=-469,
\qquad a_1=469.$$ Reciprocity then determines $a_9=7^{20}a_1$ and $a_{10}=7^{25}$, but leaves $a_2,a_3,a_4,a_5$ undetermined. The first trace therefore cannot certify irreducibility or a complete Euler factor.
