---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--30-free-monoid-incidence-indistinguishability"
canonical_tex: "symbolic_dynamics/papers/30-free-monoid-incidence-indistinguishability/main.tex"
canonical_pdf: "symbolic_dynamics/papers/30-free-monoid-incidence-indistinguishability/main.pdf"
source_sha256: "04e07c1848c45808b774791ae86fb666ffe53453cc4517263689da8bdad7cb3b"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Free-Monoid Indistinguishability at the Incidence Boundary: A No-Go for Divisibility Cumulant Selectors

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/30-free-monoid-incidence-indistinguishability>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/30-free-monoid-incidence-indistinguishability/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/30-free-monoid-incidence-indistinguishability/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/30-free-monoid-incidence-indistinguishability/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/30-free-monoid-incidence-indistinguishability/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The local counterterm analysis of incidence-based symbolic dynamics leaves a possible nonlocal escape: a source-natural invariant built from several atoms, their joins, incidence Möbius values, or connected cumulants. We show that this escape is unavailable for the admitted multiplicative source. Unique factorization identifies positive-integer divisibility with the free commutative monoid of finitely supported valuation vectors. After compatible cutoffs and all roof, Gram, and compiler decorations are transported, this map is an isomorphism of decorated sources. Hence every isomorphism-natural local or nonlocal invariant, at any arity and with scalar or function-valued output, agrees on the integer source and its formal UFD clone. It is therefore impossible to be nonzero on the former while vanishing on every UFD control. The normalized Boolean-join Möbius weight fails by taking value one on both free sources; its partition-lattice connected cumulant fails oppositely by vanishing on the factorizing baseline. A stronger rank-three coherence filter is nonzero at three integer cutoffs and exactly zero on four finite non-UFD fixtures, yet its complete ledger is copied by free and polynomial-UFD clones. The final exact audit passes 28/28 tests and 1616/1616 independent checks. A pair-weighted mixed Gram series is holomorphic on $1-2\eta<\operatorname{Re}s<2\eta$ but remains a new functional. A separately constructed trace-class Gram matrix has an auxiliary ordinary Fredholm determinant; neither object upgrades the original chiral determinant, and both are cloned. The result closes the multiplicative chiral-incidence/counterterm branch. A successor must add independently motivated source-derived nonmultiplicative data.

  *Keywords:* symbolic dynamics; incidence algebra; free commutative monoid; Möbius inversion; cumulants; naturality; no-go theorem
author:
- Anonymous Authors
bibliography:
- references.bib
date: 'August 14, 2026'
title: |
  Free-Monoid Indistinguishability at the Incidence Boundary:\
  A No-Go for Divisibility Cumulant Selectors
