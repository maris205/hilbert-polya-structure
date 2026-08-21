# C88 compile report

Status: `PASS`.

Two isolated `latexmk` builds under `SOURCE_DATE_EPOCH=0`, `TZ=UTC`, and
`LC_ALL=C` produced byte-identical two-page PDFs.  The final TeX log is also
byte-identical across builds.

PDF SHA-256:
`d8341a25856ac4d26de0a6398c39c625f8475ab624a923e498fa81a4fca1125b`.

The final artifact passes embedded-font, undefined-reference/citation,
overfull/underfull box, extracted-text placeholder, page-count, raster
nonblank-pixel, and page-by-page visual inspection checks.  The numerical
table, equations, evidence hash, and scope statement fit within both page
boundaries without overlap.
