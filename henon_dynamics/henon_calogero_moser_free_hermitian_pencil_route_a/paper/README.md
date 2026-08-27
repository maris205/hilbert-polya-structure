# C196 paper artifacts

`main.tex` is the final source.  The release preserves PDFs after the
baseline and two actual source revisions:

- `main_round0_original.pdf` -- signs, rank-one simplicity, Newton equations,
  completeness, and trace integrals;
- `main_round1.pdf` -- adds gauged intercepts and the global forward/inverse
  spectral atlas;
- `main_round2.pdf` -- adds both scattering ends, rank reversal, intercept
  preservation, aperiodicity, evidence totals, and the Route-A boundary;
- `main.pdf` -- byte-identical release copy of round 2.

LuaLaTeX supplies the bilingual abstract.  Builds use
`SOURCE_DATE_EPOCH=1787788800`, `FORCE_SOURCE_DATE=1`, and UTC.  Hashes, logs,
fonts, text extraction, determinism, and visual findings are in
`COMPILE_REPORT.md`.
