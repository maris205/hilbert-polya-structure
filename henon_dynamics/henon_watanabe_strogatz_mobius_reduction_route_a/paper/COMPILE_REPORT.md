# C189 compile report

Status: PASS.

- Engine: LuaLaTeX, two passes, `SOURCE_DATE_EPOCH=1787788800`,
  `FORCE_SOURCE_DATE=1`.
- Final PDF: 2 pages, 187,133 bytes.
- Final SHA-256:
  `e84da7cdccc10df2f468035199612043c72e4e65715b0d4a6830b2234211e68a`.
- Round hashes are pairwise distinct:
  - round 0:
    `8de2c76de294a8d3655456bfa86aa57833d2a91f83edd2281c09be915af253c7`;
  - round 1:
    `9293b851164d967bfbbec43ca580a81a604c696145cdaa86962abc23d1db077b`;
  - round 2/final:
    `e84da7cdccc10df2f468035199612043c72e4e65715b0d4a6830b2234211e68a`.
- Round 0 contains the group-lift skeleton; Round 1 adds cross-ratio and
  collision-stratum closure; Round 2 adds the hostile boundary, evidence
  ledger, and strict Route-A stop.
- Two clean fresh-directory, two-pass builds reproduced the final PDF byte
  for byte.
- Final and fresh log scans contain no LaTeX/package warning,
  overfull/underfull box, undefined reference, missing glyph, or fatal
  finding.
- `pdffonts`: every font is embedded and subset.
- Visual inspection: both rendered pages are complete, legible, balanced,
  non-overlapping, and free of clipping or blank regions.  The Riccati sign,
  `SU(1,1)` matrix, cross-ratio table, fixed-root equation, elliptic projected
  period, evidence counts, and all three DOI records were checked at rendered
  resolution.

Drafting improvements and visual checks are internal workflow artifacts, not
external peer review.
