# Source Lock — SD-C25

**Freeze date:** 2026-08-14  
**Primary family:** Symbolic Dynamics  
**Authority object:** the ordered cofactor fiber over the holonomy-two
canonical cycles of the successor–divisor countable Markov shift  
**Target-zero data:** forbidden and unused  
**Route-B invocation:** forbidden  
**Review loop:** excluded by instruction

## 1. Full-shift skeleton

For an \(n\)-letter alphabet \(A_n\), let

\[
        F_n=A_n^{\mathbb Z}
\]

up to topological conjugacy.  Freeze

\[
 F_m\boxtimes F_n:=F_{A_m\times A_n}\cong F_{mn},
\]

\[
 F_m\boxplus F_n:=F_{A_m\sqcup A_n}\cong F_{m+n},
\]

\[
 S(F_n)=F_n\boxplus F_1\cong F_{n+1},
 \qquad h(F_n)=\log n.
\]

The symbol \(\boxplus\) means alphabet disjoint union followed by the
full-shift functor.  It is not claimed to be the categorical coproduct of
subshifts.

## 2. Frozen successor–divisor graph

Let

\[
 V=\{2,3,\ldots\},\qquad
 n\to d\iff d\ge2\ \text{and}\ d\mid n+1.
\]

Every edge carries the unique factor witness

\[
 q(n,d)=\frac{n+1}{d}\in\mathbb N,
\]

equivalently

\[
        S(F_n)\cong F_d\boxtimes F_{q(n,d)}.
\]

The one-sided phase space is

\[
 X_G^+
 =\{(n_0,n_1,\ldots)\in V^{\mathbb N}:n_j\to n_{j+1}\}.
\]

No primality predicate, rational-prime table, target Euler coefficient, or
Riemann-zero table enters the graph.

## 3. Imported canonical family

Paper22 proves

\[
 Q(\gamma)=2
 \iff
 \gamma=C_k=(k,k+1,\ldots,2k-1),
 \qquad k\ge2,
\]

up to cyclic rotation.  Each \(C_k\) is primitive and contains a unique
least vertex \(k\).  Paper23 marks that vertex and freezes the ordered
quotient word

\[
        W(C_k)=1^{k-1}2.
\]

The proof is elementary: \(q=1\) on the \(k-1\) successor edges and \(q=2\)
on \(2k-1\to k\).  Reflections are not identified.

## 4. Fixed finite fibers

A fixed finite semigroup fiber is a morphism

\[
        \phi:\{1,2\}^{+}\to S
\]

with \(S\) finite.  Put

\[
        a=\phi(1),\qquad b=\phi(2).
\]

Word multiplication follows reading order:
\(\phi(xy)=\phi(x)\phi(y)\).  For a DFA, transformations act on column
states and compose as functions, so reading \(1^{k-1}2\) gives
\[
        T_2\circ T_1^{k-1}(q_0).
\]
These two conventions are compatible descriptions of their respective
models and are not silently interchanged.

Its canonical response is a function of

\[
        a^{k-1}b.
\]

Finite groups, characters, DFAs, NFAs, and finite transformation
semigroups are special cases.  The fiber is fixed before the cutoff or
target comparison.  A sequence of fibers whose size grows with the cutoff
is a different model.

## 5. Fixed finite-dimensional fibers

Let \(\mathbb F\) be a characteristic-zero field and let

\[
        A,B\in M_d(\mathbb F),\qquad u,v\in\mathbb F^d
\]

be fixed independently of \(k\).  Freeze the two exact response families

\[
 x_k=u^{\mathsf T}A^{k-1}Bv,
\qquad
 y_k=\operatorname{tr}(A^{k-1}B).
\]

The trace response is cyclically invariant.  The bilinear response uses the
unique-minimum mark and the word-evaluation convention.  With the
column-source operator convention, a traversal composes as \(BA^{k-1}\);
trace cyclicity recovers \(y_k\), while the bilinear convention is realized
by transposing the representation and swapping endpoint vector/covector.

The exact predicate licensed for Skolem–Mahler–Lech credit is
zero/nonzero support or equality to a fixed scalar.  Sign, positivity,
threshold, order, and variable-tolerance predicates are not frozen claims.

