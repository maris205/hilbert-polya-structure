# PREREGISTRATION — SD-C21

**Freeze date:** 2026-08-14
**Project:** `19-stationary-semiring-sieve-shift`
**Primary system family:** Symbolic Dynamics
**Review protocol:** authority manuscript, no review round by instruction

## Research question

Can a stationary one-sided countable Markov graph, built only from the
alphabet-sum, tensor product, order, and entropy of finite full shifts,
compute primality locally and realize the exact Euler product on one
trace-class weighted adjacency?  If it can, does the arithmetic computation
remain visible in recurrent orbit data, and does the mechanism distinguish
the integer semiring from generic effective atom inventories?

## Frozen positive claims

### C1 — local quotient-search correctness

The expanded (Q_{n,d,q}) program reaches (A_n) if and only if (n) is
prime.  It uses no existential divisor edge and no prime table.

### C2 — whole-operator trace class

For every (\operatorname{Re}s>1), the rank-one edge series defining (L_s)
converges absolutely in trace norm and is holomorphic with values in
\(\mathcal S_1\).

### C3 — exact primitive/repetition ledger

The only primitive cycles are the self-loops (\gamma_p=[A_p]).  For every
(r\ge1),

\[
\operatorname{Tr}L_s^r=\sum_p p^{-rs}.
\]

### C4 — same-object Fredholm--Euler identity

For (\operatorname{Re}s>1) and every (z\in\mathbb C),

\[
\det(I-zL_s)=\prod_p(1-zp^{-s}),
\]

so (\det(I-L_s)=1/\zeta(s)) on the absolute-convergence half-plane.

## Frozen obstruction claims

### C5 — pruning equivalence

Every computation and cemetery edge is absent from every closed walk.
Pruning them preserves all power traces and the Fredholm determinant.  The
recurrent core is the direct sum of prime loops.

### C6 — positive exact-ledger pruning theorem

For nonzero positive formal edge weights and an exact one-primitive-per-atom
ledger with no other primitive classes, every recurrent SCC is a simple
cycle.  Computation outside those cycles is trace-invisible.  A contracted
cycle must retain (z^\ell) if the full graph-step marker is compared.

### C7 — universal total-decider wrapper

Every total decidable support (S\subseteq\{2,3,\ldots\}) admits the same
trace-class construction with

\[
\det(I-zL_{S,s})=\prod_{n\in S}(1-zn^{-s}).
\]

Runtime growth is immaterial because the time-index roof is bounded by a
convergent double Dirichlet series.

### C8 — factorial-monoid compiler

Every effective factorial monoid with a terminating atom verifier and
summable norm admits the analogous Euler-product compiler.  In particular,
for monic polynomials over (\mathbb F_q), the determinant at (z=1) is
(1-q^{1-s}).

## Frozen finite evidence

- independent support equality at cutoffs 32, 64, 128, 256, and 512;
- sealed no-oracle certificate over 1,651 explicit quotient-search
  nodes/edges, with zero forbidden factor identifiers or calls;
- 296 nodes and 282 edges at cutoff 24, with 287 transient nodes;
- recurrent vertices exactly (A_p) for (p\le24);
- exact rational traces for (r=1,\ldots,12);
- independent dense rational determinant at cutoff 8;
- relabeling transport exact under seed 19021;
- bounded-depth and shifted-factor controls fail prime support;
- (\mathbb F_2[t]) irreducible counts and Euler coefficients exact through
  degree 8;
- squares, powers of two, Fibonacci, and a deterministic hash predicate all
  reproduce the wrapper determinant.

Finite evidence certifies code paths only.  C1--C8 are proved independently.

## Refutation and stop rules

- A prime missed or composite accepted by the expanded graph refutes C1.
- A divergent rank-one edge majorant for some (\operatorname{Re}s>1)
  refutes C2.
- Any closed walk outside an accepted loop refutes C3 and C5.
- Any mismatch in the exact finite determinant refutes the implementation,
  not automatically the infinite theorem.
- A positive exact-ledger SCC with genuine branching and no extra primitive
  class refutes C6.
- A total-decider support for which the frozen time roof is not trace class
  refutes C7.
- A control inventory that the symbolic mechanism intrinsically excludes
  would weaken `PROVES_TOO_MUCH` and reopen arithmetic selectivity.

## Frozen anti-claims

- No categorical-coproduct claim for (\boxplus).
- No factor-existence oracle hidden in an edge.
- No Ruelle-operator or equilibrium-state claim.
- No assertion that the primality proof is logically circular.
- No assertion that primes emerge from recurrent interaction.
- No claim of topological conjugacy after pruning or cycle contraction.
- No universal pruning theorem for signed, complex, supertrace, or
  cancellation-based grammars.
- No continuation, Gamma factor, functional equation, trivial-zero
  treatment, Riemann--von Mangoldt law, Weil criterion, self-adjoint lift, or
  RH conclusion.

## Verdict

~~~text
(A0_STRUCTURAL_ARITHMETIC_RELATION,
 A1_PASS_ANALYTIC,
 A2_ANALYTIC_DETERMINANT,
 A3_FAIL,
 A4_FAIL)

ROUTE_A_REJECTED
ROUTE_B_LOCKED
SELECTOR_TAUTOLOGICAL
PRUNING_EQUIVALENT
PROVES_TOO_MUCH
~~~
