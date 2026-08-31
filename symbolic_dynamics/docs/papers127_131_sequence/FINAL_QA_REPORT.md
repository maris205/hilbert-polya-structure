# Final QA report — P127–P131

**Checkpoint:** 2026-08-31 UTC.  
**Result:** **5/5 PASS INTERNAL; FINAL FREEZE; EXTERNAL HOLD**.

| paper | pages | bytes | exact control | independent gate | fonts | visual pages |
|---:|---:|---:|---:|---|---:|---:|
| P127 | 3 | 328,070 | 1,271,047 | `GO_INTERNAL` | 26/26 | 3/3 |
| P128 | 4 | 386,639 | 180,453 | `GO_INTERNAL` | 28/28 | 4/4 |
| P129 | 6 | 342,879 | 506,663 | `GO_INTERNAL` | 25/25 | 6/6 |
| P130 | 4 | 346,056 | 735,609 | `GO_INTERNAL` | 25/25 | 4/4 |
| P131 | 4 | 314,641 | 6,101,926 | `GO_INTERNAL` | 21/21 | 4/4 |
| **total** | **21** | **1,718,285** | **8,795,698** | **5/5** | **125/125** | **21/21** |

## Control and build replay

After every hostile-review repair, all five canonical verifiers were run in
fresh Python processes with bytecode disabled.  Their stdout was compared
byte for byte with the stored transcripts.  The five comparisons passed;
the transcript SHA-256 values are:

| paper | canonical verifier-transcript SHA-256 |
|---:|---|
| P127 | `53ec418b88941cad406b24cca6837818a36e69ed3ebb0194219b4c09fbea67b1` |
| P128 | `3b5e5bbbe94ec7ed7e689ff6a2cfeb2dc04a1ebc1ce9686c44194518ac1b1204` |
| P129 | `3e40359274ae4bb033db5efe16d463b28af3fcd7464f9589bc5b136626acd080` |
| P130 | `89b6142c21feac945f9d0dd362b5edf78aed78530596330be0c237e9088d60b4` |
| P131 | `caa4df1e70fd2bdb86aa5aeb1308c2baa74b5d5e560d73980f1f6886c91bc8c6` |

Every manuscript also passed an isolated four-stage LaTeX/BibTeX build using
only its frozen source and bibliography inputs.  Settled logs contain no
actual LaTeX/package warning, undefined citation/reference, multiply defined
label, overfull/underfull box, fatal error, or actionable rerun request;
BibTeX reports `warning$ -- 0`.  Each isolated PDF reproduces its frozen
`main.pdf` byte for byte.

## Bibliography, PDF, text, and visual gates

The paper-local bibliography closures are 7/7, 6/6, 8/8, 8/8, and 6/6, for
**35/35 cited and resolved entries**.  All PDFs are A4, unencrypted, rotation
zero, date-free, JavaScript-free, form-free, attachment-free, and have empty
PDF Title, Author, Subject, and Keywords fields.  There are no embedded raster
images.

All **125/125** font rows are embedded, subsetted, and Unicode-mapped.  A
fresh `pdftotext -layout` extraction over the five final PDFs contains
**98,407 bytes** in **1,307 lines**.  Each of the 21 pages has nonempty
extractable text.  Scans contain no unresolved-reference, placeholder,
TODO/FIXME, or verification marker.  The sole `PILOT_ONLY` occurrence is the
explicitly excluded P129 maximum-endpoint observation, and each manuscript
contains its external-HOLD boundary.

All **21/21** final pages were rendered and inspected page by page.  Titles,
anonymous author lines, abstracts, theorem statements, proofs, tables,
equations, owner boundaries, conclusions, and references are legible.  No
page has clipping, overlap, missing glyphs, malformed displays, unexpected
blank space, accidental blank pages, or rotation.

## Integrity gate

The five paper-local `SHA256SUMS` files cover **103 frozen evidence files**
and pass entry by entry.  Their own SHA-256 values are:

| paper | manifest entries | `SHA256SUMS` SHA-256 |
|---:|---:|---|
| P127 | 19 | `15ef5f07e01618ce714f3050b6fda95213d01b10f86c317970bbb57eb19671d8` |
| P128 | 19 | `549a7f2eb60ab99d411d38b58baf6743b95a821e880435a756e18fd677277707` |
| P129 | 27 | `60676182dfd96e1bc8258ee3ec24c3f4cec669d09454ed761db94f14cc38775a` |
| P130 | 19 | `ba6898d96a5e9d2c60c8b81937b337b1471c81b352f438641d8abb9db2f9b929` |
| P131 | 19 | `1688f832446b7ae3ac99abce7966273a2d206a0bb0086d5932ad5d3c1602b147` |

The five canonical PDF digests are frozen in
`CANONICAL_PDF_MANIFEST.sha256`, which passes 5/5.  Its SHA-256 is
`857383775d74fef58ae832284e695fd97bf544560bd2d1c54d2ed8211482071e`.

This report certifies internal theorem-package consistency, reproducibility,
and artifact mechanics only.  External release, novelty, priority,
authorship, posting, submission, and specialist contact remain **HOLD**.
