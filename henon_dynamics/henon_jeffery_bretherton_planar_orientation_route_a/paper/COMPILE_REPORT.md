# Deterministic compile and visual report

- Engine: LuaLaTeX.
- Locked environment: `SOURCE_DATE_EPOCH=1788220800`,
  `FORCE_SOURCE_DATE=1`, `TZ=UTC`.
- Each round was compiled for two passes in each of two fresh directories.
- The two fresh builds of every round were byte-identical.
- Settled second-pass logs were warning-free: no layout, citation, reference,
  destination, missing-character, or rerun warnings.
- Every font row in every archived PDF is embedded and subset.
- `pdftotext` recovers the theorem, source-use statement, receipt, Route-A
  tuple, strict nonclaims, scope literal, and both DOI records.
- All eight rendered pages across the three archives were visually inspected;
  no clipping, overlap, missing glyph, broken formula, or unreadable table was
  found.  The first hostile rebuild exposed a literal `qquad` in the paired
  Cayley--Hamilton display; its missing backslash was repaired before the
  locked rebuild.  Round 1 deliberately leaves reference whitespace after its
  new theorem layer; the final round compacts the complete audit into three
  pages.
- Font audit totals are 14/15/19 rows for rounds 0/1/2; every row is embedded
  and subset.  Extracted word counts are 871/1170/1382 and increase strictly.

| revision | pages | SHA-256 |
|---|---:|---|
| round 0 original | 2 | `28422d18428447a0e40e9502efa30d58365ce6bed968b2143eb127b04bbc22f4` |
| round 1 | 3 | `92de1db47228be078b5cac565376cbbde312fb3d5f2c4433195c8b2246add677` |
| round 2 | 3 | `768d840bfbde6ceb4632bc1d48c10faea5ec267c743e190986824dc467a81035` |
| final (`main.pdf`) | 3 | `768d840bfbde6ceb4632bc1d48c10faea5ec267c743e190986824dc467a81035` |

The three revision hashes are distinct and the final PDF equals round 2
byte-for-byte.
