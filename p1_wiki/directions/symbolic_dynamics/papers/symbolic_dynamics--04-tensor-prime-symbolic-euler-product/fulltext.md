---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--04-tensor-prime-symbolic-euler-product"
canonical_tex: "symbolic_dynamics/papers/04-tensor-prime-symbolic-euler-product/main.tex"
canonical_pdf: "symbolic_dynamics/papers/04-tensor-prime-symbolic-euler-product/main.pdf"
source_sha256: "af3ec76bd305cda0fd5448683f092ff013489dde24eda57caaea4a0379baa225"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Tensor Primes of Full Shifts and a Symbolic Fredholm Realization of the Riemann Euler Product

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/04-tensor-prime-symbolic-euler-product>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/04-tensor-prime-symbolic-euler-product/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/04-tensor-prime-symbolic-euler-product/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/04-tensor-prime-symbolic-euler-product/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/04-tensor-prime-symbolic-euler-product/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We construct a single countable symbolic suspension from the symmetric monoidal skeleton of finite full shifts. Cartesian product gives $F_m\boxtimes F_n\cong F_{mn}$ and topological entropy gives $h_{\mathrm{top}}(F_n)=\log n$; hence the nonunit tensor atoms are exactly the full $p$-shifts and their entropy is the intrinsic clock $\log p$. A canonical diagonal atom shift turns these categorical atoms into genuine primitive periodic loops. Its weighted transfer operator on $\ell^2$ is diagonal with eigenvalues $p^{-s}$ and is trace class for $\operatorname{Re}s>1$. Consequently $\det(I-\mathcal L_s)=\zeta(s)^{-1}$, its orbit zeta is $\zeta(s)$, and logarithmic differentiation gives the exact von Mangoldt prime-power ledger. We prove that any positive recurrent component mixing two distinct atom labels creates a forbidden composite term, so the apparently degenerate diagonal grammar is forced by exactness. An opaque finite registry certifies all Euler, Möbius, and von Mangoldt coefficients through $256$ and rejects random, additive, shifted-law, and free-mixing controls. This closes the arithmetic, primitive-orbit, and Fredholm layers of Route A for one source-locked symbolic object. It does not supply the Gamma factor, functional equation, or an operator continuation through the critical strip. Indeed, the ungraded trace-class family cannot extend holomorphically through a zeta zero. We therefore isolate a graded symbolic transfer complex as the next concrete same-family target rather than claim an RH or Hilbert--Pólya result.
author:
- Anonymous Authors
bibliography:
- references.bib
date: 'August 12, 2026'
title: |
  Tensor Primes of Full Shifts and a Symbolic\
  Fredholm Realization of the Riemann Euler Product
