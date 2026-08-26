# Compile report

Final build date: 2026-08-26.

Command:

```bash
SOURCE_DATE_EPOCH=1787760000 TZ=UTC latexmk -lualatex -interaction=nonstopmode -halt-on-error main.tex
```

Final artifact:

- pages: 3, A4;
- bytes: 202,814;
- SHA-256: `7db8d34f3107f78dcfe7dbcff63b2f422dc48b0f8c18a23df0fb1281edd1e617`;
- `main.pdf == main_round2.pdf`: yes;
- clean rebuild hash equality: pass;
- all fonts embedded: pass;
- unresolved citations/references in final log: 0;
- missing glyphs in final log: 0;
- overfull boxes in final log: 0;
- visual inspection: all three pages checked. A clipped round-2 limitations heading was detected visually, replaced by an explicit margin-safe heading, rebuilt, and rechecked; final formulas, tables, bilingual abstract, margins, and references have no clipping or overlap.

The first clean pass requested the normal cross-reference rerun; `latexmk` completed it and the final log is clear. Transient TeX files are excluded from the manifest and removed after validation.
