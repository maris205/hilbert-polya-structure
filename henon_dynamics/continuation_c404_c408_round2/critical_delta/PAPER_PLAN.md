# C406 paper plan

Title: The critical second Weyl coefficient of a harmonic delta chain.

One question: determine and stabilize the second high-energy counting
coefficient when point couplings on harmonic cells have a finite nonzero
asymptotic ratio to the cell index. This is one focused spectral-asymptotics
paper, with moderate specialized significance, not a new general theory.

Status: admitted after complete proof and source review, including
`../wild_dynamics/CROSS_REVIEW_CRITICAL_DELTA.md` section 9. The unchanged
proof and source hashes are recorded there. No numerical experiment is
required by the proof; no invented validation panel or plot is requested.

## Complete claim and evidence

For `x_n=pi H_n`, positive fixed couplings `b_n` with `n b_n ->infinity`,
and the closed form on zero-left-trace `H^1`, let `N_b(k^2)` be inclusive.
If `b_n/n -> kappa in (0,infinity)`, then

    N_b(k^2)=k log k+C(kappa)k+o(k).

The per-cell IDS has cell length pi and one coupling kappa. Its
regularized integral defines `C`, continuous strictly decreasing with
range `(2 gamma-1,infinity)`. The hard limit has the Dirichlet second
coefficient. The soft regime asserts only divergence of the centered
coefficient, with the separate compactness hypothesis retained.

Main new lemma: the critical local-periodic reduction with cumulative
`o(k)` error. It combines a head of growing length, geometric blocks
with band edges, and an excluded spectral tail. A bounded error per
cell is insufficient. The finite-chain Floquet bound and telescoping
block estimate must be proved inside the PDF, not summarized as
standard semiclassics.

## Proposed reverse outline

0. Abstract: critical two-term law, explicit coefficient, full asymptotic
   class and precise endpoint scope. No target-zero or priority claim.
1. Introduction and theorem: credit the classical harmonic-chain model,
   source form theory and periodic comparison; distinguish C400's fixed
   constant coupling from the present `b_n~kappa n` balance. State all
   quantifiers, positivity assumptions and real-k inclusive convention.
2. Form and cuts: dense closed form, quantitative sampled tail estimate,
   local compactness and finite-codimension min--max comparison. No
   finite-rank claim for infinitely many cuts.
3. Periodic cell and finite chain: normalized free phase integral, band
   bottom, transfer half-trace, exceptional phase argument, ring
   decomposition and uniform finite-chain error at all thresholds.
4. Critical reduction: choose tail cutoff, head size and geometric
   block ratio; show the exact coordinate-change Rayleigh inequalities;
   bound the total freezing error by weighted summation by parts.
5. The second coefficient: justified Riemann limit near zero, harmonic
   sum, convergence of the integral, strict monotonicity and endpoint
   limits. Do not assume smooth IDS at band edges.
6. General couplings and boundaries: rate-free min--max squeeze with
   finite exceptional vertices; correct form-domain inclusions for
   hard and soft regimes; no general soft leading-order law.
7. Scope and reproducibility: source theorem only; no spectral-zeta
   continuation from an o(k) remainder, no target divisor and no HP
   realization. Brief actual internal-review/AI disclosure.

## Writing and citation constraints

Plain article with anonymous author block, complete mathematical text,
no ML venue/page/experiment quota. One compact regime table is useful
only if it keeps the soft limitation explicit. No decorative figures.
Use verified source metadata from SOURCE_AUDIT.md. S4's section 5,
Theorem 11 locator is **arXiv v1**, not the reorganized journal number.
The later thesis check is an ownership audit, not a theorem input that
requires adding a long literature survey. Credit S1--S4 concisely.

Freeze the initial TeX/Bib and PDF with an actual build receipt before
non-author manuscript review. Root coordinates final changes, two fresh
deterministic builds, all-page visual QA, exact payload sealing and Git.
Do not edit the reviewed proof/source/review files to relabel them as a
new version; their initial candidate status is historical and superseded
by the global admission decision.
