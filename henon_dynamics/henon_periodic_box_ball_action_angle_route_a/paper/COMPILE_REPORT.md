# C182 compile report

- Engine: LuaHBTeX 1.14.0 (TeX Live 2022/dev/Debian).
- Fixed environment: `SOURCE_DATE_EPOCH=1787702400`, `FORCE_SOURCE_DATE=1`, `TZ=UTC`.
- Each paper round used two `lualatex --interaction=nonstopmode --halt-on-error` passes.
- Round 0: three A4 pages, SHA-256 `6cd30103a96ce502473451a7638208aee94b136112aca30c757c3e32adc9f3a7`.
- Round 1: three A4 pages, SHA-256 `dc125ab4798070c7d4ed51d3729a6a6b7b2f7494f621a611bef02a3a1c48ae29`.
- Round 2/final: four A4 pages, SHA-256 `3cc392c7ebbd40c72920054aeef3ac0b71559b255b3cecccd9daecac066acbfc`.
- The three round hashes are pairwise distinct.  `main.pdf` and `main_round2.pdf` are byte identical.
- Two fresh isolated directories each compiled the final source twice.  Both fresh PDFs were byte identical to each other and to the released final PDF, with the final hash above.
- `pdffonts` reports every listed font embedded and subset in all three round PDFs and both fresh final PDFs.
- Final and round logs contain no LaTeX/package warning, overfull/underfull box, missing glyph, undefined reference/citation, rerun request, or multiply defined label.
- Rendered snapshots of every page in all three rounds were inspected.  English and Chinese text, equations, bibliography, declarations, margins, and page numbers are legible; no clipping, collision, truncation, malformed glyph, unintended blank page, or missing element was found.

All build auxiliaries are excluded from the manifest and removed from the package disk closure.
