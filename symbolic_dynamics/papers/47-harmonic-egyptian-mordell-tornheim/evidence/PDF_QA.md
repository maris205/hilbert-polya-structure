# P47 final PDF quality assurance

Writer-side status: `PASS`.

The final artifact is `main.pdf`, byte-identical to `main_round2.pdf`, with
SHA-256
`b6c4d6aa27fe23f74b4c9e63628cd9b34b83d1d4d0908b040cc923af4c0ae12d`.
All checks below were run inside the writer candidate after the independent
visual-HOLD repair.  The writer handoff remains
`HOLD_FOR_INDEPENDENT_WRITER_AUDIT` until a fresh external recheck.

## Fixed-epoch reproducibility

Two clean builds used `SOURCE_DATE_EPOCH=1787011200`, `TZ=UTC`, and
`LC_ALL=C`.  They reproduced all three final build products byte for byte:

- PDF SHA-256:
  `b6c4d6aa27fe23f74b4c9e63628cd9b34b83d1d4d0908b040cc923af4c0ae12d`;
- bibliography SHA-256:
  `dd828b408bbe3bb486a8d8ea7fc8794d9c6759ac564176befae50dadf5a235dc`;
- compile-log SHA-256:
  `23cf89d34d194a01ff9a4c3bcd3611670099f7286bccc121c336dbf89e7973d2`.

The final log has zero LaTeX/package warnings, undefined citations,
undefined references, and overfull or underfull boxes.

## Format and fonts

- 14 pages, each A4 (`595.276 x 841.89 pt`), with no rotation;
- 29 font records;
- every font embedded, subsetted, and Unicode mapped;
- zero Type 3 fonts;
- no encryption, form field, JavaScript, or suspect-object flag.

## Text extraction

Default, layout, and raw `pdftotext` modes decoded strictly as UTF-8.  Their
character counts were respectively 33,987, 45,847, and 33,578.  Each mode
contained:

- zero illegal C0/DEL/C1 characters (standard form-feed page separators
  excluded);
- zero replacement characters;
- zero `??`, `[?]`, `VERIFY`, `TODO`, or `FIXME` markers;
- 14 standard form-feed page separators.

The pre-repair Round-1 PDF contained 13 illegal C0 glyph mappings emitted by
extensible mathematical delimiters.  Replacing those delimiters with fixed
parentheses changed no formula or claim and reduced all three illegal-control
counts to zero.  `main_round1.pdf` is retained only as review history; the
final publication candidate is the hash above.

## Bounding boxes

Both `pdftotext -bbox` and `pdftotext -bbox-layout` produced well-formed
XHTML for 14 pages and exactly 6,490 word boxes.  In both modes, zero boxes
had reversed coordinates or extended outside the page rectangle (tolerance
0.01 pt).

## Page-by-page visual inspection

All 14 pages were rasterized at 170 dpi and inspected individually.

- pages 1--4: title, abstract, theorem statements, equations, and section
  transitions are complete and unclipped;
- page 5: the two-coordinate TikZ figure is fully inside the text block, both
  branches and arrow labels are legible, and the typed-object table aligns;
- pages 6--8: proof displays, strict endpoint notation, and trace formulas
  are legible with no collisions;
- page 7: each of the three color bands has its label in clear white space
  above the band; the open endpoints and the ticks at `0`, `1/2`, and `1`
  remain distinct; and the strict-wall explanation occupies a separate white
  callout to the right of the axis, clear of both the ticks and the
  `no bounded operator` label.  The diagram remains understandable from its
  stacked positions, labels, and open endpoints, independent of color;
- pages 9--10: determinant normalization is rendered correctly, the mixed
  triangle and negative-minor inset do not overlap, and the canonical replay
  table appears after the Section 8 heading;
- pages 11--14: references, four appendix sections, long hashes, and the
  final page all remain within bounds and readable.

There is no clipping, overlap, missing figure/table, blank page, truncated
caption, or unreadable label.  The read-only checker
`scripts/check_pdf_qa.py` also returns
`paper47.writer-pdf-qa.v1 / PASS` with the same counts.

## Superseded visual-HOLD anchors

The prior PDF was rejected by the independent writer audit because Figure 2
placed thick bands through three labels and placed the strict-wall note over
axis material.  The repair changed only that vector layout; its mathematical
thresholds, open endpoints, band extents, color semantics, and caption remain
unchanged.  The following prior anchors are withdrawn and must not be used:

- PDF SHA-256
  `bb30f866ecac88b8b5467dadecef968daa60dc9383af46eea0e7e5602a794eb0`;
- writer-seal SHA-256
  `cfb71220d7838d92345d9df70d47e6f2d669607a794cf1f2ee78b7a07f81f5b0`.

This record is writer-generated evidence.  It does not pre-empt the required
fresh audit of the new anchors.
