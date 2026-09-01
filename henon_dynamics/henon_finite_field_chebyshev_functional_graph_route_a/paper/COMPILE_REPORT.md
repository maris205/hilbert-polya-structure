# Compile report

- LuaLaTeX, two settled passes per build, with `SOURCE_DATE_EPOCH=1788134400`.
- Each of the three content rounds was compiled in two fresh directories; every same-round pair was byte-identical.
- Round SHA-256 values are `81b38a2277a4e593a89082ea9a4161d14eeafceea39c3be764b7a33c6ed7432e`,
  `cee059de35dfb9e0d98f298a08aee59c780343d5228d6f995c6711cf7835e8eb`, and
  `c966e31fe276300869a18ff7460952f850b7810e1cc0d4df3481d62da0fd5e0a`.
- `main.pdf` is byte-identical to round 2, SHA-256
  `c966e31fe276300869a18ff7460952f850b7810e1cc0d4df3481d62da0fd5e0a`.
- Final PDF: 3 pages, 187,584 bytes; all 25 fonts are embedded and subset.
- The settled log is warning-free: no LaTeX/package warning, undefined reference, rerun request,
  overfull box, or underfull box.  The `rerunfilecheck` textual occurrence is package metadata only.
- All three final pages were rendered at 110 dpi and visually inspected; equations, theorem/proof,
  strengthened field-model receipt, repaired Route-A tuple, hyperlinks, margins, references, and page breaks are intact.
