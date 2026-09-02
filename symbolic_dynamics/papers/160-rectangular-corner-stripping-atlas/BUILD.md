# Build and Round-2 artifact record — P160 RCS

**Date:** 2026-09-02 UTC  
**Status:** `ANONYMOUS ROUND-2 / INTERNAL ACCEPT / HOLD_EXTERNAL`

## Toolchain and settled sequence

- pdfTeX 1.40.22 / LaTeX2e 2021-11-15.
- Anonymous `amsart`, 10 pt, A4, 27 mm margins.
- Latin Modern; microtype protrusion on, expansion off.

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Round-1 logs are `build_round1_pdflatex_1.log`,
`build_round1_bibtex.log`, `build_round1_pdflatex_2.log`, and
`build_round1_pdflatex_3.log`. The final settled log and `.blg` contain zero
real warning, error, undefined citation/reference, rerun request, overfull
box, or underfull box. Initial-pass undefined-citation messages are expected
before BibTeX and are not present in the settled pass.

## Round-1 artifact

| Check | Value |
|---|---|
| Round-1 canonical / freeze | then-current `main.pdf` / `main_round1.pdf` |
| Historical byte comparison | identical at the Round-1 freeze |
| Pages / format | 4 / A4 (`595.276 × 841.89 pt`) |
| Size | 294,530 bytes |
| SHA-256 | `3bbbb6f3243171d612f86a17cd88b58f56bc5ec80c3533dc30464343931def03` |
| References | 5/5 cited and resolved |
| Encryption / forms / JavaScript | none / none / none |
| Identifying metadata | title, author, subject, and keywords blank |

`main_round0_original.pdf` remains unchanged at 295,886 bytes with SHA-256
`2be90261ae3b636aa8db684597896f7e7d549363879936b3f6539877577f7d08`.

## Round-1 cold and visual QA

Two independent temporary directories received only `main.tex` and
`references.bib`; each completed the settled sequence and produced SHA-256
`3bbbb6f...ef03`, byte-identical to `main_round1.pdf`. Their settled logs are retained
as `build_round1_cold1_settled.log` and `build_round1_cold2_settled.log`.

At 144 dpi all four pages were inspected: no clipping, overlap, broken glyph,
crowded table cell, or illegible equation/reference was found. `pdffonts`
reports 22 rows, all embedded, subsetted, and Unicode mapped. `pdftotext`
shows only the anonymous byline and no identity, editorial marker, local path,
email, or affiliation.

## Review-B acceptance and Round-2 artifact

Review B returned `ACCEPT — 0 Critical / 0 Major / 0 Minor`. Its independent
11,287,366-assertion verifier produced byte-identical outputs with SHA-256
`b6034231aa620d0de80a56bfcda69f8ddfe047e343498896426699252b918b8a`.
No Review-B finding required a source change. Round 2 adds only the visible
`HOLD_EXTERNAL` lifecycle sentence identified by batch final QA; this is not
a mathematical change or a Review-B repair.

Round-2 retained build logs are `build_round2_pdflatex_1.log`,
`build_round2_bibtex.log`, `build_round2_pdflatex_2.log`, and
`build_round2_pdflatex_3.log`.

| Check | Value |
|---|---|
| Current / Round-2 PDFs | `main.pdf` / `main_round2.pdf` |
| Byte comparison | identical |
| Pages / format | 4 / A4 (`595.276 × 841.89 pt`) |
| Size | 316,629 bytes |
| SHA-256 | `ce59fbfca3f50ee917089175817885fc5630b807483b7a16a5d291c69292e352` |
| Round-1 preserved | 294,530 bytes / `3bbbb6f3243171d612f86a17cd88b58f56bc5ec80c3533dc30464343931def03` |
| Round-0 preserved | 295,886 bytes / `2be90261ae3b636aa8db684597896f7e7d549363879936b3f6539877577f7d08` |

The Round-2 settled log contains zero real warning, error, undefined
citation/reference, rerun request, overfull box, or underfull box. Two fresh
source-only builds match `main.pdf` byte for byte; their settled logs are
`build_round2_cold1_settled.log` and `build_round2_cold2_settled.log`.

All four pages were rendered at 144 dpi and inspected. The lifecycle sentence
is visible and legible on page 4, with no collision or bad break. `pdffonts`
reports 23 rows, all embedded, subsetted, and Unicode mapped. Metadata fields
remain blank; the byline is anonymous; no identity/editorial marker is present.

The pre-existing `SHA256SUMS` is the Round-0 manifest and is intentionally not
regenerated here. `FINAL_QA.md` is intentionally not created by this author
freeze.
