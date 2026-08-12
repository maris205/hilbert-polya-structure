# Analytic-v3 Round-1 independent review

Date: 2026-08-06

The configured external Codex-MCP reviewer was unavailable.  Three
independent read-only subagents were therefore used as the documented
fallback.  No external-model score is reported or inferred.

## Review panel and pre-revision verdicts

| Audit | Verdict | Central finding |
|---|---|---|
| Strict ground-state rearrangement | Minor revision | The theorem and proof were sound; the form-domain closure, positivity statement, equality deficits, and the precise Brothers--Ziemer exceptional set needed to be explicit. |
| Relative heat derivation | Accept with minor revision | Every prefactor, Brownian covariance, sign, exact carrier, and uniform remainder checked; Figure 3 panel (b) needed cancellation-free evaluation. |
| Whole-paper claim and editorial drift | Revise | No reject-level mathematical or Hilbert--P\'olya problem, but the hero ledger, duplicated Sections 5/8, conclusion scope, self-citation provenance, and project metadata had drifted. |

## Mathematical revisions implemented

- Closed the rearranged form-domain step explicitly.
- Stated positivity improvement on connected \(\mathbb R^2\), simplicity of
  the bottom eigenvalue, and analytic elliptic regularity precisely.
- Displayed the kinetic and potential rearrangement deficits separately and
  verified the exact Brothers--Ziemer exceptional set has measure zero.
- Kept the strict theorem at its proved scope:
  \(a>-1\), \(a\ne0\), fixed \(\hbar>0\), one centered warp, and zero field.
- Deleted the unused all-time heat-trace ordering.  The BLL paper now supports
  only finite multiple-integral context, so no unsupported Trotter
  trace-norm passage remains.
- Defined Euler's constant and standardized the auxiliary operator notation
  \(\mathsf H_{a,\hbar}\).

## Stable heat-figure revision

Panel (b) no longer subtracts two floating-point quantities of order
\(L^2\) to recover an order-\(t^2\) residual.  It evaluates the exact
cancellation-free lower-tail identity

\[
 \frac{\mathcal B_a(t)-P_a(L)}{t^2}
 =-4\pi^2\int_0^1u e^{-2\pi t u}
 \left[(\log u)^2+4\pi r_a^2\log u\right]\,du.
\]

The final two archived values are \(11.2847201103\) at
\(t=3\times10^{-5}\) and \(11.2855341130\) at \(t=10^{-5}\), converging
to the independently derived limit \(11.2859411384\).

## Whole-paper revisions implemented

- Split the hero ledger into \(S_{\mathrm{op}}\) proved and
  \(S_{\mathrm{dyn}}\) sampled.
- Ended Section 5 after the antiunitary audit and placed the unique
  authoritative relative-spectrum container and prime-power boundary in
  Section 8.
- Restated the complete relative heat formula in the conclusion and restored
  all restrictions, including \(a>-1\) and fixed \(B\ne0\) for the reflected
  conjugation obstruction.
- Separated the published low-dimensional-chaos context from the
  H\'enon-specific \(a=1.02\) provenance.
- Added a public locator for the prior H\'enon preprint.  Round-2 file-level
  verification then showed that the related Zenodo record contains a
  different 21-page expansion; the final citation therefore uses the exact
  17-page PDF at a fixed Git commit, whose hash matches the local archive.
- Corrected the BibTeX parsing of Charles B. Morrey, Jr.
- Replaced ambiguous “exact Riemann mean” wording by an exact classical
  comparator carrying the two growing Riemann--von Mangoldt terms.
- Added the corresponding-author email already verified in the author's
  earlier manuscript sources; no address was invented.

## Round-1 regression

- PDF snapshot: `paper7_analytic_v3_round1.pdf`
- Pages: 45
- Bibliography: 77 database entries; 67 printed entries
- Tests: 58 passed
- Undefined citations/references: 0
- Overfull boxes: 0

The revised manuscript was then sent to the same three independent reviewers
for a focused Round-2 closure audit.
