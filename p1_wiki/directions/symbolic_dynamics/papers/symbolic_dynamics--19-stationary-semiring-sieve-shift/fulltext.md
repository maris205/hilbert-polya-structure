---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--19-stationary-semiring-sieve-shift"
canonical_tex: "symbolic_dynamics/papers/19-stationary-semiring-sieve-shift/main.tex"
canonical_pdf: "symbolic_dynamics/papers/19-stationary-semiring-sieve-shift/main.pdf"
source_sha256: "3974975af7c2e69295008cdd506de0e377b22a707745fab87f5565172005d0e4"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Semiring Sieve Shift: Exact Euler Determinant, Recurrent-Core Collapse, and a Factorial-Monoid Compiler No-Go

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/19-stationary-semiring-sieve-shift>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/19-stationary-semiring-sieve-shift/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/19-stationary-semiring-sieve-shift/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/19-stationary-semiring-sieve-shift/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/19-stationary-semiring-sieve-shift/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Finite full shifts carry a positive-integer semiring skeleton: Cartesian alphabet product multiplies cardinalities, disjoint alphabet union adds them, and entropy sends $F_n$ to $\log n$. We use only these operations, successor, and their induced order to build a one-sided countable deterministic Markov shift that executes trial division. Divisibility is not an edge oracle: states $Q_{n,d,q}$ expose the quotient search $q=2,3,\ldots$ until $dq=n$ or $dq>n$. Prime inputs alone reach self-loops $A_p\to A_p$; composites enter acyclic cemetery rays. Entropy-derived positive roofs give one weighted vertex-adjacency $L_s$ on $\ell^2(V)$ that is trace class and $\mathcal S_1$-holomorphic for $\operatorname{Re}s>1$. Its exact orbit ledger is $$\operatorname{Tr}L_s^r=\sum_p p^{-rs},\qquad
  \det(I-zL_s)=\prod_p(1-zp^{-s}),$$ so $\det(I-L_s)=\zeta(s)^{-1}$ in the absolute-convergence half-plane. The positive result is accompanied by a sharp obstruction. Every arithmetic instruction lies in a transient feeding tree; recurrent pruning deletes the entire verifier while preserving all power traces and Fredholm determinants. More generally, a positive exact one-primitive-per-atom ledger forces each recurrent strongly connected component to be a simple cycle. A time-damped wrapper further gives the same determinant construction for every total decidable support, and factorial monoids reproduce their own Euler products. Thus the model is algorithmically non-oracular but dynamically selector-tautological. It earns an exact analytic determinant coordinate, but no continuation, critical-strip structure, self-adjoint realization, or RH consequence; the strict outcome is `ROUTE_A_REJECTED`.
author:
- Anonymous Authors
bibliography:
- references.bib
date: 'August 14, 2026'
title: |
  A Semiring Sieve Shift:\
  Exact Euler Determinant, Recurrent-Core Collapse,\
  and a Factorial-Monoid Compiler No-Go
