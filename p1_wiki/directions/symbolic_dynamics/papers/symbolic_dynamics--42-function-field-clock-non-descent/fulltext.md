---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--42-function-field-clock-non-descent"
canonical_tex: "symbolic_dynamics/papers/42-function-field-clock-non-descent/main.tex"
canonical_pdf: "symbolic_dynamics/papers/42-function-field-clock-non-descent/main.pdf"
source_sha256: "c7bb96126efaecaa321b925c5596440f7c14626130853e22ed3039bfbb4bec22"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Finite-Field Clocks Do Not Become Rational Primes: Exact Factor Non-Descent for the Full Shift

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/42-function-field-clock-non-descent>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/42-function-field-clock-non-descent/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/42-function-field-clock-non-descent/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/42-function-field-clock-non-descent/PAPER_PLAN.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/42-function-field-clock-non-descent/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  The full shift over a finite field has a complete primitive-necklace ledger, an additive degree clock, and a finite determinant. We ask whether those same source factors can be read as the rational-prime Euler ledger without changing their clock, free symbol marker, multiplicity, or operator owner. For the historical field sizes $q\in\{2,3,5\}$, three exact obstructions answer no. First, clock preservation sends every primitive necklace of length $n$ to the forced label $q^n$; the length-two class $[01]$ would therefore map to the composite $q^2$. Second, equality of a source monomial $z^nq^{-ns}$ with a rational-prime monomial $zp^{-s}$ forces $n=1$ and $p=q$, but the source has $q$ distinct length-one factors and the target has one factor at $q$. Third, the logarithms of the marked determinants disagree at their first $z$ coefficient: $q^{1-s}$ is not the prime-zeta series $\sum_p p^{-s}$. These failures are independent of zero data and do not damage the positive function-field interpretation of the full shift. They give a typed program-closure theorem of bounded novelty, not a new arithmetic zeta mechanism. The source retains analytic primitive and determinant credit, whereas the rational-prime extension is rejected and Route B remains closed.
author:
- Anonymous Authors
bibliography:
- references.bib
date: 'August 17, 2026'
title: |
  Finite-Field Clocks Do Not Become Rational Primes:\
  Exact Factor Non-Descent for the Full Shift