## 6. Same-object weighted adjacency

Restrict the graph to \(q\in\{1,2\}\).  On

\[
        A,B\in M_d(\mathbb C),
\]

and

\[
 \mathcal H=\ell^2(\{2,3,\ldots\})\otimes\mathbb C^d
\]

with column-source convention, freeze

\[
\begin{aligned}
 L_{s,A,B}(e_n\otimes\xi)
 &=(n(n+1))^{-s}e_{n+1}\otimes A\xi\\
 &\quad+
 \mathbf1_{\{n\ {\rm odd}\}}
 \bigl(n(n+1)/2\bigr)^{-s}
 e_{(n+1)/2}\otimes B\xi .
\end{aligned}
\]

This is a weighted vertex adjacency.  It is not identified with a Ruelle
operator on a Hölder space.

For fixed complex matrices \(A,B\), not both zero,

\[
        L_{s,A,B}\in\mathcal S_1
        \iff \Re s>\frac12.
\]

On that half-plane, freeze the Fredholm determinant

\[
        D_{A,B}(s,z)=\det(I-zL_{s,A,B}).
\]

The determinant is entire in \(z\).  Its logarithmic trace expansion is
used as the normalized germ at \(z=0\); no global logarithm through
determinant zeros is asserted.

## 7. Frozen graph marker and roof

The graph-step marker is \(z\) per edge.  Paper21's endpoint roof is

\[
        \tau(n,d)=\log(nd).
\]

For the canonical orbit,

\[
        |C_k|=k,
\]

\[
 R(C_k)=2\log M_k,
\qquad
 M_k=\prod_{n=k}^{2k-1}n
     =\frac{(2k-1)!}{(k-1)!}.
\]

Hence the scalar cycle monomial is

\[
        w_k=z^kM_k^{-2s}.
\]

For a genuine \(d\)-dimensional block fiber, the local block factor is

\[
 \Delta_k(s,z)
 =\det_{\mathbb C^d}\!\left(I-w_kBA^{k-1}\right),
\]

and its local trace logarithm is

\[
 -\log\Delta_k(s,z)
 =\sum_{r\ge1}\frac{w_k^r}{r}
   \operatorname{tr}\!\left((BA^{k-1})^r\right).
\]

The expression
\[
        w_k\operatorname{tr}(BA^{k-1})
\]
is only the first trace-log coefficient.  Its vanishing does not delete the
block factor.  For example,
\(BA^{k-1}=\operatorname{diag}(1,-1)\) has trace zero but local factor
\(1-w_k^2\).  A marked bilinear observable
\(u^{\mathsf T}A^{k-1}Bv\) is not a determinant coefficient.

The complete factor has the exterior-power expansion

\[
 \Delta_k(s,z)
 =\sum_{j=0}^d(-w_k)^j
  \operatorname{tr}\!\left((\wedge^jB)(\wedge^jA)^{k-1}\right).
\]

Each fixed coefficient sequence is an LRS, so the set on which the full
block factor is nontrivial is ultimately periodic.  This conclusion is not
obtained by replacing the block factor with its first trace-log term.

Separately, an explicitly assumed one-dimensional oracle deletion control
may attach \(c_k\in\{0,1\}\) and use \(1-w_kc_k\).  That control is not a
consequence of the block trace.  Neither a block fiber nor the scalar
control may replace \(z^k\) by \(z\), or \(M_k^{-2s}\) by \(k^{-s}\),
without declaring a new object.

## 8. Growing finite-memory control

For a frozen cutoff \(N\), an \(N\)-dimensional nilpotent shift may be used
only as a control.  Its response vector or terminal matrix explicitly
stores the requested \(N\) values.  Prime, square, Fibonacci, random, hash,
and arbitrary rational sequences must be matched.

Every growing-dimension finite fit is labeled

\[
        \mathrm{CONTROL\;|\;PROVES\_TOO\_MUCH}.
\]

It earns no A1 or A3 credit.

## 9. Countable-wrapper boundary

Two architectures are frozen as imported controls:

