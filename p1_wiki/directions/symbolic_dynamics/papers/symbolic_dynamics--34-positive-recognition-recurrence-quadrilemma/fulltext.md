---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--34-positive-recognition-recurrence-quadrilemma"
canonical_tex: "symbolic_dynamics/papers/34-positive-recognition-recurrence-quadrilemma/main.tex"
canonical_pdf: "symbolic_dynamics/papers/34-positive-recognition-recurrence-quadrilemma/main.pdf"
source_sha256: "4047b376ebb22999724b1d1eb4d1a8b270402d048acc667aac6384fe3c1aad3d"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Recognition Before Recurrence: A Positive Compiler Quadrilemma for Arithmetic Markov Shifts

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/34-positive-recognition-recurrence-quadrilemma>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/34-positive-recognition-recurrence-quadrilemma/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/34-positive-recognition-recurrence-quadrilemma/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/34-positive-recognition-recurrence-quadrilemma/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/34-positive-recognition-recurrence-quadrilemma/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We study whether a stationary arithmetic recognizer can acquire an exact prime-only recurrent ledger without changing its symbolic object. The answer is negative for a precisely frozen class: one-sided countable loop-allowed directed graphs with no parallel edges, positive scalar one-step weights, a finite orbit-separating visible alphabet, additive total clock $T(\gamma_p)=\log p$, the original graph-step marker $z$, and the natural whole-vertex operator on $\ell^2(V)$. A literal atomic ledger forces every recurrent component to be one private simple atom cycle. Shared recurrence creates a mixed primitive root; off-core recognition is invisible to every power trace and, when the whole operator is trace class, to its Fredholm determinant. Finite visible separation forces an infinite subsequence $\ell(p)\ge \log p/(4\log b)$, so the exact clock leaves uniformly large weights on mutually orthogonal cycles and the whole adjacency is noncompact. First return can be trace class, but it changes $1-z^{\ell(p)}p^{-s}$ into $1-zp^{-s}$. An exact audit exhausts all $66{,}066$ loop-allowed digraphs on at most four vertices and verifies $844{,}544$ repaired mixed-root certificates with no true failure. It also preserves $18{,}272$ counterexamples to a stronger preregistered connector normal form. We claim only this source-locked synthesis; computation in symbolic systems, period-set realization, renewal zeta formulae, coding inequalities, and trace-ideal boundaries are established prior art.
author:
- Anonymous Authors
bibliography:
- references.bib
date: 'August 15, 2026'
title: |
  Recognition Before Recurrence:\
  A Positive Compiler Quadrilemma for Arithmetic Markov Shifts
