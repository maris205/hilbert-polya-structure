---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--21-successor-divisor-cycle-flood"
canonical_tex: "symbolic_dynamics/papers/21-successor-divisor-cycle-flood/main.tex"
canonical_pdf: "symbolic_dynamics/papers/21-successor-divisor-cycle-flood/main.pdf"
source_sha256: "4ed13e538dcdf8d8ed0fce6c4e0c4344a011649ee7d0d6b4081b61d1044845f4"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The Successor--Divisor Shift: A Sharp Trace-Class Determinant with an All-Length Primitive-Cycle Flood

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/21-successor-divisor-cycle-flood>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/21-successor-divisor-cycle-flood/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/21-successor-divisor-cycle-flood/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/21-successor-divisor-cycle-flood/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/21-successor-divisor-cycle-flood/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Starting from full shifts alone, we expose successor and tensor-factor relations through the countable directed graph $$n\longrightarrow d
   \quad\Longleftrightarrow\quad
   d\ge2,\qquad d\mid n+1.$$ The resulting one-sided countable Markov shift is strongly connected and mixing, yet it contains the simple primitive cycle $C_k=(k,k+1,\ldots,2k-1)$ for every $k\ge2$. We prove a finite-confinement theorem: every length-$r$ closed walk has maximum at most $2r-1$, and equality identifies $C_r$ up to rotation. Thus each infinite-graph trace has an exact finite certificate. For the natural endpoint-weighted adjacency $$L_se_n=\sum_{\substack{d\mid n+1\\d\ge2}}(nd)^{-s}e_d,$$ a row-nuclear decomposition and a Fourier extraction of the successor diagonal give the sharp equivalence $$L_s\in\mathcal S_1\quad\Longleftrightarrow\quad
   \operatorname{Re}s>\tfrac12.$$ This yields a genuine same-object Fredholm determinant throughout that open half-plane. It nevertheless fails the marked prime Euler target before any zero calculation: the graph has no loops, hence $\operatorname{Tr}L_s=0$, whereas the target's first trace is nonzero. Moreover, every natural orbit norm is a composite square. A two-quotient pruning retains the determinant threshold and the entire cycle flood, proving zero selectivity margin for the direct grammar.
author:
- Anonymous Authors
bibliography:
- references.bib
date: 'August 14, 2026'
title: |
  The Successor--Divisor Shift:\
  A Sharp Trace-Class Determinant with an\
  All-Length Primitive-Cycle Flood
