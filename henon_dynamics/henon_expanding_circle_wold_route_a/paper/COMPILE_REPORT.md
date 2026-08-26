# C177 compile report

- Engine: LuaHBTeX 1.14.0.
- Fixed epoch: `SOURCE_DATE_EPOCH=1787702400`, `FORCE_SOURCE_DATE=1`, `TZ=UTC`.
- Command: `lualatex --interaction=nonstopmode --halt-on-error main.tex` in fresh isolated directories.
- Final PDF: two A4 pages.
- Two fresh final builds were byte-identical; their bytes are released as both `main.pdf` and `main_round2.pdf`.
- Round-0 SHA-256: `017d31862b5b2524be13bddd01167217de4ff2daf1f6a9a9ee2689ffa67d9b21`.
- Round-1 SHA-256: `cbc113e35670dcde07b538cadca9ce2874f0581a3f92c9bf5b28bb92344040c8`.
- Final/main-round2 SHA-256: `7ff51b4deb6c31f2eb2c7eac52850de79bb91bf1d20460bc7ae3fa0be20e5069`.
- The three round hashes are pairwise distinct; `main.pdf` and `main_round2.pdf` are byte-identical.
- `pdffonts` reports every listed font embedded and subset.
- Both fresh logs contain no warning, overfull/underfull box, missing glyph, undefined reference/citation, rerun request, or multiply defined label.
- Visual audit of both rendered pages found legible English and Chinese text, intact equations/table/declarations, normal margins and page numbers, and no clipping, collision, truncation, malformed glyph, or unintended blank page.

Build auxiliaries are excluded from the manifest and release.
