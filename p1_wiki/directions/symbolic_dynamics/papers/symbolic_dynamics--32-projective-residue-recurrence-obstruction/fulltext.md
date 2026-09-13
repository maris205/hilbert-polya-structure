---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--32-projective-residue-recurrence-obstruction"
canonical_tex: "symbolic_dynamics/papers/32-projective-residue-recurrence-obstruction/main.tex"
canonical_pdf: "symbolic_dynamics/papers/32-projective-residue-recurrence-obstruction/main.pdf"
source_sha256: "b6ed5125f9ed6fe5c87e877afed0139fbff33d34dc5751ead7e78fcdc3c9378d"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Projective Residue Recurrence in Symbolic Dynamics: Universal Modular Cycles and Cusp-Diamond Obstructions

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/32-projective-residue-recurrence-obstruction>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/32-projective-residue-recurrence-obstruction/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/32-projective-residue-recurrence-obstruction/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/32-projective-residue-recurrence-obstruction/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/32-projective-residue-recurrence-obstruction/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We test whether a source-natural projective-residue grammar can replace a terminal prime verifier by nonterminal shared recurrence. For every $n\ge2$, the state space is $X_n=P^1(\mathbb Z/n\mathbb Z)$, with two modular transitions $S[a:b]=[-b:a]$ and $R[a:b]=[-b:a+b]$, plus bidirectional cusp edges between $n$ and $2n,3n$. The construction has no accept/reject state, and its original uninduced graph-step operator is trace class for $\operatorname{Re}s>2$, so it owns an ordinary Fredholm determinant $\det(I-zB_s)$. Prime selectivity nevertheless fails before weighting: $S^2=R^3=1$ projectively for every prime, prime power, and mixed composite, while every $n$ yields the primitive nonbacktracking cusp diamond $n\to2n\to6n\to3n\to n$. The exact static criterion $|P^1(\mathbb Z/n\mathbb Z)|=n+1$ holds precisely for primes, but using it to delete recurrent blocks is a completed terminal selector. An exact census over 191 moduli finds recurrent support on all 148 composites; 191 matched finite-semiring relabels copy the full construction and 48 random $C_2*C_3$ actions reproduce its universal recurrence. Hence A1 fails while A2 holds analytically. Route A is rejected, Route B remains locked, and the Euclidean/projective-residue recurrence branch is closed.
author:
- Anonymous Authors
bibliography:
- references.bib
date: 'August 15, 2026'
title: |
  Projective Residue Recurrence in Symbolic Dynamics:\
  Universal Modular Cycles and Cusp-Diamond Obstructions
