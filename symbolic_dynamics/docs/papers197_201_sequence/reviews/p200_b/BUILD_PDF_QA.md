# P200 Review B: source-only cold build and four-page visual audit

2026-09-05 UTC. PASS for this review surface; not the batch terminal QA.
The paper-compile skill was applied in a fresh review-owned directory,
without cleaning or changing any author/frozen files. The batch helper
was read completely before use. No venue submission was attempted.

Executed once for this review:

```sh
bash docs/papers197_201_sequence/qa/review_cold_build.sh \
 /root/autodl-tmp/symbolic_dynamics/papers/200-lex-first-alternating-switch/frozen_round1 \
 /root/autodl-tmp/symbolic_dynamics/papers/200-lex-first-alternating-switch/main_round1.pdf \
 /root/autodl-tmp/symbolic_dynamics/docs/papers197_201_sequence/reviews/p200_b
```

The helper created a new temporary directory under this review directory,
copied only `main.tex` and `references.bib`, and ran pdflatex, BibTeX and
two more pdflatex passes with deterministic date/environment settings.
It compared the resulting PDF with `main_round1.pdf` byte-for-byte before
moving the retained build into `cold_build/`. The process exited0.
It did not use an inherited auxiliary file, bibliography output or PDF.

Cold PDF and frozen PDF SHA256:
`7226b56257356fe3869a957983e0c92a7dbc79470f3e504f0f031c4b6248b3ea`.
PDF properties:4 A4 pages,290,689bytes, unencrypted, no JavaScript, blank
author/title/creator/producer metadata. All21 listed font records are
embedded, subsetted and Unicode-mapped. The final TeX/BibTeX logs contain
no warning, undefined reference/citation, overfull/underfull box or error
matches. The review retains recorder output and all four pass transcripts.

The reviewer extracted the complete four-page text and actually opened
all four120dpi renderings through the image viewer, not only page counts:

| Page | Visually checked surface | Result |
|---|---|---|
|1| Anonymous heading, abstract, literal matrices, equation1, ownership citations and row-support notation | readable, no clipping or unresolved reference |
|2| Pivot proof, recurrent iff, equation2, tail theorem and counting inequality through the page break | readable, no missing symbols or clipped proof |
|3| Wide witness/itinerary, width caveat, inverse formula, strict sentinel inequalities and complete inverse proof | full-width equations fit; all indices legible |
|4| Maximum/equality theorem,16-state exception, finite table, explicit narrow-box caveat, external hold and three references | readable, clean end matter and URLs |

No visual repair was required. There are no absent figures to resolve:
this is a four-page theorem note with one table and displayed equations.
The preserved `visual/page-1.png` through `page-4.png` and cold-build files
are covered by `QA_SHA256SUMS`. This one actual Review-B cold build is
not falsely reported as two physical cold builds or as terminal approval.
