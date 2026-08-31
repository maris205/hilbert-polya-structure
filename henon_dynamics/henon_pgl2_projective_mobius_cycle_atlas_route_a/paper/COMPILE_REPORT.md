# Compile report

- Engine: LuaLaTeX.
- Reproducibility environment: `SOURCE_DATE_EPOCH=1788048000`, `FORCE_SOURCE_DATE=1`, `TZ=UTC`.
- Each round: two LuaLaTeX passes in each of two fresh temporary directories.
- Round 0, round 1, and round 2 PDFs have distinct SHA-256 hashes.
- Final `main.pdf` is byte-identical to `main_round2.pdf`.
- Final page count: recorded by the release manifest.
- Fonts: all embedded and subset, checked by `pdffonts`.
- Text layer: required theorem, characteristic-two, Route-A, and scope literals checked by `pdftotext`.
- Visual audit: every final page rendered to PNG and inspected.
- Logs: no overfull/underfull boxes, undefined references, missing characters, or package warnings.
- Package cleanliness: no TeX sidecars or Python bytecode retained.

The final integrity pass anchored all three registered references in the
manuscript body.  Two fresh rebuilds were byte-identical, warning-free, and
visually rechecked; the retained final SHA-256 is
`b121a1e71b244b1447b53014105ae4378345b52b4f3d1df2199c16aee94c2dfe`.

The archived PDFs are release evidence; generated build directories were temporary and excluded.
