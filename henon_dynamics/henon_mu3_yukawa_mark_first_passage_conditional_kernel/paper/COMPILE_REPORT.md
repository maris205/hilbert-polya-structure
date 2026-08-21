# C98 compile report

Two isolated build directories each ran two `pdflatex` passes with
`SOURCE_DATE_EPOCH=1787300000`, `FORCE_SOURCE_DATE=1`, `TZ=UTC`, and
`LC_ALL=C`.  Their PDFs were byte-identical.

- Pages: 2, US Letter.
- Fonts: all listed fonts embedded and subsetted.
- References: no unresolved references or citations.
- Layout log: no overfull or underfull box warnings.
- Extracted text: title, kernel theorem, counts, audit hash, and firewall present.
- PDF SHA-256: `774fa65062106e611c3d597b56aa4865a341f880263b1431bc4a6661f5820cfb`.
