# Compile report

Final build date: 2026-08-26.

Command:

```bash
SOURCE_DATE_EPOCH=1787760000 TZ=UTC latexmk -lualatex -interaction=nonstopmode -halt-on-error main.tex
```

Final artifact:

- pages: 3, A4;
- bytes: 209,881;
- SHA-256: `ed64388d59e5717f588ec6b750c079eeb3aa99df4879236d2bb18ea3fb6c4a93`;
- `main.pdf == main_round2.pdf`: yes;
- clean rebuild hash equality: pass;
- all fonts embedded: pass (`pdffonts` reports `emb=yes` for every row);
- unresolved citations/references in final log: 0;
- missing glyphs in final log: 0;
- overfull boxes in final log: 0;
- visual inspection: all three pages checked; formulas, tables, bilingual abstract, margins, and references are legible with no clipping or overlap.

Round PDF hashes are recorded in `PAPER_IMPROVEMENT_LOG.md`. The first clean pass naturally requested cross-reference reruns; `latexmk` completed the required second pass, and the final log is clear. Transient `.aux`, `.log`, `.out`, `.fdb_latexmk`, and `.fls` files are removed after closure and excluded from the manifest.
