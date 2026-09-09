# C427 — A semilinear atlas for integral Vieta recurrence cycles

Status: `FINAL_BUILD_COMPLETE_PENDING_SEAL` (2026-09-09).
The [final PDF](main.pdf) has 13 pages and is selected from the second of
two fresh, byte-identical final builds. See the authoritative
[final build report](FINAL_BUILD_REPORT.md); the earlier
[build ledger](BUILD_LEDGER.md) preserves the initial history. This is
not yet a sealed release or a formal Route-A evaluation.
The first actual nonauthor pass found zero must-fix items; its optional
absolute-value clarification was adopted and actually rebuilt. See
[PAPER_IMPROVEMENT_LOG.md](PAPER_IMPROVEMENT_LOG.md). The second actual
nonauthor pass passed with O1 closed and no new findings; no further
source edit or artificial revision build was needed.

For all n>=3 and integer a, the paper gives a terminating construction
of the full ordinary integral periodic set of
`F(x1,...,xn)=(x2,...,xn,x2...xn+a-x1)` as finitely many integer linear
sets with unrestricted nonnegative parameters and exact native
least-period labels. Nonzero directions give every unbounded channel;
the remaining finite set is uniform in the invariant level. The new
core is the n>=4 mixed nonzero-block rigidity. The n=3 input is the
explicitly credited computer-assisted C421 theorem, not a new result.

## Manuscript and proof coverage

| Manuscript location | Coverage |
| --- | --- |
| `sections/01_statement.tex` | Exact object, inverse, invariant, domain, main contract, ownership table and why bounded periods alone do not imply semilinearity. |
| `sections/02_blocks.tex` | Internal maxima and all maximal nonzero-block lengths, both signs and all zero mixtures; the new finite-linearization step. |
| `sections/03_classical.tex` | Self-contained coarse integral-period divisor, including the 2-adic near-identity argument; constructive integer-cone generators and inequalities/projections. These are classical inputs. |
| `sections/04_atlas.tex` | Every actual product-tag case, necessity/sufficiency, all least-period exclusions, free parametrization, unbounded channels, finite level-independent remainder and termination. |
| `sections/05_completion.tex` | Precise inherited n=3 input, finite-level counts, ordinary source zeta, example and limits. |
| `sections/appendix_height.tex` | Full previously completed V4-H height proof, including Q=0, ±1, ±2, large Q and degenerate fixed-endpoint directions. |

The nine TeX inputs (including `main.tex`, `math_commands.tex` and
abstract) and one bibliography input are pinned in
[INPUT_MANIFEST.sha256](INPUT_MANIFEST.sha256). The source snapshots
at each real initial build are retained as `builds/initial_*/source.tar`.
No compulsory central new proof is left only in a Markdown supplement.

## Sources and evidence boundary

[SOURCE_AUDIT.md](SOURCE_AUDIT.md) records primary versions actually
accessed and the literature deductions. The complete admitted
[R6 proof](../../continuation_round6/nonlinear_geometry/PROOF_PACKAGE.md)
and [nonauthor research review](../../continuation_round6/NG2V_REVIEW/REVIEW.md)
are the prewriting provenance, not manuscript-review substitutes.
[PAPER_PLAN.md](PAPER_PLAN.md) records the approved writing/table plan.

The only computational theorem dependency is the explicitly imported
[local C421 package](../../../research_c419_c423/papers/C421_integral_return/README.md).
No old certificate or exploratory program was rerun. The atlas and
per-level finite-box enumeration are proved terminating algorithms;
no claim is made that all instances, or a large test instance, were run.

This is a source-system classification. Ordinary counts and source
zeta factors do not supply target Euler factors, root numbers,
automorphy, a spectral zero correspondence or a Hilbert–Pólya model.
No global priority, journal acceptance, human peer review, named
authorship, funding or conflict-of-interest declaration is inferred.

The two manuscript passes and final fresh identical-input build pair
are complete. The remaining owned operations are batch evaluation
adjudication, release verification and authorized Git integration.
