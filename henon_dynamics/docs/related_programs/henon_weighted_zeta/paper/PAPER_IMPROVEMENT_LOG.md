# Paper Improvement Log

## Outcome

The two-round paper-improvement loop is complete.  The final manuscript is
`main_round2.pdf`, byte-identical to `main.pdf`.  No frozen R059--R061 protocol
or persisted numerical result was modified or rerun during the writing loop.

## Score progression

| Review stage | Theory | Narrative / presentation | Verdict |
|---|---:|---:|---|
| Baseline review before Round-1 fixes | 6.0/10 | 6.5/10 | Almost / not yet submission-ready |
| Review of `main_round1.pdf` | 8.0/10 | 8.0/10 | Minor revision; accept after targeted fixes |
| Final after Round-2 fixes | not re-scored | not re-scored | All mandatory Round-2 items closed; public archive still pending |

The final row deliberately does not invent a third score: the configured loop
has two review rounds.  The Round-2 reviewers scored the Round-1 PDF, after
which their targeted minor revisions were implemented and independently
checked.

## Review records

- [Round-1 theory review](ROUND1_THEORY_REVIEW_RAW.md), SHA-256
  `b5be36080e0c7f1a6703c61674f91519e4d94def05579c3656f45019fb173177`.
- [Round-1 narrative review](ROUND1_NARRATIVE_REVIEW_RAW.md), SHA-256
  `ef397c18feac4a694f8b8831e9e1c32f2f3be91d0f1e0a3b24282931a3d0551b`.
- [Round-2 theory review](ROUND2_THEORY_REVIEW_RAW.md), SHA-256
  `9e2f59b6ff5c8e7b586e38a05aa88ab3f430c8d5eacc7b5a99c0f86607f95a34`.
- [Round-2 narrative review](ROUND2_NARRATIVE_REVIEW_RAW.md), SHA-256
  `6f70728618cd7e7f36d0d8936734378c1707aee7be2e0577880907359fdc04cb`.

## Round-1 fixes

The combined Round-1 reviews identified one central critical issue and a set
of major/minor presentation and scope issues.  The revision:

1. Defined the Euler and periodic-point flat determinants, their two cutoff
   conventions, the trace recurrence, and their formal factor dependence.
2. Recast the Euler/flat root agreement as a dependent finite-section and
   implementation check rather than independent evidence.
3. Replaced technical `h-set` language by state rectangles, added explicit
   local maximality, mixing, and a hyperbolic-basic-set corollary.
4. Defined the ideal finite-volume matrix and the restriction/extension
   operators, including dimensions and source/target conventions.
5. Replaced smoothing language by the frozen absolute dyadic-contrast rule.
6. Stated that the tail lemma does not control the reported determinant root.
7. Limited ARPACK claims to returned Ritz pairs and retained the absence of a
   rigorous spectral-radius enclosure.
8. Recast the localization result as a failed mechanism metric degenerating
   to occupancy, with conditioned negative diagnostics retained.
9. Added full seed-level summaries, paired differences, closest-work
   positioning, and six publication-quality vector figures.
10. Cleaned the bibliography to 37 cited entries, including Wang (2026), and
    retained Liang Wang's HUST affiliation.

## Round-2 fixes

The Round-2 theory and narrative reviews agreed on five overlapping mandatory
items.  All five were implemented:

1. Defined the actual ARPACK residual
   `||P_m^T v_j - lambda_j v_j||_2` with normalized vectors, and stated its
   nonnormal-matrix limitations.  The 22.8%--29.2% separation is explicitly
   only among returned eigenvalues.
2. Added the complete frozen gap rule and its pooled median
   `0.0057803 = 0.5780%`, plus the complete dyadic aggregate rule.  Only 2/4
   groups pass, so the dyadic component and overall G1 fail.
3. Distinguished physical fine-to-coarse projection from coarse-to-fine
   diagnostic reading in tables, captions, figures, discussion, and appendix.
4. Displayed the exact weighted cell-exposure formula, its inside-target
   denominator, zero-denominator convention, and inherited parent-cloud
   origin; the occupancy degeneration is now immediate from the formula.
5. Clarified units and statistical levels, defined rowwise Spearman
   correlations and 16-seed means, and separated the six cycle/matrix records
   from the eight direct/common-cloud group medians in the conclusion.

The recommended fixes were also implemented: `D_F` is identified as a formal
power series; finite-section roots receive no factorization-derived error
bound; the primitive-count formula and period-1--12 vector are displayed;
substochasticity is qualified by the recorded `1e-12` tolerance; the explicit
interior bound `sqrt(17)/12 <= |q_i| <= sqrt(3/8)` is shown; fine-cell index
blocks are defined; figure labels use parent grids; and exact manifest paths
are supplied.  The abstract now distinguishes closed exact rectangles from
strict open numerical interiors and reports the formal overall G1 failure.

## PDFs and hashes

| Artifact | Pages | SHA-256 |
|---|---:|---|
| `main_round0_original.pdf` | 22 | `b8b87270f8a3b23d135e237e4b3b936f8600f9b170dd5313a81c8a6cec57485e` |
| `main_round1.pdf` | 26 | `07dd4d59b790ce8e6f2dd1018c7787fe26d5b2a04af23d8d34782af7aad98fc8` |
| `main_round2.pdf` | 26 | `a4e4770fce02ebf906378b7e2f90465d016c7a2b15734238154cafe8508a9f42` |
| `main.pdf` | 26 | `a4e4770fce02ebf906378b7e2f90465d016c7a2b15734238154cafe8508a9f42` |

The synchronized manuscript source/figure tree hash is
`7ae28295f59497e0770e7ae6619032f4923e11813d888bb42a0c0fcd1cb18ab5`,
computed from sorted SHA-256 records for `main.tex`, `math_commands.tex`,
`references.bib`, section TeX files, the figure generator, and included PDF
figures.

## Final QA

- Manual `pdflatex -> bibtex -> pdflatex -> pdflatex -> pdflatex` build: pass.
- Final `main.log`: zero undefined citations/references, zero package/LaTeX
  warnings, and zero overfull/underfull boxes.
- Citation audit: 37 unique cited keys, 37 bibliography entries, zero missing,
  zero uncited, zero duplicate keys/titles/DOIs.
- Test suite: `120 passed in 17.29s`.
- PDF: 26 pages; every reported font object is embedded and subset.
- Visual inspection: title/abstract, new theory equations, finite-volume and
  ARPACK definitions, operator tables/figures, discussion, references, and
  supplementary gate ledger all pass.
- Author and metadata: Liang Wang; School of Artificial Intelligence and
  Automation, Huazhong University of Science and Technology, Wuhan 430074,
  P.R. China.
- Wang (2026): cited with title, journal, volume/issue, year, and DOI
  `10.1080/27684830.2026.2684334`.

## Remaining submission item

A public archival URL and immutable release identifier do not yet exist.  The
paper states this limitation explicitly and contains no invented placeholder.
They should be added before public submission.
