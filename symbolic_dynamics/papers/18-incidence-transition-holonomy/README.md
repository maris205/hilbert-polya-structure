# Paper 18 — Transition Holonomy on the Tensor-Subset Shift

Candidate **SD-C20** tests the last immediate local loophole left by the
one-letter cocycle obstruction: let a finite-group cocycle depend on the
transition \((S,T)\) through subset incidence.

The loophole is dynamically genuine.  For \(G=S_3\), assign \(r=(12)\) to
strict refinements, \(t=(23)\) to strict coarsenings, and the identity
otherwise.  The resulting skew product has a commuting fiber action and
noncommutative periodic holonomy.  On two atoms, both one-dimensional
character blocks remain clean,

\[
D_{\mathbf1}=D_{\mathrm{sgn}}=(1-x)(1-y),
\]

while the standard block leaks exactly:

\[
D_{\mathrm{std}}
=(1-x)^2(1-y)^2
+3xy(x+y)(xy+1)(x+y-1).
\]

The first trace-log differences are \(-3\) at \(x^2y\) and \(xy^2\);
the selected \(p^2q^2\) coefficient is \(-6\) at \(x^2y^2\).  The full
total-degree-four ledger also has coefficients \(-3\) at \(x^3y\) and
\(xy^3\).  The primitive cycle \([p,pq,q,pq]\) carries a nontrivial
commutator and has edge-separated standard-character gap \(3\).  Its marked
gap is distinct from the unmarked aggregate
\([x^3y^3]\Delta\log D=-9\).

## Main decision

~~~text
GO_GENUINE_TRANSITION_HOLONOMY
GO_SAME_OBJECT_ARTIN_BLOCKS
GO_TRIVIAL_EULER_FACTOR
GO_TRACE_CLASS_RE_GT_2

STOP_NONABELIAN_CLEAN_FACTOR
STOP_DETERMINANT_IMPLIES_COHOMOLOGY
STOP_ONE_DIMENSIONAL_CHARACTER_AUDIT
STOP_ROBUST_NO_LEAK
STOP_ARITHMETIC_SELECTIVITY
PROVES_TOO_MUCH

(A0_ANALYTIC_ARITHMETIC_ORIGIN,
 A1_WEAK,
 A2_ANALYTIC_DETERMINANT,
 A3_FAIL,
 A4_FAIL)

ROUTE_A_REJECTED
ROUTE_B_LOCKED
~~~

The candidate succeeds as Symbolic Dynamics: it gives an honest same-object
Artin decomposition and a trace-class nontrivial block on
\(\operatorname{Re}s>2\).  It fails as an arithmetic selector because the
incidence rule is unchanged under prime, composite, random, shuffled, or
formal atom inventories.

## Claim boundary

Exhaustive two-atom searches over \(S_3,D_4,Q_8\) found that every
all-irrep-clean table lies in the natural counting gauge class.  This is
finite exact evidence, not a theorem for all groups or inventories.  Known
equal-zeta and gain-cospectral constructions also prohibit treating
character determinants as complete cohomology invariants.

## Reading map

- Paper: [main.pdf](main.pdf)
- Frozen object: [SOURCE_LOCK.md](SOURCE_LOCK.md)
- Preregistered claims: [PREREGISTRATION.md](PREREGISTRATION.md)
- Proofs: [PROOF_PACKAGE.md](PROOF_PACKAGE.md)
- Algebra and operator derivations: [DERIVATION_PACKAGE.md](DERIVATION_PACKAGE.md)
- Primary-source and novelty boundary: [LITERATURE_AUDIT.md](LITERATURE_AUDIT.md)
- Research story: [NARRATIVE_REPORT.md](NARRATIVE_REPORT.md)
- Manuscript plan: [PAPER_PLAN.md](PAPER_PLAN.md)
- Figure specification: [FIGURE_SPEC.md](FIGURE_SPEC.md)
- Cross-family clues only: [ROUND2_CLUES.md](ROUND2_CLUES.md)
- Build verification: [COMPILATION_REPORT.md](COMPILATION_REPORT.md)

## Next in-family move

The complete subset grammar is too universal.  A next-batch candidate should
change the allowed symbolic language itself, using a constrained
factorization, renewal, or countable Markov grammar, and should pass an
arbitrary-inventory separation test before any analytic continuation program
is attempted.
