# C175 compile report

- Engine: LuaHBTeX 1.14.0.
- Fixed epoch: `SOURCE_DATE_EPOCH=1787702400`, `FORCE_SOURCE_DATE=1`, `TZ=UTC`.
- Command: two passes of `lualatex --interaction=nonstopmode --halt-on-error main.tex` in each fresh isolated directory.
- Final PDF: three A4 pages.
- Two fresh final builds were byte-identical to each other and to released `main.pdf`.
- Round-0 SHA-256: `fa962ffd7eba77e79626a02395be8ca46bae695e68984a57e02d24530c5996f7`.
- Round-1 SHA-256: `e3d3f10437fd6bb223a1f8ebc324f53d6078bac44644ba16fb4f4ac41b173373`.
- Final/main-round2 SHA-256: `be7df400f168b6665022994655ad7a04a452dac552b6741e232371880867f80d`.
- The three round hashes are pairwise distinct; `main.pdf` and `main_round2.pdf` are byte-identical.
- `pdffonts` reports every listed font embedded and subset.
- Fresh final logs contain no warning, overfull/underfull box, missing glyph, undefined reference/citation, rerun request, or multiply defined label.
- Visual audit of all three rendered page snapshots found legible English and Chinese text, intact formulas/table/declarations, normal margins and page numbers, and no clipping, collision, truncation, malformed glyph, or unintended blank page.

All build auxiliaries are excluded and absent from release.
