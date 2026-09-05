# P202 B actual new build and every-page inspection

Root executed the pinned review_cold_build.sh with frozen_round1 as source,
main_round1.pdf as comparison target, and this review's new qa directory.
The helper created an empty temporary directory and copied only main.tex
and references.bib; it then actually ran pdfLaTeX -recorder, BibTeX,
pdfLaTeX, pdfLaTeX, with SOURCE_DATE_EPOCH1704067200, FORCE_SOURCE_DATE1,
LC_ALL=C and TZ=UTC. It moved the successful build to qa/cold_build only
after byte comparison. This is a new review build, not one of the two
future terminal builds. No old auxiliary, bbl or PDF was an input.

Every command and final cmp exited0. The resulting four-page PDF is exactly
e1ca5021ff1ac74cff118d0d571fa0f3f74db32cc8b6ba5e7cd557fb69d88f8a,
the accepted Round1 PDF. Final TeX/BibTeX logs have no Warning, Undefined,
Overfull, Underfull or Error matches; initial unresolved-citation warnings
before BibTeX are preserved in the first-pass log, not a final defect.

Actual Poppler results:4 unrotated A4 pages,312997bytes,PDF1.5; unencrypted,
no JavaScript/forms/custom metadata/metadata stream. Title/author/subject/
keywords/creator/producer are blank. All25 font rows are Type1 and have
embedded/subset/Unicode=yes. Extracted text has no unresolved references
and all five cited bibliography entries appear. Raw metadata/fonts/text
are saved. The ARS structural preflight was actually run; its sidecar
reports UNAVAILABLE because pypdf is absent, not PASS. Poppler and visual
checks are independent evidence and do not relabel that missing check.

The root actually opened all four120-dpi rendered images:

| Page | Viewed evidence |
|---|---|
| 1 | Anonymous title/abstract, exact update, source limitations and complete inverse theorem; odd maximizing words legible and within margins. |
| 2 | Inverse proof, run domain, three surplus equations and full finite-clearance proof; no clipped indices or negative-case formula. |
| 3 | A/B definitions, recurrence/height theorem, three sharp-witness words, matrices and count corollary; normal proof continuation at page foot. |
| 4 | Count-proof conclusion, verification provenance, explicit HOLD_EXTERNAL and all five references; no blank extra page or lost bibliography. |

No overlapping text, clipped display, missing symbol or requested layout
repair was found. This is short-amsart project QA, not PDF/A, tagged-PDF
accessibility, conference formatting or external blind-submission approval.
