---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--15-bar-koszul-primitive-no-lift"
canonical_tex: "symbolic_dynamics/papers/15-bar-koszul-primitive-no-lift/main.tex"
canonical_pdf: "symbolic_dynamics/papers/15-bar-koszul-primitive-no-lift/main.pdf"
source_sha256: "36bbd2a40f7997cd2699d32f30a6fd0f9dd907c1262e74ccb43eb5d852e60623"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Primitive-Cycle No-Lift for the Tensor Bar Code: Koszul, Power, and Equivariant Obstructions

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/15-bar-koszul-primitive-no-lift>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/15-bar-koszul-primitive-no-lift/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/15-bar-koszul-primitive-no-lift/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/15-bar-koszul-primitive-no-lift/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/15-bar-koszul-primitive-no-lift/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We test whether the tensor bar-code determinant can be reduced, before trace-level aggregation, to primitive cycles indexed by tensor atoms. The strongest natural reduction is a one-vertex subset shift: every nonempty squarefree atom set $S$ is an edge of scalar weight $(-1)^{|S|+1}x_S$. Its determinant is exactly $D_A(x,1)=\prod_{a\in A}(1-x_a)$; on the countable full-shift tensor inventory, $x_{F_p}=p^{-s}$ gives $D_\infty(s,1)=1/\zeta(s)$ for $\operatorname{Re}s>1$. We prove that this valid scalar identity has no natural primitive-cycle lift under content, cyclic, temporal-power, and atom-permutation compatibility. At content $p^2q^2$, one positive and two negative primitive necklaces contribute $-1$; zero appears only after adding the second repetitions of two lower-content $pq$ primitives. At content $pqr$, equal scalar dimensions hide the nonzero virtual $S_3$ character $\mathbf1\oplus\mathbf{sgn}-\mathbf{Std}$. Genuine homological reduction does not repair either failure: $\operatorname{Tor}$ of the polynomial atom algebra is the full exterior algebra, cyclic primitivity is not preserved by bar faces, scalar powers $(-w)^r$ differ from odd supertraces $-w^r$, and an acyclic graded sector has determinant one. Exact enumeration and randomized formal inventories certify both the obstruction and its universality. Thus SD-C17 earns an analytic symbolic determinant but fails the primitive-orbit, global-analytic, and liftability gates; Route A is rejected and Route B remains locked.
author:
- Anonymous Authors
bibliography:
- references.bib
date: 'August 14, 2026'
title: |
  Primitive-Cycle No-Lift for the Tensor Bar Code:\
  Koszul, Power, and Equivariant Obstructions
