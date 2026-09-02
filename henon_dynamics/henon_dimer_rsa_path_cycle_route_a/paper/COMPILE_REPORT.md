# Compile report

The three substantive revisions were built with LuaLaTeX using two passes in
each of two isolated directories per round, `SOURCE_DATE_EPOCH=1788307200`,
`FORCE_SOURCE_DATE=1`, `TZ=UTC`, and the fixed PDF trailer in `main.tex`.
Both fresh builds of every round were byte-identical to each other and to the
archived artifact.  The final-round text contract includes the strict
JSON/YAML checker count `19,371` and hostile result `105/105`.

| round | role | pages | embedded/subset font rows | SHA-256 |
|---|---|---:|---:|---|
| 0 | original PGF/mean/cycle draft | 3 | 22 | `0a0d27c5341ea1eb04e31763c6eaf878f9281b95b5bce6137c34067c08123043` |
| 1 | factorial hierarchy/variance/support strengthening | 4 | 23 | `c797bca28272288017a5156ab16a15dbab7040a90e611aecaf1db2a78a2d594f` |
| 2 | executable integrity/Route/declarations closure | 5 | 24 | `b410ec70209302f891992712b4a6be16663e04d2a79cd6f7e4f1e762fef64a22` |

`paper/main.pdf` is byte-identical to `paper/main_round2.pdf` and has SHA-256
`b410ec70209302f891992712b4a6be16663e04d2a79cd6f7e4f1e762fef64a22`.
All three revision hashes are distinct.

The settled second-pass logs from all six builds contain no LaTeX/package
warning, overfull or underfull box, undefined reference, rerun request, or
missing-character event; in particular there is no overfull box above 10 pt.
`pdffonts` reports every row embedded and subset.  `pdftotext` preserves the
round-specific theorem/audit text contracts.  All 3, 4, and 5 pages were
rendered to PNG and visually inspected at 105 dpi: equations, tables,
references, margins, page breaks, and footers are legible, with no clipping,
collision, blank content page, or malformed glyph.
