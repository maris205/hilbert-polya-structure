# C84 compile report

- Status: `PASS`
- Engine: `latexmk` with `pdflatex`
- Deterministic environment: `SOURCE_DATE_EPOCH=0 FORCE_SOURCE_DATE=1 TZ=UTC`
- Isolated builds: `2/2` byte-identical to the retained PDF
- PDF SHA-256: `2a37dacc711e5a42dc7b4a33f87d2cc47d31cae20cf05ac345ebcec198c2f4f0`
- Pages / size: `2 / 325463 bytes`
- Undefined references: `0`
- Undefined citations: `0` (the paper has no bibliography)
- Overfull / underfull boxes: `0 / 0`
- Fonts: all embedded and subsetted
- Text audit: no `??`, `[?]`, `[VERIFY]`, or hostile-marker residue
- Visual audit: both rendered pages inspected; tables, equations, hash, and
  margins are intact

The clean build's first pass emitted the normal `rerunfilecheck` request after
creating `main.out`; the second pass resolved it.  No warning remains in the
final `main.log`.
