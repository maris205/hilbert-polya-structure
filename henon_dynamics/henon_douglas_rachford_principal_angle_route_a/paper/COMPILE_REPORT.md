# C197 compile report

The final round-2 manuscript is built with LuaLaTeX under a fixed
`SOURCE_DATE_EPOCH`.  Release closure records the exact PDF SHA-256 and byte
size in `C197_RELEASE_MANIFEST.json`.

Required checks:

- round 0, round 1 and round 2 PDFs are content-distinct;
- `main.pdf` is byte-identical to round 2;
- two clean rebuilds from `main.tex` reproduce the final hash;
- all fonts are embedded;
- the final log has no warnings, undefined references or bad boxes;
- `pdftotext` retains theorem and scope language;
- every page is rendered and visually inspected.

The final page count and hashes are filled by the release manifest rather than
copied manually into this report, avoiding a self-referential rebuild cycle.
