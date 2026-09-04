# Compile report

- Engine: LuaLaTeX, two passes per build.
- Fixed environment: `SOURCE_DATE_EPOCH=1788393600`, `FORCE_SOURCE_DATE=1`, `TZ=UTC`.
- Round 0: 2 pages, 17 font rows, SHA-256 `666cfcfb62be5a806b1946668f672f7a1e240855ac5be133dc0821491ceb02b4`.
- Round 1: 3 pages, 18 font rows, SHA-256 `8ddd4ad219cd4f60f20467f5991c36478a259cb32ed15e4f3485c41140a1f1f4`.
- Round 2/final: 3 pages, 20 font rows, SHA-256 `a7d1af8d688e66dbc87785b70827b3865d509eaa88876404adbd3c2d2ce460cf`.
- Every round is byte-identical across two fresh build directories.
- `main.pdf` is byte-identical to `main_round2.pdf`.
- Settled logs: 0 LaTeX/package/PDF-backend warnings, 0 overfull/underfull boxes, 0 undefined references/citations, 0 missing glyphs.
- Fonts: every reported font embedded and subset.
- Text gate: Poppler's known unmapped Computer-Modern math bytes `0x01`, `0x12`, and `0x13` are normalized after visual inspection; no other control characters, literal `qquad`, `??`, `[VERIFY]`, TODO/FIXME, or missing-glyph sentinel occur.
- Raster gate: every page renders above the minimum byte threshold.
- Visual inspection: all 3 final pages PASS; equations, theorem items, references, and page breaks are legible with no clipping or sparse orphan page.
