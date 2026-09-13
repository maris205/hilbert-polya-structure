---
p1_kind: "derived-fulltext-reading-copy"
route: "symplectic_map"
logical_paper_id: "symplectic_map--11-cat-equivariant-clock"
canonical_tex: "symplectic_map/papers/11-cat-equivariant-clock/paper/manuscript.tex"
canonical_pdf: "symplectic_map/papers/11-cat-equivariant-clock/paper/manuscript.pdf"
source_sha256: "2a49333745477cd553b97a1e14734484774621ffa7b09e405c25e23073be7958"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# An Equivariant-Zeta Audit of Cat-Map Centralizer Quotients

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symplectic_map/papers/11-cat-equivariant-clock>)
- [规范 TeX](<../../../../../symplectic_map/papers/11-cat-equivariant-clock/paper/manuscript.tex>)
- [关联 PDF](<../../../../../symplectic_map/papers/11-cat-equivariant-clock/paper/manuscript.pdf>)
- [支撑 Markdown](<../../../../../symplectic_map/papers/11-cat-equivariant-clock/PAPER_PLAN.md>)
- [BibTeX](<../../../../../symplectic_map/papers/11-cat-equivariant-clock/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We audit what standard finite equivariant, orbifold, and quotient-stack constructions retain after a cat-map centralizer quotient removes the source dynamics. For a finite abelian group $C$, translation by $a\in C$ on $X=\coprod_K n_K(C/K)$ has point period $d_K=[\langle a\rangle:\langle a\rangle\cap K]$ and $[C:\langle a\rangle K]$ cycles on each orbit type. The fixed-point rational Burnside zeta retains these source periods but depends on $a$ only through $\langle a\rangle$. The fixed-orbit integral Burnside zeta has support only at period one. Stronger labelled permutation and enhanced carriers retain the translation modulo the action kernel, while their orbifold or Morita quotient images have static dynamics. On the regular centralizer torsor of $A=\left(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\right)$ over $\mathbb{Z}/q\mathbb{Z}$, no one of four scalar-reduction types has source support and unit exponent uniformly over the locked nine-row family. The sole individual exception is point-cardinality reduction at $q=2$, where $m_2=1$ gives $(1-t^3)^{-1}$. A single exact audit at five predeclared primes and four predeclared composites reproduces the theorem-controlled ledger with independent enumeration and formula engines. The collision $r_2=r_4=3$ shows why the local exception supplies neither a common intrinsic modulus clock nor a prime selector. This is a scoped synthesis of established constructions, not a new zeta or stack theory and not a universal no-go statement.
author:
- Anonymous Authors
bibliography:
- references.bib
date: 'Pre-review manuscript, August 15, 2026'
title: 'An Equivariant-Zeta Audit of Cat-Map Centralizer Quotients'
```

## Markdown 正文

**Keywords:** cat map, Burnside ring, equivariant zeta, finite permutation, orbifold reduction, quotient stack, periodic orbit.

# Introduction and bounded question {#sec:introduction}

Let $$A=\begin{pmatrix}2&1\\1&1\end{pmatrix},
  \qquad R_q=\mathbb{Z}/q\mathbb{Z},
  \qquad q\ge2.
  \label{eq:cat-matrix}$$ A preceding finite-module audit identifies a canonical cyclic-vector locus $X_q=\mathrm{CV}_q\subset R_q^2$ and proves that $$G_q=\operatorname{Cent}_{\operatorname{GL}_2(R_q)}(A)=R_q[A]^\times
  \label{eq:centralizer}$$ acts freely and transitively on $X_q$. The cat map acts on this torsor by left translation through the distinguished element $a_q=A\bmod q\in G_q$. The coarse quotient $X_q/G_q$ is one point, and the induced transformation is identity because the transformation being studied already belongs to the group being divided out.

That one-point quotient poses a precise follow-up question. Can a standard equivariant, orbifold, or stack-level refinement retain enough of the erased motion to yield one intrinsic modulus-dependent local clock? A useful answer must distinguish several objects that are sometimes grouped under the phrase *equivariant zeta*. Fixed points, fixed group-orbits, full twisted fixed-point tables, enhanced equivariant sets, and quotient stacks retain different data and take values in different coefficient categories. The question is which information survives each named construction, what extra labels that retention costs, and whether any retained datum is a return-time law that identifies $q$ or selects prime moduli.

The answer is a definition-sensitive hierarchy. The point-order rational Burnside series remembers source period. Its ordinary cardinality reduction also remembers the number of source cycles, while its additive orbifold reduction has a fractional exponent. The orbit-order integral Burnside series remembers the free orbit type but has only period one. Stronger $G_q$-permutation and enhanced carriers remember $a_q$ because the regular action is effective and $G_q$ is kept as a labelled ambient group. Morita-invariant quotient-stack data collapse to a fixed point. These are positive and negative boundaries of different constructions, not competing claims about one invariant.

[\[rem:scope-correction\]]{#rem:scope-correction label="rem:scope-correction"} Frozen design prose described the four scalar reductions with an overstrong per-row quantifier. The exact registered ledger contains one exception: at $q=2$, $m_2=1$, so point-cardinality reduction is $(1-t^3)^{-1}$ and has both source support and unit exponent. The registered control K011 checks the weaker and correct family statement: no single reduction type has both properties uniformly across all nine locked moduli. We use only that family-uniform statement. The raw formulas and results are unchanged, and the A0 conclusion below concerns the absence of a common intrinsic modulus or prime clock. A fresh semantic audit issued `PASS_WITH_SCOPE_CORRECTION` for this publication boundary.

This note makes five bounded contributions.

1.  It gives one theorem for translation on an arbitrary finite abelian $C$-set, covering source cycles, coarse quotient cycles, both Burnside exact-period sequences, additive orbifold reductions, $\mathbb{Z}\times C$ stabilizers, action kernels, and quotient-stack inertia.

2.  It separates additive exact-period reduction from Burnside-ring multiplication and supplies an explicit nonmultiplicativity witness.

3.  It records effectivization and rigidification boundaries: the full twisted carrier recovers $a$ only modulo the ineffective kernel, whereas isotropy that survives in $BK$ components carries identity dynamics and disappears under componentwise rigidification.

4.  It specializes the hierarchy to the regular cat-map centralizer torsor, deriving point-order, orbit-order, $G$-permutation, enhanced, orbifold, groupoid, shortening, and gluing records without conflating their coefficient categories.

5.  It reports a source-locked exact audit on nine predeclared moduli and one separately typed $C_6$ structural control, with dual scientific engines and a separately reviewed post-run analyzer.

The contribution is deliberately modest. The underlying rational Burnside series, $G$-permutation invariant, integral orbit-order series, orbifold maps, enhanced carrier, and quotient-orbit mechanisms are prior art. We audit their interaction on one previously frozen torsor family. We do not define a new equivariant, Burnside, orbifold, groupoid, or stacky zeta; prove historical priority; construct a canonical comparison among the varying groups $G_q$; or exclude unexamined representation-valued, weighted, analytic, transfer-operator, Fredholm, Hecke, quantized, Ruelle, or Fried refinements. No prime--zero correspondence or Riemann-hypothesis mechanism is asserted.

Section [2](#sec:prior){reference-type="ref" reference="sec:prior"} fixes the prior-art and definition boundaries. Section [3](#sec:definitions){reference-type="ref" reference="sec:definitions"} defines the finite carriers and additive reductions. Section [4](#sec:general){reference-type="ref" reference="sec:general"} proves the general finite-$C$-set theorem. Section [5](#sec:groupoid){reference-type="ref" reference="sec:groupoid"} treats effectivity, inertia, and rigidification, including the $C_6$ control. Section [6](#sec:cat-specialization){reference-type="ref" reference="sec:cat-specialization"} specializes to the cat-map torsor. Section [7](#sec:audit){reference-type="ref" reference="sec:audit"} reports the exact audit and provenance. Section [8](#sec:discussion){reference-type="ref" reference="sec:discussion"} states the clock semantics, limitations, and route decision.

# Prior art and definition boundary {#sec:prior}

Finite cat-map centralizers, reversing symmetries, rational lattices, and field-level normal types already have a direct dynamical treatment [@BaakeNeumaerkerRoberts2013]. The regular $G_q$-torsor used here is imported from the separately finalized preceding audit. The present note neither reclassifies finite centralizers nor presents that torsor as a new rational-lattice theorem.

The rational point-order construction originates in the equivariant monodromy-zeta framework of @GuseinZadeLuengoMelle2008. It uses equivariant Lefschetz classes in the rationalized Burnside ring together with the Burnside pre-$\lambda$/power structure. This source blocks any claim that the rational exact-period series below is a construction of the present note.

The strongest direct collision is the later treatment by @GuseinZadeLuengoMelle2015. That work explicitly separates the equivariant Lefschetz class of fixed points from the alternative class of setwise fixed $G$-orbits. It defines the integral orbit-order zeta and two orbifold reductions, and its examples distinguish transformation order in a space from transformation order in a quotient. In particular, when the transformation belongs to the acting symmetry group, the induced quotient action is trivial. Our regular-torsor formulas are a finite specialization of that distinction.

A different invariant appears in @GuseinZade2013. It is a virtual finite or locally finite $G$-permutation, equivalently a $\mathbb{Z}\times G$-set, determined by all twisted classes $L^G(g\phi^m)$. Its irreducible data include a stabilizer, a return integer, and a twist coset. This full twisted carrier is strictly stronger than the untwisted point-order series in the present example. The enhanced Burnside framework of @EbelingGuseinZade2018 adds a transformation and isotropy characters and supplies a separate fixed-sector orbifold reduction. Again, we specialize those definitions rather than modify them.

Quotient-orbit shortening and gluing follow the framework of @Zegowitz2017. Her orbit-intersection formulas identify exactly how many source cycles glue and by what factor a source period shortens. @Miles2017 develops a different zeta for finitely generated acting groups through their finite-index subgroups and tacitly assumes an infinite acting group. It is a scope boundary, not an off-the-shelf finite-$G_q$ replacement. Likewise, @Walton2018 studies periodic points and twists on quotient varieties over finite fields; its hypotheses do not extend the present finite-set calculation to composite residue rings.

The current frontier uses equivariance and orbifolds in substantially different settings. Mackey-functor and cohomological zetas [@Rahmati2024], cyclic-nerve symmetries [@AyalaMazelGeeRozenblyum2025], and equivariant Ruelle, trace, and Fried programs [@HochsSaratchandran2023; @HochsSaratchandran2025; @HochsPirie2025] do not share the finite Burnside definitions audited here. A recent survey also places monodromy-zeta variants in a mature literature [@GuseinZade2026]. These works prevent a narrow finite-set calculation from being presented as a general statement about every use of *equivariant* or *orbifold* zeta.

Table [\[tab:carrier-boundary\]](#tab:carrier-boundary){reference-type="ref" reference="tab:carrier-boundary"} records the nomenclature used throughout. Every row names a different carrier or reduction.

\@L0.22L0.23YY@ Construction & Input used & Retained datum on a regular torsor & Main loss or cost\
Point-order rational Burnside zeta & fixed-point classes $L^G(\phi^k)$ & source order and regular orbit coefficient & rational exponent; untwisted data see the cyclic subgroup, not its chosen generator\
Orbit-order integral Burnside zeta & fixed-$G$-orbit classes $\widetilde L^G(\phi^k)$ & regular orbit type & dynamical support only at period one\
$G$-permutation zeta & all $L^G(g\phi^k)$ & labelled twist modulo action kernel & a varying $\mathbb{Z}\times G$-set category\
Enhanced Burnside carrier & transformation and isotropy characters & labelled return twist & free torsor has only the trivial character\
Orbifold/stack image & exact-period additive map or fixed sectors & static stabilizer sectors when present & no nontrivial quotient return period\

Figure [\[fig:retention-hierarchy\]](#fig:retention-hierarchy){reference-type="ref" reference="fig:retention-hierarchy"} summarizes the definition firewall and the information retained by each named construction.

![image](<../../../../../symplectic_map/papers/11-cat-equivariant-clock/paper/figures/fig1_retention_hierarchy.pdf>){width="\\textwidth"}

# Finite carriers and additive reductions {#sec:definitions}

Let $C$ be a finite abelian group, let $X$ be a finite $C$-set, and let $\phi\colon X\to X$ be a $C$-equivariant bijection. Write $B(C)=K_0(\mathrm{f.}\,C\text{-sets})$ for the Burnside ring. We use the Artin--Mazur inverse convention: a cycle of length $d$ contributes $(1-t^d)^{-1}$.

The fixed-point equivariant Lefschetz class is $L^C(\phi^k)=[\operatorname{Fix}(\phi^k)]\in B(C)$. Its exact-period classes $P_m^C\in B(C)$ are defined by divisor inversion, $$L^C(\phi^k)=\sum_{m\mid k}P_m^C.
  \label{eq:point-inversion}$$ The point-order rational Burnside zeta is $$\zeta_{\mathrm{pt}}^C(\phi;t)
  =\prod_{m\ge1}(1-t^m)^{-P_m^C/m}.
  \label{eq:point-zeta-definition}$$

The coefficients in [\[eq:point-zeta-definition\]](#eq:point-zeta-definition){reference-type="eqref" reference="eq:point-zeta-definition"} generally lie in $B(C)\otimes\mathbb{Q}$. This is the fixed-point construction associated with the 2008 rational series; it is not the integral orbit-order construction.

Let $\widetilde L^C(\phi^k)$ be the Burnside class of $C$-orbits that are setwise fixed by $\phi^k$, decorated by their orbit types. Define $\widetilde P_m^C$ by $$\widetilde L^C(\phi^k)=\sum_{m\mid k}\widetilde P_m^C.
  \label{eq:orbit-inversion}$$ The orbit-order integral Burnside zeta is $$\widetilde\zeta_{\mathrm{orbset}}^C(\phi;t)
  =\prod_{m\ge1}(1-t^m)^{-\widetilde P_m^C/m}.
  \label{eq:orbit-zeta-definition}$$

The divisibility theorem behind this construction makes [\[eq:orbit-zeta-definition\]](#eq:orbit-zeta-definition){reference-type="eqref" reference="eq:orbit-zeta-definition"} integral in the setting of @GuseinZadeLuengoMelle2015. In our finite translation model the integrality will also be visible directly.

For an additive map of abelian groups $\psi\colon B(C)\to R$, define $$\psi_*\!\left(\prod_{m\ge1}(1-t^m)^{-S_m/m}\right)
  :=\prod_{m\ge1}(1-t^m)^{-\psi(S_m)/m}.
  \label{eq:additive-reduction}$$ The map is applied to exact-period exponent classes before the scalar product is formed.

Two maps will be used. Cardinality is $\kappa_C([Y])=|Y|$. For abelian $C$, the orbifold map is the additive homomorphism $$\Phi_C([C/K])=|K|.
  \label{eq:orbifold-map}$$ No multiplicativity of $\Phi_C$ is available or needed. Indeed, if $C\ne1$ and $\mathbf{u}=[C/1]$, then the diagonal Cartesian product splits into $|C|$ regular orbits, so $$\mathbf{u}^2=|C|\mathbf{u},
  \qquad
  \Phi_C(\mathbf{u}^2)=|C|\ne1=\Phi_C(\mathbf{u})^2.
  \label{eq:nonmultiplicativity}$$ Equation [\[eq:additive-reduction\]](#eq:additive-reduction){reference-type="eqref" reference="eq:additive-reduction"} uses only the additive structure; it does not require $\psi$ to preserve Burnside multiplication, the pre-$\lambda$ structure, or the symmetric-power structure. Cardinality $\kappa_C$ is in fact multiplicative on finite $C$-sets, whereas $\Phi_C$ fails multiplicativity by [\[eq:nonmultiplicativity\]](#eq:nonmultiplicativity){reference-type="eqref" reference="eq:nonmultiplicativity"}. For $\Phi_C$, the definition records the 2015 procedure: reduce the Lefschetz sequence additively, perform divisor inversion, and form the scalar series.

The 2013 $C$-permutation invariant uses more input than either untwisted series. It is represented by the finite $\mathbb{Z}\times C$-set obtained from $$(j,c)\cdot x=c\phi^j(x).
  \label{eq:z-times-c-action}$$ Equivalently, it is determined by the complete table $L^C(c\phi^j)$. The enhanced carrier further keeps the transformation and isotropy characters. We reserve the names $C$-permutation zeta and enhanced Burnside carrier for these stronger labelled objects and do not identify them with [\[eq:point-zeta-definition\]](#eq:point-zeta-definition){reference-type="eqref" reference="eq:point-zeta-definition"} or [\[eq:orbit-zeta-definition\]](#eq:orbit-zeta-definition){reference-type="eqref" reference="eq:orbit-zeta-definition"}.

# Translation on a finite abelian $C$-set {#sec:general}

Fix $a\in C$, put $H=\langle a\rangle$, and write the orbit-type decomposition $$X\simeq\coprod_{K\le C} n_K(C/K),
  \qquad n_K\in\mathbb{Z}_{\ge0}.
  \label{eq:orbit-decomposition}$$ Because $C$ is abelian, no conjugacy ambiguity remains in the subgroup index $K$. For each represented orbit type define $$d_K=[H:H\cap K],
  \qquad
  M_K=[C:HK].
  \label{eq:d-m-definitions}$$

[\[thm:finite-hierarchy\]]{#thm:finite-hierarchy label="thm:finite-hierarchy"} Let $C$ be finite abelian and let $\phi_a(x)=ax$ act on [\[eq:orbit-decomposition\]](#eq:orbit-decomposition){reference-type="eqref" reference="eq:orbit-decomposition"}. Then:

1.  every point in a copy of $C/K$ has exact period $d_K$, and that copy contains $M_K$ translation cycles;

2.  the ordinary source zeta and coarse quotient zeta are $$\begin{aligned}
              \zeta_{X,\phi_a}(t)
              &=\prod_{K\le C}(1-t^{d_K})^{-n_K[C:HK]},
              \label{eq:general-source-zeta}\\
              \zeta_{X/C,\bar\phi_a}(t)
              &=(1-t)^{-\sum_K n_K};
              \label{eq:general-coarse-zeta}
            \end{aligned}$$

3.  the exact point-order and orbit-order Burnside classes are $$\begin{aligned}
              P_m^C&=\sum_{d_K=m}n_K[C/K],
              \label{eq:general-point-class}\\
              \widetilde P_1^C&=[X]=\sum_Kn_K[C/K],
              &
              \widetilde P_m^C&=0\quad(m>1);
              \label{eq:general-orbit-class}
            \end{aligned}$$

4.  additive orbifold reduction gives $$\begin{aligned}
              \Phi_{C,*}(\zeta_{\mathrm{pt}}^C)
              &=\prod_K(1-t^{d_K})^{-n_K|K|/d_K},
              \label{eq:general-point-orbifold}\\
              \Phi_{C,*}(\widetilde\zeta_{\mathrm{orbset}}^C)
              &=(1-t)^{-\sum_Kn_K|K|};
              \label{eq:general-orbit-orbifold}
            \end{aligned}$$

5.  on $C/K$, the $\mathbb{Z}\times C$-stabilizer under [\[eq:z-times-c-action\]](#eq:z-times-c-action){reference-type="eqref" reference="eq:z-times-c-action"} is $$\widehat K_a
              =\left\langle\{0\}\times K,\,(1,a^{-1})\right\rangle;
              \label{eq:general-twisted-stabilizer}$$ across all represented orbit types, this labelled carrier recovers $a$ exactly modulo the action kernel $$N=\bigcap_{n_K>0}K;
              \label{eq:action-kernel}$$

6.  the quotient stack and its inertia decompose as $$\simeq\coprod_K n_K BK,
              \label{eq:stack-decomposition}$$ with $\sum_Kn_K|K|$ inertia components; translation by $a$ induces identity dynamics up to $2$-isomorphism on every component.

On $C/K$, the equality $a^jcK=cK$ is equivalent to $a^j\in K$. The least positive such $j$ is the order of $a$ in $H/(H\cap K)$, namely $d_K$. Every point has that period. Orbit--stabilizer then gives $$\frac{[C:K]}{d_K}
  =\frac{|C|\,|H\cap K|}{|K|\,|H|}
  =\frac{|C|}{|HK|}
  =[C:HK]=M_K,
  \label{eq:cycle-count-identity}$$ which proves the first claim and [\[eq:general-source-zeta\]](#eq:general-source-zeta){reference-type="eqref" reference="eq:general-source-zeta"}.

Each copy of $C/K$ is one $C$-orbit. Since $a\in C$, translation is identity on the orbit quotient, proving [\[eq:general-coarse-zeta\]](#eq:general-coarse-zeta){reference-type="eqref" reference="eq:general-coarse-zeta"}. The points of exact period $m$ are precisely the components with $d_K=m$, which proves [\[eq:general-point-class\]](#eq:general-point-class){reference-type="eqref" reference="eq:general-point-class"}. Every $C$-orbit is setwise fixed from the first iterate, which proves [\[eq:general-orbit-class\]](#eq:general-orbit-class){reference-type="eqref" reference="eq:general-orbit-class"}. Applying the additive map $\Phi_C([C/K])=|K|$ to those exact-period classes, and only then forming the products, yields [\[eq:general-point-orbifold\]](#eq:general-point-orbifold){reference-type="eqref" reference="eq:general-point-orbifold"} and [\[eq:general-orbit-orbifold\]](#eq:general-orbit-orbifold){reference-type="eqref" reference="eq:general-orbit-orbifold"}.

For the base coset $K$, a pair $(j,c)$ stabilizes $K$ precisely when $ca^j\in K$. This subgroup is generated by $\{0\}\times K$ and $(1,a^{-1})$, proving [\[eq:general-twisted-stabilizer\]](#eq:general-twisted-stabilizer){reference-type="eqref" reference="eq:general-twisted-stabilizer"}. It records the coset $a^{-1}K$. Two translation labels give the same recorded coset for every represented $K$ exactly when they agree modulo the intersection [\[eq:action-kernel\]](#eq:action-kernel){reference-type="eqref" reference="eq:action-kernel"}.

Finally, the transitive action groupoid $C\mathbin{\ltimes}(C/K)$ is equivalent to the one-object groupoid $BK$. Since $K$ is abelian, its inertia is indexed by its $|K|$ elements. The arrow labelled $a$ gives a natural isomorphism between the identity functor and translation by $a$; naturality uses $ac=ca$. Thus each inertia component has static period-one dynamics.

[\[cor:subgroup-only\]]{#cor:subgroup-only label="cor:subgroup-only"} The point-order sequence $\{P_m^C\}$ depends on $a$ only through $H=\langle a\rangle$, so it cannot distinguish two generators of the same cyclic subgroup. The orbit-order sequence has no support beyond period one. The full labelled $C$-permutation carrier distinguishes $a$ only modulo $N$, and distinguishes it exactly if and only if the $C$-action is effective.

Applying $\kappa_C$ to [\[eq:general-point-class\]](#eq:general-point-class){reference-type="eqref" reference="eq:general-point-class"} gives exponent $[C:K]/d_K=[C:HK]$ on each represented component. Hence the ordinary source zeta [\[eq:general-source-zeta\]](#eq:general-source-zeta){reference-type="eqref" reference="eq:general-source-zeta"} is the point-order cardinality reduction. This identity does not turn $\Phi_C$ into a ring map and does not identify the stronger labelled carrier with either Burnside series.

# Effectivity, inertia, and rigidification {#sec:groupoid}

The kernel $N$ in [\[eq:action-kernel\]](#eq:action-kernel){reference-type="eqref" reference="eq:action-kernel"} separates two operations that can otherwise look alike. First, *effectivization* replaces $C$ by $C/N$. Each orbit becomes $$C/K\simeq (C/N)/(K/N),
  \label{eq:effectivized-orbit}$$ and the translation label becomes $aN$. The full twisted carrier recovers exactly this effective label. It does not canonically lift $aN$ back to a chosen element of $C$.

Second, the quotient stack retains isotropy: $$[X/(C/N)]\simeq\coprod_Kn_KB(K/N).$$ The map from $[X/C]$ to this effective quotient removes the globally ineffective subgroup $N$; in finite-groupoid language, it is the rigidification along the common ineffective stabilizer. Residual $K/N$-isotropy remains. If one then rigidifies each residual $B(K/N)$ component completely, that component becomes a point. Neither operation creates motion: translation was already $2$-isomorphic to identity before effectivization, and every retained inertia component remains static.

This distinction gives three boundaries.

-   Presentation-sensitive data such as the labelled $\mathbb{Z}\times C$-set can retain $aN$.

-   Morita-invariant quotient data can retain stabilizer groups or inertia multiplicities, but not a nontrivial translation period.

-   Full rigidification removes the remaining static isotropy rather than converting it into a return clock.

No claim is made that every object called a stacky zeta factors through these operations. The statement concerns invariants that respect Morita equivalence and the $2$-isomorphism class of the induced endomorphism.

## The effective $C_6$ control

Let $C=C_6$, let $a$ be a generator, and set $$X=C_6/C_2\ \sqcup\ C_6/C_3,
  \label{eq:c6-control}$$ where $C_j$ is the unique subgroup of order $j$. The action is effective because $C_2\cap C_3=1$, so the labelled $C$-permutation carrier recovers $a$. Nevertheless, $$d_{C_2}=3,\qquad d_{C_3}=2,\qquad
  M_{C_2}=M_{C_3}=1.$$ The exact outputs are therefore $$\begin{aligned}
  \zeta_{X,\phi_a}(t)
    &=(1-t^3)^{-1}(1-t^2)^{-1},
    \label{eq:c6-source}\\
  \zeta_{X/C,\bar\phi_a}(t)
    &=(1-t)^{-2},
    \label{eq:c6-coarse}\\
  \Phi_{C,*}(\zeta_{\mathrm{pt}}^C)
    &=(1-t^3)^{-2/3}(1-t^2)^{-3/2},
    \label{eq:c6-point-orbifold}\\
  \Phi_{C,*}(\widetilde\zeta_{\mathrm{orbset}}^C)
    &=(1-t)^{-5}.
    \label{eq:c6-orbit-orbifold}\end{aligned}$$ The quotient stack is $BC_2\sqcup BC_3$, with five static inertia components. Thus effectivity and exact recovery of a labelled order-six translation do not force a period-six source factor. The $C_6$ object is a structural unit control; it is neither an arithmetic modulus row nor a second candidate.

Figure [\[fig:effectivity-counterexamples\]](#fig:effectivity-counterexamples){reference-type="ref" reference="fig:effectivity-counterexamples"} below places this effective control beside the regular and trivial-action boundaries.

# The regular cat-map centralizer torsor {#sec:cat-specialization}

We now specialize Theorem [\[thm:finite-hierarchy\]](#thm:finite-hierarchy){reference-type="ref" reference="thm:finite-hierarchy"}. The only imported arithmetic statement is the frozen terminal result of the preceding centralizer audit: $$X_q=\mathrm{CV}_q\simeq G_q
  \quad\text{as a left regular \(G_q\)-set},
  \qquad
  \phi_q(x)=a_qx,
  \quad a_q=A\bmod q.
  \label{eq:regular-torsor}$$ No candidate or calculation from that centralizer-quotient audit is rerun here. Put $$n_q=|G_q|,
  \qquad
  r_q=\operatorname{ord}_{G_q}(a_q)=\operatorname{ord}_q(A),
  \qquad
  m_q=\frac{n_q}{r_q},
  \qquad
  \mathbf u_q=[G_q/1]\in B(G_q).
  \label{eq:n-r-m}$$ In the notation of Section [4](#sec:general){reference-type="ref" reference="sec:general"}, the regular torsor has one orbit type $K=1$, so $d_1=r_q$ and $M_1=m_q$.

[\[thm:regular-ledger\]]{#thm:regular-ledger label="thm:regular-ledger"} For every $q\ge2$, the following statements hold.

1.  The source consists of $m_q$ cycles of length $r_q$, and $$\zeta_{\phi_q}(t)=(1-t^{r_q})^{-m_q}.
              \label{eq:regular-source-zeta}$$

2.  The point-order and orbit-order Burnside zetas are $$\begin{aligned}
              \zeta_{\mathrm{pt},q}^{G_q}(t)
              &=(1-t^{r_q})^{-\mathbf u_q/r_q},
              \label{eq:regular-point-zeta}\\
              \widetilde\zeta_{\mathrm{orbset},q}^{G_q}(t)
              &=(1-t)^{-\mathbf u_q}.
              \label{eq:regular-orbit-zeta}
            \end{aligned}$$

3.  Cardinality and additive orbifold reduction give exactly $$\begin{aligned}
              \kappa_{G_q,*}(\zeta_{\mathrm{pt},q}^{G_q})
                &=(1-t^{r_q})^{-m_q},
              &
              \Phi_{G_q,*}(\zeta_{\mathrm{pt},q}^{G_q})
                &=(1-t^{r_q})^{-1/r_q},
              \label{eq:regular-point-reductions}\\
              \kappa_{G_q,*}(\widetilde\zeta_{\mathrm{orbset},q}^{G_q})
                &=(1-t)^{-n_q},
              &
              \Phi_{G_q,*}(\widetilde\zeta_{\mathrm{orbset},q}^{G_q})
                &=(1-t)^{-1}.
              \label{eq:regular-orbit-reductions}
            \end{aligned}$$

4.  The complete twisted table is $$L^{G_q}(g\phi_q^k)
              =
              \begin{cases}
                \mathbf u_q,&g=a_q^{-k},\\
                0,&g\ne a_q^{-k}.
              \end{cases}
              \label{eq:twisted-table}$$ Hence the $G_q$-permutation stabilizer is $\langle(1,a_q^{-1})\rangle$, with irreducible triple $(\{e\},1,a_q^{-1})$.

5.  The enhanced carrier is $\widehat X_{\{e\},1,a_q,1}$, while its enhanced orbifold zeta is $(1-t)^{-1}$.

6.  The action groupoid $G_q\mathbin{\ltimes}X_q$ is equivalent to one point, has no nonidentity inertia component, and carries an induced endofunctor naturally isomorphic to identity.

7.  Every source cycle shortens by $1/r_q$, and precisely $m_q$ source cycles glue to the quotient fixed point.

Under [\[eq:regular-torsor\]](#eq:regular-torsor){reference-type="eqref" reference="eq:regular-torsor"}, $\phi_q^k(x)=a_q^kx$. Cancellation shows that one point is fixed if and only if $a_q^k=1$, in which case every point is fixed. Thus every point has exact period $r_q$, giving [\[eq:regular-source-zeta\]](#eq:regular-source-zeta){reference-type="eqref" reference="eq:regular-source-zeta"} and $$L^{G_q}(\phi_q^k)
  =
  \begin{cases}
    \mathbf u_q,&r_q\mid k,\\
    0,&r_q\nmid k.
  \end{cases}
  \label{eq:regular-point-lefschetz}$$ Divisor inversion places the sole point exact class $\mathbf u_q$ at $r_q$, which proves [\[eq:regular-point-zeta\]](#eq:regular-point-zeta){reference-type="eqref" reference="eq:regular-point-zeta"}. There is exactly one $G_q$-orbit and it is setwise fixed at every iterate. The sole orbit exact class is therefore $\mathbf u_q$ at support one, proving [\[eq:regular-orbit-zeta\]](#eq:regular-orbit-zeta){reference-type="eqref" reference="eq:regular-orbit-zeta"}.

Regularity gives $\kappa_{G_q}(\mathbf u_q)=n_q$ and $\Phi_{G_q}(\mathbf u_q)=1$. Applying these maps to the exact classes proves [\[eq:regular-point-reductions\]](#eq:regular-point-reductions){reference-type="eqref" reference="eq:regular-point-reductions"} and [\[eq:regular-orbit-reductions\]](#eq:regular-orbit-reductions){reference-type="eqref" reference="eq:regular-orbit-reductions"}. A twisted iterate acts by translation through $ga_q^k$; it fixes a point exactly when $g=a_q^{-k}$. This proves [\[eq:twisted-table\]](#eq:twisted-table){reference-type="eqref" reference="eq:twisted-table"}, the stabilizer, and the inverse convention in the $G_q$-permutation triple.

The regular action has trivial isotropy and one group orbit. The enhanced return twist is $a_q$, not $a_q^{-1}$, and its only character is trivial. Only the identity fixed sector is nonempty, so the enhanced orbifold image is one fixed point. The action groupoid is transitive with trivial automorphism groups. Arrows labelled $a_q$ define a natural isomorphism from identity to the induced endofunctor. Finally, $|\mathcal O_{\phi_q}(x)\cap\mathcal O_{G_q}(x)|=r_q$, while $|\mathcal O_{G_q}(x)|=n_q$. The shortening and gluing values follow from the quotient-orbit formulas of @Zegowitz2017.

[\[prop:corrected-tradeoff\]]{#prop:corrected-tradeoff label="prop:corrected-tradeoff"} The point-cardinality factor in [\[eq:regular-point-reductions\]](#eq:regular-point-reductions){reference-type="eqref" reference="eq:regular-point-reductions"} has source support and unit exponent exactly when $m_q=1$. The point-orbifold factor has source support with exponent $1/r_q$, while both orbit factors have support one. In the locked nine-row ledger, the first condition occurs at $q=2$ and nowhere else. Consequently, no one reduction type supplies source support and unit exponent uniformly across the locked family.

The four support--exponent pairs read directly from [\[eq:regular-point-reductions\]](#eq:regular-point-reductions){reference-type="eqref" reference="eq:regular-point-reductions"}--[\[eq:regular-orbit-reductions\]](#eq:regular-orbit-reductions){reference-type="eqref" reference="eq:regular-orbit-reductions"}: $$(r_q,m_q),\qquad
  (r_q,1/r_q),\qquad
  (1,n_q),\qquad
  (1,1).
  \label{eq:four-support-exponent-pairs}$$ The first pair has unit exponent precisely when $m_q=1$. For the fixed matrix, $r_q>1$ for every $q\ge2$, because the off-diagonal entry of $A-I$ is $1$. Thus $1/r_q\ne1$, and support one is not source support. The exact ledger in Section [7](#sec:audit){reference-type="ref" reference="sec:audit"} has $m_2=1$ and $m_q>1$ for its other eight rows.

#### C21-corrected.

No one of the four scalar-reduction types has source support and unit exponent for every modulus in the locked family. The unique locked row/type exception is $(q,j)=(2,\kappa\mathrm{pt})$, where the source already consists of one cycle. We do not use the overstrong assertion that every row/type pair fails.

## Labelled retention and coefficient cost

Equations [\[eq:twisted-table\]](#eq:twisted-table){reference-type="eqref" reference="eq:twisted-table"} and the enhanced tuple give a positive retention statement: the stronger carriers recover the exact local translation $a_q$ on the effective regular action. This is not a common clock across moduli. The values lie, respectively, in $$K_0(\mathrm{f.}\,G_q\text{-perm})
  \qquad\text{and}\qquad
  \widehat B(G_q),$$ and the ambient labelled group $G_q$ varies with $q$. The construction supplies no canonical cross-$q$ identification. Reading the group name or the matrix label $A\bmod q$ as a modulus is therefore reading family metadata, not extracting a return time.

The quotient outputs make the opposite choice. They remove the labelled presentation and retain only a point with identity dynamics. On the regular torsor even isotropy disappears: the only inertia component is the identity sector. The labelled carriers and the Morita quotient are both valid, but they answer different questions.

# Exact nine-row retention audit {#sec:audit}

The registered audit used exactly the ordered tuple $$\mathcal Q_{\mathrm{lock}}=(2,3,5,7,11,4,6,9,10)
  \label{eq:locked-moduli}$$ and no other arithmetic modulus. The first five rows are predeclared prime controls and the last four are predeclared composite controls. The structural $C_6$ example in [\[eq:c6-control\]](#eq:c6-control){reference-type="eqref" reference="eq:c6-control"} occupied a separate namespace and never entered $\mathcal Q_{\mathrm{lock}}$.

Table [1](#tab:nine-row-ledger){reference-type="ref" reference="tab:nine-row-ledger"} reproduces exact integer and rational data from the registered result. The star is important: it is the unique locked row/type pair that combines source support with unit exponent.

::: {#tab:nine-row-ledger}
  ----- ------- ------- ------- -------------------------- ------------------------ -------------------------- ------------------------
    $q$  $n_q$   $r_q$   $m_q$   $\kappa(\mathrm{point})$   $\Phi(\mathrm{point})$   $\kappa(\mathrm{orbit})$   $\Phi(\mathrm{orbit})$

      2    3       3       1      $\mathbf{(3,1)}^\star$          $(3,1/3)$                  $(1,3)$                   $(1,1)$
      3    8       4       2             $(4,2)$                  $(4,1/4)$                  $(1,8)$                   $(1,1)$
      5   20      10       2             $(10,2)$                $(10,1/10)$                 $(1,20)$                  $(1,1)$
      7   48       8       6             $(8,6)$                  $(8,1/8)$                  $(1,48)$                  $(1,1)$
     11   100      5      20             $(5,20)$                 $(5,1/5)$                 $(1,100)$                  $(1,1)$
      4   12       3       4             $(3,4)$                  $(3,1/3)$                  $(1,12)$                  $(1,1)$
      6   24      12       2             $(12,2)$                $(12,1/12)$                 $(1,24)$                  $(1,1)$
      9   72      12       6             $(12,6)$                $(12,1/12)$                 $(1,72)$                  $(1,1)$
     10   60      30       2             $(30,2)$                $(30,1/30)$                 $(1,60)$                  $(1,1)$
  ----- ------- ------- ------- -------------------------- ------------------------ -------------------------- ------------------------

  : Exact support/exponent ledger. The point-cardinality reduction at $q=2$ is $(3,1)$, the sole locked row/type pair combining source support and unit exponent. No reduction type does so uniformly across all nine rows; the retained support still fails to identify the modulus because $r_2=r_4=3$. Entries are exact and use the inverse Artin--Mazur sign convention.
:::

Every row also has the following exact carrier data:

-   the $G_q$-permutation twist is $a_q^{-1}$, and the enhanced return twist is $a_q$;

-   the effective regular action recovers the labelled $a_q$;

-   no nonidentity inertia sector is nonempty; and

-   the coarse, enhanced-orbifold, and quotient-stack periods are one.

These statements live in separate raw-result namespaces. They were not derived by relabelling one scalar factor.

## What the finite rows show

The rows expose two order collisions: $$r_2=r_4=3,
  \qquad
  r_6=r_9=12.
  \label{eq:period-collisions}$$ The first collision directly limits the $q=2$ exception. Although $(1-t^3)^{-1}$ is a one-cycle source factor, support three does not identify modulus two because composite modulus four has the same source order. The second collision shows the same noninjectivity at a larger period. All four composite controls satisfy the same retention hierarchy, so the construction has no intrinsic prime selector.

The family-level scalar control is recorded with its actual logical scope:

> `K011 — family-uniform source-support/unit-exponent nonattainment.`

Its first clause checks that not all point-cardinality exponents are one; it does not check that every such exponent is nonunit. The other clauses check that point-orbifold exponents are nonunit and that both orbit reductions have support different from $r_q$. Thus the stored Boolean is correct, while the stronger prose gloss preserved in some frozen design and review files is superseded by Remark [\[rem:scope-correction\]](#rem:scope-correction){reference-type="ref" reference="rem:scope-correction"} and Proposition [\[prop:corrected-tradeoff\]](#prop:corrected-tradeoff){reference-type="ref" reference="prop:corrected-tradeoff"}.

Figure [\[fig:nine-row-retention\]](#fig:nine-row-retention){reference-type="ref" reference="fig:nine-row-retention"} gives the complete visual ledger and marks the sole locked exception rather than hiding it in a family aggregate.

![image](<../../../../../symplectic_map/papers/11-cat-equivariant-clock/paper/figures/fig2_nine_row_retention.pdf>){width="\\textwidth"}

![image](<../../../../../symplectic_map/papers/11-cat-equivariant-clock/paper/figures/fig3_effectivity_counterexamples.pdf>){width="\\textwidth"}

## One registered run and two scientific engines

The audit was exact rather than statistical. It used no random seed, floating fit, external prime table, Riemann-zero data, numerical $s$, numerical $\log q$, or numerical $q^{-s}$. One engine explicitly enumerated residue matrices, cyclic vectors, group elements, source cycles, fixed sets, twisted fixers, and action-groupoid data. A separate engine constructed the same scientific records from the regular-torsor theorem. After removing only the engine identifier, their records agreed exactly.

A fresh verifier did not import or invoke the candidate. It independently enumerated the complete finite objects, reconstructed every formal factor and rational exponent, and matched all nine rows and the separate $C_6$ control. It also checked the general cyclic-$C_n$ formulas on 264 subgroup fixtures with no discrepancy. This independent reconstruction issued `RESULT_PASS`. The finite audit validates transcription and implementation; the proof, not nine finite rows, remains the authority for the all-$q$ statements.

## Dual-tree closure and preserved failure history

The immutable registered execution tree and the post-run analyzer are separate authorities. The execution tree has digest

`5ee1918a57fee56a2ca5a117c5749f614efbfd6baed96ae45480d6091a4741eb`,

whereas the analyzer tree has digest

`423082f4675a1d41622bcb3d090a2c4c67d4732ff6dc32d0298505d90d5a78c3`.

The analyzer was permitted to validate immutable result artifacts but had no candidate authority.

The first manifest attempt failed before writing a file. Its K005 validator compared a JSON list with a Python tuple, so a correct unique-fixer record was rejected on type rather than scientific content. The raw result, claim, terminal, and execution tree remained unchanged. The separately reviewed analyzer repaired only this serialized-list boundary, reproduced all 174 unique-fixer checks, and then created the V2 manifest once. Read-only final closure passed, a second write was rejected, and the final result manifest has digest

`a0b409061c34eff0d68fdc326fe4ec6ff9295895444b857ee161fd77e417292c`.

This history matters because manifest closure establishes provenance and inventory integrity; it does not promote an imprecise prose quantifier into a theorem. The later semantic scope audit performs that separate task.

# Clock semantics, limitations, and Route-A disposition {#sec:discussion}

## Retention is not a common return clock

The strongest audited carriers retain the local translation, but they do so inside a separately labelled $G_q$-category. The point-order series retains the integer $r_q$, but [\[eq:period-collisions\]](#eq:period-collisions){reference-type="eqref" reference="eq:period-collisions"} shows that this integer is not a modulus identifier. The orbit-order, orbifold-compressed, and Morita quotient outputs have native period one. None of these facts supplies a common cross-$q$ observable equal to $q$ or $\log q$.

Substituting $t=q^{-s}$ imports the family label $q$. It is not generated by an iterate, fixed sector, groupoid automorphism, or source period. At $q=2$, no exponent normalization is needed because the source already has one cycle. That local coincidence still requires the external substitution to become a $q^{-s}$ factor, and its native support three also occurs at $q=4$.

Although the $q=2$ source already has one cycle and therefore yields the unit point-cardinality factor $(1-t^3)^{-1}$, support three is not an intrinsic modulus clock. Across the locked family no scalar reduction supplies a uniform source-support/unit-exponent construction, stronger coefficients remain in varying labelled categories, and composites obey the same hierarchy. The audited constructions therefore produce neither a common intrinsic modulus clock nor a prime selector.

## Limits of the audit

The comparison is limited to named finite constructions:

1.  the 2008 point-order rational Burnside zeta;

2.  the 2015 orbit-order integral Burnside zeta and its two additive orbifold reductions;

3.  the 2013 labelled $G$-permutation invariant;

4.  the 2018 enhanced carrier and enhanced fixed-sector orbifold zeta; and

5.  Morita- and $2$-isomorphism-invariant data of the finite quotient groupoid.

The note does not compare every representation-valued, weighted, derived, cohomological, analytic, or presentation-sensitive refinement. It does not extend the acting-group zeta of @Miles2017 to finite $G_q$, extend the finite-field quotient results of @Walton2018 to composite residue rings, or enter the analytic Ruelle/Fried programs cited in Section [2](#sec:prior){reference-type="ref" reference="sec:prior"}.

The general theorem assumes $C$ abelian. This is sufficient for the centralizer groups $G_q$ and makes the $BK$ inertia count equal to $|K|$. Nonabelian groups would require conjugacy-sensitive orbit types, centralizers, and naturality conventions. Nothing here claims that the same formulas transfer unchanged.

The exact audit is development-seen and finite. It is a falsification and implementation control, not statistical evidence and not a proof by exhaustion of all moduli. Its values were selected before the registered execution, inherited from the preceding audit, and include composites precisely to test non-prime specificity.

## Formal route decision

Within this frozen scope, the result supports $$\begin{gathered}
  \texttt{EQUIVARIANT\_RETENTION\_COMPRESSION\_TRADEOFF\_CERTIFIED},\\
  \texttt{A0\_FAIL\_MODULUS\_GLOBAL\_NON\_SPECIFIC},\qquad \texttt{ROUTE\_B\_NOT\_OPENED}.
\end{gathered}$$ The first token means family-nonuniform retention/compression, with the $q=2$ exception stated above; it does not mean pointwise mutual exclusion at every modulus. The A0 token records failure to obtain a common intrinsic modulus or prime clock, not failure of every local one-cycle factor. Route B remains unopened: no transfer, Fredholm, Hecke, quantization, Ruelle/Fried, prime--zero, or analytic claim follows from this finite hierarchy.

# Conclusion {#sec:conclusion}

Standard finite equivariant constructions do retain information erased by a coarse centralizer quotient, but they retain different information. Fixed points retain source order, fixed group-orbits retain a static orbit type, and full twisted or enhanced carriers retain a translation label modulo the action kernel. Orbifold and Morita quotient images compress the regular torsor to identity dynamics.

The exact cat-map specialization makes the cost visible. A labelled local carrier varies with $q$; an unlabelled quotient loses the clock; and the retained order collides across prime and composite moduli. The exceptional one-cycle factor at $q=2$ is real and explicit, but it has support three, which also occurs at $q=4$. The audited standard constructions therefore do not furnish a common modulus clock or prime selector.

This low-novelty boundary note closes only that named Route-A branch. Its value is the definition separation, scope correction, and exact provenance, not a claim to a new equivariant or stacky zeta. Stronger analytic or globally comparable mechanisms would require a new source lock and lie outside the present result.

# Divisor inversion and exact-period details {#app:inversion}

For completeness, let $F_k\in B(C)$ be a sequence with $F_k=\sum_{m\mid k}S_m$. Möbius inversion gives $$S_m=\sum_{d\mid m}\mu(m/d)F_d.
  \label{eq:mobius-inversion}$$ On a component $C/K$, $F_k=[C/K]$ precisely when $d_K\mid k$, and is zero otherwise. Equation [\[eq:mobius-inversion\]](#eq:mobius-inversion){reference-type="eqref" reference="eq:mobius-inversion"} therefore yields one exact point class $[C/K]$ at $d_K$. Summing the $n_K$ copies gives [\[eq:general-point-class\]](#eq:general-point-class){reference-type="eqref" reference="eq:general-point-class"}.

For fixed $C$-orbits, the class is $[C/K]$ at every iterate because translation stays inside the unique orbit. Möbius inversion then places $[C/K]$ only at support one. Summing components proves [\[eq:general-orbit-class\]](#eq:general-orbit-class){reference-type="eqref" reference="eq:general-orbit-class"}. This direct argument also shows why the point-order factor can be rational while the orbit-order factor here is integral.

# Twists, kernels, and groupoid naturality {#app:twists}

The stabilizer calculation in [\[eq:general-twisted-stabilizer\]](#eq:general-twisted-stabilizer){reference-type="eqref" reference="eq:general-twisted-stabilizer"} keeps track of the inverse convention. Under the locked left action $(j,c)\cdot xK=ca^jxK$, the base coset is fixed when $ca^j\in K$, so the positive generator is $(1,a^{-1})$. The enhanced carrier instead records the return transformation itself, namely $a$. These appearances of $a^{-1}$ and $a$ are compatible and must not be interchanged.

If $a,b\in C$, their stabilizer data agree on $C/K$ exactly when $aK=bK$. Agreement across all represented $K$ is therefore equivalent to $aN=bN$, with $N$ from [\[eq:action-kernel\]](#eq:action-kernel){reference-type="eqref" reference="eq:action-kernel"}. This proves exact recovery modulo the action kernel without asserting an intrinsically chosen generator after the ambient group label is forgotten.

For the action groupoid, let $F_a(x)=ax$. At every object $x$, choose the arrow $\eta_x\colon x\to ax$ labelled $a$. An arrow labelled $c$ gives the naturality square $$c\circ a=a\circ c,$$ which commutes because $C$ is abelian. Thus $\eta\colon\operatorname{Id}\Rightarrow F_a$ is a natural isomorphism. Any invariant depending only on the Morita class of the groupoid and the induced endomorphism up to $2$-isomorphism must assign this pair its identity value. Presentation-sensitive Burnside and permutation carriers are not covered by that conditional statement.

# Evidence and lifecycle bindings {#app:provenance}

Table [2](#tab:provenance){reference-type="ref" reference="tab:provenance"} lists the principal immutable authorities used by the manuscript. Publication assets entered only after the independent `ASSET_PASS`; manuscript-source and build hashes are bound separately in the accompanying pre-review integrity record.

::: {#tab:provenance}
  Authority                               Digest / disposition
  --------------------------------------- ---------------------------------------------------------------------------------------------------------------------------
  Authority                               Digest / disposition
  source lock v2                          `331a1f9004f83c7979daf8eacddd6844072c6b5b7068293c1276985cf6aaa87b`
  frozen upstream centralizer-audit PDF   `f685996c741c3e92d4eb18086f2a4e4d898ede10e8124a23991ada3579f8d378`; terminal complete
  independent source rereview             `2f75d6934e3d61bdc941ee6689102a1cb08a959270a7cd87965579f1ec5cc622`; `SOURCE_LOCK_PASS`
  frozen proof/formula package            `3d723fdb02c89f9b2f281da807bcd745c5991393d25e223f95d6673961c20948`; scalar quantifier superseded by the scope audit below
  immutable execution tree                `5ee1918a57fee56a2ca5a117c5749f614efbfd6baed96ae45480d6091a4741eb`
  raw exact result                        `bef8aa5d632ed11b1ca58a123bbfe967a5426e2049d862118a373e4c1dc005fe`
  independent result integrity            `c91737c8bf860bd559eebebe08420fc5d095800c47d132381f584e918e714a20`; `RESULT_PASS`
  post-run analyzer tree                  `423082f4675a1d41622bcb3d090a2c4c67d4732ff6dc32d0298505d90d5a78c3`
  independent analyzer review             `ba63afc8c88903f15ec6ac5d82f0cd65430710ca9c132b489a7cd4f70e7660a8`; `ANALYZER_PASS`
  dual-tree result manifest               `a0b409061c34eff0d68fdc326fe4ec6ff9295895444b857ee161fd77e417292c`; final read-only closure pass
  independent theorem-scope audit         `f7b365c9e6c8933cf3cbcaf3c96692cbacdaabcc84400bdc629f1d482cb243e4`; `PASS_WITH_SCOPE_CORRECTION`
  frozen publication asset tree           `95bb23519a427ef6a73a6a04b1aef6861aa4c5e4f6b844e7866bf9c43e52b28c`
  frozen figure manifest                  `e3a8d1d36ba8c4959b080a9661b242c40195ea08d27690fc8ee899b487cfd6dc`
  independent plan/figure review          `ebf1644dc03da4c1ccc03972b545688d595ed6da125de2ec831ffcf82e4e69cf`; `ASSET_PASS`

  : Core evidence bindings. Digests are SHA-256.
:::

The registered command ran once. The manuscript stage did not rerun the candidate, either test suite, the independent scientific verifier, or the post-run analyzer. It did not alter any file under `code/`, `experiments/`, or `results/`.

# Bibliographic verification boundary {#app:bibliography-boundary}

The bibliography uses primary or official metadata records frozen by the publication asset gate. The 2008, 2013, 2015, and 2018 records are direct construction authorities. Zegowitz supplies shortening/gluing terminology; Miles and Walton are scope boundaries only. Current cohomological, cyclic-nerve, Ruelle, trace, Fried, and survey records prevent unsupported generality or priority language.

The publication layer corrects one historical sidecar transcription. The DOI-authoritative record for Walton's paper is *Journal of Number Theory* **192** (2018), 386--405, DOI `10.1016/j.jnt.2018.03.023`. The frozen design sidecar records volume 189, pp. 202--223; it remains immutable as provenance. The corrected metadata are used only in this bibliography and change no source formula, theorem, result, novelty conclusion, or scientific scope.

# Availability and declarations {#availability-and-declarations .unnumbered}

#### Data and code availability.

The accompanying local research package contains the source lock, proof package, reviewed exact-arithmetic implementation, single registered result, independent reviews, theorem-scope correction, and strict result manifest. No external dataset is used by the mathematical claims or finite audit.

#### Ethics declaration.

The work involves no human participants, animals, personal data, or intervention study.

#### Author contributions.

Authorship and CRediT-role metadata are withheld in this anonymous pre-review copy and will be supplied for any non-anonymous release.

#### Conflict of interest.

Conflict-of-interest metadata are withheld with the anonymous author record and must be completed before external submission.

#### Funding acknowledgment.

Funding metadata are withheld during anonymous pre-review and must be completed before external submission.

#### AI-assisted workflow disclosure.

AI-assisted research and writing tools were used to organize source-locked materials, draft text, and support mechanical checks. Mathematical claims, citations, finite outputs, theorem-scope corrections, and lifecycle statements were separately bound to recorded source, code, result, and review gates. Responsibility for released content remains with the authors.
