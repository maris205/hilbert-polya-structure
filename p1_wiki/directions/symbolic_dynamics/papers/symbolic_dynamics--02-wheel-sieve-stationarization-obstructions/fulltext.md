---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--02-wheel-sieve-stationarization-obstructions"
canonical_tex: "symbolic_dynamics/papers/02-wheel-sieve-stationarization-obstructions/main.tex"
canonical_pdf: "symbolic_dynamics/papers/02-wheel-sieve-stationarization-obstructions/main.pdf"
source_sha256: "372612b442fe314e2e6cbd693d9bd3c481813322d8841e67991710e0977a4cc4"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Scoped Obstructions to Stationarizing a Graded Wheel-Sieve Symbolic System

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/02-wheel-sieve-stationarization-obstructions>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/02-wheel-sieve-stationarization-obstructions/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/02-wheel-sieve-stationarization-obstructions/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/02-wheel-sieve-stationarization-obstructions/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/02-wheel-sieve-stationarization-obstructions/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  A graded wheel-sieve symbolic system advances through disjoint levels while generating the exact clock increment $\tau_k=\log q_{k+1}$ from its consecutive-prime recursion. We ask which stationary symbolic transformations could add intrinsic periodic orbits without erasing that endogenous clock. Three scoped obstructions screen the most immediate constructions. First, the graded source has no periodic points and its full-backward-orbit inverse limit is empty; consequently, any dynamical system with an equivariant map to that source has no periodic points. Second, a strong forward-bisimulation quotient of a graph with no infinite forward path is acyclic; finite directed acyclic graphs are a special case. Independently, a quotient whose state decoder is exact for every representative inherits the strict level grading. Third, a fixed finite-window decoder over a finite alphabet has finite image and therefore cannot recover infinitely many exact prime multipliers or clock increments. These statements are deliberately not a universal no-go theorem. An infinite acyclic graph may have an infinite forward path, and the decoder result does not cover countable alphabets or infinite memory. The project therefore retains a separately defined infinite factor or observational recoding only as an unresolved branch, subject to exact decoders and global path-lifting semantics. Its mathematical specification is incomplete, so it remains *not testable*. This stage contains no numerical experiment, defines no determinant, and leaves analytic comparison outside scope.
author:
- Anonymous Authors
date: 'August 12, 2026'
title: |
  Scoped Obstructions to Stationarizing\
  a Graded Wheel-Sieve Symbolic System
