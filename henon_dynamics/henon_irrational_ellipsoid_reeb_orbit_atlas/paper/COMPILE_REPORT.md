# C242 compile report

- Engine: LuaLaTeX (two passes for each revision)
- Fixed environment: `SOURCE_DATE_EPOCH=1788048000`, `FORCE_SOURCE_DATE=1`,
  `TZ=UTC`, `LC_ALL=C`
- Revisions: `main_round0_original.pdf`, `main_round1.pdf`,
  `main_round2.pdf`; final `main.pdf` equals round 2 byte-for-byte
- Checks: PDF page count 2–6, embedded fonts, extracted-text keywords,
  undefined references/citations, and no build sidecars in the release tree
- Warnings: normal first-pass rerun notice only; final pass has no undefined
  references, missing citations, overfull boxes, or font warnings

The manuscript contains the exact two-orbit irrational theorem, integer-square
floor certificates, rational Morse--Bott boundary, and the locked
`ROUTE_A_REJECTED`/`NO_BAD_EULER_OR_ROOT_NUMBER` boundary.
