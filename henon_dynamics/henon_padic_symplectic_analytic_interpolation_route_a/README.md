# C394: nonlinear p-adic symplectic interpolation

This complete source theorem identifies every nonzero orbit closure of the double shear on Z_p squared with a scaled p-adic adding-one system. One exact displacement identity also determines every finite prime-power residue period and fixed count. Joint analytic interpolation yields the finite/all alternative for algebraic hitting times; source Haar, reversal and operator boundaries are retained.

- [Final paper](paper/main.pdf) and [complete proof](proof/ANALYTIC_PROOF.md).
- [Claims](CLAIMS.md), [source audit](SOURCE_AUDIT.md), and [limitations](LIMITATIONS.md).
- [Exact evidence](results/c394_interpolation_evidence.json), [actual receipts](results/TEST_REPORT.md), and [reproduction commands](REPRODUCIBILITY.md).
- [Three-round improvement record](PAPER_IMPROVEMENT_LOG.md), [failure-mode audit](review/FAILURE_MODE_AUDIT.md), and [release manifest](C394_RELEASE_MANIFEST.json).

The source arithmetic is intrinsic but local. Strict tuple: `(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`. All target flags are false, and Route B remains disabled. `NO_BAD_EULER_OR_ROOT_NUMBER`.

Baseline `697518b6db90458f86f7916fbf397b8ad5ef2372`, obstruction `HEN-O378`, fixed epoch `1788566400`. A manifest link is not a completion assertion by itself: the actual write and nonwrite receipts govern release status.
