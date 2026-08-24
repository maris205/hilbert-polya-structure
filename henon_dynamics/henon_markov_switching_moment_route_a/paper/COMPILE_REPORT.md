# Compile report — C117

- Engine: `latexmk -pdf` / pdfTeX with `SOURCE_DATE_EPOCH=0`, `TZ=UTC`.
- Isolated build A: 2 pages, SHA-256
  `415b3adca4549d3e9c8bbdbbcc72539171e11a69063af0614b1bcbf049ace83e`.
- Isolated build B and the checked-in `main.pdf`: the identical SHA-256.
- Fonts: every row reported by `pdffonts` is embedded.
- Final log: no overfull/underfull box, undefined reference/citation, or
  multiply-defined label diagnostic.
- The three release snapshots are byte-identical because the two internal
  prose corrections were incorporated before the frozen deterministic build;
  their semantic changes are recorded in `PAPER_IMPROVEMENT_LOG.md`.
