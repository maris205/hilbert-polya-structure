# Preregistration — SD-C25

**Freeze date:** 2026-08-14  
**Candidate:** SD-C25  
**Primary family:** Symbolic Dynamics  
**Zero-data firewall:** active  
**Review loop:** excluded by instruction  
**Experiment status at freeze:** protocol only; no unexecuted count is
reported as a result

## 1. Research question

Does the ordered source-derived cofactor word

\[
        W(C_k)=1^{k-1}2
\]

support a fixed finite or finite-dimensional fiber whose exact recurrent
coefficient isolates prime \(k\), while retaining the same
successor–divisor vertex determinant and its natural roof?

## 2. Frozen candidate

The base graph is

\[
 V=\{2,3,\ldots\},\qquad
 n\to d\iff d\ge2,\ d\mid n+1,
\]

with quotient witness

\[
        q(n,d)=\frac{n+1}{d}.
\]

The imported \(Q=2\) primitive family is

\[
        C_k=(k,k+1,\ldots,2k-1),
\]

marked at its unique minimum.  The ordered word, graph length, endpoint
roof, and scalar cycle monomial are frozen as

\[
 W(C_k)=1^{k-1}2,\qquad
 |C_k|=k,
\]

\[
 R(C_k)=2\log M_k,\qquad
 M_k=\frac{(2k-1)!}{(k-1)!},
\]

\[
        z^kM_k^{-2s}.
\]

## 3. Primary hypotheses

**H1 — finite-semigroup periodicity.**  For every fixed finite semigroup
morphism, the response to \(1^{k-1}2\) is eventually periodic.

**H2 — finite-automaton no-go.**  A fixed DFA or NFA cannot accept exactly
the prime values of \(k\), or any infinite prime-only subset.

**H3 — fixed-dimensional recurrence.**  For a characteristic-zero field
\(\mathbb F\) and fixed
\(A,B\in M_d(\mathbb F)\), \(u,v\in\mathbb F^d\), the responses

\[
 u^{\mathsf T}A^{k-1}Bv,\qquad
 \operatorname{tr}(A^{k-1}B)
\]

satisfy the characteristic recurrence of \(A\).

**H4 — exact support obstruction.**  Skolem–Mahler–Lech makes the zero set
of either response a finite union of arithmetic progressions plus a finite
set.  Its nonzero support is ultimately periodic and cannot be infinite
prime-only support.

**H5 — finite-cutoff universality.**  Every \(N\)-term scalar response has an
\(N\)-dimensional nilpotent bilinear realization and an \(N\)-dimensional
trace realization.

**H6 — finite-fit nonselectivity.**  The nilpotent construction fits primes,
squares, powers of two, Fibonacci membership, seeded random bits, and
arbitrary rational values with the same architecture.  It is
PROVES_TOO_MUCH.

**H7 — same-object Fredholm domain.**  For fixed
\(A,B\in M_d(\mathbb C)\), not both zero, on
\(\ell^2(V)\otimes\mathbb C^d\),

\[
        L_{s,A,B}\in\mathcal S_1
        \iff \Re s>\frac12.
\]

**H8 — licensed countable-wrapper alternative.**  In the Paper19
transient wrapper, computation prunes to diagonal selected loops.  In the
Paper20 recurrent wrapper, total roof \(\log n\) and
\(\ell(n)/\log n\to\infty\) imply noncompactness; first return changes the
graph marker.  No claim covers every countable symbolic extension.

**H9 — factorial-roof persistence with ledger separation.**  A genuine
block fiber has local factor
\[
 \det_{\mathbb C^d}(I-w_kBA^{k-1}),
 \qquad w_k=z^kM_k^{-2s},
\]
whose first trace-log term is
\(w_k\operatorname{tr}(BA^{k-1})\).  A marked bilinear response is a
separate observable.  A zero first trace does not delete a block factor;
the complete exterior-power coefficient sequences are LRS and control when
that factor is nontrivial.  Even a separately assumed one-dimensional oracle
prime-deletion control retains \(w_p=z^pM_p^{-2s}\), not \(zp^{-s}\).

**H10 — Route closure.**  H1–H9 imply A3 fails for SD-C25 despite a
source-intrinsic word and an honest finite-fiber Fredholm determinant.  The
project constructs no critical-line or Hilbert--Pólya mechanism, so its
evaluation label is A4_FAIL; this is not a theorem that such a mechanism
cannot exist elsewhere.

All ten hypotheses are theorem-level or explicitly imported scoped claims.
Finite computation is an audit only.

## 4. Exact predicate boundary

The primary finite-dimensional test is

\[
        r_k=0\quad\text{versus}\quad r_k\ne0.
\]