```

## Markdown 正文

# Introduction

The Euler product already has the syntax of a periodic-orbit expansion: primes behave like primitive objects, prime powers like repetitions, and $\log p$ like an orbit length differentiated from an exponential weight. The difficult Route-A question is not whether one can rewrite that identity, but whether a symbolic object supplies every coordinate without a prime table, a log-prime roof assignment, or a zero fit.

Earlier work in this project found complementary failures. A recursive wheel sieve produced rational primes endogenously but had no periodic points; natural continued-fraction shifts had Fredholm determinants but the wrong primitive species. Exact decoding the wheel clock into a periodic factor was then ruled out. The present paper changes the invariant: rational primes are defined as indecomposable *symbolic systems* under a natural product.

Full shifts are the smallest possible laboratory. Their Cartesian product multiplies alphabet cardinalities, while topological entropy logs that multiplication. Direct-prime symbolic systems and product factorization have an established literature [@lind1984; @meyerovitch2017; @kopra2023], and entropy has a natural monoidal interpretation [@delvenne2019]. Our aim is not to rename these facts as new. It is to compose them with a fixed orbitification, a trace-class determinant, exact controls, and the project's Route-A gates.

The outcome, summarized in [\[fig:route-a-chain\]](#fig:route-a-chain){reference-type="ref" reference="fig:route-a-chain"}, is unusually sharp. The arithmetic source, primitive ledger, and analytic determinant are exact in the Euler half-plane. Positive symbolic mixing is incompatible with the von Mangoldt support, so reducibility is forced rather than hidden. At the same time, the ordinary trace-class operator cannot be continued through a nontrivial zeta zero. A completed Riemann determinant therefore needs new, intrinsically graded symbolic structure; merely estimating the same diagonal operator harder cannot work.

We keep two notions separate throughout. A *tensor atom* is a full shift indecomposable under Cartesian product. A *temporal primitive orbit* belongs to the derived atom-loop shift. Tensor atoms are not primitive necklaces inside their representing full shifts. This firewall avoids conflating categorical and temporal factorization, whose classical orbit algebras are described by necklace and Witt-vector theory [@metropolisrota1983; @dresssiebeneicher1989].

# The monoidal full-shift source

For $n\geq1$, let $$F_n=(\{1,\ldots,n\}^{\mathbb Z},\sigma_n)$$ be the two-sided full $n$-shift. Let $\mathsf{FSh}$ be the set of their topological conjugacy classes and use the Cartesian product as the symmetric monoidal operation $\boxtimes$.

[\[prop:skeleton\]]{#prop:skeleton label="prop:skeleton"} For $m,n\geq1$, $$[F_m]\boxtimes[F_n]=[F_{mn}],\qquad
 h_{\mathrm{top}}(F_n)=\log n,$$ and the reciprocal Artin--Mazur determinant of $F_n$ is $1-nz$. Consequently $\mathcal N([F_n]):=\exp(h_{\mathrm{top}}(F_n))=n$ is a multiplicative norm on $\mathsf{FSh}$.

Choose a bijection between the product alphabet $\{1,\ldots,m\}\times\{1,\ldots,n\}$ and an $mn$-letter alphabet and apply it coordinatewise. The full-shift entropy is the logarithm of alphabet size. Finally $\#\operatorname{Fix}(\sigma_n^r)=n^r$, whence $$\exp\left(-\sum_{r\geq1}\frac{n^rz^r}{r}\right)=1-nz.$$

A class $a\in\mathsf{FSh}\setminus\{[F_1]\}$ is a tensor atom if $a=b\boxtimes c$ with $b,c\in\mathsf{FSh}$ implies that $b$ or $c$ is $[F_1]$.

[\[thm:tensor-primes\]]{#thm:tensor-primes label="thm:tensor-primes"} The tensor atoms of $\mathsf{FSh}$ are exactly $[F_p]$ for rational primes $p$. Every $[F_n]$ admits the unique tensor factorization $$[F_n]=\mathop{\boxtimes}_{p}[F_p]^{\boxtimes v_p(n)}.$$ Moreover the atom clock is intrinsic: $h_{\mathrm{top}}(F_p)=\log p$.

By [\[prop:skeleton\]](#prop:skeleton){reference-type="ref" reference="prop:skeleton"}, a nontrivial tensor decomposition of $[F_n]$ is equivalent to a factorization $n=ab$ with $a,b>1$. Thus indecomposability is equivalent to primality. Existence and uniqueness are the fundamental theorem of arithmetic transported through the product conjugacy. The clock identity is again [\[prop:skeleton\]](#prop:skeleton){reference-type="ref" reference="prop:skeleton"}.

This theorem is exact but intentionally transparent: the monoidal skeleton is isomorphic to $(\mathbb N_{\geq1},\times)$. Its value for Route A is that the operation, norm, and atoms are all registered symbolic invariants. A prime list and a hand-assigned $\log p$ roof are absent.

The ordinary temporal orbit structure of $F_n$ is different. Its primitive period-$r$ orbit count is $$O_r(F_n)=\frac1r\sum_{d\mid r}\mu(d)n^{r/d},$$ and its Artin--Mazur zeta is $(1-nz)^{-1}$ [@artinmazur1965; @bowenlanford1970; @byszewskigraffward2021]. These necklaces are not the tensor atoms in [\[thm:tensor-primes\]](#thm:tensor-primes){reference-type="ref" reference="thm:tensor-primes"}.

# From tensor atoms to temporal primitive orbits

Let $\mathcal A=\operatorname{At}(\mathsf{FSh})$. We now apply a fixed construction that depends only on the atom set.

[\[def:atom-shift\]]{#def:atom-shift label="def:atom-shift"} Define the one-sided countable Markov shift $$Y_\otimes=\{y=(a_j)_{j\geq0}\in\mathcal A^{\mathbb N}:a_{j+1}=a_j
  \text{ for every }j\},$$ with left shift $S$. Its adjacency matrix is the identity on $\mathcal A$. Equip it with the roof $$\tau(y)=h_{\mathrm{top}}(a_0).$$ The suspension is denoted $(Y_\otimes^\tau,\phi_t)$.

The phase space is a countable union of fixed symbolic points. It is neither compact nor mixing, but it is one autonomous symbolic system. Atom extraction and orbitification are both universal rules and do not change with a cutoff.

[\[thm:ledger\]]{#thm:ledger label="thm:ledger"} For every rational prime $p$, $Y_\otimes$ has exactly one primitive period-one orbit $\gamma_p$, represented by the constant symbol $[F_p]$. The suspension length of its $r$-fold repetition is $$T_{p,r}=r\tau([F_p])=r\log p=\log(p^r).$$ There are no mixed-symbol primitive cycles.

Identity adjacency forces every admissible sequence to be constant, hence each symbol supplies one primitive fixed point and no orbit uses two symbols. The roof statement follows from [\[thm:tensor-primes\]](#thm:tensor-primes){reference-type="ref" reference="thm:tensor-primes"}; suspension repetition adds roof lengths.

The diagonal adjacency is a modeling choice, but not an arbitrary prime-indexed table: its alphabet is selected by tensor indecomposability and its roof is selected by entropy. In [5](#sec:no-mixing){reference-type="ref" reference="sec:no-mixing"} we show that, under positive weights, exact von Mangoldt support forces this separation.

Because $Y_\otimes$ has countably many fixed points, its unweighted Artin--Mazur fixed-point count is infinite. The zeta used below is the *entropy-weighted Ruelle/suspension zeta*; it is not an ordinary unweighted Artin--Mazur zeta. Likewise, the monoidal object inventory and the atom-loop system are two successive constructions, not isomorphic dynamical systems.

Functorial orbit counting under products is classical [@pakapongpunward2009]. Here the order of operations matters: first factor the symbolic objects in the monoidal category, then make the atoms temporal loops. We do not identify the temporal orbit monoid of $F_n$ with the tensor monoid of full-shift objects.

# Fredholm determinant and the Euler ledger

Identify a function on $Y_\otimes$ with its values on $\mathcal A$ and set $H_\otimes=\ell^2(\mathcal A)$. The weighted Ruelle operator for the identity adjacency is $$(\mathcal L_s f)(a)=e^{-s\tau(a)}f(a).$$ Thus $\mathcal L_s e_{[F_p]}=p^{-s}e_{[F_p]}$ in the canonical basis.

[\[thm:fredholm\]]{#thm:fredholm label="thm:fredholm"} For $\operatorname{Re}s>1$, $\mathcal L_s$ is trace class and depends holomorphically on $s$ in trace norm. In that half-plane, $$\begin{aligned}
 \operatorname{Tr}(\mathcal L_s^r)&=\sum_p p^{-rs},\label{eq:trace}\\
 D_\otimes(s):=\det(I-\mathcal L_s)&=\prod_p(1-p^{-s})=\zeta(s)^{-1},\label{eq:det}\\
 Z_\otimes(s):=D_\otimes(s)^{-1}&=\zeta(s).\label{eq:zeta}\end{aligned}$$

For $\sigma=\operatorname{Re}s>1$, $$\|\mathcal L_s\|_1=\sum_p|p^{-s}|=\sum_p p^{-\sigma}<\infty.$$ Uniform convergence on compact sub-half-planes gives trace-norm holomorphy. The diagonal spectrum yields [\[eq:trace\]](#eq:trace){reference-type="eqref" reference="eq:trace"}. The standard trace-class determinant identity then gives $$\det(I-\mathcal L_s)
 =\exp\left(-\sum_{r\geq1}\frac{\operatorname{Tr}(\mathcal L_s^r)}r\right)
 =\prod_p(1-p^{-s}).$$ Euler's product proves the final equalities. This is also the weighted primitive-orbit formula of [\[thm:ledger\]](#thm:ledger){reference-type="ref" reference="thm:ledger"}; compare the general transfer operator framework in @ruelle2002.

[\[cor:coefficients\]]{#cor:coefficients label="cor:coefficients"} For $\operatorname{Re}s>1$, $$\begin{aligned}
 Z_\otimes(s)&=\sum_{n\geq1}n^{-s},\\
 D_\otimes(s)&=\sum_{n\geq1}\mu(n)n^{-s},\\
 -\frac{Z_\otimes'(s)}{Z_\otimes(s)}
 &=\sum_p\sum_{r\geq1}(\log p)p^{-rs}
 =\sum_{n\geq1}\Lambda(n)n^{-s}.\end{aligned}$$

The von Mangoldt amplitude is not a potential inserted into the dynamics: it is the derivative of the entropy clock. Formally evaluating an individual repeat term at $s=\tfrac12+iE$ gives $$(\log p)p^{-r/2}e^{-iEr\log p},$$ which is the prime-power phase and amplitude requested by the explicit formula. We make no claim that the Euler series converges on that line; its continuation is precisely the A3 problem.

# Positive no-mixing is forced {#sec:no-mixing}

The identity adjacency might appear to conceal a prime-indexed disjoint union. The next statement shows that separation is forced throughout a large natural class of positive symbolic realizations.

Consider a locally finite directed graph whose recurrent vertices carry atom labels $p(v)$ and vertex roof $\log p(v)$. Give every primitive cycle $c$ a strictly positive multiplicative weight $w_c$. Put $$N(c)=\prod_{v\in c}p(v),\qquad T(c)=\log N(c),$$ with occurrences counted along the cycle, and form $$Z_G(s)=\prod_{c\ \mathrm{primitive}}
       (1-w_cN(c)^{-s})^{-1}$$ in a nonempty right half-plane where the orbit expansion converges absolutely.

[\[thm:no-mixing\]]{#thm:no-mixing label="thm:no-mixing"} If a strongly connected component contains recurrent vertices with two distinct atom labels $p\neq q$, then $-Z_G'/Z_G$ has a strictly positive coefficient at an integer divisible by both $p$ and $q$. Consequently it cannot equal the von Mangoldt Dirichlet series. Any exact positive symbolic realization of that series has label-homogeneous recurrent components. If every primitive cycle has unit weight, exact multiplicity one further leaves one primitive loop per atom.

Strong connectivity supplies a closed directed walk visiting vertices with labels $p$ and $q$. Removing repetitions produces a primitive cycle $c$ whose mass $N(c)$ contains at least the two distinct prime factors $p,q$. The logarithmic derivative contains $$\sum_{r\geq1}T(c)w_c^rN(c)^{-rs},$$ so its coefficient at $N(c)$ is positive. Contributions of other cycles with the same mass are nonnegative and cannot cancel it. But $\Lambda(N(c))=0$ because $N(c)$ is not a prime power. Thus the ledgers cannot agree. Under unit primitive weights, multiple primitive loops of the same atom likewise overcount the coefficient at that prime.

The two-atom calculation makes the obstruction visible. With $x=p^{-s}$ and $y=q^{-s}$, isolated loops give $$Z_{\mathrm{iso}}=\frac1{(1-x)(1-y)},$$ whose coefficient at $xy$ is one and whose logarithmic derivative has no $xy$ term. Free concatenation gives $$Z_{\mathrm{free}}=\frac1{1-x-y},$$ whose $xy$ coefficient is two and whose negative logarithmic derivative has coefficient $\log p+\log q$ there. The former treats $pq$ as a product of two primitive occupations; the latter incorrectly promotes ordered mixed words to primitive trace data.

Signed or complex cancellations are not covered by [\[thm:no-mixing\]](#thm:no-mixing){reference-type="ref" reference="thm:no-mixing"}. They are exactly what a future graded symbolic system would have to derive intrinsically. Choosing signs after seeing the target would fail the arithmetic source gate.

# Exact finite certification and controls

The computation registers $F_1,\ldots,F_N$ as opaque objects. Candidate-side code sees their partial tensor table, entropy, the reciprocal Artin--Mazur linear coefficient, and fixed counts through period four. It marks an object as an atom exactly when no registered pair of nonunits tensors to it. A separate primality predicate is used only after recovery for scoring.

[\[prop:prefix\]]{#prop:prefix label="prop:prefix"} For every cutoff $N$, tensor indecomposability of each $F_n$ with $n\leq N$ is decided exactly from the truncated registry. The resulting Euler, reciprocal, and logarithmic-derivative Dirichlet coefficients are exact for all masses $n\leq N$.

Every proper factor of an integer $n\leq N$ lies in the registry. Hence a decomposition is never missed. All atom factors of every registered object are also present. Unique factorization then determines the Euler coefficients, Möbius coefficients, and prime-power support through $N$.

::: {#tab:main-experiment}
    $N$   recovered atoms   $\pi(N)$     UFD   $Z$ coefficients   $\mu/\Lambda$
  ----- ----------------- ---------- ------- ------------------ ---------------
     32                11         11   1.000              1.000           1.000
     64                18         18   1.000              1.000           1.000
    128                31         31   1.000              1.000           1.000
    256                54         54   1.000              1.000           1.000

  : Exact atom and coefficient recovery. The prime predicate appears only in the sealed score columns.
:::

All rows of [1](#tab:main-experiment){reference-type="ref" reference="tab:main-experiment"} pass. At $N=256$, $64$ matched-size random atom sets achieve only $0.2607\pm0.0327$ Euler-coefficient accuracy and relative $\Lambda$ error $1.5823\pm0.0806$. A shifted multiplication law has perfect abstract unique factorization but only $0.1758$ accuracy with the intrinsic full-shift entropy clock. It becomes exact only after the post-hoc substitution $\log(n-1)$, an explicit proves-too-much witness.

Finally, all $28$ pairs among the first eight recovered atoms were tested at four cutoffs. Isolated loops always give coefficient one at $pq$ and zero in the logarithmic derivative; free mixing always gives coefficient two and the spurious positive value $\log(pq)$. This is an exact finite implementation of [\[thm:no-mixing\]](#thm:no-mixing){reference-type="ref" reference="thm:no-mixing"}, not a statistical preference. Code, raw tables, seeds, and the machine-readable coefficient ledger accompany the paper.

# Route-A result and the critical-strip frontier

The frozen evaluator returns $$\begin{split}
(&\texttt{A0\_ANALYTIC\_ARITHMETIC\_ORIGIN},
\texttt{A1\_PASS\_ANALYTIC},\\
&\texttt{A2\_ANALYTIC\_DETERMINANT},
\texttt{A3\_PARTIAL\_ANALYTIC\_STRUCTURE},
\texttt{A4\_FAIL}).
\end{split}$$ The overall status is `ROUTE_A_ANALYTIC_CANDIDATE`. A0 is carried by tensor indecomposability and entropy, A1 by the atom-loop suspension, and A2 by [\[thm:fredholm\]](#thm:fredholm){reference-type="ref" reference="thm:fredholm"}. No coordinates are borrowed from another candidate.

A3 is only partial. The scalar identity $Z_\otimes=\zeta$ has a unique known meromorphic continuation, but the present symbolic operator does not produce that continuation. It also lacks the archimedean Gamma factor, pole removal, $s\leftrightarrow1-s$ duality, Riemann--von Mangoldt zero count, and a natural Weil Hermitian compression.

[\[thm:continuation-obstruction\]]{#thm:continuation-obstruction label="thm:continuation-obstruction"} Let $U\subset\mathbb C$ be a connected domain containing a nonempty open set in $\operatorname{Re}s>1$ and a nontrivial zero $\rho$ of $\zeta$. There is no holomorphic trace-class family $\widetilde{\mathcal L}_s$ on a fixed Hilbert space such that $\widetilde{\mathcal L}_s=\mathcal L_s$ on that open set and $\det(I-\widetilde{\mathcal L}_s)$ continues the same determinant along $U$.

The Fredholm determinant of a holomorphic trace-class family is holomorphic. On the initial open set it equals $1/\zeta(s)$ by [\[thm:fredholm\]](#thm:fredholm){reference-type="ref" reference="thm:fredholm"}. Uniqueness of analytic continuation forces equality with the meromorphic continuation of $1/\zeta$ wherever both are defined in $U$. The latter has a pole at $\rho$, contradicting holomorphy.

This theorem does not rule out a quotient of determinants, a meromorphic operator family, or a graded transfer complex. It says that the current ungraded trace-class family cannot simply be pushed across the critical strip. Nor does the naive double $\mathcal L_s\oplus\mathcal L_{1-s}$ help: the first block is trace class for $\operatorname{Re}s>1$, the second for $\operatorname{Re}s<0$, so there is no common nuclear strip.

[\[conj:graded-completion\]]{#conj:graded-completion label="conj:graded-completion"} There exists a functorially defined $\mathbb Z/2$-graded symbolic transfer complex built from the full-shift tensor product, entropy norm, and an intrinsic past--future duality, such that:

1.  its positive prime-power trace reduces to the SD-C07 ledger in the Euler half-plane;

2.  mixed-atom traces cancel by a derived, pre-registered grading;

3.  its superdeterminant or determinant quotient has a controlled meromorphic continuation and a dynamical $s\leftrightarrow1-s$ duality;

4.  the archimedean normalization is generated by the same symbolic construction rather than multiplied in afterward.

This is a research target, not evidence for RH. Random parity, a copied Gamma factor, or signs chosen after inspecting zeros would falsify its source lock. Any operator-algebraic or Hamiltonian realization remains a `ROUND2_CLUE`; Route B is not invoked.

# Conclusion

The full-shift tensor skeleton supplies a compact exact Route-A story. Its atoms are rational primes, its entropy is the logarithmic prime clock, its canonical atom-loop suspension turns tensor powers into orbit repetitions, and its Ruelle determinant is the inverse Euler product. The same source produces the full von Mangoldt ledger without a prime table, a fitted phase, or a hand-written potential.

This is not yet an explanation of the Riemann zeros. The base is maximally reducible, the determinant has inverse orientation, and its trace-class domain stops at $\operatorname{Re}s=1$. Those weaknesses are now structural rather than vague. Positive mixing is impossible if the exact prime-power support is retained, and ungraded holomorphic trace-class continuation is impossible through a zeta zero.

The project can therefore move forward with a sharper bet: the missing ingredient is not another arithmetic generator but an intrinsic symbolic grading and duality. Constructing the complex in [\[conj:graded-completion\]](#conj:graded-completion){reference-type="ref" reference="conj:graded-completion"}, or proving it impossible under a useful low-complexity source lock, is the next decisive Route-A step.

# Proof and scope audit

## Same-object chain

Every credited coordinate belongs to SD-C07:

0.96L0.20X Coordinate & Frozen source\
Prime object & tensor indecomposability inside $\mathsf{FSh}$\
Clock & topological entropy of the same atom\
Primitive orbit & constant loop in $Y_\otimes$\
Repetition & temporal repeat in the same suspension\
Weight $\log p$ & derivative of the same entropy roof\
Transfer operator & weighted preimage operator of identity adjacency\
Determinant & ordinary Fredholm determinant on $\ell^2(\mathcal A)$\

The wheel sieve, Gauss/Mayer operator, Knauf signs, external prime tables, and Riemann zeros supply none of these coordinates.

## Control logic

The main claim uses more than abstract unique factorization. It requires the commuting square $$\exp h(X\boxtimes Y)=\exp h(X)\exp h(Y)
 =\mathcal N(X)\mathcal N(Y)=\mathcal N(X\boxtimes Y),$$ with $\mathcal N(F_n)=n$ independently recoverable from fixed counts and the linear Artin--Mazur determinant. The shifted-law control preserves an abstract UFD but breaks this square; a perfect Riemann ledger returns only after an external clock is fitted. The free-mixing control preserves the atoms and clock but breaks the logarithmic prime-power support. Together they isolate the exact package being credited.

## Analytic boundary

The identity theorem permits the scalar function $Z_\otimes$ to inherit the known meromorphic continuation of $\zeta$. This is an arithmetic identity, not an operator estimate. A3 credit is therefore partial. No root errors, missing-zero counts, or fitted test regions are reported, because no target zeros are used. All such Route-A fields are marked `not_applicable` in the machine-readable evaluation.

## Primary-family boundary

All active constructions are shifts, symbolic suspensions, their entropy, or their transfer operators. Operator algebras, quantum statistical mechanics, Hamiltonians, scattering systems, and arithmetic geometry are not developed. Their possible relevance is recorded only as `ROUND2_CLUE`. Since A4 fails, the Route-B evaluator is not invoked.
