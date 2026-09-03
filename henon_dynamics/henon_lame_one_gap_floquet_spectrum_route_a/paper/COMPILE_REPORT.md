# HCS-C340 compile report

All three revisions were built with LuaLaTeX twice from fresh directories at
`SOURCE_DATE_EPOCH=1788393600`; each pair was byte-identical.

| revision | pages | font rows | SHA-256 |
|---|---:|---:|---|
| round 0 | 2 | 11 | `80b2f27455d8123fe14b069dcf9db86ab2584b5b0ca6bdcb9ddd24249de19c06` |
| round 1 | 2 | 11 | `8d7ab2a1e83c2ddf1638fef6be9642b82d64255b147efb9e75d3aa66234312aa` |
| round 2/final | 3 | 11 | `64f9670e95d464398cc88b15abe1a14a905627cd83b17d22400dc07797dcf414` |

Settled logs contain no LaTeX/package warning, overfull/underfull box,
undefined reference/citation, rerun request, or missing-character report.
All fonts are embedded and subset.  Text extraction contains the three
round-specific sentinels and no forbidden control byte or drafting literal;
every page rasterizes successfully.  `main.pdf` is byte-identical to round 2.
