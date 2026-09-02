# P163 build and verification record

**Artifact:** `papers/163-complemented-shadow-dynamics`  
**Status:** `ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL`  
**Gate inherited:** `GREEN_REENTRY_AFTER_CONTRACT_STRENGTHENING`

## Independent exact replay

The paper-local verifier is a standard-library implementation of the literal
two-level set-family map.  It imports neither the original scout nor the
re-entry-gate verifier.

```text
command: python3 code/verify.py
assertions: 1,430,898
status: PASS
row digest: 357f4687d13f71739a3faaa3fa119b9ac4ffb090363851499c6d979b2489a5e4
canonical SHA-256: 21d2dc8e66580e7b78ef9c4bd2bda3eaa393757ee466497a62defb0f15700434
fresh byte-identical replays: 2/2
```

The exact checks comprise atomic kernels and depth histograms through `n=9`;
all phase states, mixed-rank clocks, recurrent and fixed states, iterated
images, every-target image criteria, and inverse fibres through `n=4`; the
complete `n=2` boundary split; and symbolic central-slice and period-product
controls through `n=12`.  These finite computations provide counterexample
pressure only; the all-parameter claims are proved in the manuscript.

## Settled source build

Toolchain: pdfTeX `3.141592653-2.6-1.40.22` and BibTeX `0.99d`.

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The settled logs are retained as `build_pdflatex_1.log`,
`build_bibtex.log`, `build_pdflatex_2.log`, and
`build_pdflatex_3.log`.  The final pass has zero LaTeX/package warnings,
undefined references or citations, rerun requests, overfull boxes, underfull
boxes, and fatal errors.  All 6 bibliography entries resolve.

Two final source-only builds were made in separate fresh temporary
directories containing only `main.tex` and `references.bib`.  Both completed
the full four-command sequence and were byte-identical to the retained
`main.pdf` (`2/2`).

## Final PDF QA

```text
pages: 5
bytes: 424,998
page box: A4, 595.276 x 841.89 pt
PDF SHA-256: 899e7c6b24f3a6e99041d05410db75c1de152f4d98b2e90d10e4619927b216bf
font rows: 32
unembedded/unsubsetted/non-Unicode font rows: 0
encrypted: no
forms: none
JavaScript: no
```

The title, author, subject, and keyword metadata fields are blank.  Extracted
text contains no email address, local path, personal handle, affiliation, or
institutional identity.  The byline and running heads are anonymous, and the
visible external-status statement says `HOLD_EXTERNAL`.

All five final pages were rendered at 140 dpi and inspected.  Equations,
theorem blocks, running heads, footers, declarations, and references are
inside the page box; no clipping, collision, overflow, or illegible element
was observed.

## Frozen artifact hashes

```text
bb18ae1fbe2f9b7994efc3bdbe69917783e5e5e2acc539bbc8dcb37fbbb79e8f  main.tex
27ed70f7cb91a31fc14a6976ed022e9308da457fa3f7739af4a38bc830deb430  references.bib
363142fbf99bd3060114aaf12d47f024eed42ab5477fa876b0659d138096d36f  PAPER_PLAN.md
520f116e10363f07af32e2079d029373ca10c2a336ac7220eabb3f651dcbae54  CLAIMS_EVIDENCE.md
4be90bb3b7ce4d2eb1660c6984174626a9aefb4655a1b9edb22b2fed0fead95b  NARRATIVE_REPORT.md
c2fa5adf6ccd663fa26665b0398b5c704efa5abb01cf88386591611da0ed136f  README.md
4fa3924a12221c26e83da202a9a63ccb6c074c74dc3b90fe8859b837cc52437d  code/verify.py
21d2dc8e66580e7b78ef9c4bd2bda3eaa393757ee466497a62defb0f15700434  code/CANONICAL.txt
899e7c6b24f3a6e99041d05410db75c1de152f4d98b2e90d10e4619927b216bf  main.pdf
```

## Review freezes

Hostile Review A returned `0 Critical / 0 Major / 0 minor`; no artifact
change was requested and `main_round1.pdf` was frozen byte-identically.

Hostile Review B independently rederived the literal dynamics, atomic
Johnson-ball iterates, mixed-rank clock, recurrent support and period
products, central-slice extremality, the `n=2` exception, and the every-target
cover formula.  It returned `0 Critical / 0 Major / 0 minor` after:

```text
independent assertions: 1,041,401
verifier SHA-256: 7c098c5ab552fb2d136716ec7947f57d55ed23612f0bd46bdbb404d846f441fc
canonical SHA-256: 9242436ce116ba2664a1a8ab6e5caa13f1ea82d5a08c0886e88b4f142a86eb80
fresh byte-identical replays: 2/2
cold builds matching current PDF: 2/2
```

No source or PDF repair was requested.  `main.pdf`,
`main_round0_original.pdf`, `main_round1.pdf`, and `main_round2.pdf` are
byte-identical five-page files at SHA-256
`899e7c6b24f3a6e99041d05410db75c1de152f4d98b2e90d10e4619927b216bf`.
The settled warning/error count is zero; 32/32 fonts pass; all five pages,
blank identifying metadata, anonymity, and the visible `HOLD_EXTERNAL`
sentinel pass.  Git synchronization remains a batch-level action.