```

## Markdown 正文

# Introduction {#sec:introduction}

A determinant can have an Euler product without its primitive factors being rational primes. Periodic-point zeta functions organize closed dynamical orbits, while arithmetic Euler products organize prime objects of a specified ring or field. The two forms may look similar, but a factorwise identification must also preserve the type of the primitive object, its clock, its marker, its repetitions, and the operator that owns the determinant. Periodic-point zeta functions and finite-shift determinant identities are foundational prior art [@artin1965periodic; @bowen1970zeta]; their existence alone supplies no rational-prime dictionary.

This distinction is concrete for the full shift over $\mathbb{F}_q$. A primitive necklace of length $n$ has the finite-field degree clock $n\log q$ and carries the marked factor $$\bigl(1-z^n q^{-ns}\bigr)^{-1}.$$ The complete source product collapses to the reciprocal of the scalar determinant $1-zq^{1-s}$. This ledger is exact: its degree counts agree with the classical counts of monic irreducible polynomials over $\mathbb{F}_q$. Recent necklace-polynomial work reiterates that count equality [@chebolu2026necklace]. Paper 42 does not claim any of these identities as new.

The narrower question is whether the source factors can be retyped, without alteration, as the rational-prime factors $(1-zp^{-s})^{-1}$. The target is not merely another indexing set. A rational prime has clock $\log p$, one primitive marker $z$, multiplicity one in the Euler product, and a separate diagonal operator owner. Keeping those fields explicit turns a vague resemblance into three elementary compatibility tests.

The comparison yields four precise contributions.

1.  We prove that no total map from all primitive source necklaces to rational primes preserves the exact source clock. The two-letter primitive class $[01]$ already forces the composite image $q^2$.

2.  We prove a separate factor obstruction. Equality of marker and analytic weight forces length one and $p=q$, where the $q$ source factors collide with one rational-prime factor.

3.  We compare the complete marked determinants without using zeros. Their logarithms have different first $z$ coefficients on the common absolute-convergence domain.

4.  We classify six declared repairs by the coordinate they abandon. The classification preserves the positive function-field ledger and refuses to transfer ownership from a changed marker, projection, or target operator.

The conclusion is deliberately local. It does not preclude an arbitrary relabeling, a partial factor, an induced system, a countable prime inventory, or an infinite-memory construction. Each such proposal may define a useful new model, but it must declare a new object and operator contract. Nor does the paper claim that a bounded literature search proves priority. The source identities have zero novelty, the broad mechanism has zero novelty, and the exact typed closure is assessed at only $3/10$.

The rest of the paper separates prior ownership and chronology ([2](#sec:prior-scope){reference-type="ref" reference="sec:prior-scope"}), fixes the two factor types ([3](#sec:source-ledger){reference-type="ref" reference="sec:source-ledger"}), proves the three independent obstructions ([4](#sec:non-descent){reference-type="ref" reference="sec:non-descent"}), and classifies repairs ([5](#sec:repairs){reference-type="ref" reference="sec:repairs"}). The strict Route disposition and reproducibility boundary appear in [6](#sec:route){reference-type="ref" reference="sec:route"}; exact auxiliary calculations are collected in [8](#app:exact-details){reference-type="ref" reference="app:exact-details"}.

# Prior ownership, retrospective selection, and scope {#sec:prior-scope}

#### Finite-shift determinants.

Artin--Mazur zeta functions encode periodic-point counts, while Bowen and Lanford identify the determinant and Euler-product structure for finite shifts [@artin1965periodic; @bowen1970zeta]. Those frameworks own the passage from a finite symbolic system to a rational dynamical zeta function. In the present source, the resulting scalar determinant and the primitive-necklace product are inherited inputs, not new theorems about rational primes.

#### Necklaces and finite-field primes.

The necklace polynomial counts aperiodic cyclic words. The same polynomial counts monic irreducible polynomials of fixed degree over a finite field, a classical identity also stated explicitly in current literature [@chebolu2026necklace]. This equality supplies the correct function-field positive control: degree $n$ corresponds to norm $q^n$. It does not by itself select an objectwise bijection, and it does not turn the prime power $q^n$ into a positive rational prime when $n>1$.

#### The rational Euler ledger.

The Riemann zeta function has one Euler factor for each positive rational prime on $\operatorname{Re}s>1$ [@nistDLMF25211]. We use that product only as a target comparator. The countable diagonal operator with eigenvalues $p^{-s}$ owns the marked target determinant; it is not the one-dimensional weighted adjacency of the full $q$-shift. Consequently, equality of displayed zeta notation cannot transfer primitive type or operator ownership.

@ \>p0.20 \>p0.20 \>p0.19Y@ Family & Primitive object & Owned clock/marker & Paper-42 boundary\
Full $q$-shift & aperiodic cyclic word & $n\log q$, $z^n$ & Exact source; all positive formulas are prior art.\
Finite-field affine line & monic irreducible polynomial & degree norm $q^n$ & Countwise positive control; not a rational prime.\
Rational Euler product & rational prime $p$ & $\log p$, $z$ & Separate target inventory and operator.\
Partial/re-marked source & selected or induced orbit & chosen return marker & Changed projection or marker; no full-ledger credit.\
Paper 42 & no new primitive species & frozen fields only & Proves incompatibility of the same-object conjunction.\

#### Retrospective candidate selection.

The historical parent was selected by a Boolean rule over six immutable Session-4 cards. The rule requires a proved weak arithmetic relation, a proved primitive ledger, a proved analytic determinant, an A3 failure, the constant finite-field degree clock, and an explicit missing rational-prime factor correspondence. Exactly one card, historical `SD-C01`, satisfies those clauses. The uniqueness is descriptive rather than prospective: every card outcome and every witness in this paper was known before the rule was written. It therefore supplies no outcome-independent evidence, preregistration, priority, or novelty credit.

Terminal Paper 39, the final Paper-40 research seal, and the frozen Paper-41 package serve only as collision and governance boundaries. They do not rank or authorize this candidate. In particular, Paper 40 concerns a Gauss/Mayer pair object, while Paper 41 concerns a rooted Knauf clock that fails to descend on its own source. The present full-shift clock is already cyclic and temporally additive; only its proposed retyping as rational-prime factors fails.

#### Novelty and search boundary.

The frozen literature audit assigns source/function novelty $0/10$, broad mechanism novelty $0/10$, and conditional typed-closure novelty $3/10$. Citation chaining did not locate the exact clock/marker/multiplicity theorem, but a bounded negative search is not a proof that no equivalent formulation exists. The paper is therefore positioned as a program-closure and ownership certificate, not as a new relation between finite fields and rational primes.

# Frozen source ledger and typed comparison {#sec:source-ledger}

Fix $q\in\{2,3,5\}$ and let $$\Sigma_q=\mathbb{F}_q^{\mathbb Z}$$ with the left shift $\sigma$. A nonempty word is *primitive* when it is not a proper power. The source primitive object is its oriented cyclic class: cyclic rotations are identified, but reversal is not identified unless it is already a rotation. We write $\operatorname{Prim}_q$ for these primitive necklaces and $n(\gamma)$ for the length of $\gamma\in\operatorname{Prim}_q$. Ordinary word powers encode temporal repetition.

For $\gamma\in\operatorname{Prim}_q$ of length $n$, define $$T_q(\gamma)=n\log q,
 \qquad
 F_\gamma(s,z)=\left(1-z^nq^{-ns}\right)^{-1}.$$ The free variable $z$ marks one original shift symbol. Thus the $r$th repetition contributes $z^{nr}q^{-nrs}$; marker degree and temporal repetition are distinct pieces of data.

The weighted adjacency of the one-vertex, $q$-loop graph acts on $\mathbb{C}$ by $$\mathcal{L}_{q,s,z}f=zq^{1-s}f.$$ It is a scalar operator, but it still owns a complete dynamical determinant. Indeed, the full shift has exactly $q^r$ points fixed by $\sigma^r$. The marked periodic-point exponential is therefore $$\begin{aligned}
 Z_q(s,z)
 &=\exp\left(\sum_{r\ge1}\frac{q^r(zq^{-s})^r}{r}\right) \\
 &=\exp\left(\sum_{r\ge1}\frac{(zq^{1-s})^r}{r}\right)
 =\frac{1}{1-zq^{1-s}}.                                      \label{eq:source-zeta}\end{aligned}$$ This is a formal identity in $z$ and an analytic identity in the disk where the displayed logarithmic series converges. Its inverse is the ordinary finite-dimensional determinant $$D_q(s,z)=\det(I-\mathcal{L}_{q,s,z})=1-zq^{1-s}.                           \label{eq:source-det}$$ The periodic-point and determinant organization follows the standard finite- shift framework [@artin1965periodic; @bowen1970zeta].

Let $N_q(n)$ denote the number of primitive cyclic classes of length $n$. Every word fixed by $\sigma^r$ repeats a unique primitive necklace of length $d\mid r$, and each such necklace has $d$ based representatives. Hence $$q^r=\sum_{d\mid r}dN_q(d),
 \qquad
 N_q(n)=\frac1n\sum_{d\mid n}\mu(d)q^{n/d}.                 \label{eq:necklace}$$ Regrouping repetitions in [\[eq:source-zeta\]](#eq:source-zeta){reference-type="ref" reference="eq:source-zeta"} gives $$Z_q(s,z)=\prod_{\gamma\in\operatorname{Prim}_q}
 \left(1-z^{n(\gamma)}q^{-s n(\gamma)}\right)^{-1}.          \label{eq:source-product}$$ The count in [\[eq:necklace\]](#eq:necklace){reference-type="ref" reference="eq:necklace"} also counts monic irreducible polynomials of degree $n$ over $\mathbb{F}_q$ [@chebolu2026necklace]. Under the finite-field norm, both types carry $q^n$ and the degree clock $n\log q$. This is the source positive control. We use only count equality; no canonical objectwise bijection is asserted.

The rational-prime comparator has a different primitive type. Let $\mathbb{P}$ be the positive rational primes and define, on $\ell^2(\mathbb{P})$, $$Q_se_p=p^{-s}e_p.$$ For $\operatorname{Re}s>1$, the operator is trace class because $\sum_p|p^{-s}|<\infty$. It owns $$D_{\mathbb{P}}(s,z)=\det(I-zQ_s)
 =\prod_{p\in\mathbb{P}}(1-zp^{-s}),                             \label{eq:target-det}$$ whose reciprocal specializes at $z=1$ to the rational Euler product [@nistDLMF25211]. For sufficiently small $|z|$, $$-\log D_{\mathbb{P}}(s,z)
 =\sum_{r\ge1}\frac{z^r}{r}P(rs),
 \qquad
 P(s)=\sum_{p\in\mathbb{P}}p^{-s}.                              \label{eq:target-log}$$ The diagonal comparator proves that the target product has a valid operator; it does not make that operator source-owned.

Any credited factorwise descent must preserve several necessary fields at once. Comparing one source factor with one target factor produces the matrix in [\[tab:necessary-fields\]](#tab:necessary-fields){reference-type="ref" reference="tab:necessary-fields"}.

@ \>p0.20 \>p0.23 \>p0.23Y@ Field & Source length $n$ & Rational-prime target & Forced consequence\
Clock/weight & $n\log q$, $q^{-ns}$ & $\log p$, $p^{-s}$ & $p=q^n$\
Primitive marker & $z^n$ & $z$ & $n=1$\
Multiplicity & $N_q(n)$ factors & one factor per $p$ & bijective factor count\
Repetition & $z^{nr}q^{-nrs}$ & $z^rp^{-rs}$ & only after primitive fields agree\
Ownership & scalar $q$-loop adjacency & diagonal prime inventory & same owner required\

The full-ledger claim also requires totality: every source primitive factor must be accounted for. A partial map can produce a correct local factor, but it cannot identify the complete source product with the complete target product. With these types fixed, the three obstructions in the next section are direct consequences rather than post-hoc choices of a convenient marker or projection.

# Three exact non-descent theorems {#sec:non-descent}

The three failures below use different data. The clock theorem does not depend on the marker convention. The marker/multiplicity theorem does not use the analytic coefficient limit. The determinant theorem does not require an objectwise map. Keeping them separate shows exactly which proposed identification each witness defeats.

## Clock preservation forces composite support

[\[thm:clock\]]{#thm:clock label="thm:clock"} There is no total map $$\pi:\operatorname{Prim}_q\longrightarrow\mathbb{P}$$ such that $$\log\pi(\gamma)=n(\gamma)\log q$$ for every primitive source necklace $\gamma$.

The word $01$ exists over each frozen alphabet. It is primitive: if a two-letter word were a proper power, it would be the square of a one-letter word and its two symbols would coincide. Let $\gamma=[01]$. Clock preservation gives $$\log\pi(\gamma)=2\log q=\log(q^2).$$ The real logarithm is injective on positive numbers, so $\pi(\gamma)=q^2$. Since $q>1$, this forced label is composite, contrary to $\pi(\gamma)\in\mathbb{P}$.

Totality matters because the claim concerns the full primitive product. Omitting $[01]$ defines a partial projection, not a counterexample to [\[thm:clock\]](#thm:clock){reference-type="ref" reference="thm:clock"}. Mapping the class to a finite-field prime polynomial also changes the target type, and replacing the clock by an arbitrary prime enumeration abandons the theorem's equality.

## Marker and weight expose multiplicity

[\[thm:multiplicity\]]{#thm:multiplicity label="thm:multiplicity"} There is no factorwise identification of all source primitive factors $$\left(1-z^nq^{-ns}\right)^{-1}$$ with rational-prime factors $(1-zp^{-s})^{-1}$ that preserves the free marker, analytic weight, and multiplicity.

Equality of the factor monomials requires $$z^nq^{-ns}=zp^{-s}.                                         \label{eq:factor-equality}$$ Because $z$ is free, equality of exponents in [\[eq:factor-equality\]](#eq:factor-equality){reference-type="ref" reference="eq:factor-equality"} forces $n=1$. Equality of the weights as functions of $s$ then forces $p=q$. By [\[eq:necklace\]](#eq:necklace){reference-type="ref" reference="eq:necklace"}, $$N_q(1)=q.$$ Thus the source has $q$ distinct length-one primitive necklaces, all with the only compatible monomial $zq^{-s}$. The rational Euler product has one primitive factor indexed by the rational prime $p=q$. The required factor multiplicity is therefore $q:1$, not $1:1$.

Specializing $z=1$ before the comparison erases the marker witness rather than answering it. Likewise, merging the $q$ source factors or selecting one of them introduces an explicit quotient or projection. Those constructions can be useful controls, but they are outside the factorwise identification in [\[thm:multiplicity\]](#thm:multiplicity){reference-type="ref" reference="thm:multiplicity"}.

## The first marked coefficient already differs

[\[thm:coefficient\]]{#thm:coefficient label="thm:coefficient"} On their common absolute-convergence domain, $D_q(s,z)$ and $D_{\mathbb{P}}(s,z)$ are not equal as analytic functions of $(s,z)$. Their logarithms differ in the coefficient of $z$.

Equations [\[eq:source-det\]](#eq:source-det){reference-type="eqref" reference="eq:source-det"} and [\[eq:target-log\]](#eq:target-log){reference-type="eqref" reference="eq:target-log"} give $$\{-\log D_q(s,z)\}=q^{1-s},
 \qquad
 [z]\{-\log D_{\mathbb{P}}(s,z)\}=P(s)=\sum_{p\in\mathbb{P}}p^{-s}.         \label{eq:first-coefficients}$$ The target series is the coefficient obtained from the rational Euler product on $\operatorname{Re}s>1$ [@nistDLMF25211]. We show the two functions in [\[eq:first-coefficients\]](#eq:first-coefficients){reference-type="ref" reference="eq:first-coefficients"} cannot agree.

Set $s=\sigma>1$ real and multiply by $2^\sigma$. For $q=2$, the source is identically $2$, whereas $$2^\sigma P(\sigma)
 =1+\sum_{p\ge3}\left(\frac2p\right)^\sigma\longrightarrow1.$$ For $q=3$ or $q=5$, the scaled source is $$2^\sigma q^{1-\sigma}=q\left(\frac2q\right)^\sigma
 \longrightarrow0,$$ while the scaled target still tends to one. To justify the target limit, bound the tail for $\sigma\ge2$ by $\sum_{n\ge3}(2/n)^2<\infty$ and apply dominated convergence term by term. Thus the first coefficients differ for every frozen $q$, and the analytic determinants cannot be identical.

This argument uses no rational-prime table, Riemann-zero data, fitting, or global divisor comparison. It also has the correct determinant orientation: the positive Euler products are reciprocals of $D_q$ and $D_{\mathbb{P}}$, while [\[thm:coefficient\]](#thm:coefficient){reference-type="ref" reference="thm:coefficient"} compares $-\log$ of the determinants.

[\[cor:closures\]]{#cor:closures label="cor:closures"} The total exact-clock rational-prime projection fails; the same-marker factorwise identification fails; and equality of the complete marked determinants fails. No one conclusion is enlarged to all partial maps, changed markers, induced systems, or symbolic extensions.

Apply [\[thm:clock,thm:multiplicity,thm:coefficient\]](#thm:clock,thm:multiplicity,thm:coefficient){reference-type="ref" reference="thm:clock,thm:multiplicity,thm:coefficient"} to their respective contracts. Their quantifier notes exclude precisely the changed constructions listed in the statement.

# Positive controls, repairs, and ownership {#sec:repairs}

The negative theorems are informative only if nearby valid constructions remain visible. Four positive controls prevent an overbroad conclusion.

#### Function-field control.

The degree counts $N_q(n)$ agree with the counts of monic irreducible polynomials over $\mathbb{F}_q$ [@chebolu2026necklace]. Their norm $q^n$, clock $n\log q$, and power repetitions match the source ledger. The scalar determinant in [\[eq:source-det\]](#eq:source-det){reference-type="ref" reference="eq:source-det"} is therefore not defective. What fails is only its proposed interpretation as one rational-prime factor per source primitive.

#### Single-factor control.

Selecting one length-one necklace produces the valid local factor $(1-zq^{-s})^{-1}$. This factor agrees with the rational-prime factor at $p=q$. The construction is deliberately non-total: it discards the remaining length-one factors and every primitive of higher length. It cannot identify the complete ledgers.

#### Target-operator control.

The diagonal family $Q_s$ owns the rational-prime determinant on $\operatorname{Re}s>1$. Hence [\[thm:coefficient\]](#thm:coefficient){reference-type="ref" reference="thm:coefficient"} does not claim that the target Euler product lacks an operator. It says that $Q_s$ is not the source's one-dimensional weighted adjacency.

#### Repetition control.

Under the finite-field norm label $q^n$, analytic weights repeat correctly: $(q^n)^{-rs}=q^{-nrs}$. The obstruction is not exponent algebra. Rational- prime support fails at the primitive level, and the original marker repeats as $z^{nr}$ rather than $z^r$.

The six repairs frozen in the source contract are classified in [\[tab:repairs\]](#tab:repairs){reference-type="ref" reference="tab:repairs"}. The last column records the first coordinate that prevents same-object credit; other fields may fail as well.

@ \>p0.24 \>p0.19 \>p0.19Y@ Repair & What it preserves & What it changes & Classification\
Norm label $q^n$ & clock and weight & prime support for $n\ge2$ & exact negative projection\
Keep degree one & marker and clock & totality and multiplicity & incomplete source ledger\
Choose one degree-one orbit & one local factor & totality and source inventory & local positive control\
Enumerate by rational primes & support by choice & exact clock and marker semantics & post-hoc relabeling\
Induce one return per primitive & stored orbit weight & $z^n$ to $z$ and operator & changed object/marker\
Prime-polynomial dictionary & source clock, marker, counts & target primitive type & function-field positive control\

Within the repair list in [\[tab:repairs\]](#tab:repairs){reference-type="ref" reference="tab:repairs"}, every route gives up at least one of rational-prime support, exact source clock, original marker, full multiplicity, or source determinant ownership.

The norm label loses rational-prime support by [\[thm:clock\]](#thm:clock){reference-type="ref" reference="thm:clock"}. The degree-one restriction loses full multiplicity by [\[thm:multiplicity\]](#thm:multiplicity){reference-type="ref" reference="thm:multiplicity"}; choosing one orbit also loses totality. An arbitrary enumeration does not obey $\log p=n\log q$. Induction retypes $z^n$ as a return marker $z$ and changes the operator. Finally, the prime-polynomial dictionary keeps the source fields but targets function-field primes rather than rational primes.

An unlisted construction does not falsify this corollary. It requires a new source lock and a fresh entry in the ownership table. This bounded exhaustiveness is essential: the paper classifies declared repairs, not all possible codes, factors, functors, or extensions.

# Strict Route audit and reproducibility boundary {#sec:route}

The rational-prime comparison does not overwrite the source coordinates. The strict Route evaluation is therefore read row by row.

@ \>p0.08 \>p0.30Y@ Rung & Verdict & Exact reason\
A0 & `A0_WEAK_``ARITHMETIC_RELATION` & Exact finite-field prime-polynomial arithmetic exists, but rational-prime support does not emerge.\
A1 & `A1_PASS_ANALYTIC` & Primitive necklaces, orientation, powers, completeness, and multiplicity are intrinsic to the full shift.\
A2 & `A2_ANALYTIC_``DETERMINANT` & The same full-shift object owns $D_q(s,z)=1-zq^{1-s}$ and its primitive product.\
A3 & `A3_FAIL` & The rational-prime marked coefficient, completed Riemann structure, and required divisor growth are absent from the frozen object.\
A4 & `A4_FAIL` & No fixed self-adjoint same-clock Hilbert--Polya lift or completed target divisor is defined.\

Thus the tuple is $$%
  \begin{gathered}
  (\ifmmode\text{\ttfamily A0\_WEAK\_ARITHMETIC\_RELATION}\else\texttt{A0\_WEAK\_ARITHMETIC\_RELATION}\fi,\
   \ifmmode\text{\ttfamily A1\_PASS\_ANALYTIC}\else\texttt{A1\_PASS\_ANALYTIC}\fi,\\[-0.2ex]
   \ifmmode\text{\ttfamily A2\_ANALYTIC\_DETERMINANT}\else\texttt{A2\_ANALYTIC\_DETERMINANT}\fi,\
   \ifmmode\text{\ttfamily A3\_FAIL}\else\texttt{A3\_FAIL}\fi,\ \ifmmode\text{\ttfamily A4\_FAIL}\else\texttt{A4\_FAIL}\fi)
  \end{gathered},$$ with overall verdict `ROUTE_A_REJECTED`. The explicit Route-B flag and the duplicate top-level flag are both false. In particular, the separate rational-prime diagonal family cannot raise A0, A3, or A4, while the failed projection cannot lower the source-owned A1 or A2.

The independent Devil's Advocate review recomputed the necklace counts, primitivity witness, determinant orientations, first-coefficient limits, selector outcome, source-ID resolution, and predecessor boundaries. It accepted the corrected preauthority package and left no major theorem or scope defect. That review is a research-governance gate, not numerical evidence and not authority authorization.

The source chronology remains explicit. All six historical card outcomes, the retrospective rule, and the theorem witnesses were known before the research package was written. Only the corrected final research bytes were frozen before independent review. This ordering earns no preregistration, outcome-independent, priority, or novelty credit.

# Limitations and conclusion {#sec:conclusion}

The full $q$-shift already has the structure it should have: primitive necklaces, an additive finite-field degree clock, ordinary powers, a free source-symbol marker, and a same-object determinant. The obstruction appears only when those source factors are required to become rational-prime factors without changing any field. Exact clock preservation forces the length-two primitive $[01]$ to the composite $q^2$; marker and weight preservation expose a $q:1$ multiplicity collision at length one; and the complete marked determinants disagree in their first logarithmic coefficient.

These conclusions do not classify all maps between function fields and number fields. A partial map can omit obstructing orbits. An induced system can replace the symbol marker by a return marker. A countable inventory can place one state at each rational prime. An infinite-memory code can carry history that the finite full shift does not. Each option lies outside the frozen same-object contract and may be studied after declaring a new phase space, clock, marker, function space, and operator owner.

The contribution is correspondingly modest. Classical source identities and the rational Euler product receive no novelty credit; the selector is wholly retrospective; and the typed closure is rated $3/10$. Its value is methodological: it resolves one historical branch with explicit types and prevents a valid function-field determinant from being miscredited as a rational-prime mechanism. Under the strict audit, Route A is rejected and Route B remains closed.

If subsequent verification finds that this exact typed closure has already been formally published, the disposition is `STOP_DUPLICATE`: this standalone paper route stops and receives no novelty credit.

# Exact combinatorics, witness ledger, and analytic details {#app:exact-details}

## Möbius inversion and the first two degrees

Let $a_r=q^r$ be the number of based words fixed by $\sigma^r$. If $N_q(d)$ counts primitive cyclic classes of length $d$, then each class has $d$ based representatives and contributes whenever $d\mid r$. Therefore $$a_r=\sum_{d\mid r}dN_q(d).$$ Möbius inversion gives $$nN_q(n)=\sum_{d\mid n}\mu(d)q^{n/d}.$$ For $n=1,2$, $$N_q(1)=q,
 \qquad
 N_q(2)=\frac{q^2-q}{2}.$$ The exact frozen witness ledger is $$\begin{array}{c|ccc|c}
q&N_q(1)&N_q(2)&[01]\text{ primitive}&q^2\text{ prime?}\\
\hline
2&2&1&\text{yes}&\text{no}\\
3&3&3&\text{yes}&\text{no}\\
5&5&10&\text{yes}&\text{no}
\end{array}$$ The table illustrates proved formulas; no finite census is used to infer an infinite statement. The word $01$ is primitive for every alphabet containing the distinct symbols $0$ and $1$, and the same symbolic witness handles all three frozen values of $q$.

## Primitive regrouping

Starting from the primitive product, $$\begin{aligned}
 \log Z_q(s,z)
 &=\sum_{\gamma\in\operatorname{Prim}_q}\sum_{r\ge1}
   \frac{z^{n(\gamma)r}q^{-s n(\gamma)r}}{r}\\
 &=\sum_{m\ge1}\frac{z^mq^{-sm}}{m}
   \sum_{d\mid m}dN_q(d)\\
 &=\sum_{m\ge1}\frac{(zq^{1-s})^m}{m}.\end{aligned}$$ The middle line sets $m=n(\gamma)r$; the cyclic multiplicity $d$ converts the primitive count into the $q^m$ fixed based words. Exponentiation gives [\[eq:source-zeta\]](#eq:source-zeta){reference-type="ref" reference="eq:source-zeta"}. This calculation is formal in $z$ and analytic wherever the series is absolutely convergent.

## Target coefficient limit

For $\sigma\ge2$, $$2^\sigma P(\sigma)
 =1+\sum_{p\ge3}(2/p)^\sigma.$$ Each tail term tends to zero. Moreover, $$0\le \sum_{p\ge3}(2/p)^\sigma
 \le \sum_{n\ge3}(2/n)^2<\infty.$$ Dominated convergence therefore yields the target limit one. The source limits after the same scaling are two for $q=2$ and zero for $q=3,5$. Consequently $q^{1-s}$ and $P(s)$ cannot agree on a nonempty open subset of $\operatorname{Re}s>1$.

## Direct falsifiers

Each main theorem has a concrete defeat condition.

-   would fail if $[01]$ were imprimitive in the frozen shift or if $q^2$ were a rational prime. Neither condition holds.

-   would fail if a bijection of all factors preserved $z^nq^{-ns}=zp^{-s}$ and target multiplicity one. Formal marker degree and [\[eq:necklace\]](#eq:necklace){reference-type="ref" reference="eq:necklace"} rule this out.

-   would fail if $q^{1-s}=P(s)$ on a nonempty open subset. The exact limits above rule this out.

-   The repair corollary would require revision if a listed row preserved every locked field. An unlisted model instead requires a new contract.

The positive-control falsifier is equally important: if the necklace count did not match finite-field irreducible-polynomial counts, the paper would have damaged its source object. The verified count identity [@chebolu2026necklace] prevents that failure.

# Type, literature, and provenance firewalls {#app:boundaries}

## Type firewall

@ \>p0.25 \>p0.22 \>p0.20Y@ Type & Primitive relation & Clock/marker & Owner\
Shift primitive necklace & ordinary word power & $n\log q$, $z^n$ & full $q$-shift adjacency\
Finite-field prime polynomial & polynomial power & degree clock/marker & affine-line function-field ledger\
Rational-prime atom & rational prime power & $\log p$, $z$ & separate diagonal inventory\

The first two rows have equal degree counts, a classical fact reiterated in current necklace-polynomial work [@chebolu2026necklace]. The third row is the rational Euler product documented by the authoritative formula reference [@nistDLMF25211]. Neither statement creates a canonical cross-type bijection.

## Literature firewall

Artin--Mazur owns the periodic-point zeta framework [@artin1965periodic]; Bowen--Lanford owns foundational finite-shift determinant/Euler-product structure [@bowen1970zeta]; necklace counts and finite-field irreducible counts are prior art [@chebolu2026necklace]; and the rational Euler product is classical [@nistDLMF25211]. Paper 42 claims none of those functions or formulas. The only bounded claim is their incompatibility under the frozen simultaneous typing obligations.

The literature audit covered a finite set of terms and citation chains through its declared cutoff. It did not locate the exact project-specific conjunction. That statement records search procedure, not universal absence. The 2026 necklace source is a preprint and is used only for the explicit count overlap, not as peer-reviewed novelty evidence.

## Analytic and provenance firewall

The primitive product and periodic-point exponential are formal in $z$ and analytic where their displayed series converge. The rational-prime diagonal operator is trace class on $\operatorname{Re}s>1$, and its trace-log is invoked only for sufficiently small $|z|$. Meromorphic continuation at $z=1$ does not erase the free marker or create a missing factor map.

The selector was written after all source-card outcomes and witnesses were known. Predecessor packages supplied collision boundaries but no ranking or authorization. Independent review accepted the corrected research package; root governance would still be required for any authority publication. This writer draft is therefore a transportable exposition of frozen claims, not a new research lock or an integrated Route record.