```

## Markdown 正文

# Introduction {#sec:introduction}

The source studied here records multiplication as order: positive integers are ordered by divisibility, the bottom covers are the active atoms, and least common multiples are joins. Incidence inversion then supplies canonical interval coefficients in the sense of @Rota1964. Earlier steps in the construction showed that a quadratic mixed Gram phase is analytic but generic, and that local natural counterterms do not make it arithmetic-selective. A narrow question remained. Could a nonlocal statistic of many atoms, their joint interval, or the entire filtered source separate integer divisibility from non-arithmetic controls?

The most attractive candidate combines two familiar connectedness machines. A tuple of atoms is accepted when its subset joins form a Boolean interval; the top Möbius value normalizes the accepted tuple to one. One may then apply the partition-lattice cumulant transform of @Speed1983. This construction is label-blind, compatible with transport, and can inspect pairs or triples without calling a primality routine. Yet its two versions fail in opposite directions. The Boolean weight is one on both integer prime tuples and formal-generator tuples. The connected cumulant of the resulting factorizing moment is zero on the integer baseline itself.

Those failures are symptoms of a complete obstruction. The positive integers under multiplication form a free commutative monoid on their prime covers. The valuation vector $n\mapsto(v_p(n))_p$ preserves the bottom, covers, divisibility, lcms, and every interval. If the cutoff, roof, Gram, and compiled data visible to the construction are transported along this map, the integer source and a formal free-commutative/UFD clone are isomorphic as decorated sources. An isomorphism-natural invariant, no matter how global, must take equal values on them. Since the desired control statement quantifies over *every* UFD control, it includes this clone and contradicts baseline nonvanishing.

The paper makes four contributions. First, it states the admissible decorated source category and proves the free-monoid indistinguishability theorem without a locality, linearity, additivity, or fixed-arity hypothesis. Second, it gives the exact canonicity boundary for the Boolean weight and proves factorization cancellation for its connected cumulant. Third, it reports that a strengthened rank-three filter separates all four finite non-UFD fixtures, then shows why its exact free/UFD clone collision is decisive. It also embeds the pair weight into the inherited mixed Gram series, proves normal convergence on its natural strip, and assigns its marker ledger to a newly declared functional. A separate trace-class Gram matrix owns an auxiliary ordinary determinant without upgrading the chiral object. Fourth, the paper converts the obstruction into a branch closure rule: changing coefficients, cumulant conventions, tuple arity, cutoffs, or finite parts cannot reopen the same multiplicative source.

The scope is equally important. The theorem does not forbid an enrichment that adds independently motivated nonmultiplicative data. Addition-- multiplication interaction, congruence correspondences, or a genuine symbolic-dynamical transfer operator would define a new source object and require a new proof. The theorem also makes no statement about target zeros. Route B remains locked throughout.

# Admissible sources and the literature boundary {#sec:sources}

## The decorated source category

An object of $\mathcal C$ is $$X=(|X|,\le,\bot,\operatorname{At},\vee,\mu,(F_N)_N,w,G,\mathfrak A).
 \label{eq:decorated-source}$$ Here $(|X|,\le,\bot)$ is locally finite and pointed; $\operatorname{At}(X)=\{a:\bot\prec a\}$; $\vee$ records each defined finite join; $\mu$ is the interval Möbius function; $(F_N)_N$ is a compatible ambient active-atom filtration; and $w,G,\mathfrak A$ are the roof, Gram, and compiled analytic decorations admitted by the construction. An isomorphism preserves and reflects all displayed data.

Including $\mu$ explicitly fixes what an invariant may inspect, although it is redundant: an interval isomorphism preserves the incidence recurrence and therefore its Möbius function. A numerical roof mark is transported coefficient data. It may weight every object, but it may not be recomputed from printed names after relabeling in order to choose atoms. The active predicate remains the source cover relation.

Let $I$ take values in any category with pullback along source isomorphisms. It is isomorphism-natural when $$I(X)=\phi^*I(Y)
 \quad\text{for every}\quad \phi:X\xrightarrow{\sim}Y.
 \label{eq:naturality}$$ The output may be a scalar, tuple kernel, formal marker ledger, holomorphic function, operator coefficient, trace, determinant coefficient, or newly declared same-object functional.

Definition [\[eq:naturality\]](#eq:naturality){reference-type="ref" reference="eq:naturality"} does not impose locality. An invariant may inspect the complete filtered object, use tuples of arbitrary finite arity, or apply nonlinear and connected transforms. This breadth is what makes the main theorem stronger than a classification of one formula.

## Incidence, cumulant, and monoid precedents

Möbius inversion on locally finite posets is classical [@Rota1964]. Categorical functoriality was developed by @ContentLemayLeroux1980; modern decomposition spaces further organize incidence coalgebras and their CULF transport [@GalvezKockTonks2018I; @GalvezKockTonks2018III]. These results license transport as a structural requirement. They do not single out one member of an isomorphism class.

Connected organization is equally cross-family. Species and formal-series operations provide a broad transport framework [@Joyal1981]; joint cumulants are Möbius transforms on partition lattices [@Speed1983]; and incidence Hopf algebras supply primitive and antipode structures for families including graphs, matroids, and distributive lattices [@Schmitt1994]. Accordingly, neither "connected" nor "primitive" is by itself an arithmetic selector.

The monoid literature comes still closer. Arithmetical semigroups are explicitly treated as free commutative semigroups on prime generators, with polynomial, ideal, and module examples beyond the positive integers [@KnopfmacherEtAl1992]. Graded Möbius transforms occur in trace monoids [@Abbes2015], and @AbbesEtAl2019 define a transform using subsets of generators whose left lcm exists in a broad Artin--Tits setting. Thus the subset--join--Möbius architecture is established generic monoid machinery. The defensible contribution below is not that architecture but the scoped impossibility theorem for the full decorated stack.

## Why graph and dynamical determinants do not transfer

Graph zeta theory connects nonbacktracking cycles to determinant formulas [@Bass1992]; its connected-word organization also has direct combinatorial proofs [@FoataZeilberger1999]. Symbolic-dynamical zeta functions for expanding maps and Anosov flows start from periodic dynamics and transfer information [@Ruelle1976]. A recent regularized determinant formula similarly starts from a flow generator, reduced leafwise cohomology, and a dynamical Lefschetz formula [@AlvarezKimMorishita2024].

These are adjacent machines, not ownership precedents for the present mixed series. The divisor lattice has no native inverse-edge rule, periodic-orbit system, flow generator, or cohomological complex. Importing a graph or dynamical determinant conclusion without constructing that extra object would cross the information boundary. The closest literature collision is therefore subset-lcm Möbius machinery in broad monoids, and it reinforces rather than evades free-monoid indistinguishability.

The underlying primary-source search is bounded. It supports the statement that no exact indexed construction of the weighted selector was found in the declared neighborhoods, not a universal assertion that no related manuscript exists. The no-go theorem below relies only on an explicit isomorphism.

# Boolean and connected candidates {#sec:candidates}

Let $A=(a_1,\ldots,a_r)$ be a tuple of distinct atoms, initially with $r\in\{2,3\}$. Suppose its join $j(A)=\bigvee_i a_i$ exists. The subset-join map is $$\beta_A:2^{[r]}\longrightarrow[\bot,j(A)],
 \qquad S\longmapsto\bigvee_{i\in S}a_i,
 \label{eq:beta}$$ with empty join $\bot$.

$$K^{\mathrm B}_r(A)
 :=\mathbf 1_{\{\beta_A\text{ is a pointed order isomorphism}\}}
   (-1)^r\mu_X(\bot,j(A)).
 \label{eq:boolean-weight}$$ If the join is undefined, the value is zero.

On a Boolean lattice $B_r$, $\mu(\hat0,\hat1)=(-1)^r$, so every accepted tuple has $K^{\mathrm B}_r=1$.

[\[prop:boolean-natural\]]{#prop:boolean-natural label="prop:boolean-natural"} The weight [\[eq:boolean-weight\]](#eq:boolean-weight){reference-type="eqref" reference="eq:boolean-weight"} is invariant under admissible pointed isomorphisms. Its value on an old tuple is unchanged under a compatible active-cutoff enlargement evaluated in the same ambient source.

An isomorphism carries atoms to atoms, preserves every subset join, and restricts to an isomorphism of the two pointed join intervals. It therefore preserves the Boolean certificate and the top Möbius value. An active cutoff changes only which already compiled atoms enter a finite sum; it does not replace the ambient interval of an old tuple.

[\[prop:conditional-unique\]]{#prop:conditional-unique label="prop:conditional-unique"} Equation [\[eq:boolean-weight\]](#eq:boolean-weight){reference-type="eqref" reference="eq:boolean-weight"} is the unique $\{0,1\}$-valued tuple weight supported exactly on Boolean tuple-join intervals and normalized to one there. Isomorphism naturality alone does not select it.

The support and normalization axioms fix both possible values. The Möbius factor realizes the normalization because the Boolean top value is $(-1)^r$. Conversely, let $\mathfrak I_r$ be the set of pointed isomorphism classes of tuple-join intervals. Every function $f:\mathfrak I_r\to\mathbb C$ yields the natural weight $f([\bot,j(A)]_{\rm pt})$. Global filtered-source data permit still more choices.

The proposition separates a useful exact formula from an overclaim. "Natural" does not mean "canonical"; Boolean support, range, and unit normalization are scheme axioms.

## The connected alternative

Fix a moment $m(A_S)$ for each nonempty subset. Its partition-lattice connected transform is $$\kappa_r(A)=
 \sum_{\pi\in\Pi_r}(-1)^{|\pi|-1}(|\pi|-1)!
 \prod_{B\in\pi}m(A_B).
 \label{eq:cumulant}$$ The coefficients in [\[eq:cumulant\]](#eq:cumulant){reference-type="eqref" reference="eq:cumulant"} are classical [@Speed1983]; the source does not thereby choose $m$.

[\[lem:factorization-cancellation\]]{#lem:factorization-cancellation label="lem:factorization-cancellation"} If $m(A_S)=\prod_{i\in S}u_i$ for every nonempty $S$, then $\kappa_r(A)=0$ for every $r\ge2$.

Every partition product in [\[eq:cumulant\]](#eq:cumulant){reference-type="eqref" reference="eq:cumulant"} equals $\prod_i u_i$. The remaining coefficient is $$c_r=\sum_{\pi\in\Pi_r}(-1)^{|\pi|-1}(|\pi|-1)!.$$ Its exponential generating function is $\sum_{r\ge1}c_r z^r/r!=\log(e^z)=z$, so $c_r=0$ for $r\ge2$.

For the Boolean moment on a free commutative source, every nonempty subset moment is one. Thus $$\kappa_2=1-1=0,
 \qquad
 \kappa_3=1-1-1-1+2=0.
 \label{eq:low-cumulants}$$ The connected transform detects failure of multiplicative factorization; it removes the desired free baseline signal.

## The frozen five-predicate refinement

The exact suite strengthened the Boolean support before execution. For a pair or triple $A$, define $\chi_r(A)=1$ precisely when all five conditions hold:

1.  the join $j(A)$ is unique;

2.  $\beta_A$ identifies its pointed interval with $B_r$;

3.  $\mu(\bot,j(A))=(-1)^r$;

4.  the roof is multiplicative, $w(j(A))=\prod_{a\in A}w(a)$; and

5.  iterated binary joins own $j(A)$ associatively.

All five predicates are source-resident and natural under the admitted decorated isomorphisms. The 31 nonempty predicate masks were enumerated as a robustness audit; none was selected after observing controls.

The rank-three connected contraction used by that suite is $$\Theta_3
 =2\sum_{a<b<c}\chi_3(a,b,c)
 \frac{G_{ab}G_{bc}G_{ca}}{w(a)w(b)w(c)}.
 \label{eq:theta3}$$ It is important not to conflate $\Theta_3$ with the partition-lattice cumulant [\[eq:cumulant\]](#eq:cumulant){reference-type="eqref" reference="eq:cumulant"}. It is a separately filtered triangle contraction, not the full $\operatorname{Tr}\mathcal B_s^6$ and not a chiral determinant coefficient. It can be nonzero on a factorizing baseline.

The final exact audit finds $\chi_3$ and $\Theta_3$ nonzero at all three integer cutoffs and exactly zero on the four finite non-UFD fixtures. This is a genuine finite-fixture GO. It is not arithmetic selectivity: every pair, triple, coefficient, and predicate mask is reproduced by the transported free and polynomial-UFD clones.

# Free-monoid indistinguishability {#sec:clone-theorem}

Let $$M_{\mathbb Z}=(\mathbb N_{>0},\mid,1,\operatorname{lcm})
 \label{eq:integer-monoid}$$ and let $P=\operatorname{At}(M_{\mathbb Z})$, the covers of $1$. Write the formal free commutative monoid additively as $$F(P)=\bigoplus_{p\in P}\mathbb Ne_p,
 \label{eq:formal-monoid}$$ with coordinatewise order, zero bottom, and coordinatewise maximum as join. Define $$\Phi(n)=(v_p(n))_{p\in P}.
 \label{eq:valuation-map}$$ Equation [\[eq:valuation-map\]](#eq:valuation-map){reference-type="eqref" reference="eq:valuation-map"} is used to prove an isomorphism; it is not an operation made available to a candidate kernel.

Transport every admitted decoration: $$F'_N=\Phi(F_N),\qquad
 w'(\Phi(n))=w(n),\qquad
 G'_{\Phi(m),\Phi(n)}=G_{m,n},
 \label{eq:transport}$$ and apply the same index transport to each compiled tensor or operator coefficient.

[\[thm:clone\]]{#thm:clone label="thm:clone"} The valuation map $\Phi$ is an isomorphism in $\mathcal C$ from the decorated integer-divisibility source to the transported formal free-commutative/UFD source. Consequently, every isomorphism-natural invariant $I$ of the admitted data satisfies $$I(M_{\mathbb Z})=\Phi^*I(F(P)).
 \label{eq:invariant-equality}$$ The conclusion holds for local or nonlocal $I$, for every arity, and for scalar-, kernel-, ledger-, operator-coefficient-, or function-valued output.

Unique factorization makes $\Phi$ a bijection between positive integers and finitely supported exponent vectors. Moreover, $$m\mid n
 \quad\Longleftrightarrow\quad
 v_p(m)\le v_p(n)\quad\text{for every }p,
 \label{eq:order-transport}$$ so it preserves and reflects the order and sends $1$ to the zero vector. Covers of $1$ go exactly to coordinate unit vectors. For every finite family, $$v_p(\operatorname{lcm}(n_1,\ldots,n_k))=\max_i v_p(n_i),
 \label{eq:join-transport}$$ so all finite joins and all pointed intervals are preserved. Interval Möbius functions therefore agree. Equation [\[eq:transport\]](#eq:transport){reference-type="eqref" reference="eq:transport"} makes the cutoff and analytic decorations commute with the map by construction. Thus $\Phi$ is an isomorphism of the complete displayed object. Naturality of $I$ at this isomorphism gives [\[eq:invariant-equality\]](#eq:invariant-equality){reference-type="eqref" reference="eq:invariant-equality"}. No step restricts the locality, arity, or algebraic form of $I$.

[\[cor:selectivity\]]{#cor:selectivity label="cor:selectivity"} There is no admissible natural invariant $I$ such that $$I(M_{\mathbb Z})\ne0
 \quad\text{and}\quad
 I(U)=0\quad\text{for every free-commutative/UFD control }U.
 \label{eq:selectivity-gate}$$

The universal quantifier in [\[eq:selectivity-gate\]](#eq:selectivity-gate){reference-type="eqref" reference="eq:selectivity-gate"} includes the transported clone $F(P)$. The second requirement sets its value to zero, while [\[thm:clone\]](#thm:clone){reference-type="ref" reference="thm:clone"} identifies that value with the nonzero baseline value.

The clone is not a tuned control. Comparing an object with a transported copy is the minimal coherence test for an invariant advertised as natural. If a control policy forbids transported coefficient data, it no longer quantifies over every decorated UFD object. That is a weaker and different claim.

# Selectivity no-go and its exact boundary {#sec:boundary}

The force of [\[thm:clone\]](#thm:clone){reference-type="ref" reference="thm:clone"} comes from its information boundary, not from the particular Boolean formula. The following constructions remain inside that boundary and are therefore clone-invariant:

-   pair, triple, and arbitrary finite-arity join or lcm coherence;

-   interval-local and complete-source incidence Möbius transforms;

-   incidence-Hopf primitives, antipodes, and connected/logarithmic organization natural in the source;

-   partition-lattice cumulants after any source-natural moment has been fixed;

-   kernels that inspect the complete filtered tower rather than one interval;

-   the transported roof, metric, Gram, and compiled-operator stack; and

-   honest traces, determinant coefficients, or new functionals whenever they are constructed naturally from those same data.

Thus the theorem resolves the loophole left by a pair-local analysis. A hard-coded indicator of the complete integer-tower isomorphism class is also covered: it takes value one on the isomorphic formal clone. Declaring that formal presentation to be "non-arithmetic" does not change the naturality equation.

[\[thm:formula-closure\]]{#thm:formula-closure label="thm:formula-closure"} Within the category $\mathcal C$, no change of a natural join/Möbius kernel, tuple arity, moment or cumulant convention, active-cutoff exhaustion, finite-part convention, or same-object contraction can satisfy exact integer-nonzero/every-UFD-zero selectivity.

Each change still defines an invariant natural in the same decorated object. Apply [\[thm:clone\]](#thm:clone){reference-type="ref" reference="thm:clone"} to the integer source and its transported UFD clone, then repeat the contradiction in [\[cor:selectivity\]](#cor:selectivity){reference-type="ref" reference="cor:selectivity"}.

Y Y Covered by the theorem & Requires a new source object or weaker claim\
Any natural invariant of pointed divisibility, joins, intervals, Möbius values, cutoffs, roof marks, Gram data, and admitted compiled coefficients & A source-derived nonmultiplicative operation proved not to transport along the valuation map\
Local, nonlocal, nonlinear, complete-tower, and arbitrary finite-arity constructions & Addition--multiplication interaction, congruence correspondences, or a genuine transfer operator with independent motivation\
Any universally quantified class containing the transported formal UFD clone & Excluding the clone, thereby weakening "every UFD control"\
Transported labels and coefficient marks & Nontransportable printed-name or primality oracles, which violate the information boundary\
Exact baseline/control selectivity & Abandoning exact selectivity or changing the target question\

The most promising legitimate escape is therefore not another incidence coefficient. It is an independently defined operation relating two kinds of source structure, followed by a proof that the formal UFD clone cannot carry the same decoration by transport. Such an operation would require a new preregistration, control suite, analytic argument, and marker-ownership audit. It is reserved for a successor rather than inferred here.

# Analytic embedding and functional ownership {#sec:mixed-functional}

The no-go does not invalidate every analytic object built from the failed weight. It determines what that object can and cannot mean. For distinct active atoms with inherited numerical roof marks $p,q$, take $$G_{pq}=\frac{1}{(p^{2\eta}+1)(q^{2\eta}+1)},
 \qquad \eta>0.
 \label{eq:mixed-gram}$$ For a bounded pair kernel $|K_2(p,q)|\le1$, define $$\mathcal M_K(s)=2\sum_{p<q}K_2(p,q)G_{pq}
 \left(p^{-s}q^{s-1}+q^{-s}p^{s-1}\right).
 \label{eq:mixed-functional}$$ The Boolean embedding uses $K_2=K^{\mathrm B}_2$.

[\[prop:holomorphy\]]{#prop:holomorphy label="prop:holomorphy"} The series [\[eq:mixed-functional\]](#eq:mixed-functional){reference-type="eqref" reference="eq:mixed-functional"} converges normally on compact subsets of $$1-2\eta<\operatorname{Re}s<2\eta
 \label{eq:holomorphy-strip}$$ and is holomorphic there.

Put $\sigma=\operatorname{Re}s$. Equation [\[eq:mixed-gram\]](#eq:mixed-gram){reference-type="eqref" reference="eq:mixed-gram"} gives $G_{pq}\le p^{-2\eta}q^{-2\eta}$, so the two absolute summands are bounded by $$p^{-(2\eta+\sigma)}q^{-(2\eta+1-\sigma)},
 \qquad
 q^{-(2\eta+\sigma)}p^{-(2\eta+1-\sigma)}.
 \label{eq:product-majorant}$$ Both one-variable exponents exceed one precisely in [\[eq:holomorphy-strip\]](#eq:holomorphy-strip){reference-type="eqref" reference="eq:holomorphy-strip"}. Replacing the atom sums by sums over all integers gives a product of convergent zeta tails. On a compact substrip the exponents have a uniform margin above one. The Weierstrass $M$-test gives normal convergence, and termwise holomorphy proves the result.

For the inherited value $\eta=2$, the strip is $-3<\operatorname{Re}s<4$, so the critical line lies in its interior.

## Exact marker ledger

At $s=\tfrac12+it$, the two monomials in [\[eq:mixed-functional\]](#eq:mixed-functional){reference-type="eqref" reference="eq:mixed-functional"} are conjugates: $$p^{-s}q^{s-1}=\frac{e^{it\log(q/p)}}{\sqrt{pq}},
 \qquad
 q^{-s}p^{s-1}=\frac{e^{-it\log(q/p)}}{\sqrt{pq}}.
 \label{eq:conjugate-monomials}$$ Hence $$\mathcal M_K\!\left(\tfrac12+it\right)
 =4\sum_{p<q}\frac{K_2(p,q)G_{pq}}{\sqrt{pq}}
 \cos\!\left(t\log\frac qp\right).
 \label{eq:critical-mixed}$$ The formal marker is $q/p\leftrightarrow\log(q/p)$, and its exact squared coefficient is $$\frac{16K_2(p,q)^2G_{pq}^2}{pq}.
 \label{eq:squared-marker}$$ No cosine is sampled and no external ordinate is used. For $K_2=K^{\mathrm B}_2$, all terms and markers transport to the formal UFD clone, so marker ownership is rigorous while arithmetic selectivity is false.

## What object owns the series?

Equation [\[eq:mixed-functional\]](#eq:mixed-functional){reference-type="eqref" reference="eq:mixed-functional"} defines a *new source-weighted mixed functional*. The convergence proof constructs a scalar holomorphic series; it does not construct a trace-class operator whose ordinary trace is that series. It supplies no reference pair or trace-class relative hypothesis for a relative determinant.

Nor is $\mathcal M_K$ a modified Fredholm determinant. Regularized Fredholm determinants have a specified operator and power-subtraction law [@BritzEtAl2021]. The inherited honest $\det_{3}(I-z\mathcal B_s)$ removes the first two logarithmic powers, including the quadratic mixed power in full. It therefore cannot own a separately retained quadratic series. A2 remains owned by that inherited $\det_{3}$; $\mathcal M_K$ receives no new determinant gate.

## A separate auxiliary determinant

The exact suite does construct a different operator. On the atom Hilbert space, define the real zero-diagonal matrix $$H_{pq}=\chi_2(p,q)\frac{G_{pq}}{\sqrt{pq}}\quad(p\ne q),
 \qquad H_{pp}=0.
 \label{eq:auxiliary-H}$$ For $\eta=2$, $|H_{pq}|\le p^{-9/2}q^{-9/2}$. Hence $\sum_{p,q}|H_{pq}|<\infty$. The matrix-unit nuclear decomposition makes $H$ trace class, so $$D_H(z)=\det(I+zH)
 \label{eq:auxiliary-det}$$ is an honest ordinary Fredholm determinant, entire in $z$. Its first two nontrivial finite characteristic coefficients are $$D_H(z)=-\sum_{p<q}H_{pq}^2,
 \qquad
 [z^3]D_H(z)=2\sum_{p<q<r}H_{pq}H_{qr}H_{pr}.
 \label{eq:auxiliary-coefficients}$$

This is a genuine analytic gain with narrow ownership. A phase-decorated finite cutoff is diagonally conjugate to $H$, so its characteristic cycles cancel the $t$-phase. The auxiliary determinant has no spectral motion, and its complete coefficient ledger is cloned by the free/UFD controls. Moreover, the separately filtered $\Theta_3$ in [\[eq:theta3\]](#eq:theta3){reference-type="eqref" reference="eq:theta3"} uses the stronger triple predicate rather than merely the three pair edges; it is not in general the cubic coefficient in [\[eq:auxiliary-coefficients\]](#eq:auxiliary-coefficients){reference-type="eqref" reference="eq:auxiliary-coefficients"}. Neither $D_H$ nor $\Theta_3$ is the original chiral transfer determinant.

Exponentiating $\mathcal M_K$, a finite part of it, or a chosen cubic contraction would define another scheme functional, not repair determinant ownership. The rank-three weight has no canonical slot in the two-point Gram contraction; choosing a trilinear contraction is additional decoration. Even after such a choice, [\[thm:clone\]](#thm:clone){reference-type="ref" reference="thm:clone"} transports its value to the clone.

# Exact control logic and prototype boundary {#sec:exact-audit}

The central result is theorem-driven. A finite program can catch an incorrect interval test, cutoff convention, or transported index; it cannot establish [\[thm:clone\]](#thm:clone){reference-type="ref" reference="thm:clone"}, which quantifies over the infinite source and all natural invariants. We therefore separate exact mathematical predictions from implementation evidence.

L0.35L0.13L0.17Y Source & Atoms & qualified pairs & qualified triples\
Integer divisibility, cutoff 12 & 5 & 10 & 10\
Integer divisibility, cutoff 18 & 7 & 21 & 35\
Integer divisibility, cutoff 30 & 10 & 45 & 120\
Mutated cover, object 6 promoted & 8 & 3 & 0\
Composite-only inventory & 3 & 0 & 0\
Seeded generic DAG (29031) & 4 & 0 & 0\
Seeded random inventory (29032) & 5 & 0 & 0\
Transported free-commutative clone, cutoff 30 & 10 & 45 & 120\

The frozen executable design discovers atoms as covers of the bottom, computes joins and Möbius values from the order, and stores oscillations as formal ratio/amplitude data. It prohibits a primality call and preserves old tuple values under compatible ambient active-cutoff growth. A transported-clone check compares the pointed order, joins, roof marks, tuple weights, and mixed marker ledger under the finite restriction of $\Phi$.

The three surviving mutated-cover pairs are $$(2,5),\qquad(2,7),\qquad(3,5).
 \label{eq:mutated-survivors}$$ Their generated Boolean intervals do not meet the promoted-six defect. In particular, $[1,10]=\{1,2,5,10\}\cong B_2$, $\mu(1,10)=1$, and $10=2\cdot5$. Every one of the 31 nonempty predicate masks retains at least one such pair, so no pair mask separates the baseline from all four finite fixtures. By contrast, 28 masks separate baseline triples from those fixtures. The full $\chi_3$ gives a clean finite-fixture separator, but every mask is copied by the free and polynomial-UFD clones.

The canonical row census is 241 baseline subsets, 118 finite-control subsets, 45 free/UFD rows, 186 predicate-mask rows, and 165 marker rows. Canonical relabelings agree, old rows are preserved along the $12\to18\to30$ active cutoffs, and all baseline and clone pair/triple ledgers agree. The independent evaluator passes 1616/1616 checks and the regression suite passes 28/28 tests. Two isolated fresh runs generate the same 17 artifacts byte for byte, with aggregate SHA-256 `b2ea8f6c6803ef5a0a01999452f7e68ed099ccb04f2e24c8592b97b5e1fef316`. The canonical 31-entry authority ledger and all certificate hashes are recorded in the manuscript source lock.

This evidence boundary prevents two common overstatements. Passing finite relabeling and prefix tests does not prove naturality on all sources, and a finite collision table does not prove a universal no-go. Conversely, the single isomorphic UFD clone is sufficient to refute the universally quantified selectivity specification, even if every other finite control were zero.

# Route decision and branch closure {#sec:route}

SD-C32 is a mathematical GO as a negative theorem and a STOP as an arithmetic selector. The result strengthens the previous local obstruction to the entire admissible natural-invariant class, including nonlocal filtered-tower constructions.

L0.20L0.19Y Gate & Status & Reason\
A0 structural arithmetic relation & A0: structural arithmetic relation & Divisibility, bottom covers, joins, and incidence Möbius data are source-derived, although they are free-monoid generic.\
A1 fixed self-adjoint operator & A1: fail & The analytic construction remains a parameter-dependent family rather than one fixed operator carrying the parameter as spectrum.\
A2 analytic determinant & A2: analytic determinant & The inherited $\det_{3}$ remains honest on its established Schatten strip, and the trace-class $H$ owns a separate auxiliary determinant. The new $\mathcal M_K$ is not a determinant and earns no separate gate.\
A3 target equivalence & A3: fail & No equivalence to an external target-zero condition is stated or tested.\
A4 arithmetic selectivity & A4: fail & The integer source and a universally quantified formal UFD control are isomorphic after transport, so every natural invariant agrees.\

The resulting tuple is

(A0\_STRUCTURAL\_ARITHMETIC\_RELATION, A1\_FAIL,\
A2\_ANALYTIC\_DETERMINANT, A3\_FAIL, A4\_FAIL).

Thus `ROUTE_A_REJECTED`. Route B is locked and has not been opened.

## Closed moves

The theorem supports `CLOSE_CHIRAL_INCIDENCE_COUNTERTERM_BRANCH`. The following moves do not create a successor:

-   changing coefficients or normalizations of a natural interval kernel;

-   moving from pairs or triples to higher finite arity;

-   selecting another moment basis, cumulant, incidence-Hopf logarithm, or primitive extraction;

-   changing the compatible cutoff order or a finite-part convention;

-   inventing a cubic or higher contraction on the same transported data; or

-   hard-coding the complete integer-tower isomorphism class.

Every item remains a natural function of an object isomorphic to its formal UFD clone.

## Paper31 obligation

A successor is permitted only after it defines an independently motivated, source-derived nonmultiplicative operation and proves that this new datum is not transported by $\Phi$. It must then rebuild naturality, compatible cutoffs, summability, holomorphy, and marker ownership, and rerun the mutated-cover, composite-only, generic-DAG, random-inventory, and expanded free/UFD controls. Addition--multiplication interaction, congruence correspondences, and a genuine transfer operator are examples of new data, not preapproved solutions.

No change of coefficients, cumulants, arity, or regularization within the old multiplicative object satisfies this obligation. Route B remains locked unless an entirely separate theorem first meets its invocation gate.

# Conclusion {#sec:conclusion}

The nonlocal incidence loophole closes for a structural reason. Unique factorization identifies positive-integer divisibility with a formal free commutative monoid, and transporting the admitted cutoff, roof, Gram, and compiled data turns that identification into an isomorphism of decorated sources. Any invariant natural in those data, whether interval-local or a nonlinear function of the complete filtered tower, takes the same value on the integer source and the formal UFD clone. Exact nonzero-integer/ zero-every-UFD selectivity is therefore inconsistent.

The frozen candidates expose both sides of the contradiction. The normalized Boolean-join Möbius weight is one on every free squarefree tuple interval and survives on the clone. Its connected cumulant cancels a factorizing moment and is zero on the baseline. Naturality alone does not select the Boolean support or moment scheme.

The pair weight still defines an analytically legitimate mixed functional. It is holomorphic on $1-2\eta<\operatorname{Re}s<2\eta$ and carries exact ratio-frequency markers, but its clone ledger is identical. The functional is neither an ordinary trace nor a modified Fredholm determinant. A separately constructed trace-class matrix owns an auxiliary ordinary determinant, while the inherited $\det_{3}$ remains the chiral analytic object. Neither determinant supplies phase motion or arithmetic selectivity.

The endpoint is a no-go theorem and a stop rule. The multiplicative incidence and counterterm branch is closed. Paper31 may pose a new question only by adding independently justified source-derived nonmultiplicative data and proving that the resulting object breaks the transported-clone isomorphism. Reweighting the old incidence source does not do so.

# Proof details {#app:proofs}

## Boolean interval recurrence

For $S\subseteq[r]$, the interval $[\varnothing,S]$ in $2^{[r]}$ is again Boolean. The incidence recurrence $$\sum_{T\subseteq S}\mu(\varnothing,T)=\delta_{S,\varnothing}
 \label{eq:boolean-recurrence}$$ is solved by $\mu(\varnothing,T)=(-1)^{|T|}$, since $\sum_{k=0}^{|S|}\binom{|S|}{k}(-1)^k=(1-1)^{|S|}$. This proves the sign used in [\[eq:boolean-weight\]](#eq:boolean-weight){reference-type="eqref" reference="eq:boolean-weight"} without importing a numerical label or factorization oracle.

If $a_1,\ldots,a_r$ are distinct prime covers in $M_{\mathbb Z}$, their full join is $\prod_i a_i$. Every divisor of that squarefree product is a unique subset product, so $\beta_A$ is a pointed order isomorphism. If the atoms are coordinate unit vectors in $F(P)$, the same proof replaces subset products by $0/1$ exponent vectors.

## Cumulant coefficient identity

Grouping the partitions in [\[lem:factorization-cancellation\]](#lem:factorization-cancellation){reference-type="ref" reference="lem:factorization-cancellation"} by their number of blocks gives $$c_r=\sum_{k=1}^r S(r,k)(-1)^{k-1}(k-1)!,
 \label{eq:stirling-cumulant}$$ where $S(r,k)$ is a Stirling number of the second kind. Using $\sum_{r\ge k}S(r,k)z^r/r!=(e^z-1)^k/k!$, one obtains $$\begin{aligned}
 \sum_{r\ge1}c_r\frac{z^r}{r!}
 &=\sum_{k\ge1}\frac{(-1)^{k-1}}{k}(e^z-1)^k\\
 &=\log(1+e^z-1)=z.
 \label{eq:cumulant-egf}\end{aligned}$$ Thus $c_1=1$ and all higher coefficients vanish. The argument applies at every arity, although the executable candidate froze only ranks two and three.

## Intervals and Möbius values under valuation

For $m\mid n$, valuation restricts to $$_{\mid}\ \xrightarrow{\sim}\
 [\Phi(m),\Phi(n)]_{\le}.
 \label{eq:interval-isomorphism}$$ Indeed, $m\mid d\mid n$ is equivalent coordinatewise to $\Phi(m)\le\Phi(d)\le\Phi(n)$, and unique factorization supplies the inverse. Applying the incidence recurrence on the two isomorphic intervals gives $$\mu_{M_{\mathbb Z}}(m,n)
 =\mu_{F(P)}(\Phi(m),\Phi(n)).
 \label{eq:mobius-transport}$$ All constructions made from interval convolution therefore transport.

## Decoration transport and global invariants

Let $T_X$ be any source-resident $k$-index tensor. Define its clone by $$T_{F(P)}(\Phi(x_1),\ldots,\Phi(x_k))
 :=T_{M_{\mathbb Z}}(x_1,\ldots,x_k).
 \label{eq:tensor-transport}$$ The same rule transports roof marks, Gram kernels, compiled coefficient arrays, and compatible active cutoffs. A global invariant may aggregate over all entries and all cutoff levels; equation [\[eq:tensor-transport\]](#eq:tensor-transport){reference-type="eqref" reference="eq:tensor-transport"} still supplies an isomorphism of the complete filtered decorated object. The proof of [\[thm:clone\]](#thm:clone){reference-type="ref" reference="thm:clone"} therefore does not reduce a nonlocal construction to a local one.

## Uniform majorant on compact substrips

Let $K$ be a compact subset of $1-2\eta<\operatorname{Re}s<2\eta$. There is $\varepsilon>0$ such that for all $s\in K$, $$2\eta+\operatorname{Re}s\ge1+\varepsilon,
 \qquad
 2\eta+1-\operatorname{Re}s\ge1+\varepsilon.
 \label{eq:uniform-exponents}$$ Consequently the absolute value of [\[eq:mixed-functional\]](#eq:mixed-functional){reference-type="eqref" reference="eq:mixed-functional"} is bounded, uniformly on $K$, by a constant multiple of $$\left(\sum_{n\ge2}n^{-1-\varepsilon}\right)^2.
 \label{eq:uniform-majorant}$$ This proves normal convergence independently of prime-density estimates. The result is a statement about the new scalar functional only; it supplies no Schatten or trace-class classification of an unconstructed operator.

## Why exponentiation does not upgrade the object

Given any holomorphic $h(s)$, the function $\exp(h(s))$ is holomorphic and zero-free. This elementary fact does not make it a Fredholm determinant. A determinant requires an operator family and the corresponding trace-ideal or relative hypotheses. Similarly, multiplying the inherited $\det_{3}(I-z\mathcal B_s)$ by $\exp[-z^2\mathcal M_K(s)/2]$ would declare a new scheme-dependent product. It would not restore the quadratic term to the logarithm of $\det_{3}$ or convert $\mathcal M_K$ into an ordinary trace.

# Scope, reproducibility, and declarations {#app:scope}

## Claim boundary

The no-go covers every finite-arity isomorphism-natural invariant, local or nonlocal, of the decorated multiplicative source in [\[eq:decorated-source\]](#eq:decorated-source){reference-type="eqref" reference="eq:decorated-source"}. It excludes a new source carrying independently motivated nonmultiplicative data proved not to transport along $\Phi$. Printed numeric names, external primality or factorization calls, and target-zero data are not source data.

The function $\mathcal M_K$ is a newly declared mixed scalar functional, neither an ordinary trace nor a relative or modified Fredholm determinant (including $\det_2$ and $\det_{3}$). Its ratio-frequency ledger is not identified with an external zero set. Route B is locked; no target-zero locations, counts, statistics, or fitting losses are used.

## Data and code availability

The paper proves a mathematical theorem and uses no empirical or personal dataset. A finite exact prototype audits only the frozen candidate, interval implementation, compatible cutoffs, and transported clone. It passes 28/28 tests and 1616/1616 independent checks; two fresh runs reproduce 17 artifacts byte for byte. The source lock identifies the canonical 31-entry ledger and certificate hashes. The theorem does not depend on finite execution.

## Ethics statement

Ethics approval and informed consent are not applicable because the work is mathematical and uses no human participants, animals, or private records.

## Author contributions

The anonymous authors are responsible for conceptualization, formal analysis, methodology, validation, visualization, and writing. All authors approved the manuscript and accept responsibility for its claims.

## Funding and competing interests

No external funding is declared. The authors declare no competing interests.

## AI-use disclosure

AI-assisted tools supported search strategy, proof organization, exact-artifact integration, drafting, and formatting. Mathematical claims, citations, functional classifications, and scope boundaries were checked against the frozen research and primary-source artifacts. The authors take responsibility for the manuscript's accuracy and integrity.

#### Review policy.

At the governing request, no manuscript review loop was run. Formula, source, citation, route, compilation, font, metadata, control-byte, and full-document visual audits were retained; all ownership and scope declarations above remain in force.
