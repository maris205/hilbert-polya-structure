# C97 compile report

Two isolated build directories each ran two `pdflatex` passes with
`SOURCE_DATE_EPOCH=1787300000`, `FORCE_SOURCE_DATE=1`, `TZ=UTC`, and
`LC_ALL=C`.  Their PDFs were byte-identical.

- Pages: 2, US Letter.
- Fonts: all listed fonts embedded and subsetted.
- References: no unresolved references or citations.
- Layout log: no overfull or underfull box warnings.
- Extracted text: title, theorem, audit hash, and scope firewall present.
- PDF SHA-256: `7c52b3081c1941b8c18aec7cfce89e2a95f4f85581e6135505061af0260422b1`.