```

## Markdown 正文

# Introduction {#sec:introduction}

A symbolic system can acquire periodic words when one forgets enough of its state. That observation alone is not useful for an arithmetic symbolic model: the same forgetting can destroy the mechanism that gave the symbols their arithmetic meaning. The wheel-sieve system studied here makes this tension explicit. Its shift advances through a sequence of disjoint levels, and its level transition generates the next prime multiplier. The grading prevents periodic points, while the distinct, unbounded multipliers provide the exact clock that a proposed deformation must retain.

The central question is therefore categorical rather than computational: which kind of symbolic transformation is being proposed? A strict extension must still project to the original shift. A strong-bisimulation quotient must match successor behavior between equivalent states. A local recoding must expose the clock through a fixed observation rule. By a *stationarization* in this note we mean one target system governed by a single, cutoff-independent and level-blind rule; the exact convention is formalized in [\[def:stationarization\]](#def:stationarization){reference-type="ref" reference="def:stationarization"}. These three requirements lead to different theorems, with different scope boundaries. Treating them as interchangeable would either overstate a negative result or credit a cycle that no longer carries the endogenous arithmetic.

This note gives a theorem-level screen before any finite-cutoff search. Its one-sentence conclusion is:

> Strict extensions, forward-well-founded strong-bisimulation quotients, and finite-local exact-clock recodings are obstructed, but an explicitly defined infinite observational recoding may lie outside those theorem classes and has not yet become a testable object.

The contributions are precise and falsifiable.

1.  We prove that an equivariant extension of a strictly graded shift has no periodic points. Independently, we prove that the graded source's full-backward-orbit inverse limit is empty because arbitrarily long backward level histories do not exist.

2.  We prove that a strong forward-bisimulation quotient of a graph with no infinite forward path is acyclic, and derive the finite-DAG case as a corollary. The infinite ray shows that acyclicity alone is insufficient for arbitrary infinite graphs. A separate label-preservation proposition shows that a representative-exact next-prime state decoder prevents cross-level merging even in an infinite graph.

3.  We prove that a fixed finite-window decoder over a finite alphabet cannot output the unbounded exact prime clock. The proof is a finite-image argument and therefore says nothing against countable alphabets or infinite-memory rules.

The ingredients in these arguments---equivariant maps, full-backward-orbit inverse limits, bisimulation quotients, and finite-range symbolic observations---are standard mathematical mechanisms. We do not claim them as new standalone concepts. The contribution of this stage note is their assumption-explicit application to one wheel-sieve stationarization problem. All arguments needed for that application are reproduced below; no unverified citation metadata is used in this version.

The diagram in [\[fig:obstruction-map\]](#fig:obstruction-map){reference-type="ref" reference="fig:obstruction-map"} is also a statement of what the paper does *not* prove. The forward-well-founded theorem cannot be applied to an infinite DAG that admits an infinite forward path. The local-decoder theorem cannot be applied to a countable alphabet or a rule with unbounded memory. Those escape classes do not automatically solve the problem: they must still generate the exact clock internally and must distinguish genuine periodic paths from quotient cycles assembled from incompatible representatives.

The present evidence is entirely deductive. No Stage-02 numerical run has been executed, and finite cutoffs are not used as evidence for an infinite object. The putative observational recoding lacks a target phase space, a fixed rule, exact decoders, and path-lifting semantics. Its status is therefore [not testable]{.smallcaps}. In particular, this note does not select a determinant or begin analytic determinant comparison.

The remainder of the paper defines the graded model and the relevant categories ([2](#sec:setup){reference-type="ref" reference="sec:setup"}), proves the strict-extension obstruction ([3](#sec:extension){reference-type="ref" reference="sec:extension"}), proves the quotient obstructions ([4](#sec:bisimulation){reference-type="ref" reference="sec:bisimulation"}), and isolates the clock-locality obstruction ([5](#sec:clock){reference-type="ref" reference="sec:clock"}). specifies the obligations that a surviving infinite recoding would have to meet. The appendices audit the assumption boundaries and record the incomplete source-lock fields.

# Graded Wheel Setup and Category Discipline {#sec:setup}

We first define the arithmetic source named in the title, then isolate the smaller set of hypotheses used by each obstruction.

## The frozen wheel-sieve source

Set $Q_0=1$, $q_1=2$, and $Q_1=2$. For $k\geq1$, define $$q_{k+1}=\min\{n>q_k:\gcd(n,Q_k)=1\},
  \qquad Q_{k+1}=Q_kq_{k+1}.
  \label{eq:wheel-recurrence}$$ This recurrence contains no prime table.

[\[lem:prime-enumeration\]]{#lem:prime-enumeration label="lem:prime-enumeration"} If $p_k$ denotes the $k$th rational prime, then $q_k=p_k$ and $Q_k=\prod_{j=1}^k p_j$ for every $k\geq1$.

The assertion holds at $k=1$. Assume it through level $k$. The next prime $p_{k+1}$ is coprime to $Q_k$, so the minimum in [\[eq:wheel-recurrence\]](#eq:wheel-recurrence){reference-type="eqref" reference="eq:wheel-recurrence"} exists and $q_{k+1}\leq p_{k+1}$. If its minimizer were composite, let $r<q_{k+1}$ be a prime divisor. If $r\leq p_k$, then $r\mid Q_k$, contradicting $\gcd(q_{k+1},Q_k)=1$. If $r>p_k=q_k$, then $\gcd(r,Q_k)=1$, so $r$ is a smaller admissible integer than the minimizer, again a contradiction. Hence $q_{k+1}$ is prime. Minimality then makes it the first prime after $p_k$, namely $p_{k+1}$, and the formula for $Q_{k+1}$ follows by induction.

At level $k\geq0$, let $$R_k=\{0\leq r<Q_k:\gcd(r,Q_k)=1\}.$$ For $r\in R_k$, put an edge to each residue $r+jQ_k\in R_{k+1}$ with $0\leq j<q_{k+1}$ except the unique choice divisible by $q_{k+1}$. Let $X_k$ be the one-sided tail paths whose first edge begins at level $k$, and let $\sigma$ delete the first edge. Thus $$X=\bigsqcup_{k\geq 0} X_k,
  \qquad
  \sigma(X_k)\subseteq X_{k+1}.
  \label{eq:graded-space}$$ The exact transition clock is generated by the same recurrence: $$\tau_k=\log\frac{Q_{k+1}}{Q_k}=\log q_{k+1}.
  \label{eq:wheel-clock}$$

## Abstract hypotheses and project convention

Let $X=\bigsqcup_{k\geq0}X_k$ be a disjoint union and let $\sigma:X\to X$ satisfy $$\sigma(X_k)\subseteq X_{k+1}
  \qquad(k\geq0).
  \label{eq:strict-grading}$$ We call $(X,\sigma)$ a strictly graded shift and write $\operatorname{lev}(x)=k$ for $x\in X_k$.

The wheel system above is strictly graded. The quotient result below uses only that $q_{k+1}$ is distinct across levels; the decoder result uses only that the required output set is infinite.

[\[def:stationarization\]]{#def:stationarization label="def:stationarization"} For this project, a *stationarization proposal* specifies one target phase space $Y$, one self-map $S:Y\to Y$, one declared relation to the source, and total arithmetic and clock decoders. The proposal is *level-blind* when the target rule and decoders are fixed independently of the source level $k$ and every finite cutoff $K$, and their inputs contain neither an external level nor a stored table of $(q_k)$ or $(Q_k)$. This is an admissibility convention, not an assertion that such a target exists.

A wheel-preserving strict extension is a dynamical system $(Y,S)$ together with a total map $\pi:Y\to X$ satisfying $$\pi\circ S=\sigma\circ\pi.
  \label{eq:semiconjugacy}$$ Only this equivariance relation is used below; surjectivity of $\pi$ is not assumed. This convention avoids relying on competing uses of the word *semiconjugacy*.

For graph quotients, let $G=(V,E)$ be a directed graph and let $\sim$ be an equivalence relation on $V$.

The relation $\sim$ is a strong forward bisimulation when, for all $v\sim w$,

1.  if $vEv'$, then some $w'$ satisfies $wEw'$ and $v'\sim w'$; and

2.  if $wEw'$, then some $v'$ satisfies $vEv'$ and $v'\sim w'$.

The quotient graph $G/{\sim}$ has an edge $[v]\to[v']$ exactly when some representatives $u\in[v]$ and $u'\in[v']$ satisfy $uEu'$. The obstruction uses this definition only through successor matching.

[\[def:forward-well-founded\]]{#def:forward-well-founded label="def:forward-well-founded"} A directed graph is forward well-founded when it has no infinite directed path $v_0Ev_1Ev_2E\cdots$.

Finally, a finite-local observation consists of a finite alphabet $A$, a fixed finite coordinate window $W$, and one decoder $d:A^W\to Z$ into a declared codomain $Z$. The words *fixed* and *finite* exclude a cutoff-dependent lookup table or a window that grows with the level.

::: {#tab:scope}
  Class                                                                                                                        Conclusion                                                                                        Not covered
  ---------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------- ------------------------------------------------------------------
  Strict extension satisfying [\[eq:semiconjugacy\]](#eq:semiconjugacy){reference-type="eqref" reference="eq:semiconjugacy"}   Target has no periodic points; independently, the source's full-backward inverse limit is empty   New factor, quotient, recoding, or independent grammar
  Forward-well-founded graph plus strong forward bisimulation                                                                  Quotient acyclic                                                                                  Infinite graph with an infinite forward path; weaker graph image
  Representative-exact, level-injective state-class decoder                                                                    Quotient inherits strict grading                                                                  Edge or path decoder that distinguishes representatives
  Finite alphabet plus fixed finite window                                                                                     Infinite exact output set undecodable                                                             Countable alphabet, infinite memory, or another unbounded input

  : Each obstruction is tied to an explicit hypothesis class. The rightmost column is part of the result, not a proposed construction.
:::

The discipline in [1](#tab:scope){reference-type="ref" reference="tab:scope"} prevents two errors. First, a theorem cannot be enlarged by silently dropping one of its hypotheses. Second, an object outside a no-go theorem does not receive positive evidence merely by escaping that theorem.

# Strict Extensions Cannot Supply Periodic Orbits {#sec:extension}

The grading already closes the most literal stationarization proposal.

[\[thm:extension\]]{#thm:extension label="thm:extension"} Let $(X,\sigma)$ be a strictly graded shift. If $(Y,S)$ and $\pi:Y\to X$ satisfy [\[eq:semiconjugacy\]](#eq:semiconjugacy){reference-type="eqref" reference="eq:semiconjugacy"}, then $$\operatorname{Fix}(S^n)=\varnothing
  \qquad\text{for every }n\geq1.$$

Suppose $S^ny=y$ for some $y\in Y$ and $n\geq1$. Iterating [\[eq:semiconjugacy\]](#eq:semiconjugacy){reference-type="eqref" reference="eq:semiconjugacy"} gives $$\sigma^n(\pi(y))=\pi(S^ny)=\pi(y).$$ If $\pi(y)\in X_k$, strict grading places the left-hand side in $X_{k+n}$ and the right-hand side in $X_k$. The components are disjoint, so equality is impossible.

For the graded source itself, the standard natural-extension construction also collapses, for a different but related reason.

[\[prop:inverse-limit\]]{#prop:inverse-limit label="prop:inverse-limit"} For a strictly graded shift, $$\varprojlim(X,\sigma)
 =\bigl\{(x_0,x_{-1},\ldots):
     \sigma(x_{-j})=x_{-j+1}\text{ for every }j\geq1\bigr\}
 =\varnothing.$$ Moreover, $$\bigcap_{n\geq0}\sigma^n(X)=\varnothing.$$

Assume $x_0\in X_k$ has a full backward orbit. Because every application of $\sigma$ raises the level by one, disjointness forces $x_{-j}\in X_{k-j}$. No component with negative index exists, contradicting the requirement when $j>k$.

For the intersection statement, [\[eq:strict-grading\]](#eq:strict-grading){reference-type="eqref" reference="eq:strict-grading"} yields $\sigma^n(X)\subseteq\bigsqcup_{k\geq n}X_k$. A point has one finite level, so it cannot belong to all of these tails.

[\[rem:extension-scope\]]{#rem:extension-scope label="rem:extension-scope"} concern systems that retain an equivariant map *to the frozen wheel shift*. A factor, observational recoding, quotient, or independently defined stationary grammar may not satisfy [\[eq:semiconjugacy\]](#eq:semiconjugacy){reference-type="eqref" reference="eq:semiconjugacy"} in this direction. Such a construction is not refuted here, but neither is it an extension of the stated kind; it must re-establish its arithmetic interpretation from its own definition.

# Strong-Bisimulation Quotients: Well-Founded and Labelled Cases {#sec:bisimulation}

A quotient may contain a cycle even when its source graph does not: different quotient edges can be witnessed by incompatible representatives. Successor matching prevents that defect whenever the source admits no infinite forward path.

[\[thm:well-founded-bisim\]]{#thm:well-founded-bisim label="thm:well-founded-bisim"} Let $G=(V,E)$ be forward well-founded and let $\sim$ be a strong forward bisimulation. Then the quotient graph $G/{\sim}$ is acyclic.

Assume, for contradiction, that the quotient contains a directed cycle $$C_0\longrightarrow C_1\longrightarrow\cdots
  \longrightarrow C_{m-1}\longrightarrow C_m=C_0,
  \qquad m\geq1.$$ For each $i\in\{0,\ldots,m-1\}$, choose representatives $a_i\in C_i$ and $b_{i+1}\in C_{i+1}$ such that $a_iEb_{i+1}$, with indices read modulo $m$.

Choose any $v_0\in C_0$. Suppose $v_j\in C_i$ has been chosen, where $i\equiv j\pmod m$. Since $v_j\sim a_i$ and $a_iEb_{i+1}$, successor matching supplies $v_{j+1}$ such that $$v_jEv_{j+1}
  \qquad\text{and}\qquad
  v_{j+1}\sim b_{i+1}.$$ Thus $v_{j+1}\in C_{i+1}$. Induction constructs an infinite directed path $v_0Ev_1Ev_2E\cdots$ in $G$, contradicting forward well-foundedness.

[\[cor:finite-bisim\]]{#cor:finite-bisim label="cor:finite-bisim"} A strong forward-bisimulation quotient of a finite directed acyclic graph is acyclic.

An infinite path in a finite graph repeats a vertex, and the positive segment between two repetitions is a directed cycle. A finite DAG is therefore forward well-founded, so [\[thm:well-founded-bisim\]](#thm:well-founded-bisim){reference-type="ref" reference="thm:well-founded-bisim"} applies.

Acyclicity alone cannot replace forward well-foundedness for an arbitrary infinite source.

[\[rem:infinite-ray\]]{#rem:infinite-ray label="rem:infinite-ray"} Let $V=\mathbb{N}$ and put one edge $n\to n+1$ at every vertex. This infinite graph is acyclic but not forward well-founded. The universal equivalence relation, under which all vertices are equivalent, is a strong forward bisimulation: the unique successors of any two vertices are again equivalent. Its quotient has one vertex and a self-loop. Thus [\[thm:well-founded-bisim\]](#thm:well-founded-bisim){reference-type="ref" reference="thm:well-founded-bisim"} cannot be enlarged to all infinite DAGs by retaining acyclicity alone.

For the wheel system, an independent grading argument applies when one state-class decoder must be exact for every representative of that class.

[\[prop:label-grading\]]{#prop:label-grading label="prop:label-grading"} Let $V=\bigsqcup_{k\geq0}V_k$, and suppose every edge goes from $V_k$ to $V_{k+1}$. Let $\lambda:V\to\Lambda$ be constant on each $V_k$, with pairwise distinct values across levels. If $$v\sim w \quad\Longrightarrow\quad \lambda(v)=\lambda(w),
  \label{eq:label-respecting}$$ then $G/{\sim}$ is acyclic. Graph finiteness and bisimulation are not needed.

Condition [\[eq:label-respecting\]](#eq:label-respecting){reference-type="eqref" reference="eq:label-respecting"} and injectivity of the level labels force every equivalence class to lie in a single $V_k$. Define $$\overline{\operatorname{lev}}([v])=k \qquad\text{when }v\in V_k.$$ This quotient grading is well-defined. If $[v]\to[w]$, some representatives $v'\in[v]$ and $w'\in[w]$ satisfy $v'Ew'$, hence $$\overline{\operatorname{lev}}([w])=\overline{\operatorname{lev}}([v])+1.$$ The quotient level increases along every positive-length path, so no path can return to its starting class.

[\[cor:q-label\]]{#cor:q-label label="cor:q-label"} Let $G$ be the graded wheel graph and suppose there is one state-class decoder $D:V/{\sim}\to\mathbb{N}$ satisfying $$D([v])=q_{\operatorname{lev}(v)+1}
  \qquad\text{for every source representative }v.
  \label{eq:class-decoder-exact}$$ Then the quotient cannot merge different levels and cannot contain a directed cycle.

If $v\sim w$, then [\[eq:class-decoder-exact\]](#eq:class-decoder-exact){reference-type="eqref" reference="eq:class-decoder-exact"} gives $q_{\operatorname{lev}(v)+1}=D([v])=D([w])=q_{\operatorname{lev}(w)+1}$. By [\[lem:prime-enumeration\]](#lem:prime-enumeration){reference-type="ref" reference="lem:prime-enumeration"}, the values $q_k$ are pairwise distinct, so $\operatorname{lev}(v)=\operatorname{lev}(w)$. Apply [\[prop:label-grading\]](#prop:label-grading){reference-type="ref" reference="prop:label-grading"} with $\lambda(v)=q_{\operatorname{lev}(v)+1}$.

The proof of [\[thm:well-founded-bisim\]](#thm:well-founded-bisim){reference-type="ref" reference="thm:well-founded-bisim"} uses successor matching and the absence of an infinite forward source path. It does not apply to an infinite ray, a one-way simulation, a bounded-radius observational equivalence, or an arbitrary graph homomorphic image. The proof of [\[prop:label-grading\]](#prop:label-grading){reference-type="ref" reference="prop:label-grading"} applies only when the state-class decoder is exact for every representative. An edge decoder or a path-window decoder that distinguishes representatives within one state class falls outside that proposition. Falling outside either theorem creates an open proof obligation, not evidence of an arithmetic periodic orbit.

For a finite cutoff, [\[cor:finite-bisim\]](#cor:finite-bisim){reference-type="ref" reference="cor:finite-bisim"} removes the proposed positive branch entirely: a correctly computed strong-bisimulation quotient cannot produce a cycle. Running the quotient code could still serve as a regression test, but it could not supply positive Stage-02 evidence.

# The Exact-Clock Locality Obstruction {#sec:clock}

Removing the explicit level label does not by itself make the arithmetic clock local. A fixed finite symbolic observation has only finitely many possible values, independently of the decoder codomain.

[\[thm:finite-local\]]{#thm:finite-local label="thm:finite-local"} Let $A$ be a finite alphabet, let $W$ be a fixed finite coordinate window, let $Z$ be any set, and let $d:A^W\to Z$ be a fixed decoder. Then $\operatorname{im}(d)$ is finite. Consequently, no such decoder can recover every member of an infinite prescribed target set.

The pattern set $A^W$ is finite because both $A$ and $W$ are finite. The image of a function on a finite domain is finite.

[\[cor:finite-local-wheel\]]{#cor:finite-local-wheel label="cor:finite-local-wheel"} Neither a fixed decoder $d_q:A^W\to\mathbb{N}$ nor a fixed decoder $d_\tau:A^W\to\mathbb{R}$ can recover, respectively, all exact values $q_k$ or all exact values $\log q_k$ from a finite-alphabet fixed-window observation.

By [\[lem:prime-enumeration\]](#lem:prime-enumeration){reference-type="ref" reference="lem:prime-enumeration"}, the set $\{q_k:k\geq1\}$ is infinite. The logarithm is injective on positive numbers, so $\{\log q_k:k\geq1\}$ is infinite as well. Apply [\[thm:finite-local\]](#thm:finite-local){reference-type="ref" reference="thm:finite-local"} to each codomain.

[\[cor:local-escape\]]{#cor:local-escape label="cor:local-escape"} Any recoding that recovers all exact multipliers with one unchanged rule must drop at least one hypothesis of [\[thm:finite-local\]](#thm:finite-local){reference-type="ref" reference="thm:finite-local"}: it must use an infinite alphabet, an unbounded observation domain or memory, or an additional unbounded input to the decoder.

is necessary, not sufficient. A countable alphabet can carry unbounded data, and an infinite-memory map can inspect unbounded context, so neither class is excluded by the finite-image proof. The theorem does not establish that either class admits a shift-commuting, level-blind, arithmetic-faithful recoding.

There is also a distinction between escaping the theorem and satisfying the research scope. A decoder that reads the external level, consults a stored prime table, or changes with cutoff has an infinite source of information and may evade the cardinality argument. Such a decoder violates [\[def:stationarization\]](#def:stationarization){reference-type="ref" reference="def:stationarization"}; its failure is an arithmetic-fidelity failure, not a consequence of [\[thm:finite-local\]](#thm:finite-local){reference-type="ref" reference="thm:finite-local"}.

The exact boundary is therefore:

> Finite alphabet plus fixed finite window is impossible for exact recovery of an infinite clock range. Countable alphabet or infinite memory is unclassified until one explicit function space, topology, shift rule, and decoder are defined.

# The Surviving Class and Its Current Status {#sec:surviving}

The preceding results leave a broad unresolved possibility: a separately defined infinite factor or observational recoding that is neither a strict extension in the direction of [\[eq:semiconjugacy\]](#eq:semiconjugacy){reference-type="eqref" reference="eq:semiconjugacy"}, nor a forward-well-founded strong-bisimulation quotient, nor a finite-local exact-clock code. The word *possibility* is logical. It does not name a construction and does not supply evidence.

::: {#tab:status}
  Proposed class                                                 Current decision           Reason
  -------------------------------------------------------------- -------------------------- ----------------------------------------------------------------------
  Strict equivariant extension                                   Excluded in this class
  Forward-well-founded strong-bisimulation quotient              Excluded in this class
  Quotient with a representative-exact $q_{k+1}$ state decoder   Excluded in this class
  Finite-alphabet fixed-window exact-clock recoding              Excluded in this class
  Other infinite observational recoding                          Undefined / not testable   Target object, rule, decoders, and path semantics remain unspecified
  Analytic determinant comparison                                Outside current scope      No infinite arithmetic and primitive-orbit ledger exists

  : Stage-02 decisions follow from theorem hypotheses or from missing definitions. None is a numerical verdict.
:::

For this note, a *complete mathematical specification* (called a "source lock" in the project records) is a frozen definition of one infinite object together with every map, decoder, and approximation convention needed to test it. Before the unresolved branch becomes a mathematical object, that specification must include at least the following data.

1.  **Category and dynamics.** The target phase space $Y$, the target shift $S$, the map direction, the commutative relation, and whether $Y$ is an image or an orbit closure.

2.  **Grammar and regularity.** The alphabet and its topology if countable; one level-blind rule independent of cutoff; and either a coding radius or a named infinite-memory function class with its continuity requirements.

3.  **Labels and transitions.** Vertex and edge labels, treatment of parallel edges and deleted branches, and a target transition rule fixed on the infinite system.

4.  **Exact decoders.** Total arithmetic and clock decoders, with proofs that they recover the unit-residue data and the exact identity $\tau_k=\log q_{k+1}$ without an external level, prime table, or cutoff-dependent rule.

5.  **Path compatibility.** For a claimed target periodic point in the direct image, one single one-sided infinite source path must recode to its indefinitely repeated target itinerary. The source path need not be periodic. If a target periodic point is admitted only through an orbit closure, a separate approximation and clock-inheritance theorem is required.

6.  **Finite approximation.** Terminal markers, an interior comparison region, and restriction or extension maps that make every cutoff an approximation to the same infinite object.

Path compatibility is especially important. Suppose a quotient has edges $C_i\to C_{i+1}$ and each edge has a source witness. Without a lifting rule, the terminal representative of the witness for $C_i\to C_{i+1}$ need not be the initial representative of any witness for $C_{i+1}\to C_{i+2}$. A closed word in the coarse graph can therefore be assembled from locally valid but globally incompatible edges. Such a word is not yet a periodic point with a globally inherited arithmetic itinerary.

The current specification leaves the target system, alphabet, rule, decoders, closure convention, and finite-approximation semantics unresolved. Accordingly, no implementation run is authorized. Even a later finite periodic witness would authorize only an infinite theorem attempt; it would not by itself establish arithmetic fidelity or completeness of a primitive orbit ledger.

The governance consequence is unambiguous. The remaining branch is [not testable]{.smallcaps}. There is no Stage-02 numerical evidence and no determinant convention. Analytic determinant comparison remains outside the present stage.

# Conclusion and Limitations {#sec:conclusion}

Three scoped obstructions now delimit the wheel-sieve stationarization problem. Equivariant strict extensions cannot contain periodic points; independently, the graded source's full-backward-orbit inverse limit is empty. Strong forward-bisimulation cannot create quotient cycles when the source has no infinite forward path; finite DAGs are a special case. If one state-class decoder is exact for every representative, a separate grading argument blocks cross-level merging without a finiteness assumption. A finite alphabet observed through one fixed finite window cannot decode the infinite exact clock range.

These results close natural but narrow construction classes. They do not form a universal no-go theorem. An infinite DAG with an infinite forward path may have a cyclic strong-bisimulation quotient, as the infinite-ray example shows. A countable alphabet or an infinite-memory decoder falls outside the finite-image argument. Neither escape, however, supplies the missing arithmetic decoder, shift-commuting rule, or compatible path lift.

The next research step is therefore definitional rather than empirical: specify one infinite observational recoding completely and prove that it is a single, cutoff-independent symbolic system. Until that task is complete, the branch is [not testable]{.smallcaps}. This stage supports no numerical claim and defines no determinant; analytic determinant comparison remains outside scope.

# Proof-Dependency and Boundary Audit {#app:audit}

This appendix records exactly where each assumption enters. It is intended to prevent later finite experiments or recoding proposals from silently enlarging the theorems.

::: {#tab:assumption-audit}
  Result   Assumptions actually used                                    Failure or escape when removed
  -------- ------------------------------------------------------------ -----------------------------------------------------------------------------------------
           Frozen recurrence, elementary prime factorization            A stored or altered multiplier sequence is a different source
           Disjoint levels, strict level growth, equivariance           No conclusion for a new object without a map to the frozen shift
           Nonnegative levels and one-level forward growth              A bi-infinite grading or added predecessors changes the object
           No infinite forward path and successor matching              The infinite ray gives a cyclic quotient; weaker images need not lift paths
           Finite source and source acyclicity                          These hypotheses imply forward well-foundedness
           One-level edge growth and a class label injective in level   No conclusion for edge/path decoders that distinguish representatives
           Finite alphabet, fixed finite window, fixed decoder          An infinite alphabet, infinite memory, or unbounded input avoids the finite-domain step

  : Assumption audit for the proved statements.
:::

## The infinite-ray boundary in full

Let $G$ have vertices $v_n$ for $n\in\mathbb{N}$ and edges $v_n\to v_{n+1}$. A directed cycle would require the index to return to a smaller value, so $G$ is acyclic. It is not forward well-founded because the displayed ray is an infinite path. Put $v_n\sim v_m$ for all $n,m$. Given any related vertices, their unique successors are again related, in both directions required by strong forward bisimulation. The quotient has one class $C$, and every source edge witnesses $C\to C$. Thus $G/{\sim}$ has a self-loop. This example shows that acyclicity alone cannot replace the no-infinite-forward-path hypothesis in [\[thm:well-founded-bisim\]](#thm:well-founded-bisim){reference-type="ref" reference="thm:well-founded-bisim"}.

The counterexample does not validate an infinite wheel quotient. Its one-class quotient has forgotten every level-dependent value, including the exact wheel multiplier. It demonstrates a theorem boundary and nothing more.

## Why cutoff stability is not an infinite definition

Suppose partitions are computed independently at several finite cutoffs. Even identical-looking class counts do not specify an infinite quotient. A definition still needs restriction or extension maps that commute with the source and target shifts, a treatment of terminal classes, and a proof that interior classes are consistent as the cutoff changes. Without those data, one cannot decide whether a finite closed word persists, whether it is a boundary artifact, or whether its edge witnesses form one compatible one-sided infinite lift.

The preregistered cutoffs can test an already defined infinite rule. They cannot supply the rule, its decoder, or its consistency theorem.

# Mathematical-Specification Readiness Ledger {#app:source-lock}

The unresolved branch has no candidate identifier. The following ledger records the fields that must be frozen before code can provide relevant evidence.

  Field                     Required content                                                                                                                      Current state
  ------------------------- ------------------------------------------------------------------------------------------------------------------------------------- ---------------
  Category and maps         Exactly one of factor, quotient, or recoding; target space and shift; map direction; commutative relation; image/closure convention   Pending
  Alphabet and regularity   Alphabet topology if countable; coding radius or named infinite-memory class; continuity and complexity bounds                        Pending
  Frozen rule               One level-blind infinite rule, canonical serialization, and proof of cutoff independence                                              Pending
  Labels and transitions    Vertex/edge labels, parallel-edge multiplicity, deleted-branch convention, and target transition rule                                 Pending
  Arithmetic decoder        Total domain and formula; exact unit-residue recovery without a prime table or external level                                         Pending
  Clock decoder             State/edge/window domain and exact recovery of $q_{k+1}$ and $\log q_{k+1}$                                                           Pending
  Path lifting              One global one-sided lift for a direct-image periodic itinerary, or a closure/inheritance theorem for a closure-only point            Pending
  Finite approximation      Terminal marker, interior region, and restriction/extension consistency equation                                                      Pending
  Analytic layer            Function space and determinant convention, only after an infinite arithmetic and orbit ledger                                         Locked

Because all defining fields remain pending, the observational-recoding branch is [not testable]{.smallcaps}. The correct next action is to complete one infinite source lock, not to search across finite quotient rules or enlarge a cutoff after seeing results.

## Evidence and sharing record

This manuscript restates the wheel recurrence and every strict-extension, bisimulation, grading, and local-decoder argument used in its conclusions, so the PDF is mathematically self-contained. These standard mechanisms are not claimed as new standalone concepts; the contribution is their scoped use in the present screening problem. The theorem relationship figure is pure TikZ and contains no measurements. No external citation metadata, experimental result, random seed, or compute claim enters the paper.

The sharing status at this draft is:

-   anonymous author block;

-   theorem-only evidence;

-   no Stage-02 numerical run;

-   determinant convention not defined; and

-   Route B---the later analytic determinant-comparison route---locked.
