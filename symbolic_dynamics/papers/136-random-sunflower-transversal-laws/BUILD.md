# P136 build and artifact QA

## Status

`ROUND1_COMPILE_PASS / REVIEW_A_ARTIFACT_QA_PASS / HOLD_EXTERNAL`

Build date: 2026-08-31 UTC. The manuscript was built with pdfTeX from TeX Live
2022 using the clean-build stable five-stage sequence:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

All five stages exited 0. The final `main.log` contains no match for
`Warning`, `undefined`, `Overfull`, `Underfull`, or `Error`.

## Round-0 frozen artifacts

| artifact | pages | bytes | SHA-256 |
|---|---:|---:|---|
| `main_round0_original.pdf` | 4 | 264412 | `0668f9b434aad2747a3d887d0a8fa6f6e36885a41b9f27f6182ee2d6a15192ef` |

At the original freeze, `main.pdf` compared byte-for-byte with the retained
round-0 artifact. Source hashes at that freeze were:

```text
3df23e090bdac913669568e1883896d56af6e57ae29b8331c9791b5f35b53c7e  main.tex
35fe00f055e0f1417d293d5e5328166d2f90044929de1bb691d11127f9a753c4  references.bib
```

## Round-0 metadata and format QA

- A4 page size: `595.276 x 841.89 pt`.
- PDF version: 1.5; unencrypted; no metadata stream or custom metadata.
- Title, author, subject, and keywords fields are blank.
- Technical creator/producer fields are `LaTeX with hyperref` and
  `pdfTeX-1.40.22`.
- 18 font entries are embedded, subsetted, and Unicode-mapped; no bad entry.
- `pdftotext` succeeds and returns 398 lines, 2031 words, and 12070 bytes.

## Round-0 page and text QA

All four pages were rasterized and inspected. The title/abstract, displayed
formulas, theorem endings, control table, and references are legible; no text
or equation is clipped, overlapped, orphaned, or outside the margins. An
initial visual pass found the literal token `qquad` in equation (7), caused by
a missing backslash. It was repaired, the full stable build was rerun, and
both extracted-text and page-image checks confirmed its removal before the
round-0 PDF was frozen.

## Round-1 Review-A rebuild

After implementing the one major and two minor findings in
`HOSTILE_REVIEW_A.md`, the stable five-stage sequence was rerun. Every stage
exited 0. The extra final LaTeX pass is required for clean-directory page-label
stability.  The final `main.log` has no match for `Warning`, `undefined`,
`Overfull`, `Underfull`, or `Error`.

| artifact | pages | bytes | SHA-256 |
|---|---:|---:|---|
| `main.pdf` | 4 | 265938 | `3cf06ca9b8b5cd829e20e99d6eafe32d45150b9eae2b60c61a1082e391f2be04` |
| `main_round1.pdf` | 4 | 265938 | `3cf06ca9b8b5cd829e20e99d6eafe32d45150b9eae2b60c61a1082e391f2be04` |

The round-1 files compare byte-for-byte. Current source/control hashes are:

```text
39724907724bf2f0bcc2e03b0dd5fb74aefeff8fb9f9d9c4bdea1edf00131170  main.tex
35fe00f055e0f1417d293d5e5328166d2f90044929de1bb691d11127f9a753c4  references.bib
0285c2c7f82540d421888f37bad0302a3a3fd106e916c1ad590018e927b51913  code/verify.py
5553c8c797bc4b577a6252959471f1e556e850cafcdf96d8a74b39353491271c  code/verification_output.txt
```

Round-1 artifact QA confirms A4 PDF 1.5, four pages, blank title/author/
subject/keyword metadata, no custom metadata stream, and 18 embedded,
subsetted, Unicode-mapped font entries. `pdftotext` returns 410 lines, 2157
words, and 12869 bytes. All pages were rasterized and inspected after the
repair; formulas, the expanded conditioning proof, the count/time limitation,
the exact-grid control table, and references are legible without clipping or
overlap. Extracted text contains no misleading “stopping clocks,” “clock law,”
“clock convolution,” “clocks add,” or “maximal-time” assertion. Its sole
wall-clock statement explicitly denies a convolution and gives the maximum
of component completion times.

## Round-B build closure

Review B found that a four-stage clean build already produced the correct PDF
but retained a page-label rerun request.  An additional final `pdflatex` pass
removed that request without changing the PDF bytes.  The five-stage recipe
above is therefore the canonical clean-build protocol.  No theorem source,
verifier, canonical stdout, or current PDF byte changed.

The repaired recipe was replayed in the isolated directory
`/tmp/p136r2iso.9IRUmo`: all stages exited zero, the settled log had no error,
undefined citation/reference, box warning, label-change warning, or rerun
request, and the isolated PDF compared byte for byte with `main.pdf` (`cmp=0`),
retaining SHA-256
`3cf06ca9b8b5cd829e20e99d6eafe32d45150b9eae2b60c61a1082e391f2be04`.

The independent Round-B closure repeated the same five stages from only the
two source inputs in `/tmp/p136rbclosure-final.kZEshT`.  It again obtained
`cmp=0`, the same PDF hash, and a warning-free settled log.  The resulting
review verdict is `GO_INTERNAL / HOLD_EXTERNAL` with no open finding.
