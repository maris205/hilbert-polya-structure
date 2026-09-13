# Paper Configuration

- Candidate/lifecycle: `henon_period3_residue_proof_note_v1`.
- Title: *Period-Three Trace Residues and a Minimal Separator on an
  Exceptional Quartic H\'enon Fiber*.
- Format: anonymous 11 pt, single-column specialist mathematics note.
- Evidence mode: theorem proof only; registered evidence is not used.
- Date: 2026-08-16 UTC pre-review production freeze.
- Terminal author-side state:
  `READY_FOR_FRESH_INDEPENDENT_MANUSCRIPT_REVIEW`.
- Independent manuscript review has not occurred; finalization and submission
  are not authorized; `paper_final.pdf` has not been created.

## Source and publication identities

- Manuscript source: `paper/manuscript.tex`, 1,419 lines, SHA-256
  `de706b358a6b1fdec47da2ab88704ab8011ed22a1dd7de560b8912d0c845a617`.
- Shared commands: `paper/math_commands.tex`, 37 lines, SHA-256
  `40a7fe009279e803be822ad2a3fcae56793b2b5c098e0876800e51d1b4f24510`.
- Bibliography: `paper/references.bib`, SHA-256
  `f1b6fe0807e33debf87c8be19e1b81b2a4a10f886fd9f4ae1d20bf264e978adc`.
- Workspace PDF: `paper/manuscript.pdf`, SHA-256
  `bb3cd34efbff6ec3c2bc2803b0c68b30b701d79833d5a9b4eebeb68d101da949`.
- Review PDF: `paper/paper_pre_review.pdf`, SHA-256
  `bb3cd34efbff6ec3c2bc2803b0c68b30b701d79833d5a9b4eebeb68d101da949`;
  it is byte-identical to `paper/manuscript.pdf`.
- Build-artifact hashes: LOG
  `59ba77a6c79c066ef00435790911d415e6b28e487cb4e012e850faaf3bde0988`,
  BLG
  `be7f60aae83be2fe4e5cc3d0d2898fcd73661df5e2333ae4173dc63bb971ad61`,
  BBL
  `ac0ae8c4f0de3188e42f6f0b17775eb1cf90468431b048986ba23caa12dd522a`,
  AUX
  `67a5988dcf5b5359a7933f077ca2a7f92b39f82f5ceb7b8dd23200a935da3824`,
  and OUT
  `7b918498371e32fa96c359d8d5fbdf195fa62091df38d36b9b6df9882a9593d1`.

## R0 draft and bounded integration history

The independently reviewed R0 proof-only draft remains identified by
`paper/manuscript.tex` SHA-256
`f3c535739046e61378ec8896b70e6d30652a7654213894e1556d221e511d3022`
and `paper/math_commands.tex` SHA-256
`40a7fe009279e803be822ad2a3fcae56793b2b5c098e0876800e51d1b4f24510`.
Round-2 asset review binds that exact R0 manuscript. After `ASSET_PASS`, the
sole manuscript author made only the authorized ten-key citation migration,
inserted the three frozen figure blocks verbatim, added the graphics package,
and made layout-only fixes: local single-column float routing, permissive top
float fractions, a display break for four branch choices and two provenance
hashes, and an unnumbered environment for the visibly tagged recurrence
`(R)` to eliminate a duplicate PDF destination. No theorem, formula, caption,
bibliographic entry, or frozen asset was changed.

## Build and QA configuration

- Engine: pdfTeX 3.141592653-2.6-1.40.22 (TeX Live 2022/dev/Debian).
- Bibliography engine: BibTeX 0.99d.
- `latexmk` was unavailable; the equivalent explicit clean sequence was
  `pdflatex -> bibtex -> pdflatex -> pdflatex`.
- Deterministic environment: `SOURCE_DATE_EPOCH=1786838400`,
  `FORCE_SOURCE_DATE=1`, `TZ=UTC`, and `LC_ALL=C`.
- Two disposable clean trees independently produced byte-identical PDF, LOG,
  BLG, BBL, AUX, and OUT artifacts.
- Terminal build warnings: zero LaTeX, package, pdfTeX, BibTeX, citation,
  reference, duplicate-destination, overfull-box, and underfull-box warnings.
- Length: 19 pages including references. Figures 1--3 occur on pages 3, 7,
  and 9; the conclusion and references share page 19. The main text remains
  within the frozen 21.5-page specialist-note planning budget.
- Cross-references: 91 unique labels, 43 referenced targets, zero missing or
  duplicate target.
- Bibliography closure: exactly 11 distinct canonical entries; exactly 10
  cited keys; optional `BianchiHe2026` is the sole unused entry.
- PDF QA: 38 font rows, all embedded, subset, and Unicode-mapped; Type-3
  fonts 0; raster image objects 0; all three incorporated PDFs remain vector.
- Visual QA: all three original frozen figures and all 19 integrated pages
  were inspected at original/full-page resolution. No clipping, overlap,
  missing glyph, unreadable figure text, or misplaced float was found.
- PDF title, subject, keywords, and author metadata are blank; the visible
  author line is `Anonymous`.

## Frozen upstream bindings

- Proof-only lock:
  `2c7f056b7f9566f754a06c30417105c0b1cefb2d0081f4bca8bb3a00adbf8eeb`.
- Independent proof-only handoff:
  `407cec5bf295c29330c24ae461dca86ad1bf54d77f44d477d83a821bf7e41711`
  (`PROOF_ONLY_HANDOFF_PASS`).
- Paper plan:
  `e4876a50d172ccfb857b3c6667a0be85d12105f4d7da63da393531a36cef9d31`.
- Citation contract:
  `997ca84ee7d868f34cacc783993f10d1b82b86c71fbdc1c9b80f38bcf5199bfd`.
- Figure manifest:
  `3adc970996ea7a6e1dc043a554c88b8007f4fe203aa30a522b0a4663dcb31096`.
- Repaired asset tree:
  `a5006ef63be3bcc585567276f05f063fd6786c6170081e0eea8ec0ca128598ee`.
- Immutable Round-1 asset review:
  `d6bc5c624d371752f06ff1d8a8ae27367a7b4c2370b4ab2f19b52cbe24d95ed6`.
- Independent Round-2 asset review:
  `7b633dd001f1ae086863826612a15d74325406f1eaf2b95fc49e49eddd7ae404`
  (`ASSET_PASS`).

## Release boundary

This is an author-side production configuration, not a manuscript-review
verdict. Any change to a bound source, bibliography, figure block, or PDF
invalidates the downstream pre-review records. The package must now stop for
a fresh independent manuscript review.
