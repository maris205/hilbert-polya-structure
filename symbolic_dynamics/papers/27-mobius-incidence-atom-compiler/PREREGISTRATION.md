# Preregistration — Paper27 / SD-C29

## Decision question

Can the fixed integer-divisibility symbolic grammar compile a
necklace-resolved atom-loop selector without receiving a prime inventory, and
does the resulting incidence geometry yield anything beyond a disguised
coordinate atom table?

## Frozen hypotheses

### H1 — source-derived atom selector

The cover predicate of \(1\), followed by
\(q_n=\zeta\varepsilon_n\mu\), selects exactly the monochromatic temporal
repetitions of divisibility atoms, with coefficient one at every repetition
and zero on every mixed or composite-letter word.

### H2 — marker-correct analytic realization

On an explicit weighted Hilbert space, the atom idempotents are uniformly
trace-norm bounded and the transfer

\[
T_\eta(s,u)=\sum_{p\in\operatorname{At}(P)}
u^{\ell(p)}p^{-s}q_p
\]

is holomorphic and trace class whenever
\(\sum_p|u|^{\ell(p)}p^{-\operatorname{Re}s}<\infty\). Its \(r\)-th trace
must contain \(u^{r\ell(p)}p^{-rs}\).

### H3 — projector-equivalence no-go

Every finite complete primitive lift with the same source labels is
unitriangularly conjugate to the coordinate projector family. For
\(\eta>1\), the canonical countable incidence family is boundedly similar to
the coordinate family. Therefore ordinary cyclic traces and Fredholm
determinants cannot see the oblique incidence geometry.

### H4 — honest holomorphic coupling

After tensoring with the Paper25 de Rham sector, both degrees are individually
trace class on one common proved domain and the stated Euler product is their
graded determinant ratio, not the ordinary determinant of an ungraded direct
sum.

### H5 — route stop

At \(u=1\), trace class fails at and left of
\(\operatorname{Re}s=1\). Without a same-object continuation or spectral
carrier, A3 and A4 fail and Route A remains rejected.

## Required exact checks

The independently owned exact suite must derive atoms as covers rather than
read a prime table and must check:

1. exact zeta/Möbius inversion and every kernel entry;
2. all orthogonality, idempotence, completeness, rank, and trace identities;
3. restriction stability and deterministic relabeling;
4. all words and cyclic classes through frozen finite cutoffs;
5. composite-letter rejection and repetition marker exponents;
6. exact power traces and finite determinants;
7. separate even and odd determinants and their exact graded ratio;
8. the trace-log numerical residual only as a non-gating sanity check.

The suite must include the mutated-source, scalar-Möbius,
zeta-without-inverse, no-cover-filter, relabeling, and cutoff controls.

## Predeclared pass/fail logic

~~~text
A0_ANALYTIC_ARITHMETIC_ORIGIN
  PASS iff atomhood, arithmetic weight, code, and duration derive from the
  frozen source without a prime table or target spectrum.

A1_PASS_ANALYTIC
  PASS iff an infinite theorem selects only source-atom primitive loops at
  every repetition, with coefficient one and the exact digit marker.

A2_ANALYTIC_DETERMINANT
  PASS iff both holomorphic degrees have honest Fredholm determinants on one
  proved trace-class domain and their graded ratio has the claimed product.

A3_FAIL
  remains FAIL unless the same operator family receives a justified
  continuation or canonical regularization across the u=1 boundary.

A4_FAIL
  remains FAIL unless a source-specific critical-line spectral mechanism is
  proved without target-zero input.
~~~

The frozen decision is:

~~~text
(A0_ANALYTIC_ARITHMETIC_ORIGIN,
 A1_PASS_ANALYTIC,
 A2_ANALYTIC_DETERMINANT,
 A3_FAIL,
 A4_FAIL)

ROUTE_A_REJECTED
ROUTE_B_LOCKED
~~~

## Falsifiers and stop rules

- A surviving mixed word, composite-letter loop, or wrong repetition marker
  falsifies H1.
- Use of a supplied prime mask or prime-only coordinate table invalidates A0.
- Failure of finite conjugacy or of the stated bounded similarity invalidates
  the collapse theorem at that scope.
- Treating the scalar Möbius function as an idempotent coefficient invalidates
  the construction.
- Calling the graded ratio an ordinary ungraded determinant invalidates A2.
- Using a scalar continuation of \(1/\zeta\) as continuation of the trace-class
  family invalidates A3.
- Any target-zero comparison or Route B repair is forbidden.
- If the construction reduces to coordinate atom blocks, record
  STOP_INCIDENCE_SIMILARITY_COLLAPSE; this is a theorem outcome, not an
  experimental failure.

## Frozen interpretation

A successful H1 is a genuine project advance because atomhood is compiled
from the factorization grammar before cyclic trace. A successful H3 is
simultaneously a no-go: the compiler derives *which* coordinates are atoms
but creates no new semisimple orbit observable after that derivation.

The manuscript-review loop is explicitly skipped. Proof, source, formula,
citation, compilation, and visual audits are not skipped.