1. **Paper19 transient wrapper.**  A total computation is acyclic; accepted
   inputs enter diagonal loops and rejected inputs enter an acyclic cemetery.
   Traces and determinants see only the selected loops.  The wrapper
   compiles arbitrary decidable support.
2. **Paper20 recurrent wrapper.**  Accepted computations are closed into
   disjoint cycles.  If a nonnegative total roof \(\log n\) is distributed
   over length \(\ell(n)\) and
   \(\ell(n)/\log n\to\infty\), some edge weights tend to one and the whole
   vertex adjacency is noncompact.  First return changes
   \(z^{\ell(n)}\) to \(z\).

These statements do not classify every countable symbolic extension.

## 10. Allowed and forbidden information

Allowed:

- successor, tensor witnesses, quotient letters, graph paths, and cycles;
- the unique-minimum marking of \(C_k\);
- fixed finite semigroup/group/automaton and matrix fibers;
- exact integer, rational, symbolic, and finite-field audit arithmetic;
- the frozen endpoint roof, trace-class operator, and Fredholm determinant;
- primes only in a post-freeze evaluator or explicit oracle control.

Forbidden:

- primality or factorization calls in graph/fiber construction;
- a target-aware terminal map presented as intrinsic;
- target coefficients embedded into \(A,B,u,v\);
- dimension growth hidden as one fixed fiber;
- Riemann-zero data or zero-fit statistics;
- an induced return operator presented as the original vertex adjacency;
- a changed roof or marker presented as a same-object identity;
- Route-B constructions.

## 11. Frozen theorem ledger

The manuscript may claim:

1. \(W(C_k)=1^{k-1}2\);
2. infinite prime-only ultimately periodic sets do not exist;
3. every fixed finite-semigroup, group, DFA, or NFA response on this family
   is eventually periodic;
4. every fixed characteristic-zero bilinear or trace response is a linear
   recurrence sequence;
5. Skolem–Mahler–Lech makes its exact support ultimately periodic;
6. a growing nilpotent shift memorizes every finite response prefix;
7. fixed finite blocks preserve the trace-class half-plane
   \(\Re s>1/2\);
8. the two licensed Paper19/Paper20 total-decider wrappers prune or
   clock-dilute as specified above;
9. general block factors have the determinant and trace-log formulas above;
10. their exterior-power coefficient supports are ultimately periodic;
11. a separately assumed one-dimensional oracle deletion control still
   preserves the factorial roof and \(z^p\) marker.

The manuscript may not claim:

- a new unary-automata theorem;
- a new Skolem–Mahler–Lech theorem;
- the first SML period-set obstruction in Symbolic Dynamics;
- impossibility for all nonlinear or countable systems;
- a prime Euler determinant, RH result, or Hilbert–Pólya operator.

The frozen exact audit passed 32/32 tests.  Its E1 census contains 4,095
cycles and 8,390,655 edges; its block regression records first trace zero,
second repetition trace two, and full factor \(1-w^2\); and its 31 generated
artifacts are byte-identical across two runs with combined SHA-256
`25d1dc42431693a0b380741531238b5b52bbbb62f5c9602afe13845a67ebd336`.
These are implementation certificates, not substitutes for proof.

## 12. Literature source lock

Central DOI records are frozen in [LITERATURE_AUDIT.md](LITERATURE_AUDIT.md)
and [references.bib](references.bib).  De Jong 2026 is the closest direct
Symbolic-Dynamics collision and restricts the novelty claim to the
model-specific closure chain.

## 13. Route lock

\[
(\mathrm{A0\_STRUCTURAL\_ARITHMETIC\_RELATION},
 \mathrm{A1\_WEAK},
 \mathrm{A2\_ANALYTIC\_DETERMINANT},
 \mathrm{A3\_FAIL},
 \mathrm{A4\_FAIL}).
\]

\[
        \mathrm{ROUTE\_A\_REJECTED}.
\]

Route B is locked.

The A3 label is a theorem consequence within the frozen model class.  The
A4 label records that no critical-line or Hilbert--Pólya mechanism is
constructed; it is not a nonexistence theorem.