```

## Markdown 正文

# Introduction {#sec:introduction}

An arithmetic periodic-orbit construction can fail even after it computes the intended arithmetic predicate. The decisive question is whether the predicate is expressed by the primitive transition algebra of one stationary system, rather than by a terminal gate that admits selected components. A second, independent question is whether the unchanged graph-step operator owns the trace or determinant used to interpret those orbits. The preceding semiring-verifier construction answered the first question only by a completed Wilson test and failed the second on its full recurrent adjacency. First return repaired the determinant only by changing graph time. The next candidate must therefore be nonterminal, recurrent on shared states, and analytically controlled before any zeta-function interpretation.

Projective residue dynamics is a natural stress test for this obligation. Finite projective lines retain the unit and zero-divisor structure of residue rings, while the modular generators supply recurrence without halting. Projective lines over rings and generalized Farey graphs are classical objects [@blunck2000projective; @jones1991modular; @saniga2007classification]; modular symbolic dynamics also has a mature transfer-operator tradition [@mayer1991thermodynamic; @katok2006symbolic]. These facts make the candidate source-natural and analytically plausible. They do not determine whether its primitive cycles distinguish fields from composite rings.

We freeze one graph simultaneously for all moduli. The block at $n$ is $X_n=P^1(\mathbb Z/n\mathbb Z)$. Every state carries the projective actions of $$S=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
 R=\begin{pmatrix}0&-1\\1&1\end{pmatrix}.$$ The canonical cusps $c_n=[1:0]_n$ are joined in both directions between $n$ and $2n,3n$. There is no accepting or rejecting vertex, and no field flag is consulted when states or edges are created. Within-modulus edges have roof $\log n$; a cross edge between $n$ and $kn$ has roof $\log(kn)$. One free marker $z$ counts each original graph edge.

This graph meets the two architectural requirements that terminal verifiers could not meet. First, the $S$- and $R$-return families share every projective state, and cusp diamonds make distinct moduli share recurrent states. Second, the full uninduced operator is trace class on $\operatorname{Re}s>2$. The determinant is therefore ordinary and belongs to the same object whose cycles are being counted, in the sense of classical trace-class determinant theory [@simon1977infinite].

The arithmetic result is negative and occurs before this analytic success. Direct multiplication gives $S^2=R^3=-I$. Scalar $-I$ is projectively trivial, so every block, including every prime-power and mixed-composite block, has both return families. Bidirectional cusp edges create a second universal obstruction: $$c_n\longrightarrow c_{2n}\longrightarrow c_{6n}
 \longrightarrow c_{3n}\longrightarrow c_n.$$ This is a simple primitive nonbacktracking cycle for every $n\ge2$, and its top modulus is composite. The primitive ledger has therefore failed before weights, determinants, analytic continuation, or zero data can enter.

Projective geometry does expose an exact static discriminator. We prove $$|P^1(\mathbb Z/n\mathbb Z)|
 =n\prod_{p\mid n}(1+p^{-1}),$$ so the count equals $n+1$ exactly at primes. That equality does not alter the frozen recurrence. Multiplying the $n$-block by its indicator instead performs the complete field test before admitting the block. Such a repair is the terminal selector prohibited by the source lock.

The paper makes four concrete contributions.

1.  We construct and audit a nonterminal, marker-distinct and shared-state recurrent grammar derived from the finite-full-shift semiring.

2.  We prove two preweight obstructions: universal $S^2/R^3$ cycles in every modulus and an overlapping primitive cusp-diamond family through composite moduli.

3.  We prove that the same uninduced graph-step operator is trace class and trace-norm holomorphic on $\operatorname{Re}s>2$, so its ordinary Fredholm determinant is analytically honest even though its primitive ledger is arithmetically wrong.

4.  We separate static field recognition from recurrent selectivity and validate that distinction against prime-power, mixed-composite, matched finite-semiring, random-presentation, and bare-UFD controls.

The resulting route tuple is $$\begin{aligned}
 (&\texttt{A0\_STRUCTURAL\_ARITHMETIC\_RELATION},
   \texttt{A1\_FAIL},\\
  &\texttt{A2\_ANALYTIC\_DETERMINANT},
   \texttt{A3\_FAIL},
   \texttt{A4\_FAIL}).
 \end{aligned}$$ The value of the result lies in separating two failure modes that had previously coincided: analytic ownership is repaired, yet arithmetic primitive separation fails earlier and for a theorem-visible reason.

fixes the classical context and source boundary. derives the projective count, [\[sec:modular-cycles,sec:cusp-diamonds\]](#sec:modular-cycles,sec:cusp-diamonds){reference-type="ref" reference="sec:modular-cycles,sec:cusp-diamonds"} prove the two cycle floods, and [6](#sec:fredholm){reference-type="ref" reference="sec:fredholm"} establishes same-object determinant ownership. analyze the forbidden repair and controls. records the strict route decision.

# Literature context and source boundary {#sec:literature-source}

## Classical ingredients and the paper-specific question

The projective line over a ring can be defined through admissible or unimodular pairs modulo unit scaling. Its functorial geometry is developed systematically by @blunck2000projective, while finite examples expose how zero divisors change incidence and distantness [@saniga2007classification]. We use only the elementary commutative-ring case $P^1(\mathbb Z/n\mathbb Z)$ and prove the required count directly. The state space itself is not a novelty claim.

The projective actions of order two and three belong to the modular-group and Farey-graph setting. Generalized Farey graphs encode modular actions on finite quotients [@jones1991modular], and symbolic codings for the modular surface connect continued fractions, geodesic dynamics, and cross-sections [@katok2006symbolic]. Our use is deliberately adversarial: universal modular relations are tested as a candidate arithmetic recurrence mechanism, then shown to reproduce composite cycles.

Transfer operators for modular and Farey systems already produce Fredholm-determinant descriptions of Selberg or Ruelle zeta functions. @mayer1991thermodynamic gives the foundational modular-surface construction; @chang2001extension treats general modular groups with finite-dimensional representation data; and @bonanno2014thermodynamic develops a two-variable Farey-map formalism. These are the closest analytic ancestors. We do not identify our determinant with a Selberg, Ruelle, or Riemann zeta function. Instead, we ask whether the all-modulus graph-step operator itself belongs to the trace class and what arithmetic classes its owned traces contain.

L0.23YY Ingredient & Paper-specific use & Claim boundary\
Projective lines over rings & Source-derived state spaces $X_n$ and static field defect & State space and count are classical\
Modular/Farey actions & Nonterminal shared-state recurrence and generic presentation control & Relations $S^2=R^3=1$ are classical\
Transfer determinants & Same-object trace-class test for the frozen all-modulus graph & No Selberg/Ruelle/Riemann identity is claimed\
Trace-class determinants & Ordinary meaning of $\det(I-zB_s)$ & No regularized or formal product is substituted\

Within the documented search through August 15, 2026, we found no directly comparable paper combining the frozen semiring-source grammar, a complete preweight composite-cycle audit, and ordinary Fredholm ownership of the same uninduced object. This is a search-bounded positioning statement, not an absolute priority claim. Chang--Mayer is the nearest analytic collision; the present contribution is the controlled obstruction, not the classical modular machinery.

## Finite-full-shift source

Let $$F_n=(A_n^{\mathbb Z},\sigma_n),\qquad n\in\mathbb N_0,$$ denote the conjugacy class of the full shift on an $n$-symbol alphabet. The source retains the operations $$F_m\mathbin{\boxplus}F_n\cong F_{m+n},\qquad
 F_m\mathbin{\boxtimes}F_n\cong F_{mn},$$ the zero $F_0$, unit $F_1$, successor, source equality, quotient/remainder, congruence, and entropy $h(F_n)=\log n$ for $n\ge1$. Alphabet sum is an operation on full-shift classes; no categorical coproduct claim is required.

For each $n\ge2$, source congruence reconstructs $\mathcal R_n=\mathbb Z/n\mathbb Z$. Units, additive inverse, unimodular pairs, and projective classes are defined by source equations. Constants 2 and 3 are generated from the unit, and $[1:0]$ is a source-defined projective point. Consequently the state and edge formulas below are invariant under any isomorphism that transports the complete semiring/congruence presentation.

[\[conv:source-natural\]]{#conv:source-natural label="conv:source-natural"} A candidate is source-natural only if an isomorphic relabeling transports every operation, relation, state, edge, roof, and marker. Exact matched-clone agreement is required and is not counted as evidence of arithmetic selectivity.

## Information boundary and evaluation order

The candidate may use the source operations, exact finite-ring arithmetic that implements them, the two fixed matrices, cusp, frozen roofs, deterministic cutoffs and seeds, and evaluator-only labels applied after enumeration. It may not use a supplied prime, factor, prime-power, accepted-support, orbit-projector, or target-zero table. Candidate-side primality or factorization calls, fitted coefficients, Riemann-zero ordinates, root matching, and Route B are excluded.

The evaluation order is load-bearing. We first freeze the transition graph, then prove its complete primitive support, then run clone and random-action controls, and only afterward study operator class and determinants. The static equality $|X_n|=n+1$ may be reported as a source fact, but it may not decide which blocks or edges exist. This order prevents an exact primality test from being renamed as emergent periodic structure.

# Projective residue states and static field separation {#sec:projective}

For $n\ge2$, a pair $(a,b)\in\mathcal R_n^2$ is unimodular if there exist $u,v\in\mathcal R_n$ such that $ua+vb=1$. Define $$X_n=P^1(\mathcal R_n)
 =\{(a,b):\mathcal R_na+\mathcal R_nb=\mathcal R_n\}/\mathcal R_n^\times,$$ where a unit acts by simultaneous multiplication of both coordinates.

This definition uses no field test. In particular, it is valid for prime powers and mixed composite moduli, where zero divisors alter the geometry. The unit-scaling quotient is also compatible with a transported semiring presentation, a property used in [8](#sec:exact-audit){reference-type="ref" reference="sec:exact-audit"}.

[\[lem:prime-power-count\]]{#lem:prime-power-count label="lem:prime-power-count"} For $q=p^a$, $$|P^1(\mathbb Z/q\mathbb Z)|=q+q/p.$$

The ring $A=\mathbb Z/q\mathbb Z$ is local with maximal ideal $pA$. A unimodular pair has at least one unit coordinate. If the second coordinate is a unit, unit scaling gives a unique representative $[t:1]$ with $t\in A$, hence $q$ classes. If the second coordinate is a nonunit, the first is a unit and the class has a unique representative $[1:u]$ with $u\in pA$, hence $q/p$ further classes. The two families are disjoint.

[\[lem:product-projective\]]{#lem:product-projective label="lem:product-projective"} For finite commutative rings $A,B$, $$P^1(A\times B)\cong P^1(A)\times P^1(B).$$

Unimodularity and unit scaling are componentwise over $A\times B$. Passing to equivalence classes gives the bijection.

[\[thm:projective-count\]]{#thm:projective-count label="thm:projective-count"} For every $n\ge2$, $$|X_n|=\psi(n):=n\prod_{p\mid n}\left(1+\frac1p\right).$$

Apply the Chinese remainder theorem to the prime-power factorization of $n$ and combine [\[lem:prime-power-count,lem:product-projective\]](#lem:prime-power-count,lem:product-projective){reference-type="ref" reference="lem:prime-power-count,lem:product-projective"}.

[\[cor:static-field\]]{#cor:static-field label="cor:static-field"} For $n\ge2$, $$|X_n|=n+1\quad\Longleftrightarrow\quad n\text{ is prime}.$$

For $n=p$, [\[thm:projective-count\]](#thm:projective-count){reference-type="ref" reference="thm:projective-count"} gives $p+1$. Conversely, if $n$ is composite and $p\mid n$, then $n/p\ge2$ and $$\psi(n)\ge n(1+1/p)=n+n/p\ge n+2.$$

The defect $$\delta(n):=|X_n|-(n+1)$$ therefore recognizes precisely when the residue ring is a field. This is a real source-level arithmetic distinction, and it escapes the bare multiplicative-UFD clone inherited from the earlier source program. It is not yet a primitive-orbit distinction. Every state and transition in the next section is created without consulting $\delta(n)$; only that frozen ledger can decide A1.

# Universal modular recurrence {#sec:modular-cycles}

Freeze the two matrices $$S=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
 R=\begin{pmatrix}0&-1\\1&1\end{pmatrix}.$$ Both have determinant one over every residue ring and therefore preserve unimodular pairs. Their projective actions are $$S_n[a:b]=[-b:a],\qquad
 R_n[a:b]=[-b:a+b].$$ Every state has both outgoing edges. There is no halting state and no conditional closure rule.

[\[thm:universal-recurrence\]]{#thm:universal-recurrence label="thm:universal-recurrence"} For every $n\ge2$, $$S_n^2=I,\qquad R_n^3=I$$ on $X_n$. Every $x\in X_n$ lies on an $S$-marked primitive orbit of length one or two and an $R$-marked primitive orbit of length one or three.

Direct multiplication gives $$S^2=-I,\qquad
 R^2=\begin{pmatrix}-1&-1\\1&0\end{pmatrix},\qquad
 R^3=-I.$$ Scalar $-I$ multiplies both coordinates by the unit $-1$ and is therefore trivial on projective classes. The least positive return time of $x$ under $S_n$ divides two, while its least positive return under $R_n$ divides three. Each least return word is primitive. The generator labels distinguish the families, and both contain $x$.

The theorem gives the desired kind of recurrence: it is nonterminal, marker-distinct, and overlapping on actual states. It also gives an immediate A1 obstruction. The proof is uniform in $n$ and cannot distinguish a prime from a prime power or a mixed composite.

## Primitive support before roofs

The obstruction is independent of analytic weights. In the labelled path algebra, the words $SS$ and $RRR$ close at every vertex. Some vertices may have a shorter least return, but each vertex still belongs to the primitive cycle of its corresponding permutation orbit. Therefore the primitive support of every composite block is nonempty before a roof is assigned. Changing positive edge weights cannot remove those paths.

The labelled nature of the statement matters. Even if an $S$- and an $R$-orbit share the same vertex sequence in a small block, their edge words remain distinct. This is precisely the shared-state overlap required after Paper 31; it is not a claim that the two permutations generate disjoint cycles.

[\[prop:generic-compiler\]]{#prop:generic-compiler label="prop:generic-compiler"} Let $Y$ be any nonempty finite set with permutations $a,b$ satisfying $a^2=b^3=I$. The labelled action graph has an $a$-return and a $b$-return through every state.

The least return under $a$ divides two and the least return under $b$ divides three. Different generator labels distinguish the words. No residue-ring structure is used.

identifies the exact 'proves too much' control. A random finite $C_2*C_3$ action copies the recurrence property without carrying projective geometry, a field distinction, or an arithmetic source. The finite controls in [8](#sec:exact-audit){reference-type="ref" reference="sec:exact-audit"} realize this logical test with 48 seeded actions. Their role is not to prove the theorem, but to check that the implementation has not smuggled residue labels into a universal relation test.

# Cross-modulus cusp diamonds {#sec:cusp-diamonds}

Within-block recurrence could still be dismissed as a direct sum over moduli. To require shared recurrence across arithmetic scales, choose the source-defined cusp $$c_n=[1:0]_n$$ and connect it in both directions to $c_{2n}$ and $c_{3n}$ for every $n\ge2$. These edges use only multiplication by the fixed source constants 2 and 3. They do not inspect prime or composite labels.

There are two natural orientations. Reduction maps can point from $kn$ down to $n$, reflecting the ordinary residue reduction direction. Alternatively, one may retain both reduction and lift directions to make the cross-modulus graph recurrent. The following proposition shows why neither orientation provides prime-selective periodic data.

[\[prop:orientation-dichotomy\]]{#prop:orientation-dichotomy label="prop:orientation-dichotomy"} If all cross-modulus cusp edges are oriented downward, no closed path uses one. If the edges are bidirectional, then every $n\ge2$ has the simple primitive nonbacktracking cycle $$c_n\to c_{2n}\to c_{6n}\to c_{3n}\to c_n.$$ Its top modulus is composite, and diamonds based at consecutive dyadic scales share cusp states.

A downward cross edge strictly decreases the positive integer modulus, while a within-block edge leaves it unchanged. A closed path cannot contain a strict decrease with no increasing cross edge.

For bidirectional edges, the displayed path uses the operation word $\times2,\times3,\div2,\div3$. Its four moduli are distinct, and no operation immediately reverses its predecessor, including cyclically. A simple closed path cannot be a proper temporal repetition, so the cycle is primitive. The top modulus $6n$ is composite. The diamond based at $2n$ has vertices $2n,4n,12n,6n$ and shares $c_{2n}$ and $c_{6n}$ with the diamond based at $n$.

## Frozen roof and diamond weight

The roof is fixed before evaluating [\[prop:orientation-dichotomy\]](#prop:orientation-dichotomy){reference-type="ref" reference="prop:orientation-dichotomy"}. A within-$n$ edge has roof $\log n$. Either direction of the cusp edge between $n$ and $kn$, for $k\in\{2,3\}$, has roof $\log(kn)$. The four weight bases along the diamond are therefore $$2n,\quad6n,\quad6n,\quad3n,$$ so the weighted cycle contributes $$(2n)^{-s}(6n)^{-s}(6n)^{-s}(3n)^{-s}
 =(216n^4)^{-s}.$$ For positive real $s$, this term is strictly positive. Its existence was proved in the unweighted graph, so the formula records the cycle rather than creating it.

The orientation dichotomy also recovers the pruning lesson in a nonterminal setting. A directed reduction architecture may carry substantial arithmetic information, yet its strictly decreasing states disappear from all periodic traces. Adding the reverse edges restores recurrence but introduces the entire composite-diamond family. For this source-natural cusp skeleton, cross-modulus recurrence is thus either transient or arithmetically flooded.

# Same-object trace class and Fredholm ownership {#sec:fredholm}

The primitive ledger has already failed A1, but Paper 32 also asks whether the analytic ownership obstruction from Paper 31 can be removed. This section keeps every state and every original graph edge. No first return, induced map, or block projection is used.

Let $$\mathcal H=\bigoplus_{n\ge2}\ell^2(X_n).$$ Write $P_{S,n}$ and $P_{R,n}$ for the two permutation operators on $\ell^2(X_n)$. If $c_n$ also denotes its unit basis vector, define the rank-one cusp maps $$J^+_{k,n}=|c_{kn}\rangle\langle c_n|,
 \qquad J^-_{k,n}=(J^+_{k,n})^*,
 \qquad k\in\{2,3\}.$$

[\[def:primary-operator\]]{#def:primary-operator label="def:primary-operator"} For $s\in\mathbb C$, set $$B_s^{\mathrm{mod}}
 =\bigoplus_{n\ge2}n^{-s}(P_{S,n}+P_{R,n}),$$ $$C_s=\sum_{n\ge2}\sum_{k\in\{2,3\}}(kn)^{-s}
 (J^+_{k,n}+J^-_{k,n}),\qquad B_s=B_s^{\mathrm{mod}}+C_s.$$ The marker $z$ counts one application of this exact $B_s$.

[\[thm:trace-class\]]{#thm:trace-class label="thm:trace-class"} The map $s\mapsto B_s$ is trace-norm holomorphic on $\operatorname{Re}s>2$. In particular, $B_s$ is trace class there and $$D_{\mathrm{PR}}(s,z)=\det(I-zB_s)$$ is an ordinary Fredholm determinant of the uninduced graph-step operator, entire in $z$ and holomorphic in $s$.

Each projective generator is a permutation on $\psi(n)$ states and has trace norm $\psi(n)$. For $\sigma=\operatorname{Re}s$, $$\|B_s^{\mathrm{mod}}\|_1
 \le2\sum_{n\ge2}\psi(n)n^{-\sigma}.$$ The factorwise inequality $1+p^{-1}\le1+p^{-1}+\cdots+p^{-a}$ gives $\psi(n)\le\sigma_1(n)$. Hence, for $\sigma>2$, $$\|B_s^{\mathrm{mod}}\|_1
 \le2\sum_{n\ge2}\sigma_1(n)n^{-\sigma}
 <2\zeta(\sigma)\zeta(\sigma-1)<\infty.$$ Every $J^+_{k,n}$ and $J^-_{k,n}$ has trace norm one, so $$\|C_s\|_1
 \le2(2^{-\sigma}+3^{-\sigma})\sum_{n\ge2}n^{-\sigma},$$ which converges for $\sigma>1$. On a compact subset of $\operatorname{Re}s>2$, the same majorants with the minimum real part give uniform trace-norm convergence. Termwise holomorphy then proves trace-norm holomorphy. The standard trace-class determinant construction [@simon1977infinite] yields the remaining assertions.

This theorem is the main positive advance. The primary operator itself owns the determinant, the free marker retains graph-step time, and both within-block and cross-modulus edges enter the trace-norm estimate. The analytic statement does not rely on a formal orbit product.

## What the owned traces contain

For trace-class $B_s$ and sufficiently small $z$, the usual trace-log identity is $$\log\det(I-zB_s)
 =-\sum_{r\ge1}\frac{z^r}{r}\operatorname{Tr}(B_s^r).$$ Its coefficients count the labelled closed walks of the frozen operator with their source roofs. Ownership therefore makes the primitive-ledger failure more, rather than less, consequential.

[\[prop:composite-traces\]]{#prop:composite-traces label="prop:composite-traces"} For real $s>2$, every modulus $n$ contributes positive within-block terms to the trace ledger, and every base modulus contributes a positive primitive cusp-diamond term.

The word $SS$ fixes all $psi(n)$ projective states and contributes $$\psi(n)n^{-2s}$$ to $\operatorname{Tr}(B_s^2)$. Likewise, $RRR$ contributes $\psi(n)n^{-3s}$ to $\operatorname{Tr}(B_s^3)$. The diamond from [\[prop:orientation-dichotomy\]](#prop:orientation-dichotomy){reference-type="ref" reference="prop:orientation-dichotomy"} contributes $(216n^4)^{-s}$ at length four. All matrix entries are nonnegative for real $s$, so these terms cannot cancel.

An ordinary determinant is therefore present, but it encodes universal modular cycles and composite diamonds. The analytic gate A2 passes; the arithmetic primitive gate A1 remains failed. This distinction prevents determinant existence from being used as evidence of prime selectivity.

No claim is made beyond $\operatorname{Re}s>2$. We do not prove meromorphic continuation, a gamma completion, functional equation, explicit-formula correspondence, or critical-line control. Those omissions are recorded as A3 and A4 failures in [9](#sec:route-closure){reference-type="ref" reference="sec:route-closure"}.

# Why static separation is a terminal gate {#sec:terminal-gate}

The source contains enough arithmetic to distinguish fields. The central discipline is to avoid confusing that fact with a recurrent realization. Define the block projector suggested by [\[cor:static-field\]](#cor:static-field){reference-type="ref" reference="cor:static-field"}: $$Q=\bigoplus_{n\ge2}
 \mathbf 1_{\{|X_n|=n+1\}}I_{\ell^2(X_n)}.$$

[\[prop:terminal-projector\]]{#prop:terminal-projector label="prop:terminal-projector"} The coefficient of the $n$-block in $Q$ is the primality indicator. Thus $QB_sQ$ selects prime blocks by a completed static decision and is not the nonterminal candidate of [\[def:primary-operator\]](#def:primary-operator){reference-type="ref" reference="def:primary-operator"}.

By [\[cor:static-field\]](#cor:static-field){reference-type="ref" reference="cor:static-field"}, $\mathbf 1_{\{|X_n|=n+1\}}=1$ exactly when $n$ is prime. The coefficient is computed before the block contributes recurrence. Since [\[thm:universal-recurrence,prop:orientation-dichotomy\]](#thm:universal-recurrence,prop:orientation-dichotomy){reference-type="ref" reference="thm:universal-recurrence,prop:orientation-dichotomy"} already exhibit composite cycles in the unprojected graph, $Q$ removes rather than explains those cycles.

The distinction is semantic only if one ignores the order of construction; under the source lock it is formal. The frozen candidate first creates all states and edges by uniform source equations. The projector first completes the global field test and then decides which recurrent components remain. That is the same selector architecture as a terminal verifier, even though the Boolean is written as a dimension equality instead of an accept edge.

## Naturality does not supply selectivity

[\[prop:matched-transport\]]{#prop:matched-transport label="prop:matched-transport"} An isomorphism of the full semiring/congruence source transports projective states, the $S,R$ actions, cusps, roofs, $B_s$, and $D_{\mathrm{PR}}(s,z)$ exactly.

A semiring isomorphism preserves zero, one, addition, multiplication, units, and the unimodularity equation $ua+vb=1$. It descends to a bijection of projective classes and commutes with the formulas for $S,R$ and $[1:0]$. Constants 2 and 3, cross edges, and roofs are transported. The induced unitary on the direct-sum Hilbert space conjugates the two graph-step operators, and the Fredholm determinant is invariant under conjugacy.

Matched-clone equality is mandatory evidence of source naturality, not a failed control. It also limits the interpretation of the static field criterion: the criterion is preserved in a matched presentation, but so are all universal composite cycles. Relabelling cannot turn a static predicate into primitive selectivity.

The bare polynomial-UFD clone inherited from the earlier multiplicative source remains outside the enriched source because ordinary polynomial addition cannot transport $2=1+1$. This shows only that alphabet sum breaks that precise bare clone. It does not establish a universal separation from matched semiring presentations, and we make no such claim.

## Claim boundary

The obstruction applies to the frozen projective-residue graph and its source-natural static projector. It does not classify every signed, supersymmetric, homological, or representation-theoretic quotient. A cycle-level quotient might annihilate universal relation cycles without testing $|X_n|=n+1$ block by block. Such a quotient must be proved before weights and must survive the same matched and random-action controls. That narrow unresolved case becomes the Paper 33 obligation; it is not evidence that SD-C34 itself remains open.

# Exact audit and adversarial controls {#sec:exact-audit}

Finite computation verifies the implementation and control separation; it does not substitute for the infinite proofs. The candidate core first constructs every projective block, the $S,R$ permutations, labelled trace counts, cusps, and diamonds. Only the independent runner subsequently labels a modulus as prime, prime-power composite, or mixed composite. The core has no primality or factorization routine and no target-zero, network, or process interface.

The frozen range is $2\le n\le192$, with labelled traces through order eight, 48 seeded random presentation controls, one seeded matched semiring relabel per modulus, and all canonical diamonds whose four vertices remain within the cutoff. The graph, roofs, and seeds were fixed before the evaluator labels were applied.

Y r Audit surface & Exact result\
Moduli $2,\ldots,192$ & 191\
Prime moduli & 43\
Prime-power composites & 14\
Mixed composites & 134\
All composites & 148\
Static field-defect equivalence & 191/191\
Prime blocks with recurrent support & 43/43\
Composite blocks with recurrent support & 148/148\
Matched finite-semiring transports & 191/191 exact\
Seeded random $C_2*C_3$ actions & 48/48 recurrent\
Canonical diamonds within cutoff & 31\
Diamonds with composite top modulus & 31/31\
Deterministic tests & 13/13 pass\
Independent evaluator checks & 4,819,026/4,819,026 pass\
Fresh repeat runs & 16/16 artifacts byte-identical\
Final-tree integrity audit & PASS\

## Prime, prime-power, and mixed-composite strata

The static defect agrees with the independent prime label on all 191 rows, as [\[cor:static-field\]](#cor:static-field){reference-type="ref" reference="cor:static-field"} predicts. That success remains isolated in the evaluator. Recurrent support is nonzero for all 43 primes and all 148 composites. Separating composites into 14 prime powers and 134 mixed composites makes clear that the failure is not confined to squarefree rings or to one zero-divisor pattern. Every state participates in both labelled return families, exactly as [\[thm:universal-recurrence\]](#thm:universal-recurrence){reference-type="ref" reference="thm:universal-recurrence"} states.

The 31 displayed cusp diamonds cover bases $2\le n\le32$. All have top modulus $6n$ composite, and every weight-base product equals $216n^4$. The finite count is cutoff-dependent; the theorem supplies a diamond for every $n\ge2$.

## Genuine matched finite-semiring clones

For each modulus, the matched control applies a seeded opaque permutation to the residue labels. It transports zero, one, the complete addition and multiplication tables, additive inverse, projective equivalence, and the $S,R$ graph. The projective census is recomputed in the transported presentation rather than copied as a summary. All 191 semiring transports, graph transports, and complete census hashes agree exactly.

This agreement is the required naturality result from [\[prop:matched-transport\]](#prop:matched-transport){reference-type="ref" reference="prop:matched-transport"}. A candidate that failed the matched control would depend on printed residue labels. A candidate that passes it has not thereby acquired prime selectivity: the matched clone copies both the static field criterion and the composite recurrent flood.

## Random presentation controls

Each random control chooses finite permutations $a,b$ with $a^2=b^3=I$ but without a residue ring. All 48 controls have nonzero $a$- and $b$-recurrent families through the sampled states. This realizes [\[prop:generic-compiler\]](#prop:generic-compiler){reference-type="ref" reference="prop:generic-compiler"}: the within-block recurrence follows from the presentation relations alone. The control does not imitate the cusp arithmetic or projective count; it isolates exactly the mechanism that was being credited as recurrence.

## Bare-UFD and reproducibility controls

The inherited bare polynomial-UFD monomial presentation cannot transport ordinary alphabet addition, since it would require the prime indeterminate for 2 to equal $1+1$. This remains a scoped separation from that bare clone, not a failure of the matched semiring clone.

The source-oracle scan finds no forbidden token or import in the candidate core. The independent evaluator imports no candidate module and passes all 4,819,026 checks, including 2,377,759 complete addition-table entries, 2,377,759 complete multiplication-table entries, and 56,318 projective edges. Thirteen deterministic tests cover the projective relations, orbit partitions, static defect, recurrent support, clone transport, random controls, diamond weights, and source boundary. Two fresh executions reproduce all 16 primary artifacts byte for byte, with aggregate SHA-256 `3cc4d3bddb5e771c5b2621110e9499b169359438d88608c36f8dc615ce73c727`. The final-tree integrity audit reports `PASS`. Canonical hashes are recorded in the source lock and [12](#app:scope){reference-type="ref" reference="app:scope"}.

The audit cannot prove absence of every coding error beyond its assertions, and a larger cutoff would add rows without strengthening the infinite theorems. Its evidential role is narrower: verify that the implementation matches the frozen formulas and that the adversarial controls are evaluated on the same object.

# Strict Route-A evaluation and branch closure {#sec:route-closure}

The route gates are applied in their preregistered order. An analytic determinant cannot repair an incorrect primitive ledger, and a static source predicate cannot be promoted to recurrence after the fact.

L0.10L0.32Y Gate & Verdict & Decisive evidence\
A0 & structural arithmetic relation & Residue rings, projective states, and the exact static field defect are source-derived; a matched source presentation transports them.\
A1 & `A1_FAIL` & $S^2/R^3$ cycles occur in every block and every $n$ has a primitive composite cusp diamond before weights.\
A2 & analytic determinant & The unchanged $B_s$ is trace class and trace-norm holomorphic for $\operatorname{Re}s>2$; it owns $\det(I-zB_s)$.\
A3 & `A3_FAIL` & No critical-line continuation, completion, functional equation, explicit-formula bridge, or intrinsic Weil compression is obtained.\
A4 & `A4_FAIL` & No fixed self-adjoint Hilbert--Pólya carrier, critical-line mechanism, or zero correspondence is produced.\

## A0: structural arithmetic without clone evasion

The full-shift semiring and congruence reconstruct residue-ring operations, units, unimodular pairs, and the projective count. This is more arithmetic structure than a bare multiplicative monoid. A matched semiring clone copies it by construction, as naturality requires. A0 is therefore recorded as a structural arithmetic relation, not as an intrinsic presentation theorem.

## A1: primitive separation fails

The failure is complete before the roof is considered. All prime powers and mixed composites contain modular relation cycles. Cross-modulus recurrence adds a primitive mixed cycle with composite top modulus for every base $n$. Positive roofs preserve these cycles and place positive terms in owned power traces. The static projector would remove them only by deciding primality first. A1 therefore fails rather than receiving partial credit.

## A2: analytic ownership succeeds

Unlike the long terminal cycles in the preceding construction, each projective block has finite dimension $psi(n)$ and receives the summable block factor $n^{-s}$. Cross-modulus edges form a summable rank-one family. The resulting trace-class theorem applies to the same uninduced operator with one $z$ per original edge. This is a genuine A2 success and is retained as the main positive technical result.

## A3 and A4: unavailable downstream mechanisms

Trace-class holomorphy on one right half-plane gives neither a zeta completion nor a spectral theorem. The determinant contains the wrong primitive support and has no established functional equation or explicit-formula interpretation. No fixed self-adjoint operator is constructed, and no target zeros are used. A3 and A4 fail; Route B is not invoked.

The overall verdict is $$\boxed{\texttt{ROUTE\_A\_REJECTED}}.$$ The negative obstruction paper proceeds, the positive prime-selective candidate stops, and the branch action is $$\boxed{\texttt{CLOSE\_EUCLIDEAN\_PROJECTIVE\_RESIDUE\_RECURRENCE\_BRANCH}}.$$ Changing to another fixed residue map without a cycle-level selectivity theorem does not reopen the branch.

# Conclusion {#sec:conclusion}

Projective residue dynamics supplies the architecture that a terminal semiring verifier lacked. The grammar has no accept/reject state, its two labelled recurrent families share every projective state, cusp edges make different moduli share recurrence, and the original graph-step operator owns an ordinary Fredholm determinant on $\operatorname{Re}s>2$. These properties make the candidate a useful positive test of same-object analytic ownership.

The same construction gives a decisive arithmetic obstruction. Universal projective relations create recurrence in every composite block, and bidirectional cusp coupling produces a primitive composite diamond for every base modulus. The exact projective count recognizes primes only as a static field criterion. Turning that equality into prime-only recurrence requires a completed block selector and returns to the terminal architecture already closed. The strict outcome is therefore A1 failure together with genuine A2 analytic success.

The result has a narrow but useful scope. It does not show that every semiring grammar fails, nor does it classify signed or homological cancellations. It gives no continuation, functional equation, Weil criterion, critical-line theorem, self-adjoint spectral carrier, or RH consequence. The finite audit checks the frozen implementation through $n=192$; the infinite conclusions rest on direct proofs rather than the cutoff.

One in-family question remains. A source-natural cycle quotient might kill the presentation boundaries generated by $S^2$, $R^3$, and the cusp diamonds without inserting the static field projector. Such a construction must be defined on the same recurrent object, fix its signs before arithmetic labels, prove the complete surviving primitive ledger, fail on prime-power, mixed-composite and random-action controls for a theorem-visible reason, and retain same-object determinant ownership. If universal cycles survive, the quotient works equally on random actions, or the quotient is equivalent to $\mathbf 1_{\{|X_n|=n+1\}}$, the entire semiring-residue family should close.

## Data and code availability {#data-and-code-availability .unnumbered}

The theorem proofs, derivations, source lock, figure sources, exact audit summary, and SHA-256 research provenance accompany this manuscript. The candidate core, canonical repository artifacts, independent evaluation, double-run certificate, integrity audit, and their frozen ledgers are identified in the source lock. Those integration artifacts are maintained by the integration layer and were not modified by the manuscript writer.

## Ethics declaration {#ethics-declaration .unnumbered}

This theoretical and deterministic computational study uses no human participants, personal data, animals, or sensitive datasets. No institutional ethics approval was required.

## Author contributions {#author-contributions .unnumbered}

The anonymous authors contributed to conceptualization, formal analysis, methodology, software, validation, visualization, writing, and reproducibility documentation. Named CRediT assignments can be supplied for a camera-ready version.

## Conflict of interest {#conflict-of-interest .unnumbered}

The authors declare no conflict of interest.

## Funding {#funding .unnumbered}

No external funding was reported for this study.

## AI-assisted research disclosure {#ai-assisted-research-disclosure .unnumbered}

AI-assisted tools supported literature-query formulation, proof and derivation organization, deterministic prototype drafting, figure layout, and manuscript preparation. DOI metadata, numerical claims, source boundaries, proofs, and compiled artifacts were checked against the frozen research package and exact outputs. No target-zero data or model-generated experimental observations were used.

# Expanded proof details {#app:proofs}

## Projective representatives over local factors

Let $A=\mathbb Z/p^a\mathbb Z$. If $[x:y]$ is unimodular and $y$ is a unit, scaling by $y^{-1}$ produces $[xy^{-1}:1]$. Uniqueness follows because a unit fixing the second coordinate 1 must be 1. If $y$ is not a unit, unimodularity forces $x$ to be a unit. Scaling produces $[1:yx^{-1}]$, and the second coordinate lies in the maximal ideal $pA$. Conversely, every point in either displayed family is unimodular. Their union is disjoint and exhaustive, which proves $p^a+p^{a-1}$ without a field assumption.

For $A\times B$, a row $((a_1,b_1),(a_2,b_2))$ is unimodular exactly when $(a_1,a_2)$ and $(b_1,b_2)$ are unimodular. The unit group is $A^\times\times B^\times$, so the quotient is componentwise. Iterating this bijection across the Chinese-remainder factors gives $$|P^1(\mathbb Z/n\mathbb Z)|
 =\prod_{p^a\parallel n}(p^a+p^{a-1})
 =n\prod_{p\mid n}(1+p^{-1}).$$

## Primitive status of relation orbits

For a permutation $T$ of a finite set and a point $x$, let $d$ be the least positive integer with $T^dx=x$. The cyclic word $T^d$ is primitive: if it were a proper repetition of a shorter return word, that shorter word would contradict minimality. Applying this observation to $S_n^2=I$ and $R_n^3=I$ gives primitive orbit lengths in $\{1,2\}$ and $\{1,3\}$ respectively. Fixed points are legitimate primitive loops; nonfixed points lie on the corresponding 2- or 3-cycle.

The labelled graph distinguishes $S$ and $R$. Thus a shared state belongs to two marker families even when a small quotient makes their underlying vertex sets overlap unusually. The conclusion is a statement about labelled primitive support, which is the ledger used by powers of $P_{S,n}+P_{R,n}$.

## Cyclic nonbacktracking check for the cusp diamond

The modulus sequence $n,2n,6n,3n$ has four distinct entries for $n>0$. Consecutive operations are $$\times2,\quad\times3,\quad\div2,\quad\div3.$$ The inverse of each operation is not the next operation, and the inverse of the final $\div3$ is $\times3$, not the first $\times2$. Hence the path is nonbacktracking even at the cyclic boundary. Simplicity rules out a proper temporal power. Neighboring diamonds overlap without identifying all four vertices, so their recurrence is shared rather than duplicated as disjoint components.

## Trace-norm holomorphy

Fix a compact set $K\subset\{s:\operatorname{Re}s>2\}$ and choose $\sigma_K=\inf_{s\in K}\operatorname{Re}s>2$. For the within-block summands, $$\sup_{s\in K}\|n^{-s}(P_{S,n}+P_{R,n})\|_1
 \le2\psi(n)n^{-\sigma_K}.$$ The sum of these majorants is finite. For the cusp summands, $$\sup_{s\in K}\|(kn)^{-s}(J^+_{k,n}+J^-_{k,n})\|_1
 \le2(kn)^{-\sigma_K},$$ whose double series is also finite. Each finite-rank summand is entire in $s$, so the Weierstrass theorem in the trace-norm Banach space yields a holomorphic trace-class-valued function. The Fredholm determinant is continuous and holomorphic under trace-norm-holomorphic perturbations, and is entire in the scalar $z$ for each trace-class $B_s$.

## Conjugacy under a matched presentation

Let $\phi_n:\mathcal R_n\to\widetilde{\mathcal R}_n$ transport zero, one, addition, and multiplication. It transports units because $uv=1$ is preserved, and it transports unimodularity because $ua+vb=1$ is preserved. Therefore $$[a:b]\longmapsto[\phi_n(a):\phi_n(b)]$$ is a well-defined bijection of projective states. It commutes with additive inverse and addition, hence with $S_n$ and $R_n$, and sends $[1:0]_n$ to the matched cusp. Taking the direct sum of the induced basis unitaries gives $\widetilde B_s=U B_sU^{-1}$. This proves exact transport of every power trace and Fredholm determinant, not merely equality of a finite census.

## The static projector cannot be generated by the frozen edges

The graph before projection contains every block $X_n$, all $S,R$ edges, and all cusp edges. No edge formula references $|X_n|$. The block coefficient $\mathbf 1_{\{|X_n|=n+1\}}$ is thus external to its transition algebra as frozen. By [\[cor:static-field\]](#cor:static-field){reference-type="ref" reference="cor:static-field"}, computing that coefficient completes the primality decision. Inserting it is a valid projected operator, but it is a different terminally selected object and cannot be used as evidence that the unprojected primitive ledger separated primes.

# Scope, provenance, and reopening rule {#app:scope}

## Frozen research provenance

The mathematical authority is the research package , with SHA-256 `b34dd0489fae5080c683bedcaed6ddcc56025ddad6854da6e786c50c36fa61fb`. The prime-blind candidate core has SHA-256 `e7ad9ff5f515973d4a0d9a991be912961f2b7492dcac7ecf0006bf490c6179cf`, and the independent runner has SHA-256 `cb6b128b9b3ace9cd39cf11ffe4ff02ac077d2bc923470bb61dd41580877616a`. The seven-file payload ledger digest is `f7c2e0f1c1be4bdce325515feb83a80bebfaf36e5785c39b31bcb12d9481d5e6`. These hashes identify the frozen research-stage writer inputs.

The canonical repository result ledger is `689a73a593f1791e6b2f49836b50cc2a11e5ddb1b91c46053af7aaa495ae4b8f`. The independent evaluation, double-run certificate, and integrity audit have SHA-256 digests `0267d31af1f3a476528277b9154219340ac942d52872b305928d1c5d2311d66e`, `b3dc8cb3c4cd16cdbbc0a04c4f2b3dddaac65c714c8ba9e92c986cb931829afd`, and `48d0d153dae72e2131e36c0fb2cdfe076dd007439e25c3357bd9eae39cc63df0`, respectively. The experiment report and strict Route-A YAML have digests `acafeb77e0c8a8272ae92dab7fdacc26fde11d73050506eda35423095ce06ce6` and `304a0084773c0896d29acbb19c0101fb2273bbe16519c9ae8363e3e6aba51530`. These integration artifacts were read but not modified by the manuscript writer.

## Search-bounded novelty

The external search used official DOI/publisher metadata, Crossref, web, and arXiv metadata through August 15, 2026. It targeted projective lines over finite rings, modular and generalized Farey graphs, modular-surface symbolic dynamics, transfer-operator determinants, finite-index modular-group representations, and trace-class determinants. The nearest analytic work is the modular transfer formalism of @mayer1991thermodynamic and its general-group extension [@chang2001extension]. Within this search, no directly comparable controlled trilemma was found. The statement is bounded by the databases, queries, and date; it is not an absolute priority claim.

## Explicit nonclaims

The paper does not prove:

-   that every semiring, residue, signed, graded, or homological grammar fails;

-   a new primality test or a universal clone-separation theorem;

-   equality of $D_{\mathrm{PR}}$ with the Riemann, Selberg, Ihara, or another target zeta function;

-   analytic continuation to the critical strip, a functional equation, a Weil criterion, or a critical-line theorem;

-   a fixed self-adjoint Hilbert--Pólya operator or a zero correspondence;

-   Route-B readiness or any conclusion based on target-zero data.

## Paper 33 reopening rule

Continuation inside the family requires a cycle-level source-natural quotient or twist of the same projective-residue graph. It must annihilate $S^2$, $R^3$, and cusp diamonds before arithmetic labels; fix all coefficients from source symmetries; prove the complete residual primitive ledger; distinguish prime-power, mixed-composite, random-action, and nonisomorphic-ring controls; transport matched clones exactly; and retain determinant ownership with the original marker. A static field projector, surviving universal relation cycle, or cancellation reproduced by random actions closes the entire semiring-residue family.

The final decision ledger is

  --------------------------------------------------------
  `GO_PROJECTIVE_RESIDUE_OBSTRUCTION_PAPER`
  `STOP_PRIME_SELECTIVE_RECURRENT_CANDIDATE`
  `STOP_STATIC_FIELD_DEFECT_PROJECTOR`
  `PROVES_TOO_MUCH_AT_GROUP_PRESENTATION_LEVEL`
  `COMPOSITE_DIAMOND_FLOOD`
  `CLOSE_EUCLIDEAN_PROJECTIVE_RESIDUE_RECURRENCE_BRANCH`
  `ROUTE_A_REJECTED``ROUTE_B_LOCKED`.
  --------------------------------------------------------