```

## Markdown 正文

# Introduction

Computational dynamics can encode reachability, halting, and periodicity. That broad connection is classical, from generalized-shift models of Turing machines [@Kurka1997; @DelvenneKurkaBlondel2006] to recent Koopman formulations in which absorbing halting states and cycles have direct spectral signatures [@CaravelliDelvenne2026]. Period sets are also highly realizable: multidimensional shifts can encode complexity classes [@JeandelVanier2015], while finite and finitely presented systems obey sharp least-period classifications [@DoeringPavlov2019; @deJong2026]. Thus the unrestricted claim that recognition cannot become recurrence is false.

Our question is narrower. Suppose a single one-sided countable Markov graph must expose arithmetic recognition, carry a positive scalar edge roof, retain the original graph-step marker, and own an ordinary Fredholm determinant on the natural vertex Hilbert space. Can its primitive periodic ledger contain exactly one orbit for each prime and no mixed orbit? The object is frozen before the answer is known; a terminal prime projector, a supplied prime alphabet, and an induced time coordinate are disallowed as same-object repairs.

The answer is a four-way incompatibility, summarized in [\[fig:quad\]](#fig:quad){reference-type="ref" reference="fig:quad"}. Shared recurrent computation produces a mixed primitive root. Recognition outside the recurrent core prunes exactly from traces and determinants. Private visible cycles require logarithmic code length; with total roof $\log p$ their whole adjacency is noncompact. First return repairs the operator only by replacing the raw marker $z^{\ell(p)}$ with one return marker $z$.

The contribution is a quantifier-clean ownership theorem, not a new primitive-root theorem, Kraft inequality, or compactness criterion. Its value is diagnostic: the same source, marker, periodic ledger, and operator cannot be silently exchanged while credit is retained. The exact audit is part of that diagnosis. A stronger preregistered connector normal form fails on $18{,}272$ finite instances; the corrected proof needs only arbitrary mutual paths inside a strongly connected component.

The remainder of the paper separates prior art from the source lock, proves the quadrilemma, reports the exact audit, and closes the positive Route-A candidate. The next benchmark is the arithmetic $ax+b$ and Bost--Connes setting, but only after a new symbolic source lock; its partition function cannot be imported as periodic-orbit credit.

# Literature and claim boundary

Finite graph zeta and determinant formulae originate with @BowenLanford1970. Countable loop graphs are organized by first-return series, and their zeta functions exhibit the familiar $1/(1-f)$ structure [@BoyleBuzziGomez2006; @Hong2011]. Circular-code formulae already capture the combinatorics of concatenated return words [@Keller1991]. More strongly, complex local weights on a renewal shift can realize very flexible holomorphic germs [@Sarig2004]; positivity and source ownership are therefore indispensable here.

The finite-code estimate used below is elementary distinct-word counting. The classical inequality of @McMillan1956 gives a stronger bound when unique decipherability is assumed, and constrained versions are known for sofic codes [@BealPerrin2005]. We do not claim a new coding inequality. Likewise, ordinary Fredholm determinants require trace-ideal control [@Simon2005]. Infinite weighted graphs can possess other valid determinant frameworks under different total-weight hypotheses [@Deitmar2015]; our noncompactness conclusion concerns the specified whole vertex adjacency, not every possible graph operator.

Inducing is also legitimate mathematics. State expansion and time change have classical flow-equivalence lineage [@ParrySullivan1975]. Our marker statement is an ownership firewall: one first-return step is not one edge step. It does not declare induced systems invalid.

The closest current collision is the 2026 Koopman treatment of symbolic computation by @CaravelliDelvenne2026; the closest period-spectrum collision is the 2026 classification and realization result of @deJong2026. A bounded primary-source search completed on 15 August 2026 found no statement of the exact conjunction used here. This is not a priority claim. Every component has precedent, and the novelty asserted is only the source-locked conjunction and its adversarial audit.

Finally, the Bost--Connes system has partition function $\zeta(\beta)$ [@BostConnes1995], and the $ax+b$ semigroup has a canonical $C^*$-algebraic treatment [@Cuntz2008]. These are benchmarks for the next paper, not instances of the compiler class below.

# Frozen compiler class {#sec:lock}

Let $G=(V,E)$ be one fixed countable loop-allowed directed graph with no parallel edges, generated by a cutoff-independent rule. Its phase space is the one-sided edge shift $$X_G^+=\{e_0e_1\ldots:t(e_j)=o(e_{j+1})\}.$$ A primitive orbit is a nonempty directed closed edge word modulo cyclic rotation that is not a proper temporal power. Reflection is not identified. The free variable $z$ records one edge of this original graph.

Let $\mathcal A$ be a countably infinite atom set with norm $N:\mathcal A\to(1,\infty)$. We require multiplicative freeness: $$\label{eq:free}
\prod_{a\in\mathcal A}N(a)^{m_a}=1,\quad m_a\in\mathbb Z
\text{ finitely supported}
\quad\Longrightarrow\quad m_a=0\ \forall a.$$ The prime specialization is $\mathcal A=\mathbb P$ and $N(p)=p$. Enumerate the atoms in nondecreasing norm and assume eventually $$\label{eq:growth}
N(a_j)\le j^\kappa.$$ For rational primes one may take $\kappa=2$.

Fix a finite visible alphabet $\mathcal B$, $b=|\mathcal B|\ge2$, and after a higher-block recoding a one-edge label map $\lambda:E\to\mathcal B$. If $\Lambda(\gamma)$ is the cyclic label word of an orbit, visibility means $$\label{eq:separation}
\Lambda(\gamma_a)=\Lambda(\gamma_c)\quad\Longrightarrow\quad a=c.$$ Without [\[eq:separation\]](#eq:separation){reference-type="eqref" reference="eq:separation"}, an arbitrary inventory may be hidden in countable vertex names.

The nonnegative edge roof $\tau:E\to[0,\infty)$ is frozen before evaluation. For real $\sigma>0$ the whole weighted adjacency on $\mathcal H=\ell^2(V)$ is $$\label{eq:whole}
L_\sigma\delta_u=\sum_{e:u\to v}e^{-\sigma\tau(e)}\delta_v.$$ If it is unbounded, the whole-operator gate has already failed. A weighted anisotropic space or an induced return space is a different owned object.

There is exactly one primitive orbit $\gamma_a$ for every $a\in\mathcal A$, there are no other primitive orbits, and $$\label{eq:clock}
T(\gamma_a):=\sum_{e\in\gamma_a}\tau(e)=\log N(a).$$ An extra mixed primitive word is a failure before any cancellation is considered. Temporal repetitions of $\gamma_a$ are allowed and are not new primitive orbits.

The central connected ledger is $$\label{eq:ledger}
\mathcal L_G(s,z)=
\sum_{[\gamma]\ \mathrm{primitive}}\sum_{r\ge1}
\frac{z^{r|\gamma|}}{r}e^{-srT(\gamma)}.$$ We first read [\[eq:ledger\]](#eq:ledger){reference-type="eqref" reference="eq:ledger"} literally. Only after trace-class ownership is proved may it be identified with $-\log\det(I-zL_s)$.

Recognition edges may be transient, periodically active, or shared recurrent. A terminal support projector, a supplied prime table, a cutoff-dependent alphabet, target-zero data, and an after-the-fact orbit weight are forbidden. Ordinary nondeterministic paths are counted with multiplicity; Boolean path existence is not the scalar semantics of [\[eq:whole\]](#eq:whole){reference-type="eqref" reference="eq:whole"}.

# The positive compiler quadrilemma

[\[thm:main\]]{#thm:main label="thm:main"} Assume the source lock of [3](#sec:lock){reference-type="ref" reference="sec:lock"}. Write $\ell(a)=|\gamma_a|$. Then:

1.  Every $\gamma_a$ is a simple directed cycle, distinct atom cycles are vertex-disjoint, and every recurrent strongly connected component is exactly one atom cycle. Shared recurrent computation creates an extra mixed primitive root.

2.  Let $C_\sigma$ retain only the atom-cycle edges on the same vertex space. If $L_\sigma\in\mathcal S_1$, then $C_\sigma\in\mathcal S_1$ and $$\label{eq:trace-equality}
    \mathop{\mathrm{Tr}}L_\sigma^r=\mathop{\mathrm{Tr}}C_\sigma^r\quad(r\ge1),$$ so for all $z\in\mathbb C$, $$\label{eq:rawdet}
    \det(I-zL_\sigma)=\det(I-zC_\sigma)
    =\prod_{a\in\mathcal A}\bigl(1-z^{\ell(a)}N(a)^{-\sigma}\bigr).$$ All terminal and off-core recognition is determinant-invisible.

3.  Under [\[eq:growth\]](#eq:growth){reference-type="eqref" reference="eq:growth"} and [\[eq:separation\]](#eq:separation){reference-type="eqref" reference="eq:separation"}, infinitely many atoms satisfy $$\label{eq:length}
    \ell(a)\ge \frac{\log N(a)}{2\kappa\log b}.$$ For every $\sigma>0$, the whole adjacency is therefore either unbounded or bounded and noncompact, hence belongs to no finite Schatten class. For primes, $$\label{eq:prime-length}
    \ell(p)\ge\frac{\log p}{4\log b},\qquad
    \max_{e\in\gamma_p}e^{-\sigma\tau(e)}\ge b^{-4\sigma}$$ on an infinite subsequence.

4.  First return to one base point per private cycle gives the diagonal operator $R_se_a=N(a)^{-s}e_a$ and, in its trace-class half-plane, $$\label{eq:induced}
    \det(I-zR_s)=\prod_a(1-zN(a)^{-s}).$$ The raw and induced local factors agree at $z=1$, but their free-marker germs agree only if every $\ell(a)=1$. Infinite length-one cycles contradict finite-alphabet separation.

[\[cor:compiler\]]{#cor:compiler label="cor:compiler"} No compiler in the frozen class can simultaneously have genuine shared recurrent recognition, a literal prime-only ledger, finite local visibility, the exact total roof $\log p$, a compact whole adjacency on natural $\ell^2(V)$, and the unchanged edge marker. Moving recognition off the cycles gives pruning; serializing it on private visible cycles gives clock dilution; sharing it gives mixed primitives; inducing changes time.

The theorem is a conjunction of exact statements. It neither asserts that arbitrary countable graphs cannot realize a chosen orbit inventory nor rules out signed, matrix-valued, supertrace, or nonlocal cancellations.

# Recurrent rigidity and the connector repair

[\[lem:disjoint\]]{#lem:disjoint label="lem:disjoint"} Under the literal ledger and [\[eq:free\]](#eq:free){reference-type="eqref" reference="eq:free"}, every atom cycle is simple and two distinct atom cycles share no vertex.

If distinct cycles meet, rotate their edge words $x,y$ at a shared vertex and write $xy=w^m$ with $w$ primitive. The literal ledger identifies $w$ with some $\gamma_d$. Roof additivity gives $N(a)N(c)=N(d)^m$, contradicting [\[eq:free\]](#eq:free){reference-type="eqref" reference="eq:free"}. If one atom cycle repeats a vertex before closing, split it there into nonempty closed words and take their primitive roots. The same argument yields $N(a)=N(c)^mN(d)^n$, another forbidden exponent relation.

[\[lem:scc\]]{#lem:scc label="lem:scc"} Every recurrent strongly connected component is exactly one atom cycle.

Suppose one component contains distinct atom cycles $\gamma_a$ and $\gamma_c$. They are vertex-disjoint by [\[lem:disjoint\]](#lem:disjoint){reference-type="ref" reference="lem:disjoint"}. Choose any path $\alpha$ from an attachment vertex of the first cycle to one on the second, and any path $\beta$ back. The closed word $$W=\gamma_a\alpha\gamma_c\beta$$ has a primitive root $w$. Since $W=w^m$, $W$ and $w$ have identical edge support. The ledger identifies $w$ with an atom cycle. Because it meets $\gamma_a$, [\[lem:disjoint\]](#lem:disjoint){reference-type="ref" reference="lem:disjoint"} forces equality with $\gamma_a$; yet $w$ also contains an edge of $\gamma_c$, a contradiction. Every extra edge in a recurrent component lies on a closed walk and yields the same argument.

No shortest-path or interior-avoidance normal form is used. This distinction is essential. The preregistered finite proxy required both connectors to avoid both cycles internally and failed on $18{,}272$ examples. The repaired statement asks only for mutual reachability, which is exactly what a strongly connected component supplies.

The argument is graph-theoretic and independent of weights. Positivity enters later, when a literal orbit statement is converted into a trace statement without cancellation.

# Exact pruning and operator ownership {#sec:pruning}

Let $V_c$ be the union of atom-cycle vertices. Permute each cycle forward and fix all other vertices, obtaining a unitary $U$. If $E_{\rm diag}$ is the diagonal conditional expectation, then $$D_\sigma=E_{\rm diag}(U^*L_\sigma),\qquad C_\sigma=UD_\sigma.$$ Contractivity of $E_{\rm diag}$ on trace class gives $\|C_\sigma\|_1\le\|L_\sigma\|_1$.

Every diagonal coefficient of $L_\sigma^r$ is a sum over length-$r$ closed walks based at that vertex. Each edge of a closed walk lies in a recurrent component, so [\[lem:scc\]](#lem:scc){reference-type="ref" reference="lem:scc"} puts the walk entirely on one atom cycle. Consequently the diagonal coefficients of $L_\sigma^r$ and $C_\sigma^r$ coincide. Summing proves [\[eq:trace-equality\]](#eq:trace-equality){reference-type="eqref" reference="eq:trace-equality"}. The trace-class identity $$\log\det(I-zL)=-\sum_{r\ge1}\frac{z^r}{r}\mathop{\mathrm{Tr}}L^r$$ first gives equality near $z=0$, and entireness extends it to all $z$. A weighted cycle of length $\ell(a)$ has determinant $$1-z^{\ell(a)}\prod_{e\in\gamma_a}e^{-\sigma\tau(e)}
=1-z^{\ell(a)}N(a)^{-\sigma},$$ which proves [\[eq:rawdet\]](#eq:rawdet){reference-type="eqref" reference="eq:rawdet"}.

The conclusion is stronger than pruning a finite nilpotent branch: any edge outside the recurrent core is invisible, even if infinitely many such edges feed into or leave cycle vertices. But trace-class ownership is conditional. If the whole operator is not trace class, the formal orbit product is not thereby an ordinary Fredholm determinant.

The terminal control makes the meaning transparent. For $$L=\begin{pmatrix}0&0\\ c&x\end{pmatrix}
\quad(c,x>0),
\qquad \det(I-zL)=1-zx.$$ Deleting the feed state changes neither a power trace nor the determinant. A recognizer followed by accept-loop orbitification can therefore implement any decidable support, but the periodic ledger records the terminal output convention rather than recurrent computation.

# Finite visibility and clock dilution

Let $M_J=\max_{j\le J}\ell(a_j)$. There are fewer than $$W_b(L)=\sum_{r=1}^L b^r<\frac{b^{L+1}}{b-1}$$ nonempty words of length at most $L$, and no more cyclic words. Separation therefore implies $J\le W_b(M_J)$, hence for all large $J$, $$M_J\ge\frac{\log J}{2\log b}.$$ At every record index $J$, $\ell(a_J)=M_J$. Combining this with $\log N(a_J)\le\kappa\log J$ gives [\[eq:length\]](#eq:length){reference-type="eqref" reference="eq:length"} on an infinite subsequence.

Choose on each such cycle an edge $e_a$ of minimum roof. By the exact total clock, $$\tau(e_a)\le \frac{\log N(a)}{\ell(a)}\le2\kappa\log b,
\quad
e^{-\sigma\tau(e_a)}\ge b^{-2\kappa\sigma}.$$ The source vertices $u_a=o(e_a)$ lie on distinct private cycles, so $\delta_{u_a}$ is orthonormal and weakly null. Positivity yields $$\|L_\sigma\delta_{u_a}\|_2\ge b^{-2\kappa\sigma}.$$ A compact operator sends a bounded weakly null sequence to a norm-null sequence. Thus a bounded $L_\sigma$ is noncompact and cannot belong to any finite Schatten class.

The finite alphabet and orbit separation do real work. If one private two-cycle is supplied per prime, with both roofs $(\log p)/2$, the recurrent direct sum is compact for every $\sigma>0$ and trace class for $\sigma>2$. Its factor is $1-z^2p^{-s}$, however, and an infinite visible inventory has been hidden in vertex names. A countable one-symbol-per-prime diagonal also escapes, but is exactly a supplied atom inventory.

The proof is elementary; general weighted-shift theory supplies a broader context [@JablonskiJungStochel2012]. We claim only its consequence for the frozen logarithmic clock.

# First return and the free-marker firewall

Choose one base vertex on each private cycle. One induced step traverses the whole cycle and has weight $$\prod_{e\in\gamma_a}e^{-s\tau(e)}=e^{-sT(\gamma_a)}=N(a)^{-s}.$$ Thus $R_se_a=N(a)^{-s}e_a$, and where $\sum_aN(a)^{-\operatorname{Re}(s)}<\infty$ it is trace class with determinant [\[eq:induced\]](#eq:induced){reference-type="eqref" reference="eq:induced"}. This is a valid operator.

It is not the original edge-step object. The exact local comparison is $$\label{eq:marker-pair}
\underbrace{1-z^{\ell(a)}N(a)^{-s}}_{\text{raw graph steps}},
\qquad
\underbrace{1-zN(a)^{-s}}_{\text{one return step}}.$$ Setting $z=1$ forgets the distinction. As free-marker germs they agree only when $\ell(a)=1$. More generally, if a positive raw determinant equals $\prod_a(1-zN(a)^{-\sigma})$ at one absolutely convergent real $\sigma$, the coefficient of $z$ forces every atom orbit to have length one. A finite alphabet has only finitely many one-letter cyclic words, contradicting infinite separation.

This is a noncommuting ownership square: one may preserve the original marker and lose whole-operator compactness, or induce to a trace-class diagonal and change time. Equality after $z=1$ does not make the two routes the same object.

# Exact adversarial audit

The computation was frozen before canonical execution and uses only exact integer, rational, and symbolic arithmetic. Candidate generation and the independent evaluator use different algorithms: Tarjan SCCs versus transitive-closure SCCs, DFS cycles versus vertex-permutation cycles, period-divisor roots versus coordinate-period roots, and Newton identities versus direct recurrent-block reconstruction.

\@L0.34Y r@ Gate & Interpretation & Exact outcome\
All loop-allowed digraphs, $n\le4$ & exhaustive, not sampled & $66{,}066$ graphs\
Shared-state mixed roots & exhaustive within that census & $613{,}996/613{,}996$\
Repaired connector roots & arbitrary mutual SCC paths & $161{,}475/161{,}475$\
Seeded $n=5,\dots,8$ controls & finite, explicitly nonexhaustive & $69{,}073/69{,}073$\
Strict connector proxy & preregistered normal form & $18{,}272$ failures\
Terminal compiler & $126$ recurrent, $34$ acyclic states & exact pruning\
Kraft/clock & $12$ configurations & $6{,}141$ rows, $0$ failures\
Raw/induced marker & one factor per frozen atom & $17/17$ differ, agree at $z=1$\

The repaired mixed-root audit totals $844{,}544/844{,}544$ certificates with no true failure. The failed strict proxy remains in the public artifact ledger: $24$ failures on three vertices, $17{,}952$ on four vertices, and $296$ among the seeded controls. This is evidence for theorem repair, not a discarded inconvenience.

The terminal graph has $160$ states, of which $126$ are recurrent and $34$ are acyclic decision states. Newton reconstruction equals the product of the $17$ recurrent cycle factors. Across eight post-freeze inventories, every proper nonempty support pruning changes the determinant. Signed and matrix controls deliberately lie outside the theorem: a signed three-state nilpotent recurrent matrix has determinant one, and orthogonal matrix branches can annihilate mixed products while retaining pure ones.

The canonical authority run contains $76/76$ passing tests. Two cleared fresh-result runs produced $19/19$ byte-identical artifacts with aggregate SHA-256 `ae0aa6d1767bb207d0096df149224995bfb40aba674367a2f300668bfdd88c02`. The final result ledger contains $41$ entries; its ledger-file SHA-256 is `6ffbbee5ce1e2a20f0fb00839b89981293c25a8eca2a0995ed384e7448dc7591`. The sealed package additionally checks LF-only text, exact terminal newlines, absence of cache and timestamp fields, Route schema, source separation, and result-set equality.

# Route closure and conclusion

The exact statements are mathematically positive, but the candidate route is negative. The frozen Route-A tuple is $$\texttt{(A0\_STRUCTURAL\_ARITHMETIC\_RELATION,
A1\_FAIL, A2\_FAIL, A3\_FAIL, A4\_FAIL)}.$$ A0 receives only structural credit: multiplicative freeness and the logarithmic roof are source-derived. A1 fails because shared recurrence is incompatible with a literal atom-only primitive ledger. A2 fails because the primary whole operator is noncompact under finite visible separation; the induced determinant belongs to a changed marker. A3 and A4 fail because the mechanism is generic for any multiplicatively free atom inventory and does not provide a spectral carrier. Overall: $$\texttt{ROUTE\_A\_REJECTED},\qquad
\texttt{ROUTE\_B\_LOCKED}.$$

The theorem closes a compiler interface, not Symbolic Dynamics as a research family. Its sharp controls identify the open boundaries: signed or matrix-valued trace cancellation, infinite visible alphabets, nonlocal orbit actions, and operator-algebraic constructions require new theorems.

The next paper will test the $\mathbb N\rtimes\mathbb N^\times$ and Bost--Connes benchmarks without importing their diagonal partition function as a periodic ledger. It must freeze a graph-step marker and ask, before any prime label is read, whether positive semigroup motion is acyclic, whether symmetrization creates universal backtracking or relation cycles, and whether the owned operator is genuinely the same symbolic object. Until those gates are passed, $\zeta(\beta)$ as a partition function is not evidence for a prime-selective recurrent compiler.

# Proof details and analytic continuation boundaries

This appendix records two points that are easy to lose in a compressed presentation.

## Trace-class extraction

The diagonal conditional expectation is contractive on $\mathcal S_1$. Therefore the cyclic extraction $C_\sigma=UD_\sigma$ used in [6](#sec:pruning){reference-type="ref" reference="sec:pruning"} is trace class whenever $L_\sigma$ is. No assertion is made when the latter is merely formal. If $s\mapsto L_s$ is trace-norm holomorphic on a connected domain containing a real interval, the extraction is bounded linear and hence trace-norm holomorphic; determinant equality on the real interval then extends by the identity theorem. This does not create continuation beyond the proved trace-class domain.

## Why the primitive root retains both cycles

For a nonempty directed word $W$, let $w$ be its primitive root, so $W=w^m$. Every occurrence of every edge of $W$ lies in one of the repeated copies of $w$, and every edge in $w$ occurs in $W$. Thus $\mathop{\mathrm{supp}}(W)=\mathop{\mathrm{supp}}(w)$. Directed words have no cancellation. Consequently the paths in [\[lem:scc\]](#lem:scc){reference-type="ref" reference="lem:scc"} may revisit either atom cycle; no internal-disjointness or shortest-path hypothesis is needed.

## Coefficientwise marker test

At an absolutely convergent real $\sigma$, the coefficient of $z$ in the raw connected ledger is $$\sum_{a:\ell(a)=1}N(a)^{-\sigma},$$ whereas the induced target coefficient is $\sum_aN(a)^{-\sigma}$. Positivity makes equality possible only when the complement is empty. This is why a cancellation-based signed or supertrace model lies outside the theorem.

# Scope declarations and sharp controls

-   A disjoint union of one prescribed cycle per desired length realizes an arbitrary primitive inventory. It violates source-visible finite coding or simply hardwires the inventory.

-   A one-way connector between two private cycles creates no mixed closed word. Mutual return, not mere attachment, is the hypothesis of [\[lem:scc\]](#lem:scc){reference-type="ref" reference="lem:scc"}.

-   With signed scalar weights, the strongly connected matrix $$\begin{pmatrix}0&u&-u\\1&0&0\\1&0&0\end{pmatrix}$$ is nilpotent and has determinant one. The underlying mixed primitive words still exist, but their trace contributions cancel.

-   Matrix-valued, graded, homological, and supertrace models are not classified. Orthogonal branch products give finite counter-controls to an unscoped scalar conclusion.

-   Negative finite edge roofs do not repair the average-roof estimate when the cycle total remains $\log N(a)$; they can instead destroy boundedness. Zero weights destroy the required nonzero orbit product.

-   A local or regularized graph zeta may remain meaningful when the whole vertex adjacency is noncompact. Such an object cannot be called its ordinary Fredholm determinant without a separate ownership theorem.

-   No target-zero data, zero locations, critical-line fitting, or Route-B continuation is used anywhere in the construction or audit.

The result is therefore a closed theorem for a deliberately narrow positive compiler class and an open invitation at its signed, matrix-valued, and operator-algebraic boundaries.
