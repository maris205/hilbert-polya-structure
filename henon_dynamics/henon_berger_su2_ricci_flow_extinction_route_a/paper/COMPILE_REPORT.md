# Compile report: HCS-C360

The three revision products are compiled from `main.tex` with LuaLaTeX at
fixed epoch `1788480000`.  Each checked PDF must match two independent fresh
two-pass builds.  The frozen products are:

- Round 0: 2 pages, 15 font rows, SHA-256
  `fab8de150b1457f8db34ca79d2ca2d208998356eecec770e39fe5b00f4b834b5`;
- Round 1: 2 pages, 15 font rows, SHA-256
  `3b4391516a0a3e90b162f3cd2a4272ff155dc27a0bdf5ebc451993ef90aeac1d`;
- Round 2/final: 3 pages, 15 font rows, SHA-256
  `7bfdff28366ad0d123631254cefc55d233164bfbe93c6ff12e3e230226926c38`.

The release audit requires three distinct revision digests,
`main.pdf == main_round2.pdf`, no LaTeX/package/PDF-backend warning,
overfull/underfull box, undefined reference, rerun request, or missing
character in the settled log; all fonts embedded and subset; clean UTF-8 text
extraction without draft tokens; and successful rasterization of every page.

The final manifest records exact byte sizes, page counts, font rows, and
raster receipts after the release write.
