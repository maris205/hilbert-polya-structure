# HCS-C54 compilation report

Status: **PASS; DOCS_FINAL_NO_MORE_EDITS against RELEASE_CANDIDATE evidence**

## Build

- Engine: pdflatex through latexmk 4.76.
- Command:
  `latexmk -C && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`.
- Exit status: zero.
- PDF: `paper/main.pdf`.
- Total pages: 14 A4 pages.
- Main manuscript through Declarations reaches page 12.
- Appendices begin on page 12; references begin on page 14.
- File size: 454270 bytes.
- PDF SHA-256:
  `34a0de185f16c93746ade889db2921f362906a2859b3d9786f65009224fa88b5`.
- Captured build transcript SHA-256:
  `1b5af11bdc10232574acfd0d8cca1fc04d654ad232cf532c3e61b360da3cbace`.
- Final LaTeX log SHA-256:
  `8a30cb020e28c1c9c26740f509c9df87d6f4d5967aa0d97b82173640578bab9d`.

No venue page limit is asserted; the project uses its single-column
mathematical-article format.

## Automated checks

- Undefined citations: 0.
- Undefined cross-references: 0.
- LaTeX/package warnings after the final stabilized pass: 0.
- Overfull boxes: 0.
- Underfull boxes: 0.
- Rerun requests: 0.
- Stale section files: 0; every file in `paper/sections/` is input by
  `main.tex`.
- Source graph: 52 unique labels, 36 resolved references, 14 resolved
  citation uses, and seven bibliography keys, all cited.
- Text extraction: PASS, 34801 bytes.
- Residual `TODO`, `FIXME`, `XXX`, or `VERIFY` markers in extracted PDF: 0.
- Literal `??` or `[?]` placeholders in extracted PDF: 0.

## Release-candidate evidence lock

- Payload SHA-256:
  `f068d5e11ea8e6245e04bd3a30e77140267f835c4e07412ce2009c7fb04ceae1`.
- Certificate SHA-256:
  `780cc9f249e836d3fa5b51a00fd2cdb9af0eac595d929cd1be4d728df1921846`.
- Independent-check SHA-256:
  `160b3a9d11354b41404642a3dd22d6e43f2ce576126acb21eb0133e552fc0c0a`.
- Schema SHA-256:
  `4cee6c2252d5743ca3c5fee40ec98fbc945223312d2196fb63a43730281deedf`.
- Code/results-manifest SHA-256:
  `62f67e6d4929496974020febab3bc0e2cff45ed153b0cef51937031863d866ba`.
- Immutable replay: 36/36 semantic checks and 93/93 unit tests pass,
  including all targeted hostile mutations and the exhaustive rebound sweep
  of 198 semantic leaves.
- Certificate inventory: 1,078 scalar leaves, comprising 198 semantic, 876
  exact-derived, and four allowlisted history leaves.
- Manifest scope: the persistent `results/CODE_RESULTS_HASHES.sha256` lists
  exactly seven release code files and four release result files.  It excludes
  both manifest files and contains no manuscript or project-root file.

The 44-entry full-project inventory includes the persistent scoped manifest.
The implementation commit deliberately remains a later provenance stage; it
is not represented by the displayed scoped manifest and is not a theorem
input.

## PDF checks

- All 26 fonts are embedded, subsetted, and Unicode-mapped.
- No Type 3 font occurs.
- PDF version: 1.5; the file is unencrypted and has A4 page geometry.
- Pages 1, 11, 12, and 14 were independently rasterized and visually inspected
  after the clean build.  The title and abstract, mathematical display, RC
  verification table, scoped-manifest explanation, all five evidence hashes,
  declarations, appendix ending, and references are legible, unclipped, and
  contained within the text block.
- Each of the five release-candidate hashes extracts exactly once from the
  PDF text.

## Scope checks visible in the paper

- “Full” means the full projective monomial stabilizer of the homogeneous
  ideal, not the full projective linear automorphism group.
- The equation and rational-group-form theorems are unconditional for every
  `n >= 2`; smooth packet data are inherited only in rows 2, 3, and 4, and
  no semisimplicity theorem is inherited.
- The complete split-local exponent is ordinarily realizable exactly when
  `n` divides 4.  “Ordinary” is project shorthand for an actual finite-rank
  compatible realization with integral multiplicities, not p-adic or
  Newton-polygon ordinarity.
- The third-row common-group character is first a theorem over `K`; a common
  rational group scheme requires the twisted Fermat rational form.
- Split-invisible virtual classes restrict to zero over `K` and cannot alter
  restricted rank or isotypic multiplicities.
- No inert or global root, all-row smoothness or packet theorem, automorphy,
  analytic continuation, functional equation, or RH statement is claimed.

This is the final paper-source/PDF/report freeze against the persistent scoped
code/results release candidate and its 44-entry full-project inventory.  The
later implementation-commit provenance backfill must not reopen or alter the
paper, the PDF, or this compilation report.