```

## Markdown 正文

# Introduction {#sec:introduction}

An Euler product can be correct after aggregation while its proposed orbit interpretation is wrong. That distinction is decisive in arithmetic symbolic dynamics. A strong Route-A candidate needs primitive symbolic cycles, their temporal repetitions, and the determinant to carry one and the same ledger. Producing $1/\zeta(s)$ from an alternating inventory is not enough if mixed primitive cycles cancel only after information has been moved between different repetition orders.

The preceding tensor bar-code construction localized this issue. Its source was intrinsic: finite full shifts satisfy $$\mathsf F_m\otimes\mathsf F_n=\mathsf F_{mn},\qquad h(\mathsf F_n)=\log n,
  \tag{1.1}$$ so tensor atoms and their powers arise without a supplied prime mask. A one-vertex shift on ordered factorization words, with reduced-bar scalar signs, had determinant $1/\zeta$ in a proved half-plane. Its primitive cycles, however, were cyclic necklaces of factorization words rather than the atom loops demanded by a prime/prime-power interpretation.

This paper takes the boldest same-family next step. The bar resolution of a polynomial algebra is compressible to a Koszul resolution [@priddy1970; @skoldberg2006; @jollenbeckwelker2009]. Decategorizing its squarefree exterior basis suggests keeping one signed return edge for every nonempty subset of tensor atoms. For a finite atom set $A$, define $$\mathcal F_A(x)
  =\sum_{\varnothing\ne S\subseteq A}(-1)^{|S|+1}x_S.
  \tag{1.2}$$ Then $1-\mathcal F_A=\prod_{a\in A}(1-x_a)$. This looks like the desired reduction: mixed subsets have been compressed to a finite squarefree alphabet, while the scalar determinant already factors into atom terms.

The appearance is false at the primitive level. The cancellation in (1.2) is a statement in a commutative coefficient ring. Temporal recurrence uses cyclic words and actual powers of scalar weights, and equivariant naturality remembers atom permutations. Those two refinements expose obstructions invisible under scalar specialization.

#### Contributions.

We make four source-locked claims.

1.  We define the tensor-atom Koszul subset shift SD-C17, prove its formal determinant $D_A(x,1)=\prod_a(1-x_a)$, and prove the countable analytic specialization $D_\infty(s,1)=1/\zeta(s)$ for $\operatorname{Re}s>1$.

2.  We give the first decisive primitive/power certificate for this candidate. At $p^2q^2$, the primitive signed sum is $-1$ and is canceled only by the $r=2$ repetitions of the two $pq$ primitives. Hence no primitive-local sign involution can commute with temporal powers.

3.  We strengthen cardinality to naturality. At $pqr$, the positive and negative sides both have dimension three, but their virtual $S_3$ representation is $\mathbf 1\oplus\mathbf{sgn}-\mathbf{Std}$. No atom-permutation- equivariant pairing exists.

4.  We prove a homological no-lift theorem. Koszul homology retains mixed exterior classes; bar faces do not preserve cyclic primitivity; scalar signs do not obey supertrace power laws; and genuine acyclic sectors are graded-determinant invisible.

The ingredients are classical algebra and combinatorics. Our narrow contribution is their exact assembly under the primitive/repetition and naturality obligations of one frozen symbolic candidate. We neither claim a new Koszul resolution nor infer anything about Riemann zeros.

The conclusion is deliberately asymmetric. SD-C17 has an analytic determinant and an intrinsic arithmetic source, so the positive calculation is not dismissed. It fails the primitive-orbit gate, has no new global analytic structure, and has no natural operator lift. Its exact tuple is $$\begin{split}
(&\texttt{A0\_ANALYTIC\_ARITHMETIC\_ORIGIN},
  \texttt{A1\_FAIL},\\
 &\texttt{A2\_ANALYTIC\_DETERMINANT},
  \texttt{A3\_FAIL},\texttt{A4\_FAIL}).
\end{split}
\tag{1.3}$$ Accordingly, `ROUTE_A_REJECTED`; Route B is not invoked.

The remainder fixes the classical boundary, defines the candidate, proves the two finite obstructions, and then closes the chain-level escape routes. The exact audit is reported only after the theorems, so computation verifies the ledger rather than choosing it.

# Algebraic boundary and novelty discipline {#sec:boundary}

Four mature theories meet in SD-C17. Keeping their data types separate is more important than expanding the bibliography.

## Weighted symbolic determinants and necklaces

For a one-vertex shift with finitely or absolutely summably many weighted edges, the vertex adjacency is the sum of the edge weights. Its determinant is therefore $1-F$, and $$-\log(1-F)=\sum_{n\ge1}\frac{F^n}{n}
  \tag{2.1}$$ regroups into primitive cyclic words and their repetitions. This is the weighted one-vertex specialization of the symbolic determinant framework of @bowenlanford1970. Necklaces, primitive roots, and their Witt-type algebras are classical [@metropolisrota1983]. We use only the elementary primitive-root decomposition and prove the required finite counts directly.

Equation (2.1) already warns against confusing three objects:

-   a signed edge in the alphabet;

-   a primitive cyclic word made of those edges;

-   the $r$th temporal repetition of that primitive word.

The determinant aggregates all three. A primitive-orbit claim must recover them before aggregation.

## Bar and Koszul reductions

For an augmented algebra, the bar resolution is canonical but large. Koszul algebras admit smaller resolutions with exterior-shaped generators [@priddy1970]; modern Koszul duality places this pattern in a broader operadic setting [@ginzburgkapranov1994]. Algebraic discrete Morse theory constructs chain-homotopy reductions of bar and related complexes [@skoldberg2006; @jollenbeckwelker2009]. If a group acts, the matching must satisfy additional equivariance conditions; arbitrary order-based matchings need not descend equivariantly [@freij2009].

These results authorize a genuine chain reduction only when chain groups, differentials, matchings, and induced symmetries are specified. They do not authorize replacing a scalar coefficient $(-1)^d$ by a supertrace parity after a determinant has been computed. SD-C17 is intentionally the scalar decategorification, and tests whether that scalar object can be lifted back without changing its temporal ledger.

## Hochschild, Harrison, and indecomposables

For a smooth polynomial algebra in characteristic zero, the Hochschild--Kostant--Rosenberg theorem identifies Hochschild homology with differential forms [@hkr1962]. Mixed forms survive in exterior degrees at least two. Harrison theory isolates the commutative indecomposable component [@barr1968]; André--Quillen theory expresses the same smooth direction through the cotangent complex [@quillen1970]. Hodge-type decompositions make explicit that the Harrison component is one summand or quotient of the fuller Hochschild information, not its entirety [@gerstenhaberschack1987; @loday1998].

This distinction blocks a tempting shortcut. An atom-only Harrison or cotangent sector may be mathematically natural, but projecting to it deletes mixed cyclic recurrence. It cannot be presented as a trace-preserving equivalence of the original scalar subset shift.

## Exact novelty boundary

The following are not new here: inclusion--exclusion, the Euler product in its convergence half-plane, the Koszul resolution, the exterior computation of Tor, HKR, Harrison/AQ decomposition, equivariant Morse theory, and necklace enumeration. We claim only the following bounded contribution:

> For the source-locked tensor-atom subset shift, the $p^2q^2$ power ledger, the $pqr$ $S_3$ character, and the scalar/supertrace firewall jointly rule out a primitive-local, power-compatible, atom-permutation-natural Koszul lift.

No priority claim is made for the individual combinatorial identities. The value is the obstruction package and the decision it forces for SD-C17.

# The tensor-atom Koszul subset shift {#sec:subset-shift}

## Source object and finite formal model

Let $\mathcal M=\{\mathsf F_n:n\ge1\}$ with tensor product and entropy as in (1.1). Its nonunit irreducible objects are the tensor atoms $\mathsf F_p$. Fix a finite set $A\subset\operatorname{Atom}(\mathcal M)$ and attach an independent formal variable $x_a$ to each $a\in A$. For nonempty $S\subseteq A$, put $$x_S=\prod_{a\in S}x_a,
  \qquad \varepsilon(S)=(-1)^{|S|+1}.
  \tag{3.1}$$

The phase space is the one-vertex full edge shift with alphabet $$\mathcal E_A=\{S\subseteq A:S\ne\varnothing\}.
  \tag{3.2}$$ An edge $S$ has scalar formal weight $w(S)=\varepsilon(S)x_S$. A closed orbit is a cyclic word of subset edges; reflection is not quotiented.

Under the analytic tensor specialization, an atom $a=\mathsf F_p$ has $x_a=e^{-sh(a)}=p^{-s}$ and an edge has roof $$T(S)=\sum_{a\in S}h(a),
  \qquad w_s(S)=\varepsilon(S)e^{-sT(S)}.
  \tag{3.3}$$ No prime coefficient, Möbius value, von Mangoldt weight, or target zero is part of (3.2)--(3.3).

The vertex function space is $\ell^2(\{*\})\cong\mathbb C$. Define the weighted adjacency and determinant before any simplification: $$L_{A,x}c=\mathcal F_A(x)c,
  \qquad
  \mathcal F_A(x)=\sum_{\varnothing\ne S\subseteq A}\varepsilon(S)x_S,
  \tag{3.4}$$ $$D_A(x,z)=\det_{\mathbb C}(I-zL_{A,x})=1-z\mathcal F_A(x).
  \tag{3.5}$$

[\[thm:formal-determinant\]]{#thm:formal-determinant label="thm:formal-determinant"} For every finite atom set $A$, $$\mathcal F_A(x)=1-\prod_{a\in A}(1-x_a),
  \qquad
  D_A(x,1)=\prod_{a\in A}(1-x_a).
  \tag{3.6}$$

Expand the product in (3.6). Its term indexed by $S$ is $(-1)^{|S|}x_S$; separating the empty subset gives the first equality. The second follows from the frozen determinant (3.5).

The theorem is an exact determinant of the symbolic adjacency, not merely an identity imposed on its value. It is also completely universal: no property of tensor atoms was used. The same fact will count positively at A2 and negatively at the arithmetic-selectivity control.

## Countable analytic specialization

Let the alphabet contain every finite nonempty subset of the countable tensor atom set. For $\sigma=\operatorname{Re}s>1$, $$\begin{split}
  \sum_{S\ne\varnothing}|w_s(S)|
  &=\sum_{S\ne\varnothing}\prod_{\mathsf F_p\in S}p^{-\sigma}\\
  &=\prod_p(1+p^{-\sigma})-1
   =\frac{\zeta(\sigma)}{\zeta(2\sigma)}-1<\infty.
\end{split}
\tag{3.7}$$ Thus the countable edge sum defines a scalar trace-class operator on $\mathbb C$.

[\[cor:countable-determinant\]]{#cor:countable-determinant label="cor:countable-determinant"} For $\operatorname{Re}s>1$, $$D_\infty(s,1)=\prod_p(1-p^{-s})=\frac1{\zeta(s)}.
  \tag{3.8}$$

Absolute convergence in (3.7) permits inclusion--exclusion over finite atom sets followed by the countable limit. The final equality is the ordinary Euler product in its absolute-convergence half-plane.

Equation (3.8) does not extend the Euler product or add a Gamma factor, functional equation, or divisor theorem. The arithmetic source earns A0 credit because tensor atoms and their entropy are intrinsic. The determinant earns A2 credit in its stated domain. Neither fact establishes A1.

## Primitive semantics

For a cyclic word $\gamma=[S_1\cdots S_\ell]$, define $$w(\gamma)=\prod_{j=1}^{\ell}\varepsilon(S_j)x_{S_j}.
  \tag{3.9}$$ A necklace is primitive when its least cyclic period is $\ell$. Whenever $|z\mathcal F_A|<1$, unique primitive-root decomposition gives $$-\log D_A(x,z)
  =\sum_{\gamma\ \mathrm{primitive}}
    \sum_{r\ge1}\frac{z^{r|\gamma|}w(\gamma)^r}{r}.
  \tag{3.10}$$ The scalar sign is powered in (3.10). An edge with negative weight changes sign at odd repetitions and becomes positive at even repetitions. This power law is part of the candidate and cannot be replaced after the fact.

Primitive cycles already include one-edge mixed subsets $[\{p,q\}]$ and multi-edge mixed necklaces. The atom factors in (3.6) arise only after the full trace-log has been aggregated. The next two sections show exactly where an orbitwise interpretation breaks.

# The primitive-power obstruction {#sec:power}

The first mixed content $pq$ gives a seductive but incomplete picture. The next repeated content proves that no primitive-local pairing can explain the determinant while respecting temporal powers.

Fix two atoms and abbreviate $$a=\{p\},\qquad b=\{q\},\qquad c=\{p,q\}.
  \tag{4.1}$$ Their scalar signs are $+,+,-$, respectively. At content $pq$, there are exactly two primitive necklaces: $$[ab]\quad\text{of weight }+x_px_q,
  \qquad
  [c]\quad\text{of weight }-x_px_q.
  \tag{4.2}$$ They pair perfectly at first order.

[\[thm:p2q2\]]{#thm:p2q2 label="thm:p2q2"} At multidegree $x_p^2x_q^2$, the primitive necklaces of SD-C17 are exactly $$\begin{array}{ccl}
  \lbrack aabb\rbrack && +,\\
  \lbrack abc\rbrack  && -,\\
  \lbrack acb\rbrack  && -.
\end{array}
\tag{4.3}$$ Their primitive signed sum is $-1$. The complete coefficient of $x_p^2x_q^2$ in $-\log D_A(x,1)$ is nevertheless zero because the $r=2$ repetitions of the two primitives in (4.2) contribute $1/2+1/2=1$.

A word of content $p^2q^2$ contains zero, one, or two copies of $c$.

With no $c$, it has two $a$'s and two $b$'s. Up to cyclic rotation the two possibilities are $[aabb]$, which is primitive, and $[abab]=[ab]^2$, which is not. With one $c$, the remaining content is one $a$ and one $b$. The two cyclic orders $[abc]$ and $[acb]$ are primitive. With two $c$'s, $[cc]=[c]^2$ is imprimitive. This proves completeness of (4.3). Multiplying edge signs gives one positive and two negative weights, so the primitive coefficient is $-1$.

The imprimitive words enter (3.10) as repetitions of the two $pq$ primitives: $$\frac{(+x_px_q)^2}{2}
  +\frac{(-x_px_q)^2}{2}
  =x_p^2x_q^2.
  \tag{4.4}$$ Adding (4.4) to the primitive coefficient gives zero, in agreement with $-\log D_A=\sum_a-\log(1-x_a)$.

[\[cor:no-primitive-involution\]]{#cor:no-primitive-involution label="cor:no-primitive-involution"} There is no content-preserving sign-reversing bijection on primitive necklaces that both explains every mixed coefficient and commutes with temporal powers.

At content $p^2q^2$, the primitive positive and negative cardinalities are one and two. No bijection exists even before naturality is imposed. Moreover, the missing positive unit comes from powers of lower-content primitives, so a degreewise primitive pairing cannot reproduce the complete coefficient.

## Why a fixed parity pairing changes the trace

Suppose one pairs the two $pq$ objects in (4.2) and interprets the minus sign as a fixed odd parity. Their second repetitions would contribute $$\frac{(+1)^2}{2}-\frac{(+1)^2}{2}=0,
  \tag{4.5}$$ whereas the frozen scalar weights contribute $1$ in (4.4). The discrepancy is not a convention: it changes the trace of $L^2$ and therefore the determinant.

The obstruction is stronger than a failed visual pairing. It says that the scalar Euler factor is assembled by a Witt/necklace relation crossing primitive contents and repetition orders. A primitive $p\leftrightarrow
\gamma_p$, $p^r\leftrightarrow\gamma_p^r$ ledger cannot be read from the signed subset cycles before this aggregation.

## General squarefree cancellation

At squarefree content $x_1\cdots x_k$, every word is a cyclically ordered set partition. A word with $m$ blocks has sign $(-1)^{k+m}$ and there are $(m-1)!S(k,m)$ such words. Hence its total scalar coefficient is $$c_k=\sum_{m=1}^k(-1)^{k+m}(m-1)!S(k,m).
  \tag{4.6}$$

[\[prop:stirling\]]{#prop:stirling label="prop:stirling"} For $k\ge2$, $c_k=0$; for $k=1$, $c_1=1$.

By , $$-\log D_A(x,1)=\sum_{a\in A}-\log(1-x_a).
  \tag{4.7}$$ The right side contains no mixed monomial. Equation (4.6) enumerates the coefficient of $x_1\cdots x_k$ on the left, proving the claim.

The zero in (4.6) is a scalar dimension statement. The next section retains the atom-permutation action and finds a nonzero character behind the first nontrivial zero.

# The equivariant obstruction {#sec:equivariant}

Naturality under a relabeling of tensor atoms is mandatory. A construction that depends on a chosen lexicographic order or preferred cyclic orientation measures presentation, not tensor structure. The squarefree content $pqr$ is the smallest place where dimension cancellation and equivariant cancellation separate.

Every cyclic set partition of three atoms is primitive. The positive and negative sets are $$C_+=\{[pqr],[p][q][r],[p][r][q]\},
  \tag{5.1}$$ $$C_-=\{[p][qr],[q][pr],[r][pq]\}.
  \tag{5.2}$$ The two sets have the same cardinality, matching the scalar zero in . Their $S_3$ actions are different.

[\[thm:s3\]]{#thm:s3 label="thm:s3"} In conjugacy-class order identity, transposition, three-cycle, the fixed-point characters of (5.1)--(5.2) are $$\chi_+=(3,1,3),\qquad \chi_-=(3,1,0).
  \tag{5.3}$$ Thus $$\chi_+-\chi_-=(0,0,3),
  \tag{5.4}$$ and, in the representation ring of $S_3$, $$[\mathbb C[C_+]]-[\mathbb C[C_-]]
  =\mathbf 1\oplus\mathbf{sgn}-\mathbf{Std}.
  \tag{5.5}$$ In particular, no $S_3$-equivariant sign-reversing bijection exists.

The one-block necklace $[pqr]$ is fixed by all atom permutations. The two cyclic orientations of three singleton blocks form one orbit of size two. A transposition exchanges them, while a three-cycle acts by cyclic rotation and therefore fixes both necklace classes. This gives $(3,1,3)$.

The three singleton--pair partitions form one orbit of size three. The identity fixes all three, a transposition fixes the partition determined by its invariant singleton, and a three-cycle fixes none. This gives $(3,1,0)$. Subtraction proves (5.4). Comparing with the irreducible character table of $S_3$ gives (5.5). An equivariant bijection would induce equal fixed counts for every group element, contradicting the last entries of (5.3).

The orbit types make the obstruction transparent: $$C_+\cong S_3/S_3\ \sqcup\ S_3/C_3,
  \qquad
  C_-\cong S_3/C_2.
  \tag{5.6}$$ Scalar dimension sends both sides to three and kills (5.5). The character at a three-cycle retains the residual value three.

## Why order-based pairings are not repairs

A lexicographic rule can pair the three displayed positive and negative objects after choosing $p<q<r$. Such a rule necessarily selects a cyclic orientation and a distinguished atom. The exact permutation audit finds equivariance failures for four of the six atom permutations, with three failed pairs in each noncommuting case.

This is the finite manifestation of the equivariant Morse obligation emphasized by @freij2009: a matching chosen on representatives does not become natural merely because matched cardinalities agree. Here the character theorem is stronger than checking a particular lexicographic rule; it rules out every equivariant bijection.

## The surviving in-family clue

Equation (5.5) identifies exactly what scalar specialization erases. It suggests retaining a representation- or cycle-index-valued trace before applying the dimension homomorphism. That is a new symbolic candidate, not a repair of SD-C17. It must preserve Adams/power operations and remain coherent as the atom set grows. We record it as the next in-family research obligation, not as evidence that the present candidate passes A1.

# Homological and cyclic no-lift {#sec:homological}

The finite orbit obstructions leave an apparent escape: perhaps the scalar subset signs are shadows of a genuine bar-to-Koszul chain contraction, so one should cancel in homology rather than pair primitive cycles. This section shows why that move changes the object or becomes determinant invisible.

## Koszul reduction retains mixed exterior classes

Let $$R_A=\Bbbk[x_a:a\in A]
  \tag{6.1}$$ over a field $\Bbbk$, augmented by $x_a\mapsto0$, and let $V_A$ have basis $e_a$. The standard Koszul complex is $$K(R_A;x_a)=R_A\otimes_\Bbbk\Lambda V_A.
  \tag{6.2}$$

[\[thm:tor\]]{#thm:tor label="thm:tor"} For every $i$, $$\operatorname{Tor}^{R_A}_i(\Bbbk,\Bbbk)\cong\Lambda^i V_A.
  \tag{6.3}$$ In particular, $e_p\wedge e_q$ is nonzero for distinct atoms. A chain reduction quasi-isomorphic to the bar resolution cannot leave only the degree-one atom classes.

The Koszul complex (6.2) is a free resolution of the augmentation module. Tensoring it over $R_A$ with $\Bbbk$ sends each $x_a$ to zero, so its induced differential vanishes. Its homology is therefore the full exterior algebra. Tor is invariant under chain homotopy equivalence, which proves the final statement.

Algebraic Morse reduction can replace a large bar model by (6.2), but it cannot erase the mixed exterior homology without ceasing to be a quasi-isomorphism. The subset basis is small, not atom-only.

## Primitivity is not a bar subcomplex

A different proposal is to take primitive cyclic words before applying the bar or Hochschild differential. Adjacent multiplication makes this impossible.

[\[prop:primitive-boundary\]]{#prop:primitive-boundary label="prop:primitive-boundary"} In the monomial bar complex on two generators, multiplication faces can send a primitive cyclic word to an imprimitive one and an imprimitive cyclic word to a primitive one.

The cyclic word $[a|b|ab]$ is primitive. Merging its first two entries gives $[ab|ab]=[ab]^2$, which is imprimitive. Conversely, $[a|b|a|b]=[a|b]^2$ is imprimitive, while the same merge gives $[ab|a|b]$, which has least period three and is primitive.

Neither the primitive span nor the imprimitive span is a subcomplex. Consequently, \"take primitive homology\" is not a quotient operation inherited from the ordinary bar differential. A new differential designed to preserve primitivity would define a new symbolic object and would need a new determinant proof.

The cyclic boundary adds further faces but does not repair this local leak; standard cyclic and Hochschild constructions organize all cyclic words, not a primitive-only chain layer [@loday1998].

## HKR versus an atom-only commutative quotient

For the smooth polynomial algebra (6.1), HKR gives $$\operatorname{HH}_i(R_A)\cong\Omega^i_{R_A/\Bbbk}
  \cong R_A\otimes_\Bbbk\Lambda^iV_A.
  \tag{6.4}$$ Thus mixed forms persist on the Hochschild/cyclic side as well. In characteristic zero, Harrison and André--Quillen theory isolate the indecomposable commutative direction. For a polynomial algebra the cotangent complex is represented by $\Omega^1_{R_A/\Bbbk}$ in degree zero, so higher André--Quillen homology vanishes.

That vanishing is not a contraction of (6.4). It results from selecting a different Hodge component or quotient. Already in degree two, $\operatorname{HH}_2(R_A)$ contains $dx_p\wedge dx_q$, whereas the smooth higher indecomposable sector vanishes. The dimensions differ, so an atom-only Harrison/AQ projection cannot preserve the full Hochschild trace or the primitive recurrence of SD-C17.

## Scalar sign versus supertrace

The most dangerous conflation is purely notational. For a negative scalar edge of unsigned weight $w$, temporal repetition gives $$(-w)^r=(-1)^rw^r.
  \tag{6.5}$$ For an odd one-dimensional chain space with even operator $w$, the supertrace is $$\operatorname{Str}(w^r\mid C_{\mathrm{odd}})=-w^r
  \tag{6.6}$$ for every $r$. Equations (6.5)--(6.6) agree only for odd repetitions and differ by $2w^r$ for every even repetition. At $r=2$, this is exactly the power leak identified in .

[\[thm:acyclic\]]{#thm:acyclic label="thm:acyclic"} Let $(C,d)$ be a finite-dimensional $\mathbb Z/2$-graded acyclic complex and let $T$ be an even chain map. Then $$\operatorname{Str}(T^r\mid C)=0\quad(r\ge1),
  \tag{6.7}$$ and $$\operatorname{sdet}(I-zT)
  :=\exp\!\left(-\sum_{r\ge1}\frac{z^r}{r}\operatorname{Str}(T^r)\right)=1.
  \tag{6.8}$$

Choose a contracting homotopy $h$ with $dh+hd=I$. Since $T$ commutes with $d$, $$T^r=d(T^rh)+(T^rh)d.
  \tag{6.9}$$ This is a graded commutator of odd maps, whose supertrace is zero. Equation (6.8) follows term by term.

A true two-term contractible block therefore contributes nothing to the graded determinant. By contrast, the scalar two-edge alphabet $\{+w,-w\}$ has a mixed length-two primitive $[+w][-w]$ of weight $-w^2$. It cancels the $+w^2$ sum of the two length-one second repetitions. The two objects have the same aggregate trace zero but different primitive ledgers.

## Combined no-lift theorem

[\[def:lift\]]{#def:lift label="def:lift"} A primitive-natural Koszul lift of SD-C17 is a reduction that:

1.  cancels within primitive cyclic content classes or replaces matched classes by acyclic graded sectors;

2.  commutes with cyclic rotation, temporal powers, and finite atom permutations;

3.  preserves the frozen scalar trace at every repetition order;

4.  deletes all mixed subset classes while retaining nontrivial atom determinant factors.

[\[thm:no-lift\]]{#thm:no-lift label="thm:no-lift"} No reduction satisfying exists.

A primitive sign pairing fails at $p^2q^2$ by and independently fails atom-permutation naturality at $pqr$ by . Reinterpreting scalar signs as chain parities changes even-power traces by (6.5)--(6.6). Making the proposed cancellation genuinely acyclic gives determinant one by , so it cannot retain the nontrivial scalar factor. A quasi-isomorphic bar-to-Koszul reduction retains mixed classes by , and cyclic primitivity cannot be isolated as a subcomplex by . Every allowed branch violates at least one condition of .

The theorem is scoped. It does not forbid representation-valued or other chain-enhanced symbolic candidates with additional data frozen from the start. It forbids presenting such a new object as a trace-preserving reinterpretation of the scalar SD-C17 shift.

# Exact audit, controls, and route decision {#sec:audit}

The proofs determine the decision. Computation checks that the frozen enumerator, cyclic convention, temporal powers, and symmetry actions implement those proofs without a hidden presentation choice. Every calculation uses integers or exact rational arithmetic; no Riemann-zero data, root search, fitted phase, or fitted pairing is present.

## Primitive and power certificates

The primitive ledger contains seven exact rows across contents $pq$ and $p^2q^2$. It recovers the two primitives in (4.2), the three target-degree primitives in (4.3), and the two imprimitive words assigned to their correct lower-content primitive roots. The machine-readable certificate records $$N_+(p^2q^2)=1,\qquad N_-(p^2q^2)=2,
  \qquad c_{\rm prim}=-1,
  \tag{7.1}$$ and $$c_{r=2}(pq)=\frac12+\frac12=1,
  \qquad c_{\rm total}(p^2q^2)=0.
  \tag{7.2}$$ These are exact coefficient statements, not floating residuals.

## Equivariant and general squarefree checks

The $S_3$ certificate independently constructs the action on (5.1)--(5.2). It returns orbit sizes $1+2$ and $3$, fixed-character difference $(0,0,3)$, and irreducible multiplicities $(1,1,-1)$ for $(\mathbf 1,\mathbf{sgn},\mathbf{Std})$. A frozen lexicographic pairing commutes with only two of the six atom permutations; each of the other four permutations has three failed images.

The general audit checks (4.6) through $k=12$. All eleven mixed rows $2\le k\le12$ vanish exactly. An independent explicit enumeration of cyclic set partitions checks all 27 block-count rows through $k=7$. The total numbers of cyclic set partitions are shown in .

::: {#tab:cyclic-counts}
      $k$   2   3    4     5       6       7
  ------- --- --- ---- ----- ------- -------
    total   2   6   26   150   1,082   9,366

  : Exact cyclic set-partition counts. Each block-count component equals $(m-1)!S(k,m)$; the table reports totals over $m$.
:::

The scalar zeros at all tested orders confirm the determinant. The nonzero $S_3$ character confirms that a scalar zero is weaker than a natural orbitwise cancellation.

## Scalar/supertrace firewall

For repetition orders $1\le r\le8$, the audit compares (6.5) and (6.6). All four even repetitions disagree; at $r=2$ the coefficients are $+1$ and $-1$. After the trace-log factor, a non-power-compatible pairing leaks exactly one unit.

The true contractible control uses basis order even, odd and matrices $$d=\begin{pmatrix}0&1\\0&0\end{pmatrix},
  \qquad
  h=\begin{pmatrix}0&0\\1&0\end{pmatrix}.
  \tag{7.3}$$ Exact multiplication verifies $dh+hd=I$. With $T=wI$, $dT=Td$ and every supertrace through $r=8$ is zero. The block contains no mixed length-two primitive, whereas the scalar alphabet $\{+w,-w\}$ contains $[+w][-w]$. This control catches precisely the forbidden substitution of a chain contraction for a scalar signed alphabet.

## Universality and proves-too-much control

The arbitrary-variable theorem is itself the strongest adversarial control. The experiment instantiates it with $16$ frozen rational seeds for each $2\le k\le8$, giving 112 exact controls. Every row satisfies $$1-\sum_{S\ne\varnothing}(-1)^{|S|+1}x_S
  =\prod_{i=1}^k(1-x_i)
  \tag{7.4}$$ and remains invariant under presentation shuffles.

Passing all 112 controls is negative arithmetic evidence. Equation (7.4) holds for random, composite-labelled, and synthetic inventories just as it does for tensor atoms. The mechanism therefore receives $$\texttt{STOP\_ARITHMETIC\_SELECTIVITY / PROVES\_TOO\_MUCH}.
  \tag{7.5}$$ The arithmetic information in (3.8) lies in the tensor-atom inventory and its entropy specialization, not in the universal subset cancellation.

## Verification status

All 10 unit tests and all 11 code/result checksum checks pass. CSV files use LF line endings. The executable summary, exact certificates, and checksums are stored under `results/`; the source and tests are stored under `code/`. These checks certify the finite implementation, while carry the theorem claims.

## Route-A evaluation

L0.16L0.27X Gate & Verdict & Reason\
A0 &

::: {#tab:route}
  --------------------
  A0\_ANALYTIC
  ARITHMETIC\_ORIGIN
  --------------------

  : Strict Route-A decision for SD-C17.
:::

& Tensor-indecomposable full shifts give the atom inventory and entropy gives the roof without target data.\
A1 & `A1_FAIL` & Primitive objects are subset necklaces; power-compatible and equivariant atom reduction is impossible by .\
A2 &

::: {#tab:route}
  --------------
  A2\_ANALYTIC
  DETERMINANT
  --------------

  : Strict Route-A decision for SD-C17.
:::

& The declared one-dimensional Fredholm determinant is exact, and the countable edge sum is absolutely convergent for $\operatorname{Re}s>1$.\
A3 & `A3_FAIL` & There is no new continuation, completed functional equation, Gamma factor, global divisor theorem, counting law, or intrinsic Weil compression.\
A4 & `A4_FAIL` & No natural unitary, scattering, Hamiltonian, or self-adjoint lift is defined.\

Overall, SD-C17 is rejected on Route A. A2 cannot compensate for A1, and the proves-too-much control prevents promotion. Route B is false for the present candidate and remains locked.

# Conclusion and next obligation {#sec:conclusion}

The Koszul subset shift is the cleanest scalar reduction of the tensor bar inventory. Its positive theorem is exact: one source-locked symbolic adjacency has determinant $$D_A(x,1)=\prod_{a\in A}(1-x_a),$$ and its countable tensor specialization is $1/\zeta(s)$ in $\operatorname{Re}s>1$. The construction is not rejected because its determinant is formal or numerically unstable. It is rejected because its orbit semantics do not survive closer resolution.

At $p^2q^2$, scalar zero borrows contributions from lower-content temporal powers. At $pqr$, scalar dimension erases a nonzero $S_3$ character. A genuine bar-to-Koszul reduction retains mixed exterior homology; cyclic primitivity is not a chain layer; scalar signs obey a different power law from supertraces; and acyclic chain sectors contribute graded determinant one. These failures are independent and together prove the scoped primitive-cycle no-lift theorem.

The strongest lesson is not that homology is irrelevant. It is that homology, primitive recurrence, and scalar determinant are different data types. Moving between them requires a functor that respects temporal powers and atom symmetries. SD-C17 has no such functor.

The next step remains inside Symbolic Dynamics. Equation (5.5) suggests a character-resolved cycle-index determinant that retains nontrivial atom-permutation modes before scalar specialization. Its first obligations are finite and severe: coherence under $A\subset A'$, compatibility with Adams/power operations, trace-class control in the countable atom limit, and separation from arbitrary-inventory controls. The $p^2q^2$ and $pqr$ certificates should be rerun before any root computation.

Any proposal to realize the signs as geometric orientation, holonomy, or a self-adjoint graded carrier leaves the current family. Such ideas are recorded only as `ROUND2_CLUE`. They are not pursued here, and Route B stays locked.

The frozen decision is therefore $$\boxed{\texttt{ROUTE\_A\_REJECTED};\quad
       \texttt{ROUTE\_B\_LOCKED}.}$$ This is a substantive negative result: the scalar Euler product is largely symbolic, but the primitive-natural structure required for an arithmetic orbit model is not contained in this Koszul decategorification.

# Supplementary proofs and scope ledger {#app:proofs}

## Primitive-root regrouping with weights

Let $F=\sum_{e\in\mathcal E_A}w(e)$. The coefficient of $z^n$ in $\sum_{n\ge1}z^nF^n/n$ is a sum over based words of length $n$. Every based word has a unique primitive cyclic root $\gamma$ of length $\ell$ and a unique repetition number $r=n/\ell$. A primitive necklace of length $\ell$ has exactly $\ell$ based rotations. Therefore its total coefficient in the based-word sum is $$\frac{\ell}{r\ell}w(\gamma)^r=\frac{w(\gamma)^r}{r}.
  \tag{A.1}$$ This proves (3.10) as a formal identity. In the analytic specialization it also holds wherever the trace-log converges absolutely.

The formula makes the scalar-sign firewall unavoidable. If a primitive weight is negative, its $r$th term in (A.1) contains the $r$th power of that minus sign. A fixed chain parity is a different trace convention.

## Complete $p^2q^2$ necklace census

The content equation for a word with counts $(n_a,n_b,n_c)$ is $$n_a+n_c=2,\qquad n_b+n_c=2.
  \tag{A.2}$$ Thus $(n_a,n_b,n_c)$ is one of $(2,2,0)$, $(1,1,1)$, or $(0,0,2)$.

For $(2,2,0)$, the binary necklaces are represented by $aabb$ and $abab$. The latter has least period two. For $(1,1,1)$, cyclic orders modulo rotation are represented by $abc$ and $acb$, both of least period three. For $(0,0,2)$, the only word is $cc$, of least period one after taking the primitive root. This proves that (4.3) and the two $r=2$ terms exhaust the coefficient.

## Irreducible decomposition of the $S_3$ residual

The irreducible character table in class order $1,(12),(123)$ is $$\begin{array}{c|rrr}
 &1&(12)&(123)\\ \hline
\mathbf 1&1&1&1\\
\mathbf{sgn}&1&-1&1\\
\mathbf{Std}&2&0&-1
\end{array}
\tag{A.3}$$ and the virtual residual is $(0,0,3)$. Its inner products with the three irreducible characters, using class sizes $1,3,2$, are $$\langle\chi,\mathbf 1\rangle=1,
  \qquad
  \langle\chi,\mathbf{sgn}\rangle=1,
  \qquad
  \langle\chi,\mathbf{Std}\rangle=-1.
  \tag{A.4}$$ Hence $\chi=\mathbf 1\oplus\mathbf{sgn}-\mathbf{Std}$. Its dimension is zero, explaining why the scalar determinant cannot see it.

## Koszul and Harrison index conventions

The Koszul computation in concerns Tor of the augmentation module. HKR in (6.4) concerns Hochschild homology with coefficients in the algebra. Harrison homology and André--Quillen homology use another quotient and an index shift: in characteristic zero, higher Harrison groups encode the derived indecomposable commutative direction. For a polynomial algebra, the cotangent complex is the projective module of Kähler differentials in degree zero, so higher derived functors vanish.

These statements are compatible, not contradictory. They answer different questions. The mixed Tor and Hochschild exterior classes prove that an atom-only commutative quotient is not a quasi-isomorphic replacement for the full bar/Hochschild recurrence ledger.

## Trace-class extension of the acyclic lemma

was stated in finite dimension, which is all the exact control requires. The same graded-commutator proof extends to a countable complex only when the products in (6.9) are trace class and supertrace cyclicity is justified. No such infinite chain complex is source-locked for SD-C17, so we do not claim the extension here.

## Scope and nonclaims

The paper proves no statement about:

-   zeros of $\zeta$ outside the Euler-product half-plane;

-   the completed function $\xi$, its functional equation, or Gamma factor;

-   a Riemann--von Mangoldt counting law or Weil compression;

-   a self-adjoint, unitary, scattering, or Hamiltonian operator;

-   all possible representation-valued symbolic determinants;

-   all chain-enhanced grammars that add new source data before cyclic reduction.

The countable identity $D_\infty=1/\zeta$ is valid only in $\operatorname{Re}s>1$ under the absolute alphabet sum (3.7). Analytic continuation of the already-known Euler product is not credited to the symbolic shift.

The route tuple remains $$\begin{split}
(&\texttt{A0\_ANALYTIC\_ARITHMETIC\_ORIGIN},
  \texttt{A1\_FAIL},\\
 &\texttt{A2\_ANALYTIC\_DETERMINANT},
  \texttt{A3\_FAIL},\texttt{A4\_FAIL}),
\end{split}$$ with `ROUTE_A_REJECTED` and Route B locked.
