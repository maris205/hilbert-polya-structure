# Paper Improvement Log

## Round 0

- Preserved the pre-review manuscript as `paper_round0_original.pdf` and the
  integrity-gated version as `paper_pre_review.pdf`.
- Independent round-1 review: **5/10, weak reject / major revision**.
- Core theorem, branchwise exact-symplectic proposition, and rank-one
  corollary were judged correct as stated.

## Round 1 revisions

1. Added Lemma `Sole periodic boundary identification` and a direct
   all-period proof from the endpoint dynamics
   `0 -> 1 -> -d -> d -> d` and the restricted adjacency on labels `{1,2}`.
   The period-20 parent audit is now explicitly only an implementation check.
2. Retitled and repositioned the manuscript as an audited specialist note.
   The text makes no priority claim for finite-span containment, higher-block
   recoding, locally constant weights, generalized bakers, or boundary-zeta
   machinery.
3. Added and verified theorem-focused references: Lind--Marcus (2021),
   Parry--Pollicott (1990), and Marcus--Tuncel (1991).
4. Corrected the abstract to say exact symplecticity holds on branch interiors.
5. Compressed the main certification section and moved the evidence table and
   detailed controls to the reproducibility appendix.
6. Subordinated internal route labels to an ordinary mathematical conclusion.
7. Recompiled with `pdflatex -> bibtex -> pdflatex -> pdflatex` because
   `latexmk` is unavailable in the environment.  The 16-page PDF has zero
   undefined citations/references, zero overfull boxes, and embedded fonts.

Round-1 artifact: `paper_round1.pdf`.

## Round 2 revisions

1. Replaced the implicit generating-partition assumption in Lemma 3 with an
   explicit nested-cylinder proof.  The frozen quadratic is nonflat and has
   negative Schwarzian derivative; its critical point and both core endpoints
   land on the repelling fixed point (d), whose multiplier is bounded below
   by (5244381/3125000>1).  Singer's basin theorem, the
   no-wandering-interval theorem, and the homterval lemma then exclude every
   nontrivial itinerary fibre.  Unique off-boundary coding also proves least-
   period preservation before the existing sole-endpoint calculation is
   applied.
2. Added and claim-audited de Melo--van Strien (1993), including the exact
   theorem scope used by the proof; the bibliography now contains 17 audited
   entries.
3. Removed the two visible dangling-hyphen breaks and corrected the
   Bowen--Lanford suffix parsing.
4. Moved the computational audit figure to the reproducibility appendix and
   fixed it in source order; the orbit-lattice figure is now fixed after the
   boundary proof rather than floating into the proof.
5. Recompiled with `pdflatex -> bibtex -> pdflatex -> pdflatex`.  The resulting
   17-page PDF has no undefined citations/references, no overfull or underfull
   box warnings, and all fonts are embedded.

Round-2 artifact: `paper_round2.pdf`, SHA-256
`3cc1f56d8bc82ff3776b7b6578fcd689aaa0c1d2e4a532397fad66b4774655b7`.

## Final polish and independent review

1. The final independent technical review returned **PASS_WITH_MINORS,
   7.5/10**, and confirmed that the generating-partition, homterval,
   least-period, and sole-boundary-ghost arguments close the previous major
   issue at all periods.
2. Applied both non-blocking review suggestions: each finite named cylinder is
   now explicitly identified as a compact interval obtained along monotone
   inverse branches, and the de Melo--van Strien citation points to
   Chapter II, Lemma 3.1 and Theorems 6.1--6.2.
3. Recompiled with `pdflatex -> bibtex -> pdflatex -> pdflatex`, reran all 89
   tests, and rechecked all 25 frozen research artifacts in `REPORT.sha256`.

Final artifact: `paper_final.pdf`, SHA-256
`d94bc574bd7128b777c075569234e76c76c3d2e13694b0c8239220f0aebb69bf`.
