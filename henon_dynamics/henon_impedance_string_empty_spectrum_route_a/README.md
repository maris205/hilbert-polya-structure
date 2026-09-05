# C396 — Impedance string: empty spectrum and finite extinction

Complete source theorem and reproducibility package, 2026-09-05.
Baseline: `697518b6db90458f86f7916fbf397b8ad5ef2372`.
Obstruction: HEN-O380. Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.

The full infinite-dimensional wave generator is unitarily unfolded in the
physical energy norm. All nontransparent spectral points and the exact
all-time norm are known. At transparent impedance the generator has empty
spectrum, but the semigroup has norm one until the sharp time (2L/c).
Its exact pseudospectra, Hilbert–Schmidt/nontrace boundary and trivial det2
are proved, rather than inferred from finite matrices.

- [Complete proof](proof/ANALYTIC_PROOF.md)
- [Final paper](paper/main.pdf), [original](paper/main_round0_original.pdf),
  [first revision](paper/main_round1.pdf), [second revision](paper/main_round2.pdf)
- [Evidence](results/c396_evidence.json) and [actual test report](results/TEST_REPORT.md)
- [Strict evaluation](evaluations/route_a/HCS-C396/2026-09-05.yaml)
- [Source ownership](SOURCE_AUDIT.md) and [internal review](CROSS_REVIEW.md)

Strict tuple: `A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_FORMAL_HINT`.
Overall: `ROUTE_A_REJECTED`; all nine target/Route-B flags and separate
Route-B invocation authorization are literal false.
This is package-level progress on a new source mechanism, not new ownership
of the classical Driscoll–Trefethen formulas or a target spectral success.
