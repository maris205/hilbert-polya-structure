# Final QA report — P122–P126

**Checkpoint:** 2026-08-30 UTC.  
**Result:** **5/5 PASS INTERNAL; FINAL FREEZE; EXTERNAL HOLD**.

| paper | pages | bytes | exact control | independent gate | fonts | visual pages |
|---:|---:|---:|---:|---|---:|---:|
| P122 | 4 | 293,934 | 1,637,027 | `GO_INTERNAL` | 24/24 | 4/4 |
| P123 | 4 | 281,582 | 203,244 | `GO_INTERNAL` | 20/20 | 4/4 |
| P124 | 5 | 293,617 | 1,735,656 | `GO_INTERNAL` | 23/23 | 5/5 |
| P125 | 5 | 367,999 | 27,405,887 | `GO_INTERNAL` | 26/26 | 5/5 |
| P126 | 4 | 319,631 | 8,756,710 | `GO_INTERNAL` | 24/24 | 4/4 |
| **total** | **22** | **1,556,763** | **39,738,524** | **5/5** | **117/117** | **22/22** |

## Control and build replay

After all hostile-review repairs, every canonical verifier was run in a fresh
Python process with bytecode disabled and compared byte for byte with its
stored transcript.  All comparisons passed.  P124's two independent verifier
lanes contribute 1,469,669 and 265,987 assertions to its combined total.

Each manuscript passed an isolated four-stage LaTeX/BibTeX build.  Final
log/BLG audits found zero emitted warnings, undefined citations or references,
overfull/underfull boxes, fatal errors, or actionable rerun requests.  The
isolated outputs reproduce the frozen PDFs byte for byte.

## Bibliography, PDF, text, and visual gates

The paper-local bibliography closures are 6/6, 8/8, 9/9, 6/6, and 9/9, for
**38/38 cited and resolved entries**.  All PDFs are A4, unencrypted, rotation
zero, date-free, JavaScript-free, form-free, and carry an empty PDF Author
metadata field.

All **117/117** reported font rows are embedded, subsetted, and Unicode-mapped.
A fresh `pdftotext -layout` extraction over the five final PDFs contains
**90,692 bytes** in **1,242 lines**.  Placeholder, unresolved-reference,
verification-marker, and stale-status scans are clean.

All **22/22** final pages were rendered and inspected page by page.  Titles,
abstracts, theorem statements, proofs, tables, equations, owner boundaries,
conclusions, and references are legible.  There is no clipping, overlap,
unexpected blank page, missing glyph, malformed display, or rotation.

## Integrity gate

The five paper-local `SHA256SUMS` files cover **100 frozen evidence files** and
pass entry by entry.  Their own SHA-256 values are:

| paper | manifest entries | `SHA256SUMS` SHA-256 |
|---:|---:|---|
| P122 | 21 | `eb12b24d150a5657a0244caff460ee068b3d710a009691aa263a4747c5ec9d3e` |
| P123 | 19 | `fb99df3eb03f23e710cd97f0730b6e73aea4302d5dbf621629f398407ed001f5` |
| P124 | 21 | `cf52615a6e286314f087cc4787295fd5e421d07953759d62f254d00518911be2` |
| P125 | 19 | `50bd8c71726fb8cf70d3ac29f994b084fe5652fea462d6397b350b70c80c0a1e` |
| P126 | 20 | `1402e0a34198f04b7f9624372dd3f2e45912d3f3464bdd5809a72a5b60d65a25` |

The five canonical PDF digests are frozen in
`CANONICAL_PDF_MANIFEST.sha256`, which passes 5/5.  Its SHA-256 is
`ff4da20f7e59fffc56a73c0781d335ce780ebe4b93c5a9a6f58aa970b8fe4c31`.

This report certifies internal theorem-package consistency, reproducibility,
and artifact mechanics only.  External release and owner clearance remain
**HOLD**.