```

## Markdown 正文

# Introduction {#sec:introduction}

An arithmetic dynamical model should do more than place a desired Euler factor on a diagonal. Its recurrent language should explain why the primitive inventory is arithmetic and why temporal repetitions have the correct powers. This demand is especially severe for the Riemann Euler product. The formal target $$\prod_p(1-p^{-s})$$ is easy to write once the primes have been selected. The harder question is whether one symbolic system can generate the selection, the repetitions, and the determinant without importing a prime table.

Finite full shifts offer a deliberately elementary source. If $F_n$ is the full shift on $n$ symbols, then product alphabets and disjoint alphabet union recover multiplication and addition of cardinalities, while $h(F_n)=\log n$. This skeleton is arithmetically exact and invariant under alphabet relabeling. We ask whether it can drive a countable Markov grammar that computes primality locally and turns the accepted result into periodic orbits.

The answer has an exact positive half. We build a deterministic graph with input states $I_n$, divisor states $T_{n,d}$, quotient states $Q_{n,d,q}$, accepted states $A_n$, and cemetery states $R_{n,k}$. At fixed $d$, the graph does not ask whether a cofactor exists. It constructs $q=2,3,\ldots$ by successor and compares $F_d\boxtimes F_q$ with $F_n$. Equality rejects; strict overshoot advances $d$; passing the square test accepts. Consequently $A_n$ is reached exactly for prime $n$. Positive entropy roofs make the weighted adjacency of the entire unpruned graph trace class for $\operatorname{Re}s>1$. Its only cycles are the accepted self-loops, and the standard trace-class determinant identity [@Simon1977] gives $$\operatorname{Tr}L_s^r=\sum_p p^{-rs},\qquad
\det(I-zL_s)=\prod_p(1-zp^{-s}).$$ This is one operator, not a coordinatewise family assembled after the fact.

The negative half is just as exact. Every operation that establishes primality occurs before the periodic loop is entered. The verifier states form feeding trees and cemetery rays, hence occur in no closed walk. If they are all deleted, every power trace and the full Fredholm determinant remains unchanged. The recurrent model is then the diagonal prime-loop construction that the verifier was meant to improve.

We prove two broader obstructions. First, under positive nonzero formal weights, an exact one-primitive-per-atom ledger forces every recurrent strongly connected component to be a simple directed cycle: recurrent branching creates another primitive orbit. Second, any total deterministic decider can be wrapped in time-damped configuration chains, accepted loops, and reject rays. The resulting adjacency is trace class on the same half-plane and has the Euler product of the chosen decidable support. The construction therefore works for squares, powers of two, Fibonacci numbers, hash predicates, and atom sets of effective factorial monoids. It is *algorithmically non-oracular, but dynamically selector-tautological*.

Our contributions are the following.

1.  We freeze the alphabet-sum/tensor semiring of finite full shifts with categorical language kept explicit.

2.  We expand trial division into local $Q_{n,d,q}$ successor states and prove that no factor-existence oracle is hidden in the graph.

3.  We define one weighted vertex-adjacency on the whole one-sided countable Markov graph and prove $\mathcal S_1$-holomorphy for $\operatorname{Re}s>1$.

4.  We prove the exact primitive/repetition ledger and the two-variable Fredholm--Euler identity.

5.  We prove transient pruning, a scoped positive exact-ledger SCC theorem, and deterministic-verifier collapse.

6.  We prove a universal total-decider compiler and its factorial-monoid specialization, including the $\mathbb F_q[t]$ control.

7.  We report exact finite implementation certificates behind a strict theorem/evidence firewall.

The result remains entirely within Symbolic Dynamics. We call $L_s$ a weighted vertex-adjacency, not a Ruelle operator; no thermodynamic Banach space is used. We do not continue the operator across $\operatorname{Re}s=1$, append a Gamma factor, construct a self-adjoint realization, or infer anything about the location of zeta zeros.

#### Organization.

places the candidate against classical symbolic, computational, and determinant work. freeze the source and verifier. prove trace class and the Euler identity. give the no-go theorems. reports exact finite certificates, and [\[sec:route,sec:conclusion\]](#sec:route,sec:conclusion){reference-type="ref" reference="sec:route,sec:conclusion"} records the strict route decision and next in-family obligation.

# Classical boundary and closest collisions {#sec:boundary}

The determinant conversion is classical. For finite-state shifts, periodic-point zeta functions and matrix determinants are linked by the Bowen--Lanford formalism [@BowenLanford1970]. Infinite weighted graphs can also admit Fredholm determinant formulas when the total weight is summable [@Deitmar2015]. We use the operator-theoretic trace-class determinant of @Simon1977. Accordingly, our analytic novelty claim is not a new determinant identity in the abstract; it is that the particular unpruned semiring verifier defines one trace-class operator with the exact prime ledger.

The source objects are also classical. Entropies of topological Markov shifts have a mature realization theory [@Lind1984], and direct-prime subshifts formalize indecomposability under direct product [@Kopra2023]. We use only the finite full-shift skeleton. Its alphabet-sum must be distinguished from categorical constructions among subshifts and block maps, whose universal properties depend on the chosen category [@SaloTorma2015]. The full shift on a disjoint alphabet contains mixed sequences and is not the topological disjoint union of its two summands.

Primality recognition and machine simulation are not new. Classical work already separates the complexity of recognizing prime representations by automata [@HartmanisShank1968]; register and counter machines capture broad recursive computation [@ShepherdsonSturgis1963]; and Turing machines can themselves be studied as topological dynamical systems [@Kurka1997]. This prevents the broad claim that SD-C21 is novel merely because a dynamical graph computes primes. The narrower contribution is its source lock: the local instructions are tensor product, alphabet successor, and alphabet-sum order, and the cofactor is exposed in the state graph.

Countable symbolic systems create a second warning. Thermodynamic and zeta questions for countable Markov chains require summability and recurrence hypotheses absent from finite matrices [@GurevichSavchenko1998; @Sarig1999]. More pointedly, a fixed renewal shift with a suitable two-coordinate weight can realize arbitrary holomorphic zeta germs near the origin [@Sarig2004Renewal]. We do not use that construction, but it motivates the adversarial question: has a countable grammar discovered arithmetic, or has it merely compiled a target?

Formal-language zetas [@BerstelReutenauer1990] and the number-theoretic combinatorics of trace-monoid hikes [@GiscardRochet2017] show that primitive words and graph walks support wide classes of Euler-like factorizations. Their graph primes are not automatically rational primes. Likewise, semiring structures and factorization questions occur for finite dynamical systems [@NaquinGadouleau2024]. These are close conceptual collisions, not ancestors of the precise $I,T,Q,A,R$ graph.

The defensible contribution is therefore the conjunction of an unrolled full-shift-semiring verifier, a trace-class whole adjacency, an exact Euler determinant, and a pruning/compiler theorem that limits its meaning. The last item is essential. Without it, a correct formula would be easy to overinterpret as recurrent arithmetic selectivity.

# The finite-full-shift semiring skeleton {#sec:semiring}

Let $A_n$ be an $n$-element alphabet and let $$F_n=A_n^{\mathbb Z}$$ denote the corresponding two-sided full shift, considered up to topological conjugacy. The source objects are two-sided because their entropy and product structure are convenient and canonical. The verifier built later is a separate one-sided countable Markov shift.

For $m,n\ge1$, set $$F_m\boxtimes F_n:=F_{A_m\times A_n}\cong F_{mn},
\qquad
F_m\boxplus F_n:=F_{A_m\sqcup A_n}\cong F_{m+n}.$$ We call $\boxplus$ the *alphabet-sum*, or alphabet coproduct followed by the full-shift functor.

This terminology is deliberate. The dynamical disjoint union $F_m\sqcup F_n$ permits a point to stay in one component forever. By contrast, $F_{A_m\sqcup A_n}$ permits arbitrary temporal mixing between the two alphabets. We therefore make no claim that $\boxplus$ is a categorical coproduct in a category of subshifts.

Alphabet cardinality immediately gives a semiring skeleton: $$[F_m]\boxtimes[F_n]=[F_{mn}],\qquad
[F_m]\boxplus[F_n]=[F_{m+n}].$$ Both operations are invariant under alphabet relabeling. The intrinsic norm used below is topological entropy, $$h(F_n)=\log n,
\qquad
h(F_m\boxtimes F_n)=h(F_m)+h(F_n).$$

We also freeze an additive order and successor: $$F_a<F_b
\quad\Longleftrightarrow\quad
F_a\boxplus F_c=F_b\ \text{for some }c\ge1,
\qquad
S(F_d)=F_d\boxplus F_1=F_{d+1}.$$ Thus comparison, multiplication, and increment can all be stated in source language. In an executable presentation, the witness $F_c$ is exposed by successor rather than supplied by an existential edge guard.

The construction does not discover a new semiring law: it chooses a simple family of symbolic objects whose alphabet cardinalities reproduce $\mathbb N_{\ge1}$. This is nevertheless source-intrinsic enough to earn the structural arithmetic coordinate used in [10](#sec:route){reference-type="ref" reference="sec:route"}. The later Euler identity is credited separately at the determinant coordinate.

The key question is what happens when these instructions are made temporal. The next section turns them into a local deterministic graph and carefully avoids the one forbidden shortcut: an edge that already knows whether a factor exists.

# The expanded semiring sieve graph {#sec:graph}

For each input object $F_n$, $n\ge2$, introduce an input state $I_n$ and a divisor state $T_{n,2}$. Further states are $$T_{n,d},\qquad Q_{n,d,q},\qquad A_n,\qquad R_{n,k},$$ where $d,q\ge2$ and $k\ge1$. The graph is the union of the unique forward orbits of all $I_n$ under the following transition program, together with the full one-way cemetery continuations.

First, $$I_n\longrightarrow T_{n,2}.$$ At a divisor state, compare $F_d\boxtimes F_d$ with $F_n$: $$T_{n,d}\longrightarrow
\begin{cases}
A_n,&d^2>n,\\
Q_{n,d,2},&d^2\le n.
\end{cases}
\label{eq:T-transition}$$ At a quotient state, compare $F_d\boxtimes F_q$ with $F_n$: $$Q_{n,d,q}\longrightarrow
\begin{cases}
Q_{n,d,q+1},&dq<n,\\
R_{n,1},&dq=n,\\
T_{n,d+1},&dq>n.
\end{cases}
\label{eq:Q-transition}$$ Finally, $$A_n\longrightarrow A_n,
\qquad
R_{n,k}\longrightarrow R_{n,k+1}.
\label{eq:terminal-transitions}$$

The square comparison in [\[eq:T-transition\]](#eq:T-transition){reference-type="eqref" reference="eq:T-transition"} occurs before quotient search. This accepts $n=2,3$ rather than incorrectly testing $d=2$ as a proper factor. The cemetery is an infinite unilateral ray. Making it an absorbing loop would create a false primitive orbit for every composite and is forbidden.

#### No-oracle boundary.

The edge rule does not contain the predicate $d\mid n$. Starting at $Q_{n,d,2}$, it forms successive products $$F_d\boxtimes F_2, F_d\boxtimes F_3,ldots$$ until equality or the first strict overshoot. Only after [\[eq:Q-transition\]](#eq:Q-transition){reference-type="eqref" reference="eq:Q-transition"} has been defined and proved correct may the phrase "reject if $d$ divides $n$" be used as a macro.

[\[thm:trial\]]{#thm:trial label="thm:trial"} The orbit of $I_n$ reaches $A_n$ if and only if $n$ is prime. Consequently, the only directed cycles in the graph are the self-loops at $A_p$, one for each rational prime $p$.

For fixed $n,d$ with $d^2\le n$, the quotient index strictly increases. Hence it reaches equality $dq=n$ exactly when $d$ divides $n$, and otherwise reaches the first $q$ with $dq>n$ and advances to $d+1$. If $n=ab$ is composite with $2\le a\le b$, then $a\le\sqrt n$; the divisor chain reaches $d=a$ before the strict-square stop and quotient search reaches $q=b$. Conversely, equality with $d,q\ge2$ is a nontrivial factorization. Passing all $d\le\sqrt n$ therefore characterizes primes.

Outside $A_n$, every transition strictly increases the active quotient, divisor, or cemetery index along its functional forward orbit. Those states cannot lie on a directed cycle. The declared accept loops are consequently all the cycles, and correctness restricts them to prime indices.

## One-sided phase space

Let $G$ denote this countable graph and let $X_G^+$ be its one-sided edge shift. The one-sided qualification matters. A two-sided edge shift retains only edges admitting an infinite legal past; input and early computation states would disappear. We make no two-sided claim and use the vertex space of the full source graph for the operator below.

The graph is stationary in the standard sense that one fixed adjacency rule is iterated. The input index $n$ labels countably many components; it is not a time-dependent change of dynamics. The construction is effective and contains no precomputed prime list. It is nevertheless extensionally a complete prime selector, a distinction made precise in [\[sec:pruning,sec:compiler\]](#sec:pruning,sec:compiler){reference-type="ref" reference="sec:pruning,sec:compiler"}.

# Entropy roofs and the whole weighted adjacency {#sec:operator}

We now put computation and periodic support into one operator. Freeze the edge roof $$\begin{aligned}
\tau(I_n,T_{n,2})&=\log(2n),\label{eq:roof-input}\\
\tau(T_{n,d},A_n)&=\log(nd),\label{eq:roof-accept}\\
\tau(T_{n,d},Q_{n,d,2})&=\log(2nd),\label{eq:roof-tq}\\
\tau(Q_{n,d,q},\mathrm{next})&=\log(ndq),\label{eq:roof-q}\\
\tau(R_{n,k},R_{n,k+1})&=\log(n(k+1)),\label{eq:roof-r}\\
\tau(A_n,A_n)&=\log n.\label{eq:roof-loop}\end{aligned}$$ Every value is the entropy of a tensor product of source full shifts. The factor $2$ in [\[eq:roof-tq\]](#eq:roof-tq){reference-type="eqref" reference="eq:roof-tq"} records entry into the first explicit quotient state and matches the finite implementation.

There are two different naturality claims. The accepted loop roof $h(F_n)=\log n$ is canonical on the chosen source skeleton, but it is attached only after the program accepts $n$. By contrast, the transient roofs [\[eq:roof-input\]](#eq:roof-input){reference-type="eqref" reference="eq:roof-input"}--[\[eq:roof-r\]](#eq:roof-r){reference-type="eqref" reference="eq:roof-r"} are a `MODELING_CHOICE`. They are source-expressible and useful for summability, but trial division does not force them. Any locally uniformly summable replacement on transient edges gives the same power traces and determinant.

Let $$\mathcal H=\ell^2(V(G))$$ with standard basis $(\delta_v)_{v\in V(G)}$. For $\operatorname{Re}s>1$, define the arrival-weighted adjacency $$L_s\delta_u=\sum_{e:u\to v}e^{-s\tau(e)}\delta_v.
\label{eq:operator}$$ The sum has one term at each source vertex because the graph is deterministic. We retain the edge-sum notation to expose the nuclear decomposition. No thermodynamic function space is being used, so we call $L_s$ a weighted vertex-adjacency or graph transfer, not a Ruelle operator.

[\[thm:traceclass\]]{#thm:traceclass label="thm:traceclass"} For every $s$ with $\sigma=\operatorname{Re}s>1$, the operator $L_s$ is trace class. The map $s\mapsto L_s$ is holomorphic with values in $\mathcal S_1(\mathcal H)$ on that half-plane.

Each edge contributes the rank-one operator $$e^{-s\tau(e)}|\delta_{t(e)}\rangle\langle\delta_{o(e)}|$$ of trace norm $e^{-\sigma\tau(e)}$. The loop and input sums are bounded by $$\sum_p p^{-\sigma}+\sum_{n\ge2}(2n)^{-\sigma}<\infty.$$ For divisor-state edges, including the unique terminal value $d=\lfloor\sqrt n\rfloor+1$, a fixed endpoint constant gives $$\sum_{n\ge2}n^{-\sigma}
 \sum_{2\le d\le\sqrt n+1}d^{-\sigma}
\le C_\sigma\sum_{n\ge2}n^{-\sigma}<\infty.$$ For quotient states, enlarging every finite reachable range yields $$\sum_{n\ge2}\sum_{d\ge2}\sum_{q\ge2}(ndq)^{-\sigma}
\le
\left(\sum_{n\ge2}n^{-\sigma}\right)
\left(\sum_{d\ge2}d^{-\sigma}\right)
\left(\sum_{q\ge2}q^{-\sigma}\right)<\infty.$$ Finally the cemetery contribution is bounded by $$\sum_{\substack{n\ge2\\ n\,\mathrm{composite}}}
\sum_{k\ge1}[n(k+1)]^{-\sigma}
\le
\left(\sum_{n\ge2}n^{-\sigma}\right)
\left(\sum_{j\ge2}j^{-\sigma}\right)<\infty.$$ Thus the edge series converges absolutely in trace norm. Replacing $\sigma$ by a compact lower bound on every compact sub-half-plane gives locally uniform convergence of holomorphic finite partial sums. The Banach-valued Weierstrass theorem proves $\mathcal S_1$-holomorphy.

The theorem concerns the raw graph, not a recurrent pruning. This is the strongest analytic success of the candidate: computation edges, cemetery edges, and accepted loops genuinely coexist in one trace-class operator on the same half-plane as the Euler product.

# Exact primitive ledger and Euler determinant {#sec:euler}

For $\operatorname{Re}s>1$, define $$D_{\mathrm{SV}}(s,z)=\det_{\mathcal H}(I-zL_s),
\qquad
D_{\mathrm{SV}}(s)=D_{\mathrm{SV}}(s,1).$$ The determinant exists because of [\[thm:traceclass\]](#thm:traceclass){reference-type="ref" reference="thm:traceclass"}. The extra variable $z$ records graph-step length; it will be important when discussing cycle contraction.

[\[thm:traces\]]{#thm:traces label="thm:traces"} For every integer $r\ge1$ and $\operatorname{Re}s>1$, $$\operatorname{Tr}(L_s^r)=\sum_p p^{-rs}.$$ The primitive periodic orbits are exactly $\gamma_p=[A_p]$. Their $r$-fold temporal repetitions have total weight $p^{-rs}$ and multiplicity one. There are no mixed primitive cycles.

For any vertex $v$, the diagonal coefficient $\left\langle L_s^r\delta_v,\delta_v\right\rangle$ is the sum of weights of length-$r$ closed walks rooted at $v$. By [\[thm:trial\]](#thm:trial){reference-type="ref" reference="thm:trial"}, each such walk is the $r$-fold traversal of one accepted prime loop. Its loop weight is $p^{-s}$. Trace class permits the diagonal coefficients to be summed in the standard basis, giving the stated formula. The same cycle census proves the primitive and multiplicity claims.

[\[thm:euler\]]{#thm:euler label="thm:euler"} For $\operatorname{Re}s>1$ and every $z\in\mathbb C$, $$D_{\mathrm{SV}}(s,z)=\prod_p(1-zp^{-s}).
\label{eq:euler-two-variable}$$ In particular, $$D_{\mathrm{SV}}(s)=\prod_p(1-p^{-s})=\zeta(s)^{-1}.
\label{eq:euler-zeta}$$

For $|z|$ initially small, the trace-class determinant expansion and [\[thm:traces\]](#thm:traces){reference-type="ref" reference="thm:traces"} give $$\begin{aligned}
\log D_{\mathrm{SV}}(s,z)
&=-\sum_{r\ge1}\frac{z^r}{r}\operatorname{Tr}(L_s^r)\\
&=-\sum_p\sum_{r\ge1}\frac{(zp^{-s})^r}{r}
=\sum_p\log(1-zp^{-s}).
\end{aligned}$$ For fixed $\operatorname{Re}s>1$, the Fredholm determinant is entire in $z$. The product on the right of [\[eq:euler-two-variable\]](#eq:euler-two-variable){reference-type="eqref" reference="eq:euler-two-variable"} is also entire and normally convergent on compact $z$-sets because $\sum_pp^{-\sigma}<\infty$. Equality near zero extends to every $z$. At $z=1$, Euler's product is absolutely convergent and gives [\[eq:euler-zeta\]](#eq:euler-zeta){reference-type="eqref" reference="eq:euler-zeta"}.

The formula clears three bookkeeping gates simultaneously. Primitive orbits have the intended support, temporal repetitions carry the exponent $r$ automatically, and the same parent operator produces all traces and the determinant. It does not yet say that the computation producing the support is recurrently visible. That question has the opposite answer.

# Recurrent-core collapse {#sec:pruning}

Let $\mathcal H_A$ be the closed span of the accepted states and set $\mathcal H_T=\mathcal H_A^\perp$. Ordering the decomposition as $\mathcal H_A\oplus\mathcal H_T$ gives $$L_s=
\begin{pmatrix}
D_s&B_s\\
0&Q_s
\end{pmatrix},
\qquad
D_s\delta_{A_p}=p^{-s}\delta_{A_p}.
\label{eq:block}$$ The cross block records the last transition from a successful trial trace to its accepted state. There is no edge from an accepted state back into the verifier.

[\[thm:invisibility\]]{#thm:invisibility label="thm:invisibility"} For every $r\ge1$ and $\operatorname{Re}s>1$, $$\operatorname{Tr}Q_s^r=0,
\qquad
\operatorname{Tr}L_s^r=\operatorname{Tr}D_s^r.$$ For every $z\in\mathbb C$, $$\det(I-zQ_s)=1,
\qquad
\det(I-zL_s)=\det(I-zD_s).$$ Changing or deleting all transient edges, provided the replacement remains trace class, changes none of these determinants.

The quotient graph underlying $Q_s$ has no closed walk. Every diagonal coefficient of $Q_s^r$ therefore vanishes, and trace class justifies summing those coefficients. The block-triangular form then gives equality of the power traces. Near $z=0$, the trace-log identity gives $$\log\det(I-zQ_s)
=-\sum_{r\ge1}\frac{z^r}{r}\operatorname{Tr}Q_s^r=0.$$ Both determinants are entire in $z$, so the identities extend globally. Any transient modification has the same closed-walk census and the same argument applies.

This theorem proves two facts that should not be conflated. The whole operator is analytically legitimate, so the Euler identity is not obtained by silently discarding a non-trace-class decoration. Nevertheless, the determinant is completely insensitive to the decoration. The computation and its chosen transient roofs earn no periodic-orbit credit.

## A positive exact-ledger obstruction

The collapse is not peculiar to trial division. We next isolate the mechanism under assumptions strong enough to make the result true and narrow enough to avoid claims about cancellation-based models.

[\[thm:ledger-pruning\]]{#thm:ledger-pruning label="thm:ledger-pruning"} Let $G'$ be a directed graph with nonzero formal edge weights in the positive power-series semiring over independent variables $(x_a)_{a\in\mathcal A}$. Assume an exact orbitwise ledger: for every $a$ there is one declared primitive class $\gamma_a$ of total weight $x_a$, its powers are temporal repetitions, and there is no other primitive class, including no mixed formal monomial and no distinct primitive of weight $x_a^r$. Then:

1.  every recurrent strongly connected component is a simple directed cycle;

2.  these components are in bijection with the declared primitive classes;

3.  every vertex and edge outside those cycles is absent from every power trace;

4.  pruning the nonrecurrent graph preserves all raw power traces and the full $z$-Fredholm determinant whenever defined.

A simple cycle of graph length $\ell$ and total weight $w$ contributes $1-z^\ell w$. First-return contraction to one loop preserves the unmarked factor $1-w$; it preserves the marked determinant only when the contracted loop retains the composite marker $z^\ell$.

Every recurrent edge lies on a directed cycle. Suppose one recurrent SCC contains two declared cycles. Strong connectivity supplies finite directed connector paths in both directions. Following the first cycle, one connector, the second cycle, and the return connector produces a closed word that is not a temporal repetition of either declared class. Dividing by its least period yields an additional primitive orbit, contrary to the exact ledger.

If an SCC contains one declared cycle and any extra recurrent edge or vertex, that edge lies on another directed cycle and the same connector argument applies. Positivity and independent formal variables prohibit cancellation or specialization from erasing the extra primitive. Thus each recurrent SCC is exactly one simple declared cycle. Nonrecurrent edges lie in no closed walk, so they occur in no power trace. Trace-log identities give pruning invariance. The factor of an $\ell$-cycle follows by multiplying its edge weights around one return; graph-step marking contributes $z^\ell$.

[\[cor:functional\]]{#cor:functional label="cor:functional"} Every outdegree-one verifier graph is a functional digraph whose recurrent components are cycles with feeding trees. If its ledger has exactly one primitive per accepted object, computation in the feeding trees is determinant-invisible. Computation placed along an accepted cycle becomes a state subdivision of the accepted first-return loop after contraction, with graph-step length retained by $z^\ell$.

The corollary is an orbit and determinant statement, not a topological conjugacy of the original one-sided systems. Nor does [\[thm:ledger-pruning\]](#thm:ledger-pruning){reference-type="ref" reference="thm:ledger-pruning"} classify signed, complex, supertrace, or homological grammars: distinct cycles can then cancel after applying an additional functional. That broader dichotomy remains open and requires a different data-type audit.

For SD-C21, every declared cycle already has graph length one. Pruning and contraction therefore produce exactly the diagonal operator $D_s$ with no $z$-marker ambiguity. This is the precise sense in which the model is `PRUNING_EQUIVALENT` to a prime-loop core.

# Universal support and factorial-monoid compilers {#sec:compiler}

The pruning theorem explains why the trial computation disappears. A universal construction shows that this is not a harmless presentation artifact: essentially any decidable accepted inventory can be made to look the same to a Fredholm determinant.

[\[thm:universal\]]{#thm:universal label="thm:universal"} Let $S\subseteq\{2,3,\ldots\}$ be decided by a total deterministic machine with finite runtime $T(n)\ge1$. There exists a one-sided countable functional graph and an $\mathcal S_1$-holomorphic weighted adjacency $L_{S,s}$ for $\operatorname{Re}s>1$ such that, for every $r\ge1$ and $z\in\mathbb C$, $$\operatorname{Tr}L_{S,s}^r=\sum_{n\in S}n^{-rs},
\qquad
\det(I-zL_{S,s})=\prod_{n\in S}(1-zn^{-s}).
\label{eq:universal}$$

For each input $n$, expose the complete configuration chain $$C_{n,0}\longrightarrow C_{n,1}\longrightarrow\cdots
\longrightarrow C_{n,T(n)}.$$ Send the terminal state to a self-loop $A_n$ when $n\in S$, and otherwise to a one-way cemetery ray. Give the $t$th computation or terminal edge weight $[n(t+2)]^{-s}$, the $k$th cemetery edge weight $[n(k+1)]^{-s}$, and the accepted loop weight $n^{-s}$. With $\sigma=\operatorname{Re}s>1$, $$\begin{aligned}
\left\lVert L_{S,s}\right\rVert_1
&\le \sum_{n\ge2}\sum_{t=0}^{T(n)}[n(t+2)]^{-\sigma}
 +\sum_{n\notin S}\sum_{k\ge1}[n(k+1)]^{-\sigma}
 +\sum_{n\in S}n^{-\sigma}\\
&\le 2\left(\sum_{n\ge2}n^{-\sigma}\right)
       \left(\sum_{j\ge2}j^{-\sigma}\right)
 +\sum_{n\ge2}n^{-\sigma}<\infty.
\end{aligned}$$ The bound is independent of the growth of $T(n)$ because every finite inner sum is dominated by the full $j$-series. Compact lower bounds on $\sigma$ give $\mathcal S_1$-holomorphy. Only the accepted loops are closed walks, so the proof of [\[thm:traces,thm:euler\]](#thm:traces,thm:euler){reference-type="ref" reference="thm:traces,thm:euler"} gives [\[eq:universal\]](#eq:universal){reference-type="eqref" reference="eq:universal"}.

The theorem is stronger than a random-support experiment. It applies to squares, powers of two, Fibonacci numbers, or the output of an arbitrarily slow total program. The determinant faithfully records the accepted set but contains no certificate of why that set was selected.

[\[thm:factorial\]]{#thm:factorial label="thm:factorial"} Let $M$ be a countable effective factorial monoid with atom set $\mathcal A$, a terminating atom verifier, a multiplicative norm $N:M\to(1,\infty)$, and source-defined transient roofs summable on a half-plane. Suppose $$\sum_{a\in\mathcal A}N(a)^{-\sigma}<\infty.$$ The verifier-to-loop compilation gives a trace-class weighted adjacency $L_{M,s}$ satisfying $$\operatorname{Tr}L_{M,s}^r=\sum_{a\in\mathcal A}N(a)^{-rs},
\qquad
\det(I-zL_{M,s})
=\prod_{a\in\mathcal A}(1-zN(a)^{-s}).
\label{eq:factorial}$$

The terminating atom verifier supplies the configuration chain in [\[thm:universal\]](#thm:universal){reference-type="ref" reference="thm:universal"}; a summable source enumeration supplies the transient decay. Correctness, summability, and the absence of reject cycles are the only inputs to the trace and determinant proofs. No special property of rational primes is used.

For a concrete control, take the monoid of monic polynomials over $\mathbb F_q$ and $N(f)=q^{\deg f}$. Unique factorization gives $$\prod_{\pi\ \mathrm{monic\ irreducible}}
(1-u^{\deg\pi})^{-1}
=\sum_{f\ \mathrm{monic}}u^{\deg f}
=\sum_{d\ge0}q^du^d=\frac1{1-qu}.$$ Substituting $u=q^{-s}$ and inverting yields $$\det(I-L_{M,s})
=\prod_\pi(1-q^{-s\deg\pi})=1-q^{1-s}.
\label{eq:poly-control}$$

The same logic applies to free commutative monoids with arbitrary summable generator norms, shuffled atom inventories, and generalized-prime systems. Thus the exact Riemann Euler factor is a genuine success at A2 but not a selector theorem. The graph has computed the predicate before it creates periodic support. We call this `SELECTOR_TAUTOLOGICAL` and `PROVES_TOO_MUCH`, not logically circular: the trial-division proof in [\[thm:trial\]](#thm:trial){reference-type="ref" reference="thm:trial"} remains a real proof.

# Exact finite certificate and adversarial controls {#sec:finite}

The theorems above do not depend on computation. A separate exact prototype checks that the expanded implementation matches the frozen graph, including the absence of a hidden divisor predicate. All arithmetic matrix audits use rational numbers; the independent prime sieve appears only in validation, never in graph construction. The final suite passed $13/13$ tests.

L0.25L0.23X audit & range or size & result\
prime support & cutoffs $32,64,128,256,512$ & exact at every cutoff; 97 primes through 512\
source no-oracle scan & 1,651 reachable $Q$ nodes/edges & forbidden factor identifiers and calls: 0\
whole graph & $n\le24$, cemetery depth 3 & 296 vertices, 282 edges, 287 transient vertices\
recurrent SCCs & $n\le24$ & exactly $A_p$ for $p=2,3,5,7,11,13,17,19,23$\
power traces & $s=2$, $r=1,\ldots,12$ & every rational trace equals $\sum_{p\le24}p^{-2r}$\
dense determinant & $n\le8$, 37 vertices, 34 edges & $772486/893025$ at $s=2,z=1/3$, exact\
$\mathbb F_2[t]$ control & degrees $1$ through 8 & irreducible counts $(2,1,2,3,6,9,18,30)$; Euler coefficients exact\

The determinant row is an independent Bareiss elimination of the complete finite weighted matrix. Its value is $$\frac{772486}{893025}
=\prod_{p\le8}\left(1-\frac1{3p^2}\right).$$ The larger cutoff is certified through the SCC census and twelve independent power traces, avoiding a costly symbolic determinant that would add no new theorem.

## Naturality and failure controls

Alphabet relabeling with frozen seed 19021 transported both semiring operations and decoded to the same 97 primes through 512. Shuffling only the entropy/cardinality association failed the target trace, showing that operation transport, not an unstructured weight multiset, carries the source program.

Bounded trial depths $2,3,5,7,11$ produced respectively $159,75,42,23,13$ false positives through 512. Replacing factorization of $n$ by factorization of $n+1$ selected 96 inputs, overlapped the 97 primes in only one input, and had symmetric difference 191. These failures certify that the quotient search and square termination, rather than a trivial local statistic, determine support.

The decisive controls go in the opposite direction. The universal wrapper was instantiated through 24 for squares, powers of two, Fibonacci numbers, and a deterministic hash residue. In every case the recurrent SCCs were exactly the accepted loops and the independent rational determinant matched the corresponding product. Thirty-two matched-cardinality random accepted sets used the same diagonal technology with prime overlaps between 12 and 22. These controls do not refute implementation correctness; they establish its lack of arithmetic selectivity.

::: {#tab:universal-controls}
  predicate           accepted support through 24  exact determinant
  ------------------ ----------------------------- -------------------
  squares                      $4,9,16$            $79/80$
  powers of two               $2,4,8,16$           $478819/512000$
  Fibonacci                 $2,3,5,8,13,21$        $2066801/2250000$
  hash modulo five         $2,3,12,13,22,23$       $209/225$

  : Universal-decider controls through 24. The displayed determinants come from the independent matrix prefix $n\le8$ at $s=2,z=1/5$; recurrent support is audited through 24.
:::

Finite entrywise norm sums were also monitored as cutoffs increased. At cutoff 512 they were approximately $17.0961,8.0651,3.03265,0.882212$ for $\sigma=1.1,1.25,1.5,2$. These monotone partial sums illustrate the frozen roof; convergence is supplied by [\[thm:traceclass\]](#thm:traceclass){reference-type="ref" reference="thm:traceclass"}, not inferred from the table.

#### Evidence firewall.

The source scan, support check, SCC census, and rational matrices certify the finite implementation. They do not prove the infinite trace-class theorem, the Fredholm identity, or the pruning theorem. Conversely, the universal controls are constructive witnesses to [\[thm:universal\]](#thm:universal){reference-type="ref" reference="thm:universal"}; they are not a statistical argument against primes.

# Strict route evaluation and limitations {#sec:route}

The candidate is unusually clean at the local analytic gates and unusually clear about why those gates are insufficient. We freeze the coordinate tuple $$\boxed{
\begin{gathered}
(\texttt{A0\_STRUCTURAL\_ARITHMETIC\_RELATION},\\
\texttt{A1\_PASS\_ANALYTIC},
\ \texttt{A2\_ANALYTIC\_DETERMINANT},\\
\texttt{A3\_FAIL},\ \texttt{A4\_FAIL}).
\end{gathered}}$$

#### A0: structural arithmetic relation.

The finite-full-shift skeleton supplies source-intrinsic addition, multiplication, successor, order, and entropy. The explicit quotient search uses those relations and no prime table. We do not upgrade A0 to an analytic origin: the exact Euler formula belongs at A2 and the universal compiler denies unique arithmetic selectivity.

#### A1: analytic ledger pass.

The primitive inventory is exact, complete, multiplicity one, and power coherent. Temporal repetition produces $p^{-rs}$ on the same graph. The later selector-tautology does not make this ledger false; it triggers a separate adversarial gate.

#### A2: analytic determinant.

One $\mathcal S_1$-holomorphic whole adjacency has the exact two-variable product and $1/\zeta(s)$ at $z=1$ on $\operatorname{Re}s>1$. The equality is neither a finite-cutoff extrapolation nor a product assigned after operator construction.

#### A3: fail.

No new meromorphic continuation, Gamma factor, completed determinant, functional equation, trivial-zero treatment, Riemann--von Mangoldt law, or Weil-type compression is derived. Importing the known continuation of $\zeta$ into the right side of [\[eq:euler-zeta\]](#eq:euler-zeta){reference-type="eqref" reference="eq:euler-zeta"} does not continue the operator family or prove a dynamical functional equation.

#### A4: fail.

The recurrent core is a diagonal compact contraction for $\operatorname{Re}s>1$. There is no canonical unitary, self-adjoint, scattering, Hamiltonian, or normal critical-line lift. No spectrum is identified with nontrivial zeta zeros.

## Adversarial gate

The positive tuple does not override the no-go theorems: $$\begin{gathered}
\texttt{STOP\_RECURRENT\_ARITHMETIC\_ADVANCE},\qquad
\texttt{STOP\_GLOBAL\_ANALYTIC\_STRUCTURE},\\
\texttt{STOP\_ARITHMETIC\_SELECTIVITY},\qquad
\texttt{SELECTOR\_TAUTOLOGICAL},\\
\texttt{PRUNING\_EQUIVALENT},\qquad
\texttt{PROVES\_TOO\_MUCH}.
\end{gathered}$$ Therefore $$\boxed{\texttt{ROUTE\_A\_REJECTED}\qquad
\texttt{ROUTE\_B\_LOCKED}.}$$

This verdict does not diminish the trial-division theorem. No prime table, Riemann-zero table, fitted phase, or von Mangoldt coefficient is loaded. The operator is not patched coordinate by coordinate. The failure is instead dynamical: the complete selector runs in transient time, and periodic data only record the answer. The universal wrapper proves that an exact accepted support determinant is not, by itself, an arithmetic mechanism.

# Conclusion {#sec:conclusion}

The semiring sieve answers a useful "how far" question. Starting from finite full shifts, one can express addition, multiplication, successor, comparison, and entropy; expand quotient search into local states; decide primality without a factor oracle; and place the entire resulting countable graph in one trace-class weighted adjacency. The primitive ledger and Fredholm determinant are then exactly the Riemann Euler ledger on $\operatorname{Re}s>1$.

That achievement also exposes the boundary of verifier-based models. The determinant counts closed walks, while a terminating computation naturally lives in feeding trees. Here the two data types coexist but do not interact: pruning deletes every arithmetic instruction. The positive exact-ledger theorem explains why simply moving the computation into a recurrent positive Markov component is not an easy repair---branching creates extra primitive cycles. The universal total-decider theorem shows that accepted loops can compile any decidable support.

The next in-family candidate must therefore forbid self-loops created after a completed atom test. It should place all nonunit full-shift objects in a single recurrent semiring-local grammar, expose every cofactor witness, and classify its primitive SCCs before choosing a Fredholm weight. A minimal relation is the expanded successor-divisor rule $d\mid m+1$. It advances only if prime or prime-power information becomes an invariant of recurrent cycles and separates from shuffled, composite, random-divisibility, and factorial-monoid controls.

For the present object the conclusion is exact: the Euler determinant is correct, the computation is non-oracular, the recurrent advance is null, and no statement about Riemann zeros follows.

# Supplementary proof details {#app:proofs}

## Reachable-state bounds

For fixed $n$, the divisor index reaches at most $\lfloor\sqrt n\rfloor+1$. At a fixed tested divisor $d$, the quotient index reaches at most $\lfloor n/d\rfloor+1$. These bounds are used only to confirm that each input trace is finite before acceptance or rejection. The trace-class proof deliberately enlarges both ranges to infinity, producing the transparent product majorant $$\sum_{n,d,q\ge2}(ndq)^{-\sigma}.$$ Endpoint choices change this estimate by at most a constant multiple of $\sum_nn^{-\sigma}$. The source lock fixes the prototype-consistent $T\to Q_{n,d,2}$ roof $\log(2nd)$.

## Trace class versus entrywise summability

For an arbitrary matrix, summability of entries in one basis is stronger than trace class and need not be necessary. Here it is a convenient sufficient condition because every edge is a rank-one matrix unit. If $E_0\subset E_1\subset\cdots$ exhausts the edges, then $$\left\lVert\sum_{e\in E_j}E_e(s)-\sum_{e\in E_i}E_e(s)\right\rVert_1
\le\sum_{e\in E_j\setminus E_i}e^{-\sigma\tau(e)}.$$ The scalar tail tends to zero, so the operator series is Cauchy in $\mathcal S_1$. This also avoids any conditional rearrangement of edge terms.

## Why vanishing diagonal entries give zero trace

For every $r\ge1$, $Q_s^r$ is trace class because $Q_s$ is trace class and bounded. The trace of a trace-class operator equals the absolutely convergent sum of its diagonal coefficients in every orthonormal basis. Those coefficients enumerate rooted length-$r$ closed walks. Acyclicity makes each coefficient zero, hence $\operatorname{Tr}Q_s^r=0$. No triangular-basis spectral theorem is required.

## Entireness in the graph marker

For fixed $s$, the Fredholm determinant $z\mapsto\det(I-zL_s)$ is entire. The canonical product $$P_s(z)=\prod_p(1-zp^{-s})$$ is normally convergent on every disk $|z|\le R$, since $\sum_p\sup_{|z|\le R}|zp^{-s}|\le R\sum_pp^{-\sigma}<\infty$. Thus equality of logarithms near zero extends to equality of entire functions; no choice of logarithm is needed away from zero.

## Scope of the SCC connector argument

The exact-ledger theorem is stated orbitwise before arithmetic specialization. This prevents two distinct cycles of coincident numerical weight from being identified. The independent variables also distinguish a mixed cycle from a temporal repetition. Positivity prevents cancellation in the trace logarithm. If signed or matrix weights are allowed, an additional primitive can have zero trace under a chosen functional; the theorem does not exclude that possibility.

## Universal wrapper with arbitrary runtime

The bound $$\sum_{t=0}^{T(n)}(t+2)^{-\sigma}
\le\sum_{j\ge2}j^{-\sigma}$$ is uniform in $T(n)$. Consequently no polynomial, primitive-recursive, or computable complexity estimate is used beyond total termination. The wrapper is source-effective whenever the machine is, but the determinant cannot recover runtime: all configuration edges lie outside closed walks.

## First-return contraction

Let a simple directed cycle have edges $e_1,\ldots,e_\ell$ and weights $w_1,\ldots,w_\ell$. Its weighted adjacency has nonzero trace only at powers divisible by $\ell$, with $$\operatorname{Tr}L^{m\ell}=\ell(w_1\cdots w_\ell)^m.$$ Hence $$\det(I-zL)
=\exp\left(-\sum_{m\ge1}\frac{z^{m\ell}}{m}
(w_1\cdots w_\ell)^m\right)
=1-z^\ell w_1\cdots w_\ell.$$ This calculation is why contraction must retain $z^\ell$. At $z=1$ it reduces to the usual first-return loop factor.

# Claim, anti-claim, and route ledger {#app:ledger}

L0.29L0.19X statement & status & reason\
Expanded graph accepts exactly primes & theorem & local quotient successor search plus square-root criterion\
Whole adjacency is trace class for $\operatorname{Re}s>1$ & theorem & absolutely summable rank-one edge decomposition\
Power traces and Euler determinant are exact & theorem & complete cycle census and Fredholm trace formula\
Verifier is determinant-invisible & theorem & transient block has no closed walks\
Positive exact ledgers prune to simple cycles & scoped theorem & recurrent branching creates an extra primitive orbit\
All signed or homological verifiers collapse & open / not claimed & cancellation invalidates the positive formal-weight proof\
Finite source uses no factor oracle & exact source certificate & 1,651 explicit quotient states/edges; forbidden calls and identifiers absent\
Finite support/SCC/matrix outputs are exact & exact evidence & integer and rational arithmetic; 13/13 tests\
The graph continues $1/\zeta$ past $\operatorname{Re}s=1$ & false / not claimed & no continued operator or determinant is constructed\
The recurrent dynamics discover primes & false for SD-C21 & accepted support is created after a complete verifier\
The construction proves RH & false / not claimed & A3 and A4 fail; no zero realization\

#### Frozen route package.

    (A0_STRUCTURAL_ARITHMETIC_RELATION,
     A1_PASS_ANALYTIC,
     A2_ANALYTIC_DETERMINANT,
     A3_FAIL,
     A4_FAIL)

    GO_SOURCE_INTRINSIC_SEMIRING_VERIFIER
    GO_EXACT_PRIMITIVE_REPETITION_LEDGER
    GO_WHOLE_OPERATOR_TRACE_CLASS_RE_GT_1
    GO_SAME_OBJECT_EULER_FREDHOLM_IDENTITY

    STOP_RECURRENT_ARITHMETIC_ADVANCE
    STOP_GLOBAL_ANALYTIC_STRUCTURE
    STOP_ARITHMETIC_SELECTIVITY
    SELECTOR_TAUTOLOGICAL
    PRUNING_EQUIVALENT
    PROVES_TOO_MUCH

    ROUTE_A_REJECTED
    ROUTE_B_LOCKED

The positive and negative lines are intentionally retained together. The same-object Fredholm identity is real; so is the theorem that it forgets the computation. This combination is the complete result of SD-C21.
