# Paper improvement log — HCS-C126

No external reviewer, reviewer score, venue prediction, literature novelty
judgment, or independent human assessment is claimed.  The following are two
internal evidence-led revision passes.

## Round 0 — theorem draft

The baseline connected Chebyshev composition to \(3^n\) base fixed points and
derived the unique fiber coordinate and rational Artin–Mazur zeta.  It did not
yet fully separate root-family overlap, root simplicity, and least-period
preservation, and it reported stability only at the fixed-point level.

## Round 1 — proof closure

- made both cosine root families and their exact \(\{\pm1\}\) intersection
  explicit;
- added endpoint and interior derivative calculations, turning a degree count
  into a distinct-real-root theorem;
- added the least-period preservation argument using uniqueness of the fiber
  lift;
- derived positive/negative orientation counts and the odd-divisor inversion
  formula for primitive negative-orientation orbits;
- promoted the tangent statement from a prefix to an all-period triangular
  derivative and repetition theorem.

The round-1 PDF is preserved as a release snapshot of the final reconciled
source; this log records the substantive proof changes without retaining an
obsolete claim boundary in a binary artifact.

## Round 2 — falsification and scope repair

- strengthened the unit-fiber control from a denominator warning to the exact
  fixed-line/no-closure dichotomy;
- factored the non-Chebyshev second fixed polynomial, showing five distinct
  roots, triple roots at \(\pm1/2\), and a neutral two-cycle;
- added a dedicated “Progress over prior gate” statement distinguishing this
  all-period result from another finite orbit prefix;
- stated that the unweighted Artin–Mazur zeta is not a weighted target-facing
  Fredholm determinant;
- reconciled all paper, evidence, test, and evaluation language to
  `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` and
  `route_b_invocation_allowed: false`;
- added deterministic-build, font, warning, replay, and hostile-mutation release
  checks.

The round-2 and final PDFs are also release snapshots of the same final source,
so every preserved binary carries the corrected theorem and route boundary.