Fixed-level tests \(r_k=c\) are allowed by applying the zero-set theorem to
\(r_k-c\).  Sign, positivity, threshold, cutpoint, and variable-tolerance
recognition are outside the hypothesis.  A failure of one of these stronger
predicates does not count as evidence for H4.

## 5. Exact audit protocol

### E1 — source/no-oracle certificate

For \(2\le k\le4096\), generate \(C_k\), verify every edge by exact
divisibility, and assert:

\[
 W(C_k)=1^{k-1}2,\quad |C_k|=k,\quad Q(C_k)=2.
\]

Static inspection must report zero candidate calls or identifiers for
primality, prime tables, factorization libraries, or zero data.

### E2 — finite-state periodicity

Exhaust all unary maps on \(|Q|\le4\), with systematic terminal maps and
accepting sets.  Compute exact tail \(\mu\) and period \(\lambda\), then
verify response equality for at least \(4\lambda+2\mu\) subsequent indices.
Include Boolean-relation, cyclic-group, transformation-semigroup, and
non-group controls.

### E3 — constructive composite witness

After the candidate and \((\mu,\lambda)\) are frozen, a separate evaluator
may choose an accepted prime \(p\ge\mu\).  It must verify that

\[
        p(1+\lambda)\equiv p\pmod\lambda
\]

has the same response and is composite.

### E4 — exact recurrence certificate

For deterministic rational matrices of dimensions \(1\le d\le8\), compute
\(\chi_A\), both responses through at least \(4d+16\), and every
Cayley–Hamilton residual exactly.  Compare exact rational generating
functions and report minimal recurrence order.

### E5 — nilpotent memorizer controls

For \(N\in\{32,64,128,256\}\), realize both bilinear and trace forms for:

- prime indicator;
- square indicator;
- powers of two;
- Fibonacci membership;
- fixed seeded pseudorandom bits;
- fixed hash-derived bits;
- arbitrary signed rational values.

Assert exact agreement through \(N\) and exact zero thereafter.  Record
dimension, parameter count, and target-vector SHA-256.  Every output is
labeled oracle-containing memorizer control.

### E6 — same-object block traces

On small exact graph cutoffs:

- build the \(q\in\{1,2\}\) block adjacency;
- enumerate closed walks through period \(32\);
- isolate \(C_k\);
- verify its trace factor
  \(\operatorname{tr}(A^{k-1}B)\);
- compare exact power traces and finite block determinant coefficients.

### E7 — trace-class diagnostics

At

\[
 \sigma\in\{0.45,0.49,0.50,0.51,0.60,1.00\},
\]

record exact or interval-certified partial nuclear sums, separated into
successor and return families.  Include \(A=0\), \(B=0\), and both-nonzero
controls.  No finite plot may establish the exact threshold.

### E8 — countable-wrapper controls

For primes, squares, powers of two, an ultimately periodic set, and a seeded
total predicate:

- verify transient computation and cemetery edges lie on no closed walk;
- compare full and recurrent-pruned power traces;
- close matched computations recurrently with
  acceptance-independent padding;
- verify the maximum-edge lower bound
  \(n^{-\sigma/\ell(n)}\);
- compare \(z^{\ell(n)}\) before inducing with \(z\) after inducing.

### E9 — roof and marker mismatch

For \(2\le k\le4096\), verify the integer monomial identity

\[
        \prod_{(n,d)\in C_k}nd=M_k^2
\]

and compare \(z^kM_k^{-2s}\) to \(zk^{-s}\).  Prime filtering occurs only
in the post-freeze evaluator.

### E10 — determinism and integrity

Two clean runs must be byte-identical.  The report must include:

- frozen parameters;
- environment lock;
- source-oracle certificate;
- test summary;
- artifact SHA-256 inventory;
- explicit candidate/evaluator separation;
- Route-A YAML with two-stage provenance pending until external evaluation.

## 6. PASS/FAIL rule

The preregistration passes only if every exact identity succeeds, the
no-oracle scan is clean, both runs agree byte-for-byte, and every digest
verifies.  Numerical plots cannot override an exact failure.  Any changed
cutoff, matrix family, target family, or predicate creates a new provenance
record rather than silently modifying this protocol.

An implementation failure does not invalidate a proved theorem until the
mathematical assumptions and the implementation are reconciled.  A
successful implementation does not replace proof.

## 7. Stop conditions

Stop the ordered finite-fiber branch once:

- finite semigroup responses are proved eventually periodic;
- fixed-dimensional exact supports are controlled by SML;
- growing finite memory fits arbitrary data;
- the licensed Paper19/Paper20 wrappers are shown selector-tautological or
  clock-diluted;
- a separately assumed one-dimensional oracle deletion control is shown to
  retain factorial roofs and \(z^p\).

Every mathematical stop condition fires.

## 8. Frozen route tuple

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

Route B is locked.  No zero search, review loop, or Route-B construction is
authorized after this verdict.
