# C184 test report

## Exact executable checks

- Producer: PASS — 5 levels, 103 lineage rows, 542 exact characteristic
  coefficient cells, and 537 finite graph eigenvalue cells.
- Independent checker: PASS — 3,041 assertions; no producer import.
- SymPy reconstruction: PASS — 33,177 checks and four direct graph
  characteristic polynomials.
- Canonical replay: PASS — 117,576 exact evidence bytes.
- Mutation suite: PASS — 70 repaired-hash semantic rejections and one
  stale-hash rejection.

## Coverage and independence

The checker reconstructs pre-gasket edges by iterated IFS copies rather than
the producer's triangle subdivision.  It separately rebuilds every lineage,
coefficient, multiplicity, determinant exponent, source lock, Route-A gate,
scope flag, citation, integrity mode, and nonclaim.  Exact graph determinants
use fraction-free Bareiss elimination, and low-level characteristic
polynomials are tested at integer arguments.  Floating eigenvalue comparison
through level five is an independent regression control with tolerance
\(10^{-10}\), not the all-level proof.

The SymPy path directly forms graph matrices and characteristic polynomials
through level four, reconstructs the recurrence through level five, checks
exact inverse branches and exceptional cancellation, proves determinant
exponent recurrences through level twenty, and verifies dimension closure
through level thirty.

Finite checks do not prove the all-level theorem.  The local elimination,
singular-kernel multiplicities, dimension induction, and polynomial proof
are carried in `THEOREM_PACKAGE.md` and `paper/main.tex`.