```

## Markdown 正文

# Introduction {#sec:introduction}

Arithmetic symbolic dynamics faces a recurrence problem before it faces a spectral one. A transient symbolic verifier can recognize a prescribed integer property, but transient computation leaves no primitive periodic orbit and is therefore invisible to a dynamical determinant. Closing every verification path into a loop restores recurrence at the cost of a long clock, often destroying the compactness required by Fredholm theory. This paper studies a third possibility: discard the verifier architecture and let a local arithmetic relation among full shifts generate recurrence directly.

For the full shift $F_n$ on $n$ symbols, alphabet product and alphabet sum realize multiplication and addition of cardinalities. In particular, $$F_{n+1}\cong F_d\boxtimes F_q
 \quad\Longleftrightarrow\quad
 n+1=dq.$$ Keeping every nonunit factor $d$ produces the *successor--divisor graph* $$n\to d\iff d\mid n+1,\qquad n,d\ge2.$$ The relation contains no prime list and no primality test. It is an intrinsic arithmetic change of state between full-shift objects.

The first surprise is positive. The graph is strongly connected and mixing, and its natural weighted adjacency is trace class on the sharp half-plane $\operatorname{Re}s>1/2$. Thus a recurrent arithmetic shift can carry a genuine Fredholm determinant very close to the line relevant to the Session's long-term question. The second surprise is decisive and negative. The same two transitions that create recurrence also create a simple primitive cycle at every length: $$k\to k+1\to\cdots\to2k-1\to k.$$ Recurrence is obtained, but arithmetic selectivity is lost.

## Main results

Our contributions are four exact statements.

1.  **Recurrent topology and an all-length flood.** We give constructive paths proving strong connectivity and mixing. For every $k\ge2$, the cycle $C_k=(k,k+1,\ldots,2k-1)$ is simple and primitive. More generally, every nonunit divisor $d\mid r$ gives a different primitive length-$r$ class.

2.  **Exact finite confinement.** If $M$ is the maximal vertex on a length-$r$ closed walk, the first step from $M$ is a proper-divisor drop, whereas every subsequent edge can increase its source by at most one. This gives $$M\le2r-1.$$ Equality forces $C_r$. Consequently the infinite trace of order $r$ is exactly certified by the induced prefix through $2r-1$.

3.  **A sharp trace-class theorem.** With endpoint roof $\tau(n,d)=\log n+\log d$, we prove $$L_s\in\mathcal S_1\quad\Longleftrightarrow\quad\operatorname{Re}s>\frac12.$$ The upper bound comes from a rank-one row decomposition whose $d$-th nuclear norm is $O(d^{-2\operatorname{Re}s})$. Necessity follows by Fourier extraction of the successor weighted shift.

4.  **A coefficientwise target obstruction and a zero-margin control.** The source graph has no loops, so its marked determinant has zero linear coefficient. The marked prime Euler determinant does not. Every source orbit norm is also a composite square. Finally, the severe pruning that retains only quotient labels $q=1,2$ preserves strong connectivity, mixing, every $C_k$, and the sharp trace-class threshold.

The combination matters. The determinant is not rejected because it lacks analytic control: its own-object analytic theorem is unusually clean. Rather, it is rejected because the primitive-orbit species is exactly wrong. Marked coefficients expose this before zero locations can obscure the comparison.

## Relation to determinant and zeta traditions

Periodic-orbit zeta functions originate in the Artin--Mazur framework and their finite-shift determinant realization is classical [@ArtinMazur1965; @BowenLanford1970]. Countable Markov shifts require additional recurrence and convergence care [@GurevichSavchenko1998; @Sarig1999]. We do not invoke a general thermodynamic formalism to prove the candidate-specific operator theorem. Instead, a direct trace-ideal argument first establishes trace class, after which standard Fredholm determinant facts apply [@Simon1977].

## Strict scope

The whole paper stays inside Symbolic Dynamics. Its strongest analytic object is $$D_{\mathrm{SD}}(s,z)=\det(I-zL_s),\qquad \operatorname{Re}s>\frac12.$$ This is the determinant of the frozen successor--divisor shift. We prove no continuation to the boundary, functional equation, Gamma completion, Riemann--von Mangoldt law, Weil compression, RH statement, or Hilbert--Pólya operator. No target-zero data are used. The final route tuple is $$\begin{aligned}
(&\mathrm{A0\_STRUCTURAL\_ARITHMETIC\_RELATION},
  \mathrm{A1\_WEAK},\\
 &\mathrm{A2\_ANALYTIC\_DETERMINANT},
  \mathrm{A3\_FAIL},
  \mathrm{A4\_FAIL}),
\end{aligned}$$ with overall verdict $\mathrm{ROUTE\_A\_REJECTED}$.

## Organization

sets the literature and novelty boundary. freezes the full-shift source, graph, roof, and operator. prove recurrence, the cycle flood, and finite confinement. establish the sharp operator theorem and determinant ledger. give the target obstruction and pruning controls. records the strict route decision and the minimal next symbolic obligation.

# Classical and literature boundary {#sec:literature}

## Periodic-orbit and countable-shift foundations

The periodic-point zeta function of @ArtinMazur1965 organized fixed points by temporal repetition. For restrictions of finite shifts, @BowenLanford1970 established the determinant paradigm relating closed paths, primitive cycles, and a finite adjacency matrix. These works fix the combinatorial convention used here: a primitive orbit is a directed closed word modulo cyclic rotation, not reflection, and every rooted closed word is a temporal power of a unique primitive class.

The present graph has countably many vertices. Generating functions and dynamic zeta factorizations for countable symbolic Markov chains were developed by @GurevichSavchenko1998; thermodynamic formalism for countable Markov shifts was developed by @Sarig1999. Our phase space belongs to that broad symbolic setting, but our operator is deliberately described as a weighted vertex adjacency on $\ell^2$. We do not identify it with a Ruelle operator on a Hölder or variation-controlled function space.

## Infinite graph determinants

Once trace class is known, the analytic determinant facts we use are standard trace-ideal results [@Simon1977]. Candidate-specific content lies in proving the exact trace-class domain, not in reproving general Fredholm theory. @Deitmar2015 obtained Fredholm determinant formulas for Ihara zeta functions of infinite weighted graphs of finite total weight. That is close in analytic technology but different in object: Ihara theory uses nonbacktracking graph data, while SD-C23 freezes the ordinary directed vertex adjacency generated by $d\mid n+1$.

## Arithmetic graph neighbors

Several uses of divisibility in graph theory are nearby only at the level of vocabulary. @PhunphayapEtAl2025 define directed integer graphs using values of arithmetic functions on multiples. @McNew2022 studies the finite ordinary divisor graph on $[1,n]$ in connection with permutation cycle covers. @PeruccaSeureWolff2024 combine additive and multiplicative transitions on finite residue sets. None of these objects has the shifted-factor edge $n\to d\iff d\mid n+1$, the countable Markov phase space, or the operator family considered here.

\@L0.27YY@ Source family & Shared ingredient & Boundary from SD-C23\
Artin--Mazur; Bowen--Lanford & Periodic points, primitive/repetition ledger, determinant & Compact or finite-shift setting; no successor--divisor graph\
Gurevich--Savchenko; Sarig & Countable symbolic Markov chains & General formalism; no $2r-1$ confinement or sharp row theorem\
Simon & Trace ideals and Fredholm determinants & Functional analysis after, not proof of, the arithmetic operator bound\
Deitmar & Infinite weighted graph zeta determinants & Ihara/nonbacktracking object rather than directed vertex adjacency\
Arithmetic divisor graphs & Integer divisibility in graph transitions & Finite, unshifted, modular, or arithmetic-function transitions\

## Search-bounded novelty statement

We searched arXiv, publisher and DOI indexes, MathNet, AMS, SIAM, and Cambridge through 2026-08-14 for successor--divisor graphs, directed graphs with $d\mid n+1$, shifted divisor graphs, countable arithmetic Markov shifts, and weighted infinite-graph determinants. To our knowledge within that bounded search, we found no directly comparable analysis of the successor--divisor countable Markov shift with the $2r-1$ confinement and sharp trace-class theorem proved below. This is not an absolute priority claim; it only records the collision search used to position the result.

# Full-shift source and the frozen symbolic object {#sec:source}

## A semiring skeleton of full shifts

For a finite alphabet $A_n$ of cardinality $n$, write $$F_n=A_n^{\mathbb Z}$$ for the two-sided full shift, up to topological conjugacy. We use two alphabet-level operations: $$F_m\boxtimes F_n
 :=F_{A_m\times A_n}\cong F_{mn},$$ $$F_m\boxplus F_n
 :=F_{A_m\sqcup A_n}\cong F_{m+n}.$$ The second is alphabet-sum followed by the full-shift functor; it is not a topological disjoint union of $F_m$ and $F_n$. The only numerical invariant used to set the roof is the full-shift entropy $$h(F_n)=\log n.$$ Define the successor object $$S(F_n)=F_n\boxplus F_1\cong F_{n+1}.$$ The displayed family realizes the positive-integer semiring in one conjugacy-class representative per alphabet size. We claim no stronger categorical universality.

[\[def:graph\]]{#def:graph label="def:graph"} Let $G_{\mathrm{SD}}=(V,E)$, where $$V=\{2,3,\ldots\},$$ and $$n\to d
 \quad\Longleftrightarrow\quad
 d\ge2,\qquad d\mid n+1.$$ Equivalently, an edge is the unique exposed factorization $$S(F_n)\cong F_d\boxtimes F_q,
 \qquad
 q=q(n,d):=\frac{n+1}{d}\in\mathbb N.$$

The quotient label is available for auditing and pruning, but is not a prime predicate. In particular, the full source grammar accepts every nonunit factor of $n+1$.

## Countable Markov shift and orbit convention

The one-sided phase space is $$X_{\mathrm{SD}}^{+}
 =
 \{(n_0,n_1,\ldots)\in V^{\mathbb N}:
   n_j\to n_{j+1}\text{ for every }j\}.$$ A rooted period-$r$ word is a closed path $$n_0\to n_1\to\cdots\to n_{r-1}\to n_0.$$ An orbit identifies cyclic rotations but not reflections. It is primitive when the closed word is not a positive temporal power of a shorter word. These conventions separate three quantities that must not be conflated: rooted trace terms, primitive rotation classes, and temporal repetitions.

## Roof, weighted adjacency, and determinant

[\[def:operator\]]{#def:operator label="def:operator"} On an edge $n\to d$, set $$\tau(n,d)=h(F_n\boxtimes F_d)=\log n+\log d.$$ On $$\mathcal H=\ell^2(V)$$ with standard basis $(e_n)_{n\ge2}$, define the column-source operator $$L_se_n
 =
 \sum_{\substack{d\ge2\\d\mid n+1}}
 (nd)^{-s}e_d.$$

Each source column is finite because $n+1$ has finitely many divisors. For a closed orbit $$\gamma=(n_0,\ldots,n_{\ell-1}),
 \qquad n_\ell=n_0,$$ define $$N(\gamma)=\prod_{j=0}^{\ell-1}n_j.$$ Every cyclic vertex occurs once as a source and once as a target, hence $$\label{eq:cyclic-weight}
\prod_{j=0}^{\ell-1}(n_jn_{j+1})^{-s}
=N(\gamma)^{-2s}.$$ The factor two is forced by the frozen roof; it is not removed after target comparison.

Once trace class is proved, the whole determinant convention is $$D_{\mathrm{SD}}(s,z)=\det(I-zL_s).$$ There are no character blocks or hidden components in this paper: every trace and primitive factor belongs to this whole adjacency.

## Source firewall

The construction uses only integer successor, divisor enumeration, multiplication/equality, alphabet cardinality, and full-shift entropy. It uses no prime inventory, von Mangoldt weights, target zeros, or fitted parameter. Target comparison begins only after have been frozen.

# Recurrent topology and the primitive-cycle flood {#sec:topology}

The edge grammar has two elementary consequences: $$n\to n+1$$ for every $n\ge2$, because $n+1$ divides itself, and $$n\to d\quad\Longrightarrow\quad d\le n+1.$$ The successor edges supply ascent. Small factors of $n+1$ supply descent.

[\[thm:mixing\]]{#thm:mixing label="thm:mixing"} The graph $G_{\mathrm{SD}}$ is strongly connected. Moreover, for every $u,v\in V$, there is $N(u,v)$ such that every $n\ge N(u,v)$ occurs as the length of a path from $u$ to $v$. Hence $X_{\mathrm{SD}}^{+}$ is topologically mixing in the path sense.

If $n$ is odd, then $2\mid n+1$, so $n\to2$. If $n$ is even, then $$n\to n+1\to2.$$ Thus every vertex reaches $2$ in at most two edges. Conversely, the successor chain $$2\to3\to\cdots\to m$$ reaches any $m\ge2$, proving strong connectivity.

For mixing, use the two loops based at $3$, $$3\to2\to3,
 \qquad
 3\to4\to5\to3,$$ of lengths two and three. Fix paths $u\to3$ and $3\to v$, with total length $b$. Every integer at least two is $2a+3c$ for some $a,c\ge0$. For every sufficiently large $n$, insert the required numbers of the two based loops to obtain length $n-b$, then follow the fixed exit path.

[\[thm:canonical\]]{#thm:canonical label="thm:canonical"} For every $k\ge2$, $$C_k=(k,k+1,\ldots,2k-1)$$ is a simple primitive directed cycle of length $k$. Its vertex mass and weight are $$M_k=\prod_{j=k}^{2k-1}j=\frac{(2k-1)!}{(k-1)!},
 \qquad
 w_s(C_k)=M_k^{-2s}.$$

Successor edges traverse $k,k+1,\ldots,2k-1$. The last vertex returns to $k$ because $$k\mid2k=(2k-1)+1.$$ All displayed vertices are distinct, so the closed word is simple. A simple closed word of length at least two cannot be a positive temporal power of a shorter word. The mass and weight follow from [\[eq:cyclic-weight\]](#eq:cyclic-weight){reference-type="ref" reference="eq:cyclic-weight"}.

[\[prop:subflood\]]{#prop:subflood label="prop:subflood"} Let $d\mid r$ with $d\ge2$. Then $$C_{r,d}=(d,d+1,\ldots,d+r-1)$$ is a simple primitive cycle of length $r$. If $P_r$ counts primitive rotation classes of length $r$, then $$P_r\ge \tau(r)-1,$$ where $\tau(r)$ is the number of positive divisors of $r$.

Successor edges traverse the interval, and the final edge closes because $$d\mid d+r=(d+r-1)+1.$$ The cycle is simple. Distinct divisors $d$ give distinct minimum vertices, so their rotation classes differ. There are $\tau(r)-1$ divisors $d\ge2$.

makes the structural tension visible. The successor transition is the only unbounded ascent mechanism needed for connectivity. The quotient-two return is the only descent mechanism needed for the entire canonical flood. The remaining divisor edges enrich the periodic inventory but do not create the decisive obstruction.

# Exact finite confinement {#sec:confinement}

Countable graphs normally make a fixed trace look like an infinite enumeration problem. Here a maximum principle makes it finite.

[\[lem:drop\]]{#lem:drop label="lem:drop"} Let $M$ be a maximal vertex on a directed closed walk, and let $M\to d$ be the next edge. Then $$d\le\frac{M+1}{2}.$$

The edge condition gives $d\mid M+1$. The choice $d=M+1$ contradicts maximality, so $d$ is a proper divisor of $M+1$. Every proper positive divisor of an integer $N$ is at most $N/2$.

[\[thm:confinement\]]{#thm:confinement label="thm:confinement"} Every length-$r$ directed closed walk is contained in $$\{2,3,\ldots,2r-1\}.$$ If the walk reaches $2r-1$, then it is $C_r$, up to cyclic rotation.

There is no length-one closed walk because $n\nmid n+1$. Let $r\ge2$, rotate a closed walk to start at a maximum $M$, and write its next vertex as $d$. By [\[lem:drop\]](#lem:drop){reference-type="ref" reference="lem:drop"}, $$d\le\frac{M+1}{2}.$$ Every edge $x\to y$ satisfies $y\le x+1$. After the first drop there are $r-1$ edges left before returning to $M$, so $$M\le d+r-1
 \le\frac{M+1}{2}+r-1.$$ Rearranging gives $M\le2r-1$.

If $M=2r-1$, equality must hold throughout. Thus $$d=\frac{M+1}{2}=r,$$ and every remaining edge increases by exactly one. The rotated walk is $$2r-1\to r\to r+1\to\cdots\to2r-1,$$ which is $C_r$.

[\[cor:cutoff\]]{#cor:cutoff label="cor:cutoff"} For fixed $r$, the order-$r$ closed-walk sum of the infinite graph equals the corresponding sum in every induced prefix with cutoff $N\ge2r-1$. The only primitive rotation class meeting the top vertex at the sharp cutoff is $C_r$.

confines every relevant walk to the prefix. Its equality statement identifies the only class containing $2r-1$.

## Primitive and repetition recurrence

Let $T_r$ denote the number of rooted length-$r$ closed walks, and let $P_r$ denote the number of primitive length-$r$ rotation classes. Every rooted closed word is a power of a unique primitive class. A primitive class of length $d\mid r$ contributes $d$, not $r$, distinct rooted representatives after repetition. Therefore $$\label{eq:necklace}
 T_r=\sum_{d\mid r}dP_d,
 \qquad
 P_r=\frac1r\sum_{d\mid r}\mu(r/d)T_d.$$ The second identity is Möbius inversion. It is the exact convention used by all finite certificates.

The table is a compact regression ledger. Its qualitative message is already theorem-level: $P_r\ge1$ for every $r\ge2$, and the count grows far beyond the single canonical family. The proof of confinement, rather than stabilization observed at two numerical cutoffs, certifies exactness.

## Sparse finite protocol

For an order $r$, exact enumeration needs only the sparse induced adjacency on $2,\ldots,2r-1$. Dynamic propagation or sparse matrix powering computes its diagonal sum. Cartesian enumeration of all words is unnecessary and, for moderate $r$, prohibitive. The extremal contribution supplies an additional audit: exactly $r$ rooted walks at order $r$ use the top vertex, namely the rotations of $C_r$.

## Frozen exact certificate

The exact regression suite certifies all unweighted orders through $32$, ending with $$T_{32}=14{,}532{,}674,
 \qquad
 P_{32}=454{,}021.$$ Explicit rotation reduction finds $667$ primitive classes through length $16$. At $s=1,2,3$, the suite records $48$ exact weighted traces and $51$ determinant coefficients through degree $16$; Newton recurrence and independent multiplication of the primitive factors have zero coefficient mismatch. A source audit checks $30{,}626$ edges with zero quotient mismatch and zero loops. All $19$ declared tests pass, and two full regenerations produce a byte-identical frozen ledger. These computations regress the preceding theorems; they are not premises of confinement or of the trace-class threshold.

# The sharp trace-class half-plane {#sec:traceclass}

The endpoint weights are much more summable than a direct entry count suggests. The right decomposition is by target rows, not by individual edges.

[\[thm:traceclass\]]{#thm:traceclass label="thm:traceclass"} The matrix in [\[def:operator\]](#def:operator){reference-type="ref" reference="def:operator"} extends to a trace-class operator on $\ell^2(V)$ exactly on the half-plane $$L_s\in\mathcal S_1
 \quad\Longleftrightarrow\quad
 \operatorname{Re}s>\frac12.$$

Write $\sigma=\operatorname{Re}s$.

*Sufficiency.* Fix a target row $d\ge2$. Its source columns are precisely $$n=kd-1\ge2,\qquad k\ge1.$$ Let $R_{d,s}$ be the operator consisting of that row. It maps into $\mathbb Ce_d$ and is therefore rank one, with $$\begin{aligned}
\|R_{d,s}\|_1
&=
\left(
 \sum_{\substack{k\ge1\\kd-1\ge2}}
 [d(kd-1)]^{-2\sigma}
\right)^{1/2}.                                      \label{eq:row-exact}\end{aligned}$$ Since $kd-1\ge kd/2$, $$\label{eq:row-bound}
\|R_{d,s}\|_1
\le
2^\sigma\zeta(2\sigma)^{1/2}d^{-2\sigma}.$$ For $\sigma>1/2$, both the inner $k$-series and outer $d$-series are finite, and $$\sum_{d\ge2}\|R_{d,s}\|_1<\infty.$$ Hence $$L_s=\sum_{d\ge2}R_{d,s}$$ converges in trace norm.

*Necessity.* Let $$U_te_n=\mathrm e^{int}e_n,\qquad 0\le t\le2\pi.$$ If $L_s$ were trace class, its first Fourier diagonal $$\label{eq:fourier-extraction}
 \mathcal E_1(L_s)
 =
 \frac1{2\pi}\int_0^{2\pi}
 \mathrm e^{-it}U_tL_sU_t^*\,\,\mathrm dt$$ would be a trace-class Bochner integral. A matrix entry in row $d$, column $n$, acquires the phase $\mathrm e^{i(d-n)t}$, so [\[eq:fourier-extraction\]](#eq:fourier-extraction){reference-type="ref" reference="eq:fourier-extraction"} selects $d-n=1$. Those entries are exactly the successor edges: $$\mathcal E_1(L_s)e_n=[n(n+1)]^{-s}e_{n+1}.$$ This unilateral weighted shift has singular values $[n(n+1)]^{-\sigma}$, $n\ge2$. It is trace class if and only if $$\sum_{n\ge2}[n(n+1)]^{-\sigma}<\infty,$$ which is equivalent to $2\sigma>1$. Thus no trace-class extension of the frozen matrix exists when $\sigma\le1/2$.

Summing $|(L_s)_{d,n}|$ over all edges treats each row as an $\ell^1$ object and discards its rank-one geometry. The exact row norm in [\[eq:row-exact\]](#eq:row-exact){reference-type="ref" reference="eq:row-exact"} takes an inner $\ell^2$ sum before the outer nuclear sum, producing $d^{-2\sigma}$ and the sharp boundary. A cruder sufficient domain must not be reported as the operator threshold.

[\[prop:holomorphy\]]{#prop:holomorphy label="prop:holomorphy"} The map $$s\longmapsto L_s$$ is holomorphic from $\{\operatorname{Re}s>1/2\}$ into $\mathcal S_1$.

Let $K$ be compact in the half-plane and choose $\sigma_0>1/2$ with $\operatorname{Re}s\ge\sigma_0$ on $K$. Differentiating an entry $m$ times introduces $\log^m(nd)$. Choose $0<\varepsilon<\sigma_0-1/2$. For $x\ge2$, $$\log^m x\le C_{m,\varepsilon}x^\varepsilon.$$ The derivative row series is therefore dominated by the same estimate as [\[eq:row-bound\]](#eq:row-bound){reference-type="ref" reference="eq:row-bound"}, with real part $\sigma_0-\varepsilon>1/2$. The row series and its derivative series converge locally uniformly in trace norm.

[\[cor:successor-necessity\]]{#cor:successor-necessity label="cor:successor-necessity"} Any subgraph that retains every successor edge has no larger trace-class domain than $\operatorname{Re}s>1/2$ for the inherited endpoint weights.

The Fourier extraction in [\[eq:fourier-extraction\]](#eq:fourier-extraction){reference-type="ref" reference="eq:fourier-extraction"} depends only on the first superdiagonal, so the same necessary condition applies.

## Interpretation of the boundary

is an own-object analytic result. It says neither that $D_{\mathrm{SD}}$ continues to $\operatorname{Re}s=1/2$ nor that this boundary is a natural boundary. It also gives no symmetry $s\mapsto1-s$. The theorem does show that the wrong candidate determinant is analytically well defined through much of the classical critical strip. Analytic availability alone is therefore not evidence of the correct prime-orbit ledger.

# Fredholm determinant and the primitive ledger {#sec:fredholm}

Trace class supplies a whole determinant; finite confinement supplies an exact path interpretation of every trace coefficient.

[\[thm:fredholm\]]{#thm:fredholm label="thm:fredholm"} For $\sigma=\operatorname{Re}s>1/2$, $$D_{\mathrm{SD}}(s,z)=\det(I-zL_s)$$ is holomorphic in $s$ and entire in $z$. For $z$ sufficiently close to zero, $$\label{eq:logdet}
 -\log D_{\mathrm{SD}}(s,z)
 =
 \sum_{r\ge1}\frac{z^r}{r}\operatorname{Tr}L_s^r,$$ and $$\label{eq:primitive-product}
 D_{\mathrm{SD}}(s,z)
 =
 \prod_{[\gamma]\ {\rm primitive}}
 \left(
 1-z^{\ell(\gamma)}N(\gamma)^{-2s}
 \right).$$ More precisely, [\[eq:primitive-product\]](#eq:primitive-product){reference-type="ref" reference="eq:primitive-product"} is absolutely convergent for $$|z|<\|L_{\sigma}\|^{-1}.$$ No primitive-product convergence at $z=1$ is asserted.

and trace-class Fredholm theory give the first statement and [\[eq:logdet\]](#eq:logdet){reference-type="ref" reference="eq:logdet"}; see, for example, @Simon1977. The logarithmic series converges whenever $|z|\|L_s\|<1$.

By [\[cor:cutoff\]](#cor:cutoff){reference-type="ref" reference="cor:cutoff"}, each trace is the finite closed-walk sum $$\operatorname{Tr}L_s^r
 =
 \sum_{n_0\to\cdots\to n_{r-1}\to n_0}
 \prod_{j=0}^{r-1}(n_jn_{j+1})^{-s}.$$ Taking absolute values gives the corresponding trace for the positive operator $L_\sigma$. The estimate $$\operatorname{Tr}L_\sigma^r
 \le\|L_\sigma\|_1\|L_\sigma\|^{r-1}$$ shows absolute summability when $|z|\|L_\sigma\|<1$. Group each closed word by its unique primitive root and use $$-\log(1-x)=\sum_{m\ge1}\frac{x^m}{m}.$$ The cyclic weight is $N(\gamma)^{-2s}$ by [\[eq:cyclic-weight\]](#eq:cyclic-weight){reference-type="ref" reference="eq:cyclic-weight"}, giving [\[eq:primitive-product\]](#eq:primitive-product){reference-type="ref" reference="eq:primitive-product"}.

[\[cor:conjugation\]]{#cor:conjugation label="cor:conjugation"} $$D_{\mathrm{SD}}(\overline s,\overline z)
 =
 \overline{D_{\mathrm{SD}}(s,z)}.$$

The matrix satisfies $L_{\overline s}=\overline{L_s}$ entrywise, and the Fredholm determinant respects conjugation.

is a reality symmetry of one holomorphic operator family. It is not a functional equation and gives no reflection across $\operatorname{Re}s=1/2$.

## First weighted traces

[\[prop:first-traces\]]{#prop:first-traces label="prop:first-traces"} The first four traces are $$\begin{aligned}
\operatorname{Tr}L_s&=0,                                                   \label{eq:t1}\\
\operatorname{Tr}L_s^2&=2\,6^{-2s},                                       \label{eq:t2}\\
\operatorname{Tr}L_s^3&=3\,60^{-2s},                                      \label{eq:t3}\\
\operatorname{Tr}L_s^4&=2\,6^{-4s}+4\,120^{-2s}+4\,840^{-2s}.              \label{eq:t4}\end{aligned}$$

There is no loop. The only primitive length-two class is $(2,3)$, with vertex product $6$. The only primitive length-three class is $(3,4,5)$, with product $60$. At length four there is the double traversal of $(2,3)$ and the two primitive classes $$(2,3,4,5),
 \qquad
 (4,5,6,7),$$ with products $120$ and $840$. Each primitive length-$r$ class has $r$ rooted rotations. A finite-prefix classification justified by [\[thm:confinement\]](#thm:confinement){reference-type="ref" reference="thm:confinement"} is expanded in [12](#app:proofs){reference-type="ref" reference="app:proofs"}.

At $s=1$, [\[eq:t1,eq:t2,eq:t3,eq:t4\]](#eq:t1,eq:t2,eq:t3,eq:t4){reference-type="ref" reference="eq:t1,eq:t2,eq:t3,eq:t4"} become $$0,\qquad\frac1{18},\qquad\frac1{1200},\qquad\frac{29}{15876}.$$ The first primitive factors are $$(1-z^2\,6^{-2s})
 (1-z^3\,60^{-2s})
 (1-z^4\,120^{-2s})
 (1-z^4\,840^{-2s})\cdots.$$

## Determinant coefficients

Write $$D_{\mathrm{SD}}(s,z)=\sum_{m\ge0}a_m(s)z^m,\qquad a_0=1.$$ Differentiating [\[eq:logdet\]](#eq:logdet){reference-type="ref" reference="eq:logdet"} gives the Newton recurrence $$\label{eq:newton}
 ma_m(s)=-\sum_{r=1}^m\operatorname{Tr}(L_s^r)a_{m-r}(s).$$ The first coefficients are $$\begin{aligned}
a_1(s)&=0,\\
a_2(s)&=-6^{-2s},\\
a_3(s)&=-60^{-2s},\\
a_4(s)&=-120^{-2s}-840^{-2s}.\end{aligned}$$ The temporal double of $C_2$ appears in the logarithm but cancels from $a_4$, as multiplication of primitive factors requires. At $s=1$, $$a_0,a_1,a_2,a_3,a_4
 =
 1,0,-\frac1{36},-\frac1{3600},-\frac1{14112}.$$ This is a small but useful audit that primitive factors and repetitions have not been conflated.

# Exact obstruction to the marked prime Euler target {#sec:target}

The determinant theorem in [\[thm:fredholm\]](#thm:fredholm){reference-type="ref" reference="thm:fredholm"} belongs to the frozen symbolic object. We now compare its marked primitive ledger with the target $$D_{\mathbb P}(s,z)=\prod_p(1-zp^{-s}),
 \qquad
 \operatorname{Re}s>1.$$ The marker $z$ records primitive degree. It prevents accidental scalar agreement at $z=1$ from being mistaken for equality of orbit species.

[\[thm:target-mismatch\]]{#thm:target-mismatch label="thm:target-mismatch"} On the common domain $\operatorname{Re}s>1$, the germs at $z=0$ of $D_{\mathrm{SD}}(s,z)$ and $D_{\mathbb P}(s,z)$ are not equal.

An integer $n\ge2$ never divides $n+1$, so the source graph has no loop. Consequently $$[z]D_{\mathrm{SD}}(s,z)=-\operatorname{Tr}L_s=0.$$ For the target, absolute convergence gives $$D_{\mathbb P}(s,z)
 =
 1-z\sum_pp^{-s}+O(z^2).$$ For real $s>1$, $$\sum_pp^{-s}>0,$$ so the target coefficient is strictly negative. The germs differ before any zero is considered.

[\[rem:z1\]]{#rem:z1 label="rem:z1"} does not claim that an isolated scalar equality $$D_{\mathrm{SD}}(s,1)=D_{\mathbb P}(s,1)$$ is impossible at every individual $s$. Such an accident would not restore the marked trace sequence or primitive factors and therefore would not constitute a target representation.

[\[thm:orbit-species\]]{#thm:orbit-species label="thm:orbit-species"} Every closed orbit $\gamma$ has length at least two. Its vertex mass $$N(\gamma)=\prod_{v\in\gamma}v$$ is composite, and its roof norm is $$\exp(T_\gamma)=N(\gamma)^2,$$ a composite perfect square.

Absence of loops gives length at least two. Every vertex is at least two, so $N(\gamma)$ is a product of at least two integers greater than one. By [\[eq:cyclic-weight\]](#eq:cyclic-weight){reference-type="ref" reference="eq:cyclic-weight"}, the orbit roof is $$T_\gamma=2\log N(\gamma).$$

Even an unauthorized halving of the frozen endpoint roof would leave $N(\gamma)$ composite. The problem is therefore not merely the factor two: the orbit inventory itself has the wrong arithmetic species.

## Why own-object analyticity does not repair the ledger

The trace-class theorem extends $D_{\mathrm{SD}}$ as a holomorphic same-object determinant throughout $\operatorname{Re}s>1/2$, including much of the classical critical strip. It does not transport the prime Euler product into that half-plane. The two marked germs already disagree where both defining products are absolutely meaningful. Any later continuation of one object, were it to exist, would continue the mismatch rather than erase it.

This distinction is the central diagnostic outcome: $$\text{strong recurrence and Fredholm control}
\quad\not\Longrightarrow\quad
\text{prime-orbit selectivity}.$$

# Pruning and quotient controls {#sec:controls}

Every edge carries the unique quotient label $$q(n,d)=\frac{n+1}{d}.$$ The full graph retains all $q\ge1$. To test whether the full divisor inventory creates the observed signal, we retain only $q=1,2$.

Let $G_{\{1,2\}}$ have the same vertex set as $G_{\mathrm{SD}}$ and retain exactly the edges with $q(n,d)\in\{1,2\}$. Thus $$q=1:\ n\to n+1,
 \qquad
 q=2:\ 2d-1\to d.$$ Let $L_s^{\{1,2\}}$ be its inherited endpoint-weighted adjacency.

[\[thm:spine\]]{#thm:spine label="thm:spine"} The graph $G_{\{1,2\}}$ is strongly connected and path-sense mixing, has no loops, and contains $C_k$ for every $k\ge2$. Moreover, $$L_s^{\{1,2\}}\in\mathcal S_1
 \quad\Longleftrightarrow\quad
 \operatorname{Re}s>\frac12.$$

All successor edges remain. If $n=2k-1$ is odd, the quotient-two edge $$n\to k$$ strictly decreases $n$ unless $n=3$, in which case it reaches $2$. If $n>2$ is even, then $$n\to n+1\to\frac{n+2}{2}<n.$$ Iterating reaches $2$, while successor edges connect $2$ to every vertex. Thus the spine is strongly connected. It retains the length-two and length-three loops based at $3$, so the proof of [\[thm:mixing\]](#thm:mixing){reference-type="ref" reference="thm:mixing"} gives mixing.

Every canonical cycle uses successor edges followed by $$2k-1\to k,$$ whose quotient is two. Hence every $C_k$ remains. No loop can appear because the spine is a subgraph of the loopless full graph.

For a target row $d$, there are at most two source columns, $d-1$ and $2d-1$. Its rank-one row norm is $O(d^{-2\sigma})$, so summing rows proves trace class for $\sigma>1/2$. Necessity follows from the retained successor diagonal exactly as in [\[thm:traceclass\]](#thm:traceclass){reference-type="ref" reference="thm:traceclass"}.

The full graph and the spine therefore have zero control margin for the properties causing rejection: recurrence, aperiodicity, no degree-one trace, the all-length cycle flood, and the sharp trace-class boundary. The extra divisors are not responsible for the decisive signal.

[\[prop:successor-only\]]{#prop:successor-only label="prop:successor-only"} The quotient-one graph contains only $n\to n+1$. It is acyclic and has no periodic orbit. Its inherited weighted adjacency is trace class exactly for $\operatorname{Re}s>1/2$, and its Fredholm determinant is identically one there.

The vertex label strictly increases at every step. The adjacency is the weighted shift $$S_se_n=[n(n+1)]^{-s}e_{n+1},$$ whose singular values are $[n(n+1)]^{-\operatorname{Re}s}$. This gives the stated trace-class range. All power traces vanish because the graph is acyclic, so the local logarithmic determinant is zero. Since the Fredholm determinant is entire in $z$, it equals one identically.

[\[prop:qfamily\]]{#prop:qfamily label="prop:qfamily"} Fix $q\ge2$. Any quotient inventory containing $1$ and $q$ contains, for every $d\ge2$, the simple primitive cycle $$C_{d,q}=(d,d+1,\ldots,qd-1)$$ of length $d(q-1)$.

Quotient one supplies all successor edges along the interval. The final edge has quotient $$\frac{(qd-1)+1}{d}=q.$$ The vertices are distinct, giving a simple primitive cycle.

\@L0.24YYYY@ Inventory & Recurrent & Primitive lengths & Loops & Sharp $\mathcal S_1$ range\
All quotients & yes, mixing & every $k\ge2$ & none & $\operatorname{Re}s>1/2$\
$q\in\{1,2\}$ & yes, mixing & every $k\ge2$ & none & $\operatorname{Re}s>1/2$\
$q=1$ & no & none & none & $\operatorname{Re}s>1/2$\
$q\in\{1,q_0\}$, $q_0\ge2$ & not needed here & every $d(q_0-1)$ & none & not claimed\

The frozen control census contains $225$ quotient-family rows, $20$ graph-control rows, $64$ positive-weight rows, and $56$ trace-class diagnostic rows. The counts organize coverage; the zero-margin statement itself is the theorem-level consequence of [\[thm:spine\]](#thm:spine){reference-type="ref" reference="thm:spine"}.

## Weight-inventory controls

Replacing the entropy inventory by positive vertex functions such as $n+1$, $n^2+1$, or $2^n$ changes weights but not the directed graph. Such substitutions can diagnose convergence sensitivity; they cannot remove or create primitive cycles while weights remain nonzero. We therefore label them *weight controls*, not arithmetic-graph selectivity controls. The quotient spine is the decisive graph control.

# Strict route evaluation and next obligation {#sec:route}

The correct evaluation separates the strength of the candidate's own determinant from its failure as a prime-orbit representation.

\@L0.12L0.34Y@ Stage & Verdict & Exact reason\
A0 & `STRUCTURAL_ARITHMETIC_RELATION` & The edge is derived from full-shift successor and tensor factorization, with no target predicate.\
A1 & `WEAK` & The source is natural and recurrent, but the quotient grammar has zero selectivity margin and the orbit inventory is composite.\
A2 & `ANALYTIC_DETERMINANT` & The whole adjacency is trace class exactly for $\operatorname{Re}s>1/2$, giving a same-object Fredholm determinant.\
A3 & `FAIL` & No target completion, functional equation, Gamma factor, global divisor law, or Weil compression is derived.\
A4 & `FAIL` & The marked degree-one coefficient and orbit norms reject the target; no RH or Hilbert--Pólya conclusion follows.\

Thus the strict tuple is $$\boxed{
\begin{gathered}
(\mathrm{A0\_STRUCTURAL\_ARITHMETIC\_RELATION},
 \mathrm{A1\_WEAK},\\
 \mathrm{A2\_ANALYTIC\_DETERMINANT},
 \mathrm{A3\_FAIL},
 \mathrm{A4\_FAIL})
\end{gathered}}$$ and the overall verdict is $$\boxed{\mathrm{ROUTE\_A\_REJECTED}}.$$ A2 is intentionally positive: it certifies the analytic determinant of the same symbolic object. That credit may not be inflated into A3 merely because the half-plane reaches $\operatorname{Re}s>1/2$.

## Triggered stop labels

All of the following stop conditions fire: $$\begin{gathered}
\texttt{STOP\_PRIME\_ORBIT\_LEDGER},\qquad
\texttt{CYCLE\_FLOOD},\\
\texttt{PRUNING\_PERSISTS},\qquad
\texttt{PROVES\_TOO\_MUCH},\\
\texttt{STOP\_SCOPED},\qquad
\texttt{ROUTE\_B\_LOCKED}.
\end{gathered}$$ The labels do not invalidate the positive graph and operator theorems. They prevent a wrong primitive species from being promoted because its determinant is analytically attractive.

## Minimal Paper22 obligation

The unique quotient $q=(n+1)/d$ should be exposed on edge symbols. The next symbolic task is to classify relabel-natural finite-state quotient filters or finite-dimensional same-object cocycles. already blocks memoryless positive filtering: retaining $q=1$ and any $q\ge2$ creates infinitely many simple primitive cycles.

Any cancellation proposal must therefore satisfy three locks:

1.  prove cancellation coefficientwise at the trace level;

2.  report the whole determinant and every relevant isotypic block;

3.  show that unwanted cycles are canceled, not merely moved into an unreported block.

This obligation remains inside Symbolic Dynamics. Geometric, scattering, or self-adjoint carriers are recorded only as out-of-scope round-two clues and do not affect the present verdict. No Paper22 construction is attempted here.

# Conclusion {#sec:conclusion}

The successor--divisor shift resolves one difficulty and exposes another. The local relation $$F_{n+1}\cong F_d\boxtimes F_q$$ creates genuine recurrence without an external verification clock. Its countable graph is mixing, its fixed-order traces are finitely confined, and its natural weighted adjacency has the sharp theorem $$L_s\in\mathcal S_1\iff\operatorname{Re}s>\frac12.$$ These are substantive positive results for one symbolic object.

The same construction fails exactly where prime-orbit selectivity begins. It has no degree-one orbit, has simple primitive cycles at every length $k\ge2$, and assigns every orbit a composite-square norm. The $q\in\{1,2\}$ spine preserves all decisive features, so the full divisor inventory contributes zero selectivity margin. The strongest honest summary is therefore: $$\text{source-intrinsic recurrence}
\;+\;
\text{sharp Fredholm control}
\;-\;
\text{correct primitive species}.$$

The determinant is worth keeping as a mathematically clean negative control, not as a Riemann representation. The Session can advance only by adding a quotient-resolved symbolic mechanism with a coefficientwise theorem. Until such a mechanism survives the marked ledger and whole-block audit, Route A remains rejected and Route B remains locked.

# Expanded proofs and exact certificate conventions {#app:proofs}

## Path-length mixing at a fixed base vertex

The two cycles used in [\[thm:mixing\]](#thm:mixing){reference-type="ref" reference="thm:mixing"} are genuinely based at the same vertex: $$3\to2\to3$$ has length two, while $$3\to4\to5\to3$$ has length three because $3\mid6$. If fixed paths from $u$ to $3$ and from $3$ to $v$ have lengths $a$ and $b$, then every path length of the form $$a+2x+3y+b,\qquad x,y\ge0,$$ is realized. Since the numerical semigroup generated by $2,3$ contains every integer except $1$, every length at least $a+b+2$ is realized. This is the stated path-sense mixing, with no compactness assumption on the countable alphabet.

## Finite trace formula

For a fixed $r$, each source has finite outdegree, so every diagonal matrix element $$\langle e_n,L_s^re_n\rangle$$ is a finite sum over rooted closed walks based at $n$. By [\[thm:confinement\]](#thm:confinement){reference-type="ref" reference="thm:confinement"}, it vanishes for $n>2r-1$. Therefore $$\label{eq:finite-trace-app}
 \sum_{n\ge2}\langle e_n,L_s^re_n\rangle
 =
 \sum_{n=2}^{2r-1}\langle e_n,L_s^re_n\rangle$$ is a finite exponential polynomial in $s$ for every $s\in\mathbb C$. When $\operatorname{Re}s>1/2$, $L_s^r$ is trace class and its trace equals the basis-diagonal sum, so [\[eq:finite-trace-app\]](#eq:finite-trace-app){reference-type="ref" reference="eq:finite-trace-app"} is the operator trace.

This separates two assertions:

-   the fixed-order closed-walk expression is a finite entire function of $s$;

-   the Fredholm determinant formed from the whole operator is proved only where $L_s\in\mathcal S_1$.

Finite coefficients alone do not continue the whole determinant through the trace-class boundary.

## Primitive recurrence checks

The unweighted recurrence $$T_r=\sum_{d\mid r}dP_d$$ keeps primitive rotations and temporal powers separate. For example, $$T_4=10=2P_2+4P_4=2+8,$$ so $P_4=2$. Likewise, $$T_6=29=2P_2+3P_3+6P_6=2+3+24,$$ so $P_6=4$. Counting a repeated length-two orbit as four unrelated rooted objects would violate both identities.

In the weighted setting, a primitive class $\gamma$ of length $d\mid r$ contributes $$d\,N(\gamma)^{-2sr/d}$$ to $\operatorname{Tr}L_s^r$: it has $d$ rooted representatives and is traversed $r/d$ times. Hence $$\label{eq:weighted-necklace}
 \operatorname{Tr}L_s^r
 =
 \sum_{d\mid r}d
 \sum_{\substack{[\gamma]\ {\rm primitive}\\\ell(\gamma)=d}}
 N(\gamma)^{-2sr/d}.$$ Substitution of [\[eq:weighted-necklace\]](#eq:weighted-necklace){reference-type="ref" reference="eq:weighted-necklace"} into [\[eq:logdet\]](#eq:logdet){reference-type="ref" reference="eq:logdet"} yields the primitive product in [\[thm:fredholm\]](#thm:fredholm){reference-type="ref" reference="thm:fredholm"}.

## Low-order classification without brute force

::: {#tab:low-classes}
   Length      Class     Closing divisibility     $N(\gamma)$   Rotations
  -------- ------------- ---------------------- ------------- -----------
     1         none      $n\nmid n+1$                     ---           0
     2        $(2,3)$    $2\mid4$                           6           2
     3       $(3,4,5)$   $3\mid6$                          60           3
     4      $(2,3,4,5)$  $2\mid6$                         120           4
     4      $(4,5,6,7)$  $4\mid8$                         840           4

  : Primitive classes through length four. The last column is the number of rooted trace terms contributed at the primitive length.
:::

For length $r\le4$, [\[thm:confinement\]](#thm:confinement){reference-type="ref" reference="thm:confinement"} restricts the maximum to $2r-1$. Choose a maximum $M$ and its proper-divisor successor $d$. The remaining edges can increase by at most one. At $r=2$, the inequality forces $M=3,d=2$. At $r=3$, the primitive case forces $M=5,d=3$; the only other closed words would be powers of a length-one loop, which does not exist. At $r=4$, the primitive maxima are $5$ and $7$, yielding the two rows in [1](#tab:low-classes){reference-type="ref" reference="tab:low-classes"}; the remaining rooted terms are the two rotations of the double traversal of $(2,3)$. This produces $$T_1,T_2,T_3,T_4=0,2,3,10$$ and [\[prop:first-traces\]](#prop:first-traces){reference-type="ref" reference="prop:first-traces"}.

## Trace-norm holomorphy in detail

For $m\ge0$, the $m$-th $s$-derivative of a row coefficient is $$(-\log[d(kd-1)])^m[d(kd-1)]^{-s}.$$ Fix $\sigma_0>1/2$ and choose $\varepsilon\in(0,\sigma_0-1/2)$. The bound $$\log^m x\le C_{m,\varepsilon}x^\varepsilon,\qquad x\ge2,$$ shows that the derivative row norm is bounded, up to a constant depending on $m,\varepsilon,\sigma_0$, by $$d^{-2(\sigma_0-\varepsilon)}.$$ The outer sum converges. Uniform trace-norm convergence on compact subsets justifies termwise differentiation of the row series and proves [\[prop:holomorphy\]](#prop:holomorphy){reference-type="ref" reference="prop:holomorphy"}. Standard local Lipschitz bounds for the Fredholm determinant then give holomorphy of $D_{\mathrm{SD}}$ in $s$.

## Exact sparse certificate protocol

For each desired order $r$:

1.  construct only the induced sparse graph on $2,\ldots,2r-1$;

2.  propagate integer path counts for $r$ steps and sum the diagonal;

3.  recompute at larger cutoffs as a regression, while labeling $2r-1$ as the theorem-certified cutoff;

4.  recover $P_r$ by Möbius inversion and check the forward recurrence;

5.  require exactly $r$ rooted walks using the top vertex;

6.  for integer $s$, repeat with rational endpoint weights and compare determinant coefficients from [\[eq:newton\]](#eq:newton){reference-type="ref" reference="eq:newton"} with multiplication of primitive factors.

Sparse dynamic propagation is polynomial in the finite edge inventory for a fixed order. Cartesian enumeration of all $N^r$ vertex words is neither needed nor authorized by the certificate design.

## Endpoint and near-boundary diagnostics

Finite nuclear prefixes at $\sigma=0.51$ converge very slowly because the outer comparison series is close to $\sum d^{-1.02}$. Their initial growth cannot falsify [\[thm:traceclass\]](#thm:traceclass){reference-type="ref" reference="thm:traceclass"}. Conversely, apparent numerical stability at $\sigma=0.50$ cannot prove convergence. The row decomposition and Fourier extraction, not a finite plot, decide the exact threshold.

# Claim, scope, and route ledger {#app:ledger}

## Claim-status matrix

\@L0.31L0.15Y@ Claim & Status & Authority\
Full-shift successor/factor edge grammar & proved & Cardinality identities in [3](#sec:source){reference-type="ref" reference="sec:source"}\
Strong connectivity and mixing & proved & Constructive paths and based $2,3$ cycles\
Canonical primitive $C_k$ for all $k\ge2$ & proved &\
Divisor-indexed subflood & proved &\
$2r-1$ confinement and extremal uniqueness & proved &\
Exact finite trace cutoff & proved &\
Primitive/repetition recurrence & proved &\
$L_s\in\mathcal S_1\iff\operatorname{Re}s>1/2$ & proved & Row decomposition plus Fourier diagonal\
Trace-norm holomorphy and Fredholm determinant & proved &\
Marked target mismatch & proved &\
Composite-square orbit norms & proved &\
Spine persistence and zero control margin & proved &\
No exact literature collision found & search-bounded & Protocol in [2](#sec:literature){reference-type="ref" reference="sec:literature"}\

## Explicit nonclaims

Nothing in this paper proves or assumes:

-   $D_{\mathrm{SD}}(s,1)=1/\zeta(s)$;

-   convergence of the primitive product at $z=1$;

-   analytic continuation of $D_{\mathrm{SD}}$ to or across $\operatorname{Re}s=1/2$;

-   a functional equation or Gamma factor;

-   a completed Riemann divisor or Riemann--von Mangoldt law;

-   a Weil Hermitian compression;

-   RH or a Hilbert--Pólya operator;

-   absolute priority over all arithmetic graph constructions.

The conjugation identity in [\[cor:conjugation\]](#cor:conjugation){reference-type="ref" reference="cor:conjugation"} is not a functional equation. The exact fixed-order trace expressions in [\[eq:finite-trace-app\]](#eq:finite-trace-app){reference-type="ref" reference="eq:finite-trace-app"} are not a continuation of the infinite Fredholm determinant. The half-plane in [\[thm:traceclass\]](#thm:traceclass){reference-type="ref" reference="thm:traceclass"} is not credited as A3.

## Whole-object and comparison locks

The only operator determinant is the whole Fredholm determinant $$D_{\mathrm{SD}}(s,z)=\det(I-zL_s).$$ There is no regular-representation determinant, character factor, or unreported isotypic block. The target comparison is performed after the source graph, roof, and operator are frozen. It uses marked Taylor coefficients and no target zeros.

## Control interpretation

The quotient spine is a graph-selectivity control. Positive changes of the roof inventory are weight controls only. The observed zero margin means that all quotient edges beyond $q=2$ can be deleted without changing the properties that reject the target. It does not mean that the full graph and spine have identical trace coefficients at every order.

## Frozen final decision

$$\begin{aligned}
(&\mathrm{A0\_STRUCTURAL\_ARITHMETIC\_RELATION},\\
 &\mathrm{A1\_WEAK},\\
 &\mathrm{A2\_ANALYTIC\_DETERMINANT},\\
 &\mathrm{A3\_FAIL},\\
 &\mathrm{A4\_FAIL}).
\end{aligned}$$ $$\mathrm{ROUTE\_A\_REJECTED}.$$ The stop state is scoped to SD-C23. Route B is locked. The only authorized successor task is the quotient-resolved symbolic classification stated in [10](#sec:route){reference-type="ref" reference="sec:route"}; this paper does not begin that task.

## Round-two clue firewall

A geometric or scattering carrier might someday turn quotient-resolved symbolic holonomy into a unitary object. That thought crosses to another system family and is recorded only as a round-two clue. No carrier, Hamiltonian, boundary condition, or self-adjoint operator enters the definitions, proofs, or Route-A score of SD-C23.
