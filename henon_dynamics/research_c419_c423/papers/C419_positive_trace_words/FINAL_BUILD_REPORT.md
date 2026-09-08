# C419 final build and all-page inspection

2026-09-08 UTC. PASS for the final same-input build pair and PDF inspection.
This is a production gate, not a mathematical computation, human peer review,
worldwide-priority certificate, or batch seal.

## Reviewed inputs

The coordinator read both complete manuscript reviews, including all 391 lines
of round two. All three accepted round-one suggestions were verified closed;
there are zero outstanding mandatory corrections or new revision requests.
The fourteen production TeX/Bib inputs were compared with snapshots/round1/
before and after building; all comparisons passed. No production input was
edited after the second review. The recorded final input manifest is
builds/final1/source_inputs.sha256, SHA256
b8f2efb7257549fe94f83f6fee4f2918dbb1ff55e79dccf2d4a39deebd70ff3c.

The reviewed 11-page PDF remains unchanged in builds/round1/main.pdf, SHA256
eaeee202c03e9b25c67a53c98199027297f96fe64baf670f235a249d5a41215d.
All baseline and author-polished sources, PDFs and logs are retained.

## Actual fresh builds and identity

Both final directory names and the root main.pdf alias were confirmed absent.
The two new empty directories were created without copied auxiliary files.
From this paper directory, the following command was run separately with
DIR equal to builds/final1 and builds/final2, using Bash pipefail:

```bash
env SOURCE_DATE_EPOCH=1788825600 FORCE_SOURCE_DATE=1 TZ=UTC LC_ALL=C \
  latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error \
  '-usepretex=\pdftrailerid{}' -jobname=main -outdir=DIR main.tex \
  2>&1 | tee DIR/compile_console.log
```

DIR is an explanatory placeholder for those two literal command arguments.
Both actual latexmk invocations exited 0, converging in three pdfTeX passes
and two BibTeX passes each. The installed latexmk 4.76 and pdfTeX
3.141592653-2.6-1.40.22 (TeX Live 2022/dev/Debian) were used, without
installation or upgrades. The build-only preamble omits the automatic PDF
trailer ID; it does not edit the reviewed source or postprocess a PDF.
The stored creation/modification instant is 2026-09-08 00:00 UTC;
the local Poppler display renders it as 08:00 CST.

Both final PDFs contain 11 pages and 346075 bytes, SHA256:

```text
8089cac2f3826f5813a7153038d217ff744af3a159ec4d288dd098f411ef2723
```

Actual cmp of the two PDFs and the two generated bibliography files exited 0.
The newly extracted final -layout text also compared exactly with a fresh
same-option extraction of the approved reviewed PDF. A read-only stream
comparison omitting only the 75 characters of the reviewed PDF's trailer ID
line, while retaining its newline, compared exactly with the final PDF:

```bash
cmp builds/final1/main.pdf \
  <(sed -E 's@^/ID \[<[^>]+> <[^>]+>\]$@@' builds/round1/main.pdf)
```

That diagnostic exited 0 and wrote neither PDF. No content, font, layout or
formula changed. There was no failed C419 final pair; the metadata setting
was used from the first final build based on the earlier C421 diagnosis.
The final root main.pdf was newly copied from final1 after byte comparisons;
no existing root alias was overwritten.

## Diagnostics and all-page visual check

Final main.log and main.blg files in both directories were scanned for actual
warnings, undefined references/citations, errors and overfull/underfull boxes:
zero matches. Early convergence warnings remain honestly in console logs;
they are absent from the final logs. Literal placeholder/unknown-reference
markers in final extracted text also yielded zero matches. For these rg
commands, exit 1 means no match, not a compilation failure.

The PDF is unencrypted PDF 1.5, letter size, with no form or JavaScript.
All 19 font entries are embedded, subset, Unicode-mapped Type 1 fonts.
Final1 was newly rendered at 100 dpi by pdftoppm (exit 0), and the coordinator
actually opened all eleven images, page-01.png through page-11.png.

Pages 1–3 contain the title, theorem, source table and coordinate conventions;
pages 4–6 contain the separator, descent, small-set argument and realization;
pages 7–9 contain the repaired same-page formula, level tables and exact
ordinary-cycle proof; pages 10–11 contain backward escape, limitations and all
seven references. Every page is legible, with no clipping, overlapping text,
missing glyph or lost argument. Table 3 still floats before the completed
realization paragraph, as explicitly accepted in both review and revision.

Final log SHA256 values are:

- final1/main.log: 2ff385b776eb086b8718c5ccc6488a8d3f6830be6200250bf98e23e8feb98a16
- final2/main.log: 951a0cb1281f29c039baced9ea920bb45b0e50114161b7294bf6116db2323c0a

Logs are not claimed identical; their build-directory bookkeeping differs.
No old mathematical program, source search or external review was run for
this production task. Formal evaluation and exact batch sealing have their
own records. The paper-compile and batch-release requirements supplied the
fresh-build, diagnostic and all-final-page gates applied here.
