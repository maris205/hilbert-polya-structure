---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-mu3-universal-dihedral-denominator-rigidity"
canonical_tex: "henon_dynamics/henon_mu3_universal_dihedral_denominator_rigidity/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_mu3_universal_dihedral_denominator_rigidity/paper/main.pdf"
source_sha256: "0ab8b1515e4b11be310268c7479093995973d65c3587baeeb4f9259d5b64c6c9"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Universal Dihedral Symmetry and Split-Denominator Rigidity in a Cubic--Quadric Source Tower

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_mu3_universal_dihedral_denominator_rigidity>)
- [规范 TeX](<../../../../../henon_dynamics/henon_mu3_universal_dihedral_denominator_rigidity/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_mu3_universal_dihedral_denominator_rigidity/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_mu3_universal_dihedral_denominator_rigidity/README.md>)
- [BibTeX](<../../../../../henon_dynamics/henon_mu3_universal_dihedral_denominator_rigidity/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For $K=\mathbf Q(\rho)$, $\rho^2+\rho+1=0$, consider the source-ordered cubic--quadric pair $$C_n=\sum_{i=0}^{2n-1}x_i^3,\qquad
  Q_{n,\rho}=\sum_{i=0}^{2n-2}x_ix_{i+1}
               +\rho x_{2n-1}x_0.$$ We classify its full projective monomial ideal stabilizer for every $n\ge2$: it is $\operatorname{Dih}(C_{3n})$ of order $6n$. Transport through the inherited semilinear rational descent gives a nonconstant finite etale $\mathbf Q$-group scheme of rank $6n$ with exactly two rational geometric elements. These are unconditional equation-level results. For a packet-admissible smooth row, the inherited rational compatible realizations have pure weights zero and one and ranks $(4^n+5)/3$ and $2(4^n-4)/3$. We prove that an actual finite-rank rational compatible system realizes the complete prescribed split-local exponent $4/n$ if and only if $n\mid4$; hence the only rows $n\ge2$ are $2$ and $4$. The inherited packet data are currently certified only for $n=2,3,4$, and no semisimplicity theorem is imported. At $n=3$, an exact residue-corrected $\operatorname{Dih}(C_9)$-character calculation over the common geometric source field shows that no nonzero central source-isotypic sector clears the $4/3$ factor on both pure rails. Split-invisible virtual rational classes restrict to zero and cannot change that obstruction. The classification is local to good split primes; it supplies no inert or global root, automorphy, continuation, functional equation, or RH statement.
author:
- 'Hilbert--Pólya Dynamical Structure Exploration Project'
bibliography:
- references.bib
date: August 2026
title: |
  Universal Dihedral Symmetry and Split-Denominator Rigidity\
  in a Cubic--Quadric Source Tower
```

## Markdown 正文

# Introduction {#sec:introduction}

Rational descent changes the multiplicity problem in the Hénon moment source tower. At a good rational prime split in $K=\mathbf Q(\rho)$, the two equal $K$-place factors convert the inherited exponent $2/n$ into $4/n$ on one rational factor. The fourth row therefore becomes ordinary. Here and throughout, *ordinary* is project shorthand for realization by an actual finite-rank compatible system with integral multiplicities; it is unrelated to $p$-adic or Newton-polygon ordinarity. Two questions remain: whether any other row can be ordinary without changing the split Euler object, and whether source symmetry can isolate an integral sector when the whole packet remains fractional.

Both questions require a universal source theorem. Constructing a dihedral subgroup in a few rows is insufficient: a missing projective monomial stabilizer could provide a new central projector. Conversely, a full projective automorphism theorem would be stronger than the available equation algebra. We work in the exact intermediate category: monomial matrices in $\operatorname{PGL}$ that stabilize the homogeneous ideal of the cubic--quadric pair. An edge-phase recurrence enumerates this group without assuming smoothness.

The arithmetic obstruction also needs two distinct weights. At $n=3$, the scaled total rank is the integer $84$, while the separate scaled ranks are $92/3$ and $160/3$. A total-rank calculation therefore gives the wrong answer. We instead restrict a putative rational compatible realization to $G_K$, fix a coefficient prime $\ell$, and take semisimplifications. This operation preserves traces, characteristic polynomials, ranks, and purity; it does not assert that the inherited packet is semisimple. Chebotarev and Brauer--Nesbitt then separate the two pure rails and turn the problem into exact divisibility.

## Contributions {#contributions .unnumbered}

The paper proves four claims.

1.  For every $n\ge2$, the full projective monomial stabilizer of the homogeneous ideal is $$\operatorname{PMonStab}(C_n,Q_{n,\rho})\cong\operatorname{Dih}(C_{3n}),\qquad |G_n|=6n.$$ The support quotient contains exactly the even rotations and odd reflections of the $2n$-cycle.

2.  The inherited semilinear reversal transports generators by $$r\longmapsto r^{-1},\qquad s\longmapsto rs.$$ It gives a nonconstant finite etale rational group scheme of rank $6n$ with exactly two rational geometric elements.

3.  For every packet-admissible row, an actual rational compatible system matches the prescribed split trace if and only if $n\mid4$. The same classification holds for the stronger complete split-local factor identity. The inherited packet data cover $n=2,3,4$, not every $n$.

4.  Over the common geometric group at $n=3$, we compute both pure characters exactly and prove that no nonzero central source-isotypic summand clears the $4/3$ denominator. We also show that a split-invisible virtual rational counterpacket restricts to zero over $K$ and cannot alter the rank or character obstruction.

## Relation to primary work {#relation-to-primary-work .unnumbered}

Brünjes identifies the full projective monomial group of a Fermat form and the one-dimensional primitive character sectors [@Brunjes2003 Proposition 3.8, Lemma/Definition 4.3, and Theorem 4.6]. Our cubic--quadric stabilizer is the intersection with a weighted chronological cycle and requires the new closure recurrence. Nagel's general Cayley-ring theorem gives $H_{\mathrm{var}}^{n-p,p}\cong R_{p,d(X)}$ [@Nagel1997 Proposition 2.16]; for the present threefold it yields $H^{2,1}\cong R_{1,-1}$. Favero--Iliev--Katzarkov provide a $(2,3)$ fivefold instance of the Cayley/Jacobian method [@FaveroIlievKatzarkov2014 §5.4]. Their $\mathbf P^7$ formula is context rather than a locator for our threefold character.

Purity is inherited from the standard Weil-theoretic framework [@Deligne1980]. The density and character-rigidity inputs are Chebotarev in Serre's formulation [@Serre1981 §2.1, Theorem 1] and the characteristic-zero Brauer--Nesbitt consequence [@BrauerNesbitt1941]. These sources provide general tools, not the rank arithmetic or the source-specific characters. A bounded arXiv/Crossref search found no exact statement of the simultaneous stabilizer or the $n\mid4$ classification; this is a search record, not a database-exhaustive priority claim.

## Scope {#scope .unnumbered}

The all-$n$ statements concern equations and a finite group form. Smoothness and rational packet data are inherited only in rows $2,3,4$; rows $n\ge5$ are conditional. The word full always modifies *projective monomial ideal stabilizer*, not the full PGL automorphism group. The third-row common character is first a theorem over $K$; a common rational group-scheme action requires a twisted Fermat descent datum. Finally, every ordinary-realization statement is local to good split primes. No global or inert root, bad-place package, automorphy, continuation, functional equation, or RH statement is proved.

::: {#tab:position}
  Question                   Nearest input                                             Result here
  -------------------------- --------------------------------------------------------- ------------------------------------------------------------
  Fermat monomial symmetry   Full Fermat projective monomial group                     Full simultaneous cubic--quadric projective monomial group
  Cayley cohomology          General bigraded identification and a fivefold instance   Exact residue-corrected $G_3$-character in dimension three
  Rational split exponent    Exponent $4/n$ after quadratic descent                    Actual complete split-factor realization iff $n\mid4$

  : The paper classifies the simultaneous source pair and its prescribed split multiplicity; it does not enlarge the geometric or analytic category.
:::

# The source ideal and the monomial category {#sec:source-category}

Let $$K=\mathbf Q(\rho),\qquad \rho^2+\rho+1=0,\qquad
N=2n,\qquad n\ge2,$$ and set $$C_n=\sum_{i=0}^{N-1}x_i^3,\qquad
Q_{n,\rho}=\sum_{i=0}^{N-2}x_ix_{i+1}
             +\rho x_{N-1}x_0.
\label{eq:source-pair}$$ The variable order and the coefficient of the closing edge are part of the source datum. Write $$X_n=V(C_n,Q_{n,\rho})\subset\mathbf P_K^{N-1}.$$ No smoothness assumption is needed until correspondences or compatible packets are introduced.

[\[def:pmon\]]{#def:pmon label="def:pmon"} $\operatorname{PMonStab}(C_n,Q_{n,\rho})$ is the subgroup of $\operatorname{PGL}_N(K)$ represented by monomial matrices that stabilize the homogeneous ideal $(C_n,Q_{n,\rho})$.

This definition does not identify the group with $\operatorname{Aut}_{\operatorname{PGL}}(X_n)$. Nonmonomial automorphisms are outside the theorem.

[\[lem:ideal-lines\]]{#lem:ideal-lines label="lem:ideal-lines"} Every element of $\operatorname{PMonStab}(C_n,Q_{n,\rho})$ preserves the two equation lines $KC_n$ and $KQ_{n,\rho}$.

The degree-two part of the ideal is $KQ_{n,\rho}$, so an ideal stabilizer scales the quadric. In degree three it has $$g^*C_n=aC_n+LQ_{n,\rho}$$ for $a\in K$ and a linear form $L$. The monomial pullback $g^*C_n$ and $aC_n$ contain only pure cubes. Since every monomial in $Q_{n,\rho}$ is a product of two distinct variables, $LQ_{n,\rho}$ has no pure-cube monomial. Pure-cube coefficient comparison gives $g^*C_n=aC_n$. Then $LQ_{n,\rho}=0$, and the polynomial ring is a domain, so $L=0$.

Represent a projective monomial element by $$x_i\longmapsto\lambda_i x_{\sigma(i)}.$$ Lemma [\[lem:ideal-lines\]](#lem:ideal-lines){reference-type="ref" reference="lem:ideal-lines"} implies $\lambda_i^3=a$ for every $i$. Divide the lift by $\lambda_0$. The normalized representative is $$x_i\longmapsto\rho^{e_i}x_{\sigma(i)},\qquad
e_i\in\mathbf F_3,\qquad e_0=0.
\label{eq:normalized-map}$$ The support of the quadric is the $N$-cycle, so $\sigma$ lies in its dihedral permutation group.

There is one further derived normalization. If $g^*Q_{n,\rho}=\beta Q_{n,\rho}$, compare any transformed edge coefficient with the coefficient on its target edge. Both belong to $\mu_3$, because the source coefficients and the normalized diagonal phases do. Their ratio is $\beta$. Consequently $$\beta=\rho^q\qquad\text{for a unique }q\in\mathbf F_3.
\label{eq:q-derived}$$ Thus the phase $q$ used below is forced by ideal stabilization rather than added as an assumption.

# The universal projective monomial group {#sec:universal-group}

Our convention is $$\operatorname{Dih}(C_m)=
\langle r,s\mid r^m=s^2=1,\ srs=r^{-1}\rangle,$$ which has order $2m$.

[\[thm:universal-group\]]{#thm:universal-group label="thm:universal-group"} For every $n\ge2$, $$G_n:=\operatorname{PMonStab}(C_n,Q_{n,\rho})
\cong\operatorname{Dih}(C_{3n}),\qquad |G_n|=6n.$$ The support map gives an exact sequence $$1\longrightarrow C_3\longrightarrow G_n
\longrightarrow\operatorname{Dih}(C_n)\longrightarrow1,$$ where the support image consists of the even rotations and odd reflections of the $2n$-cycle.

## The edge recurrence

Let $E_j=\{j,j+1\}$, with indices modulo $N$, and set $$c_j=\begin{cases}
1,&j=N-1,\\
0,&0\le j<N-1.
\end{cases}$$ For the normalized map [\[eq:normalized-map\]](#eq:normalized-map){reference-type="eqref" reference="eq:normalized-map"}, write the forced quadric scale as $\rho^q$ using [\[eq:q-derived\]](#eq:q-derived){reference-type="eqref" reference="eq:q-derived"}. Coefficient comparison on the image of $E_j$ gives $$e_{j+1}=q+c_{\sigma(E_j)}-c_j-e_j\pmod3.
\label{eq:edge-recurrence}$$ For fixed $\sigma,q,e_0$, this recurrence has at most one phase solution.

[\[lem:closure-parity\]]{#lem:closure-parity label="lem:closure-parity"} Let $j_*$ be the unique index such that $\sigma(E_{j_*})=E_{N-1}$. The solution of [\[eq:edge-recurrence\]](#eq:edge-recurrence){reference-type="eqref" reference="eq:edge-recurrence"} closes at $e_N=e_0$ if and only if $j_*$ is odd.

Iterating the recurrence gives $$e_N-e_0=
\sum_{j=0}^{N-1}(-1)^{N-1-j}
\bigl(q+c_{\sigma(E_j)}-c_j\bigr).$$ Because $N$ is even, the alternating sum of the $q$-terms is zero. Only $j_*$ contributes to the first closing-edge indicator, and only $N-1$ contributes to the second. The remaining expression is $$(-1)^{N-1-j_*}-1.$$ It vanishes exactly when $j_*$ is odd.

For a rotation $\sigma(i)=i+k$, the preimage index is $j_*=N-1-k$. The closure condition is therefore $k$ even. For a reflection $\sigma(i)=k-i$, the preimage index is $j_*=k$, so $k$ must be odd. There are $n$ surviving supports of each type. The closure condition is independent of $q$, and each $q\in\mathbf F_3$ yields one normalized lift. Hence the exhaustive list contains $$3(n+n)=6n
\label{eq:group-count}$$ elements.

## Generators and presentation

Define $$(rx)_i=\rho^{a_i}x_{i+2},\qquad
a_i=
\begin{cases}
1,&i=N-2,\\
2,&i=N-1,\\
0,&\text{otherwise},
\end{cases}
\label{eq:r-generator}$$ and $$(sx)_i=\rho^{b_i}x_{1-i},\qquad
b_i=
\begin{cases}
1,&i=1\text{ or }(i\ge2\text{ even}),\\
0,&\text{otherwise}.
\end{cases}
\label{eq:s-generator}$$ The phases cube to one. Edge substitution gives $$Q_{n,\rho}(rx)=Q_{n,\rho}(x),\qquad
Q_{n,\rho}(sx)=\rho Q_{n,\rho}(x).$$ Thus $r,s\in G_n$.

The support of $r$ has order $n$, while phase accumulation gives $$r^n=\operatorname{diag}(1,\rho,1,\rho,\ldots,1,\rho)
\quad\text{in }\operatorname{PGL}_N.
\label{eq:r-power-n}$$ The right side has order three, so $r$ has exact order $3n$. Direct support and phase composition gives $$s^2=1,\qquad srs=r^{-1}.$$ Every element of $\langle r\rangle$ has rotation support, whereas $s$ has reflection support. Hence $s\notin\langle r\rangle$. Since $r$ has order $3n$, the elements $$r^k,\quad r^ks,\qquad 0\le k<3n,$$ are $6n$ distinct elements of $\langle r,s\rangle$. This subgroup lies in the exhaustive $6n$-element stabilizer list, so the two sets coincide. This proves the group isomorphism in Theorem [\[thm:universal-group\]](#thm:universal-group){reference-type="ref" reference="thm:universal-group"}.

The support kernel is $\{1,r^n,r^{2n}\}\cong C_3$. The support image has order $2n$ and is the subgroup of even rotations and odd reflections, isomorphic to $\operatorname{Dih}(C_n)$. This proves the exact sequence.

Theorem [\[thm:universal-group\]](#thm:universal-group){reference-type="ref" reference="thm:universal-group"} is equation algebra in characteristic zero. It neither assumes nor proves that $X_n$ is smooth, and it does not classify nonmonomial projective automorphisms.

# The nonconstant rational group form {#sec:rational-form}

Let $\tau$ denote the nontrivial element of $\operatorname{Gal}(K/\mathbf Q)$, so that $\tau(\rho)=\rho^2$. Define $$\eta_0=0,\qquad
\eta_i=
\begin{cases}
1,&i\ne0\text{ is even},\\
0,&i\text{ is odd},
\end{cases}$$ and let the inherited semilinear reversal have linear part $$(M_nx)_i=\rho^{\eta_i}x_{-i}.
\label{eq:descent-matrix}$$ Direct substitution gives $$C_n(M_nx)=C_n(x),\qquad
Q_{n,\rho}(M_nx)=\rho Q_{n,\rho^2}(x),\qquad
M_n\tau(M_n)=I.
\label{eq:descent-identities}$$ Thus $M_n\circ\tau$ is a descent datum for the equation pair. This equation-level statement is available for every $n\ge2$; it does not assert smoothness or produce a motive in a new row.

[\[thm:rational-form\]]{#thm:rational-form label="thm:rational-form"} Transport through [\[eq:descent-matrix\]](#eq:descent-matrix){reference-type="eqref" reference="eq:descent-matrix"} acts on $G_n=\operatorname{Dih}(C_{3n})$ by $$\delta(g)=M_n\tau(g)M_n^{-1},\qquad
\delta(r)=r^{-1},\qquad
\delta(s)=rs=sr^{-1}.
\label{eq:galois-action}$$ Consequently $G_n$ descends to a finite ${\rm etale}$ $\mathbf Q$-group scheme $\mathscr G_n$ of rank $6n$, split by $K$. It is nonconstant and has exactly two rational geometric elements: $$\mathscr G_n(\mathbf Q)=
\begin{cases}
\{1,r^{3n/2}\},&n\text{ even},\\
\{1,r^{(3n+1)/2}s\},&n\text{ odd}.
\end{cases}$$ In particular, $\mathscr G_n(\mathbf Q)\cong C_2$.

Apply $\tau$ to the phases in [\[eq:r-generator\]](#eq:r-generator){reference-type="eqref" reference="eq:r-generator"}--[\[eq:s-generator\]](#eq:s-generator){reference-type="eqref" reference="eq:s-generator"}, conjugate the supports and phases by $M_n$, and compare with the same normalized generators. The phase identities give exactly [\[eq:galois-action\]](#eq:galois-action){reference-type="eqref" reference="eq:galois-action"}. Since this is a Galois action by group automorphisms, standard finite Galois descent produces the asserted finite etale group scheme.

For rotations and reflections, respectively, $$\delta(r^k)=r^{-k},\qquad
\delta(r^ks)=r^{1-k}s.$$ The fixed-point congruences are therefore $$2k\equiv0\pmod{3n},\qquad
2k\equiv1\pmod{3n}.$$ If $n$ is even, the first congruence has the two solutions $0,3n/2$ and the second has none. If $n$ is odd, the first has only $0$ and the second has the unique solution $(3n+1)/2$. This proves the displayed list. Since $6n>2$, not every geometric element is fixed; the rational group scheme is nonconstant.

## Reynolds averaging and quadratic transfer

Only on a certified smooth row do the automorphism graphs define the correspondences used here. Over $K$, the geometric Reynolds idempotent is $$e_{G_n}=\frac{1}{6n}\sum_{g\in G_n}\Gamma_g.
\label{eq:reynolds}$$ It includes all $6n$ graphs, not merely the rotation subgroup. If $\pi$ denotes quadratic base change from the rational descended row, its rational transfer is $$e_{\mathscr G_n}=\frac12\pi_*e_{G_n},\qquad
\pi^*e_{\mathscr G_n}=e_{G_n}.
\label{eq:quadratic-transfer}$$ The denominator $6n$ in Reynolds averaging and the denominator $2$ in Galois transfer have different origins and must not be combined. Neither [\[eq:reynolds\]](#eq:reynolds){reference-type="eqref" reference="eq:reynolds"} nor [\[eq:quadratic-transfer\]](#eq:quadratic-transfer){reference-type="eqref" reference="eq:quadratic-transfer"} promotes the equation-level all-$n$ theorem to an all-$n$ Chow statement.

# Ordinary split-factor rigidity {#sec:denominator}

[\[def:packet-admissible\]]{#def:packet-admissible label="def:packet-admissible"} A row $n$ is packet-admissible if the source is smooth and actual rational compatible realizations $\mathsf E_n$ and $\mathsf O_n$ have been constructed, pure of weights zero and one, with $$e_n:=\operatorname{rank}\mathsf E_n=\frac{4^n+5}{3},\qquad
o_n:=\operatorname{rank}\mathsf O_n=\frac{2(4^n-4)}{3}=2(e_n-3).
\label{eq:rail-ranks}$$

The inherited construction certifies this packet data for $n=2,3,4$. It does not certify semisimplicity, and it does not establish packet-admissibility for $n\ge5$. Every result in this section is conditional on Definition [\[def:packet-admissible\]](#def:packet-admissible){reference-type="ref" reference="def:packet-admissible"}.

For a good rational prime $p$, use geometric Frobenius and write $$L_p(\mathsf V,u)
=\det(1-F_pu\mid\mathsf V)^{-1},
\qquad
\operatorname{Log}_0L_p(\mathsf V,u)
=\sum_{m\ge1}\frac{\operatorname{Tr}(F_p^m\mid\mathsf V)}{m}u^m.$$

[\[thm:denominator\]]{#thm:denominator label="thm:denominator"} Let $n\ge2$ be packet-admissible. The following are equivalent.

1.  There is an actual finite-rank rational compatible system $\mathsf V_n$ such that, at every good rational prime $p$ split in $K$, $$\operatorname{Tr}(F_p\mid\mathsf V_n)
    =\frac4n\operatorname{Tr}(F_p\mid\mathsf E_n\oplus\mathsf O_n).$$

2.  There is such a system satisfying, at every good split prime, $$\operatorname{Log}_0L_p(\mathsf V_n,u)
    =\frac4n\operatorname{Log}_0L_p(\mathsf E_n\oplus\mathsf O_n,u).$$

3.  $n\mid4$.

Hence the only possible rows $n\ge2$ are $n=2$ and $n=4$.

Condition (ii) implies (i) by comparing the coefficient of $u$. Assume (i), fix a coefficient prime $\ell$, restrict all three $\ell$-adic realizations to $G_K$, and then take semisimplifications. This last operation preserves traces, characteristic polynomials, ranks, and the purity of the two inherited rails. In particular, it is not an assertion that the original packet systems are semisimple.

After enlarging to one finite coefficient extension $E_\ell/\mathbf Q_\ell$, choose a common finite set $S$ containing $\ell$, ramification, and all bad primes in scope. The Grothendieck group below is generated by the finite-dimensional continuous semisimple $E_\ell$-representations obtained from these fixed-$\ell$ realizations, unramified outside $S$; it is not an unrestricted representation category.

Outside finitely many excluded primes, the degree-one prime ideals of $K$ lie over split rational primes, and they form a Dirichlet-density-one set. The assumed trace identity therefore holds on a dense set of Frobenius classes for $G_K$. Chebotarev density [@Serre1981 §2.1, Theorem 1] and the characteristic-zero Brauer--Nesbitt consequence [@BrauerNesbitt1941] give $$n[(\operatorname{Res}V_{n,\ell})^{\mathrm{ss}}]
=4[(\operatorname{Res}E_{n,\ell})^{\mathrm{ss}}]
+4[(\operatorname{Res}O_{n,\ell})^{\mathrm{ss}}]
\label{eq:k0-identity}$$ in the semisimple Grothendieck group.

The two right-hand summands have different pure weights [@Deligne1980 §1.2, especially (1.2.2) and (1.2.5)(i)], so they have no common irreducible constituent. Separating [\[eq:k0-identity\]](#eq:k0-identity){reference-type="eqref" reference="eq:k0-identity"} by weight and then taking ranks forces $$n\mid4e_n,\qquad n\mid4o_n.
\label{eq:rank-divisibility}$$ Since $o_n=2(e_n-3)$, these congruences imply $n\mid8e_n$ and $n\mid8(e_n-3)$; subtraction gives $n\mid24$. The remaining finite check is

        $n$         $2$   $3$   $4$   $6$   $8$   $12$   $24$
  --------------- ----- ----- ----- ----- ----- ------ ------
   $4e_n\bmod n$    $0$   $2$   $0$   $2$   $4$    $8$   $20$
   $4o_n\bmod n$    $0$   $1$   $0$   $4$   $0$    $4$   $16$

Only $n=2,4$ satisfy both congruences.

Conversely, if $n\mid4$, define the actual system $$\mathsf V_n=
\mathsf E_n^{\oplus 4/n}\oplus
\mathsf O_n^{\oplus 4/n}.
\label{eq:direct-copy-converse}$$ It matches every Frobenius power trace at every good prime. The defining series for $\operatorname{Log}_0$ then proves (ii), completing the equivalence.

[\[rem:total-rank\]]{#rem:total-rank label="rem:total-rank"} At $n=3$, $$\frac43(e_3+o_3)=\frac43\cdot63=84$$ is integral, but the separate scaled ranks are $$\frac43e_3=\frac{92}{3},\qquad
\frac43o_3=\frac{160}{3}.$$ The weight separation in [\[eq:k0-identity\]](#eq:k0-identity){reference-type="eqref" reference="eq:k0-identity"}, rather than the total rank, is the decisive step.

# The exact third-row common-group obstruction {#sec:n3-character}

Throughout this section the common geometric source group is taken over $K$: $$G_3=\operatorname{Dih}(C_9),\qquad |G_3|=18.$$ It has one identity, nine reflections of order two, two nonidentity rotations of order three, and six rotations of order nine. Let $\varepsilon$ be the reflection-sign representation. For $1\le j\le4$, let $U_j$ denote the two-dimensional irreducible with $$\chi_{U_j}(r^k)=\zeta_9^{jk}+\zeta_9^{-jk},\qquad
\chi_{U_j}(r^ks)=0.
\label{eq:dihedral-irreducibles}$$

## The Cayley quotient and residue action

Nagel's complete-intersection identification is $$H_{\mathrm{var}}^{n-p,p}(X)\cong R_{p,d(X)},\qquad
d(X)=\sum_i d_i-n-r-2$$ [@Nagel1997 Proposition 2.16]. In the present $(2,3)$ threefold, $n=3$, $r=1$, and $\sum_i d_i=5$, so $d(X)=-1$. With $p=1$, this gives the precise specialization $$H^{2,1}(X_3)=H_{\mathrm{var}}^{2,1}(X_3)
\cong R_{1,-1}.
\label{eq:nagel-specialization}$$ The $\mathbf P^7$ fivefold calculation in [@FaveroIlievKatzarkov2014 §5.4] is useful context for the Cayley bigrading, but it is not the locator for [\[eq:nagel-specialization\]](#eq:nagel-specialization){reference-type="eqref" reference="eq:nagel-specialization"}.

For the Cayley polynomial $yC_3+zQ_{3,\rho}$, bidegree $(1,-1)$ has the 27 monomials $$zx_i\quad(0\le i<6),\qquad
yx_ix_j\quad(0\le i\le j<6).$$ The relevant Jacobian subspace is generated by the six relations $$3yx_i^2+z\frac{\partial Q_{3,\rho}}{\partial x_i},
\qquad 0\le i<6,
\label{eq:cayley-derivatives}$$ and by $yQ_{3,\rho}$. These seven vectors are linearly independent over $K$, so $$\dim R_{1,-1}=27-7=20.
\label{eq:cayley-dimension}$$

If $M_g$ is the coordinate matrix and $A_g$ is the induced matrix on the two-dimensional equation space, polynomial pullback alone is not the cohomological action. The residue action is $$T_g=\frac{\det M_g}{\det A_g}\,T_g^{\mathrm{poly}}.
\label{eq:residue-correction}$$ The determinant ratio is essential: omitting or inverting it changes the character.

[\[thm:n3-character\]]{#thm:n3-character label="thm:n3-character"} The residue-corrected action on $H^{2,1}(X_3)$ has rotation traces $$\bigl(\operatorname{Tr}(r^k)\bigr)_{k=0}^{8}
=(20,-1,-1,2,-1,-1,2,-1,-1)$$ and trace $-2$ on every reflection. Consequently $$\begin{aligned}
H^{2,1}(X_3)
&=2\varepsilon+2U_1+2U_2+3U_3+2U_4,
\label{eq:h21-decomposition}\\
\mathsf O_3
&=4\varepsilon+4U_1+4U_2+6U_3+4U_4.
\label{eq:odd-decomposition}\end{aligned}$$ For the Fermat rail, including its additional trivial line, $$\bigl(\operatorname{Tr}(r^k\mid\mathsf E_3)\bigr)_{k=0}^{8}
=(23,2,2,-4,2,2,-4,2,2),$$ every reflection has trace $-1$, and $$\mathsf E_3
=\mathbf 1+2\varepsilon+3U_1+3U_2+U_3+3U_4.
\label{eq:even-decomposition}$$

The matrices induced by $r$ and $s$ preserve the seven-dimensional relation space generated by [\[eq:cayley-derivatives\]](#eq:cayley-derivatives){reference-type="eqref" reference="eq:cayley-derivatives"} and $yQ_{3,\rho}$. Taking the trace on the 27-dimensional monomial space, subtracting the trace on that relation space, and multiplying by the residue factor [\[eq:residue-correction\]](#eq:residue-correction){reference-type="eqref" reference="eq:residue-correction"} gives the displayed rotation and reflection traces. Inner products with the six irreducible characters $\mathbf 1,\varepsilon,U_1,\ldots,U_4$ give [\[eq:h21-decomposition\]](#eq:h21-decomposition){reference-type="eqref" reference="eq:h21-decomposition"}. The character is real, and adjoining its Hodge conjugate doubles the multiplicities, yielding [\[eq:odd-decomposition\]](#eq:odd-decomposition){reference-type="eqref" reference="eq:odd-decomposition"}.

For the Fermat rail, the primitive Jacobian ring is $$K[x_0,\ldots,x_5]/(x_0^2,\ldots,x_5^2).$$ The relevant squarefree degrees are $0,3,6$. Fixed-monomial traces, multiplied by the residue factor $\det M_g$, and the extra trivial line give the second trace vector. The same character inner products yield [\[eq:even-decomposition\]](#eq:even-decomposition){reference-type="eqref" reference="eq:even-decomposition"}. The exact trace-to-multiplicity ledger is recorded in Appendix [10](#app:proof-ledgers){reference-type="ref" reference="app:proof-ledgers"}.

[\[cor:no-central-sector\]]{#cor:no-central-sector label="cor:no-central-sector"} No nonzero central $G_3$-isotypic summand of $\mathsf E_3\oplus\mathsf O_3$ has multiplicity divisible by three on both pure rails.

The multiplicities are

      sector        $\mathbf 1$   $\varepsilon$   $U_1$   $U_2$   $U_3$   $U_4$
  --------------- ------------- --------------- ------- ------- ------- -------
   $\mathsf E_3$            $1$             $2$     $3$     $3$     $1$     $3$
   $\mathsf O_3$            $0$             $4$     $4$     $4$     $6$     $4$

Scaling an isotypic summand by $4/3$ is integral only if its multiplicity is divisible by three. Every column fails this test on at least one rail, so no nonempty collection of central isotypic sectors works. Over the rational coefficient field, $U_1,U_2,U_4$ form one Galois orbit block. Its multiplicity pair remains $(3,4)$, and therefore coefficient-field packaging does not remove the obstruction.

[\[rem:common-group\]]{#rem:common-group label="rem:common-group"} Theorem [\[thm:n3-character\]](#thm:n3-character){reference-type="ref" reference="thm:n3-character"} is first a theorem for the common geometric $G_3$-action over $K$. The Fermat packet in its standard rational form and the complete intersection with $M_3$-descent need not carry the same rational group scheme. A formulation under one $\mathscr G_3$ uses the $M_3$-twisted rational form of the Fermat rail. That twist preserves the split trace and the $K$-character above, while its inert traces may differ.

# Split-invisible classes and the global firewall {#sec:counterpacket}

Fix a coefficient prime $\ell$, a finite extension $E_\ell/\mathbf Q_\ell$ containing the traces in scope, and a finite set $S$ containing $\ell$, the ramified primes, and the bad primes of every compatible system under discussion. For $F=\mathbf Q$ or $K$, let $S_F$ be the primes of $F$ above $S$, and let $$K_{0,\ell}^{\mathrm{ss}}(F;S_F)$$ be the Grothendieck group generated by the finite-dimensional continuous semisimple $E_\ell$-representations of $G_F$ arising from these fixed-$\ell$ compatible-system realizations and their semisimple subquotients, all unramified outside the primes above $S$. This is not the unrestricted category of all representations of $G_F$. Restriction is the map $$\operatorname{Res}:K_{0,\ell}^{\mathrm{ss}}(\mathbf Q;S)
\longrightarrow K_{0,\ell}^{\mathrm{ss}}(K;S_K).$$

[\[prop:counterpacket\]]{#prop:counterpacket label="prop:counterpacket"} Let $D$ be a virtual rational class in the preceding fixed-$\ell$, finite-ramification category. If its trace vanishes at all but a relative-Dirichlet-density-zero subset of the good rational primes split in $K$, then $$\operatorname{Res}(D)=0.$$ If $D$ is represented by an actual system, then $D=0$.

Prime ideals of $K$ of residue degree one form a Dirichlet-density-one set. Outside the finite ramified set they lie over split rational primes, and the exceptional rational split primes in the hypothesis lift to a density-zero subset of that set. Hence the trace of $\operatorname{Res}(D)$ vanishes on a dense set of Frobenius conjugacy classes. Chebotarev and Brauer--Nesbitt imply $\operatorname{Res}(D)=0$. If $D$ is actual, restriction preserves its nonnegative rank; a zero restricted class therefore has rank zero and is the zero representation.

Restriction is not injective on virtual classes. The explicit class $$\mathbf 1-\chi_{K/\mathbf Q}
\label{eq:explicit-kernel-class}$$ is nonzero over $\mathbf Q$ because $K/\mathbf Q$ is a nontrivial quadratic extension, but it restricts to zero over $K$. More generally, $$U-U\otimes\chi_{K/\mathbf Q}$$ is a kernel class, and it is nonzero when $U\not\simeq U\otimes\chi_{K/\mathbf Q}$. Every such kernel class has rank zero. It can change a rational extension and its inert traces, but it cannot change a $K$-rail rank or a common $G_3$-isotypic multiplicity. Thus virtual split-invisible counterpackets do not evade Theorem [\[thm:denominator\]](#thm:denominator){reference-type="ref" reference="thm:denominator"} or Corollary [\[cor:no-central-sector\]](#cor:no-central-sector){reference-type="ref" reference="cor:no-central-sector"}.

## Why split-local identities do not globalize

At a good inert rational prime $p$, let $v$ be the prime of $K$ above $p$, and write $$P_p(U)=\prod_i(1-\alpha_iU).$$ Because $F_v=F_p^2$, one has the exact identity $$P_{K,v}(U^2)
=\prod_i(1-\alpha_i^2U^2)
=P_p(U)P_p(-U).
\label{eq:inert-polynomial}$$ The right-hand side is generally not a square. The equality of the two degree-one factors at a split rational prime therefore supplies no corresponding inert square root.

The conclusions of this paper are accordingly confined to good split primes. They do not construct a global or inert fractional Euler root, prove smoothness or packet-admissibility for $n\ge5$, supply bad-place data, or establish automorphy, meromorphic continuation, a functional equation, or RH.

# Exact replay and release boundary {#sec:replay}

The proofs in Sections [2](#sec:source-category){reference-type="ref" reference="sec:source-category"}--[7](#sec:counterpacket){reference-type="ref" reference="sec:counterpacket"} are the theorem evidence. Exact computation is used as a reproducibility layer for finite arithmetic, matrix traces, and hostile mutations; it does not replace the all-$n$ recurrence proof. No temporary or unpackaged scout file is a release source or theorem input.

The project-local release chain has four roles:

1.  the producer emits one canonical certificate for the group, descent, rank, and character ledgers;

2.  an independent checker reconstructs the semantic claims rather than trusting producer booleans;

3.  targeted mutations must fail when the support parity, residue determinant ratio, weight separation, coefficient orbit, or scope firewall is corrupted;

4.  the persistent scoped manifest binds exactly seven release code files and four release result files while excluding both manifest files; the 44-entry full-project inventory includes it, while the implementation commit remains a separate provenance stage.

The required exact checks include the following.

  Gate                  Required result
  --------------------- --------------------------------------------------------------------------------------------------------------------------------------------
  Universal group       Symbolic closure parity, $6n$ exhaustive count, generator relations, and independent brute force in the smallest rows
  Rational form         $\delta(r)=r^{-1}$, $\delta(s)=rs$, exactly two fixed geometric elements, and distinct Reynolds/transfer denominators
  Denominator theorem   Separate-rail survivors exactly $2,4$; the total-rank mutation must be rejected for accepting $n=3$
  Third-row character   27 monomials, seven independent relations, quotient dimension 20, residue-corrected group law, both trace vectors, and orbit block $(3,4)$
  Scope                 Nonzero class $\mathbf 1-\chi_{K/\mathbf Q}$ with zero restriction and rank; all global-root and analytic-promotion flags remain false

The tested local promotion protocol is rollback-atomic and exception-safe under injected failures after its write stages. This is not a power-loss atomicity or storage-durability claim.

## Release-candidate verification record

The upstream dependency gate reads HCS-C53 from committed git object `9d509d3b...` and verifies both the committed Route digest and its exact artifact tuple. The unabbreviated commit, digest, and dependency tuple are recorded in the project source audit; mutable working-tree bytes are not accepted as provenance.

The immutable project-local release-candidate replay passes 36 of 36 semantic checks and 93 of 93 unit tests. The latter include all targeted hostile mutations and an exhaustive rebound sweep of 198 semantic leaves. The certificate has 1,078 scalar leaves: 198 semantic, 876 exact-derived, and four allowlisted history leaves. The exact artifact hashes are:

  ----------------------- ------------------------------------------------------------------
  payload                 f068d5e11ea8e6245e04bd3a30e77140267f835c4e07412ce2009c7fb04ceae1
  certificate             780cc9f249e836d3fa5b51a00fd2cdb9af0eac595d929cd1be4d728df1921846
  independent check       160b3a9d11354b41404642a3dd22d6e43f2ce576126acb21eb0133e552fc0c0a
  schema                  4cee6c2252d5743ca3c5fee40ec98fbc945223312d2196fb63a43730281deedf
  code/results manifest   62f67e6d4929496974020febab3bc0e2cff45ed153b0cef51937031863d866ba
  ----------------------- ------------------------------------------------------------------

These are release-candidate identifiers for the persistent scoped code/results lane. The displayed manifest hash is the digest of `results/CODE_RESULTS_HASHES.sha256`, whose 11 entries exclude both manifest files; the full-project inventory includes that file. The implementation commit is intentionally absent and belongs to a later provenance stage. The clean LaTeX build and PDF freeze are performed against the displayed immutable tuple; later provenance backfill must not alter the frozen manuscript.

## Claim boundary

The unconditional universal result is the projective monomial equation/group classification. The packet theorem applies only to packet-admissible smooth rows, with inherited certified packet data in rows $2,3,4$. The $n=3$ common-character theorem is first over $K$. Nothing in the replay layer upgrades these quantifiers, identifies the projective monomial stabilizer with the full PGL automorphism group, or supplies an inert/global root, automorphy, continuation, a functional equation, or RH.

# Declarations {#sec:declarations}

#### Data and code availability.

No external dataset or fitted parameter is used. The exact producer, independent checker, mutation suite, and result certificates are maintained inside the HCS-C54 project directory. Section [8](#sec:replay){reference-type="ref" reference="sec:replay"} records the immutable release-candidate tuple for the persistent scoped code/results lane. The 44-entry full-project inventory includes that scoped manifest. The implementation commit remains a later provenance stage and must not change the frozen paper.

#### Primary-source audit.

Bibliographic metadata and the proposition, theorem, section, and equation locators used in the manuscript are recorded in the project-local primary-source audit. The bounded novelty search is a documented screen, not a systematic-review or exhaustive priority certificate.

#### Author contributions.

The work was carried out collaboratively: conceptualization, formal analysis, verification design, writing, and curation.

#### Competing interests.

The authors declare no competing interests.

#### Funding.

No external funding is declared for this project.

#### Ethics.

The work uses no human participants, animal subjects, or personal data.

# Proof ledgers {#app:proof-ledgers}

## Closure and the support quotient

Iterating [\[eq:edge-recurrence\]](#eq:edge-recurrence){reference-type="eqref" reference="eq:edge-recurrence"} from $e_0=0$ gives $$e_N-e_0=
\sum_{j=0}^{N-1}(-1)^{N-1-j}
\bigl(q+c_{\sigma(E_j)}-c_j\bigr).$$ The coefficient of $q$ is $\sum_{j=0}^{N-1}(-1)^{N-1-j}=0$ because $N=2n$ is even. If $j_*$ is the unique inverse-image index of the closing edge, the two indicator sums reduce the closure condition to $$(-1)^{N-1-j_*}-1=0.$$ Thus $j_*$ is odd. For the support $i\mapsto i+k$, one has $j_*=N-1-k$, so $k$ is even. For $i\mapsto k-i$, one has $j_*=k$, so $k$ is odd. This gives $2n$ supports and three forced-scale lifts per support.

The phase of $r^n$ is zero on even coordinates and one on odd coordinates, up to a common projective scalar. Hence $$r^n=\operatorname{diag}(1,\rho,1,\rho,\ldots,1,\rho),$$ which has order three. Together with the order-$n$ support of $r$, this proves $|r|=3n$. The support and phase identities $s^2=1$ and $srs=r^{-1}$ then give a dihedral subgroup of size $6n$, equal to the exhaustive list.

## Fixed-point congruences

From [\[eq:galois-action\]](#eq:galois-action){reference-type="eqref" reference="eq:galois-action"}, $$\delta(r^k)=r^{-k},\qquad
\delta(r^ks)=r^{1-k}s.$$ The number of rotation solutions to $2k=0$ modulo $3n$ is $\gcd(2,3n)$; the reflection congruence $2k=1$ has a solution exactly when $3n$ is odd. These alternatives yield the two elements listed in Theorem [\[thm:rational-form\]](#thm:rational-form){reference-type="ref" reference="thm:rational-form"} and no others.

## Rank reduction

The two necessary congruences $$n\mid4e_n,\qquad n\mid4o_n$$ and the identity $o_n=2(e_n-3)$ imply $$n\mid8e_n,\qquad n\mid8(e_n-3),\qquad n\mid24.$$ There are therefore only seven candidate divisors $n\ge2$. The residue table in the proof of Theorem [\[thm:denominator\]](#thm:denominator){reference-type="ref" reference="thm:denominator"} is exhaustive, not a finite approximation to an unbounded scan.

## Character reconstruction

For any class function $\chi$ on $G_3$, the one-dimensional multiplicities are $$\begin{aligned}
m_{\mathbf 1}
&=\frac1{18}\left(\sum_{k=0}^{8}\chi(r^k)
 +\sum_{k=0}^{8}\chi(r^ks)\right),\\
m_{\varepsilon}
&=\frac1{18}\left(\sum_{k=0}^{8}\chi(r^k)
 -\sum_{k=0}^{8}\chi(r^ks)\right).\end{aligned}$$ The two-dimensional multiplicities are $$m_{U_j}=\frac1{18}\sum_{k=0}^{8}
\chi(r^k)\bigl(\zeta_9^{-jk}+\zeta_9^{jk}\bigr),
\qquad 1\le j\le4.$$ Applying these formulas to the two trace rows gives

     character       $m_{\mathbf 1}$   $m_{\varepsilon}$   $m_{U_1}$   $m_{U_2}$   $m_{U_3}$   $m_{U_4}$
  ---------------- ----------------- ------------------- ----------- ----------- ----------- -----------
   $H^{2,1}(X_3)$                $0$                 $2$         $2$         $2$         $3$         $2$
   $\mathsf E_3$                 $1$                 $2$         $3$         $3$         $1$         $3$

Dimension checks give $20$ and $23$, respectively. The Galois action on ninth roots permutes $U_1,U_2,U_4$ and leaves the multiplicity pair $(3,4)$ after the odd rail is doubled. This is why splitting that orbit into three unrelated rational sectors is not allowed.

# A Fermat-only diagonal refinement {#app:fermat-refinement}

This appendix records a stronger statement that uses more symmetry on the Fermat rail than is common to the cubic--quadric pair. It is not used in the proof of Theorem [\[thm:denominator\]](#thm:denominator){reference-type="ref" reference="thm:denominator"} or Corollary [\[cor:no-central-sector\]](#cor:no-central-sector){reference-type="ref" reference="cor:no-central-sector"}.

For the Fermat cubic in six variables, the projective diagonal group is $$D=(\mu_3^6)/\mu_3.$$ The primitive character labels have $$(a_0,\ldots,a_5)\in\{1,2\}^6,\qquad
\sum_i a_i\equiv0\pmod3.$$ Brünjes identifies the primitive character labels [@Brunjes2003 Lemma/Definition 4.3]. The corresponding primitive pieces are one-dimensional by [@Brunjes2003 Theorem 4.6]. In this six-variable cubic, the admissible tuples have respectively zero, three, or six entries equal to $2$, accounting for $$1+\binom63+1=22$$ primitive lines, in agreement with the squarefree degrees $0,3,6$ used in Section [6](#sec:n3-character){reference-type="ref" reference="sec:n3-character"}.

[\[prop:fermat-diagonal\]]{#prop:fermat-diagonal label="prop:fermat-diagonal"} After extending coefficients to a splitting field for $D$, no nonzero central sum of primitive Fermat diagonal-character sectors admits ordinary multiplicity $4/3$.

Every selected primitive character occurs with multiplicity one. An actual representation scaled by $4/3$ would require its multiplicity to be divisible by three, which fails on every selected line. Packaging Galois orbits over a smaller coefficient field does not help: after scalar extension, each constituent again has multiplicity one.

The classical interpretation of the associated Fermat eigenvalues by Jacobi sums is described in [@Weil1952; @Brunjes2003], but no Jacobi-sum analytic consequence is used here. In particular, the proposition proves neither automorphy nor a functional equation. It is deliberately confined to the Fermat diagonal group: the complete-intersection rail is stable only under the common group $G_3$, so the main two-rail obstruction must use Theorem [\[thm:n3-character\]](#thm:n3-character){reference-type="ref" reference="thm:n3-character"}.
