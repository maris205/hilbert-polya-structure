# C423 first manuscript-review response and actual revision

2026-09-08 UTC. The coordinator read the entire 335-line
[first nonauthor manuscript review](../../manuscript_reviews/round1/C423_REVIEW.md),
SHA-256 59809633d137276f3d55cf8d920ce1608f35bc6bd84c5f9b6eac01afc78dd9a2.
It is PASS with zero mandatory corrections. Both optional suggestions
were adopted as precision improvements, not reclassified as mathematical
errors or as an artificial increase in a numerical score.

O1: the abstract now states locally that the two nonzero differences
are excluded in the nonconstant case. Its constant-pair alternative
remains intact. O2: the relative algebraic closure sentence now explains
that any root over it is algebraic over K by transitivity, so it is
indeed an algebraic closure. No hypothesis or proof conclusion changed.

Only sections/0_abstract.tex and sections/4_classification.tex changed.
Their current SHA-256 values are respectively:

    2686b4e620bf1f555f4e86454ce3368403a3bd3ff113841d57707c6b086f3b3a
    6cc16c60e7c0b3f41c8ff12585d34089e6c3141876fd98808d2939b418f4d155

All ten pre-revision source files were preserved in
snapshots/author_polished/ before these edits. All ten new inputs
are copied in snapshots/round1/. The original first baseline in
snapshots/baseline/ and both earlier actual PDFs are retained.

[The new PDF](builds/round1/main.pdf) has six pages and 317422 bytes,
SHA-256 36c2088ca4d794087a698413431d55e7d7e00ed1d2c4b1e3a5cfa5b9f8814e98.
One actual fresh-directory latexmk invocation exited 0:

    env SOURCE_DATE_EPOCH=1788825600 FORCE_SOURCE_DATE=1 TZ=UTC LC_ALL=C latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=builds/round1 main.tex

Its normal three pdflatex and two BibTeX passes resolved early references.
Final main.log/main.blg have no Warning/Overfull/Underfull/undefined/error
match; rg exited 1 for no matches. No old mathematical program,
source query, paid model, Git write or release action occurred.

This records a genuine first review-driven revision. Second full-text
review, affected/current-page visual checking and final deterministic
build/release gates remain; no review of an old proof is substituted
for the second manuscript review. Current review input is the new
builds/round1/main.pdf, not either earlier baseline.
